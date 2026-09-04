#!/usr/bin/env python3
"""Rebuild README.md from the curated sections of aisecurity.ninja.

The site is the source of truth. This script reads the JSON files the site
itself renders from (data/*.json) and writes a README in list form. Output is
deterministic: same data in, same bytes out, so the monthly workflow only
commits when something on the site actually changed.

Where the data comes from, in order of preference:
  1. --local DIR              read DIR/*.json (testing)
  2. SOURCE_REPO_TOKEN set    read public/data/*.json from the site's source
                              repository through the GitHub API (what the
                              workflow does: the live site's bot protection
                              challenges datacenter IPs such as GitHub runners)
  3. otherwise                fetch https://aisecurity.ninja/data/*.json

Stdlib only. This script is MIT licensed; the generated text is CC BY 4.0.
"""
import json
import os
import re
import sys
import urllib.request
from pathlib import Path
from typing import Optional

SITE = "https://aisecurity.ninja"
REPO = "https://github.com/sambucci/ai-security-ninja"
SOURCE_REPO = "sambucci/web-aisecurity-ninja"   # private; the deployed site is its main branch
SOURCE_PATH = "public/data"

# Section order on the page. Slug, kind ("entries" or "papers").
SECTIONS = [
    ("frameworks-and-governance", "entries"),
    ("foundational-papers", "papers"),
    ("code-and-pocs", "entries"),
    ("guides-and-tutorials", "entries"),
    ("courses", "entries"),
    ("communities", "entries"),
    ("links", "entries"),
]

# Sentences in the section leads that only restate the non-affiliation
# disclaimer. They are collapsed into one note near the top of the README.
DISCLAIMER_MARKERS = (
    "not affiliated",
    "not an endorsement",
    "not a recommendation",
    "not directly connected",
    "inclusion is not",
    "does not constitute",
)

MIN_TOTAL_ENTRIES = 60  # refuse to overwrite the README if the feed looks broken

# --- Hero banner (figlet ANSI Shadow renderings plus two original sprites, kept as plain
# strings so the workflow needs nothing beyond the standard library) ---
BANNER_TOP = [
    " █████╗ ██╗    ███████╗███████╗ ██████╗██╗   ██╗██████╗ ██╗████████╗██╗   ██╗",
    "██╔══██╗██║    ██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗██║╚══██╔══╝╚██╗ ██╔╝",
    "███████║██║    ███████╗█████╗  ██║     ██║   ██║██████╔╝██║   ██║    ╚████╔╝",
    "██╔══██║██║    ╚════██║██╔══╝  ██║     ██║   ██║██╔══██╗██║   ██║     ╚██╔╝",
    "██║  ██║██║    ███████║███████╗╚██████╗╚██████╔╝██║  ██║██║   ██║      ██║",
    "╚═╝  ╚═╝╚═╝    ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝",
]
BANNER_NINJA = [
    "███╗   ██╗██╗███╗   ██╗     ██╗ █████╗",
    "████╗  ██║██║████╗  ██║     ██║██╔══██╗",
    "██╔██╗ ██║██║██╔██╗ ██║     ██║███████║",
    "██║╚██╗██║██║██║╚██╗██║██   ██║██╔══██║",
    "██║ ╚████║██║██║ ╚████║╚█████╔╝██║  ██║",
    "╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚════╝ ╚═╝  ╚═╝",
]
NINJA_SPRITE = [
    "     ▄██████▄",
    " ▄▄ ███▀██▀███",
    "  ▀ ▀████████▀",
    "     ▄██████▄",
    "  ▄██▀▀██████▀▀▀",
    " █▀    ██████",
    "      ▄██▀▀██▄",
    "    ▄██▀    ▀██▄",
]
SHURIKEN = [
    "      █▄",
    "    ▄████",
    " ▄███▀▀▀██▄",
    "▀▀███   ████▀",
    "   ▀█████▀▀",
    "    ▀██▀",
    "      ▀",
]


def _vpad(lines, h):
    out = [""] * ((h - len(lines)) // 2) + lines
    return out + [""] * (h - len(out))


def banner(total: int, sections: int, reviewed: str) -> str:
    """The hero block: AI SECURITY, then a ninja throwing a shuriken past the word NINJA, then a stats line."""
    width = max(len(l) for l in BANNER_TOP)
    lw = max(len(l) for l in NINJA_SPRITE)
    nw = max(len(l) for l in BANNER_NINJA)
    rw = max(len(l) for l in SHURIKEN)
    h = max(len(NINJA_SPRITE), len(BANNER_NINJA), len(SHURIKEN))
    left, word, right = _vpad(NINJA_SPRITE, h), _vpad(BANNER_NINJA, h), _vpad(SHURIKEN, h)
    gap = (width - lw - nw - rw) // 2
    mid = [(left[i].ljust(lw) + " " * gap + word[i].ljust(nw) + " " * gap + right[i]).rstrip() for i in range(h)]
    a, b, c = f"ENTRIES  {total}", f"SECTIONS  {sections}", f"LAST REVIEWED  {reviewed}"
    g = (width - len(a) - len(b) - len(c)) // 2
    stats = a + " " * g + b + " " * (width - len(a) - len(b) - len(c) - g) + c
    return "```text\n" + "\n".join(BANNER_TOP + [""] + mid + [""] + [stats]) + "\n```\n"


def fetch(slug: str, local: Optional[Path]):
    if local is not None:
        return json.loads((local / f"{slug}.json").read_text(encoding="utf-8"))
    headers = {"User-Agent": "ai-security-ninja-mirror (+" + REPO + ")"}
    token = os.environ.get("SOURCE_REPO_TOKEN", "").strip()
    if token:
        url = f"https://api.github.com/repos/{SOURCE_REPO}/contents/{SOURCE_PATH}/{slug}.json?ref=main"
        headers["Authorization"] = f"Bearer {token}"
        headers["Accept"] = "application/vnd.github.raw+json"
    else:
        url = f"{SITE}/data/{slug}.json"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as resp:
        raw = resp.read()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        where = "the source repository" if token else "the live site"
        hint = "" if token else " (its bot protection challenges datacenter IPs; set SOURCE_REPO_TOKEN to read from the source repository instead)"
        raise SystemExit(f"{slug}.json from {where} is not JSON: {len(raw)} bytes starting {raw[:80]!r}{hint}")


def clean(text: str) -> str:
    """Normalise punctuation and escape Markdown in prose fields (never URLs)."""
    text = (text or "").strip()
    text = re.sub(r"\s+", " ", text)
    # Em-dashes: a pair becomes a parenthetical with commas, a single one a colon.
    text = re.sub(r"\s*—([^—.]*?)—\s*", r", \1, ", text)
    text = re.sub(r"\s*—\s*", ": ", text)
    text = text.replace("–", "-")
    for ch in ("*", "_", "[", "]"):
        text = text.replace(ch, "\\" + ch)
    return text


def lead_without_disclaimer(lead: str) -> str:
    sentences = re.split(r"(?<=[.!?])\s+", (lead or "").strip())
    kept = [s for s in sentences if s and not any(m in s.lower() for m in DISCLAIMER_MARKERS)]
    return clean(" ".join(kept))


def join_authors(authors) -> str:
    """The source splits author strings on commas, which breaks names like
    'X (Robust Intelligence, Inc.)'. Re-join fragments until parentheses balance."""
    merged, buf = [], ""
    for part in authors or []:
        buf = f"{buf}, {part}" if buf else part
        if buf.count("(") <= buf.count(")"):
            merged.append(buf.strip())
            buf = ""
    if buf:
        merged.append(buf.strip())
    return clean(", ".join(merged))


def anchor(title: str) -> str:
    a = re.sub(r"[^\w\s-]", "", title.lower())
    return re.sub(r"\s+", "-", a.strip())


def render_entry(e: dict) -> str:
    name = clean(e.get("name", ""))
    url = (e.get("url") or "").strip()
    meta = ", ".join(clean(str(v)) for v in (e.get("meta") or {}).values() if str(v).strip())
    head = f"- **[{name}]({url})**" if url else f"- **{name}**"
    if meta:
        head += f" ({meta})"
    desc = clean(e.get("description", ""))
    return head + (f"\n\n  {desc}\n" if desc else "\n")


def render_paper(p: dict) -> str:
    title = clean(p.get("title", ""))
    link = (p.get("link") or "").strip()
    who = join_authors(p.get("authors"))
    year = clean(str(p.get("year", "")))
    tail = ", ".join(x for x in (who, year) if x)
    head = f"- **[{title}]({link})**" if link else f"- **{title}**"
    if tail:
        head += f" ({tail})"
    brief = clean(p.get("brief", ""))
    return head + (f"\n\n  {brief}\n" if brief else "\n")


def main() -> int:
    local = None
    if len(sys.argv) == 3 and sys.argv[1] == "--local":
        local = Path(sys.argv[2])
    elif len(sys.argv) != 1:
        print(__doc__)
        return 2

    sections = []
    for slug, kind in SECTIONS:
        data = fetch(slug, local)
        if kind == "papers":
            items = data if isinstance(data, list) else data.get("entries", [])
            sections.append({"slug": slug, "title": "Foundational papers", "lead": "",
                             "reviewed": "", "kind": kind, "items": items})
        else:
            sections.append({"slug": slug, "title": data.get("title") or slug,
                             "lead": data.get("lead", ""), "reviewed": data.get("last_reviewed", ""),
                             "kind": kind, "items": data.get("entries", [])})

    total = sum(len(s["items"]) for s in sections)
    empty = [s["slug"] for s in sections if not s["items"]]
    if total < MIN_TOTAL_ENTRIES or empty:
        print(f"Refusing to write: {total} entries, empty sections: {empty}", file=sys.stderr)
        return 1
    reviewed = max((s["reviewed"] for s in sections if s["reviewed"]), default="")

    out = []
    out.append(banner(total, len(sections), reviewed))
    out.append("A curated, living map of AI security: frameworks, foundational papers, code, guides, "
               f"courses and communities. This repository mirrors the curated sections of [aisecurity.ninja]({SITE}) "
               "and rebuilds itself from the site's data once a month.\n")
    out.append("I built the map as my own reference and made it public because it seemed useful. The site carries "
               f"the whole thing, including a [papers feed]({SITE}/papers) that updates itself every day from arXiv; "
               "that stream is deliberately not mirrored here. What this repository holds is the slow-moving, "
               "human-reviewed layer, the part that benefits from being forkable, searchable and citable.\n")
    out.append("**Inclusion is not endorsement.** I am not affiliated with, endorsed by or connected to any of the "
               "projects, organisations, courses or communities listed. Entries are amended or removed on evidence; "
               "see [how to suggest a change](#about-this-repository) at the end.\n")
    out.append(f"{total} entries in {len(sections)} sections. Sections last reviewed on the site: {reviewed}.\n")

    out.append("## Contents\n")
    for s in sections:
        out.append(f"- [{s['title']}](#{anchor(s['title'])}) ({len(s['items'])})")
    out.append("")

    for s in sections:
        out.append(f"## {s['title']}\n")
        lead = lead_without_disclaimer(s["lead"])
        if lead:
            out.append(lead + "\n")
        render = render_paper if s["kind"] == "papers" else render_entry
        for item in s["items"]:
            out.append(render(item))

    out.append("## About this repository\n")
    out.append(f"The site is the source of truth. This README is generated by [`build_readme.py`](build_readme.py) "
               "from the site's `data/*.json` files, and a [monthly workflow](.github/workflows/rebuild.yml) rebuilds it, "
               "committing only when something changed. Do not edit README.md by hand: the next rebuild would "
               "overwrite your change.\n")
    out.append(f"To suggest an entry or a correction, [open an issue]({REPO}/issues) with a source. Accepted "
               "changes land on the site first and flow here at the next rebuild. An entry is amended or removed "
               "when a source shows it should be, never on a single failed link.\n")
    out.append("Kept by [Luca Sambucci](https://www.sambucci.com), founder of "
               "[Noctive Security](https://www.noctivesecurity.com). Curated through an agent, kept free of hype.\n")
    out.append("Text licensed under [CC BY 4.0](LICENSE); `build_readme.py` is MIT.\n")

    Path("README.md").write_text("\n".join(out), encoding="utf-8")
    print(f"README.md written: {total} entries, {len(sections)} sections, last reviewed {reviewed}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
