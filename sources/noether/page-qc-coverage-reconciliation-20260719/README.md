# Noether page-QC coverage reconciliation

This directory is the privacy-clean public projection of the 2026-07-19
P10/P14/P15 page-QC reconciliation checkpoint. It repairs an author-level
tracking defect; it does not alter or republish a German TeX/PDF body.

## Scope

- 51 historical complete-page audit records are represented: P10 printed
  pp. 536-545, P14 pp. 182-203, and P15 pp. 138-156.
- The canonical per-page ledger grows from 724 to 758 unique page keys.
- All 34 previously absent expected page keys are restored; the three bounded
  paper ranges now have zero missing page keys.
- Exact later-authority survival links connect live P10 and P15 to R796 and
  live P14 to the post-R804-v11 authority span.
- These are imported historical audits, not 51 fresh inspections performed on
  2026-07-19.

The broader Noether source-audit cursor remains Paper 4 printed pp. 118-143.
Paper 4 pp. 144-154 and the cumulative tail pp. 711-777 were already integrated
before this reconciliation.

## Producer custody

The exact local producer archive is
`Noether_LocalCodex_20260719_PageQC_CoverageReconciliation_COMPLETE.zip`:

- 1,046,227 bytes
- SHA-256
  `DE513046F4DDD9006990F2B76F2FD4E5E693ABCFB286C44C3F5A0D1F62B1D5F6`
- 39 ZIP entries including one directory entry; 38 file entries
- 7,403,613 decompressed file bytes
- zero duplicate or unsafe archive paths

The original ZIP is not mirrored publicly. It contains absolute local paths,
internal task references, source-span TeX bodies, diffs, and path-bearing build
scripts. `reports/ORIGINAL_ARCHIVE_CONTENTS.csv` preserves the relative names,
bytes, and hashes for its 33 manifested build artifacts without redistributing
those excluded contents. The producer handoff described this manifest as 28
rows; direct inspection found 33 valid rows, and that count discrepancy is
retained in `PRODUCER_PACKAGE_RECEIPT.json`.

## Public projection

- `historical_audits/` contains the four exact, public-safe source audit CSVs.
- `ledgers/` contains 1,270 detailed QC rows, 758 canonical page rows, and 466
  correction-origin rows. Only cells containing private/internal locators were
  replaced with fixed redaction notices.
- `reports/` contains before/after coverage, sanitized span-survival metadata,
  a manifest-only source-witness inventory, validation, and the original
  archive contents manifest.
- `SANITIZATION_MAP.csv` links every transformed producer artifact to its
  public successor by bytes and SHA-256.
- `PRODUCER_LOGBOOK_ADDENDUM.md` records the original failure mode and the
  general workflow lesson.

The 51 source-page image witnesses remain local and are represented by
filename, byte count, existence state, and a
`manifest_only_local_witness_not_redistributed` disposition. No source scan
pixels are included here.

## Claim boundary

This is evidence/provenance reconciliation. It is not a new Noether edition,
not proof that the pages were freshly re-inspected on 2026-07-19, not global
author completion, not independent human certification, and not a rights
determination.
