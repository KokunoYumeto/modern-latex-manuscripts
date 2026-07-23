# SGA6 high-detail source-audit crops, cold re-verification indices 327-330

This no-overwrite incremental release preserves the high-value source crops
actually generated and read after the prior index-321 increment. It does not
turn ordinary reader-page renders into a second copy of the parent PDF.

## Image archives

- `10o_SGA6_SourceAudit_Explicit_Targeted_HighDetail_Crops_ColdReverify_idx327_330_20260723.zip` contains 1 explicit `zoom`, `zoomp`,
  `peek`, or `recheck` crops / 152,536
  image bytes.
- No additional recovered named crop archive was emitted for this interval because every selected high-detail image was explicitly named as a targeted zoom or recheck.


Each ZIP includes its exact image manifest plus this README, the parent-source
identity, and the audit-context table. The manifests record image hashes,
dimensions, parent PDF index where recoverable, printed-page evidence from the
audit log where available, generator-script identity, recovered crop
coordinates, render DPI, processing profile, and QA disposition.

`10p_SGA6_SourceAudit_Crop_Provenance_RightsBlocked_Metadata_ColdReverify_idx327_330_20260723.zip` groups the complete public provenance surface, including both
targeted-image manifests and the rights-blocked routine-page manifest. Detailed
files remain individually browsable in the public GitHub package; Zenodo keeps
them compact.

## Deliberate non-image surface

`SGA6_Routine_PageBands_idx327_330_RightsBlocked_Manifest_20260723.csv` records 20 routine whole-page or
page-band derivatives / 4,779,405
bytes. Their exact hashes and provenance remain public, but their pixels are
not redistributed. These are computationally cheap near-page reconstructions,
carry higher source-redistribution risk, and are not the symbol-level evidence
requested for durable preservation.

## Parent and snapshot

The parent is the 720-page Internet Archive-derived SGA6 reader
`Théorie des Intersections et Théorème de Riemann-Roch.pdf`, 26,833,956 bytes, SHA-256 `73FBBAD41340C12ECCDCFCF6C3A1656953FE3D712AA8E391678458CCD17B4BAA`.
The parent PDF itself is not bundled. This temporal, no-overwrite image
increment covers files modified after `2026-07-23T19:26:00+00:00` and closes
at `2026-07-23T20:14:00+00:00`, after the cold-reverification pass reached parent
index 330 and before it began index 331. The
recoverable indices span 327 through
330 across
4 distinct indices; this is not a claim of continuous
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
