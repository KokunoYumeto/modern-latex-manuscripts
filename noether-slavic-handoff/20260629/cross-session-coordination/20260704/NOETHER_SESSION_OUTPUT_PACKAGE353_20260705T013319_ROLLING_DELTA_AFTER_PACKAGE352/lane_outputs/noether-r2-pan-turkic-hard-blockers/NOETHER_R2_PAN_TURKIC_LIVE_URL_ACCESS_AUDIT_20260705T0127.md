# R2 Pan-Turkic Live URL Access Audit

Prepared: 2026-07-05T01:27+02:00

Scope: metadata-only live access probe over unique source_url values in the R2 normalized source-canon register. The audit checks external URL status headers where possible, carries existing local hashes/license-access signals, and treats explicit hard-blocker gap rows as non-URL rows. It does not fetch or publish raw source bodies and does not make license-clearance, review, approval, gate, translation, bridge, pilot, Zenodo, or Git-push claims.

## Summary

- Register CSV SHA-256: 5BFD1920A01B1079A1C1047553ABD4313276185B8EA4C7D26A809B22092A49D7.
- Register rows represented: 61.
- Unique URL/gap groups audited: 47.
- Source-level TeX/LaTeX/arXiv/e-print/source-archive rows in register: 0.
- Explicit hard-blocker gap rows in register: 8.
- Remote status summary: 200=45; not_applicable_explicit_gap_row=1; probe_error=1.
- Live access signal summary: explicit gap row; no external source URL by design=1; live_head_reachable_or_redirect=45; probe_error_no_body_fetched=1.
- Language group summary: Kyrgyz=9; Tatar=10; Tatar-region lead=1; Tatar; Kyrgyz; Turkmen; Uyghur=1; Turkmen=11; Uyghur=15.

## Machine Files

- `outputs/NOETHER_R2_PAN_TURKIC_LIVE_URL_ACCESS_AUDIT_20260705T0127.csv`
- `outputs/NOETHER_R2_PAN_TURKIC_LIVE_URL_ACCESS_AUDIT_20260705T0127.json`

## Boundary

No raw source body was uploaded or packaged here. No translation output, glossary/term promotion, Pan-Turkic bridge, pilot, native/community-review claim, canonical approval claim, accepted terminology claim, license-clearance claim, gate promotion, Zenodo action, canonical source edit, Git stage, Git commit, or Git push is made here.

