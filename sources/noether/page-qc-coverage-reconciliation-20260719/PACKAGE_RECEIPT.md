# Archive projection receipt

Archive review independently reopened the producer ZIP, streamed every file,
checked its archive structure, and extracted it to a temporary directory before
classification.

## Intake checks

- Producer ZIP size and SHA-256 match the durable handoff.
- The archive has no duplicate names, path traversal, rooted paths, or stream
  read failures.
- All 33 rows in the enclosed build manifest match extracted paths, sizes, and
  SHA-256 values.
- The handoff's 28-row manifest count does not match the enclosed 33-row file;
  the file itself is internally valid and is treated as authoritative for
  archive-content accounting.

## Public transformations

The three reconciled ledgers retain their original rows, columns, decisions,
statuses, notes, counts, and non-private provenance. Affected locator cells are
replaced atomically rather than partially rewriting path strings:

- detailed page-QC ledger: private source-witness and evidence-file locators;
- canonical per-page ledger: private evidence locators;
- correction-origin ledger: private paths or internal task references in the
  origin-source field.

The span-survival report retains artifact basenames, authority labels, hashes,
line counts, equality results, and dispositions. The witness inventory drops
only the absolute-path column and adds an explicit manifest-only disposition.
The validation report drops only the live-TeX absolute locator and keeps its
SHA-256 plus every reported metric.

`SANITIZATION_MAP.csv` records producer/public hashes and affected-cell counts.
The public tree is separately checked for strict CSV parsing, rectangularity,
formula-sigil safety, JSON parsing, duplicate stable identifiers where a
primary key exists, and private/internal locator patterns.

## Exclusions

The original ZIP, source-span TeX bodies, source diffs, build and promotion
scripts, prior full ledgers, complete master logbook, absolute witness paths,
and all source-page images are excluded from this projection. Their existence
and hashes remain represented without making a redistribution or certification
claim.
