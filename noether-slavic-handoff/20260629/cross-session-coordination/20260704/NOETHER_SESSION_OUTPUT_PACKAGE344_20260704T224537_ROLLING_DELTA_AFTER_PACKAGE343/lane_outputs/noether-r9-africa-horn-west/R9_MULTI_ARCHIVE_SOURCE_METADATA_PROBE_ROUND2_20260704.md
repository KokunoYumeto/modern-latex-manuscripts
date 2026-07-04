# R9 Multi-Archive Source Metadata Probe Round 2 - 2026-07-04

This source-canon-first continuation probes public metadata endpoints for unresolved R9 Africa/Horn/West Africa source-package gaps. It covers GitHub repository search, Hugging Face dataset search, Zenodo records, and Internet Archive advanced search for Amharic, Hausa, Somali, Oromo, Tigrinya/Tigrigna, Afar/Qafar, Yoruba, Wolof, Akan/Twi, Fulfulde/Fulani, and Mandinka/Manding query strings.

No source bodies, PDFs, datasets, parquet files, repository archives, or TeX packages were downloaded in this pass. The companion CSV records URL, HTTP status, result count, local metadata path, metadata SHA-256, header metadata path/hash where available, topic/language tags, top metadata summaries, source-gate decision, blocker note, and `promotion_allowed=false` for every row.

## Probe Totals

| measure | count |
|---|---:|
| metadata query rows | 52 |
| candidate-metadata rows | 14 |
| zero-result, error, or explicit-gap rows | 38 |
| local metadata/header files under `work/source_canon_witnesses/20260704_r9_archive_probe_round2/` | 102 |

## Platform Findings

| platform | finding |
|---|---|
| GitHub | Earlier queries in the pass returned explicit zero-result metadata; the last three related-row queries hit unauthenticated API rate limits. No GitHub repository body or archive was captured. |
| Hugging Face | All round-2 queries returned zero-result metadata. The earlier blocked Twi candidate remains recorded in the prior live probe and is not admitted here. |
| Zenodo | All 13 queries returned candidate metadata counts, often very broad and noisy. Top records were mostly language/NLP, education, or unrelated academic records rather than source-level mathematical corpora in the target languages. They require manual filtering before any source-canon use. |
| Internet Archive | One Tigrinya/Tigrigna query returned a CIA Reading Room metadata item unrelated to mathematical source canon; all other round-2 Internet Archive rows were zero-result metadata. |

## Source-Gate Result

No new row is admitted as source-level mathematical corpus evidence. The Zenodo rows are retained as metadata search witnesses only because the result sets are broad and do not by themselves establish target-language mathematical source canon, algebra/invariant-theory relevance, license clearance, or source-body availability. The GitHub rate-limit rows are explicit acquisition blockers to retry later, not evidence of absence.

## Next Acquisition Questions

| row family | next source-canon action |
|---|---|
| Amharic | Retry source-package searches with narrower official repository and exact Amharic-script terms after OCR/font repair remains separately tracked. |
| Hausa | Continue source-owner return for the Amsoshi/app/book route; repeat GitHub/source archive searches after rate-limit window with Hausa-language math terms. |
| Somali/Oromo | Prioritize permission/attribution and proof/register review on the existing Ethiopia Learning shelves; source-package searches remain unclosed. |
| Tigrinya/Tigrigna | Keep the already captured number-verbalization TeX/source-code witnesses separate from algebra/textbook evidence; Internet Archive hit is not usable source canon. |
| Afar/Qafar | Seek transcript or official source-body route; round-2 archive metadata did not close the source-body gap. |
| Related West African rows | Retry GitHub for Akan/Twi, Fulfulde/Fulani, and Mandinka/Manding after API reset; keep glossary, dictionary, packet, and benchmark rows provenance-only until exact source/license/body returns exist. |

Boundary: no translation, accepted term, native/community review, canonical approval, license clearance, gate promotion, completion claim, package upload, or Git push is made.
