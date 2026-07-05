# Pass 34: fold v6.1/apply-patch/batch-0 audit results into artifacts.
import json
import sys
import zipfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")

# 1) Pan-Romance ledger v3.2: dual-review convergence
p = BASE / "PAN_ROMANCE_C2_FILL_LEDGER_v3_20260705.json"
led = json.loads(p.read_text(encoding="utf-8"))
for r in led["rows"]:
    if r["concept"] == "invariant theory":
        r["status"] = "witnessed_sourcebody_internal"
        r["note"] += " | UPGRADED after ChatGPT sense re-probe v1.1 manual review confirmed FR/ES invariant-theory contexts (dual-review convergence F+C)"
    if r["concept"] == "resultant":
        r["note"] += " | re-probe v1.1 independently confirmed resultante-for-polynomials (dual-review convergence)"
    if r["concept"] in ("covariant", "contravariant"):
        r["note"] += " | re-probe v1.1 concurs: sense NOT confirmed in general shelves — stays sense-review, needs Noether-stratum sources"
led["review_note"] += " v3.2: invariant theory upgraded (dual review); covariant/contravariant stay demoted (both reviews concur); 6 specialist gaps + ground form remain for Noether intake."
led["artifact"] = "pan_romance_c2_fill_ledger_v3_2"
p.write_text(json.dumps(led, ensure_ascii=False, indent=1), encoding="utf-8")
print("ledger v3.2 written")

# 2) batch-0 validation note
note = r"""# BATCH-0 ORTHOGRAPHY PATCH — FABLE VALIDATION + CODEX APPLY CONDITIONS
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
"""
(BASE / "BATCH0_VALIDATION_AND_CODEX_CONDITIONS_20260705.md").write_text(note, encoding="utf-8")

# 3) route-B rejection + spec v2
d6 = """# ROUTE-B KWIC PROBE v1 — REJECTED AS-IS (defect D6) + refined spec
2026-07-05. TAIL_B_INTL_STEM_KWIC_PROBE_v1 (1,667 rows) fails intake audit:
- Schema: rows carry route_key/lang/form = null — the evidence channel is unusable as emitted.
- Genre contamination: sample windows include Slovak PROGRAMMING course notes (CPU/RAM text) and Russian
  non-math prose — generic stems (form, linear, special, general, normal) match any technical text.
- Root cause is SHARED: my route-B stem list (INTL regex) included over-generic stems. Own-fault noted.

Refined route-B spec (v2):
1. Drop generic stems entirely: form, general, normal, special, linear, sistem, metod, princip, relaci, element.
   Keep only distinctive math stems: algebr, polynom/polinom, invariant, determinant, homomorf/izomorf/automorf,
   ideal, teorem, matri[cx], vektor, dimenzi, koeficient, kongruen, diskriminant, rezultant, kvaternion, tenzor,
   aksiom, lema, korolar, modul (with module/modulo sense-note).
2. Math-genre file filter BEFORE probing: path/content heuristics (reject files matching procesor|RAM|program-course
   markers; require >=2 distinct math-stem types per file).
3. Emit schema: route_key, lang, form (non-null mandatory), file, count, window; validate non-null before emit.
4. Volume cap per stem per language (10 best files) — 1,667 undifferentiated rows is spray, not evidence.
"""
(BASE / "ROUTE_B_REJECTION_AND_SPEC_v2_20260705.md").write_text(d6, encoding="utf-8")

# 4) STATUS
entry = """
## Done (2026-07-05, pass 34 — v6.1/apply-patch/batch-0 intake: first text-touching artifact audited)
- [x] **Batch-0 orthography diff AUDITED** ([validation note](BATCH0_VALIDATION_AND_CODEX_CONDITIONS_20260705.md)): 260/262 pairs exactly the 6 sanctioned mappings; word inventory clean; no bib/German titles touched. DEFECTS: D5a same-line partial application ('najobščejšem' skipped beside fixed 'obščejših' — verbatim apply would CREATE mixed orthography); D5b diff patches renders/ AND translations/ (renders are derived). VERDICT: validated with 3 conditions (regenerate line-wide idempotent + TeX-aware exclusions; translations/ only + re-render; Cyrillic rebuild + gates). NOT applied here — codex-lane production, no silent divergence from the dump copy.
- [x] **Noether sense re-probe accepted** (dual-review convergence): invariant theory UPGRADED (ledger v3.2), resultant re-confirmed, covariant/contravariant stay sense-review (both reviews concur).
- [x] **Route-B KWIC probe REJECTED as-is** ([D6 + spec v2](ROUTE_B_REJECTION_AND_SPEC_v2_20260705.md)): null schema fields + genre contamination (Slovak programming notes matched on 'linear'). ROOT CAUSE SHARED: my INTL stem list was over-generic — spec v2 fixes both sides. Mutual-catch ran both directions this round.
- [x] Apply-pass design intake: bands consistent with R1 draft (12/5/6/2/2); JSON channel carries null action fields (CSV authoritative) — minor channel defect noted.
- Cursor: batch-0 + conditions to codex lane; lexeme switches await Floris's read of the R1 headline calls; route-B v2 rerun = ChatGPT bounded task; route-A per-concept probes (516 rows) = the big open queue.
"""
sp = BASE / "STATUS.md"
sp.write_text(sp.read_text(encoding="utf-8").rstrip() + "\n" + entry, encoding="utf-8")

# 5) bundle refresh
zp = BASE / "CHATGPT_HANDOFF_BUNDLE_20260705.zip"
with zipfile.ZipFile(zp, "a", zipfile.ZIP_DEFLATED) as z:
    have = set(z.namelist())
    for f in ["BATCH0_VALIDATION_AND_CODEX_CONDITIONS_20260705.md",
              "ROUTE_B_REJECTION_AND_SPEC_v2_20260705.md"]:
        if f not in have:
            z.write(BASE / f, f)
print("all pass-34 artifacts written; bundle:", zp.stat().st_size, "bytes")
