# Draft source audit - Expose VIII Corollary 2.3 proof opening

## Scope and locators

- Unit ID: `SGA2-VIII-C23-POC`.
- Included: corrected French lines 2683-2713, from the assumed regular-affine
  case through the complete open-cover comparison and editor's note (5).
- Original printed pages: 89-90. The marker opening printed page 90 occurs at
  French line 2685, after this unit's first paragraph.
- Physical source-PDF pages: 79-80.
- Re-composed running pages shown in the headers: 71-72.
- Excluded: blank line 2714 and the next reduction beginning at line 2715.
- Exact next cursor: French source line 2715 after blank line 2714.

## Source controls

The corrected arXiv French TeX is the textual authority. Its directly compiled
SMF reader is the page and visual control for the same edition; it is not an
independent original-typescript scan. jcreinhold e7a259f is a comparison-only
LLM lineage and supplies neither authority nor independent corroboration.

## Formula, logic, and note controls

The target preserves

- the definition
  `c_j(x)=codim(X_j intersect closure{x} intersect Y,
  X_j intersect closure{x})`;
- the weak inequality `c_j(x)>=c(x)`;
- the codimension-realizing point `y`, the equality
  `c(x)=dim O_{closure{x},y}`, and the resulting `c_j(x)=c(x)`;
- the local-to-global direction: condition (a) for the `X_j` implies condition
  (a) for `X`;
- the corrected partial converse before note (5): condition (a) for `X`
  implies it only for those `X_j` for which `c(x)=c_j(x)` at this stage; and
- the complete editor's note: `(c_J)=>(a_J)` through
  `(c')=>(d)=>(a')`, together with `(a)=>(c)` and `(c)<=>(c_J)`, hence
  `(a)=>(a_J)`.

Root pre-seal review caught two source-typography details. The period after
"purposes" now precedes marker (5), exactly as in the corrected branch and
physical page 80, and the source-emphasized *infra* remains emphasized as
*below*. A separate extraction-only revision replaced oversized display
delimiters with ordinary parentheses after the first build emitted U+0001;
the formula itself did not change and final extraction has zero forbidden
control bytes.

## Comparison disposition

The external candidate is close in its main prose and formula but omits the
entire corrected editor's note (5). Every accepted phrase was independently
rechecked against the French authority and same-edition compiled pages. The
candidate was not promoted.

## Independent closure

Independent source, formula, logic, note, typography, boundary, isolated-build,
render, extraction, and machine-evidence review found no substantive target
defect. The unit is sealed at French line 2715 after blank line 2714.
