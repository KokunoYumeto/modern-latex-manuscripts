# EGA I active source custody snapshot

This directory preserves an exact, privacy-clean snapshot of the active
no-overwrite EGA I English source-alignment successor as it stood at
2026-07-30T09:51:26+02:00.

## Scope

The source-aligned pass is reviewed continuously through Section 3.3.15.
The exact next cursor is Section 3.4.1, printed page 111 / authority physical
page 110.

The source tree contains the complete inherited EGA I TeX closure because the
working reader compiles as a volume. Material beyond the declared cursor is
preserved as inherited working source and is not promoted by this snapshot.

## Authority

- EGA I NUMDAM French original: 227 pages, 31,680,717 bytes, SHA-256
  `9ABA23020217535977E279BDD06A0413F48DA703086865BA4C00766C85DF4AE6`.
- EGA II NUMDAM French original, used only for the inserted EGA I addenda
  Section 1.8: 219 pages, 27,414,108 bytes, SHA-256
  `111834EFFFE9E90D068389D418F08925A82B4A54AE2957F080712D4180E032EB`.

The authority PDFs are not included. Their rendered pages decide ambiguous
readings; embedded text and pre-existing OCR are locator material only.

## Contents and status

`source/` contains 14 files and 555,687 bytes captured byte-exactly from the
active source tree. `SHA256SUMS.csv` gives the identity of every other file in
this directory.

The current active source has a coherent three-pass XeLaTeX build:

- 109 letter pages / 732,306 bytes
- SHA-256
  `5DEBA2E39976DC4064D4B7573F64229526165942452A5F4D5BD11562717BD426`
- final log SHA-256
  `4C74241B0808CA4D6EA7373B11986BF01FDBB5F4F5A8C2F1744513F7E29DC0F0`
- 272 named destinations / 1,241 internal GoTo actions / 0 broken targets

That PDF and its build logs are not included here. This is a lightweight
source-survival update, not a new public reader release. An isolated one-pass
build from the copied GitHub source also exited 0 and produced 108 pages.

This is a public GitHub survival snapshot, not a reader release, completed EGA
I translation, critical edition, rights clearance, or convention-v2 reference
certification. The existing EGA Zenodo record is unchanged.
