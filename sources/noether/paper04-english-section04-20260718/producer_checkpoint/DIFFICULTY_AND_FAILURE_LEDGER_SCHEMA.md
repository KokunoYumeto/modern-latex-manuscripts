# Difficulty and failure ledger schema

`DIFFICULTY_AND_FAILURE_LEDGER.jsonl` is append-only. Every nonblank line is one JSON object with a stable `issue_id`, positive integer `record_revision`, nullable `supersedes`, evidence class, authority role, source and target locators, status, confidence, attempts, rejected alternatives, resolution or open state, residual risk, recurrence cue, revisit condition, and lesson.

Initial records use `record_revision: 1` and `supersedes: null`. A correction appends a new object with the same `issue_id`, the next integer revision, and `supersedes` equal to `issue_id@prior_revision`; earlier lines are never rewritten after package freeze. Closure records may use `closes_issues` only for locally resolved IDs and `english_scope_resolutions` for issues resolved in this bounded English unit whose cross-language consequence remains open. Artifact receipts use safe relative paths and exact integer bytes plus uppercase SHA-256.
