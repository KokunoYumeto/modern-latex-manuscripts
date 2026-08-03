from __future__ import annotations

import csv
import hashlib
import json
import sys
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "INPUT_READERS_r4_clean.csv"
BUILD = ROOT / "build_navigation_r4_clean_reader_surface"
PDF = BUILD / "SGA_1_7II_English_Global_Reader_navigation_r4_clean.pdf"
ROUTE_VALIDATION = BUILD / "VALIDATION.json"
SURFACE_VALIDATION = (
    ROOT
    / "reader_surface_controls"
    / "sga_standalone_reader_surface_scan_20260803_r2"
    / "ADJUDICATED_VALIDATION.json"
)
OUTPUT = BUILD / "CLEAN_INPUT_CONTENT_VALIDATION.json"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def content_bytes(page) -> bytes:
    contents = page.get_contents()
    if contents is None:
        return b""
    return contents.get_data()


def box_tuple(page, key: str) -> tuple[float, float, float, float]:
    box = page.get(key)
    return tuple(float(value) for value in box)


def main() -> int:
    if len(sys.argv) == 1:
        manifest = MANIFEST
        pdf = PDF
        route_validation = ROUTE_VALIDATION
        output = OUTPUT
    elif len(sys.argv) in (5, 6):
        manifest = Path(sys.argv[1])
        pdf = Path(sys.argv[2])
        route_validation = Path(sys.argv[3])
        output = Path(sys.argv[4])
        surface_validation = Path(sys.argv[5]) if len(sys.argv) == 6 else SURFACE_VALIDATION
    else:
        print(
            "usage: validate_cumulative_clean_inputs.py "
            "[MANIFEST.csv CUMULATIVE.pdf ROUTE_VALIDATION.json OUTPUT.json [SURFACE_VALIDATION.json]]",
            file=sys.stderr,
        )
        return 2

    with manifest.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))

    route = json.loads(route_validation.read_text(encoding="utf-8-sig"))
    if len(sys.argv) == 1:
        surface_validation = SURFACE_VALIDATION
    surface = json.loads(surface_validation.read_text(encoding="utf-8-sig"))
    cumulative = PdfReader(str(pdf))
    offset = 0
    input_records = []
    mismatches = []

    for row in rows:
        path = ROOT / row["local_pdf"]
        actual_hash = sha256(path)
        reader = PdfReader(str(path))
        record = {
            "input_id": row["input_id"],
            "volume": row["title"],
            "path": row["local_pdf"],
            "bytes": path.stat().st_size,
            "sha256": actual_hash,
            "pages": len(reader.pages),
            "cumulative_first_page": offset + 1,
            "cumulative_last_page": offset + len(reader.pages),
            "content_stream_matches": 0,
            "geometry_matches": 0,
        }
        if path.stat().st_size != int(row["bytes"]):
            mismatches.append(f"{row['input_id']}:bytes")
        if actual_hash != row["sha256"]:
            mismatches.append(f"{row['input_id']}:sha256")
        if len(reader.pages) != int(row["pages"]):
            mismatches.append(f"{row['input_id']}:pages")

        for local_index, source_page in enumerate(reader.pages):
            global_index = offset + local_index
            target_page = cumulative.pages[global_index]
            if content_bytes(source_page) == content_bytes(target_page):
                record["content_stream_matches"] += 1
            else:
                mismatches.append(
                    f"{row['input_id']}:content:{local_index + 1}->{global_index + 1}"
                )
            source_geometry = (
                box_tuple(source_page, "/MediaBox"),
                tuple(float(value) for value in (source_page.get("/CropBox") or source_page.get("/MediaBox"))),
                int(source_page.get("/Rotate") or 0),
            )
            target_geometry = (
                box_tuple(target_page, "/MediaBox"),
                tuple(float(value) for value in (target_page.get("/CropBox") or target_page.get("/MediaBox"))),
                int(target_page.get("/Rotate") or 0),
            )
            if source_geometry == target_geometry:
                record["geometry_matches"] += 1
            else:
                mismatches.append(
                    f"{row['input_id']}:geometry:{local_index + 1}->{global_index + 1}"
                )

        input_records.append(record)
        offset += len(reader.pages)

    metadata = {str(k): str(v) for k, v in (cumulative.metadata or {}).items()}
    metadata_text = " ".join(metadata.values()).lower()
    forbidden_metadata = {
        term: metadata_text.count(term)
        for term in [
            "workpass",
            "working edition",
            "source status",
            "source-synchron",
            "machine-assisted",
            "PRIVATE_OPERATOR",
            "audit",
            "certif",
            "codex",
            "claude",
        ]
    }
    checks = {
        "nine_exact_inputs": len(rows) == 9,
        "page_sum_exact": offset == len(cumulative.pages) == 4177,
        "input_hash_size_page_replay": not any(
            item.endswith((":bytes", ":sha256", ":pages")) for item in mismatches
        ),
        "all_page_content_streams_exact": not any(":content:" in item for item in mismatches),
        "all_page_geometry_exact": not any(":geometry:" in item for item in mismatches),
        "route_validation_pass": route.get("status") == "PASS" and route.get("errors") == [],
        "surface_adjudication_pass": surface.get("status") == "PASS" and surface.get("errors") == [],
        "neutral_metadata": not any(forbidden_metadata.values()),
    }
    result = {
        "schema": "sga-global-clean-input-content-validation-v1",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "errors": [name for name, passed in checks.items() if not passed],
        "checks": checks,
        "manifest": {
            "path": str(manifest),
            "bytes": manifest.stat().st_size,
            "sha256": sha256(manifest),
            "rows": len(rows),
        },
        "cumulative": {
            "path": str(pdf),
            "bytes": pdf.stat().st_size,
            "sha256": sha256(pdf),
            "pages": len(cumulative.pages),
            "metadata": metadata,
            "forbidden_metadata_hits": forbidden_metadata,
        },
        "route_validation_sha256": sha256(route_validation),
        "surface_adjudication_sha256": sha256(surface_validation),
        "inputs": input_records,
        "mismatches": mismatches,
    }
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "errors": result["errors"], "pages": len(cumulative.pages), "mismatches": len(mismatches)}))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
