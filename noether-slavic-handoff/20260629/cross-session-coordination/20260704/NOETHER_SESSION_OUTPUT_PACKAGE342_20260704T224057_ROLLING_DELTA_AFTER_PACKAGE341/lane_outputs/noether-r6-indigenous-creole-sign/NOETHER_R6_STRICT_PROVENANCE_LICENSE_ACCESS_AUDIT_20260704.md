# NOETHER R6 Strict Provenance License / Access Audit

Status: source_canon_license_access_boundary_metadata_only_no_clearance_claim

Generated: 2026-07-04

Lane: Session I / R6 Indigenous, Creole, and Sign Access

Purpose: classify the package and reuse boundary for the 82 strict exact-URL R6 source-canon witness rows. This audit sits after path/hash replay and URL reachability. It is not a translation artifact, term spine, visual inventory, pilot, source-authority approval, native-review record, community-consent record, license-clearance record, or completion claim.

## Inputs

| Input artifact | Rows | Use |
|---|---:|---|
| `NOETHER_R6_SOURCE_CANON_STRICT_PROVENANCE_WITNESS_TABLE_20260704.csv` | 82 | Strict provenance witness table with exact URL, local path, SHA-256, license/access signal, tags, and source/non-claim boundaries. |
| `NOETHER_R6_STRICT_PROVENANCE_PATH_HASH_AUDIT_20260704.csv` | 82 | Local path and SHA-256 replay evidence. |
| `NOETHER_R6_STRICT_PROVENANCE_URL_REACHABILITY_AUDIT_20260704.csv` | 82 | Headers-only live URL status; no source bodies saved. |

## Output

| Output artifact | Rows | Use |
|---|---:|---|
| `NOETHER_R6_STRICT_PROVENANCE_LICENSE_ACCESS_AUDIT_20260704.csv` | 82 | Per-witness package-use boundary, redistribution payload policy, source-body policy, reviewer/source-owner gate, ethics note, and non-claim boundary. |

## License / Access Classes

| License/access class | Rows | Package boundary |
|---|---:|---|
| `media_or_reuse_pending_no_payload` | 39 | Metadata only. No media payload, embeds, screenshots, derived stills, generated captions, generated transcripts, public alt text, or visual inventory. |
| `source_owner_license_pending_pointer_only` | 25 | Metadata and external pointer only until source-owner or license return. No cached source body payload. |
| `reuse_pending_metadata_only` | 15 | Metadata only until reuse permission and source-authority return. No copied source body or excerpts. |
| `open_access_signal_recorded_reuse_still_requires_attribution_sidecar_and_scope_review` | 3 | The open-access signal is recorded, but R6 still treats source-body reuse as gated. Any source-body payload would require a separate B3 source-canon payload artifact with attribution and scope review. |

## Target Coverage

| Target family | Audited rows | Boundary |
|---|---:|---|
| Indigenous Americas | 4 | Named language/source-owner reviewer route and reuse review required before any excerpt, register, term, translation, or corpus-support promotion. |
| Creole/contact | 14 | Named creole/contact source-owner or reviewer route required before any pan-creole inference, excerpt, term, translation, or corpus-support promotion. |
| Signed language | 60 | Signed-language source-owner/reviewer plus media, caption/transcript, and visual-access gates required before any sign or visual inventory movement. |
| Signed language comparator | 4 | Comparator route only. Not authority for ASL, LSQ, DGS, or any local signed language. |

## Package Rule

B3 may consume row-level provenance metadata, hashes, URLs, topic/language/access tags, and explicit blockers from this audit as support metadata. This lane does not package raw source bodies, copied text, sign media, video/API payload bodies, screenshots, stills, captions, transcripts, public alt text, translations, terms, signs, visual inventories, pilots, or source archives.

The audit records license/access signals exactly as support metadata. It does not claim license clearance, media reuse clearance, source-authority acceptance, native review, community consent, canonical approval, gate promotion, or lane completion.

## Gate State

| Gate | Count |
|---|---:|
| Rows audited | 82 |
| Missing license/access classes | 0 |
| Missing payload policies | 0 |
| Missing non-claim boundaries | 0 |
| License/media reuse clearances | 0 |
| Accepted source-authority rows | 0 |
| Accepted terms | 0 |
| Accepted signs or visual lexical items | 0 |
| Translation starts | 0 |
| Pilots | 0 |

## Next Gates

1. Keep the CSV audit with the strict provenance table whenever B3 or a reader index consumes R6 metadata.
2. For any future row with new permission evidence, create a dated blocker-to-support transition note before changing source-body or package policy.
3. For any signed-language media route, separate link permission, embed permission, screenshot/still permission, caption/transcript permission, visual-access description, and sign authority.
4. For Indigenous and creole/contact rows, keep named-language reviewer/source-owner route evidence separate from general language-family or interlanguage claims.
