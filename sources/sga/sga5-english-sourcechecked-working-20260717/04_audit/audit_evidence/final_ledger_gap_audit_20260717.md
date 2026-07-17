# SGA 5 English final ledger-gap audit — 2026-07-17

Audit snapshot: 2026-07-17 23:16 CEST.  This is a read-only review of the
active SGA 5 package and its durable audit reports.  No TeX, PDF, build log, or
active-package control file was edited by this reviewer.

## Concise gate result

**Manuscript/content evidence: PASS, with one documented source ambiguity.**

**Package/path integrity at this snapshot: FAIL pending the exact fixes below.**

**Public release: HOLD.**  Rights/license and attribution are unresolved, and
the final payload/checksum manifests did not yet exist at the audit snapshot.
No upload or DOI mutation is authorized.

The frozen primary objects rehash as follows:

| Object | Bytes | SHA-256 |
|---|---:|---|
| `SGA5_English_sync_workpass.tex` | 796,755 | `3CC5204680B2A2CE92FDF09401AB1A4654F9E0A4B0ED932D110FC0B1B024720F` |
| `SGA5_English_sync_workpass.pdf` | 2,054,026 | `176759209CD284F1DD6D3E26D0C7600EC146AB01FAA637BF6F6BB97BFAA396A4` |
| current French authority | 848,165 | `791F4EFFC5E02832D5D77ED03518C8156D6F07E4C8238B03545DB93D883FBB28` |
| legacy English witness | 756,192 | `6CEAB9D43C519EE7C9585933CC314A4807DC7A95750D1C8E8FAB2752A8EBF8CD` |
| original LNM 589 scan | 62,025,563 | `B256EBD072A8C68209518412A263C9289C6F1854A346733D86F885930D5FE6CA` |

The PDF has 309 pages.  The two final logs and the two console captures are
pairwise byte-identical and report a successful 309-page build.

## Required fixes before the package can be called manifest-complete

| ID | Severity | Finding | Exact required action |
|---|---|---|---|
| G-01 | blocking | `MANIFEST.csv` and `ZENODO_PAYLOAD_MANIFEST.csv` were absent.  `SHA256SUMS.csv` still named the superseded 756,217-byte TeX and 1,862,682-byte/295-page PDF. | Generate the two missing manifests after all evidence-path fixes.  Replace `SHA256SUMS.csv` with hashes of the frozen TeX/PDF and every promoted control/evidence file.  Verify every row from disk with zero missing paths, size mismatches, or hash mismatches. |
| G-02 | blocking | `SOURCE_CORRECTION_FINAL_RESOLUTION.csv` has 254 non-resolving `review_evidence` values when interpreted relative to the package: 197 `middle_residual.md`, 45 `late_residual.md`, and 12 `expose_i_residual.md`.  Hash-identical copies exist under `audit_evidence/`. | Change those values to `audit_evidence/middle_residual.md`, `audit_evidence/late_residual.md`, and `audit_evidence/expose_i_residual.md`, respectively.  The other 178 rows correctly name top-level `SOURCE_FORMULA_COMPARISON_EXACT.csv`. |
| G-03 | high | Top-level reports still contain non-package-relative evidence names.  `EXPOSE_I_VII_ADVERSARIAL_AUDIT_20260717.md` names bare `expose_i_residual.md` and `expose_vii_application_receipt_20260717.md`.  `EXPOSE_III_SOURCE_SYNC_REPORT_20260717.md` names `tmp/sga5_audits/...` from inside the package, plus a bare `sga5_fr_workpass.tex`. | Point report references to the packaged `audit_evidence/...` copies and to `../../02_native_examples/sga5_current_french_workpass/sga5_fr_workpass.tex`.  Do not leave paths that only work from the workspace root. |
| G-04 | high | Zenodo controls conflict.  `STATUS.md`, `PUBLICATION_READINESS.md`, the lane queue, and the lane release ledger identify `10.5281/zenodo.21416482` as the audited live version.  The later read-only check recorded in `INDEPENDENT_REVIEW.md` found latest concept version `10.5281/zenodo.21419947`; `21416482` is an earlier version under the same concept. | Reconcile every controlling document and payload row to concept DOI `10.5281/zenodo.20410947`, latest checked version `10.5281/zenodo.21419947`, and prior version `10.5281/zenodo.21416482` only as history.  Require a fresh latest-version check before any future versioning.  Never mint a competing concept. |
| G-05 | high | `00_lane_control/WITNESS_MANIFEST.csv` still records the old SGA5 synchronized TeX/PDF sizes, hashes, 295-page count, and `in-progress` status.  `ENGLISH_ZENODO_PAYLOAD_QUEUE_20260717.csv` still records SGA5 as `in-production`. | After package closure, update the two SGA5 witness rows to the frozen values above and PDF page count 309.  Use a status that distinguishes technical-content readiness from the continuing rights/Zenodo hold.  Update the queue consistently; do not mark it uploaded or publication-ready. |
| G-06 | medium | The 432-row historical `SOURCE_FORMULA_COMPARISON_EXACT.csv` uses `patch_record` values such as bare JSON/crop filenames and `swarm_results/...`.  These are archival provenance identifiers and do not resolve inside the package, although representative originals still exist elsewhere on disk. | Either add a short controlling note that `patch_record` is a historical identifier, not a package-relative file path, with the archived source root/hash; or provide a locator table.  Do not imply that all 432 patch-record strings are packaged files. |
| G-07 | advisory | The PDF's title, author, subject, and keyword metadata fields are empty. | Parent manager should either accept this explicitly as a citation/discoverability caveat or regenerate/re-QA the PDF with approved metadata after rights/attribution decisions. |

## Findings discovered and closed during this audit

The following defects were material when found but are closed in the current
snapshot.  They remain listed so later reviewers do not mistake the fixes for
never-tested assumptions.

| ID | Earlier defect | Current verification |
|---|---|---|
| C-01 | `EXPOSE_I_VII_ADVERSARIAL_REPAIR_MAP_20260717.csv` contained invalid CSV quoting in I-A004. | Fixed.  All 30 active-package CSVs now parse with Python `csv.reader(..., strict=True)`; every file has a constant column count. |
| C-02 | `STATUS.md` and `BUILD_WARNING_AUDIT.md` claimed zero LaTeX warnings. | Fixed.  The package now records three `\scriptsize`-in-math-mode warnings at TeX lines 3258, 3485, 5740/PDF pages 63, 67, 118, plus nine overfull boxes.  All affected pages were rendered and checked. |
| C-03 | The top-level terminology ledger omitted III B §5.6.1, §5.7.5, §5.8.1 and the twelve decisions in the nested III-B tranche ledger. | Fixed.  `TERMINOLOGY_REJECTED_CHOICES.csv` now has 40 strict-valid rows, including `SGA5-EDIT-016`--`018` and `SGA5-IIIB-001`--`012`. |
| C-04 | All 32 rows of `STRUCTURAL_PARITY_DIFFERENCES_FINAL.csv` still said `open-structural-review`. | Fixed.  All 32 now say `closed-see-representation-review`; the eight scalar deltas have matching closed classifications in `STRUCTURAL_PARITY_REPRESENTATION_REVIEW.csv`. |
| C-05 | Evidence paths in `STRUCTURAL_PARITY_REPRESENTATION_REVIEW.csv` and the III-B structural row of `SOURCE_CRITICAL_ADDITIONAL_REPAIRS.csv` were not package-relative. | Fixed.  They now point to existing `audit_evidence/...` objects. |
| C-06 | Final visual-QA documentation counted 26 high-risk pages and omitted the three font-warning loci. | Fixed.  `VISUAL_QA.md` records 28 high-risk pages and explicitly covers pages 63, 67, and 118. |

## Positive integrity checks

- `SOURCE_FORMULA_COMPARISON_EXACT.csv` and
  `SOURCE_CORRECTION_FINAL_RESOLUTION.csv` each contain the unique, gap-free ID
  set `SGA5-EXACT-0001`--`SGA5-EXACT-0432`.  Exposé, page, kind, old string,
  new string, and authority crosswalk exactly.
- The 432 final resolutions reconcile to 170 `propagated-exact`, 150
  `propagated-reviewed-nonexact`, 53 `reviewed-current-equivalent`, 51
  `reviewed-source-language-only`, and 8
  `rejected-absent-final-french-authority`; no row is pending.
- `SOURCE_CRITICAL_ADDITIONAL_REPAIRS.csv` is strict-valid and indexes 21
  non-candidate repair groups across I, III, III B, V, VI, VII, VIII, X, XII,
  XV, and the global K-bullet macro correction.
- The active `audit_evidence/` tree contains 60 files.  Each is byte-for-byte
  identical to its same-relative-path source under `tmp/sga5_audits` (60/60
  SHA-256 matches, no missing peer).
- `STRUCTURAL_PARITY_SUMMARY_FINAL.csv` has ten exposé rows and zero diagram,
  footnote, or list-item deltas.  Remaining scalar TeX-count deltas are
  individually classified as reviewed source-equivalent representations.
- The continuation cursor is closed through the Index on printed p.484.  The
  only carried source ambiguity is `SGA5-AMB-001`, the Exposé-I printed-p.43
  D-subscript; the current French-authority reading is preserved without a
  conjectural repair.
- SGA 1--4 controls exist on disk and match the hashes in
  `00_lane_control/WITNESS_MANIFEST.csv`: SGA 1, 2, 3, and 4 English PDFs plus
  the editable SGA 3 TeX.  The reports use them as terminology/style controls,
  not as authorities displacing the SGA 5 French workpass or scan.
- All 309 PDF pages have corresponding page renders; all sixteen contact
  sheets are populated 8-bit RGB PNGs.  Programmatic blank-page testing found
  no blank page.  Pages 88, 308, and 309 are intentional sparse end matter.
- The final build has 0 fatal errors, 0 package warnings, 0 pdfTeX warnings,
  0 underfull boxes, 3 reviewed LaTeX font warnings, and 9 reviewed overfull
  boxes.  This is an accepted-diagnostics build, not a warning-free build.

## Final manifest requirements

`MANIFEST.csv` should give, at minimum, package-relative path, role, bytes,
SHA-256, and payload disposition for the frozen TeX/PDF; both final logs and
console captures; correction/final-resolution and additional-repair ledgers;
formula and structural comparisons; terminology ledger; cursor/status;
source/formula summary; build-warning and visual-QA reports; independent
review; publication-readiness and license/attribution controls; every durable
audit-evidence file relied on by those controls; and the final visual-evidence
set or a sealed archive/hash of that set.  A manifest must not attempt to hash
itself unless an outer receipt supplies that hash.

`ZENODO_PAYLOAD_MANIFEST.csv` should mark each proposed file `include` or
`exclude` with a reason and exact frozen hash.  It must exclude the original
LNM 589 scan, the legacy English witness, SGA 1--4 controls, and transient
scratch/intermediate builds.  It must record the unresolved rights/license and
attribution hold, the existing concept DOI, the latest-version check, and the
prohibition on a duplicate concept record.  No row may imply that a public
upload already occurred.

After generating those files, run one final machine verification from disk:
strict-parse every CSV; resolve every controlling package path; verify bytes and
SHA-256 for every manifest row; confirm the TeX/PDF still have the frozen
hashes; and require zero unexplained mismatches.  Until that succeeds, the
package is technically content-complete but not manifest-complete.
