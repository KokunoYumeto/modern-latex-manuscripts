# Noether Slavic Source-Canon GitHub TeX Frontier Recheck - 2026-07-04

Scope: bounded GitHub TeX/source probe for the still-open weak Slavic source-canon blockers. This pass queried `bs`, `hsb`, and `dsb` with topic/language-marker filters and obvious non-math exclusions.

Boundary: source-level TeX frontier evidence only. Open-source license metadata allows local payload capture, but it does not establish official target-language authority, native review, canonical approval, accepted correction, license clearance for reuse, or translation completion.

## Summary

* Run artifact: `C:\Users\memo_\Documents\Codex\2026-07-04\noether-slavic-canonical-baseline\noether-slavic-source-canon\20260704\NOETHER_SLAVIC_SOURCE_CANON_GITHUB_TEX_20260705T0125Z`
* Candidate TeX hits: 24
* Open-license payload files: 4
* Blocked/not-uploaded rows: 23
* GitHub rate-limit blocker rows: 3
* Payload zip SHA256: 5A17C33606A95FD3939BAC50A5E62219CAFDA097E4831AF485E8BF839CF0B8A8

## Per-Language State

| language | candidates | payload_files | blocked_rows | rate_limit_rows | decision | next_action |
|---|---:|---:|---:|---:|---|---|
| Bosnian | 14 | 4 | 10 | 0 | payload_exists_but_not_promoted_pending_authority_review | Do not close Bosnian blocker; review payloads only as South Slavic comparators and continue seeking official PMF textbook fulltext/source. |
| Upper Sorbian | 8 | 0 | 8 | 0 | no_promotable_payload_this_pass | Upper Sorbian hits remain blocked/no payload; continue seeking Domowina/Sorbian Institute booklet or corpus body. |
| Lower Sorbian | 2 | 0 | 5 | 3 | no_promotable_payload_this_pass | Lower Sorbian search hit GitHub rate limit on later terms; retry after rate window or use WITAJ/Domowina/corpus routes. |

## Payload Authority Audit

| repo | path | sha256 | authority_decision |
|---|---|---|---|
| Headary/maturita | cj/sources/spolecenstvo_prstenu.tex | 6B90B0A19350398DBC738EC892997C6D630CC50DEBEA7F2B96D76E2A9E335270 | reject_for_bosnian_authority_czech_literary_text_not_math |
| bornagojsic/dismat2 | zadace/dz09/main.tex | 9725FBB076D17BD47ED4F9A97537692BA62AC935F24F67C52D0AA815187F2ECE | south_slavic_discrete_math_homework_candidate_not_official_bosnian_source |
| iruspro/zapiski-fmf | 01_letnik/alg1/skripta/algebraicne-strukture.tex | 3D07DCDE7E9688AF46C4F24D1A834E0CA77AEB481A2A89FAC65976A8112C050B | slovene_algebra_notes_comparator_not_bosnian_source |
| kkumer/simetrije | 1_grupe.tex | E05A130AA35C085453C59327EE7D73BBE3B24266D31579DB59F57AA3FD2B12A4 | croatian_or_south_slavic_group_theory_comparator_not_bosnian_official_source |

## Promotion Decision

No GitHub TeX hit is promoted into the canonical Slavic witness table from this pass. The Bosnian-tagged payloads are overlapping South Slavic or false-positive source hits, not the official Bosnian PMF textbook source/fulltext. Upper and Lower Sorbian remain content-blocked; Lower Sorbian also has a GitHub rate-limit retry blocker.

## Artifact Hashes

* SUMMARY.json SHA256: 6877A94165841762EEF9FDEA34A1DC508A169538C44359C5C6FF09EFEAC88E16
* GITHUB_TEX_TARGET_LANGUAGE_CANDIDATES.csv SHA256: 73E7B30C4F36769C438E6E83FC9F7027CF7871A159457499EF44373DC9F8BC3A
* GITHUB_TEX_OPEN_LICENSE_PAYLOAD_MANIFEST.csv SHA256: 0CE6AA62C0CCBD2F0CBDEDCBF9F0B270D8A05CE7AE18E0B4B0BDB62BA995F353
* GITHUB_TEX_BLOCKED_OR_NOT_UPLOADED.csv SHA256: A148CDBB3F350781E1992CB181561BB2802D813A485EF64981B0F6FF6BA97D1D
* GITHUB_TEX_PAYLOAD_ZIPS.csv SHA256: 078AA0B3E0B1ED6DFC6E3E3326CFA452CFBEF2344226200071D73EE87D33D462
* ARTIFACT_SHA256SUMS.txt SHA256: 0E0843CFFF41AFF6312C8F97C942C705B35EDDBFC372B3924ED205BCF1ED8A91
