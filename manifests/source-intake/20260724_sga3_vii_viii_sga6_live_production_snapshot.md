# SGA3 VII/VIII and SGA6 live-production custody snapshot

Observed: `2026-07-24T05:57:36.2916424+02:00`

This is a privacy-clean archive-control snapshot. It records one stable
bounded checkpoint inside a mutable SGA3 tree, one complete-body but
pre-release SGA3 state, and the current SGA6 cold-audit cursor. It is not a
body transport, publication authorization, or Zenodo mutation request.

## Public head

- Existing SGA concept: `10.5281/zenodo.20410947`.
- Current SGA version:
  [`10.5281/zenodo.21523096`](https://doi.org/10.5281/zenodo.21523096).
- GitHub `main` at the start of this sweep:
  `a13e4d3be41617a0e497da689e8ea1b17b55b035`.
- The current public record already closes the SGA6 ultra-detail
  visual-evidence increment through idx378. This snapshot does not reopen or
  duplicate that publication.

## SGA3 Expose VIIA stable checkpoint

Local root name: `sga3_exposeVII_english_reconstruction_20260724`.

The root is mutable because VIIB production has begun, but the producer
created a distinct complete-VIIA build directory and QA receipt before
continuing.

- Scope: complete Expose VIIA, Polo--Gille local pages 1-60, combined-reader
  pages 454-513, re-edition printed pages 443-502.
- Next checkpoint boundary: Expose VIIB local page 1 / combined page 514 /
  printed page 503.
- Reader:
  `build_viiA_complete/SGA3_Expose_VIIA_English_Loop1_Complete.pdf`,
  73 A4 pages / 835,831 bytes, SHA-256
  `32C8D81F790FB66AEF7E0828FCDD31CCDEDF98A0BB4C244EDAB878D9FF177641`.
- Checkpoint QA:
  `qa/VISUAL_QA_CHECKPOINT04_VIIA_COMPLETE.md`, 4,476 bytes, SHA-256
  `59214B9FF52BC1C62CBE0C6EA6DB13DA1533EAF9B424368C8F3D66EBDAC952CB`.
- Checkpoint master identity: 2,505 bytes, SHA-256
  `A84D1377D7742AECEC55E5A215E435D23308D4D00EA49AB78E5F67648C2BB17E`.
- The old checkpoint wrapper is no longer a separate live file. Its exact
  identity was independently replayed in memory from the current 2,644-byte
  master by removing only the two complete VIIB input lines. The replay
  matched the checkpoint hash above.
- The 15 VIIA component files total 216,335 bytes. Their sorted
  `relative_path TAB bytes TAB SHA256`, no-terminal-LF aggregate is
  `F54E73ED8CE5EE32E20490694B1C0A6A70F0A3161DFB347F7F32032B4608E7A3`.
- The 78 uniquely resolved Loop-1 PNG dependencies total 459,606 bytes. Their
  equivalent aggregate is
  `A664D2837009F99F88BD9037208C7E14A16702B573D3A9FFA2FA0D1AA0CE0991`.
- All 73 pages were rendered and visually inspected; three XeLaTeX passes
  completed without fatal, undefined-reference, duplicate-destination,
  missing-character, or overfull-box diagnostics.

This is a coherent bounded Loop-1 checkpoint, but it is not an archive
handoff. VIIB is already active, all 78 source-derived PNG diagrams still
need native Loop2 reconstruction, exhaustive convention-v2 closure remains
open, and no privacy-clean immutable public projection or independent
release seal exists. The source-derived pixels therefore remain local and
rights-caveated.

## SGA3 Expose VIII complete-body pre-release state

Local root name: `sga3_exposeVIII_english_reconstruction_20260724`.

- Scope: complete English body of Expose VIII through its bibliography;
  Expose IX is excluded.
- Current master:
  `tex/SGA3_Expose_VIII_English.tex`, 1,513 bytes, SHA-256
  `42441AE14E33CFCEC7D239C05F0061FA96674B0C560965DA7C0062F31B6993A8`.
- Pre-reference reader:
  `build/full_exposeVIII_r10_pre_reference/SGA3_Expose_VIII_English.pdf`,
  31 pages / 680,305 bytes, SHA-256
  `490B466416C3194DF8F43DF533BB0870FBDE3B2618B6397946A52EDAE7BE8006`.
- Graph-only validation:
  `control/reference_v2_r1/VALIDATION.json`, 5,300 bytes, SHA-256
  `34B4E50747B5712B96B904FDE4D16A5D4454A35390ACA6FB445EEC6ECF73C566`,
  status `PASS`, errors `[]`.
- Graph counts: 10 source dependencies, 154 targets, 520 candidates, 181
  linked edges, 339 residuals, 87 planned actions, 109 existing-link
  candidates, and nine unavailable existing wrappers.

The PASS is expressly limited to graph/source/application-plan checks.
Wrappers and target markers have not been applied. No compiled
destination/action replay, post-application build, visual release gate,
sealed public projection, or archive handoff exists. This tree is active
production and is not queued for GitHub body publication or Zenodo.

## SGA6 cold source audit

Local root name: `sga6_full_audit_20260703`.

The live audit had advanced to entry `#1139`, cold re-verification of
`idx387`, with `idx388` next.

- French workpass TeX: 1,320,410 bytes, SHA-256
  `BC1E14DE020AA72BCBA056C10BF6BA893665093A10537B62DC172B600AD80457`.
- Current reader: 373 pages / 2,871,580 bytes, SHA-256
  `27B0168E5F9F986BFAD070C7EAA2C7F0E900EF1735F1FE6DAFAD685E12B225BB`.
- Current TeX log: 46,586 bytes, SHA-256
  `4B5409540C581D3B6740FA28129264CF2FCE5D50D58A140C88C5B89D2712CD25`.
- `CERT_LOG.md`: 8,990,465 bytes, SHA-256
  `B8401A43F11E2556666BB032E8B3BE08FFBC9B4E4B5EE574064CF20E2A27E39C`.
- `sga6_fr_workpass.out` was a zero-byte transient at the snapshot boundary,
  SHA-256
  `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855`.

The files were stable during each individual hash read, but the tree remains
live and may change immediately afterward. The zero-byte auxiliary is not a
payload defect and is not mirrored. The audit has moved beyond the public
idx378 visual-evidence boundary; a later crop successor requires a distinct
sealed selection, rights curation, exact provenance, and independent replay.

## External sweep and disposition

- A fetch of all GitHub remotes found no project branch newer than current
  public `main`.
- No relevant new package appeared in the standard Downloads roots during
  this sweep.
- GitHub action: publish this metadata-only custody snapshot.
- Zenodo action: none.
- SGA3 VIIA: preserve the exact checkpoint identity, but do not infer a
  release from a mutable producer root.
- SGA3 VIII: complete-body pre-release work only.
- SGA6: active audit cursor only; do not upload live workpass files or
  transients.

This snapshot does not certify translation completeness beyond the stated
bounded scopes, source fidelity beyond the cited local controls,
mathematical correctness, rights clearance, accessibility, or critical
edition status.
