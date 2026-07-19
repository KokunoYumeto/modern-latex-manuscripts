# SGA 1 I.9 opening through Proposition I.9.1 — source check and review

Date: 2026-07-19 (Europe/Berlin).

## Outcome

The bounded English fragment through Proposition I.9.1 is locally
source-audited and closed at French line 1703. The first excluded line is 1704.
Every formula, hypothesis, logical dependency, paragraph boundary, source
emphasis, page transition, and source-selected punctuation branch in the unit
was checked against the French TeX. The original print was used as a visual and
pagination control, not as a translation substrate.

## Material decisions

- `Propriétés de permanence` is rendered as **Permanence properties**.
  Thosgood's *Invariance properties* was rejected as a change of register.
- Historical prime-ideal `rang` is rendered as **height**, not *rank*.
- `dans la terminologie encore courante` remains *in the terminology still in
  use*. The target-control reading *in the more modern language* reverses the
  source claim.
- All source emphasis is retained, including the full dimension/depth,
  Cohen--Macaulay, equal-height, embedded-prime, and *every prime ideal*
  assertions.
- French lines 1656--1680 remain one paragraph across the marginal page-16
  marker. Lines 1690--1702 remain one proof paragraph through the displayed
  graded-ring formula.
- The `orig=false` authority branch supplies the comma after
  `L=B\otimes_A k`; that corrected branch was retained.
- The formula is exactly
  `gr^*(B)=gr^*(A)\otimes_k L`. Thosgood's `gr^\bullet` and final uppercase
  `K`, jcreinhold's plain-text `gr*`, and the inherited Pandoc formula debris
  were rejected.
- The source has unheaded proof prose and `cqfd`; the target uses *This proves
  the proposition* without adding a proof environment or QED symbol, and
  retains the parenthetical N.B.

## External English controls

The controls were used only to expose English choices and regressions:

- jmoellermath Exposé I chapter: 12,973 bytes, SHA-256
  `5607E758966B31A5DB558C33506CB0A60413F7295B0F506F7215888C65CFF8B3`;
  no I.9 body coverage.
- Thosgood I.9 tree lines 1--45: 2,451 LF bytes, SHA-256
  `AAA66BDD2793369D43928BAB2CDEE14DEEA209410E6C0AACC7962A42E6807A43`.
- Current jcreinhold Markdown lines 763--801: 2,177 LF bytes, SHA-256
  `CCD8D102315730A29A3462926C2F49F9C152E57B2DDA9448B1030DE2B521F7C8`.
- Inherited same-lineage conversion lines 1477--1525: 2,325 LF bytes,
  SHA-256
  `472F3A2E27827B4ECD85E1673900961CB6A0AF6FD978517B6BD51F3E6641F062`.

None of these controls is source authority or independent source
corroboration.

## Machine evidence

- `ledgers/SOURCE_COMPARISON_I_9_1.csv`: 7 data rows, rectangular,
  formula-injection safe, SHA-256
  `CFA761B44BBFBBF9A3E9A7A2C0D77FECABD508946C1FB6E071F242C692F150DE`.
- `ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_9_1.csv`: 9 data rows,
  rectangular, formula-injection safe, SHA-256
  `E8E58CF284190EE84D7F12AA564A5919366183FF723E433D3ABB8B638E343FB1`.
- `machine_ledgers/SGA1_I9_1_EVIDENCE_GRAPH.jsonl`: 4 records,
  SHA-256
  `E739AFEDDE0AD0C6B42D064CD6BA91F6E5480159794BD466C8DD82A6755D2B77`.
- Cumulative machine validation: 382 CSV data rows / 176 JSONL records /
  zero failures.

The exact next cursor is excluded French line 1704.
