# Noether R7 Maori Pangarau Tahurangi PDF Access Capture - 2026-07-05

Scope: source-canon/provenance only. This packet records Aotearoa New Zealand Māori/Pāngarau curriculum and pedagogy routes: exact temp-hashed official Pāngarau PDF bitstreams where direct download works, and explicit access/wrapper blockers where exact source bodies remain unavailable. It does not translate, approve terms, claim native review, claim canonical approval, clear licenses, promote gates, claim completion, or push Git.

Rows:

- CSV: `NOETHER_R7_MAORI_PANGARAU_TAHURANGI_PDF_ACCESS_CAPTURE_ROWS_20260705.csv`
- Row count: 12
- Payload policy: no raw PDF, HTML, text, or source bodies are stored in `outputs`; PDF and wrapper probes were downloaded to temporary files, hashed, byte-counted, and deleted immediately.

## Exact PDF Witnesses

- `TMoA-Pāngarau-0-8-English.pdf`: 5,318,697 bytes; SHA-256 `74DC27D608AF0F7275D715A684479D43295A0CEDFA6A4A69F0BFAF6D410EFD82`
- `TMoA_Pāngarau_Tūārere1-4-English.pdf`: 1,662,556 bytes; SHA-256 `526ADC34B1AC2242EE5E05F15C2D2BCCFC216E845C716E8CE1446C672602F68F`
- `Tuhinga-hukihuki-Wāhanga-Ako-Pāngarau-08-2024-ENG.pdf`: 19,071,528 bytes; SHA-256 `4B5A9F159A8CFC64E78D6D7E3C95BB166504AEF6C83EB9AD6FE0E83AF929DE68`

## Access Boundaries

- Kauwhata Reo/Tāhūrangi official Pāngarau pages for Tūārere 1, 2, 3, 4 and the Te Marautanga landing route returned HTTP 403 in direct shell access.
- Education Counts' Pāngarau spotlight page returned HTTP 403 in direct shell access, although search indexing identifies the Te Reo mathematics pedagogy summary listing.
- The legacy UNESCO `EdPractices_19ma.pdf` path returned a tiny HTML wrapper rather than a PDF body.
- The legacy IAOED `EdPractices_19ma.pdf` path failed under TLS in current tooling.
- A UNESDOC ark route returned hashable HTML metadata, but not the exact Te Reo PDF body.

## Disposition

This packet strengthens the Pacific/Aotearoa source-canon shelf with exact official Pāngarau PDF provenance, while separating blocked or wrapper routes from corpus-body evidence. The three exact PDFs remain PDF fallback witnesses, not TeX/LaTeX/e-print/source archive packages and not translation or accepted-terminology authority.

Next source actions:

- Retry Kauwhata Reo pages through browser/manual access and connect page-level metadata to direct PDF bodies where possible.
- Resolve the current Te Reo `Te ako pāngarau whaihua` PDF body, if an accessible current route exists.
- Search for Māori-medium Pāngarau source packages or official downloadable resource bundles beyond PDF fallback.

## Validation Snapshot

- Row CSV count: 12
- Exact PDF temp-hash rows: 3
- Official page direct-403 rows: 6
- Legacy/metadata wrapper or TLS blocker rows: 3
- Rows missing required no-claim boundary: 0
- Raw PDF/HTML/text/source payload files stored in `outputs`: 0
