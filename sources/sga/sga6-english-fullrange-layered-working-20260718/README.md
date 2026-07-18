# SGA 6 English Full-Range Layered Working Reader

Published on Zenodo as version DOI
[`10.5281/zenodo.21421931`](https://doi.org/10.5281/zenodo.21421931), under
the permanent SGA concept DOI
[`10.5281/zenodo.20410947`](https://doi.org/10.5281/zenodo.20410947).
The directly readable PDF is also mirrored at
[`reader-pdfs/sga/02_SGA6_English_FullRange_Layered_WorkingReader_NotCritical_20260718.pdf`](../../../reader-pdfs/sga/02_SGA6_English_FullRange_Layered_WorkingReader_NotCritical_20260718.pdf).

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
pages, contact sheets, and source-local prefix repair evidence. Earlier SGA
Zenodo files retain the full source scans and French workpass packages.

This is a machine-assisted working translation and review surface. It is not a
critical edition, native/community certification, uniform whole-volume source
certification, or a guarantee that every mathematical symbol and diagram is
correct. Citation-critical material should still be checked against the scans.

Run `build.ps1` to rebuild the PDF. Run `validate.ps1` after rebuilding to check
the page count, clean diagnostics, embedded fonts, and authority coordinates.

## GitHub and Zenodo surfaces

This GitHub mirror keeps the editable TeX, ledgers, build evidence, twenty
contact sheets covering all 381 output pages, ten selected full-resolution
render checks, and compact prefix-repair records. The 118.56 MB Zenodo ZIP is
the complete release package: it additionally contains all 381 individual page
renders and the full source-image evidence used by the localized prefix repairs.
`ZENODO_PACKAGE_PAYLOAD_MANIFEST.csv` and
`ZENODO_PACKAGE_SHA256SUMS.txt` describe that complete package, including files
not duplicated in the compact GitHub mirror. `GITHUB_MIRROR_SHA256SUMS.txt`
describes the files actually mirrored here.
The exact public Zenodo API receipt is retained in
`manifests/published-zenodo/20260718_sga6_english_fullrange_record_21421931.json`.
