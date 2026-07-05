# CJK Source Metadata Bytecount Gap Recheck

Generated: 2026-07-05T15:21:36+02:00

Purpose: resolve the remaining CJK source-metadata bytecount gaps using GitHub commit/tree metadata only. The recheck queries commit and tree JSON metadata for recorded commit SHA-1s and records blob `size` values; it does not fetch raw source bodies or archives.

## Summary

- Rows rechecked: 4.
- Status counts: {'metadata_tree_byte_count_resolved': 4}.
- Target/access counts: {'Japanese': 3, 'Korean addendum/source routing': 1}.

| ID | Target/access | Repository | Commit | Status | Resolved blobs | Byte total |
| --- | --- | --- | --- | --- | ---: | ---: |
| CJK-META-BYTE-20260705-001 | Japanese | imamuray/algebraic-systems | `0dc0f139d456` | metadata_tree_byte_count_resolved | 3/3 | 87773 |
| CJK-META-BYTE-20260705-002 | Japanese | t-higashida/commutative_ring_and_field | `583a25166b56` | metadata_tree_byte_count_resolved | 6/6 | 3736 |
| CJK-META-BYTE-20260705-003 | Japanese | Seasawher/matsumura | `48b9d10bab2d` | metadata_tree_byte_count_resolved | 6/6 | 66745 |
| CJK-META-BYTE-20260705-004 | Korean addendum/source routing | calofmijuck/algebra | `defc7798c87d` | metadata_tree_byte_count_resolved | 6/6 | 40047 |

## Boundaries

- GitHub API URLs are provenance/findability evidence only and do not authorize source payload packaging.
- Korean evidence remains addendum/source-routing, not Korean native-edition authority.
- No raw source body/archive, translation, glossary promotion, native/public signoff, canonical approval, license clearance, gate promotion, completion, Korean-school claim, pan-CJK claim, or Git push is made.
