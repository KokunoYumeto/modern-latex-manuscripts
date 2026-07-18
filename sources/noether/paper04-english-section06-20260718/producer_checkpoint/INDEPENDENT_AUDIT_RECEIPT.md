# Independent audit receipt

Result: **FINAL PRE-MANIFEST PASS** with no blockers.

The independently audited tree contained 31 files and 2,211,887 bytes. Its start and end tree digest was identical: `3E659656D122B8B76C1D72867C9432784B34079603CCD754DA3D756F51050C7F`.

## Build, PDF, and render

- The single packaged TeX file was copied alone into a fresh directory and built in three pdfLaTeX passes, all exit code 0.
- Pass 1 had only the expected rerun request; passes 2 and 3 had zero warning, box, undefined-command, fatal, emergency-stop, or rerun diagnostics.
- Packaged and fresh extracted text were byte-identical: 11,991 bytes, SHA-256 `AE7EF7D03CA204FCF8532FE2905C53A93A96A5B8074DBE61A83DC96278765773`.
- Fresh 200-dpi page renders were byte- and pixel-identical to both packaged page renders, with absolute error 0.
- Both pages were visually inspected at original resolution and were clean.
- The PDF has two A4 pages, descriptive metadata, 22/22 embedded subset font rows, no encryption, JavaScript, attachments, forms, additional actions, collection, or unsafe action. Its initial GoTo is safe. Tagged PDF accessibility is not claimed.

## Machine evidence

- Five CSV files: 58 records.
- Three JSON files and four JSONL files: 30 JSONL records.
- Stable evidence IDs: 86; declared references: 25.
- Undefined references, reciprocity errors, parent/child errors, revision errors, duplicate keys, header errors, and formula-injection findings: 0.
- Five local graph artifacts and two excluded-control hash receipts reconciled exactly.
- Validation 001 remains the exact false-PASS historical artifact and is reciprocally marked failed and superseded by validation 002, the repaired PASS.

## Privacy, file safety, and scope

The audit found zero private/user paths, personal-name paths, coordination UUIDs, archive-owner labels, staging labels, or machine evidence IDs in the reader. There are no reparse points, alternate data streams, hidden/system files, logs, build byproducts, archives, executables, German source bodies, inherited-English bodies, scans, or scan-derived source images. PNG structure and trailing-data checks passed.

Scope and cursor are consistent: Section 6 only, R823 lines 4045--4110; line 4111 blank and excluded; cursor line 4112, Section 7; printed pages 137--141 and physical scan pages 20--24. Formula tags (40)--(45), Theorems IV--VI, and all three footnotes are present.

This evidence supports a bounded machine-assisted English working checkpoint only. It does not establish completeness of Paper 4, critical-edition status, mathematical certification, independent human or peer review, accessibility conformance, publication action, or rights clearance.
