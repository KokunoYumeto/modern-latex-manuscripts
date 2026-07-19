# Production source audit - SGA2-VIII-P32P1

This bounded production unit covers corrected French lines 2901-2907: the
opening of the proof of Proposition 3.2 through the complete statement of
condition (c). Blank line 2908 is excluded. French line 2909, the implication
`(a) => (b)`, is the exact continuation cursor.

The corrected arXiv TeX is authority. The direct compiled 216-page French
reader is generated from the same corrected edition and is therefore page,
layout, and visual evidence rather than independent corroboration. The unit
starts at the bottom of physical PDF p. 84 / running p. 76 and continues at the
top of physical p. 85 / running p. 77. It remains on original printed p. 97:
the source does not advance that coordinate until the `pageoriginale` token at
French line 2915.

The target preserves the coherent extension `G`, its restriction to `U`, the
isomorphism with `F`, the EGA I 9.4.3 citation, the application of Corollary
2.3, and the equivalence of conditions (a) and (c). Condition (c) preserves
the quantifier `x in S`, operator `prof`, the strict inequality, both singleton
closures, intersection with `Y`, and the codimension argument order.

The symbol `Y` is not reintroduced inside this proposition. It is inherited
from Corollary 2.3 and the Section 2 convention `U = X setminus Y`. The target
formula keeps `Y` unchanged; the authority box adds a disclosed context note.
That note is not a French-source emendation.

The jcreinhold e7a259f Markdown is comparison-only. Its opening translation is
broadly aligned, but comparison line 653 changes the authority's `x in S` to
`x in overline S`. Both corrected TeX line 2904 and the visual source page read
`S`, so the comparison reading is rejected. Its fenced plain-text formula and
flattened overline presentation are not promoted.

Manager decision `EG-SGA2-FG-NOTATION-ADJUDICATION-20260719-0001` closes
Option A: target calligraphic `F` and `G` are explicit English normalizations
from source upright glyphs, never literal glyph preservation. The operator
`prof` remains unchanged. No separate `Z`, `R`, `E`, or set-minus policy is
invoked inside this bounded body.

The first target render used scalable codimension delimiters and was visually
correct, but PDF text extraction exposed one forbidden C0 control character.
Production revision 2 replaced only those scalable delimiters with ordinary
parentheses. The rebuilt formula is semantically and visually unchanged; the
final extraction has zero forbidden C0 controls and one ordinary page form
feed.

No confirmed defect in French lines 2901-2907 is claimed. This is production
self-review only; independent source/formula, visual, machine-evidence, and
privacy review remain required before any seal.
