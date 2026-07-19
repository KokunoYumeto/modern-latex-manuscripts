# SGA 1 source check — duplicate-numbered I.9.2 pair

State: locally source/build/render/anchor/machine sealed after independent
final review. This document does not claim public freeze, publication, or
complete SGA 1 coverage.

## Authority and boundary

- Sole text authority: corrected French arXiv `math/0206203v2` TeX,
  `smf_doc-math_3_01.tex`, 1,094,587 bytes, SHA-256
  `754E9FD6BC04BA52359D0CF4102AA01D2805A00B0E3E298CCD7396564CC7702D`.
- Driver: `sga1-smf.tex`, 3,312 bytes, SHA-256
  `DB1CFDFC8356CA532415EDBE7A2147CB1F078569FAD7BC6ABBF5C6E4A1928B31`;
  `orig=false`.
- Statement body and numbering apparatus: lines 1704--1720, 17 LF lines /
  538 bytes, SHA-256
  `A561F19005B1040B3B2C12C7FBD9EC20B7EB761D8AEBC331647E5B1170ED9562`.
- Structural envelope through blank line 1721: 18 LF lines / 539 bytes,
  SHA-256
  `55F044CF7103997F3B2705898EAAF4CBDD40B4551C44A1A10C3C5509AE1D5980`.
- Exact excluded cursor: substantive line 1722, `Cela \'equivaut au`, 19
  bytes, SHA-256
  `50DC75EA126D97F233DCA54B8E8DE47B2BB2E4ADF795965DCDF362804F05D174`.

The unit is statement-complete but proof-deferred: line 1722 begins the
equivalence with Corollary I.9.3 and the ensuing proof lies outside.

## Source decisions

- Corollary I.9.2 retains the unconditional implication from regular `Y` to
  regular `X`, with its converse conditioned on surjective `f`.
- The corrected branch at line 1708 selects French `surjectif`; original
  `surjective` is a source-language gender defect. Both map to English
  `surjective`, so no target semantic difference was invented.
- Lines 1712--1713 explicitly record the original duplicate number 9.2 and
  reset the theorem counter. The target maps that reset to the shared
  proposition counter, keeps distinct TeX labels `I.9.2` and `prop:I.9.2`,
  and gives readers a visible editorial note. A scoped `\theHproposition`
  override gives the second statement the unique internal destination
  `proposition.1.9.2.second` while leaving its visible number I.9.2.
- Proposition I.9.2 retains the unconditional implication from reduced `Y`
  to reduced `X`, with its converse conditioned on surjective `f`.

Rejected forms include `reciprocal`, `onto`, a compressed iff formulation,
merging the two statements, silently renumbering the proposition I.9.3,
hiding the duplication only in a source comment, and starting the successor
at line 1723. The first isolated visible-success build, r3, is also rejected:
its pass-two and pass-three logs disclosed a duplicate
`proposition.1.9.2` PDF destination. The repaired r4 successor retains the
same rendered pages with distinct internal destinations.

## Page and candidate controls

Direct visual controls are recorded in
`SOURCE_PAGE_AND_NUMBERING_CHECK_I_9_2_20260719.md`: original print physical
PDF page 33 / printed page 16; corrected v2 physical page 30 / footer 14; and
orig-true physical page 27 / footer 14. All visibly corroborate the duplicate
number. Scan/PDF controls are locators only and remain outside public payloads.

English comparison has only two effective lineages: Hosgood/Thosgood and the
Reinhold LLM candidate. `jmoellermath` has no I.9 body; the inherited TeX is a
stale Reinhold conversion. Agreement is therefore not source evidence.

## Target

- Fragment: `drafts/SGA1_I_9_2_English_source_draft.texfrag`.
- 1,370 bytes; SHA-256
  `510FB1A44CAE30C12ADDB0046EB31B232A93550493A00405CBDF4C7AF3395579`.
- Cumulative TeX: 18,833 bytes; SHA-256
  `7C7FD36084FF4891F943508620D20A91BCDE669114C3C149FADF99E1B95F23B2`.

Machine detail is in `SOURCE_COMPARISON_I_9_2.csv`,
`SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_9_2.csv`,
`SGA1_I9_2_EVIDENCE_GRAPH.jsonl`, and the cumulative adverse,
normalization, and difficulty/revision ledgers.
