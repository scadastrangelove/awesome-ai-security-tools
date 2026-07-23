#!/usr/bin/env python3
"""Refresh static GitHub metrics in data/sections.json.

The README intentionally avoids live per-entry shields.io badges. Run this
script before a release to snapshot stars and default-branch last-commit dates.
It uses the GitHub GraphQL API in batches and needs an authenticated token from
GITHUB_TOKEN, GH_TOKEN, or `gh auth token`.
"""

from __future__ import annotations

from argparse import ArgumentParser
from datetime import UTC, datetime
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any
from urllib.error import HTTPError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "data" / "sections.json"
GRAPHQL_URL = "https://api.github.com/graphql"
BATCH_SIZE = 50


class MetricError(RuntimeError):
    pass


def iter_entries(data: dict[str, Any]):
    for section in data["sections"]:
        if "groups" in section:
            for group in section["groups"]:
                yield from group["entries"]
        else:
            yield from section["entries"]


def github_token() -> str:
    for name in ("GITHUB_TOKEN", "GH_TOKEN"):
        token = os.environ.get(name)
        if token:
            return token

    try:
        result = subprocess.run(
            ["gh", "auth", "token"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError) as exc:
        raise MetricError(
            "GitHub token not found. Set GITHUB_TOKEN/GH_TOKEN or run `gh auth login`."
        ) from exc

    token = result.stdout.strip()
    if not token:
        raise MetricError("`gh auth token` returned an empty token.")
    return token


def graphql(token: str, query: str) -> dict[str, Any]:
    body = json.dumps({"query": query}).encode("utf-8")
    request = Request(
        GRAPHQL_URL,
        data=body,
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/vnd.github+json",
        },
        method="POST",
    )

    try:
        with urlopen(request, timeout=60) as response:
            payload = json.load(response)
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise MetricError(f"GitHub GraphQL request failed: HTTP {exc.code}: {detail}") from exc

    if payload.get("errors"):
        raise MetricError("GitHub GraphQL returned errors: " + json.dumps(payload["errors"]))
    return payload["data"]


def repo_query(batch: list[str]) -> str:
    fields = []
    for index, repo in enumerate(batch):
        owner, name = repo.split("/", 1)
        fields.append(
            f"""
            r{index}: repository(owner: {json.dumps(owner)}, name: {json.dumps(name)}) {{
              stargazerCount
              pushedAt
              defaultBranchRef {{
                target {{
                  ... on Commit {{
                    committedDate
                  }}
                }}
              }}
            }}
            """
        )
    return "query RepositoryMetrics {\n" + "\n".join(fields) + "\n}"


def fetch_metrics(token: str, repos: list[str], snapshot: str) -> dict[str, dict[str, Any]]:
    metrics: dict[str, dict[str, Any]] = {}
    for offset in range(0, len(repos), BATCH_SIZE):
        batch = repos[offset:offset + BATCH_SIZE]
        data = graphql(token, repo_query(batch))
        for index, repo in enumerate(batch):
            item = data.get(f"r{index}")
            if item is None:
                raise MetricError(f"GitHub repository not found or inaccessible: {repo}")

            default_target = (item.get("defaultBranchRef") or {}).get("target") or {}
            updated_at = default_target.get("committedDate") or item.get("pushedAt")
            if not updated_at:
                raise MetricError(f"GitHub repository has no pushed/default-branch date: {repo}")

            metrics[repo] = {
                "stars": int(item["stargazerCount"]),
                "updated": updated_at[:10],
                "snapshot": snapshot,
            }
    return metrics


def main() -> int:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA,
                        help="structured JSON data path")
    args = parser.parse_args()

    try:
        with args.data.open(encoding="utf-8") as handle:
            data = json.load(handle)

        repos = list(dict.fromkeys(
            entry["repo"] for entry in iter_entries(data) if entry.get("repo")
        ))
        snapshot = datetime.now(UTC).date().isoformat()
        metrics = fetch_metrics(github_token(), repos, snapshot)

        for entry in iter_entries(data):
            repo = entry.get("repo")
            if repo:
                entry["metrics"] = metrics[repo]

        with args.data.open("w", encoding="utf-8") as handle:
            json.dump(data, handle, ensure_ascii=False, indent=2)
            handle.write("\n")

    except MetricError as exc:
        print(f"metrics error: {exc}", file=sys.stderr)
        return 2

    print(f"Updated {len(repos)} GitHub metric snapshots in {args.data}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
