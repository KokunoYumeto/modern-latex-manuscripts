# SGA5 full source-faithful audit — STATUS (resumable)

## Goal
Take SGA5 French TeX from "working draft that no longer drops whole pages" to an
actually-correct source-faithful edition, so a mathematician can trust it instead of
spending years fixing it. Every level: prose, equations, symbols, diagrams, labels.

## Why this exists
The diagram-only passes (repair018–032) worked from a 179-row manifest that has holes
(e.g. diagram (4.4.2), source p103, was never on it — and was wrong). "Complete" in the
old packets meant "finished the rows on the list," not "the file is correct." So the only
trustworthy method is page-by-page against the source scan, ignoring the old lists.

## Method (do not deviate)
- Work ONLY on the copy `sga5_fr_workpass.tex` (this folder). Never edit the canonical
  `SGA5\cumulative\fr\sga5_fr_repair032_codex_work.tex` directly. Produce a diff for review.
- Base = repair032 (Codex's 5 fixes were checked and are genuine — keep them).
- Source of truth = the SCAN, `sga5_sga6_repair022_20260612\1\SGA5\cumulative\scans\sga5_src.pdf`
  (484 pages; printed page number == PDF page index, no offset, verified on p102/205/338).
- Per source page: render it, read it, find the matching TeX region (by tag number /
  theorem number / French phrase), compare EVERYTHING, log every mismatch in FINDINGS.md,
  fix in the work copy.
- Render helper: `_work\render_src.py <page...>` (writes 150dpi page + zoom crops on request).

## Source ↔ TeX skeleton (exposés)
TeX total lines: 15380. Section starts (TeX line):
- Exposé I  Complexes dualisants: 313 (Intro), 327 (§1) … 1372 (§5), 1495 (Appendice)
- Exposé III Künneth/Lefschetz: 1856 (§1) … 2743 (§4 Lefschetz), 3462 (§5), 3702 (§6 appendice)
- Exposé III B Termes locaux: 4161 / 4342
- Exposé V J-adiques: 6642 ;  VI: 8185 ;  VII: 9045 ;  VIII: 11544
- Exposé X Euler–Poincaré: 12196 ;  XII: 13209 / 14103 ;  XV Frobenius: 14202
(Source page for each exposé start to be filled in as the pass reaches it.)

## Progress log (source pages)
SOURCE NOW = `C:\Users\Floris\Documents\Papors\OS\SGA5 (1).pdf` (complete Springer book).
**Printed page = PDF page − 12.** Render via `_work\chunk_page.py <printed>` (3 zoom chunks @600dpi→2400px).
See SOURCE_AND_RESOLUTION.md — 360 dpi is the global ceiling (confirmed online); this scan is as good as exists.

| source pp | status | notes |
|-----------|--------|-------|
| 1 | DONE clean | Exposé I title + intro paras 1–3 match verbatim. |
| 2 | DONE, 1 fix | FIXED local-duality pairing symbol (stalk vs local-cohomology). |
| 3 | DONE clean | §1 head, Déf 1.1, Rem 1.2 a)/b) — all 3 chunks match verbatim. |
| 103 | FIXED (out of order) | (4.4.2) 7 spurious ⊗ subscripts + regrouped top-left box → corrected. |
| 4 | DONE, 1 fix | FIXED dévissage H→I (I^i). |
| 5 | DONE clean | end 1.3 proof, Rem 1.3.1, Déf 1.4, Prop 1.5 stmt. |
| 6 | DONE clean | Lemme 1.5.1 + proof, Preuve de Prop 1.5 (short page). |
| 7 | DONE clean | Rem 1.5.2, Prop 1.6 + proof, bidualité intro. |
| 8 | DONE clean | bidualité, Déf 1.7, Rem 1.8 a/b. |
| 9 | DONE clean | Rem 1.8 c/d/e, formules d'échange, tor-dim, footnote. |
| 10 | DONE, 1 fix | FIXED Lemme 1.9 a) hypothesis D_c^-→D_c. |
| 11 | DONE clean | Prop 1.11 b/c/d + proof. |
| 12 | DONE, 1 fix | FIXED Prop 1.12 a)(i) duality iso: D_Y R f_*→R f_! (shriek). |
| 13 | DONE, 1 fix | FIXED a(ii) finitude R f_*→R f_! (shriek). |
| 14 | DONE, 1 fix + erratum | FIXED "démontre(ra)"; LOGGED source erratum in Cor 1.13 chain (no TeX change). |
| 15 | DONE, emendation kept | source typo D_c(F); TeX correctly has D_c(Y), kept. |
| 16 | DONE, 2 notes | emendation kept (1.5→1.6); source cross-ref (1.6 for dualisant) flagged. No TeX change. |
| 17 | DONE, 3 fixes | Théorème 2.1 proof L^∨[-r]→L[r] cluster (TeX 599, 601, 603). |
| 18 | DONE, emendation kept | Lemme 2.2; source `H^{-i(x)}` typo, TeX correctly has `-r(x)`, kept. |
| 19 | DONE clean | Lemme 2.2 proof: specialization square (*) checked node-by-node, r-loc-const arg. |
| 20 | DONE clean | Lemme 2.2 end: suite exacte (**), splitting, contradiction `i_!A_U + j_*A_x`. |
| 21 | DONE clean | §3 head, §3.1 Préliminaires, 3.1.1 Lieu singulier (reg). |
| 22 | DONE clean | 3.1.2 Dévissage (conditions i/ii/iii, ii bis/iii bis), 3.1.3 head. |
| 23 | DONE clean | 3.1.3 (cdloc)_n + 3.1.4 Pureté (fundamental-class iso), G. Ofer footnote. |
| 24 | DONE, 1 fix | 3.1.5 Résolution; FIXED spurious `\Gamma^*`→`\Gamma` (source has plain Γ). |
| 25 | DONE clean | 3.1.6 Finitude, §3.2 head, Prop 3.2.1 stmt + formula (*). |
| 26 | DONE, 1 fix | Prop 3.2.1 proof (dense); FIXED `×_Z`→`×_X` to source (equal since Y⊆Z). |
| 27 | DONE clean | Rem 3.2.2, Cor 3.2.3 (dim.q.inj≤2d), Lemme 3.2.4 stmt+proof start. |
| 28 | DONE clean | Lemme 3.2.4 end (E_2 ss), Cor 3.2.5, §3.3 head, Prop 3.3.1 a) i/i-bis/ii. |
| 29 | DONE clean | Prop 3.3.1 conditions ii-bis/ter/iii + b); Preuve (i bis)⟹(ii) duality. |
| 30 | DONE, 1 note | distinguished triangle checked; source `D_c^+(X)` at cqfd likely typo for Y, TeX faithful, flagged. |
| 31 | DONE clean | mapping-cylinder triangle (+1) checked node-by-node; récurrence; end Prop 3.3.1. |
| 32 | DONE clean | §3.4 bidualité, Théorème 3.4.1 + Démonstration (dévissage, change-of-base). |
| 33 | DONE clean | Lemme 3.4.2 stmt + proof a) p=1 (purity (μ_n)^{⊗1}_Y[-2]) / b) p≥2 sequences. |
| 34 | DONE, 1 fix + 2 emend | FIXED `A_X`→`A_{Y_p}` (dualizing sheaf on Y_p); 2 emendations kept (`A_X`→`A_{X'}` typo, "(ii) et (ii)"→"(ii) et (iii)" typo). |
| 35 | DONE clean | Cor 3.4.4 proof, Rem 3.4.5, §4 Dualité locale, §4.1 normalisation. |
| 36 | DONE, 1 fix | FIXED (4.2.2)''' `μ_n^{⊗d}`→`(μ_n)_X^{⊗d}` (dropped base subscript); §4.2 pairings match. |
| 37 | DONE clean | Exercice 4.2.3 (local duality (*) iso, RΓ_x pairings), §4.3 head. |
| 38 | DONE clean | §4.3 Lemme 4.3 + carré cartésien (checked), dualité/base-change isos. |
| 39 | DONE clean | Lemme 4.4, §4.5 start, Y/X/x̄/X' carré cartésien (checked), (4.5.1) RΓ_x̄=g^*R^!i. |
| 40 | DONE clean | §4.5 (4.5.2), K_X/K_Y/K_X'/K_x̄ setup, (4.5.3) (D_X F)_x̄ chain. |
| 41 | DONE, 2 fixes | FIXED (4.5.3)' formula (was H_Y^i×R^{-i}Γ → D_X(F)_x̄×RΓ_x̄); FIXED circular bidualité step D_x̄D_x̄→D_X D_X. Label note: (4.5.3)^bis. |
| 42 | DONE clean | Prop 4.5.4, Rem 4.5.5 (dualité globale D_Y R_!f≅Rf_*D_X), Exercice 4.5.6. |
| 43 | DONE, 1 flagged | §4.6 (4.6.1); FLAGGED induction-ordinaire line (TeX 1167) — operators/D-subscript ambiguous at native res, no change. |
| 44 | DONE, 1 emend | (4.6.1)'/'' , Exemple 4.6.2, §4.7 start; emendation kept "contenant X"→"x" (source typo). |
| 45 | DONE clean | §4.7 (4.7.1)' + (4.7.2)–(4.7.6); note j^!/j^* at (4.7.6) (equal, open j). |
| 46 | DONE clean | §4.7 (4.7.7)/(4.7.8), perfectness G=(ji)^*F, triangle (b) checked, (4.7.10). |
| 47 | DONE clean | §4.7 (4.7.10) deriv, triangle (a) checked, accouplements (4.7.12)–(4.7.14). |
| 48 | DONE, 1 fix | §4.7 (4.7.15)+Prop 4.7.16 (2 triangles checked); FIXED spurious `_x` on (4.7.15) 3rd term. |
| 49 | DONE clean | §4.7 end (Rem 4.7.17: local⇔global dualité, Poincaré-type pairing). |
| 50 | DONE clean | §5 Dualité locale sur les courbes head, Théorème 5.1 + Démonstration (5.1.1) start. |
| 51 | DONE, 1 fix | §5.1 Hochschild–Serre; FIXED s.s. abutment `H^{p+q}`→`H^*`; (5.1.2)–(5.1.6). |
| 52 | DONE clean | §5.1 (5.1.7) H^1(U,μ_n)≅A, pureté, (5.1.8), Lemme 5.1.9 stmt. |
| 53 | DONE clean | §5.1 end (Lemme 5.1.9 proof, (5.1.8)') — Exposé I §5 complete. |
| 54 | DONE, 1 fix | Bibliographie; FIXED key `[SGA]`→`[SGAA]` (citation anchor — confirms SGAA). |
| 55 | DONE, 2 fixes | Appendice (Illusie) §1.1; FIXED `A^X`→`{}_A X` (+ `\D_A(X)`→`\D({}_A X)`), `A_U`→`A_{U_i}`. |
| 56 | DONE, 1 fix | Appendice §1.2 + Prop 1.3 dévissage; FIXED "équivaut à (i) si"→"à la condition analogue où" (p56/57 boundary). |
| 57 | DONE clean | Prop 1.3 Preuve; cartesian square (U→Y/Z→X) checked. |
| 58 | DONE clean | Lemme 1.3.1 stmt + proof (Nakayama). |
| 59 | DONE clean | §2 Dimension quasi-injective (dim.q.inj ponctuelle, dim.top stricte); note `dimstop`/`dim.top`. |
| 60 | DONE, 1 fix | §2 end, §3 Complexes dualisants, §4 Pureté absolue start; FIXED `de X`→`de Y` (résid. char. of base Y in I 1.12/1.13/1.15). |
| 61 | DONE, 1 fix | §4 (4.1)/(4.2)/(4.3); FIXED spurious `+` on `\D_A^+`→`\D_A` ((4.2) extends to unbounded D). |
| 62 | DONE clean | §4 (4.3), Déf 4.4 pureté au sens fort. |
| 63 | DONE clean | §5 Prop 5.1 stmt + Démonstration start (relation (*)). |
| 64 | DONE clean | §5 proof (duality, (4.3), R Hom(M,Ri^!F)_ȳ); cartesian square (Y→D(f)/Z→X) checked. |
| 65 | DONE, 2 fixes | §5 proof end; FIXED `D(f)`→`D(f̄)` (dropped bar), `M'_x̄`→`M'` (spurious subscript). |
| 66–102, 104–484 | TODO | ordered pass continuing (p66-70 rendered in _work\src; p71-72 + 73+ need rendering) |

Next ordered-pass cursor: **source page 66** (Appendice §5 end — Cor 5.1.1, Rem 5.1.2; §6 Constructibilité de R Hom; §7 Existence de complexes dualisants — Lemmes 7.1/7.2/7.3, dense). NOTE: dedicated notation pass owes SGA→SGAA (anchored by p54 `[SGAA]`), `dimstop`/`dim.top`, AND `\D_A`→`\D({}_A X)` (the Appendice left-module category notation, cf. p55/p61).

SYSTEMATIC TODO (logged in FINDINGS): "SGA"→"SGAA" citation A-drop from ~§4.3 onward (55 `SGA~` vs 36 `SGAA~`, MIXED with legit volume refs) — needs a dedicated per-instance classification pass, NOT a bulk replace. Deferred so the math audit keeps moving.

## METHODOLOGY (refined p13-15): two kinds of discrepancy — see FINDINGS top.
1. TeX≠source & source right → fix TeX to source. 2. Source itself wrong → produce the correct
source-faithful reading, never silently copy the slip; LOG it (emendation kept if TeX already right;
erratum-flagged if TeX faithfully copied a source imprecision). Edition must be math-correct AND
document every departure from the scan.

## Autonomous loop ACTIVE — DRIVER = CRON 622c0e68 (every 2 min, set 2026-06-24)
**Sole driver now = recurring cron job `622c0e68`, fires every 2 min (`*/2 * * * *`), 7-day expiry.**
(Replaced the original `b3af5d72` which fired every 30 min — the long gaps left visible idle windows.)
Each firing: read this STATUS cursor, audit a batch (moderate is fine now — the 2-min cron makes it
near-continuous across firings), fix workpass.tex in place, log FINDINGS, advance the cursor here.
The cron's prompt CronDeletes the job when pages 1-484 are done.
NOTE: do NOT also arm a ScheduleWakeup loop — the cron is the single driver (CronList shows 622c0e68);
two drivers would race on STATUS.md. NO parallel agents / workflows (Floris's absolute no-background rule),
even with ultracode on. Continues while Floris is away.
because the 30-min gaps left visible idle windows. To stop: Floris interrupts, or CronDelete 622c0e68. Tally so far: pp.1–65 + p103;
**26 transcription fixes** (p2 pairing, p4 H→I, p10 D_c^-→D_c, p12 a(i) f_*→f_!, p13 a(ii) f_*→f_!,
p14 "démontre(ra)", p17×3 L^∨[-r]→L[r], p24 Γ^*→Γ, p26 ×_Z→×_X, p34 A_X→A_{Y_p}, p36 (4.2.2)''' μ_n→(μ_n)_X,
p41 (4.5.3)' formula, p41 D_x̄D_x̄→D_X D_X, p48 (4.7.15) spurious _x, p51 H^{p+q}→H^*, p54 biblio key [SGA]→[SGAA],
p55 A^X→{}_A X, p55 A_U→A_{U_i}, p56 "condition analogue où", p60 de X→de Y, p61 \D_A^+→\D_A, p65 D(f)→D(f̄),
p65 M'_x̄→M', p103 (4.4.2)); **6 emendations kept** (p15 D_c(F)→D_c(Y),
p16 (1.5)→(1.6), p18 H^{-i(x)}→H^{-r(x)}, p34 A_X→A_{X'}, p34 "(ii) et (ii)"→"(ii) et (iii)",
p44 "contenant X"→"x"); **3 source errata flagged, no change** (p14 Cor 1.13 chain, p16 (1.6)-for-dualisant,
p30 D_c^+(X)-for-Y); **1 flagged UNRESOLVED** (p43 §4.6 induction-ordinaire line, ambiguous at native res);
plus **1 SYSTEMATIC** (SGA→SGAA citation A-drop, deferred to dedicated pass — see FINDINGS). The two p41 fixes
were genuine corrupted formulas in §4.5 (dense duality pairings); §4.3–§4.7 otherwise solid transcription.

## Coverage truth
- 65 of 484 source pages fully audited (pp.1–65) + p103 (diagram 4.4.2). Exposé I (pp.1–72) in progress
  (Exposé I §1–§5 + Bibliographie done; in the Illusie Appendice §1–§5, p55–65+).
- 26 transcription fixes + 6 emendations-kept + 3 source-errata-flagged + 1 unresolved-flag (see tally / FINDINGS).
  (pp.61–65, Appendice §4–§5: 3 fixes — p61 \D_A^+→\D_A, p65 D(f̄) + M'; 2 cartesian diagrams checked.)
- SYSTEMATIC notation pass owes: SGA→SGAA (anchored by p54 biblio key `[SGAA]`), `dimstop`/`dim.top` (p59–60),
  AND `\D_A(X)`/`\D_A^+(X)`→`\D({}_A X)`/`\D^+({}_A X)` (the Appendice left-A_X-module category notation, cf. p55/p61).
- Errors span diagram, prose, symbol, and functor levels — confirming the full all-levels pass is
  necessary; the old diagram-only passes could not have caught the prose/symbol/functor errors.
- Do NOT claim completeness until the page table above is filled 1→484.

## Deliverables in this folder
- `sga5_fr_workpass.tex` — the cumulative LaTeX being CORRECTED in place (repair032 base + my fixes).
- `FINDINGS.md` — the logbook: every correction, with source-page evidence (the receipt).
- `sga5_index.csv` / `sga5_index.json` — machine-readable index of the whole document.
- `SOURCE_AND_RESOLUTION.md` — source file + resolution decision + page map.
- `_work\` — render + index scripts (rerunnable).

## Document scope (from sga5_index.csv, rebuild anytime via _work\build_index.py)
1141 indexed elements: **399 statements, 507 numbered formulas, 185 diagrams, 50 sections.**
Density (where errors concentrate — the math-heavy exposés):
- III (pp.73–137): 142 formulas, 60 diagrams   ← the (4.4.2) error lived here
- III B (pp.138–203): 148 formulas, 41 diagrams
- VII (pp.282–350): 99 formulas ;  XII (pp.407–441): 53 formulas ;  X: 38 formulas
- I, V, VI, VIII, XV are lighter (mostly prose).
Index `src_page_est` is interpolated (rough locator); the page-by-page audit corrects it to the true page.

## Deliverable when a batch is done
- updated `sga5_fr_workpass.tex`
- `workpass_vs_repair032.diff`
- FINDINGS.md (every change, with source page evidence)
- compile check (pdflatex ×2, page count, 0 errors) before any hand-off
