# Round 6 - actual fixed delta with cumulative folder

This is not a final corpus package. It is a focused replacement bundle.

## Directory use

- `new-this-round/replacement-pdfs/`: the five replacement PDFs produced in this pass.
- `new-this-round/patched-tex/`: patched TeX sources used for those PDFs.
- `cumulative-actually-fixed/replacement-pdfs/`: the round-5 accepted replacements plus the five new round-6 replacements.
- `cumulative-actually-fixed/patched-tex/`: patched TeX sources for the same cumulative set.
- `reports/`: manifests, text sweeps, final compile logs, page-removal notes, and render samples.

## New replacements in this round

- `10-14 English Translation - Robert of Chester and Karpinski.pdf` - 28 pages, 153435 bytes, actionable text-sweep hits: 0.
- `10-15 English Translation - Omar Khayyam - Treatise on Algebra.pdf` - 15 pages, 125405 bytes, actionable text-sweep hits: 0.
- `10-16 English Translation - Rosen - Algebra of Mohammed Ben Musa.pdf` - 42 pages, 262909 bytes, actionable text-sweep hits: 0.
- `60-04 Islamic Original - Omar Khayyam - Treatise on Algebra.pdf` - 15 pages, 125405 bytes, actionable text-sweep hits: 0.
- `70-05 Reference Text - Smith-Karpinski - Numerals.pdf` - 23 pages, 137031 bytes, actionable text-sweep hits: 0.

## What was fixed in this round

- Robert of Chester/Karpinski: rebuilt from TeX with working Linux Libertine/Biolinum font declarations; removed the broken visible `oemtitleo>`/`columnrule` first page by replacing the PDF; pruned 20 empty/title-only spacer pages from the delivered replacement.
- Omar Khayyam: repaired the `tcolorbox` title option failure that produced visible `tcb@breakable`; moved Arabic runs to Amiri to avoid Arabic/Latin missing-glyph failures; removed process-footers about XeLaTeX/polyglossia/font choices. The same repaired source is provided under the English and Islamic-original filenames because the existing held outputs were variants of the same bilingual/source-facing reader.
- Rosen: fixed a source command collision around `\ar`, corrected the corrupted `الخوارزmi` Arabic token to `الخوارزمي`, and removed a blank spacer page.
- Smith-Karpinski Numerals: rebuilt and rechecked from source. Its prior hold reason was driven by broad false positives around ordinary text such as `title`/bibliographic language; the rebuilt PDF has no actual HTML/404 contamination in the current sweep.

## Validation notes

- New round-6 replacements compiled with zero final-pass `Missing character` warnings in the included logs.
- New round-6 replacements have no post-prune near-blank pages by the current text-count audit.
- New round-6 replacements have no `oemtitleo`, `columnrule`, `tcb@`, `sectioncolor`, `commentarycolor`, local path, process-agent label, or replacement-character hits in the current text sweep.
- Render samples are in `reports/render-samples/new/`; the contact sheet is `reports/round6_new_replacements_contact_sheet.jpg`.
- `Codex` appears in the Robert/Karpinski PDF only as bibliographic/manuscript language such as `Codex Vindobonensis`, not as an agent/process label.

## Held / not fixed here

- Arabic translation `30-05 Arabic Translation - al-Khwarizmi - Algebra.pdf` is still held; the available source is not clean Arabic-script translation throughout.
- Omar Arabic translation `30-06` is not shipped in this delta; only the bilingual/source-facing Omar files listed above were repaired.
- Ruska `60-05` was attempted but not shipped: it still has source-level Greek/transliteration macro failures and pages with mathematical symbol boxes. Do not upload it from this package.
- Combined readers are not rebuilt here. Rebuild them only after enough component PDFs have been replaced, otherwise damaged held components will be reintroduced.

## Cumulative replacement set

- `10-11 English Translation - al-Kashi - Miftah al-Hisab.pdf` - 30 pages
- `10-12 English Translation - al-Khwarizmi - Algebra.pdf` - 30 pages
- `10-14 English Translation - Robert of Chester and Karpinski.pdf` - 28 pages
- `10-15 English Translation - Omar Khayyam - Treatise on Algebra.pdf` - 15 pages
- `10-16 English Translation - Rosen - Algebra of Mohammed Ben Musa.pdf` - 42 pages
- `30-04 Arabic Translation - al-Kashi - Miftah al-Hisab.pdf` - 29 pages
- `60-01 Islamic Original - al-Kashi - Miftah al-Hisab.pdf` - 27 pages
- `60-02 Islamic Original - al-Khwarizmi - Algebra.pdf` - 33 pages
- `60-04 Islamic Original - Omar Khayyam - Treatise on Algebra.pdf` - 15 pages
- `70-05 Reference Text - Smith-Karpinski - Numerals.pdf` - 23 pages
