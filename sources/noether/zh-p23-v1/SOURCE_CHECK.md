# Source check

Internal source reconciliation covers `NOE-P23-U00` through `U07` in `SOURCE_UNIT_MAP.csv`.

- Source/Hans/Hant emphasis loci: 27 / 27 / 27.
- Hans/Hant ordered math spans: 124 / 124; canonical sequences identical after removing CJK text and whitespace.
- Primed sums: 3 / 3.
- `g(y,d y)` loci: 2 / 2.
- Numbered displays: 5 / 5.
- Superseded `\varphi` and custom `\dd`: zero.
- All six prohibited uncontrolled Hant variants (`箇`, `衆`, `纔`, `裏`, `爲`, `羣`): zero.
- Eight typed decisions validate with zero errors against `OPERATIONAL_DECISION_INTERFACE.schema.json`.

`qa/FREEZE_VALIDATION_REPORT.json` is the machine-readable check authority. Exact phrase-by-phrase external review remains absent; equality of counts is not represented as independent semantic certification.
