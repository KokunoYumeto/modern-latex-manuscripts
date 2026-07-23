# SGA6 high-detail source-audit crop snapshot at cold-reverification index 314

This release preserves the high-value source crops actually generated and
read during the current SGA6 cold re-verification. It does not turn ordinary
reader-page renders into a second copy of the parent PDF.

## Image archives

- `SGA6_SourceAudit_Explicit_Targeted_HighDetail_Crops_Snapshot_ColdReverify_idx314_20260723.zip` contains 460 explicit `zoom`, `zoomp`,
  `peek`, or `recheck` crops / 41,930,961
  image bytes.
- `SGA6_SourceAudit_Recovered_Named_HighDetail_Crops_Snapshot_ColdReverify_idx314_20260723.zip` contains 1470 additional named formula,
  glyph, punctuation, diagram, and prose-detail crops /
  111,046,911 image bytes.

Each ZIP includes its exact image manifest plus this README, the parent-source
identity, and the audit-context table. The manifests record image hashes,
dimensions, parent PDF index where recoverable, printed-page evidence from the
audit log where available, generator-script identity, recovered crop
coordinates, render DPI, processing profile, and QA disposition.

## Deliberate non-image surface

`SGA6_Routine_PageBands_RightsBlocked_Manifest_20260723.csv` records 1698 routine whole-page or
page-band derivatives / 489,940,982
bytes. Their exact hashes and provenance remain public, but their pixels are
not redistributed. These are computationally cheap near-page reconstructions,
carry higher source-redistribution risk, and are not the symbol-level evidence
requested for durable preservation.

## Parent and snapshot

The parent is the 720-page Internet Archive-derived SGA6 reader
`Théorie des Intersections et Théorème de Riemann-Roch.pdf`, 26,833,956 bytes, SHA-256 `73FBBAD41340C12ECCDCFCF6C3A1656953FE3D712AA8E391678458CCD17B4BAA`.
The parent PDF itself is not bundled. This temporal, no-overwrite image
snapshot closes at `2026-07-23T17:33:54+00:00`, after the current cold-reverification
pass reached parent index 314 and before it began index 315. It also preserves
same-parent targeted crops from earlier audit phases. The recoverable indices
span 4 through
714 across
496 distinct indices; this is not a claim of continuous
index coverage.

The generator scripts survive only as local operational files and contain
private paths. They are not published. Their SHA-256 identities and recoverable
page/bounding-box/DPI parameters are projected into the manifests.

## Claim and rights boundary

These images are visual/provenance evidence used in source checking. They do
not certify the French transcription, English translation, mathematics,
completeness, or critical-edition status. Underlying French work and scan
rights remain with their holders. No blanket license or rights transfer is
asserted. Reported DPI is output rasterization resolution, not a claim of new
optical detail beyond the parent scan.
