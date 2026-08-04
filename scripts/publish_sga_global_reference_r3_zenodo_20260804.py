#!/usr/bin/env python3
"""Publish the exact SGA 1--7 II global-reference R3 successor.

The script is intentionally constrained to one existing Zenodo lineage.  It
cannot create a concept, refuses an untracked draft, stages one resumable
same-concept successor of record 21778810, and requires a second explicit
command containing the tracked draft id before the irreversible publish call.

The 152-member complete ZIP is preserved as the first public object.  The
clean cumulative reader is the default preview, followed by the nine
standalone readers, nine master TeX files, nine source closures, and current
human-readable provenance/reference controls.  Historical and machine QA
surfaces remain complete inside the ZIP, avoiding Zenodo's 100-file limit.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import os
import sys
import time
import zipfile
from pathlib import Path
from urllib.parse import quote

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
MODERN = {"Accept": "application/vnd.inveniordm.v1+json"}
PREDECESSOR_ID = 21778810
PREDECESSOR_DOI = "10.5281/zenodo.21778810"
CONCEPT_ID = "20410947"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PREDECESSOR_FILES = 34
PREDECESSOR_BYTES = 182_736_901
PREDECESSOR_PREVIEW = "00_SGA_1-7II_English_Global_Reader.pdf"

EXPECTED_ROOT_FILES = 156
EXPECTED_ROOT_BYTES = 271_898_317
EXPECTED_DIRECT_FILES = 57
EXPECTED_MANIFEST_ROWS = 154
EXPECTED_MANIFEST_BYTES = 20_146
EXPECTED_MANIFEST_SHA256 = (
    "8A62B5A6B1F35F99B254DF7D7D20B9EA395C6CD961CA7284A338406E28F2F9EE"
)
EXPECTED_MANIFEST_TREE_SHA256 = (
    "2C6969D39A35BBC4D21A53BCF0BA543C9E9540D404640689ABCD8497A958B1CD"
)
EXPECTED_MANIFEST_VALIDATION_BYTES = 526
EXPECTED_MANIFEST_VALIDATION_SHA256 = (
    "978048132933D9DF62C058DC7DC220AD10017ED8A6B5D339148208F1C1143B89"
)

COMPLETE_ZIP = (
    "00_Current_SGA1-7II_English_Readers_and_Buildable_TeX_20260804_R3.zip"
)
EXPECTED_ZIP_BYTES = 135_952_927
EXPECTED_ZIP_SHA256 = (
    "CC17EE1FEFBC890D1AFE1BD2C08F6F2ECBB9C2AC20BDD0BE828C9F57E9617218"
)
EXPECTED_ZIP_MEMBERS = 152
GLOBAL_READER = "00_SGA_1-7II_English_Global_Reader.pdf"
EXPECTED_GLOBAL_BYTES = 34_611_470
EXPECTED_GLOBAL_SHA256 = (
    "4F5FF5D1535FFBD34F3EE2CF6350AA5DF8849D5BF9E91EA4F428A3ABF6299681"
)
PAYLOAD_MANIFEST = "ZENODO_PAYLOAD_MANIFEST.csv"
PAYLOAD_VALIDATION = "ZENODO_PAYLOAD_MANIFEST_VALIDATION.json"
CONTENT_MANIFEST = "PACKAGE_CONTENT_MANIFEST.csv"
CONTENT_VALIDATION = "PACKAGE_CONTENT_VALIDATION.json"

PUBLICATION_DATE = "2026-08-04"
VERSION = "2026-08-04 SGA 1-7 II global cross-volume reference v2 R3"
TITLE = (
    "SGA 1-7: English Readers, French Texts, TeX Archives, and SGA7 "
    "Source Transcriptions"
)
DESCRIPTION = """<h2>SGA 1-7 II English reader and source archive</h2>
<p>This record preserves the current English reader corpus for SGA 1 through SGA 7 II, including SGA 4 1/2, together with discoverable master TeX files, buildable source closures, provenance controls, and the reference graph used to connect the volumes.</p>
<p><strong>Start here:</strong> the first file is the complete 152-member transport ZIP. The default preview is <code>00_SGA_1-7II_English_Global_Reader.pdf</code>, a 4,179-page cumulative reader. The nine clean standalone reader PDFs follow it, then the nine master TeX files and nine source/history closures.</p>
<p>The cumulative reader contains 39,941 named destinations and 31,325 internal named links, with no broken or misrouted links in the exact-package replay. The current cross-volume graph records 1,049 candidates as 658 applied edges and 391 explicit residuals against 241 targets. Privacy-clean logbooks, revision and continuation records, rights notes, manifests, and validation surfaces remain directly readable; the complete historical and machine-QA projection is retained inside the first ZIP.</p>
<p>The reader PDFs contain the mathematical text and source-era apparatus, without archive workflow notes, source-status pages, or AI explanatory footnotes. This is a working English translation and reference corpus, not a critical edition, a mathematical certification, or a substitute for the French authorities. No package-wide license is invented, and rights in underlying works remain with their rightsholders.</p>"""
ADDITIONAL_NOTE = """<p><strong>2026-08-04 R3 successor.</strong> This same-concept version replaces the cumulative reader with the global cross-volume reference-v2 build, advances the SGA 2 privacy-clean source closure to R11, and carries the exact current SGA 3 source ZIP. Package gates: 154/154 manifest rows, 152/152 complete-ZIP members, 4,179/4,179 reader pages, 39,941 destinations, 31,325 named links, broken links 0, Type3 fonts 0, image objects 0, privacy hits 0. Predecessor record 21778810 remains immutable version history.</p>"""

STANDALONE_READERS = (
    "00a_SGA1_English_Reader.pdf",
    "00b_SGA2_English_Reader.pdf",
    "00c_SGA3_English_Reader.pdf",
    "00d_SGA4_English_Reader.pdf",
    "00d5_SGA4half_English_Reader.pdf",
    "00e_SGA5_English_Reader.pdf",
    "00f_SGA6_English_Reader.pdf",
    "00i_SGA7I_English_Reader.pdf",
    "00j_SGA7II_English_Reader.pdf",
)
MASTER_TEX = (
    "02a_SGA1_English_Master.tex",
    "02b_SGA2_English_Master.tex",
    "02c_SGA3_English_Master.tex",
    "02d_SGA4_English_Master.tex",
    "02d5_SGA4half_English_Master.tex",
    "02e_SGA5_English_Master.tex",
    "02f_SGA6_English_Master.tex",
    "02i_SGA7I_English_Master.tex",
    "02j_SGA7II_English_Master.tex",
)
SOURCE_ZIPS = (
    "10a_SGA1_English_Source_PresentationClean_R3_20260803.zip",
    "10b_SGA2_English_Source_and_History_R11_PrivacyClean_20260804.zip",
    "10c_SGA3_English_Reader_and_Buildable_TeX_R29_20260730.zip",
    "10d_SGA4_English_Proper_ReaderClean_R8_Source_20260803.zip",
    "10d5_SGA4half_English_Source_CleanFont_R2_20260803.zip",
    "10e_SGA5_English_Source_PresentationClean_R10_20260803.zip",
    "10f_SGA6_English_Source_R10_20260803.zip",
    "10i_SGA7I_English_Source_CleanFont_R2_20260803.zip",
    "10j_SGA7II_English_Source_CleanFont_R2_20260803.zip",
)
TOP_LEVEL_CONTROLS = (
    "README.md",
    "PACKAGE_CONTENT_MANIFEST.csv",
    "PACKAGE_CONTENT_VALIDATION.json",
    "PACKAGE_VALIDATION.json",
    PAYLOAD_MANIFEST,
    PAYLOAD_VALIDATION,
)
DIRECT_CONTROL_PATHS = (
    "controls/CURRENT_SUPERSESSION_AND_ORDER.csv",
    "controls/PACKAGE_LOGBOOK.md",
    "controls/PUBLIC_PRIVACY_TRANSFORM.csv",
    "controls/PUBLIC_PROJECTION_EXCLUSIONS.csv",
    "controls/PUBLIC_PROJECTION_REPAIR_VALIDATION.json",
    "controls/PUBLICATION_READINESS.md",
    "controls/REFERENCE_GRAPH_README.md",
    "controls/RIGHTS_AND_PROVENANCE.md",
    "controls/current_global_r3/APPLICATION_VALIDATION.json",
    "controls/current_global_r3/PDF_FONTS.txt",
    "controls/current_global_r3/PDF_IMAGES.txt",
    "controls/current_global_r3/PDF_INFO.txt",
    "controls/current_global_r3/R3_CONTINUATION.md",
    "controls/current_global_r3/R3_CROSS_VOLUME_LOGBOOK.md",
    "controls/current_global_r3/R3_STATUS.md",
    "controls/current_global_r3/REFERENCE_CANDIDATES_VALIDATION.json",
    "controls/current_global_r3/REFERENCE_CANDIDATES.csv",
    "controls/current_global_r3/REFERENCE_EDGES.csv",
    "controls/current_global_r3/REFERENCE_FORMULA_SAFETY_TRANSFORM.csv",
    "controls/current_global_r3/REFERENCE_GRAPH_VALIDATION.json",
    "controls/current_global_r3/REFERENCE_RESIDUALS.csv",
    "controls/current_global_r3/REFERENCE_TARGETS.csv",
)
CONTROL_ORDER = (
    "README.md",
    "PACKAGE_LOGBOOK.md",
    "RIGHTS_AND_PROVENANCE.md",
    "PUBLICATION_READINESS.md",
    "R3_CROSS_VOLUME_LOGBOOK.md",
    "R3_STATUS.md",
    "R3_CONTINUATION.md",
    "CURRENT_SUPERSESSION_AND_ORDER.csv",
    "PUBLIC_PRIVACY_TRANSFORM.csv",
    "PUBLIC_PROJECTION_EXCLUSIONS.csv",
    "PUBLIC_PROJECTION_REPAIR_VALIDATION.json",
    "REFERENCE_GRAPH_README.md",
    "REFERENCE_TARGETS.csv",
    "REFERENCE_CANDIDATES.csv",
    "REFERENCE_EDGES.csv",
    "REFERENCE_RESIDUALS.csv",
    "REFERENCE_FORMULA_SAFETY_TRANSFORM.csv",
    "REFERENCE_CANDIDATES_VALIDATION.json",
    "REFERENCE_GRAPH_VALIDATION.json",
    "APPLICATION_VALIDATION.json",
    "PDF_INFO.txt",
    "PDF_FONTS.txt",
    "PDF_IMAGES.txt",
    "PACKAGE_CONTENT_MANIFEST.csv",
    "PACKAGE_CONTENT_VALIDATION.json",
    "PACKAGE_VALIDATION.json",
    PAYLOAD_MANIFEST,
    PAYLOAD_VALIDATION,
)

OBSOLETE_PREDECESSOR_FILES = {
    "00_Current_SGA1-7II_English_Presentation_Clean_Readers_and_Buildable_Source_20260803.zip",
    "10b_SGA2_English_Source_and_History_R10_20260730.zip",
    "ARCHIVE_PRIVACY_TRANSFORMATIONS.csv",
    "PACKAGE_MANIFEST_VALIDATION.json",
    "PACKAGE_PAYLOAD_MANIFEST.csv",
    "PACKAGE_PREMANIFEST_VALIDATION.json",
    "SGA_English_1_7II_presentation_clean_checkpoint_20260803_r2_COMPLETE_ZIP_VALIDATION.json",
}
EXPECTED_CHANGED_SAME_NAMES = {
    GLOBAL_READER,
    "10c_SGA3_English_Reader_and_Buildable_TeX_R29_20260730.zip",
}

TEMP_ROOT = (
    Path(os.environ.get("LOCALAPPDATA", os.environ.get("TEMP", ".")))
    / "Temp"
    / "sga_global_reference_r3_20260804"
)
STATE_PATH = TEMP_ROOT / "draft_state.json"


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


def auth(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def auth_modern(token: str) -> dict[str, str]:
    return {**auth(token), **MODERN}


def file_identity(entry: dict) -> tuple[int, str]:
    return int(entry["size"]), normalized_md5(entry["checksum"])


def legacy_identity(entry: dict) -> tuple[int, str]:
    return int(entry["filesize"]), normalized_md5(entry["checksum"])


def replay_zip(root: Path) -> dict[str, object]:
    expected: dict[str, tuple[int, str]] = {}
    with (root / CONTENT_MANIFEST).open(
        "r", encoding="utf-8-sig", newline=""
    ) as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 150:
        raise RuntimeError("SGA content manifest row count changed")
    for row in rows:
        name = row["relative_path"].replace("\\", "/")
        expected[name] = (int(row["bytes"]), row["sha256"].upper())
    for name in (CONTENT_MANIFEST, CONTENT_VALIDATION):
        path = root / name
        expected[name] = (path.stat().st_size, sha256(path))

    observed: dict[str, dict[str, object]] = {}
    archive_path = root / COMPLETE_ZIP
    with zipfile.ZipFile(archive_path) as archive:
        infos = [info for info in archive.infolist() if not info.is_dir()]
        names = [info.filename.replace("\\", "/") for info in infos]
        if len(infos) != EXPECTED_ZIP_MEMBERS or len(names) != len(set(names)):
            raise RuntimeError("SGA complete ZIP count or uniqueness changed")
        if set(names) != set(expected):
            raise RuntimeError("SGA complete ZIP member boundary changed")
        for index, info in enumerate(infos, start=1):
            name = info.filename.replace("\\", "/")
            digest = hashlib.sha256()
            with archive.open(info) as handle:
                for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
                    digest.update(block)
            identity = (info.file_size, digest.hexdigest().upper())
            if identity != expected[name]:
                raise RuntimeError(f"SGA complete ZIP member changed: {name}")
            observed[name] = {"bytes": identity[0], "sha256": identity[1]}
    return {
        "status": "PASS",
        "members": len(observed),
        "bytes": archive_path.stat().st_size,
        "sha256": sha256(archive_path),
        "member_identities": observed,
    }


def local_surface(root: Path, *, replay_complete_zip: bool = True) -> dict[str, object]:
    if not root.is_dir():
        raise RuntimeError(f"SGA package root is not a directory: {root}")
    all_paths = sorted(
        (path for path in root.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(root).as_posix().casefold(),
    )
    if (
        len(all_paths) != EXPECTED_ROOT_FILES
        or sum(path.stat().st_size for path in all_paths) != EXPECTED_ROOT_BYTES
    ):
        raise RuntimeError("SGA package root file count or byte total changed")

    manifest_path = root / PAYLOAD_MANIFEST
    validation_path = root / PAYLOAD_VALIDATION
    fixed = {
        PAYLOAD_MANIFEST: (EXPECTED_MANIFEST_BYTES, EXPECTED_MANIFEST_SHA256),
        PAYLOAD_VALIDATION: (
            EXPECTED_MANIFEST_VALIDATION_BYTES,
            EXPECTED_MANIFEST_VALIDATION_SHA256,
        ),
        COMPLETE_ZIP: (EXPECTED_ZIP_BYTES, EXPECTED_ZIP_SHA256),
        GLOBAL_READER: (EXPECTED_GLOBAL_BYTES, EXPECTED_GLOBAL_SHA256),
    }
    for name, identity in fixed.items():
        path = root / name
        if (path.stat().st_size, sha256(path)) != identity:
            raise RuntimeError(f"Fixed SGA package identity changed: {name}")

    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    if (
        validation.get("status") != "PASS"
        or validation.get("errors") != []
        or validation.get("manifest", {}).get("rows") != EXPECTED_MANIFEST_ROWS
        or validation.get("manifest", {}).get("canonical_tree_sha256")
        != EXPECTED_MANIFEST_TREE_SHA256
    ):
        raise RuntimeError("SGA payload-manifest validation changed")

    with manifest_path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError("SGA payload manifest row count changed")
    represented = set()
    row_identity: dict[str, tuple[int, str]] = {}
    for row in rows:
        relative = row["relative_path"].replace("\\", "/")
        path = root / Path(relative)
        represented.add(relative)
        expected = (int(row["bytes"]), row["sha256"].upper())
        if not path.is_file() or (path.stat().st_size, sha256(path)) != expected:
            raise RuntimeError(f"SGA payload-manifest replay changed: {relative}")
        row_identity[relative] = expected
    all_relative = {path.relative_to(root).as_posix() for path in all_paths}
    if all_relative - represented != {PAYLOAD_MANIFEST, PAYLOAD_VALIDATION}:
        raise RuntimeError("SGA self-excluding payload-manifest boundary changed")

    top_names = {path.name for path in root.iterdir() if path.is_file()}
    required_top = {
        COMPLETE_ZIP,
        GLOBAL_READER,
        *STANDALONE_READERS,
        *MASTER_TEX,
        *SOURCE_ZIPS,
        *TOP_LEVEL_CONTROLS,
    }
    if top_names != required_top or len(top_names) != 35:
        raise RuntimeError("SGA top-level public surface changed")

    direct_paths = [root / name for name in sorted(top_names, key=str.casefold)]
    direct_paths.extend(root / Path(relative) for relative in DIRECT_CONTROL_PATHS)
    remote_names = [path.name for path in direct_paths]
    if len(remote_names) != EXPECTED_DIRECT_FILES or len(set(remote_names)) != len(remote_names):
        raise RuntimeError("SGA direct-public filename count or uniqueness changed")
    surface = {
        path.name: {
            "path": path,
            "relative_path": path.relative_to(root).as_posix(),
            "bytes": path.stat().st_size,
            "md5": md5(path),
            "sha256": sha256(path),
        }
        for path in direct_paths
    }
    for name, row in surface.items():
        relative = str(row["relative_path"])
        if relative not in row_identity and relative not in {
            PAYLOAD_MANIFEST,
            PAYLOAD_VALIDATION,
        }:
            raise RuntimeError(f"Direct SGA object is not manifest-bound: {name}")

    order = [
        COMPLETE_ZIP,
        GLOBAL_READER,
        *STANDALONE_READERS,
        *MASTER_TEX,
        *SOURCE_ZIPS,
        *CONTROL_ORDER,
    ]
    if len(order) != EXPECTED_DIRECT_FILES or set(order) != set(surface):
        raise RuntimeError("SGA configured public order is not an exact permutation")

    package_validation = json.loads(
        (root / "PACKAGE_VALIDATION.json").read_text(encoding="utf-8")
    )
    if package_validation.get("status") != "PASS" or package_validation.get("errors") != []:
        raise RuntimeError("SGA package validation is not PASS/errors[]")

    result: dict[str, object] = {
        "surface": surface,
        "order": order,
        "root_files": len(all_paths),
        "root_bytes": sum(path.stat().st_size for path in all_paths),
        "manifest_rows": len(rows),
    }
    if replay_complete_zip:
        zip_result = replay_zip(root)
        if zip_result["sha256"] != EXPECTED_ZIP_SHA256:
            raise RuntimeError("SGA complete ZIP replay identity changed")
        result["zip_replay"] = zip_result
    return result


def fetch_live_predecessor(session, surface: dict[str, dict[str, object]]) -> dict:
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
        len(entries),
        sum(int(row["size"]) for row in entries.values()),
        live.get("files", {}).get("default_preview"),
        live.get("status"),
        live.get("versions", {}).get("is_latest"),
    )
    expected = (
        PREDECESSOR_ID,
        PREDECESSOR_DOI,
        CONCEPT_ID,
        CONCEPT_DOI,
        PREDECESSOR_FILES,
        PREDECESSOR_BYTES,
        PREDECESSOR_PREVIEW,
        "published",
        True,
    )
    if observed != expected:
        raise RuntimeError(f"SGA live predecessor boundary changed: {observed!r}")

    desired_names = set(surface)
    if set(entries) != (set(entries) & desired_names) | OBSOLETE_PREDECESSOR_FILES:
        raise RuntimeError("SGA live predecessor filename boundary changed")
    retained_names = set(entries) & desired_names
    if len(retained_names) != 27 or len(OBSOLETE_PREDECESSOR_FILES) != 7:
        raise RuntimeError("SGA predecessor retained/obsolete partition changed")
    changed = {
        name
        for name in retained_names
        if file_identity(entries[name])
        != (int(surface[name]["bytes"]), str(surface[name]["md5"]))
    }
    if changed != EXPECTED_CHANGED_SAME_NAMES:
        raise RuntimeError(f"SGA changed same-name partition changed: {sorted(changed)}")
    exact = retained_names - changed
    if len(exact) != 25:
        raise RuntimeError("SGA exact inherited no-op count changed")
    return live


def verify_active_draft_boundary(session, token: str) -> dict | None:
    state = load_state()
    predecessor_scoped = session.get(
        f"{API}/records/{PREDECESSOR_ID}/draft",
        headers=auth_modern(token),
        timeout=(30, 180),
    )
    if state is None:
        if predecessor_scoped.status_code == 200:
            raise RuntimeError("Untracked SGA successor draft exists; refusing mutation")
        base.check(predecessor_scoped, {404})
        return None
    if state.get("published"):
        if predecessor_scoped.status_code not in {404, 410}:
            raise RuntimeError("Published SGA state conflicts with an active draft")
        return state
    # Zenodo may expose the successor only at its own draft id and return 404
    # for the predecessor-scoped convenience route.  The durable state file is
    # therefore the authority for which one draft may be resumed, and that
    # exact id must itself remain authenticated and open.
    if predecessor_scoped.status_code == 200:
        if int(predecessor_scoped.json()["id"]) != int(state["draft_id"]):
            raise RuntimeError("Predecessor-scoped SGA draft identity changed")
    else:
        base.check(predecessor_scoped, {404})
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
        raise RuntimeError("Tracked SGA draft identity, concept, or state changed")
    return state


def create_or_resume_draft(session, token: str, live: dict) -> tuple[int, bool]:
    state = verify_active_draft_boundary(session, token)
    if state is not None:
        if state.get("published"):
            raise RuntimeError("Tracked SGA successor is already published")
        draft_id = int(state["draft_id"])
        draft = base.check(
            session.get(
                f"{API}/records/{draft_id}/draft",
                headers=auth_modern(token),
                timeout=(30, 180),
            ),
            {200},
        ).json()
        if str(draft.get("parent", {}).get("id")) != CONCEPT_ID:
            raise RuntimeError("Tracked SGA draft left the required concept")
        return draft_id, False

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
        raise RuntimeError("SGA predecessor is not a safe same-concept versioning base")
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
        raise RuntimeError("SGA successor did not inherit the exact predecessor files")
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
        or modern.get("parent", {}).get("pids", {}).get("doi", {}).get("identifier")
        != CONCEPT_DOI
        or modern.get("versions", {}).get("index")
        != int(live.get("versions", {}).get("index", 0)) + 1
        or modern.get("versions", {}).get("is_latest_draft") is not True
    ):
        raise RuntimeError("Created SGA draft lineage/version identity changed")
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


def desired_metadata(current: dict) -> dict:
    metadata = copy.deepcopy(current)
    metadata["title"] = TITLE
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["version"] = VERSION
    metadata["description"] = DESCRIPTION
    metadata["additional_descriptions"] = [
        {"description": ADDITIONAL_NOTE, "type": {"id": "notes"}}
    ]
    return metadata


def verify_staged(
    draft: dict,
    surface: dict[str, dict[str, object]],
    order: list[str],
) -> None:
    entries = modern_entries(draft)
    if set(entries) != set(surface):
        raise RuntimeError("SGA staged filename boundary is not exact")
    mismatches = []
    for name, local in surface.items():
        if file_identity(entries[name]) != (int(local["bytes"]), str(local["md5"])):
            mismatches.append(name)
    if mismatches:
        raise RuntimeError(f"SGA staged file identity mismatches: {mismatches}")
    metadata = draft.get("metadata", {})
    notes = metadata.get("additional_descriptions", [])
    if (
        metadata.get("title") != TITLE
        or metadata.get("publication_date") != PUBLICATION_DATE
        or metadata.get("version") != VERSION
        or metadata.get("description") != DESCRIPTION
        or len(notes) != 1
        or notes[0].get("description") != ADDITIONAL_NOTE
        or notes[0].get("type", {}).get("id") != "notes"
        or draft.get("files", {}).get("default_preview") != GLOBAL_READER
    ):
        raise RuntimeError("SGA staged metadata or default preview changed")
    observed_order = draft.get("files", {}).get("order") or []
    if observed_order not in (order, []):
        raise RuntimeError("SGA staged file order conflicts with the required order")


def preflight(session, token: str, root: Path) -> dict[str, object]:
    package = local_surface(root)
    surface = package["surface"]
    assert isinstance(surface, dict)
    live = fetch_live_predecessor(session, surface)
    state = verify_active_draft_boundary(session, token)
    return {
        "status": "PASS_READY_FOR_ONE_SAME_CONCEPT_SUCCESSOR",
        "concept_id": CONCEPT_ID,
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_ID,
        "predecessor_doi": PREDECESSOR_DOI,
        "predecessor_version_index": live["versions"]["index"],
        "predecessor_files": len(modern_entries(live)),
        "predecessor_bytes": sum(
            int(row["size"]) for row in modern_entries(live).values()
        ),
        "active_draft": state is not None and not state.get("published", False),
        "tracked_draft_id": None if state is None else state.get("draft_id"),
        "package_root_files": package["root_files"],
        "package_root_bytes": package["root_bytes"],
        "manifest_rows_replayed": package["manifest_rows"],
        "zip_members_replayed": package["zip_replay"]["members"],
        "direct_public_files": len(surface),
        "direct_public_bytes": sum(int(row["bytes"]) for row in surface.values()),
        "inherited_exact_noops": 25,
        "changed_same_name_replacements": sorted(EXPECTED_CHANGED_SAME_NAMES),
        "obsolete_inherited_files_to_remove": sorted(OBSOLETE_PREDECESSOR_FILES),
        "duplicate_concept_created": False,
    }


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


def stage(session, token: str, root: Path) -> dict[str, object]:
    package = local_surface(root)
    surface = package["surface"]
    order = package["order"]
    assert isinstance(surface, dict) and isinstance(order, list)
    live = fetch_live_predecessor(session, surface)
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
    allowed = set(modern_entries(live)) | set(surface)
    if not set(remote).issubset(allowed):
        raise RuntimeError("Tracked SGA draft contains an unexpected filename")

    deleted = []
    for name in sorted(set(remote) - set(surface), key=str.casefold):
        print(f"DELETE SUPERSEDED {name}", flush=True)
        base.check(
            session.delete(
                remote[name]["links"]["self"],
                headers=auth(token),
                timeout=(30, 600),
            ),
            {204},
        )
        deleted.append(name)

    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth(token),
            timeout=(30, 300),
        ),
        {200},
    ).json()
    remote = legacy_entries(deposition)
    replaced = []
    for name in sorted(set(remote) & set(surface), key=str.casefold):
        wanted = (int(surface[name]["bytes"]), str(surface[name]["md5"]))
        if legacy_identity(remote[name]) == wanted:
            continue
        print(f"DELETE FOR EXACT REPLACEMENT {name}", flush=True)
        base.check(
            session.delete(
                remote[name]["links"]["self"],
                headers=auth(token),
                timeout=(30, 600),
            ),
            {204},
        )
        replaced.append(name)

    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth(token),
            timeout=(30, 300),
        ),
        {200},
    ).json()
    remote = legacy_entries(deposition)
    bucket = deposition["links"]["bucket"]
    uploaded = []
    for name in order:
        if name in remote:
            continue
        upload_file(session, token, bucket, name, Path(surface[name]["path"]))
        uploaded.append(name)

    draft = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft",
            headers=auth_modern(token),
            timeout=(30, 600),
        ),
        {200},
    ).json()
    entries = modern_entries(draft)
    if set(entries) != set(surface):
        raise RuntimeError("SGA staged file set is incomplete after upload")
    identity_errors = [
        name
        for name in surface
        if file_identity(entries[name])
        != (int(surface[name]["bytes"]), str(surface[name]["md5"]))
    ]
    if identity_errors:
        raise RuntimeError(f"SGA staged MD5/byte mismatches: {identity_errors}")

    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": GLOBAL_READER,
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
    verify_staged(patched, surface, order)
    state = load_state()
    if state is None or int(state["draft_id"]) != draft_id:
        raise RuntimeError("SGA tracked state disappeared while staging")
    state.update(
        {
            "status": "STAGED_EXACT_READY_FOR_EXPLICIT_PUBLISH",
            "staged": True,
            "staged_files": len(surface),
            "staged_bytes": sum(int(row["bytes"]) for row in surface.values()),
            "default_preview": GLOBAL_READER,
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
        "predecessor_record": PREDECESSOR_ID,
        "created_new_same_concept_draft": created,
        "duplicate_concept_created": False,
        "deleted_superseded": deleted,
        "replaced_same_name": replaced,
        "uploaded_now": uploaded,
        "files": len(surface),
        "bytes": sum(int(row["bytes"]) for row in surface.values()),
        "default_preview": patched["files"]["default_preview"],
        "file_order": order,
        "title": patched["metadata"]["title"],
        "publication_date": patched["metadata"]["publication_date"],
        "version": patched["metadata"]["version"],
    }


def stream_public_identity(
    session,
    url: str,
    destination: Path | None = None,
) -> tuple[int, str]:
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


def replay_downloaded_zip(path: Path, root: Path) -> dict[str, object]:
    with (root / CONTENT_MANIFEST).open(
        "r", encoding="utf-8-sig", newline=""
    ) as handle:
        rows = list(csv.DictReader(handle))
    expected = {
        row["relative_path"].replace("\\", "/"): (
            int(row["bytes"]),
            row["sha256"].upper(),
        )
        for row in rows
    }
    for name in (CONTENT_MANIFEST, CONTENT_VALIDATION):
        local = root / name
        expected[name] = (local.stat().st_size, sha256(local))
    errors = []
    observed = []
    with zipfile.ZipFile(path) as archive:
        infos = [info for info in archive.infolist() if not info.is_dir()]
        names = [info.filename.replace("\\", "/") for info in infos]
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
            observed.append(
                {
                    "relative_path": name,
                    "bytes": identity[0],
                    "sha256": identity[1],
                    "match": match,
                }
            )
    return {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "members": len(observed),
        "matches": sum(1 for row in observed if row["match"]),
        "mismatches": sum(1 for row in observed if not row["match"]),
        "member_identities": observed,
    }


def publish_and_readback(
    session,
    token: str,
    root: Path,
    confirm_draft_id: str,
    receipt_path: Path | None,
) -> dict[str, object]:
    package = local_surface(root)
    surface = package["surface"]
    order = package["order"]
    assert isinstance(surface, dict) and isinstance(order, list)
    live = fetch_live_predecessor(session, surface)
    state = verify_active_draft_boundary(session, token)
    if state is None or state.get("published") or not state.get("staged"):
        raise RuntimeError("No exact staged SGA draft is tracked for publication")
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
    verify_staged(draft, surface, order)
    if (
        str(draft.get("parent", {}).get("id")) != CONCEPT_ID
        or draft.get("versions", {}).get("index")
        != int(live.get("versions", {}).get("index", 0)) + 1
    ):
        raise RuntimeError("SGA staged draft lineage or version index changed")

    published_response = base.check(
        session.post(
            draft["links"]["publish"],
            headers=auth_modern(token),
            timeout=(30, 1200),
        ),
        {200, 202},
    )
    try:
        record_id = int(published_response.json().get("id", draft_id))
    except Exception:
        record_id = draft_id
    if record_id != draft_id:
        raise RuntimeError("SGA publication returned an unexpected record id")
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
        raise RuntimeError("SGA successor did not become anonymously public")
    if (
        str(record.get("parent", {}).get("id")) != CONCEPT_ID
        or record.get("parent", {}).get("pids", {}).get("doi", {}).get("identifier")
        != CONCEPT_DOI
        or record.get("versions", {}).get("index")
        != int(live.get("versions", {}).get("index", 0)) + 1
        or record.get("versions", {}).get("is_latest") is not True
    ):
        raise RuntimeError("Published SGA concept/version identity changed")
    verify_staged(record, surface, order)

    entries = modern_entries(record)
    download_path = TEMP_ROOT / f"record_{record_id}_{COMPLETE_ZIP}"
    download_path.parent.mkdir(parents=True, exist_ok=True)
    readback_rows = []
    errors = []
    for index, name in enumerate(order, start=1):
        print(f"READBACK {index}/{len(order)} {name}", flush=True)
        destination = download_path if name == COMPLETE_ZIP else None
        observed = stream_public_identity(
            anonymous, entries[name]["links"]["content"], destination
        )
        expected = (int(surface[name]["bytes"]), str(surface[name]["sha256"]))
        match = observed == expected
        if not match:
            errors.append(name)
        readback_rows.append(
            {
                "filename": name,
                "source_relative_path": surface[name]["relative_path"],
                "bytes": observed[0],
                "sha256": observed[1],
                "match": match,
                "content_url": entries[name]["links"]["content"],
            }
        )
    if errors:
        raise RuntimeError(f"SGA anonymous direct-file readback mismatches: {errors}")
    zip_readback = replay_downloaded_zip(download_path, root)
    if (
        zip_readback["status"] != "PASS"
        or zip_readback["matches"] != EXPECTED_ZIP_MEMBERS
    ):
        raise RuntimeError("SGA anonymous complete-ZIP member replay failed")
    download_path.unlink()

    active = session.get(
        f"{API}/records/{PREDECESSOR_ID}/draft",
        headers=auth_modern(token),
        timeout=(30, 180),
    )
    if active.status_code not in {404, 410}:
        raise RuntimeError("An SGA active draft remains after publication")

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
        "direct_readback_matches": sum(1 for row in readback_rows if row["match"]),
        "direct_readback_mismatches": 0,
        "complete_zip": {
            "filename": COMPLETE_ZIP,
            "bytes": EXPECTED_ZIP_BYTES,
            "sha256": EXPECTED_ZIP_SHA256,
            "members": EXPECTED_ZIP_MEMBERS,
            "member_readback_matches": zip_readback["matches"],
            "member_readback_mismatches": zip_readback["mismatches"],
        },
        "manifest": {
            "filename": PAYLOAD_MANIFEST,
            "bytes": EXPECTED_MANIFEST_BYTES,
            "sha256": EXPECTED_MANIFEST_SHA256,
            "represented_rows": EXPECTED_MANIFEST_ROWS,
            "represented_tree_sha256": EXPECTED_MANIFEST_TREE_SHA256,
        },
        "active_draft": False,
        "duplicate_concept_created": False,
        "direct_readback": readback_rows,
        "complete_zip_member_readback": zip_readback,
    }
    state.update(
        {
            "status": "PASS_PUBLISHED_AND_ANONYMOUS_READBACK",
            "doi": result["version_doi"],
            "record_url": result["record_url"],
            "readback_matches": result["direct_readback_matches"],
            "zip_member_matches": zip_readback["matches"],
            "readback_completed_at_epoch": int(time.time()),
        }
    )
    save_json(STATE_PATH, state)
    if receipt_path is not None:
        save_json(receipt_path, result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("preflight", "stage", "publish"))
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--confirm-publish")
    args = parser.parse_args()
    root = args.root.resolve()
    session = base.make_session()
    token = base.find_token()
    if args.action == "preflight":
        result = preflight(session, token, root)
    elif args.action == "stage":
        result = stage(session, token, root)
    else:
        if not args.confirm_publish:
            raise RuntimeError("Publishing requires --confirm-publish DRAFT_ID")
        result = publish_and_readback(
            session,
            token,
            root,
            args.confirm_publish,
            args.receipt,
        )
    summary = {
        key: value
        for key, value in result.items()
        if key
        not in {
            "direct_readback",
            "complete_zip_member_readback",
            "file_order",
            "configured_file_order",
            "api_file_order",
            "uploaded_now",
        }
    }
    if "uploaded_now" in result:
        summary["uploaded_now_count"] = len(result["uploaded_now"])
    print(json.dumps(summary, ensure_ascii=True, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr, flush=True)
        raise
