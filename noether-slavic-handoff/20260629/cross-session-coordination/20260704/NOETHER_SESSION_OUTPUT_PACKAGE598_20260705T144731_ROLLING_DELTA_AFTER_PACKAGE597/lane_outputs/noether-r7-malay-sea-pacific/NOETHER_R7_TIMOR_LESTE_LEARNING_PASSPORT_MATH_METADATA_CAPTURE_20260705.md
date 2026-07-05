# Noether R7 Timor-Leste Learning Passport Math Metadata Capture - 2026-07-05

Scope: source-canon/provenance only. This packet records public Timor-Leste Learning Passport route metadata for Tetun/Portuguese mathematics courses. It does not translate, approve terms, claim native review, claim canonical approval, clear licenses, promote gates, claim completion, or push Git.

Rows:

- CSV: `NOETHER_R7_TIMOR_LESTE_LEARNING_PASSPORT_MATH_METADATA_CAPTURE_ROWS_20260705.csv`
- Row count: 29
- Payload policy: no raw HTML, JavaScript, JSON, PDF, video, text, or source bodies are stored in `outputs`; remote route bodies were hashed in memory and represented only by row metadata.

## Captured Routes

- Timor-Leste Learning Passport landing page: HTTP 200, 485278 bytes, SHA-256 `30274AE17962720B286C05B82779668C14E67C9C64C7CD2B9B5ABB4778C8C630`.
- `landing-page.js`: HTTP 200, 7767 bytes, SHA-256 `480BD7A852CCA99E09A30F08448DD7B56E6998BA8E899A3821230682F4D64888`.
- 27 public `/api/v1/Courses/{courseId}/Metadata` endpoints for mathematics-related courses.

## Findings

- All 29 route probes returned HTTP 200.
- The JavaScript route establishes the public metadata endpoint pattern: `/api/v1/Courses/{courseId}/Metadata`.
- The metadata endpoints list course names, item counts, first visible item titles, and image routes.
- Across the 27 mathematics metadata endpoints, 825 course items are listed.
- Largest metadata courses observed: `Manual de Matemática` and `Livro de Exercícios de Matemática`, each with 172 listed items.
- Course IDs include mathematics exercise books, teacher guides, summaries, Tele-Escola mathematics video courses, Grade/period courses, and complementary multiplication/addition/division table material.

## Boundary

This packet is stronger than a title-only web-search gap because the landing page, API-route JavaScript, and 27 course metadata JSON endpoints are directly hashable. It is still not exact corpus-body evidence: no underlying lesson, PDF, video, or source-package body was exposed or captured in this unauthenticated pass.

Next source actions:

- Probe official item-body/file APIs or offline package routes if access gates permit.
- Search for downloadable Timor-Leste mathematics PDFs corresponding to the captured course IDs and item lists.
- Keep all Learning Passport rows as route/metadata provenance unless exact lesson or file bodies are captured and hashed separately.

## Validation Snapshot

- Row CSV count: 29
- Landing/JavaScript route rows: 2
- Course metadata rows: 27
- HTTP 200 rows: 29
- Listed mathematics course items: 825
- Rows missing required no-claim boundary: 0
- Raw HTML/JS/JSON/PDF/video/text/source payload files stored in `outputs`: 0
