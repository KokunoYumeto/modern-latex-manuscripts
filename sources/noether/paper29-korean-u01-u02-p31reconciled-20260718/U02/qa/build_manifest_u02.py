#!/usr/bin/env python3
"""Build and validate the immutable Korean Noether P29 U02 checkpoint manifest."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "MANIFEST_U02.csv"
SUMS = ROOT / "SHA256SUMS_U02.txt"
REPORT = ROOT / "qa" / "U02_PACKAGE_VALIDATION.json"
OUTPUTS = {MANIFEST.resolve(), SUMS.resolve(), REPORT.resolve()}

ROOT_DOCS = {
    "README_U02.md",
    "STATUS_U02.md",
    "SOURCE_VERSION_CURSOR_U02.md",
    "BUILD_REPORT_U02.md",
    "RENDER_CHECK_U02.md",
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
    if "U03" in rel or "u03" in rel:
        return False
    if name.endswith((".aux", ".pyc", ".synctex.gz")) or "__pycache__" in path.parts:
        return False
    if rel.startswith("evidence/visual_evidence_u02/reconstruction/build/"):
        return False
    if rel in ROOT_DOCS:
        return True
    if rel.startswith("source/"):
        return "U02" in name or name == "Noether_Paper29_German_P31_Sealed_exact_slice.tex"
    if rel.startswith("ko/"):
        return "U02" in name
    if rel.startswith("qa/"):
        return "U02" in name or "u02" in name
    if rel.startswith("visual_inspection/"):
        return "U02" in name
    if rel.startswith("evidence/structural_index_u02/"):
        return True
    if rel.startswith("evidence/difficulty_ledger_u02/"):
        return True
    if rel.startswith("evidence/visual_evidence_u02/"):
        return True
    if rel.startswith("evidence/") and len(path.relative_to(ROOT).parts) == 2:
        return "U02" in name or "u02" in name
    return False


def role(rel: str) -> str:
    upper = rel.upper()
    if rel.endswith(".schema.json"):
        return "schema"
    if "VALIDATE" in upper and rel.endswith(".py"):
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
    if "STRUCTURAL_INDEX" in upper:
        return "structural_index"
    if "DIFFICULTY_LEDGER" in upper:
        return "difficulty_ledger"
    if "VISUAL_EVIDENCE" in upper or "VISUAL_" in upper or "RECONSTRUCTION" in upper:
        return "visual_evidence_control"
    if any(token in upper for token in ("TERMINOLOGY", "CROSSWALK", "CORPUS", "ADVERSE")):
        return "terminology_or_evidence_control"
    if "PARITY" in upper:
        return "source_target_parity"
    if rel.endswith(".zip"):
        return "public_payload_zip"
    if rel.endswith(".py"):
        return "reproducibility_script"
    return "documentation_or_metadata"


def disposition(rel: str) -> str:
    upper = rel.upper()
    if "/PUBLIC_PAYLOAD/" in f"/{upper}" or rel.lower().endswith(".zip"):
        return "open_payload"
    if rel.startswith("visual_inspection/"):
        return "open_payload"
    if rel.startswith("evidence/visual_evidence_u02/") and (
        "PUBLIC_SAFE" in upper or "OPEN_PAYLOAD" in upper or "VISUAL_SCOPE" in upper
    ):
        return "open_payload_metadata"
    if rel.startswith("evidence/visual_evidence_u02/reconstruction/"):
        return "project_generated_reconstruction_evidence"
    if rel.startswith("evidence/visual_evidence_u02/"):
        return "private_operational_or_archive_review"
    if rel.startswith("ko/") or rel.startswith("evidence/") or rel.startswith("qa/"):
        return "internal_review_candidate"
    return "source_control_or_documentation"


def run_validator(relative: str) -> dict:
    path = ROOT / relative
    if not path.is_file():
        return {
            "path": relative,
            "exit_code": 127,
            "stdout": "",
            "stderr": "validator missing",
        }
    proc = subprocess.run(
        [sys.executable, str(path)],
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
    forbidden_source_images: list[str] = []
    with zipfile.ZipFile(zip_path) as archive:
        for info in archive.infolist():
            entries.append({"path": info.filename, "bytes": info.file_size})
            if info.filename.lower().endswith((".jpg", ".jpeg", ".tif", ".tiff")):
                forbidden_source_images.append(info.filename)
            if info.filename.lower().endswith((".json", ".jsonl", ".csv", ".md", ".txt", ".tex")):
                content = archive.read(info).decode("utf-8", errors="replace")
                if "evidence://local-user" in content or "Papors" in content or "Chatnotes" in content:
                    private_leaks.append(info.filename)
    return {
        "entry_count": len(entries),
        "uncompressed_bytes": sum(item["bytes"] for item in entries),
        "entries": entries,
        "forbidden_source_image_entries": forbidden_source_images,
        "private_path_leaks": private_leaks,
    }


def main() -> int:
    validators = [
        "qa/validate_authority_u02.py",
        "evidence/structural_index_u02/validate_structural_index.py",
        "evidence/difficulty_ledger_u02/validate_difficulty_ledger.py",
        "qa/build_validate_term_graph_parity_u02.py",
        "evidence/visual_evidence_u02/validate_visual_evidence.py",
    ]
    validation = [run_validator(path) for path in validators]

    files = sorted(
        (path for path in ROOT.rglob("*") if included(path)),
        key=lambda path: path.relative_to(ROOT).as_posix(),
    )
    rows: list[dict] = []
    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        rows.append(
            {
                "work_unit": "P29-KO-U02",
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

    errors: list[str] = []
    if any("U03" in row["relative_path"] or "u03" in row["relative_path"] for row in rows):
        errors.append("U03 artifact leaked into U02 manifest")
    if any(item["exit_code"] != 0 for item in validation):
        errors.append("one or more U02 validators failed or are missing")

    zip_candidates = sorted((ROOT / "evidence" / "visual_evidence_u02").glob("*.zip"))
    zip_details: dict | None = None
    if len(zip_candidates) != 1:
        errors.append(f"expected exactly one U02 visual public ZIP, found {len(zip_candidates)}")
    else:
        visual_zip = zip_candidates[0]
        zip_check = inspect_public_zip(visual_zip)
        zip_details = {
            "path": visual_zip.relative_to(ROOT).as_posix(),
            "bytes": visual_zip.stat().st_size,
            "sha256": sha256(visual_zip),
            **zip_check,
        }
        if zip_check["forbidden_source_image_entries"]:
            errors.append("rights-blocked source image present in public ZIP")
        if zip_check["private_path_leaks"]:
            errors.append("private path leaked into public ZIP metadata")

    required_hashes = {
        "source/Noether_Paper29_German_P31_U02_Rationalbasis_exact_lf.tex": "B7EF88537BCD90D0408B3D1942DA410410FE45E79DD457B2DF6DFA2D4929DCAC",
        "ko/Noether_Paper29_Korean_U02_v001.tex": "B694D05E57B58E1B0373D976356E6B3B3F4883D7CC9398081DB12111877B6A7C",
        "ko/Noether_Paper29_Korean_U02_v001.pdf": "EE0A0ED2E150A5EC48945EA7E47C3F394667F288FF5E933BB00DDF193FBE8988",
        "visual_inspection/Noether_Paper29_Korean_U02_v001.png": "F2F772AE57371BA57020C4E816203D3DC154EB46186457846AE2DEBCBEC1FD9E",
        "evidence/structural_index_u02/STRUCTURAL_INDEX.jsonl": "F6954C84D72F3E5C02DAEF3B7B1BFF239587A1ECEEA6D7472B8A6EC00C96B60A",
        "evidence/difficulty_ledger_u02/DIFFICULTY_LEDGER.jsonl": "DC61B76D9A1F6DBA940CCC5D5219468473597304E3C89D231FFF89C41E7903B0",
    }
    row_map = {row["relative_path"]: row for row in rows}
    for rel, expected in required_hashes.items():
        actual = row_map.get(rel, {}).get("sha256")
        if actual != expected:
            errors.append(f"acceptance hash mismatch: {rel}: {actual} != {expected}")

    u01_manifest = ROOT / "MANIFEST_U01.csv"
    u01_report = ROOT / "qa" / "U01_PACKAGE_VALIDATION.json"
    u01_immutability = {
        "manifest_sha256": sha256(u01_manifest),
        "expected_manifest_sha256": "0BCFDC8D74380C71B929A9B5CE599562ADBD47585F9FB7EF7A10367CC37A670A",
        "package_report_sha256": sha256(u01_report),
        "expected_package_report_sha256": "979D46C353A50982A1A0D024455EE4A8CEDCF5FCC06212DF73D874CE4B10CE00",
    }
    if u01_immutability["manifest_sha256"] != u01_immutability["expected_manifest_sha256"]:
        errors.append("sealed U01 manifest changed")
    if u01_immutability["package_report_sha256"] != u01_immutability["expected_package_report_sha256"]:
        errors.append("sealed U01 package report changed")

    report = {
        "work_unit": "P29-KO-U02",
        "authority_sha256": "A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F",
        "source_unit_sha256": "B7EF88537BCD90D0408B3D1942DA410410FE45E79DD457B2DF6DFA2D4929DCAC",
        "continuation_cursor": (
            "Paper 29 exact full-source line 41, 2. \\srcspaced{Beweis des Endlichkeitskriteriums.}; "
            "line 40 is a blank separator"
        ),
        "manifest_rows": len(rows),
        "manifest_sha256": sha256(MANIFEST),
        "sha256s_sha256": sha256(SUMS),
        "validators": validation,
        "public_visual_zip": zip_details,
        "u01_immutability": u01_immutability,
        "review_boundary": {
            "internal_source_fidelity_build_extraction_visual": "pass",
            "independent_internal_model_fidelity_review": "pass_no_substantive_or_structural_defect",
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
