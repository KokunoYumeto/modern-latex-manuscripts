# al-Battani table reconstruction — lessons learned & reusable workflow

Written for the open-source DOI workflow (repo: `modern-latex-manuscripts`).
Anyone (Codex, future workers) should be able to read this and not re-solve these problems.
Everything here is publishable. Scripts referenced are in `albattani_work\rebuilt\`.

## Lesson 1 — "the tables are unreadable" was a RESOLUTION problem, not a language one
- **Symptom:** coordinate cells illegible; abjad numerals indistinguishable; reconstruction stalled at ~5%.
- **Root cause:** the round-74 and round-83 packages carried CROPPED, downsampled table *plates*.
  Faint abjad numerals lose their distinguishing dots at that resolution. Round-83 had deleted the
  plates entirely to look "clean public", which made it worse than round-74.
- **Fix:** work from the FULL original scan (Nallino 1899, 292 pp), never the derived plates.
  Render the page region with PyMuPDF: `page.get_pixmap(dpi=N, clip=Rect)`. Names readable ~300 dpi;
  numerals need **500–820 dpi** with a tight crop on the number grid, often split into per-column crops.
- **Rule:** never reconstruct tables from a "cleaned/public" package that stripped source plates.
  Always trace back to the highest-resolution original.

## Lesson 2 — longitude abjad encoding (a transcription trap)
- **Symptom:** longitude column looked like small numbers (11, 13, ...), implausible for the constellation.
- **Root cause:** the catalogue gives ABSOLUTE ecliptic longitude 0–360° in COMPOUND abjad
  (e.g. شلد = 300+30+4 = 334°). The three dots of ش (300) wash out and look like س (60); a 3-letter
  value gets misread as a 2-letter one. Confusable skeletons: ب/ت/ث/ن/ي and ج/ح/خ and د/ذ/ر/ز.
- **Fix:** read longitude as a compound 0–360 number; expect monotonic increase within a constellation
  (self-validation). At high dpi re-check the dot patterns. My page-20 longitudes were wrong on this and
  are flagged in the data for re-read.
- **Rule:** establish the numeral ENCODING before transcribing; sanity-check monotonicity and plausible range.

## Lesson 3 — font toolchain on Windows + MiKTeX
- Reader source assumed Noto Serif / Noto Serif CJK SC (absent). Compile failed.
- **Fix:** substitute OS-guaranteed fonts: main = Cambria, CJK = SimSun, Arabic = Amiri (present).
  XeLaTeX + fontspec + polyglossia + xeCJK + bidi.
- **Rule:** pin OS-shipped fonts or vendor fonts into the repo so builds are reproducible.

## The reusable pipeline (data-driven critical edition)
- **Single source of truth:** `star_catalogue.csv` — columns: constellation, const_ar, const_zh, n,
  arabic, roman, lon_d, lon_m, lat_d, lat_m, dir, mag, page, note. Trailing `?` on a cell = doubtful
  reading (becomes a red apparatus flag); empty = not yet read.
- **`build_catalogue.py`** reads the CSV and emits the LaTeX edition grouped by constellation, then
  compiles with XeLaTeX. Re-run after each batch.
- **Why:** the CSV IS the open dataset; the typeset edition is generated, never hand-maintained. Scales
  to the whole catalogue; anyone can re-typeset or reuse the numbers.
- **Standards:** DIN 31635 romanization; Toomer (*Almagest*) / Kunitzsch catalogue layout
  (identification, λ, β, magnitude, N/S); cite by folio + Nallino page; preserve abjad, add decimals.

## Bottleneck and the GPU plan (RTX 4080 SUPER, 16 GB available; torch NOT yet installed)
- Rate-limiter: careful per-cell abjad reading + row-alignment between the name column and the number
  columns. Manual reading has a real error rate on faint minute-cells, and it consumes a lot of context.
- **Standard OCR is unsuitable** (Tesseract/EasyOCR/PaddleOCR are trained on modern Arabic digits/text,
  not abjad numerals in 1899 typeset tables).
- **Planned GPU pipeline:**
  1. `pip install torch` (CUDA build) + a local vision-language model (e.g. Qwen2-VL-7B, fits 16 GB
     quantized).
  2. Auto-segment each table page into per-row / per-cell crops (PyMuPDF + the column x-boundaries).
  3. VLM first-pass read of each cell to CSV, prompted with the abjad system and the absolute-longitude
     convention.
  4. Verify/spot-check against monotonicity and a sample re-read; flag disagreements.
- This offloads the reading from chat context to the card and is the scalable route to the full ~1000-star
  catalogue. Build it as a deliberate step.

## Lesson 4 — local VLMs read Arabic descriptions, NOT abjad numerals
- Tested Qwen2-VL-2B and Qwen2.5-VL-3B on the star-catalogue page (full scan, high-res crops, batched).
- **Speed is fine** once you batch small crops: ~0.8–1.4 s/row, 4.7–11.6 GB VRAM. Full-page input is the
  trap (thousands of vision tokens, ~16 GB, minutes/page) — always crop to rows/cells.
- **Descriptions: good.** 3B read "المقدّم الشمالي من مرَّط الكتّان" correctly. The identification column can be automated.
- **Numbers: failed, both models, both prompt strategies.** Asked to convert abjad→number, it echoed the
  example value from the prompt (334) on every row. Asked to OCR raw letters, it dumped the alphabet.
  This is a training-distribution gap (abjad-as-number in tiny cells), not a size gap — 7B won't fix it reliably.
- **Implication:** numbers need a purpose-built reader — segment cells via the printed column rules (vertical
  dark-pixel projection; inner rules are faint, needs a low threshold) + a small classifier over the ~30 abjad
  glyphs in the 1899 typeface (synthetic training data from period Arabic fonts). Or transcribe manually.
- Scripts: `vlm_read_table.py`, `vlm_batch_test.py`, `vlm_ocr_cells.py`.

## Lesson 5 — the custom abjad classifier is a real ML build, not a quick script
- 361-way whole-number CNN: ~58% synthetic (too many near-identical classes).
- 3-digit-head (hundreds/tens/units) CNN: ~47% synthetic — global average-pooling destroys letter
  POSITION, which the heads need. Fix: keep a position-preserving feature map (flatten spatial), or
  segment per-letter, or use a CRNN+CTC sequence reader.
- **Real-print transfer: 0/7** even on cells I'm certain of. Synthetic Amiri/Noto/Scheherazade →
  1899 Nallino typeface is too big a domain gap. A synthetic-only model will not read the real print.
- Cell segmentation also needs real per-page column-rule detection — fractional x-guesses were off by
  ~0.15 of page width (landed on the descriptions, not the numbers).
- **Conclusion / corrected plan:** the OCR and the manual reading are the SAME effort. Hand-read cells
  ARE the labeled training set. Path: read cells manually (reliable progress now + labels), accumulate a
  few hundred real labeled cells, then fine-tune the classifier on REAL print. Pure synthetic is a dead end.
- Reusable scaffolding (all in `rebuilt/`): `train_abjad_ocr.py`, `ocr_validate.py`, `vlm_read_table.py`,
  `vlm_batch_test.py`, `vlm_ocr_cells.py`. The VLM reliably handles the DESCRIPTION column already.

## Lesson 6 — use existing OCR tools, modular by content type (don't hand-roll)
After the hand-rolled CNN failed, scanned the field. Decision: a modular dispatcher over proven
open-source engines, reusable across every work and script (not just abjad):
- **Math / formulas → LaTeX:** Pix2Text (layout+tables+math+text, 80+ langs incl. Chinese), pix2tex, texify.
- **Historical / trainable scripts (abjad numerals, old Arabic, Sanskrit):** Kraken — TRAINABLE on the
  specific 1899 print using hand-read lines as labels. This is the right replacement for the CNN; existing
  Arabic/Persian/Ottoman/Indic/CJK models exist. (eScriptorium = its labeling GUI.)
- **Modern multilingual print (Chinese, Japanese, Cyrillic, Devanagari):** Surya (90+ scripts) or PaddleOCR-VL (109).
- **Layout/structure:** docling (already cached) or Surya layout.
Architecture: `route(region) -> engine` by content type (math→Pix2Text, historical→Kraken, modern→Surya).
This serves al-Battani abjad now AND the Chinese/Japanese/Sanskrit/math of every other work — modular, OS-tier.
Manual reads still matter: they become Kraken's training labels.

## Lesson 6b — VALIDATED: Pix2Text reads math into LaTeX (existing tool, no reinventing)
Ran Pix2Text (in the isolated OCR venv, device=cpu) on a real Noether invariant-theory page. It captured
the multi-line `aligned` equation systems, symbolic invariant notation, fractions, sub/superscripts, and
the equation tag — clean LaTeX. **Math OCR = solved by an existing OS tool.** Caveat: its CJK text output
was patchy, so route TEXT (Chinese/Japanese/Devanagari) to Surya, not Pix2Text — which is what the modular
dispatcher (`ocr_dispatch.py`) does. ONNX provider note: Pix2Text wants `onnxruntime-gpu` for CUDA; with
plain `onnxruntime` pass `Pix2Text.from_config(device="cpu")`.

## Lesson 7 — isolate heavy OCR/ML tools in their own venv (don't share the working torch env)
Installing surya-ocr + pix2tex + docling into the MAIN env let pip silently replace the working GPU
torch (2.6.0+cu124) with **torch 2.12.0+cpu** — CUDA went False and broke everything mid-run
("DLL load failed importing _C"). Cause: the tools declare an unpinned `torch`, so pip resolves to the
latest CPU wheel and overrides the CUDA build.
**Rule:** each heavy tool stack gets its OWN environment. Here:
- Main env (`miniconda3`): GPU torch 2.6.0+cu124 + transformers — for our own scripts (VLM, training).
- OCR env (`%USERPROFILE%\\ocr_env` or another isolated venv, configured via `OCR_TOOL_PYTHON`): surya/pix2tex/docling + their torch (then force the matching
  CUDA build on top). Invoke via the `OCR_TOOL_PYTHON` environment variable, for example `%USERPROFILE%\\ocr_env\\Scripts\\python.exe` on Windows.
To restore a clobbered torch: `pip install --force-reinstall torch==2.6.0 torchvision==0.21.0 --index-url https://download.pytorch.org/whl/cu124`.

## Lesson 8 — for a numeric table, find the editor's PRINTED table, not just the manuscript scan
The single biggest unlock for the star catalogue. We spent a long time trying to read the **abjad
numerals** off the Arabic manuscript scan (the Escorial codex, ~1068 px in the round-74 embed). Two
problems made that a dead end for full accuracy:
1. **Resolution.** Degree cells were readable; minute cells and confusable letter-pairs (ب/ت/ث/ن,
   ج/ح/خ, د/ذ/ر/ز, ع/غ, س/ش/ص) were marginal at that DPI.
2. **The manuscript ≠ the critical text.** Nallino frequently **emended** the codex toward Ptolemy /
   al-Ṣūfī where it looked corrupt. So the manuscript's own figures (what you read off the abjad) are
   often NOT the scholarly-accepted values — they're a witness, and the apparatus records the variance.

The fix: go to **Nallino Pars II (1907)**, the volume that prints **al-Battānī's tables translated into
Latin with Western-numeral coordinates** and modern (Bayer/Flamsteed) identifications. The star
catalogue is the table *"Situs et magnitudines stellarum fixarum anno 1191 a Dhū 'l-qarnayn"*. One clean
read per page gives longitude, latitude, plaga (N/S), magnitude, and a modern ID — unambiguous. We
transcribed all 485 stars this way (`nallino_cat.tsv`).
- **Where to get it:** Internet Archive, combined item `nallino-al-battini-opus-astronomicium-pars-1-3-1899`
  (the Latin Parts I–II, 1162 pp). The star table is at **PDF pp 592–624**. (The Arabic Pars III,
  `albattnsivealbat03battuoft`, is text-only — it does NOT contain the catalogue table.)
- **Locating a table inside a 1000-page PDF:** scan every page's text layer for constellation names +
  digit density (`fitz` + a keyword/regex score) to bound it, then render candidates. The OCR text layer
  gives clean **Latin descriptions** (reusable) but **scrambles the numbers** — so read numbers visually
  from a hi-DPI crop, pull descriptions from the text layer.
- **Validate, don't trust blindly:** check named bright stars against modern ecliptic latitudes
  (Sirius −39.6°, Vega +61.7°, Arcturus +30.7°, Aldebaran −5.5°, Fomalhaut −21.1°, Rigel −31.1°). If
  those line up, the whole transcription is sound. They did.
- **General rule:** for any historical numeric table that a 19th–20th c. scholar critically edited,
  the editor's printed edition (in the edition's own language, with modern numerals) is a faster and
  MORE authoritative source than re-reading the manuscript — and it carries the apparatus that tells you
  where the manuscript disagrees. Read the manuscript to honour the witness; cite the edition for values.

## Lesson 9 — parallel agents: trust them for TEXT, verify them on NUMBERS and non-Latin OCR
We fanned the remaining work out to ~22 parallel agents (two workflows). The results split cleanly by
task type, and the split is the lesson:
- **Reliable: translating printed Latin.** 8 agents translated the catalogue's Latin star descriptions
  (pulled from the PDF text layer) into English — 382/485 stars, faithful ("the bright star at the end of
  the left foot" = Rigel). Text-layer Latin + LLM translation is trustworthy. This completed the trilingual
  edition.
- **Unreliable: VLM reading low-res non-Latin script.** 10 agents told to transcribe the **Arabic** star
  descriptions from the 1068-px manuscript scan **hallucinated** — generic plausible phrases, Ursa Minor
  appearing on seven different pages, constellation order wrong. Discarded entirely. (Consistent with the
  earlier finding that VLMs read Arabic prose only at higher resolution; at this DPI they confabulate.)
- **Partly unreliable: dense numeric tables.** The "Canon of Kings" agent got the ruler **names, dynastic
  order, and caliph reign-lengths right** but **scrambled the ancient regnal-year columns** (confused the
  "regnal" vs "cumulative" columns) — verified by reading the actual page (p.449). The terms/eras agents
  similarly mixed real reading with textbook values.
**Rules:** (1) Use parallel agents to translate/normalise TEXT you already have — reliable and fast.
(2) For VALUES (coordinates, regnal years) and for OCR of non-Latin/low-res script, treat agent output as
a *draft to verify*, not data — spot-check against the page; a wrong number is worse than a missing one.
(3) Build adversarial verification in (we caught the faces table contradicting its own cited quote, and the
king-numbers contradicting p.449). (4) Honest negative results are findings: the zodiac terms simply are
not tabulated in Nallino's Latin volume — record that rather than fabricate a table.

## Where everything lives
- Workspace: a local al-Battani working directory, preferably configured as `ALBATTANI_WORK` and kept out of git.
- Full source scan: `albattani_work\source_scan\nallino_1899_albattanisivealb00batt.pdf`
- Data + build + editions: `albattani_work\rebuilt\` (`star_catalogue.csv`, `build_catalogue.py`,
  `al_battani_star_catalogue_EDITION.pdf`, plus the geography leaf and the Pisces/Cetus page)
- Progress log: `albattani_work\STATUS.md`
- Open-source destination: this repository.

