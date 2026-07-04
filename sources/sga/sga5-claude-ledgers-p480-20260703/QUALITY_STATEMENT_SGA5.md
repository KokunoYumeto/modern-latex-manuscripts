# SGA 5 — modern LaTeX edition: quality & provenance statement

*Last updated 2026-07-03. Written to accompany the public release so readers understand exactly what level of quality they are getting.*

## What this edition is
A modern LaTeX re-typesetting of **SGA 5** (*Cohomologie ℓ-adique et fonctions L*, Lecture Notes in
Mathematics 589, 1977), covering a curated selection of **10 exposés** (I, III, III B, V, VI, VII, VIII,
X, XII, XV). It compiles to **306 pages, 0 LaTeX errors**.

## How it was verified
A **by-hand** audit, page-by-page, against the printed 1977 scan (LNM 589):
- each page cross-read against the scan at 200 dpi, with **600–1100 dpi crops** for any ambiguous glyph,
  subscript, or accent;
- every check logged in `CERT_LOG.md`; every book-vs-edition difference catalogued in `ERRATA_LNM589.md`;
- a compile gate (306 pp / 0 err) re-run after every change.

No automated "looks-complete" claims are made. The verifier read the pages.

## Error taxonomy — keep these two things separate
Two very different quantities tend to get merged. They are not the same.

**(A) Errors in *this edition* — the `.tex` a reader actually consumes.** These are what affect you.
- Across the most recent ~48 dense cold re-reads: **3 corrections**, of which **1 was mathematically
  substantive** — a wrong subscript case, `ℙ^1_S` → `ℙ^1_s` (the exceptional divisor of a blow-up), where
  even so the surrounding text made the intent unambiguous. The other 2 were fidelity/consistency, not
  mathematics: one redundant clause that was not present in the source, and one functor-subscript
  convention made internally consistent.
- Cumulative over the whole project: **59** edition-side corrections have landed. The large majority are
  transcription / notation / typography; a small minority are mathematically substantive. **None is known
  to break a proof.**

**(B) Errata of the original 1977 book.** The bulk of the catalogue — **~121 entries** — documents typos
*in Grothendieck et al.'s printed text* that this edition already renders correctly: dropped symbols,
stray primes, letter transpositions (e.g. `shcéma`→`schéma`), a summation sign where a direct sum is meant,
capital/lowercase slips, wrong cross-references, etc. These are the **source's** errors, not the edition's.
They are flagged so a reader can reconcile the modern text with the 1977 print.

## Honest caveat — what NOT to over-claim
This is a **carefully-checked working scholarly edition, not a certified-complete one.** Completeness and
accuracy are **not** claimed. Cold re-reading still occasionally surfaces a residual edition slip; the rate
is low (≈ 1 mathematically-substantive edition error per ~48 dense pages in the latest pass, and declining)
but **not zero.**

**Trust level to communicate:** *faithful and carefully checked* — suitable for reading and citation —
but any single symbol on which a proof turns should still be confirmed against the scan (the errata flags
the known book-side ones).

## Companion files
- `sga5_fr_workpass.tex` — the edition source (306 pp).
- `ERRATA_LNM589.md` — book-vs-edition differences (~121 entries, typed by disposition:
  `[corrected]` / `[faithful]` / `[normalized]` / `[non-error]`).
- `CERT_LOG.md` — the running verification ledger.
- `METHOD_AND_LESSONS.md` — method writeup and lessons.
