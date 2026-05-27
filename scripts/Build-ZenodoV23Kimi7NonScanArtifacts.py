#!/usr/bin/env python3
"""Stage Zenodo v23: v22 carried forward plus Kimi 7 non-scan artifact ZIPs."""

from __future__ import annotations

import csv
import hashlib
import json
import shutil
import zipfile
from datetime import date, datetime
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
V22_UPLOAD = PROJECT_ROOT / "release_candidates" / "zenodo_v22_sga_batch004_reader_qc" / "upload"
OUT_ROOT = PROJECT_ROOT / "release_candidates" / "zenodo_v23_kimi7_nonscan_artifacts"
UPLOAD = OUT_ROOT / "upload"
REPORTS = OUT_ROOT / "reports"
ZENODO = PROJECT_ROOT / "zenodo"

KIMI7_INITIAL_CLEAN = (
    Path.home()
    / "Downloads"
    / "KIMI7_NONSCAN_REFINED_FOR_WEB_CURRENT_CLEAN"
    / "WEB_UPLOAD_CHUNKS"
    / "kimi7_nonscan_refined_for_web_CLEAN_chunk_001.zip"
)
KIMI7_INITIAL_SUMMARY = (
    Path.home()
    / "Downloads"
    / "KIMI7_NONSCAN_REFINED_FOR_WEB_CURRENT_CLEAN"
    / "kimi7_nonscan_refined_for_web_CLEAN_summary.json"
)
KIMI7_INITIAL_AUDIT = (
    Path.home()
    / "Downloads"
    / "KIMI7_NONSCAN_REFINED_FOR_WEB_CURRENT_CLEAN"
    / "PDF_AUDIT"
    / "audit_stdout.json"
)

KIMI7_CONTINUE = (
    Path.home()
    / "Downloads"
    / "KIMI7_CONTINUE_NONSCAN_DELTA_FOR_WEB_CURRENT"
    / "WEB_UPLOAD_CHUNKS"
    / "kimi7_continue_nonscan_delta_for_web_chunk_001.zip"
)
KIMI7_CONTINUE_SUMMARY = (
    Path.home()
    / "Downloads"
    / "KIMI7_CONTINUE_NONSCAN_DELTA_FOR_WEB_CURRENT"
    / "kimi7_continue_nonscan_delta_summary.json"
)
KIMI7_CONTINUE_AUDIT = (
    Path.home()
    / "Downloads"
    / "KIMI7_CONTINUE_NONSCAN_DELTA_FOR_WEB_CURRENT"
    / "PDF_AUDIT"
    / "audit_stdout.json"
)

KIMI7_ARTIFACTS = [
    {
        "source": KIMI7_INITIAL_CLEAN,
        "dest_name": "10_artifacts__kimi7_nonscan_refined_clean.zip",
        "summary": KIMI7_INITIAL_SUMMARY,
        "audit": KIMI7_INITIAL_AUDIT,
        "label": "Kimi 7 initial resolved non-scan handoff, cleaned after PDF audit",
    },
    {
        "source": KIMI7_CONTINUE,
        "dest_name": "10_artifacts__kimi7_continue_nonscan_delta.zip",
        "summary": KIMI7_CONTINUE_SUMMARY,
        "audit": KIMI7_CONTINUE_AUDIT,
        "label": "Kimi 7 continuation/repair-pass non-scan delta",
    },
]


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


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def assert_zip_ok(path: Path) -> None:
    with zipfile.ZipFile(path, "r") as zf:
        bad = zf.testzip()
    if bad:
        raise RuntimeError(f"Bad member in {path.name}: {bad}")


def zip_member_counts(path: Path) -> dict[str, int]:
    image_exts = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".webp", ".jp2", ".j2k", ".bmp", ".gif", ".pgm"}
    file_count = 0
    pdf_count = 0
    image_count = 0
    with zipfile.ZipFile(path, "r") as zf:
        for info in zf.infolist():
            if info.is_dir():
                continue
            file_count += 1
            suffix = Path(info.filename).suffix.lower()
            if suffix == ".pdf":
                pdf_count += 1
            if suffix in image_exts:
                image_count += 1
    return {"file_count": file_count, "pdf_count": pdf_count, "image_member_count": image_count}


def copy_v22_surface() -> dict[str, Any]:
    if not V22_UPLOAD.exists():
        raise SystemExit(f"Missing v22 upload surface: {V22_UPLOAD}")
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    UPLOAD.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)

    copied = 0
    skipped_full_repo = 0
    for src in sorted(V22_UPLOAD.iterdir(), key=lambda p: p.name):
        if not src.is_file():
            continue
        if src.name.startswith("99_full_repo__"):
            skipped_full_repo += 1
            continue
        shutil.copy2(src, UPLOAD / src.name)
        copied += 1
    return {
        "v22_files_copied_directly": copied,
        "v22_full_repo_files_skipped_for_rebuild": skipped_full_repo,
    }


def add_kimi7_artifacts() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for item in KIMI7_ARTIFACTS:
        source = item["source"]
        if not source.exists():
            raise SystemExit(f"Missing Kimi 7 artifact source: {source}")
        assert_zip_ok(source)
        dest = UPLOAD / item["dest_name"]
        shutil.copy2(source, dest)
        counts = zip_member_counts(dest)
        summary = load_json(item["summary"]) if item["summary"].exists() else {}
        audit = load_json(item["audit"]) if item["audit"].exists() else {}
        row = {
            "filename": dest.name,
            "label": item["label"],
            "bytes": dest.stat().st_size,
            "sha256": sha256(dest),
            "zip_file_count": counts["file_count"],
            "zip_pdf_count": counts["pdf_count"],
            "zip_image_member_count": counts["image_member_count"],
            "audit_pdf_count": audit.get("pdf_count"),
            "audit_status_counts": json.dumps(audit.get("status_counts", {}), sort_keys=True),
            "summary_selected_or_kept_file_count": summary.get("kept_file_count", summary.get("selected_file_count")),
        }
        rows.append(row)
    write_csv(
        REPORTS / "v23_kimi7_added_artifacts.csv",
        rows,
        [
            "filename",
            "label",
            "bytes",
            "sha256",
            "zip_file_count",
            "zip_pdf_count",
            "zip_image_member_count",
            "audit_pdf_count",
            "audit_status_counts",
            "summary_selected_or_kept_file_count",
        ],
    )
    return {
        "added_artifact_count": len(rows),
        "added_artifacts": rows,
        "note": "These Kimi 7 ZIPs are artifact/source handoffs only. Their generated PDFs were audited for technical readability, but individual PDFs are not promoted to top-level reader PDFs in v23.",
    }


def write_summary(carry: dict[str, Any], kimi7: dict[str, Any]) -> dict[str, Any]:
    v22_public = {}
    v22_public_path = ZENODO / "zenodo_v22_public_check_summary.json"
    if v22_public_path.exists():
        v22_public = load_json(v22_public_path)
    summary = {
        "generated_at": now_iso(),
        "carry_forward": carry,
        "kimi7_nonscan_artifacts": kimi7,
        "reader_surface_change": "No new top-level reader PDFs in v23; Kimi 7 material is added as artifact ZIPs only.",
        "v22_public_record_carried_forward": v22_public,
        "upload_file_count_without_full_repo_pending": len([p for p in UPLOAD.iterdir() if p.is_file()]),
        "full_repo_zip": "99_full_repo__modern_latex_corpus_v23_kimi7_nonscan_artifacts.zip",
        "full_repo_zip_bytes": None,
        "full_repo_zip_sha256": None,
        "manifest_note": "The authoritative per-file sizes and hashes are in zenodo_v23_upload_files.csv. Full-repo ZIP hash is omitted here to avoid self-referential metadata drift because this JSON is included inside the full-repo ZIP.",
    }
    summary_path = REPORTS / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    shutil.copy2(summary_path, UPLOAD / "80_metadata__v23_kimi7_nonscan_artifacts_summary.json")
    shutil.copy2(REPORTS / "v23_kimi7_added_artifacts.csv", UPLOAD / "80_manifest__v23_kimi7_added_artifacts.csv")
    return summary


def rebuild_full_repo_zip() -> Path:
    dest = UPLOAD / "99_full_repo__modern_latex_corpus_v23_kimi7_nonscan_artifacts.zip"
    if dest.exists():
        dest.unlink()
    with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED, allowZip64=True) as zf:
        for path in sorted(UPLOAD.iterdir(), key=lambda p: p.name):
            if path.is_file() and path != dest:
                zf.write(path, path.name)
    assert_zip_ok(dest)
    return dest


def upload_manifest() -> list[dict[str, Any]]:
    rows = []
    for path in sorted(UPLOAD.iterdir(), key=lambda p: p.name):
        if path.is_file():
            rows.append({"filename": path.name, "bytes": path.stat().st_size, "sha256": sha256(path)})
    write_csv(REPORTS / "zenodo_v23_upload_files.csv", rows, ["filename", "bytes", "sha256"])
    (REPORTS / "zenodo_v23_upload_files.txt").write_text(
        "\n".join(str(UPLOAD / row["filename"]) for row in rows) + "\n",
        encoding="utf-8",
    )
    return rows


def metadata_json() -> dict[str, Any]:
    previous = load_json(ZENODO / "metadata_v22_sga_batch004_reader_qc.json")
    description = previous["description"]
    v23_paragraph = (
        "\n<p><strong>What changed in v23 while preserving availability:</strong> the v22 corpus was copied forward in full. "
        "This version adds two Kimi 7 non-scan artifact ZIPs: "
        "<code>10_artifacts__kimi7_nonscan_refined_clean.zip</code>, the cleaned initial Kimi 7 non-scan handoff with four placeholder/broken PDFs removed after audit, "
        "and <code>10_artifacts__kimi7_continue_nonscan_delta.zip</code>, the continuation/repair-pass delta. "
        "Together these add 4,689 non-image files, including 804 generated PDFs that passed technical <code>pdfinfo</code> and text-extraction checks. "
        "They are provided as artifact/source material for review and continuation, not promoted as polished top-level reader PDFs.</p>\n"
    )
    marker = "<p><strong>How the files are organized:</strong></p>"
    if marker in description:
        description = description.replace(marker, v23_paragraph + "\n" + marker)
    else:
        description += v23_paragraph
    return {
        **previous,
        "publication_date": date.today().isoformat(),
        "version": "2026-05-27 v23 Kimi 7 non-scan artifacts",
        "description": description,
        "keywords": sorted(set(previous.get("keywords", [])) | {"Kimi 7", "web-session handoff", "artifact ZIP"}),
        "notes": (
            "Public working corpus for modern LaTeX editions of older mathematics and physics manuscripts. "
            "Version 23 carries v22 forward and adds two Kimi 7 non-scan artifact ZIPs with audited generated PDFs and TeX/text source material; no new top-level reader PDFs are promoted in this pass."
        ),
    }


def main() -> int:
    carry = copy_v22_surface()
    kimi7 = add_kimi7_artifacts()
    summary = write_summary(carry, kimi7)
    full = rebuild_full_repo_zip()
    rows = upload_manifest()
    summary["upload_file_count"] = len(rows)
    summary["upload_total_bytes"] = sum(int(row["bytes"]) for row in rows)
    summary["upload_artifact_zip_count"] = sum(1 for row in rows if str(row["filename"]).startswith("10_artifacts__"))
    summary["upload_pdf_count"] = sum(1 for row in rows if str(row["filename"]).startswith("00_pdf__") and str(row["filename"]).endswith(".pdf"))
    summary["full_repo_zip_bytes_manifest"] = full.stat().st_size
    summary["full_repo_zip_sha256_manifest"] = sha256(full)
    (REPORTS / "summary_final_after_full_repo.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    metadata = metadata_json()
    metadata_path = ZENODO / "metadata_v23_kimi7_nonscan_artifacts.json"
    metadata_path.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    result = {
        "out_root": str(OUT_ROOT),
        "upload_dir": str(UPLOAD),
        "metadata_json": str(metadata_path),
        "upload_file_count": len(rows),
        "upload_total_bytes": sum(int(row["bytes"]) for row in rows),
        "full_repo_zip": full.name,
        "full_repo_zip_bytes": full.stat().st_size,
        "full_repo_zip_sha256": sha256(full),
        "over_100_files": len(rows) > 100,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    if len(rows) > 100:
        raise SystemExit("Refusing v23 candidate: over Zenodo 100-file practical limit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
