# Independent replay PASS: SGA6 source-audit crops idx349-353

Status: **PASS**

The no-overwrite release boundary was independently replayed against the live
Claude scratchpad, the exact parent-reader identity, the generator-script
projections, the packaged certificate-log snapshot, every manifest row, and
every ZIP member.

## Closed boundary

- Parent PDF indices: 349 through 353, exactly.
- Selected source images: 28 files.
- Public targeted pixels: 3 files / 231,187 bytes.
- Rights-blocked routine page-band pixels: 25 files / 5,660,082 bytes.
- Recovered named crops outside the explicit targeted set: 0.
- Privacy findings in generated public metadata: 0.
- Formula-trigger cells in all CSV controls: 0.
- Source-image identity differences: 0.
- ZIP set, path, CRC, byte-count, and SHA-256 differences: 0.

## Targeted crop replay

- `zoom352_ou.png`: parent index 352 / parent page 353 / printed page 339;
  21,597 x 3,432 grayscale pixels; 9,000-DPI output rasterization; SHA-256
  `BB3F50AE63C9A669358E8A3D41F0624EF5A191AD7B26E4F8901DAEF738F3C23A`.
- `zoom353_remarque.png`: parent index 353 / parent page 354 / printed page
  340; 21,166 x 2,288 grayscale pixels; 8,000-DPI output rasterization;
  SHA-256
  `B1F188A0A259F619299FE7E03F26416A6E489AA7E00223FA2890267E275330CB`.
- `zoom353_deduit.png`: parent index 353 / parent page 354 / printed page 340;
  19,690 x 2,441 grayscale pixels; 8,000-DPI output rasterization; SHA-256
  `30C3B18349659044B3B74996CDC17A5658C4200FF694A8E7C3A6A74A28C841F8`.

The replay explicitly asserts these filename-to-index bindings. This catches
stale helper variables in one-off generator scripts and verifies the concrete
page expression that actually produced each crop.

## Outer archives

- Targeted crop ZIP: 251,666 bytes, 7 members, SHA-256
  `6B5388B3EB3ADEBAACF64C5D66A15C1D7AB299D249100957B097EA99499D1386`.
- Provenance and rights-blocked metadata ZIP: 36,766 bytes, 6 members,
  SHA-256
  `793AC91A3A5D4899E7676146634A0FFC9E9759E9F1A05A2B4D257F3F423CB658`.

The machine-readable replay is
`INDEPENDENT_REPLAY_VALIDATION_20260724.json`, 5,276 bytes, SHA-256
`081516ADE299004D504AD4D20FF99A1C3FD06D172023BE36723B42D9626BD3F7`.
Its status is `PASS` and `errors` is empty.

These crops are source-audit visual/provenance evidence. They do not certify
the transcription, translation, mathematics, completeness, critical-edition
status, or redistribution rights in the parent work or scan.
