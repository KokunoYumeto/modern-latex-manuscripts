# D020 final cold source-fidelity audit

Status: IN_PROGRESS. Independent read-only audit; this is not a PASS certificate.

## Scope and method

Read `control/GOVERNING_INSTRUCTIONS.md` and the complete PDF skill. Inspected the controlling PDF directly, with fresh Poppler 140-dpi renders in `audit/final_source_qa`. Compared the French and English page records, using source pixels as authority. No production files patched; no inherited QA verdict accepted as evidence. Page topology is physical 1 = NUMDAM cover; physical 2–36 = printed 273–307.

Authority PDF SHA-256 independently recomputed: `8392B345D4854E6DC55FB42CFC0B616D941935983723627237239A87348F42E5`.

## Confirmed findings (work in progress)

1. Physical 4 / printed 275, (1.4)c: scan uses `|X|_F` (F subscript) for the set of orbits. French `edition/source_language.ndjson` instead has `|X|/F`. English has `|X|_F`. Even if the quotient notation is mathematically conventional, this is not source-faithful diplomatic notation.

## Exact inspected coverage so far

- Source pixels: physical pages 1–6, complete page images.
- French page-record text: physical pages 1–6.
- English text/formulas: physical pages 1–2 and 4–6. Physical 3 English remains to check.
- No rendered reader PDF coverage yet.

Next executable action: resolve the candidate physical-5 `forme`/`formelle` and physical-6 arrow discrepancies from larger source renders; continue ordered page comparison through physical 36, then record exact final coverage and hashes.
