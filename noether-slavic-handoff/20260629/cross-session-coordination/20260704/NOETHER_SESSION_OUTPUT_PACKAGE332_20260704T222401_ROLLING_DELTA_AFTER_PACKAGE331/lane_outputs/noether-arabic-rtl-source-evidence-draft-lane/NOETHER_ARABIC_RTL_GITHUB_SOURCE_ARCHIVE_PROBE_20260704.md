# Arabic RTL GitHub / Source-Archive Probe

Date: 2026-07-04

Status: `draft_noncanonical_source_archive_probe_not_native_reviewed_not_approved`

This probe records a focused live search for Arabic mathematical TeX/source-archive evidence relevant to the Noether Arabic lane. It is source-canon/provenance and gap evidence only. It does not translate, approve terminology, claim native review, claim canonical approval, clear licenses, promote gates, populate reviewer packets, or push Git.

## Scope

Targets:

- Arabic TeX/LaTeX/source repositories for algebra, rings, fields, groups, representation theory, homomorphism/isomorphism, Artinian/minimal-condition vocabulary, and invariant theory.
- GitHub code search and repository search first.
- Web fallback restricted to GitHub results when GitHub search became noisy or blocked.

## Results

No new direct Arabic mathematical TeX/LaTeX/source-archive witness was admitted in this pass.

Summary:

- Exact TeX code queries with zero hits:
  - `"جبر خطي" extension:tex`
  - `"نظرية الحلقات" extension:tex`
  - `"نظرية الزمر" extension:tex`
  - `"نظرية التمثيل" extension:tex`
  - `"الحلقات والحقول" extension:tex`
  - `"تشاكل" "حلقة" extension:tex`
  - `"ارتيني" extension:tex OR "أرتيني" extension:tex`
- Repository metadata queries with zero hits:
  - `Arabic LaTeX algebra`
  - `جبر خطي LaTeX`
  - `Arabic math tex`
- False-positive TeX clusters:
  - `"تماثل" "حلقة" extension:tex` returned programming, ML/genomics, school-computing, and blockchain/whitepaper contexts.
  - `"حقل" "جبر" extension:tex` returned broad noisy hits, including programming, i18n/performance corpus, religious text, agriculture docs, and non-Arabic/Persian material.
- Invariant-theory exact TeX query:
  - `"نظرية الثوابت" extension:tex` hit a GitHub HTTP 403 rate-limit/access response in this pass.
  - A public-web fallback with `site:github.com "نظرية الثوابت" "tex"` returned GitHub false positives, not target Arabic mathematical source packages.

## GitHub Rate / Access Context

`gh api rate_limit` after the probes reported:

- core remaining: 4998
- search remaining: 27
- code_search remaining: 10

Despite that snapshot, one `gh search code` request for the exact invariant-theory phrase returned HTTP 403 with a GitHub API rate-limit/access message. The correct lane action is to record the blocker and rerun bounded exact searches later or through B3's search-budget workflow, not to scrape.

## Artifact

Machine-readable probe rows:

`NOETHER_ARABIC_RTL_GITHUB_SOURCE_ARCHIVE_PROBE_20260704.csv`

Rows: 15.

## Current Gap Impact

This pass strengthens the existing gap rows:

- Direct Arabic TeX/LaTeX/arXiv/source archive support for treated algebra/invariant-theory topics remains not found.
- Direct Arabic specialist invariant-theory/covariant/binary-form source support remains not found.
- Artinian/minimal-condition Arabic TeX/source evidence remains not found.
- Ring homomorphism/isomorphism Arabic TeX/source evidence remains not found.

The existing PDF/HTML/raw-wikitext provenance rows remain useful fallback evidence, but they are not source-level TeX/LaTeX mathematical corpora and do not approve Arabic terminology.

## Boundary

No source body was copied into this lane. Only search metadata, candidate URLs, classifications, and gap/blocker notes are recorded. No native review, canonical approval, accepted terminology, license clearance, gate promotion, translation completion, reviewer packet population, or Git push is claimed.
