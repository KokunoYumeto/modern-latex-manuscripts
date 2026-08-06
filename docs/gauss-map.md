# Gauss GitHub Coverage Map

Observed 2026-08-06. This page records the Carl Friedrich Gauss material whose
bytes are actually present in GitHub. It separates the bounded Band II
source-aligned stream, two small translation pilots, eight broad working
readers, their component-source and repair generations, and a much larger
continuation packet that is registered but not tracked.

These are working reconstructions and preservation records, not critical
editions, peer review, or mathematical certification. Original-language and
English files are independent surfaces; neither implies that the other has
received the same later corrections.

## Start Here

| Work/layer | Independent readers | Exact represented state |
|---|---|---|
| *Werke* II, actual beginning through printed p.303 | [Original language, 224 pages](<../reader-pdfs/gauss/12 Carl Friedrich Gauss - Werke Band II Actual Beginning through Printed Page 303 - Original Language.pdf>) · [English, 194 pages](<../reader-pdfs/gauss/13 Carl Friedrich Gauss - Werke Band II Actual Beginning through Printed Page 303 - English Translation.pdf>) | Strongest bounded cumulative reader pair. The retained status reports source checking through p.303 and names p.305 as next, but its source/witness tree is not tracked in this repository. Recover the registered continuation packet before restarting or extending it. |
| *Theorematis arithmetici demonstratio nova*, Articles 5–7 | [Source, 2 pages](<../reader-pdfs/gauss/08 Carl Friedrich Gauss - Theorematis Arithmetici Demonstratio Nova, Articles 5-7 - Source Text.pdf>) · [English, 2 pages](<../reader-pdfs/gauss/09 Carl Friedrich Gauss - Theorematis Arithmetici Demonstratio Nova, Articles 5-7 - English Translation.pdf>) | Editable pilot source/translation with compile and text-leak checks. Exact scan-page references are recorded, but the source scans were not included and direct scan verification remains pending. |
| Seeber identity passage, *Werke* II p.193 | [Source, 2 pages](<../reader-pdfs/gauss/10 Carl Friedrich Gauss - Seeber Identity Passage - Source Text.pdf>) · [English, 2 pages](<../reader-pdfs/gauss/11 Carl Friedrich Gauss - Seeber Identity Passage - English Translation.pdf>) | Same pilot gate and same pending scan-verification caveat. |

## Bounded Band II Stream Through Printed Page 303

The [2026-06-04 status](../manifests/gauss_band_ii_through_printed_page303_20260604.md)
states that the cumulative pair reaches printed p.303 after adding Dedekind's
remarks to `De nexu`, pp.292–303. It reports no screenshots substituted for
equations, tables, or diagrams and gives `Geometrische Seite der ternaeren
Formen`, printed p.305, as the forward target.

The two direct PDFs are present, but the status's named source/witness root is
not tracked. Treat “source-checked” as the preserved producer claim for those
specific bytes, not as a GitHub-replayable source audit. Do not restart the
earlier p.1–303 work merely because its scans and editable cumulative source
are absent here.

Older notes for the [p.211 cumulative](../manifests/gauss_band_ii_through_printed_page_211_status_20260602.md)
and [biquadratic Articles 30–76](../manifests/gauss_biquadratic_articles_30_76_status_20260602.md)
point to direct files and source roots no longer tracked under those names.
Their ranges are historical/recovery evidence; the p.303 pair is the current
direct bounded reading surface.

## Broad Working Readers

Eight direct PDFs are byte-identical to the eight cumulative PDFs in the
[2026-05-30 rebuild](../sources/gauss/gauss-current-cumulative-rebuild-2026-05-30/).
The rebuild appends source-checkable repair supplements; it does not assert that
every inherited component is clean.

| Surface | Direct reader | Pages | May 2026 component audit |
|---|---|---:|---|
| Band I | [working reader](<../reader-pdfs/gauss/00 Carl Friedrich Gauss - Werke, Band I - Modern LaTeX Working Edition.pdf>) | 260 | 10 grade-A TeX components. |
| Band I alternate | [working reader](<../reader-pdfs/gauss/01 Carl Friedrich Gauss - Werke, Band I - Alternate Modern LaTeX Working Edition.pdf>) | 300 | 10 grade A, 1 grade C. |
| Band II | [working reader](<../reader-pdfs/gauss/02 Carl Friedrich Gauss - Werke, Band II - Modern LaTeX Working Edition.pdf>) | 309 | 10 grade A, 1 grade D; one 85 MB component was flagged oversized. Prefer the bounded p.303 pair above for sequential work. |
| Band III | [working reader](<../reader-pdfs/gauss/03 Carl Friedrich Gauss - Werke, Band III - Modern LaTeX Working Edition.pdf>) | 326 | 11 grade A. |
| Band VI | [working reader](<../reader-pdfs/gauss/04 Carl Friedrich Gauss - Werke, Band VI - Modern LaTeX Working Edition.pdf>) | 812 | 11 grade A, 1 grade C, 6 grade D; four repair supplements are appended, but unresolved inherited OCR risk remains. |
| Band VII | [working reader](<../reader-pdfs/gauss/05 Carl Friedrich Gauss - Werke, Band VII - Modern LaTeX Working Edition.pdf>) | 476 | 13 grade A, 1 grade D; three repair/fill supplements are appended. |
| Band XI Part I | [working reader](<../reader-pdfs/gauss/06 Carl Friedrich Gauss - Werke, Band XI Part I - Modern LaTeX Working Edition.pdf>) | 331 | 10 grade A plus a recovered supplement. |
| Individual papers | [working reader](<../reader-pdfs/gauss/07 Carl Friedrich Gauss - Individual Papers - Modern LaTeX Working Edition.pdf>) | 247 | 10 grade A. |

The source component shelf also contains Bands IV and V, even though no direct
cumulative reader is fronted for them. The audit classifies Band IV as 5 grade
A / 2 C / 2 D and Band V as 10 A / 2 C / 2 D. Their absence from the reader
list is not absence of work; it is a quality/presentation distinction.

## Component Sources, Audits, And Repairs

The [component root](../sources/gauss/source_tex_and_component_pdfs/)
contains 118 TeX files and 118 PDFs across ten groups: Bands I, I alternate,
II–VII, XI Part I, and individual papers. One extra Band-I PDF has no TeX mate
and is retained as adverse history rather than silently deleted.

The [triage](../sources/gauss/audit_reports/GAUSS_TRIAGE_REPORT.md) records
100 grade-A, 6 grade-C, and 12 grade-D TeX files. It is heuristic QA, not source
certification. The initial compile environment rejected unguarded `microtype`;
a later compile test built 76 selected chapters / 2,157 pages after the local
workaround. Display audits called seven or eight combined PDFs clean candidates,
which means the sampled rendering passed that display gate—not that their
mathematics or transcription was source-complete.

The rebuild root preserves fourteen compiled repair sources, including Band I
fills, two Band II passages, one Band III repair, four Band VI repairs, three
Band VII repairs, and a Band XI recovery. They are appended repair witnesses;
do not infer that every grade-C/D component was superseded.

## Two-Unit Band II Pilot

The [pilot root](../sources/gauss/band-ii-pilot-current/gauss-band-ii-pilot/)
contains 175 tracked files / 12,375,035 bytes. In addition to the four direct
source/translation PDFs and their TeX, it preserves the full 118-file source
TeX snapshot, repair-source snapshot, priority queue, P0/P1 holdouts, audit
tables, compile logs, and bounded render witnesses.

The pilot status explicitly says packet 01 did not include the source scans.
Its cited source pages must be checked before the two units are upgraded to a
scan-verified claim. The direct files are byte-identical to the pilot cumulative
PDFs; they are not duplicates of distinct intellectual work.

## Registered Continuation Packet, Payload Absent

The [v3 continuation registry](../manifests/source-intake/20260701_gauss_pro_continuation_packet_v3.md),
[machine record](../manifests/source-intake/20260701_gauss_pro_continuation_packet_v3.json),
and [combined intake note](../manifests/source-intake/20260629_gauss_dirichlet_pro_continuation_packets.md)
identify nine ZIPs / 2,783,070,272 bytes. They cover controls, pp.1–76,
pp.149–211, pp.212–268, `de nexu`, later repair/audit rounds, literal repairs,
and late closure/geometric ternary-form work.

None of those nine ZIP payloads is tracked in GitHub. The intake note also
records a control-ZIP self-hash caveat: use the root registry hash, not an older
internal self-hash. The recorded absolute local path is a historical locator,
not current public-custody proof. Recover and hash-replay the exact ZIPs before
starting new p.305 work or assuming later repairs are available.

## Exact Content Inventory

The audited GitHub-native selection contains 528 files / 381,814,974 bytes.
Canonical tree SHA-256:
`85E34D7B0E0FDE7A865D2D9432E713AD0A5AB0C05E62AE86A4E578599194C337`.

It includes all 508 files under `sources/gauss`, all fourteen direct readers,
and six historical/source-intake controls. See
[`20260806_gauss_map.json`](../manifests/github-custody/20260806_gauss_map.json)
for selection-level counts and hashes.

## Continue Without Duplicating Work

1. Recover and replay the exact nine-ZIP v3 packet before restarting Band II p.1–303 or beginning p.305.
2. If the packet is unavailable, continue only from the precise p.305 cursor and preserve the missing-source limitation.
3. Verify the two pilot passages against their cited scan pages before upgrading their status.
4. Prioritize unresolved grade-C/D components in Bands IV–VII; use source scans rather than the broad readers as authority.
5. Keep broad working readers, repair supplements, rejected/OCR components, and bounded source-aligned readers as distinct generations.
