# Hi Claude — Codex notes for SGA 6 idx685--702 and the unindexed back matter

Floris asked that scan/workpass issues be marked durably where the French workpass lives. I did **not** edit `sga6_fr_workpass.tex`. The English synchronization used French commit `8ccdcf8eeef35cba9cc7ca09fe79e6b3f863becc` (workpass SHA-256 `77703F2D7E8FF9000C2C1E7320A903A48ADE00BF62C8F5F240FF88C42ED82703`), whose certified checkpoint ends at idx662. Everything noted here is therefore post-checkpoint and remains `PENDING_CLAUDE`.

## Definite scan/workpass discrepancies

1. **idx686 / printed 673 / source-PDF 676** — after `c_i(E)`, the scan says that `E` is a vector bundle on `X`, or more generally an arbitrary element of `K^\bullet(X)`. The workpass omits this explanatory parenthesis.

2. **idx694 / printed 681 / source-PDF 684** — the workpass gives `H^2`; both scans give `H^{2\bullet}`. This appears to be a dropped bullet.

3. **idx695 / printed 682 / source-PDF 685** — the workpass has `\mu_2^{\otimes 3}`. Low- and high-resolution scans give `\mu_\ell^{\otimes 3}`. The surrounding text fixes `\ell` as the cohomological prime. The English draft uses the scan reading.

4. **idx700 / printed 687 / source-PDF 690, bibliography [3]** — the workpass expands Bott--Samelson with a title and page range not printed in the scan. The scan has only the authors, journal, volume 80, page 1004, and year 1958. If the expanded citation is retained, it should be labelled editorial enrichment rather than source transcription.

5. **unindexed source-PDF 698--702 / printed 696--700, notation index** — please verify and restore the visible typographic distinctions flattened in the workpass:

   - subscripts in the `D(A_S)` family;
   - paired ordinary/underlined `parf`, `f-parf`, and `Y-parf` forms;
   - underlined `S` in the third `D(S,A)`-type entry;
   - `E|` (not `F|`);
   - `f_{gr}` (not bare `gr`);
   - `\widehat G_a` and `\widehat G_g`;
   - underlined `\operatorname{Pic}^{\circ}_{X/k}`;
   - `r^0_{\mathcal O_{U\times V}}` (not `X\times V`);
   - `1+\widehat B^+`;
   - terminal `Z(x)` (ordinary `Z`, not `\mathbb Z`).

## Source anomalies to retain or resolve editorially

- **idx701 / bibliography [16]** — the scan itself prints `(SGA 6)` in the Deligne entry. The English draft retains it pending an explicit editorial decision.
- **idx701 / bibliography [17]** — the author is printed `U. Mausin`. The English draft retains that spelling pending an explicit editorial decision.
- **volume pagination** — printed page 690 is absent from the 702-page scan. The terminological index begins on printed 691 / source-PDF 693. Please keep the gap explicit rather than forcing a false one-to-one sequence.

## Coverage warning

idx702 ends Exposé XIV, but not the volume. Ten additional scan pages remain: the terminological index (source-PDF 693--697) and index of notations (source-PDF 698--702). The true final leaf is source-PDF 702 / printed 700 and ends at `Z(x)`.

The English tranche is source-checked against both scans, but it remains explicitly `DRAFT_AFTER_CERTIFIED_CHECKPOINT` until the French lane certifies it.
