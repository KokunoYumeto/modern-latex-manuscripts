# Steiner Source Packet

Date: 2026-06-29

Local packet root:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\source intake priority authors 20260629\Steiner\Steiner_SOURCE_PACKET_20260629`

Upload ZIP folder:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\source intake priority authors 20260629\Steiner\Steiner_SOURCE_PACKET_20260629\01_UPLOAD_THESE_ZIPS`

## Purpose

Source-intake packet for Jakob Steiner's `Gesammelte Werke`, edited by K. Weierstrass.

This is source intake and web/colleague handoff material. It is not a finished transcription, translation, source-checked edition, or critical edition.

## Upload Order

| Order | ZIP | Size | SHA256 |
|---:|---|---:|---|
| 1 | `Steiner_CONTROL_START_HERE_20260629.zip` | 5,113 bytes / 0.00 MB | `56B3296B4FAB03E970885990502E946EA00CEE2E5EA626B443879C7D4476163E` |
| 2 | `Steiner_01_VOL1_PRIMARY_600PDF_MBP_20260629.zip` | 69,085,461 bytes / 65.89 MB | `D3928712A2F61F2123440C36CD7C4F706F38E41B5312C869721A1DD86E5139DF` |
| 3 | `Steiner_02_VOL1_BSB_JP2_COMPARATOR_20260629.zip` | 465,408,842 bytes / 443.85 MB | `3E464B0F838796FBE9F38ED66142B0FF3CE9081F76E61B2CBAD5D769B8B9B79B` |
| 4 | `Steiner_03_VOL2_GOOGLE_SOURCE_20260629.zip` | 67,748,677 bytes / 64.61 MB | `08899B07FA6BE0B7382EE6957E8033D725A8E7692AD375DA2AF48349BE57F7A3` |

All four upload ZIPs are below 500 MB and were ZIP-tested locally.

## Source Selection

| Witness | Role | Volume | Pages | Source-quality note |
|---|---|---:|---:|---|
| `jacobsteinersges027694mbp` | Primary source | I | 631 | PDF with scandata reporting 600 ppi; cleanest local Volume I witness found in this intake pass. |
| `11740034bsb` | Comparator source | I | 633 | Large image PDF plus JP2 comparator, OCR text, metadata, scandata, and text PDF. Metadata reports 72 ppi, which should be treated cautiously rather than as optical truth. |
| `jacobsteinersge01steigoog` | Primary source | II | 808 | Google source/OCR package; OCR detects `ZWEITER BAND` and 23 figure plates. |

## Duplicate / Lower-Priority Local Witnesses

The packet root keeps a local-only `99_LOCAL_DUPLICATE_OR_LOWER_PRIORITY_NOT_UPLOAD` folder:

- `jacobsteinersge02steigoog`: Volume I-style witness, 627-page PDF.
- `jacobsteinersge03steigoog`: Volume I-style witness, 636-page PDF.
- `jacobsteinersge04steigoog`: same PDF hash as `jacobsteinersge03steigoog`; only metadata/text sidecars retained locally.

These are recorded for provenance and future comparison, but they are not first-upload material because the 600 ppi MBP/Pittsburgh witness plus BSB JP2 comparator are better for Volume I source-grounded work.

## Recommended Task

Produce a modern LaTeX transcription and optional English translation:

- Volume I from the 600 ppi MBP/Pittsburgh witness, with BSB JP2/PDF/OCR as comparator and locator support.
- Volume II from `jacobsteinersge01steigoog`.

Do not silently omit figure plates, geometric diagrams, plate references, tables, apparatus, or source notes. OCR is locator/control text only; promoted TeX must be checked against source images. Diagram-heavy passages should be marked for visual audit rather than paraphrased.

## Quality Rule

Distinguish high-resolution source PDF/page-image evidence, comparator JP2/PDF image evidence, OCR/ABBYY/DjVu locator text, and future promoted TeX. This packet makes a faithful source-grounded Steiner lane possible; it does not claim one has already been produced.
