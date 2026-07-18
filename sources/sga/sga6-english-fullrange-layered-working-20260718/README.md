# SGA 6 English Full-Range Layered Working Reader

Published in corrected form on Zenodo as version DOI
[`10.5281/zenodo.21422245`](https://doi.org/10.5281/zenodo.21422245), under
the permanent SGA concept DOI
[`10.5281/zenodo.20410947`](https://doi.org/10.5281/zenodo.20410947).
The directly readable PDF is also mirrored at
[`reader-pdfs/sga/02_SGA6_English_FullRange_Layered_WorkingReader_CORRECTED_20260718.pdf`](../../../reader-pdfs/sga/02_SGA6_English_FullRange_Layered_WorkingReader_CORRECTED_20260718.pdf).

## Corrective release

This endpoint supersedes the SGA 6 English PDF and support ZIP in historical
Zenodo version `10.5281/zenodo.21421931`. That reader printed footnote marker 14
in Lemma 5.8.2 but lost the note text because the insertion was executed inside
an `amsmath` display. Physical PDF page 81 now contains marker 14, footnote 14,
and the complete final-object/constant-sheaf note. The corrected reader SHA-256
is `F8B1E15754BEB5C83CF2A47B261D6F9F907DE5B7E8A6ED4DF311C624E38C7B8E`.
The complete corrected Zenodo package SHA-256 is
`42B9371BE6A031E459A2F77ED27C56F34A11C1E9BBC7B015DFB6DF2E4236F7E8`.

This package covers the full extant physical source scan, source-PDF pages
001-702, in a 381-page English reader. Coverage is not the same as uniform
source certification. The authority layers are:

- source-PDF 001-525: inherited English control, partially source-synchronized
  but not globally source-checked;
- idx532-662 / source-PDF 526-656: source-checked English synchronized against
  the directly checked French workpass for this range;
- idx663-702 / source-PDF 657-692 and terminal source-PDF 693-702: scan-checked
  English draft pending future French-source reconciliation.

The package contains editable TeX, the reader PDF, exact authority/formula/
terminology/page ledgers, clean two-pass build evidence, all 381 rendered reader
pages, contact sheets, source-local prefix repair evidence, the exact post-seal
technical diff, and an independent integration review. Earlier SGA Zenodo files
retain the full source scans and French workpass packages.

This is a machine-assisted working translation and review surface. It is not a
critical edition, native/community certification, uniform whole-volume source
certification, or a guarantee that every mathematical symbol and diagram is
correct. Citation-critical material should still be checked against the scans.

Run `build.ps1` to rebuild the PDF. Run `validate.ps1` after rebuilding to check
the page count, clean diagnostics, embedded fonts, and authority coordinates.

## GitHub and Zenodo surfaces

This GitHub mirror keeps the editable TeX, ledgers, build evidence, twenty
contact sheets covering all 381 output pages, selected full-resolution render
checks, compact prefix-repair records, and the correction evidence. The 139.31
MB corrected Zenodo ZIP is the complete release package: it additionally
contains all 381 individual page renders and the full source-image evidence used
by the localized repairs. Its internal `PAYLOAD_MANIFEST.csv` and
`SHA256SUMS.txt` provide exact package verification.
The exact public Zenodo API receipt is retained in
`manifests/published-zenodo/20260718_sga6_english_correction_record_21422245.json`.
