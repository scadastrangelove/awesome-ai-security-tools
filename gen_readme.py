#!/usr/bin/env python3
"""Generate the Awesome AI Security Tools README from structured data.

Badges are dynamic shields.io endpoints (stars + last commit) that render live
from the GitHub API, so counts stay fresh without manual updates.
"""

from argparse import ArgumentParser
from pathlib import Path
import re

STAR = "%E2%98%85"  # ★


def badges(repo: str) -> str:
    s = (f"[![stars](https://img.shields.io/github/stars/{repo}"
         f"?style=flat-square&label={STAR})](https://github.com/{repo})")
    c = (f"[![updated](https://img.shields.io/github/last-commit/{repo}"
         f"?style=flat-square&label=updated)](https://github.com/{repo})")
    return f"{s} {c}"


def hf_model_url(model: str) -> str:
    return f"https://huggingface.co/{model}"


def render_hf_model(e):
    model = e["model"]
    url = e.get("url", hf_model_url(model))
    tags = e["tags"]
    org = f" *({e['org']})*" if e.get("org") else ""
    meta = []
    if e.get("license"):
        meta.append(f"license: {e['license']}")
    if e.get("access"):
        meta.append(f"access: {e['access']}")
    if e.get("artifacts"):
        meta.append(f"artifacts: {e['artifacts']}")
    note = f" *{' · '.join(meta)}.*" if meta else ""
    if e.get("note"):
        note = f"{note} {e['note']}" if note else f" {e['note']}"
    return f"- **[{e['name']}]({url})** {tags} — {e['desc']}{org}{note}"


def link(pair):
    label, url = pair
    return f"[{label}]({url})"


def github_anchor(title: str) -> str:
    """Approximate GitHub's Markdown heading anchors for this README."""
    cleaned = re.sub(r"[^\w\s-]", "", title.lower())
    return cleaned.replace(" ", "-")


def render_entry(e):
    if e.get("kind") == "hf_model":
        return render_hf_model(e)
    repo = e["repo"]
    url = e.get("url", f"https://github.com/{repo}")
    tags = e["tags"]
    org = f" *({e['org']})*" if e.get("org") else ""
    note = f" {e['note']}" if e.get("note") else ""
    line = (f"- **[{e['name']}]({url})** {tags} — {e['desc']}{org}{note} "
            f"{badges(repo)}")
    out = [line]
    if e.get("sources"):
        out.append("  - **Sources:** " + " · ".join(link(s) for s in e["sources"]))
    if e.get("related"):
        out.append("  - **Related:** " + " · ".join(link(r) for r in e["related"]))
    return "\n".join(out)


# Short reusable link targets
GH = "https://github.com/"
HF = "https://huggingface.co/"
VULNHUNTR = ("Vulnhuntr", GH + "protectai/vulnhuntr")
XVULNHUNTR = ("xvulnhuntr", GH + "CompassSecurity/xvulnhuntr")
VULNHUNTR_MOD = ("vulnhuntr-mod", GH + "kxcode/vulnhuntr-mod")
ASAMM = ("asamm", GH + "scadastrangelove/asamm")
AGENT_AUDIT = ("agent-audit", GH + "scadastrangelove/agent-audit")
ATR = ("ATR – Agent Threat Rules", GH + "panguard-ai/agent-threat-rules")
AGUARA = ("aguara", GH + "garagon/aguara")
AGENTGUARD = ("agentguard", GH + "GoPlusSecurity/agentguard")
AGENTIC_RADAR = ("agentic-radar", GH + "splx-ai/agentic-radar")
AGENT_SCAN = ("Snyk Agent Scan", GH + "snyk/agent-scan")
SKILL_SCANNER = ("Cisco AI Defense – skill-scanner", GH + "cisco-ai-defense/skill-scanner")
MCP_SCANNER = ("Cisco AI Defense – mcp-scanner", GH + "cisco-ai-defense/mcp-scanner")
NUCLEI_AT = ("nuclei-autotriage", GH + "cyberok-org/nuclei-autotriage")
SWE_AGENT = ("SWE-agent", GH + "SWE-agent/SWE-agent")
MODELSCAN = ("modelscan", GH + "protectai/modelscan")
FICKLING = ("Fickling", GH + "trailofbits/fickling")
PICKLESCAN = ("picklescan", GH + "mmaitre314/picklescan")
SECLAB_TASKFLOW = ("seclab-taskflow-agent", GH + "GitHubSecurityLab/seclab-taskflow-agent")
SIGMA_OPTIMIZER = ("SigmaOptimizer", GH + "YusukeJustinNakajima/SigmaOptimizer")
FRAIM = ("Fraim", GH + "fraim-dev/fraim")
SOCTALK = ("soctalk", GH + "soctalk/soctalk")
SPIKEE = ("spikee", GH + "ReversecLabs/spikee")
PROMPTMAP = ("promptmap", GH + "utkusen/promptmap")

# ---------------------------------------------------------------------------
# Data model: list of (section_title, anchor, intro, body)
# body is either a list of entries (rendered) or a list of (subtitle, [entries])
# ---------------------------------------------------------------------------

SECTIONS = []

SECTIONS.append((
    "Autotriage of Security Findings",
    "autotriage-of-security-findings",
    "AI/LLM tools that triage, deduplicate, prioritize, or validate the output of scanners and finding sources.",
    [
        {"name": "nuclei-autotriage", "repo": "cyberok-org/nuclei-autotriage", "tags": "🟢⚠️",
         "org": "CyberOK",
         "desc": "Two-stage LLM triage (falsifier + red-team pass) of Nuclei JSONL findings via OpenAI-compatible endpoints (vLLM/Ollama).",
         "note": "— **note:** restrictive personal/non-commercial EULA, not a permissive OSS license.",
         "related": [AGENT_AUDIT, ASAMM]},
        {"name": "seclab-taskflow-agent", "repo": "GitHubSecurityLab/seclab-taskflow-agent", "tags": "🟢", "org": "GitHub Security Lab",
         "desc": "YAML-driven taskflow agent framework for triaging CodeQL/SAST alerts and filtering false positives.",
         "related": [SIGMA_OPTIMIZER]},
        {"name": "honeyslop", "repo": "gadievron/honeyslop", "tags": "🟢",
         "desc": "Code-canary decoys to triage AI-hallucinated (\"slop\") vulnerability reports flooding bug-bounty programs."},
        {"name": "nano-analyzer", "repo": "weareaisle/nano-analyzer", "tags": "🟢🔬", "org": "AISLE",
         "desc": "Minimal three-stage LLM pipeline (context → scan → skeptical triage) for zero-day discovery in C/C++."},
        {"name": "SigmaOptimizer", "repo": "YusukeJustinNakajima/SigmaOptimizer", "tags": "🟢",
         "desc": "Generates, tests, and refines Sigma rules from real logs with false-positive checking.",
         "related": [SOCTALK, SECLAB_TASKFLOW]},
        {"name": "ai-soc-triage-assistant", "repo": "pranavibunny/ai-soc-triage-assistant", "tags": "🟢⚠️",
         "desc": "SOC alert triage assistant with prompt-injection guardrails, output validation, and MITRE ATT&CK mapping."},
    ],
    "> See also: OpenAI's *Aardvark* / *Codex Security* research previews — public references exist, but there is no standalone installable repo to badge here.",
))

SECTIONS.append((
    "AI Agent & Coding-Agent Security",
    "ai-agent--coding-agent-security",
    "Securing the AI agents themselves — auditing coding agents (Claude Code, Codex, OpenClaw), scanning skills / plugins / MCP manifests, and governance for agentic development. A fast-moving 2026 category, split below by role.",
    [
        ("Scanners & Auditors", [
            {"name": "agent-audit", "repo": "scadastrangelove/agent-audit", "tags": "🟢", "org": "CyberOK / S. Gordeychik",
             "desc": "Forensic auditor for local AI coding agents (Claude Code, Codex CLI, OpenClaw) **and** project-surface scanner for repos shipping skills, plugins, and MCP manifests; 296 bundled rules across native + imported detector families, with optional LLM cross-verification.",
             "sources": [ASAMM, ATR, AGUARA, SKILL_SCANNER],
             "related": [ASAMM, AGUARA, AGENTGUARD, AGENTIC_RADAR, NUCLEI_AT]},
            {"name": "AI-Infra-Guard", "repo": "Tencent/AI-Infra-Guard", "tags": "🟢", "org": "Tencent Zhuque Lab",
             "desc": "Full-stack AI red-teaming platform covering OpenClaw security scan, agent scan, skills scan, MCP scan, AI-infra vulnerability scan, and LLM jailbreak evaluation.",
             "related": [AGENT_AUDIT, AGUARA, SKILL_SCANNER, MCP_SCANNER]},
            {"name": "aguara", "repo": "garagon/aguara", "tags": "🟢",
             "desc": "Single-binary static scanner (Go, no LLM) for AI-agent skills and MCP servers; multi-layer engine (pattern + NLP + taint tracking + rug-pull detection). Companion **[aguara-mcp](https://github.com/garagon/aguara-mcp)** exposes scanning as an MCP tool.",
             "related": [("aguara-mcp", GH + "garagon/aguara-mcp"), AGENT_AUDIT, AGENT_SCAN, SKILL_SCANNER]},
            {"name": "agent-scan", "repo": "snyk/agent-scan", "tags": "🟢", "org": "Snyk",
             "desc": "Security scanner for AI agents, MCP servers, and agent skills; the successor path for the original Invariant Labs mcp-scan work.",
             "related": [AGUARA, MCP_SCANNER, SKILL_SCANNER]},
            {"name": "inkog", "repo": "inkog-io/inkog", "tags": "🟠", "org": "Inkog",
             "desc": "Commercial-backed static security scanner for AI agents across LangChain, LangGraph, CrewAI, AutoGen, and no-code workflows; Apache-2.0 CLI with proprietary deep-scan engine.",
             "related": [AGENT_SCAN, AGENTIC_RADAR]},
            {"name": "AgentShield", "repo": "affaan-m/agentshield", "tags": "🟢",
             "desc": "Security scanner for AI-agent configurations, MCP servers, hooks, and tool permissions with CLI, GitHub Action, and app workflows.",
             "related": [AGENT_AUDIT, AGENT_SCAN]},
            {"name": "repo-forensics", "repo": "alexgreensh/repo-forensics", "tags": "🟢⚠️",
             "desc": "Offline scanner for AI-agent repos, skills, plugins, and MCP servers; license is PolyForm Noncommercial.",
             "related": [AGENT_AUDIT, AGUARA]},
            {"name": "skill-scanner", "repo": "cisco-ai-defense/skill-scanner", "tags": "🟠", "org": "Cisco AI Defense",
             "desc": "Scanner for agent skills combining YAML + YARA patterns, LLM-as-a-judge, and behavioral dataflow analysis (Codex / Cursor skill formats).",
             "related": [("defenseclaw", GH + "cisco-ai-defense/defenseclaw"), AGUARA, MCP_SCANNER]},
            {"name": "mcp-scanner", "repo": "cisco-ai-defense/mcp-scanner", "tags": "🟢⚠️", "org": "Cisco AI Defense",
             "desc": "Scanner for MCP servers and agentic tool surfaces, covering tools, prompts, resources, package risk, malware indicators, and deployment readiness.",
             "related": [SKILL_SCANNER, AGENT_SCAN, AGUARA]},
            {"name": "mcp-guardian", "repo": "alexandriashai/mcp-guardian", "tags": "🟢",
             "desc": "JS/TS library and CLI for detecting prompt injection in MCP tool descriptions and pinning tool definitions.",
             "related": [MCP_SCANNER, AGENT_SCAN]},
            {"name": "agentic-radar", "repo": "splx-ai/agentic-radar", "tags": "🟠", "org": "SplxAI",
             "desc": "CLI security scanner for agentic workflows (LangGraph, CrewAI, n8n, etc.) — maps tools/data flows and flags risks."},
        ]),
        ("Frameworks, Rule Standards & Benchmarks", [
            {"name": "asamm", "repo": "scadastrangelove/asamm", "tags": "🔬", "org": "CyberOK / S. Gordeychik",
             "desc": "*Agentic SAMM* — an OWASP SAMM extension for AI-driven development: an entry-point-based threat taxonomy plus 17 controls across 5 SAMM functions (Governance, Design, Implementation, Verification, Operations) with L1/L2/L3 maturity. License: CC BY-SA 4.0.",
             "sources": [("OWASP SAMM", "https://owaspsamm.org/"),
                         ("NIST AI RMF", "https://www.nist.gov/itl/ai-risk-management-framework"),
                         ("NCSC Secure AI Guidelines", "https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development"),
                         ("MCP Security Best Practices", "https://modelcontextprotocol.io/")],
             "related": [AGENT_AUDIT]},
            {"name": "agent-threat-rules (ATR)", "repo": "panguard-ai/agent-threat-rules", "tags": "🟢",
             "desc": "Open, versioned, machine-readable detection-rule format for AI-agent threats (prompt injection, tool poisoning, MCP attacks, skill compromise) — \"Sigma for agents\" (MIT). Engine-agnostic; converts to Splunk/Elastic/SARIF.",
             "related": [AGENT_AUDIT, AGUARA]},
            {"name": "MCP-Security-Checklist", "repo": "slowmist/MCP-Security-Checklist", "tags": "🟢", "org": "SlowMist",
             "desc": "Security checklist for MCP clients, servers, multi-MCP deployments, lifecycle controls, authz/authn, isolation, and crypto-specific MCP integrations.",
             "related": [MCP_SCANNER, ATR]},
            {"name": "Anthropic-Cybersecurity-Skills", "repo": "mukul975/Anthropic-Cybersecurity-Skills", "tags": "🟢",
             "desc": "Large community cybersecurity skill library for AI agents, mapped to MITRE ATT&CK, NIST CSF, MITRE ATLAS, D3FEND, and NIST AI RMF.",
             "note": "— **note:** independent community project, not affiliated with Anthropic.",
             "related": [("sast-skills", GH + "utkusen/sast-skills"), SKILL_SCANNER]},
            {"name": "AgentDojo", "repo": "ethz-spylab/agentdojo", "tags": "🟢🔬",
             "desc": "Benchmark environment for prompt-injection attacks and defenses in tool-using LLM agents.",
             "related": [AGENT_AUDIT, ATR]},
        ]),
        ("Runtime Protection & Enforcement", [
            {"name": "onecli", "repo": "onecli/onecli", "tags": "🟢",
             "desc": "Credential gateway and encrypted vault for AI agents; injects real API credentials at the gateway so agents only see placeholder keys.",
             "related": [AGENTGUARD, ("defenseclaw", GH + "cisco-ai-defense/defenseclaw")]},
            {"name": "microsandbox", "repo": "superradcompany/microsandbox", "tags": "🟢",
             "desc": "Local-first, microVM-backed programmable sandboxes for AI agents with SDKs, CLI, MCP support, and rootless hardware isolation.",
             "related": [AGENTGUARD, ("defenseclaw", GH + "cisco-ai-defense/defenseclaw")]},
            {"name": "agentguard", "repo": "GoPlusSecurity/agentguard", "tags": "🟢",
             "desc": "Real-time security layer for coding agents: hooks scan every new skill, block dangerous actions before execution, run daily posture patrols, and track which skill triggered each action (incl. Web3-specific checks).",
             "related": [AGENT_AUDIT, ("defenseclaw", GH + "cisco-ai-defense/defenseclaw")]},
            {"name": "defenseclaw", "repo": "cisco-ai-defense/defenseclaw", "tags": "🟠", "org": "Cisco AI Defense",
             "desc": "Enforcement and evidence layer for agentic deployments: static CodeGuard checks, sandboxing, registry ingestion with SSRF guards, and audit/observability.",
             "related": [SKILL_SCANNER, AGENTGUARD]},
            {"name": "AgentFence", "repo": "agentfence/agentfence", "tags": "🟢",
             "desc": "Runtime-oriented test harness for deployed agents, probing prompt injection, secret leakage, and system-instruction exposure.",
             "note": "*Early-stage project.*",
             "related": [AGENTGUARD, AGENT_SCAN]},
            {"name": "clawsec", "repo": "prompt-security/clawsec", "tags": "🟢⚠️", "org": "Prompt Security",
             "desc": "Security skill suite for OpenClaw-family agents; AGPL-3.0 licensed.",
             "related": [AGENTGUARD, SKILL_SCANNER]},
        ]),
    ],
    None,
))

SECTIONS.append((
    "AI/ML Supply Chain & Model Security",
    "aiml-supply-chain--model-security",
    "Tools for securing model artifacts, serialized ML files, AI/ML supply-chain surfaces, and malicious-package detection datasets/benchmarks.",
    [
        {"name": "Fraim", "repo": "fraim-dev/fraim", "tags": "🟢",
         "desc": "Framework for AI-powered security workflows including LLM SAST and IaC analysis with SARIF/HTML output.",
         "related": [("sast-skills", GH + "utkusen/sast-skills")]},
        {"name": "Adversarial Robustness Toolbox (ART)", "repo": "Trusted-AI/adversarial-robustness-toolbox", "tags": "🟢", "org": "LF AI & Data / IBM",
         "desc": "Flagship machine-learning security library for evaluating and defending models against evasion, poisoning, extraction, and inference attacks across major ML frameworks.",
         "related": [("Foolbox", GH + "bethgelab/foolbox"), ("PrivacyRaven", GH + "trailofbits/PrivacyRaven")]},
        {"name": "Foolbox", "repo": "bethgelab/foolbox", "tags": "🟢",
         "desc": "Classic Python toolbox for generating adversarial examples and benchmarking robustness of PyTorch, TensorFlow, and JAX models.",
         "related": [("Adversarial Robustness Toolbox", GH + "Trusted-AI/adversarial-robustness-toolbox")]},
        {"name": "modelscan", "repo": "protectai/modelscan", "tags": "🟢", "org": "Protect AI",
         "desc": "Scans ML model files for unsafe serialization patterns and embedded code, with a focus on model serialization attacks.",
         "related": [FICKLING, PICKLESCAN, ("ai-exploits", GH + "protectai/ai-exploits")]},
        {"name": "Fickling", "repo": "trailofbits/fickling", "tags": "🟢", "org": "Trail of Bits",
         "desc": "Python pickle decompiler, rewriter, and static analyzer for inspecting and detecting malicious pickle/PyTorch payloads.",
         "related": [MODELSCAN, PICKLESCAN]},
        {"name": "picklescan", "repo": "mmaitre314/picklescan", "tags": "🟢",
         "desc": "Lightweight CLI/library for detecting suspicious Python pickle operations in ML and model artifacts.",
         "related": [MODELSCAN, FICKLING]},
        {"name": "AIsbom", "repo": "Lab700xOrg/aisbom", "tags": "🟢",
         "desc": "AI software bill of materials tooling for AI/ML supply-chain inventory and provenance metadata.",
         "related": [MODELSCAN, ("model-provenance-kit", GH + "cisco-ai-defense/model-provenance-kit")]},
        {"name": "model-provenance-kit", "repo": "cisco-ai-defense/model-provenance-kit", "tags": "🟢", "org": "Cisco AI Defense",
         "desc": "Toolkit for model-family provenance and fingerprinting across model weights, tokenizers, and architecture signals.",
         "related": [("AIsbom", GH + "Lab700xOrg/aisbom")]},
        {"name": "pickle-fuzzer", "repo": "cisco-ai-defense/pickle-fuzzer", "tags": "🟢", "org": "Cisco AI Defense",
         "desc": "Structure-aware fuzzer for pickle scanners, useful for hardening tools such as modelscan, Fickling, and picklescan.",
         "related": [MODELSCAN, FICKLING, PICKLESCAN]},
        {"name": "Medusa", "repo": "Pantheon-Security/medusa", "tags": "🟢⚠️", "org": "Pantheon Security",
         "desc": "AI-first security scanner for AI/ML repos, agents, and MCP surfaces; AGPL-3.0 licensed.",
         "related": [AGENT_AUDIT, MODELSCAN]},
        {"name": "PrivacyRaven", "repo": "trailofbits/PrivacyRaven", "tags": "🟢🔬", "org": "Trail of Bits",
         "desc": "Privacy-testing library for deep-learning systems, covering model extraction and membership-inference style attacks.",
         "note": "— **note:** archived/hiatus project, but still a useful reference implementation.",
         "related": [("Adversarial Robustness Toolbox", GH + "Trusted-AI/adversarial-robustness-toolbox")]},
        {"name": "gym-malware", "repo": "endgameinc/gym-malware", "tags": "🟢🔬",
         "desc": "OpenAI Gym environment for reinforcement-learning agents that mutate PE malware to evade static ML malware detectors."},
        {"name": "deep-pwning", "repo": "cchio/deep-pwning", "tags": "🟢🔬",
         "desc": "Historical \"Metasploit for machine learning\" framework for experimenting with adversarial robustness of ML models."},
        {"name": "open-malicious-code-benchmark", "repo": "False-Positive-Community/open-malicious-code-benchmark", "tags": "🟢🔬", "org": "False Positive Community",
         "desc": "OMCBench benchmark suite for malicious-code/package detection: labeled Python and JavaScript package archives, common runners, and published precision/recall/F1 metrics.",
         "note": "— **note:** evaluates an unreleased commercial ML detector (MOLOT / PT Application Inspector) alongside open-source baselines.",
         "related": [("GuardDog", GH + "DataDog/guarddog"), ("OSSGadget", GH + "microsoft/OSSGadget"), ("malicious-code-ruleset", GH + "apiiro/malicious-code-ruleset"), ("bandit4mal", GH + "lyvd/bandit4mal")]},
        {"name": "malicious-software-packages-dataset", "repo": "DataDog/malicious-software-packages-dataset", "tags": "🟢🔬", "org": "Datadog Security Labs",
         "desc": "Human-vetted dataset of malicious software packages across npm, PyPI, IDE extensions, and AI Skills, useful for detector training and evaluation.",
         "note": "— **note:** contains real malware samples; Datadog notes selection bias because many samples were identified by GuardDog.",
         "related": [("GuardDog", GH + "DataDog/guarddog"), ("pypi_malregistry", GH + "lxyeternal/pypi_malregistry")]},
        {"name": "GuardDog", "repo": "DataDog/guarddog", "tags": "🟢", "org": "Datadog",
         "desc": "CLI for detecting malicious PyPI, npm, Go, RubyGems, GitHub Actions, and VSCode extension packages using Semgrep rules and package-metadata heuristics.",
         "related": [("malicious-software-packages-dataset", GH + "DataDog/malicious-software-packages-dataset"), ("Packj", GH + "ossillate-inc/packj")]},
        {"name": "package-analysis", "repo": "ossf/package-analysis", "tags": "🟢🔬", "org": "OpenSSF",
         "desc": "Sandboxed static/dynamic analysis pipeline for open-source packages, capturing filesystem, process, and network behavior and publishing data for malicious-package research.",
         "related": [("malicious-packages", GH + "ossf/malicious-packages"), ("package-feeds", GH + "ossf/package-feeds")]},
        {"name": "malicious-code-ruleset", "repo": "apiiro/malicious-code-ruleset", "tags": "🟢", "org": "Apiiro",
         "desc": "Focused Semgrep ruleset for malicious-code patterns such as dynamic execution and obfuscation, used as an OMCBench baseline.",
         "related": [("open-malicious-code-benchmark", GH + "False-Positive-Community/open-malicious-code-benchmark")]},
        {"name": "pypi_malregistry", "repo": "lxyeternal/pypi_malregistry", "tags": "🔬⚠️",
         "desc": "ASE'23 / USENIX Security'26 malicious-PyPI dataset with more than 10k malicious package versions.",
         "note": "— **note:** no LICENSE file found and the repository contains malware samples; handle in an isolated environment.",
         "related": [("malicious-software-packages-dataset", GH + "DataDog/malicious-software-packages-dataset")]},
    ],
    None,
))

SECTIONS.append((
    "Pentest & Red-Team Agents",
    "pentest--red-team-agents",
    "Autonomous and semi-autonomous AI agents for penetration testing, exploitation, and attack simulation.",
    [
        {"name": "PentestGPT", "repo": "GreyDGL/PentestGPT", "tags": "🟢🔬",
         "desc": "The original USENIX'24 LLM pentest agent; re-released as an autonomous pipeline with strong benchmark results."},
        {"name": "PentAGI", "repo": "vxcontrol/pentagi", "tags": "🟢", "org": "VXControl",
         "desc": "Fully autonomous multi-agent pentest framework with Docker sandboxing."},
        {"name": "CAI – Cybersecurity AI", "repo": "aliasrobotics/cai", "tags": "🟢🟠", "org": "Alias Robotics",
         "desc": "Modular, bug-bounty-ready agent framework supporting 300+ LLM models. MIT for research; separate commercial license for production/on-prem."},
        {"name": "Strix", "repo": "usestrix/strix", "tags": "🟢",
         "desc": "Autonomous \"AI hackers\" that dynamically run code and validate vulnerabilities with PoCs (Apache-2.0)."},
        {"name": "hackingBuddyGPT", "repo": "ipa-lab/hackingBuddyGPT", "tags": "🟢🔬",
         "desc": "Minimal (~50 LOC) research framework for LLM-driven Linux priv-esc and web pentesting (FSE'23)."},
        {"name": "Nebula", "repo": "berylliumsec/nebula", "tags": "🟢🟠",
         "desc": "AI pentesting CLI assistant with local-LLM support (Llama-3.1, Mistral, DeepSeek)."},
        {"name": "HexStrike-AI", "repo": "0x4m4/hexstrike-ai", "tags": "🟢",
         "desc": "MCP server exposing 150+ security tools (nmap, gobuster, nuclei, …) to AI agents (MIT)."},
        {"name": "Burp Suite MCP Server", "repo": "PortSwigger/mcp-server", "tags": "🟢⚠️", "org": "PortSwigger",
         "desc": "Official Burp Suite extension exposing Burp to AI clients through MCP.",
         "note": "— **note:** GPL-3.0 licensed.",
         "related": [("HexStrike-AI", GH + "0x4m4/hexstrike-ai")]},
        {"name": "pentest-ai", "repo": "0xSteph/pentest-ai", "tags": "🟢",
         "desc": "Offensive-security MCP server with 200+ wrapped tools, specialist agents, and OWASP-oriented probes for authorized testing.",
         "related": [("pentest-ai-agents", GH + "0xSteph/pentest-ai-agents")]},
        {"name": "pentest-ai-agents", "repo": "0xSteph/pentest-ai-agents", "tags": "🟢",
         "desc": "Collection of Claude Code offensive-security subagents for authorized penetration-testing research.",
         "related": [("pentest-ai", GH + "0xSteph/pentest-ai")]},
        {"name": "Shannon", "repo": "KeygraphHQ/shannon", "tags": "🟢🟠⚠️",
         "desc": "White-box autonomous AI pentester with strong XBOW-benchmark results.",
         "note": "*Shannon Lite is AGPL-3.0; Shannon Pro is commercial.*"},
        {"name": "AIDA", "repo": "Vasco0x4/AIDA", "tags": "🟢⚠️",
         "desc": "Model-agnostic autonomous pentest agent running inside an isolated Docker environment; AGPL-3.0 licensed."},
        {"name": "HackSynth", "repo": "aielte-research/HackSynth", "tags": "🟢🔬⚠️",
         "desc": "Planner/summarizer LLM-agent framework for autonomous penetration testing and benchmark evaluation; AGPL-3.0 licensed."},
        {"name": "VulnBot", "repo": "KHenryAegis/VulnBot", "tags": "🟢🔬",
         "desc": "Multi-agent collaborative penetration-testing framework with RAG support."},
        {"name": "PentestAgent", "repo": "GH05TCREW/pentestagent", "tags": "🟢",
         "desc": "Black-box AI pentest framework with MCP, multi-agent spawning, and persistent sessions."},
        {"name": "cyber-security-llm-agents", "repo": "NVISOsecurity/cyber-security-llm-agents", "tags": "🟢⚠️", "org": "NVISO",
         "desc": "AutoGen-based agents for cybersecurity tasks (shown at RSAC 2024)."},
        {"name": "Pentest-Swarm-AI", "repo": "Armur-Ai/Pentest-Swarm-AI", "tags": "🟢",
         "desc": "Swarm-intelligence multi-agent pentest with stigmergic blackboard coordination (Go)."},
        {"name": "hackGPT", "repo": "NoDataFound/hackGPT", "tags": "🟢⚠️",
         "desc": "LLM offensive-security toolkit."},
    ],
    None,
))

SECTIONS.append((
    "AI-Powered Recon & Narrow ML Tools",
    "ai-powered-recon--narrow-ml-tools",
    "Hyper-specific AI/ML tools for a single offensive-security, recon, or detection step — the subwiz/eyeballer pattern rather than broad autonomous agents. 🅐 = self-contained trained model or learned model/pattern engine; 🅑 = LLM wrapper that calls an external API.",
    [
        ("Subdomain & DNS Prediction", [
            {"name": "subwiz", "repo": "hadriansecurity/subwiz", "tags": "🟢", "org": "Hadrian Security",
             "desc": "🅐 Lightweight nanoGPT model that predicts resolvable subdomains via beam search; model weights are published on Hugging Face.",
             "related": [("HadrianSecurity/subwiz model", HF + "HadrianSecurity/subwiz")]},
            {"name": "regulator", "repo": "cramppet/regulator", "tags": "🟢⚠️",
             "desc": "🅐 Learns and ranks regex-like naming patterns from known subdomains to generate likely new candidates.",
             "note": "— **note:** no LICENSE file found; treat as source-available until clarified.",
             "related": [("subwiz", GH + "hadriansecurity/subwiz")]},
        ]),
        ("Recon Screenshot Triage", [
            {"name": "eyeballer", "repo": "BishopFox/eyeballer", "tags": "🟢⚠️", "org": "Bishop Fox",
             "desc": "🅐 Convolutional neural network that classifies pentest/recon screenshots (login pages, webapps, old-looking sites, parked domains, and custom 404s) for attack-surface triage.",
             "note": "— **note:** GPL-3.0 licensed."},
        ]),
        ("Software / Tech Fingerprinting", [
            {"name": "GyoiThon", "repo": "gyoisamurai/GyoiThon", "tags": "🟢🔬",
             "desc": "🅐 Machine-learning-assisted web intelligence tool that fingerprints products, versions, CVEs, login pages, debug messages, and related web-server signals from HTTP responses.",
             "note": "— **note:** older project; Apache-2.0 licensed, but maintenance appears low."},
            {"name": "http-fingerprint-transformer", "repo": "Darwinkel/bachelor-thesis-information-science", "tags": "🔬⚠️",
             "desc": "🅐 Transformer-encoded HTTP-header fingerprinting experiment for classifying web-server software and versions.",
             "note": "— **note:** thesis artifact; code is GPL-3.0 and data is CC BY-SA 4.0."},
        ]),
        ("AI-Assisted Fuzzing", [
            {"name": "ffufai", "repo": "jthack/ffufai", "tags": "🟢⚠️", "org": "Joseph Thacker",
             "desc": "🅑 AI wrapper around the ffuf web fuzzer that suggests file extensions and paths from the target URL and headers using OpenAI or Anthropic models.",
             "note": "— **note:** requires an LLM API key; README states MIT but no LICENSE file was found."},
        ]),
        ("Password / Credential ML", [
            {"kind": "hf_model", "name": "PassGPT", "model": "javirandor/passgpt-10characters", "tags": "🔬⚠️", "org": "Rando et al.",
             "desc": "🅐 GPT-style password model trained on leaked passwords for research on password generation and strength estimation.",
             "license": "CC BY-NC-4.0", "access": "open 10-char model; 16-char variant gated", "artifacts": "PyTorch/Safetensors",
             "note": "Research-only / non-commercial use; related code: [javirandor/passgpt](https://github.com/javirandor/passgpt)."},
            {"name": "PassGAN", "repo": "brannondorsey/PassGAN", "tags": "🔬",
             "desc": "🅐 WGAN that learns password distributions from leaks to generate guesses; historical reference implementation of the PassGAN paper (MIT)."},
            {"name": "neural_network_cracking", "repo": "cupslab/neural_network_cracking", "tags": "🔬", "org": "CMU CUPS Lab",
             "desc": "🅐 RNN password-guessing model from *Fast, Lean, and Accurate: Modeling Password Guessability Using Neural Networks* (USENIX Security 2016); Apache-2.0 licensed.",
             "related": [("PassGPT", HF + "javirandor/passgpt-10characters"), ("PassGAN", GH + "brannondorsey/PassGAN")]},
        ]),
        ("Phishing Detection (Visual / URL)", [
            {"kind": "hf_model", "name": "phishing-url-detection", "model": "pirocheto/phishing-url-detection", "tags": "🟢",
             "desc": "🅐 Packaged URL phishing classifier with ONNX and pickle artifacts.",
             "license": "MIT", "access": "open", "artifacts": "ONNX, pickle",
             "note": "Model card recommends ONNX over pickle for safer inference."},
            {"name": "PhishIntention", "repo": "lindsey98/PhishIntention", "tags": "🔬",
             "desc": "🅐 Deep-vision phishing detector that infers both brand intention and credential-taking intention from webpage appearance and dynamics (USENIX Security 2022).",
             "note": "— **note:** CC0-1.0 licensed."},
            {"name": "VisualPhishNet", "repo": "S-Abdelnabi/VisualPhishNet", "tags": "🔬⚠️", "org": "CISPA",
             "desc": "🅐 Triplet CNN for zero-day phishing detection by visual similarity to trusted websites (ACM CCS 2020).",
             "note": "— **note:** no LICENSE file found; dataset access is research-request based."},
        ]),
        ("ML-Generated Detection Rules", [
            {"name": "yaraml_rules", "repo": "sophos/yaraml_rules", "tags": "🟢", "org": "Sophos",
             "desc": "🅐 Trains scikit-learn classifiers on malware/benign corpora and compiles the learned model into deployable YARA rules (Apache-2.0)."},
        ]),
        ("Defensive Trained-Model Detectors", [
            {"name": "DeepSQLi", "repo": "gatewayd-io/DeepSQLi", "tags": "🟢⚠️", "org": "GatewayD",
             "desc": "🅐 Deep-learning SQL-injection detector with dataset, trained models, and a Flask Prediction API for GatewayD IDS/IPS integration.",
             "note": "— **note:** AGPL-3.0 licensed; defensive detector rather than offensive generator."},
            {"name": "deepsecrets", "repo": "ntoskernel/deepsecrets", "tags": "🟢",
             "desc": "Semantic secrets scanner using lexing/parsing, entropy checks, and hashed-known-secret matching across 500+ languages.",
             "note": "— **note:** useful narrow detector, but not a trained ML model."},
        ]),
    ],
    None,
))

SECTIONS.append((
    "AI-Powered SAST & Secure Code Review",
    "ai-powered-sast--secure-code-review",
    "Static analysis and secure code review enhanced with LLMs.",
    [
        {"name": "Vulnhuntr", "repo": "protectai/vulnhuntr", "tags": "🟢", "org": "Protect AI",
         "desc": "Zero-shot vulnerability discovery in Python repos via LLM call-chain analysis; credited with a 0-day RCE in Ragflow.",
         "related": [XVULNHUNTR, VULNHUNTR_MOD]},
        {"name": "deepsec", "repo": "vercel-labs/deepsec", "tags": "🟢", "org": "Vercel Labs",
         "desc": "Agent-powered security harness for scanning large codebases with coding agents, resumable parallel runs, custom matchers, and optional revalidation.",
         "related": [("claude-code-security-review", GH + "anthropics/claude-code-security-review"), ("sast-skills", GH + "utkusen/sast-skills")]},
        {"name": "claude-code-security-review", "repo": "anthropics/claude-code-security-review", "tags": "🟠", "org": "Anthropic",
         "desc": "Official Claude-based semantic SAST GitHub Action that reviews PR diffs."},
        {"name": "IRIS", "repo": "iris-sast/iris", "tags": "🟢🔬",
         "desc": "Neurosymbolic SAST combining LLMs with CodeQL for Java vulnerability detection (MIT)."},
        {"name": "sast-skills", "repo": "utkusen/sast-skills", "tags": "🟢",
         "desc": "Agent skills that turn AI coding assistants into a multi-agent SAST scanner.",
         "related": [FRAIM, ("llm-sast-scanner", GH + "SunWeb3Sec/llm-sast-scanner")]},
        {"name": "llm-sast-scanner", "repo": "SunWeb3Sec/llm-sast-scanner", "tags": "🟢",
         "desc": "SAST skill for AI coding agents with structured source-to-sink analysis across 34 vulnerability classes.",
         "note": "*License: MIT stated in README.*",
         "related": [("sast-skills", GH + "utkusen/sast-skills")]},
        {"name": "sast-ai-workflow", "repo": "RHEcosystemAppEng/sast-ai-workflow", "tags": "🟢", "org": "Red Hat Ecosystem AppEng",
         "desc": "LangGraph workflow for reviewing static-analysis findings, reducing false positives, and producing vulnerability review output.",
         "related": [SECLAB_TASKFLOW, FRAIM]},
        {"name": "xvulnhuntr", "repo": "CompassSecurity/xvulnhuntr", "tags": "🟢", "org": "Compass Security",
         "desc": "Archived fork of Vulnhuntr extending support to C#, Java, and Go.",
         "sources": [VULNHUNTR], "related": [VULNHUNTR_MOD]},
        {"name": "llm-security-scanner", "repo": "iknowjason/llm-security-scanner", "tags": "🟢⚠️",
         "desc": "LLM-powered code scanner that opens GitHub issues for findings."},
        {"name": "vulnhuntr-mod", "repo": "kxcode/vulnhuntr-mod", "tags": "🟢",
         "desc": "Modified Vulnhuntr with Qwen/Hunyuan support and Chinese-language prompts.",
         "sources": [VULNHUNTR], "related": [XVULNHUNTR]},
    ],
    None,
))

SECTIONS.append((
    "LLM-Driven Fuzzing",
    "llm-driven-fuzzing",
    "Two families: (a) LLMs generating harnesses/targets for traditional fuzzing, and (b) fuzzing the LLM itself.",
    [
        ("Harness / target generation", [
            {"name": "oss-fuzz-gen", "repo": "google/oss-fuzz-gen", "tags": "🟢", "org": "Google",
             "desc": "LLM-driven fuzz-harness generation for OSS-Fuzz; reported 26 real vulnerabilities (incl. CVE-2024-9143 in OpenSSL)."},
            {"name": "PromptFuzz", "repo": "PromptFuzz/PromptFuzz", "tags": "🟢🔬⚠️",
             "desc": "LLM-mutated prompts to generate fuzz drivers for C/C++ libraries (Rust)."},
            {"name": "Fuzz4All", "repo": "fuzz4all/fuzz4all", "tags": "🟢🔬",
             "desc": "\"Universal\" LLM-based fuzzer across compilers/languages (ICSE 2024)."},
            {"name": "ChatAFL", "repo": "ChatAFLndss/ChatAFL", "tags": "🟢🔬",
             "desc": "LLM-guided protocol fuzzing extending AFLNet (NDSS'24)."},
            {"name": "TitanFuzz", "repo": "ise-uiuc/TitanFuzz", "tags": "🟢🔬⚠️",
             "desc": "First LLM-based fuzzer for PyTorch/TensorFlow (ISSTA'23)."},
        ]),
        ("Fuzzing the LLM", [
            {"name": "LLMFuzzer", "repo": "mnns/LLMFuzzer", "tags": "🟢",
             "desc": "First open-source fuzzing framework for LLM API integrations."},
            {"name": "ps-fuzz", "repo": "prompt-security/ps-fuzz", "tags": "🟠", "org": "Prompt Security",
             "desc": "System-prompt hardening fuzzer; 16 attacks × 16 providers."},
            {"name": "FuzzyAI", "repo": "cyberark/FuzzyAI", "tags": "🟠", "org": "CyberArk",
             "desc": "Automated LLM fuzzer for jailbreaks/prompt injection."},
            {"name": "spikee", "repo": "ReversecLabs/spikee", "tags": "🟢", "org": "ReversecLabs / WithSecure",
             "desc": "Prompt-injection evaluation and exploitation kit with dataset generation, Burp integration, and pluggable judges.",
             "related": [PROMPTMAP]},
            {"name": "promptmap", "repo": "utkusen/promptmap", "tags": "🟢⚠️",
             "desc": "Prompt-injection scanner for custom LLM applications in white-box and black-box modes; GPL-3.0 licensed.",
             "related": [SPIKEE]},
            {"name": "ai-prompt-fuzzer", "repo": "PortSwigger/ai-prompt-fuzzer", "tags": "🟢", "org": "PortSwigger",
             "desc": "Burp Suite extension fuzzing GenAI/LLM prompts."},
        ]),
    ],
    None,
))

SECTIONS.append((
    "Threat Intelligence",
    "threat-intelligence",
    "AI/LLM tooling for CTI gathering, IOC/TTP extraction, and analysis.",
    [
        {"name": "trs", "repo": "deadbits/trs", "tags": "🟢",
         "desc": "LLM + ChromaDB tool to summarize threat reports and extract MITRE TTPs and IOCs."},
        {"name": "TI-Mindmap-GPT", "repo": "format81/TI-Mindmap-GPT", "tags": "🟢",
         "desc": "Streamlit app: AI summaries, mindmaps, IOC/TTP extraction, and ATT&CK Navigator layers."},
        {"name": "aiocrioc", "repo": "referefref/aiocrioc", "tags": "🟢",
         "desc": "LLM + OCR IOC extraction (pulls IOCs from images/PDFs)."},
        {"name": "ThreatIngestor", "repo": "InQuest/ThreatIngestor", "tags": "🟢",
         "desc": "Extracts/aggregates IOCs from feeds; integrates with MISP/ThreatKB (pairs well with LLM post-processing)."},
        {"name": "IATelligence", "repo": "fr0gger/IATelligence", "tags": "🟢",
         "desc": "Explains imported Windows APIs in PE files via GPT and maps to MITRE ATT&CK.",
         "related": [("MCP_Security", GH + "fr0gger/MCP_Security")]},
        {"name": "MCP_Security", "repo": "fr0gger/MCP_Security", "tags": "🟢⚠️",
         "desc": "MCP server (ORKL) for querying the ORKL threat-intel API.",
         "related": [("IATelligence", GH + "fr0gger/IATelligence")]},
        {"name": "threat-intelligence-cti-analysis", "repo": "AnandBinuArjun/threat-intelligence-cti-analysis", "tags": "🟢",
         "desc": "NLP/LLM pipeline for IOC extraction, MITRE ATT&CK mapping, and knowledge-graph generation from unstructured CTI.",
         "related": [SOCTALK]},
    ],
    None,
))

SECTIONS.append((
    "Log Analysis / SIEM / SOC Triage",
    "log-analysis--siem--soc-triage",
    "AI agents for SOC alert triage, investigation, and incident response.",
    [
        {"name": "AI-SOC-Agent", "repo": "M507/ai-soc-agent", "tags": "🟢",
         "desc": "Black Hat 2025 MCP server exposing security-investigation tools (ELK, IRIS)."},
        {"name": "soctalk", "repo": "soctalk/soctalk", "tags": "🟢",
         "desc": "LangGraph SOC automation agent with MCP integrations for Wazuh, Cortex, TheHive, and MISP plus mock-agent test lab.",
         "related": [SIGMA_OPTIMIZER]},
        {"name": "Vigil SOC", "repo": "Vigil-SOC/vigil", "tags": "🟢", "org": "Vigil SOC",
         "desc": "Open-source AI SOC with readable Python agents, Markdown playbooks, and MCP integrations for triage, investigation, hunting, response, reporting, and forensics.",
         "related": [SOCTALK]},
        {"name": "agentic-soc-platform", "repo": "FunnyWolf/agentic-soc-platform", "tags": "🟢",
         "desc": "Agentic SOC platform (LangGraph/Dify) with local-LLM support."},
        {"name": "SigmAIQ", "repo": "AttackIQ/SigmAIQ", "tags": "🟢⚠️", "org": "AttackIQ",
         "desc": "pySigma wrapper and LangChain toolkit for automatic Sigma rule creation and translation; LGPL-2.1 licensed.",
         "related": [SIGMA_OPTIMIZER]},
        {"name": "SOCGPT", "repo": "Ninadjos/SOCGPT-AI-Powered-SOC-Assistant", "tags": "🟢",
         "desc": "LLM log summarization, severity triage, MITRE mapping, and Q&A."},
        {"name": "AttackGen", "repo": "mrwadams/attackgen", "tags": "🟢",
         "desc": "LLM-driven incident-response scenario generator using MITRE ATT&CK + ATLAS."},
    ],
    None,
))

SECTIONS.append((
    "Reverse Engineering",
    "reverse-engineering",
    "LLM-assisted binary analysis and traffic inspection.",
    [
        {"name": "Gepetto", "repo": "JusticeRage/Gepetto", "tags": "🟢",
         "desc": "IDA Pro plugin: GPT adds comments and meaningful variable names."},
        {"name": "ida-pro-mcp", "repo": "mrexodia/ida-pro-mcp", "tags": "🟢",
         "desc": "MCP bridge for IDA Pro exposing decompile, disassemble, xref, rename, and debugging workflows to LLM clients."},
        {"name": "GhidraMCP", "repo": "LaurieWired/GhidraMCP", "tags": "🟢",
         "desc": "MCP server exposing Ghidra reverse-engineering ops to any MCP-capable LLM.",
         "related": [("GhidrOllama", GH + "lr-m/GhidrOllama"), ("OGhidra", GH + "llnl/OGhidra")]},
        {"name": "ReVa", "repo": "cyberkaida/reverse-engineering-assistant", "tags": "🟢",
         "desc": "Ghidra-focused reverse-engineering assistant with MCP support, Claude Skills integration, and long-form analysis workflows.",
         "related": [("GhidraMCP", GH + "LaurieWired/GhidraMCP"), ("GhidrAssistMCP", GH + "symgraph/GhidrAssistMCP")]},
        {"name": "GhidrAssistMCP", "repo": "symgraph/GhidrAssistMCP", "tags": "🟢",
         "desc": "Native Ghidra MCP extension with broad tool coverage, headless support, and security-sensitive tool gating.",
         "related": [("ReVa", GH + "cyberkaida/reverse-engineering-assistant"), ("ghidra-mcp", GH + "bethington/ghidra-mcp")]},
        {"name": "ghidra-mcp", "repo": "bethington/ghidra-mcp", "tags": "🟢",
         "desc": "Ghidra MCP server with large tool coverage, GUI plugin, headless server, and lazy tool loading.",
         "related": [("GhidrAssistMCP", GH + "symgraph/GhidrAssistMCP")]},
        {"name": "GhidrOllama", "repo": "lr-m/GhidrOllama", "tags": "🟢⚠️",
         "desc": "Ghidra script using the Ollama API for function analysis/renaming.",
         "related": [("OGhidra", GH + "llnl/OGhidra"), ("GhidraMCP", GH + "LaurieWired/GhidraMCP")]},
        {"name": "GhidraGPT", "repo": "weirdmachine64/GhidraGPT", "tags": "🟢",
         "desc": "Ghidra plugin that integrates LLMs for automated code refactoring and analysis.",
         "related": [("GhidraMCP", GH + "LaurieWired/GhidraMCP"), ("ReVa", GH + "cyberkaida/reverse-engineering-assistant")]},
        {"name": "LLM4Decompile", "repo": "albertan017/LLM4Decompile", "tags": "🟢🔬⚠️",
         "desc": "Research project for binary-to-C decompilation with LLMs; code is MIT, but model weights use a more restrictive license."},
        {"name": "x64dbg_mcp", "repo": "bromoket/x64dbg_mcp", "tags": "🟢",
         "desc": "MCP server exposing x64dbg debugging and reverse-engineering operations to AI clients."},
        {"name": "binaryninja-mcp", "repo": "MCPPhalanx/binaryninja-mcp", "tags": "🟢",
         "desc": "MCP server for Binary Ninja-assisted reverse engineering."},
        {"name": "OGhidra", "repo": "llnl/OGhidra", "tags": "🟢", "org": "Lawrence Livermore National Lab",
         "desc": "Natural-language Ghidra analysis via Ollama.",
         "related": [("GhidrOllama", GH + "lr-m/GhidrOllama"), ("GhidraMCP", GH + "LaurieWired/GhidraMCP")]},
        {"name": "ghidra_tools (G-3PO)", "repo": "tenable/ghidra_tools", "tags": "🟢", "org": "Tenable",
         "desc": "Ghidra plugin for AI-assisted decompiled-code analysis."},
        {"name": "gpt-wpre", "repo": "moyix/gpt-wpre", "tags": "🔬",
         "desc": "Whole-program reverse engineering with GPT-3."},
        {"name": "burpgpt", "repo": "aress31/burpgpt", "tags": "🟢",
         "desc": "Burp Suite extension integrating GPT for passive scanning.",
         "related": [("Burp-extension-for-GPT", GH + "tenable/Burp-extension-for-GPT")]},
        {"name": "Burp-extension-for-GPT", "repo": "tenable/Burp-extension-for-GPT", "tags": "🟢", "org": "Tenable",
         "desc": "Burp extension to analyze HTTP traffic with GPT.",
         "related": [("burpgpt", GH + "aress31/burpgpt")]},
    ],
    None,
))

SECTIONS.append((
    "LLM Red-Teaming & Guardrails",
    "llm-red-teaming--guardrails",
    "Tools for attacking and defending LLM applications themselves.",
    [
        ("Scanners, Evals & Guardrails", [
            {"name": "garak", "repo": "NVIDIA/garak", "tags": "🟢", "org": "NVIDIA",
             "desc": "The LLM vulnerability scanner — probes for prompt injection, jailbreaks, data leakage, and more.",
             "related": [("PyRIT", GH + "microsoft/PyRIT"), ("promptfoo", GH + "promptfoo/promptfoo")]},
            {"name": "PyRIT", "repo": "microsoft/PyRIT", "tags": "🟢", "org": "Microsoft",
             "desc": "Python Risk Identification Tool; battle-tested across 100+ GenAI red-team operations."},
            {"name": "promptfoo", "repo": "promptfoo/promptfoo", "tags": "🟢",
             "desc": "LLM eval + red-teaming/pentesting CLI with 50+ attack plugins (MIT).",
             "note": "*Note: OpenAI announced an acquisition agreement in March 2026; remains MIT-licensed — track governance.*"},
            {"name": "Augustus", "repo": "praetorian-inc/augustus", "tags": "🟢", "org": "Praetorian",
             "desc": "Single-binary LLM security testing framework for prompt injection, jailbreaks, and adversarial attacks across many providers.",
             "related": [("garak", GH + "NVIDIA/garak"), ("PyRIT", GH + "microsoft/PyRIT")]},
            {"name": "agentic_security", "repo": "msoedov/agentic_security", "tags": "🟢",
             "desc": "Agentic LLM vulnerability scanner and AI red-team kit for jailbreaks, prompt injection, fuzzing, and API stress testing.",
             "related": [("garak", GH + "NVIDIA/garak"), SPIKEE]},
            {"name": "DeepTeam", "repo": "confident-ai/deepteam", "tags": "🟢",
             "desc": "Open-source framework for red-teaming LLMs and LLM systems across jailbreaks, prompt injection, data leakage, and safety risks."},
            {"name": "Moonshot", "repo": "aiverify-foundation/moonshot", "tags": "🟢", "org": "AI Verify Foundation",
             "desc": "Modular tool for benchmarking, red-teaming, and evaluating LLM applications with custom connectors and recipes."},
            {"name": "Guardrails AI", "repo": "guardrails-ai/guardrails", "tags": "🟢", "org": "Guardrails AI",
             "desc": "Python framework for adding input/output guards, validators, structured-output controls, and Guardrails Hub checks to LLM applications.",
             "related": [("NeMo Guardrails", GH + "NVIDIA-NeMo/Guardrails"), ("LLM Guard", GH + "protectai/llm-guard")]},
            {"name": "Giskard", "repo": "Giskard-AI/giskard-oss", "tags": "🟢", "org": "Giskard AI",
             "desc": "Open-source evaluation, testing, and red-teaming framework for LLM agents, including agent vulnerability scanning and RAG evaluation workflows.",
             "related": [("Moonshot", GH + "aiverify-foundation/moonshot"), ("promptfoo", GH + "promptfoo/promptfoo")]},
            {"name": "LangKit", "repo": "whylabs/langkit", "tags": "🟢", "org": "WhyLabs",
             "desc": "LLM monitoring toolkit extracting safety/security signals such as jailbreak similarity, prompt-injection similarity, hallucination checks, PII patterns, toxicity, and refusal metrics."},
            {"name": "LLM Guard", "repo": "protectai/llm-guard", "tags": "🟢", "org": "Protect AI",
             "desc": "Suite of input/output scanners (PII, prompt injection, etc.).",
             "related": [("Rebuff", GH + "protectai/rebuff")]},
            {"name": "Rebuff", "repo": "protectai/rebuff", "tags": "🟢", "org": "Protect AI",
             "desc": "Archived prompt-injection detector (heuristics + LLM + vector DB + canary tokens).",
             "related": [("LLM Guard", GH + "protectai/llm-guard")]},
            {"name": "NeMo Guardrails", "repo": "NVIDIA-NeMo/Guardrails", "tags": "🟢", "org": "NVIDIA",
             "desc": "Programmable guardrails (input/output/dialog/retrieval rails) for LLM apps."},
            {"name": "PurpleLlama", "repo": "meta-llama/PurpleLlama", "tags": "🟢", "org": "Meta",
             "desc": "Llama Guard classifiers, CodeShield, and CyberSecEval."},
            {"name": "LLAMATOR", "repo": "LLAMATOR-Core/llamator", "tags": "🟢⚠️",
             "desc": "Red-teaming framework for chatbots and GenAI systems; CC BY-NC-SA 4.0 licensed."},
            {"name": "Vigil", "repo": "deadbits/vigil-llm", "tags": "🟢🔬",
             "desc": "Library/REST API to scan prompts and responses for prompt injection."},
            {"name": "Counterfit", "repo": "Azure/counterfit", "tags": "🟢", "org": "Microsoft",
             "desc": "ML/AI penetration-testing automation tool."},
            {"name": "AI-Red-Teaming-Playground-Labs", "repo": "microsoft/AI-Red-Teaming-Playground-Labs", "tags": "🟢", "org": "Microsoft",
             "desc": "CTFd-based AI red-team training challenges."},
            {"name": "EasyJailbreak", "repo": "EasyJailbreak/EasyJailbreak", "tags": "🟢🔬",
             "desc": "Framework for building and testing adversarial jailbreak prompts."},
            {"name": "TextAttack", "repo": "QData/TextAttack", "tags": "🟢🔬",
             "desc": "Python framework for adversarial attacks, data augmentation, and training for NLP models; useful for robustness testing beyond chat-only LLM scanners."},
            {"name": "GPTFuzz", "repo": "sherdencooper/GPTFuzz", "tags": "🟢🔬",
             "desc": "Research framework for red-teaming LLMs with auto-generated jailbreak prompts."},
            {"name": "HarmBench", "repo": "centerforaisafety/HarmBench", "tags": "🟢🔬", "org": "Center for AI Safety",
             "desc": "ICML 2024 standardized evaluation framework for automated red-teaming and robust-refusal benchmarking.",
             "related": [("JailbreakBench", GH + "JailbreakBench/jailbreakbench")]},
            {"name": "llm-attacks (GCG)", "repo": "llm-attacks/llm-attacks", "tags": "🟢🔬",
             "desc": "Canonical Greedy Coordinate Gradient adversarial-suffix attack implementation for transferable attacks on aligned language models.",
             "related": [("nanoGCG", GH + "GraySwanAI/nanoGCG")]},
            {"name": "nanoGCG", "repo": "GraySwanAI/nanoGCG", "tags": "🟢",
             "desc": "Fast, lightweight PyTorch implementation of the GCG adversarial-suffix algorithm.",
             "related": [("llm-attacks (GCG)", GH + "llm-attacks/llm-attacks")]},
            {"name": "JailbreakBench", "repo": "JailbreakBench/jailbreakbench", "tags": "🟢🔬",
             "desc": "NeurIPS 2024 open robustness benchmark and leaderboard for generating and defending against LLM jailbreaks."},
            {"name": "Open-Prompt-Injection", "repo": "liu00222/Open-Prompt-Injection", "tags": "🟢🔬",
             "desc": "Open-source toolkit and benchmark for implementing and evaluating prompt-injection attacks, defenses, and LLM-integrated applications."},
            {"name": "Whistleblower", "repo": "Repello-AI/whistleblower", "tags": "🟢⚠️", "org": "Repello AI",
             "desc": "Offensive testing tool for inferring system prompts and discovering capabilities of LLM applications exposed through APIs.",
             "note": "— **note:** no LICENSE file found."},
            {"name": "LLMmap", "repo": "pasquini-dario/LLMmap", "tags": "🟢🔬",
             "desc": "Minimal-query fingerprinting tool for identifying LLMs from behavioral traces, with a pretrained open-set inference model."},
            {"name": "llm-security", "repo": "greshake/llm-security", "tags": "🔬",
             "desc": "Original PoC for indirect prompt-injection attacks."},
            {"name": "JailbreakLLMs", "repo": "TrustAIRLab/JailbreakLLMs", "tags": "🔬⚠️",
             "desc": "Research dataset of 6,387 ChatGPT prompts, including in-the-wild jailbreak prompts from Reddit, Discord, websites, and open datasets."},
            {"name": "Do-Not-Answer", "repo": "Libr-AI/do-not-answer", "tags": "🟢🔬",
             "desc": "Dataset for evaluating LLM safeguards on unsafe or policy-sensitive prompts."},
            {"name": "prompt-injection-defenses", "repo": "tldrsec/prompt-injection-defenses", "tags": "🟢⚠️",
             "desc": "Curated catalog of practical defenses against prompt injection."},
        ]),
        ("Prompt-Injection Classifier Models", [
            {"kind": "hf_model", "name": "Wolf Defender Prompt Injection", "model": "patronus-studio/wolf-defender-prompt-injection", "tags": "🟢", "org": "Patronus Studio / Casdo Labs",
             "desc": "Hugging Face text-classification model for prompt-injection detection in agents, chatbots, and CI workflows.",
             "license": "Apache-2.0", "access": "open", "artifacts": "Safetensors, ONNX"},
            {"kind": "hf_model", "name": "DeBERTa v3 Prompt Injection v2", "model": "protectai/deberta-v3-base-prompt-injection-v2", "tags": "🟢", "org": "Protect AI",
             "desc": "Apache-licensed prompt-injection classifier usable via Transformers pipelines and ONNX.",
             "license": "Apache-2.0", "access": "open", "artifacts": "Safetensors, ONNX"},
            {"kind": "hf_model", "name": "PromptGuard", "model": "codeintegrity-ai/promptguard", "tags": "🟢⚠️", "org": "CodeIntegrity AI",
             "desc": "ModernBERT-based prompt-injection and jailbreak classifier.",
             "license": "Apache-2.0", "access": "gated auto", "artifacts": "Safetensors"},
            {"kind": "hf_model", "name": "Prompt Guard 86M", "model": "meta-llama/Prompt-Guard-86M", "tags": "🟠⚠️", "org": "Meta",
             "desc": "Meta prompt-injection and jailbreak classifier from the Llama Guard family.",
             "license": "Llama 3.1", "access": "gated manual", "artifacts": "Safetensors"},
            {"kind": "hf_model", "name": "prompt-injection-sentinel", "model": "qualifire/prompt-injection-sentinel", "tags": "🔬⚠️", "org": "Qualifire",
             "desc": "ModernBERT-large classifier for prompt-injection and jailbreak detection.",
             "license": "other", "access": "gated auto", "artifacts": "Safetensors"},
        ]),
        ("Specialty Security LLMs", [
            {"name": "SecGPT", "repo": "Clouditera/SecGPT", "tags": "🟢", "org": "Clouditera",
             "desc": "Open cybersecurity-tuned LLM family for vulnerability analysis, log/traffic investigation, anomaly detection, attack/defense reasoning, command analysis, and security Q&A.",
             "related": [("SecGPT model", HF + "clouditera/secgpt")]},
        ]),
    ],
    None,
))

SECTIONS.append((
    "LLM Honeypots & Deception",
    "llm-honeypots--deception",
    "Honeypots and deception that use LLMs to simulate convincing systems.",
    [
        {"name": "Beelzebub", "repo": "mariocandela/beelzebub", "tags": "🟢",
         "desc": "Low-code honeypot using LLMs to simulate SSH/HTTP/MCP services (Go)."},
        {"name": "DECEIVE", "repo": "splunk/DECEIVE", "tags": "🟢🔬", "org": "Splunk",
         "desc": "Proof-of-concept LLM-powered SSH honeypot that evaluates sessions as benign, suspicious, or malicious."},
        {"name": "TRAP", "repo": "parameterlab/trap", "tags": "🟢🔬",
         "desc": "Research code for Targeted Random Adversarial Prompt honeypots that identify black-box LLM usage through model-specific prompt suffixes (ACL 2024 Findings)."},
        {"name": "shelLM", "repo": "stratosphereips/shelLM", "tags": "🟢🔬",
         "desc": "LLM-powered SSH honeypot (paper *\"LLM in the Shell\"*).",
         "related": [("VelLMes", GH + "stratosphereips/VelLMes-AI-Honeypot")]},
        {"name": "VelLMes", "repo": "stratosphereips/VelLMes-AI-Honeypot", "tags": "🟢🔬",
         "desc": "Multi-protocol LLM honeypot framework (successor to shelLM).",
         "related": [("shelLM", GH + "stratosphereips/shelLM")]},
        {"name": "llm-honeypot", "repo": "PalisadeResearch/llm-honeypot", "tags": "🔬⚠️", "org": "Palisade Research",
         "desc": "Cowrie SSH honeypot extended with prompt-injection traps to detect LLM hacker agents."},
    ],
    None,
))

SECTIONS.append((
    "CTF / Exploit / Bug-Bounty Agents & Benchmarks",
    "ctf--exploit--bug-bounty-agents--benchmarks",
    "Offensive agents and the benchmarks used to evaluate them.",
    [
        {"name": "SWE-agent (EnIGMA)", "repo": "SWE-agent/SWE-agent", "tags": "🟢🔬",
         "desc": "EnIGMA offensive-CTF mode; SOTA on NYU CTF, InterCode-CTF, and Cybench (v0.7 branch).",
         "related": [("Cybench", GH + "andyzorigin/cybench"), ("NYU CTF Bench", GH + "NYU-LLM-CTF/NYU_CTF_Bench"),
                     ("InterCode", GH + "princeton-nlp/intercode")]},
        {"name": "Cybench", "repo": "andyzorigin/cybench", "tags": "🔬",
         "desc": "40 professional CTF tasks across 4 competitions; widely used by AI safety institutes."},
        {"name": "NYU CTF Bench", "repo": "NYU-LLM-CTF/NYU_CTF_Bench", "tags": "🔬",
         "desc": "Dockerized CSAW CTF challenges for LLM-agent evaluation."},
        {"name": "CTFTiny", "repo": "NYU-LLM-CTF/CTFTiny", "tags": "🔬⚠️",
         "desc": "Lightweight CTF benchmark from the NYU LLM CTF group; GPL-2.0 licensed.",
         "related": [("NYU CTF Bench", GH + "NYU-LLM-CTF/NYU_CTF_Bench")]},
        {"name": "InterCode", "repo": "princeton-nlp/intercode", "tags": "🔬",
         "desc": "Interactive-coding benchmark incl. InterCode-CTF."},
        {"name": "inspect_evals", "repo": "UKGovernmentBEIS/inspect_evals", "tags": "🟢🔬", "org": "UK AI Security Institute",
         "desc": "Maintained Inspect AI evaluation suite containing multiple cyber benchmarks and tasks."},
        {"name": "BountyBench", "repo": "bountybench/bountybench", "tags": "🔬",
         "desc": "25 real systems / 40 bug bounties for Detect-Exploit-Patch evaluation."},
        {"name": "Cyber-Zero", "repo": "amazon-science/Cyber-Zero", "tags": "🔬", "org": "Amazon Science",
         "desc": "Trains cybersecurity agents without runtime; ships an EnIGMA+ scaffold.",
         "sources": [SWE_AGENT], "related": [SWE_AGENT]},
        {"name": "ExploitBench", "repo": "exploitbench/exploitbench", "tags": "🔬",
         "desc": "Measures AI-agent progress on V8/Chromium exploit ladders."},
        {"name": "AI Goat", "repo": "dhammon/ai-goat", "tags": "🟢🔬⚠️",
         "desc": "Vulnerable-by-design local LLM CTF for learning prompt injection, insecure output handling, data leakage, excessive agency, and related LLM app risks.",
         "note": "— **note:** GPL-2.0 licensed."},
        {"name": "Damn Vulnerable LLM Agent", "repo": "ReversecLabs/damn-vulnerable-llm-agent", "tags": "🟢🔬", "org": "ReversecLabs / WithSecure",
         "desc": "Deliberately vulnerable LangChain ReAct agent for practicing prompt-injection and Thought/Action/Observation injection attacks.",
         "related": [SPIKEE]},
        {"name": "claude-bug-bounty", "repo": "shuvonsec/claude-bug-bounty", "tags": "🟢",
         "desc": "Claude Code plugin orchestrating recon → vuln classes → reporting."},
        {"name": "Bug-Bounty-Agents", "repo": "matty69v/Bug-Bounty-Agents", "tags": "🟢",
         "desc": "43 AI agent personas for Claude Code / Copilot / Cursor across the bug-bounty lifecycle."},
        {"name": "ai-exploits", "repo": "protectai/ai-exploits", "tags": "🟢", "org": "Protect AI",
         "desc": "Real-world AI/ML exploits (Metasploit modules + Nuclei templates) for MLflow, Ray, H2O."},
    ],
    None,
))

SECTIONS.append((
    "Cloud / IaC / DFIR / OSINT / Phishing",
    "cloud--iac--dfir--osint--phishing",
    "AI tooling for cloud/IaC security, digital forensics, OSINT, and phishing detection.",
    [
        {"name": "EscalateGPT", "repo": "tenable/EscalateGPT", "tags": "🟢", "org": "Tenable",
         "desc": "GPT-based discovery of privilege-escalation paths in AWS IAM policies."},
        {"name": "MemoryInvestigator", "repo": "jan-hendrik-lang/MemoryInvestigator", "tags": "🔬",
         "desc": "Volatility 3 + LLM + RAG for memory-forensic triage.",
         "related": [("Volatility-MCP-Server", GH + "bornpresident/Volatility-MCP-Server")]},
        {"name": "Volatility-MCP-Server", "repo": "bornpresident/Volatility-MCP-Server", "tags": "🟢",
         "desc": "MCP exposing Volatility 3 plugins for natural-language memory forensics.",
         "related": [("MemoryInvestigator", GH + "jan-hendrik-lang/MemoryInvestigator")]},
        {"name": "llm_osint", "repo": "sshh12/llm_osint", "tags": "🟢🔬",
         "desc": "Proof-of-concept LLM OSINT framework using knowledge and web agents for internet research workflows."},
        {"name": "ai_osint", "repo": "7WaySecurity/ai_osint", "tags": "🟢",
         "desc": "Curated AI-OSINT dorks, queries, and techniques for discovering exposed LLM and AI infrastructure."},
        {"name": "PhishLLM", "repo": "code-philia/PhishLLM", "tags": "🔬⚠️",
         "desc": "Reference-less phishing detection via LLM brand recognition (USENIX'24).",
         "related": [("PhishVLM", GH + "code-philia/PhishVLM")]},
        {"name": "mcp-dnstwist", "repo": "BurtTheCoder/mcp-dnstwist", "tags": "🟢",
         "desc": "MCP server for dnstwist DNS fuzzing to support typosquatting, phishing, and lookalike-domain analysis."},
        {"name": "osintgpt", "repo": "estebanpdl/osintgpt", "tags": "🟢⚠️",
         "desc": "OpenAI embeddings + Qdrant over OSINT corpora."},
        {"name": "gpt-osint", "repo": "gigz/gpt-osint", "tags": "🟢",
         "desc": "Web-based GPT-4 OSINT tool over social-media dumps and CSVs."},
    ],
    None,
))

# Related awesome lists (repos -> badges too)
AWESOME = [
    ("awesome-llm-cybersecurity-tools", "tenable/awesome-llm-cybersecurity-tools", "Tenable's list (archived but a strong reference)."),
    ("Awesome-LLM4Cybersecurity", "tmylla/Awesome-LLM4Cybersecurity", "600+ papers on LLMs for cybersecurity."),
    ("awesome-ai-cybersecurity", "ElNiak/awesome-ai-cybersecurity", "Broad AI-for-security collection."),
    ("awesome-genai-cyberhub", "Ashfaaq98/awesome-genai-cyberhub", "GenAI-driven cybersecurity resources."),
    ("awesome-ai-security", "gmh5225/awesome-ai-security", "For pentesters, bug hunters, and researchers."),
    ("awesome-ai-security", "ottosulin/awesome-ai-security", "AI security resources."),
    ("Awesome-AI-Security", "TalEliyahu/Awesome-AI-Security", "AI security resources."),
    ("Awesome-AI-For-Security", "AmanPriyanshu/Awesome-AI-For-Security", "AI-for-security tools, papers, and datasets."),
    ("awesome-cybersecurity-agentic-ai", "raphabot/awesome-cybersecurity-agentic-ai", "Agentic-AI cybersecurity tools and security MCP servers."),
    ("open-source-llm-scanners", "psiinon/open-source-llm-scanners", "Open-source LLM scanners and testing tools."),
    ("awesome-mcp-security", "Puliczek/awesome-mcp-security", "MCP security resources, tools, writeups, and server/client risk references."),
    ("awesome-ml-security", "trailofbits/awesome-ml-security", "Trail of Bits' curated machine-learning security resources."),
    ("awesome-ml-privacy-attacks", "stratosphereips/awesome-ml-privacy-attacks", "Machine-learning privacy-attack papers and resources."),
    ("awesome-ml-for-cybersecurity", "jivoi/awesome-ml-for-cybersecurity", "Large classic list of machine-learning-for-cybersecurity resources (stale-ish but still useful)."),
    ("Awesome-AI4DevSecOps", "awsm-research/Awesome-AI4DevSecOps", "Taxonomy of AI-driven security solutions for DevSecOps."),
    ("awesome-llm-security", "corca-ai/awesome-llm-security", "Securing LLMs."),
    ("awesome-security-for-ai", "zmre/awesome-security-for-ai", "Products for securing AI systems."),
    ("awesome-gpt-security", "cckuailong/awesome-gpt-security", "GPT/LLM security tools and cases."),
    ("awesome-threat-intelligence", "hslatman/awesome-threat-intelligence", "Classic CTI list (pairs with the AI-CTI section)."),
]


def build():
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
    out.append("GitHub-hosted entries show live **★ stars** and **last-commit** badges (rendered from the GitHub API by shields.io). Hugging Face model entries show license, access, and artifact metadata. Ordering within a section favors flagship and actively maintained projects.")
    out.append("")
    out.append("---")
    out.append("")
    # Contents
    out.append("## Contents")
    out.append("")
    for title, anchor, _intro, body, _foot in SECTIONS:
        out.append(f"- [{title}](#{anchor})")
        if body and isinstance(body[0], tuple):
            for sub_title, _ in body:
                out.append(f"  - [{sub_title}](#{github_anchor(sub_title)})")
    out.append("- [Related Awesome Lists](#related-awesome-lists)")
    out.append("- [Contributing](#contributing)")
    out.append("- [License](#license)")
    out.append("")
    out.append("---")
    out.append("")
    # Sections
    for title, anchor, intro, body, foot in SECTIONS:
        out.append(f"## {title}")
        out.append("")
        if intro:
            out.append(intro)
            out.append("")
        if body and isinstance(body[0], tuple):
            for sub_title, entries in body:
                out.append(f"### {sub_title}")
                out.append("")
                for e in entries:
                    out.append(render_entry(e))
                out.append("")
        else:
            for e in body:
                out.append(render_entry(e))
            out.append("")
        if foot:
            out.append(foot)
            out.append("")
        out.append("---")
        out.append("")
    # Awesome lists
    out.append("## Related Awesome Lists")
    out.append("")
    for name, repo, desc in AWESOME:
        out.append(f"- **[{name}]({GH}{repo})** — {desc} {badges(repo)}")
    out.append("")
    out.append("---")
    out.append("")
    # Contributing
    out.append("## Contributing")
    out.append("")
    out.append("Contributions are welcome! Open a PR adding entries in the format below, keeping each section sorted by relevance/maintenance.")
    out.append("")
    out.append("```")
    out.append("- **[name](repo-url)** 🟢/🔬/🟠/⚠️ — One-line description. *(maintainer/org)* <stars badge> <last-commit badge>")
    out.append("  - **Sources:** [upstream A](url) · [upstream B](url)       # optional — projects this is built on")
    out.append("  - **Related:** [sibling tool](url) · [related project](url) # optional — peers / forks / successors")
    out.append("```")
    out.append("")
    out.append("Badges use the dynamic shields.io GitHub endpoints, so they update automatically:")
    out.append("")
    out.append("```")
    out.append("[![stars](https://img.shields.io/github/stars/OWNER/REPO?style=flat-square&label=★)](https://github.com/OWNER/REPO)")
    out.append("[![updated](https://img.shields.io/github/last-commit/OWNER/REPO?style=flat-square&label=updated)](https://github.com/OWNER/REPO)")
    out.append("```")
    out.append("")
    out.append("Guidelines: link the canonical upstream repo (not a fork); verify the URL resolves; tag the correct type and add ⚠️ for non-permissive, non-commercial, or unclear/no-license projects; prefer real, installable projects over blog-only references.")
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
    parser.add_argument("-o", "--output", type=Path,
                        default=Path(__file__).with_name("README.md"),
                        help="README path to write or check")
    parser.add_argument("--check", action="store_true",
                        help="fail if the output README is not up to date")
    args = parser.parse_args()

    rendered = build()
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
