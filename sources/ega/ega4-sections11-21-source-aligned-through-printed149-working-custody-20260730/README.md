# EGA IV Sections 11-21 active source custody snapshot

This directory preserves an exact, privacy-clean snapshot of the active
no-overwrite EGA IV Sections 11-21 English source-alignment successor as it
stood at 2026-07-30T16:34:07+02:00.

## Scope

The latest fully documented source-alignment gate closes printed page 149,
including the corrected proof of Proposition 11.4.11 and Proposition 11.4.12.
The next authority page is printed page 150, beginning at
`source/source_aligned/ega4-11.tex` line 2341. Later Section 11 bytes and
Sections 12-21 are preserved as inherited working source and are not promoted
by this snapshot.

The source tree includes Sections 11-21 because that is the active standalone
build closure. It does not claim that all of Sections 11-21 have been
source-aligned.

## Authority

- EGA IV Part 3, governing Sections 11-15: SHA-256
  `F365212B38F20608BA34C21AE3EE40BBAE1B42D9D3DFF01A85356F9CC819C23E`.
- EGA IV Part 4, governing Sections 16-21: SHA-256
  `B4277FB99C6EDF8FEEC5B01F54368E4B8521BCD52871316C0EDF6FF4AE69389E`.

The authority PDFs and crops are not included. Direct authority images decide
transcription; pre-existing OCR is locator and drafting material only. The
page-149 decisions were made from fifteen overlapping 5,000-dpi authority
bands whose private evidence manifest is SHA-256
`C9B6BAD145B1022B1223C6215BF1BAE5C7C47FB78B123E4C600F365E49D32AB5`.

## Material corrections

The page-149 gate restores the displayed fiber identity and its actual
flatness base in Reduction I, restores the printed direction of the local-ring
factorization, reconstructs the lost disjoint-union and finite-morphism
argument in Reduction III, and corrects Proposition 11.4.12 to the authority's
base-change notation. French authority bytes are unchanged.

## Contents and status

The preserved build harness and active source tree contain 14 files and
1,830,715 bytes. Their original relative layout is retained so the master can
resolve its inputs. Only `source/source_aligned/ega4-11.tex` differs from the
preceding printed-page-146 snapshot. `SHA256SUMS.csv` gives the identity of
every other file in this directory.

The captured source has a coherent four-pass XeLaTeX checkpoint build:

- 319 letter pages / 2,119,563 bytes
- SHA-256
  `3095714E4F363FD9923450F5E5409732F04A40DE3576201756F04E257F5B0C5E`
- final log SHA-256
  `741D6F4AD227F78CE833E84B5FC79F70CF7E17F93A14FB0D5F6674F16D1D7EA2`
- zero hard TeX diagnostics or rerun requests

That PDF and its build logs are not included here. This is a lightweight
source-survival update, not a new public reader release. A disposable isolated
one-pass build from the copied GitHub source also exited 0 and produced 317
pages.

This is a public GitHub survival snapshot, not an EGA IV Sections 11-21 reader
release, completion claim, critical edition, rights clearance, or
convention-v2 reference certification. The existing EGA Zenodo record remains
unchanged.
