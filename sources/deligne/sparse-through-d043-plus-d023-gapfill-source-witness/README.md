# Pierre Deligne sparse maintained corpus through D043

This source tree builds the separate English and French cumulative readers and preserves the editable, source-aligned work files used in the maintained release.

## Coverage

Included complete works, in numerical order: D001-D016, D018, D021, D022, D023, D025-D030, D034-D036, D038-D040, and D043.

Explicit gaps through the current sparse sequence: D017, D019-D020, D024, D031-D033, D037, and D041-D042. The corpus is intentionally sparse: a later independently audited complete work is included even when an earlier work is absent or partial. A subsequently completed gap work is inserted at its numerical position in the next rebuild. D013 is complete at 14/14 physical authority pages and is inserted between D012 and D014. D016 is complete at 97/97 physical authority pages and remains between D015 and D018.

## Build

Run XeLaTeX twice on `Deligne_EN.tex` or `Deligne_FR.tex` from this directory. The entry points include the maintained standalone work PDFs from `works/`. Editable TeX, apparatus, assets, authority witnesses, independent gate receipts, and publication-safe source carriers are kept beside the work files. D013 is preserved under `works/D013_PUBLIC_SAFE` with complete diplomatic French and standalone English TeX/PDF editions, the controlling 14-page authority, restrained apparatus, the exact audited complete-state archive, exact ZERO_ACCEPTED evidence, and the independent corpus-gate receipts. D016 is preserved under `works/D016_PUBLIC_SAFE` with complete French and English TeX/PDF editions, the controlling 97-page authority, restrained apparatus, visual QA, and a fresh nonpatching full-paper cold audit. D018 is preserved under `works/D018_PUBLIC_SAFE` with complete source-language and standalone literal-English TeX/PDF editions aligned to the controlling 174-page authority, restrained apparatus, accepted image fallbacks, visual QA, and a fresh nonpatching full-paper cold audit. D027 is preserved under `works/D027_PUBLIC_SAFE`: English is the source-language edition, French is the faithful translation, and the collected-volume split is comparison-only. D022, D030, D034, D035, D036, D038, D039, D040, and D043 are independent math-typeset editions with restrained apparatus and explicit authority/comparator boundaries. D023 is preserved under `works/D023_PUBLIC_SAFE` with its controlling 30-page authority, source-language English and standalone French math-typeset editions, editable Markdown/TeX, restrained apparatus, comparison-only witness, ZERO_ACCEPTED prior-work ledger, and fresh independent full-paper audit. D013, D016, D023, and D038 are inserted at their numerical locations without regressing later published page streams.

For deterministic cumulative reproduction, set `SOURCE_DATE_EPOCH=946684800`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`, then run `xelatex -interaction=nonstopmode -halt-on-error` twice for each entrypoint, sequentially. This release contains 790 English and 804 French pages. D013 occupies English pages 187-200 and French pages 188-201. The cold-build, include-map, all-page identity, and changed-page visual receipts are under `release_receipts/D013_FORWARD_INTEGRATION/`.

The editable D013 work uses real LaTeX mathematics and `tikz-cd` diagrams with `newtxtext/newtxmath`; compile its standalone TeX with pdfLaTeX. Its audited supplied PDFs are preserved exactly. The independent gate documents byte-identical same-engine cold reruns and text/geometry/raster equivalence across the supplied and current pdfTeX versions. No HTML or raw-text substitute is used as a reader edition.

## Provenance boundary

Raw browser returns and private-path-bearing inherited containers are not published here. Their exact byte identities and ZERO_ACCEPTED dispositions are preserved by publication-safe ledgers, tombstones, sanitized derivatives, and—where independently verified safe—the exact archived state. Nothing in those inherited containers was accepted merely because it existed.
