# Eisenstein Source Packet

Date: 2026-06-29

Local packet root:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\source intake priority authors 20260629\Eisenstein\Eisenstein_SOURCE_PACKET_20260629`

Upload ZIP folder:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\source intake priority authors 20260629\Eisenstein\Eisenstein_SOURCE_PACKET_20260629\01_UPLOAD_THESE_ZIPS`

## Purpose

Compact source-intake packet for Gotthold Eisenstein's `Mathematische Abhandlungen, besonders aus dem Gebiete der hoeheren Arithmetik und der elliptischen Funktionen`.

This is source intake and web/colleague handoff material. It is not a finished transcription, translation, source-checked edition, or critical edition.

## Upload Order

| Order | ZIP | Size | SHA256 |
|---:|---|---:|---|
| 1 | `Eisenstein_CONTROL_START_HERE_20260629.zip` | 5,593 bytes / 0.01 MB | `73788250310D8DF956A1BC491ABD2CACD188993FC3052EFF1D5D2DC37A1E3534` |
| 2 | `Eisenstein_01_CANONICAL_UOFT_RAW_SOURCE_20260629.zip` | 301,906,822 bytes / 287.92 MB | `B4FABC68353CF1BE8C08C94043997A7D149D95A2F24097206497E7C7E427ED2F` |
| 3 | `Eisenstein_02_COMPARATOR_PDFS_20260629.zip` | 326,304,714 bytes / 311.19 MB | `C453B64675BB987EBB239B54C5D23DBACDA79EB50609043331D46A6974A2DA28` |
| 4 | `Eisenstein_03_BSB_GOOGLE_JP2_OCR_COMPARATORS_20260629.zip` | 311,427,075 bytes / 297.00 MB | `2F66CE8F2A253531F9B41D31583616C95C284AACBD5199946C18D7DB4E68628E` |

All four upload ZIPs are below 500 MB and were ZIP-tested locally.

## Canonical Source Choice

Primary source witness:

- `mathematischeabh00eiseuoft.pdf`, 354 pages.
- `mathematischeabh00eiseuoft_raw_jp2.zip`.
- UofT ABBYY, DjVu text, and metadata sidecars.

Reason: the UofT witness is the only local Eisenstein source with a true raw JP2 archive. A sampled raw page has geometry `5010 x 3336`; the embedded `72` resolution metadata should not be treated as optical scan DPI.

## Comparator Witnesses

| Witness | Pages | Local role | Source-quality note |
|---|---:|---|---|
| BSB `10053424bsb` | 355 | Comparator PDF/JP2/text/metadata/scandata | Large image PDF plus processed JP2; local title metadata may be unreliable, so inspect the source itself. |
| Google/IA `bub_gb_NXBtAAAAMAAJ` | 348 | Comparator PDF/JP2/ABBYY/DjVu/metadata/scandata | Compact comparator and OCR control. |
| UofT processed JP2 | 354 | Optional local-only image layer | Not primary because the raw JP2 archive is better. |

## Recommended Task

Produce a modern LaTeX transcription from the UofT raw source witness. Use comparator PDFs/JP2/OCR only to resolve unclear readings or page/order disagreements.

Do not promote OCR or existing text without checking formulas and notation against source images. Flag ambiguous symbols, unusual formula layout, and witness disagreements in an audit note.

## Quality Rule

Distinguish raw JP2/source image, processed JP2/PDF image, OCR text, and promoted TeX. OCR is a locator/control witness only; promoted TeX must be source-compared.
