# Independent replay: PASS

The no-overwrite SGA6 crop interval after the index-326 increment and through
cold-reverification index 330 was independently replayed before dispatch.

- Source interval: files modified after `2026-07-23T19:26:00Z` and no later
  than `2026-07-23T20:14:00Z`.
- Parent PDF indices represented: exactly 327 through 330.
- Targeted high-detail pixels: 1 file / 152,536 bytes.
- Routine page and page-band derivatives: 20 files / 4,779,405 bytes,
  all `rights_blocked_not_public`; none appears as a public ZIP member.
- Source-image identity replay: 21/21 exact.
- Producer freeze/race validation: `PASS`, `errors: []`.
- Independent replay validation: `PASS`, `errors: []`.
- The live certification log advanced after the frozen snapshot; all eight
  packaged audit entries remain present, and each image now links to the
  highest cold-reverification entry for its parent index.
- The selected 9,000-DPI ambiguity crop was directly inspected at original
  resolution and cleanly resolves the source reading `ou` rather than `où`.

## Compact public archives

1. `10o_SGA6_SourceAudit_Explicit_Targeted_HighDetail_Crops_ColdReverify_idx327_330_20260723.zip`
   - 168,122 bytes
   - SHA-256
     `87D7528A44ABABE47E06EA35A5E5D38133B756BAF7D4A448CF0BD9946451B788`
   - 5 members: 1 targeted PNG plus 4 metadata members
   - 167,038 uncompressed bytes
2. `10p_SGA6_SourceAudit_Crop_Provenance_RightsBlocked_Metadata_ColdReverify_idx327_330_20260723.zip`
   - 29,136 bytes
   - SHA-256
     `5A3C552C7BA04018AF071B8B93D9E4E49FA238CDE54D7D4FA246208E1B30A83B`
   - 6 metadata members
   - 27,740 uncompressed bytes

ZIP CRC, safe-name, duplicate-name, exact-set, byte-count, and SHA-256 checks
passed. Five CSV files are rectangular and formula-safe. Public metadata has
zero private path, owner-name, agent-name, email, credential, or thread-marker
hits. Independent replay validation is 4,865 bytes, SHA-256
`E56ECE654129BBC6B3C51D843A21F6A4CB6CBC45E3FEA6B3666F7317694290A3`.

This receipt validates archive mechanics and the public boundary. It does not
certify the French transcription, English translation, mathematics,
completeness, critical-edition status, or rights in the parent scan.
