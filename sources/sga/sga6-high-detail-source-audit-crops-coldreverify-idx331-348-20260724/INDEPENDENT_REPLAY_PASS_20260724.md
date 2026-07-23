# Independent replay PASS: SGA6 source-audit crops idx331-348

Status: PASS

The final no-overwrite projection was independently replayed against the live
Claude scratchpad source set and the frozen release ZIPs.

## Exact result

- Source images replayed: 93/93.
- Parent indices represented: 331-348.
- Public targeted pixels: 3 files / 479,785 bytes.
- Recovered named pixels: 0.
- Routine page-band derivatives: 90 files / 21,548,165 bytes, represented by
  exact public metadata only and not redistributed.
- CSVs: rectangular and formula-safe.
- Privacy scan: zero hits.
- ZIP paths, sets, sizes, hashes, CRCs, and member identities: PASS.
- Parent reader: 720 pages / 26,833,956 bytes / SHA-256
  `73FBBAD41340C12ECCDCFCF6C3A1656953FE3D712AA8E391678458CCD17B4BAA`.
- Audit-log packaging snapshot: 8,783,922 bytes / SHA-256
  `53108A9AC03D0231F342F45B8FFD96EDB157408F63E58620CE948CBC68F6533E`.

## Public archives

- `10q_SGA6_SourceAudit_Explicit_Targeted_HighDetail_Crops_ColdReverify_idx331_348_20260724.zip`
  - 524,940 bytes
  - SHA-256
    `9699239A633DA3736676BF9CF861B0B750E99A9027EC215020460B960F1F1157`
  - 7 members, including 3 targeted PNGs
- `10r_SGA6_SourceAudit_Crop_Provenance_RightsBlocked_Metadata_ColdReverify_idx331_348_20260724.zip`
  - 101,314 bytes
  - SHA-256
    `E241BC56FE0932EDA9DA914C13B7D7C360C724D020050BD243E7E921B26B1987`
  - 6 metadata members and no pixels

## Targeted adjudications

- idx333: the scan reads `i.j`; the period was preserved.
- idx335: the scan reads `{Xt}`, not `{1+Xt}`; the asymmetry was preserved.
- idx339: the prose reads lowercase `v` while formulas use `\nabla`; the
  source-level mismatch was documented rather than silently normalized.

These crops are visual and provenance evidence used during source checking.
They do not certify the transcription, translation, mathematics, rights,
completeness, or critical-edition status.
