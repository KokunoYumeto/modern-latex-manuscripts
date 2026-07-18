#!/usr/bin/env python3
"""Build and validate the Korean Noether P29 U03 checkpoint manifest."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "MANIFEST_U03.csv"
SUMS = ROOT / "SHA256SUMS_U03.txt"
REPORT = ROOT / "qa" / "U03_PACKAGE_VALIDATION.json"
OUTPUTS = {MANIFEST.resolve(), SUMS.resolve(), REPORT.resolve()}
ROOT_DOCS = {
    "README_U03.md", "STATUS_U03.md", "SOURCE_VERSION_CURSOR_U03.md", "SOURCE_CHECK_U03.md",
    "BUILD_REPORT_U03.md", "RENDER_CHECK_U03.md", "REVIEW_QUESTIONS_U03.md", "WORKER_RETURN_U03.md"
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def included(path: Path) -> bool:
    if not path.is_file() or path.resolve() in OUTPUTS:
        return False
    rel = path.relative_to(ROOT).as_posix()
    name = path.name
    if "U04" in rel or "u04" in rel:
        return False
    if name.endswith((".aux", ".pyc", ".synctex.gz")) or "__pycache__" in path.parts:
        return False
    if rel in ROOT_DOCS:
        return True
    if rel.startswith("source/"):
        return "U03" in name or name == "Noether_Paper29_German_P31_Sealed_exact_slice.tex"
    if rel.startswith("ko/"):
        return "U03" in name
    if rel.startswith("qa/"):
        return "U03" in name or "u03" in name
    if rel.startswith("visual_inspection/"):
        return "U03" in name
    if rel.startswith("evidence/structural_index_u03/"):
        return True
    if rel.startswith("evidence/difficulty_ledger_u03/"):
        return True
    if rel.startswith("evidence/visual_evidence_u03/"):
        return True
    if rel.startswith("evidence/") and len(path.relative_to(ROOT).parts) == 2:
        return "U03" in name or "u03" in name
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
    if rel.startswith("evidence/visual_evidence_u03/") and (
        "PUBLIC_SAFE" in upper or "OPEN_PAYLOAD" in upper or "VISUAL_SCOPE" in upper
    ):
        return "open_payload_metadata"
    if rel.startswith("evidence/visual_evidence_u03/reconstruction/"):
        return "project_generated_reconstruction_evidence"
    if rel.startswith("evidence/visual_evidence_u03/"):
        return "private_operational_or_archive_review"
    if rel.startswith(("ko/", "evidence/", "qa/")):
        return "internal_review_candidate"
    return "source_control_or_documentation"


def run_validator(relative: str) -> dict:
    path = ROOT / relative
    if not path.is_file():
        return {"path": relative, "exit_code": 127, "stdout": "", "stderr": "validator missing"}
    proc = subprocess.run([sys.executable, str(path)], cwd=ROOT, text=True, capture_output=True, check=False)
    return {"path": relative, "exit_code": proc.returncode, "stdout": proc.stdout.strip(), "stderr": proc.stderr.strip()}


def inspect_public_zip(path: Path) -> dict:
    forbidden: list[str] = []
    leaks: list[str] = []
    entries: list[dict] = []
    with zipfile.ZipFile(path) as archive:
        for info in archive.infolist():
            entries.append({"path": info.filename, "bytes": info.file_size})
            if info.filename.lower().endswith((".jpg", ".jpeg", ".tif", ".tiff")):
                forbidden.append(info.filename)
            if info.filename.lower().endswith((".json", ".jsonl", ".csv", ".md", ".txt", ".tex")):
                content = archive.read(info).decode("utf-8", errors="replace")
                if "HOST_USER_PATH_MARKER" in content or "HOST_USER_PATH_MARKER" in content or "Papors" in content or "Chatnotes" in content:
                    leaks.append(info.filename)
    return {
        "entry_count": len(entries), "uncompressed_bytes": sum(item["bytes"] for item in entries),
        "entries": entries, "forbidden_source_image_entries": forbidden, "private_path_leaks": leaks
    }


def main() -> int:
    validators = [
        "qa/validate_authority_u03.py",
        "evidence/structural_index_u03/validate_structural_index.py",
        "evidence/difficulty_ledger_u03/validate_difficulty_ledger.py",
        "qa/build_validate_term_graph_parity_u03.py",
        "evidence/visual_evidence_u03/validate_visual_evidence.py"
    ]
    validation = [run_validator(path) for path in validators]
    files = sorted((path for path in ROOT.rglob("*") if included(path)), key=lambda path: path.relative_to(ROOT).as_posix())
    rows = []
    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        rows.append({
            "work_unit": "P29-KO-U03", "relative_path": rel, "bytes": path.stat().st_size,
            "sha256": sha256(path), "role": role(rel), "publication_disposition": disposition(rel)
        })
    with MANIFEST.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["work_unit", "relative_path", "bytes", "sha256", "role", "publication_disposition"])
        writer.writeheader()
        writer.writerows(rows)
    SUMS.write_text("".join(f"{row['sha256']}  {row['relative_path']}\n" for row in rows), encoding="utf-8", newline="\n")

    errors: list[str] = []
    if any("U04" in row["relative_path"] or "u04" in row["relative_path"] for row in rows):
        errors.append("U04 artifact leaked into U03 manifest")
    if any(item["exit_code"] != 0 for item in validation):
        errors.append("one or more U03 validators failed or are missing")
    if any(row["relative_path"].lower().endswith((".jpg", ".jpeg", ".tif", ".tiff")) for row in rows):
        errors.append("rights-blocked source raster leaked into U03 package manifest")

    visual_zip = ROOT / "evidence" / "visual_evidence_u03" / "KO_NOETHER_P29_U03_VISUAL_EVIDENCE_PUBLIC_PAYLOAD_20260718.zip"
    zip_check = inspect_public_zip(visual_zip)
    zip_details = {"path": visual_zip.relative_to(ROOT).as_posix(), "bytes": visual_zip.stat().st_size, "sha256": sha256(visual_zip), **zip_check}
    if zip_check["forbidden_source_image_entries"]:
        errors.append("rights-blocked source image present in public ZIP")
    if zip_check["private_path_leaks"]:
        errors.append("private path leaked into public ZIP metadata")

    required_hashes = {
        "source/Noether_Paper29_German_P31_U03_FinitenessCriterionProofSetup_exact_lf.tex": "1CD2F142F472BE2A590EC8AACA45CEB49966A09FE803CC410D138B3F7BDE7458",
        "ko/Noether_Paper29_Korean_U03_v001.tex": "0DFEE79E2DF3A81005BDAF8488E108D9E324703133D0B9548F5A54933975CC60",
        "ko/Noether_Paper29_Korean_U03_v001.pdf": "4E6DEC776EE572EFCC97138F21D0AE98ABA5A8F3DD4E3362E1BD2808A23D7A19",
        "visual_inspection/Noether_Paper29_Korean_U03_v001.png": "42E78806891372C91FDB089A5374103B8BD8E4E7BECFC14D1C94C719F7911579",
        "evidence/structural_index_u03/STRUCTURAL_INDEX.jsonl": "B9301BEA16DC6D6FC0B0425080916A29FE0AC011C23CA0B2236675B887D0E380",
        "evidence/difficulty_ledger_u03/DIFFICULTY_LEDGER.jsonl": "90EDE7EA9052680E296A44BFA6445A3148B83C0F3BBCCDD6EA3936DEB4EDECC5",
        "evidence/visual_evidence_u03/VISUAL_EVIDENCE_INDEX.jsonl": "927BA1320175865ED838F22EBE6030581D8FE708E33C56B93660A8773EB2CB6E",
        "evidence/visual_evidence_u03/KO_NOETHER_P29_U03_VISUAL_EVIDENCE_PUBLIC_PAYLOAD_20260718.zip": "71C211021F4ED2D3C422D88E2742B1B913096E2EA8D7A72C09FA8FDFAB7EE0AD"
    }
    row_map = {row["relative_path"]: row for row in rows}
    for rel, expected in required_hashes.items():
        actual = row_map.get(rel, {}).get("sha256")
        if actual != expected:
            errors.append(f"acceptance hash mismatch: {rel}: {actual} != {expected}")

    immutability = {
        "u01_manifest": {"actual": sha256(ROOT / "MANIFEST_U01.csv"), "expected": "0BCFDC8D74380C71B929A9B5CE599562ADBD47585F9FB7EF7A10367CC37A670A"},
        "u01_report": {"actual": sha256(ROOT / "qa" / "U01_PACKAGE_VALIDATION.json"), "expected": "979D46C353A50982A1A0D024455EE4A8CEDCF5FCC06212DF73D874CE4B10CE00"},
        "u02_manifest": {"actual": sha256(ROOT / "MANIFEST_U02.csv"), "expected": "1C3173028AE2F8E583580B19C44B4D34BD5BC14AF5A27667D9BCDB1B0C9DCFEE"},
        "u02_report": {"actual": sha256(ROOT / "qa" / "U02_PACKAGE_VALIDATION.json"), "expected": "9D1417B58D602C7A1B275EF5A92157C46070DCA6DFB86C83DA5029FBE3BF2E05"}
    }
    for label, value in immutability.items():
        if value["actual"] != value["expected"]:
            errors.append(f"sealed {label} changed")

    report = {
        "schema_version": "1.0.0", "work_unit": "P29-KO-U03",
        "authority_sha256": "A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F",
        "source_unit_sha256": "1CD2F142F472BE2A590EC8AACA45CEB49966A09FE803CC410D138B3F7BDE7458",
        "continuation_cursor": "Full-P29 line 46 blank; next substantive line 47.",
        "manifest_rows": len(rows), "manifest_sha256": sha256(MANIFEST), "sha256s_sha256": sha256(SUMS),
        "validators": validation, "public_visual_zip": zip_details, "prior_unit_immutability": immutability,
        "latest_ids": {
            "decision": "CJK-KO-P29-012", "structural": "NOE-P29-KO-U03-STEP-007",
            "difficulty": "CJK-KO-P29-U03-HARD-008", "terminology": "KO-P29-U03-D014",
            "visual": "VE-LOSS-P29-KO-U03-001"
        },
        "review_boundary": {
            "internal_source_fidelity_build_extraction_visual": "pass",
            "independent_internal_model_fidelity_review": "pass_after_refinement",
            "external_korean_domain_dprk_community_review": "absent_do_not_claim",
            "source_image_redistribution_rights": "unresolved_manifest_only"
        },
        "errors": errors
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"manifest_rows": len(rows), "manifest_sha256": report["manifest_sha256"], "errors": errors}, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
