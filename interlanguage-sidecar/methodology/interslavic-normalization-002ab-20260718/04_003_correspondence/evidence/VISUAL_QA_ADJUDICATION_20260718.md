# Tranche 003 correspondence: visual QA adjudication

Date: 2026-07-18

Scope: 179 compiled PDFs (89 Latin-script units and 90 Cyrillic-script units), 556 pages total.

## Evidence inspected

- All 556 rendered pages were inspected through the six master sheets listed in `RENDER_QA_REPORT.json`.
- All seven higher-resolution stratified sample sheets were inspected. These include first/middle/last-page samples across the tranche and all six pages of the repaired Paper 35 Cyrillic unit.
- The two context-sensitive replacements were separately rendered at 160 dpi and inspected in both scripts:
  - Paper 09, section 09, page 2: `iz odpovědanja` / `из одповеданьа`.
  - Paper 31, section 07, entry 02, page 1: `pridružene proste idealy` / `придружене просте идеалы`.

No clipping, overlap, black-box glyph failures, missing-glyph substitutions, accidental blank pages, or normalization-induced layout defects were observed.

## Machine-flag adjudication

`RENDER_QA_REPORT.json` correctly preserves one machine flag and therefore has `machine_pass: false`:

- Unit 127, Paper 17 section 12, Cyrillic, page 5; `blank_flag: true`, non-white fraction 0.000834.

The page was separately rendered at 160 dpi and visually inspected. It is an intentional sparse final page containing the centered receipt line `(Prijeto 4 avgusta 1919.)` in Cyrillic plus page number 5. The text is legible and unclipped. This is a threshold false positive, not an empty or defective page.

## Adjudicated result

Human visual review passes the bounded tranche. The underlying machine report is not altered: its flag remains part of the evidence, and this document records the manual disposition.

This result concerns rendered layout and glyph integrity only. It is not a claim of community certification or independent source-faithfulness of the underlying translations.
