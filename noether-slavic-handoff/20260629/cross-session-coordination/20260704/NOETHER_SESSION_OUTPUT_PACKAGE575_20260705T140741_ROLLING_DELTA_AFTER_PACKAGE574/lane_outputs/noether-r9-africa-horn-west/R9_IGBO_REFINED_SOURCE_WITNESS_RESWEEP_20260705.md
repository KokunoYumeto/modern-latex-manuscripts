# R9 Igbo Refined Source-Witness Resweep

Generated: 2026-07-05T12:07:32.709796+00:00 UTC

## Boundary

This artifact is a metadata-only refined resweep for Igbo mathematical source witnesses. It queries source/archive platforms with English and Igbo/endonym strings, saves response/header JSON with hashes, and records candidate/gap decisions. It does not download source bodies, repository archives, PDFs, datasets, or source text; it does not translate, approve terms, claim native/community review, clear licenses, promote gates, package, stage, commit, or push.

## Summary

- Queries: 6
- Platforms per query: 5
- Total rows: 30
- Nonzero metadata rows: 10
- Rows with `body_saved=false`: 30
- Rows with `source_text_saved=false`: 30
- Rows with `promotion_allowed=false`: 30

## Counts By Platform

| platform | count |
|---|---:|
| GitHub repository search API | 6 |
| Hugging Face dataset search API | 6 |
| Internet Archive advancedsearch API | 6 |
| Open Library search API | 6 |
| Zenodo records API | 6 |

## Counts By Query

| query | count |
|---|---:|
| akwukwo mgbako na mwepu | 5 |
| akwụkwọ mgbakọ na mwepụ | 5 |
| igbo mathematics | 5 |
| igbo mathematics textbook | 5 |
| mgbako na mwepu | 5 |
| mgbakọ na mwepụ | 5 |

## Counts By Candidate Signal

| candidate signal | count |
|---|---:|
| nonzero_metadata_likely_noise_requires_triage | 10 |
| zero_result_no_candidate | 20 |

## Counts By Decision

| source gate decision | count |
|---|---:|
| metadata_noise_not_admitted | 10 |
| query_error_not_admitted | 5 |
| zero_result_gap_not_admitted | 15 |

## Nonzero Metadata Rows

| query | platform | count | signal | summary |
|---|---|---:|---|---|
| igbo mathematics | Open Library search API | 1 | nonzero_metadata_likely_noise_requires_triage | The Igbo ancient traditional number system and an Igbo new decimal number system / language=eng / ia= / access=no_ebook / fulltext=False |
| igbo mathematics | Internet Archive advancedsearch API | 8 | nonzero_metadata_likely_noise_requires_triage | VOA_Global_English_20190422_230000 / title=VOA [Voice of America] Global English : April 22, 2019 07:00PM-08:00PM EDT / language=eng / mediatype=audio / rights=None; VOA_Global_English_20190422_120000 / title=VOA [Voi... |
| igbo mathematics | GitHub repository search API | 138 | nonzero_metadata_likely_noise_requires_triage | cambridgetcg/youspeak / lang=Python / license=None / url=https://github.com/cambridgetcg/youspeak; HarperKollins/AfriLearn / lang=Go / license=None / url=https://github.com/HarperKollins/AfriLearn; nirholas/cryptocurr... |
| igbo mathematics | Zenodo records API | 49860 | nonzero_metadata_likely_noise_requires_triage | 21205148 / title=Collatz-Thwaites-Ulam-Hasse-Syracuse-Kakutani (CTUHSK) Theorem : Convergence of Collatz (3n+1) Sequence to the Trivial Cycle Proved / type=Other / access=None; 21205032 / title=The Morato de Dalmases ... |
| igbo mathematics textbook | Internet Archive advancedsearch API | 1 | nonzero_metadata_likely_noise_requires_triage | bridging-world-history / title=Bridging World History (Alternate) ★ "Lost" Annenberg Series with Course Materials / language=eng / mediatype=movies / rights=Fair Use Notice |
| igbo mathematics textbook | Zenodo records API | 57619 | nonzero_metadata_likely_noise_requires_triage | 21205148 / title=Collatz-Thwaites-Ulam-Hasse-Syracuse-Kakutani (CTUHSK) Theorem : Convergence of Collatz (3n+1) Sequence to the Trivial Cycle Proved / type=Other / access=None; 21205032 / title=The Morato de Dalmases ... |
| mgbako na mwepu | Zenodo records API | 746378 | nonzero_metadata_likely_noise_requires_triage | 21204996 / title=UNIVERSO ASSIMETRICAMENTE SIMÉTRICO, E10 CÍCLICO E DISCIPLINA MODAL DA TEORIA DA OBJETIVIDADE: uma análise crítico-propositiva do artigo de Prithvidev Kamboj em diálogo com a Teoria da Objetividade / ... |
| mgbakọ na mwepụ | Zenodo records API | 746377 | nonzero_metadata_likely_noise_requires_triage | 21204996 / title=UNIVERSO ASSIMETRICAMENTE SIMÉTRICO, E10 CÍCLICO E DISCIPLINA MODAL DA TEORIA DA OBJETIVIDADE: uma análise crítico-propositiva do artigo de Prithvidev Kamboj em diálogo com a Teoria da Objetividade / ... |
| akwukwo mgbako na mwepu | Zenodo records API | 746378 | nonzero_metadata_likely_noise_requires_triage | 21204996 / title=UNIVERSO ASSIMETRICAMENTE SIMÉTRICO, E10 CÍCLICO E DISCIPLINA MODAL DA TEORIA DA OBJETIVIDADE: uma análise crítico-propositiva do artigo de Prithvidev Kamboj em diálogo com a Teoria da Objetividade / ... |
| akwụkwọ mgbakọ na mwepụ | Zenodo records API | 746377 | nonzero_metadata_likely_noise_requires_triage | 21204996 / title=UNIVERSO ASSIMETRICAMENTE SIMÉTRICO, E10 CÍCLICO E DISCIPLINA MODAL DA TEORIA DA OBJETIVIDADE: uma análise crítico-propositiva do artigo de Prithvidev Kamboj em diálogo com a Teoria da Objetividade / ... |

## Source-Gate Reading

The resweep either returns explicit zero-result gaps or nonzero metadata that still lacks exact target-language mathematical source-body evidence. Any nonzero row must be manually triaged for body availability, language/domain fit, URL/hash provenance, license/access signal, and source-owner or reviewer gates before any source-canon use.

CSV: `C:\Users\memo_\Documents\Codex\2026-07-04\noether-r9-africa-horn-west\outputs\R9_IGBO_REFINED_SOURCE_WITNESS_RESWEEP_20260705.csv`
