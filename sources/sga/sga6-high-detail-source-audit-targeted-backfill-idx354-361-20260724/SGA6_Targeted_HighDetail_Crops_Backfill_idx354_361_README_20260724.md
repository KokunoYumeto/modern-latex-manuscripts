# SGA6 targeted high-detail source-audit crop backfill, indices 354-361

This no-overwrite release closes a visual-evidence gap in the first SGA6 crop
snapshot. It preserves 25 tight formula, glyph, punctuation, and notation crops
that were generated and read during the 2026-07-10 source repair but were not
represented by basename or SHA-256 in the earlier public targeted manifests.

## Public image archive

- `10t_SGA6_SourceAudit_Targeted_HighDetail_Crops_Backfill_idx354_361_20260724.zip` contains 25 targeted images /
  4,974,469 image bytes.
- Per-index image counts: idx354: 1, idx356: 3, idx357: 1, idx358: 7, idx359: 6, idx360: 3, idx361: 4.
- Each target is bound through its exact generator script or inline-command
  hash to an exact rights-blocked 500-dpi source band, then to parent PDF index,
  one-based PDF page, printed page, parent scan hash, crop coordinates, scale,
  original repair ledger entry, and later cold-reverification ledger entry.
- Pixel replay is exact from parent PDF to the historical source bands and from
  those bands to all 25 published targets.

These crops cover dense lambda-ring and Chern-ring notation around formulas
(5.5.2), (5.6.1), (6.1.1), (6.1.2), (6.2.1), and (6.3.1)-(6.3.2), including
subscripts, operation symbols, punctuation, and displayed morphisms. Filenames
are historical working names; the manifest is the controlling locator.

## Rights-blocked page bands

`SGA6_PageBands_idx354_361_RightsBlocked_Manifest_20260724.csv` records 80 full-width page-band
derivatives / 15,487,185 bytes:

- 40 historical 500-dpi repair bands (`p354`-`p361`);
- 40 current 2400-dpi cold-reverification bands (`cve0p354`-`cve0p361`).

Their exact hashes, dimensions, page mappings, bounding boxes, generator
identities, and QA dispositions remain public, but their pixels are not
redistributed. `10u_SGA6_SourceAudit_Crop_Provenance_RightsBlocked_Metadata_Backfill_idx354_361_20260724.zip` groups this complete provenance surface.

## Parent, claims, and rights

The parent is the 720-page Internet Archive-derived SGA6 reader
`Théorie des Intersections et Théorème de Riemann-Roch.pdf`, 26,833,956 bytes, SHA-256
`73FBBAD41340C12ECCDCFCF6C3A1656953FE3D712AA8E391678458CCD17B4BAA`. The parent PDF is not bundled.

These images are visual/provenance evidence used in source checking. They do
not certify the French transcription, English translation, mathematics,
completeness, or critical-edition status. Underlying French work and scan
rights remain with their holders. No blanket license or rights transfer is
asserted.
