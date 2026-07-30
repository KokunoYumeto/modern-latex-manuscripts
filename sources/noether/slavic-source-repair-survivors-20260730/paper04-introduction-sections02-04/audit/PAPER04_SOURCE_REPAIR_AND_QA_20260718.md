# Noether Paper 4 source repair and QA - 2026-07-18

## Scope

This tranche repairs sixteen active reader-body TeX files: Introduction and Sections 2-4 in Latin Interslavic, Cyrillic Interslavic, Russian, and Ukrainian. It does not claim a new whole-paper translation audit or human/community linguistic certification.

The changes are source-critical corrections only. They distinguish:

- original-print defects or omissions, which reader bodies may correct only with an explicit adverse/editorial note;
- R823 transcription defects, which are corrected directly;
- inherited target-lineage errors, which are corrected against print and R823;
- negative controls, which remain unchanged after direct checking.

## Confirmed changes

The authoritative row-level account is PAPER04_CONFIRMED_REPAIRS_20260718.csv. In summary:

1. Introduction: Study citation controlled to volume 10 while explicitly reporting the original's volume 1 misprint.
2. Section 2: \sigma>\tau repaired to \sigma\geq\tau.
3. Section 3: \rho<n repaired to \rho\leq n.
4. Section 3: the source-omitted continuation dots were restored as a^{(i+1)}\cdots a^{(\rho)} with a localized editorial footnote in each language.
5. Section 3: inherited K^{\rho_{k-1}} repaired to source (K-1)^{\rho_{k-1}}.
6. Section 4, equation (23): inherited q_\rho^{(1)} repaired to q_{\rho-1}^{(1)}.
7. Section 4, equation (28): both collapsed R823 subscripts restored exactly from printed p. 133.

## Source authority

The source managers supplied original-print page witnesses and focused crops. The decisive focused witnesses are:

- printed p. 126, condition \sigma\geq\tau;
- printed p. 129, \rho\leq n and the omitted continuation diagnosed from equation (16);
- printed p. 130, (K-1)^{\rho_{k-1}};
- printed p. 132, equation (23), q_{\rho-1}^{(1)};
- printed p. 133, equation (28), q_{\rho-(\tau-\sigma)} and p_{\tau-(\tau-\sigma)}.

The German diplomatic edition follows a stricter policy: source-print defects remain literal in its body and are disclosed in apparatus; R823 transcription defects are repaired. These reader translations use an explicitly disclosed editorial correction for the p. 129 omission.

## Build and render QA

- All 16 TeX files compiled with XeLaTeX twice.
- All 16 PDFs exist; total output is 49 pages.
- Compile scan found zero fatal errors, undefined controls, rerun warnings, or overfull boxes.
- The logs contain 112 underfull-box notices across 14 units. These are disclosed layout warnings, not hidden as a clean-log claim.
- All 49 pages were rendered at 240 dpi.
- Four complete language contact sheets were inspected for blank pages, clipping, overlap, broken displays, and missing glyphs.
- Exact changed pages were also inspected at original render resolution: all four Section 2 page-2 renders; all four Section 3 page-2 and page-3 renders; all four Section 4 page-1 and page-2 renders.
- The restored ellipsis footnotes fit; (K-1), equation (23), and both longer equation (28) subscripts remain legible and do not collide with surrounding material.

The long absolute filenames printed between thumbnails are labels generated only in the QA contact sheets. They are not present in any PDF.

## Reproducibility and process defect

apply_paper04_source_repairs_20260718.ps1 requires exact preimage hashes and exactly one old reading at each locus. Two initial runs stopped safely: one exposed the inherited K normalization, and one exposed the Cyrillic introduction's Бд. abbreviation. The corpus was restored from the exact prechange backup before each corrected rerun.

The first successful compilation command contained a PowerShell argument-interpolation error and wrote outputs into four literal $out directories. Those outputs were not accepted. All sixteen units were rebuilt to the intended language/unit directories, the accidental directories were verified and removed, and the final build-status ledger points only to the corrected outputs. This failure is retained in the append-only difficulty ledger because silent output-path mistakes can invalidate otherwise sound QA.

## Structural index

The canonical Latin/Cyrillic structural index was rebuilt after the eight active Interslavic-file changes. It now contains 12,968 records, 6,484 per script. Validation passes with zero referential or CSV-parity errors; the pre-existing 18 unmatched cross-script records remain explicitly unresolved rather than force-paired.

## Remaining limits

This package closes only the listed source/lineage defects in the sixteen named units. It does not certify all Paper 4 wording, terminology, or source fidelity, and it does not replace the lane-wide open normalization and human-validation work.
