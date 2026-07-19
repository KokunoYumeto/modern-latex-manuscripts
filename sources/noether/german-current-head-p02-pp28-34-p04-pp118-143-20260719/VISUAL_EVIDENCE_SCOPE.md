# Visual evidence scope

The visual surface is classified by disposition, not silently reduced to the
files that are easiest to publish.

| Control | Rows | Public pixels | Meaning |
| --- | ---: | --- | --- |
| VISUAL_EVIDENCE_INDEX.jsonl | 17 | yes | Sixteen final target pages plus one contact sheet |
| SOURCE_IMAGE_RIGHTS_BLOCKED.csv | 193 | no | Scan-derived pages, strips, and mixed composites |
| SOURCE_WITNESS_DISPOSITION.csv | 4 | no | Source PDFs and the external Paper 2 authority |
| EXCLUDED_VISUAL_EVIDENCE.csv | 3 | no | Superseded or duplicate target renders |
| RENDER_REPLAY_VALIDATION.csv | 16 | n/a | Fresh producer/rebuild page-render controls |

All 16 public page images derive from the final PDF with SHA-256
572CF1EAA7F4895D0DA3644AE872D228AE40F6BCD81EC87DC3DEE1ADC9183C92.
The contact sheet is a navigation aid, not an independent authority.

Full source pages receive a full-frame bounding box. Producer crops whose
source-space coordinates were not retained say
producer_crop_coordinates_not_recorded; no bounding boxes are invented.
Generation-density statements and embedded-density metadata are separate
fields so filename claims do not overwrite absent or inconsistent metadata.
