# Noether R6 Strict Provenance URL Reachability Audit

Generated: 2026-07-04

Lane: Session I / R6 Indigenous, Creole, and Sign Access

Status: URL reachability/provenance maintenance only. No source body was saved. No source-authority, reviewer approval, community consent, canonical approval, license clearance, media reuse, accepted term/sign, translation, pilot, lane-completion claim, Git staging, commit, or push is claimed.

## Method

The audit used headers-only `HEAD` probes with a `GET` range fallback when needed. It recorded HTTP status, final URL, content type, content-length header when provided, and errors. It did not store remote response bodies, source text, media, captions, transcripts, screenshots, OCR output, or derived excerpts.

## Result

| Artifact | Rows | Role |
|---|---:|---|
| `NOETHER_R6_SOURCE_CANON_STRICT_PROVENANCE_WITNESS_TABLE_20260704.csv` | 82 | Strict exact-URL source-canon/provenance witnesses after removing placeholder URL rows. |
| `NOETHER_R6_STRICT_PROVENANCE_URL_REACHABILITY_AUDIT_20260704.csv` | 82 | Per-row URL reachability and access audit. |
| `NOETHER_R6_NON_STRICT_ROUTE_METADATA_ROWS_20260704.csv` | 1 | DGS route metadata row with local hash but placeholder live URL, split out of the strict table. |

| Reachability status | Rows |
|---|---:|
| `reachable_headers_only` | 77 |
| `access_restricted_endpoint_present` | 5 |
| Missing/moved/request-failed rows | 0 |

## Access-Restricted Rows

| Gap row | Witness | Target | URL status |
|---|---|---|---|
| `R6-URL-GAP-001` | `R6-QA-SAR-003` | Aymara | Minedu DSpace handle returned `403 Forbidden` to headers-only audit. |
| `R6-URL-GAP-002` | `R6-QA-SAR-001` | Quechua Central | Minedu DSpace handle returned `403 Forbidden` to headers-only audit. |
| `R6-URL-GAP-003` | `R6-QA-SAR-002` | Quechua Chanka | Minedu DSpace handle returned `403 Forbidden` to headers-only audit. |
| `R6-URL-GAP-004` | `DGS-SAR-004` | DGS | Sign2MINT API endpoint returned `403 Forbidden` to headers-only audit. |
| `R6-URL-GAP-005` | `DGS-SAR-005` | DGS | Sign2MINT video/CDN route returned `403 Forbidden` to headers-only audit. |
| `R6-URL-GAP-006` | `DGS-SAR-008` | DGS | Row contained a placeholder URL with `...`; moved to non-strict route metadata until an exact URL is resolved. |

The three Minedu rows still have local file/hash provenance and prior license/access signals in the strict table. The 403 result is a live reachability/access blocker, not a source rejection and not a license/source-authority change.

The DGS rows remain route/source-access metadata only. URL reachability does not authorize sign acceptance, media reuse, copied stills, captions/transcripts, visual inventory, translation, or pilot work.

## Maintenance Rule

Future R6 updates should rerun this audit when source URLs change, when B3 package metadata consumes strict witness rows, or when an access-restricted/source-owner route is resolved. Rows with placeholder URLs or inaccessible live routes must remain explicit gaps until repaired.
