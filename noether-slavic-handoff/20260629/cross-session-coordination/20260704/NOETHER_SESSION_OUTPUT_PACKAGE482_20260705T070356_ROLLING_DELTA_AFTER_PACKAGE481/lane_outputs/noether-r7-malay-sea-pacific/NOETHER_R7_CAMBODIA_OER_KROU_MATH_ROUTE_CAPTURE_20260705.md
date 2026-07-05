# Noether R7 Cambodia OER/Krou Math Route Capture - 2026-07-05

Scope: source-canon/provenance only. This packet adds Cambodia official-OER and Krou route evidence to the SEA/Pacific source-return shelf. It does not translate, approve terms, claim native review, claim canonical approval, clear licenses, promote gates, claim completion, or push Git.

Rows:

- CSV: `NOETHER_R7_CAMBODIA_OER_KROU_MATH_ROUTE_CAPTURE_ROWS_20260705.csv`
- Row count: 12
- Payload policy: no raw HTML/PDF/image/source bodies are stored in `outputs`; rows contain URL, status, byte count, hash, signal fields, license/access signal, and gap status only.

## Motivation

The previous SEA/Pacific retry packet kept Khmer mostly at glossary/book-index status. This pass searched for stronger official Cambodia/MoEYS route evidence, especially upper-secondary mathematics. It found a useful OER route stack but not an exact higher-algebra source body.

## Findings

- OER Cambodia home, About, Mathematics label, Grade 12 label, Upper Secondary label, and upper-secondary Mathematics curriculum pages are current HTTP 200 routes and hashable.
- OER pages carry an observed Creative Commons Attribution 3.0 site signal. This packet records the signal but does not claim license clearance.
- The upper-secondary Mathematics curriculum page is an official MoEYS/OER route for Grade 10/11/12 mathematics curriculum context, but no downloadable curriculum body was captured from that page in this pass.
- The curriculum page thumbnail/image is hashable as a route sidecar only, not a text corpus.
- Two MoEYS storage PDF candidates surfaced by search returned tiny `text/plain` responses rather than PDF payloads from direct tooling.
- Krou Cambodia routes, including a search-visible Grade 12 Mathematics lesson route, are blocked by SSL from direct tooling in this pass.

## Disposition

This packet strengthens the Cambodia SEA/Pacific source-return shelf with official OER route provenance and a clear CC BY site-signal row. It still does not supply target-language higher-algebra proof prose, a TeX/LaTeX/e-print/source archive, or accepted terminology authority.

Next source actions:

- Continue item-level OER/Krou discovery for exact Grade 12 mathematics documents or downloadable lesson bodies.
- Retry Krou through browser/manual TLS or an alternate API route.
- Treat MoEYS storage PDF candidates as wrapper/blocker rows until a real PDF payload is captured.
- Keep Khmer glossary rows separate from official OER route rows and out of translation authority.
