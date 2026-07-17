# Independent final review — SGA 5 English synchronization workpass

Review date: 2026-07-17, Europe/Berlin.

Reviewer role: a separate final-audit pass within the SGA 5 production task,
performed against the frozen TeX/PDF and current control ledgers. The reviewer
participated in earlier bounded middle-exposé audit work, but did not edit the
frozen TeX, PDF, build logs, or final manifests during this final review. This
is independent package/source-evidence review in that limited operational
sense; it is not independent human scholarly certification.

## Review verdict

**Technical content pass / publication hold.**

The reviewed cumulative contains all ten published exposés in this workpass
(I, III, III B, V, VI, VII, VIII, X, XII, and XV), followed by the Index. The
source-critical cursor is closed through printed page 484. The final TeX and
PDF hashes match the frozen build controls, the two final build passes are
reproducibly identical at the log/console level, all 309 PDF pages render, and
the correction, structural, formula, terminology, and continuation evidence is
internally coherent at the checks described below.

This verdict does **not** remove the rights/license and attribution hold. It
does not authorize a public upload, claim an independent critical edition, or
turn machine-assisted provenance into a human translator credit.

## Frozen objects independently rehashed

| Object | Bytes | SHA-256 | Result |
|---|---:|---|---|
| `SGA5_English_sync_workpass.tex` | 796,755 | `3CC5204680B2A2CE92FDF09401AB1A4654F9E0A4B0ED932D110FC0B1B024720F` | match |
| `SGA5_English_sync_workpass.pdf` | 2,054,026 | `176759209CD284F1DD6D3E26D0C7600EC146AB01FAA637BF6F6BB97BFAA396A4` | match |
| `BUILD_FINAL_PASS1_20260717.log` | 49,352 | `4AEE7355405CCA10390DB2105F981F24E43DF9B02C0006DCADCA9DD16419F2C6` | match |
| `BUILD_FINAL_PASS2_20260717.log` | 49,352 | `4AEE7355405CCA10390DB2105F981F24E43DF9B02C0006DCADCA9DD16419F2C6` | match |
| `BUILD_FINAL_PASS1_20260717.console.txt` | 22,988 | `193023D40F6C77CDA92EEEC0ECDF708206B2DF1FAE5CCF921BBA727453E50BE6` | match |
| `BUILD_FINAL_PASS2_20260717.console.txt` | 22,988 | `193023D40F6C77CDA92EEEC0ECDF708206B2DF1FAE5CCF921BBA727453E50BE6` | match |

The immutable authorities also rehash to their pinned values:

- legacy English witness:
  `6CEAB9D43C519EE7C9585933CC314A4807DC7A95750D1C8E8FAB2752A8EBF8CD`;
- source-checked French workpass:
  `791F4EFFC5E02832D5D77ED03518C8156D6F07E4C8238B03545DB93D883FBB28`;
- original LNM 589 scan witness:
  `B256EBD072A8C68209518412A263C9289C6F1854A346733D86F885930D5FE6CA`.

The scan remains audit-only and is excluded from any proposed payload.

## Source and ledger integrity checks

1. `SOURCE_FORMULA_COMPARISON_EXACT.csv` and
   `SOURCE_CORRECTION_FINAL_RESOLUTION.csv` each contain 432 unique candidate
   IDs. Their ID sets and their source page, exposé, kind, old string, new
   string, and authority fields match exactly. Every final-resolution field is
   populated.
2. The 432 final dispositions reproduce the declared totals: 170
   `propagated-exact`, 150 `propagated-reviewed-nonexact`, 53
   `reviewed-current-equivalent`, 51 `reviewed-source-language-only`, and 8
   `rejected-absent-final-french-authority`.
3. `SOURCE_CRITICAL_ADDITIONAL_REPAIRS.csv` supplies the non-candidate residual
   and adversarial evidence across every exposé, including the omitted Exposé
   III B §§5.0–5.8, the Exposé VII proof/diagram tranche, and the global
   `K^\bullet` correction. Its linked repair maps and tranche ledgers exist.
4. The I/VII adversarial repair map closes 23 rows (4 in I and 19 in VII). The
   Exposé III repair map closes 53 rows (34 receipt and 19 structural rows).
   The III B semantic ledger closes 33 rows.
5. `STRUCTURAL_PARITY_SUMMARY_FINAL.csv` contains the expected ten exposé rows.
   Diagram-block, footnote, and list-item deltas are zero in every row. The
   eight remaining nonzero scalar TeX-count deltas have one-for-one closed
   classifications in `STRUCTURAL_PARITY_REPRESENTATION_REVIEW.csv`; the 32
   final multiset-difference rows are explicitly limited to the reviewed
   Exposé-I tag/statement representation differences.
6. `TERMINOLOGY_REJECTED_CHOICES.csv` records the chosen terms, rejected
   literal/editorial alternatives, retained source emendations, and the sole
   carried glyph ambiguity (`SGA5-AMB-001`, Exposé I printed p.43). The
   ambiguity is documented rather than silently guessed.
7. The SGA 1–4 English controls are present on disk and hash-match
   `../../00_lane_control/WITNESS_MANIFEST.csv`: SGA 1, 2, 3, and 4 PDFs plus the SGA
   3 editable TeX. They are correctly treated as terminology/style controls,
   not as authorities displacing the SGA 5 French workpass or scan.

These tests establish ledger integrity and the documented review coverage. They
do not infer completion merely from a successful compile or from the word
“final” in a filename.

## Build-log review

Both retained final `pdflatex` passes produced the same 309-page, 2,054,026-byte
PDF. The final log contains:

- fatal errors: 0;
- package warnings: 0;
- pdfTeX warnings: 0;
- underfull boxes: 0;
- localized LaTeX font warnings: **3**;
- overfull boxes: **9**.

The three `\scriptsize`-in-math-mode warnings map to PDF pages 63, 67, and 118.
The nine overfull-box diagnostics map to PDF pages 4, 45, 53, 73, 82, 85, 111,
115, and 266. Every implicated page was opened at rendered resolution. Labels,
arrows, formulas, and prose are present and legible; no content crosses the
physical crop, disappears, or collides. The build is therefore accepted with
reviewed diagnostics, not misreported as a warning-free LaTeX run.

## Programmatic and visual PDF review

PDF structure:

- page count: **309**;
- encryption: none;
- page boxes: 309/309 exactly 612 × 792 points (US Letter);
- page renders: 309/309 present at 850 × 1100 pixels;
- contact sheets: all 16 are 8-bit RGB, populated, and visually readable;
- unintended blank pages: **0**.

For the blank-page audit, extracted character counts were combined with a
grayscale ink proxy (pixels below value 250). No page has zero extracted text
and no page falls below 0.5% ink. A deliberately conservative candidate rule
(below 600 extracted characters or below 2% ink) identifies exactly pages 88,
308, and 309. Direct inspection shows intentional content: the Exposé III
bibliography/reference tail on p.88 and the terminological-index tail on
pp.308–309.

High-risk review covered the required final-layout pages 4 and 118; the Exposé
I printed-p.38, p.48, and p.71 diagram anchors; the changed Exposé III B pages;
the late Exposé VII repairs; and representative/final-fix pages throughout X,
XII, and XV. In particular, the printed-p.48 paired distinguished triangles
map to **PDF page 28**, not page 29. The corrected high-risk evidence now
includes `visual_qa/high_risk/page-028.png`; PDF 29 is retained as the adjacent
proposition/restatement context. Both are clean.

Detailed independent evidence remains in:

- `audit_evidence/final_visual_programmatic_audit_20260717.md`, SHA-256
  `CE6BBE309AB5E230C98B02A700E7F483C363352A2DA28CA32A6444A6010F4D54`;
- `audit_evidence/final_visual_programmatic_audit_20260717.csv`, SHA-256
  `E5611F3A1D3A3584142CAED39A4A5503F2084965A45871CE044EA89635BFF1F3`.

Those evidence copies are already co-located hash-identically under
`audit_evidence/`; any changed copy requires a new hash.

## Zenodo and publication-state check

The public Zenodo REST API was queried read-only during this review. The SGA
concept DOI is `10.5281/zenodo.20410947`. At the 2026-07-17 22:59 CEST check,
the concept endpoint resolved to current latest version
`10.5281/zenodo.21419947`, titled as the SGA 6 idx662 source-rescribe
checkpoint. `10.5281/zenodo.21416482` is an earlier idx646 version under the
same concept. Neither record's public file list contains this SGA 5 English
TeX/PDF payload.

Therefore the correct future route, after the rights decision and a fresh
latest-version check, is a new version of the existing concept record. Minting
a duplicate concept DOI or uploading an unverified/stale payload would violate
the package controls.

## Remaining caveats and gate conditions

1. No repository-level license or rights grant covering this derivative
   English work was found. Public release remains on hold until the parent
   manager records the permitted license, copyright notice, and final
   attribution.
2. The PDF's descriptive title, author, subject, and keyword metadata fields
   are empty. This does not affect text or rendering, but it is a publication
   discoverability/citation caveat for the parent manager.
3. The three font warnings and nine overfull boxes are accepted only because
   their exact rendered pages were reviewed; they must remain disclosed in the
   retained build evidence.
4. Exposé I printed p.43 retains the explicitly logged D-subscript ambiguity.
   No unsupported conjectural glyph repair should be introduced.
5. Exposé I printed p.14 retains the known source defect logged as
   `SGA5-EDIT-001`. Publication requires the explicit editorial note mandated
   by that ledger row; a silent mathematical emendation remains rejected.
6. Final payload manifests and checksums must be generated or reverified after
   this review and the detailed audit evidence are in their final package
   locations. Any later TeX/PDF/evidence edit reopens the affected build,
   render, and hash gates.
7. No upload, Zenodo mutation, DOI minting, or public-release action was
   performed by this reviewer.

Subject to those caveats, the frozen SGA 5 English cumulative passes this
independent technical content/package review and is ready for parent-manager
rights and publication coordination.
