# R9 Official/Academic Web Provenance Header Audit - 2026-07-04

This artifact continues the R9 Africa/Horn/West Africa source-canon-first lane
by tightening official and academic web provenance for already-known source
routes. It records header-only live checks and reconciles them with local
source-return manifests.

Boundary: this is source/provenance/gap evidence only. It does not approve
translation, terminology, native/community review, canonical status, source
license clearance, gate promotion, completion, package upload, or Git push.

## Method

- Performed HTTP `HEAD` checks for representative R9 source-route URLs.
- Stored response/error metadata as JSON under:
  `work/source_canon_witnesses/20260704_r9_official_provenance_headers/`.
- Did not download or commit raw HTML, PDF, CSV, parquet, OCR cache, source
  body, or runtime output in this pass.
- Cross-checked live header results against existing local pass2 manifests and
  payload hashes where available.
- Every CSV row has `promotion_allowed=false`.

Machine-readable ledger:

`R9_OFFICIAL_ACADEMIC_WEB_PROVENANCE_HEADER_AUDIT_20260704.csv`

## Key Findings

- Hausa has live metadata routes for the Amsoshi overview and Google Play app
  page. These remain route/provenance witnesses only because the app/book
  source bodies and source-owner permission are not returned.
- Igbo has a commercial book route and an academic PDF context route. The
  Amazon route rejects `HEAD` with 405 but prior manifest evidence records page
  access; the academic PDF is reachable and hashable as header metadata. Neither
  is a reusable Igbo mathematical source corpus.
- Ethiopia Learning homepage is reachable and remains the portal route for
  Amharic, Oromo, Somali, and Tigrigna/Tigrinya textbook shelves.
- Direct Ethiopia Learning PDF `HEAD` checks for representative Amharic, Oromo,
  Somali, and Tigrigna files failed with an SSL error in this pass. The local
  pass2 manifests still record prior HTTP 200 downloads with PDF hashes, so the
  correct status is not "missing"; it is "locally source-returned but live
  header recheck blocked."
- Afar currently has academic/report context URLs that are live and PDF typed,
  but they are not Afar mathematical source corpus witnesses. Afar remains a
  transcript/source-return blocker.
- The Tigrinya arXiv abstract route is live and the e-print tar remains the
  only current source-level R9 package witness, limited to number/register
  evidence and not algebra or invariant theory.

## Next Work

- Retry Ethiopia Learning direct PDF headers with a different TLS client only
  if needed; current local manifests already carry hashes for source-return
  provenance.
- For Hausa and Igbo, seek source-owner/content returns rather than extracting
  app-store or commercial metadata pages.
- For Afar, search official school/source repositories or transcript-bearing
  material instead of relying on education-context reports.
- For Amharic, Oromo, Somali, and Tigrigna/Tigrinya, continue OCR/text-layer,
  proof-register, and source-permission blocker work from the existing hashed
  PDF shelves.
