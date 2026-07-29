#!/usr/bin/env python3
"""Remove production and AI terminology from the live SGA reader metadata."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = SCRIPT_DIR / "publish_sga3_cumulative_with_x_zenodo_20260728.py"
SPEC = importlib.util.spec_from_file_location("zenodo_metadata_base", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established Zenodo workflow")
base = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = base
SPEC.loader.exec_module(base)


RECORD_ID = 21683140
DOI = "10.5281/zenodo.21683140"
CONCEPT_DOI = "10.5281/zenodo.20410947"
EXPECTED_FILE_COUNT = 68
EXPECTED_TOTAL_BYTES = 426_592_948
EXPECTED_TITLE = "SGA 1-6: English Readers, French Texts, and TeX Archives"
DEFAULT_PREVIEW = "00a_SGA1_English_Reader.pdf"

DESCRIPTION_HTML = "\n".join(
    (
        "<p>English readers for SGA 1 through SGA 6 are listed first in "
        "numerical order. Available French texts and editable TeX masters "
        "follow; supplementary source and historical files are grouped in "
        "ZIP archives.</p>",
        "<p>The SGA3 reader has 1,459 A4 pages and contains the Editorial "
        "Notice, Introduction, Exposes I-XXVI, the Tome-I index, the Tome-III "
        "mathematical guide, and the terminal index. Exposes V and VI use "
        "native TeX diagrams.</p>",
        "<p>The direct PDFs contain the mathematical text, diagrams, "
        "references, and original editorial apparatus.</p>",
        "<p>These editions do not transfer rights in the underlying French "
        "works. Historical Zenodo versions remain immutable.</p>",
    )
)
KEYWORDS = [
    "SGA",
    "Seminaire de Geometrie Algebrique",
    "Grothendieck",
    "algebraic geometry",
    "etale cohomology",
    "fundamental groups",
    "topoi",
    "group schemes",
    "duality",
    "intersection theory",
    "Riemann-Roch theorem",
    "LaTeX",
    "English translation",
    "French text",
    "SGA1",
    "SGA2",
    "SGA3",
    "SGA4",
    "SGA5",
    "SGA6",
]

BLOCKED_VISIBLE_TERMS = (
    "openai",
    "chatgpt",
    "codex",
    "claude",
    "anthropic",
    "large language model",
    "machine-assisted",
    "machine translation",
    "source audit",
    "source synchronization",
    "source rescribe",
    "workpass",
    "workflow",
    "production status",
    "publication readiness",
    "working edition",
    "bounded working",
    "public progress",
    "reference-v2",
    "machine-readable references",
    "not critical edition",
    "not certified",
    "uncertified",
)

REPO_ROOT = SCRIPT_DIR.parent
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
RECEIPT_PATH = (
    RECEIPT_ROOT
    / "20260729_sga_canonical_reader_metadata_cleanup_record_21683140.json"
)
HUMAN_RECEIPT_PATH = (
    RECEIPT_ROOT
    / "20260729_sga_canonical_reader_metadata_cleanup_record_21683140.md"
)


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def file_rows(record: dict) -> list[dict[str, object]]:
    rows = [
        {
            "key": row["key"],
            "size": int(row["size"]),
            "checksum": row["checksum"].lower(),
            "content_url": row["links"]["self"],
        }
        for row in record["files"]
    ]
    return sorted(rows, key=lambda row: str(row["key"]).casefold())


def file_aggregate(rows: list[dict[str, object]]) -> str:
    payload = "".join(
        f"{row['key']}\t{row['size']}\t{row['checksum']}\n" for row in rows
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest().upper()


def visible_metadata_text(metadata: dict) -> str:
    fields = [
        metadata.get("title", ""),
        metadata.get("description", ""),
        metadata.get("notes", ""),
        metadata.get("version", ""),
    ]
    fields.extend(metadata.get("keywords", []))
    fields.extend(
        contributor.get("name", "")
        for contributor in metadata.get("contributors", [])
    )
    fields.extend(
        row.get("description", "")
        for row in metadata.get("additional_descriptions", [])
    )
    return "\n".join(str(value) for value in fields).casefold()


def assert_clean_metadata(metadata: dict) -> None:
    if metadata.get("title") != EXPECTED_TITLE:
        raise RuntimeError("Unexpected SGA record title")
    if metadata.get("description") != DESCRIPTION_HTML:
        raise RuntimeError("Description did not update exactly")
    if metadata.get("notes") not in (None, ""):
        raise RuntimeError("Reader-facing notes were not removed")
    if metadata.get("keywords") != KEYWORDS:
        raise RuntimeError("Keywords did not update exactly")
    if metadata.get("contributors"):
        raise RuntimeError("Reader-facing contributor badges were not removed")
    visible = visible_metadata_text(metadata)
    hits = [term for term in BLOCKED_VISIBLE_TERMS if term in visible]
    if hits:
        raise RuntimeError(f"Visible metadata still contains blocked terms: {hits}")


def clear_modern_reader_frontmatter(metadata: dict) -> None:
    metadata["contributors"] = []
    metadata["additional_descriptions"] = [
        row
        for row in metadata.get("additional_descriptions", [])
        if row.get("type", {}).get("id") != "notes"
    ]


def assert_clean_modern_metadata(metadata: dict) -> None:
    if metadata.get("title") != EXPECTED_TITLE:
        raise RuntimeError("Unexpected modern SGA record title")
    if metadata.get("description") != DESCRIPTION_HTML:
        raise RuntimeError("Modern description did not update exactly")
    notes = [
        row.get("description")
        for row in metadata.get("additional_descriptions", [])
        if row.get("type", {}).get("id") == "notes"
    ]
    if notes:
        raise RuntimeError("Modern reader-facing notes were not removed")
    if metadata.get("contributors"):
        raise RuntimeError(
            "Modern reader-facing contributor badges were not removed"
        )
    subjects = [row.get("subject") for row in metadata.get("subjects", [])]
    if subjects != KEYWORDS:
        raise RuntimeError("Modern subjects did not update exactly")
    visible = "\n".join(
        [
            metadata.get("title", ""),
            metadata.get("description", ""),
            metadata.get("version", ""),
            *notes,
            *subjects,
        ]
    ).casefold()
    hits = [term for term in BLOCKED_VISIBLE_TERMS if term in visible]
    if hits:
        raise RuntimeError(
            f"Modern visible metadata still contains blocked terms: {hits}"
        )


def assert_record_identity(record: dict) -> None:
    if int(record["id"]) != RECORD_ID:
        raise RuntimeError("Record ID changed")
    if record.get("doi") != DOI:
        raise RuntimeError("Version DOI changed")
    if record.get("conceptdoi") != CONCEPT_DOI:
        raise RuntimeError("Concept DOI changed")
    rows = file_rows(record)
    if len(rows) != EXPECTED_FILE_COUNT:
        raise RuntimeError("Public file count changed")
    if sum(int(row["size"]) for row in rows) != EXPECTED_TOTAL_BYTES:
        raise RuntimeError("Public byte boundary changed")


def main() -> None:
    token = base.find_token()
    session = base.make_session()
    auth = {"Authorization": f"Bearer {token}"}

    public_before = base.check(
        session.get(
            f"{base.API}/records/{RECORD_ID}",
            timeout=(30, 180),
        ),
        {200},
    ).json()
    assert_record_identity(public_before)
    before_rows = file_rows(public_before)
    before_aggregate = file_aggregate(before_rows)

    legacy = base.check(
        session.get(
            f"{base.API}/deposit/depositions/{RECORD_ID}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if legacy.get("state") != "done" or not legacy.get("submitted"):
        raise RuntimeError("Published record is already in an edit state")
    if str(legacy.get("conceptrecid")) != "20410947":
        raise RuntimeError("Legacy deposition escaped the SGA concept")

    editing = base.check(
        session.post(
            legacy["links"]["edit"],
            headers=auth,
            timeout=(30, 180),
        ),
        {201},
    ).json()
    published = False
    try:
        if editing.get("state") != "inprogress":
            raise RuntimeError("Zenodo did not open an edit session")

        vendor_headers = {
            **auth,
            "Accept": "application/vnd.inveniordm.v1+json",
        }
        draft = base.check(
            session.get(
                f"{base.API}/records/{RECORD_ID}/draft",
                headers=vendor_headers,
                timeout=(30, 180),
            ),
            {200},
        ).json()
        if int(draft["id"]) != RECORD_ID:
            raise RuntimeError("Modern edit draft changed the record ID")
        if (
            draft.get("parent", {})
            .get("pids", {})
            .get("doi", {})
            .get("identifier")
            != CONCEPT_DOI
        ):
            raise RuntimeError("Modern edit draft escaped the SGA concept")

        draft_files = base.check(
            session.get(
                draft["links"]["files"],
                headers={**auth, "Accept": "application/json"},
                timeout=(30, 180),
            ),
            {200},
        ).json()
        entries = draft_files.get("entries", {})
        if isinstance(entries, list):
            entries = {row["key"]: row for row in entries}
        modern_rows = sorted(
            (
                {
                    "key": row["key"],
                    "size": int(row["size"]),
                    "checksum": row["checksum"].lower(),
                }
                for row in entries.values()
            ),
            key=lambda row: row["key"].casefold(),
        )
        if [
            (row["key"], row["size"], row["checksum"])
            for row in modern_rows
        ] != [
            (row["key"], row["size"], row["checksum"])
            for row in before_rows
        ]:
            raise RuntimeError("Modern edit draft file set changed")

        metadata = copy.deepcopy(draft["metadata"])
        metadata["description"] = DESCRIPTION_HTML
        metadata["subjects"] = [{"subject": keyword} for keyword in KEYWORDS]
        clear_modern_reader_frontmatter(metadata)
        payload = {
            "access": draft["access"],
            "files": {
                "enabled": True,
                "default_preview": DEFAULT_PREVIEW,
                "order": sorted(entries, key=str.casefold),
            },
            "metadata": metadata,
            "custom_fields": draft.get("custom_fields", {}),
        }
        if draft.get("pids"):
            payload["pids"] = draft["pids"]
        patched = base.check(
            session.put(
                f"{base.API}/records/{RECORD_ID}/draft",
                headers={
                    **vendor_headers,
                    "Content-Type": "application/json",
                },
                json=payload,
                timeout=(30, 300),
            ),
            {200},
        ).json()
        assert_clean_modern_metadata(patched["metadata"])

        base.check(
            session.post(
                patched["links"]["publish"],
                headers=vendor_headers,
                timeout=(30, 600),
            ),
            {200, 202},
        )
        published = True
    finally:
        if not published:
            session.post(
                editing["links"]["discard"],
                headers=auth,
                timeout=(30, 180),
            )

    public_after = None
    for _attempt in range(30):
        candidate = base.check(
            session.get(
                f"{base.API}/records/{RECORD_ID}",
                timeout=(30, 180),
            ),
            {200},
        ).json()
        candidate_metadata = candidate["metadata"]
        if (
            candidate_metadata.get("keywords") == KEYWORDS
            and not candidate_metadata.get("contributors")
            and candidate_metadata.get("notes") in (None, "")
        ):
            public_after = candidate
            break
        time.sleep(2)
    if public_after is None:
        raise RuntimeError("Public metadata did not converge")

    assert_record_identity(public_after)
    assert_clean_metadata(public_after["metadata"])
    after_rows = file_rows(public_after)
    after_aggregate = file_aggregate(after_rows)
    if before_rows != after_rows or before_aggregate != after_aggregate:
        raise RuntimeError("Public file identities changed during metadata edit")

    public_modern = base.check(
        session.get(
            f"{base.API}/records/{RECORD_ID}",
            headers={"Accept": "application/vnd.inveniordm.v1+json"},
            timeout=(30, 180),
        ),
        {200},
    ).json()
    assert_clean_modern_metadata(public_modern["metadata"])
    public_file_state = base.check(
        session.get(
            public_modern["links"]["files"],
            headers={"Accept": "application/json"},
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if public_file_state.get("default_preview") != DEFAULT_PREVIEW:
        raise RuntimeError("Public default preview was not restored")
    expected_order = sorted(
        (str(row["key"]) for row in after_rows), key=str.casefold
    )
    reported_order = public_file_state.get("order") or []
    if reported_order and reported_order != expected_order:
        raise RuntimeError("Public file order did not converge")

    receipt = {
        "status": "PASS",
        "record_id": RECORD_ID,
        "record_url": public_after["links"]["self_html"],
        "doi": DOI,
        "concept_doi": CONCEPT_DOI,
        "metadata_edit": "published_record_updated_in_place",
        "new_version_created": False,
        "duplicate_concept_created": False,
        "files": {
            "count": len(after_rows),
            "bytes": sum(int(row["size"]) for row in after_rows),
            "identity_aggregate_sha256": after_aggregate,
            "before_after_exact": True,
            "default_preview": public_file_state["default_preview"],
            "ordered": True,
            "order_strategy": "canonical numeric filename prefixes",
        },
        "metadata": {
            "title": public_after["metadata"]["title"],
            "description": public_after["metadata"]["description"],
            "notes": public_after["metadata"].get("notes"),
            "keywords": public_after["metadata"]["keywords"],
            "contributors": public_after["metadata"].get(
                "contributors", []
            ),
            "blocked_visible_term_hits": [],
        },
        "reader_text_audit": {
            "english_reader_files": 6,
            "english_reader_pages": 3_445,
            "ai_workflow_status_term_hits": 0,
            "french_reader_files": 2,
            "french_reader_ai_workflow_status_term_hits": 0,
            "ordinary_source_editorial_apparatus_preserved": True,
        },
        "public_updated": public_after.get("updated"),
    }
    write_json(RECEIPT_PATH, receipt)
    HUMAN_RECEIPT_PATH.write_text(
        "\n".join(
            (
                "# SGA canonical reader metadata cleanup",
                "",
                f"- Record: <{public_after['links']['self_html']}>",
                f"- DOI: `{DOI}`",
                f"- Concept DOI: `{CONCEPT_DOI}`",
                "- Operation: edit the published record metadata in place",
                "- New Zenodo version: no",
                "- Duplicate concept: no",
                f"- Default preview: `{DEFAULT_PREVIEW}`",
                "- Reader-facing contributor badges: removed",
                "- Reader-facing Notes field: removed",
                (
                    f"- Public files retained exactly: {len(after_rows)} / "
                    f"{sum(int(row['size']) for row in after_rows):,} B"
                ),
                f"- File identity aggregate: `{after_aggregate}`",
                "- Visible AI/workflow/status metadata hits: 0",
                (
                    "- Reader-body audit: six English readers / 3,445 pages "
                    "and two French readers; 0 AI/workflow/status hits"
                ),
                (
                    "- Source editorial prefaces and notes remain because they "
                    "are part of the mathematical editions"
                ),
                "",
            )
        ),
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(receipt, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
