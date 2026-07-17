# Final build and warning audit

Audit date: 2026-07-17, Europe/Berlin.

## Frozen outputs

- TeX SHA-256: `3CC5204680B2A2CE92FDF09401AB1A4654F9E0A4B0ED932D110FC0B1B024720F`.
- PDF SHA-256: `176759209CD284F1DD6D3E26D0C7600EC146AB01FAA637BF6F6BB97BFAA396A4`.
- PDF properties: 309 letter-size pages; 2,054,026 bytes; PDF 1.5;
  unencrypted.
- Build command, both passes:
  `pdflatex -interaction=nonstopmode -halt-on-error -file-line-error SGA5_English_sync_workpass.tex`.
- Evidence: `BUILD_FINAL_PASS1_20260717.log`,
  `BUILD_FINAL_PASS2_20260717.log`, and their console captures.

## Diagnostic result

Both final passes completed. The final pass contains:

- fatal errors: 0;
- LaTeX warnings: 3 localized font warnings;
- package warnings: 0;
- pdfTeX warnings: 0;
- underfull boxes: 0;
- overfull boxes: 9.

The three LaTeX font warnings occur at TeX lines 3258, 3485, and 5740, where
`\\scriptsize` is requested inside math mode. They map to PDF pages 63, 67, and
118. All three pages were rerendered at 180 dpi and directly inspected: the
affected diagrams and formula labels are complete, legible, and inside the
page. These are formatting warnings, not missing glyphs or source-content
losses.

The nine overfull diagnostics are localized at TeX lines 415–417 (38.56 pt),
2234–2236 (10.82 pt), 2664 (11.47 pt), 3850–3852 (23.10 pt), 4237–4239
(0.29 pt), 4398–4400 (11.66 pt), 5490 (5.14 pt), 5626–5628 (8.09 pt), and
13617–13618 (15.10 pt). Their rendered pages were inspected. The affected
mathematical or bibliographic material remains visible within the physical page;
there is no crop, overlap, lost formula, or unreadable edge text.

## Layout repairs made before freeze

- The long bold underline on PDF page 4 was made breakable with `ulem`; the
  previously clipped final words now wrap normally.
- The large §5.12.3 diagram on PDF page 118 was recast in the compact
  source-authority layout, removing severe right-edge clipping without changing
  its nodes, arrows, or labels.
- `hypertexnames=false` removed approximately 1,399 duplicate destination
  warnings; `\texorpdfstring` repaired the mathematics-bearing bookmark; five
  literal `X_{\mathrm{ét}}` forms were normalized to the established `X_{\et}`
  macro to remove invalid accent warnings.

These are layout/metadata repairs. They do not alter the source-critical English
content. A clean compile is only one promotion condition; the formula,
terminology, structural, and rendered-page evidence remains independently
required.
