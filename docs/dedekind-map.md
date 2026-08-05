# Dedekind GitHub Coverage Map

Observed 2026-08-05. This page records the Richard Dedekind material whose
bytes are actually present in GitHub. It distinguishes current direct readers,
source-bearing partial work, broad reader-only drafts, a cross-author item, and
historical completion notes whose named artifacts are not currently tracked.

These are working reconstructions and preservation records, not critical
editions, peer review, or mathematical certification. German and English are
independent reading surfaces; neither language is proof that the other has
received the same later corrections.

## Start Here

| Work/layer | Independent readers | Exact represented state |
|---|---|---|
| *Gesammelte Mathematische Werke* I, items I–IV | [English, 24 pages](<../reader-pdfs/dedekind/01 Dedekind - GMW Volume I Items I-IV - English Translation Cumulative.pdf>) · [German, 27 pages](<../reader-pdfs/dedekind/02 Dedekind - GMW Volume I Items I-IV - German Source Cumulative.pdf>) | Current cumulative through printed p.39. Item V begins on printed p.40. Editable German and English TeX are in the [current source root](../sources/dedekind/DR16_V1_II_IV_p27_39/). |
| *Stetigkeit und irrationale Zahlen*, preface and §§1–4 | [English, 7 pages](<../reader-pdfs/classical/Dedekind - Continuity and Irrational Numbers, Preface and Sections 1-4 - English Translation Segment.pdf>) · [German, 8 pages](<../reader-pdfs/classical/Dedekind - Stetigkeit und irrationale Zahlen, Preface and Sections 1-4 - German Source-Checked Segment.pdf>) | Printed pp.315–328 of GMW III. §§5–7 remain. Editable TeX, status, audit, manifest, and the source slice are in the [segment root](../sources/classical/dedekind-dirichlet-current-starts/dedekind-stetigkeit-segment/). |
| GMW Bands I–III broad working readers | [Band I, 312 pages](<../reader-pdfs/classical/Dedekind - Gesammelte Mathematische Werke, Band I.pdf>) · [Band II, 304 pages](<../reader-pdfs/classical/Dedekind - Gesammelte Mathematische Werke, Band II.pdf>) · [Band III, 354 pages](<../reader-pdfs/classical/Dedekind - Gesammelte Mathematische Werke, Band III.pdf>) | Preserved reader-only modern-LaTeX drafts. No matching source/status tree for these three PDFs is included in the audited Dedekind selection, so filenames and page counts do not prove source-critical completion. |
| “Remark on Dirichlet's Works, vol. I, p.348, line 7” | [English, 2 pages](../sources/dirichlet/Dirichlet_R22_XXXVII_XLI_20260604/new/en/pdf/39_dedekind_note_en.pdf) · [German, 2 pages](../sources/dirichlet/Dirichlet_R22_XXXVII_XLI_20260604/new/orig/pdf/39_dedekind_note_de.pdf) | A Dedekind-authored note preserved inside the Dirichlet corpus, with independent TeX and PDF in both languages. |

## Current GMW I Continuation Surface

The [current status](../sources/dedekind/DR16_V1_II_IV_p27_39/00_status/status.md)
states that the cumulative readers contain item I, structurally checked over
printed pp.1–26, plus newly represented items II–IV over printed pp.27–39.
The packet contains ten files / 1,610,108 bytes:

- cumulative independent German and English TeX/PDF through item IV;
- independent German and English TeX/PDF for the new item II–IV tranche;
- a source scan slice for printed pp.27–39; and
- the status/continuation record.

The reported build gate is four successful TeX builds with no reported box,
warning, or error diagnostics, plus bounded spot-render checks. This map does
not repeat those renders or upgrade that report to a page-by-page audit.

Continue with item V, “Abriß einer Theorie der höheren Kongruenzen in bezug
auf einen reellen Primzahl-Modulus,” at printed p.40. Do not restart item I:
the older item-I paths are gone, but the current cumulative and status retain
that represented range.

## *Stetigkeit und irrationale Zahlen*

The [audit note](../sources/classical/dedekind-dirichlet-current-starts/dedekind-stetigkeit-segment/new-work-and-witnesses/audit/DEDK_ROUND01_AUDIT.md)
defines a bounded source-checked segment: title, dedication, contents fragment,
preface, and §§1–4 through the construction and ordering of cuts. Its source
range is printed pp.315–328 / source-PDF pp.319–332.

The root contains thirteen files / 4,669,337 bytes: cumulative German and
English TeX/PDF, duplicate new-work copies, a 3,517,051-byte source slice,
status/audit prose, and a package-era manifest. The two direct reader PDFs are
byte-identical to the cumulative PDFs. The retained status flags two readings
for later page-image review (`Durege` and normalized `Crelle's Journal`) and
states that §§5–7 remain through printed p.334/335.

The manifest uses earlier package-relative directory names
(`cumulative_current` and `new_work_this_round`); use the links on this page for
the actual current GitHub paths.

## Broad Bands I–III Readers

GitHub also preserves three large compiled readers under `reader-pdfs/classical`.
They are useful for reading and recovery, but this repository selection exposes
no matching editable source tree, range ledger, continuation cursor, or
source-check control for those exact three PDF bytes. Treat them as broad
working drafts and use the smaller source-bearing checkpoints above when an
exact continuation or correction must be justified.

## Historical Completion Notes That Need Artifact Recovery

Three narrative manifests survive as evidence of earlier work:

- [GMW I item I](../manifests/dedekind_gmw_volume_i_item_i_complete_20260604.md)
  reports complete German/English item-I readers and a source slice. Its named
  paths are not tracked now; the later p.1–39 cumulative is the usable surface.
- [*Was sind und was sollen die Zahlen?*](../manifests/dedekind_was_sind_zahlen_complete_20260602.md)
  reports complete German and English editions, but its named reader and source
  paths are not tracked now.
- [Dedekind/Dirichlet prefaces and notices LII–LIX](../manifests/dedekind_dirichlet_prefaces_notices_lii_lix_20260602.md)
  reports a German/English cumulative packet, but its named reader and source
  paths are not tracked now.

These notes are recovery leads, not proof that their referenced bytes remain
available. Locate and restore the exact old artifacts before fronting them;
do not spend another translation pass merely because the direct paths are
missing from today's tree.

## Exact Content Inventory

The audited GitHub-native selection contains 37 files / 14,578,425 bytes.
Canonical tree SHA-256:
`8CDDA297DDC20B36BA19D9415BF034A32105CFFC5195C0E68670C8631E312F15`.

It includes the current GMW I root, the full *Stetigkeit* segment, seven direct
Dedekind reader PDFs, four German/English Dedekind-note files embedded in the
Dirichlet tree, and the three historical completion notes. See
[`20260805_ded_map.json`](../manifests/github-custody/20260805_ded_map.json)
for selection-level counts and hashes.

## Continue Without Duplicating Work

1. GMW I: continue at item V / printed p.40; retain items I–IV as the current cumulative base.
2. *Stetigkeit*: finish §§5–7, checking the two flagged proper-name readings against the included source slice.
3. Recover the exact *Was sind und was sollen die Zahlen?* and LII–LIX artifacts named by the historical notes before assigning new translation work.
4. Keep the Dedekind note discoverable from both Dedekind and Dirichlet maps; it is one cross-author work, not two distinct translations.
5. Do not infer source fidelity, synchronization, or completeness from a broad PDF filename alone.
