# Arabic RTL Codepoint and Interlinear Pretranslation Ledger

Status: generated-draft / non-canonical / Arabic-only QA and pretranslation support. Not native reviewed.

## Files

- `ARABIC_RTL_CODEPOINT_EXTRACTION_LEDGER_20260705.csv`: codepoint, script, TeX/formula, and extraction-risk rows for source forms, normalized forms, and formula-neighboring notes in `forms.csv`.
- `ARABIC_SIX_ROW_INTERLINEAR_PRETRANSLATION_SCAFFOLD_20260705.csv`: six-row German-to-Arabic pretranslation scaffolds grounded in existing source-use labels and branch weights.
- `ARABIC_SIX_ROW_INTERLINEAR_PRETRANSLATION_SCAFFOLD_20260705.jsonl`: JSONL mirror for downstream tooling.
- `MANIFEST.csv` and `SHA256SUMS.txt`: local artifact manifest and checksum ledger.

## Boundary

- Arabic evidence in this ledger does not cover Persian, Persianate, Dari, Tajik, Urdu, Ottoman, or Turkic rows.
- OCR and extraction witnesses remain separate from native source bodies and generated drafts.
- Rows with Arabic plus Latin/TeX/math neighbors are marked `rtl-ltr-formula-boundary-risk` until rendered in final page context.
- No native review, accepted terminology, approval, license clearance, source certification, gate promotion, final status, or translation-completion claim is made.
