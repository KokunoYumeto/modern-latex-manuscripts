# EGA I active source custody snapshot

This directory preserves an exact, privacy-clean snapshot of the active
no-overwrite EGA I English source-alignment successor as it stood at
2026-07-30T12:12:49+02:00.

## Scope

The source-aligned pass is reviewed continuously through Section 5.4. The
exact next cursor is Proposition 5.5.1 at `source/ega1/ega1-5.tex` line 594,
printed page 136 / authority physical page 135.

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

`source/` contains 14 files and 556,053 bytes captured byte-exactly from the
active source tree. `SHA256SUMS.csv` gives the identity of every other file in
this directory.

The captured source has a coherent three-pass XeLaTeX checkpoint build:

- 109 letter pages / 730,401 bytes
- SHA-256
  `BD514FDD7DFC0B9D093BC974825D1FEE8B743A61C71E02BE0F01212DE6C719B3`
- final log SHA-256
  `4975AC21E9D24A53AA8269C45D03EF5F6BC7BD5848DD4EAD4C4F9E4F072E93C6`
- zero hard TeX diagnostics or rerun requests

That PDF and its build logs are not included here. This is a lightweight
source-survival update, not a new public reader release. An isolated one-pass
build from the copied GitHub source also exited 0 and produced 108 pages.

This is a public GitHub survival snapshot, not a reader release, completed EGA
I translation, critical edition, rights clearance, or convention-v2 reference
certification. The existing EGA Zenodo record is unchanged.
