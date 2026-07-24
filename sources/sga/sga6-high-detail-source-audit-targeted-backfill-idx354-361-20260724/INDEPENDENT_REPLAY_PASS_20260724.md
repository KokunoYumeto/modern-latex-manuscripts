# Independent Replay PASS

Date: 2026-07-24

Status: PASS

This read-only replay independently verified the SGA6 idx354-361 targeted
high-detail crop backfill against the declared parent scan, historical crop
scripts and commands, audit-log references, and both earlier public crop
snapshots.

## Results

- 105 source identities replayed with zero errors.
- 40 historical full-width bands reconstructed exactly from the parent scan.
- 25 targeted crops reconstructed pixel-for-pixel from those bands.
- 463 prior public target hashes checked; intersection with this backfill: 0.
- 16 original/current audit-context rows closed with zero errors.
- 25 targeted public images accepted.
- 80 full-width page bands retained as metadata-only, rights-blocked witnesses.
- Four CSV controls are rectangular and formula-safe.
- Eight public text/control files scanned with zero privacy hits.

## Archive Identities

- `10t_SGA6_SourceAudit_Targeted_HighDetail_Crops_Backfill_idx354_361_20260724.zip`
  - 4,943,590 bytes
  - SHA-256 `D6B99C7C450CDA649A85105E2546FDD8A98521FB7776DE3A330B92A0D213BCC0`
  - 29 members: 25 targeted images and 4 metadata files
- `10u_SGA6_SourceAudit_Crop_Provenance_RightsBlocked_Metadata_Backfill_idx354_361_20260724.zip`
  - 21,306 bytes
  - SHA-256 `13CFE8D8BB73F24C8627A2243A0786AB70F3E025DF0888B32040257345FE99F1`
  - 5 metadata members
- Producer validation
  - SHA-256 `9E6D48208C736C854C35BF26F3ADD7EDE9A2254C709B046FD2D75435EB4A011F`
- Zenodo upload manifest
  - SHA-256 `B81DFF1D302E7B8904F62C89261E49D7908E71620FA1E15BA1938C8688DC5467`
- Package checksum list
  - SHA-256 `E56F2C8599AE23F53AEEFFB66A6D17568B5BDB1E9F7D7E40E311286FD5A5CC9A`
- Independent replay validation JSON
  - 9,409 bytes
  - SHA-256 `D14A812E97BA78209998BCD1011819233FFE41835804C0022341A2876A7C5FDC`

The live audit log remained active after the packaged audit snapshot was
captured. Both identities are recorded in the validation JSON; the replayed
idx354-361 references themselves close exactly. This PASS does not authorize
redistribution of the parent scan or the 80 full-width page bands.
