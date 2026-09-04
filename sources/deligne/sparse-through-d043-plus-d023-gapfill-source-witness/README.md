# Pierre Deligne sparse maintained corpus through D043

## Verified GitHub publication

[Release `deligne-d033-gapfill-20260904`](https://github.com/KokunoYumeto/modern-latex-manuscripts/releases/tag/deligne-d033-gapfill-20260904) · [payload commit `b842d35a3cdb`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/b842d35a3cdb66cdc2eeec1a8b13982d643505b7)

Every exact tracked-source path and the payload documentation path passed anonymous commit-pinned byte readback. All six release assets were also downloaded anonymously to EOF and matched their build-receipt byte counts, MD5, and SHA-256 identities. Payload readback receipt SHA-256: `0C0FB3C06EE0D5BB82B9DD295E6B0D512BBC11795D58FCB5716D2CCB4A2A454E`.

This source tree builds the separate English and French cumulative readers and preserves the editable, source-aligned work files used in the maintained release.

## Coverage

Included complete works, in numerical order: D001-D019, D021, D022, D023, D025-D031, D033-D036, D038-D040, and D043.

Explicit gaps through the current sparse sequence: D020, D024, D032, D037, and D041-D042. The corpus is intentionally sparse: a later independently audited complete work is included even when an earlier work is absent or partial. A subsequently completed gap work is inserted at its numerical position in the next rebuild. D013 is complete at 14/14 physical authority pages and is inserted between D012 and D014. D016 is complete at 97/97 physical authority pages and remains between D015 and D017.

## Build

Run XeLaTeX twice on `Deligne_EN.tex` and three times on `Deligne_FR.tex` from this directory; the third French pass verifies settled contents numbers. The entry points include the maintained standalone work PDFs from `works/`. Editable TeX, apparatus, assets, authority witnesses, independent gate receipts, and publication-safe source carriers are kept beside the work files. D013 is preserved under `works/D013_PUBLIC_SAFE` with complete diplomatic French and standalone English TeX/PDF editions, the controlling 14-page authority, restrained apparatus, the exact audited complete-state archive, exact ZERO_ACCEPTED evidence, and the independent corpus-gate receipts. D016 is preserved under `works/D016_PUBLIC_SAFE` with complete French and English TeX/PDF editions, the controlling 97-page authority, restrained apparatus, visual QA, and a fresh nonpatching full-paper cold audit. D018 is preserved under `works/D018_PUBLIC_SAFE` with complete source-language and standalone literal-English TeX/PDF editions aligned to the controlling 174-page authority, restrained apparatus, accepted image fallbacks, visual QA, and a fresh nonpatching full-paper cold audit. D027 is preserved under `works/D027_PUBLIC_SAFE`: English is the source-language edition, French is the faithful translation, and the collected-volume split is comparison-only. D022, D030, D034, D035, D036, D038, D039, D040, and D043 are independent math-typeset editions with restrained apparatus and explicit authority/comparator boundaries. D023 is preserved under `works/D023_PUBLIC_SAFE` with its controlling 30-page authority, source-language English and standalone French math-typeset editions, editable Markdown/TeX, restrained apparatus, comparison-only witness, ZERO_ACCEPTED prior-work ledger, and fresh independent full-paper audit. D013, D016, D023, and D038 are inserted at their numerical locations without regressing later published page streams.

For deterministic cumulative reproduction, set `SOURCE_DATE_EPOCH=946684800`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`, then run `xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error` twice for English and three times for French, sequentially. On the originating Windows workspace, acquire `Global\InterlanguageTeXSlotV1` with a bounded timeout before any TeX process, hold it continuously through the full captured process tree and all passes/log checks, and release it in a finally path after the tree ends. This release contains 1100 English and 1113 French pages. D013 occupies English pages 187-200 and French pages 188-201; D031 occupies English pages 849-891 and French pages 862-904. Current cold-build, include-map, all-page identity, and changed-page visual receipts are under `release_receipts/D033_FORWARD_INTEGRATION/`. Earlier D031 and D017 release receipts and their release-specific narratives are retained as historical evidence. The receipts under `release_receipts/D013_FORWARD_INTEGRATION/` remain exact historical predecessor evidence.

The editable D013 work uses real LaTeX mathematics and `tikz-cd` diagrams with `newtxtext/newtxmath`; compile its standalone TeX with pdfLaTeX. Its audited supplied PDFs are preserved exactly. The independent gate documents byte-identical same-engine cold reruns and text/geometry/raster equivalence across the supplied and current pdfTeX versions. No HTML or raw-text substitute is used as a reader edition.

## Provenance boundary

Raw browser returns and private-path-bearing inherited containers are not published here. Their exact byte identities and ZERO_ACCEPTED dispositions are preserved by publication-safe ledgers, tombstones, sanitized derivatives, and—where independently verified safe—the exact archived state. Nothing in those inherited containers was accepted merely because it existed.

## D031 gap insertion (historical release narrative)

D031, *Shimura Varieties: Modular Interpretation and Techniques for Constructing Canonical Models*, is inserted after D030 and before D034. Both accepted readers contain43 physical pages aligned to printed247-289; page290 is absent. French is diplomatic and English is a standalone translation. Exact native editable TeX, Markdown,12-page apparatus, controlling authority and comparison-only witness are under `works/D031_PUBLIC_SAFE`. The native readers contain23 TikZ-CD and7 native Dynkin diagrams each, no image fallbacks.

Compile `normalized/english_translation.tex`, `normalized/french_diplomatic.tex`, or `normalized/apparatus.tex` with pdfLaTeX twice from that directory. These self-contained native sources reproduce the maintained readers; the cumulative XeLaTeX instructions above remain applicable. Historical gate build scripts with literal local-account substitutions are evidentiary derivatives, not portable entrypoints.

The supplied original archive remains private and unchanged. Its original name/size/hash and every original-to-public member identity are in `works/D031_PUBLIC_SAFE/D031_ARCHIVE_DERIVATIVE_RECEIPT.json`; the public-safe archive is included exactly once. Only literal local-account substrings in matching text leaves were replaced, while all unaffected member bytes remain exact. Historical internal manifests still attest original bytes, with the external derivative graph explaining changed ancestors. The nested raw editions and215 inherited salvage records remain ZERO_ACCEPTED and are not accepted reader input.

The maintained D031 reader PDFs include one independently validated presentation-only derivative: physical33 printed279 has a vertical-arrow label positioned at75percent to clear an oblique arrow. Exact original gate PDFs/TeX remain under `works/D031_PUBLIC_SAFE/gate_normalized_witness/`. The separate `D031_PRESENTATION_VALIDATION_RECEIPT.json` records the ten-byte TeX option insertion, original/current hashes, all43 raw extracted-text identities with PyMuPDF and whitespace-normalized text identities with independent pypdf extraction,42 unaffected native-page raster identities and final cumulative QA. Independent pypdf extraction changes one inter-label whitespace on page33; the text tokens remain exact. There is no mathematical-source change or promotion of inherited salvage.

## D017 gap insertion (historical release narrative)

D017, *Formes modulaires et représentations de GL(2)* / *Modular forms and representations of GL(2)*, is inserted immediately after D016 and before D018. The accepted standalone French and English readers contain 52 pages each; the controlling 51-page authority, editable TeX/NDJSON, restrained apparatus, accepted image fallbacks, and public-safe provenance chunks are preserved under `works/D017_PUBLIC_SAFE`. The cumulative rebuild is independently checked at 885 English and 899 French pages. All inherited evidence remains ZERO_ACCEPTED; no source master is modified.

## D019 gap insertion (historical release narrative)

D019, *Hodge Theory III* / *Théorie de Hodge III*, is inserted after D018 and before D021. The current cumulative books contain 1040 English and 1053 French pages. The independently accepted canonical editions contain 155 English and 154 French reader pages aligned to 73 article pages; the 74-page authority includes an excluded cover. Exact canonical PDF/TeX/data/assets, the complete reproducible source packet with its original authority, and canonical acceptance evidence are preserved under `works/D019_PUBLIC_SAFE`. The separately admitted lossless transport PDFs used for cumulative inclusion preserve all text and image samples. They do not replace canonical bytes. All inherited source witnesses remain byte-identical and inherited evidence remains ZERO_ACCEPTED. Earlier release-specific narrative remains historical.

## Nonincluded work status snapshot (2026-09-04)

This parent-supplied intake snapshot does not promote a returned browser packet to normalized acceptance. D032 S20 and D037 S05-GA01 are complete return claims awaiting independent deterministic gates, not active partial claims. D048 S14 is a returned facsimile-witness packet at 84/86 physical and 83/85 article pages; next P15 covers physical 85-86 / printed 88-89. It is not normalized acceptance. D020 remains 30/36 with P06 next; D044 remains 54/174 with P10 next. These works are not inserted by this D019 release.

## D033 gap insertion

D033 is inserted after D031 and before D034. English is the original source-language edition; French is its translation. Each reader contains 60 pages aligned to printed 227-286. D033 occupies English cumulative pages 892-951 and French cumulative pages 905-964. The three-page apparatus is preserved separately and is not appended to either cumulative reader. Canonical reader PDFs and editable TeX remain exact under `works/D033_PUBLIC_SAFE`; the complete source ZIP remains unchanged. Its archived returned convenience-reader PDFs are not cumulative inputs.

Included coverage: D001-D019; D021-D023; D025-D031; D033-D036; D038-D040; D043. Explicit public gaps: D020; D024; D032; D037; D041-D042. These public gaps identify works outside this cumulative release; they are not missing downloads.

The local orchestrator uses three to five bounded XeLaTeX passes per clean replica and requires settled TOC and PDF hashes, with three independent clean replicas. All passes and immediate log checks share the single machine-wide TeX mutex and captured-process-tree contract stated above. New local raw evidence stays outside public packaging roots; separately hash-mapped literal-name derivatives preserve public provenance without changing historical original-hash claims.
