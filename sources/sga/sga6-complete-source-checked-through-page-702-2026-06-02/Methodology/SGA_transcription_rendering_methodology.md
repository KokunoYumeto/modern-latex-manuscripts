# SGA transcription and rendering methodology

This cumulative methodlog is included to let future local machines and model instances reproduce the SGA rebuild efficiently.

## Source-first rule

The original SGA scan is the controlling source. Existing English drafts or OCR are only alignment aids. Each delivery includes the exact source-scan slice used for the new pages.

## Rebuild loop

1. Extract exact source pages from the original scan.
2. Render the source pages to PNG/contact sheets and inspect for formulas, diagrams, page breaks, and marginal notes.
3. Reconstruct French and translate English in TeX, preserving mathematical numbering, displayed formulas, exact sequences, diagrams, and bibliographies.
4. Compile new-only and cumulative reader PDFs with two LaTeX passes.
5. Render reader PDFs and source slices for visual checks.
6. Audit for process chatter, placeholders, local paths, missing diagram notes, and LaTeX warnings.
7. Package TeX, PDFs, source scans, render checks, logs, manifests, checksums, and this methodlog.

## Diagram discipline

All visibly diagrammatic source elements are audited. Mathematical diagrams are rendered in `tikz-cd` or as faithful displayed exact sequences; they are not replaced by prose summaries.

## Batch 095 addition

For Exposé XIV, pages 670--692, the workflow used the original SGA 6 scan as the controlling source, rendered the full range to page images and contact sheets, compared the legacy English draft against the French scan, and retained the displayed diagrams (4.1), (6.3), and (6.4) as explicit `tikzcd` diagrams in both reader languages.  The next source block is the terminal indices beginning at source page 693.


## Final index-specific note

Terminological and notation indexes should be handled as table-faithfulness tasks. Render source pages, preserve every row and reference column, translate terminology in the English reader, keep mathematical notation unchanged, and search the already typeset body before normalizing ambiguous notation. For SGA 6 this resolved entries including `x_N`, `\varphi^a`, `\mathcal C_0`, `\parfamp`, `\toramp`, `\Qcoh`, `\Pic^\tau`, and algebraic/numerical variants of `K` and `Gr`.


## Batch 096 index-specific note

Terminological and notation indexes are not OCR-forward documents. The safe path is to render source pages, build typographic tables, preserve reference columns, translate only terminological labels in the English reader, retain mathematical notation unchanged, and re-render/audit table breaks and math glyphs.
