# Emerging Projects

Early-stage LLM security projects with fewer than **50 GitHub stars**.

These stay visible for discovery while they gain traction. On periodic review they may move to the [main list](README.md) (≥50★), to [Unavailable Projects](deprecated.md) if gone, or to Inactive there if archived or abandoned.

---

## 🛠️ Tools

### 🧰 Multi-Purpose Model Scanners

- ![GitHub Repo stars](https://img.shields.io/github/stars/inkog-io/inkog?style=social) [**Inkog**](https://github.com/inkog-io/inkog) AI agent security scanner (CLI + MCP server) detects prompt injection, SQLi via LLM
- ![GitHub Repo stars](https://img.shields.io/github/stars/Mohamed7415/fpverify?style=social) [**fpverify**](https://github.com/Mohamed7415/fpverify): Detects silent model substitution by API relays via behavioral fingerprints
- ![GitHub Repo stars](https://img.shields.io/github/stars/tugkanboz/llm-security-scanner?style=social) [**LLM Security Scanner**](https://github.com/tugkanboz/llm-security-scanner) Prompt injection with OWASP LLM Top 10 and Turkish payloads

### 🤖 MCP & Agent Scanners

- ![GitHub Repo stars](https://img.shields.io/github/stars/ArmorerLabs/Armorer-Guard?style=social) [**Armorer Guard**](https://github.com/ArmorerLabs/Armorer-Guard) Local Rust scanner for AI-agent prompt injection and dangerous tool-call context
- ![GitHub Repo stars](https://img.shields.io/github/stars/pezhik/skilltotal?style=social) [**SkillTotal**](https://github.com/pezhik/skilltotal): Static scanner for MCP servers, agent skills, and npm/PyPI packages that cites file and line
- ![GitHub Repo stars](https://img.shields.io/github/stars/taoq-ai/ziran?style=social) [**Ziran**](https://github.com/taoq-ai/ziran) Security testing framework for AI agents
- ![GitHub Repo stars](https://img.shields.io/github/stars/sunglasses-dev/sunglasses?style=social) [**Sunglasses**](https://github.com/sunglasses-dev/sunglasses): Runtime trust scanner for AI agents covering prompt injection, tool poisoning, and MCP attacks
- ![GitHub Repo stars](https://img.shields.io/github/stars/razashariff/mcps-audit?style=social) [**MCPs-audit**](https://github.com/razashariff/mcps-audit) OWASP Security Scanner for MCP Servers
- ![GitHub Repo stars](https://img.shields.io/github/stars/Aveerayy/agent-guard?style=social) [**Agent Guard**](https://github.com/Aveerayy/agent-guard) Runtime governance firewall for AI agents, policy enforcement, MCP tool scanning
- ![GitHub Repo stars](https://img.shields.io/github/stars/DSHCorrectover/correctover-scan?style=social) [**correctover-scan**](https://github.com/DSHCorrectover/correctover-scan): CLI that scans MCP client config files for credential exposure, SSRF, and missing auth
- ![GitHub Repo stars](https://img.shields.io/github/stars/MAUROCERON/ai-agent-security-mini-audit?style=social) [**AI Agent Risk Self-Check**](https://github.com/MAUROCERON/ai-agent-security-mini-audit): Browser self-check for AI-agent workflow risks (OWASP/NIST mapping)
- ![GitHub Repo stars](https://img.shields.io/github/stars/AgentPostmortem/MCP-audit?style=social) [**MCP-audit**](https://github.com/AgentPostmortem/MCP-audit): Security scanner and linter for MCP servers with SARIF output
- ![GitHub Repo stars](https://img.shields.io/github/stars/maxugc/crosscheck?style=social) [**crosscheck skillcheck**](https://github.com/maxugc/crosscheck): Scans an agent skill or MCP server for injection, exfiltration, and credential theft before install
- ![GitHub Repo stars](https://img.shields.io/github/stars/Frank-Masciopinto/ironheights?style=social) [**Ironheights**](https://github.com/Frank-Masciopinto/ironheights): Pre-install security scanner for OpenClaw/ClawHub agent skills (prompt injection, credential theft, tampering)

### 💣 Prompt Injection

- ![GitHub Repo stars](https://img.shields.io/github/stars/controllability/jailbreak-evaluation?style=social) [**Jailbreak Evaluation**](https://github.com/controllability/jailbreak-evaluation): Python package for language model jailbreak evaluation
- ![GitHub Repo stars](https://img.shields.io/github/stars/Ventrova/sentinel-scan-cli?style=social) [**Sentinel Scan CLI**](https://github.com/Ventrova/sentinel-scan-cli): Free CLI running a 15-attack prompt-injection suite against your own LLM endpoint

### 🗡️ Autonomous Pentesting Frameworks

- ![GitHub Repo stars](https://img.shields.io/github/stars/scadastrangelove/rust-in-peace?style=social) [**rust-in-peace**](https://github.com/scadastrangelove/rust-in-peace): Agent-assisted vulnerability discovery for Rust, Android APKs, and AI agents

### 🛡️ Defensive & Guardrail Tools

- ![GitHub Repo stars](https://img.shields.io/github/stars/aisecuritygateway/aisecuritygateway?style=social) [**AI Security Gateway**](https://github.com/aisecuritygateway/aisecuritygateway): LLM firewall with PII redaction, prompt injection blocking for LLM APIs.
- ![GitHub stars](https://img.shields.io/github/stars/LostOxygen/llm-confidentiality?style=social) [**LLM Confidentiality**](https://github.com/LostOxygen/llm-confidentiality): Ensuring confidentiality in LLMs
- ![GitHub Repo stars](https://img.shields.io/github/stars/hermes-labs-ai/little-canary?style=social) [**little-canary**](https://github.com/hermes-labs-ai/little-canary): Detects prompt injection via a sacrificial canary model before the primary model acts
- ![GitHub Repo stars](https://img.shields.io/github/stars/GetSHIM/shim-cli?style=social) [**shim-cli**](https://github.com/GetSHIM/shim-cli): Local hooks that mask secrets and PII in coding-agent tool results
- ![GitHub Repo stars](https://img.shields.io/github/stars/pixiebrix/agent-browser-shield?style=social) [**Agent Browser Shield**](https://github.com/pixiebrix/agent-browser-shield): Browser extension stripping prompt injection and masking PII before pages reach an agent
- ![GitHub stars](https://img.shields.io/github/stars/NeuralTrust/TrustGate?style=social) [**TrustGate**](https://github.com/NeuralTrust/TrustGate): Generative Application Firewall for GenAI Applications
- ![GitHub Repo stars](https://img.shields.io/github/stars/purseclab/jailbreak-defense?style=social) [**Jailbreak Defense (Draft Models)**](https://github.com/purseclab/jailbreak-defense): Pre-model safeguard using draft models to screen inputs (CAIS'26)
- ![GitHub Repo stars](https://img.shields.io/github/stars/foro-sh/pii-mcp?style=social) [**pii-mcp**](https://github.com/foro-sh/pii-mcp): MCP middleware that redacts PII from tool results before they reach the model
- ![GitHub Repo stars](https://img.shields.io/github/stars/selan-ai/whatileaked?style=social) [**whatileaked**](https://github.com/selan-ai/whatileaked): Scans local Claude Code, Codex and Cursor transcripts for credentials already sent to the model
- ![GitHub Repo stars](https://img.shields.io/github/stars/AtlasPA/openclaw-security?style=social) [**OpenClaw Security Suite**](https://github.com/AtlasPA/openclaw-security): Defensive security suite for AI agent workspaces (prompt injection, integrity verification, secret scanning, supply chain analysis)
- ![GitHub Repo stars](https://img.shields.io/github/stars/krishyaid-coder/sluice?style=social) [**Sluice**](https://github.com/krishyaid-coder/sluice): Local MCP proxy that tracks sensitive values and blocks cross-tool data leaks
- ![GitHub Repo stars](https://img.shields.io/github/stars/Negative-Star-Innovators/AgentRedactor?style=social) [**AgentRedactor**](https://github.com/Negative-Star-Innovators/AgentRedactor): Local proxy redacting PII/secrets from coding-agent LLM requests and restoring responses
- ![GitHub Repo stars](https://img.shields.io/github/stars/jinyounghub/agentic-workflow-guard?style=social) [**agentic-workflow-guard**](https://github.com/jinyounghub/agentic-workflow-guard): CLI and GitHub Action detecting prompt-injection paths in AI-powered GitHub Actions workflows
- ![GitHub Repo stars](https://img.shields.io/github/stars/knbtz65v2c-pixel/plumblint?style=social) [**Plumblint**](https://github.com/knbtz65v2c-pixel/plumblint): Local zero-dependency prompt-injection detector with published calibration and known bypasses
- ![GitHub Repo stars](https://img.shields.io/github/stars/markmishaev76/Prompt-Shield?style=social) [**Prompt Shield**](https://github.com/markmishaev76/Prompt-Shield): GitHub Action for detecting indirect prompt injection in CI/CD pipelines. 4-layer defense architecture
- ![GitHub Repo stars](https://img.shields.io/github/stars/ppcvote/ultraprobe?style=social) [**UltraProbe**](https://github.com/ppcvote/ultraprobe): Deterministic CLI auditing system prompts and agent tool descriptions for missing prompt-injection defenses

### 🔐 Agent Authorization & Governance

- ![GitHub Repo stars](https://img.shields.io/github/stars/agentguard-ai/tealtiger?style=social) [**TealTiger**](https://github.com/agentguard-ai/tealtiger): Deterministic runtime governance for AI agents with tool allowlisting and SARIF audit evidence
- ![GitHub Repo stars](https://img.shields.io/github/stars/ProvablyAI/sourcerykit?style=social) [**SourceryKit**](https://github.com/ProvablyAI/sourcerykit): Verifies agent HTTP/MCP calls against a trusted source with ZK proofs and allow-list blocking
- ![GitHub Repo stars](https://img.shields.io/github/stars/anthony-chaudhary/dos-kernel?style=social) [**DOS Kernel**](https://github.com/anthony-chaudhary/dos-kernel): Deterministic trust kernel verifying agent done-claims from git evidence
- ![GitHub Repo stars](https://img.shields.io/github/stars/onkarbadve/agy-auto?style=social) [**agy-auto**](https://github.com/onkarbadve/agy-auto): PreToolUse permission firewall for CLI agents with deterministic deny and scoped approvals
- ![GitHub Repo stars](https://img.shields.io/github/stars/dislovelhl/acgs-lite?style=social) [**Acgs-lite**](https://github.com/dislovelhl/acgs-lite): Governance layer blocking unsafe agent actions with audit trails
- ![GitHub Repo stars](https://img.shields.io/github/stars/phinq-co/phinq?style=social) [**Phinq**](https://github.com/phinq-co/phinq): Governance proxy with tool-call risk scoring, human approval, and audit log
- ![GitHub Repo stars](https://img.shields.io/github/stars/vijaym2k6/SteerPlane?style=social) [**SteerPlane**](https://github.com/vijaym2k6/SteerPlane): Runtime guardrails for AI agents: loop detection, cost ceilings, and tool-call allow/deny rules
- ![GitHub Repo stars](https://img.shields.io/github/stars/BGMLAI/gate.cat?style=social) [**gate.cat**](https://github.com/BGMLAI/gate.cat): Deterministic action veto blocking destructive coding-agent commands before execution
- ![GitHub Repo stars](https://img.shields.io/github/stars/raintree-technology/policystrata?style=social) [**PolicyStrata**](https://github.com/raintree-technology/policystrata): Deterministic policy regression testing and runtime decision gates for LLM data agents
- ![GitHub stars](https://img.shields.io/github/stars/MrLightful/scopra?style=social) [**Scopra**](https://github.com/MrLightful/scopra): Business-rule policy SDK for evaluating agent input and output before actions run
- ![GitHub Repo stars](https://img.shields.io/github/stars/hamidmatiny/aegis?style=social) [**AEGIS**](https://github.com/hamidmatiny/aegis): LLM gateway with agent-gate tool permissioning and Ed25519 audit trails

---

## 🕵️ Benchmarks

- ![GitHub Repo stars](https://img.shields.io/github/stars/hermes-labs-ai/hermes-jailbench?style=social) [**hermes-jailbench**](https://github.com/hermes-labs-ai/hermes-jailbench): Known-pattern jailbreak regression benchmark for LLM endpoints with deterministic scoring
- ![GitHub stars](https://img.shields.io/github/stars/bastion-soft/pi-detector-bench?style=social) [**PI Detector Bench**](https://github.com/bastion-soft/pi-detector-bench): Benchmark for prompt-injection detectors scoring catch-rate and false positives
- ![GitHub Repo stars](https://img.shields.io/github/stars/astrogilda/agent-evidence-vectors?style=social) [**agent-evidence-vectors**](https://github.com/astrogilda/agent-evidence-vectors): Conformance vectors and a reference verifier for in-toto agent execution evidence
- ![GitHub Repo stars](https://img.shields.io/github/stars/raxITlabs/decision-models-as-guardrails?style=social) [**Decision Models as Guardrails**](https://github.com/raxITlabs/decision-models-as-guardrails): Benchmark of 18 decision models and Bedrock Guardrails on 9,975 guardrail checks, scoring accuracy and cost

---

## 🧪 Playground

- ![GitHub Repo stars](https://img.shields.io/github/stars/ReversecLabs/llm-vulnerable-recruitment-app?style=social) [**LLM CV Screener**](https://github.com/ReversecLabs/llm-vulnerable-recruitment-app)

---

## 🧪 PoC & Study Resources

- ![GitHub stars](https://img.shields.io/github/stars/HKU-TASR/Imperio?style=social) [Imperio](https://github.com/HKU-TASR/Imperio): Robust prompt engineering for anchoring LLMs
- ![GitHub stars](https://img.shields.io/github/stars/meng-wenlong/LMSanitator?style=social) [LMSanitator](https://github.com/meng-wenlong/LMSanitator): Defending LLMs against stealthy prompt injection
- ![GitHub stars](https://img.shields.io/github/stars/wegodev2/virtual-prompt-injection?style=social) [Virtual Prompt Injection](https://github.com/wegodev2/virtual-prompt-injection): Tool for virtual prompt injection
- ![GitHub stars](https://img.shields.io/github/stars/MiracleHH/CBA?style=social) [CBA](https://github.com/MiracleHH/CBA): Consciousness-Based Authentication for LLM Security
- ![GitHub stars](https://img.shields.io/github/stars/StavC/PromptWares?style=social) [PromptWare](https://github.com/StavC/PromptWares): PromptWares for GenAI-powered applications
- ![GitHub stars](https://img.shields.io/github/stars/ZrW00/MuScleLoRA?style=social) [MuScleLoRA](https://github.com/ZrW00/MuScleLoRA): Multi-scenario backdoor fine-tuning of LLMs
- ![GitHub stars](https://img.shields.io/github/stars/UCF-ML-Research/TrojText?style=social) [TrojText](https://github.com/UCF-ML-Research/TrojText): Trojan attacks on text classifiers
- ![GitHub stars](https://img.shields.io/github/stars/clearloveclearlove/BadActs?style=social) [BadActs](https://github.com/clearloveclearlove/BadActs): Backdoor attacks via activation steering
- ![GitHub Repo stars](https://img.shields.io/github/stars/Continuum-AI-Corp/Orca-AI-Incident-Archive?style=social) [**Orca AI Incident Archive**](https://github.com/Continuum-AI-Corp/Orca-AI-Incident-Archive): Sourced database of real-world AI agent security incidents, flagging confirmed harm and AI involvement
- ![GitHub stars](https://img.shields.io/github/stars/naimul011/backdoor_attacks_on_fine-tuned_llama?style=social) [Backdoor Attacks on Fine-tuned LLaMA](https://github.com/naimul011/backdoor_attacks_on_fine-tuned_llama): Backdoor attacks on fine-tuned LLaMA
