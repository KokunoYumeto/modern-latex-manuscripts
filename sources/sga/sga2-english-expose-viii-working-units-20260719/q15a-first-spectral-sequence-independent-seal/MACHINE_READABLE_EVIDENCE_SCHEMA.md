# Machine-readable evidence schema

CSV files are UTF-8 comma-delimited tables with one header row and stable
primary IDs in column one. Every substantive record carries a unit ID,
authority role, source and target locators, status, confidence, revision,
continuation cursor, and revisit condition where applicable. Cells beginning
with spreadsheet formula sigils are forbidden.

JSONL files contain exactly one UTF-8 JSON object per line. Structural records
use stable IDs plus revision-qualified record IDs. Difficulty records use
stable IDs plus unique event IDs. Parent and child links, cross-references,
`supersedes`, `superseded_by`, and `closed_by` must close inside the unit or
use an explicit `INBOUND:` or `OUTBOUND:` prefix.

Unit: `SGA2-VIII-Q15A`. Source scope: corrected French lines 2611--2616.
Continuation cursor: line 2618 after blank line 2617.
