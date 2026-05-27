#!/usr/bin/env python3
"""Stage Zenodo v21: v20 carried forward plus cleaned cleanup 9 non-EU layer."""

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
V20_UPLOAD = PROJECT_ROOT / "release_candidates" / "zenodo_v20_sga_translation_batch003" / "upload"
OUT_ROOT = PROJECT_ROOT / "release_candidates" / "zenodo_v21_cleanup9_non_eu"
UPLOAD = OUT_ROOT / "upload"
REPORTS = OUT_ROOT / "reports"
ZENODO = PROJECT_ROOT / "zenodo"
CLEAN_ROOT = Path.home() / "Downloads" / "CLEANED_DROPS" / "cleanup9_kimi5_001_005_redo_cleaned"
CLEAN_ZIP = Path.home() / "Downloads" / "CLEANED_DROPS" / "cleanup9_kimi5_001_005_redo_processed_current_package_CLEANED.zip"
PDF_AUDIT_SUMMARY = PROJECT_ROOT / "release_candidates" / "cleanup9_audit" / "cleanup9_cleaned_pdf_audit_stdout.json"
DEMOTED_TOP_LEVEL_PDFS = {
    "00_pdf__gauss_werke.pdf": "Demoted from reader-facing surface in v21. The file opens, but it is a 1,793-page OCR/stitched working draft with visible OCR/layout damage and is not suitable as a clean top-level reader PDF. It remains preserved inside the Gauss artifact ZIP and in the v21 history ZIP.",
}


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def slugify(stem: str) -> str:
    stem = stem.replace("_COMBINED", "")
    stem = stem.replace("_CURRENT_COMBINED", "")
    stem = stem.lower()
    stem = re.sub(r"[^a-z0-9]+", "_", stem)
    stem = re.sub(r"_+", "_", stem).strip("_")
    return stem


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


def copy_v20_surface_and_pack_old_80_files() -> dict[str, Any]:
    if not V20_UPLOAD.exists():
        raise SystemExit(f"Missing v20 upload surface: {V20_UPLOAD}")
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    UPLOAD.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)

    old_80: list[Path] = []
    demoted_rows: list[dict[str, Any]] = []
    copied = 0
    for src in sorted(V20_UPLOAD.iterdir(), key=lambda p: p.name):
        if not src.is_file():
            continue
        if src.name.startswith("99_full_repo__"):
            continue
        if src.name in DEMOTED_TOP_LEVEL_PDFS:
            demoted_rows.append(
                {
                    "filename": src.name,
                    "bytes": src.stat().st_size,
                    "sha256": sha256(src),
                    "reason": DEMOTED_TOP_LEVEL_PDFS[src.name],
                }
            )
            continue
        if src.name.startswith("80_"):
            old_80.append(src)
            continue
        shutil.copy2(src, UPLOAD / src.name)
        copied += 1

    history_zip = UPLOAD / "80_metadata__release_history_and_audits_through_v20.zip"
    with zipfile.ZipFile(history_zip, "w", compression=zipfile.ZIP_DEFLATED, allowZip64=True) as zf:
        for src in old_80:
            zf.write(src, f"v20_individual_80_files/{src.name}")
        extras = [
            ZENODO / "zenodo_v20_public_check_summary.json",
            ZENODO / "metadata_v20_sga_translation_batch003.json",
            PROJECT_ROOT / "zenodo" / "v20_sga_translation_batch003_publish" / "zenodo_v20_remote_file_check_summary_stdout.json",
        ]
        for src in extras:
            if src.exists():
                zf.write(src, f"v20_publication_checks/{src.name}")
        for row in demoted_rows:
            src = V20_UPLOAD / str(row["filename"])
            if src.exists():
                zf.write(src, f"demoted_top_level_reader_pdfs/{src.name}")
    with zipfile.ZipFile(history_zip, "r") as zf:
        bad = zf.testzip()
    if bad:
        raise RuntimeError(f"Bad member in history ZIP: {bad}")

    write_csv(REPORTS / "v21_demoted_top_level_reader_pdfs.csv", demoted_rows, ["filename", "bytes", "sha256", "reason"])
    return {
        "v20_files_copied_directly": copied,
        "v20_80_files_packed": len(old_80),
        "v20_top_level_reader_pdfs_demoted": len(demoted_rows),
        "demoted_top_level_reader_pdfs": demoted_rows,
        "history_zip": history_zip.name,
        "history_zip_bytes": history_zip.stat().st_size,
        "history_zip_sha256": sha256(history_zip),
    }


def add_cleanup9_files() -> dict[str, Any]:
    if not CLEAN_ROOT.exists():
        raise SystemExit(f"Missing cleaned cleanup9 root: {CLEAN_ROOT}")
    if not CLEAN_ZIP.exists():
        raise SystemExit(f"Missing cleaned cleanup9 ZIP: {CLEAN_ZIP}")

    rows: list[dict[str, Any]] = []
    non_eu_dir = CLEAN_ROOT / "non_eu_combined"
    for src in sorted(non_eu_dir.glob("*.pdf"), key=lambda p: p.name.lower()):
        dest = UPLOAD / f"00_pdf__non_eu__{slugify(src.stem)}.pdf"
        shutil.copy2(src, dest)
        row = pdf_info(dest)
        row.update({"source": str(src), "role": "non_eu_combined_reader_pdf"})
        rows.append(row)

    cayley_src = CLEAN_ROOT / "cayley_combined" / "cayley_all_current_incremental_COMBINED.pdf"
    cayley_dest = UPLOAD / "00_pdf__cayley_collected_papers_incremental_current_partial.pdf"
    shutil.copy2(cayley_src, cayley_dest)
    cayley_row = pdf_info(cayley_dest)
    cayley_row.update({"source": str(cayley_src), "role": "cayley_partial_incremental_reader_pdf"})
    rows.append(cayley_row)

    artifact = UPLOAD / "10_artifacts__cleanup9_kimi5_non_eu_cayley_redo_cleaned.zip"
    shutil.copy2(CLEAN_ZIP, artifact)
    with zipfile.ZipFile(artifact, "r") as zf:
        bad = zf.testzip()
    if bad:
        raise RuntimeError(f"Bad member in cleanup9 artifact ZIP: {bad}")

    audit_summary = {}
    if PDF_AUDIT_SUMMARY.exists():
        audit_summary = json.loads(PDF_AUDIT_SUMMARY.read_text(encoding="utf-8"))

    write_csv(REPORTS / "v21_cleanup9_added_reader_pdfs.csv", rows)
    return {
        "cleanup9_artifact_zip": artifact.name,
        "cleanup9_artifact_zip_bytes": artifact.stat().st_size,
        "cleanup9_artifact_zip_sha256": sha256(artifact),
        "added_non_eu_top_level_pdfs": sum(1 for row in rows if row["role"] == "non_eu_combined_reader_pdf"),
        "added_cayley_partial_top_level_pdfs": sum(1 for row in rows if row["role"] == "cayley_partial_incremental_reader_pdf"),
        "added_reader_pdf_rows": rows,
        "cleanup9_pdf_audit_summary": audit_summary,
    }


def rebuild_full_repo_zip() -> Path:
    dest = UPLOAD / "99_full_repo__modern_latex_corpus_v21_cleanup9_non_eu.zip"
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
    write_csv(REPORTS / "zenodo_v21_upload_files.csv", rows, ["filename", "bytes", "sha256"])
    (REPORTS / "zenodo_v21_upload_files.txt").write_text("\n".join(str(UPLOAD / row["filename"]) for row in rows) + "\n", encoding="utf-8")
    return rows


def copy_v21_reports_to_upload(summary: dict[str, Any]) -> None:
    summary_path = REPORTS / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    shutil.copy2(summary_path, UPLOAD / "80_metadata__v21_cleanup9_non_eu_summary.json")
    shutil.copy2(REPORTS / "v21_cleanup9_added_reader_pdfs.csv", UPLOAD / "80_audit__v21_cleanup9_added_reader_pdfs.csv")
    shutil.copy2(REPORTS / "v21_demoted_top_level_reader_pdfs.csv", UPLOAD / "80_audit__v21_demoted_top_level_reader_pdfs.csv")
    if PDF_AUDIT_SUMMARY.exists():
        shutil.copy2(PDF_AUDIT_SUMMARY, UPLOAD / "80_audit__v21_cleanup9_cleaned_pdf_audit_summary.json")
    readme = f"""Zenodo v21 staging note: cleaned cleanup 9 non-EU/Cayley layer

Generated: {summary['generated_at']}

This candidate carries v20 forward. The former individual v20 80_* audit files
are preserved inside 80_metadata__release_history_and_audits_through_v20.zip to
make room for individual reader PDFs without losing release history.

Added:
- 22 cleaned non-European combined reader PDFs as top-level 00_pdf__non_eu__*.pdf files.
- 1 partial Cayley current-incremental reader PDF.
- 10_artifacts__cleanup9_kimi5_non_eu_cayley_redo_cleaned.zip with TeX, PDFs,
  manifests, local cleaning notes, and source tree.

The cleaned cleanup 9 PDF audit reports 85/85 PDFs OK after removing two
zero-byte placeholders, removing two HTML files mislabeled as PDFs, and
rebuilding the corrupt Cayley all-in-one PDF from the valid volume PDFs.

Demoted:
- 00_pdf__gauss_werke.pdf was removed from the top-level reader surface because
  it is a rough OCR/stitched working draft rather than a clean reader PDF. The
  same material remains in 10_artifacts__gauss_werke.zip and in the v21 history
  ZIP under demoted_top_level_reader_pdfs/.
"""
    (UPLOAD / "80_README_v21_cleanup9_non_eu.txt").write_text(readme, encoding="utf-8")


def metadata_json(summary: dict[str, Any]) -> dict[str, Any]:
    previous = json.loads((ZENODO / "metadata_v20_sga_translation_batch003.json").read_text(encoding="utf-8"))
    description = previous["description"]
    old_non_eu = "<li><strong>Non-European / Central Asian source-manuscript release layer:</strong> <code>[----------] not yet incorporated here</code>. Local handoff/download packets exist, but those materials are not yet converted into this public LaTeX release layer.</li>"
    new_non_eu = "<li><strong>Non-European / Central Asian source-manuscript release layer:</strong> <code>[####------] first cleaned release layer</code>. v21 adds 22 cleaned non-European combined reader PDFs as individual top-level files plus a cleaned artifact ZIP containing 85 locally audited PDFs, TeX files, manifests, and cleanup notes from the KIMI5/web-session batch.</li>"
    description = description.replace(old_non_eu, new_non_eu)
    v21_para = """
<p><strong>What changed in v21 while preserving availability:</strong> the v20 corpus was copied forward with one reader-surface demotion: <code>00_pdf__gauss_werke.pdf</code> is no longer presented as a clean top-level PDF because it is a rough 1,793-page OCR/stitched working draft, but the material remains preserved inside <code>10_artifacts__gauss_werke.zip</code> and inside the release-history ZIP. The former individual <code>80_*</code> audit/report files through v20 were packed into <code>80_metadata__release_history_and_audits_through_v20.zip</code> to reduce front-page clutter without losing history. This version adds 22 cleaned non-European combined reader PDFs as <code>00_pdf__non_eu__...</code> files, adds one clearly marked partial Cayley incremental reader PDF, and adds <code>10_artifacts__cleanup9_kimi5_non_eu_cayley_redo_cleaned.zip</code>. Local audit of the cleaned cleanup 9 tree reported <code>[##########] 85/85</code> PDFs passing <code>pdfinfo</code> and text extraction after removing placeholder/bad PDFs and rebuilding the Cayley all-in-one PDF.</p>
"""
    description = description.replace("<p><strong>How the files are organized:</strong></p>", v21_para + "\n<p><strong>How the files are organized:</strong></p>")
    description = description.replace(
        "<li><code>80_...</code> files are manifests, audit summaries, replacement reports, packaging notes, and cleanup queues.</li>",
        "<li><code>80_...</code> files are current manifests, audit summaries, replacement reports, packaging notes, and cleanup queues. Older v20-and-before <code>80_*</code> files are preserved together in <code>80_metadata__release_history_and_audits_through_v20.zip</code>.</li>",
    )
    metadata = dict(previous)
    metadata["publication_date"] = date.today().isoformat()
    metadata["version"] = "2026-05-27 v21 cleaned non-European/Cayley batch"
    metadata["description"] = description
    metadata["notes"] = "Public working corpus for modern LaTeX editions of older mathematics and physics manuscripts. Version 21 carries v20 forward, demotes the rough Gauss Werke OCR/stitched draft from the top-level reader surface while preserving it in artifacts/history, and adds a cleaned KIMI5/web-session non-European and Cayley batch."
    keywords = list(metadata.get("keywords", []))
    for keyword in ["non-European mathematics", "Central Asian science", "Chinese mathematics", "Indian mathematics", "Islamic mathematics", "Cayley"]:
        if keyword not in keywords:
            keywords.append(keyword)
    metadata["keywords"] = keywords
    return metadata


def main() -> int:
    carry = copy_v20_surface_and_pack_old_80_files()
    cleanup = add_cleanup9_files()

    preliminary = {
        "generated_at": now_iso(),
        "carry_forward": carry,
        "cleanup9": cleanup,
    }
    copy_v21_reports_to_upload(preliminary)
    full_repo = rebuild_full_repo_zip()
    upload_rows = upload_manifest()

    summary = {
        "generated_at": preliminary["generated_at"],
        "carry_forward": carry,
        "cleanup9": cleanup,
        "upload_file_count": len(upload_rows),
        "upload_total_bytes": sum(int(row["bytes"]) for row in upload_rows),
        "upload_pdf_count": sum(1 for row in upload_rows if row["filename"].startswith("00_pdf__") and row["filename"].endswith(".pdf")),
        "upload_artifact_zip_count": sum(1 for row in upload_rows if row["filename"].startswith("10_artifacts__") and row["filename"].endswith(".zip")),
        "full_repo_zip": str(full_repo),
        "full_repo_zip_bytes": full_repo.stat().st_size,
        "full_repo_zip_sha256": sha256(full_repo),
        "over_100_files": len(upload_rows) > 100,
    }
    copy_v21_reports_to_upload(summary)
    full_repo = rebuild_full_repo_zip()
    upload_rows = upload_manifest()
    summary["upload_file_count"] = len(upload_rows)
    summary["upload_total_bytes"] = sum(int(row["bytes"]) for row in upload_rows)
    summary["full_repo_zip_bytes"] = full_repo.stat().st_size
    summary["full_repo_zip_sha256"] = sha256(full_repo)
    (REPORTS / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    metadata = metadata_json(summary)
    metadata_path = ZENODO / "metadata_v21_cleanup9_non_eu.json"
    metadata_path.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(json.dumps({"summary": summary, "metadata_path": str(metadata_path), "upload_list": str(REPORTS / "zenodo_v21_upload_files.txt")}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
