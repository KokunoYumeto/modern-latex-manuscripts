# Visual evidence scope

The public visual surface is split by disposition rather than by file type.

| Control | Rows | Public pixels | Meaning |
| --- | ---: | --- | --- |
| `VISUAL_EVIDENCE_INDEX.jsonl` | 61 | yes | Final target-output pages and contact sheets |
| `SOURCE_IMAGE_RIGHTS_BLOCKED.csv` | 124 | no | Scan-derived source pages, crops, and mixed composites |
| `EXCLUDED_VISUAL_EVIDENCE.csv` | 66 | no | Superseded before-renders and intermediate after-renders |
| `SOURCE_WITNESS_DISPOSITION.csv` | 8 | no | Five source PDFs plus three locator/concordance controls |
| `RENDER_REPLAY_VALIDATION.csv` | 58 | n/a | Final-PDF page-render replay and gap-fill controls |

All 58 public page images derive from the final PDF with SHA-256
`7029E3A8BF3D23600C0BD95BEF291EFA1E4F197582F8B603913A3E81B9F2079C`.
The three contact sheets are navigation aids, not independent authorities.

Full-page source images receive a full-frame bounding box. Producer crops for
which source-space coordinates were not retained state
`producer_crop_coordinates_not_recorded`; no coordinates are invented.
Embedded density metadata is reported as found. Filename-level generation
claims do not silently replace missing or inconsistent embedded metadata.
