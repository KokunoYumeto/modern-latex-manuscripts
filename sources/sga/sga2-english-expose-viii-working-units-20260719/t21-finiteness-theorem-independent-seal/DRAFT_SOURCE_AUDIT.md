# Draft source audit - Expose VIII Theorem 2.1

## Scope and locators

- Unit ID: `SGA2-VIII-T21`.
- Included: corrected French lines 2640-2659, Section 2 heading and the complete
  statement of Theorem 2.1.
- Original printed page: 89 only. The next `\pageoriginale` marker is after this
  unit, so the physical page break does not change the original printed page.
- Physical source-PDF pages: 78-79.
- Re-composed running pages printed in the PDF header: 70-71.
- Excluded: blank line 2660 and Corollary 2.2 beginning at line 2661.
- Exact next cursor: French source line 2661 after blank line 2660.

## Source decisions

The theorem number, three note attachments, conditions a) and b), every
quantifier, the local-cohomology exponent and stalk, and the closure/codimension
formula were checked directly against both the corrected French TeX and its
compiled PDF. The TeX's corrected branches supply calligraphic `F` and the
resolved Hartshorne cross-reference p. 46. Equation (2.1) is an automatically
numbered and labeled equation, not a manually tagged display.

The external jcreinhold e7a259f English Markdown was used only as one comparison
lineage. Its standard phrases “finiteness theorem” and “locally embeddable” are
accepted only after direct source checking. Its missing visible theorem numeral,
fenced-text rendering of (2.1), and `original page 71` comment are rejected:
71 is the re-composed running page, while the original printed page is 89.

A root precheck caught and corrected two bibliographic fidelity errors in the
first draft: `Mme Raynaud` had been reduced ambiguously to `M. Raynaud`, and
`Ec.` had the wrong grave accent. The final target restores `Mme Raynaud
(Raynaud M., ...)` and acute `Ec.`. A custom theorem head style preserves the
automatic theorem counter while placing note marker (1) before the heading
period exactly as in the French print.

The first target build used enlarged delimiters around the codimension
arguments. Although visually correct, their text mapping emitted one forbidden
`0x01` byte. They were replaced with ordinary source-sized parentheses; the
formula, both closure bars, argument order, and `equation.2.1` destination
remain unchanged, and final extraction contains zero forbidden control bytes.

## Caveats

The direct compiled PDF comes from the same corrected French edition and is not
an independent original-typescript scan. This bounded unit is a working English
translation, not an Expose VIII or volume completion, a critical edition, or a
publicly source-certified artifact. A separate line/formula/note/build/render/
machine review subsequently passed and is recorded in
`INDEPENDENT_REVIEW_SEAL_20260719.md`; the scope caveats remain unchanged.
