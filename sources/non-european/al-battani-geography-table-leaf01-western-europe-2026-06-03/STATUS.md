# al-Battani work — Claude's mirror and progress

Floris assigned Claude BOTH the segment professionalization AND the table
reconstruction. This is my own working mirror; I do not edit the originals.

## Workspace (mirrored 2026-06-03)
- `current_head_round83/` — round 83 canonical reference (the current best text).
- `source_plates_round74/` — round 74 table plates + register (53 source-scan leaves;
  round 83 had dropped these).
- `source_scan/` — the full Nallino 1899 scan (292 pp). Highest-quality source.
- `segment_sources/` — latest editable TeX for segments 1–90 (gathered from rounds 50–66).
- `rebuilt/` — my output.

## Table structure (mapped from the plates)
- T00: completion / correction note (1 leaf)
- T01: chronology, caliphs, regnal tables (6 leaves)
- T02: geography, city coordinates (8 leaves)
- T03: zodiac, terms, houses, auxiliary (3 leaves)
- T04: fixed-star catalogue (35 leaves)

Reconstruction status before me: ~2–7% (per leaf, 65–97 source rows, 0–7 curated).

## Reading the source: solved
The round-74 plates were too low-resolution to read numerals. The full Nallino scan in
`source_scan/` is sharp at 500–820 dpi: names and abjad coordinates both legible. All
reconstruction now works from the full scan, page by page, with each numeric cell magnified.

## ★ STAR CATALOGUE (T04) — COMPLETE (this session)
The whole fixed-star catalogue is now done with **authoritative coordinates**:
- `rebuilt/albattani_catalogue_authoritative.csv` — **485 stars, 47 figures**, ecliptic
  longitude+latitude+N/S+magnitude + modern Bayer/Flamsteed ID + Arabic description (where collated).
- `rebuilt/al_battani_catalogue_COMPLETE.pdf` — the typeset edition (12 pp), lacuna shown in place.
- `rebuilt/nallino_cat.tsv` — raw transcription + codex variants. Build: `build_authoritative_*.py`.

**How (the breakthrough):** the Arabic abjad scan (~1068 px) is marginal for minute-cells, and Nallino
emended the codex toward Ptolemy — so the manuscript's figures differ from the critical text. The
decisive source is **Nallino Pars II (1907)**, his printed Latin table *"Situs et magnitudines stellarum
fixarum anno 1191 a Dhū 'l-qarnayn"* (epoch ≈880 CE): al-Battānī's catalogue in clean type with
Western-numeral coordinates + modern IDs. Downloaded the IA combined edition, found the table at PDF pp
592–624, rendered hi-DPI, transcribed every star. Bright-star latitudes checked vs modern values — all
matched (Sirius −39.6, Vega +61.7, Arcturus +30.7, Aldebaran −5.5, Fomalhaut −21.1, Rigel −31.1, …).
**Lacuna confirmed by Nallino himself** ("desideratur in codice folium"): Argo Navis + Hydra + Crater-
start. Shipped to the push queue (`albattani_star_catalogue_COMPLETE/`).

Earlier this session, before finding Pars II: hand-read ~80 stars' abjad coordinates from the scan,
anchoring bright stars — those agreed with the codex readings in Nallino's apparatus (the manual slog
was faithful; Nallino's emendations explain the residual differences).

## Earlier validated templates
- `rebuilt/al_battani_geo_T02_leaf01_western_europe.tex` (+ .pdf). First geographical leaf (T02).
- `rebuilt/al_battani_stars_pisces_p20.tex` (+ .pdf). Early single-page catalogue template.

## Progress vs whole
T04 star catalogue (the largest block) is **COMPLETE**. Remaining table blocks: geography (T02, 8
leaves; 1 drafted), chronology (T01, 6), zodiac/auxiliary (T03, 3). Plus segment leveling 43–100.

## Next target located: geography table (T02)
The geography table is **already located in Nallino Pars II** (same combined PDF, `grind/nallino_pars123.pdf`):
- **Pages ~481–501**, header *"Tabula latitudinum et longitudinum urbium, iuxta quod reperitur in Libro
  Figurae [Terrae] et quod etiam probatum est"* — a **CITY** gazetteer (~270 localities) in two side-by-side
  sub-tables per page: Nomina urbium | Longit. | Latitudo. Western-numeral coordinates, with rich Latin
  footnotes identifying each place (Lelewel/Ptolemy cross-refs). Same transcription method as the catalogue.
- **Reconciliation needed:** the existing drafted leaf `al_battani_geo_T02_leaf01_western_europe.tex` lists
  Ptolemaic **provinces** (Britannia, Hispania Baetica, Gallia…), whereas Nallino's table lists **cities**.
  Decide whether to (a) rebuild T02 as the full city gazetteer from Nallino (recommended — authoritative,
  complete, parallels the catalogue), keeping the province leaf as a separate "regional overview", or
  (b) match provinces to representative cities. Recommend (a).
- After geography: chronology (T01) and zodiac (T03) tables are likewise in Pars II — locate by the same
  page-text keyword+digit-density scan.

## Method (per leaf)
1. Render the leaf from the full Nallino scan at high DPI.
2. Transcribe the Arabic as printed (diplomatic).
3. Identify each entry (Ptolemaic province / modern name / Chinese).
4. Read the abjad numerals cell by cell; cross-check against Nallino's edition.
5. Build a trilingual longtable; flag every uncertain cell.

## Remaining
- Tables: 8 geo + 6 chronology + 3 zodiac + 35 star leaves, coordinates and all.
- Segments: level up 43–100 to the rich format of 1–5; recover source for 91–100.
This is a large grind. It is now started and will proceed leaf by leaf and segment by segment.
