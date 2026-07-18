# SGA 5 French-control reconciliation

Reconciled: 2026-07-18, Europe/Berlin.

## Disposition

The exact French TeX at SHA-256
`791F4EFFC5E02832D5D77ED03518C8156D6F07E4C8238B03545DB93D883FBB28`
remains the pinned source-language comparison authority used by this English
workpass. This file's identity is established. The stronger proposition that
the French workpass is independently certified complete is **not** established
by the currently co-located control set, because those controls contain a
material chronological conflict and several claimed deliverables are absent.

This reconciliation does not choose the strongest claim merely because it is
later. It records both claims, preserves their provenance, and narrows the
English task's reliance to the exact TeX plus direct use of the original scan
at ambiguous or source-critical loci.

## Conflicting coverage records

1. `SOURCE_AUDIT_STATUS.md` records an early ordered pass. Lines 107 and 109
   leave printed pp.66-102 and 104-484 open with the next cursor at p.66;
   lines 128 and 141 summarize only pp.1-65 plus p.103; line 149 explicitly
   says not to claim completeness until the page table reaches 484.
2. `CERT_LOG.md` is a later, much larger manual log. Its p.480 entry (around
   line 488) says the ten-expose body was checked page by page through the end
   of Expose XV. Its very large line 499 also claims the printed pp.481-484
   indexes were checked and cites a 306-page build gate; this is not structured
   as a clean one-row-per-page ledger.
3. `README_DELIVERABLES.md`, `FINDINGS.md`, and
   `QUALITY_STATEMENT_SGA5.md` repeat later completion/build claims, but they
   do not reconcile or supersede `SOURCE_AUDIT_STATUS.md` in a durable signed
   handoff, and the reader/build artifacts to which they refer are not all
   present beside the TeX. `FINDINGS.md` also contains a 307-page build claim,
   while later files say 306 pages. `QUALITY_STATEMENT_SGA5.md` repeats the
   page-review narrative but explicitly stops short of a certified-complete
   edition.

Therefore the honest control statement is: a later internal log claims the
ten-expose French body was reviewed through printed p.480, while an earlier
status file remains open after p.65 plus p.103. This English task has not
independently replayed the full French certification process and does not
convert either record into independent human certification.

## Current directory inventory

The French-control directory currently contains exactly seven files. Their
bytes, hashes, roles, and claim status are frozen in
`FRENCH_CONTROL_INVENTORY_20260718.csv`.

The following deliverables named or implied by the French documentation were
not found in the project workspace during the 2026-07-18 reconciliation:

- `sga5_fr_workpass.pdf`;
- `METHOD_AND_LESSONS.md`;
- `AGENT_SCORECARD.md`;
- `FINDINGS_consolidated_20260624.md`;
- `_work/swarm_results/workpass_vs_repair032.diff`;
- `_work/chunk_page.py`;
- `_work/render_src.py` and `_work/crop_src.py`;
- `_work/build_index.py`;
- `_work/patches_p*.json`;
- `SOURCE_AND_RESOLUTION.md`;
- `sga5_index.csv` and `sga5_index.json`;
- `SGA5_AUDIT_METHOD_WRITEUP.md`.

The current Zenodo version contains a file named
`00_SGA5_French_Workpass_NotCertified_20260706.pdf` (2,015,658 bytes, 306
pages; locally recorded SHA-256
`977E3180CF5404DC7F0057C87551E41A7C0B87AE89BAFA5D8D40425DCD08B68A`).
It is an external visual/control witness. No retained build receipt currently
proves that it was generated from the exact co-located TeX hash above, so it is
not used as an editable authority or as proof of completeness.

## Effect on the English synchronization

- The French TeX is pinned by exact hash and remains the primary source-text
  control for the curated ten-expose English cumulative.
- The original LNM 589 scan remains the source witness used to adjudicate
  ambiguity, formulas, diagrams, and suspected defects. It is audit-only and
  excluded from public payloads.
- The reopened p.14 and p.43 English notes were adjudicated directly against
  the French TeX and scan, so this documentation conflict does not invalidate
  those two decisions.
- No statement in the replacement English payload will call the French
  workpass, the English translation, or the package a certified critical
  edition.

## Continuation rule

If a frozen French reader or the missing final French audit receipt is later
recovered, hash it, establish its build relationship to the pinned TeX, and
append a new dated reconciliation. Do not rewrite or delete the contradictory
historical controls.
