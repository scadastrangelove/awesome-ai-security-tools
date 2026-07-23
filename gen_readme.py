#!/usr/bin/env python3
"""Generate the Awesome AI Security Tools README from structured JSON data.

GitHub stars and last-commit dates are rendered from static snapshots stored in
data/sections.json. Refresh them before a release with
scripts/update_github_metrics.py; the README itself does not call live badge
services for per-entry GitHub metadata.
"""

from argparse import ArgumentParser
from collections import Counter
import json
from pathlib import Path
import re
from typing import Any


GH = "https://github.com/"
HF = "https://huggingface.co/"

STATUS_BADGES = {
    "open_source": "🟢",
    "research": "🔬",
    "commercial_open": "🟠",
}
STATUS_ORDER = ("open_source", "research", "commercial_open")

WARNING_FLAGS = {
    "license_caveat",
    "no_license",
    "noncommercial",
    "copyleft",
    "abliterated_or_uncensored",
}
KNOWN_FLAGS = WARNING_FLAGS | {
    "early_stage",
    "archived",
    "heavy_runtime",
    "requires_api_key",
    "authorized_testing_only",
    "commercial_features",
}


class DataError(ValueError):
    """Raised when the structured data is invalid."""


def format_int(value: int) -> str:
    return f"{value:,}"


def github_metrics(entry: dict[str, Any]) -> str:
    metrics = entry.get("metrics")
    if not metrics:
        return ""
    parts = []
    if "stars" in metrics:
        parts.append(f"★ {format_int(metrics['stars'])}")
    if "updated" in metrics:
        parts.append(f"updated {metrics['updated']}")
    return f" *({' · '.join(parts)})*" if parts else ""


def latest_metrics_snapshot(data: dict[str, Any]) -> str | None:
    snapshots = [
        entry["metrics"]["snapshot"]
        for entry in iter_entries(data)
        if entry.get("metrics", {}).get("snapshot")
    ]
    return max(snapshots) if snapshots else None


def hf_model_url(model: str) -> str:
    return f"{HF}{model}"


def link(item: dict[str, str]) -> str:
    return f"[{item['label']}]({item['url']})"


def github_anchor(title: str) -> str:
    """Approximate GitHub's Markdown heading anchors for this README."""
    cleaned = re.sub(r"[^\w\s-]", "", title.lower())
    return cleaned.replace(" ", "-")


def entry_tags(entry: dict[str, Any]) -> str:
    statuses = entry.get("status", [])
    flags = entry.get("flags", [])
    tags = "".join(STATUS_BADGES[s] for s in STATUS_ORDER if s in statuses)
    if any(flag in WARNING_FLAGS for flag in flags):
        tags += "⚠️"
    return tags


def render_hf_model(entry: dict[str, Any]) -> str:
    model = entry["model"]
    url = entry.get("url", hf_model_url(model))
    tags = entry_tags(entry)
    org = f" *({entry['org']})*" if entry.get("org") else ""
    meta = []
    if entry.get("license"):
        meta.append(f"license: {entry['license']}")
    if entry.get("access"):
        meta.append(f"access: {entry['access']}")
    if entry.get("artifacts"):
        meta.append(f"artifacts: {entry['artifacts']}")
    note = f" *{' · '.join(meta)}.*" if meta else ""
    if entry.get("note"):
        note = f"{note} {entry['note']}" if note else f" {entry['note']}"
    return f"- **[{entry['name']}]({url})** {tags} — {entry['desc']}{org}{note}"


def render_entry(entry: dict[str, Any]) -> str:
    if entry.get("kind") == "hf_model":
        return render_hf_model(entry)
    if entry.get("kind") == "awesome_list":
        repo = entry["repo"]
        url = entry.get("url", f"{GH}{repo}")
        return f"- **[{entry['name']}]({url})** — {entry['desc']}{github_metrics(entry)}"
    repo = entry["repo"]
    url = entry.get("url", f"{GH}{repo}")
    tags = entry_tags(entry)
    org = f" *({entry['org']})*" if entry.get("org") else ""
    note = f" {entry['note']}" if entry.get("note") else ""
    line = f"- **[{entry['name']}]({url})** {tags} — {entry['desc']}{org}{note}{github_metrics(entry)}"
    out = [line]
    if entry.get("sources"):
        out.append("  - **Sources:** " + " · ".join(link(s) for s in entry["sources"]))
    if entry.get("related"):
        out.append("  - **Related:** " + " · ".join(link(r) for r in entry["related"]))
    return "\n".join(out)


def load_data(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    validate_data(data)
    return data


def iter_entries(data: dict[str, Any]):
    for section in data["sections"]:
        if "groups" in section:
            for group in section["groups"]:
                yield from group["entries"]
        else:
            yield from section["entries"]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise DataError(message)


def validate_data(data: dict[str, Any]) -> None:
    require(isinstance(data.get("sections"), list), "data.sections must be a list")

    repos = []
    models = []
    anchors = []

    for section in data["sections"]:
        title = section.get("title", "<untitled>")
        require("title" in section, "section is missing title")
        require("anchor" in section, f"section {title!r} is missing anchor")
        anchors.append(section["anchor"])
        has_entries = "entries" in section
        has_groups = "groups" in section
        require(has_entries != has_groups, f"section {title!r} must have exactly one of entries/groups")
        groups = section.get("groups")
        if groups is not None:
            require(isinstance(groups, list), f"section {title!r} groups must be a list")
            for group in groups:
                require("title" in group, f"section {title!r} has a group without title")
                require(isinstance(group.get("entries"), list),
                        f"group {group.get('title', '<untitled>')!r} entries must be a list")

    duplicate_anchors = [anchor for anchor, count in Counter(anchors).items() if count > 1]
    require(not duplicate_anchors, f"duplicate section anchors: {', '.join(duplicate_anchors)}")

    for entry in iter_entries(data):
        name = entry.get("name", "<unnamed>")
        kind = entry.get("kind")
        require("desc" in entry, f"entry {name!r} is missing desc")
        flags = entry.get("flags", [])
        require(isinstance(flags, list), f"entry {name!r} flags must be a list")
        unknown_flags = [f for f in flags if f not in KNOWN_FLAGS]
        require(not unknown_flags, f"entry {name!r} has unknown flags: {unknown_flags}")

        if kind == "awesome_list":
            require("repo" in entry, f"awesome list entry {name!r} is missing repo")
            repos.append(entry["repo"])
        else:
            statuses = entry.get("status")
            require(isinstance(statuses, list) and statuses,
                    f"entry {name!r} must have non-empty status")
            unknown_statuses = [s for s in statuses if s not in STATUS_BADGES]
            require(not unknown_statuses, f"entry {name!r} has unknown status: {unknown_statuses}")

        if kind == "hf_model":
            require("model" in entry, f"HF model entry {name!r} is missing model")
            models.append(entry["model"])
        elif kind != "awesome_list":
            require("repo" in entry, f"entry {name!r} is missing repo")
            repos.append(entry["repo"])

        for field in ("sources", "related"):
            for item in entry.get(field, []):
                require(set(item) == {"label", "url"},
                        f"entry {name!r} {field} items must contain label and url only")

        metrics = entry.get("metrics")
        if metrics is not None:
            require("repo" in entry, f"entry {name!r} has metrics but no repo")
            require(set(metrics) == {"stars", "updated", "snapshot"},
                    f"entry {name!r} metrics must contain stars, updated, and snapshot only")
            require(isinstance(metrics["stars"], int) and metrics["stars"] >= 0,
                    f"entry {name!r} metrics.stars must be a non-negative integer")
            for field in ("updated", "snapshot"):
                require(isinstance(metrics[field], str)
                        and re.fullmatch(r"\d{4}-\d{2}-\d{2}", metrics[field]),
                        f"entry {name!r} metrics.{field} must be YYYY-MM-DD")

    duplicate_repos = [repo for repo, count in Counter(repos).items() if count > 1]
    duplicate_models = [model for model, count in Counter(models).items() if count > 1]
    require(not duplicate_repos, f"duplicate repos: {', '.join(duplicate_repos)}")
    require(not duplicate_models, f"duplicate models: {', '.join(duplicate_models)}")


def build(data: dict[str, Any]) -> str:
    sections = data["sections"]
    latest_snapshot = latest_metrics_snapshot(data)
    out = []
    out.append("# Awesome AI Security Tools [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
    out.append("")
    out.append("> A curated list of **public-source, research, and commercial** tools for AI security and AI-assisted cybersecurity — autotriage, agent security, AI/ML supply chain, pentest agents, AI SAST, LLM-driven fuzzing, threat intelligence, SOC/SIEM triage, reverse engineering, LLM red-teaming, and more.")
    out.append("")
    out.append("[![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)")
    out.append("[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing)")
    out.append("")
    out.append("**Type legend:** 🟢 public source / open-source · 🔬 research (paper / benchmark / dataset / framework) · 🟠 commercial with open components · ⚠️ restrictive, non-commercial, or unclear/no license — check before use.")
    out.append("")
    snapshot_note = (f" Latest snapshot: {latest_snapshot}."
                     if latest_snapshot else " run `python3 scripts/update_github_metrics.py` before release.")
    out.append("GitHub-hosted entries show static **★ stars** and **last-commit** snapshots; refresh them with `python3 scripts/update_github_metrics.py` before release." + snapshot_note + " Hugging Face model entries show license, access, and artifact metadata. Ordering within a section favors flagship and actively maintained projects.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## Contents")
    out.append("")
    for section in sections:
        out.append(f"- [{section['title']}](#{section['anchor']})")
        for group in section.get("groups", []):
            out.append(f"  - [{group['title']}](#{github_anchor(group['title'])})")
    out.append("- [Contributing](#contributing)")
    out.append("- [License](#license)")
    out.append("")
    out.append("---")
    out.append("")

    for section in sections:
        out.append(f"## {section['title']}")
        out.append("")
        if section.get("intro"):
            out.append(section["intro"])
            out.append("")
        if "groups" in section:
            for group in section["groups"]:
                out.append(f"### {group['title']}")
                out.append("")
                for entry in group["entries"]:
                    out.append(render_entry(entry))
                out.append("")
        else:
            for entry in section["entries"]:
                out.append(render_entry(entry))
            out.append("")
        if section.get("footer"):
            out.append(section["footer"])
            out.append("")
        out.append("---")
        out.append("")

    out.append("## Contributing")
    out.append("")
    out.append("Contributions are welcome! This README is generated from structured data.")
    out.append("")
    out.append("1. Edit `data/sections.json` (validated by `data/schema.json`).")
    out.append("2. Use structured fields such as `status`, `flags`, and `license`; do not paste rendered emoji tags into the data.")
    out.append("3. Regenerate and check the README:")
    out.append("")
    out.append("```bash")
    out.append("python3 scripts/update_github_metrics.py")
    out.append("python3 gen_readme.py")
    out.append("python3 gen_readme.py --check")
    out.append("```")
    out.append("")
    out.append("Example entry:")
    out.append("")
    out.append("```json")
    out.append("{")
    out.append('  "name": "ExampleTool",')
    out.append('  "repo": "OWNER/REPO",')
    out.append('  "status": ["open_source"],')
    out.append('  "license": "MIT",')
    out.append('  "flags": ["early_stage"],')
    out.append('  "desc": "One factual sentence about what the tool does.",')
    out.append('  "related": [')
    out.append('    {"label": "Sibling tool", "url": "https://github.com/OWNER/SIBLING"}')
    out.append("  ]")
    out.append("}")
    out.append("```")
    out.append("")
    out.append("Status values: `open_source`, `research`, `commercial_open`. Common flags: `license_caveat`, `early_stage`, `archived`, `heavy_runtime`, `requires_api_key`, `authorized_testing_only`, `commercial_features`, `no_license`, `noncommercial`, `copyleft`, `abliterated_or_uncensored`.")
    out.append("")
    out.append("Guidelines: link the canonical upstream repo (not a fork); verify the URL resolves; tag the correct type and add a caveat flag/note for non-permissive, non-commercial, unclear, missing, or restrictive licenses; prefer real, installable projects over blog-only references.")
    out.append("")
    out.append("For Hugging Face model entries, include the model id, license, access status (open/gated), and artifact formats (for example Safetensors or ONNX).")
    out.append("")
    out.append("## License")
    out.append("")
    out.append("To the extent possible under law, the contributors have waived all copyright and related rights to this list ([CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/)). Linked projects retain their own licenses — check each before use.")
    out.append("")
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path,
                        default=Path(__file__).with_name("data") / "sections.json",
                        help="structured JSON data path")
    parser.add_argument("-o", "--output", type=Path,
                        default=Path(__file__).with_name("README.md"),
                        help="README path to write or check")
    parser.add_argument("--check", action="store_true",
                        help="fail if the output README is not up to date")
    args = parser.parse_args()

    try:
        data = load_data(args.data)
        rendered = build(data)
    except DataError as exc:
        print(f"data error: {exc}", flush=True)
        return 2

    if args.check:
        current = args.output.read_text(encoding="utf-8")
        if current != rendered:
            print(f"{args.output} is out of date; run gen_readme.py", flush=True)
            return 1
        print(f"{args.output} is up to date.")
        return 0

    args.output.write_text(rendered, encoding="utf-8")
    print(f"{args.output} generated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
