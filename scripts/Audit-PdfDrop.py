#!/usr/bin/env python3
"""Audit a recursive PDF drop with pdfinfo and pdftotext."""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def run_command(args: list[str], timeout: int) -> tuple[int, str, str]:
    proc = subprocess.run(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
    )
    return proc.returncode, proc.stdout, proc.stderr


def parse_pdfinfo(stdout: str) -> dict[str, str]:
    info: dict[str, str] = {}
    for line in stdout.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            info[key.strip()] = value.strip()
    return info


def audit_pdf(path: Path, root: Path, pdfinfo: str, pdftotext: str) -> dict[str, object]:
    row: dict[str, object] = {
        "relative_path": str(path.relative_to(root)),
        "path": str(path),
        "bytes": path.stat().st_size,
        "pdfinfo_ok": False,
        "pdftotext_ok": False,
        "pages": "",
        "page_size": "",
        "encrypted": "",
        "text_chars": 0,
        "text_words": 0,
        "text_density_chars_per_page": "",
        "status": "ERROR",
        "notes": "",
        "pdfinfo_stderr": "",
        "pdftotext_stderr": "",
    }
    if path.stat().st_size == 0:
        row["status"] = "ZERO_BYTES"
        row["notes"] = "zero-byte PDF"
        return row

    try:
        code, out, err = run_command([pdfinfo, str(path)], timeout=60)
        row["pdfinfo_stderr"] = err.strip()
        if code == 0:
            row["pdfinfo_ok"] = True
            info = parse_pdfinfo(out)
            row["pages"] = info.get("Pages", "")
            row["page_size"] = info.get("Page size", "")
            row["encrypted"] = info.get("Encrypted", "")
        else:
            row["status"] = "PDFINFO_FAIL"
            row["notes"] = f"pdfinfo exit {code}"
            return row
    except Exception as exc:  # noqa: BLE001 - audit should capture failures
        row["status"] = "PDFINFO_ERROR"
        row["notes"] = f"{type(exc).__name__}: {exc}"
        return row

    try:
        code, out, err = run_command([pdftotext, "-enc", "UTF-8", str(path), "-"], timeout=120)
        row["pdftotext_stderr"] = err.strip()
        if code == 0:
            row["pdftotext_ok"] = True
            normalized = re.sub(r"\s+", " ", out).strip()
            row["text_chars"] = len(normalized)
            row["text_words"] = len(normalized.split()) if normalized else 0
            try:
                pages = int(str(row["pages"]))
                if pages > 0:
                    row["text_density_chars_per_page"] = round(int(row["text_chars"]) / pages, 2)
            except ValueError:
                pass
        else:
            row["status"] = "PDFTOTEXT_FAIL"
            row["notes"] = f"pdftotext exit {code}"
            return row
    except Exception as exc:  # noqa: BLE001
        row["status"] = "PDFTOTEXT_ERROR"
        row["notes"] = f"{type(exc).__name__}: {exc}"
        return row

    if int(row["text_chars"]) < 20:
        row["status"] = "LOW_TEXT"
        row["notes"] = "opened, but extracted text is very low"
    else:
        row["status"] = "OK"
    return row


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--prefix", default="pdf_drop_audit")
    parser.add_argument("--pdfinfo", default="pdfinfo")
    parser.add_argument("--pdftotext", default="pdftotext")
    args = parser.parse_args()

    root = args.root.resolve()
    out_dir = args.out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    pdfs = sorted(root.rglob("*.pdf"), key=lambda p: str(p).lower())
    rows = [audit_pdf(path, root, args.pdfinfo, args.pdftotext) for path in pdfs]

    csv_path = out_dir / f"{args.prefix}_{timestamp}.csv"
    json_path = out_dir / f"{args.prefix}_{timestamp}_summary.json"
    fieldnames = [
        "relative_path",
        "path",
        "bytes",
        "pdfinfo_ok",
        "pdftotext_ok",
        "pages",
        "page_size",
        "encrypted",
        "text_chars",
        "text_words",
        "text_density_chars_per_page",
        "status",
        "notes",
        "pdfinfo_stderr",
        "pdftotext_stderr",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    status_counts: dict[str, int] = {}
    for row in rows:
        status = str(row["status"])
        status_counts[status] = status_counts.get(status, 0) + 1
    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "root": str(root),
        "pdf_count": len(rows),
        "total_pdf_bytes": sum(int(row["bytes"]) for row in rows),
        "status_counts": status_counts,
        "bad_or_attention_files": [row for row in rows if row["status"] != "OK"],
        "csv": str(csv_path),
        "summary_json": str(json_path),
    }
    json_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0 if not summary["bad_or_attention_files"] else 2


if __name__ == "__main__":
    sys.exit(main())
