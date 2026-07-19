# Independent package audit — SGA 2 Exposé V cumulative English checkpoint

Status: **PASS — ready for public archive curator handoff; owner release decision remains pending.**

## Scope and boundary

- Corrected French authority: lines 1770–2136.
- Printed-volume pages: 60–71.
- Exposé V body controls: one-based physical source-PDF pages 55–63 / recomposed running pages 47–55.
- Predecessor context only: physical pages 52–54 / running pages 44–46.
- Continuation cursor: corrected French line 2139, where Exposé VI begins; line 2137 is blank and line 2138 is layout control.
- Fourteen bounded component units were already independently source-reviewed and sealed. This audit independently checks their integration and the cumulative publication object; it does not silently replace their bounded source reviews.

## Independent checks completed

- Recomputed the exact bytes and SHA-256 of all 42 sealed component artifacts: fourteen TeX files, fourteen PDFs, and fourteen independent review seals. All match `COMPONENT_UNIT_INTEGRATION.csv`.
- Recomputed every cumulative target-line segment and matched all fourteen segment hashes to the sealed mathematical bodies. Component order, start/end markers, and target locators are closed and exact; wrapper/preamble changes did not alter any mathematical segment.
- Reverified the corrected French TeX, compiled French PDF, and jcreinhold comparison candidate against their recorded bytes and SHA-256. The French TeX remains translation authority, the French PDF remains ultimate page/visual control, and jcreinhold remains one comparison lineage only.
- Repeated two-pass pdfLaTeX compilation from the cumulative TeX. Pass two has no fatal, undefined, overfull, underfull, missing-glyph, or rerun diagnostics; its only warning is the benign moved margin note on page 6.
- Re-rendered all nine final target pages at 180 dpi and inspected every page. Re-inspected all nine body-source renders and all three predecessor-context renders. No clipping, overlap, blank page, missing glyph, broken diagram, or displaced marginal source marker was found.
- Rechecked PDF structure and fonts: nine A4 pages; thirty reported font rows; every font embedded, subset, and Unicode-mapped. The PDF has descriptive document-information fields but no XMP metadata stream and is not tagged.
- Rechecked source/formula structure at the opening and equations (1)–(4), the editorial sign note, Theorem 2.1 and equations (13)–(14), Theorem 3.1 and its diagram/equation sequence, Proposition 3.5 and equations (24)–(26), the exact `D(epsilon)`-then-`gamma` identity, and Corollary 3.6. No cumulative-body correction was required.
- Strictly reparsed all six CSV ledgers: 568 records total. They pass UTF-8/no-BOM, rectangularity, primary-ID uniqueness, and spreadsheet-formula safety; complete Artifact Tool import/inspection and bounded rendered-preview checks pass.
- Strictly reparsed both JSONL ledgers, including duplicate-key detection, hierarchy closure, revision reciprocity, source/target reference closure, and continuation-cursor consistency.
- Reverified the proposed-payload and all-files manifests before final package-state regeneration. The regenerated manifests are validated again as the final packaging step; French source-page PNGs remain excluded from the proposed public payload.
- Recursive text privacy scan found no private user-root paths, private GitHub-root paths, coordination-inbox names, or UUID-shaped local task identifiers.

## Outcome and caveats

The checkpoint is suitable for immediate handoff to the public archive curator as a bounded, independently audited Exposé V checkpoint. It is not a critical edition or source certification, and no upload was performed. Underlying French-source rights are not granted by this package. The jcreinhold repository's CC BY 4.0 declaration applies only to that comparison candidate and does not license the French source or automatically license this new English translation. Release license, attribution, metadata enhancement, and any public publication action remain public archive curator decisions. No prior public Exposé V checkpoint was discovered; this audited package supersedes the internal assembly self-gate closure `SGA2-V-CUM-ASSEMBLY-SELF-GATE-20260718` only.
