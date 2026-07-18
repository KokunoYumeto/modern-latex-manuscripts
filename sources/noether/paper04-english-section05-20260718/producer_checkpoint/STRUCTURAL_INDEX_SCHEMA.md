# Structural index schema

`STRUCTURAL_INDEX.jsonl` is append-only. Each nonblank line is one JSON object with a stable `unit_id`, positive `record_revision`, evidence class, authority role, bounded status, confidence, unit type, exact R823 and print coordinates, parent/child links, target locator, source uncertainty, review state, and nullable `supersedes` reference.

The root section record additionally declares a continuation cursor. Child spans must partition R823 lines 3953–4043 exactly, including internal blank control lines, without a gap or overlap. Initial records use revision 1 and `supersedes: null`; corrections append a higher revision and point to `unit_id@prior_revision`.

