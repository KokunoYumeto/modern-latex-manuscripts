# EGA IV Sections 16-21 live source custody snapshot

Captured at `2026-07-31T05:26:00+02:00` after exact pre/copy/post identity checks.
This directory preserves the current editable source closures for the two
active EGA IV Part 4 alignment lanes and provides fresh three-pass convenience
builds from those copied bytes.

## Conservative checkpoint boundary

- Sections 16-18: producer checkpoint `checkpoint_printed132_r34`, aligned
  through printed page 132; conservative next page 133.
- Sections 19-21: producer checkpoint `build_p185_251_r13`, aligned through
  printed page 251; conservative next page 252.

The copied source files were newer than one or both named producer checkpoints.
Those later bytes are preserved because they are valuable live work, and the
fresh builds prove a coherent TeX closure. This snapshot does not promote
alignment coverage beyond the conservative checkpoint boundaries above.

## Build and public-reader hygiene

Both copied source closures built in three XeLaTeX passes with zero hard TeX
diagnostics. Extracted PDF text has zero private-path, task-ID, model-name, or
project-process hits. The convenience readers contain mathematical content,
title, and contents only; no status or AI preface is injected.

## Authority and exclusions

The controlling authority is the 360-page NUMDAM EGA IV Part 4 PDF, SHA-256
`B4277FB99C6EDF8FEEC5B01F54368E4B8521BCD52871316C0EDF6FF4AE69389E`. The authority PDF, source pixels, OCR bodies, raw logs,
auxiliary files, caches, and private process material are excluded here. The
actual high-detail source images are preserved separately on the existing EGA
Zenodo concept.

This is GitHub source survival and a buildable working snapshot. It is not a
complete EGA IV reader, critical edition, rights determination, peer review,
accessibility certification, or mathematical certification.
