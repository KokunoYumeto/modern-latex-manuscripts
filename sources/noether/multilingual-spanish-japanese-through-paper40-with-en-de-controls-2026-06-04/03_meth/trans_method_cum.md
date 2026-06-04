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


## Paper 40 translation method note

Paper 40 was translated against the German source/control in the two archival batches and checked against the English control only as an aid.  The translation prioritizes source-visible historical terminology while using modern mathematical disambiguation where Spanish/Japanese would otherwise collapse distinct notions.  In particular, noncommutative `Körper` is kept visible but made division-ring-aware, and `Abspaltungskörper` is kept distinct from `Zerfällungskörper`.

No screenshots are used as substitutes for formulas or tables.  Formula displays and footnotes are editable TeX.
