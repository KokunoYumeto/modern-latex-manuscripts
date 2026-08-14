# Evidence and maintenance method

## Authority and ownership

The sidecar reads translation projects but never edits them. The evidence schema classifies a source as `official_standard`, `official_guidance`, `professional_reference`, `project_artifact`, `checker_artifact`, `candidate_crosswalk`, or `computation`. Professional-society dictionaries are references, not government standards. Mutability is an admission/state property rather than a source class: a mutable head is excluded from authority unless captured as an exact observation, and it is never substituted for a cited closed identity. Adverse history is represented by an `adverse_support` evidence record plus `adverse.tsv`.

One language cannot authorize another. A Chinese/Japanese/Korean comparison becomes shared only when it concerns language-neutral structure or when each named locale has its own evidence.

## Intake loop

1. Bind exact artifact, version, bytes, SHA-256, and stable locus.
2. Classify the claim before interpreting it: source fact, computation, editorial inference, project decision, or external validation.
3. Separate support, candidate, competitor, adverse, absence, and veto.
4. Record sense window, excluded senses, uncertainty, and qualitative dominance risk.
5. Recompute mechanical claims independently.
6. Add the smallest rule supported by the evidence; do not generalize across languages or regions.
7. Preserve corrections append-only and record supersession.

The project does not use a scalar readiness score. Publication is permitted after its declared machine checks pass. Human/community review is optional, nonblocking evidence; no external certification is claimed unless it actually exists.

## Formula projection

For each stable formula ID, parse or tokenize enough structure to compare:

- control sequence and alphabet family;
- ordered operands and relation/operator;
- nested groups and delimiter pairs;
- left/right scripts, primes, bars, inverse images, and quantifiers;
- equation label and punctuation association.

Counts are diagnostics only. A missing obligation, undeclared target repeat, or unexpected tree delta fails closed. Known source defects use an explicit corrected-source layer; source bytes are not silently changed.

## Text projection

Protect TeX controls and symbolic math while exposing `\text`, `\mbox`, `\hbox`, and other prose-bearing subspans to the locale adapter. Delimiter recognition counts preceding backslashes. Text normalization is strict UTF-8 plus NFC only.

Locale adapters supply terminology, morphology, script, spacing, punctuation, names, and font behavior. They must accept “unknown/unsupported” rather than inheriting a neighboring language's form.

## Build projection

The reproducible gate records engine/font/input identities, serial pass hashes, log diagnostics, PDF structure, font/ToUnicode inventory, independent extractions, and page renders. CMap injection is allowed only as the missing-only, invariant-preserving repair described in the standard.

## Public update rule

Every component release contains the human standard, typed evidence, adverse ledger, schema, sources, rights, citation metadata, manifest, and verifier. This component is deposited additively in the existing Interlanguage methodology concept; it does not create a competing concept DOI. A published containing-record version is immutable, and corrections use another version. GitHub and Zenodo readbacks must match the local manifest before the component is declared published.

## Adoption output

An adopting lane emits the independent state vector defined by `report.schema.json`; it never emits one aggregate readiness score. Sanitization is split into a shared byte/TeX layer and a locale layer. Shared processing handles UTF-8, NFC, LF, exact paths, controls, formula structure, and nested prose discovery. Locale processing alone handles terminology, grammar, morphology, punctuation, and script, with exact precondition counts and invariant formula/control streams.

`tests.json` is the minimum reusable fixture set. A lane adds its own language-specific fixtures without changing another lane's profile or treating comparison candidates as authority.
