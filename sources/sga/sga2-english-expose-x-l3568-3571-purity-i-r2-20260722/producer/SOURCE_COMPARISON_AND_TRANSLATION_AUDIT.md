# Source comparison and translation audit

Status: **PRODUCER PASS — pending fresh independent review**

## Authority and boundary

- Sole editable translation authority: corrected arXiv French TeX, full-file SHA-256 `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Exact admitted scope: lines 3568–3571 inclusive, 1,951 Latin-1/LF bytes, SHA-256 `9F1568E7EF1A39A857E5DD119673EAC07F291F3D8E0B60B13DD8107DADB462BE`.
- Locators: original printed pp. 121–122; source-PDF physical p. 105; recomposed running p. 97. The printed p. 122 marker occurs inside source line 3569.
- Raw continuation cursor: blank line 3572, SHA-256 `01BA4719C80B6FE911B091A7C05124B64EEECE964E09C058EF8F9805DACA546B`.
- Next substantive cursor: line 3573, no-EOL SHA-256 `BBC2D1966E57C80C63782EA45A3F0AEB36B3A38968C4A69B7A8CB64B67D17071`. Line 3573 and its pending candidates are excluded in full.
- The French authority was not modified. The same-edition PDF is locator/layout evidence only, not independent corroboration.

## Sentence and logic alignment

The target retains the complete two-stage proof of Theorem 3.4(i):

1. Dimension-two base case: define the punctured spectrum, invoke Lemma 3.5, extend the étale algebra coherently, use the depth/projective-dimension identity to obtain freeness, and eliminate the non-étale locus through the principal discriminant ideal.
2. Higher-dimensional induction: reduce to the complete case using Corollary 3.8, choose a parameter nonzero modulo the square of the maximal ideal, pass to the regular quotient of dimension `n-1`, and apply Lemma 3.9(i).

No hypothesis, implication, reference, symbol, direction, or dimension bound has been dropped or strengthened.

## Formula and notation comparison

| Source control | Target control | Result |
|---|---|---|
| `X'=\Spec(A)`, `x=\rr(A)`, `X=X'-\{x\}` | `X'=\operatorname{Spec}(A)`, `x=\mathfrak r(A)`, `X=X'\setminus\{x\}` | PASS; styling/notation normalization only |
| `\prof A=2` | `\operatorname{depth} A=2` | PASS; standard English operator |
| `\Et(X')\to\Et(X)` fully faithful | same functor and property | PASS; no unsupported hat |
| `\Aa=r_*(\Oo_R)` | `\mathcal A=r_*(\mathcal O_R)` | PASS; calligraphic normalization only |
| `i_*(\Aa)=\Bb` over `\Oo_{X'}` | `i_*(\mathcal A)=\mathcal B` over `\mathcal O_{X'}` | PASS; base and pushforward preserved |
| `\dimp\Bb+\prof\Bb=\dim A=2` | `\operatorname{pd}\mathcal B+\operatorname{depth}\mathcal B=\dim A=2` | PASS; equality and term order preserved |
| discriminant ideal of `\Bb/A` | discriminant ideal of `\mathcal B/A` | PASS |
| `t\in\rr(A)` nonzero in `\rr(A)/\rr(A)^2` | same condition with `\mathfrak r` | PASS |
| `B=A/tA`, regular, dimension `n-1` | same quotient, regularity, and dimension | PASS |
| Lemma `X.3.9` (i), applicable because `A` is complete | Lemma 3.9(i), same applicability | PASS |

There are no diagrams in this bounded unit.

## Inherited context and source-defect disposition

Stable observation `SGA2-X-L3569-REGULARITY-CONTEXT-OBS-001` records that line 3569 first says only “a noetherian local ring of dimension 2,” then later explicitly invokes regularity. Theorem 3.4(i), whose proof this is, already states the regular noetherian local hypothesis. The target retains the line-level wording and visibly discloses the inherited theorem context. This is an observation, not a confirmed source defect, and the authority remains byte-identical.

No confirmed textual source defect was found in lines 3568–3571. The page-marker split is a locator fact, not a textual defect.

## External English comparison

The current jcreinhold e7a259f Markdown is one LLM-generated comparison lineage only. Its relevant lines 446–466 were reviewed. It agrees on the proof skeleton but is rejected as a substrate because it retains literal `prof`/`dp`, changes the source's `Et` to unsupported hatted notation, flattens calligraphic algebra symbols, and uses several less precise literal renderings. No agreement from this witness is treated as independent source corroboration.

## Release state

The TeX, PDF, renders, and ledgers remain `internal_not_for_release`. A fresh independent review is required before any seal, cumulative integration, archive handoff, or publication claim.
