#!/usr/bin/env python3
"""Restore the exact pre-provisional SGA file shelf as a same-concept head."""

from __future__ import annotations

import copy
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
CURRENT_RECORD = 21775746
RESTORE_RECORD = 21762813
CONCEPT_DOI = "10.5281/zenodo.20410947"
RESTORE_FILES = 92
RESTORE_BYTES = 783_417_797
DEFAULT_PREVIEW = "00b_SGA2_English_Reader.pdf"
PRIMARY_ZIP = "00_Current_SGA1-7II_English_Readers_and_Buildable_TeX_20260802.zip"
PROVISIONAL_ADDITIONS = {
    "00z_SGA_1-7II_English_Global_Reader_navigation_r3_PROVISIONAL_20260803.pdf",
    "10z1_SGA_1-7II_Global_Reader_navigation_r3_VALIDATION_20260803.json",
    "10z2_SGA_1-7II_Global_Reader_navigation_r3_BUILD_EVIDENCE_20260803.json",
    "10z3_SGA_1-7II_Global_Reader_INPUT_READERS_r3_20260803.csv",
    "10z4_SGA_1-7II_Global_Reader_LOGBOOK_PRIVACY_CLEAN_20260803.md",
    "10z5_SGA_1-7II_Global_Reader_ARCHIVE_README_CAVEATS_20260803.md",
    "10z6_SGA_1-7II_Global_Reader_PUBLIC_MANIFEST_20260803.csv",
    "10z7_SGA_1-7II_Global_Reader_PUBLIC_PACKAGE_20260803.zip",
}
MODERN = {"Accept": "application/vnd.inveniordm.v1+json"}
DESCRIPTION = (
    "<p><strong>SGA 1-7 archive:</strong> This record provides the current English "
    "reader shelf for SGA 1 through SGA 7 II, together with French reader texts, "
    "buildable TeX sources, compact source archives, validation evidence, and "
    "append-only provenance.</p>"
    "<p><strong>Start here:</strong> the first ZIP collects the complete direct "
    "English reader shelf and its buildable TeX closures. The same English readers "
    "and principal TeX files are also available individually for immediate reading "
    "and source inspection.</p>"
    "<p><strong>Coverage:</strong> SGA 1 through SGA 6 are represented by their "
    "current English readers. SGA 3 includes the complete 1,470-page cumulative "
    "reader covering the Introduction, Exposes I-XXVI, indexes, and guide. SGA 7 I "
    "includes its complete English working reader for all written exposes; SGA 7 II "
    "includes its complete English working reader through volume EOF. The separately "
    "available French SGA 7 II working transcription remains partial and is not "
    "represented as complete.</p>"
    "<p><strong>Sources and auditability:</strong> direct TeX, compact buildable source "
    "archives, manifests, decision history, correction ledgers, and validation "
    "surfaces are retained so readers can inspect both the texts and their production "
    "history.</p>"
    "<p>These are working scholarly translations, editions, or transcriptions, not "
    "critical editions, peer review, mathematical certification, exhaustive reference "
    "certification, accessibility certification, or a new rights determination.</p>"
)


def modern_record(session, record_id: int, *, token: str | None = None) -> dict:
    headers = dict(MODERN)
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return base.check(
        session.get(
            f"{API}/records/{record_id}?expand=true",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()


def identity(entry: dict) -> tuple[int, str]:
    return int(entry["size"]), base.normalized_md5(entry["checksum"])


def assert_same(entries: dict[str, dict], wanted: dict[str, dict], label: str) -> None:
    if set(entries) != set(wanted):
        raise RuntimeError(f"{label}: file-name boundary differs")
    for name, row in wanted.items():
        if identity(entries[name]) != identity(row):
            raise RuntimeError(f"{label}: inherited identity differs for {name}")


def ordered(names: set[str]) -> list[str]:
    english_pdfs = sorted(
        (name for name in names if name.lower().endswith(".pdf") and "english" in name.lower()),
        key=str.casefold,
    )
    other_pdfs = sorted(
        (name for name in names if name.lower().endswith(".pdf") and name not in english_pdfs),
        key=str.casefold,
    )
    tex = sorted((name for name in names if name.lower().endswith(".tex")), key=str.casefold)
    preferred = [PRIMARY_ZIP, *english_pdfs, *other_pdfs, *tex]
    result = [name for name in preferred if name in names]
    result.extend(sorted(names - set(result), key=str.casefold))
    if result[0] != PRIMARY_ZIP:
        raise RuntimeError("Complete reader/source ZIP is not first")
    return result


def main() -> None:
    session = base.make_session()
    token = base.find_token()
    auth_legacy = {"Authorization": f"Bearer {token}"}
    auth_modern = {**MODERN, "Authorization": f"Bearer {token}"}

    current = modern_record(session, CURRENT_RECORD)
    restore = modern_record(session, RESTORE_RECORD)
    if (
        current["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or restore["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or current.get("is_published") is not True
        or restore.get("is_published") is not True
    ):
        raise RuntimeError("SGA concept/published guard failed")
    current_entries = base.modern_entries(current)
    restore_entries = base.modern_entries(restore)
    if (
        len(restore_entries) != RESTORE_FILES
        or sum(int(row["size"]) for row in restore_entries.values()) != RESTORE_BYTES
        or set(current_entries) - set(restore_entries) != PROVISIONAL_ADDITIONS
        or set(restore_entries) - set(current_entries)
    ):
        raise RuntimeError("Pre-provisional restore boundary changed")
    for name, row in restore_entries.items():
        if identity(current_entries[name]) != identity(row):
            raise RuntimeError(f"Current record mutated predecessor byte: {name}")

    latest = base.check(
        session.get(current["links"]["latest"], headers=MODERN, timeout=(30, 180)),
        {200},
    ).json()
    if int(latest["id"]) != CURRENT_RECORD:
        raise RuntimeError("Current SGA head changed before restore")
    probe = session.get(
        f"{API}/records/{CURRENT_RECORD}/draft?expand=true",
        headers=auth_modern,
        timeout=(30, 180),
    )
    if probe.status_code != 404:
        raise RuntimeError("An active SGA draft already exists; refusing a parallel draft")

    predecessor = base.check(
        session.get(
            f"{API}/deposit/depositions/{CURRENT_RECORD}",
            headers=auth_legacy,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    created = base.check(
        session.post(
            predecessor["links"]["newversion"],
            headers=auth_legacy,
            timeout=(30, 300),
        ),
        {201},
    ).json()
    deposition = base.check(
        session.get(
            created["links"]["latest_draft"],
            headers=auth_legacy,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    draft_id = int(deposition["id"])
    inherited = base.legacy_entries(deposition)
    if set(inherited) != set(current_entries):
        raise RuntimeError("New restore draft did not inherit the current head exactly")
    for name in PROVISIONAL_ADDITIONS:
        base.check(
            session.delete(
                inherited[name]["links"]["self"],
                headers=auth_legacy,
                timeout=(30, 300),
            ),
            {204},
        )

    draft = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft?expand=true",
            headers=auth_modern,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    draft_entries = base.modern_entries(draft)
    assert_same(draft_entries, restore_entries, "staged restore")
    metadata = copy.deepcopy(restore["metadata"])
    metadata["publication_date"] = "2026-08-03"
    metadata["version"] = "2026-08-03 complete SGA 1-7 II reader shelf"
    metadata["description"] = DESCRIPTION
    metadata["additional_descriptions"] = []
    order = ordered(set(draft_entries))
    payload = {
        "access": restore["access"],
        "files": {
            "enabled": True,
            "default_preview": DEFAULT_PREVIEW,
            "order": order,
        },
        "metadata": metadata,
        "custom_fields": restore.get("custom_fields", {}),
    }
    if draft.get("pids"):
        payload["pids"] = draft["pids"]
    patched = base.check(
        session.put(
            f"{API}/records/{draft_id}/draft",
            headers={**auth_modern, "Content-Type": "application/json"},
            json=payload,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    assert_same(base.modern_entries(patched), restore_entries, "patched restore")
    if (
        patched["files"].get("default_preview") != DEFAULT_PREVIEW
        or patched["files"].get("order") not in ([], order)
        or patched["metadata"].get("description") != DESCRIPTION
        or patched["metadata"].get("additional_descriptions") != []
        or patched["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
    ):
        raise RuntimeError("Restore presentation controls changed")

    published = base.check(
        session.post(
            patched["links"]["publish"],
            headers=auth_modern,
            timeout=(30, 900),
        ),
        {200, 202},
    ).json()
    record_id = int(published["id"])
    record = None
    for attempt in range(30):
        response = session.get(
            f"{API}/records/{record_id}?expand=true",
            headers=MODERN,
            timeout=(30, 180),
        )
        if response.status_code == 200 and response.json().get("is_published"):
            record = response.json()
            break
        time.sleep(min(1 + attempt, 5))
    if record is None:
        raise RuntimeError("Published restore did not become public")
    assert_same(base.modern_entries(record), restore_entries, "public restore")
    latest = base.check(
        session.get(record["links"]["latest"], headers=MODERN, timeout=(30, 180)),
        {200},
    ).json()
    if (
        int(latest["id"]) != record_id
        or record["files"].get("default_preview") != DEFAULT_PREVIEW
        or record["files"].get("order") not in ([], order)
        or record["metadata"].get("description") != DESCRIPTION
        or record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
    ):
        raise RuntimeError("Public restore identity/presentation check failed")
    draft_check = session.get(
        f"{API}/records/{record_id}/draft",
        headers=auth_modern,
        timeout=(30, 180),
    )
    if draft_check.status_code != 404:
        raise RuntimeError("Published restore retains an edit draft")

    print(
        json.dumps(
            {
                "status": "PUBLISHED_RESTORE_PASS",
                "record_id": record_id,
                "doi": record["pids"]["doi"]["identifier"],
                "concept_doi": CONCEPT_DOI,
                "restored_from_record": RESTORE_RECORD,
                "supersedes_record": CURRENT_RECORD,
                "files": len(restore_entries),
                "bytes": sum(int(row["size"]) for row in restore_entries.values()),
                "default_preview": DEFAULT_PREVIEW,
                "first_file": order[0],
                "description_is_whole_project": record["metadata"]["description"] == DESCRIPTION,
                "active_draft": False,
                "duplicate_concept": False,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
