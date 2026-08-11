# Steinitz GitHub Coverage Map

Observed 2026-08-06. This page records the Ernst Steinitz material whose bytes
are actually present in GitHub. The current shelf contains nine bounded German
and English working-edition pairs, two source-scan entry points, a one-page
reader guide, editable/source layers, and a checksum ledger that also names
hundreds of files not present in the current tree.

“Complete” below is a retained producer claim for the named work or range, not
a critical-edition, peer-review, or mathematical-certification claim. German
and English readers remain independent surfaces. Maintenance performed no
compilation, rendering, OCR, source correction, or producer-file mutation.

## Start Here

Open the [one-page reader guide](<../reader-pdfs/steinitz/00 Ernst Steinitz - Reader Guide and Status.pdf>),
then select a work below. The page counts are the current GitHub PDF structure,
not printed-source page counts.

| Work and bounded scope | German reader | English reader | Current source/custody state |
|---|---:|---:|---|
| 1894, configurations and construction; retained complete-dissertation claim | [23 pages](<../reader-pdfs/steinitz/01 Ernst Steinitz - 1894 Configurations and Construction - German Complete.pdf>) | [17 pages](<../reader-pdfs/steinitz/02 Ernst Steinitz - 1894 Configurations and Construction - English Translation Complete.pdf>) | Both direct PDFs exactly match files in the [1894 source layer](../sources/steinitz/Steinitz_21/01_1894_dissertation/). Complete and split TeX/PDF/TXT plus source PDF slices are present; 13 scan images and 10 QA images named by the checksum ledger are absent. |
| 1897, configurations $n^3$ | [3 pages](<../reader-pdfs/steinitz/03 Ernst Steinitz - 1897 Configurations n3 - German.pdf>) | [3 pages](<../reader-pdfs/steinitz/04 Ernst Steinitz - 1897 Configurations n3 - English Translation.pdf>) | Both match the [1897 source layer](../sources/steinitz/Steinitz_21/02_1897_config/). German/English TeX/PDF/TXT are present, but the four scans and source PDF named by the ledger are absent. |
| 1899, modules in algebraic number fields, package pages 001–057 | [43 pages](<../reader-pdfs/steinitz/05 Ernst Steinitz - 1899 Modules in Algebraic Number Fields - German.pdf>) | [38 pages](<../reader-pdfs/steinitz/06 Ernst Steinitz - 1899 Modules in Algebraic Number Fields - English Translation.pdf>) | Both match the complete p001–057 files in the [modules layer](../sources/steinitz/Steinitz_21/03_1899_moduln/), which also preserves p001–016, p001–032, p017–032, and p033–057 generations. The source PDF remains; 82 ledgered scan images do not. |
| 1899, continuity and irrational numbers | [9 pages](<../reader-pdfs/steinitz/07 Ernst Steinitz - 1899 Continuity and Irrational Numbers - German.pdf>) | [8 pages](<../reader-pdfs/steinitz/08 Ernst Steinitz - 1899 Continuity and Irrational Numbers - English Translation.pdf>) | Both match the [continuity layer](../sources/steinitz/Steinitz_21/04_1899_stetigkeit/). TeX/PDF/TXT and a source PDF remain; 12 ledgered scans are absent. |
| 1901, Abelian groups, printed pp.80–85 | [4 pages](<../reader-pdfs/steinitz/09 Ernst Steinitz - 1901 Abelian Groups - German.pdf>) | [3 pages](<../reader-pdfs/steinitz/10 Ernst Steinitz - 1901 Abelian Groups - English Translation.pdf>) | Both match the [1901 layer](../sources/steinitz/Steinitz_21/05_1901_abelgroups/). TeX/PDF/TXT, a six-page source PDF, page map, and slice summary remain; six ledgered scans are absent. The two small controls differ from their ledger hashes only because Git stores LF while the ledger hashed CRLF bytes. |
| 1905, one-sided polyhedron, printed pp.281–307 | [17 pages](<../reader-pdfs/steinitz/15 Ernst Steinitz - 1905 One-Sided Polyhedron - German.pdf>) | [16 pages](<../reader-pdfs/steinitz/16 Ernst Steinitz - 1905 One-Sided Polyhedron - English Translation.pdf>) | The direct readers and [27-page direct source slice](<../reader-pdfs/steinitz/17 Ernst Steinitz - 1905 One-Sided Polyhedron - Source Scan Slice.pdf>) have no byte-identical copies in the current [1905 source layer](../sources/steinitz/Steinitz_21/06_1905_polyhedron/). That layer contains only a README and a different 27-page source PDF, with no TeX; its PDF opens but emits a broken-xref warning. |
| 1910, algebraic theory of fields, §§1–24 | [87 pages](<../reader-pdfs/steinitz/11 Ernst Steinitz - 1910 Algebraic Theory of Fields Sections 1-24 - German.pdf>) | [82 pages](<../reader-pdfs/steinitz/12 Ernst Steinitz - 1910 Algebraic Theory of Fields Sections 1-24 - English Translation.pdf>) | Both match the [1910 layer](../sources/steinitz/Steinitz_21/07_1910_fields/). Sections 21–24 have editable body TeX; the complete wrappers embed retained base PDFs for §§1–20/22, so the full range is not an all-editable-TeX surface. A source PDF remains; 161 ledgered scans are absent. |
| 1911, rectangular systems and modules I, printed pp.328–354 | [14 pages](<../reader-pdfs/steinitz/13 Ernst Steinitz - 1911 Rectangular Systems and Modules in Algebraic Number Fields I - German.pdf>) | [13 pages](<../reader-pdfs/steinitz/14 Ernst Steinitz - 1911 Rectangular Systems and Modules in Algebraic Number Fields I - English Translation.pdf>) | Both match the complete files in the [1911 layer](../sources/steinitz/Steinitz_21/08_1911_rectI/). Complete and split TeX/PDF/TXT plus source PDFs and a page map remain; 42 scans and 55 QA images are absent. The page-map mismatch is LF-versus-CRLF only. |
| 1912, rectangular systems II, printed pp.297–345 | [22 pages](<../reader-pdfs/steinitz/18 Ernst Steinitz - 1912 Rectangular Systems II - German Complete.pdf>) | [17 pages](<../reader-pdfs/steinitz/19 Ernst Steinitz - 1912 Rectangular Systems II - English Translation Complete.pdf>) | Both match complete files in the [1912 layer](../sources/steinitz/Steinitz_21/09_1912_rectII/). The [49-page direct source slice](<../reader-pdfs/steinitz/20 Ernst Steinitz - 1912 Rectangular Systems II Full Source Scan Slice Pages 297-345.pdf>) also matches its source-layer copy. Complete and split TeX/PDF/TXT remain; 98 scans and 28 QA images are absent. |

The nine German/English pairs total eighteen direct mathematical readers.
Sixteen are byte-identical to copies in `Steinitz_21`; only the two 1905
readers lack source-tree byte matches. The 1912 direct source slice also
matches; the 1905 direct source slice is a distinct generation.

## Checksum Ledger: Current Bytes And Missing Witnesses

The [checksum ledger](../sources/steinitz/Steinitz_21/00_checksums/SHA256SUMS.txt)
is 74,531 bytes, SHA-256
`D9E525A1B2E9DDEE8B9CCCE2779BD93FC452740C43015D7F50088537F7D5E4C5`.
It has 696 unique, well-formed, path-safe rows. It is not a manifest of only the
current GitHub tree:

- all 176 current non-ledger source files are named, with no current file omitted;
- 173 current files match their ledger SHA-256 exactly;
- three current small text controls have LF bytes while the ledger hashes their exact CRLF transforms;
- 520 ledger paths are absent: 278 JPG scans, 241 PNG scan/QA renders, and one 1897 source PDF.

The three exact-byte mismatches are the 1901 `page_map.csv`, 1901
`slice_summary.json`, and 1911 `page_map.csv`. Their content is not silently
reinterpreted as a hash match: the current LF hashes and ledger CRLF hashes are
both recorded in the machine audit. The 520 absent paths remain valuable
recovery locators, but the ledger alone is not public custody of their bytes.

## PDF Structure And Source Caveats

All 21 direct PDFs structurally open, enumerate 496 total pages, and emitted no
parser warning in the current read-only pass. All 60 PDFs inside `Steinitz_21`
also open and enumerate 1,585 page slots; the source-tree copy of the 1905
27-page slice emits a broken-xref warning even though a retained note calls it
rebuilt and valid. No maintenance render or visual inspection was performed.

The current source tree contains 60 PDFs, 58 TeX files, 51 text files, five
Markdown notes, two CSV controls, and one JSON control. It contains no JPG or
PNG files. Several source PDFs therefore preserve page-image witnesses even
though their ledgered individual scans are absent; the 1897 group has no
current source PDF at all.

## Conflicting Status Notes

The root README and corpus status call all nine named groups complete for their
represented scopes. Two same-package notes preserve earlier or conflicting
states:

- `1905_source_resliced.md` says the 1905 translation/transcription had not yet been added, while direct German/English readers and the later audit note say it was complete;
- `source_followup.md` calls 1912 Rect II a future production target, while the current source and reader shelves contain complete-labelled German/English files for pp.297–345.

The bytes and filenames prove that those reader/source files exist; they do not
resolve source accuracy or turn “complete” into certification. Preserve the
contradictory notes as revision history rather than deleting them.

The GitHub controls still name two author-corpus gaps: the 1906
Euler-polyhedron note and the 1908 *Beiträge zur Analysis Situs*. The 1906
note is absent from this bounded GitHub selection, but the snapshotted
dedicated-record state reports a package-audited German/English 1906 packet;
bind and bibliographically compare that packet before treating the gap as new
production. The broader project controls also report a provisional 22-page,
approximately 300ppi Ranicki offprint for the 1908 work. Its exact bytes and
bibliographic identity are not bound to GitHub, so recover and hash-bind that
known witness before seeking a stronger source rather than restarting discovery
from zero. No 1913, 1914, or 1916 work is in this bounded GitHub selection,
regardless of descriptions maintained on other publication surfaces.

## Exact Content Inventory

The audited GitHub-native selection contains 198 files / 206,630,468 bytes.
Canonical tree SHA-256:
`F9D9A4ECC31144F4A73A39EBF2B9BEA48878556042677F642BBF02E98AEAA541`.

It includes all 177 files under `sources/steinitz` and all 21 direct reader
PDFs. See
[`20260806_steinitz_map.json`](../manifests/github-custody/20260806_steinitz_map.json)
for selection-level hashes, every direct-reader identity, checksum replay, and
the exact current caveat state.

## Continue Without Duplicating Work

1. Use the direct reader table before assigning any of the nine represented scopes again.
2. Recover the 520 ledgered-but-absent scan, QA, and 1897 source-PDF paths; preserve their exact original hashes.
3. Reconcile the 1905 and 1912 status contradictions in a producer-owned successor without rewriting this history.
4. Bind any future 1905 source package to the exact direct reader/source-slice generation and restore its editable TeX.
5. Preserve the 1910 PDF-backed §§1–20 base layers unless a fully editable, source-verified replacement is handed off.
6. For 1906, first bind and compare the dedicated-record German/English packet; if it is the Euler-polyhedron note, ingest and review that existing generation rather than retranscribing it, and create a new generation only if the identity is proved distinct. For 1908, first recover and hash-bind the reported provisional 22-page Ranicki offprint, verify the bibliography, and seek a stronger witness before strict source certification. Do not infer later Steinitz works are already in GitHub.
