# Additional Author Cluster: Exact GitHub Map

Observed 2026-08-06. This page describes only the bytes tracked in the
repository's additional-author shelf. It does not infer custody from an
external catalog, an old local path, a filename, or an unpublished package.

The shelf currently has ten direct PDFs for nine authors. They are real
readers totaling 2,938 PDF pages. The accompanying source shelf, however,
contains only three small report or triage files. It does not contain the
TeX, source PDFs, or package ZIPs described by its inherited README.

## Open These First

- [Direct reader shelf](../reader-pdfs/author-cluster/) - 10 PDFs / 2,938
  pages / 15,291,684 bytes.
- [Tracked report shelf](../sources/author-cluster/) - 3 files / 6,419
  bytes; no TeX, source PDF, or ZIP.
- [Machine custody manifest](../manifests/github-custody/20260806_cluster.json)
  - exact paths, bytes, SHA-256, page counts, PDF structure, and stale-control
  findings.

An absent source packet is a GitHub custody gap, not evidence that the
mathematics or translation never existed elsewhere. Recover exact producer
bytes before recreating work.

## Current Reader Surface

| Author / work | Current reader | Language and exact GitHub state |
|---|---|---|
| Hermann Minkowski, *Gesammelte Abhandlungen*, Volume II selections | [333-page reader](<../reader-pdfs/author-cluster/00 Reader PDF - Minkowski - Gesammelte Abhandlungen Volume II - Selected Papers.pdf>) | German selected-paper assembly beginning with paper XIX and continuing through geometry, physics, the *Raum und Zeit* address, a Dirichlet address, and a subject index. The current bytes do not prove complete Volume II coverage. |
| Erich Hecke, *Vorlesungen ueber die Theorie der algebraischen Zahlen* | [184-page reader](<../reader-pdfs/author-cluster/01 Reader PDF - Hecke - Vorlesungen ueber die Theorie der algebraischen Zahlen.pdf>) | German working assembly. It contains chapter and page-number resets, a second contents surface at PDF page 127, and publisher-catalog prose on PDF pages 181-184. Internal links resolve, but the assembly needs source-level completeness review. |
| Edmund Landau, *Elementary Number Theory* | [243-page reader](<../reader-pdfs/author-cluster/02 Reader PDF - Landau - Elementary Number Theory.pdf>) | English mathematical body. It begins at `Part I` / printed page 13 and has no direct title, translator, or publisher front matter. The old triage note calls it the Goodman translation, but that attribution is not embedded as PDF metadata or backed by a tracked source packet here. |
| Ernst Steinitz, *Algebraische Theorie der Koerper* | [73-page legacy reader](<../reader-pdfs/author-cluster/03 Reader PDF - Steinitz - Algebraische Theorie der Koerper.pdf>) | German mixed-shelf generation. It is a distinct byte and layout identity from the current [87-page dedicated German sections 1-24 reader](<../reader-pdfs/steinitz/11 Ernst Steinitz - 1910 Algebraic Theory of Fields Sections 1-24 - German.pdf>). Use the [Steinitz map](steinitz-map.md) for current work; preserve this file as history. |
| Kurt Hensel, *Zahlentheorie* | [251-page reader](<../reader-pdfs/author-cluster/04 Reader PDF - Hensel - Zahlentheorie.pdf>) | German reader beginning with the 1913 title page and ending with the printed errata surface. No editable or source closure is tracked in this shelf. |
| Kiyoshi Oka, analytic functions of several variables, Memoirs I-X | [141-page reader](<../reader-pdfs/author-cluster/05 Reader PDF - Oka - Analytic Functions of Several Variables I-X.pdf>) | English translation collection. The ten memoir sequence is visible from Memoir I at PDF page 1 through Memoir X at page 112, followed by bibliography and an added-in-print note. No work-level source or translation provenance packet is tracked here. |
| Felix Hausdorff, *Set Theory* | [413-page reader](<../reader-pdfs/author-cluster/06 Reader PDF - Hausdorff - Set Theory.pdf>) | English reading edition. It is a distinct language and container surface from the German Hausdorff collection below. |
| Hermann Grassmann, *Ausdehnungslehre* and related works | [613-page reader](<../reader-pdfs/author-cluster/07 Reader PDF - Grassmann - Ausdehnungslehre and Related Works.pdf>) | English translation anthology containing the 1844 work, *Geometric Analysis*, and selected mathematical and physical papers. Its first page reproduces a German title; that does not make the whole reader a German edition. |
| Felix Hausdorff, *Mengenlehre* and descriptive-set/topology writings | [675-page reader](<../reader-pdfs/author-cluster/08 Reader PDF - Hausdorff - Mengenlehre and Descriptive Set Theory Writings.pdf>) | German composite reader: 1927/1935 *Mengenlehre* surfaces followed by descriptive-set, topology, and Nachlass material. It is not a byte duplicate of the English *Set Theory* reader and has no tracked editable/source closure here. |
| Wilhelm Killing, transformation groups | [12-page reader](<../reader-pdfs/author-cluster/09 Reader PDF - Killing - Transformationsgruppen.pdf>) | German `Zweiter Theil` only: *Die Zusammensetzung der stetigen endlichen Transformationsgruppen*. The generic filename must not be read as a complete multi-part Killing corpus. |

## What The Source Shelf Actually Contains

| Tracked file | Bytes | Exact role |
|---|---:|---|
| [reports/README.md](../sources/author-cluster/reports/README.md) | 454 | Inherited description saying that an archive preserves TeX/PDF/source packets. Those packets are not present under the tracked GitHub root. |
| [reports/public_summary.json](../sources/author-cluster/reports/public_summary.json) | 1,092 | Lists all ten current reader filenames exactly, but supplies no pages, bytes, hashes, source bindings, or supersession identities. |
| [triage note](../sources/author-cluster/triage_notes/landau_sylvester_source_followup.md) | 4,873 | Historical routing note with local-path claims and recommendations. It is not current custody proof. |

The tracked source shelf has:

- TeX files: 0;
- source or repair PDFs: 0;
- package ZIPs: 0;
- per-reader historical SHA-256 controls: 0.

The new machine manifest is therefore the first exact GitHub byte binding for
all ten current cluster readers. It proves repository custody, not producer
lineage, source fidelity, or build synchronization.

## Stale And Superseded Report Statements

The old triage note is preserved unchanged, but several statements are no
longer current GitHub guidance:

- it calls the Landau reader a 255-page, approximately 1.8 MB file not yet in
  GitHub; the tracked reader is 243 pages / 1,298,513 bytes;
- it says Sylvester is not in GitHub, whereas the current
  [Sylvester map](sylvester-map.md) exposes a 500-page Volume I reader, source
  scan, TeX/TXT, controls, and continuation cursor;
- it says Cayley Volume VIII modern typesetting was skipped, whereas the
  current [Cayley map](cayley-map.md) binds a direct Volume VIII slice and its
  adverse manifest state;
- its external local paths were not followed and do not establish GitHub
  custody.

The current GitHub cluster roots also contain no routed Mikami, Kronecker,
Kron, Picard, Klein-Fricke, Bianchi, Gordan, Frobenius, Poincare, or Kneser
payload. Such material may be named in other catalogs or external records, but
it is not part of this exact 13-file GitHub selection.

## PDF Structure Replay

A bounded, read-only structural pass opened all ten PDFs with pypdf 6.12.2 and
mutool 1.23.0:

- 10/10 containers opened; parser failures 0; mutool warning files 0;
- 2,938 pages; 29 pages with no extracted text; extraction failures 0;
- 281 named destinations and 470 internal `GoTo` actions; broken actions 0;
- zero URI actions, zero outline entries, and zero page image XObjects;
- 1,550 per-document unique font-resource rows; Type 3 rows 0; unembedded rows
  0.

No page was rendered. These checks establish container readability, internal
link resolution, and font embedding only. They do not establish visual
quality, source fidelity, mathematical correctness, translation accuracy,
completeness, or accessibility.

## Exact Inventory

The bounded selection contains 13 files / 15,298,103 bytes:

- reader tree: 10 files / 15,291,684 bytes / SHA-256
  `CFC80403114AAB06ADD1034C83CB92E2B1CB7341AF00FA978B88654DDBBB88F6`;
- report tree: 3 files / 6,419 bytes / SHA-256
  `8047F317A536BAFC1E5AC9883220E7DFDB26D268F157662A1AF95B828C977DC6`;
- aggregate tree: 13 files / 15,298,103 bytes / SHA-256
  `4F009D0501A5F6B888BC5A9B7E89CBB64F9BC121F1FEB64EF51442A4FA4837DC`.

The canonical stream uses ordinal repository-relative path order and one
`relative_path<TAB>bytes<TAB>SHA256<LF>` row per file, UTF-8 without a BOM.

## Continue Without Losing Or Duplicating Work

1. Use these ten PDFs as the current reader bytes; do not regenerate Landau,
   Oka, Hausdorff, Grassmann, or the other represented scopes merely because
   editable source is absent.
2. Recover exact TeX/source/package bytes from hash-backed producer custody.
   Do not invent the missing source archive from the inherited README.
3. Treat the Hecke assembly, the limited Killing second part, the Minkowski
   selection, and the two Hausdorff containers according to the caveats above.
4. Route Steinitz work through the dedicated current map; keep the 73-page
   mixed-shelf file as preserved history.
5. Add any newly recovered author packet under a short, author-owned root with
   an exact manifest and explicit predecessor relation. Do not hide it in a
   new mixed container.
