# Machine-readable ledger schema

Encoding is UTF-8. CSV files use a header row, comma delimiters, and LF line endings. JSONL files contain one JSON object per nonblank line. SHA-256 values are uppercase hexadecimal; where a row intentionally summarizes multiple evidence objects, semicolon-separated hashes are explicitly labeled by the row method.

## Cumulative ledgers

- `SOURCE_ALIGNMENT_COVERAGE.csv`: twelve component rows plus the closing boundary control.
- `FORMULA_SYMBOL_NOTE_STRUCTURE_COMPARISON.csv`: selected formula, symbol, source-note, and structure controls spanning the assembly.
- `TERMINOLOGY_NORMALIZATION_ADVERSE_CHOICES.csv`: stable terminology and transparent editorial choices.
- `AUTHORITY_AND_REVIEW_EVIDENCE.csv`: authority order, comparison role, bounded-unit review evidence, and revision-linked state evidence.
- `PUBLIC_COMPONENT_INTEGRATION.csv`: public component scope, coordinate, normalized-body, and integration controls without private unit locators.
- `PUBLIC_PROJECTION_TRANSFORMS.csv`: exactly six apparatus-only privacy/terminology transforms; no mathematical-body transform.
- `BUILD_RENDER_EVIDENCE.csv`: fourteen current TeX/PDF, structural, render, integration, audit, and publication-state rows.
- `INDEPENDENT_AUDIT_EVIDENCE.csv`: twelve independent source, mathematics, integration, build, render, machine, and hygiene audit rows with stable identifiers and supersession links.
- `STRUCTURAL_INDEX.jsonl`: historical candidate root revision, twelve component records, and audited root revision 2.
- `DIFFICULTY_REVISION_LEDGER.jsonl`: nine cumulative decision events, including independent-audit closure and the still-open archive-owner decision.
- `MACHINE_READABLE_VALIDATION.json`: ledger rectangularity, identifier, formula-safety, JSONL, integration, build, privacy, and revision/reference-closure results.
- `INDEPENDENT_AUDIT_VALIDATION.json`: privacy-safe exact audit summary and current principal artifact hashes.

## Evidence previews

Every substantive CSV ledger is imported, inspected, and rendered with Artifact Tool. Preview PNGs and the retained receipt are under `render_qa/ledger_previews`. The self-excluding payload manifest is imported and rendered only after payload freeze; its preview and receipt are retained in the independent audit workspace rather than placed inside the payload, avoiding a cryptographic self-reference cycle.

## Validation rules

1. Every substantive ledger CSV has a nonempty header, rectangular rows, and unique values in its first column.
2. No CSV cell begins with `=`, `+`, `-`, or `@` after leading whitespace.
3. Every JSONL line parses as exactly one JSON object with a stable identifier and revision.
4. Structural parent/child, supersession, event-supersession, and continuation-cursor references close.
5. There are exactly twelve component integration rows and all twelve component markers occur once in order.
6. The six public-projection transform rows reconstruct the sanitized apparatus and change no theorem/proof/mathematical body.
7. All recorded file hashes and byte counts match current payload files.
8. The public payload contains no private absolute path or URI-style local locator.
9. Local compile transcripts, auxiliary files, and source rasters are excluded.
10. Publication authorization and archival deposit remain false until the archive owner records a separate decision.
11. `ZENODO_PAYLOAD_MANIFEST.csv` lists every payload file except itself and is validated post-freeze outside the self-indexed payload.
