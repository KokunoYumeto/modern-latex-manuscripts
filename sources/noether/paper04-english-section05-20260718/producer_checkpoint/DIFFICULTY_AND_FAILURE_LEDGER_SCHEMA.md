# Difficulty and failure ledger schema

`DIFFICULTY_AND_FAILURE_LEDGER.jsonl` is append-only. Every nonblank line is one JSON object with a stable `issue_id`, positive integer `record_revision`, nullable `supersedes`, evidence class, authority role, source and target locators, status, confidence, attempts, rejected alternatives, resolution or open state, residual risk, recurrence cue, revisit condition, and transferable lesson.

Initial records use revision 1 and `supersedes: null`. Later corrections append a new revision and refer to `issue_id@prior_revision`; frozen rows are not rewritten. Exact artifact receipts may be attached only after the final source hash, build, extraction, render, and visual review are closed.

