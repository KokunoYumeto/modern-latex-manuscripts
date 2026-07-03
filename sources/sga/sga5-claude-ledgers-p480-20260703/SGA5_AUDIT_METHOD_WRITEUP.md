# Source-faithful audit of SGA 5 by a verify-gated agent workflow

*Method and results. Written 2026-06-25, on completion of the full page-by-page pass.*

## What was done

SGA 5 (*Cohomologie ℓ-adique et fonctions L*, Springer LNM 589) was checked page by
page against the original scan, and every discrepancy in the working LaTeX transcription
was corrected. All 484 printed pages were covered. The corrected file
`sga5_fr_workpass.tex` compiles to 307 typeset pages with zero errors. Around 300
discrepancies were fixed, each backed by a crop of the scan.

The point was a base a mathematician can trust. SGA 5 was never retyped the way SGA 1 and
SGA 2 were. Earlier repair passes only touched diagrams, and they worked from a partial
manifest, so they missed prose and symbol errors entirely — including a diagram that was
simply wrong and was not even on the list.

## The method

Four steps per page, the last one done by hand.

1. **Render.** `chunk_page.py` cuts each printed page into three overlapping crops
   (top / middle / bottom) at high zoom from the 360-dpi scan. The scan has 12 front
   pages, so printed page = PDF page − 12.

2. **Audit.** One read-only agent per page. It reads the three crops, greps and reads the
   matching stretch of the `.tex`, and compares element by element. It returns exact,
   unique `old_string → new_string` patches, each tagged: **type-A** (the `.tex` is wrong),
   **type-B** (the source itself has a defect — preserve it, do not invent a fix), or
   **cosmetic** (no meaning change).

3. **Verify.** One adversarial agent per candidate fix. It defaults to REJECT and has to be
   argued out of it. It checks four things: the `old_string` is unique; the source actually
   supports the new reading; the change is not merely cosmetic; and the **direction** is
   right — a fix must make the `.tex` match the source, never undo a standardization the
   editor applied on purpose.

4. **Apply and gate.** Every accepted fix is reviewed by eye against the scan, applied with
   a deterministic unique-match applier (`patch_apply.py`, which refuses any patch whose
   target is missing or non-unique, and keeps a `.bak`), and gated on `pdflatex`: the build
   must stay at 307 pages and 0 errors or the change is backed out.

A `Workflow` script (`_work/sga5_audit_workflow.js`) drives steps 2–3 as a pipeline, about
30 pages per batch, one batch at a time. Steps 1 and 4 stay in the foreground.

## Lessons

**Agents over-revert.** Left alone, the audit agents over-weight literal fidelity and
propose undoing the editor's defensible corrections — stripping a uniform `⊗` subscript
standardization, or reverting an obvious source-typo fix back to the typo. The verify
prompt was hardened to reject these, but the human review at step 4 is still required. The
verifier is a filter, not a substitute for looking.

**A clean compile is not enough.** A reconstructed `tikzcd` whose arrow label held an
unbraced comma — `"t\mapsto(t,0)"` — compiled with zero errors but silently ate a whole
page: TeX read the comma as an option separator, broke the arrow, and swallowed everything
up to the next `\subsection*`. The page count dropped from 307 to 306 with no warning. The
rule that came out of this: after inserting any diagram or float, check that the page count
is unchanged **and** render the page — do not trust a 0-error build. The fix is to brace
comma-bearing label content, `"{t\mapsto(t,0)}"`, which is the file's own convention.

**A handful of conventions carry most of the meaning,** and getting them wrong is invisible
to a casual read:
- `x̄` (geometric point — stalks, strict localizations) versus plain `x` (dimension and
  codimension subscripts);
- `\Hom` versus `\underline{\Hom}` (global versus sheaf), and `\R\Hom` versus
  `\R\underline{\Hom}` (global derived versus derived sheaf Hom);
- `SGA` versus `SGAA` — the source writes "SGA A" for SGA 4, and dropping the second A
  silently re-points a cross-reference at a different seminar volume;
- Tate-twist signs: `(\mu_n)^{\otimes -d}`, where a dropped minus flips the twist.

**Error density tracks math density.** Clean prose runs about one fix per two pages. Dense
regions run much higher — the §9 blow-up argument and the Grothendieck-written Exposé I were
the worst.

## Representative fixes

- **§9, systematic.** The pushforward `v_*` was repeatedly mis-transcribed as the pullback
  `v^*` through the blow-up argument; equation terms were dropped; one concluding equation
  was wrong. This stretch alone held ~16 consequential errors — the clearest evidence the
  second pass earns its keep.
- **(9.8.8), Lemme 9.8.7.** Two diagrams (a cartesian square and a commutative diagram) plus
  their connecting prose had been dropped; `v_*` should have read `v''_*`. Both diagrams were
  reconstructed from the scan and restored.
- **Local duality, p2.** The perfect pairing had been flattened: the first term, a *stalk*
  of the dual `\underline{\H}^i(F')_x`, had been turned into a local-cohomology group,
  erasing the very asymmetry that is local duality.
- **Cross-references.** Twelve `SGA → SGAA` corrections in Exposé I, each re-pointing a
  citation at SGA 4 as the source intends.

## Reproduce

Scripts (all rerunnable, no GPU): `_work/chunk_page.py`, `_work/sga5_audit_workflow.js`,
`_work/patch_apply.py`. Trackers: `STATUS.md` (resume cursor and per-region coverage),
`FINDINGS.md` (per-page logbook with source evidence), `_work/patches_p*.json` (the exact
patch sets the workflow produced, with the agent's evidence for each). Working file:
`sga5_fr_workpass.tex` (base = `repair032`; edits go here, not the canonical, so the diff is
reviewable).

## Cost

Roughly 44–65k tokens per page, ~0.7M per 15-page batch. The binding limit is the
rate/session ceiling, not the token budget: throttled or failed agents bill almost nothing,
while completed ones do the heavy reading, so a verify-gated workflow over hundreds of pages
beats hundreds of manual single-page cycles. Run one workflow at a time.
