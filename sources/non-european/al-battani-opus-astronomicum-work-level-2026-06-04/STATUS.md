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

## ★ GEOGRAPHY (T02) — COMPLETE (this session)
The full geographical gazetteer is done — **269 localities with coordinates**:
- `rebuilt/albattani_geography.csv` — open dataset (regions + cities).
- `rebuilt/al_battani_geography_gazetteer.pdf` — typeset edition (6 pp).
- `grind/geo_cat.tsv` — raw transcription. Build: `build_geography.py`.
Two source tables in Nallino Pars II (combined PDF `grind/nallino_pars123.pdf`): the **regional
mid-points** table (94 regions, pp.481–484; 93 transcribed, Britannia → China) and the **city** gazetteer
(*Tabula latitudinum et longitudinum urbium*, pp.485–501; 176 cities, nos. 94–269). Range-validated,
0 anomalies, no numbering gaps. Includes Mecca (with al-Battānī's verified longitude 77°53′), Medina,
Baghdad, Damascus, Alexandria, Rome, Constantinople, Athens, and ar-Raqqa (his own observatory). Shipped
to the push queue (`albattani_geography_gazetteer/`). The earlier Western-Europe province leaf is the same
data, leaf-formatted.

## ★ Parallel push (this session): English descriptions, chronology, zodiac
Ran ~22 agents across two workflows to finish the remainder.
- **Catalogue is now TRILINGUAL.** 8 agents translated the Latin star descriptions (text layer) to English:
  **382/485 stars** now have English + 165 Arabic + all 485 coordinates. Rebuilt
  `al_battani_catalogue_COMPLETE.pdf` and `albattani_catalogue_authoritative.csv` (added `english` column);
  reshipped. Merge script: `enrich_catalogue_english.py`.
- **Chronology (T01): framework + Canon of Kings.** `al_battani_chronology_tables.pdf` — the 8 eras and
  al-Battānī's recension of Ptolemy's Canon (Nabonassar → Umayyad caliphs, Nallino pp.449–454). Caliph
  reign-lengths reliable; ancient regnal figures flagged to collate (the auto-read scrambled the
  regnal/cumulative columns — verified vs p.449). Builder `build_chronology.py`. Shipped to push queue.
- **Zodiac (T03): honest negative.** The terms (bounds) are not tabulated in Nallino's Latin volume and
  the faces are only textual/uncertain — no values-table fabricated. A clean T03 needs the Arabic (Pars III).
- **Arabic-OCR workflow discarded.** 10 agents reading the low-res Arabic scan hallucinated; not used.
See LESSONS_LEARNED Lesson 9 (parallel agents: reliable for translating text, must be verified on numbers
and non-Latin OCR). Remaining if wanted: re-read the Canon's ancient regnal columns from pp.449–454 for
exact figures; source the T03 astrological tables from the Arabic witness.

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
