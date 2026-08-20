# Awesome AI Security Tools [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of **public-source, research, and commercial** tools for AI security and AI-assisted cybersecurity — autotriage, agent security, AI/ML supply chain, pentest agents, AI SAST, LLM-driven fuzzing, threat intelligence, SOC/SIEM triage, reverse engineering, LLM red-teaming, and more.

[![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing)

**Type legend:** 🟢 public source / open-source · 🔬 research (paper / benchmark / dataset / framework) · 🟠 commercial with open components · ⚠️ restrictive, non-commercial, or unclear/no license — check before use.

GitHub-hosted entries show static **★ stars** and **last-commit** snapshots; refresh them with `python3 scripts/update_github_metrics.py` before release. Latest snapshot: 2026-08-17. Hugging Face model entries show license, access, and artifact metadata. Ordering within a section favors flagship and actively maintained projects.

---

## Contents

- [Autotriage of Security Findings](#autotriage-of-security-findings)
- [AI Agent & Coding-Agent Security](#ai-agent--coding-agent-security)
  - [Scanners & Auditors](#scanners--auditors)
  - [Frameworks, Rule Standards & Benchmarks](#frameworks-rule-standards--benchmarks)
  - [Runtime Protection & Enforcement](#runtime-protection--enforcement)
- [AI/ML Supply Chain & Model Security](#aiml-supply-chain--model-security)
- [Pentest & Red-Team Agents](#pentest--red-team-agents)
- [AI-Powered Recon & Narrow ML Tools](#ai-powered-recon--narrow-ml-tools)
  - [Subdomain & DNS Prediction](#subdomain--dns-prediction)
  - [Recon Screenshot Triage](#recon-screenshot-triage)
  - [Software / Tech Fingerprinting](#software--tech-fingerprinting)
  - [AI-Assisted Fuzzing](#ai-assisted-fuzzing)
  - [Password / Credential ML](#password--credential-ml)
  - [Phishing Detection (Visual / URL)](#phishing-detection-visual--url)
  - [AI/ML-Assisted Detection Rules & Engines](#aiml-assisted-detection-rules--engines)
  - [Defensive Trained-Model Detectors](#defensive-trained-model-detectors)
- [AI-Powered SAST & Secure Code Review](#ai-powered-sast--secure-code-review)
- [AI-Powered Threat Modeling](#ai-powered-threat-modeling)
- [LLM-Driven Fuzzing](#llm-driven-fuzzing)
  - [Harness / target generation](#harness--target-generation)
  - [Fuzzing the LLM](#fuzzing-the-llm)
- [Threat Intelligence](#threat-intelligence)
- [Log Analysis / SIEM / SOC Triage](#log-analysis--siem--soc-triage)
- [Reverse Engineering](#reverse-engineering)
- [LLM Red-Teaming & Guardrails](#llm-red-teaming--guardrails)
  - [Scanners, Evals & Guardrails](#scanners-evals--guardrails)
  - [Prompt-Injection Classifier Models](#prompt-injection-classifier-models)
  - [Specialty Security LLMs](#specialty-security-llms)
- [LLM Honeypots & Deception](#llm-honeypots--deception)
- [CTF / Exploit / Bug-Bounty Agents & Benchmarks](#ctf--exploit--bug-bounty-agents--benchmarks)
- [Cloud / IaC / DFIR / OSINT / Phishing](#cloud--iac--dfir--osint--phishing)
- [Related Awesome Lists](#related-awesome-lists)
- [Contributing](#contributing)
- [Contact](#contact)
- [License](#license)

---

## Autotriage of Security Findings

AI/LLM tools that triage, deduplicate, prioritize, or validate the output of scanners and finding sources.

- **[nuclei-autotriage](https://github.com/cyberok-org/nuclei-autotriage)** 🟢⚠️ — Two-stage LLM triage (falsifier + red-team pass) of Nuclei JSONL findings via OpenAI-compatible endpoints (vLLM/Ollama). *(CyberOK)* — **note:** restrictive personal/non-commercial EULA, not a permissive OSS license. *(★ 1 · updated 2026-05-25)*
  - **Related:** [agent-audit](https://github.com/scadastrangelove/agent-audit) · [asamm](https://github.com/scadastrangelove/asamm)
- **[seclab-taskflow-agent](https://github.com/GitHubSecurityLab/seclab-taskflow-agent)** 🟢 — YAML-driven taskflow agent framework for triaging CodeQL/SAST alerts and filtering false positives. *(GitHub Security Lab)* *(★ 221 · updated 2026-08-17)*
  - **Related:** [SigmaOptimizer](https://github.com/YusukeJustinNakajima/SigmaOptimizer)
- **[honeyslop](https://github.com/gadievron/honeyslop)** 🟢 — Code-canary decoys to triage AI-hallucinated ("slop") vulnerability reports flooding bug-bounty programs. *(★ 97 · updated 2026-05-20)*
- **[nano-analyzer](https://github.com/weareaisle/nano-analyzer)** 🟢🔬 — Minimal three-stage LLM pipeline (context → scan → skeptical triage) for zero-day discovery in C/C++. *(AISLE)* *(★ 307 · updated 2026-04-14)*
- **[SigmaOptimizer](https://github.com/YusukeJustinNakajima/SigmaOptimizer)** 🟢 — Generates, tests, and refines Sigma rules from real logs with false-positive checking. *(★ 11 · updated 2025-08-01)*
  - **Related:** [soctalk](https://github.com/soctalk/soctalk) · [seclab-taskflow-agent](https://github.com/GitHubSecurityLab/seclab-taskflow-agent)
- **[ai-soc-triage-assistant](https://github.com/pranavibunny/ai-soc-triage-assistant)** 🟢⚠️ — SOC alert triage assistant with prompt-injection guardrails, output validation, and MITRE ATT&CK mapping. *(★ 0 · updated 2026-02-23)*

> See also: OpenAI's *Aardvark* research preview — public references exist, but there is no standalone installable repository to badge here.

---

## AI Agent & Coding-Agent Security

Securing the AI agents themselves — auditing coding agents (Claude Code, Codex, OpenClaw), scanning skills / plugins / MCP manifests, and governance for agentic development. A fast-moving 2026 category, split below by role.

### Scanners & Auditors

- **[agent-audit](https://github.com/scadastrangelove/agent-audit)** 🟢 — Forensic auditor for local AI coding agents (Claude Code, Codex CLI, OpenClaw) **and** project-surface scanner for repos shipping skills, plugins, and MCP manifests; 296 bundled rules across native + imported detector families, with optional LLM cross-verification. *(CyberOK / S. Gordeychik)* *(★ 15 · updated 2026-07-15)*
  - **Sources:** [asamm](https://github.com/scadastrangelove/asamm) · [ATR – Agent Threat Rules](https://github.com/Agent-Threat-Rule/agent-threat-rules) · [aguara](https://github.com/garagon/aguara) · [Cisco AI Defense – skill-scanner](https://github.com/cisco-ai-defense/skill-scanner)
  - **Related:** [asamm](https://github.com/scadastrangelove/asamm) · [aguara](https://github.com/garagon/aguara) · [agentguard](https://github.com/GoPlusSecurity/agentguard) · [agentic-radar](https://github.com/splx-ai/agentic-radar) · [nuclei-autotriage](https://github.com/cyberok-org/nuclei-autotriage)
- **[AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard)** 🟢 — Full-stack AI red-teaming platform covering OpenClaw security scan, agent scan, skills scan, MCP scan, AI-infra vulnerability scan, and LLM jailbreak evaluation. *(Tencent Zhuque Lab)* *(★ 4,514 · updated 2026-08-17)*
  - **Related:** [agent-audit](https://github.com/scadastrangelove/agent-audit) · [aguara](https://github.com/garagon/aguara) · [Cisco AI Defense – skill-scanner](https://github.com/cisco-ai-defense/skill-scanner) · [Cisco AI Defense – mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)
- **[SkillSpector](https://github.com/NVIDIA/SkillSpector)** 🟢 — Security scanner for AI-agent skills used by Claude Code, Codex CLI, Gemini CLI, and similar ecosystems; combines static analysis, AST/YARA/taint checks, optional LLM semantic review, MCP least-privilege/tool-poisoning checks, risk scoring, and SARIF/JSON/Markdown output. *(NVIDIA)* *(★ 14,696 · updated 2026-08-15)*
  - **Related:** [Cisco AI Defense – skill-scanner](https://github.com/cisco-ai-defense/skill-scanner) · [skilltotal](https://github.com/pezhik/skilltotal) · [Snyk Agent Scan](https://github.com/snyk/agent-scan) · [Cisco AI Defense – mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)
- **[Ramparts](https://github.com/highflame-ai/ramparts)** 🟢 — Rust scanner for MCP servers and agent-skill bundles with YARA rules, optional LLM analysis, OSV/CVE lookups, OWASP MCP Top 10 mapping, and SARIF/JSON/Markdown reports. *(★ 96 · updated 2026-08-07)*
  - **Related:** [SkillSpector](https://github.com/NVIDIA/SkillSpector) · [Cisco AI Defense – skill-scanner](https://github.com/cisco-ai-defense/skill-scanner) · [Cisco AI Defense – mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)
- **[mcp-armor](https://github.com/aira-security/mcp-armor)** 🟢 — Local MCP security scanner with auto-discovery for agentic IDE configs, tool/resource/prompt inventory, prompt-injection checks, rug-pull and tool-poisoning detection, baseline drift monitoring, and JSON/Markdown reports. *(Aira Security)* *(★ 120 · updated 2026-03-27)*
  - **Related:** [SkillSpector](https://github.com/NVIDIA/SkillSpector) · [Ramparts](https://github.com/highflame-ai/ramparts) · [Cisco AI Defense – mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)
- **[aguara](https://github.com/garagon/aguara)** 🟢 — Single-binary static scanner (Go, no LLM) for AI-agent skills and MCP servers; multi-layer engine (pattern + NLP + taint tracking + rug-pull detection). Companion **[aguara-mcp](https://github.com/garagon/mcp-aguara)** exposes scanning as an MCP tool. *(★ 86 · updated 2026-08-12)*
  - **Related:** [aguara-mcp](https://github.com/garagon/mcp-aguara) · [agent-audit](https://github.com/scadastrangelove/agent-audit) · [Snyk Agent Scan](https://github.com/snyk/agent-scan) · [Cisco AI Defense – skill-scanner](https://github.com/cisco-ai-defense/skill-scanner)
- **[agent-scan](https://github.com/snyk/agent-scan)** 🟢 — Security scanner for AI agents, MCP servers, and agent skills; the successor path for the original Invariant Labs mcp-scan work. *(Snyk)* *(★ 2,913 · updated 2026-08-13)*
  - **Related:** [aguara](https://github.com/garagon/aguara) · [Cisco AI Defense – mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner) · [Cisco AI Defense – skill-scanner](https://github.com/cisco-ai-defense/skill-scanner)
- **[inkog](https://github.com/inkog-io/inkog)** 🟠 — Commercial-backed static security scanner for AI agents across LangChain, LangGraph, CrewAI, AutoGen, and no-code workflows; Apache-2.0 CLI with proprietary deep-scan engine. *(Inkog)* *(★ 28 · updated 2026-06-07)*
  - **Related:** [Snyk Agent Scan](https://github.com/snyk/agent-scan) · [agentic-radar](https://github.com/splx-ai/agentic-radar)
- **[AgentShield](https://github.com/affaan-m/agentshield)** 🟢 — Security scanner for AI-agent configurations, MCP servers, hooks, and tool permissions with CLI, GitHub Action, and app workflows. *(★ 1,070 · updated 2026-07-22)*
  - **Related:** [agent-audit](https://github.com/scadastrangelove/agent-audit) · [Snyk Agent Scan](https://github.com/snyk/agent-scan)
- **[repo-forensics](https://github.com/alexgreensh/repo-forensics)** 🟢⚠️ — Offline scanner for AI-agent repos, skills, plugins, and MCP servers; license is PolyForm Noncommercial. *(★ 155 · updated 2026-08-08)*
  - **Related:** [agent-audit](https://github.com/scadastrangelove/agent-audit) · [aguara](https://github.com/garagon/aguara)
- **[skill-scanner](https://github.com/cisco-ai-defense/skill-scanner)** 🟠 — Scanner for agent skills combining YAML + YARA patterns, LLM-as-a-judge, and behavioral dataflow analysis (Codex / Cursor skill formats). *(Cisco AI Defense)* *(★ 2,440 · updated 2026-08-04)*
  - **Related:** [defenseclaw](https://github.com/cisco-ai-defense/defenseclaw) · [aguara](https://github.com/garagon/aguara) · [Cisco AI Defense – mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)
- **[mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)** 🟢⚠️ — Scanner for MCP servers and agentic tool surfaces, covering tools, prompts, resources, package risk, malware indicators, and deployment readiness. *(Cisco AI Defense)* *(★ 1,037 · updated 2026-08-07)*
  - **Related:** [Cisco AI Defense – skill-scanner](https://github.com/cisco-ai-defense/skill-scanner) · [Snyk Agent Scan](https://github.com/snyk/agent-scan) · [aguara](https://github.com/garagon/aguara)
- **[mcp-guardian](https://github.com/alexandriashai/mcp-guardian)** 🟢 — JS/TS library and CLI for detecting prompt injection in MCP tool descriptions and pinning tool definitions. *(★ 6 · updated 2026-07-29)*
  - **Related:** [Cisco AI Defense – mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner) · [Snyk Agent Scan](https://github.com/snyk/agent-scan)
- **[MCP Observatory](https://github.com/KryptosAI/mcp-observatory)** 🟢🟠 — CI-native MCP-server testing tool for schema drift, safe attack simulation, record/replay verification, health scoring, and SARIF evidence before agents depend on a server. *(KryptosAI)* — **note:** the local evidence engine is open source; hosted telemetry intelligence, fleet workflows, and commercial ranking remain outside the package. *(★ 176 · updated 2026-08-15)*
  - **Related:** [Cisco AI Defense – mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner) · [skilltotal](https://github.com/pezhik/skilltotal)
- **[agentic-radar](https://github.com/splx-ai/agentic-radar)** 🟠 — CLI security scanner for agentic workflows (LangGraph, CrewAI, n8n, etc.) — maps tools/data flows and flags risks. *(SplxAI)* *(★ 1,036 · updated 2025-11-27)*
- **[skilltotal](https://github.com/pezhik/skilltotal)** 🟢 — Offline deterministic static scanner (regex + AST, no LLM, no account) for AI components — agent skills/plugins, MCP servers, npm & PyPI packages, and git repos; flags supply-chain risk, dangerous capabilities, prompt-injection surfaces, MCP tool poisoning/shadowing, and data-exfiltration paths, maps to the OWASP Agentic Skills Top 10, and emits JSON + SARIF 2.1.0. *(skilltotal.ai)* *(★ 1 · updated 2026-08-17)*
  - **Related:** [aguara](https://github.com/garagon/aguara) · [Snyk Agent Scan](https://github.com/snyk/agent-scan) · [Cisco AI Defense – skill-scanner](https://github.com/cisco-ai-defense/skill-scanner) · [Cisco AI Defense – mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)
- **[Sunglasses](https://github.com/sunglasses-dev/sunglasses)** 🟢 — Local input/content scanner for AI agents that checks prompts, files, media metadata, skills, and tool descriptions against pattern and mechanism-based prompt-injection, exfiltration, command-injection, and agent-threat rules. — **note:** early-stage project; published precision/recall benchmark is self-reported by the project. *(★ 4 · updated 2026-08-14)*
  - **Related:** [skilltotal](https://github.com/pezhik/skilltotal) · [Armorer Guard](https://github.com/ArmorerLabs/Armorer-Guard)
- **[trentclaw](https://github.com/trnt-ai/trent-openclaw-security-assessment)** 🟠 — Client-side security auditor for OpenClaw deployments: applies pattern-based secret redaction locally, then uploads config/skill metadata and confirm-gated skill archives to Trent AI's API, which identifies misconfigurations, risky skills (prompt injection, permission escalation, data exfiltration), and chained attack paths. *(Trent AI)* — **note:** core detection runs server-side via the Trent AI API (requires an API key); the Apache-2.0 client collects OpenClaw config/skill metadata, applies pattern-based secret redaction locally, and uploads skill archives only after an explicit in-terminal confirmation. *(★ 23 · updated 2026-07-27)*
- **[A2A Security Scanner](https://github.com/cisco-ai-defense/a2a-scanner)** 🟢 — CLI and PyPI scanner for Agent-to-Agent (A2A) agent cards, source code, registries, and live endpoints using specification validation, YARA rules, heuristics, endpoint testing, and an optional LLM analyzer. *(Cisco AI Defense)* *(★ 163 · updated 2026-04-16)*
  - **Related:** [Cisco AI Defense – mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner) · [Agent Threat Rules](https://github.com/Agent-Threat-Rule/agent-threat-rules)

### Frameworks, Rule Standards & Benchmarks

- **[asamm](https://github.com/scadastrangelove/asamm)** 🔬 — *Agentic SAMM* — an OWASP SAMM extension for AI-driven development: an entry-point-based threat taxonomy plus 17 controls across 5 SAMM functions (Governance, Design, Implementation, Verification, Operations) with L1/L2/L3 maturity. License: CC BY-SA 4.0. *(CyberOK / S. Gordeychik)* *(★ 17 · updated 2026-07-26)*
  - **Sources:** [OWASP SAMM](https://owaspsamm.org/) · [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) · [NCSC Secure AI Guidelines](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development) · [MCP Security Best Practices](https://modelcontextprotocol.io/)
  - **Related:** [agent-audit](https://github.com/scadastrangelove/agent-audit)
- **[agent-threat-rules (ATR)](https://github.com/Agent-Threat-Rule/agent-threat-rules)** 🟢 — Open, versioned, machine-readable detection rules for AI-agent threats (prompt injection, tool poisoning, MCP attacks, and skill compromise) — "Sigma for agents"; 768 rules across 10 categories with integrations for Microsoft AGT, Cisco AI Defense, MISP, OWASP, FINOS, and SigmaHQ. *(★ 371 · updated 2026-08-17)*
  - **Related:** [agent-audit](https://github.com/scadastrangelove/agent-audit) · [aguara](https://github.com/garagon/aguara)
- **[Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit)** 🟢 — Multi-language toolkit for policy-enforced agent tool calls and audit records, with optional identity, MCP-gateway, sandboxing, reliability, and compliance components. *(Microsoft)* — **note:** official public preview; APIs and deployment patterns may change before general availability. *(★ 5,962 · updated 2026-08-12)*
  - **Related:** [ATR – Agent Threat Rules](https://github.com/Agent-Threat-Rule/agent-threat-rules) · [ToolHive](https://github.com/stacklok/toolhive)
- **[MCP-Security-Checklist](https://github.com/slowmist/MCP-Security-Checklist)** 🟢 — Security checklist for MCP clients, servers, multi-MCP deployments, lifecycle controls, authz/authn, isolation, and crypto-specific MCP integrations. *(SlowMist)* *(★ 835 · updated 2025-04-28)*
  - **Related:** [Cisco AI Defense – mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner) · [ATR – Agent Threat Rules](https://github.com/Agent-Threat-Rule/agent-threat-rules)
- **[Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)** 🟢 — Large community cybersecurity skill library for AI agents, mapped to MITRE ATT&CK, NIST CSF, MITRE ATLAS, D3FEND, and NIST AI RMF. — **note:** independent community project, not affiliated with Anthropic. *(★ 28,060 · updated 2026-08-08)*
  - **Related:** [sast-skills](https://github.com/utkusen/sast-skills) · [Cisco AI Defense – skill-scanner](https://github.com/cisco-ai-defense/skill-scanner)
- **[Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter)** 🟢 — Claude Code / agent-skill bundle for authorized bug hunting and external red-team workflows across web, API, identity, cloud, recon, reporting, Burp MCP, slash commands, and the cbh CLI. — **note:** skill bundle and workflow knowledge base, not a standalone scanner. *(★ 3,630 · updated 2026-08-17)*
  - **Related:** [sast-skills](https://github.com/utkusen/sast-skills) · [Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)
- **[AgentDojo](https://github.com/ethz-spylab/agentdojo)** 🟢🔬 — Benchmark environment for prompt-injection attacks and defenses in tool-using LLM agents. *(★ 753 · updated 2026-06-02)*
  - **Related:** [agent-audit](https://github.com/scadastrangelove/agent-audit) · [ATR – Agent Threat Rules](https://github.com/Agent-Threat-Rule/agent-threat-rules)
- **[Agent3Sigma-Canary](https://github.com/antgroup/Agent3Sigma-Canary)** 🟢🔬 — Sandboxed research framework for evaluating AI-agent security over complete execution trajectories, covering direct/indirect injection, skill and memory poisoning, and practical risk outcomes. *(Ant Group)* — **note:** research framework that requires Docker plus target and auxiliary LLM configuration; use only in controlled environments. *(★ 35 · updated 2026-08-09)*
  - **Related:** [AgentDojo](https://github.com/ethz-spylab/agentdojo) · [HarmBench](https://github.com/centerforaisafety/HarmBench)
- **[Agent Security Bench (ASB)](https://github.com/agiresearch/ASB)** 🟢🔬 — Official ICLR 2025 benchmark for evaluating attacks and defenses in LLM-based agents across ten scenarios, including direct and indirect prompt injection, memory poisoning, and defensive strategies. — **note:** research benchmark rather than a production control; reproducing evaluations requires configured target and evaluator models. *(★ 285 · updated 2026-04-16)*
  - **Related:** [AgentDojo](https://github.com/ethz-spylab/agentdojo) · [Agent3Sigma-Canary](https://github.com/antgroup/Agent3Sigma-Canary)
- **[Skill-Inject](https://github.com/aisa-group/skill-inject)** 🟢🔬 — Benchmark for measuring prompt-injection vulnerabilities carried by agent skill files across Claude Code, Codex CLI, and Gemini CLI under multiple safety-policy conditions. — **note:** benchmark artifact that executes controlled malicious skill scenarios; run only in an isolated test environment with synthetic data and accounts. *(★ 91 · updated 2026-07-01)*
  - **Related:** [SkillSpector](https://github.com/NVIDIA/SkillSpector) · [AgentDojo](https://github.com/ethz-spylab/agentdojo)
- **[AI Security Verification Standard (AISVS)](https://github.com/OWASP/AISVS)** 🔬⚠️ — Stable verification standard defining testable security requirements for AI applications across model lifecycle, supply chain, data handling, agentic systems, and MCP integrations. *(OWASP)* — **note:** security standard and checklist, not an executable scanner; share-alike terms apply to adapted material. *(★ 429 · updated 2026-07-30)*
  - **Related:** [asamm](https://github.com/scadastrangelove/asamm) · [Agent Threat Rules](https://github.com/Agent-Threat-Rule/agent-threat-rules)

### Runtime Protection & Enforcement

- **[nono](https://github.com/nolabs-ai/nono)** 🟢 — Least-privilege sandbox for AI coding agents that isolates the agent and delegated tools with composable filesystem, network, credential-proxy, and command policies. *(NoLabs)* — **note:** APIs are still stabilizing ahead of the 1.0 release; review every pulled profile before use. *(★ 3,687 · updated 2026-08-17)*
  - **Related:** [microsandbox](https://github.com/superradcompany/microsandbox) · [ToolHive](https://github.com/stacklok/toolhive)
- **[Arcjet Guard](https://github.com/arcjet/arcjet-js)** 🟢🟠 — JavaScript runtime guard for AI-agent tool calls and MCP handlers, with prompt-injection detection, sensitive-data detection/redaction, and custom local policy rules. *(Arcjet)* — **note:** open SDK packages integrate with Arcjet's hosted platform; assess the service, account, and data-processing requirements for the protections you enable. *(★ 681 · updated 2026-08-15)*
  - **Related:** [LLM Guard](https://github.com/protectai/llm-guard) · [AgentLock](https://github.com/webpro255/agentlock)
- **[ToolHive](https://github.com/stacklok/toolhive)** 🟢 — Platform for running MCP servers in isolated containers with per-request identity/access policy, registry and gateway workflows, audit logs, Kubernetes operator support, and observability hooks. *(Stacklok)* *(★ 2,019 · updated 2026-08-14)*
  - **Related:** [microsandbox](https://github.com/superradcompany/microsandbox) · [defenseclaw](https://github.com/cisco-ai-defense/defenseclaw)
- **[Pipelock](https://github.com/luckyPipewrench/pipelock)** 🟢 — AI-agent firewall and verifiable egress-control layer mediating HTTP, WebSocket, CONNECT, MCP, and A2A traffic to detect prompt injection, secret exfiltration, SSRF, and suspicious outbound actions. — **note:** open-source core is Apache-2.0; commercial reporting/features are also advertised. *(★ 796 · updated 2026-08-17)*
  - **Related:** [ToolHive](https://github.com/stacklok/toolhive) · [mcp-context-protector](https://github.com/trailofbits/mcp-context-protector)
- **[SourceryKit](https://github.com/ProvablyAI/sourcerykit)** 🟠⚠️ — Python SDK for agent guardrails that intercepts outbound HTTP calls, enforces trusted-endpoint policies, logs requests, and checks agent handoff claims against a Provably backend before propagation. *(ProvablyAI)* — **note:** BSL-1.1 licensed; requires Provably backend/API credentials and database setup. *(★ 18 · updated 2026-08-12)*
  - **Related:** [Pipelock](https://github.com/luckyPipewrench/pipelock) · [mcp-context-protector](https://github.com/trailofbits/mcp-context-protector)
- **[emisar](https://github.com/AndrewDryga/emisar)** 🟠⚠️ — Agent-infrastructure control plane that exposes declared, typed actions through MCP, applies policy and approval gates before dispatch, revalidates calls on an outbound-only host runner, and records separate control-plane and host audit trails. — **note:** runner, MCP bridge, and packs are Apache-2.0; the hosted portal/control plane is BSL-1.1 and converts to Apache-2.0 on 2029-07-26. Connecting a runner requires an emisar account and outbound HTTPS to the control plane. *(★ 416 · updated 2026-08-17)*
- **[mcp-context-protector](https://github.com/trailofbits/mcp-context-protector)** 🟢 — MCP security wrapper that sits in front of downstream MCP servers, scans tool responses with guardrail providers, and supports quarantine/review workflows for desktop and coding-agent MCP configs. *(Trail of Bits)* *(★ 222 · updated 2026-02-13)*
  - **Related:** [Cisco AI Defense – mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner) · [ToolHive](https://github.com/stacklok/toolhive) · [Pipelock](https://github.com/luckyPipewrench/pipelock)
- **[MCP Defender](https://github.com/MCP-Defender/MCP-Defender)** 🟢⚠️ — Desktop app that proxies MCP tool-call requests and responses for Cursor, Claude, VS Code, and Windsurf, checks intercepted traffic against signatures, and prompts users to allow or block suspicious calls. — **note:** AGPL-3.0 licensed; project has been acquired by Docker. *(★ 255 · updated 2026-06-05)*
  - **Related:** [ToolHive](https://github.com/stacklok/toolhive) · [mcp-context-protector](https://github.com/trailofbits/mcp-context-protector)
- **[MCP Gateway](https://github.com/lasso-security/mcp-gateway)** 🟢 — Plugin-based MCP gateway that proxies configured MCP servers, sanitizes sensitive request/response data, supports guardrail plugins such as basic masking and Presidio, and runs a server reputation/risk check before loading MCP servers. *(Lasso Security)* *(★ 385 · updated 2026-01-22)*
  - **Related:** [ToolHive](https://github.com/stacklok/toolhive) · [Pipelock](https://github.com/luckyPipewrench/pipelock) · [mcp-context-protector](https://github.com/trailofbits/mcp-context-protector)
- **[Parallax](https://github.com/agent-defense/parallax)** 🟢 — Rust runtime policy engine for AI agents: evaluates lifecycle events with regex, keyword, Sigma, CEL, and SQL rules to block or redact prompt injection, data exfiltration, dangerous tool calls, and secret leakage. — **note:** early-stage project with limited adoption signal. *(★ 35 · updated 2026-06-05)*
  - **Related:** [Pipelock](https://github.com/luckyPipewrench/pipelock) · [Armorer Guard](https://github.com/ArmorerLabs/Armorer-Guard)
- **[Armorer Guard](https://github.com/ArmorerLabs/Armorer-Guard)** 🟢 — Local Rust scanner and MCP proxy for AI-agent prompt injection, credential leakage, exfiltration, and risky tool-call arguments, with structured reasons and no scanner network calls. — **note:** young project with limited independent adoption signal. *(★ 42 · updated 2026-08-09)*
  - **Related:** [agentguard](https://github.com/GoPlusSecurity/agentguard) · [ATR – Agent Threat Rules](https://github.com/Agent-Threat-Rule/agent-threat-rules)
- **[onecli](https://github.com/onecli/onecli)** 🟢 — Credential gateway and encrypted vault for AI agents; injects real API credentials at the gateway so agents only see placeholder keys. *(★ 3,104 · updated 2026-07-31)*
  - **Related:** [agentguard](https://github.com/GoPlusSecurity/agentguard) · [defenseclaw](https://github.com/cisco-ai-defense/defenseclaw)
- **[microsandbox](https://github.com/superradcompany/microsandbox)** 🟢 — Local-first, microVM-backed programmable sandboxes for AI agents with SDKs, CLI, MCP support, and rootless hardware isolation. *(★ 7,569 · updated 2026-08-17)*
  - **Related:** [agentguard](https://github.com/GoPlusSecurity/agentguard) · [defenseclaw](https://github.com/cisco-ai-defense/defenseclaw)
- **[agentguard](https://github.com/GoPlusSecurity/agentguard)** 🟢 — Real-time security layer for coding agents: hooks scan every new skill, block dangerous actions before execution, run daily posture patrols, and track which skill triggered each action (incl. Web3-specific checks). *(★ 456 · updated 2026-06-25)*
  - **Related:** [agent-audit](https://github.com/scadastrangelove/agent-audit) · [defenseclaw](https://github.com/cisco-ai-defense/defenseclaw)
- **[defenseclaw](https://github.com/cisco-ai-defense/defenseclaw)** 🟠 — Enforcement and evidence layer for agentic deployments: static CodeGuard checks, sandboxing, registry ingestion with SSRF guards, and audit/observability. *(Cisco AI Defense)* *(★ 819 · updated 2026-08-17)*
  - **Related:** [Cisco AI Defense – skill-scanner](https://github.com/cisco-ai-defense/skill-scanner) · [agentguard](https://github.com/GoPlusSecurity/agentguard)
- **[clawsec](https://github.com/prompt-security/clawsec)** 🟢⚠️ — Security skill suite for OpenClaw-family agents; AGPL-3.0 licensed. *(Prompt Security)* *(★ 1,083 · updated 2026-08-05)*
  - **Related:** [agentguard](https://github.com/GoPlusSecurity/agentguard) · [Cisco AI Defense – skill-scanner](https://github.com/cisco-ai-defense/skill-scanner)
- **[AgentLock](https://github.com/webpro255/agentlock)** 🟢🔬⚠️ — Pre-action authorization gate for LLM agent tool calls that decides from session provenance rather than content, with deny-by-default tool permissions, parameter lineage, Ed25519 signed receipts, and a hash-chained audit log; AGPL-3.0 licensed with commercial options. — **note:** evaluated on AgentDojo with predictions pre-registered before the runs; the published results include a suite where the defense costs more utility than the attack it prevents. *(★ 19 · updated 2026-08-12)*
- **[h5i](https://github.com/h5i-dev/h5i)** 🟢 — Local Rust CLI for auditable coding-agent workspaces: per-agent worktrees with sandbox policies, provenance capture, peer review, neutral verification, secret/prompt-injection audit signals, and refs/h5i/* run metadata. — **note:** security-adjacent agent-workspace governance tool, not a vulnerability scanner or VM-equivalent sandbox. *(★ 531 · updated 2026-08-16)*
  - **Related:** [microsandbox](https://github.com/superradcompany/microsandbox) · [defenseclaw](https://github.com/cisco-ai-defense/defenseclaw)
- **[DvalinCode](https://github.com/arthurpanhku/dvalincode)** 🟢 — Local-first AI coding agent with runtime governance controls: org/repo policy gates for tools, models, MCP servers, paths, and commands, plus provider/shell/MCP egress controls and hash-chained audit logs. — **note:** young project with limited independent adoption signal. *(★ 112 · updated 2026-08-17)*
  - **Related:** [h5i](https://github.com/h5i-dev/h5i) · [Pipelock](https://github.com/luckyPipewrench/pipelock) · [Armorer Guard](https://github.com/ArmorerLabs/Armorer-Guard)
- **[TAP](https://github.com/holonym-foundation/tap-oss)** 🟢🟠 — Credential-isolation proxy and MCP server for AI agents: agents send placeholder credentials, TAP injects real secrets server-side after per-action policy checks, with optional human approval on sensitive calls. *(human.tech)* — **note:** Apache-2.0 runtime is self-hostable, but the hosted dashboard and managed-service deployment glue are proprietary; self-hosting puts credential/key isolation and policy-engine hardening on the operator. *(★ 12 · updated 2026-07-23)*
- **[Agent Memory Guard](https://github.com/OWASP/www-project-agent-memory-guard)** 🟢 — Runtime middleware for AI-agent memory reads and writes, screening prompt injection, memory poisoning, secret/PII leakage, protected-key tampering, and size anomalies before persisted memory is reused. *(OWASP)* — **note:** OWASP Incubator project; published benchmark numbers are project-reported and should be independently reproduced before production enforcement. *(★ 125 · updated 2026-08-16)*
- **[AIO Sandbox](https://github.com/agent-infra/sandbox)** 🟢⚠️ — All-in-one Docker workspace for AI agents with browser, shell, file, code-execution, MCP, and VSCode interfaces, plus API-key/JWT controls and private-deployment guidance. — **note:** the public repository ships SDKs, integrations, and docs rather than the core runtime service; official Chromium-enabled deployments use `seccomp=unconfined`. Treat it as a trusted execution environment, not a hardened isolation boundary; use separate VMs or a hardened runtime plus network policy for hostile workloads. *(★ 5,727 · updated 2026-08-17)*
  - **Related:** [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) · [microsandbox](https://github.com/superradcompany/microsandbox)
- **[Agentgateway](https://github.com/agentgateway/agentgateway)** 🟢 — Agent-native proxy and gateway for MCP and A2A traffic with OAuth/JWT/API-key authentication, CEL-based RBAC policies, TLS, rate limiting, and OpenTelemetry observability. *(★ 4,385 · updated 2026-08-14)*
  - **Related:** [MCP Gateway](https://github.com/lasso-security/mcp-gateway) · [Pipelock](https://github.com/luckyPipewrench/pipelock)
- **[Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox)** 🟢 — Kubernetes CRDs and controllers for isolated, stateful singleton agent workloads, delegating low-level isolation to configured runtimes such as gVisor or Kata Containers. *(Kubernetes SIG Apps)* — **note:** sandbox orchestrator, not an isolation runtime itself; security depends on the selected RuntimeClass, network policy, and workload configuration. *(★ 3,544 · updated 2026-08-16)*
  - **Sources:** [Kubernetes announcement](https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox/)
  - **Related:** [AIO Sandbox](https://github.com/agent-infra/sandbox)
- **[Prismor](https://github.com/PrismorSec/prismor)** 🟢 — Self-hosted runtime control plane for coding agents with pre-tool-call hooks, policy-driven observe/approve/block decisions, an MCP gateway, secret and egress controls, and tamper-evident audit evidence. *(★ 291 · updated 2026-08-16)*
  - **Related:** [Armorer Guard](https://github.com/ArmorerLabs/Armorer-Guard) · [AgentLock](https://github.com/webpro255/agentlock)
- **[tirith](https://github.com/sheeki03/tirith)** 🟢⚠️ — Terminal guard for developers and AI coding agents that intercepts homograph and terminal-injection tricks, obfuscated execution chains, pipe-to-shell patterns, credential exfiltration, and malicious skill/config files. — **note:** AGPL-3.0 with a separate commercial license; shell interception is a host-side guard, not a substitute for sandboxing or least-privilege tool access. *(★ 2,664 · updated 2026-08-13)*
  - **Related:** [nono](https://github.com/nolabs-ai/nono) · [gate.cat](https://github.com/BGMLAI/gate.cat)
- **[ADR](https://github.com/uber/ADR)** 🟢🔬 — Agentic AI Detection and Response system combining cross-client agent telemetry, ADR-Bench security scenarios, and a dual-agent detector for suspicious intent, tool use, and execution traces. *(Uber)* — **note:** deployed at Uber and published with an MLSys 2026 paper; the open release includes the Sensor, benchmark, and Detector, but not ADR Prevention or the offline ADR Explorer. Default detector configurations require model-provider credentials. *(★ 1,442 · updated 2026-08-16)*
  - **Related:** [Pipelock](https://github.com/luckyPipewrench/pipelock) · [AgentLock](https://github.com/webpro255/agentlock)
- **[xaidr](https://github.com/delphisecurity/xaidr)** 🟢 — In-process runtime security sensor for AI agents that inspects input, tool calls, output, and agent-to-agent envelopes inside the agent process, with structured shell-command classification, YAML policy, privilege tiers, an opt-in circuit breaker, and OpenTelemetry export. *(Delphi Security)* — **note:** early-stage in-process sensor, not an isolation boundary; monitor mode is the default and unexpected scan failures fail open while emitting degraded telemetry. Published detection and false-positive figures are project-reported on its committed corpus. *(★ 22 · updated 2026-08-17)*
  - **Related:** [agentguard](https://github.com/GoPlusSecurity/agentguard) · [defenseclaw](https://github.com/cisco-ai-defense/defenseclaw)
- **[Agentmetry](https://github.com/blitzcrieg1/agentmetry)** 🟢 — Local-first flight recorder for AI coding agents and MCP servers that writes a hash-chained JSONL trail with RFC 6962 Merkle roots, applies MITRE-mapped sequence detection across a session, attests every 300s which agent surfaces are covered, uncovered, absent or unknown, and forwards to Splunk HEC, Elastic ECS, Google SecOps UDM or CloudEvents. — **note:** young project with limited independent adoption signal; it records and detects rather than blocks, and its README states that hooks are cooperative and that tamper-evident is not the same as attributable.
  - **Related:** [HOL Guard](https://github.com/hashgraph-online/hol-guard) · [ADR](https://github.com/uber/ADR)

---

## AI/ML Supply Chain & Model Security

Tools for securing model artifacts, serialized ML files, AI/ML supply-chain surfaces, and malicious-package detection datasets/benchmarks.

- **[Fraim](https://github.com/fraim-dev/fraim)** 🟢 — Framework for AI-powered security workflows including LLM SAST and IaC analysis with SARIF/HTML output. *(★ 160 · updated 2025-12-01)*
  - **Related:** [sast-skills](https://github.com/utkusen/sast-skills)
- **[Adversarial Robustness Toolbox (ART)](https://github.com/Trusted-AI/adversarial-robustness-toolbox)** 🟢 — Flagship machine-learning security library for evaluating and defending models against evasion, poisoning, extraction, and inference attacks across major ML frameworks. *(LF AI & Data / IBM)* *(★ 6,179 · updated 2025-11-13)*
  - **Related:** [Foolbox](https://github.com/bethgelab/foolbox) · [PrivacyRaven](https://github.com/trailofbits/PrivacyRaven)
- **[Foolbox](https://github.com/bethgelab/foolbox)** 🟢 — Classic Python toolbox for generating adversarial examples and benchmarking robustness of PyTorch, TensorFlow, and JAX models. *(★ 2,972 · updated 2024-03-04)*
  - **Related:** [Adversarial Robustness Toolbox](https://github.com/Trusted-AI/adversarial-robustness-toolbox)
- **[modelscan](https://github.com/protectai/modelscan)** 🟢 — Scans ML model files for unsafe serialization patterns and embedded code, with a focus on model serialization attacks. *(Protect AI)* *(★ 762 · updated 2026-02-18)*
  - **Related:** [Fickling](https://github.com/trailofbits/fickling) · [picklescan](https://github.com/mmaitre314/picklescan) · [ai-exploits](https://github.com/protectai/ai-exploits)
- **[Fickling](https://github.com/trailofbits/fickling)** 🟢 — Python pickle decompiler, rewriter, and static analyzer for inspecting and detecting malicious pickle/PyTorch payloads. *(Trail of Bits)* *(★ 662 · updated 2026-08-13)*
  - **Related:** [modelscan](https://github.com/protectai/modelscan) · [picklescan](https://github.com/mmaitre314/picklescan)
- **[picklescan](https://github.com/mmaitre314/picklescan)** 🟢 — Lightweight CLI/library for detecting suspicious Python pickle operations in ML and model artifacts. *(★ 418 · updated 2026-07-01)*
  - **Related:** [modelscan](https://github.com/protectai/modelscan) · [Fickling](https://github.com/trailofbits/fickling)
- **[AIsbom](https://github.com/Lab700xOrg/aisbom)** 🟢 — AI software bill of materials tooling for AI/ML supply-chain inventory and provenance metadata. *(★ 76 · updated 2026-08-17)*
  - **Related:** [modelscan](https://github.com/protectai/modelscan) · [model-provenance-kit](https://github.com/cisco-ai-defense/model-provenance-kit)
- **[model-provenance-kit](https://github.com/cisco-ai-defense/model-provenance-kit)** 🟢 — Toolkit for model-family provenance and fingerprinting across model weights, tokenizers, and architecture signals. *(Cisco AI Defense)* *(★ 101 · updated 2026-08-12)*
  - **Related:** [AIsbom](https://github.com/Lab700xOrg/aisbom)
- **[pickle-fuzzer](https://github.com/cisco-ai-defense/pickle-fuzzer)** 🟢 — Structure-aware fuzzer for pickle scanners, useful for hardening tools such as modelscan, Fickling, and picklescan. *(Cisco AI Defense)* *(★ 17 · updated 2026-08-03)*
  - **Related:** [modelscan](https://github.com/protectai/modelscan) · [Fickling](https://github.com/trailofbits/fickling) · [picklescan](https://github.com/mmaitre314/picklescan)
- **[Medusa](https://github.com/Pantheon-Security/medusa)** 🟢⚠️ — AI-first security scanner for AI/ML repos, agents, and MCP surfaces; AGPL-3.0 licensed. *(Pantheon Security)* *(★ 964 · updated 2026-06-24)*
  - **Related:** [agent-audit](https://github.com/scadastrangelove/agent-audit) · [modelscan](https://github.com/protectai/modelscan)
- **[PrivacyRaven](https://github.com/trailofbits/PrivacyRaven)** 🟢🔬 — Privacy-testing library for deep-learning systems, covering model extraction and membership-inference style attacks. *(Trail of Bits)* — **note:** archived/hiatus project, but still a useful reference implementation. *(★ 214 · updated 2025-09-05)*
  - **Related:** [Adversarial Robustness Toolbox](https://github.com/Trusted-AI/adversarial-robustness-toolbox)
- **[gym-malware](https://github.com/endgameinc/gym-malware)** 🟢🔬 — OpenAI Gym environment for reinforcement-learning agents that mutate PE malware to evade static ML malware detectors. *(★ 636 · updated 2018-06-15)*
- **[deep-pwning](https://github.com/cchio/deep-pwning)** 🟢🔬 — Historical "Metasploit for machine learning" framework for experimenting with adversarial robustness of ML models. *(★ 571 · updated 2022-05-17)*
- **[open-malicious-code-benchmark](https://github.com/False-Positive-Community/open-malicious-code-benchmark)** 🟢🔬 — OMCBench benchmark suite for malicious-code/package detection: labeled Python and JavaScript package archives, common runners, and published precision/recall/F1 metrics. *(False Positive Community)* — **note:** evaluates an unreleased commercial ML detector (MOLOT / PT Application Inspector) alongside open-source baselines. *(★ 17 · updated 2026-06-09)*
  - **Related:** [GuardDog](https://github.com/DataDog/guarddog) · [OSSGadget](https://github.com/microsoft/OSSGadget) · [malicious-code-ruleset](https://github.com/apiiro/malicious-code-ruleset) · [bandit4mal](https://github.com/lyvd/bandit4mal)
- **[malicious-software-packages-dataset](https://github.com/DataDog/malicious-software-packages-dataset)** 🟢🔬 — Human-vetted dataset of malicious software packages across npm, PyPI, IDE extensions, and AI Skills, useful for detector training and evaluation. *(Datadog Security Labs)* — **note:** contains real malware samples; Datadog notes selection bias because many samples were identified by GuardDog. *(★ 372 · updated 2026-08-17)*
  - **Related:** [GuardDog](https://github.com/DataDog/guarddog) · [pypi_malregistry](https://github.com/lxyeternal/pypi_malregistry)
- **[GuardDog](https://github.com/DataDog/guarddog)** 🟢 — CLI for detecting malicious PyPI, npm, Go, RubyGems, GitHub Actions, and VSCode extension packages using Semgrep rules and package-metadata heuristics. *(Datadog)* *(★ 1,184 · updated 2026-08-14)*
  - **Related:** [malicious-software-packages-dataset](https://github.com/DataDog/malicious-software-packages-dataset) · [Packj](https://github.com/ossillate-inc/packj)
- **[package-analysis](https://github.com/ossf/package-analysis)** 🟢🔬 — Sandboxed static/dynamic analysis pipeline for open-source packages, capturing filesystem, process, and network behavior and publishing data for malicious-package research. *(OpenSSF)* *(★ 903 · updated 2026-07-21)*
  - **Related:** [malicious-packages](https://github.com/ossf/malicious-packages) · [package-feeds](https://github.com/ossf/package-feeds)
- **[malicious-code-ruleset](https://github.com/apiiro/malicious-code-ruleset)** 🟢 — Focused Semgrep ruleset for malicious-code patterns such as dynamic execution and obfuscation, used as an OMCBench baseline. *(Apiiro)* *(★ 149 · updated 2025-02-24)*
  - **Related:** [open-malicious-code-benchmark](https://github.com/False-Positive-Community/open-malicious-code-benchmark)
- **[pypi_malregistry](https://github.com/lxyeternal/pypi_malregistry)** 🔬⚠️ — ASE'23 / USENIX Security'26 malicious-PyPI dataset with more than 10k malicious package versions. — **note:** no LICENSE file found and the repository contains malware samples; handle in an isolated environment. *(★ 129 · updated 2026-07-21)*
  - **Related:** [malicious-software-packages-dataset](https://github.com/DataDog/malicious-software-packages-dataset)

---

## Pentest & Red-Team Agents

Autonomous and semi-autonomous AI agents for penetration testing, exploitation, and attack simulation.

- **[PentestGPT](https://github.com/GreyDGL/PentestGPT)** 🟢🔬 — The original USENIX'24 LLM pentest agent; re-released as an autonomous pipeline with strong benchmark results. *(★ 14,906 · updated 2026-07-14)*
- **[PentAGI](https://github.com/vxcontrol/pentagi)** 🟢 — Fully autonomous multi-agent pentest framework with Docker sandboxing. *(VXControl)* *(★ 21,860 · updated 2026-08-06)*
- **[CAI – Cybersecurity AI](https://github.com/aliasrobotics/cai)** 🟢🟠 — Modular, bug-bounty-ready agent framework supporting 300+ LLM models. MIT for research; separate commercial license for production/on-prem. *(Alias Robotics)* *(★ 9,745 · updated 2026-07-14)*
- **[Strix](https://github.com/usestrix/strix)** 🟢 — Autonomous "AI hackers" that dynamically run code and validate vulnerabilities with PoCs (Apache-2.0). *(★ 53,569 · updated 2026-08-17)*
- **[hackingBuddyGPT](https://github.com/ipa-lab/hackingBuddyGPT)** 🟢🔬 — Minimal (~50 LOC) research framework for LLM-driven Linux priv-esc and web pentesting (FSE'23). *(★ 1,209 · updated 2026-08-10)*
- **[Nebula](https://github.com/berylliumsec/nebula)** 🟢🟠 — AI pentesting CLI assistant with local-LLM support (Llama-3.1, Mistral, DeepSeek). *(★ 1,087 · updated 2026-07-26)*
- **[HexStrike-AI](https://github.com/0x4m4/hexstrike-ai)** 🟢 — MCP server exposing 150+ security tools (nmap, gobuster, nuclei, …) to AI agents (MIT). *(★ 11,116 · updated 2026-08-03)*
- **[Deep Eye](https://github.com/zakirkun/deep-eye)** 🟢 — AI-assisted penetration-testing scanner that orchestrates multiple LLM providers for payload generation, 45+ vulnerability checks, CVE/RAG-assisted testing, AI triage, scan diffing, browser automation, proxying, and multi-format reports. — **note:** MIT-licensed; authorized use only. Heavy runtime surface: optional browser automation/proxying, plaintext API-key config, plugins with full OS access, and pickle model files called out in SECURITY.md. *(★ 1,972 · updated 2026-08-14)*
  - **Related:** [HexStrike-AI](https://github.com/0x4m4/hexstrike-ai) · [pentest-ai](https://github.com/0xSteph/pentest-ai)
- **[Burp Suite MCP Server](https://github.com/PortSwigger/mcp-server)** 🟢⚠️ — Official Burp Suite extension exposing Burp to AI clients through MCP. *(PortSwigger)* — **note:** GPL-3.0 licensed. *(★ 1,071 · updated 2026-08-12)*
  - **Related:** [HexStrike-AI](https://github.com/0x4m4/hexstrike-ai)
- **[pentest-ai](https://github.com/0xSteph/pentest-ai)** 🟢 — Offensive-security MCP server with 200+ wrapped tools, specialist agents, and OWASP-oriented probes for authorized testing. *(★ 1,598 · updated 2026-08-17)*
  - **Related:** [pentest-ai-agents](https://github.com/0xSteph/pentest-ai-agents)
- **[pentest-ai-agents](https://github.com/0xSteph/pentest-ai-agents)** 🟢 — Collection of Claude Code offensive-security subagents for authorized penetration-testing research. *(★ 2,132 · updated 2026-08-16)*
  - **Related:** [pentest-ai](https://github.com/0xSteph/pentest-ai)
- **[DarkMoon](https://github.com/ASCIT31/Dark-Moon)** 🟢⚠️ — Autonomous AI penetration-testing platform that orchestrates specialized web, AD, Kubernetes, CMS, and framework agents through an MCP-controlled Docker toolbox with local privacy-tokenization for sensitive target data. — **note:** GPL-3.0 licensed; heavy Docker/LLM stack, use only for authorized testing. *(★ 843 · updated 2026-08-06)*
  - **Related:** [PentAGI](https://github.com/vxcontrol/pentagi) · [HexStrike-AI](https://github.com/0x4m4/hexstrike-ai) · [pentest-ai](https://github.com/0xSteph/pentest-ai)
- **[T3MP3ST](https://github.com/elder-plinius/T3MP3ST)** 🟢⚠️ — Autonomous offensive-security meta-harness that wraps local or API-backed coding agents into a multi-agent recon-to-exploit workflow with MCP/API, War Room UI, tool arsenal, and committed benchmark artifacts. — **note:** very new AGPL-3.0 project with bold benchmark claims; use only for authorized testing and verify independently before operational use. *(★ 5,596 · updated 2026-08-12)*
  - **Related:** [PentAGI](https://github.com/vxcontrol/pentagi) · [HexStrike-AI](https://github.com/0x4m4/hexstrike-ai) · [pentest-ai](https://github.com/0xSteph/pentest-ai)
- **[Shannon](https://github.com/KeygraphHQ/shannon)** 🟢🟠⚠️ — White-box autonomous AI pentester with strong XBOW-benchmark results. *Shannon Lite is AGPL-3.0; Shannon Pro is commercial.* *(★ 46,882 · updated 2026-08-12)*
- **[AIDA](https://github.com/Vasco0x4/AIDA)** 🟢⚠️ — Model-agnostic autonomous pentest agent running inside an isolated Docker environment; AGPL-3.0 licensed. *(★ 471 · updated 2026-07-19)*
- **[HackSynth](https://github.com/aielte-research/HackSynth)** 🟢🔬⚠️ — Planner/summarizer LLM-agent framework for autonomous penetration testing and benchmark evaluation; AGPL-3.0 licensed. *(★ 314 · updated 2025-06-24)*
- **[VulnBot](https://github.com/KHenryAegis/VulnBot)** 🟢🔬 — Multi-agent collaborative penetration-testing framework with RAG support. *(★ 185 · updated 2025-04-07)*
- **[PentestAgent](https://github.com/GH05TCREW/pentestagent)** 🟢 — Black-box AI pentest framework with MCP, multi-agent spawning, and persistent sessions. *(★ 2,958 · updated 2026-08-04)*
- **[cyber-security-llm-agents](https://github.com/NVISOsecurity/cyber-security-llm-agents)** 🟢⚠️ — AutoGen-based agents for cybersecurity tasks (shown at RSAC 2024). *(NVISO)* *(★ 388 · updated 2024-05-07)*
- **[Pentest-Swarm-AI](https://github.com/Armur-Ai/Pentest-Swarm-AI)** 🟢 — Swarm-intelligence multi-agent pentest with stigmergic blackboard coordination (Go). *(★ 2,205 · updated 2026-08-04)*
- **[hackGPT](https://github.com/NoDataFound/hackGPT)** 🟢⚠️ — LLM offensive-security toolkit. *(★ 1,199 · updated 2026-08-12)*
- **[ShiftGrid](https://github.com/BuFuuu/shiftgrid)** 🟢 — Prompt engine that turns Claude Code into a transparent, human-in-the-loop pentester, structuring engagements through checklists, observations, and notes exposed via an agent-facing API. — **note:** early-stage local Docker application with no built-in authentication; keep its API and UI ports bound to localhost. *(★ 39 · updated 2026-08-02)*
- **[BugTraceAI](https://github.com/BugTraceAI/BugTraceAI-CLI)** 🟢⚠️ — Self-hosted autonomous web-application security scanner that combines reconnaissance, specialist exploit agents, Go fuzzers, and Playwright validation to produce evidence-backed findings. *(BugTraceAI)* — **note:** AGPL-3.0 licensed and beta; use only for authorized testing. Requires an LLM provider or local Ollama endpoint and a substantial Docker/Playwright/Go runtime. *(★ 174 · updated 2026-07-30)*
  - **Related:** [Project overview](https://github.com/BugTraceAI/BugTraceAI) · [Web dashboard](https://github.com/BugTraceAI/BugTraceAI-WEB) · [Docker launcher](https://github.com/BugTraceAI/BugTraceAI-Launcher)
- **[HunterX](https://github.com/nullc0d30/HunterX)** 🟢 — AI-assisted offensive security engine that orchestrates reconnaissance, security-tool coordination, vulnerability detection and validation, evidence collection, and report-ready findings in one workflow. *(NullC0d3)* — **note:** early-stage and tool-orchestration-heavy; run only in an isolated, authorized assessment environment. *(★ 12 · updated 2026-08-16)*
- **[MCP Security Hub](https://github.com/FuzzingLabs/mcp-security-hub)** 🟢 — Collection of Dockerized MCP servers that expose offensive-security tools such as Nmap, Nuclei, SQLMap, Ghidra, Hashcat, and related assessment utilities to MCP-capable assistants. *(FuzzingLabs)* — **note:** orchestration and wrapper collection rather than a security boundary; its containers invoke offensive tools and must be used only in isolated, explicitly authorized environments. *(★ 761 · updated 2026-04-08)*
  - **Related:** [pentest-ai](https://github.com/0xSteph/pentest-ai) · [Burp Suite MCP Server](https://github.com/PortSwigger/mcp-server)

---

## AI-Powered Recon & Narrow ML Tools

Hyper-specific AI/ML tools for a single offensive-security, recon, or detection step — the subwiz/eyeballer pattern rather than broad autonomous agents. 🅐 = self-contained trained model or learned model/pattern engine; 🅑 = LLM wrapper that calls an external API.

### Subdomain & DNS Prediction

- **[subwiz](https://github.com/hadriansecurity/subwiz)** 🟢 — 🅐 Lightweight nanoGPT model that predicts resolvable subdomains via beam search; model weights are published on Hugging Face. *(Hadrian Security)* *(★ 388 · updated 2025-12-18)*
  - **Related:** [HadrianSecurity/subwiz model](https://huggingface.co/HadrianSecurity/subwiz)
- **[regulator](https://github.com/cramppet/regulator)** 🟢⚠️ — 🅐 Learns and ranks regex-like naming patterns from known subdomains to generate likely new candidates. — **note:** no LICENSE file found; treat as source-available until clarified. *(★ 392 · updated 2023-02-18)*
  - **Related:** [subwiz](https://github.com/hadriansecurity/subwiz)

### Recon Screenshot Triage

- **[eyeballer](https://github.com/BishopFox/eyeballer)** 🟢⚠️ — 🅐 Convolutional neural network that classifies pentest/recon screenshots (login pages, webapps, old-looking sites, parked domains, and custom 404s) for attack-surface triage. *(Bishop Fox)* — **note:** GPL-3.0 licensed. *(★ 1,290 · updated 2024-02-19)*

### Software / Tech Fingerprinting

- **[GyoiThon](https://github.com/gyoisamurai/GyoiThon)** 🟢🔬 — 🅐 Machine-learning-assisted web intelligence tool that fingerprints products, versions, CVEs, login pages, debug messages, and related web-server signals from HTTP responses. — **note:** historical research reference; Apache-2.0 licensed, but maintenance is low. *(★ 826 · updated 2021-06-29)*

### AI-Assisted Fuzzing

- **[ffufai](https://github.com/jthack/ffufai)** 🟢⚠️ — 🅑 AI wrapper around the ffuf web fuzzer that suggests file extensions and paths from the target URL and headers using OpenAI or Anthropic models. *(Joseph Thacker)* — **note:** requires an LLM API key; README states MIT but no LICENSE file was found. *(★ 801 · updated 2025-12-04)*

### Password / Credential ML

- **[PassGPT](https://huggingface.co/javirandor/passgpt-10characters)** 🔬⚠️ — 🅐 GPT-style password model trained on leaked passwords for research on password generation and strength estimation. *(Rando et al.)* *license: CC BY-NC-4.0 · access: open 10-char model; 16-char variant gated · artifacts: PyTorch/Safetensors.* Research-only / non-commercial use; related code: [javirandor/passgpt](https://github.com/javirandor/passgpt).
- **[PassGAN](https://github.com/brannondorsey/PassGAN)** 🔬 — 🅐 WGAN that learns password distributions from leaks to generate guesses; historical reference implementation of the PassGAN paper (MIT). — **note:** historical research reference; not an actively maintained password-auditing product. *(★ 2,009 · updated 2018-09-30)*
- **[neural_network_cracking](https://github.com/cupslab/neural_network_cracking)** 🔬 — 🅐 RNN password-guessing model from *Fast, Lean, and Accurate: Modeling Password Guessability Using Neural Networks* (USENIX Security 2016); Apache-2.0 licensed. *(CMU CUPS Lab)* — **note:** historical USENIX research implementation, not a maintained password-auditing product. *(★ 243 · updated 2018-11-30)*
  - **Related:** [PassGPT](https://huggingface.co/javirandor/passgpt-10characters) · [PassGAN](https://github.com/brannondorsey/PassGAN)

### Phishing Detection (Visual / URL)

- **[phishing-url-detection](https://huggingface.co/pirocheto/phishing-url-detection)** 🟢 — 🅐 Packaged URL phishing classifier with ONNX and pickle artifacts. *license: MIT · access: open · artifacts: ONNX, pickle.* Model card recommends ONNX over pickle for safer inference.
- **[Phishing Email Detection DistilBERT v2.4.1](https://huggingface.co/cybersectony/phishing-email-detection-distilbert_v2.4.1)** 🟢 — DistilBERT text-classification model for email and URL phishing detection, trained on a public Hugging Face phishing-email dataset. *license: Apache-2.0 · access: open · artifacts: Safetensors.* — **note:** strong download signal, but independently verify the very high published metrics before production use.
- **[PhishIntention](https://github.com/lindsey98/PhishIntention)** 🔬 — 🅐 Deep-vision phishing detector that infers both brand intention and credential-taking intention from webpage appearance and dynamics (USENIX Security 2022). — **note:** CC0-1.0 licensed. *(★ 263 · updated 2026-06-04)*
- **[VisualPhishNet](https://github.com/S-Abdelnabi/VisualPhishNet)** 🔬⚠️ — 🅐 Triplet CNN for zero-day phishing detection by visual similarity to trusted websites (ACM CCS 2020). *(CISPA)* — **note:** no LICENSE file found; dataset access is research-request based. *(★ 30 · updated 2022-02-09)*

### AI/ML-Assisted Detection Rules & Engines

- **[SYARA](https://github.com/nabeelxy/syara)** 🟢🔬 — 🅐 Semantic YARA-like rule engine for text and multimodal signals, adding embedding similarity, classifier-backed rules, LLM evaluators, and pHash matching to familiar YARA-style syntax. — **note:** early-stage engine; useful for LLM-era intent signals such as phishing, prompt injection, jailbreaks, hallucination, and disinformation rather than classic binary-only YARA matching. *(★ 18 · updated 2026-03-05)*
- **[AutoYara](https://github.com/FutureComputing4AI/AutoYara)** 🟢🔬 — 🅐 Research implementation of automatic YARA rule generation via biclustering over byte n-grams for malware-family samples. — **note:** Apache-2.0 research code from the ACM AISec 2020 paper; README explicitly says it comes with no warranty or support. *(★ 79 · updated 2025-10-08)*
  - **Related:** [Automatic Yara Rule Generation Using Biclustering](https://arxiv.org/abs/2009.03779)
- **[yaraml_rules](https://github.com/sophos/yaraml_rules)** 🟢🔬 — Research code that trains scikit-learn classifiers on malware and benign corpora, then compiles the learned model into deployable YARA rules. *(Sophos)* — **note:** historical research reference; the maintained value is the ML-to-YARA technique, not a current detection product. *(★ 215 · updated 2020-12-18)*
- **[RuleLLM](https://github.com/zhang-xr/RuleLLM)** 🟢🔬 — 🅑 LLM-assisted malware-rule generator that clusters malicious code samples and produces/refines/validates YARA and Semgrep rules. — **note:** MIT-licensed research prototype; requires OpenAI-compatible API access plus YARA/Semgrep validators. *(★ 12 · updated 2025-04-25)*

### Defensive Trained-Model Detectors

- **[DeepSQLi](https://github.com/gatewayd-io/DeepSQLi)** 🟢⚠️ — 🅐 Deep-learning SQL-injection detector with dataset, trained models, and a Flask Prediction API for GatewayD IDS/IPS integration. *(GatewayD)* — **note:** AGPL-3.0 licensed; defensive detector rather than offensive generator. *(★ 7 · updated 2026-02-21)*
- **[deepsecrets](https://github.com/ntoskernel/deepsecrets)** 🟢 — Semantic secrets scanner using lexing/parsing, entropy checks, and hashed-known-secret matching across 500+ languages. — **note:** useful narrow detector, but not a trained ML model. *(★ 172 · updated 2026-06-04)*
- **[VLAI Vulnerability Severity Classifier](https://huggingface.co/CIRCL/vulnerability-severity-classification-roberta-base)** 🟢🔬 — RoBERTa-based vulnerability-severity classifier trained on CIRCL vulnerability scores to assist triage before manual CVSS scoring. *(CIRCL)* *license: CC-BY-4.0 · access: open · artifacts: Safetensors.*

---

## AI-Powered SAST & Secure Code Review

Static analysis and secure code review enhanced with LLMs.

- **[Vulnhuntr](https://github.com/protectai/vulnhuntr)** 🟢 — Zero-shot vulnerability discovery in Python repos via LLM call-chain analysis; credited with a 0-day RCE in Ragflow. *(Protect AI)* *(★ 2,741 · updated 2025-02-06)*
  - **Related:** [IRIS](https://github.com/iris-sast/iris)
- **[deepsec](https://github.com/vercel-labs/deepsec)** 🟢 — Agent-powered security harness for scanning large codebases with coding agents, resumable parallel runs, custom matchers, and optional revalidation. *(Vercel Labs)* *(★ 7,695 · updated 2026-08-13)*
  - **Related:** [claude-code-security-review](https://github.com/anthropics/claude-code-security-review) · [sast-skills](https://github.com/utkusen/sast-skills)
- **[Codex Security](https://github.com/openai/codex-security)** 🟠 — CLI and TypeScript SDK that use Codex Security to find, validate, and help fix vulnerabilities in a codebase, with scan comparison and containerized bulk-scan support. *(OpenAI)* — **note:** the CLI/SDK are open source, but scans require Codex Security access and, for best results, OpenAI Trusted Access. *(★ 9,911 · updated 2026-08-16)*
  - **Related:** [deepsec](https://github.com/vercel-labs/deepsec) · [defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness)
- **[open·kritt](https://github.com/Kritt-ai/open-kritt)** 🟢⚠️ — Self-hosted platform that orchestrates Codex or Claude Code across focused vulnerability-research workflows, then validates, de-duplicates, ranks, and reports resulting findings. *(Kritt AI)* — **note:** jobs run as root in disposable Docker containers with writable target copies and direct internet access; the stack has no application auth by default and sends scanned code to the configured model provider. Deploy only on a dedicated, access-controlled host and scan authorized targets. *(★ 1,877 · updated 2026-08-16)*
  - **Related:** [deepsec](https://github.com/vercel-labs/deepsec) · [Visa Vulnerability Agentic Harness](https://github.com/visa/visa-vulnerability-agentic-harness)
- **[Visa Vulnerability Agentic Harness](https://github.com/visa/visa-vulnerability-agentic-harness)** 🟢 — Agentic SAST pipeline for autonomous vulnerability discovery, exploitability verification, SARIF/Markdown reporting, remediation, and validation using frontier AI models. *(Visa)* — **note:** Apache-2.0; authorized use only. The default `scan` profile can continue into remediation and edit target source files; use `--stop-after s9` for detection-only runs. *(★ 2,556 · updated 2026-08-04)*
  - **Related:** [deepsec](https://github.com/vercel-labs/deepsec) · [defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness)
- **[defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness)** 🟢 — Reference Claude Code skills and autonomous vulnerability-discovery pipeline for threat modeling, static scanning, triage, execution-verified C/C++ memory-bug discovery, reporting, and patch generation. *(Anthropic)* — **note:** official reference implementation, not maintained as a product; the autonomous pipeline executes target code and should be run only inside the documented gVisor sandbox. *(★ 7,270 · updated 2026-08-06)*
  - **Related:** [deepsec](https://github.com/vercel-labs/deepsec) · [claude-code-security-review](https://github.com/anthropics/claude-code-security-review)
- **[rust-in-peace](https://github.com/scadastrangelove/rust-in-peace)** 🟢 — Rust-security fork of Anthropic's defending-code reference harness, adding a Rust profile for agentic review of unsafe/FFI memory bugs, panic-DoS, deserialization-trust issues, and Miri/ASan/panic/hang-verified findings. *(Sergey Gordeychik)* — **note:** very new Apache-2.0 fork; autonomous runs execute target code and should use the documented sandbox. *(★ 14 · updated 2026-08-11)*
  - **Related:** [defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness) · [deepsec](https://github.com/vercel-labs/deepsec)
- **[claude-code-security-review](https://github.com/anthropics/claude-code-security-review)** 🟠 — Official Claude-based semantic SAST GitHub Action that reviews PR diffs. *(Anthropic)* *(★ 5,866 · updated 2026-02-11)*
- **[IRIS](https://github.com/iris-sast/iris)** 🟢🔬 — Neurosymbolic SAST combining LLMs with CodeQL for Java vulnerability detection (MIT). *(★ 413 · updated 2026-07-02)*
- **[sast-skills](https://github.com/utkusen/sast-skills)** 🟢 — Agent skills that turn AI coding assistants into a multi-agent SAST scanner. *(★ 1,276 · updated 2026-04-08)*
  - **Related:** [Fraim](https://github.com/fraim-dev/fraim) · [llm-sast-scanner](https://github.com/SunWeb3Sec/llm-sast-scanner)
- **[llm-sast-scanner](https://github.com/SunWeb3Sec/llm-sast-scanner)** 🟢 — SAST skill for AI coding agents with structured source-to-sink analysis across 34 vulnerability classes. *License: MIT stated in README.* *(★ 274 · updated 2026-04-07)*
  - **Related:** [sast-skills](https://github.com/utkusen/sast-skills)
- **[sast-ai-workflow](https://github.com/RHEcosystemAppEng/sast-ai-workflow)** 🟢 — LangGraph workflow for reviewing static-analysis findings, reducing false positives, and producing vulnerability review output. *(Red Hat Ecosystem AppEng)* *(★ 20 · updated 2026-06-29)*
  - **Related:** [seclab-taskflow-agent](https://github.com/GitHubSecurityLab/seclab-taskflow-agent) · [Fraim](https://github.com/fraim-dev/fraim)
- **[llm-security-scanner](https://github.com/iknowjason/llm-security-scanner)** 🟢⚠️ — LLM-powered code scanner that opens GitHub issues for findings. *(★ 22 · updated 2025-04-02)*
- **[Trail of Bits Skills](https://github.com/trailofbits/skills)** 🟢⚠️ — Claude Code- and Codex-compatible security workflow skills for code review, differential review, false-positive analysis, supply-chain checks, GitHub Actions auditing, Semgrep rule generation, and vulnerability research. *(Trail of Bits)* — **note:** reusable agent workflow instructions rather than a standalone deterministic scanner; share-alike terms apply to adapted material. *(★ 6,624 · updated 2026-08-14)*
  - **Related:** [sast-skills](https://github.com/utkusen/sast-skills) · [Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter)
- **[OpenHack](https://github.com/hadriansecurity/OpenHack)** 🟢 — File-based source-guided white-box security-review workspace that orchestrates agents through reconnaissance, vulnerability hunting, validation, evidence capture, and reporting. *(Hadrian Security)* — **note:** requires an external coding harness/model and can consume substantial model tokens; OpenHack provides workflow state and review artifacts, not sandboxing or an execution-security boundary. Use only on authorized targets. *(★ 730 · updated 2026-06-01)*
  - **Related:** [deepsec](https://github.com/vercel-labs/deepsec) · [rust-in-peace](https://github.com/scadastrangelove/rust-in-peace)
- **[Buttercup](https://github.com/trailofbits/buttercup)** 🟢🔬⚠️ — Multi-component cyber reasoning system for finding, validating, and patching software vulnerabilities with coordinated agent workflows. *(Trail of Bits)* — **note:** AGPL-3.0 research/competition system rather than a lightweight scanner; deployment uses multiple services, Docker, and configured model providers. *(★ 1,676 · updated 2026-08-10)*
  - **Related:** [OpenHack](https://github.com/hadriansecurity/OpenHack) · [Visa Vulnerability Agentic Harness](https://github.com/visa/visa-vulnerability-agentic-harness)

---

## AI-Powered Threat Modeling

Architecture-level threat model generation and design-phase risk analysis driven by LLM reasoning.

- **[tachi](https://github.com/davidmatousek/tachi)** 🟢 — Threat modeling and AI-reasoning vulnerability detection harness for Claude Code that dispatches 14 specialized threat agents (6 STRIDE, 5 LLM, 3 agentic) against an architecture description in Mermaid, C4, PlantUML, ASCII, or free text, producing SARIF 2.1.0 for code scanning, MAESTRO seven-layer classification, attack trees, CVSS-aligned composite risk scores, compensating-controls analysis of the target codebase, and a PDF report. *(David Matousek)* — **note:** runs inside Claude Code; architecture descriptions are processed by the configured Claude model. *(★ 89 · updated 2026-08-13)*
  - **Related:** [STRIDE GPT](https://github.com/mrwadams/stride-gpt) · [defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness)
- **[STRIDE GPT](https://github.com/mrwadams/stride-gpt)** 🟢 — LLM-powered threat modeling tool that generates STRIDE threat models, attack trees, data flow diagrams, DREAD risk scores, mitigations, and Gherkin test cases from application descriptions, architecture diagrams, or codebases (agentic analysis mode), with OWASP LLM Top 10 and Agentic (ASI) coverage, MITRE ATT&CK/ATLAS mapping, Markdown/JSON/SARIF/HTML output, and broad LLM provider support via LiteLLM including local hosting. *(Matthew Adams)* *(★ 1,101 · updated 2026-08-12)*
  - **Related:** [tachi](https://github.com/davidmatousek/tachi)

---

## LLM-Driven Fuzzing

Two families: (a) LLMs generating harnesses/targets for traditional fuzzing, and (b) fuzzing the LLM itself.

### Harness / target generation

- **[oss-fuzz-gen](https://github.com/google/oss-fuzz-gen)** 🟢 — LLM-driven fuzz-harness generation for OSS-Fuzz; reported 26 real vulnerabilities (incl. CVE-2024-9143 in OpenSSL). *(Google)* *(★ 1,430 · updated 2026-03-02)*
- **[PromptFuzz](https://github.com/PromptFuzz/PromptFuzz)** 🟢🔬⚠️ — LLM-mutated prompts to generate fuzz drivers for C/C++ libraries (Rust). *(★ 342 · updated 2026-05-15)*
- **[Fuzz4All](https://github.com/fuzz4all/fuzz4all)** 🟢🔬 — "Universal" LLM-based fuzzer across compilers/languages (ICSE 2024). *(★ 336 · updated 2025-08-11)*
- **[ChatAFL](https://github.com/ChatAFLndss/ChatAFL)** 🟢🔬 — LLM-guided protocol fuzzing extending AFLNet (NDSS'24). *(★ 392 · updated 2025-06-20)*
- **[TitanFuzz](https://github.com/ise-uiuc/TitanFuzz)** 🟢🔬⚠️ — First LLM-based fuzzer for PyTorch/TensorFlow (ISSTA'23). *(★ 94 · updated 2023-09-10)*

### Fuzzing the LLM

- **[LLMFuzzer](https://github.com/mnns/LLMFuzzer)** 🟢🔬 — First open-source fuzzing framework for LLM API integrations. — **note:** historical research reference; maintenance appears low compared with current LLM security scanners. *(★ 377 · updated 2024-02-12)*
- **[ps-fuzz](https://github.com/prompt-security/ps-fuzz)** 🟠 — System-prompt hardening fuzzer; 16 attacks × 16 providers. *(Prompt Security)* *(★ 703 · updated 2026-02-16)*
- **[FuzzyAI](https://github.com/cyberark/FuzzyAI)** 🟠 — Automated LLM fuzzer for jailbreaks/prompt injection. *(CyberArk)* *(★ 1,563 · updated 2026-02-06)*
- **[spikee](https://github.com/ReversecLabs/spikee)** 🟢 — Prompt-injection evaluation and exploitation kit with dataset generation, Burp integration, and pluggable judges. *(ReversecLabs / WithSecure)* *(★ 231 · updated 2026-07-13)*
  - **Related:** [promptmap](https://github.com/utkusen/promptmap)
- **[promptmap](https://github.com/utkusen/promptmap)** 🟢⚠️ — Prompt-injection scanner for custom LLM applications in white-box and black-box modes; GPL-3.0 licensed. *(★ 1,250 · updated 2025-12-01)*
  - **Related:** [spikee](https://github.com/ReversecLabs/spikee)
- **[ai-prompt-fuzzer](https://github.com/PortSwigger/ai-prompt-fuzzer)** 🟢 — Burp Suite extension fuzzing GenAI/LLM prompts. *(PortSwigger)* *(★ 36 · updated 2025-09-04)*

---

## Threat Intelligence

AI/LLM tooling for CTI gathering, IOC/TTP extraction, and analysis.

- **[trs](https://github.com/deadbits/trs)** 🟢 — LLM + ChromaDB tool to summarize threat reports and extract MITRE TTPs and IOCs. *(★ 10 · updated 2023-11-15)*
- **[TI-Mindmap-GPT](https://github.com/format81/TI-Mindmap-GPT)** 🟢 — Streamlit app: AI summaries, mindmaps, IOC/TTP extraction, and ATT&CK Navigator layers. *(★ 111 · updated 2026-02-16)*
- **[aiocrioc](https://github.com/referefref/aiocrioc)** 🟢 — LLM + OCR IOC extraction (pulls IOCs from images/PDFs). *(★ 38 · updated 2024-12-04)*
- **[ThreatIngestor](https://github.com/InQuest/ThreatIngestor)** 🟢 — Extracts/aggregates IOCs from feeds; integrates with MISP/ThreatKB (pairs well with LLM post-processing). *(★ 922 · updated 2026-05-26)*
- **[IATelligence](https://github.com/fr0gger/IATelligence)** 🟢 — Explains imported Windows APIs in PE files via GPT and maps to MITRE ATT&CK. *(★ 384 · updated 2022-12-09)*
  - **Related:** [MCP_Security](https://github.com/fr0gger/MCP_Security)
- **[MCP_Security](https://github.com/fr0gger/MCP_Security)** 🟢⚠️ — MCP server (ORKL) for querying the ORKL threat-intel API. *(★ 51 · updated 2025-01-22)*
  - **Related:** [IATelligence](https://github.com/fr0gger/IATelligence)
- **[threat-intelligence-cti-analysis](https://github.com/AnandBinuArjun/threat-intelligence-cti-analysis)** 🟢 — NLP/LLM pipeline for IOC extraction, MITRE ATT&CK mapping, and knowledge-graph generation from unstructured CTI. *(★ 4 · updated 2025-11-03)*
  - **Related:** [soctalk](https://github.com/soctalk/soctalk)
- **[CTINexus](https://github.com/peng-gao-lab/ctinexus)** 🟢🔬 — LLM-assisted framework for data-efficient extraction of cyber-threat intelligence and construction of structured cybersecurity knowledge graphs from unstructured reports. — **note:** ships tests, releases, Docker configuration, and a Python package; extraction workflows require a configured supported LLM provider. *(★ 85 · updated 2026-02-25)*
  - **Related:** [threat-intelligence-cti-analysis](https://github.com/AnandBinuArjun/threat-intelligence-cti-analysis) · [CTIBench](https://github.com/maveryn/cti-bench)
- **[CTIBench](https://github.com/maveryn/cti-bench)** 🔬⚠️ — NeurIPS 2024 Spotlight benchmark with 4,610 examples across CTI knowledge, CWE root-cause mapping, CVSS prediction, ATT&CK technique extraction, and threat-actor attribution. — **note:** non-commercial research benchmark; the repository publishes data, evaluation notebooks, model outputs, and raw logs rather than a production CTI service. *(★ 92 · updated 2026-05-07)*
  - **Related:** [CTINexus](https://github.com/peng-gao-lab/ctinexus) · [CTI-BERT](https://huggingface.co/ibm-research/CTI-BERT)
- **[CTI-BERT](https://huggingface.co/ibm-research/CTI-BERT)** 🟢🔬 — BERT model pretrained from scratch on a large cybersecurity text corpus for downstream CTI extraction, classification, and question-answering tasks. *(IBM Research)* *license: Apache-2.0 · access: open · artifacts: PyTorch.*

---

## Log Analysis / SIEM / SOC Triage

AI agents for SOC alert triage, investigation, and incident response.

- **[AI-SOC-Agent](https://github.com/M507/ai-soc-agent)** 🟢 — Black Hat 2025 MCP server exposing security-investigation tools (ELK, IRIS). *(★ 47 · updated 2025-12-28)*
- **[soctalk](https://github.com/soctalk/soctalk)** 🟢 — LangGraph SOC automation agent with MCP integrations for Wazuh, Cortex, TheHive, and MISP plus mock-agent test lab. *(★ 78 · updated 2026-08-12)*
  - **Related:** [SigmaOptimizer](https://github.com/YusukeJustinNakajima/SigmaOptimizer)
- **[Vigil SOC](https://github.com/Vigil-SOC/vigil)** 🟢 — Open-source AI SOC with readable Python agents, Markdown playbooks, and MCP integrations for triage, investigation, hunting, response, reporting, and forensics. *(Vigil SOC)* *(★ 247 · updated 2026-08-17)*
  - **Related:** [soctalk](https://github.com/soctalk/soctalk)
- **[agentic-soc-platform](https://github.com/FunnyWolf/agentic-soc-platform)** 🟢 — Agentic SOC platform (LangGraph/Dify) with local-LLM support. *(★ 1,144 · updated 2026-08-05)*
- **[SigmAIQ](https://github.com/AttackIQ/SigmAIQ)** 🟢⚠️ — pySigma wrapper and LangChain toolkit for automatic Sigma rule creation and translation; LGPL-2.1 licensed. *(AttackIQ)* *(★ 97 · updated 2025-11-03)*
  - **Related:** [SigmaOptimizer](https://github.com/YusukeJustinNakajima/SigmaOptimizer)
- **[RulePilot](https://github.com/LLM4SOC-Topic/RulePilot)** 🟢🔬 — LLM-powered security-rule generation agent for Splunk, Microsoft Sentinel, and Elastic, with field detection from log samples, multi-stage refinement, and cross-platform rule conversion. — **note:** MIT-licensed ICSE 2026 research prototype; requires an OpenAI API key. *(★ 15 · updated 2025-10-20)*
  - **Related:** [SigmAIQ](https://github.com/AttackIQ/SigmAIQ) · [SigmaOptimizer](https://github.com/YusukeJustinNakajima/SigmaOptimizer)
- **[SOCGPT](https://github.com/Ninadjos/SOCGPT-AI-Powered-SOC-Assistant)** 🟢 — LLM log summarization, severity triage, MITRE mapping, and Q&A. *(★ 7 · updated 2025-06-11)*
- **[AttackGen](https://github.com/mrwadams/attackgen)** 🟢 — LLM-driven incident-response scenario generator using MITRE ATT&CK + ATLAS. *(★ 1,234 · updated 2026-08-13)*
- **[Google Security Operations and Threat Intelligence MCP Server](https://github.com/google/mcp-security)** 🟢 — MCP servers and packages that let MCP clients access Google Security Operations, SOAR, Google Threat Intelligence, and Security Command Center for investigation, hunting, and security automation workflows. *(Google Cloud)* — **note:** integration layer rather than an MCP-defense tool; requires Google credentials and access to the connected security products/services. *(★ 517 · updated 2026-04-29)*
  - **Related:** [MCP_Security](https://github.com/fr0gger/MCP_Security) · [Vigil SOC](https://github.com/Vigil-SOC/vigil)
- **[ExCyTIn-Bench (SecRL)](https://github.com/microsoft/SecRL)** 🟢🔬 — ICML 2026 benchmark for evaluating LLM agents on cyber-threat investigation and threat hunting through security question-answering over eight anonymized incident databases. *(Microsoft)* — **note:** evaluation requires model-provider credentials, Dockerized MySQL incident databases, and roughly 10 GB for the standard eight-container setup (up to 33 GB for the combined database). *(★ 143 · updated 2026-08-03)*
  - **Related:** [CTIBench](https://github.com/maveryn/cti-bench) · [Google Security Operations MCP](https://github.com/google/mcp-security)

---

## Reverse Engineering

LLM-assisted binary analysis and traffic inspection.

- **[Gepetto](https://github.com/JusticeRage/Gepetto)** 🟢 — IDA Pro plugin: GPT adds comments and meaningful variable names. *(★ 3,457 · updated 2026-08-15)*
- **[ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp)** 🟢 — MCP bridge for IDA Pro exposing decompile, disassemble, xref, rename, and debugging workflows to LLM clients. *(★ 11,393 · updated 2026-08-17)*
- **[GhidraMCP](https://github.com/LaurieWired/GhidraMCP)** 🟢 — MCP server exposing Ghidra reverse-engineering ops to any MCP-capable LLM. *(★ 9,805 · updated 2025-06-23)*
  - **Related:** [GhidrOllama](https://github.com/lr-m/GhidrOllama) · [OGhidra](https://github.com/llnl/OGhidra)
- **[ReVa](https://github.com/cyberkaida/reverse-engineering-assistant)** 🟢 — Ghidra-focused reverse-engineering assistant with MCP support, Claude Skills integration, and long-form analysis workflows. *(★ 805 · updated 2026-07-28)*
  - **Related:** [GhidraMCP](https://github.com/LaurieWired/GhidraMCP) · [GhidrAssistMCP](https://github.com/symgraph/GhidrAssistMCP)
- **[GhidrAssistMCP](https://github.com/symgraph/GhidrAssistMCP)** 🟢 — Native Ghidra MCP extension with broad tool coverage, headless support, and security-sensitive tool gating. *(★ 719 · updated 2026-08-02)*
  - **Related:** [ReVa](https://github.com/cyberkaida/reverse-engineering-assistant) · [ghidra-mcp](https://github.com/bethington/ghidra-mcp)
- **[ghidra-mcp](https://github.com/bethington/ghidra-mcp)** 🟢 — Ghidra MCP server with large tool coverage, GUI plugin, headless server, and lazy tool loading. *(★ 3,333 · updated 2026-08-12)*
  - **Related:** [GhidrAssistMCP](https://github.com/symgraph/GhidrAssistMCP)
- **[GhidrOllama](https://github.com/lr-m/GhidrOllama)** 🟢⚠️ — Ghidra script using the Ollama API for function analysis/renaming. *(★ 154 · updated 2024-11-29)*
  - **Related:** [OGhidra](https://github.com/llnl/OGhidra) · [GhidraMCP](https://github.com/LaurieWired/GhidraMCP)
- **[GhidraGPT](https://github.com/weirdmachine64/GhidraGPT)** 🟢 — Ghidra plugin that integrates LLMs for automated code refactoring and analysis. *(★ 658 · updated 2026-07-22)*
  - **Related:** [GhidraMCP](https://github.com/LaurieWired/GhidraMCP) · [ReVa](https://github.com/cyberkaida/reverse-engineering-assistant)
- **[LLM4Decompile](https://github.com/albertan017/LLM4Decompile)** 🟢🔬⚠️ — Research project for binary-to-C decompilation with LLMs; code is MIT, but model weights use a more restrictive license. *(★ 6,965 · updated 2026-02-12)*
- **[x64dbg_mcp](https://github.com/bromoket/x64dbg_mcp)** 🟢 — MCP server exposing x64dbg debugging and reverse-engineering operations to AI clients. *(★ 104 · updated 2026-06-08)*
- **[binaryninja-mcp](https://github.com/MCPPhalanx/binaryninja-mcp)** 🟢 — MCP server for Binary Ninja-assisted reverse engineering. *(★ 47 · updated 2025-05-13)*
- **[OGhidra](https://github.com/llnl/OGhidra)** 🟢 — Natural-language Ghidra analysis via Ollama. *(Lawrence Livermore National Lab)* *(★ 410 · updated 2026-08-14)*
  - **Related:** [GhidrOllama](https://github.com/lr-m/GhidrOllama) · [GhidraMCP](https://github.com/LaurieWired/GhidraMCP)
- **[ghidra_tools (G-3PO)](https://github.com/tenable/ghidra_tools)** 🟢 — Ghidra plugin for AI-assisted decompiled-code analysis. *(Tenable)* *(★ 312 · updated 2023-05-10)*
- **[gpt-wpre](https://github.com/moyix/gpt-wpre)** 🔬 — Whole-program reverse engineering with GPT-3. *(★ 407 · updated 2022-12-31)*
- **[burpgpt](https://github.com/aress31/burpgpt)** 🟢 — Burp Suite extension integrating GPT for passive scanning. *(★ 2,347 · updated 2024-06-09)*
  - **Related:** [Burp-extension-for-GPT](https://github.com/tenable/Burp-extension-for-GPT)
- **[Burp-extension-for-GPT](https://github.com/tenable/Burp-extension-for-GPT)** 🟢 — Burp extension to analyze HTTP traffic with GPT. *(Tenable)* *(★ 116 · updated 2023-05-01)*
  - **Related:** [burpgpt](https://github.com/aress31/burpgpt)
- **[REA](https://github.com/morluto/rea)** 🟢 — Local CLI and MCP toolkit for agent-assisted reverse engineering of native binaries, managed PE/CLI files, JavaScript/Electron apps, and browser runtimes, using Hopper or an operator-provided Ghidra installation. — **note:** deep native analysis uses separately licensed Hopper or operator-installed Ghidra. Setup can modify agent MCP registrations after interactive approval, and dynamic providers run with the current user's permissions; analyze only authorized artifacts. *(★ 346 · updated 2026-08-14)*
  - **Related:** [GhidraMCP](https://github.com/LaurieWired/GhidraMCP) · [ReVa](https://github.com/cyberkaida/reverse-engineering-assistant)

---

## LLM Red-Teaming & Guardrails

Tools for attacking and defending LLM applications themselves.

### Scanners, Evals & Guardrails

- **[NuGuard](https://github.com/NuGuardAI/nuguard)** 🟢 — Generates an AI-SBOM, statically analyzes agentic applications, red-teams live targets for prompt injection/tool misuse/data exfiltration, and validates behavioral policy compliance with SARIF, JSON, and Markdown reports. *(NuGuard AI)* — **note:** beta project; live red-team scans actively probe the target and require authorization. LLM-assisted features need provider credentials, and the optional NuGuard.ai hosted offering adds commercial features. *(★ 23 · updated 2026-08-14)*
  - **Related:** [garak](https://github.com/NVIDIA/garak) · [Medusa](https://github.com/Pantheon-Security/medusa)
- **[garak](https://github.com/NVIDIA/garak)** 🟢 — The LLM vulnerability scanner — probes for prompt injection, jailbreaks, data leakage, and more. *(NVIDIA)* *(★ 8,834 · updated 2026-08-14)*
  - **Related:** [PyRIT](https://github.com/microsoft/PyRIT) · [promptfoo](https://github.com/promptfoo/promptfoo)
- **[PyRIT](https://github.com/microsoft/PyRIT)** 🟢 — Python Risk Identification Tool; battle-tested across 100+ GenAI red-team operations. *(Microsoft)* *(★ 4,316 · updated 2026-08-14)*
- **[promptfoo](https://github.com/promptfoo/promptfoo)** 🟢 — LLM eval + red-teaming/pentesting CLI with 50+ attack plugins (MIT). *Note: OpenAI announced an acquisition agreement in March 2026; remains MIT-licensed — track governance.* *(★ 24,302 · updated 2026-08-17)*
- **[Augustus](https://github.com/praetorian-inc/augustus)** 🟢 — Single-binary LLM security testing framework for prompt injection, jailbreaks, and adversarial attacks across many providers. *(Praetorian)* *(★ 280 · updated 2026-08-17)*
  - **Related:** [garak](https://github.com/NVIDIA/garak) · [PyRIT](https://github.com/microsoft/PyRIT)
- **[agentic_security](https://github.com/msoedov/agentic_security)** 🟢 — Agentic LLM vulnerability scanner and AI red-team kit for jailbreaks, prompt injection, fuzzing, and API stress testing. *(★ 1,966 · updated 2026-07-31)*
  - **Related:** [garak](https://github.com/NVIDIA/garak) · [spikee](https://github.com/ReversecLabs/spikee)
- **[HackAgent](https://github.com/AISecurityLab/hackagent)** 🟢 — Python SDK and CLI for red-teaming AI agents with research-backed attacks such as AdvPrefix, AutoDAN-Turbo, PAIR, TAP, FlipAttack, BoN, and static templates across agent frameworks. — **note:** works locally without an API key; optional cloud reporting is available. *(★ 358 · updated 2026-08-15)*
  - **Related:** [PyRIT](https://github.com/microsoft/PyRIT) · [garak](https://github.com/NVIDIA/garak) · [agentic_security](https://github.com/msoedov/agentic_security)
- **[wallbreaker](https://github.com/JailbrokenAI/wallbreaker)** 🟢🔬⚠️ — Claude-Code-style terminal and red-team harness for authorized LLM safety testing, with HarmBench, PAIR/TAP, Crescendo, GCG-style workflows, Parseltongue transforms, MCP tooling, LLM judges, and reproducible run artifacts. — **note:** offensive jailbreak toolkit for authorized testing only; AGPL-3.0 licensed and NOTICE flags external jailbreak corpora with their own or missing upstream licenses. *(★ 1,208 · updated 2026-08-11)*
  - **Related:** [HarmBench](https://github.com/centerforaisafety/HarmBench) · [PyRIT](https://github.com/microsoft/PyRIT) · [garak](https://github.com/NVIDIA/garak)
- **[HiveTrace Red](https://github.com/HiveTrace/HiveTraceRed)** 🟢 — Early-stage LLM red-teaming framework with 80+ attack templates, async evaluation pipelines, WildGuard evaluators, multi-provider support, and HTML reporting. — **note:** young project with limited independent adoption signal. *(★ 29 · updated 2026-08-13)*
  - **Related:** [garak](https://github.com/NVIDIA/garak) · [PyRIT](https://github.com/microsoft/PyRIT) · [promptfoo](https://github.com/promptfoo/promptfoo)
- **[DeepTeam](https://github.com/confident-ai/deepteam)** 🟢 — Open-source framework for red-teaming LLMs and LLM systems across jailbreaks, prompt injection, data leakage, and safety risks. *(★ 2,451 · updated 2026-08-12)*
- **[Moonshot](https://github.com/aiverify-foundation/moonshot)** 🟢 — Modular tool for benchmarking, red-teaming, and evaluating LLM applications with custom connectors and recipes. *(AI Verify Foundation)* *(★ 347 · updated 2026-02-05)*
- **[Guardrails AI](https://github.com/guardrails-ai/guardrails)** 🟢 — Python framework for adding input/output guards, validators, structured-output controls, and Guardrails Hub checks to LLM applications. *(Guardrails AI)* *(★ 7,294 · updated 2026-08-14)*
  - **Related:** [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) · [LLM Guard](https://github.com/protectai/llm-guard)
- **[Giskard](https://github.com/Giskard-AI/giskard-oss)** 🟢 — Open-source evaluation, testing, and red-teaming framework for LLM agents, including agent vulnerability scanning and RAG evaluation workflows. *(Giskard AI)* *(★ 5,755 · updated 2026-08-17)*
  - **Related:** [Moonshot](https://github.com/aiverify-foundation/moonshot) · [promptfoo](https://github.com/promptfoo/promptfoo)
- **[LangKit](https://github.com/whylabs/langkit)** 🟢 — LLM monitoring toolkit extracting safety/security signals such as jailbreak similarity, prompt-injection similarity, hallucination checks, PII patterns, toxicity, and refusal metrics. *(WhyLabs)* *(★ 994 · updated 2024-11-22)*
- **[LLM Guard](https://github.com/protectai/llm-guard)** 🟢 — Suite of input/output scanners (PII, prompt injection, etc.). *(Protect AI)* — **note:** archived by the maintainer; retained as a historical reference for local input/output guardrails. *(★ 3,201 · updated 2026-07-08)*
  - **Related:** [Rebuff](https://github.com/protectai/rebuff)
- **[Rebuff](https://github.com/protectai/rebuff)** 🟢 — Archived prompt-injection detector (heuristics + LLM + vector DB + canary tokens). *(Protect AI)* — **note:** archived by the maintainer; retained as a historical prompt-injection defense reference. *(★ 1,520 · updated 2024-01-25)*
  - **Related:** [LLM Guard](https://github.com/protectai/llm-guard)
- **[NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails)** 🟢 — Programmable guardrails (input/output/dialog/retrieval rails) for LLM apps. *(NVIDIA)* *(★ 6,965 · updated 2026-08-17)*
- **[PurpleLlama](https://github.com/meta-llama/PurpleLlama)** 🟢 — Llama Guard classifiers, CodeShield, and CyberSecEval. *(Meta)* *(★ 4,355 · updated 2026-08-14)*
- **[LLAMATOR](https://github.com/LLAMATOR-Core/llamator)** 🟢⚠️ — Red-teaming framework for chatbots and GenAI systems; CC BY-NC-SA 4.0 licensed. *(★ 215 · updated 2026-01-15)*
- **[Vigil](https://github.com/deadbits/vigil-llm)** 🟢🔬 — Library/REST API to scan prompts and responses for prompt injection. *(★ 496 · updated 2024-01-31)*
- **[Counterfit](https://github.com/Azure/counterfit)** 🟢 — ML/AI penetration-testing automation tool. *(Microsoft)* *(★ 935 · updated 2025-07-18)*
- **[AI-Red-Teaming-Playground-Labs](https://github.com/microsoft/AI-Red-Teaming-Playground-Labs)** 🟢 — CTFd-based AI red-team training challenges. *(Microsoft)* *(★ 2,046 · updated 2025-10-07)*
- **[EasyJailbreak](https://github.com/EasyJailbreak/EasyJailbreak)** 🟢🔬 — Framework for building and testing adversarial jailbreak prompts. *(★ 886 · updated 2026-03-30)*
- **[TextAttack](https://github.com/QData/TextAttack)** 🟢🔬 — Python framework for adversarial attacks, data augmentation, and training for NLP models; useful for robustness testing beyond chat-only LLM scanners. *(★ 3,467 · updated 2026-08-15)*
- **[GPTFuzz](https://github.com/sherdencooper/GPTFuzz)** 🟢🔬 — Research framework for red-teaming LLMs with auto-generated jailbreak prompts. *(★ 604 · updated 2026-02-27)*
- **[HarmBench](https://github.com/centerforaisafety/HarmBench)** 🟢🔬 — ICML 2024 standardized evaluation framework for automated red-teaming and robust-refusal benchmarking. *(Center for AI Safety)* *(★ 1,029 · updated 2024-08-05)*
  - **Related:** [JailbreakBench](https://github.com/JailbreakBench/jailbreakbench)
- **[llm-attacks (GCG)](https://github.com/llm-attacks/llm-attacks)** 🟢🔬 — Canonical Greedy Coordinate Gradient adversarial-suffix attack implementation for transferable attacks on aligned language models. *(★ 4,761 · updated 2024-08-02)*
  - **Related:** [nanoGCG](https://github.com/GraySwanAI/nanoGCG)
- **[nanoGCG](https://github.com/GraySwanAI/nanoGCG)** 🟢 — Fast, lightweight PyTorch implementation of the GCG adversarial-suffix algorithm. *(★ 346 · updated 2025-05-13)*
  - **Related:** [llm-attacks (GCG)](https://github.com/llm-attacks/llm-attacks)
- **[JailbreakBench](https://github.com/JailbreakBench/jailbreakbench)** 🟢🔬 — NeurIPS 2024 open robustness benchmark and leaderboard for generating and defending against LLM jailbreaks. *(★ 654 · updated 2025-03-31)*
- **[Open-Prompt-Injection](https://github.com/liu00222/Open-Prompt-Injection)** 🟢🔬 — Open-source toolkit and benchmark for implementing and evaluating prompt-injection attacks, defenses, and LLM-integrated applications. *(★ 479 · updated 2025-10-29)*
- **[PINT Benchmark](https://github.com/lakeraai/pint-benchmark)** 🟢🔬 — Prompt-injection test benchmark for evaluating detectors and guardrails across multilingual prompt injection, jailbreak, benign, and hard-negative inputs. *(Lakera)* — **note:** archived benchmark retained as a historical research reference; use newer maintained corpora for current detector comparisons. *(★ 198 · updated 2026-04-02)*
  - **Related:** [Open-Prompt-Injection](https://github.com/liu00222/Open-Prompt-Injection) · [Prompt Guard 86M](https://huggingface.co/meta-llama/Prompt-Guard-86M)
- **[PIArena](https://github.com/sleeepeer/PIArena)** 🟢🔬 — ACL 2026 toolbox and benchmark for prompt-injection attacks and defenses, with ready-to-use attacks/defenses, evaluation pipelines, agent benchmarks, a Hugging Face dataset, and leaderboard. *(★ 47 · updated 2026-04-20)*
  - **Related:** [PINT Benchmark](https://github.com/lakeraai/pint-benchmark) · [Open-Prompt-Injection](https://github.com/liu00222/Open-Prompt-Injection)
- **[Whistleblower](https://github.com/Repello-AI/whistleblower)** 🟢⚠️ — Offensive testing tool for inferring system prompts and discovering capabilities of LLM applications exposed through APIs. *(Repello AI)* — **note:** no LICENSE file found. *(★ 177 · updated 2025-10-27)*
- **[LLMmap](https://github.com/pasquini-dario/LLMmap)** 🟢🔬 — Minimal-query fingerprinting tool for identifying LLMs from behavioral traces, with a pretrained open-set inference model. *(★ 424 · updated 2025-07-24)*
- **[llm-security](https://github.com/greshake/llm-security)** 🔬 — Original PoC for indirect prompt-injection attacks. *(★ 2,128 · updated 2025-07-17)*
- **[JailbreakLLMs](https://github.com/TrustAIRLab/JailbreakLLMs)** 🔬⚠️ — Research dataset of 6,387 ChatGPT prompts, including in-the-wild jailbreak prompts from Reddit, Discord, websites, and open datasets. *(★ 23 · updated 2024-02-21)*
- **[Do-Not-Answer](https://github.com/Libr-AI/do-not-answer)** 🟢🔬 — Dataset for evaluating LLM safeguards on unsafe or policy-sensitive prompts. *(★ 341 · updated 2024-06-07)*
- **[prompt-injection-defenses](https://github.com/tldrsec/prompt-injection-defenses)** 🟢⚠️ — Curated catalog of practical defenses against prompt injection. *(★ 724 · updated 2025-02-22)*
- **[little-canary](https://github.com/hermes-labs-ai/little-canary)** 🟢🔬 — Prompt-injection preflight risk sensor that routes untrusted input through a powerless sacrificial model, then reads response residue to return pass/flag/block before the primary agent acts. — **note:** experimental sensing layer, not a security guarantee or runtime containment. A failed canary can return availability-first routing with explicit degraded coverage; remote/OpenAI-compatible canary or judge endpoints receive raw input. *(★ 27 · updated 2026-08-14)*
  - **Related:** [Rebuff](https://github.com/protectai/rebuff) · [prompt-injection-defenses](https://github.com/tldrsec/prompt-injection-defenses)
- **[Kiji Privacy Proxy](https://github.com/Dataiku/kiji-proxy)** 🟢 — Local privacy proxy for OpenAI-compatible AI API traffic that detects and masks 26 PII types with an ONNX model before forwarding requests, then restores mappings in responses. *(Dataiku 575 Lab)* — **note:** protects configured proxied traffic, not every path by which an application or agent can disclose data; operators retain responsibility for proxy routing and local mapping storage. *(★ 422 · updated 2026-07-27)*
  - **Related:** [LLM Guard](https://github.com/protectai/llm-guard) · [Kiji PII model](https://huggingface.co/DataikuNLP/kiji-pii-model-onnx)
- **[Anamorpher](https://github.com/trailofbits/anamorpher)** 🟢🔬 — Research tool with a frontend and Python API for crafting and visualizing image-scaling attacks that reveal hidden prompt injections to multimodal AI systems after downscaling. *(Trail of Bits)* — **note:** active beta research tool for authorized testing; generated payloads are sensitive to the target's image-resampling implementation and preprocessing pipeline. *(★ 1,076 · updated 2026-02-19)*
  - **Sources:** [Trail of Bits research announcement](https://blog.trailofbits.com/2025/08/21/weaponizing-image-scaling-against-production-ai-systems/)
  - **Related:** [PromptFuzz](https://github.com/PromptFuzz/PromptFuzz) · [promptfoo](https://github.com/promptfoo/promptfoo)
- **[Prompt SIREN](https://github.com/facebookresearch/prompt-siren)** 🟢🔬 — Research workbench for developing and evaluating prompt-injection attacks and defenses with state-machine agent control, AgentDojo/SWE-bench integrations, configuration sweeps, and reproducible result aggregation. *(Meta AI)* — **note:** experiment harness; running target evaluations requires model-provider credentials and may need Docker or browser extras depending on the selected environment. *(★ 61 · updated 2026-05-18)*
  - **Related:** [AgentDojo](https://github.com/ethz-spylab/agentdojo) · [PyRIT](https://github.com/microsoft/PyRIT)

### Prompt-Injection Classifier Models

- **[Wolf Defender Prompt Injection](https://huggingface.co/patronus-studio/wolf-defender-prompt-injection)** 🟢 — Hugging Face text-classification model for prompt-injection detection in agents, chatbots, and CI workflows. *(Patronus Studio / Casdo Labs)* *license: Apache-2.0 · access: open · artifacts: Safetensors, ONNX.*
- **[DeBERTa v3 Prompt Injection v2](https://huggingface.co/protectai/deberta-v3-base-prompt-injection-v2)** 🟢 — Apache-licensed prompt-injection classifier usable via Transformers pipelines and ONNX. *(Protect AI)* *license: Apache-2.0 · access: open · artifacts: Safetensors, ONNX.*
- **[PromptGuard](https://huggingface.co/codeintegrity-ai/promptguard)** 🟢⚠️ — ModernBERT-based prompt-injection and jailbreak classifier. *(CodeIntegrity AI)* *license: Apache-2.0 · access: gated auto · artifacts: Safetensors.*
- **[Prompt Guard 86M](https://huggingface.co/meta-llama/Prompt-Guard-86M)** 🟠⚠️ — Meta prompt-injection and jailbreak classifier from the Llama Guard family. *(Meta)* *license: Llama 3.1 · access: gated manual · artifacts: Safetensors.*
- **[prompt-injection-sentinel](https://huggingface.co/qualifire/prompt-injection-sentinel)** 🔬⚠️ — ModernBERT-large classifier for prompt-injection and jailbreak detection. *(Qualifire)* *license: other · access: gated auto · artifacts: Safetensors.*

### Specialty Security LLMs

- **[SecGPT](https://github.com/Clouditera/SecGPT)** 🟢 — Open cybersecurity-tuned LLM family for vulnerability analysis, log/traffic investigation, anomaly detection, attack/defense reasoning, command analysis, and security Q&A. *(Clouditera)* *(★ 3,099 · updated 2025-06-25)*
  - **Related:** [SecGPT model](https://huggingface.co/clouditera/secgpt)
- **[Antares-1B](https://huggingface.co/fdtn-ai/antares-1b)** 🟢⚠️ — Open-weight security SLM specialized for agentic vulnerability localization: it explores repository snapshots through a terminal-style loop and ranks likely vulnerable files for analyst review. *(Cisco Foundation AI)* *license: Apache-2.0 · access: gated manual · artifacts: Safetensors + CLI ZIP.* — **note:** HF access is gated/manual; related smaller model: [Antares-350M](https://huggingface.co/fdtn-ai/antares-350m), benchmark: [VLoc Bench](https://cisco-foundation-ai.github.io/vulnerability-localization-benchmark/).
- **[Trendyol Cybersecurity LLM v2 70B](https://huggingface.co/Trendyol/Trendyol-Cybersecurity-LLM-v2-70B-Q4_K_M)** 🟢 — Defense-focused cybersecurity LLM based on Llama-3.3-70B, trained on an alignment-safe security instruction dataset for SOC, cloud, AppSec, detection, and vulnerability-management workflows. *(Trendyol Group Security Team)* *license: Apache-2.0 · access: open · artifacts: GGUF.*
- **[WhiteRabbitNeo 2.5 Qwen Coder 7B](https://huggingface.co/WhiteRabbitNeo/WhiteRabbitNeo-2.5-Qwen-2.5-Coder-7B)** 🟢⚠️ — Cybersecurity-oriented Qwen2.5-Coder fine-tune positioned for offensive and defensive security assistance. *(WhiteRabbitNeo)* *license: Apache-2.0 + WhiteRabbitNeo restrictions · access: open · artifacts: Safetensors.*
- **[Lily-Cybersecurity-7B-v0.2](https://huggingface.co/segolilylabs/Lily-Cybersecurity-7B-v0.2)** 🟢 — Mistral-7B-Instruct fine-tune for cybersecurity assistance, trained on hand-crafted security and hacking-related instruction pairs. *(Segolily Labs)* *license: Apache-2.0 · access: open · artifacts: Safetensors.*
- **[RavenX CyberAgent 35B Q4_K_M](https://huggingface.co/deadbydawn101/RavenX-CyberAgent-Qwen3.6-35B-A3B-Opus-4.7-OpenMythos-Pentester-BugHunter-RATH-GGUF)** 🟢⚠️ — GGUF security-specialized text-generation model positioned for pentest, bug-bounty, tool-calling, MCP, CVSS/CWE, and MITRE ATT&CK workflows. *(RavenX LLC / DeadByDawn101)* *license: Apache-2.0 · access: open · artifacts: GGUF.* — **note:** built from an abliterated base model and marketed for autonomous security assessment; use only in authorized, sandboxed agent harnesses with tool-call validation.

---

## LLM Honeypots & Deception

Honeypots and deception that use LLMs to simulate convincing systems.

- **[Beelzebub](https://github.com/beelzebub-labs/beelzebub)** 🟢⚠️ — Low-code honeypot using LLMs to simulate SSH/HTTP/MCP services (Go). — **note:** GPL-3.0 licensed. *(★ 2,148 · updated 2026-08-11)*
- **[DECEIVE](https://github.com/splunk/DECEIVE)** 🟢🔬 — Proof-of-concept LLM-powered SSH honeypot that evaluates sessions as benign, suspicious, or malicious. *(Splunk)* *(★ 288 · updated 2026-05-13)*
- **[TRAP](https://github.com/parameterlab/trap)** 🟢🔬 — Research code for Targeted Random Adversarial Prompt honeypots that identify black-box LLM usage through model-specific prompt suffixes (ACL 2024 Findings). *(★ 15 · updated 2024-11-20)*
- **[shelLM](https://github.com/stratosphereips/shelLM)** 🟢🔬 — LLM-powered SSH honeypot (paper *"LLM in the Shell"*). *(★ 64 · updated 2026-06-25)*
  - **Related:** [VelLMes](https://github.com/stratosphereips/VelLMes-AI-Honeypot)
- **[VelLMes](https://github.com/stratosphereips/VelLMes-AI-Honeypot)** 🟢🔬 — Multi-protocol LLM honeypot framework (successor to shelLM). *(★ 78 · updated 2025-02-18)*
  - **Related:** [shelLM](https://github.com/stratosphereips/shelLM)
- **[llm-honeypot](https://github.com/PalisadeResearch/llm-honeypot)** 🔬⚠️ — Cowrie SSH honeypot extended with prompt-injection traps to detect LLM hacker agents. *(Palisade Research)* *(★ 60 · updated 2026-01-23)*

---

## CTF / Exploit / Bug-Bounty Agents & Benchmarks

Offensive agents and the benchmarks used to evaluate them.

- **[SWE-agent (EnIGMA)](https://github.com/SWE-agent/SWE-agent)** 🟢🔬 — EnIGMA offensive-CTF mode; SOTA on NYU CTF, InterCode-CTF, and Cybench (v0.7 branch). *(★ 20,069 · updated 2026-07-16)*
  - **Related:** [Cybench](https://github.com/andyzorigin/cybench) · [NYU CTF Bench](https://github.com/NYU-LLM-CTF/NYU_CTF_Bench) · [InterCode](https://github.com/princeton-nlp/intercode)
- **[Cybench](https://github.com/andyzorigin/cybench)** 🔬 — 40 professional CTF tasks across 4 competitions; widely used by AI safety institutes. *(★ 311 · updated 2026-07-09)*
- **[NYU CTF Bench](https://github.com/NYU-LLM-CTF/NYU_CTF_Bench)** 🔬 — Dockerized CSAW CTF challenges for LLM-agent evaluation. *(★ 170 · updated 2025-09-22)*
- **[CTFTiny](https://github.com/NYU-LLM-CTF/CTFTiny)** 🔬⚠️ — Lightweight CTF benchmark from the NYU LLM CTF group; GPL-2.0 licensed. *(★ 18 · updated 2026-03-10)*
  - **Related:** [NYU CTF Bench](https://github.com/NYU-LLM-CTF/NYU_CTF_Bench)
- **[InterCode](https://github.com/princeton-nlp/intercode)** 🔬 — Interactive-coding benchmark incl. InterCode-CTF. *(★ 254 · updated 2024-05-05)*
- **[inspect_evals](https://github.com/UKGovernmentBEIS/inspect_evals)** 🟢🔬 — Maintained Inspect AI evaluation suite containing multiple cyber benchmarks and tasks. *(UK AI Security Institute)* *(★ 627 · updated 2026-08-17)*
- **[BountyBench](https://github.com/bountybench/bountybench)** 🔬 — 25 real systems / 40 bug bounties for Detect-Exploit-Patch evaluation. *(★ 102 · updated 2025-06-22)*
- **[Cyber-Zero](https://github.com/amazon-science/Cyber-Zero)** 🔬 — Trains cybersecurity agents without runtime; ships an EnIGMA+ scaffold. *(Amazon Science)* — **note:** archived research artifact retained as a historical reference for training cybersecurity agents without a live runtime. *(★ 101 · updated 2025-09-02)*
  - **Sources:** [SWE-agent](https://github.com/SWE-agent/SWE-agent)
  - **Related:** [SWE-agent](https://github.com/SWE-agent/SWE-agent)
- **[ExploitBench](https://github.com/exploitbench/exploitbench)** 🔬 — Measures AI-agent progress on V8/Chromium exploit ladders. *(★ 344 · updated 2026-07-04)*
- **[AI Goat](https://github.com/dhammon/ai-goat)** 🟢🔬⚠️ — Vulnerable-by-design local LLM CTF for learning prompt injection, insecure output handling, data leakage, excessive agency, and related LLM app risks. — **note:** GPL-2.0 licensed. *(★ 355 · updated 2024-08-22)*
- **[AIGoat](https://github.com/AISecurityConsortium/AIGoat)** 🟢🔬⚠️ — Local-first vulnerable LLM security playground with guided OWASP LLM Top 10 attack labs, CTF challenges, progressive defenses, and an Ollama-backed AI shopping-assistant target. — **note:** platform code is Apache-2.0, but training/challenge content is CC BY-NC-SA-4.0 and requires permission for commercial workshops. *(★ 76 · updated 2026-04-24)*
- **[LLMVault](https://github.com/CyberSunil/LLMVault)** 🟢🔬 — Intentionally vulnerable LLM security-training platform with OWASP LLM Top 10 labs, CTF-style challenges, hints, scoring, and mitigation guidance. — **note:** deliberately vulnerable training target; run only in an isolated, authorized environment. Live Mode optionally requires Ollama or provider credentials. *(★ 296 · updated 2026-08-10)*
- **[Damn Vulnerable LLM Agent](https://github.com/ReversecLabs/damn-vulnerable-llm-agent)** 🟢🔬 — Deliberately vulnerable LangChain ReAct agent for practicing prompt-injection and Thought/Action/Observation injection attacks. *(ReversecLabs / WithSecure)* *(★ 505 · updated 2025-06-25)*
  - **Related:** [spikee](https://github.com/ReversecLabs/spikee)
- **[claude-bug-bounty](https://github.com/shuvonsec/claude-bug-bounty)** 🟢 — Claude Code plugin orchestrating recon → vuln classes → reporting. *(★ 4,236 · updated 2026-08-10)*
- **[Bug-Bounty-Agents](https://github.com/matty69v/Bug-Bounty-Agents)** 🟢 — 43 AI agent personas for Claude Code / Copilot / Cursor across the bug-bounty lifecycle. *(★ 369 · updated 2026-04-30)*
- **[ai-exploits](https://github.com/protectai/ai-exploits)** 🟢 — Real-world AI/ML exploits (Metasploit modules + Nuclei templates) for MLflow, Ray, H2O. *(Protect AI)* *(★ 1,745 · updated 2024-10-23)*
- **[CyberGym](https://github.com/sunblaze-ucb/cybergym)** 🟢🔬 — Large-scale evaluation framework for AI-agent vulnerability analysis on real-world tasks, with locally deployed challenge infrastructure, task generation, and proof-of-concept validation. *(UC Berkeley / Sunblaze)* — **note:** deploy only in an isolated local environment; the full benchmark runtime is extremely large (documentation cites up to ~10 TB) and must not be exposed to the public internet. *(★ 737 · updated 2026-08-04)*
  - **Related:** [Cybench](https://github.com/andyzorigin/cybench) · [CVE-Bench](https://github.com/uiuc-kang-lab/cve-bench)
- **[CVE-Bench](https://github.com/uiuc-kang-lab/cve-bench)** 🟢🔬 — ICML 2025 benchmark that evaluates AI agents against reproducible Docker environments for real critical-severity web-application CVEs and exploit objectives. — **note:** runs intentionally vulnerable services and should be used only in isolated environments; arm64 support is experimental. *(★ 271 · updated 2026-01-14)*
  - **Related:** [CyberGym](https://github.com/sunblaze-ucb/cybergym) · [BountyBench](https://github.com/bountybench/bountybench)

---

## Cloud / IaC / DFIR / OSINT / Phishing

AI tooling for cloud/IaC security, digital forensics, OSINT, and phishing detection.

- **[EscalateGPT](https://github.com/tenable/EscalateGPT)** 🟢 — GPT-based discovery of privilege-escalation paths in AWS IAM policies. *(Tenable)* *(★ 122 · updated 2024-01-17)*
- **[Cynative](https://github.com/cynative/cynative)** 🟢 — Local AI security research agent for cloud, code, and runtime environments across GitHub, GitLab, AWS, GCP, Azure, and Kubernetes, with read-only action gates, sandboxed code execution, evidence-backed verification, and audit logs. *(★ 190 · updated 2026-08-14)*
  - **Related:** [Fraim](https://github.com/fraim-dev/fraim) · [EscalateGPT](https://github.com/tenable/EscalateGPT)
- **[Julius](https://github.com/praetorian-inc/julius)** 🟢 — Local Go tool that fingerprints LLM service infrastructure on authorized endpoints, identifies 60+ serving, gateway, MCP, and RAG platforms, and can enumerate exposed models. *(Praetorian)* — **note:** use only against endpoints you own or are authorized to assess. *(★ 208 · updated 2026-08-06)*
  - **Related:** [AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) · [ai_osint](https://github.com/7WaySecurity/ai_osint)
- **[MemoryInvestigator](https://github.com/jan-hendrik-lang/MemoryInvestigator)** 🔬 — Volatility 3 + LLM + RAG for memory-forensic triage. *(★ 13 · updated 2025-09-16)*
  - **Related:** [Volatility-MCP-Server](https://github.com/bornpresident/Volatility-MCP-Server)
- **[Volatility-MCP-Server](https://github.com/bornpresident/Volatility-MCP-Server)** 🟢 — MCP exposing Volatility 3 plugins for natural-language memory forensics. *(★ 39 · updated 2025-07-07)*
  - **Related:** [MemoryInvestigator](https://github.com/jan-hendrik-lang/MemoryInvestigator)
- **[llm_osint](https://github.com/sshh12/llm_osint)** 🟢🔬 — Proof-of-concept LLM OSINT framework using knowledge and web agents for internet research workflows. *(★ 317 · updated 2024-11-02)*
- **[ai_osint](https://github.com/7WaySecurity/ai_osint)** 🟢 — Curated AI-OSINT dorks, queries, and techniques for discovering exposed LLM and AI infrastructure. *(★ 154 · updated 2026-06-19)*
- **[PhishLLM](https://github.com/code-philia/PhishLLM)** 🔬⚠️ — Reference-less phishing detection via LLM brand recognition (USENIX'24). *(★ 39 · updated 2026-06-04)*
  - **Related:** [PhishVLM](https://github.com/code-philia/PhishVLM)
- **[mcp-dnstwist](https://github.com/BurtTheCoder/mcp-dnstwist)** 🟢 — MCP server for dnstwist DNS fuzzing to support typosquatting, phishing, and lookalike-domain analysis. *(★ 51 · updated 2025-03-03)*
- **[osintgpt](https://github.com/estebanpdl/osintgpt)** 🟢⚠️ — OpenAI embeddings + Qdrant over OSINT corpora. *(★ 525 · updated 2023-12-11)*

---

## Related Awesome Lists

- **[awesome-llm-cybersecurity-tools](https://github.com/tenable/awesome-llm-cybersecurity-tools)** — Tenable's list (archived but a strong reference). *(★ 488 · updated 2024-04-08)*
- **[Awesome-LLM4Cybersecurity](https://github.com/tmylla/Awesome-LLM4Cybersecurity)** — 600+ papers on LLMs for cybersecurity. *(★ 1,748 · updated 2026-07-08)*
- **[awesome-ai-cybersecurity](https://github.com/ElNiak/awesome-ai-cybersecurity)** — Broad AI-for-security collection. *(★ 151 · updated 2026-08-13)*
- **[awesome-genai-cyberhub](https://github.com/Ashfaaq98/awesome-genai-cyberhub)** — GenAI-driven cybersecurity resources. *(★ 54 · updated 2026-08-07)*
- **[awesome-ai-security](https://github.com/gmh5225/awesome-ai-security)** — For pentesters, bug hunters, and researchers. *(★ 39 · updated 2026-08-17)*
- **[awesome-ai-security](https://github.com/ottosulin/awesome-ai-security)** — AI security resources. *(★ 1,397 · updated 2026-08-16)*
- **[Awesome-AI-Security](https://github.com/TalEliyahu/Awesome-AI-Security)** — AI security resources. *(★ 853 · updated 2026-07-18)*
- **[Awesome-AI-For-Security](https://github.com/AmanPriyanshu/Awesome-AI-For-Security)** — AI-for-security tools, papers, and datasets. *(★ 146 · updated 2026-08-13)*
- **[awesome-cybersecurity-agentic-ai](https://github.com/raphabot/awesome-cybersecurity-agentic-ai)** — Agentic-AI cybersecurity tools and security MCP servers. *(★ 536 · updated 2026-06-28)*
- **[awesome-ai-agents-security](https://github.com/ProjectRecon/awesome-ai-agents-security)** — Focused map of AI-agent security resources across runtime protection, red-teaming scanners, static analysis, sandboxing, guardrails, benchmarks, and identity. *(★ 63 · updated 2026-06-12)*
- **[Awesome-Offensive-AI-Agentic-Landscape](https://github.com/Yeti-791/Awesome-Offensive-AI-Agentic-Landscape)** — Offensive AI-agent landscape covering open-source pentest/red-team agents, offensive/security-specialized models, papers, benchmarks, and commercial tools. *(★ 214 · updated 2026-07-20)*
- **[awesome-ai-agent-attacks](https://github.com/webpro255/awesome-ai-agent-attacks)** — Sourced timeline of real AI-agent security incidents, breaches, vulnerabilities, and attack techniques. *(★ 65 · updated 2026-08-11)*
- **[AI Security Repository Radar](https://github.com/Zero0x00/Ai-Security-radar-)** — Daily-updated AI/LLM/MCP/RAG security repository radar with category, license, stars, and quality/relevance metadata. *(★ 5 · updated 2026-08-17)*
- **[awesome-MLSecOps](https://github.com/RiccardoBiosas/awesome-MLSecOps)** — Curated MLSecOps resources spanning adversarial ML, LLM security, AI red teaming, model scanning, supply-chain protection, and MLOps pipeline security. *(★ 450 · updated 2026-08-15)*
- **[awesome-ai-guardrails](https://github.com/enguard-ai/awesome-ai-guardrails)** — Catalog of AI guardrail models, tools, organizations, datasets, and papers, with useful Hugging Face model coverage. *(★ 64 · updated 2026-07-30)*
- **[open-source-llm-scanners](https://github.com/psiinon/open-source-llm-scanners)** — Open-source LLM scanners and testing tools. *(★ 109 · updated 2026-02-05)*
- **[awesome-mcp-security](https://github.com/Puliczek/awesome-mcp-security)** — MCP security resources, tools, writeups, and server/client risk references. *(★ 729 · updated 2026-03-03)*
- **[awesome-ml-security](https://github.com/trailofbits/awesome-ml-security)** — Trail of Bits' curated machine-learning security resources. *(★ 170 · updated 2026-02-06)*
- **[awesome-ml-privacy-attacks](https://github.com/stratosphereips/awesome-ml-privacy-attacks)** — Machine-learning privacy-attack papers and resources. *(★ 640 · updated 2024-03-18)*
- **[awesome-ml-for-cybersecurity](https://github.com/jivoi/awesome-ml-for-cybersecurity)** — Large classic list of machine-learning-for-cybersecurity resources (stale-ish but still useful). *(★ 9,290 · updated 2024-04-11)*
- **[Awesome-AI4DevSecOps](https://github.com/awsm-research/Awesome-AI4DevSecOps)** — Taxonomy of AI-driven security solutions for DevSecOps. *(★ 19 · updated 2025-07-02)*
- **[awesome-llm-security](https://github.com/corca-ai/awesome-llm-security)** — Securing LLMs. *(★ 1,683 · updated 2025-08-20)*
- **[awesome-gpt-security](https://github.com/cckuailong/awesome-gpt-security)** — GPT/LLM security tools and cases. *(★ 669 · updated 2026-07-24)*
- **[awesome-threat-intelligence](https://github.com/hslatman/awesome-threat-intelligence)** — Classic CTI list (pairs with the AI-CTI section). *(★ 10,541 · updated 2026-05-31)*
- **[awesome-threat-modelling](https://github.com/hysnsec/awesome-threat-modelling)** — General-purpose threat modeling list — methodologies and non-AI tools (Threat Dragon, pytm, Threagile); dormant since 2023 but a solid reference. *(★ 1,793 · updated 2023-07-15)*
- **[Awesome-LLMs-for-Vulnerability-Detection](https://github.com/huhusmang/Awesome-LLMs-for-Vulnerability-Detection)** — Focused, continuously updated index of LLM-based software-vulnerability detection research across function, repository, agentic, and smart-contract analysis, including datasets, benchmarks, and surveys. *(★ 1,239 · updated 2026-08-16)*

---

## Contributing

Contributions are welcome! This README is generated from structured data.

1. Edit `data/sections.json` (validated by `data/schema.json`).
2. Use structured fields such as `status`, `flags`, and `license`; do not paste rendered emoji tags into the data.
3. Regenerate and check the README:

```bash
python3 scripts/update_github_metrics.py
python3 gen_readme.py
python3 gen_readme.py --check
```

Example entry:

```json
{
  "name": "ExampleTool",
  "repo": "OWNER/REPO",
  "status": ["open_source"],
  "license": "MIT",
  "flags": ["early_stage"],
  "desc": "One factual sentence about what the tool does.",
  "related": [
    {"label": "Sibling tool", "url": "https://github.com/OWNER/SIBLING"}
  ]
}
```

Status values: `open_source`, `research`, `commercial_open`. Common flags: `license_caveat`, `early_stage`, `archived`, `heavy_runtime`, `requires_api_key`, `authorized_testing_only`, `commercial_features`, `no_license`, `noncommercial`, `copyleft`, `abliterated_or_uncensored`.

Guidelines: link the canonical upstream repo (not a fork); verify the URL resolves; tag the correct type and add a caveat flag/note for non-permissive, non-commercial, unclear, missing, or restrictive licenses; prefer real, installable projects over blog-only references.

For Hugging Face model entries, include the model id, license, access status (open/gated), and artifact formats (for example Safetensors or ONNX).

## Contact

Maintained by **Sergey Gordeychik** — [scadastrangelove@gmail.com](mailto:scadastrangelove@gmail.com) · [blog](https://scadastrangelove.blogspot.com/) · [@scadasl](https://x.com/scadasl).

## License

To the extent possible under law, the contributors have waived all copyright and related rights to this list ([CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/)). Linked projects retain their own licenses — check each before use.
