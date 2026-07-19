# SGA2 English `F`/`G` notation adjudication

Date: 2026-07-19  
Decision: `EG-SGA2-FG-NOTATION-ADJUDICATION-20260719-0001`

## Ruling

Option A is approved. The SGA2 English register retains calligraphic
`\mathcal F` and `\mathcal G` for coherent sheaves when that established
target-language convention is already in use. This is a deliberate English
normalization from the corrected French source's upright roman `F` and `G`;
it is not source-glyph preservation.

The ruling changes provenance descriptions, not sealed mathematical targets.
No sealed TeX, PDF, render, hash, or package may be silently mutated.

## Source basis

- Authority style file:
  `source_control/french_arxiv/sga2-smf.sty`,  SHA-256
  `5895C022FAF0FC1294C7B8ECFE4E74C47329F02FF317B19170C52FA855224884`.
- `sga2-smf.sty:352` defines `\Fa` with `\DeclareMathOperator{\Fa}{F}`.
- `sga2-smf.sty:354` defines `\Ga` with `\DeclareMathOperator{\Ga}{G}`.
- `source_control/french_arxiv/sga2-smf.tex:75` sets
  `\setboolean{original}{false}`. The corrected branch therefore still renders
  upright operator `F`/`G` at these macro sites.
- The direct corrected-edition PDF agrees. It is layout/render corroboration of
  the same edition, not independent original-print evidence.

## Existing accurate baseline

`SGA2-VIII-P2-SETUP-TERM-011` already states the distinction correctly:
source/corrected upright `F` becomes calligraphic `\mathcal F` as an established
English-register normalization. That row remains the baseline control.

## Affected sealed controls

The following sealed units contain one or more provenance statements that
incorrectly describe the corrected French branch as calligraphic or
source-preserved:

- `SGA2-VIII-C22`;
- `SGA2-VIII-D2B`;
- `SGA2-VIII-III-IV`;
- `SGA2-VIII-IV-II-N0`;
- `SGA2-VIII-IV-II-N1`, including both `\Fa` and `\Ga`.

Their calligraphic English target glyphs may remain. Each unit must receive
append-only successor ledger/control records that:

1. identify upright roman `F`/`G` as the corrected French source rendering;
2. identify calligraphic `\mathcal F`/`\mathcal G` as deliberate English
   normalization;
3. explicitly supersede the inaccurate provenance claim without overwriting
   the old row or altering the sealed target/package;
4. preserve all prior hashes and custody history;
5. distinguish archive-message delivery from remote publication/readback.

If any affected object is already public, archive maintenance should preserve
version history and issue the provenance correction through the existing
concept/current-record workflow. This adjudication alone does not authorize a
new DOI, replacement PDF, or duplicate record.

## Prospective controls

- Active `SGA2-VIII-IV-II-NGT1` may retain calligraphic `\mathcal F` only if
  its normalization/adverse-delta ledger explicitly records the upright-source
  to calligraphic-target change before independent seal.
- Applications and all later SGA2 units must record source and target glyphs
  separately at preflight. “Corrected branch” never implies “calligraphic.”
- A later SGA2-wide typography-policy replacement may revisit the target
  register, but no local worker may silently switch or back-edit sealed units.

## Machine-readable control

The authoritative row-wise manager control is
`SGA2_ENGLISH_FG_NOTATION_ADJUDICATION_20260719.csv` (nine data rows, fourteen
columns). The accompanying XLSX is an internal human-readable rendering of the
same control, not a public payload.

