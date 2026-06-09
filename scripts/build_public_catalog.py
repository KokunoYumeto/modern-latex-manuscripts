#!/usr/bin/env python3
"""Build the public Zenodo file catalog for this repository.

This script uses only the public Zenodo records API. It does not need a token.
Run it from the repository root:

    python scripts/build_public_catalog.py

Outputs:
    manifests/public-file-catalog.csv
    docs/public-file-catalog.md
"""

from __future__ import annotations

import csv
import html
import json
import re
import sys
import urllib.request
from pathlib import Path
from typing import Any


RECORDS: list[tuple[str, str]] = [
    ("main", "20415117"),
    ("workflow", "20611670"),
    ("noether", "20616638"),
    ("weber", "20616798"),
    ("cayley", "20616177"),
    ("sga", "20616461"),
    ("deligne", "20615537"),
    ("ega", "20414353"),
    ("ukrainian_applied_math", "20490906"),
    ("gauss", "20586894"),
    ("albattani_opus_astronomicum", "20584850"),
    ("non_european_consolidated", "20586401"),
    ("chinese", "20415752"),
    ("indian_sanskrit", "20415755"),
    ("islamic_arabic", "20415770"),
    ("historical_references", "20415777"),
    ("classical_algebra_arithmetic", "20583048"),
    ("sylvester", "20586907"),
    ("dedekind", "20586067"),
    ("dirichlet", "20586064"),
    ("bianchi", "20615949"),
    ("gordan_clebsch_gordan", "20616261"),
    ("steinitz", "20616989"),
    ("additional_author_cluster", "20616046"),
]

RECORD_NOTES = {
    "cayley": [
        "Accuracy warning 2026-06-09: Cayley files listed here are retained for provenance and repair. Current Cayley PDFs/TeX are not accuracy-certified; package names containing `Source-Checked` are obsolete labels until a future per-page glyph/source audit re-promotes specific ranges. The narrow `Cayley_V1_critical_p001_024_20260609.zip` packet is the current promoted restart tranche for Volume I printed pp.1-24 / Papers 1-4.",
    ],
    "classical_algebra_arithmetic": [
        "Accuracy warning 2026-06-09: Cayley files in this older mixed shelf are retained for provenance and repair only; do not treat the Cayley slice readers as faithful editions without a new page-by-page audit.",
    ],
}


def fetch_record(record_id: str) -> dict[str, Any]:
    url = f"https://zenodo.org/api/records/{record_id}"
    with urllib.request.urlopen(url, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def file_role(filename: str) -> str:
    lower = filename.lower()
    if lower.endswith(".zip"):
        return "artifact/source ZIP"
    if lower.endswith((".json", ".md", ".csv", ".txt")):
        return "manifest/status"
    if lower.endswith(".pdf"):
        return "reader/reference PDF"
    return "other"


def file_url(record_id: str, filename: str) -> str:
    from urllib.parse import quote

    return f"https://zenodo.org/records/{record_id}/files/{quote(filename)}"


def build_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for label, record_id in RECORDS:
        record = fetch_record(record_id)
        title = record.get("metadata", {}).get("title", "")
        for item in sorted(record.get("files", []), key=lambda value: value.get("key", "").lower()):
            filename = item.get("key", "")
            size_mb = float(item.get("size", 0)) / (1024 * 1024)
            rows.append(
                {
                    "record_label": label,
                    "record_id": record_id,
                    "record_title": title,
                    "file_role": file_role(filename),
                    "filename": filename,
                    "size_mb": f"{size_mb:.4f}",
                    "url": file_url(record_id, filename),
                }
            )
    return rows


def write_csv(rows: list[dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "record_label",
                "record_id",
                "record_title",
                "file_role",
                "filename",
                "size_mb",
                "url",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(rows: list[dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row["record_label"], []).append(row)

    lines: list[str] = [
        "# Public File Catalog",
        "",
        "Generated from the public Zenodo records API.",
        "",
        f"Total files indexed: {len(rows)}",
        "",
    ]

    for label, _record_id in RECORDS:
        group = grouped.get(label, [])
        if not group:
            continue
        title = group[0]["record_title"]
        record_id = group[0]["record_id"]
        lines.extend(
            [
                f"## {html.escape(title)}",
                "",
                f"Record: <https://zenodo.org/records/{record_id}>",
                "",
            ]
        )
        for note in RECORD_NOTES.get(label, []):
            lines.extend([note, ""])
        lines.extend(
            [
                "| Role | Size MB | File |",
                "|---|---:|---|",
            ]
        )
        for row in group:
            filename = row["filename"]
            lines.append(
                f"| {row['file_role']} | {row['size_mb']} | [{html.escape(filename)}]({row['url']}) |"
            )
        lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    root = Path.cwd()
    rows = build_rows()
    write_csv(rows, root / "manifests" / "public-file-catalog.csv")
    write_markdown(rows, root / "docs" / "public-file-catalog.md")
    print(f"Indexed {len(rows)} public files from {len(RECORDS)} records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
