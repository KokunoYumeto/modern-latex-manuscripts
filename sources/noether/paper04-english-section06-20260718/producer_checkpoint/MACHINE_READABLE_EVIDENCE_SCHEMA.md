# Machine-readable evidence contract

This checkpoint follows the machine-readable evidence contract stated below.

- CSV files are strict UTF-8, rectangular, and have exact declared headers. The first field is a stable ID; revisions are positive integers; status is explicit. Cells must not begin with spreadsheet formula-injection characters.
- JSONL files contain one object per nonblank line, have no duplicate keys, and preserve stable IDs and append-only revisions.
- Source, formula, terminology, adverse-witness, structural, difficulty/failure, control, build, render, and artifact-receipt evidence remain distinct.
- R823 is editable textual authority; the original 1911 print adjudicates historical readings and source defects; inherited English is comparison-only.
- A `PASS` means the named mechanical or bounded review gate passed. It does not mean mathematical certification, critical editing, independent human review, rights clearance, or publication readiness.
