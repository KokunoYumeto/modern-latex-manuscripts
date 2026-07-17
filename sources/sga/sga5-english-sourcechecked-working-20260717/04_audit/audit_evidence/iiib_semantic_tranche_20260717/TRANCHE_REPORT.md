# SGA 5 English — Exposé III B semantic tranche report

## Outcome

The remaining assigned Exposé III B semantic tranche is closed against the source-checked French authority and the original LNM 589 scan.

- Assigned receipt scope: 32 rows, excluding `0382–0406` because the inserted §§5.0–5.8 block had already closed them.
- Patched in this tranche: 22 receipt rows.
- Verified already current without rewriting: 10 receipt rows.
- Additional source-presentation repair: one (§5.9 inline extension-of-scalars functor), required to close the last III B display-count delta.
- Exact receipt result: 32/32 desired anchors present; inherited anchors absent for every patched row.
- Source ambiguity: none remains.

The production file moved from pre-tranche SHA-256 `8322E14DAEBE5EDFF35FCF5A71BFB863DE5C8AACEF5F1106D8394C5FB4496F07` to the immediate reviewed/build snapshot `9D97AB94F341801EC8937BD407440B4AD98E8DDD17EDE27A8C90CD243CF390BB`. Later non-overlapping edits outside Exposé III B moved the cumulative through coordination snapshots `94FD91FD0EF018E95D0C9EE04A34B8DDABCF3F7D5DB224B9D5320FE479B3EC25` and `237ACFB99BBD51A83495662F9D56260768DB7CFB4F22AE132583B2A3D71EF978` to final-package revalidation snapshot `313435A40E17DF53DC9C86D271548EFCE1C27520662D609D05C4FB373211E4F2`. Across all later snapshots, the Exposé III B UTF-8 slice is unchanged and has SHA-256 `0405187228682396D5D78830868277F35B37B3036BDF6435C139145E84246CC5`.

## Source-critical decisions

The tranche restores or corrects, among other details:

- the lowercase `$\phi$` / uppercase `$\Phi$` distinction in the Langlands datum;
- labels `(1)`–`(4)` on the §2.1 diagrams and their exact cartesian references;
- the unprimed `$M$` and tensor base `$S$` in §2.4;
- square `(*)`, displays `(2)` and `(3)`, and their dependent prose in §5.10.9;
- left/right module categories throughout §6.2;
- the exact second argument of 6.2.3;
- the source domain of local trace 6.5.3;
- tensor bases `$A,\Lambda,A$` and the final `$A$`-base identification in §6.6;
- both independent hypotheses of Proposition 6.23.

The potentially dangerous Proposition 6.23 correction was checked directly across scan printed pp.199–200: `$(fc_1)^{-1}(V)$` is connected and `$d_1^{-1}(V)\subset d_2^{-1}(V)$`. Neither the inherited equality nor an earlier shorthand that omitted the inclusion was retained.

## Build gate

This tranche's preserved PDF and log belong to the immediate build snapshot `9D97AB94F341801EC8937BD407440B4AD98E8DDD17EDE27A8C90CD243CF390BB`. The parent manager explicitly owns the final frozen cumulative rebuild after all non-overlapping tranches; this agent did not overwrite that final build boundary.

- Command: two consecutive passes of `pdflatex -interaction=nonstopmode -halt-on-error SGA5_English_sync_workpass.tex`.
- Result: both passes exit `0`.
- Output: 309 pages, 1,984,750 bytes.
- PDF SHA-256: `7E17A3BC0B72C678D2799340DFD16A93D1AFEC2FC9DD222644742F754B382C68`.
- Preserved build log SHA-256: `3AF212B050AE9EAAFFE93494C4979590571EC0322D3718B522DC043B3E0C3F86`.
- Fatal errors / emergency stops: `0`.
- Underfull boxes: `0`.
- The cumulative log retains eleven overfull-box notices and five pre-existing LaTeX warnings across the 309-page volume. The materially changed III B pages were rendered and inspected; none is clipped or colliding. English PDF page 114 was additionally rendered as a control for the inherited 8.095pt III B paragraph warning and is visually intact.

## Exact III B structural parity

| Feature | French | English | Delta |
|---|---:|---:|---:|
| `tikzcd` | 40 | 40 | 0 |
| `tikzpicture` | 1 | 1 | 0 |
| all diagram blocks | 41 | 41 | 0 |
| footnotes | 7 | 7 | 0 |
| equation environments | 145 | 145 | 0 |
| unnumbered display openings | 240 | 240 | 0 |
| list items | 9 | 9 | 0 |
| explicit tags | 151 | 151 | 0 |
| statements | 28 | 28 | 0 |

There is no remaining III B tag or statement-number multiset difference in `STRUCTURAL_PARITY_DIFFERENCES.csv`. Structural equality is used here as a gate alongside the receipt and source review, not as standalone proof of translation completeness.

## Render and scan QA

Twelve materially changed English PDF pages were rendered at 160 dpi, together with thirteen directly corresponding scan pages plus the continuation scan page for printed p.200. Every row in `RENDER_QA.csv` has verdict `pass`.

Inspected English PDF pages: `93, 94, 97, 111, 115, 119, 121, 123, 124, 128, 129, 135`; control page: `114`.

Inspected scan PDF pages: `156, 158, 161, 183, 188, 193, 196, 198, 199, 200, 204, 205, 211, 212` (printed pp.144, 146, 149, 171, 176, 181, 184, 186–188, 192–193, 199–200).

No clipping, formula truncation, broken glyph, diagram collision, orphan punctuation, or blank-page defect was found.

## Package contents

- `RECEIPT_CLOSURE.csv`: exact old/new closure for all 32 assigned receipt IDs plus the supplemental §5.9 repair.
- `REPAIR_EVIDENCE_LEDGER.csv`: printed source page, stable English line/statement anchor, exact correction, authority/evidence, and disposition for every receipt and supplemental repair.
- `ANCHOR_VALIDATION.csv`: stable-live uniqueness/legacy-absence disposition for all 32 assigned semantic anchors.
- `STABLE_LIVE_REVALIDATION.md`: current-live cumulative/slice hashes, anchor audit, the contextual `c_*` distinction, and regenerated III B parity.
- `SOURCE_FORMULA_COMPARISON.md`: formula-, category-, and scan-level adjudication.
- `TERMINOLOGY_REJECTED_CHOICES.csv`: retained terminology and rejected normalizations.
- `STRUCTURAL_PARITY_SUMMARY.csv` and `STRUCTURAL_PARITY_DIFFERENCES.csv`: regenerated against the reviewed production TeX.
- `BUILD_TRANCHE_IIIB_SEMANTIC_20260717.log`: preserved full cumulative build log.
- `RENDER_QA.csv`, `renders/english_contact_sheet.png`, `renders/scan_contact_sheet.png`, and individual rendered pages.
- `CONTINUATION_CURSOR.md`: durable end cursor for this tranche.
- `SHA256_MANIFEST.csv`: exact artifact hashes.

## Handoff boundary

The assigned Exposé III B semantic tranche is complete at receipt `0432` against final-package revalidation TeX snapshot `313435A40E17DF53DC9C86D271548EFCE1C27520662D609D05C4FB373211E4F2`. Line references in the repair ledger are tied to its unchanged III B slice hash `0405187228682396D5D78830868277F35B37B3036BDF6435C139145E84246CC5`. This report does not claim completion of the entire SGA 5 English cumulative or its publication payload; other exposés, cumulative formula review, final manifests, and publication readiness remain under the parent manager's global cursor.
