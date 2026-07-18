# Structural validation

`STRUCTURAL_INDEX.jsonl` contains 10 append-only revision-1 records resolving to 10 active stable units. Every record has explicit `record_revision: 1` and `supersedes: null`; no later revision chain is present.

Validation completed:

- every JSON line parses and all required structural fields are present;
- stable unit IDs are unique;
- every package-local child ID resolves;
- each package-local child points back to the parent that lists it;
- all seven difficulty-ledger records have explicit revision and null-supersession fields, and their unit IDs resolve to active structural units;
- difficulty issue IDs are unique and the closure reference resolves backward;
- R823 line spans and printed-page spans stay inside the declared section envelope;
- section 4 and earlier-section references are retained as declared outbound references rather than false package-local nodes;
- all 10 source-alignment rows resolve to active structural units.

Result: 10 structural records, 10 active units, 7 difficulty records, 10 source-alignment rows, and zero parse, schema, ID, hierarchy, closure-reference, or bounded-coverage failures.
