#!/usr/bin/env python3
"""Mechanical PR checks for awesome-llm-security list entries.

Validates format, badge/link match, live repo, star threshold (README vs
emerging), duplicates, description length, and rough star order.
Does not judge topical fit, section choice, or merge vs commit — maintainers do.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STAR_THRESHOLD = 10
DESC_SOFT_LIMIT = 120
DESC_HARD_LIMIT = 180

GITHUB_LINE = re.compile(
    r"^- !\[GitHub (?:Repo )?stars\]\(https://img\.shields\.io/github/stars/"
    r"(?P<badge_owner>[^/]+)/(?P<badge_repo>[^)?]+)"
    r"(?:\?[^)]*)?\) "
    r"\[\*\*(?P<name>[^*]+)\*\*\]\(https://github\.com/"
    r"(?P<link_owner>[^/]+)/(?P<link_repo>[^)/]+)/?\)"
    r"(?P<sep>[: ]+)\s*(?P<desc>.+)$"
)

LINK_ONLY_LINE = re.compile(
    r"^- \[\*\*(?P<name>[^*]+)\*\*\]\((?P<url>https?://[^)]+)\)"
    r"(?P<sep>[: ]+)\s*(?P<desc>.+)$"
)

SECTION_HEADER = re.compile(r"^### ")


@dataclass
class Finding:
    level: str  # error | warn | info
    message: str


@dataclass
class AddedEntry:
    file: str
    line_no: int
    raw: str
    kind: str  # github | link_only | unknown
    owner: str | None = None
    repo: str | None = None
    name: str | None = None
    desc: str | None = None
    stars: int | None = None
    findings: list[Finding] = field(default_factory=list)


def github_api(path: str) -> dict | None:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    req = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "awesome-llm-security-pr-check",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def parse_diff_added_lines(diff_text: str) -> list[tuple[str, int, str]]:
    """Return (path, new_file_line_no, line_text) for added content lines."""
    results: list[tuple[str, int, str]] = []
    path = ""
    new_line = 0
    tracked = False
    for line in diff_text.splitlines():
        if line.startswith("--- "):
            continue
        if line.startswith("+++ b/"):
            path = line[6:]
            tracked = path in ("README.md", "emerging.md")
            new_line = 0
            continue
        if line.startswith("@@"):
            m = re.search(r"\+(\d+)", line)
            new_line = int(m.group(1)) - 1 if m else 0
            continue
        if not tracked:
            continue
        if line.startswith("+") and not line.startswith("+++"):
            new_line += 1
            results.append((path, new_line, line[1:]))
        elif line.startswith("-") and not line.startswith("---"):
            continue
        elif line.startswith(" ") or line == "":
            # context line (unified diff prefixes space; empty rare)
            if line.startswith(" "):
                new_line += 1
    return results


def load_existing_slugs() -> set[str]:
    slugs: set[str] = set()
    for fname in ("README.md", "emerging.md"):
        text = (ROOT / fname).read_text(encoding="utf-8")
        for m in re.finditer(
            r"github\.com/([^/\s)]+)/([^/\s)]+)", text, re.IGNORECASE
        ):
            slugs.add(f"{m.group(1)}/{m.group(2)}".rstrip("/").lower())
    return slugs


def section_github_stars(file_text: str, around_line: int) -> list[tuple[int, str, str]]:
    """Return (line_no, owner/repo, line) for GitHub badge entries in the same ### section."""
    lines = file_text.splitlines()
    # find section bounds
    start = 0
    end = len(lines)
    for i in range(around_line - 1, -1, -1):
        if SECTION_HEADER.match(lines[i]):
            start = i + 1
            break
    for i in range(around_line, len(lines)):
        if SECTION_HEADER.match(lines[i]) or lines[i].startswith("## "):
            end = i
            break
    out: list[tuple[int, str, str]] = []
    for i in range(start, end):
        m = GITHUB_LINE.match(lines[i])
        if m:
            slug = f"{m.group('link_owner')}/{m.group('link_repo')}"
            out.append((i + 1, slug, lines[i]))
    return out


def check_entry(entry: AddedEntry, existing_before: set[str], file_text: str) -> None:
    if entry.kind == "unknown":
        if entry.raw.startswith("- ") and (
            "shields.io/github/stars" in entry.raw or "github.com/" in entry.raw
        ):
            entry.findings.append(
                Finding(
                    "error",
                    "Line does not match expected list format "
                    "(badge + [**Name**](url): description).",
                )
            )
        return

    if not entry.desc or not entry.desc.strip():
        entry.findings.append(Finding("error", "Missing description."))
        return

    desc = entry.desc.strip()
    if len(desc) > DESC_HARD_LIMIT:
        entry.findings.append(
            Finding(
                "error",
                f"Description too long ({len(desc)} chars; keep under ~{DESC_SOFT_LIMIT}, hard fail at {DESC_HARD_LIMIT}).",
            )
        )
    elif len(desc) > DESC_SOFT_LIMIT:
        entry.findings.append(
            Finding(
                "warn",
                f"Description is {len(desc)} chars (target ≤{DESC_SOFT_LIMIT}).",
            )
        )

    if entry.kind == "link_only":
        entry.findings.append(
            Finding("info", "Link-only entry (no star badge) — OK for non-GitHub resources.")
        )
        return

    assert entry.owner and entry.repo
    badge_slug = f"{entry.owner}/{entry.repo}"
    # badge vs link already enforced by regex groups if kind==github with match
    slug_l = badge_slug.lower()

    # duplicate: slug appears more than once in combined files after change,
    # or already existed and this is a second add (heuristic: count in file)
    count = len(
        re.findall(
            re.escape(f"github.com/{entry.owner}/{entry.repo}"),
            file_text,
            flags=re.IGNORECASE,
        )
    )
    if count > 1:
        entry.findings.append(
            Finding("error", f"Duplicate listing for `{badge_slug}` in {entry.file}.")
        )
    elif slug_l in existing_before and count == 1:
        # might be a move; treat as info
        entry.findings.append(
            Finding("info", f"`{badge_slug}` was already listed elsewhere — confirm this is a move, not a duplicate.")
        )

    data = github_api(f"/repos/{entry.owner}/{entry.repo}")
    if data is None:
        entry.findings.append(
            Finding("error", f"GitHub repo not found: `{badge_slug}` (404).")
        )
        return

    stars = int(data.get("stargazers_count") or 0)
    entry.stars = stars
    if data.get("archived"):
        entry.findings.append(Finding("warn", f"`{badge_slug}` is archived."))
    if data.get("private"):
        entry.findings.append(Finding("error", f"`{badge_slug}` is private."))

    if entry.file == "README.md" and stars < STAR_THRESHOLD:
        entry.findings.append(
            Finding(
                "error",
                f"`{badge_slug}` has {stars}★ — belongs in `emerging.md` (<{STAR_THRESHOLD}★), not README.",
            )
        )
    elif entry.file == "emerging.md" and stars >= STAR_THRESHOLD:
        entry.findings.append(
            Finding(
                "warn",
                f"`{badge_slug}` has {stars}★ — eligible for README (≥{STAR_THRESHOLD}★).",
            )
        )
    else:
        entry.findings.append(
            Finding("info", f"`{badge_slug}` has {stars}★ — file placement OK.")
        )

    # rough star order within section
    neighbors = section_github_stars(file_text, entry.line_no)
    # find our index
    idx = next(
        (i for i, (_, slug, _) in enumerate(neighbors) if slug.lower() == slug_l),
        None,
    )
    if idx is None or entry.stars is None:
        return

    def fetch_stars(slug: str) -> int | None:
        o, r = slug.split("/", 1)
        d = github_api(f"/repos/{o}/{r}")
        return int(d["stargazers_count"]) if d else None

    if idx > 0:
        above_slug = neighbors[idx - 1][1]
        above_stars = fetch_stars(above_slug)
        if above_stars is not None and entry.stars > above_stars * 1.5 and entry.stars - above_stars >= 50:
            entry.findings.append(
                Finding(
                    "warn",
                    f"Star order: `{badge_slug}` ({entry.stars}★) is below `{above_slug}` ({above_stars}★) — may belong higher.",
                )
            )
    if idx < len(neighbors) - 1:
        below_slug = neighbors[idx + 1][1]
        below_stars = fetch_stars(below_slug)
        if below_stars is not None and below_stars > entry.stars * 1.5 and below_stars - entry.stars >= 50:
            entry.findings.append(
                Finding(
                    "warn",
                    f"Star order: `{badge_slug}` ({entry.stars}★) is above `{below_slug}` ({below_stars}★) — may belong lower.",
                )
            )

    # parked at very top of a long section with low stars vs first neighbor
    if idx == 0 and len(neighbors) > 3:
        # compare to median of next few
        sample = []
        for _, slug, _ in neighbors[1:4]:
            s = fetch_stars(slug)
            if s is not None:
                sample.append(s)
        if sample and entry.stars is not None and max(sample) > entry.stars * 2 and max(sample) - entry.stars >= 100:
            entry.findings.append(
                Finding(
                    "warn",
                    f"Placed at top of section but {entry.stars}★ is far below neighbors — likely a star-order mistake.",
                )
            )


def classify_line(path: str, line_no: int, text: str) -> AddedEntry | None:
    if not text.startswith("- "):
        return None
    m = GITHUB_LINE.match(text)
    if m:
        bo, br = m.group("badge_owner"), m.group("badge_repo")
        lo, lr = m.group("link_owner"), m.group("link_repo")
        entry = AddedEntry(
            file=path,
            line_no=line_no,
            raw=text,
            kind="github",
            owner=lo,
            repo=lr.rstrip("/"),
            name=m.group("name"),
            desc=m.group("desc"),
        )
        if (bo, br.rstrip("/")) != (lo, lr.rstrip("/")):
            entry.findings.append(
                Finding(
                    "error",
                    f"Badge `{bo}/{br}` does not match link `{lo}/{lr}`.",
                )
            )
        return entry
    m2 = LINK_ONLY_LINE.match(text)
    if m2:
        return AddedEntry(
            file=path,
            line_no=line_no,
            raw=text,
            kind="link_only",
            name=m2.group("name"),
            desc=m2.group("desc"),
        )
    if "shields.io" in text or "github.com/" in text:
        return AddedEntry(file=path, line_no=line_no, raw=text, kind="unknown")
    return None


def render_report(entries: list[AddedEntry]) -> tuple[str, int, int]:
    errors = warns = 0
    lines = [
        "<!-- awesome-llm-security-pr-check -->",
        "## List entry check",
        "",
        "Automated format / stars / link checks from [CONTRIBUTING.md](https://github.com/beyefendi/awesome-llm-security/blob/main/CONTRIBUTING.md). "
        "Section fit and merge decisions are still maintainer-reviewed.",
        "",
    ]
    if not entries:
        lines += [
            "_No new list bullet lines detected in `README.md` / `emerging.md`._",
            "",
        ]
        return "\n".join(lines), 0, 0

    for e in entries:
        title = e.name or e.raw[:60]
        stars = f" · {e.stars}★" if e.stars is not None else ""
        lines.append(f"### `{e.file}:{e.line_no}` — {title}{stars}")
        lines.append("")
        if not e.findings:
            lines.append("- ✅ No issues")
        for f in e.findings:
            icon = {"error": "❌", "warn": "⚠️", "info": "ℹ️"}[f.level]
            lines.append(f"- {icon} **{f.level}:** {f.message}")
            if f.level == "error":
                errors += 1
            elif f.level == "warn":
                warns += 1
        lines.append("")

    lines.append("---")
    lines.append(f"**Summary:** {errors} error(s), {warns} warning(s).")
    if errors:
        lines.append("")
        lines.append(
            "Please fix errors (format, badge/link match, wrong file for star count, dead repo) and push again."
        )
    lines.append("")
    return "\n".join(lines), errors, warns


def upsert_pr_comment(body: str) -> None:
    repo = os.environ.get("GITHUB_REPOSITORY")
    pr = os.environ.get("PR_NUMBER")
    token = os.environ.get("GITHUB_TOKEN")
    if not (repo and pr and token):
        return
    owner, name = repo.split("/", 1)
    # list comments
    comments = github_api(f"/repos/{owner}/{name}/issues/{pr}/comments?per_page=100") or []
    marker = "<!-- awesome-llm-security-pr-check -->"
    existing_id = None
    if isinstance(comments, list):
        for c in comments:
            if marker in (c.get("body") or ""):
                existing_id = c.get("id")
                break

    data = json.dumps({"body": body}).encode()
    if existing_id:
        url = f"https://api.github.com/repos/{owner}/{name}/issues/comments/{existing_id}"
        method = "PATCH"
    else:
        url = f"https://api.github.com/repos/{owner}/{name}/issues/{pr}/comments"
        method = "POST"
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "awesome-llm-security-pr-check",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        resp.read()


def main() -> int:
    base = os.environ.get("BASE_SHA", "origin/main")
    head = os.environ.get("HEAD_SHA", "HEAD")
    # Prefer explicit diff file from workflow
    diff_path = os.environ.get("DIFF_FILE")
    if diff_path and Path(diff_path).is_file():
        diff_text = Path(diff_path).read_text(encoding="utf-8")
    else:
        import subprocess

        diff_text = subprocess.check_output(
            ["git", "diff", f"{base}...{head}", "--", "README.md", "emerging.md"],
            cwd=ROOT,
            text=True,
        )

    # existing slugs from base versions roughly: current working tree minus added
    # Simpler: use current files for section order; for duplicate-before use base checkout if available
    existing_before: set[str] = set()
    try:
        import subprocess

        for fname in ("README.md", "emerging.md"):
            try:
                text = subprocess.check_output(
                    ["git", "show", f"{base}:{fname}"],
                    cwd=ROOT,
                    text=True,
                    stderr=subprocess.DEVNULL,
                )
            except subprocess.CalledProcessError:
                continue
            for m in re.finditer(
                r"github\.com/([^/\s)]+)/([^/\s)]+)", text, re.IGNORECASE
            ):
                existing_before.add(f"{m.group(1)}/{m.group(2)}".rstrip("/").lower())
    except Exception:
        existing_before = load_existing_slugs()

    added_raw = parse_diff_added_lines(diff_text)
    entries: list[AddedEntry] = []
    for path, line_no, text in added_raw:
        # skip pure whitespace / headers
        if text.startswith("#") or not text.strip():
            continue
        entry = classify_line(path, line_no, text)
        if entry:
            entries.append(entry)

    file_texts = {
        "README.md": (ROOT / "README.md").read_text(encoding="utf-8"),
        "emerging.md": (ROOT / "emerging.md").read_text(encoding="utf-8"),
    }

    for e in entries:
        check_entry(e, existing_before, file_texts[e.file])

    report, errors, warns = render_report(entries)
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        Path(summary_path).write_text(report + "\n", encoding="utf-8")
    out_file = os.environ.get("REPORT_FILE", str(ROOT / "pr-check-report.md"))
    Path(out_file).write_text(report + "\n", encoding="utf-8")
    print(report)

    if os.environ.get("POST_PR_COMMENT", "").lower() in ("1", "true", "yes"):
        try:
            upsert_pr_comment(report)
        except Exception as exc:
            print(f"warning: could not post PR comment: {exc}", file=sys.stderr)

    # Fail only on errors
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
