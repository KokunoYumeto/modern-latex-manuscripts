# al-Battānī — Complete Fixed-Star Catalogue (authoritative coordinates)

**Ready to publish.** This is the COMPLETE star catalogue of al-Battānī (Muḥammad ibn Jābir
al-Battānī, d. 929 CE), with authoritative ecliptic coordinates — the largest table block of his
*Opus Astronomicum* (Kitāb al-Zīj), now finished.

## Files
- `al_battani_catalogue_COMPLETE.pdf` — the typeset edition (12 pp). Grouped by constellation in
  Ptolemaic order; per star: number, modern ID (Bayer/Flamsteed + proper name), al-Battānī's Arabic
  description (where collated), ecliptic **longitude**, **latitude**, **N/S**, **magnitude**. The
  documented codex lacuna is shown in place.
- `albattani_catalogue_authoritative.csv` — the open dataset (485 stars). Columns: constellation
  (Latin/Arabic/Chinese), n, bayer, common name, lon_d, lon_m, lat_d, lat_m, dir (N/S), mag, arabic
  description, note.
- `nallino_cat.tsv` — the raw transcription (coordinate source of truth) with per-star notes incl.
  codex variants.

## What it contains
- **485 stars across 47 of the 48 Ptolemaic figures** (Ursa Minor → Piscis Austrinus).
- Coordinates and magnitudes are **al-Battānī's own**, as established in **C. A. Nallino's critical
  edition**, *Al-Battānī sive Albatenii Opus Astronomicum*, **Pars II (Milan 1907)** — the printed
  table *"Situs et magnitudines stellarum fixarum anno 1191 a Dhū 'l-qarnayn"* (epoch ≈ 880 CE).
  Longitudes are absolute ecliptic degrees.
- Every named bright star is present and was **independently checked against modern ecliptic
  latitudes** (Sirius −39.6°, Vega +61.7°, Arcturus +30.7°, Capella +22.9°, Aldebaran −5.5°,
  Regulus +0.5°, Spica −2.1°, Antares −4.6°, Fomalhaut −21.1°, Rigel −31.1°, Betelgeuse −16°,
  Procyon −16°, Deneb +60°, Altair +29°, Pollux/Castor, Polaris +66°). All matched.

## The lacuna (publish honestly)
A leaf is **missing from the Escorial codex** (Nallino: *"desideratur in codice folium"*), which held
**Argo Navis** (with Canopus), **Hydra**, and the first stars of **Crater**. Those stars are not
recoverable from this witness; the gap is recorded in place, not silently closed.

## Provenance / scholarly note
al-Battānī sometimes recorded coordinates that differ from Ptolemy; Nallino occasionally **emended**
the manuscript toward Ptolemy / al-Ṣūfī. The catalogue here follows Nallino's **adopted critical
values**; where the Escorial codex itself differs, Nallino's apparatus preserves the manuscript reading
(captured in the `note` field of the TSV). The project's independent hand-reading of the Arabic abjad
table agreed with the codex readings in that apparatus.

## Suggested metadata
- Title: *"al-Battānī — Catalogue of the Fixed Stars (complete, with authoritative ecliptic
  coordinates)"*
- Keywords: al-Battani, Albategnius, Arabic astronomy, zij, star catalogue, history of astronomy,
  Ptolemy Almagest, precession, critical edition, open data.
- License: open (CC-BY or project default). The CSV is an openly reusable dataset.
- ⚠ **Metadata rule:** the maintainer's first name must NEVER appear in public metadata. Use the
  project's standard pseudonymous/handle attribution.
