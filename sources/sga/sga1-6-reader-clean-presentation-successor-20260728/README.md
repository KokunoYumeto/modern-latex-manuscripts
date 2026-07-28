# SGA 1-6 reader-clean presentation successor

This package replaces the five principal English SGA 1, 2, 4, 5, and 6
reader PDFs and their direct master TeX files in place. The mathematical
bodies, diagrams, labels, and reference infrastructure are preserved.
Reader-facing production commentary is not.

The replacements remove:

- SGA 1's translation-source subtitle and `Source and status note`;
- SGA 2's appended `English-reader note`;
- SGA 4's release-state line and standalone `Source and rights notice`;
- SGA 5's machine-assistance wording from PDF metadata; and
- SGA 6's `Editorial status` page and terminal editorial source-note
  appendix.

The public filenames remain unchanged so the compact landing surface gains
cleaner books without another row of competing reader variants.

## Validation

`PACKAGE_VALIDATION.json` records page counts, PDF metadata, named
destinations, internal links, page-size checks, phrase scans, and exact
normalized page-text comparison against Zenodo record `21650398`.

The comparison allows only the pages deliberately affected by the removed
front matter or appendix. In particular:

- SGA 5 is text-identical on all 309 pages;
- SGA 2 differs only on the editor-preface page where the appended project
  note was removed;
- SGA 4 differs only on the title page and now-blank verso;
- SGA 1 otherwise matches the predecessor with its one-page offset; and
- SGA 6 otherwise matches the predecessor with its one-page offset.

The five readers remain scholarly working translations with their existing
scope and quality qualifications. This cleanup is not a new critical-edition,
rights-clearance, peer-review, accessibility, or exhaustive-reference claim.
Provenance, rights qualifications, validation evidence, and superseded
states remain available in external release metadata and grouped archive
ZIPs rather than interrupting the books.

Existing SGA concept DOI: `10.5281/zenodo.20410947`.

