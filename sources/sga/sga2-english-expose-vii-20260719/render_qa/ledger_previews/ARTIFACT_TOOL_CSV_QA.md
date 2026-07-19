# Artifact Tool CSV import, inspection, and render QA

All eight substantive package CSV ledgers were imported with `Workbook.fromCSV`, inspected over their complete used ranges with values and formulas included, and rendered as styled PNG previews. Every preview was then inspected at original resolution. No import, inspection, render, clipping, or structural presentation failure was found.

| CSV | Data rows | Columns | Inspected range | Preview SHA-256 |
|---|---:|---:|---|---|
| `AUTHORITY_AND_REVIEW_EVIDENCE.csv` | 7 | 13 | `A1:M8` | `62669C2D87921CEEBC82C1D7B133F3E9866C5B0C1A807EFD4E3C3173A949BC4F` |
| `BUILD_RENDER_EVIDENCE.csv` | 14 | 14 | `A1:N15` | `783027DE99D3B096D57ED856ECCE627FF64D8880FB60430B131C3CB6C0DB344C` |
| `FORMULA_SYMBOL_NOTE_STRUCTURE_COMPARISON.csv` | 14 | 9 | `A1:I15` | `0F3C48878CEF92536608AAA48EE0CF983DBE27A6A009A866D6D4D954B22F9E73` |
| `INDEPENDENT_AUDIT_EVIDENCE.csv` | 12 | 16 | `A1:P13` | `363303853CBECB1572DAF8D3D564FDA1ED558DDC96854A686583D92A6ACC9235` |
| `PUBLIC_COMPONENT_INTEGRATION.csv` | 12 | 15 | `A1:O13` | `AAED943E427C6E130090F1C7A9C61E8BB2CA7258CEE95F54F7CDB1004F8F5553` |
| `PUBLIC_PROJECTION_TRANSFORMS.csv` | 6 | 7 | `A1:G7` | `CC31F734CC58AC797DDA65FE11A9A95B3812AC73F6CD368A1E391D2213403E92` |
| `SOURCE_ALIGNMENT_COVERAGE.csv` | 13 | 10 | `A1:J14` | `9A31B9CE0DB9A3925618A44C55951D1FF3A1C53F8B5CA159CBBA63122372875C` |
| `TERMINOLOGY_NORMALIZATION_ADVERSE_CHOICES.csv` | 14 | 7 | `A1:G15` | `309DD72D0A60DD8FDDAB2BA9C459BF7CAC81DABA026A8A91A50367B898795AFF` |

The machine receipt is `ARTIFACT_TOOL_CSV_QA.json`; the eight adjacent PNG files are the retained previews.

The self-excluding payload manifest is handled after package freeze. It is imported, inspected, rendered, and retained in the independent audit workspace rather than added back into the payload, which avoids a cryptographic self-reference cycle.
