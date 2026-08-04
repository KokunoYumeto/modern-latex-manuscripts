#!/usr/bin/env python3
"""Generate the deterministic Paper 35 producer-workspace SHA-256 manifest."""

from pathlib import Path
import hashlib


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "SHA256SUMS.txt"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


files = sorted(
    (path for path in ROOT.rglob("*") if path.is_file() and path != OUTPUT),
    key=lambda path: path.relative_to(ROOT).as_posix(),
)
lines = [
    "# Noether Paper 35 Chinese producer workspace manifest",
    "# SHA256  BYTES  RELATIVE_PATH",
    "# SHA256SUMS.txt is intentionally excluded to avoid self-reference.",
]
for path in files:
    relative = path.relative_to(ROOT).as_posix()
    lines.append(f"{sha(path)}  {len(path.read_bytes())}  {relative}")
OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
print(f"files={len(files)} bytes={len(OUTPUT.read_bytes())} sha256={sha(OUTPUT)}")

