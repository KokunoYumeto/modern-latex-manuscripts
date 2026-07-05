# CJK Source-Canon Durable Run Log Metadata Bytecount Recheck

Generated: 2026-07-05T15:23:05+02:00

Purpose: record the metadata-only recheck that resolved the remaining sampled bytecount gaps left by the explicit bytecount/upload-policy normalization sidecar.

## Event

- Event id: `CJK-RUNLOG-METADATA-BYTECOUNT-20260705-001`
- Motivation: After explicit bytecount/upload-policy normalization, four source-metadata rows still lacked exact payload-size fields. The next source-canon-first step was a metadata-only GitHub commit/tree recheck for those rows.
- Decision: Recorded GitHub commit/tree API URLs, tree SHA-1s, and blob size fields for the four remaining source-metadata rows without fetching raw source bodies or source archives.
- Row count: 4
- Status counts: `{"metadata_tree_byte_count_resolved": 4}`
- Target/access counts: `{"Japanese": 3, "Korean addendum/source routing": 1}`
- Resolved byte totals: `{"Seasawher/matsumura": "66745", "calofmijuck/algebra": "40047", "imamuray/algebraic-systems": "87773", "t-higashida/commutative_ring_and_field": "3736"}`

## Retained Blockers

- Byte-count metadata is strengthened for sampled blobs, but raw source/archive payloads remain blocked pending owner/B3 license-access review; Korean remains addendum/source-routing only; native/public review and source-canon completion remain unclaimed.

## Boundaries

- Run-log update only; no raw source body/archive fetch, translation, glossary promotion, native/public signoff, canonical approval, license clearance, gate promotion, source-canon completion, Korean-school claim, pan-CJK claim, or Git push.
- This addendum does not mutate earlier packaged durable-run-log files.
