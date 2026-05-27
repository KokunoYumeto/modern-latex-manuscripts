#!/usr/bin/env python3
"""Stage Zenodo v22: v21 carried forward plus SGA batch 004 and reader QC.

This keeps availability high: demoted top-level reader PDFs remain preserved in
artifact/history material while the public reader surface gets cleaner.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
import subprocess
import zipfile
from datetime import date, datetime
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
V21_UPLOAD = PROJECT_ROOT / "release_candidates" / "zenodo_v21_cleanup9_non_eu" / "upload"
OUT_ROOT = PROJECT_ROOT / "release_candidates" / "zenodo_v22_sga_batch004_reader_qc"
UPLOAD = OUT_ROOT / "upload"
REPORTS = OUT_ROOT / "reports"
WORK = OUT_ROOT / "work"
ZENODO = PROJECT_ROOT / "zenodo"

SGA_BATCH_ROOT = Path.home() / "Downloads" / "SGA" / "SGA_TRANSLATION_BATCHES_CURRENT"
SGA_BATCH_ZIP = SGA_BATCH_ROOT / "zips" / "sga_translation_batch_004_cumulative_sga4_expose_I_through_8_8_with_all_rendered_pdfs.zip"
SGA_BATCH_EXTRACTED = SGA_BATCH_ROOT / "extracted_latest_cumulative"
SGA_BATCH_READER_PDF = SGA_BATCH_ROOT / "combined_reader_pdfs" / "SGA4_Expose_I_sections_0_to_8_8_cumulative_en.pdf"
SGA_BATCH_SUMMARY = SGA_BATCH_ROOT / "SGA_TRANSLATION_BATCHES_CURRENT_summary.json"

V21_READER_AUDIT = Path("C:/tmp/v21_reader_pdf_surface_audit_short")

DEMOTED_TOP_LEVEL_PDFS = {
    "00_pdf__non_eu__karpinski_robert_of_chester_latin_translation_1915.pdf": (
        "Demoted from reader-facing surface in v22 after display audit. The PDF opens and has extractable text, "
        "but sampled rendering showed many near-blank/cropped pages, so it is better preserved inside artifacts "
        "than advertised as a clean top-level reader PDF."
    ),
}


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fields is None:
        fields = sorted({key for row in rows for key in row})
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def run_text(cmd: list[str], timeout: int = 180) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout)


def pdf_info(path: Path) -> dict[str, Any]:
    proc = run_text(["pdfinfo", str(path)], 120)
    text_proc = run_text(["pdftotext", "-f", "1", "-l", "3", "-layout", str(path), "-"], 180)
    pages = ""
    if proc.returncode == 0:
        match = re.search(r"^Pages:\s+(\d+)", proc.stdout, re.M)
        pages = match.group(1) if match else ""
    return {
        "filename": path.name,
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
        "pdfinfo_ok": proc.returncode == 0,
        "pdftotext_ok": text_proc.returncode == 0,
        "pages": pages,
        "sample_text_chars": len(text_proc.stdout) if text_proc.returncode == 0 else 0,
        "error_tail": (proc.stderr + text_proc.stderr)[-800:] if proc.returncode != 0 or text_proc.returncode != 0 else "",
    }


def copy_v21_surface() -> dict[str, Any]:
    if not V21_UPLOAD.exists():
        raise SystemExit(f"Missing v21 upload surface: {V21_UPLOAD}")
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    UPLOAD.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)
    WORK.mkdir(parents=True, exist_ok=True)

    demoted_rows: list[dict[str, Any]] = []
    old_80: list[Path] = []
    copied = 0
    skipped_full_repo = 0
    for src in sorted(V21_UPLOAD.iterdir(), key=lambda p: p.name):
        if not src.is_file():
            continue
        if src.name.startswith("99_full_repo__"):
            skipped_full_repo += 1
            continue
        if src.name in DEMOTED_TOP_LEVEL_PDFS:
            row = {
                "filename": src.name,
                "bytes": src.stat().st_size,
                "sha256": sha256(src),
                "reason": DEMOTED_TOP_LEVEL_PDFS[src.name],
            }
            demoted_rows.append(row)
            continue
        if src.name.startswith("80_"):
            old_80.append(src)
            continue
        shutil.copy2(src, UPLOAD / src.name)
        copied += 1

    history_zip = UPLOAD / "80_metadata__release_history_and_audits_through_v21.zip"
    with zipfile.ZipFile(history_zip, "w", compression=zipfile.ZIP_DEFLATED, allowZip64=True) as zf:
        for src in old_80:
            zf.write(src, f"v21_individual_80_files/{src.name}")
        extras = [
            ZENODO / "zenodo_v21_public_check_summary.json",
            ZENODO / "metadata_v21_cleanup9_non_eu.json",
            PROJECT_ROOT / "zenodo" / "v21_cleanup9_non_eu_publish" / "zenodo_v21_remote_file_check_summary_stdout.json",
        ]
        for src in extras:
            if src.exists():
                zf.write(src, f"v21_publication_checks/{src.name}")
        for row in demoted_rows:
            src = V21_UPLOAD / str(row["filename"])
            if src.exists():
                zf.write(src, f"demoted_top_level_reader_pdfs/{src.name}")
    with zipfile.ZipFile(history_zip, "r") as zf:
        bad = zf.testzip()
    if bad:
        raise RuntimeError(f"Bad member in v21 history ZIP: {bad}")

    write_csv(REPORTS / "v22_demoted_top_level_reader_pdfs.csv", demoted_rows, ["filename", "bytes", "sha256", "reason"])
    return {
        "v21_files_copied_directly": copied,
        "v21_80_files_packed": len(old_80),
        "v21_full_repo_files_skipped_for_rebuild": skipped_full_repo,
        "v22_top_level_reader_pdfs_demoted": len(demoted_rows),
        "demoted_top_level_reader_pdfs": demoted_rows,
        "history_zip": history_zip.name,
        "history_zip_bytes": history_zip.stat().st_size,
        "history_zip_sha256": sha256(history_zip),
    }


def add_sga_batch004_to_artifact() -> dict[str, Any]:
    old_artifact = V21_UPLOAD / "10_artifacts__sga_translation_handoff_1_7.zip"
    new_artifact = UPLOAD / old_artifact.name
    if not old_artifact.exists():
        raise SystemExit(f"Missing v21 SGA artifact: {old_artifact}")
    for required in [SGA_BATCH_ZIP, SGA_BATCH_EXTRACTED, SGA_BATCH_READER_PDF]:
        if not required.exists():
            raise SystemExit(f"Missing SGA batch 004 input: {required}")

    shutil.copy2(old_artifact, new_artifact)
    add_prefix = "06_NEW_SGA_TRANSLATION_BATCHES"
    extracted_prefix = f"{add_prefix}/extracted_sga_translation_batch_004_cumulative_sga4_expose_I_through_8_8_with_all_rendered_pdfs"
    added_rows: list[dict[str, Any]] = []

    with zipfile.ZipFile(new_artifact, "a", compression=zipfile.ZIP_DEFLATED, allowZip64=True) as zf:
        def add_file(src: Path, arcname: str) -> None:
            zf.write(src, arcname)
            added_rows.append({"archive_path": arcname, "bytes": src.stat().st_size, "sha256": sha256(src)})

        add_file(SGA_BATCH_ZIP, f"{add_prefix}/{SGA_BATCH_ZIP.name}")
        for src in sorted(SGA_BATCH_EXTRACTED.rglob("*")):
            if src.is_file():
                rel = src.relative_to(SGA_BATCH_EXTRACTED).as_posix()
                add_file(src, f"{extracted_prefix}/{rel}")
        if SGA_BATCH_SUMMARY.exists():
            add_file(SGA_BATCH_SUMMARY, f"{add_prefix}/batch_004_local_handoff_summary.json")
        readme = WORK / "README_BATCH_004_ADDITION.md"
        readme.write_text(
            "SGA batch 004 addition\n\n"
            "This v22 artifact addition includes the cumulative SGA4 Expose I English translation through sections 8.7-8.8, "
            "the rendered cumulative PDFs, TeX sources, render logs/check images, existing SGA1-3 English snapshots carried by the batch, "
            "and the current SGA5 Expose I section 1 draft material.\n",
            encoding="utf-8",
        )
        add_file(readme, f"{add_prefix}/README_BATCH_004_ADDITION.md")

    with zipfile.ZipFile(new_artifact, "r") as zf:
        bad = zf.testzip()
    if bad:
        raise RuntimeError(f"Bad member in updated SGA artifact ZIP: {bad}")
    write_csv(REPORTS / "v22_sga_batch004_artifact_added_files.csv", added_rows, ["archive_path", "bytes", "sha256"])
    return {
        "updated_sga_artifact": new_artifact.name,
        "updated_sga_artifact_bytes": new_artifact.stat().st_size,
        "updated_sga_artifact_sha256": sha256(new_artifact),
        "added_files_inside_sga_artifact": len(added_rows),
        "added_bytes_inside_sga_artifact": sum(int(row["bytes"]) for row in added_rows),
    }


def add_top_level_sga_reader_pdf() -> dict[str, Any]:
    dest = UPLOAD / "00_pdf__sga4_expose_i_english_translation_current_through_8_8.pdf"
    shutil.copy2(SGA_BATCH_READER_PDF, dest)
    row = pdf_info(dest)
    row.update({"source": str(SGA_BATCH_READER_PDF), "role": "sga4_english_translation_current_reader_pdf"})
    write_csv(REPORTS / "v22_added_top_level_reader_pdfs.csv", [row])
    return row


def add_reader_audit_zip(carry: dict[str, Any]) -> dict[str, Any]:
    audit_zip = UPLOAD / "80_audit__v22_reader_surface_qc_and_demotions.zip"
    sources = [
        V21_READER_AUDIT / "v21_reader_pdf_surface.csv",
        V21_READER_AUDIT / "v21_reader_pdf_surface_sample_page_metrics.csv",
        V21_READER_AUDIT / "audit_stdout.json",
        V21_READER_AUDIT / "sample_pages" / "00_pdf__non_eu__karpinski_robert_of_chester_latin_translation_1915" / "contact__00_pdf__non_eu__karpinski_robert_of_chester_latin_translation_1915.jpg",
        V21_READER_AUDIT / "sample_pages" / "00_pdf__non_eu__qin_jiushao_shuxue_jiuzhang" / "contact__00_pdf__non_eu__qin_jiushao_shuxue_jiuzhang.jpg",
        REPORTS / "v22_demoted_top_level_reader_pdfs.csv",
    ]
    rows = []
    csv_path = V21_READER_AUDIT / "v21_reader_pdf_surface.csv"
    if csv_path.exists():
        with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
    hold_rows = [row for row in rows if row.get("verdict") != "clean_candidate"]
    summary = {
        "generated_at": now_iso(),
        "source_audit_dir": str(V21_READER_AUDIT),
        "audited_top_level_pdf_count": len(rows),
        "clean_candidate_count": sum(1 for row in rows if row.get("verdict") == "clean_candidate"),
        "hold_count_before_v22_demotions": len(hold_rows),
        "hold_filenames_before_v22_demotions": [row.get("pdf") for row in hold_rows],
        "v22_demoted_top_level_reader_pdfs": carry["demoted_top_level_reader_pdfs"],
        "v22_kept_with_attention": [
            {
                "filename": "00_pdf__non_eu__qin_jiushao_shuxue_jiuzhang.pdf",
                "reason": "Display audit had two renderer hiccups, but the contact sheet and text/content metrics look usable for a current working reader PDF.",
            }
        ],
    }
    summary_path = REPORTS / "v22_reader_surface_qc_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    sources.append(summary_path)
    demoted_pdf = V21_UPLOAD / "00_pdf__non_eu__karpinski_robert_of_chester_latin_translation_1915.pdf"
    if demoted_pdf.exists():
        sources.append(demoted_pdf)

    with zipfile.ZipFile(audit_zip, "w", compression=zipfile.ZIP_DEFLATED, allowZip64=True) as zf:
        for src in sources:
            if src.exists():
                if src == demoted_pdf:
                    arcname = f"demoted_top_level_reader_pdfs/{src.name}"
                else:
                    arcname = src.name
                zf.write(src, arcname)
    with zipfile.ZipFile(audit_zip, "r") as zf:
        bad = zf.testzip()
    if bad:
        raise RuntimeError(f"Bad member in reader audit ZIP: {bad}")
    return {
        "reader_audit_zip": audit_zip.name,
        "reader_audit_zip_bytes": audit_zip.stat().st_size,
        "reader_audit_zip_sha256": sha256(audit_zip),
        **summary,
    }


def copy_v22_reports_to_upload(summary: dict[str, Any]) -> None:
    summary_path = REPORTS / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    shutil.copy2(summary_path, UPLOAD / "80_metadata__v22_sga_batch004_reader_qc_summary.json")
    readme = f"""Zenodo v22 staging note: SGA batch 004 plus reader-surface QC

Generated: {summary['generated_at']}

This candidate carries v21 forward without dropping whole works. It adds the
current SGA translation batch 004 into 10_artifacts__sga_translation_handoff_1_7.zip,
adds a top-level reader PDF for the cumulative SGA4 Expose I English translation
through sections 8.7-8.8, and records the v21 reader-surface display audit.

The former individual v21 80_* files are preserved together inside
80_metadata__release_history_and_audits_through_v21.zip so the Zenodo front page
stays under the 100-file limit while retaining release history.

Demoted from top-level reader PDFs:
- 00_pdf__non_eu__karpinski_robert_of_chester_latin_translation_1915.pdf, because
  sampled rendering showed many near-blank/cropped pages. The material remains
  preserved inside the cleanup 9 artifact and inside the v22 reader audit ZIP.

Kept with attention:
- 00_pdf__non_eu__qin_jiushao_shuxue_jiuzhang.pdf. The automated renderer hit
  two sample-page hiccups, but the contact sheet and text/content metrics look
  usable as a current working reader PDF.
"""
    (UPLOAD / "80_README_v22_sga_batch004_reader_qc.txt").write_text(readme, encoding="utf-8")


def rebuild_full_repo_zip() -> Path:
    dest = UPLOAD / "99_full_repo__modern_latex_corpus_v22_sga_batch004_reader_qc.zip"
    if dest.exists():
        dest.unlink()
    with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED, allowZip64=True) as zf:
        for path in sorted(UPLOAD.iterdir(), key=lambda p: p.name):
            if path.is_file() and path != dest:
                zf.write(path, path.name)
    with zipfile.ZipFile(dest, "r") as zf:
        bad = zf.testzip()
    if bad:
        raise RuntimeError(f"Bad member in full-repo ZIP: {bad}")
    return dest


def upload_manifest() -> list[dict[str, Any]]:
    rows = []
    for path in sorted(UPLOAD.iterdir(), key=lambda p: p.name):
        if path.is_file():
            rows.append({"filename": path.name, "bytes": path.stat().st_size, "sha256": sha256(path)})
    write_csv(REPORTS / "zenodo_v22_upload_files.csv", rows, ["filename", "bytes", "sha256"])
    (REPORTS / "zenodo_v22_upload_files.txt").write_text("\n".join(str(UPLOAD / row["filename"]) for row in rows) + "\n", encoding="utf-8")
    return rows


def metadata_json(summary: dict[str, Any]) -> dict[str, Any]:
    metadata = json.loads((ZENODO / "metadata_v21_cleanup9_non_eu.json").read_text(encoding="utf-8"))
    description = metadata["description"]
    description = description.replace(
        "SGA 4 has Orgogozo/Laszlo French PDF/TeX sources plus new cumulative English translation batches for Expose I through sections 6-7.",
        "SGA 4 has Orgogozo/Laszlo French PDF/TeX sources plus cumulative English translation batches for Expose I through sections 8.7-8.8.",
    )
    description = description.replace(
        "the v20 added SGA translation ZIPs also passed ZIP integrity checks before inclusion.",
        "the v20/v22 added SGA translation ZIPs also passed ZIP integrity checks before inclusion.",
    )
    v22_para = """
<p><strong>What changed in v22 while preserving availability:</strong> the v21 corpus was copied forward. One top-level reader PDF, <code>00_pdf__non_eu__karpinski_robert_of_chester_latin_translation_1915.pdf</code>, was demoted after the display audit showed many near-blank/cropped sampled pages; it remains preserved inside the cleanup 9 artifact and the v22 reader-audit ZIP. The SGA handoff artifact was updated with SGA translation batch 004, including cumulative SGA4 Expose I English translation material through sections 8.7-8.8, rendered PDFs, TeX sources, render checks, and current SGA5 Expose I section 1 draft material. This version also adds <code>00_pdf__sga4_expose_i_english_translation_current_through_8_8.pdf</code> as a reader-facing current English translation PDF. The v21 reader-surface audit reported <code>[##########] 56/58</code> clean candidates before v22 demotion; the remaining Qin Jiushao PDF is kept as usable working material with an attention note.</p>
"""
    description = description.replace("<p><strong>How the files are organized:</strong></p>", v22_para + "\n<p><strong>How the files are organized:</strong></p>")
    metadata["publication_date"] = date.today().isoformat()
    metadata["version"] = "2026-05-27 v22 SGA batch 004 and reader QC"
    metadata["description"] = description
    metadata["notes"] = (
        "Public working corpus for modern LaTeX editions of older mathematics and physics manuscripts. "
        "Version 22 carries v21 forward, adds SGA translation batch 004 to the SGA handoff artifact, "
        "adds a current SGA4 Expose I English reader PDF through sections 8.7-8.8, and demotes one weak Karpinski top-level PDF while preserving it in artifacts."
    )
    keywords = list(metadata.get("keywords", []))
    for keyword in ["SGA4 English translation", "reader-surface audit", "quality control"]:
        if keyword not in keywords:
            keywords.append(keyword)
    metadata["keywords"] = keywords
    return metadata


def main() -> int:
    carry = copy_v21_surface()
    sga = add_sga_batch004_to_artifact()
    top_pdf = add_top_level_sga_reader_pdf()
    reader_audit = add_reader_audit_zip(carry)

    preliminary = {
        "generated_at": now_iso(),
        "carry_forward": carry,
        "sga_batch004": sga,
        "added_reader_pdf": top_pdf,
        "reader_surface_qc": reader_audit,
    }
    copy_v22_reports_to_upload(preliminary)
    full_repo = rebuild_full_repo_zip()
    upload_rows = upload_manifest()

    summary = {
        **preliminary,
        "upload_file_count": len(upload_rows),
        "upload_total_bytes": sum(int(row["bytes"]) for row in upload_rows),
        "upload_pdf_count": sum(1 for row in upload_rows if row["filename"].startswith("00_pdf__") and row["filename"].endswith(".pdf")),
        "upload_artifact_zip_count": sum(1 for row in upload_rows if row["filename"].startswith("10_artifacts__") and row["filename"].endswith(".zip")),
        "full_repo_zip": str(full_repo),
        "full_repo_zip_bytes": full_repo.stat().st_size,
        "full_repo_zip_sha256": sha256(full_repo),
        "over_100_files": len(upload_rows) > 100,
    }
    copy_v22_reports_to_upload(summary)
    full_repo = rebuild_full_repo_zip()
    upload_rows = upload_manifest()
    summary["upload_file_count"] = len(upload_rows)
    summary["upload_total_bytes"] = sum(int(row["bytes"]) for row in upload_rows)
    summary["upload_pdf_count"] = sum(1 for row in upload_rows if row["filename"].startswith("00_pdf__") and row["filename"].endswith(".pdf"))
    summary["upload_artifact_zip_count"] = sum(1 for row in upload_rows if row["filename"].startswith("10_artifacts__") and row["filename"].endswith(".zip"))
    summary["full_repo_zip_bytes"] = full_repo.stat().st_size
    summary["full_repo_zip_sha256"] = sha256(full_repo)
    summary["over_100_files"] = len(upload_rows) > 100
    (REPORTS / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    if summary["over_100_files"]:
        raise SystemExit(f"Refusing v22 candidate with over 100 files: {summary['upload_file_count']}")

    metadata = metadata_json(summary)
    metadata_path = ZENODO / "metadata_v22_sga_batch004_reader_qc.json"
    metadata_path.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(json.dumps({"summary": summary, "metadata_path": str(metadata_path), "upload_list": str(REPORTS / "zenodo_v22_upload_files.txt")}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
