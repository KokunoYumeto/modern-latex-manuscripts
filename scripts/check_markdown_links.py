#!/usr/bin/env python3
"""Check local Markdown links in repository docs.

External links are ignored. Anchor-only links are ignored. The check verifies
that relative Markdown links point to existing local files.

Run from the repository root:

    python scripts/check_markdown_links.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")


def iter_markdown_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if ".git" not in path.parts and "node_modules" not in path.parts
    )


def target_path(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip()
    if not target or target.startswith(SKIP_PREFIXES):
        return None
    if " " in target and not target.startswith("<"):
        # Markdown links in this repo should not need bare spaces.
        target = target.split()[0]
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    target = target.split("#", 1)[0]
    if not target:
        return None
    return (source.parent / unquote(target)).resolve()


def main() -> int:
    root = Path.cwd().resolve()
    problems: list[str] = []
    for md_file in iter_markdown_files(root):
        text = md_file.read_text(encoding="utf-8")
        for match in LINK_PATTERN.finditer(text):
            resolved = target_path(md_file, match.group(1))
            if resolved is None:
                continue
            try:
                resolved.relative_to(root)
            except ValueError:
                problems.append(f"{md_file.relative_to(root)}: link leaves repo: {match.group(1)}")
                continue
            if not resolved.exists():
                problems.append(f"{md_file.relative_to(root)}: missing link target: {match.group(1)}")

    if problems:
        for problem in problems:
            print(problem)
        return 1
    print(f"Checked local links in {len(iter_markdown_files(root))} Markdown files: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

