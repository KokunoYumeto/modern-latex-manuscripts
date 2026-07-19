# Source mapping

## Collected-tail source packet

- File: `02_source/tail_p765_777/Noether_GesammelteAbhandlungen_IA_tail_full_pp725_796.pdf`
- Scope: 72 packet-local pages corresponding to source-PDF pages 725-796.
- Authority class: IA-derived collected-volume scan PDF; best complete local tail witness available for this pass.
- SHA-256: `F98C16E6529BC4C24F8D1CDC087B48825FD71173EB18F0C1A25D0D1508B8F9B0`.

## Closed collected band

| Packet pages | Source-PDF pages | Collected pages | Complete-page witnesses | Audit |
| ---: | ---: | ---: | --- | --- |
| 1-36 | 725-760 | 711-746 | `tail_p711_746/full_pages_650dpi/tail-01.png` through `tail-36.png` | `03_audit/tail_p711_746/tail_p711_746_page_audit.csv` |
| 37-54 | 761-778 | 747-764 | `tail_p747_764/full_pages_650dpi/tail-37.png` through `tail-54.png` | `03_audit/tail_p747_764/tail_p747_764_page_audit.csv` |
| 55-67 | 779-791 | 765-777 | `tail_p765_777/tail-55.png` through `tail-67.png` | `03_audit/tail_p765_777/tail_p765_777_page_audit.csv` |

For this band:

- packet-local page = collected page - 710;
- source-PDF page = collected page + 14.

Exact source slices:

- `02_source/tail_p711_746/Noether_collected_pp711_746_source_slice.pdf`, 36 pages, SHA-256 `F986F6896BA7D8862367946A5CF8B5029B350CB01AC486941044932407ED72BA`;
- `02_source/tail_p747_764/Noether_collected_pp747_764_source_slice.pdf`, 18 pages, SHA-256 `CBA8BF02F66134CA3831129394F090D0952328F746756ACF11525C19F69BC722`;
- `02_source/tail_p765_777/Noether_collected_pp765_777_source_slice.pdf`, 13 pages, SHA-256 `9083177C451C0CF00F432F727E3F98EE77FC30875F9858BFAD9B90260DD36F17`.

## Paper 4 follow-up source

- Source slice: `02_source/P04_p144_154_deep_followup/Web_P04_source_printed_p144_154.pdf`.
- Scope: Paper 4 printed pp. 144-154, mapped to source-slice pages 1-11 and original source-PDF pages 27-37.
- SHA-256: `D39D67C60EDC3F045727DF5EF32C0DEFDFF1F482D1E419B9A6A0F0A13B72C87F`.
- Complete-page witnesses: `02_source/P04_p144_154_deep_followup/full_pages/P04_p144_source_600dpi.jpg` through `P04_p154_source_600dpi.jpg`.
- Exact output mapping: `03_audit/P04_p144_154_deep_followup/Web_P04_p144_154_output_page_mapping.csv`.
- Bounded formula and page dispositions: `03_audit/P04_p144_154_deep_followup/`.

## Dense-field witnesses

The `dense_crops_1300dpi` and Paper 4 `focus` directories contain inspection aids derived from the complete source-page witnesses. They do not supersede the source PDFs. OCR locator files under the tail directories are explicitly non-authoritative.
