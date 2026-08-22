#!/usr/bin/env python3
"""Build the bounded D015 GitHub pre-commit byte manifest."""

from __future__ import annotations

import argparse
import hashlib
import subprocess
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--from-index", action="store_true", help="Hash the exact staged Git blobs rather than working-tree bytes")
    args = parser.parse_args()
    repo = args.repo.resolve()
    base = Path("sources/deligne/forward-001-016p040-source-witness/D016_LC_p031_040")
    fixed = [
        base / "SEQ_CUM/D015_AM/PDF/D015_AM_full_EN.pdf",
        base / "SEQ_CUM/D015_AM/PDF/D015_AM_full_FR.pdf",
        base / "SEQ_CUM/D015_AM/SCAN/D015_AM_full_SCAN.pdf",
        base / "SEQ_CUM/D015_AM/TEX/D015_AM_full_EN.tex",
        base / "SEQ_CUM/D015_AM/TEX/D015_AM_full_FR.tex",
        base / "SEQ_CUM/D015_AM/TEX/D015_APPARATUS.md",
        base / "SEQ_CUM/ALL_001_016p040/PDF/ALL_001_016p040_EN.pdf",
        base / "SEQ_CUM/ALL_001_016p040/PDF/ALL_001_016p040_FR.pdf",
        base / "SEQ_CUM/ALL_001_016p040/SCAN/ALL_001_016p040_SCAN.pdf",
        base / "SEQ_CUM/ALL_001_016p040/TEX/ALL_001_016p040_MANIFEST.md",
        base / "Method/DIAGRAM_AUDIT_006_015.md",
        Path("reader-pdfs/deligne/00-000 Deligne - Sequential Cumulative Papers 001-016p040 - English Translation.pdf"),
        Path("reader-pdfs/deligne/01-000 Deligne - Sequential Cumulative Papers 001-016p040 - French Working PDF.pdf"),
        Path("reader-pdfs/deligne/00-015 Deligne - Unirational Non-Rational Varieties - English Translation.pdf"),
        Path("reader-pdfs/deligne/01-015 Deligne - Varietes unirationnelles non rationnelles - French Working PDF.pdf"),
        Path("manifests/99 Deligne - Public Summary.json"),
    ]
    fixed.extend(path.relative_to(repo) for path in sorted((repo / base / "SEQ_CUM/D015_AM/TEX/D015_assets").glob("*.png")))
    fixed.extend(
        path.relative_to(repo)
        for path in sorted((repo / base / "Method").glob("D015*"))
        if path.name != args.output.name
    )
    paths = sorted(set(fixed), key=lambda path: path.as_posix().lower())
    lines = ["repo_path\tbytes\tsha256"]
    for relative in paths:
        path = repo / relative
        if not path.is_file():
            raise FileNotFoundError(path)
        if args.from_index:
            data = subprocess.run(
                ["git", "show", f":{relative.as_posix()}"],
                cwd=repo,
                check=True,
                capture_output=True,
            ).stdout
            size = len(data)
            digest = hashlib.sha256(data).hexdigest().upper()
        else:
            size = path.stat().st_size
            digest = sha256(path)
        if size >= 100_000_000:
            raise ValueError(f"GitHub 100 MB contract exceeded: {path}")
        lines.append(f"{relative.as_posix()}\t{size}\t{digest}")
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"entries={len(paths)} bytes={args.output.stat().st_size} sha256={sha256(args.output)}")


if __name__ == "__main__":
    main()
