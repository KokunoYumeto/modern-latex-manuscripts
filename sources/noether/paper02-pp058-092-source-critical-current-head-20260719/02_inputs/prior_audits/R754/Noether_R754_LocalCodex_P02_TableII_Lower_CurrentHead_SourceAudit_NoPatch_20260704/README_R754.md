# Noether R754 - P02 Table II lower current-head source audit, no patch

Scope: Paper 02, Tabelle I and Tabelle II, with emphasis on Tabelle II lower rows 8-23.

Base: `Noether_R753_local integration lane_CurrentHead_FragilitySmokeAudit_NoPatch_20260704`.

Result: no TeX patch promoted.

Reason: the live R753 table extract is normalized-identical to the validated R646/R736 P02 table branch. The only raw diff against the R736 current extract is the terminal newline at EOF. Existing 1000 dpi Table II source slices were reopened visually for the lower-table danger rows, especially rows 8-23 where previous corrections involved row alignment, dot-H notation, exponent choices, empty row 22, and final KH/aH rows.

Included evidence:

- `1/01_current/cum_de_R754_same_as_R753.tex` and `.pdf`: current cumulative carried unchanged.
- `1/02_table_extracts/R753_P02_tables_live_extract.tex`: live table block from current head.
- `1/02_table_extracts/P02_tables_RA34_validated_reference.tex`: prior validated table branch.
- `1/03_source_witnesses/TableII_RA33_RA34/*.png`: 650/1000 dpi source witnesses for Table II.
- `1/03_source_witnesses/TableI_RA31/*.png`: 650 dpi/zoom witnesses for Table I.
- `1/04_rendered_current/*.png`: current PDF output pages 41-42 rendered at 300 dpi for layout QA.
- `1/05_audit/*.csv`: row-level old correction ledgers and current-head disposition.
- `1/05_audit/P02_tables_R736_current_vs_R753_live.diff`: live-current diff; newline-only.

Boundary: this is not a whole-edition certification. It closes the current-head survival check for the known P02 table/alignment repair branch and provides a reusable anti-regression witness package.
