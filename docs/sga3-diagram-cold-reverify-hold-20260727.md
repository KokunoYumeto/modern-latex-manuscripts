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

- Expose VII: strict hold, with the diagram-repair gate now passed. All 32
  source-backed repairs passed fresh nonauthor review, the other 103 diagrams
  remain byte-identical, ambiguity is zero, and the evidence binds 300-dpi
  changed/seam pages, 600- and 1,200-dpi whole diagrams, and 128 targeted
  1,200-dpi details. The full 760-target source-context kind audit also passed;
  its two differences are manager-adjudicated as `diagram` and `theorem`.
  The hold remains because the final 135-target anchor resolution and
  exhaustive graph have not yet been bound to a new rebuilt package and exact
  terminal release audit. The earlier graph freeze is adverse history: it
  flattened inherited target kinds and falsely linked six TikZ coordinate
  literals (`2.1`, `3.3`, and `3.2`) as section references.
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
  No existing VII candidate may receive final publication/readback
  certification. A distinct post-reference rebuilt freeze and exact release
  handoff are required.
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
