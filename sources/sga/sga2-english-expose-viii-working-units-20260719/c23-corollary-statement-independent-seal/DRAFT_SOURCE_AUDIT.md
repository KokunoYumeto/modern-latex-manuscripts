# Draft source audit - Expose VIII Corollary 2.3

## Scope and locators

- Unit ID: `SGA2-VIII-C23`.
- Included: corrected French lines 2670-2681, the complete statement of
  Corollary 2.3 and editor's note (4).
- Original printed page: 89 only. The `\pageoriginale` marker at line 2641
  opens printed page 89; `\pageoriginaled` at line 2685 opens printed page 90
  after this unit.
- Physical source-PDF page: 79.
- Re-composed running page shown in the header: 71.
- Excluded: blank line 2682 and the proof beginning at line 2683.
- Exact next cursor: French source line 2683 after blank line 2682.

## Source controls

The corrected arXiv French TeX is the textual authority. Its direct compiled
SMF reader is the page and visual control for the same edition; it is not an
independent original-typescript scan. jcreinhold e7a259f is a comparison-only
LLM lineage and supplies neither authority nor independent corroboration.

## Formula, logic, and note controls

The target retains all four Roman-numbered conditions and their equivalence.
Condition (i) has the strict inequality `> n-c(x)`. Condition (ii) has the
weak inequality `>= n` and the qualifier `c(x)=1`. Condition (iii) quantifies
over every integer `i` and has the bound `i<=n`. Condition (iv) retains the
higher direct-image notation `R^i i_*`, the restriction to `U`, and the strict
bound `i<n`.

The editor's note is retained in full and attached to condition (iv): the
condition appeared only in the body of the proof, was absent from the original
corollary statement, and was added because it is used in Section 3.

## Comparison disposition

The comparison candidate has useful close wording and correctly preserves the
Roman numbering, inequalities, and added condition. Its heading is unnumbered
in rendered Markdown, it uses `prof` without resolving target register, and it
is not an independent witness. Every accepted phrase was rechecked against the
French authority and compiled page.

