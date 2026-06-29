# Galois / Eisenstein DPI Source-Quality Check

Date: 2026-06-29

Purpose: record the source-resolution evidence for the Galois and Eisenstein
source-intake packets without confusing derivative PDF metadata or helper-image
metadata with actual scan-source quality.

This is source-intake metadata only. It is not a finished edition, not promoted
TeX, and not a critical-edition claim.

## Galois

Local packets:

- `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\source intake priority authors 20260629\Galois\Galois_SOURCE_PACKET_20260629.zip`
- `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Galois\Galois_source_staging_20260629.zip`

Source-quality conclusion:

- The 1897 IA collected-edition source should be described as **IA scandata
  reports 600 dpi / 600 ppi source masters**.
- A sampled 1897 JP2 page has geometry `5100 x 6600` but no embedded DPI units
  in ImageMagick; do not cite the JP2 header itself as embedded optical DPI.
- The 1908 manuscript/UMich witness has IA scandata `<dpi>600</dpi>` and
  per-page `<ppi>600</ppi>`. A sampled TIFF page has geometry `3522 x 5700`.
- The 1846 NUMDAM/JMPA PDF is a useful first-publication comparator, but it is
  not the preferred scan-master layer for the quick-win transcription packet.
- Gutenberg TeX is a control transcription only and should not be promoted
  without scan comparison.

Recommended public phrasing:

> Galois is a compact source-intake/quick-win packet. The preferred 1897 and
> 1908 image witnesses are recorded by their scan metadata as 600 ppi, while
> derivative PDFs/OCR/Gutenberg TeX are locator or comparator witnesses only.

## Eisenstein

Local packet root:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\source intake priority authors 20260629\Eisenstein\Eisenstein_SOURCE_PACKET_20260629`

Source-quality conclusion:

- The UofT raw JP2 archive remains the canonical local Eisenstein image witness.
- A sampled UofT raw page has geometry `5010 x 3336`.
- Embedded `72` resolution metadata in the UofT derivative layer is coordinate
  metadata, not optical scan DPI. Do not describe this packet as 72 dpi.
- No strict optical DPI claim is made for Eisenstein from the current local
  evidence. Describe it as raw JP2/source-image intake with BSB/Google
  comparators, not as a certified 600+ ppi source.
- BSB and Google/IA sources are useful comparator/OCR layers but are not the
  first authority for promoted TeX.

Recommended public phrasing:

> Eisenstein is source-intake/handoff material centered on a UofT raw JP2 image
> witness, with BSB and Google/IA comparator layers. OCR and existing text are
> locator/control witnesses only; no strict optical DPI certification is made.

## Workflow Lesson

Record native resolution from the source platform's scan metadata or page-image
masters where possible. Treat PDF `72 dpi` metadata and rasterized helper images
as presentation/coordinate artifacts unless independent scan metadata supports
an optical-resolution claim.
