import datetime
import hashlib
import json
import pathlib
import re


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
INTERLANGUAGE_METHOD_MD = BASE / "INTERLANGUAGE_CONSTRUCTED_LANGUAGE_METHOD_LANE_20260629.md"
BIBLIOGRAPHY_JSON = BASE / "INTERLANGUAGE_METHOD_BIBLIOGRAPHY_AUTHORITY_MATRIX_20260629.json"
AUTHORITY_FRAMEWORK_JSON = BASE / "INTERLANGUAGE_REVIEWER_AUTHORITY_DECISION_FRAMEWORK_20260629.json"
PUBLICATION_OUTLINE_JSON = BASE / "AI_TECHNICAL_REGISTER_PUBLICATION_OUTLINE_20260629.json"
SELECTION_MATRIX_JSON = BASE / "LOCAL_SOURCE_WITNESS_SELECTION_MATRIX_20260630.json"
INSPECTION_PACKET_JSON = BASE / "SELECTED_SOURCE_WITNESS_INSPECTION_PACKET_20260630.json"
FILESYSTEM_VALIDATION_JSON = BASE / "SELECTED_SOURCE_WITNESS_FILESYSTEM_VALIDATION_20260630.json"
DELTA_STAGING_JSON = BASE / "SELECTED_SOURCE_WITNESS_TEXT_TEX_DELTA_STAGING_PLAN_20260630.json"
OUT_JSON = BASE / "METHODOLOGY_PUBLICATION_CROSSWALK_20260630.json"
OUT_MD = BASE / "METHODOLOGY_PUBLICATION_CROSSWALK_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "methodology_publication_crosswalk_no_network_no_authority_claim"


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


def case_study_evidence(lane: str) -> dict:
    common = {
        "claim_status": "case_study_evidence_available_not_completion_claim",
        "native_or_external_authority_status": "not_reviewed_or_not_proven_here",
        "canonical_completion_status": "not_complete_for_non_slavic_lanes",
    }
    if lane == "ukrainian_russian_interslavic_panslavic":
        common.update(
            {
                "evidence_artifacts": ["prior Slavic handoff pointers", "status manifest", "review packet scaffolds"],
                "mechanical_claims_now": ["completed/review-ready lane is represented by prior checkpoint pointers"],
                "blocked_claims": ["new review-return corrections require ingestion before further completion claims"],
            }
        )
    elif lane == "simplified_chinese":
        common.update(
            {
                "evidence_artifacts": [
                    "SIMPLIFIED_CHINESE_TERM_ANCHOR_SEED_20260629.json",
                    "CHINESE_SOURCE_EVIDENCE_REINFORCEMENT_20260629.json",
                    "selected witness inspection packet",
                ],
                "mechanical_claims_now": ["manual/source-review tasks are routed to selected local witnesses"],
                "blocked_claims": ["native review and page-context note completion"],
            }
        )
    elif lane == "french_spanish":
        common.update(
            {
                "evidence_artifacts": [
                    "ROMANCE_FRENCH_SPANISH_TERM_ANCHOR_SEED_20260629.json",
                    "READY_CONTEXT_NOTE_ENTRY_PACKET_FRENCH_JAPANESE_20260630.json",
                    "selected source-witness filesystem validation",
                ],
                "mechanical_claims_now": ["French ready-note tasks and Spanish manual-review tasks are routed"],
                "blocked_claims": ["French page-context notes and Spanish manual/source review remain blank"],
            }
        )
    elif lane == "japanese":
        common.update(
            {
                "evidence_artifacts": [
                    "JAPANESE_TERM_ANCHOR_SEED_20260629.json",
                    "READY_CONTEXT_NOTE_ENTRY_PACKET_FRENCH_JAPANESE_20260630.json",
                    "selected source-witness filesystem validation",
                ],
                "mechanical_claims_now": ["Japanese ready-note tasks are routed to selected witnesses"],
                "blocked_claims": ["page-context notes and native mathematical review"],
            }
        )
    elif lane == "persian_family_registers":
        common.update(
            {
                "evidence_artifacts": [
                    "PERSIAN_FAMILY_ARABIC_TERM_ANCHOR_SEED_20260629.json",
                    "PERSIAN_FAMILY_DARI_TAJIK_REGISTER_GAP_20260629.json",
                    "source-core coverage gap plan",
                ],
                "mechanical_claims_now": ["fa_IR, prs_AF, and tg_Cyrl_TJ are separated by gate and witness status"],
                "blocked_claims": ["cross-register authority, Tajik term-anchor promotion, and Farsi source-core delta"],
            }
        )
    elif lane == "arabic":
        common.update(
            {
                "evidence_artifacts": [
                    "ARABIC_SOURCE_EVIDENCE_REINFORCEMENT_20260629.json",
                    "MANUAL_SOURCE_REVIEW_PACKET_BLOCKED_LANES_20260630.json",
                    "selected witness inspection packet",
                ],
                "mechanical_claims_now": ["Arabic manual/source-review tasks are routed with RTL/OCR cautions"],
                "blocked_claims": ["native Arabic mathematical review and RTL render inspection"],
            }
        )
    elif lane == "interlanguage_constructed_pilot":
        common.update(
            {
                "evidence_artifacts": [
                    "INTERLANGUAGE_METHOD_BIBLIOGRAPHY_AUTHORITY_MATRIX_20260629.json",
                    "INTERLANGUAGE_REVIEWER_AUTHORITY_DECISION_FRAMEWORK_20260629.json",
                    "AI_TECHNICAL_REGISTER_PUBLICATION_OUTLINE_20260629.json",
                ],
                "mechanical_claims_now": ["research and authority framework exists as a publication lane"],
                "blocked_claims": ["constructed or semi-constructed pilots are not canonical editions without external review"],
            }
        )
    return common


def claim_taxonomy() -> list[dict]:
    return [
        {
            "claim_type": "mechanical_validation",
            "can_be_supported_now_by": ["hash checks", "count validators", "path existence checks", "no-copy boundary scans"],
            "cannot_support": ["native acceptability", "pedagogical usefulness", "community consent"],
            "current_artifact_examples": ["status manifest validator", "filesystem validation", "sync ledger"],
        },
        {
            "claim_type": "source_evidence",
            "can_be_supported_now_by": ["source shelves", "witness shortlists", "selected witness inspection packet"],
            "cannot_support": ["term approval", "translation quality"],
            "current_artifact_examples": ["local source evidence inventory", "source-witness selection matrix"],
        },
        {
            "claim_type": "terminology_anchor",
            "can_be_supported_now_by": ["term-anchor rows", "page counts", "blank note/review forms"],
            "cannot_support": ["approved glossary", "canonical terminology"],
            "current_artifact_examples": ["term anchor seeds", "page context note worklist"],
        },
        {
            "claim_type": "review_authority",
            "can_be_supported_now_by": ["review packet templates", "reviewer role requirements", "authority framework"],
            "cannot_support": ["completed review when fields remain blank"],
            "current_artifact_examples": ["manual source review packet", "interlanguage reviewer framework"],
        },
        {
            "claim_type": "open_source_handoff",
            "can_be_supported_now_by": ["manifest", "sync ledger", "source-core split plan", "delta staging plan"],
            "cannot_support": ["community ownership or consent by itself"],
            "current_artifact_examples": ["GitHub PC branch sync ledger", "text/TeX delta staging plan"],
        },
        {
            "claim_type": "educational_utility",
            "can_be_supported_now_by": ["curricular target notes", "undergraduate math/physics scope", "OER framing"],
            "cannot_support": ["classroom adoption without teacher/user review"],
            "current_artifact_examples": ["publication outline", "authority decision framework"],
        },
        {
            "claim_type": "canonical_edition",
            "can_be_supported_now_by": ["rendered artifacts", "review-return ledgers", "accepted corrections", "native/external review"],
            "cannot_support": ["completion from local evidence shelves alone"],
            "current_artifact_examples": ["Slavic handoff pointers", "accepted correction ledger template"],
        },
    ]


def build_document(manifest: dict) -> dict:
    bibliography = load_json(BIBLIOGRAPHY_JSON)
    authority = load_json(AUTHORITY_FRAMEWORK_JSON)
    outline = load_json(PUBLICATION_OUTLINE_JSON)
    selection = load_json(SELECTION_MATRIX_JSON)
    inspection = load_json(INSPECTION_PACKET_JSON)
    filesystem = load_json(FILESYSTEM_VALIDATION_JSON)
    delta = load_json(DELTA_STAGING_JSON)

    case_studies = []
    for row in outline.get("case_study_lanes", []):
        item = dict(row)
        item.update(case_study_evidence(row.get("lane")))
        case_studies.append(item)

    claims_allowed = list(outline.get("claims_allowed_now", [])) + [
        "selected non-Slavic witness shelves have metadata-only path validation",
        "selected witness text/TeX source-core gaps have a no-archive staging plan",
    ]
    claims_not_allowed = list(outline.get("claims_not_allowed_yet", [])) + [
        "metadata-only source-core gap plans are uploaded source material",
        "blank selected-witness inspection tasks are completed review",
    ]

    return {
        "artifact": "methodology_publication_crosswalk",
        "status": STATUS,
        "generated_date": "2026-06-30",
        "generated_utc": now_utc(),
        "bandwidth_mode": "local_only_no_network_actions",
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
        "inputs": {
            "interlanguage_method_lane_note": INTERLANGUAGE_METHOD_MD.name,
            "interlanguage_bibliography_authority_matrix": BIBLIOGRAPHY_JSON.name,
            "interlanguage_reviewer_authority_framework": AUTHORITY_FRAMEWORK_JSON.name,
            "publication_outline": PUBLICATION_OUTLINE_JSON.name,
            "source_witness_selection_matrix": SELECTION_MATRIX_JSON.name,
            "selected_witness_inspection_packet": INSPECTION_PACKET_JSON.name,
            "selected_witness_filesystem_validation": FILESYSTEM_VALIDATION_JSON.name,
            "selected_witness_delta_staging_plan": DELTA_STAGING_JSON.name,
            "status_manifest": STATUS_MANIFEST.name,
        },
        "summary": {
            "working_titles": len(outline.get("working_titles", [])),
            "case_study_lanes": len(case_studies),
            "method_sections": len(outline.get("method_sections", [])),
            "claim_taxonomy_rows": len(claim_taxonomy()),
            "authority_lane_types": len(bibliography.get("authority_matrix", [])),
            "review_authority_checklists": len(authority.get("review_authority_checklists", [])),
            "scholarly_policy_anchors": len(authority.get("scholarly_and_policy_anchors", [])),
            "zonal_interlanguage_project_sources": sum(
                1 for row in bibliography.get("project_sources", []) if "interlanguage" in row.get("category", "")
            ),
            "selected_witness_lanes_or_cohorts": selection.get("summary", {}).get("lane_or_cohort_count", 0),
            "selected_witness_inspection_tasks": inspection.get("summary", {}).get("inspection_task_count", 0),
            "selected_witness_unique_shelves_validated": filesystem.get("summary", {}).get("unique_witness_shelves", 0),
            "planned_text_tex_delta_shelves": delta.get("summary", {}).get("planned_delta_shelves", 0),
            "claims_allowed_now": len(claims_allowed),
            "claims_not_allowed_yet": len(claims_not_allowed),
            "native_review_status": "not_reviewed",
            "canonical_completion_claim": False,
            "publication_completion_claim": False,
            "review_packet_population_performed": False,
            "translation_or_revision_performed": False,
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
        },
        "core_thesis": outline.get("core_thesis"),
        "working_titles": outline.get("working_titles", []),
        "case_study_crosswalk": case_studies,
        "claim_taxonomy": claim_taxonomy(),
        "method_section_crosswalk": [
            {
                "section": section,
                "source_artifact_support": "existing_noether_handoff_artifacts",
                "authority_boundary": "mechanical_or_evidential_claim_only_until_external_review",
            }
            for section in outline.get("method_sections", [])
        ],
        "authority_lane_types": bibliography.get("authority_matrix", []),
        "review_authority_checklists": authority.get("review_authority_checklists", []),
        "claims_allowed_now": claims_allowed,
        "claims_not_allowed_yet": claims_not_allowed,
        "publication_next_gates": [
            "convert crosswalk into article/report draft sections",
            "keep constructed/semi-constructed pilots as methodology examples unless reviewed",
            "tie each non-Slavic lane claim to selected witness inspection output after notes are filled",
            "record reviewer returns and accepted corrections before any canonical-edition claim",
        ],
        "boundaries": [
            "This crosswalk copies no source-language passages and no source-language term strings.",
            "It is a publication-methodology scaffold, not a completed paper or authority review.",
            "It does not claim native acceptability, community consent, or canonical completion.",
            "Open-source handoff is treated as auditability and forkability, not ownership transfer by itself.",
            "No network action was performed.",
        ],
    }


def write_markdown(document: dict) -> None:
    summary = document["summary"]
    lines = [
        "# Methodology publication crosswalk - 2026-06-30",
        "",
        "Status: publication-methodology crosswalk only. No network action, authority review, translation, or source-passage copying was performed.",
        "",
        "## Summary",
        "",
        f"- Working titles: {summary['working_titles']}",
        f"- Case-study lanes: {summary['case_study_lanes']}",
        f"- Method sections: {summary['method_sections']}",
        f"- Claim taxonomy rows: {summary['claim_taxonomy_rows']}",
        f"- Authority lane types: {summary['authority_lane_types']}",
        f"- Review authority checklists: {summary['review_authority_checklists']}",
        f"- Selected witness inspection tasks linked: {summary['selected_witness_inspection_tasks']}",
        f"- Planned text/TeX delta shelves linked: {summary['planned_text_tex_delta_shelves']}",
        f"- Canonical completion claim: `{str(summary['canonical_completion_claim']).lower()}`",
        "",
        "## Case Study Crosswalk",
        "",
        "| Lane | Research role | Claim status | Authority status |",
        "| --- | --- | --- | --- |",
    ]
    for row in document["case_study_crosswalk"]:
        lines.append(
            f"| `{row['lane']}` | {row['research_role']} | `{row['claim_status']}` | `{row['native_or_external_authority_status']}` |"
        )
    lines.extend(["", "## Claim Taxonomy", ""])
    lines.extend(f"- `{row['claim_type']}`: can be supported by {', '.join(row['can_be_supported_now_by'])}" for row in document["claim_taxonomy"])
    lines.extend(["", "## Claims Not Allowed Yet", ""])
    lines.extend(f"- {claim}" for claim in document["claims_not_allowed_yet"])
    lines.extend(["", "## Boundaries", ""])
    lines.extend(f"- {boundary}" for boundary in document["boundaries"])
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def update_status_index(document: dict, manifest: dict) -> None:
    text = STATUS_INDEX.read_text(encoding="utf-8")
    counts = {
        "json": len(manifest["artifacts"]["json"]),
        "markdown": len(manifest["artifacts"]["markdown"]),
        "scripts": len(manifest["artifacts"]["scripts"]),
    }
    text = re.sub(
        r"- JSON artifacts indexed: \d+ plus this status manifest",
        f"- JSON artifacts indexed: {counts['json']} plus this status manifest",
        text,
    )
    text = re.sub(
        r"- Markdown artifacts indexed: \d+ plus this status index",
        f"- Markdown artifacts indexed: {counts['markdown']} plus this status index",
        text,
    )
    text = re.sub(
        r"- Reproducible scripts indexed: \d+",
        f"- Reproducible scripts indexed: {counts['scripts']}",
        text,
    )
    summary = document["summary"]
    line = (
        "- Methodology publication crosswalk: "
        f"{summary['case_study_lanes']} case-study lanes / "
        f"{summary['claim_taxonomy_rows']} claim taxonomy rows / "
        f"{summary['review_authority_checklists']} authority checklists / "
        "0 network actions"
    )
    if re.search(r"^- Methodology publication crosswalk: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Methodology publication crosswalk: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Selected source-witness text/TeX delta staging plan:"
        rows = text.splitlines()
        for offset, row in enumerate(rows):
            if row.startswith(marker):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                break
    text = text.replace(
        "source-core-gap/delta-staging metadata",
        "source-core-gap/delta-staging/methodology-publication-crosswalk metadata",
    )
    text = text.replace(
        "methodology-publication-crosswalk/methodology-publication-crosswalk metadata",
        "methodology-publication-crosswalk metadata",
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
    refresh_existing_artifact_hashes(manifest)
    summary = document["summary"]
    manifest["methodology_publication_crosswalk"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "working_titles": summary["working_titles"],
        "case_study_lanes": summary["case_study_lanes"],
        "method_sections": summary["method_sections"],
        "claim_taxonomy_rows": summary["claim_taxonomy_rows"],
        "authority_lane_types": summary["authority_lane_types"],
        "review_authority_checklists": summary["review_authority_checklists"],
        "scholarly_policy_anchors": summary["scholarly_policy_anchors"],
        "zonal_interlanguage_project_sources": summary["zonal_interlanguage_project_sources"],
        "selected_witness_lanes_or_cohorts": summary["selected_witness_lanes_or_cohorts"],
        "selected_witness_inspection_tasks": summary["selected_witness_inspection_tasks"],
        "selected_witness_unique_shelves_validated": summary["selected_witness_unique_shelves_validated"],
        "planned_text_tex_delta_shelves": summary["planned_text_tex_delta_shelves"],
        "claims_allowed_now": summary["claims_allowed_now"],
        "claims_not_allowed_yet": summary["claims_not_allowed_yet"],
        "canonical_completion_claim": False,
        "publication_completion_claim": False,
        "review_packet_population_performed": False,
        "translation_or_revision_performed": False,
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }
    write_json(OUT_JSON, document)
    write_markdown(document)
    upsert_artifact(manifest, "json", OUT_JSON, STATUS)
    upsert_artifact(manifest, "markdown", OUT_MD)
    upsert_artifact(manifest, "scripts", SELF_PATH)
    refresh_existing_artifact_hashes(manifest)
    update_status_index(document, manifest)
    write_json(STATUS_MANIFEST, manifest)


def main() -> None:
    manifest = load_json(STATUS_MANIFEST)
    document = build_document(manifest)
    write_json(OUT_JSON, document)
    write_markdown(document)
    update_manifest(document)
    print(
        json.dumps(
            {
                "methodology_publication_crosswalk_json": str(OUT_JSON),
                "case_study_lanes": document["summary"]["case_study_lanes"],
                "claim_taxonomy_rows": document["summary"]["claim_taxonomy_rows"],
                "review_authority_checklists": document["summary"]["review_authority_checklists"],
                "claims_not_allowed_yet": document["summary"]["claims_not_allowed_yet"],
                "canonical_completion_claim": document["summary"]["canonical_completion_claim"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
