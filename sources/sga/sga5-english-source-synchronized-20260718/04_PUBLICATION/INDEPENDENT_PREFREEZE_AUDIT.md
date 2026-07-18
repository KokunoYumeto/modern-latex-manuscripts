# Independent pre-freeze audit

Audit date: 2026-07-18, Europe/Berlin.

## Reviewed snapshot

- Support-stage files: 49.
- Uncompressed bytes: 13,901,515.
- External snapshot manifest:
  `CONTROL/PREFREEZE_SNAPSHOT_SHA256.csv`.
- Snapshot-manifest SHA-256:
  `4F8FFD44993262F3BD7737A933ADBC123EB20104881730FD0D4EFD356C65434D`.
- Recomputed matches: 49/49; byte, hash, and path mismatches: 0.

Two separate read-only review passes examined this snapshot. Their independence
is operational: they did not author or edit the reviewed TeX/PDF, source
ledgers, publication controls, or snapshot manifest. This is not independent
human scholarly certification.

## Primary objects and source disclosures

- TeX: 798,096 bytes, SHA-256
  `5A79546320606564E0FEF609A13E7F71D42487281325C4CCF97DC20990B7F4C4`.
- PDF: 2,060,055 bytes, 309 pages, SHA-256
  `0455F60C9318F0080A8ACFD4F307849F67E9C321A4C5FB9BB01A21E862721290`.
- PDF parses strictly, is unencrypted, has nonblank metadata, and has zero
  extraction failures or empty pages.
- Extracted PDF text contains the complete printed-p.14 source-defect note and
  printed-p.43 ambiguity note.
- Focused renders of PDF pages 8 and 26 visibly contain the respective notes,
  with no clipping or overlap.

## Build and ledger checks

- Both path-sanitized logs report a 309-page build, zero fatal/undefined/
  package/pdfTeX warnings, zero underfull boxes, and nine disclosed overfull
  boxes.
- Each sanitized log is 49,723 bytes, SHA-256
  `4842DC57268881939F5565FCB6CC473DEBF4B245C16C500058B4C9CD95192946`,
  with 185 `<LOCAL_USER_ROOT>` placeholders and no private path prefix.
- The exact-candidate and final-resolution ledgers each contain 432 unique IDs
  with identical ID sets. Final dispositions sum to 432: 170 propagated exact,
  150 propagated after reviewed nonexact mapping, 53 current-equivalent, 51
  source-language-only, and 8 rejected absent from the final French control.
- The terminology/adverse ledger has 40 rows; the reopened-locus ledger has two
  rows; the structural summary/difference/representation ledgers have 10, 34,
  and 9 rows respectively.
- Exposé I's English/French footnote delta is exactly +2 and is classified as
  the two editorial disclosures, not hidden source-footnote parity.
- The 254/432 granular private-tree evidence locators omitted from this lean
  bundle are explicitly disclosed; 178/432 resolve to the bundled exact CSV.

## Render and origin checks

- Bundled images: 22, all openable—six focused 180-DPI page renders and 16
  sequential contact sheets covering PDF pages 1-309 with no gap or overlap.
- The six focused hashes match the private English-reader QA originals.
- Every contact sheet's private-source and packaged bytes, formats, and hashes
  match the 16-row normalization receipt.
- Normalized contacts are PNG24 8-bit sRGB; dimensions are preserved and
  normalized-vs-source RMSE is at most 0.001499.
- All 309 contact cells map sequentially to private English-reader page renders;
  the four formerly viewer-blank sheets and both focused disclosure pages were
  directly opened and found populated and legible.
- No bundled image is a source-scan render. The PDF contains no embedded raster
  image rows.

## Privacy, source-exclusion, rights, and live-state checks

- No absolute private path, filesystem username leak, UUID/task/thread ID, or
  unpublished correspondence was found in text or binary metadata. Deliberate
  mentions of Floris are attribution, not path leakage.
- No source scan, scan-derived image, French TeX/PDF, inherited English TeX, or
  external-English candidate file is bundled; no payload file hashes to those
  controls.
- Scan and crop references in the ledgers are bounded evidence locators and
  rights caveats, not bundled witnesses.
- The French-control contradiction and missing-reader status are disclosed;
  no independent French completeness certification is inferred.
- A final read-only API check during review resolved the concept to
  `10.5281/zenodo.21430393`, with 17 files and `cc-zero` record metadata. The
  older SGA 5 PDF and scan-bearing support ZIP remain unchanged. `cc-zero` is
  not represented as proof of redistribution rights.

## Verdict and remaining gate

**PASS for pre-freeze content, safety, render, and evidence packaging.** No
substantive-body, disclosure, privacy, scan-exclusion, ledger, render-QA,
rights-wording, or live-state blocker remains in the reviewed snapshot.

This verdict does not approve a yet-unbuilt ZIP or public manifest and does not
certify the scholarship. After adding this receipt and exact internal
manifests, the support ZIP and four-file public payload must be rehashed,
extracted and verified, scanned again for privacy/source exclusions, and
subjected to a final no-race check before handoff.
