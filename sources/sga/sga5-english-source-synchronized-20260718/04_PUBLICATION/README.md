# SGA 5 English source-synchronized working edition

Checkpoint date: 2026-07-18.

## Scope

This package contains an editable TeX source and 309-page reader for ten
curated SGA 5 exposés: I, III, III B, V, VI, VII, VIII, X, XII, and XV, plus a
terminological index. It is a machine-assisted, source-synchronized working
edition. It is not complete SGA 5, a critical edition, certified, independently
human-reviewed, or rights-cleared.

## Source basis

The synchronization compared an inherited English witness with a pinned French
TeX control and consulted the original LNM 589 scan at ambiguous or
source-critical loci. External English translations were used only as
terminology/style controls. Their agreement is not source evidence.

The printed-p.14 source defect is preserved and explained in an editorial
footnote. The printed-p.43 D-subscript remains genuinely ambiguous; the
French-control form is retained and the alternative type-consistent reading is
disclosed rather than silently selected.

## Contents

- `00_EDITION`: repaired TeX and 309-page PDF;
- `01_BUILD`: two path-sanitized build logs and sanitization receipt;
- `02_SOURCE_REVIEW`: source/formula, correction, terminology, adverse-choice,
  reopened-locus, delta, and structural-parity evidence;
- `03_RENDERED_QA`: metadata receipt, six focused English-reader renders, and
  sixteen sequential contact sheets covering all 309 pages;
- `04_PUBLICATION`: scope, provenance, French-control reconciliation, Zenodo
  state, rights caveats, independent operational review, and exact member
  manifests.

`MANIFEST.csv` inventories all substantive support members except the two
manifest files. `SHA256SUMS.csv` hashes every final member, including
`MANIFEST.csv`, except itself; the final ZIP and four proposed public files are
hashed externally in the candidate `CONTROL` directory to avoid self-hash
cycles.

## Exclusions

The original scan and every scan-derived image are excluded. The French TeX and
reader, inherited English witness, external English candidates, private paths,
task identifiers, and unpublished correspondence are also excluded. External
controls are identified by exact hash and, where useful, a non-private
project-relative locator; no external control file is bundled.

## Current public-record context

The SGA concept DOI is `10.5281/zenodo.20410947`; the current version observed
at 2026-07-18T14:59:03Z is `10.5281/zenodo.21430393`. Its old English PDF and scan-bearing
support ZIP are proposed to be superseded by this checkpoint after a verified
archive-maintenance publication. The record metadata license
identifier `cc-zero` does not establish redistribution rights in the bundled
underlying or derivative works.
