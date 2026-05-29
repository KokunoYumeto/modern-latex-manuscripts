# Quality refresh actual-fixed cumulative delta (no source scans)

This is an incremental uploadable delta. It does not claim that the whole corpus is clean or complete.

New or updated this round: 18 PDFs. This includes 15 newly added pass-through/PDF-surface-cleaned readers plus 3 previously cumulative PDFs that were re-cleaned after a cumulative audit found visible XeLaTeX/process footer text.

Cumulative actually-fixed folder: 33 PDFs.

Round-8 reports are carried forward. Round-9 reports are:

- `reports/quality-refresh_new_surface_audit.csv`
- `reports/quality-refresh_cumulative_text_render_audit.csv`
- `reports/quality-refresh_cumulative_actual_fixed_manifest.csv`
- `reports/quality-refresh_new_surface_render_contact_sheet.jpg`

The round-9 audit checks for blank/tiny pages, replacement characters, square glyphs, visible LaTeX/control strings, local paths, HTML/404 text, process labels, and visible XeLaTeX/process footer text.

The round-9 additions are PDF-surface repairs/pass-through verifications, not source-level TeX rebuilds. Source-level TeX repairs from rounds 5-8 are still carried in `cumulative-actually-fixed/patched-tex/`.
