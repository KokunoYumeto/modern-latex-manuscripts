# Independent audit receipt

Result: **FINAL PRE-MANIFEST PASS** with no blockers.

## Build, PDF, and render

- The packaged TeX was copied alone into a fresh directory and built in three pdfLaTeX passes, all exit code 0.
- Pass 1 had only the expected outline rerun request; passes 2 and 3 had zero warning, box, undefined-command, fatal, emergency-stop, or rerun diagnostics.
- Packaged and fresh extracted text were byte-identical: 16745 bytes, SHA-256 DB26F14773E5D452F31A34F05C28A1032558F55E6DC95D59D04F3FFD68D5BF13.
- Fresh 200-dpi page renders were byte- and pixel-identical to all three packaged page renders; absolute error 0.
- All three pages and the contact sheet were visually inspected and were clean.
- The PDF has three A4 pages, descriptive metadata, 22/22 embedded subset font rows, no encryption, JavaScript, embedded files, forms, collection, page additional actions, or unsafe action. The initial GoTo and eight footnote GoTo links are safe. Tagged PDF accessibility is not claimed.

## Source and machine evidence

- Latest source-alignment revisions cover 157/157 lines with no gap or overlap.
- All formulas (46)--(61), nine unnumbered displays, four original notes, four public source-defect notes, both defining properties, and Theorem VII are accounted for.
- Five source defects were rechecked against the print and disclosed. Formula (46), formula (48), and the post-(56) dummy-index judgments remain explicit.
- Five CSV ledgers contain 91 record revisions; four JSONL ledgers contain 88 revisions; 148 stable public IDs and 49 declared latest references close with zero error.

## Privacy, safety, and scope

No private paths, personal-name paths, task/thread/decision identifiers, raw logs, source bodies, scans, scan-derived source imagery, inherited-English bodies, archives, executables, reparse points, alternate data streams, or unsafe embedded payloads are included. Scope and cursor are consistent: Section 7 only, R823 lines 4112--4268; line 4269 blank and excluded; cursor line 4270, Section 8.

This evidence supports a bounded machine-assisted English working checkpoint only. It does not establish completeness of Paper 4, critical-edition status, mathematical certification, independent human review, peer review, accessibility conformance, publication action, or rights clearance.
