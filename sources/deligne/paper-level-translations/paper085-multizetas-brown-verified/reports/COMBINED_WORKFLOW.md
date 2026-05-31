# Combined Deligne translation workflow

This is the consolidated working rule set from the user direction and the Codex/restart-packet direction.

## Unit of work

Ship one serious paper/letter unit at a time. Do not send small status-only updates. A return should contain a complete artifact package or a materially advanced cumulative package.

## Fidelity rule

No summaries, no compressed proof sketches, no pseudo-translation, no OCR/verbatim garbage in reader-facing PDFs. The mathematical content must cover the whole source item: title, metadata, sections, numbered statements, formulae, diagrams, bibliography, and any remarks or appendices.

## Bilingual rule

Each unit should have an English layer and a French/source layer. If the original is French, the French/source layer is the source/reference layer and the English layer is the faithful translation. If the original is English, the English/source layer is the source/reference layer and the French layer is the faithful translation.

## Source-grounding rule

Use the current faithful bilingual package as baseline. Items in the rebuild queue remain unpromoted until source-grounding is strict. Papers 084 and 085 specifically require clean source-layer repair before front-facing promotion. Paper 032/Weil II remains a section-by-section rebuild queue item.

## Artifact structure

Every returned package should be a single folder with:

- `pdf/` compiled PDFs;
- `tex/` TeX sources;
- `source_grounding/` source/reference material used for checking;
- `reports/manifest.csv`;
- `reports/FIDELITY_NOTE.md`;
- `reports/SHA256SUMS.txt`.

No screenshots are included as content. Render checks are allowed internally; only text reports are shipped unless render-debug images are explicitly requested.

## Promotion rule

A paper may be marked front-facing only if the package has full TeX/PDF layers, source grounding, clean compilation, and no known skipped sections. Draft or working layers may be included, but must be named as such and not silently promoted.
