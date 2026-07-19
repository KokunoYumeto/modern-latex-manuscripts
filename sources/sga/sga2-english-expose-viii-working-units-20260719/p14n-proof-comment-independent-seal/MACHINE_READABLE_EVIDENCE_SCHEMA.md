# Machine-readable evidence schema

CSV files are UTF-8 comma-delimited tables with one header row and stable
primary IDs in column one. Every record carries authority role, source and
target locators, status, confidence, record revision, continuation cursor, and
revisit condition where applicable. Cells beginning with spreadsheet formula
sigils are forbidden.

JSONL files contain exactly one UTF-8 JSON object per line. Structural records
use stable IDs plus revision-linked record IDs; difficulty records use stable
IDs plus event IDs. Parent and child links, cross-references, supersedes,
superseded_by, and closed_by must close within the unit or use an explicit
INBOUND: or OUTBOUND: prefix.
