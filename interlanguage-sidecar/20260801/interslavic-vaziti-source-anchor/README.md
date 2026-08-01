# Interslavic `važiti` mathematical-sense source anchor

## Purpose

The public Interslavic normalization checkpoint reports 353 `važi*` / `važe*`
probes in 101 files. The corpus uses this family for mathematical English such
as "holds", "applies", or "is valid". That family was left unchanged because
the earlier review did not have enough external language authority for a
corpus-wide semantic decision.

This packet records a narrow check against the current source data of the
Interslavic Dictionary. It is a source anchor, not a corpus rewrite.

## Dictionary evidence

- Repository: <https://github.com/sonic16x/interslavic>
- Exact commit: `0fab0c5b4463118d46b1cdcd506926d8848052c9`
- Commit date: 2026-03-28
- Source file: `src/services/dictionary-test/basic.json`
- Source blob SHA-1: `d630e808167ed1baceeca47e210197186eadb60c`
- Downloaded source-file bytes: 23,237,295
- Downloaded source-file SHA-256:
  `738038CF6038B9CFD27C93CAA4BB5C7472917777049B49CE8EB9422DAA72A9A8`
- Dictionary rows checked: 18,464

At that commit, dictionary row `6005` gives `važiti` only as the transitive
imperfective verb "weigh, balance". No English gloss in the 18,464-row source
contains `valid`, `applicable`, or an abstract mathematical "holds" sense for
`važiti`.

The same dictionary separately gives:

- `priměnjati` / `priměniti`: "apply (method, rule), employ (use)";
- `dŕžati`: "hold, keep";
- `pravdivy`: "real, true, genuine, truthful";
- `praviľny`: "correct, proper, accurate".

The exact relevant rows are preserved in
`INTERSLAVIC_DICTIONARY_RELEVANT_ROWS_20260801.csv`.

## Disposition

This evidence does **not** authorize a blind replacement. A single substitute
would not fit every one of the 353 contexts, and the dictionary does not itself
prescribe a general mathematical equivalent of English "holds/is valid".

The existing corpus therefore remains byte-unchanged. The blocker is narrowed
as follows:

1. The mathematical extension of `važiti` is not supported by the checked
   dictionary source.
2. `priměnjati` / `priměniti` are dictionary-backed where a method or rule is
   explicitly being applied.
3. Other contexts still require sentence-level linguistic or community
   adjudication before any normalization tranche.

## Claim boundary

This packet documents one dictionary snapshot and one conservative corpus
decision. It is not community certification, a complete Interslavic style
guide, or proof that every current `važi*` / `važe*` occurrence is wrong. The
dictionary application states that its word stock derives from Jan van
Steenbergen's Interslavic materials; the repository reports an MIT software
license, but this packet makes no broader rights inference about lexicographic
content.
