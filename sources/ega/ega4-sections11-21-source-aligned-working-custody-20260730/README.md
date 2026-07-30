# EGA IV Sections 11-21 active source custody snapshot

This directory preserves an exact, privacy-clean snapshot of the active
no-overwrite EGA IV Sections 11-21 English source-alignment successor as it
stood at 2026-07-30T10:11:00+02:00.

## Scope

The latest fully documented source-alignment gate closes the repairs through
Theorem 11.3.10 and Lemma 11.3.10.2 on printed page 138. The next authority
page is printed page 139. Later Section 11 bytes and Sections 12-21 are
preserved as inherited working source and are not promoted by this snapshot.

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
1,822,111 bytes. Their original relative layout is retained so the master can
resolve its inputs. `SHA256SUMS.csv` gives the identity of every other file in
this directory.

The current active source has a coherent three-pass XeLaTeX build:

- 317 letter pages / 2,111,931 bytes
- SHA-256
  `30D79ED03C3920DDF13F429A7B53F42201F977F05FC7BF51084DAF0A84311C52`
- final log SHA-256
  `4575561B86A75EF41FB1C6D91A70186DAE4FFCAF6E540672A2C0E45E84EE69E4`

That PDF and its build logs are not included here. This is a lightweight
source-survival update, not a new public reader release. An isolated one-pass
build from the copied GitHub source also exited 0 and produced 314 pages.

This is a public GitHub survival snapshot, not an EGA IV Sections 11-21 reader
release, completion claim, critical edition, rights clearance, or
convention-v2 reference certification. The existing EGA Zenodo record remains
unchanged.
