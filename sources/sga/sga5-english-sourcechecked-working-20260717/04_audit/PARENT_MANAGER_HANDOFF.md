# SGA 5 English source-checked handoff

Handoff date: 2026-07-17, Europe/Berlin.

Parent task: `IL Manager - English and Germanic`, thread
`019f70c0-aa55-7723-b00a-1d95324af359`.

Production task: `019f711e-cac3-7a10-a0e6-dc0131799c3a`.

## Disposition

The complete ten-exposé SGA 5 English cumulative is source-synchronized and
technically content-ready. Publication remains on hold for the parent manager's
rights/license and final attribution decision. No external upload, deposition,
or DOI creation occurred.

## Frozen primary artifacts

- TeX: `SGA5_English_sync_workpass.tex`, SHA-256
  `3CC5204680B2A2CE92FDF09401AB1A4654F9E0A4B0ED932D110FC0B1B024720F`.
- PDF: `SGA5_English_sync_workpass.pdf`, 309 pages, SHA-256
  `176759209CD284F1DD6D3E26D0C7600EC146AB01FAA637BF6F6BB97BFAA396A4`.
- French authority SHA-256:
  `791F4EFFC5E02832D5D77ED03518C8156D6F07E4C8238B03545DB93D883FBB28`.
- Legacy English witness SHA-256:
  `6CEAB9D43C519EE7C9585933CC314A4807DC7A95750D1C8E8FAB2752A8EBF8CD`.
- Original scan witness SHA-256:
  `B256EBD072A8C68209518412A263C9289C6F1854A346733D86F885930D5FE6CA`;
  audit-only, excluded from release.

## What changed materially

- Resolved all 432 scan-derived candidates and retained their final disposition.
- Closed residual/adversarial passes in every exposé, including formula signs,
  functors, indices, omitted proof steps, and arrow directions.
- Reconstructed the formerly absent Exposé III B §§5.0–5.8.
- Restored or corrected source-significant diagrams in I, III, III B, V, VII,
  X, XII, and XV; every exposé now has exact diagram-block parity.
- Corrected the global graded K-theory macro to `K^\bullet`.
- Applied layout-only repairs on PDF pages 4 and 118 and eliminated the earlier
  duplicate-destination/metadata warnings without changing mathematical content.

## Verification state

- Two successful frozen `pdflatex` passes.
- Zero fatal, package, pdfTeX, or underfull diagnostics; three localized LaTeX
  font warnings and nine overfull boxes were reviewed on rendered pages.
- All 309 pages rendered and inspected; high-risk repair pages received a
  separate review.
- Final correction, structural, terminology, cursor, build, visual, rights,
  manifest, and independent-review records are co-located with the workpass.

## Parent actions before publication

1. Review and record the rights/license decision and final attribution wording
   in `LICENSE_ATTRIBUTION.md` or a superseding parent control.
2. Reverify `SHA256SUMS.csv` and upload only the `include` rows in
   `ZENODO_PAYLOAD_MANIFEST.csv`.
3. Version the existing SGA concept DOI `10.5281/zenodo.20410947`; do not mint a
   duplicate. The latest record returned by Zenodo at the 2026-07-17 22:59 CEST
   freeze is `10.5281/zenodo.21419947`; `10.5281/zenodo.21416482` is the earlier
   lane-audited predecessor. Recheck the concept immediately before versioning.
4. Preserve the original exposé bylines, the Codex/GitHub legacy provenance, the
   2026-07-17 machine-assisted synchronization statement, and the bounded scope
   of the content-readiness claim.
5. If any primary file changes, rerun the two-pass build, all-page render QA,
   structural comparison, and every hash/manifest before release.

The carried source ambiguity is the printed-page-43 D-subscript in Exposé I.
It is explicitly logged as `SGA5-AMB-001`; no silent conjecture was made. The
known printed-page-14 defect is separately logged as `SGA5-EDIT-001` and needs
an explicit editorial footnote before publication; its rejected silent repair
is not synchronization debt.
