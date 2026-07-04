# Noether Romance Source-Canon Access/License URL Refresh

Status: draft / non-canonical / provenance-only / not native reviewed / not approved.

Created: 2026-07-04.

Scope: Romance source-canon maintenance for French and Spanish target-language witness rows. This note records URL, source-archive, and license/access-signal refreshes only. It does not translate corpus prose, approve terms, clear licenses, populate reviewer packets, promote gates, or authorize a Git push from this lane.

Update note: a later same-day sidecar, `NOETHER_ROMANCE_SOURCE_CANON_LICENSE_TERMS_DEEPENING_20260704.md`, narrows several access/license terms after this URL refresh. Use that later note and the regenerated field audit for current weak-row counts.

## Summary

- Base witness table refreshed: `NOETHER_ROMANCE_SOURCE_CANON_WITNESS_TABLE_20260704.csv`.
- Program-required table regenerated: `NOETHER_ROMANCE_SOURCE_CANON_WITNESS_TABLE_REQUIRED_SHAPE_20260704.csv`.
- Field audit regenerated: `NOETHER_ROMANCE_SOURCE_CANON_FIELD_COMPLETENESS_AUDIT_20260704.csv`.
- Machine refresh sidecar created: `NOETHER_ROMANCE_SOURCE_CANON_ACCESS_LICENSE_URL_REFRESH_20260704.csv`.
- Source URL audit now has 21 `ok` rows and 5 true `not_applicable_gap_row` rows; no non-gap witness remains in `missing_gap`.
- License/access audit remains intentionally conservative: 11 `recorded`, 7 `recorded_blank_api_field`, and 8 `weak_or_gap_recorded`.

## Refreshed Evidence Classes

| Class | Rows | Result | Residual limit |
|---|---|---|---|
| arXiv TeX/license href refresh | FR-A-001 through FR-A-006; ES-A-007 | arXiv HTML pages expose TeX source links and license hrefs. License hrefs normalized to either `http://arxiv.org/licenses/nonexclusive-distrib/1.0/` or `http://arxiv.org/licenses/assumed-1991-2003/`; arXiv API license fields were blank in this pass. | Recorded as access/license signal only, not license clearance. |
| French PDF/page fallback refresh | FR-C-007 through FR-C-010 | Stable PDF or bibliographic URLs returned HTTP 200; source URLs populated where previously only live URLs were present. | Mourougane and Marche license not found; Numdam access terms not normalized. |
| Spanish PDF fallback URL refresh | ES-C-008 through ES-C-010 | Stable URLs found or verified for UVaDOC, UBA, and Dialnet fallback witnesses; base table now records live/source URLs. | UVaDOC has explicit openAccess and CC BY-NC-ND 4.0 metadata signal; UBA and Dialnet licenses not found. No TeX/source archive verified for these fallback witnesses. |
| Spanish aggregate gap correction | ES-GAP-003 | Original "Spanish PDF live URL/license gap" narrowed: URL gaps for ES-C-008/009/010 are resolved. | Residual license/source-archive gaps are retained on the individual witness rows. |

## Row-Level Refresh Ledger

| Row | Language | Refreshed signal | Residual gap |
|---|---|---|---|
| FR-A-001 | French | `arXiv HTML license href http://arxiv.org/licenses/nonexclusive-distrib/1.0/; TeX href /src/1712.04728; arXiv API license field blank` | No license-clearance claim; algebra-register witness only. |
| FR-A-002 | French | `arXiv HTML license href http://arxiv.org/licenses/nonexclusive-distrib/1.0/; TeX href /src/0911.2903; arXiv API license field blank` | No license-clearance claim; domain-adjacent cluster-algebra witness. |
| FR-A-003 | French | `arXiv HTML license href http://arxiv.org/licenses/nonexclusive-distrib/1.0/; TeX href /src/1508.04495; arXiv API license field blank` | Does not unblock Noether tensor corpus row without a German anchor. |
| FR-A-004 | French | `arXiv HTML license href http://arxiv.org/licenses/nonexclusive-distrib/1.0/; TeX href /src/2211.16134; arXiv API license field blank` | Functor-category domain; not direct classical invariant-theory source. |
| FR-A-005 | French | `arXiv HTML license href http://arxiv.org/licenses/assumed-1991-2003/; TeX href /src/math/0206203; arXiv API license field blank` | Broad foundational witness only. |
| FR-A-006 | French | `arXiv HTML license href http://arxiv.org/licenses/assumed-1991-2003/; TeX href /src/math/0507070; arXiv API license field blank` | Adjacent algebra source only. |
| ES-A-007 | Spanish | `arXiv HTML license href http://arxiv.org/licenses/nonexclusive-distrib/1.0/; TeX href /src/2207.10005; arXiv API license field blank` | Hilbert-problem register, not Hilbert-basis theorem. |
| FR-C-007 | French | Mourougane PDF URL HTTP 200; source URL populated. | License not found; PDF/text fallback only. |
| FR-C-008 | French | Numdam bibliographic/PDF access HTTP 200; source URL populated. | License/access terms not normalized; PDF fallback only. |
| FR-C-009 | French | Numdam bibliographic/PDF access HTTP 200; source URL populated. | License/access terms not normalized; historical PDF fallback. |
| FR-C-010 | French | Marche GIT course PDF URL HTTP 200; source URL populated. | License not found; PDF fallback only. |
| ES-C-008 | Spanish | UVaDOC handle and PDF URL verified; metadata signal records openAccess and CC BY-NC-ND 4.0 rights URI. | PDF/text fallback; no TeX/source archive verified; no license-clearance claim. |
| ES-C-009 | Spanish | UBA thesis listing and direct PDF URL verified. | License not found; semisimple bridge remains review-sensitive. |
| ES-C-010 | Spanish | Dialnet direct PDF URL verified. | Bibliographic metadata still thin; license not found. |
| ES-GAP-003 | Spanish | Aggregate URL gap narrowed after ES-C-008/009/010 refresh. | Residual license/source-archive gaps remain on individual witness rows. |

## Boundary

This pass is source-canon/provenance maintenance only. It preserves the source-canon-first coordination rule and the B3 packaging boundary: language lanes record local evidence, hashes, URLs, access/license signals, and gaps; they do not push, approve, review, clear rights, or promote gates.
