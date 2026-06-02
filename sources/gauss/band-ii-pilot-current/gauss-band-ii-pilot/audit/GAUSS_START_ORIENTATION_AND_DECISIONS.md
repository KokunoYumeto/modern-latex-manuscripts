# Gauss Start Orientation and Decisions

## Local inputs inspected

- `Gauss Starter Packet 20260601 - 01 Core Readers TeX Audit.zip`
- `gauss_text_tex_audit_material.zip` inside that packet
- `01_gauss_phase1_satellite_ready_reader_pdfs_and_artifacts.zip`
- Existing Gauss audit outputs: `GAUSS_TRIAGE_REPORT.md`, `gauss_tex_quality.csv`, `gauss_pdf_audit.csv`, and public summary JSON.

## Current source status

The useful source base is the 118-file TeX snapshot in `source_tex_and_component_pdfs/`. Its audit classification is:

- 100 grade A files;
- 6 grade C files;
- 12 grade D files.

The P0/P1 list is in `source_inventory/HOLDOUTS_P0_P1.csv`. The worst current OCR-damaged areas are concentrated in Band VI, with additional holdouts in Bands IV, V, VII, and Band II ch9. The project should treat the broad reader PDFs as readers, not as the authority for repair. The authority for continuation is: source scan -> source TeX -> rendered PDF -> audit.

## Decision for this first round

I did not attempt a giant automatic rewrite. That would risk turning genuine source into another untrusted derivative. Instead I promoted two small, already scan-locked Band II repair passages into a clean working batch and added English translations. This gives a reproducible pattern for subsequent units:

1. keep source TeX separate;
2. remove/avoid local compile blockers such as unguarded `microtype`;
3. render source and translation PDFs;
4. run a raw-TeX leakage check;
5. keep exact source page references in the audit note.

## Next high-value moves

1. Feed packet 02 and 03 if available: source scans/component PDFs and rendered crops are needed for strict source checking.
2. Continue Band II/Band III less-standard translations where TeX grade is A and scan pages are available.
3. Run P0 OCR repair on Band VI ch8, ch10, ch11, ch12, ch13 first. Do not translate those before repair.
4. Keep cumulative current lean: add completed, checked source/translation units; keep bulk provenance in the central source inventory.
