# Final source and formula comparison

Comparison date: 2026-07-17, Europe/Berlin.

## Authorities

- Final English TeX SHA-256:
  `3CC5204680B2A2CE92FDF09401AB1A4654F9E0A4B0ED932D110FC0B1B024720F`.
- Source-checked French TeX SHA-256:
  `791F4EFFC5E02832D5D77ED03518C8156D6F07E4C8238B03545DB93D883FBB28`.
- Original LNM 589 scan SHA-256:
  `B256EBD072A8C68209518412A263C9289C6F1854A346733D86F885930D5FE6CA`.

The French workpass controls the current correction state. The scan adjudicates
formula glyphs, arrow direction/topology, source errors, and any point where the
French or inherited English is ambiguous. The on-disk SGA 1–4 English editions
were used only for established English terminology and house style.

## Candidate-level result

`SOURCE_FORMULA_COMPARISON_EXACT.csv` preserves the 432 scan-derived candidate
rows and their initial exact-matcher evidence. Every row has a final bilingual
resolution in `SOURCE_CORRECTION_FINAL_RESOLUTION.csv`:

The exact CSV's `patch_record` field is a stable historical candidate-batch
identifier (for example `swarm_results/patches_rerun.json`), not a
package-relative path. The frozen, traversable evidence locator for each row is
the `review_evidence` field in `SOURCE_CORRECTION_FINAL_RESOLUTION.csv`; its
values resolve either to `SOURCE_FORMULA_COMPARISON_EXACT.csv` itself or to a
report under `audit_evidence/`.

| Final resolution | Rows |
|---|---:|
| propagated exact | 170 |
| propagated after reviewed nonexact English mapping | 150 |
| reviewed; current English already equivalent | 53 |
| reviewed; source-language-only change | 51 |
| rejected; absent from final French authority | 8 |
| **total** | **432** |

The eight rejected rows were not silently applied. Each retains its candidate
page, old/new strings, and authority explanation in the final-resolution CSV.

## Exposé-level formula and topology result

| Exposé | Final formula/source gate | Diagram topology | Key evidence |
|---|---|---:|---|
| I | 42 residual, 20 initial-ledger, 16 exact, and 4 adversarial groups current | 13/13 | `audit_evidence/expose_i_residual.md`; `EXPOSE_I_VII_ADVERSARIAL_AUDIT_20260717.md`; `EXPOSE_I_VII_ADVERSARIAL_REPAIR_MAP_20260717.csv` |
| III | 34 receipt and 19 structural groups current; 145 equations/tags | 60/60 | `EXPOSE_III_SOURCE_SYNC_REPORT_20260717.md`; `EXPOSE_III_REPAIR_MAP_20260717.csv` |
| III B | omitted §§5.0–5.8 restored; 145 equations, 151 tags, 240 displays | 41/41 | `audit_evidence/iiib_semantic_tranche_20260717/REPAIR_EVIDENCE_LEDGER.csv`; `audit_evidence/iiib_semantic_tranche_20260717/TRANCHE_REPORT.md` |
| V | all 193 display/equation blocks paired after full residual pass | 26/26 | `audit_evidence/expose_v_vi_viii_independent_residual.md` |
| VI | 122 paired displays; sole raw delta is inline `U(X)` | 3/3 | `audit_evidence/expose_v_vi_viii_independent_residual.md` |
| VII | 100 tags and 62 statements exact; 409/410 display wrappers with D1/D2 caption embedded in English | 15/15 | `EXPOSE_I_VII_ADVERSARIAL_AUDIT_20260717.md`; `EXPOSE_I_VII_ADVERSARIAL_REPAIR_MAP_20260717.csv` |
| VIII | all 110 displays paired; §8 module sides and Greek proof label corrected | 13/13 | `audit_evidence/expose_v_vi_viii_independent_residual.md` |
| X | ordered math 895/895 after normalization | 7/7 | `audit_evidence/x_xii_xv_independent_receipt/ORDERED_MATH_ALIGNMENT.csv`; `audit_evidence/x_xii_xv_independent_receipt/DIAGRAM_TOPOLOGY.csv` |
| XII | complete ordered-math review; display splitting/expanded proof classified separately | 4/4 | `audit_evidence/x_xii_xv_independent_receipt/ORDERED_MATH_ALIGNMENT.csv`; `audit_evidence/x_xii_xv_independent_receipt/DIAGRAM_TOPOLOGY.csv`; `audit_evidence/expose_x_xii_xv_independent_residual.md` |
| XV | complete ordered-math review; one formatting split classified separately | 5/5 | `audit_evidence/x_xii_xv_independent_receipt/ORDERED_MATH_ALIGNMENT.csv`; `audit_evidence/x_xii_xv_independent_receipt/DIAGRAM_TOPOLOGY.csv`; `audit_evidence/expose_x_xii_xv_independent_residual.md` |

The complete raw structural counts are in
`STRUCTURAL_PARITY_SUMMARY_FINAL.csv`. Every nonzero scalar count delta is
classified in `STRUCTURAL_PARITY_REPRESENTATION_REVIEW.csv`. The only multiset
differences are the 32 Exposé-I tag/statement representation rows enumerated in
`STRUCTURAL_PARITY_DIFFERENCES_FINAL.csv`; direct source review found no missing
mathematical statement behind them.

## Non-candidate discoveries

The exact matcher was not treated as an exhaustive audit. Independent ordered
formula, prose, and diagram passes found and repaired additional defects,
including wrong Tate-twist signs, source-significant underlines and functors,
reversed/missing arrows, omitted proof equalities and displays, the complete
III B §§5.0–5.8 sequence, K-theory grading, left/right module assignments, and
relative-Frobenius formulas. `SOURCE_CRITICAL_ADDITIONAL_REPAIRS.csv` indexes
the exact page-level ledgers and reports for these operations.

## Ambiguities and source errors

The terminology/rejected-choice ledger records every retained emendation or
rejected literal choice that affects interpretation. The sole unresolved glyph
is the Exposé-I p.43 D-subscript. It remains at the current French-authority
reading and is labeled `SGA5-AMB-001`; no smoother conjecture was substituted.
The separate known source defect at Exposé-I p.14 is retained source-faithfully
under `SGA5-EDIT-001`; publication requires an explicit editorial note rather
than an undocumented mathematical rewrite.

Verdict: all ten exposés are current at the audited mathematical, formula,
diagram, footnote, statement, and source-significant prose loci. This is a
source-synchronization verdict, not an independent critical-edition or rights
claim.
