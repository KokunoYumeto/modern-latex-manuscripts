#!/usr/bin/env python3
"""Generate the deterministic Noether P35 Chinese producer revision-3 manifest."""

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
    "# Noether Paper 35 Chinese producer revision-3 workspace manifest",
    "# SHA256  BYTES  RELATIVE_PATH",
    "# SHA256SUMS.txt is intentionally excluded to avoid self-reference.",
]
for path in files:
    relative = path.relative_to(ROOT).as_posix()
    lines.append(f"{sha(path)}  {path.stat().st_size}  {relative}")
OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
print(f"files={len(files)} bytes={OUTPUT.stat().st_size} sha256={sha(OUTPUT)}")

