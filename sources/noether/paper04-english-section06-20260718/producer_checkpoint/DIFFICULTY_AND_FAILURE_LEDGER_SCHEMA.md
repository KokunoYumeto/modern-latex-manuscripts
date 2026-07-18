# Difficulty and failure ledger schema

Each nonblank line of `DIFFICULTY_AND_FAILURE_LEDGER.jsonl` is a UTF-8 JSON object with stable `record_id`, positive `revision`, `status`, `class`, `locator`, `evidence`, `decision`, `closure_state`, `supersedes_record_revision`, and `references`. Later revisions append rather than replace earlier lines. A record may be `resolved_in_target` while an upstream authority correction remains pending; that distinction must be explicit.
