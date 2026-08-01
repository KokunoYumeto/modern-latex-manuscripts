# Independent archive replay

Date: 2026-08-01

Status: **PASS with disclosed cross-volume warning surface**.

## Package identity

- producer candidate: 84 files / 38,155,078 bytes;
- path-size-SHA-256 aggregate:
  `CE9CFD708A5BBB1C21F406583DAB9ADD93D93FD936E5D98D316273C02A561209`;
- self-excluding manifest: 83 rows / 9,728 bytes / SHA-256
  `A8823F48D3FAE63AA5CED4299821E13BA01EF14B850618374EDB8B088C15D514`;
- copied-package verifier: PASS, 83/83 rows, errors empty;
- reader: 651 pages / 4,252,287 bytes / SHA-256
  `6087FD9475DBDE908EA2025326BC7A49AF33583C7047A7D9332648D2B6387C7A`.

## Fresh build and PDF comparison

A temporary copied package was built through five XeLaTeX passes. The fresh
PDF is 4,252,295 bytes with SHA-256
`0D621FE052751CFFFEC259812DC6B9CC1C5B2EF0696F36CAE5DDA70FC73EC7BB`.
Its only observed document-level difference is the creation timestamp.

Exact comparisons passed for:

- 651/651 decoded page-content streams;
- 651/651 extracted-text pages;
- 651/651 page geometries;
- every link annotation and rectangle;
- all 5,911 named destinations and coordinates.

Direct rendered review of pages 1, 100, 441, and 651 found no clipping,
overlap, malformed formula, blank-content, or pagination defect.

## Warning boundary

The final build log contains 1,814 undefined `hyperref` warning occurrences
covering 703 unique labels. None is an EGA-IV label and there are zero ordinary
undefined-reference warnings. They are intentional positive residuals for EGA
0/I/II/III or external-volume locators. The PDF contains 7,374 valid internal
GoTo actions and zero broken actions.

The packaged build helper accepts relative output paths. An initial absolute
temporary-output invocation was rejected before XeLaTeX started; the intended
relative invocation completed normally. This is a portability limitation of
the helper, not a reader or source-closure defect.

The temporary copied package, fresh build, console, and renders were deleted
after this replay.
