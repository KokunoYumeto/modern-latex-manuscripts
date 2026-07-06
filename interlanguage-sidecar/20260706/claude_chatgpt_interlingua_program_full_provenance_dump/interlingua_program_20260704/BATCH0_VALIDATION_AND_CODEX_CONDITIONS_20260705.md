# BATCH-0 ORTHOGRAPHY PATCH — FABLE VALIDATION + CODEX APPLY CONDITIONS
2026-07-05. Audit of NORMALIZATION_BATCH0_ORTHOGRAPHY_PATCH_PROPOSAL_v1.diff (262 change-pairs, 6 mappings).

## Verdict: VALIDATED WITH 3 CONDITIONS — do not apply the .diff verbatim.

Audit results:
- 260/262 pairs are EXACTLY the six sanctioned mappings (vzet->vzęt, obšč->obć, dlugost->dolgost, v(o)obče->obće).
  Changed-word inventory contains nothing outside the six families. No German/bibliographic titles touched;
  the 4 \footnote-context lines change only surrounding ISV prose.
- DEFECT D5a: 2 pairs apply the mapping to ONE token but skip a neighbor ON THE SAME LINE
  ('obščejših' fixed, 'najobščejšem' left) — occurrence-offset patching. Applying verbatim would CREATE mixed orthography.
- DEFECT D5b: the diff patches BOTH germanOut/translations/ AND germanOut/renders/ trees (paper06 hunk duplicated).
  renders/ are derived artifacts.

## Conditions for the codex lane
1. REGENERATE the patch line-wide and idempotently from the six mappings (whole-line replacement per mapping,
   TeX-aware exclusions: skip \cite / \label / \bibitem / \href / \url / \texttt arguments, comments, math mode) —
   do NOT replay the occurrence-queue offsets.
2. Apply to translations/ ONLY; re-render renders/ from source; rebuild Cyrillic siblings in the same run (G5 sync gate).
3. Gate: recompile 0-err; rerun coverage + cyrillic_sync_check; expected delta = orthography consolidation only
   (type count drops slightly, token coverage unchanged or +epsilon).

Scope: this batch stays orthography-only. Lexeme switches (odnovrěmenno->jednočasno, sootvětstvovati->odpovědati,
korak->krok...) remain queued behind Floris/reviewer sign-off of the R1 draft; human-review rows
(ręd, jednako, važiti, slučaj) excluded entirely.
