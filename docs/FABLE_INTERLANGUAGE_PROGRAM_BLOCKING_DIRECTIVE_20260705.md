# Historical Fable Interlanguage Intake Directive

Date: 2026-07-05
Historical scope: interlanguage, Interslavic, Slavic, Romance, Persian/Farsi,
Turkic, CJK, and constructed/bridge-language source intake.
Status: preserved 2026-07-05 coordination history; not active contributor
guidance. Use the current adoption board and repository intake forms instead.

This directive accompanied `UPLOAD_ALL_LATEX_SOURCE_BODIES_NOW_20260705.md` at
that historical generation. The durable rule is to preserve real source bodies,
their exact provenance, and their relation to generated methodology artifacts.

## Immediate rule

At that generation, each related push was expected to include an acknowledgement file named:

`FABLE_REQUIREMENTS_ACKNOWLEDGED_YYYYMMDD.md`

That acknowledgement must explicitly say which of the requirements below were satisfied, which were not yet satisfied, and where the produced files live. A vague status note, index, or summary is not enough.

The acknowledgement recorded which requirements were satisfied and which source bodies remained missing. Current contributions use the repository's issue and pull-request contracts instead.

## Fable artifacts to read and preserve

The historical Fable program is preserved through its exact GitHub and external
record identities. Its minimum control artifacts were:

- `PROGRAM.md`
- `AUTHORSHIP.md`
- `HEURISTIC_REGISTER.md`
- `BRANCH_WEIGHTING_SPEC.md`
- `BRANCH_WEIGHTING_SPEC_FOR_CHATGPT.md`
- `CLAIM_LEDGER.md`
- `COMPLETENESS_STATE_20260704.md`
- `CONCORDANCE.md`
- `SOURCE_USE_POLICY.md`
- `INTERSLAVIC_GATE_MAP.md`
- `SITING_TABLE_v1.md`
- `INTERLINGUAL_CONCEPT_LEDGER_20260704.csv/json/md`
- `UNION_TERM_SPINE_20260704.md/json`
- `UNION_TERM_SPINE_v2_WITH_SLAVIC.csv/json`
- `INTERSLAVIC_LEDGER_RETROFIT_20260704.csv/json`
- `DO_NOT_USE_LEDGER_20260704.md/json`
- `NORMALIZATION_DECISION_TABLE_v1_20260704.md/json`
- `REGISTER_DOUBLET_BRANCH_EVIDENCE_v1/v2`
- `F10_EAST_SLAVIC_SKEW_AUDIT_20260704.md/json`
- `F7_FRENCH_INTERLOCK_NOTE_20260704.md`
- `V3_DEFECT_REPORT_FOR_CHATGPT_20260704.md`
- `V4_DEFECT_REPORT_AND_HANDOFF_FOR_CHATGPT_20260704.md`
- Any file or note whose name contains `Fable`, `F7`, `F10`, `F11`, `F12`, `F13`, `G15`, `15G`, `branch`, `weight`, `marginal`, `witness`, or `heuristic`.

If `G15` / `15G` is absent from a bounded intake, record the searched source identity and continue with the rest of the program; do not silently ignore the reference.

## Correct formal object

Do not reduce this to a loose prose summary. Build the actual data structures.

Fable's correction is important: the immediate object is a `weighted rooted-tree witness measure` / `branch-weight witness ledger`. Weighted automata, weighted tree automata, formal power series, and semiring language are supporting theory; do not use them as decorative labels if the implemented object is the rooted-family witness ledger.

The required formal/practical layer is:

1. A family tree or branch map for every language family currently touched.
2. A per-language source index.
3. A per-word/per-concept interlanguage index.
4. A branch-weight witness ledger.
5. A marginal intelligibility ledger.
6. A dominance-collapse/adverse-evidence ledger.
7. A source-use ledger distinguishing source witness, generated draft, consistency shelf, and non-witness material.

## Required ledgers

Produce these as CSV plus JSON/JSONL when possible:

- `languages.csv`: language code, name, family, branch, script, region, source-count, TeX-count, PDF-count, native-source status.
- `source_documents.csv`: every source document as-is; path, language, branch, file type, provenance URL/path, hash, license/availability note if known, witness category.
- `lexemes.jsonl`: every concept/word/term row; stable ID, gloss, domain, source spine, target bridge lane.
- `forms.csv`: lexeme ID, language, branch, script, source form, normalized form, source document, source location, witness category.
- `word_weights.csv`: lexeme ID, candidate bridge form, supporting forms, adverse forms, false-friend notes, branch weights, marginal intelligibility score, dominance penalty, final status.
- `branch_weight_ledger.csv`: raw witness counts, capped/log counts, equal-splits/phylogenetic down-weighting, effective branch number D, KL/skew from target, notes.
- `marginal_intelligibility.csv`: candidate form, dominant-baseline access, non-dominant access gain, loss/confusion cost, false-friend risk, accept/review/reject status.
- `do_not_use.csv`: false friends, bad glosses, contaminated label rows, source-channel errors, and terms explicitly rejected.
- `rules_acknowledgement.md`: explicit checklist that names each rule here and says done/not-done with paths.

## Heuristics that must be operational, not merely mentioned

Implement the Fable/ChatGPT heuristics as actual ledger fields or audit checks:

- Dense branch points: prefer forms with broad recognizability and low semantic drift.
- Marginal intelligibility: a candidate must add access beyond the dominant-language baseline.
- Non-dominance: reject collapse into softened Spanish, rough Russian, or any other dominant standard when it adds little access elsewhere.
- Global-not-Eurocentric: do not treat Greco-Latin academic vocabulary as automatically global.
- Passive recognizability first, active learnability second.
- Internationalisms only when they reduce ambiguity more than they add opacity.
- Source format is not a gate: LaTeX is preferred where available, but PDF/DOC/archive cultures still count if source discipline is maintained.
- Voting-machine / regularized barycenter: branch fairness matters more than raw source count.
- Threshold gates: below threshold, mark exploratory; do not promote to source-canon.
- Invariant ledgers: specify what survives script conversion, register shift, bridge mapping, and paraphrase.
- Few-shot thin rows: use reconstruction only when flagged as reconstruction, never as attestation.
- Eponym/symbol split: eponyms and symbols transfer differently from common proof prose.

## Required source-body behavior

The source-canon corpus still has to be uploaded as the whole corpus as-is. Do not upload only indexes, counts, manifests, or summaries.

For each language touched, upload every source file available:

- `.tex`, `.ltx`, `.sty`, `.cls`, `.bib`, `.bbl`, `.dtx`, `.ins`
- diagrams and assets needed to compile
- PDFs and source archives when available
- repo snapshots or ZIP/TAR payloads when the corpus is large

Large size is not an objection. Split into multiple ZIPs if necessary. Preserve directory structure. Include hashes. Do not flatten the corpus into cherry-picked examples.

## Language scope

This applies to all touched languages and families, including but not limited to:

- Interslavic
- Ukrainian
- Russian
- Belarusian
- Polish
- Czech
- Slovak
- Slovenian
- Croatian
- Serbian
- Bulgarian
- Macedonian
- Pan-Romance / Romance sources
- Persian/Farsi
- Turkic lanes
- CJK lanes
- any later interlanguage or controlled-register lane

For Persian/Farsi and other non-Slavic lanes: prioritize actual source corpus, source indexing, lexeme/form extraction, and translation work over more meta-planning. If the source corpus is thin, mark it thin and continue source intake; do not invent witness status.

## Public archive boundary

Generated translations, proposed interlanguage forms, and AI-derived consistency ledgers are useful, but they are not native source witnesses. Public metadata must say so clearly.

Use these categories:

- `source-witness`: native/source material used as evidence.
- `generated-draft`: AI-produced translation or interlanguage proposal.
- `consistency-shelf`: useful for internal comparison, not an independent witness.
- `audit-ledger`: human/machine-readable status and defect tracking.
- `methodology`: workflow/reflection artifact.

## Historical continuation action

1. Pull latest `main`.
2. Read this directive.
3. Read the Fable artifacts listed above.
4. Upload/push the full raw source corpora as-is, not summaries.
5. Produce the per-language and per-word ledgers listed above.
6. Commit `FABLE_REQUIREMENTS_ACKNOWLEDGED_YYYYMMDD.md` with exact paths and remaining gaps.
7. If any required corpus is not available on that PC, state the exact missing corpus and where it must be copied from.
