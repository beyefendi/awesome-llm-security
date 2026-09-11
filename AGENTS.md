# Agent instructions for this repository

This is a curated [awesome list](https://github.com/sindresorhus/awesome) for LLM / agent security.

## When the user says "pull PRs" / triage PRs

1. **Read and follow** the personal skill first:
   - `~/.cursor/skills/oss-pr-triage/SKILL.md`
   - (source of truth: `~/GitHub/agents-personal/skills/content/oss-pr-triage/SKILL.md`)
2. Choose **Merge / Direct commit / Request revision** *before* editing or pushing.
3. Do **not** auto-merge from CI. The GitHub Action only coaches contributors.

## Landing policy (short)

| Situation | Action |
|-----------|--------|
| Credible project, clean/near-clean PR, star order roughly OK | **Merge** (edit on PR branch if needed) — preserve contributor credit |
| High-★ / well-known + clean one-liner | **Merge** — never skip for speed |
| 0–9★, wrong file (README vs emerging), heavy rewrite, batch with big edits | **Direct commit** on `main` with `Closes #N` |
| Star order **big mistake** (e.g. dumped at top of section without earning #1) | **Direct commit** — re-place by stars |
| Broken badge, 404, description wraps, unclear section | **Request revision** (comment; leave PR open) |

## List rules (must keep)

- `README.md`: GitHub projects **≥ 10★** (or link-only non-GitHub)
- `emerging.md`: GitHub projects **&lt; 10★**
- One-line descriptions; badge `OWNER/REPO` matches link
- Within a section: descending star order; link-only after GitHub entries
- Section by **primary function** (see `CONTRIBUTING.md`)

## CI vs maintainer

| Layer | Owns |
|-------|------|
| `.github/workflows/pr-check.yml` | Format, badge/link match, live repo, ★ threshold → file, duplicates, rough star-order **warnings** |
| Maintainer / this agent | Relevance, correct section, merge vs commit, description wording, final land |

## Do not

- Push force to `main`
- Auto-merge PRs from Actions
- Invent star badges for sites without a public GitHub repo
- Land off-topic marketing submissions to “be nice”
