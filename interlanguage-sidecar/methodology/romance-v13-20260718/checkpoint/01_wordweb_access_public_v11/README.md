# Romance WordWeb and marginal-access checkpoint v11

This is a public-safe projection of the internal v11 Romance semantic and access artifacts. It contains 60 concepts, 106 explicit senses, 39 extension nodes, 811 metadata-only evidence records, 106 provisional construction decisions, nine named reader cohorts, and the complete 954-row sense-by-cohort access grid.

It deliberately excludes source quotations, source locators, host paths, raw source bodies, and extension-node context snippets. Those materials remain internal because source-body reuse rights are unresolved or not publication-cleared. Evidence IDs, source hashes where available, classifications, and review notes are retained so that the semantic audit surface does not collapse into an unsupported vocabulary list.

The acceptance boundary is strict: 78 senses have accepted internal source support; 28 are explicit gaps. The 120 inherited Spanish/French core records still have zero quotations and remain unresolved. The grid has zero human observations, zero pilot-eligible rows, and zero form promotions. Orthographic values are design diagnostics only; they are not marginal-intelligibility or comprehension measurements.

The graph boundary is equally strict: 406 relation records are present, but only 27 have valid target IDs. With 106 concept-to-sense memberships, there are 133 ID-resolved references—not 406 graph edges.

## Contents

- `data/PAN_ROMANCE_WORDWEB_PUBLIC_v11.json`: semantic structure, evidence metadata, relations, and provisional decisions.
- `data/PAN_ROMANCE_ACCESS_LEDGER_PUBLIC_v11.json` and `.csv`: the complete 106 × 9 design grid.
- `data/ROMANCE_READER_COHORTS_v2.csv`: the canonical nine-cohort topology.
- `data/WORDWEB_UNRESOLVED_SENSE_GAPS_v11.csv`: the 28-sense open-evidence cursor.
- `method/MII_METHOD_PUBLIC_v11.md`: formula, cohort, evidence, and human-study gates.
- `PROVENANCE_INPUT_HASHES.json`: exact binding to the four internal v11 inputs without exposing them.
- `qa/`: deterministic validation and build evidence, added by the reproduction runner.
- `scripts/`: builder, validator, and reproduction runner.

This checkpoint is active evidence, not a complete Romance interlanguage, not an empirical MII result, and not a declaration of license for any underlying source body. Package licensing and public repository placement remain decisions for the archive maintainer.
