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
