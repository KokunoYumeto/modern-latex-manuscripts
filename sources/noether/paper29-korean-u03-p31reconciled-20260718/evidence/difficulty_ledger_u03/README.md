# P29-KO-U03 append-only difficulty ledger

DIFFICULTY_LEDGER.jsonl is the canonical immutable hash-chained record of hard units, failed paths, corrections, and held risks. The CSV is a generated projection. The initializer refuses to overwrite a non-identical existing prefix. Later corrections must append a new chained record; they must never rewrite an earlier record.

The schema and validator check every record and the complete chain. Resolved entries remain evidence. Internal validation does not constitute external or human review.
