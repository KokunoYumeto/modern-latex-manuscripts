# Machine-readable evidence schema - SGA2-VIII-C22

Unit stable ID: `SGA2-VIII-C22`. Continuation cursor: French source line 2670
after blank line 2669.

The four substantive CSV ledgers are UTF-8, RFC-4180-style rectangular tables.
Every row has a stable primary ID, unit ID, authority role, source and/or target
locator, status, confidence, record revision, continuation cursor, and a
revisit or supersession trigger. Cells are quoted and must not begin with an
Excel formula sigil (`=`, `+`, `-`, or `@`). `UNIT_HASHES.csv` is generated
only after the independently sealed artifact set is frozen.

`STRUCTURAL_INDEX.jsonl` uses `record_id = stable_id@record_revision` and
requires parent/child closure for internal stable IDs. External links are
explicitly prefixed (`INBOUND:`, `OUTBOUND:`) or named comparison controls.
Revision links use exact record IDs and must be reciprocal. The root and QA
records carry self-gate-to-independent-seal revision histories. Independent
structure, note, formula, and boundary records are children of the root.

`DIFFICULTY_REVISION_LEDGER.jsonl` uses unique `event_id` values and stable
object IDs shared with the structural ledger. A revision event names the exact
prior event in `supersedes`; the prior event names its closer in `closed_by`.
The initially supplied printed-page locator 90 is retained as rejected input;
the source-backed correction to printed page 89 supersedes it.

Validation requires exact authority hashes; CSV rectangularity and formula
safety; unique primary IDs; JSONL parse, required-field, stable-ID, parent,
child, revision, and event closure; source/target page distinctions; build and
render evidence; forbidden-control-byte and privacy scans; Artifact Tool
import/inspection/render checks; and an exact self-excluding SHA-256 manifest
of every proposed checkpoint file.
