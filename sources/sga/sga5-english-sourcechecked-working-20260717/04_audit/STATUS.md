# SGA 5 English synchronization workpass

Status timestamp: 2026-07-17, Europe/Berlin.

## Current gate

**CONTENT READY / ZENODO HOLD.**

The sole active English cumulative is synchronized through the Index on printed
page 484 against the current source-checked French authority, with the original
LNM 589 scan used whenever either inherited text was ambiguous. All ten
published exposés in this cumulative— I, III, III B, V, VI, VII, VIII, X, XII,
and XV—have passed their source-critical formula, prose, statement, footnote,
item, and diagram-topology gates.

Technical completion does not authorize publication. The proposed payload is
held pending a recorded rights/license and attribution decision by the parent
English manager. No upload or new Zenodo record has been made.

## Source-critical receipt

- All 432 scan-derived candidates have a final resolution in
  `SOURCE_CORRECTION_FINAL_RESOLUTION.csv`: 170 propagated-exact, 150
  propagated-reviewed-nonexact, 53 reviewed-current-equivalent, 51
  reviewed-source-language-only, and 8 rejected because the candidate is absent
  from the final French authority.
- Additional repairs found by bilingual residual and adversarial comparison are
  indexed in `SOURCE_CRITICAL_ADDITIONAL_REPAIRS.csv`; their exact page, anchor,
  old/new reading, authority, and disposition are in the linked machine ledgers
  and audit reports under `audit_evidence/`.
- Exposé I closes 42 residual groups, 20 initial correction-ledger groups, and
  four final diagram-topology repairs. Its printed-page-43 glyph ambiguity is
  explicitly documented and was not guessed; the known printed-page-14 source
  defect is preserved source-faithfully and requires an editorial footnote
  before release rather than a silent emendation.
- Exposé III closes 34 candidate receipts and 19 structural repairs. Exposé III B
  includes the formerly omitted §§5.0–5.8 and closes the 33-row semantic tranche
  ledger.
- Exposés V, VI, VIII, X, XII, and XV received independent all-math/all-diagram
  residual passes. Exposé VII closes its 24 earlier nonexact receipts, 49 exact
  receipts, and 19 adversarial repairs.
- `STRUCTURAL_PARITY_SUMMARY_FINAL.csv` records exact diagram-block, footnote,
  and item counts in every exposé. The few scalar TeX-count differences are
  source-equivalent representation choices classified in
  `STRUCTURAL_PARITY_REPRESENTATION_REVIEW.csv`; no omitted mathematical
  assertion is hidden by those counts.

## Frozen build

- TeX: `SGA5_English_sync_workpass.tex`, SHA-256
  `3CC5204680B2A2CE92FDF09401AB1A4654F9E0A4B0ED932D110FC0B1B024720F`.
- PDF: `SGA5_English_sync_workpass.pdf`, 309 pages, 2,054,026 bytes, SHA-256
  `176759209CD284F1DD6D3E26D0C7600EC146AB01FAA637BF6F6BB97BFAA396A4`.
- Two final `pdflatex` passes completed with no fatal error, package warning, or
  pdfTeX warning. Three localized LaTeX font warnings (`\\scriptsize` requested
  inside math mode) and nine inherited/localized overfull boxes remain; every
  affected page was rendered and checked. See `BUILD_WARNING_AUDIT.md`.
- All 309 pages were rendered to PNG and reviewed by contact sheet, with a
  high-risk source-repair sample inspected at higher resolution. See
  `VISUAL_QA.md` and `visual_qa/`.

## Authorities

- Legacy English witness:
  `../../01_recovered_witnesses/sga5_english_legacy/SGA5_english_strict_cumulative.tex`,
  SHA-256 `6CEAB9D43C519EE7C9585933CC314A4807DC7A95750D1C8E8FAB2752A8EBF8CD`.
- Current French authority:
  `../../02_native_examples/sga5_current_french_workpass/sga5_fr_workpass.tex`,
  SHA-256 `791F4EFFC5E02832D5D77ED03518C8156D6F07E4C8238B03545DB93D883FBB28`.
- Original scan (audit witness only; excluded from payload):
  `C:/Users/Floris/Documents/Papors/OS/SGA5 (1).pdf`, SHA-256
  `B256EBD072A8C68209518412A263C9289C6F1854A346733D86F885930D5FE6CA`.
- English style controls: the on-disk SGA 1–4 English baselines recorded in the
  audit reports; they informed established English terminology but never
  displaced the SGA 5 source authority.

## Publication controls

`PUBLICATION_READINESS.md`, `ZENODO_PAYLOAD_MANIFEST.csv`,
`LICENSE_ATTRIBUTION.md`, `MANIFEST.csv`, and `SHA256SUMS.csv` control any
handoff. The existing SGA Zenodo concept DOI is `10.5281/zenodo.20410947`.
Zenodo's latest-version endpoint returned `10.5281/zenodo.21419947` at the
2026-07-17 22:59 CEST freeze; `10.5281/zenodo.21416482` is the earlier
lane-audited predecessor. The parent manager must recheck and version that
existing concept after resolving rights, not mint a duplicate.
