# SGA 5 English publication readiness

Assessment date: 2026-07-17, Europe/Berlin.

Decision: **CONTENT READY / ZENODO HOLD**.

## Technical gate

| Requirement | Evidence | Result |
|---|---|---|
| Complete editable English | `SGA5_English_sync_workpass.tex` | pass |
| Complete reader PDF | `SGA5_English_sync_workpass.pdf`, 309 pages | pass |
| French and scan authority pinned | `STATUS.md`, `LICENSE_ATTRIBUTION.md` | pass |
| All ten exposés source-checked | exposé reports, `SOURCE_CORRECTION_FINAL_RESOLUTION.csv`, `SOURCE_CRITICAL_ADDITIONAL_REPAIRS.csv` | pass |
| Exact correction/formula ledger | 432-row final-resolution ledger, initial correction ledger, additional-repair evidence index | pass |
| Formula/structure comparison | `SOURCE_FORMULA_COMPARISON_EXACT.csv`, final structural CSVs, representation review | pass |
| Terminology and rejected choices | `TERMINOLOGY_REJECTED_CHOICES.csv` | pass |
| Continuation cursor | `CONTINUATION_CURSOR.md`, closed through printed p.484 | pass |
| Two-pass build and retained logs | `BUILD_FINAL_PASS1_20260717.log`, `BUILD_FINAL_PASS2_20260717.log` | pass |
| Rendered visual QA | `VISUAL_QA.md`, `visual_qa/` | pass |
| Independent package review | `INDEPENDENT_REVIEW.md` | pass |
| Exact payload and checksum controls | `ZENODO_PAYLOAD_MANIFEST.csv`, `MANIFEST.csv`, `SHA256SUMS.csv` | pass when hash verification reports zero mismatches |

The technical gate depends on the exact SHA-256 values in the final manifests.
A renamed, rebuilt, or edited file is not covered by this assessment until the
manifests and QA evidence are regenerated.

The final build has no fatal, package, or pdfTeX warning. Its three localized
LaTeX font warnings and nine overfull-box diagnostics are enumerated in
`BUILD_WARNING_AUDIT.md`; every implicated page passed rendered inspection.
The PDF's internal descriptive title/author/subject/keywords fields are empty;
this does not affect content or rendering, but the parent manager must supply
the approved bibliographic metadata in the existing Zenodo concept record.

## Content-readiness basis

The active cumulative preserves the complete legacy English and synchronizes it
against the source-checked French workpass, with direct scan adjudication for
formula signs, indices, arrow topology, ambiguous glyphs, and source errors. All
432 scan-derived candidates have final dispositions. Additional residual passes
closed inherited omissions and non-candidate defects, including Exposé III B
§§5.0–5.8, Exposé VII's p.346 proof/diagrams, and final diagram-topology defects.

Every exposé has exact final counts for diagrams, footnotes, and list items. The
remaining scalar display/environment deltas are individually classified as TeX
representation choices in `STRUCTURAL_PARITY_REPRESENTATION_REVIEW.csv`; they do
not conceal omitted mathematics. One genuine source ambiguity survives at
Exposé I p.43 and is explicitly logged rather than guessed.

Exposé I p.14 also retains a known mathematical source defect. The controlling
ledger row `SGA5-EDIT-001` rejects a silent repair and requires an explicit
editorial footnote before release. This is a parent publication-policy gate,
not outstanding synchronization debt.

## Rights and attribution hold

No repository-level license or rights grant covering this English derivative
work was found. The original LNM 589 scan is an audit witness and is excluded
from the payload. The parent English manager must determine the permitted
license, copyright notice, and final attribution before public release. See
`LICENSE_ATTRIBUTION.md`.

The inherited English is old-laptop Codex/GitHub lineage, not Claude. The
2026-07-17 synchronization is a machine-assisted Codex workpass under Floris's
direction. Those provenance facts must not be converted into an invented human
translator credit or an unsupported critical-edition claim.

## Zenodo disposition

- Existing SGA concept DOI: `10.5281/zenodo.20410947`.
- Latest record returned by Zenodo at the 2026-07-17 22:59 CEST freeze:
  `10.5281/zenodo.21419947`.
- Earlier record audited by the parent lane: `10.5281/zenodo.21416482`.
- Neither record contains the SGA 5 English payload.
- Required action after the rights decision: create a new version of the
  existing concept record and upload exactly the rows marked `include` in
  `ZENODO_PAYLOAD_MANIFEST.csv`.
- Prohibited action: minting a competing concept record or uploading this
  payload while any hash, rights, attribution, or parent-manager gate is open.
- Because the concept is actively versioned by other lane work, recheck its
  latest-version endpoint immediately before creating the SGA 5 version.

## Scope of the claim

“Content ready” means the ten-exposé English cumulative in this directory is
current at the audited source-critical loci and has passed build and visual QA.
It does not claim a newly established copyright license, independent human
certification, coverage of unpublished/missing exposés outside this curated
cumulative, or authority over the original French edition.
