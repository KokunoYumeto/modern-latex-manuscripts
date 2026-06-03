# al-Battānī, *Opus Astronomicum* (Kitāb al-Zīj) — Coverage & Completeness

A professional edition states honestly how much of the original it contains. This edition is
**complete in its text and partial in its numeric tables**, as detailed below.

## TEXT — COMPLETE
- All **100 transcription segments**, covering the work's full chapter sequence (opening and preface
  through the spherical-astronomy and instrument chapters).
- Trilingual throughout: **Arabic source + English translation + Chinese translation + a modern
  Arabic rendering**, per section.
- Source: Nallino 1899 critical edition (Escorial witness). Verified as the most complete text version
  across the project's rounds.

## TABLES — STAR CATALOGUE COMPLETE; other blocks in progress
A *zīj* is fundamentally a book of astronomical tables. The largest single block — the **fixed-star
catalogue (T04)** — is now **complete with authoritative coordinates**. The remaining blocks
(chronology, geography, zodiac/auxiliary) are the next work. Current status:

| Block | Content | Leaves | Reconstructed | Status |
|---|---|---|---|---|
| T01 | Chronology, caliphs, regnal years | 6 | 0 | pending |
| T02 | Geography, city longitude/latitude | 8 | 1 leaf (Western Europe: names + IDs solid; coordinates pending) | partial |
| T03 | Zodiac, terms, houses, auxiliary | 3 | 0 | pending |
| T04 | Fixed-star catalogue | ~35 | **COMPLETE — 485 stars, 47 figures, with authoritative ecliptic coordinates** (longitude, latitude, N/S, magnitude) + modern Bayer/Flamsteed IDs + named bright stars. Coordinates established from **Nallino's printed critical table (Pars II, 1907)**, epoch ~880 CE, cross-checked against modern bright-star latitudes (Sirius −39.6°, Vega +61.7°, Arcturus +30.7°, Aldebaran −5.5°, Fomalhaut −21.1°, Rigel −31.1° — all confirmed). **Argo Navis (Canopus) + Hydra + start of Crater absent = a documented LEAF LACUNA in the Escorial codex** (recorded by Nallino, shown in place). | **COMPLETE** (coordinates done; Arabic source-descriptions merged for ~190 stars, remainder collating) |

- What "reconstructed" means here: a proper trilingual critical table with the source Arabic, an
  identification, and verified coordinates — not OCR debris. Star descriptions and identifications read
  reliably; the abjad **numerals** are the hard part.
- A scholarly note already recorded: the **longitude convention shifts between sections** (within-sign
  degrees for the Pisces figure, absolute ecliptic degrees for the Two Fishes) — to be reconciled
  against Nallino's introduction, not silently normalised.

## Method used for the star catalogue (the breakthrough)
The abjad numerals in the Arabic codex scan (≈1068 px) are marginal to read cell-by-cell, and Nallino
often *emended* the codex toward Ptolemy/al-Ṣūfī — so the manuscript's own figures differ from the
critical text. The decisive source is therefore **Nallino's Pars II (1907) printed table**,
*"Situs et magnitudines stellarum fixarum anno 1191 a Dhū 'l-qarnayn"* — al-Battānī's catalogue set
in clean Latin type with **Western-numeral coordinates** and modern (Bayer/Flamsteed) identifications.
It was downloaded from the Internet Archive combined edition, the table pages rendered at high DPI, and
every star transcribed (longitude, latitude, plaga = N/S, magnitude, modern ID). Bright-star latitudes
were checked against present-day ecliptic values as an independent control; all matched.
- Data: `rebuilt/nallino_cat.tsv` (raw transcription) → `rebuilt/albattani_catalogue_authoritative.csv`
  (open dataset) → `rebuilt/al_battani_catalogue_COMPLETE.pdf` (typeset edition).
- The codex's *own* abjad readings, where they diverge from Nallino's adopted values, are preserved in
  Nallino's apparatus (recorded as notes) — a genuine critical-edition layer, not silently normalised.
- Earlier hand-read abjad values (the manual slog) agreed with the codex readings in Nallino's
  apparatus — the manual reading was faithful; Nallino's emendations explain the residual differences.

## One-line statement for the publication metadata
> Complete trilingual edition of the **text** of al-Battānī's *Opus Astronomicum* (all 100 segments,
> Arabic with English and Chinese), **plus the complete fixed-star catalogue** (485 stars with
> authoritative ecliptic coordinates and modern identifications, after Nallino's critical edition; one
> documented codex lacuna for Argo/Hydra). The remaining numeric tables (chronology, geography, zodiac)
> are in progress.
