# NOETHER R6 Public Source-Archive Discovery Audit

Status: public_source_archive_discovery_metadata_only_no_witness_promotion

Generated: 2026-07-04

Lane: Session I / R6 Indigenous, Creole, and Sign Access

Purpose: add concrete public discovery evidence behind the R6 GitHub/e-print/source-archive gap rows. This slice checks bounded public metadata surfaces only. It does not download source archives, clone repositories, copy source bodies, inspect private content, create translation output, promote terms/signs, create visual inventories, create pilots, claim review/approval/clearance, or push Git.

## Outputs

| Artifact | Rows | Use |
|---|---:|---|
| `NOETHER_R6_PUBLIC_SOURCE_ARCHIVE_DISCOVERY_AUDIT_20260704.csv` | 17 | Public metadata probe ledger for GitHub repository search, arXiv API search, and CTAN search-page routes. |
| `NOETHER_R6_SOURCE_ARCHIVE_CANDIDATE_ROUTE_LEDGER_20260704.csv` | 1 | Candidate repository route split out for future manual review; not a strict witness. |

## Probe Surfaces

| Surface | Probe rows | Result |
|---|---:|---|
| GitHub repository search | 11 | Ten queries returned zero repository hits. One query returned a candidate repository metadata route requiring manual target-language math-source review. |
| arXiv API search | 3 | Metadata hits were returned, but they are not validated as target-language mathematical source archives. They are mainly NLP/sign-language or false-positive phrase hits and remain candidate/blocker evidence only. |
| CTAN search page | 3 | Search pages were reachable, but no R6 mathematical source package was validated from the search metadata. |

## Classification Counts

| Classification | Rows |
|---|---:|
| `no_repository_hits_returned_for_query` | 10 |
| `candidate_eprint_hits_require_target_language_not_about_language_review` | 3 |
| `ctan_search_surface_checked_no_validated_r6_math_source_package_from_search_metadata` | 3 |
| `candidate_repository_metadata_route_not_strict_witness_source_body_review_required` | 1 |

## Candidate Route

| Candidate | URL | Signal | Status |
|---|---|---|---|
| `R6-SRC-CAND-GH-001` | `https://github.com/mexicanisimo/Tutoaula` | GitHub metadata describes an educational platform offering third-grade primary courses including mathematics in Spanish and Nahuatl; repository license signal is MIT; default branch commit is `b8431a83bd843320228e8b8b8aeb16f203c31a8b`. | Candidate repository route only. Not a strict source-canon witness because no source body was cloned or hashed, no target-language mathematical content was inspected, and no source-owner/reviewer route has returned. |

This candidate narrows `R6-GITHUB-GAP-001` but does not close it. It also does not change `R6-SRCARCH-GAP-001`, because the current evidence is repository metadata only, not a validated native mathematical TeX/LaTeX/arXiv/e-print/source archive witness.

## Non-Claim Boundary

The public discovery CSV records search metadata, URLs, visible repository/license signals, and candidate/blocker classifications. It does not record source authority, reviewer approval, community consent, canonical approval, license clearance, media reuse permission, accepted terminology, accepted signs, excerpt selection, translation starts, visual inventory readiness, pilot readiness, completion, Git staging, commit, or push.

## Next Gates

1. If `mexicanisimo/Tutoaula` is pursued, create a separate repository-inspection capture policy before reading or copying source bodies.
2. Record file-level hashes, source-body license scope, language evidence, mathematical topic evidence, and package payload boundaries before any movement into a strict witness table.
3. Keep arXiv hits out of R6 witness tables unless a later pass proves target-language mathematical source content rather than papers about languages, NLP datasets, or sign-language processing.
4. Keep CTAN search-page rows as discovery metadata only unless a specific R6 target-language mathematical package is identified with package URL, license/access signal, hashable source path, and relevance notes.
