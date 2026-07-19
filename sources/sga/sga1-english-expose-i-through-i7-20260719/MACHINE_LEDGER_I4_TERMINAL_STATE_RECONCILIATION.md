# SGA 1 §I.4 terminal-state reconciliation during §I.7 closure

Date: 2026-07-19

Scope: machine-state reconciliation only. No source reading, English translation, formula, TeX, PDF, build log, or rendered page changed.

The cumulative working difficulty/revision JSONL retained seven obsolete nonterminal §I.4 states even though `SGA1-I4-VERIFY-0001` and later frozen checkpoints had already closed those gates. The independently frozen §I.6 r4 public projection provides the established closure mapping in `ledgers/PUBLIC_SGA1_I4_DIFFICULTY_FAILURE_REVISION.jsonl` (28,189 bytes; SHA-256 `CC3BD371D6EDB089048952704BD8ABD8BA9D8E4DBABC78CDF67B3018C5519769`).

The working ledger now ports only that already-established state linkage:

- `SGA1-I4-FIX-0001`
- `SGA1-I4-FIX-0002`
- `SGA1-I4-REV-0002`
- `SGA1-I4-DEFECT-0001`
- `SGA1-I4-PAGE-0001`
- `SGA1-I4-PAGE-0002`
- `SGA1-I4-TERM-0001`

Each is `closed_corrected` with `closed_by_record_id` equal to `SGA1-I4-VERIFY-0001`; the verifier reciprocally lists all seven in `closes_record_ids`. Their decisions, source locators, target evidence, and revision histories are unchanged.

The reconciled pre-receipt ledger state has 62 records, 108,750 bytes, and SHA-256 `58113CE5565F52AF592FD56E2B4A39A704C32B2A857C8DA78C7C01BC34769252`. A stable reconciliation record is appended after this state, so that digest is an intermediate custody witness rather than the final ledger digest.
