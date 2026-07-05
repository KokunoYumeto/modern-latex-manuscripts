import datetime
import hashlib
import json
import pathlib
import re


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
INTEGRATED_MATRIX_JSON = BASE / "INTEGRATED_LANE_HANDOFF_READINESS_MATRIX_20260630.json"
AUTHORITY_QUEUE_JSON = BASE / "EXTERNAL_AUTHORITY_REVIEW_QUEUE_20260630.json"
AUTHORITY_FORMS_JSON = BASE / "EXTERNAL_AUTHORITY_REVIEW_PACKET_FORMS_20260630.json"
SUPPORT_NOTES_JSON = BASE / "SUPPORT_COHORT_AUTHORITY_NOTES_20260630.json"
OUT_JSON = BASE / "RENDER_SCRIPT_VALIDATION_PREFLIGHT_20260630.json"
OUT_MD = BASE / "RENDER_SCRIPT_VALIDATION_PREFLIGHT_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "render_script_validation_preflight_local_only_no_render_no_review"

COMMON_MATH_LAYOUT_CHECKS = [
    "formula_text_association",
    "theorem_label_cross_reference_integrity",
    "bibliography_and_footnote_render_integrity",
    "page_breaks_around_display_math",
]

COMMON_SCRIPT_GOVERNANCE_CHECKS = [
    "observed_source_anchor_separated_from_project_proposal",
    "glossary_ordering_rule_recorded",
    "reviewer_scope_recorded_before_approval_claim",
]

PROFILES = {
    "slavic_reference": {
        "kind": "slavic_reference_lane",
        "label": "Slavic Latin/Cyrillic Sidecar Reference",
        "readiness_group": "review_ready_precedent_pointer_not_rebuilt_here",
        "profile": "latin_cyrillic_dual_script_sidecar",
        "script_systems": ["Latin", "Cyrillic"],
        "writing_direction": "ltr",
        "required_render_checks": [
            "latin_cyrillic_sidecar_equivalence",
            "transliteration_report_hash_check",
            "font_coverage_latin_cyrillic",
            "sidecar_file_pair_manifest_match",
        ],
        "required_script_governance_checks": [
            "Latin_and_Cyrillic_are_parallel_sidecars_not_separate_authority_claims",
            "sidecar_conversion_is_mechanical_until_reviewed",
            "review_return_corrections_apply_to_both_script_sides_when_in_scope",
        ],
        "prerequisite_gate": "maintain_prior_review_ready_pointers_and_ingest_future_returns",
        "upstream_blocker_class": "review_return_or_source_correction_only",
        "required_reviewer_roles": [
            "slavic_language_reviewer",
            "latin_cyrillic_sidecar_validator",
            "mathematical_register_reviewer",
        ],
    },
    "simplified_chinese": {
        "profile": "cjk_han_simplified",
        "script_systems": ["Han simplified", "Latin math notation"],
        "writing_direction": "ltr",
        "required_render_checks": [
            "cjk_font_coverage",
            "cjk_line_breaking",
            "punctuation_width_and_spacing",
            "pdf_bookmark_unicode",
        ],
        "required_script_governance_checks": [
            "simplified_traditional_boundary_recorded",
            "CJK_term_sorting_rule_recorded",
            "Chinese_visual_reviewer_required_before_packet_population",
        ],
    },
    "japanese": {
        "profile": "cjk_japanese",
        "script_systems": ["Kanji", "Kana", "Latin math notation"],
        "writing_direction": "ltr",
        "required_render_checks": [
            "japanese_font_coverage",
            "cjk_line_breaking",
            "fullwidth_halfwidth_spacing",
            "pdf_bookmark_unicode",
        ],
        "required_script_governance_checks": [
            "Japanese_Noetherian_phrasing_requires_native_review",
            "kana_kanji_glossary_sort_rule_recorded",
            "Japanese_visual_reviewer_required_before_packet_population",
        ],
    },
    "french": {
        "profile": "latin_roman_french",
        "script_systems": ["Latin"],
        "writing_direction": "ltr",
        "required_render_checks": [
            "French_hyphenation_loaded",
            "accented_glyph_font_coverage",
            "French_spacing_punctuation_check",
            "PDF_copy_paste_unicode_check",
        ],
        "required_script_governance_checks": [
            "French_register_not_collapsed_into_Romance_bridge",
            "French_glossary_sort_rule_recorded",
            "French_visual_reviewer_required_before_packet_population",
        ],
    },
    "spanish": {
        "profile": "latin_roman_spanish",
        "script_systems": ["Latin"],
        "writing_direction": "ltr",
        "required_render_checks": [
            "Spanish_hyphenation_loaded",
            "accented_glyph_font_coverage",
            "Spanish_punctuation_and_math_spacing_check",
            "PDF_copy_paste_unicode_check",
        ],
        "required_script_governance_checks": [
            "Spanish_register_not_collapsed_into_Romance_bridge",
            "Spanish_glossary_sort_rule_recorded",
            "Spanish_reviewer_required_before_packet_population",
        ],
    },
    "arabic": {
        "profile": "rtl_arabic",
        "script_systems": ["Arabic", "Latin math notation"],
        "writing_direction": "rtl",
        "required_render_checks": [
            "rtl_directionality",
            "Arabic_shaping_and_ligatures",
            "math_formula_direction_isolation",
            "page_number_and_header_direction_check",
        ],
        "required_script_governance_checks": [
            "Arabic_OCR_or_provenance_risk_recorded",
            "Arabic_module_representation_gap_recorded",
            "RTL_visual_reviewer_required_before_packet_population",
        ],
    },
    "fa_IR": {
        "profile": "rtl_persian_farsi",
        "script_systems": ["Perso-Arabic", "Latin math notation"],
        "writing_direction": "rtl",
        "required_render_checks": [
            "rtl_directionality",
            "Persian_glyph_and_joining_check",
            "Persian_punctuation_and_numeral_policy",
            "math_formula_direction_isolation",
        ],
        "required_script_governance_checks": [
            "Iranian_Persian_not_collapsed_with_Dari_or_Tajik",
            "Persian_register_reviewer_scope_recorded",
            "RTL_or_script_reviewer_required_before_packet_population",
        ],
    },
    "prs_AF": {
        "profile": "rtl_dari_persian",
        "script_systems": ["Perso-Arabic", "Latin math notation"],
        "writing_direction": "rtl",
        "required_render_checks": [
            "rtl_directionality",
            "Dari_glyph_and_joining_check",
            "Dari_punctuation_and_numeral_policy",
            "math_formula_direction_isolation",
        ],
        "required_script_governance_checks": [
            "Dari_not_collapsed_with_Iranian_Persian_or_Tajik",
            "Dari_register_reviewer_scope_recorded",
            "RTL_or_script_reviewer_required_before_packet_population",
        ],
    },
    "tg_Cyrl_TJ": {
        "profile": "cyrillic_tajik_source_discovery",
        "script_systems": ["Cyrillic", "Latin math notation"],
        "writing_direction": "ltr",
        "required_render_checks": [
            "Tajik_Cyrillic_font_coverage",
            "Cyrillic_math_spacing",
            "PDF_copy_paste_unicode_check",
            "source_discovery_render_feasibility_note",
        ],
        "required_script_governance_checks": [
            "Tajik_source_discovery_required_before_term_queue",
            "Tajik_not_collapsed_with_Persian_or_Dari",
            "Tajik_Cyrillic_reviewer_required_before_packet_population",
        ],
    },
    "africa_deep_gap": {
        "profile": "african_local_script_scope_tbd",
        "script_systems": ["Latin", "Ethiopic", "Arabic", "local scripts TBD"],
        "writing_direction": "mixed_or_tbd",
        "required_render_checks": [
            "script_identification_before_render",
            "font_coverage_for_selected_script",
            "local_punctuation_and_numeral_policy",
            "PDF_copy_paste_unicode_check",
        ],
        "required_script_governance_checks": [
            "named_language_or_register_required_before_edition_lane",
            "local_educator_or_community_reviewer_required",
            "regional_grouping_is_not_script_authority",
        ],
    },
    "east_southeast_asia_pacific": {
        "profile": "east_southeast_asia_pacific_script_scope_tbd",
        "script_systems": ["CJK", "Latin", "Thai", "Khmer", "Lao", "Burmese", "other scripts TBD"],
        "writing_direction": "mixed_or_tbd",
        "required_render_checks": [
            "script_identification_before_render",
            "complex_script_line_breaking",
            "font_coverage_for_selected_script",
            "PDF_bookmark_unicode_check",
        ],
        "required_script_governance_checks": [
            "named_language_lane_required_before_render_claim",
            "regional_grouping_is_not_language_or_script_authority",
            "script_specific_reviewer_required_before_packet_population",
        ],
    },
    "methodology_interlanguage_access": {
        "profile": "interlanguage_or_constructed_script_governance",
        "script_systems": ["Latin", "Cyrillic", "constructed or project-specific scripts TBD"],
        "writing_direction": "ltr_or_tbd",
        "required_render_checks": [
            "orthography_version_manifest",
            "script_conversion_rule_validation",
            "font_coverage_for_project_script",
            "example_render_marked_as_demonstration",
        ],
        "required_script_governance_checks": [
            "project_or_community_authority_identified",
            "constructed_pilot_marked_opt_in_and_not_canonical",
            "script_change_logged_as_proposal_until_reviewed",
        ],
    },
    "pan_turkic_adjacent": {
        "profile": "pan_turkic_multi_script_scope_tbd",
        "script_systems": ["Latin", "Cyrillic", "Arabic"],
        "writing_direction": "mixed_or_tbd",
        "required_render_checks": [
            "selected_standard_script_identified",
            "Latin_Cyrillic_or_Arabic_font_coverage",
            "transliteration_or_orthography_rule_manifest",
            "PDF_copy_paste_unicode_check",
        ],
        "required_script_governance_checks": [
            "family_adjacency_not_unified_standard",
            "reviewers_required_for_each_affected_standard",
            "script_standardization_reviewer_required_before_packet_population",
        ],
    },
    "source_first_reference_textbooks": {
        "profile": "source_reference_mixed_scripts",
        "script_systems": ["source dependent"],
        "writing_direction": "source_dependent",
        "required_render_checks": [
            "source_license_and_format_recorded",
            "reference_material_not_retypeset_as_lane_output",
            "math_display_integrity_if_excerpted_under_license",
            "PDF_or_TeX_source_quality_note",
        ],
        "required_script_governance_checks": [
            "reference_textbook_not_language_authority",
            "source_quality_reviewer_scope_recorded",
            "OER_reuse_boundary_recorded",
        ],
    },
    "south_asia_hindustani_indic_dravidian": {
        "profile": "south_asia_multi_script_scope_tbd",
        "script_systems": ["Devanagari", "Perso-Arabic", "Bengali", "Tamil", "Telugu", "Kannada", "Malayalam", "Gujarati", "Gurmukhi"],
        "writing_direction": "mixed_or_tbd",
        "required_render_checks": [
            "named_script_selected_before_render",
            "complex_script_font_shaping",
            "local_numeral_and_punctuation_policy",
            "PDF_copy_paste_unicode_check",
        ],
        "required_script_governance_checks": [
            "language_and_script_not_collapsed_into_region",
            "local_script_specific_reviewer_required",
            "education_context_review_required_before_edition_lane",
        ],
    },
}


def now_utc() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="microseconds")


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def load_json(path: pathlib.Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: pathlib.Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")


def artifact_path(path: pathlib.Path) -> str:
    return "noether-slavic-handoff/20260629/" + path.relative_to(BASE).as_posix()


def artifact_local_path(path_from_manifest: str) -> pathlib.Path:
    rel = path_from_manifest.split("20260629/", 1)[-1]
    return BASE / rel


def artifact_item(path: pathlib.Path, status: str | None = None) -> dict:
    item = {"path": artifact_path(path), "sha256": sha256(path), "bytes": path.stat().st_size}
    if status:
        item["status"] = status
    return item


def upsert_artifact(manifest: dict, group: str, path: pathlib.Path, status: str | None = None) -> None:
    by_path = {item["path"]: item for item in manifest["artifacts"][group]}
    rel = artifact_path(path)
    previous_status = by_path.get(rel, {}).get("status")
    by_path[rel] = artifact_item(path, status or previous_status)
    manifest["artifacts"][group] = [by_path[key] for key in sorted(by_path)]


def refresh_existing_artifact_hashes(manifest: dict) -> None:
    for group in ("json", "markdown", "scripts"):
        refreshed = []
        for item in manifest["artifacts"][group]:
            path = artifact_local_path(item["path"])
            if path.exists() and path.is_file():
                updated = dict(item)
                updated["sha256"] = sha256(path)
                updated["bytes"] = path.stat().st_size
                refreshed.append(updated)
            else:
                refreshed.append(item)
        manifest["artifacts"][group] = refreshed


def visual_or_script_roles(roles: list[str]) -> list[str]:
    markers = ["visual", "script", "rtl", "cjk", "sidecar", "tex_pdf"]
    return [role for role in roles if any(marker in role for marker in markers)]


def build_row(row_id: str, source: dict | None = None) -> dict:
    profile = PROFILES[row_id]
    source = source or {}
    required_roles = profile.get("required_reviewer_roles") or source.get("required_reviewer_roles", [])
    return {
        "row_id": f"render-script-{row_id.replace('_', '-')}",
        "lane_or_cohort": row_id,
        "kind": profile.get("kind", source.get("kind")),
        "label": profile.get("label", source.get("label")),
        "readiness_group": profile.get("readiness_group", source.get("readiness_group")),
        "render_script_profile": profile["profile"],
        "script_systems": profile["script_systems"],
        "writing_direction": profile["writing_direction"],
        "math_layout_risks": COMMON_MATH_LAYOUT_CHECKS,
        "required_render_checks": profile["required_render_checks"],
        "required_script_governance_checks": profile["required_script_governance_checks"],
        "common_script_governance_checks": COMMON_SCRIPT_GOVERNANCE_CHECKS,
        "prerequisite_gate": profile.get("prerequisite_gate", source.get("next_gate")),
        "upstream_blocker_class": profile.get("upstream_blocker_class", source.get("handoff_readiness_status")),
        "selected_witnesses": source.get("selected_witnesses", 0),
        "selected_witnesses_with_source_core": source.get("selected_witnesses_with_source_core", 0),
        "filesystem_missing_paths": source.get("filesystem_missing_paths", 0),
        "planned_delta_shelves": source.get("planned_delta_shelves", 0),
        "planned_delta_text_source_like_gap_files": source.get("planned_delta_text_source_like_gap_files", 0),
        "authority_packet_groups": source.get("authority_packet_groups", 0),
        "authority_reviewer_role_forms": source.get("authority_reviewer_role_forms", len(required_roles)),
        "required_reviewer_roles": required_roles,
        "visual_or_script_reviewer_roles": visual_or_script_roles(required_roles),
        "render_validation_status": "not_started_preflight_only",
        "script_sidecar_validation_status": "not_started_preflight_only",
        "render_output_artifacts": [],
        "input_artifacts": [
            "INTEGRATED_LANE_HANDOFF_READINESS_MATRIX_20260630.json",
            "EXTERNAL_AUTHORITY_REVIEW_QUEUE_20260630.json",
            "EXTERNAL_AUTHORITY_REVIEW_PACKET_FORMS_20260630.json",
        ],
        "output_artifacts_to_update_or_create": [
            "RENDER_SCRIPT_VALIDATION_PREFLIGHT_20260630.json",
            "RENDER_SCRIPT_VALIDATION_PREFLIGHT_20260630.md",
        ],
        "local_execution_allowed_without_network": True,
        "render_jobs_started": 0,
        "pdfs_created": 0,
        "visual_inspections_completed": 0,
        "script_sidecar_validations_completed": 0,
        "review_fields_filled": 0,
        "review_packets_sent": 0,
        "review_returns_received": 0,
        "external_reviews_performed": 0,
        "accepted_corrections_ingested": 0,
        "actual_render_performed": False,
        "visual_inspection_performed": False,
        "script_sidecar_validation_performed": False,
        "review_packet_population_performed": False,
        "translation_or_revision_performed": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "canonical_approval_status": "not_approved",
        "canonical_completion_claim": False,
        "publication_completion_claim": False,
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }


def build_document() -> dict:
    manifest = load_json(STATUS_MANIFEST)
    integrated = load_json(INTEGRATED_MATRIX_JSON)
    authority_queue = load_json(AUTHORITY_QUEUE_JSON)
    authority_forms = load_json(AUTHORITY_FORMS_JSON)
    support_notes = load_json(SUPPORT_NOTES_JSON)

    matrix_rows = {row["lane_or_cohort"]: row for row in integrated["lane_or_cohort_rows"]}
    rows = [build_row("slavic_reference")]
    for row_id in sorted(matrix_rows):
        rows.append(build_row(row_id, matrix_rows[row_id]))

    cjk_rows = [row for row in rows if row["writing_direction"] == "ltr" and row["render_script_profile"].startswith("cjk")]
    rtl_rows = [row for row in rows if row["writing_direction"] == "rtl"]
    latin_rows = [row for row in rows if row["render_script_profile"].startswith("latin_roman")]
    cyrillic_or_sidecar_rows = [
        row
        for row in rows
        if "Cyrillic" in row["script_systems"] or "sidecar" in row["render_script_profile"]
    ]
    mixed_or_tbd_rows = [row for row in rows if "tbd" in row["writing_direction"] or row["writing_direction"] == "source_dependent"]
    rows_with_visual_or_script_roles = [row for row in rows if row["visual_or_script_reviewer_roles"]]

    summary = {
        "render_script_rows": len(rows),
        "slavic_reference_rows": 1,
        "core_language_lane_rows": sum(1 for row in rows if row["kind"] == "core_language_lane"),
        "extension_cohort_rows": sum(1 for row in rows if row["kind"] == "extension_cohort"),
        "cjk_rows": len(cjk_rows),
        "rtl_rows": len(rtl_rows),
        "latin_rows": len(latin_rows),
        "cyrillic_or_sidecar_rows": len(cyrillic_or_sidecar_rows),
        "mixed_or_tbd_rows": len(mixed_or_tbd_rows),
        "rows_with_visual_or_script_reviewer_roles": len(rows_with_visual_or_script_roles),
        "authority_queue_rows_total": authority_queue["summary"]["total_authority_queue_rows"],
        "authority_packet_groups": authority_forms["summary"]["packet_groups"],
        "support_cohort_notes": support_notes["summary"]["support_cohort_notes"],
        "render_jobs_started": 0,
        "pdfs_created": 0,
        "visual_inspections_completed": 0,
        "script_sidecar_validations_completed": 0,
        "review_fields_filled": 0,
        "review_packets_sent": 0,
        "review_returns_received": 0,
        "external_reviews_performed": 0,
        "accepted_corrections_ingested": 0,
        "network_actions_performed": 0,
        "actual_render_performed": False,
        "visual_inspection_performed": False,
        "script_sidecar_validation_performed": False,
        "review_packet_population_performed": False,
        "translation_or_revision_performed": False,
        "canonical_completion_claim": False,
        "publication_completion_claim": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }

    return {
        "artifact": "render_script_validation_preflight",
        "status": STATUS,
        "generated_date": "2026-06-30",
        "generated_utc": now_utc(),
        "bandwidth_mode": "local_only_no_network_actions",
        "inputs": {
            "status_manifest": STATUS_MANIFEST.name,
            "integrated_matrix": INTEGRATED_MATRIX_JSON.name,
            "external_authority_review_queue": AUTHORITY_QUEUE_JSON.name,
            "external_authority_review_packet_forms": AUTHORITY_FORMS_JSON.name,
            "support_cohort_authority_notes": SUPPORT_NOTES_JSON.name,
        },
        "policy": {
            "preflight_only_no_render_jobs": True,
            "render_validation_before_canonical_pdf_claim": True,
            "script_sidecar_validation_before_sidecar_equivalence_claim": True,
            "rtl_and_cjk_require_visual_or_script_review": True,
            "support_cohorts_require_named_lane_before_render_claim": True,
            "local_mechanical_validation_is_not_native_review": True,
            "no_network_upload_or_download_performed": True,
        },
        "summary": summary,
        "preflight_rows": rows,
        "boundaries": [
            "This artifact is a render/script preflight matrix, not a render log.",
            "No TeX build, PDF render, visual inspection, reviewer packet population, or external review was performed.",
            "It copies no source-language passages and no source-language term strings.",
            "Support cohorts remain non-edition support shelves until explicitly promoted and reviewed.",
            "No network action, remote upload, or GitHub push was performed.",
        ],
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
        "canonical_completion_claim": False,
        "publication_completion_claim": False,
        "manifest_status_at_build_time": manifest.get("status"),
    }


def write_markdown(document: dict) -> None:
    summary = document["summary"]
    lines = [
        "# Render/Script Validation Preflight - 2026-06-30",
        "",
        "This local preflight records render and script obligations before future TeX/PDF or sidecar claims. It is not a render log, review result, or completion claim.",
        "",
        "## Summary",
        "",
        f"- Render/script rows: {summary['render_script_rows']}",
        f"- CJK rows: {summary['cjk_rows']}",
        f"- RTL rows: {summary['rtl_rows']}",
        f"- Latin rows: {summary['latin_rows']}",
        f"- Cyrillic or sidecar rows: {summary['cyrillic_or_sidecar_rows']}",
        f"- Mixed/TBD script rows: {summary['mixed_or_tbd_rows']}",
        "- Render jobs started: 0",
        "- PDFs created: 0",
        "- Visual inspections completed: 0",
        "- Script-sidecar validations completed: 0",
        "- Network actions performed: 0",
        "",
        "## Rows",
        "",
        "| Lane/cohort | Profile | Direction | Render status | Required visual/script roles |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in document["preflight_rows"]:
        roles = ", ".join(row["visual_or_script_reviewer_roles"]) or "none routed yet"
        lines.append(
            f"| {row['label']} | `{row['render_script_profile']}` | {row['writing_direction']} | "
            f"{row['render_validation_status']} | {roles} |"
        )
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- This matrix does not create or inspect rendered PDFs.",
            "- Render/script checks must be performed after upstream source-note or manual-review gates clear.",
            "- Local mechanical preflight does not replace native, visual, script, educator, or community review.",
            "- No source text, source-language term strings, credentials, reviewer returns, or accepted corrections are copied here.",
            "- No network action was performed.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def update_status_index(document: dict, manifest: dict) -> None:
    text = STATUS_INDEX.read_text(encoding="utf-8")
    summary = document["summary"]
    line = (
        "- Render/script validation preflight: "
        f"{summary['render_script_rows']} rows / "
        f"{summary['cjk_rows']} CJK / "
        f"{summary['rtl_rows']} RTL / "
        f"{summary['latin_rows']} Latin / "
        "0 renders"
    )
    if re.search(r"^- Render/script validation preflight: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Render/script validation preflight: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Support cohort authority notes:"
        rows = text.splitlines()
        inserted = False
        for offset, row in enumerate(rows):
            if row.startswith(marker):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                inserted = True
                break
        if not inserted:
            text = text.rstrip() + "\n" + line + "\n"
    text = text.replace(
        "integrated-handoff-readiness/lane-promotion-next-action/support-cohort-authority-note metadata",
        "integrated-handoff-readiness/lane-promotion-next-action/support-cohort-authority-note/render-script-preflight metadata",
    )
    if "Generated UTC: " in text:
        old = text.split("Generated UTC: ", 1)[1].splitlines()[0]
        text = text.replace(old, manifest["generated_utc"], 1)
    STATUS_INDEX.write_text(text, encoding="utf-8")


def update_manifest(document: dict) -> None:
    manifest = load_json(STATUS_MANIFEST)
    manifest["generated_utc"] = now_utc()
    upsert_artifact(manifest, "json", OUT_JSON, STATUS)
    upsert_artifact(manifest, "markdown", OUT_MD)
    upsert_artifact(manifest, "scripts", SELF_PATH)
    summary = document["summary"]
    manifest["render_script_validation_preflight"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "render_script_rows": summary["render_script_rows"],
        "slavic_reference_rows": summary["slavic_reference_rows"],
        "core_language_lane_rows": summary["core_language_lane_rows"],
        "extension_cohort_rows": summary["extension_cohort_rows"],
        "cjk_rows": summary["cjk_rows"],
        "rtl_rows": summary["rtl_rows"],
        "latin_rows": summary["latin_rows"],
        "cyrillic_or_sidecar_rows": summary["cyrillic_or_sidecar_rows"],
        "mixed_or_tbd_rows": summary["mixed_or_tbd_rows"],
        "rows_with_visual_or_script_reviewer_roles": summary["rows_with_visual_or_script_reviewer_roles"],
        "authority_queue_rows_total": summary["authority_queue_rows_total"],
        "authority_packet_groups": summary["authority_packet_groups"],
        "support_cohort_notes": summary["support_cohort_notes"],
        "render_jobs_started": 0,
        "pdfs_created": 0,
        "visual_inspections_completed": 0,
        "script_sidecar_validations_completed": 0,
        "review_fields_filled": 0,
        "review_packets_sent": 0,
        "review_returns_received": 0,
        "external_reviews_performed": 0,
        "accepted_corrections_ingested": 0,
        "network_actions_performed": 0,
        "actual_render_performed": False,
        "visual_inspection_performed": False,
        "script_sidecar_validation_performed": False,
        "review_packet_population_performed": False,
        "translation_or_revision_performed": False,
        "canonical_completion_claim": False,
        "publication_completion_claim": False,
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }
    update_status_index(document, manifest)
    refresh_existing_artifact_hashes(manifest)
    write_json(STATUS_MANIFEST, manifest)


def main() -> None:
    document = build_document()
    write_json(OUT_JSON, document)
    write_markdown(document)
    update_manifest(document)
    print(
        json.dumps(
            {
                "render_script_validation_preflight_json": str(OUT_JSON),
                "render_script_rows": document["summary"]["render_script_rows"],
                "cjk_rows": document["summary"]["cjk_rows"],
                "rtl_rows": document["summary"]["rtl_rows"],
                "latin_rows": document["summary"]["latin_rows"],
                "render_jobs_started": document["summary"]["render_jobs_started"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
