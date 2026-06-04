# Cumulative methodology update through Papers 36--39

## Scope

This packet adds Papers 36--39 to the Spanish/Japanese branch and carries forward the checked cumulative branch through Paper 35.  It also performs the requested English/German cumulative table repair for the Paper 02 table pages.

## Retroactive layout repair

Paper 02 Tables I--II are kept as editable TeX tables, not images.  The previous landscape wrappers in the English and German cumulative TeX were removed, matching the already-applied Spanish/Japanese repair.  The table bodies were not rewritten; the change is layout-only: A4 portrait pages, `adjustbox`, and a reduced maximum total height.  Render checks for pages 39--40 are included for English, German, Spanish, and Japanese.

## Terminology decisions

`Differente` is now treated as the technical algebraic-number-theory different: Spanish `diferente`, Japanese `ディファレント（差異イデアル）` on first technical occurrence.  This replaces the older too-literal Japanese gloss in the methodology while preserving older body text unless a local cumulative repair is needed.

`Hauptordnung` in Paper 37 is translated literally as `orden principal` / `主オーダー` rather than silently normalizing to maximal order.  The source phrase is historically marked and should remain visible for later Takagi integration.

`Galoismodul`, `operatorisomorph`, and crossed-product vocabulary are standardized across Papers 37--39 as `módulo galoisiano` / `ガロア加群`, `operator-isomorfo` / `作用素同型`, and `producto cruzado` / `交叉積`.

`Körper` in the algebra sections remains context-sensitive.  Field extensions are `cuerpo` / `体`; normal division algebras use `álgebra de división` / `斜体` where division-ring language is required.

## Global optimization note

The cumulative Spanish/Japanese branch was rebuilt from the checked Paper 35 cumulative branch.  No older mathematical formulas were changed.  The English/German cumulative table repair is included as control-lineage material under `04_ctrl/en_de_cumfix/`.


# Cumulative methodology update through Paper 40

## Scope

This packet completes Paper 40, `Nichtkommutative Algebren`, in Spanish and Japanese and rebuilds the cumulative Spanish/Japanese branch through Paper 40.  The English and German cumulative controls are also carried forward from the already-cleaned Paper 39 table-fix branch, so the Paper 02 table pages remain standard A4 portrait pages in all four cumulative PDFs.

## Retroactive layout continuity

The Paper 02 Tables I--II repair remains active in Spanish, Japanese, English, and German cumulative outputs.  The tables are still editable TeX; the layout change is only page geometry/fit, not a mathematical or textual rewrite.  Render checks for pages 39--40 are included for all four cumulative PDFs.

## Paper 40 terminology decisions

`Körper` remains context-sensitive.  In commutative extension-field passages it is `cuerpo` / `体`; in the noncommutative algebra passages it is division-ring language, with first occurrences rendered as `cuerpo no conmutativo (anillo de división)` / `非可換体（斜体）` and subsequent technical occurrences as `anillo de división` / `斜体` where clarity requires.

`Zerfällungskörper` and `Abspaltungskörper` are not collapsed.  The former is `cuerpo de descomposición` / `分解体`; the latter is `cuerpo de escisión parcial` / `部分分解体`.  This distinction is important for the Paper 40 representation-theoretic classification and for later Takagi/Brauer integration.

`reziproke Darstellung`, `direkte Darstellung`, and `reziprok-isomorph` are standardized as `representación recíproca`, `representación directa`, `recíprocamente isomorfo` / `相反表現`, `直接表現`, `相反同型`.

## Global optimization note

A small cumulative wording refinement was applied inside Paper 40 before packaging: Spanish `subcuerpo maximal` in the noncommutative theorem statements was corrected to `subanillo de división maximal`; Japanese `極大な部分体` in the same noncommutative context was corrected to `極大部分斜体`.  A Japanese reference to Paper 36's technical `Differente` was also normalized to `ディフェレント（Different）` rather than ordinary `異なる`.  Formulas, footnotes, and control witnesses were not altered.
# Methodology addendum: Papers 41--42

Paper 41 is class-field-theory/genus language. `Hauptgeschlechtssatz` remains Spanish `teorema del género principal` and Japanese `主属定理`, matching the earlier Paper 39 policy. `Geschlecht` is not collapsed into ordinary `clase`; `clase` / `類` remains reserved for ideal classes and representation classes.

Paper 42 uses `Gebiet` for an arithmetic grouping of maximal orders. It is rendered as `dominio` / `領域`; this is intentionally distinct from `Ringbereich`, even though both can be called domains in English. `Maximalordnung`, `Hauptordnung`, and `Erweiterungsideal` continue the order-theoretic terminology from Papers 31, 35, and 37--40.

All source-visible footnotes in Papers 41--42 were translated in Spanish and Japanese, even though the existing English control omits some of them. The German source/control witness is kept unchanged for comparison.

The Paper 02 table-page repair remains carried in all four cumulative branches. Pages 39--40 in ES/JA/EN/DE cumulative render checks are standard A4 portrait pages with editable TeX table bodies.

# Paper 43 methodology addition

Paper 43 completes the numbered Noether corpus in this branch. The main terminology decision is to keep `Differente` as the algebraic-number-theory different/different ideal: Spanish `diferente`, Japanese `ディファレント`. `Differenzenideal` and `Differenzenquotient` remain ordinary difference-ideal / difference-quotient language, so they are not collapsed into the technical `Differente`.

The invariant construction is rendered consistently as direct-product/coefficient-extension language. `direktes Produkt` is Spanish `producto directo` and Japanese `直積`; `Erweiterung des Koeffizientenbereichs` is Spanish `extensión del dominio de coeficientes` and Japanese `係数領域の拡大`.

`Ergänzungsmodul` and `Ergänzungsbasis` are treated as complementary-module/complementary-basis terminology tied to Dedekind's different definition: Spanish `módulo complementario`, `base complementaria`; Japanese `補加群`, `補基底`.

The next phase is a recursive source-audit pass from Paper 01 forward. Pass R01 begins in this package with Paper 01; later passes should compare source scan, German witness, English control, and ES/JA cumulative body, then apply wording-only or content-restoration fixes to the cumulative branch when they are genuinely justified by the source.
# RA02 methodology addition

Paper 02 formula (10) derivation contains hatted nu factors in the scan. Treat `\widehat{\nu}x^2` as source-authoritative in this block. The prior cumulative forms with plain `\nu x^2` and one malformed literal `u x^2` were scan-derived transcription defects, not deliberate source anomalies.

Confirmed genuine source anomaly retained: Paper 02 scan p. 69 has `H_j^2, H_j^2` in the reduction line; leave as duplicate unless a later source witness proves otherwise.

Recursive audit procedure: audit German to scan first, then propagate to EN/ES/JA. Do not let an English control override the scan.
