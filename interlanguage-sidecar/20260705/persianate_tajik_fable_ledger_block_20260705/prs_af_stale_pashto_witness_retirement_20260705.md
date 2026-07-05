# prs_AF Stale Pashto Witness Retirement

Generated: 2026-07-05

Status: generated-draft/non-canonical; no native review, accepted terminology, source certification, license clearance, gate promotion, final status, or translation completion claim.

## Summary

This artifact corrects a boundary leak left after the Pashto split: six `prs_AF` rows in `forms.csv` still cited `prs_AF/prs_af_ecampus_algebra_momand.pdftotext.txt`, but that body is now reclassified as `ps_AF` Pashto. The correction retires algebra/core term rows to source-acquisition gap status and replaces only the proof-grammar rows that already have independent Kabul University Dari/Persian C2 witnesses.

## Corrections

| Correction | Lexeme | Concept | Action | New source/use |
| --- | --- | --- | --- | --- |
| `PRS-RETIRE-PTR-ALG-0001` | `PTR-ALG-0001` | ring | retired_to_gap | `ps_AF/prs_af_ecampus_algebra_momand.pdftotext.txt`; do-not-use-for-prs_AF |
| `PRS-RETIRE-PTR-ALG-0002` | `PTR-ALG-0002` | field | retired_to_gap | `ps_AF/prs_af_ecampus_algebra_momand.pdftotext.txt`; do-not-use-for-prs_AF |
| `PRS-RETIRE-PTR-ALG-0003` | `PTR-ALG-0003` | ideal | retired_to_gap | `ps_AF/prs_af_ecampus_algebra_momand.pdftotext.txt`; do-not-use-for-prs_AF |
| `PRS-REPLACE-PTR-PRF-0006` | `PTR-PRF-0006` | equation | replaced_with_independent_dari_witness | `prs_AF/prs_af_kabul_university_discrete_mathematics_2023-11.pdftotext.txt`; source-witness-pdf-with-ocr-locator |
| `PRS-REPLACE-PTR-PRF-0007` | `PTR-PRF-0007` | formula | replaced_with_independent_dari_witness | `prs_AF/prs_af_kabul_university_discrete_mathematics_2023-11.pdftotext.txt`; source-witness-pdf-with-ocr-locator |
| `PRS-REPLACE-PTR-PRF-0008` | `PTR-PRF-0008` | relation | replaced_with_independent_dari_witness | `prs_AF/prs_af_kabul_university_discrete_mathematics_2023-11.pdftotext.txt`; source-witness-pdf-with-ocr-locator |

## Boundary

- `ps_AF` Pashto source bodies remain adjacent zero-weight evidence only.
- No Persian/Farsi, Pashto, Tajik, or Urdu evidence authorizes a Dari/Persian Afghanistan row.
- `tg_Cyrl_TJ` entries remain source-discovery/non-promoted.
- This is a generated correction and draft-support ledger, not native review or approval.
