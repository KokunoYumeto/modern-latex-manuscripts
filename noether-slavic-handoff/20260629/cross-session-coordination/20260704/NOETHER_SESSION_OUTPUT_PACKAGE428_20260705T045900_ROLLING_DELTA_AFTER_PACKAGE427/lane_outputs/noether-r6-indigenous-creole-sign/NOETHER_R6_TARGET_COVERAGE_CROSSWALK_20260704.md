# NOETHER R6 Target Coverage Crosswalk

Status: target_coverage_crosswalk_source_canon_only_no_promotion

Generated: 2026-07-04

Lane: Session I / R6 Indigenous, Creole, and Sign Access

Purpose: provide a machine-readable and human-readable crosswalk showing how every current R6 target string is represented across strict witnesses, explicit gaps, candidate routes, non-source guardrails, and non-strict route metadata. This is source-canon coverage hygiene only. It is not translation readiness, source authority, reviewer approval, community consent, license clearance, media clearance, visual inventory readiness, pilot readiness, completion, or Git action.

## Inputs

| Input artifact | Rows | Contribution |
|---|---:|---|
| `NOETHER_R6_SOURCE_CANON_STRICT_PROVENANCE_WITNESS_TABLE_20260704.csv` | 82 | Strict exact-URL provenance witness rows. |
| `NOETHER_R6_SOURCE_CANON_EXPLICIT_GAP_LEDGER_20260704.csv` | 78 | Explicit exact-source, source-archive, GitHub/source-repository, URL/access, and authority blocker rows. |
| `NOETHER_R6_SOURCE_ARCHIVE_CANDIDATE_ROUTE_LEDGER_20260704.csv` | 1 | Candidate GitHub repository metadata route; not a strict witness. |
| `NOETHER_R6_NON_SOURCE_GUARDRAIL_ROWS_20260704.csv` | 10 | International Sign comparator policy/question guardrails; not source witnesses. |
| `NOETHER_R6_NON_STRICT_ROUTE_METADATA_ROWS_20260704.csv` | 1 | DGS placeholder-URL route metadata; not strict exact-URL provenance. |

## Output

| Output artifact | Rows | Use |
|---|---:|---|
| `NOETHER_R6_TARGET_COVERAGE_CROSSWALK_20260704.csv` | 57 | Per-target coverage state with witness, gap, candidate, guardrail, and non-strict route counts plus next gate and authority boundary. |

## Coverage States

| Coverage state | Rows | Meaning |
|---|---:|---|
| `explicit_blocker_only` | 28 | Target appears only in explicit gap/blocker rows. |
| `retry_capture_plus_explicit_blockers` | 9 | Target has a dated retry-capture addendum, but reviewer/source-owner and reuse gates remain explicit blockers before support movement. |
| `route_retry_metadata_blocker` | 5 | Target has dated route-retry metadata, but source-body access is still blocked and no support movement is allowed. |
| `strict_witness_plus_explicit_blockers` | 9 | Target has strict witness metadata and also unresolved explicit blockers. |
| `strict_witness_metadata_only` | 5 | Target has strict witness metadata without separate exact-target gap rows in the current ledger. |
| `candidate_route_only_not_witness` | 1 | Target has a candidate route only; it is not a source-canon witness. |

## Family Counts

| Target family | Crosswalk rows |
|---|---:|
| Creole/contact | 17 |
| Current gap retry | 8 |
| Indigenous Americas | 26 |
| Signed language | 5 |
| Signed language comparator | 1 |

## Special Rows

| Target | Crosswalk state | Boundary |
|---|---|---|
| `Bislama` / `Bislama/Vanuatu` | `retry_capture_plus_explicit_blockers` | Exact official Vanuatu Matematiks/Saens PDF captures are now recorded in the Bislama retry addendum, but reviewer/source-owner and reuse/license gates remain closed before source authority, terms, excerpts, translation, visual inventory, pilot, or package payload use. |
| `Guatemala Uspanteko` / `Uspanteko/Guatemala` | `retry_capture_plus_explicit_blockers` | The DIGEBI source capture addendum records an official product-page download route and exact PDF hash, but source-owner/reviewer and reuse/license gates remain closed before authority, terms, excerpts, translation, visual inventory, pilot, or package payload use. |
| `Quechua/Bolivia` / `Bolivia Quechua` / `Bolivia Quechua longitudes` / `Bolivia Red Minedu repository` | `retry_capture_plus_explicit_blockers` | The Red Minedu capture addendum records exact matching-hash PDF captures from HTTPS and HTTP routes for `19985.pdf`, but source-owner/reviewer and reuse/license gates remain closed before authority, terms, excerpts, OCR reuse, translation, visual inventory, pilot, or package payload use. |
| `Papiamento/Papiamentu - Aruba` | `route_retry_metadata_blocker` for the current-gap retry row | Official EA.AW catalog URLs remain search-visible, but direct source-body access is still blocked by 404 or verification behavior; no PDF source body, source-body hash, authority, clearance, term, translation, or pilot movement is created. |
| `Guarani/Paraguay` / `Paraguay Guarani` / `Paraguay Guarani/Matematica PRODEPA` / `Paraguay MEC CMS` | `route_retry_metadata_blocker` | The Paraguay MEC route retry addendum records a search-visible official MEC page, named PRODEPA/Guarani/Matematica file evidence, and contextual MEC PDF routes, but local page/PDF access timed out; no PDF source body, source-body hash, authority, clearance, term, translation, or pilot movement is created. |
| `Nahuatl / Indigenous-language education candidate` | `candidate_route_only_not_witness` | Candidate GitHub metadata route only. No source-body hash, strict witness, source authority, license clearance, term extraction, translation, or pilot. |
| `DGS` | `strict_witness_plus_explicit_blockers` with 1 non-strict route row | Strict route metadata exists, but one placeholder-URL route remains non-strict and DGS media/API/reviewer gates remain open. |
| `International Sign comparator` | `strict_witness_metadata_only` with 10 non-source guardrails | Comparator/guardrail only. Not authority for ASL, LSQ, DGS, or any local signed language. |

## Gate State

| Gate | Count |
|---|---:|
| Accepted source-authority rows | 0 |
| Reviewer/source-owner approvals | 0 |
| Community-consent claims | 0 |
| License/media clearances | 0 |
| Accepted terms/signs | 0 |
| Selected excerpts | 0 |
| Translation starts | 0 |
| Visual inventories | 0 |
| Pilots | 0 |
| Git pushes from R6 | 0 |

## Next Use

Use the crosswalk before changing any R6 source state:

1. If a target is `explicit_blocker_only`, add exact source evidence or reviewer/source-owner return through a blocker-to-support transition note first.
2. If a target is `retry_capture_plus_explicit_blockers`, use the retry addendum as provenance metadata only and record reviewer/source-owner plus reuse/license decisions before any movement.
3. If a target is `route_retry_metadata_blocker`, use the retry addendum as blocker metadata only and resolve source-body access or source-owner route before any support movement.
4. If a target is `strict_witness_plus_explicit_blockers`, resolve the named blocker without treating the strict witness as blanket authority.
5. If a target is `candidate_route_only_not_witness`, create a separate capture policy before reading or hashing source bodies.
6. If guardrails or non-strict route rows are present, keep them out of strict witness counts until exact URL/path/hash/source-authority criteria are met.

The CSV authority boundary is identical across rows: source-canon coverage state only; no source authority, reviewer approval, community consent, canonical approval, license clearance, media reuse permission, accepted terms/signs, translation, pilot, completion, or Git push.
