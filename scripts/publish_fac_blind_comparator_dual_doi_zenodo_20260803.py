#!/usr/bin/env python3
"""Publish the guarded FAC blind-comparator methodology/replication successors."""

from __future__ import annotations

import publish_all_session_provenance_zenodo_20260802 as guarded


guarded.TARGETS = {
    "methodology": {
        "predecessor_record": 21_764_482,
        "concept_id": 21_124_403,
        "concept_doi": "10.5281/zenodo.21124403",
    },
    "replication": {
        "predecessor_record": 21_764_484,
        "concept_id": 20_461_174,
        "concept_doi": "10.5281/zenodo.20461174",
    },
}
guarded.SAFE_PUBLISH_ORDER = ("methodology", "replication")
guarded.PUBLICATION_DATE = "2026-08-03"


if __name__ == "__main__":
    raise SystemExit(guarded.main())
