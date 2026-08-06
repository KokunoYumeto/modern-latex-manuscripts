# Ukrainian Applied Mathematics: Exact GitHub Map

Observed 2026-08-06. This page describes only the bytes tracked under the
repository's Ukrainian applied-mathematics reader and source shelves. It does
not infer custody from an external record, an old package description, or an
untracked local path.

The direct shelf has one guide and twelve Ukrainian mathematical readers. The
source shelf has the same twelve logical reader modules, a 65-file TeX layer,
three CSV controls, five Markdown status files, and one research-radar fetch
script. Several retained notes describe an older package layout; use the paths
on this page as the current GitHub surface.

## Open These First

- [Direct reader shelf](../reader-pdfs/ukrainian-applied-math/) - 13 PDFs /
  385 pages / 4,710,882 bytes.
- [Integrated 124-page reader](<../reader-pdfs/ukrainian-applied-math/01 Ukrainian Applied Mathematics - Applied Mathematics and Engineering Library.pdf>).
- [Buildable public driver](../sources/ukrainian-applied-math/public_integrated_reader_tex/main_public.tex)
  - all 49 declared inputs are tracked.
- [Source and translation status](../sources/ukrainian-applied-math/06_source_status/SOURCE_AND_TRANSLATION_STATUS.md).
- [Machine custody manifest](../manifests/github-custody/20260806_ukrainian.json)
  - all 99 paths, bytes, SHA-256 identities, direct/source relations, TeX
  closure, and PDF structure.

An incomplete or unchecked module is existing work to inspect and improve, not
permission to translate the same scope from zero.

## Direct Reader Surface

The status phrases in the final column are inherited producer labels. This
GitHub audit verifies custody and container structure; it does not upgrade any
translation or mathematical QA state.

| Direct file | Pages | Bytes | Recorded scope and state |
|---|---:|---:|---|
| [Reader guide](<../reader-pdfs/ukrainian-applied-math/00 Ukrainian Applied Mathematics - Reader Guide and Status.pdf>) | 1 | 113,159 | Preserved guide dated 2026-06-01. Its counts and package-layout claims are partly stale; see below. |
| [Integrated applied-mathematics library](<../reader-pdfs/ukrainian-applied-math/01 Ukrainian Applied Mathematics - Applied Mathematics and Engineering Library.pdf>) | 124 | 521,878 | Working core covering signals, state estimation, control, robotics, sensor fusion, numerical methods, SDR/RF, and related terminology. |
| [PySDR selected module](<../reader-pdfs/ukrainian-applied-math/02 PySDR - Selected Software Defined Radio Module - Ukrainian.pdf>) | 100 | 420,542 | Producer-described strongest current SDR module; retained QA notes remain in the reader. |
| [Software-defined-radio survey core](<../reader-pdfs/ukrainian-applied-math/03 Survey of Software Defined Radio - Ukrainian Core.pdf>) | 6 | 110,529 | Format-checked working module; distinct bytes from its source-shelf PDF. |
| [Wave-equation controllability, Chapters 1-3](<../reader-pdfs/ukrainian-applied-math/04 Wave Equations Controllability and Stabilization - Ukrainian Chapters 1-3.pdf>) | 40 | 246,470 | Format-checked translated/staged scope; not the complete source work. |
| [Event sensor fusion and odometry](<../reader-pdfs/ukrainian-applied-math/05 Event Sensor Fusion and Odometry - Ukrainian.pdf>) | 8 | 432,046 | Working draft. |
| [Multi-sensor fusion survey](<../reader-pdfs/ukrainian-applied-math/06 Multi-Sensor Fusion Survey - Ukrainian.pdf>) | 19 | 2,057,026 | Working draft; distinct bytes from its source-shelf PDF. |
| [Antenna and radio-frequency notes](<../reader-pdfs/ukrainian-applied-math/07 Antenna and Radio Frequency Notes - Ukrainian.pdf>) | 23 | 169,700 | Format-checked translation fragments. |
| [Autonomous robots: perception and navigation](<../reader-pdfs/ukrainian-applied-math/08 Autonomous Robots Perception and Navigation - Ukrainian.pdf>) | 45 | 334,419 | Format-checked working module; 12 internal actions point to absent named targets. |
| [Robust Student-t filtering](<../reader-pdfs/ukrainian-applied-math/09 Robust Student-t Filtering - Ukrainian.pdf>) | 9 | 95,398 | Working draft. |
| [Micro Lie theory](<../reader-pdfs/ukrainian-applied-math/10 Micro Lie Theory - Ukrainian Partial Module.pdf>) | 4 | 80,504 | Experimental partial module; distinct bytes from its source-shelf PDF. |
| [Error-state Kalman filtering](<../reader-pdfs/ukrainian-applied-math/11 Error-State Kalman Filtering - Ukrainian Core Start.pdf>) | 4 | 85,480 | Core start only. |
| [Practical Kalman filtering](<../reader-pdfs/ukrainian-applied-math/12 Practical Kalman Filtering - Ukrainian Core Bridge.pdf>) | 2 | 43,731 | Bridge only. |

The twelve mathematical readers total 384 pages. The guide is a separate
one-page status object and is not mathematical coverage.

## Direct And Source PDF Relations

Every direct mathematical reader has one logical counterpart under the source
shelf. Preserve both paths: eight pairs are byte-identical, while four pairs
are distinct builds or generations.

Byte-identical direct/source pairs:

- integrated library;
- PySDR selected module;
- wave-equation Chapters 1-3;
- event sensor fusion and odometry;
- antenna/RF notes;
- robust Student-t filtering;
- error-state Kalman-filter core start;
- practical Kalman-filter bridge.

Distinct direct/source identities:

| Logical module | Direct SHA-256 | Source-shelf SHA-256 | Exact observation |
|---|---|---|---|
| SDR architecture survey | `51FD26BF1096DBC44A5A4BD406557C7FE390670079D90E747294EF17967FBBA4` | `6BF517A66B6F4F286B9276AC9A09D76A1684BE90DC7A8E576ACF45F54263991A` | Both have 6 pages and equal page geometry; extracted text differs on page 2. |
| Multi-sensor fusion survey | `B786A8D16B756535B7E04A4C202E53A6EB4C6969C3EF774DE457C3EEF4C9F382` | `508282625BC110427437446291A55E1EA8552FDCC6626C0A7EBE13A2B7D414AE` | Both have 19 pages and equal page geometry; extracted text differs on page 17. |
| Autonomous robots | `5AD0BDC7C0F7A8B659CC38745E18837EFB5D8F7CF3CD151B0DBDB9C2B602D902` | `E1F097B75D7C082F0342CD16E1CED0DAE729956B710DC1B3890004696B5FF812` | Both have 45 pages and equal page geometry; extracted text differs on page 1. Both retain the same 12 broken internal actions. |
| Micro Lie partial | `698019D9258FE78660DD203990881C4F5570837DC37E10A0352DF4DCA1E7F469` | `D7EC07220F2ABA24823721217DDDABBA0A4D098C83F6B39E7E0FFBDC6F1583DC` | Both have 4 pages and equal page geometry; extracted text differs on page 1. |

The tracked 25 PDF paths therefore represent 17 unique byte identities. File
duplication is a presentation/source relation, not twelve extra translations.

## Editable Source And Controls

The [source shelf](../sources/ukrainian-applied-math/) contains 86 files /
5,009,407 bytes:

- 65 TeX files / 346,719 bytes;
- 12 PDFs / 384 pages / 4,626,924 bytes;
- 3 CSV files / 16,908 bytes;
- 5 Markdown files / 18,305 bytes;
- 1 shell script / 551 bytes.

The public driver `main_public.tex` declares 49 inputs and all 49 are present.
This is path closure only: archive maintenance did not compile or render it.

The retained `main.tex` is a historical broader driver, not the current
buildable entry point. It declares 68 inputs, but six are absent:

- `chapters/24_claude_integration_status.tex`;
- `chapters/31_code_agents_and_claude_integration.tex`;
- `chapters/36_agent_continuation_queue.tex`;
- `chapters/37_claude_source package_audit_and_integration.tex`;
- `chapters/44_full_claude_source package_map.tex`;
- `chapters/50_spark_micro_lie_and_local_ocr_lane.tex`.

Do not fabricate those files or treat the historical driver as a failed
current release. Use `main_public.tex`; recover missing historical inputs only
from exact producer custody.

The CSV controls retain 13 research-radar rows, 40 OCR/source-audit rows, and
31 source-candidate rows. The fetch script is preserved but was not executed
by archive maintenance.

## Stale Guide And README Statements

The one-page guide and the README files remain preserved unchanged, but they
must not be used as current inventory controls:

- the guide says the integrated reader has 143 pages; the tracked direct and
  source copies are both 124 pages and byte-identical;
- the guide lists a ten-page dynamic-target OCR draft that is absent from the
  direct and source shelves;
- the guide says the artifact archive contains contact sheets, while the exact
  tracked selection has no PNG or other image file;
- the README names `01_integrated_reader`, `03_tex_source`,
  `05_quality_audit`, `07_agent_continuation`, and
  `08_local_review_material`; those directories are not present under the
  tracked source root.

These are catalog discrepancies, not grounds to delete the preserved guide or
recreate missing bytes speculatively.

## PDF Structure Replay

A bounded, read-only pass opened all 25 PDF paths with pypdf 6.12.2 and mutool
1.23.0:

- 25/25 containers opened; 769 pages; text-extraction failures 0; pages with
  no extracted text 0; mutool warning files 0;
- 4,461 named destinations, 1,778 internal `GoTo` actions, and 260 URI
  actions;
- 24 broken `GoTo` actions, consisting of the same 12 missing caption targets
  in each of the two autonomous-robots PDF builds;
- 1,030 outline entries and 358 per-document unique font-resource rows;
- Type 3 font rows 0; four unembedded rows are Base-14 Helvetica, with no
  other unembedded font row found;
- two page-image XObject rows, representing one image in the byte-identical
  event-fusion pair.

No page was rendered. These checks establish byte identity, container
readability, path closure, and link/font-resource structure only. They do not
establish visual quality, source fidelity, Ukrainian-language review,
mathematical correctness, work-level completeness, or accessibility.

## Exact Inventory

The bounded selection contains 99 files / 9,720,289 bytes:

- reader tree: 13 files / 4,710,882 bytes / SHA-256
  `62CC0C183CE09B21C0CBA9C4DF96EAF29D8526FB36A6E115050B06B0D957CDAE`;
- source tree: 86 files / 5,009,407 bytes / SHA-256
  `57341EDFD00182AD1C420B1EFAF379D7D1D6C514D7AE6F3E0C537262AD85739C`;
- aggregate tree: 99 files / 9,720,289 bytes / SHA-256
  `0E0F9701E2B931B8418F4C1B55E9A40A7A08FFA36C49F7CE9D003594B2D1E392`.

The canonical stream uses ordinal repository-relative path order and one
`relative_path<TAB>bytes<TAB>SHA256<LF>` row per file, UTF-8 without a BOM.

## Continue Without Losing Or Duplicating Work

1. Start from the exact module already present; do not retranslate PySDR,
   Zuazua Chapters 1-3, the sensor-fusion surveys, the robotics module, or the
   partial estimation modules merely because their QA remains open.
2. Use `main_public.tex` for the integrated editable surface. Keep `main.tex`
   as historical evidence until its six exact missing inputs are recovered or
   its supersession is producer-documented.
3. Preserve all four distinct direct/source PDF pairs. Their equal page counts
   do not make their bytes or text identical.
4. Route the twelve missing autonomous-robots caption targets and the four
   page-local direct/source text divergences back to the producing lane for
   verification; archive maintenance must not repair the PDFs or TeX itself.
5. Bind every future checkpoint by exact path, bytes, SHA-256, scope, and
   predecessor relation, then update this map instead of creating another
   unindexed tree.
