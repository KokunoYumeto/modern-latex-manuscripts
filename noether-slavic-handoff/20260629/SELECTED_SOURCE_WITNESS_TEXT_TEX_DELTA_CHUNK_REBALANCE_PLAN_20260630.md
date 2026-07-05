# Selected Source-Witness Text/TeX Delta Chunk Rebalance Plan - 2026-06-30

Status: `selected_source_witness_text_tex_delta_chunk_rebalance_plan_no_archive_no_network`

This rebalances the concrete delta filelist into upload-sized metadata chunks. It references file IDs from the delta filelist and does not copy file contents, source passages, source-language terms, PDFs, images, archives, credentials, or remote payloads.

## Summary

- Source filelist: 4304 rows / 266380389 bytes / 5 old chunks
- Old max chunk bytes: 203282867; old chunks over soft target: 2
- Rebalanced chunks: 7; max bytes: 49084777; min bytes: 1905301
- Soft-target exceptions: 3 singleton chunks for 3 individual oversized files
- Estimated compressed chunks over 20 MB: 0
- Archives created: 0; uploads/pushes/downloads: 0

## Rebalanced Chunks

| Chunk | Files | Bytes | Est. compressed | Over soft target | Singleton exception | Source chunks |
|---|---:|---:|---:|---|---|---|
| selected-witness-text-tex-delta-rebalanced-01 | 1 | 49084777 | 12414033 | true | true | selected-witness-text-tex-delta-05 |
| selected-witness-text-tex-delta-rebalanced-02 | 1 | 47445879 | 11999539 | true | true | selected-witness-text-tex-delta-05 |
| selected-witness-text-tex-delta-rebalanced-03 | 1 | 42115314 | 10651386 | true | true | selected-witness-text-tex-delta-05 |
| selected-witness-text-tex-delta-rebalanced-04 | 19 | 41943040 | 10607816 | false | false | selected-witness-text-tex-delta-02, selected-witness-text-tex-delta-03, selected-witness-text-tex-delta-04, selected-witness-text-tex-delta-05 |
| selected-witness-text-tex-delta-rebalanced-05 | 155 | 41943040 | 10607816 | false | false | selected-witness-text-tex-delta-02, selected-witness-text-tex-delta-03, selected-witness-text-tex-delta-04, selected-witness-text-tex-delta-05 |
| selected-witness-text-tex-delta-rebalanced-06 | 1459 | 41943038 | 10607816 | false | false | selected-witness-text-tex-delta-01, selected-witness-text-tex-delta-02, selected-witness-text-tex-delta-03, selected-witness-text-tex-delta-04, selected-witness-text-tex-delta-05 |
| selected-witness-text-tex-delta-rebalanced-07 | 2668 | 1905301 | 481870 | false | false | selected-witness-text-tex-delta-01, selected-witness-text-tex-delta-02, selected-witness-text-tex-delta-03, selected-witness-text-tex-delta-04, selected-witness-text-tex-delta-05 |

## Lane Coverage

| Lane/cohort | Files | Bytes | Rebalanced chunks |
|---|---:|---:|---:|
| africa_deep_gap | 420 | 161052751 | 7 |
| arabic | 3 | 1019081 | 2 |
| east_southeast_asia_pacific | 2808 | 12000153 | 4 |
| fa_IR | 10 | 242109 | 2 |
| french | 697 | 44000805 | 4 |
| japanese | 53 | 5298968 | 3 |
| methodology_interlanguage_access | 34 | 27211089 | 4 |
| pan_turkic_adjacent | 2 | 43663 | 1 |
| prs_AF | 162 | 13964965 | 4 |
| simplified_chinese | 53 | 5298968 | 3 |
| source_first_reference_textbooks | 91 | 1153266 | 3 |
| south_asia_hindustani_indic_dravidian | 3 | 47814 | 3 |
| spanish | 697 | 44000805 | 4 |
| tg_Cyrl_TJ | 22 | 557176 | 3 |

## Boundary Notes

- This is a rebalanced plan only; it creates no archive and performs no upload.
- Three individual files exceed the soft uncompressed target, so they are isolated as singleton chunks.
- Every chunk remains under the existing estimated compressed-size cap.
