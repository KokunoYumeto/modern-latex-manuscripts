# SGA5 audit — source file & resolution decision (2026-06-24)

## Which source, and is anything higher-res?

Measured native embedded-image resolution of every SGA5 file on disk:

| file (C:\Users\Floris\Documents\Papors\OS\) | pages | native px/page | notes |
|---|---|---|---|
| **SGA5 (1).pdf** | 496 | **2176×3035** | Springer LNM 589, COMPLETE: title, copyright, editor intro, TABLE DES MATIÈRES, index. **CHOSEN canonical source.** |
| Théorie des topos…SGA5.pdf | 496 | 2176×3035 | byte-for-pixel same scan as above (duplicate, 59.2 MB) |
| SGA5.pdf | 496 | 2176×3035 | same scan; only the PDF page-box is smaller, so a naive "dpi" reads ~370 instead of ~256 — **same pixels**, no extra detail |
| SGA5.ps | 496 | (same scan) | PostScript print-stream made by Acrobat 6.0 in 2004 from "opr02KFL.pdf"; monochrome; not higher-res |
| SGA5.djvu | ~480 | (unknown) | only 3.9 MB total ⇒ heavily compressed, almost certainly LOW-res; no ddjvu/djvused installed to confirm |

**Conclusion:** the ceiling is **2176×3035 px ≈ 360 dpi optical**, and it is the SAME across
every copy. There is **no higher-resolution version on disk**. The 484-page scan used by the
old repair stream is the same 2176×3035 scan, just stripped of front matter.

### Online search for a higher-res scan (2026-06-24) — NONE EXISTS
Searched archive.org, the Grothendieck Circle, and the general web:
- **Internet Archive** `cohomologieladiq0000unse` IS SGA 5, but scanned at **360 dpi**
  (Sony A6300, 514 pp) — same resolution as our files — and it is borrow-only (no download).
- **"SGA on the web"** (Calegari / Borger / Stein, the standard free SGA scans) **does NOT
  include SGA 5** at all — the Melbourne library they photocopied from didn't have it. So the
  famous mirror skips SGA 5; our scan came from a different 360 dpi source (the PS is from a
  2004 Acrobat file "opr02KFL.pdf").
- **No retyped / born-digital SGA 5.** SGA 1 and SGA 2 were re-typeset by volunteers
  (arXiv math/0206203 is the typeset SGA 1; SMF redid SGA 2). SGA 5 never got that treatment —
  which is exactly why THIS project (a clean LaTeX SGA 5) is worth doing.
- No 600 dpi scan found anywhere.

**Bottom line: 360 dpi (2176×3035 px) is the highest-resolution SGA 5 that exists publicly, and
we already have it.** The file we're using is as good as it gets. The only upgrade path is a
fresh physical scan at 600 dpi (would need the physical book); worth it someday for the
diagram-dense exposés (III, III B, XII, XV) to kill typewriter prime/tilde/shriek ambiguity,
but not blocking and not currently obtainable.

## Resolution standard for this audit (the "650–1000 dpi" rule)
- We CANNOT add detail ("no enhance button"). But enlarging the native pixels makes small marks
  legible, which is the whole game for typewriter primes/subscripts/iso-tildes.
- **Standard:** render witness CROPS at **1000 dpi**, full-page overviews at **650 dpi**.
  Never render below native ("350 dpi is trash" — it throws away real pixels).
- Understand what these numbers mean: 650–1000 dpi here = legibility ENLARGEMENT of the
  ~360 dpi native scan, NOT true optical resolution. Read marks accordingly; when a prime/tilde
  is genuinely unresolvable at native, say so rather than guessing.

## Canonical source + page mapping (USE THIS GOING FORWARD)
- Source = `C:\Users\Floris\Documents\Papors\OS\SGA5 (1).pdf` (Springer LNM 589, complete).
- **Printed page = PDF page − 12.** (PDF p13 = printed p1, verified; identical image to the old
  484-scan p1, so all prior reads/fixes against the 484-scan remain valid — same pixels.)
- Exposé → printed-page ranges (from the book's Table des Matières):
  - I  Complexes dualisants (Grothendieck/Illusie): **1–72**
  - III  Formule de Lefschetz (Grothendieck/Illusie): **73–137**
  - III B  Calculs de termes locaux (Illusie): **138–203**
  - V  Systèmes projectifs J-adiques (Jouanolou): **204–250**
  - VI  Cohomologie ℓ-adique (Jouanolou): **251–281**
  - VII  Cohomologie de schémas classiques / classes de Chern (Jouanolou): **282–350**
  - VIII  Groupes de classes…complexes parfaits (Grothendieck/Bucur): **351–371**
  - X  Formule d'Euler–Poincaré (Grothendieck/Bucur): **372–406**
  - XII  Nielsen–Wecken / Lefschetz (Grothendieck/Bucur): **407–441**
  - XIV = XV  Morphisme de Frobenius / fonctions L (Houzel): **442–480**
  - Index terminologique 481 ; Index des notations 483
  - Exposés **II, IV, IX, XI, XIII do not exist** (book footnote; II dropped, III rewritten + III B added).
