# Machine-ledger validation

The public package preserves append-only revision history while replacing excluded source-image and internal-coordination paths with public-safe control locators. No record or supersession edge was discarded.

- Five CSV ledgers: 70 records total, 64 current records.
- Two JSONL ledgers: 23 records total, 19 current records.
- CSV files parse as strict rectangular UTF-8 with exact headers, stable IDs, integer revisions, safe leading characters, and no duplicate `(ID, revision)` pair.
- Every JSONL line parses as exactly one JSON object with its declared schema fields.
- Structural parent/child and local cross-reference links close against declared unit IDs or explicitly external prior/next units.
- Every `supersedes` reference resolves to the immediately preserved earlier revision.
- The difficulty/failure closure revision preserves the failed first closure and explicitly supersedes it after the two printed-page-137 deltas were found.
- All active artifact receipts resolve either to exact packaged files or to clearly labeled excluded-control receipts with retained byte/hash evidence.
- Validation failures: 0.

