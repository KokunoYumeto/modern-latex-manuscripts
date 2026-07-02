# Selected Source-Witness Text/TeX Delta Deduped Upload-Candidate Plan - 2026-06-30

Status: `selected_source_witness_text_tex_delta_deduped_upload_candidate_plan_no_archive_no_network`

This separates new-content delta rows from path-alias metadata rows already represented by content hash in the source-core snapshot. It is metadata-only and creates no archive or remote upload.

## Summary

- Source filelist: 4304 rows / 266380389 bytes
- Upload candidates: 792 rows / 218182499 bytes
- Path aliases retained as metadata: 3512 rows / 48197890 bytes
- Deduped chunks: 5; chunks over estimated compressed cap: 0
- Singleton soft-target exceptions: 3
- Archives created: 0; uploads/pushes/downloads: 0

## Deduped Chunks

| Chunk | Upload rows | Bytes | Est. compressed | Over soft target | Singleton exception |
|---|---:|---:|---:|---|---|
| selected-witness-text-tex-delta-deduped-01 | 1 | 49084777 | 12414033 | true | true |
| selected-witness-text-tex-delta-deduped-02 | 1 | 47445879 | 11999539 | true | true |
| selected-witness-text-tex-delta-deduped-03 | 1 | 42115314 | 10651386 | true | true |
| selected-witness-text-tex-delta-deduped-04 | 15 | 41943032 | 10607814 | false | false |
| selected-witness-text-tex-delta-deduped-05 | 774 | 37593497 | 9507773 | false | false |

## Upload-Candidate Extensions

| Extension | Rows | Bytes |
|---|---:|---:|
| .bib | 3 | 91268934 |
| .json | 17 | 48011481 |
| .ltx | 18 | 230504 |
| .md | 2 | 4830 |
| .sty | 1 | 27558 |
| .tex | 4 | 98400 |
| .txt | 559 | 38155162 |
| .xml | 188 | 40385630 |

## Alias Metadata Extensions

| Extension | Rows | Bytes |
|---|---:|---:|
| .bib | 30 | 945519 |
| .cls | 57 | 2013727 |
| .json | 19 | 789493 |
| .md | 31 | 159215 |
| .sty | 248 | 3170773 |
| .tex | 3082 | 38944451 |
| .txt | 45 | 2174712 |

## Boundary Notes

- Upload candidates are new-content hash rows only.
- Path aliases are retained as metadata and point back to the delta filelist.
- This plan creates no archive and performs no network action.
