# Re-certifying SGA 5 by hand: method and lessons

*A companion to the source-faithful LaTeX edition `sga5_fr_workpass.tex` (SGA 5 = LNM 589,
Cohomologie ℓ-adique et fonctions L). Written for the open-source release alongside the edition,
`ERRATA_LNM589.md`, `CERT_LOG.md`, and `AGENT_SCORECARD.md`.*

## Why this was done

SGA 5 has thousands of downloads and, unlike SGA 1 and SGA 2, was never retyped — it circulates only
as a scan of the mimeographed typescript (Springer LNM 589). A machine-assisted "audit swarm" had
already produced a corrected LaTeX transcription, but a swarm that reports "audit complete" cannot be
trusted as a *certification*: it can miss, and it can silently invent. The goal here was a base a
mathematician can build on without re-checking — established the only way that earns trust: **by hand,
one page at a time, every symbol against the scan.**

This document records the method and what it taught us. It is deliberately not a completeness claim
(see *Status* at the end).

## The source and the edition

- **Source:** `SGA5 (1).pdf` = the full LNM 589, 496 PDF pages = printed p1–484, all exposés. The
  scan tops out at ~360 dpi; that is the global resolution ceiling (no higher-res scan exists), so
  ambiguous glyphs are read from 600 dpi *crops* of that same scan, not a better source.
- **Offset:** printed page = PDF page − 12, holding book-wide.
- **The edition** `sga5_fr_workpass.tex` is a **curated selection of 10 exposés** — I, III, III B, V,
  VI, VII, VIII, X, XII, XV — skipping II, IV, IX, XI, XIII, XIV. It compiles to **306 pages, 0 errors**.
  So the edition and the scan diverge after each curated exposé; each exposé had to be mapped to its
  own printed-page range and the intervening (untranscribed) exposés skipped.

## The method

For every page:

1. **Render** the printed page as 5 overlapping zoom chunks (`_work/chunk_page.py N --chunks 5`).
2. **Read** all chunks *and* the matching `.tex` span.
3. **Compare symbol by symbol** — not just prose, but every subscript, twist, shriek, underline, and
   arrow direction in every display and diagram.
4. **Zoom before any pen-move.** Anything ambiguous is cropped at 600 dpi (`fitz`/PIL scripts to
   `_work/src/zoom/`) and read again *before* deciding. The rule is verify-the-source-first: never
   "correct" toward what the math ought to say until the scan has been read at the glyph level.
5. **Diagrams edge by edge.** Each commutative diagram is checked node-by-node and arrow-by-arrow, not
   glanced at. (193 diagrams, D001–D193, were verified this way.)
6. **Record** every page in `CERT_LOG.md` (a per-page ledger + a live "grind cursor" resume anchor) and
   score the swarm's work on that page in `AGENT_SCORECARD.md`.
7. **Never break the gate.** After any edit, `pdflatex ×2` must still give 306 pp / 0 err. The gate is
   a floor, not a goal: it catches nothing about faithfulness, only that the edition still builds.

### Fix vs. flag

The hardest discipline is deciding when a discrepancy is the edition's fault (fix it) versus the
book's (usually keep it, and note it):

- **Fix** — a wrong symbol in a formula, a dropped display, or a dropped word, where the edition
  departs from a *correct* book. These are transcription errors.
- **Flag, keep faithful** — a genuine error or a coherent notational abuse *in the printed book*.
  The edition reproduces it and the erratum is logged (→ `ERRATA_LNM589.md`), so the reader sees the
  book, not a silent emendation.
- **Silently correct, then disclose** — a genuine one-off typo in the book (a spelling slip, a `∈K`
  for `∈A`) where reproducing it helps no one; the edition prints the right reading and the change is
  disclosed in the errata.

The discriminator that made this tractable: **a genuine typo occurs once and contradicts a sibling
formula; an intended notation recurs coherently.** Getting this wrong in both directions is easy — see
the `f^*v` reversal below.

## What was found

- **480 pages** certified by hand (p435 is a physical duplicate of p434 in the book).
- **52 `.tex` fixes** (+1 cosmetic). Every fix is a wrong-symbol-in-display or a dropped
  word/paragraph — *none* changed the mathematics, which was faithful throughout.
- **162 source-level items**: 114 where the book is correct and the edition matches; 19 book typos the
  edition silently corrected; 29 book errors/abuses kept faithful with an erratum note.
- **193 diagrams** verified edge-by-edge, all content-correct.
- **8/8 QED (`cqfd`) markers** confirmed present in the scan; the one editorially-fabricated marker
  (a `c.q.f.d.` not in the source, Exposé XII p422) was found and removed during the grind.
- **Gate held at 306 pp / 0 err** throughout (307 → 306 once, deliberately, when a spurious
  "Exposé XII (suite et fin)" heading + rule — absent from the book — was removed).

The edition turned out to be a **faithful critical edition already**: the certification mostly
*confirmed* it (error-exclusion) rather than rebuilding it. The contribution is the confidence, plus
the ~52 real fixes the swarm missed and the errata to the printed book.

## The defect taxonomy (what transcription actually gets wrong)

The errors clustered into a few mechanisms, each **invisible to the compiler and to label-checking**,
each caught only by re-deriving types + internal consistency + zoom:

- **Dropped `\underline` on sheaf-Hom/Ext (Exposé I only).** ~25 of Exposé I's fixes were sheaf
  `H̲`/`Ext̲`/`Hom̲` left un-underlined. This was a **transcription-method artifact local to one
  exposé**: from Exposé III on, internal-Hom is routed through a `\uRHom` macro with the underline
  baked in, so the residue never recurs. A method choice, not a systematic blind spot.
- **The spurious `^e` tic (Exposé III B §5).** A base-algebra derived tensor `⊗_A`/`⊗_B` inflated to
  `⊗_{A^e}`/`⊗_{B^e}` where the math forbids it — 4 times, sporadically (three consecutive clean
  squares sat between instances). Caught by re-deriving module types, not pattern-matching: §6.6.1 is
  *saturated* with legitimate `A ⊗^L_{A^e} A` Hochschild tensors and none were false-flagged.
- **Composite-operator garbles (Exposé III B §6).** `i^c c^!` for `i_*^c i^{c!}` — a functor-composition
  shriek scramble. Same class as the `^e` tic: a composite operator, invisible to compile.
- **Systematic module-side swap (Exposé VIII §8).** `_AC ↔ C_A` swapped through an entire definition
  (6 sites) — type-breaking (left⊗right), invisible to compile, caught by re-deriving the tensor's
  side-typing.
- **`A` (crossbar) vs `Λ` (caret) glyph confusion (Exposé X).** The typescript's crossbar-`A`
  (coefficient algebra) and caret-`Λ` (= Z/ℓⁿZ) were mis-read in **both directions** — `Λ→A` and
  `A→Λ` — four times. Resolved by a rule: `A`-module contexts → `A`; pairing subscripts on `Sw` /
  `RΓ` (which are `Λ[G]`-perfect) → `Λ`; each disambiguated by 600 dpi crop.
- **Twist-sign vigilance is uneven, not absent.** The swarm *missed* a dropped codim-`d` minus
  (`⊗d`, p26) but *caught* the identical codim-1 case (`⊗1→⊗−1`, p33). Same error class, opposite
  outcome — so it is page-dependent scrutiny, not a capability gap. This is precisely why a uniform
  by-hand pass is needed: agent recall is page-dependent, not error-type-dependent.

**Defect density tracks display density, not mathematical difficulty.** Exposé III B §3 (dense prose)
took zero fixes; §2 (a display-heavy reformulation with many referenced labels) took six. Where the
page is symbol-dense, transcription slips; where it is argument-dense, it holds.

## Method lessons

- **Verify the source before the pen moves — it repeatedly saved a wrong "fix".** The book's own index
  numbers the last exposé "XIV" while its title page prints "XV"; the instinct was to "correct" the
  index, but reading the book's back-matter first showed the book itself says XIV — so the faithful
  edition keeps both and notes the erratum. Same story at `f^*v` (Exposé III B p199): I "fixed"
  `f^*v → h^*v`, then reverted — `f^*v` is the source's *consistent* base-change abuse, not a typo.
- **The swarm's precision was high, its recall patchy.** Across the graded pages: **0 false positives,
  0 botched fixes** — when it changed something, it was right. But it missed real errors (the
  underlines, the twist parallel-skips, one `SGA→SGAA` parallel-skip). So the swarm is a good *finder*
  and a poor *certifier*; the by-hand pass is where trust is actually manufactured.
- **The compile gate certifies nothing about faithfulness.** Every defect above compiles cleanly. A
  green build and a correct edition are unrelated claims.

## Deliverables and reproducibility

- `sga5_fr_workpass.tex` — the edition (306 pp / 0 err).
- `ERRATA_LNM589.md` — errata to the printed LNM 589, by exposé, each entry `[corrected]` /
  `[faithful]` / `[normalized]`; the 7 substantive mathematical corrections independently re-zoomed.
- `CERT_LOG.md` — the per-page certification ledger.
- `AGENT_SCORECARD.md` — the swarm's page-by-page score.
- `_work/chunk_page.py`, `_work/src/zoom/*.py` — rerunnable rendering/zoom tooling.
- `_work/swarm_results/workpass_vs_repair032.diff` — full diff against the pre-audit baseline.

## Status (read this)

This is a **complete by-hand page-by-page pass** — every page read against the scan, every discrepancy
fixed or flagged — which establishes a base worth trusting. It is **not** a proof of correctness or
completeness. Error rates of ~1 per 2 pages persist even in clean prose, so a second independent pass
would still find things. Treat the edition as a strong, motivated, *provisional* base: better than the
raw scan and better than the swarm output, but a working draft, not a theorem.
