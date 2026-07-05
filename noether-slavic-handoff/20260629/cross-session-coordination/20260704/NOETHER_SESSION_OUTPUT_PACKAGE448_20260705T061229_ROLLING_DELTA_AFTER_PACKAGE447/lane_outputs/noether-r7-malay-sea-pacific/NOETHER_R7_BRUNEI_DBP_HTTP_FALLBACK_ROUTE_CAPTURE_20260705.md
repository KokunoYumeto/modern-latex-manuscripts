# Noether R7 Brunei DBP HTTP Fallback Route Capture - 2026-07-05

Scope: source-canon/provenance only. This packet refines the prior Brunei DBP/MABBIM access blocker by separating HTTPS failure from HTTP fallback access. It does not translate, approve terms, claim native review, claim canonical approval, clear licenses, promote gates, claim completion, or push Git.

Rows:

- CSV: `NOETHER_R7_BRUNEI_DBP_HTTP_FALLBACK_ROUTE_CAPTURE_ROWS_20260705.csv`
- Row count: 12
- Payload policy: no raw HTML/PDF/source bodies are stored in `outputs`; rows contain protocol status, remote hashes, byte counts, signal counts, and blocker notes only.

## Motivation

Earlier Brunei/Singapore packets recorded the DBP/MABBIM route as blocked because direct HTTPS tooling failed. This pass retried the same official route plus related DBP governance routes over both HTTPS and HTTP. The result is narrower and more useful: HTTPS remains blocked, but several official DBP Brunei routes are reachable and hashable over HTTP.

## Findings

- HTTPS direct probes still fail for the DBP Brunei root, MABBIM institutional page, Jawatankuasa page, language-development page, MABBIM announcement, and MABBIM event route.
- HTTP fallback probes return `200` and hashable HTML for:
  - DBP Brunei MABBIM institutional page.
  - Jawatankuasa Tetap Bahasa Melayu Brunei Darussalam page.
  - Bahagian Pembinaan dan Pengembangan Bahasa page.
  - MABBIM announcement/event/news-list routes.
- The HTTP MABBIM institutional page has MABBIM signals and one mathematics signal in the page text, but the automated probe found zero `Aljabar`, `Gelanggang`, `Modul`, or `Noether` signals.
- Related HTTP DBP governance/news/event routes have MABBIM signals but no mathematics or higher-algebra signals in this pass.

## Disposition

This pass upgrades the Brunei DBP state from a broad "blocked" row to a protocol-specific source-return state:

- HTTPS route: still blocked by reset/SSL failure from direct tooling.
- HTTP fallback route: hashable official-route/governance provenance.
- Exact mathematical corpus content: still not captured.
- TeX/LaTeX/e-print/source archive package: still not found.

The DBP Brunei MABBIM route can now be used as a source-return locator and governance provenance row, but it still does not authorize translation support or term approval. Future work should look for item-level Brunei DBP/MOE math terminology documents, not infer them from these route pages.
