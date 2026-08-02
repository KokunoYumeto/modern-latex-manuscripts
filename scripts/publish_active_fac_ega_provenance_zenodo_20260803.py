#!/usr/bin/env python3
"""Publish the bounded 2026-08-03 FAC/EGA provenance successor safely.

This wrapper narrows the established guarded publisher to the four concepts
whose bytes changed after the v3 provenance publication.  Deligne and SGA7 are
intentionally absent because their complete public provenance objects remain
byte-identical.  The wrapper changes no publishing logic: it only fixes the
allowed existing concepts, exact current predecessor records, publication
date, and safe order before handing control to the guarded implementation.
"""

from __future__ import annotations

import publish_all_session_provenance_zenodo_20260802 as guarded


guarded.TARGETS = {
    "methodology": {
        "predecessor_record": 21_762_751,
        "concept_id": 21_124_403,
        "concept_doi": "10.5281/zenodo.21124403",
    },
    "replication": {
        "predecessor_record": 21_762_799,
        "concept_id": 20_461_174,
        "concept_doi": "10.5281/zenodo.20461174",
    },
    "fac_gaga": {
        "predecessor_record": 21_762_806,
        "concept_id": 21_720_996,
        "concept_doi": "10.5281/zenodo.21720996",
    },
    "ega": {
        "predecessor_record": 21_762_807,
        "concept_id": 20_414_353,
        "concept_doi": "10.5281/zenodo.20414353",
    },
}
guarded.SAFE_PUBLISH_ORDER = (
    "methodology",
    "replication",
    "fac_gaga",
    "ega",
)
guarded.PUBLICATION_DATE = "2026-08-03"


if __name__ == "__main__":
    raise SystemExit(guarded.main())
