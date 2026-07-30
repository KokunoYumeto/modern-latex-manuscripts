# EGA IV Sections 16-18 working custody through printed page 14

At `2026-07-30T23:55:02+02:00`, archive maintenance captured the latest
closed source-alignment gate from the active EGA IV Sections 16-18 lane. The
producer had begun imaging printed page 15, but the copied source and controls
were stable before and after capture.

## Exact custody package

`sources/ega/ega4-sections16-18-source-aligned-through-printed14-working-custody-20260730`

- 13 files / 672,972 bytes;
- 12-row self-excluding `SHA256SUMS.csv`, SHA-256
  `9399E26A447726B3AD56F491293949AB72C0C2DD6E8046E09F2D00C46D8E1031`;
- validation SHA-256
  `269BE276B91585103D6C85D6328CE5C007DCCD880CCBEE1EDC6CA7B88E01FC3E`,
  status `PASS_SOURCE_CUSTODY_ONLY`, errors `[]`;
- active `ega4-16.tex`, 176,699 bytes, SHA-256
  `0709ABA3B463E86C5CCB0CE8778BC684F4DBB55D27CBAF21713F4BB141214B35`;
- exact source-alignment progress CSV, 10 rows / 2,208 bytes, SHA-256
  `F9E157454314CBAFE44B1F3CD3720F4AF3CF77A59343D84C48E405C6B813C4E4`.

Printed pages 5-14 / authority physical pages 4-13 are closed. The continuation
cursor is printed page 15 / physical page 14 / Proposition 16.3.4 continuation,
`ega4-16.tex` line 500. Pages 11-14 restore an omitted affine-module equality
and citation, correct the primed global-sections locus, repair the
principal-parts graded object, restore an Erratum III locator, and distinguish
invariance from pointwise fixation under the canonical symmetry.

The copied package builds in an isolated one-pass XeLaTeX replay to 120 pages
with exit code 0 and zero TeX error lines. The producer's clean three-pass r7
checkpoint is 121 pages / 827,040 bytes, SHA-256
`5774244064F3BFCF27AAE772C7195A9C4CABBE1EFD6D12004F40FA50556ED314`,
but remains excluded and unpromoted. Two complete package builds were
byte-identical, and privacy hits were zero.

This no-overwrite package supersedes the printed-page-10 package only as the
current active source-survival snapshot; the earlier package remains public
history. Authority PDFs, source pixels, raw logs, and reader PDFs remain
excluded. This is not a reader release, Sections 16-18 completion claim,
critical edition, rights clearance, accessibility review, or reference-v2
certification. No Zenodo mutation is requested.
