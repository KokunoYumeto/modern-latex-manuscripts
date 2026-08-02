# D006 LOGBOOK/STATUS NUL-corruption and recovery control

Date: 2026-08-02

Status: `PASS_CANONICAL_BYTES_RESTORED`

## Adverse disk state

A lightweight byte check found that two D006 control files had become entirely NUL-filled during the PC-instability interval:

- `LOGBOOK.md`: 32,497 bytes, all 32,497 bytes NUL, SHA-256 `E5CCE11415A8E0E9C567864170722790EBE3BA5FD53AE300A5CB02CB84B3F8A7`.
- `STATUS.md`: 4,420 bytes, all 4,420 bytes NUL, SHA-256 `6C26FFDE2BECBC77DDDF0922ACDD1824813188361C908DD251AA8896DB577ED1`.
- Both adverse files had disk timestamp 2026-08-02 15:52:34.

The corruption was detected before any attempted semantic-index append could be applied. No TeX source, PDF, diagram, or semantic CSV was implicated.

## Recovery authority and replay

The recovery authority is the immutable Codex file-change history for task `<REDACTED_TASK_ID>`.

All D006 `add` and `update` patches for the two files were replayed chronologically in memory:

- LOGBOOK changes replayed: 20.
- STATUS changes replayed: 18.
- Patch replay errors: 0.
- Recovered LOGBOOK: 30,929 UTF-8 bytes, matching the known pre-corruption size; historical SHA-256 `C7B1AFA3EA08609D1BF8914025D386F75CD0D05A4942FDF7C980F388F786A487`.
- Recovered STATUS: 3,804 UTF-8 bytes, matching the known pre-corruption size; historical SHA-256 `47E59C765ABE24A6F8DED72AC5DF43956EA12E097A3E399586B1AA05C7FD8D17`.

Exact no-overwrite recovery copies are:

- `LOGBOOK_RECOVERED_FROM_THREAD_HISTORY_20260802.md`
- `STATUS_RECOVERED_FROM_THREAD_HISTORY_20260802.md`

The recovery copies were then hash-verified against both historical identities. Only after that verification, the two NUL-filled canonical paths were replaced from those exact recovered bytes. The restored canonical `LOGBOOK.md` is again 30,929 bytes with SHA-256 `C7B1AFA3EA08609D1BF8914025D386F75CD0D05A4942FDF7C980F388F786A487`; the restored canonical `STATUS.md` is again 3,804 bytes with SHA-256 `47E59C765ABE24A6F8DED72AC5DF43956EA12E097A3E399586B1AA05C7FD8D17`; both have zero NUL bytes. The exact no-overwrite recovery copies remain as durable recovery evidence.
