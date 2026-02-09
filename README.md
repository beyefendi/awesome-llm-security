
# 🤖 Awesome LLM Security [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of awesome tools, documents, and projects about LLM Security.

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

---

## 🛠️ Tools


### 🧰 Multi-Purpose Scanners & Tools

- [**promptfoo**](https://github.com/promptfoo/promptfoo): LLM red teaming and evaluation framework with adversarial attacks (jailbreaks, prompt injection, PAIR, tree-of-attacks). CI/CD integration. ![GitHub Repo stars](https://img.shields.io/github/stars/promptfoo/promptfoo?style=social)
- [**Garak**](https://github.com/leondz/garak/): LLM vulnerability scanner ![GitHub Repo stars](https://img.shields.io/github/stars/leondz/garak?style=social)
- [**AI-Infra-Guard**](https://github.com/Tencent/AI-Infra-Guard/): LLM vulnerability scanner with Web UI, REST APIs, and Docker-based deployment. ![GitHub Repo stars](https://img.shields.io/github/stars/Tencent/AI-Infra-Guard?color=gold)
- [**LLM Guard**](https://github.com/laiyer-ai/llm-guard): Security toolkit for LLM interactions ![GitHub Repo stars](https://img.shields.io/github/stars/laiyer-ai/llm-guard?style=social)
- [**Agentic Security**](https://github.com/msoedov/agentic_security): Security toolkit for AI agents ![GitHub stars](https://img.shields.io/github/stars/msoedov/agentic_security?style=social)
- [**DeepTeam**](https://github.com/confident-ai/deepteam): Modular LLM red teaming framework (prompt injection, hallucination, data leaks, jailbreaks). ![GitHub Repo stars](https://img.shields.io/github/stars/confident-ai/deepteam?style=social)
- [**LLaMator**](https://github.com/RomiconEZ/LLaMator): Framework for testing vulnerabilities of LLMs ![GitHub stars](https://img.shields.io/github/stars/RomiconEZ/LLaMator?style=social)
- [**Plexiglass**](https://github.com/kortex-labs/plexiglass): Security toolbox for testing and safeguarding LLMs ![GitHub Repo stars](https://img.shields.io/github/stars/kortex-labs/plexiglass?style=social)
- [**LLMmap**](https://github.com/pasquini-dario/LLMmap): Tool for mapping LLM vulnerabilities ![GitHub stars](https://img.shields.io/github/stars/pasquini-dario/LLMmap?style=social)

---

### 🤖 Agentic Scanners

- [**AgentBench**](https://github.com/THUDM/AgentBench): Benchmark to evaluate LLMs as agents ![GitHub stars](https://img.shields.io/github/stars/THUDM/AgentBench?style=social)
- [**Agentic Radar**](https://github.com/splx-ai/agentic-radar): Open-source CLI security scanner for agentic workflows. ![GitHub Repo stars](https://img.shields.io/github/stars/splx-ai/agentic-radar?style=social)
- [**MCP Scanner**](https://github.com/cisco-ai-defense/mcp-scanner) ![GitHub Repo stars](https://img.shields.io/github/stars/cisco-ai-defense/mcp-scanner?style=social)
- [**Awesome MCP Security**](https://github.com/Puliczek/awesome-mcp-security): Curated list of MCP security resources ![GitHub stars](https://img.shields.io/github/stars/Puliczek/awesome-mcp-security?style=social)
- [**MCP Shield**](https://github.com/riseandignite/mcp-shield) ![GitHub Repo stars](https://img.shields.io/github/stars/riseandignite/mcp-shield?style=social)
- [**Invariant**](https://github.com/invariantlabs-ai/invariant): Trace analysis tool for AI agents ![GitHub stars](https://img.shields.io/github/stars/invariantlabs-ai/invariant?style=social)
- [**MCP Safety Scanner**](https://github.com/johnhalloran321/mcpSafetyScanner) ![GitHub Repo stars](https://img.shields.io/github/stars/johnhalloran321/mcpSafetyScanner?style=social)
- [**Awesome LLM Agent Security**](https://github.com/wearetyomsmnv/Awesome-LLM-agent-Security): LLM agent security resources, attacks, vulnerabilities ![GitHub stars](https://img.shields.io/github/stars/wearetyomsmnv/Awesome-LLM-agent-Security?style=social)
- [**Tenuo**](https://github.com/tenuo-ai/tenuo): Capability-based authorization for AI agents ![GitHub stars](https://img.shields.io/github/stars/tenuo-ai/tenuo?style=social)
- [**Agent Security Scanner MCP**](https://github.com/sinewaveai/agent-security-scanner-mcp): MCP server for scanning code for SQL injection, XSS, secrets exposure, prompt injection, and AI-hallucinated package detection. ![GitHub Repo stars](https://img.shields.io/github/stars/sinewaveai/agent-security-scanner-mcp?style=social)

---

### 🧑‍💻 RAG Security

- [**PoisonedRAG**](https://github.com/sleeepeer/PoisonedRAG): Poisoned RAG systems ![GitHub stars](https://img.shields.io/github/stars/sleeepeer/PoisonedRAG?style=social)
- [RAG Attacks and Mitigations](https://github.com/wearetyomsmnv/Adversarial-AI---Attacks-Mitigations-and-Defense-Strategies/tree/main/ch15/RAG): RAG attacks, mitigations, and defense strategies
- [Awesome Jailbreak on LLMs - RAG Attacks](https://github.com/yueliu1999/Awesome-Jailbreak-on-LLMs?tab=readme-ov-file#attack-on-rag-based-llm): RAG-based LLM attack techniques

---

### 💣 Prompt Injection

- [**Jailbreak LLMs**](https://github.com/verazuo/jailbreak_llms): Real-world prompt jailbreak dataset (15k+ examples). ![GitHub Repo stars](https://img.shields.io/github/stars/verazuo/jailbreak_llms?color=gold)
- [**Awesome Jailbreak LLMs**](https://github.com/yueliu1999/Awesome-Jailbreak-on-LLMs): Collection of jailbreak techniques, datasets, and defenses. ![GitHub Repo stars](https://img.shields.io/github/stars/yueliu1999/Awesome-Jailbreak-on-LLMs?color=gold)
- [**Jailbreaking LLMs (PAIR)**](https://github.com/patrickrchao/JailbreakingLLMs): Black-box jailbreak generation via automatic prompt refinement. ![GitHub Repo stars](https://img.shields.io/github/stars/patrickrchao/JailbreakingLLMs?color=gold)
- [**Prompt Fuzzer**](https://github.com/prompt-security/ps-fuzz): Open-source tool to help you harden your GenAI applications. ![GitHub Repo stars](https://img.shields.io/github/stars/prompt-security/ps-fuzz?style=social)
- [**Open Prompt Injection**](https://github.com/liu00222/Open-Prompt-Injection): Tool to evaluate prompt injection attacks and defenses on benchmark datasets. ![GitHub Repo stars](https://img.shields.io/github/stars/liu00222/Open-Prompt-Injection?style=social)
- [**LLMFuzzer**](https://github.com/mnns/LLMFuzzer): Fuzzing framework for LLM prompt generation. ![GitHub Repo stars](https://img.shields.io/github/stars/mnns/LLMFuzzer?style=social)
- [**Spikee**](https://github.com/ReversecLabs/spikee): Prompt injection toolkit. ![GitHub Repo stars](https://img.shields.io/github/stars/ReversecLabs/spikee?color=gold)
- [**Jailbreak Evaluation**](https://github.com/controllability/jailbreak-evaluation): Python package for language model jailbreak evaluation. ![GitHub Repo stars](https://img.shields.io/github/stars/controllability/jailbreak-evaluation?style=social)

---

### 🛡️ Defensive & Guardrail Tools

- [**Guardrails**](https://github.com/guardrails-ai/guardrails): Add structured validation and policy enforcement for LLMs. ![GitHub Repo stars](https://img.shields.io/github/stars/guardrails-ai/guardrails?color=gold)
- [**NeMo Guardrails**](https://github.com/NVIDIA-NeMo/Guardrails): Tool that protects against jailbreak and hallucinations with customizable rulesets ![GitHub stars](https://img.shields.io/github/stars/NVIDIA/NeMo-Guardrails?style=social)
- [**PurpleLlama**](https://github.com/facebookresearch/PurpleLlama): Tools to assess and improve LLM security from META. ![GitHub Repo stars](https://img.shields.io/github/stars/facebookresearch/PurpleLlama?style=social)
- [**PyRIT**](https://github.com/Azure/PyRIT): Python Risk Identification Tool for generative AI ![GitHub stars](https://img.shields.io/github/stars/Azure/PyRIT?style=social)
- [**LLM-Guard**](https://github.com/protectai/llm-guard): Tool for securing LLM interactions (replaced rebuff) ![GitHub stars](https://img.shields.io/github/stars/protectai/llm-guard?style=social)
- [**LangKit**](https://github.com/whylabs/langkit): Functions for jailbreak detection, prompt injection, and sensitive information detection ![GitHub stars](https://img.shields.io/github/stars/whylabs/langkit?style=social)
- [**Prompt Injection Defenses**](https://github.com/tldrsec/prompt-injection-defenses): Practical and proposed defenses against prompt injection. ![GitHub Repo stars](https://img.shields.io/github/stars/tldrsec/prompt-injection-defenses?style=social)
- [**Vigil**](https://github.com/deadbits/vigil-llm): Prompt injection detection toolkit and REST API for LLM security risk scoring. ![GitHub Repo stars](https://img.shields.io/github/stars/deadbits/vigil-llm?style=social)
- [**Plexiglass**](https://github.com/safellama/plexiglass): Security tool for LLM applications ![GitHub stars](https://img.shields.io/github/stars/safellama/plexiglass?style=social)
- [**Last Layer**](https://github.com/arekusandr/last_layer): Low-latency pre-filter for prompt injection prevention. ![GitHub Repo stars](https://img.shields.io/github/stars/arekusandr/last_layer?style=social)
- [**Veritensor**](https://github.com/ArseniiBrazhnyk/Veritensor): Scanner for AI models to detect Pickle/PyTorch malware, check licenses, and verify HF hashes. ![GitHub Repo stars](https://img.shields.io/github/stars/ArseniiBrazhnyk/Veritensor?style=social)
- [**TrustGate**](https://github.com/NeuralTrust/TrustGate): Generative Application Firewall for GenAI Applications ![GitHub stars](https://img.shields.io/github/stars/NeuralTrust/TrustGate?style=social)
- [**LLM Confidentiality**](https://github.com/LostOxygen/llm-confidentiality): Tool for ensuring confidentiality in LLMs ![GitHub stars](https://img.shields.io/github/stars/LostOxygen/llm-confidentiality?style=social)
- [**LocalMod**](https://github.com/KOKOSde/localmod): Self-hosted content moderation API with prompt injection detection, toxicity filtering, PII detection, and NSFW filtering ![GitHub stars](https://img.shields.io/github/stars/KOKOSde/localmod?style=social)
- [**Tenuo**](https://github.com/tenuo-ai/tenuo): Capability tokens for AI agents with task-scoped TTLs, offline verification, and proof-of-possession binding ![GitHub stars](https://img.shields.io/github/stars/tenuo-ai/tenuo?style=social)
- [**OpenClaw Security Suite**](https://github.com/AtlasPA/openclaw-security): 11-tool defensive security suite for AI agent workspaces (prompt injection defense, integrity verification, secret scanning, supply chain analysis). Pure Python stdlib, zero dependencies, local-only execution. ![GitHub Repo stars](https://img.shields.io/github/stars/AtlasPA/openclaw-security?style=social)
- [**Prompt Shield**](https://github.com/markmishaev76/Prompt-Shield): GitHub Action for detecting indirect prompt injection in CI/CD pipelines. 4-layer defense architecture. ![GitHub Repo stars](https://img.shields.io/github/stars/markmishaev76/Prompt-Shield?style=social)
- [AIDEFEND](https://edward-playground.github.io/aidefense-framework/): Practical knowledge base for AI security defenses

---

## 🕵️ Benchmarks

- [**JailbreakBench**](https://jailbreakbench.github.io/): Evaluating and analyzing jailbreak methods for LLMs
- [**L1B3RT45**](https://github.com/elder-plinius/L1B3RT45/): AI jailbreaking tools ![GitHub stars](https://img.shields.io/github/stars/elder-plinius/L1B3RT45?style=social)
- [**LLM Hacking Database**](https://github.com/pdparchitect/llm-hacking-database): Attacks against LLMs ![GitHub stars](https://img.shields.io/github/stars/pdparchitect/llm-hacking-database?style=social)
- [**Lakera PINT Benchmark**](https://github.com/lakeraai/pint-benchmark): Benchmark for prompt injection detection ![GitHub stars](https://img.shields.io/github/stars/lakeraai/pint-benchmark?style=social)
- [**Easy Jailbreak**](https://github.com/EasyJailbreak/EasyJailbreak): Python framework to generate adversarial jailbreak prompts ![GitHub stars](https://img.shields.io/github/stars/EasyJailbreak/EasyJailbreak?style=social)
- [**PALLMs (Payloads for Attacking Large Language Models)**](https://github.com/mik0w/pallms) ![GitHub stars](https://img.shields.io/github/stars/EasyJailbreak/EasyJailbreak?style=social)

---

## 🧩 Threat Modeling

- [**ThreatModels**](https://github.com/jsotiro/ThreatModels/tree/main): Repository for LLM threat models
- [**Pangea Attack Taxonomy**](https://pangea.cloud/resources/taxonomy/): Comprehensive taxonomy of AI/LLM attacks and vulnerabilities
- [**AI Risk Taxonomy**](https://airisk.mit.edu/)
- [**AIR-Bench 2024**](https://crfm.stanford.edu/helm/air-bench/latest/)

---

## 🧪 Playground

- [**Gandalf**](https://gandalf.lakera.ai/): Prompt injection wargame
- [**Damn Vulnerable LLM Agent**](https://github.com/ReversecLabs/damn-vulnerable-llm-agent) ![GitHub Repo stars](https://img.shields.io/github/stars/ReversecLabs/damn-vulnerable-llm-agent?style=social)
- [**LLM CV Screener**](https://github.com/ReversecLabs/llm-vulnerable-recruitment-app) ![GitHub Repo stars](https://img.shields.io/github/stars/ReversecLabs/llm-vulnerable-recruitment-app?style=social)

---

## 🧪 PoC & Study Resources

- [CipherChat](https://github.com/RobustNLP/CipherChat): Secure communication tool for LLMs ![GitHub stars](https://img.shields.io/github/stars/RobustNLP/CipherChat?style=social)
- [LLMs Finetuning Safety](https://github.com/LLM-Tuning-Safety/LLMs-Finetuning-Safety): Safety for fine-tuning LLMs ![GitHub stars](https://img.shields.io/github/stars/LLM-Tuning-Safety/LLMs-Finetuning-Safety?style=social)
- [Visual Adversarial Examples](https://github.com/Unispac/Visual-Adversarial-Examples-Jailbreak-Large-Language-Models): Jailbreaking LLMs with visual adversarial examples ![GitHub stars](https://img.shields.io/github/stars/Unispac/Visual-Adversarial-Examples-Jailbreak-Large-Language-Models?style=social)
- [FigStep](https://github.com/ThuCCSLab/FigStep): Jailbreaking vision-language models via typographic visual prompts ![GitHub stars](https://img.shields.io/github/stars/ThuCCSLab/FigStep?style=social)
- [OWASP Agentic AI](https://github.com/precize/OWASP-Agentic-AI/): OWASP Top 10 for Agentic AI ![GitHub stars](https://img.shields.io/github/stars/precize/OWASP-Agentic-AI?style=social)
- [BrokenHill](https://github.com/BishopFox/BrokenHill): Automated attack tool for GCG attack ![GitHub stars](https://img.shields.io/github/stars/BishopFox/BrokenHill?style=social)
- [Weak-to-Strong Generalization](https://github.com/XuandongZhao/weak-to-strong): Eliciting strong capabilities with weak supervision ![GitHub stars](https://img.shields.io/github/stars/XuandongZhao/weak-to-strong?style=social)
- [AnyDoor](https://github.com/sail-sg/AnyDoor): Arbitrary backdoor instances in LLMs ![GitHub stars](https://img.shields.io/github/stars/sail-sg/AnyDoor?style=social)
- [Image Hijacks](https://github.com/euanong/image-hijacks): Image-based hijacks of LLMs ![GitHub stars](https://img.shields.io/github/stars/euanong/image-hijacks?style=social)
- [Imperio](https://github.com/HKU-TASR/Imperio): Robust prompt engineering for anchoring LLMs ![GitHub stars](https://img.shields.io/github/stars/HKU-TASR/Imperio?style=social)
- [LMSanitator](https://github.com/meng-wenlong/LMSanitator): Defending LLMs against stealthy prompt injection ![GitHub stars](https://img.shields.io/github/stars/meng-wenlong/LMSanitator?style=social)
- [Virtual Prompt Injection](https://github.com/wegodev2/virtual-prompt-injection): Tool for virtual prompt injection ![GitHub stars](https://img.shields.io/github/stars/wegodev2/virtual-prompt-injection?style=social)
- [CBA](https://github.com/MiracleHH/CBA): Consciousness-Based Authentication for LLM Security ![GitHub stars](https://img.shields.io/github/stars/MiracleHH/CBA?style=social)
- [MuScleLoRA](https://github.com/ZrW00/MuScleLoRA): Multi-scenario backdoor fine-tuning of LLMs ![GitHub stars](https://img.shields.io/github/stars/ZrW00/MuScleLoRA?style=social)
- [PromptWare](https://github.com/StavC/PromptWares): PromptWares for GenAI-powered applications ![GitHub stars](https://img.shields.io/github/stars/StavC/PromptWares?style=social)
- [TrojText](https://github.com/UCF-ML-Research/TrojText): Trojan attacks on text classifiers ![GitHub stars](https://img.shields.io/github/stars/UCF-ML-Research/TrojText?style=social)
- [BadActs](https://github.com/clearloveclearlove/BadActs): Backdoor attacks via activation steering ![GitHub stars](https://img.shields.io/github/stars/clearloveclearlove/BadActs?style=social)
- [Backdoor Attacks on Fine-tuned LLaMA](https://github.com/naimul011/backdoor_attacks_on_fine-tuned_llama): Backdoor attacks on fine-tuned LLaMA ![GitHub stars](https://img.shields.io/github/stars/naimul011/backdoor_attacks_on_fine-tuned_llama?style=social)


---

## 🎥 Courses

- [AI Security Explained](https://www.youtube.com/playlist?list=PLOspHqNVtKADin6JGozvzSvUQFTQRdum-): Short essential theoretical knowledge.
- [Prompt Injection and Jailbreaking 101](https://www.youtube.com/playlist?list=PLHSZe6NjhTwW1jboW_ccfJpVTMJQvi1zW): Practical short lab studies.

---

## 🌟 Miscellaneous

- [**WhistleBlower**](https://github.com/Repello-AI/whistleblower): Infer the system prompt of an AI agent based on its generated text outputs. ![GitHub Repo stars](https://img.shields.io/github/stars/Repello-AI/whistleblower?style=social)
- [**LLM Security startups**](https://github.com/rushout09/llm-security-startups)
- [**LLM Security Problems at DEFCON31 Quals**](https://github.com/Nautilus-Institute/quals-2023/tree/main/pawan_gupta): The world's top security competition
- [**0din GenAI Bug Bounty from Mozilla**](https://0din.ai): The 0Day Investigative Network is a bug bounty program focusing on flaws within GenAI models. Vulnerability classes include Prompt Injection, Training Data Poisoning, DoS, and more.
- [**Adversarial Prompting**](https://www.promptingguide.ai/risks/adversarial): Documentation
- [**OWASP Top 10 for LLMs**](https://owasp.org/www-project-top-10-for-large-language-model-applications/): Official list of key LLM risks including prompt injection.

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

Contributions are always welcome. Please read the [Contribution Guidelines](CONTRIBUTING.md) before contributing.

> **Alternative:** [Awesome LLMSecOps](https://github.com/wearetyomsmnv/Awesome-LLMSecOps)

---

<a href="https://star-history.com/#beyefendi/awesome-llm-security&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=beyefendi/awesome-llm-security&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=beyefendi/awesome-llm-security&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=beyefendi/awesome-llm-security&type=Date" />
  </picture>
</a>
