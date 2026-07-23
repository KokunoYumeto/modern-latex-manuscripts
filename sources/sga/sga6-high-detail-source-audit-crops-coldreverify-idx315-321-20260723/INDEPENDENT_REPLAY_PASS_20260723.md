# Independent replay: PASS

The no-overwrite SGA6 crop interval after the index-314 snapshot and through
cold-reverification index 321 was independently replayed before dispatch.

- Source interval: files modified after `2026-07-23T17:33:54Z` and no later
  than `2026-07-23T18:33:00Z`.
- Parent PDF indices represented: exactly 315 through 321.
- Targeted high-detail pixels: 4 files / 395,186 bytes.
- Routine page and page-band derivatives: 35 files / 8,095,035 bytes,
  all `rights_blocked_not_public`; none appears as a public ZIP member.
- Source-image identity replay: 39/39 exact.
- Producer freeze/race validation: `PASS`, `errors: []`.
- Independent replay validation: `PASS`, `errors: []`.
- All four selected targeted images were directly inspected at original
  resolution.

## Compact public archives

1. `10k_SGA6_SourceAudit_Explicit_Targeted_HighDetail_Crops_ColdReverify_idx315_321_20260723.zip`
   - 418,592 bytes
   - SHA-256
     `06E8C7E19D9933B13663B37E525FEE55719BEDD6E6759B99012775FA81145473`
   - 8 members: 4 targeted PNGs plus 4 metadata members
   - 417,014 uncompressed bytes
2. `10l_SGA6_SourceAudit_Crop_Provenance_RightsBlocked_Metadata_ColdReverify_idx315_321_20260723.zip`
   - 45,513 bytes
   - SHA-256
     `F90CA7ABB63217D7303C29DD73FD744154738F3D77DAF9310BD9BAA412093ED9`
   - 6 metadata members
   - 44,117 uncompressed bytes

ZIP CRC, safe-name, duplicate-name, exact-set, byte-count, and SHA-256 checks
passed. Five CSV files are rectangular and formula-safe. Public metadata has
zero private path, owner-name, agent-name, email, credential, or thread-marker
hits.

This receipt validates archive mechanics and the public boundary. It does not
certify the French transcription, English translation, mathematics,
completeness, critical-edition status, or rights in the parent scan.
