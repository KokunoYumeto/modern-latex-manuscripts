# EGA 0 and EGA III English complete readers — reference-v2 successor

This no-overwrite successor contains the complete local English EGA 0 reader
through section 13 and the complete published EGA III reader through section
7, together with editable TeX and exhaustive machine-readable reference data.

The two final readers are:

- `EGA0_English_Complete_Through_Section13_Reference_v2.pdf` — 120 pages;
- `EGAIII_English_Complete_Sections1_Through7_Reference_v2.pdf` — 150 pages.

The reference graph is split deliberately:

- `REFERENCE_TARGETS.csv` records every delivered named PDF destination;
- `REFERENCE_TARGET_ALIASES.csv` maps active TeX labels to those destinations;
- `REFERENCE_CANDIDATES.csv` is the exhaustive visible source-reference universe;
- `REFERENCE_APPLICATIONS.csv` records compiled same-reader applications;
- `REFERENCE_RESIDUALS.csv` records positive nonedges, chiefly external-volume,
  external-work, unpublished-section, and structural locators;
- `REFERENCE_EDGES.csv` is the complete delivered-PDF GoTo graph.

The exact set relation is
`REFERENCE_CANDIDATES = REFERENCE_APPLICATIONS disjoint-union REFERENCE_RESIDUALS`.
The PDF-edge universe is separate because it also contains inherited table-of-
contents and other automatically generated navigation links.

No OCR was generated, rerun, or packaged. Existing Floris GPU OCR was used only
as locator/drafting support during the source-first translation stage. The two
frozen NUMDAM French PDFs controlled source decisions and are not redistributed
in this package.

This is a source-aligned working English edition, not a critical edition,
proofreading certification, legal determination, or tagged/accessibility-
remediated PDF.
