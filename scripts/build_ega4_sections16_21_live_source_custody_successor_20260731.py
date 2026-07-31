#!/usr/bin/env python3
"""Capture the post-05:26 EGA IV Sections 16-21 live-source successor."""

from __future__ import annotations

import csv
import json
import shutil
from pathlib import Path

import build_ega4_sections16_21_live_source_custody_20260731 as base


base.LANES = (
    {
        "key": "sections16-18",
        "master": "ega4_sections16_18_source_aligned_successor_r1.tex",
        "sources": ("ega4-16.tex", "ega4-17.tex", "ega4-18.tex"),
        "checkpoint": "checkpoint_printed149_r36",
        "aligned_from": 5,
        "aligned_through": 149,
        "next_page": 150,
        "output": "EGA4_sections16_18_live_source_20260731T0546.pdf",
    },
    {
        "key": "sections19-21",
        "master": "ega4_sections19_21_source_aligned_successor_r1.tex",
        "sources": ("ega4-19.tex", "ega4-20.tex", "ega4-21.tex"),
        "checkpoint": "build_p185_271_r14",
        "aligned_from": 185,
        "aligned_through": 271,
        "next_page": 272,
        "output": "EGA4_sections19_21_live_source_20260731T0546.pdf",
    },
)


def rewrite_controls(destination: Path) -> None:
    (destination / ".gitattributes").write_bytes(b"* -text\n")
    readme = """# EGA IV Sections 16-21 live source custody successor

Captured after exact pre/copy/post identity checks. This directory preserves
the then-current editable source closures for the two active EGA IV Part 4
alignment lanes and fresh three-pass convenience builds from those copied
bytes.

## Conservative checkpoint boundary

- Sections 16-18: producer checkpoint `checkpoint_printed149_r36`, aligned
  through printed page 149; conservative next page 150.
- Sections 19-21: producer checkpoint `build_p185_271_r14`, aligned through
  printed page 271; conservative next page 272.

The copied source files were newer than the named producer checkpoints. Those
later bytes are preserved because they are valuable live work, while the
public claim remains bounded by the named checkpoints above.

Both copied source closures built in three XeLaTeX passes with zero hard TeX
diagnostics. Extracted PDF text has zero private-path, task-ID, model-name, or
project-process hits. The readers contain mathematical content, title, and
contents only; no status or AI preface is injected.

The controlling authority is the 360-page NUMDAM EGA IV Part 4 PDF, SHA-256
`B4277FB99C6EDF8FEEC5B01F54368E4B8521BCD52871316C0EDF6FF4AE69389E`.
The authority PDF, source pixels, OCR bodies, raw logs, auxiliaries, caches,
and private process material are excluded. Actual source images are preserved
separately on the existing EGA Zenodo concept.

This is GitHub source survival and a buildable working snapshot, not a complete
EGA IV reader, critical edition, rights determination, peer review,
accessibility certification, or mathematical certification.
"""
    status = """# Public custody status

- Sections 16-18 checkpoint-backed alignment: printed pages 5-149.
- Sections 19-21 checkpoint-backed alignment: printed pages 185-271.
- Later live editable bytes: preserved without a stronger coverage claim.
- Editable source closure: included for Sections 16-21.
- Fresh convenience builds: included; three XeLaTeX passes each.
- Reader-facing AI/process prose: none.
- Authority scan, pixels, OCR, raw logs, and auxiliaries: excluded.
- Complete EGA IV or exhaustive reference-v2 claim: no.
- Classification: public GitHub live source survival plus fresh build closure.
- Zenodo mutation for this source snapshot: none.
- Rights: no blanket license grant asserted.
"""
    (destination / "README.md").write_text(readme, encoding="ascii")
    (destination / "STATUS_PUBLIC.md").write_text(status, encoding="ascii")

    manifest_path = destination / "SHA256SUMS.csv"
    validation_path = destination / "CUSTODY_VALIDATION.json"
    rows: list[dict[str, str]] = []
    for path in sorted(destination.rglob("*"), key=lambda item: item.as_posix()):
        if not path.is_file() or path in {manifest_path, validation_path}:
            continue
        relative = path.relative_to(destination).as_posix()
        if relative.startswith("checkpoints/"):
            role = "fresh_snapshot_build"
        elif "/source/source_aligned/" in relative:
            role = "editable_source"
        elif "/build_harness/" in relative:
            role = "build_dependency"
        elif relative == ".gitattributes":
            role = "byte_preservation_control"
        elif relative == "README.md":
            role = "public_scope_and_caveat"
        elif relative == "STATUS_PUBLIC.md":
            role = "public_status"
        else:
            raise RuntimeError(f"Unclassified custody file: {relative}")
        rows.append(
            {
                "path": relative,
                "bytes": str(path.stat().st_size),
                "sha256": base.sha256(path),
                "role": role,
                "status": "github_live_custody",
            }
        )
    with manifest_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=("path", "bytes", "sha256", "role", "status")
        )
        writer.writeheader()
        writer.writerows(rows)

    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    validation["package_files"] = len(rows) + 2
    validation["represented_files"] = len(rows)
    validation["manifest"] = {
        "rows": len(rows),
        "bytes": manifest_path.stat().st_size,
        "sha256": base.sha256(manifest_path),
        "exact": True,
    }
    validation_path.write_text(
        json.dumps(validation, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    args = base.parse_args()
    result = base.main()
    if result != 0:
        return result
    rewrite_controls(args.destination.resolve())
    validation = json.loads(
        (args.destination.resolve() / "CUSTODY_VALIDATION.json").read_text(
            encoding="utf-8"
        )
    )
    print(json.dumps(validation, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
