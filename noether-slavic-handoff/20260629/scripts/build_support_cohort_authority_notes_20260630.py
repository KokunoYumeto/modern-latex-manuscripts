import datetime
import hashlib
import json
import pathlib
import re


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
INTEGRATED_MATRIX_JSON = BASE / "INTEGRATED_LANE_HANDOFF_READINESS_MATRIX_20260630.json"
LANE_QUEUE_JSON = BASE / "LANE_PROMOTION_NEXT_ACTION_QUEUE_20260630.json"
AUTHORITY_QUEUE_JSON = BASE / "EXTERNAL_AUTHORITY_REVIEW_QUEUE_20260630.json"
METHODOLOGY_CROSSWALK_JSON = BASE / "METHODOLOGY_PUBLICATION_CROSSWALK_20260630.json"
OUT_JSON = BASE / "SUPPORT_COHORT_AUTHORITY_NOTES_20260630.json"
OUT_MD = BASE / "SUPPORT_COHORT_AUTHORITY_NOTES_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "support_cohort_authority_notes_local_only_not_review_result"

COHORT_DETAILS = {
    "africa_deep_gap": {
        "usefulness": "Tracks African-language and local education support shelves where source scarcity, colonial-language mediation, or local classroom authority may be central.",
        "candidate_registers": [
            "Swahili or other regional lingua-franca mathematics registers",
            "Amharic, Hausa, Yoruba, Zulu, or other local-language technical education contexts",
            "locally authored university or teacher-training material where available",
        ],
        "non_edition_boundary": "Do not promote an African-language edition lane from metadata alone; require local educator/community and mathematical-register review first.",
        "anti_extractive_note": "Open-source availability must mean local editability, rejection, and forkability, not a claim that this PC branch owns or speaks for a local register.",
    },
    "east_southeast_asia_pacific": {
        "usefulness": "Keeps East, Southeast Asian, and Pacific evidence shelves visible for later language-lane promotion where local TeX/text corpora already exist.",
        "candidate_registers": [
            "Korean, Vietnamese, Thai, Indonesian, Malay, Tagalog, or Pacific education contexts",
            "university algebra, number theory, and mathematical physics sources",
            "script-specific render and terminology conventions before any translation pass",
        ],
        "non_edition_boundary": "Treat the cohort as source evidence only until a named language lane, reviewer authority, script/render plan, and glossary governance are created.",
        "anti_extractive_note": "Regional grouping is only a triage convenience; it must not flatten distinct languages, scripts, or education systems.",
    },
    "methodology_interlanguage_access": {
        "usefulness": "Preserves the semi-constructed, constructed, and interlanguage methodology lane as publishable research support for technical-register construction.",
        "candidate_registers": [
            "zonal interlanguage projects with their own authority structures",
            "constructed-language pilots framed as opt-in educational or methodological experiments",
            "computational interlingua or machine-translation pivot studies kept separate from language standards",
        ],
        "non_edition_boundary": "Interlanguage or constructed-language pilots remain research/pilot material unless external project, pedagogy, and mathematical review authorize stronger use.",
        "anti_extractive_note": "Authority must be explicit: project communities, learners, educators, and reviewers can reject, fork, or narrow any proposed register.",
    },
    "pan_turkic_adjacent": {
        "usefulness": "Captures Turkic-family adjacency as a possible future bridge problem involving script, orthography, and cross-register governance.",
        "candidate_registers": [
            "Turkish, Azerbaijani, Uzbek, Kazakh, Kyrgyz, Tatar, or other Turkic technical registers",
            "Latin, Cyrillic, and Arabic-script governance questions where relevant",
            "algebra and number theory material with local university provenance",
        ],
        "non_edition_boundary": "Do not treat Turkic adjacency as a unified lane without reviewers for each affected standard and script.",
        "anti_extractive_note": "Family-level usefulness does not create authority to collapse national, regional, or script communities.",
    },
    "source_first_reference_textbooks": {
        "usefulness": "Keeps broad source-first undergraduate mathematics and physics textbooks available as reference evidence before translation choices are made.",
        "candidate_registers": [
            "open algebra, linear algebra, number theory, and mathematical physics textbooks",
            "source-first examples useful for terminology, exposition, and curricular comparison",
            "license-clear reference material for later reviewer packets",
        ],
        "non_edition_boundary": "Reference textbooks support evidence and pedagogy analysis; they are not themselves language-lane approval or canonical Noether editions.",
        "anti_extractive_note": "Reuse must stay license-aware and reviewer-aware; open reference material is not a substitute for local language authority.",
    },
    "south_asia_hindustani_indic_dravidian": {
        "usefulness": "Tracks South Asian language-family evidence shelves where script, regional standard, and education-system differences can matter as much as terminology.",
        "candidate_registers": [
            "Hindi, Urdu, Bengali, Tamil, Telugu, Marathi, Kannada, Malayalam, Gujarati, Punjabi, or related technical registers",
            "Devanagari, Perso-Arabic, Bengali, Tamil, Telugu, Kannada, Malayalam, Gujarati, or Gurmukhi script handling where relevant",
            "local university algebra, physics, and teacher-training material",
        ],
        "non_edition_boundary": "Do not collapse South Asian languages or scripts into one edition lane; promotion requires a named lane and local/script-specific review.",
        "anti_extractive_note": "Support shelves must leave ownership, adaptation, and rejection with local educators and language users.",
    },
}

COMMON_PROMOTION_REQUIREMENTS = [
    "name a single language, register, or explicitly governed pilot scope",
    "identify source witnesses before translation or revision",
    "separate observed source anchors from project-proposed terminology",
    "define script, orthography, transliteration, and render-validation duties",
    "create reviewer packet roles before learner-facing or canonical claims",
    "record accepted corrections through the correction ledger before promotion",
]


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


def build_document() -> dict:
    matrix = load_json(INTEGRATED_MATRIX_JSON)
    lane_queue = load_json(LANE_QUEUE_JSON)
    authority_queue = load_json(AUTHORITY_QUEUE_JSON)
    crosswalk = load_json(METHODOLOGY_CROSSWALK_JSON)

    matrix_rows = {
        row["lane_or_cohort"]: row
        for row in matrix["lane_or_cohort_rows"]
        if row.get("kind") == "extension_cohort"
    }
    queue_rows = {
        row["lane_or_cohort"]: row
        for row in lane_queue["lane_action_rows"]
        if row.get("kind") == "extension_cohort"
    }

    notes = []
    for cohort_id in sorted(COHORT_DETAILS):
        matrix_row = matrix_rows[cohort_id]
        queue_row = queue_rows[cohort_id]
        detail = COHORT_DETAILS[cohort_id]
        notes.append(
            {
                "cohort_id": cohort_id,
                "label": matrix_row["label"],
                "kind": "extension_cohort",
                "authority_note_status": "drafted_support_authority_note_not_review_result",
                "edition_status": "support_cohort_not_canonical_edition_lane",
                "current_handoff_readiness_status": matrix_row["handoff_readiness_status"],
                "next_gate": matrix_row["next_gate"],
                "source_gate_use": matrix_row["source_gate_use"],
                "usefulness": detail["usefulness"],
                "candidate_registers": detail["candidate_registers"],
                "non_edition_boundary": detail["non_edition_boundary"],
                "anti_extractive_note": detail["anti_extractive_note"],
                "promotion_requirements": COMMON_PROMOTION_REQUIREMENTS,
                "selected_witnesses": matrix_row["selected_witnesses"],
                "selected_witnesses_with_source_core": matrix_row["selected_witnesses_with_source_core"],
                "filesystem_missing_paths": matrix_row["filesystem_missing_paths"],
                "planned_delta_shelves": matrix_row["planned_delta_shelves"],
                "planned_delta_text_source_like_gap_files": matrix_row["planned_delta_text_source_like_gap_files"],
                "inspection_tasks": matrix_row["inspection_tasks"],
                "support_cohort_tasks": queue_row["support_cohort_tasks"],
                "authority_packet_groups": matrix_row["authority_packet_groups"],
                "authority_reviewer_role_forms": matrix_row["authority_reviewer_role_forms"],
                "required_reviewer_roles": matrix_row["required_reviewer_roles"],
                "input_artifacts": queue_row["input_artifacts"],
                "output_artifacts_to_update_or_create": [
                    "SUPPORT_COHORT_AUTHORITY_NOTES_20260630.json",
                    "SUPPORT_COHORT_AUTHORITY_NOTES_20260630.md",
                    "EXTERNAL_AUTHORITY_REVIEW_PACKET_FORMS_20260630.json",
                ],
                "local_execution_allowed_without_network": True,
                "review_fields_filled": 0,
                "review_packets_sent": 0,
                "review_returns_received": 0,
                "external_reviews_performed": 0,
                "accepted_corrections_ingested": 0,
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
        )

    summary = {
        "support_cohort_notes": len(notes),
        "extension_cohort_action_rows": len(queue_rows),
        "selected_witnesses": sum(row["selected_witnesses"] for row in notes),
        "selected_witnesses_with_source_core": sum(row["selected_witnesses_with_source_core"] for row in notes),
        "filesystem_missing_paths": sum(row["filesystem_missing_paths"] for row in notes),
        "planned_delta_shelves": sum(row["planned_delta_shelves"] for row in notes),
        "planned_delta_text_source_like_gap_files": sum(row["planned_delta_text_source_like_gap_files"] for row in notes),
        "inspection_tasks": sum(row["inspection_tasks"] for row in notes),
        "support_cohort_tasks": sum(row["support_cohort_tasks"] for row in notes),
        "authority_packet_groups": sum(row["authority_packet_groups"] for row in notes),
        "authority_reviewer_role_forms": sum(row["authority_reviewer_role_forms"] for row in notes),
        "methodology_claim_taxonomy_rows": len(crosswalk.get("claim_taxonomy", [])),
        "authority_queue_rows_total": authority_queue["summary"]["total_authority_queue_rows"],
        "network_actions_performed": 0,
        "review_fields_filled": 0,
        "review_packets_sent": 0,
        "review_returns_received": 0,
        "external_reviews_performed": 0,
        "accepted_corrections_ingested": 0,
        "review_packet_population_performed": False,
        "translation_or_revision_performed": False,
        "canonical_completion_claim": False,
        "publication_completion_claim": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }

    return {
        "artifact": "support_cohort_authority_notes",
        "status": STATUS,
        "generated_date": "2026-06-30",
        "generated_utc": now_utc(),
        "bandwidth_mode": "local_only_no_network_actions",
        "inputs": {
            "status_manifest": STATUS_MANIFEST.name,
            "integrated_matrix": INTEGRATED_MATRIX_JSON.name,
            "lane_promotion_next_action_queue": LANE_QUEUE_JSON.name,
            "external_authority_review_queue": AUTHORITY_QUEUE_JSON.name,
            "methodology_publication_crosswalk": METHODOLOGY_CROSSWALK_JSON.name,
        },
        "policy": {
            "support_cohort_is_not_edition_lane": True,
            "source_witnesses_before_translation_or_revision": True,
            "external_authority_before_native_or_community_claims": True,
            "open_source_handoff_is_auditability_not_ownership_transfer": True,
            "regional_family_grouping_is_triage_not_language_authority": True,
            "local_mechanical_validation_is_not_native_review": True,
            "no_network_upload_or_download_performed": True,
        },
        "summary": summary,
        "cohort_notes": notes,
        "boundaries": [
            "These notes draft local authority and usefulness boundaries for support cohorts only.",
            "They do not promote any support cohort into a canonical edition lane.",
            "They copy no source-language passages and no source-language term strings.",
            "They do not claim native, educator, community, or project authority review.",
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
        "manifest_status_at_build_time": load_json(STATUS_MANIFEST).get("status"),
    }


def write_markdown(document: dict) -> None:
    summary = document["summary"]
    lines = [
        "# Support Cohort Authority Notes - 2026-06-30",
        "",
        "These local notes preserve the support-cohort boundary for the Noether multilingual workflow. They are not review results and do not promote any support cohort into a canonical edition lane.",
        "",
        "## Summary",
        "",
        f"- Support cohort notes: {summary['support_cohort_notes']}",
        f"- Selected witness slots: {summary['selected_witnesses']}",
        f"- Authority reviewer-role forms routed: {summary['authority_reviewer_role_forms']}",
        f"- Planned text/source-like gap files: {summary['planned_delta_text_source_like_gap_files']}",
        "- Network actions performed: 0",
        "- Native/external reviews performed: 0",
        "- Approved terms: 0",
        "- Accepted corrections: 0",
        "",
        "## Cohort Notes",
        "",
    ]
    for row in document["cohort_notes"]:
        lines.extend(
            [
                f"### {row['label']}",
                "",
                f"- Cohort ID: `{row['cohort_id']}`",
                f"- Status: {row['authority_note_status']}",
                f"- Edition boundary: {row['edition_status']}",
                f"- Usefulness: {row['usefulness']}",
                f"- Non-edition boundary: {row['non_edition_boundary']}",
                f"- Anti-extractive/open-source note: {row['anti_extractive_note']}",
                f"- Reviewer roles: {', '.join(row['required_reviewer_roles'])}",
                f"- Selected witnesses: {row['selected_witnesses']} ({row['selected_witnesses_with_source_core']} source-core-backed)",
                f"- Planned text/source-like gap files: {row['planned_delta_text_source_like_gap_files']}",
                "",
                "Candidate registers or evidence directions:",
            ]
        )
        for item in row["candidate_registers"]:
            lines.append(f"- {item}")
        lines.extend(["", "Promotion requirements before an edition lane exists:"])
        for item in row["promotion_requirements"]:
            lines.append(f"- {item}")
        lines.append("")

    lines.extend(
        [
            "## Boundaries",
            "",
            "- Support cohorts are evidence and methodology scaffolds, not canonical editions.",
            "- Regional or family groupings are triage devices only.",
            "- Open-source handoff means auditability, local editability, rejection, and forkability; it is not community consent by itself.",
            "- Source text, source-language term strings, credentials, reviewer returns, and accepted corrections are not copied here.",
            "- No network action was performed.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def update_status_index(document: dict, manifest: dict) -> None:
    text = STATUS_INDEX.read_text(encoding="utf-8")
    summary = document["summary"]
    line = (
        "- Support cohort authority notes: "
        f"{summary['support_cohort_notes']} cohorts / "
        f"{summary['selected_witnesses']} selected witnesses / "
        f"{summary['authority_reviewer_role_forms']} reviewer-role forms / "
        "0 network actions"
    )
    if re.search(r"^- Support cohort authority notes: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Support cohort authority notes: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Lane promotion next-action queue:"
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
        "integrated-handoff-readiness/lane-promotion-next-action metadata",
        "integrated-handoff-readiness/lane-promotion-next-action/support-cohort-authority-note metadata",
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
    manifest["support_cohort_authority_notes"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "support_cohort_notes": summary["support_cohort_notes"],
        "extension_cohort_action_rows": summary["extension_cohort_action_rows"],
        "selected_witnesses": summary["selected_witnesses"],
        "selected_witnesses_with_source_core": summary["selected_witnesses_with_source_core"],
        "filesystem_missing_paths": summary["filesystem_missing_paths"],
        "planned_delta_shelves": summary["planned_delta_shelves"],
        "planned_delta_text_source_like_gap_files": summary["planned_delta_text_source_like_gap_files"],
        "inspection_tasks": summary["inspection_tasks"],
        "support_cohort_tasks": summary["support_cohort_tasks"],
        "authority_packet_groups": summary["authority_packet_groups"],
        "authority_reviewer_role_forms": summary["authority_reviewer_role_forms"],
        "methodology_claim_taxonomy_rows": summary["methodology_claim_taxonomy_rows"],
        "authority_queue_rows_total": summary["authority_queue_rows_total"],
        "network_actions_performed": 0,
        "review_fields_filled": 0,
        "review_packets_sent": 0,
        "review_returns_received": 0,
        "external_reviews_performed": 0,
        "accepted_corrections_ingested": 0,
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
                "support_cohort_authority_notes_json": str(OUT_JSON),
                "support_cohort_notes": document["summary"]["support_cohort_notes"],
                "selected_witnesses": document["summary"]["selected_witnesses"],
                "authority_reviewer_role_forms": document["summary"]["authority_reviewer_role_forms"],
                "network_actions_performed": document["summary"]["network_actions_performed"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
