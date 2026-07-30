# EGA IV Sections 11-21 active source custody snapshot

This directory preserves an exact, privacy-clean snapshot of the active
no-overwrite EGA IV Sections 11-21 English source-alignment successor as it
stood at 2026-07-30T11:47:00+02:00.

## Scope

The latest fully documented source-alignment gate closes the repairs through
Corollary 11.4.3 on printed page 145. The next authority page is printed page
146. Later Section 11 bytes and Sections 12-21 are preserved as inherited
working source and are not promoted by this snapshot.

The source tree includes Sections 11-21 because that is the active standalone
build closure. It does not claim that all of Sections 11-21 have been
source-aligned.

## Authority

- EGA IV Part 3, governing Sections 11-15: SHA-256
  `F365212B38F20608BA34C21AE3EE40BBAE1B42D9D3DFF01A85356F9CC819C23E`.
- EGA IV Part 4, governing Sections 16-21: SHA-256
  `B4277FB99C6EDF8FEEC5B01F54368E4B8521BCD52871316C0EDF6FF4AE69389E`.

The authority PDFs are not included. Direct authority images decide
transcription; pre-existing OCR is locator and drafting material only.

## Contents and status

The preserved build harness and active source tree contain 14 files and
1,830,120 bytes. Their original relative layout is retained so the master can
resolve its inputs. `SHA256SUMS.csv` gives the identity of every other file in
this directory.

The captured source has a coherent four-pass XeLaTeX checkpoint build:

- 319 letter pages / 2,118,752 bytes
- SHA-256
  `FDBFE91AF3F856FD50DB373896A7597A42F0460689B19616EBFE39E470E40FEA`
- final log SHA-256
  `14072FFCBFE467CCE729E6A926E28E2F6DF3DF01F4F16B95744EE94915882E90`
- zero hard TeX diagnostics or rerun requests

That PDF and its build logs are not included here. This is a lightweight
source-survival update, not a new public reader release. An isolated one-pass
build from the copied GitHub source also exited 0 and produced 316 pages.

This is a public GitHub survival snapshot, not an EGA IV Sections 11-21 reader
release, completion claim, critical edition, rights clearance, or
convention-v2 reference certification. The existing EGA Zenodo record remains
unchanged.
