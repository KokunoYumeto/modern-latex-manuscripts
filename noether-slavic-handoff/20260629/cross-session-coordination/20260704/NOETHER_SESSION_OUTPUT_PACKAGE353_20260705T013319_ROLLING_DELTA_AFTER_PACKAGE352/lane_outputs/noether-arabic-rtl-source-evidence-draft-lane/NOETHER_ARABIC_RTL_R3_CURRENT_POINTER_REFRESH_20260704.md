# Noether Arabic RTL R3 Current Pointer Refresh

Created: 2026-07-04

Status: draft source-canon/provenance refresh only. Non-canonical, not native reviewed, not approved, not license-cleared, not a package, and not a completion claim. This does not authorize translation, glossary expansion, term promotion, reviewer packets, gate promotion, raw-payload publication, or Git push.

## Current R3 Sources Checked

- `R3_SOURCE_CANON_POLICY_SYNC_AUDIT_20260704T210315Z`
- `R3_ARABIC_EXTERNAL_POINTER_PAYLOAD_PROBE_20260704T210216Z`
- `R3_SOURCE_BODY_PACKAGE_OMIT_MANIFEST_20260704T210917Z`

## Arabic-Relevant Refresh

| Refresh row | Source | Arabic-relevant fact | Hash / status | Lane action |
| --- | --- | --- | --- | --- |
| `AR-R3-CUR-001` | R3 policy sync `210315Z` | 70 policy rows; 26 Arabic RTL consumer rows; 3 Arabic gap rows. | rows CSV `485D299ACDA44CF33C050919408E533ED52F6C48DCC8CF6E2098AC4880F1706C` | Treat as current R3 policy/access/upload baseline. |
| `AR-R3-CUR-002` | R3 Arabic payload probe `210216Z` | 13 Arabic external-pointer payloads fetched; 9 match expected hashes; 4 live-drift/hash mismatch rows; 0 fetch failures. | rows CSV `34B36157ABE1725A6D4B114FCF233DCE93A1EC6D055993A735AADC08EF39F495` | Use as current payload-probe baseline; keep mismatches blocked. |
| `AR-R3-CUR-003` | Payload mismatch detail | Drift rows remain `INV-009`, `INV-010`, `REP-011`, and rejected `REJECT-013`. | `INV-010` current probe hash is `E8CFF35F018A69200B17D0E1BEE7B3FBAAFF543D40A66338423AE110EDFB9AD7` | Do not replace expected hashes without B3 or owner-lane review. |
| `AR-R3-CUR-004` | R3 source-body omit manifest `210917Z` | 57 omit rows total; 33 Arabic-targeted raw body/cache rows; 26 under current pointer/cache roots; 7 superseded/historical duplicates. | rows CSV `6AEA9C1B7576670B057AE58F5EC08C0406E0B3A67B83639EF2906DAF1C935558` | Use as current packaging-safety omit surface. |
| `AR-R3-CUR-005` | Current Arabic omit rows | Arabic payload kinds: 15 PDFs, 5 HTML snapshots, 5 text/wikitext, 4 zip archives, 3 TeX bodies, 1 tar archive. | 6 preferred duplicate refs; 20 unique current/cache refs | Manifest/hash/path only; no raw source body copying or publication. |

## Notes

R3 split-lane sync still observed an older Arabic rollup hash, `CB3A0B369F87CA577E9FFA166D7C311DB77E11796C0601B296A526E86F5083B0`, while the Arabic lane had already moved forward locally. This refresh records the newer R3 current pointers without treating R3's observed pre-refresh hash as an error in the Arabic source-canon content.

The current R3 policy sync preserves the same Arabic upload-policy counts as the earlier intake: 17 manifest/hash/URL-only rows, 5 conditional attribution/license-review rows, 1 manifest-only source-archive row, and 3 gap-only rows. The direct Arabic invariant-theory TeX/arXiv/GitHub source-package gaps remain open.

The source-body omit manifest is a packaging-safety artifact. It identifies raw payloads and caches that should remain manifest/hash/URL provenance unless B3 creates a dedicated gated payload artifact and license/access review supports it.

## Boundary

This refresh is source-canon/provenance maintenance only. It makes no translation, term approval, bridge promotion, native-review, canonical-approval, license-clearance, gate-promotion, completion, package, or Git-push claim.
