# Independent extracted-package replay

Date: 2026-07-30

Status: **PASS**

The 45-file pre-receipt package was copied to an isolated short-path directory
and verified without modifying the candidate. It contained 4,046,276 bytes.
Its canonical relative-path, byte-count, and SHA-256 row identity was
`9AC1511D0CBF6917D865E8F5D435603B4D8CB2AF55D3FB96A741A7242CDF2300`
both before and after replay.

The copied package verifier returned PASS with:

- 43/43 manifested files exact;
- 750 targets, 1,459 edges, 2,431 candidates, 1,364 applications, and 418
  residuals;
- 113 PDF pages, 1,701 named destinations, and 1,459 resolved internal GoTo
  actions;
- CSV, JSON, font, privacy, and forbidden-source-witness errors all zero.

A fresh BibTeX plus five-pass XeLaTeX build from the copied package returned
PASS. Its final PDF was 1,356,417 bytes with SHA-256
`2B9F84B3BFEE0CBD44EF57FF50B35282BBC3EC34F21905FE14F31ADAA8AE78C2`.
The differing byte identity is limited to build-path-sensitive PDF identifiers.
Against the packaged reader, all 113 decoded page streams and extracted-text
streams, all 1,701 destination signatures, all 1,459 annotation/action
signatures, and metadata were exact.

This receipt records technical reproducibility only. It is not mathematical
peer review, accessibility certification, legal advice, or rights clearance.
