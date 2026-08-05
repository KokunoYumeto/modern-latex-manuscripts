# Dirichlet GitHub Coverage Map

Observed 2026-08-05. This page records the P. G. Lejeune Dirichlet material
whose bytes are actually present in GitHub. It separates the current Band II
QA readers, their predecessor/tail source, a stricter source-checked Paper I,
the unsafe selected-works scaffold, and continuation packages that are
registered only by manifest.

These are working reconstructions and preservation records, not critical
editions, peer review, or mathematical certification. Original-language and
English files are independent surfaces; neither implies that the other has
received the same corrections.

## Start Here

| Work/layer | Independent readers | Exact represented state |
|---|---|---|
| *Werke* Band II, items I–XLI plus Band I errata | [Original languages, 280 pages](<../reader-pdfs/dirichlet/01 Dirichlet - Werke Band II Papers I-XLI - Original Languages Cumulative.pdf>) · [English, 217 pages](<../reader-pdfs/dirichlet/02 Dirichlet - Werke Band II Papers I-XLI - English Translation Cumulative.pdf>) | Current R23 QA readers. The prepended QA sheet preserves two open defects: item XXV needs full formula-level repair, and item XXVII still needs a typed German source track. |
| Band II Paper I, *Über die Stabilität des Gleichgewichts* | [German, 3 pages](<../reader-pdfs/classical/Dirichlet - Ueber die Stabilitaet des Gleichgewichts - German Source-Checked Edition.pdf>) · [English, 3 pages](<../reader-pdfs/classical/Dirichlet - On the Stability of Equilibrium - English Translation.pdf>) | Separately rebuilt against the scan, with editable TeX, audit, status, and manifests in the [Paper-I root](../sources/classical/dedekind-dirichlet-current-starts/dirichlet-stability/). Use this surface for Paper I rather than the rough selected reader. |
| R22 Band II predecessor and tail source | [Original languages, 279 pages](../sources/dirichlet/Dirichlet_R22_XXXVII_XLI_20260604/cum/pdf/dirichlet_b2_I-XLI_orig.pdf) · [English, 216 pages](../sources/dirichlet/Dirichlet_R22_XXXVII_XLI_20260604/cum/pdf/dirichlet_b2_I-XLI_en.pdf) | Earlier cumulative before the QA status sheet. The tracked root directly preserves TeX/PDF for items XXXVII–XLI and the Band I errata, plus indexes and locator text. |
| Selected-works scaffold | [241-page reader](<../reader-pdfs/classical/Dirichlet - Selected Works.pdf>) | Retained for recovery and comparison only. The source audit identifies omissions, construction artifacts, modern insertions, and mathematically material Paper-I errors. Do not front it as source truth. |

## Current Band II QA Surface

The two direct Band II readers are byte-identical to the cumulative PDFs in the
[R23 QA root](../sources/dirichlet/Dirichlet_R23_CumQA_V1src_20260604/).
The [44-row order ledger](../sources/dirichlet/Dirichlet_R23_CumQA_V1src_20260604/cum/index/order_b2_QA.csv)
records 42 carried-forward typographic tracks and two explicit repair states:

- **XXV, *Untersuchungen über ein Problem der Hydrodynamik***, Werke II
  pp.263–302: the prior German was a facsimile/source locator and the English
  was a normalized main-equation reading translation rather than a complete
  line-by-line mathematical translation. Full formula-level repair remains.
- **XXVII, Kummer's memorial address for Dirichlet**, Werke II pp.309–356:
  the English prose track is carried, but the German source track remains an
  image-only facsimile and needs a typed transcription.

The [repair queue](../sources/dirichlet/Dirichlet_R23_CumQA_V1src_20260604/audit/repair_queue.csv)
and [compaction audit](../sources/dirichlet/Dirichlet_R23_CumQA_V1src_20260604/audit/compaction_audit.md)
are controlling caveats. GitHub retains 39-page and 36-page source witnesses
for XXV and XXVII, plus a 23-page XXVII text draft explicitly marked
`not_promoted`. Do not erase those adverse states or describe the whole
cumulative as final.

R23 also stages a 21-page source witness for **Volume I Paper I**. It does not
claim a completed Volume I transcription or translation.

## Source-Checked Band II Paper I

The [source-completeness audit](../sources/classical/dedekind-dirichlet-current-starts/dirichlet-stability/new-work-and-witnesses/audit/DIRICHLET_SOURCE_COMPLETENESS_AUDIT_20260601.md)
documents why the selected-works reader cannot be trusted as a source. It
identifies three material Paper-I errors: a missing kinetic-energy term, an
equality where the source has a bound, and the wrong sign in the final example.
The independent three-page German and English readers in the Paper-I root are
the corrected GitHub surfaces and are byte-identical to their cumulative copies.

The old Paper-I status says Paper II is next. That cursor predates the later
Band II I–XLI cumulative and must not trigger a blind restart. Continue by
repairing the exact R23 defects or by recovering the later source packet first.

## R22 Tail And Cross-Author Material

The [R22 status](../sources/dirichlet/Dirichlet_R22_XXXVII_XLI_20260604/README.md)
adds items XXXVII–XLI and the Band I errata after the prior I–XXXVI cumulative.
The tracked tail includes the Kronecker and Humboldt correspondence, Dedekind's
remark on Dirichlet's Werke I p.348 line 7, Weber's remark, the translation
list, and the errata, each with original-language and English TeX/PDF.

The Dedekind-authored note is also cataloged on the [Dedekind map](dedekind-map.md).
That is one shared work with two catalog routes, not duplicate content.

## Partial Mirrors And Newline Normalization

The checked-in R22 and R23 roots are partial mirrors of their original package
manifests:

- R22: 35 tracked files; 33 of 131 manifest entries are present and 98 are not
  tracked here. Thirty-two present entries match directly. The remaining CSV
  differs only because Git stores LF while the package manifest hashed CRLF;
  reconstructing CRLF reproduces the manifest hash exactly.
- R23: 19 tracked files; 16 of 44 manifest entries are present and 28 are not
  tracked here. Twelve present entries match directly. Four CSVs differ only by
  LF/CRLF normalization, and CRLF reconstruction reproduces all four manifest
  hashes exactly.

This is not evidence of mathematical mutation, but it means the package
manifests must not be presented as complete inventories of the GitHub folders.
The GitHub-native tree hashes below bind the bytes actually tracked.

## Registered Continuation Packet, Payload Absent

The [v3 continuation registry](../manifests/source-intake/20260701_dirichlet_pro_continuation_packet_v3.md)
and [machine record](../manifests/source-intake/20260701_dirichlet_pro_continuation_packet_v3.json)
identify four ZIPs / 778,351,208 bytes:

1. controls and manifests;
2. Papers 01–14 foundation/cumulative;
3. Papers XXIII–XLI continuation; and
4. Volume I source backfill through p.80.

Those four ZIP bytes are not tracked in GitHub. Their recorded local path is a
historical locator, not current public custody proof. Recover and hash-replay
the exact registered ZIPs before assuming their internal sources are available
or beginning duplicate reconstruction.

## Historical Notes With Missing Named Paths

Three older notes remain useful provenance but point to paths no longer
tracked: [Band II I–XII](../manifests/dirichlet_band_ii_status_20260602.md),
[Band II I–XXXV](../manifests/dirichlet_werke_band_ii_through_paper_xxxv_20260604.md),
and [Dedekind/Dirichlet notices LII–LIX](../manifests/dedekind_dirichlet_prefaces_notices_lii_lix_20260602.md).
The current QA readers subsume the Band II ranges as reading surfaces, but not
all old per-item source bytes. The LII–LIX artifacts require recovery.

## Exact Content Inventory

The audited GitHub-native selection contains 81 files / 74,831,618 bytes.
Canonical tree SHA-256:
`74C47AB45A853FC548D12D0F798C39381937E7E0ECA8C7CEDE6C19E065EF054E`.

It includes both Band II generations, the complete Paper-I source/audit root,
five direct readers, and five historical/source-intake controls. See
[`20260805_dir_map.json`](../manifests/github-custody/20260805_dir_map.json)
for selection-level counts, hashes, and mirror diagnostics.

## Continue Without Duplicating Work

1. Repair Band II XXV at full formula and line level using the retained witness.
2. Produce a typed German source track for Band II XXVII; keep its facsimile and rejected draft as history.
3. Recover and replay the exact v3 continuation ZIPs before restarting Papers II–XLI or Volume I through p.80.
4. Do not use the 241-page selected reader as source authority.
5. Preserve R22 as predecessor history and R23's status sheet/repair queue as the current cumulative caveat surface.
