# SGA 6 English Full-Range Layered Working Reader

Published in corrected form on Zenodo and retained on current version DOI
[`10.5281/zenodo.21430393`](https://doi.org/10.5281/zenodo.21430393), under
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
The historical corrected support-package SHA-256 is
`42B9371BE6A031E459A2F77ED27C56F34A11C1E9BBC7B015DFB6DF2E4236F7E8`.
That ZIP is withdrawn from the current public surface because a wrap-aware
audit found reconstructable host-local paths in text/control files. The reader
PDF is byte-identical and remains current.

This package covers the full extant physical source scan, source-PDF pages
001-702, in a 381-page English reader. Coverage is not the same as uniform
source certification. The authority layers are:

- source-PDF 001-525: inherited English control, partially source-synchronized
  but not globally source-checked;
- idx532-662 / source-PDF 526-656: source-checked English synchronized against
  the directly checked French workpass for this range;
- idx663-702 / source-PDF 657-692 and terminal source-PDF 693-702: scan-checked
  English draft pending future French-source reconciliation.

The retained mirror contains the reader TeX/PDF, path-neutral evidence, renders,
and correction material. Path-bearing build/provenance/source-control files are
withheld pending a regenerated privacy-clean support package and checksums.
Earlier SGA Zenodo versions retain immutable historical packages.

This is a machine-assisted working translation and review surface. It is not a
critical edition, native/community certification, uniform whole-volume source
certification, or a guarantee that every mathematical symbol and diagram is
correct. Citation-critical material should still be checked against the scans.

Run `build.ps1` to rebuild the PDF. The prior public validator is withheld with
the path-bearing support controls and must be replaced by a path-neutral public
validator before the support package returns.

## GitHub and Zenodo surfaces

This GitHub mirror keeps only the path-neutral public subset while the support
package is rebuilt. See `PUBLIC_SUPPORT_PACKAGE_WITHDRAWAL.md`. The current
Zenodo receipt is retained at
`manifests/published-zenodo/20260718_sga6_support_privacy_withdrawal_record_21430393.json`.
