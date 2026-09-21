# Dirichlet — Band I, Paper IV — Prompt 01 checkpoint

Status: **Prompt 01 complete; whole-paper project in progress. Next cursor: 2.**

The accepted French, English and apparatus page sets are each exactly
`65, 66, 67, 68, 69, 70, 71, 72, 73, 74` (10 of the eventual 34 author pages).
Printed pp.63–64 are the title copy leaf and blank verso, logged separately and
excluded from both author-text readers. The fixed topology for pp.63–98 has been
validated, but validation of that map is not textual acceptance of pp.75–98.
Prompt 02 has not been executed. The first unprocessed author page is 75.

## Current editions

`readers/PAPER_IV_FR_PP065_074.pdf` and
`readers/PAPER_IV_EN_PP065_074.pdf` are independent monolingual, ten-page readers.
Their editable sources are in `editions/fr/` and `editions/en/`, with one TeX file
for each original author page. Each reader includes each of its page records once.
`readers/PAPER_IV_APPARATUS_S01.pdf` is the separate two-page editorial apparatus;
its TeX and ten pagewise Markdown records are in `apparatus/`.

The French retains the printed wording and notation, including legible source
problems. The English retains the complete arguments and mathematical relations.
The p.71 author footnote appears in both readers, anchored as printed. Editorial
comments do not intrude into the author text. The p.66 unqualified converse and the
p.70 printed plus sign remain unchanged and are discussed only in the apparatus.
There are no unresolved illegible-source ambiguities in the current batch.

These readers are diplomatic, source-page-bounded re-typesettings, not facsimile
images. Source paragraph starts, page seams, formula placement/grouping,
punctuation, headings, quotation marks and note anchors are retained. Physical
within-page line wrapping and discretionary line-end hyphenation are reflowed;
lexical hyphens are retained. French running heads and imprints are reproduced,
and translated in English. Signature marks are retained as page furniture, not
miscounted as author-page numbers. The authority images retain the exact original
lineation and typography. The source has no visible folio 65: its identity is
established by the fixed page map; the reader does not invent a visible folio.

## Authority and preserved inputs

`input/` contains all 21 files extracted byte-for-byte from the directly attached
input package. The suffixed and unsuffixed mounted packet ZIPs were readable,
CRC-valid and byte-identical. All 21 loose mounted Project copies also match.
See `qa/MASTER_ZIP_VALIDATION.json` and `qa/LOOSE_ATTACHED_COPY_VALIDATION.tsv`.
The large outer input package itself is not duplicated inside this cumulative
ZIP; its 21 original members and its exact digest are preserved instead.

The exact-scope PDF is controlling. All 36 of its page rasters match the
corresponding full-volume pages at 72 dpi. The untouched full-volume PDF is
retained for provenance, not ingested as text outside Paper IV. The following
work's boundary title was inspected only; no Paper V text was transcribed or
translated, and its temporary derived image was discarded.

Both original inherited ZIPs are preserved unchanged in `input/`. R27 is also
unpacked without byte changes in `inherited/R27/`. Its 46 original files remain
preserved evidence; they are not substitutes for the accepted current editions.
Every line of its French and English TeX was classified and its author content
replayed against the controlling scan. Its ten scan leaves match the authority.
R28's 51 member hashes and ZIP CRC were validated, but its text was not processed
or accepted in Prompt 01. Old cumulative readers include earlier papers: those
bytes are preserved only, never incorporated into the current author readers.

The earlier failed input-access checkpoint accepted zero author pages. Its full
contents and standalone metadata are preserved under
`prior_evidence/input_access_checkpoint/`; they do not describe current status.
The old cumulative ZIP itself is not nested. Preservation hashes are in
`qa/PRIOR_ACCESS_CHECKPOINT_PRESERVATION.json`.

## Audit evidence

`SOURCE_BACKED_DIFF.tsv` has 44 concrete correction/alignment rows, with authority
page identities and specific witness locations. Its ellipses and compressed
formula descriptions are diff notation only; the editions do not substitute
summaries for the source. Typographic and structural repairs are distinguished
from repairs of inherited mathematical or lexical errors.

`qa/UNIT_ALIGNMENT.tsv` aligns 54 units, including headings and rule records.
`qa/FORMULA_AUDIT.tsv` records 415 inline/display mathematical segments; this
includes variable mentions and is not a count of distinct equations. Formula
tokens match across French and English apart from translated prose inside math.
`qa/SOURCE_LINE_AUDIT.tsv` has 420 audited editable French TeX lines: these are
explicitly edition-source line numbers, not invented physical scan-line numbers.
`qa/INHERITED_TEX_LINE_AUDIT.tsv` classifies every physical line of both R27 TeX
files, with source-page evidence for content and a separate wrapper disposition.
`qa/NOTE_AUDIT.tsv` covers the full author note and anchor.

`qa/VISUAL_AUDIT.tsv` records direct inspection of every final French page (10),
English page (10), and apparatus page (2), with render and reader hashes.
The final second-pass logs contain no warnings, overfull/underfull boxes, or
missing-character reports. Expected first-pass rerun notices were resolved by
the second pass and are recorded rather than concealed. Final output renders,
source images, geometry checks and build logs are retained. Two repaired build
issues have separate historical logs, not current acceptance status.

## Handoff metadata and verification

The four release siblings are the cumulative ZIP, `CHECKPOINT.json`,
`MANIFEST.tsv`, and `SOURCE_BACKED_DIFF.tsv`. Keep them together.

The **external** manifest hashes every regular-file member of the ZIP exactly
once. The **external** checkpoint binds the ZIP, manifest, standalone diff and all
member hashes. The ZIP includes the byte-identical diff and the self-contained
`state/CURSOR.json`, exact accepted-page records and all working evidence. The
external checkpoint and external manifest are not nested inside the archive:
this avoids circular archive/self-hash claims. A checkpoint cannot contain its own
SHA-256; it binds all the other release artifacts instead. The manifest has no
self-exclusion because it is not itself an archive member.

The ZIP has sorted normalized relative member names, fixed timestamps and file
modes. It contains no earlier cumulative ZIP, no symlinks, and no standalone font
files. Font subsets embedded in reader PDFs are ordinary PDF content.

After unpacking the cumulative ZIP, verify the release with:

```sh
python tools/verify_handoff.py /path/to/DIRICHLET_P04_S01_CUMULATIVE_FULL_STATE.zip \
  /path/to/MANIFEST.tsv /path/to/CHECKPOINT.json /path/to/SOURCE_BACKED_DIFF.tsv
```

The verification reads the archive again, checks CRCs, safe unique normalized
paths, every member length/hash, exact manifest coverage, standalone diff
identity, accepted page sets, internal cursor, page-record hashes, and external
checkpoint artifact bindings.

## Editing and resumption

Current page TeX files are the editable edition sources. To rebuild this frozen
Prompt 01 state, run `python tools/build_readers.py`; it builds each author reader
twice and refreshes all author-page renders. Apparatus editing is in
`apparatus/main.tex`; compile it twice with XeLaTeX. The `write_*` scripts preserve
the original authoring recipe and can overwrite files: do not rerun them over
later corrected or extended state without first updating the recipe.

Visual acceptance is not created by compiling or by automated tests. Any later
source change requires comparison with the authority, updated diff/page records,
two builds and inspection of the affected output, then new package bindings.
The supplied `finalize_qa.py` contains this session's explicit manual observation
receipt; it must not be used to assert visual inspection of unseen future pages.

On a later instruction to proceed, first read `input/00_READ_FIRST.md` and files
01–09, validate the handoff, then execute `input/21_PROMPT_02_PP075_086.md`.
Preserve the current evidence and old bytes; do not nest this cumulative ZIP in
the next one. Prompt 04's independent whole-paper cold audit remains future work.
