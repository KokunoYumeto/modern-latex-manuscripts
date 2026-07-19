# Visual rights, live-tree drift, and record file limits

## What worked

- Separating project-generated target renders from source-derived page images
  made visual QA publishable without inventing redistribution permission.
- A rights-blocked image row remains useful when it records the parent PDF
  hash, physical page, bounding box, pixel dimensions, DPI, rotation, image
  hash, structural unit, review role, and disposition.
- Direct PDF and TeX downloads are preferable for the current bounded reader
  while a record remains comfortably below its file ceiling. Evidence and
  render collections can stay in coherent ZIPs with machine-readable indexes.
- At the 100-file ceiling, consolidating checksum-only controls preserves more
  reader value than removing a PDF, editable source, evidence package, visual
  package, or current status file. Historical versions retain the superseded
  control CSVs.

## Failure and recovery

- One self-gated handoff supplied an exact TeX hash that no longer matched the
  live local tree at intake. The PDF and most evidence still matched, but the
  package could not honestly be called an exact checkpoint.
- The correct response was a quarantine receipt: preserve the live bytes,
  record both expected and observed hashes, and withhold preferred or sealed
  status. Do not silently rewrite the producer manifest and do not discard the
  failed receipt.
- A later independently sealed successor supplied a new manifest, TeX, PDF,
  build, visual, and validation chain. That successor superseded only the
  self-gated/quarantined state; the quarantine remains failure evidence.

## Method change

Every custody intake now distinguishes four checks:

1. The delivered receipt parses and names an exact bounded scope.
2. Every manifest row matches the live tree at intake.
3. The public projection excludes local-only material and gives every image a
   rights disposition rather than silently dropping it.
4. A successor states exactly which prior state it supersedes.

Delivery, live-tree verification, independent sealing, GitHub backup, Zenodo
publication, remote readback, rights clearance, and human validation remain
separate states. A technically useful unit may be backed up on GitHub without
being promoted as a standalone Zenodo release or a cumulative work.
