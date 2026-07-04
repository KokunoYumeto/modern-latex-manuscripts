# MY GOAL — read this first, every time

I am finishing **SGA5**: a complete, source-faithful, page-by-page corrected LaTeX edition of
*Cohomologie ℓ-adique et Fonctions L* (Springer LNM 589). This is my standing goal and I do not
consider it finished until **all 484 printed pages** have been audited and corrected. I keep going
on my own — across compaction, across checkpoints, while Floris sleeps. I do not stop to ask. I do
not babysit-stop every page. I am not done until the book is done.

**Why this matters:** SGA5 has ~1200 downloads, was never retyped (SGA1/SGA2 were, SGA5 wasn't),
and the earlier repair passes worked from a holey list that missed real errors (e.g. diagram
(4.4.2) was wrong and not even on the list). The point is to hand a mathematician a base they can
TRUST, so they do mathematics instead of spending two years fixing transcription. That is worth
the grind.

## How I work (non-negotiable behavior)
- **Big continuous batches.** Each turn: audit as MANY pages as the turn allows (aim 15+), one
  after another. No per-page chat. No stopping after one page. No "shall I continue".
- **Correct in place.** Every discrepancy → an edit to `sga5_fr_workpass.tex` right then. The log
  is a receipt, not the work.
- **One foreground shell call at a time. Never background anything.**
- **Resume, don't restart.** Always read `STATUS.md` first for the cursor page.

## The loop (per page)
1. Render: `_work\chunk_page.py <printed>` — source `C:\Users\Floris\Documents\Papors\OS\SGA5 (1).pdf`,
   **printed page = PDF page − 12**. 3 zoom chunks (top/mid/bot) at 2400px. Native scan is 360 dpi
   (the global ceiling — confirmed, nothing better exists); zoom equations finer when a glyph is
   ambiguous (`render_src.py <printed> --dpi 600 --y0 .. --y1 ..`, same pixels).
2. Read every chunk. Zoom every equation/diagram. Compare against `sga5_fr_workpass.tex`.
3. Fix every mismatch in place (prose, equations, symbols, diagrams, labels).
4. Log each correction in `FINDINGS.md` (source page + what + why).
5. Advance the `STATUS.md` cursor and page table.
6. Rebuild the index every ~20 pages: `_work\build_index.py`.
7. Only `ScheduleWakeup` (60s, `/loop …` prompt) when the turn is actually full.

## Watch for (the error classes already seen)
Wrong subscripts on ⊗ (bare ⊗^L in source); regrouped operators (f_*(A⊗B) vs (f_*A)⊗(f_*B));
H vs I, primes, shrieks (^! vs _!), iso-tildes dropped on arrows, missing arrows in ladders,
reversed inclusion arrows, dropped (*)/local labels. Typewriter primes/tildes are the hard ones —
zoom and, if truly unresolvable at native, say so in the log rather than guess.

## Files (all in `_claude_aid\sga5_full_audit_20260623\`)
- `sga5_fr_workpass.tex` — the file I'm correcting (base = repair032; Codex's 5 fixes verified good, kept).
- `STATUS.md` — resume tracker (cursor + page table). Read first.
- `FINDINGS.md` — logbook of every correction.
- `sga5_index.csv` / `.json` — machine-readable index.
- `SOURCE_AND_RESOLUTION.md` — source + dpi facts.
- `_work\` — chunk_page.py, render_src.py, build_index.py.

## Definition of DONE
All printed pages 1–484 audited (STATUS table full). Then: rebuild index, run `pdflatex` twice on
workpass (expect ~306 pp, 0 errors), produce `workpass_vs_repair032.diff`, write a final summary in
FINDINGS, and stop the loop (omit the next ScheduleWakeup). Until then: keep going.
