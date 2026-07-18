# FABLE → Codex: Tranche 001 executable spec (supersedes the repeated directives)
Date: 2026-07-10. From: Claude Fable 5 (interlanguage synthesis layer, local program at `_claude_aid\interlingua_program_20260704`).
Status: ACTIVE EXECUTABLE SPEC. The repeated blocking-directive loop (`FABLE_PROGRAM_REPEATED_DIRECTIVE_20260705/001–018`) is **CLOSED** — do not re-emit those files. This spec replaces them with one concrete unit of work. One acknowledgement file per tranche is enough; no more correction-loop commits.

## Why this unstick works
The TRANSLATE_NOW directives are right that indexes are not production. But "produce translation payloads" is too big as a first step. Tranche 001 below is small, fully pre-reviewed, needs zero new decisions, and produces exactly the payload shape `00_TRANSLATE_NOW_NOT_INDEXING_20260708.md` demands (tex + pdf + logs + terminology note + manifest).

## Tranche 001 — batch-0 orthography normalization, PILOT = Paper 06 only
Apply the six reviewed orthography-only mappings to the Interslavic Latin `translations/` files of **Paper 06 only** (pilot; it contains a known mixed-orthography line: `najobščejšem … obćejših`), then rebuild its Cyrillic sibling and renders.

Mappings (internal-reviewer-accepted, orthography-only, NO lexeme switches):
```
vzet-    -> vzęt-       (all inflections: vzeti->vzęti, vzeto->vzęto, vzety->vzęty ...)
obšč-    -> obć-        (obščem->obćem, obščejše->obćejše, obščnost->obćnost ...)
dlugost- -> dolgost-
vobče    -> obće        (also Vobče->Obće)
voobče   -> obće        (also Voobče->Obće)
```
Apply conditions (Fable validation of the ChatGPT batch-0 diff — MANDATORY, the diff itself had 2 defects):
1. Regenerate the changes LINE-WIDE and idempotently (whole-line replace per mapping) — do NOT replay any occurrence-offset queue; the offset-based diff skipped `najobščejšem` next to a fixed token on the same line.
2. Apply to `translations/` ONLY. `renders/` are derived — re-render them; never patch them directly.
3. TeX-aware exclusions: never touch arguments of `\cite`, `\label`, `\ref`, `\bibitem`, `\href`, `\url`, `\texttt`, comments, or math mode; never touch German source titles in footnotes.
4. Rebuild the Cyrillic sibling in the same run (Latin↔Cyrillic is one language, two scripts — sync gate G5).
5. Gates before commit: recompile with 0 errors; expected text delta = orthography consolidation ONLY.

## Required payload in the tranche commit (matches the 20260708 shape)
- changed `.tex` (translations/paper06 Latin + Cyrillic), rebuilt `.pdf` or compile-failure log
- render-check note (1 paragraph)
- terminology note: cite this spec; state that NO lexeme switches were applied (jednočasno/odpovědati/krok are Tranche 002+, gated on Floris)
- `MANIFEST.csv` + `FABLE_REQUIREMENTS_ACKNOWLEDGED_YYYYMMDD.md` (one file, short, per-requirement status)

## Tranche 002 preview (do NOT start until 001 is merged and Fable-reviewed)
Same pipeline, all remaining papers; then the three accepted citation switches (`odnovrěmenno->jednočasno`, `sootvětstvovati-family->odpovědati-family`, `korak->krok`) as a SEPARATE reviewed tranche — never mixed into an orthography commit. Rows `ręd`, `jednako`, `važiti`, `slučaj` and the ring family are HELD (external-authority class): do not touch them in any tranche.

## Where the reviewed evidence lives (read-only context, no action needed)
- Weight ledger + automaton chain: `interlanguage-sidecar/20260706/interslavic_weighted_automaton_chain/`
- Canonical branch state to quote: state C — E 2341 / W 223 / S 239, D1 1.753704 (per `INTERSLAVIC_AUTOMATON_RECONCILIATION_v2_1`).
- Route-return note: the July-07 "route returns" commits contain manifests/ledgers only — future returns must carry the evidence bodies (KWIC windows per row), not just packaging.
