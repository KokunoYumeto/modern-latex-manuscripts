# Dirichlet Source-Completeness Audit - 2026-06-01

## Input inspected

From `Dedekind Dirichlet Starter Packet 20260601.zip`:

- `current_public_readers/Dirichlet - Selected Works.pdf` - 241 pages, pypdf-produced reader.
- `local_source_scans/dirichlet_werke_vol1_1889.pdf` - 657 pages.
- `local_source_scans/dirichlet_werke_vol2_1897.pdf` - 433 pages.
- `local_source_scans/glejeunedirichl00dirigoog.pdf` - duplicate of the Band II scan by size and page count.
- `source_bundle_from_public_artifacts/source_dedekind_dirichlet_bundle_20260529.zip` - contains `15_Dirichlet_Glejune_COMBINED.pdf` only; no editable Dirichlet TeX was recovered from this bundle.

## Main verdict

The current Dirichlet public reader is **not source-complete** and **not source-trustworthy enough for front-facing use without repair**. It should be treated as a rough selected-work scaffold. The authoritative sources in the starter packet are the two Werke scans, especially Band II for the current selected reader.

## Why the selected reader is not enough

1. The local source scans contain both Werke volumes. Band I alone has 36 listed works; Band II has 41 listed items including appendix/correspondence material. The current reader is only 241 pages and begins with Band II material. It is therefore not a complete edition.
2. The reader is internally segmented into generated `Teil` blocks with reset page numbers and mixed title pages. This is a construction artifact, not the original Werke structure.
3. The current reader contains visible OCR/typesetting errors and broken footnote markers. In Paper I these include mathematically material errors.
4. At least one explanatory passage in the reader around PDF page 211, beginning `Das sogenannte Dirichlet'sche Princip oder Schubfachprincip...`, reads like a modern explanatory insertion rather than source text from the Werke. Treat such passages as suspect until matched to the scan.

## Confirmed first-paper errors in the current selected reader

The scan-checked source is `dirichlet_werke_vol2_1897.pdf`, scan pages 20-21, printed source pages 7-8.

Current reader PDF page 9 renders the condition as:

```tex
-\varphi(\lambda_0,\mu_0,\nu_0,\ldots)<p
```

The scan has:

```tex
-\varphi(\lambda_0,\mu_0,\nu_0,\ldots)+\Sigma m v_0^2<p
```

Current reader PDF page 9 renders the velocity relation as an equality with `+\varphi(\lambda,\mu,\nu,\ldots)`:

```tex
\Sigma m v^2 = \Sigma m v_0^2-\varphi(\lambda_0,\mu_0,\nu_0,\ldots)+\varphi(\lambda,\mu,\nu,\ldots)
```

The scan has the bounded form:

```tex
\Sigma m v^2 \leq \Sigma m v_0^2-\varphi(\lambda_0,\mu_0,\nu_0,\ldots)
```

Current reader PDF page 10 renders the last example as `-\lambda^2`. The scan has `\lambda^2`. This changes the mathematical point of Dirichlet's counterexample.

These three errors justify a source-first repair workflow for every subsequent Dirichlet item.

## High-level source table from the scans

### Band I scan contents

Band I contains works I-XXXVI. The table of contents begins with early French/Latin number-theoretic works, then Fourier series and heat, quadratic forms, arithmetic progressions, asymptotic number theory, definite integrals, complex numbers, and related short reports. Key high-priority items include:

- IX. `Ueber die Darstellung ganz willkürlicher Functionen durch Sinus- und Cosinusreihen` - p. 133.
- XXI. `Beweis des Satzes, dass jede unbegrenzte arithmetische Progression ... unendlich viele Primzahlen enthält` - p. 313.
- XXVIII. `Recherches sur diverses applications de l'analyse infinitésimale à la théorie des nombres` - p. 411.
- XXX-XXXII. complex-number and complex-form works - pp. 503, 509, 533.

Band I is not represented as a complete editable reader in the supplied public Dirichlet PDF.

### Band II scan contents

Band II contains works I-XLI. The first seven items are:

1. `Ueber die Stabilität des Gleichgewichts` - p. 3.
2. `Sur un moyen général de vérifier l'expression du potentiel relatif à une masse quelconque, homogène ou hétérogène` - p. 9.
3. `Ueber die charakteristischen Eigenschaften des Potentials ...` - p. 17.
4. `Ueber die Reduction der positiven quadratischen Formen mit drei unbestimmten ganzen Zahlen` - p. 21.
5. `Ueber die Reduction der positiven quadratischen Formen mit drei unbestimmten ganzen Zahlen` - p. 27.
6. `Ueber die Bestimmung der mittleren Werthe in der Zahlentheorie` - p. 49.
7. `Ueber einen neuen Ausdruck zur Bestimmung der Dichtigkeit einer unendlich dünnen Kugelschale ...` - p. 67.

The full Band II table continues through:

- VIII. divisibility of numbers in three squares - p. 89.
- X. `De formarum binarium secundi gradus compositione` - p. 105.
- XII-XVI. reciprocity/quadratic-form works - pp. 121-189.
- XX, XXV. hydrodynamics problem - pp. 215 and 263.
- XXII. Jacobi memorial address - p. 225.
- XXIII. Academy monthly report extracts - p. 253.
- XXVI. Abel theorem note - p. 303.
- XXVII. Kummer memorial address - p. 309.
- XXXVI-XXXVIII. Dirichlet correspondence with Gauss, Kronecker, Humboldt - pp. 373, 388, 412.
- XLI. list of translations not included in the collected works - p. 421.

## Recommended continuation order

1. Finish Band II paper-by-paper in source order, because the selected reader already gives rough text for several early items but needs formula audit.
2. Use the same workflow as Paper I: render scan pages, rebuild editable source TeX, translate only after source formulas are checked, compile, and document exact scan pages.
3. After Band II I-VII, decide whether to switch to Band I high-impact items, especially arithmetic progressions and Fourier series, or continue Band II sequentially.
4. Do not promote any `Teil` segment or current selected-reader page as cumulative truth until it has been checked against the scan.

## Current round output

Paper I is now rebuilt and translated in `new_work_this_round/` and mirrored to `cumulative_current/`. This is the first trustworthy cumulative Dirichlet unit in this package.
