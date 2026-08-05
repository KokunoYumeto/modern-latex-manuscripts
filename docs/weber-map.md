# Weber GitHub Coverage Map

Observed 2026-08-05. This page records the Weber material actually present in
GitHub so that readers and continuation tasks do not infer coverage from an
older catalog sentence or from filenames such as `complete`, `cert`, or
`current`.

These are working reconstructions and audit records, not critical editions,
peer review, or mathematical certification. English and German readers are
independent surfaces; an English reader is not silently synchronized merely
because a later German repair exists.

## Start Here

| Volume/layer | Best direct GitHub file | Exact represented state |
|---|---|---|
| Volume I German | [420-page working reader](../sources/weber/weber-volume1-german-complete-working-source-repair-20260731/reader/Weber_VolumeI_German_Complete_Working_SourceRepair_20260731.pdf) and [editable TeX](../sources/weber/weber-volume1-german-complete-working-source-repair-20260731/source/Weber_VolumeI_German_Complete_Working_SourceRepair_20260731.tex) | Complete working body through Section 188 and printed errata. The stricter cold page-by-page re-verification reaches printed p.124; p.125 is next. |
| Volume I English | [318-page Batch84 English reader](../sources/weber/Weber_Cumulative_ThreeVolumes_Batch84_Vol1_RecursiveAudit_p7_p14_20260604/02_cumulative_work/volume_1_complete_repaired_through_batch84/english/pdf/weber_volume1_cumulative_complete_batch84_english_translation.pdf) and [TeX](../sources/weber/Weber_Cumulative_ThreeVolumes_Batch84_Vol1_RecursiveAudit_p7_p14_20260604/02_cumulative_work/volume_1_complete_repaired_through_batch84/english/tex/weber_volume1_cumulative_complete_batch84_english_translation.tex) | Historical working translation. It predates many German repairs and is explicitly unsynchronized with the current German reader. |
| Volume II German | [218-page reader through Sections 1–143](../sources/weber/Weber_Cumulative_ThreeVolumes_Batch84_Vol1_RecursiveAudit_p7_p14_20260604/02_cumulative_work/volume_2_available/german/pdf/weber_volume2_cumulative_available_through_sections1_143_german_source.pdf) and [TeX](../sources/weber/Weber_Cumulative_ThreeVolumes_Batch84_Vol1_RecursiveAudit_p7_p14_20260604/02_cumulative_work/volume_2_available/german/tex/weber_volume2_cumulative_available_through_sections1_143_german_source.tex) | The direct GitHub filename and Batch84 control establish Sections 1–143, not Section 176. |
| Volume II English | [190-page reader through Sections 1–143](../sources/weber/Weber_Cumulative_ThreeVolumes_Batch84_Vol1_RecursiveAudit_p7_p14_20260604/02_cumulative_work/volume_2_available/english/pdf/weber_volume2_cumulative_available_through_sections1_143_english_translation.pdf) and [TeX](../sources/weber/Weber_Cumulative_ThreeVolumes_Batch84_Vol1_RecursiveAudit_p7_p14_20260604/02_cumulative_work/volume_2_available/english/tex/weber_volume2_cumulative_available_through_sections1_143_english_translation.tex) | Historical working translation through the same named range; no later synchronized layer is present in this shelf. |
| Volume III German | [251-page repaired cumulative](../sources/weber/Weber_Cumulative_ThreeVolumes_Batch84_Vol1_RecursiveAudit_p7_p14_20260604/02_cumulative_work/volume_3/german/pdf/weber_volume3_current_repaired_cumulative_german_source.pdf) and [TeX](../sources/weber/Weber_Cumulative_ThreeVolumes_Batch84_Vol1_RecursiveAudit_p7_p14_20260604/02_cumulative_work/volume_3/german/tex/weber_volume3_current_repaired_cumulative_german_source.tex) | Preserved Batch84 working cumulative. No read control establishes whole-volume completion or a continuation cursor. |
| Volume III English | [245-page repaired cumulative](../sources/weber/Weber_Cumulative_ThreeVolumes_Batch84_Vol1_RecursiveAudit_p7_p14_20260604/02_cumulative_work/volume_3/english/pdf/weber_volume3_current_repaired_cumulative_english_translation.pdf) and [TeX](../sources/weber/Weber_Cumulative_ThreeVolumes_Batch84_Vol1_RecursiveAudit_p7_p14_20260604/02_cumulative_work/volume_3/english/tex/weber_volume3_current_repaired_cumulative_english_translation.tex) | Preserved Batch84 working translation; not claimed synchronized with later German work. |

## Current Volume I German Surface

The [current package](../sources/weber/weber-volume1-german-complete-working-source-repair-20260731/)
contains 26 files / 11,500,208 bytes. Its own status and validation establish:

- 420 A4 pages through Section 188 and the printed errata;
- one self-contained 1,319,161-byte TeX source with native TikZ figures;
- a 2,275,193-byte reader with extractable text, no raster image XObjects, and no Type 3 fonts;
- a whole-body source-fidelity repair pass, held-section retranscription, four consistency sweeps, and broad visual spot checks;
- stricter cold re-verification only through printed p.124, with p.125 next;
- fourteen compact visual witnesses, eleven reviewed and three retained for the pending cursor.

This root supersedes the direct p.88 German reader as the current Volume I
German reading surface. It does not supersede or synchronize the older English
Volume I, Volume II, or Volume III readers.

## Preserved Volume I Predecessors And Audit History

### p.1–88 German gap-pass

The [p.88 checkpoint](../sources/weber/weber-vol1-b139-p001-p088-gap-pass-20260716/)
contains 54 files / 25,777,879 bytes. It freezes a 419-page German workpass
directly checked through printed p.88; p.89 was next in its declared p.1–99
tranche. Its certification and method logs preserve applied changes, rejected
candidates, source-print errors, reversals, and later escalation. In particular,
the sample-cert history records that nominally certified areas could still
contain reconstructed prose and therefore must not be treated as clean merely
because `CERT` appears in a filename. The 420-page package above is the later
German continuation surface.

### Batch84 three-volume history

The [Batch84 tree](../sources/weber/Weber_Cumulative_ThreeVolumes_Batch84_Vol1_RecursiveAudit_p7_p14_20260604/)
contains 23 files / 14,056,819 bytes. It preserves separate German and English
Volume I–III working readers plus a bounded Volume I Introduction audit of
printed pp.7–14. That audit restored omitted proof material and records the next
historical cursor as the paragraph beginning `Sind alpha,beta,gamma,delta jetzt
Zahlen`. The cursor belongs to this older recursive-audit generation; it does
not override the current strict cold cursor at printed p.125.

## High-Detail Visual Evidence

The [high-detail crop root](../sources/weber/weber-vol1-high-detail-audit-crops-20260723/)
is a manifest/control mirror, not an image payload in GitHub. Its README and
validation describe 248 page-mapped tight crops and 846 recovered images with
unresolved page locators, but the checked-in root contains no image files and no
two large crop ZIPs. GitHub preserves the two CSV manifests, parent identity,
validation, checksums, and build script.

The 248 mapped images retain exact printed-page/source-PDF locators. The 846
recovered images deliberately retain `volume_known_page_unresolved`; this map
does not invent coordinates. These are visual/provenance witnesses, not edition
or translation certification.

## Coverage Conflict To Preserve

Some older broad catalog prose says Volume II reaches Section 176. No tracked
reader or TeX file in `sources/weber` exposes that range. The exact direct files
present here say `sections1_143`, and no tracked Weber filename supplies a
Section-176 object. GitHub coverage is therefore reported as Sections 1–143
until an exact later checkpoint is supplied. The older statement remains
historical evidence, not proof of bytes in this shelf.

## Exact Content Inventory

The audited GitHub-native selection contains 110 files / 51,862,550 bytes.
Canonical tree SHA-256:
`E306F606FD55F575912D5A56F34E3352C402284325A5D8949DC7403944C67101`.

It covers all three reader/audit roots and seven files from the high-detail
control mirror. One external-upload wrapper manifest remains preserved in that
root but is outside this GitHub-content digest. See
[`20260805_web_map.json`](../manifests/github-custody/20260805_web_map.json)
for selection-level counts and hashes.

## Continue Without Duplicating Work

1. German Volume I: continue the strict cold pass at printed p.125; do not restart the completed working body.
2. English Volume I: reconcile against later German repairs before claiming synchronization.
3. Volume II: the exact GitHub continuation surface ends at Section 143. Do not claim or restart a later range without locating its immutable bytes first.
4. Volume III: inspect the retained readers paper-by-paper; no complete-volume or next-cursor claim is established here.
5. Preserve certification failures, rejected candidates, and source-print errors. Never reduce the logs to only accepted fixes.
