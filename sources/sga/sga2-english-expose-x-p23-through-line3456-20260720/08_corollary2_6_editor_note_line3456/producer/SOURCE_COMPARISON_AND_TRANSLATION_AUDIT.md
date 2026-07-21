# SGA2 Expose X, Corollary 2.6, editor's note (3): source and translation audit

Status: producer source-check pass; fresh independent review not yet performed.
Release state: `internal_not_for_release`. The French authority remains
byte-identical.

## Boundary and authority

- Unit: corrected French TeX line 3456 only, the complete `\ndetext{...}`
  editor's note (3).
- Authority: `smf_doc-math_4_01.tex`, 586,789 bytes, SHA-256
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Exact no-EOL UTF-8 replay: 2,145 bytes, SHA-256
  `C5F8286F8A860C2BA1F892B9CBAEF882C810C72AADB23BFAA2667B86EF9A3581`.
- Exact CRLF replay: 2,147 bytes, SHA-256
  `694B4AE97FB45D030BE47C59D4DD1F28C359109855379B731DB8D379E1744A86`.
- Blank line 3457 is excluded. Raw continuation cursor: 3457. Next
  substantive cursor: 3458, the opening of Section 3.
- Locators are distinct: original printed pp. 117--118; physical source-PDF
  pp. 101--102; recomposed running pp. 93--94. No `\pageoriginale` marker
  occurs inside line 3456.
- The 216-page same-edition reader (SHA-256
  `41AD02C57321A8D2200FF32A929BC93ADBC3DE0D59DCD5A284D28D859FB87A90`)
  is manifestation and layout evidence only, not independent original-print
  corroboration.
- Both source-page renders were inspected at original detail and retained:
  physical 101, SHA-256
  `E59A5DADE48D40EA47B11A4747A72A21ABA090FA09F697F403FC5B4ACD0FB793`;
  physical 102, SHA-256
  `70EA3E1FBDB313FDD2F832170D35457AA0BA38A2F1E93FF61C12F99411B813E3`.
  They are internal rights-gated QA evidence, not proposed public files.

## Sentence-by-sentence source/candidate/target comparison

The external candidate is current jcreinhold Markdown, 31,425 bytes, SHA-256
`2BDDBC3D15EECE7A47FDBDFBE31DAE735446BC14480A75113E704F63901C7BF5`.
Its Corollary 2.6 body calls `[^N.D.E-X-3]` at line 256, and its complete note
is present at lines 541--559. It is comparison-only and is not an independent
source witness.

| Segment | French control | Candidate disposition | Source-aligned target disposition |
|---|---|---|---|
| S1 | Combined with X.3.3 and criteria XII.2.4 and XII.3.4, one obtains a relative Lefschetz theorem. | Retains the claim but drops both `XII` prefixes. | Retains Proposition 3.3 and both cross-volume prefixes. |
| S2 | Projective flat `f:X->S`; connected noetherian schemes; effective relatively ample relative Cartier divisor `D`. | Substantively aligned. | Uses project-standard lowercase `noetherian`, `projective and flat`, and `on X`; no mathematical change. |
| S3 | Fiber depth at closed points at least 2 implies connected `D` and surjective `i_U`. | Substantively aligned. | Preserves the depth threshold, quantifiers, connectedness, and map direction. |
| S4 | Fiber depth along closed points of `D_s` at least 3 plus pure local rings (e.g. complete intersections) implies `i_X` is an isomorphism. | Substantively aligned. | Preserves the stronger depth threshold, purity hypothesis, example, and conclusion. |
| S5 | Bost citation, title, journal, volume, pages, and Theorems 1.1 and 2.1. | Retained. | Retained, with ordinary English bibliographic punctuation only. |
| S6 | For a merely smooth geometrically connected projective surface, connectedness and surjectivity hold when `D` is only nef with square greater than 0. | Uses “simply,” which can suggest “simply connected.” | Uses “merely”; retains connectedness, surjectivity, nefness, positive self-intersection, and Theorems 2.3/2.4. |
| S7 | Arithmetic surface over `O_K`; Bost improves Ihara; a positive section point makes the projection-induced map invertible with inverse induced by `P`. | Complete, but says “was invertible with inverse.” | Says the first map is an isomorphism whose inverse is the oppositely directed map induced by `P`; preserves titles and references. |

No omission adverse ID is created: the candidate contains the full note.

## Formula, symbol, and map-direction audit

| Stable check | Source | Target | Result |
|---|---|---|---|
| `MAP-IU-001` | `i_U: pi_1(D) -> pi_1(U)` | same direction, explicitly displayed | pass |
| `MAP-IX-002` | `i_X` is an isomorphism | same special-case map and conclusion | pass |
| `MAP-SURFACE-003` | `pi_1(D) -> pi_1(U)` | same direction, explicitly displayed | pass |
| `MAP-PROJECTION-004` | `pi_1(X) -> pi_1(Spec O_K)` induced by projection | same direction and inducing datum | pass |
| `MAP-SECTION-005` | `pi_1(Spec O_K) -> pi_1(X)` induced by `P` | same inverse direction and inducing datum | pass |
| `DEPTH-006` | `depth(X_s) >= 2` at every closed point | same quantifier and threshold | pass |
| `DEPTH-007` | `depth(X_s) >= 3` at closed points of `D_s` | same locus and threshold | pass |
| `POSITIVITY-008` | `D` nef with square `>0` | `D` nef with self-intersection `>0` | pass; explicit English mathematical register |

The five fundamental-group map occurrences are all retained. The first and
third have the same direction but occur under different hypotheses; they were
checked separately. No formula or symbol ambiguity remains.

## Cross-reference and bibliography controls

- X.3.3 resolves to Proposition 3.3, verified from authority lines 3476--3478,
  SHA-256 `DEF682AC4249F1CEA33072025BA8FF37084AFA0DD31CB809FD7E913506C89C23`.
- X.3.4 resolves to the purity theorem, verified from lines 3482--3490,
  SHA-256 `9CA39625788C11C05F6580B3AA383E92069B419EA8DFD0EA9FC98C697A63AD12`.
- XII.2.4 resolves to Corollary 2.4, verified from lines 4141--4148,
  SHA-256 `B74BCCB29ECEFAF4A5953FB688F142597D5980146395B1D4A1DA3A52984F63BA`.
- XII.3.4 resolves to Corollary 3.4, verified from lines 4278--4290,
  SHA-256 `EB18BCEED21D1DA8566C0352510A68AE9EAB6924CED8A9C88AF8E0CBE4ABBB9F`.
- The Bost and Ihara titles, publication data, theorem numbers, and corollary
  number are retained from the French authority. They were not replaced by
  candidate wording or silently bibliographically emended.
- Within the source sentence, the later `loc. cit., Corollary 7.2` and
  `loc. cit., Theorem 1.2` refer back to the Bost article; the target preserves
  that structure. No unresolved reference ambiguity was found.

## Accepted normalization and rejected comparison choices

- `SGA2-X-L3456-AU-DESSUS-NORMALIZATION-001@1` (accepted): corrected source
  mode selects `au-dessus` from `\sisi{au dessus}{au-dessus}`; target “over.”
  This is an explicit source normalization, not a source defect.
- `SGA2-X-L3456-JCREINHOLD-XII-PREFIX-REJECT-001@1` (rejected): candidate
  “criteria 2.4 and 3.4” loses the authority's two `XII` prefixes.
- `SGA2-X-L3456-JCREINHOLD-SIMPLY-REJECT-001@1` (rejected): candidate
  “simply a ... surface” risks the technical reading “simply connected”;
  target “merely” preserves the discourse sense.
- `SGA2-X-L3456-JCREINHOLD-INVERTIBLE-PHRASE-REJECT-001@1` (rejected):
  candidate “was invertible with inverse” is replaced by “is an isomorphism
  whose inverse is,” without changing either map direction.
- Lowercase `noetherian` follows the established SGA English lane register.
- “Map” replaces literal French `fleche`; “effective relative Cartier divisor
  on X” follows standard English mathematical register. Neither is a source
  emendation.

## Build, extraction, and visual QA

- Target TeX: 3,730 bytes, SHA-256
  `9D0A5373889DB323F804DA0C21A22405E93988743E310D1328C0E31F6356EDD5`.
- Clean pass 1: 7,463 bytes, SHA-256
  `694C0BF3409DB9C7E69708752F4E37688E7296CB50AF6A5F485B7BE47B2A406B`;
  only the expected first-pass `rerunfilecheck` warning.
- Clean passes 2 and 3: 7,347 bytes each, identical SHA-256
  `EF5BA1AF494161B566CB1112DDEE657447262B4D2627BCED0F7623CD23B1F237`;
  no warnings or errors.
- Target PDF: one A4 page, 275,147 bytes, SHA-256
  `33B82F41791672BA26C0237A25B2A8D9B8807AE38C9060B66943A021887D1B0C`.
- Extracted text: 3,172 bytes, SHA-256
  `080D6C1021C2EC081DCD3F09D4E50CD14A9E2AFCAED326637D086DBB41F5A663`.
- Fourteen font rows are embedded, subsetted, and Unicode-mapped.
- Target render at 200 dpi: 419,804 bytes, SHA-256
  `BBC2E912CFA9BCC0B255FE4B6807978F8868D2EEF9A2C72E0790571E80BC5BB5`.
- Direct original-detail visual review passed: authority box, all displayed
  maps, mathematical subscripts, acute accent in `Ec.`, Belyi diacritic,
  bibliography, normalization note, margins, and footer are legible; there is
  no clipping, overlap, missing glyph, or black box.

## Caveats and disposition

- No genuine source defect or unresolved source ambiguity was found.
- The source-page rasters are internal rights-gated evidence.
- Build and engine logs contain private local paths and must be sanitized or
  excluded from any public payload.
- This is producer work pending fresh independent review. It is not sealed,
  publication-ready, or an archive handoff.
