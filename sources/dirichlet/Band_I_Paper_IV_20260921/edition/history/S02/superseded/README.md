# Dirichlet · Band I · Paper IV · Prompt 02 cumulative state

**Current checkpoint:** Prompt 02 completed; next cursor **3**. This release accepts exactly printed **65–86** in the diplomatic French edition, independent English translation, and separate pagewise apparatus. The title leaf63 and blank verso64 remain logged copy matter and are excluded from both author readers. Printed87–98 are untouched by this release. Paper IV as a whole is **not complete**; Prompt03 and the independent final cold audit remain required.

## Current editable sources and readers

| Layer | Editable source | Current reader | PDF pages |
|---|---|---|---:|
| Diplomatic French | `editions/fr/main.tex` and `editions/fr/pages/p065.tex`–`p086.tex` | `readers/PAPER_IV_FR_PP065_086.pdf` |22|
| Faithful English | `editions/en/main.tex` and `editions/en/pages/p065.tex`–`p086.tex` | `readers/PAPER_IV_EN_PP065_086.pdf` |22|
| Separate apparatus | `apparatus/main.tex`, `apparatus/pages/`, `apparatus/CATALOGUE.tsv` | `readers/PAPER_IV_APPARATUS_S02.pdf` |3|

The two author readers are monolingual and independent. Each has exactly one output page for each accepted printed page; their first page is65, not63. The apparatus catalogue contains22 page records. The old three S01 readers remain at their original filenames as prior evidence, not the current extent. The current reader identities and hashes are in `state/CURSOR.json` and the external checkpoint.

## Validated starting state and preservation

The actual accepted S01 ZIP used here was `DIRICHLET_P04_S01_CUMULATIVE_FULL_STATE.zip`, **131808818 bytes**, SHA-256 **DEE2786989BCE3556912265B110856DB4578181386E322E4FC97CE64D583F162**. Its240 file members, standalone manifest/diff bindings, and exact accepted FR/EN/apparatus65–74 with cursor2 were revalidated from bytes. See `qa/s02/S01_INTAKE_VALIDATION.json` and `S01_INTAKE_MEMBER_VALIDATION.tsv`.

All240 S01 member byte sequences are preserved. Unchanged files remain at their original paths. The S01 versions of changed cumulative mains, apparatus main/catalogue, ledgers, README, cursor and diff are under `prior_evidence/S01/`; the three external S01 metadata files are there too. `qa/s02/S01_MEMBER_PRESERVATION.tsv` identifies the preservation location of every original member. **The previous cumulative ZIP is not nested.** Historical zero-page input-access evidence remains in `prior_evidence/input_access_checkpoint/`; it is not current state and has not been counted as a transcription.

The21 original packet members remain unchanged in `input/`. The raw controlling PDF, full-volume PDF, and original R27/R28 ZIPs are unchanged. The inherited R27 files and all51 unpacked R28 files are retained under `inherited/`. Their cumulative PDFs contain earlier papers and are preserved only as archival evidence, never used as author-reader content. The original R27/R28 bytes themselves remain labelled unverified prior work: acceptance applies only to the authority-replayed derivative editions.

## Source scope and this session's collation

The controlling witness is `input/10_AUTHORITY_EXACT_SCOPE_PDF_PAGES_080_115_PRINTED_PP063_098.pdf`. The unchanged full-volume PDF supplies provenance. `input/05_PAGE_MAP.tsv` fixes full-PDF page = printed page+17 and exact-scope leaf = printed page−62.

Prompt02 processed printed75–86, full-PDF92–103, exact leaves13–24. Printed75–80 were replayed pagewise against the source using the inherited R28 French and English units only as comparators. All396 physical lines of the two inherited TeX files are classified in `qa/s02/INHERITED_TEX_LINE_AUDIT.tsv`. The six R28 witness PNGs were additionally proved pixel-identical to the matching controlling-PDF grayscale renders at110dpi. Printed81–86 were transcribed directly from the controlling scans and translated completely. No OCR or external comparator supplied author text.

`qa/s02/UNIT_ALIGNMENT.tsv` records85 new aligned units. `FORMULA_AUDIT.tsv` records499 new paired inline/display math segments, including isolated variables and whole arrays; these counts are not counts of numbered equations. After manual source review, all paired math tokens and placement agree across FR/EN, except explicitly translated “ou/or” and layout spacing. `SOURCE_LINE_AUDIT.tsv` maps508 French and508 English editable TeX lines to source passages. Its numbers are **edition-source line numbers, not claimed physical scan-line numbers**. The code does not perform human collation.

Cumulative indexes under `qa/s02/CUMULATIVE_*` combine preserved S01 evidence and this session's records:139 aligned units,914 paired math segments, and all22 accepted author pages. Their inclusion does not claim an independent final cold collation. The original S01 QA files under `qa/` remain historical evidence; the new session's current QA is in `qa/s02/`.

## Diplomatic treatment and separate apparatus

Printed wording, equations, signs, primes, exponents, parentheses, labels, quoted propositions, paragraph starts, source page seams, and author note anchors are retained. Running heads and the volume imprint are translated in English. Physical line wrapping within a source page is re-typeset rather than photographically copied; line-end word division is reflowed without modernizing lexical hyphens. Original page boundaries and display groupings are explicit.

Legible source discrepancies are not silently repaired. This session retains the **t** in the p77 “8n+7 / 8n+3” sentence, **p²=φ²+ψ²** on p82, and **t²+au²=ps** without an exponent on that s on p85 in both editions. The apparatus records these separately, with source details. The previously accepted p66 and p70 source issues and the restored p71 author note remain unchanged. There are no new author footnotes75–86; the p86 reference points to the note near the start of section3 on p71. No unresolved illegible-source ambiguity remains in this batch.

The first p86 draft omitted the terminal point after each of two three-dot ellipses. Both source points were restored in FR and EN, each reader rebuilt twice, and both final p86 pages re-inspected. The source detail and before-draft files are preserved. No content from p87 has been introduced.

`SOURCE_BACKED_DIFF.tsv` is cumulative: the44 S01 rows are retained verbatim, followed by26 concrete S02 correction rows. `qa/s02/SOURCE_BACKED_DIFF_S02.tsv` isolates the new rows. New untouched-page production is not misrepresented as correction of inherited content. Legible source discrepancies retained without emendation are recorded in apparatus, not as invented before/after corrections.

## Build, layout, seams and regression

All three current documents were compiled with XeLaTeX twice in the final verified run: six successful passes, **22/22/3 pages**, with no final warnings, overfull/underfull boxes, or missing-glyph reports. Logs and engine version are in `qa/s02/build/` and `qa/s02/XELATEX_VERSION.txt`. Earlier repaired build/draft evidence is retained in `qa/s02/build/repair_history/` and is not current build state. Font embedding was checked; no standalone font files are distributed.

All47 current PDF pages were rendered at126dpi. The24 added author pages and all3 apparatus pages were inspected individually. The20 unchanged author pages were reviewed in current-render pair sheets and also checked for exact text and full126dpi pixel identity to accepted S01. All20 matched exactly. All accepted S01 author page sources, apparatus page notes, and page-state records remain byte-identical. See `VISUAL_AUDIT.tsv`, `PDF_GEOMETRY_AUDIT.tsv`, `EMBEDDED_FONT_AUDIT.tsv`, `S01_READER_REGRESSION.tsv`, and `BUILD_AND_VISUAL_RECEIPT.json`.

`PAGE_SEAM_AUDIT.tsv` checks74/75,80/81, and every intermediate seam through85/86. Page75 resumes the section4 factor proof immediately, without R28's added continuation title. The factor list crosses79/80 after h,; the prose crosses83/84 after “ce qui est la”, and85/86 after “d'être beaucoup”. English breaks at the corresponding argument position. Printed86 ends at the final reciprocal-symbol row, not a fabricated end of the paper.

## Rebuilding this extent

From this unpacked root, `python tools/s02/build_s02.py` rebuilds the two cumulative readers and apparatus twice and renders them. It requires XeLaTeX with the standard packages specified in each main, Latin Modern fonts from TeX, PyMuPDF and Pillow. Each main can also be compiled directly, with its containing directory as the working directory. The current main sources are self-contained with their own page files.

`tools/s02/validate_intake.py` checks the original S01/input-package ZIPs when those sibling files are available. `make_records_s02.py` and `finalize_qa_s02.py` encode the completed collation and visual observations and supplement them with mechanical checks; rerunning a script is not a substitute for reviewing edited text or changed renders. Historical tools under `tools/` outside `tools/s02/` are preserved S01 evidence and are **not** the current orchestration path. Extent-specific authoring scripts must not be used to reset a later cumulative state.

## Four-file handoff and non-circular hash contract

The required siblings are the S02 cumulative ZIP, external `CHECKPOINT.json`, external `MANIFEST.tsv`, and external `SOURCE_BACKED_DIFF.tsv`. The external checkpoint binds the ZIP, manifest, diff, and every ZIP member by uppercase SHA-256 and byte length. The manifest has exactly one normalized relative-path row per file member, with role, acceptance, page range and provenance. The ZIP includes the current `state/CURSOR.json` and a byte-identical cumulative diff. The external checkpoint and manifest are not recursively embedded as current members; their S01 predecessors are preserved as historical evidence.

The release is built in sorted-path order with fixed timestamps and file modes, built a second time to verify deterministic ZIP bytes, then reopened to verify CRC, safe unique normalized names, exact manifest membership, all member hashes and checkpoint bindings. Run `python tools/s02/verify_handoff_s02.py /path/to/DIRICHLET_P04_S02_CUMULATIVE_FULL_STATE.zip` with the three metadata siblings beside it to recheck the handoff independently.

**Stop point: next cursor3, first untouched author page87.** No Prompt03 execution and no final cold-audit claim are part of this release.
