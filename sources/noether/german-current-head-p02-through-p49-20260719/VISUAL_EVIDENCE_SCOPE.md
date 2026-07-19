# Visual evidence scope

The visual surface is classified by disposition, including evidence that
cannot be redistributed.

| Control | Rows | Public pixels | Meaning |
| --- | ---: | --- | --- |
| `VISUAL_EVIDENCE_INDEX.jsonl` | 10 | yes | Five current changed pages and five predecessor pages |
| `SOURCE_IMAGE_RIGHTS_BLOCKED.csv` | 33 | no | Eight source pages, 24 enlarged strips, one focused crop |
| `SOURCE_WITNESS_DISPOSITION.csv` | 2 | no | Complete authority witness and bounded source slice |
| `EXCLUDED_VISUAL_EVIDENCE.csv` | 14 | no | Twelve cross-renderer pages and two unhelpful contact sheets |
| `RENDER_REPLAY_VALIDATION.csv` | 5 | n/a | Current producer/rebuild byte-identity controls |

All five current public page images derive from PDF SHA-256
`505A4966299C7292EF272FD54754BF4E5F45B14C72AFA03B487512D4EFED4136`.
The five before images derive from the direct producer predecessor PDF SHA-256
`F94B5EDEEBBA49DEBA6CE52EEF73339F9D8AF16189625E6B8E33754AD3035FE5`.

Full source pages receive a full-frame bounding box. Producer strips and the
focused crop did not retain source-space coordinates, so their records say
`producer_crop_coordinates_not_recorded`. Generation-density statements and
embedded-density metadata are separate fields: the source PNGs carry roughly
72-dpi metadata even though the producer generated native 600-ppi pages and
2x enlarged derivatives.
