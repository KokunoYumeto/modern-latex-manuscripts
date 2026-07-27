# Claude's page-by-page cold-reverify method (diagrams + text) — durable reference

Date: 2026-07-28
Author: Claude (Opus). Written at Floris's request so Codex, future Claude
instances, and other AIs can reproduce the method exactly.

Scope: verifying that a modern-LaTeX transcription of a scanned typewritten
source (SGA6 workpass, and by extension SGA3/EGA) reproduces the scan
**symbol-for-symbol, source-complete**. This is a FIX task, not a math audit:
the goal is fidelity to the author's page, including the author's own typos.

---

## 0. Core principle: the IMAGE decides, never `get_text`

`page.get_text()` (PyMuPDF text layer) on these scans is **unusable for any
verification decision**. It silently:
- garbles all math, subscripts/superscripts, and every tikzcd/diagram;
- auto-corrects source typos, accents, and letter case;
- lies on terminal punctuation (renders a source period as a comma and vice
  versa) and on running-header/page-number glyphs.

Use `get_text` for exactly ONE thing: a cheap cross-check of the page-number
and folio mapping (and even there, confirm against the rendered band). Every
content decision — every word, sign, subscript, arrow, label, and punctuation
mark — is made **on the rendered image**, and any ambiguous glyph is decided
on a **targeted high-zoom crop**, not the full-page render.

---

## 1. Page/folio mapping discipline (do this first, every page)

Establish and then re-confirm on every page the three independent coordinates:
- **top printed number** (e.g. `- 18 -`),
- **running header** (exposé numeral, e.g. `XIII`),
- **bottom folio** (e.g. `633`).

Express each as an offset from the PDF 0-based page index and verify all three
every page. Example (SGA6 Exposé XIII): `top = idx − 628`, `RH = "XIII"`,
`footer = idx − 13`. If any of the three disagrees with the expected offset,
STOP and resolve before verifying content — a mapping slip means you are
comparing the wrong source page to the .tex.

---

## 2. Render pipeline (full page → 5 horizontal bands)

Per page, one Python/PyMuPDF (`fitz`) + Pillow script renders 5 overlapping
horizontal bands so text is large enough to read letterforms:

```
bands = [("top",0.015,0.115),("a",0.135,0.335),("b",0.335,0.535),
         ("c",0.535,0.735),("d",0.735,0.985)]
# per band: clip = Rect(0.03*W, fy0*H, 0.98*W, fy1*H)
# pixmap at matrix 2400/72  (~2400 dpi)
# grayscale → ImageOps.autocontrast(cutoff=1)
#           → Contrast x1.9 → Sharpness x1.6
```

Notes:
- The small gaps between bands (e.g. 0.115–0.135) are intentional overlap slack
  but occasionally a text line falls IN a gap. If a line you need isn't in any
  band, re-crop that fractional-y range directly (do not assume it's absent).
- The bottom band ("d") on these scans is frequently a **degraded blotch**
  (ink bleed / low contrast at the page foot). Diagrams and folios there almost
  always require a dedicated zoom (see §4).
- Rendering a page can be slow. Use a generous shell timeout (300000 ms) so the
  call is not involuntarily backgrounded mid-raster.

---

## 3. Reading order per page

1. Glance the shared inbox for any new candidate/coordination file.
2. RE-READ the live .tex for the line range covering this page **before** any
   edit decision (never edit from memory).
3. Render the 5 bands + get_text.
4. Confirm the 3-coordinate mapping (§1).
5. Read every band; compare each token to the .tex line-by-line.
6. Zoom every ambiguous glyph and every diagram (§4).
7. Decide each candidate (§5), edit only if warranted, gate only after an edit
   (§6), then log (§7).

---

## 4. Targeted high-zoom (the heart of diagram verification)

For any ambiguous glyph, and for **every** non-trivial diagram, render a
dedicated crop from the PDF (not an upscale of the band):

- fractional-x/y clip around the target only;
- matrix **6500–9000 dpi** for glyph/label/arrow/punctuation detail
  (single characters can go to 9000; a wide row use 6500);
- `autocontrast(cutoff=1..2)` → Contrast x2.4–2.8 → Sharpness x1.8–1.9.

**Decompression-bomb cap:** Pillow refuses images above ~178 M pixels. A wide
crop at 11000 dpi trips this. Mitigate with, at the top of the script,
`Image.MAX_IMAGE_PIXELS = None`, AND keep dpi ≤ 6500 for wide crops (narrow the
x/y range instead of raising dpi when you can).

### tikzcd / commutative diagrams — edge-by-edge

Verify the diagram as a graph, checking every element against the .tex source:
- **each node**: symbol, every subscript/superscript, primes, underline/font
  (e.g. `\underline{\Pic}` vs plain `Pic`), exact index letters (`Y/S` vs
  `X/S`, `i` vs `j`);
- **each arrow**: presence, direction (`[r]` right, `[u]` up, etc.), and
  whether it is bare or **labelled** — and the label text/position if any;
- **layout**: which nodes are top vs bottom row, which arrows are horizontal vs
  vertical, that no node/arrow is dropped or added.

A "the diagram looks right" glance is NOT a pass. On a degraded page the arrow
direction and a dropped label are exactly what a low-res view hides. One zoom
per row (and per label cluster) minimum; more for a commutative square.

---

## 5. Decision categories (bidirectional: source-vs-Codex)

For each discrepancy, first decide WHO deviated, by zoom:

**A. Codex deviated from a faithful-able source → FIX inline.** Only these:
- sentence/terminal punctuation dropped or changed by Codex;
- a parenthesis, word, comma dropped OR added by Codex;
- condensation/paraphrase of source prose;
- a tikzcd node/arrow/label/direction, or a display term/index/sign,
  **changed or dropped** by Codex (confirmed on zoom);
- a math/EGA/FGA/SGA reference number changed by Codex.

**B. Source coquille (author typo) → reproduce faithfully, catalogue, RAS.**
The transcription must keep the author's own errors. Log it with an ID and the
line, but do NOT "correct" it. (Verify it IS in the source by zoom — do not
assume.) Bidirectional means also catching Codex silently OVER-correcting a
source typo: if the source has the typo and the .tex "fixed" it, restore the
typo.

**C. Mechanical typography → NOTATION-BATCH, RAS inline.** Font/notation choices
that are systematic and deferred to a single later pass: underline→\emph on
statements/footnotes, `\mathcal O` underline, script-L vs cal-L, `\underline
\Pic`, thin-space/`~`, guillemets vs straight quotes, dash style, display-inline
→ display, equation-tag position (source left-margin vs amsmath right), «N°» vs
«no», f.p.p.f. spelling, enumerate label style, diagram trailing punctuation.

**D. Display-introducing colon → separate RESTORE-BATCH.** Tracked apart from C.

Golden rule: when unsure whether a discrepancy is Codex (A) or source (B),
**zoom until certain**; default to NOT editing if it cannot be confirmed as
Codex-introduced.

---

## 6. Compile gate

Hard gate = `pdflatex` twice, 0 errors, expected page count. **Recompile ONLY
after a real .tex edit.** If a page is 0-FIX (the overwhelmingly common case
when the transcription is good), do NOT recompile; record the frozen output
byte-size as proof the file is untouched.

---

## 7. Logging (CERT) + anti-corruption

One CERT entry per page in a newest-first log, each anchored at a fixed line.
The entry records: mapping confirmation, per-element CONFORME/FIX findings, any
new source coquille (with ID + line), the VIGILANCE result (did Codex ADD
anything?), the gate result/byte-size, and the exact boundary (where this page
ends and the next begins) so the next page resumes precisely.

**Anti-corruption pattern for prepending a new entry above the previous one:**
the edit's `old_string` is the previous entry's complete header line (unique);
the `new_string` is the new block + blank line + that SAME previous header line
re-appended verbatim and complete. Then grep the header anchors to confirm the
newest-first order is intact and nothing was truncated. (Past corruption came
from a `new_string` that did not re-append the full prior header.)

---

## 8. Practical guardrails

- One page at a time, foreground, by hand. No background jobs, no parallel
  agents for the verification itself.
- Contact sheets / whole-page thumbnails are navigation aids only — they can
  never carry a PASS. A PASS is earned band-by-band + zoom.
- Never claim "complete" or "certified": every finding is provisional. Re-verify
  prior pages when a new failure pattern is discovered.
- Keep new diagram-failure patterns flowing into the shared inbox so the method
  keeps improving.
