# SGA6 high-detail source-audit crops, cold re-verification indices 331-348

This no-overwrite incremental release preserves the high-value source crops
actually generated and read after the prior index-330 increment. It does not
turn ordinary reader-page renders into a second copy of the parent PDF.

## Image archives

- `10q_SGA6_SourceAudit_Explicit_Targeted_HighDetail_Crops_ColdReverify_idx331_348_20260724.zip` contains 3 explicit `zoom`, `zoomp`,
  `peek`, or `recheck` crops / 479,785
  image bytes.
- No additional recovered named crop archive was emitted for this interval because every selected high-detail image was explicitly named as a targeted zoom or recheck.


Each ZIP includes its exact image manifest plus this README, the parent-source
identity, and the audit-context table. The manifests record image hashes,
dimensions, parent PDF index where recoverable, printed-page evidence from the
audit log where available, generator-script identity, recovered crop
coordinates, render DPI, processing profile, and QA disposition.

## Targeted findings

- `zoom333_ij.png` (parent PDF index 333 / page 334) was generated to resolve
  punctuation in the displayed formula. The crop confirms that the scan reads
  `i.j` with a period; the source quirk was intentionally preserved.
- `zoom335_xt.png` (parent PDF index 335 / page 336) was generated to distinguish
  the displayed factor. The crop confirms the scan's asymmetric `{Xt}`, not
  `{1+Xt}`; the source reading was intentionally preserved.
- `zoom339_notee.png` (parent PDF index 339 / page 340) was generated to compare
  prose and formula notation. The crop confirms lowercase `v` in the prose
  while the formulas use `\nabla`; that source-level mismatch was documented
  rather than silently normalized.

`10r_SGA6_SourceAudit_Crop_Provenance_RightsBlocked_Metadata_ColdReverify_idx331_348_20260724.zip` groups the complete public provenance surface, including both
targeted-image manifests and the rights-blocked routine-page manifest. Detailed
files remain individually browsable in the public GitHub package; Zenodo keeps
them compact.

## Deliberate non-image surface

`SGA6_Routine_PageBands_idx331_348_RightsBlocked_Manifest_20260724.csv` records 90 routine whole-page or
page-band derivatives / 21,548,165
bytes. Their exact hashes and provenance remain public, but their pixels are
not redistributed. These are computationally cheap near-page reconstructions,
carry higher source-redistribution risk, and are not the symbol-level evidence
requested for durable preservation.

## Parent and snapshot

The parent is the 720-page Internet Archive-derived SGA6 reader
`Théorie des Intersections et Théorème de Riemann-Roch.pdf`, 26,833,956 bytes, SHA-256 `73FBBAD41340C12ECCDCFCF6C3A1656953FE3D712AA8E391678458CCD17B4BAA`.
The parent PDF itself is not bundled. This temporal, no-overwrite image
increment covers files modified after `2026-07-23T20:14:00+00:00` and closes
at `2026-07-23T23:05:00+00:00`, after the cold-reverification pass reached parent
index 348 and before it began index 349. The
recoverable indices span 331 through
348 across
18 distinct indices; this is not a claim of continuous
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
