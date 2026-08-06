# Cayley GitHub Coverage Map

Observed 2026-08-06. This page records the Arthur Cayley material whose bytes
are actually present in GitHub: thirteen direct working readers for Volumes
I–XIII, two May source generations, a June Volume I assembly package, and one
stale triage note. It does not infer custody from filenames, external record
descriptions, or local paths named only inside notes.

All inherited “Complete”, “Source-Checked”, and “critical” labels remain
de-promoted. The repository's standing warning records substantial Volume I
symbol/text mismatches, and no Cayley range is presently promoted as
source-faithful. Maintenance performed no compilation, rendering, OCR,
transcription, source correction, or producer-file mutation.

## Start Here

These are the thirteen direct GitHub readers. Their page counts are PDF page
slots, not claims about printed-source coverage.

| Volume | Direct reader | Read-only PDF state |
|---|---:|---|
| I | [488 pages](<../reader-pdfs/classical/Arthur Cayley - Collected Mathematical Papers, Volume I - Complete Source-Checked Modern LaTeX Reader.pdf>) | Opens; broken-xref warning; does not byte-match the June manifest-bound copy. |
| II | [421 pages](<../reader-pdfs/classical/Cayley - Collected Mathematical Papers, Volume II - Source-Checked Modern LaTeX Slice Reader.pdf>) | Opens without parser warning. |
| III | [322 pages](<../reader-pdfs/classical/Cayley - Collected Mathematical Papers, Volume III - Source-Checked Modern LaTeX Slice Reader.pdf>) | Opens without parser warning. |
| IV | [496 pages](<../reader-pdfs/classical/Cayley - Collected Mathematical Papers, Volume IV - Source-Checked Modern LaTeX Slice Reader.pdf>) | Opens without parser warning; contains explicit placeholder/OCR-illegible table notices. |
| V | [443 pages](<../reader-pdfs/classical/Cayley - Collected Mathematical Papers, Volume V - Source-Checked Modern LaTeX Slice Reader.pdf>) | Opens; broken-xref warning; contains explicit diagram/woodcut/plate omissions. |
| VI | [407 pages](<../reader-pdfs/classical/Cayley - Collected Mathematical Papers, Volume VI - Source-Checked Modern LaTeX Slice Reader.pdf>) | Opens; broken-xref warning. |
| VII | [336 pages](<../reader-pdfs/classical/Cayley - Collected Mathematical Papers, Volume VII - Source-Checked Modern LaTeX Slice Reader.pdf>) | Opens without parser warning. |
| VIII | [536 pages](<../reader-pdfs/classical/Cayley - Collected Mathematical Papers, Volume VIII - Source-Checked Modern LaTeX Slice Reader.pdf>) | Opens; broken-xref warning; its retained slice manifest does not replay exactly. |
| IX | [348 pages](<../reader-pdfs/classical/Cayley - Collected Mathematical Papers, Volume IX - Source-Checked Modern LaTeX Slice Reader.pdf>) | Opens without parser warning; contains an explicit non-reproduction of a full subsidiary table. |
| X | [576 pages](<../reader-pdfs/classical/Cayley - Collected Mathematical Papers, Volume X - Source-Checked Modern LaTeX Slice Reader.pdf>) | Opens; broken-xref warning; says dense schedules remain compact or partial. |
| XI | [415 pages](<../reader-pdfs/classical/Cayley - Collected Mathematical Papers, Volume XI - Source-Checked Modern LaTeX Slice Reader.pdf>) | Opens; broken-xref warning. |
| XII | [437 pages](<../reader-pdfs/classical/Cayley - Collected Mathematical Papers, Volume XII - Source-Checked Modern LaTeX Slice Reader.pdf>) | Opens; broken-xref warning. |
| XIII | [488 pages](<../reader-pdfs/classical/Cayley - Collected Mathematical Papers, Volume XIII - Source-Checked Modern LaTeX Slice Reader.pdf>) | Opens; broken-xref warning. |

All thirteen readers structurally enumerate, totaling 5,713 PDF page slots.
None is byte-identical to any of the 283 PDFs in the bounded source
selections. A successful open proves container readability, not source
accuracy, completeness, or synchronization with a TeX file.

## Preserved Source Generations

| Generation | Current GitHub bytes | Exact custody state |
|---|---:|---|
| [May clean per-volume tree](../sources/classical/cayley-current-slice-and-source-rebuild-2026-05-29/cayley_clean_per_volume_public/) | 300 files / 38,304,093 bytes | TeX, selected PDFs, backups, Volume VIII controls/facsimile slices, and historical placeholders. Its range-like filenames are navigation aids, not verified coverage. |
| [May repaired-slice tree](../sources/classical/cayley-current-slice-and-source-rebuild-2026-05-29/cayley_repaired_slice_sources_2026-05-29/) | 450 files / 82,204,074 bytes | Earlier paired TeX/PDF slice generations for Volumes I–VII and IX–XIII, plus retained repair scripts and explicit omission notes. It has no Volume VIII directory. |
| [June Volume I assembly](../sources/classical/cayley-volume-i-complete-source-checked-reader-2026-06-02/) | 30 files / 10,627,136 bytes | Six gap-fill TeX/PDF/status groups, a 27-row assembly manifest, a distinct merged reader, and eight verification PNGs. Producer “source-checked” claims are retained but remain de-promoted by the later catalog warning. |
| [Volume VIII triage note](../sources/classical/triage_notes/cayley_volume_viii_source_scan_found.md) | 1 file / 4,714 bytes | Historical locator/recovery note. Its claims that the Volume VIII reader was pending and Sylvester was absent are now stale. |

The 283 source-tree PDFs also structurally enumerate, totaling 7,285 page
slots. Only the June merged Volume I reader emitted a broken-xref warning.
There are no parser failures. This was a read-only structural pass; no page was
rendered or visually certified.

## Volume I: Manifest Replay And Identity Conflict

The [June README](../sources/classical/cayley-volume-i-complete-source-checked-reader-2026-06-02/README_START_HERE.md),
[summary](../sources/classical/cayley-volume-i-complete-source-checked-reader-2026-06-02/summary.json),
and [slice manifest](../sources/classical/cayley-volume-i-complete-source-checked-reader-2026-06-02/slice_order_manifest.csv)
describe a 27-slice reader. The manifest's source labels cover every integer
1–573 once, its reader-page fields cover 1–488 once, all 27 referenced PDFs
exist, and their actual page counts total 488 with no row-level page error.
That verifies the recorded assembly sequence, not the fidelity of its text or
the semantic truth of the source-page labels.

The two files presented as the same reader are different bytes:

- the [manifest-bound merged copy](<../sources/classical/cayley-volume-i-complete-source-checked-reader-2026-06-02/merged_reader/Arthur Cayley - Collected Mathematical Papers, Volume I - Complete Source-Checked Modern LaTeX Reader.pdf>)
  is 7,762,244 bytes, SHA-256
  BC903768B0044F4A282C439C5BD18996987CD33CD893F8175E20B54708A4EFFF;
- the [direct reader](<../reader-pdfs/classical/Arthur Cayley - Collected Mathematical Papers, Volume I - Complete Source-Checked Modern LaTeX Reader.pdf>)
  is 7,764,737 bytes, SHA-256
  7B44F77BA13BFA88D7681A1647A08A917605870A908BBAF03CAB4A31B59FEC49.

Both have 488 pages. The summary names the direct-reader path but records the
merged copy's size and hash. Neither identity is silently substituted for the
other.

The separate May-clean file
[cayley_vol01_pages_573_620.tex](../sources/classical/cayley-current-slice-and-source-rebuild-2026-05-29/cayley_clean_per_volume_public/sources_tex_Vol_I/cayley_vol01_pages_573_620.tex)
also shows why filenames are not coverage proof. It is 9,321 bytes, SHA-256
A1C9154EBF71E23F422CDF4CC79AA14E78DE2F0B2C8BE9644EF5CC8915C4521B;
its internal title says pages 551–589, its only page-counter values are 551
and 552, and it ends while the displayed proof is still continuing. It does
not establish content through page 620.

The status files cite local scans and page images used by the producer. Those
exact full source scans and source PNG sets are not tracked in this selection.
The eight PNGs in the June package are verification renders, not the cited
source-page image set.

## Volume VIII: Adverse And Superseded State

The [Volume VIII slice manifest](../sources/classical/cayley-current-slice-and-source-rebuild-2026-05-29/cayley_clean_per_volume_public/sources_tex_Vol_VIII/cayley_vol08_reader_slice_manifest.csv)
has 19 rows and declares 537 reader pages. The current referenced PDFs total
536 pages:

- the pages 267–291, 467–516, and 542–566 rows have stale byte counts;
- the pages 304–316 row declares 14 pages / 205,431 bytes but the current file
  has 13 pages / 192,358 bytes;
- these produce five replay errors across four rows.

The direct Volume VIII reader also has 536 pages, but it has no byte-identical
source-tree copy, so matching page totals do not prove that it is the exact
current slice concatenation.

Three historical placeholder TeX/PDF pairs remain under
[the placeholder directory](../sources/classical/cayley-current-slice-and-source-rebuild-2026-05-29/cayley_clean_per_volume_public/sources_tex_Vol_VIII/_gap_placeholders/).
One separate [incomplete pages 517–541 generation](../sources/classical/cayley-current-slice-and-source-rebuild-2026-05-29/cayley_clean_per_volume_public/sources_tex_Vol_VIII/_superseded_incomplete_20260602/)
is explicitly superseded. Preserve them as adverse/revision history; do not
present them as the current reader.

The [pilot notes](../sources/classical/cayley-current-slice-and-source-rebuild-2026-05-29/cayley_clean_per_volume_public/sources_tex_Vol_VIII/PILOT_NOTES.md)
also record a diagram replaced by text and formula-risk areas. The stale triage
note names a 640-page, 45,622,978-byte source scan with SHA-256
57A89FB28684FE60870316578FE76E41958AEB5369E8F0490632A5DB5DBDF97C.
That scan identity is not present in the bounded GitHub tree, and maintenance
did not follow the note's external absolute path.

## Explicit Reader-Visible Omissions

Read-only text extraction confirms editorial caveats inside the direct readers:

- Volume IV reader pp.381, 384, and 386 describe a table represented as a
  placeholder, an OCR-illegible multi-column collection, and further
  placeholder tables.
- Volume V reader pp.57, 71–73, and 112 omit a diagram, small
  woodcut/auxiliary figures, a plate, and two curve figures.
- Volume IX reader p.215 says the full numerical cells of a subsidiary table
  are not reproduced to avoid OCR noise.
- Volume X reader p.368 says dense schedules are still being promoted and
  some remain in compact or partial form.

The corresponding retained TeX notes occur in the repaired-slice tree. These
are direct evidence that the affected readers are not complete native
transcriptions. A targeted phrase search found no equivalent marker in the
other direct volumes, but absence of that phrase is not a source audit and
does not re-promote them.

## Filename And Internal-Label Replay

The May-clean tree contains 184 primary TeX paths matching a volume/page-range
filename pattern. Of those, 127 contain a parseable first internal “Pages
A--B” label, and 21 disagree with the filename range. Some internal labels may
describe a paper rather than the whole file; the discrepancy still means
neither naming surface can certify coverage by itself. The machine audit lists
all 21 pairs.

The current static record page names a later Volume I restart packet, but no
tracked repository path contains that packet name. Its description is not
GitHub custody and was not used to re-promote these readers.

## Exact Content Inventory

The bounded GitHub-native selection contains 794 files / 201,021,770 bytes:

- 296 PDFs, 419 TeX files, 16 text files, nine Markdown files, eight PNG
  verification renders, two CSVs, one JSON, two Python scripts, and 41 backup
  files;
- 12,998 structurally enumerated PDF page slots across all direct and source
  generations, including duplicates;
- zero byte-identical direct-reader/source-PDF pairs.

Canonical tree SHA-256:
4C6F4E6B282C58D2DA6FDCF62640553609E809D656436102AC5737056AE27F50.
The canonical stream uses ordinal repository-relative path order and one
relative_path, byte-count, SHA-256 row per file, encoded as UTF-8 without a
BOM and terminated by LF.

See
[20260806_cayley_map.json](../manifests/github-custody/20260806_cayley_map.json)
for every reader identity, selection digest, manifest discrepancy, internal
range-label mismatch, omission marker, and maintenance boundary.

## Continue Without Duplicating Work

1. Preserve all current generations and the de-promotion history; do not
   overwrite adverse or superseded bytes.
2. Recover the exact Volume I and Volume VIII source scans/page witnesses
   named by the retained controls, hash them, and bind them locally before a
   page-level audit.
3. Reconcile the two 488-page Volume I identities and correct the summary/path
   binding in a producer-owned successor.
4. Repair the four stale Volume VIII manifest rows and bind any future direct
   reader to its exact slice sequence.
5. Replace the explicit Volume IV, V, IX, and X omission/placeholder surfaces
   with source-checked native content while preserving the old notes.
6. Re-promote only an exact, independently source-audited range; do not infer
   accuracy or coverage from a filename, successful compile, clean-looking
   render, or external catalog description.
