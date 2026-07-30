# EGA I active source custody snapshot

This directory preserves an exact, privacy-clean snapshot of the active
no-overwrite EGA I English source-alignment successor as it stood at
2026-07-30T10:11:00+02:00.

## Scope

The source-aligned pass is reviewed continuously through Section 3.6.5.
The exact next cursor is Section 3.7.1, printed page 118 / authority physical
page 117.

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

`source/` contains 14 files and 555,820 bytes captured byte-exactly from the
active source tree. `SHA256SUMS.csv` gives the identity of every other file in
this directory.

The current active source has a coherent three-pass XeLaTeX build:

- 109 letter pages / 732,479 bytes
- SHA-256
  `614CA63E4E5FF08532B609FEECB31F54633C65B8E14CC970CFE0195A2957BAF7`
- final log SHA-256
  `CEE9F36B3D12E09A43BE7F315322609072B04837F0F8414B9AF2877F6C8A526D`
- 273 named destinations / 1,242 internal GoTo actions / 0 broken targets

That PDF and its build logs are not included here. This is a lightweight
source-survival update, not a new public reader release. An isolated one-pass
build from the copied GitHub source also exited 0 and produced 108 pages.

This is a public GitHub survival snapshot, not a reader release, completed EGA
I translation, critical edition, rights clearance, or convention-v2 reference
certification. The existing EGA Zenodo record is unchanged.
