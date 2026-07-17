# Noether Spanish R823 Working Translation

## Reader

Open `01_reader/Noether_Spanish_R823_Cumulative_WorkingTranslation_20260718.pdf`.
It is a 473-page Spanish working translation aligned to the current R823
German source-control corpus.

## Declared Scope

- 81 of 81 source units represented;
- Papers 1-43;
- the lecture-book title/introduction and Sections 1-31;
- Kapferer-Noether material, supplement, bibliography, notices, reviews,
  publication lists, corrections, and books list;
- 101 locator-backed terminology decisions.

The production gate records all checks passing. The archive-maintainer reran
the frozen 13-row artifact-hash check with zero failures, scanned the final log
for fatal, undefined, box-overflow, and missing-character patterns, checked PDF
text extraction, and visually inspected beginning, middle, terminal, and
high-density mathematical renders before packaging.

## Package Layout

- `01_reader/`: the directly readable cumulative PDF;
- `02_tex/`: the cumulative TeX and every local TeX input named by the frozen
  build recorder;
- `03_source_authority/`: the exact R823 German cumulative TeX used as source
  authority;
- `04_evidence/`: production ledger, completion gate, source and target unit
  manifests, unit parity, terminology/provenance, build log/recorder, visual-QA
  ledger, and final artifact hashes;
- `05_visual_qa/`: all 19 whole-reader contact sheets plus selected readable
  full-page renders;
- `PACKAGE_MANIFEST.csv` and `SHA256SUMS.csv`: package-level inventory and
  hashes.

The wider Noether Zenodo record separately retains direct article witnesses,
German source-control packages, older cumulative readers, and other language
branches. They are not duplicated wholesale here.

## Status Boundary

This is a substantial source-reconciled Spanish working translation. It is not
a critical edition, a native-language or peer-review certificate, a guarantee
that every mathematical symbol has received independent human verification, or
a publication-grade final edition. The word `complete` inside production logs
means complete for the declared 81-unit corpus and local gate, not critical
certification.

Corrections are welcome through issues or pull requests at
https://github.com/KokunoYumeto/modern-latex-manuscripts.
