# Eisenstein / Galois / Steiner Source-Intake Audit, 2026-07-06

This manifest records a local source-intake audit for three possible continuation lanes. These are not reader releases, transcriptions, translations, source-audited editions, DOI publication claims, or critical editions.

## Local Root

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\source intake priority authors 20260629`

## Summary

| Author | Best first source | Pages checked | Handoff status | Public status |
|---|---|---:|---|---|
| Eisenstein | UofT raw JP2/PDF witness for `Mathematische Abhandlungen` | 354 | Four upload ZIPs present; CRC OK; SHA256 manifest matches | Source intake only |
| Galois | 1897 printed `Oeuvres mathematiques` IA scan, checked against 1846 JMPA and optional 1908 manuscripts | 96 main / 65 comparator / 77 manuscript | One compact source packet ZIP present; CRC OK | Source intake only, quick-win candidate |
| Steiner | Vol. I MBP/Pittsburgh 600 ppi witness; Vol. II Google witness; BSB Vol. I JP2 comparator | 631 / 808 / 633 comparator | Four upload ZIPs present; CRC OK; SHA256 manifest matches | Source intake only |

## Eisenstein

Canonical local source:

- `Eisenstein\Eisenstein_SOURCE_PACKET_20260629\01_CANONICAL_UOFT_RAW_SOURCE\mathematischeabh00eiseuoft.pdf`, 354 pages.
- `Eisenstein\Eisenstein_SOURCE_PACKET_20260629\01_CANONICAL_UOFT_RAW_SOURCE\mathematischeabh00eiseuoft_raw_jp2.zip`.

Comparator/localizer material:

- `10053424bsb.pdf`, 355 pages.
- `bub_gb_NXBtAAAAMAAJ.pdf`, 348 pages.
- BSB/Google JP2/OCR sidecars.

Recommended handoff order:

1. `Eisenstein_CONTROL_START_HERE_20260629.zip`
2. `Eisenstein_01_CANONICAL_UOFT_RAW_SOURCE_20260629.zip`
3. `Eisenstein_02_COMPARATOR_PDFS_20260629.zip`
4. `Eisenstein_03_BSB_GOOGLE_JP2_OCR_COMPARATORS_20260629.zip`

Rule: promote TeX only after formulas and notation are checked against the UofT raw source witness; OCR is locator/control text.

## Galois

Best quick-win source:

- `Galois\Galois_QUICK_WIN_SOURCE_PACKET_20260629\01_1897_collected_scan_IA\uvresmathmatiqu00frangoog.pdf`, 96 pages.

Supporting witnesses:

- `Galois_1846_JMPA_Oeuvres_mathematiques_Numdam.pdf`, 65 pages.
- `Galois_1908_Manuscrits_IA.pdf`, 77 pages.
- `gutenberg_40213_1897_oeuvres.tex`, convenience/control only.

Compact handoff:

- `Galois\Galois_SOURCE_PACKET_20260629.zip`, 71.29 MB, 25 members, CRC OK, SHA256 `77DA4AC0B368A79E1F323C276E881FF12CBBEE3DA695522CFF48D6681E40E4A1`.

Rule: this is the easiest of the three to start because the main printed corpus is under 100 scanned pages and already has a TeX control layer.

## Steiner

Primary local sources:

- Volume I: `Steiner\Steiner_SOURCE_PACKET_20260629\01_VOLUME_I_PRIMARY_600PDF_MBP\jacobsteinersges027694mbp.pdf`, 631 pages.
- Volume II: `Steiner\Steiner_SOURCE_PACKET_20260629\03_VOLUME_II_GOOGLE_SOURCE\jacobsteinersge01steigoog.pdf`, 808 pages.

Comparator:

- Volume I BSB: `Steiner\Steiner_SOURCE_PACKET_20260629\02_VOLUME_I_BSB_JP2_COMPARATOR\11740034bsb.pdf`, 633 pages.

Recommended handoff order:

1. `Steiner_CONTROL_START_HERE_20260629.zip`
2. `Steiner_01_VOL1_PRIMARY_600PDF_MBP_20260629.zip`
3. `Steiner_02_VOL1_BSB_JP2_COMPARATOR_20260629.zip`
4. `Steiner_03_VOL2_GOOGLE_SOURCE_20260629.zip`

Rule: Steiner is not a quick win. It is a large geometry lane with figure/diagram pressure; diagrams and plate references must be audited visually.

## Validation Performed

- PDF page counts checked with bundled Python/PyPDF.
- Upload ZIP CRC tests passed for all Eisenstein, Galois, and Steiner handoff ZIPs.
- Eisenstein and Steiner SHA256 upload manifests match local files.
- No source packet is promoted as a reader or edition.
