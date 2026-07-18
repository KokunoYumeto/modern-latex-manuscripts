#!/usr/bin/env python3
"""Build and validate the immutable Korean Noether P29 U01 checkpoint manifest."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "MANIFEST_U01.csv"
SUMS = ROOT / "SHA256SUMS_U01.txt"
REPORT = ROOT / "qa" / "U01_PACKAGE_VALIDATION.json"
OUTPUTS = {MANIFEST.resolve(), SUMS.resolve(), REPORT.resolve()}

ROOT_DOCS = {
    "README.md",
    "STATUS.md",
    "SOURCE_VERSION_CURSOR.md",
    "BUILD_REPORT.md",
    "RENDER_CHECK.md",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def included(path: Path) -> bool:
    resolved = path.resolve()
    if resolved in OUTPUTS or not path.is_file():
        return False
    rel = path.relative_to(ROOT).as_posix()
    name = path.name
    if "U02" in rel or "u02" in rel:
        return False
    if name.endswith((".aux", ".pyc")) or "__pycache__" in path.parts:
        return False
    if rel in ROOT_DOCS:
        return True
    if rel.startswith("source/"):
        return "U01" in name or name in {
            "Noether_Paper29_German_P31_Sealed_exact_slice.tex",
            "Noether_Paper29_German_P31_Sealed_full_control.tex",
            "Noether_Paper29_German_P31_Sealed_full_control.pdf",
        }
    if rel.startswith("ko/"):
        return "U01" in name
    if rel.startswith("qa/"):
        return "U01" in name or name == "build_manifest_u01.py"
    if rel.startswith("visual_inspection/"):
        return "U01" in name
    if rel.startswith("evidence/structural_index/"):
        return True
    if rel.startswith("evidence/difficulty_ledger/"):
        return True
    if rel.startswith("evidence/visual_evidence/"):
        return True
    if rel.startswith("evidence/") and len(path.relative_to(ROOT).parts) == 2:
        return "U01" in name
    return False


def role(rel: str) -> str:
    if rel.endswith(".schema.json"):
        return "schema"
    if "validate" in rel.lower() and rel.endswith(".py"):
        return "validator"
    if rel.endswith(".tex") and rel.startswith("ko/"):
        return "editable_korean_tex"
    if rel.endswith(".pdf") and rel.startswith("ko/"):
        return "korean_reader_pdf"
    if rel.endswith(".tex") and rel.startswith("source/"):
        return "german_source_or_control_tex"
    if rel.endswith(".pdf") and rel.startswith("source/"):
        return "german_control_pdf"
    if rel.endswith(".png"):
        return "rendered_visual_evidence"
    if rel.endswith(".log"):
        return "build_log"
    if "STRUCTURAL_INDEX" in rel:
        return "structural_index"
    if "DIFFICULTY_LEDGER" in rel:
        return "difficulty_ledger"
    if "VISUAL_EVIDENCE" in rel or "VISUAL_" in rel:
        return "visual_evidence_control"
    if "TERMINOLOGY" in rel or "CROSSWALK" in rel or "CORPUS" in rel or "ADVERSE" in rel:
        return "terminology_or_evidence_control"
    if "PARITY" in rel:
        return "source_target_parity"
    if rel.endswith(".zip"):
        return "public_payload_zip"
    if rel.endswith(".py"):
        return "reproducibility_script"
    return "documentation_or_metadata"


def disposition(rel: str) -> str:
    if "/public_payload/" in f"/{rel}" or rel.endswith("KO_NOETHER_P29_U01_VISUAL_EVIDENCE_PUBLIC_PAYLOAD_20260718.zip"):
        return "open_payload"
    if rel.startswith("visual_inspection/"):
        return "open_payload"
    if rel.startswith("evidence/visual_evidence/") and (
        "PUBLIC_SAFE" in rel or "OPEN_PAYLOAD" in rel or "VISUAL_SCOPE" in rel
    ):
        return "open_payload_metadata"
    if rel.startswith("evidence/visual_evidence/"):
        return "private_operational_or_archive_review"
    if rel.startswith("ko/") or rel.startswith("evidence/") or rel.startswith("qa/"):
        return "internal_review_candidate"
    return "source_control_or_documentation"


def run_validator(relative: str) -> dict:
    proc = subprocess.run(
        [sys.executable, str(ROOT / relative)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "path": relative,
        "exit_code": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
    }


def inspect_public_zip(zip_path: Path) -> dict:
    entries: list[dict] = []
    private_leaks: list[str] = []
    jpeg_entries: list[str] = []
    with zipfile.ZipFile(zip_path) as archive:
        for info in archive.infolist():
            entries.append({"path": info.filename, "bytes": info.file_size})
            if info.filename.lower().endswith((".jpg", ".jpeg")):
                jpeg_entries.append(info.filename)
            if info.filename.lower().endswith((".json", ".jsonl", ".csv", ".md", ".txt")):
                text = archive.read(info).decode("utf-8", errors="replace")
                if "evidence://local-user" in text or "Papors" in text or "Chatnotes" in text:
                    private_leaks.append(info.filename)
    return {
        "entry_count": len(entries),
        "uncompressed_bytes": sum(item["bytes"] for item in entries),
        "entries": entries,
        "jpeg_entries": jpeg_entries,
        "private_path_leaks": private_leaks,
    }


def main() -> int:
    files = sorted((path for path in ROOT.rglob("*") if included(path)), key=lambda path: path.relative_to(ROOT).as_posix())
    rows: list[dict] = []
    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        rows.append(
            {
                "work_unit": "P29-KO-U01",
                "relative_path": rel,
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
                "role": role(rel),
                "publication_disposition": disposition(rel),
            }
        )

    with MANIFEST.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=["work_unit", "relative_path", "bytes", "sha256", "role", "publication_disposition"],
        )
        writer.writeheader()
        writer.writerows(rows)

    SUMS.write_text(
        "".join(f"{row['sha256']}  {row['relative_path']}\n" for row in rows),
        encoding="utf-8",
        newline="\n",
    )

    validators = [
        "evidence/structural_index/validate_structural_index.py",
        "evidence/difficulty_ledger/validate_difficulty_ledger.py",
        "qa/build_validate_term_graph_parity_u01.py",
        "evidence/visual_evidence/validate_visual_evidence.py",
    ]
    validation = [run_validator(path) for path in validators]
    visual_zip = ROOT / "evidence" / "visual_evidence" / "KO_NOETHER_P29_U01_VISUAL_EVIDENCE_PUBLIC_PAYLOAD_20260718.zip"
    zip_check = inspect_public_zip(visual_zip)

    errors: list[str] = []
    if any("U02" in row["relative_path"] or "u02" in row["relative_path"] for row in rows):
        errors.append("U02 artifact leaked into U01 manifest")
    if any(item["exit_code"] != 0 for item in validation):
        errors.append("one or more U01 validators failed")
    if zip_check["jpeg_entries"]:
        errors.append("rights-blocked JPEG present in public ZIP")
    if zip_check["private_path_leaks"]:
        errors.append("private path leaked into public ZIP metadata")

    required_hashes = {
        "source/Noether_Paper29_German_P31_U01_Introduction_exact_lf.tex": "3C0A6DF0150F21977FA8FA7814C5B7D1761CE90A3A6C127AF532E110DE62AF09",
        "ko/Noether_Paper29_Korean_U01_v001.tex": "1781D71A7B4EE1643E402E72A0D9604D2DDA4CFC1A294FB594DE21299BCD338C",
        "ko/Noether_Paper29_Korean_U01_v001.pdf": "509AFF874A21B2FA0D4098330A80FF4FCB9800D84837C9BAF86A439777D2C676",
        "visual_inspection/Noether_Paper29_Korean_U01_v001.png": "1EF5FE9157DDC2CD1E54A1217142DA2EE8F8E03185C07703F0DA0BDC0E5679DD",
    }
    row_map = {row["relative_path"]: row for row in rows}
    for rel, expected in required_hashes.items():
        actual = row_map.get(rel, {}).get("sha256")
        if actual != expected:
            errors.append(f"acceptance hash mismatch: {rel}: {actual} != {expected}")

    report = {
        "work_unit": "P29-KO-U01",
        "authority_sha256": "A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F",
        "continuation_cursor": "Paper 29 exact source line 25, § 1. Das Endlichkeitskriterium",
        "manifest_rows": len(rows),
        "manifest_sha256": sha256(MANIFEST),
        "sha256s_sha256": sha256(SUMS),
        "validators": validation,
        "public_visual_zip": {
            "path": visual_zip.relative_to(ROOT).as_posix(),
            "bytes": visual_zip.stat().st_size,
            "sha256": sha256(visual_zip),
            **zip_check,
        },
        "review_boundary": {
            "internal_source_fidelity_build_extraction_visual": "pass",
            "external_korean_domain_dprk_community_review": "absent_do_not_claim",
            "source_image_redistribution_rights": "unresolved_manifest_only",
        },
        "errors": errors,
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"manifest_rows": len(rows), "errors": errors}, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
