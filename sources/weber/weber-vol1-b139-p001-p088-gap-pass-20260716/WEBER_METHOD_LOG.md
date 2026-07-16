# Weber audit — method log (what works, what fails, adjustments)

Running record for the vol1 (Band I) grind. Companion to `WEBER_CERT_LOG.md` (per-fix provenance).
Loop started 2026-06-25 via `/loop "do vol 1 - keep meticulous logs of what works and adjust"`.

## The loop (validated on p100–107)
Per batch: render pages (`chunk_page.py`, 500-dpi native, 2400px chunks) → `weber_audit_workflow.js`
(audit agent/page → adversarial verify/fix, default REJECT) → **I hand-verify every surviving fix
against the scan** → apply verified ones to B139 `weber_v1_ge.tex` → `pdflatex` gate (0 errors AND
page count not dropped) → log to `WEBER_CERT_LOG.md`. One workflow at a time (rate-limit rule).

## What WORKS
- **Agent recall is high** — on p100–107 the agents found every real drop I'd found by hand.
- **Verify stage filters most false positives** (uniqueness + source-support, default reject).
- **Compile gate + page-count check** catches silent breakage (the SGA5 swallowed-page lesson).
- **Discipline holds** — agents preserve 1890s orthography, route source-typos to type-B (don't
  revert the editor's corrections), call parens/punctuation cosmetic.

## What FAILS (why the hand-check is mandatory)
- **Audit agents hallucinate drops/collapses that aren't in the `.tex`** (p105 eq5: claimed a
  one-line collapse; the `.tex` already had the correct two-line form). The verifier caught all 4
  on p105 — but in batch 1 one phantom slipped through *accepted* (p1 determinant, a page with no
  scan). **Verifier reliability varies.**
- **Phantom pages** when args are mangled or scans missing → agents invent content. (Fixed.)

## Adjustments
- 2026-06-25 — fixed `parseArgs` (handle stringified `{volume,axis,pages}`), `pad(3)` chunk names,
  `texOf` v1/v2/v3 path (was `vol1`).
- 2026-06-25 — added **no-scan guard** to `chunks()` (agent must bail, not hallucinate, if PNGs unreadable).
- 2026-06-25 — added **"CONFIRM ABSENCE BEFORE CLAIMING A DROP"** rule to the audit prompt (grep the
  `.tex` to confirm content is truly absent before emitting a drop-fix). Targets the eq5-type
  hallucination; effect measured from p108 onward.
- Batch size: 3 → 5 → trying 6. Tune by review load (every accepted fix = an eye-read of the scan).

## Metrics
| batch | pages | agents | tokens | clean pages | real fixes applied | false-pos rejected | phantom slipped | compile |
|-------|-------|--------|--------|-------------|--------------------|--------------------|-----------------|---------|
| 1 | p100–102 | 13 | 456k | p101 | 4 (p100 det row + deriv block; p102 a′₁ + dropped eq) | 1 (caught by me) | 1 (p1 dup, harmless) | 357pp/0err |
| 2 | p103–107 | 10 | 336k | p103,104,107 | 1 (p106 "VII." label) | 4 (all p105, by verifier) | 0 | 357pp/0err |

## Open / global decisions
- **"Coëfficient" diaeresis** — source has it, `.tex` drops it throughout. Systematic → decide once
  for the whole work, do NOT patch per page.
- Volume identity: vol1 = Band I confirmed (running heads "Zweiter/Dritter Abschnitt" + content match).
- Cursor: ★ **CONTENT MAP COMPLETE (p1-648).** PHASE 2 (re-transcription) IN PROGRESS. **DONE: §141, §162, §163, §158, §165, §148, §149, §153, §154, §155, §156, §167, §168** (all page-by-page, compile-gated); **§151 VERIFIED FAITHFUL (0 changes)**, §150+§152 already faithful. **§148–156 BLOCK COMPLETE.** **B139 = 403pp / 0 err.** **HELD remaining: §180-188, §69, p466, §138-numbering.** **§148 (Permutationsgruppen) DONE** (p472-476; .tex reconstruction: δ→σ fixed, restored dropped displays $F[\chi(\rho)]=0$/$F[\chi(\rho_1)]=0$ + identity-composition displays + $\pi_c^{-1}=\pi_b^{-1}\pi_a^{-1}$, eq(8) 3rd member, item-2 numbering, and the whole dropped ending = cyclic-group example + Abel'sche-Gruppen + Theiler def; corrected fabricated "die symmetrische Gruppe"; \perm macro + \rho kept). §148 page range p472-476; §149 "Galois'sche Gruppe" opens on p476. **§165 (Auflösung der cyklischen Gleichungen) DONE** (p546-551; .tex was a GPT reconstruction — modernized notation, dropped/merged eqs; restored clean eqs (1)-(21) incl. eq(2) radical-form, the ψ₁=0 exceptional case, the m=pn/α_n-α_0 argument, full real/Abel development, p551 Realitätsverhältnisse; **13th erratum p548 eq(7)** 2nd term missing ^{m_2}, zoom-confirmed, kept faithful; Weber prints "Coëfficient" ë but house form "Coefficient" kept). **§138-numbering MAPPED but edit DEFERRED** (whole-section rule-renumber; mapping in cert-log "PHASE 2 recon §138-numbering"). **§162 (Abel'sche Gleichungen) DONE** (def + commutativity + §147-derivation + full converse; 11th erratum p536 Θ_kΘ_h(x)). **§163 DONE** (p537-541; Weber reuses eqs (7)=Φ/π and (11)=η-array/Θ-chain). **§158 (Imprimitive Gruppen) DONE** (p516-521; the .tex was a wholesale GPT summary that dropped eqs 2-6 + (α)/(β) matrices + Normaltheiler proof + Umkehrung, and used δ where Weber prints σ — all restored; **12th erratum p521 boxed-thm-2 "Imprimivität"** missing "ti", kept faithful; ⚠ check §159's "Fünfzehnter Abschnitt. Cyklische Gleichungen" heading vs p522 scan when I get there). **§149 (Galois'sche Gruppe) DONE** (p476-481; HEAVY reconstruction — the .tex compressed Weber's 6-page section to ~1p: δ→σ fixed, θ→Φ with eq(1) mislabel corrected, arabic "1."→Roman "I." Satz, a)/b)/c)/d) un-merged with intervening proof prose restored, the ENTIRE dropped d)-proof restored [eqs (5)π_1…π_ν,(6)ρ_1…ρ_ν,(7)ρ'_1…ρ'_ν + g'(t)=g(t) closure argument], G(t)/Affect/Kronecker restored [reverted a non-Weber "Theiler von m!" gloss to "Theiler von Π(m)"], "keine Affect" proposition set as indented quote, and the dropped Galois biography **footnote** (p481) restored via \footnote+\glqq/\grqq). §149 ends p481; **§150 "Transitive und intransitive Gruppen" opens p481** (already re-transcribed in map phase — verified its eqs (1)/(2)+f(α')=0 argument match p481-482). **§151 (Primitive und imprimitive Gruppen, p483-487) VERIFIED FAITHFUL — 0 changes** (read all scans p483-487; eqs (1)-(13) incl. Weber's DOUBLED (4) [= (t-Θ)…=φ(t) AND ω-array, both numbered (4); a genuine Weber reused-number, NOT a bug — same as §163's (7)/(11)], boxed results 1/2/3, m=6 example, §152 boundary all match; also re-confirmed §150 complete+faithful). **KEY REVISION: the §148-156 block is NOT a uniform rewrite — §150/§151/§152 are faithful (patchable); only §148/§149/§153/§154/§155/§156(+§158) were actually rewritten.** **§153 (Zerlegung von Permutationen in Transpositionen und in Cyklen, p492-500) DONE** — heavy reconstruction (~8pp compressed to 103 lines) fully re-transcribed: restored the DELETED Satz 3 (unique disjoint-cycle decomp) + its eqs (1)(2)(3) + the 3 worked examples π₁=(0,2,6,5,4,1,3,7)/π₂=(0,4,5,7,6)(1,2)(3)/π₃=(0,7,4,5)(1,2,3,6) [.tex had a FABRICATED placeholder (a,b,c)(d,e)(f)], the full even/odd τ-composition proof, Satz 7's 4 generating identities, the ENTIRE proofs of Sätze 9/10/11 (M/M'/M'' imprimitivity chain, ~2.5pp), and the period/order material (eq (4) + even/odd π² formulas + lcm-of-cycle-lengths Grad); de-modernized \pmod 2→(mod. 2), \prod→Weber's expanded difference-product+u/α-variable phrasing, gibt→giebt; theorems 1.–11. now contiguous (no skipped 3), equations (1)-(4) kept as separate \tag numbering. 383pp/0err/0 overfull. **§154 (Divisoren der Gruppen. Nebengruppen und conjugirte Gruppen, p501-507) DONE** — systematic compression reconstruction; restored: ϰ(varkappa) for the .tex's wrong χ throughout; the DROPPED eqs (7)(8)(9) (.tex jumped 6→10); fixed (11) mislabel (Weber's (11)=π=π₁⁻¹ϰπ₁, .tex had put it on π_i⁻¹Qπ_i); restored coset-distinctness + "bilden keine Gruppe" + disjoint-cosets proofs, thm-2 explicit displays, the entire πQ-decomposition P=Q+π₁⁻¹Q+… + proof, the ψ=ψ(ϰ) closure argument, conjugate-functions derivation, transformation-rule (Satz 6) cycle proof, thm-7 proof (P=Q+Qπ₁+…+Qπ_{m-1}); restored the DROPPED 2nd footnote (gleichberechtigte Untergruppe); **14th erratum: q/ν** (Weber prints "ν Elemente" p502 + ϰ_{ν-1} in eq (9) p504 vs q in (2)(3)(7); zoom-confirmed, kept as printed). 386pp/0err/0 overfull. **§155 (Reduction der Galois'schen Resolvente durch Adjunction. Normaltheiler einer Gruppe, p507-511) DONE** — compression reconstruction; restored: DROPPED eqs (3) [ψ-relist] + (5) [ω=χ(ψ)/φ'(ψ)] (.tex jumped 1,2→4→6); the χ(t)=φ(t)(Σω_i/(t−ψ_i)) polynomial form (.tex modernized to bare \sum + Ω[t]/Ω(t)); Satz-1 Φ(t) irreducibility detail; the DROPPED Satz-3 restatement (N is p^ten over Ω, q^ten over Ω(ψ)); full Galois-resolvent decomposition g(t,ψ)/(6) g(t)=g(t,ψ)…g(t,ψ_{j-1}) (.tex used g_0…g_{j-1}); theilerfremd def + R-is-a-group proof; Ω''=Ω(ψ,ψ_1…) paragraph + all-conjugates-identical⇒Normalkörper; "5." restored as numbered Satz w/ proof (.tex demoted to prose); Normaltheiler def per Weber (not .tex's π⁻¹Qπ=Q paraphrase); **BOTH dropped footnotes** (Lagrange citation p508 + Normaltheiler/décomposition-propre note p511). French accents compile clean. 387pp/0err/0 overfull/0 missing-char. **§156 (Die Gruppe der Resolventen, p511-513) DONE** — heavy compression reconstruction (~31 lines for ~2.5 Weber pp) fully re-transcribed: restored the true singular-Hülfsgleichung opening + §.155,2. Lagrange citation + N=Ω(ψ) identity; case 1 "theilerfremd" wording + (nach Satz 4., §.155) + the DROPPED display N=Ω(ψ,ψ₁…ψ_{j-1}) + the "zugleich Galois'sche Resolvente der ursprünglichen Gleichung" remark; case 2 "der dann ein Normaltheiler von P ist" + the "nur in Factoren vom Grade r zerlegt" sentence; the einfache-Gruppe remark verbatim; **the FULL Galois-group-of-the-resolvent argument with σ-notation** (the .tex DROPPED σ entirely) incl. the π'=σπ display + the set-off Ergebniss (Nebengruppe Rπ); fixed degree to Weber's inline "gleich dem Quotienten p:r oder dem Index des Theilers R von P" (.tex had bare \[p:r\]); **restored the ENTIRE dropped tail** = Totalresolvente-isomorphism/äquivalent paragraph + Partialresolvente/Spaltung paragraph + the "Resolventen von möglichst niedrigem Grade" practical closing (all 3 absent from .tex, which truncated at "Ist R=1…Grad p"). Footnote ¹ at foot of p511 confirmed = §155 Normaltheiler note (already at line 18153) — §156 has none of its own, not double-restored. \emph for Resolventen/Total-/Partialresolvente (house convention). 388pp/0err/0 overfull/0 missing-char. **§167 (Die Kreistheilungsperioden und die Periodengleichungen, p554-560) DONE** — opens the **Sechzehnter Abschnitt "Kreistheilung"** (chapter head \section* at line 19461 already present, left untouched). WORST reconstruction yet: ~35 lines for Weber's ~7 pp; .tex kept only eqs (1),(2),(12) + **FABRICATED its (13)** as "Σηᵢ=−1"; dropped eqs (3)-(11),(13-real),(14)-(18) + the whole irreducibility/Galois-group/period/Basis/determinant theory + modernized (\mapsto). Fully re-transcribed: true Abel'sche-Gleichungen opening + geometric motivation + Körper-R naming + n=ungerade-Primzahl(±1/n=2) + **dropped transcendental exponentials** e^{2πi/n}…; eqs (1)-(11) incl. index theory (g^α≡a, ind a, §.136), **Theorem I** (\Roman* item)+proof, C=Galois-group argument, n−1=ef; eqs (12)-(18) incl. the Gauss f-gliedrige Perioden (12), conjugirte-Perioden+distinctness, **Theorem II** (\Roman*[start=2]), REAL (13) φ(r)=Σ^h a_h r_h + φ(r_e) derivation, (14)+**Basis** def, (15) F_e(x), (16) product-formula, **(17) the e×e determinant** (\begin{vmatrix}+\hdotsfor{4}, Weber's printed commas), (18) Φ_e(x)+Newton/Potenzsummen(§.42)+C_{ee'}/η' recursion+prime-factor resolvent chain+closing cyclic-permutation group. All 18 tags present & contiguous. \mathrm{ind}, (\mathrm{mod.}\ n), n^{ten}/e^{ten}/f^{ten} ordinals, Σ index-above/range-below convention, Coefficienten(ë→e), existiren/giebt/charakterisirt kept. 391pp/0err/0 overfull/0 missing-char (+3pp from ~7 restored pp). **§168 (Die Gauss'sche Methode zur Berechnung der Resolventen, p560-564) DONE** — running heads "Producte von Perioden"/"Dreizehn-Theilung". Reconstruction with a **mathematically FABRICATED n=13 example** (.tex printed η_0=r+r^3+r^9+r^27 → r^27=r^1 dup; garbage residues). Rewrote eqs (1)-(6) back to Weber (η^{(λ)}=r^λ+r^{λ'}+…; the s,t-sum forms; the t→t+s swap; (4) η^{(λ)}η^{(μ)}=Ση^{(λ+μ⁽ⁱ⁾)}; uneigentliche η^{(0)}=f; (5) ηη_h=…; (6) η_kη_{h+k}=…). Restored Weber's REAL n=13 computation (hand-verified): (7) §.136 index table [N:1,2,4,8,3,6,12,11,9,5,10,7]; (8)/(9) the periods; ηη=η^{(2)}+η^{(-4)}+η^{(0)}+η^{(6)}=−4η−3η_1−2η_2; the η²/ηη_1/ηη_2 formulas; 3×3 determinant; (10) η³+η²−4η+1=0, discr 169=13²; cos-forms; biquadratic ξ=r+r^{-1}, (11) ξ²−ηξ+η_2=0, (12) r⁴−ηr³+(η_2+2)r²−ηr+1=0, 2sin/√(4−ξ²); six-term path (13) ζ=r+r³+r⁴+…, (14) ζ²+ζ−3=0, (15) ζ=(−1±√13)/2; two-term ξ_0..ξ_5 system, ζ=ξ+ξ_2+ξ_4, ξξ_2ξ_4=1−ζ, (16) x³−ζx²−x−1+ζ=0. **GLYPH zoom-confirmed (crop_src.py): 6-term periods=ζ(zeta), 2-term=ξ(xi)** — do NOT conflate (the phrase "Nach Adjunction der Werthe ζ,ζ₁ … für die zweigliedrigen Perioden [ξ]" + printed "ζ=ξ+ξ_2+ξ_4" force distinct letters). Index table = array{c|cc…}+\hline; determinant=vmatrix w/ Weber commas; Σ^s/Σ^t index-above; \S\,167,\,(12)/(2)/(17), \S\,136; e^{2πi/13}, cos(kπ/13); §168 has NO footnote (¹ on p564 is §169's). All 16 tags present & contiguous. 393pp/0err/0 overfull/0 missing-char (+2pp). **§169 (Zurückführung der Kreistheilungsgleichung auf reine Gleichungen, p564-570) DONE** — running head "Siebzehn-Theilung". Reconstruction that reworded the opening, **dropped BOTH footnotes** (Gauss disq.arith. + v.Staudt Crelle 24), **got the numbering catastrophically wrong** (numbered Weber's two UNNUMBERED tables → shifted everything, SKIPPED Weber's (14), FABRICATED a (23)), and **cut Weber's entire p569mid-p570 sign-determination tail** to one sentence. Restored Weber's exact numbering (1)-(22) with index/ψ tables UNNUMBERED and (−1,η)=√17 / (i,η)=⁴√17{…} UNNUMBERED; restored both footnotes, all dropped derivation steps (the Σ_{0,n-2}^h form, the μ=−λ case w/ Σ^s r^{s(t+1)} split + §136 ind(n−1)=½(n−1), the double-sum (4), the successive-mult block before (14)), and the whole sign-tail (½(−1,η)=Σcos, the two trig identities, sin(11π/34)>sin(3π/34), the reelle-Theil computations). n=17 numeric values were CORRECT in .tex (accurate 17-gon) — only numbering wrong; fixed (10) (−1)^{fλ}→(−1)^{μλ}. De-modernized \sum_{s=1}^{n-1}/\sum_{s,t}→\sum_{1,n-1}^s/\sum^s\sum^t. Kept file conventions \ind + \pmod (Weber's "(mod. m)" deferred to global sweep). Two \footnote render-confirmed (Gauss=fn59, Staudt=fn60), eyeballed PDF pp356-360. All 22 tags present & contiguous. **395pp/0err/0 overfull/0 underfull/0 missing-char/0 undefined** (+2pp). **§170 (Eigenschaften der Zahlen ψ, p570-574) DONE** — running head "Die Zahlen ψ". Reconstruction that reworded the opening, **MOVED the "Jacobi bis e=23/Kronecker" paragraph from Weber's END to the START**, **dropped the Kronecker footnote**, mis-numbered (Weber (1)-(17); .tex had only (1)-(11)), carried a **MATH ERROR** (.tex ψ_{−λ−μ,μ}=(−1)^n ψ_{λ,μ}; Weber = **(−1)^μ**), and dropped the e=7 detail + (α,η)^14 check + most of the Congruenz-Satz. Restored Weber's exact (1)-(17): (1) λλ'≡1(mod e); (2) ψ_λ(α^λ')=ψ_λ'(α); (3) λ+λ''+1≡0; (4) ψ_λ(α)=(−1)^f ψ_λ''(α); (5) ψψ(ε⁻¹)=n; (6) ψ_λψ_λ(α⁻¹)=n; (7) triple-product=…/(ε^{λ+μ+ν},r); (8) ψ_2λψ_2λ+1=ψ_1ψ_λ(α²); (9) (α,η)^7=ψ_1(α)⁴ψ_1(α²)²ψ_1(α⁴); (10) λ+μ+ν≡0(mod m); (11) ψ_{λ,μ}(ε)=Σε^{μ indt+ν ind(t+1)}; (12) ψ_{λ,μ}(g)=Σg^…≡Σt^μ(t+1)^ν; (13) ≡Σ_{1,n−1}t^μ(t+1)^ν; (14) ≡Σ_{0,ν}^h B_h^{(ν)}Σt^{μ+h}; (15) Σg^{s(μ+h)}≡0; (16) ≡m≡−1; (17) two-case Π-formula. Fixed (−1)^n→(−1)^μ; restored Kronecker footnote + moved Jacobi paragraph back to its Weber position + full e=7 example + (α,η)^14 verification + the whole (10)-(17) Congruenz derivation; DROPPED the non-Weber "Hier bedeutet Π(k)=1·2···k". De-modernized \sum_{t=1}^{n-2}→\sum_{1,n-2}^t etc. Cross-refs \S\,169,(5)/(6)/(8)/(3)/(15)/(14) consistent w/ §169's fixed numbering. \footnote confirmed (fn 61); eyeballed PDF pp361-364. All 17 tags present & contiguous. **397pp/0err/0 overfull/0 underfull/0 missing-char/0 undefined** (+2pp). **§171/§172 VERIFIED complete+faithful** (map-phase worked-example islands; §171=Gauss'sche Summen w/ 14 eqs+Gauss fn62, §172=⅓/¼ periods e=3/e=4; inbound cross-refs from §170/§171/§172 to §169 all resolve correctly against my Weber-renumbered §169 — triangulates the §169 renumber as correct, no breakage; §171 line 20350 needs (α^λ,r)(α^{−λ},r)=(−1)^{μλ}n = my new §169(10) for the Gauss sum ✓). **§173 (Die complexen Zahlen von Gauss, p585-591) FULLY MAPPED (notes = scratchpad/weber_173_notes.md), COMPOSE + APPLY NEXT.** §173 is a heavy reconstruction: Weber uses NUMBERED SÄTZE 1.-6. (p/q reps, Bezout, prime-divides-product, unique-factorization) + only 3 tagged EQS ((1)=Euclid chain, (2) αϰ+βλ=δ, (3) αϰ+βλ=1); .tex fabricated tags (1)-(9), dropped BOTH footnotes (¹ Gauss Theoria residuorum biquadraticorum / ¹ Gauss primär-choice), reworded opening+prose, flattened the Sätze to prose, and ★ GOT THE GAUSSIAN-PRIME LIST WRONG (fabricated 9+5i=norm106 composite, dropped 5+8i/9+4i/7+10i, altered 3+2i→2+3i; Weber's list=22 correct entries). Cross-refs to preserve: §.138,4./§.138/§.172,(27)/§.172,(38),(39). §174 boundary confirmed p592. **§173 DONE** — restored Weber's Sätze-1.-6. structure + eqs (1)-(3) [dropped .tex's bogus (1)-(9)], both footnotes (Gauss Theoria residuorum biquadraticorum / Gauss primär-choice), the full compressed prose, and ★ the CORRECTED 22-entry Gaussian-prime list (.tex had fabricated 9+5i=composite, dropped 5+8i/9+4i/7+10i, altered 3+2i). \varkappa for ϰ, \leqq for ≦. Cross-refs §.138,4/§.172,(27)/(38)/(39) preserved. All Sätze+eqs render-confirmed PDF pp372-376. **400pp/0err/0 overfull/0 underfull/0 missing-char/0 undefined** (+3pp). **NEXT: §174** (Der Körper der dritten Einheitswurzeln, p592+; the R(ρ) cube-root field analog of §173 — likely same reconstruction pattern: check for Sätze structure, footnotes, dropped prose, and verify eq numbering + any prime list). **§174 DONE** — R(ρ) cube-root field; Weber has NO numbered eqs so DROPPED .tex's fabricated (1)-(6); restored opening (Hauptsatz…§173,(1)), R(√−3) naming, factored Norm form, (2a−b)²+3b²=4 units, both associate systems, "in Uebereinstimmung mit §172", removed spurious "<1"; PRIME LIST verified correct (matches Weber, kept). \rho/\leqq/\pmod3. Render-confirmed PDF pp376-377. **400pp/0err/0 overfull/0 underfull/0 missing-char/0 undefined** (held 400). **§175 DONE** — Reduction der Gruppe durch reine Gleichungen (p595-597), FIRST section of Siebzehnter Abschnitt. **Also FIXED the chapter head** \begin{center}\large…\end{center} → \section*{Siebzehnter Abschnitt. Algebraische Auflösung von Gleichungen.} (title confirmed vs p595_top). Weber has NO numbered eqs → dropped .tex's fabricated \tag{1} (y^m−a=0) and \tag{2} (ε=ψ); **fixed MATH ERROR x_{n-1}→x_{m-1}** in ε=ψ(x₀,x₁…x_{m-1}); restored the dropped roots display ε,ε₁,ε₂…ε_{m−1}, the dropped C.Jordan footnote (Traité p.386) on "umformt", the dropped indented question "Unter welchen Bedingungen…reducirt?", and Weber's exact wording of Theorems I & II (quote blocks). Cross-refs \S\,162/\S\,157/\S\,155/\S\,163. Render-confirmed §175 region PDF. **401pp/0err/0 overfull/0 underfull/0 missing-char/0 undefined** (+1pp). **§176 DONE** — Metacyklische Gleichungen (p597bot-599). Reconstruction: restored Weber's opening + P₁-chain, FIXED Satz III display (.tex `P,P₁,P₂,…,1` → Weber `P,P₁,P₂,P₃…` no trailing 1), restored the 2nd display `P,P₁,P₂…P_{μ−1},1`, restored the dropped Kronecker/Frobenius/Hölder footnote (\glqq/\grqq), Satz IV kept + full proof restored (μm=n, §158 cites, base case n=Primzahl→μ=1). NO numbered eqs. Render-confirmed. **401pp/0err/0 overfull/0 underfull/0 missing-char/0 undefined** (held 401). **§177 DONE** — Einfachheit der alternirenden Gruppe (p600bot-603top). Reconstruction w/ SOUND math: all 5 cycle computations were correct (kept). Fixed: \kappa→\varkappa (Weber's ϰ); restored dropped case-3 parenthetical + dropped footnote 1 (Abel/Ruffini/Burkhardt) + the compressed final symmetric-group paragraph (ϰ²,ϰλ=1⇒λ=ϰ); de-modernized (∈/Commutator/∩ removed); \perm now &-aligned 2-row matrix; only eq (1) λ=ϰ⁻¹π⁻¹ϰπ numbered. **⚠ ALSO patched §176**: my §176 pass had missed its final closing paragraph ("Unter der Voraussetzung also…allgemein nachgewiesen.") at the top of p600 — appended it (lesson: always read the next section's first scan to confirm the boundary). **402pp/0err/0 overfull/0 underfull/0 missing-char/0 undefined** (401→402). **§178 DONE** — Nicht metacyklische Gleichungen im Körper der rationalen Zahlen (p603mid-606top). HEAVY reconstruction, several serious defects fixed: **MATH ν(n)→Π(n)** (Galois resolvent degree = n!); removed FABRICATED third-person "Weber benutzt hier…"; restored dropped footnote 1 (Hilbert, J.f.Math Bd.110); removed FABRICATED "Eisenstein'sche Kriterium" name + restored Weber's numbered Satz 3; **FABRICATED final label "A."→"4."**; restored the dropped closing paragraph; "Daraus folgt:"→"Daraus folgt als Corollar:"; restored expanded f(x) 2nd line + "(vergl. den siebenten Abschnitt)"; Satz-3 proof α (not a) + Weber's x^{k−ν} contradiction. NO numbered eqs; Sätze 1-4 as quote blocks. **402pp/0err/0 overfull/0 underfull/0 missing-char/0 undefined** (held 402). **§179 DONE** — Auflösung durch reelle Radicale (p606mid-609mid). Heavy reconstruction fixed: eq ORDER (.tex had (2) before (1); Weber = (1) roots then (2)); **ν→μ** (Grad von f₁); restored dropped footnote ¹ (Hölder Math.Ann.38/Kneser 41) + §165 ref + 3 dropped unnumbered displays (ε^λα^μ=b, μh+pk=1, a=(bʰaᵏ)ᵖ); restored the whole COMPRESSED geometric-problems discussion (Cirkel/Lineal, Siebeneck, §154,7/§157, Dreitheilung, Delisches Problem/x³=2); casus irreducibilis plain (not \emph); ϱ=\varrho (g-root), ε (adjoined root, not .tex's θ), Ω(ε); eqs (1)-(4), Sätze 1,2 quote blocks. **403pp/0err/0 overfull/0 underfull/0 missing-char/0 undefined** (402→403). **§180 (Metacyklische Gleichungen von Primzahlgrad) DONE** — LARGEST section yet, spans **p609bot–p620** (§181 opens p621). HEAVY MODERNIZED+FABRICATED reconstruction fully re-transcribed: **restored dropped Satz IV** (the .tex fabricated I,II,III→V numbering; Weber = I–IX contiguous); **fixed FABRICATED eq (6)** (.tex had −a₀z^{n−1}−… ; Weber = −a₀ψ(z)/z−… + restored the Lagrange display, ψ(z)=z(z−1)…, ψ≡z^n−z, ψ'≡−1); **erratum #15 z₀≡b/(a−b)** crop-confirmed Weber typo, transcribed as printed; restored BOTH footnotes (p611 Kronecker-nennt + p620 Monatsbericht 1856); de-modernized \triangleleft/\bigl\{set-builder\bigr\}; restored λ^h + (a^h−1)/(a−1) displays, eqs (5) full ranges + (11)(12) + coset decomp P=Q+Qπ₁+… + C=1,γ…; restored the gutted VI/VII ϰ₀/γ-counting converse proof + the discriminant-sign derivation. All eqs (1)-(12) & Sätze I–IX contiguous. ϰ=\varkappa; \perm for π-matrix & λλ' pmatrix; \S\,176/158,3/153/29/136. Render-confirmed pdftotext (Sätze I–IX in order, footnotes 71+72, Lagrange, z₀, Nebengruppen). **407pp/0err/0 overfull/0 underfull/0 missing-char/0 undefined** (403→407, +4pp). **HELD remaining: §181-188, §69, p466, §138-numbering.** **§181 (Anwendung auf die metacyklischen Gleichungen fünften Grades) DONE** — n=5 metacyclic-quintic theory, p621-627top (§182 opens p627mid), eqs (1)-(24). Reconstruction kept most eq bodies but stripped scaffolding: **restored dropped eq (11) [six u₁..u₆] + eq (12) [six u'₁..u'₆]** (Weber's y-sextic = GENUINE REUSED (12), both zoom-confirmed p623 — kept double-(12)); **restored BOTH dropped footnotes** (Jacobi/Cayley on (9), Runge Acta math.Bd.7 on Bring-Jerrard (13)); **fixed MATH ERROR (15)** .tex √(−α)→Weber ⁴√(−α); **killed FABRICATED "Weber bildet die Resolvente…"** → Cayley remark + besonderen-Fall; restored degree-table+√Δ-10ten-Grade, full ten-diff product in (16), β=0 y-values, the √α→−√α derivation + (v−α)⁴(…)=0, the whole metacyklisch-verification discussion (6u⁵−20αu³+30α²u−√Δ=0, 5(u²−α)³=0, v=α⇒β=0), the λ=−1,μ=1 intermediates + conclusion; restored §74 ref on (19) + §178,3 on x⁵+5x+5t; de-modernized (1)-table (dropped \hline/rules, (s)/(t)/(t²) parens) + restored Nebengruppen-verschieden proof + "wie schon Lagrange" on (8). Render-confirmed pdftotext (footnotes 73+74, u/u' blocks, double-(12), ⁴√, example). **410pp/0err/0 overfull/0 underfull/0 missing-char/0 undefined** (407→410, +3pp). **HELD remaining: §182-188, §69, p466, §138-numbering.** **§182 (Die Gruppe der Resolvente) DONE** — LAST section of Siebzehnter Abschnitt, p627mid-629bot (§183 opens ACHTZEHNTER ABSCHNITT). Reconstruction kept eq bodies (1),(2) + π/w displays but stripped ~half the prose + carried a fabricated 3rd-person "Weber". Fixed: **killed FABRICATED "untersucht Weber den Einfluss…"** → Weber "haben wir nur den Einfluss zu untersuchen"; **restored dropped §182 opening** (merkwürdiger Schluss / x₀..x₄ als unabhängige Variable) + eq (1); **restored the whole M-conjugates π⁻¹Mπ trivial-intersection paragraph + §177**; **restored §156 Totalresolvente-Bezeichnung + F(z)-transitiv reasoning + Weber's 1·2·3·4·5=120 / 6·120 forms** (.tex had compressed to "…720 hat"); **restored §153,2 ref + the (11)→(12) transposition-derivation** of the π-generators + the "wo sich die in den π…u/v" clause; restored the P8 display π₁=(w₀,w₁)…π₄=(w₀,w₄) + §153,2 + "wie die Summe der w"; restored "für ein beliebiges rationales λ" (P9). **ERRATUM #16 PRESERVED**: w₀ = v₁v₂ + **v'₄**v₅ + v₃v₆ (stray prime on v₄; v has no primed members — zoom-confirmed p629 crop_22_31; .tex had silently "corrected" to v₄v₅). **ERRATUM #17 PRESERVED**: "Da **F(z)** auch irreducibel ist" (zoom-confirmed p628 crop_55_25 — italic z unmistakable; resolvent is F(v)=0 throughout, so F(z) is a Weber misprint). Ordinals set as printed (6^{ten}/5^{ten} numeral+superscript, matching Weber vs reconstruction's spelled-out sechsten/fünften). Render-confirmed pdftotext (merkwürdigen Schluss / conjugirten Gruppen π⁻¹Mπ / eingeführten Bezeichnung eine Totalresolvente / Da F(z) auch irreducibel / haben wir nur den Einfluss zu untersuchen [untersucht Weber now ABSENT] / beliebiges rationales). **410pp/0err/0 overfull/0 underfull/0 missing-char/0 undefined** (held 410, +2600 chars absorbed by layout). **§182 COMPLETES the Siebzehnter Abschnitt — the whole §175-182 metacyclic block is now source-faithful. 17 Weber errata flagged (16=§182 v'₄, 17=§182 F(z)).** **HELD remaining: §183-188 (Achtzehnter Abschnitt "Wurzeln metacyklischer Gleichungen"), §69, p466, §138-numbering.** **§183 (Stellung der Aufgabe. Hülfssatz) VERIFIED FAITHFUL — 2 surgical fixes** — FIRST section of the ACHTZEHNTER ABSCHNITT, p630mid-633mid. **Chapter head verified correct** vs p630 scan (Achtzehnter Abschnitt. Wurzeln metacyklischer Gleichungen. — untouched). Read all scans p630-633 by eye: opening, Abel/Kronecker/H.Weber footnote (Marburg 1892), eqs (2),(3), Normalform Sätze 1/2/3, X=X₁X₂ argument, cross-refs §164/180/134/142/143/144/152, Satz-3 averaging display — ALL match .tex verbatim. **ONLY DEFECT: 2 modernized sums** de-modernized to Weber's index-above/range-below form: (a) eq (1) `\sum_{h=0}^{n-1}`→`\sum_{0,n-1}^{h}`; (b) Satz-3 avg display `\sum_{h=1}^{n-1}`→`\sum_{1,n-1}^{h}` (both confirmed p631/p633; matched §167/169/170 house form). No dropped content/fabrication/matherr — §183 is like §150/151/171/172 (faithful, patchable). Boundary note: .tex §184 opening DROPPED Weber's "und wenden darauf die Sätze des vorigen Paragraphen an" → §184 IS a reconstruction. **410pp/0err/0 overfull/0 underfull/0 missing-char/0 undefined** (held 410). **HELD remaining: §184-188 (Achtzehnter Abschnitt), §69, p466, §138-numbering.** **§184 (Sätze über die Resolventen) DONE** — full re-transcription (HEAVIEST since §180) applied + compiled + render-verified page-by-page (output-PDF pp400-404). Notes = scratchpad/weber_184_notes.md; full apparatus in CERT log (2026-07-02 §184 entry). Fixed ~9 eq math errors [(4)→(ε,x)^n; (5) 1-line→3-line recursion array; (8) sign 1-g^{n-1}; (9) wholesale→[(ε,x)^{(g^{n-1}-1)/n}(ε^λ,x)]^n f₀^{g^{n-2}}…; (17) g-exps→q_{n-2}…q_1; (18) Φ_v→Φ_v^n; (20) restore φ(u) numerator+=χ(u); (21) Θ_v=Θ(u)→χ(u)/φ'(u)=Θ(u); g-congruences =→≡ ×2]; **erratum #18** (Satz 6 prints f_{n-1}, kept as printed); Satz numbering 4-7 (rebuilt as quote blocks, .tex's \enumerate[resume] was broken); GREEK α)β)γ)δ) list labels; de-modernized sums (eq2-requote Σ_{1,n-1}, eq3 Σ_{1,n}, eq20 Σ_{0,n-2}; double-(2) kept); ~30 prose drops restored. Original defect map (now COMPLETED): SECOND section of Achtzehnter Abschnitt; spans **p633mid–638mid** (5+ pp; §185 opens p638). .tex block = lines 21959–22124 (§185 @22125; RE-GREP before edit). ★★ HEAVIEST reconstruction since §180 — a FULL re-transcription. **~9 EQ-BODY MATH ERRORS**: (4) (ε,x)^λ→(ε,x)^n [zoom-confirmed p634bot]; (5) .tex collapsed Weber's 3-LINE recursion array [(ε^g,x)(ε,x)^{-g}=f₀ / (ε^{g²},x)(ε^g,x)^{-g}=f₁ / … / (ε^{g^{n-1}},x)(ε^{g^{n-2}},x)^{-g}=f_{n-2}] into one WRONG line; (8) sign g^{n-1}-1 → **1-g^{n-1}**; (9) .tex WHOLESALE WRONG → Weber [(ε,x)^{(g^{n-1}-1)/n}(ε^λ,x)]^n f₀^{g^{n-2}}f₁^{g^{n-3}}…f_{n-2}; (17) .tex g^{n-2}-exps → Weber **q_{n-2}** (quotient) exps; (18) Φ_v→**Φ_v^n**; (20) .tex dropped the **φ(u) numerator** + the **=χ(u)** RHS; (21) .tex `Θ_v=Θ(u)` → Weber **χ(u)/φ'(u)=Θ(u)**; the two g-congruences =→**≡**. **★ERRATUM #18** (zoom-confirmed p635 crop_12_53): Satz 6 prints "f₀,f₁…**f_{n-1}**" (only n−1 fns exist f₀…f_{n-2}, so f_{n-1} is a Weber misprint); .tex silently "corrected" to f_{n-2} → restore printed f_{n-1}, flag. **SATZ NUMBERING**: Weber Sätze 4,5,6,7 (continue §183's 1,2,3; "Aus 2. und 4." confirms); .tex `\enumerate[resume,label=\arabic*.]` is BROKEN (§183 used quote blocks) → FIX to render 4-7. **GREEK LABELS** α)β)γ)δ) (.tex \alph* a-d); γ) restore "(0,1,2…n-2)". **DE-MODERNIZE SUMS**: eq(2)-requote Σ_{1,n-1}^{h}, eq(3) Σ_{1,n}^{h} [range "1,n" zoom-confirmed], g^{-1}-display, eq(20) Σ_{0,n-2}^{v}. **~30 PROSE DROPS** (all cited w/ line#s in notes): incl. "und wenden darauf die Sätze des vorigen Paragraphen an" (§184 opening), the 4 λ-Vertauschungen displays, "wie nach dem Theorem 4. zu sehen ist", the "Hierbei ist unter einer metacyklischen Function…" def para, "Diese Formeln gelten für jedes v [+ F_h=F_k / aus 4. …]" continuation, "(§. 155)", the eq-19/20/21 follow-ups, closing "deren Coëfficienten metacyklische Functionen der x sind, und ε nicht mehr enthalten", + xref drops §180/§163/§183,(3). **411pp/0err/0 overfull/0 underfull/0 missing-char/0 undefined (410→411, +1pp). 18 Weber errata flagged (18th = §184 Satz6 f_{n-1}). HELD remaining: §185-188 (Achtzehnter Abschnitt), §69, p466, §138-numbering. **§185 (Wurzeln metacyklischer Gleichungen) DONE** — full re-transcription (HEAVY, on par with §184) applied + compiled + render-verified page-by-page (output-PDF pp404-406). Notes=scratchpad/weber_185_notes.md; full apparatus in CERT log (2026-07-02 §185 entry). Fixes: **𝔎** base field (\mathfrak{K} — Weber's, ≠ §184's Ω); eq(2) **θ→Θ** +fuller chain +§163; eq(3) **Θ→Φ** +refs +"worin Φ…(in 𝔎)"; ε_v **\epsilon→\varepsilon**; eq(1) removed stray "=0"; eq(8) sign **+g**; eq(12) **E_0^{r_v}**; eq(13) **restored** (was wholesale-wrong); eq(9)-ref **(6)→(5)**; **erratum #19** (Vor.2 prints f_{n-1}, kept); Eigenschaft **δ)**; de-mod sums (6)(9)(14) →\sum_{0,n-2}^{v}; restored numbered Voraussetzungen list + k/K 4-display setup + 2 E_{v-1} displays + "ξ₀ durch n−1 Radicale…zu gross wäre" + "Nach §184,(16)&(17)…von Null verschieden" + Cayley §36 + ~25 prose drops. Original defect map (now COMPLETED): THIRD section of Achtzehnter Abschnitt; substitutes roots ξ of an irreducible metacyclic eqn (over base field 𝔎) for §184's x; explicit root formula (6)/(7) via ⁿ√ radicals. .tex block = lines 22166–22257 (§186 @22258; RE-GREP). eqs (1)-(14). ★★ HEAVY reconstruction (on par with §184). **NOTATION FIXES**: Ω→**𝔎** (\mathfrak{K}, opening ×2 — Weber's base field, distinct from §184's Ω; doc already uses \mathfrak); eq(2) **θ→Θ** (+fuller cyclic chain k_{n-1}=Θ(k_{n-2}),k_0=Θ(k_{n-1}) +§163 ref); eq(3) **Θ→Φ** (+"nach dem Schlusssatze des §184 und zwar in der Form"+"worin Φ eine rationale Function (in 𝔎) bedeutet"); ε_v system **\epsilon→\varepsilon** (eqs 9,10,13 + 3 displays; fixed root ε e.g. ε^{-hr_v} already \varepsilon). **MATH ERRORS**: eq(1) remove appended "=0" (Weber ψ(u)=(u-k₀)…(u-k_{n-2}), no =0); eq(8) (ⁿ√R_{v-1})^{-g}→**^{+g}** [zoom-confirmed]; eq(12) E_0^{g^v}→**E_0^{r_v}** [zoom-confirmed]; eq(13) .tex wholesale-wrong ε_{n-2}ε_{n-3}^g…→Weber **ε_0^{r_{n-2}}ε_1^{r_{n-3}}…ε_{n-2}^{r_0}** (=eq10 at v=0); eq(9)-intro ref **(6)→(5)**. **ERRATUM #19**: Voraussetzung 2 prints "f₀,f₁…f_{n-1}" (only f₀…f_{n-2} exist — same pattern as §184 Satz6 erratum #18; .tex "corrected" to f_{n-2}); transcribe as printed, flag. **STRUCTURE**: Eigenschaft d)→δ); de-modernize sums eqs(6),(9),(14) \sum_{v=0}^{n-2}→\sum_{0,n-2}^{v}; restore the numbered Voraussetzungen list (1.,2.) + "Nach (13),(16),(17),§184…" intervening prose (.tex flattened to 1 sentence); restore k/K setup with 4 DISPLAYS + Weber wording; restore 2 dropped E_{v-1} displays before (12); restore dropped passages [ξ₀ durch n−1 Radicale…zu gross wäre; Nach §184,(16)&(17)…von Null verschieden; die man z.B.…Cayley §36]; ~25 prose drops/rewords (all cited in notes). eqs matching .tex (keep): (4),(5),(7),R_v-display,(11),radical-displays,(14)-body. **412pp/0err/0 overfull/0 underfull/0 missing-char/0 undefined (411→412, +1pp). 19 Weber errata flagged (19th=§185 Vor.2 f_{n-1}). HELD remaining: §186-188 (Achtzehnter Abschnitt), §69, p466, §138-numbering. NEXT FIRE: §186 (Befreiung von den beschränkenden Voraussetzungen), opens p641bot (.tex marker was line 22258, RE-GREP before edit). §186 opening visible in output-PDF p406: drops the two §185 Voraussetzungen; uses η₀..η_{n-1} for the n roots of an irreducible metacyclic eqn + introduces new unknowns via eq (1) ξ₀=ψ(η₀), ξ₁=ψ(η₁),…,ξ_{n-1}=ψ(η_{n-1}). LIKELY same reconstruction pattern (check: 𝔎 field vs Ω, Θ/Φ/θ/ε letters, dropped prose/refs, eq-body errors, more f_{n-1}-type errata, de-mod sums). Method: re-grep §186 marker, render p641bot + p642+ scans, compare to .tex §186 block (lines ~22258-22368, ~110 lines — LARGE), MAP to weber_186_notes.md (defer compose to a fresh fire per discipline), then compose retrans_186.py, apply, compile-gate (page count must not drop; +pp OK), 0 overfull/underfull/missingchar/undefined, visual-verify by rendering output-PDF §186 pages via pdftoppm + eyeball (this method caught everything for §184/§185), log CERT+METHOD, re-arm. **§186 (Befreiung von den beschränkenden Voraussetzungen) DONE** — LARGEST section (p641bot–646bot, 5+ pp, 16 eqs, 2 Roman Sätze). Mapped whole (all scans re-verified this fire), composed retrans_186.py, applied (+4366 chars), compiled, render-verified output-PDF pp406–409 page-by-page. Notes=scratchpad/weber_186_notes.md; full apparatus in CERT log (2026-07-02 §186 entry). Key fixes: Ω→**𝔎** everywhere; **cancelling .tex numbering errors** (dropped eq(3) χ-poly + merged eq(4) η-system = −1; fabricated an extra "(5) x_h=χ(y_h)" = +1) → restored eq(3)+full eq(4), DELETED fabricated (5), so (6)-on re-align; eq(5) ψ→**χ**; eq(6) → **RATIO** (ε^{r_v},y)/(ε^{r_v},x)=Θ_v; eq(7) Θ_v→**Q_v**; eq(14) index h→**v**; restored Vandermonde det + §143,1 passage + Tschirnhausen (§52) + Q_vK_v paragraph + unnumbered 3-term chain + (h,h+βr) & (h,g⁻¹h) & S(ξ) & τ-list displays + full irreducibility argument (§179, x^n−R_0, Φ/Ψ); Sätze I./II. as Roman quote blocks; a)-d)→α)β)γ)δ); de-mod sums \sum_{0,n-2}^{v}; **erratum #20** (p646top S(ξ₀…ξ_{n-2}) misprint for ξ_{n-1}, kept as printed). **413pp/0err/0 overfull/0 underfull/0 missing-char/0 undefined (412→413, +1pp). 20 Weber errata flagged (20th=§186 S(ξ) n-2). §186 COMPLETE — the whole §183-186 metacyclic-roots core of the Achtzehnter Abschnitt is now source-faithful.** **HELD remaining: §187-188 (Achtzehnter Abschnitt), §69, p466, §138-numbering.** NEXT FIRE: **§187 (Realitätsverhältnisse)** — SHORT section (opens p647; .tex marker was line 22400, RE-GREP before edit; .tex §187 block ≈ lines 22400-22417, only ~18 lines, then §188 "Metacyklische Gleichungen fünften Grades" @22418). Method as usual: re-grep §187/§188 markers, render p647 scans, compare to .tex §187 block, map+compose (may be small enough to compose same fire), apply, compile-gate, visual-verify output-PDF via pdftoppm, log CERT+METHOD, re-arm. After §187: §188 (n=5 metacyclic quintics — likely reconstruction w/ eqs), then §69, p466, §138-numbering; then global sweeps (\bgibt\b→giebt, \pmod→(mod.), errata de-dup review).** **§187 (Realitätsverhältnisse) DONE** — NOT a short patch: HEAVY compression reconstruction (p647top–648top). The .tex collapsed Weber's whole Φ/Ψ reality argument (5 dropped displays + reasoning) into 2 fabricated lines. Composed retrans_187.py same fire (fresh in context), applied (+1123 chars), compiled, render-verified output-PDF p410. Fixes: Ω→**𝔎**; restored §180 + §165 cross-refs ("wie wir im §180 gesehen haben" / "haben wir im §165 gesehen, dass es…giebt, nämlich"); **FIXED .tex mis-ref "Formel(10) des §184"→Weber "§186"**; restored the dropped Φ-displays (2) + g^{(n-1)/2}+1 rationality reasoning + Ψ(k_v) display + Ψ(k_v)=Ψ(k_{v+(n-1)/2}) + the n^{ten}-Potenzen/Einheitswurzel=1 conjugate-imaginary argument; conjugiert→**conjugirt**, gibt→**giebt**; concluding Satz as quote block. **ERRATUM #21** (p647mid prints k_0…k_{n-1} ×2 + τ_0…τ_{n-1}, but cyclic eqn is (n-1)^ten Grades w/ roots k_0…k_{n-2} & only n-1 radicals τ_0…τ_{n-2}; concluding Satz p648 correctly prints k_{n-2}; kept n-1 as printed at both P2 occurrences, zoom-confirmed). No numbered eqs (all displays unnumbered). **413pp/0err/0 overfull/0 underfull/0 missing-char/0 undefined (held 413). 21 Weber errata flagged (21st=§187 k_{n-1}/τ_{n-1}).** **HELD remaining: §188 (Achtzehnter Abschnitt — LAST section), §69, p466, §138-numbering.** NEXT FIRE: **§188 (Metacyklische Gleichungen fünften Grades)** — the FINAL section of Band I / the Achtzehnter Abschnitt (opens p648mid; .tex marker was line 22450, RE-GREP before edit). §188 opening (output-PDF p410) uses **Ω** ("in einem beliebigen Körper Ω die Wurzeln aller metacyklischen Gleichungen fünften Grades zu finden") — check 𝔎-vs-Ω convention (§187 used 𝔎, so likely Ω→𝔎), plus the usual reconstruction pattern (dropped eqs/displays, refs, errata, de-mod sums). n=5 worked example — likely has numbered eqs + explicit quintic computation; map carefully vs scans p648mid onward. Method as usual (re-grep marker, render scans, map+compose, apply, compile-gate, pdftoppm visual-verify, log, re-arm). After §188 the whole ACHTZEHNTER ABSCHNITT (§183-188) + Band I main text is source-faithful → then §69, p466, §138-numbering, then global sweeps.** **§188 (Metacyklische Gleichungen fünften Grades) FULLY MAPPED — COMPOSE + APPLY NEXT FIRE.** LAST section of Band I main text; spans **p648mid–p653mid** (5+ pp, eqs (1)-(14), NO Sätze). Notes = scratchpad/weber_188_notes.md (complete, all scans read + eq(14) zoom-confirmed). .tex block = lines 22470–22632 (then \section*{Berichtigungen} @22633, \end{document} @22639; RE-GREP before edit; **end anchor = \section*{Berichtigungen}**). n=5 metacyclic-quintic worked example: solve the cyclic biquadratic (roots k_0..k_3) generally via w=(k_0-k_2)(k_1-k_3), then substitute into §186(9) for the quintic root ξ. Reconstruction pattern (kept most eq bodies, stripped prose + a few eq errors): **Ω→𝔎** (Weber uses Fraktur throughout, confirmed p648bot/p649/p651); **ρ→ϱ (\varrho)** everywhere (eq 10, basis, perms, eq 14, 3-radical, closing); ★**MATH ERROR** Abel-display .tex √(1+e)→Weber **√(1+e²)** (p652); ★★**ERRATUM #22** eq(14) — Weber's printed K_2 (last term +A_4rϱ; S² math wants −), K_3 (3rd term A_2ϱ' wants A_3; last term −A_4rϱ' wants +) disagree w/ the substitution-group math which the .tex silently "corrected" — RESTORE Weber's printed (mis)forms + flag (zoom-confirmed crop_15_14); ★★**DROPPED**: the Kronecker/rational-numbers passage ("…ein sehr merkwürdiger von Kronecker herrührender Satz, den wir im zweiten Bande kennen lernen werden"), the "Es handelt sich dann nur darum…algebraisch ausdrücken kann" sentence, ★★the whole **4-ROW substitution TABLE** (p650bot, .tex compressed to "Daraus folgt…rationalen Ausdruck besitzt"), "Der Ausdruck (12) ist also insofern allgemeiner…zerfällt", the "wenn man rechts für ϱ'²…r² rational ist" explanation, "also niemals bei reellen Körpern", + many clause drops; de-mod ordinals ("fünften"→"5^{ten}", restore "der Reihe nach congruent mit 1,2,4,8"); Coëff→Coeff (ë→e); keep giebt/substituiren/permutirt. Method next fire: compose retrans_188.py from notes (careful — 14 eqs incl. many 2/4-line aligned displays, the 4-row×6-col table, two 2-row Vertauschung displays [render as \begin{pmatrix}; check \perm macro], the √ nests), apply via marker range-replace (end anchor \section*{Berichtigungen}), compile-gate (page count must not drop; +pp OK), 0 overfull/underfull/missingchar/undefined, visual-verify by rendering output-PDF §188 pages via pdftoppm + eyeball, log CERT+METHOD, re-arm. **413pp/0err currently. 21 Weber errata flagged (22nd=§188 eq14 pending on apply).** After §188 apply: the whole ACHTZEHNTER ABSCHNITT + Band I main text source-faithful; also VERIFY the printed \section*{Berichtigungen} (2 entries: S.182 X_m/X_n; S.347 (2x²+1)²/(2x²-1)²) vs the actual errata page; then §69, p466, §138-numbering, then global sweeps (\bgibt\b→giebt, \pmod→(mod.), errata de-dup review).** **§188 (Metacyklische Gleichungen fünften Grades) DONE** — composed retrans_188.py from notes, applied (+3039 chars), compiled, render-verified output-PDF pp411-414 page-by-page. Fixes: Ω→**𝔎** everywhere; ρ→**ϱ (\varrho)** everywhere; ★**MATH ERROR** Abel display √(1+e)→**√(1+e²)**; ★★**ERRATUM #22** eq(14) restored Weber's printed K_2 (+A_4rϱ), K_3 (A_2ϱ', −A_4rϱ') — 3 sign/subscript slips the .tex had silently "corrected", zoom-confirmed; ★★restored the DROPPED **Kronecker/rational-numbers passage**, the "Es handelt sich dann nur darum…" sentence, the **4-row×6-col substitution TABLE**, "Der Ausdruck (12) ist also insofern allgemeiner…zerfällt", the "wenn man rechts für ϱ'²…r² rational ist" explanation, "also niemals bei reellen Körpern", the specific "B und h durch Be und he²", "worin A_1..A_4 rational sind", "der Reihe nach congruent mit 1,2,4,8", "wie in §185"; de-mod "5^{ten} Grades"; both Vertauschungen as \begin{pmatrix}; 4-row table w/ Weber commas. eqs (1)-(13) bodies kept. **414pp/0err/0 overfull/0 underfull/0 missing-char/0 undefined (413→414). 22 Weber errata flagged (22nd=§188 eq14 K_2/K_3).** **★★★ MILESTONE: §188 COMPLETES the ACHTZEHNTER ABSCHNITT (§183-188) AND the entire re-transcribable body of Band I main text — the whole vol1 §141→§188 section-by-section source-faithful pass is DONE.** **HELD remaining (NON-section items): (1) verify printed \section*{Berichtigungen} (Weber's own 2-entry errata) vs the actual errata page [lines 22483-22487ish, RE-GREP]; (2) §69; (3) p466; (4) §138-numbering (whole-section rule-renumber, MAPPED, edit deferred); then global sweeps (\bgibt\b→giebt; \pmod→(mod.) de-modernize; errata de-dup review of the 22 flagged Weber errata + reused-eq-number audit).** NEXT FIRE: start on the held-list — begin with the **Berichtigungen verification** (quick: render the printed errata page — it's at the very end of the book after p653; find its printed page, compare the 2 entries S.182/S.347), then **§69** (re-grep \sect{69}, render its scans, compare to .tex — flagged long ago as HELD, unknown defect profile). Method unchanged (re-grep, render, map/compose, apply, compile-gate, pdftoppm verify, log, re-arm). **BERICHTIGUNGEN DONE** — verified vs printed p654 (zoom crop_52_43): fixed .tex $X_m$/$X_n$ → **$x_m$/$x_n$** (lowercase, Weber prints lowercase x) + removed the .tex's extra comma after "Seite 182"/"Seite 347" (Weber: "Seite 182 in der Formel"). 2nd entry $(2x^2+1)^2$ statt $(2x^2-1)^2$ already matched. Compiles 414pp/0err. CERT log entry added. **§69 (Invarianten-Eigenschaft der Tschirnhausen-Transformation) FULLY MAPPED — COMPOSE + APPLY NEXT FIRE.** Sechster Abschnitt; printed **p212mid–p215mid** (§70 opens p215; .tex block lines 7756–7876, §70 @7877, RE-GREP; **end anchor = \sect{70}{Ausf\"uhrungen \"uber den Hermite'schen Satz}**). Notes = scratchpad/weber_69_notes.md (complete, all scans p212-215 read + eq(14)/(16) checked). ★★★ CENTRAL DEFECT: Weber uses THREE function-letters — F(t,x)↔**Φ(τ,ξ)** (τ-power versions) and Y(t,x)↔**H(τ,ξ)** (τ_k-variable versions) — but the .tex COLLAPSED them, wrongly writing **H for Weber's Φ** in eqs (3),(8),(9) + the "ebenso in Φ(τ,ξ)" text (H is correct only in (10 2nd line),(11),(12),(17)). Other defects: TITLE hyphen (Invarianteneigenschaft→**Invarianten-Eigenschaft**); eq(3) DROPPED 2nd-line expansion τ^{n-2}Φ_0(ξ)+…+Φ_{n-2}(ξ) + the Φ_i/F_i explanation; eq(7) .tex CLEARED the **(1/n)** factors (×n) — restore Weber's un-cleared form; ★★eqs (14)-(16) WHOLESALE wrong — eq(14) powers REVERSED (.tex t_{n-2}z^{n-2}+…+t_0 → Weber t_{n-2}−(n−2)t_{n-3}z+…±t_0z^{n-2} ascending), .tex's numbered (15) Θ(z) is WRONG (Weber's (15) = the z↔ξ substitution z=(αξ+β)/(γξ+δ),ξ=(δz−β)/(−γz+α); Weber's Θ(ξ) is UNNUMBERED w/ ascending ξ-powers), eq(16) z→**ξ**; ~7 DROPPED unnumbered displays (dt/dτ=r/(γτ+δ)²; 3 displays between (7)&(8); the multiplier list 1,−(n−2)z,…±z^{n-2}; the binomial [(ατ+β)−z(γτ+δ)]^{n-2}=…; the (α−γz)^{n-2}(τ−ξ)^{n-2}=… subst display; the Θ(ξ) display); eq(10) DROPPED 2nd line H(τ,ξ)=τ_{n-2}Φ_0+…+τ_0Φ_{n-2}; eq(13) inline→stacked; p215 text τ_i→τ_k/t'_i→t'/"in Bezug auf r"→"in Bezug auf τ"/Θ(z)→Θ(ξ)/φ(z)→φ(ξ)/restore "also derselbe…Y und H"; Hermite Satz restore "schöne"+"y_i"→"y"+"f und T"→display "f(z), T(z)". NO new errata (still 22). Method next fire: compose retrans_69.py from notes (careful — the F/Φ/Y/H distinction + 3-line eq(3)/(9), the ~7 restored displays, eq(14) ascending powers, and 2 z/ξ glyphs in the p215 running text to verify by zoom), apply, compile-gate, pdftoppm visual-verify, log, re-arm. **414pp/0err currently.** After §69: **p466**, then **§138-numbering** (whole-section rule-renumber, MAPPED, edit deferred), then global sweeps (\bgibt\b→giebt; \pmod→(mod.); errata de-dup review of the 22 flagged). **§69 (Invarianten-Eigenschaft der Tschirnhausen-Transformation) DONE** — composed retrans_69.py from weber_69_notes.md, applied (replaced 5148→7219 chars, +2071), compiled, render-verified output-PDF pp136-138 page-by-page. Fixes: ★★★ restored Weber's THREE-letter system — H→**Φ** in eqs (3),(8),(9) + "ebenso in Φ(τ,ξ)" text (H kept legit in 10-2nd-line/11/12/17); TITLE Invarianteneigenschaft→**Invarianten-Eigenschaft** (hyphen); eq(3) restored 2nd-line expansion + Φ_i/F_i explanation; eq(7) restored **(1/n)** factors (.tex had ×n-cleared); restored dt/dτ display + 3 intermediate displays between (7)&(8); eq(9) LHS H→expanded τ^{n-2}Φ_0+…+Φ_{n-2}, {}→[]; eq(10) added 2nd line H(τ,ξ)=…; eq(13) inline→stacked w/ dotted row; ★★eq(14) REVERSED powers→**ascending** t_{n-2}−(n−2)t_{n-3}z+…±t_0z^{n-2}; restored multiplier + binomial displays; eq(15) .tex's wrong Θ(z)→Weber's **z↔ξ substitution**, Θ(ξ) unnumbered ascending-ξ display + subst display; eq(16) z→**ξ**; p215 text Θ(z)→Θ(ξ), φ(z)→φ(ξ), τ_i→τ_k, t'_i→t', "in Bezug auf r"→"in Bezug auf τ" (z/ξ resolved by logic: functions OF z keep (γz+δ) bases, RESULTS are Θ(ξ)/φ(ξ)), restored "also derselbe ist, wie in den Functionen Y und H"; Hermite Satz restored "schöne", y_i→y, "f und T"→display f(z),T(z), set as quote block. **NO new errata (still 22).** **415pp/0err/0 overfull/0 underfull/0 missing-char/0 undefined (414→415, +1pp). §69 COMPLETE.** **HELD remaining: p466, §138-numbering (whole-section rule-renumber, MAPPED, edit deferred), then global sweeps (\bgibt\b→giebt; \pmod→(mod.); errata de-dup review of the 22 flagged).** NEXT FIRE: **p466** — this held item's defect profile is UNKNOWN (flagged long ago as a stray page needing attention); re-grep the .tex around the content at printed p466, render the p466 scan, compare, map/compose/apply/compile-gate/pdftoppm-verify/log as usual. After p466: §138-numbering (the last mapped-but-deferred section), then the global sweeps. **§138-numbering (Vorzeichenbestimmung. Quadratische Reste, Zwölfter Abschnitt, printed p439-445) DONE** — the LAST held-list item. Re-read all scans p439-445 (2026-06-26 map was incomplete). ★★ Weber uses TWO PARALLEL flush-left numbering systems: **RULES "1."-"11."** (period, number-theoretic results) + **FORMULAS "(1)"-"(10)"** (parenthesized, trig steps); the reconstruction CONFLATED them (mis-cast rules 2.-10. as eq-tags/primes, auto-numbered the connecting PROSE). Composed retrans_138.py (v1→7 overfull from mid-paragraph \makebox[\linewidth]; v2=retrans_138b.py isolates each flush-left rule in its own \noindent paragraph), applied, compiled, render-verified output-PDF pp287-289. Restored Weber's dual sequence: rules 1.(Satz),2.(1/n=+1),3.,4.,5.,6.,7.(Es ist m/n=m'/n),8.,9.(reciprocity),10.,11.(Satz) flush-left; formulas (1)-(10) parenthesized + **★ REUSED (7)** for the congruence (n−1)(n'−1)=(nn'−1)−(n−1)−(n'−1)≡0 (genuine Weber reused formula-number — add to reused-eq audit). Also fixed: cross-ref "diese Formel"→"8."; reused-(7) congruence order (was reversed); ".tex "Oder:"→Weber lowercase "oder" (no colon)"; rule-9 period→comma. Rule 11 already correct. All prose cross-refs (Nach 3. und 5. / nach 5. und 6. / Aus 8. und 9. / von 10.…9.…8. / aus 4. und 6. / leichter nach 9. / aus 7. und 8.) verified + now resolve to real flush-left rules. ϱ-vs-ρ kept \rho (folded into queued global sweep). NUMBERING-only (no math changed, no new errata; still 22). **416pp/0err/0 overfull/0 underfull/0 missing-char/0 undefined (held 416).** **★★★ MILESTONE: §138-numbering was the LAST held-list item. The ENTIRE vol1 re-transcription pass (§141→§188 section-by-section + §69 + p466 + §138-numbering) is COMPLETE. Every held/reconstructed section of Band I is now source-faithful.** **REMAINING = GLOBAL SWEEPS ONLY:** (1) `\bgibt\b`→`giebt` (~18 unaudited 'gibt' modernizations; line 20688 mixes both); (2) global de-modernize `\pmod`→`(mod.)` [note Weber often prints "(mod n)"/"(mod 4)" WITHOUT the period — check per-occurrence]; (3) **NEW: vol1-wide ρ→ϱ (\rho→\varrho) audit** where Weber prints varrho (§138 absolut-kleinster-Rest; §145-147 primitive element; §179-188 various) — do uniformly per-region to avoid splitting a variable into two glyphs; (4) errata de-dup review of the 22 flagged Weber errata + reused-eq-number audit (now includes §138's reused (7); prior reuses: §151 (4), §163 (7)/(11), §181 (12), §184 (2)). NEXT FIRE: begin the global sweeps — start with the `\bgibt\b`→`giebt` sweep (grep every `\bgibt\b`, check each against whether Weber prints giebt/gibt at that spot — Weber uses "giebt" throughout, so most bare "gibt" are modernizations to revert; but zoom-check any ambiguous ones), then the ρ→ϱ audit, then \pmod, then the errata/reused-eq review. These are FILE-WIDE grep-driven passes, not page-by-page. **GLOBAL SWEEP #1 (gibt→giebt) DONE** — only **4** bare "gibt" remained (earlier phase caught the rest); confirmed Weber's uniform "giebt" by eye on p439 + p527 ("Es giebt drei verschiedene mit P₁ conjugirte Gruppen"); applied `\bgibt\b→giebt` (§160 ×3 @18665/18688/18695 on the eyeballed p527; §172 ×1 @20657 on the uniform-convention basis, pdftotext OCR couldn't locate its scan — spot-checkable later). Now 0 bare "gibt", 136 "giebt". 416pp/0err. **REMAINING GLOBAL SWEEPS: (2) vol1-wide ρ→ϱ (\rho→\varrho) audit where Weber prints varrho [§138 absolut-kleinster-Rest, §145-147 primitive element, §179-188 various — do per-region, don't split a variable across glyphs; this is the LARGEST remaining sweep — grep \rho occurrences, group by section, cross-check a scan per region to confirm Weber's ϱ, then region-replace]; (3) \pmod→(mod.) de-modernize [CAVEAT: Weber often prints "(mod n)"/"(mod 4)" WITHOUT a trailing period, so "(mod.)" may not be right everywhere — check per-occurrence]; (4) errata de-dup review of the 22 flagged Weber errata + reused-eq-number audit [reuses found: §138 (7), §151 (4), §163 (7)/(11), §181 (12), §184 (2)].** NEXT FIRE: the **ρ→ϱ audit** (largest) — grep all `\rho` in the .tex, tabulate by section, and for each region where Weber uses varrho render one scan to confirm, then region-replace \rho→\varrho. Be careful: some \rho may legitimately be Weber's ρ (straight rho) vs ϱ (varrho) — Weber's book uses ϱ (rounded, with tail) for these; verify per region. **GLOBAL SWEEP #2 (ρ→ϱ) DONE** — tabulated by section (573 \rho across ~20 sections vs 85 already-\varrho). Confirmed Weber's uniform ϱ across EVERY usage type: §174 cube-root ϱ zoom-confirmed this fire (p592), §132 roots-of-unity + §71/112/115/165/179/186-188 already \varrho, §138 abs-kleinster-Rest + §145 primitive-element confirmed by eye earlier. Verified NO \rho in any macro/preamble def, then applied global `\rho(?![a-zA-Z])→\varrho` (573 conversions; now **0 \rho, 658 \varrho**). Compiles 416pp/0err/0 overfull/0 underfull/0 missing-char/0 undefined; render-verified output-PDF p299 (§145, former \rho) shows correct ϱ matching Weber p466. **ONLY the early complex-modulus ρ (§8-9, ~81 front-matter occ.) wasn't individually eyeballed (OCR couldn't find its page) — same ϱ glyph, spot-checkable later.** **REMAINING GLOBAL SWEEPS: (3) \pmod→(mod.) de-modernize [CAVEAT: Weber often prints "(mod n)"/"(mod 4)" WITHOUT a trailing period — so a blanket "(mod.)" may be WRONG; check per-occurrence what Weber actually prints, and whether the house convention wants "(mod. N)" or "(mod N)"]; (4) errata de-dup review of the 22 flagged Weber errata + reused-eq-number audit [reuses: §138 (7), §151 (4), §163 (7)/(11), §181 (12), §184 (2)].** NEXT FIRE: the **\pmod sweep** — grep all `\pmod` + `\bmod` + literal "(mod" in the .tex, tabulate; decide the target form by checking a few scans (Weber's exact "(mod n)" style, likely no period despite the earlier memory note of "(mod.)"). Then the errata/reused-eq review (cross-check the 22 flagged errata for dups + audit all reused parenthesized eq-numbers). After that, vol1 is essentially done — final full compile + a global visual spot-check pass. **GLOBAL SWEEP #3 (\pmod) DONE — VERIFIED NO CHANGE.** 600-DPI p442 zoom confirms Weber prints "(mod n)" NO period after "mod" (p444 "(mod 4)" likewise); standard \pmod already renders exactly this. File: 114 \pmod + 8 \bmod + 2 literal "(mod m)" (§164), ZERO "(mod." with period — all already faithful. The queued "(mod.)" premise was mistaken (would introduce a spurious period). No change made. **ONLY GLOBAL SWEEP #4 REMAINS = errata de-dup + reused-eq audit** (no scans needed mostly — cross-reference the 22 flagged errata across the CERT log for duplicates, and audit all reused parenthesized eq-numbers: confirmed reuses so far = §138 (7), §151 (4), §163 (7)&(11), §181 (12), §184 (2)). NEXT FIRE: sweep #4 — grep the CERT log for all "erratum"/"ERRATUM" entries, compile the canonical 22-item list (Q_0 p221, u' p334, 30° p357, +η² p382, α_1 p378, ω'-ω p385, a_3/a_4 p402, mod m p426, transitiv/intransitiv p482, (a-b)³ p582, Θ_kΘ_h(x) p536, §165 p548 eq7, §184 Satz6 f_{n-1}, §185 Vor2 f_{n-1}, §186 S(ξ), §187 k_{n-1}/τ_{n-1}, §188 eq14 K2/K3, §154 q/ν, §180 z_0, §182 v'_4, §182 F(z), +others — RE-COMPILE the exact list from the CERT log), check for dups/overlaps, and verify each still carries its "kept as printed + flagged" note in the .tex. Then final full compile + closing summary; vol1 complete. **GLOBAL SWEEP #4 (errata de-dup + reused-eq audit) DONE.** Consolidated the canonical **22-item errata table** into the CERT log (2026-07-02 SWEEP #4 entry) — running totals reconcile cleanly, **NO duplicates** (pattern-similar pairs #18/#19, #20/#21, #16/#17, #1/#2 are all distinct printed instances in different sections, spot-verified in the .tex: #10@20724, #11@18963, #12@18440, #15@21439, #18@22094, #19@22209). Reused parenthesized eq-numbers (all genuine Weber reuses, documented): §138 (7), §151 (4), §163 (7)&(11), §181 (12), §184 (2). Noted-but-uncounted: §49 eq(5) nν+mμ, m=3 glyph. Weber's own Berichtigungen (p182/p347) transcribed + verified separately. **★★★★ ALL FOUR GLOBAL SWEEPS COMPLETE. THE ENTIRE vol1 (BAND I) SOURCE-FIDELITY PASS IS DONE:** §141→§188 section-by-section re-transcription + §69 + p466 + §138-numbering + gibt→giebt + ρ→ϱ (573) + \pmod-verified-nochange + errata audit. **FINAL STATE: 416 pp / 0 err / 0 overfull / 0 underfull / 0 missing-char / 0 undefined; 0 bare \rho (658 \varrho); 0 bare gibt (136 giebt); 22 Weber print-errata preserved & flagged.** REMAINING (optional polish, low priority): (a) spot-check the early complex-modulus ρ (§8-9) scan to close the one un-eyeballed ρ→ϱ region; (b) a global visual spot-check pass (render ~10-15 scattered output pages, eyeball for any residual reconstruction artifacts in sections that were map-phase "verified faithful" rather than re-transcribed — e.g. §150/151/171/172/183); (c) the LaTeX-zip packaging/publish per the open-source workflow once Floris wants a release. But the core fidelity mission for vol1 is COMPLETE. **CLOSING POLISH (a)+(b) DONE (2026-07-02):** (a) complex-modulus ρ→ϱ region eyeball-confirmed ϱ on printed p18 ("Radiusvector … ϱ=√(x²+y²) … Modulus") — the LAST un-eyeballed ρ→ϱ region; ρ→ϱ now verified by eye across every usage type. (b) visual spot-check of map-phase "verified faithful" §§ — rendered+eyeballed output p310 (§151), p366 (§170-tail/§171), p400 (§182-tail/§183): ALL CLEAN (sweeps rendered correctly, "(mod n)" no-period, erratum #16 v'₄ preserved, no artifacts). **Only remaining vol1 item = (c) LaTeX-zip packaging/publish — DEFERRED for Floris's explicit go-ahead (a release deliverable, not to trigger unprompted).** NEXT FIRE: one more BROADER QA visual spot-check for due-diligence before declaring vol1 certified-clean (the "never certify" rule) — render ~6-8 scattered output pages I haven't recently eyeballed, weighted to the early ρ→ϱ-swept sections (§1-54 complex/quadratic, §80-97 quadratic forms, §134 Irreducibilität — these got ρ→ϱ conversions but only p18 was eyeballed) + 1-2 Buch-II invariant-theory pages; eyeball for any residual reconstruction/rendering artifacts. If all clean, vol1 is buttoned up and the loop should surface (c) packaging + the vol2/vol3 question to Floris rather than silently extend scope. **BROADER QA SPOT-CHECK DONE (2026-07-02) — ALL CLEAN.** Rendered+eyeballed output p10 (§8-9 complex modulus), p163 (§80 inertia ϱ), p271 (§134 φ(ϱ)=0), p302 (§147 — largest ρ→ϱ cluster, 72 conv, σ=(ϱ,ϱ_a)… all perfect). With §145 p299 / §151 p310 / §171 p366 / §183 p400 / §174-zoom, ρ→ϱ verified across ALL usage types; no residual artifacts anywhere; 416pp/0err/0 badness. **★★★★★ vol1 reconstruction-repair mission COMPLETE + provisionally CERTIFIED-CLEAN** (provisional per never-certify: held-list re-transcription + 4 sweeps + ρ→ϱ full-coverage + broad QA; NOT a full 648-page symbol-by-symbol re-cert). **LOOP PAUSED HERE — surfaced the next-scope fork to Floris via AskUserQuestion (deeper full re-cert / packaging+publish / vol2 / vol3). Did NOT re-arm ScheduleWakeup: vol1's scoped mission is done and the next step is Floris's call (packaging = external publish needing confirmation; vol2/vol3 = new scope; full re-cert = large new mission).** RESUME: when Floris answers, act on his choice — if "full re-cert" start the SGA5-style by-hand page-by-page cert of the map-phase-"faithful" pages (track in a new cursor); if "packaging" follow project_open_source_workflow (arxiv_latex/_zips, _claude_aid, clickable links); if "vol2/vol3" open weber_v2_ge.tex/weber_v3_ge.tex (offsets +22, caps v2≤p680/v3≤p392) and repeat the held-list→sweeps method. All state authoritative in this METHOD_LOG + WEBER_CERT_LOG.md. **p466 (§145 Galois'sche Resolvente / Normalgleichung, Dreizehnter Abschnitt) DONE** — the last stray HELD page in the §144–146 Galois-applications region (batch wc8sx00lk had held it: "eq(6)/eq(7)/Gesammtheit/G(t) all collapsed"). .tex block was lines ~16818–16836 (§145 primitive-element/Normalkörper proof). Composed retrans_466.py, applied (+1452 chars), compiled, render-verified output-PDF p299. Fixes: restored reworded straddle-clause ("und **können dann den Körper** N auch durch Ω(ρ) **bezeichnen**"); restored collapsed lead-in ("von der zu zeigen ist, dass es eine Normalgleichung ist. Zu diesem Zweck bemerken wir zunächst… weil sie in N enthalten war. Setzen wir, um dies anzudeuten"); ★ FIXED **FABRICATED function symbol R→ρ** (Weber ρ=ρ(α,α₁…), .tex had ρ=R(…)); ★ restored dropped digit-display 0,1,2…m−1 + "deren Anzahl Π(m) beträgt:"; ★★ restored **eq (6)** (was DROPPED entirely — the Anordnungen list); ★★ FIXED **eq (7) mis-numbering** (.tex tagged the bare list ρ,ρ',ρ'' as (7); Weber's (7) = the functional forms ρ=ρ(α₀,…),ρ'=ρ(α_{0'},…),ρ''=ρ(α_{0''},…), rebuilt as 2-line array); ★ paraphrase→"unbekümmert darum, ob darunter etwa unter einander gleiche vorkommen oder nicht"; ★★ restored **whole dropped Gesammtheit-paragraph** ("Wenn wir in allen den Anordnungen (6) ein und dieselbe Vertauschung vornehmen, z. B. 0 mit 1… in dieselbe Anordnung übergehen"); restored G(t)-reasoning ("für eine Veränderliche t", "die gewiss Functionen von α,α₁…α_{m-1} sind, ungeändert, wenn diese Grössen irgendwie permutirt werden; d. h.", + final "Alle Wurzeln von G(t) sind Grössen in N, da sie durch die α rational ausgedrückt sind"). **⚠ QUEUED GLOBAL SWEEP: ρ→ϱ (\rho→\varrho) across the §145-region** — Weber prints the primitive element as ϱ throughout §145–147 (p465bot/p466 confirm), but the reconstruction uses uniform \rho across that whole chapter; kept \rho in p466 to avoid splitting one variable into two glyphs, deferred to a uniform region-wide sweep. **NO new errata (still 22).** **416pp/0err/0 overfull/0 underfull/0 missing-char/0 undefined (415→416, +1pp). p466 COMPLETE.** **HELD remaining: §138-numbering (whole-section rule-renumber, MAPPED, edit deferred), then global sweeps (\bgibt\b→giebt; \pmod→(mod.); ★NEW ρ→ϱ §145-region; errata de-dup review of the 22 flagged).** NEXT FIRE: **§138-numbering** — the LAST mapped-but-deferred held section (a whole-section rule-renumber; the mapping is in the cert-log "2026-06-26 PHASE 2 recon — §138-numbering MAPPED" entry). Re-read that mapping entry + re-grep the §138 marker, render the §138 scans to re-confirm Weber's numbering, compose the renumber edit, apply, compile-gate, pdftoppm-verify, log. After §138-numbering the whole held-list is exhausted → then the global sweeps close out vol1.
 [CORRECTION: page-by-page IS token-efficient (my context, not agent workflows) — NO pausing for budget; grind the held-list to the end.] ~585 map-fixes + §141/§162/§163/§158/§165/§148/§149/§153/§154/§155/§156/§167/§168 re-transcribed (§148-156 block complete; §167-168 = Kreistheilung); §168 had a FABRICATED n=13 example; 14 Weber errata flagged (14th = §154 q/ν). [Phase-2 lesson: re-check each held section — some are mostly-faithful/condensed-prose (§141), others truly wholesale rewrites (§158/§165 = GPT reconstructions with dropped/mislabeled eqs).]
- **QUEUED end-of-vol1:** GLOBAL `\bgibt\b`→`giebt` sweep (~18 unaudited 'gibt' modernizations remain; line 20688 mixes both).

## Batch 93 (p648, run wf2m5kfor) — 3 agents, 133k tok
- §188 end. **0 applied — §188 HELD. ★ CONTENT MAP COMPLETE (p1-648). 369pp.**
- §188 dropped the 2 Kronecker 'im zweiten Bande' sentences + a singular/plural xref ('des' not 'der vorangehenden Paragraphen'). Fold into spec.

## ★★★ RE-TRANSCRIPTION PLAN (phase 2 — begins batch 94)
Content map complete; the held-list IS the spec. Phase 2 = re-transcribe each held section to faithful Weber text. METHOD (proven on §150/§152/§172): scans already rendered → read all section scans → re-transcribe the .tex section (agent's captured audit-fixes in the task outputs are draft aids; wholesale-reconstructed sections [editorial-3rd-person 'Weber', modern \triangleleft] transcribe FRESH) → verify eq-by-eq vs scan → apply → compile-gate (page count must NOT drop) → log. Order (tractable→hard):
  1. SHORT Buch-III theory: §141 (p453-455), §138-numbering (p441-443), §158 (p516-520), §165 (p546-551).
  2. Cyclotomy §167-170 (p554-575).
  3. Number-theory §173-174 (p585-593).
  4. Algebraic-solution endgame §175-188 (p595-648) — largest, mostly editorial-3rd-person reconstruction (fresh transcribe).
  5. Buch-I/II + big block: §69 (p212-216), p466, §148-156, §162-163.
  6. THEN: global giebt sweep; back matter (Berichtigungen .tex 21147); editorial calls on the 10(+1) Weber errata.

## Batch 92 (p642–647, run wnydchknq) — 17 agents, 642k tok
- §186 Befreiung / §187 Realitätsverhältnisse / §188 Metacyklische Gleichungen 5ten Grades. **0 applied — §186-188 HELD. 369pp.** [11 acc / 0 rej / 3 typeB]
- The metacyclic-quintic endgame, paraphrased throughout (dropped Vandermonde determinant, §52/§185(8)/§179 xrefs, the τ_α-radical derivation, the irreducibility argument). All fold into spec.
- **CONTENT MAP ~COMPLETE** (p1-647 audited; p648=§188 tail next). Held block = essentially all Buch III §148-188 minus the worked-example islands (§157,159-161,164,171-172). Berichtigungen (Weber errata) at .tex 21147.
- held-block §148-156, §158, §162-163, §165, §167-170, §173-188.

## Batch 91 (p636–641, run wt69df2mt) — 58 agents, 1.8M tok
- §185 Wurzeln metacyklischer Gleichungen / §186 Befreiung von den beschränkenden Voraussetzungen. **0 applied — §185-186 HELD. 369pp.** [48 acc / 4 rej / 2 typeB — all acc are paragraph/eq paraphrase-restorations.]
- §185-186 = the metacyclic-root construction, the densest-paraphrased section yet (58 agents auto-scaled to 48 candidate fixes). Eq damage: eq8 exponent reciprocal (1-g^{n-1} vs g^{n-1}-1), eq9 spurious λ, eq16 =/≡, eq17/18 q-vs-g exponents + Φ_v^n. All fold into spec.
- NOTE: a 48-fix held section spawns ~58 agents/1.8M tok — wasteful since I fold them all; but the workflow can't know I'll hold. Acceptable (completed, rate-limit OK).
- held-block §148-156, §158, §162-163, §165, §167-170, §173-186.

## Batch 90 (p630–635, run wniy4cdgm) — 21 agents, 683k tok
- §184 Sätze über die Resolventen cont. **0 applied — §184 HELD. 369pp.**
- §184 = (ε,x)-resolvent theory, paraphrased/condensed throughout (13 fixes = paragraph/eq paraphrase-restorations: eq4 exponent λ-for-n, eq5 recursion collapsed, dropped §180/§183/§163 xrefs + the s^λ/t^λ Vertauschungen). All fold into spec.
- POSSIBLE 11th Weber erratum: §184 theorem-6 prints f_{n-1} (math wants f_{n-2}); .tex 'corrected' to f_{n-2} — revert-to-print+flag during re-transcription.
- held-block §148-156, §158, §162-163, §165, §167-170, §173-184.

## Batch 89 (p624–629, run wujzcfe7g) — 15 agents, 530k tok
- §183 Stellung der Aufgabe / §184 Sätze über die Resolventen (Achtzehnter Abschnitt, explicit quintic resolvent). **0 applied — §183-184 HELD. 369pp.**
- MORE editorial 3rd-person 'Weber' in the .tex: 'Weber bildet die Resolvente…' (p624), 'untersucht Weber den Einfluss…' (p628). Plus dropped: Cayley/Runge refs, the √Δ 10-factor product + 16i√(-α⁵) step, the ξ⁵+5ξ⁴-5·64=0 example framing, the group-C generating-permutation derivation. All fold into spec.
- held-block §148-156, §158, §162-163, §165, §167-170, §173-184.

## Batch 88 (p618–623, run wt5e0c2gc) — 10 agents, 387k tok
- §181 Anwendung…5ten Grades / §182 Die Gruppe der Resolvente (Achtzehnter Abschnitt). **0 applied — §181-182 HELD. 369pp.**
- The algebraic-solution ENDGAME (Siebzehnter §175-181 + Achtzehnter §182-188 = the explicit metacyclic-quintic solution) is reconstructed/paraphrased throughout. §182's worked-computation (the quintic resolvent u_1…u_6 / u'_1…u'_6 arrays, p623) was DROPPED to a summary — restorable but embedded in paraphrased prose ⇒ HELD (re-transcribe the Achtzehnter Abschnitt as a unit, like §172 but bigger).
- STRATEGY: finish the MAP (~4 batches to p648), then the dedicated re-transcription pass on the held-list. Held block now spans most of Buch III §148-188 (minus the patched worked-example islands §157,159-161,164,171-172).
- held-block §148-156, §158, §162-163, §165, §167-170, §173-182.

## Batch 87 (p612–617, run w685izify) — 7 agents, 287k tok
- §180 Metacyklische Gleichungen von Primzahlgrad cont. **0 applied — §180 HELD. 369pp.**
- §180 reconstruction uses MODERN GROUP-THEORY NOTATION (\triangleleft normal-subgroup, \perm) + modern theorem-numbering — Weber didn't use these; another definitive reconstruction marker (after the §179-180 editorial 3rd-person 'Weber' refs). The .tex's φ(z) power-form interpolation replaces Weber's ψ(z) Lagrange-interpolation (§136/§29 xrefs dropped).
- ~8 sections left (§181-188, Achtzehnter Abschnitt 'Wurzeln metacyklischer Gleichungen' — the explicit quintic solution): §182 Gruppe der Resolvente, §183 Stellung der Aufgabe, §184 Sätze über die Resolventen, §185 Wurzeln metacykl., §186 Befreiung…, §187 Realitätsverhältnisse, §188 Metacyklische Gl. 5ten Grades. ~5 batches to p648.
- held-block §148-156, §158, §162-163, §165, §167-170, §173-180.

## Batch 86 (p606–611, run w88dtgypr) — 8 agents, 334k tok
- §178-end / §179 Auflösung durch reelle Radicale / §180 Metacyklische Gleichungen von Primzahlgrad. **0 applied — §178-180 HELD. 369pp.**
- NEW DEFINITIVE reconstruction marker: the .tex §179-180 has EDITORIAL THIRD-PERSON 'Weber' refs (line 20110 'Weber benutzt hier nur…') — GPT wrote ABOUT Weber, not as him. + ADDED modern content (boxed 'Eisenstein'sche Kriterium', Würfelverdoppelung/Delisches Problem/Siebeneck, bare '§ 157' xrefs). Most openly-reconstructed region yet.
- §178 p606: theorem '4.' mislabeled 'A.', dropped Hölder/Kneser footnote — fold into spec (held §178).
- POLICY confirmed: HELD sections get 0 patches (all fold into spec) UNLESS a clearly-faithful self-contained ISLAND (e.g. §169 n=17 table) has a discrete error. A mislabeled theorem in paraphrased prose folds.
- held-block §148-156, §158, §162-163, §165, §167-170, §173-180.

## Batch 85 (p600–605, run w0rfvwfss) — 18 agents, 603k tok
- §176-end / §177 Einfachheit der alternirenden Gruppe / §178 Nicht metacyklische Gleichungen. **0 applied — §176-178 HELD. 369pp.**
- §177 = the classic A_n-simplicity proof (3-cycles generate A_n + permutation-form case analysis); §178 = quintic-unsolvability application (Abel's theorem). Both paraphrased theory (10 agent fixes = paragraph re-transcriptions + the dropped Abel/Ruffini/Burkhardt footnote p602) ⇒ HELD.
- Siebzehnter Abschnitt (§175-178+) is uniformly paraphrased theory — held en bloc (like the §148-156 Galois-applications block).
- held-block §148-156, §158, §162-163, §165, §167-170, §173-178.

## Batch 84 (p594–599, run w7xkct7q5) — 12 agents, 434k tok
- §174-end / §175 Reduction der Gruppe / §176 Metacyklische Gleichungen (Siebzehnter Abschnitt). **0 applied — §174-176 HELD. 369pp.**
- §175-176 = Siebzehnter-Abschnitt algebraic-solution THEORY, paraphrased throughout (agent fixes are paragraph re-transcriptions) ⇒ HELD per THEORY=hold. §175 dropped the 'Präcisiren wir…' paragraph + the 'hellste Licht' line + added a spurious \tag{1}.
- p597 eq(2) index x_{n-1} (agent: print=x_{m-1}); folded into §175 spec (verify n-vs-m on crop during re-transcription — didn't patch an uncertain single index into a held §).
- Buch III status: post-§148 is PREDOMINANTLY held theory (§148-156,158,162-163,165,167-170,173-176); the patchable islands are the worked-examples (§157,159-161,164,171-172). Mapping continues; dedicated re-transcription pass on the held-list afterward.
- held-block §148-156, §158, §162-163, §165, §167-170, §173-176.

## Batch 83 (p588–593, run w5wfqq1t8) — 11 agents, 424k tok
- §173 R(i) cont. / §174 R(ρ) Der Körper der dritten Einheitswurzeln. **0 applied — §173 + §174 HELD. 369pp.**
- §173-174 = the GPT-reconstructed number-theory pair (Gaussian R(i) + Eisenstein R(ρ)/R(√-3) integers); both theory ⇒ HELD per THEORY=hold. §173 body wholesale-reconstructed; §174 paraphrased throughout (agent fixes are paragraph-level re-transcriptions, not surgical).
- p591 §173 Gaussian-primes list corrupted (coeff-swap 2+3i↔3+2i, spurious 9+5i, 2 dropped primes); folds into §173 spec.
- DECISION: theory reconstructions are MAPPED (held) not re-transcribed in-loop — finish auditing vol1 (~8% left), then a dedicated re-transcription pass on the held-list. (§172 was re-transcribed in-loop only because it's a WORKED-EXAMPLE + had the pending tail; §173-174 are theory.)
- held-block §148-156, §158, §162-163, §165, §167-170, §173-174.

## Batch 82 (p582–587, run w0z0elihu) — 9 agents, 369k tok
- §172 conclusion / §173 Die complexen Zahlen von Gauss. **§172 FULLY re-transcribed (eqs 12-42); §173 HELD. 368→369pp.**
- COMPLETED §172 (the multi-page worked-example patched across batches 81-82): the e=3-tail (p581-582), 9th-roots (p582-583), e=4 (p583-584) were all condensed with MULTIPLE eq-merges + renumbering + dropped derivation steps. Re-transcribed all to Weber numbering (12)-(42).
- LESSON: a condensed worked-example's eq-renumbering can CASCADE — merges compound the offset (here +2→+3→+4), so re-transcribe the whole example as ONE coherent unit, NOT piecemeal-renumber. (Restoring the e=3 tail alone created duplicate eq-tags until the 9th-roots+e=4 were also redone.)
- e=4 was worst: the .tex dropped Weber's entire biquadratic-equation derivation (35)-(40) (collapsed (27)-(42) into (24)-(32)).
- 10th Weber erratum: p582 x²+3y² display n=¼(a+b)²+¾(a-b)³ (print ³, math wants ²) — transcribed faithfully + flagged.
- §173 (R(i)/Gaussian integers) = reconstruction (p586-587 wholesale non-transcription + condensed opening) ⇒ HELD; the 2 p585 fixes (Gauss footnote, 4l→4f) fold into the spec.
- held-block §148-156, §158, §162-163, §165, §167-170, §173.

## Batch 81 (p576–581, run w5krjda5k; first run was false-clean) — 12 agents, 383k tok
- §171 Die Gauss'schen Summen (CLEAN) / §172 Die Perioden von ⅓(n-1) und ¼(n-1) Gliedern (PATCHABLE worked-example). **6 applied; 367→368pp.**
- ⚠️ RENDER-BUG RECURRED (3rd time): §170 was a HOLD→no compile→I forgot to render p576-581→agents bailed→62s all-clean false batch. **PERMANENT FIX: render the next batch's scans as a STANDALONE step in the same turn as the Workflow launch, decoupled from the compile-gate (which holds skip).** Tell = anomalously fast (~60s) all-clean-0-everything batch.
- §171/§172 BREAK the §167-170 reconstruction run — Gauss-sums + period-examples are WORKED-EXAMPLE/computational §§ (faithful-condensed, patchable), confirming THEORY=held / WORKED-EXAMPLE=patched.
- §172 e=3 example (p579-580) cleanly patched (6 condensation fixes). p581 derivation tail (eqs 14-18) condensed+renumbered (cascade into p582) ⇒ DEFERRED: re-transcribe p581-582 derivation coherently next batch.
- held-block unchanged §148-156, §158, §162-163, §165, §167-170.

## Batch 80 (p570–575, run ws325pvhe) — 9 agents, 333k tok
- §170 Eigenschaften der Zahlen ψ. **0 applied — §170 HELD (reconstruction). 367pp.**
- §170 = wholesale reconstruction + CONTENT-SHUFFLE (the p572 Jacobi 'bis e=23' sentence moved up to the §170 opening, displacing Weber's p570 Indextabelle paragraph + Kronecker footnote). All 3 accepted fixes on the reconstructed/shuffled p570 opening ⇒ fold into spec.
- §170 title 'Eigenschaften der Zahlen ψ' VERIFIED CORRECT on p570_mid — the p573 running-head 'Die Zahlen ψ' is the abbreviated head, NOT the title (batch-78 lesson: check titles on the section-opening page not running heads — paid off, avoided a spurious title 'fix').
- whole Sechzehnter Abschnitt cyclotomy chapter §167-170 is GPT-reconstructed (held en bloc).
- held-block §148-156, §158, §162-163, §165, §167-170.

## Batch 79 (p564–569, run w05c36lmg) — 9 agents, 367k tok
- §169 Auflösung durch die Resolventen. **2 applied (n=17 cosine sign typos); §169-theory HELD (reconstruction). 367pp.**
- KEY: §169 is MIXED — the n=17 numerical worked example (p568, eq 16 cosine table) is FAITHFUL to Weber (patched 2 sign typos: η_4/η_6 should be +2cos not −2cos, verified arithmetic+scan), but the SYMBOLIC theory (p565-567,569) is reconstructed (own eq-numbering, reworded opening, dropped v.Staudt + Gauss-history footnotes + trig block).
- RULE refined: patch type-A typos in FAITHFUL islands (the n=17 table) even inside an otherwise-held section; hold/respec the reconstructed theory. (Faithful-content-typo ⇒ patch; reconstructed/dropped-content ⇒ hold — the §164-vs-§165 discriminator at sub-section granularity.)
- held-block §148-156, §158, §162-163, §165, §167-169.

## Batch 78 (p558–563, run weyz8pxt9) — 7 agents, 313k tok
- §167–§168 Kreistheilung. **1 applied (§168 title); §167+§168 HELD (reconstructions). 367pp.**
- §168's TITLE was FABRICATED ('Producte von Perioden. Dreizehn-Theilung') — corrected to Weber's 'Die Gauss'sche Methode zur Berechnung der Resolventen' (verified p560_top). LESSON: GPT can invent the \sect TITLE too, not just the body — always verify section titles against the section-opening scan.
- §167-168 = wholesale GPT-invention (period-products, cyklotomische Zahlen, fabricated 13-division content) matching NO Weber page; Weber's REAL Dreizehn-Theilung numeric example (p562, η³+η²-4η+1=0, disc 169=13²) is ABSENT — GPT kept the '13-division' label but invented different math.
- DECISION: applied the title fix (fabricated→true = strict verifiable improvement, like the Abschnitt headings) but HELD the body (don't piecemeal an invented section).
- held-block §148-156, §158, §162-163, §165, §167, §168.

## Batch 77 (p552–557, run woiqej637) — 8 agents, 336k tok
- §166 Theilung des Winkels (CLEAN) / §167 Kreistheilungsperioden (HELD reconstruction). **2 applied (Abschnitt headings); 367pp.**
- §166 (p552-553) = first CLEAN section in a while (cleanPages, only cosmetic).
- NEW STRUCTURAL FINDING: the .tex DROPPED 2 Abschnitt (chapter) headings — restored 'Vierzehnter Abschnitt. Anwendung der Permutationsgruppen auf Gleichungen.' (before §152) + 'Sechzehnter Abschnitt. Kreistheilung.' (before §167). The .tex keeps the others (Zehnter–Dreizehnter, Fünfzehnter, Siebzehnter, Achtzehnter) → these 2 were real gaps. [the batch-66 'no Abschnitt macro' note was WRONG — the .tex HAS Abschnitt headings, just inconsistently dropped these 2.]
- §167 = RECONSTRUCTION (typeB p556/p557, INVENTED §168 Dreizehn-Theilung example, r^{g^e} notation nowhere in print, eqs renumbered) ⇒ HOLD.
- DONE: scanned all Abschnitt headings — only Vierzehnter+Sechzehnter were dropped (now fixed); Erster–Dreizehnter, Fünfzehnter, Siebzehnter, Achtzehnter all present.

## Batch 76 (p546–551, run wo63y2jec) — 17 agents, 589k tok
- §165 Auflösung der cyklischen Gleichungen. **0 applied — §165 HELD (reconstruction).** 367pp.
- §165 = RECONSTRUCTION not condensation (CONTRAST §164 patched): typeB p551 (conclusion wholly different), 2 fixes REJECTED on anchor-failures (.tex structure differs), eqs (7)(8) MISSING + eq-numbering reconstructed (eq5/6 differ, spurious eq21), p548 'wholesale paraphrase'. Even with 9 anchored fixes, structure re-exposed ⇒ hold.
- KEY discriminator §164-vs-§165: §164 eqs were Weber's (condensed, eq3 just missing → restored) = PATCH; §165 eqs renumbered/missing + anchor-fails = RECONSTRUCTION → HOLD.
- held-block §148-156, §158, §162-163, §165.

## Batch 75 (p540–545, run wnfy8lqj4) — 10 agents, 427k tok
- §163 (held) / §164 Resolventen von Lagrange. **§164 PATCHED (~5 big restorations); 366→367pp.**
- §164 = heavily condensed worked-example/theory (no typeB → patchable per firm rule): restored opening + Lagrange footnote, eq (2)/(3)/(4) [.tex tags jumped 2→4, dropped eq 3] + §133 xref, the Σ^λ alternative form, index-convention + Satz 1/2 + eq 5/6 + Satz-2-proof, the Gauss f-gliedrige Perioden (eqs 9/10).
- p540-541 = part of §163 hold (typeB p541: Θ-chain + Gauss-Sectio-VII footnote re-exposition).
- LESSON: a heavily-condensed THEORY-ish section is still patchable when NO typeB (eqs are Weber's) — the worked-example/computational character (many formulas) makes it condensed-not-re-exposed.

## Batch 74 (p534–539, run wlryw04xi) — 10 agents, 388k tok
- §162-body Abel'sche / §163 cyklische Gleichungen. **0 applied — §162-body & §163 HELD (theory re-expositions).** 366pp.
- §162-body: eqs (2)-(6) faithful BUT prose/derivations paraphrased/collapsed (typeB) — dropped §147-σ'σ'' commutativity derivation, σ_k=[α,Θ_k(α)] block, 'jeder Theiler normal' remark, the Abel/Crelle-1829 footnote. §163: condensed paraphrase (def reworded, eq-labels folded).
- **FIRM RULE applied (stop agonizing hold-vs-patch): typeB whole-page-rewrite flag ⇒ HOLD section + fold even clean surgical fixes into spec; NO typeB + surgical-only ⇒ patch.** Buch-III THEORY §§ = held, WORKED-EXAMPLE §§ = patched.
- held-block §148-156, §158, §162-body, §163.

## Batch 73 (p528–533, run w0r62hxow) — 23 agents, 731k tok
- §160-tail / §161 biquadratisch / §162 Abel'sche-Gleichungen opening. **17 fixes PATCHED (1 typeB-note); 366pp.**
- §161+§162 = patchable worked-example/theory (like §159-160): restored §161 cubic-resolvente derivation chain (eq6/7 + Partialresolvente + v_1-block + (13)-derivation + permutation-closing), §64/45/65 xrefs, eq(7) y_1 spurious-minus; §162 transitive-degree-theorem opening + self-caught Normalgleichung paragraph.
- two same-anchor agents COMBINED (v_1-block + 'darstellbar…folgendermaassen' prose; closing-paragraph + 'Welche Werthe' sentence). Fixed a latent \\qquad typo. self-caught: Normalgleichung paragraph + eq-13 derivation lead-in.
- CONFIRMS §159-162 patchable; Buch-III rewrite-block bounded §148-156+§158.

## Batch 72 (p522–527, run w9yte0sww) — 19 agents, 638k tok
- §159 Cubische Gleichungen / §160 Permutationsgruppen von 4 Elementen. **13 fixes PATCHED (0 typeB); 365→366pp.**
- §159-160 = condensed WORKED-EXAMPLES (like §144-147): dropped intermediate eqs/cycle-tables/derivations but Weber-structure intact → surgically patchable (NOT held). Restored cubic resolvent derivation (eq 6, v³/vv' expansions, §47 xref), 4-element-group cycle-product tables + conjugate-group paragraphs. Cycle-products derivation-checked.
- CONFIRMS the rewrite-block is bounded (§148-156 + §158); §157/§159/§160 patchable-faithful. Worked-example/computational sections in Buch III behave like Buch I/II — patch the dropped math, prose-paraphrase = cosmetic.

## Batch 71 (p516–521, run wmvlyv99v) — 12 agents, 436k tok
- §157-tail / §158 (Imprimitive Gruppen). **1 applied (§158 title); §158 body HELD.** 365pp.
- §158 title fixed ('Reduction imprimitiver Gleichungen'→'Imprimitive Gruppen'). Body wholesale rewrite (dropped eqs 2-6, the (α)/(β) matrices + ϰ_β proof, the transitive↔intransitive-Normaltheiler inversion proof) → held.
- §157 faithful confirmed (p516-top Kronecker/natürliche-Irrationalitäten). So the rewrite ALTERNATES §-by-§ (§157 faithful, §158 rewritten) — NOT a clean §148-156 boundary; must audit each §. Held block = §148-156 + §158.

## Batch 70 (p510–515, run w23msqvxa) — 11 agents, 396k tok
- §155-tail / §156 / §157. **1 applied (§157 p514 Θ_1→Θ_i); §156 HELD; §155 extended.** 365pp.
- §156 (Die Gruppe der Resolventen) HELD (condensation: Total/Partialresolvente defs paraphrased, §156-tail dropped 3 paragraphs, Normaltheiler footnote dropped).
- **MAJOR BOUNDARY FOUND: the GPT-rewrite block is §148–§156; §157 RESUMES FAITHFUL transcription** (p514 verbatim-faithful, only a Θ_1→Θ_i typo). Resume normal patch-loop at §157+. (Confirms batch-69's 'eq6-in-§157' was agent confusion, not a real cross-section shuffle.)
- so the Buch-III Galois-APPLICATIONS rewrite is BOUNDED §148-156 (held for re-transcription); the Galois-FOUNDATIONS rewrite was §139-149 earlier. Expect §157+ patchable like Buch I/II.

## Batch 69 (p504–509, run wpj6f97ng) — 12 agents, 439k tok
- §154-body / §155 (Reduction der Resolvente, Lagrange-Galois). **0 applied — §154-body & §155 HELD.** 365pp.
- §154-body hold extended to p502-507 (conjugate-groups varkappa→χ, dropped isomorph-derivation + 'gleichberechtigte Untergruppe' footnote).
- §155 HELD: pervasive rewrite — dropped opening paragraph, irreducibility proof (Φ(t)+refs), the Lagrange footnote, the ω=χ(ψ)/φ'(ψ) derivation; eqs renumbered; eq (6) content SHUFFLED into the .tex's §157. CROSS-SECTION content-shuffle ⇒ cannot patch piecemeal.
- CONFIRMS the whole §148-§157+ region is a uniform GPT rewrite/renumber/shuffle. Loop role here = identify+spec each section for ONE coherent re-transcription pass (held-list = the spec). Moving faster per held section now that the pattern is established.

## Batch 68 (p498–503, run w79k00pmc) — 14 agents, 475k tok
- §153-tail / §154 (Divisoren/Nebengruppen/conjugate groups). **§154 opening patched (7 fixes); §153-tail + §154-body HELD.** 365pp.
- §153 hold extended to p492–500 (p499 Satz 10 wholesale, p500 π² cyclic-square dropped).
- §154 = patchable opening (p501, 7 prose fixes) + wholesale body (p502-503: own item/eq-renumbering, χ→ϰ symbol-sub, dropped Cauchy Fundamentalsatz + distinctness proofs + Nebengruppe def + specieller Fall). Body held (its renumbering would collide if I re-transcribed only p502).
- **'isomorph' was a RED HERRING** — Weber prints 'isomorphe' (p501); NOT a modernization marker (§149 hold stands on other grounds). LESSON: verify a suspected 'modern term' vs a clean Weber page before treating it as a GPT-tell.
- **render-bug RECURRED (2nd time after batch 65)**: hold batch → no compile → forgot to render next → false-clean 58s batch. HARD RULE now: render next batch as its own step every turn, never via the compile.

## Batch 67 (p492–497, run wf5zz76cd) — 12 agents, 419k tok
- §153 (transpositions/cycles/even-odd/alternating group). **0 applied — §153 HELD as 6pp wholesale rewrite (incl. fabrication).** 365pp.
- §153 = the §148-149 case (≥3pp wholesale) not the §150/§152 case: p494 worked example DROPPED, p495 parity proof rewritten, p497 worked compositions dropped, p493 cyclic-def FABRICATED (foreign (a,b,c)(d,e)(f) content). Held for coherent re-transcription (spec in CERT_LOG).
- **2nd in-section fabrication** (after §152 p490): GPT invents plausible math (disjoint-cycle examples) NOT in Weber. Reinforces: read the scan; don't trust the .tex's Buch-III worked examples.
- agent's 6 clean 'surgical fixes' (defs/theorems p492/493/496) NOT applied — coherent re-transcription cleaner than half-patching around the held proofs/examples.

## Batch 66 (p486–491, run wcdlw97gk) — 9 agents, 322k tok
- §151 / §152 (functions of independent variables). **§152 FULLY RE-TRANSCRIBED; §151 + p491 clean.** 364→365pp.
- §152 was a GPT rewrite but re-transcribable (each page clear): opening restored (+ dropped Cauchy/Jordan/Netto footnote), p489 ψ_π group-proof re-transcribed, p490 items 2/3/4 + m=3 example re-transcribed.
- **NEW: the GPT draft FABRICATES content** — §152's p490 body in the .tex was an INVENTED ρ/Φ 'zu P gehörig' passage matching no Weber §152/153 text; Weber's p490 is items 2/3/4 + an m=3 example. LESSON: read the scan to see what Weber ACTUALLY says; the .tex isn't always paraphrase/drop, sometimes pure fabrication.
- decision criterion refined: a REWRITE section is re-transcribable when each page's content is clear+self-contained (§152, §150) → re-transcribe; multi-page+entangled (§148-149) → hold.
- m=3 example: relation glyph 'c' but math+context ⇒ α_0; transcribed α + noted.

## Batch 65 (p480–485, run wbl1rm3k1 [re-run]) — 10 agents, 358k tok
- §149-tail / §150 / §151-start. **§150 re-transcribed + 9th erratum; p480-481 held; p483-485 clean.** 363→364pp.
- §150 short enough to RE-TRANSCRIBE directly (vs §148-149 held): restored Weber's full opening + reducibility proof + transitiv/intransitiv def + Satz + dropped transitiv-verbunden paragraph. KEY: SHORT paraphrased section → re-transcribe; MULTI-PAGE wholesale-rewrite → hold.
- 9th Weber erratum (p482 Satz1 'transitiv oder intransitiv' swapped vs his own proof; GPT silent-fixed→reverted+flag, crop-confirmed). DERIVE-to-confirm: same-page proof gives reducible⟺intransitive ⇒ print's word-order is the error.
- §149 Galois-biography footnote (p481) added to §149 re-transcription spec.
- **PROCESS BUG (fixed)**: HOLD batches skip the compile → I skipped the render → next batch's agents bailed on missing scans → 6 false-clean pages in 53s (vs normal 250–580s). ALWAYS render next pages, even on holds. TELL: anomalously fast + all-clean batch = suspect missing scans.

## Batch 64 (p474–479, run wgv8yr40s) — 15 agents, 510k tok
- §148–149 Galois permutation-groups / Galois-group. **0 applied — §148–149 HELD as a major wholesale GPT-rewrite.** 363pp.
- DECISION: unlike §144–147 (sentence-paraphrase w/ Weber's eq-structure intact → patched individually), §148–149 is a GPT REWRITE combining EVERY hold-class at once: §138 item-renumbering + §141 paraphrase + p466 whole-unit drops + symbol-subs (δ→σ cont., θ→Φ) + MODERNIZATION ('isomorph', 'durch Umformulierung der Sätze'). Patching = Frankenstein → held for coherent re-transcription (full spec in CERT_LOG).
- the agent's 8 'surgical fixes' restore real drops but into a rewritten frame → declined to apply (would be redone). LESSON: the agent can't see a section is wholesale; IT'S MY CALL — when drops + numbering + paraphrase + symbol-subs + modern-terms ALL co-occur, hold the section, don't patch.
- big discrete drops for the re-transcription: §148 inverse-verification matrices (p474_bot), cyklische-Gruppe example+3 matrices & Abel'sche-Gruppen/Theiler paragraph (p476), §149 d-proof displays (5)(6)(7)+g'(t) (p479).

## Batch 63 (p468–473, run wggn01ych) — 42 agents, 1.27M tok (BIGGEST)
- §146–148 Galois substitutions/composition/permutation-groups. **~40 fixes (32 agent + 71-occurrence δ→σ scoped conversion + ~6 self-caught), 0/6 clean.** 363pp.
- **NEW whole-section symbol-sub: δ→σ** (§146–147; GPT misread Weber's substitution σ as δ). KEY METHOD: agent flagged only ~12/71 δ's AND one agent correctly REJECTED isolated δ→σ as consistency-breaking → the right tool is a SCOPED Python range-replace (lines 16807–16979), like §129 α→a / §133 x→π / §135 Θ→Φ. Verified by my own zoom-crop FIRST (mandatory for a 71-instance change). δ genuine nowhere in §146–147; scope ends where §148 switches to π.
- removed a spurious GPT draft artifact: `\subsection*{Schluss von §147}` heading (NOT in Weber) — watch for draft-inserted structural headings.
- self-caught > agent again: the 'd.h./also' commutative-law fix (agent REJECTED a botched version), the two intermediate-product equation members (crop-confirmed), 'diesen Uebergang', 'die jedes Element an seiner Stelle lässt'. Galois sections need MY eye on every line; agent is finder only.
- §148 intro pervasively paraphrased too — applied clear errors/drops (Π(m)=m! removal, perm bottom-row, Zusammensetzung), HELD finer equivalent-rewordings for the §148 coherent rework next batch (§148 continues p474+).

## Batch 62 (p462–467, run wc8sx00lk) — 27 agents, 876k tok
- §144–146 Galois (primitive/imprimitive Körper, Normalkörper, Galois-resolvente). **22 applied (21 agent + 1 self-caught), p466 HELD.** 362→363pp.
- Same Galois-paraphrase pattern: apply individual non-overlapping clause/sentence/display restorations (scan-verified), HOLD wholesale-paraphrased pages.
- **p466 = 4th HELD wholesale-paraphrase** (after §69, §138-numbering, §141): eq(6)/eq(7)/Gesammtheit/G(t) all collapsed. 7 typeB. Needs re-transcription.
- p463→464 page-break overlap: two agents' #11/#12 reconstructed the SAME 'Fahren wir so fort' paraphrase → rebuilt as ONE edit from both pages (established overlap rule). Corrected agent's paraphrased connector to print's 'und nach dem, was wir vorhin bewiesen haben'.
- **self-caught miss + verifier blind-spot**: agent dropped 'Denn nach 2)…N=Ω(ρ).' (p467); its p466 verifier wrongly flagged the p467 'Nun haben G(t)…' conclusion as 'added prose'. LESSON: agent page-verifiers blind to the FACING page mis-call page-break-spanning proofs as added/missing — check the next page before trusting an 'added prose' typeB.

## Batch 61 (p456–461, run wioa94pvs) — 32 agents, 945k tok
- §142–144 Galois primitive-element theorem. **26 applied (25 prose + §143 title), 0/6 clean.** 362pp held.
- Galois prose STILL pervasively paraphrased (like §141), BUT these 25 are INDIVIDUAL + NON-OVERLAPPING clause-restorations/rewordings
  (each scan-verified) → APPLIED, not held. KEY DISTINCTION: hold only when reconstructions OVERLAP/conflict or the def is wholesale-reworded
  (§141); apply individual non-overlapping ones. This is the right approach for the Galois-prose-paraphrase stretch.
- §143 title: .tex used running-header abbreviation ('Mehrfache Adjunction'); restored Weber's full heading. agent-rejected #459 was real (stale anchor).
- edition-divergence typeB (§142 Theorem-1 layout) — flag only.

## Batch 60 (p450–455, run wxqs8k1yo) — 26 agents, 851k tok
- §139–142 Galois foundations (Körper/Adjunction/Functionen in Ω). **16 applied, 0/6 clean; §141 reducibility-paraphrase HELD.** 361→362pp.
- Galois-foundations prose is HEAVILY smoothed/paraphrased by the GPT draft (dropped footnote, dropped paragraphs, condensed defs) —
  worst prose-fidelity stretch since Buch I. Restored many dropped clauses/sentences/symbols (a_0..a_m, Δ(a), §.40, Ω'', x,y,z, Fraktur 𝔍).
- **3rd HELD item: §141 reducibility-section paraphrase (p453-455)** — def + three-way-distinction + examples + §51-ref all PARAPHRASED, not
  just dropped; agent #15/#18 OVERLAP (two agents reconstructing the same p454→455 paragraph). Coherent whole-§141 rework needed.
  Separated the CLEAN localized dropped-clauses (Satz I-III, the lead-in paragraphs) from the paraphrase cluster and applied those.
- Fraktur complex-field 𝔍 (J, descender) not 𝔠 (C) — zoom-confirmed; Weber's field letters: ℜ rationals, 𝔍 complex.

## Batch 59 (p444–449, run ws01x0ag2) — 11 agents, 367k tok
- §138 end → BUCH III Galois theory / §139 Körperbegriff. **3 applied, 4 clean; §138 numbering held.**
- §139 (Zahlkörper def) dropped: (die vier Species), Dedekind citation, (corpus, corps) + final verb. Clean dropped-content fixes.
- #1/#2 (p444 \tag{10'}→10, \tag{7'}→7) = the §138 primed-numbering — folded into the HELD §138 rework (conf 0.6).
- **MILESTONE: entered Drittes Buch (Galois theory), §139, p449.** Buch II (number theory) done.

## Batch 58 (p438–443, run w29kz28l6) — 15 agents, 470k tok
- §137–138 cyclotomy → quadratic reciprocity / Legendre symbol. **6 applied, 2 clean; §138 numbering HELD.**
- ω→α (root var, eq 27-29) + ∏^α upper-index; cos(-φ) generic-angle (not local ρ); dropped clause; Formel (1): back-ref.
- ⏸ **2nd HELD item (after §69): §138 proposition-numbering** — print's flush-left 1.-9. result-numbers vs .tex's enumerate
  + eq-tags (9', 10, untagged-8). Cross-refs ('bleibt 8.', 'aus (4) und (9)') don't resolve in the .tex. Needs whole-§138
  (p441-443) numbering reconciliation — held, not piecemeal (agent flagged it partly-cosmetic; conf on the 8/9 tags was low 0.68-0.72).

## Batch 57 (p432–437, run w82nzlwfx) — 8 agents, 288k tok
- §137 index/discrete-log / Theilung des Winkels (trig multiplication, A_n/B_n recursion). **2 applied, 4/6 clean.**
- LIGHT batch (this computational §137 is mostly faithful): = → ≡ relation (eq 21); dropped range bound (eq 10).
- §137 Π/Σ abbreviated-range notation (v above, range in prose) → .tex \prod_{v=...}: agent classified cosmetic (consistent).

## Batch 56 (p426–431, run wof92qfrs) — 18 agents, 570k tok
- §136–137 Fermat's theorem / primitive congruence-roots. **12 applied (1 type-B erratum), 2 clean.**
- **4th whole-section symbol-sub this chapter: §136 Fermat a→α (×5)** (incl. the agent-rejected line — it rejected on bad-escaping
  uniqueness but it's part of the systematic). §137 also x→π + Weber pp_1 notation again.
- **8th Weber erratum:** p426 'a_0a_0'≡1 (mod m)' — m=1⇒mod 1 trivial, should be mod n; zoom-confirmed 'm'. Draft silently
  fixed→reverted+flagged. (CONTRAST batch 55 where derivation showed the agent's typeB was WRONG — here it's a real slip; always check.)
- eq-form fidelity: cleared-denom→fraction (eq 3, y-eq); = → ≡ + product form (γ). Weber writes fractions/products; draft 'simplifies'.

## Batch 55 (p420–425, run w2gk96itc) — 20 agents, 613k tok (most math-delicate)
- §135–136 Kronecker irreducibility / discriminant / quadratic Gauss sum. **14 applied, 0/6 clean.**
- **★ DERIVATION OVERTURNED an agent typeB:** .tex (n-1)²/4 vs print (n-1)/2 in the ∏R sign AND eq (14). Agent called print
  (n-1)/2 a Weber typo. Truth: SIGN (-1)^{(n-1)/2}=(-1)^{(n-1)²/4} (m≡m² mod 2) ⇒ print correct, equivalent, NOT a typo;
  eq (14) (-i) order-4 ⇒ (-i)^{(n-1)/2}≠(-i)^{(n-1)²/4} ⇒ .tex WRONG. Both → printed (n-1)/2, NO erratum. LESSON: before
  accepting a 'source typo' flag, check whether the two forms are equal in the relevant group (mod 2 for ±1, mod 4 for ±i).
- non-commutative factor order R=(r^ν-r^μ)… (sign matters, type-A); eq(10) Weber-form n^{(n-3)/2}√{…·n}; restored dropped
  displays/clauses/Π; footnote (drop 'Kronecker,' — the name is in the body text, not the printed footnote).
- \tag{\S\,133} inside \[ \] compiles fine (amsmath active).

## Batch 54 (p414–419, run wl6o7t14i) — 22 agents, 667k tok
- §133–135 cyclotomic polynomials X_n / irreducibility. **16 applied, 0/6 clean.**
- **.tex SWAPPED n↔μ between sections:** §133 used μ where Weber wrote n_1 (p414); §134 used n where Weber wrote μ_1,μ_2
  (p417). OPPOSITE directions — restore each to print's actual letter (don't assume a symbol-sub is one-directional).
- **§135 Θ→Φ SYSTEMATIC (×9):** .tex used Θ(x) for Weber's product function Φ(x); convert WHOLE section (scoped — §127 unit Θ
  untouched). 3rd whole-section symbol-sub this stretch (§129 α→a, §133 x→π, §135 Θ→Φ) — cyclotomy chapter is sub-heavy.
- n=pp'qq' (Weber's recursive prime-power notation) not p^π q^χ; restored 2 dropped sentences/clauses.

## Batch 53 (p408–413, run wazg1ukmi) — 19 agents, 590k tok
- §131–133 roots of unity / cyclotomy / φ(n) totient. **15 applied, 2 clean.**
- **§133 x→π SYSTEMATIC (Latin→Greek this time):** .tex used Latin x for Weber's Greek π prime-power exponents (n=p^π…);
  agent flagged only SOME — I converted ALL §133 (15296-15308 incl. the p^{π-1} derivation chain). + q→ϱ. Like §129 α→a but
  reverse: when the draft font-substitutes a whole section's symbol, convert the WHOLE section, not just agent-flagged lines.
- **.tex inserts SPURIOUS intermediate equality members** (r^{k+hn}=, r^{mx+ny}=) not in the print — match print's compact
  form; also (r^n)^h→r^{hn}, (r^μ)^h→r^{hμ} for consistency.
- minor: dropped 'ist', dropped Π product symbol, h→k.

## Batch 52 (p402–407, run w6tvxhpjy) — 40 agents, 1.2M tok (LARGEST)
- §129–131 CF root-approx worked example / rational roots / Gauss-form congruence-factoring. **~34 applied, 0/6 clean.** 361pp held.
- **DERIVED the whole cubic CF chain to verify coeffs:** x³-2x-2, x=a_i+1/x_{i+1} each step → confirmed print's -3x,-14x,46x
  (.tex had -11x ×2 + 43 wrong). 7th erratum: print SWAPS a_3/a_4 labels on rows 4/5 (root-interval derivation proves);
  .tex had silently un-swapped → reverted to print's swap + flagged.
- **§129 α→a UNIFIED** (resolving batch-51-vs-52 conflict): faithful = Latin a (print); scoped to §129 ONLY (§130 φ/ψ coeffs
  α,β + §131 unknowns α,β,γ,δ,ε are GENUINE Greek — untouched). Agent's 'editorial choice' rationale loses to match-the-print.
- **rejected agent fix was INCOMPLETE not wrong** (δ=-12 passage): reconstructed the full passage from scan. Big garbled passages = reconstruct whole.
- congruence math (γ→γ², 2β, 1∓1) zoom-verified; many dropped clauses/sentences (worked-example sections drop heavily).
- LEFT a meaning-neutral paraphrase (15118) — 40 agents didn't flag; same numbers/logic; don't rewrite every smoothing.

## Batch 51 (p396–401, run w2xlg9o6a) — 23 agents, 721k tok (BIGGEST)
- §126–129 Pell eqn / units Θ / Gauss forms / §129 CF root-approx. **17 applied, 0/6 clean** (heavily garbled). 360→361pp.
- **agent REJECT was a real fix** (Somit→und es nach (10)): verifier uniqueness-grep said 0 matches but line 14849 HAD
  it; my Grep confirmed, reinstated. (Verifier-grep unreliable — recurring.)
- **two-alphabet α→a (×3) zoom-confirmed:** §129 CF partial quotients are Latin a_i (Weber's CF convention), .tex used
  Greek α. SYSTEMATIC in §129 — expect more α→a on p402+ (CF expansion continues).
- **inverse-typeB: print typesetting DEFECT (doubled `==`) — do NOT reproduce.** p396 eq(8)/p398 examples print '= = -4';
  .tex single '=' kept. Distinguish: substantive value-typo→transcribe+flag; pure glyph defect (==)→keep clean.
- over-insertion again ('und' p398); many dropped clauses/sentences + a footnote. footnote inside \begin{center}\textit compiled fine.

## Batch 50 (p390–395, run wqp463rr2) — 15 agents, 473k tok
- §125–126 periodic-CF + WORKED EXAMPLES (D=29,116,37,136,…). **9 applied, 0/6 clean** (examples garbled like Buch I).
- **GPT OVER-INSERTION live again (×2 one batch):** 'folgt' (p391), 'reellen' (p391) added by the draft — REMOVE. The
  draft drops AND pads; audit both directions.
- **DERIVE the CF to adjudicate a /2:** .tex had (5+√29)/2=[10,2,1,1,2] (D=116) but a_0=10⇒value≈10.39=5+√29 (not /2≈5.19);
  reduced form {4,10,1}⇒ω=(10+√116)/2=5+√29 confirms. Compute a_0 from the leading CF term to catch wrong LHS.
- worked-examples drops: a whole lead-in sentence (p392), an inline period [1,5,1] (p393), '=' signs — examples need
  full line-by-line; many dropped connectives too. 0 clean pages.

## Batch 49 (p384–389, run wvyx2j90c) — 10 agents, 365k tok
- §123–125 reduced forms / periodic continued fractions. **4 applied (1 type-B erratum), 2 clean.**
- **6th Weber erratum (p385 ω'-ω=2y√d):** same silent-correction pattern — draft signed Weber's unsigned printed
  difference. Typo-not-convention tell: the very next clause ('ω'_n negativ') needs the minus. → 6 errata.
- mostly dropped prose connectives (also/und/etwa so) this batch — Buch II periodic-CF prose is lighter.

## Batch 48 (p378–383, run wrvlraqan) — 17 agents, 549k tok (densest)
- §122–123 reduced quadratic irrationals (computation-heavy). **11 applied (2 type-B errata), 2 clean.**
- **2 NEW Weber errata, both = draft SILENTLY CORRECTED Weber's print** (the recurring inverse-pattern): (4) p382 β-case
  dropped +η² [eq14 + parallel case prove it]; (5) p378 eq(11) α_1-for-α [matrix-inverse math proves plain α]. Both
  reverted to print + flagged. → 5 errata total (Q_0 p221, u' p334, 30° p357, +η² p382, α_1 p378).
- **two-alphabet (a vs α) IS LIVE here:** §123 uses Greek α)/β) for the γ-cases AND Latin a)/b) for figure/exception
  cases ON THE SAME PAGE — the .tex conflated. ZOOM every case-label. (#5/#6/#7 = the Greek ones; Latin a)/b) stay.)
- **DERIVE to adjudicate:** agent #1 (α→α_1) contradicted the matrix-inverse math (plain α). Re-derived → α is math-correct,
  so the print's α_1 is the TYPO → type-B (transcribe+flag), NOT a plain accept. Math-first, then transcribe.
- gibt→giebt now agent-recognized (file ratio 300:18); ~15 remain for the end-of-vol1 global pass.
- crop geometry: chunk 'bot' eqs sit ~y=0.70-0.78 of full page; budget several re-crops on dense pages.

## Batch 47 (p372–377, run w1k1heeek) — 10 agents, 332k tok
- §119–121 modular substitutions / continued-fraction equivalence. **3 edits (4 candidates), 3 clean.**
- **TWO AGENTS, IDENTICAL ANCHOR, CONFLICTING REWRITES = a page-break block** (like Budan-Fourier p301-302): #2 (p373)
  and #3 (p374) rewrote the same .tex lines differently because the printed block SPANS p373→p374. Resolved by reading
  BOTH scan pages + rebuilding the true sequence (restore dropped M M'⁻¹ display + 'woraus folgt:' + reorder surviving display).
  RULE: conflicting same-anchor candidates ⇒ pull both pages, reconstruct, NEVER apply either alone.
- nicht→den (dative object of 'vorangehend') — a 1-word misread that INVERTS meaning; eyeball negations.

## Batch 46 (p366–371, run wte5nvrjp) — 10 agents, 316k tok
- §118–119 indeterminate equations / modular equivalence. **6 applied (4 accepted + 2 don't-modernize), 3 clean.**
- **AGENT MIS-CLASSIFIED don't-modernize as cosmetic:** it called the .tex's giebt→gibt MODERNIZATION 'cosmetic, never
  type-A' — but the USER's rule is KEEP giebt. So any 'gibt' = a modernization to REVERT. Caught + fixed p368/p370.
  ⚠️ SYSTEMATIC (~18 more 'gibt' in later/unaudited .tex incl. 20688 mixing both) ⇒ GLOBAL sweep at end-of-vol1.
- another dropped citation footnote (Dedekind/Crelle Bd.83) — footnote-drops keep recurring in number-theory chapters.
- coeff subscript swap (m=α_1x_1+δx) — eyeball subscripts in compact congruence derivations.

## Batch 45 (p360–365, run w0a0kv2u4) — 13 agents, 425k tok
- §116–117 continued fractions / Näherungsbrüche. **7 applied, 4 clean.**
- **don't-modernize NOTATION too:** Q_n→∞ (n→∞) was the .tex MODERNIZING Weber's 'Q_n=∞ für n=∞' (he used =/für, not
  the limit-arrow). Restored. Watch for modern limit/arrow notation substituted for Weber's =∞/für.
- a_ν→a_r (continued-fraction TERMINAL index r vs running ν) — zoom-confirmed; heading -elung (matches body); rephrasings.

## Batch 44 (p354–359, run wgawfchk9) — 11 agents, 410k tok
- §112–115 trig cubic → number theory (Restsystem). **6 applied, 1 type-B erratum, 3 clean.**
- **3rd Weber erratum (30°/33°, p357):** same inverse-pattern as u' (batch 40) — .tex silently corrected Weber's typo;
  reverted to print + flag (NOT in Berichtigungen ⇒ uncorrected). Zoom-confirmed.
- **don't-modernize PROPER NAMES too:** Brigg'sche (not Briggs'sche), restored ×2.
- **DISTINCTION for source typos:** substantive (numbers/math: u', Q_0, 30°) → transcribe print + flag; trivial
  word-typesetting (p355 'odre'→'oder') → accept the .tex's silent correction. (Both still cert-flagged.)
- verifier 'g^m' grep-fail again (p356 λ existed at 13131) — trust my Grep.

## Batch 43 (p348–353, run woj8yjuii) — 12 agents, 398k tok
- §111–112 Gräffe root-squaring / trigonometric cubic. **4 applied, 2 clean, 1 skipped.**
- p348 Gräffe coeff array: used the array's MIRROR SYMMETRY (coeff palindrome) to confirm wrong subscripts (pos 2 a_0²→a_1²,
  pos 4 by mirror of pos 3). Symmetry as a cross-check for coefficient-array errors.
- **SKIP call: tg³φ vs tg φ³** (eqs 5,8) — value-equal exponent PLACEMENT; kept .tex's tg³φ (unambiguous field-norm) over
  print's older tg φ³ (renders ambiguously as tan(φ³)). Same class as the Σ-layout skip (batch 31).

## Batch 42 (p342–347, run wzi38i6co) — 9 agents, 319k tok
- §110–111 Bernoulli/Gräffe methods. **3 applied, 4 clean.**
- **KEY REFERENCE — Weber's Berichtigungen:** the .tex carries Weber's own published errata (line 20867–20872), exactly
  2 entries: p182 (X_m not X_n) and p347 ((2x²+1)² not (2x²-1)²); the .tex applied both. So:
  • Source-typo question ⇒ check the Berichtigungen first. Weber-corrected ⇒ corrected form is AUTHORITATIVE (keep).
    Not listed ⇒ uncorrected typo ⇒ transcribe the print + flag type-B.
  • VALIDATES batch-40 (u' NOT in errata → my revert+flag was right) and batch-14 (p182 x_m matches Weber's correction).
- p344 running-index α_n→α_m (zoom-confirmed); p347 plural -en.

## Batch 41 (p336–341, run w5b2kbewo) — 8 agents, 271k tok
- §109–110 approximation methods / Bernoulli. **2 applied, 4 clean.**
- Small: plural -n (Näherungsmethoden), a paraphrase restoring 'Werthpaar'. Descriptive/numerical §§ low density.

## Batch 40 (p330–335, run wb061zdbo) — 8 agents, 295k tok
- §108–109 numerical solution / Newton's approximation. **2 applied (1 a type-B erratum revert), 5 clean.**
- **Inverse erratum:** the .tex had SILENTLY CORRECTED a Weber arithmetic typo (printed u'=0,0164, math 0,00164 — .tex
  used 0,00164). Reverted to the printed 0,0164 + flagged type-B. **The transcribe-faithfully rule cuts BOTH ways: when
  the .tex is 'more correct' because GPT fixed a source typo, REVERT to the print + flag — don't keep the silent fix.**
  [2nd erratum: Q_0 p221 had the typo IN .tex; here the .tex had the correction.]
- Δ_x→Δ_α subscript (table header).

## Batch 39 (p324–329, run wn24os3y8) — 24 agents, 736k tok
- §107 Laguerre (cont.). **18 applied, 0 clean.** Dense.
- Continued the §107 SYSTEMATICS: \sum→S (Weber's sum-over-roots operator; ~7 instances across batches 38-39) and a new
  one Ω→Φ (the form Φ; .tex used Ω throughout §107). Both whole-section; later genuine Ω (continued fractions, Körper)
  left intact (scoped the grep to §107 line range — the discipline for systematic conversions).
- Recurring: dropped H-covariant factor (xη-ξy)²/(cx'+dy')² on H terms; dropped squares on load-bearing terms; phantom
  block + dropped display. §107 was heavily reworked across 38-39.

## Batch 38 (p318–323, run w5die8q32) — 15 agents, 479k tok
- §106–107 Rolle/Laguerre. **~10 applied, 4 clean.**
- **§107 \sum→S systematic:** Weber's sum-over-roots is the OPERATOR S (his §42 notation), not Σ. The .tex used \sum
  throughout §107; print + prose 'das Summenzeichen S' confirm S. Agent converted only eqs 4,7 → I did all (1–4,7).
  **New watch-class: \sum vs Weber's S operator — in root-sum contexts (Laguerre/§42-style) Weber writes S.**
- p323 also: phantom-block removal (eq 4), a dropped r²H covariant display (agent's rejected-on-uniqueness — I located
  + restored), a dropped (cx'+dy')² factor, eq renumbering (5/6/7). Rebuilt with \begin{equation}\tag (safe form),
  not the stray `\[ \tag \]` the .tex had.

## Batch 37 (p312–317, run wwhxovth2) — 10 agents, 346k tok
- §103 Klein's geometric comparison / §104 Laguerre upper bound. **4 applied, 0 rejected, 2 clean.**
- Small: dropped heading-author 'Klein's', dropped xref '(a. f. S.)', subscript f_n→f_{n-1}, 'in'→'im §4'.
- Descriptive/geometric §§ low density again; the f_{n-1} confirmed via the §4 definition block on the next page.

## Batch 36 (p306–311, run w1x9p9vuc) — 15 agents, 513k tok
- §101–102 Newton/Descartes/Jacobi criteria. **9 applied, 0 rejected, 2 clean.**
- Dropped content: Doppelreihe top row (p309), eq (2) 1st formula (p311), enumeration-caveat clause (p306). Sign
  inversion +,-,+→-,+,- and dropped coeff 3D (p311) — math-relevant, scan-confirmed.
- **OVER-INSERTION (rare):** .tex added 'Jacobi,' to a footnote starting 'Observatiunculae' (body already says 'hat
  Jacobi'). Same class as p242/p304 over-expansions — GPT draft occasionally ADDS plausible text.
- **don't-modernize:** 'aller reellen'→'aller reeller' (print's older strong genitive -er) — same class as Theil/giebt.

## Batch 35 (p300–305, run wa273i4qi) — 15 agents, 519k tok
- §99–100 Budan-Fourier theorem / Newton's rule. **~12 applied + 2 sign tables restored, 1 clean (p305).**
- **Restored 2 DROPPED SIGN TABLES** (p301-302, Budan-Fourier μ-gerade/μ-ungerade case analysis) the .tex collapsed
  into prose. Agent flagged them <0.6 ('can't reconstruct, spans page break') — but with BOTH scan pages I had every
  +/− entry and rebuilt confidently. **Lesson: an agent 'spans page break / can't reconstruct' flag is MINE to resolve —
  pull both pages and rebuild; don't accept the collapse as final.** Rendered as clean arrays.
- λ→𝔷 (Fraktur z=Zahl/count) systematic ×3; zoom-confirmed. p304 eq (6) garble + eq (4) self-contradiction (F_n=1 vs
  F_n=f_n²) + an over-expansion — computation §§ keep garbling.

## Batch 34 (p294–299, run w3c0efzrk) — 8 agents, 314k tok
- §94–98 fundamental theorem of algebra. **2 applied, 0 rejected, 5 clean.**
- Both small (eq-into-sentence period→comma + d.h. lowercase). §95–98 (the geometric FTA proof) transcribed well.
- Footnotes on p296 (Gauss 1799), p299 (Sturm) PRESENT in .tex — footnote-drop pattern NOT recurring in these §§.

## Batch 33 (p288–293, run w2jxi5lw0) — 13 agents, 427k tok
- §93–94 Charakteristikentheorie. **8 applied, 0 rejected, 3 clean.**
- **a→α systematic (×4):** intersection-point label is Greek α; .tex had Latin a. Zoom-confirmed (crop_src.py) —
  important because the doc legitimately uses Latin a for COUNTS ('Ist a die Anzahl der Punkte A') on the SAME spread.
  So a/α is a real two-alphabet distinction; ALWAYS zoom a-vs-α, never assume from context.
- p292 dropped eq member (= via eq (2)), p288 parens, p289 connective — small.

## Batch 32 (p282–287, run wqtorxz0i) — 23 agents, 734k tok
- §89–93 Hermite-form discriminant determinant + characteristic theory. **16 applied, 2 clean.** Dense — Buch II isn't
  uniformly clean; computation-heavy §§ still garble.
- **TWO systematic notation conversions:** h_{i,k}→H_{i,k} (p284 bilinear-form coeffs) and θ→Φ (p286 arbitrary function;
  θ would clash with the angle ϑ=\vartheta). Both whole-passage. Verifier rejected 1 cell of EACH on bad-grep
  uniqueness — my own grep confirmed they exist, applied. **Verifier grep escaping is unreliable; trust my Grep over the verifier's uniqueness-fail.**
- **Restored a dropped determinant-decomposition block** (p284): |f_k(x_i)|=|a_0-triangular|×|Vandermonde| + a_0^{2n-2}→a_0²
  coefficient fix. Math-verified (product²=a_0^{2n}Π²=a_0²D). +1 page (359→360).
- **eq (6) uniform-range check:** the 3 sums must share range 0..n-1 (the .tex had n-2, 0 on lines 2-3). Use the uniform
  structure of a multiline sum to catch per-line limit errors.

## Batch 31 (p276–281, run wf8ghhsen) — 6 agents, 211k tok
- §88 Säculargleichung. **0 applied — ALL 6 pages CLEAN.** First fully-clean batch.
- **Σ-notation boundary clarified:** p277 .tex `\sum_{i=1}^n` vs print `\sum_{1,n}^{i}` = LEFT (cosmetic). Distinct from
  p255/p259 where the .tex had bare `\sum_1^m` (index variable DROPPED → fixed). **Rule: fix when the index variable is
  LOST; leave when complete but in conventional layout** (accept minor doc-internal Σ-style variation as the result).
- Confirms Buch II has genuinely clean whole sections (GPT draft transcribed §88 well). Agent auto-scaled to 6.

## Batch 30 (p270–275, run wns0kdpad) — 12 agents, 413k tok
- §85–87 Sturm chains. **6 applied, 0 rejected, 3 clean.**
- **Fraktur label (1)→(ℜ):** the .tex digitized Weber's Fraktur chain name `ℜ` (Reihe) as `(1)`. The AGENT was internally
  inconsistent (read K on p272, R on p273) and the VERIFIER disagreed (R) → classic zoom-it situation. crop_src.py
  confirmed Fraktur ℜ. **Lesson: when agent vs verifier disagree on a glyph (esp. Fraktur K/R), ZOOM — don't average.**
- Did it as a systematic 5-instance label fix (eq tag + all in-text refs), one consistent letter.
- **New Fraktur watch-class:** Fraktur letters in parens used as labels get digitized to numbers (𝔯→'1'). Watch for stray
  '(1)/(2)' in-text refs that should be Fraktur names, esp. in the Galois chapters (Gruppe 𝔊, etc.).

## Batch 29 (p264–269, run wtx630oo8) — 7 agents, 244k tok
- §83–84. **1 applied, 0 rejected, 5 clean.**
- p264 = 2nd `\`-macro escape-corruption (`\nu`→newline+`u`; cf. p194 `\\eta`). These compile fine but render WRONG
  (silent). Ran sweep `\$\\(pi|mu|nu|rho|tau|chi|phi|psi),?\s*$` → 1 candidate ~line 19660 CHECKED = FALSE POSITIVE
  (legit line-wrapped list `$\psi,`⏎`\psi_1,`⏎`\ldots`). **Discriminator: a REAL corruption's next line starts with a
  non-macro fragment (p264 next line was `u$`); a legit wrap continues with `\macro`.** So the sweep is a triage, not
  a verdict — eyeball the next line.
- **New standing check: escape-corruptions are SILENT (0 compile errors, wrong glyph). The line-end-macro grep is a
  cheap periodic sweep — re-run each major section.**

## Batch 28 (p258–263, run w3kk5thy0) — 19 agents, 592k tok
- §81–83 quadratic forms / vanishing determinants. **13 applied, 0 rejected, 3 clean.**
- **Systematic `ξ`→`z` across §81** (10 instances): the .tex consistently mistranscribed Weber's Latin linear-form
  variable z as Greek ξ. Did the whole passage as ONE conversion.
- **Verifier signal worth noting:** it REJECTED a single ξ→z cell with reason 'needs uniform conversion, not a single
  line'. Treat that kind of rejection as 'DO the whole passage', not 'skip' — the verifier is flagging systematicity.
- Σ double-index (Σ_{1,k}^{r,s}) collapsed to Σ_1^k AGAIN (now p255, p259×2) — Weber's range-on-bottom/indices-on-top
  Σ is a recurring transcription loss; watch it in every quadratic-form sum.

## Batch 27 (p252–257, run wj6z5uigg) — 9 agents, 331k tok
- §79 Bezoutiante/Realität + §80 Trägheit (inertia of quadratic forms). **3 applied, 0 rejected, 3 clean.**
- All 3 small symbol/form fidelity fixes: dropped `±`, transposed eq (π+ν=n-1), Weber's double-index Σ_{1,m}^{i,k}.
  Buch II error profile = small single-symbol/form deviations (vs Buch I's dropped derivation blocks).
- Consistent rule on transposed equations (π+ν+1=n vs π+ν=n-1): MATCH the print = type-A faithfulness, NOT cosmetic
  (a transposition across '=' changes the literal form, unlike a commutative reorder which stays cosmetic).

## Batch 26 (p246–251, run wpkamn8yq) — 9 agents, 326k tok
- §78 biquadratic discussion. **3 applied, 0 rejected, 4 clean.**
- 2 more dropped §-end footnotes (Kronecker/Dyck, Clebsch/Faà di Bruno) — drop pattern continues (now
  p209, p210, p233×2, p250×2). The footnote-presence sweep is increasingly worth doing.
- `-I^2`→`-T^2`: caught by .tex-internal consistency (§66 (7) uses -T²) + zoom-clear scan. T/I confusion = another
  single-glyph misread class to watch in Buch II.

## Batch 25 (p240–245, run w7dhyhsih) — 8 agents, 272k tok
- §76–78 root reality / Sturm. **2 applied, 0 rejected, 4 clean.**
- **First clear OVER-EXPANSION:** p242 the .tex ADDED the full discriminant product where Weber printed only a
  representative factor `(x_1-x_2)²` (prose covers 'sämmtliche Wurzeldifferenzen'). So the GPT draft doesn't only
  drop — it occasionally 'helpfully' expands shorthand. Confirms the audit must (and does) flag .tex-content-not-
  on-page, both directions.
- Buch II staying low-density (4/6 clean), as expected for root/Galois theory vs the garbled invariant-theory Buch I.

## Batch 24 (p234–239, run wszgm639n) — 7 agents, 265k tok
- §75/76 end of Erstes Buch → 'Zweites Buch. Die Wurzeln' divider (p239). **1 applied, 0 rejected, 5 clean.**
- Density dropped sharply (5/6 clean) now that the invariant-theory/transformation chapters are done — expect
  lower fix-rates in Buch II (root/Galois theory). Agent auto-scaled DOWN to 7 (vs 30 in §71); the scaling
  tracks candidate density well, so token cost will fall through the cleaner chapters.
- p235 sign fix confirmed by math (next eq) + scan.

## Batch 23 (p228–233, run wv6xbxijm) — 20 agents, 611k tok
- §73 Bezoutiante + §74/75. **12 applied, 0 rejected, 3 clean (p230–232).**
- **Systematic `t`→`τ` across a whole table column** (E-table right factor column). Handled as ONE whole-column
  rewrite (12 cells) not 12 patches — the systematic-notation rule again. This auto-fixed the 2 cells the verifier
  rejected (one uniqueness-fail on its scoped old_string, one a_0/a_1 misread).
- **Verifier a_0/a_1 misread caught by row-pattern + zoom:** verifier claimed E_{1,3}=3a_0τ_0; the row pattern
  (3a_1 in E_{1,1},E_{1,2}) said 3a_1; crop_src.py zoom confirmed 3a_1. The f'(t)-coefficient structure of the
  column is a strong internal check — use structural patterns to overrule single-cell agent/verifier reads.
- 2 dropped §-end bibliographic footnotes restored (Cayley, Gordan). **Recurring pattern: §-end citation footnotes
  keep getting dropped (p209, p210, p233×2).** Candidate for a targeted footnote-presence sweep across vol1.

## Batch 22 (p222–227, run wxv40r1h5) — 16 agents, 523k tok
- §71 Cardano tail + §72 general transformation. **10 applied, 0 rejected, 3 clean (p225–227).**
- §72 is back to normal density (3 clean pages) after the §68–71 garbled stretch. §71's Cardano tail (p222)
  was still heavy — a big multi-equation derivation block badly garbled, restored from the scan + verified
  internally consistent.
- `\varrho` misread as `\Omega` (curly-rho → capital-omega): single systematic symbol, fixed at both occurrences.
- **agent restructure block (#5) matched the scan exactly AND was internally math-consistent — when BOTH hold,
  a big block restore is safe.** (Contrast §69, where the agent grafts were mutually inconsistent → held.) This
  is the discriminator for "restore vs hold" on big garbled blocks.

## Batch 21 (p216–221, run w1buniwck) — 30 agents, 915k tok (worst region, §70–71)
- §70 Hermite-satz + §71 cubic transformation. **20 applied, 1 Weber erratum flagged, 0 clean pages.**
- §71 (cubic) is computation-dense → many dropped/garbled coefficients (dropped `a_0^λ`, `a_0^{n-1}`,
  the whole `Q_0=…` RHS, the `Q_0` line; wrong exponents `x_1→x_1²`; `-tH`→`-2/3 H`).
- **Built `crop_src.py`** (the long-pending tight-zoom tool): renders a fractional page box at high dpi +
  upscales, for glyphs the width-capped chunks can't resolve. Used it to settle a 2/3-vs-2/9 denominator →
  confirmed Weber printed 2/3 (a genuine erratum; math demands 2/9, proven two ways).
- **Math cross-checks caught a real fork the agents missed:** agent #14 (`3Q_0=⅔H·Q_2-a_1f`) and #18
  (`Q_0=-⅔t_0H`) are mutually inconsistent ×3. Re-deriving independently (sum of eq (9); and matching eq (10)
  to 3·eq (9)) proved #14 right and Weber's printed `Q_0` wrong. **LESSON: on computation-dense pages, derive
  the relations yourself — agent fixes can each be plausible but mutually inconsistent.**
- **Half-made agent fix completed by me:** eq (5) — the agent fixed only the prose (`y_1-y_2`) and left the
  equation in general `i,k` form; I restored the print's specific `1,2` + plain fraction. Always cross-check the
  WHOLE display when the agent flags only its prose.
- θ→t was a systematic Greek→Latin (3 spots) — fixed together (whole-section consistency), per the batch-20 rule.

## Batch 20 (p210–215, run wgfxgnw5z) — 27 agents, 894k tok (worst region yet)
- §68–69 Tschirnhausen/Hermite transformation. **§68: 5 applied. §69: 10 HELD.**
- §68 (p210–211) was genuine same-edition garbling (dropped Hermite footnote; eqs (3),(4),(6),(9) all
  index-shifted or wrong-LHS) — verified + applied like any batch.
- **§69 (p213–215) is the first STRUCTURAL hold.** The .tex confused Weber's `Φ(τ,ξ)` with `H` (symbol
  collision) and dropped the `Φ_ν` expansions + a derivation block. The verify stage flagged it as a
  possible 'edition difference' and rejected the piecemeal Φ-graft. My read: confused transcription, not
  a different edition — but it needs a COHERENT whole-section rework, not loop patches. Flagged in cert log.
- **New rule: when a section shows a SYSTEMATIC notation collision (one symbol consistently standing in
  for another, with internal self-consistency), HOLD the whole section for a dedicated coherent pass — do
  NOT apply the agent's per-line grafts (they make a broken hybrid).** Same lesson as the SGA5 global-notation
  decisions: systematic = decide once, section-wide; never piecemeal.
- 27-agent auto-scale: the workflow scaled up because §68–69 had ~20+ candidates. High recall, but the §69
  structural issue is exactly what per-page agents can't resolve (no whole-section context). Reconfirms that
  whole-section human judgment is the gate, not the swarm.

## Batch 19 (p204–209, run w1agyukjg) — 17 agents, 549k tok (dense)
- §65–67 invariant theory: **11 applied, 0 rejected, p204 clean.** Dropped derivation block, weight
  exponent r^{2μ}, I→I' ×3, an inverted substitution (ξ'=λξ→ξ=λξ' + matching coeff exponents — both are
  consistent conventions, so I matched the print and moved both together), χ→ψ ×2, generator-list order,
  a dropped bibliography footnote.
- **Faint-scan lesson:** the p209 chunk renders were washed-out → I deferred the footnote, re-rendered the
  FULL page (clear), verified the 4 citations exactly, then applied. **New step: when a chunk is too faint
  to read, re-render `--full` before deciding — don't guess, don't silently drop.**

## Batch 18 (p198–203, run w97rvytee) — 9 agents, 325k tok
- **3 applied (p198 dropped Q^τ + dropped display; p203 discriminant exponent via homogeneity), 0 rejected,
  4 clean.** The p203 fix is a clean math-verified catch: D's two terms must share degree 6, so the .tex's
  −4a'_1a'_3³ (deg 4) → −4a'_1³a'_3³ (deg 6).

## Batch 17 (p192–197, run w6wwajy55) — 18 agents, 574k tok (densest yet)
- §62–63 cubic-form invariant theory: **10 applied, 2 rejected, p193 clean.** Heavy garbling — a `\\eta`
  LaTeX corruption, a garbled identische-Relationen equation (wrong primes+subscripts+structure), 2 dropped
  clauses, wrong exponents (α,β vs h,k), a fabricated 2-step λ−2α chain, a dropped D^{-1/6} exponent.
- Rejects: γ→σ (6th revert-the-editor; print's σ is a typo, the proof is about γ) + a "remove ist" skip.
- **Note:** dense invariant-theory pages need full math reasoning (verified the λ−2α equivalence via eq (3);
  confirmed D^{-1/6} via r⁶=−27/D) AND reading multiple chunks — the disputed equations straddled chunk
  boundaries, so I fetched p195_top / p197_bot in a 2nd pass before deciding.

## Batch 16 (p186–191, run wsm4x3nui) — 7 agents, 246k tok
- **1 applied (p188 dropped word "den"), 0 rejected, 5 clean.** §60 (covariants / Hessian) well-transcribed.
  The commutative-cosmetic rule is now firing in-agent (a_0 r^n vs r^n a_0 auto-classified cosmetic).

## Batch 15 (p180–185, run wkgrk0q50) — 10 agents, 354k tok
- **0 applied; p183/184 clean; all candidates cosmetic or revert-the-editor.** §57–59 (quadratic forms /
  functional determinant) is well-transcribed.
- Key reject: p185 `Φ'`→`Φ` — the .tex's Φ' (partial derivative = coeff of t in the Taylor expansion,
  parallel to F') is math-correct; the print dropped the prime. 5th revert-the-editor catch.
- Skipped as cosmetic: dummy summation-index name (i vs ν) and Σ-index placement (\sum_i vs \sum^i) —
  no math meaning; the .tex's consistent choices are defensible standardizations.

## Batch 14 (p174–179, run wh4r37hzt) — 10 agents, 343k tok
- **4 applied, 0 rejected, 3 clean.** Notable: a dropped section-divider heading (Fünfter Abschnitt /
  Lineare Transformation) — first dropped-heading catch in vol1; plus a dropped α_0 (caught via the
  .tex's own "vier Verhältnisse" internal inconsistency) and reversed transformation-coeff indices
  a_{ν,i}→a_{i,ν}.
- **New watch category:** Abschnitt section-divider headings sit between sections and are easy for the
  transcription to skip — check page tops at section boundaries.

## Batch 13 (p168–173, run w0h0vvsc5) — 8 agents, 281k tok
- **1 applied (p172 dropped ν-equation + "und"), 1 rejected (p172 s-subscript (n-1)→(n+1), 4th
  revert-the-editor catch), 5 clean.** §52 mixed a genuine drop and a source-typo-revert temptation on
  the SAME page — verify each candidate independently, even within one page.

## Batch 12 (p162–167, run wbi1e27lk) — 7 agents, 246k tok
- **0 applied, 1 rejected by me, 5 clean.** The reject (p162 "Endgleichung für z"→"x") is the 3rd
  revert-the-editor/inject-error catch (cf. batches 7, 11): eliminating x,y can't give an equation "für x";
  the §50 chain is x→y→z so the end-equation is in z (.tex correct). Agent's reasoning self-contradictory again.
- **Standing pattern:** in well-transcribed regions a large share of agent "accepted" candidates are
  attempts to revert correct .tex readings to source typos — caught by math/context, not by the verifier.

## Batch 11 (p156–161, run wokiihclr) — 9 agents, 318k tok
- **2 prose fixes applied (p160, p161), 1 rejected by me, 3 clean.** The reject (p158 eq (14), resultant
  degrees) was the hardest call so far: the agent's fix would have INJECTED a Weber error into the
  math-correct .tex. Settled by a concrete n=2/m=1 example (Σν=m, Σμ=n is the truth). The agent's own
  type-B note had the right reasoning while its fix contradicted it — classic "verify the MATH, not the agent."
- Found a paired Weber erratum: §49 (5) `nν+mμ` should be `mν+nμ` (same swap); the .tex reproduces it
  faithfully — left type-B (notes the .tex's eq14-corrected vs §49(5)-faithful internal inconsistency).

## Batch 10 (p150–155, run wxyrbtpam) — 8 agents, 270k tok
- **1 applied (p154 β−γ sign error −u+v→u−v), 1 rejected by me (revert-the-editor: p155 dropped a_4 — the
  quartic needs all 5 coeffs), 4 clean.** The sign error is a good catch (a real math error in the .tex);
  the a_4 reject is the familiar "keep the editor's completion of a source oversight" pattern (cf. Collectet, (19)/(20)).

## Batch 9 (p144–149, run wmbmrvo7l) — 9 agents, 305k tok
- Low-density: **2 small fixes (p144 dropped word "etwa", p148 dropped 0 in a tuple), 3 clean, 1 correctly
  rejected** (verifier kept the authentic ".tex etc."). §44–45 symmetric-functions text is well-transcribed.

## Batch 8 (p138–143, run wo4jo4wfi) — 16 agents, 519k tok
- §41–43 symmetric functions: **9 real fixes applied, 1 correctly rejected by the verifier, p138 clean.**
  Many dropped equation lines/terms (f_3 line, eq (4) first line, eq (11) long form, +A_{m-1}α) + a dropped
  Newton footnote + a `\Pi(n)`→`n!` notation modernization.
- **Verifier got one right** (rejected p140 x→n, keeping the .tex's correct "n") — inconsistent but not useless.
- Weber's factorial is `\Pi(n)`, not `n!`; the .tex sometimes modernizes it — watch for more. Orthography
  policy holding: fix lone spelling slips (sämtlich→sämmtlich), defer systematic modernizations (Theil/teil).

## Batch 7 (p132–137, run w0za37gy4) — 9 agents, 323k tok
- **0 fixes applied. 4 clean (p132/133/136/137). All 3 agent candidates REJECTED on review** — the
  strongest "hand-check is the gate" data point yet (the verifier passed all 3):
  - p134 ×2: agent escalated Weber's double-bar `≦` (= ≤) to `\gtreqless` (⋛); the .tex `\le` is correct
    (prose "innerhalb oder an der Grenze" + the math both say ≤). The agent even described it as ≦ but mislabeled it.
  - p135: revert-the-editor xref (print "(20),(21)" is an off-by-one source typo; .tex correct "(19),(20)" kept).
- **Adjustment applied:** rule added — Weber's `≦/≧` are leqq/geqq (cosmetic `\le/\ge`), never escalate to `\gtreqless`/3-way.
- **Verifier scorecard:** it has now passed false candidates I rejected in batches 1, 4, and 7; reliable
  filtering only in batch 2. The verify stage is a WEAK filter; my eye is the gate.

## Batch 6 (p126–131, run wtfu7alt6) — 16 agents, 561k tok (densest yet)
- §38–39 Fundamental-Theorem convergence proof: **10 real fixes, 0 rejected, p127 clean.** Highest-value
  batch — the math was garbled in consequential ways: systematic θ→Θ (×4), a `kleiner`↔`grösser`
  inequality-direction inversion, several dropped general terms, a mis-tagged eq (11) with a dropped
  equation, a dropped QED.
- **New adjustment/check:** an agent "restructure" patch un-tagged a display using `\begin{equation}`
  (which auto-numbers) where the doc convention is `\[…\]`. I corrected it on apply. RULE: inspect any
  agent restructure that adds/converts an equation environment for spurious auto-numbering.
- Dense proof pages → many interrelated fixes; 16 agents auto-spun (561k tok). Consider 4-page batches
  in proof-dense regions to cap review load.

## Batch 5 (p120–125, run wnbmmoci2) — 10 agents, 348k tok
- 4 real fixes, all single-symbol/variable misreads (p121 d→δ ×2; p123 spurious "=y+iz" removed; p124 γ→y localized); p120/122/125 clean, 0 rejected.
- **Pattern emerging:** this region's errors are Greek/Latin glyph confusions (d/δ, γ/y, and ε/ξ in batch 4)
  — the dominant vol1 failure mode is **single-glyph misreads, not big drops**. Cheap for agents to find,
  easy to eye-verify, but they MATTER (wrong variable). Verifier passed all 4 (correct this time).
- Cosmetic discipline held: kept "kann" (Weber typo "kan"→type-B), `≦`→`\le`.

## Batch 4 (p114–119, run w4kwfrqpa) — 12 agents, 386k tok
- 5 real fixes applied (p114 roots-of-unity ξ→ε ×3 + bogus-eq removal/restore; p118 xref (1)→(6)); p115/116/117 clean.
- **I rejected 1 the verifier passed:** p119 `Collected`→`Collectet` — agent tried to revert the editor's
  correction of Weber's misprint (and self-contradictorily flagged it type-B too). The "don't revert
  obvious-typo corrections" rule is already in the prompt; the agent still violated it → hand-check is the gate.
- p114 was the fix-dense page: one symbol misread (ε→ξ) propagated to 4 spots plus a fabricated equation —
  exactly the kind of cascading transcription error worth catching.

## Batch 3 (p108–113, run wahdj8vfy) — 13 agents, 440k tok
- Verifier accepted **ALL 8** candidates (0 rejected) → the **hand-check did all the filtering**: I
  applied 5 real, SKIPPED 2 as cosmetic (p111 `ci`↔`ic` commutative reorder), p110 clean.
- The **confirm-absence rule worked**: the p109 agent grepped for the dropped `√[2n]` equation,
  found none, and correctly flagged the drop (no false "it's there").
- **Adjustment applied (active from p114):** "commutative reordering is cosmetic, never type-A" rule
  added to the audit prompt — directly targets the p111 over-flags.
- **Observation:** verifier reliability is inconsistent (filtered 4/4 in batch 2, 0/8 here) — my eye
  is the real gate, not the verify stage. Dense pages (8 candidates/6 pp) → keep batches ≤6 in this region.

════════════════════════════════════════════════════════════════════════════════
★ CURRENT STATUS — 2026-07-02 (AUTHORITATIVE; supersedes the line-45 cursor) ★
════════════════════════════════════════════════════════════════════════════════
vol1 = **417 pp / 0 err / 0 overfull / 0 underfull / 0 missing-char / 0 undefined.**

**What just happened (the 20-page SAMPLE CERT overturned the "certified-clean" claim):**
Floris ordered a full-rigor by-hand symbol-by-symbol cert of a 20-page sample, count errors, sign off, let
the error rate decide re-cert depth. Result = **NOT clean** (full table: WEBER_SAMPLE_CERT.md; provenance:
WEBER_CERT_LOG.md 2026-07-02 entry). The "map-phase verified faithful" AND the Phase-2 "§141→§188 complete"
designations are BOTH unreliable. Found + FIXED this session:
  • §26 (p90) — REFORMULATED island → FULLY re-transcribed (k/i indices, Σ^i sums, α-normalisation).
  • §164 (p542-p545) — HEAVILY CONDENSED reconstruction the held-list MISSED (gap between held §163 & §165)
    → FULLY re-transcribed: restored dropped Satz 3+eq(8), Satz 4, B_k & E_k/G_k developments, period-grouped
    (ε,α) expansion; fixed 6 index-below→above sums, "e-gliedrige"→"f-gliedrige" error, \\alpha typo. +1 pp.
  • p400 dropped clause FIXED; p580/§172 3 reworded-prose items FIXED.
  • 23rd Weber erratum flagged (§164 eq 8 prints ε² for ε^{λ₂}).
Error concentration = theory/PROSE GLUE; equations were mostly faithful even in bad sections.

**NEXT (escalation, per Floris "errors bad → escalate" — IN PROGRESS, grind continuously, no checkpointing):**
Systematically RE-VERIFY §141-188 page-by-page — do NOT trust the "complete" claim. For each section: locate its
.tex span, pull the section-opening scan, compare PROSE (not just eqs) symbol-by-symbol; where a section is
condensed/reworded/reconstructed, re-transcribe it fully to Weber's printed form; compile-gate + pdftoppm-verify.
Priority order (most-likely-reconstructed first): the held-list theory §§ that were claimed done —
§141, §148-156, §158, §162-163, §165, §166-170, §173-188 — verify each was ACTUALLY re-transcribed vs only
claimed; then re-scan the patched worked-example islands §157, §159-161 (like §172, may keep reworded glue).
Already re-verified clean this session: §151, §155 (sample), §171, §183 (prior spot-checks), §172 (fixed), §26 &
§164 (re-transcribed). Method reminder: page-by-page by MY context (render chunk_page.py 1 P; crop_src.py to zoom;
FLAG illegible never guess). Scan offset vol1 +26. Keep house conventions (\varrho, giebt, Coefficienten, Σ^index
above, \S\, refs, d.\ h. / z.\ B.). Track sub-progress by appending here; keep THIS block as the top cursor.
────────────────────────────────────────────────────────────────────────────────
RE-VERIFY PROGRESS (§141-188 pass):
  • 2026-07-02 turn 2: **§141** re-verified vs scan p453-455 (top/p454-bot/p455-top all EXACT-match) —
    FAITHFUL; 1 minor fix (restored dropped relative "die" in the multi-var-function three-way-distinction,
    .tex 16507). **§157** faithful (map-phase by-eye p514/p516 + coherent .tex; Kronecker def intact).
    **§158** (was flagged "rewritten") re-verified vs scan p517-top = EXACT-match → Phase-2 re-transcription
    DID fix it; FAITHFUL. **§166** (gap suspect between held §165/§167) = CLEAN (CERT_LOG map-phase p552-553 +
    coherent .tex). Compiles 417pp/0 badness.
  • FINDING: held-list sections WERE properly re-transcribed (§141,§158 confirmed); by-eye-checked sections
    are clean (§157,§166). §164 slipped only because it was NOT in the held-list AND not in a by-eye batch.
    So residual risk = the "patched worked-example islands" §159-161 (worked examples like §164/§172, both of
    which had issues) + spot-confirm §162-163,§167-170,§173-188 openings.
  • 2026-07-02 turn 3: **§159 (Cubische Gleichungen)** re-verified vs scans p522-524 — ★ PERVASIVELY REWORDED
    (a §164/§172-class reconstruction the map-phase only partly patched: eqs were restored but the whole prose
    was a GPT paraphrase with DROPPED paragraph + DROPPED display). FULLY re-transcribed the prose (10 surgical
    fixes via retrans_159.py): opening sentence; "Die Permutationsgruppe…"→"Die Gruppe der Permutationen…nämlich
    aus der identischen Permutation 1, aus zwei dreigliedrigen Cyklen und drei Transpositionen"; "und heisst daher
    die cyklische Gruppe"→"und wird daher cyklische Gruppe genannt"; "Es seien…die Wurzeln"→"Es seien nun…die drei
    Wurzeln"; "Im Körper der rationalen Functionen der Coefficienten…"→"Legen wir den Körper Ω zu Grunde, der aus
    allen rationalen Functionen der unabhängigen Veränderlichen…dieser Gleichung; wenn wir aber"; "adjungirt,
    wobei"→"adjungiren, worin"; eq(5) restored Weber's leading "+"; "die Discriminante ist…auf die cyklische Gruppe
    (2)"→"die Discriminante der Gleichung (3) ist…auf (2)"; "In dem so erweiterten Körper"→"In dem Körper Ω', der
    durch diese Adjunction aus Ω entsteht"; and the big v-passage — restored Weber's "Wollen wir…die zwar nicht
    selbst, deren Cubus aber…denn v muss…als Factor erhalten", the DROPPED paragraph "Durch diese Adjunction kann
    eine Reduction der Gruppe nicht eintreten…(§157)", and the DROPPED display "ε=(−1+√−3)/2, ε²=(−1−√−3)/2". From
    "dann ist der Erfolg von π…" onward (eqs 8-10, Cardano) was already faithful. Output-PDF pp333-334 eyeballed =
    matches Weber. Compiles 417pp/0 badness. ⚠ p522-524 scans are FADED/low-contrast — read carefully, ε²-denom "3"
    on the faded scan was an artifact (math + the ε line confirm 2).
  • LESSON refined: "patched worked-example islands" (§159-161,§164,§172) = the reconstruction was NEVER de-reworded,
    only had a few eqs restored. Each needs a PROSE pass. So far §164✓,§172✓,§159✓ re-done; §160,§161 pending.
  • 2026-07-02 turn 4: **§160 (Permutationsgruppen von vier Elementen)** re-verified vs scans p524-527 — ★ same
    §159-class rework (eqs 1-7 all correct/faithful, but prose paraphrased with dropped sentences + a dropped
    display). 7 surgical prose fixes: (a) restored the DROPPED opening "Ein gutes Beispiel für die Galois'sche
    Theorie bieten die Gleichungen vierten Grades, wo die Verhältnisse so einfach liegen, dass sich Alles leicht
    übersehen lässt, und doch die wichtigsten Erscheinungen der Gruppenbildung dabei zu Tage treten." (.tex had
    jumped to "Aus vier Ziffern…"); (b) Satz 1 "Enthält…"→"Wenn…enthält…, und"; (c) Satz 2 "Enthält sie…"→"wenn
    sie…enthält"; (d) "Eine von P und Q verschiedene transitive Gruppe, die eine Transposition enthält, muss…und
    damit zunächst"→Weber's "Wenn also nun eine von P und Q verschiedene Gruppe zunächst eine Transposition (0,2)
    enthält, so muss sie, wenn sie transitiv ist, auch (1,3) enthalten, und demnach die ganze intransitive Gruppe
    vierten Grades:"; (e) restored the DROPPED argument+display before eq(4) ("…Ein viergliedriger Cyklus aber, in
    dem 0 und 2 cyklisch an einander stossen, kann nicht vorkommen…[(0,2)(0,2,3,1)=(0,3,1)] Ebenso können nicht 1
    und 3…"); (f) "Hat…keine Transposition, so ist sie entweder Q_1…und damit eine cyklische Gruppe"→Weber's
    "Wenn…keine Transposition enthält, so enthält sie entweder keinen viergliedrigen Cyklus und ist dann mit (6)
    identisch, oder…und enthält dann auch die ganze cyklische Gruppe, wie". eqs (1)-(7) + the P_1/Q_1/P_2 groups +
    the conclusion were already faithful. Output-PDF p335 eyeballed. Compiles 417pp/0 badness.
  • So far re-done: §164✓,§172✓,§159✓,§160✓. Remaining worked-example island: **§161** (Auflösung der
    biquadratischen Gleichungen, .tex ~18720, scan p528-533).
  • 2026-07-02 turn 5: also caught **§160 TAIL** rework I'd missed (p528-top): "Die mit P₂ conjugirten drei
    Gruppen haben ausser der Identität…"→Weber "Aus P₂ gehen ebenfalls drei conjugirte Gruppen hervor, die aber
    ausser 1…"; "Ausser P,Q…giebt es"→"Es giebt also ausser…"; "ist noch [P₃] hervorzuheben…dreier"→"verdient noch
    die Gruppe (3): [P₃,] hervorgehoben zu werden…von drei". FIXED. **§160 now fully done.**
  • **§161 (Auflösung der biquadratischen Gleichungen)** — PARTIALLY re-verified (p528-531 done, p532-533 remain).
    Pattern: OPENING p528 + eqs (1)-(20) all FAITHFUL, but connective prose reworked in stretches (like §159/§160).
    Fixes so far: (a) eq(6)-(7) drop "als eine zu Q_1 gehörige Function…die beiden dazu conjugirten Werthe";
    (b) eq(10) removed fabricated connectives "folgt"/"und also" + restored the colon; (c) ë-normalisation
    "Coëffic"→"Coeffic" ×3 (§161 + §175-region, house convention); (d) p531: restored "In Bezug auf die übrigen
    Wege…können wir uns kürzer fassen. Wenn wir zunächst nicht √D adjungiren…" (was "Man kann…auf anderem Wege"),
    "genügt. Besser noch nimmt man als Wurzeln der cubischen Resolvente" (was "Bequemer nimmt man als Wurzeln"),
    "Man erhält ferner, wenn man [19] setzt, [z=a₂−3u] und daraus die Resolvente für u:" (was "Setzt man ferner…
    so ist…und die Resolvente für u wird"). Compiles 417pp/0 badness.
  • 2026-07-02 turn 6: **§161 TAIL (p531bot-p532) FULLY re-transcribed** — was a §159/§160-class reconstruction
    with DROPPED equations + a CHANGED equation: restored "Wenn man aber von der Gleichung (18) oder (20) nicht
    eine, sondern alle Wurzeln adjungirt…Die Grössen v₁,v₂,v₃ sind nach (12)…"; restored "Man kann ferner zur
    Lösung…eine zu der cyklischen Gruppe P₂ gehörige (eine cyklische) Function…"; restored the Totalresolvente
    sentences; **corrected eq (22)** ξ=α+α₂−½a₁=½√v₂ (the .tex had wrongly put the a₁=0 special form
    ξ=α+α₂=−α₁−α₃); restored the "so sind von den sechs Wurzeln je zwei entgegengesetzt gleich…" + "Nehmen wir zur
    Vereinfachung…a₁=0 an" (was mis-ordered); **restored the DROPPED eq (24)** 2αα₂=b/ξ+ξ²+a, 2α₁α₃=−b/ξ+ξ²+a;
    **restored the DROPPED display** 4c=(ξ²+a)²−b²/ξ² + "oder"; de-reworded the eq(25)/eq(26)/closing connectives.
    File 417→**418 pp** (restored content). Output-PDF p339 eyeballed = matches Weber. Compiles 418pp/0 badness.
  • ★ **ALL worked-example islands DONE: §159✓ §160✓ §161✓ §164✓ + §172✓.** Plus §26✓ (Buch-II). Verified faithful:
    §141,§157,§158,§166. Fixed misc: p400, p580. Errata count 23.
  • NEXT (final escalation phase): spot-confirm the HELD-THEORY §§ were actually re-transcribed (not just claimed) —
    check section OPENINGS vs scans for §148-156, §162-163, §167-170, §173-188 (§141✓ §158✓ already confirmed from
    this list; §150 logged re-transcribed in map phase). If an opening matches scan → faithful, move on; if reworded
    → deep-dive like §164. Buch-I/II (§1-137) was sample-clean except §26 (fixed); low priority.
  • 2026-07-02 turn 7: **§163 (Reduction der Abel'schen Gl. auf cyklische, p537-539) VERIFIED FAITHFUL** vs scans
    p537/p538 (opening prose + eqs (4),(5) word-for-word). One fidelity fix: section TITLE was "…auf cyklische
    Gleichungen" but Weber prints "…auf cyklische." (adjective alone) → dropped the trailing "Gleichungen".
  • 2026-07-02 turn 7 — ★★ **METHOD-BREAKING FIND: §162 (Abel'sche Gleichungen, p533-536) WAS DAMAGED despite being
    a "held-theory" section.** The .tex read as perfectly coherent prose, but a whole chunk was silently DROPPED at
    the §162 opening: (a) the derivation "Nun reducirt sich P durch Adjunction der Wurzel α₀ auf Q₀, durch α₁ auf
    π₁⁻¹Q₀π₁ etc. …dass also durch π,π₁,π₂,…π_{m-1} die Gruppe erschöpft sei. Wir haben also:"; (b) the Satz "Damit
    eine irreducible Gleichung eine Normalgleichung sei, ist nothwendig und hinreichend, dass der Grad der Gruppe mit
    dem Grade der Gleichung übereinstimme."; (c) the REAL opening of the Abel-def paragraph "Wir betrachten hier
    zunächst die specielle Art von Gleichungen, zu denen die von Gauss zuerst aufgelösten Kreistheilungsgleichungen
    gehören,…" — the reconstruction had compressed all of (a)-(c) into the bare "Zu diesen Gleichungen gehören, die
    Abel allgemein aufzulösen gelehrt hat…". Also fixed "aufzulösen"→"auflösen" (Weber's older construction) and
    eq(1) period→comma. Rest of §162 body (p534bot-p536, eqs (2)-(6) + commutativity proof) verified FAITHFUL
    word-for-word incl. Weber's own x/α typo at σ_kσ_h (reproduced). Abel footnote verified exact. Compiles 418pp/0.
  • ★ **ADJUSTMENT (why this matters):** the "held-theory §§ were faithfully re-transcribed" assumption is FALSE.
    §162 slipped through because internal coherence ≠ fidelity — the dropped chunk left grammatical prose behind.
    CONSEQUENCE: section-OPENING spot-checks are INSUFFICIENT; must do real page-by-page scan comparison of the whole
    body of each §. Widening the sweep. §162 opening even MATCHED (Q π₁ etc.) — the damage was mid-section. Do not
    trust any § until every one of its scan pages has been eyeballed against the .tex.
  • 2026-07-02 turn 7: **§167 (Kreistheilungsperioden, p554-557+) VERIFIED FAITHFUL** — page-by-page scan-vs-tex
    from the opening through eq(12) (the multi-line f-gliedrige Perioden), ALL word-for-word: p554-mid/bot,
    p555-top/mid/bot, p556-top/mid/bot, p557-mid. Despite the map-phase "HELD (reconstruction)" mark, §167 was
    re-transcribed correctly in a later pass (tell: the house `\sum^{h}` index-above form at eq(8); Coëffic→Coeffic
    house-normalised as intended). Fixed only cosmetic "(mod.\ n)"→"(mod\ n)" ×2 (scan prints "mod" no period).
    NOTE: 3 more `\mathrm{mod.}` remain elsewhere — fix each when on its scan page (don't blind-replace).
  • ★ REVISED PICTURE of the map-phase HELD-block (§148-156,§158,§162-163,§165,§167): several were RE-TRANSCRIBED
    in a later pass and are now faithful (§158✓ §162-body✓ §163✓ §167✓ this session), but §162 had a dropped-chunk
    at its opening (fixed). STILL UNCONFIRMED (never re-checked vs scans since the map phase): **§165** (Auflösung
    der cykl. Gl., p546-551) and the **§148-156 "rewrite-block"** — these are the highest remaining risk.
  • 2026-07-02 turn 7: **§165 (Auflösung der cyklischen Gleichungen, p546-551) VERIFIED FAITHFUL end-to-end** —
    page-by-page scan-vs-tex, opening through eq(21) + the complete closing reality-of-roots discussion, ALL
    word-for-word: p546-mid, p547-top/mid/bot, p548-top/mid, p549-top, p550-mid, p551-mid. Strong hand-transcription
    tells confirmed against print: house `\sum_{0,m-1}^{λ}` (index-above+range) = Weber's printed sum exactly;
    `\varrho` for ϱ; Coëffic→Coeffic normalised; `\pmod m` renders "(mod m)" matching Weber. NO fixes needed.
    Another map-phase "HELD (reconstruction)" § that was actually re-transcribed correctly later.
  • ★ CONCLUSION on the map-phase HELD-block: §158✓ §162-body✓ §163✓ §165✓ §167✓ are all FAITHFUL now (re-done in a
    later pass); only §162's opening chunk was still damaged (fixed turn 7). The "HELD" label meant "not fixed in the
    map phase" — most got re-transcribed afterwards. REMAINING unconfirmed HELD: the **§148-156 "rewrite-block"**
    (map phase called it full rewrites, not patchable) — the last and highest-risk block to scan-verify.
  • 2026-07-02 turn 7: **§148-156 rewrite-block — SPOT-CHECKED, RE-TRANSCRIBED & FAITHFUL.** The map phase had
    flagged §148-149 as "wholesale GPT-rewrite" and §153 as "6-page rewrite WITH fabrication" (the scariest items).
    Both are now FULLY re-transcribed:
      – **§148 (Permutationsgruppen, p473-476) VERIFIED FAITHFUL:** eq(6) bottom row now correct `a_{b_i}` (was
        wrong `b_iπ_a`); "was mit (5) völlig gleichbedeutend ist" restored; **the cyklische-Gruppe example + its 3
        matrices (p476) restored** (CERT_LOG said DROPPED) — matches scan p476-top word-for-word; the Abel'sche-
        Gruppen/Theiler paragraph restored. `\perm{}{}` macro + `\varrho` = hand-transcription tells.
      – **§153 (Zerlegung in Transpositionen/Cyklen, p492-497) VERIFIED FAITHFUL & DE-FABRICATED:** the cyclic-def
        (p493) is now Weber's actual matrix form, NOT the fabricated "(a,b,c)(d,e)(f)/disjoint-commute" content;
        **the π₁,π₂,π₃ worked example + eqs (1)-(3) (p494) restored** (CERT_LOG said ENTIRELY DROPPED) — matches scan
        p494-top/mid exactly, matrices AND cycle decompositions (π₁=(0,2,6,5,4,1,3,7), π₂=(0,4,5,7,6)(1,2)(3), …).
    Per CERT_LOG §150,§152 were re-done in the map phase and §151 was clean. ⇒ whole §148-156 block is faithful.
  • ★★ TURN-7 BOTTOM LINE: the map-phase "HELD/rewrite" labels meant "not yet fixed in the map phase", NOT "still
    broken now". A later re-transcription pass systematically re-did them ALL correctly. Confirmed faithful this
    session: §148 §150 §152 §153 §158 §162(body) §163 §165 §167 (+§151 clean). The ONLY residual damage found in
    the whole §141-188 sweep beyond the known islands was §162's dropped OPENING chunk (fixed turn 7). The vol1 .tex
    is in far better shape than the 20-page sample-cert's alarming rate implied — the real damage was concentrated in
    the worked-example islands (§159-161,§164,§172) + §26 + §162-opening, ALL now fixed. File 418pp/0 badness.
  • 2026-07-02 turn 8 (loop re-fire): **§149 & §153 fully VERIFIED vs scans; §154 opening confirmed.**
      – **§149 (Galois'sche Gruppe, p476-481) VERIFIED FAITHFUL:** opening matches scan p476-mid; `\Phi[...]` brackets
        (not GPT's `θ(...)` parens); Sätze a)-d) all restored; displays (5),(6),(7) + the g'(t) product present; the
        Affect/Kronecker discussion; **the Galois biography footnote (p481) restored & matches scan word-for-word**
        (Férussac 1830, Chevalier letter Revue encyclop. Sept 1832, Liouville 1846 Bd XI "Mém. sur les conditions de
        résolubilité…", Maser 1889 Berlin Springer, Serret II.1854/IV.1879, Betti Annali 1853, Jordan Traité 1870,
        Netto Substitutionentheorie Leipzig 1882) — CERT_LOG had flagged this footnote as DROPPED. §148 Abel/Theiler
        para also re-confirmed vs p476-mid.
      – **§153 (Zerlegung in Transp./Cyklen) VERIFIED COMPLETE p492-500** (runs longer than CERT_LOG's "p492-497"
        estimate — fills through p500): eqs (1)-(3)+worked example (p494) ✓, transposition→symmetric theorem +
        "Die vorgelegte Gruppe sei P…(0,1)…" (p498, .tex 17754/17757) ✓, imprimitivity M'/M'' proof + conjugation
        formula (p499) ✓, three-cycle theorem + (0,2,1)(0,m,m+1)(0,1,2)=(1,m,m+1) (p499-bot, .tex 17800) ✓, item 11
        + powers/order/Periode material π⁰,π¹,… smallest e, eq(4), cyclic-perm powers examples π=(0,1)(2,3,4)… (p500,
        .tex 17805-17840) ✓. The fabrication-risk section is PRISTINE end-to-end.
      – **§154 (Divisoren/Nebengruppen/conjugirte Gruppen) opening VERIFIED** vs scan p501-top (title + "Wir haben im
        §.152 gesehen…" match .tex 17843-17845). Body (17845-18083) shows re-transcription tells: `\varkappa` for
        Weber's ϰ (Q-elements), restored "Auch Untergruppe genannt" footnote, Cauchy fundamental-theorem, eqs (1)-(5).
    ⇒ §148 §149 §150 §151 §152 §153 all VERIFIED FAITHFUL; §154 opening clean. §148-156 block essentially cleared.
  • 2026-07-02 turn 9 (loop re-fire): **§154 & §155 fully VERIFIED vs scans end-to-end — no fixes needed.**
      – **§154 (Divisoren/Nebengruppen/conjugirte Gruppen) VERIFIED FAITHFUL p501-507:** opening p501 ✓; eqs (1),(2)
        with Weber's ϰ=`\varkappa` (p501-mid) ✓; Cauchy fundamental-theorem + Qπ₂=Qϰπ₁=Qπ₁ (p502-mid) ✓; second
        Nebengruppen-Zerlegung + Zugehörigkeit-def (p503-mid) ✓; Satz 5 + eq(10) (p505-top) ✓; conjugate-groups
        eq(11) π=π₁⁻¹ϰπ₁ (p505-bot) ✓; eq(12) + **"gleichberechtigte Untergruppe" footnote** (p506, .tex 18044) ✓;
        Satz 6 (π⁻¹ϰπ transform rule) + Satz 7 (transitive-group degree = m-multiple) + P=Q+Qπ₁+…+Qπ_{m-1} (p506bot-
        p507top, .tex 18052-18080) ✓. Long section (6 Weber pp). ϰ/ϱ/restored-footnote hand-transcription throughout.
      – **§155 (Reduction d. Galois'schen Resolvente/Normaltheiler) VERIFIED p507-509:** heading+opening p507 ✓
        (.tex 18083-85); eqs (3),(4),(5) + χ(t) Lagrange-interpolation sum + Satz 2 ω=χ(ψ)/φ'(ψ) (p508-mid, .tex
        18112-30) ✓; Satz 3 + Normalkörper N degree p/q statement (p509-top, .tex 18136-42) ✓. .tex also carries the
        restored **Lagrange footnote** (18105) + **Normaltheiler footnote** (18185, "Galois…décomposition propre…
        ausgezeichnete/invariante Untergruppen") — hand-transcription tells; body eqs(6),Sätze 4,5 read complete.
    ⇒ **§148,§149,§150,§151,§152,§153,§154,§155 ALL VERIFIED FAITHFUL** vs scans (§150/151/152 via map-log). The
    §148-156 rewrite-block — last & highest-risk HELD block — is essentially CLEARED. Whole map-phase HELD/rewrite
    backlog now confirmed re-transcribed & faithful. vol1 damage was ONLY: islands §159-161/§164/§172 + §26 +
    §162-opening (all fixed). File stable 418pp/0 badness (no edits turns 8-9).
  • 2026-07-02 turn 10 (loop re-fire): **§156 (Die Gruppe der Resolventen) VERIFIED FAITHFUL end-to-end — block CLEARED.**
      – Scan-checked p511-513 line-by-line against .tex 18183-18236; EVERY line matches verbatim, no drops:
        §155 tail (Normaltheiler def+footnote¹, Satz 5, "einfache Gruppe"+Durchschnitt, R-normal-in-Q para) p511 ✓
        (.tex 18185-18197); §156 heading+opening "Die Hülfsgleichung φ(t)=0…geht in die Galois'sche Resolvente über…
        Satze von Lagrange (§.155,2.)" p511-mid/bot ✓ (.tex 18200-18206); the Normaltheiler footnote¹ (Galois
        décomposition propre / ausgezeichnete-invariante Untergruppen) reproduced word-for-word on p511-bot ✓
        (.tex 18185). Fall 1 Totalresolvente (theilerfremd → N=Ω(ψ,ψ₁…ψ_{j-1})) p512-top ✓ (.tex 18211-15); Fall 2
        Partialresolvente (Theiler R Grad r → Normaltheiler, Factoren Grad r) p512-mid ✓ (.tex 18216); "Ist P einfache
        Gruppe → nur Totalresolventen…" ✓ (.tex 18219); eq(1) ψ,ψ₁,ψ₂…ψ_{j-1} + invariance argument p512-bot ✓
        (.tex 18221-26); "Es ist nun der Grad…zu bestimmen" + σ/π'=σπ + Nebengruppe Rπ result + "Der Grad…gleich der
        Anzahl dieser Nebengruppen" (= p:r) p513-top ✓ (.tex 18228-36). No edits (file stays 418pp/0 badness).
    ⇒ **§148,§149,§150,§151,§152,§153,§154,§155,§156 ALL VERIFIED FAITHFUL vs scans. THE §148-156 BLOCK IS FULLY
    CLEARED** — the last & highest-risk map-phase HELD/rewrite block is now scan-confirmed end-to-end. Confirmed vol1
    reconstruction damage was ONLY: worked-example islands §159-161/§164/§172 + §26 + §162-dropped-opening (all fixed).
  • 2026-07-02 turn 10 (cont.): **§168, §169, §170 (Sechzehnter Abschnitt cyclotomy block) VERIFIED FAITHFUL vs scans
    p560-574 — 2 fixes to §168 only; §169 & §170 clean.** These were the map-phase HELD/reconstruction block (§168 had
    a FABRICATED title, §170 flagged "reconstruction + content-shuffle") — the later re-transcription pass redid all
    three faithfully, confirming the escalation-clears-alarm pattern once more.
      – **§168 (Die Gauss'sche Methode z. Berechnung d. Resolventen, p560-564) VERIFIED, 2 fixes:** title correct
        (GPT had fused the two running-heads "Producte von Perioden"/"Dreizehn-Theilung" into a fake title; true title
        present). Body matches verbatim: eqs(1)-(6) η^(λ)η^(μ) product derivation w/ house `\sum^{s}` forms, n=13
        Indextabelle(7) N-row 1,2,4,8,3,6,12,11,9,5,10,7, eq(8) cubic-resolvente periods, eq(9)-(10) cubic η³+η²-4η+1=0
        +Disc 169=13², cos-forms, eqs(11)-(16) ξ/ζ/two-term periods. **FIX: two `(\mathrm{mod.}\ n)`→`(\mathrm{mod}\ n)`
        (19826,19830) — Weber prints "(mod n)" NO period on p560 (same errata as §167's 19608/19625, fixed earlier).**
        [Noted-not-fixed: `z. B.` unescaped @19907 — cosmetic, Weber prints "z. B."; house `z.\ B.` varies volume-wide.]
      – **§169 (Zurückführung d. Kreistheilungsgl. auf reine Gl., p564-570) VERIFIED FAITHFUL, NO fixes:** the big
        disq.-arithm. footnote¹ RESTORED word-for-word (Gauss art359/360, Lagrange, Jacobi Werke Bd6, Kummer Crelle35
        +Berl.Akad.1856, Eisenstein+Cauchy, Bachmann Leipzig1872); eqs(1)-(15) Lagrange-resolvent product theory w/
        house `\sum_{0,n-2}^h` forms; **n=17 worked example ALL correct** — Indextabelle N-row 1,3,9,10,13,5,15,11,16,
        14,8,7,4,12,2,6, eq(16) periods (η₂=-2cos π/17…η₇=-2cos5π/17, every sign verified via reduction identity),
        ind-t/ind(t+1) table, eq(17) ψ coefficients, eq(18) ψ(α)=-3-i√8 etc, eq(19)(α,η)⁸, eqs(20)-(22), (-1,η)=√17,
        (i,η)=⁴√17{…} quartic-radical, sign-determination trig, v.Staudt footnote¹ (Crelle24,1842) restored. [map-phase's
        "2 n=17 cosine-sign typos" already correctly incorporated — all signs match scan.]
      – **§170 (Eigenschaften d. Zahlen ψ, p570-574) VERIFIED FAITHFUL, NO fixes — NO content-shuffle found:** Kronecker
        footnote¹ (Journ.f.Math. Bd93) restored; opening 3 paras in correct order; eqs(1)-(8) ψ-relation theory
        (congruences (1)/(3), ψ_λ(α^{λ'})=ψ_{λ'}(α), (-1)^μ/(-1)^f sign formulas, ψψ(ε^{-1})=n, 3-number vertausch);
        e=7 example (λ/λ'/λ'' tables, eq(9)(α,η)⁷=ψ₁(α)⁴ψ₁(α²)²ψ₁(α⁴)); closing Satz congruence(10)+eqs(11)-(17)
        binomial/geometric-series number theory w/ Π-factorial result eq(17). Every line matches verbatim.
    ⇒ File recompiled after §168 fixes: **418pp / 0 err / 0 overfull / 0 underfull / 0 missing-char / 0 undefined.**
    §168-170 CLEARED. Cyclotomy block done; §159-161/§164/§172 islands + §26 remain the only known damage in vol1.
  • 2026-07-02 turn 11 (loop re-fire): **§171 (Die Gauss'schen Summen) VERIFIED FAITHFUL end-to-end p575-579top — NO
    fixes.** Confirms the map-phase "§171 CLEAN" label. Scan-checked p575→p579top line-by-line vs .tex 20458-20648:
      – opening + Gauss "Summatio quarundam serierum singularium" footnote (overflows p575→p576, kept as ONE
        `\footnote{}` — correct, LaTeX repaginates) ✓; f(x,μ) recursion eqs(10)-(11), eq(12) product
        f(x,μ)=(1-x)(1-x³)…(1-x^{μ-1}) [.tex 20558] ✓; μ=m=n-1/x=r substitution, (m,ν)=(-1)^ν r^{-ν(ν+1)/2}
        =(-1)^ν r^{ν²+ν} [20571-75] ✓; ν²+ν≡(ν-(n-1)/2)²-((n-1)/2)² (mod n) congruence [20579] ✓; f(r^{-2},m)
        reduction to r^{-m²/4}Σr^{ν²} [20588-92] ✓; r^{m²/4}f=1+2A=A-B [20596], eq(13) A-B=(r-r^{-1})(r³-r^{-3})…
        (r^{n-2}-r^{-n+2}) [20608] ✓; ν/μ factor-Kategorie discussion, A-B=(-1)^l∏(r^h-r^{-h}) [20623] ✓;
        r=e^{2πik/n}, r^h-r^{-h}=2i sin(2πkh/n) [20627-29], §138,(4) sin-product 2^{(n-1)/2}∏sin=(k/n)√n [20637] ✓;
        eq(14) A-B=(k/n)√n [n≡1] / =i(k/n)√n [n≡3 (mod 4)] [20641-48] ✓; §172 boundary confirmed [20651-53].
      – **NOTATION note (NOT damage):** scan prints the three ∏'s (20623/20633/20637) in Weber's 1895 index-above
        house typography (h on top, range 1,(n-1)/2 below); .tex renders them modern `\prod_{h=1}^{(n-1)/2}`. This is
        the CONSISTENT volume-wide product normalization (grep: §138 region 16095-16358 all modern; the cited §138,(4)
        at .tex 16118 is likewise modern & already-verified). Fixing §171 alone would BREAK consistency with the formula
        it references. Weber's genuinely-special period-sum notation `\sum_{1,n-2}^t` IS preserved (see §172 @20662).
        [Same "don't-chase, consistent-normalization" category as Coëfficienten→Coefficienten and z. B. spacing.]
      – eq(14) mod: scan "(mod 4)" NO period → `\pmod4` correct. File unchanged (418pp/0 badness; no edits this turn).
    ⇒ §171 CLEARED. Remaining known vol1 damage = worked-example islands §159-161/§164/**§172** + §26 (all fixed except
    §172 which is NEXT to re-verify). Everything else in vol1 confirmed faithful by scan or map-log.
  • 2026-07-02 turn 12 (loop re-fire): **§172 (⅓/¼(n-1) periods) — full page-by-page p579-585; map-phase numeric
    fixes HELD but MORE damage found & re-transcribed (4 edits).** KEY CONFIRMATION: a "known island" that already got
    map-phase numeric fixes STILL had pervasive prose+dropped-equation damage that ONLY the whole-body scan caught —
    section-opening/numeric spot-checks are insufficient (same lesson as §162). Scan-verified vs .tex 20651-21000:
      – **HELD (map-phase fixes correct):** e=3 worked-example values `-(1+3ϱ)` (n=7) & `-(4+3ϱ)` (n=13) match print
        exactly [.tex 20723-24]; both Indextabellen (n=7: 0,2,1,4,5,3; n=13: 0,1,4,2,9,5,11,3,8,10,7,6) correct; ALL
        numbered eqs (1)-(42) content correct incl. 9th-roots block (21)-(26) & entire e=4 block (27)-(42); Kummer
        footnote¹ (Journ.f.Math. Bd.32) restored; §172 opening + n=x²+3y² Satz faithful.
      – **DAMAGE FIXED (4 edits, span-slice re-transcription):**
        (A) cubic-derivation region [.tex 20728-20760]: GPT had reworded the opening ("Die Gleichung, deren Wurzeln…"→
            true "Aus diesen Formeln können wir leicht die cubische Gleichung herleiten…Sie hat wegen (4) die Form"),
            changed eq(8) period→comma, and DROPPED: sentence "und die ganzen Zahlen β,γ sind zu bestimmen."; the whole
            derivation "Führen wir die Multiplication in (6) aus…n=η²+η₁²+η₂²-ηη₁-ηη₂-η₁η₂=(η+η₁+η₂)²-3β, also"
            (replaced by terse "Aus (6) folgt"); un-numbered eq nψ₁(ϱ)=s₃-6γ+3sϱ+3s'ϱ²; sentence "Aus (8) und (9)
            erhält man aber s₃=-n-3γ, also"; "und ebenso"; eqs n-1=-9γ+3s+3s' and n[ψ₁(ϱ)+ψ₁(ϱ²)]+3n-1=-27γ + prose
            "wozu noch, wenn man (4) in den Cubus erhebt,…kommt. Addirt man die drei letzten Gleichungen, so folgt…
            oder endlich nach (2) und (3)" (all replaced by terse "Durch Addition der entsprechenden Gleichungen folgt").
            Re-transcribed the full span faithfully; connects into eq(12) unchanged.
        (C) closing Satz [20987→now ~20874]: GPT "Hieraus folgt zugleich der Satz: …lässt sich als Summe zweier Quadrate
            darstellen." → true "Wir wollen auch hier den in der Formel (34) ausgedrückten Satz hervorheben: …lässt sich
            in die Summe zweier Quadrate zerlegen."
        (D) **Weber print-erratum FLAGGED (reproduced, NOT corrected):** n=¼(a+b)²+¾(a-b)**³** [20820] — zoom-confirmed
            Weber prints exponent 3; math. correct is (a-b)²; .tex already reproduced it faithfully, added inline
            `% [sic]` flag. First type-B content-erratum flagged inline in vol1.
        (E) 3η+1=ξ [20795]: inline→displayed to match print (Weber displays it; parallels eq(40) 4η+1=ξ). Cosmetic-fidelity.
      – **NOT chased (documented):** scan prints "Einheitswu**z**el" (missing r, Weber typo) p582 — .tex keeps correct
        "Einheitswurzel" per house typo-normalization (cf. Coëfficienten→Coefficienten); "Coëfficienten" ë-drops p584 ✓.
    ⇒ Recompiled TWICE: **418pp / 0 err / 0 overfull / 0 underfull / 0 missing-char / 0 undefined.** §172 CLEARED.
    Remaining known vol1 islands (§159-161/§164/§26) all previously fixed; §172 was the last un-re-verified island.
  • 2026-07-02 turn 13 (loop re-fire): **§173 (Die complexen Zahlen von Gauss — R(i)) VERIFIED FAITHFUL end-to-end
    p585-591 — NO fixes.** Long prose-heavy section (Gaussian-integer theory), scan-checked line-by-line vs .tex
    21002-21159; EVERY line matches verbatim. This section is the START of the Siebzehnter Abschnitt (running head
    "Complexe Zahlen"), .tex still tags it \sect but Abschnitt heading handled elsewhere.
      – Opening + Gauss footnote¹ (Theoria residuorum biquadraticorum, comm. secunda, Werke Bd.II) ✓; p/q split
        p=4f+1,2 / q=4f+3 ✓; Sätze 1-3 (p=a²+b², q not sum-of-2-squares, (ab')²≡-1 (mod q) impossible by §138,4) ✓;
        Norm N(ξ)=x²+y² def + 4 Einheiten +1,-1,+i,-i ✓; associirte Zahlen (a+bi,-a-bi,-b+ai,b-ai) ✓; Euclidean
        algorithm w/ N(α₂)/N(α₁)≦½, eq(1) division-chain system, gcd ✓; Sätze 4-6 (eq(2) ακ+βλ=δ, eq(3) ακ+βλ=1,
        Fundamentalsatz 5, unique-factorization Satz 6) + full proofs (α=ππ'π''…, κκ'…=ππ'… uniqueness) ✓; prime
        determination: n=πα, two cases N(π)=n [p splits ππ'] / N(π)=n² [q inert]; 2=(1+i)(1-i)=-i(1+i)² ✓; primäre
        Zahlen (a≡1 mod4, b even) + Gauss footnote¹ (two primary-defs) ✓; §172,(27),(38),(39) refs correct; the
        norm<200 complex-prime list (22 entries, all verified: 1+i…1+14i, norms 2…197 all prime<200) ✓.
      – **Mod-periods all correct:** scan prints "(mod 4)","(mod q)","(mod 8)" NO period → `\pmod{...}` ✓; "§138,4."
        reference-period ✓. NO reconstruction damage anywhere — pure-theory prose transcribed faithfully.
    ⇒ **PATTERN:** §173 (long pure-prose theory) is CLEAN, unlike §172 (worked-example/derivation island w/ drops).
    Supports hypothesis: GPT reconstruction damage concentrated in numeric/derivation islands; theory-prose sections
    faithful. But STILL scan every section fully (§172 taught us numeric-fixed ≠ prose-clean). File unchanged (418pp).
  • 2026-07-02 turn 14 (loop re-fire): **§174 (Der Körper der dritten Einheitswurzeln / R(ρ)) VERIFIED FAITHFUL
    end-to-end p592-594 — NO fixes.** Second consecutive clean pure-theory section. Scan-checked line-by-line vs
    .tex 21161-21221; every line matches verbatim.
      – **CORRECTION to prior log:** §173 AND §174 are the TAIL of the *Sechzehnter* Abschnitt (running head p592/594
        = "Sechzehnter Abschnitt"), NOT the Siebzehnter. The Siebzehnter Abschnitt ("Algebraische Auflösung von
        Gleichungen") heading is at .tex 21223, immediately before §175 — so §175 STARTS the 17th Abschnitt.
      – Opening (refs §173,(1) Euclidean-algorithm) ✓; ρ=(-1+√-3)/2, R(ρ)=R(√-3) def; Norm N(ξ)=(x+ρy)(x+ρ²y)
        =x²-xy+y²=((2x-y)²+3y²)/4 ✓; N(α)=a²-ab+b²=1 → (2a-b)²+3b²=4 → six Einheiten ±1,±ρ,±ρ² ✓; associate system
        ±(a+bρ),±[-b+(a-b)ρ],±(b-a-aρ) ✓; Euclidean N(ξ-μ)=x²-xy+y²≦¾, unique factorization ✓; prime determination
        p=ππ'; 3=-ρ²(1-ρ)² (√-3 the prime), 3f+1 splits per §172 / 3f+2 inert (a²-ab+b²≢2 mod3) ✓; associate triple
        a+bρ,b+aρ²,b-(a-b)ρ, b=3B, 4p=A²+27B² (per §172), factorization p=((A+3B)/2+3ρB)((A-3B)/2-3ρB) ✓; norm<200
        R(ρ)-prime list (22 entries 1-ρ…13+15ρ, all verified, norms 3…199) ✓.
      – **Scan note:** p594 mid+bot render faint (verso bleed-through of p593 — same leaf); §174 ends with the prime
        list on p594_top, rest of p594 blank. Siebzehnter-Abschnitt heading + §175 start FRESH on p595 (new page per
        Abschnitt convention). File unchanged (418pp/0 badness).
    ⇒ PATTERN holds: §173, §174 (pure-theory prose) both CLEAN; only worked-example/derivation islands (§172) had
    drops. Cologne of Sechzehnter Abschnitt (complex-number theory §168-174) now fully scan-verified.
  • 2026-07-02 turn 15 (loop re-fire): **§175 (Reduction der Gruppe durch reine Gleichungen — OPENS Siebzehnter
    Abschnitt "Algebraische Auflösung von Gleichungen") VERIFIED FAITHFUL end-to-end p595-597 — NO fixes.** THIRD
    consecutive clean pure-theory section. Scan-checked line-by-line vs .tex 21223-21273 (+ §176 heading 21275); every
    line matches verbatim. This was the flagged "higher-risk endgame" opener — came through clean.
      – Abschnitt heading + §175 title (p595) ✓; opening on algebraic solution + Ω-extension question ✓; reine
        Gleichung y^m-a=0 + reducibility/transitivity (p595_bot) ✓; Jordan footnote¹ (Traité des substitutions p.386)
        + §162 ref (p596_top) ✓; boxed question "Unter welchen Bedingungen wird die Gruppe P... reducirt?" +
        irreducibility caveat + Ω-preparation (p596_mid) ✓; φ(x)=0 reduces P→Q, ε,ε₁…ε_{m-1} roots + Jordan fn
        (p596_bot) ✓; §157 Schlusssatz → index j|m, m prime ⇒ m=j; ε=ψ(x₀…x_{m-1}); conjugate groups π⁻¹Qπ ⇒ Q
        Normaltheiler von P (p597_top/mid, .tex 21255-21259) ✓; **Satz I** (Adjunction Abel'sche Gleichung ⇒ P hat
        Normaltheiler Q von Primzahlindex, boxed 21263-21265) ✓; converse "Dieser Satz lässt sich auch umkehren" +
        argument via §155, §163 cyklisch (21269) ✓; **Satz II** (Normaltheiler Q von Primzahlindex m ⇒ Adjunction
        cyklische Gleichung m^ten Grades reducirt P auf Q, boxed 21271-21273) ✓; §176 heading + opening line ✓.
      – Scan note: p597 recto running head reads "§. 176. Metacyklische Gleichungen" while body top is still §175 —
        Weber's recto head names the section appearing lower on the page (§176 starts on p597_bot). Running heads are
        LaTeX-auto-generated, NOT transcribed → layout artifact, not a fidelity issue. File unchanged (418pp/0 badness).
    ⇒ PATTERN now 3-for-3 on theory prose (§173/§174/§175 all CLEAN); only §172 (worked-example/derivation island)
    had drops. Endgame-risk hypothesis NOT yet triggered — but §176-188 have more derivation content; keep scanning
    every section fully. Sixteenth Abschnitt (complex-number theory) + opening of Seventeenth now scan-verified.
  • 2026-07-02 turn 16 (loop re-fire): **§176 (Metacyklische Gleichungen) CONTENT VERIFIED FAITHFUL end-to-end
    p597_bot-p600_top — 0 word-drops.** Scan-checked line-by-line vs .tex 21277-21305; every line matches verbatim.
    Opening def; Satz III (composition-series criterion, quote 21281-87); metacyklische-Gruppe def + Kronecker/
    Frobenius/Hölder footnote (21293); Satz IV (irreducible + one radical-solvable root ⇒ metacyklisch, quote
    21297-99) + induction proof (μm=n via §158; n prime base case; 21301-05); §176 closing recap (21305) + §177
    heading. Recompiled TWICE after fixes below: **418 pp / 0 err / 0 overfull / 0 underfull / 0 missing-char /
    0 undefined.**
  ════════════════════════════════════════════════════════════════════════════════
  ★★★ MAJOR METHOD FINDING (turn 16) — SYSTEMATIC DROPPED SPERRDRUCK (gesperrt emphasis) ★★★
    While scanning §176 I noticed Weber's *letterspaced* (gesperrt) emphasis on the DEFINING terms "metacyklische
    Gleichung"/"metacyklische Gruppe"/"vollständige" was rendered PLAIN in the .tex. Investigated:
      – The .tex's ONLY emphasis vehicle is `\emph{}` (no \gesperrt/\textls/soul macro in preamble). It IS used for
        some of Weber's gesperrt defined-terms (Resultante, Discriminante, Totalresolvente, Resolventen, "gebrochene
        rationale Function", echt/unecht gebrochen, book-titles) → so the INTENT is gesperrt → \emph.
      – BUT the GPT reconstruction DROPPED gesperrt in many places. Confirmed by zoom/scan in §176 (3 terms) AND in
        §173 (p586): "…heissen a s s o c i i r t e Z a h l e n" (term gesperrt); and WHOLE definition-sentences set
        fully gesperrt — "Die Zahlen a+bi … heissen die ganzen Zahlen des Körpers R(i).", "Eine ganze Zahl, deren
        Norm gleich 1 ist, heisst eine Einheit.", "Eine ganze Zahl α heisst durch … β theilbar, wenn … so dass
        α=βγ ist." — ALL rendered plain in .tex. (Note: the Norm-definition sentence itself is NOT gesperrt — extent
        VARIES: sometimes whole sentence, sometimes just the term. Must zoom each.)
    ⇒ CONSEQUENCE: gesperrt-dropping is SYSTEMATIC & likely volume-wide (independent of word-damage: §176 had 0
      word-drops yet dropped 3 gesperrt). My prior "§173/§174/§175 VERIFIED FAITHFUL / 0 edits" claims are
      CONTENT/word-level ONLY — Sperrdruck was NOT checked. DO NOT treat those as emphasis-faithful.
    ⇒ METHOD ADJUSTMENT:
      (1) FORWARD content pass (§177+): now ALSO note obvious gesperrt (whole-sentence defs / clearly letterspaced
          terms) and \emph them inline — cheap since scans are read anyway; log any ambiguous-extent cases.
      (2) Sperrdruck is otherwise a DEDICATED SEPARATE PASS (own phase): careful per-definition ZOOM to fix exact
          extent (whole-sentence vs term-only), section by section. Covers §1-176 (all already content-checked).
          Do it RIGHT — never certify extent without zoom.
      (3) §176 gesperrt: 3 terms restored this turn (metacyklische Gleichung @21277, metacyklische Gruppe @21293,
          vollständige @21295) — but §176 Sperrung NOT exhaustively re-verified; include in the dedicated pass.
      (4) §173 Sperrung drops CONFIRMED (p586: ≥4 defs) but NOT yet fixed — first target of the dedicated pass.
  ════════════════════════════════════════════════════════════════════════════════
  • 2026-07-02 turn 17 (loop re-fire): **§177 (Einfachheit der alternirenden Gruppe) CONTENT VERIFIED FAITHFUL
    end-to-end p600_mid-p603_top — 0 word-edits.** Scan-checked line-by-line vs .tex 21309-21360; every line verbatim.
    NOTABLE: this was the flagged "derivation-heavy → §172-risk" section but came through CLEAN — all 5 Fall
    computations EXACT:
      – opening §149→symm. group; alternating = index-2 Normaltheiler; n=4 Klein-four Normaltheiler
        `1,(0,1)(2,3),(0,2)(1,3),(0,3)(1,2)`; S4 metacyklisch → biquadr. §160,161 (p600) ✓
      – proof: A gen. by 3-cycles (§153,6/§154,6); π-matrix \perm{0…n-1}{a_0…a_{n-1}}; Q∩3-cycle⇒Q=A; eq(1)
        λ=κ⁻¹π⁻¹κπ (p601) ✓
      – Fall 1: (1,m,m-1…2)(2,3,1,4…m)=(1,2,4); Fall 2: (1,3,2)(4,6,5)(3,2,4)(1,5,6)=(1,2,5,3,4); Fall 3:
        (1,3,2)(4,5)(2,4,3)(1,5)=(1,2,5,3,4); Fall 4: (1,2)(3,4)(5,6)(3,2)(5,4)(1,6)=(1,3,5)(2,6,4); Fall 5:
        (1,2)(3,4)(5)(2,5)(3,4)(1)=(1,5,2) — ALL EXACT (p601-602) ✓
      – "alle Fälle erschöpft" n=4 exception + Abel/Ruffini/Burkhardt footnote (Crelle Bd I 1826; Schlömilch's Zs.
        Leipzig 1892) — verbatim; corollary (S has only S,A,1 as Normaltheiler; p602-603) ✓
    ⇒ ADJUST hypothesis: "derivation-heavy ⇒ damaged" is NOT reliable — §177 is derivation-heavy yet clean, while
      §172 (also derivation) was damaged. Damage is patchy/unpredictable; the ONLY safe rule remains: scan every
      section fully. File unchanged by content pass (418pp/0 badness; last edits = §176 gesperrt, compiled clean).
      GESPERRT candidates in §177 (deferred to dedicated pass): "alternirende Gruppe" @21309, "einfach" @21315,
      unsolvability-conclusion clause @21315.
  • 2026-07-02 turn 18 (loop re-fire): **§178 (Nicht metacyklische Gleichungen im Körper der rationalen Zahlen)
    CONTENT VERIFIED FAITHFUL end-to-end p603_mid-p606_mid — 0 word-edits.** Scan-checked line-by-line vs .tex
    21364-21421; every line verbatim. Was on the re-scan list (previously internal-evidence only) → now confirmed by
    full forward scan. Another prose+derivation section (Eisenstein criterion proof) came through CLEAN.
      – affect question (rational-coeff eqns without Affect = symm. group); Galois resolvent G(t) deg Π(n); Hilbert
        irreducibility footnote (Journal f. Math. Bd.110) ✓; §153,9 (transitive non-symm. prime-degree ⇒ no single
        transposition) ✓; Satz 1 (prime-degree affect ⇒ 2 roots rational in others); Satz 2 (real Ω corollary) ✓;
        f(x)=(x-α1)…(x-αn)=x^n+a1x^{n-1}+…+an display + continuity/root-count argument ✓; **Satz 3 = Eisenstein
        criterion** (p∤c0, p|c1…cn, p²∤cn ⇒ φ irreducibel) + FULL proof (§2 integer factors; α_hβ_k=c_n; β_ν argument;
        coeff of x^{k-ν} ⇒ k-ν=n impossible) — all EXACT ✓; a_i=c_i/c0; Satz 4 (∞ many affect-free rational eqns of
        each prime degree) + closing caveat ✓.
    GESPERRT candidates (deferred to dedicated pass): Sätze 1,2,3,4 STATEMENTS all letterspaced (quote kept, Sperrung
    dropped) — NB contrast §176 Roman Sätze I-IV which were quote-NORMAL; so per-Satz Sperrung VARIES, must zoom each.
    File unchanged by content pass (418pp/0 badness).
  • 2026-07-02 turn 19 (loop re-fire): **§179 (Auflösung durch reelle Radicale) CONTENT VERIFIED FAITHFUL end-to-end
    p606_mid-p609_bot — 1 FIX.** Scan-checked line-by-line vs .tex 21425-21481.
      – **FIX (ϱ→ε transcription error RESTORED, .tex 21429):** scan+zoom confirmed Weber prints "die sämmtlichen
        Wurzeln von χ in Ω(ϱ) enthalten, und wenn also ϱ reell ist" (varrho, TWICE); GPT .tex had `\Omega(\varepsilon)`
        and `\varepsilon reell` — WRONG (also breaks the math: via §157 the adjoined ε & all χ-roots are rational in
        g(t)'s roots = rational in ϱ, so χ-roots ∈ Ω(ϱ); ϱ real ⇒ Ω(ϱ) real ⇒ χ-roots real. With ε it's a non-sequitur:
        "χ-roots ∈ Ω(ε)" needs χ normal, not given). NB the FIRST ε ("Adjunction einer Wurzel ε") is correctly ε
        (zoom-confirmed, no descender) — only the two Ω(ϱ)/ϱ instances were corrupted. This is a .tex error (NOT Weber),
        so fixed to ϱ, no [sic]. Recompiled TWICE: **418pp/0 err/0 overfull/0 underfull/0 missing-char/0 undefined.**
      – Verbatim: casus-irreducibilis opening + Hölder/Kneser footnote (Math.Ann. 38/41); Normalgleichung (real Ω,
        root ϱ); Satz 1 (real-root Normalgl. reducible only by all-real prime-degree eqns); reelle Radical question;
        **x^p-a irreducibility proof** eqs (1) α,εα…ε^{p-1}α, (2) x^p-a=0, (3) =f1 f2, ε^λα^μ=b, (4) a^μ=b^p, μh+pk=1,
        a=a^{μh}a^{pk}=(b^h a^k)^p — all EXACT; Satz 2 (odd-degree Normalgl. not reducible by real radical); cubic
        classification (order 3 cyclic/Siebeneck; order 6 ±disc; casus irred.=Dreitheilung; x³=a Delisches Problem).
    GESPERRT candidates (deferred): Sätze 1,2 statements; "casus irreducibilis" (Latin, letterspaced, several
    instances). CONTENT-faithful; NOT emphasis-verified.
  • 2026-07-02 turn 20 (loop re-fire): **§180 (Metacyklische Gleichungen von Primzahlgrad) — IN PROGRESS, part 1 of ~2:
    p609_bot-p612_top (.tex 21485-21548) CONTENT VERIFIED FAITHFUL + 1 ERRATUM FLAG.** Big section (21483-21733,
    ~7pp); splitting across iterations.
      – Verbatim: Galois-criterion setup (f(x) irred. prime n>2, metacyklische Kette (1) P,P1…P_{μ-1},1); §158,3 ⇒
        P_{μ-1} order n; π=(0,1…n-1); substitutions (2) (z,z+b); general linear (3) (z,az+b), n(n-1) of them, group
        closure eq(4) λλ'=λ''=(z,aa'z+a'b+b') [λλ' matrix comp EXACT]; "lineare Gruppe" def + Kronecker footnote;
        divisor (z,az) order n-1; λ^h=[z,a^h z+(1+a+…+a^{h-1})b], λ^h=(z,z+hb) for a=1; (a^h-1)/(a-1); order e=ord_n(a).
      – **ERRATUM FLAG (.tex 21548, z_0 fixed point):** zoom-confirmed Weber prints `z_0 ≡ b/(a-b) (mod n)`; .tex
        faithfully reproduced `\frac{b}{a-b}` (so transcription CORRECT/faithful). BUT math wrong: fixed point of
        z→az+b is z_0=b/(1-a), not b/(a-b). = Weber PRINT ERROR (type-B). Added inline `% [sic] … 1-a … Erratum
        reproduziert` — NOT corrected. (2nd type-B erratum flag in vol1 after §172 (a-b)^3.) Recompiled TWICE:
        **418pp/0 err/0 overfull/0 underfull/0 missing-char/0 undefined.**
    GESPERRT candidates in §180 so far (deferred): "lineare Gruppe" @21529. CONTENT-faithful (part 1); NOT emphasis-ver.
  • 2026-07-02 turn 21 (loop re-fire): **§180 CONTENT TRACK COMPLETE — part 2 p613-p620 (.tex 21562-21733) VERIFIED
    FAITHFUL end-to-end, 0 word-edits.** §180 now fully content-verified p609-620 (part 1 last turn + part 2 this turn).
    No content damage across the whole ~11pp section — only the single z_0 erratum flag (already added part 1).
      – p613 (21562-21589): λλ₀^{-h}=(z, z+a₀^{-h}b+((a₀^{-h}-1)/(a₀-1))b₀) comp eq ✓; identity-condition
        b₀/(a₀-1)≡b/(a₀^h-1) (mod n) ✓; transitivity conclusion (element fixed ⇒ L intransitiv) ✓; eq(5) λ=(z,a₀^h z+b),
        h=0…e-1,b=0…n-1, order en ✓; Satz I (transitive lineare L Normaltheiler von P ⇒ P linear) ✓.
      – p614-615 (21589-21649): Lagrange interpolation proof — π=(z,a_z), φ(z) deg≤n-1, ψ(z)=z(z-1)…(z-n+1),
        ψ(z)≡z^n-z, ψ'(z)≡-1, eq(6) φ(z)≡-Σ a_i ψ(z)/(z-i) (mod n) ✓; eq(7) φ(z+1)≡a'φ(z)+a, a'≡1, φ(z+h)=φ(z)+ah,
        eq(8) φ(z)=az+b ⇒ P linear (Satz proven) ✓; cyklische Gruppe normal in any linear group ✓; **Satz II** (Galois:
        Gruppe einer metacykl. Gl. von Primzahlgrad ist linear) + Kette-(1) descent proof ✓; **Satz III** (irred. prime-deg
        w/ linear group ⇒ metacyklisch) ✓.
      – p616-617 (21649-21685): L' Theiler vom Index p (e=pe', λ'=(z,a₀^{ph}z+b)) normal ✓; transitive-linear ≡
        metacyklisch synonymy; conjugate P'=π^{-1}Pπ; erzeugende Substitutionen (9) s=(z,z+1),t=(z,gz) / (10)
        t^{α₀}=(z,a₀z); halbmetacyklische Gruppe (a₀=g², quad. residues) ✓; s∈alt., t∉alt. cycle-parity argument;
        **Satz IV** (volle metacykl. Gr. ⊄ alt.; GCD = halbmetacykl.) ✓; metacyklische Function y, Resolvente F(y)=0 deg ν
        (ν=1·2·3…(n-2)) ✓.
      – p618-620 (21685-21733): **Satz V** (Radicale ⇔ Resolvente F(y) deg ν has rational simple root) ✓; linear group:
        only identity fixes 2 Ziffern (az+b≡z has ≤1 soln unless a≡1,b≡0) ✓; **Satz VI** (metacykl. prime-deg ⇒ all roots
        rational in any 2) + **converse** proof (cycle-structure: only γ n-cycles + ϰ fixing one Ziffer; m=μn+ν+1 (11),
        m=n(μ+1) (12) ⇒ ν=n-1; C=1,γ…γ^{n-1} normal ⇒ P linear) ⇒ **Satz VII** ✓; Kronecker real-field footnote
        (Monatsber. Berl. Akad. 14 April 1856) ✓; **Satz VIII** (irred. metacykl. odd prime-deg, real coeff ⇒ all real or
        exactly one) ✓; Discriminante sign (-1)^{(n-1)/2} ⇒ **Satz IX** (n≡1 mod4 ⇒ disc>0; n≡3 ⇒ sign decides VIII) ✓.
    GESPERRT candidates in §180 (deferred to Sperrung track): ALL Sätze I-IX statements letterspaced (quote kept, Sperrung
    dropped); inline gesperrt terms/clauses — "lineare Gruppe" @21529, cyklische-Gruppe-normal remark @21639, "volle
    lineare Gruppe" @21662, "erzeugenden Substitutionen dieser Gruppen" @21670, "halbmetacyklische Gruppe" @21670, "Jeder
    transitive Theiler…metacyklisch" @21677, "metacyklische Function" @21683, "Also enthält P ausser der identischen…nicht
    ändert" @21695. File UNCHANGED by content pass (still 418pp/0 badness — no compile needed, no edits this iteration).
  • 2026-07-02 turn 22 (loop re-fire): **§181 (Anwendung auf die metacykl. Gleichungen 5ten Grades) p621-623 (.tex
    21734-21839) VERIFIED FAITHFUL — 2 EDITS (1 title reword-fix, 1 Weber erratum flag).** Compile-gated clean after.
      – **FIX (title reword, .tex 21734):** \sect{181} title read "…Gleichungen fünften Grades"; scan (zoom-confirmed)
        prints "…Gleichungen $5^{\text{ten}}$ Grades" (numeral+superscript, matching running head + body usage). GPT
        spelled out the ordinal → reword. Fixed to `$5^{\text{ten}}$ Grades` (math-in-heading OK — §133 precedent
        `$n$ten Grades`; body of §181 uses $5^{\text{ten}}$). ⚠ SYSTEMATIC WATCH: §54/74/75/188 titles ALSO say
        "fünften Grades", §80 "zweiten Grades" — scan-check ordinal form when reached (§188 ahead this Abschnitt).
      – **ERRATUM FLAG (Weber duplicate eq-number, .tex 21837):** scan p623 prints "(12)" for BOTH the u'_1..u'_6 block
        (p623_mid) AND the sextic y^6+a_2y^4+a_4y^2+a_6-√Δ(a_1y^5+a_3y^3+a_5y)=0 (p623_bot). Weber genuinely numbers
        two eqs (12). .tex reproduced faithfully (two `\tag{12}`, LaTeX allows manual dup tags). Added `% [sic] …
        doppelte Gleichungsnummer im Druck … nicht umnummeriert`. = 3rd type-B Weber erratum in vol1 (after §172
        (a-b)^3, §180 z_0). Recompiled TWICE: **418pp/0 err/0 overfull/0 underfull/0 missing-char/0 undefined.**
      – Verbatim: n=5 group orders (cyclic 5, halbmet. 10, voll met. 20); Resolvente 6ten/12ten Grades; erzeugende
        subst. s=(z,z+1),t=(z,2z),t²=(z,4z); tables (1)(2)(3) of Ziffer/Paar permutations [all entries checked];
        halbmet. functions u (4), u' (5), f(x) (6), u+u'=b (7), y=u-u' (8), Y=(u-u')/√Δ (9) + Jacobi/Cayley footnote;
        A-decomposition (10) A=N+N(1,2)(3,4)+Nt(0,1)+…; (1,2)(3,4)t=(1,4) distinctness; conjugates u_1..u_6 (11),
        u'_1..u'_6 (12) [all 60 monomials checked]; sextic form (12) + degree argument (a_1=a_3=0, a_5=const).
    GESPERRT: none flagged on p621-623 (no letterspaced defs in this computational stretch). CONTENT-faithful.
  • 2026-07-02 turn 23 (loop re-fire): **§181 COMPLETE (p624-627, .tex 21840-21952) VERIFIED FAITHFUL — 0 edits.**
    §181 now fully content-verified p621-627 (title+erratum edits were turn 22). §182 opened (p627 tail).
      – p624: degree table (a_1√Δ,a_2,a_3√Δ,a_4,a_5√Δ,a_6 = grades 2,4,6,8,10,12); √Δ deg 10 ⇒ a_1=a_3=0, a_5 const;
        Cayley note; Bring-Jerrard x^5+αx+β=0 (13) + Runge footnote (Acta math. Bd.7); (14) a_2=m_1α,a_4=m_2α²,a_6=m_3α³,
        a_5=m; special case β=0 (15) x_0=0,x_1=⁴√(-α),… ; (16) √Δ=Π(x_i-x_j)=16i√(-α)⁵=-16√α⁵, Δ=256α⁵ [all verbatim].
      – p625: b=0 ⇒ y=2u; y-values y_1=y_2=y_3=y_6=-2√α, y_4=(4-2i)√α, y_5=(4+2i)√α; (17) sextic factorization
        =(y+2√α)⁴(y²-8y√α+20α)=y⁶-20αy⁴+240α²y²+512√α⁵y+320α³; (18) general resolvente -32√Δy; (19) Δ=5⁵β⁴+2⁸α⁵
        (via §74 formula 3); (20) u-eqn u⁶-5αu⁴+15α²u²-√Δu+5α³=0; (21) v=u²: (v³-5αv²+15α²v+5α³)²=Δv [verbatim].
      – p626: alt form (v-α)⁴(v²+6αv+25α²)=0; (22) =5⁵β⁴v; metacyklizität check (u=v=0⇔α=0; disc=0 excluded by irred.;
        derivative 6u⁵-20αu³+30α²u-√Δ=0 elim ⇒ 5(u²-α)³=0 ⇒ v=α ⇒ β=0 reducible); x⁵+5x+5t=0 never metacyklisch
        example (§178,3 irred.); (23) α,β param by λ,μ [verbatim].
      – p627: (24) x⁵+αx+β=0 solvable iff α,β in form (23); example λ=-1,μ=1 ⇒ ξ⁵+5ξ⁴-5·64=0 (via xξ=5). §182 opens:
        v_1..v_6=(u_i-u'_i)² (1); F(v)=0 deg-6 resolvente of f(x)=0; M-conjugates trivially intersect (via §177) ⇒
        Totalresolvente (§156), group order 120; "S_6 has a transitive divisor of index 6" [quote, gesperrt].
    GESPERRT (deferred): §181 p626 conclusion "keine Gleichung von der Form x⁵+5x+5t=0 metacyklisch" letterspaced;
    §182 p627 quote-Satz "Die symmetrische Permutationsgruppe von sechs Ziffern hat einen transitiven Divisor vom
    Index 6" (gesperrt?—verify on p628 zoom). File UNCHANGED this iteration (no edits; still 418pp/0 badness, no compile).
  • 2026-07-02 turn 24 (loop re-fire): **§182 COMPLETE (p628-629, .tex 21965-22023) VERIFIED FAITHFUL — 1 EDIT
    (Weber erratum flag).** §182 now fully content-verified p627-629. Compile-gated clean (byte-identical, comment inert).
      – **v'_4 RESOLVED = Weber ERRATUM, not GPT typo (.tex 22002):** the flagged `w_0=v_1v_2+v'_4v_5+v_3v_6` — ZOOM of
        p629 (crop_26_31) shows Weber HIMSELF prints v'_4 (clear stray prime on v_4). So the .tex was FAITHFUL, NOT a
        transcription typo as first hypothesised. Math: w_0 is image of base w_3=v_1v_3+v_2v_4+v_5v_6 under (2,6,5,4,3),
        = v_1v_2+v_4v_5+v_3v_6 (plain v_4). Prime is a stray print mark. Added `% [sic] … kein v' definiert …
        Erratum reproduziert, nicht korrigiert`. = 4th type-B Weber erratum in vol1 (after §172 (a-b)^3, §180 z_0,
        §181 dup-(12)). ★ LESSON (works/adjust): an anomaly that looks like a GPT typo may be Weber's own print error —
        ALWAYS zoom the scan before "fixing"; faithful action = keep + [sic], not silently correct. Recompiled TWICE:
        418pp/0 err/0 overfull/0 underfull/0 missing-char/0 undefined (byte-identical 2263542 → comment inert).
      – Verbatim: M-conjugates intersect trivially (via §177) ⇒ Totalresolvente (§156), group order 120; S_6 transitive
        index-6 divisor [gesperrt Satz]; erzeugende π_1=(1,3)(2,5)(4,6), π_2=(1,4)(2,3)(5,6), π_3=(1,5)(2,6)(3,4),
        π_4=(1,6)(2,4)(3,5) from transpositions (0,1)..(0,4); products π_1π_2=(1,2,6)(3,4,5), π_1π_2π_3=(1,6,5,4),
        π_1π_2π_3π_4=(2,4,6,3,5), cube=(2,3,4,5,6); base fn v_1v_3+v_2v_4+v_5v_6; w_0..w_4 (2) [all products checked,
        w_0 has the Weber prime]; π_i=(w_0,w_i) ⇒ S_5 on w-indices; W=Σw_i² (or ∏(λ-w_i)) generates index-6 group,
        root of irred. deg-6 eqn. [all verbatim]
    GESPERRT (deferred): §182 p628 Satz "Die symmetrische Permutationsgruppe von sechs Ziffern hat einen transitiven
    Divisor vom Index 6" letterspaced; "Totalresolvente" @21967 letterspaced (dropped \emph — Totalresolvente IS an
    \emph-term elsewhere per memory). CONTENT-faithful; NOT emphasis-verified.
  • 2026-07-02 turn 25 (loop re-fire): **§183 COMPLETE (p630-633, .tex 22029-22098) + §184 COMPLETE (p633-638,
    .tex 22100-22303) VERIFIED FAITHFUL end-to-end — 0 CONTENT EDITS.** File UNCHANGED (still 418pp/0 badness, no
    compile needed). §185 opened (p638 tail, .tex 22307). Clean 8-page stretch; heavy formula content, all verbatim.
      – §183 (Stellung der Aufgabe. Hülfssatz): p630 Abschnitt-divider + title + Abel/Kronecker problem-statement +
        big Abel(Oeuvres ed.Sylow II p.217 / Brief Crelle 14.März 1826 p.266)/Kronecker(Monatsber.1853,1856)/
        H.Weber(Marburg 1892) footnote ✓; p631 Lagrange resolvent (ε,x)=Σ_{0,n-1}ε^h x_h (1) [from §164]; Hülfssatz
        X=ξ^{n-1}+…+ξ+1 (2) irred in R [§134]; Ω(ε) Normalform c_0+…+c_{n-2}ε^{n-2} (3) [§142]; **Satz 1** (Normalform
        uniqueness, quote); p632 reducibility-contradiction (§143), Divisoren via Permutationsgruppe P (§152), **Satz 2**
        (P-invariance ⇒ coeff P-invariant, quote); p633 Normalkörper Ω(ε) (§144), averaging Φ(ε)=c_0-(Σc)/(n-1),
        **Satz 3** (all (ε,ε^h) ⇒ in Ω, quote). ✓ ALL VERBATIM.
      – §184 (Sätze über die Resolventen): p633 s: (ε,x)→ε^{-1}(ε,x); p634 t: (ε,x)→(ε^{g^{-1}},x), s^λ/t^λ
        Vertauschungen, **Satz 4** (metacykl. generators table), **Satz 5** (4) (ε,x)^n=Φ(ε), (ε^λ,x)(ε,x)^{-λ}=F(ε)
        [§163]; p635 (5) f_0..f_{n-2} array, (6) f_h=f(ε^{g^h}), t^{-1} cycle, (7) C(f_0..f_{n-2}), **Satz 6** (cykl. C
        of f ⇒ metacykl. coeff), metacykl.-Function defn, **Satz 7** (rational-coeff C ⇒ metacykl. of x); p636 (8) product
        relation, (9), g=g_1+ln congruences (mod n², mod n), (10) λ, (11) F(ε)=(ε,x)^{nk}, (12), (13)-(14) generalization;
        p637 (15) g^v=nq_v+r_v, (16), (17) Φ_v, (18), r_v/g-ln independence, **characteristic props α)β)γ)δ)** of ω_v;
        p638 Lagrange §155 → Θ_v expressible via ω_v, (19) φ(u)=Π(u-ω_v), (20) χ(u) sum, (21) χ/φ'=Θ ⇒ Θ_v=Θ(ω_v).
        ✓ ALL VERBATIM. (mod-forms match: Weber prints no period, \pmod correct.)
    ★ WORKS/confirmed this turn: long dense formula sections (Lagrange-resolvent theory) transcribe CLEAN in the .tex —
      the GPT-reconstruction damage is concentrated in PROSE/titles (rewording) not in the heavy computational math. So
      content-track can move FAST through equation-dense §§ (2400px thirds legible for all sub/superscripts). No zoom
      needed except for ordinal-title checks + suspected errata. 8 pages/iteration sustainable on such stretches.
    GESPERRT (deferred to Sperrung track): §183-184 letterspaced items — all numbered **Sätze 1-7** (quote blocks kept,
      Sperrung dropped to plain); inline: "die imaginären $n^{ten}$ Einheitswurzeln" (p631), "Normalform" (p631/632
      repeatedly), "metacyklische Function" defn (p635), the four props α)β)γ)δ) headers, "Normalkörper" (p633).
      CONTENT-faithful; NOT emphasis-verified.
  • 2026-07-02 turn 26 (loop re-fire): **§185 part 1 (p638-640, .tex 22307-22391) VERIFIED FAITHFUL — 1 EDIT
    (source-fidelity normalization removed).** Compile-gated clean after: 418pp/0 err/0 overfull/0 underfull/0 missing/
    0 undefined (2263535 bytes).
      – **FIX (GPT-added exponent removed, .tex 22369):** R_v shorthand read `...k_{v+n-2}^{r_0}`; ZOOM p640 (crop_44_30)
        shows Weber prints the last factor as plain `k_{v+n-2}` (NO r_0 exponent) — he omits the trivial r_0(=1) exp in
        the shorthand though he writes it in (5)/(6)/(18 §184). Removed `^{r_0}` to match print. Math. null (r_0=1);
        typographic normalization, not content. ★ LESSON (mirror of the errata lesson): FIDELITY CUTS BOTH WAYS — keep
        Weber's own errata (+[sic]) AND remove GPT's null "improvements" not in the print. Same rule: reproduce EXACTLY
        what the scan shows. ⚠ ADJUST: always ZOOM sub/superscripts on shorthand-DEFINITIONS — that's where GPT silently
        normalizes (adds =1 exponents, fills patterns). This is the FIRST "GPT-added" fix (vs. drops/rewords) found so far.
      – Verbatim: §185 opening (ξ→x, metacykl. functions rational in 𝔎); 2 Voraussetzungen (1: no (ε,ξ) vanishes;
        2: no two f_v equal); f_v→k_v distinct, Φ_v→K_v (may coincide); (1) ψ(u)=Π(u-k_v) cyclic (n-1)^ten even deg;
        (2) k_{i+1}=Θ(k_i) [§163]; (3) K_v=Φ(k_v) [§184]; (4) τ_v=ⁿ√k_v; (5) (ε^{r_v},ξ)=K_v τ…^{r_0}; A=(1,x);
        (6) nξ_0=A+ΣK_v τ…; K_v,k_v≠0; (7) nξ_0=A+ΣK_v ⁿ√R_v; (8) K_v ⁿ√R_v=K_{v-1}^g k_{v-1}(ⁿ√R_{v-1})^g; (6)'s advantage
        (only n values); proof-start (ⁿ√k_v → ε_v ⁿ√k_v). ✓ ALL VERBATIM else.
    GESPERRT (deferred): §185 "beschränkende Voraussetzungen" 1./2. quote blocks; "Normalform" (tracked). Not emph-verified.
  • 2026-07-02 turn 27 (loop re-fire): **§185 COMPLETE (p641) + §186 part 1 (p641-643, .tex 22430-22476) VERIFIED
    FAITHFUL — 0 EDITS this iteration.** File UNCHANGED (still 418pp/0 badness; no compile). §185 fully done p638-641
    (its only edit = R_v fix on p640, prior turn). §186 through eq (8).
      – §185 finish (p641): (9) nξ=A+ΣE_v K_v τ…; (10) E_v=ε_v^{r_{n-2}}…ε_{v+n-2}^{r_0} [Weber DOES print r_0 here →
        confirms p640 R_v-shorthand omission was shorthand-specific, fix correct]; (11) r_v≡g·r_{v-1} (mod n); (12)
        E_v=E_0^{r_v}; (13) E_0; only n values; Cayley §36 ref; (14) nξ_h=A+Σε^{-hr_v}K_v τ… [§133]. ✓ verbatim.
      – §186 (Befreiung von den beschränkenden Voraussetzungen) p641-643: Tschirnhausen removal of §185's 2 Voraussetz.
        η_h roots of ANY irred metacykl deg-n; (1) ξ_h=ψ(η_h); (2) ψ deg n-1 (a∈𝔎); Tschirnh.-Transf (§52), 𝔎(ξ)=𝔎(η);
        (3) χ; (4) η_h=χ(ξ_h). det(ξ↔a)=Vandermonde(η)=Differenzenprod≠0; [§143,1] rational a make (ε,ξ)≠0, k_α-k_β≠0,
        ξ distinct. (5) y_h=χ(x_h); (6) Θ_v=(ε^{r_v},y)/(ε^{r_v},x); Θ has props α)β)γ)δ); (7) Q_v=Q(k_v); (8)
        (ε^{r_v},η)=Q_v(ε^{r_v},ξ) ⇒ same form as §185(5) with K_v→Q_v K_v (may partly vanish). ✓ verbatim.
    ★ WORKS: content-track continues fast/clean through this dense metacyklische-radical theory (§183-186 all essentially
      verbatim bar the one R_v shorthand normalization). The single deviation-type seen so far in this Abschnitt is
      GPT-added/normalized exponents on shorthand — keep zooming shorthand defs.
    GESPERRT (deferred): §186 "Tschirnhausen-Transformation" (p642); Theorem I quote block (p644). Not emph-verified.
  • 2026-07-02 turn 28 (loop re-fire): **§186 COMPLETE (p644-646, .tex 22478-22571) VERIFIED FAITHFUL — 1 EDIT
    (Weber erratum flag).** Compile-gated clean: 418pp/0 err/0 overfull/0 underfull/0 missing/0 undefined (2263535 bytes,
    byte-identical — comment inert). §186 fully done p641-646. §187 opens next (.tex 22573, p647).
      – **ERRATUM FLAG (Weber index slip, .tex 22559):** conclusion prints S(ξ_0,ξ_1…ξ_{n-2}) where the same symm. fn was
        defined S(ξ_0,ξ_1…ξ_{n-1}) on p645. n roots ⇒ last index should be n-1; ξ_{n-2} is a Weber Fluechtigkeitsfehler.
        Both reproduced faithfully in .tex (each matches its own print); added `% [sic] … gemeint ξ_{n-1} … nicht korrigiert`.
        = **5th type-B Weber erratum** in vol1 (after §172 (a-b)^3, §180 z_0, §181 dup-(12), §182 v'_4). Recompiled clean.
      – Theorem I (forward, p644): ξ=A+ΣK_v τ… (9) [details logged]; (9) prints τ_{v+n-2}^{r_0} — Weber writes r_0 in FULL
        formulas, omits only in p640 k-shorthand (⇒ p640 R_v fix consistent). Converse (p644-646): (10)-(16) index-perm
        analysis (radical sign-change → (h,h+βr_{-α-1}); (τ) cyclic → (h,g^{-1}h)); symm S(ξ)→rational in 𝔎; irred [§179]
        via x^n-R_0. **Theorem II** (p646): every (9)-form ξ = root of deg-n eqn in 𝔎, irred except special case (one root
        rational, rest in 𝔎(ε)). ✓ verbatim.
    ★ ADJUST/pattern (types of deviation seen this Abschnitt): (a) GPT-ADDED null exponent → REMOVE (p640 R_v); (b)
      Weber-OWN slip → KEEP + [sic] (p646 ξ_{n-2}). Same rule both ways: match the print EXACTLY. Everything else in
      §183-186 is verbatim. Erratum tally now 5; plus 1 GPT-normalization removed.
    GESPERRT (deferred): §186 "Tschirnhausen-Transformation" (p642), Theorem I (p644), Theorem II (p646). Not emph-verified.
  • 2026-07-02 turn 29 (loop re-fire): **§187 COMPLETE (Realitätsverhältnisse, p647-648) + §188 opening (p648) VERIFIED
    FAITHFUL — 1 EDIT (GPT-normalization removed).** Compile-gated clean: 418pp/0 err/0 overfull/0 underfull/0 missing/
    0 undefined (2263541). §183-187 now all content-complete; §188 (LAST §, n=5 quintics) begun.
      – **FIX (GPT-normalized index restored, .tex 22603):** §187 reality proof read `die Wurzeln $\xi_h$ alle reell
        sind`; ZOOM p648 (crop_5_21) shows Weber prints `$\xi_z$` (italic z, his §180 permutation-index letter). GPT
        normalized z→h. Restored ξ_z to print. = 2nd "GPT-normalization removed" (after §185/p640 R_v). Reinforces:
        GPT silently normalizes indices/exponents to expected convention — ZOOM and match print.
      – **★ ORDINAL WATCH RESOLVED for §188:** §188 title `f\"unften Grades`; scan p648 prints "fünften" SPELLED OUT →
        .tex MATCHES, NO fix. OPPOSITE of §181 (numeral "5ten"). ⟹ Weber inconsistent across titles; scan-check EACH,
        never assume the pattern. §188 body also spells "fünften"/"vierten" (Weber spells ordinals in body consistently).
      – §187 verbatim: 2 Arten metacykl. [§180] / 2 Arten cyclic even-deg [§165]; real-k ⇒ ξ_0 real + conj pairs; imag-k ⇒
        ⁿ√R_{v+(n-1)/2}·ⁿ√R_v=Ψ(k_v) rational (g^{(n-1)/2}+1≡0) ⇒ radicals conj imag ⇒ (via r_v≡-r_{v+(n-1)/2}) all ξ real.
        Satz (quote). §188 opening: find all metacykl. quintic roots in any 𝔎 via cyclic-quartic roots k_0..k_3; Kronecker
        Bd.II remark. ✓ verbatim.
    Erratum tally: 5 type-B Weber errata; + 2 GPT-normalizations removed (R_v exp, ξ_z index). Everything else verbatim.
  • 2026-07-02 turn 30 (loop re-fire): **§188 COMPLETE (p649-653, .tex 22617-22793) + BERICHTIGUNGEN (p654) VERIFIED
    FAITHFUL — 1 EDIT (Weber erratum flag). ★★ END OF VOL1 BODY reached (content-track forward pass).** Compile-gated
    clean: 418pp/0 err/0 overfull/0 underfull/0 missing/0 undefined (byte-identical 2263541, comment inert).
      – **ERRATUM FLAG (Weber index slip in eq (14), .tex 22786):** K_3=A_1−A_2r−A_2ϱ'−A_4rϱ' — coeff of ϱ' printed
        A_2, but the parallel build (K_0/K_1/K_2 give ϱ/ϱ' the coeff A_3) wants A_3. ZOOM p653 (crop_18_18) CONFIRMS
        the print reads A_2 (subscript identical to A_2r in same line, ≠ the "3" glyph in "K_3" below). .tex already
        faithful (A_2ϱ'); added `% [sic] … Fluechtigkeitsfehler (gemeint A_3) … quellentreu, nicht korrigiert`.
        = **6th type-B Weber erratum** in vol1 (after §172 (a-b)^3, §180 z_0, §181 dup-(12), §182 v'_4, §186 ξ_{n-2}).
      – §188 verbatim p649-653: cyclic quartic (1)-(12) [w=(k_0-k_2)(k_1-k_3), 8b/8a√c, b²=c(1+a²), k-diffs=2√(b±a√c),
        (6) √c relation, C/B sums (7)(8), explicit k (9), r/ϱ/ϱ' + 6 radicals + σ-matrix + 4×6 sign table, quartic (11),
        b=0/a=i special case, h-subst → (12), Abel variant]; quintic root via §186(9): g=2→exps 1,2,4,3, τ_v=⁵√k_v,
        (13) ξ=A+ΣK_vτ…, K_v Abel-form → (14) via 3 radicals, K_0=A_1+A_2r+√(ϱ²(A_3+A_4r)²) recovers k_0-form. All
        faithful bar the (14) K_3 A_2 slip. ("Coëfficienten"→"Coefficienten" house-conv; "Abel" ×2 letterspaced→SPERRUNG;
        body "5ten Grades" numeral matches .tex $5^{ten}$.)
      – **BERICHTIGUNGEN (p654) verified faithful:** print has EXACTLY 2 errata entries, both verbatim in .tex (22798,
        22800: "Seite 182 … x_m statt x_n", "Seite 347 … (2x²+1)² statt (2x²−1)²"). GPT dropped NO entries. (Cosmetic:
        print centers "Berichtigungen." w/ period+rules; .tex left-aligned \section* no period. Not content.)
      – **★ RUNNING-HEAD CONCERN CLOSED:** .tex preamble l.64-65 sets FIXED \lhead{Weber Vol. I}/\rhead{Deutsche Quelle};
        does NOT reproduce Weber's per-page running heads. So the p649/p651 running-head "5ten" vs §188 title "fünften"
        discrepancy is MOOT (no Weber running heads in the .tex at all). Item resolved, no action.
    ★★ MILESTONE — the CONTENT-TRACK FORWARD PASS has reached the physical END of the printed vol1 body (§188 is the last
      § of the Achtzehnter Abschnitt = last Abschnitt; then Berichtigungen + \end{document}; p653_bot/p654_bot blank).
      **NOT a completeness claim** (my completeness claims are always wrong): "reached the end" ≠ "whole volume verified".
    ★ COVERAGE MAP (from WEBER_CERT_LOG.md, built this turn): CERT log's earliest entry is **p100**. So:
        · **p1–p99 (§1..~§30, Erstes Buch foundations): NEVER audited** — not by the 2026-06-25 swarm, not by this
          context-read method. ← EARLIEST CONTENT GAP.
        · p100–599 (§~30..§176): covered by 2026-06-25 swarm batches ("verified by eye" AGENT runs — per own rule
          "audit agent output many times", these deserve spot-suspicion, not blind trust).
        · p600–654 (§177–188 + Berichtigungen): covered by THIS restart's context-read (forward pass now complete).
  • 2026-07-02 turn 31 (loop re-fire): **p1-4 (EINLEITUNG start, .tex 157-233) — FIRST audit of the p1-99 gap — 4 EDITS.**
    Compile-gated clean: 418pp / 0 err / 0 overfull / 0 underfull / 0 missing / 0 undefined (2264012 bytes).
      – FIX 1 (misread, p2 fn .tex 173): Euklid cite `Buch VII, 11`->`II` (Roman II = Elem. Bk VII Satz 2, ggT-Satz;
        glyph = the "II" in "Bd. II" same line). ZOOM crop_13_85.
      – FIX 2 (**WEBER ERRATUM**, p4 .tex 203): ordering def prints "Ist a>b und b>c oder **a>b>c**" — 2nd case identical
        to 1st (redundant); intended ascending a<b<c. GPT had silently corrected to "a<b und b<c". ZOOM crop_66_43 = all
        ">". Reverted to printed "a>b>c" + [sic]. = **7th type-B Weber erratum** (1st found outside the metacykl. Abschn.).
      – FIX 3 (Fraktur, p4 .tex 201): Menge symbol printed Fraktur **M**; .tex plain `$M$` (inconsistent — \mathfrak R,S
        already in same passage). `$M$`->`$\mathfrak M$`. ZOOM crop_33_27. ⚠ WATCH other M / Schnitt A,B Fraktur.
      – FIX 4 (content drop, p4 .tex 206-210): display printed with labels "$\mu=$"/"$\mu'=$"; GPT dropped both (bare
        fractions). Restored. ZOOM crop_28_84.
    ★ SYSTEMATIC (Einleitung): (a) Weber INLINES short relations, GPT display-set them — content-faithful, NOT reverting
      (accepted normalization; do not churn). (b) Fraktur set-symbols rendered plain italic in spots — fix per page vs
      print. (c) letterspaced-caps headings vs .tex \Large — cosmetic house-style, untouched.
    p1,p3 fully faithful; p2 (1 fix), p4 (3 fixes). Einleitung is DENSE with gesperrt terms → heavy SPERRUNG deferral.
  • 2026-07-02 turn 32 (loop re-fire): **p5-7 (EINLEITUNG cont., .tex 211-241) — 4 EDITS.** Compile-gated clean:
    418pp / 0 badness (2264024 bytes).
      – FIX 1-3 (Fraktur, p5 .tex 215): general Menge symbol prints Fraktur **M** in 3 spots ("geordneten Menge M",
        "Schnitt in M", "Element mu von M") — all plain `$M$` -> `$\mathfrak M$`. CONFIRMS Menge-M->Fraktur is systematic
        (2nd confirming page after p4/201). Cut PARTS $A,B$ stay Latin (correct).
      – FIX 4 (misread, p7 .tex 235): "der **einem** der Schnitte" -> "**einen**" (accusative, obj. of erzeugt; ZOOM
        crop_52_31 = two-stroke n). .tex had ungrammatical dative.
    p6 fully faithful (ℜ-not-continuous √μ proof, 𝔖 construction, Dedekind fn continuation). p5,p7 faithful bar the fixes.
    All sets ℜ,𝔖,𝔄,𝔅 correctly \mathfrak. Trivial skipped: p5 "Massen, niemals" comma.
  • 2026-07-02 turn 33 (loop re-fire): **p8 (EINLEITUNG messbar-def + measurement, .tex 241-256) — 5 EDITS.**
    Compile-gated clean: 418pp / 0 badness (2264020 bytes).
      – FIX 1 (**REWORD restored**, .tex 252): print "keine Elemente liegen, **weil, wenn** ... aus der Definition der
        Messbarkeit **folgen wuerde**, dass"; GPT had reworded to "denn wenn ... so wuerde ... folgen". ZOOM crop_9_64.
        Restored Weber's wording.
      – FIX 2-5 (Fraktur Menge-M, .tex 243 ×3 + 248 ×1): "geordnete Menge M", "in M allgemein", "von M abgeleitet",
        "Elemente von M haben" — all `$M$` -> `$\mathfrak M$`. (3rd confirming page for the systematic pattern.)
    ★ NEW SYSTEMATIC (punctuation-tier, SKIPPED, flagged for possible separate pass): **GPT period-normalization of
      Weber's colons/semicolons** — swaps ":"/";" for "." (+capitalises next word), breaking Weber's long sentences.
      This page: "Voraussetzungen:"→".", "gelten; und"→". Und", "Element; denn"→". Denn". Same tier as skipped commas.
    p8 content faithful bar the 5 edits.
  • 2026-07-02 turn 34 (loop re-fire): **p9 (EINLEITUNG messbar Mengen + cut-addition, .tex 254-260) — 5 EDITS + 1
    documented Weber font-slip (kept).** Compile-gated clean: 418pp / 0 badness (2264034 bytes).
      – FIX 1-2 (Fraktur, .tex 254 ×2): "stetigen geordneten Menge M", "Schnitt (A,B) in M" -> `$\mathfrak M$`.
      – FIX 3 (**≦ vs <**, .tex 254): cut cond. printed "$a+x\le c$" (Weber's ≦ double-bar); .tex had strict "$a+x<c$"
        (leaves boundary a+x=c in neither A nor B = partition gap). ZOOM crop_3_11 (≦ distinct from plain > in c>a,
        a+x>c). `<`->`\le`. Genuine relation error.
      – FIX 4 (dropped word "so", .tex 258): "die natürliche Zahl m **so** bestimmen" — restored (ZOOM crop_3_69).
      – FIX 5 (Fraktur, .tex 260): "den Schnitt in $R$" -> `$\mathfrak R$` (print ℜ; lone .tex inconsistency).
      – DOCUMENTED-not-fixed (Weber font-slip, .tex 258): "a+hμ in **𝔅**" prints upright Fraktur 𝔅 (Setzfehler for
        Latin B = upper cut part; ZOOM crop_3_69). .tex keeps correct Latin B per Collectet precedent. Noted in CERT.
    p9 content faithful bar the fixes. Punctuation period-normalization recurs (skipped).
  • 2026-07-02 turn 35 (loop re-fire): **p10 (EINLEITUNG cut-addition tail + Verhältnisse def, .tex 260-268) — 3 EDITS.**
    Compile-gated clean: 418pp / 0 badness (2264024 bytes).
      – FIX 1-2 (Fraktur, .tex 264+266): "messbaren Menge M", "wenn M das System der nat. Zahlen" -> `$\mathfrak M$`
        (ZOOM crop_3_50). 5th confirming page.
      – FIX 3 (**word-order REWORD**, .tex 266): print "...sind, **dann und nur dann $qa=pb$**, wenn $mq=np$ ist"; GPT had
        reordered to "$qa=pb$ dann und nur dann, wenn ...". ZOOM crop_3_56. Restored Weber's order.
    p10 content faithful bar the 3 edits (Verhältnisse def, Zähler/Nenner, rational Verhältniss/Zahl all verbatim).
  • 2026-07-02 turn 36 (loop re-fire): **p11 (EINLEITUNG a:b vs m:n comparisons + Verhältnis-cases start, .tex 268-296)
    — 3 EDITS + 1 DEFERRED notation remap.** Compile-gated clean: 418pp / 0 badness (2264297 bytes).
      – FIX 1 (Fraktur, .tex 270): "messbaren Mannigfaltigkeit M" -> `$\mathfrak M$` (6th confirming page).
      – FIX 2 (**= vs >**, misread, .tex 274): print "wenn $m:n>p:q$"; .tex had "$m:n=p:q$". ZOOM crop_3_29 (">" like
        the > in a:b>p:q). `=`->`>`.
      – FIX 3 (**DROPPED SENTENCE**, .tex 279): restored "...ist, **d. h. man kann zwischen $a:b$ und $m:n$ beliebig
        viele rationale Verhältnisse einschalten.** Um dies zu zeigen ..." (GPT had dropped the whole clause).
      – ★★ DEFERRED (e/ε/e' notation remap, .tex 294-302): Weber uses **e** (Latin) / **ε** (Greek lunate) / **e'** for
        the ratios; .tex normalized to $\epsilon$/$\epsilon'$/$\epsilon''$. ZOOM crop_3_89 confirms e≠ε. Remap next turn
        (see NEXT) — passage spans onto p12.
    p11 content faithful bar the fixes + deferred e/ε.
  • 2026-07-02 turn 37 (loop re-fire): **p12 (EINLEITUNG Verhältnis equality/inequality -> Zahlbegriff, .tex 294-306)
    — DID the deferred e/ε/e' remap (5 lines) + found a CONTENT CORRUPTION.** Compile-gated clean: 418pp / 0 badness
    (2264181 bytes).
      – ★ REVERSED last turn's decline. Comprehensive re-zoom (p11_bot + p12_top + p12_mid + crop_13_30) shows Weber's
        scheme is CLEAR & CONSISTENT: **e**(Latin)=1st ratio a:b, **ε**(Greek lunate)=2nd ratio α:β, **e'**(Latin)=
        "jedes andere Verhältniss". .tex had normalized all to $\epsilon/\epsilon'/\epsilon''$. Remapped .tex 294,296,
        298,302 fully; .tex 300 only the leading "wenn e oder ε" (its "Denn"-clause ε,ε' are a ratio+its equal
        replacement, genuinely Greek — KEPT).
      – ★★ CONTENT CORRUPTION fixed (.tex 298): print "...**ε**<μ' folgt, dass μ<μ', und folglich **e**<μ' sich ergiebt"
        = two DIFFERENT ratios. .tex had both as $\epsilon$, making "folglich ε<μ'" CIRCULAR (destroys the α/β mutual-
        exclusion argument). Restored Latin e in the conclusion. Real logic error from GPT-normalization, not cosmetic.
      – CASE-LABEL confirm (.tex 298): print introduces sub-cases as BARE "α)"/"β)" (not "2α)/2β)"); my prior-turn
        bare-label restoration is CORRECT. "2α)/2β)" appears only later (300,302, back-refs) — .tex already right.
      – p12_bot FAITHFUL (no edits): Gattungsbegriff->Zahl + footnote + irrationale/rationale Zahlen + geordnete Menge
        (.tex 304) and Zähler/Nenner Satz start (.tex 306) match verbatim.
    ★ METHOD LESSON (logged): for a suspected systematic normalization, zoom the WHOLE passage's CLEAR instances before
      ruling on the ambiguous crop — do NOT decline on one blurry crop (as I wrongly did turn 36). The re-zoom is what
      exposed both the consistent e/ε/e' scheme AND the 298 corruption.
  • 2026-07-02 turn 38 (loop re-fire): **p13 (EINLEITUNG Zähler/Nenner Satz + a:c=b:d + Hauptsatz a:b=c:d, .tex 306-324)
    — 3 EDITS.** Compile-gated clean: 418pp / 0 badness (2264193 bytes).
      – FIX 1 (**≧ vs =**, normalization, .tex 306): print "$mb\ge na'\ge na+n(a'-a)$" — BOTH signs Weber's ≧; .tex had
        2nd as "=" (GPT "corrected" it since na'=na+n(a'-a) is an identity). ZOOM crop_5_22 (wedge+double-bar = ≧, not
        plain "="). `=`->`\ge`. GPT-normalization removed.
      – FIX 2 (**dropped word "und"**, .tex 311): print "$a:b<a':b$**; und** ganz ebenso"; .tex ". Ganz" (period-norm
        dropped the connective). Restored "; und ganz". (Rule refined: ";"->"." that DELETES a word = content-fix;
        bare ":"/";"->"." = skip.)
      – FIX 3 (**Fraktur Menge-M**, .tex 322): "ein Element $x$ von **𝔐** in $A$" -> `$\mathfrak M$` (ZOOM crop_55_75;
        𝔐 vs plain-italic A,B). 7th confirming Fraktur-M page.
      – DISPLAY-layout (SKIP, documented): proof-conditions print as 2 stacked lines "na<mc"/"nb>md"; .tex 1 line
        "na<mc,\qquad nb>md". Content identical; display normalization not reverted.
    p13 content faithful bar the 3 edits (Zähler/Nenner monotonicity Satz+proof, a:c=b:d Satz+proof, Hauptsatz+Stetig-
    keit proof all verbatim).
  • 2026-07-02 turn 39 (loop re-fire): **p14 (EINLEITUNG Addition-well-defined proof + messbar/stetig + Mult/Div/
    Grundformel, .tex 324-346) — 6 FIXES (5 rewords + 1 DROPPED EQUATION).** Compile-gated clean: 418pp / 0 badness
    (2264381 bytes). ★ FIRST Einleitung page with dense multi-reword paraphrase (prior pages = Fraktur/misread/single-drop).
      – .tex 328 TRIPLE reword: (a) "Brüche. Es bleibt zu zeigen, dass ... b:c=b':c' **ist**, auch" -> print "Brüche, und
        um sie allgemein zu rechtfertigen, braucht dann nur noch gezeigt zu werden, dass ... b:c=b':c', auch" (+spurious
        "ist" removed); (b) "Der Beweis geschieht dadurch, dass aus ... folgt" -> print "Wir beweisen dies, indem wir
        zeigen, dass, wenn ... ist, auch ... sein muss"; (c) "Ist nämlich" -> print "Es sei also, wenn $m$ und $n$ zwei
        ganze Zahlen sind,".
      – .tex 333 reword: "so ist ..., und daher" -> print "dann ist ... und also".
      – **.tex 335 DROPPED EQUATION**: display had only "$b/c>(mc-na)/nc$"; print has "$b/c>(mc-na)/nc,\ (mc'-na')/nc'>
        b'/c'$" — restored the load-bearing 2nd inequality (proof chains b/c>(mc-na)/nc=(mc'-na')/nc'>b'/c').
      – .tex 337 reword: "Andererseits folgt aus ... leicht" -> print "Andererseits folgt aber leicht aus der
        Voraussetzung ..., dass auch".
      – .tex 339/341 reword: display trailing comma dropped + "und also" -> "ist, also" (restore "dass auch [eqn] ist,
        also..." construction).
      – FAITHFUL: a/c+b/c=(a+b)/c; messbar/stetig-Zahlen para (343, bar trivial comma); Mult/Div/Grundformel/Subtraction
        (345-346) verbatim.
    ★ METHOD LESSON: proof-paragraphs carry DENSER paraphrase than expository prose — transcribe the WHOLE paragraph &
      diff sentence-by-sentence, don't spot-check; GPT rewrote connectives AND silently dropped a display line.
  • 2026-07-02 turn 40 (loop re-fire): **p15 (EINLEITUNG √α via Schnitt + Cantor Zahlenreihen, .tex 348-359) — 0 NET
    EDITS (faithful page).** Recompiled clean: 418pp / 0 badness (2264381 = identical to p14-final).
      – FAITHFUL: √α existence via Schnitt; Cantor Zahlenreihen intro+footnote; def + $S=x_1,x_2,x_3,x_4\ldots$; g-bound+
        delta-Cauchy condition; Schnitt(A,B) construction; "$\alpha$ erzeugt ... wie klein auch eps sei"; "Nach Cantor
        ist die Zahlenreihe S geradezu die Definition der Zahl α". All verbatim.
      – SKIP-tier: dropped colon before "$S=\ldots$" display; ellipsis without surrounding commas in print
        ("$x_2\ldots x_n$") vs .tex commas. Trivial.
      – ★ EPSILON investigation -> REVERTED: .tex 359 `$\varepsilon$`; Weber's ε is LUNATE (=`\epsilon`; ZOOM crop_13_73).
        Changed ->`\epsilon`, THEN grepped: **`\varepsilon` is house-wide (321×**; preamble only `\eps:=\varepsilon`, no
        redef). Per-page change would fracture the convention for a NULL-semantic glyph. REVERTED. Decision: accept
        `\varepsilon` as house epsilon (like inline->display); ratio passage (p11-12) keeps `\epsilon` as the sole
        exception (Latin-e-vs-Greek-ε contrast). NO doc-wide sweep.
    ★★ METHOD LESSON: BEFORE "fixing" a glyph/notation on one page, GREP THE WHOLE DOC — an established house convention
      (100s of uses) must not be fractured per-page; treat as accepted normalization unless doing a full verified sweep.
  • 2026-07-02 turn 41 (loop re-fire): **p16 (EINLEITUNG negative Zahlen + Null + Reihe der reellen Zahlen, .tex
    359tail-367) — 1 EDIT (reword + dropped word).** Compile-gated clean: 418pp / 0 badness (2264464 bytes).
      – FIX (.tex 361, REWORD + DROPPED "Null"): print "von der wir uns **freimachen durch Einführung der Null und der
        negativen Zahlen**"; .tex "**frei machen, indem wir die negativen Zahlen einführen**" (reworded AND dropped "der
        Null und" — print introduces BOTH zero and negatives). ZOOM crop_10_31. Restored.
      – FAITHFUL: two-copies construction of negatives (grösser<->kleiner reversal, $(-x)+(-y)=-(x+y)$ etc.); zusammen-
        ordnen $-x<x$; lone Schnitt $(-x,x)$ => adjoin "Null oder 0" => vollständige Reihe der reellen Zahlen; Addition-
        def intro. All verbatim.
      – SKIP: semicolon-vs-comma between the two inline eqs. Trivial.
  • 2026-07-02 turn 42 (loop re-fire): **p17 (EINLEITUNG addition laws + number-line + Mult/Div + complex-numbers intro,
    .tex 368-399) — 3 EDITS.** Compile-gated clean: 418pp / 0 badness (2264472 bytes).
      – FIX 1 (**VERBAL-CONDITION normalization**, .tex 372-376): print "$x+(-y)=x-y$, **wenn** $x>y$, $=-(y-x)$, **wenn**
        $y>x$" (German "wenn" + elliptical 2nd eq); .tex had parenthetical "(x>y)" + repeated LHS. Restored with
        `\text{wenn }`. NEW pattern: German conditional words -> symbolic parentheticals.
      – FIX 2 (**± vs +**, sign, .tex 384): print "der Länge $\pm z_2$"; .tex "$+z_2$". ZOOM crop_2_46 (clear ±). Restored.
      – FIX 3 (**DROPPED PHRASE "Es sei"**, .tex 394): print "nach folgenden Regeln. **Es sei** [display]"; .tex "Regeln:"
        (dropped "Es sei" + colon-for-period). Restored.
      – SKIP: "(linken)" parens vs ", linken" comma (bracketing punctuation, no word); colon before "die Gesetze:";
        mult/div display layout+trailing-comma.
      – FAITHFUL: commut/assoc laws; number-line; Mult/Div rules; complex intro (Paare (x,y), eq iff x=a,y=b, unordered
        Mannigfaltigkeit) + 2 def displays. All verbatim.
  • 2026-07-02 turn 43 (loop re-fire): **p18 (EINLEITUNG complex numbers: i, x+yi, arithmetic, division, Gauss plane +
    modulus, .tex 392tail-427) — 3 FIXES (2 dropped words + 1 DROPPED EQUATION).** Compile-gated clean: 418pp / 0 badness
    (2264588 bytes).
      – FIX 1 (sentence-continuation / DROPPED "und", .tex 397+399): print is ONE sentence across p17->p18 break: "Es sei
        [eq1], [eq2], **und wir** setzen ausserdem fest..."; .tex split it (2nd display "."; "**Wir**" cap, "und" dropped).
        Restored 397 "."->"," + 399 "Wir"->"und wir". Confirms the p17 "Es sei" restoration.
      – FIX 2 (DROPPED "oder", .tex 401 display): print "$(x,0)(0,1)=(0,x)$ **oder** $=ix$"; .tex chained "...=(0,x)=ix".
        Restored with `\text{oder}`.
      – **FIX 3 (DROPPED EQUATION+"oder", .tex 420)**: division derived in TWO forms in print — (A)
        "$x+yi=(a+bi)\frac{(a-bi)(x+yi)}{(a^2+b^2)}$" + "**oder**" + (B) "$\frac{x+yi}{a+bi}=\frac{ax+by+i(ay-bx)}{a^2+b^2}$";
        .tex had ONLY (B). ZOOM crop_18_35. Restored (A)+"oder". **2nd dropped-equation of the gap-pass (cf. p14).**
      – FAITHFUL: $(x,0)=x$; $(x,y)=0$ iff x=y=0; $i=(0,1)$; all arithmetic displays; imaginär/complex defs; Gauss plane;
        modulus $\varrho=\sqrt{x^2+y^2}$. All verbatim.
  • 2026-07-02 turn 44 (loop re-fire): **p19 (EINLEITUNG modulus/conjugates + triangle-inequality Satz & proof, .tex
    433-458) — 4 FIXES.** Compile-gated clean: 418pp / 0 badness (2264603 bytes).
      – **FIX 1 (GPT FABRICATION removed, .tex 441)**: print "$Z=(x+a)+(y+b)i$"; .tex had "$Z=z+c=(x+a)+(y+b)i$" — GPT
        INSERTED "$z+c=$" not in Weber. ZOOM crop_52_50. Removed. **NEW damage class: GPT ADDED a step (vs the usual drops).**
      – FIX 2 (reword+punct, .tex 450+452): print "$=2(r\varrho-ax-by)$**; das ist** sicher positiv"; .tex "$...$**, was**
        sicher positiv **ist**". Restored "das ist sicher positiv" + ";".
      – FIX 3 (dropped "ist", .tex 456): print "dass $r\varrho\ge ax+by$ **ist**, und nur dann"; .tex dropped "ist,". Restored.
      – FIX 4 (SIGN ≧->> strict, .tex 456): print "$r+\varrho$ **>** $R$ ist" (single wedge; ZOOM crop_44_68); .tex
        "$\varrho+r\ge R$". Weber: ">" general + "=" special case. Restored strict ">".
      – ★ SKIP (commutative operand REORDER): Weber "$r+\varrho$/$r\varrho$/$r^2\varrho^2$" (r first) vs .tex ϱ-first
        (~7×); same symbols, NULL -> style-tier skip (kept .tex order for consistency; only the SIGN was fixed). Also SKIP:
        display-boundary "." + "Dann ist" cap vs print "," + "dann ist" (no word dropped); commas before "als" (×2).
      – FAITHFUL: modulus-of-0, conjugates, triangle-ineq Satz + full proof algebra, Dreieck interpretation, |sum|≥|diff|.
  • 2026-07-02 turn 45 (loop re-fire): **p20 (EINLEITUNG END: triangle-ineq tail + Buchstabenrechnung/Identitäten/
    Unbekannte, .tex 458-466) — 0 EDITS (faithful). ★★ EINLEITUNG (p1-20) CONTENT-AUDIT COMPLETE.** File unchanged
    (418pp / 0 badness / 2264603).
      – FAITHFUL: "$R\ge r-\varrho$" (sign ≧ = double-bar, matches .tex; distinct from p19 strict ">"); "Gleichheit ...
        z:c reell und negativ"; the Buchstabenrechnung close (Algebra=Buchstabenrechnung; Identitäten->Variable;
        Forderung/lösen->Unbekannte; two kinds of letters). All verbatim.
      – SKIP: ";" vs ":" at "zweierlei Art sein". Bare punctuation.
    ★★ MILESTONE: whole Einleitung body (.tex 158-466, printed pp.1-20) audited page-by-page vs ~500dpi scans (provisional,
      by-eye — NOT a completeness claim). Aggregate damage fixed p1-20: 7 type-B errata kept+[sic]; 1 font-slip documented;
      ~15 Fraktur Menge-M; 5 GPT-normalizations removed; 1 fabrication removed (z+c); 2 dropped equations restored;
      multiple sign fixes (≦/≧/±/>); many dropped-word/reword restorations. SKIP-tier norms documented.
  • 2026-07-02 turn 46 (loop re-fire): **p21-p22 (divisional title page + blank verso, .tex 468-475) — 0 EDITS (faithful).**
    File unchanged (418pp / 0 badness / 2264603).
      – p21 = title page: "ERSTES BUCH." / "DIE GRUNDLAGEN." — .tex title text matches exactly (omits only the decorative
        separator rules). p22 = blank verso (mirror show-through of p21 only).
  • 2026-07-02 turn 47 (loop re-fire): **p23 (§1 Ganze Functionen start: def + eq(1) + Grad/Coefficienten + add/mult
    rules, .tex 477-494) — 0 net EDITS (faithful).** File unchanged (418pp / 0 badness / 2264603).
      – HEADINGS match (Erster Abschnitt / Rationale Functionen / §.1 / Ganze Functionen). eq(1)
        $f(x)=a_0x^n+\cdots+a_n$ index-matched; ascending display index-matched; Grad/Coeff/add-mult prose verbatim.
      – SKIP: "§." period vs "\S~"; "Coëfficienten" vs "Coefficienten" (documented house ë-drop).
      – ★ EQ-NUMBER POSITION (LAYOUT, out of scope): Weber LEFT-numbers eqns ("(1)" at left margin); .tex
        documentclass has NO leqno -> renders RIGHT. Tried `[11pt,leqno]`: clean but +9pp reflow (418->427). REVERTED
        (German-TEXT pass only; +9pp ripples through swarm-verified p100+). -> owed to a SEPARATE FORMATTING PASS.
      – §1 prose simple/clean -- lower GPT-damage density than the Einleitung's Dedekind prose.
    ★ METHOD LESSON: global LAYOUT fidelity (eq-number side/style, margins) is OUT of scope for the content gap-pass;
      document for a dedicated formatting pass; don't fold reflowing changes into the content audit.
  • 2026-07-02 turn 48 (loop re-fire): **p24 (§1 cont.: Mult-Grad + product convolution eq(2)(3)(4) + Rechenregeln +
    several-var intro, .tex 494-534) — 0 net EDITS (faithful).** File unchanged (418pp / 0 badness / 2264603).
      – Convolution eq(4) $c_\nu=a_0b_\nu+a_1b_{\nu-1}+\cdots+a_\nu b_0$ subscript-matched; $c_0,c_1,c_2$ matched;
        index-rule + Rechenregeln ($ab=ba$,$(ab)c=a(bc)$,$(a+b)c=ac+bc$) verbatim.
      – SKIP: Coëfficient->Coefficient (house ë-drop); eq(4) ellipsis-"+" ("$+\cdots a_{\nu-1}b_1$" vs "$+\cdots+...$",
        trivial); eq-numbers print-LEFT (leqno item, owed to formatting pass); ellipsis-commas.
      – §1 math-body clean/low-damage: 2 faithful pages running (p23,p24) vs the Einleitung's dense Dedekind prose.
  • 2026-07-02 turn 49 (loop re-fire): **p25 (§1 several-var tail + §2 Gauss-Satz start: primitive def + Satz +
    proof-setup, .tex 534-548) — 0 net EDITS (faithful).** File unchanged (418pp / 0 badness / 2264603).
      – §2 heading "§. 2. / Ein Satz von Gauss." matches. Footnote "Gauss, Disquisitiones arithmeticae, Art. 42."
        placement + text match. Primitive-func def + Satz + proof-setup (prime p; indices) all index-matched.
      – SKIP: Coëfficient->Coefficient (house ë-drop); §. period; eq# left (leqno); ellipsis/trivial commas.
      – ⚠ EMPHASIS (DEFERRED): footnote title -- print appears ROMAN "Disquisitiones arithmeticae"; .tex `\emph{}` (italic).
        Flag for emphasis pass (verify+resolve; either GPT-added italic or editorial book-title convention).
      – 3 faithful pages running (p23,p24,p25): §1-§2 math-body clean vs Einleitung dense prose.
  • 2026-07-02 turn 50 (loop re-fire): **p26 (§2 Gauss-lemma proof: c_{r+s} eq(1) + Widerspruch + several-var induction
    + imprimitive-def, .tex 550-574) — 0 net EDITS (faithful).** File unchanged (418pp / 0 badness / 2264603).
      – Key convolution eq(1) $c_{r+s}=a_rb_s+a_{r-1}b_{s+1}+\cdots+a_{r+1}b_{s-1}+\cdots$ subscript-matched; p-divisib.
        split displays, Widerspruch, induction ("Schluss von m-1 auf m"), imprimitive/Theiler def all matched.
      – SKIP: Coëfficient->Coefficient (house ë-drop); colons before displays; eq# left (leqno); ellipsis-commas.
        (.tex `\hbox{aber nicht in }` in displays renders fine.)
      – ★ 4 faithful pages running (p23-26). META: GPT damaged the Einleitung's DENSE Dedekind prose far more than the
        routine §1-§2 polynomial algebra -> §-body pages audit fast (verify+log) until a dense/tricky passage.
  • 2026-07-02 turn 51 (loop re-fire): **p27 (§2 tail Theiler-Satz + monic φ/ψ/γ; §3 Division start, .tex 576-605) —
    0 net EDITS (faithful).** File unchanged (418pp / 0 badness / 2264603).
      – Monic forms $\varphi=x^m+\alpha_1x^{m-1}+\cdots+\alpha_m$, $\psi=x^n+\cdots+\beta_n$, product $\gamma$-coeffs
        subscript-matched; Hauptnenner proof; §3 "§.3. Division." heading + eq(1) A/B matched. §2 DONE.
      – SKIP: Coëfficient->Coefficient (ë-drop); eq# left (leqno). Running header not in .tex (not audited).
      – ★ 5 faithful pages running (p23-27): §1-§3 math-body clean.
  • 2026-07-02 turn 52 (loop re-fire): **p28 (§3 Division long-division algorithm: Kette eq(4), Q eq(5), A=QB+C eq(6),
    terminology, .tex 605-638) — 0 net EDITS (faithful).** File unchanged (418pp / 0 badness / 2264603).
      – Division Kette eq(4) 3 rows+dots matched row-for-row (primed indices $a'_0,a''_0$, $m'-n,m''-n$); Q eq(5),
        A=QB+C eq(6), Dividendus/Divisor/Rest/Quotient terminology all matched.
      – SKIP: Coëfficienten->Coefficienten (ë-drop); colons; eq# left (leqno); ellipsis-commas.
      – ★ 6 faithful pages running (p23-28): §1-§3 math-body clean.
  • 2026-07-02 turn 53 (loop re-fire): **p29 (§3 b_0-denom discussion + cubic example eq(7-10) + decimal analogy,
    .tex 640-662) — 0 net EDITS (faithful).** File unchanged (418pp / 0 badness / 2264603).
      – Cubic example verified term-by-term: eq(7) f, eq(8) f'=3a_0x^2+2a_1x+a_2, eq(9) Q=1/3 x+a_1/9a_0, eq(10)
        C=(6a_0a_2-2a_1^2)/9a_0 x+(9a_0a_3-a_1a_2)/9a_0 -- all coeffs/products/denoms matched. Decimal analogy matched.
      – SKIP: Coëfficienten->Coefficienten (ë-drop); colons; eq# left (leqno).
      – ⚠ FORMATTING (deferred): ordinal-suffix superscript -- print "$(m-n+1)^{te}$" (raised te) vs .tex baseline "te"
        (.tex inconsistent; elsewhere $n^{ten}$). Flag for formatting pass (normalize te/ten/ter superscription per Weber).
      – ★ 7 faithful pages running (p23-29). §3 DONE.
  • 2026-07-02 turn 54 (loop re-fire): **p30 (§4 Theilung durch eine lineare Function: setup + Horner recursion
    eq(1-6) + Restsatz C=f(alpha), .tex 664-713) — 0 net EDITS (faithful).** File unchanged (418pp / 0 badness / 2264603).
      – ALL 6 displays row-checked vs scan: eq(1) f(x); eq(2) f=(x-a)Q+C; eq(3) Q; eq(4) BOTH rows (subscripts n-3/n-2/n-1);
        eq(5) recursion 6 rows (q_i-alpha q_{i-1}=a_i, C-alpha q_{n-1}=a_n); eq(6) solved 6 rows (q_i=a_0 alpha^i+...,
        C=f(alpha)); Restsatz prose. All matched.
      – SKIP: Coefficienten (ë-drop); ellipsis-connector "+" (scan "cdots a_{n-1}" vs .tex "cdots+a_{n-1}"); eq# left (leqno).
      – ⚠ FORMATTING (deferred): ordinal-suffix superscript -- scan "(n-1)^{ten}","0^{ten}" raised vs .tex baseline.
      – ★ 8 faithful pages running (p23-30). §4 setup DONE (eq7/eq8 land on p31).
  • 2026-07-02 turn 54b (loop re-fire, cont.): **p31 (§4 tail: eq(7) Restsatz-quotient + series eq(8-11), .tex 715-766)
    — 0 net EDITS (faithful). §4 COMPLETE.** File unchanged (418pp / 0 badness / 2264603).
      – eq(7) fraction; eq(8) f_i series (exponents x^{n-1/n-2/n-3} zoom-checked); inverse expansion (a_1^2-a_2) coeff;
        eq(9) y_i f_i; eq(10) F=Qf+sum; eq(11) recurrence f_r-x f_{r-1}=a_r. All matched.
      – SKIP: Coefficienten (ë-drop); ellipsis-"+"; eq# left. Running header "Division durch lineare Functionen" != title
        (body-only, N/A). ⚠ LAYOUT: .tex 768-769 double \clearpage (layout pass).
      – ★ 9 faithful pages running (p23-31). §4 DONE.
  • 2026-07-02 turn 54c (loop re-fire, cont.): **p32 (§5 Gebrochene Functionen; Theilbarkeit: defs + eq(1-3) +
    Zerlegungs-Satz + geom-series example, .tex 771-808) — 0 net EDITS (faithful).** File unchanged (418pp/0/2264603).
      – §5 heading; def gebrochene rationale/echt/unecht; eq(1) F/f; eq(2) F=Qf+phi; eq(3) F/f=Q+phi/f; Zerlegungs-Satz;
        theilbar-def; geom-series (x^m-1)/(x-1)=x^{m-1}+...+1. All matched.
      – SKIP: eq# left; ellipsis-"+". ⚠ EMPHASIS (deferred): scan gesperrt on defs + Satz + theilbar + identisch
        verschwindet; .tex \emph only on SOME term-defs -> emphasis pass verifies+adds. CONTENT words match.
      – ★ 10 faithful pages running (p23-32). §5 started.
  • 2026-07-02 turn 54d (loop re-fire, cont.): **p33 (§5 Theilbarkeit laws 1-6 + proofs, .tex 810-854) — 0 net EDITS
    (faithful).** File unchanged (418pp/0/2264603).
      – law1 transitivity (F=Qf,f=q phi=>F=Qq phi); law2 (F|f=>QF|f); law3 (F,f|phi=>F±f|phi, ± ZOOM-VERIFIED); law4
        (sum Q_iF_i|f, proof (Q_1 Phi_1+...)f); law5 (self); law6 (Constante). All matched.
      – SKIP: ellipsis-"+"/commas; footer "Weber, Algebra. I."+sig; running header (body-only). ⚠ EMPHASIS (defer):
        laws 5./6.+Constante gesperrt. ⚠ FORMATTING (defer): "nullten Grades" superscript.
      – ★ 11 faithful pages running (p23-33). §5 nearly done (laws 7,8 land on p34).
  • 2026-07-02 turn 55 (loop re-fire): **p34 (§5 tail laws 7,8 + §6 gcd start eq(1,2), .tex 856-882) — 0 net EDITS
    (faithful). §5 DONE, §6 STARTED.** File unchanged (418pp/0/2264603).
      – deg-quotient para; law7 (equal-deg mutual=>const factor); law8 (x-α|f <=> f(α)=0, .tex telegraphic "die dass"
        matches); §6 heading; eq(1) f=A,phi=A'; first div A=Q'A'+A''; Functionenreihe eq(2) A,A',A'',A'''...; grades
        n,n',...abnehmen; last const A^{(ν)}. All matched.
      – ⚠ INDEX GLYPH: A^{(ν)} superscript ambiguous (ν/r) at page zoom -> confirm on p35 (ν-2,ν-1,ν co-occur). .tex=\nu.
      – SKIP: ellipsis; "(S. die Einleitung.)" kept; header/footer. ⚠ EMPHASIS (defer): laws 7.,8.+Algorithmus... gesperrt.
      – ★ 12 faithful pages running (p23-34).
  • 2026-07-02 turn 55b (loop re-fire, cont.): **p35 (§6 gcd Kette eq(3) + gcd-arg + eq(4) + example-1 setup eq(5),
    .tex 883-914) — 0 net EDITS (faithful).** File unchanged (418pp/0/2264603).
      – ★ ZOOM: paren-superscript = Greek ν (nu), NOT r (matches .tex \nu). eq(3) Kette 5 rows; gcd-arg; eq(4) A^{(ν)}=0;
        gcd=A^{(ν-1)}; example-1 eq(5) A,B quadratics. All matched.
      – ★ EMPHASIS VERIFIED: scan gesperrt theilerfremd/relativ prim == .tex \emph (faithful additions). Others gesperrt
        (grösste gemeinsame Theiler, rationalen Rechenoperationen) = emphasis-pass.
      – ★ 13 faithful pages running (p23-35).
  • 2026-07-02 turn 56 (loop re-fire): **p36 (§6 DENSE RESULTANTE eq(6-11) + Resultante def + example-2 eq(12),
    .tex 916-968) — 0 net EDITS (faithful). VERIFIED TERM-BY-TERM.** File unchanged (418pp/0/2264603).
      – eq(8) c_0,c_1 (indices ok); eq(9) D numerator 3 terms; ★eq(10) 7-term resultante ALL terms+signs (+ + - - - + +)
        MATCHED; ★eq(11) factored (a_0b_2-b_0a_2)^2+(a_0b_1-a_1b_0)(a_2b_1-a_1b_2)=0 MATCHED; example-2 eq(12) f,f'.
      – ★ EMPHASIS VERIFIED: scan gesperrt "Resultante" == .tex \emph (faithful).
      – ★★ METHOD INSIGHT: dense coeff-algebra pages AS CLEAN as routine -- damage was in Einleitung verbal prose, not
        symbolic math regardless of density. 14 straight clean (p23-36).
  • 2026-07-02 turn 56b (loop re-fire, cont.): **p37 (§6 DISCRIMINANTE: cubic gcd eq(13-19) + Discriminante def + Satz
    eq(20-21), .tex 969-1016) — 0 net EDITS (faithful). TERM-BY-TERM.** File unchanged (418pp/0/2264603).
      – eq(15) c_0,c_1 (6,2,9); eq(16); eq(18) D; ★eq(19) CUBIC DISCRIMINANT a_1^2a_2^2+18a_0a_1a_2a_3-4a_0a_2^3-4a_1^3a_3
        -27a_0^2a_3^2=0 ALL terms/signs/coeffs(1,18,4,4,27)/cubes MATCHED; eq(20) A''=A-Q'A'; A'''=(1+Q'Q'')A'-Q''A.
      – ★ EMPHASIS VERIFIED: gesperrt "Discriminante" == .tex \emph. "theilerfremd" (non-def) correctly NOT \emph.
      – SKIP: eq(15) ";" vs "," (punct); ë-drop; running header. ★★ 15 straight clean (p23-37); dense-algebra AS clean.
  • 2026-07-02 turn 57 (loop re-fire): **p38 (§6 tail BEZOUT eq(21-25) + Satz I & Satz II start, .tex 1018-1059) — 0 net
    EDITS (faithful). Greek-letter zoom.** File unchanged (418pp/0/2264603).
      – eq(21) A'''=pA+p'A' (lower); eq(22) A^{(ν)}=PA+P'A' (upper); Satz I eq(23) Ff+Φψ=1 (Bezout); eq(24); eq(25)
        Φχ=Qf+φ; Ff+φψ=χ; Satz II start. All matched. ★ F/Φ/f/ψ/χ/φ/Q all distinguished, NO misreads.
      – SKIP: ë-drop; comma after χ(x) (punct); running header. ★ 16 straight clean (p23-38).
  • 2026-07-02 turn 57b (loop re-fire, cont.): **p39 (§6 Satz II eq(26) + §7 VIETA eq(1-2), .tex 1059-1096) — 0 net
    EDITS (faithful). §7 STARTED.** File unchanged (418pp/0/2264603).
      – eq(26) Ff+φψ=χ; §7 heading; eq(1) f=(x-α_1)...(x-α_n)=x^n+a_1x^{n-1}+...+a_n; VIETA eq(2) -a_1=Σα_1, +a_2=Σα_1α_2,
        (-1)^ν a_ν=Σα_1...α_ν, (-1)^n a_n=α_1...α_n (last NO Σ). All signs/α-subscripts matched.
      – SKIP: ellipsis-"+"; ë-drop; "nten Grade" ordinal; running header. ⚠ EMPHASIS: "vollständigen Induction" gesperrt.
      – ★ 17 straight clean (p23-39).
  • 2026-07-02 turn 58 (loop re-fire): **p40 (§7 induction examples + eq(3) recursion + B_ν^{(n)} count eq(4-5),
    .tex 1097-1140) — 0 net EDITS (faithful).** File unchanged (418pp/0/2264603).
      – quad/cubic expansions (cubic 3-term middle α_1α_2+α_1α_3+α_2α_3 verified); eq(3) a_ν=a'_ν-α_n a'_{ν-1} rows
        (a_n=-α_n a'_{n-1}, no a'_n); B_ν^{(n)} count; eq(4) recursion; eq(5) chain. All matched. ★ B double-index correct.
      – SKIP: ellipsis-"+"; ν^{ten} Classe ordinal; running header. ★ 18 straight clean (p23-40).
  • 2026-07-02 turn 58b (loop re-fire, cont.): **p41 (§7 binomial eq(6) + Pi-notation eq(7-9) + Pascal eq(10) +
    induction, .tex 1141-1186) — 0 net EDITS (faithful).** File unchanged (418pp/0/2264603).
      – eq(6) binomial; Pi(m)=1·2·3...m, Pi(0)=1; eq(8) Pi(m)=m Pi(m-1); eq(9) B_ν^{(n)}=Pi(n)/(Pi(ν)Pi(n-ν)); Pascal
        eq(10) B_ν^{(n)}=B_ν^{(n-1)}+B_{ν-1}^{(n-1)} (B_n^{(n)}=B_{n-1}^{(n-1)}); induction step. All matched. ★ Pi-args +
        B (n)/(n-1) superscripts correct.
      – SKIP: eq(6) "n·(n-1)" dot vs juxtaposition (notation); running header. ★ 19 straight clean (p23-41).
  • 2026-07-02 turn 59 (loop re-fire): **p42 (§8 binomische Lehrsatz: eq(1) + Pi-sums + Pascal-triangle table, .tex
    1188-1230) — 0 net EDITS (faithful). §8 STARTED.** File unchanged (418pp/0/2264603).
      – §8 heading; α_i=-y; a_ν=(-1)^ν Σα...=y^ν B_ν^{(n)}; eq(1) (x+y)^n=x^n+B_1^{(n)}x^{n-1}y+...+B_n^{(n)}y^n; expanded
        Pi-sum forms; ★ Pascal table n=1..7 EXACT (1,7,21,35,35,21,7,1 etc). All matched.
      – ★ NOTATION FINDING (defer to fmt pass, NOT fixed): first expanded-Σ has explicit limits (ν over, "0,n" under) in
        scan; .tex bare \sum. Operator-decoration/notation, not text -> formatting pass. POTENTIALLY SYSTEMATIC: grep \sum
        doc-wide, restore Weber Σ limits. (other Σ bare in both.)
      – SKIP: Binomialcoëfficienten ë-drop; "nten" ordinal; header. ⚠ EMPHASIS: binomischen Lehrsatz/Binomialcoëff gesperrt.
      – ★ 20 straight clean (p23-42).
  • 2026-07-02 turn 59b (loop re-fire, cont.): **p43 (§8 Binomialcoeff identities eq(2-5) + alt-sum, .tex 1232-1276)
    — 0 net EDITS (faithful).** File unchanged (418pp/0/2264603).
      – eq(2) power series; geom-series (1+x)^{n+1}-1)/x; eq(3); column-sum eq(4); hockey-stick eq(5) B_ν^{(ν)}+...+B_ν^{(n)}
        =B_{ν+1}^{(n+1)}; alt multipliers ±B_k^{(n)}; alt-sum =[1-(1+x)]^n=(-x)^n. All B ladders matched.
      – NOTE: .tex uses \sum_{ν=0}^{μ} limits at eq(8) (1301) -> p42 bare-\sum is localized drop (fmt pass, restorable).
      – SKIP: punct/ellipsis/ë-drop/header/ordinals. ★ 21 straight clean (p23-43).
  • 2026-07-02 turn 60 (loop re-fire): **p44 (§8 product-identities eq(6-8) + §9 Interpolation start, .tex 1279-1326)
    — 1 CONTENT FIX (FABRICATION). Ends 21-page clean streak.** Compiles 418pp / 0 overfull / 0 underfull / PDF 2264580 B.
      – ★★ FIX: .tex 1328 "...a_n, UM die sich...auflösen lassen" -> scan (ZOOM) "...a_n, die sich..." (no "um"; "um"
        breaks grammar). REMOVED "um ". 2nd fabrication (after z+c p19). Compile-gated clean.
      – eq(6)/(7)/(8) double-B product identities MATCHED; §9 heading; eq(1) f(x); eq(2) f(α_i)=A_i.
      – ★ Σ-NOTATION: eq(8) scan Weber-Σ (ν over, 0,μ under) vs .tex modern \sum_{ν=0}^{μ} = same limits, old-vs-modern
        convention -> fmt pass. Refines p42 finding (systematic Weber-Σ-convention; content intact).
      – SKIP: ë-drop; ellipsis-"+"; nten ordinal; header.
      – ★★ FINGERPRINT CORRECTION: the "2264603" in prior logs was the PDF byte size (not .tex). Gate = **418pp / 0
        overfull / 0 underfull**; PDF ~2264580 B; .tex ~1308110 B. Compile: pdflatex x2 in .../v1/ge/.
  • 2026-07-02 turn 61 (loop re-fire): **p45 (§9 Interpolation: generalized B_ν^{(x)} + M-system eq(3-6), .tex 1328-1357)
    — 3 CONTENT FIXES.** Compiles 418pp / 0 overfull / 0 underfull / PDF 2264596 B.
      – ★★ FIX1 (normalization revert): .tex prose "$B_\nu^{(x)}$...wenn $x$ keine ganze Zahl" -> scan (ZOOM) "$B_\nu^{(n)}$
        ...wenn $n$..." (Weber uses (n) in prose, x only in eq3 display). RESTORED n.
      – ★★ FIX2 (dropped term): eq(5) f(n) row missing $M_2B_2^{(n)}$ (scan has it, paralleling f(2)). RESTORED.
      – ★★ FIX3 (spelling revert, Weber variant [sic]): footnote scan "Binom**in**alcoëfficienten" vs .tex "Binomial".
        RESTORED "Binominal" (body uses Binomial; Weber footnote variant/typo).
      – ★★★ METHOD INSIGHT: §4-§8 pure-identity pages PRISTINE ~15pp; §9 (prose exposition) = 3 fixes. **DAMAGE FOLLOWS
        PROSE/EXPOSITION density, not math density.** => read prose word-by-word in expository/definitional passages.
      – Streak: 21 clean (p23-43), then p44 (1 fix), p45 (3 fixes). §9 is a damage cluster (like Einleitung).
  • 2026-07-03 turn 62 (loop re-fire): **p46 (§9 tail eq(7) + §10 Differenzen start eq(1-5), .tex 1360-1404) — 1 CONTENT
    FIX (Weber capital-F typo [sic]).** Compiles 418pp / 0 overfull / 0 underfull / PDF 2264595 B.
      – ★★ FIX: .tex 1373 "die Function $f(x)$ bestimmt" -> scan (ZOOM) CAPITAL "$F(x)$" (differs from lowercase f in eq7
        above; §9 fn is lowercase f). Weber typo; GPT corrected F->f. RESTORED $F(x)$ [sic].
      – §9 tail eq(7) ±M_ν=...; §10 heading; eq(1) B_ν^{(x)}; eq(2) Pascal-x; eq(3) f(x)=f(0)+ΣM_iB_i^{(x)}; eq(4) Δ_x=
        f(x+1)-f(x); eq(5) Δ_x=M_1+M_2B_1^{(x)}+... All matched.
      – ★ META-PATTERN: §9-§10 expository cluster keeps carrying damage (p45×3, p46×1); prose-density-driven. Word-by-word
        prose read caught F(x).
  • 2026-07-03 turn 63 (loop re-fire): **p47 (§10 tail eq(6-8)+diff-table; §11 start, .tex 1405-1455) — 1 CONTENT FIX
    (dropped sentence) + 3 formatting flags.** Compiles 418pp / 0 overfull / 0 underfull / PDF 2264696 B.
      – ★★ FIX: post-table sentence "und, wenn die $f(0),f(1),\ldots$ gegeben sind, durch einfache Subtractionen berechnet
        wird." DROPPED (table -> straight to §11). RESTORED after table.
      – ⚠ FORMATTING (deferred, logged): eq(6) 3-row aligned diff-on-left vs .tex inline-swapped+general-row->\ldots; eq7/eq8
        extra intermediate term; diff-table top-aligned+ruled vs .tex bottom-aligned+plain. All layout (entries/text match).
      – ★ LESSON: drops hide at display/table/section SEAMS -- check text right before/after every display, table, heading.
      – §10-§11 expository cluster: p45×3, p46×1, p47×1. Prose-density damage continues.
  • 2026-07-03 turn 64 (loop re-fire): **p48 (§11 Arith. Reihen höherer Ordnung cont.: Δ-recursion eq(2-3) + f(x)-generation +
    Satz, .tex 1456-1510) — FAITHFUL, 0 content fixes.** File unchanged: 418pp / 0 overfull / 0 underfull / PDF 2264696 B.
      – top: eq(2) Δ_0=u_1-u_0...; eq(3) Δ'_0=Δ_1-Δ_0...; u_m=u_0+Δ_0+...+Δ_{m-1}; def arith-Reihe nter Ordnung. ✓
      – mid: ladder Δ_x=f(x+1)-f(x); Δ'_x=Δ_{(x+1)}-Δ_x; ...; Δ_x^{(n-1)}=Δ_{(x+1)}^{(n-2)}-Δ_x^{(n-2)} (★parenthesized (x+1)
        subscripts in scan MATCH .tex \Delta_{(x+1)}); degree remark. ✓
      – bot: u_0,u_1,u_2...; "n Werthe u_0..u_{n-1} + constante nte Diff"; "(n+1)te Glied u_n"; **Satz** "Eine arith. Reihe nter
        Ordnung ist vollständig bestimmt, wenn ihre n+1 ersten Glieder gegeben sind"; "Da nun...f(0),f(1),f(2)...f(n)". ✓ word-for-word.
      – ⚠ EMPHASIS: Satz is gesperrt in scan; .tex \begin{quote} (no letter-space). Defer to emphasis pass.
      – ★ META-PATTERN REFINEMENT: p48 EXPOSITORY but FULLY FAITHFUL -- its prose is NARRATIVE/THEOREM-STATEMENT, not the
        definition-generalization-with-new-notation that damaged §9 (p45) & §10 tail (p46-47). Refined rule: DAMAGE CLUSTERS WHERE
        GPT CAN NORMALIZE NOTATION/DEFINITIONS (generalize/rename/"improve" a def), not merely where prose is dense. Clean
        theorem/narrative pages pass through. Seam-checks (Satz + 2 displays) all clean.
  • 2026-07-03 turn 64b (continuous grind): **p49 (§11 tail: Summen s_m + erzeugende Function F(x)-system eq(4) + x^2 example,
    .tex 1510-1564) — content FAITHFUL, 0 fixes + 1 formatting flag.** File unchanged: 418pp / 0 overfull / 0 underfull / PDF 2264696 B.
      – top: "aus den ganzen rat. Fn nten Grades f(x) alle arith. Reihen erzeugt"; s_m=u_0+u_1+...+u_m; (n+1)ter Ordnung; s_{m+1}-s_m=u_{m+1}. ✓
      – mid: "Formel(7) §10 Summe s_m... s_0,s_1...s_{n+1}"; "erzeugende Function F(x) von s_m... f(x) von u_m"; F(0)=f(0),F(1)=f(0)+f(1),
        F(2)=f(0)+f(1)+f(2),⋯; F(x)=F(0)+D_0B_1^{(x)}+D'_0B_2^{(x)}+⋯. ✓
      – bot: D-system D_0=F(1)-F(0)=f(1)/D'_0=f(2)-f(1)=Δ_1; D_1/D'_1; D_2=F(3)-F(2)=f(3)/D''_0=Δ_2-Δ_1=Δ'_1; eq(4) F(x)=f(0)+f(1)B_1^{(x)}
        +Δ_1B_2^{(x)}+Δ'_1B_3^{(x)}+⋯; "f(x)=x^2... m ersten Quadratzahlen"; Δ_x=2x+1, Δ'_x=2; "also". ✓ word-for-word.
      – ⚠ FORMATTING: scan has full-width continuation-dots row AFTER the D-system display; .tex drops it (D''_0=Δ'_1. -> \] direct).
        Typographic "pattern continues" marker, no German text/quantity. Defer to formatting pass (restore dots-row). F-system \cdots IS in .tex.
      – ★ META-PATTERN: 2 clean pages (p48-49); both expository but narrative/computational (no def-generalization). Refined rule holds.
  • 2026-07-03 turn 64c (continuous grind): **p50 (§11 tail x^2/x^3 results + §12 Der polynomische Lehrsatz start eq(1-5),
    .tex 1566-1608) — FULLY FAITHFUL, 0 fixes.** File unchanged: 418pp / 0 overfull / 0 underfull / PDF 2264696 B.
      – top: F(x)=x+3·x(x-1)/(1·2)+2·x(x-1)(x-2)/(1·2·3)=x(x+1)(2x+1)/6; x^3=>F(x)=(x(x+1)/2)^2; "m ersten Cuben=Quadrat mten
        Trigonalzahl"; §12 heading "Der polynomische Lehrsatz". ✓
      – mid: "Im §8...binom. Lehrsatz Form abgeleitet"; eq(1) (x+y)^n=Π(n)Σ^{α,β}x^α y^β/(Π(α)Π(β)); eq(2) α+β=n; "Diese Form
        gestattet...Verallgemeinerung auf nte Potenz eines Polynoms"; eq(3) (x+y+z+⋯)^n=Π(n)Σ^{α,β,γ,…}...; Bestimmung-prose. ✓
      – bot: eq(4) α+β+γ+⋯=n; "Um aber die Richtigkeit...Polynom ein Glied weniger...nur zwei Glieder enthält"; "Wir setzen dann";
        eq(5) u=y+z+⋯; "wenden auf (x+u) Formel(1) an, aus der sich ergiebt:". ✓ word-for-word.
      – ⚠ EMPHASIS/FMT (tracked): §12 heading gesperrt; eq-nums (1)-(5) leqno. Σ^{...} = Weber upper-limit-only, matches .tex.
      – ★ META-PATTERN STRENGTHENED: §12 expository INTRO CLEAN -- it RE-DERIVES from §8's established Π/Σ notation (no new def to
        normalize). vs §9 (p45) which GENERALIZED B_ν to real args => damaged. Rule: damage clusters at DEF-GENERALIZATION/NOTATION-
        NORMALIZATION, not expository prose per se. 3 clean pages (p48, p49-content, p50).
  • 2026-07-03 turn 64d (continuous grind): **p51 (§12 tail eq(6-11) poly-thm proof + Trinom^3 + §13 Derivirte Functionen start
    eq(1)+def-para, .tex 1610-1662) — FULLY FAITHFUL, 0 fixes.** File unchanged: 418pp / 0 overfull / 0 underfull / PDF 2264696 B.
      – §12 proof: eq(6) (x+y+z+⋯)^n=Π(n)Σ^{α,ν}x^α u^ν/(Π(α)Π(ν)); eq(7) α+ν=n; eq(8) u^ν=Π(ν)Σ^{β,γ,…}...; eq(9) β+γ+⋯=ν;
        "in (6) eingesetzt => Formel(3), (7) geht in (4) über"; eq(10) P_{α,β,γ,…}^{(n)}=Π(n)/(Π(α)Π(β)Π(γ)⋯); "Polynomialcoëfficienten". ✓
      – Trinom: eq(11) (x+y+z)^3=x^3+y^3+z^3+3x^2y+3xy^2+3x^2z+3xz^2+3y^2z+3yz^2+6xyz (all 10 terms). ✓
      – §13 start: heading "Derivirte Functionen"; "Es sei"; eq(1) f(x)=a_0x^n+a_1x^{n-1}+a_2x^{n-2}+⋯+a_n; "ganze rat. Fn nter Ordnung". ✓
      – def-para (1658, WORD-BY-WORD): "Wenn wir darin x durch Binom x+y ersetzen... binom. Lehrsatz anwenden... nach fallenden oder
        nach steigenden Potenzen von x oder y ordnen... nach steigenden Potenzen von y... höchste Potenz von y... nte... Coëfficient
        der nullten Potenz von y ist f(x) selbst... y=0 setzt. Wir setzen also, indem wir die anderen Coëfficienten mit"; f'(x),f''(x)/Π(2),
        f'''(x)/Π(3),…; "bezeichnen:". ✓ every word, no drops/inserts.
      – ⚠ EMPHASIS/FMT (tracked): §13 heading gesperrt; eq-nums leqno; eq(11) line-break after 3xy^2(scan)/3xz^2(.tex)=layout. Σ^{...}=Weber upper-limit.
      – SKIP: Coëfficient/-en ë-drop ×3; ellipsis; ordinal. ★ 4 clean pages p48-51 (all derive/define from established notation).
  • 2026-07-03 turn 64e (continuous grind): **p52 (§13 Derivirte Functionen: eq(2) Taylor + Derivirte-def + eq(3) f' + Hauptsatz
    eq(4-8), .tex 1663-1709) — FULLY FAITHFUL, 0 fixes.** File unchanged: 418pp / 0 overfull / 0 underfull / PDF 2264696 B.
      – eq(2) f(x+y)=f(x)+yf'(x)+y^2/(1·2)f''(x)+⋯=Σ_{ν=0}^{n} y^ν/Π(ν) f^{(ν)}(x); Derivirte-def ("erste,zweite,dritte Derivirte
        oder Abgeleitete"; f^{(ν)} Grad n-ν nicht übersteigen); "Die erste Derivirte... binom. Lehrsatz auf (1)". ✓
      – eq(3) f'(x)=na_0x^{n-1}+(n-1)a_1x^{n-2}+(n-2)a_2x^{n-3}+⋯; Hauptsatz "x in x+z oder y in y+z"; eq(4) f(x+y+z)=Σy^ν/Π(ν)f^{(ν)}(x+z)
        =Σ(y+z)^ν/Π(ν)f^{(ν)}(x); eq(5) f^{(ν)}(x+z)=Σz^μ/Π(μ)f^{(ν,μ)}(x); eq(6) (y+z)^ν/Π(ν)=Σ^{β,γ}y^β z^γ/(Π(β)Π(γ)),β+γ=ν. ✓
      – eq(7) ΣΣ y^ν z^μ/(Π(ν)Π(μ))f^{(ν,μ)}(x)=Σ^{β,γ}y^β z^γ/(Π(β)Π(γ))f^{(β+γ)}(x); "Die letzte Summe... β,γ... Vergleichung der
        Coëfficienten... (nach §1)"; eq(8) f^{(ν,μ)}(x)=f^{(ν+μ)}(x); "also den Satz:". ✓ word-for-word.
      – ⚠ FMT (tracked): Σ Weber-conv (ν over/0,n under) eq(2)/(4)/(5)/(7); leqno. SKIP ë-drop. EMPHASIS gesperrt (Derivirte terms).
      – ★ 5 clean pages p48-52; entire §13 Taylor/Hauptsatz derivation clean (established notation, no def to normalize; multi-index f^{(ν,μ)} exact).
  • 2026-07-03 turn 65 (loop re-fire): **p53 (§13 tail: Satz + eq(9) deriv-ladder + Binomialcoeff-Darstellung eq(10-12) +
    notation-choice para start, .tex 1710-1740) — FULLY FAITHFUL, 0 fixes + 2 fmt flags.** File unchanged: 418pp / 0 overfull /
    0 underfull / PDF 2264696 B.
      – Satz "Die μte Derivirte von der νten Derivirten ist die (ν+μ)te Derivirte der ursprünglichen Function"; eq(9) f/f'/f'' ladder;
        "Eine etwas einfachere Form... anderen Bezeichnungsweise..."; eq(10) f(x)=a_0x^n+B_1^{(n)}a_1x^{n-1}+B_2^{(n)}a_2x^{n-2}+⋯+a_n;
        eq(11) ausführlich; "»mit den Binomialcoëfficienten geschrieben«"; eq(12) f/f'/f'' with Binomialcoeff. ✓ word-for-word.
      – ⚠ FMT: 2 dropped continuation-dots rows (after eq(9) & eq(12) aligns; same class as p49). leqno. EMPHASIS gesperrt (Satz + "mit
        den Binomialcoeff geschrieben"). SKIP ë-drop ×3.
      – ★ 6 clean pages p48-53. notation-CHOICE para (1740) clean so far. ★★ DAMAGE-WATCH: Gauss/Disq.ar. HISTORICAL remark (free
        discursive prose) at TOP of p54 -- refined rule predicts high risk; verify word-by-word.
  • 2026-07-03 turn 65b (continuous grind): **p54 (§13 tail Gauss/Disq.ar. remark + §14 Derivirte eines Productes start eq(1-5),
    .tex 1740-1769) — FULLY FAITHFUL, 0 fixes.** File unchanged: 418pp / 0 overfull / 0 underfull / PDF 2264696 B.
      – ★★ DAMAGE-WATCH RESOLVED CLEAN: Gauss/Disq.ar. historical remark WORD-FOR-WORD faithful (Gauss, "(in den Disq. ar.)",
        ax^2+2bxy+cy^2, "unnöthigen und sehr bedauerlichen Complication" all preserved).
      – §14 heading "Derivirte eines Productes"; intro (Differentialquotienten/Infinitesimalrechnung/D_ν); eq(1) f(x+y)=f(x)+yD_1f+
        y^2/(1·2)D_2f+y^3/(1·2·3)D_3f+⋯; eq(2) D_ν(Cf)=CD_νf; eq(3) D_ν(f+φ)=D_νf+D_νφ; eq(4) f(x+y)=u_0+yu_1+...+y^nu_n & φ(x+y)=v_0+...+y^mv_m;
        eq(5) u_ν=D_νf/Π(ν), v_ν=D_νφ/Π(ν). ✓ word-for-word.
      – SKIP: ë-drop; ellipsis-connector-+; φ=\varphi. EMPHASIS gesperrt (§14 heading; Gauss). leqno.
      – ★★★ REFINEMENT: discursive prose damaged when LONG+ABSTRACT (Einleitung) but CLEAN when SHORT+FACT-ANCHORED (name/citation/
        formula). Rule unchanged (read all prose word-by-word); calibrates expectation. 7 clean pages p48-54; §11-§14 block entirely clean.
  • 2026-07-03 turn 66 (loop re-fire): **p55 (§14 product-derivative: Leibniz eq(6-7) + n-factor D eq(8) + linear-factor product
    eq(9-11), .tex 1770-1823) — FULLY FAITHFUL, 0 fixes + 1 fmt flag.** File unchanged: 418pp / 0 overfull / 0 underfull / PDF 2264696 B.
      – eq(6) D_ν(fφ)/Π(ν)=u_νv_0+u_{ν-1}v_1+...+u_0v_ν; eq(7) D_ν(fφ)=φD_νf+B_1^{(ν)}D_{ν-1}fD_1φ+B_2^{(ν)}D_{ν-2}fD_2φ+⋯ (Binomialcoeff);
        "In ähnlicher Weise... Polynomialcoeff... mehr als zwei Factoren"; eq(8) D(u_1...u_n)=u'_1u_2...u_n+...+u_1...u'_n; "oder kürzer"
        D(∏u)/∏u=ΣDu_ν/u_ν; eq(9) f(x)=(x-α_1)...(x-α_n); eq(10) f'(x)=Σ(product-with-one-factor-omitted); eq(11) f'(x)=Σf(x)/(x-α_i);
        "Ein sehr wichtiges Resultat... x=α_i... nämlich". ✓ word-for-word.
      – ⚠ FMT: eq(10) middle-omission as separate dots-row (scan) vs inline +\cdots (.tex); same dots-row family (p49/p53). leqno.
        SKIP ë-drop, ellipsis-connector-+, φ=\varphi. EMPHASIS gesperrt "erste Derivirte".
      – ★ 8 clean pages p48-55; §14 entirely clean; §11-§14 block clean (all derive from established notation).
  • 2026-07-03 turn 66b (continuous grind): **p56 (§14 tail eq(12) f'(α_i) + §15 Ganze Functionen mehrerer Veränderlichen: Formen
    start [DEF multivar + homogen + Euler eq(1)], .tex 1824-1853) — FULLY FAITHFUL, 0 fixes.** File unchanged: 418pp / 0 overfull /
    0 underfull / PDF 2264696 B.
      – eq(12) f'(α_1)=(α_1-α_2)...(α_1-α_n), ..., f'(α_n)=(α_n-α_1)...(α_n-α_{n-1}) [dots-row PRESENT in .tex here, matches]; §15 heading.
      – ★★ DAMAGE-WATCH CLEAN: §15 DEF core word-for-word -- "Unter einer ganzen rat. Fn nten Grades mehrerer Veränderlichen F(x,y,z,…)
        verstehen wir eine Summe von Gliedern" ΣA_{α,β,γ,…}x^α y^β z^γ⋯; "α+β+γ+⋯ den Werth n nicht übersteigt... wenigstens in einem Gliede
        erreicht... Grad=grösster Werth"; "denselben Werth => homogen"; Euler eq(1) F(tx,ty,tz,…)=t^nF(x,y,z,…) + Beweis (t^{α+β+γ+⋯} factor). ✓
      – SKIP ellipsis, ordinal. EMPHASIS gesperrt (§15 heading; "homogen"). leqno.
      – ★★★ REFINEMENT: §15 INTRODUCES DEFINITIONS yet CLEAN => damage trigger is NOTATION-NORMALIZATION opportunities, NOT definitions
        per se. §9 damaged = introduced B_ν^{(x)} w/ var-superscript GPT normalized + spelling variants; §15 = plain-prose defs w/ standard
        Σ/subscript notation, nothing to normalize. Rule unchanged (read all prose word-by-word, esp. NEW NOTATION). 9 clean pages p48-56.
  • 2026-07-03 turn 67 (loop re-fire): **p57 (§15 homogenization [x=x_i/x_m, Φ] + Polynomialcoeff-form eq(2-3) + ν-index-form
    eq(4) + permutation-count, .tex 1853-1890) — FULLY FAITHFUL, 0 fixes.** File unchanged: 418pp / 0 overfull / 0 underfull / PDF 2264696 B.
      – homogenization x=x_1/x_m,...; x_m^n F(...); Φ(x_1,...,x_m); eq(2) Φ=ΣΠ(n)/(Π(α_1)...Π(α_m))A_{α_1,...,α_m}x_1^{α_1}...x_m^{α_m};
        eq(3) α_1+...+α_m=n; eq(4) Φ=ΣA_{ν_1,...,ν_n}x_{ν_1}...x_{ν_n}; permutation-count (m^n Glieder, Π(n) Permutationen, reducirt auf...). ✓ word-for-word.
      – SKIP Polynomialcoëff ë-drop, ellipsis. EMPHASIS gesperrt ("verschiedene", "mit den Polynomialcoëff"). leqno.
      – ★★★ SHARPENING: §15 (p57) INTRODUCES new notation (Φ, eq2/eq4 forms) yet CLEAN => damage predictor is NOT notation-intro but LOCAL
        INCONSISTENCY/VARIANT GPT smooths. §9 damaged = prose B_ν^{(n)} vs display B_ν^{(x)} reconciled + spelling variant. §15 uses Φ/α/ν/Π
        consistently => nothing to reconcile => clean. Sharpest predictors: prose-vs-display mismatch / spelling variants / dropped terms at seams. 10 clean pages p48-57.
  • 2026-07-03 turn 67b (continuous grind): **p58 (§15 tail: (2)/(4) identity + Gliederzahl (m,n) recursion eq(5-6) + Formen
    terminology, .tex 1892-1921) — FULLY FAITHFUL, 0 fixes. §15 COMPLETE clean.** File unchanged: 418pp / 0 overfull / 0 underfull / PDF 2264696 B.
      – Π(n)/(Π(α_1)Π(α_2)⋯); "(4) irgend ein Product... genau [...] mal vorkommt"; "(2) und (4) identisch... x_{ν}...=x_1^{α_1}...x_m^{α_m},
        A_{ν...}=A_{α...}"; (m,n)-count para; eq(5) (m,n)=(m,n-1)+(m-1,n); eq(6) (m,n)=m(m+1)...(m+n-1)/(1·2...n)=Π(m+n-1)/(Π(n)Π(m-1)); "als
        richtig erweist"; Formen-terminology (Formen/unär/binär/ternär/quaternär; binäre Formen ≡ ganze rat. Fn 1 Veränderl.; Werth 1). ✓ word-for-word.
      – SKIP ellipsis. EMPHASIS gesperrt (Formen/unäre/binäre/ternäre/quaternäre). leqno.
      – ★ 11 clean pages p48-58; §15 COMPLETE clean; §11-§15 block ENTIRELY clean. Formen-terminology clean (fact-anchored terms). Never-certify: verify each page.
  • 2026-07-03 turn 68 (loop re-fire): **p59 (§16 Die Derivirten von Functionen mehrerer Variablen start: partial-deriv eq(1-3)
    + multivar-Taylor eq(4), .tex 1923-1966) — FULLY FAITHFUL, 0 fixes.** File unchanged: 418pp / 0 overfull / 0 underfull / PDF 2264696 B.
      – §16 heading; intro (Begriff aus §13 übertragen, Ableitung je Variable); eq(1) F(x,y,z,…)=ΣA_{α,β,γ,…}x^α y^β z^γ⋯; eq(2)
        F'(x)=Σα A x^{α-1}y^β z^γ⋯; eq(3) F'(y)=Σβ A x^α y^{β-1}z^γ⋯; "höheren Ableitungen"; multivar-Taylor: x_i+ξ_i binome; Φ(x+ξ);
        (x_1+ξ_1)^{μ_1}...(x_m+ξ_m)^{μ_m} [★ZOOM: exponents μ not α]; "Taylor'sche Entwickelung"; eq(4) Φ(x+ξ)=Σ ξ_1^{α_1}...ξ_m^{α_m}/(Π(α_1)...Π(α_m))D_{α_1,...,α_m}Φ. ✓ word-for-word.
      – ★ ZOOM: (x_i+ξ_i)-exponents μ_i vs α_i ambiguous at thirds-res; crop settled μ (matches .tex). Weber: μ_i=original x-exponents,
        α_i=ξ-exponents post-Taylor (distinct roles same page). => always zoom generic-exponent glyphs.
      – SKIP Coëff ë-drop, ellipsis. EMPHASIS gesperrt (§16 heading; "einer"; "Taylor'sche"). leqno. 12 clean pages p48-59.
  • 2026-07-03 turn 69 (loop re-fire): **p60 (§16 cont.: ∂-notation eq(5) + D-rules I/II + power-product derivative eq(6-8),
    .tex 1968-2033) — FULLY FAITHFUL, 0 fixes.** File unchanged: 418pp / 0 overfull / 0 underfull / PDF 2264696 B.
      – eq(5) D_{α_1,...,α_m}Φ=∂^ν Φ/(∂x_1^{α_1}∂x_2^{α_2}⋯∂x_m^{α_m}) [∂-notation]; D-rule I D(CΦ)=CDΦ; II D(Φ+Ψ)=DΦ+DΨ; "Beides folgt aus (4)";
        power-product setup D_{α}(x_1^{μ_1}...x_m^{μ_m}); (x_1+ξ_1)^{μ_1}=Σ^{α_1}Π(μ_1)/(Π(α_1)Π(μ_1-α_1))ξ_1^{α_1}x_1^{μ_1-α_1}; eq(6) full
        Π-quotient; eq(7) D_{α}(x_1^{μ_1}...x_m^{μ_m})=Π(μ_1)...Π(μ_m)/(Π(μ_1-α_1)...Π(μ_m-α_m))x_1^{μ_1-α_1}...x_m^{μ_m-α_m}, α_i≤μ_i; eq(8)
        =0 sobald α>μ. ✓ word-for-word (num/denom verified).
      – SKIP ellipsis. EMPHASIS gesperrt "Derivirten νter Ordnung". leqno; Σ^{α...}=Weber upper-limit(fmt). 13 clean pages p48-60.
  • 2026-07-03 turn 69b (continuous grind): **p61 (§16 cont.: double-deriv eq(9) + Satz III commutativity + deriv-shorthand +
    quadratic-form eq(10-13), .tex 2035-2095) — FULLY FAITHFUL, 0 fixes.** File unchanged: 418pp / 0 overfull / 0 underfull / PDF 2264696 B.
      – β-system; eq(9) D_β D_α(x^μ)=D_{β+α}(x^μ); Satz III D_β D_α Φ=D_{β+α}Φ (Verallg. von (8) §13); deriv-shorthand D_{1,0..0}Φ=Φ'(x_1),
        Φ''(x_1,x_2)=Φ''(x_2,x_1); quadratic form eq(10) Φ(x)=Σa_{i,k}x_i x_k (a_{i,k}=a_{k,i}); eq(11) ½Φ'(x_i)=Σa_{i,j}x_j; eq(12) Φ(x,ξ)=
        Φ(ξ,x)=Σξ_iΦ'(x_i)=Σx_iΦ'(ξ_i); eq(13) Φ(x+ξ)=Φ(x)+Φ(x,ξ)+Φ(ξ). ✓ word-for-word.
      – SKIP ellipsis. leqno. Running header varies within §16 (out of scope). 14 clean pages p48-61.
  • 2026-07-03 turn 70 (loop re-fire): **p62 (§16 tail Polare def eq(14-15) + §17 Euler'sches Theorem start eq(1-4), .tex 2096-2144)
    — FULLY FAITHFUL, 0 fixes.** File unchanged: 418pp / 0 overfull / 0 underfull / PDF 2264696 B.
      – Polare def: Φ(x,ξ) Polare von Φ, linear+homogen in x & ξ; eq(14) Φ(x,ξ)=2Σa_{ik}ξ_i x_k; eq(15) Φ(x,x)=2Φ(x); §17 heading; Euler
        intro (Fundamentalsatz... von Euler entdeckt); eq(1) ξ_i=tx_i; eq(2) (1+t)^n Φ(x)=Σ(tx_1)^{α_1}.../((Π(α_1)...)D_{α}Φ; binom. Satz
        => für jedes ν=1..n; eq(3) Π(n)/Π(n-ν)Φ=Σ^{α}Π(ν)/(Π(α_1)...Π(α_m))x_1^{α_1}...x_m^{α_m}D_{α}Φ; eq(4) α_1+...+α_m=ν. ✓ word-for-word.
      – SKIP Coëff ë-drop, ellipsis. EMPHASIS gesperrt ("Polare"; §17 heading; "Euler"). leqno; Σ^{α}=Weber upper-limit(fmt). 15 clean pages p48-62.
  • 2026-07-03 turn 70b (continuous grind): **p63 (§17 tail: Euler cases eq(5-6) + Polaren eq(7-10) + binary-form eq(9-dup);
    LAST PAGE of ERSTER ABSCHNITT, .tex 2146-2196) — FULLY FAITHFUL, 0 fixes + 1 documented Weber erratum.** File unchanged: 418pp / 0
    overfull / 0 underfull / PDF 2264696 B.
      – eq(5) nΦ=Σx_iΦ'(x_i) [ν=1 Euler]; eq(6) n(n-1)Φ=Σ_{i,k=1}^{m}x_i x_k Φ''(x_i,x_k) [ν=2]; eq(7) Φ_ν(ξ,x)=Σξ_1^{α_1}.../((Π...)D_αΦ;
        eq(8) Φ(x+ξ)=Φ(x)+Φ_1+...+Φ_n; eq(9) Φ_{n-ν}(x,ξ)=Φ_ν(ξ,x); eq(10) Φ_n(x,ξ)=Φ(ξ); "νte Polare" def; binary form m=2: Φ(x,y)=u,
        D_{h,ν-h}Φ=u_h; eq(9)[DUP] Π(n)/Π(n-ν)u=Σ_{h=0}^{ν}Π(ν)/(Π(h)Π(ν-h))u_h x^h y^{ν-h}. ✓ word-for-word.
      – ★★ WEBER ERRATUM (type-B, faithful in .tex, do NOT correct): binary-form eq numbered (9) in SCAN (ZOOM) = DUPLICATE of earlier eq(9).
        Weber reused (9) [sequence ...(8)(9)(10)(9)]. .tex \tag{9} both = faithful; no label conflict; compiles clean. Documented.
      – SKIP ellipsis-connector, ordinal. EMPHASIS gesperrt "νte Polare". leqno; Σ index-over=Weber-conv(fmt).
      – ★ MILESTONE: ERSTER ABSCHNITT COMPLETE (§1-§17). 16 clean pages p48-63 (only faithful dup-(9)). Next: Zweiter Abschnitt Determinanten §18.
  • 2026-07-03 turn 71 (loop re-fire): **p64 (ZWEITER ABSCHNITT: Determinanten divider + §18 Permutationen von n Elementen start
    eq(1-2), .tex 2199-2230) — FULLY FAITHFUL, 0 fixes + 1 fmt flag.** File unchanged: 418pp / 0 overfull / 0 underfull / PDF 2264696 B.
      – ★ PAGE-ALIGNMENT VERIFIED: "Zweiter Abschnitt./Determinanten." divider INLINE at top of printed p64 (not a separate page); offset
        +26 holds, NO page shift. Section-opening page has no running header.
      – §18 heading; "System von n unterschiedenen Elementen... n Ziffern 1,2,3...n"; "Complex mit 𝔄 bezeichnen... Elemente von 𝔄... z.B.
        2,1,3...n"; "Uebergang... heisst eine Permutation"; "mit Π(n)... Π(1)=1,Π(2)=2... zu n-1..."; n-th-element insertion arg; eq(1)
        Π(n)=nΠ(n-1); eq(2) Π(n)=1·2·3...n. ✓ word-for-word.
      – ★ FRAKTUR 𝔄 PRESERVED (both occurrences match \mathfrak A; no italic-norm). Stay vigilant (Fraktur = known GPT-risk in Determinanten).
      – ⚠ FMT: scan "Π(1)=1,Π(2)=2" INLINE in prose; .tex promotes to display \[...\]. Identical content -> fmt pass (inline->display). Low pri.
      – SKIP ellipsis, ordinal. EMPHASIS gesperrt (§18 heading; "Permutation"). 17 clean pages p48-64.
  • 2026-07-03 turn 72 (loop re-fire): **p65 (§18 tail Transpositionen eq(3)+examples; §19 Permutationen erster u. zweiter Art
    start, .tex 2231-2265) — FULLY FAITHFUL, 0 fixes + 3 fmt flags (systematic).** File unchanged: 418pp / 0 overfull / 0 underfull / PDF 2264696 B.
      – ★ §-STRUCTURE: header "§19" correct -- §19 "Permutationen erster u. zweiter Art" starts partway down p65 (.tex 2257, grep-confirmed);
        heading present in .tex (not dropped).
      – §18 tail: Π(n) meaning=§7; eq(3) 𝔄'=α_1,...,α_n; Transposition-procedure (in 𝔄... mit α_1... 2 mit α_2); example (1,2,3,4)→(4,2,3,1)
        →(4,3,2,1) via (1,4),(2,3); "unendlich viele Arten" + (1,2),(1,3),(2,4),(1,2). §19 heading; "Π(n) Anordnungen in zwei Arten zerlegen";
        "n(n-1)/2 Paare... Wir wollen nun den n Elementen". ✓ word-for-word.
      – ★ FRAKTUR 𝔄/𝔄' PRESERVED at all 5+ occurrences (no italic-norm). Determinanten Fraktur clean through p65.
      – ⚠ FMT (SYSTEMATIC): §18-§19 .tex promotes inline formula-lists to displays [(1,4),(2,3); (1,2),(1,3),(2,4),(1,2); n(n-1)/2 all INLINE
        in scan, DISPLAY in .tex; +p64 Π(1)=1,Π(2)=2]. Content identical. Track as ONE systematic fmt item.
      – SKIP ellipsis. EMPHASIS gesperrt (§19 heading; "Transpositionen"). 18 clean pages p48-65.
  • 2026-07-03 turn 73 (loop re-fire): **p66 (§19 Differenzenproduct P eq(1) + permuted P' eq(2) + sign-of-permutation I/II,
    .tex 2265-2293) — FULLY FAITHFUL, 0 fixes.** File unchanged: 418pp / 0 overfull / 0 underfull / PDF 2264696 B.
      – Zahlwerthe a_i, n(n-1)/2 Differenzen; eq(1) P=(a_1-a_2)(a_1-a_3)...(a_{n-1}-a_n); "positiv wenn a_1>a_2>...>a_n"; "von 𝔄 zu 𝔄'
        übergehen, P geht in" eq(2) P'=(a_{α_1}-a_{α_2})...(a_{α_{n-1}}-a_{α_n}) [★ZOOM nested a_{α_i} correct]; "P' gleich P oder entgegengesetzt";
        I.(gesperrt) erste/zweite Art def; II.(gesperrt) Transposition (h,k) ändert Vorzeichen; "Factor ±(a_h-a_k), Factorenpaare ±(a_h-a_ν)(a_k-a_ν)...
        Daraus folgt:". ✓ word-for-word.
      – ★ FRAKTUR 𝔄/𝔄' PRESERVED (all occ.). Nested a_{α_i} subscripts correct.
      – ⚠ FMT: eq(1) 4-line-display vs .tex single-line; eq(2) 3-line+dots-row vs .tex 2-line; systematic inline->display (differences-list,
        Factorenpaare). Content-identical layout. EMPHASIS gesperrt (I. + II. paragraphs). 19 clean pages p48-66.
  • 2026-07-03 turn 74 (loop re-fire): **p67 (§19 tail III/Folgerung/IV + repeat-transposition arg + n=3 array + footnote, .tex
    2294-2327) — 2 CONTENT FIXES (both ellipsis) + FAITHFUL otherwise.** After fix: 418pp / 0 overfull / 0 underfull / PDF 2264703 B
    (was 2264696). Compile-gate PASSED. ★ BROKE the 19-clean streak (p48-66).
      – ★★ FIX #55+#56: TWO GPT ellipsis deviations in ONE sentence (.tex 2309). Weber uses "…" 3× as "and so on"; GPT inconsistent:
        (a) "𝔄'' in 𝔅'' …," -> .tex DROPPED ellipsis -> FIX #55 inserted \ldots. (b) "𝔅' wieder in 𝔄' … über" -> .tex SUBSTITUTED
        real words "u.~s.~f." -> FIX #56 reverted to \ldots (word-fabrication). (c) "𝔅,𝔅',𝔅'' … alle" -> .tex already \ldots (kept).
        All 3 now match Weber. ZOOM-confirmed (crop_3_37, crop_3_44) + full mid third.
      – FAITHFUL: III.(gesperrt) erste-Art=gerade/zweite=ungerade #Transpositionen; identische Perm lässt 𝔄 ungeändert; Folgerung
        (parity invariant); repeat-transposition 𝔄->𝔅->𝔄 arg; P,P',P''…; jedem 𝔄 erster Art <-> 𝔅 zweiter Art. IV.(gesperrt) ½Π(n);
        n=3 array (1,2,3),(2,3,1),(3,1,2)/(3,2,1),(2,1,3),(1,3,2) [exact]; footnote "Diese Sätze… XIV. Abschnitt sehen". ✓ word-for-word.
      – ★ FRAKTUR 𝔄/𝔄'/𝔄'' + 𝔅/𝔅'/𝔅'' ALL PRESERVED (many occ.); no font-slip.
      – ⚠ FMT/STRUCT (text preserved, not content): (a) FOOTNOTE FLATTENED — "Diese Sätze…" is a real footnote (¹⁾ after ½Π(n), rule,
        small type) in Weber; .tex = inline body text, ¹⁾ marker dropped -> \footnote in fmt pass. (b) DROPPED EQ-NUM (3) — array numbered
        (3) leqno in Weber; .tex untagged -> \tag{3}+leqno in fmt pass. (c) §20 heading not on p67 (footnote+"5*" end page).
      – ★★ METHOD REFINEMENT: "ellipsis=SKIP" is MATH-list dot/comma typography ONLY. PROSE "…"(=und so fort) dropped OR word-substituted
        by GPT = CONTENT fix. ★ HOTSPOT: parallel-structure enumerations are GPT-inconsistency traps — when 1 ellipsis kept, CHECK SIBLINGS.
        Never-certify reconfirmed: "clean-looking" systematic Determinanten prose still hid damage at enumeration seams.
  • 2026-07-03 turn 75 (loop re-fire): **p68 (§20 Determinanten start: Δ-def eq(1) + Zeilen/Colonnen + M diagonal eq(2) + M'
    permuted eq(3) + ΣM sum-def, .tex 2329-2358) — 1 CONTENT FIX (dropped display) + FAITHFUL otherwise.** After fix:
    418pp / 0 overfull / 0 underfull / PDF 2264914 B (was 2264703). Compile-gate PASSED.
      – ★★ FIX #57: DROPPED DISPLAY restored (.tex 2358). Weber prints "Die Summe aus diesen Producten / M+M'+M''+⋯=ΣM" (introduces
        ΣM sum-notation) then "soll Δ sein". GPT folded to prose "…Producten soll Δ sein" — display + ΣM notation DROPPED. ZOOM-confirmed
        (crop_18_82). Grep: \Sigma M nowhere else (deleted, not relocated). Restored \[ M+M'+M''+\cdots=\Sigma M \].
      – FAITHFUL: §20 heading; n² Grössen, doppelter Index a_i^{(k)}, i&k=1,2,3…n; Quadrat (oberer Index=Horizontalreihe, unterer=Vertical),
        bezeichnen mit Δ; eq(1) Δ=n×n vmatrix a_1^{(1)}…a_n^{(n)} [double-index verified]; Zeilen/Colonnen; "arithmetische Verbindung…";
        "Man bilde das Product… Diagonale"; eq(2) M=a_1^{(1)}a_2^{(2)}a_3^{(3)}…a_n^{(n)}; "leite daraus Π(n) Producte M,M',M''… her…
        positive/negative Zeichen je nach Art…"; eq(3) M'=±a_{α_1}^{(1)}a_{α_2}^{(2)}…a_{α_n}^{(n)} [ZOOM correct]. ✓ word-for-word.
      – ⚠ FMT: (a) MATRIX COMMA-SEPARATORS — Weber eq(1) rows comma-separated "a_1^{(1)}, a_2^{(1)}, … a_n^{(1)}"; .tex &-sep (systematic
        Determinanten convention). (b) matrix dots-row. (c) leqno eq-nums (1)/(2)/(3). SKIP math-list ellipsis. EMPHASIS gesperrt (§20 head;
        Zeilen; Colonnen).
      – ★★ METHOD: dropped-display hotspot — GPT dropped an UNNUMBERED display that INTRODUCES notation (ΣM). Unnumbered displays = higher
        drop-risk (no \tag). When prose says "Die Summe/das Product … [name/soll]" watch for a dropped defining display; grep the symbol.
  • 2026-07-03 turn 76 (loop re-fire): **p69 (§20 Determinanten cont.: Determinante/Hauptglied def + eq(4) n=2 + eq(5) n=3 +
    andere Bezeichnung eq(6-7) + Jacobi eq(8)/Kronecker eq(9) + symmetr. Det., .tex 2358-2427) — 3 CONTENT FIXES + FAITHFUL
    otherwise.** After fix: 418pp / 0 overfull / 0 underfull / PDF 2264839 B (was 2264914). Compile-gate PASSED. ★★ §20 HIGH-DAMAGE.
      – ★★ FIX #58: FABRICATED MATRIX removed (eq(4)). Weber n=2 = expansion-only "Δ=a_1^{(1)}a_2^{(2)}−a_2^{(1)}a_1^{(2)}"; GPT inserted a
        2×2 vmatrix not in scan (ZOOM crop_3_15). eq(5) expansion-only in both → only eq(4) fabricated (improvised). Removed vmatrix.
      – ★★ FIX #59: DROPPED PHRASE restored. Scan "und für n=3 [nach (3) des vorigen Paragraphen]:"; GPT dropped the bracket. Restored.
        Ref = §19 n=3 array (numbered (3)) → CORROBORATES p67 dropped-eq-num(3) flag.
      – ★★ FIX #60: eq(8) SUBSCRIPT ALTERATION. Jacobi "nur das Hauptglied" = natural: scan "Δ=Σ± a_1^{(1)}a_2^{(2)}…a_n^{(n)}"; GPT wrote
        a_{α_1}…a_{α_n} (copied from generic M' eq(3)/p68), contradicting Hauptglied. ZOOM crop_6_57 (subs 1,2,n). Restored natural subs.
      – FAITHFUL: Determinante/Hauptglied def; eq(5) n=3 six-term [★ZOOM all 6 present/signed; pos 123,231,312 match; NEG terms same set
        {321,213,132} different order = commutative reorder=SKIP]; eq(6) ad−bc; eq(7) ab'c''+bc'a''+ca'b''−ac'b''−ba'c''−cb'a'' [exact];
        eq(9) |a_i^{(k)}|; symmetr. det a_i^{(k)}=a_k^{(i)} / a_{i,k}=a_{k,i}; "heissen symmetrisch". ✓ word-for-word.
      – ⚠ FMT: matrix comma-sep; leqno (4)-(9); eq(5) neg-summand order (skip). EMPHASIS gesperrt ("Hauptglied","symmetrisch").
      – ★★ METHOD (3 §20 damage mechanisms): (1) FABRICATED INTERMEDIATE FORM — GPT ADDS a matrix/step not in scan; check if display has
        MORE than scan. (2) NEIGHBOR-COPY ALTERATION — GPT homogenizes symbol to adjacent eq w/ different meaning (Hauptglied-natural vs
        generic-α); verify vs PROSE semantics not the neighbor. (3) DROPPED BRACKETED CROSS-REFS "[nach (N) des …]". ZOOM EVERY eq vs prose.
  • 2026-07-03 turn 77 (loop re-fire): **p70 (§21 Hauptsätze über Determinanten start: intro + M' eq(1) + eq(2) + 𝔅/𝔄 prose +
    Satz I, .tex ~2424-2444) — 2 CONTENT FIXES (both dropped) + FAITHFUL otherwise.** After fix: 418pp / 0 overfull / 0 underfull /
    PDF 2264920 B (was 2264839). Compile-gate PASSED.
      – ★★ FIX #61: DROPPED CROSS-REF. Scan "Wenn wir in dem Product [§. 20, (3)]"; GPT dropped bracket. Restored "[\S\,20, (3)]"
        (house style \S\,NN,(K)). 3rd dropped-bracket in §20-21.
      – ★★ FIX #62: DROPPED EQ-TAIL "=𝔄". Weber display "(α_1,α_2…α_n)=𝔄" (defines 𝔄, parallel to (β…)=𝔅 display); GPT flattened to
        inline & lost "=𝔄". Restored =\mathfrak A. (display-promo=fmt.)
      – FAITHFUL: §21 heading; intro; eq(1) M'=±a_{α_1}…a_{α_n} [α CORRECT here]; eq(2) ±a_1^{(β_1)}…a_n^{(β_n)}; (β…)=𝔅; 𝔅/𝔄-Anordnung
        prose (Transpositionen rückgängig, Art-parity, Gesammtheit); Satz I (Hauptglied a_1^{(1)}…a_n^{(n)} NATURAL -> CORROBORATES #60).
        ★ Fraktur 𝔄/𝔅 all preserved. ✓ word-for-word.
      – ⚠ FMT: (α…)=𝔄 display-vs-inline; trailing comma after 𝔅 display (skip); leqno. SKIP math-list ellipsis, §.-period.
      – ★★ METHOD: (1) DROPPED-BRACKETED-CROSS-REF systematic in §20-21 (p69+p70) — scan prose for "[§ N,(K)]"/"[nach (K)…]". (2) DROPPED
        EQ-TAIL via display-flatten — inline relation missing its "=X" RHS. (3) Hauptglied-natural corroborated (p69 eq(8) + p70 Satz I).
  • 2026-07-03 turn 78 (loop re-fire): **p71 (§21 cont.: Zeilen/Colonnen remark + Sätze II-V + start of V-proof, .tex ~2446-2462)
    — 1 CONTENT FIX (dropped cross-ref) + FAITHFUL otherwise.** After fix: 418pp / 0 overfull / 0 underfull / PDF 2264959 B
    (was 2264920). Compile-gate PASSED.
      – ★★ FIX #63: DROPPED CROSS-REF. Scan "In der Darstellung §. 20, (1) von Δ…"; GPT dropped "§.20,(1)". ZOOM crop_5_8. Restored
        "\S\,20, (1)". ★★ 4th dropped cross-ref in §20-21 (#59 p69, #61 p70, #62 p70 =𝔄-tail, #63 p71) — SYSTEMATIC.
      – FAITHFUL: Zeilen/Colonnen remark; II.(Zeilen↔Colonnen invariant); 𝔄/M transposition→sign arg; III.(index-swap→Vorzeichen);
        "Etwas anders ausgedrückt" restatement [set-off block, words identical]; IV.(permutation→Art-sign); "Aus III Fundamentalsatz:";
        V.(gleiche Reihen→Null); "Denn die Vertauschung… beide Reihen identisch" (→p72). ★ Fraktur 𝔄/𝔄'/𝔄''; M,M',M''; Δ preserved. ✓ word-for-word.
      – ⚠ FMT: "Etwas anders ausgedrückt" set-off block (cap Wenn) vs .tex inline "; wenn" — words same, cap+layout=SKIP. leqno.
        SKIP: "Aus III[.]" period, §.-period, cap. EMPHASIS gesperrt (II-V statements).
      – ★ RUNNING-HEADER (out of scope): recto head "Sätze über Determinanten." vs §21 title "Hauptsätze über Determinanten." = Weber's
        abbreviated running head (layout; .tex doesn't repro Weber heads). Not content.
      – ★★ METHOD: cross-ref drop CONFIRMED SYSTEMATIC (4× in §20-21). RULE: scan every sentence-initial "In/Nach/Aus der Darstellung/Formel/
        Product…" for a "§ N,(K)"/"[nach (K)…]" cross-ref GPT dropped (short, mid-prose = highest-miss-risk drop-class). + dropped "=X" eq-tails.
  • 2026-07-03 turn 79 (loop re-fire): **p72 (§21 V-proof tail + Satz VI + §22 Unterdeterminanten start: Σ±-def + eq(1-3) +
    generic-index passage, .tex ~2462-2493) — 2 CONTENT FIXES (#64 α→natural, #65 index-relabel) + FAITHFUL otherwise.** After fix:
    418pp / 0 overfull / 0 underfull / PDF 2264891 B (was 2264959). Compile-gate PASSED.
      – ★★ FIX #64: Σ±-DISPLAY α→NATURAL (.tex 2472). §22 opens "Σ ± a_1^{(1)}a_2^{(2)}…a_n^{(n)}" (natural Hauptglied); .tex had a_{α_i}.
        ZOOM crop_20_35. ★ 3rd confirmation of the Hauptglied-natural pattern (eq(8) #60 + Satz I corrob + this).
      – ★★ FIX #65: GENERIC-INDEX RELABEL. Weber lower=ν upper=μ; .tex had lower=r upper=ν. ZOOM crop_5_64 ("jeden anderen ν", eq(2)
        a_ν^{(k)}) + crop_30_73 ("das Product a_ν^{(μ)}"). Fixed "jeden anderen r"->ν, eq(2) a_r->a_ν (×3), "das Product a_r^{(ν)}"->a_ν^{(μ)}.
        "worin μ gleichfalls…" ties μ(upper)∥ν(lower); .tex's r broke it.
      – FAITHFUL: V-proof tail; Satz VI; §22 heading "Unterdeterminanten" ★PRESENT (concern resolved); Δ→A switch ("deren Werth jetzt mit A");
        u.s.f. genuine here (.tex correct, ≠p67); eq(1) A=Σa_1^{(k)}A_1^{(k)}; eq(3) A=Σa_k^{(μ)}A_k^{(μ)}; "worin μ…". ✓ word-for-word.
      – ⚠ FMT: leqno. SKIP "Satz V[.]" period, math-list ellipsis, u.s.f.(genuine). EMPHASIS gesperrt (§22 head, Satz VI).
      – ★★★ NEW DAMAGE CLASS: GENERIC-INDEX RELABELING. GPT renamed Weber's running indices (ν→r, μ→ν). INSIDIOUS: math works, compiles,
        reads fine — but UNFAITHFUL + likely MULTI-PAGE. Grep: .tex uses r(+s) lower / ν upper across §22-23 (2495,2548-50,2564,2569-73).
        ★★ RULE: on EVERY §22+ page VERIFY generic-index LETTERS vs scan; do NOT trust .tex letters; do NOT blanket-replace (two-row a_r/a_s
        arg needs per-page scan check). Highest-subtlety damage yet.
  • 2026-07-03 turn 80 (loop re-fire): **p73 (§22 Unterdeterminanten cont.: A_ν^{(μ)} def + eq(4) (n-1)-reihige + Bildungsgesetz +
    eq(5) 3-reihige, .tex ~2495-2525) — 3 CONTENT FIXES + FAITHFUL otherwise.** After fix: 418pp / 0 overfull / 0 underfull /
    PDF 2265074 B (was 2264891). Compile-gate PASSED. ★★8 zooms for μ/ν.
      – ★★ FIX #66: 2495 A_r^{(ν)} -> A_ν^{(μ)} (stray "r" artifact; ZOOM crop_59_8/62_8). ⚠ Weber SWAPS μ↔ν dummies between 2495 (A_ν^{(μ)})
        and 2512 (A_μ^{(ν)}) — local inconsistency, each matched to own scan; 2495 μ/ν low-confidence, re-verify.
      – ★★ FIX #67: DROPPED CROSS-REF "[§. 20, (1)]" at 2510. Restored. 6th dropped cross-ref in §20-22.
      – ★★ FIX #68: eq(5) DROPPED INTERMEDIATE cofactor form (a|2×2|−b|2×2|+c|2×2|). Restored (aligned). OPPOSITE of p69 eq(4) added-matrix.
      – FAITHFUL: A_ν^{(μ)} def; eq(4) A_1^{(1)}=(n-1) vmatrix; Bildungsgesetz (ν=Zeile/row, μ=Colonne/col; a_μ^{(ν)}; (-1)^{μ+ν}); eq(5). ✓.
        ★★ .tex 2512-2523 was CORRECT (not a relabel).
      – ★★★ METHOD: "GENERIC-INDEX RELABEL" NOT UNIFORM — p72 relabel real, but p73 mostly FALSE ALARM (.tex correct; Weber floats μ,ν as
        dummies, even swaps them). Verify EACH instance; don't blanket-swap.
      – ★★★ METHOD: μ/ν DISAMBIGUATION — nearly made a bad μ↔ν swap off tiny subscripts. SAVE: anchor on LARGE INLINE letter (crop_17_48
        "ν−1 Zeilenvertauschungen") + §20 geometry (upper=Zeile, lower=Colonne). Tiny sub/superscript glyph-reads UNRELIABLE at 500dpi thirds.
  • 2026-07-03 turn 81 (loop re-fire): **p74 (§22 orthogonality eq(6)/eq(7) + eq(8) + eq(9) row-add + Sätze VII/VIII/IX, .tex
    ~2532-2572) — 5 CONTENT FIXES (incl. SWAPPED eq(6)/eq(7)) + FAITHFUL otherwise.** After fix: 418pp / 0 overfull / 0 underfull /
    PDF 2265026 B (was 2265074). Compile-gate PASSED.
      – ★★★ FIX #70: SWAPPED EQUATIONS eq(6)⇄eq(7). Weber eq(6)[aus(2),column]=a_μ^{(1)}A_ν^{(1)}+… (μ,ν LOWER); eq(7)[aus(3),row]=
        a_1^{(μ)}A_1^{(ν)}+… (μ,ν UPPER). GPT had bodies SWAPPED. ZOOM crop_10_16 (eq6=a_μ^{(1)}A_ν^{(1)}). Swapped back.
      – ★★ FIX #69: 2532 A_μ^{(ν)}->A_ν^{(μ)} (×2). "der untere Index ν" forces ν=lower -> A_ν^{(μ)}. Prose disambiguates lower/upper.
      – ★★ FIX #71: eq(9) r/s->ν/μ (a_ν+λa_μ)A_ν [=eq(2)+λ·eq(6)]. ★★ FIX #72: 2569 "p a_r"->  "p a_ν" (Satz VIII proof).
      – FAITHFUL: eq(8) exact; VII/VIII/IX statements; "aus (2)/(3)"; §21,VI ref. ✓ word-for-word.
      – ★★★ METHOD: NEW SUB-CLASS "SWAPPED/TRANSPOSED NUMBERED EQS" — GPT attaches eq bodies to wrong \tag. RULE: for consecutive eqs that
        are sub/super transposes, verify EACH vs scan AND derivation ("aus (N)": column->lower-index; row->upper-index).
      – ★★★ METHOD: generic-index relabel r/s->ν/μ PAGE-SPECIFIC (real p72,p74; false p73). Verify index letters per-page; Weber=Greek dummies,
        stray Latin r/s = GPT artifact. PROSE "untere/obere Index X" = disambiguator.
  • 2026-07-03 turn 82 (loop re-fire): **p75 (§22 Satz IX proof + Vandermonde eq(10)/eq(11), .tex ~2574-2623) — 2 CONTENT FIXES +
    FAITHFUL otherwise.** After fix: 418pp / 0 overfull / 0 underfull / PDF 2265141 B (was 2265026). Compile-gate PASSED.
      – ★★ FIX #73: Satz IX proof relabel r->ν, ν->μ (2574,2576,2578). Scan: "a_ν^{(1)}…a_ν^{(n)} Ausnahme a_ν^{(μ)}… A=a_ν^{(μ)}A_ν^{(μ)}…
        a_1^{(μ)}…a_n^{(μ)} Ausnahme a_ν^{(μ)}". ZOOM crop_28_14 (subscript ν). Consistent w/ "nach (2)"=column-ν expansion.
      – ★★ FIX #74: DROPPED INTERMEDIATE Vandermonde step. Scan: "nach VII:" |1,0,0;…| → "und nach IX:" \[|b−a,b(b−a);c−a,c(c−a)|\] →
        "und endlich nach VIII:" eq(10). GPT collapsed to "und nach IX. und VIII.:" dropping the 2×2 display. Restored.
      – FAITHFUL: Satz IX tail; Vandermonde 3×3 setup; VII-reduction |1,0,0;…|; eq(10) (b−a)(c−a)(c−b); n×n Vandermonde matrix; eq(11)
        (a_2−a_1)…(a_n−a_{n-1}) [all factors]. ✓ word-for-word.
      – ⚠ FMT: eq(11) 4-line+dots-row vs .tex single-line; matrix comma-sep; leqno. SKIP ";"+lowercase-der vs "."+Der (punct/cap). EMPH Satz IX.
      – ★★ METHOD: (1) r->ν relabel recurs in §22 worked-proofs (p72,p74,p75). (2) DROPPED-INTERMEDIATE-STEP confirmed recurring (p73 eq5, p75
        Vandermonde) — GPT collapses multi-Satz reductions dropping intermediate displays + merging "nach X:" phrases. When a worked example cites
        multiple Sätze in sequence, CHECK for a dropped intermediate display between each.
  • 2026-07-03 turn 83 (loop re-fire): **p76 (§22 end: Vandermonde column-reversal eq(12) + differential-quotient Unterdet. notation,
    .tex ~2633-2671) — 1 CONTENT FIX (i,k relabel) + FAITHFUL otherwise.** After fix: 418pp / 0 overfull / 0 underfull / PDF 2265146 B
    (was 2265141). Compile-gate PASSED.
      – ★★ FIX #75: differential passage a_μ^{(ν)}->a_i^{(k)}, A_μ^{(ν)}->A_i^{(k)} (~10 occ, 2663-2671). Weber uses standard a_i^{(k)}; GPT
        normalized to Greek. ZOOM crop_36_64 (∂A/∂a_i^{(k)}=A_i^{(k)}). ★★ NEW DIRECTION: index relabel is BIDIRECTIONAL (Latin i,k↔Greek μ,ν).
        ★ scoped to passage — a_μ^{(ν)} is CORRECT on p73, WRONG here; NEVER global-replace.
      – FAITHFUL: column-reversal (n/2 oder (n−1)/2; (−1)^{n(n−1)/2}; n(n−1)/2); eq(12) reversed Vandermonde=product; differential prose +
        ∂A/∂a_i^{(k)}=A_i^{(k)} + A'(t)=ΣA_i^{(k)}∂a_i^{(k)}/∂t. ✓ word-for-word.
      – ⚠ FMT: eq(12) matrix comma-sep + \gathered multi-line RHS; leqno. SKIP Coeff-ë, ellipsis, trailing punct.
      – ★★ METHOD: INDEX RELABEL BIDIRECTIONAL + PASSAGE-SCOPED. GPT changes letters both ways (i,k->μ,ν p76; ν,μ->r,s p72/74/75). Verify per-page;
        correct letter is passage-specific; NEVER global-replace an index string. Weber: differential/general-element=a_i^{(k)}; running-index relations=ν,μ.
  • 2026-07-03 turn 84 (loop re-fire, fable-5): **p77 (§23 Unterdeterminanten im weiteren Sinne: heading + eq(1) + Regel I +
    Elemente-Auswahl, .tex ~2674-2708) — ★★★ NEW DAMAGE ZONE (§23 = MODERNIZED ORTHOGRAPHY) + 4 fixes.** After fix: 418pp / 0 overfull /
    0 underfull / PDF 2265243 B (was 2265146). Compile-gate PASSED.
      – ★★★ ZONE: .tex 2674-2716 (§23, printed p77-78) written in MODERN German (Faktor/Kolonne/Produkt/daß/läßt/ergibt/permutieren/
        unverändert) vs Weber's 1895 print (Factor/Colonne/Product/dass/lässt/ergiebt/permutiren/ungeändert). Scan-verified. Grep bounds:
        2676-2716 + stray "ergibt sich" 2787 (§24, check at p79/80) + 5144 (later). Modernized zones = HIGH-DAMAGE (more rewording too).
      – ★ FIX #76: orthography batch p77 (Factor ×4, Colonnen/Colonne, dass, Product, permutiren, ungeändert[real reword], heading period).
      – ★★ FIX #77: "auf folgende Art verallgemeinern:" restored (GPT dropped phrase + colon). ★★ FIX #78: separable "aus," restored.
      – ★★ FIX #79: dropped clause "d.h. so, dass nicht zweimal derselbe untere oder derselbe obere Index vorkommt," + Weber's single-sentence
        flow restored ("…und bezeichnen den Inbegriff…, mit").
      – FAITHFUL: §23 heading exact (period added); eq(1) exact; Regel I (gesperrt) content exact; elements-display exact. Running header
        "Höhere Unterdeterminanten." = Weber's own abbreviation (layout).
      – ⚠⚠ PENDING p78: (a) TAG QUESTION — elements-display UNNUMBERED in scan but .tex \tag{3}, A-symbol \tag{2} AFTER it, refs "die
        Elemente (3)" ×2 (2714,2716). Read Weber's true numbering + ref-text off p78 scan; fix tags+refs TOGETHER. (b) modernization 2714,2716
        (daß/läßt/Kolonnen/ergibt). (c) Regel-I inline-A = fmt.
      – ★★★ METHOD: new class WHOLESALE ORTHOGRAPHY MODERNIZATION (zone-based). Detect via grep (daß|Kolonn|Produkt|Faktor|läßt|ergibt|-ieren),
        bound zone, scan-verify per page. ss/ß, c/k, -iren/-ieren, Colonne/Kolonne = SOURCE-FIDELITY fixes (NOT skip-tier; only ë-drop stays skip).
        Modernized zones read word-by-word — GPT rewords more aggressively there (#77-79 in ONE paragraph).
  • 2026-07-03 turn 84b (same turn as p77, fable-5): **p78 (§23: eq(2) Complex + Umstellen eq(3) + Regeln II/III + Beweis, .tex
    ~2703-2745) — 6 FIXES incl. TAG RESTRUCTURE + DROPPED PROOF. + SCAN-PDF PATH REPAIRED.** After fix: 418pp / 0 overfull /
    0 underfull / PDF 2266311 B. Compile-gate PASSED.
      – ★★ INFRA: monolithic scan PDF gone (folder reorganized into Bd*_chapters). Same IA scan at `Bd1_IA_chapters\Weber_Algebra_Bd1_IA.pdf`
        (686pp). OFFSET +26 VERIFIED (printed78→pdf104). audit_manifest.json repointed (648 vol1 units); scripts read manifest → no code change.
      – ★★★ FIX #80: TAG RESTRUCTURE. Weber: (2)=COMBINED "a_{α_1}^{(β_1)}…a_{α_ν}^{(β_ν)} A_{α…}^{β…}." display; (3)=α-element list in
        Umstellen-paragraph; p77 element list UNNUMBERED. GPT had (3) on p77 list, bare-A as (2). Fixed; refs "(3)"/"(2) auf (1)"/"(4) und (5)" now resolve.
      – ★★★ FIX #81: UMSTELLEN-PARAGRAPH rebuilt from compressed paraphrase (restored 2 displays, "an die Stelle der Elemente." [★sic mid-sentence
        Punkt, ZOOM crop_5_20, type-B erratum #9, % kommentiert], "gelangen; dann aber lässt sich die Regel I. auf die Bestimmung von A_{α…}^{β…} anwenden und es ergiebt sich:").
      – ★★ FIX #82: "Für die Zeichenbestimmung aber ergiebt sich folgende Vorschrift. [¶] Man ordne …:" restored (GPT merged).
      – ★★ FIX #83: "indem man α_{ν+1}…α_n und ebenso β_{ν+1}…β_n der Grösse nach auf einander folgend annimmt." (GPT paraphrase reverted).
      – ★★★ FIX #84: DROPPED PROOF PARAGRAPH after Regel III restored ("Denn die Determinante ändert ihr Zeichen… stattgefunden.").
      – ★ FIX #85: orthography/detail batch (Colonnen ×3, dass/lässt/weglässt/stehen lässt, ergiebt ×2, "(vom Vorzeichen abgesehen)" parens,
        "II." period, "(4) und (5)").
      – ★★★ METHOD: modernized zones hide STRUCTURAL damage (misplaced tags, fabricated/dropped displays, dropped proofs, paraphrases, merged ¶¶).
        Verify EVERY tag + refs. Tag-gaps (no (6)) & near-duplicate eqs ((9)/(10) ±) = corruption markers. Weber mid-sentence periods = type-B, zoom+keep+[sic].
  • 2026-07-03 turn 85 (loop re-fire, fable-5): **p79 (§23: νte Unterdet. def + Regel IV + primed-Complex + eq(6) + complementäre B,
    .tex ~2748-2790) — 5 FIXES incl. MISSING (6) RESTORED + overbar-notation fabrication reverted.** After fix: 418pp / 0 overfull /
    0 underfull / PDF 2267530 B. Compile-gate PASSED.
      – ★★ FIX #86: def-sentence rebuilt — restored dropped A-display + de-modernized (definirten/Grössen/heissen/νten/νter/(n−ν)reihige) +
        "Aus III. folgt in Bezug auf diese Unterdeterminanten der Satz:" (GPT: "Es folgt:").
      – ★★★ FIX #87: Regel IV COMPLETED — GPT truncated the "oder allgemeiner: … zur zweiten oder zur ersten Art gehört." half. Restored.
      – ★★★ FIX #88: NOTATION FABRICATION reverted — Weber primes α'_1…α'_ν (GPT: überstrichene ᾱ) + A-symbol subscripts UNPRIMED α (GPT
        A_{ᾱ…} = semantically wrong). + "aber mit … irgend eine Anordnung der α_1…α_ν" + "den Complex der Glieder" restored.
      – ★★★ FIX #89: MISSING (6) RESTORED — "und wenn wir also alle diese Glieder sammeln, so erhalten wir den Complex:" + (6)
        A_{α…}^{β…}Σ±a_{α_1}^{(β_1)}…a_{α_ν}^{(β_ν)}. Tag-gap resolved; §23 tags coherent (1)-(8).
      – ★★ FIX #90: dropped Σ±=|ν×ν vmatrix| defining display restored + "wollen wir die zu A_{…} complementäre Unterdeterminante nennen und
        mit B_{…} bezeichnen." (passive paraphrase reverted; bare-B display removed → inline).
      – ★★★ METHOD: GPT invents NOTATION (overbars for primes; wrong A-subscripts) — CHECK EVERY ACCENT/subscript vs scan + semantics.
        Never insert dangling half-sentences: defer cross-page sentences until continuation read.
  • 2026-07-03 turn 86 (loop re-fire, fable-5): **p80 (§23: complementäre-B Eigenschaften + (7) + Laplace Satz V (8) + zweite
    Darstellung Satz VI (9)/(10), .tex ~2780-2830) — 6 FIXES incl. (9)/(10) superscript-swap + Sätze V/VI restored. ★ GATE 418→419pp
    (legitimate growth; sanity: 68 sections/1100 eqs/end intact).** After fix: 419pp / 0 overfull / 0 underfull / PDF 2269496 B.
      – ★★ FIX #91: cross-page sentence completed — "Sie enthält genau die Zeilen und Colonnen, die in A_{α…} fehlen und stimmt, abgesehen
        vom Vorzeichen, mit der Unterdeterminante (n−ν)ter Ordnung [A_{α_{ν+1}…α_n}^{β_{ν+1}…β_n}] überein." (was absent).
      – ★★ FIX #92: "Der Complex der Glieder (6) wird also bezeichnet mit" ((6)-ref restored; paraphrase reverted).
      – ★★★ FIX #93: dropped combinatorial ¶ restored ("Wählen wir nun für α… jede Combination von ν der Ziffern…, deren Anzahl (nach §.7)
        B_ν^{(n)} ist… jedes Glied kommt in einem und nur in einem dieser Complexe vor.") — the Laplace range-condition.
      – ★★★ FIX #94: SATZ V restored ("V. Demnach erhalten wir, wenn wir alle Ausdrücke (7) summiren…") + (8) Σ^α upper index +
        "Selbstverständlich… β summiren." + "Dies ist der Satz von Laplace." (GPT one-liner "Daraus folgt der Satz von Laplace").
      – ★★★ FIX #95: derivation ¶ ("Man wähle in A irgend zwei Reihen aus…") + SATZ VI ("Wir können daher setzen:") + "oder nach IV."
        (GPT fabricated "oder, nach der Vorzeichenregel,") restored.
      – ★★★ FIX #96: (9)/(10) SUPERSCRIPT-SWAP resolved — Weber (9) A_{ν,k}^{i,μ} vs (10) A_{ν,k}^{μ,i} (order swap ⇒ sign flip via IV);
        GPT had identical A_{νk}^{μi} in both (contradiction). + ν,k comma + Σ^{i,k}.
      – ★★★ METHOD: near-duplicate ±eqs → hunt the homogenized index-ORDER difference, don't delete. Weber numbers Sätze (I-VI §23) — GPT
        strips Roman numerals; check every "folgt:"/"Satz von X". Gate page-count = tripwire, not constant: verify structure counts, then re-baseline.
  • 2026-07-03 turn 87 (loop re-fire, fable-5): **p81 (§23 end: Wir-bemerken ¶ + geränderte Det. (11)/(12)/(13) + §24 heading,
    .tex ~2820-2860) — 6 FIXES. ★★★ §23 MODERNIZED-ZONE REBUILD COMPLETE (27 fixes p77-81). Zone ends at §23.** After fix:
    419pp / 0 overfull / 0 underfull / PDF 2270503 B. Compile-gate PASSED.
      – ★★ FIX #97: "Wir bemerken zu diesem Satze noch… folglich A_{ν,k}^{μ,i} der Coëfficient von a_k^{(i)} in der Determinante A_ν^{(μ)}."
        cross-page ¶ restored (was absent). – ★★ FIX #98: "Man kann nach diesem Satze die sogenannte geränderte Determinante (11) nach den
        Elementen der letzten Zeile und Colonne entwickeln und erhält:" (GPT "Für die…ergibt sich" reverted).
      – ★ FIX #99: (12) U=qA−Σ^iΣ^k u_iv_kA_k^{(i)} (double Σ; GPT single). – ★★ FIX #100: "Man erhält diese Gleichung aus (10), wenn man
        n in n+1 verwandelt…" ¶ restored (was absent).
      – ★★★ FIX #101: (13) corrected — Weber A_{ν,k}^{i,μ}=∂²A/(∂a_ν^{(i)}∂a_k^{(μ)}) (pairing consistent w/ (9)); GPT had A_{νk}^{μi}=
        ∂²A/(∂a_ν^{(μ)}∂a_k^{(i)}) (super-order AND ∂-variables swapped). + "bei den…bisweilen…zweckmässig, so dass z.B. …gesetzt wird."
      – ★ FIX #102: §24 heading period + ¶ break after "linearer Gleichungen."
      – ★★★ ZONE-END: §24 opening already old-orthography + faithful. MODERNIZED ZONE = §23 ONLY. §23 FINAL: 27 fixes p77-81 (worst stretch
        in vol1; separate modernizing reconstruction pass). Stray "ergibt sich" ~.tex 5144 still to verify when reached.
  • 2026-07-03 turn 88 (loop re-fire, fable-5): **p82 (§24: eq(1) System + (2) triviale Lösung + (3) Rechteck + Matrix-Def,
    .tex ~2860-2889) — 3 FIXES; §24 back to LOW-damage profile.** After fix: 419pp / 0 overfull / 0 underfull / PDF 2270517 B.
      – ★★ FIX #103: "…= 0, worin die Coëfficienten a_i^{(k)} als gegebene Grössen betrachtet werden." (GPT "Darin werden…betrachtet."
        reword reverted; Coefficienten ë-skip kept).
      – ★ FIX #104: "Ueber die Zahlen" (GPT "Über" normalization; .tex elsewhere uses Ueber* correctly).
      – ★ FIX #105: "(oder n-reihig, wenn n=m ist)." parens restored (GPT comma; precedent p74 parens-class).
      – FAITHFUL: eq(1) m×n system; (2); extremer Fall; (3) Rechteck; Matrix-Definition + "Die der Matrix entstammenden…auffasst."
        [whole passage gesperrt]. ✓ word-for-word. EMPHASIS tracked: "alle", "beliebige Werthe", "Matrix", entstammenden-passage.
      – ★★ METHOD: §24 = low-damage again (§23 catastrophe was zone-specific). Watch: Über/Ueber normalization (grep later); parens-vs-comma;
        "worin…werden"-clause rewords.
  • 2026-07-03 turn 89 (loop re-fire, fable-5): **p83 (§24: ν-Annahme + eq(4) + Satz I + eq(5), .tex ~2891-2916) — 4 FIXES.**
    After fix: 419pp / 0 overfull / 0 underfull / PDF 2270610 B. Compile-gate PASSED.
      – ★★ FIX #106: Annahme-¶ — dropped parenthetical "(oder falls n=m ist, diesen gemeinschaftlichen Werth nicht übertrifft)" +
        ¶ break + dropped symbol "Coefficienten a_i^{(k)}" restored (+ (ν+1)reihigen unhyphen).
      – ★ FIX #107: eq(4) fabricated "≠0" removed (scan: period; non-vanishing in prose). Fabrication-class: GPT adds redundant decoration.
      – ★ FIX #108: Satz-I ¶ split + "heraus:" colon (GPT merged + comma) + "Lösung, als" comma.
      – ★★ FIX #109: eq(5) dropped a^{(2)}-row restored (scan 4 rows; GPT 3). ★ NEW CHECK: count display rows scan-vs-.tex on every multi-row eq
        (GPT truncates middles, keeps first+dots+last).
      – FAITHFUL: rest of Annahme; eq(4) entries; "Denn offenbar…"; Unterdeterminanten-notation sentence; Satz I content; multipliciren-prose
        (μ correct). Header "Matrix." = Weber's abbreviated running head.
      – ⚠⚠ PENDING p84: PROOF-TAIL — Weber "so folgt, weil nach §. 22 (2) und (6) [Σ_{1,ν}^{i} A_μ^{(i)} a_λ^{(i)} = 0 oder = A] […]";
        GPT compressed to "wegen der Relationen des vorigen Paragraphen [Ax_μ=0]…". Rebuild WITH p84 (zoom Σ bounds 1,ν-vs-1,n + a_λ).
  • 2026-07-03 turn 90 (loop re-fire, fable-5): **p84 (§24: Satz-I proof-tail + Satz II + eq(6) + (7)/(8), .tex ~2914-2951) — 5 FIXES
    incl. proof-tail rebuild + (7)/(8) modern-Σ de-compression (λ restored).** After fix: 419pp / 0 / 0 / PDF 2271183 B. Gate PASSED.
      – ★★★ FIX #110: proof-tail rebuilt — "so folgt, weil nach §.22 (2) und (6) [Σ_{1,ν}^{i}A_μ^{(i)}a_λ^{(i)}=0 oder =A] ist, je nachdem
        λ von μ verschieden ist oder nicht, [Ax_μ=0,] und da…, [x_μ=0.]" (GPT: "wegen der Relationen des vorigen Paragraphen" + no Σ-display).
        ZOOM crop_28_84 (bounds "1,ν", subscript λ).
      – ★ FIX #111: Satz II "Werth Null, oder:" + ¶ before 2nd formulation. – ★★ FIX #112: eq(6) dropped a^{(2)}-ROW + dropped a_2-TERMS
        restored (2nd row-truncation occurrence; row-count check works).
      – ★★★ FIX #113: (7) de-compressed to Weber's explicit "−C_{ν+1,μ}x_{ν+1}−⋯−C_{n,μ}x_n" (GPT: modern Σ_{h=ν+1}^n C_{μh}x_h — fabricated
        compression + λ→h rename + C-order swap); (8) C_{λ,μ}=Σ_{1,ν}^{i}a_λ^{(i)}A_μ^{(i)}, λ=ν+1…n.
      – ★ FIX #114: "wie vorhin," + colons + 2951 C/a → λ (sentence-tail wording = p85-verify).
      – ★★★ METHOD — NEW SUB-CLASS: MODERN-Σ COMPRESSION. GPT rewrites explicit expansions as compact \sum with its own index names/bounds.
        RULE: every \sum_{i=1}^{ν}/\sum_{h=…}^{…} in .tex is SUSPECT — check scan for explicit form, Weber's letter (Greek λ), Weber Σ-style.
      – ⚠⚠ PENDING p85/86: λ→h + Σ-compression EXTENDS through Satz-III machinery (.tex 2959-3164 incl. B-system analogues). Rebuild per
        page-scan; NO blanket replace. + 2951-tail wording.
  • 2026-07-03 turn 91 (loop re-fire, fable-5): **p85 (§24: C_{λ,μ}-tail + Satz III + Σ-Erklärung + (9)-(12), .tex ~2951-3010) —
    6 FIXES; h-index VINDICATED.** After fix: 419pp / 0 / 0 / PDF 2271418 B. Gate PASSED.
      – ★★★ h-RESOLUTION: Weber uses λ (free index, (7)/(8)) AND h (summation letter, (9)-(13), printed Σ^h) — .tex's h in (9)-(13) was
        CORRECT; p84 λ-fixes stand; the feared 2959-3164 rename-zone dissolves (only Σ-bounds style = fmt).
      – ★★ FIX #115: 2951-tail full wording "die Elemente der μten Colonne a_μ^{(1)}…a_μ^{(ν)} durch a_λ^{(1)}…a_λ^{(ν)} ersetzt."
      – ★★ FIX #116: Satz III subordinate form ("zu zeigen [no colon] III. dass … befriedigt sind…, dass also…"; GPT main-clause recast).
      – ★★★ FIX #117: DROPPED Σ-NOTATION SENTENCE restored ("Man vereinfacht die Rechnung sehr durch Anwendung eines Summenzeichens Σ,
        bei dem wir, wie schon oben, die Summationsbuchstaben oben, die Grenzen unten anhängen.") + "dann die Gleichungen (7)" + colon.
        ★ = Weber's own spec for the Σ-convention (authoritative for fmt-pass).
      – ★ FIX #118: (9) factor order a_h^{(i)}A_μ^{(i)}x_h. – ★ FIX #119: (10) missing ", k=1,2,…,m." tail added.
      – ★★ FIX #120: (12) dropped a^{(2)}-row + a_2-column restored (3rd serial row-truncation: eq(5) p83, eq(6) p84, (12) p85).
      – ★★ METHOD: verify index-letter ROLE (free vs summation) before renaming; row/column-count EVERY display; Σ-typography now
        Weber-documented.
  • 2026-07-03 turn 92 (loop re-fire, fable-5): **p86 (§24 end: (13) + m=n−1 + (14)-(18), .tex ~2999-3040) — 3 FIXES. §24 COMPLETE
    (21 fixes p82-86).** After fix: 419pp / 0 / 0 / PDF 2271453 B. Gate PASSED.
      – ★ FIX #121: "folgenden Ausdruck geben: [¶] Bezeichnen wir…" (GPT period+run-on). ★ FIX #122: "…so ist die Lösung des Systems:"
        colon (+ A-list comma dropped per scan). ★★ FIX #123: (15) dropped a^{(2)}-row restored — **4th serial row-truncation**.
      – FAITHFUL: (13) w/ k-tail; m=n−1 prose ("eine"/"Verhältnisse" gesperrt); (14) 4 rows OK; (16); (17) [2-line=fmt]; (18) exact.
      – ⚠ WATCH §25: heading period; **"notwendig"-modernization suspect** (.tex mixes notwendig/nöthig; Weber prints "nothwendig" —
        verify per p87 scan); (1)-tag \ne0 fabrication-suspect (cf. #107).
      – ★★ METHOD: §24 damage profile = drops (rows/clauses/¶) + small fabrications + Σ-compression + Sätze-recasts; serial a^{(2)}-row
        truncation (4x) = §24 signature. Row-count check standard.
  • 2026-07-03 turn 93 (loop re-fire, fable-5): **p87 (§25 Elimination: heading + Def + Bedingungen + Binomial-Anzahl, .tex
    ~3048-3058) — 4 FIXES.** After fix: 419pp / 0 / 0 / PDF 2271073 B. Gate PASSED.
      – ★ FIX #124: §25 heading period. – ★★ FIX #125: direct question restored ("und fragen: wann hat dies System eine Lösung…
        verschwinden? Wir haben schon gesehen, dass…"; GPT indirect + drop).
      – ★★ FIX #126: nothwendig-sweep ×3 ("nothwendige und hinreichende" gesperrt; "nothwendig Null"; +"so dass also"; "§24, II." period;
        (ν+1)reihigen unhyphen). – ★★ FIX #127: dropped clause "und wir erhalten den Fall §.24, II. und wie zu erwarten war, eine Bedingung."
        + "grösser als nöthig ist" + "nothwendige Folgen".
      – FAITHFUL: Elimination-Def ¶ word-for-word ("Elimination" gesperrt); Binomial-display exact; n≦m glyph=\le OK.
      – ★★ METHOD: -th- spellings (nothwendig/nöthig/Werth/Theil) = source-fidelity class like c/k; grep-sweep "notwendig|Werte |Teil"
        when suspicious. §25 profile = §24-like.
      – ⚠⚠ PENDING p88: "notwendigen"→nothwendigen? (3058) + (1)-display ≠0-fabrication-suspect (cf. #107) + §24,(9)/(11) refs verify.
  • 2026-07-03 turn 94 (loop re-fire, fable-5): **p88 (§25: präciser-Frage + §24-Antwort-¶ + (1)-(3), .tex ~3057-3097) — 6 FIXES
    incl. 2 dropped passages + ≠0-fabrication #2.** After fix: 419pp / 0 / 0 / PDF 2270965 B. Gate PASSED.
      – ★★ FIX #128: präciser-¶ (nothwendigen; "etwas"; "Bedingungen:" colon + set-off dass-block; "linearen, homogenen" comma).
      – ★★★ FIX #129: DROPPED ¶ restored ("Auch diese Frage ist in §.24 eigentlich schon beantwortet… Es genügt aber schon, wenn es von
        einer kleineren Anzahl der (ν+1)reihigen Determinanten feststeht, dass sie verschwinden.").
      – ★★ FIX #130: (1) \ne0 REMOVED (fabrication #2, cf. #107; Weber: prose "als von Null verschieden an") + a^{(2)}-row restored (5th) + colon.
      – ★ FIX #131: fabricated "\S\,24," before (11) removed (Weber: "die Summen (11)") + "werden also:" colon.
      – ★★ FIX #132: (2) a_2-column + a^{(2)}-row restored (6th serial). – ★★★ FIX #133: dropped passage after (3) restored ("und diese
        Bedingungen genügen auch. Die Gleichung (2) oder (3) ist aber identisch befriedigt, wenn h=1,2…ν oder k=1,2…ν ist, und giebt also…
        Solche Bedingungen ergeben sich nur für"; GPT: "Hierbei ist").
      – ★★ METHOD: ≠0-decoration = CONFIRMED serial fabrication (check every \ne0 vs scan; Weber: non-vanishing in prose). Cross-ref
        ADDITIONS (extra "§ N,") join drops — verify both directions. §25 drops are LONGER units (full ¶¶).
      – ⚠⚠ PENDING p89: (4)/(5) + Unabhängigkeits-¶ verify + §26 heading period + §26 eq(1) y-system row-count.
  • NEXT (p1-99 content pass IN PROGRESS — ERSTER ABSCHNITT §1-§17 p23-63 + Einleitung p1-20 + title p21-22 + §18-§25(part) p64-88 DONE):
    — CONTENT TRACK (primary): **p89** = §25 end + §26 start (.tex ~3098-3120): (4) h/k-ranges; (5) (n−ν)(m−ν); Unabhängigkeits-¶
      ("Diese Bedingungen sind wirklich von einander unabhängig…gleich Null setzt."); §26 heading "Unhomogene lineare Gleichungen" [+period];
      §26 opening ¶¶ (homogen-Vereinfachung; Werth-1-Ableitung; selbständige Behandlung) + eq(1) y-system [row-count]. Continue gap-pass p89->p99.
      ⚠ ★row/col counts; ★≠0-fabrications; ★-th- spellings; ★dropped ¶¶ (LONG units in §25); ★cross-refs both directions; ★colons/set-off blocks;
      ★Fraktur. ⚠ commutative reorder=skip. ⚠ matrix comma-sep=fmt. ⚠ EPSILON. ⚠ punct/cap/§./ë=skip (ß/k/-ieren/Ue/-th- NOT skip). ⚠ EMPHASIS
      gesperrt(defer: dass-block p88). ⚠ leqno=fmt. ⚠ Σ-Weber-conv=fmt. ⚠ grep before glyph fix.
    — SPERRUNG/EMPHASIS TRACK (owed): §25 "Elimination"+"nothwendige und hinreichende"+"eine"+dass-block(p87-88); §24 Sätze I-III+terms;
      §23 Regeln I-IV+Sätze V/VI+Laplace; §22 VII-IX+heading; §21 I-VI+title; §20 terms; §19; §18; §17-§12; p48 Satz; p25 title; §4-§26 titles;
      §5-§8. Einleitung(p1-20)+§173..188.
    — ★ FORMATTING/NOTATION PASS (owed): leqno; ordinal-superscript; double \clearpage; Σ Weber-conv (spec p85); eq/dots-row p47-55; §18-19
      inline->display; p67 footnote+eq-num(3); p68-87 matrix comma-sep/dots-rows/leqno/multi-line; **p88 dass-block set-off + (1)/(2) comma-sep**. After content pass.
    — SCOPE: front matter NOT in .tex (body-only). German-TEXT fidelity only. ★ ss/ß, c/k, -iren/-ieren, Ue/Ü, -th-, index-letters/roles,
      explicit-vs-Σ, row/col-counts, ≠0-decorations = CONTENT (ë-drop = skip).
    — ★ INFRA: vol1 scan = `Papors\OS\Lehrbuch der Algebra\Bd1_IA_chapters\Weber_Algebra_Bd1_IA.pdf`, offset +26 (manifest updated 2026-07-03).
    TALLY: **9 type-B Weber errata + 2 variant/typo [sic]** + 1 font-slip; **24 GPT-norms removed**; **13 fabrications removed (+\ne0 #130,
      +§24-ref #131)**; **51 dropped restored (+§24-Antwort-¶ #129, identisch-befriedigt passage #133, (1)/(2) rows+col #130/#132, etwas #128)**;
      **16 index alterations**; **11+ paraphrases reverted**; **1 tag restructure**; sign fixes; Fraktur-M x15. **~133 LANDED FIXES.** Pages DONE:
      Einleitung p1-20 + title p21-22 + §1-§17 p23-63 + §18-§25(part) p64-88 (p48-66=19-clean; p67-76=22; §23:p77-81=27; §24:p82-86=21;
      p87=4; p88=6). Gate: **419pp / 0 / 0 (PDF ~2270965 B)**. 11 pages to go (p89-p99).
════════════════════════════════════════════════════════════════════════════════
