# Targeted layout repair repair delta

Scope: small, uploadable replacement delta. This package is not a full corpus replacement.

## New/updated replacement PDFs in this round

- 10-12 English Translation - al-Khwarizmi - Algebra.pdf
- 60-02 Islamic Original - al-Khwarizmi - Algebra.pdf
- 10-14 English Translation - Robert of Chester and Karpinski.pdf
- 10-16 English Translation - Rosen - Algebra of Mohammed Ben Musa.pdf
- 70-05 Reference Text - Smith-Karpinski - Numerals.pdf

## What was repaired

- `10-12 English Translation - al-Khwarizmi - Algebra.pdf`: reworked the cramped bilingual layout into stacked Arabic/English blocks and rewrote the displayed equation chains so the formula rows no longer run off the page. The compile log now has 0 Overfull hbox and 0 Overfull vbox warnings.
- `60-02 Islamic Original - al-Khwarizmi - Algebra.pdf`: stacked the three boxed example formula rows in the simple cases; compile log has 0 Overfull hbox and 0 Overfull vbox warnings.
- `10-14 English Translation - Robert of Chester and Karpinski.pdf`: wrapped oversized chapter headings, softened line breaking, and re-pruned non-reader spacer/title-only pages after rebuilding; compile log has 0 Overfull hbox and 0 Overfull vbox warnings.
- `10-16 English Translation - Rosen - Algebra of Mohammed Ben Musa.pdf`: fixed the overfull preface paragraph caused by nonbreaking bibliographic spacing and removed the spacer page after rebuild; compile log has 0 Overfull hbox and 0 Overfull vbox warnings.
- `70-05 Reference Text - Smith-Karpinski - Numerals.pdf`: wrapped the Boethius section heading and relaxed line breaking; compile log has 0 Overfull hbox and 0 Overfull vbox warnings.

## Cumulative folder

`cumulative-actually-fixed/replacement-pdfs/` contains the 10 files currently carried forward as the uploadable fixed set:
the five round-5 files, the five round-6 files, and the current replacements overwriting the affected ones.

## Audit notes

See:

- `reports/targeted_layout_repair_compile_layout_audit.csv`
- `reports/targeted_layout_repair_cumulative_actual_fixed_manifest.csv`
- `reports/targeted_layout_repair_render_blank_page_audit.json`
- `reports/render-samples/targeted_layout_repair_render_contact_sheet.jpg`

The targeted layout repair replacement PDFs have no hits for the text sweep terms: replacement character, white/black square glyph, `title=`, `tcb@`, `sectioncolor`, `commentarycolor`, local `/mnt/` paths, Windows `C:\` paths, internal tool labels, HTML/404/nginx text, or visible `Overfull` strings.

## Not fixed here

This delta does not rebuild combined readers. It does not claim the whole non-European corpus is clean. The Arabic translation file `30-05 Arabic Translation - al-Khwarizmi - Algebra.pdf`, the Omar Arabic translation, Ruska, and the combined readers remain held pending separate repair.
