# P34 printed pp. 641-668 source audit, v19

## Scope

This pass independently opened GDZ full-resolution source pages 641-649 and 663-668 against the v18 current-head TeX. Together with v18's page-by-page pass over pp. 650-662, this gives a continuous independent current-head audit of P34 printed pp. 641-668. The already heavily worked Web/WebB lane covers pp. 669-692.

## Substantive mathematical repair

Printed p648 distinguishes the homomorphism sign from the isomorphism sign on the preceding page. The source then prints the isomorphism sign in all three displayed theorem conclusions:

```tex
\overline{\mG}/\overline{\mA}\simeq \mG/\mA,
(\mG/\mN)/(\mA/\mN)\simeq \mG/\mA,
\mA\mB/\mB\simeq \mA/(\mA\cap\mB).
```

The v18 cumulative used `\sim` at all three loci. v19 restores `\simeq`. The proof's genuinely homomorphic maps remain `\sim`.

## Source-significant typography and case

Source emphasis marking definition names, scope, hypotheses, and forward references had been flattened on pp. 643-644 and 646-649. v19 restores those marked phrases. It also restores the printed lowercase compounds `o-links-Modul` and `o'-rechts-Modul`.

These changes are not counted as hard-math symbol repairs except for the three p648 relation signs. They remain important to a diplomatic source-critical edition because the source uses emphasis to distinguish defined terms and theorem scope.

## No-patch pages

No secure delta was found on pp. 641-642, 645, or 663-668. Their explicit page dispositions are recorded in `P34_p641_649_p663_668_dispositions_v19.csv` and in the master page-QC ledger.

## QA

- XeLaTeX passed twice.
- Output remains 466 pages.
- The repaired band renders on cumulative output pp. 317-321.
- The p648 source relation signs were checked again in a 2x labelled crop.
- v19 output p320 was visually reopened after recompilation.
- No source words or formulas were inserted from OCR.

## Process lesson

A prose-complete page can still contain a mathematical error when two relation glyphs have distinct meanings but similar silhouettes. For theorem statements, audit the displayed relation against the named theorem and against the source's own symbol definitions; do not infer correctness from nearby prose or from successful compilation.
