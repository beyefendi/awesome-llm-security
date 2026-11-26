
# 🤖 Awesome LLM Security [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

---

## 📚 Table of Contents

- [🤖 Awesome LLM Security ](#-awesome-llm-security-)
  - [📚 Table of Contents](#-table-of-contents)
  - [🛠️ Tools](#️-tools)
  - [🕵️ Benchmarks](#️-benchmarks)
  - [🧩 Threat Modeling](#-threat-modeling)
  - [🧪 Playground](#-playground)
  - [🧪 PoC \& Study Resources](#-poc--study-resources)
  - [🎥 Courses](#-courses)
  - [🌟 Miscellaneous](#-miscellaneous)
  - [📰 Blogs and Social Media](#-blogs-and-social-media)
  - [🙏 Acknowledgements](#-acknowledgements)
  - [Star History](#star-history)

---

## 🛠️ Tools

![misused](https://img.shields.io/badge/misused-b91c1c?style=flat-square) A vendor, CERT, or government report names the project in a real operation.

### 🧰 Multi-Purpose Model Scanners

- ![GitHub Repo stars](https://img.shields.io/github/stars/promptfoo/promptfoo?style=social) [**promptfoo**](https://github.com/promptfoo/promptfoo) LLM red teaming and evaluation framework with CI/CD integration
- ![GitHub Repo stars](https://img.shields.io/github/stars/leondz/garak?style=social) [**Garak**](https://github.com/leondz/garak/) LLM vulnerability scanner
- ![GitHub Repo stars](https://img.shields.io/github/stars/Tencent/AI-Infra-Guard?color=gold) [**AI-Infra-Guard**](https://github.com/Tencent/AI-Infra-Guard/) LLM vulnerability scanner with Web UI, REST APIs, and Dockerized
- ![GitHub Repo stars](https://img.shields.io/github/stars/laiyer-ai/llm-guard?style=social) [**LLM Guard**](https://github.com/laiyer-ai/llm-guard) Security toolkit for LLM interactions
- ![GitHub Repo stars](https://img.shields.io/github/stars/confident-ai/deepteam?style=social) [**DeepTeam**](https://github.com/confident-ai/deepteam) LLM red teaming framework (prompt injection, hallucination, data leaks, jailbreaks)
- ![GitHub stars](https://img.shields.io/github/stars/msoedov/agentic_security?style=social) [**Agentic Security**](https://github.com/msoedov/agentic_security) Security toolkit for AI agents
- ![GitHub Repo stars](https://img.shields.io/github/stars/toby-bridges/api-relay-audit?style=social) [**API Relay Audit**](https://github.com/toby-bridges/api-relay-audit): Local CLI for auditing third-party LLM relays and proxies for prompt injection and response anomalies
- ![GitHub stars](https://img.shields.io/github/stars/0din-ai/ai-scanner?style=social) [**AI-Scanner**](https://github.com/0din-ai/ai-scanner) AI model safety scanner built on NVIDIA garak
- ![GitHub stars](https://img.shields.io/github/stars/pasquini-dario/LLMmap?style=social) [**LLMmap**](https://github.com/pasquini-dario/LLMmap) Tool for mapping LLM vulnerabilities
- ![GitHub stars](https://img.shields.io/github/stars/RomiconEZ/LLaMator?style=social) [**LLaMator**](https://github.com/RomiconEZ/LLaMator) Framework for testing vulnerabilities of LLMs
- ![GitHub Repo stars](https://img.shields.io/github/stars/kortex-labs/plexiglass?style=social) [**Plexiglass**](https://github.com/kortex-labs/plexiglass) Security toolbox for testing and safeguarding LLMs

---

### 🤖 MCP & Agent Scanners

- ![GitHub stars](https://img.shields.io/github/stars/THUDM/AgentBench?style=social) [**AgentBench**](https://github.com/THUDM/AgentBench): Benchmark to evaluate LLMs as agents
- ![GitHub Repo stars](https://img.shields.io/github/stars/cisco-ai-defense/mcp-scanner?style=social) [**MCP Scanner**](https://github.com/cisco-ai-defense/mcp-scanner) Scan MCP servers for potential threats & security findings
- ![GitHub Repo stars](https://img.shields.io/github/stars/splx-ai/agentic-radar?style=social) [**Agentic Radar**](https://github.com/splx-ai/agentic-radar) Open-source CLI security scanner for agentic workflows
- ![GitHub stars](https://img.shields.io/github/stars/Puliczek/awesome-mcp-security?style=social) [**Awesome MCP Security**](https://github.com/Puliczek/awesome-mcp-security) Curated list of MCP security resources
- ![GitHub Repo stars](https://img.shields.io/github/stars/riseandignite/mcp-shield?style=social) [**MCP Shield**](https://github.com/riseandignite/mcp-shield) Security scanner for MCP servers
- ![GitHub Repo stars](https://img.shields.io/github/stars/Repello-AI/Agent-Wiz?style=social) [**Agent-Wiz**](https://github.com/Repello-AI/Agent-Wiz): CLI for threat modeling agentic workflows from LangChain, LangGraph, CrewAI, and AutoGen
- ![GitHub Repo stars](https://img.shields.io/github/stars/humanbound/humanbound?style=social) [**Humanbound**](https://github.com/humanbound/humanbound): Runs LLM-generated adversarial attacks against agents over HTTP, scored against OWASP LLM and Agentic Top 10
- ![GitHub Repo stars](https://img.shields.io/github/stars/johnhalloran321/mcpSafetyScanner?style=social) [**MCP Safety Scanner**](https://github.com/johnhalloran321/mcpSafetyScanner) Automated MCP safety auditing and remediation using Agents
- ![GitHub Repo stars](https://img.shields.io/github/stars/alexgreensh/repo-forensics?style=social) [**Repo Forensics**](https://github.com/alexgreensh/repo-forensics): Offline scanner for agent repos, skills, plugins, and MCP servers detecting supply-chain and injection risk
- ![GitHub Repo stars](https://img.shields.io/github/stars/sinewaveai/agent-security-scanner-mcp?style=social) [**Agent Security Scanner MCP**](https://github.com/sinewaveai/agent-security-scanner-mcp) MCP server for scanning code for web vulnerabilities, prompt injection, and AI-hallucinated package detection
- ![GitHub stars](https://img.shields.io/github/stars/wearetyomsmnv/Awesome-LLM-agent-Security?style=social) [**Awesome LLM Agent Security**](https://github.com/wearetyomsmnv/Awesome-LLM-agent-Security) LLM agent security resources, attacks, vulnerabilities
- [**Skill Safe**](https://skillsafe.online): Free hosted security checker for AI agent skills and MCP servers

---

### 🧑‍💻 RAG Security

- ![GitHub stars](https://img.shields.io/github/stars/sleeepeer/PoisonedRAG?style=social) [**PoisonedRAG**](https://github.com/sleeepeer/PoisonedRAG) Poisoned RAG systems
- [**RAG Attacks and Mitigations**](https://github.com/wearetyomsmnv/Adversarial-AI---Attacks-Mitigations-and-Defense-Strategies/tree/main/ch15/RAG) RAG attacks, mitigations, and defense strategies
- [**Awesome Jailbreak on LLMs - RAG Attacks**](https://github.com/yueliu1999/Awesome-Jailbreak-on-LLMs?tab=readme-ov-file#attack-on-rag-based-llm) RAG-based LLM attack techniques

---

### 💣 Prompt Injection

- ![GitHub Repo stars](https://img.shields.io/github/stars/verazuo/jailbreak_llms?color=gold) [**Jailbreak LLMs**](https://github.com/verazuo/jailbreak_llms): Real-world prompt jailbreak dataset (15k+ examples)
- ![GitHub Repo stars](https://img.shields.io/github/stars/yueliu1999/Awesome-Jailbreak-on-LLMs?color=gold) [**Awesome Jailbreak LLMs**](https://github.com/yueliu1999/Awesome-Jailbreak-on-LLMs): Collection of jailbreak techniques, datasets, and defenses
- ![GitHub Repo stars](https://img.shields.io/github/stars/patrickrchao/JailbreakingLLMs?color=gold) [**Jailbreaking LLMs (PAIR)**](https://github.com/patrickrchao/JailbreakingLLMs): Black-box jailbreak generation via automatic prompt refinement
- ![GitHub Repo stars](https://img.shields.io/github/stars/prompt-security/ps-fuzz?style=social) [**Prompt Fuzzer**](https://github.com/prompt-security/ps-fuzz): Harden your GenAI applications
- ![GitHub Repo stars](https://img.shields.io/github/stars/liu00222/Open-Prompt-Injection?style=social) [**Open Prompt Injection**](https://github.com/liu00222/Open-Prompt-Injection): Evaluate prompt injection attacks and defenses on benchmark datasets
- ![GitHub Repo stars](https://img.shields.io/github/stars/mnns/LLMFuzzer?style=social) [**LLMFuzzer**](https://github.com/mnns/LLMFuzzer): Fuzzing framework for LLM prompt generation
- ![GitHub Repo stars](https://img.shields.io/github/stars/ReversecLabs/spikee?color=gold) [**Spikee**](https://github.com/ReversecLabs/spikee): Prompt injection toolkit

---

### 🗡️ Autonomous Pentest Agents

- ![GitHub Repo stars](https://img.shields.io/github/stars/usestrix/strix?style=social) ![misused](https://img.shields.io/badge/misused-b91c1c?style=flat-square) [**Strix**](https://github.com/usestrix/strix): Multi-agent pentest framework.
- ![GitHub Repo stars](https://img.shields.io/github/stars/KeygraphHQ/shannon?style=social) [**Shannon**](https://github.com/KeygraphHQ/shannon): AI pentester that reads source, then attacks the running app to prove each finding.
- ![GitHub Repo stars](https://img.shields.io/github/stars/vxcontrol/pentagi?style=social) ![misused](https://img.shields.io/badge/misused-b91c1c?style=flat-square) [**PentAGI**](https://github.com/vxcontrol/pentagi): Multi-agent pentest system.
- ![GitHub Repo stars](https://img.shields.io/github/stars/BaaRai/ARTEX?style=social) ![misused](https://img.shields.io/badge/misused-b91c1c?style=flat-square) [**ARTEX**](https://github.com/BaaRai/ARTEX): Autonomous multi-agent penetration testing system.
- ![GitHub Repo stars](https://img.shields.io/github/stars/GreyDGL/PentestGPT?style=social) ![misused](https://img.shields.io/badge/misused-b91c1c?style=flat-square) [**PentestGPT**](https://github.com/GreyDGL/PentestGPT): Autonomous pentest agent.
- ![GitHub Repo stars](https://img.shields.io/github/stars/0x4m4/hexstrike-ai?style=social) ![misused](https://img.shields.io/badge/misused-b91c1c?style=flat-square) [**HexStrike AI**](https://github.com/0x4m4/hexstrike-ai): MCP server that lets agents run offensive-security tools for automated pentesting.
- ![GitHub Repo stars](https://img.shields.io/github/stars/AIPentest/CyberStrikeAI?style=social) ![misused](https://img.shields.io/badge/misused-b91c1c?style=flat-square) [**CyberStrikeAI**](https://github.com/AIPentest/CyberStrikeAI): AI pentest workspace with agents, MCP tools, and attack-chain evidence.
- ![GitHub Repo stars](https://img.shields.io/github/stars/elder-plinius/T3MP3ST?style=social) [**T3MP3ST**](https://github.com/elder-plinius/T3MP3ST): Autonomous multi-agent red-team harness.
- ![GitHub Repo stars](https://img.shields.io/github/stars/BitterSecurity/Decepticon?style=social) [**Decepticon**](https://github.com/BitterSecurity/Decepticon): Autonomous hacking agent for red teams.
- ![GitHub Repo stars](https://img.shields.io/github/stars/awarexone/Agentic-Bug-Hunter?style=social) [**Agentic Bug Hunter**](https://github.com/awarexone/Agentic-Bug-Hunter): AI-powered bug bounty hunting toolkit.
- ![GitHub Repo stars](https://img.shields.io/github/stars/oritera/Cairn?style=social) ![misused](https://img.shields.io/badge/misused-b91c1c?style=flat-square) [**Cairn**](https://github.com/oritera/Cairn): State-space search engine for autonomous penetration testing.
- ![GitHub Repo stars](https://img.shields.io/github/stars/sooryathejas/METATRON?style=social) [**METATRON**](https://github.com/sooryathejas/METATRON): Local-LLM pentest assistant that runs recon tools and analyzes the results.
- ![GitHub Repo stars](https://img.shields.io/github/stars/Netw0rkNoob/VulnClaw?style=social) [**VulnClaw**](https://github.com/Netw0rkNoob/VulnClaw): Pentest CLI agent that takes a target from recon through exploitation to a report.
- ![GitHub Repo stars](https://img.shields.io/github/stars/CyberStrikeus/CyberStrike?style=social) ![misused](https://img.shields.io/badge/misused-b91c1c?style=flat-square) [**CyberStrike**](https://github.com/CyberStrikeus/CyberStrike): Offensive-security harness for automated penetration testing.
- ![GitHub Repo stars](https://img.shields.io/github/stars/samugit83/redamon?style=social) [**RedAmon**](https://github.com/samugit83/redamon): Maps an attack surface into a graph and exploits it from a Kali sandbox behind approval gates.
- ![GitHub Repo stars](https://img.shields.io/github/stars/GH05TCREW/pentestagent?style=social) [**PentestAgent**](https://github.com/GH05TCREW/pentestagent): Agent framework for black-box bug bounty, red team, and pentest work.
- ![GitHub Repo stars](https://img.shields.io/github/stars/Armur-Ai/Pentest-Swarm-AI?style=social) [**Pentest-Swarm-AI**](https://github.com/Armur-Ai/Pentest-Swarm-AI): Go-native agents to autonomously perform full-cycle pentests.
- ![GitHub Repo stars](https://img.shields.io/github/stars/N1nEmAn/sapper-v2?style=social) [**sapper**](https://github.com/N1nEmAn/sapper-v2): Multi-agent pentest orchestration harness.
- ![GitHub Repo stars](https://img.shields.io/github/stars/zakirkun/deep-eye?style=social) [**Deep Eye**](https://github.com/zakirkun/deep-eye): Pentest tool that has LLMs generate payloads and scan targets.
- ![GitHub Repo stars](https://img.shields.io/github/stars/0xSteph/pentest-ai?style=social) [**pentest-ai**](https://github.com/0xSteph/pentest-ai): AI pentester that re-runs each exploit to prove the finding.
- ![GitHub Repo stars](https://img.shields.io/github/stars/bugbasesecurity/pentest-copilot?style=social) [**Pentest-Copilot**](https://github.com/bugbasesecurity/pentest-copilot): Browser-based AI assistant for pentest and bug bounty work.
- ![GitHub Repo stars](https://img.shields.io/github/stars/JoasASantos/NeuroSploit?style=social) [**NeuroSploit**](https://github.com/JoasASantos/NeuroSploit): AI-powered penetration testing framework.
- ![GitHub Repo stars](https://img.shields.io/github/stars/SanMuzZzZz/LuaN1aoAgent?style=social) [**LuaN1aoAgent**](https://github.com/SanMuzZzZz/LuaN1aoAgent): Autonomous pentest agent built on graph-based reasoning.
- ![GitHub Repo stars](https://img.shields.io/github/stars/PentesterFlow/agent?style=social) [**PentesterFlow**](https://github.com/PentesterFlow/agent): Terminal pentest agent with skills, a Burp bridge, and analyst control.
- ![GitHub Repo stars](https://img.shields.io/github/stars/xalgorix/xalgorix?style=social) [**Xalgorix**](https://github.com/xalgorix/xalgorix): Autonomous pentest agent for reconnaissance, vulnerability detection, and exploitation.
- ![GitHub Repo stars](https://img.shields.io/github/stars/ipa-lab/hackingBuddyGPT?style=social) [**hackingBuddyGPT**](https://github.com/ipa-lab/hackingBuddyGPT): Research framework for building LLM hacking agents.
- ![GitHub Repo stars](https://img.shields.io/github/stars/ASCIT31/Dark-Moon?style=social) [**Darkmoon**](https://github.com/ASCIT31/Dark-Moon): Autonomous AI pentest platform with per-tech sub-agents and an evidence trail per finding.
- ![GitHub Repo stars](https://img.shields.io/github/stars/s0ld13rr/pentestcode?style=social) [**PentestCode**](https://github.com/s0ld13rr/pentestcode): Multi-agent pentest system that keeps engagement state between runs.
- ![GitHub Repo stars](https://img.shields.io/github/stars/berylliumsec/nebula?style=social) [**Nebula**](https://github.com/berylliumsec/nebula): Operator pentest harness with skills, Kali tools, approvals, and an assistant.
- ![GitHub Repo stars](https://img.shields.io/github/stars/vigolium/vigolium?style=social) [**Vigolium**](https://github.com/vigolium/vigolium): Vulnerability scanner whose agent swarm picks modules and writes attack extensions.
- ![GitHub Repo stars](https://img.shields.io/github/stars/pikpikcu/airecon?style=social) [**AIRecon**](https://github.com/pikpikcu/airecon): Autonomous security agent built on a self-hosted LLM.
- ![GitHub Repo stars](https://img.shields.io/github/stars/Lazarus-ai-OSS/clearwing?style=social) [**Clearwing**](https://github.com/Lazarus-ai-OSS/clearwing): Autonomous scanner that runs Kali tools and builds exploits with human approval.
- ![GitHub Repo stars](https://img.shields.io/github/stars/Zyrexnn/Cybermes?style=social) [**Cybermes**](https://github.com/Zyrexnn/Cybermes): Bug-bounty agent framework built on Hermes Agent.
- ![GitHub Repo stars](https://img.shields.io/github/stars/cdxiaodong/cain-agent?style=social) [**Cain**](https://github.com/cdxiaodong/cain-agent): AI pentest agent with a cloud module for authorized assessments.
- ![GitHub Repo stars](https://img.shields.io/github/stars/R-s0n/ars0n-framework-v2?style=social) [**Ars0n Framework v2**](https://github.com/R-s0n/ars0n-framework-v2): Bug bounty recon framework that exposes scans to AI assistants over MCP.
- ![GitHub Repo stars](https://img.shields.io/github/stars/AntiFox-AI/antifox?style=social) ![misused](https://img.shields.io/badge/misused-b91c1c?style=flat-square) [**AntiFox**](https://github.com/AntiFox-AI/antifox): Agentic pentest platform derived from ARTEX.
- ![GitHub Repo stars](https://img.shields.io/github/stars/FrancescoStabile/numasec?style=social) [**numasec**](https://github.com/FrancescoStabile/numasec): AI agent for cybersecurity work.
- ![GitHub Repo stars](https://img.shields.io/github/stars/asaotomo/FofaMap?style=social) [**FofaMap**](https://github.com/asaotomo/FofaMap): Ties FOFA asset discovery to Nuclei validation in one workflow.
- ![GitHub Repo stars](https://img.shields.io/github/stars/Yean-Sec/StrikeAgent_AtkBrain-Flash?style=social) [**StrikeAgent**](https://github.com/Yean-Sec/StrikeAgent_AtkBrain-Flash): AI pentest platform that re-rates and re-verifies findings.
- ![GitHub Repo stars](https://img.shields.io/github/stars/FishCodeTech/muteki?style=social) [**Muteki**](https://github.com/FishCodeTech/muteki): Offensive-security harness for automated penetration testing.
- ![GitHub Repo stars](https://img.shields.io/github/stars/ARCANGEL0/Mitsu?style=social) [**Mitsu**](https://github.com/ARCANGEL0/Mitsu): Pentest agent that runs an authorized engagement from recon through post-exploitation.
- ![GitHub Repo stars](https://img.shields.io/github/stars/adshao/flounder?style=social) [**Flounder**](https://github.com/adshao/flounder): Turns coding agents into a bug-bounty auditor that builds exploits locally.
- ![GitHub Repo stars](https://img.shields.io/github/stars/Vasco0x4/AIDA?style=social) [**AIDA**](https://github.com/Vasco0x4/AIDA): Turns an LLM into an autonomous pentester inside a scope you set.
- ![GitHub Repo stars](https://img.shields.io/github/stars/SHAdd0WTAka/Zen-Ai-Pentest?style=social) [**Zen-Ai-Pentest**](https://github.com/SHAdd0WTAka/Zen-Ai-Pentest): Multi-agent pentest framework with automated vulnerability scanning.
- ![GitHub Repo stars](https://img.shields.io/github/stars/chu0119/Pojun?style=social) [**Pojun**](https://github.com/chu0119/Pojun): Multi-agent platform that takes a one-line goal from recon through to a report.
- ![GitHub Repo stars](https://img.shields.io/github/stars/faizann24/rogue?style=social) [**Rogue**](https://github.com/faizann24/rogue): LLM web vulnerability scanner that generates payloads and verifies findings.
- ![GitHub Repo stars](https://img.shields.io/github/stars/capture0x/AdStrike?style=social) [**AdStrike**](https://github.com/capture0x/AdStrike): Active Directory attack framework an LLM drives over MCP.
- ![GitHub Repo stars](https://img.shields.io/github/stars/S1N6H/pentest-harness?style=social) [**Pentest Harness**](https://github.com/S1N6H/pentest-harness): Self-hosted agent harness for authorized pentests, bug bounty, and labs.
- ![GitHub Repo stars](https://img.shields.io/github/stars/chainreactors/cyber-harness?style=social) [**cyber-harness**](https://github.com/chainreactors/cyber-harness): Single-binary agent for pentest, red team, and bug bounty.
- ![GitHub Repo stars](https://img.shields.io/github/stars/martian56/redcell?style=social) [**RedCell**](https://github.com/martian56/redcell): Agents that run a penetration test end to end inside a Kali container.
- ![GitHub Repo stars](https://img.shields.io/github/stars/ok-helloworld/vibe-pentest?style=social) [**Vibe Pentest**](https://github.com/ok-helloworld/vibe-pentest): Multi-agent black-box pentest tool, including business-logic flaws.
- ![GitHub Repo stars](https://img.shields.io/github/stars/vectra-ai-research/Halberd?style=social) [**Halberd**](https://github.com/vectra-ai-research/Halberd): Multi-cloud attack emulation with a Claude agent that finds and runs attack paths.
- ![GitHub Repo stars](https://img.shields.io/github/stars/BugTraceAI/BugTraceAI?style=social) [**BugTraceAI**](https://github.com/BugTraceAI/BugTraceAI): Self-hosted agentic web pentest suite with scanning, API testing, and MCP.
- ![GitHub Repo stars](https://img.shields.io/github/stars/kpolley/redai?style=social) [**RedAI**](https://github.com/kpolley/redai): Terminal workbench that finds vulnerabilities and validates them with PoC scripts.
- ![GitHub Repo stars](https://img.shields.io/github/stars/yee-yore/DorkAgent?style=social) [**DorkAgent**](https://github.com/yee-yore/DorkAgent): LLM agent that automates Google dorking for bug hunting and pentesting.
- ![GitHub Repo stars](https://img.shields.io/github/stars/straylabs-ai/deadend-cli?style=social) [**deadend-cli**](https://github.com/straylabs-ai/deadend-cli): Self-hosted agentic tooling for black-box pentests.
- ![GitHub Repo stars](https://img.shields.io/github/stars/pensarai/apex?style=social) [**Apex**](https://github.com/pensarai/apex): Terminal pentest agent for black-box and white-box tests in a Kali container.
- ![GitHub Repo stars](https://img.shields.io/github/stars/OTT-Cybersecurity-LLC/lyrie-ai?style=social) [**Lyrie**](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai): Pentest CLI that fingerprints targets, validates exploits, and red-teams LLM endpoints.
- ![GitHub Repo stars](https://img.shields.io/github/stars/aielte-research/HackSynth?style=social) [**HackSynth**](https://github.com/aielte-research/HackSynth): LLM agent and evaluation framework for autonomous penetration testing.
- ![GitHub Repo stars](https://img.shields.io/github/stars/irraz/vulnerator-ai?style=social) [**vulnerator-ai**](https://github.com/irraz/vulnerator-ai): Pentest agent on Hermes that drives Kali and browser tools over MCP.
- ![GitHub Repo stars](https://img.shields.io/github/stars/ZacharyZcR/SecGPT?style=social) [**SecGPT**](https://github.com/ZacharyZcR/SecGPT): AutoGPT-style tool for pentesting, vulnerability scanning, and code audit.
- ![GitHub Repo stars](https://img.shields.io/github/stars/yohannesgk/blacksmith?style=social) [**BlacksmithAI**](https://github.com/yohannesgk/blacksmith): Multi-agent pentest framework with recon, exploit, and post-exploit agents.
- ![GitHub Repo stars](https://img.shields.io/github/stars/haiou-666/Haiou-workshop?style=social) [**Haiou Workshop**](https://github.com/haiou-666/Haiou-workshop): AI workbench for reverse engineering, authorized pentests, and CTF.
- ![GitHub Repo stars](https://img.shields.io/github/stars/KHenryAegis/VulnBot?style=social) [**VulnBot**](https://github.com/KHenryAegis/VulnBot): Multi-agent framework for autonomous penetration testing.
- ![GitHub Repo stars](https://img.shields.io/github/stars/fzn0x/watchtower?style=social) [**Watchtower**](https://github.com/fzn0x/watchtower): Pentest CLI where LLM agents orchestrate security tools.
- ![GitHub Repo stars](https://img.shields.io/github/stars/KKingZero/Zypheron-CLI?style=social) [**Zypheron**](https://github.com/KKingZero/Zypheron-CLI): Local-first security CLI for recon, scanning, and operator workflows.
- ![GitHub Repo stars](https://img.shields.io/github/stars/antoninoLorenzo/AI-OPS?style=social) [**AI-OPS**](https://github.com/antoninoLorenzo/AI-OPS): Penetration testing assistant built on open-source LLMs.
- ![GitHub Repo stars](https://img.shields.io/github/stars/0x0pointer/agent-smith?style=social) [**agent-smith**](https://github.com/0x0pointer/agent-smith): Pentest framework where skills teach the LLM a methodology.
- ![GitHub Repo stars](https://img.shields.io/github/stars/andreashappe/cochise?style=social) [**cochise**](https://github.com/andreashappe/cochise): Autonomous assumed-breach penetration testing of Active Directory.
- ![GitHub Repo stars](https://img.shields.io/github/stars/dbx0/executioner?style=social) [**Executioner**](https://github.com/dbx0/executioner): Local workspace where AI agent teams run an assessment in your scope.
- ![GitHub Repo stars](https://img.shields.io/github/stars/cylabcyberautonomy/Incalmo?style=social) [**Incalmo**](https://github.com/cylabcyberautonomy/Incalmo): LLM-driven network pentest tool for multistage attacks.
- ![GitHub Repo stars](https://img.shields.io/github/stars/Stickman230/claude-pentest?style=social) [**claude-pentest**](https://github.com/Stickman230/claude-pentest): Claude Code plugin that runs pentest engagements through Kali over MCP.
- ![GitHub Repo stars](https://img.shields.io/github/stars/webxos/phalanx?style=social) [**Phalanx**](https://github.com/webxos/phalanx): Multi-agent pentest framework with recon, exploit, and post-exploit agents.
- ![GitHub Repo stars](https://img.shields.io/github/stars/nbshenxm/pentest-agent?style=social) [**PentestAgent (nbshenxm)**](https://github.com/nbshenxm/pentest-agent): Research framework that automates recon, vulnerability analysis, and exploitation.
- ![GitHub Repo stars](https://img.shields.io/github/stars/InfSecLabs/PentestAssistant?style=social) [**PentestAssistant**](https://github.com/InfSecLabs/PentestAssistant): LLM web pentest assistant that runs nmap and sqlmap through tool calls.
- ![GitHub Repo stars](https://img.shields.io/github/stars/arthurgervais/mapta?style=social) [**MAPTA**](https://github.com/arthurgervais/mapta): Multi-agent system for autonomous web security assessment with exploit validation.
- ![GitHub Repo stars](https://img.shields.io/github/stars/matank001/Moxy?style=social) [**Moxy**](https://github.com/matank001/Moxy): Intercepting-proxy DAST tool where an AI agent edits traffic and drives a browser.
- ![GitHub Repo stars](https://img.shields.io/github/stars/lordx64/pentestkit?style=social) [**pentestkit**](https://github.com/lordx64/pentestkit): Multi-agent pentest framework where a verifier tries to exploit each candidate.
- ![GitHub Repo stars](https://img.shields.io/github/stars/ABSllk/Hexestra?style=social) [**Hexestra**](https://github.com/ABSllk/Hexestra): Pentest workbench where a coding agent drives the browser, shell, and traffic.
- ![GitHub Repo stars](https://img.shields.io/github/stars/ZackSecurity/Zack-AI-Scanner?style=social) [**Zack AI Scanner**](https://github.com/ZackSecurity/Zack-AI-Scanner): Burp extension that runs an LLM against one request and sends the payloads.
- ![GitHub Repo stars](https://img.shields.io/github/stars/sergio11/zero_trace_hacking_tool?style=social) [**ZeroTrace**](https://github.com/sergio11/zero_trace_hacking_tool): AI dorking tool for reconnaissance.
- ![GitHub Repo stars](https://img.shields.io/github/stars/YasodGinige/AutoPentester?style=social) [**AutoPentester**](https://github.com/YasodGinige/AutoPentester): LLM agent framework for automated penetration testing.
- ![GitHub Repo stars](https://img.shields.io/github/stars/nishu2402/HEAVEN-Autonomous-Penetration-Testing?style=social) [**HEAVEN**](https://github.com/nishu2402/HEAVEN-Autonomous-Penetration-Testing): Autonomous pentest framework with a plan-act loop and a post-exploitation playbook.
- ![GitHub Repo stars](https://img.shields.io/github/stars/drcrypterdotru/sqlmap-skynet?style=social) [**SQLMap Skynet**](https://github.com/drcrypterdotru/sqlmap-skynet): AI-assisted SQLMap orchestration with an MCP server for agents.
- ![GitHub Repo stars](https://img.shields.io/github/stars/dreadnode/ares?style=social) [**Ares**](https://github.com/dreadnode/ares): LLM-coordinated red-team platform that chains Active Directory attack tools.
- ![GitHub Repo stars](https://img.shields.io/github/stars/prutxvi/cybersentry?style=social) [**CyberSentry**](https://github.com/prutxvi/cybersentry): Autonomous agent for website penetration testing.
- ![GitHub Repo stars](https://img.shields.io/github/stars/vmihalis/hacker-bob?style=social) [**Hacker Bob**](https://github.com/vmihalis/hacker-bob): Autonomous bug bounty hunter on a local MCP runtime.
- ![GitHub Repo stars](https://img.shields.io/github/stars/snow10100/pena?style=social) [**BreachSeek - PENA**](https://github.com/snow10100/pena): Multi-agent system that automates penetration testing.

---

### 🔎 Agentic Code Auditors

- ![GitHub Repo stars](https://img.shields.io/github/stars/vercel-labs/deepsec?style=social) [**deepsec**](https://github.com/vercel-labs/deepsec): Security harness for codebase vulnerability scanning with coding agents.
- ![GitHub Repo stars](https://img.shields.io/github/stars/lintsinghua/DeepAudit?style=social) ![misused](https://img.shields.io/badge/misused-b91c1c?style=flat-square) [**DeepAudit**](https://github.com/lintsinghua/DeepAudit): Multi-agent source-code auditor with Docker sandbox exploit validation.
- ![GitHub Repo stars](https://img.shields.io/github/stars/gadievron/raptor?style=social) [**Raptor**](https://github.com/gadievron/raptor): Claude Code agent for offensive and defensive security research.
- ![GitHub Repo stars](https://img.shields.io/github/stars/protectai/vulnhuntr?style=social) [**Vulnhuntr**](https://github.com/protectai/vulnhuntr): LLM vulnerability discovery that traces code paths to remotely exploitable bugs.
- ![GitHub Repo stars](https://img.shields.io/github/stars/Kritt-ai/open-kritt?style=social) [**Open Kritt**](https://github.com/Kritt-ai/open-kritt): Self-hosted platform where AI agents find and validate vulnerabilities in code.
- ![GitHub Repo stars](https://img.shields.io/github/stars/larlarua/AutoCVE?style=social) [**AutoCVE**](https://github.com/larlarua/AutoCVE): Multi-agent platform for vulnerability detection, verification, and reporting.
- ![GitHub Repo stars](https://img.shields.io/github/stars/capitalone/VulnHunter?style=social) [**VulnHunter**](https://github.com/capitalone/VulnHunter): Source-code hunter that drops findings it cannot prove exploitable.
- ![GitHub Repo stars](https://img.shields.io/github/stars/evilsocket/audit?style=social) [**audit**](https://github.com/evilsocket/audit): Claude agent pipeline that hunts vulnerabilities and writes proof-of-concept code.
- ![GitHub Repo stars](https://img.shields.io/github/stars/knostic/OpenAnt?style=social) [**OpenAnt**](https://github.com/knostic/OpenAnt): LLM-powered vulnerability discovery with a second adversarial verification stage.
- ![GitHub Repo stars](https://img.shields.io/github/stars/deonmenezes/mantishack?style=social) [**Mantishack**](https://github.com/deonmenezes/mantishack): Vulnerability pipeline that validates findings by simulating an attacker on the code.
- ![GitHub Repo stars](https://img.shields.io/github/stars/openhackai/OpenHack?style=social) [**OpenHack**](https://github.com/openhackai/OpenHack): Agent scanner that hunts and exploit-tests vulnerabilities in a codebase.
- ![GitHub Repo stars](https://img.shields.io/github/stars/PlamenTSV/plamen?style=social) [**Plamen**](https://github.com/PlamenTSV/plamen): Agent swarm that audits smart contracts and node clients with PoC exploits.
- ![GitHub Repo stars](https://img.shields.io/github/stars/dinosn/raptor-loop-hunt?style=social) [**raptor-loop-hunt**](https://github.com/dinosn/raptor-loop-hunt): Claude Code skill that loops a vulnerability hunt over a codebase.
- ![GitHub Repo stars](https://img.shields.io/github/stars/m4xxxxx/AIxVuln?style=social) [**AIxVuln**](https://github.com/m4xxxxx/AIxVuln): Multi-agent system that audits code and verifies findings with sandboxed PoCs.
- ![GitHub Repo stars](https://img.shields.io/github/stars/fuzzingbrain/afc-crs-all-you-need-is-a-fuzzing-brain?style=social) [**FuzzingBrain**](https://github.com/fuzzingbrain/afc-crs-all-you-need-is-a-fuzzing-brain): LLM system on OSS-Fuzz that finds vulnerabilities and builds proof-of-concept inputs.

---

### 🎯 Offensive Agent Skills

- ![GitHub Repo stars](https://img.shields.io/github/stars/zhaoxuya520/reverse-skill?style=social) [**reverse-skill**](https://github.com/zhaoxuya520/reverse-skill): Skill router that sends coding agents to reverse-engineering, pentest, and CTF tools.
- ![GitHub Repo stars](https://img.shields.io/github/stars/elementalsouls/Claude-BugHunter?style=social) [**Claude-BugHunter**](https://github.com/elementalsouls/Claude-BugHunter): Claude Code skill bundle for bug hunting and external red-team work.
- ![GitHub Repo stars](https://img.shields.io/github/stars/SnailSploit/Claude-Red?style=social) [**Claude-Red**](https://github.com/SnailSploit/Claude-Red): Offensive-security skill library that primes Claude for specific attack surfaces.
- ![GitHub Repo stars](https://img.shields.io/github/stars/ljagiello/ctf-skills?style=social) [**ctf-skills**](https://github.com/ljagiello/ctf-skills): Agent skills for CTF challenges across web, pwn, crypto, reversing, and forensics.
- ![GitHub Repo stars](https://img.shields.io/github/stars/elementalsouls/Claude-OSINT?style=social) [**Claude-OSINT**](https://github.com/elementalsouls/Claude-OSINT): Claude skills that prime the model for offensive recon and exposure checks.
- ![GitHub Repo stars](https://img.shields.io/github/stars/yaklang/hack-skills?style=social) [**hack-skills**](https://github.com/yaklang/hack-skills): Hacking skill library agents load for web, Active Directory, pwn, and mobile.
- ![GitHub Repo stars](https://img.shields.io/github/stars/0xSteph/pentest-ai-agents?style=social) [**pentest-ai-agents**](https://github.com/0xSteph/pentest-ai-agents): Offensive-security subagents for Claude Code.
- ![GitHub Repo stars](https://img.shields.io/github/stars/uphiago/recon-skills?style=social) [**recon-skills**](https://github.com/uphiago/recon-skills): Agent skills for external recon, web and API testing, and attack paths.
- ![GitHub Repo stars](https://img.shields.io/github/stars/SeaOf0/dsh-redteam-model?style=social) [**dsh-redteam-model**](https://github.com/SeaOf0/dsh-redteam-model): Red-team working modes and runtime plugins for the DeepSeek harness.
- ![GitHub Repo stars](https://img.shields.io/github/stars/BrownFineSecurity/iothackbot?style=social) [**IoTHackBot**](https://github.com/BrownFineSecurity/iothackbot): IoT security toolkit with Claude Code skills for vulnerability discovery.
- ![GitHub Repo stars](https://img.shields.io/github/stars/transilienceai/communitytools?style=social) [**communitytools**](https://github.com/transilienceai/communitytools): Claude Code skills, agents, and commands for pentesting and bug bounty.
- ![GitHub Repo stars](https://img.shields.io/github/stars/matty69v/Bug-Bounty-Agents?style=social) [**Bug-Bounty-Agents**](https://github.com/matty69v/Bug-Bounty-Agents): Drop-in agent personas for bug bounty recon, hunting, and PoC validation.
- ![GitHub Repo stars](https://img.shields.io/github/stars/hypnguyen1209/offensive-claude?style=social) [**offensive-claude**](https://github.com/hypnguyen1209/offensive-claude): Offensive framework for Claude Code covering the kill chain.
- ![GitHub Repo stars](https://img.shields.io/github/stars/crazyMarky/pentest-skills?style=social) [**pentest-skills**](https://github.com/crazyMarky/pentest-skills): Pentest skills for Claude Code and Gemini CLI that turn requests into tool runs.
- ![GitHub Repo stars](https://img.shields.io/github/stars/ADScanPro/Claude-AD?style=social) [**Claude-AD**](https://github.com/ADScanPro/Claude-AD): Active Directory pentest playbook for Claude Code.
- ![GitHub Repo stars](https://img.shields.io/github/stars/awarexone/web3-bug-bounty-hunting-ai-skills?style=social) [**web3-bug-bounty-hunting-ai-skills**](https://github.com/awarexone/web3-bug-bounty-hunting-ai-skills): Claude Code skills for smart-contract bug bounty hunting.
- ![GitHub Repo stars](https://img.shields.io/github/stars/x-glacier/kali-pentest?style=social) [**kali-pentest**](https://github.com/x-glacier/kali-pentest): Kali pentest skill for Claude Code, OpenClaw, and Hermes Agent.
- ![GitHub Repo stars](https://img.shields.io/github/stars/zhaji2333/CkSKILLS?style=social) [**CkSKILLS**](https://github.com/zhaji2333/CkSKILLS): Skill library that turns researcher methodology into reusable bug-hunting skills.
- ![GitHub Repo stars](https://img.shields.io/github/stars/forefy/.context?style=social) [**forefy context**](https://github.com/forefy/.context): Agent skills for security audits, pentests, and bug bounty work.
- ![GitHub Repo stars](https://img.shields.io/github/stars/Prohao42/aimy-skill?style=social) [**aimy-skill**](https://github.com/Prohao42/aimy-skill): Pentest skill for AI agents with an exploit-chain check flow.
- ![GitHub Repo stars](https://img.shields.io/github/stars/hassan-algo/open-sesame?style=social) [**open-sesame**](https://github.com/hassan-algo/open-sesame): Claude Code pentest skills for web and network engagements.

---

### 🔌 Offensive MCP Bridges

- ![GitHub Repo stars](https://img.shields.io/github/stars/six2dez/burp-ai-agent?style=social) [**Burp AI Agent**](https://github.com/six2dez/burp-ai-agent): Burp Suite extension that adds AI scanners and an MCP bridge for agents.
- ![GitHub Repo stars](https://img.shields.io/github/stars/Wh0am123/MCP-Kali-Server?style=social) [**MCP-Kali-Server**](https://github.com/Wh0am123/MCP-Kali-Server): MCP server that gives an AI agent a Kali Linux machine and its tools.
- ![GitHub Repo stars](https://img.shields.io/github/stars/GH05TCREW/MetasploitMCP?style=social) [**MetasploitMCP**](https://github.com/GH05TCREW/MetasploitMCP): MCP server that lets an agent drive Metasploit.
- ![GitHub Repo stars](https://img.shields.io/github/stars/shinthink/blitzstrike?style=social) [**Blitz Strike**](https://github.com/shinthink/blitzstrike): MCP toolbelt that maps attack surface and verifies findings on a live target.
- ![GitHub Repo stars](https://img.shields.io/github/stars/PatrikFehrenbach/h1-brain?style=social) [**h1-brain**](https://github.com/PatrikFehrenbach/h1-brain): MCP server that links an assistant to HackerOne scopes and reports.
- ![GitHub Repo stars](https://img.shields.io/github/stars/Cy-S3c/BurpMCP-Ultra?style=social) [**BurpMCP-Ultra**](https://github.com/Cy-S3c/BurpMCP-Ultra): MCP server that gives AI agents Burp Suite tools for scanning and fuzzing.
- ![GitHub Repo stars](https://img.shields.io/github/stars/sspsec/Scan-Spring-GO?style=social) [**Scan-Spring-GO**](https://github.com/sspsec/Scan-Spring-GO): Spring scanner that exposes its modules to AI clients over MCP.
- ![GitHub Repo stars](https://img.shields.io/github/stars/bhavsec/autopentest-ai?style=social) [**AutoPentest AI**](https://github.com/bhavsec/autopentest-ai): MCP server whose agents run web pentests.
- ![GitHub Repo stars](https://img.shields.io/github/stars/DMontgomery40/pentest-mcp?style=social) [**Pentest MCP**](https://github.com/DMontgomery40/pentest-mcp): MCP server that gives assessment agents nmap, Nuclei, and related tools.
- ![GitHub Repo stars](https://img.shields.io/github/stars/mwnickerson/bloodhound_mcp?style=social) [**bloodhound_mcp**](https://github.com/mwnickerson/bloodhound_mcp): MCP server that lets an LLM query BloodHound attack paths.
- ![GitHub Repo stars](https://img.shields.io/github/stars/hahwul/gori?style=social) [**gori**](https://github.com/hahwul/gori): Intercepting proxy whose MCP server lets AI agents drive the engagement.
- ![GitHub Repo stars](https://img.shields.io/github/stars/ccq1/awsome_kali_MCPServers?style=social) [**awsome-kali-MCPServers**](https://github.com/ccq1/awsome_kali_MCPServers): MCP servers that expose Kali Linux tools to AI clients.

---

### 🛡️ Defensive & Guardrail Tools

- ![GitHub Repo stars](https://img.shields.io/github/stars/maximhq/bifrost?style=social) [**Bifrost**](https://github.com/maximhq/bifrost): AI gateway with guardrails, rate limits, and access controls for governed model and MCP traffic
- ![GitHub Repo stars](https://img.shields.io/github/stars/guardrails-ai/guardrails?color=gold) [**Guardrails**](https://github.com/guardrails-ai/guardrails): Add structured validation and policy enforcement for LLMs
- ![GitHub stars](https://img.shields.io/github/stars/NVIDIA/NeMo-Guardrails?style=social) [**NeMo Guardrails**](https://github.com/NVIDIA-NeMo/Guardrails): Protects against jailbreak and hallucinations with customizable rulesets
- ![GitHub Repo stars](https://img.shields.io/github/stars/facebookresearch/PurpleLlama?style=social) [**PurpleLlama**](https://github.com/facebookresearch/PurpleLlama): Tools to assess and improve LLM security from META
- ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/PyRIT?style=social) [**PyRIT**](https://github.com/microsoft/PyRIT): Python Risk Identification Tool for generative AI
- ![GitHub stars](https://img.shields.io/github/stars/whylabs/langkit?style=social) [**LangKit**](https://github.com/whylabs/langkit): Functions for jailbreak detection, prompt injection, and sensitive information detection
- ![GitHub Repo stars](https://img.shields.io/github/stars/tldrsec/prompt-injection-defenses?style=social) [**Prompt Injection Defenses**](https://github.com/tldrsec/prompt-injection-defenses): Practical and proposed defenses against prompt injection
- ![GitHub Repo stars](https://img.shields.io/github/stars/secureagentics/Adrian?style=social) [**Adrian**](https://github.com/secureagentics/Adrian): Runtime security for AI agents detecting and blocking prompt injection, malicious tool use, and out-of-remit actions
- ![GitHub Repo stars](https://img.shields.io/github/stars/hashgraph-online/hol-guard?style=social) [**HOL Guard**](https://github.com/hashgraph-online/hol-guard): Local-first agent security layer intercepting tool calls and scanning MCP, skills, and plugins
- ![GitHub Repo stars](https://img.shields.io/github/stars/deadbits/vigil-llm?style=social) [**Vigil**](https://github.com/deadbits/vigil-llm): Prompt injection detection toolkit and REST API for LLM security risk scoring
- ![GitHub Repo stars](https://img.shields.io/github/stars/salemalem/npmscan-mcp-plugin?style=social) [**npmscan**](https://github.com/salemalem/npmscan-mcp-plugin): MCP server that checks npm packages for malware, vulnerabilities and maintainer takeovers before an agent installs them
- ![GitHub stars](https://img.shields.io/github/stars/invariantlabs-ai/invariant?style=social) [**Invariant**](https://github.com/invariantlabs-ai/invariant) Trace analysis tool for AI agents
- ![GitHub Repo stars](https://img.shields.io/github/stars/Agent-Threat-Rule/agent-threat-rules?style=social) [**Agent Threat Rules**](https://github.com/Agent-Threat-Rule/agent-threat-rules) Detection rule standard for AI threats (e.g., prompt injection and MCP attacks)
- ![GitHub Repo stars](https://img.shields.io/github/stars/future-agi/traceAI?style=social) [**TraceAI**](https://github.com/future-agi/traceAI): Tracing for LLM and agent apps
- ![GitHub stars](https://img.shields.io/github/stars/safellama/plexiglass?style=social) [**Plexiglass**](https://github.com/safellama/plexiglass): Security tool for LLM applications
- ![GitHub Repo stars](https://img.shields.io/github/stars/arekusandr/last_layer?style=social) [**Last Layer**](https://github.com/arekusandr/last_layer): Low-latency pre-filter for prompt injection prevention
- ![GitHub Repo stars](https://img.shields.io/github/stars/jnMetaCode/shellward?style=social) [**ShellWard**](https://github.com/jnMetaCode/shellward): AI Agent security middleware
- ![GitHub stars](https://img.shields.io/github/stars/KOKOSde/localmod?style=social) [**LocalMod**](https://github.com/KOKOSde/localmod): Self-hosted content moderation API with prompt injection detection, toxicity filtering, PII detection, and NSFW filtering
- ![GitHub Repo stars](https://img.shields.io/github/stars/future-agi/ai-evaluation?style=social) [**AI Evaluation**](https://github.com/future-agi/ai-evaluation): Guardrail scanners (jailbreak, PII, prompt-injection); AutoEval pipelines
- ![GitHub Repo stars](https://img.shields.io/github/stars/ArseniiBrazhnyk/Veritensor?style=social) [**Veritensor**](https://github.com/ArseniiBrazhnyk/Veritensor): AI model scanner to detect Pickle/PyTorch malware, check licenses, and verify HF hashes
- ![GitHub stars](https://img.shields.io/github/stars/killertcell428/aigis?style=social) [**Aigis**](https://github.com/killertcell428/aigis): Firewall for AI agents. OWASP LLM Top 10, RAG context filter, MCP 3-stage scanning
- [AIDEFEND](https://edward-playground.github.io/aidefense-framework/): Practical knowledge base for AI security defenses
- [OWASP Agent Memory Guard](https://github.com/OWASP/www-project-agent-memory-guard): Reference implementation for ASI06 (Memory Poisoning). Runtime defense for LLM agent memory.

---

### 🔐 Agent Authorization & Governance

- ![GitHub Repo stars](https://img.shields.io/github/stars/NVIDIA/OpenShell?style=social) [**OpenShell**](https://github.com/NVIDIA/OpenShell): Policy-enforced sandbox runtime for autonomous agents, isolating files, syscalls, network, and credentials
- ![GitHub Repo stars](https://img.shields.io/github/stars/speakeasy-api/gram?style=social) [**Gram**](https://github.com/speakeasy-api/gram): MCP control plane that enforces agent access policies and logs tool activity
- ![GitHub stars](https://img.shields.io/github/stars/tenuo-ai/tenuo?style=social) [**Tenuo**](https://github.com/tenuo-ai/tenuo): Capability-based authorization for AI agents
- ![GitHub Repo stars](https://img.shields.io/github/stars/lelu-ai/lelu?style=social) [**Lelu**](https://github.com/lelu-ai/lelu): Authorization engine gating agent tool calls on policy and prompt injection
- ![GitHub Repo stars](https://img.shields.io/github/stars/supernovae-st/nika?style=social) [**Nika**](https://github.com/supernovae-st/nika): Rust agent workflow runtime with default-deny permits, secret-flow analysis, and hash-chained traces
- [APort](https://aport.io/): Runtime policy and verification layer for AI agents and MCP-connected tools
- [Tuning Engines](https://www.tuningengines.com/): AI control and evidence layer for governed model, MCP, skill, and agent traffic with guardrails, policy decisions, approvals, traces, cost analytics
- [Penholder](https://penholder.ai/): Human-approval write-gate holding agent database writes pending until a human commits
- [**Speakeasy**](https://www.speakeasy.com/product/ai-control-plane): Enterprise AI control plane governing agent and MCP access with policy enforcement and auditability
- [**Alovia Watchdog**](https://aloviaai.com): Runtime allow/flag/block check of agent actions against a per-agent mission
- [**Praesidia**](https://praesidia.ai/): Tool permissions, approvals and signed decision records for agent and MCP calls routed through Praesidia
- [**Scalekit**](https://www.scalekit.com/): Per-user scoped OAuth and tool-level authorization for agents across 600+ apps, with audit logs of every call
- [**MAQPNA**](https://maqpna.com/): Self-hosted agent runtime: sandboxed sessions, default-deny tool policy, human approvals and a hash-chained audit log

---

## 🕵️ Benchmarks

- [**JailbreakBench**](https://jailbreakbench.github.io/): Evaluating and analyzing jailbreak methods for LLMs
- ![GitHub stars](https://img.shields.io/github/stars/elder-plinius/L1B3RT45?style=social) [**L1B3RT45**](https://github.com/elder-plinius/L1B3RT45/): AI jailbreaking tools
- ![GitHub stars](https://img.shields.io/github/stars/EasyJailbreak/EasyJailbreak?style=social) [**Easy Jailbreak**](https://github.com/EasyJailbreak/EasyJailbreak): Python framework to generate adversarial jailbreak prompts
- ![GitHub stars](https://img.shields.io/github/stars/EasyJailbreak/EasyJailbreak?style=social) [**PALLMs (Payloads for Attacking Large Language Models)**](https://github.com/mik0w/pallms)
- ![GitHub stars](https://img.shields.io/github/stars/pdparchitect/llm-hacking-database?style=social) [**LLM Hacking Database**](https://github.com/pdparchitect/llm-hacking-database): Attacks against LLMs
- [**Helium Model Worldview Benchmark**](https://huggingface.co/datasets/HeliumTrades/helium-model-worldview-benchmark): 304 paired cue-swap prompts measuring refusal and bias flip consistency across models
- [**Agentic AI Test Checklist 110**](https://huggingface.co/datasets/srinivaspadmanabhuni/agentic-ai-test-checklist-110): Manual test checklist for tool-using agents, including prompt-injection and OWASP agent-security cases

---

## 🧩 Threat Modeling

- [**ThreatModels**](https://github.com/jsotiro/ThreatModels/tree/main): Repository for LLM threat models
- [**Pangea Attack Taxonomy**](https://pangea.cloud/resources/taxonomy/): Comprehensive taxonomy of AI/LLM attacks and vulnerabilities
- [**AI Risk Taxonomy**](https://airisk.mit.edu/)
- [**AIR-Bench 2024**](https://crfm.stanford.edu/helm/air-bench/latest/)
- [**Offsec Harness Index**](https://offsecharnesses.ai/): Offensive AI harnesses named in vendor, CERT, and government reports, including general agents used in operations.

---

## 🧪 Playground

- [**Gandalf**](https://gandalf.lakera.ai/): Prompt injection wargame
- ![GitHub Repo stars](https://img.shields.io/github/stars/ReversecLabs/damn-vulnerable-llm-agent?style=social) [**Damn Vulnerable LLM Agent**](https://github.com/ReversecLabs/damn-vulnerable-llm-agent)
- ![GitHub Repo stars](https://img.shields.io/github/stars/CyberSunil/LLMVault?style=social) [**LLMVault**](https://github.com/CyberSunil/LLMVault): Hands-on OWASP LLM Top 10 training lab and CTF
- ![GitHub Repo stars](https://img.shields.io/github/stars/R3dShad0w7/PromptMe?style=social) [**PromptMe**](https://github.com/R3dShad0w7/PromptMe)
- ![GitHub Repo stars](https://img.shields.io/github/stars/OWASP/PwnzzAI?style=social) [**PwnzzAI**](https://github.com/OWASP/PwnzzAI) OWASP LLM ToP 10 vulnerabilities
- [**PromptTrace**](https://prompttrace.airedlab.com): Prompt injection and AI security 10 labs + 15-level CTF with real LLMs.
- [**AI RiskAtlas**](https://riskatlas.principle.sg): Interactive LLM and agent security lab with incident cases and attack simulations
- [**RansomLeak AI Security**](https://ransomleak.com/exercises/clawdbot-prompt-injection/): Browser exercise on indirect prompt injection against an AI assistant

### 🚩 CTF Agents

- ![GitHub Repo stars](https://img.shields.io/github/stars/verialabs/ctf-agent?style=social) [**ctf-agent**](https://github.com/verialabs/ctf-agent): Multi-model swarm that solves CTF challenges.
- ![GitHub Repo stars](https://img.shields.io/github/stars/yhy0/CHYing-agent?style=social) [**CHYing-agent**](https://github.com/yhy0/CHYing-agent): CTF agent from Tencent Cloud AI pentest hackathons.
- ![GitHub Repo stars](https://img.shields.io/github/stars/0ca/BoxPwnr?style=social) [**BoxPwnr**](https://github.com/0ca/BoxPwnr): Benchmarks LLM agents on HackTheBox, PortSwigger, and other security labs.
- ![GitHub Repo stars](https://img.shields.io/github/stars/NYU-LLM-CTF/nyuctf_agents?style=social) [**NYU CTF agents**](https://github.com/NYU-LLM-CTF/nyuctf_agents): LLM agents that solve CTF challenges for the NYU CTF Bench.
- ![GitHub Repo stars](https://img.shields.io/github/stars/QiantangCredit/heimdall-agent?style=social) [**Heimdall**](https://github.com/QiantangCredit/heimdall-agent): Self-hosted AI solver for CTF and security labs.

---

## 🧪 PoC & Study Resources

- ![GitHub stars](https://img.shields.io/github/stars/RobustNLP/CipherChat?style=social) [CipherChat](https://github.com/RobustNLP/CipherChat): Secure communication tool for LLMs
- ![GitHub stars](https://img.shields.io/github/stars/LLM-Tuning-Safety/LLMs-Finetuning-Safety?style=social) [LLMs Finetuning Safety](https://github.com/LLM-Tuning-Safety/LLMs-Finetuning-Safety): Safety for fine-tuning LLMs
- ![GitHub stars](https://img.shields.io/github/stars/Unispac/Visual-Adversarial-Examples-Jailbreak-Large-Language-Models?style=social) [Visual Adversarial Examples](https://github.com/Unispac/Visual-Adversarial-Examples-Jailbreak-Large-Language-Models): Jailbreaking LLMs with visual adversarial examples
- ![GitHub stars](https://img.shields.io/github/stars/ThuCCSLab/FigStep?style=social) [FigStep](https://github.com/ThuCCSLab/FigStep): Jailbreaking vision-language models via typographic visual prompts
- ![GitHub stars](https://img.shields.io/github/stars/precize/OWASP-Agentic-AI?style=social) [OWASP Agentic AI](https://github.com/precize/OWASP-Agentic-AI/): OWASP Top 10 for Agentic AI
- ![GitHub Repo stars](https://img.shields.io/github/stars/Repello-AI/whistleblower?style=social) [WhistleBlower](https://github.com/Repello-AI/whistleblower): Infer the system prompt of an AI agent based on its generated text outputs.
- ![GitHub stars](https://img.shields.io/github/stars/BishopFox/BrokenHill?style=social) [BrokenHill](https://github.com/BishopFox/BrokenHill): Automated attack tool for GCG attack
- ![GitHub stars](https://img.shields.io/github/stars/XuandongZhao/weak-to-strong?style=social) [Weak-to-Strong Generalization](https://github.com/XuandongZhao/weak-to-strong): Eliciting strong capabilities with weak supervision
- ![GitHub stars](https://img.shields.io/github/stars/sail-sg/AnyDoor?style=social) [AnyDoor](https://github.com/sail-sg/AnyDoor): Arbitrary backdoor instances in LLMs
- ![GitHub stars](https://img.shields.io/github/stars/euanong/image-hijacks?style=social) [Image Hijacks](https://github.com/euanong/image-hijacks): Image-based hijacks of LLMs
- [**ATLAS**](https://doi.org/10.5281/zenodo.21428133): Forensic study of prompt-injection cascades across a four-agent enterprise workflow
- [**RELAY**](https://doi.org/10.5281/zenodo.21425933): Study of authority framing and laundered code in multi-agent CI/CD pipelines
- [**Agent Skill Security Scan**](https://upskill.coach/research/agent-skill-security): Study of 121 agent skill repos and MCP servers scanned for prompt injection, secret exfiltration, and vulnerable deps
- [**2026 Developer & AI Web App Surface Hygiene Benchmark**](https://zcoldwater.github.io/vibeshield-action/security-txt-sourcemap-benchmark-2026.html): Audit of 60 AI & dev web apps measuring RFC 9116 `security.txt` adoption, JS sourcemap leaks, and COOP headers

---

## 🎥 Courses

- [AI Security Explained](https://www.youtube.com/playlist?list=PLOspHqNVtKADin6JGozvzSvUQFTQRdum-): Short essential theoretical knowledge
- [AI Agents for Pentest](https://youtube.com/playlist?list=PLHSZe6NjhTwUa2jVwQgDM2BTyWVvbmAls): Using agents for penetration testing
- [Prompt Injection and Jailbreaking](https://www.youtube.com/playlist?list=PLHSZe6NjhTwW1jboW_ccfJpVTMJQvi1zW): Practical short lab studies
- [hego.red](https://hego.red/): Practical AI/LLM red teaming notes on prompt injection, jailbreaks, RAG poisoning, and agent attacks

---

## 🌟 Miscellaneous

- [**LLM Security startups**](https://github.com/rushout09/llm-security-startups)
- [**LLM Security Problems at DEFCON31 Quals**](https://github.com/Nautilus-Institute/quals-2023/tree/main/pawan_gupta): The world's top security competition
- [**0din GenAI Bug Bounty from Mozilla**](https://0din.ai): GenAI models threats (prompt injection, training data poisoning, DoS)
- [**Adversarial Prompting**](https://www.promptingguide.ai/risks/adversarial): Documentation
- [**OWASP Top 10 for LLMs**](https://owasp.org/www-project-top-10-for-large-language-model-applications/): Official list of key LLM risks including prompt injection

---

## 📰 Blogs and Social Media

- 🐦 X: [@llm_sec](https://twitter.com/llm_sec)
- 🐦 X: [@SanderSchullhoff](https://x.com/sanderschulhoff)
- 📝 Blog: [LLM Security](https://llmsecurity.net/) (by [@llm_sec](https://twitter.com/llm_sec))
- 📝 Blog: [Embrace The Red](https://embracethered.com/blog/index.html)
- 📝 Blog: [Simon Willison](https://simonwillison.net/)
- 📰 Newsletter: [AI safety takes](https://newsletter.danielpaleka.com/)
- 📰 Newsletter & Blog: [Hackstery](https://hackstery.com)

---

## 🙏 Acknowledgements

This repository is actively maintained as a fork of the original project. It includes pending contributions, removes broken links, and separates academic papers from other resources for better organization.

- Main list: projects with broader adoption (typically ≥50★)
- [Emerging Projects](emerging.md): early-stage projects under 50★
- [Unavailable Projects](deprecated.md): commercialized, disappeared, or inactive entries
- [Research Papers](papers.md)

Contributions are always welcome. Please read the [Contribution Guidelines](CONTRIBUTING.md) before contributing.

> **Alternative:** [Awesome LLMSecOps](https://github.com/wearetyomsmnv/Awesome-LLMSecOps)

---

## Star History

<a href="https://www.star-history.com/?type=date&repos=beyefendi%2Fawesome-llm-security">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=beyefendi/awesome-llm-security&type=date&theme=dark&legend=top-left&sealed_token=uTfMq1U6cETRU74gebK8lc5-05SMZuwz-WbI2QzakjB1rLIAXACgQsFdh2iN6zPfFX8ASKYRyBx5enu2RcTLas2SQNcAwOrH9-tCwYFk9j1g9ikW26p01ZnAZFQkEsUH55pke_Ap_Iso7-O83X-7gkBCnIb7NtO5Q-uc4GOm7tXk8GBfGR668AKDX2Up" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=beyefendi/awesome-llm-security&type=date&legend=top-left&sealed_token=uTfMq1U6cETRU74gebK8lc5-05SMZuwz-WbI2QzakjB1rLIAXACgQsFdh2iN6zPfFX8ASKYRyBx5enu2RcTLas2SQNcAwOrH9-tCwYFk9j1g9ikW26p01ZnAZFQkEsUH55pke_Ap_Iso7-O83X-7gkBCnIb7NtO5Q-uc4GOm7tXk8GBfGR668AKDX2Up" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=beyefendi/awesome-llm-security&type=date&legend=top-left&sealed_token=uTfMq1U6cETRU74gebK8lc5-05SMZuwz-WbI2QzakjB1rLIAXACgQsFdh2iN6zPfFX8ASKYRyBx5enu2RcTLas2SQNcAwOrH9-tCwYFk9j1g9ikW26p01ZnAZFQkEsUH55pke_Ap_Iso7-O83X-7gkBCnIb7NtO5Q-uc4GOm7tXk8GBfGR668AKDX2Up" />
 </picture>
</a>
