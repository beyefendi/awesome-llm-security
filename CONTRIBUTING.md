# Contribution Guidelines

We follow the [Awesome Manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md).

To add, remove, or change something, open a **pull request**. PRs that match this format are much faster to review and merge.

---

## Where to add

| File | When |
|------|------|
| [README.md](README.md) | GitHub projects with **≥ 10 stars** (or non-GitHub resources without a star badge) |
| [emerging.md](emerging.md) | GitHub projects with **&lt; 10 stars** |
| [papers.md](papers.md) | Academic papers |
| [deprecated.md](deprecated.md) | Do not add here — maintainers move entries when projects disappear or commercialize |

If your project later reaches 10★, open a PR to move it from `emerging.md` to `README.md`.

---

## Pick the right section

Choose by **primary function**, not marketing language:

| Section | Belongs here if it… |
|---------|---------------------|
| Multi-Purpose Model Scanners | Scans / red-teams LLMs broadly |
| MCP & Agent Scanners | Scans agents, MCP servers, or agentic workflows |
| RAG Security | Targets RAG systems |
| Prompt Injection | Attack / jailbreak tooling and datasets |
| Autonomous Pentesting Frameworks | AI-driven pentest platforms |
| Defensive & Guardrail Tools | Detects or filters attacks (injection, PII, jailbreaks) |
| Agent Authorization & Governance | Authorizes, approves, blocks, or audits agent **actions** |
| Benchmarks | Repeatable evaluation harnesses |
| Playground | Labs, CTFs, vulnerable apps |
| PoC & Study Resources | Research, studies, PoCs |

When unsure, ask in an issue before opening a PR.

---

## Entry format

### GitHub projects (with stars badge)

```markdown
- ![GitHub Repo stars](https://img.shields.io/github/stars/OWNER/REPO?style=social) [**Name**](https://github.com/OWNER/REPO): Short one-line description
```

### Sites / docs (no GitHub repo)

```markdown
- [**Name**](https://example.com/): Short one-line description
```

Do **not** invent a stars badge for a repo that does not exist. Badge `OWNER/REPO` and link must match.

---

## Description rules (required)

1. **Keep the description in one line. Do not overflow to the next line.**
2. Keep it short — roughly **one sentence**, under ~120 characters of description text.
3. State **what it does**, not how many features, pricing, or compliance claims.
4. No marketing fluff, emoji spam, or multi-clause press-release wording.

### Example (good)

```markdown
- ![GitHub Repo stars](https://img.shields.io/github/stars/leondz/garak?style=social) [**Garak**](https://github.com/leondz/garak/): LLM vulnerability scanner
```

### Example (bad — do not do this)

```markdown
- ![GitHub Repo stars](https://img.shields.io/github/stars/example/tool?style=social) [**Example Tool**](https://github.com/example/tool): An enterprise-grade, EU AI Act–ready firewall with 26 shields, tamper-evident audit trails, PII redaction, secret detection, unicode steganography checks, and a free tier so teams can prove what their AI saw and produced across OpenAI, Anthropic, and Gemini
```

Problems: wraps to multiple lines, too long, marketing language.

---

## Placement rules

1. **Star order** — within a section, insert by `stargazers_count` (highest first). Link-only entries (no badge) go after GitHub entries.
2. **One entry per project** — do not duplicate across sections.
3. **Live link** — repo/site must be public and reachable.
4. **Not already listed** — search `README.md` and `emerging.md` first.

---

## Pull request checklist

Before opening a PR, confirm:

- [ ] Added under the correct section (and correct file: README vs emerging)
- [ ] Entry matches the format above
- [ ] Description is a **single line** (does not wrap)
- [ ] Placed in **star order** within the section
- [ ] Stars badge `OWNER/REPO` matches the link (or no badge for non-GitHub)
- [ ] Not a duplicate
- [ ] PR title names the project; body is short (optional disclosure if you maintain it)

---

## Scope

On-topic: LLM, agent, MCP, RAG, or prompt-injection security (offensive or defensive tools, benchmarks, playgrounds, studies).

Off-topic or usually declined: general AI demos with no security focus, pure marketing pages with no substance, broken/private repos.

Commercial products without a public repo may be accepted as link-only entries when they clearly fit a section; maintainers may hold them.

---

## Questions

Open an issue for a **scope check** before writing a PR if the fit is unclear. That saves everyone time.
