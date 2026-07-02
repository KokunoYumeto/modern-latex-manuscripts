# Source-core split upload staging plan - 2026-06-30

Status: local staging plan only. No chunk archives were created and no network action was performed.

## Totals

- Source-core files assigned: 7801
- Source-core uncompressed bytes assigned: 302374591
- Planned chunks: 11
- Planned chunks estimated under 20 MB compressed: 11
- Planned chunks estimated over 20 MB compressed: 0
- Uploaded chunks: 0
- Network actions performed: false

## Root Summary

| Root | Chunks | Files | Bytes |
| --- | ---: | ---: | ---: |
| modern_latex_noether_sources | 3 | 289 | 92415553 |
| noether_zenodo_record_pointers | 1 | 1 | 14248 |
| pc_handoff_payload | 1 | 67 | 2612766 |
| slavic_canonical_workspace | 6 | 7444 | 207332024 |

## Planned Chunks

| Chunk | Root | Files | Uncompressed bytes | Estimated compressed bytes | Under 20 MB estimate |
| --- | --- | ---: | ---: | ---: | --- |
| `source-core-01-modern-latex-noether-sources-01` | modern_latex_noether_sources | 109 | 41196603 | 10423130 | `true` |
| `source-core-02-modern-latex-noether-sources-02` | modern_latex_noether_sources | 130 | 41408378 | 10476690 | `true` |
| `source-core-03-modern-latex-noether-sources-03` | modern_latex_noether_sources | 50 | 9810572 | 2485288 | `true` |
| `source-core-04-noether-zenodo-record-pointers-01` | noether_zenodo_record_pointers | 1 | 14248 | 7699 | `true` |
| `source-core-05-pc-handoff-payload-01` | pc_handoff_payload | 67 | 2612766 | 664890 | `true` |
| `source-core-06-slavic-canonical-workspace-01` | slavic_canonical_workspace | 1343 | 41834803 | 10584537 | `true` |
| `source-core-07-slavic-canonical-workspace-02` | slavic_canonical_workspace | 1338 | 40773191 | 10316044 | `true` |
| `source-core-08-slavic-canonical-workspace-03` | slavic_canonical_workspace | 2412 | 41832205 | 10583880 | `true` |
| `source-core-09-slavic-canonical-workspace-04` | slavic_canonical_workspace | 1064 | 40629139 | 10279612 | `true` |
| `source-core-10-slavic-canonical-workspace-05` | slavic_canonical_workspace | 1270 | 41936822 | 10610338 | `true` |
| `source-core-11-slavic-canonical-workspace-06` | slavic_canonical_workspace | 17 | 325864 | 86510 | `true` |

## Boundaries

- This is a staging plan only; it creates no source-core split archives.
- This performs no fetch, push, clone, download, upload, or GitHub API call.
- This assigns files from the existing source-core snapshot by path, size, and hash only.
- This does not copy source-language passages or native-register extraction text.
- This is not a review result and not a completion claim.
