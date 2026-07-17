# Interlanguage Research Department

Current operational research layer, assembled 2026-07-17 from the complete Fable and ChatGPT Pro interlinguistics record.

This department does not own translations. The persistent language-group managers own translation into their languages for **every work** in the corpus, including Noether, SGA, and material not yet in English. This layer supplies the shared linguistic method, evidence rules, mathematical diagnostics, and lane-specific research findings that those managers use.

## Current bottom line

The final reconciliation uses three different objects for three different jobs:

1. A **typed, channel-separated evidence graph** records source -> concept -> form -> evidence -> decision paths. The final packages call this an automaton; operationally it is an automaton-shaped directed acyclic graph.
2. A **weighted rooted family tree** measures branch breadth, dependence, and dominance. Hill numbers and KL divergence describe concentration; edge-coverage phylogenetic diversity describes diminishing returns from related witnesses.
3. A formal **weighted automaton or transducer** is justified only when an extraction or routing process has an input alphabet, states, transitions, initial/final behavior, a semiring, and defined path aggregation. The current evidence packages do not yet implement that full object.

The early “tree, not automaton” objection and the later automaton packages are therefore reconciled, not chosen between. Use the evidence graph for provenance and routing, the family tree for genealogical dependence, and formal automata only if a later extraction system actually defines automaton behavior.

## Mandatory first reads

1. [RESEARCH_AUTHORITY_AND_PROVENANCE.md](RESEARCH_AUTHORITY_AND_PROVENANCE.md)
2. [INTERLINGUISTIC_METHOD_SYNTHESIS.md](INTERLINGUISTIC_METHOD_SYNTHESIS.md)
3. [MATHEMATICAL_OBJECTS_AND_AUDIT.md](MATHEMATICAL_OBJECTS_AND_AUDIT.md)
4. [CLAIM_STATUS_REGISTER.json](CLAIM_STATUS_REGISTER.json)
5. [OPERATIONAL_DECISION_INTERFACE.schema.json](OPERATIONAL_DECISION_INTERFACE.schema.json)
6. The relevant file in [LANE_HANDOFFS](LANE_HANDOFFS)

The latest read-only cross-language table remains:

`C:\Users\Floris\Documents\interlanguage\01_methodology\claude_fable_program\CONSOLIDATED_INTERLANGUAGE_INTERFACE_v1_20260710.html`

Its source JSON preserves 216 concepts, 25 language columns, weight summaries, global-register classes, adverse/competitor mass, F14 trap flags, history descriptions, and reviewed internal decisions. It is an interface, not a certification table.

## Hard boundaries

- `support`, `absence`, `candidate`, `competitor`, `adverse`, and `veto` are separate channels.
- A use weight is not a truth probability.
- A concept-shelf hit is not a row-verified witness.
- A generated translation is never a native-language witness.
- Canonical source-language authority may normalize a source concept but cannot certify target-language usage.
- Internal AI triangulation is quality assurance, not external validation.
- No scalar may auto-promote or auto-reject a term.
- No “readiness” score is accepted without hard source, review, script, adverse-evidence, and human-comprehension gates.
- No current lane has an accepted external/community review return.

## Claim statuses

- `established_arithmetic`: reproducible directly from declared values.
- `measured_corpus_finding`: observed in the frozen corpus or ledger, with stated scope.
- `supported_method`: adopted operational rule supported by the corpus record and/or established method.
- `exploratory_proxy`: useful for ranking or diagnosis, not a decision or validation measure.
- `proposed_unimplemented`: theoretically specified but not run on this corpus.
- `descriptive_only`: retained as description after weak predictive performance.
- `withdrawn`: explicitly retracted and prohibited from current use.
- `rejected_as_decision_measure`: may remain as archaeology but must not drive decisions.

## Reproducibility

Run:

```powershell
python 01_methodology/research_department/tools/audit_existing_packages.py
```

The audit re-computes the final Interslavic State C and W0 branch statistics, checks edge and row counts, detects the unified package’s mislabeled readiness formula, and records provenance caveats. Its generated report is written to `audit_outputs/AUDIT_RESULTS.json`.

## Manager handoffs

The eight handoffs correspond to the persistent management tasks, not to individual works:

- Slavic / Interslavic
- Chinese, Japanese, and Korean local standards
- Spanish, French, and Romance
- English and Germanic
- Turkic
- Arabic, Persianate, and RTL
- Malay, Southeast Asian, and Pacific
- Horn of Africa and West Africa

Every manager remains responsible for translating any work into its target languages and maintaining its source corpus, examples, concept web, script/register policy, and decision trail.
