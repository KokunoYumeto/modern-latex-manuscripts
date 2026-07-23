# Weber Volume I High-Detail Audit Crops

This package preserves the source-image derivatives actually used in the
current Weber Volume I transcription and fidelity audit. It does not repackage
ordinary PDF page renders as a substitute for the source PDF.

## Public image dumps

- `Weber_VolumeI_PageMapped_HighDetail_Audit_Crops_20260723.zip`: 248 tight high-detail crops,
  136,178,476 uncompressed image bytes.
  Every image has an exact Weber printed-page and source-PDF-page locator in
  `Weber_VolumeI_PageMapped_HighDetail_Audit_Crops_Manifest_20260723.csv`. The crop filename records the upper-left origin as
  a percentage of the source page; the opposite corner was not retained and is
  therefore not invented.
- `Weber_VolumeI_Recovered_Unmapped_Audit_Images_20260723.zip`: 846 additional recovered audit images,
  130,572,847 uncompressed image bytes.
  These are preserved because they are real working zooms or derivatives from
  the same current Volume I audit, but their filenames do not retain a reliable
  page locator. Their manifest says `volume_known_page_unresolved`.

## Deliberate exclusions

The source directory contains 3066 PNG files / 1,218,008,434
bytes. This release excludes 1972 routine whole-page,
top/middle/bottom strip, offset-check, and enhancement renders /
951,257,111 bytes. Those files are
computationally cheap derivatives of the already available zoomable source PDF
and are not the high-value crop corpus requested for archive preservation.

## Parent and method

The parent is Heinrich Weber, *Lehrbuch der Algebra*, Volume I (1895), exact
scan SHA-256 `50BA482A39C9918AC81B31D631B65B11C37C5E67BEC42C559F6D504A28196DEB`. The PDF has 686 pages and the audit
mapping is `source PDF page = printed page + 26`.

The page-mapped tight-crop filenames were emitted by the audit's `crop_src.py`
profile. Its documentation declares a 600-dpi source render and a 3x display
upscale by default, but callers could override those values; the PNG manifests
therefore report embedded DPI when present and do not turn the tool default
into false per-file certainty.

## Claim boundary

These images are visual/provenance evidence. They do not certify the German
transcription, English translation, mathematics, completeness, or critical
edition status. The second ZIP is intentionally retained with unresolved page
locators rather than given fabricated coordinates.

The 1895 source work is public domain. This release asserts no new copyright in
the historical source text or mechanically derived crop pixels.
