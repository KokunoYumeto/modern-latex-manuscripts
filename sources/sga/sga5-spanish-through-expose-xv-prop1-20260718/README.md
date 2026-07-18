# SGA 5 Spanish source-reconciled working checkpoint

Open `output/pdf/sga5_es.pdf` first. It is a 296-page Spanish working reader built from 345 editable TeX units.

## Included coverage

The integrated Spanish branch is reconciled unit by unit against the frozen French SGA 5 workpass, with scan checks recorded by the production lane, through complete Exposes I, III A, III B, V, VI, VII, VIII, X, and XII. Expose XV is included through section 2, no. 1, including the complete proof of Proposition 1 on Frobenius correspondences.

The next source cursor is French authority line 14682, Expose XV section 2, Proposition 2. Draft text exists beyond that boundary in the live production lane, but it is intentionally excluded here.

## Rebuild

Run `build.ps1` from this directory. The script verifies the bundled frozen French authority hash, regenerates unit and expanded-document hashes, compiles with `latexmk`, and rejects warnings, box errors, missing characters, undefined controls, and fatal errors.

The editable master is `sga5_es.tex`; its 345 referenced bodies are in `units/`. The bundled local authority is `authority/sga5_fr_workpass.tex`. Build and source-reconciliation evidence is in `evidence/`.

## Verification

- Expanded TeX target SHA-256: `3524CCA58E27491CEF0339B84E2C8C772DB9AD103495A3D58301FBC5FE8F5B14`.
- Frozen French authority SHA-256: `791F4EFFC5E02832D5D77ED03518C8156D6F07E4C8238B03545DB93D883FBB28`.
- Production reader PDF SHA-256 before release rebuild: `F675ECBFECC98C0E6BF2D27E9829D190FA535014C481D7F89F6E9E91642DEFB8`.
- Production build: 296 pages and zero forbidden diagnostics.
- Tail pages 290-296: rendered with Poppler at 160 dpi and inspected at original resolution.

## Status boundary

This is substantive source-reconciled translation work, not OCR-only output. It is an intentionally incomplete SGA 5 Spanish working edition. It is not an independently human-certified translation, a critical edition, a publication-grade proofread edition, or a claim that every diagram and formula is error-free.

The printed scan remains an audit witness and is not redistributed in this compact package. The broader SGA archive retains source-support material used by the project.
