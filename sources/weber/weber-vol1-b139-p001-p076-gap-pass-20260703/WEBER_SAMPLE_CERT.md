# WEBER vol1 — 20-PAGE SAMPLE FULL-CERTIFICATION (started 2026-07-02, per Floris)

**Mandate (Floris, voice):** full-rigor by-hand check of ~20 sample pages of the NOT-yet-re-transcribed
("map-phase verified faithful" / agent-audited-only) pages; count errors; sign off with the error count; the
error rate decides how much further re-certification is warranted (clean → minimal/"one recert"; errors bad or
a couple small → escalate to broader/full re-cert).

**Method per page:** render `chunk_page.py 1 P` (top/mid/bot) [zoom via crop_src.py for any doubtful glyph];
read each chunk in full; locate the corresponding `.tex` span (Grep a distinctive phrase); compare
symbol-by-symbol (text + every equation + every subscript/index + orthography); classify each finding:
 - **A** = real .tex deviation from Weber (dropped/added/wrong content or symbol) → would fix
 - **B** = a Weber print-typo the .tex faithfully reproduces OR silently "corrected" → flag (already-handled ⇒ note)
 - **cosmetic** = immaterial (kerning, glyph-degrade) → ignore
Count A-findings as the error metric.

## SAMPLE PAGES (20) — spread across the un-re-transcribed regions
Buch I–II (§1–137, the bulk agent-audited-only region; avoids §69 p212-215 which was re-transcribed):
 p20, p40, p65, p90, p115, p140, p165, p190, p230, p260, p290, p320, p345, p375, p400, p420
Buch-III "faithful islands" (map-phase verified, not re-transcribed):
 p485 (§151), p510 (§157), p544 (§164), p580 (§171/§172)

## RESULTS (per page: A-errors / B-flags / notes)
_(cursor: filling in batches; running A-error total at bottom)_

**BATCH 1 (2026-07-02): p20, p40, p65 — CERTIFIED.**
- **p20** (Einleitung, .tex 460-464): **1 minor-A** — .tex "können von zweierlei Art sein**:** entweder" but
  Weber prints "sein**;** entweder" (semicolon). +1 BORDERLINE (likely systematic file style, not counted as a
  per-page error): .tex ` ``Unbekannte'' ` (renders English " ") vs Weber „Unbekannte" (German quotes). All
  prose otherwise verbatim-faithful; no dropped/fabricated content.
- **p40** (§7 Erster Abschnitt, .tex 1088-1127): **0 errors.** Every eq exact — Vieta (x-α₁)(x-α₂)=…,
  the 3-factor expansion, eq(3) aᵥ=a'ᵥ-α_n a'_{ν-1} recursion (incl. a_n=-α_n a'_{n-1}), eq(4) binomial
  B_ν^{(n)}=B_{ν-1}^{(n)}(n-ν+1)/ν — all match; all prose verbatim.
- **p65** (§19 Permutationen, .tex 2228-2242): **0 substantive.** eq(3) 𝔄'=α₁,α₂…α_n, Fraktur \mathfrak A/A',
  Transpositionen prose, (1,2,3,4)→(4,3,2,1) example all faithful. +1 BORDERLINE systematic: `\S~7` renders
  "§ 7" vs Weber "§. 7" (missing period in §-ref — likely a file-wide \S-ref style, not counted).

**BATCH 2 (2026-07-02): p90 — ★ MAJOR FINDING.**
- **p90** (§26 Zweiter Abschnitt, linear-eqn solution, .tex 3018-3057): **★ REFORMULATED PAGE (multiple type-A).**
  The .tex does NOT match Weber's printed p90:
  1. **Index re-lettered**: Weber fixes index **k** (running index **i**): "Ist k einer der Indices…",
     $A_i^{(k)}$, $A_k^{(1)}\ldots A_k^{(n)}$, $x_k$. The .tex uses **μ** (running **k**): $A_\mu^{(k)}$, $x_\mu$.
  2. **Sums MODERNIZED**: Weber prints $\Sigma^i$ (index-above, no range) in eqs (3),(4); the .tex has
     $\sum_{k=1}^{n}$ (modern range). Violates the de-modernize-sums house convention.
  3. **★ Solution REFORMULATED (α dropped)**: Weber prints "Setzen wir $A_k^{(i)}=A\,\alpha_k^{(i)}$" then eq (5)
     "$x_1=\alpha_1^{(1)}y_1+\alpha_1^{(2)}y_2+\cdots+\alpha_1^{(n)}y_n$" (normalized cofactors α, solving x_i).
     The .tex has "Setzen wir $A_\mu^{(k)}=A_{k\mu}$" then eq (5) "$A x_1=A_{11}y_1+A_{12}y_2+\cdots$" — the
     entire α-notation is ABSENT; replaced by a two-index $A_{ik}$ minor + un-normalized $A x_i=\ldots$.
     **600-dpi zoom (vol1_p090_crop_20_55) confirms Weber's α + x_i= form unambiguously.** Mathematically
     equivalent but NOT Weber's printed presentation.
  4. Minor rewords: "worin die Coëfficienten … betrachtet werden" → .tex "Darin werden die Coefficienten …
     betrachtet"; "…in die Augen fällt" → .tex "fällt dabei in die Augen".
  eqs (1),(2),(6+) and the surrounding prose otherwise match. **⇒ §26 is a partial GPT-reformulation that the
  agent-map phase missed** — needs re-transcription to Weber's k/i + Σ^i + α form. Counts as a MAJOR type-A page.

- **p115** (§34 Befreiung vom zweiten Gliede, .tex 3910-3954): **0 errors.** eqs (1) f(x)=xⁿ+a₁xⁿ⁻¹+…,
  (2) x=y−a₁/n, binomial xⁿ/xⁿ⁻¹/xⁿ⁻² expansions, f(x)=yⁿ+(a₂−(n−1)/2n·a₁²)yⁿ⁻²+…, (3) φ(y) for n=2/3/4,
  and ALL a,b,c coefficient formulas match exactly; prose verbatim.
- **p140** (§42 Vierter Abschnitt, symmetric functions, .tex 4940-4946): **0 substantive.** eq (2)
  f(x)=xⁿ+a₁xⁿ⁻¹+…+a_{n-1}x+a_n, Grundfunctionen prose (a₁=−Σα etc.) all match. +1 BORDERLINE systematic
  (`\S\,1`→"§ 1" vs Weber "§. 1.").

**BATCH 3 (2026-07-02): p165, p190, p230 — all CLEAN.**
- **p165** (§51 Zerlegbare/unzerlegbare Functionen, .tex 5883-5893): 0 errors. UV+U'V'+U''V''+… divisibility
  prose, "w geht in W auf", theilerfremd def, Satz I (\Roman*.) all match. (1 immaterial: .tex "+\cdots" vs
  Weber "…" in the UV-sum.)
- **p190** (§61 Fünfter Abschnitt, binary forms, .tex 6804-6832): 0 errors. eqs (6) xβ₁−yα₁=(xβ₁), (7)
  x₁y₂−x₂y₁=(x₁y₂), (8) bracket-abbrev system, (9) linear subst x=αx'+βy'/y=γx'+δy', (10) r=αδ−βγ all match.
- **p230** (§74 Transformation der Gleichung fünften Grades, .tex 8561-8583): 0 errors. §74 title, "im §54
  skizzirt", Bezoutiante t₂=0/t₃=0, quadratic B_{0,0}t₀²+2B_{0,1}t₀t₁+B_{1,1}t₁²=0, √(B_{0,1}²−B_{0,0}B_{1,1}),
  Hauptgleichung/F. Klein prose all match.

**BATCH 4 (2026-07-02): p260, p290, p320.**
- **p260** (§81 end / §82 opening, .tex 9623-9625): **0 errors.** π,ν,ϱ inertia prose (ϱ=\varrho ✓,
  φ=\varphi, Φ=\Phi), §82 title match exactly.
- **p290** (§95 Charakteristik/Schnittpunkte, Achter Abschnitt, .tex 10847-10855): **0 prose errors.** §95
  title, E(φ,ψ)/A(φ,ψ)/E(f;φ,ψ)/A(f;φ,ψ) prose match; **Fig. 10 present as tikzpicture** (geometric fidelity
  per the map-phase diagram pass, not re-verified here).
- **p320** (§106 Rolle'sches Theorem, Neunter Abschnitt, .tex 11758-11773): **1 minor-A** — scan "einmal**,**
  oder allgemeiner" but .tex "einmal oder allgemeiner" (dropped comma). eq (2) [(x−α)(x−β)f'(x)]/f(x)=a(x−β)+
  b(x−α)+(x−α)(x−β)f₁'(x)/f₁(x), the sign-argument prose, and Satz XII (quote block) all match.

**BATCH 5 (2026-07-02): p345, p375, p400.**
- **p345** (§111 Gräffe'sche Näherungsmethode, .tex 12710-12723): **1 minor-A** — scan "eine noch bessere**,** als
  bei dem" but .tex "eine noch bessere als bei dem" (dropped comma). eq (1) $\sqrt[m]{\alpha^m+\beta^m+\gamma^m+
  \cdots}$, the Encke footnote `\footnote{Crelle's Journal, Bd. 22 (1841).}`, and the quotient
  $[\alpha^m+\cdots]/[\alpha^{m-1}+\cdots]$ all match. ("gegeben" at scan top is the page-break tail of "an-gegeben".)
- **p375** (§120 Aequivalente Zahlen, continuation, .tex 13895-13918): **0 errors.** eq (4) matrix product
  $y=(\alpha,\beta;\gamma,\delta)(P_n,P_{n-1};Q_n,Q_{n-1})(x_n)=(R_n,\ldots)(x_n)$, eq (5) $R_n=\alpha P_n+\beta Q_n$
  system, eq (6) $R_nS_{n-1}-S_nR_{n-1}=(-1)^n\varepsilon$, and $S_n=Q_n(\gamma P_n/Q_n+\delta)$ all match; prose
  verbatim; §-ref "§. 120" carries its period. (Substitution-bracket commas rendered as clean pmatrix = consistent
  cosmetic.) NB running head shows "§ 121" — running heads are not authoritative; content on this page is §120's tail.
- **p400** (§128 Elfter Abschnitt, Pell'sche Gleichung, .tex 14934-14944): **★ 1 real-A content omission + 1 comma.**
  1. **★ DROPPED CLAUSE**: Weber "…sind, liefert. **Dies ist aber sehr einfach; denn** ist $\Theta_1$ irgend eine…"
     → the .tex had dropped "Dies ist aber sehr einfach; denn " and re-capitalised to "liefert. **Ist** $\Theta_1$…".
     **FIXED** (restored clause + lowercased ist). First real content drop in a "faithful island" since §26/p90.
  2. minor comma: scan "genügt dazu**,** zu zeigen" vs .tex "dazu zu zeigen" — **FIXED** (restored comma).
  eq $\Theta=(T+U\sqrt D)/2$, the $\pm\Theta^n$ prose, and the $\Theta^n\le\Theta_1<\Theta^{n+1}$ chain all match.
  (Borderline uncounted: .tex "kleiner als $1$**,** und" vs scan possibly no comma — too faint to confirm, left.)

**BATCH 6 (2026-07-02): p420, p485, p510, p544, p580 — SAMPLE COMPLETE.**
- **p420** (§134 Zwölfter Abschnitt, cyclotomy, .tex 15528-15532): **0 errors.** βᵃ/β/α cyclotomy prose, ϱ=\varrho ✓
  (both instances), "φ(x) stimmen … überein mit … X_n", "nicht in Factoren niedrigeren Grades … zerlegbar" all
  match. (Coëfficienten→Coefficienten ×3 = house ë-drop.)
- **p485** (§151 Imprimitive Körper, .tex 17427-17437): **0 errors.** eq (5) intro prose, eq (6) ω=Φ(Θ)/φ'(Θ),
  eq (7) (u−α)(u−α₁)⋯(u−α_{r-1})=φ(u,Θ) [r-1 subscript ✓, distinct from n-1 in the intro list] all match.
- **p510** (running head §155, Vierzehnter Abschnitt — sample list said "§157", MISLABEL; content is §155, .tex
  18169-18171): **0 errors.** R=Durchschnitt(Q,Q') def, π₁π₂ closure, ω=xψ+x'ψ' construction all verbatim.
- **p544** (§164 Fünfzehnter Abschnitt, Lagrange resolvents, .tex 19159-19173): **★★ MAJOR CONDENSED RECONSTRUCTION.**
  Was NOT in the held-list and NOT flagged — a GAP (§163 & §165 were held, §164 slipped between). The .tex:
  1. **Dropped display eq** after "Macht man … Permutation π": Weber "so ergiebt sich nach 1. [$\Sigma^\varepsilon
     \varepsilon^{-k-\nu}(\varepsilon,\alpha)^\nu$], d. h. A_k^{(ν)} geht…" → .tex "so **geht** A_k^{(ν)}…" (eq gone).
  2. **Reworded** "Der Satz 2. ist ein specieller Fall eines allgemeinen Theorems. Entwickeln wir ein Product…"
     → "Noch allgemeiner entwickle man…"; dropped the standalone product display + the "worin ν,ν₁,ν₂… positive,
     λ₁,λ₂… beliebige ganze Zahlen sind, und ordnen es… nach Potenzen von ε, so mag sich ergeben" prose.
  3. eq (7) sum **modernized** `\sum_{h=0}^{m-1}` vs Weber's index-above Σ^h_{0,m-1} (even inconsistent with eq (5)
     at 19146 which correctly uses `\sum_{0,m-1}^{h}`).
  4. **Dropped the whole B_k derivation**: Weber "…Formen **von der Variablen α** sind. Da auch diese Entwickelung
     für alle m^ten Einheitswurzeln ε gilt, so kann man die Formel (2) anwenden und erhält [B_k=Σ^ε ε^{-k}(ε,α)^ν
     (ε,α^{λ₁})^{ν₁}…], woraus man nach 1. schliessen kann, dass B_k durch die Substitution π in [B_{k+ν+λ₁ν₁+…}]
     übergeht. Wir haben also:" → .tex "Dann sind die B_h von ε unabhängige Formen, und die Substitution π führt
     B_h in [B_{h+…}] über." (drops "von der Variablen α", the derivation eq, k→h relettered).
  5. **Dropped the formal enumerated Satz 3** "3. Die Permutation π, auf die Indices der α angewandt, ruft unter den
     Indices der Coëfficienten des nach ε geordneten Productes [eq (8)] die Permutation π^{ν+λ₁ν₁+λ₂ν₂…} hervor."
     → replaced by one-line "In diesem Satze liegt die allgemeine Form der Lagrange'schen Rechnung."
  6. **Dropped** the "In diesen Theoremen kann die Permutation π wiederholt werden; sie bleiben richtig, wenn π durch
     irgend eine Potenz von π ersetzt wird…" paragraph (Weber p544 bot). ⇒ §164 needs FULL re-transcription (spans
     ~p543-p546). Counts as a MAJOR type-A section. **Proves the Phase-2 "§141→§188 section-by-section complete"
     claim is unreliable — this section was never properly done.**
- **p580** (§172 Sechzehnter Abschnitt, worked example — log claimed "FULLY re-transcribed", .tex 20595-20630):
  **3 type-A (all FIXED).** Eqs (6),(7) and BOTH index tables (n=7: I=0,2,1,4,5,3; n=13: I=0,1,4,2,9,5,11,3,8,10,7,6)
  faithful, but connective prose reworded: (a) "worin"→.tex "wobei" [FIXED]; (b) "Beispielsweise erhält man für
  n=7,13, **wenn man die primitiven Wurzeln 3,2 zu Grunde legt** und die Indextabellen anwendet:" → .tex "Für n=7,13
  liefern die Indextabellen zum Beispiel" (dropped the primitive-roots clause) [FIXED]; (c) "für n=7,"/"für n=13,"
  labels → .tex "n=7:"/"n=13:" [FIXED]. Even a "re-transcribed" section kept reworded glue.

## ★ SIGN-OFF (2026-07-02) — 20/20 SAMPLE PAGES CHECKED
**ERROR COUNT (per Floris's mandate — count first, then decide re-cert depth):**
- **2 MAJOR reconstructed/reformulated sections**: **§26 (p90)** [reformulated: index re-lettering, modernized sums,
  α-normalization dropped] and **§164 (p544)** [condensed: 6 distinct drops/rewords, dropped display eqs + formal
  Satz 3]. Both need FULL re-transcription. NEITHER is currently faithful.
- **2 real content drops (both FIXED this pass)**: p400 (dropped "Dies ist aber sehr einfach; denn" clause);
  p580/§172 (dropped "primitiven Wurzeln 3,2 zu Grunde legt" clause + 2 rewords).
- **4 minor punctuation (p20 semicolon; p320, p345, p400 commas)** — p400's FIXED; p20/p320/p345 left (immaterial,
  systematic comma-dropping in the un-re-transcribed prose).
- **12 pages fully clean**: p40, p65, p115, p140, p165, p190, p230, p260, p290, p420, p485, p510.
- 2 borderline-systematic style items (English-vs-German quotes; \S-ref missing period) — NOT per-page errors.

**VERDICT: NOT CLEAN → ESCALATE (per Floris's rule "if the errors are bad … escalate").** The sample proves the
"map-phase verified faithful" AND the Phase-2 "§141→§188 complete" designations are BOTH unreliable: §164 (thought
faithful) is a heavy reconstruction; §172 (claimed re-transcribed) kept reworded prose; §26 (Buch-II) is reformulated.
Error concentration is in the **theory/prose glue**, not the equations (equations were mostly faithful even in the bad
sections). **This is exactly the "never certify — completeness claims are always wrong" pattern.**

**ESCALATION PLAN (executing, not checkpointing):**
1. ✅ **DONE** — Re-transcribed **§26 (p90)** to Weber's k/i indices + Σ^i index-above sums + α-normalization.
   (.tex 3028-3057; renders correct; compiles.)
2. ✅ **DONE** — Re-transcribed **§164 (p542-p545)** fully to Weber's printed form: restored dropped display eqs,
   Satz 3 + eq (8), Satz 4, the B_k and E_k/G_k developments, the period-grouped (ε,α) expansion; fixed 6
   index-below→above sums, the "e-gliedrige"→"f-gliedrige" error, the \\alpha typo, and the spurious ¶ break;
   preserved the ε² erratum (#23). File 416→417 pp. Output-PDF pp345-347 eyeballed. Compiles 417pp/0 badness.
3. ⏳ **IN PROGRESS** — **Re-verify §141-188 page-by-page** (the range whose "complete" claim is disproven) — do
   NOT trust it; grind each section's PROSE against scans (equations were mostly ok; prose is where rewording hides).
   Cursor lives in WEBER_METHOD_LOG.md. Next: §141, §148-156, §158, §162-163, §165, §166-170, §173-188 — verify
   each was ACTUALLY re-transcribed vs. only claimed. Also re-check §157/§159-161 (patched worked-example islands).
4. ⏳ Re-check the other Buch-III "faithful islands": §150, §151✅clean(sample), §155✅clean(sample),
   §171✅clean(prior spot-check), §183✅clean(prior spot-check). §164 was the mislabeled one; §172 had reworded glue.
5. pdflatex gate after each fix batch (page count must not drop; growth from restored content is expected).
**Pattern holds: §26 is the only reformulated island; 10 other sections faithful (minor punctuation slips only).**
Remaining: p345, p375, p400, p420, p485, p510, p544, p580. Plus 2 borderline-systematic style items
(English-vs-German quotes; \S-ref missing period) — NOT counted as per-page errors; if confirmed systematic
they'd be single global-style decisions, not page-errors. **Trend: the "faithful" pages are genuinely faithful
— only rare minor punctuation slips, zero content/math errors so far. Sign-off pending remaining 17 pages.**
Remaining: p90, p115, p140, p165, p190, p230, p260, p290, p320, p345, p375, p400, p420, p485, p510, p544, p580.
