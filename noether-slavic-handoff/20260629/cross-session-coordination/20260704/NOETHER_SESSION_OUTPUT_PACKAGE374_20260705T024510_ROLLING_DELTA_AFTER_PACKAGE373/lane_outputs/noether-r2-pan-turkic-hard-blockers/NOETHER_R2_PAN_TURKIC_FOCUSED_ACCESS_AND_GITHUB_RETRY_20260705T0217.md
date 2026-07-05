# R2 Pan-Turkic Focused Access And GitHub Retry

Prepared: 2026-07-05T02:17+02:00

Scope: metadata-only retry for the unresolved Kyrgyz Daramet PDF live-access probe and the three broad GitHub TeX searches that were previously incomplete/rate-limited. This does not fetch or publish raw source bodies and does not make translation, review, approval, license-clearance, gate, bridge, pilot, Zenodo, or Git-push claims.

## Control State

- AGENTS.md SHA-256: EE41CF302952ADC624160B9A94CC5AE4CD3EB61B309115F61D1316D0EF039548.
- .github/copilot-instructions.md SHA-256: CBF1788357F102CE372EF35606FD931AE8A79F782C1B495C96B78351A93AE34A.
- Parent ledger SHA-256: 8CFD618B2AD0AACE2150D4DFDA5003409E3D1D8477186CD97EBF4F835E64876A.
- B3 steward log SHA-256: 655559493B44E73515AF8F89CBE1A5FB7B70C3BF402BE0465E86F0713C02F35E.
- Git HEAD/upstream: 13a30325278b5ec8285e7d90d2f9e78672e3007e / 13a30325278b5ec8285e7d90d2f9e78672e3007e.
- Git status: ## codex/noether-pc-20260629...origin/codex/noether-pc-20260629.

## Findings

- R2 normalized register remains 61 rows, with 0 source-level TeX/LaTeX/arXiv/e-print/source-archive rows and 8 explicit hard-blocker gap rows.
- Daramet strict TLS HEAD failed with certificate revoked (CRYPT_E_REVOKED), confirming the prior SSL warning.
- Daramet TLS-relaxed HEAD returned HTTP/1.1 200 OK, Content-Type: application/pdf, Content-Length: 2319102, Last-Modified: Thu, 16 Nov 2017 11:02:39 GMT, and ETag: 5a0d704f-2362fe; no body was fetched.
- Local Daramet PDF SHA-256 remains `3ADF45747524AC0691C659B5AB1568F9AE4DACF3886ECDE92A57AD31E601FBE4` at `outputs/sources/current_web_source_canon_20260704/CWS-KY-002_daramet_algebra_8_klass.pdf`.
- GitHub retry outcome summary: false_positive_font_sample_not_math_source=1; false_positive_generated_docs_not_math_source=2; false_positive_language_list_not_math_source=2; strict_tls_failed_certificate_revoked=1; tls_relaxed_head_200_pdf=1; zero_results=1.
- Broad GitHub TeX retries produced no new Pan-Turkic mathematical source-level witness: Kyrgyz/Uyghur hits were language-list/generated-doc/font-sample false positives; Turkmen mathematics query returned zero results.

## Machine Files

- outputs/NOETHER_R2_PAN_TURKIC_FOCUSED_ACCESS_AND_GITHUB_RETRY_20260705T0217.csv
- outputs/NOETHER_R2_PAN_TURKIC_FOCUSED_ACCESS_AND_GITHUB_RETRY_20260705T0217.json

## Boundary

No raw source body was uploaded or packaged here. No translation output, glossary/term promotion, Pan-Turkic bridge, pilot, native/community-review claim, canonical approval claim, accepted terminology claim, license-clearance claim, gate promotion, Zenodo action, canonical source edit, Git stage, Git commit, or Git push is made here.
