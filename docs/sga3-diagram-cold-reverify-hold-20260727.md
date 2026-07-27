# SGA3 diagram cold-reverify hold

Date: 2026-07-27

Status: controlling release hold for pending unpublished diagram-bearing SGA3
payloads and for future EGA diagram work.

The external manager control is the local lane-control file
`SGA_DIAGRAM_CLAUDE_STYLE_COLD_REVERIFY_HIGH_ZOOM_CONTROL_20260727.md`.

- bytes: 4,268
- SHA-256:
  `8682D7E64EADF2E92F8015EF79BA337D3ADB062B232F296DEB6C4009360D10CB`

This repository note records the rule and its release effect. It does not
claim that the external control file itself is part of a Zenodo payload.

## Required release evidence

Every pending unpublished SGA3 payload containing reconstructed mathematical
diagrams must bind all of the following before final publication/readback
certification:

- a source-context full-page render at 300 dpi or higher;
- every full diagram at 600 dpi or higher;
- ambiguous labels, decorations, or punctuation at 900-1200 dpi, or clearer
  original-source detail;
- at least four targeted detail crops for each nontrivial diagram and at
  least two for each simple diagram, with more whenever ambiguity remains;
- an exact node, arrow-direction, arrow-label, decoration, and terminal-
  punctuation inventory;
- source page, delivered page, coordinates, source-image hash, target-PDF
  hash, crop paths and hashes, reviewer disposition, and repair identity;
- comparison of source crop, diagram TeX, and delivered PDF, including the
  prose immediately before and after the diagram;
- a fresh final cold reverify by a reviewer who did not author the diagram.

Build success, source-code inspection, OCR, extracted text, contact sheets,
native-diagram status, and pixel similarity are supporting evidence only.
Contact sheets can navigate the review but cannot carry the PASS.

Any repair requires a fresh build, changed-page render, complete high-zoom
diagram reinspection, and adjacent-page seam check when pagination or flow
can change.

## Affected pending SGA3 work

The following known unpublished diagram-bearing scopes are controlled:

- Expose VII: strict hold. The 32 source-backed diagram repairs passed their
  scoped high-zoom review, but a later cold page replay found a delivered-page
  layout collision: footnote 41 overlaps DIAG033 inside footnote 40 on
  physical page 26 / printed page 22. Stable finding
  `IR-SGA3-VII-DIAGRAM32-PAGE026-FOOTNOTE-OVERLAP-001` controls. All current
  VII COW r1/r2 generations are adverse pre-layout-fix history. The earlier
  graph freeze is independently adverse: it flattened inherited target kinds
  and falsely linked six TikZ coordinate literals (`2.1`, `3.3`, and `3.2`)
  as section references.
  The controlling local hold is
  `SGA3_EXPOSE_VII_HIGH_ZOOM_DIAGRAM_32_REPAIR_HOLD_20260727.md`, 3,179
  bytes, SHA-256
  `AA121D61219000E22A3AB46113F180A8A001FAE5B65FEE6566AC352725C5A7F6`.
  The additive detector hold is
  `SGA3_EXPOSE_VII_NATIVE_DIAGRAM_REFERENCE_DETECTOR_FAIL_20260727.md`,
  3,973 bytes, SHA-256
  `D984FEF9257BBC978DBB55127E1379A8F69328A50AF43CA9ABBF2A4BDBAB7705`.
  Its statement that repaired `diagram_049.tex` remained byte-identical is
  append-only corrected by
  `SGA3_EXPOSE_VII_NATIVE_DIAGRAM_REFERENCE_DETECTOR_IDENTITY_CORRECTION_20260727.md`,
  2,364 bytes, SHA-256
  `569CC7AD3821B858314FA84E698D2D397E645E2D5CBF32AE1FD48989BE402508`.
  The two target-kind decisions are bound by
  `SGA3_EXPOSE_VII_TARGET_KIND_TWO_ROW_ADJUDICATION_20260727.md`, 3,066 bytes,
  SHA-256
  `FA22E7149B4CB6F71A534CB9472650D51725C9F66DB3078650C20D735AAF217C`.
  The current controlling page-layout hold is
  `SGA3_EXPOSE_VII_PAGE26_DIAG033_FOOTNOTE_OVERLAP_FAIL_20260727.md`, 5,837
  bytes, SHA-256
  `7FDB876D090F7C8ED228BBC2DAB1BEE52206E33B35C37DE1F9127431F2F624D5`.
  Its independent FAIL report has SHA-256
  `2AE8B40411F7C389BBDFAFD8C9FB0C918C5CE23ACC683028C001EDEF415D8FAF`;
  the corresponding FAIL validation has SHA-256
  `2796F2342D21994EB405F832DC5876F4F4E98A7F8D8CD639591FE2EA4A046F71`.
  No existing VII candidate may receive final publication/readback
  certification. A no-overwrite layout repair, full 300/600/900-1,200-dpi
  replay, fresh source freeze, rebuilt graph/package, privacy and rights
  closure, and independent terminal release PASS are required.
- Expose XI: the diagram gate passed and the exact bounded checkpoint is now
  public on same-concept record
  [21630748](https://zenodo.org/records/21630748). The public-package receipt
  `DIAGRAM_COLD_REVERIFY_RECEIPT.json`, SHA-256
  `D852EECC167479848EA85831389A54CC1607B937EBCB3CF9130AE43EF8964F22`,
  binds the target-only public 300-dpi full pages, 600-dpi whole diagrams,
  and 1,200-dpi detail crops. Authority-derived source pixels and forensic
  side-by-side plates remain excluded. The exact 124-member source/QA archive
  and all 74 record files passed anonymous readback.
- Any future Expose X or Exposes XII-XXVI diagram-bearing payload: held at
  release time until the same evidence is bound.
- Any cumulative SGA3 reader: every Codex-created or Codex-reconstructed
  diagram included in it must pass this control before a final cumulative
  seal.

The rule also carries forward to EGA diagram reconstruction.

## Published history

Already published bounded SGA3 checkpoints for I-IV, V, VI, VIII, IX, and XI are
not deleted, rolled back, or silently relabeled as failures. They remain
immutable working-history objects. Their existence is not a final cumulative
SGA3 quality claim. Where their diagram evidence does not meet this newer
control, a complying additive successor is required before those diagrams are
used in a final cumulative SGA3 release.
