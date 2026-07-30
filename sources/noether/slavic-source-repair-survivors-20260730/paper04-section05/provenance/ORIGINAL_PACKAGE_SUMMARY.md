# Noether Paper 4 Sections 4-5 checkpoint summary

Date: 2026-07-18

## Scope

This bounded checkpoint independently compares the original Paper 4 print, the R823 German transcription, and the four active Section 4-5 Slavic reader bodies at the disputed loci on printed pp. 132, 135, and 137.

## Promoted repair

Equation (35) in all four Section 5 bodies had an unsupported target-lineage regression:

```tex
R_{\rho+\sigma_1-\alpha-\lambda}
```

It is repaired to the R823 reading:

```tex
R_{\rho_1+\sigma_1-\alpha-\lambda}.
```

The repaired editable units are Latin Interslavic, Cyrillic Interslavic, Russian, and Ukrainian Section 5 TeX.

## Adjudicated without body change

- Printed p. 132 repeats `\tau\geq\sigma` in cases 3 and 4; the readers retain R823's disjoint case partition with `\tau>\sigma` in case 3.
- Printed p. 135 equation (35) and R823 differ in three coordinated indices; the readers retain the coherent R823 editorial emendation.
- Printed p. 137 says `Defekt \alpha`; the readers retain R823's contextually coherent `Defekt \rho`.
- Printed p. 137 uses an identity/congruence sign in the linear-form condition; the readers retain R823's ordinary equality.

These are recorded as adverse print-to-editorial deltas, not silently normalized and not misclassified as target translation defects.

## Evidence and QA

- Original Paper 4 scan and R823 TeX are included.
- Printed pp. 132, 135, and 137 were rendered at 600 dpi and opened directly.
- Focused crops for every adjudicated locus are included.
- All four repaired Section 5 units compiled twice with XeLaTeX.
- The four PDFs contain nine pages total: 2 Latin Interslavic, 2 Cyrillic Interslavic, 3 Russian, and 2 Ukrainian.
- All nine pages were rendered at 240 dpi and visually inspected.
- The compile scan found no fatal errors, undefined controls, rerun warnings, or overfull boxes.
- The live difficulty ledger validates with 17 entries.
- The structural index validates with 12,970 records across 442 canonical Latin/Cyrillic units and no unresolved references.

## Authority limit

This is a source-audited checkpoint for the named loci and one repaired formula family. It is not a complete certification of Paper 4, Sections 4-5, any full-language translation, or the full Noether corpus. The German diplomatic source policy remains separate: original-print defects are preserved in diplomatic German and disclosed in apparatus, while downstream target regressions are repaired in reader bodies.

## Supersession

This checkpoint supersedes:

- the four active Section 5 bodies containing bare `\rho` in equation (35);
- the incomplete earlier equation-(35) alert snapshot with SHA-256 `B577CE71E0D03E44CE6132E17FBF89E7845D73BF4BF330F3D592A62ADCBE2F92`.

The canonical expanded equation-(35) alert has SHA-256 `575858ED2D73BD9AC5D97A923B8200CF8014C26E357E56AD3440747D1E6BA0B5`.

## Continuation

Continue source-critical Paper 4 review outside the three adjudicated printed pages; do not infer page-wide or section-wide closure from these targeted records.
