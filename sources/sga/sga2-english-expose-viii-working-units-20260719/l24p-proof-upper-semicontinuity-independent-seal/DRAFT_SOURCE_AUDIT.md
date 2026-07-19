# Draft source audit - SGA2 Expose VIII Lemma 2.4 proof

Status: bounded self-review and independent source, formula, emendation,
build, render, extraction, and machine review closed. No cumulative Expose
VIII or publication claim is made.

## Scope and coordinates

- Corrected French TeX: lines 2723-2731.
- Original printed pages: 90-91. The printed-page-91 marker occurs inside
  line 2729.
- Physical source-PDF page: 80.
- Recomposed running page: 72.
- Included raw TeX state: line 2723 resets the equation counter to 1.
- Excluded boundary: blank line 2732.
- Next cursor: line 2733, beginning the subsequent affine main-proof phase.

The bounded unit contains the complete proof of Lemma 2.4: affine local setup,
a finitely generated projective resolution, finite stalkwise projective
dimension, the kernel K, freeness near the point, localization to a principal
open, a finite projective resolution after localization, upper
semicontinuity, and the quasi-compactness conclusion.

## Direct formula and logic review

The active corrected branch defines

    K = ker(L^{-d} -> L^{-d+1}).

The target preserves this branch, the element and principal-open controls
f in O_X(U) and x in D(f) contained in U-prime, the citations [M], Chapter VI,
Proposition 2.1 and EGA 0_I, 5.4.1 Errata, all localizations, both zero
endpoints, and the direction upper semicontinuous.

## Two transparent source emendations

French line 2729 and the compiled page print M with subscript f-prime even
though only f is chosen and the next display ends in M_f. The target uses M_f.

French line 2730 prints localized L with exponent d-minus-1. That term matches
the inactive historical kernel branch retained inside sisi, but the active
corrected branch makes K a submodule of L^{-d}. The target therefore begins
the localized resolution with K_f to localized L^{-d}.

Both corrections are visibly disclosed in the target source note. They are
editorial emendations, not restorations from an independent original scan:
the direct PDF is compiled from this same corrected TeX. The French authority
remains byte-unchanged.

Independent source review and a separate branch/formula review accept both
target readings with no body change. The active `original=false` driver
state selects the negative-index kernel branch; only `f` is introduced.
The same-edition PDF caveat remains in force.

The fully located Codex alert
SGA2_EXPOSE_VIII_LEMMA_2_4_TWO_INDEX_DEFECTS_CODEX_20260719.md has SHA-256
8CE744D7024DFABA16C07E2C41F41AB3BCC65B02C4ABA1DC0E3E41D5841B7FFD.
It is coordination and review evidence, not source authority.

## Comparison candidate

The jcreinhold e7a259f candidate follows the proof closely, silently changes
M with subscript f-prime to M_f, repeats the stale localized L exponent
d-minus-1, and omits the raw equation-counter state. It is one LLM-generated
comparison lineage. Neither its agreement nor its correction is treated as
independent corroboration.

## Extraction correction

The first target build emitted one forbidden U+0001 byte after the kernel
formula during layout-text extraction. Removing only the `\bigl` and `\bigr`
delimiter-sizing commands preserved the mathematical formula and eliminated
the control byte. Both build passes, target renders, extraction, PDF reports,
and dependent hashes were regenerated after that TeX correction. Final
extraction contains zero forbidden control bytes.

The next source cursor remains line 2733 after blank line 2732.
