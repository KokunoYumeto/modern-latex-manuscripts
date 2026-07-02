import datetime
import hashlib
import json
import pathlib
import re


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
SOURCE_NOTE = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\MULTILINGUAL_CONSTRUCTED_LANGUAGE_PILOT_PACKET_COORDINATION_NOTE_20260630T180000Z.md"
)
OUT_JSON = BASE / "CONSTRUCTED_LANGUAGE_PILOT_COORDINATION_NOTE_INTAKE_20260630.json"
OUT_MD = BASE / "CONSTRUCTED_LANGUAGE_PILOT_COORDINATION_NOTE_INTAKE_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "methodology_support_cohort_coordination_note_pointer_not_canonical_not_publication_claim"
SOURCE_THREAD_ID = "019f1343-5922-78d3-b58e-6584dc556a14"

PACKET_SHAPE_CATEGORIES = [
    "proof_literacy_micro_packet",
    "set_function_packet",
    "numeracy_public_service_packet",
    "video_first_signed_language_packet",
    "source_authority_reader",
    "review_only_bridge_grammar_workbench",
    "return_ingestion_ledger",
]

NON_CLAIM_BOUNDARIES = [
    "canonical_readiness_claim",
    "translation_readiness_claim",
    "constructed_surface_readiness_claim",
    "publication_readiness_claim",
    "pilot_readiness_claim",
]


def now_utc() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="microseconds")


def sha256_path(path: pathlib.Path) -> str:
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
    item = {"path": artifact_path(path), "sha256": sha256_path(path), "bytes": path.stat().st_size}
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
                updated["sha256"] = sha256_path(path)
                updated["bytes"] = path.stat().st_size
                refreshed.append(updated)
            else:
                refreshed.append(item)
        manifest["artifacts"][group] = refreshed


def build_document() -> dict:
    source_exists = SOURCE_NOTE.exists() and SOURCE_NOTE.is_file()
    source_bytes = SOURCE_NOTE.stat().st_size if source_exists else 0
    source_sha256 = sha256_path(SOURCE_NOTE) if source_exists else ""
    source_mtime_utc = (
        datetime.datetime.fromtimestamp(SOURCE_NOTE.stat().st_mtime, datetime.timezone.utc).isoformat(timespec="seconds")
        if source_exists
        else ""
    )
    return {
        "artifact": "constructed_language_pilot_coordination_note_intake",
        "status": STATUS,
        "generated_date": "2026-06-30",
        "generated_utc": now_utc(),
        "source_thread_id": SOURCE_THREAD_ID,
        "source_note_path": str(SOURCE_NOTE),
        "source_note_exists": source_exists,
        "source_note_bytes": source_bytes,
        "source_note_sha256": source_sha256,
        "source_note_mtime_utc": source_mtime_utc,
        "intake_policy": {
            "branch_role": "canonical_edition_lane_receiving_methodology_support_pointer",
            "source_note_body_copied": False,
            "source_note_excerpt_copied": False,
            "source_language_terms_copied": False,
            "credentials_or_tokens_copied": False,
            "no_network_actions_performed": True,
            "pointer_only": True,
        },
        "packet_shape_categories": PACKET_SHAPE_CATEGORIES,
        "non_claim_boundaries": {boundary: False for boundary in NON_CLAIM_BOUNDARIES},
        "handoff_use": [
            "methodology_support_cohort_pointer",
            "constructed_and_semi_constructed_language_research_lane_input",
            "packet_shape_reuse_candidate_after_source_license_and_reviewer_returns",
        ],
        "totals": {
            "packet_shape_categories": len(PACKET_SHAPE_CATEGORIES),
            "non_claim_boundaries": len(NON_CLAIM_BOUNDARIES),
            "source_note_body_copied": 0,
            "source_note_excerpt_copied": 0,
            "network_actions": 0,
        },
    }


def write_markdown(document: dict) -> None:
    lines = [
        "# Constructed-language pilot coordination note intake - 2026-06-30",
        "",
        "Status: pointer-only methodology/support-cohort intake. This does not claim canonical readiness, translation readiness, constructed-surface readiness, publication readiness, or pilot readiness.",
        "",
        "## Source Pointer",
        "",
        f"- Source thread: `{document['source_thread_id']}`",
        f"- Source note path: `{document['source_note_path']}`",
        f"- Source note exists: {str(document['source_note_exists']).lower()}",
        f"- Source note bytes: {document['source_note_bytes']}",
        f"- Source note SHA-256: `{document['source_note_sha256']}`",
        "",
        "## Packet Shape Categories",
        "",
    ]
    for category in document["packet_shape_categories"]:
        lines.append(f"- `{category}`")
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- The source note body is not copied into this branch payload.",
            "- The intake is methodology/support material only.",
            "- All pilot, publication, translation, and constructed-surface gates remain closed.",
            "- Source licensing, reviewer authority, and return ingestion remain required before any surface work.",
            "- No network action, upload, or remote branch update is performed by this intake.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def update_status_index(document: dict, manifest: dict) -> None:
    text = STATUS_INDEX.read_text(encoding="utf-8")
    text = re.sub(
        r"- JSON artifacts indexed: \d+ plus this status manifest",
        f"- JSON artifacts indexed: {len(manifest['artifacts']['json'])} plus this status manifest",
        text,
    )
    text = re.sub(
        r"- Markdown artifacts indexed: \d+ plus this status index",
        f"- Markdown artifacts indexed: {len(manifest['artifacts']['markdown'])} plus this status index",
        text,
    )
    text = re.sub(
        r"- Reproducible scripts indexed: \d+",
        f"- Reproducible scripts indexed: {len(manifest['artifacts']['scripts'])}",
        text,
    )
    line = (
        "- Constructed-language pilot coordination note intake: "
        f"{document['totals']['packet_shape_categories']} packet-shape categories / "
        f"{document['totals']['non_claim_boundaries']} non-claim boundaries / pointer only / 0 network actions"
    )
    if re.search(r"^- Constructed-language pilot coordination note intake: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Constructed-language pilot coordination note intake: .*", line, text, flags=re.MULTILINE)
    else:
        rows = text.splitlines()
        inserted = False
        for offset, row in enumerate(rows):
            if row.startswith("- Support cohort authority notes:"):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                inserted = True
                break
        if not inserted:
            text = text.rstrip() + "\n" + line + "\n"
    if "constructed-language-pilot-coordination-note-intake" not in text:
        text = text.replace(
            "support-cohort-authority-note/render-script-preflight",
            "support-cohort-authority-note/constructed-language-pilot-coordination-note-intake/render-script-preflight",
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
    totals = document["totals"]
    manifest["constructed_language_pilot_coordination_note_intake"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "source_thread_id": document["source_thread_id"],
        "source_note_exists": document["source_note_exists"],
        "source_note_bytes": document["source_note_bytes"],
        "source_note_sha256": document["source_note_sha256"],
        "packet_shape_categories": totals["packet_shape_categories"],
        "non_claim_boundaries": totals["non_claim_boundaries"],
        "source_note_body_copied": False,
        "source_note_excerpt_copied": False,
        "source_language_terms_copied": False,
        "credentials_or_tokens_copied": False,
        "no_network_actions_performed": True,
        "canonical_readiness_claim": False,
        "translation_readiness_claim": False,
        "constructed_surface_readiness_claim": False,
        "publication_readiness_claim": False,
        "pilot_readiness_claim": False,
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
    document = build_document()
    write_json(OUT_JSON, document)
    write_markdown(document)
    update_manifest(document)
    print(
        json.dumps(
            {
                "constructed_language_pilot_coordination_note_intake_json": str(OUT_JSON),
                "source_note_exists": document["source_note_exists"],
                "source_note_bytes": document["source_note_bytes"],
                "source_note_sha256": document["source_note_sha256"],
                "packet_shape_categories": document["totals"]["packet_shape_categories"],
                "non_claim_boundaries": document["totals"]["non_claim_boundaries"],
                "no_network_actions_performed": document["intake_policy"]["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
