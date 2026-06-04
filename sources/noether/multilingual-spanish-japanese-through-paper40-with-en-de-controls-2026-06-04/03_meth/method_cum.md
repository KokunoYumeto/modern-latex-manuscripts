# Cumulative methodology update through Papers 36--39

## Scope

This packet adds Papers 36--39 to the Spanish/Japanese branch and carries forward the checked cumulative branch through Paper 35.  It also performs the requested English/German cumulative table cleanup for the Paper 02 table pages.

## Retroactive layout cleanup

Paper 02 Tables I--II are kept as editable TeX tables, not images.  The previous landscape wrappers in the English and German cumulative TeX were removed, matching the already-applied Spanish/Japanese cleanup.  The table bodies were not rewritten; the change is layout-only: A4 portrait pages, `adjustbox`, and a reduced maximum total height.  Render checks for pages 39--40 are included for English, German, Spanish, and Japanese.

## Terminology decisions

`Differente` is now treated as the technical algebraic-number-theory different: Spanish `diferente`, Japanese `ディファレント（差異イデアル）` on first technical occurrence.  This replaces the older too-literal Japanese gloss in the methodology while preserving older body text unless a local cumulative cleanup is needed.

`Hauptordnung` in Paper 37 is translated literally as `orden principal` / `主オーダー` rather than silently normalizing to maximal order.  The source phrase is historically marked and should remain visible for later Takagi integration.

`Galoismodul`, `operatorisomorph`, and crossed-product vocabulary are standardized across Papers 37--39 as `módulo galoisiano` / `ガロア加群`, `operator-isomorfo` / `作用素同型`, and `producto cruzado` / `交叉積`.

`Körper` in the algebra sections remains context-sensitive.  Field extensions are `cuerpo` / `体`; normal division algebras use `álgebra de división` / `斜体` where division-ring language is required.

## Global optimization note

The cumulative Spanish/Japanese branch was rebuilt from the checked Paper 35 cumulative branch.  No older mathematical formulas were changed.  The English/German cumulative table cleanup is included as control-lineage material under `04_ctrl/en_de_cumfix/`.


# Cumulative methodology update through Paper 40

## Scope

This packet completes Paper 40, `Nichtkommutative Algebren`, in Spanish and Japanese and rebuilds the cumulative Spanish/Japanese branch through Paper 40.  The English and German cumulative controls are also carried forward from the already-cleaned Paper 39 table-fix branch, so the Paper 02 table pages remain standard A4 portrait pages in all four cumulative PDFs.

## Retroactive layout continuity

The Paper 02 Tables I--II cleanup remains active in Spanish, Japanese, English, and German cumulative outputs.  The tables are still editable TeX; the layout change is only page geometry/fit, not a mathematical or textual rewrite.  Render checks for pages 39--40 are included for all four cumulative PDFs.

## Paper 40 terminology decisions

`Körper` remains context-sensitive.  In commutative extension-field passages it is `cuerpo` / `体`; in the noncommutative algebra passages it is division-ring language, with first occurrences rendered as `cuerpo no conmutativo (anillo de división)` / `非可換体（斜体）` and subsequent technical occurrences as `anillo de división` / `斜体` where clarity requires.

`Zerfällungskörper` and `Abspaltungskörper` are not collapsed.  The former is `cuerpo de descomposición` / `分解体`; the latter is `cuerpo de escisión parcial` / `部分分解体`.  This distinction is important for the Paper 40 representation-theoretic classification and for later Takagi/Brauer integration.

`reziproke Darstellung`, `direkte Darstellung`, and `reziprok-isomorph` are standardized as `representación recíproca`, `representación directa`, `recíprocamente isomorfo` / `相反表現`, `直接表現`, `相反同型`.

## Global optimization note

A small cumulative wording refinement was applied inside Paper 40 before packaging: Spanish `subcuerpo maximal` in the noncommutative theorem statements was corrected to `subanillo de división maximal`; Japanese `極大な部分体` in the same noncommutative context was corrected to `極大部分斜体`.  A Japanese reference to Paper 36's technical `Differente` was also normalized to `ディフェレント（Different）` rather than ordinary `異なる`.  Formulas, footnotes, and control witnesses were not altered.
