# Noether R7 Hmong/Filipino Cambium Indexed Glossary Access Boundary - 2026-07-05

Scope: source-canon/provenance only. This packet records Cambium/Smarter Balanced Hmong and Filipino mathematics glossary routes that are visible through public search indexing but return HTTP 403 under direct retrieval in this lane. It does not translate, approve terms, claim native review, claim canonical approval, clear licenses, promote gates, claim completion, or push Git.

Rows:

- CSV: `NOETHER_R7_HMONG_FILIPINO_CAMBIUM_INDEXED_GLOSSARY_ACCESS_BOUNDARY_ROWS_20260705.csv`
- Row count: 8
- Payload policy: no raw PDF, JSON, HTML, text, or source bodies are stored in `outputs`; direct probes returned 403 and no byte-count/hashable payload was captured.

## Findings

- Search indexing exposed three direct mathematics glossary PDF candidates:
  - `https://wa.portal.cambiumast.com/content/contentresources/en/G10-Hmong-Glossary_F6_Final.pdf`
  - `https://wa.portal.cambiumast.com/content/contentresources/en/G4-Hmong-Glossary_F6_Final.pdf`
  - `https://wa.portal.cambiumast.com/content/contentresources/en/G10-Filipino-Glossary_F6_Final.pdf`
- Search indexing also exposed a Grade 8 Hmong resourceitem metadata route:
  - `https://wa.portal.cambiumast.com/content/resourceitem/en/smarter-balanced-math-glossary-grade-8-hmong`
- The indexed Grade 8 Hmong metadata points to `/content/contentresources/en/G8-Hmong-Glossary_F6_Final.pdf`; this lane probed the corresponding absolute PDF URL and recorded the same direct-access blocker.
- Direct retrieval with browser-like headers returned HTTP 403 for all four PDF routes and all four resourceitem routes in the row file.
- The direct tool path therefore has no exact body, byte count, SHA-256 hash, local path, or redistribution/license clearance for these resources.

## Disposition

These rows improve source-return routing for Hmong and Filipino/Tagalog/Ilocano mathematics glossary candidates, but they are access-boundary evidence only. The search-index excerpts are not local source payloads and are not translation evidence or accepted terminology evidence.

Next source actions:

- Retry the Cambium routes in a browser/manual-access workflow or locate an official alternate API/download route.
- If payload access opens, hash the PDF or JSON body in temp storage, delete the body, and update this packet with exact byte counts and SHA-256 values.
- Keep pattern-derived resourceitem slugs below indexed/source-body status until independently indexed or directly retrievable.

## Validation Snapshot

- Row CSV count: 8
- Direct 403 rows: 8
- Rows missing required no-claim boundary: 0
- Rows missing source URL: 0
- Raw PDF/JSON/HTML/text/source payload files stored in `outputs`: 0
- Coverage map row: `R7COV021`
