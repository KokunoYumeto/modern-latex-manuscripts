#!/usr/bin/env python3
"""Compose the controlling final summary after independent audit closure."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


EVIDENCE = Path(__file__).resolve().parent
ROOT = EVIDENCE.parent


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


compiled_path = EVIDENCE / "R9_COMPILED_REFERENCE_VALIDATION.json"
visual_path = EVIDENCE / "R9_VISUAL_QA.json"
postlink_path = EVIDENCE / "R9_POSTLINK_RESIDUAL_RESCAN_SUMMARY.json"
audit_path = EVIDENCE / "R9_INDEPENDENT_REFERENCE_AUDIT.md"
compiled = json.loads(compiled_path.read_text(encoding="utf-8"))
visual = json.loads(visual_path.read_text(encoding="utf-8"))
postlink = json.loads(postlink_path.read_text(encoding="utf-8"))
if compiled["status"] != "PASS" or visual["status"] != "PASS" or postlink["status"] != "PASS":
    raise RuntimeError("one or more controlling gates are not PASS")
if not audit_path.is_file() or "Final disposition: **PASS**" not in audit_path.read_text(encoding="utf-8"):
    raise RuntimeError("independent PASS audit is not yet present")

result = {
    "status": "PASS_EXHAUSTIVE_INTERNAL_REFERENCES",
    "revision": "R9",
    "scope": "complete 309-page SGA5 English synchronized reader",
    "convention": {
        "revision": "v2 exhaustive",
        "sha256": "F5BDC71164EDA34128E584E4F117993D31EE07698E329986CF5013519E5CA8CC",
    },
    "reader": {
        "tex_bytes": compiled["r9_tex"]["bytes"],
        "tex_sha256": compiled["r9_tex"]["sha256"],
        "pdf_bytes": compiled["r9_pdf"]["bytes"],
        "pdf_sha256": compiled["r9_pdf"]["sha256"],
        "pages": compiled["r9_pdf"]["pages"],
        "fonts_embedded_subset_unicode": compiled["r9_pdf"]["fonts"],
    },
    "graph": {
        "targets": compiled["machine_graph"]["targets"],
        "cumulative_edges": compiled["machine_graph"]["edges"],
        "new_r9_edges": 720,
        "candidate_dispositions": compiled["machine_graph"]["candidates"],
        "compiled_named_destinations": compiled["r9_pdf"]["named_destinations"],
        "compiled_goto_annotations": compiled["r9_pdf"]["goto_annotations"],
        "original_r8_links_preserved": compiled["r8_link_preservation"],
    },
    "exhaustive_inventory": {
        "prelink_occurrences": compiled["exhaustive_prelink_occurrences"],
        "prelink_final_classes": compiled["exhaustive_prelink_classification_counts"],
        "postlink_unwrapped_occurrences": compiled["postlink_unwrapped_occurrences"],
        "postlink_final_classes": compiled["postlink_final_classification_counts"],
        "unwrapped_internally_resolvable": 0,
        "unadjudicated": 0,
    },
    "source_and_visible_preservation": {
        "removing_r9_markup_reconstructs_r8_exact": compiled["source_reconstruction"]["exact"],
        "r8_tex_sha256": compiled["source_reconstruction"]["baseline_r8_tex_sha256"],
        "r8_r9_layout_text_exact": compiled["visible_text_preservation"]["r8_r9_layout_exact"],
        "r8_r9_flow_text_exact": compiled["visible_text_preservation"]["r8_r9_flow_exact"],
        "page_count_exact": True,
    },
    "build": {
        "three_pass_aux_out_converged": True,
        "decoded_page_content_converged": True,
        "prohibited_final_diagnostics": 0,
        "timestamp_variance_disclosed": compiled["build"]["pdf_byte_variance"],
    },
    "visual_qa": {
        "status": visual["status"],
        "sampled_rendered_pages": len(visual["selected_pages"]),
        "receipt_sha256": sha256(visual_path),
    },
    "controls": {
        "compiled_validation_sha256": sha256(compiled_path),
        "postlink_summary_sha256": sha256(postlink_path),
        "independent_audit_sha256": sha256(audit_path),
    },
    "intentional_nonlinks_not_backlog": {
        "external_work_citations": 268,
        "unavailable_same_work_targets": 6,
        "structural_declarations": 945,
        "typography_layout_geometry_values": 179,
        "note": "All remain visibly unchanged and positively dispositioned; none is an unresolved internal reference.",
    },
    "historical_controls": (
        "Unprefixed summary/validation files inherited in the copied R8 tree are predecessor evidence; "
        "R9_* controls are authoritative for this successor."
    ),
    "archive_or_claude_handoff": "none_by_this_worker",
}

output = EVIDENCE / "R9_FINAL_REFERENCE_SUMMARY.json"
output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "sha256": sha256(output)}, indent=2))
