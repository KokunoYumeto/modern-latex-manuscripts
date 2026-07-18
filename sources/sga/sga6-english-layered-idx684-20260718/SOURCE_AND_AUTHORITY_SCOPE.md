# Source and authority scope

## Coordinate-separated checkpoint

| Coordinate system | First | Last | Next cursor |
|---|---:|---:|---:|
| current-rescribe index | 663 | 684 | 685 |
| printed volume page | 650 | 671 | 672 |
| declared source-PDF page | 653 | 674 | 675 |
| high-resolution witness page | 664 | 685 | 686 |

These coordinates must not be interchanged. The pagewise ledger carries all
four coordinates for every promoted unit.

## Authority order

1. Declared 702-page source scan, SHA-256
   `5194436E290B8FCA54BACD5FF672588335408F1AAD3AE07D62BBA68DF35E3D76`.
2. High-resolution 720-page corroborating scan, SHA-256
   `73FBBAD41340C12ECCDCFCF6C3A1656953FE3D712AA8E391678458CCD17B4BAA`.
3. Current French source-rescribe through idx684, commit
   `859bd5abc3a813ee51e7cbcc6d623e08c1336235`, TeX SHA-256
   `7F32C2080A78A2746CBE52DCC1EC43A8505269F25518FA7B9A86E4E89AF858AC`.
4. Inherited English and later repair baselines as comparison lineage only.

Where the French checkpoint and scans differ, the scan-backed disposition is
explicitly recorded in `ledgers/RECONCILIATION_DELTA_LEDGER.csv`; nothing is
silently normalized. `ledgers/TERMINOLOGY_AND_REJECTED_CHOICES_DELTA.csv`
records accepted and rejected wording or notation. The pagewise ledger binds
the exact current English line ranges to every source coordinate.

## Honest limits

This checkpoint establishes reconciliation only for idx663--684. It does not
turn the inherited prefix into a page-audited translation, does not promote
idx685--702 beyond scan-checked working status, and is neither a critical
edition nor external peer review. The paired idx685 parenthesis was checked
only to close the idx684 boundary; idx685 remains the continuation cursor.
