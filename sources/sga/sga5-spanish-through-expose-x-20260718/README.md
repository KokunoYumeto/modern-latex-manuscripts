# SGA 5 Spanish source-reconciled working checkpoint

Open `output/pdf/sga5_es.pdf` first. It is a 268-page Spanish working reader built from 297 editable TeX units.

## Included coverage

The integrated Spanish branch is reconciled unit by unit against the frozen French SGA 5 workpass, with scan checks recorded by the production lane, through complete Exposes I, III A, III B, V, VI, VII, VIII, and X. Expose X includes section 7, Corollary 7.12, Lemma 7.14, their proofs, and the references.

The next source cursor is the opening of Expose XII. Draft text exists beyond the released cursor, but it is intentionally excluded until it receives the same ordered source and scan reconciliation.

## Rebuild

Run `build.ps1` from this directory. The script verifies the frozen French authority hash, regenerates unit and expanded-document hashes, compiles with `latexmk`, and rejects warnings, box errors, missing characters, undefined controls, and fatal errors.

The editable master is `sga5_es.tex`; its 297 referenced bodies are in `units/`. Build and source-reconciliation evidence is in `evidence/`.

## Verification

- Expanded TeX target SHA-256: `459D0DA0155E6846E157BBA0EE150DB22DBD7D2A7CD2547CC0596B10EFC83F23`
- Frozen French authority SHA-256: `791F4EFFC5E02832D5D77ED03518C8156D6F07E4C8238B03545DB93D883FBB28`
- Reader PDF SHA-256: `5E936A2A39EC229BDA12DEE0446B23FB53A5722AB10167489D7B6EE88FB8ACBB`
- Build: 268 pages, zero forbidden diagnostics
- New tail pages 264-268: rendered with Poppler at 160 dpi and inspected at original resolution

## Status boundary

This is substantive source-reconciled translation work, not OCR-only output. It is an intentionally incomplete SGA 5 Spanish working edition. It is not an independently human-certified translation, a critical edition, a publication-grade proofread edition, or a claim that all SGA 5 diagrams and formulas are error-free.

The underlying scan is an audit witness and is not duplicated in this compact package. The broader SGA Zenodo record retains the French source workpass and source-support materials used by the project.
