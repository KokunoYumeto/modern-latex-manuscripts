#!/usr/bin/env python3
"""Create and replay the self-excluding SGA5 R9 delivery manifest."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
EVIDENCE = ROOT / "machine_readable_references"
MANIFEST = EVIDENCE / "R9_DELIVERY_MANIFEST.csv"
VALIDATION = EVIDENCE / "R9_DELIVERY_MANIFEST_VALIDATION.json"

FILES = [
    ("SGA5_English_sync_workpass.tex", "reader_source"),
    ("SGA5_English_sync_workpass.pdf", "compiled_reader"),
    ("machine_readable_references/MACHINE_READABLE_INTERNAL_REFERENCES_CONVENTION_v2_EXHAUSTIVE.md", "frozen_convention"),
    ("machine_readable_references/REFERENCE_TARGETS.csv", "target_ledger"),
    ("machine_readable_references/REFERENCE_EDGES.csv", "edge_ledger"),
    ("machine_readable_references/REFERENCE_CANDIDATES.csv", "candidate_disposition_ledger"),
    ("machine_readable_references/R9_RESIDUAL_LOCATOR_INVENTORY.csv", "prelink_exhaustive_inventory"),
    ("machine_readable_references/R9_RESIDUAL_LOCATOR_INVENTORY_SUMMARY.json", "prelink_inventory_summary"),
    ("machine_readable_references/R9_EXHAUSTIVE_RESIDUAL_CLASSIFICATION.csv", "prelink_final_classification"),
    ("machine_readable_references/R9_POSTLINK_RESIDUAL_RESCAN.csv", "postlink_residual_replay"),
    ("machine_readable_references/R9_POSTLINK_RESIDUAL_RESCAN_SUMMARY.json", "postlink_replay_summary"),
    ("machine_readable_references/R9_LINK_INSERTION_SUMMARY.json", "link_insertion_summary"),
    ("machine_readable_references/R9_VISIBLE_SOURCE_PRESERVATION.csv", "source_preservation_proof"),
    ("machine_readable_references/R9_COMPILED_REFERENCE_VALIDATION.json", "compiled_pdf_validation"),
    ("machine_readable_references/R9_VISUAL_QA.json", "visual_qa_receipt"),
    ("machine_readable_references/visual_qa_r9/contact_1.png", "visual_qa_contact_sheet"),
    ("machine_readable_references/visual_qa_r9/contact_2.png", "visual_qa_contact_sheet"),
    ("machine_readable_references/visual_qa_r9/contact_3.png", "visual_qa_contact_sheet"),
    ("machine_readable_references/visual_qa_r9/contact_4.png", "visual_qa_contact_sheet"),
    ("machine_readable_references/visual_qa_r9/contact_5.png", "visual_qa_contact_sheet"),
    ("machine_readable_references/r9_exhaustive_references.py", "reproducible_inventory_and_insertion_tool"),
    ("machine_readable_references/r9_compiled_validate.py", "compiled_validation_tool"),
    ("machine_readable_references/r9_visual_qa_receipt.py", "visual_qa_receipt_tool"),
    ("machine_readable_references/r9_final_summary.py", "final_summary_tool"),
    ("machine_readable_references/r9_delivery_manifest.py", "self_excluding_manifest_tool"),
    ("machine_readable_references/R9_FINAL_REFERENCE_SUMMARY.json", "final_summary"),
    ("machine_readable_references/R9_INDEPENDENT_REFERENCE_AUDIT.md", "independent_audit"),
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


rows = []
for index, (relative, role) in enumerate(FILES, 1):
    path = ROOT / relative
    if not path.is_file():
        raise FileNotFoundError(path)
    rows.append(
        {
            "artifact_id": f"SGA5-R9-DELIVERY-{index:03d}",
            "relative_path": relative.replace("\\", "/"),
            "bytes": str(path.stat().st_size),
            "sha256": sha256(path),
            "role": role,
            "release_status": "internal_successor_no_archive_handoff",
        }
    )

fields = ["artifact_id", "relative_path", "bytes", "sha256", "role", "release_status"]
with MANIFEST.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)

with MANIFEST.open("r", encoding="utf-8", newline="") as handle:
    replay = list(csv.DictReader(handle))
errors = []
if replay != rows:
    errors.append("CSV parse replay differs from generated rows")
if len({row["artifact_id"] for row in replay}) != len(replay):
    errors.append("duplicate artifact ID")
if len({row["relative_path"] for row in replay}) != len(replay):
    errors.append("duplicate relative path")
for row in replay:
    path = ROOT / row["relative_path"]
    if not path.is_file():
        errors.append(f"missing: {row['relative_path']}")
        continue
    if path.stat().st_size != int(row["bytes"]):
        errors.append(f"byte mismatch: {row['relative_path']}")
    if sha256(path) != row["sha256"]:
        errors.append(f"hash mismatch: {row['relative_path']}")
    for value in row.values():
        if value.startswith(("=", "+", "-", "@")):
            errors.append(f"formula-prefix cell: {row['artifact_id']}")

aggregate_stream = "".join(
    f"{row['relative_path']}\t{row['bytes']}\t{row['sha256']}\n" for row in replay
).encode("utf-8")
result = {
    "status": "PASS" if not errors else "FAIL",
    "errors": errors,
    "manifest_self_excluded": True,
    "validation_control_excluded_to_avoid_recursive_identity": True,
    "manifest_rows": len(replay),
    "represented_bytes": sum(int(row["bytes"]) for row in replay),
    "manifest_bytes": MANIFEST.stat().st_size,
    "manifest_sha256": sha256(MANIFEST),
    "canonical_aggregate_sha256": hashlib.sha256(aggregate_stream).hexdigest().upper(),
    "all_rows_replayed_exact": not errors,
}
VALIDATION.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if not errors else 1)
