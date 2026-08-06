# Sylvester GitHub Coverage Map

Observed 2026-08-06. This page records the James Joseph Sylvester material
whose bytes are actually present in GitHub. The current reading surface is a
source-page-marked working edition of *The Collected Mathematical Papers*,
Volume I, through book p.493. It is not the end of Volume I or an
author-complete edition.

Maintenance performed no compilation, rendering, OCR, transcription, source
correction, or producer-file mutation. Producer compile/render statements are
retained as provenance claims; the maintenance pass independently checked file
identities, manifests, TeX marker ranges, PDF structure, and repository
relationships only.

## Start Here

Open the [current 500-page reader](<../reader-pdfs/sylvester/Sylvester - Collected Mathematical Papers, Volume I - Source-Checked Edition through Book Page 493.pdf>).
Its PDF pages are typeset-output pages, while the edition's margin markers and
manifests refer to book pages. The reader covers book pp.1–493 and stops at the
exact p.493 source-page boundary in the middle of Art.42 and in the middle of a
sentence. Continue with book p.494; do not infer that the sentence or Volume I
is complete.

The direct reader is byte-identical to both retained cumulative copies:

- [`cum/pdf/Vol1_pp001_493.pdf`](../sources/sylvester/sylv_b26/cum/pdf/Vol1_pp001_493.pdf)
- [`cum/tex/Vol1_pp001_493.pdf`](../sources/sylvester/sylv_b26/cum/tex/Vol1_pp001_493.pdf)

All three are 2,058,797 bytes with SHA-256
`EAC30D5025050871458A1E95C1715771AF02DD8BB83D5F1B89FBD3353D472A4A`.
Use the [current TeX](../sources/sylvester/sylv_b26/cum/tex/Vol1_pp001_493.tex),
[plain text](../sources/sylvester/sylv_b26/cum/txt/Vol1_pp001_493.txt),
[493-page source scan](../sources/sylvester/sylv_b26/cum/scan_pdf/src_019_511_book001_493.pdf),
and [page manifest](../sources/sylvester/sylv_b26/cum/src_manifest.csv) for
checking and continuation.

## Preserved Generations

| Generation | Mathematical range | Current GitHub files | Exact state |
|---|---|---|---|
| Current cumulative | Book pp.1–493 | 500-page reader, 493-page scan, TeX, TXT, and 493-row page manifest | Current continuation head. The manifest maps book pp.1–493 to source-PDF pp.19–511 without a missing or repeated row. |
| Batch 26 addition | Book pp.476–493 | 20-page reader, 18-page scan, TeX, TXT, and 18-row page manifest | Continues Paper 57 through the beginning of Art.42. The two retained batch-reader PDFs are byte-identical. The next page is book p.494. |
| Predecessor | Book pp.1–475 | 364-page reader, 475-page scan, TeX, and TXT | Distinct predecessor generation. It remains useful history and must not replace the corrected pp.1–493 head. |
| Future-aid index | Stale locator note: p.269 onward and Volumes II–IV | One Markdown index only | The four ZIP packages named by the index are not tracked here. Its p.218 endpoint predates the current p.493 head. Names, sizes, and hashes are recovery locators, not custody of the ZIP bytes. |

The current and predecessor PDF page counts differ because they are different
typeset generations; neither PDF page count is a claim about printed book-page
count. All nine tracked PDFs opened in the read-only structural pass, totaling
2,890 PDF page slots including duplicate copies, with no parser warning.

## Page And Marker Replay

The cumulative TeX has 494 `\sourcepage{...}` occurrences representing all
493 integers from 1 through 493. Page 39 occurs twice: one marker begins Paper
5 and the other begins the immediately following “Note to the Foregoing” on
the same book page. The producer audit records this duplicate and no missing
marker. The new-range TeX has exactly one marker for every page 476–493; the
predecessor has 476 occurrences representing 1–475, with the same p.39
duplicate.

The [cumulative manifest](../sources/sylvester/sylv_b26/cum/src_manifest.csv)
has 493 contiguous rows: book pp.1–493 map to source-PDF pp.19–511. The
[new-range manifest](../sources/sylvester/sylv_b26/new/src_manifest.csv) has 18
contiguous rows: book pp.476–493 map to source-PDF pp.494–511.

The new-range manifest also names eighteen `new/img/*.png` witnesses, and both
the status and producer audit say those witnesses are present. They are not in
the tracked GitHub tree: this selection contains zero image files and no
`new/img` files. The two scan PDFs preserve the corresponding source-page
images, but a filename or count in a control is not custody of the eighteen
individual PNG bytes.

## Corrections And Producer QA Claims

The [status](../sources/sylvester/sylv_b26/STATUS.md) and
[producer audit](../sources/sylvester/sylv_b26/qa/audit_001_493.json) record two
corrections made while adding pp.476–493:

- the cumulative p.475 exponent in `\Syz_{m-i,0}` was changed to
  `(-)^{(i-1)i/2}` after comparison with p.476;
- an earlier unclosed `\scriptsize` group was closed.

They also record successful `pdflatex` runs, twenty rendered new-range pages,
selected cumulative renders, zero `includegraphics`, twenty-two TikZ blocks,
and no placeholder/TODO markers. These are retained producer claims. The PNG
renders and the `verify` surface named by the status are not tracked, and
maintenance did not rerun or promote those checks to independent visual or
source certification.

## Exact Content Inventory

The bounded GitHub-native selection contains 21 files / 78,215,696 bytes:

- 20 files under `sources/sylvester`;
- one direct reader under `reader-pdfs/sylvester`;
- nine PDFs, three TeX files, three text files, three Markdown files, two CSV
  manifests, and one JSON audit.

Canonical tree SHA-256:
`60E56B3A14023F9ED56E536FCA74C102F3E8570EE098128F77DD3AF20FEB620A`.
The canonical stream uses ordinal repository-relative path order and one
`relative_path<TAB>bytes<TAB>SHA256<LF>` row per file, encoded as UTF-8 without
a BOM.

See
[`20260806_sylvester_map.json`](../manifests/github-custody/20260806_sylvester_map.json)
for selection-level digests, all PDF identities, manifest replay, marker
counts, missing-witness state, and the exact maintenance boundary.

## Continue Without Duplicating Work

1. Continue Art.42 at book p.494 against the retained source scan; do not restart pp.1–493.
2. Preserve the pp.1–475 generation and both documented corrections as revision history.
3. Recover the eighteen named PNG witnesses if their exact producer bytes still exist; do not synthesize replacements under those identities.
4. Recover and hash-check the four future-aid ZIPs before relying on them for Volumes II–IV.
5. Independently source-check citation-critical text and mathematics before calling this a critical edition; the current GitHub evidence does not establish that certification.
