#!/usr/bin/env python3
"""Publish the complete Spanish SGA 5 checkpoint on the existing SGA concept.

This script cannot mint a concept.  It requires the exact live SGA predecessor,
refuses an untracked draft, preserves every inherited file, uploads the complete
408-member Spanish transport plus directly readable reader/source/control
surfaces, and requires an explicit tracked draft id for publication.  The final
step anonymously downloads and hashes every public file and replays every member
of the Spanish transport ZIP.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import os
import time
import zipfile
from pathlib import Path
from urllib.parse import quote

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
MODERN = {"Accept": "application/vnd.inveniordm.v1+json"}
PREDECESSOR_ID = 21782424
PREDECESSOR_DOI = "10.5281/zenodo.21782424"
CONCEPT_ID = "20410947"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PREDECESSOR_VERSION_INDEX = 256
PREDECESSOR_FILES = 57
PREDECESSOR_BYTES = 220_992_794
DEFAULT_PREVIEW = "00_SGA_1-7II_English_Global_Reader.pdf"

REPO_ROOT = Path(__file__).resolve().parents[1]
INTERLANGUAGE_ROOT = Path(
    os.environ.get(
        "INTERLANGUAGE_ROOT",
        str(Path.home() / "Documents" / "interlanguage"),
    )
)
PREDECESSOR_RECEIPT = (
    REPO_ROOT
    / "manifests"
    / "published-zenodo"
    / "20260804_sga_global_reference_r3_record_21782424_public_readback.json"
)
AUTHORIZATION_CONTROL = (
    REPO_ROOT
    / "manifests"
    / "source-intake"
    / "20260804_sga5_spanish_public_release_authorization_and_hold_supersession.md"
)
CUSTODY_ROOT = (
    INTERLANGUAGE_ROOT
    / "03_projects"
    / "language_management"
    / "romance"
    / "90_logs"
    / "private_archive_custody"
    / "SGA5_ES_COMPLETE_RIGHTS_HOLD_20260804_r1"
)
COMPLETE_ZIP_PATH = CUSTODY_ROOT / "SGA5_ES_376U_326P_91A644AB_2B69F774.zip"
CUSTODY_MANIFEST_PATH = CUSTODY_ROOT / "ZIP_MEMBER_MANIFEST.csv"
COMPLETE_ZIP_NAME = COMPLETE_ZIP_PATH.name
EXPECTED_ZIP_BYTES = 2_821_750
EXPECTED_ZIP_SHA256 = (
    "202EBF8A05F1C6A1F96D7B6235A6FD67185CB64A8B53C4F86ADD3EDBC068EB8C"
)
EXPECTED_ZIP_MEMBERS = 408
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 5_804_945
EXPECTED_MEMBER_TREE_SHA256 = (
    "D3EE03791196BC1F9E70D4D5B005370A3F86FCAA752A67860FFCC70E062BB640"
)

PUBLICATION_DATE = "2026-08-04"
VERSION = "2026-08-04 global reference R3 with complete Spanish SGA 5"
TITLE = (
    "SGA 1-7: English Readers, French Texts, Spanish SGA 5, "
    "TeX Archives, and SGA7 Source Transcriptions"
)
DESCRIPTION = """<h2>SGA 1-7 mathematical reader and source archive</h2>
<p>This record preserves the current SGA reader corpus, editable sources, build closures, provenance, and cross-volume reference controls. It includes the English reader corpus for SGA 1 through SGA 7 II (including SGA 4 1/2), retained French source surfaces, and a complete Spanish working translation of the contents published in SGA 5 / Lecture Notes in Mathematics 589.</p>
<p><strong>Start here:</strong> the first file is the complete English SGA 1-7 II reader/source ZIP. The default preview is <code>00_SGA_1-7II_English_Global_Reader.pdf</code>, the 4,179-page cumulative English reader. Clean standalone English readers and their TeX/source closures follow.</p>
<p><strong>Spanish SGA 5:</strong> <code>SGA5_ES.pdf</code> is the directly readable 326-page Spanish reader, <code>sga5_es.tex</code> is its editable master, and <code>SGA5_ES_376U_326P_91A644AB_2B69F774.zip</code> preserves all 408 source, unit, evidence, script, manifest, and control files. The checkpoint covers all contents actually published in SGA 5: front matter; Exposes I, III, III B, V, VI, VII, VIII, X, XII, and XIV=XV; and both terminal indexes. Its exact gate records 376 source units and 401 terminology decisions.</p>
<p>The reader PDFs contain mathematics and source-era apparatus, not archive workflow notes or AI explanatory footnotes. These are source-reconciled working translations and preservation artifacts, not critical editions, native-language certifications, mathematical peer review, or blanket license grants. Rights in underlying works remain with their rightsholders; public preservation does not claim a transfer of those rights.</p>
<p>Exact human-readable logbooks, continuation, decisions, reversals, claim boundaries, manifests, and validation surfaces are kept directly accessible or inside the complete transports. Earlier noncanonical Spanish SGA 5 generations remain immutable version history and are superseded by the complete checkpoint here.</p>"""
ADDITIONAL_NOTE = """<p><strong>Complete Spanish SGA 5 checkpoint.</strong> The public transport is 2,821,750 bytes, contains 408 files / 5,804,945 uncompressed bytes, and has SHA-256 <code>202EBF8A05F1C6A1F96D7B6235A6FD67185CB64A8B53C4F86ADD3EDBC068EB8C</code>. Completion gate: PASS 9/9. PDF: 326 pages, SHA-256 <code>2B69F774EF0F3E56262C45E36DE1807DB3428563678AB1132322521C716E32CC</code>. The initial pre-emptive archive release hold is retained as adverse history and explicitly superseded by the public-release authorization control. Rights caveats describe claim boundaries and are not used as release holds.</p>"""

TEMP_ROOT = (
    Path(os.environ.get("LOCALAPPDATA", os.environ.get("TEMP", ".")))
    / "Temp"
    / "sga5_spanish_complete_20260804"
)
STATE_PATH = TEMP_ROOT / "draft_state.json"

ARCHIVE_MEMBER_PUBLIC_NAMES = {
    "SGA5_ES.pdf": "SGA5_ES.pdf",
    "sga5_es.tex": "sga5_es.tex",
    "README.md": "SGA5_ES_README.md",
    "PUBLIC_SOURCE_AND_RIGHTS.md": "SGA5_ES_PUBLIC_SOURCE_AND_RIGHTS.md",
    "CONTINUATION_CURSOR.md": "SGA5_ES_CONTINUATION_CURSOR.md",
    "ROMANCE_CLAIM_BOUNDARY.md": "SGA5_ES_ROMANCE_CLAIM_BOUNDARY.md",
    "SUPERSESSION.md": "SGA5_ES_SUPERSESSION.md",
    "PUBLIC_RELEASE_CORE_STATE.json": "SGA5_ES_PUBLIC_RELEASE_CORE_STATE.json",
    "FINAL_GATE_PUBLIC.json": "SGA5_ES_FINAL_GATE_PUBLIC.json",
    "PUBLIC_RELEASE_MANIFEST.csv": "SGA5_ES_PUBLIC_RELEASE_MANIFEST.csv",
    "SHA256SUMS.txt": "SGA5_ES_SHA256SUMS.txt",
}
CUSTODY_PUBLIC_FILES = {
    "PRIVATE_CUSTODY_RECEIPT.md": (
        "SGA5_ES_SUPERSEDED_INITIAL_CUSTODY_RIGHTS_HOLD_RECEIPT.md"
    ),
    "PRIVATE_CUSTODY_VALIDATION.json": (
        "SGA5_ES_SUPERSEDED_INITIAL_CUSTODY_RIGHTS_HOLD_VALIDATION.json"
    ),
    "ZIP_MEMBER_MANIFEST.csv": "SGA5_ES_ZIP_MEMBER_MANIFEST.csv",
    "BROAD_PATH_ALERT_CLASSIFICATION.csv": (
        "SGA5_ES_PRIVACY_ALERT_CLASSIFICATION.csv"
    ),
}
AUTHORIZATION_PUBLIC_NAME = (
    "SGA5_ES_PUBLIC_RELEASE_AUTHORIZATION_AND_HOLD_SUPERSESSION.md"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def md5(path: Path) -> str:
    digest = hashlib.md5(usedforsecurity=False)
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().lower()


def normalized_md5(value: str) -> str:
    return str(value).lower().removeprefix("md5:")


def auth(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def auth_modern(token: str) -> dict[str, str]:
    return {**auth(token), **MODERN}


def save_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    temporary.replace(path)


def load_state() -> dict | None:
    if not STATE_PATH.is_file():
        return None
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def modern_entries(record: dict) -> dict[str, dict]:
    return record.get("files", {}).get("entries", {})


def legacy_entries(record: dict) -> dict[str, dict]:
    return {row["filename"]: row for row in record.get("files", [])}


def modern_identity(row: dict) -> tuple[int, str]:
    return int(row["size"]), normalized_md5(row["checksum"])


def legacy_identity(row: dict) -> tuple[int, str]:
    return int(row["filesize"]), normalized_md5(row["checksum"])


def member_tree_sha(rows: list[dict]) -> str:
    digest = hashlib.sha256()
    for row in sorted(rows, key=lambda item: item["relative_path"]):
        digest.update(
            (
                f"{row['relative_path']}\t{int(row['bytes'])}\t"
                f"{row['sha256'].upper()}\n"
            ).encode("utf-8")
        )
    return digest.hexdigest().upper()


def replay_zip(path: Path) -> tuple[list[dict], dict]:
    with CUSTODY_MANIFEST_PATH.open(
        "r", encoding="utf-8-sig", newline=""
    ) as handle:
        expected_rows = list(csv.DictReader(handle))
    expected = {
        row["relative_path"].replace("\\", "/"): (
            int(row["bytes"]),
            row["sha256"].upper(),
        )
        for row in expected_rows
    }
    observed_rows: list[dict] = []
    errors: list[str] = []
    with zipfile.ZipFile(path) as archive:
        bad = archive.testzip()
        if bad is not None:
            errors.append(f"crc:{bad}")
        infos = [item for item in archive.infolist() if not item.is_dir()]
        names = [item.filename.replace("\\", "/") for item in infos]
        if len(names) != EXPECTED_ZIP_MEMBERS or set(names) != set(expected):
            errors.append("member_boundary")
        for info in infos:
            name = info.filename.replace("\\", "/")
            if name not in expected:
                continue
            digest = hashlib.sha256()
            with archive.open(info) as handle:
                for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
                    digest.update(block)
            identity = (info.file_size, digest.hexdigest().upper())
            match = identity == expected[name]
            if not match:
                errors.append(name)
            observed_rows.append(
                {
                    "relative_path": name,
                    "bytes": identity[0],
                    "sha256": identity[1],
                    "match": match,
                }
            )
    tree = member_tree_sha(observed_rows)
    if tree != EXPECTED_MEMBER_TREE_SHA256:
        errors.append("member_tree_sha256")
    total = sum(int(row["bytes"]) for row in observed_rows)
    if total != EXPECTED_ZIP_UNCOMPRESSED_BYTES:
        errors.append("uncompressed_bytes")
    return observed_rows, {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "members": len(observed_rows),
        "matches": sum(1 for row in observed_rows if row["match"]),
        "mismatches": sum(1 for row in observed_rows if not row["match"]),
        "uncompressed_bytes": total,
        "member_tree_sha256": tree,
    }


def extract_direct_members(rows: list[dict]) -> dict[str, Path]:
    expected = {row["relative_path"]: row for row in rows}
    direct_root = TEMP_ROOT / "exact_direct_members"
    direct_root.mkdir(parents=True, exist_ok=True)
    result: dict[str, Path] = {}
    with zipfile.ZipFile(COMPLETE_ZIP_PATH) as archive:
        for member, public_name in ARCHIVE_MEMBER_PUBLIC_NAMES.items():
            row = expected.get(member)
            if row is None:
                raise RuntimeError(f"Required Spanish direct member missing: {member}")
            destination = direct_root / public_name
            data = archive.read(member)
            if (
                len(data) != int(row["bytes"])
                or hashlib.sha256(data).hexdigest().upper() != row["sha256"]
            ):
                raise RuntimeError(f"Extracted Spanish member changed: {member}")
            if not destination.is_file() or destination.read_bytes() != data:
                destination.write_bytes(data)
            result[public_name] = destination
    return result


def local_new_surface() -> tuple[dict[str, dict], dict]:
    if (
        COMPLETE_ZIP_PATH.stat().st_size != EXPECTED_ZIP_BYTES
        or sha256(COMPLETE_ZIP_PATH) != EXPECTED_ZIP_SHA256
    ):
        raise RuntimeError("Spanish complete ZIP identity changed")
    member_rows, zip_replay = replay_zip(COMPLETE_ZIP_PATH)
    if zip_replay["status"] != "PASS":
        raise RuntimeError(f"Spanish complete ZIP replay failed: {zip_replay}")
    paths = extract_direct_members(member_rows)
    paths[COMPLETE_ZIP_NAME] = COMPLETE_ZIP_PATH
    paths[AUTHORIZATION_PUBLIC_NAME] = AUTHORIZATION_CONTROL
    for local_name, public_name in CUSTODY_PUBLIC_FILES.items():
        paths[public_name] = CUSTODY_ROOT / local_name
    for path in paths.values():
        if not path.is_file():
            raise RuntimeError(f"Required Spanish public file is missing: {path}")
    surface = {
        name: {
            "path": str(path),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
            "md5": md5(path),
        }
        for name, path in paths.items()
    }
    expected_core = {
        COMPLETE_ZIP_NAME: (
            EXPECTED_ZIP_BYTES,
            EXPECTED_ZIP_SHA256,
        ),
        "SGA5_ES.pdf": (
            2_196_982,
            "2B69F774EF0F3E56262C45E36DE1807DB3428563678AB1132322521C716E32CC",
        ),
        "sga5_es.tex": (
            26_139,
            "49A77434448F402C40EB935F982C4EDE7EF5B611677D2BD254D6E0520D460E7F",
        ),
        "SGA5_ES_PUBLIC_RELEASE_MANIFEST.csv": (
            48_146,
            "B4B2D346CD29662FB2AAAEC2DA5CC4CBB9F561856E3B2F0EC9EC2ACCBEB8CBF6",
        ),
        "SGA5_ES_FINAL_GATE_PUBLIC.json": (
            4_373,
            "35E76152CA87C41DCF7471EBD853AEB823D89B7A2BC6BFD7F75003A4903E17CF",
        ),
        "SGA5_ES_SHA256SUMS.txt": (
            44_675,
            "C31B729B6EB237BFDB76A8CF85811B366E23762B6AF838944B58C8B5FBB5710B",
        ),
    }
    for name, expected in expected_core.items():
        observed = (surface[name]["bytes"], surface[name]["sha256"])
        if observed != expected:
            raise RuntimeError(
                f"Spanish public core identity changed for {name}: {observed}"
            )
    return surface, zip_replay


def predecessor_receipt() -> dict:
    receipt = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8"))
    if (
        receipt.get("status")
        != "PASS_PUBLISHED_SAME_CONCEPT_AND_ANONYMOUS_RAW_READBACK"
        or int(receipt.get("record_id", 0)) != PREDECESSOR_ID
        or receipt.get("concept_doi") != CONCEPT_DOI
        or int(receipt.get("direct_files", 0)) != PREDECESSOR_FILES
        or int(receipt.get("direct_bytes", 0)) != PREDECESSOR_BYTES
        or receipt.get("default_preview") != DEFAULT_PREVIEW
        or int(receipt.get("direct_readback_matches", 0)) != PREDECESSOR_FILES
        or int(receipt.get("direct_readback_mismatches", -1)) != 0
    ):
        raise RuntimeError("SGA predecessor readback receipt boundary changed")
    return receipt


def fetch_live(session) -> dict:
    live = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_ID}/versions/latest",
            headers=MODERN,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    entries = modern_entries(live)
    observed = (
        int(live["id"]),
        live.get("pids", {}).get("doi", {}).get("identifier"),
        str(live.get("parent", {}).get("id")),
        live.get("parent", {}).get("pids", {}).get("doi", {}).get("identifier"),
        int(live.get("versions", {}).get("index", 0)),
        live.get("versions", {}).get("is_latest"),
        live.get("status"),
        len(entries),
        sum(int(row["size"]) for row in entries.values()),
        live.get("files", {}).get("default_preview"),
    )
    expected = (
        PREDECESSOR_ID,
        PREDECESSOR_DOI,
        CONCEPT_ID,
        CONCEPT_DOI,
        PREDECESSOR_VERSION_INDEX,
        True,
        "published",
        PREDECESSOR_FILES,
        PREDECESSOR_BYTES,
        DEFAULT_PREVIEW,
    )
    if observed != expected:
        raise RuntimeError(f"Live SGA predecessor boundary changed: {observed!r}")
    receipt = predecessor_receipt()
    receipt_rows = {row["filename"]: row for row in receipt["direct_readback"]}
    if set(receipt_rows) != set(entries):
        raise RuntimeError("Live SGA file set differs from its raw-readback receipt")
    for name, row in receipt_rows.items():
        if int(row["bytes"]) != int(entries[name]["size"]):
            raise RuntimeError(f"Live SGA inherited byte count changed: {name}")
    return live


def verify_active_draft(session, token: str) -> dict | None:
    state = load_state()
    probe = session.get(
        f"{API}/records/{PREDECESSOR_ID}/draft",
        headers=auth_modern(token),
        timeout=(30, 180),
    )
    if state is None:
        if probe.status_code == 200:
            raise RuntimeError("Untracked SGA successor draft exists; refusing mutation")
        base.check(probe, {404})
        return None
    if state.get("published"):
        if probe.status_code not in {404, 410}:
            raise RuntimeError("Published Spanish SGA5 state conflicts with a draft")
        return state
    if probe.status_code == 200 and int(probe.json()["id"]) != int(state["draft_id"]):
        raise RuntimeError("Predecessor-scoped SGA draft identity changed")
    if probe.status_code != 200:
        base.check(probe, {404})
    tracked = base.check(
        session.get(
            f"{API}/records/{int(state['draft_id'])}/draft",
            headers=auth_modern(token),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if (
        int(tracked["id"]) != int(state["draft_id"])
        or str(tracked.get("parent", {}).get("id")) != CONCEPT_ID
        or tracked.get("is_published") is not False
    ):
        raise RuntimeError("Tracked Spanish SGA5 draft boundary changed")
    return state


def create_or_resume_draft(session, token: str, live: dict) -> tuple[int, bool]:
    state = verify_active_draft(session, token)
    if state is not None:
        if state.get("published"):
            raise RuntimeError("Spanish SGA5 successor is already published")
        return int(state["draft_id"]), False
    predecessor = base.check(
        session.get(
            f"{API}/deposit/depositions/{PREDECESSOR_ID}",
            headers=auth(token),
            timeout=(30, 300),
        ),
        {200},
    ).json()
    if (
        predecessor.get("state") != "done"
        or not predecessor.get("submitted")
        or not predecessor.get("links", {}).get("newversion")
        or str(predecessor.get("conceptrecid")) != CONCEPT_ID
    ):
        raise RuntimeError("SGA predecessor is not a safe same-concept base")
    created = base.check(
        session.post(
            predecessor["links"]["newversion"],
            headers=auth(token),
            timeout=(30, 600),
        ),
        {201},
    ).json()
    deposition = base.check(
        session.get(
            created["links"]["latest_draft"],
            headers=auth(token),
            timeout=(30, 300),
        ),
        {200},
    ).json()
    draft_id = int(deposition["id"])
    if set(legacy_entries(deposition)) != set(modern_entries(live)):
        raise RuntimeError("SGA successor did not inherit every predecessor file")
    modern = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft",
            headers=auth_modern(token),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if (
        str(modern.get("parent", {}).get("id")) != CONCEPT_ID
        or modern.get("versions", {}).get("index") != PREDECESSOR_VERSION_INDEX + 1
        or modern.get("versions", {}).get("is_latest_draft") is not True
    ):
        raise RuntimeError("Created Spanish SGA5 draft left the required lineage")
    save_json(
        STATE_PATH,
        {
            "status": "OPEN_TRACKED_DRAFT",
            "predecessor_record": PREDECESSOR_ID,
            "concept_id": CONCEPT_ID,
            "concept_doi": CONCEPT_DOI,
            "draft_id": draft_id,
            "published": False,
            "created_at_epoch": int(time.time()),
        },
    )
    return draft_id, True


def desired_order(inherited_order: list[str], new_names: set[str]) -> list[str]:
    order = list(inherited_order)
    if set(order) != set(predecessor_receipt()["configured_file_order"]):
        raise RuntimeError("Inherited SGA order boundary changed")

    def insert_after(anchor: str, names: list[str]) -> None:
        index = order.index(anchor) + 1
        order[index:index] = names

    insert_after("00e_SGA5_English_Reader.pdf", ["SGA5_ES.pdf"])
    insert_after("02e_SGA5_English_Master.tex", ["sga5_es.tex"])
    insert_after(
        "10e_SGA5_English_Source_PresentationClean_R10_20260803.zip",
        [COMPLETE_ZIP_NAME],
    )
    controls = [
        AUTHORIZATION_PUBLIC_NAME,
        "SGA5_ES_README.md",
        "SGA5_ES_PUBLIC_SOURCE_AND_RIGHTS.md",
        "SGA5_ES_CONTINUATION_CURSOR.md",
        "SGA5_ES_ROMANCE_CLAIM_BOUNDARY.md",
        "SGA5_ES_SUPERSESSION.md",
        "SGA5_ES_PUBLIC_RELEASE_CORE_STATE.json",
        "SGA5_ES_FINAL_GATE_PUBLIC.json",
        "SGA5_ES_PUBLIC_RELEASE_MANIFEST.csv",
        "SGA5_ES_SHA256SUMS.txt",
        "SGA5_ES_ZIP_MEMBER_MANIFEST.csv",
        "SGA5_ES_PRIVACY_ALERT_CLASSIFICATION.csv",
        "SGA5_ES_SUPERSEDED_INITIAL_CUSTODY_RIGHTS_HOLD_RECEIPT.md",
        "SGA5_ES_SUPERSEDED_INITIAL_CUSTODY_RIGHTS_HOLD_VALIDATION.json",
    ]
    control_anchor = "PACKAGE_CONTENT_MANIFEST.csv"
    index = order.index(control_anchor)
    order[index:index] = controls
    if len(order) != len(set(order)) or set(order) != set(inherited_order) | new_names:
        raise RuntimeError("Spanish SGA5 desired order is not an exact partition")
    return order


def desired_metadata(current: dict) -> dict:
    metadata = copy.deepcopy(current)
    metadata["title"] = TITLE
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["version"] = VERSION
    metadata["description"] = DESCRIPTION
    metadata["additional_descriptions"] = [
        {"description": ADDITIONAL_NOTE, "type": {"id": "notes"}}
    ]
    existing = list(metadata.get("subjects", []))
    wanted = [
        {"subject": "Spanish mathematical translation"},
        {"subject": "SGA 5"},
        {"subject": "algebraic geometry"},
    ]
    seen = {
        json.dumps(row, ensure_ascii=True, sort_keys=True) for row in existing
    }
    for row in wanted:
        key = json.dumps(row, ensure_ascii=True, sort_keys=True)
        if key not in seen:
            existing.append(row)
            seen.add(key)
    metadata["subjects"] = existing
    return metadata


def verify_staged(
    draft: dict,
    live: dict,
    new_surface: dict[str, dict],
    order: list[str],
) -> None:
    entries = modern_entries(draft)
    inherited = modern_entries(live)
    if set(entries) != set(inherited) | set(new_surface):
        raise RuntimeError("Spanish SGA5 staged filename boundary is not exact")
    errors: list[str] = []
    for name, row in inherited.items():
        if modern_identity(entries[name]) != modern_identity(row):
            errors.append(name)
    for name, row in new_surface.items():
        if modern_identity(entries[name]) != (int(row["bytes"]), row["md5"]):
            errors.append(name)
    if errors:
        raise RuntimeError(f"Spanish SGA5 staged identity errors: {errors}")
    metadata = draft.get("metadata", {})
    notes = metadata.get("additional_descriptions", [])
    if (
        metadata.get("title") != TITLE
        or metadata.get("publication_date") != PUBLICATION_DATE
        or metadata.get("version") != VERSION
        or metadata.get("description") != DESCRIPTION
        or len(notes) != 1
        or notes[0].get("description") != ADDITIONAL_NOTE
        or draft.get("files", {}).get("default_preview") != DEFAULT_PREVIEW
    ):
        raise RuntimeError("Spanish SGA5 staged metadata/preview changed")
    observed_order = draft.get("files", {}).get("order") or []
    if observed_order not in (order, []):
        raise RuntimeError("Spanish SGA5 staged file order changed")


def upload_file(session, token: str, bucket: str, name: str, path: Path) -> None:
    print(f"UPLOAD {name} ({path.stat().st_size} bytes)", flush=True)
    with path.open("rb") as handle:
        base.check(
            session.put(
                f"{bucket.rstrip('/')}/{quote(name, safe='')}",
                headers={**auth(token), "Content-Type": "application/octet-stream"},
                data=handle,
                timeout=(30, 3600),
            ),
            {200, 201},
        )


def preflight(session, token: str) -> dict:
    new_surface, zip_replay = local_new_surface()
    live = fetch_live(session)
    state = verify_active_draft(session, token)
    order = desired_order(
        predecessor_receipt()["configured_file_order"], set(new_surface)
    )
    return {
        "status": "PASS_READY_FOR_ONE_SAME_CONCEPT_SUCCESSOR",
        "concept_id": CONCEPT_ID,
        "concept_doi": CONCEPT_DOI,
        "predecessor_record_id": PREDECESSOR_ID,
        "predecessor_version_doi": PREDECESSOR_DOI,
        "predecessor_version_index": live["versions"]["index"],
        "predecessor_files_preserved": len(modern_entries(live)),
        "predecessor_bytes_preserved": sum(
            int(row["size"]) for row in modern_entries(live).values()
        ),
        "active_draft": state is not None and not state.get("published", False),
        "tracked_draft_id": None if state is None else state.get("draft_id"),
        "new_direct_files": len(new_surface),
        "new_direct_bytes": sum(int(row["bytes"]) for row in new_surface.values()),
        "resulting_files": len(order),
        "spanish_zip_replay": zip_replay,
        "default_preview_retained": DEFAULT_PREVIEW,
        "duplicate_concept_created": False,
        "release_hold": False,
    }


def stage(session, token: str) -> dict:
    new_surface, zip_replay = local_new_surface()
    live = fetch_live(session)
    inherited = modern_entries(live)
    order = desired_order(
        predecessor_receipt()["configured_file_order"], set(new_surface)
    )
    draft_id, created = create_or_resume_draft(session, token, live)
    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth(token),
            timeout=(30, 300),
        ),
        {200},
    ).json()
    remote = legacy_entries(deposition)
    allowed = set(inherited) | set(new_surface)
    if not set(remote).issubset(allowed) or not set(inherited).issubset(remote):
        raise RuntimeError("Tracked draft contains an unexpected file boundary")
    for name, row in inherited.items():
        if legacy_identity(remote[name]) != modern_identity(row):
            raise RuntimeError(f"Inherited SGA file changed in draft: {name}")
    bucket = deposition["links"]["bucket"]
    uploaded: list[str] = []
    for name in order:
        if name in remote:
            continue
        row = new_surface[name]
        upload_file(session, token, bucket, name, Path(row["path"]))
        uploaded.append(name)
    draft = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft",
            headers=auth_modern(token),
            timeout=(30, 600),
        ),
        {200},
    ).json()
    if set(modern_entries(draft)) != allowed:
        raise RuntimeError("Spanish SGA5 draft file set incomplete after upload")
    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": DEFAULT_PREVIEW,
            "order": order,
        },
        "metadata": desired_metadata(draft["metadata"]),
        "custom_fields": draft.get("custom_fields", {}),
    }
    if draft.get("pids"):
        payload["pids"] = draft["pids"]
    patched = base.check(
        session.put(
            f"{API}/records/{draft_id}/draft",
            headers={**auth_modern(token), "Content-Type": "application/json"},
            json=payload,
            timeout=(30, 600),
        ),
        {200},
    ).json()
    verify_staged(patched, live, new_surface, order)
    state = load_state()
    if state is None or int(state["draft_id"]) != draft_id:
        raise RuntimeError("Tracked Spanish SGA5 state disappeared")
    state.update(
        {
            "status": "STAGED_EXACT_READY_FOR_EXPLICIT_PUBLISH",
            "staged": True,
            "staged_files": len(order),
            "new_files": len(new_surface),
            "default_preview": DEFAULT_PREVIEW,
            "staged_at_epoch": int(time.time()),
        }
    )
    save_json(STATE_PATH, state)
    return {
        "status": "STAGED_EXACT_READY_FOR_EXPLICIT_PUBLISH",
        "draft_id": draft_id,
        "draft_url": patched.get("links", {}).get("self_html"),
        "concept_id": CONCEPT_ID,
        "concept_doi": CONCEPT_DOI,
        "predecessor_record_id": PREDECESSOR_ID,
        "created_new_same_concept_draft": created,
        "duplicate_concept_created": False,
        "inherited_files_preserved": len(inherited),
        "uploaded_now": uploaded,
        "files": len(order),
        "bytes": sum(int(row["size"]) for row in inherited.values())
        + sum(int(row["bytes"]) for row in new_surface.values()),
        "default_preview": DEFAULT_PREVIEW,
        "file_order": order,
        "spanish_zip_replay": zip_replay,
        "release_hold": False,
    }


def stream_identity(session, url: str, destination: Path | None = None) -> tuple[int, str]:
    digest = hashlib.sha256()
    total = 0
    response = base.check(session.get(url, stream=True, timeout=(30, 3600)), {200})
    try:
        handle = None if destination is None else destination.open("wb")
        try:
            for block in response.iter_content(4 * 1024 * 1024):
                if not block:
                    continue
                if handle is not None:
                    handle.write(block)
                digest.update(block)
                total += len(block)
        finally:
            if handle is not None:
                handle.close()
    finally:
        response.close()
    return total, digest.hexdigest().upper()


def publish_and_readback(
    session,
    token: str,
    confirm_draft_id: str,
    receipt_dir: Path,
) -> dict:
    new_surface, local_zip_replay = local_new_surface()
    live = fetch_live(session)
    order = desired_order(
        predecessor_receipt()["configured_file_order"], set(new_surface)
    )
    state = verify_active_draft(session, token)
    if state is None or state.get("published") or not state.get("staged"):
        raise RuntimeError("No exact staged Spanish SGA5 draft is tracked")
    draft_id = int(state["draft_id"])
    if confirm_draft_id != str(draft_id):
        raise RuntimeError(f"Publishing requires --confirm-publish {draft_id}")
    draft = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft",
            headers=auth_modern(token),
            timeout=(30, 600),
        ),
        {200},
    ).json()
    verify_staged(draft, live, new_surface, order)
    if (
        str(draft.get("parent", {}).get("id")) != CONCEPT_ID
        or draft.get("versions", {}).get("index") != PREDECESSOR_VERSION_INDEX + 1
    ):
        raise RuntimeError("Spanish SGA5 staged lineage changed")
    published = base.check(
        session.post(
            draft["links"]["publish"],
            headers=auth_modern(token),
            timeout=(30, 1200),
        ),
        {200, 202},
    )
    try:
        record_id = int(published.json().get("id", draft_id))
    except Exception:
        record_id = draft_id
    if record_id != draft_id:
        raise RuntimeError("Spanish SGA5 publication returned another record id")
    state.update(
        {
            "status": "PUBLISHED_AWAITING_ANONYMOUS_READBACK",
            "published": True,
            "record_id": record_id,
            "published_at_epoch": int(time.time()),
        }
    )
    save_json(STATE_PATH, state)

    anonymous = base.make_session()
    record = None
    for _ in range(60):
        probe = anonymous.get(
            f"{API}/records/{record_id}", headers=MODERN, timeout=(30, 300)
        )
        if probe.status_code == 200 and probe.json().get("status") == "published":
            record = probe.json()
            break
        time.sleep(2)
    if record is None:
        raise RuntimeError("Spanish SGA5 successor did not become public")
    if (
        str(record.get("parent", {}).get("id")) != CONCEPT_ID
        or record.get("parent", {}).get("pids", {}).get("doi", {}).get("identifier")
        != CONCEPT_DOI
        or record.get("versions", {}).get("index") != PREDECESSOR_VERSION_INDEX + 1
        or record.get("versions", {}).get("is_latest") is not True
    ):
        raise RuntimeError("Published Spanish SGA5 lineage identity changed")
    verify_staged(record, live, new_surface, order)

    prior = predecessor_receipt()
    expected = {
        row["filename"]: (int(row["bytes"]), row["sha256"].upper())
        for row in prior["direct_readback"]
    }
    expected.update(
        {
            name: (int(row["bytes"]), row["sha256"])
            for name, row in new_surface.items()
        }
    )
    entries = modern_entries(record)
    download_path = TEMP_ROOT / f"record_{record_id}_{COMPLETE_ZIP_NAME}"
    readback_rows: list[dict] = []
    errors: list[str] = []
    for index, name in enumerate(order, start=1):
        print(f"READBACK {index}/{len(order)} {name}", flush=True)
        destination = download_path if name == COMPLETE_ZIP_NAME else None
        observed = stream_identity(
            anonymous, entries[name]["links"]["content"], destination
        )
        match = observed == expected[name]
        if not match:
            errors.append(name)
        readback_rows.append(
            {
                "filename": name,
                "bytes": observed[0],
                "sha256": observed[1],
                "match": match,
                "content_url": entries[name]["links"]["content"],
                "disposition": (
                    "new_spanish_checkpoint" if name in new_surface else "retained_predecessor"
                ),
            }
        )
    if errors:
        raise RuntimeError(f"Spanish SGA5 public readback mismatches: {errors}")
    downloaded_rows, downloaded_zip_replay = replay_zip(download_path)
    if downloaded_zip_replay["status"] != "PASS":
        raise RuntimeError("Downloaded Spanish transport member replay failed")
    download_path.unlink()
    active = session.get(
        f"{API}/records/{PREDECESSOR_ID}/draft",
        headers=auth_modern(token),
        timeout=(30, 180),
    )
    if active.status_code not in {404, 410}:
        raise RuntimeError("An SGA draft remains after Spanish publication")
    result = {
        "status": "PASS_PUBLISHED_SAME_CONCEPT_AND_ANONYMOUS_RAW_READBACK",
        "errors": [],
        "record_id": record_id,
        "record_url": record["links"]["self_html"],
        "version_doi": record["pids"]["doi"]["identifier"],
        "concept_id": CONCEPT_ID,
        "concept_doi": CONCEPT_DOI,
        "predecessor_record_id": PREDECESSOR_ID,
        "predecessor_version_doi": PREDECESSOR_DOI,
        "version_index": record["versions"]["index"],
        "title": record["metadata"]["title"],
        "publication_date": record["metadata"]["publication_date"],
        "version": record["metadata"]["version"],
        "default_preview": record["files"]["default_preview"],
        "configured_file_order": order,
        "api_file_order": record["files"].get("order") or [],
        "direct_files": len(readback_rows),
        "direct_bytes": sum(row["bytes"] for row in readback_rows),
        "retained_predecessor_files": PREDECESSOR_FILES,
        "new_spanish_direct_files": len(new_surface),
        "direct_readback_matches": sum(1 for row in readback_rows if row["match"]),
        "direct_readback_mismatches": 0,
        "complete_spanish_zip": {
            "filename": COMPLETE_ZIP_NAME,
            "bytes": EXPECTED_ZIP_BYTES,
            "sha256": EXPECTED_ZIP_SHA256,
            "members": EXPECTED_ZIP_MEMBERS,
            "uncompressed_bytes": EXPECTED_ZIP_UNCOMPRESSED_BYTES,
            "member_tree_sha256": EXPECTED_MEMBER_TREE_SHA256,
            "local_member_replay": local_zip_replay,
            "public_member_replay": downloaded_zip_replay,
        },
        "active_draft": False,
        "duplicate_concept_created": False,
        "release_hold": False,
        "direct_readback": readback_rows,
        "complete_spanish_zip_member_readback": downloaded_rows,
    }
    receipt_path = (
        receipt_dir
        / f"20260804_sga5_spanish_complete_record_{record_id}_public_readback.json"
    )
    save_json(receipt_path, result)
    result["receipt_path"] = str(receipt_path)
    result["receipt_bytes"] = receipt_path.stat().st_size
    result["receipt_sha256"] = sha256(receipt_path)
    state.update(
        {
            "status": "PASS_PUBLISHED_AND_ANONYMOUS_READBACK",
            "doi": result["version_doi"],
            "record_url": result["record_url"],
            "readback_matches": result["direct_readback_matches"],
            "zip_member_matches": downloaded_zip_replay["matches"],
            "receipt_path": str(receipt_path),
            "readback_completed_at_epoch": int(time.time()),
        }
    )
    save_json(STATE_PATH, state)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("preflight", "stage", "publish"))
    parser.add_argument("--confirm-publish")
    parser.add_argument(
        "--receipt-dir",
        type=Path,
        default=REPO_ROOT / "manifests" / "published-zenodo",
    )
    args = parser.parse_args()
    session = base.make_session()
    token = base.find_token()
    if args.action == "preflight":
        result = preflight(session, token)
    elif args.action == "stage":
        result = stage(session, token)
    else:
        if not args.confirm_publish:
            raise RuntimeError("Publishing requires --confirm-publish DRAFT_ID")
        result = publish_and_readback(
            session,
            token,
            args.confirm_publish,
            args.receipt_dir.resolve(),
        )
    summary = {
        key: value
        for key, value in result.items()
        if key
        not in {
            "direct_readback",
            "complete_spanish_zip_member_readback",
            "file_order",
            "configured_file_order",
            "api_file_order",
            "uploaded_now",
        }
    }
    print(json.dumps(summary, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
