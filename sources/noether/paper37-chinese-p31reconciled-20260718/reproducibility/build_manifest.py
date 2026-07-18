#!/usr/bin/env python3
"""Create the curated Paper 37 manifest after a clean freeze decision.

The script refuses to write MANIFEST.json or SHA256SUMS.txt unless the current
freeze report is a clean pass and a durable Chinese lane decision ID is given.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUTHORITY_SHA256 = "A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F"
LOGICAL_SOURCE_SHA256 = "68C72173E0C060BC68CB3651AF078ACE82B4D5806C8A41584632AA2BB4A9B27B"
HANS_TEX_SHA256 = "A4A0A97E548840915650FE813AED8FC120D2ABE79F3FA76F9ADF35D5EDAB1B0C"
HANT_TEX_SHA256 = "FC2493ADE14D66835C0EBAAD7C84C78AFFD33A357594F45384CD518C94F32012"

TOP = [
    "README.md",
    "STATUS.md",
    "CLAIM_AND_CURSOR.md",
    "SOURCE_CUSTODY.json",
    "SOURCE_USE.md",
    "SOURCE_CHECK.md",
    "SOURCE_UNIT_MAP.csv",
    "STRUCTURAL_INDEX.csv",
    "STRUCTURAL_INDEX.json",
    "TERMINOLOGY.md",
    "LOCALIZATION_STATUS.csv",
    "BUILD_REPORT.md",
    "RENDER_CHECK.md",
]
FOLDERS = [
    "source",
    "witness",
    "source_control",
    "zh-Hans-CN",
    "zh-Hant-controlled",
    "evidence",
    "decisions",
    "qa",
    "renders/final",
]
EXCLUDED_NAMES = {
    "MANIFEST.json",
    "SHA256SUMS.txt",
    "CHINESE_WORKER_RETURN.md",
    "ARCHIVE_HANDOFF.md",
    "CHINESE_PUBLICATION_HANDOFF.md",
}
EXCLUDED_SUFFIXES = {
    ".aux",
    ".out",
    ".toc",
    ".xdv",
    ".fls",
    ".fdb_latexmk",
    ".pyc",
    ".tmp",
    ".bak",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--decision-id",
        required=True,
        help="Latest durable freeze decision ID, for example ZH-D047.",
    )
    return parser.parse_args()


def include(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    parts_lower = {part.lower() for part in relative.parts}
    if path.name in EXCLUDED_NAMES or path.suffix.lower() in EXCLUDED_SUFFIXES:
        return False
    if "__pycache__" in parts_lower or "node_modules" in parts_lower:
        return False
    relative_posix = relative.as_posix().lower()
    if relative_posix.startswith("qa/csv_artifact_validation/previews/"):
        return False
    if "worker_return" in path.name.lower() or "archive_handoff" in path.name.lower():
        return False
    return True


args = parse_args()
if not re.fullmatch(r"ZH-D\d{3}", args.decision_id):
    raise SystemExit("--decision-id must match ZH-D followed by three digits")

freeze_path = ROOT / "qa/FREEZE_VALIDATION_REPORT.json"
if not freeze_path.is_file():
    raise SystemExit("Refusing manifest build: qa/FREEZE_VALIDATION_REPORT.json is absent")
freeze = json.loads(freeze_path.read_text(encoding="utf-8"))
if freeze.get("status") != "pass" or freeze.get("errors"):
    raise SystemExit("Refusing manifest build: freeze report is not a clean pass")
if freeze.get("authority", {}).get("sha256") != AUTHORITY_SHA256:
    raise SystemExit("Refusing manifest build: freeze report authority hash mismatch")
file_hashes = freeze.get("file_hashes", {})
if file_hashes.get("source_lf") != LOGICAL_SOURCE_SHA256:
    raise SystemExit("Refusing manifest build: logical source hash mismatch")
if file_hashes.get("hans_tex") != HANS_TEX_SHA256 or file_hashes.get("hant_tex") != HANT_TEX_SHA256:
    raise SystemExit("Refusing manifest build: accepted Hans/Hant target hash mismatch")
if freeze.get("counts", {}).get("rendered_pages") != 13:
    raise SystemExit("Refusing manifest build: freeze report does not bind 13 rendered pages")

missing_top = [name for name in TOP if not (ROOT / name).is_file()]
if missing_top:
    raise SystemExit(f"Refusing manifest build: required top-level files absent: {missing_top}")

files = [ROOT / name for name in TOP]
for folder in FOLDERS:
    base = ROOT / folder
    if not base.is_dir():
        raise SystemExit(f"Refusing manifest build: required folder absent: {folder}")
    files.extend(path for path in base.rglob("*") if path.is_file() and include(path))
files = sorted(set(files), key=lambda path: path.relative_to(ROOT).as_posix())

records = [
    {"path": path.relative_to(ROOT).as_posix(), "bytes": path.stat().st_size, "sha256": sha(path)}
    for path in files
]
manifest = {
    "schema_version": "1.0.0",
    "work_unit": "NOE-P37",
    "created_date": "2026-07-18",
    "authority_sha256": AUTHORITY_SHA256,
    "logical_source_sha256": LOGICAL_SOURCE_SHA256,
    "accepted_targets": {
        "zh-Hans-CN_tex_sha256": HANS_TEX_SHA256,
        "zh-Hant_controlled_tex_sha256": HANT_TEX_SHA256,
    },
    "freeze_report_sha256": sha(freeze_path),
    "artifact_count": len(records),
    "artifacts": records,
    "review_state": "internal_source_schema_build_render_freeze",
    "publication_state": "archive_handoff_ready_not_received",
    "decision_log": (
        "03_projects/language_management/cjk/00_lane_control/"
        f"CHINESE_DECISION_LOGBOOK_20260718.md#{args.decision_id}"
    ),
    "handoff_notes_excluded": [
        "CHINESE_WORKER_RETURN.md",
        "ARCHIVE_HANDOFF.md",
        "lane publication/archive handoff notes",
    ],
    "mechanical_exclusions": [
        "TeX auxiliary files",
        "Python caches",
        "Node dependency trees",
        "candidate render directories",
        "artifact-tool CSV preview folders",
        "MANIFEST.json and SHA256SUMS.txt from their own artifact inventory",
    ],
    "limits": [
        "no external, community, or human-expert Chinese validation",
        "no zh-Hans-SG localization or validation",
        "controlled Hant is generic and not Taiwan, Hong Kong, or Macao localization",
        "later transcription repairs are not represented as original-print defects",
        "no new original-print/body-text/formula defect found in this unit",
        "SGA held and untouched",
    ],
}
(ROOT / "MANIFEST.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
lines = [f"{row['sha256']}  {row['path']}" for row in records]
lines.append(f"{sha(ROOT / 'MANIFEST.json')}  MANIFEST.json")
(ROOT / "SHA256SUMS.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

print(json.dumps({
    "artifact_count": len(records),
    "manifest_sha256": sha(ROOT / "MANIFEST.json"),
    "sha256sums_sha256": sha(ROOT / "SHA256SUMS.txt"),
    "decision_id": args.decision_id,
}, indent=2))
