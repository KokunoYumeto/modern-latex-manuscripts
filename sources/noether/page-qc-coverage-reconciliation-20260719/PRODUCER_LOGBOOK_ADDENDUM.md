
## 2026-07-19 - P10/P14/P15 page-QC coverage-index reconciliation

### What failed

The canonical per-page QC index contained only 5 of the expected 10 P10 pages, 4 of 22 P14 pages, and 8 of 19 P15 pages. That made 34 pages look unaudited even though complete page-level source-audit CSVs and all corresponding source images were already present locally.

This was a tracking and logbook defect, not proof that the underlying pages had never been inspected. It arose because later author-level ledgers imported a few focused Web rows but did not ingest the older complete-page dispositions.

### Evidence recovered

- P10: 10 rows, printed pp. 536-545, from `P10_pp536_545_visual_dispositions_20260629.csv`.
- P14: 22 rows, printed pp. 182-203, from `P14_page_visual_dispositions.csv`.
- P15: 19 rows, printed pp. 138-156, from `P15_page_audit_R780.csv`.
- Every named P10, P14, and P15 page-image witness was found on disk.

### Current-head authentication

The older audit heads were not treated as current merely because their files existed.

- Live P10 is byte-identical to the P10 span in R796.
- Live P15 is byte-identical to the P15 span in R796.
- Live P14 is byte-identical to the P14 span in the post-R804 integrated v11 head.
- Each live span differs from the older complete-page audit head. Those differences represent later source-backed revision history and are retained as explicit diff evidence, not hidden by a blanket survival claim.

### Ledger action

All 51 historical audit instances are imported into the detailed page-QC ledger with their original auditor/source basis and an explicit `not a fresh visual pass` limitation. Canonical page rows are updated or created per printed page. The canonical index grows from 724 to 758 unique page keys, closing the 34-row bookkeeping gap.

No TeX repair is promoted in this checkpoint. No page is called newly visually certified by the import itself. The value of this operation is that future completion estimates and work assignments can distinguish genuinely unaudited pages from pages whose existing audit evidence had merely been omitted from the control ledger.

### Generalizable lesson

A paper-level closure note is not enough. Every complete-page audit must be ingested as one machine-readable record per printed page at the time it is performed. Later focused repairs should add QC instances; they must not replace or obscure the complete-page audit record. Exact-span survival links and historical source inspections are separate facts and must both be logged.

