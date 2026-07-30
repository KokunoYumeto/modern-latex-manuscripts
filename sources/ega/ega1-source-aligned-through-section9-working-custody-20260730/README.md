# EGA I active source custody snapshot

This directory preserves an exact, privacy-clean snapshot of the active
no-overwrite EGA I English source-alignment successor as it stood at
2026-07-30T16:20:33+02:00.

## Scope

The source-aligned pass is reviewed continuously through Section 9, ending
with Proposition 9.6.6. The exact next cursor is the Section 10 heading at
`source/ega1/ega1-10.tex` line 1, printed page 181 / authority physical page
180.

The source tree contains the complete inherited EGA I TeX closure because the
working reader compiles as a volume. Material beyond the declared cursor is
preserved as inherited or active working source and is not promoted by this
snapshot.

## Authority and inherited English

- EGA I NUMDAM French original: 227 pages, 31,680,717 bytes, SHA-256
  `9ABA23020217535977E279BDD06A0413F48DA703086865BA4C00766C85DF4AE6`.
- EGA II NUMDAM French original, used only for the inserted EGA I addenda
  Section 1.8: 219 pages, 27,414,108 bytes, SHA-256
  `111834EFFFE9E90D068389D418F08925A82B4A54AE2957F080712D4180E032EB`.
- The inherited English base is the community translation at
  <https://github.com/ryankeleti/ega>. Its preserved project attribution and
  contributor history continue to apply.

The authority PDFs are not included. Their rendered pages decide ambiguous
readings; embedded text and pre-existing user-supplied OCR are locator
material only. No OCR was generated for this snapshot.

## Contents and status

`source/` contains 14 files and 556,753 bytes captured byte-exactly from the
active source tree. Six source components differ from the preceding Section
5.4 custody snapshot. `SHA256SUMS.csv` gives the identity of every other file
in this directory.

The captured source has a coherent three-pass XeLaTeX checkpoint build:

- 109 letter pages / 732,055 bytes
- SHA-256
  `672492D78496793F0C6C00FF80263B81852F6DD6983DA04D723C112711761286`
- final log SHA-256
  `EFA774A9B90A5D4F6B0DFC77489AD6B5CB64C52BD866536FD4B26A2ACA577AB5`
- zero hard TeX diagnostics or broken named targets

That PDF and its build logs are not included here. An isolated one-pass build
from the copied GitHub source also exited 0 and produced 108 pages.

This is a public GitHub survival snapshot, not a reader release, completed EGA
I translation, critical edition, rights clearance, peer review, or
convention-v2 reference certification. The existing EGA Zenodo record is
unchanged.
