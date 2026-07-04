# Noether Romance Source-Canon License/Access Terms Deepening

Status: draft / non-canonical / provenance-only / not native reviewed / not approved.

Created: 2026-07-04.

Scope: source-canon maintenance for selected French and Spanish witness rows that still had vague or weak access/license wording after the prior URL refresh. This note records provenance and access signals only. It does not clear rights, approve terms, translate corpus prose, populate reviewer packets, promote gates, or authorize a Git push from this lane.

Update note: a later same-day sidecar, `NOETHER_ROMANCE_SOURCE_CANON_FRENCH_COURSE_PDF_LICENSE_GAP_DEEPENING_20260704.md`, deepens the remaining French course-PDF rights/license gaps for FR-C-007 and FR-C-010 with text/metadata probes. Use that later note for the current French PDF gap evidence.

Second update note: `NOETHER_ROMANCE_SOURCE_CANON_SPANISH_REPO_LICENSE_GAP_DEEPENING_20260704.md` deepens the Spanish repository license gap for ES-B-002 / ES-GAP-004 with GitHub API output, a full text-like archive scan, classified hit review, and linked teaching-page probes.

## Summary

- Updated base witness table: `NOETHER_ROMANCE_SOURCE_CANON_WITNESS_TABLE_20260704.csv`.
- Regenerated required-shape table: `NOETHER_ROMANCE_SOURCE_CANON_WITNESS_TABLE_REQUIRED_SHAPE_20260704.csv`.
- Regenerated field audit: `NOETHER_ROMANCE_SOURCE_CANON_FIELD_COMPLETENESS_AUDIT_20260704.csv`.
- Created machine sidecar: `NOETHER_ROMANCE_SOURCE_CANON_LICENSE_TERMS_DEEPENING_20260704.csv`.
- License/access audit after this pass: 15 `recorded`, 7 `recorded_blank_api_field`, and 4 `weak_or_gap_recorded`.
- Remaining weak/gap rows are now concentrated in: FR-C-007, FR-C-010, ES-B-002, and ES-GAP-004.

## Evidence Checked

| Row | Evidence source | Result | Residual limit |
|---|---|---|---|
| FR-C-008 | Numdam Brion article page plus Numdam conditions page | Numdam metadata and DOI/page details verified; Numdam conditions say metadata are CC0 and full-text files are individually downloadable for research/educational purpose, but Numdam posting does not transfer authorization. | PDF fallback only; no TeX/source archive; no third-party upload clearance. |
| FR-C-009 | Numdam Perrin article page plus Numdam conditions page | Same Numdam access/metadata terms recorded for the historical Perrin article. | PDF fallback and historical register; no TeX/source archive; no third-party upload clearance. |
| ES-B-002 | GitHub repo page, raw README, GitHub API, local zip archive scan | Public TeX repository confirmed; GitHub API `repo.license` is null and the license endpoint returned 404; local archive has README but no LICENSE/COPYING match; README has no license grant. | Strong source witness but explicit license gap remains. |
| ES-C-009 | UBA thesis page plus direct PDF URL | UBA thesis page says PDF publication on the page requires a completed author authorization form; page footer carries Universidad de Buenos Aires copyright. | PDF/text fallback; no TeX/source archive verified; no license-clearance claim. |
| ES-C-010 | Dialnet article page, direct PDF, and Dialnet legal notice | Dialnet article page verifies Spanish bibliographic metadata and full-text link; legal notice records free access, private/research/educational use, no unauthorized commercial use, no mass automated download, and reserved IP rights. | PDF fallback; no TeX/source archive verified; no license-clearance claim. |
| ES-GAP-004 | GitHub API plus local zip archive scan | Repository license gap deepened and tied to ES-B-002: public TeX source exists, but no explicit license was detected. | Retain as explicit B3/source-canon review gap before reuse beyond provenance. |

## Decisions

- Numdam rows move from vague `license/access terms not normalized` wording to exact Numdam access-terms wording.
- Dialnet row moves from `license not found` to exact Dialnet legal-use wording.
- UBA row moves from `license not found` to an explicit publication-authorization/copyright boundary.
- San Salvador GitHub row remains weak, but the gap is now evidenced by GitHub API response plus local archive scan.
- No row is treated as license-cleared; all rows retain draft/non-canonical/not-native-reviewed/not-approved boundaries.

## Boundary

This pass only improves source-canon/provenance witnesses. It does not change the Romance tensor-product corpus blockers, Spanish semisimple manual-review boundary, or B3-only packaging/push policy.
