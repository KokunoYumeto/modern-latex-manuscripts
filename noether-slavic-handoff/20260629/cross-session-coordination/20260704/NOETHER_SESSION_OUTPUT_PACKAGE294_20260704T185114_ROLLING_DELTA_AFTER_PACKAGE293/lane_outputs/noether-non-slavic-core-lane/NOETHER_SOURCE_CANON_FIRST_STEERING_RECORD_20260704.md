# Noether Source-Canon-First Steering Record

Recorded: 2026-07-04T18:39:02+02:00

Thread: Session C / coordinator, `019f2b1a-c368-7072-a0b6-eb61614a7580`

## Controlling Steering

The current controlling task is source canon/provenance first. Translation
progress, package churn, glossary expansion, bridge promotion, and completion
claims are not the objective until each relevant target-language lane has a
findable source-canon witness table.

The broad source-corpus/provenance publication is useful support evidence, but
it is not sufficient for the current question unless it directly points to
target-language mathematical source witnesses for the lane under discussion.

## Required Witness Table Shape

Each language/source lane should produce or update an easy-to-find artifact with
at least these fields:

- `lane`
- `target_language_or_access_target`
- `source_title`
- `source_author_or_owner`
- `topic_tags`
- `evidence_tier`
- `source_type`
- `source_url`
- `local_path`
- `license_or_access_signal`
- `sha256_or_other_hash`
- `source_language`
- `is_target_language_witness`
- `is_source_level_tex_or_archive`
- `is_pdf_docx_or_text_fallback`
- `gap_or_blocker_note`
- `non_claim_boundary`

Preferred evidence tier is source-level TeX/LaTeX/arXiv/e-print/source archive.
Where unavailable, lanes may use PDF/DOCX/text provenance, but must label the
fallback clearly and record exact gaps.

## Current Observed State

- Package frontier at this coordinator observation remains package 293 at
  commit `3817aa670bb149a3bbce254536aa01f3759ba18c`; the safe checkout was
  clean and matched upstream/remote/PR #1 at the last local verification.
- `noether-source-corpus-provenance/20260704/NOETHER_SOURCE_LINK_PROVENANCE_INDEX_20260704T153636`
  exists in the safe checkout and remains source/provenance support, not a
  per-language source-canon answer.
- `noether-slavic-source-canon` was not present in the safe checkout at
  2026-07-04T18:39+02:00. B3 is actively working to build that dedicated
  publication path.
- The Slavic baseline lane received the override and is building a CSV plus
  Markdown witness table instead of continuing package/hash churn.
- Arabic, Romance, CJK, CJK native/source-evidence, Persianate/Tajik, R3, and
  Interlanguage Authority threads already received source-canon-first
  delegations and were active on witness tables at this scan.
- R2 Pan-Turkic, R6 Indigenous/Creole/Sign, R7 Malay/SEA/Pacific, R9
  Africa/Horn/West Africa, and OLP/relation-function support were sent matching
  source-canon-first delegations from this coordinator pass.

## Lane Boundary

Language lanes should not push Git. B3/package steward alone stages, commits,
pushes, and verifies.

No lane should claim native review, community approval, canonical approval,
gate promotion, bridge promotion, or blanket license clearance from a source
witness table. The table makes evidence findable; it does not approve terms.

## Supersession Note

Earlier Session C audits that speak in translation-completion terms remain
historical records. For live work, this steering record supersedes those next
actions: source-canon witness tables are the first deliverable.

## Live Pulse Addendum

Recorded: 2026-07-04T18:47:00+02:00

- B3 pushed a repo-level requirement commit on the remote branch:
  `96f81f4739b633170904054e57dc00b82f8e4344`
  (`Request full language baseline source corpus payloads`).
- The committed file is
  `noether-slavic-handoff/20260629/URGENT_LANGUAGE_BASELINE_SOURCE_CORPUS_REQUIREMENT_20260704.md`.
- The local safe checkout remained behind that remote commit at this pulse and
  also contained untracked package-lane/source-canon work. The coordinator did
  not stage, clean, or push those paths.
- Package 294 was locally materialized as
  `NOETHER_SESSION_OUTPUT_PACKAGE294_20260704T184253_ROLLING_DELTA_AFTER_PACKAGE293`;
  it includes copied source-canon witness artifacts from several lanes. B3
  remains responsible for gating, staging, committing, pushing, and reconciling
  that package.
- The Slavic baseline lane completed first source-canon witness artifacts:
  `NOETHER_SLAVIC_TARGET_LANGUAGE_SOURCE_CANON_WITNESS_TABLE_20260704.csv`
  length `37734`, SHA-256
  `7E7EC54133B8529D09260F8BF557F3470FF7AFCDDC4D79F3D4976C67AA776209`;
  JSON length `53503`, SHA-256
  `39E392EBE4063DBF3CDAC2A53DA99B90B6E310CFA6F69031775B24D6C9411A5A`;
  Markdown length `3925`, SHA-256
  `3B0973F90ED22AC179CBFF8BF687D246E91480D65F403F54B09A510B34D41D3C`.
- The Slavic lane reported 29 rows total: 20 local hashed PDF/text
  mathematical witnesses and 9 candidate/gap/bibliographic rows. This is a
  source-canon witness table, not a native-review or canonical-approval claim.
- A local untracked B3 harvester path exists at
  `noether-slavic-source-canon/20260704/NOETHER_SLAVIC_SOURCE_CANON_ARXIV_20260704T184700Z`;
  at this pulse only the directory shell and `manifests` subdirectory were
  visible to the coordinator while B3 continued the larger run.
