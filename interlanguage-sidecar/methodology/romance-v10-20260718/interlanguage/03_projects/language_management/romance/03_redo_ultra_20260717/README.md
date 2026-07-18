# Romance four-stage redo — crash-recovered production state v10

This tree continues the Romance interlanguage lane from the immutable v9 predecessor. It does not claim that the 466-page R823 authority has been fully translated into a Romance interlanguage. The current machine gate is `qa/ROMANCE_ACCEPTANCE_GATE_v10.json`; the four-stage goal remains **ACTIVE_NOT_COMPLETE**.

- **Stage A — provenance and branches:** 61 explicit routes, 8 active and 53 zero-body routes. Rumantsch Grischun has three independently verified official general school-mathematics exam parts, but zero specialist-algebra bodies. Sursilvan, Sutsilvan, Surmiran, Putèr, and Vallader remain five separate zero-body routes. Stage A is not complete.
- **Stage B — consolidated corpus:** corpus v3 contains 148 representations, 142 primary unique records, 6 representation aliases, 66 counting-eligible records, and 5 excluded records. The current corpus tranche passes; branch and specialist-domain depth remain incomplete.
- **Stage C — WordWeb and production alignment:** `PAN_ROMANCE_WORDWEB_v10` preserves v9's 60 concepts, 106 senses, 39 C2 nodes, and exactly 802 evidence records: 120 inherited quotation-free unresolved ES/FR locator claims plus 682 reviewed occurrences. Primary row dispositions remain 510 accepted, 127 rejected, and 45 held. Accepted support reaches 73/106 senses; 33 senses remain unsupported. The v10 semantic-compatibility layer audits all 104 controlled-terminology rows and corrects six false links (`HG13`, `HG22`, `HG26`, `HG64`, `HG72`, `HG76`). The 194-row production crosswalk preserves all 101 Spanish and 93 French ledger rows: Spanish has 61 exact/pinned mappings and 40 explicit unmapped rows; French has 9 exact mappings and 84 explicit unmapped rows. It adds no attestation and promotes no form.
- **Stage C access/MII boundary:** `PAN_ROMANCE_ACCESS_LEDGER_v10` remains an exact 106 × 9 = 954-row sense/cohort grid. Every one of its seven human-result fields is null/empty on every row; all 954 rows have `pilot_eligible=false`; there are zero human observations and zero form promotions. Its orthographic proxy values are deterministic design diagnostics and do not measure intelligibility. Empirical MII therefore remains zero observations.
- **Stage D — controlled creation:** T001 covers body lines 21047–21087; T002 covers 21089–21097; T003 covers 21099–21115; T004 covers 21117–21146; T005 covers 21148–21202; and T006 covers 21209–21254. T001–T006 compile and validate, all six final output copies equal their build PDFs byte-for-byte, and all 15 fresh 150-dpi renders reproduce the pinned QA images. The T006 v2 metadata successors correctly identify the displayed column as unstarred while preserving the reciprocal-module stars; source and target TeX are unchanged. None is language- or human-validated. The next semantic authority line is 21256.

The exact zero-hit terms in the current corpus occurrence table are T11, T34, T52, T53, T54, and T56. A zero hit or unsupported sense is a source gap, not a negative human-intelligibility result. The 404 inherited form records and all candidate decisions retain their v8 noncanonical, unpromoted status.

## Rebuild sequence

1. Rebuild or verify corpus v3 and branch routing v2 with their existing scripts.
2. Preserve `ROMANCE_TERM_OCCURRENCES_v1.csv`; regenerate v2 only from the frozen corpus inputs when required.
3. Run/verify the six T01–T60 review tables and the three-row RM-2024 delta review.
4. Run `scripts/build_wordweb_and_access_v9.py` only when its frozen evidence inputs legitimately change.
5. Run the T001–T006 local prepare/build/validate sequences when their source or target bytes change.
6. Run `scripts/verify_pdf_renders_v10.py`.
7. Run `scripts/build_semantic_alignment_v10.py` to regenerate the effective-link layer, T006 metadata successors, and ES/FR production crosswalk.
8. Run `scripts/validate_romance_tranche_v10.py --core-only` before changing successor documentation.
9. Run `scripts/validate_romance_tranche_v10.py` to emit the final v10 manifest and acceptance gate.

V9's versioned WordWeb, access ledgers, gate, manifest, builders, and validation surfaces remain unchanged. `README.md` and `CONTINUATION_CURSOR.md` are intentionally mutable current-state pointers and now describe v10.

No pilot, native-validation, scalar-readiness, empirical-MII, or full-R823 Romance translation claim is authorized.
