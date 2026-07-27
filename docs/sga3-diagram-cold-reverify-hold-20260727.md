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

- Expose VII: held. Its current independent R4 package audit also reproduces
  stale or normalized `raw_exact.line_text` in 230 of 1,395 rows across 36
  files. It cannot receive final publication/readback certification until both
  that machine-evidence defect and this diagram gate are closed.
- Expose XI: the diagram gate now passes. Receipt
  `DIAGRAM_COLD_REVERIFY_RECEIPT.json`, SHA-256
  `08C4C1D4314CAECD813761BF0EAA5FEB42268F387C58193FFD1098DAC8D6F619`,
  binds a fresh nonauthor review, four source and five target full pages at
  300 dpi, eight source and eight target whole-diagram views at 600 dpi,
  thirty source and thirty target detail crops at 1,200 dpi, and eight
  forensic plates. XI still lacks a sealed privacy-clean exact public
  projection and full release audit, so no publication is authorized yet.
- Any future Expose X or Exposes XII-XXVI diagram-bearing payload: held at
  release time until the same evidence is bound.
- Any cumulative SGA3 reader: every Codex-created or Codex-reconstructed
  diagram included in it must pass this control before a final cumulative
  seal.

The rule also carries forward to EGA diagram reconstruction.

## Published history

Already published bounded SGA3 checkpoints for I-IV, V, VI, VIII, and IX are
not deleted, rolled back, or silently relabeled as failures. They remain
immutable working-history objects. Their existence is not a final cumulative
SGA3 quality claim. Where their diagram evidence does not meet this newer
control, a complying additive successor is required before those diagrams are
used in a final cumulative SGA3 release.
