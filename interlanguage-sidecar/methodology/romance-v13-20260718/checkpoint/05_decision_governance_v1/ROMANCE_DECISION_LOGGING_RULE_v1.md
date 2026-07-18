# Romance decision-logging rule v1

Status: active lane governance. This rule applies to corpus/provenance, branch routing, WordWeb semantics, access/MII, controlled-language construction, source translation, QA gates, and publication handoffs.

## Required record

Every material decision must be entered in `ROMANCE_DECISION_LEDGER_v1.jsonl` when it is made. A material decision includes every:

- source admission, rejection, quarantine, alias, deduplication, variety, domain, rights, or coverage classification;
- sense split, sense link, support/adverse/held classification, relation edge, candidate form, promotion, or unresolved-gap decision;
- cohort, penalty, proxy, human-evidence, pilot, or intelligibility decision;
- lexical, grammatical, orthographic, register, translation, clause-alignment, or anti-collapse choice;
- build, render, validation, acceptance-gate, checkpoint, supersession, or public-payload choice.

Routine commands do not need duplicate prose entries when their exact invocation and result are already preserved in a build or validation log. Any judgment that determines what the command means, admits an artifact, changes a claim, or selects between alternatives does require a decision entry.

Each entry must preserve:

1. the decision and selected option;
2. the alternatives actually considered;
3. the evidence used and its limitations;
4. the motivation/rationale;
5. uncertainty and adverse evidence;
6. expected consequences and claim boundary;
7. review status and revisit condition;
8. a reflection stating what the decision solved, what it did not solve, and what later evidence could reverse it;
9. related artifact paths or identifiers.

Backfilled entries must say that they are backfills and must not invent exact decision times. Corrections append a new entry that names the superseded decision; prior entries are never silently rewritten or deleted. Human validation, native review, pilot data, and empirical intelligibility remain distinct evidence classes and may not be inferred from machine checks or orthographic proxies.

## Maintenance

`validate_romance_decision_ledger.py` checks JSON syntax, unique IDs, required fields, alternative/evidence/reflection presence, review states, and explicit public-claim boundaries. The next successor manager control plane and top-level acceptance gate must bind the rule, ledger, validator, and validation report by SHA-256. A green lane gate is invalid if these decision-control artifacts have drifted or are omitted.

