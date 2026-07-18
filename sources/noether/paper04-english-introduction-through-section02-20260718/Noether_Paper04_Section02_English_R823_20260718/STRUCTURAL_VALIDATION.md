# Structural validation

`STRUCTURAL_INDEX.jsonl` contains 13 append-only records resolving to 11 active stable units. Two revision chains are present: the section-wide closure and the corrected prose-unit hierarchy. Both chains are explicit and consecutive.

Validation completed:

- every JSON line parses;
- all required structural fields are present;
- every active child ID resolves;
- each active child points back to the parent that lists it;
- all difficulty-ledger unit IDs resolve to active structural units;
- issue IDs are unique and closure references resolve backward;
- `N04-S02-P03` and `N04-S02-EQ07` are now direct sibling children of the section, matching the equation's parent and the section's ordered child list;
- external cross-references are retained as declared outbound references and are not falsely treated as package-local nodes.

Result: 13 structural records, 11 active units, 7 difficulty records, zero parse, schema, revision, ID, hierarchy, or closure-reference failures.

Structural index SHA-256: `75A339F6FE967723D2177CEF57E9BA0D8284C514BE45C12E86BB8D00D321B962`.

Difficulty ledger SHA-256: `AE0D4FA6E001BED0EFF0A0758F411E404903C052F4C5746A5ED8D18E286A7E86`.
