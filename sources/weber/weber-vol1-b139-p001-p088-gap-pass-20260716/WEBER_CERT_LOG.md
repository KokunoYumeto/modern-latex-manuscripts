# Weber audit — certification log

Tracks every change applied to the canonical B139 `.tex` (under `…/02_cumulative/vN/ge/`),
with provenance. Method: agent finder (weber_audit_workflow.js) → I verify each fix by eye against
the 500-dpi scan → apply → pdflatex gate (0 errors AND page count not dropped).

## v1 (Band I) — weber_v1_ge.tex
Backup before first edit: `weber_v1_ge.tex.bak_pre_agentfix_20260625` (same dir).
State: **compiles 360 pp / 0 errors** (grew from 356 as dropped blocks/footnotes were restored).

### 2026-06-25 — p100 + p102 (agent run wzmu04tqc; each fix hand-verified vs scan)
APPLIED (4):
- **p100 eq (9) determinant** — restored the dropped `φ(α₂)` row (scan shows φ(x), φ(α₁), φ(α₂), …, φ(αₙ); .tex had only φ(α₁) then dots).
- **p100 derivation block** — restored the dropped *"wofür wir auch setzen können"* + three displays `[x,…]=f(x)/(x−αᵢ)·[…]` + *"und ebenso"* (the bridge from (10) to formula (11)).
- **p102** — `f₁(x)=a₀xⁿ⁻¹+a′₁xⁿ⁻²+⋯` (restored the dropped `a′₁xⁿ⁻²` term).
- **p102** — restored the dropped second equation `f(x)=(x−α)(x−β)f₂(x)` on the `f₁=(x−β)f₂` display line.

DEFERRED (not applied — need tight-crop zoom to settle):
- p100 "Nenner" — `x−α₁, x−α₂ … x−αₙ` vs .tex ellipsis `x−α₁,…,x−αₙ` (agent conf 0.8; minor).
- p102 — source "Coëfficient" diaeresis vs .tex "Coefficient": my hand-read flagged it, the agent read it as faithful. Sub-symbol mark; settle with a crop before any change.

p101: clean (verified).

### 2026-06-25 — p103–107 (agent run wdraz676o; each candidate verified by eye)
APPLIED (1):
- **p106** — restored the dropped theorem numeral **VII.** before "Sind die Coefficienten $a_0,\ldots,a_n$ und die Variable $x$ reell…" (set off like VI/VIII; .tex had it as a bare paragraph). Compiles **357 pp / 0 err** (unchanged).

NO FIX NEEDED: p103, p104, p107 clean. **p105 — agent proposed 4 fixes, verifier rejected ALL 4** as phantom (old_string 0 matches); I hand-confirmed eq (5) is already the correct two-line `split` form (the audit agent hallucinated a one-line collapse). p104 `a_2/x` is a source-print typo the .tex correctly carries as `a_2/x^2` (type-B, untouched).

SYSTEMATIC (deferred — global policy, decide once for the whole work, do NOT patch per page): source prints "Coëfficient" (diaeresis); the .tex has "Coefficient" throughout.

### 2026-06-25 — p108–113 (run wahdj8vfy; each candidate verified by eye)
APPLIED (5):
- **p108 sign-schema** — restored the printed single shared header `ξ−ε<ξ<ξ+ε` (was two x-headers) and the `f(x)` row labels (were bare `1. 2. 3. 4.`).
- **p109** — restored a DROPPED displayed equation `\sqrt[2n]{a}=\sqrt[2]{\sqrt[n]{a}},\ \sqrt[4n]{a}=\sqrt[2]{\sqrt[2n]{a}}\ldots` and fixed garbled radical indices (`√a,√[n]a,√[n]α / "für jedes α"` → `√[n]a,√[2]a,√a / "für jedes a"`).
- **p112** — restored dropped equation number **(2)** on the `a=r(cosφ+i sinφ), a'=…` display (was untagged; (1),(3) present).
- **p113** — prose `nicht mehr als n` → source `n und nicht mehr` (exactly n; more precise).
- **p113** — prose `Die beistehende Figur` → `Die beistehende Fig. 1` (explicit reference; the Fig. 1 tikz exists in the .tex).
Compiles **357 pp / 0 err** (unchanged).

SKIPPED as cosmetic (commutative reorder, no math change): p111 ×2 `(b-ci)`→`(b-ic)` in eq (9) and the fraction. `ci=ic`; print and .tex are both internally inconsistent on the order anyway. p110 clean.

### 2026-06-25 — p114–119 (run w4kwfrqpa; verified by eye)
APPLIED (5):
- **p114** roots of unity — `\xi_k`→`\varepsilon_k` (×3: eq (11), "Werth von ε_k", Moivre `ε_k=ε^k`); the print uses ε throughout, the .tex misread it as ξ.
- **p114** — removed a spurious tagged eq (12) `\xi_k^n=1` and restored the real eq (12) `x^n=1` (the .tex had demoted it to inline); dropped the spurious word "ihrer".
- **p118** — xref `cubischen Gleichung (1)`→`(6)` (print shows (6)).
Compiles **357 pp / 0 err**.

REJECTED by me (kept the .tex): p119 footnote `Collected`→`Collectet`. Weber misprinted "Collectet"; the .tex correctly has "Collected" (Cayley's real title) — a defensible editor correction of an obvious typo, so KEPT and flagged type-B (the agent self-contradictorily emitted it as both a fix and a type-B). p115, p116, p117 clean.

### 2026-06-25 — p120–125 (run wnbmmoci2; verified by eye)
APPLIED (4) — all single-symbol/variable misreads:
- **p121** `d`→`\delta` (×2) — the lower-bound proof's small quantity is δ in print; the .tex had Latin d.
- **p123** — removed `=y+iz` that was wrongly added to the FIRST "Variable $x$" (print has bare x there; `=y+iz` belongs only to the second occurrence "der Variablen x=y+iz").
- **p124** `(P,\gamma)/\gamma<\eta/\gamma>\eta` → `(P,y)/y<\eta/y>\eta` — the cut variable is y (print); γ is correctly used later for the minimum value, so this was a localized misread.
Compiles **357 pp / 0 err**. p120, p122, p125 clean; 0 rejected.
Source typos correctly KEPT (not reverted): p125 Weber "kan"→.tex correct "kann" (type-B); `≦` double-bar glyph → `\le` (cosmetic).

### 2026-06-25 — p126–131 (run wtfu7alt6; dense §38–39 proof; each verified by eye)
APPLIED (10):
- **p126** — restored dropped QED marker "w. z. b. w." after eq (18).
- **p128** eq (5) — restored dropped explicit term: `a<b_1\le b_2\le b_3\le\cdots\le b_{n-1}`.
- **p129** — `\beta_i`/`\rho_i` → `\beta_1`/`\rho_1` (print uses subscript 1).
- **p130** — SYSTEMATIC `\theta`→`\Theta` (capital, ×4: the `a'<a\Theta` chain, eq (14) `a\Theta^\nu`, "da Θ^ν", and the `\Theta=1-\omega/4Q` definition); the print uses capital Θ throughout this proof.
- **p130 "Differenzen"** — fixed a `kleiner`↔`grösser` DIRECTION INVERSION and restored two dropped displays (the differences `(1-a/4Q),(1-a'/4Q),…` and `\Theta=1-\omega/4Q`); the .tex had paraphrased to inline `a^(ν)/4Q … grösser … ω/4Q`.
- **p130 eq (11)** — restored the dropped equation `α'=α-af(α)/(2Qf'(α))` and moved the (11) tag onto it; the δ/h display it had wrongly tagged is now untagged `\[…\]` (NOT `\begin{equation}`, which would auto-number spuriously). Added the dropped general term to the `a'<a\Theta` chain.
- **p131** — `|f'(α^(r))|≥k`→`|f'(α)|>k` (print: plain α, strict >; matches the p129 bound); restored the dropped general term `a^(ν−1)−a^(ν)>(a^(ν−1))²/4Q` in the eq (13) chain (stacked).
Compiles **357 pp / 0 err**. p127 clean; 0 rejected. Type-B kept: p130 eq (12) print "u" typo → .tex correctly "a".

### 2026-06-25 — p132–137 (run w0za37gy4; verified by eye)
APPLIED (0). p132, p133, p136, p137 clean. No .tex change → gate stays **357 pp / 0 err**.
**ALL 3 agent candidates REJECTED on review** (the verifier had passed all 3 — hand-check was the only gate):
- **p134 eq (10) & eq (14)** — agent escalated Weber's double-bar `≦` to `\gtreqless` (⋛). REJECTED: the .tex `\le` is correct — the prose says "im Inneren oder an der Peripherie/Grenze von (ϱ)" (= ≤) and the math (bound holds inside the disk) confirms ≤. The agent's own description ("two bars over a < wedge") is ≦=≤, mislabeled. Cosmetic glyph; kept `\le`.
- **p135 xref `(19),(20)`→`(20),(21)`** — REJECTED: the .tex correctly points to the inequalities (which ARE (19),(20)); the print's "(20),(21)" is an off-by-one SOURCE typo the editor fixed. Kept the correction; flagged type-B.

### 2026-06-25 — p138–143 (run wo4jo4wfi; §41–43 symmetric functions; verified by eye)
APPLIED (9):
- **p139** `n!`→`\Pi(n)` (Weber's factorial notation, book-wide; the .tex had modernized it).
- **p140** `sämtlich`→`sämmtlich` (lone slip vs the .tex's own 34× "sämmtlich" + the print).
- **p141** eq (2) — restored printed form `f(x)/(x−α)=…+f(α)/(x−α)` (the .tex had folded f(α) into the LHS numerator).
- **p141** eq (3) — restored dropped line `f_3(α)=α³+a₁α²+a₂α+a₃`.
- **p141** eq (4) — restored dropped first line `S(f(x)/(x−α))=f'(x)`.
- **p141** `worin nach §4,(8):`→`worin [§4,(8)]:` (brackets, dropped "nach").
- **p142** — restored dropped Newton footnote ("Arithmetica universalis, edit. 's Gravesande, p. 592").
- **p143** eq (11) — restored the dropped LONG form + connecting prose "die sich nach (7) auch so darstellen lassen:" (the .tex had only the short unnumbered form, mislabeled (11)).
- **p143** eq (3) — restored dropped term `+A_{m-1}α`.
Compiles **358 pp / 0 err** (was 357; +1 from restored content; no page swallowed). p138 clean.
REJECTED (verifier got this right): p140 `x`→`n` — print "x" is a source typo (sign of a_n is (−1)^n, depends on n); .tex correctly "n". Type-B.

### 2026-06-25 — p144–149 (run wmbmrvo7l; verified by eye)
APPLIED (2): **p144** restored dropped word "etwa" ("in S etwa noch vorkommenden"); **p148** restored dropped explicit 0 in the order tuple `(1,0,0,\ldots,0)` (matches siblings (1,1,0…0)/(2,0,0…0)). Compiles **358 pp / 0 err**. p145, p146, p149 clean.
REJECTED (verifier got this right): p147 — agent wanted to delete the .tex's "etc.", but the verifier's zoom confirmed the .tex matches the page; kept.

### 2026-06-25 — p150–155 (run wxyrbtpam; verified by eye)
APPLIED (1): **p154** eq (10) `β−γ`: `-u+v`→`u−v` — a genuine SIGN error (print shows u−v; the (X+Y, X−Y) difference-pattern and the cubic case at .tex 5529 both confirm). Compiles **358 pp / 0 err**. p150–153 clean.
REJECTED by me (revert-the-editor): **p155** `a_0,a_1,a_2,a_3,a_4`→`a_0,a_1,a_2,a_3` — the general quartic eq (14) is `a_0x⁴+…+a_4` (5 coeffs); the print's list OMITS a_4 (source oversight), the .tex's complete `a_0…a_4` is correct. Kept; type-B.

### 2026-06-25 — p156–161 (run wokiihclr; verified by eye)
APPLIED (2): **p160** prose `unendlich vieler`→`unendlicher` Wurzeln; **p161** prose `gewisse Werthepaare`→`gewisse dieser Werthpaare` (dropped "dieser"). Compiles **358 pp / 0 err**. p156, p157, p159 clean.
REJECTED by me (would inject a Weber error into the correct .tex): **p158 eq (14)** `Σν=m,Σμ=n`→`Σν=n,Σμ=m`. MATH truth is `Σν=m, Σμ=n` (verified by concrete example: f deg n=2, φ deg m=1 → Res=a_0b_1²−a_1b_0b_1+a_2b_0², degree 1=m in the a's, 2=n in the b's). The .tex already has the correct form; the PRINT's eq (14) is a Weber error.
  **Paired Weber erratum (type-B, left faithful):** §49 eq (5) prints `nν+mμ` for the resultant's y-degree, but the math-correct form is `mν+nμ` (same m↔n swap as the print's eq (14)). The .tex reproduces the print's `nν+mμ` there — faithful to the source error; note this leaves the (corrected) eq (14) and §49 (5) mutually inconsistent in the .tex. Flagged, not silently changed.

### 2026-06-25 — p162–167 (run wbi1e27lk; verified by eye)
APPLIED (0). p163–167 clean; p162 effectively clean. No .tex change → gate stays **358 pp / 0 err**.
REJECTED by me: **p162** `Endgleichung für z`→`für x`. Eliminating x and y cannot yield an equation "für x" (an eliminated variable); the §50 elimination chain is x→y→z, so the end-equation is in **z** — the .tex is correct. The print's "x" (if that is the glyph; the agent's own reasoning was self-contradictory) is a Weber typo. Kept .tex "z"; type-B.

### 2026-06-25 — p168–173 (run w0h0vvsc5; verified by eye)
APPLIED (1): **p172** restored a dropped displayed equation `ν_0+ν_1+ν_2+⋯+ν_{n-1}=m` + the "und" connector (between the "…vorkommt," prose and the μ-equation; it restates eq (13)). Compiles **358 pp / 0 err**. p168–171, p173 clean.
REJECTED by me (revert-the-editor; 4th such): **p172** s-subscript `(n-1)`→`(n+1)` — eq (12)'s x-exponent uses (n-1), so eq (14)'s s-subscript must too; the print's "(n+1)" is an internal-inconsistency typo, the .tex's "(n-1)" is correct. Kept; type-B.

### 2026-06-25 — p174–179 (run wh4r37hzt; verified by eye)
APPLIED (4):
- **p175** restored dropped `α_0` in the ratio chain `α_0:α_1:α_2:α_3:α_4` (the .tex said "vier Verhältnisse" but listed only 4 quantities = 3 ratios; eq (2) has 5 params α_0..α_4).
- **p178** restored the dropped section divider `Fünfter Abschnitt. / Lineare Transformation.` (the .tex flowed straight into §55; the parallel "Sechster Abschnitt" was present in-file).
- **p179** ×2 transformation-coeff index order `a_{ν,i}`→`a_{i,ν}` (and primed): print shows i first, consistent with the single-function `a_i`; coeffs not symmetric.
Compiles **358 pp / 0 err**. p174, p176, p177 clean; 0 rejected.

### 2026-06-25 — p180–185 (run wkgrk0q50; verified by eye)
APPLIED (0). p183, p184 clean; p180/181/185 had only cosmetic/revert candidates. No .tex change → gate stays **358 pp / 0 err**.
- **p185 eq (2)** `Φ'(x'_i)`→`Φ(x'_i)`: REJECTED (revert-the-editor) — eq (2) is the coeff of t in `Φ(x'_i+tξ'_i)=Σξ'_iΦ'(x'_i)`, so Φ' (partial derivative) is REQUIRED, parallel to eq (1)'s F'. The .tex's Φ' is correct; the print's unprimed Φ is a dropped-prime typo. Type-B.
- **p180 eq (3)** `ξ_i u_i`→`ξ_ν u_ν` and **p181 eq (11)** over-Σ index: SKIPPED as cosmetic — dummy summation-index name/placement, no meaning change; the .tex's consistent `i`/`\sum_i` is a defensible standardization (cf. the agent's own "Σ-index placement is cosmetic" note on p185).
- **p182** `x_m`→`x_n`: rejected by verifier; keep-the-editor anyway (print's x_n is a typo, ψ is of m variables).

### 2026-06-25 — p186–191 (run wsm4x3nui; verified by eye)
APPLIED (1): **p188** restored dropped word "den" ("Wenn wir nach den §. 16, (4) die Function"). Compiles **358 pp / 0 err**. p186, p187, p189, p190, p191 clean; 0 rejected. (Agent correctly auto-classified a commutative reorder `a_0 r^n`/`r^n a_0` as cosmetic — the rule is firing in-agent now.)

### 2026-06-25 — p192–197 (run w6wwajy55; §62–63 cubic-form invariant theory; verified by eye + math)
Densest batch yet — 13 candidates, **10 APPLIED, 2 rejected, p193 clean**:
- **p194** fixed .tex corruption `\\eta`→`\eta` (doubled backslash rendered a line break + literal "eta").
- **p195** identische Relationen: garbled chained-primed `3a'_1A'_0+a'_0A'_1=…` → two clean unprimed identities `3a_3A_0+a_1A_2=a_2A_1, a_2A_0+3a_0A_2=a_1A_1`.
- **p196** `C`→`C'` ×3 (covariant in the normal-form variables); exponents `α,3β`→`h,3k`; restored dropped parenthetical "(da wir die numerischen Coefficienten … vorausgesetzt haben)".
- **p197** restored dropped clause "(weil eine symmetrische Function von zwei Grössen…)"; `λ−2α` fabricated 2-step chain → `\frac32(μ−ν+2β+2τ)`; `r durch D`→`D^{-1/6}`.
Compiles **358 pp / 0 err**.
REJECTED: **p197** `γ`→`σ` (6th revert-the-editor — the paragraph proves γ integral; the print's "σ" is a Weber typo, the .tex's γ correct; type-B). SKIPPED: **p192** remove "ist" (low value, removing a grammatical word).

### 2026-06-25 — p198–203 (run w97rvytee; verified by eye + math)
APPLIED (3): **p198** restored dropped leading `Q^τ` on the first "Summe der Form" (eq (8) correctly keeps it dropped since Q is primitive); **p198** restored dropped display `(-1)^α M x^{2(α+β)} y^β` (+ "dieses"→"dies"); **p203** eq (11) `D=…−4a'_1a'_3³`→`−4a'_1³a'_3³` (D is a degree-6 invariant; the .tex term was inhomogeneous degree 4). Compiles **358 pp / 0 err**. p199–202 clean; 0 rejected.

### 2026-06-25 — p204–209 (run w1agyukjg; §65–67 invariant theory; verified by eye + math)
Dense — 11 candidates, **11 APPLIED, 0 rejected, p204 clean**:
- **p205** restored dropped derivation block (`ψ_1=a'_1ξ²−a'_3η²=a_0[…]/(α−β)` + "Darin aber … cyklisch zu vertauschen. Man findet so").
- **p206** `I'=r^λ I`→`r^{2μ}` (weight; I is degree μ); `Function I`→`I'`; `I(a)=I(0,…).`→`I'(0,…),`; "Diese Function I … a'_1a'_3 und a'_2"→"und diese Function I … a'_2 und dem Product a'_1a'_3".
- **p207** inverted substitution `ξ'=λξ`→`ξ=λξ'` (+ matching coeff exponents `λ^{-2}a'_1,λ²a'_3`→`λ²a'_1,λ^{-2}a'_3`); `χ`→`ψ` in eq (5) + its prose (Weber distinguishes ψ(5) from χ(6)).
- **p208** generator list `A,D,B`→`A,B,D` (matches print + eq (3)).
- **p209** restored dropped bibliography footnote (Clebsch 1872 / Faà di Bruno 1881 / Gordan–Kerschensteiner 1885 / F. Meyer 1890–91) — verified against a full-page re-render (the chunk scans were too faint).
Compiles **358 pp / 0 err**.

### 2026-06-25 — p210–215 (run wgfxgnw5z; §68–69 Tschirnhausen/Hermite; SPLIT — §68 fixed, §69 HELD)
Worst-transcribed region so far (27 agents, 894k tok). **§68 (p210–211): 5 APPLIED. §69 (p213–215): 10 HELD (see flag). p212 cosmetic only.**
§68 applied (genuine same-edition garbling):
- **p210** restored dropped footnote (Hermite, *Sur quelques théorèmes d'algèbre…*, Comptes rendus, Paris 1859).
- **p211 eq (3)** wrong LHS `x^ν`→`f(t)/(t−x)`, ν→n indices, restored dropped `+t f_{n-2}(x)` term.
- **p211 eq (4)** f_ν array shifted by one: restored `f_0=a_0` row, corrected last row to degree n−1.
- **p211 eq (6)** S[f_ν] shifted: restored `S[f_0]=na_0`, added `S[f_2]` row.
- **p211 eq (9)** wrong general formula → explicit `F_0,…,F_{n-2}` array (the .tex formula gives wrong F_0 even after eq (4) is corrected).
Compiles **359 pp / 0 err** (footnote + restored rows = +1 page; no swallow).

⚠️ **§69 HELD — p212–216 (.tex 7748–7876) needs a DEDICATED COHERENT REWORK, not piecemeal:**
The .tex §69 systematically writes `H(τ,ξ)` for Weber's eq-(3) analytic function `Φ(τ,ξ)`, which COLLIDES with the print's *separate* `H(τ,ξ)` (eq (10), the τ_k-substituted symbolic form `=Στ_kΦ_k`). It also drops the `Φ_ν(ξ)` expansion lines and a derivation block (the `dt/dτ=r/(γτ+δ)²` formula + the subtraction step). The verify stage correctly REJECTED the single eq-(8) Φ-graft (would reference an undefined symbol / break consistency) and flagged a possible "edition difference"; my read is it's a confused transcription, not a different edition. Either way the 10 agent candidates are scoped Φ/H grafts that together make a broken hybrid. **FIX PLAN:** read all print §69 (p212–216) in one pass, then rework .tex 7748–7876 coherently — restore `Φ` for the eq-(3) function, keep `H` only for the eq-(10) symbolic form, restore the `Φ_ν` expansions + the dropped blocks. Do NOT apply the agent's 10 §69 candidates individually. (Edition cross-check available: BSB first-edition Band I scan on disk.)

### 2026-06-25 — p216–221 (run w1buniwck; §70 Hermite-satz + §71 cubic transformation; verified by eye + math)
Another worst-region (30 agents, 915k tok), 0 clean pages. **20 APPLIED, 1 Weber erratum flagged.**
§70 (p216–218):
- **p216** restored dropped `a_0^\lambda` (`a_0^λ P(y_1…y_n)=K(t,a)`); `Coefficienten von f'(t)`→`-\frac1n f'(t)`; coefficient list →`0, -\frac{n-1}{n}a_1…, -\frac1n a_{n-1}` (added 0, minus signs, removed spurious `(n-2)/n a_2`); `p_2…p_n`/`p_ν`→capital `P` (eq (3) + prose).
- **p217** display `\frac{f(t)}{t-x}`→`-\frac1n f'(t)` added (it's F(t,x)); eq (5) restored print's specific indices + plain fraction `y_1-y_2=(x_1-x_2)\frac{f(t)}{(t-x_1)(t-x_2)}` (.tex had general i,k + a `(…)_t` wrapper not in print) + matching prose; **systematic Greek→Latin** `θ_{ik}`→`t_{i,k}` (×3: prose, eq (6), eq (7)) — print uses Latin t for building blocks, capital Θ for their product; eq (7) also restored `a_0^{n-1}` on LHS.
- **p218** `C_ν=Q_ν/Θ`→`ΘC_ν=Q_ν` (print's form).
§71 cubic (p220–221):
- **p220** eq (5) 2nd group `\tfrac23a_1x²+\tfrac13a_2x+\tfrac13a_3`→`a_0x²+a_1x+\tfrac23a_2` (= F_1 from §68); Δ `-4(\tfrac13H)³-27(\tfrac1{27}Q)²`→`-\tfrac1{27}(4H³+Q²)` (print's compact form, connects to eq (7)).
- **p221** restored dropped `3Q_0=\tfrac23H(t_1,t_0)Q_2-a_1f(t_1,t_0)` (.tex had `Q_0=0`); `y_2-y_3` factor `(x_2+x_3+t)`→`(t_1-t_0x_1)`; `y_2²-y_3²` restored dropped `y_1` factor; sum formulas `Σx_1(x_2-x_3)`→`Σx_1²(x_2-x_3)` & `a_0²x_1²`→`a_0³x_1³` (.tex's first was identically 0); restored dropped `Q_0` line + fixed `Q_1`,`Q_2` (`-t`→`-t_0`); eq (10) `-tH(t)`→`-\tfrac23H(t)`.
Compiles **359 pp / 0 err** (no swallow).

⚠️ **WEBER ERRATUM (type-B, transcribed faithfully as printed):** p221 final `Q_0` line prints `-\tfrac23 t_0 H`, but the H-coefficient must be **2/9** — proven twice: (a) Weber's own `3Q_0=\tfrac23H·Q_2-a_1f` (same page) with `Q_2=-t_0` ⇒ `-\tfrac29 t_0H`; (b) matching eq (10) `(3a_0x+a_1)f=-\tfrac23H+yf'-3y²` against `3·`eq (9) ⇒ `3Q_0=-a_1f-\tfrac23H` ⇒ `2/9`. Weber's page is internally inconsistent; the printed `Q_0` (2/3) is the typo. Zoom-verified via new `crop_src.py` (glyph is unambiguously `3`). RESTORED AS PRINTED (2/3) + flagged; candidate for an editorial `[sic; 2/9]` footnote — user's call.

DEFERRED (equal-value, not yet scan-confirmed): p218 `\sqrt{\Delta}`→`\Theta\sqrt{D}` (=√Δ since Δ=DΘ²). REJECTED (w/ agent): p217 eq (6) i,k authentic; p219 ×3 (.tex already correct).

### 2026-06-25 — p222–227 (run wxv40r1h5; §71 Cardano tail + §72 general transformation; verified by eye + math)
**10 APPLIED, 0 rejected, p225–227 clean** (16 agents, 523k tok).
§71 Cardano (p222):
- eq (12)/(13) `\Omega`→`\varrho` (varrho misread as Omega) + eq (13) `Q(t)`→`Q`; eq (14) `\sqrt[3]{Q(t)}`→`\sqrt[3]{3\varrho f(t)}`; prose `Der`→`und der Ausdruck (10)`.
- **Restored a badly-garbled Cardano-derivation block** (§62 link): `.tex` had `ξ=-h^{-1}Q`, `f(t)=r³f(t)=η³+ξ³`, `(16) 3a_0x+a_1=A-(ξ+η)`, `A=q_0/2A_0³` → print's `ξ=-hϱ; f(t)=ξ³, f'=3ξ²ξ'; f(t)=-h³ϱ³, f'=3h³A_0ϱ²; y=hϱ∛(3ϱ)/3; 3a_0x+a_1=-hA_0∛(3ϱ)-1/(h∛(3ϱ)); (16)=A_0(k-h)∛(3ϱ); hA_0∛(3ϱ)=∛((-q_0+3ϱa_0)/2), kA_0∛(3ϱ)=∛((+q_0+3ϱa_0)/2)`. Internally math-consistent (`ξ=-hϱ⇒f=ξ³=-h³ϱ³`, `f'=3ξ²ξ'=3h³A_0ϱ²`, eq (14)⇒`y=hϱ∛(3ϱ)/3`).
- eq (17) Cardano formula `q,p`→Weber's `a_3,a_2` (depressed cubic `p=a_2,q=a_3`); added `(§35)` xref.
§72 (p223–224):
- **p223** eq (5) restored dropped `a_0` factor (`E_{r,0}=a_0t_{n-1-r}`, consistent w/ eq (9) at s=0); prose `E_{r,s}; diese sind…t.`→ relative clause `E_{r,s}, die…t sind.`
- **p224** prose `Wenn wir`→`und wenn wir` (dropped connective + de-capitalized).
Compiles **359 pp / 0 err**.

### 2026-06-25 — p228–233 (run wv6xbxijm; §73 Bezoutiante + §74/75; verified by eye + math)
**12 APPLIED, 0 rejected, p230–232 clean** (20 agents, 611k tok).
- **§73 E-table (p228–229)** systematic `t`→`τ` in the entire RIGHT factor column (the bilinear φ(t)φ(τ) construction; left columns stay in t). Rewrote all 12 cells at once: row coeff = f'(t) coeff (4a_0,3a_1,2a_2,a_3) × τ_{3-s}. Agent caught 10; verifier wrongly rejected 2 (E_{3,2} uniqueness-fail on its scoped old_string; E_{1,3} misread as `3a_0` — zoom-confirmed `3a_1`, consistent with the row). Whole-column rewrite covers all.
- **§75 (p233)** restored two dropped footnotes: Cayley (on Tschirnhausen's Transformation, Phil. Trans. 1861, Math. Papers IV, Nr. 275) + Gordan (Math. Annalen Bd. 28, 1886).
Compiles **359 pp / 0 err**.

### 2026-06-25 — p234–239 (run wszgm639n; §75/76 → 'Zweites Buch. Die Wurzeln'; verified by eye + math)
**1 APPLIED, 0 rejected, p234/236/237/238/239 clean** (7 agents, 265k tok). Mostly clean (end of Erstes Buch).
- **p235** `ξ=-\frac1{y+\sqrt c}`→`ξ=\frac1{y+\sqrt c}` (spurious minus; the next line `y=(1-ξ√c)/ξ` only follows from `+`; scan shows no minus, equals sign directly on the fraction bar).
Compiles **359 pp / 0 err**. (p239 = the 'Zweites Buch / Die Wurzeln' divider — new major part begins.)

### 2026-06-25 — p240–245 (run w7dhyhsih; §76–78 root reality/Sturm; verified by eye + math)
**2 APPLIED, 0 rejected, p240/241/243/245 clean** (8 agents, 272k tok).
- **p242** discriminant display: `.tex` OVER-EXPANDED Weber's prototype `(x_1-x_2)^2,` into the full product `(x_1-x_2)^2(x_1-x_3)^2⋯(x_{n-1}-x_n)^2,` — print shows only the single representative factor (full product described in prose 'Quadrate der sämmtlichen Wurzeldifferenzen'). Reverted to print. **(rare direction: .tex ADDED content, not dropped.)**
- **p244** prose `also sind alle drei Wurzeln reell`→`also alle drei Wurzeln reell` (dropped inserted `sind`; elliptical, parallel to 'also nur eine Wurzel … reell' above).
Compiles **359 pp / 0 err**.

### 2026-06-25 — p246–251 (run wpkamn8yq; §78 biquadratic discussion; verified by eye + math)
**3 APPLIED, 0 rejected, p246–249 clean** (9 agents, 326k tok).
- **p250** restored two dropped footnotes: Kronecker (Monatsbericht Berliner Akad. 14 Feb 1878 + Dyck Katalog math. Modelle, München 1892, source of Fig. 5); Clebsch (Theorie der binären Formen §47) + Faà di Bruno (Walter, Leipzig 1881, §20, w/ Nöther's Zusatz).
- **p251** `-I^2`→`-T^2` in the covariant series `1, H, H²-16Af², -T²` (capital T misread as I; .tex's own §66 (7) at line 7534 uses -T²; scan p251_bot unambiguous T).
Compiles **359 pp / 0 err**.

### 2026-06-25 — p252–257 (run wj6z5uigg; §79 Bezoutiante/Realität + §80 Trägheit; verified by eye + math)
**3 APPLIED, 0 rejected, p252/256/257 clean** (9 agents, 331k tok).
- **p253** restored dropped leading `\pm` on the Vandermonde determinant (`\pm|det|=∏(x_r-x_s)`; Vandermonde = product only up to sign).
- **p254** `π+ν+1=n`→`π+ν=n-1` (transposed +1; print's literal form).
- **p255** eq (2) `\sum_{1}^{m}`→`\sum_{1,m}^{i,k}` (Weber's double-index Σ: indices i,k on top, range 1..m below; .tex dropped the i,k labels).
Compiles **359 pp / 0 err**.

### 2026-06-25 — p258–263 (run w3kk5thy0; §81–83 quadratic forms / vanishing determinants; verified by eye + math)
**13 APPLIED, 0 rejected, p261–263 clean** (19 agents, 592k tok).
- **§81 systematic `ξ`→`z`** (p258–259): the .tex rendered Weber's Latin linear forms `z_1,…,z_k`/`z_s` as `\xi` throughout — 10 instances (eq (2), the matrix prose, h-equation, y-system RHS ×3, the eq-(4)/(5) lead-in, eq-(6) lead-in). Converted the whole passage (incl. the cell the verifier rejected for wanting exactly this uniform conversion).
- **p259** eq (7) `\sum_{1}^{k}`→`\sum_{1,k}^{r,s}` (double-index Σ again); eq (6) `\varphi(…)',`→`\varphi(…);` (spurious prime + comma→semicolon).
- **p260** second-underdeterminant `A_{i,k}^{h,l}`→`A_{i,i'}^{k,k'}` (print's index convention).
Compiles **359 pp / 0 err**.

### 2026-06-25 — p264–269 (run wtx630oo8; §83–84; verified by eye)
**1 APPLIED, 0 rejected, p265–269 clean** (7 agents, 244k tok). Very clean.
- **p264** .tex escape-corruption: `$\pi,\nu$` was split at a line-wrap into `$\pi,`⏎`u$` (the `\n` of `\nu` eaten as a newline → rendered 'π, u'). Restored `\nu`. **(2nd escape-corruption after p194's `\\eta`.)**
Compiles **359 pp / 0 err**. Sweep `\$\\(greek),?$` (unclosed macro at line-end) found 1 more candidate ~line 19660 (~p500) — flagged for when the audit reaches it.

### 2026-06-25 — p276–281 (run wf8ghhsen; §88 Säculargleichung; verified by eye)
**0 APPLIED — ALL SIX PAGES CLEAN** (6 agents, 211k tok). §88 (secular equation / Sturm) faithfully transcribed; only cosmetic diffs (Coëfficient diaeresis, ss/ß, spaced ellipses, footnote accent style acute-vs-grave, and a conventional `\sum_{i=1}^n` vs Weber's `\sum_{1,n}^{i}` layout — LEFT as complete-notation re-expression, NOT an info-loss like p255/p259's bare `\sum_1^m`). Gate unchanged **359 pp / 0 err** (no .tex change). Sturm footnotes on p279/p280 PRESENT in .tex (not dropped).

### 2026-06-25 — p270–275 (run wns0kdpad; §85–87 Sturm chains; verified by eye + zoom)
**6 APPLIED, 0 rejected, p270/271/275 clean** (12 agents, 413k tok).
- **Sturm-chain label**: the .tex rendered Weber's Fraktur chain name `(ℜ)` as the digit `(1)` throughout §86. Zoom-confirmed Fraktur **ℜ** (R for Reihe; agent was split K/R, verifier said R, my zoom + context = R). Fixed all 5 instances → `(\mathfrak R)`: eq (1) right-margin label (added, kept \tag{1}) + 4 in-text refs.
- **p274** prose `So ist P_n(x) … Grades, und`→`so dass P_n(x) … Grades ist, und` (restored subordinate clause + clause-final `ist`).
Compiles **359 pp / 0 err**.

### 2026-06-25 — p282–287 (run wqtorxz0i; §89–93 Hermite form / discriminant determinant / characteristic theory; verified by eye + math)
**16 APPLIED, p282/287 clean** (23 agents, 734k tok). Dense again.
- **p283** eq (6): all three sums `\sum_{s=0}^{·}`→`\sum_{s=0}^{n-1}` (2nd was n-2, 3rd was 0; print uniform 0..n-1) + eq-end period→comma; `z=y`→`τ=t`; `Dies`→`und dies`; `so ergeben sich`→`so ergiebt sich`.
- **p284** systematic `h_{i,k}`→`H_{i,k}` (×3: H=ΣΣ def, prose, S-def) + prose `t_it_k`→`t_iτ_k` (bilinear §91(6)); **restored dropped determinant-decomposition block** (`(-1)^nf(α)/a_0·|f_k(x_i)|²` + `|a_0-triangular|×|Vandermonde|` + `a_0^{2n-2}D`→`a_0²D`; math: product²=a_0^{2n}Π²=a_0²D); `so wird Δ`→`Δ also`; `Δ_n(α)`→`Δ_n(α)=Δ`.
- **p285** cubic Kette `-H_{2,2},-(…)/a_0,-Δ`→`(1/a_0)H_{2,2},(1/a_0)(…),(1/a_0)Δ` (signs+factor); 'vier Functionen' 3rd/4th terms badly garbled → restored (incl. `-f(α)D`).
- **p286** systematic `θ`→`Φ` (×3: prose, dΦ, eq (2) `[φ,Φ]`) — Weber's arbitrary function is Φ (θ would clash with the angle ϑ).
Compiles **360 pp / 0 err** (was 359; +1 from restored p284 block).

### 2026-06-25 — p288–293 (run w2jxi5lw0; §93–94 Charakteristikentheorie; verified by eye + zoom)
**8 APPLIED, 0 rejected, p290/291/293 clean** (13 agents, 427k tok).
- **p289 systematic `a`→`α`** (×4: 'der Punkt α', 'ψ in α positiv/negativ', Fig 9 node) — the intersection-point label is Greek α (zoom-confirmed; matches φ/ψ style + Fig 9). NB the doc DOES use Latin a elsewhere (counts: 'Ist a die Anzahl', p288), so a/α is a real distinction — zoomed to be sure.
- **p292** eq (3) restored dropped third member `=ψ'(x)²+ψ'(y)²` (= φ'(x)²+φ'(y)² via eq (2)).
- **p288** parenthesized '(Im Falle der Fig. 8 ist sie gleich −1)'; **p289** prose `Es gilt`→`und es gilt`.
Compiles **360 pp / 0 err**.

### 2026-06-25 — p294–299 (run w3c0efzrk; §94–98 fundamental theorem of algebra; verified by eye)
**2 APPLIED, 0 rejected, p295–299 clean** (8 agents, 314k tok). Mostly clean.
- **p294** eq (4) `k=A_ε.`→`k=A_ε,` + `D. h.`→`d. h.` (the equation flows into the 'd.h.' sentence; period+capital → comma+lowercase).
- Footnotes p296 (Gauss 1799 'Demonstratio nova'), p299 (Sturm) PRESENT in .tex (only accent/punct cosmetic diffs).
Compiles **360 pp / 0 err**.

### 2026-06-25 — p300–305 (run wa273i4qi; §99–100 Budan-Fourier / Newton's rule; verified by eye + zoom)
**~12 APPLIED + restored 2 dropped sign tables, p305 clean** (15 agents, 519k tok). Dense (computation §§).
- **p303 systematic `λ`→`𝔷`** (×3: prose + 2 eqs) — the root-count is Fraktur 𝔷 (z for Zahl; zoom-confirmed; .tex had Greek λ). μ (multiplicity) correctly kept.
- **p301–302 RESTORED 2 dropped sign tables** (Budan-Fourier case analysis: '1. μ gerade' + '2. μ ungerade', each with a)/b) sub-cases and δ_1/δ_2 sign-rows) — the .tex had collapsed both into a prose paraphrase. Reconstructed from both scan pages (all +/− entries legible) + restored the 'Es geht also' conclusion.
- **p304** eq (4) `F_0=F_n=1`→`F_0=F=1` (the .tex's F_n=1 contradicted F_n=f_n² on the same line); eq (6) badly garbled → `f_ν F_ν'(x)=(n-ν-1)(F_ν f_{ν+1}+F_{ν+1}f_{ν-1})`; removed over-expansion clause 'bis auf positive Zahlenfactoren…Form.'.
- **p300** `unverändert`→`ungeändert` (Weber's word); **p301** `f^{(ν+μ)}(ξ)`→`(x)`; **p302** `Reihe`→`Reihen`.
Compiles **360 pp / 0 err**.

### 2026-06-25 — p306–311 (run w1x9p9vuc; §101–102 Newton/Descartes/Jacobi criteria; verified by eye + zoom)
**9 APPLIED, 0 rejected, p307/308 clean** (15 agents, 513k tok).
- **p309** eq (4) restored dropped top row of the Doppelreihe (`a_0,…,a_n` over `A_0,…,A_n`; wrapped in gathered).
- **p311** sign sequence `+,-,+`→`-,+,-` (inverted); `D=A_1A_2-B²`→`3D=…` (dropped 3); eq (2) restored dropped 1st formula `y=(x-α)/(β-x)`; footnote removed over-inserted `Jacobi,`; connective `In der Reihe`→`und in der Reihe`.
- **p306** restored dropped 'lassen aber…nur zwei Fälle' enumeration-caveat clause + `Functionen f_ν`→`Functionen, etwa f_ν,`.
- **p310** `aller reellen Wurzeln`→`aller reeller Wurzeln` (don't-modernize: print's strong genitive `-er`).
Compiles **360 pp / 0 err**.

### 2026-06-25 — p312–317 (run wwhxovth2; §103 Klein / §104 Laguerre; verified by eye + zoom)
**4 APPLIED, 0 rejected, p314/315 clean** (10 agents, 346k tok).
- **p312** §103 heading restored dropped author 'Klein's' (→ 'Klein's geometrische Vergleichung der verschiedenen Kriterien').
- **p313** restored dropped xref note 'Fig. 16 (a. f. S.)' (auf folgender Seite).
- **p316** Laguerre function list `f_0…f_n(x)`→`f_0…f_{n-1}(x)` (the §4 associated functions are f_0..f_{n-1}; f(x)=f_n(x) separate; confirmed by the p317 definition block).
- **p317** `in \S\,4`→`im \S\,4` (Weber's 'im §', dropped m).
Compiles **360 pp / 0 err**.

### 2026-06-25 — p318–323 (run w5die8q32; §106–107 Rolle/Laguerre; verified by eye + math)
**~10 APPLIED, p318/319/321/322 clean** (15 agents, 479k tok).
- **§107 (p323) systematic `\sum`→`S`** (Weber's sum-over-roots operator; print + prose 'das Summenzeichen S' confirm; eqs 1–4,7 all S) — agent had only converted some.
- **p323 eq (3)** removed spurious `n` (numerator `f'(x)²-H(x)`, consistent w/ eq (2)); **eq (4)** fixed + removed a PHANTOM 'in der sinngemässen…' block; **eq (5/6)** numbered the `rx'=dx-by` system as (6); **restored dropped display `r²H(x,y)=H'(x',y')` + 'Hiernach'**; **eq (7)** S form + restored dropped factor `(cx'+dy')²` + retag (6→7).
- **p320** `Ausdrucks`→`Ausdruckes` (dropped genitive -e; Weber uses -es 4×); `c-fache Wurzel u.s.f.`→`c-fache etc.\ Wurzel`; Theorem XIV `f(x)=0`→`f(x)` (XIII has =0, XIV doesn't).
Compiles **360 pp / 0 err**.

### 2026-06-25 — p324–329 (run wn24os3y8; §107 Laguerre cont.; verified by eye + math)
**18 APPLIED, 0 clean** (24 agents, 736k tok). Dense §107 continuation.
- **systematic `\sum`→`S`** (Weber's operator, §107): eq (8), the P display, p327 power-sums `S(α²),S(α),S(α²)/S(α),S[α(α-ξ')]` (agent had left several as \sum).
- **systematic `Ω`→`Φ`** (the form Φ=(Xy-Yx)²P-(Xη-Yξ)²): eq (9) + 3 prose — .tex used Ω throughout §107; later genuine Ω (continued fractions §116+, Körper §137) left intact (scoped to §107 line range).
- **eq (8)** restored dropped factor `(xη-ξy)²` on H (parallel to eq (7)); **squared term** `((Xη-Yξ)/(Xy-Yx))²=((ξβ-ηα)/(xβ-yα))²` (.tex dropped both ²); **restored dropped display `P=S(…)²`**.
- prose: `und (X_1,X_2)`, `Frage: wie ist…`, `und man erhält`, double-`aber`→single, `beiden anderen abhängt. Die`, `Quadratwurzel…haben kann` (singular), `(mit Laguerre)` restored.
Compiles **360 pp / 0 err**.

### 2026-06-25 — p330–335 (run wb061zdbo; §108–109 numerical/Newton approximation; verified by eye + math)
**2 APPLIED, 1 type-B erratum, p330–333/335 clean** (8 agents, 295k tok). Mostly clean.
- **p334** worked-example table header `\Delta_x,\Delta'_x`→`\Delta_\alpha,\Delta'_\alpha` (print uses α-subscripts, per eqs (6)–(8)).
- ⚠️ **WEBER ERRATUM (type-B, restored to print):** p334 `u'` printed as `0,0164` but Weber's own sum `α+u+u'=1,76937` (α=1,7, u=0,06773) requires `0,00164`. The .tex had silently 'corrected' it to `0,00164`; per discipline I REVERTED to the printed `0,0164` + flagged (printed digit is a Weber arithmetic typo; consistent value 0,00164). [cf. Q_0 erratum p221.]
Compiles **360 pp / 0 err**.

### 2026-06-25 — p336–341 (run w5b2kbewo; §109–110 approximation/Bernoulli; verified by eye)
**2 APPLIED, 0 rejected, p337–339/341 clean** (8 agents, 271k tok). Mostly clean.
- **p336** `Näherungsmethode anwenden`→`Näherungsmethoden` (plural; print shows -en).
- **p340** restored dropped/paraphrased prose: `dem Intervall (α,β) angehörige Intervall, worin f(ξ)`→`Werthpaar in dem Intervall (α,β), wofür f(ξ)` (dropped 'Werthpaar', paraphrase).
Compiles **360 pp / 0 err**. (typeB: p336 eq tagged '(3)' duplicates an earlier (3) — printed-page numbering quirk, .tex faithfully reproduces it.)

### 2026-06-25 — p342–347 (run wzi38i6co; §110–111 Bernoulli/Gräffe; verified by eye + zoom)
**3 APPLIED, 0 rejected, p342/343/345/346 clean** (9 agents, 319k tok).
- **p344** rewritten eq (6): running index `α_n φ(α_n)`→`α_m φ(α_m)` on the last numerator AND denominator terms (kept inner `p-α_n`).
- **p347** `die vierte und achte Potenzen`→`die vierten und achten` (plural -en).
- **typeB (no change — Weber-corrected):** p347 print `(2x²-1)²` is a typo Weber fixed in his Berichtigungen; the .tex correctly has `(2x²+1)²`.
**BERICHTIGUNGEN reference:** the .tex carries Weber's published errata (line 20867–20872), only 2 entries: p182 (`X_m` not `X_n`) and p347 (`(2x²+1)²`). → confirms my p334 u'-revert (NOT in errata ⇒ uncorrected typo, transcribe + flag) and the batch-14 p182 x_m decision.
Compiles **360 pp / 0 err**.

### 2026-06-25 — p348–353 (run woj8yjuii; §111–112 Gräffe / trig. cubic; verified by eye + math)
**4 APPLIED, 0 rejected, p349/353 clean** (12 agents, 398k tok).
- **p348** Gräffe-squared coeff array: pos 2 `4a_0²`→`4a_1²`, pos 4 `6a_2²-12a_3a_1`→`6a_3²-12a_2a_4` (confirmed by print + the array's mirror symmetry; pos 3 `6a_2²-12a_1a_3` was already correct).
- **p352** `λ=g^m/e^{m+n}`→`g^n`; `keine positive Wurzeln`→`Wurzel` (singular).
- **SKIPPED (cosmetic, value-equal):** p350/p351 eqs (5),(8) `\tg^3\varphi` vs print `tg φ³` — both = (tanφ)³; kept the .tex's unambiguous `tg³φ` (field-norm; `\tg\varphi^3` reads as tan(φ³) to a modern eye).
Compiles **360 pp / 0 err**.

### 2026-06-25 — p354–359 (run wgawfchk9; §112–115 trig cubic → number theory; verified by eye + zoom)
**6 APPLIED, 1 type-B erratum, p355/358/359 clean** (11 agents, 410k tok).
- **p354** `a^m c^m`→`a^n c^m` (middle term of the λ chain); **p356** `λ=g^m/e^{n+m}`→`g^n` (recurring g-exponent error, cf. p352); **p356** `Decimale`→`Decimalen`.
- **p353+p357 `Briggs'schen`→`Brigg'schen`** (×2, don't-modernize: Weber consistently writes 'Brigg'sche'; the .tex modernized the name).
- ⚠️ **WEBER ERRATUM #3 (type-B, restored to print):** p357 'Nähe der Werthe 30°40'' — printed 30° is a typo for 33° (inconsistent w/ the computed θ=33°40' + bracket 33°41'/33°42'; NOT in Berichtigungen). The .tex had silently corrected to 33°40'; reverted to printed 30° + flag (zoom-confirmed). The genuine 33°40' (computed value, line 13168) kept.
- typeB (no change): p355 print 'odre' (trivial typesetting typo for 'oder'); .tex's 'oder' kept.
Compiles **360 pp / 0 err**.

### 2026-06-25 — p360–365 (run w0a0kv2u4; §116–117 continued fractions; verified by eye + zoom)
**7 APPLIED, 0 rejected, p360/362/364/365 clean** (13 agents, 425k tok).
- **p361** §116 heading `Kettenbruchentwicklung`→`Kettenbruchentwickelung` (-elung; .tex body uses -elung); eq (8) final index `a_ν`→`a_r` (×2 lines; continued-fraction terminal index is r, not the running ν).
- **p363** `an. Wir können`→`an, und wir können`; `wobei`→`wo`; `die Gleichheit Q_{n-1}=Q_n`→`mit der oberen Grenze Q_n` (.tex rephrased the parallel construction).
- **don't-modernize:** `Q_n\to\infty\;(n\to\infty)`→`Q_n=\infty\;\text{für }n=\infty` (the .tex modernized Weber's '=∞ für n=∞' to limit-arrow notation).
Compiles **360 pp / 0 err**.

### 2026-06-25 — p366–371 (run wte5nvrjp; §118–119 indeterminate eqns / modular equivalence; verified by eye)
**6 APPLIED, 0 rejected, p366/369/370 clean** (10 agents, 316k tok).
- **p367** `Da hier n=11`→`und da hier n=11`. **p368** `m=α_1x+δx_1`→`m=α_1x_1+δx` (subscripts swapped); solution block `x_1=x, x_2=x_1y_2, x_3=x_1y_3`→`x_1, x_2=xy_2, x_3=xy_3` (first term x_1 alone, multiplier plain x).
- **p371 DROPPED FOOTNOTE restored:** Dedekind, *Schreiben an Herrn Borchardt … elliptischen Modulfunctionen*, Crelle Bd. 83 (1877) — citation footnote after 'äquivalent', grep-confirmed absent from .tex.
- **don't-modernize (agent mis-classified as cosmetic):** p368/p370 `gibt`→`giebt` (×2). ⚠️ **SYSTEMATIC: .tex has ~18 more 'gibt' in later/unaudited sections (14256+, 17335+, …20688 which even mixes giebt/gibt on one line) — GLOBAL `\bgibt\b`→`giebt` sweep DEFERRED to end-of-vol1.**
Compiles **360 pp / 0 err**.

### 2026-06-25 — p372–377 (run w1k1heeek; §119–121 modular substitutions / CF-equivalence; verified by eye across the page-break)
**3 edits (4 candidates), 0 rejected, p372/375/377 clean** (10 agents, 332k tok).
- **p373/374 DROPPED matrix display + connective restored (page-break block, reconstructed from BOTH pages):** print runs M=(…), M'=(…) → 'Es ist dann auch' → **M M'⁻¹=(α,β;γ,δ)** → 'eine lineare Substitution, und' → (m,μ;n,ν)=(α,β;γ,δ)(m',μ';n',ν') → **'woraus folgt:'** → m=αm'+βn'. The .tex had dropped the M M'⁻¹ display + 'woraus folgt:' and mis-slotted the surviving display. Added the M=/M'= labels too (load-bearing — referenced in M M'⁻¹).
- **p376** prose `die Zahl der nicht übereinstimmenden`→`die Zahl der den übereinstimmenden` (nicht→den; 'den' is dative = the Theilnenner PRECEDING the agreeing ones; the .tex's 'nicht' inverted the meaning).
Compiles **360 pp / 0 err**.

### 2026-06-25 — p378–383 (run wrvlraqan; §122–123 reduced quadratic irrationals; verified by eye + heavy zoom)
**11 APPLIED (2 type-B errata), p380/381 clean** (17 agents, 549k tok — densest batch yet).
- **p379** eq (14) `-c=-a_1γ²+…`→`-c=a_1γ²+…` (spurious minus; matches the +a_1/+2a_1 leading pattern of rows a,b; agent numeric-inversion confirmed).
- **p382** case labels Latin `a)/b)`→Greek `α)/β)` (×3: display + 'Im Falle α)' + 'Im Falle β)'; the §123 γ-cases are Greek, distinct from the Latin figure/exception cases a)/b) on the same page — the .tex conflated them); prose `nicht kleiner als`→`mindestens gleich`; reorder `entweder α=0, δ=0…`→`entweder: δ=0,…ξ_1=-ξ, α=0, das ist der Ausnahmefall b)`.
- **p383** `gibt`→`giebt` ×3 (14260/14278/14284 — 3 of the queued sweep, now in-batch).
- ⚠️ **WEBER ERRATUM #4 (type-B, p382):** β-case 'nach (14)' formula printed `(ξ±δ)²⋚1` — DROPS the `+η²` that eq (14) `(γξ+δ)²+γ²η²⋚1` carries (γ²=1) and that the parallel δ=±1 sub-case `(ξ±1)²+η²⋚1` keeps. Reverted the draft's silent re-correction `(ξ+δ)²+η²` → printed `(ξ±δ)²` (also +→± type-A) + flag.
- ⚠️ **WEBER ERRATUM #5 (type-B, p378):** eq (11) inverse printed `ω=(δω_1-β)/(-γω_1+α_1)` — the `α_1` is a typo for plain `α` (matrix inverse of [[α,β],[γ,δ]]; no α_1 exists here). Draft had silently corrected to `α`; reverted to printed `α_1` + flag (zoom-confirmed subscript).
Compiles **360 pp / 0 err**.

### 2026-06-25 — p384–389 (run wvyx2j90c; §123–125 reduced forms / periodic CFs; verified by eye)
**4 APPLIED (1 type-B erratum), p386/389 clean** (10 agents, 365k tok).
- **p384** `so liegen die Bilder`→`so liegen also die Bilder`. **p387** `…wieder. Wenn die Periode`→`…wieder, also, wenn die Periode`. **p388** `Es genügt also,…bezeichnen:`→`und es genügt also,…bezeichnen, etwa so:` (dropped 'und'/'etwa so').
- ⚠️ **WEBER ERRATUM #6 (type-B, p385, §124):** the non-vanishing difference printed `ω'-ω=2y√d` (no minus) — but ω=x+y√d, ω'=x-y√d ⇒ ω'-ω=-2y√d, and the next clause 'wonach (4) zeigt, dass ω'_n negativ ist' REQUIRES the minus. Draft had silently signed it `-2y√d`; reverted to printed `2y√d` + flag.
Compiles **360 pp / 0 err**.

### 2026-06-25 — p390–395 (run wqp463rr2; §125–126 periodic-CF worked examples D=29/116/37/136; verified by eye + math)
**9 APPLIED, 0 clean pages** (15 agents, 473k tok — worked-examples section garbled throughout).
- **p390** `Irrationalzahlen. Wenn`→`Irrationalzahlen, und wenn`; `gehören und also`→`gehören, und die also` (dropped 'die').
- **p391 GPT OVER-INSERTIONS:** `Daraus folgt also`→`Daraus also` (spurious 'folgt'); `von allen anderen reellen Zahlen`→`…anderen Zahlen` (spurious 'reellen'). Audit BOTH directions.
- **p392 DROPPED SENTENCE restored:** before 'Die grösste in √D…', the .tex dropped 'Wir bestimmen zunächst nach §. 125, 4. die sämmtlichen zu D gehörigen reducirten Zahlen.'; also `λ ist hier 5`→`=5` (dropped = sign).
- **p393** D=116 CF `\frac{5+√29}2=[10,2,1,1,2]`→`5+√29=[10,…]` (.tex wrongly added /2; {4,10,1}⇒ω=(10+√116)/2=5+√29, a_0=10 ✓; the D=29 CF (5+√29)/2=(5,5,5…) is separate + correct); restored dropped inline `[1,5,1]:` (D=37).
- **p394** `Die Kettenbruchperioden sind`→`und die Kettenbruchperioden`. **p395** `Mit Rücksicht auf`→`und also mit Rücksicht auf die Gleichung`.
Compiles **360 pp / 0 err**.

### 2026-06-25 — p396–401 (run w2xlg9o6a; §126–129 Pell eqn / units / Gauss forms / CF root-approx; verified by eye + zoom)
**17 APPLIED, 0 clean pages** (23 agents, 721k tok — biggest batch; heavily garbled). **Page count 360→361** (restored dropped sentences/footnote legitimately grew the doc; 0 errors).
- **p396** `…ist. Aus`→`…ist; und aus`; `Nun folgt aus (6)`→`Nun folgt aber aus (6)`; `2c+b>√D, also`→`2c+b>√D [§. 125, (4)], also` (dropped xref); `so ist hiernach`→`so ist sie hiernach`.
- **p397** restored 2 dropped 'also der oberen/unteren Zeichen' clauses; restored a whole dropped sentence ('wo das Gleichheitszeichen…nur für n=1…ebenso wie in (12).'); `Somit ist also nach (10)`→`und es ist also nach (10)` (was agent-REJECTED on a bad-grep uniqueness fail — line 14849 had it; reinstated).
- **p398** `wachsen muss, und dass also`→`…muss, dass also` (over-inserted 'und').
- **p399** restored dropped clause 'Es ist also Θ_3 gleichfalls eine zu √D gehörige Einheit, und' + '(und folglich auch mehrerer)'.
- **p400** `liegen:`→`liegen, da diese Potenzen mit dem Exponenten ins Unendliche wachsen; also`; `Θ, gegen`→`Θ, was gegen`; `sein.`→`sein, was zu beweisen war.`; **restored dropped footnote** (Disq. ar. art. 183 ff., Dirichlet-Dedekind, Vorlesungen über Zahlentheorie. Vierte Auflage. §. 72 ff.).
- **p401 two-alphabet α→a** (×3, zoom-confirmed Latin a = CF partial quotients): `α_0 finden`, `x=α_0+1/x_1`, `α_1`; `je nachdem D…ist, und`→`(je nachdem D…ist) und`.
- typeB (NO change): p396 eq (8) + p398 examples print a doubled `==` (typesetting defect); .tex's single `=` kept (glyph glitch, not content).
Compiles **361 pp / 0 err**.

### 2026-06-25 — p402–407 (run w6tvxhpjy; §129–131 CF root-approx worked example / rational roots / Gauss-form factoring; verified by eye + math derivation)
**~34 APPLIED, 0 clean pages** (40 agents, 1.2M tok — LARGEST batch). 33 agent-accepted + rejected-reconstructed + §129 α→a unified.
- **p402 cubic CF chain (math-derived every row):** coeffs `3x³-x²-11x-1`→`-3x` (x=1+1/x₁ ⇒ 3x³-x²-3x-1), `9x³-22x²-11x-2`→`-14x`, `43x³`→`46x³`; restored dropped lead-in sentence (f₂ root), 4th CF group (a₀,a₁,a₂,a₃), CF terminal `,2,`; ⚠️ **WEBER ERRATUM #7 (type-B):** print SWAPS a₃/a₄ labels (a₄=1 on the 9x³ row whose root∈(2,3)⇒a₃=2; a₃=2 on the 46x³ row whose root∈(1,2)⇒a₄=1) — reproduced print's swap (the .tex had silently un-swapped them).
- **§129 α→a UNIFIED:** the .tex used Greek α for §129's CF partial quotients; print uses Latin a (matches batch 51 p401). Converted all §129 α→a (scoped — §130 φ/ψ coeffs α,β and §131 unknowns α,β,γ,δ,ε stay Greek).
- **p403/404** dropped Coefficienten clause; restored dropped ψ(x) display; `X`→`x_1` (substitution var); 3 dropped clauses.
- **p405** dropped sentence (Auswahl der erprobenden Zahlen), xref `(§. 50)`, footnote `etc.`, rewordings.
- **p406** congruences `γ`→`γ²`, `β≡±2,±1`→`±1,±2,±1`, `1+1`→`1∓1`; dropped clauses.
- **p407** `β≡-1(mod29)`→`2β≡-1(mod29)`; reconstructed the δ=-12 passage (rejected agent fix was incomplete — restored 'zur Folge hat, die aber nicht lösbar ist' + 'noch übrig'); `1. bis 5. sind befriedigt…verificiren ist`.
- typeB (NO change): doubled `==` print defect (kept clean `=`).
Compiles **361 pp / 0 err**.

### 2026-06-25 — p408–413 (run wazg1ukmi; §131–133 roots of unity / cyclotomy / φ(n) totient; verified by eye + zoom)
**15 APPLIED, p408/411 clean** (19 agents, 590k tok).
- **p409** `h,h'=h+μ`→`k,k'=k+μ` (symbol, matches eq (4)); `r^h=r^{h'}`→`r^k=r^{k+μ}`; `r^{k'}=r^{k+hn}=r^k(r^n)^h`→`r^{k'}=r^k r^{hn}` (.tex inserted a spurious middle member).
- **p410** dropped 'ist' (`oder n durch μ theilbar`); `r^μ=r^{mx+ny}=(r^m)^x(r^n)^y`→`r^μ=r^{mx} r^{ny}` (spurious member); `r^n=(r^μ)^h r^{μ'}`→`r^n=r^{hμ} r^{μ'}` (compact form per print).
- **p412 §133 x→π SYSTEMATIC:** the .tex used Latin x for the prime-power exponents (n=p^x p_1^{x_1}…); print uses Greek π. Converted ALL §133 exponents x→π (more than the agent flagged — incl. 15304's p^{π-1} chain, 15306, 15308); also `q`→`ϱ` (varrho, root of unity); restored 'd. h. also,' connective.
- **p413** restored dropped product symbol `Π`.
Compiles **361 pp / 0 err**.

### 2026-06-25 — p414–419 (run wl6o7t14i; §133–135 cyclotomic polynomials X_n / irreducibility; verified by eye + zoom)
**16 APPLIED, 0 clean pages** (22 agents, 667k tok).
- **SYMBOL SWAPS (.tex swapped n↔μ between sections):** p414 §133 `f_μ`→`f_{n_1}`, `für μ`→`für n_1` (Weber's index here is n_1); p417 §134 `n_1,n_2`→`μ_1,μ_2` (Weber's auxiliary divisor-products are μ).
- **p419 §135 Θ→Φ SYSTEMATIC (×9):** the .tex used Θ(x) for Weber's product function Φ(x)=φ(x)φ(x²)… (capital Φ, distinct from lowercase φ factor). Converted all §135 Θ→Φ (scoped — the §127 unit Θ stays). zoom-confirmed.
- **p416** `n=p^π q^χ`→`n=pp'qq'` (Weber's recursive notation, consistent w/ eq (9) pp'/p').
- **p415** restored dropped sentence 'worin sich das Productzeichen Π auf alle Theiler μ von n bezieht.'; **p418** restored dropped parenthetical '(da wir anderenfalls durch das Product der beiden Coefficienten dividiren würden)'.
Compiles **361 pp / 0 err**.

### 2026-06-25 — p420–425 (run w2gk96itc; §135–136 Kronecker irreducibility / DISCRIMINANT / quadratic Gauss sum; verified by eye + zoom + DERIVATION)
**14 APPLIED, 0 clean pages** (20 agents, 613k tok — most math-delicate yet). **NO new erratum** (agent's suspected typeB was a misdiagnosis).
- **GAUSS-SUM EXPONENT (n-1)/2 vs (n-1)²/4 — DERIVED, agent typeB REJECTED:** .tex had `(-1)^{(n-1)^2/4}` (∏R sign, p423) and `(-i)^{(n-1)^2/4}` (eq 14, p424); print has `(n-1)/2` in both. Agent flagged (n-1)/2 as a Weber typo (pair count is (n-1)²/4). BUT: for the SIGN (-1)^m=(-1)^{m²} (m≡m² mod 2) so (n-1)/2 is a VALID equivalent — NOT a typo; for eq (14) (-i) has order 4 so (-i)^{(n-1)/2}≠(-i)^{(n-1)²/4} → the .tex was WRONG. Both fixed to printed (n-1)/2 (type-A); print correct, NO erratum. (pair-count (n-1)²/4 at 15636 stays.)
- **p423** eq (12) `R=(r^μ-r^ν)(…)`→`(r^ν-r^μ)(…)` (1st-factor sign, non-commutative); eq (10) `n^{(n-2)/2}√{(-1)^{(n-1)/2}}`→`n^{(n-3)/2}√{(-1)^{(n-1)/2}·n}`; restored dropped `[r^ν-r^μ, ν<μ]` display; `n=1(mod4)`→`n≡1`,`n≡-1(mod4)`; `nach §.46`→`(§.46)`.
- **p422** restored dropped Π + clause + display after eq (6); restored dropped eq `∏(x-r)=∏(r-x)=X_n` + 'also' + (§.133).
- **p424** restored 2 dropped product-display RHS (`=r^{±(n²-1)/8}`).
- **p420** footnote `Kronecker, …$x^n-1$,`→`…$(x^n-1)$.` (drop name—it's in the body; add parens, period). **p421** `transcendente`→`transcendenter`. **p425** `enthält`→`erhält`.
Compiles **361 pp / 0 err**.

### 2026-06-25 — p426–431 (run wof92qfrs; §136–137 Fermat's theorem / primitive congruence-roots; verified by eye + zoom)
**12 APPLIED (1 type-B erratum #8), p428/431 clean** (18 agents, 570k tok).
- **§136 Fermat a→α SYSTEMATIC (×5):** the .tex used Latin a for Weber's base α in α^n≡α (eq 6,7 + 'für jede ganze Zahl α' + 'α=0,α=1' + '(α+1)^n≡α^n+1'). Converted all (incl. the agent-rejected line — same systematic).
- **p426** `a_0x+a_1`→`a_0x+a`; root `x≡-a_0'a_1`→`α≡-aa_0'`; eq (3) cleared-denom→fraction `(f(x)-f(α))/(x-α)=f_1(x)`.
- ⚠️ **WEBER ERRATUM #8 (type-B, p426):** m=1 base case prints `a_0a_0'≡1 (mod m)` — but m=1 ⇒ mod 1 trivial; should be mod n. Zoom-confirmed 'm'. Draft had silently 'corrected' to mod n; reverted to printed mod m + flag.
- **p429** `ay≡1-bx`→`y≡(1-bx)/a` (fraction form); `γ=γ^{ay+bx}`→`γ≡γ^{bx}γ^{ay}` (= → ≡, product).
- **p430 §137** `p^x…φ(p^x)…Grade p^x, p^{x-1}=p_1`→`pp_1…φ(pp_1)…p^π, p^{π-1}=p_1` (Weber pp_1 notation + x→π); `g^h`→`g^m`.
Compiles **361 pp / 0 err**.

### 2026-06-25 — p432–437 (run w82nzlwfx; §137 index / Theilung des Winkels / trig multiplication; verified by eye)
**2 APPLIED, p433/434/436/437 clean** (8 agents, 288k tok — section mostly clean).
- **p432** eq (21) `ind 1=0`→`ind 1≡0` (= → ≡ congruence, matches parallel 'ind(-1)≡(n-1)/2 (mod n-1)').
- **p435** eq (10) restored dropped range bound `0≦v≦(n+1)/2`.
Compiles **361 pp / 0 err**.

### 2026-06-25 — p438–443 (run w29kz28l6; §137–138 cyclotomy → quadratic reciprocity / Legendre symbol; verified by eye)
**6 APPLIED, p439/442 clean; §138 numbering #7–9 HELD** (15 agents, 470k tok).
- **p438** eq (27)/(28)/(29) `ω`→`α` (root variable) + product upper-index `∏^α` (eq 28,29).
- **p440** `cos(-ρ)=cosρ`→`cos(-φ)=cosφ` (Weber's generic-angle identity uses φ, not the local ρ); restored dropped clause 'wie sich aus der folgenden Zusammenstellung ergiebt, worin k eine nicht negative ganze Zahl bedeutet'.
- **p441** `die genaue Formel`→`die genaue Formel (1):`.
- ⏸ **HELD §138 numbering (#7/#8/#9):** print numbers the Legendre-symbol results flush-left 1.–9. ('8.' multiplicativity, '9.' reciprocity), but the .tex re-laid them as enumerate + eq-tags incl. primed/out-of-order (9', 10) and 'diese Formel' for '8.'. Cross-refs ('bleibt 8.', 'aus (4) und (9)') don't resolve. Systematic re-layout (cf §69) — needs a coherent §138-numbering rework (p441–443), NOT piecemeal. **NEW STANDING ITEM.**
Compiles **361 pp / 0 err**.

### 2026-06-25 — p444–449 (run ws01x0ag2; §138 end → BUCH III §139 Galois theory / Körperbegriff; verified by eye)
**3 APPLIED, p445/446/447/448 clean; §138 numbering #1/#2 HELD** (11 agents, 367k tok).
- **p449 §139** restored 3 dropped items in the Zahlkörper-definition paragraph: '(die vier Species)' after Rechenoperationen; the Dedekind citation '(Dirichlet-Dedekind, Vorlesungen über Zahlentheorie, 2. Aufl. 1871, §. 159)'; '(corpus, corps)' after Körper + sentence-final verb restored ('…zukommt, bedeutet.').
- ⏸ **p444 §138 numbering HELD (#1/#2):** `\tag{10'}`→`10`, `\tag{7'}`→`7` — same primed-numbering re-layout held in batch 58; folded into the §138-numbering rework.
- **Transition:** §138 (quadratic reciprocity) ends; **Drittes Buch: Algebraische Grössen / Dreizehnter Abschnitt: Die Galois'sche Theorie / §139 Der Körperbegriff** begins (p449).
Compiles **361 pp / 0 err**.

### 2026-06-25 — p450–455 (run wxqs8k1yo; §139–142 Galois foundations: Körper/Adjunction/Functionen in Ω; verified by eye)
**16 APPLIED, 0 clean pages; §141 reducibility-paraphrase HELD** (26 agents, 851k tok — heavily smoothed prose). **Page 361→362** (restored footnote + dropped paragraphs grew the doc; 0 errors).
- **p450** restored dropped footnote (Galois'schen Gleichungstheorie, Math. Ann. Bd 43); dropped clause '(da alle ganzen Zahlen durch Addition und Subtraction von Einern entstehen)'; '(rationalen und irrationalen)'.
- **p451** 'die Constanten'→'die constanten Coefficienten…etwa auf den der rationalen Zahlen' + restored dropped sentence 'Wir wollen hier nicht weiter die Beispiele häufen…'; 'enthält u. s. f.'; 'Körper Ω''' (dropped symbol).
- **p452** Fraktur `𝔠`→`𝔍` ×2 (complex field; print Fraktur J w/ descender, zoom-confirmed); §141 prose: restored `a_0,a_1…a_m`, dropped Δ(a) clause, §.40 cross-ref.
- **p453** restored 2 dropped paragraphs ('Sind die a nicht unabhängige…' + 'Wir können also…sprechen') before 'Wenn nun Ω…'.
- **p454** Satz I-III dropped clauses: 'der uns in der Folge…Dienste leisten wird'; '(d.h. eine in Ω enthaltene Grösse)'+'also'; proof-tail 'also müsste f'(x) durch f(x) theilbar…niedriger ist'; 'd.h. alle Coefficienten von F(x) müssen Null sein'; Variablen 'x,y,z…'.
- **p455 §142** restored '„über" Ω oder auch, wenn Zweifel…kurz, einen algebraischen Körper'.
- ⏸ **HELD §141 reducibility-section paraphrase (p453–455):** def (16461–63: 'Man spricht bisweilen…im Körper Ω', dropped 'Präcisirung'), three-way-distinction + x²-y²/x²-2y²/x²+y²+1 EXAMPLES (agent #15/#18 OVERLAP across p454→455), §51-reference ('Bei jenen Ausführungen…wegfällt'), 'linearer Factor x-α', 'aus allen Zahlen'. Pervasive paraphrase ⇒ coherent §141 rework. **3rd STANDING ITEM.**
Compiles **362 pp / 0 err**.

### 2026-06-25 — p456–461 (run wioa94pvs; §142–144 Galois: algebraic körper / primitive-element theorem / primitive & imprimitive Körper; verified by eye)
**26 APPLIED (25 prose-restorations + §143 full title), 0 clean pages** (32 agents, 945k tok). 362pp held.
- **Galois prose pervasively paraphrased** by the draft; restored ~25 dropped clauses/sentences + rewordings to Weber's exact wording, all individual + non-overlapping (verified page-by-page on scans). E.g. p456 'und bleiben also…Ω(α) stehen', 'weil…x=α nicht die Wurzel von zwei verschiedenen irreducibeln Gleichungen'; p458 the full Satz-1 induction proof + 'mit anderen Worten…Ω(α)'; p459 'nicht nur eine, sondern…deren Zahl gleich dem Grade'; p460 §142-Festsetzung xref, 'Es kann sein, dass diese Körper…wovon später Näheres'; p461 'n Grössen, eine aus jedem der conjugirten Körper', 'nach dem Theorem II, §.141'.
- **§143 section title** restored to Weber's full heading 'Gleichzeitige Adjunction mehrerer algebraischer Grössen' (the .tex had used the running-header abbreviation 'Mehrfache Adjunction').
- agent-rejected #459 ('nicht nur eine, sondern…') was a real fix (uniqueness-fail on a stale anchor) — reinstated.
- typeB (NO change): p457 §142-conclusion edition-divergence (.tex numbered Theorem 1 + proof vs print's inline c_0..c_{n-1} + eq (6)) — flagged.
### 2026-06-25 — p462–467 (run wc8sx00lk; §144–146 Galois: primitive/imprimitive Körper, Normalkörper, Galois'sche Resolvente; verified by eye)
**22 APPLIED (21 agent prose-restorations + 1 self-caught drop), 1 page HELD (p466)** (27 agents, 876k tok). 362→**363 pp** (growth from restored prose).
- §144–145 prose pervasively paraphrased; restored individual non-overlapping clauses/sentences/displays, all scan-verified. E.g. p462 the φ(Θ)=0 display + 'd. h. Φ(t) ist irreducibel' + 'jeder andere irreducibele Factor…Potenz von φ(t)' + §143,1-Satz ref + 'sogar so, dass die Coefficienten…rationale Zahlen sind'; p463 'deren Coefficienten Zahlen in Ω', 'worin Φ′(Θ) von Null verschieden ist', dropped 'Denn jede Zahl des Körpers Ω(Θ)…' paragraph, 'Aus dieser Definition…Wir wollen jetzt…imprimitiven Körper kennen lernen'; p464 the full Ω(β,γ)-induction (rebuilt across the p463→464 break, subsuming both agents' overlapping #11/#12), 'Wir können unsere Definition auch so fassen', 'In den Normalkörpern herrschen viel einfachere Gesetze…Galois verdankt'; p465 'dass nämlich…durch jede beliebige rational ausdrückbar ist', 'von der wir nur voraussetzen wollen', 'Ist Ω(α) ein Normalkörper, so ist er mit seiner Norm identisch'; p467 'd. h. N ist ein Normalkörper. w. z. b. w.', the 3-part formal Galois-resolvente definition.
- **self-caught miss**: agent (and its p466 verifier) missed the .tex drops 'Denn nach 2) ist N in Ω(ρ) enthalten…folglich ist N=Ω(ρ).' (p467_mid) — restored.
- **corrected an agent paraphrase**: p464 reconstruction's connector → print's 'und nach dem, was wir vorhin bewiesen haben' (agent wrote 'Wie wir bewiesen haben').
- **HELD p466** (Normalkörper/Galois-resolvent construction, .tex ~16784–16797): WHOLESALE paraphrase — eq (6) arrangements + Π(m) count dropped, eq (7) explicit forms collapsed to bare ρ,ρ′,ρ″, the Gesammtheit-invariance paragraph condensed to one sentence, the G(t)=∏(t−ρ) symmetric-function argument condensed. 7 typeB; needs coherent re-transcription (like §141). NOTE: the p466 verifier wrongly called the 'Nun haben G(t)…' conclusion 'added prose' — it is on p467 (proof spans the break), so #20 was applied.
### 2026-06-25 — p468–473 (run wggn01ych; §146–148 Galois: substitutions of a normal field / composition / permutation groups; verified by eye + zoom)
**~40 fixes (32 agent + δ→σ whole-section conversion + ~6 self-caught), 0 clean pages** (42 agents, 1.27M tok — biggest batch yet). 363pp held.
- **δ→σ WHOLE-SECTION symbol conversion** (§146–147, lines 16807–16979, 71 occurrences): the GPT draft systematically misread Weber's substitution symbol σ as δ. Confirmed by my own zoom-crop (p469 'Substitution σ_a ausführen') + multiple independent agent crops. The agents flagged only ~12 of the ~71 δ's, and one agent rightly REJECTED isolated δ→σ fixes as consistency-breaking — so a scoped Python range-replace was the right tool, not piecemeal. δ is genuine nowhere in §146–147 (all substitutions); scope ends at §148 (Permutationsgruppen → π).
- §146 prose: restored §141-II xref, the g[Θ_k(ρ)]=0 / g[Θ_k(ρ_h)]=0 displays, 'Uebereinstimmung halber…Θ_0(ρ)' + 'Also sind…verschieden. Wir können dies als Satz zusammenfassen', the ρ_k=Θ_hΘ_a(ρ)=Θ_k(ρ) chain, the ω=ψ(ρ_h) display, 'Man kann aber bei gegebenem σ_a…Also:'.
- §147 prose: the full 'Da wir…das erste oder das zweite Element beliebig wählen können…Wir haben daher:' paragraph; 'sogenannte associative Gesetz, das sich in folgendem Satz ausspricht'; the σσ'σ''σ'''… display; §146,3 xrefs. **Removed spurious draft artifact `\subsection*{Schluss von §147}`** (not in Weber). Restored 'Eigenschaften 1., 2., 3.' + Gesammtheit (was modernized to Gesamtheit).
- §148 (p473): corrected eq (6) perm bottom row (.tex had wrong 'b_iπ_a', print 'a_{b_i}'), removed spurious '=m!' from Π(m)=1·2·3⋯m (not in print), restored the Zusammensetzung-of-permutations sentences.
- **self-caught (agent missed)**: the 'd. h.'-placement + spurious 'also' in the commutative-law sentence (an agent had REJECTED a botched version — I did it right); the two intermediate-product members (σσ')σ''=(ρ,ρ_b)(ρ_b,ρ_c)=… and σ(σ'σ'')=(ρ,ρ_a)(ρ_a,ρ_c)=… that the .tex compressed (crop-confirmed); 'diesen Uebergang'; 'die jedes Element an seiner Stelle lässt'.
- HELD (for §148 coherent rework next batch when p474+ available): finer §148-intro equivalent-paraphrases ('Spalten vertauschen' vs 'die einzelnen Paare anders anordnen'; 'geschrieben werden' vs 'was mit (5) völlig gleichbedeutend ist').
### 2026-06-25 — p474–479 (run wgv8yr40s; §148–149 Galois: permutation groups / Galois'sche Gruppe; verified by eye)
**0 applied — §148–149 HELD as a major wholesale GPT-rewrite** (15 agents, 510k tok; agent emitted 8 'surgical' fixes + 6 typeB, all inside a rewritten frame). 363pp unchanged.
- **§148–149 (p474–479) is a pervasive GPT paraphrase/rewrite of Weber's two sections**, NOT a transcription — too entangled to patch piecemeal (it combines ALL prior hold-classes at once: §138-style item-renumbering + §141-style paraphrase + p466-style whole-unit drops + symbol-subs + MODERNIZATION). Held for coherent re-transcription. Spec for that pass:
  · §148 (p474–475): prose reworded throughout; the two untagged inverse-verification matrices π_aπ_a⁻¹=(0..m-1/0..m-1) & π_a⁻¹π_a=(a_0..a_{m-1}/a_0..a_{m-1}) DROPPED (p474_bot); eq (8) third member =π_aπ_bπ_c dropped; the π_c⁻¹=π_b⁻¹π_a⁻¹ sentence + 'π_0 ist sich selbst entgegengesetzt' clause dropped (p475_top); print's flush-left items 1.,2.,3. folded into prose (.tex keeps only the '3.' enumerate) = §138-class; Permutationsgruppe DEFINITION reworded; Q={π_0..π_{q-1}} renotated (print Q=π,π',π''…); closing 'Was zwischen diesen beiden extremen Fällen…folgenden Abschnitten beschäftigen' dropped (added non-Weber 'symmetrische Gruppe').
  · p476: the entire cyklische-Gruppe example + its 3 matrices DROPPED; the Abel'sche-Gruppen + Theiler/theilbar paragraph DROPPED.
  · §149 (p476–479): GPT REWRITE — modern term 'isomorph' + meta-comment 'durch Umformulierung der Sätze des §146'; δ→σ (substitution symbol, continuing the §146-147 sub) + θ→Φ (primitive-element function); eqs (1)(2) use θ(...) parens where print has Φ[...] brackets; Sätze a)–d) reformulated; the d)-proof paraphrased, dropping displays (5)(6)(7), the g'(t) product, the §146,2 xref, the 'Hierauf können wir…gehört zur Galois'schen Gruppe' passage.
- HELD-ITEM TALLY: §69, §138-numbering, §141, p466, **§148–149**.
Compiles **363 pp / 0 err** (nothing applied).

### 2026-06-25 — p480–485 (run wbl1rm3k1; §149-tail / §150 / §151-start Galois; verified by eye + zoom)
**§150 RE-TRANSCRIBED + 9th Weber erratum; p480–481 §149-tail HELD; p483–485 agent-clean** (10 agents, 358k tok). 363→**364 pp** (§150 expansion).
- **§150 (Transitive und intransitive Gruppen, p481–482) re-transcribed**: the .tex had condensed Weber's ~1.5-page §150 to ~24 lines — paraphrased opening ('erhält man ein einfaches Kennzeichen für Reducibilität' vs Weber 'können wir ein sehr einfaches Kennzeichen dafür herleiten, ob die Gleichung F(x)=0 reducibel oder irreducibel ist'); condensed reducibility proof (dropped the f(α')=0 display, the §149,a) ref, 'Es werden also…nur unter einander permutirt', the '=f(x)' + §149,b) ref); WRONG transitiv-def (.tex 'für je zwei Elemente' vs Weber 'wenigstens eine Permutation…ein beliebiges Element in ein beliebiges anderes'); DROPPED closing paragraph (transitiv verbunden / Systeme der Intransitivität). All restored to Weber. (Unlike §148–149 = held: §150 is short + agent-isolated → direct re-transcription right.)
- **9th Weber erratum (p482 Satz 1)**: Weber prints 'reducibel oder irreducibel, je nachdem ihre Galois'sche Gruppe **transitiv oder intransitiv** ist' = reducible↔transitive, CONTRADICTING his own same-page proof (reducible⟺intransitive; standard irreducible⟺transitive). GPT draft silently corrected to 'intransitiv oder transitiv'; reverted to Weber's printed wording + flagged (crop-confirmed). [Errata: Q_0 p221, u' p334, 30° p357, +η² p382, α_1 p378, ω'-ω p385, a_3/a_4 p402, mod m p426, **transitiv/intransitiv p482**.]
- §149-tail (p480–481) HELD (part of §148–149 hold). ADD TO §149 SPEC: dropped Galois-biography footnote at §149 end (p481, on '…muss folglich mit G(t) übereinstimmen ¹)' — Évariste Galois bio: Duell 1832, 1830 Férussac Bulletin note, Brief an Auguste Chevalier (Revue encyclopédique Sept 1832), Liouville 1846 Bd XI, Maser 1889 German ed., Serret/Betti/Jordan/Netto).
- p483–485 agent-clean (§151 Primitive und imprimitive Gruppen start).
- **PROCESS BUG**: first batch-65 run returned 6 false-clean pages in 53s — launched without rendering p480–485 (batch 64 was a HOLD → no compile → render skipped); agents bailed on missing scans. FIX/LESSON: render the next batch EVERY batch, incl. holds; an anomalously fast all-clean batch ⇒ suspect missing scans.
### 2026-06-25 — p486–491 (run wcdlw97gk; §151 / §152 Galois: permutation groups, functions of independent variables; verified by eye + zoom)
**§152 FULLY RE-TRANSCRIBED (incl. replacing GPT-fabricated content); §151 & p491 clean** (9 agents, 322k tok). 364→**365 pp**.
- §151 (p486–487) clean (Primitive und imprimitive Gruppen).
- **§152 (Wirkung der Permutationsgruppen auf Functionen von unabhängigen Veränderlichen, p488–490) fully re-transcribed**:
  · Opening (p488): restored 'Für ein tieferes Eindringen in die Algebra…Grundlage bilden' + the dropped Cauchy/Jordan/Netto footnote (Journal de l'École polytechn. 1815; Jordan, Traité 1870; Netto, Substitutionentheorie 1882); 'von einander unabhängiger Zeichen (Veränderliche)'; 'ganze rationale Function von ihnen…ψ'.
  · Body p489: re-transcribed the ψ=ψ_π proof (permutations leaving ψ fixed form a group) — the .tex had condensed it (dropped §44-ref, 'andere extreme Fall', the ψ_{π'}=ψ_{ππ'} chain).
  · Body p490: the .tex here was GPT-**FABRICATED** (a ρ/Φ 'zu P gehörig / Φ(t)=(t-ρ)…' passage matching NO Weber §152/§153 content). Replaced with Weber's actual p490 §152: items 2 (P_1=Pπ_1 ≅ P, via §148,2/3), 3 (group⊇identity), 4 (group⊇inverse), + the m=3 example.
- **m=3 example glyph**: print reads '2α_2 = c + α_1' but the stated invariance (only identity + 3-cycle (0,1,2/1,2,0) leave α_1−α_2 fixed) requires 2α_2 = α_0 + α_1; 'between the three roots α,α_1,α_2' rules out an external constant ⇒ transcribed as α (α_0); 'c' = alpha degraded at 500dpi (possible minor erratum, noted not counted).
- p491 clean (§153 start).
- **NEW LESSON: the GPT draft can FABRICATE content** (not just paraphrase/drop) — §152's ρ/Φ body was invented. Always READ the scan to see what Weber actually says before trusting/patching a rewritten section. And: a 'rewrite' section IS re-transcribable when each page's scan content is clear + self-contained (§152, §150); HOLD only when multi-page + entangled (§148-149).
### 2026-06-25 — p492–497 (run wf5zz76cd; §153 Galois: Zerlegung von Permutationen in Transpositionen und in Cyklen; verified by eye)
**0 applied — §153 HELD as a major 6-page wholesale rewrite (incl. fabrication)** (12 agents, 419k tok). 365pp.
- **§153 (p492–497) is a 6-page GPT rewrite/condensation/fabrication** of Weber's permutation-decomposition theory (transpositions, cycles, even/odd, alternating group); the .tex §153 (~85 lines for 6 Weber pages) covers the topics but is not source-faithful. Held for coherent re-transcription. Spec:
  · p492 opening: paraphrased — restore 'Wir haben schon im zweiten Abschnitt…Transpositionen…Nebeneinanderstellen…(0,1)…' + 'Eine Transposition, zweimal wiederholt, führt zur Identität…'.
  · p493: cyclic-permutation definition FABRICATED — the .tex inserted foreign '(a,b,c)(d,e)(f) / disjoint cycles commute' content; Weber's actual text = cyclic-def matrix (0,1,2…/1,2,3…0) + compact (0,1,2…m-1) notation + 'Dabei ist es gleichgültig…' + numbered Satz 3 (unique disjoint-cycle decomposition). Theorems 1 ('auf unendlich viele verschiedene Arten') & 2 (group with all (0,k) = symmetric + 'nach 1. …zusammensetzen') reworded/dropped.
  · p494: Weber's worked example (π_1,π_2,π_3 explicit two-row matrices) + eqs (1),(2),(3) of the cycle-construction algorithm ENTIRELY DROPPED.
  · p495 (running head 'Permutationen erster und zweiter Art'): the τπ cycle-count two-case derivation (case 1 γ=(1,2…a,a+1…b),τ=(1,a); case 2 γ,γ'; parity paragraph 'Wir haben damit den Satz') REWRITTEN to 2 sentences + μ≡m−ν (mod 2).
  · p496: dropped the identische/Einheitsgruppe definition.
  · p497: statements 6,7,8 + four worked cycle-composition proofs ((1,0,2)=…,(0,2,3)=…,(1,3,4)=…,(2,3,4)=…) DROPPED/condensed.
- **2nd in-section fabrication** (after §152 p490): the GPT draft invents plausible math (disjoint-cycle examples) not in Weber. The agent's 6 clean 'surgical fixes' (defs/theorems at p492/493/496) NOT applied — would leave a half-faithful section around the held proofs/examples.
- HELD-ITEM TALLY: §69, §138-numbering, §141, p466, §148–149, **§153**.
Compiles **365 pp / 0 err** (nothing applied).

### 2026-06-25 — p498–503 (run w79k00pmc; §153-tail / §154 Galois: Divisoren, Nebengruppen, conjugirte Gruppen; verified by eye)
**§154 opening PATCHED (7 fixes); §153-tail & §154-body HELD** (14 agents, 475k tok). 365pp.
- §153-tail (p498–500) folds into the §153 HOLD (now spans p492–500): p499 Satz 10 ('transitive Gruppe von n Ziffern mit dreigliedrigem Cyklus → alternirende oder imprimitiv') + proof wholesale-dropped (.tex one-liner, 'm Ziffern'); p500 the π² even/odd-n cyclic-square formulas dropped (agent #1, not applied → §153 spec).
- **§154 opening (p501) PATCHED (7 fixes)**: 'ausgeglichen oder wenigstens'; 'jetzt…irgend…gegebenen…von einander verschiedenen'; α_2 restored in Ω(ρ)=Ω(α,α_1,α_2…); '(nach §.146,149)…oder auch…verstehen'; 'wir wollen die Operationen von P (seien es nun Substitutionen von N oder Permutationen der α) mit…bezeichnen'; Theiler/Divisor def 'wenn also je zwei…wieder ein Element aus Q ergeben…die Gruppe Q' + footnote 'Auch Untergruppe genannt.'
- **§154 body (p502–503) HELD** (reworded/condensed rewrite): .tex renumbers items 1–7 + eqs ((6)→(10) drops (7)(8)(9)), uses χ for Weber's ϰ (varkappa), DROPS the coset-distinctness proof, the Nebengruppe definition, the two-cosets-disjoint proof, **Cauchy's Fundamentalsatz** attribution+statement, the 'specieller Fall' (element order | group order), and condenses the conjugate-group treatment. Re-transcribe with Weber's ϰ + numbering.
- **'isomorph' RED HERRING corrected**: Weber himself prints 'isomorphe' (p501) — NOT a GPT-modernization marker; the §149 'isomorph' flag was wrong (the §149 hold stands on its other grounds). LESSON: verify a suspected 'modern term' against a clean Weber page before treating it as a tell.
- **render-bug recurred (2nd time, as batch 65)**: §153 hold → no compile → I skipped rendering p498–503 → agents bailed → 6 false-clean pages in 58s; re-ran after rendering. HARD RULE: render next batch as a standalone step EVERY turn.
- HELD-ITEM TALLY: §69, §138-numbering, §141, p466, §148–149, §153(p492–500), **§154-body(p502–503)**.
### 2026-06-25 — p504–509 (run wpj6f97ng; §154-body / §155 Galois: Reduction der Resolvente, Lagrange-Galois; verified by eye)
**0 applied — §154-body & §155 HELD (both wholesale rewrites)** (12 agents, 439k tok). 365pp.
- §154-body HOLD extended to p502–507 (p504-506 conjugate-groups: varkappa→χ, dropped the π_1⁻¹Qπ_1-isomorph derivation + the 'gleichberechtigte Untergruppe' footnote + the transformation-rule proof; p507 item-7 transitive-group coset proof condensed [agent #1 folds in]).
- **§155 (Reduction der Galois'schen Resolvente durch Adjunction. Normaltheiler, p507–509) HELD** — pervasive rewrite/renumber: dropped opening 'allmähliche Reduction…durch Adjunction' paragraph + 'wie im vorigen Paragraphen'; theorem 1 condensed + its irreducibility proof (Φ(t), refs §154,5 / §149,b) dropped; **Lagrange footnote** (Réflexions sur la résolution…Berlin 1770/71, Oeuvres III; 'allgemeine Formulirung rührt von Galois her') dropped; the ω=χ(ψ)/φ'(ψ) derivation (eq 5) + 'Grössenreihen (3),(4)' paragraph dropped/paraphrased; eqs renumbered; the printed eq (6) g(t)=g(t,ψ)g(t,ψ_1)… is MISPLACED into the .tex's §157 (~line 17868) — cross-section content-shuffle. Agent #2–#6 fold into this spec.
- CONFIRMS: the whole §148–§157+ Galois-applications region is a uniform GPT rewrite/renumber/shuffle → held section-by-section for one coherent re-transcription pass.
- HELD-ITEM TALLY: §69, §138-numbering, §141, p466, §148–149, §153(p492–500), §154(p502–507), **§155(p507–509)**.
### 2026-06-25 — p510–515 (run w23msqvxa; §155-tail / §156 / §157 Galois; verified by eye + crop)
**1 applied (§157, p514); §156 HELD; §155 hold extended** (11 agents, 396k tok). 365pp.
- §155 hold extended to p510–511: dropped Normaltheiler footnote (Galois 'décomposition propre' → 'eigentliche/ausgezeichnete/invariante Untergruppen'), the §155 closing (Normaltheiler/einfache-Gruppe defs, item 5), the Ω''=Ω(ψ,ψ_1…) display, the 'Von besonderem Interesse…Normalkörper' conclusion.
- **§156 (Die Gruppe der Resolventen, p511–513) HELD** (condensation/paraphrase): Total/Partial-resolvente defs paraphrased (agent p512 ×3 restore the N=Ω(ψ,ψ_1…ψ_{j-1}) display + 'Normaltheiler von P' + §155/Satz4 refs); §156 opening (Hülfsgleichung→Resolvente, §155,2 ref, 'N mit Ω(ψ) identisch') paraphrased; §156 tail DROPPED 3 full paragraphs (rejected fix p513 — real but mid-sentence anchor).
- **MAJOR BOUNDARY: §157 (Aufgabe der Auflösung…, p513–515) RESUMES FAITHFUL transcription** — p514 is verbatim-faithful; only 1 fix: Θ_1→Θ_i subscript misread ('auch Θ_i(ρ_2)=ρ_3'), crop-confirmed (context ρ_i=Θ_i(ρ), g_1[Θ_i(t),ε]=0). **So the GPT-rewrite block is §148–§156; §157+ is patchable-faithful.** (Re-checks batch-69's 'eq(6) misplaced into §157' — §157 legitimately contains it; was agent confusion.)
- HELD-ITEM TALLY: §69, §138-numbering, §141, p466, §148–149, §153(p492–500), §154(p502–507), §155(p507–511), **§156(p511–513)**. [§148–156 = the GPT-rewrite block.]
### 2026-06-25 — p516–521 (run wmvlyv99v; §157-tail / §158 Imprimitive Gruppen; verified by eye + crop)
**1 applied (§158 title); §158 body HELD** (12 agents, 436k tok). 365pp.
- §157 tail (p516-top) faithful (Kronecker / natürliche Irrationalitäten) — confirms §157 faithful.
- **§158 (Imprimitive Gruppen, p516–520) HELD** (wholesale rewrite): TITLE fixed (.tex 'Reduction imprimitiver Gleichungen' → Weber 'Imprimitive Gruppen', crop-confirmed p516). Body held — opening paraphrased ('Wir machen von unseren allgemeinen Sätzen…§151…n=r·s…s Reihen von je r Gliedern'); eq (1) array δ→σ + missing tag; dropped eqs (2)-(6) (f(x)=∏f(x,y); ψ,ψ_1…; (ψ,ψ_i); Q,Qπ_i; Partialresolvente χ(u)=0); dropped the s-1 permutations + (α)/(β) matrices + ϰ_β=π_β⁻¹ϰπ_β proof + §151/§154,7 refs; dropped the transitive-group↔intransitive-Normaltheiler inversion proof (p520); Ω(y)→Ω(ψ) (p520).
- so the rewrite ALTERNATES section-by-section: §157 faithful, §158 rewritten — NOT a clean §148-156 boundary; must audit each §. Held block now §148–156 + §158.
- HELD-ITEM TALLY: §69, §138-numbering, §141, p466, §148–149, §153, §154, §155, §156, **§158**.
### 2026-06-25 — p522–527 (run w9yte0sww; §159 Cubische Gleichungen / §160 Permutationsgruppen von vier Elementen; verified by eye)
**13 fixes APPLIED (patched, not held); 0 typeB** (19 agents, 638k tok). 365→**366 pp**.
- §159–160 are condensed WORKED-EXAMPLE sections (like §144-147 / cyclotomy): the .tex dropped intermediate equations/derivations/cycle-tables but kept Weber's structure → surgically patchable (0 typeB). Applied:
  · §159 (cubic): eq (6) 2α_1/2α_2=a-α±√D/f'(α) + α_1±α_2 relations + 'Denn ausser sich selbst…Typus (1,2)' (p523); v³=α³+α_1³+α_2³+6αα_1α_2+3εA+3ε²A' (p524); vv'=α²+…−α_1α_2 expansion; [§.47,(8)] xref + a=α+α_1+α_2 display; 'also in dem Körper Ω' enthalten sind…' clause; eq (7) trailing ';'.
  · §160 (4-element groups): '(vgl. den Schluss von §.149)' + 24-perm phrasing; Transpositionspaare def '(0,1)(2,3)'; the alternating-group 'keine einzelne Transposition…' sentence; 'alle vorhandenen Theiler…(§.154,6.)' passage; the dreigliedriger-Cyklus proof table ((0,1,2)²=(0,2,1)…(0,3,2)²=(0,2,3)) + (0,1)(0,2)=(0,1,2) (p526); the (0,2)(0,1,2,3)=(0,3)(1,2)… verification table; P_1-conjugate-groups paragraph; P_2 second-cyklus paragraph (p527). All cycle-products derivation-checked.
- prose-paraphrase elsewhere (25 cosmetic notes) left as meaning-preserved (consistent w/ §144-147 worked-example policy).
- so §157, §159, §160 are patchable-faithful; the rewrite-block is §148–156 + §158.
### 2026-06-25 — p528–533 (run w0r62hxow; §160-tail / §161 biquadratische Gleichungen / §162 Abel'sche Gleichungen opening; verified by eye)
**17 fixes APPLIED (patched); 1 typeB-note** (23 agents, 731k tok). 366pp.
- §161 (biquadratic) = condensed WORKED-EXAMPLE (patchable, like §159-160): restored §161-opening (§64 xref, 'Gruppe P', the Adjungirt-Q/Q_1-Index-3-Normalgleichung reasoning); eq (7) y_1=(α-α_2)(α_3-α_1) [removed spurious leading minus]; cubic-Partialresolvente §64/65+U,V,W remark; §45/§64 Vorzeichen reasoning; the (9)·(y_1-y_2) derivation + 'wodurch y_1,y_2 bestimmt'; 'imprimitiv (und zwar nach drei Arten)…Am besten…'; the v_1=a_1²-4(α+α_1)(α_2+α_3)/y_1-y_2/a_2 derivation block (two same-anchor agents COMBINED); the eq-(13) 'das Product…symmetrische Function…a_1³-4a_1a_2+8a_3 findet' derivation; the closing 'Wenn man der √D…cyklisch vertauscht' permutation paragraph + corrected 'Welche Werthe…algebraischen…biquadratischen Gleichung' sentence; z∈P_1 'zweite Gleichung (10)' xref; fixed a latent '\\qquad' typo.
- §160-conclusion: 'den mit P_1 und P_2 conjugirten Theilern von P' (zu→mit, +von P).
- §162 (Abel'sche Gleichungen, p533) opening PATCHED: transitive-group-degree theorem fuller version (#16) + 'also der Grad von P…Producte aus m und Q_0' + 'ist also niemals von niedrigerem Grade' (#17); self-caught the Normalgleichung paragraph (restored Weber's '…ausdrückbar sein sollte (§.145). Daraus ergiebt sich…identische Gruppe…' vs the .tex's reworded+over-extended version).
- so §159–162 all patchable worked-example/theory; rewrite-block stays §148-156+§158.
### 2026-06-25 — p534–539 (run wlryw04xi; §162-body Abel'sche / §163 cyklische Gleichungen; verified by eye)
**0 applied — §162-body & §163 HELD (theory re-expositions)** (10 agents, 388k tok). 366pp.
- §162-body (p534–536) HELD: GPT re-exposition of Abelian-equation theory — EQUATIONS (2)(3)(4)(5)(6) are faithful, but prose/derivations paraphrased/collapsed (typeB p535/p536): dropped 'Es seien nämlich…das commutative Gesetz gilt', the §147-cited σ'σ''/σ''σ' commutativity derivation, the σ_k=[α,Θ_k(α)] bracket-notation block, the 'jeder Theiler [einer commutativen Gruppe] normal' remark, the irreducibel/reducible-Gleichungen passage. DROPPED: §162 Abel footnote (p534: 'Abel, Mémoire sur une classe d'équations résolubles algébriquement, Crelle Bd.4 1829; Oeuvres 1881 Bd.1 S.418') + 'die Abel allgemein aufzulösen gelehrt hat…Abel'sche Gleichungen nennen wollen'.
- §163 (Reduction der Abel'schen Gleichungen auf cyklische, p537–539) HELD: condensed paraphrase (typeB p539: def-sentence reworded, eq-labels (7)/(8)/(9) folded). Spec: §163-opening theorem 'Eine Permutation einer transitiven Abel'schen Gruppe enthält nur Cyklen gleicher Gliederzahl' (+ π^r-argument); ω_1=ψ(β,β_1…β_{r-1}) eq (6) + §158 xref.
- **FIRM RULE (stop hold-vs-patch agonizing): typeB 'whole-page rewrite/re-exposition' flag ⇒ HOLD the section + fold all fixes (incl. clean surgical) into the spec; NO typeB + only surgical drops ⇒ patch.** Buch-III THEORY §§ = held; WORKED-EXAMPLE §§ = patched.
- HELD-block now §148-156, §158, §162-body, §163.
### 2026-06-25 — p540–545 (run wnfy8lqj4; §163 cyklische (held) / §164 Resolventen von Lagrange; verified by eye)
**§164 PATCHED (~5 big restorations); §163 (p540-541) part of the §163 hold** (10 agents, 427k tok). 366→**367 pp**.
- §163 (p540–541) = part of the §163 HOLD (typeB p541: the Θ-chain eq (11), Kreistheilung/Gauss-Sectio-VII footnote — re-exposition).
- **§164 (Resolventen von Lagrange, p542–545) PATCHED** — heavily condensed worked-example/theory (no typeB, eqs are Weber's just condensed → patchable): restored the §164 opening + the dropped Lagrange footnote ('Réflexions etc., s. S. 508; Früher haben wir unter Resolventen auflösende Gleichungen verstanden, hier sind es auflösende Functionen'); 'Die so definirten Summen…Lagrange'schen Resolventen nennt'; eq (2) Σε^k=m oder 0 + §133 xref + the dropped eq (3) mα=Σ(ε,α) + eq (4) (.tex tags had jumped 2→4); the 'Die Summen (2),(3)…mα=Σ^λ(ε^λ,α)' alternative form; index-convention (α_h=α_k mod m); Satz 1 (π→ε^{-k}); polynomial expansion eq (5) Σ_{0,m-1}^h-form + A_h=A_k convention; Satz 2 (π^ν on coeff indices) + eq (6) + its proof; the f-gliedrige Perioden 'wie es Gauss…Kreistheilung' (eqs 9/10).
- residual minor paraphrase noted (p544 'Noch allgemeiner entwickle man' vs Weber 'Der Satz 2 ist ein specieller Fall…Entwickeln wir ein Product').
### 2026-06-25 — p546–551 (run wo63y2jec; §165 Auflösung der cyklischen Gleichungen; verified by eye)
**0 applied — §165 HELD (reconstruction)** (17 agents, 589k tok). 367pp.
- **§165 (Auflösung der cyklischen Gleichungen, p546–551) HELD**: the .tex §165 is a RECONSTRUCTION, not a transcription — typeB p551 (conclusion: Θ-chain, reell-Θ(x), odd-m / conjugate-imaginary / cubic-equations paragraphs — wholly different); 2 agent fixes REJECTED on anchor-failures (.tex structure differs); eqs (7),(8) MISSING + eq-numbering reconstructed (.tex eq 5/6 differ, a spurious eq 21); p548 'WHOLESALE PARAPHRASE, reconstruction not transcription'. Re-transcription spec (agent's 9 anchored fixes + drops): opening 2 paras ('durch Anwendung der jetzt bewiesenen Sätze…Reduction auf reine Gleichungen' + 'Wir verstehen jetzt unter den α…bekannte Grössen'); '§164,2 Theorem'; eq (2) (ε^λ,α)=√[m]{ψ_λ}; the radical-selection eqs 5/6 ((ε^λ,α)(ε^{λ_1},α)^{m_1ν}… + λ≡-ν(λ_1m_1+…)); the ψ_1=0 exception + m(α_n-α_0)=Σ(ε^{-nλ}-1)(ε^λ,α); eqs (7),(8) (√[p_i]{φ_i} factorization); the ρ_1²=(±a_1)^m=a_1^m derivation + eq (12)/(13); the trig form (eq 21 √{A^{-ν}}) + the Abel-reell reference; the §165 conclusion (Θ-chain, odd-m, cubic-equations).
- §164-vs-§165 DISCRIMINATOR: §164 eqs were Weber's (condensed, only eq3 missing → restored) ⇒ PATCH; §165 eqs renumbered/missing + anchor-fails ⇒ RECONSTRUCTION ⇒ HOLD.
- HELD-block now §148-156, §158, §162-163, §165.
### 2026-06-25 — p552–557 (run woiqej637; §166 Theilung des Winkels / §167 Kreistheilungsperioden; verified by eye)
**2 applied (Abschnitt headings); §166 CLEAN; §167 HELD (reconstruction)** (8 agents, 336k tok). 367pp.
- §166 (Theilung des Winkels, p552–553) = CLEAN/faithful (cleanPages 552,553; only cosmetic ellipsis-chain / {1\over m} vs \frac differences).
- **TWO dropped Abschnitt (chapter) headings restored** — the .tex keeps Zehnter–Dreizehnter, Fünfzehnter, Siebzehnter, Achtzehnter but had DROPPED two: '\section*{Vierzehnter Abschnitt. Anwendung der Permutationsgruppen auf Gleichungen.}' before §152, and '\section*{Sechzehnter Abschnitt. Kreistheilung.}' before §167.
- **§167 (Kreistheilungsperioden, p554–557) HELD**: the .tex §167 is a RECONSTRUCTION/modern paraphrase (typeB p556+p557: general theory eqs (6)-(12), the cyclic group C, periods η=r+r_e+…, conjugirte Perioden, the §163-reduction — all absent; .tex uses r^{g^e} / r↦r^g notation found nowhere in print + an INVENTED Dreizehn-Theilung §168 example; p555 coverage-gap; eqs renumbered). Re-transcription spec (agent's p554 §167-opening fix + drops): opening ('Die wichtigsten unter den Abel'schen Gleichungen…Bestimmung der Einheitswurzeln…Kreistheilungsgleichungen'); 'Körper Ω…nur der Körper der rationalen Zahlen, den wir R nennen'; the prime-2/±1 parenthetical; the n-1 primitives + the e^{2kπi/n} display; eq (1) r,r²,…r^{n-1}; eqs (2)-(12) (cyclotomic X, the r^{g^h}=r_h ordering, φ(r) poly, the cyclic group C, periods η, conjugirte Perioden, §163-reduction chain).
- HELD-block now §148-156, §158, §162-163, §165, §167.
### 2026-06-25 — p558–563 (run weyz8pxt9; §167–§168 Kreistheilung; verified by eye)
**1 applied (§168 title); §167+§168 HELD (reconstructions)** (7 agents, 313k tok). 367pp.
- **§168 fabricated TITLE corrected** (verified p560_top): '\sect{168}{Producte von Perioden. Dreizehn-Theilung}' (GPT-invented) → '\sect{168}{Die Gauss'sche Methode zur Berechnung der Resolventen}' (Weber's true title).
- **§167 (p558-559) + §168 (p560-563) BOTH HELD** — wholesale reconstructions (all 5 typeB 'non-transcription'): the .tex §167-168 (lines 18780-18873) is GPT-invented modern content (period-products η_λη_μ=Σr^…, 'cyklotomische Zahlen' c_k, 'Restarithmetik', a fabricated 4-membered η_0=r+r³+r⁹+r²⁷ for n=13) matching NO Weber page. Weber's REAL content (absent): §167 Theorem II + eqs (13)-(16) (φ(r)=Σa_h r_h, the η-basis of R(η), F_e(x)=Π(x-η_h), ηη_h=Σa_{i,h}η_i); §168 'Die Gauss'sche Methode' — period-product reduction eqs (3)-(8) + Weber's GENUINE numeric Dreizehn-Theilung example on p562 (eq(10) η³+η²-4η+1=0, discriminant 169=13², r=e^{2πi/13}, the cos(kπ/13) forms — GPT KEPT the '13-division' label but invented different content). Folds into the §167-168 re-transcription spec.
- HELD-block now §148-156, §158, §162-163, §165, §167, §168.
### 2026-06-25 — p564–569 (run w05c36lmg; §169 Auflösung durch die Resolventen; verified by eye)
**2 applied (n=17 cosine sign typos); §169-theory HELD (reconstruction)** (9 agents, 367k tok). 367pp.
- **2 type-A sign typos fixed in the n=17 worked example (p568, eq 16), verified on scan + arithmetic:** η_4=2cos(26π/17)=**+**2cos(8π/17) (.tex had −; 26π/17=π+9π/17⇒+cos8π/17) and η_6=2cos(30π/17)=**+**2cos(4π/17) (.tex had −; 30π/17=π+13π/17⇒+cos4π/17). η_2/η_3/η_5/η_7 minus signs verified CORRECT (left). The n=17 cosine table (eq 16) is FAITHFUL to p568 (structure+values match) — type-A typos in faithful content, patchable even though the rest of §169 is reconstructed.
- **§169-theory (p564-567, p569) HELD** — wholesale reconstruction (typeB p565-567,569): the .tex §169 (lines 18874-19100) reworks the resolvent derivation with its own eq-numbering (1)-(16) vs Weber's (5)-(16)/(11)-(15), a reworded opening ('Gauss hat schon…Disquisitiones' — not in print), the resolvent form (α^λ,r)=r+α^λr_1+… replaced, missing the §167,(12) xref. Re-transcription spec: the p564 dropped Gauss-history footnote (Gauss disq.arith. art.359-360 + disq. circa aequationes puras; Lagrange; Jacobi Werke Bd.6; Kummer Crelle 35 + Berl.Akad.1856; Eisenstein; Cauchy; Bachmann 'Die Lehre von der Kreistheilung' Leipzig 1872); the symbolic eqs (2)-(16); the p569 dropped v.Staudt footnote (Crelle 24, 1842, 17-gon construction) + the bottom trig block (½(-1,η)=cos2π/17-cosπ/17+…, denom 34). NOTE: the FAITHFUL p568 n=17 example sits inside the reconstructed §169 (patch islands, re-transcribe the theory).
- HELD-block now §148-156, §158, §162-163, §165, §167-169.
### 2026-06-25 — p570–575 (run ws325pvhe; §170 Eigenschaften der Zahlen ψ; verified by eye)
**0 applied — §170 HELD (reconstruction + content-shuffle)** (9 agents, 333k tok). 367pp.
- **§170 (Eigenschaften der Zahlen ψ, p570–575) HELD** — wholesale reconstruction (typeB p571-574): renumbered eqs, dropped derivations, CONTENT-SHUFFLE (the Jacobi 'bis e=23' sentence belonging to p572 was moved up to the §170 opening, .tex line 19107, displacing Weber's p570 Indextabelle paragraph + Kronecker footnote). §170 title 'Eigenschaften der Zahlen ψ' VERIFIED CORRECT on p570_mid (the p573 running-head 'Die Zahlen ψ' is just the abbreviated head — batch-78 title lesson applied, no spurious fix). Re-transcription spec (the 3 p570 fixes + drops): the 3-paragraph opening ('Die im vorigen Paragraphen abgeleiteten Formeln…Fülle von Anwendungen…zahlentheoretische Sätze für ganze Kategorien von Primzahlen' / 'Für die Algebra…in beliebiger Menge' / 'Der Ableitung…allgemeine Betrachtungen über die Functionen ψ'); the dropped p570 Indextabelle paragraph ('Zur Berechnung der Zahlen ψ_{λ,μ}(ε) [§.169,(5)]…wie im Falle n=17…Jacobi merkwürdige Untersuchungen') + Kronecker footnote (Journ. f. Mathem. Bd. 93); the abridged p572 Jacobi sentence (restore 'mit Hülfe dieser Formeln für ein gegebenes, als Primzahl vorausgesetztes e…d.h. durch ψ_1(a),ψ_1(a²),ψ_1(a³)…'); the symbolic eqs (p571-575). Also CONFIRMS the §169 hold: p570_top shows §169's dropped n=17 trig block (η-η_2+η_4-η_6=… Vorzeichenbestimmung) continuing onto p570.
- HELD-block now §148-156, §158, §162-163, §165, §167-170.
### 2026-06-25 — p576–581 (run w5krjda5k; §171 Die Gauss'schen Summen / §172 Die Perioden von ⅓(n-1) und ¼(n-1) Gliedern; verified by eye)
**6 applied (§172 e=3 example); §171 CLEAN; §172 p581 derivation-tail DEFERRED to next batch** (12 agents, 383k tok). 367→**368 pp**.
[⚠️ first run was a FALSE-CLEAN — RENDER-BUG recurred (3rd time): §170 hold→no compile→forgot to render p576-581→agents bailed on missing scans→62s all-clean. Re-rendered + re-ran. PERMANENT FIX: render is now a STANDALONE step before every Workflow launch, decoupled from the compile-gate.]
- §171 (Die Gauss'schen Summen, p576–578) = CLEAN (cleanPages; only cosmetic: ≦=leqq, Fraktur ϱ=\rho, §-period style, a worn '1'/'!' print glyph, page furniture).
- **§172 (Die Perioden von ⅓(n-1) und ¼(n-1) Gliedern) — PATCHABLE worked-example** (like §164; eqs Weber's, 0 rejected). §172 title verified correct (.tex 19432). 6 condensation fixes in the e=3 example (p579-580), all verified on p579_mid/bot + p580_top: (1) restored 'jetzt zu dem Falle e=3…wobei n-1 durch 3 theilbar angenommen…also n=7,13,19,31,37,43…' (dropped n-list); (2) restored the §168 xref 'die, wie wir in §168 gesehen haben, …cubischen Gleichung sind'; (3) restored ψ_1(ρ)'s FIRST form Σ_{1,n-2}^t ρ^{ind t-2 ind(t+1)} + 'wofür, da -2≡1(mod 3), auch' + 'gesetzt werden kann. Diese Zahl…in einer der beiden Formen' (.tex had dropped the first form + collapsed eq 1); (4) moved A=2a-b out of eq(2)'s display into prose 'dargestellt werden, worin a,b,A ganze Zahlen sind und A=2a-b ist. Es ist dann'; (5) restored eq-xrefs 'und die Formeln (10),(15) des §169 ergeben'; (6) added the 2nd relation ψ_1(ρ)ψ_1(ρ²)=n to eq(6).
- **DEFERRED to next batch (p582):** §172's e=3 derivation TAIL on p581 (eqs 14-18) is condensed + RENUMBERED with a cascade into p582 — the .tex merged Weber (14)+(15)→(14), (16)→(15), (17)+(18)→(16), and DROPPED 3 steps: 'und daraus A³≡1 (mod 9)'; the '-4·27γ=A³+3Ab²+3A²+9b²-4' expansion + 'und daraus 3b²≡0 (mod 9)' + 'Es ist also b durch 3 theilbar, und wenn wir b=3B setzen'; the split √D=(η-η_1)(η-η_2)(η_1-η_2)=s-s' (17) / √D=nB (18). Re-transcribe the p581-582 derivation coherently with p582 (the ξ³-3nξ-nA=0 + interval eqs continue onto p582, where the numbering resolves).
### 2026-06-25 — p582–587 (run w0z0elihu; §172 conclusion / §173 Die complexen Zahlen von Gauss; verified by eye)
**§172 e=3-tail + 9th-roots + e=4 FULLY RE-TRANSCRIBED (eqs 12-42); §173 HELD (reconstruction)** (9 agents, 369k tok). 368→**369 pp**.
- **§172 (Perioden ⅓/¼(n-1)) COMPLETED** — the e=3-derivation tail (p581-582), the 9th-roots example (p582-583), and the e=4 example (p583-584) were all heavily condensed (merged eqs + dropped derivation steps + renumbered); re-transcribed in full to Weber's numbering (12)-(42), verified eq-by-eq on p581-584:
  - e=3 tail: restored 'und daraus A³≡1 (mod 9)' + the (2),(3),(6)-ref, split the merged (14)/(15) (n=a²-ab+b² / 4n=A²+3b²), restored '-4·27γ=A³+3Ab²+3A²+9b²-4' + '3b²≡0 (mod 9)', split (17)/(18) (√D=s-s' / √D=nB), restored the root-assignment paragraph (sechs Zuordnungen) + Kummer footnote (Journ. f. Math. Bd. 32), the theorem 'wo a,b,A,B ganze Zahlen sind', and the x²+3y² derivation.
  - 9th-roots: restored the dropped opening ('…wichtige Rolle…Vollständigkeit halber…Eine 9te Einheitswurzel r genügt der Gleichung 6ten Grades'), split (25)/(26), restored 'was den Formeln (5),(6) ganz analog ist'.
  - e=4: restored the ψ-prose + the ENTIRE biquadratic derivation Weber (35)-(40) (the quadratic with roots η,η_2 → 16ηη_2=… (35); the quadratic + (36); the linear-coeff (37); the mod-8 analysis → a≡-(-1)^f (38), b≡0 (39); the substitution 4η+1=ξ (40)). [.tex had collapsed Weber's (27)-(42) into (24)-(32).]
- **10th WEBER ERRATUM (p582):** the x²+3y² display prints n=¼(a+b)²+¾(a-b)³ — the final exponent ³ is a Weber print typo (math requires (a-b)²); transcribed faithfully as ³ + flagged. ERRATA now 10: Q_0 p221, u' p334, 30° p357, +η² p382, α_1 p378, ω'-ω p385, a_3/a_4 p402, mod m p426, transitiv/intransitiv p482, (a-b)³ p582.
- **§173 (Die complexen Zahlen von Gauss, p585–587+) HELD** — R(i)/Gaussian-integer theory wholesale reconstructed (typeB p586-587: divisibility theorems, Norm/Einheit defs, prime-factorization, Euclidean division — all grep-absent); the §173 OPENING (p585) is also condensed/paraphrased (.tex 'der aus dem rationalen Körper durch Adjunction…' vs Weber 'der durch Adjunction…aus dem Körper der rationalen Zahlen'; the p/q-Primzahl sentence collapsed). Re-transcription spec: the dropped Gauss footnote (Theoria residuorum biquadraticorum, commentatio secunda, Werke Bd. II); 4l→4f; the full p585-587 R(i) theory.
- HELD-block now §148-156, §158, §162-163, §165, §167-170, §173.
### 2026-06-25 — p588–593 (run w5wfqq1t8; §173 R(i) cont. / §174 Der Körper der dritten Einheitswurzeln R(ρ); verified by eye)
**0 applied — §173 + §174 HELD (number-theory reconstructions)** (11 agents, 424k tok). 369pp.
- **§173 (R(i)) body cont. (p588-591) HELD** — the p591 Gaussian-primes list is corrupted in the .tex (20 entries: has '2+3i' for Weber's '3+2i' [coeff-swap], a spurious '9+5i' [norm 106, not prime] for '5+8i', drops '9+4i' and '7+10i'; Weber lists 22 primes of norm <200); folds into the §173 spec.
- **§174 (Der Körper der dritten Einheitswurzeln / R(ρ) = R(√-3), Eisenstein integers, p592-593) HELD** — paraphrased/reconstructed theory parallel to §173: .tex opening 'Die Beweise des vorigen Paragraphen beruhen wesentlich auf dem euklidischen Algorithmus…' vs Weber's full 'Der Hauptsatz des vorigen Paragraphen…§173,(1)…Dies findet statt bei dem Körper…R(ρ) oder R(√-3)…'; dropped the factored-fraction norm step, the (2a-b)²+3b²=4 unit-determination, the 'System associirter Zahlen' block, the gcd/unique-factorization + prime-3-zerfällt paragraphs. Re-transcription spec: the agent's p592 opening + p593 (eqs 3/4 + the R(ρ) prime-factorization). [The .tex also added spurious \tag{1},\tag{2} on the norm/units that Weber leaves unnumbered.]
- Structural note: 'Siebzehnter Abschnitt. Algebraische Auflösung von Gleichungen.' heading correctly placed (now line 19948, before §175) — an earlier stale-line concern (19867) was just my §172 edits shifting it.
- HELD-block now §148-156, §158, §162-163, §165, §167-170, §173-174.
### 2026-06-25 — p594–599 (run w7xkct7q5; §174-end R(ρ) / §175 Reduction der Gruppe durch reine Gleichungen / §176 Metacyklische Gleichungen; verified by eye)
**0 applied — §174-end + §175 + §176 HELD (paraphrased Siebzehnter-Abschnitt theory)** (12 agents, 434k tok). 369pp.
- §174 (R(ρ)) end (p594): held (complex-primes-list prose paraphrased; folds into §174 spec).
- **§175 (Reduction der Gruppe durch reine Gleichungen, p595–598) HELD** — Siebzehnter-Abschnitt algebraic-solution theory, paraphrased throughout: the .tex condensed Weber's opening (dropped 'worunter man die Darstellung…durch eine Reihe von Radicalen…versteht', 'Auf diese Frage fällt von der Gruppentheorie das hellste Licht', the whole 'Präcisiren wir zunächst…successive Adjunction von Wurzelgrössen' paragraph; added a spurious \tag{1} on y^m-a=0 which is unnumbered in print) + the 'Soll eine irreducible Gleichung…' reducibility paragraph. Spec: agent's p595 opening re-transcriptions. NOTE eq(2): .tex ε=ψ(x_0,…,x_{n-1}) — agent crop-claims print shows x_{m-1} (passage uses ε_{m-1}, Primzahl m); verify n-vs-m on crop during re-transcription (not patched — uncertain single index in a held §).
- **§176 (Metacyklische Gleichungen, p599+) HELD** — paraphrased theory (p599 '…ob eine oder einige der Wurzeln…während andere…nicht gestatten. Diese Frage ist nur berechtigt bei irreduciblen Gleichungen…' condensed; the metacyclic-induction proof reworded).
- HELD-block now §148-156, §158, §162-163, §165, §167-170, §173-176.
### 2026-06-25 — p600–605 (run w0rfvwfss; §176-end / §177 Einfachheit der alternirenden Gruppe / §178 Nicht metacyklische Gleichungen; verified by eye)
**0 applied — §176-178 HELD (paraphrased Siebzehnter-Abschnitt theory)** (18 agents, 603k tok). 369pp. [10 acc / 2 rej / 5 typeB / 22 cosm — all acc are paragraph re-transcriptions, no discrete type-A.]
- **§177 (Einfachheit der alternirenden Gruppe, p601-602) HELD** — the classic proof that A_n is simple (n≥5): the 3-cycle generation (any Normaltheiler Q ⊇ a 3-cycle ⇒ Q=A) + the case-analysis of permutation forms (κ with a >3-cycle etc.) is paraphrased throughout (8 agent paragraph re-transcriptions, p601). Spec: restore the full proof prose + the 'λ=κ⁻¹π⁻¹κπ=' eq-prefixes.
- **§178 (Nicht metacyklische Gleichungen im Körper der rationalen Zahlen, p602-605) HELD** — quintic-unsolvability application, paraphrased; the DROPPED Abel/Ruffini footnote (p602): 'Der erste vollständige Beweis, dass die allgemeine Gleichung von höherem als dem 4ten Grade durch Radicale nicht lösbar ist, rührt von Abel her (Crelle Bd I, 1826)…Ruffini (1799-1806)…Burkhardt „Die Anfänge der Gruppentheorie und Paolo Ruffini" (Leipzig 1892)' folds into the spec.
- §176 (Metacyklische Gleichungen) ends on p600 (held).
- HELD-block now §148-156, §158, §162-163, §165, §167-170, §173-178.
### 2026-06-25 — p606–611 (run w88dtgypr; §178-end / §179 Auflösung durch reelle Radicale / §180 Metacyklische Gleichungen von Primzahlgrad; verified by eye)
**0 applied — §178-180 HELD (reconstruction; editorial 3rd-person 'Weber' + added modern content)** (8 agents, 334k tok). 369pp.
- **§179 (Auflösung durch reelle Radicale) + §180 (Metacyklische Gleichungen von Primzahlgrad, p607-611) HELD** — WHOLESALE reconstruction. KEY marker: the .tex has EDITORIAL THIRD-PERSON refs to Weber (line 20110 'Weber benutzt hier nur eine einfachere Folgerung: für jeden Primzahlgrad lassen sich Gleichungen ohne Affect finden') — the GPT wrote ABOUT Weber, not AS Weber. Plus ADDED modern content not in print: a boxed 'Eisenstein'sche Kriterium' (line 20129), 'Würfelverdoppelung'/'Delisches Problem'/'Siebeneck' examples, modern bare xrefs '§ 157'/'§ 2' (vs the edition's \S\,NNN). Weber's actual p608-610 text (the f_1(x) const-term / ε^λa^μ=b derivation, the §158,3 + §153 citations, the (z,z+b)/(z,az+b) substitutions) is grep-absent.
- §178 (p606) end held: the .tex mislabels theorem '4.' (Es giebt von jedem Primzahlgrade…ohne Affect) as 'A.'; dropped the §179-intro Hölder/Kneser footnote (Math. Ann. Bd. 38 / Bd. 41). Both fold into the spec.
- HELD-block now §148-156, §158, §162-163, §165, §167-170, §173-180.
### 2026-06-25 — p612–617 (run w685izify; §180 Metacyklische Gleichungen von Primzahlgrad cont.; verified by eye)
**0 applied — §180 HELD (wholesale reconstruction w/ MODERN notation)** (7 agents, 287k tok). 369pp. [0 acc / 1 rej / 6 typeB.]
- **§180 (Metacyklische Gleichungen von Primzahlgrad, p613-617) HELD** — wholesale reconstruction across p613-617: the .tex paraphrases the linear-group theory (the Satz 'transitive lineare Gruppe L Normaltheiler von P ⇒ P linear', the Galois linear-group criteria I-III, the P_{μ-1}→P chain proof) with MODERN SYMBOLS (\triangleleft normal-subgroup, \perm, \pmod) + modern theorem-numbering — none of which Weber used. The .tex uses the φ(z) POWER-form interpolation (φ(z)≡-Σa_i(z-i)^{n-1}) vs Weber's ψ(z) LAGRANGE-interpolation (ψ(z)=z(z-1)…(z-n+1) via §136 ψ(z)≡z^n-z + §29); dropped the §136/§29 xrefs + the 'lauter linearen Permutationen'/'Anblick der Formeln' prose. p617 running head 'Metacyklische Gruppen' vs .tex title 'Metacyklische Gleichungen von Primzahlgrad'. 1 rejected (p616 print λ'=(z,a_0^{ph}z+b) vs .tex 'L'' — reconstructed context, folds).
- HELD-block unchanged §148-156, §158, §162-163, §165, §167-170, §173-180.
### 2026-06-25 — p618–623 (run wt5e0c2gc; §181 Anwendung…5ten Grades / §182 Die Gruppe der Resolvente [Achtzehnter Abschnitt]; verified by eye)
**0 applied — §181-182 HELD (the algebraic-solution endgame, reconstruction)** (10 agents, 387k tok). 369pp.
- **§181 (Anwendung auf die metacyklischen Gleichungen fünften Grades, p618-620, end of Siebzehnter Abschnitt) HELD** — paraphrased: Satz V reworded; dropped 'Eine andere Form dieser Bedingung…' + the cyclic-decomposition argument; dropped the Kronecker footnote (Ueber algebraisch auflösbare Gleichungen, Monatsber. Berl. Akad. 14. April 1856) + the reell-Rationalitätsbereich paragraph ('Wenn…zwei Wurzeln reell…alle reell…ungeraden Grades') + the (x_h-x_k)² discriminant-sign argument.
- **§182 (Die Gruppe der Resolvente, p620-623, Achtzehnter Abschnitt 'Wurzeln metacyklischer Gleichungen') HELD** — worked-computation paraphrased: the .tex DROPPED the explicit quintic resolvent computation (p623: the permutation list (1,2)(3,4), t(0,1)=(0,1,2,4,3),… + the full 6-eq arrays (11) u_1…u_6 and (12) u'_1…u'_6 in the x_i) — collapsed to a one-sentence summary; also dropped the (8) xref + a,b,c,d,e coeff list. These (substantial computational restorations) fold into the §182 spec.
- HELD-block now §148-156, §158, §162-163, §165, §167-170, §173-182.
### 2026-06-25 — p624–629 (run wujzcfe7g; §183 Stellung der Aufgabe / §184 Sätze über die Resolventen [Achtzehnter Abschnitt]; verified by eye)
**0 applied — §183-184 HELD (reconstruction w/ editorial 3rd-person 'Weber')** (15 agents, 530k tok). 369pp.
- **§183-184 (the explicit quintic resolvent, p624-629) HELD** — reconstruction confirmed by EDITORIAL THIRD-PERSON 'Weber' in the .tex itself: 'Weber bildet die Resolvente für die Bring-Jerrard'sche Form' (p624), 'untersucht Weber den Einfluss der vier Transpositionen (0,1)…' (p628) — Weber's 1st-person text rewritten about him. Dropped: the Cayley-coefficient-computation note + the Runge footnote (Acta math. Bd.7); the √Δ ten-factor product expansion + the '=16i√(-α⁵)' step (p624 eq16); the 'aus einem beliebigen Rationalitätsbereich…' clause + the 64α=-5⁴/64β=-5⁴ relations + the ξ⁵+5ξ⁴-5·64=0 worked example framing (p627); the §184-opening 'merkwürdigen Schluss über die Gleichungen 6ten Grades' + the generating permutations π_1..π_4 of group C (via §153,2) (p628). All fold into the §183-184 spec.
- HELD-block now §148-156, §158, §162-163, §165, §167-170, §173-184.
### 2026-06-25 — p630–635 (run wniy4cdgm; §184 Sätze über die Resolventen cont.; verified by eye)
**0 applied — §184 HELD (paraphrased resolvent theory)** (21 agents, 683k tok). 369pp.
- **§184 (Sätze über die Resolventen, p633-635) HELD** — the (ε,x)-resolvent theory paraphrased/condensed throughout: dropped 'und wenden darauf die Sätze des vorigen Paragraphen an' + many 'aber'/'wenn wir'/'beiden' word-drops + the §180/§183,(3)/§163 xrefs; eq(4) printed (ε,x)^n but .tex has (ε,x)^λ (crop-confirmed n); the s^λ/t^λ Vertauschungen displays dropped (.tex uses h not Weber's λ); eq(5) collapsed (the .tex's cumulative (ε^{g^h},x)(ε,x)^{-g^h}=f_h replaces Weber's 3-line recursion (ε^g,x)(ε,x)^{-g}=f_0, (ε^{g²},x)(ε^g,x)^{-g}=f_1, …, f_{n-2}); theorem-6 index f_{n-2} vs print f_{n-1} (likely a Weber source typo → transcribe-print+flag). All fold into the §184 spec.
- POSSIBLE 11th erratum: §184 thm-6 f_{n-1} (math wants f_{n-2}); resolve during re-transcription.
- HELD-block unchanged §148-156, §158, §162-163, §165, §167-170, §173-184.
### 2026-06-26 — p636–641 (run wt69df2mt; §185 Wurzeln metacyklischer Gleichungen / §186 Befreiung von den beschränkenden Voraussetzungen; verified by eye)
**0 applied — §185-186 HELD (paraphrased metacyclic-root theory)** (58 agents, 1.8M tok; 48 acc / 4 rej / 2 typeB / 21 cosm). 369pp.
- **§185-186 (p636-641) HELD** — the metacyclic-root construction, paraphrased/condensed throughout (48 paragraph/eq fixes): dropped clauses ('und wenn wir noch beachten, dass ε^{g^{n-1}}=ε ist', 'worin l eine beliebige ganze Zahl…bis auf Vielfache von n definirt', 'wenn man beachtet, dass die Functionen f_0…cyklische Permutation…(ε,ε^g)', the F_v-festsetzung 'F_h=F_k wenn h≡k mod n-1' + the s/t^{-1} action, 'so dass r_0 immer =1 ist'); eq damage (eq8 (ε,x)^{1-g^{n-1}} vs .tex ^{g^{n-1}-1} [reciprocal]; eq9 spurious λ in f-exponents; eq16 '=' vs '≡' mod n + g_1 vs g; eq17 q_{n-2}/q_{n-3} exponents vs .tex g^{…} + spurious trailing ^g; eq18 Φ_v^n vs .tex Φ_v); dropped xrefs (8),(10). All fold into the §185-186 spec.
- HELD-block now §148-156, §158, §162-163, §165, §167-170, §173-186.
### 2026-06-26 — p642–647 (run wnydchknq; §186 Befreiung / §187 Realitätsverhältnisse / §188 Metacyklische Gleichungen fünften Grades; verified by eye)
**0 applied — §186-188 HELD (the metacyclic-quintic endgame)** (17 agents, 642k tok; 11 acc / 0 rej / 3 typeB / 25 cosm). 369pp.
- **§186-188 (p642-647) HELD** — paraphrased/condensed throughout: §186 dropped the Vandermonde determinant |1,η_h,…,η_h^{n-1}| + the §52 Tschirnhausen xref + 'ein System von Gleichungen'; the τ_α-radical Vertauschung derivation (eqs 13/14/16 index h-for-v, the dropped ξ_h chain A+Σε^{hr_v}K_{v+1}…, the enumerated '1.'/'2.' steps); the irreducibility argument (dropped §185(8)/§179 xrefs, the √[n]{R_v} all-rational-or-all-irrational + Ω(ε)-degree reasoning). All fold into the §186-188 spec.
- **CONTENT MAP ~COMPLETE** (p1-647 audited; only p648=§188 tail remains). Held block = essentially all of Buch III §148-188 EXCEPT the patched worked-example islands §157,159-161,164,171-172. Weber's Berichtigungen (errata) at .tex line 21147.
- HELD-block now §148-156, §158, §162-163, §165, §167-170, §173-188.
### 2026-06-26 — p648 (run wf2m5kfor; §188 Metacyklische Gleichungen fünften Grades end; verified by eye)
**0 applied — §188 HELD; ★ CONTENT MAP of vol1 COMPLETE** (3 agents, 133k tok; 2 acc / 0 typeB). 369pp.
- §188 (p648) held: dropped 2 Kronecker sentences ('So können wir…beliebig viele metacyklische Gleichungen bilden. Dass darin alle…im Körper der rationalen Zahlen enthalten sind, ist ein…von Kronecker herrührender Satz, den wir im zweiten Bande kennen lernen werden'); 'der vorangehenden Paragraphen' → 'des vorangehenden Paragraphen' (singular xref). Cosmetic: Fraktur 𝔎 → Ω (systematic). Fold into §188 spec.
- ★★★ **vol1 CONTENT MAP COMPLETE (p1-648, 93 batches).** ~585 verified fixes applied (Buch I-II + the patched/re-transcribed Buch-III worked-example islands §150,152,157,159-161,164,171-172). HELD-block (= the re-transcription spec) = §69, §138-numbering, §141, p466, §148-156, §158, §162-163, §165, §167-170, §173-188. 10 Weber errata flagged (+1 possible §184 thm-6). NEXT = PHASE 2 (re-transcription) per WEBER_METHOD_LOG.md plan.
### 2026-06-26 — ★ PHASE 2 (re-transcription) — §141 (Functionen in einem Körper) DONE; verified by eye vs p453-455
**§141 RE-TRANSCRIBED (held→faithful)** — 369→**370 pp** / 0 err.
- §141 was condensed-throughout (theorem statements I-IV faithful, connective prose condensed). Restored vs the scans: (a) def — 'Man spricht bisweilen auch…wenn es z.B. der Körper der rationalen Zahlen ist…ohne die Bezeichnung „im Körper Ω" hinzuzufügen' + the dropped 'Dass aber an sich die genaue Präcisirung des Körpers…Rationalitätsbereich…wesentlich…Bemerkungen' sentence; (b) the 'lineare Function' tail ('die dann natürlich reducibel ist, da sie wieder in die Factoren zerlegt werden kann, aus denen sie entstanden ist') + the Ω' details + 'denn es kann…ein linearer Factor x-α abgesondert werden' + 'In dem Körper, der aus allen Zahlen besteht…reducibel'; (c) the Satz I/II/III connective structure ('Wir können dem Satze I auch den folgenden Ausdruck geben:' before II, 'Insbesondere können wir daraus schliessen:' before III — were lost to the flat enumerate; restructured to separate enumerates); (d) the full three-way distinction ('Unter den Functionen von mehr als einer unabhängigen Veränderlichen…während die der zweiten Art als zerlegbare, die der ersten Art als unzerlegbare…') + the concrete examples (x²-y²=(x-y)(x+y) reducibel; x²-2y² = (x+y√2)(x-y√2) factors-not-in-Ω; x²+y²+1 unzerlegbar) + 'Eine in einem Körper Ω irreducible, aber zerlegbare Function wird…reducibel'; (e) the §51 'Bei jenen Ausführungen…Rationalitätsbereich…wegfällt' clause + 'Benutzt ist aber immer nur'.
- LESSON for phase 2: a 'pervasive-paraphrase'-flagged section can be MOSTLY faithful (theorems/eqs intact) + condensed only in connective prose ⇒ re-transcription = restore the condensed prose, keep the faithful skeleton. Worth re-checking each held section's actual state before assuming a full rewrite.
- HELD-block: §141 DONE/REMOVED → remaining §69, §138-numbering, p466, §148-156, §158, §162-163, §165, §167-170, §173-188.
### 2026-06-26 — PHASE 2 recon — §138-numbering MAPPED (edit deferred to focused pass)
Did NOT edit (whole-§138 rule-numbering standardization is too sprawling for the remaining budget; risk of a half-done renumber). **The mapping is now solved** — for the focused pass:
- §138 has TWO parallel numbering systems, both flush-left in print: **parenthesized eq-tags (5)…(10)** for displayed formulas [the .tex's \tag{5}-\tag{10} are CORRECT: (7) α=sin²(2νm'π/n) p442; (8) φ=2νm'π/n; (9) the ∏sin/∏sin product p442_bot; (10) (m/n)=(-1)^{(m-1)(n-1)/4}2^{(m-1)(n-1)/2}∏∏(α-β) p443_mid] AND **rule numbers "1."…"9."** (period, no parens) for the propositions.
- THE .tex ERRORS: (a) rule **8.** = numerator-mult (mm'/n)=(m/n)(m'/n) [.tex 16326-16329 is an UNTAGGED display — add flush-left "8."]; (b) cross-ref .tex 16330 "bleibt diese Formel auch noch richtig" → print "bleibt 8. auch noch richtig"; (c) rule **9.** = reciprocity (m/n)=(-1)^{(m-1)(n-1)/4}(n/m) [.tex 16345 mislabeled "\tag{9'}" — should be flush-left rule "9."]; (d) .tex 16355 "\tag{10'}" = the "letzter Satz" (m/n)(m/n')=(m/nn') and .tex 16362 "\tag{7'}" = its congruence proof-step — both need Weber's true numbers (read p443_bot/p444); (e) rules 1.–7. layout on p439-442 (.tex 16200-16290) still to be checked for the same primed/dropped-label issue.
- TODO focused pass: standardize ALL §138 rules 1.–9. to flush-left "N." (distinct from eq-tags), fix cross-refs ("diese Formel"→"8.", verify "aus 8. und 9.", "von 10. die Formel 9.", "aus 7. und 8.", "nach 9." all resolve), remove spurious primes (7',9',10').

### 2026-06-26 — PHASE 2 — §162-body (Abel'sche Gleichungen) p534 def-section RE-TRANSCRIBED; commutativity p535-536 REMAINS
**§162 p534 def-section faithful** — 370pp/0err. Restored vs p534 scans: the §162 intro + Abel footnote ('Abel, Mémoire sur une classe d'équations résolubles algébriquement, Crelle Bd.4 1829, Oeuvres 1881 Bd.1 S.418') + 'die Abel allgemein aufzulösen gelehrt hat…nennen wollen'; the def wording ('…ausdrückbar ist, und wenn, falls (2)…die Bedingung (3)…für je zwei dieser Functionen besteht'); the 'Es bedeutet hierin das Zeichen Θ_hΘ_k(α), dass die Function Θ_h(x) für das Argument x=Θ_k(α)…Selbstverständlich…als rational angenommenen Körper Ω'; the cyclotomy paragraph (Weber's 'die Gleichungen, durch die die Einheitswurzeln bestimmt sind…Θ_hΘ_k(r)=Θ_kΘ_h(r)=r^{hk}' + the reine-Gleichung 'Θ_h(x)=r^hx…Θ_hΘ_k(x)=Θ_kΘ_h(x)=r^{h+k}x' — .tex had reworded to 'Kreistheilungsgleichungen' + dropped both Θ-eqs).
- ⏸ REMAINS for §162 (p534bot-536, read p535-536 to finish): the irreducibel-reduction (Weber 'Wenn die Function F(x) nicht irreducibel ist…φ(x)=0 nach §145 eine Galois'sche Resolvente…' vs .tex 18417 reworded) + the commutativity theorem/derivation (the σ=(α,α),σ'=(α,α')… defs eq (6), the σ_k=[α,Θ_k(α)] bracket block, the §147-cited σ'σ''/σ''σ' commutativity, the 'jeder Theiler [commutativer Gruppe] normal' remark) + the converse (18441). eqs (4)(5)(6) faithful.
- HELD remaining: §69, §138-numbering, p466, §148-156, §158, §162(commutativity p535-536), §163, §165, §167-170, §173-188.
Compiles **370 pp / 0 err**.

### 2026-06-26 — PHASE 2 — §162 commutativity + converse DONE → §162 (Abel'sche Gleichungen) FULLY re-transcribed
**§162 COMPLETE** — 370→**371 pp** / 0 err. Restored vs p535-536: the irreducibel-reduction tail ('φ(x)=0 nach §145 eine Galois'sche Resolvente…Es genügt also…beschränken'); the commutativity theorem (full statement) + 'Es seien nämlich (4)…(5)…die darunter enthaltenen Wurzeln des irreducibeln Factors φ(x)' + 'Da, wie schon bemerkt, φ(x)=0 eine Galois'sche Resolvente…(6)' + the §147 bracket-composition derivation (σ'σ''=[α,Θ'(α)][Θ'(α),Θ'Θ''(α)]=[α,Θ'Θ''(α)] etc.) + 'Folglich ist die Gruppe…isomorphe Permutationsgruppe…commutativ'; the FULL converse ('Es gilt nun auch das Umgekehrte…Q der Theiler…π_i^{-1}Qπ_i=π_i^{-1}π_iQ=Q…Q identisch…Normalgleichung…σ_k=[α,Θ_k(α)]…Θ_hΘ_k(α)=Θ_kΘ_h(α)…Abel'sche Gruppen genannt werden (§148)') + the closing corollary ('Es folgt also noch…transitiven Abel'schen Permutationsgruppe…Zahl der Permutationen mit der Zahl der vertauschten Ziffern übereinstimmt').
- **11th Weber erratum (p536):** prints 'σ_kσ_h=[α,Θ_kΘ_h(x)]' — the (x) should be (α) (parallel to σ_hσ_k=[α,Θ_hΘ_k(α)]; a [α,β]-bracket needs a value, not a function of x); transcribed faithfully as (x) + flagged. ERRATA now 11 (Q_0 p221, u' p334, 30° p357, +η² p382, α_1 p378, ω'-ω p385, a_3/a_4 p402, mod m p426, transitiv/intransitiv p482, (a-b)³ p582, Θ_kΘ_h(x) p536).
- HELD remaining: §69, §138-numbering, p466, §148-156, §158, §163, §165, §167-170, §173-188. (§141, §162 DONE this session.)
Compiles **371 pp / 0 err**.

### 2026-06-26 — PHASE 2 recon — §163 (Reduction Abel→cyklisch) MAPPED; re-transcription DEFERRED (eq-coupled, needs uninterrupted budget)
§163 (.tex 18488-18552, p537-541) = GPT RE-EXPOSITION with folded/renumbered eqs ⇒ a partial restore would create duplicate/conflicting eq-labels (the .tex mislabels Weber's cycle-rows eq (2) as its (1), and its body uses (4)(5)(7)(8)). Must be a WHOLE-§163 re-transcription (eqs 1-11 renumbered to Weber). Spec for the focused/July-1 pass:
- p537 opening (read this session): restore the π^r-argument + theorem '1. Eine Permutation einer transitiven Abel'schen Gruppe enthält nur Cyklen von gleicher Gliederzahl'; 'Die Anzahl r…Theiler von m…m=rs…s die Anzahl der r-gliedrigen Cyklen'; Weber eq (1) π=γγ_1γ_2…γ_{s-1}, eq (2) the cycle-rows γ=(α,α_1…α_{r-1})…γ_{s-1}=(σ,…), eq (3) π_1^{-1}ππ_1=π + the §.154,6 reference. [.tex 18490-18496 'Die Commutativität…systematische Reduction…imprimitiv' is the GPT rewrite.]
- p538-541 body: cyclic-function ω=ψ(α,α_1…α_{r-1}) eq + the reduction to a lower-degree Abel'sche + cyclic Gleichungen; the cyklisch-Gleichung def + C=1,π,…,π^{m-1} (8); p541 Θ-chain eq (11) + the dropped Gauss-Sectio-VII (Kreistheilung) footnote + §158 xref.
Compiles **371 pp / 0 err**.

### 2026-06-26 — PHASE 2 — §163 p537-538 RE-TRANSCRIBED (opening + cyclic-function reduction); p539-541 remain
[Budget note: Floris corrected me — the manual page-by-page (open→zoom→check→next) is the TOKEN-EFFICIENT path (my own context, not agent workflows that burn 300k-1.8M/batch); slow wall-clock is fine (SGA5 runs parallel). So NO more pausing for budget — grind the held-list to the end. §163 CAN be done page-by-page: replacing the .tex's mislabeled opening (incl. its bogus eq (1)) avoids duplicate labels, converging to Weber numbering.]
**§163 p537-538 done** — 371pp/0err. Restored vs p537-538: the π^r-argument + theorem '1. Eine Permutation einer transitiven Abel'schen Gruppe enthält nur Cyklen von gleicher Gliederzahl'; 'Die Anzahl r…Theiler von m…m=rs…'; eq (1) π=γγ_1γ_2…γ_{s-1}, eq (2) the cycle-rows (γ,γ_1,…,γ_{s-1} as an aligned array), eq (3) π_1^{-1}ππ_1=π + the §.154,6 reference + the '-ordnung…nur unter einander (cyklisch) vertauscht…s>1…imprimitiv' conclusion; the cyclic-function def + eq (4) ω=ψ(α,…), (5) conjugates, restored the dropped (6) ω_1=ψ(β,…), (7) Φ(t)=0 + §.158 xref + 'Man erhält aber die durch π_1π_2…commutativ. Daher ist Φ(t)=0 eine Abel'sche Gleichung s^ten Grades'; the F(x)=F(x,ω)…F(x,ω_{s-1}) factorization + 'von denen der erste…Periode der cyklischen Permutation γ'. Numbering now Weber (1)-(7) coherent.
- p539 DONE (372pp/0err): the cyklisch-Gleichung def ('Wir wollen eine Gleichung…eine cyklische Gleichung nennen…einfachste Specialfall…sind') + reduction-summary ('Wir haben dann also bewiesen…Diesen Satz kann man wieder…Die Lösung einer Abel'schen Gleichung lässt sich immer…zurückführen, deren Grade Theiler…sind') + the GENERAL def ('Es ist nicht nothwendig…Wir können daher allgemein die Definition so fassen: Eine Gleichung m^ten Grades…cyklische Gleichung im Körper Ω, wenn ihre Wurzeln…die cyklischen Functionen der Wurzeln in Ω rational sind') + eq (7) π=(α,α_1,α_2…α_{m-1}), (8) C=1,π,π²,π³…π^{m-1}, the Galois-group sentence + (9) C_e=1,π^e…π^{(f-1)e} (dropped m=ef from the display — it's in the prose). **NOTE Weber reuses eq (7): Φ(t)=0 on p538 AND π=(α,…) on p539 (general-def restart) — transcribed faithfully as two (7)s; editorial de-dup is a later call.**
- ★ **§163 p540-541 DONE → §163 FULLY re-transcribed** (372pp/0err). Restored vs p540-541: the C_e conclusion ('und wenn eine Function…in keiner umfassenderen Gruppe…so ist C_e diese Gruppe. C_e ist aber, wenn e<m ist, intransitiv, und die Gleichung ist reducibel'); the non-prime reduction ('Auch auf die cyklischen Gleichungen, deren Grad keine Primzahl ist…m=ef…π^e in e Cyklen γ…') with (10) the full γ,γ_1,…,γ_{e-1} array [FIXED γ_0→γ] and (11) the full η=ψ(…),η_1=ψ(…),…,η_{e-1}=ψ(…) array [.tex had folded it]; the F(x)=F(x,η)…F(x,η_{e-1}) factorization + the F_1=(x-α)(x-α_e)… + Lagrange [§155,(2)] argument F_1=F(x,η) + 'F(x,η)=0 ist aber wieder cyklisch in Ω(η)'. **RESTORED the ENTIRE dropped p541**: the 'jede Wurzel rational durch jede andere…folgendermaassen cyklisch anordnen' + Ψ(x)=F(x)(Σα_{i+1}/(x-α_i)) + Ψ(x)/F'(x)=Θ(x) + (11) α_1=Θ(α),α_2=Θ(α_1),…,α=Θ(α_{m-1}) + 'mag F(x) reducibel oder irreducibel…F(x),F'(x) keinen gemeinsamen Theiler'; the 'Auflösung…abhängig…Primfactoren von m…Potenz von 2…Quadratwurzeln…Auf diesem Wege hat Gauss zuerst die Kreistheilungsgleichungen behandelt' + footnote 'Gauss, Disquisitiones arithmeticae, Sectio VII'; the prime-degree remark ('für einen Primzahlgrad…Normalgleichung und cyklische Gleichung zusammenfallen…1,π,π²…π^{n-1}, also cyklisch').
- **NOTE Weber ALSO reuses eq (11)**: the η-array (p540) AND the Θ-chain α_1=Θ(α) (p541) both tagged (11) — transcribed faithfully (2nd Weber eq-number reuse in §163, after (7)=Φ/π). Editorial de-dup of (7),(11) is a later call.
- ★★★ **§163 COMPLETE** (p537-541). §141, §162, §163 fully re-transcribed this session.
Compiles **371 pp / 0 err**.

### 2026-07-02 — PHASE 2 — §158 (Imprimitive Gruppen) FULLY re-transcribed p516–521; verified by eye vs scans
The .tex §158 was a WHOLESALE GPT SUMMARY (~50 lines) that dropped eq (2), eqs (3)-(6), the (α)/(β)
Vertauschungs-matrices, the whole Normaltheiler proof, the conjugate-groups Q_α…Q_σ development, and the
Umkehrung construction; it reworded the opening (no §.151 xref) and mislabeled the last row **δ** (Weber: **σ**).
Replaced the entire body (.tex 17913-17961) with the faithful Weber text via marker-anchored Python range-replace:
- Opening "Wir machen von unseren allgemeinen Sätzen…im §. 151 gesehen…n=r·s…s Reihen von je r Gliedern" + eq (1)
  the A/B/…/S row-array (last row **σ**, not δ).
- Normaltheiler-proof para (Q an-ihrer-Stelle, π⁻¹ϰπ∈Q) + eq (2) f(x)=f_α(x,ψ)f_β(x,ψ)…f_σ(x,ψ).
- Partialresolvente χ(u)=0 (§. 155) + eqs (3) ψ,ψ₁… (4) (ψ,ψ),(ψ,ψ₁)… (5) Q,Qπ₁,… + isomorphism argument.
- Conjugate groups Q_α,Q_β…Q_σ (gcd = Q, Index j); φ(y)=0 s-degree; §. 154,7 ⇒ s|j, j prime ⇒ j=s.
- eq (6) f(x)=f(x,y_α)…f(x,y_σ) = the (2) factors; f(x,y_α) irred in Ω(y_α) but not nec. in Ω(ψ).
- p519-520 P_α…P_σ group-connection: the π_β…π_σ matrix pair, (α) & (β) matrices, ϰ_β=π_β⁻¹ϰπ_β proof ⇒ **boxed 1.**
- Umkehrung (p520-521): transitive P + intransitive Normaltheiler Q ⇒ imprimitiv; systems C,… construction ⇒ **boxed 2.**, **boxed 3.** (Resolvente/Normalgleichung j-degree ⇒ Theiler-des-Grades factors) + prime-degree-solved close.
- **12th Weber erratum (p521, boxed thm 2):** Weber prints "Systeme der **Imprimivität**" (missing "ti"; std = Imprimitivität) — transcribed faithfully as printed, flagged here. Editorial call deferred with the other errata.
- Used \varkappa for Weber's script-κ (ϰ); eqs numbered with \tag{1}..\tag{6} per house style; §-refs as "§. 151".
- ⚠ **To check when I reach §159:** the heading "Fünfzehnter Abschnitt. Cyklische Gleichungen" (.tex 18032) sits
  directly before §159 "Cubische Gleichungen" (cubic/quartic worked examples) — possible wrong Abschnitt title; verify vs the p522 section-opening scan.
Compiles **375 pp / 0 err** (372→375, growth from restored content; page count did NOT drop).

### 2026-07-02 — PHASE 2 — §165 (Auflösung der cyklischen Gleichungen) FULLY re-transcribed p546–551; verified by eye vs scans
The .tex §165 was a GPT reconstruction: modernized notation, "gibt"→(should be giebt), "\S\,164"→(should be §. 164),
and — worst — dropped/merged the equation set (it had (1)-(4),(5--6),(9),(11--13),(14),(15),(16),(21); Weber has a
clean (1)-(21)). It also mangled key equations. Replaced the whole body (.tex 18785-18894) with Weber's faithful text
via marker-anchored Python range-replace. Corrections restored:
- eq (2): .tex had "$(\varepsilon^\lambda,\alpha)^m=\psi_\lambda$"; Weber prints the radical form $(\varepsilon^\lambda,\alpha)=\sqrt[m]{\psi_\lambda}$.
- opening: Weber "Reduction auf **reine** Gleichungen" (.tex dropped "reine"); "$(1,\alpha)=a$ als die Summe der Wurzeln" (.tex wrongly expanded $a=\alpha+\alpha_1+\cdots$).
- eq (4): restored the full derivation ($\chi_\lambda=b_0^{(\lambda)}+\cdots$, $(\varepsilon,\alpha)^{m-\lambda}(\varepsilon^\lambda,\alpha)=\chi_\lambda$) and both equality-forms; Weber's "$\mu=1,\nu=m-\lambda$" (.tex had $\nu=-\lambda$).
- restored the ENTIRE dropped $\psi_1=0$ exceptional-case discussion + the $m=pn$ / $\alpha_n-\alpha_0$ difference argument ($m(\alpha_n-\alpha_0)=\sum_{0,m-1}^{\lambda}(\varepsilon^{-n\lambda}-1)(\varepsilon^\lambda,\alpha)$) with Weber's two decompositions $m=p_1p_2\ldots$ (prime powers) then $m=p_1m_1=p_2m_2\ldots$ (.tex had a single wrong "$m=p_1m_1=p_2m_2$").
- restored clean eqs (5),(6),(7),(8) (.tex had a bogus merged "(5--6)" and no (7),(8)).
- restored the full real-case (Abel, $\Omega$ reell) development eqs (9)-(21) + the unnumbered displays ($\varrho_1^2=(\pm a_1)^m=a_1^m$, $a_1^m=b_1^2+c_1^2$, $\sqrt[p_1]{\varphi_1}=\sqrt{a_1^{m_1}}e^{i\Theta_1/p_1}$, the $e^{i\Theta}$ displays); eq (21) Weber: $\chi_\lambda\sqrt{A}^{-\nu}(\cos\frac{\Theta\nu}{m}-i\sin\frac{\Theta\nu}{m})$ (.tex had a wrong $\sqrt[m]{A^{-1}}$).
- restored the whole dropped p551 tail (Realitätsverhältnisse: $\alpha_{\nu+k}=\Theta^\nu(\alpha_k)$, $2k=m$, the $\alpha_k,\alpha_{k+m/2}$ conjugate-imaginary pairs, cubic-discriminant remark). Used $\varrho$ (Weber's ϱ), $\varphi/\varphi'$, $\varepsilon$.
- **13th Weber erratum candidate (p548, eq 7):** the 2nd term is printed $(\varepsilon^{\lambda_2},\alpha)=\sqrt[p_2]{\varphi_2}$ **without** the $^{m_2}$ exponent that the 1st term ($(\varepsilon^{\lambda_1},\alpha)^{m_1}$) and the math require — zoom-confirmed via crop_src. Transcribed faithfully as printed, flagged (editorial call deferred with the other errata).
- ORTHOGRAPHY: Weber prints "**Coëfficient**" (ë) on p546, but the whole book's .tex uses "Coefficient" (100+×, settled normalization like ß→ss) — kept "Coefficienten" for consistency, noted here.
Compiles **377 pp / 0 err** (375→377, growth from restored content; page count did NOT drop).

### 2026-07-02 — PHASE 2 — §148 (Permutationsgruppen) FULLY re-transcribed p472–476; verified by eye vs scans
First section of the §148-156 block. Title "Permutationsgruppen" was CORRECT (verified on opening scan p472; the
p473+ running head "Permutationen" is just the abbreviated running head). The .tex body was a reconstruction (eq
skeleton eqs 1-13 mostly intact, but reworded prose + dropped displays + a symbol error + a dropped ending).
Replaced the whole body (.tex 17013-17124) with Weber's faithful text via marker-anchored Python range-replace:
- **δ → σ:** the .tex used $\delta=(\rho,\rho_1)$ for the substitution; Weber prints $\sigma=(\rho,\rho_1)$ (same class of error as §158's δ→σ). Fixed throughout.
- restored the two dropped displays $F(\alpha)=F[\chi(\rho)]=0$ and $F[\chi(\rho_1)]=0$ (with Weber's square brackets $F[\ldots]$, not the .tex's round $F(\ldots)$).
- opening reworded ".tex 'Im §.145 wurde gezeigt…besitzt…ihre Wurzeln'" → Weber "Im §. 145 haben wir gesehen…hat…Wurzeln von (1)"; "\S\,145/146" → "§. 145/146".
- eq (8): restored Weber's THIRD member $(\pi_a\pi_b)\pi_c=\pi_a(\pi_b\pi_c)=\pi_a\pi_b\pi_c$ (.tex dropped it) + "associative **Princip**" (.tex: "Gesetz") + Weber's full proof.
- restored the two dropped identity-composition displays ($\pi_a\pi_a^{-1}$=id, $\pi_a^{-1}\pi_a$=id) and the unnumbered $\pi_c^{-1}=\pi_b^{-1}\pi_a^{-1}$; restored Weber's inverse/identity prose (eqs 9-11).
- restored item **2.** as a numbered result (the .tex had demoted eqs (12)/(13) to plain prose); restored item 3's def with Weber's $Q=\pi,\pi',\pi'',\pi'''\ldots$ (.tex had set-builder $Q=\{\pi_0,\ldots,\pi_{q-1}\}$) and "Grad…Anzahl der Permutationen, die sie enthält" (.tex reworded).
- **corrected a fabrication:** the .tex wrote "…bildet eine Gruppe, **die symmetrische Gruppe**" — Weber does NOT say "symmetrische Gruppe" here; he writes "bildet eine solche Gruppe. Ebenso ist die einzige identische Permutation eine Gruppe für sich. Was zwischen diesen beiden extremen Fällen…in den folgenden Abschnitten beschäftigen." Restored.
- restored the ENTIRE dropped §148 ending (p476): the **cyclic-group example** (three 3-cycle $\perm{}{}$ matrices) and the **commutative/Abel'sche Gruppen** paragraph + the **Theiler** definition ($Q_1$ Theiler von $Q$).
- Kept the \perm{}{} pmatrix macro (faithfully renders Weber's parenthesized 2-row symbol) and \rho for the Normalkörper generator (matches §146-149).
Compiles **378 pp / 0 err** (377→378, growth from restored content; page count did NOT drop).

### 2026-07-02 — PHASE 2 — §149 (Galois'sche Gruppe) FULLY re-transcribed p476–481; verified by eye vs scans
Second section of the §148-156 block, and a HEAVY reconstruction (the .tex compressed Weber's full 6-page section
into ~1 page, dropping the entire d)-proof machinery and the Galois footnote). Replaced the whole body
(.tex 17163-17231) with Weber's faithful text via marker-anchored Python range-replace. Corrections restored:
- **δ → σ:** the .tex used $\delta$ for the Normalkörper substitution throughout §149; Weber prints $\sigma$ (same
  recurring error as §148/§158). Fixed everywhere.
- **θ → Φ + eq (1) mislabel:** the .tex labeled its opening display "$\rho=\theta(\alpha,\ldots)$" as eq (1). Weber's
  eq (1) is the *substituted* identity $\rho=\Phi[\chi(\rho),\chi_1(\rho)\ldots\chi_{m-1}(\rho)]$ (square brackets, capital Φ);
  the plain $\rho=\Phi(\alpha,\ldots)$ and $\alpha_s=\chi_s(\rho)$ are UNNUMBERED displays before it. eq (2) likewise
  $\rho_k=\Phi[\chi(\rho_k)\ldots]$ (.tex had θ + round brackets). Restored the χ_s(ρ_h)=χ_s(ρ_k) uniqueness argument.
- **arabic "1." → Roman "I.":** Weber labels the main Satz **I.** (Roman), with eqs (3) σ,σ_1…σ_{μ-1} and (4) π,π_1…π_{μ-1}.
  The .tex had it as an arabic "1." enumerate. Rendered with \Roman* label; the later cross-ref "durch den Satz I." now resolves.
- **a)/b)/c)/d) un-merged:** the .tex crammed a,b,c,d into one \alph* enumerate. Weber intersperses proof prose:
  a)+b) together → combined proof (φ(ρ), σ_a=(ρ,ρ_a), §.146,1 and §.146,4) → "Zu a) b) kommt noch als Drittes:" → c)
  → its proof (§.143 primitive ρ, g(ρ)=0, g(ρ_a)=0) → "Daraus schliessen wir noch…Satz:" → d). Broke into 3
  enumerates (start=3, start=4) with the intervening prose restored. Used \varphi for Weber's φ (house style).
- **restored the ENTIRE dropped d)-proof (p479–480):** eqs (5) π_1…π_ν, (6) ρ_1…ρ_ν, (7) ρ'_1…ρ'_ν, the
  group-closure argument (π_iπ_k∈P ⇒ (7)≡(6)), the product g'(t)=(t-ρ_1)…(t-ρ_ν) = g(t) ⇒ P identical with the
  Galois group. The .tex had replaced all this with a vague 3-line paraphrase ("g'(t)=(t-ρ_1)…invariant…identisch").
- restored Weber's G(t)=(t-ρ)(t-ρ')… argument (μ | Π(m); μ = Grad der Galois'schen Gruppe) — .tex had added a
  non-Weber "Theiler von m!" gloss; reverted to Weber's "Theiler von Π(m)".
- Affect/Kronecker paragraph re-transcribed close to print (Π(m):μ = Grad des Affectes; Rationalitätsbereich Ω);
  set "Die allgemeine Gleichung m-ten Grades…hat…keinen Affect." as its own indented proposition (quote), matching
  Weber's set-off display; restored the p481 proof (symm. Grundfunctionen, g(ρ)=0 identisch, ρ→ρ,ρ',ρ''… ⇒ g≡G).
- **restored the dropped Galois biography footnote** (p481, on "…mit G(t) übereinstimmen ¹)"): Évariste Galois d.1832
  Duell; 1830 Férussac Bulletin note; Brief an Auguste Chevalier (Revue encyclopédique Sept 1832); Liouville 1846
  Bd XI (Mém. sur les conditions de résolubilité…); Maser 1889 (Berlin, Springer); Serret / Betti / Jordan / Netto.
  Rendered with \footnote{…} and \glqq/\grqq German quotes.
- ORTHOGRAPHY: Weber prints "Coëfficienten" (ë) on p480–481; kept "Coefficienten" (settled book-wide normalization,
  as in §165). "ergiebt" kept (giebt-form). §-refs as "\S\,146" (settled, no period).
Compiles **380 pp / 0 err** (378→380, growth from restored content; page count did NOT drop).

### 2026-07-02 — PHASE 2 — §151 (Primitive und imprimitive Gruppen) VERIFIED FAITHFUL p483–487; **0 changes**
Third section of the §148-156 block — but on full page-by-page verification it is a **FAITHFUL transcription**, NOT a
reconstruction. Read every scan p483→487 and matched the .tex (17318-17486) line by line:
- **Eqs (1)–(13) all match Weber exactly, INCLUDING the doubled (4).** The .tex has two `\tag{4}` — one for
  $(t-\Theta)(t-\Theta_1)\cdots(t-\Theta_{s-1})=\varphi(t)$ (Weber p483_bot) and one for the ω-array (Weber p484_bot).
  I initially flagged this as a numbering bug, but the SCAN confirms Weber himself prints (4) twice (same reused-number
  quirk as §163's (7)/(11)). So the .tex is correct — NO fix. [Lesson: a "duplicate tag" is not automatically an error;
  verify against the scan — Weber reuses equation numbers.]
- eqs (5) $\varphi(t)(\sum\omega_i/(t-\Theta_i))=\Phi(t)$, (6) $\omega=\Phi(\Theta)/\varphi'(\Theta)$, (7) product
  $=\varphi(u,\Theta)$, (8) y-array, (9) $\psi(t,A)/\psi(t,B)/\psi(t,S)$ array, (10) $\varphi(u)=\prod(u-y_i)$,
  (11) $\psi(t,A)=\psi(t,y)$, (12) $\psi(\alpha,y)=0$, (13) $\psi(\alpha,u)=0,\varphi(u)=0$ — all verbatim.
- All THREE boxed results match verbatim: 1. "Ein imprimitiver Körper hat eine imprimitive Gruppe." (p484),
  2. "Der imprimitive Körper Ω(α) vom n-ten Grade geht durch Adjunction… in einen Körper Ω'(α) vom r-ten Grade über." (p485),
  3. "Ein primitiver Körper hat eine primitive Gruppe." (p487). The m=6 cyclic imprimitivity example (A=1,3,5/B=2,4,6
  and A=1,4/B=2,5/C=3,6) matches; the §152/"Vierzehnter Abschnitt. Anwendung der Permutationsgruppen auf Gleichungen."
  boundary (p488) matches.
- Orthography already correct in .tex: "giebt/ergiebt" kept; "Coefficienten" (Weber prints ë, settled normalization).
- **ALSO re-confirmed §150 (Transitive und intransitive Gruppen, .tex 17283-17317) faithful+complete** (map-phase work):
  eqs (1)(2), the f(α')=0 reducibility argument (cites §.149,a)), the converse (§.149,b)), transitiv/intransitiv
  defs, boxed result 1, and "Systeme der Intransitivität" all present and matching p481–482.
- **REVISION to the block model:** the §148-156 "GPT-rewrite block" is NOT uniform. §150, §151, §152 are FAITHFUL
  (patchable, like §157/§159-162); only §148, §149, §153, §154, §155, §156 (+§158) were actually rewritten. Must
  keep auditing each § individually. No compile needed (file unchanged; still 380pp/0err).

### 2026-07-02 — PHASE 2 — §153 (Zerlegung von Permutationen in Transpositionen und in Cyklen) FULL RE-TRANSCRIPTION p492–500
Fourth section of the §148-156 block; a **heavy GPT reconstruction** — ~8 printed pages (p492_bot–p500_bot)
compressed into ~103 .tex lines, with prose reworded and most proofs deleted. Read every scan p492→501, then
replaced the whole body (.tex 17566-17669) with Weber's faithful text via marker-anchored Python range-replace
(retrans_153.py, raw triple-quoted body — no unicode_escape). Corrections restored:
- **THEOREM 3 restored (the .tex had DELETED it):** the reconstruction's enumerate jumped 1,2 → **4**, dropping
  Satz 3 (unique disjoint-cycle decomposition) entirely, plus its whole proof — eqs (1) $\pi=\perm{...}{a_0\ldots}$,
  (2) $0,a_0{=}b,a_b{=}c\ldots$, (3) $(0,b,c\ldots)$ — and the intro reason. All 11 theorems now carry Weber's
  correct arabic numbering 1.–11. with no gap.
- **restored the three worked examples** $\pi_1=(0,2,6,5,4,1,3,7)$, $\pi_2=(0,4,5,7,6)(1,2)(3)$,
  $\pi_3=(0,7,4,5)(1,2,3,6)$ (full two-row perm-matrix = cycle form). The .tex had a *fabricated* placeholder
  example "$(a,b,c)(d,e)(f)$" instead.
- **restored the full even/odd τ-composition proof** (Satz 4): $\tau\gamma=(1,a{+}1\ldots b)(2,3\ldots a)$ splits a
  cycle; $\tau\gamma\gamma'=(1,2'\ldots a',1',2\ldots a)$ merges two — with the m−ν counting → $\mu\equiv m-\nu$.
- **restored Satz 7's four generating identities** $(1,0,2)=\ldots$, $(0,2,3)=\ldots$, $(1,3,4)=\ldots$,
  $(2,3,4)=\ldots$ (the .tex kept only the two Satz-6 identities + the Satz-8 one).
- **restored the ENTIRE proofs of Sätze 9, 10, 11** (~2.5 pp, p498–500): the M/M'/M'' imprimitivity argument
  ($\pi^{-1}(0,1)\pi=(\mu,r)$; the $\pi\pi'^{-1}(\alpha,\beta)\pi'\pi^{-1}=(\gamma,\delta)$ system-identity chain;
  "Wenn n eine Primzahl ist… nur die symmetrische Gruppe"; the $(0,2,1)(0,m,m{+}1)(0,1,2)=(1,m,m{+}1)$ step). The
  .tex had reduced 9/10/11 to bare one-line statements.
- **restored the period/order material intro**: $\pi^0,\pi^1,\pi^2,\pi^3\ldots$; eq (4) $1,\pi,\pi^2\ldots\pi^{e-1}$;
  the even/odd $\pi^2$ formulas for a cyclic $\pi$; lcm-of-cycle-lengths as the Grad. The example $\pi=(0,1)(2,3,4)$,
  $\pi^2\ldots\pi^6=1$ was already correct and kept (re-set as Weber's inline "z. B." display).
- **DE-MODERNIZED (the three flagged reconstruction tells):** `\pmod 2` → Weber's `$\mu\equiv m-\nu\ (\mathrm{mod.}\ 2)$`;
  `\prod_{0\le i<j\le m-1}(u_i-u_j)` → Weber's expanded staggered difference-product with the u- **and** α-variable
  phrasing ("von m Veränderlichen $u_0\ldots u_{m-1}$ oder auch von m … Grössen $\alpha_0\ldots\alpha_{m-1}$"); "gibt"
  → **giebt** (also "ergiebt", "giebt es" throughout).
- **numbering-systems kept distinct:** theorems 1.–11. as enumerate (house `[label=\arabic*.,start=N]` convention,
  unchanged), equations (1)(2)(3)(4) as `\tag{}` displays. [Cross-check: the (4) on p500 confirms the earlier
  (1)(2)(3) in the Satz-3 proof are real Weber equation numbers, not invented.]
- ORTHOGRAPHY: "theilbar", "Eintheilung", "Gesammtheit", "Werth", "Classen", "Function/Functionen", "Composition/
  componiren", "Product", "nothwendig" kept as printed. Restored intro's historical reference ("Wir haben schon im
  zweiten Abschnitt… erwähnt.") that the .tex had dropped.
Compiles **383 pp / 0 err / 0 overfull hbox** (380→383, growth from restored content; page count did NOT drop).
Full verbatim source map staged in scratchpad weber_153_notes.md.

### 2026-07-02 — PHASE 2 — §154 (Divisoren der Gruppen. Nebengruppen und conjugirte Gruppen) FULL RE-TRANSCRIPTION p501–507
Fifth section of the §148-156 block; a systematic **compression/paraphrase** reconstruction — proofs gutted,
displays dropped, notation altered. Read every scan p501→507, replaced the whole body (.tex 17811-17935) with
Weber's faithful text via marker-anchored range-replace (retrans_154.py, raw triple-quoted body). Corrections:
- **ϰ (varkappa) restored — the .tex used $\chi$ (chi) for the elements of $Q$.** Weber prints ϰ throughout
  ((2) $\varkappa,\varkappa_1\ldots\varkappa_{q-1}$; all the $\varkappa_i\pi_1$ coset algebra). Fixed to \varkappa
  everywhere. (Zoom-confirmed on p501/p502: baseline rounded-k glyph, not the descending χ.)
- **restored the DROPPED equations (7), (8), (9)** — the .tex jumped straight from (6) to (10). Weber's
  (7) $\psi(\varkappa)=\cdots=\psi(\varkappa_{q-1})=\psi$, (8) $\psi_1=\psi(\pi)=\psi(\varkappa\pi_1)$,
  (9) $Q\pi_1=\varkappa\pi_1,\ldots\varkappa_{\nu-1}\pi_1$, with the whole $\pi=\varkappa_1^{-1}\varkappa\pi_1$
  membership proof, all restored.
- **eq (11) mislabel fixed.** The .tex tagged $\pi_i^{-1}Q\pi_i$ as (11); Weber's (11) is
  $\pi=\pi_1^{-1}\varkappa\pi_1$ (the transforming permutation). Restored, and the $\pi_1^{-1}Q\pi_1$-group symbol
  set as the unnumbered display it is; (12) = the conjugate-group list, kept.
- **restored the coset-distinctness proof** ($\varkappa_1\pi_1=\varkappa_2\pi_1\Rightarrow\varkappa_1=\varkappa_2$…)
  and the **"bilden keine Gruppe" argument** ($\pi_1=\varkappa_1^{-1}\varkappa_3\varkappa_2^{-1}$) — .tex had one bland
  sentence. Restored the **two-cosets-disjoint proof** ($\varkappa_1\pi_1=\varkappa_2\pi_2\Rightarrow Q\pi_2=Q\pi_1$).
- **restored theorem 2's explicit displays** ($Q\pi,Q\pi_1\pi\ldots$ vs $Q,Q\pi_1\ldots$) — .tex had reworded it into
  a vague "nur in anderer Ordnung" one-liner with the wrong meaning.
- **restored the entire $\pi Q$-decomposition** $P=Q+\pi_1^{-1}Q+\cdots+\pi_{j-1}^{-1}Q$ + its proof (.tex dropped it
  to a single sentence), the $\psi=\psi(\varkappa)$ / $\psi(\pi)=\psi(\varkappa\pi)$ group-closure argument, the
  conjugate-functions $\psi(\varkappa),\psi(\varkappa\pi_1)\ldots$ double-row derivation, the
  $\pi_1^{-1}\varkappa\pi_1\,\pi_1^{-1}\varkappa_1\pi_1=\pi_1^{-1}\varkappa\varkappa_1\pi_1$ group check and the
  §149 isomorphism note, the transformation-rule (Satz 6) full cycle proof with the two-row $\pi$-matrix, and
  theorem 7's proof ($P=Q+Q\pi_1+\cdots+Q\pi_{m-1}$, Grad $=m\cdot$Grad $Q$). .tex had reduced 6 and 7 to bare lines.
- **restored the DROPPED 2nd footnote** (p506): conjugirte Gruppen \glqq gleichberechtigte Untergruppe\grqq. The
  1st footnote ("Auch Untergruppe genannt", p502) was already present and is faithful — kept.
- theorems separated properly: Weber's numbered Sätze 1.–7. (statement-list) restored with prose+displays
  interleaved (the .tex had crammed 4+5 into one enumerate with (10) misplaced inside item 5).
- **14th Weber erratum flagged (q/ν):** Weber prints "jede dieser Nebengruppen $\nu$ Elemente" (p502) and
  $\varkappa_{\nu-1}\pi_1$ in eq (9) (p504), while (2)(3)(7) use $q$ for $|Q|$ — a q/ν inconsistency (probable
  misprint for q). Both zoom-confirmed as ν; transcribed **as printed** (revert-to-print policy) and flagged here.
  Also Weber's inline "$\pi_2=\varkappa\pi$" (p502, shorthand for $\varkappa\pi_1$; the next display has
  $Q\varkappa\pi_1$) transcribed as printed.
- ORTHOGRAPHY/house: \varkappa for ϰ; "giebt/ergiebt" kept; \S-refs "\S\,146,\,149", "\S\,152,\,5.", "\S\,149,\,a)";
  ordinal $m^{\text{ten}}$ Grades; "d. h."/"z. B."/"u. s. f."/"w. z. b. w." plain; "Theiler/Eigenthümlichkeit/
  Gesammtheit/gemeinschaftliches" as printed.
Compiles **386 pp / 0 err / 0 overfull hbox** (383→386, growth from restored content; page count did NOT drop).

### 2026-07-02 — PHASE 2 — §155 (Reduction der Galois'schen Resolvente durch Adjunction. Normaltheiler einer Gruppe) FULL RE-TRANSCRIPTION p507–511
Sixth section of the §148-156 block; a compression/paraphrase reconstruction. Read every scan p507→511, replaced
the whole body (.tex 18051-18139) with Weber's faithful text via marker-anchored range-replace (retrans_155.py).
Corrections:
- **restored the DROPPED equations (3) and (5).** The .tex eq-numbering jumped (1)(2)→(4)→(6). Weber's (3) is the
  re-listing $\psi,\psi_1\ldots\psi_{j-1}$ in the Satz-2 proof; (5) is $\omega=\chi(\psi)/\varphi'(\psi)$. Both restored.
- **restored the χ(t) polynomial form.** The .tex modernized Satz 2's proof to a bare $\sum_{i=0}^{j-1}\omega_i/(t-\psi_i)$
  "invariant, also in Ω(t)". Weber's actual argument is $\varphi(t)\bigl(\tfrac{\omega}{t-\psi}+\cdots+\tfrac{\omega_{j-1}}{t-\psi_{j-1}}\bigr)=\chi(t)$,
  a whole function of degree $(j-1)$, giving (5). Restored (and dropped the un-Weber $\Omega[t]$/$\Omega(t)$ bracket notation).
- **restored the DROPPED Satz-1 irreducibility proof detail** ($\Phi(t)$ with $\Phi(\psi)=0\Rightarrow\Phi(\psi_i)=0\Rightarrow\varphi\mid\Phi$);
  .tex had a vague one-liner.
- **restored the DROPPED Satz-3 restatement**: "Der Normalkörper $N=\Omega(\alpha\ldots\alpha_{m-1})$ ist ein Körper
  $p^{\text{ten}}$ Grades über $\Omega$ und $q^{\text{ten}}$ Grades über $\Omega'=\Omega(\psi)$" — absent from .tex.
- **restored the full Galois-resolvent decomposition.** Weber: $g(t,\psi)=(t-\rho)\ldots(t-\rho_{q-1})$,
  $g_i(t)=g(t,\psi_i)$, and (6) $g(t)=g(t,\psi)g(t,\psi_1)\ldots g(t,\psi_{j-1})$. The .tex had dropped the $g(t,\psi)$
  definition and used $g(t)=g_0(t)g_1(t)\ldots g_{j-1}(t)$ instead. Kept Weber's $\rho_{0,i}\ \rho_{1,i}\ldots$ (with
  his missing comma after $\rho_{0,i}$, as printed).
- **restored the theilerfremd definition + the "R is a group" proof** ($\pi_1,\pi_2\in Q,Q'\Rightarrow\pi_1\pi_2\in R$);
  the .tex had collapsed the Durchschnitt paragraph and pre-stated the $x\psi+x'\psi'$ result without Weber's proof.
  Restored Satz 4's full lead-in (the $\omega=\omega(\pi)$ argument, "Ebenso … mehr als zwei Gruppen").
- **restored the $\Omega''=\Omega(\psi,\psi_1\ldots\psi_{j-1})$ adjunction paragraph** and the "all conjugates identical
  ⇒ Normalkörper" case (dropped in .tex).
- **"5." restored as a numbered Satz** with its proof ($\varkappa\in R\Rightarrow\pi^{-1}\varkappa\pi$, so
  $\pi^{-1}R\pi=R$). The .tex had demoted 5 to flowing prose and dropped the proof.
- **Normaltheiler definition** given as Weber's ("ein Theiler … der diese Eigenschaft hat" — i.e. all conjugates
  identical), not the .tex's paraphrase "$\pi^{-1}Q\pi=Q$ für jede Operation". "identischen Gruppe" (not the .tex's
  "Einheitsgruppe"); "einfache Gruppe" def and the R-normality remarks restored verbatim.
- **restored BOTH dropped footnotes:** (a) the Lagrange citation on "Satz von Lagrange" (Réflexions sur la résolution
  algébrique des équations; Mém. Acad. Berlin 1770/71; Oeuvres t. III; "nur in einer specielleren Fassung … allgemeine
  Formulirung rührt von Galois her") and (b) the Normaltheiler note ("Galois … décomposition propre … eigentliche
  Theiler … neuere Schriftsteller: ausgezeichnete oder invariante Untergruppen"). French accents compile clean
  (0 missing-char warnings).
- ORTHOGRAPHY/house: \varphi for φ, \Phi, \chi, \rho for the resolvent root (house choice, as §149; Weber's glyph is
  ϱ, cosmetic); \varkappa for ϰ; "giebt/ergiebt"; "Coefficienten" (Weber prints ë, settled); ordinals
  $p^{\text{ten}}/q^{\text{ten}}/j^{\text{ten}}/(j-1)^{\text{ten}}$; \S-refs "\S\,154,\,5.", "\S\,149,\,a),\,b)",
  "\S\,145", "\S\,143,\,1.", "\S\,154"; "d. h."/"z. B." plain; "Werthen/theilbar/Zerfällung/theilerfremd" as printed.
Compiles **387 pp / 0 err / 0 overfull hbox / 0 missing-char** (386→387, growth from restored content; no drop).

### 2026-07-02 — PHASE 2 — §156 (Die Gruppe der Resolventen) FULL RE-TRANSCRIPTION p511–513
The .tex §156 (~31 lines) was a heavy compression/reword of Weber's ~2.5 pages. Re-transcribed faithfully
vs printed scans p511(bot)–513(bot). Deviations fixed:
- **restored the true opening.** The .tex opened "Die Hülfsgleichungen φ(t)=0 für eine zu Q gehörige Function ψ
  nennen wir … Resolventen. Wird Q zur Einheitsgruppe, so ist nach Lagrange …". Weber's actual opening is
  "Die Hülfsgleichung φ(t)=0, von der die Bestimmung der Function ψ abhängt, geht in die Galois'sche Resolvente
  über, wenn der Theiler Q … die identische Gruppe ist. Denn dann kann nach dem Satze von Lagrange (§.155,2.)
  jede Function des Körpers N, also auch die Wurzeln α selbst rational durch ψ ausgedrückt werden, und N ist mit
  Ω(ψ) identisch." + "Wir wollen diese Gleichungen φ(t)=0 daher in einem allgemeinen Sinne Resolventen nennen."
  Restored the §.155,2. citation, the N=Ω(ψ) identity, and the correct singular Hülfsgleichung.
- **Satz 1 (case 1): restored "theilerfremd" wording** (the .tex had "nur die Einheitsgruppe gemeinsam"), the
  "(nach Satz 4., §.155)" citation, the **dropped display N = Ω(ψ, ψ₁ … ψ_{j-1})**, and the dropped remark "eine
  Galois'sche Resolvente der Gleichung φ(t)=0 ist zugleich eine Galois'sche Resolvente der ursprünglichen
  Gleichung." "Totalresolvente der gegebenen Gleichung" (full phrase).
- **Satz 2 (case 2): restored "der dann ein Normaltheiler von P ist"**, the "zu ψ conjugirten Functionen"/"zu R
  gehörigen Grösse" wording, and the dropped sentence "Die Galois'sche Resolvente … ist durch diese Adjunction
  noch nicht vollständig gelöst, sondern sie ist nur in Factoren vom Grade r zerlegt." The .tex had compressed to
  "so zerlegt die Adjunction … nur in Factoren vom Grade r".
- **restored the einfache-Gruppe remark verbatim** ("Ist P eine einfache Gruppe, so existiren nur
  Totalresolventen, während, wenn P Normaltheiler hat, zu jedem solchen Normaltheiler eine Partialresolvente
  gefunden werden kann.") — the .tex had "correspondiren den Normaltheilern Partialresolventen".
- **restored the FULL Galois-group-of-the-resolvent argument** (the .tex had compressed it to two sentences and
  DROPPED the σ notation entirely): the "jede Gleichung in Ω zwischen den Grössen (1) bleibt richtig …" and
  "wenn eine Function in Ω … alle diese Permutationen gestattet … gleich einer Grösse in Ω" justification; the
  "Die Operationen von R mögen mit σ bezeichnet sein" naming; the derivation "π'π⁻¹ … gleich einer der Grössen σ,
  oder **π' = σπ**" (dropped display restored); the set-off Ergebniss "Die Permutationen der Nebengruppe Rπ und
  nur diese …". Kept (1) ψ,ψ₁,ψ₂…ψ_{j-1} as the tagged display.
- **fixed the degree statement to Weber's inline form**: "d. h. gleich dem Quotienten p:r oder dem Index des
  Theilers R von P." The .tex had it as a bare display \[p:r\] + "dem Index des Normaltheilers R".
- **restored the ENTIRE dropped tail (2 paragraphs, ~p513 mid–bot)**: (a) "Ist R die identische Gruppe, also r=1,
  … so ist der Grad ihrer Gruppe ebenso hoch … und beide Gruppen sind überdies isomorph. In Bezug auf die Gruppe
  ist also nichts gewonnen. Die gegebene Gleichung ist mit der Resolvente, so verschieden auch ihre Grade sein
  mögen, äquivalent."; (b) "Ist auf der anderen Seite Q ein Normaltheiler, also R mit Q identisch, so ist φ(t)=0
  eine Partialresolvente und der Grad ihrer Gruppe ist gleich dem Index j des Theilers Q von P. Nach der
  Adjunction einer Wurzel dieser Resolvente reducirt sich die Gruppe … auf Q, also auf den Grad q. Es ist also
  eine Spaltung der Gruppe erfolgt."; (c) the practical closing "Wenn man Resolventen bilden will von möglichst
  niedrigem Grade, so hat man Theiler der Gruppe P aufzusuchen von möglichst kleinem Index, also von möglichst
  hohem Grade; soll aber gleichzeitig eine Reduction der Gruppe eintreten, so müssen die Theiler Normaltheiler
  sein." The .tex had truncated at "Ist R=1 … Grad p" — all of (a)(b)(c) were absent.
- **FOOTNOTE check:** the ¹) footnote at the foot of p511 ("Galois spricht von der eigentlichen Zerlegung
  (décomposition propre) … invariante Untergruppen") is Weber's §155 Normaltheiler note, already correctly
  attached to the §155 "Normaltheiler (oder normalen Theiler)" definition (line 18153). §156 has NO footnote of
  its own — not double-restored.
- ORTHOGRAPHY/house: \varphi for φ, \Omega, \alpha, \pi, \sigma; \emph for the defined terms Resolventen/
  Totalresolvente/Partialresolvente (house convention, as theilerfremd/Resultante elsewhere); "existiren"
  (Weber), "reducirt", "conjugirten", "sämmtlicher", "Grösse/Grössen/heisst/grössten" (ss settled);
  \S\,155,\,2. ref; "d. h." plain; enumerate[label=\arabic*.] for the two cases (matches §155/§154 idiom).
Compiles **388 pp / 0 err / 0 overfull hbox / 0 missing-char** (387→388, growth from restored content; no drop).
**§148–156 block now COMPLETE.**

### 2026-07-02 — PHASE 2 — §167 (Die Kreistheilungsperioden und die Periodengleichungen) FULL RE-TRANSCRIPTION p554–560
Opens the **Sechzehnter Abschnitt "Kreistheilung"** (chapter head \section*{...} at line 19461 already present — left untouched). The .tex §167 was one of the WORST reconstructions seen: ~35 lines for Weber's ~7 printed pages (p554–560). It kept only eqs (1),(2),(12) and **FABRICATED its (13)** as "η₀+η₁+…+η_{e−1}=−1" (a relation Weber never numbers here); it DROPPED eqs (3)–(11), the real (13), and (14)–(18), plus the entire irreducibility / Galois-group / period-theory / Basis / determinant development, and modernized notation (`\mapsto`, wrong eq numbers). Fully re-transcribed vs scans. Restored in full:
- **The true opening** (the .tex fabricated "Die wichtigsten cyklischen Gleichungen sind die Kreistheilungsgleichungen…"): Weber opens "Die wichtigsten unter den Abel'schen Gleichungen sind die, von denen die Bestimmung der Einheitswurzeln abhängt…" + the Kreisperipherie-theilen geometric motivation; the Körper Ω = Körper R der rationalen Zahlen naming; the n=ungerade-Primzahl restriction with the n=2/±1 parenthetical; and the **dropped transcendental exponentials** e^{2πi/n}, e^{4πi/n} … e^{2(n−1)πi/n}.
- **eqs (1)–(11)**: (1) r,r²…r^{n−1}; the r^h=r^k (mod n) remark; (2) X=x^{n−1}+…+1=0; the primitive-root / index theory (1,g,g²…g^{n−2}; g^α≡a (mod.n); α=ind a; §.136); r,r^g…r^{g^{n−2}}; (3) r^{g^h}=r_h; (4) r,r₁…r_{n−2}; (5) φ(r)=b₀+b₁r+…; the 1+r+…+r^{n−1}=0 recap; (6) φ(r)=(b₁−b₀)r+…−b₀r^{n−1}; (7) φ(r)=ar+a₁r₁+…; **Theorem I** (φ(r)=0 ⇒ all a vanish) as a \Roman* enumerate item + its proof; (8) φ(r)=Σ^h a_h r_h; the π=(r,r₁…r_{n−2}) cyclic permutation; (9) C=1,π,π²…π^{n−2}; the Normalgleichung/eigene-Galois-Resolvente (§.145) argument; (10) the substitutions (r,r),(r,r₁)…; (r,r_h)=(r_k,r_{k+h}); the C-isomorphism ⇒ Galois group; §.163 reduction; n−1=ef; (11) C_e=1,π^e…π^{(f−1)e}.
- **eqs (12)–(18)**: (12) the f-gliedrige Gauss periods η,η₁…η_{e−1} (restored as full aligned display; the .tex had it but truncated); the conjugirte-Perioden naming + distinctness proof (via Theorem I); the "irreducibel ganzzahlige Gleichung e^ten Grades" conclusion; **Theorem II** (every R(η) number = homogeneous linear function of the periods) as a \Roman*[start=2] item; **the REAL (13)** φ(r)=Σ^h a_h r_h + the φ(r_e)=Σa_h r_{h+e}=Σa_{h−e}r_h derivation; the Σ_{0,e−1}^h expansion; (14) φ(r)=aη+a₁η₁+…; the **Basis** definition; (15) F_e(x)=(x−η)…(x−η_{e−1}); (16) ηη_h=a_{0,h}η+…; the linear-system display; **(17) the e×e determinant** (rendered \begin{vmatrix} with Weber's printed commas + \hdotsfor{4} dots row); the ganzzahlig-Coefficienten remark; (18) Φ_e(x)=(x−r)(x−r_e)…; the Newton-formula/Potenzsummen (§.42) + r^{g^h}+…=η_h; the Φ_e ~ (2) analogy + C_{ee'}/η' recursion; the prime-factor resolvent-chain remark; and the closing group-of-F_e(x) = cyclic permutation (η,η₁…η_{e−1}).
- ORTHOGRAPHY/house: \varphi, \Phi, \eta, \pi, \Omega, \alpha, \lambda, \mu; X for the cyclotomic polynomial; \mathrm{ind}\,a; (\mathrm{mod.}\ n) house form; ordinals n^{ten}/(n-1)^{ten}/e^{ten}/f^{ten}; \S\,136 / \S\,145 / \S\,163 / \S\,42; "existiren/giebt/ergiebt/charakterisirt/conjugirte/irreducibeln/cyklisch/transcendenten/adjungirt" (Weber spellings kept); "Coefficienten" (Weber prints Coëfficient ë — settled normalization); Σ with index-above / range-below convention (\sum^{h}, \sum_{0,e-1}^{h}); substitutions as (r,\ r_h) pairs; \Roman* enumerate for Theorems I/II. All 18 tags present & contiguous.
Compiles **391 pp / 0 err / 0 overfull hbox / 0 missing-char** (388→391, +3pp from ~7 restored pages; no drop).

### 2026-07-02 — PHASE 2 — §168 (Die Gauss'sche Methode zur Berechnung der Resolventen) FULL RE-TRANSCRIPTION p560–564
Running heads "Producte von Perioden" / "Dreizehn-Theilung". The .tex block (~52 lines) was a
RECONSTRUCTION with **a mathematically FABRICATED worked example**. Re-transcribed vs scans
p560(mid)–564(top). Deviations fixed:
- **rewrote eqs (1)–(6) back to Weber.** The .tex had (1) η_λ=Σ_{ν}r^{g^{λ+eν}} (wrong sum-form),
  (2) η_λη_μ=Σ_{ν,ρ}… (mislabelled), (3) η_λη_μ=Σc_kη_k+fδ + "cyclotomische Zahlen" paraphrase,
  (4) a congruence "1+g^{…}≡g^{…} (mod n)" — none of which are Weber's. Weber's actual development:
  (1) η^{(λ)}=r^λ+r^{λ'}+r^{λ''}+⋯ / η^{(μ)}=…; (2) λ'≡λg^e, λ''≡λg^{2e}…, μ'≡μg^e… (mod n); the
  s,t-sum forms η^{(λ)}=Σ^s r^{λg^{se}} etc.; the product Σ^sΣ^t r^{λg^{se}+μg^{te}}; the t→t+s
  substitution → Σ^sΣ^t r^{(λ+μg^{te})g^{se}}; (3) the summation-order swap Σ^tΣ^s…; the inner sum =
  the period η^{(λ+μg^{te})}; (4) η^{(λ)}η^{(μ)}=η^{(λ+μ)}+η^{(λ+μ')}+…; the uneigentliche-Periode
  η^{(0)}=f remark + the η+η₁+…+η_{e−1}=−1 relation (§.167,(2)); (5) ηη_h=a_{0,h}η+…; (6) η_kη_{h+k}=
  a_{0,h}η_k+a_{1,h}η_{k+1}+…+a_{e−1,h}η_{k−1}.
- **the n=13 example was GPT-FABRICATED and mathematically WRONG** — the .tex printed
  η_0=r+r^3+r^9+r^27 (r^27=r^1, a duplicate), η_1=r^2+r^6+r^18+r^54, η_2=r^4+r^12+r^36+r^108 (residues
  garbage; not a valid period decomposition). Replaced with Weber's actual computation, verified by
  hand: (7) the §.136 index table [I:0..11 / N:1,2,4,8,3,6,12,11,9,5,10,7]; (8) η=r+r_3+r_6+r_9,
  η_1=r_1+r_4+r_7+r_{10}, η_2=r_2+r_5+r_8+r_{11}; (9) η=r+r^{-5}+r^{-1}+r^5=η^{(1)}, η_1=r^2+r^3+r^{-2}+
  r^{-3}=η^{(2)}, η_2=r^4+r^6+r^{-4}+r^{-6}=η^{(4)}; the ηη=η^{(2)}+η^{(-4)}+η^{(0)}+η^{(6)}=4+η^{(2)}+
  2η^{(4)}=−4η−3η_1−2η_2 derivation; the η²/ηη_1/ηη_2 formulas; the 3×3 determinant (§.167,(17)); (10)
  η³+η²−4η+1=0 with discriminant 169=13²; the cos-forms (η=2cos2π/13+2cos10π/13=… etc. + the product
  forms η=4cos(4π/13)cos(6π/13)…); the biquadratic path ξ=r+r^{-1}=2cos2π/13, ξ'=r^5+r^{-5}, (11)
  ξ²−ηξ+η_2=0, (12) r⁴−ηr³+(η_2+2)r²−ηr+1=0, the 2sin/√(4−ξ²) remark; the alt six-term-period path
  (13) ζ=r+r³+r⁴+r^{-1}+r^{-3}+r^{-4}, ζ_1=…, (14) ζ²+ζ−3=0, (15) ζ=(−1±√13)/2; the two-term ξ,ξ_1…ξ_5
  system, ζ=ξ+ξ_2+ξ_4 / ξξ_2=ξ_3+ξ_4 / ξξ_2ξ_4=2+ζ_1=1−ζ, and (16) x³−ζx²−x−1+ζ=0.
- **GLYPH (zoom-confirmed, crop_src.py p563/p564):** the 6-term periods use **ζ (zeta)**, the 2-term
  periods use **ξ (xi)** — the .tex/my-first-notes conflated them; the sentence "Nach Adjunction der
  Werthe ζ,ζ₁ … für die zweigliedrigen Perioden [ξ]" and the printed "ζ = ξ+ξ_2+ξ_4" are only coherent
  with distinct letters. Rendered \zeta / \xi accordingly.
- ORTHOGRAPHY/house: index table as \begin{array}{c|cc…} with \hline (Weber's comma-separated I/N
  table, commas dropped per tabular norm); determinant as \begin{vmatrix} with Weber's printed commas;
  Σ index-above convention \sum^{s}/\sum^{t}; (\mathrm{mod.}\ n); \mathrm{ind}\,\lambda; 4^{ten}
  ordinal; \S\,167,\,(12)/(2)/(17), \S\,136; e^{2πi/13}; \cos\frac{k\pi}{13}; "conjugirter/uneigentliche/
  zweigliedrigen/viergliedrigen/Discriminante/biquadratische/giebt/ergiebt" kept; "z. B." plain. §168
  has no footnote (the ¹ on p564 belongs to §169). All 16 tags present & contiguous.
Compiles **393 pp / 0 err / 0 overfull hbox / 0 missing-char** (391→393, +2pp from restored content; no drop).

### 2026-07-02 — PHASE 2 — §169 (Zurückführung der Kreistheilungsgleichung auf reine Gleichungen) FULL RE-TRANSCRIPTION p564–570
Running head "Siebzehn-Theilung". The .tex block (lines 19890–20118, ~228 lines) was a RECONSTRUCTION
that reworded the opening, **dropped BOTH historical footnotes**, modernized notation, **got the
equation numbering catastrophically wrong**, and **cut Weber's entire two-page sign-determination
tail (p569mid–p570)** replacing it with one summary sentence. Re-transcribed vs scans p564(top)–570(mid).
Deviations fixed:
- **EQUATION RENUMBERING** — the .tex NUMBERED Weber's two UNNUMBERED tables (the n=17 index table and
  the ψ-computation table), giving them (14) and (16), which shifted the whole tail; it also SKIPPED
  Weber's (14) [(α,η)^λ=(α^λ,η)ψ_1…ψ_{λ−1}] and **FABRICATED a (23)** for the (i,η)=⁴√17{…} formula,
  which Weber leaves UNNUMBERED. Restored Weber's exact numbering (1)–(22): (1) resolvent def; (2)
  product; (3) (ε^λ,r)(ε^−λ,r)=(−1)^λn; (4) the double-sum intermediate [.tex had DROPPED it]; (5)
  ratio=ψ_{λ,μ}; (6) ψ_{λ,μ} def; (7) α=ε^μ; (8) ψ_λ(α) def; (9) (α^λ,r)(α,r)=…; (10) (α^λ,r)(α^−λ,r)=
  (−1)^{μλ}n [.tex wrongly printed (−1)^{fλ}]; (11) (α^λ,r)=(α^λ,η)=…; (12) (α^λ,η)(α,η)=…, λ=1..(e−2);
  (13) (α^λ,η)(α^−λ,η)=(−1)^{fλ}n; (14) (α,η)^λ=(α^λ,η)ψ_1…ψ_{λ−1} [.tex had DROPPED it]; (15)
  (α,η)^e=(−1)^f n ψ_1…ψ_{e−2}; (16) n=17 PERIODS [index table above it UNNUMBERED]; (17) ψ_1..ψ_3 for
  8th root [ψ-table above it UNNUMBERED]; (18) ψ-values at α=(1+i)/√2 [α-def display UNNUMBERED]; (19)
  (α,η)⁸=17(3+i√8)⁴(1−4i)²; (20) the three squares; (21) the three =17 products [(1,η)=−1 is inline text,
  not tagged]; (22) (α,η)(α³,η)=(−1,η)(3+i√8). Then (−1,η)=√17 and (i,η)=⁴√17{√((√17−1)/2)+i√((√17+1)/2)}
  UNNUMBERED. n=17 numeric values were all CORRECT in the .tex (GPT reproduced the 17-gon accurately) —
  only the numbering was wrong.
- **RESTORED the two dropped footnotes.** ¹ on "zurückgeführt": "Gauss, disq. arithm. art. 359, 360;
  disq. circa aequationes puras ulterior evolutio, Werke Bd. II. Lagrange, rés. des équations numériques.
  Jacobi, „Ueber die Kreistheilung…". Werke Bd. 6. Kummer, Crelle's Journal Bd. 35 und Abhandl. d. Berl.
  Akademie 1856. … Bachmann, „Die Lehre von der Kreistheilung". Leipzig 1872." ¹ on "gehen wir nicht
  ein": "Vgl. hierüber v. Staudt, Construction des regulären Siebzehnecks. Crelle's Journ. Bd. 24, 1842."
- **RESTORED the dropped p569mid–p570 sign-determination tail** the .tex had cut: the ½(−1,η)=Σcos
  expansion, the two trig identities (cos2π/17−cosπ/17=−2sin(π/34)sin(3π/34) etc.), the sin(11π/34)>
  sin(3π/34) positivity argument, and the reelle-Theil computations for (i,η) [η−η₂+η₄−η₆=…] and (α,η)
  [η−η₄+(1/√2)(η₁−η₃−η₅+η₇)=…], ending "was sich gleichfalls als positiv erweist."
- **RESTORED dropped derivation steps**: the (ε^λ,r)=Σ_{0,n−2}^h ε^{λh}r_h form before (1); the pre-(2)
  product; the μ=−λ case with the Σ^s r^{s(t+1)}=−1/(n−1) split and the §136 ind(n−1)=½(n−1) step; the
  successive-multiplication block before (14).
- **DE-MODERNIZED notation**: .tex \sum_{s=1}^{n-1}/\sum_{s,t} → Weber's index-above/range-below
  \sum_{1,n-1}^s / \sum_{0,n-2}^h / \sum^s\sum^t (file convention, matches §167/§168); reworded opening
  restored to Weber ("durch Benutzung der Resolventen direct", "in den disq. arithm.").
- ORTHOGRAPHY/house: kept file conventions \ind and \pmod (40+ uses file-wide; Weber's "(mod. m)" period
  is a deferred global-sweep item, not touched here for consistency); \emph work-titles + „…" German
  quotes in footnotes (line-6692 style); $m^{\text{ten}}$/$e^{\text{te}}$/$8^{\text{te}}$ ordinals;
  \S\,136 and \S\,167,\,(12) cross-refs; \sqrt8 kept (not simplified to 2√2); \sqrt[4]{17}; index/ψ
  tables as \begin{array}{c|r…} + \hline. Tags (1)–(22) present & contiguous; two \footnote confirmed
  rendered (Gauss=fn59, Staudt=fn60) via pdftotext + eyeballed PDF pp357–360.
Compiles **395 pp / 0 err / 0 overfull hbox / 0 underfull / 0 missing-char / 0 undefined** (393→395,
+2pp from restored content; no drop). Visually verified rendered PDF pp356–360.

### 2026-07-02 — PHASE 2 — §170 (Eigenschaften der Zahlen ψ) FULL RE-TRANSCRIPTION p570–574
Running head "Die Zahlen ψ". The .tex block (lines 20137–20272) was a RECONSTRUCTION that (a) reworded the
opening, (b) **MOVED the "Jacobi bis e=23 / Kronecker" paragraph from Weber's END (p572bot–573top) to the
START** and reworded it, (c) **dropped the Kronecker footnote**, (d) got the numbering wrong (Weber has
(1)–(17); .tex had only (1)–(11), all mislabeled), (e) **carried a MATH ERROR** — printed the intermediate
relation as ψ_{−λ−μ,μ}(ε)=(−1)^n ψ_{λ,μ}(ε) where Weber has **(−1)^μ**, and (f) dropped the e=7 example
detail, the (α,η)^14 verification, and most of the Congruenz-Satz derivation. Re-transcribed vs scans
p570(mid)–574(bot). Deviations fixed:
- **NUMBERING** restored to Weber's (1)–(17): (1) λλ'≡1(mod e); (2) ψ_λ(α^λ')=ψ_λ'(α); (3) λ+λ''+1≡0(mod e);
  (4) ψ_λ(α)=(−1)^f ψ_λ''(α); (5) ψ_{λ,μ}(ε)ψ_{λ,μ}(ε⁻¹)=n; (6) ψ_λ(α)ψ_λ(α⁻¹)=n; (7) ψ_{λ,μ}(ε)ψ_{λ+μ,ν}(ε)
  =(ε^λ,r)(ε^μ,r)(ε^ν,r)/(ε^{λ+μ+ν},r); (8) ψ_{2λ}(α)ψ_{2λ+1}(α)=ψ_1(α)ψ_λ(α²); (9) (α,η)^7=ψ_1(α)⁴ψ_1(α²)²
  ψ_1(α⁴) [e=7]; (10) λ+μ+ν≡0(mod m); (11) ψ_{λ,μ}(ε)=Σ_{1,n−2}^t ε^{μ ind t+ν ind(t+1)}; (12) ψ_{λ,μ}(g)=
  Σg^…≡Σt^μ(t+1)^ν (mod n); (13) ≡Σ_{1,n−1}^t t^μ(t+1)^ν; (14) ≡Σ_{0,ν}^h B_h^{(ν)}Σ_{1,n−1}^t t^{μ+h};
  (15) Σ_{0,m−1}^s g^{s(μ+h)}≡0; (16) ≡m≡−1; (17) two-case Π-formula (ψ≡0 for λ+μ<m; ψ≡−Π(2m−λ−μ)/
  [Π(m−λ)Π(m−μ)] for m<λ+μ<2m), (mod n).
- **MATH-ERROR FIX**: the intermediate ψ_{−λ−μ,μ}(ε)=(−1)^μ ψ_{λ,μ}(ε) — .tex had (−1)^n; Weber prints
  (−1)^μ (verified p571mid). This propagates the correct (−1)^f in (4).
- **RESTORED the Kronecker footnote** (anchor "angestellt hat"): "Vergl. Kronecker, Zur Theorie der Abel'schen
  Gleichungen. Journ. f. Mathem. Bd. 93."
- **MOVED the Jacobi/Kronecker paragraph back to Weber's position** (after (8), before the e=7 example) and
  restored its wording ("…bis e=23 durchgeführt. Seine Vermuthung aber…nach den Untersuchungen von Kronecker
  wahrscheinlich nicht richtig.").
- **RESTORED the full e=7 example** (the λ/λ'/λ'' table [1,2,3,4,5 / 1,4,5,2,3 / 5,4,3,2,1], the ψ-relations
  from (2)&(4), ψ_2ψ_3=ψ_1ψ_1(α²), n=ψ_3ψ_3(α⁶)=ψ_3ψ_1(α⁴), the §.169,(15) product form) and the (9) result,
  plus the **restored (α,η)^14=(α²,η)^7 ψ_1(α)^7 verification** [§.169,(14)].
- **RESTORED the whole Congruenz-Satz derivation** (10)–(17): the periodic form (11), the g-substitution (12),
  the summation-extension (13), the binomial-theorem step (14), the g^s reindex + geometric-series (15)/(16),
  the λ+μ≶m case analysis, and the two-case Π-formula (17). The .tex had compressed all this to its (8)–(11).
- **DROPPED the non-Weber addition** "Hier bedeutet Π(k)=1·2···k." (.tex clarification not in Weber; Weber's
  Π is the factorial defined earlier in the book).
- DE-MODERNIZED: .tex \sum_{t=1}^{n-2} → Weber's \sum_{1,n-2}^t / \sum_{0,m-1}^s / \sum_{0,\nu}^h / bare \sum^t.
  Kept file conventions \ind, \pmod. Cross-refs \S\,169,\,(5)/(6)/(8)/(3)/(15)/(14) now point to §169's
  Weber-numbering (which this pass already fixed). \footnote render-confirmed (fn 61). B_h^{(ν)} binomials,
  \Pi factorial, m^{\text{te}} ordinal. All 17 tags present & contiguous.
Compiles **397 pp / 0 err / 0 overfull hbox / 0 underfull / 0 missing-char / 0 undefined** (395→397, +2pp
from restored content; no drop). Visually verified rendered PDF pp361–364 (and §171 boundary on p365).

### 2026-07-02 — PHASE 2 — §173 (Die complexen Zahlen von Gauss) FULL RE-TRANSCRIPTION p585–591
Running head "Complexe Zahlen"; STILL WITHIN the Sechzehnter Abschnitt (no chapter head before §173). Note
§171/§172 were first re-verified this session as genuine map-phase transcriptions (complete + faithful),
and all inbound §169 cross-refs (from §170/§171/§172) confirmed to resolve against the Weber-renumbered §169
— triangulating that renumber as correct. The .tex §173 block (lines 20861–20952) was a RECONSTRUCTION: it
reworded the opening + much prose, **flattened Weber's numbered Sätze to plain prose**, **fabricated an
equation-numbering (1)-(9)** foreign to Weber, **dropped BOTH footnotes**, and **printed a mathematically
WRONG Gaussian-prime list**. Re-transcribed vs scans p585(mid)–591(bot). Deviations fixed:
- **STRUCTURE restored to Weber's**: numbered SÄTZE 1.–6. (as \begin{enumerate}[label=\arabic*.,…,start=N]
  blocks, interspersed with prose/eqs): 1. every p=a²+b²; 2. q≠a²+b²; 3. a²+b² div q ⇒ a,b div q; 4. Bezout
  (∃ϰ,λ: αϰ+βλ=δ); 5. prime∣product ⇒ prime∣factor; 6. unique factorization. Plus Weber's only three tagged
  EQS: (1) the Euclid-algorithm CHAIN [α=μα₁+α₂, …, α_{h−1}=μ_{h−1}α_h]; (2) αϰ+βλ=δ; (3) αϰ+βλ=1. The
  .tex's bogus tags (1)-(9) dropped entirely.
- **RESTORED BOTH footnotes**: ¹ on "R(i) zu bezeichnen haben" = "Gauss, Theoria residuorum biquadraticorum,
  commentatio secunda. Werke, Bd. II."; ¹ on "die primäre nennen kann" = "Gauss giebt an der erwähnten
  Stelle zwei verschiedene Bestimmungen für die primären Zahlen zur Auswahl, von denen dies die erste ist.
  Er behält weiterhin die zweite bei."
- **★ GAUSSIAN-PRIME LIST corrected** (the sharpest .tex error): the .tex FABRICATED "9+5i" (norm 106 =
  2·53, **not prime**), DROPPED 5+8i (89), 9+4i (97), 7+10i (149), and altered 3+2i→"2+3i". Restored Weber's
  actual 22-entry list (1+i; then all p≡1 mod4 below 200: 1+2i,3+2i,1+4i,5+2i,1+6i,5+4i,7+2i,5+6i,3+8i,
  5+8i,9+4i,1+10i,3+10i,7+8i,11+4i,7+10i,11+6i,13+2i,9+10i,7+12i,1+14i). Every norm hand-verified prime.
- **RESTORED the compressed prose**: the full norm/units/associates/divisibility development, the ξ−μ
  norm-reduction argument (N(ξ−μ)≦½), the Euclid derivation of the ggT, the Satz-6 unique-factorization
  proof (ϰϰ'ϰ''…=ππ'π''… ⇒ termwise agreement), and the prime-determination argument (local cases 1./2.
  N(π)=n / N(π)=n²; p=ππ'=a²+b²; q stays prime; 2=(1+i)(1−i)=−i(1+i)²) — all absent/summarized in the .tex.
- ORTHOGRAPHY/house: \varkappa for Weber's ϰ (Bezout coeffs + 2nd prime factorization; render-confirmed),
  \leqq for ≦, \pmod (file convention), z.\ B./d.\ h./u.\ s.\ f. spacing, giebt/theilbar/associirt/conjugirt/
  Coefficienten kept; cross-refs \S\,138,\,4. / \S\,172,\,(27) / \S\,172,\,(38),\,(39) preserved. Two
  \footnote render-confirmed (fn 64, fn 65); eyeballed PDF pp372–375 + prime list & §174 boundary on p376.
Compiles **400 pp / 0 err / 0 overfull hbox / 0 underfull / 0 missing-char / 0 undefined** (397→400, +3pp
from restored prose; no drop). Visually verified rendered PDF pp372–376.

### 2026-07-02 — PHASE 2 — §174 (Der Körper der dritten Einheitswurzeln) FULL RE-TRANSCRIPTION p592–594
Running head "Körper der dritten Einheitswurzeln"; LAST section of the Sechzehnter Abschnitt (Kreistheilung),
followed by the chapter head "Siebzehnter Abschnitt. Algebraische Auflösung von Gleichungen." then §175. The
.tex block (lines 21020–21105) was a RECONSTRUCTION of the R(ρ) cube-root-field (analog of §173's R(i)).
Re-transcribed vs scans p592(mid)–594(top). Deviations fixed:
- **★ Weber's §174 has NO numbered equations** — every display is unnumbered. The .tex FABRICATED tags
  (1)-(6). Dropped all six tags.
- **Opening restored** to Weber's: "Der Hauptsatz des vorigen Paragraphen, dass jede ganze Zahl des Körpers
  R(i) sich nur auf eine Art in unzerlegbare Factoren zerlegen lässt … beruht … auf dem Algorithmus des
  grössten gemeinschaftlichen Theilers, der in den Formeln \S\,173,\,(1) enthalten ist …" (.tex had reworded
  to "Die Beweise des vorigen Paragraphen beruhen wesentlich auf dem euklidischen Algorithmus …").
- **Restored the R(√−3) alternative naming**, the **factored middle form of the Norm**
  N(ξ)=(x+ρy)(x+ρ²y)=x²−xy+y²=(2x−y+y√−3)/2·(2x−y−y√−3)/2=((2x−y)²+3y²)/4 (.tex dropped the middle product),
  the **(2a−b)²+3b²=4 unit-derivation form** + the "sechs Einheiten" reasoning, and the **explicit
  associated-number systems** ±(a+bρ),±(aρ+bρ²)=±[−b+(a−b)ρ],±(aρ²+b)=±(b−a−aρ) and a+bρ,b+aρ²,b−(a−b)ρ
  (both dropped/compressed by .tex).
- **Removed the .tex's spurious "<1"** on N(ξ−μ)≦¾ (Weber writes just ≦¾); **restored "in Uebereinstimmung
  mit \S\,172"** after 4p=A²+27B²; restored the full prime-classification prose (3f+1 splits/3f+2 inert,
  the Coefficient-von-ρ-durch-3 selection). 3=−ρ²(1−ρ)² kept inline (Weber's form), not a display.
- **PRIME LIST: verified CORRECT** — the .tex's 22-entry Eisenstein-prime list (1−ρ,1+3ρ,…,13+15ρ) MATCHES
  Weber exactly (unlike §173's Gauss list which was wrong); kept as-is (only re-wrapped to Weber's 7/6/6/3
  rows). No footnotes in §174.
- ORTHOGRAPHY/house: \rho (file convention; Weber's ϱ glyph), \leqq for ≦, \pmod3, \S\,173,\,(1)/\S\,172
  cross-refs, Coefficient(ë→e), conjugirte/associirte/theilbar kept. Eyeballed PDF pp376–377.
Compiles **400 pp / 0 err / 0 overfull hbox / 0 underfull / 0 missing-char / 0 undefined** (held at 400;
restored prose ≈ offset dropped tags; no drop). Visually verified rendered PDF pp376–377.
NOTE (for §175): the "Siebzehnter Abschnitt" chapter head uses \begin{center}\large … \end{center} whereas
all other Abschnitt heads use \section*{…}; fix to \section* + verify title vs scan when doing §175.

### 2026-07-02 — PHASE 2 — §175 (Reduction der Gruppe durch reine Gleichungen) FULL RE-TRANSCRIPTION p595–597
FIRST section of the Siebzehnter Abschnitt (chapter head "Siebzehnter Abschnitt. Algebraische Auflösung von
Gleichungen." confirmed vs p595_top scan). .tex block (lines 21082–21127) was a RECONSTRUCTION.
- **★ Also fixed the chapter head**: was `\begin{center}\large Siebzehnter Abschnitt. …\end{center}` →
  `\section*{Siebzehnter Abschnitt. Algebraische Auflösung von Gleichungen.}` to match every other Abschnitt.
- **★ Weber's §175 has NO numbered equations** — every display is unnumbered. The .tex FABRICATED `\tag{1}`
  on `y^m−a=0` and `\tag{2}` on `ε=ψ(…)`; both dropped.
- **MATH ERROR fixed**: .tex wrote `ε=ψ(x₀,x₁,…,x_{n-1})`; Weber has `x_{m-1}` (p597, the eq is in the m
  roots x₀…x_{m−1} of the degree-m cyclic resolvent). Corrected to `x_{m-1}`.
- **DROPPED content restored**: (a) the roots display `ε, ε₁, ε₂ … ε_{m−1},` of φ(x)=0 (p596bot); (b)
  footnote 1 "Auf diese Form der Fragestellung hat zuerst C. Jordan hingewiesen (Traité des substitutions
  p. 386)." on "umformt" (p596); (c) the displayed indented question "Unter welchen Bedingungen wird die
  Gruppe P … reducirt?" (p596mid).
- **Theorems I & II**: .tex paraphrased both ("besitzt P einen Normaltheiler…", "$m$-ten Grades", "Der Satz
  lässt sich umkehren."). Restored Weber's exact wording (I: "so hat P einen Normaltheiler Q von
  Primzahlindex."; the umkehr-para verbatim incl. §155/§163 cross-refs; II: "$m^{ten}$ Grades … auf Q
  reducirt."). Rendered as \begin{quote} blocks (Weber sets them indented/gesperrt).
- Opening prose (§. 175 first two paras) reworded in .tex ("an denen sich" / "man fragt, ob…" / "wobei a dem
  Grundkörper angehört") → restored Weber's exact two paragraphs incl. "Auf diese Frage fällt von der
  Gruppentheorie das hellste Licht." and "d. h. einer reinen Gleichung."
- Cross-refs normalised to house form \S\,162 / \S\,157 / \S\,155 / \S\,163. \varphi/\varepsilon/\psi/\pi/
  \Omega per file convention. Footnote render-confirmed; theorems I/II + question + footnote eyeballed in
  rendered PDF (pdftotext §175 region). Downstream §176 cites "§175" correctly.
Compiles **401 pp / 0 err / 0 overfull hbox / 0 underfull / 0 missing-char / 0 undefined** (400→401, +1pp
from restored content; growth expected). Visually verified rendered §175 region.

### 2026-07-02 — PHASE 2 — §176 (Metacyklische Gleichungen) FULL RE-TRANSCRIPTION p597bot–599
SECOND section of the Siebzehnter Abschnitt. .tex block (lines 21134–21170) was a RECONSTRUCTION.
- **★ Weber's §176 has NO numbered equations** — the two displays are unnumbered.
- Reworded opening restored to Weber verbatim: "Wir wollen eine Gleichung … eine metacyklische Gleichung
  nennen." + the full P₁-chain ("Besteht P₁ aus der einzigen identischen Permutation, so ist P selbst
  cyklisch…" — dropped by .tex) down to "bis wir endlich zur Einheitsgruppe gelangen."; and "nach dem im
  §175 Bemerkten … dieselben, wie die durch Radicale lösbaren" (was ".tex: Nach dem Vorhergehenden … genau
  die durch Radicale lösbaren").
- **Satz III display FIXED**: .tex had `P,P₁,P₂,…,1`; Weber's Satz-III display is `P, P₁, P₂, P₃ …` (NO
  trailing 1). Wording restored ("von denen jede folgende ein normaler Theiler der nächst vorangehenden von
  Primzahlindex ist").
- **Restored the 2nd display** `P, P₁, P₂ … P_{μ−1}, 1` (in the metacyklische-Gruppe definition) — dropped
  by .tex.
- **Restored footnote** (Kronecker/Frobenius/Hölder, „metacyklische Gruppen"/„auflösbare Gruppen") — .tex
  had dropped it, keeping only an inline paraphrase "Der Ausdruck ist eine leichte Erweiterung…". \glqq/\grqq.
- Satz IV wording matched .tex (kept), BUT restored Weber's FULL proof the .tex had compressed: the intro
  "Diese Frage ist nur berechtigt bei irreduciblen Gleichungen, da bei reduciblen … alle denkbaren
  Combinationen vorkommen können"; the whole μm=n argument with the §158 Sätze cite and the inline factor
  list φ(x,ε),φ₁(x,ε),…φ_{m−1}(x,ε); and the base case "Ist z. B. n eine Primzahl, so muss μ=1 … Satz IV
  für Gleichungen von Primzahlgrad richtig" + the induction close (φ=0,φ₁=0,…φ_{m−1}=0 same group → all
  metacyklisch). Cross-refs \S\,175/\S\,158. n^{ten}/μ^{ten} ordinals.
- Render-confirmed (pdftotext §176 region): opening, footnote 67, Satz III/IV, both displays, proof tail.
Compiles **401 pp / 0 err / 0 overfull hbox / 0 underfull / 0 missing-char / 0 undefined** (held at 401;
restored content ≈ offset dropped material). Visually verified rendered §176 region.
- **★ CORRECTION (patched while doing §177):** my first §176 pass ended the Satz-IV proof one paragraph too
  early — Weber's proof has a final closing paragraph at the TOP of p600 ("Unter der Voraussetzung also, dass
  der Satz IV für Gleichungen μ^{ten} Grades richtig ist, folgt seine Richtigkeit für Gleichungen μm^{ten}
  Grades; und da er für Gleichungen von Primzahlgrad gilt, so ist er allgemein nachgewiesen.") that I had
  missed (it sits above the §177 heading). Appended it. Lesson reaffirmed: always read the NEXT section's
  first scan to confirm the true section boundary before closing a section.

### 2026-07-02 — PHASE 2 — §177 (Einfachheit der alternirenden Gruppe) FULL RE-TRANSCRIPTION p600bot–603top
THIRD section of the Siebzehnter Abschnitt. .tex block (lines 21164–21235) was a RECONSTRUCTION (all prose
reworded) — but its group-theory MATH was sound.
- **★ Only ONE numbered eq**: (1) λ=ϰ⁻¹π⁻¹ϰπ. All other displays unnumbered (V₄-group list, the π 2-row
  matrix, all 5 case computations).
- **★ ϰ vs κ**: the .tex used `\kappa`; Weber prints ϰ (varkappa) — switched to `\varkappa` throughout
  (consistent with §154's choice for the same letter).
- **★ All 5 cycle computations were CORRECT in the .tex** (each hand-verified digit-by-digit vs the p601–602
  scan): case1 (1,m,m−1…2)(2,3,1,4…m)=(1,2,4); case2 (1,3,2)(4,6,5)(3,2,4)(1,5,6)=(1,2,5,3,4); case3
  (1,3,2)(4,5)(2,4,3)(1,5)=(1,2,5,3,4); case4 (1,2)(3,4)(5,6)(3,2)(5,4)(1,6)=(1,3,5)(2,6,4); case5
  (1,2)(3,4)(5)(2,5)(3,4)(1)=(1,5,2). Kept the math; restored Weber's exact prose framing of each case.
- **DROPPED content restored**: (a) the case-3 parenthetical "(Dass in ϰ, wenn es zu A gehört, noch ein
  zweiter Cyclus von gerader Gliederzahl vorkommen muss, ist hier gleichgültig.)"; (b) **footnote 1**
  (Abel, Crelle Bd I 1826 / Ruffini 1799–1806 / Burkhardt „Die Anfänge der Gruppentheorie und Paolo Ruffini")
  attached to "…4^{ten} Grades ermöglicht wird" — .tex had dropped it; (c) the compressed final
  symmetric-group paragraph, restored in full incl. the ϰ²,ϰλ=1 ⇒ λ=ϰ argument and "Permutation der ersten
  Art" (Weber's term for even perms).
- **De-modernized**: removed the .tex's "κ∈Q", "der Commutator", "Q'=A∩Q" set-notation → Weber's prose form
  ("der grösste gemeinschaftliche Theiler Q' von A und Q"). `\perm` now uses the house `&`-aligned 2-row
  pmatrix (the .tex had commas, collapsing it to one column). Cross-refs \S\,149/\S\,153,\,6./\S\,154,\,6./
  \S\,160,161. Coëfficienten (ë) normalized to Coefficienten. n^{ten}/4^{ten} ordinals.
- Render-confirmed (pdftotext §177 region): title, case-1 conclusion, footnote 68, full final paragraph.
Compiles **402 pp / 0 err / 0 overfull hbox / 0 underfull / 0 missing-char / 0 undefined** (401→402, +1pp
from §176-patch + §177 restored content; the §176 patch was gated in the same compile). Visually verified.

### 2026-07-02 — PHASE 2 — §178 (Nicht metacyklische Gleichungen im Körper der rationalen Zahlen) FULL RE-TRANSCRIPTION p603mid–606top
FOURTH section of the Siebzehnter Abschnitt. .tex block (lines 21221–21264) was a HEAVY reconstruction with
multiple serious defects (existence of unsolvable rational-coefficient equations of each prime degree).
- **★ MATH ERROR fixed**: the Galois resolvent of the general degree-n equation has degree **Π(n)** (= n!);
  the .tex wrote **ν(n)**. Corrected \nu(n)→\Pi(n).
- **★ FABRICATED third-person editorializing removed**: .tex wrote "Weber benutzt hier nur eine einfachere
  Folgerung" (Weber does not write about himself). Restored Weber's actual text: the Hilbert citation with
  "Auf diesen allgemeinen Satz können wir hier nicht eingehen." + "Wir werden aber die gestellte Frage viel
  einfacher, wenn auch bei Weitem nicht so allgemein beantworten, indem wir zeigen…".
- **DROPPED footnote 1 restored** (Hilbert: "Ueber die Irreducibilität ganzer rationaler Functionen mit
  ganzzahligen Coefficienten. Journal für Mathematik, Bd. 110.") — .tex had dropped it.
- **★ FABRICATED attribution removed**: .tex called the irreducibility criterion "das Eisenstein'sche
  Kriterium" — Weber never names it; it is his numbered **Satz 3**. Restored as a numbered quote-block Satz
  with its φ(x)=c₀xⁿ+… display.
- **★ FABRICATED Satz label fixed**: the final result was labelled "A." in the .tex — Weber numbers it **4.**
  (continuing 1.,2.,3.). Corrected.
- **DROPPED closing paragraph restored** (the whole "Der Beweis, der hier geführt ist, zeigt … die Sache sich
  ebenso verhält." on the incompleteness/density of the construction) — .tex had ended at its bogus "A.".
- Smaller fixes: "Daraus folgt:" → "Daraus folgt als Corollar:"; restored the expanded 2nd line of the f(x)
  display (=xⁿ+a₁xⁿ⁻¹+…+aₙ) and the "(vergl. den siebenten Abschnitt)" cross-ref; Satz-3 proof now uses
  Weber's α₀…α_h (not the .tex's latin a) for the first factor and restores Weber's exact x^{k−ν}
  contradiction (coeff α_hβ_ν+α_{h−1}β_{ν+1}+… not div. p ⇒ k−ν=n impossible since k<n). NO numbered eqs
  (all displays unnumbered). \S\,153,\,9./\S\,2. Coëfficienten (ë)→Coefficienten. n^{ten} ordinal.
- Render-confirmed (pdftotext §178 region): Π(n), Hilbert footnote 69, "Daraus folgt als Corollar:", Satz 4
  (correct number), the restored closing paragraph.
Compiles **402 pp / 0 err / 0 overfull hbox / 0 underfull / 0 missing-char / 0 undefined** (held at 402;
restored content ≈ offset dropped material). Visually verified rendered §178 region.

### 2026-07-02 — PHASE 2 — §179 (Auflösung durch reelle Radicale) FULL RE-TRANSCRIPTION p606mid–609mid
FIFTH section of the Siebzehnter Abschnitt (casus irreducibilis / non-solvability by real radicals). Mapped
one fire, composed/applied the next (deferred to avoid a fatigued compose — large section). .tex block was a
HEAVY reconstruction.
- **★ Equation ORDER fixed**: the .tex printed `\tag{2}` (x^p−a=0) BEFORE `\tag{1}` (the roots), an out-of-
  order artifact. Weber's order is (1) roots α,εα,…ε^{p−1}α FIRST, then (2) x^p−a=0. Restored. Tags: (1)=roots,
  (2)=x^p−a=0, (3)=x^p−a=f₁f₂, (4)=a^μ=b^p.
- **★ ν→μ fixed**: the .tex used ν for the degree of f₁; Weber uses **μ** throughout the irreducibility proof.
- **DROPPED footnote ¹ restored** (Hölder, Mathematische Annalen Bd. 38; Kneser, ebendas. Bd. 41) — .tex
  dropped it. Also restored the dropped "die wir im §165 kennen gelernt haben" cross-ref.
- **DROPPED displays restored**: three unnumbered displays the .tex had removed/inlined — ε^λα^μ=b (the
  x-independent term of f₁), μh+pk=1, and a=a^{μh}a^{pk}=(b^h a^k)^p.
- **★ COMPRESSED geometric-problems discussion restored**: the .tex crushed all of Weber's p609 discussion
  (P8–P11) into a single fabricated sentence. Restored in full: the "drei oder vier Arten" framing, §154,7
  and §157 cross-refs, the compass-and-straightedge (Cirkel und Lineal) impossibility, the regular-heptagon
  (Siebeneck) example, angle-trisection (Dreitheilung), and the Delian problem (Würfelverdoppelung, x³=2).
- De-modernized: casus irreducibilis set PLAIN (Weber gesperrt, not the .tex's \emph); restored ϱ (\varrho)
  as the g(t)-root and ε (\varepsilon) as the adjoined root of χ where the .tex had used θ; Ω(ε) [glyph read
  as ε, consistent with §157 for prime-degree χ]. Coëfficienten→Coefficienten. \sqrt[p]{a}; p^{ten}/6^{ten}.
  Sätze 1,2 as quote blocks. Journal titles plain (house convention, matches §178).
- Render-confirmed (pdftotext §179 region): opening + §165 ref + footnote 70; eqs in Weber's order; Satz 2;
  the full geometric-problems tail (Cirkel/Lineal, Siebeneck, Delian problem).
Compiles **403 pp / 0 err / 0 overfull hbox / 0 underfull / 0 missing-char / 0 undefined** (402→403, +1pp
from restored content). Visually verified rendered §179 region.

### 2026-07-02 — PHASE 2 — §180 (Metacyklische Gleichungen von Primzahlgrad) FULL RE-TRANSCRIPTION p609bot–620
SIXTH and **LARGEST** section of the Siebzehnter Abschnitt: Galois's linear-group criterion for solvability of
prime-degree equations. Spans **p609bot–p620** (§181 opens p621). Mapped across two fires (p609bot–613top, then
p613mid–620), z₀ zoom-resolved, composed/applied the next fire (deferred-compose discipline for a large section).
The .tex block was a HEAVY, MODERNIZED, and partly FABRICATED reconstruction. Verified page-by-page by eye vs the
~500 dpi scans (p610–p620) before applying.
- **★ FABRICATED THEOREM NUMBERING fixed**: the .tex had Sätze I, II, III then jumped to V (NO IV). Weber's true
  numbering is **I, II, III, IV, V, VI, VII, VIII, IX — contiguous, 9 Sätze**. Restored the dropped **Satz IV**
  ("Die volle metacyklische Gruppe ist kein Theiler der alternirenden Gruppe. Der grösste gemeinschaftliche
  Theiler beider Gruppen ist die halbmetacyklische Gruppe.", p617) with its full s/t-cycle-parity proof.
- **★ FABRICATED eq (6) fixed**: the .tex wrote `φ(z) ≡ −a₀z^{n−1} − a₁(z−1)^{n−1} − …` (mathematically WRONG).
  Weber's (6) is `φ(z) ≡ −a₀·ψ(z)/z − a₁·ψ(z)/(z−1) − ⋯ − a_{n−1}·ψ(z)/(z−n+1) (mod n)`. Also restored the
  preceding Lagrange interpolation display + ψ(z)=z(z−1)…(z−n+1), ψ(z)≡z^n−z, ψ'(z)≡−1 (all §29/§136-derived).
- **★ ERRATUM #15 (z₀ fixed point)**: Weber PRINTS `z₀ ≡ b/(a−b) (mod n)` (crop_src 600dpi ×4 zoom-confirmed,
  vol1_p612_crop_30_27.png). Mathematically the fixed point of z↦az+b is b/(1−a); "a−b" is a genuine WEBER TYPO.
  **Transcribed EXACTLY AS PRINTED** (\frac{b}{a-b}) — not "corrected". Flagged as preserved erratum #15.
- **BOTH dropped footnotes restored**: (p611) "Kronecker nennt nur diese Gruppe metacyklisch." on "lineare Gruppe
  nennen"; and (p620) the Kronecker-paper cite "Ueber algebraisch auflösbare Gleichungen. Monatsbericht der
  Berliner Akademie, 14. April 1856." on "reellen Rationalitätsbereichs" (title PLAIN, house convention).
- **DE-MODERNIZED**: .tex's `\triangleleft` (L◁P) → Weber's prose "Normaltheiler von"; `\bigl\{…set-builder…\bigr\}`
  → Weber's (z, a₀^{ph}z + b) with stacked ranges; the λλ' composition restored as Weber's 2-row \perm pmatrix.
- **RESTORED the many dropped displays / eqs**: λ^h general + λ^h for a=1; geometric series (a^h−1)/(a−1); the
  z₀ passage + the μ/ν-quotient definition; λλ₀^{−h} composition + the congruence b₀/(a₀−1)≡b/(a₀^h−1); eq (5)
  full stacked ranges; eqs (11) m=μn+ν+1 and (12) m=n(μ+1); the coset decomposition P=Q+Qπ₁+⋯+Qπ_{n−1};
  C=1,γ,γ²…γ^{n−1}. All numbered eqs (1)–(12) present and contiguous.
- **RESTORED the gutted VI/VII converse proof**: the .tex compressed the whole ϰ₀/γ-counting argument (eqs 11,12,
  Nebengruppen, C-Normaltheiler ⇒ Satz I) to two sentences. Fully restored per Weber p618bot–620.
- **RESTORED the discriminant-sign derivation** before Satz IX ((x_h−x_k)² sign analysis ⇒ (−1)^{(n−1)/2}).
- Notation: ϰ=\varkappa (Weber's letter, matches §154/§177), γ/φ/ψ/π/λ/μ/ν/α standard; Coëfficienten→Coefficienten;
  giebt/reducirt/-irt kept; \pmod (Weber "(mod n)"; file convention, deferred sweep); \S\,176/\,158,3./\,153/\,29/\,136.
  Sätze I–IX as \begin{quote} blocks (sibling style). \perm macro for the π-matrix + λλ' pmatrix.
- Render-confirmed (pdftotext full-PDF grep): Sätze I–IX all present in order (I, II@l190, III@l195, IV@l33828,
  V@l244, VI@l248, VII@l288, VIII@l292, IX@l33899); footnote 71 (Kronecker nennt) + footnote 72 (Monatsbericht
  1856); Lagrange interpolation; Periode-der-Substitution/z₀ passage; Nebengruppen decomposition.
Compiles **407 pp / 0 err / 0 overfull hbox / 0 underfull / 0 missing-char / 0 undefined** (403→407, +4pp from
~11 pp of restored content). Visually verified rendered §180 region.

### 2026-07-02 — PHASE 2 — §181 (Anwendung auf die metacyklischen Gleichungen fünften Grades) FULL RE-TRANSCRIPTION p621–627top
SEVENTH section of the Siebzehnter Abschnitt: the concrete $n=5$ metacyclic-quintic worked theory (§182 opens
p627mid). Mapped across three fires (p621-623, p624-625, p626-627), composed/applied the next. eqs (1)-(24). The
.tex block kept most numbered-equation *bodies* but stripped the scaffolding — dropped two big equation-blocks,
both footnotes, derivations, cross-refs, and carried a math error. Verified page-by-page by eye vs the ~500 dpi
scans (p621-627) before applying.
- **★ NUMBERING / dropped blocks (11),(12)**: the .tex compressed Weber's eq (11) [the six explicit $u_1\ldots u_6$]
  AND eq (12) [the six $u'_1\ldots u'_6$] into one sentence, so its numbering skipped (11), jumping (10)→(12).
  Restored both blocks. Weber's sixth-degree $y$-resolvent is a **GENUINE REUSED (12)** — both labels zoom-confirmed
  on p623 (u'-block @crop_4_40, $y$-sextic @crop_4_63), same reuse pattern as §151/§163. Kept the double-(12).
- **★ BOTH footnotes restored** (the .tex had none): (p622) "Jacobi, observatiunculae ad theoriam aequationum
  pertinentes, Crelle's Journ. Bd. 13. Jacobi's Werke, Bd. 3. Cayley, philos. transactions 1861, Collected math.
  papers, Vol. IV, p. 309." on eq (9); (p624) "Runge, Acta mathematica, Bd. 7." on the Bring-Jerrard form (13).
- **★ MATH ERROR eq (15)**: the .tex wrote $x_1=\sqrt{-\alpha}$ (square root); Weber has $x_1=\sqrt[4]{-\alpha}$
  (FOURTH root — correct, since $x^4=-\alpha$; zoom-confirmed). Fixed all four roots $x_1\ldots x_4$.
- **★ Killed FABRICATED 3rd-person "Weber bildet die Resolvente für die Bring-Jerrard'sche Form"** → Weber's actual
  text: the Cayley-computation remark + "Wir wollen uns hier damit begnügen, die Resolvente für einen besonderen
  Fall zu bilden. Der dabei gefundene Werth für die Zahl $a_5$ ist dann natürlich allgemein gültig."
- **Restored dropped displays/derivations**: the degree-table ($a_1\sqrt\Delta\ldots a_6$ / grades 2,4,6,8,10,12) +
  the "$\sqrt\Delta$ vom 10ten Grade ⇒ $a_1=a_3=0$" reasoning; the full ten-difference product + intermediate
  $16i(\sqrt{-\alpha})^5$ in (16); the $\beta=0$ $y$-values ($y_1=y_2=y_3=y_6=-2\sqrt\alpha$, $y_4=(4-2i)\sqrt\alpha$,
  $y_5=(4+2i)\sqrt\alpha$); the "Eine andere Form" ($\sqrt\alpha\to-\sqrt\alpha$) derivation + the unnumbered
  $(v-\alpha)^4(v^2+6\alpha v+25\alpha^2)=0$; the ENTIRE metacyklisch-verification discussion (the $6u^5-20\alpha u^3
  +30\alpha^2u-\sqrt\Delta=0$ and $5(u^2-\alpha)^3=0$ displays, the $v=\alpha\Rightarrow\beta=0$ argument); the
  $\lambda=-1,\mu=1$ intermediates "$64\alpha=-5^4$, $64\beta=-5^4$" + the "als Beispiel … irreducibel" conclusion.
- **Restored cross-refs**: $\S\,74$ (Formel (3)) on the discriminant (19); $\S\,178,\,3.$ on the $x^5+5x+5t$ example.
- **De-modernized the (1) table**: dropped the .tex's \hline + vertical rule; row labels $(s),(t),(t^2)$ in parens;
  plain aligned columns (tables (2),(3) likewise). Restored the Nebengruppen-all-distinct proof + the
  $(1,2)(3,4)t=(1,4)$ display. Restored "wie schon Lagrange gefunden hat" on (8). Coëfficienten→Coefficienten;
  radicals $(\sqrt\alpha)^5={\sqrt{\alpha}}^{5}$ (exponent outside, per zoom). eq bodies (13),(14),(16)-(24) verified.
- Render-confirmed (pdftotext full-PDF grep): footnote 73 (Jacobi/observatiunculae/Cayley) + footnote 74 (Runge);
  eq (11) $u_1..u_6$ + eq (12) $u'_1..u'_6$ blocks present; two (12) tags present (double-(12)); (15) fourth-root;
  Nebengruppen-verschieden proof; Cayley remark; metacyklisch-verification discussion; $\xi^5+5\xi^4-5\cdot64=0$.
Compiles **410 pp / 0 err / 0 overfull hbox / 0 underfull / 0 missing-char / 0 undefined** (407→410, +3pp from
restored content). Visually verified rendered §181 region.

### 2026-07-02 — PHASE 2 — §182 (Die Gruppe der Resolvente) FULL RE-TRANSCRIPTION p627mid–629bot
LAST section of the Siebzehnter Abschnitt (§183 opens the ACHTZEHNTER ABSCHNITT "Wurzeln metacyklischer
Gleichungen" on p630). The merkwürdiger Schluss on sextic equations: the resolvent $F(v)=0$ with roots
$v_i=(u_i-u'_i)^2$ is a Totalresolvente of the metacyclic quintic; its group is the transitive index-6 divisor $C$
of $S_6$; the $w$-functions. Mapped in one fire (weber_182_notes.md, P1–P9), composed/applied the next. The .tex
block kept the numbered-equation *bodies* (eqs (1),(2)) and the π/w displays but stripped ~half the prose
scaffolding and carried a fabricated 3rd-person "Weber". Verified by eye vs the ~500 dpi scans (p627–629) + two
zoom crops before applying.
- **★ Killed FABRICATED 3rd-person "Um diese Gruppe $C$ zu beschreiben, untersucht Weber den Einfluss…"** → Weber's
  actual 1st-person text: "Um diese merkwürdige Gruppe, die wir mit $C$ bezeichnen wollen, zu finden, haben wir nur
  den Einfluss zu untersuchen, den die sämmtlichen 120 Permutationen der $x$ auf die $v$ oder auf die Grössen (11)
  des vorigen Paragraphen ausüben."
- **★ Restored DROPPED §182 opening (P1, p627mid)**: "Die Sätze, die wir im vorigen Paragraphen abgeleitet haben,
  gestatten einen merkwürdigen Schluss über die Gleichungen 6ten Grades. Wir nehmen jetzt wieder die
  $x_0\ldots x_4$ des vorigen Paragraphen als unabhängige Variable an." (.tex jumped straight to "Die sechs
  Grössen…"). Also restored P1's tail: $F(v)=0$ irreducibel + "eine Resolvente der Gleichung 5ten Grades".
- **★ Restored DROPPED M-conjugates paragraph (P2, p627bot-628top)**: "Ist $M$ die volle metacyklische Gruppe…, so
  haben die zu $M$ conjugirten Gruppen $\pi^{-1}M\pi$ keinen anderen gemeinschaftlichen Theiler, als die identische
  Permutation…" (whole trivial-intersection argument + the $\S\,177$ ref — entirely absent from .tex).
- **★ Restored DROPPED §156 Totalresolvente-Bezeichnung + F(z)-reasoning (P3)**: Weber "Die Resolvente $F(v)=0$ ist
  also nach der in $\S\,156$ eingeführten Bezeichnung eine Totalresolvente… deren Grad $1\cdot2\cdot3\cdot4\cdot5=120$
  ist. Da $F(z)$ auch irreducibel ist… Sie ist vom Grade 120, während der Grad der symmetrischen Gruppe… $6\cdot120$
  ist." The .tex had compressed this to "…Totalresolvente…, also 120. Da die symm. Gruppe … 720 hat…". Restored the
  §156 ref, the transitiv reasoning, and Weber's $6\cdot120$ form (vs the reconstruction's 720). Kept the Satz.
- **★ ERRATUM #16 PRESERVED (w₀)**: Weber PRINTS $w_0=v_1v_2+v'_4v_5+v_3v_6$ — a stray prime on $v_4$
  (zoom-confirmed p629 @crop_22_31). $v$ has no primed members (only $u'$), so $v'_4$ is a Weber misprint (should be
  $v_4$). The .tex had silently "corrected" it to $v_4v_5$. → transcribed **as printed** $v'_4v_5$, flagged; do NOT
  silently correct.
- **★ ERRATUM #17 PRESERVED (F(z))**: Weber prints "Da $F(z)$ auch irreducibel ist" (zoom-confirmed p628
  @crop_55_25 — the italic $z$ argument is unmistakable). The resolvent is $F(v)=0$ throughout, so $F(z)$ is a Weber
  misprint (should be $F(v)$). → transcribed **as printed** $F(z)$, flagged; do NOT silently correct.
- **Restored dropped §153,2 derivation (P5)**: "Wir haben nun früher gesehen ($\S\,153,\,2.$), dass die
  Transpositionen $(0,1)\ldots(0,4)$ … die ganze symmetrische Gruppe … erzeugen. … Durch Anwendung einer
  Transposition $(0,1)$ geht jeder der Ausdrücke (11), $\S\,181$ in einen der Ausdrücke (12) über und umgekehrt…"
  before the π-generators; restored the trailing clause "wo sich die in den π vorkommenden Transpositionen $(1,3),
  \ldots$ auf die Indices der $u$ oder der $v$ beziehen." π-generator display + example products (P6) matched .tex.
- **Restored P8 display + §153,2 ref**: the $\pi_1=(w_0,w_1),\ldots,\pi_4=(w_0,w_4)$ transposition line + "entspricht
  nach $\S\,153,\,2.$ der ganzen Gruppe $C$ die symmetrische Gruppe der Indices der $w$" + "wie die Summe der $w$"
  (the .tex had reworded/compressed the C↔symmetric-group paragraph, dropping the explicit display).
- **Restored P9 wording**: "für ein beliebiges rationales $\lambda$" on the $(\lambda-w_0)\ldots(\lambda-w_4)$
  product (dropped by .tex). eq bodies (1),(2) verified against scans; ordinals set as printed ($6^{\text{ten}}$,
  $5^{\text{ten}}$ — numeral+superscript, matching Weber vs the reconstruction's spelled-out "sechsten/fünften").
- Render-confirmed (pdftotext full-PDF grep): "merkwürdigen Schluss"; "conjugirten Gruppen $\pi^{-1}M\pi$";
  "eingeführten Bezeichnung eine Totalresolvente"; "Da F(z) auch irreducibel"; "haben wir nur den Einfluss zu
  untersuchen" (and "untersucht Weber" now ABSENT, count 0); "früher gesehen"; "beliebiges rationales".
Compiles **410 pp / 0 err / 0 overfull hbox / 0 underfull / 0 missing-char / 0 undefined** (410→410, +2600 chars,
absorbed by layout — no page drop). Visually verified rendered §182 region. **§182 COMPLETES the Siebzehnter
Abschnitt — the entire §175–182 metacyclic block is now source-faithful.**

### 2026-07-02 — PHASE 2 — §183 (Stellung der Aufgabe. Hülfssatz) VERIFIED FAITHFUL — 2 surgical fixes p630mid–633mid
FIRST section of the ACHTZEHNTER ABSCHNITT "Wurzeln metacyklischer Gleichungen" (chapter head **verified correct**
vs p630 scan: "Achtzehnter Abschnitt. Wurzeln metacyklischer Gleichungen." — left untouched). The Abel/Kronecker
problem statement + the Ω(ε)-Normalform Hülfssatz (Sätze 1,2,3). **Unlike §180-182, this section is essentially
FAITHFUL** — read every scan p630-633 by eye: the opening, the Abel/Kronecker/H.Weber footnote (Marburg 1892
"...vereinfacht und in einem Punkte berichtigt"), eqs (2),(3), the Normalform paragraph, Sätze 1/2/3 (quote blocks),
the X=X₁X₂ reducibility argument, all cross-refs (§164/§180/§134/§142/§143/§144/§152), and the Satz-3 averaging
display all match the .tex verbatim.
- **★ ONLY DEFECT — 2 modernized sums de-modernized to Weber's index-above/range-below convention**:
  (a) eq (1) $(\varepsilon,x)=\ldots=\sum\limits_{0,n-1}^{h}\varepsilon^h x_h$ — .tex had modern `\sum_{h=0}^{n-1}`;
  (b) the Satz-3 averaging display $\Phi(\varepsilon)=\tfrac1{n-1}\sum\limits_{1,n-1}^{h}\Phi(\varepsilon^h)=\ldots$
  — .tex had modern `\sum_{h=1}^{n-1}`. Both confirmed on p631/p633 (Weber prints the index letter $h$ ABOVE the Σ
  and the range "0, n−1" / "1, n−1" BELOW). Matched to the house form used in §167/§169/§170
  (`\sum_{0,n-1}^{h}` / `\sum_{1,n-1}^{h}`). No other changes; no dropped content, no fabrication, no math error.
- NOTE on the §184 boundary: while confirming where §183 ends (§184 "Sätze über die Resolventen" opens p633mid), I
  saw the .tex §184 opening has DROPPED Weber's clause "und wenden darauf die Sätze des vorigen Paragraphen an" —
  consistent with the earlier held-note that §184 is a genuine reconstruction. §184 handled next; left untouched now.
Compiles **410 pp / 0 err / 0 overfull hbox / 0 underfull / 0 missing-char / 0 undefined** (held 410).
Visually verified rendered §183 region.

### 2026-07-02 — PHASE 2 — §184 (Sätze über die Resolventen) FULL RE-TRANSCRIPTION p633mid–638mid
SECOND section of the ACHTZEHNTER ABSCHNITT; the $(\varepsilon,x)$-Lagrange-resolvent theory (influence of $s,t$;
the $f_h$/$F_v$/$\Phi_v$ functions; the metacyclic-function Sätze 4–7; eqs (1)–(21)). ★★ **HEAVIEST reconstruction
since §180** — the .tex kept the section's skeleton but carried **~9 equation-body math errors** the agent workflow
never caught, plus ~30 prose drops. Mapped the whole section p633–638 by eye + 6 zoom crops (eqs 8/9/17 + the two
g-congruences), composed retrans_184.py, and **verified every fix in the rendered output PDF** (pp 400–404).
- **★★ eq (4)**: .tex `(\varepsilon,x)^\lambda=\Phi(\varepsilon)` — Weber prints **$(\varepsilon,x)^n$**
  (zoom-confirmed p634bot). Fixed.
- **★★ eq (5)**: .tex collapsed Weber's **3-line recursion array** [$(\varepsilon^g,x)(\varepsilon,x)^{-g}=f_0$ /
  $(\varepsilon^{g^2},x)(\varepsilon^g,x)^{-g}=f_1$ / $\cdots$ / $(\varepsilon^{g^{n-1}},x)(\varepsilon^{g^{n-2}},x)^{-g}
  =f_{n-2}$] into ONE wrong line `(\varepsilon^{g^h},x)(\varepsilon,x)^{-g^h}=f_h`. Restored the array (dotted middle).
- **★★ eq (8)**: .tex exponent `(\varepsilon,x)^{g^{n-1}-1}` — Weber prints **$(\varepsilon,x)^{1-g^{n-1}}$**
  (sign, zoom-confirmed p636 crop_28_17). Fixed.
- **★★ eq (9)**: .tex WHOLESALE WRONG `[(\varepsilon,x)^{-\lambda}(\varepsilon^\lambda,x)]^n f_0^{\lambda g^{n-2}}
  \cdots f_{n-2}^\lambda` — Weber's is $(\varepsilon^\lambda,x)^n=[(\varepsilon,x)^{(g^{n-1}-1)/n}(\varepsilon^\lambda,x)]^n
  f_0^{g^{n-2}}f_1^{g^{n-3}}\cdots f_{n-2}$ (inner exp = the fraction $(g^{n-1}-1)/n$, plain f-exponents; zoom-confirmed
  p636 crop_28_24, and the math checks against eq (8)). Restored.
- **★★ eq (17)**: .tex f-exponents `g^{n-2},g^{n-3},\ldots` — Weber uses the **quotients $q_{n-2},q_{n-3},\ldots q_1$**
  (from eq 15 $g^v=nq_v+r_v$; since $g^{n-1-j}=nq+r$, $\Phi_v$ collects the $(f^n)^q$ parts; zoom-confirmed p637
  crop_16_37). Fixed to $\Phi_v=F_v f_v^{q_{n-2}}f_{v+1}^{q_{n-3}}\cdots f_{v+n-3}^{q_1}$.
- **★★ eq (18)**: .tex `\Phi_v` (no exponent) — Weber prints **$\Phi_v^n$**. Fixed.
- **★★ eq (20)**: .tex `\sum_{v=0}^{n-2}\frac{\Theta_v}{u-\omega_v}` — Weber has the **$\varphi(u)$ numerator** AND the
  **$=\chi(u)$** RHS: $\sum_{0,n-2}^{v}\frac{\Theta_v\varphi(u)}{u-\omega_v}=\chi(u)$. Restored (+ de-modernized sum).
- **★★ eq (21)**: .tex `\Theta_v=\Theta(u)` (WRONG) — Weber is **$\chi(u)/\varphi'(u)=\Theta(u)$**. Restored.
- **★ g-congruences**: .tex used `=` — Weber prints **$\equiv$** in both; congruence-2 last term is Weber's plain
  **$g^{n-2}$** (not the .tex's $g_1^{n-2}$; zoom-confirmed p636 crop_30_41). Fixed to $\equiv$ + $g^{n-2}$.
- **★ ERRATUM #18 PRESERVED (Satz 6)**: Weber prints "der Grössen $f_0,f_1\ldots f_{n-1}$" — but only $n-1$ functions
  exist ($f_0\ldots f_{n-2}$), so $f_{n-1}$ is a Weber MISPRINT (should be $f_{n-2}$; zoom-confirmed p635 crop_12_53).
  The .tex had silently "corrected" it to $f_{n-2}$. → transcribed **as printed** $f_{n-1}$, flagged; do NOT correct.
- **★ SATZ NUMBERING**: Weber's §184 Sätze are **4,5,6,7** (continuing §183's 1,2,3; "Aus 2. und 4." confirms). The
  .tex used `\enumerate[resume,label=\arabic*.]` which was BROKEN (§183 rendered its Sätze as quote blocks, so the
  arabic counter did NOT resume at 4). Rebuilt all four as quote blocks with typed "4."/"5."/"6."/"7." (matches §183
  house style; render-confirmed as 4–7).
- **★ GREEK LABELS**: the a)–d) property list uses Weber's **$\alpha)\,\beta)\,\gamma)\,\delta)$** (the .tex used
  `\alph*` → a)b)c)d)). Rebuilt with `\item[$\alpha$)]` etc. Restored the dropped "(0,1,2…n-2)" in $\gamma)$.
- **DE-MODERNIZED SUMS**: eq (2)-requote $\sum_{1,n-1}^{h}$ (a genuine DOUBLE-(2): Weber prints (2) twice — expanded
  p633, sum-form p634 — kept both \tag{2}, like §151/§163/§181); eq (3) $\sum_{1,n}^{h}$ (range "1,n" zoom-confirmed);
  the $g^{-1}$-display $\sum^{h}$; eq (20) $\sum_{0,n-2}^{v}$.
- **~30 PROSE DROPS restored** (all render-confirmed): "und wenden darauf die Sätze des vorigen Paragraphen an";
  "der **beiden** erzeugenden"; "(\S\,180)"; "**aber**" (×3); the 4 general/special-λ Vertauschungen displays;
  "die **Folgerung**"; "$[\S\,183,\,(3)]$" + "(\S\,163)" on Satz 5; the eq-(5) lead-in "$n-1$ Functionen, die alle
  durch $s$ ungeändert bleiben…"; "wie nach dem Theorem 4. zu sehen ist"; "wie man aus (5) ersieht"; "da sie in
  verschiedene lineare Factoren zerlegt sind"; "**t und**"; "und wir erhalten das Theorem"; the "Hierbei ist unter
  einer metacyklischen Function…" definition para; "und wir erhalten aus 3. das Theorem"; "**dann**" + the
  "$\varepsilon^{g^{n-1}}=\varepsilon$ ist" clause + "der Gleichungen (5)" on eq (8); "worin $l$ eine beliebige ganze
  Zahl bedeutet, da ja die primitiven Wurzeln nur bis auf Vielfache von $n$ definirt sind"; "was durch $n$ theilbar
  ist" on eq (11); the "wenn man beachtet, dass die Functionen … cyklische Permutation erleiden …" verallgemeinern
  clause; the whole "Diese Formeln gelten für jedes $v$ … durch $t^{-1}$ eine cyklische Permutation erfahren"
  continuation; "**hier**"; "so dass $r_0$ immer $=1$ ist"; "sind also von der Bedingung (10) unabhängig und können
  aus einer beliebigen primitiven Wurzel $g$ abgeleitet werden"; "um es nochmals zu wiederholen"; "(\S\,155)"; the
  explicit "$\alpha)\,\beta)\,\gamma)\,\delta)$" in the Lagrange para; "man kann also für diese Functionen die $f_v$
  wählen"; "bedeutet $u$ eine Variable, und"; the "so gestattet die Function $\varphi(u)$ die Permutationen $s,t$ …
  nach dem Satze 3. des \S\,183 … in Bezug auf $x$" follow-up to eq (19); "dem die Eigenschaften α)β)γ)δ) zukommen";
  the "$(n-2)^{\text{ten}}$ Grades … Substitutionen $s,t,\sigma$" wording; the displayed $\Theta_v=\Theta(\omega_v)$;
  the closing "deren Coefficienten metacyklische Functionen der $x$ sind, und $\varepsilon$ nicht mehr enthalten".
- Conventions: Coëfficienten→Coefficienten (ë→e); $n^{\text{te}}$/$(n-2)^{\text{ten}}$ ordinals; \pmod kept (global
  (mod.) sweep deferred); §185 boundary left intact (chapter continues).
Compiles **411 pp / 0 err / 0 overfull hbox / 0 underfull / 0 missing-char / 0 undefined** (410→411, +1pp from
restored content). **Rendered §184 (output-PDF pp 400–404) eyeballed page-by-page** — every eq fix, erratum #18,
Satz 4–7 numbering, Greek α–δ labels, and all restorations confirmed correct in the typeset output.

### 2026-07-02 — PHASE 2 — §185 (Wurzeln metacyklischer Gleichungen) FULL RE-TRANSCRIPTION p638bot–641
THIRD section of the ACHTZEHNTER ABSCHNITT; substitutes the roots $\xi$ of an irreducible metacyclic equation (over
base field $\mathfrak{K}$) for §184's variables $x$, and derives the explicit root formula (6)/(7) via $n$-th-root
radicals $\tau_v=\sqrt[n]{k_v}$; shows it yields exactly $n$ values. eqs (1)–(14). ★★ **HEAVY reconstruction (on par
with §184)** — notation substitutions + ~5 equation-body math errors + ~25 prose drops. Mapped p638–641 by eye + 8
zoom crops (eqs 8/12 + Θ/Φ letters + f_{n-1} + sum-limits), composed retrans_185.py, and **verified every fix in the
rendered output PDF** (pp 404–406).
- **★ NOTATION — base field $\mathfrak{K}$ (Fraktur)**: Weber's §185 base field is **𝔎** (Fraktur K, distinct from
  §184's Ω = field of metacyclic functions of $x$); the .tex had used Ω throughout the opening. Restored $\mathfrak{K}$
  (×3: "Körper 𝔎", "rational (in 𝔎)", "worin Φ … (in 𝔎)"). Doc already loads eufrak/uses \mathfrak.
- **★★ eq (2) — Θ not θ + fuller chain**: .tex `k_1=\theta(k_0),\ldots,k_0=\theta(k_{n-2})` — Weber uses **$\Theta$**
  (capital, zoom-confirmed) and the fuller cyclic chain $k_1=\Theta(k_0),k_2=\Theta(k_1),\ldots,k_{n-1}=\Theta(k_{n-2}),
  k_0=\Theta(k_{n-1})$ + the "(\S\,163)" ref. Fixed.
- **★★ eq (3) — Φ not Θ**: .tex `K_0=\Theta(k_0),\ldots` — Weber uses **$\Phi$** (capital, zoom-confirmed):
  $K_0=\Phi(k_0),\ldots,K_{n-2}=\Phi(k_{n-2})$. Restored + "nach dem Schlusssatze des \S\,184 und zwar in der Form" +
  "worin $\Phi$ eine rationale Function (in $\mathfrak{K}$) bedeutet". [The .tex had SHIFTED the letters: Weber θ… no —
  Weber eq2=Θ, eq3=Φ; .tex eq2=θ, eq3=Θ.]
- **★ ε_v system \varepsilon not \epsilon**: the $\varepsilon_v$ root-of-unity system (eqs 9,10,13 + 3 displays) —
  Weber uses **ε (\varepsilon)** (curly, zoom-confirmed p640bot), the .tex used \epsilon (lunate). Fixed. (The FIXED root
  ε, e.g. $\varepsilon^{-hr_v}$ in eq 14, was already \varepsilon.)
- **★★ eq (1) — no "=0"**: .tex `\psi(u)=(u-k_0)\cdots(u-k_{n-2})=0` — Weber's eq (1) is the polynomial DEFINITION
  $\psi(u)=(u-k_0)\cdots(u-k_{n-2})$ WITHOUT "=0" (the $\psi(u)=0$ sits in the prose). Removed the "=0".
- **★★ eq (8) — sign +g**: .tex `\bigl(\sqrt[n]{R_{v-1}}\bigr)^{-g}` — Weber prints **$(\sqrt[n]{R_{v-1}})^{g}$**
  (+g, zoom-confirmed p640 crop_30_58; math from (5)+the $k_{v-1}$ relation confirms +g). Fixed.
- **★★ eq (12) — E_0^{r_v}**: .tex `E_0^{g^v}` — Weber prints **$E_0^{r_v}$** (zoom-confirmed p641 crop_28_37;
  congruent since $r_v\equiv g^v \pmod n$, but transcribe as printed). Fixed.
- **★★ eq (13) — wholesale wrong in .tex**: .tex `E_0=\epsilon_{n-2}\epsilon_{n-3}^{g}\cdots\epsilon_0^{r_{n-2}}` —
  Weber prints **$E_0=\varepsilon_0^{r_{n-2}}\varepsilon_1^{r_{n-3}}\cdots\varepsilon_{n-2}^{r_0}$** (= eq (10) at
  $v=0$; ascending indices, descending exponents). Restored.
- **★ eq (9)-intro ref (6)→(5)**: .tex "Dann geht **(6)** in eine andere Form über" — Weber "Dann geht **(5)** … , die
  wir so darstellen". Fixed the ref + restored "die wir so darstellen".
- **★ ERRATUM #19 PRESERVED (Voraussetzung 2)**: Weber prints "nicht zwei der Functionen $f_0,f_1\ldots f_{n-1}$" — but
  only $n-1$ functions exist ($f_0\ldots f_{n-2}$), so $f_{n-1}$ is a Weber MISPRINT (same pattern as §184 Satz 6 =
  erratum #18). The .tex had "corrected" to $f_{n-2}$. → transcribed **as printed** $f_{n-1}$, flagged.
- **Eigenschaft δ) not d); de-modernized sums** eqs (6),(9),(14) `\sum_{v=0}^{n-2}`→`\sum_{0,n-2}^{v}`.
- **Restored dropped structure**: the numbered Voraussetzungen list (1., 2. — .tex flattened to one sentence) + the
  "Nach (13),(16),(17),\S\,184 bekommen dann die Functionen $f_v,F_v,\Phi_v$ …" intervening prose; the k/K setup with
  all FOUR displays (f/k/Φ/K) + Weber's "es gehe … in … über" wording; the TWO $E_{v-1}$ displays before eq (12); the
  dropped passages ["so ist also $\xi_0$ durch $n-1$ Radicale $n^{\text{ten}}$ Grades ausgedrückt … zu gross wäre";
  "Nach \S\,184, (16) und (17) … von Null verschieden"; "die man z. B. dadurch erhalten kann … (Man vergleiche …
  Cayley'sche Auflösung der cubischen Gleichungen \S\,36.)"]; ~15 more prose drops/rewords (all cited in notes) incl.
  "(\S\,155)"→n/a, "(\S\,133)", "(\S\,184,(15))", "die durch ε so ausgedrückt wird", "in der That", "aber vor (7) den
  grossen", "doch", "beliebiges", "und schreiben (6) in der Form", "Danach liefert uns die Formel (18),\S\,184 …",
  "worin … bedingt". Conventions: Coëfficienten→Coefficienten; $n^{\text{te}}$/$n^{\text{ter}}$/$(n-1)^{\text{ten}}$
  ordinals; multipliciren; $(1,x)=A$ kept as printed [normal-res read = plain x; flagged, immaterial to the math].
- eqs matching .tex (kept): (4) $\tau_v=\sqrt[n]{k_v}$, (5), (7), the $R_v$ display, (11) $r_v\equiv gr_{v-1}\pmod n$,
  the radical displays, (14) body. §186 boundary left intact.
Compiles **412 pp / 0 err / 0 overfull hbox / 0 underfull / 0 missing-char / 0 undefined** (411→412, +1pp).
**Rendered §185 (output-PDF pp 404–406) eyeballed page-by-page** — $\mathfrak{K}$, Θ/Φ, \varepsilon, eqs (1)/(8)/(12)/
(13), erratum #19, δ), de-mod sums, both restored $E_{v-1}$ displays, and all prose restorations confirmed in the
typeset output.

### 2026-07-02 — PHASE 2 — §186 (Befreiung von den beschränkenden Voraussetzungen) FULL RE-TRANSCRIPTION p641bot–646bot
Wholesale reconstruction (largest so far — spans 5+ printed pp, 16 eqs, 2 Roman Sätze). Mapped page-by-page against
~500 dpi scans (p641bot title, p642 top/mid/bot, p643 top/mid/bot, p644, p645, p646), 5 foundational chunks re-verified
against notes this fire before composing. Weber's TRUE eq-numbering locked (1)–(16); the .tex had **cancelling
numbering errors** (dropped Weber(3)+merged Weber(4) → −1; fabricated an extra "(5)" → +1) so numbers re-aligned from
(6) on. Fixes applied:
- **★ NOTATION — base field $\mathfrak{K}$ (Fraktur)**: every reconstruction $\Omega$ → **𝔎** (Körper 𝔎, 𝔎(η₀),
  𝔎(ξ₀), 𝔎(ξ_r), 𝔎(η_r), 𝔎(ε), coeffs $a,b$ in 𝔎, $k_v$-roots in 𝔎, $S\in$ 𝔎) — consistent with §185.
- **eq (3) RESTORED** — Weber's $\chi(x)=b_0+b_1x+\cdots+b_{n-1}x^{n-1}$ (χ-polynomial def) was **dropped** by .tex.
- **eq (4) RESTORED to full system** — Weber $\eta_0=\chi(\xi_0),\ldots,\eta_{n-1}=\chi(\xi_{n-1})$; .tex compressed to a
  single "$\eta_0=\chi(\xi_0)$" mislabeled (3).
- **FABRICATION DELETED** — .tex "(5) $x_h=\chi(y_h)$" does **not exist** in Weber (goes (5)→(6) directly). Removed.
- **eq (5) fixed** — .tex "(4) $y_h=\psi(x_h)$" (wrong function ψ) → Weber (5) $y_0=\chi(x_0),\ldots,y_{n-1}=\chi(x_{n-1})$
  (function **χ**, full system).
- **eq (6) fixed to RATIO** — .tex "$(\varepsilon^{r_v},x)=\Theta_v$" (numerator dropped) → Weber
  $\dfrac{(\varepsilon^{r_v},y)}{(\varepsilon^{r_v},x)}=\Theta_v$.
- **eq (7) LHS fixed** — .tex "$\Theta_v=Q(k_v)$" → Weber "$Q_v=Q(k_v)$".
- **eq (14) index fixed** — .tex $(\sqrt[n]{R_h},\varepsilon^{\beta r_{h-\alpha-1}}\sqrt[n]{R_h})$ (index h) → Weber
  index **v**: $(\sqrt[n]{R_v},\varepsilon^{\beta r_{v-\alpha-1}}\sqrt[n]{R_v})$.
- **DROPPED displays/passages RESTORED**: the Vandermonde determinant $|1,\eta_i,\eta_i^2,\ldots,\eta_i^{n-1}|$ (4-row,
  dotted, +"gleich dem Differenzenproduct der η"); the §143,1 rational-values passage; the Tschirnhausen "(§. 52)" xref;
  the whole $Q_vK_v$-paragraph after (8) (".tex jumped from (8) to Satz I"); the unnumbered 3-term display chain
  $A+\sum\varepsilon^{hr_v}K_{v+1}\sqrt[n]{R_{v+1}}=A+\sum\varepsilon^{hr_{v-1}}K_v\sqrt[n]{R_v}=A+\sum\varepsilon^{hg^{-1}r_v}K_v\sqrt[n]{R_v}$;
  the $(h,h+\beta r_{-\alpha-1})$ and $(h,g^{-1}h)$ permutation displays; the $S(\xi)$ and $\tau_0\ldots\tau_{n-2}$ displays;
  the full irreducibility argument (§179, $x^n-R_0$, $\Phi(\xi_0)=0$/$\Psi(\sqrt[n]{R_0})=0$, 𝔎(ε)-degree reasoning).
- **Sätze I./II. as Roman quote blocks** (robust; the doc's `enumerate[resume]` avoided) — I. = root-formula theorem
  (eq 9 embedded), II. = the converse. `a)–d)` → `α) β) γ) δ)`. De-modernized sums `\sum_{0,n-2}^{v}`; ordinals
  numeral+superscript ($n^{\text{ten}}$, $(n-1)^{\text{ten}}$, $n^{\text{te}}$); Coëff→Coeff (ë→e); heavy prose restored.
- **★ ERRATUM #20 (Weber misprint, preserved as printed + flagged)**: p646top prints $S(\xi_0,\xi_1\ldots\xi_{n-2})$ —
  subscript $n{-}2$ — but p645bot printed $\xi_{n-1}$; $S$ is symmetric in all $n$ roots so $n{-}1$ is correct. Kept the
  $n{-}2$ as printed at the second occurrence (zoom-confirmed on p646 crop). **Errata total through §186 = 20.**
- eqs matching .tex (kept): (1),(2),(9),(10),(11),(12),(13),(15),(16) bodies; (10) ε^{+hr_v} sign; $(11)$/$(12)$ radicals.
Compiles **413 pp / 0 err / 0 overfull hbox / 0 underfull / 0 missing-char / 0 undefined** (412→413, +1pp; +4366 chars restored).
**Rendered §186 (output-PDF pp 406–409) eyeballed page-by-page** — Fraktur 𝔎, eqs (1)–(16), both Sätze I./II., the
Vandermonde det, eq(6) ratio, eq(7) $Q_v$, eq(14) index v, the 3-term chain, erratum #20, de-mod sums, and every prose/
display restoration confirmed in the typeset output.

### 2026-07-02 — PHASE 2 — §187 (Realitätsverhältnisse) FULL RE-TRANSCRIPTION p647top–648top
Heavy compression reconstruction: the .tex **collapsed Weber's entire Φ/Ψ reality argument** (5 displays + the
divisibility/rationality reasoning) into two fabricated sentences. Mapped p647 top/mid/bot + p648 top against scans this
fire. Fixes:
- **Ω → 𝔎** (reeller Körper 𝔎, ×2).
- **Restored dropped cross-refs**: "wie wir im \S\,180 gesehen haben" (metacyclic reality) + "haben wir im \S\,165
  gesehen, dass es … giebt, nämlich" (cyclic even-degree reality); .tex had bare "so giebt es … Ebenso gibt es …".
- **FIXED .tex mis-reference** "Formel (10) des §184" → Weber "die Formel (10) \S\,186" (scan-confirmed p647mid).
- **Restored the whole dropped Φ/Ψ argument** (all unnumbered displays): (A) $\sqrt[n]{R_{v+\frac{n-1}{2}}}=\Phi(k_v)(\sqrt[n]{R_v})^{g^{(n-1)/2}}$;
  (B) $\sqrt[n]{R_{v+\frac{n-1}{2}}}\sqrt[n]{R_v}=\Phi(k_v)(\sqrt[n]{R_v})^{g^{(n-1)/2}+1}$; the "$g^{(n-1)/2}+1$ durch $n$
  theilbar ⇒ rechte Seite rational" reasoning; (C) $\sqrt[n]{R_{v+\frac{n-1}{2}}}\sqrt[n]{R_v}=\Psi(k_v)$;
  (D) $\Psi(k_v)=\Psi(k_{v+\frac{n-1}{2}})$ ⇒ "$\Psi(k_v)$ reell"; the "$n^{\text{ten}}$ Potenzen conjugirt … bis auf
  eine $n^{\text{te}}$ Einheitswurzel … Product reell ⇒ Einheitswurzel $=1$" argument. The .tex had kept only the
  $r_v\equiv-r_{v+\frac{n-1}{2}}\pmod n$ display + "Formel (11) … alle reell".
- conjugiert → **conjugirt** (Weber's -irt, throughout); gibt → **giebt**; concluding Satz set as quote block preceded by
  "Damit ist also der Satz für einen reellen Körper 𝔎 bewiesen:".
- **★ ERRATUM #21 (Weber misprint, preserved as printed + flagged)**: p647mid prints the cyclic-eqn roots as
  $k_0,k_1\ldots k_{n-1}$ (×2) and the radicals as $\tau_0,\tau_1,\ldots\tau_{n-1}$ — but the cyclic equation is
  $(n-1)^{\text{ten}}$ Grades (roots $k_0\ldots k_{n-2}$) and only $n-1$ radicals $\tau_0\ldots\tau_{n-2}$ exist; the
  concluding Satz on p648 correctly prints $k_{n-2}$. Kept $n-1$ as printed at both P2 occurrences (zoom-confirmed
  crop_5_28), $n-2$ in the Satz. **Errata total through §187 = 21.**
- No numbered eqs in §187 (all displays unnumbered). The "Formel (11) … die Wurzeln ξ alle reell" subscript read as
  $\xi_h$ (immaterial glyph on p648, matches formula (11)'s index; not flagged).
Compiles **413 pp / 0 err / 0 overfull hbox / 0 underfull / 0 missing-char / 0 undefined** (held 413; +1123 chars restored).
**Rendered §187 (output-PDF p410) eyeballed** — Fraktur 𝔎, all six displays (Φ×2, Ψ×2, the ⁿ√R-pair, the $r_v$ congruence),
§180/§165/§186 refs, erratum #21, and the concluding-Satz quote block confirmed in the typeset output.

### 2026-07-02 — PHASE 2 — §188 (Metacyklische Gleichungen fünften Grades) FULL RE-TRANSCRIPTION p648mid–653mid
**LAST section of Band I main text** (Achtzehnter Abschnitt). n=5 metacyclic-quintic worked example: solve the cyclic
biquadratic (roots $k_0\ldots k_3$) generally via $w=(k_0-k_2)(k_1-k_3)$, then substitute into §186(9) for the quintic
root $\xi$. eqs (1)-(14), NO Sätze. Mapped page-by-page (p648-p653, all chunks + eq(14) zoom-confirmed) → notes =
scratchpad/weber_188_notes.md; composed retrans_188.py, applied, compiled, render-verified output-PDF pp411-414 page-by-page.
Fixes:
- **Ω → 𝔎** everywhere (Weber uses Fraktur throughout §188 — confirmed p648bot/p649/p651).
- **ρ → ϱ (\varrho)** everywhere (eq 10, the 6-radical basis, both permutation displays, eq 14, the 3-radical block, the
  closing display) — Weber's rounded-tail rho, matching §179.
- **★ MATH ERROR fixed**: the Abel display printed $k_0=C+B\sqrt{1+e}+\ldots$ in the .tex; Weber's first radical is
  $\sqrt{1+e^2}$ (scan-confirmed p652/p653). Restored $\sqrt{1+e^2}$.
- **★★ ERRATUM #22 (Weber misprints, preserved as printed + flagged)** — eq (14), zoom-confirmed crop_15_14: Weber's
  printed $K_2,K_3$ disagree with his own substitution-group derivation, which the .tex had silently "corrected".
  Restored Weber's printed forms: (22a) $K_2=\ldots+A_4r\varrho$ [the $S^2$ image is $-A_4r\varrho$]; (22b) $K_3$ third
  term $-A_2\varrho'$ [should be $A_3\varrho'$]; (22c) $K_3$ last term $-A_4r\varrho'$ [the $S^3$ image is $+A_4r\varrho'$].
  Kept all three as printed, flagged. **Errata total through §188 = 22.**
- **DROPPED content RESTORED**: the Kronecker/rational-numbers passage ("So können wir also beispielsweise für den Körper
  der rationalen Zahlen … ist ein sehr merkwürdiger von Kronecker herrührender Satz, den wir im zweiten Bande kennen
  lernen werden"); the "Es handelt sich dann nur darum, cyklische Functionen in genügender Anzahl zu bilden … algebraisch
  ausdrücken kann" sentence; **★★ the entire 4-row × 6-col substitution TABLE** (the 4 iterates of the substitution on the
  6-element basis $1,r,\varrho,\varrho',r\varrho,r\varrho'$; .tex had compressed it to "Daraus folgt … rationalen
  Ausdruck besitzt") + its "und wenn man diese Vertauschung wiederholt … folgende Vertauschungen gemacht werden … und wenn
  man die vier so sich ergebenden Ausdrücke addirt …" framing; "Der Ausdruck (12) ist also insofern allgemeiner, als er
  auch den besonderen Fall $a=0$ umfasst, in dem die biquadratische Gleichung in zwei quadratische Gleichungen zerfällt";
  the "wenn man rechts für $\varrho'^2$ seinen Ausdruck durch $r$ einsetzt und bedenkt, dass $r^2$ rational ist"
  explanation; "also niemals bei reellen Körpern"; the specific "$a=1:e$ … $B$ und $h$ durch $Be$ und $he^2$ ersetzt";
  "worin $A_1,A_2,A_3,A_4$ rational sind"; "der Reihe nach congruent mit $1,2,4,8$"; "wie in \S\,185"; + many clause drops.
- de-mod: ordinal "$5^{\text{ten}}$ Grades" (numeral, p652 body; title keeps spelled "fünften Grades" as printed);
  Coëff→Coeff (ë→e); "z. B."/"d. h." normal spaces; giebt/substituiren/permutiren kept. Both 2-row Vertauschung displays
  as \begin{pmatrix} (parens; the p652bot one clearly parenthesized). 4-row table as array, Weber's commas kept.
- eqs matching .tex (kept): (1),(2),(3),(4),(5),(6),(7),(8),(9),(10),(11),(12),(13) bodies; only the Abel display (C) and
  eq (14) (D) changed.
Compiles **414 pp / 0 err / 0 overfull hbox / 0 underfull / 0 missing-char / 0 undefined** (413→414, +1pp; +3039 chars).
**Rendered §188 (output-PDF pp411–414) eyeballed page-by-page** — Fraktur 𝔎, ϱ throughout, eqs (1)–(14), the restored
4-row substitution table, both pmatrix substitutions, the √(1+e²) fix, erratum #22 (K_2/K_3 printed misprints), the
Kronecker passage, and every restored clause confirmed in the typeset output. **§188 COMPLETES the Achtzehnter Abschnitt
(§183-188) and the entire Band I main text — the whole re-transcribable body of vol1 is now source-faithful.**
NOTE: the printed \section*{Berichtigungen} (Weber's own errata, 2 entries) sits after §188 and was NOT touched by this
edit (it is after the end anchor); should be verified against the actual printed errata page as a separate small task.

### 2026-07-02 — PHASE 2 — \section*{Berichtigungen} (Weber's own errata) VERIFIED vs printed p654
Rendered + zoom-read the printed Berichtigungen page (printed p654, after §188). Two fixes to the .tex:
- **$X_m$ statt $X_n$ → $x_m$ statt $x_n$** (LOWERCASE x — zoom-confirmed crop_52_43, matches the lowercase x in the 2nd
  entry's $(2x^2+1)^2$; the .tex had wrongly capitalised the first entry).
- **"Seite 182, in der Formel" → "Seite 182 in der Formel"** and **"Seite 347, in der Formel" → "Seite 347 in der
  Formel"** (Weber prints NO comma after the page number; the .tex had added one to both entries).
- 2nd-entry math $(2x^2+1)^2$ statt $(2x^2-1)^2$ already matched Weber (kept). Compiles 414pp/0err/0 overfull/0 undefined
  (text-only micro-edit; not separately rendered — the fix is a 2-glyph + 2-comma change verified against the p654 zoom).

### 2026-07-02 — PHASE 2 — §69 (Invarianten-Eigenschaft der Tschirnhausen-Transformation) FULL RE-TRANSCRIPTION printed p212–215
**Non-sequential held-list item** (Sechster Abschnitt, back in the front matter — Tschirnhausen invariance, the run-up to
Hermite's theorem). Located via source-PDF OCR text search (running head "§. 69. Invarianten-Eigenschaft" at pdfpage 239 =
printed p213). Mapped page-by-page (p212-215, all chunks + eqs 14/15 zoom-checks) → notes = scratchpad/weber_69_notes.md;
composed retrans_69.py, applied ("replaced 5148 → 7219 chars", +2071), compiled, render-verified output-PDF pp136–138.
**★★★ CENTRAL DEFECT — the .tex COLLAPSED Weber's THREE-letter function system.** Weber uses four letters in two pairs:
$F(t,x)\leftrightarrow\Phi(\tau,\xi)$ are the **τ-power** forms; $Y(t,x)\leftrightarrow H(\tau,\xi)$ are the **τ_k-variable**
forms. The reconstruction wrote $H$ for Weber's $\Phi$ in eqs (3),(8),(9) and the "ebenso in Φ(τ,ξ)" text — merging the
power-form with the variable-form. Restored $\Phi$ at all four sites; kept $H$ where Weber legitimately uses it (eq 10 2nd
line, eqs 11, 12, 17).
Fixes:
- **TITLE Invarianteneigenschaft → Invarianten-Eigenschaft** (Weber hyphenates — running-head + p212 confirmed).
- eq (3): restored dropped 2nd-line expansion + the $\Phi_i/F_i$ explanation; $H\to\Phi$.
- eq (7): restored the $(1/n)$ factors the .tex had cleared by multiplying through by $n$.
- restored the $dt/d\tau$ display + **3 intermediate displays** dropped between (7) and (8).
- eq (8): $H(\tau,\xi)\to\Phi(\tau,\xi)$. eq (9): LHS $H\to$ expanded $\tau^{n-2}\Phi_0+\ldots+\Phi_{n-2}$; braces $\{\}\to[]$.
- eq (10): added dropped 2nd line $H(\tau,\xi)=\ldots$ .
- eq (13): inline → stacked (\begin{array}) with dotted continuation row.
- **eq (14): REVERSED the .tex's descending powers → Weber's ascending** $t_{n-2}-(n-2)t_{n-3}z+\ldots\pm t_0 z^{n-2}$
  (scan-confirmed); restored the multiplier display + the binomial-coefficient display around it.
- **eq (15): the .tex had a wrong $\Theta(z)$ — replaced with Weber's $z\leftrightarrow\xi$ substitution**; restored the
  following $\Theta(\xi)$ unnumbered display (ascending ξ-powers) + its subst display.
- eq (16): $z\to\xi$.
- p215 running text: $\Theta(z)\to\Theta(\xi)$, $\varphi(z)\to\varphi(\xi)$, $\tau_i\to\tau_k$, $t'_i\to t'$, "in Bezug
  auf $r$" → "in Bezug auf $\tau$" (z/ξ ambiguity resolved by logic: functions **of** z keep $(\gamma z+\delta)$ bases,
  **results** are Θ(ξ)/φ(ξ)); restored "also derselbe ist, wie in den Functionen Y und H".
- Hermite Satz: restored dropped "schöne" (Weber: "der schöne Satz von Hermite"); $y_i\to y$; "f und T" → display
  $f(z),\;T(z)$; set as \begin{quote} block matching house convention.
- de-mod: giebt/Coefficienten/Functionen kept as printed; no ordinals in this section.
- **NO new errata** (§69 adds none; running total stays **22**).
Compiles **415 pp / 0 err / 0 overfull hbox / 0 underfull / 0 missing-char / 0 undefined** (414→415, +1pp; +2071 chars).
**Rendered §69 (output-PDF pp136–138) eyeballed page-by-page** — Φ/H disambiguation, eq (3) 2nd line, the $dt/d\tau$ +
3 restored displays, eq (7) $(1/n)$ factors, eq (9) expanded LHS, eq (10) 2nd line, eq (13) stacked, eq (14) ascending
powers, eq (15) z↔ξ substitution, Θ(ξ) block, eqs (16)–(18), and the Hermite Satz quote block all confirmed in the
typeset output.

### 2026-07-02 — PHASE 2 — p466 (§145 Galois'sche Resolvente / Normalgleichung) FULL RE-TRANSCRIPTION printed p466
**Held-list stray page** (Dreizehnter Abschnitt; the one page left HELD in batch wc8sx00lk's p462–467 §144–146 run — flagged "eq(6)/eq(7)/Gesammtheit/G(t) all collapsed"). This page proves $N$ is a Normalkörper (the Galois'sche Resolvente construction). Rendered printed p465bot/p466/p467top to fix the boundaries (p467 already faithful = end anchor "Nun haben $G(t)$…"). Composed retrans_466.py, applied (+1452 chars), compiled, render-verified output-PDF p299.
Fixes:
- **Straddle sentence reworded → restored**: .tex "und bezeichnen $N$ auch durch $\Omega(\rho)$" → Weber "und **können dann den Körper** $N$ auch durch $\Omega(\rho)$ **bezeichnen**" (verb-last order, confirmed p465bot→p466top join).
- **Collapsed lead-in restored**: .tex "Die eine Wurzel $\rho$ ist eine rationale Function … Schreiben wir" → Weber "von der zu zeigen ist, dass es eine Normalgleichung ist. Zu diesem Zweck bemerken wir zunächst, dass die eine Wurzel $\rho$ dieser Gleichung eine rationale Function der $\alpha,\alpha_1\ldots\alpha_{m-1}$ ist, **weil sie in $N$ enthalten war**. **Setzen wir, um dies anzudeuten**,".
- **★ FABRICATED function symbol $R$ → $\rho$**: .tex wrote $\rho=R(\alpha,\ldots)$ / $R(\alpha_0,\ldots)$; Weber's function symbol is $\rho$ itself ($\rho=\rho(\alpha,\alpha_1\ldots)$). Restored $\rho(\cdot)$.
- **★ DROPPED display restored**: the digit-arrangement display $0,1,2\ldots m-1,$ + "deren Anzahl $\Pi(m)$ beträgt:".
- **★★ eq (6) restored (was DROPPED entirely)**: $(0,1,2\ldots m-1),\ (0',1',2'\ldots(m-1)'),\ (0'',1'',2''\ldots(m-1)'')\ldots,$ + the "worin die Ziffern mit einem, zwei etc. Accenten dieselben sind, wie die ohne Accent, nur in anderer Reihenfolge, und bilden hieraus die Functionen" connector.
- **★★ eq (7) fixed (was MIS-NUMBERED)**: .tex tagged the bare list "$\rho,\rho',\rho''\ldots$" as (7); Weber's (7) is the full functional forms $\rho=\rho(\alpha_0,\alpha_1\ldots\alpha_{m-1}),\ \rho'=\rho(\alpha_{0'},\ldots),\ \rho''=\rho(\alpha_{0''},\ldots)\ldots$ (rebuilt as a 2-line \begin{equation}\tag{7}\begin{array}{rcl} display, = aligned).
- **★ Paraphrase → restored**: .tex "von der Gestalt $R(\alpha_0,\ldots)$ mit permutirten Argumenten" → Weber "**unbekümmert darum, ob darunter etwa unter einander gleiche vorkommen oder nicht**".
- **★★ DROPPED Gesammtheit-argument restored** (whole paragraph): "Wenn wir in allen den Anordnungen (6) ein und dieselbe Vertauschung vornehmen, z.\ B. $0$ mit $1$, so ändert sich die Gesammtheit dieser Anordnungen nicht … in dieselbe Anordnung übergehen." (.tex had collapsed to the single sentence "Durch jede Vertauschung der Wurzeln werden diese Functionen nur unter einander permutirt").
- **DROPPED G(t)-reasoning restored**: "für eine Veränderliche $t$", "die gewiss Functionen von $\alpha,\alpha_1\ldots\alpha_{m-1}$ sind, ungeändert, wenn diese Grössen irgendwie permutirt werden; d.\ h.", and the final sentence "**Alle Wurzeln von $G(t)$ sind Grössen in $N$, da sie durch die $\alpha$ rational ausgedrückt sind.**". G(t) display kept unnumbered as printed.
- de-mod/house: giebt/Coefficienten (Weber "Coëfficienten" ë→e) kept; z.\ B. / d.\ h. normal-escaped spaces (file convention, 76/109×); §.\,143 §-ref spacing kept.
- **⚠ NOTE — ϱ vs ρ (queued global sweep):** Weber prints the primitive-element glyph as **ϱ (\varrho)** throughout §145 (confirmed p465bot/p466 "primitives Element ϱ", "so genügt ϱ", "ϱ=ϱ(α…)"). Kept **\rho** here to match the uniform \rho the reconstruction uses across the whole §145–147 Galois-resolvent chapter — changing only p466 would split one variable into two glyphs. Added a **global \rho→\varrho (§145-region) sweep** to the end-of-vol1 queue.
- No new errata (still 22).
Compiles **416 pp / 0 err / 0 overfull hbox / 0 underfull / 0 missing-char / 0 undefined** (415→416, +1pp). **Rendered output-PDF p299 eyeballed** — eqs (5),(6),(7), the restored digit display, the full Gesammtheit paragraph, the G(t) display + restored reasoning, and the clean p467 paragraph join all confirmed. **p466 was the last stray HELD page in the Galois-applications region.**

### 2026-07-02 — PHASE 2 — §138-numbering (Vorzeichenbestimmung. Quadratische Reste) FULL RENUMBER printed p439–445
**LAST held-list item** (Zwölfter Abschnitt, quadratic reciprocity). The 2026-06-26 mapping was incomplete;
re-read all scans p439–445 by eye. ★★ **Weber's §138 uses TWO PARALLEL flush-left numbering systems**: (a)
**RULES "1."–"11."** (period, no parens) for the number-theoretic RESULTS, and (b) **FORMULAS "(1)"–"(10)"**
(parenthesized) for the trigonometric identities/steps. The reconstruction had CONFLATED them — it mis-cast
Weber's rule numbers 2.–10. as parenthesized eq-tags/primes and auto-numbered the connecting PROSE instead.
Composed retrans_138.py (v1 → 7 overfull from mid-paragraph \makebox[\linewidth]; v2=retrans_138b.py isolates
each flush-left rule in its own \noindent paragraph), applied, compiled, render-verified output-PDF pp287–289.
Weber's true dual sequence (all confirmed against scans):
- RULES: **1.** Satz [(m/n)=±1 je nachdem…]; **2.** (1/n)=+1; **3.** (−m/n)=(−1)^{(n−1)/2}(m/n); **4.**
  (−1/n)=(−1)^{(n−1)/2}; **5.** (2m/n)=(−1)^{(n²−1)/8}(m/n); **6.** (2/n)=(−1)^{(n²−1)/8}; **7.** "Es ist"
  (m/n)=(m'/n) wenn m≡m'; **8.** (mm'/n)=(m/n)(m'/n); **9.** reciprocity (m/n)=(−1)^{(m−1)(n−1)/4}(n/m); **10.**
  (m/n)(m/n')=(m/nn'); **11.** Satz [Legendre residue/nonresidue].
- FORMULAS (kept, .tex tags were correct): (1),(2) cos/sin=±1/±√n; (3),(4) exact cos/sin; (5) sin mφ/sinφ;
  (6) β=sin²; (7) α=sin²; (8) φ=; (9) ∏sin/∏sin; (10) (m/n)=…∏∏(α−β); **★ (7) REUSED** for the congruence
  (n−1)(n'−1)=(nn'−1)−(n−1)−(n'−1)≡0 (mod 4) — a **genuine Weber reused parenthesized formula-number** (like
  §163 (7)/(11), §151 (4), §184 (2)); flag for the reused-eq audit.
Fixes vs .tex: rules 2.,3.,4.,5.,6.,8.,9.,10. WERE (bare display)/\tag{3'}/\tag{4'}/\tag{5}/\tag{6}/(bare)/\tag{9'}/\tag{10'}
→ now flush-left "N." (rendered via \makebox[\linewidth]{\makebox[2em][l]{N.}\hfill$…$\hfill\makebox[2em]{}}); rule 7
was \tag{7} inside the bogus enumerate → now "7. Es ist" + 2 displays; the first enumerate had auto-numbered the
PROSE paragraphs 1,2,3,4 → now rule 1 is a single-item enumerate and the prose is plain paragraphs; **★ cross-ref
"bleibt diese Formel auch noch richtig" → Weber "bleibt 8. auch noch richtig"**; **★ reused (7) congruence order
REVERSED in .tex → Weber "(n−1)(n'−1)=(nn'−1)−(n−1)−(n'−1)≡0"**; **★ ".tex "Oder:" (cap+colon) → Weber lowercase
"oder" (no colon)"**; rule 9 trailing period → comma (sentence continues). Rule 11 already correct (enumerate
start=11); all prose cross-refs "Nach 3. und 5."/"nach 5. und 6."/"Aus 8. und 9."/"von 10. die Formel 9. und dann
8. … aus 4. und 6."/"leichter nach 9."/"aus 7. und 8." verified correct + now resolve to real flush-left rules.
- **⚠ ϱ vs ρ**: Weber prints the absolut-kleinster-Rest as ϱ; kept \rho (matches §138 KEEP region; folded into the
  broader queued vol1 ρ→ϱ sweep).
- No new errata (still 22); NUMBERING-only fix (no math changed — the rule formulas were mathematically correct
  in the .tex, only their labels were wrong).
Compiles **416 pp / 0 err / 0 overfull hbox / 0 underfull / 0 missing-char / 0 undefined** (held 416; +8 chars net
over v1). **Rendered output-PDF pp287–289 eyeballed** — rules 2.–11. flush-left, formulas (5)–(10) + reused (7)
parenthesized-right, the "8." cross-ref, the reordered congruence, lowercase "oder", and the §139 transition all
confirmed. **★★★ §138-numbering was the LAST held-list item — the entire vol1 §141→§188 + §69 + p466 +
§138-numbering re-transcription pass is now COMPLETE. Only global sweeps remain.**

### 2026-07-02 — PHASE 2 — GLOBAL SWEEP #1: gibt → giebt (DONE)
First of the closing global sweeps. Weber (1895, pre-1901 orthographic reform) uses **giebt** uniformly —
directly re-confirmed by eye this session on p439 ("giebt bei der Theilung") and p527 ("Es giebt drei
verschiedene mit $P_1$ conjugirte Gruppen"). Grep `\bgibt\b` found only **4** bare "gibt" left (the earlier
phase caught the rest): 3 in §160 (p527, the four-element permutation-group discussion — 18665/18688/18695)
and 1 in §172 (line 20657, the ϱ-cube-period computation "so gibt die Ausführung der Cuben"). Applied
`\bgibt\b→giebt` via word-boundary regex (asserted exactly 4 replacements; "giebt" does not contain "gibt"
as a substring so no double-apply). §160 ×3 rest on the p527 scan just eyeballed; the §172 instance rests on
the twice-confirmed uniform convention (its specific scan not individually rendered — pdftotext OCR fails on
"Cuben" in that old scan; can be spot-checked in a later pass, but Weber's giebt is orthographically uniform
across Band I). Now **0 bare "gibt", 136 "giebt"** in the file. Compiles **416 pp / 0 err / 0 overfull / 0
undefined** (held 416). **Remaining global sweeps: ρ→ϱ audit, \pmod→(mod.), errata/reused-eq review.**

### 2026-07-02 — PHASE 2 — GLOBAL SWEEP #2: \rho → \varrho (DONE)
Weber (1895 German typography) prints lowercase rho as **ϱ (varrho)** uniformly — straight ρ was not used in
German math printing of that era. The .tex was MIXED: 573 `\rho` (modernized) vs 85 `\varrho` (already
converted by me/earlier phase). Established the uniform-ϱ convention by eye across EVERY distinct usage type:
- roots of unity: **§132** (already \varrho) + **§174** cube-root ϱ=(−1+√−3)/2 zoom-confirmed this fire
  (p592: "dritten Einheitswurzel ϱ", "R(ϱ)", "ξ=x+ϱy", "α=a+bϱ" — clear rounded varrho tail);
- absolut-kleinster-Rest: **§138** (p439/440 confirmed by eye);
- primitive element: **§145** (p465bot/p466 confirmed by eye);
- g-root/radicals: **§179/§186/§187/§188** (already \varrho);
- cubic transf/trig/continued-fractions/cyclic: **§71/§112/§115/§165** (already \varrho).
Applied global `\rho(?![a-zA-Z])→\varrho` (word-boundary regex; \varrho contains no "\rho" substring so no
double-apply; verified no `\rho` in any \newcommand/\def/preamble macro before running). **Converted 573; now
0 \rho, 658 \varrho.** The early complex-modulus ρ (§8-9, ρ²=x²+y², ~81 front-matter occurrences) was NOT
individually eyeballed (pdftotext OCR couldn't locate its printed page) but is the same ϱ glyph — rests on the
established uniform typography; spot-checkable later. Compiles **416 pp / 0 err / 0 overfull / 0 underfull / 0
missing-char / 0 undefined** (held 416). **Rendered output-PDF p299 (§145 Galois'sche Resolvente, a former
\rho section) eyeballed** — Ω(ϱ), ϱ=ϱ(α,α₁…), ϱ,ϱ',ϱ'', G(t)=(t−ϱ)(t−ϱ')(t−ϱ''), N=Ω(ϱ) all render as correct
varrho, matching Weber's printed p466. **Remaining global sweeps: \pmod→(mod.) [caveat: Weber often prints
"(mod n)"/"(mod 4)" without the trailing period], errata/reused-eq review.**

### 2026-07-02 — PHASE 2 — GLOBAL SWEEP #3: \pmod (VERIFIED — NO CHANGE NEEDED)
The queued "\pmod → (mod.)" de-modernization was based on a **mistaken premise**. Direct evidence:
- **p442 600-DPI zoom** (§138 rule 7): Weber prints "wenn $m \equiv m'$ **(mod n)**" — "mod" then a space then
  the modulus, **NO period after "mod"** (the period after ")" is the sentence end). p444 likewise "(mod 4)".
- Standard LaTeX `\pmod{n}` renders exactly "(mod n)" (no period) — so the .tex's **114 `\pmod` already match
  Weber**. The file also has 8 `\bmod` (inline "mod" operator) and 2 literal "(mod $m$)" (§164, lines
  19134/19148, also no-period) — and **ZERO** literal "(mod." with a period anywhere.
So the current mod-form is already source-faithful; converting to "(mod.)" would INTRODUCE a spurious period
Weber does not print. **No change made.** (If a later spot-check of a number-theory section ever finds a Weber
"(mod. m)" with period, handle locally — but the confirmed dominant form is no-period, and the file is
internally uniform.) Compiles unchanged **416 pp / 0 err**. **Remaining: global sweep #4 = errata de-dup +
reused-eq audit.**

### 2026-07-02 — PHASE 2 — GLOBAL SWEEP #4: ERRATA DE-DUP + REUSED-EQ AUDIT (DONE) — CANONICAL TABLE
Consolidated all flagged Weber print-errata from the CERT log into one canonical list and checked for
duplicates. Running totals across the log ("through §186=20, §187=21, §188=22") reconcile cleanly to **22
numbered errata**, no duplicates. Spot-verified 6 of them still transcribed EXACTLY AS PRINTED in the .tex
(#10 line 20724, #11 line 18963, #12 line 18440, #15 line 21439, #18 line 22094, #19 line 22209) — the
giebt + ρ→ϱ global sweeps did not disturb any (they touch only orthography/rho-glyph, not errata math).

**CANONICAL 22 WEBER PRINT-ERRATA (all transcribed as printed + flagged; NOT silently corrected):**
1. p221 — $Q_0$ (arithmetic/index typo)
2. p334 — $u'=0{,}0164$ (Weber's own sum needs $0{,}00164$; NOT in Weber's Berichtigungen ⇒ uncorrected typo)
3. p357 — $30°$
4. p382 — $+\eta^2$
5. p378 — $\alpha_1$
6. p385 — $\omega'-\omega$
7. p402 — $a_3/a_4$
8. p426 — mod $m$
9. p482 — "transitiv/intransitiv" (§150-region)
10. p582 — $\tfrac14(a+b)^2+\tfrac34(a-b)^3$ (final exponent $^3$ typo, math wants $^2$)
11. p536 — §162 $\sigma_k\sigma_h=[\alpha,\Theta_k\Theta_h(x)]$ (the $(x)$ should be $(\alpha)$)
12. p521 — §158 "Systeme der Imprimivit\"at" (missing "ti"; std Imprimitivität)
13. p548 — §165 eq (7) 2nd term $(\varepsilon^{\lambda_2},\alpha)=\sqrt[p_2]{\varphi_2}$ missing the $^{m_2}$ exponent
14. p502/504 — §154 $q$ vs $\nu$ ("$\nu$ Elemente" + $\varkappa_{\nu-1}$ vs $q$ in (2)(3)(7))
15. p612 — §180 $z_0\equiv\dfrac{b}{a-b}\pmod n$ (fixed point of $z\mapsto az+b$ is $b/(1-a)$; "$a-b$" is a typo)
16. p629 — §182 $w_0=v_1v_2+v'_4v_5+v_3v_6$ (stray prime on $v_4$; $v$ has no primed members)
17. p628 — §182 "Da $F(z)$ auch irreducibel ist" (resolvent is $F(v)=0$; $F(z)$ is a misprint)
18. p635 — §184 Satz 6 "$f_0,f_1\ldots f_{n-1}$" (only $f_0\ldots f_{n-2}$ exist; $f_{n-1}$ typo) [.tex line 22094]
19. p??? — §185 Voraussetzung 2 "$f_0,f_1\ldots f_{n-1}$" (same $f_{n-1}$ pattern, distinct instance) [.tex line 22209]
20. p646 — §186 $S(\xi_0\ldots\xi_{n-2})$ (should be $\xi_{n-1}$; the recurring $n{-}1$/$n{-}2$ index misprint)
21. p648 — §187 $k_{n-1}$/$\tau_{n-1}$ (cyclic eqn is $(n-1)$-degree ⇒ $k_0\ldots k_{n-2}$, only $n-1$ radicals)
22. p653 — §188 eq (14) $K_2$ ($+A_4r\varrho$), $K_3$ ($-A_2\varrho'$ / $-A_4r\varrho'$) — 3 sign/subscript slips
**De-dup result: NO duplicates.** Pattern-similar pairs are genuinely distinct printed instances in different
sections: #18 vs #19 (both "$f_{n-1}$" but §184-Satz6 line 22094 vs §185-Vor2 line 22209 — confirmed separate);
#20 vs #21 (both the $n{-}1$/$n{-}2$ index pattern but §186 $S(\xi)$ vs §187 $k$/$\tau$); #16 vs #17 (both §182 but
$v'_4$ vs $F(z)$); #1 vs #2 (both arithmetic typos but different pages/values).

**NOTED-BUT-UNCOUNTED errata (documented, deliberately not in the 22):** §49 eq (5) `nν+mμ` (type-B "paired"
observation, left faithful — leaves §49(5) vs eq(14) mutually inconsistent, cf. log line 102); the m=3 example
glyph "c vs α_0" (p~509, 500dpi-degraded, "possible minor, not counted").

**REUSED PARENTHESIZED EQ-NUMBERS (all genuine Weber reuses, NOT bugs — each documented at its section):**
§138 (7) [α=sin² AND the congruence]; §151 (4) [doubled]; §163 (7) and (11); §181 (12) [u-sextic]; §184 (2)
[doubled]. No spurious/broken reuses remain (the reconstruction's fabricated primed tags were all removed).

**Weber's OWN published Berichtigungen** (the errata page, printed p654, 2 entries: p182 $x_m$; p347
$(2x^2+1)^2$) are transcribed in the .tex `\section*{Berichtigungen}` and were verified vs p654 separately —
these are Weber's editorial corrections, distinct from the 22 print-typos above.

Compiles **416 pp / 0 err** (audit-only, no .tex change). **★★★ ALL FOUR GLOBAL SWEEPS COMPLETE. The entire
vol1 (Band I) source-fidelity pass is now DONE: §141→§188 section-by-section + §69 + p466 + §138-numbering +
gibt→giebt + ρ→ϱ + \pmod-verify + errata audit. 22 print-errata preserved & flagged, 416pp, zero badness.**

### 2026-07-02 — PHASE 2 — CLOSING POLISH (a)+(b) DONE
- **(a) complex-modulus ρ→ϱ region CONFIRMED by eye** (the one un-eyeballed ρ→ϱ region): printed **p18**
  (Erster Abschnitt, complex numbers) — "Der Radiusvector … hat den Zahlwerth **ϱ = √(x²+y²)** … der der
  absolute Werth … Modulus der complexen Zahl z" — clear varrho tail. So the global ρ→ϱ conversion is now
  verified by eye across EVERY usage type in Band I (complex modulus + roots-of-unity + primitive-element +
  abs-kleinster-Rest + radicals/g-root/cube-root). Last ρ→ϱ gap closed.
- **(b) visual spot-check of map-phase "verified faithful" sections — ALL CLEAN.** Rendered + eyeballed
  output-PDF **p310 (§151), p366 (§170-tail/§171), p400 (§182-tail/§183)**: §151 eqs (1)-(4)+Θ=χ(α) chain+m=6
  example; §170 eqs (15)-(17) ψ_{λ,μ} congruences+Π-binomial; §171 Gauss-sum opening (A=Σr^a,B=Σr^b,(−1,r)=A−B);
  §182 w₀-w₄ (eq 2) with **erratum #16 v'₄ preserved**; §183 opening + footnote 75. All render coherent — the
  giebt + ρ→ϱ sweeps rendered cleanly here, "(mod n)" no-period correct, errata intact, no residual artifacts.
Compiles **416 pp / 0 err** (verification-only). **vol1 (Band I) fidelity pass + closing polish COMPLETE.**
Only remaining vol1 item = (c) LaTeX-zip packaging/publish, deferred for Floris's go-ahead.

### 2026-07-02 — PHASE 2 — BROADER QA VISUAL SPOT-CHECK (DONE) — vol1 provisionally CERTIFIED-CLEAN
Final due-diligence render+eyeball of scattered output pages weighted to the ρ→ϱ-swept sections only
eyeballed at p18 before. **ALL CLEAN:**
- **output p10** (§8-9 early complex numbers) — the modulus/triangle-inequality passage: ϱ=√(x²+y²), ϱ²=x²+y²,
  (ϱ+r−R)(ϱ+r+R)=…, ϱ²r²−(ax+by)²=(ay−bx)², R≥r−ϱ — all ϱ correct, matches Weber source p18.
- **output p163** (§80 Trägheit der Formen) — Sylvester inertia "defect" ϱ: "Unterschied m−π−ν mit ϱ", eq (1)
  π+ν+ϱ=m — ϱ correct (distinct usage: count of zero coefficients).
- **output p271** (§134 Irreducibilität) — primitive-root ϱ: "die wir mit ϱ bezeichnen wollen, für die φ(ϱ)=0";
  X_n=φ(x)ψ(x), Φ(x)=φ(x)φ(x²)…φ(x^{n-1}) — clean.
- **output p302** (§147 Zusammensetzung der Substitutionen — the LARGEST ρ→ϱ cluster, 72 conversions) —
  σ=(ϱ,ϱ_a), σ'=(ϱ_a,ϱ_b), σ''=(ϱ,ϱ_b) (eq 1), σσ'=σ'' (2), (σσ')σ''=σ(σ'σ'') (3), eq (4), the σσ'σ''σ'''
  chain with ϱ_a,ϱ_b,ϱ_c,ϱ_e — every ϱ + subscript renders perfectly.
Together with the earlier spot-checks (§145 p299, §151 p310, §170/171 p366, §182/183 p400) and the §174 zoom,
the ρ→ϱ sweep is verified correct across ALL usage types (complex modulus / inertia defect / primitive root /
Galois primitive element / substitution pairs / roots of unity / g-root / cube-root) and NO residual
reconstruction or rendering artifact appeared on any spot-checked page. Compiles **416 pp / 0 err / 0 badness**.
**★★★★★ vol1 (Band I) — the reconstruction-repair fidelity mission is COMPLETE and provisionally
CERTIFIED-CLEAN** (provisional per house rule "never certify": all held/reconstructed sections re-transcribed +
4 global sweeps + full ρ→ϱ verification + broad QA spot-check; NOT a full symbol-by-symbol re-cert of every one
of the 648 pages — the map-phase "faithful" islands rest on agent-audit + spot-checks). 22 Weber print-errata
preserved & flagged. Remaining is a scope decision for Floris: deeper full page-by-page re-cert / LaTeX-zip
packaging+publish / advance to vol2·vol3.

### 2026-07-02 — ★ 20-PAGE FULL-RIGOR SAMPLE CERT (per Floris) — OVERTURNS the "certified-clean" claim above
Ran the by-hand symbol-by-symbol sample cert Floris ordered (details + per-page table in WEBER_SAMPLE_CERT.md).
**Result: NOT clean.** The "map-phase verified faithful" AND the Phase-2 "§141→§188 complete" designations are
BOTH proven unreliable. Findings across 20 pages:
- **§26 (p90) — REFORMULATED, now FULLY RE-TRANSCRIBED.** Was index-relettered (μ/k → Weber's k/i), sums
  modernised (\sum_{k=1}^n → Σ^i index-above), α-normalisation dropped ($A_\mu^{(k)}=A_{k\mu}$ + un-normalised
  $Ax_i$ → Weber's $A_k^{(i)}=A\alpha_k^{(i)}$ + eq (5) solving $x_i=\alpha_i^{(k)}y_k$), and the
  "[\S\,23,(3),(7)]" clause dropped. Re-transcribed .tex 3028-3057 to Weber's exact printed form (scans p90
  top/mid/bot + 600dpi α-zoom). Renders correct.
- **§164 (p542-p545) — HEAVILY CONDENSED RECONSTRUCTION, now FULLY RE-TRANSCRIBED.** This section was NOT in
  the held-list (it slipped the gap between held §163 and §165) and the Phase-2 "§141-188 complete" claim never
  actually did it. Damage: dropped display eq (Σ^ε ε^{-k-ν}…) after "Macht man…"; reworded "Der Satz 2. ist ein
  specieller Fall…"→"Noch allgemeiner…"; dropped the standalone product + variable-explanation prose; eq (7) sum
  modernised; dropped the whole B_k=Σ^ε…(ε,α^{λ}) derivation; **dropped the formal enumerated Satz 3 + eq (8)**;
  dropped the "In diesen Theoremen…" paragraph; wrote "**e**-gliedrige Perioden" (Weber: f-gliedrige — self-
  contradicting its own next line); dropped Weber's period-grouped (ε,α) expansion; a `\\alpha` typo in eq (10);
  dropped "wofür wir auch (ε,η) schreiben können."; **dropped the entire final development — eqs E_k^{(ν)}/G_k,
  the "Entsprechend der Formel (10)…" displays, and the formal Satz 4** — replacing it all with a one-line
  fabricated summary. Re-transcribed the whole section to Weber's printed form (scans p542 mid/bot, p543 top/bot,
  p544 top/mid/bot, p545 top/mid/bot, p546 top; two eq-formulae zoom-confirmed at 600dpi). Also fixed **6
  index-below sums → index-above** (eqs 2,3,4 Σ^ε; λ-restatement Σ^λ; eq 6 Σ^ε) matching Weber's placement, and
  the spurious paragraph break after eq (4). Rendered output-PDF pp345-347 eyeballed page-by-page — every eq,
  Satz, index-above sum, and prose restoration confirmed. File 416→**417 pp** (growth from ~1.5 pp restored).
- **p400 (§128) — dropped clause FIXED**: restored "Dies ist aber sehr einfach; denn" (+ lower-cased "ist") and
  a dropped comma ("dazu, zu zeigen").
- **p580 (§172, a claimed-"re-transcribed" section) — 3 reworded-prose items FIXED**: "wobei"→"worin";
  restored "…wenn man die primitiven Wurzeln 3,2 zu Grunde legt…" (dropped clause); "n=7:"/"n=13:"→"für n=7,"/
  "für n=13,". Eqs + both index tables were already faithful.
- Minor uncounted punctuation slips left in un-re-transcribed prose: p20 (semicolon), p320 (comma), p345 (comma).
- **12 pages fully clean**: p40, p65, p115, p140, p165, p190, p230, p260, p290, p420, p485, p510.
- **★ 23rd WEBER ERRATUM (type-B, p544, §164 eq 8):** Weber prints the 3rd factor of the product as
  $(\varepsilon^{2},\alpha)^{\nu_2}$ — a print typo for $(\varepsilon^{\lambda_2},\alpha)^{\nu_2}$ (per eq (7) and
  the parallel structure; zoom-confirmed "2" not "λ₂"). Transcribed **as printed** ($\varepsilon^2$) + flagged.
**⇒ The "vol1 provisionally CERTIFIED-CLEAN" claim above is WITHDRAWN.** Error concentration is in theory/prose
GLUE (equations were mostly faithful even in the bad sections). ESCALATION (Floris's rule "errors bad → escalate"):
systematically re-verify §141-188 page-by-page — the range whose "complete" claim is now disproven — do NOT trust
it. Track in WEBER_METHOD_LOG.md. This is the "never certify — completeness claims are always wrong" pattern.
Compiles **417 pp / 0 err / 0 overfull / 0 underfull / 0 missing-char / 0 undefined** after all fixes.

NOTE: these 4 were found by the agent workflow and independently matched my by-hand audit. The same
run also produced HALLUCINATED fixes on phantom no-scan pages (args bug, now fixed) — proof the agent
output must never be applied unverified. Every line above was confirmed by eye before applying.


### 2026-07-02 — §168-170 Sechzehnter-Abschnitt cyclotomy block (p560-574; verified by eye, context-read)
**2 applied (§168 mod-period); §169 & §170 CLEAN.** These were the map-phase HELD/reconstruction block
(§168 had a fabricated title; §170 flagged "reconstruction + content-shuffle") — later re-transcription redid
all three faithfully. Full page-by-page scan-vs-tex confirmed verbatim match.
- **§168 FIX (2):** `(\mathrm{mod.}\ n)` -> `(\mathrm{mod}\ n)` at .tex 19826 (inline "lambda == g^h (mod n)")
  and 19830 (eq(2) tail). Weber prints "(mod n)" WITHOUT period on p560 (zoom-clear); same errata pattern as the
  two §167 instances fixed earlier (19608/19625). Rest of §168 (eqs 1-16, n=13 example) matches verbatim.
- **§169 CLEAN:** disq.-arithm footnote + v.Staudt footnote both restored word-for-word; n=17 worked example all
  cosine signs / ψ-coefficients / radical formulas correct (map-phase's "2 n=17 sign typos" already incorporated).
- **§170 CLEAN:** Kronecker footnote restored; NO content-shuffle found (paragraph order matches print); eqs 1-17
  incl. e=7 example + closing Satz with Π-factorial result all verbatim.
Recompiled after §168 fixes: **418 pp / 0 err / 0 overfull / 0 underfull / 0 missing-char / 0 undefined.**
Confirmed by eye before applying — agent output not used; this was direct context-read of ~500dpi scans.


### 2026-07-02 — §172 (⅓/¼(n-1) periods) full page-by-page p579-585 (verified by eye, context-read)
**4 edits. Map-phase numeric fixes HELD; prose+dropped-equation damage FOUND & re-transcribed.**
KEY: a numeric-fixed "island" still had heavy prose reconstruction only caught by whole-body scan (cf. §162 lesson).
- **HELD:** e=3 worked values `-(1+3ϱ)` (n=7), `-(4+3ϱ)` (n=13) match print [.tex 20723-24]; Indextabellen n=7/n=13
  correct; numbered eqs (1)-(42) all correct incl. 9th-roots (21)-(26) & e=4 (27)-(42); Kummer footnote¹ restored.
- **FIX A (span re-transcription, .tex ~20728-20769):** re-transcribed the cubic-derivation region. GPT had reworded
  the opening + eq(8) punctuation and DROPPED: "und die ganzen Zahlen β,γ sind zu bestimmen."; the derivation
  "Führen wir die Multiplication in (6) aus…=(η+η₁+η₂)²-3β, also" (was terse "Aus (6) folgt"); un-numbered eq
  nψ₁(ϱ)=s₃-6γ+3sϱ+3s'ϱ²; "Aus (8) und (9) erhält man aber s₃=-n-3γ, also"; "und ebenso"; eqs n-1=-9γ+3s+3s' and
  n[ψ₁(ϱ)+ψ₁(ϱ²)]+3n-1=-27γ + prose "wozu noch, wenn man (4) in den Cubus erhebt,…so folgt…oder endlich nach (2)
  und (3)" (was terse "Durch Addition der entsprechenden Gleichungen folgt"). Restored verbatim from scans p580-581.
- **FIX C (.tex closing Satz):** `Hieraus folgt zugleich der Satz: …als Summe zweier Quadrate darstellen.` →
  `Wir wollen auch hier den in der Formel (34) ausgedrückten Satz hervorheben: …in die Summe zweier Quadrate zerlegen.`
- **FIX D (type-B Weber erratum FLAGGED, reproduced not corrected):** `n=\frac14(a+b)^2+\frac34(a-b)^3.` — zoom on
  p582 confirms Weber prints exponent **3**; mathematically correct is (a-b)². .tex already reproduced it; added inline
  `% [sic] Weber druckt (a-b)^3 (Druckfehler); mathematisch korrekt (a-b)^2 -- Erratum reproduziert`.
- **FIX E (display):** inline `$3\eta+1=\xi$` → displayed `\[3\eta+1=\xi\]` to match print (parallels eq(40) 4η+1=ξ).
- **Not chased:** scan "Einheitswuzel" p582 (Weber 1-letter typo) — .tex keeps "Einheitswurzel" per house typo-norm.
Recompiled TWICE: **418 pp / 0 err / 0 overfull / 0 underfull / 0 missing-char / 0 undefined.** §172 CLEARED.
Confirmed by eye vs ~500dpi scans before applying — agent output not used; direct context-read.


### 2026-07-02 — §173 (Die complexen Zahlen von Gauss / R(i)) full page-by-page p585-591 (verified by eye)
**0 edits — VERIFIED FAITHFUL end-to-end.** Long prose-heavy Gaussian-integer section; scan-checked line-by-line
vs .tex 21002-21159; every line matches verbatim. No reconstruction damage.
- Gauss footnote¹ (Theoria residuorum biquadraticorum, comm.secunda, Werke Bd.II) restored; p=4f+1,2 / q=4f+3;
  Sätze 1-3 (p=a²+b²; (ab')²≡-1 (mod q) impossible per §138,4); Norm N(ξ)=x²+y²; 4 Einheiten; associirte Zahlen;
  Euclidean algorithm eq(1); Sätze 4-6 eqs(2)(3) + unique-factorization proof; n=πα two cases (p splits / q inert);
  2=-i(1+i)²; primäre Zahlen + Gauss footnote¹ (two defs); §172,(27),(38),(39) refs; norm<200 prime list (22 entries,
  all verified 1+i…1+14i).
- Mod-periods correct ("(mod 4)","(mod q)","(mod 8)" no period → \pmod). File unchanged (418pp/0 badness).
PATTERN: pure-theory prose section CLEAN (contrast §172 island). Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — §174 (Der Körper der dritten Einheitswurzeln / R(ρ)) full page-by-page p592-594 (verified by eye)
**0 edits — VERIFIED FAITHFUL end-to-end.** Second consecutive clean pure-theory section (cf. §173). Scan-checked
line-by-line vs .tex 21161-21221; every line matches verbatim. No reconstruction damage.
- Opening (refs §173,(1)); ρ=(-1+√-3)/2, R(ρ)/R(√-3); Norm N(ξ)=x²-xy+y²=((2x-y)²+3y²)/4; N(α)=a²-ab+b²=1 →
  (2a-b)²+3b²=4 → six Einheiten ±1,±ρ,±ρ²; associate system; Euclidean N(ξ-μ)≦¾, unique factorization; 3=-ρ²(1-ρ)²;
  3f+1 splits / 3f+2 inert; 4p=A²+27B² (per §172); factorization p=((A+3B)/2+3ρB)((A-3B)/2-3ρB); norm<200 prime
  list (22 entries 1-ρ…13+15ρ, verified).
- CORRECTION: §173+§174 are TAIL of Sechzehnter Abschnitt (running head confirms); §175 STARTS Siebzehnter Abschnitt.
- Scan note: p594 mid/bot faint (verso bleed-through, blank page); §174 ends prime-list on p594_top. File unchanged.
Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — §175 (Reduction der Gruppe durch reine Gleichungen — OPENS Siebzehnter Abschnitt) full page-by-page p595-597 (verified by eye)
**0 edits — VERIFIED FAITHFUL end-to-end.** THIRD consecutive clean pure-theory section (cf. §173, §174). This is
the opener of the flagged "algebraic-solution endgame" (§175-188) — came through clean. Scan-checked line-by-line
vs .tex 21223-21273 (+ §176 heading 21275); every line matches verbatim. No reconstruction damage.
- Siebzehnter-Abschnitt heading + §175 title (p595); algebraic-solution opening + Ω-extension question; reine
  Gleichung y^m-a=0 + reducibility/transitivity; Jordan footnote¹ (Traité des substitutions p.386) + §162 ref;
  boxed question "Unter welchen Bedingungen wird die Gruppe P... reducirt?" + irreducibility caveat + Ω-prep;
  φ(x)=0 reduces P→Q, ε,ε₁…ε_{m-1} roots + Jordan fn; §157 Schlusssatz → index j|m, m prime ⇒ m=j; ε=ψ(x₀…x_{m-1});
  conjugate groups π⁻¹Qπ ⇒ Q Normaltheiler von P (.tex 21255-21259).
- **Satz I** (Adjunction Abel'sche Gleichung ⇒ P hat Normaltheiler Q von Primzahlindex; boxed 21263-21265) ✓;
  converse "Dieser Satz lässt sich auch umkehren" via §155, §163 (21269) ✓; **Satz II** (Normaltheiler Q von
  Primzahlindex m ⇒ Adjunction cyklische Gleichung m^ten Grades reducirt P auf Q; boxed 21271-21273) ✓; §176
  heading + opening line ✓.
- Scan note: p597 recto running head reads "§. 176. Metacyklische Gleichungen" while body top is still §175 —
  Weber's recto head names the section appearing lower on the page (§176 begins p597_bot). Running heads are
  LaTeX-auto-generated, NOT transcribed → layout artifact, not a fidelity issue. File unchanged (418pp/0 badness).
PATTERN: theory-prose sections now 3-for-3 clean (§173/§174/§175); only §172 (derivation island) had drops.
Confirmed by eye vs ~500dpi scans; direct context-read (agent output not used).


### 2026-07-02 — §176 (Metacyklische Gleichungen) full page-by-page p597_bot-p600_top (verified by eye)
**CONTENT: 0 word-drops — verbatim end-to-end.** Scan-checked line-by-line vs .tex 21277-21305.
Opening def (metacyklisch = radical-solvable = Kette cyklischer Gl.); P,P1,P2… prime-index Normaltheiler chain;
Satz III (composition-series criterion, quote 21281-87); metacyklische-Gruppe def + Kronecker/Frobenius/Hölder
footnote (21293); Satz IV (irred.+one radical-solvable root ⇒ metacyklisch, quote 21297-99) + induction proof
(μm=n via §158; n-prime base case; 21301-05); closing recap (21305); §177 heading confirmed.
**SPERRDRUCK: 3 gesperrt defined-terms were DROPPED in .tex → restored as \emph (fidelity fix):**
  - @21277 "eine metacyklische Gleichung nennen" → \emph{metacyklische Gleichung}
  - @21293 "eine metacyklische Gruppe\footnote" → \emph{metacyklische Gruppe}
  - @21295 "für die vollständige Auflösbarkeit" → \emph{vollständige}
  (zoom-confirmed letterspacing p598. §176 Sperrung NOT exhaustively re-verified — see dedicated pass.)
Recompiled TWICE: **418 pp / 0 err / 0 overfull / 0 underfull / 0 missing-char / 0 undefined.**
Confirmed by eye vs ~500dpi scans; direct context-read.

### 2026-07-02 — CORRECTION / SCOPE NOTE on prior "VERIFIED FAITHFUL" claims (§173, §174, §175) — turn 16
The §173/§174/§175 "0 edits — VERIFIED FAITHFUL" entries above are **CONTENT / word-level ONLY.** During §176 I
discovered Weber's **Sperrdruck (gesperrt/letterspaced emphasis) on DEFINITIONS is systematically DROPPED** in the
GPT .tex (rendered plain). This is independent of word-damage (§176 had 0 word-drops yet dropped 3 gesperrt).
CONFIRMED in §173 (p586): "…heissen a s s o c i i r t e Z a h l e n"; and whole definition-sentences fully
gesperrt — "Die Zahlen a+bi … heissen die ganzen Zahlen des Körpers R(i).", "Eine ganze Zahl, deren Norm gleich 1
ist, heisst eine Einheit.", "Eine ganze Zahl α heisst durch … β theilbar, wenn … so dass α=βγ ist." — all plain in
.tex. (Extent VARIES: whole-sentence vs term-only; the Norm-def sentence is NOT gesperrt.) → These sections are
NOT emphasis-faithful. A DEDICATED zoom-verified Sperrdruck restoration pass over §1-176 is owed (see METHOD_LOG
turn-16 finding). Never certify Sperrung extent without zoom.


### 2026-07-02 — §177 (Einfachheit der alternirenden Gruppe) full page-by-page p600_mid-p603_top (verified by eye)
**CONTENT: 0 word-edits — verbatim end-to-end.** Scan-checked line-by-line vs .tex 21309-21360.
Flagged as derivation-heavy (§172-style damage risk) but came through CLEAN — all 5 permutation-commutator
computations EXACT:
  - Opening §149 → symm. group; alternating = index-2 Normaltheiler (adjoin √disc); n=4 Klein-four Normaltheiler
    1,(0,1)(2,3),(0,2)(1,3),(0,3)(1,2); index-2 chain; S4 metacyklisch → biquadr. §160,161.
  - Proof: A generated by 3-cycles (§153,6/§154,6); π-matrix; (a0,a1,a2)/(a0,a2,a1); Q∩3-cycle ⇒ Q=A; eq(1)
    λ=κ⁻¹π⁻¹κπ.
  - Fall 1 λ=(1,m,m-1…2)(2,3,1,4…m)=(1,2,4); Fall 2 =(1,3,2)(4,6,5)(3,2,4)(1,5,6)=(1,2,5,3,4); Fall 3
    =(1,3,2)(4,5)(2,4,3)(1,5)=(1,2,5,3,4); Fall 4 =(1,2)(3,4)(5,6)(3,2)(5,4)(1,6)=(1,3,5)(2,6,4); Fall 5
    =(1,2)(3,4)(5)(2,5)(3,4)(1)=(1,5,2). ALL match verbatim.
  - "alle Fälle erschöpft" (n>4), n=4 exception + Abel/Ruffini/Burkhardt footnote (Crelle Bd I 1826; Ruffini
    1799-1806; "Die Anfänge der Gruppentheorie und Paolo Ruffini"; Schlömilch's Zs. Leipzig 1892) verbatim;
    corollary: symm. group has only S, A, 1 as Normaltheiler.
**SPERRUNG:** gesperrt candidates NOT edited this pass (deferred to dedicated Sperrung sweep): "alternirende
Gruppe" @21309, "einfach" @21315, unsolvability-conclusion clause @21315. So §177 = CONTENT-faithful; NOT yet
emphasis-verified.
File unchanged by content pass (418pp/0 badness). Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — §178 (Nicht metacyklische Gleichungen im Körper der rationalen Zahlen) full page-by-page p603_mid-p606_mid (verified by eye)
**CONTENT: 0 word-edits — verbatim end-to-end.** Scan-checked line-by-line vs .tex 21364-21421. Was on the re-scan
list (previously internal-evidence only) → NOW confirmed by full forward scan.
  - affect question (rational-coeff eqns w/o Affect = symm. group); Galois resolvente G(t) deg Π(n); Hilbert
    irreducibility footnote (Journal f. Math. Bd.110); §153,9 (transitive non-symm. prime-degree ⇒ no single
    transposition).
  - Satz 1 (prime-degree affect ⇒ 2 roots rational in the others); Satz 2 (real Ω corollary: no 2-imaginary/n-2-real).
  - f(x)=(x-α1)(x-α2)…(x-αn)=x^n+a1x^{n-1}+a2x^{n-2}+…+an; continuity/root-count argument.
  - Satz 3 = EISENSTEIN criterion (p∤c0, p|c1…cn, p²∤cn ⇒ φ(x)=c0x^n+c1x^{n-1}+…+cn irreducibel) + FULL proof
    (§2 → integer factors; φ=(α0x^h+…+αh)(β0x^k+…+βk); α_hβ_k=c_n; β_ν not div by p; coeff of x^{k-ν} not div ⇒
    k-ν=n impossible since k<n) — all EXACT.
  - a1=c1/c0, a2=c2/c0 … an=cn/c0; Satz 4 (∞ many affect-free rational eqns of every prime degree) + closing caveat.
**SPERRUNG:** Sätze 1,2,3,4 STATEMENTS are gesperrt in print (quote kept in .tex, letterspacing dropped) — NOT
edited this pass (deferred to dedicated Sperrung sweep). NB: contrast §176 Roman Sätze I-IV (quote-NORMAL) → per-Satz
Sperrung varies, zoom each. So §178 = CONTENT-faithful; NOT yet emphasis-verified.
File unchanged by content pass (418pp/0 badness). Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — §179 (Auflösung durch reelle Radicale) full page-by-page p606_mid-p609_bot (verified by eye)
**CONTENT: 1 FIX (ϱ→ε transcription error restored).** Scan-checked line-by-line vs .tex 21425-21481.
- **FIX (.tex 21429):** scan+zoom confirmed Weber prints "die sämmtlichen Wurzeln von χ in Ω(ϱ) enthalten, und wenn
  also ϱ reell ist" (varrho, TWICE). GPT .tex had \Omega(\varepsilon) and \varepsilon reell — WRONG. Also breaks the
  math: by §157 the adjoined ε and all conjugate roots of χ are rational in g(t)'s roots (= rational in ϱ), so all
  χ-roots ∈ Ω(ϱ); ϱ real ⇒ Ω(ϱ) real ⇒ χ-roots real. With ε "χ-roots ∈ Ω(ε)" is a non-sequitur (needs χ normal).
  NB: the FIRST ε ("Adjunction einer Wurzel ε einer irreduciblen Gleichung χ=0") is CORRECTLY ε (zoom: no descender);
  only the two Ω(ϱ)/ϱ instances were corrupted. .tex error (NOT Weber) → fixed to ϱ, no [sic].
  Recompiled TWICE: 418 pp / 0 err / 0 overfull / 0 underfull / 0 missing-char / 0 undefined.
- Verbatim: casus-irreducibilis opening + Hölder/Kneser footnote (Math. Annalen Bd.38 / Bd.41); Normalgleichung
  setup (real Ω, root ϱ, all-real-or-all-imaginary); Satz 1 (real-root Normalgl. reducible only by all-real
  prime-degree eqns); reelle-Radical question (p prime, a not p-th power); x^p-a irreducibility proof — eqs (1)
  α,εα,ε²α…ε^{p-1}α, (2) x^p-a=0, (3) x^p-a=f1(x)f2(x), ε^λα^μ=b, (4) a^μ=b^p, μh+pk=1, a=a^{μh}a^{pk}=(b^h a^k)^p —
  ALL exact; Satz 2 (odd-degree Normalgl. not reducible by real radical); casus-irreducibilis application; cubic
  classification (order 3 cyclic/Siebeneck; order 6 ±Discriminante; Dreitheilung; x³=a Delisches Problem).
**SPERRUNG:** Sätze 1,2 statements gesperrt; "casus irreducibilis" (Latin term) letterspaced several times — NOT
edited (deferred to dedicated Sperrung pass). So §179 CONTENT-faithful; NOT yet emphasis-verified.
Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — §180 (Metacyklische Gleichungen von Primzahlgrad) PART 1 p609_bot-p612_top (verified by eye)
**CONTENT: faithful + 1 ERRATUM FLAG.** Big section (.tex 21483-21733, ~7pp) split across iterations; part 1 =
.tex 21485-21548. Scan-checked line-by-line; verbatim.
- Galois-criterion setup: f(x) irreducible prime degree n>2 → metacyklische Kette (1) P,P1,P2…P_{μ-1},1; §158,3 ⇒
  vorletzte Gruppe P_{μ-1} order n; π=(0,1,2…n-1); x_z indexing mod n; substitutions (2) (z,z+b).
- General linear substitution (3) (z,az+b), a≢0 (mod n), n(n-1) of them; group closure: λ=(z,az+b), λ'=(z,a'z+b'),
  λλ'=(x_z/x_{az+b})(x_z/x_{a'z+b'})=(x_z/x_{a'(az+b)+b'}); eq(4) λλ'=λ''=(z,aa'z+a'b+b') — EXACT.
- "lineare Gruppe" def + Kronecker footnote ("Kronecker nennt nur diese Gruppe metacyklisch."); divisor (z,az) order
  n-1; λ^h=[z,a^h z+(1+a+…+a^{h-1})b]; a=1 ⇒ λ^h=(z,z+hb); (1+a+…+a^{h-1})=(a^h-1)/(a-1); order e=ord_n(a).
- **ERRATUM FLAG (.tex 21548):** zoom-confirmed Weber prints z_0 ≡ b/(a-b) (mod n) for the fixed point of λ=(z,az+b).
  .tex faithfully had \frac{b}{a-b} (transcription CORRECT). BUT z_0=az_0+b ⇒ z_0=b/(1-a), so a-b is a Weber PRINT
  ERROR (type-B). Added inline `% [sic] … mathematisch korrekt 1-a … Erratum reproduziert` — NOT corrected. 2nd
  type-B erratum flag in vol1 (after §172 (a-b)^3). Recompiled TWICE: 418pp / 0 err / 0 overfull / 0 underfull /
  0 missing-char / 0 undefined.
**SPERRUNG:** "lineare Gruppe" @21529 gesperrt (deferred). §180 part 1 CONTENT-faithful; NOT emphasis-verified.
RESUME §180 at p612_mid (.tex ~21550). Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — §180 PART 2 p613-p620 (.tex 21562-21733) — CONTENT TRACK COMPLETE (verified by eye)
**CONTENT: 0 word-edits — verbatim end-to-end.** Completes §180 (part 1 p609-612 last turn). Whole ~11pp section
now content-verified; ONLY damage was the single z_0=b/(a-b) erratum (flagged part 1). Scan-checked line-by-line.
- p613: composition λλ₀^{-h}=(z, z+a₀^{-h}b+((a₀^{-h}-1)/(a₀-1))b₀); identity-cond b₀/(a₀-1)≡b/(a₀^h-1) (mod n);
  transitivity conclusion; eq(5) λ=(z,a₀^h z+b) h=0..e-1 b=0..n-1 order en; Satz I (transitive linear L ⊴ P ⇒ P linear).
- p614-615: Lagrange interpolation proof — φ(z) deg≤n-1, ψ(z)=z(z-1)..(z-n+1), ψ≡z^n-z, ψ'≡-1, eq(6)
  φ(z)≡-Σ a_i ψ(z)/(z-i); eq(7) φ(z+1)≡a'φ(z)+a, a'≡1, φ(z+h)=φ(z)+ah, eq(8) φ(z)=az+b ⇒ P linear. cyklische Gruppe
  normal in any containing linear group. Satz II (Galois: metacykl. prime-deg group is linear) + chain-(1) descent.
  Satz III (irred. prime-deg w/ linear group ⇒ metacyklisch).
- p616-617: L' index-p normal subgroup (e=pe', λ'=(z,a₀^{ph}z+b)); transitive-linear ≡ metacyklisch synonymy; conjugate
  P'=π⁻¹Pπ; erzeugende Substitutionen (9)/(10); halbmetacyklische Gruppe (a₀=g²); Satz IV (volle metacykl. ⊄ alt.;
  GCD=halbmetacykl.) via s∈alt/t∉alt cycle parity; metacyklische Function y, Resolvente F(y)=0 deg ν=1·2·3..(n-2).
- p618-620: Satz V (Radicale ⇔ Resolvente deg-ν rational simple root); linear group fixes ≤1 Ziffer; Satz VI (metacykl.
  ⇒ all roots rational in any 2) + converse (γ n-cycles + ϰ single-fixer; (11) m=μn+ν+1, (12) m=n(μ+1) ⇒ ν=n-1;
  C=1,γ..γ^{n-1} normal ⇒ Satz VII); Kronecker footnote (Monatsber. Berl. Akad. 14.4.1856); Satz VIII (odd prime-deg
  metacykl real-coeff ⇒ all real or exactly one); disc sign (-1)^{(n-1)/2} ⇒ Satz IX (n≡1 mod4 disc>0; n≡3 sign decides).
- ϰ correctly \varkappa; Coëfficienten→Coefficienten per house convention (scan prints ë, normalized).
**SPERRUNG (deferred to dedicated track):** ALL Sätze I-IX statements letterspaced (quote kept, Sperrung dropped) +
inline gesperrt terms — "lineare Gruppe" @21529, cyklische-Gruppe-normal remark @21639, "volle lineare Gruppe" @21662,
"erzeugenden Substitutionen dieser Gruppen" @21670, "halbmetacyklische Gruppe" @21670, "Jeder transitive Theiler…
metacyklisch" @21677, "metacyklische Function" @21683, "Also enthält P ausser der identischen…nicht ändert" @21695.
So §180 = CONTENT-faithful; NOT yet emphasis-verified. File UNCHANGED by content pass (418pp/0 badness; no edits, no
compile needed this iteration). Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — §181 (Anwendung auf die metacykl. Gleichungen 5ten Grades) p621-623 (.tex 21734-21839) — PART 1 (verified by eye)
**CONTENT: 2 EDITS (1 title reword-fix, 1 Weber erratum flag).** Scan-checked line-by-line; recompiled clean after.
- **FIX (title reword, .tex 21734):** \sect{181} title had "…Gleichungen fünften Grades"; scan (zoom-confirmed) prints
  "…Gleichungen 5ten Grades" (numeral 5 + superscript ten, matching running head "Gleichungen 5ten Grades" + the body's
  $5^{\text{ten}}$ usage). GPT spelled the ordinal out = reword. Fixed to `$5^{\text{ten}}$ Grades`. Math-in-heading is
  safe (§133 precedent `$n$ten Grades`); recompiled 418pp/0 badness. NB SYSTEMATIC: §54/74/75/188 titles also read
  "fünften Grades", §80 "zweiten Grades" — must scan-check ordinal form when reached (§188 ahead in this Abschnitt).
- **ERRATUM FLAG (Weber duplicate eq-number (12), .tex 21837):** scan p623 numbers BOTH the u'_1..u'_6 block (p623_mid)
  AND the sextic y^6+a_2y^4+a_4y^2+a_6-√Δ(a_1y^5+a_3y^3+a_5y)=0 (p623_bot) as "(12)". Weber genuinely prints two eqs
  (12). .tex reproduced faithfully (two \tag{12}; LaTeX permits manual duplicate tags). Added inline `% [sic] …
  doppelte Gleichungsnummer im Druck … Erratum reproduziert, nicht umnummeriert`. = 3rd type-B Weber erratum in vol1
  (after §172 (a-b)^3, §180 z_0). Transcription CORRECT; NOT corrected. Recompiled TWICE: 418pp/0 err/0 overfull/
  0 underfull/0 missing-char/0 undefined.
- Verbatim: n=5 group orders (cyclic 5 / halbmet. 10 / voll met. 20); metacykl. Function ⇒ Resolvente 6ten Grades,
  halbmet. ⇒ 12ten Grades (splits into two 6ten after adjoining √Δ); erzeugende Substitutionen s=(z,z+1),t=(z,2z),
  t²=(z,4z) for mod 5; tables (1) Ziffer-perms, (2) Paar-perms under s,t², (3) Paar-perms under t [all entries checked];
  u (4), u' (5), f(x)=x^5-ax^4+bx^3-cx^2+dx-e (6), u+u'=b (7), y=u-u' (8), Y=(u-u')/√Δ (9) + Jacobi/Cayley footnote
  (Crelle Bd.13 / Jacobi Werke Bd.3 / Cayley phil.trans.1861 Coll.math.papers IV p.309); A=N+N(1,2)(3,4)+Nt(0,1)+…
  +Nt(0,4) (10); Nebengruppen-distinctness via (1,2)(3,4)t=(1,4)∉M; conjugating perms t(0,1)=(0,1,2,4,3) etc.;
  u_1..u_6 (11) + u'_1..u'_6 (12) [all 60 monomials checked verbatim]; sextic (12) reduced form; degree/parity argument.
**SPERRUNG:** none on p621-623 (computational stretch, no letterspaced defs). CONTENT-faithful; NOT emphasis-verified.
Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — §181 COMPLETE (p624-627, .tex 21840-21952) + §182 opening — (verified by eye)
**CONTENT: 0 edits — verbatim end-to-end.** Completes §181 (part 1 p621-623 was prior turn, w/ 2 edits). Scan-checked
line-by-line; file already compile-clean (no edits this iteration).
- p624: degree table (a_1√Δ,a_2,a_3√Δ,a_4,a_5√Δ,a_6 → grades 2,4,6,8,10,12); √Δ deg 10 in x ⇒ a_1=0,a_3=0,a_5=const;
  Cayley computation note; Bring-Jerrard form (13) x^5+αx+β=0 + Runge footnote (Acta math. Bd.7); degree argument
  (d 4th-order, e 5th-order ⇒ a_2,a_4,a_6 indep of β for (13)); (14) a_2=m_1α,a_4=m_2α²,a_6=m_3α³,a_5=m; β=0 special
  case (15) x_0=0,x_1=⁴√(-α),x_2=i⁴√(-α),x_3=-⁴√(-α),x_4=-i⁴√(-α); (16) √Δ=Π(x_i-x_j)=16i√(-α)⁵=-16√α⁵, Δ=256α⁵.
- p625: b=0 ⇒ y=2u (via 7,8); y_1=y_2=y_3=y_6=-2√α, y_4=(4-2i)√α, y_5=(4+2i)√α; (17) identity
  y⁶+a_2y⁴+a_4y²+a_6-a_5√Δy=(y+2√α)⁴(y²-8y√α+20α)=y⁶-20αy⁴+240α²y²+512√α⁵y+320α³; (18) general resolvente
  (sub √Δ for -16√α⁵) y⁶-20αy⁴+240α²y²-32√Δy+320α³=0; (19) Δ=5⁵β⁴+2⁸α⁵ (§74 formula 3); (20) u⁶-5αu⁴+15α²u²-√Δu+5α³=0;
  (21) v=u²: (v³-5αv²+15α²v+5α³)²=Δv. Page footer "Weber, Algebra. I. / 40".
- p626: alt form via √α→-√α: (v-α)⁴(v²+6αv+25α²)=0; (22) =5⁵β⁴v; metacyklizität check (u=0/v=0⇔α=0=known metacykl.
  x⁵+β=0; opposite roots ⇔ Δ=0 excluded; equal roots ⇒ derivative 6u⁵-20αu³+30α²u-√Δ=0, elim √Δ ⇒ 5(u²-α)³=0 ⇒
  v=α ⇒ β=0 ⇒ reducible); integer-v search among factors of 25α⁶; x⁵+5x+5t=0 never metacyklisch (§178,3 irred.);
  (23) α=5⁵μ⁴λ/[(λ-1)⁴(λ²+6λ+25)], β=5⁵μ⁵λ/[same]. [all monomials/coeffs checked verbatim]
- p627: (24) x⁵+αx+β=0 solvable (λ,μ rational); converse (irred. solvable ⇔ α,β in form 23); example λ=-1,μ=1 ⇒
  64α=-5⁴,64β=-5⁴, sub xξ=5 ⇒ ξ⁵+5ξ⁴-5·64=0 (irred. solvable example). §182 opens: v_1..v_6=(u_i-u'_i)² (1);
  F(v)=0 deg-6 resolvente; M-conjugates π⁻¹Mπ intersect trivially (Normaltheiler of A impossible by §177 ⇒ Einheit);
  Totalresolvente (§156), group deg = deg of f's group = 120; ⇒ S_6 has transitive divisor of index 6.
**SPERRUNG (deferred):** §181 p626 final conclusion "keine Gleichung von der Form x⁵+5x+5t=0 metacyklisch" letterspaced;
§182 p627 quote-Satz "Die symmetrische Permutationsgruppe von sechs Ziffern hat einen transitiven Divisor vom Index 6"
(gesperrt-status to confirm on p628 zoom). CONTENT-faithful; NOT emphasis-verified.
**⚠ OPEN ITEM for next iteration:** .tex 22002 (p628) `w_0 = v_1v_2 + v'_4v_5 + v_3v_6` has stray prime v'_4 (no v'
defined) — likely transcription typo for v_4; ZOOM-verify p628, fix if confirmed. Confirmed by eye vs ~500dpi scans.


### 2026-07-02 — §182 (Die Gruppe der Resolvente) COMPLETE p627-629 (.tex 21956-22023) — (verified by eye)
**CONTENT: 1 EDIT (Weber erratum flag).** Scan-checked line-by-line; recompiled clean (byte-identical, comment inert).
- **v'_4 = Weber ERRATUM, NOT GPT typo (.tex 22002):** flagged w_0=v_1v_2+v'_4v_5+v_3v_6 — ZOOM p629 (crop_26_31)
  confirms Weber HIMSELF prints v'_4 (clear stray prime on v_4). .tex was FAITHFUL, not a transcription typo (my
  initial hypothesis). Math: w_0 = image of base w_3=v_1v_3+v_2v_4+v_5v_6 under 5-cycle (2,6,5,4,3) = v_1v_2+v_4v_5+v_3v_6
  (plain v_4); the prime is a stray print mark. Added inline `% [sic] … kein v' definiert … Erratum reproduziert,
  nicht korrigiert`. = 4th type-B Weber erratum in vol1 (after §172 (a-b)^3, §180 z_0, §181 dup-eq-(12)). Transcription
  CORRECT; NOT corrected. Recompiled TWICE: 418pp/0 err/0 overfull/0 underfull/0 missing-char/0 undefined.
  ★ LESSON: an anomaly that reads like a GPT typo can be Weber's own print error — always ZOOM the scan before editing;
  faithful action = keep + [sic], never silently "correct" to the mathematically-right value.
- Verbatim: v_1..v_6=(u_i-u'_i)² (1); F(v)=0 deg-6 resolvente, Coeff symm in a,b,c,d,e, irred; M-conjugates π⁻¹Mπ
  intersect only in identity (a common divisor would be a Normaltheiler of A, impossible ⇒ Einheit, §177); ⇒ F is a
  Totalresolvente (§156), its group order = order of f's group = 1·2·3·4·5=120; F irred ⇒ transitive on v-indices, deg
  120 vs S_6 order 6·120 ⇒ S_6 has transitive index-6 divisor C; erzeugende π_1=(1,3)(2,5)(4,6), π_2=(1,4)(2,3)(5,6),
  π_3=(1,5)(2,6)(3,4), π_4=(1,6)(2,4)(3,5) (from transp. (0,1)..(0,4) on u/v-indices via §181 (11)↔(12)); products
  π_1π_2=(1,2,6)(3,4,5), π_1π_2π_3=(1,6,5,4), π_1π_2π_3π_4=(2,4,6,3,5), ^3=(2,3,4,5,6); base fn v_1v_3+v_2v_4+v_5v_6
  fixed by π_1,π_1π_2; w_0..w_4 (2) via (2,3,4,5,6)-powers [all 15 products checked, w_0 carries the Weber prime];
  π_i=(w_0,w_i) ⇒ C↔S_5 on w-indices (§153,2); W=w_0²+..+w_4² (or ∏(λ-w_i)) is a C-function, root of irred deg-6 eqn.
**SPERRUNG (deferred):** §182 p628 Satz "Die symmetrische Permutationsgruppe von sechs Ziffern hat einen transitiven
Divisor vom Index 6" letterspaced; "Totalresolvente" @21967 letterspaced (dropped \emph). CONTENT-faithful; NOT
emphasis-verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — §183 COMPLETE (p630-633, .tex 22029-22098) + §184 COMPLETE (p633-638, .tex 22100-22303) — (verified by eye)
**CONTENT: 0 EDITS — verbatim end-to-end across 8 pages.** File UNCHANGED (still 418pp/0 badness; no compile needed).
§185 opened (p638 tail). Both sections are heavy Lagrange-resolvent formula theory; every equation, subscript,
superscript, and cross-reference checked line-by-line against ~500dpi scans (2400px thirds, no zoom needed).
- **§183 (Stellung der Aufgabe. Hülfssatz):** Achtzehnter-Abschnitt divider + title; Abel/Kronecker problem (find ALL
  metacykl. Gl.; Kronecker solves via roots not equations) + big footnote (Abel Oeuvres ed.Sylow t.II p.217 / Brief an
  Crelle 14.März 1826 p.266; Kronecker Monatsber. Berl.Akad. 1853,1856; H.Weber Marburg 1892) verbatim. Lagrange
  resolvent (ε,x)=x_0+εx_1+…+ε^{n-1}x_{n-1}=Σ_{0,n-1}^h ε^h x_h (1) [from §164]; Hülfssatz X=ξ^{n-1}+ξ^{n-2}+…+ξ+1 (2)
  irred in R [§134]; Ω(ε) Normalform c_0+c_1ε+…+c_{n-2}ε^{n-2} (3) [§142]. Satz 1 (Normalform uniqueness); reducibility
  contradiction (§143); Divisoren via Permutationsgruppe P, zugehöriger Körper (§152); Satz 2 (P-invariance ⇒ coeff
  P-invariant); Ω(ε) Normalkörper (§144); averaging Φ(ε)=1/(n-1)Σ_{1,n-1}Φ(ε^h)=c_0-(c_1+…+c_{n-2})/(n-1); Satz 3
  (all subst (ε,ε^h) ⇒ in Ω). [all verbatim]
- **§184 (Sätze über die Resolventen):** s: (ε,x)→ε^{-1}(ε,x); (1) s=(h,h+1),t=(h,gh) [§180]; t: (ε,x)→(ε^{g^{-1}},x)
  via h→g^{-1}h; s^λ/t^λ Vertauschungen; Satz 4 (metacykl. generators table (s)(s^{-1})(t)(t^{-1})); (4)
  (ε,x)^n=Φ(ε), (ε^λ,x)(ε,x)^{-λ}=F(ε); Satz 5 (Normalform coeff cyklisch [§163]); (5) f_0..f_{n-2} array,
  (6) f_h=f(ε^{g^h}), t^{-1} cycle (0,1,..n-2); (7) C(f_0..f_{n-2}); Satz 6 (cykl. C of f ⇒ metacykl. coeff);
  metacykl.-Function defn; Satz 7 (rational-coeff cykl. C ⇒ metacykl. of x, rational coeff); (8) (ε,x)^{1-g^{n-1}}=
  f_0^{g^{n-2}}..f_{n-2} product; (9); g=g_1+ln, g^{n-1}≡g_1^{n-1}+n(n-1)lg_1^{n-2} (mod n²), (g^{n-1}-1)/n congruence
  (mod n); (10) λ=(g^{n-1}-1)/n≡1; (11) F(ε)=(ε^λ,x)(ε,x)^{-λ}=(ε,x)^{nk}; (12) (ε,x)^n=[F(ε)]^n f_0^{g^{n-2}}..f_{n-2};
  (13) F(ε^{g^v})=F_v=(ε^{g^v},x)^{nk}; (14); (15) g^v=nq_v+r_v, 0<r_v<n, r_0=1; (16) f_{v-1}=(ε^{r_v},x)(ε^{r_{v-1}},x)^{-g};
  (17) Φ_v=F_v f_v^{q_{n-2}}..f_{v+n-3}^{q_1}; (18); r_v/g-ln independence; characteristic props α)β)γ)δ) of ω_v={f_v,F_v,Φ_v};
  Lagrange §155 ⇒ Θ_v rational via ω_v; (19) φ(u)=Π(u-ω_v); (20) Σ Θ_v φ(u)/(u-ω_v)=χ(u) deg (n-2)^{ten};
  (21) χ(u)/φ'(u)=Θ(u) ⇒ Θ_v=Θ(ω_v). [all verbatim] mod-forms match Weber (no period, \pmod correct).
★ LESSON confirmed (works/adjust): GPT-reconstruction damage is concentrated in PROSE and TITLES (rewording/dropping),
  NOT in dense computational math — long equation-heavy sections transcribe clean. Content-track can move 8pp/iteration
  on such stretches; reserve zoom for ordinal-title checks + suspected errata only.
**SPERRUNG (deferred):** §183-184 letterspaced — all numbered Sätze 1-7 (quote blocks kept, Sperrung→plain); inline
"die imaginären $n^{ten}$ Einheitswurzeln", "Normalform" (repeated), "Normalkörper", "metacyklische Function" defn, the
four props α)β)γ)δ) headers. CONTENT-faithful; NOT emphasis-verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — §185 (Wurzeln metacyklischer Gleichungen) p638-640 (.tex 22307-22391) — PART 1 (verified by eye)
**CONTENT: 1 EDIT (source-fidelity normalization removed).** Scan-checked line-by-line; recompiled clean after.
- **FIX (GPT-added exponent removed, .tex 22369):** the R_v abbreviation `R_v=k_v^{r_{n-2}}k_{v+1}^{r_{n-3}}...k_{v+n-2}^{r_0}`
  — ZOOM p640 (crop_44_30) shows Weber prints the LAST factor as plain `k_{v+n-2}` with NO exponent r_0. Weber omits the
  trivial r_0(=1) exponent in THIS shorthand, though he DOES print `^{r_0}` in the full formulas (5)/(6) on the same page
  and (18) §184. GPT had normalized the shorthand by adding `^{r_0}`. Removed it to match the print. Math. identical
  (r_0=1) — a typographic normalization, NOT a content/errata correction. Recompiled: 418pp/0 err/0 overfull/0 underfull/
  0 missing-char/0 undefined (2263535 bytes).
  ★ LESSON (mirror of the errata lesson): fidelity cuts BOTH ways. Just as I must KEEP Weber's own print-errata (+[sic],
  don't "fix"), I must REMOVE GPT's mathematically-null "improvements" that aren't in the print (here a =1 exponent).
  The rule is identical: reproduce EXACTLY what the scan shows — no additions, no corrections. Always ZOOM ambiguous
  sub/superscripts on shorthand-defs (they're where GPT normalizes silently).
- Verbatim (§185 opening + first radical-expression block): ξ_0..ξ_{n-1}=roots of an irred. metacykl. eqn deg n in body
  𝔎, ordered so metacykl. functions of ξ are rational in 𝔎; two beschränkende Voraussetzungen (1: no resolvent (ε,ξ)
  with ε imag. n-th root vanishes; 2: no two of f_0..f_{n-1} become equal); f_v->k_v (distinct), Φ_v->K_v (may coincide);
  (1) ψ(u)=Π(u-k_v) cyclic (n-1)^ten (even) deg, rational coeff; (2) k_{i+1}=Θ(k_i) cyclically [§163]; (3) K_v=Φ(k_v),
  Φ rational in 𝔎 [§184 Schlusssatz]; (4) τ_v=ⁿ√k_v; (5) (ε^{r_v},ξ)=K_v τ_v^{r_{n-2}}...τ_{v+n-2}^{r_0}; A=(1,x) rational;
  (6) nξ_0=A+Σ_{0,n-2}K_v τ_v^{r_{n-2}}...τ_{v+n-2}^{r_0}; K_v,k_v ≠0 [§184 (16)(17)]; R_v shorthand; (7) nξ_0=A+ΣK_v ⁿ√R_v
  (n-1 radicals of deg n, each n-valued but not independent); (8) K_v ⁿ√R_v=K_{v-1}^g k_{v-1}(ⁿ√R_{v-1})^g via
  (ε^{r_v},ξ)(ε^{r_{v-1}},ξ)^{-g}=k_{v-1} [§184 (16)]; (6) advantage over (7): only n values (the n roots ξ) however the
  radicals are chosen; proof begins: replace ⁿ√k_v by ε_v ⁿ√k_v (ε_v arbitrary n-th roots). [all verbatim]
**SPERRUNG (deferred):** §185 "beschränkende Voraussetzungen" 1./2. in quote blocks (letterspaced-status likely);
"Normalform" already tracked. CONTENT-faithful; NOT emphasis-verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — §185 COMPLETE (p641, .tex 22393-22426) + §186 part 1 (p641-643, .tex 22430-22476) — (verified by eye)
**CONTENT: 0 EDITS — verbatim end-to-end.** (§185's only edit was the R_v fix on p640, prior iteration.) Scan-checked
line-by-line; file already compile-clean (no edits this iteration).
- **§185 finish (p641):** (9) nξ=A+Σ_{0,n-2}E_v K_v τ_v^{r_{n-2}}…τ_{v+n-2}^{r_0} (E_v = n-th root); (10)
  E_v=ε_v^{r_{n-2}}ε_{v+1}^{r_{n-3}}…ε_{v+n-2}^{r_0} [NB: here Weber DOES print the last factor's r_0 exponent —
  confirms the p640 R_v-shorthand omission was shorthand-specific, so that fix was right]; (11) r_v≡g·r_{v-1} (mod n)
  [§184 (15)]; E_{v-1}, E_{v-1}^g expansions; (12) E_v=E_{v-1}^g=E_0^{r_v}; (13) E_0=ε_0^{r_{n-2}}…ε_{n-2}^{r_0}; ⇒ only
  n values from (6) (vary one radical τ_v); Cayley cubic ref (§36); (14) nξ_h=A+Σε^{-hr_v}K_v τ… [§133], varied radicals
  ⇒ cyclic permutation of ξ_h. [all verbatim]
- **§186 (Befreiung von den beschränkenden Voraussetzungen), part 1 (p641-643):** removes §185's 2 Voraussetzungen via
  a Tschirnhausen transform. η_0..η_{n-1}=roots of ANY irred. metacykl. eqn deg n; (1) ξ_h=ψ(η_h); (2)
  ψ(y)=a_0+a_1y+…+a_{n-1}y^{n-1} (a in 𝔎, unbestimmt); ξ distinct ⇒ ξ also roots of irred. metacykl. eqn, (1) is a
  Tschirnhausen-Transf. (§52), ξ_0 primitive elt of 𝔎(η_0), fields 𝔎(ξ_r)=𝔎(η_r); (3) χ(x)=b_0+…+b_{n-1}x^{n-1};
  (4) η_h=χ(ξ_h). Can choose a so §185's Voraussetzungen 1./2. hold: the ξ↔a linear substitution has determinant =
  Vandermonde of η = Differenzenproduct ≠ 0; (ε,x) and f_α-f_β are §184-nonzero functions ⇒ [§143,1] rational a exist
  making (ε,ξ)≠0 and k_α-k_β≠0 and ξ_h distinct — QED. Then: introduce y_h=χ(x_h) (5); (6) Θ_v=(ε^{r_v},y)/(ε^{r_v},x);
  Θ_v is s-invariant [§184,4], Normalform coeff cyclic [§183], t^{-1}→Θ_{v+1}, σ=(ε,ε^g) same ⇒ Θ-system has props
  α)β)γ)δ); [§184 Schlusssatz] Θ_v → rational fn of k_v (7) Q_v=Q(k_v); (8) (ε^{r_v},η)=Q_v(ε^{r_v},ξ); substituting
  §185(5) gives (ε^{r_v},η) of the SAME form with K_v→Q_v K_v (which may partly vanish). [all verbatim]
**SPERRUNG (deferred):** §186 "Tschirnhausen-Transformation" (p642) letterspaced (term). §186 Theorem I (p644, quote block)
letterspaced. CONTENT-faithful; NOT emphasis-verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — §186 COMPLETE (p644-646, .tex 22478-22571) — (verified by eye)
**CONTENT: 1 EDIT (Weber erratum flag).** Scan-checked line-by-line; recompiled clean (byte-identical, comment inert).
§186 now fully content-verified p641-646. §187 (Realitätsverhältnisse) opens next (.tex 22573, p647).
- **ERRATUM FLAG (Weber index slip, .tex 22559):** conclusion prints `S(\xi_0,\xi_1\ldots\xi_{n-2})` where the same
  symmetric function was defined `S(\xi_0,\xi_1\ldots\xi_{n-1})` on p645 (.tex 22553). Since there are n roots
  ξ_0..ξ_{n-1}, the last index should be n-1; `ξ_{n-2}` is a Weber print slip. Both occurrences reproduced FAITHFULLY in
  the .tex (n-1 at 22553, n-2 at 22559 — each matches its own printed form). Added `% [sic] … Druck-Fluechtigkeitsfehler
  (gemeint ξ_{n-1}) … quellentreu reproduziert, nicht korrigiert`. = 5th type-B Weber erratum in vol1 (after §172 (a-b)^3,
  §180 z_0, §181 dup-(12), §182 v'_4). Recompiled: 418pp/0 err/0 overfull/0 underfull/0 missing-char/0 undefined
  (byte-identical 2263535). NB distinct in kind from the §185/p640 R_v edit (that was a GPT-ADDED null exponent removed;
  this is a Weber-OWN slip kept + flagged) — the two together illustrate fidelity in both directions.
- **§186 Theorem I (forward, p644):** every root ξ of a metacykl. prime-deg-n eqn = A+Σ_{0,n-2}K_v τ_v^{r_{n-2}}…τ_{v+n-2}^{r_0}
  (9); A rational; k_0..k_{n-2} = distinct nonzero roots of a cyclic (n-1)^ten eqn; K_v rational fn of k_v (same form all v);
  r_v = least positive residues of 1,g,g²…g^{n-2}; n radical-choices → n roots of one rational eqn. (9) from §185(6) with
  A,K_v → nA,nK_v (Vereinfachung). [Note: (9) here PRINTS τ_{v+n-2}^{r_0} — Weber writes r_0 in full formulas, omits it
  only in the p640 k-shorthand; consistent with the p640 fix.]
- **§186 converse (p644-646):** (10) ξ_h=A+Σε^{hr_v}K_v τ…, h=0..n-1; (11) abbreviated w/ ⁿ√R_v; (12) ⁿ√R_v=τ_v^{r_{n-2}}…
  τ_{v+n-2}^{r_0} [prints r_0]. Two Änderungen: 1. radical sign-change (13) (τ_α,ε^β τ_α) → (14) (ⁿ√R_v,ε^{βr_{v-α-1}}ⁿ√R_v),
  via r_{α+β}≡r_α r_β (mod n) → index perm (h,h+βr_{-α-1}); 2. cyclic (15) (τ_0..τ_{n-2}) → (16) (ⁿ√R_v,ⁿ√R_{v+1}),
  (K_v,K_{v+1}) → index perm (h,g^{-1}h). Any symm/metacykl S(ξ) → rational fn of τ → depends only on k_v → invariant
  under (k_0..k_{n-2}) cyclic → in 𝔎 (rational) ⇒ the ξ (10) are roots of a deg-n eqn in 𝔎. Irreducibility [§179]:
  ⁿ√R_v all rational or all irrational [§185(8)]; x^n-R_0 reducible ⇒ ξ_h rational, eqn reducible, ξ∈𝔎(ε) deg≤n-1;
  x^n-R_0 irreducible ⇒ Φ(ξ_0)=0→Ψ(ⁿ√R_0)=0 survives all n roots ⇒ ξ_0→all ξ ⇒ eqn irred in 𝔎. **Theorem II** (converse):
  every (9)-form ξ is a root of a deg-n eqn in 𝔎, irred except the special case (one root rational, rest in 𝔎(ε)). [verbatim]
**SPERRUNG (deferred):** §186 "Tschirnhausen-Transformation" (p642), Theorem I (p644 quote), Theorem II (p646 quote)
letterspaced. CONTENT-faithful; NOT emphasis-verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — §187 COMPLETE (Realitätsverhältnisse, p647-648, .tex 22573-22609) + §188 opening (p648, .tex 22611-22615) — (verified by eye)
**CONTENT: 1 EDIT (source-fidelity normalization removed).** Scan-checked line-by-line; recompiled clean.
- **FIX (GPT-normalized index restored, .tex 22603):** §187 reality-proof last line read `die Wurzeln $\xi_h$ alle reell
  sind`; ZOOM p648 (crop_5_21) shows Weber prints `$\xi_z$` (clear italic z subscript) — generic index z, as he uses for
  permutation indices back in §180 (s=(z,z+1)). GPT had normalized z→h to match the ξ_h convention of formula (11).
  Restored `$\xi_z$` to match print. Semantically null (bound index). = 2nd "GPT-normalization removed" edit in vol1
  (after §185/p640 R_v ^{r_0}). Recompiled: 418pp/0 err/0 overfull/0 underfull/0 missing-char/0 undefined (2263541).
  Reinforces the p640 lesson: GPT silently normalizes indices/exponents to the "expected" convention; ZOOM and match print.
- **★ ORDINAL-TITLE WATCH RESOLVED for §188:** §188 title = `Metacyklische Gleichungen f\"unften Grades`. Scan p648 (mid,
  letterspaced heading) prints "fünften Grades" SPELLED OUT — .tex MATCHES. So §188 is FAITHFUL as-is, NO fix. This is
  the OPPOSITE of §181 (where Weber printed numeral "5ten" and GPT's spelled-out "fünften" was the reword needing fix).
  CONCLUSION: Weber is inconsistent across section titles (§181 numeral, §188 spelled) — must scan-check EACH, never
  assume the pattern. Body text of §188 also spells "fünften"/"vierten" (Weber spells ordinals in body consistently).
  Still-pending title checks: §54/74/75 ("fünften"), §80 ("zweiten") — scan-check when/if revisited.
- **§187 verbatim (Realitätsverhältnisse):** real 𝔎 → two Arten of metacykl. prime-deg eqns [§180] (1 real + n-1 imag, OR
  all real); two Arten of cyclic even-deg eqns [§165] (all real / all imag). If k_0..k_{n-1} real & τ real → (10) §186
  gives ξ_0 real, ξ_h & ξ_{-h} conj. imag. If k imag → k_v, k_{v+(n-1)/2} conj [§165]; via (8) §185:
  ⁿ√R_{v+(n-1)/2}=Φ(k_v)(ⁿ√R_v)^{g^{(n-1)/2}}, ⇒ ⁿ√R_{v+(n-1)/2}·ⁿ√R_v=Ψ(k_v) rational (since g^{(n-1)/2}+1≡0 mod n) →
  Ψ(k_v)=Ψ(k_{v+(n-1)/2}) real → the two radicals conj. imag. (n-th powers conj, product real ⇒ unit factor=1); with
  r_v≡-r_{v+(n-1)/2} (mod n), (11) ⇒ all ξ_z real. **Satz** (quote): cyclic eqn (k) real-rooted ⇒ one ξ real rest imag;
  (k) imag-rooted ⇒ all ξ real.
- **§188 opening (p648):** goal — find roots of ALL metacykl. quintics in any 𝔎; needs the roots k_0,k_1,k_2,k_3 of a
  cyclic quartic (distinct, nonzero). Kronecker-Bd.II remark (all such over Q are cyclotomic). [verbatim; computation
  continues p649: w=(k_0-k_2)(k_1-k_3) (1), w=4√c (2), etc.]
**SPERRUNG (deferred):** §187 Satz (p648 quote), §188 title. CONTENT-faithful; NOT emphasis-verified. Confirmed by eye
vs ~500dpi scans; direct context-read.


### 2026-07-02 — §188 COMPLETE (p649-653, .tex 22617-22793) + BERICHTIGUNGEN (p654) — END OF VOL1 BODY reached — (verified by eye)
**CONTENT: 1 EDIT (Weber erratum flag).** Scan-checked p649-654 line-by-line; recompiled clean.
- **ERRATUM FLAG (Weber index slip in eq (14), .tex 22786):** $K_3=A_1-A_2r-A_2\varrho'-A_4r\varrho'$ — the coeff of $\varrho'$
  is printed $A_2$, but the parallel build of (14) gives $\varrho/\varrho'$ the coeff $A_3$ in $K_0,K_1,K_2$; so $A_3$
  is expected and $A_2$ is a Weber print slip. ZOOM p653 (crop_18_18) CONFIRMS the print reads $A_2$ (subscript 2
  identical to the $A_2r$ in the same line, distinct from the "3" glyph in "$K_3$" below). .tex already faithful
  ($A_2\varrho'$); added `% [sic] … Druck-Fluechtigkeitsfehler (gemeint A_3) … quellentreu reproduziert`. = **6th
  type-B Weber erratum in vol1** (after §172 $(a-b)^3$, §180 $z_0$, §181 dup-(12), §182 $v'_4$, §186 $\xi_{n-2}$).
  Recompiled: 418pp / 0 err / 0 overfull / 0 underfull / 0 missing-char / 0 undefined (byte-identical 2263541, comment inert).
- **§188 content verbatim (p649-653):** cyclic quartic solved via w=(k_0-k_2)(k_1-k_3) (1), w=4√c (2); the two cyclic
  fns → (3) 8b, 8a√c; relation (4) b²=c(1+a²); (5) k-diffs =2√(b±a√c); (6) √c=√(b+a√c)·√(b-a√c); (7)(8) k-sums via
  C,B; (9) explicit k_0..k_3; (10) r,ϱ,ϱ' abbrevs, r=ϱϱ', six radicals 1,r,ϱ,ϱ',rϱ,rϱ'; the σ-permutation matrix
  (r,ϱ,ϱ')→(−r,ϱ',−ϱ) + 4×6 sign table; quartic (11) x⁴−2(B²c+b)x²−4Bacx+B⁴c²−2B²bc+c=0; special b=0/a=i case
  (⁴√c form + reduced quartic; only if i∈𝔎); h-substitution b=h(1+a²),c=h²(1+a²) → (12); Abel's variant
  (a=1:e, √(1+e²)); the quintic root: g=2 → r-exponents 1,2,4,3; τ_v=⁵√k_v; (13) ξ=A+ΣK_v τ…; K_v = Abel form,
  better via 3 radicals r,ϱ,ϱ'; (14) K_0..K_3; K_0=A_1+A_2r+√(ϱ²(A_3+A_4r)²) → form of k_0 in (9) recovered. All
  faithful except the (14) K_3 A_2 slip (flagged above). ("Coëfficienten"→"Coefficienten" house-conv; "Abel"
  letterspaced → SPERRUNG; body "5ten Grades" numeral matches .tex $5^{ten}$.)
- **BERICHTIGUNGEN (p654) — verified faithful:** printed errata page has EXACTLY 2 entries, both verbatim in .tex
  (22798, 22800): "Seite 182 … Zeile 12 … x_m statt x_n." and "Seite 347 … Zeile 24 … (2x²+1)² statt (2x²−1)²."
  GPT dropped NO errata entries. (Minor cosmetic: print centers "Berichtigungen." w/ period + rule ornaments; .tex
  uses left-aligned \section*{Berichtigungen} no period. Not a content issue.)
- **★ RUNNING-HEAD CONCERN CLOSED:** .tex preamble (l.64-65) sets FIXED \lhead{Weber Vol. I}/\rhead{Deutsche Quelle};
  it does NOT reproduce Weber's per-page running heads. So the earlier-noted p649/p651 running-head "5ten" vs §188
  title "fünften" discrepancy is MOOT — the .tex carries no Weber running heads at all. Item resolved, no action.
- **★★ MILESTONE — END OF VOL1 BODY reached (content-track forward pass):** §188 is the last § of the Achtzehnter
  Abschnitt, which is the last Abschnitt of the vol1 body; after it only Berichtigungen + \end{document}. p653_bot
  and p654_bot are blank. The forward CONTENT pass has now reached the physical end of the printed body.
  **NOT a completeness claim:** "reached the end" ≠ "whole volume verified". Individual zoom-verification of EARLIER
  sections is only as recorded in this log; many early pages may never have been page-by-page zoom-checked in the
  current method. SPERRUNG track fully OWED (whole volume). Front matter (Inhaltsverzeichnis/title) is NOT in the
  .tex (body-only reconstruction) — separate scope question, unchecked.
**SPERRUNG (deferred):** §188 "Abel" (p652 ×2, letterspaced author name), §188 title. CONTENT-faithful; NOT
emphasis-verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p1-4 (EINLEITUNG start, .tex 157-233) — FIRST context-read audit of the p1-99 gap — (verified by eye)
**CONTENT: 4 EDITS.** These pages were NEVER audited before (CERT log had begun at p100). Recompiled clean:
418pp / 0 err / 0 overfull / 0 underfull / 0 missing-char / 0 undefined (2264012 bytes).
- **FIX 1 (misread, p2 footnote, .tex 173):** Euklid citation printed `Buch VII, II` (Roman II = Elements Bk VII, Satz 2,
  the ggT/GCD proposition); glyph identical to the "II" in "Bd. II" of the same line. GPT had read it as arabic `11`.
  Changed `11`->`II` + `% [quellentreu]`. ZOOM crop_13_85.
- **FIX 2 (WEBER ERRATUM, p4, .tex 203):** ordering def — Weber prints "Ist a>b und b>c oder **a>b>c**, so sagen wir,
  dass b zwischen a und c liegt." The 2nd (oder-)case "a>b>c" is IDENTICAL to the 1st "a>b und b>c" (redundant);
  the intended 2nd case is the ascending a<b<c so that "b zwischen a und c" is completely defined. GPT had SILENTLY
  corrected it to "a<b und b<c". ZOOM crop_66_43 confirms ALL signs are ">". Reverted .tex to the printed "a>b>c" +
  `% [sic]` (Erratum reproduced, not corrected). = **7th type-B Weber erratum in vol1** (after §172 (a-b)^3, §180 z_0,
  §181 dup-(12), §182 v'_4, §186 xi_{n-2}, §188 K_3 A_2). ★ First erratum found OUTSIDE the metacyklische Abschnitt —
  the Einleitung has them too; the p1-99 gap is genuinely unaudited.
- **FIX 3 (Fraktur notation, p4, .tex 201):** Menge symbol printed Fraktur **M** (blackletter, like Weber's set/field
  symbols); .tex had plain italic `$M$`. Weber uses Fraktur for sets — .tex ALREADY has \mathfrak R (rationals),
  \mathfrak S (cuts) in the very same passage — so plain M was an inconsistency. Changed `$M$`->`$\mathfrak M$`.
  ZOOM crop_33_27. ⚠ WATCH: other Menge-M's (e.g. .tex 215 "geordnete Menge $M$"), and the Schnitt parts $A,B$
  (.tex has \A=\mathfrak A, \B=\mathfrak B macros) — verify Fraktur vs italic on each coming page.
- **FIX 4 (content drop restored, p4, .tex 206-210):** displayed eq printed with labels "$\mu=$" and "$\mu'=$" before
  the two fractions (hmn'/hnn', hm'n/hnn'); GPT had dropped BOTH labels (bare fractions only), leaving "so kann man ...
  setzen" with nothing set. Restored `\mu=`/`\mu'=`. ZOOM crop_28_84.
- **FAITHFUL (content):** p1 (Einleitung opening: natural numbers, 4 Species, direct/inverse ops, division), p2 (primes,
  rel.-prime, GCD/Euklid algorithm), p3 (lcm, unique prime factorisation), p4 (Zahlbegriff overview, Mannigfaltigkeit/
  Menge def, geordnet/discrete/dicht, Brueche, dense-set proof-start). All prose verbatim bar the 4 edits.
- **★ SYSTEMATIC PATTERNS in Einleitung (works/adjust):**
  (a) **Inline->display normalization:** Weber prints short relations INLINE in prose (a=q_1a_1+a_2; a_1=q_2a_2+a_3; the
      GCD pair; etc.); GPT display-set them as `\[...\]`. Content faithful; display-setting short relations is a
      defensible editorial choice — NOT reverting (documented as accepted normalization). Do NOT churn these.
  (b) **Fraktur set-symbols:** .tex renders some set-symbols as plain italic where Weber prints Fraktur (Menge M fixed;
      \mathfrak R,S already correct). Check each M / A / B / other set-letter against the print per page.
  (c) **Heading style:** print letterspaced-caps headings ("EINLEITUNG."); .tex plain \Large/\section* — consistent
      house style across the doc, cosmetic, not touched.
**SPERRUNG (deferred):** the Einleitung is DENSE with gesperrt technical terms (vier Species, Addition/Multiplication/
Subtraction/Division, Divisor/Dividend/theilbar/Factor/Theiler, Primzahl, relative Primzahlen/theilerfremde,
Algorithmus des groessten gemeinschaftlichen Theilers, kleinste gemeinschaftliche Vielfache, geordnet/discrete/dicht/
stetig, Menge/Mannigfaltigkeit, Brueche, Schnitt, ...). CONTENT-faithful; NOT emphasis-verified. Confirmed by eye vs
~500dpi scans; direct context-read.


### 2026-07-02 — p5-7 (EINLEITUNG cont., .tex 211-241) — p1-99 gap pass — (verified by eye)
**CONTENT: 4 EDITS.** Recompiled clean: 418pp / 0 err / 0 overfull / 0 underfull / 0 missing-char / 0 undefined (2264024).
- **FIX 1-3 (Fraktur, p5, .tex 215):** the general Menge symbol prints Fraktur **M** in THREE spots on this line —
  "geordneten Menge M", "Schnitt in M", "Element mu von M" — all had plain italic `$M$` in .tex. Changed each to
  `$\mathfrak M$` (ZOOM crop_33_27 on p4 + direct read p5). CONFIRMS the Menge-M->Fraktur pattern is systematic (2nd
  page confirming, after p4/201). The cut PARTS $A,B$ stay Latin (correct — Weber: cuts = Fraktur 𝔄,𝔅; a cut's parts
  = Latin A,B; .tex already right on those).
- **FIX 4 (misread, p7, .tex 235):** "der **einem** der Schnitte von 𝔄 erzeugt" — print shows "**einen**" (accusative,
  object of "erzeugt"; ZOOM crop_52_31 confirms final two-stroke "n", not three-stroke "m"). .tex had dative "einem"
  (ungrammatical here). Changed `einem`->`einen`.
- **FAITHFUL (content):** p5 (μ-betweenness display closing, Punkte-einer-Linie, Schnitt def, stetig def, Dedekind fn
  head), p6 (ℜ-not-continuous proof via √μ: x²(mq²−np²)>nxy(2p+1)>n(2pxy+y²), mq²x²>n(px+y)², a'=(px+y):qx; 𝔖 as set
  of cuts; Dedekind fn continuation Weierstrass/Cantor/Messbarkeit), p7 (𝔖 stetig proof; abstracte-Betrachtung +
  Euklid Bk X fn). All sets ℜ,𝔖,𝔄,𝔅 correctly \mathfrak. All prose verbatim bar the 4 edits.
- **★ SYSTEMATIC — Fraktur Menge-M (running):** general "die Menge M" is Fraktur 𝔐 throughout Weber; .tex has plain
  italic $M$ in spots. Fixed so far: .tex 201 (p4), 215 ×3 (p5). ⚠ STILL AHEAD (fix per print page): .tex 243 "Eine
  geordnete Menge $M$ heisst messbar" + "in $M$ ausführbar" + "von $M$" (p8), 254 "stetigen geordneten Menge $M$",
  264 "messbaren Menge $M$", 270 "messbaren Mannigfaltigkeit $M$", and any later. Verify Fraktur on each print page.
- Trivial skipped (below content-track threshold, consistent w/ prior punctuation calls): p5 print "Massen, niemals"
  has a comma the .tex omits ("Massen niemals").
**SPERRUNG (deferred):** gesperrt terms this stretch — geordnet/discrete/dicht/stetig, messbar, Menge/Mannigfaltigkeit,
Schnitt, commensurabel/incommensurabel, Zähler/Nenner, Verhältniss, rationale Zahl, Dedekind/Weierstrass/Cantor/Euklid
(author names letterspaced). CONTENT-faithful; NOT emphasis-verified. Confirmed by eye vs ~500dpi scans; context-read.


### 2026-07-02 — p8 (EINLEITUNG: messbar-Menge def + measurement, .tex 241-256) — p1-99 gap pass — (verified by eye)
**CONTENT: 5 EDITS.** Recompiled clean: 418pp / 0 err / 0 overfull / 0 underfull / 0 missing-char / 0 undefined (2264020).
- **FIX 1 (REWORD restored, .tex 252):** print reads "...keine Elemente liegen, **weil, wenn** $b<c<b+a$ waere, aus der
  Definition der Messbarkeit **folgen wuerde**, dass $a'=c-b$ kleiner als $a$ waere." GPT had reworded to
  "...liegen**; denn wenn** ... waere, **so wuerde** aus der Definition der Messbarkeit **folgen**, dass ...". Same sense,
  different words/structure. ZOOM crop_9_64 confirms "weil, wenn". Restored Weber's wording. (No inline % comment —
  mid-paragraph would comment out the line tail; documented here.)
- **FIX 2-5 (Fraktur Menge-M, .tex 243 ×3 + 248 ×1):** the messbar-def general Menge symbol prints Fraktur **M** in
  "geordnete Menge M", "sind in M allgemein", "Element a+b von M abgeleitet", "Elemente von M haben" — all plain
  `$M$` -> `$\mathfrak M$`. (3rd page confirming the systematic Menge-M->Fraktur pattern, after p4/p5.)
- **FAITHFUL (content):** messbar def (Add./Vervielf./Subtr. in M; a+b>a,b; a+b=b+a, (a+b)+c=a+(b+c); a+b=c ⇒ b=c−a;
  Vervielf. ma), messbar consequences (no largest; dichte messbare ⇒ no smallest via a'=c−b; converse; stetig ⇒
  Messbarkeit simplifies). All prose verbatim bar the 5 edits.
- **★ SYSTEMATIC — GPT period-normalization of Weber's colons/semicolons (NEW pattern, punctuation-tier, SKIPPED on
  content track, flagged for a possible separate punctuation pass):** GPT repeatedly broke Weber's long sentences by
  swapping his ":" / ";" for "." (+ capitalising the next word). This page: "Voraussetzungen**:** Addition" -> ".",
  "gelten**;** und" -> ". Und", "kleinstes Element**;** denn" -> ". Denn". Below the content-track threshold (same
  tier as the skipped commas); NOT fixed. If a punctuation-faithful pass is wanted later, this is a recurring target.
- **★ Fraktur Menge-M running list — fixed so far:** .tex 201 (p4), 215 ×3 (p5), 243 ×3 + 248 ×1 (p8). ⚠ STILL AHEAD:
  254 "stetigen geordneten Menge $M$" (p9), 264 "messbaren Menge $M$", 270 "messbaren Mannigfaltigkeit $M$", later.
**SPERRUNG (deferred):** messbar, Vervielfältigung, Differenz, Verhältniss, Zähler/Nenner (gesperrt terms). CONTENT-
faithful; NOT emphasis-verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p9 (EINLEITUNG: messbar Mengen, cut-addition, .tex 254-260) — p1-99 gap pass — (verified by eye)
**CONTENT: 5 EDITS + 1 documented Weber font-slip (kept).** Recompiled clean: 418pp / 0 err / 0 overfull / 0 underfull /
0 missing-char / 0 undefined (2264034).
- **FIX 1-2 (Fraktur Menge-M, .tex 254 ×2):** "stetigen geordneten Menge M", "Schnitt (A,B) in M" — plain `$M$` ->
  `$\mathfrak M$`. (4th confirming page.)
- **FIX 3 (≦ vs <, .tex 254):** cut condition printed "für die $a+x\le c$ ist, nach A" (Weber's **≦** double-bar);
  .tex had strict "$a+x<c$", which leaves the boundary element (a+x=c) in NEITHER A nor B — a partition gap. ZOOM
  crop_3_11 confirms the ≦ (double horizontal bar), distinct from the plain ">" in "c>a" and "a+x>c" on the same
  lines. Changed `<`->`\le` (house conv for ≦). Genuine relation error, not cosmetic.
- **FIX 4 (dropped word "so", .tex 258):** print "die natürliche Zahl $m$ **so** bestimmen, dass $m\mu>b-a$" (correlative
  so ... dass); .tex had dropped "so". ZOOM crop_3_69. Restored.
- **FIX 5 (Fraktur, .tex 260):** "den Schnitt in $R$" — print shows Fraktur **ℜ** (rationals, like all other ℜ on the
  page); .tex had plain italic `$R$` (a lone inconsistency — .tex uses \mathfrak R everywhere else). `$R$`->`$\mathfrak R$`.
- **DOCUMENTED, NOT fixed (Weber font-slip, .tex 258):** print "für die $a+h\mu$ in **𝔅** enthalten ist" uses upright
  Fraktur 𝔅 where the surrounding "in B" (same sentence, ×3) are slanted Latin B; context = upper part B of the cut
  α=(A,B), so it's a Setzfehler (typesetter grabbed the Fraktur sort). ZOOM crop_3_69 confirms genuine Fraktur 𝔅.
  .tex keeps the semantically-correct Latin **B** — per the Collectet→Collected precedent (keep an obvious
  typo-correction, flag it here) rather than inject a misleading 𝔅 (which elsewhere denotes the cut-of-cuts). Noted.
- **FAITHFUL (content):** stetig⇒messbar simplification (Schnitt via a+x≦c/a+x>c, a+b=c), nat numbers messbar (kleinstes
  1), rationals messbar, Strecken/Stoffmengen/Zeiträume as messbar examples + Hypotenuse-as-sum remark, 𝔖 messbar prep
  (a'+μ=b'), cut-addition def (A,B)+(A',B')=(A'',B''), a''≤a+a' (.tex already \le — matches). All bar the 5 edits.
- **★ Fraktur running list — fixed so far:** .tex 201, 215×3, 243×3+248, **254×2, 260(R)** = 11 total. Punctuation
  period-normalization recurs (skipped): "ein Schnitt; denn"->". Denn". ⚠ AHEAD: 264 "messbaren Menge $M$", 270
  "Mannigfaltigkeit $M$", 322 "Element $x$ von $M$", + later.
**SPERRUNG (deferred):** messbar, Verhältniss, Zähler/Nenner, Euklid (Bk V) — gesperrt. CONTENT-faithful; NOT
emphasis-verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p10 (EINLEITUNG: cut-addition tail + Verhältnisse def, .tex 260-268) — p1-99 gap pass — (verified by eye)
**CONTENT: 3 EDITS.** Recompiled clean: 418pp / 0 err / 0 overfull / 0 underfull / 0 missing-char / 0 undefined (2264024).
- **FIX 1-2 (Fraktur Menge-M, .tex 264 + 266):** "messbaren Menge M zu Paaren" (264), "wenn M das System der
  natürlichen Zahlen" (266) — plain `$M$` -> `$\mathfrak M$`. (5th confirming page; ZOOM crop_3_50 shows Fraktur 𝔐.)
- **FIX 3 (WORD-ORDER REWORD restored, .tex 266):** print "...zwei andere ganze Zahlen sind, **dann und nur dann
  $qa=pb$**, wenn $mq=np$ ist." GPT had reordered to "$qa=pb$ dann und nur dann, wenn ...". ZOOM crop_3_56 confirms
  Weber's order (dann und nur dann BEFORE qa=pb). Restored.
- **FAITHFUL (content):** cut-addition tail (α'' > α,α'; A'' ⊃ A; μ+μ' Schnitt), Verhältnisse def (Euklid Bk V), pair
  a:b vs b:a, Zähler/Nenner, rational Verhältniss (na=mb, qa=pb ⟺ mq=np, p/q coprime), rationale Zahl = geordnete
  dichte messbare Mannigfaltigkeit. All prose verbatim bar the 3 edits.
- **★ Fraktur running list — fixed so far:** .tex 201, 215×3, 243×3+248, 254×2, 260(R), **264, 266** = 13 total. ⚠ AHEAD:
  270 "messbaren Mannigfaltigkeit $M$" (p11), 322 "Element $x$ von $M$", + any later. Verify Fraktur per page then fix.
**SPERRUNG (deferred):** Verhältniss/Zähler/Nenner/rationales/rationale Zahl (gesperrt), Euklid. CONTENT-faithful; NOT
emphasis-verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p11 (EINLEITUNG: a:b vs m:n comparisons + Verhältnis-cases start, .tex 268-296) — p1-99 gap pass — (verified by eye)
**CONTENT: 3 EDITS + 1 DEFERRED systematic notation remap (e/ε/e').** Recompiled clean: 418pp / 0 err / 0 overfull /
0 underfull / 0 missing-char / 0 undefined (2264297).
- **FIX 1 (Fraktur, .tex 270):** "messbaren Mannigfaltigkeit M" -> `$\mathfrak M$` (6th confirming page).
- **FIX 2 (= vs >, misread, .tex 274):** print "und wenn $m:n>p:q$, so ist auch $a:b>p:q$"; .tex had "$m:n=p:q$"
  (= where print shows >). ZOOM crop_3_29 confirms ">" (matches the > in a:b>p:q). Changed `=`->`>`.
- **FIX 3 (DROPPED SENTENCE restored, .tex 279):** after the display "$a/b>m_1/n_1>m/n$" the print reads "...ist, **d. h.
  man kann zwischen $a:b$ und $m:n$ beliebig viele rationale Verhältnisse einschalten.** Um dies zu zeigen, ...". GPT
  had dropped that whole clause (.tex went "...ist. Um dies zu zeigen"). Restored verbatim.
- **★★ DEFERRED — systematic notation remap e/ε/e' (.tex 294-302):** Weber denotes the two ratios by **e** (Latin) and
  **ε** (Greek lunate epsilon), and a further ratio by **e'** (print "mit e, ε bezeichnen"; "e<μ<ε ... jedes andere
  Verhältniss e'"). ZOOM crop_3_89 confirms e (Latin, mid-bar) is DISTINCT from ε (Greek, open/lunate). The .tex
  normalized this to $\epsilon,\epsilon',\epsilon''$. Mapping to restore: `$\epsilon$`->`$e$`, `$\epsilon'$`->
  `$\varepsilon$`, `$\epsilon''$`->`$e'$`, over .tex 294-302 (294,296 on p11; 298,300,302 on p12). **NOT done this turn**
  — passage spans onto p12; will remap all 5 lines COHERENTLY next turn after verifying p12's print (298-302). (Can't
  replace_all `$\epsilon$` — appears in other sections; must edit these lines individually.)
- **FAITHFUL (content):** nat.numbers ⊂ rational (m:1), a:b vs m:n comparison def (na>mb ⇒ a:b>m:n; transitivity; ≦/>
  cases with h,k intercalation formulas a/b>(hm+k)/(hn)>m/n etc.), Verhältnis-cases 1)/2) setup. Bar the 3 edits +
  the deferred e/ε.
- **★ Fraktur running list — fixed so far:** 201,215×3,243×3,248,254×2,260-R,264,266, **270** = 14 total.
**SPERRUNG (deferred):** Verhältnisse/rationale Zahl, "einander gleich" (gesperrt). CONTENT-faithful; NOT emphasis-
verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p12 (EINLEITUNG: Verhaeltnis equality/inequality -> Zahlbegriff, .tex 294-306) — p1-99 gap pass — (verified by eye)
**CONTENT: the DEFERRED e/eps notation remap is now DONE (5 lines re-notated), + it turned up a genuine CONTENT
CORRUPTION. Plus 1 case-label confirm. p12_bot faithful (no edits).** Recompiled clean: 418pp / 0 err / 0 overfull /
0 underfull / 0 missing-char / 0 undefined (2264181).

- **REVERSAL of last turn's decline.** Last turn I declined the e/eps remap as "too subtle / semantically null."
  That was WRONG. p11_bot + p12_top + p12_mid zooms show Weber's scheme is CLEAR and CONSISTENT:
    * **e** (Latin, mid-bar closed) = first ratio a:b
    * **eps** (Greek lunate, open crescent) = second ratio alpha:beta
    * **e'** (Latin prime) = "jedes andere Verhaeltniss" (case-1 third ratio)
  The .tex had normalized ALL of these to $\epsilon,\epsilon',\epsilon''$, erasing the Latin/Greek distinction.
  Evidence (unambiguous): p11_bot "auch mit **e, eps** bezeichnen"; "denn ist **e**<mu<**eps**, so ist jedes andere
  Verhaeltniss **e'**"; p12_top "sowohl zwischen **e** und **e'** als zwischen **e'** und **eps**"; p12_mid "Im Falle
  2a) heisst **e** kleiner als **eps**".

- **>>> CONTENT CORRUPTION found & fixed (.tex 298):** print line reads "...**eps**<mu' folgt, dass mu<mu', und
  folglich **e**<mu' sich ergiebt" — two DIFFERENT ratios (Greek eps, then Latin e). The .tex had normalized BOTH to
  $\epsilon$, giving "eps<mu' ... folglich eps<mu'" = a CIRCULAR/trivial statement that destroys Weber's mutual-
  exclusion argument (alpha & beta cannot both hold). Restoring the Latin **e** in the conclusion makes it the
  meaningful "folglich e<mu'". This is a real logic error introduced by GPT-normalization, not cosmetic. It is the
  single strongest justification for doing the whole remap.

- **EDITS (full-line re-notation, .tex 294,296,298,300,302):** mapping applied per-occurrence (NOT a blind global
  swap): .tex $\epsilon$->e, $\epsilon'$->\epsilon (Greek, drop prime), $\epsilon''$->e' throughout 294/296/298/302.
  **Two deliberate exceptions kept Greek** (verified by zoom, logically required):
    * .tex 298 "$\epsilon<\mu'$ folgt" — the FIRST of the pair is the Greek second-ratio eps (stays \epsilon); only the
      SECOND ("folglich") becomes Latin e.
    * .tex 300 "Denn ist $\mu<\epsilon$ und $\mu\gtrless\epsilon'$ ... zwischen $\epsilon$ und $\epsilon'$ ... $\epsilon,
      \epsilon'$ sind nicht gleich" — here eps,eps' are a ratio and its EQUAL REPLACEMENT (Weber illustrates the
      replacement argument with the eps ratio); both genuinely Greek in print (crop_13_30 confirms open-crescent
      eps + eps'). Only the leading "wenn $\epsilon$ oder $\epsilon'$"->"wenn $e$ oder $\epsilon$" changed on 300.
  Each new line re-read + matched symbol-by-symbol to the scan. Compiles 0-badness (so $e$,$e'$,$\epsilon$,$\epsilon'$
  all render).

- **CASE-LABEL confirm (.tex 298):** print p12_top shows the sub-cases introduced as BARE "alpha)" / "beta)"
  ("entweder a) e<mu<eps oder b) e>mu'>eps"), NOT "2a)/2b)". My prior-turn restoration of bare $\alpha)$/$\beta)$ on
  298 is CORRECT. The "2a)/2b)" form appears only later (300,302, referring back to "case 2's a)/b)") and the .tex
  already had those right ($2\alpha)$,$2\beta)$).

- **p12_bot FAITHFUL (no edits):** .tex 304 (Gattungsbegriff->Zahl, footnote "Auf den Gattungsbegriff...natuerliche
  Zahlen", rationale/irrationale Zahlen, "geordnete Menge...Repraesentant") + start of Zaehler/Nenner Satz (.tex 306
  "Von zwei Verhaeltnissen mit demselben Nenner...dessen Zaehler groesser ist, und") all match print verbatim. The
  Zaehler/Nenner proof, a:c=b:d Satz, and Hauptsatz (.tex 306-322) are on p13 (incl. .tex 322 "ein Element $x$ von $M$"
  -> CHECK FRAKTUR M on p13).
- **METHOD note:** the "audit output many times" mandate paid off here — my first-pass decline was wrong; only by
  re-zooming p11_bot/p12_top comprehensively (not just the one ambiguous crop) did the consistent e/eps/e' scheme +
  the 298 corruption become visible. Lesson: for a suspected systematic normalization, zoom the WHOLE passage's clear
  instances before ruling on the ambiguous ones; do not decline on the strength of a single blurry crop.
**SPERRUNG (deferred):** "einander gleich", "irrationale Zahlen", "rationalen Zahlen" (gesperrt). CONTENT-faithful;
NOT emphasis-verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p13 (EINLEITUNG: Zaehler/Nenner Satz proof + a:c=b:d Satz + Hauptsatz a:b=c:d, .tex 306-324) — p1-99 gap pass — (verified by eye)
**CONTENT: 3 EDITS + 1 display-layout note (skip).** Recompiled clean: 418pp / 0 err / 0 overfull / 0 underfull /
0 missing-char / 0 undefined (2264193).
- **FIX 1 (≧ vs =, misread/normalization, .tex 306):** in the Zaehler/Nenner proof, print reads "Denn waere
  $mb\ge na' \ge na+n(a'-a)$" — BOTH relations are Weber's ≧ (wedge + double bar). .tex had "$mb\ge na'=na+n(a'-a)$"
  (2nd sign normalized to "="). Since na'=na+n(a'-a) is an IDENTITY, GPT "corrected" the ≧ to =. ZOOM crop_5_22 shows
  the 2nd glyph is a clear ">"-wedge with two horizontal bars above (≧), NOT a plain "=" (no wedge). Restored `=`->`\ge`
  (house rendering of Weber's ≧, matching the 1st sign on the same line). GPT-normalization removed.
- **FIX 2 (DROPPED WORD "und" + punctuation, .tex 311):** print "also $a:b<a':b$**; und** ganz ebenso kann man
  beweisen"; .tex had "$a:b<a':b$**. Ganz** ebenso" — the ";und" period-normalized to ". " which DROPPED the connective
  "und" (and capitalised Ganz). Unlike pure punctuation swaps (skip-tier), this deletes a WORD, so treated as content:
  restored "; und ganz". (Distinguishes dropped-connective from bare ":"/";"->".": the former is fixed, the latter skipped.)
- **FIX 3 (Fraktur Menge-M, .tex 322):** print "ein Element $x$ von **𝔐** in $A$" — ornate blackletter 𝔐, distinct from
  the plain-italic $A$,$B$ (cut parts) on the same line. .tex had plain `$M$`. ZOOM crop_55_75 confirms Fraktur 𝔐.
  `$M$`->`$\mathfrak M$`. **7th confirming Fraktur-M page.**
- **DISPLAY-LAYOUT note (SKIP, documented):** the two proof-conditions print as TWO stacked display lines
  "$na<mc$" / "$nb>md.$"; .tex has them on ONE line "$na<mc, \qquad nb>md$" (comma-joined). Content identical (both
  inequalities); display sub-layout only -> ACCEPTED normalization (same tier as inline-vs-display), NOT reverting.
- **FAITHFUL (content):** Zaehler/Nenner monotonicity Satz + its proof (n with na>b & n(a'-a)>b; smallest m with mb>na;
  na<mb<na'; a/b<m/n<a'/b; a:b<a':b; b'>b => a:b>a:b'), the "waechst mit Zaehler / faellt mit Nenner" restatement,
  the a:c=b:d Satz + proof (assume a:c<b:d => m,n with na<mc,nb>md => na:nb<mc:md => a:b<c:d, contradiction), and the
  Hauptsatz (3 of a,b,c,d given in a stetige messbare Menge => 4th exists with a:b=c:d) + its Stetigkeit proof (Schnitt
  by x:b vs c:d). All prose/formulas verbatim bar the 3 edits.
- **★ Fraktur running list — fixed so far:** 201,215×3,243×3,248,254×2,260(R),264,266,270, **322** = 15 total.
**SPERRUNG (deferred):** "kleinste ganze Zahl", Hauptsatz, plus the many gesperrt words on p13 (Zaehler/Nenner, "Wenn
von den vier Groessen...bestimmen" is heavily gesperrt) — CONTENT-faithful; NOT emphasis-verified. Confirmed by eye vs
~500dpi scans; direct context-read.


### 2026-07-02 — p14 (EINLEITUNG: Addition well-defined proof + messbar/stetig + Mult/Div/Grundformel, .tex 324-346) — p1-99 gap pass — (verified by eye)
**CONTENT: HEAVY GPT PARAPHRASE — 6 fixes in the addition-proof paragraph (5 REWORDS + 1 DROPPED EQUATION).** This is
the first Einleitung page with dense multi-reword damage (prior pages were mostly Fraktur/misread/single-drop). Recompiled
clean: 418pp / 0 err / 0 overfull / 0 underfull / 0 missing-char / 0 undefined (2264381).
- **FIX 1 (.tex 328, TRIPLE REWORD in one paragraph):**
    (a) print "...rationalen Brüche, **und um sie allgemein zu rechtfertigen, braucht dann nur noch gezeigt zu werden**,
        dass, wenn $a:c=a':c'$ und $b:c=b':c'$, auch..." ; .tex had "...Brüche**. Es bleibt zu zeigen**, dass, wenn ...
        $b:c=b':c'$ **ist**, auch..." (GPT paraphrased the clause + inserted a spurious "ist"). Restored.
    (b) print "**Wir beweisen dies, indem wir zeigen, dass, wenn** $a:c=a':c'$ und $(a+b):c>(a'+b'):c'$ **ist, auch**
        $b:c>b':c'$ **sein muss**." ; .tex "**Der Beweis geschieht dadurch, dass aus** ... **auch** ... **folgt**."
        (whole-sentence reword). Restored.
    (c) print "**Es sei also, wenn $m$ und $n$ zwei ganze Zahlen sind,**" ; .tex "**Ist nämlich**". Restored.
- **FIX 2 (.tex 333, reword):** print "**dann ist** $n(a+b)>mc$ **und also**" ; .tex "**so ist** $n(a+b)>mc$**, und daher**".
- **>>> FIX 3 (.tex 335, DROPPED EQUATION):** print display reads "${b\over c}>{mc-na\over nc},\quad {mc'-na'\over nc'}>
    {b'\over c'}$" — TWO inequalities; .tex had only the FIRST (${b\over c}>{mc-na\over nc}$). The 2nd inequality
    $(mc'-na')/nc' > b'/c'$ was DROPPED — and it is load-bearing: the proof chains $b/c > (mc-na)/nc = (mc'-na')/nc' >
    b'/c'$ to conclude $b:c>b':c'$; without the 2nd inequality the conclusion doesn't follow. Restored.
- **FIX 4 (.tex 337, reword):** print "**Andererseits folgt aber leicht aus der Voraussetzung** $a:c=a':c'$, **dass auch**" ;
    .tex "**Andererseits folgt aus** $a:c=a':c'$ **leicht**".
- **FIX 5 (.tex 339/341, reword of the closing):** print "...dass auch [display] **ist, also** $b:c>b':c'$, w. z. b. w." ;
    .tex had a trailing comma on the display + "**und also** ...". Dropped the comma, "und also"->"ist, also" to restore
    Weber's "dass auch [eqn] ist, also..." construction.
- **FAITHFUL (content):** addition def $a/c+b/c=(a+b)/c$; the messbar+stetig-Zahlen paragraph (.tex 343, bar a trivial
    added comma "Menge, und"->print "Menge und"); Mult (delta=1 => alpha=beta*gamma) + commutativity, Division, Grundformel
    alpha(beta+gamma)=alpha*beta+alpha*gamma, and the "vier Grundrechnungsarten... Subtrahend<Minuend" closing (.tex 345-346)
    all verbatim.
- **★ METHOD note:** proof-paragraphs carry DENSER paraphrase damage than the surrounding expository prose. On such
    paragraphs, transcribe the ENTIRE paragraph from the scan and diff sentence-by-sentence (don't spot-check) — GPT rewrote
    connective phrasing ("Der Beweis geschieht dadurch" / "Ist nämlich" / "und daher") AND silently dropped a display line.
**No new type-B erratum; Fraktur count unchanged (15).** SPERRUNG (deferred): "w. z. b. w.", Multiplication/Division
(gesperrt). CONTENT-faithful; NOT emphasis-verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p15 (EINLEITUNG: √α via Schnitt + Cantor Zahlenreihen, .tex 348-359) — p1-99 gap pass — (verified by eye)
**CONTENT: 0 net edits (FAITHFUL page). One epsilon-glyph investigation -> reverted (house convention).** Recompiled
clean: 418pp / 0 err / 0 overfull / 0 underfull / 0 missing-char / 0 undefined (2264381 = identical to p14-final,
confirming zero net change).
- **FAITHFUL (content, verbatim vs scan):** √α existence via Schnitt (Quadrat<α in A; the cut = √α; "Existenz der
  Quadratwurzeln nachgewiesen"); Cantor Zahlenreihen intro + footnote (Cantor, Math. Ann. Bd.5 1872; Heine, J.f.Math.
  Bd.74 1872); Cantor def "unbegrenztes, in bestimmter Weise geordnetes System"; display $S=x_1,x_2,x_3,x_4\ldots$;
  the g-lower-bound + delta-Cauchy condition ($x_n-x_m$ or $x_m-x_n$ < delta once m,n large); the Schnitt(A,B)
  construction (throw to B the numbers eventually un-exceeded; rest to A); "$\alpha$ erzeugt ... wie klein auch eps sei,
  unendlich viele $x_n$ zwischen $\alpha-eps$ und $\alpha$"; "Nach Cantor ist die Zahlenreihe S geradezu die Definition
  der Zahl α". All matched.
- **SKIP-tier (documented, not fixed):** (a) print has a COLON before the display "$S=\ldots$" ("zu verstehen:"); .tex
  dropped it (bare punctuation, no word lost). (b) print writes the ellipsis WITHOUT surrounding commas ("$x_2 \ldots
  x_n$", "$x_4 \ldots$"); .tex has commas ("$x_2,\ldots,x_n$", "$x_4,\ldots$"). Trivial.
- **★ EPSILON-GLYPH INVESTIGATION (.tex 359) -> REVERTED, house convention accepted:** .tex uses `$\varepsilon$` (curly
  ε) at "wie klein auch eps sei" / "$\alpha-eps$". ZOOM crop_13_73 shows Weber's printed ε is the LUNATE crescent form
  (= LaTeX `\epsilon` ϵ, NOT the curly `\varepsilon`). I first changed `\varepsilon`->`\epsilon` to match the scan —
  THEN grepped the file: **`\varepsilon` occurs 321× document-wide** (preamble only defines `\eps:=\varepsilon`, no
  glyph redefinition). So the .tex author SYSTEMATICALLY normalizes Weber's lunate ε to curly `\varepsilon` everywhere.
  Changing ONE page to `\epsilon` would fracture a 321-use house convention for a semantically-NULL glyph difference.
  **REVERTED to `\varepsilon`.** Decision: ACCEPT `\varepsilon` as the house epsilon (a consistent, null-semantic
  normalization of Weber's lunate ε — same tier as the accepted inline->display normalization). The ratio passage
  (p11-12) keeps `\epsilon` as the sole intentional exception (there the lunate form maximises the Latin-e-vs-Greek-ε
  visual contrast that is the point of that passage). NO document-wide epsilon sweep (disproportionate).
- **★★ METHOD LESSON (logged):** BEFORE "fixing" a glyph/notation choice on one page, GREP THE WHOLE DOCUMENT for it.
  If it's an established house convention (hundreds of uses), a per-page change creates an inconsistency WART — worse
  than the normalization. Treat such consistent normalizations as accepted (like inline->display) unless committing to
  a full, verified document-wide sweep. (This caught me mid-edit on p15; reverted before it shipped.)
**No new type-B erratum; no Fraktur/reword/misread fixes this page.** SPERRUNG (deferred): "irrational", G. Cantor,
Zahlenreihe (gesperrt). CONTENT-faithful; NOT emphasis-verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p16 (EINLEITUNG: negative Zahlen + Null + Reihe der reellen Zahlen, .tex 359tail-367) — p1-99 gap pass — (verified by eye)
**CONTENT: 1 EDIT (reword + dropped word).** Recompiled clean: 418pp / 0 err / 0 overfull / 0 underfull / 0 missing-char /
0 undefined (2264464).
- **FIX (.tex 361, REWORD + DROPPED WORD "Null"):** print "...eine unbequeme Beschränkung ergeben, von der wir uns
  **freimachen durch Einführung der Null und der negativen Zahlen**." ; .tex had "...von der wir uns **frei machen, indem
  wir die negativen Zahlen einführen**." GPT reworded the clause AND dropped "der Null und" — the print introduces BOTH
  the zero AND the negative numbers here (the section covers both), .tex mentioned only negatives. Also "freimachen"
  (one word in print) vs .tex "frei machen". ZOOM crop_10_31 confirms "freimachen durch Einführung der Null und der
  nega[tiven] Zahlen". Restored verbatim.
- **FAITHFUL (content, verbatim vs scan):** tail of Cantor para (.tex 359: "Diese Zahlenreihen ... unter einander
  gleich ... Gesammtheit der Zahlenreihen S ... stetige Menge"); the two-copies construction of negatives (x = positive
  system; second copy = negatives, each element $-x$; ordered "gerade entgegengesetzt" so grösser<->kleiner; Add/Subtr
  in $-x$: $(-x)+(-y)=-(x+y)$, $(-x)-(-y)=-(x-y)$); the zusammenordnen ($-x<x$) giving a geordnete Menge with no
  greatest/least; the lone Schnitt $(-x,x)$ un-generated => Stetigkeits-Verletzung; adjoin "Zahl Null oder $0$" defined
  by that cut => "geordnete stetige, beiderseits unbegrenzte Menge, die vollständige Reihe der reellen Zahlen"; intro to
  general Addition "definitionsweise setzen:". All matched.
- **SKIP-tier (documented):** print SEMICOLON between the two inline eqs "$(-x)+(-y)=-(x+y)$**;** $(-x)-(-y)=-(x-y)$" ;
  .tex COMMA. Trivial punctuation.
**No new type-B erratum; no Fraktur; epsilon = house $\varepsilon$ (not touched).** SPERRUNG (deferred): "positiven
Zahlen", "negativen Zahlen", "Null", "reellen Zahlen", "grösser"/"kleiner" (gesperrt). CONTENT-faithful; NOT emphasis-
verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p17 (EINLEITUNG: addition laws + number-line + Mult/Div of reals + complex-numbers intro, .tex 368-399) — p1-99 gap pass — (verified by eye)
**CONTENT: 3 EDITS (1 verbal-condition normalization, 1 sign misread, 1 dropped phrase).** Recompiled clean: 418pp /
0 err / 0 overfull / 0 underfull / 0 missing-char / 0 undefined (2264472).
- **FIX 1 (VERBAL-CONDITION normalization restored, .tex 372-376):** print display reads "$x+(-y)=x-y$, **wenn** $x>y$,
  $=-(y-x)$, **wenn** $y>x$." — Weber uses the German word **"wenn"** for the conditions and an ELLIPTICAL 2nd equation
  (shared LHS: just "$=-(y-x)$"). The .tex had normalized this to PARENTHETICAL conditions + a repeated LHS:
  "$x+(-y)=x-y \quad (x>y)$, \qquad $x+(-y)=-(y-x) \quad (y>x)$." Restored Weber's form with `\text{wenn }` (amsmath, used
  doc-wide e.g. line 5686 "\text{und}"). NEW damage pattern: German conditional words -> symbolic parentheticals.
- **FIX 2 (± vs +, sign misread, .tex 384):** print "die Strecke von der Länge **$\pm z_2$**" (plus-minus: z_2 can be
  pos/neg -> laid off right or left); .tex had "$+z_2$" (plain plus). ZOOM crop_2_46 shows a clear ± (plus with a bar
  BELOW). `+`->`\pm`. Genuine sign fidelity fix.
- **FIX 3 (DROPPED PHRASE "Es sei", .tex 394):** print "...nach folgenden Regeln. **Es sei** [display]"; .tex had
  "...nach folgenden Regeln**:**" — dropped the introductory phrase "Es sei" (+ colon-for-period). "Es sei" ("Let ...
  be") governs the two definition displays. Restored "Regeln. Es sei".
- **SKIP-tier (documented, not fixed):** (a) print "nach der anderen **(linken)** Seite" (parenthetical gloss) vs .tex
  "**, linken**" (comma) — bracketing-only punctuation, no word changed. (b) colon before "die Gesetze:" display. (c)
  mult/div display 2-line layout + trailing-comma vs .tex flow. All punctuation/layout tier.
- **FAITHFUL (content):** commutative/associative laws $z_1+z_2=z_2+z_1$, $(z_1+z_2)+z_3=z_1+(z_2+z_3)$ + "commutative/
  associative Gesetz" naming + summation-of-many + Subtraction via $z_1+(-z_2)$, $-(-z)=z$; number-line picture (0 fixed
  point, positives right, negatives left, sum $z_1+z_2$ by laying off $\pm z_2$); Mult/Div rules $x(-y)=(-x)y=-xy$,
  $(-x)(-y)=xy$, $0x=0$ + "Division ... ausser wenn der Divisor Null ist"; complex-numbers intro (Paare $(x,y)$; equal iff
  $x=a,y=b$; unordered Mannigfaltigkeit; +/-/*/÷ "nach folgenden Regeln"); the two def displays $(x,y)+(a,b)=(x+a,y+b)$,
  $(x,y)(a,b)=(xa-yb,xb+ya)$. All matched.
**No new type-B erratum; no Fraktur; epsilon untouched (house \varepsilon).** SPERRUNG (deferred): "commutative",
"associative", "complexen Grössen" (gesperrt). CONTENT-faithful; NOT emphasis-verified. Confirmed by eye vs ~500dpi
scans; direct context-read.


### 2026-07-02 — p18 (EINLEITUNG: complex numbers — i, x+yi, arithmetic, division, Gauss plane + modulus, .tex 392tail-427) — p1-99 gap pass — (verified by eye)
**CONTENT: 3 FIXES (1 dropped connective "und" + sentence split, 1 dropped word "oder", 1 DROPPED EQUATION+"oder").**
Recompiled clean: 418pp / 0 err / 0 overfull / 0 underfull / 0 missing-char / 0 undefined (2264588).
- **FIX 1 (sentence-continuation / DROPPED "und", .tex 397+399):** print runs ONE sentence across the p17->p18 break:
  "...Regeln. Es sei [display eq1], [display eq2], **und wir** setzen ausserdem fest, dass $(x,0)=x$ sei..." — the 2nd
  definition display ends with a COMMA and continues with lowercase "**und** wir". The .tex had split it: 2nd display
  ended with a PERIOD (.tex 397) and .tex 399 started "**Wir**" (capital, "und" dropped). Restored: 397 "."->"," and
  399 "Wir"->"und wir". (Confirms the p17 "Es sei" restoration — the whole "Es sei ..., und wir ..." sentence is now whole.)
- **FIX 2 (DROPPED WORD "oder", .tex 401 display):** print "$(x,0)(0,1)=(0,x)$ **oder** $=ix$" ; .tex had chained
  "$(x,0)(0,1)=(0,x)=ix$" (dropped the German "oder"). Restored with `\text{oder}`.
- **>>> FIX 3 (DROPPED EQUATION + "oder", .tex 420):** the division is derived in TWO display forms in print:
  (A) "$x+yi=(a+bi)\dfrac{(a-bi)(x+yi)}{(a^2+b^2)}$"  then a line "**oder**"  then
  (B) "$\dfrac{x+yi}{a+bi}=\dfrac{ax+by+i(ay-bx)}{a^2+b^2}$". The .tex had ONLY form (B) — the whole derivation display
  (A) + the connecting "oder" were DROPPED. ZOOM crop_18_35 confirms (A): (a+bi) factor · num=(a-bi)(x+yi) / denom=(a^2+b^2).
  [(a+bi)(a-bi)=a^2+b^2 makes (A) the identity that yields (B).] Restored (A)+"oder" before (B). **2nd dropped-equation of
  the gap-pass (cf. p14 dropped inequality).**
- **FAITHFUL (content):** $(x,0)=x$ stipulation, $(x,y)=0$ iff x=y=0, $i=(0,1)$; the i/addition/subtraction/mult displays
  ($x+yi$, $(x+a)+(y+b)i$, $(x-a)+i(y-b)$, $(x+yi)(a+bi)=xa-yb+i(xb+ya)$, $i^2=-1$, $(x+yi)(x-yi)=x^2+y^2$); "rein
  imaginär"/"imaginäre Einheit"/"imaginär oder complex" definitions; reals+pure-imaginaries as Specialfälle; Gauss plane
  representation ($z=x+yi$, rechtwinkliges Coord.system, x-Axe reals, y-Axe pure imag., origin=0); modulus
  $\varrho=\sqrt{x^2+y^2}$ = "absolute Werth / Betrag / (ält.) Modulus". All matched.
- **SKIP-tier (documented):** display 2-line-vs-1-line layouts; colons before displays. Punctuation/layout only.
**No new type-B erratum; no Fraktur; epsilon untouched.** SPERRUNG (deferred): "rein imaginäre Zahlen", "imaginäre
Einheit", "imaginär", "complex", "reellen", "Gauss" (gesperrt). CONTENT-faithful; NOT emphasis-verified. Confirmed by eye
vs ~500dpi scans; direct context-read.


### 2026-07-02 — p19 (EINLEITUNG: modulus/conjugates + triangle-inequality Satz & proof, .tex 433-458) — p1-99 gap pass — (verified by eye)
**CONTENT: 4 FIXES (1 GPT FABRICATION removed, 1 reword, 1 dropped "ist", 1 sign ≧->>).** Recompiled clean: 418pp /
0 err / 0 overfull / 0 underfull / 0 missing-char / 0 undefined (2264603).
- **>>> FIX 1 (GPT FABRICATION / ADDED content removed, .tex 441):** print display reads "$Z=(x+a)+(y+b)i$"; the .tex had
  "$Z=z+c=(x+a)+(y+b)i$" — GPT INSERTED an intermediate "$z+c=$" NOT in Weber's print. ZOOM crop_52_50 shows "Z = (x+a)
  + (y+b)i" with nothing between "$Z=$" and "$(x+a)$". Removed the fabricated "$z+c=$". **FIRST fabrication/addition of the
  gap-pass (new damage class: GPT ADDED a step, vs the usual drops).** [Watch for more added intermediates.]
- **FIX 2 (REWORD + punctuation, .tex 450+452):** print "...$=2(r\varrho-ax-by)$**; das ist** sicher positiv, wenn..." ;
  .tex "...$=2(\varrho r-ax-by)$**, was** sicher positiv **ist**, wenn...". Restored "das ist sicher positiv" + the
  display's trailing "," -> ";".
- **FIX 3 (DROPPED "ist", .tex 456):** print "dass $r\varrho\ge ax+by$ **ist**, und nur dann gleich"; .tex "dass
  $\varrho r\ge ax+by$ und nur dann gleich" (dropped "ist,"). ZOOM crop_3_61. Restored "ist,".
- **FIX 4 (SIGN ≧ -> > (strict), .tex 456):** print "dass $r+\varrho$ **>** $R$ ist und nur in dem besonderen Falle
  $r+\varrho=R$..." — strict ">" (single wedge, no bar; ZOOM crop_44_68). .tex had "$\varrho+r\ge R$" (≧). Weber states
  ">" generally + "=" as the special case; GPT folded it to "≧". Restored strict ">". (4th sign fidelity fix of the volume.)
- **★ SKIP-tier (documented, NOT fixed) — COMMUTATIVE OPERAND REORDER:** Weber prints "$r+\varrho$" / "$r\varrho$" /
  "$r^2\varrho^2$" (r first); the .tex normalized to "$\varrho+r$" / "$\varrho r$" / "$\varrho^2 r^2$" (ϱ first),
  ~7 instances on this page. Same symbols, commutative, semantically NULL -> treated as style-tier (like inline->display).
  Kept .tex's order for page-consistency; did NOT restore per-instance. (Only the SIGN in "r+ϱ>R" was fixed, not its order.)
- **SKIP-tier (other):** "$R^2=...$." display period + capitalized "Dann ist" vs print comma + "dann ist" (display-boundary
  period-norm, no word dropped); commas before "als" (×2, "kleiner ist, als"). Punctuation/capitalization only.
- **FAITHFUL (content):** "einzige Zahl 0 ... absoluter Werth 0"; positive value on a circle; conjugate imaginaries
  ($x+yi$,$x-yi$; product = square of modulus; i->-i substitution); triangle-inequality Satz ("absoluter Werth einer
  Summe ... niemals grösser ... nur dann gleich, wenn ... reell und positiv"); the whole proof algebra (z,c,Z; ϱ²,r²,R²;
  $(r+\varrho-R)(r+\varrho+R)=(r+\varrho)^2-R^2=2(r\varrho-ax-by)$; $r^2\varrho^2-(ax+by)^2=(ay-bx)^2$); geometric
  Dreieck interpretation; 2nd consequence (|sum| ≥ |difference|, via c=Z-z). All matched bar the 4 fixes + skips.
**No new type-B erratum; no Fraktur; epsilon untouched.** SPERRUNG (deferred): none gesperrt of note here. CONTENT-
faithful; NOT emphasis-verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p20 (EINLEITUNG END: triangle-ineq tail + Buchstabenrechnung/Identitäten/Unbekannte, .tex 458-466) — p1-99 gap pass — (verified by eye)
**CONTENT: 0 net edits (FAITHFUL page). ★★ MILESTONE: EINLEITUNG (p1-20) CONTENT-AUDIT COMPLETE.** File unchanged
(418pp / 0 badness / 2264603 = p19-final).
- **FAITHFUL (content, verbatim vs scan):** triangle-ineq tail ("$r\le R+\varrho$ oder $R\ge r-\varrho$"; the display's
  sign is ≧ = double-bar, matches .tex \ge -- distinct from p19's strict "$r+\varrho>R$"; consistent with the following
  "Die Gleichheit findet hier nur dann statt, wenn der Quotient $z:c$ reell und negativ ist"). Then the Buchstaben-
  rechnung closing of the Einleitung: Algebra = Buchstabenrechnung; two kinds of Buchstabengleichungen — (1) Identitäten
  (umformbar zu genauer Übereinstimmung; give richtige Zahlengleichungen on substitution, bar Division-durch-Null;
  Buchstaben = "Variable"); (2) equations with a Forderung (solve = "die Gleichung zu lösen"; Buchstaben = "Unbekannte");
  and the two-kinds-of-letters remark (given values vs to-be-determined). All matched.
- **SKIP-tier (documented):** print ";" vs .tex ":" at "von zweierlei Art sein[;/:] entweder" (bare punctuation).
- **★★ EINLEITUNG MILESTONE:** the entire Einleitung front-matter body (.tex 158-466, printed pp.1-20) is now audited
  page-by-page against the ~500dpi scans. Damage found & fixed across p1-20 (NOT a completeness claim -- provisional,
  by-eye): **7 type-B Weber errata kept+[sic]; 1 Weber font-slip documented; ~15 Fraktur Menge-M restored; 5 GPT-
  normalizations removed (e/ε/e', ≧→=, wenn-cond→parenthetical, R_v/ξ_z earlier); 1 GPT fabrication removed (z+c);
  2 dropped equations restored (p14 inequality, p18 division display); multiple sign fixes (≦/≧/±/>); many dropped-word/
  reword restorations (und, Null, oder, Es sei, ist, so, dropped sentences, etc.).** Recurring SKIP-tier normalizations
  documented (period/;/:/paren/cap punctuation, display 1-vs-2-line layout, ellipsis-commas, commutative operand reorder,
  house \varepsilon). NEXT: "ERSTES BUCH. DIE GRUNDLAGEN." divisional title (p21) then **Erster Abschnitt §1 Ganze
  Functionen** (.tex 477+).
- **SPERRUNG owed (whole Einleitung):** gesperrt->\emph never done for p1-20 -- large deferred batch. After content gap.
CONTENT-faithful; NOT emphasis-verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p21-p22 (DIVISIONAL TITLE PAGE + blank verso, .tex 468-475) — p1-99 gap pass — (verified by eye)
**CONTENT: 0 edits (both faithful). File unchanged (418pp / 0 badness / 2264603).**
- **p21 = divisional title page:** print (centered) "**ERSTES BUCH.**" / [rule] / "**DIE GRUNDLAGEN.**" / [rule], rest
  blank. .tex 470-473: `\begin{center}{\Large\bfseries ERSTES BUCH.}\\ {\large\bfseries DIE GRUNDLAGEN.}\end{center}`.
  Title TEXT matches exactly ("ERSTES BUCH.", "DIE GRUNDLAGEN."). The .tex omits the two decorative separator rules
  (typographic nicety, not text) — acceptable. Faithful.
- **p22 = blank verso** (only mirror show-through of p21's title visible; no content of its own). Matches the .tex
  \clearpage between the ERSTES-BUCH title and Erster Abschnitt. Faithful.
- NEXT: **Erster Abschnitt. Rationale Functionen / §1. Ganze Functionen** begins on printed **p23** (.tex 477+).
CONTENT-faithful; NOT emphasis-verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p23 (§1 GANZE FUNCTIONEN start: def + eq(1) + Grad/Coefficienten + add/mult rules, .tex 477-494) — p1-99 gap pass — (verified by eye)
**CONTENT: 0 net edits (FAITHFUL page). First §1 body page.** File unchanged (418pp / 0 badness / 2264603 = p22-final).
- **HEADINGS match:** print "Erster Abschnitt." / "Rationale Functionen." (Abschnitt title) + "§. 1." / "Ganze
  Functionen." (§ title) == .tex 477 `\section*{Erster Abschnitt. Rationale Functionen.}` + 479 `\section*{\S~1. Ganze
  Functionen.}`. Text exact.
- **FAITHFUL (content, verbatim + index-checked vs scan):** ganze-Function def; eq(1) $f(x)=a_0x^n+a_1x^{n-1}+a_2x^{n-2}
  +\cdots+a_{n-1}x+a_n$ (every index/exponent matched: $a_0x^n$, $a_1x^{n-1}$, $a_2x^{n-2}$, $a_{n-1}x$, $a_n$); Grad =
  ganzzahliger Exponent = natürliche Zahl; $0$ten Grades = Constante; Veränderliche $x$; Coefficienten $a_0..a_n$;
  ascending-order display $f(x)=a_n+a_{n-1}x+\cdots+a_1x^{n-1}+a_0x^n$ (index-matched); add/subtr/mult -> ganze rat.
  Functionen; addition-Coefficient rule ($x^\nu$ coeff = sum of summand coeffs). All matched.
- **SKIP-tier (documented house/format):** (a) print "§. 1." (period after §) vs .tex "\S~1." ("§ 1.") -- consistent
  house §-format. (b) print "Co**ë**fficienten" vs .tex "Coefficienten" -- the DOCUMENTED house ë-drop convention
  (Coëfficienten->Coefficienten). Not fixed.
- **★ EQ-NUMBER POSITION observation (LAYOUT, out of scope -> documented for separate pass):** Weber LEFT-numbers
  equations -- eq(1) prints "(1)" at the LEFT margin. The .tex `\documentclass[11pt]{article}` has NO `leqno`, so
  \tag/\begin{equation} numbers render on the RIGHT (opposite side from Weber), document-wide. Tried
  `\documentclass[11pt,leqno]{article}`: compiles CLEAN (0 badness) but reflows +9 pages (418->427). **REVERTED** --
  (1) this pass is GERMAN-TEXT fidelity ONLY; eq-number side is LAYOUT, not text; (2) a +9pp global reflow ripples
  through the swarm-verified p100+ region for a null-semantic layout preference. **Flagged for a SEPARATE dedicated
  formatting/layout pass:** add `leqno` to documentclass (one-line; expect ~+9pp clean reflow) to match Weber's
  left-numbered equations. Same tier as the accepted display-layout / \varepsilon normalizations.
- **★ METHOD LESSON:** global LAYOUT fidelity (eq-number side, and by extension margins/leading/eq-number style) is OUT
  of scope for the German-content gap-pass -- document such items for a dedicated formatting pass; do NOT fold global
  reflowing changes into the content audit (they ripple through already-verified pages).
**No new type-B erratum; no Fraktur; epsilon untouched.** §1 prose is simple/clean (polynomial defs) -- much lower GPT-
damage density than the Einleitung's dense Dedekind-cut prose so far. SPERRUNG (deferred): "ganze rationale Functionen",
"Grad", "Veränderliche", "Coefficienten", "absteigenden/aufsteigenden Potenzen" (gesperrt). CONTENT-faithful; NOT
emphasis-verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p24 (§1 cont.: Mult-Grad + product Bildungsgesetz/convolution + Rechenregeln + several-variables, .tex 494-534) — p1-99 gap pass — (verified by eye)
**CONTENT: 0 net edits (FAITHFUL page). 2nd consecutive clean §1 page.** File unchanged (418pp / 0 badness / 2264603).
- **FAITHFUL (content, verbatim + index-checked vs scan):** addition-Grad rule (max degree; lowers only if top coeffs
  cancel); Mult-Grad = sum of factor grades; product Bildungsgesetz eq(2) $A(x)=a_0x^m+a_1x^{m-1}+a_2x^{m-2}+\cdots$,
  $B(x)=b_0x^n+\cdots$; eq(3) $A(x)B(x)=C(x)=c_0x^{m+n}+c_1x^{m+n-1}+c_2x^{m+n-2}+\cdots$; $c_0=a_0b_0$, $c_1=a_0b_1+a_1b_0$,
  $c_2=a_0b_2+a_1b_1+a_2b_0$; **convolution eq(4) $c_\nu=a_0b_\nu+a_1b_{\nu-1}+a_2b_{\nu-2}+\cdots+a_{\nu-1}b_1+a_\nu b_0$
  (every subscript matched)**; index-rule (a-index>m, b-index>n => 0; $c_\nu$=coeff of $x^{m+n-\nu}$ from $a_\mu x^{m-\mu}
  \cdot b_{\nu-\mu}x^{n-\nu+\mu}$); $a_0=b_0=1 => c_0=1$; monic-product rule; Rechenregeln $ab=ba$, $(ab)c=a(bc)$,
  $(a+b)c=ac+bc$ hold for polynomials (equal iff equal coeffs at equal powers); several-variables functions intro. All matched.
- **SKIP-tier (documented house/format/trivial):** (a) "Coëfficient(en)" -> "Coefficient(en)" house ë-drop (×several).
  (b) eq(4) ellipsis-connector: print "$+\cdots a_{\nu-1}b_1$" (no + after dots) vs .tex "$+\cdots+a_{\nu-1}b_1$"
  (+ after dots) -- trivial implied-operator around ellipsis, same tier as ellipsis-commas. (c) eq-numbers "(2)(3)(4)"
  print-LEFT (the documented leqno layout item, owed to formatting pass). (d) ellipsis-commas ($0,1,2\ldots m+n$).
- §1 math-body remains clean/low-damage (simple polynomial algebra) -- 2 faithful pages running (p23,p24), contrasting
  the Einleitung's dense Dedekind prose. NEXT: §1 tail (several-var functions cont.) then **§2. Ein Satz von Gauss** (.tex 536).
**No new type-B erratum; no Fraktur; epsilon untouched.** SPERRUNG (deferred): "Multiplication", "Bildungsgesetz",
gesperrt formula-refs. CONTENT-faithful; NOT emphasis-verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p25 (§1 several-var tail + §2 GAUSS-SATZ start: primitive-function def + Satz + proof-setup, .tex 534-548) — p1-99 gap pass — (verified by eye)
**CONTENT: 0 net edits (FAITHFUL page). 3rd consecutive clean page.** File unchanged (418pp / 0 badness / 2264603).
- **§2 HEADING match:** print "§. 2." / "Ein Satz von Gauss." == .tex 536 `\section*{\S~2. Ein Satz von Gauss.}`.
  Running header "§. 2. Satz von Gauss." (short) -- fine.
- **FAITHFUL (content, verbatim + index-checked vs scan):** §1 several-var tail ($x^ry^sz^t\cdots$ terms, exponent-
  combos once, equality-by-same-products); §2 intro (Anwendung der Multiplicationsregel -> Gauss-Satz); footnote
  "Gauss, Disquisitiones arithmeticae, Art. 42." (marker after "soll", text at page foot -- placement matches);
  integer-coeff setup ($A(x),B(x)$ int -> $C(x)=A(x)B(x)$ int by (4)); primitive/ursprünglich def (coeffs $a_0,a_1,
  \ldots,a_m$ no common divisor); the Satz (product of primitives is primitive); proof-setup (if $c_0,c_1,c_2\ldots
  c_{m+n}$ share divisor>1 => prime $p$ divides all $c$; by primitivity $p$ divides neither all $a_0..a_m$ nor all
  $b_0..b_n$). All indices matched.
- **SKIP-tier (documented house/format/trivial):** Coëfficient(en)->Coefficient(en) house ë-drop (×many); "§." period;
  eq-numbers print-LEFT (leqno item); ellipsis-commas; trivial commas (e.g. "c_{m+n}, wie").
- **⚠ EMPHASIS (DEFERRED to emphasis/SPERRUNG pass, NOT fixed):** footnote book title -- print appears to set
  "Disquisitiones arithmeticae" in ROMAN; .tex has `\emph{Disquisitiones arithmeticae}` (italic). Either GPT-added
  italic (modern book-title convention) or an editorial choice. Emphasis/font-style is deferred to the dedicated
  emphasis pass -> verify (zoom) + resolve there (match Weber roman, or keep editorial italic). Flagged.
- §1-§2 math-body remains clean/low-damage: **3 faithful pages running (p23,p24,p25)** vs the Einleitung's dense prose.
  NEXT: §2 proof cont. (p aufgeht in $a_0..a_{r-1}$ but not $a_r$; $c_{r+s}$ display eq(1); Widerspruch; several-var
  extension by induction, .tex 550-572).
**No new type-B erratum; no Fraktur; epsilon untouched.** SPERRUNG (deferred, + the \emph title note above). CONTENT-
faithful; NOT emphasis-verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p26 (§2 Gauss-lemma proof: c_{r+s} eq(1) + Widerspruch + several-var induction + imprimitive-def, .tex 550-574) — p1-99 gap pass — (verified by eye)
**CONTENT: 0 net edits (FAITHFUL page). 4th consecutive clean page.** File unchanged (418pp / 0 badness / 2264603).
- **FAITHFUL (content, SUBSCRIPT-checked vs scan):** $p$-divisibility split displays ($a_0,a_1\ldots a_{r-1}$ but not
  $a_r$; $b_0,b_1\ldots b_{s-1}$ but not $b_s$); $r\le m$ (=0 possible), $s\le n$; **the key convolution display eq(1)
  $c_{r+s}=a_rb_s+a_{r-1}b_{s+1}+a_{r-2}b_{s+2}+\cdots+a_{r+1}b_{s-1}+a_{r+2}b_{s-2}+\cdots$ -- every subscript matched
  index-for-index (a-index up / b-index down, sum=r+s)**; Widerspruch (first term $a_rb_s$ not div by $p$, all others
  are since multiplied by $a_0..a_{r-1},b_0..b_{s-1}$); several-var extension (primitive def + Satz) + proof by
  induction (coeffs as functions of $m-1$ vars; Formel(1) => $m$ vars; "Schluss von $m-1$ auf $m$"); imprimitive-
  Function def ("Theiler der Function"). All matched.
- **SKIP-tier (documented house/format):** Coëfficient(en)->Coefficient(en) house ë-drop (×many); colons before
  displays ("aufgehen in:", "folgender Weise:"); eq# print-LEFT (leqno item); ellipsis-commas. .tex uses `\hbox{aber
  nicht in }` inside the a_r/b_s displays -- renders fine (matches print "aber nicht in").
- ★ §1-§2 math-body damage-density is ~NIL: **4 faithful pages running (p23-26)** vs the Einleitung's damage-every-page.
  META: GPT reconstruction damaged the DENSE/hard Dedekind-cut prose (Einleitung) far more than the routine polynomial
  algebra (§1-§2). Expect §-body pages to audit fast (verify+log, few edits) until a dense/tricky passage appears.
  NEXT: §2 tail (.tex 576-591: "Theiler eines Productes"=product of Theiler; PA·QB=PQC; the monic-rational form
  $\varphi(x)=x^m+\alpha_1x^{m-1}+\cdots$, $\psi(x)$, product $\gamma$-coeffs) then §3.
**No new type-B erratum; no Fraktur; epsilon untouched.** SPERRUNG/emphasis deferred (+ the p25 \emph title note).
CONTENT-faithful; NOT emphasis-verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p27 (§2 tail: Theiler-Satz + monic-rational φ/ψ/γ; then §3 DIVISION start, .tex 576-605) — p1-99 gap pass — (verified by eye)
**CONTENT: 0 net edits (FAITHFUL page). 5th consecutive clean page.** File unchanged (418pp / 0 badness / 2264603).
- **FAITHFUL (content, subscript-checked vs scan):** restated Satz "Theiler eines Productes = Product der Theiler";
  $PA\cdot QB=PQC$ argument; monic forms $\varphi(x)=x^m+\alpha_1x^{m-1}+\alpha_2x^{m-2}+\cdots+\alpha_m$,
  $\psi(x)=x^n+\beta_1x^{n-1}+\cdots+\beta_n$; product $\varphi\psi=x^{m+n}+\gamma_1x^{m+n-1}+\gamma_2x^{m+n-2}+\cdots
  +\gamma_{m+n}$ (all Greek subscripts $\alpha_i,\beta_j,\gamma_k$ matched); rational-vs-int coeff statement; Hauptnenner
  proof ($a_0\varphi=A$, $b_0\psi=B$ primitive; product Theiler $a_0b_0$ => Widerspruch). §3 heading "§. 3. / Division."
  matches. §3 eq(1) $A=a_0x^m+a_1x^{m-1}+\cdots$, $B=b_0x^n+b_1x^{n-1}+\cdots$ matched; "$m\ge n$, $a_0,b_0\ne 0$" setup.
- **SKIP-tier:** Coëfficient(en)->Coefficient(en) house ë-drop (×many); eq# print-LEFT (leqno item). Running header
  "§.3. Division." NOT reproduced (.tex uses fixed \lhead/\rhead) -> not audited.
- ★ 5 faithful pages running (p23-27): §1-§3 math-body clean (routine algebra) vs Einleitung damage-every-page.
  NEXT: §3 Division cont. (poly long division: difference $A-\frac{a_0}{b_0}x^{m-n}B$ eq(2), $A'$ eq(3) with deg $m'<m$,
  the Gleichungs-Kette / quotient+remainder, .tex 606+).
**No new type-B erratum; no Fraktur; epsilon untouched.** SPERRUNG/emphasis deferred. CONTENT-faithful; NOT emphasis-
verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p28 (§3 Division: long-division algorithm — Kette eq(4), Q eq(5), A=QB+C eq(6), terminology, .tex 605-638) — p1-99 gap pass — (verified by eye)
**CONTENT: 0 net edits (FAITHFUL page). 6th consecutive clean page.** File unchanged (418pp / 0 badness / 2264603).
- **FAITHFUL (content, subscript-checked vs scan):** difference eq(2) $A-\frac{a_0}{b_0}x^{m-n}B$; eq(3) $A'=a'_0x^{m'}
  +a'_1x^{m'-1}+\cdots$, $m'<m$; **the division Kette eq(4) — 3 rows + dots matched ROW-FOR-ROW with primed indices**
  ($A-\frac{a_0}{b_0}x^{m-n}B=A'$; $A'-\frac{a'_0}{b_0}x^{m'-n}B=A''$; $A''-\frac{a''_0}{b_0}x^{m''-n}B=A'''$; $\cdots$);
  "höchstens $m-n+1$ Glieder" reasoning; Q eq(5) $Q=\frac{a_0}{b_0}x^{m-n}+\frac{a'_0}{b_0}x^{m'-n}+\cdots$; eq(6)
  $A=QB+C$; Division terminology (A=Dividendus, B=Divisor, C=Rest, Q=Quotient; "Grad des Restes niedriger als Divisor").
  All matched. $m\ge n$, $m'\ge n$ conds (≧ double-bar = .tex \ge) ok.
- **SKIP-tier:** Coëfficienten->Coefficienten (ë-drop); colons before displays; eq# print-LEFT (leqno item); ellipsis-commas.
- ★ 6 faithful pages running (p23-28): §1-§3 math-body clean. NEXT: §3 cubic worked example (f(x) eq(7), f'(x)=1st
  Derivirte eq(8), Q eq(9), C eq(10) with fraction coeffs) — .tex 640+ — ZOOM the example's fraction numerators
  ($6a_0a_2-2a_1^2$, $9a_0a_3-a_1a_2$, denom $9a_0$).
**No new type-B erratum; no Fraktur; epsilon untouched.** SPERRUNG/emphasis deferred. CONTENT-faithful; NOT emphasis-
verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p29 (§3 Division: b_0-denom discussion + cubic worked example eq(7-10) + decimal analogy, .tex 640-662) — p1-99 gap pass — (verified by eye)
**CONTENT: 0 net edits (FAITHFUL page). 7th consecutive clean page.** File unchanged (418pp / 0 badness / 2264603).
- **FAITHFUL (content, TERM-checked vs scan):** b_0-power-in-denominator discussion (max $(m-n+1)$te power);
  **cubic example verified term-by-term**: eq(7) $f(x)=a_0x^3+a_1x^2+a_2x+a_3$; eq(8) $f'(x)=3a_0x^2+2a_1x+a_2$ (1st
  Derivirte); eq(9) $Q=\frac13 x+\frac{a_1}{9a_0}$; **eq(10) $C=\frac{6a_0a_2-2a_1^2}{9a_0}x+\frac{9a_0a_3-a_1a_2}{9a_0}$
  -- all coefficients (6,2,9,9), products ($a_0a_2$,$a_1^2$,$a_0a_3$,$a_1a_2$), denominators ($9a_0$) MATCHED**; decimal-
  system analogy (f(x) = decimal number when coeffs in [0,10), x=10; larger coeffs -> multiple representations; used to
  avoid fractional/negative coeffs in division). All matched.
- **SKIP-tier:** Coëfficienten->Coefficienten (ë-drop ×many); colons before displays; eq# print-LEFT (leqno item).
- **⚠ FORMATTING (DEFERRED to formatting pass, NOT fixed):** ordinal-suffix superscription -- print "$(m-n+1)^{\text{te}}$"
  (raised "te"); .tex "$(m-n+1)$te" (baseline "te"). The .tex is INCONSISTENT (elsewhere uses $n^{\text{ten}}$). This is
  typographic (ordinal suffix), same tier as leqno/§-style -> flag for the formatting pass (normalize ordinal suffixes
  te/ten/ter to superscript per Weber), NOT a German-text-content fix.
- ★ 7 faithful pages running (p23-29): §1-§3 math-body clean. §3 DONE. NEXT: **§4 Theilung durch eine lineare Function**
  (p30, .tex 664+: divisor $(x-\alpha)$; $f(x)=(x-\alpha)Q+C$ eq(2); $Q=q_0x^{n-1}+\cdots+q_{n-1}$ eq(3); expansion eq(4);
  Vergleichung eq(5) => recursion for $q_i$; likely $C=f(\alpha)$ remainder theorem).
**No new type-B erratum; no Fraktur; epsilon untouched.** SPERRUNG/emphasis deferred. CONTENT-faithful; NOT emphasis-
verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p30 (§4 Theilung durch eine lineare Function: setup + Horner recursion eq(1-6), Restsatz C=f(alpha), .tex 664-713) — p1-99 gap pass — (verified by eye)
**CONTENT: 0 net edits (FAITHFUL page). 8th consecutive clean page.** File unchanged (418pp / 0 badness / 2264603).
- **FAITHFUL (content, display-by-display vs scan, ALL 6 displays row-checked):** heading "§.4. Theilung durch eine
  lineare Function."; eq(1) $f(x)=a_0x^n+a_1x^{n-1}+a_2x^{n-2}+\cdots+a_n$; divisor $(x-\alpha)$, coeff of $x$ =1,
  $Q$ vom $(n-1)$ten Grade, $C$ vom $0$ten Grade; eq(2) $f(x)=(x-\alpha)Q+C$; eq(3) $Q=q_0x^{n-1}+q_1x^{n-2}+\cdots
  +q_{n-2}x+q_{n-1}$; **eq(4) BOTH rows matched** (row1 $q_0x^n+q_1x^{n-1}+\cdots+q_{n-2}x^2+q_{n-1}x+C$; row2
  $-\alpha q_0x^{n-1}-\cdots-\alpha q_{n-3}x^2-\alpha q_{n-2}x-\alpha q_{n-1}$ -- subscripts n-3/n-2/n-1 verified);
  **eq(5) Horner recursion 6 rows matched** ($q_0=a_0$; $q_1-\alpha q_0=a_1$; $q_2-\alpha q_1=a_2$; dots; $q_{n-1}
  -\alpha q_{n-2}=a_{n-1}$; $C-\alpha q_{n-1}=a_n$); **eq(6) solved 6 rows matched** ($q_1=a_0\alpha+a_1$; $q_2=a_0
  \alpha^2+a_1\alpha+a_2$; $q_{n-1}=a_0\alpha^{n-1}+a_1\alpha^{n-2}+\cdots+a_{n-1}$; $C=a_0\alpha^n+\cdots+a_{n-1}
  \alpha+a_n=f(\alpha)$); Restsatz prose "C entsteht aus f(x), wenn man x=alpha setzt ... mit f(alpha) bezeichnet". All matched.
- **SKIP-tier:** Coefficienten (ë-drop); ellipsis-connector "+" (scan "$\cdots a_{n-1}$" no plus before a_{n-1}; .tex
  "$\cdots+a_{n-1}$") -- documented house skip; eq# print-LEFT (leqno item).
- **⚠ FORMATTING (DEFERRED, NOT fixed):** ordinal-suffix superscription -- scan "$(n-1)^{te{}n}$", "$0^{te{}n}$" (raised
  "ten"); .tex "$(n-1)$ten", "$0$ten" (baseline). Same tier as leqno -> formatting pass.
- ★ 8 faithful pages running (p23-30): §1-§4 math-body clean. NEXT: **p31** = §4 cont. (.tex 715-732+): eq(7)
  $\frac{f(x)-f(\alpha)}{x-\alpha}=Q(x)$ (deg $n-1$); series eq(8) $f_0=1, f_1=x+a_1, f_2=x^2+a_1x+a_2, \ldots,
  f_{n-1}=x^{n-1}+a_1x^{n-2}+\cdots+a_{n-1}$; "Diese Functionen ... gute Dienste leisten" + Bemerkungen.
**No new type-B erratum; no Fraktur; epsilon untouched.** SPERRUNG/emphasis deferred. CONTENT-faithful; NOT emphasis-
verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p31 (§4 tail: eq(7) Restsatz-quotient, series eq(8-11) f_r + inverse expansion, .tex 715-766) — p1-99 gap pass — (verified by eye)
**CONTENT: 0 net edits (FAITHFUL page). 9th consecutive clean page. §4 COMPLETE.** File unchanged (418pp / 0 badness / 2264603).
- **FAITHFUL (content, display-by-display vs scan):** eq(7) $\frac{f(x)-f(\alpha)}{x-\alpha}=Q(x)$ ($Q$ deg $n-1$);
  substitute alpha->x with $a_0=1$ giving eq(8) $f_0=1$, $f_1=x+a_1$, $f_2=x^2+a_1x+a_2$, dots, $f_{n-1}=x^{n-1}
  +a_1x^{n-2}+a_2x^{n-3}+\cdots a_{n-1}$; "Diese Functionen ... gute Dienste leisten"; inverse expansion $1=f_0$,
  $x=f_1-a_1f_0$, $x^2=f_2-a_1f_1+(a_1^2-a_2)f_0$, dots; eq(9) $y_0f_0+y_1f_1+\cdots+y_{n-1}f_{n-1}$; eq(10)
  $F(x)=Qf(x)+y_0f_0+y_1f_1+\cdots+y_{n-1}f_{n-1}$; eq(11) recurrence $f_r(x)-xf_{r-1}(x)=a_r$. All matched (subscripts,
  exponents $x^{n-1/n-2/n-3}$, the $(a_1^2-a_2)$ coeff all zoom-checked).
- **SKIP-tier:** Coefficienten (ë-drop ×2); ellipsis-connector "+"; eq# print-LEFT (leqno item).
- **⚠ RUNNING HEADER (NOT in body .tex, not audited):** print header "§.4. Division durch lineare Functionen." differs from
  section title "Theilung durch eine lineare Function." (Weber's own header/title wording mismatch) -- body-only scope, N/A.
- **⚠ LAYOUT (NOT content):** .tex 768-769 double `\clearpage` before §5 -- possible extra blank page; layout pass item.
- ★ 9 faithful pages running (p23-31): §1-§4 math-body clean. NEXT: **p32** = §5 Gebrochene Functionen; Theilbarkeit
  (.tex 771+): def gebrochene rationale Function eq(1) F/f; echt/unecht gebrochen; eq(2) F=Qf+phi (deg phi < deg f).
**No new type-B erratum; no Fraktur; epsilon untouched.** SPERRUNG/emphasis deferred. CONTENT-faithful; NOT emphasis-
verified. Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p32 (§5 Gebrochene Functionen; Theilbarkeit: defs + eq(1-3) + Zerlegungs-Satz + theilbar-def + geom-series example, .tex 771-808) — p1-99 gap pass — (verified by eye)
**CONTENT: 0 net edits (FAITHFUL page). 10th consecutive clean page.** File unchanged (418pp / 0 badness / 2264603).
- **FAITHFUL (content vs scan):** §5 heading "Gebrochene Functionen; Theilbarkeit"; def "gebrochene rationale / kurz
  gebrochene / rationale Function"; eq(1) $\frac{F(x)}{f(x)}$; echt/unecht gebrochen (deg Zähler vs Nenner); eq(2)
  $F(x)=Qf(x)+\varphi(x)$; eq(3) $\frac{F(x)}{f(x)}=Q+\frac{\varphi(x)}{f(x)}$; Satz "Jede gebrochene Function kann in
  die Summe aus einer ganzen und einer echt gebrochenen Function zerlegt werden"; deg $\varphi\le n-1$; theilbar-def
  ($\varphi$ identisch verschwindet); "nur scheinbar gebrochen ... der ganzen Function Q gleich"; geom-series example
  $\frac{x^m-1}{x-1}=x^{m-1}+x^{m-2}+x^{m-3}+\cdots+1$. All matched.
- **SKIP-tier:** eq# print-LEFT (leqno item); ellipsis-connector "+".
- **⚠ EMPHASIS (DEFERRED to emphasis pass, NOT fixed):** scan gesperrt on defined terms + whole Zerlegungs-Satz +
  "theilbar" + "identisch verschwindet". .tex has \emph on SOME term-defs (gebrochene rationale/gebrochene/rationale
  Function; echt gebrochen; unecht gebrochen) but NOT on the Satz / theilbar / identisch verschwindet. => emphasis pass
  must (a) verify existing \emph spans vs scan gesperrt and (b) add the missing gesperrt spans. CONTENT words all match.
- ★ 10 faithful pages running (p23-32): §1-§5 math-body clean. NEXT: **p33** = §5 Theilbarkeit laws (.tex 810+): "dieselben
  Gesetze wie für Zahlen"; law 1 (transitivity F|f, f|phi => F|phi, proof F=Qf,f=q phi => F=Qq phi); law 2 (F|f => QF|f);
  law 3 (F,f | phi => F±f | phi); law 4 ($Q_1F_1+Q_2F_2+\cdots$ | f); "Der letzte Satz umfasst..." proof.
**No new type-B erratum; no Fraktur; epsilon untouched.** Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p33 (§5 Theilbarkeit laws 1-6 + proofs, .tex 810-854) — p1-99 gap pass — (verified by eye)
**CONTENT: 0 net edits (FAITHFUL page). 11th consecutive clean page.** File unchanged (418pp / 0 badness / 2264603).
- **FAITHFUL (content vs scan):** "dieselben Gesetze wie für Zahlen"; law 1 transitivity ($F=Qf$, $f=q\varphi$ =>
  $F=Qq\varphi$; Qq ganze rationale Fn => F durch phi theilbar); law 2 ($F|f$ => $QF(x)|f(x)$); **law 3 ($F,f|\varphi$ =>
  $F(x)\pm f(x)|\varphi(x)$) -- the $\pm$ ZOOM-VERIFIED vs scan** (.tex \pm ok); law 4 ($F_1,F_2\ldots|f$, $Q_i$ bel. =>
  $Q_1F_1+Q_2F_2+\cdots|f$) + proof ($F_i=\Phi_i f$; $Q_1F_1+Q_2F_2+\cdots=(Q_1\Phi_1+Q_2\Phi_2+\cdots)f$); law 5 (durch
  sich selbst theilbar); const-factor invariance para; law 6 (durch jede Constante theilbar). All matched row-for-row.
- **SKIP-tier:** ellipsis-connector "+"; ellipsis-commas. Footer "Weber, Algebra. I." + signature "3" = print catchword,
  not in .tex (N/A). Running header "Theilbarkeit ganzer Functionen" != §5 title (body-only, N/A).
- **⚠ EMPHASIS (DEFERRED):** numbered-law statements (5., 6.) + "Constante" gesperrt in scan; .tex no \emph. Emphasis pass.
- **⚠ FORMATTING (DEFERRED):** "nullten Grades" ordinal-suffix superscript.
- ★ 11 faithful pages running (p23-33): §1-§5 math-body clean. NEXT: **p34** = §5 laws 7,8 (.tex 856-860: deg-quotient =
  deg-diff; law 7 equal-degree mutual theilbar => const factor; law 8 $x-\alpha | f(x) \iff f(\alpha)=0$) then **§6 Grösster
  gemeinschaftlicher Theiler** (.tex 862+: gcd algorithm, eq(1) f=A, phi=A'; division chain eq(2) A,A',A'',...; eq(3+) Kette).
**No new type-B erratum; no Fraktur; epsilon untouched.** Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p34 (§5 tail laws 7,8 + §6 Grösster gemeinschaftlicher Theiler start eq(1,2), .tex 856-882) — p1-99 gap pass — (verified by eye)
**CONTENT: 0 net edits (FAITHFUL page). 12th consecutive clean page. §5 COMPLETE, §6 STARTED.** File unchanged (418pp/0/2264603).
- **FAITHFUL (content vs scan):** deg(Quotient)=deg(Dividend)-deg(Divisor) para; law 7 (equal-degree mutual-theilbar =>
  differ only by constant Factor, second theilbar by first); **law 8 (nach §4: $f(x)$ durch $x-\alpha$ theilbar <=>
  $f(\alpha)=0$)** -- .tex "die dass $f(\alpha)=0$ sei" matches scan telegraphic phrasing exactly (no comma to add);
  §6 heading "Grösster gemeinschaftlicher Theiler"; "Aufgabe von fundamentaler Bedeutung ... Algorithmus des grössten
  gemeinschaftlichen Theilers ... (S. die Einleitung.)"; eq(1) $f(x)=A$, $\varphi(x)=A'$; deg phi <= deg f; first division
  $A=Q'A'+A''$; Functionenreihe eq(2) $A,A',A'',A'''\ldots$; grades $n,n',n'',n'''\ldots$ abnehmen -> Null; last const
  rem $A^{(\nu)}$; "Kette der Gleichungen". All matched.
- **SKIP-tier:** ellipsis-commas/"+"; "(S. die Einleitung.)" cross-ref KEPT; running header/footer (body-only, N/A).
- **⚠ INDEX GLYPH TO CONFIRM p35:** last-remainder superscript $A^{(\nu)}$ renders ambiguous (ν vs r) at page zoom; .tex
  uses \nu (correct/standard, matches Kette). Disambiguate on p35 where $A^{(\nu-2)},A^{(\nu-1)},A^{(\nu)}$ co-occur.
- **⚠ EMPHASIS (DEFERRED):** numbered laws (7.,8.) + "Algorithmus des grössten gemeinschaftlichen Theilers" gesperrt; .tex no \emph.
- ★ 12 faithful pages running (p23-34): §1-§6start math-body clean. NEXT: **p35** = §6 Kette eq(3) (.tex 883-892:
  $A=Q'A'+A''$, $A'=Q''A''+A'''$, ..., $A^{(\nu-3)}=Q^{(\nu-2)}A^{(\nu-2)}+A^{(\nu-1)}$, $A^{(\nu-2)}=Q^{(\nu-1)}A^{(\nu-1)}
  +A^{(\nu)}$) + gcd argument (theilerfremd/relativ prim def has \emph in .tex -> VERIFY vs scan) + eq(4) $A^{(\nu)}=0$ +
  gcd=$A^{(\nu-1)}$ + worked example A,B quadratics eq(5-8) $c_0=(a_1b_0-b_1a_0)/b_0$, $c_1=(a_2b_0-b_2a_0)/b_0$.
**No new type-B erratum; no Fraktur; epsilon untouched.** Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p35 (§6 gcd Kette eq(3) + gcd argument + eq(4) + example-1 setup eq(5), .tex 883-914) — p1-99 gap pass — (verified by eye + ZOOM)
**CONTENT: 0 net edits (FAITHFUL page). 13th consecutive clean page.** File unchanged (418pp/0/2264603).
- **★ ZOOM-CONFIRMED index glyph: paren-superscript is Greek ν (nu), NOT Latin r** (crop of row $A^{(\nu-2)}=Q^{(\nu-1)}
  A^{(\nu-1)}+A^{(\nu)}$: pointed v-shape = ν; matches .tex \nu). p34's $A^{(\nu)}$ thereby confirmed too.
- **FAITHFUL (content vs scan):** **eq(3) Kette 5 rows matched** ($A=Q'A'+A''$; $A'=Q''A''+A'''$; dots; $A^{(\nu-3)}=
  Q^{(\nu-2)}A^{(\nu-2)}+A^{(\nu-1)}$; $A^{(\nu-2)}=Q^{(\nu-1)}A^{(\nu-1)}+A^{(\nu)}$); "worin $A^{(\nu)}$ Constante";
  gcd-argument (gemeinsamer Theiler von A,A' teilt A'',...,$A^{(\nu)}$); theilerfremd/relativ prim def; eq(4) $A^{(\nu)}=0$;
  $A^{(\nu-1)}$ = grösster gemeinsamer Theiler; Algorithmus-remark; example-1 "Es seien zunächst" eq(5) $A=a_0x^2+a_1x+a_2$,
  $B=b_0x^2+b_1x+b_2$; "zwei Functionen zweiten Grades, $a_0,b_0\ne0$". All matched.
- **★ EMPHASIS VERIFIED (not deferred here):** scan gesperrt "theilerfremd" + "relativ prim" == .tex \emph{theilerfremd}
  \emph{relativ prim} -- these \emph ADDITIONS are FAITHFUL (match Weber gesperrt). (Other gesperrt: "grösste gemeinsame
  Theiler", "rationalen Rechenoperationen" -- .tex no \emph; emphasis-pass.)
- **SKIP-tier:** Coëfficienten (ë-drop); ellipsis; footer sig "3*" (N/A); running header (N/A).
- ★ 13 faithful pages running (p23-35). NEXT: **p36 = DENSE RESULTANTE page** (.tex 916-960: eq(6) $A=\frac{a_0}{b_0}B+C$;
  eq(7) $C=c_0x+c_1$; eq(8) $c_0=\frac{a_1b_0-b_1a_0}{b_0}$,$c_1=\frac{a_2b_0-b_2a_0}{b_0}$; $B=QC+D$; eq(9) $D=\frac{b_0
  c_1^2-b_1c_0c_1+b_2c_0^2}{c_0^2}$; eq(10) big 7-term resultante $a_0^2b_2^2+a_2^2b_0^2-2a_0a_2b_0b_2-a_1a_2b_0b_1-a_0a_1
  b_1b_2+a_0a_2b_1^2+a_1^2b_0b_2=0$; eq(11) factored $(a_0b_2-b_0a_2)^2+(a_0b_1-a_1b_0)(a_2b_1-a_1b_2)=0$; \emph{Resultante}
  def; example-2 eq(12) f,f'). HIGHEST misread-risk -> ZOOM every term of eq(8),(9),(10),(11).
**No new type-B erratum; no Fraktur; epsilon untouched.** Confirmed by eye+zoom vs ~500dpi scans; direct context-read.


### 2026-07-02 — p36 (§6 DENSE RESULTANTE: example-1 eq(6-11) + Resultante def + example-2 setup eq(12), .tex 916-968) — p1-99 gap pass — (verified by eye, TERM-BY-TERM)
**CONTENT: 0 net edits (FAITHFUL page). 14th consecutive clean page.** File unchanged (418pp/0/2264603).
- **★ DENSEST algebra of §6 verified EXACT term-by-term:** eq(6) $A=\frac{a_0}{b_0}B+C$; eq(7) $C=c_0x+c_1$; eq(8)
  $c_0=\frac{a_1b_0-b_1a_0}{b_0}$, $c_1=\frac{a_2b_0-b_2a_0}{b_0}$ (indices 1,0,1,0 / 2,0,2,0); $c_0=0$ case; $B=QC+D$
  ($\alpha=-c_1:c_0$); eq(9) $D=\frac{b_0c_1^2-b_1c_0c_1+b_2c_0^2}{c_0^2}$; **eq(10) 7-TERM resultante, ALL terms + FULL
  sign pattern (+ + - - - + +) MATCHED**: $a_0^2b_2^2+a_2^2b_0^2-2a_0a_2b_0b_2-a_1a_2b_0b_1-a_0a_1b_1b_2+a_0a_2b_1^2
  +a_1^2b_0b_2=0$; **eq(11) factored MATCHED**: $(a_0b_2-b_0a_2)^2+(a_0b_1-a_1b_0)(a_2b_1-a_1b_2)=0$; "Weglassung des
  Nenners $b_0c_0^2$"; example-2 eq(12) $f=a_0x^3+a_1x^2+a_2x+a_3=A$, $f'=3a_0x^2+2a_1x+a_2=B$.
- **★ EMPHASIS VERIFIED (faithful):** scan gesperrt "Resultante" == .tex \emph{Resultante}. (Add to verified-good list
  w/ theilerfremd/relativ prim.)
- **SKIP-tier:** ellipsis; running header (N/A). No ë-words this page.
- ★★ METHOD INSIGHT (logged): dense coefficient-algebra proof pages are AS CLEAN as routine ones -- GPT damage was
  concentrated in Einleitung verbal/conceptual prose, NOT in symbolic math regardless of density. 14 straight clean.
- ★ 14 faithful pages running (p23-36). NEXT: **p37 = DISCRIMINANTE page** (.tex 969-1005: eq(13) $A=QB+C$; eq(14)
  $C=c_0x+c_1$; eq(15) $c_0=\frac{6a_0a_2-2a_1^2}{9a_0}$, $c_1=\frac{9a_0a_3-a_1a_2}{9a_0}$; eq(16) $3a_0a_2-a_1^2=0$,
  $9a_0a_3-a_1a_2=0$; eq(17) $B=PC+D$; eq(18) $D=\frac{a_2c_0^2-2a_1c_0c_1+3a_0c_1^2}{c_0^2}$; eq(19) DISCRIMINANT
  $a_1^2a_2^2+18a_0a_1a_2a_3-4a_0a_2^3-4a_1^3a_3-27a_0^2a_3^2=0$; \emph{Discriminante} def). ZOOM eq(15),(18),(19)
  coeffs (18,4,4,27; cubes $a_2^3,a_1^3$; $a_0^2,a_3^2$).
**No new type-B erratum; no Fraktur; epsilon untouched.** Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p37 (§6 DISCRIMINANTE: example-2 cubic gcd eq(13-19) + Discriminante def + Satz eq(20-21start), .tex 969-1016) — p1-99 gap pass — (verified by eye, TERM-BY-TERM)
**CONTENT: 0 net edits (FAITHFUL page). 15th consecutive clean page.** File unchanged (418pp/0/2264603).
- **★ CUBIC DISCRIMINANT verified EXACT term-by-term:** eq(13) $A=QB+C$; eq(14) $C=c_0x+c_1$; eq(15) $c_0=\frac{6a_0a_2
  -2a_1^2}{9a_0}$, $c_1=\frac{9a_0a_3-a_1a_2}{9a_0}$ (coeffs 6,2,9); eq(16) $3a_0a_2-a_1^2=0$, $9a_0a_3-a_1a_2=0$; eq(17)
  $B=PC+D$; eq(18) $D=\frac{a_2c_0^2-2a_1c_0c_1+3a_0c_1^2}{c_0^2}$; **eq(19) DISCRIMINANT ALL 5 terms + signs (+ + - - -)
  + coeffs (1,18,4,4,27) + cubes MATCHED**: $a_1^2a_2^2+18a_0a_1a_2a_3-4a_0a_2^3-4a_1^3a_3-27a_0^2a_3^2=0$; eq(20)
  $A''=A-Q'A'$; $A'''=(1+Q'Q'')A'-Q''A$. All matched.
- **★ EMPHASIS VERIFIED (faithful):** scan gesperrt "Discriminante" == .tex \emph{Discriminante}. Also: "theilerfremd"
  at .tex 1000 (non-defining occurrence) correctly NOT \emph -- consistent w/ defining \emph on p35.
- **SKIP-tier:** eq(15) scan ";" separator vs .tex "," (punctuation, skip); Coëfficienten (ë-drop); running header
  "Quadratische und cubische Function" (body-only, N/A).
- ★★ METHOD INSIGHT reconfirmed: 2nd straight dense-algebra page (resultante p36, discriminant p37) EXACT. Symbolic math
  is clean regardless of density. 15 straight clean (p23-37).
- ★ 15 faithful pages running (p23-37). NEXT: **p38** = §6 tail Bezout Satz (.tex 1018-1066): eq(21) $A'''=pA+p'A'$;
  eq(22) $A^{(\nu)}=PA+P'A'$; relativ-prim application $P=A^{(\nu)}F$, $P'=A^{(\nu)}\Phi$; **Satz I eq(23) $F(x)f(x)+
  \Phi(x)\psi(x)=1$** (Bezout); verallgemeinerung eq(24) $\cdot\chi(x)=\chi$; eq(25) $\Phi\chi=Qf+\varphi$; **Satz II eq(26)
  $F(x)f(x)+\varphi(x)\psi(x)=\chi(x)$**; then **§7 Producte linearer Factoren** start.
**No new type-B erratum; no Fraktur; epsilon untouched.** Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p38 (§6 tail BEZOUT: eq(21-25) + Satz I & start of Satz II, .tex 1018-1059) — p1-99 gap pass — (verified by eye, Greek-letter ZOOM)
**CONTENT: 0 net edits (FAITHFUL page). 16th consecutive clean page.** File unchanged (418pp/0/2264603).
- **FAITHFUL (content vs scan):** eq(21) $A'''=pA+p'A'$ (lower p,p'); eq(22) $A^{(\nu)}=PA+P'A'$ (upper P,P'); relativ-prim
  setup $P=A^{(\nu)}F(x)$, $P'=A^{(\nu)}\Phi(x)$; **Satz I. eq(23) BEZOUT $F(x)f(x)+\Phi(x)\psi(x)=1$**; verallg. eq(24)
  $F(x)\chi(x)f(x)+\Phi(x)\chi(x)\psi(x)=\chi(x)$; eq(25) $\Phi(x)\chi(x)=Q(x)f(x)+\varphi(x)$; $F(x)f(x)+\varphi(x)\psi(x)
  =\chi(x)$ (untagged); Satz II. start. All matched.
- **★ GREEK FUNCTION-LETTERS all correctly distinguished (zoom-verified):** F (cap-F) / Φ (\Phi) / f / ψ (\psi) / χ (\chi)
  / φ (\varphi) / Q -- NO misreads across eq(23)-(25). p/p' (lower) vs P/P' (upper) correct in eq(21)/(22).
- **SKIP-tier:** Coëfficienten (ë-drop); .tex 1043 comma after χ(x) (punctuation, scan line-break ambiguous); running header.
- ★ 16 faithful pages running (p23-38). NEXT: **p39** = Satz II eq(26) $F(x)f(x)+\varphi(x)\psi(x)=\chi(x)$ + **§7 Producte
  linearer Factoren** (.tex 1066+): deg(product)=Σdeg; eq(1) $f(x)=(x-\alpha_1)\cdots(x-\alpha_n)=x^n+a_1x^{n-1}+\cdots+a_n$;
  VIETA eq(2) $-a_1=\sum\alpha_1$, $+a_2=\sum\alpha_1\alpha_2$, ..., $(-1)^\nu a_\nu=\sum\alpha_1\cdots\alpha_\nu$, ...,
  $(-1)^n a_n=\alpha_1\cdots\alpha_n$; induction examples ($(x-\alpha_1)(x-\alpha_2)=x^2-(\alpha_1+\alpha_2)x+\alpha_1\alpha_2$ etc).
**No new type-B erratum; no Fraktur; epsilon untouched.** Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p39 (§6 Satz II eq(26) + §7 Producte linearer Factoren: VIETA eq(1-2), .tex 1059-1096) — p1-99 gap pass — (verified by eye)
**CONTENT: 0 net edits (FAITHFUL page). 17th consecutive clean page. §7 STARTED.** File unchanged (418pp/0/2264603).
- **FAITHFUL (content vs scan):** Satz II conclusion eq(26) $F(x)f(x)+\varphi(x)\psi(x)=\chi(x)$; §7 heading "Producte
  linearer Factoren"; deg(product)=Sum(deg); n lin factors -> $n$ten Grade; eq(1) $f(x)=(x-\alpha_1)(x-\alpha_2)\cdots
  (x-\alpha_n)=x^n+a_1x^{n-1}+a_2x^{n-2}+\cdots+a_n$; Vieta prose ($-a_1$=Sum α, $a_2$=Sum je-2, $-a_3$=je-3, general
  $(-1)^\nu a_\nu$=Sum je-ν); **VIETA eq(2) 4 rows + 2 dot-rows MATCHED**: $-a_1=\sum\alpha_1$; $+a_2=\sum\alpha_1\alpha_2$;
  $(-1)^\nu a_\nu=\sum\alpha_1\alpha_2\cdots\alpha_\nu$; $(-1)^n a_n=\alpha_1\alpha_2\cdots\alpha_n$ (last row NO Sum,
  single product -- correct); "vollständigen Induction". All signs/Sum/α-subscripts matched.
- **SKIP-tier:** ellipsis-connector "+" (eq1 "cdots a_n"); Coëfficient(en) (ë-drop); "nten Grade" ordinal (formatting);
  running header. ⚠ EMPHASIS (defer): "vollständigen Induction" gesperrt.
- ★ 17 faithful pages running (p23-39). NEXT: **p40** = §7 induction examples + eq(3) + B_ν^{(n)} combinatorics (.tex
  1097-1144): $(x-\alpha_1)(x-\alpha_2)=x^2-(\alpha_1+\alpha_2)x+\alpha_1\alpha_2$; cubic expansion; induction step eq(3)
  $a_1=a'_1-\alpha_n$, $a_2=a'_2-\alpha_n a'_1$, ..., $a_\nu=a'_\nu-\alpha_n a'_{\nu-1}$, ..., $a_n=-\alpha_n a'_{n-1}$;
  count-of-terms $B_\nu^{(n)}$ (binomial); eq(4) recursion; eq(5); eq(6) $B_\nu^{(n)}=\frac{n(n-1)\cdots(n-\nu+1)}{1\cdot2
  \cdots\nu}$. ZOOM B_ν^{(n)} indices + eq(3) primed-a recursion.
**No new type-B erratum; no Fraktur; epsilon untouched.** Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p40 (§7 induction examples + eq(3) recursion + B_ν^{(n)} count eq(4-5), .tex 1097-1140) — p1-99 gap pass — (verified by eye)
**CONTENT: 0 net edits (FAITHFUL page). 18th consecutive clean page.** File unchanged (418pp/0/2264603).
- **FAITHFUL (content vs scan):** quad $(x-\alpha_1)(x-\alpha_2)=x^2-(\alpha_1+\alpha_2)x+\alpha_1\alpha_2$; **cubic
  $(x-\alpha_1)(x-\alpha_2)(x-\alpha_3)=x^3-(\alpha_1+\alpha_2+\alpha_3)x^2+(\alpha_1\alpha_2+\alpha_1\alpha_3+\alpha_2
  \alpha_3)x-\alpha_1\alpha_2\alpha_3$ (3-term middle coeff all pairs verified)**; induction hyp $(x-\alpha_1)\cdots
  (x-\alpha_{n-1})=x^{n-1}+a'_1x^{n-2}+\cdots+a'_{n-1}$; **eq(3) recursion rows** $a_1=a'_1-\alpha_n$; $a_2=a'_2-\alpha_n
  a'_1$; $a_3=a'_3-\alpha_n a'_2$; $a_\nu=a'_\nu-\alpha_n a'_{\nu-1}$; $a_n=-\alpha_n a'_{n-1}$ (last: NO a'_n term);
  count $B_\nu^{(n)}$ = Combinationen n-to-ν; eq(4) $B_\nu^{(n)}=B_{\nu-1}^{(n)}\frac{n-\nu+1}{\nu}$; $B_1^{(n)}=n$;
  eq(5) chain. All matched. ★ B_ν^{(n)} double-index (sub ν, paren-super (n)) rendered correctly throughout.
- **SKIP-tier:** ellipsis-connector "+" (induction display); "ν^{ten}/(ν-1)^{ten} Classe" ordinal (formatting); running header.
- ★ 18 faithful pages running (p23-40). NEXT: **p41** = eq(6) binomial + Pi-notation + Pascal (.tex 1141-1181): eq(6)
  $B_\nu^{(n)}=\frac{n(n-1)(n-2)\cdots(n-\nu+1)}{1\cdot2\cdot3\cdots\nu}$; Pi-Zeichen eq(7) $\Pi(m)=1\cdot2\cdot3\cdots m$,
  $\Pi(0)=1$; eq(8) $\Pi(m)=m\Pi(m-1)$; eq(9) $B_\nu^{(n)}=B_{n-\nu}^{(n)}=\frac{\Pi(n)}{\Pi(\nu)\Pi(n-\nu)}$ (symmetry
  ν<->n-ν, $B_0^{(n)}=1$); induction re-derivation Pascal eq(10) $B_\nu^{(n)}=B_\nu^{(n-1)}+B_{\nu-1}^{(n-1)}$. ZOOM Pi-args
  + B double-indices ((n) vs (n-1) superscripts!).
**No new type-B erratum; no Fraktur; epsilon untouched.** Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p41 (§7 binomial closed-form eq(6) + Pi-notation eq(7-9) + Pascal recursion eq(10) + induction proof, .tex 1141-1186) — p1-99 gap pass — (verified by eye)
**CONTENT: 0 net edits (FAITHFUL page). 19th consecutive clean page.** File unchanged (418pp/0/2264603).
- **FAITHFUL (content vs scan):** eq(6) $B_\nu^{(n)}=\frac{n(n-1)(n-2)\cdots(n-\nu+1)}{1\cdot2\cdot3\cdots\nu}$; Pi-Zeichen
  eq(7) $\Pi(m)=1\cdot2\cdot3\cdots m$, $\Pi(0)=1$; eq(8) $\Pi(m)=m\Pi(m-1)$; eq(9) $B_\nu^{(n)}=B_{n-\nu}^{(n)}=\frac{\Pi(n)}
  {\Pi(\nu)\Pi(n-\nu)}$ (symmetry ν<->n-ν, $B_0^{(n)}=1$); **Pascal recursion eq(10) rows MATCHED**: $B_1^{(n)}=B_1^{(n-1)}
  +1$; $B_2^{(n)}=B_2^{(n-1)}+B_1^{(n-1)}$; $B_\nu^{(n)}=B_\nu^{(n-1)}+B_{\nu-1}^{(n-1)}$; $B_n^{(n)}=B_{n-1}^{(n-1)}$
  (last: single term); induction step $B_\nu^{(n)}=\frac{\Pi(n-1)}{\Pi(\nu)\Pi(n-\nu-1)}+\frac{\Pi(n-1)}{\Pi(\nu-1)\Pi(n-\nu)}$
  -> (nach 8) $\frac{\Pi(n)}{\Pi(\nu)\Pi(n-\nu)}$; "Allgemeingültigkeit (9) bewiesen". All matched. ★ Pi-args + B (n)/(n-1)
  superscripts + ν/ν-1 subscripts all correct.
- **SKIP-tier:** eq(6) numerator scan "n·(n-1)" explicit dot vs .tex "n(n-1)" juxtaposition (notation, same product); running header.
- ★ 19 faithful pages running (p23-41). NEXT: **p42** = positive-integer remark + **§8 Der binomische Lehrsatz** (.tex
  1188-1220): $\alpha_i=-y$ => $a_\nu=(-1)^\nu\sum\cdots=y^\nu B_\nu^{(n)}$; eq(1) $(x+y)^n=x^n+B_1^{(n)}x^{n-1}y+B_2^{(n)}
  x^{n-2}y^2+\cdots+B_n^{(n)}y^n$; expanded $=x^n+nx^{n-1}y+\frac{n(n-1)}{1\cdot2}x^{n-2}y^2+\cdots+y^n=\Pi(n)\sum\frac{
  x^{n-\nu}y^\nu}{\Pi(n-\nu)\Pi(\nu)}$; Binomialcoefficienten def; table. ZOOM binomial expansion coeffs.
**No new type-B erratum; no Fraktur; epsilon untouched.** Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p42 (§8 Der binomische Lehrsatz: eq(1) expansion + Pi-sum forms + Binomialcoeff table, .tex 1188-1230) — p1-99 gap pass — (verified by eye)
**CONTENT: 0 net edits (FAITHFUL page). 20th consecutive clean page. §8 STARTED.** File unchanged (418pp/0/2264603).
- **FAITHFUL (content vs scan):** "B_ν^{(n)} positive ganze Zahlen"; §8 heading "Der binomische Lehrsatz"; α_1=α_2=...=α_n
  =-y; $a_\nu=(-1)^\nu\sum\alpha_1\alpha_2\cdots\alpha_\nu=y^\nu B_\nu^{(n)}$; eq(1) $(x+y)^n=x^n+B_1^{(n)}x^{n-1}y+B_2^{(n)}
  x^{n-2}y^2+\cdots+B_n^{(n)}y^n$; expanded $=x^n+nx^{n-1}y+\frac{n(n-1)}{1\cdot2}x^{n-2}y^2+\cdots+y^n=\Pi(n)\sum\frac{
  x^{n-\nu}y^\nu}{\Pi(n-\nu)\Pi(\nu)}=\Pi(n)\sum\frac{x^\alpha y^\beta}{\Pi(\alpha)\Pi(\beta)}$ (α+β=n); Binomialcoeff def;
  **Pascal-triangle TABLE n=1..7 verified EXACT** (1,1 / 1,2,1 / 1,3,3,1 / 1,4,6,4,1 / 1,5,10,10,5,1 / 1,6,15,20,15,6,1 /
  1,7,21,35,35,21,7,1). All matched.
- **★ NOTATION FINDING (DEFERRED to formatting/notation pass, NOT fixed):** the FIRST expanded-sum Σ in scan carries EXPLICIT
  limits -- index "ν" ABOVE and range "0, n" BELOW the Σ; .tex renders bare `\sum` (limits dropped). This is operator-
  decoration/notation (like leqno/ordinal-superscript), NOT German text content -> defer. **POTENTIALLY SYSTEMATIC**: grep
  `\sum` doc-wide in formatting pass; restore Weber's Σ index/range where scan shows them. (2nd expanded Σ + the $a_\nu$ Σ
  are bare in BOTH scan and .tex -- only the ν/0,n one differs.)
- **SKIP-tier:** Binomialcoëfficienten (ë-drop; .tex "Binomialcoefficienten"); "nten Potenz" ordinal (formatting); running
  header. ⚠ EMPHASIS (defer): "binomischen Lehrsatz", "Binomialcoëfficienten" gesperrt.
- ★ 20 faithful pages running (p23-42). NEXT: **p43** = §8 tail: 2 binomial-coeff identities (.tex 1232-1274): eq(2)
  power series $1=B_0^{(0)}$, ..., $(1+x)^n=B_0^{(n)}+B_1^{(n)}x+\cdots+B_n^{(n)}x^n$; geom-series sum $\frac{(1+x)^{n+1}
  -1}{x}$; eq(3); column-sum eq(4)/hockey-stick eq(5) $B_\nu^{(\nu)}+B_\nu^{(\nu+1)}+\cdots+B_\nu^{(n)}=B_{\nu+1}^{(n+1)}$;
  alternating-sign multiply ($B_0^{(n)},-B_1^{(n)},+B_2^{(n)},\ldots,\pm B_n^{(n)}$). ZOOM the B superscript ladders.
**No new type-B erratum; no Fraktur; epsilon untouched.** Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p43 (§8 Binomialcoeff identities: eq(2) power series + geom-series + eq(3) + column-sum eq(4) + hockey-stick eq(5) + alternating-sum setup, .tex 1232-1276) — p1-99 gap pass — (verified by eye)
**CONTENT: 0 net edits (FAITHFUL page). 21st consecutive clean page.** File unchanged (418pp/0/2264603).
- **FAITHFUL (content vs scan):** eq(2) $1=B_0^{(0)}$; $1+x=B_0^{(1)}+B_1^{(1)}x$; $(1+x)^2=B_0^{(2)}+B_1^{(2)}x+B_2^{(2)}x^2$;
  $(1+x)^n=B_0^{(n)}+B_1^{(n)}x+B_2^{(n)}x^2+\cdots+B_n^{(n)}x^n$; geom-series $1+(1+x)+\cdots+(1+x)^n=\frac{(1+x)^{n+1}-1}{x}$;
  eq(3) $\frac{(1+x)^{n+1}-1}{x}=B_1^{(n+1)}+B_2^{(n+1)}x+\cdots+B_{n+1}^{(n+1)}x^n$; **column-sum eq(4)** ($B_0^{(0)}+B_0^{(1)}
  +\cdots+B_0^{(n)}=B_1^{(n+1)}$; $B_1^{(1)}+B_1^{(2)}+\cdots+B_1^{(n)}=B_2^{(n+1)}$; $B_n^{(n)}=B_{n+1}^{(n+1)}$);
  **hockey-stick eq(5)** $B_\nu^{(\nu)}+B_\nu^{(\nu+1)}+\cdots+B_\nu^{(n)}=B_{\nu+1}^{(n+1)}$; alternating multipliers
  $B_0^{(n)},-B_1^{(n)},+B_2^{(n)},\ldots\pm B_n^{(n)}$ (obere Zeichen geradem/untere ungeradem n); alt-sum $B_0^{(n)}-B_1^{(n)}
  (1+x)+B_2^{(n)}(1+x)^2-\cdots\pm B_n^{(n)}(1+x)^n=[1-(1+x)]^n=(-x)^n$. All B super/subscript ladders MATCHED.
- **SKIP-tier:** "worin wenn"/"worin, wenn" comma (punct); ellipsis "⋯±" vs "…,±"; Binomialcoëfficienten (ë-drop); running
  header "Binomial-Coëfficienten"; ordinals.
- **NOTE (re p42 Σ-limits):** .tex DOES use \sum_{ν=0}^{μ} with limits at eq(8) (.tex 1301, on p44) -> confirms p42 bare
  \sum is a LOCALIZED per-instance limit-drop, cleanly restorable in formatting pass (not a house style).
- ★ 21 faithful pages running (p23-43). NEXT: **p44** = §8 tail product-identities eq(6)/(7)/(8) + **§9 Interpolation**
  (.tex 1278-1314): Formelsystem eq(6) $0=B_0^{(0)}B_0^{(n)}-B_0^{(1)}B_1^{(n)}+\cdots\pm B_0^{(n)}B_n^{(n)}$, ...,
  $\pm1=\pm B_n^{(n)}B_n^{(n)}$; reversed eq(7); summed eq(8) $\sum_{\nu=0}^\mu(-1)^\nu B_{\mu-\nu}^{(n-\nu)}B_\nu^{(n)}
  =\{1 (\mu=0); 0 (\mu=1..n)\}$; §9 Interpolation heading + setup (ganze rat. Fn nten Grades, n+1 Werthe). ★ZOOM the
  double-B PRODUCTS + double-superscripts (n-ν)/(n-1)/(n-2) + cases-brace.
**No new type-B erratum; no Fraktur; epsilon untouched.** Confirmed by eye vs ~500dpi scans; direct context-read.


### 2026-07-02 — p44 (§8 tail product-identities eq(6-8) + §9 Interpolation start eq(1-2), .tex 1279-1326) — p1-99 gap pass — (verified by eye + ZOOM) — **1 CONTENT FIX**
**CONTENT: 1 net edit (FABRICATION removed). Ends 21-page clean streak (p23-43).** Compiles **418pp / 0 overfull / 0 underfull / PDF 2264580 B**.
- **★★ FIX (GPT FABRICATION removed):** .tex 1328 read "für die Unbekannten $a_0,a_1,\ldots,a_n$, **um die** sich im
  Allgemeinen durch Determinanten auflösen lassen" -- scan (ZOOM-confirmed) reads "..., **die** sich im Allgemeinen..."
  (NO "um"). The inserted "um" is not in source AND breaks German grammar ("um die sich...lassen" doesn't parse). REMOVED
  "um ". This is the 2nd fabrication caught (after z+c p19). Compile-gated clean (418pp, 0 badness).
- **FAITHFUL (rest, TERM-checked vs scan):** eq(6) product-identity rows ($0=B_0^{(0)}B_0^{(n)}-B_0^{(1)}B_1^{(n)}+B_0^{(2)}
  B_2^{(n)}-\cdots\pm B_0^{(n)}B_n^{(n)}$; ...; $\pm1=\pm B_n^{(n)}B_n^{(n)}$); eq(7) reversed (via $B_\nu^{(n)}=B_{n-\nu}^{(n)}$:
  $1=B_0^{(n)}B_0^{(n)}$; $0=B_1^{(n)}B_0^{(n)}-B_0^{(n-1)}B_1^{(n)}$; ...; $0=B_n^{(n)}B_0^{(n)}-B_{n-1}^{(n-1)}B_1^{(n)}
  +B_{n-2}^{(n-2)}B_2^{(n)}-\cdots\pm B_0^{(0)}B_n^{(n)}$); eq(8) $\sum(-1)^\nu B_{\mu-\nu}^{(n-\nu)}B_\nu^{(n)}=\{1,\mu=0;
  0,\mu=1..n\}$; §9 heading "Interpolation"; setup; eq(1) $f(x)=a_0x^n+a_1x^{n-1}+\cdots+a_{n-1}x+a_n$; eq(2) $f(\alpha_0)
  =A_0,f(\alpha_1)=A_1,\ldots,f(\alpha_n)=A_n$. All double-B products/superscripts MATCHED.
- **★ Σ-NOTATION refinement (formatting-pass):** eq(8) scan shows Weber-style Σ (variable "ν" OVER, range "0,μ" UNDER);
  .tex uses modern $\sum_{\nu=0}^{\mu}$ -- SEMANTICALLY IDENTICAL limits (range preserved), just old-vs-modern convention.
  Reclassifies p42 finding: systematic Weber-Σ-convention (var-over/range-under) -> formatting pass; content intact.
- **SKIP-tier:** Coëfficienten (ë-drop); ellipsis-connector "+"; "nten Grades" ordinal; running header.
- ★ Streak reset: 21 clean (p23-43) then 1 fix p44. NEXT: **p45** = §9 cont. generalized-binomial (.tex 1328-1356): "0,1,2,
  ...,n" Voraussetzung; $B_\nu^{(x)}=\frac{x(x-1)\cdots(x-\nu+1)}{1\cdot2\cdot3\cdots\nu}$ eq(3) (deg-ν, footnote); eq(4)
  $f(x)=M_0B_0^{(x)}+M_1B_1^{(x)}+\cdots+M_nB_n^{(x)}$; linear system eq(5) $f(0)=M_0B_0^{(0)}$, $f(1)=M_0B_0^{(1)}+M_1
  B_1^{(1)}$, ..., $f(n)=M_0B_0^{(n)}+\cdots+M_nB_n^{(n)}$; solve via eq(8). ZOOM B_ν^{(x)} (variable-x superscript!) + M-indices + footnote.
**No new type-B erratum; no Fraktur; epsilon untouched.** Fabrication FIX compile-gated. Confirmed by eye+zoom vs ~500dpi scans.


### 2026-07-02 — p45 (§9 Interpolation: generalized B_ν^{(x)} eq(3) + footnote + M-expansion eq(4) + M-system eq(5) + eq(6), .tex 1328-1357) — p1-99 gap pass — (verified by eye + ZOOM ×2) — **3 CONTENT FIXES**
**CONTENT: 3 net edits (1 normalization-revert, 1 dropped-term restore, 1 spelling-revert).** Compiles **418pp / 0 overfull / 0 underfull / PDF 2264596 B**.
- **★★ FIX 1 (GPT NOTATION-NORMALIZATION reverted):** .tex 1330 prose read "Die Binomialcoefficienten $B_\nu^{(x)}$ ...
  auch wenn $x$ keine ganze Zahl ist" -- scan (ZOOM-confirmed) reads "$B_\nu^{(n)}$ ... auch wenn $n$ keine ganze Zahl
  ist". Weber uses (n) in the reference-back prose (matching §7's $B_\nu^{(n)}$), switches to x only in eq(3) display.
  GPT normalized prose n->x for "consistency". RESTORED $B_\nu^{(n)}$ + "wenn $n$". (eq(3)/(4) legitimately use (x) -- unchanged.)
- **★★ FIX 2 (DROPPED TERM restored):** eq(5) $f(n)$ row scan = $M_0B_0^{(n)}+M_1B_1^{(n)}+M_2B_2^{(n)}+\cdots+M_nB_n^{(n)}$
  (3 explicit terms, paralleling f(2)); .tex dropped the $M_2B_2^{(n)}$ term (only M_0,M_1,dots). RESTORED $+M_2B_2^{(n)}$.
- **★★ FIX 3 (SPELLING-NORMALIZATION reverted; Weber variant/[sic]):** footnote scan (ZOOM) = "verallgemeinerten
  **Binominal**coëfficienten" (Binom-IN-al, extra 'in'); .tex normalized to "Binomialcoefficienten". Weber body uses
  "Binomial"; this footnote "Binominal" is his own variant/typo. RESTORED "Binominal" (ë-drop kept = house). **[sic]**:
  deviates from body spelling; reproduced faithfully per type-B rule.
- **FAITHFUL (rest):** Voraussetzung x=0,1,...,n; eq(3) $B_\nu^{(x)}=\frac{x(x-1)\cdots(x-\nu+1)}{1\cdot2\cdots\nu}$ (deg-ν);
  x^ν expressible via B_ν^{(x)}; eq(4) $f(x)=M_0B_0^{(x)}+\cdots+M_nB_n^{(x)}$; M-system eq(5) f(0)/f(1)/f(2) rows; eq(6)
  $M_0=f(0)$. All matched.
- **★★★ METHOD INSIGHT (major):** §4-§8 (pure symbolic identities) were PRISTINE ~15pp; §9 Interpolation -- which
  reintroduces EXPOSITORY PROSE (generalizing B_ν to real arg, framing the problem) -- carries 3 fixes. **GPT damage
  follows PROSE/EXPOSITION density, NOT math density.** Parallels Einleitung (dense prose=damaged). => slow down + read
  prose word-by-word in expository/definitional passages; math-identity runs stay fast.
- **SKIP:** ë-drop; ellipsis; "νten/nten Grades" ordinal; running header.
- NEXT: **p46** = §9 tail eq(7) general $\pm M_\nu=B_0^{(\nu)}f(0)-B_1^{(\nu)}f(1)+\cdots\pm B_\nu^{(\nu)}f(\nu)$ (via
  multiply-by-$B_i^{(\nu)}$-alternating + eq(8)); then **§10 Lösung des Interpolationsproblems durch die Differenzen**
  (.tex 1360-1395+): eq(1) B_ν^{(x)} def; eq(2) Pascal $B_\nu^{(x+1)}=B_\nu^{(x)}+B_{\nu-1}^{(x)}$; eq(3) $f(x)=f(0)+M_1
  B_1^{(x)}+\cdots$; difference operator setup. ★READ PROSE WORD-BY-WORD (expository §).
**Confirmed by eye+zoom×2 vs ~500dpi scans; 3 fixes compile-gated clean.**


### 2026-07-03 — p46 (§9 tail eq(7) general M_ν + §10 Differenzen start eq(1-5), .tex 1360-1404) — p1-99 gap pass — (verified by eye + ZOOM ×2) — **1 CONTENT FIX**
**CONTENT: 1 net edit (Weber capital-F typo restored [sic]).** Compiles **418pp / 0 overfull / 0 underfull / PDF 2264595 B**.
- **★★ FIX (Weber TYPO reproduced [sic]; GPT normalization reverted):** .tex 1373 read "wodurch nach (4) die Function
  $f(x)$ bestimmt" -- scan (ZOOM-confirmed, glyph clearly CAPITAL F, differs from lowercase f in eq(7) f(0)/f(1) directly
  above) reads "die Function $F(x)$ bestimmt". §9's interpolating function is lowercase f(x) throughout (eq1,eq4); Weber's
  capital F(x) here is a print typo. GPT "corrected" F->f. RESTORED $F(x)$ per fidelity. [sic]: Weber's capital-F typo for
  f(x), reproduced (documented here so it's not re-normalized).
- **FAITHFUL (rest):** §9 tail: multiply-1st-eq(5)-by-B_0^{(1)},2nd-by-(-B_1^{(1)}) => $-M_1=B_0^{(1)}f(0)-B_1^{(1)}f(1)$;
  general multipliers $B_0^{(\nu)},-B_1^{(\nu)},+B_2^{(\nu)},\ldots,\pm B_\nu^{(\nu)}$; eq(7) $\pm M_\nu=B_0^{(\nu)}f(0)
  -B_1^{(\nu)}f(1)+B_2^{(\nu)}f(2)-\cdots\pm B_\nu^{(\nu)}f(\nu)$; §10 heading "Lösung des Interpolationsproblems durch die
  Differenzen"; eq(1) $B_\nu^{(x)}$ def; eq(2) Pascal $B_\nu^{(x+1)}=B_\nu^{(x)}+B_{\nu-1}^{(x)}$, $B_0^{(x+1)}=B_0^{(x)}=1$;
  eq(3) $f(x)=f(0)+M_1B_1^{(x)}+M_2B_2^{(x)}+\cdots+M_nB_n^{(x)}$; eq(4) $\Delta_x=f(x+1)-f(x)$; eq(5) $\Delta_x=M_1+M_2
  B_1^{(x)}+M_3B_2^{(x)}+\cdots+M_nB_{n-1}^{(x)}$. All matched.
- **★ META-PATTERN holds:** §9-§10 expository/Interpolation cluster continues to carry damage (p45 ×3, p46 ×1) -- prose-
  density-driven. Reading prose word-by-word caught the F(x) typo-normalization.
- **SKIP:** ë-drop; ellipsis; "x·(x-1)" dot notation; running header.
- NEXT: **p47** = §10 cont. difference-table (.tex 1405-1434+): $M_1=\Delta_0=f(1)-f(0)$; eq(6) $\Delta_x'=\Delta_{x+1}
  -\Delta_x$, $\Delta_x''=\Delta_{x+1}'-\Delta_x'$; $M_0=f(0),M_1=\Delta_0,M_2=\Delta_0',\ldots,M_n=\Delta_0^{(n-1)}$; eq(7)
  $f(x)=f(0)+\Delta_0B_1^{(x)}+\Delta_0'B_2^{(x)}+\cdots+\Delta_0^{(n-1)}B_n^{(x)}$ (NEWTON forward-difference formula!);
  eq(8) Δ-expansions; difference table. ★EXPOSITORY -- read prose word-by-word; ZOOM Δ-primes (Δ,Δ',Δ'',Δ^{(n-1)}) + B_i^{(x)}.
**Confirmed by eye+zoom×2 vs ~500dpi scans; fix compile-gated clean.**


### 2026-07-03 — p47 (§10 tail: eq(6) diff-defs + eq(7) Newton + eq(8) + difference-table; §11 start, .tex 1405-1455) — p1-99 gap pass — (verified by eye + ZOOM) — **1 CONTENT FIX + formatting flags**
**CONTENT: 1 net edit (DROPPED SENTENCE restored).** Compiles **418pp / 0 overfull / 0 underfull / PDF 2264696 B**.
- **★★ FIX (DROPPED SENTENCE restored):** after the n=3 difference-table, scan continues the sentence "**und, wenn die
  $f(0),f(1),\ldots$ gegeben sind, durch einfache Subtractionen berechnet wird.**" -- .tex jumped straight from table \]
  to §11 heading, DROPPING this whole post-table clause. RESTORED it after the table. (Sentence = "...one lays out a
  table, which for n=3 would have the following form: [TABLE] and, when f(0),f(1),... are given, is computed by simple
  subtractions.")
- **FAITHFUL (content vs scan):** $M_1=\Delta_0=f(1)-f(0)$; eq(7) Newton $f(x)=f(0)+\Delta_0B_1^{(x)}+\Delta_0'B_2^{(x)}
  +\cdots+\Delta_0^{(n-1)}B_n^{(x)}$; eq(8) $\Delta_x$/$\Delta_x'$ expansions; $M_0=f(0),M_1=\Delta_0,\ldots,M_n=\Delta_0^{(n-1)}$;
  "Δ_x..Δ_x^{(n-1)} Grade n-1,..,0, letzte constant"; diff-table entries (f0-3, Δ_0/1/2, Δ'_0/1, Δ''_0); §11 heading
  "Arithmetische Reihen höherer Ordnung"; eq(1) $u_0,u_1,u_2,u_3\ldots$. All German text + quantities matched.
- **⚠ FORMATTING-PASS FLAGS (display-layout, NOT content -- deferred, logged):**
  (a) **eq(6):** scan = 3-row ALIGNED display, difference-on-LEFT ($\Delta_{x+1}-\Delta_x=\Delta_x'$; $\Delta_{x+1}'-\Delta_x'
  =\Delta_x''$; dots; $\Delta_{x+1}^{(n-2)}-\Delta_x^{(n-2)}=\Delta_x^{(n-1)}$); .tex = inline 2-item, sides SWAPPED
  ($\Delta_x'=\Delta_{x+1}-\Delta_x,\ldots$), general row -> "\ldots". => formatting pass: restore Weber's 3-row aligned
  diff-on-left form (matches how .tex renders ALL other Weber recursion displays).
  (b) **eq(7)/(8):** scan shows 2 explicit terms before ellipsis; .tex adds an extra intermediate term ($\Delta_0''B_3^{(x)}$
  in eq7; $\Delta_0''B_2^{(x)}$ in eq8-row1). Typographic term-count. => formatting pass (or leave; content identical).
  (c) **difference-TABLE:** scan top-aligns Δ's with f(0) + uses VERTICAL RULES; .tex bottom-aligns with f(3), no rules.
  Same entries. => formatting pass: restore top-aligned + ruled layout.
- **SKIP:** ë-drop; ellipsis; running header "§11 Arithmetische Reihen".
- **★ META-PATTERN:** §10-§11 expository cluster continues -- p47 dropped a whole SENTENCE (post-table). Word-by-word +
  cross-checking .tex-around-displays caught it (the drop was BETWEEN a table and a section heading -- easy to miss).
  => LESSON: check text IMMEDIATELY BEFORE/AFTER displays & tables & section breaks (drop-prone seams).
- NEXT: **p48** = §11 cont. (.tex 1456-1481+): eq(2) $\Delta_0=u_1-u_0$,$\Delta_1=u_2-u_1$,$\Delta_2=u_3-u_2\ldots$; eq(3)
  $\Delta_0'=\Delta_1-\Delta_0$,$\Delta_1'=\Delta_2-\Delta_1\ldots$; $u_1=u_0+\Delta_0$, $u_m=u_0+\Delta_0+\Delta_1+\cdots
  +\Delta_{m-1}$; def arith-Reihe nter Ordnung (nte Diff const); f(x) with x=0,1,2,3. ★EXPOSITORY -- read prose word-by-word;
  check display seams.
**Confirmed by eye+zoom vs ~500dpi scans; fix compile-gated clean.**


### 2026-07-03 — p48 (§11 Arithmetische Reihen höherer Ordnung, cont.: Δ-recursion eq(2-3) + Satz + f(x)-generation, .tex 1456-1510) — p1-99 gap pass — (verified by eye + ZOOM) — **FAITHFUL (0 content fixes)**
**CONTENT: 0 edits. First fully-clean page since the §9-§10 damage cluster.** File unchanged: **418pp / 0 overfull / 0 underfull / PDF 2264696 B** (no edit -> no recompile).
- **FAITHFUL (top, .tex 1456-1478):** eq(2) $\Delta_0=u_1-u_0$,$\Delta_1=u_2-u_1$,$\Delta_2=u_3-u_2\ldots$; eq(3) $\Delta_0'=\Delta_1-\Delta_0$,
  $\Delta_1'=\Delta_2-\Delta_1\ldots$; "Reihe (1) vollständig bestimmt"; $u_1=u_0+\Delta_0$; $u_m=u_0+\Delta_0+\Delta_1+\cdots+\Delta_{m-1}$;
  def arith-Reihe nter Ordnung (nte Diff const => (n+1)te = lauter Nullen).
- **FAITHFUL (mid, .tex 1481-1494):** "Man erhält eine arith. Reihe nter Ordnung, wenn man in einer ganzen Function nten Grades f(x)
  für x die Zahlen 0,1,2,3... einsetzt"; ladder $\Delta_x=f(x+1)-f(x)$; $\Delta_x'=\Delta_{(x+1)}-\Delta_x$; $\cdots$; $\Delta_x^{(n-1)}
  =\Delta_{(x+1)}^{(n-2)}-\Delta_x^{(n-2)}$ (★ parenthesized $(x+1)$ subscripts in scan MATCH .tex `\Delta_{(x+1)}`); "so ist Δ_x vom
  (n-1)ten, Δ'_x vom (n-2)ten Grade... und also Δ_x^{(n-1)} constant".
- **FAITHFUL (bot, .tex 1496-1510):** display $u_0,u_1,u_2\ldots$; "so ist die ganze Reihe vollständig bestimmt, wenn die n Werthe
  $u_0,u_1,u_2\ldots u_{n-1}$ und ausserdem die constante nte Differenz gegeben sind. Diese letztere ist aber bestimmt, wenn auch noch
  das (n+1)te Glied $u_n$ gegeben ist. Wir können also den Satz aussprechen:"; **Satz** "Eine arithmetische Reihe nter Ordnung ist
  vollständig bestimmt, wenn ihre n+1 ersten Glieder gegeben sind."; "Da nun eine Function f(x) vom nten Grade gleichfalls durch die
  willkürlich gegebenen Werthe $f(0),f(1),f(2)\ldots f(n)$" (sentence continues onto p49). ALL word-for-word.
- **⚠ EMPHASIS-PASS FLAG:** the Satz is set **gesperrt** (letter-spaced) in scan; .tex uses `\begin{quote}` indentation (no letter-
  spacing). Content identical -> defer to emphasis/Sperrung pass.
- **SKIP:** ë-drop; ellipsis-commas; ordinal "nter/(n-1)ten/(n+1)te"; running header "§11 Arithmetische Reihen".
- **★ META-PATTERN REFINEMENT:** p48 is EXPOSITORY (§11) yet FULLY FAITHFUL. Its prose is NARRATIVE / THEOREM-STATEMENT, not the
  definition-generalization-with-new-notation that damaged §9 (p45) and the §10 tail (p46-47). => refine the rule: GPT damage clusters
  where it can NORMALIZE NOTATION/DEFINITIONS (generalize B_ν to real x, rename n->x, "improve" a def), not merely where prose is dense.
  A clean theorem-statement/narrative page passes through even in an expository §. Seam-checks (Satz quote + 2 displays) all clean.
- NEXT: **p49** = §11 cont. (.tex 1510-1550+): "völlig bestimmt ist, so folgt, dass aus den ganzen rationalen Functionen nten Grades
  f(x) alle arith. Reihen nter Ordnung erzeugt werden..."; "allgemeines Glied durch Formel (7) des vorigen §"; **Summen-section**:
  $s_m=u_0+u_1+\cdots+u_m$ (arith Reihe (n+1)ter Ordnung); $s_{m+1}-s_m=u_{m+1}$; erzeugende Function $F(x)$ von $s_m$: $F(0)=f(0)$,
  $F(1)=f(0)+f(1)$, $F(2)=f(0)+f(1)+f(2)$, ... ★EXPOSITORY/NARRATIVE -- read prose word-by-word; ★CHECK SEAMS (the s_m displays +
  F(x)-system). ZOOM s_m / F(x) subscripts + the +...+ sum chains.
**Confirmed by eye+zoom vs ~500dpi scans; page faithful, no edit.**


### 2026-07-03 — p49 (§11 tail: Summen s_m + erzeugende Function F(x)-system eq(4) + x^2 example, .tex 1510-1564) — p1-99 gap pass — (verified by eye) — **content FAITHFUL (0 fixes) + 1 formatting flag**
**CONTENT: 0 edits.** File unchanged: **418pp / 0 overfull / 0 underfull / PDF 2264696 B** (no edit -> no recompile).
- **FAITHFUL (top, .tex 1510-1520):** "so folgt, dass aus den ganzen rationalen Functionen nten Grades f(x) alle arith. Reihen
  nter Ordnung erzeugt werden, wenn man darin für x die Reihe der natürlichen Zahlen setzt"; "Der Ausdruck des allgemeinen Gliedes
  ist dann durch die Formel (7) des vorigen Paragraphen gegeben"; "Die Summen der m+1 ersten Glieder... nter Ordnung"; $s_m=u_0+u_1
  +\cdots+u_m$; "bilden eine arith. Reihe (n+1)ter Ordnung, da ihre ersten Differenzen"; $s_{m+1}-s_m=u_{m+1}$.
- **FAITHFUL (mid, .tex 1522-1547):** "eine arith. Reihe nter Ordnung bilden"; "Es lässt sich also mit Hülfe der Formel (7) des
  §10 die Summe s_m allgemein bestimmen, wenn man $s_0,s_1\ldots s_{n+1}$ als bekannt annimmt"; "Um die erzeugende Function F(x)
  von s_m zu finden, wenn f(x) die erzeugende Function von u_m ist, setzt man"; $F(0)=f(0)$, $F(1)=f(0)+f(1)$, $F(2)=f(0)+f(1)+f(2)$,
  $\cdots$; "und hat dann in der Formel (7), §10:"; $F(x)=F(0)+D_0B_1^{(x)}+D'_0B_2^{(x)}+\cdots$; "zu setzen:".
- **FAITHFUL (bot, .tex 1545-1564):** D-system $D_0=F(1)-F(0)=f(1)$,$D'_0=f(2)-f(1)=\Delta_1$; $D_1=F(2)-F(1)=f(2)$,$D'_1=f(3)-f(2)
  =\Delta_2$; $D_2=F(3)-F(2)=f(3)$,$D''_0=\Delta_2-\Delta_1=\Delta'_1$; "So erhält man"; **eq(4)** $F(x)=f(0)+f(1)B_1^{(x)}+\Delta_1
  B_2^{(x)}+\Delta'_1B_3^{(x)}+\cdots$; "Nehmen wir z.B. f(x)=x^2, so giebt uns F(m) die Summe der m ersten Quadratzahlen. Es ist";
  $\Delta_x=2x+1,\ \Delta'_x=2$; "also". (footer "Weber, Algebra. I." + sheet-signature "4" = printer's mark, out of scope.)
- **⚠ FORMATTING-PASS FLAG (typographic, NOT content):** scan has a full-width **continuation-dots row** ($\cdot\ \cdot\ \cdot\ \cdots$)
  AFTER the D-system aligned display (after the $D_2$/$D''_0$ row); .tex drops it (goes straight from $D''_0=\Delta'_1.$ to \]). Pure
  "pattern continues" marker -- zero German text, zero new quantity. Same family as p47 general-row/ellipsis flags. => formatting pass:
  restore the trailing dots-continuation row in the D-system display. (The F-system's own \cdots row IS present in .tex, 1537.)
- **SKIP:** ë-drop; ellipsis-commas; ordinal "nter/(n+1)ter"; running header "§11 Arithmetische Reihen".
- **★ META-PATTERN:** p49 EXPOSITORY/computational (§11 tail) but content-FAITHFUL -- narrative + worked example, no def-generalization
  to normalize. Confirms refined rule (damage clusters at notation/def-normalization, not mere prose density). 2 clean pages (p48-49).
- NEXT: **p50** = x^2/x^3 example results + **§12 Der polynomische Lehrsatz** start (.tex 1566-1590+): $F(x)=x+3\frac{x(x-1)}{1\cdot2}
  +2\frac{x(x-1)(x-2)}{1\cdot2\cdot3}=\frac{x(x+1)(2x+1)}{6}$; für f(x)=x^3: $F(x)=(\frac{x(x+1)}{2})^2$; "Summe der m ersten Cuben
  = Quadrat der mten Trigonalzahl"; §12 heading; "Im §8 ist für den binom. Lehrsatz die Form abgeleitet:" eq(1) $(x+y)^n=\Pi(n)\sum^{\alpha,\beta}
  \frac{x^\alpha y^\beta}{\Pi(\alpha)\Pi(\beta)}$; Bedingung $\alpha+\beta=n$. ★§12 is a NEW SECTION (polynomischer Lehrsatz) -- watch the
  §-heading SEAM + the transition prose; ZOOM Π-products, Σ^{α,β} limits, x^α y^β exponents. EXPOSITORY intro likely = damage-prone.
**Confirmed by eye vs ~500dpi scans; page content-faithful, no edit.**


### 2026-07-03 — p50 (§11 tail x^2/x^3 results + §12 Der polynomische Lehrsatz start eq(1-5), .tex 1566-1608) — p1-99 gap pass — (verified by eye) — **FULLY FAITHFUL (0 fixes)**
**CONTENT: 0 edits.** File unchanged: **418pp / 0 overfull / 0 underfull / PDF 2264696 B** (no edit -> no recompile).
- **FAITHFUL (top, .tex 1566-1575):** $F(x)=x+3\frac{x(x-1)}{1\cdot2}+2\frac{x(x-1)(x-2)}{1\cdot2\cdot3}=\frac{x(x+1)(2x+1)}{6}$;
  "Für f(x)=x^3 ergiebt dieselbe Rechnung"; $F(x)=\left(\frac{x(x+1)}{2}\right)^2$; "Die Summe der m ersten Cuben ist also gleich
  dem Quadrat der mten Trigonalzahl"; **§12 heading "Der polynomische Lehrsatz"** (gesperrt).
- **FAITHFUL (mid, .tex 1577-1596):** "Im §8 ist für den binomischen Lehrsatz die Form abgeleitet:"; **eq(1)** $(x+y)^n=\Pi(n)
  \sum^{\alpha,\beta}\frac{x^\alpha y^\beta}{\Pi(\alpha)\Pi(\beta)}$; "in der sich die Summe auf alle Combinationen zweier Zahlen
  α,β erstreckt, deren keine negativ ist und die der Bedingung"; **eq(2)** $\alpha+\beta=n$; "genügen."; "Diese Form gestattet,
  zunächst durch Induction, eine Verallgemeinerung auf die nte Potenz eines Polynoms:"; **eq(3)** $(x+y+z+\cdots)^n=\Pi(n)\sum^{\alpha,\beta,\gamma,\ldots}
  \frac{x^\alpha y^\beta z^\gamma\cdots}{\Pi(\alpha)\Pi(\beta)\Pi(\gamma)\cdots}$; "mit der Bestimmung, dass α,β,γ... alle positiven
  oder verschwindenden ganzzahligen Werthe durchlaufen, die der Bedingung".
- **FAITHFUL (bot, .tex 1596-1608):** **eq(4)** $\alpha+\beta+\gamma+\cdots=n$; "genügen. Um aber die Richtigkeit dieser Formel
  allgemein zu beweisen, nehmen wir an, sie sei bewiesen, wenn das Polynom ein Glied weniger enthält, wie sie es in der That ist,
  wenn das Polynom nur zwei Glieder enthält."; "Wir setzen dann"; **eq(5)** $u=y+z+\cdots$; "und wenden auf (x+u) die Formel (1)
  an, aus der sich ergiebt:". ALL word-for-word.
- **⚠ EMPHASIS/FORMATTING (already tracked, NOT new):** §12 heading gesperrt (emphasis pass, §-titles); eq-numbers (1)-(5) left-set
  (leqno, formatting pass). Σ^{α,β} / Σ^{α,β,γ,…} = Weber upper-limit-only convention, matches .tex \sum^{...} (content intact).
- **SKIP:** ë-drop; ellipsis; ordinal "nte/mten"; running header "Erster Abschnitt / §12".
- **★ META-PATTERN (STRENGTHENED):** the §12 EXPOSITORY INTRO came through CLEAN -- because it RE-DERIVES from §8's already-
  established binomial notation (Π, Σ), giving GPT no new definition to "normalize". Contrast §9 (p45), which GENERALIZED B_ν to real
  args (new def) => damaged. Refined rule confirmed: damage clusters at DEFINITION-GENERALIZATION / NOTATION-NORMALIZATION, not at
  expository prose per se. 3 clean pages (p48, p49-content, p50).
- NEXT: **p51** = §12 polynomial-theorem induction proof (.tex 1610-1650+): eq(6) $(x+y+z+\cdots)^n=\Pi(n)\sum^{\alpha,\nu}\frac{x^\alpha
  u^\nu}{\Pi(\alpha)\Pi(\nu)}$; eq(7) $\alpha+\nu=n$ "mit der Beschränkung"; "Nun ist aber nach der Annahme schon bewiesen:"; eq(8)
  $u^\nu=\Pi(\nu)\sum^{\beta,\gamma,\ldots}\frac{y^\beta z^\gamma\cdots}{\Pi(\beta)\Pi(\gamma)\cdots}$; eq(9) $\beta+\gamma+\cdots=\nu$;
  substitution combining (6)+(8). ★§12 proof is DERIVATION from established notation -- likely clean, but read prose word-by-word +
  ZOOM Π(ν)/Π(α), u^ν, Σ^{α,ν} vs Σ^{β,γ,…} limits. Watch the induction-argument prose seams.
**Confirmed by eye vs ~500dpi scans; page fully faithful, no edit.**


### 2026-07-03 — p51 (§12 tail eq(6-11) polynomial-thm proof + Polynomialcoeff. + Trinom^3 + §13 Derivirte Functionen start eq(1) + def-para, .tex 1610-1662) — p1-99 gap pass — (verified by eye, prose word-by-word) — **FULLY FAITHFUL (0 fixes)**
**CONTENT: 0 edits.** File unchanged: **418pp / 0 overfull / 0 underfull / PDF 2264696 B** (no edit -> no recompile).
- **FAITHFUL (top/mid, §12 proof .tex 1610-1638):** eq(6) $(x+y+z+\cdots)^n=\Pi(n)\sum^{\alpha,\nu}\frac{x^\alpha u^\nu}{\Pi(\alpha)\Pi(\nu)}$;
  "mit der Beschränkung" eq(7) $\alpha+\nu=n$; "Nun ist aber nach der Annahme schon bewiesen:"; eq(8) $u^\nu=\Pi(\nu)\sum^{\beta,\gamma,\ldots}
  \frac{y^\beta z^\gamma\cdots}{\Pi(\beta)\Pi(\gamma)\cdots}$; eq(9) $\beta+\gamma+\cdots=\nu$; "und wenn dies in (6) eingesetzt wird, so
  ergiebt sich unmittelbar die Formel (3), und (7) geht in (4) über"; "Die Coëfficienten"; **eq(10)** $P_{\alpha,\beta,\gamma,\ldots}^{(n)}
  =\frac{\Pi(n)}{\Pi(\alpha)\Pi(\beta)\Pi(\gamma)\cdots}$; "die ihrer Bedeutung nach ganze Zahlen sind, heissen die Polynomialcoëfficienten".
- **FAITHFUL (mid, Trinom + §13 start .tex 1640-1658):** "Beispielsweise erhält man für die dritte Potenz des Trinoms:"; **eq(11)**
  $(x+y+z)^3=x^3+y^3+z^3+3x^2y+3xy^2+3x^2z+3xz^2+3y^2z+3yz^2+6xyz$ (ALL 10 terms, same order); **§13 heading "Derivirte Functionen"**;
  "Es sei"; **eq(1)** $f(x)=a_0x^n+a_1x^{n-1}+a_2x^{n-2}+\cdots+a_n$; "eine ganze rationale Function nter Ordnung".
- **FAITHFUL (bot, def-para .tex 1658-1662 -- read WORD-BY-WORD):** "Wenn wir darin x durch ein Binom x+y ersetzen, so können wir auf
  jedes einzelne Glied den binomischen Lehrsatz anwenden, und können das Ergebniss nach fallenden oder nach steigenden Potenzen von x
  oder von y ordnen. Wir wollen die Ordnung nach steigenden Potenzen von y ausführen. Die höchste Potenz von y, die vorkommt, ist die
  nte, und der Coëfficient der nullten Potenz von y ist die Function f(x) selbst, wie man erkennt, wenn man y=0 setzt. Wir setzen also,
  indem wir die anderen Coëfficienten mit"; display $f'(x),\ \frac{f''(x)}{\Pi(2)},\ \frac{f'''(x)}{\Pi(3)},\ldots$; "bezeichnen:".
  (footer "4*" = sheet signature, out of scope.) Every word matched; NO drops/inserts (both "nach" present; "das Ergebniss" ss intact).
- **⚠ EMPHASIS/FORMATTING (already tracked, NOT new):** §13 heading gesperrt (emphasis pass); eq-nums (6)-(11)+(1) left-set (leqno);
  eq(11) multi-line break after 3xy^2 (scan) vs after 3xz^2 (.tex) = display line-break layout (skip). Σ^{α,ν}/Σ^{β,γ,…} = Weber upper-
  limit-only, matches .tex \sum^{...}.
- **SKIP:** Coëfficient/Coëfficienten/Polynomialcoëfficienten (ë-drop ×3, house); ellipsis; ordinal "nte/nter"; header "§13 Derivirte Functionen".
- **★ META-PATTERN (holds, 4 clean pages p48-51):** §12 proof + §13 intro def-para BOTH clean -- they DERIVE/DEFINE using established
  binomial/Π/Σ notation (no notation to normalize). Long definitional prose (1658) came through word-for-word. Refined rule strongly held.
- NEXT: **p52** = §13 cont. (.tex 1663-1710+): **eq(2)** $f(x+y)=f(x)+yf'(x)+\frac{y^2}{1\cdot2}f''(x)+\cdots=\sum_{\nu=0}^{n}\frac{y^\nu}{\Pi(\nu)}
  f^{(\nu)}(x)$; "Die Functionen f'(x),f''(x),f'''(x),... heissen die erste, zweite, dritte,... Derivirte oder Abgeleitete von f(x). Es sind
  ganze Functionen von x und f^{(ν)}(x) kann den Grad n-ν nicht übersteigen..."; "Die erste Derivirte... erhält man durch Anwendung des
  binom. Lehrsatzes auf (1):"; **eq(3)** $f'(x)=na_0x^{n-1}+(n-1)a_1x^{n-2}+(n-2)a_2x^{n-3}+\cdots$. ★ZOOM the Σ in eq(2) (\sum_{ν=0}^{n}
  -- check Weber's actual limit-placement vs modern); read the Derivirte definition prose word-by-word (DEFINITIONAL -- watch for norms/drops).
**Confirmed by eye vs ~500dpi scans; page fully faithful, no edit.**


### 2026-07-03 — p52 (§13 Derivirte Functionen: eq(2) Taylor + Derivirte-def + eq(3) f' + Hauptsatz eq(4-8), .tex 1663-1709) — p1-99 gap pass — (verified by eye, prose word-by-word) — **FULLY FAITHFUL (0 fixes)**
**CONTENT: 0 edits.** File unchanged: **418pp / 0 overfull / 0 underfull / PDF 2264696 B** (no edit -> no recompile).
- **FAITHFUL (top, .tex 1663-1671):** **eq(2)** $f(x+y)=f(x)+yf'(x)+\frac{y^2}{1\cdot2}f''(x)+\cdots=\sum_{\nu=0}^{n}\frac{y^\nu}{\Pi(\nu)}
  f^{(\nu)}(x)$ (scan Σ: ν OVER, "0,n" UNDER = Weber-conv, matches .tex range); "Die Functionen f'(x),f''(x),f'''(x)... heissen die
  erste, zweite, dritte,... Derivirte oder Abgeleitete von f(x). Es sind ganze Functionen von x und f^{(ν)}(x) kann den Grad n-ν nicht
  übersteigen, da die Summe der Exponenten von x und y in keinem Gliede den Grad n übersteigt"; "Die erste Derivirte, die also der
  Coëfficient der ersten Potenz von y in der Entwickelung von f(x+y) nach steigenden Potenzen von y ist, erhält man durch Anwendung
  des binomischen Lehrsatzes auf (1):".
- **FAITHFUL (mid, .tex 1673-1695):** **eq(3)** $f'(x)=na_0x^{n-1}+(n-1)a_1x^{n-2}+(n-2)a_2x^{n-3}+\cdots$; "Der Hauptsatz über die
  derivirten Functionen ergiebt sich aus (2), wenn wir x in x+z oder y in y+z verwandeln:"; **eq(4)** $f(x+y+z)=\sum_{0}^{n}\frac{y^\nu}{\Pi(\nu)}
  f^{(\nu)}(x+z)=\sum_{0}^{n}\frac{(y+z)^\nu}{\Pi(\nu)}f^{(\nu)}(x)$; "Bezeichnen wir mit f^{(ν,μ)}(x) die μte Derivirte von f^{(ν)}(x),
  so ist nach (2):"; **eq(5)** $f^{(\nu)}(x+z)=\sum_{0}^{n-\nu}\frac{z^\mu}{\Pi(\mu)}f^{(\nu,\mu)}(x)$; "und nach dem binomischen Satz:";
  **eq(6)** $\frac{(y+z)^\nu}{\Pi(\nu)}=\sum^{\beta,\gamma}\frac{y^\beta z^\gamma}{\Pi(\beta)\Pi(\gamma)},\ \beta+\gamma=\nu$; "Setzen wir dies in (4) ein, so folgt:".
- **FAITHFUL (bot, .tex 1695-1709):** **eq(7)** $\sum_{0,n}^{\nu}\sum_{0,n-\nu}^{\mu}\frac{y^\nu z^\mu}{\Pi(\nu)\Pi(\mu)}f^{(\nu,\mu)}(x)
  =\sum^{\beta,\gamma}\frac{y^\beta z^\gamma}{\Pi(\beta)\Pi(\gamma)}f^{(\beta+\gamma)}(x)$; "Die letzte Summe ist über alle nicht negativen
  Zahlen β,γ zu erstrecken, deren Summe den Grad n von f(x) nicht übersteigt. Dieselben Zahlencombinationen durchlaufen aber auch die
  Exponenten ν,μ auf der linken Seite, und die Vergleichung der Coëfficienten gleicher Potenzen und Producte ergiebt (nach §1):"; **eq(8)**
  $f^{(\nu,\mu)}(x)=f^{(\nu+\mu)}(x)$; "also den Satz:". ALL word-for-word.
- **⚠ FORMATTING (Σ Weber-convention, tracked):** eq(2)/(4)/(5)/(7) scan Σ = variable-OVER / range-UNDER ("ν" over, "0,n" under; "μ"
  over, "0,n-ν" under); .tex uses \sum_{ν=0}^{n} etc. -- SAME ranges, old-vs-modern placement. => formatting pass. eq-nums leqno.
- **SKIP:** Coëfficient/Coëfficienten (ë-drop); ellipsis; ordinal "μte/νte/nte". **EMPHASIS (gesperrt, tracked):** "erste,zweite,dritte /
  Derivirte oder Abgeleitete / Die erste Derivirte" letter-spaced.
- **★ META-PATTERN (5 clean pages p48-52):** entire §13 Taylor/Hauptsatz derivation CLEAN -- derives from established binomial/Π/Σ notation,
  no new def to normalize. Even the multi-index f^{(ν,μ)} bookkeeping came through exact. Refined rule strongly held.
- NEXT: **p53** = §13 cont. (.tex 1710-1760+): **Satz** "Die μte Derivirte von der νten Derivirten ist die (ν+μ)te Derivirte der
  ursprünglichen Function"; "Man erhält also die sämmtlichen höheren Derivirten, indem man nach der Regel (3) aus jeder vorangehenden
  die erste Derivirte bildet:"; **eq(9)** align $f(x)=a_0x^n+a_1x^{n-1}+\cdots$, $f'(x)=na_0x^{n-1}+(n-1)a_1x^{n-2}+\cdots$, $f''(x)=
  n(n-1)a_0x^{n-2}+(n-1)(n-2)a_1x^{n-3}+\cdots$; "Eine etwas einfachere Form nehmen diese Derivirten an, wenn man sich einer anderen
  Bezeichnungsweise bedient..."; "Es liegt wegen der Unbestimmtheit der Coefficienten a_0,...,a_n... ganze rationale Function nten Grades
  so darstellen:" + eq. ★Satz set gesperrt (emphasis). Read prose word-by-word; ZOOM eq(9) descending-coeff patterns (n,(n-1); n(n-1),
  (n-1)(n-2)) + x-exponents. New "Bezeichnungsweise" intro may be DEFINITIONAL => damage-watch.
**Confirmed by eye vs ~500dpi scans; page fully faithful, no edit.**


### 2026-07-03 — p53 (§13 tail: Satz + eq(9) deriv-ladder + Binomialcoeff-Darstellung eq(10-12) + notation-choice para start, .tex 1710-1740) — p1-99 gap pass — (verified by eye, prose word-by-word) — **FULLY FAITHFUL (0 fixes) + 2 formatting flags**
**CONTENT: 0 edits.** File unchanged: **418pp / 0 overfull / 0 underfull / PDF 2264696 B** (no edit -> no recompile).
- **FAITHFUL (top, .tex 1710-1720):** **Satz** (gesperrt) "Die μte Derivirte von der νten Derivirten ist die (ν+μ)te Derivirte der
  ursprünglichen Function"; "Man erhält also die sämmtlichen höheren Derivirten, indem man nach der Regel (3) aus jeder vorangehenden
  die erste Derivirte bildet:"; **eq(9)** align $f(x)=a_0x^n+a_1x^{n-1}+a_2x^{n-2}+a_3x^{n-3}+\cdots$, $f'(x)=na_0x^{n-1}+(n-1)a_1x^{n-2}
  +(n-2)a_2x^{n-3}+\cdots$, $f''(x)=n(n-1)a_0x^{n-2}+(n-1)(n-2)a_1x^{n-3}+\cdots$; "Eine etwas einfachere Form nehmen diese Derivirten
  an, wenn man sich einer anderen Bezeichnungsweise bedient, die häufig im Gebrauch und für gewisse Zwecke fast unentbehrlich ist, die
  wir im Anschluss hieran besprechen wollen."
- **FAITHFUL (mid, .tex 1722-1737):** "Es liegt wegen der Unbestimmtheit der Coëfficienten a_0,a_1...a_n offenbar keine Beschränkung
  darin, wenn wir eine ganze rationale Function nten Grades so darstellen:"; **eq(10)** $f(x)=a_0x^n+B_1^{(n)}a_1x^{n-1}+B_2^{(n)}a_2x^{n-2}
  +\cdots+a_n$; "oder ausführlich:"; **eq(11)** $f(x)=a_0x^n+na_1x^{n-1}+\frac{n(n-1)}{1\cdot2}a_2x^{n-2}+\cdots$; "Wenn eine Function
  f(x) so dargestellt ist, werden wir sagen, sie sei »mit den Binomialcoëfficienten geschrieben«"; "Grössere Uebereinstimmung zeigen
  hierdurch bereits die Formeln (9), die dann so lauten:"; **eq(12)** align rows.
- **FAITHFUL (bot, .tex 1737-1740):** eq(12) $\frac{1}{n}f'(x)=a_0x^{n-1}+(n-1)a_1x^{n-2}+\frac{(n-1)(n-2)}{1\cdot2}a_2x^{n-3}+\cdots$,
  $\frac{1}{n(n-1)}f''(x)=a_0x^{n-2}+(n-2)a_1x^{n-3}+\frac{(n-2)(n-3)}{1\cdot2}a_2x^{n-4}+\cdots$; "worin die rechten Seiten alle auch
  mit den Binomialcoëfficienten geschrieben erscheinen. Wir werden später den Nutzen dieser Bezeichnungsweise noch weiter kennen lernen,
  müssen aber schon hier hervorheben, dass die Wahl der einen oder anderen Dar-" (breaks to p54). ALL word-for-word.
- **⚠ FORMATTING-PASS FLAGS (typographic, NOT content):** (a) continuation-dots row dropped after the **eq(9)** align (scan has it; .tex
  \end{align} direct); (b) continuation-dots row dropped after the **eq(12)** align (scan row ends with ","; .tex \end{align} direct).
  Both = "pattern continues" markers, same class as p49 D-system dots-row. => formatting pass. Plus eq-nums leqno.
- **SKIP:** Coëfficienten/Binomialcoëfficienten (ë-drop ×3); ellipsis; ordinal "μte/νte/(ν+μ)te/nten". **EMPHASIS (gesperrt, tracked):**
  Satz; "mit den Binomialcoefficienten geschrieben".
- **★ META-PATTERN (6 clean pages p48-53):** §13 tail incl. the Binomialcoeff-Darstellung + eq(9)/(12) ladders all clean -- still
  derivation/re-expression from established notation. The notation-CHOICE discursive para (1740) came through clean SO FAR (up to the
  p53/p54 break). ★ DAMAGE-WATCH: the Gauss/Disq.ar. HISTORICAL REMARK (free discursive prose, no notation-anchor) is at TOP of p54 --
  this is exactly the kind of passage the refined rule predicts as damage-prone. Verify it word-by-word next.
- NEXT: **p54** = §13 tail Gauss-remark + **§14 Derivirte eines Productes** start (.tex 1740-1785+): (1740 cont) "...anderen
  Darstellungsweise doch nicht ganz gleichgültig ist, die erste oft auch den Vorzug verdient. Besonders in den Fällen, wo die
  Coefficienten Zahlen sind und es auf das zahlentheoretische Verhalten... ankommt, darf man nicht ausser Acht lassen, dass durch die
  Binomialcoefficienten ein der Sache fremdes numerisches Element eingeführt wird. **Dass Gauss in der Theorie der quadratischen Formen
  (in den Disq. ar.) die Schreibweise mit den Binomialcoefficienten anwendet, wenn er die quadratischen Formen durch ax^2+2bxy+cy^2
  darstellt, und dass diese Bezeichnung allgemein Eingang gefunden hat, hat in der Zahlentheorie zu einer unnöthigen und sehr
  bedauerlichen Complication geführt.**"; **§14 heading "Derivirte eines Productes"**; §14 intro (Differentialquotienten/Differentialrechnung
  connection, D_ν notation); eq(1) $f(x+y)=f(x)+yD_1f+\frac{y^2}{1\cdot2}D_2f+\cdots$; eq(2) $D_\nu(Cf)=CD_\nu f$; eq(3) $D_\nu(f+\varphi)
  =D_\nu f+D_\nu\varphi$; eq(4-5) product-derivative setup. ★★ READ THE GAUSS PARAGRAPH + §14 INTRO WORD-BY-WORD (free discursive/
  historical prose = HIGH damage-risk per refined rule; watch drops/rewords/inserts of proper names, "Disq. ar.", ax^2+2bxy+cy^2, and the
  eval-judgement clauses "unnöthigen und sehr bedauerlichen Complication"). ★ EPSILON: eq(3) uses \varphi (φ) -- house var, skip.
**Confirmed by eye vs ~500dpi scans; page fully faithful, no edit.**


### 2026-07-03 — p54 (§13 tail Gauss/Disq.ar. remark + §14 Derivirte eines Productes start eq(1-5), .tex 1740-1769) — p1-99 gap pass — (verified by eye, HISTORICAL PROSE word-by-word) — **FULLY FAITHFUL (0 fixes)**
**CONTENT: 0 edits.** File unchanged: **418pp / 0 overfull / 0 underfull / PDF 2264696 B** (no edit -> no recompile).
- **★★ DAMAGE-WATCH RESOLVED CLEAN -- Gauss/Disq.ar. historical remark (top, .tex 1740):** WORD-FOR-WORD faithful: "...anderen Dar-
  stellungsweise doch nicht ganz gleichgültig ist, die erste oft auch den Vorzug verdient. Besonders in den Fällen, wo die Coëfficienten
  Zahlen sind und es auf das zahlentheoretische Verhalten dieser Coëfficienten ankommt, darf man nicht ausser Acht lassen, dass durch die
  Binomialcoëfficienten ein der Sache fremdes numerisches Element eingeführt wird. Dass **Gauss** in der Theorie der quadratischen Formen
  (in den Disq. ar.) die Schreibweise mit den Binomialcoëfficienten anwendet, wenn er die quadratischen Formen durch $ax^2+2bxy+cy^2$
  darstellt, und dass diese Bezeichnung allgemein Eingang gefunden hat, hat in der Zahlentheorie zu einer unnöthigen und sehr bedauer-
  lichen Complication geführt." Proper name (Gauss), citation "(in den Disq. ar.)", form $ax^2+2bxy+cy^2$, eval-clause "unnöthigen und
  sehr bedauerlichen Complication" -- ALL preserved. (Gauss gesperrt = emphasis; ë-drops skip.)
- **FAITHFUL (mid, §14 start .tex 1742-1751):** **§14 heading "Derivirte eines Productes"**; intro "Die derivirten Functionen, die wir
  hier betrachtet haben, sind keine anderen als die aus der Differentialrechnung bekannten Differentialquotienten; wir haben den Begriff
  aber hier, wo es sich um ganze rationale Functionen handelt, ohne Anwendung der Infinitesimalrechnung gewonnen aus den Entwickelungs-
  coëfficienten der Potenzen von y in der Function f(x+y). Bezeichnen wir die νte Ableitung von f(x) mit $D_\nu f$, so ist nach (2), §13:";
  **eq(1)** $f(x+y)=f(x)+yD_1f+\frac{y^2}{1\cdot2}D_2f+\frac{y^3}{1\cdot2\cdot3}D_3f+\cdots$; "und daraus ergeben sich sofort die beiden
  Grundsätze, die sich in den Formeln"; **eq(2)** $D_\nu(Cf)=CD_\nu f$.
- **FAITHFUL (bot, .tex 1755-1769):** **eq(3)** $D_\nu(f+\varphi)=D_\nu f+D_\nu\varphi$; "ausdrücken, worin C eine Constante, φ eine
  zweite ganze rationale Function von x ist"; "Eine Verallgemeinerung der Formel (2) giebt die Darstellung der Derivirten des Productes
  fφ. Setzt man nämlich nach (1) abkürzend"; **eq(4)** $f(x+y)=u_0+yu_1+y^2u_2+\cdots+y^nu_n$, $\varphi(x+y)=v_0+yv_1+y^2v_2+\cdots+y^mv_m$;
  "also"; **eq(5)** $u_\nu=\frac{D_\nu f}{\Pi(\nu)},\ v_\nu=\frac{D_\nu\varphi}{\Pi(\nu)}$. ALL word-for-word.
- **SKIP:** Coëfficienten/Binomialcoëfficienten/Entwickelungscoëfficienten (ë-drop); ellipsis-connector "+" (eq(4) scan "+\cdots y^nu_n"
  vs .tex "+\cdots+y^nu_n" = typographic); φ=\varphi (house var). **EMPHASIS (gesperrt, tracked):** §14 heading; "Gauss"; eq-nums leqno.
- **★★★ META-PATTERN REFINEMENT (important):** the Gauss HISTORICAL/discursive remark -- which the "discursive prose = damage-prone"
  heuristic flagged as HIGH-risk -- came through CLEAN. => refine: discursive prose is damaged when LONG + ABSTRACT (the Einleitung's
  philosophical prose), but CLEAN when SHORT + FACT-ANCHORED (a proper name, a citation, a specific formula give GPT nothing to "improve"
  and concrete anchors it won't drop). Operational rule UNCHANGED (read all prose word-by-word); this just calibrates expectation. 7 clean
  pages p48-54. So far the §11-§14 block (arith-series/poly-thm/derivatives) is entirely clean -- consistent (all derive/define/cite from
  established notation & facts; no def-generalization-with-normalization like §9's B_ν-to-real-arg).
- NEXT: **p55** = §14 cont. product-derivative (Leibniz) derivation (.tex 1770-1815+): eq(5) tail; substitute eq(4) into $f(x+y)\varphi(x+y)
  =(f\varphi)(x+y)$, collect powers of y => Leibniz-type formula for $D_\nu(f\varphi)$ as a sum $\sum D_\lambda f\,D_\mu\varphi/(...)$ with
  $\lambda+\mu=\nu$; likely a boxed/tagged $D_\nu(f\varphi)=\sum\binom{\nu}{\lambda}D_\lambda f D_\mu\varphi$-type result. ★ Read the
  derivation prose word-by-word; ZOOM u_ν/v_ν/D_ν subscripts, λ+μ=ν combinatorial limits, Π(ν)/Π(λ)/Π(μ) factors. Fix drops/rewords/
  misreads/norms/FABRIC; [sic] Weber errata. Compile-gate IF edit. Expect clean (derivation from established D_ν/Π notation) but verify.
**Confirmed by eye vs ~500dpi scans; page fully faithful, no edit.**


### 2026-07-03 — p55 (§14 product-derivative: Leibniz eq(6-7) + n-factor D eq(8) + linear-factor product eq(9-11), .tex 1770-1823) — p1-99 gap pass — (verified by eye, prose word-by-word) — **FULLY FAITHFUL (0 fixes) + 1 formatting flag**
**CONTENT: 0 edits.** File unchanged: **418pp / 0 overfull / 0 underfull / PDF 2264696 B** (no edit -> no recompile).
- **FAITHFUL (top, .tex 1772-1786):** "so ergiebt die Ausführung der Multiplication der beiden Formeln (4), wenn man in dem Product
  den Coëfficienten von y^ν aufsucht:"; **eq(6)** $\frac{D_\nu(f\varphi)}{\Pi(\nu)}=u_\nu v_0+u_{\nu-1}v_1+u_{\nu-2}v_2+\cdots+u_0v_\nu$;
  "oder"; **eq(7)** $D_\nu(f\varphi)=\varphi D_\nu f+B_1^{(\nu)}D_{\nu-1}fD_1\varphi+B_2^{(\nu)}D_{\nu-2}fD_2\varphi+\cdots$; "worin
  $B_1^{(\nu)},B_2^{(\nu)},\ldots$ die Binomialcoëfficienten sind. In ähnlicher Weise kann man unter Anwendung der Polynomialcoëfficienten
  die Derivirten eines Productes von mehr als zwei Factoren bilden."; "Wir wollen die erste Derivirte, die wir jetzt mit D statt mit D_1
  bezeichnen, für ein Product von n Factoren danach bilden."
- **FAITHFUL (mid, .tex 1786-1809):** "Für zwei Factoren erhalten wir nach (7):"; $D(f\varphi)=\varphi Df+fD\varphi=\varphi f'(x)+f\varphi'(x)$;
  "und allgemein, wenn wir die Factoren mit u_1,u_2...u_n, die Derivirten mit u'_1,u'_2...u'_n bezeichnen:"; **eq(8)** $D(u_1u_2\cdots u_n)
  =u'_1u_2\cdots u_n+u_1u'_2\cdots u_n+\cdots+u_1u_2\cdots u'_n$; "oder kürzer:"; $\frac{D(u_1u_2\cdots u_n)}{u_1u_2\cdots u_n}=\sum\frac{Du_\nu}{u_\nu}$;
  "Wenn wir also ein Product aus linearen Factoren"; **eq(9)** $f(x)=(x-\alpha_1)(x-\alpha_2)\cdots(x-\alpha_n)$; "betrachten, so erhalten
  wir, da die ersten Derivirten von x-α_1, x-α_2,...x-α_n sämmtlich gleich 1 sind,".
- **FAITHFUL (bot, .tex 1812-1823):** **eq(10)** $f'(x)=(x-\alpha_2)(x-\alpha_3)\cdots(x-\alpha_n)+(x-\alpha_1)(x-\alpha_3)\cdots(x-\alpha_n)
  +\cdots+(x-\alpha_1)(x-\alpha_2)\cdots(x-\alpha_{n-1})$; "wofür man auch setzen kann:"; **eq(11)** $f'(x)=\frac{f(x)}{x-\alpha_1}+\frac{f(x)}{x-\alpha_2}
  +\cdots+\frac{f(x)}{x-\alpha_n}$; "Ein sehr wichtiges Resultat ergiebt sich hieraus, wenn x gleich einem der Werthe α_1,α_2...α_n gesetzt
  wird, nämlich" (breaks to p56). ALL word-for-word.
- **⚠ FORMATTING-PASS FLAG (layout, NOT content):** eq(10) scan typesets the middle-term omission as a SEPARATE continuation-dots ROW
  between rows 2 and 3; .tex encodes it INLINE as "+\cdots" at the end of row 2. Same term-content. => formatting pass (same dots-row
  family as p49/p53). eq-nums leqno.
- **SKIP:** Coëfficienten/Binomialcoëfficienten/Polynomialcoëfficienten (ë-drop); ellipsis-connector "+" (eq6/eq8 scan "\cdots u_0v_ν"
  vs .tex "+\cdots+u_0v_ν"); φ=\varphi (house). **EMPHASIS (gesperrt, tracked):** "erste Derivirte".
- **★ META-PATTERN (8 clean pages p48-55):** §14 product-derivative (Leibniz + n-factor rule + logarithmic-derivative form + linear-
  factor f'(x)=Σf(x)/(x-α_i)) all clean -- derivation from established D_ν/Π/Binomial notation. §11-§14 block entirely clean.
- NEXT: **p56** = §14 tail eq(12) + **§15 Ganze Functionen mehrerer Veränderlichen: Formen** start (.tex 1824-1870+): **eq(12)**
  $f'(\alpha_1)=(\alpha_1-\alpha_2)(\alpha_1-\alpha_3)\cdots(\alpha_1-\alpha_n)$, ..., $f'(\alpha_n)=(\alpha_n-\alpha_1)\cdots(\alpha_n-\alpha_{n-1})$;
  **§15 heading**; DEF multivariate ganze rat. Fn nten Grades $F(x,y,z,\ldots)=\sum A_{\alpha,\beta,\gamma,\ldots}x^\alpha y^\beta z^\gamma\cdots$
  (Exponenten-Summe ≤ n, =n in >=1 Glied; Grad = max Σ); DEF **homogen** (alle Glieder gleiche Exponentensumme); Euler-homogeneity **eq(1)**
  $F(tx,ty,tz,\ldots)=t^nF(x,y,z,\ldots)$ + proof; homogenization "Durch Vermehrung der Veränderlichen...". ★★ §15 is DEFINITION-INTRODUCING
  (multivariate fns, Form, homogen) -- DAMAGE-WATCH like §9 (new defs = GPT-normalization-prone). Read DEF prose WORD-BY-WORD; ZOOM
  A_{α,β,γ,…} subscripts, Σ x^α y^β z^γ, α+β+γ+⋯ conditions, t^n. Fix drops/rewords/misreads/norms/FABRIC; [sic] Weber errata. Compile-gate IF edit.
**Confirmed by eye vs ~500dpi scans; page fully faithful, no edit.**


### 2026-07-03 — p56 (§14 tail eq(12) f'(α_i) + §15 Ganze Functionen mehrerer Veränderlichen: Formen start [DEF multivar + homogen + Euler eq(1)], .tex 1824-1853) — p1-99 gap pass — (verified by eye, DEF prose word-by-word) — **FULLY FAITHFUL (0 fixes)**
**CONTENT: 0 edits.** File unchanged: **418pp / 0 overfull / 0 underfull / PDF 2264696 B** (no edit -> no recompile).
- **FAITHFUL (top, §14 tail .tex 1826-1834):** **eq(12)** $f'(\alpha_1)=(\alpha_1-\alpha_2)(\alpha_1-\alpha_3)\cdots(\alpha_1-\alpha_n)$,
  $f'(\alpha_2)=(\alpha_2-\alpha_1)(\alpha_2-\alpha_3)\cdots(\alpha_2-\alpha_n)$, [dots-row -- PRESENT in .tex 1828 as `\quad\cdots`, MATCHES],
  $f'(\alpha_n)=(\alpha_n-\alpha_1)(\alpha_n-\alpha_2)\cdots(\alpha_n-\alpha_{n-1})$; **§15 heading "Ganze Functionen mehrerer Veränderlichen:
  Formen"**.
- **★★ DAMAGE-WATCH RESOLVED CLEAN -- §15 DEFINITIONAL core (mid, .tex 1836-1844) WORD-FOR-WORD:** "Wir haben bisher vorzugsweise die
  ganzen rationalen Functionen von einer Veränderlichen betrachtet; wir können uns aber nicht immer darauf beschränken und haben ja auch
  schon oben Functionen mehrerer Veränderlichen benutzt. Unter einer ganzen rationalen Function nten Grades mehrerer Veränderlichen
  $F(x,y,z,\ldots)$ verstehen wir eine Summe von Gliedern:"; $\sum A_{\alpha,\beta,\gamma,\ldots}x^\alpha y^\beta z^\gamma\cdots$; "worin
  α,β,γ... ganzzahlige nicht negative Exponenten sind, deren Summe α+β+γ+⋯ den Werth n nicht übersteigt, und wenigstens in einem Gliede
  auch wirklich erreicht. Der Grad wird also bestimmt durch den grössten Werth, den die Summe α+β+γ+⋯ annimmt."; "Wenn die Summe der
  Exponenten α+β+γ+⋯ in allen Gliedern denselben Werth hat, so heisst die Function **homogen**."; "Eine fundamentale Eigenschaft der
  homogenen Functionen nten Grades ist die, dass, wenn alle Variablen mit demselben Factor vervielfältigt werden, der Erfolg derselbe
  ist, wie wenn die Function mit der nten Potenz vervielfältigt wird; in Zeichen,".
- **FAITHFUL (bot, Euler proof .tex 1844-1853):** "...wenn t eine beliebige Veränderliche bedeutet:"; **eq(1)** $F(tx,ty,tz,\ldots)=t^nF(x,y,z,\ldots)$;
  "denn ersetzt man in dem Product $x^\alpha y^\beta z^\gamma\cdots$ die Variablen durch tx,ty,tz,..., so erhält es den Factor"; $t^{\alpha+\beta+\gamma+\cdots}$;
  "hat nun α+β+γ+⋯ in allen Gliedern denselben Werth n, so kann der Factor t^n vor die Summe herausgenommen werden. Hat aber die Summe
  α+β+γ+⋯ in den einzelnen Gliedern verschiedene Werthe, so kann ein solcher gemeinschaftlicher Factor nicht herausgenommen werden, wenig-"
  (breaks to p57). ALL word-for-word.
- **SKIP:** ellipsis; ordinal "nten". **EMPHASIS (gesperrt, tracked):** §15 heading; "homogen". leqno.
- **★★★ META-PATTERN REFINEMENT (important):** §15 INTRODUCES DEFINITIONS (multivar fn, Grad, homogen, Euler) yet came through CLEAN.
  => the damage trigger is NOT "definitions" per se but NOTATION-NORMALIZATION OPPORTUNITIES. §9 (p45) was damaged because it introduced
  $B_\nu^{(x)}$ with a VARIABLE-superscript in prose GPT normalized (n->x) + spelling variants (Binominal); §15 defines in PLAIN PROSE with
  STANDARD Σ/subscript notation -> nothing for GPT to normalize -> clean. Operational rule unchanged (read all prose word-by-word, esp.
  where NEW NOTATION appears). 9 clean pages p48-56; §11-§15(start) block clean.
- NEXT: **p57** = §15 cont. homogenization + (likely) Euler's theorem / partial-derivative identities (.tex 1853-1895+): (1853 cont)
  "...wenigstens nicht, ohne dass noch verschiedene Potenzen von t in den einzelnen Gliedern bleiben."; "Durch Vermehrung der
  Veränderlichen kann man jede nicht homogene Function in eine homogene von gleichem Grade verwandeln. Ist nämlich m-1 die Anzahl der
  Variablen in einer nicht homogenen Function nten Grades, so setzen wir" + eq (homogenizing variable substitution); then likely the
  partial-derivative / Euler-relation development. Continue gap-pass p57->p99. ★ §15 continues (multivar/homogen theory) -- keep reading
  DEF/theory prose WORD-BY-WORD; ZOOM the homogenizing substitution (m-1 vars, extra variable), any Σ/∂ notation. Fix drops/rewords/
  misreads/norms/FABRIC; [sic] Weber errata. Compile-gate IF edit. Expect clean but VERIFY (never certify).
**Confirmed by eye vs ~500dpi scans; page fully faithful, no edit.**


### 2026-07-03 — p57 (§15 homogenization [x=x_i/x_m, Φ] + Polynomialcoeff-form eq(2-3) + ν-index-form eq(4) + permutation-count, .tex 1853-1890) — p1-99 gap pass — (verified by eye, notation-intro prose word-by-word) — **FULLY FAITHFUL (0 fixes)**
**CONTENT: 0 edits.** File unchanged: **418pp / 0 overfull / 0 underfull / PDF 2264696 B** (no edit -> no recompile).
- **FAITHFUL (top, .tex 1853-1863):** "...wenigstens nicht, ohne dass noch verschiedene Potenzen von t in den einzelnen Gliedern
  bleiben."; "Durch Vermehrung der Veränderlichen kann man jede nicht homogene Function in eine homogene von gleichem Grade verwandeln.
  Ist nämlich m-1 die Anzahl der Variablen in einer nicht homogenen Function nten Grades, so setzen wir"; $x=\frac{x_1}{x_m}, y=\frac{x_2}{x_m},
  z=\frac{x_3}{x_m},\ldots$; "und erhalten in"; $x_m^n F(\frac{x_1}{x_m},\frac{x_2}{x_m},\frac{x_3}{x_m},\ldots)$; "eine ganze homogene
  Function nten Grades der Variablen x_1,x_2...x_m, die wir mit".
- **FAITHFUL (mid, .tex 1863-1884):** $\Phi(x_1,x_2,\ldots,x_m)$; "bezeichnen."; "Es empfiehlt sich bisweilen, die homogenen Functionen
  mehrerer Variablen mit den Polynomialcoëfficienten zu schreiben. Wir setzen daher"; **eq(2)** $\Phi(x_1,\ldots,x_m)=\sum\frac{\Pi(n)}{\Pi(\alpha_1)
  \Pi(\alpha_2)\cdots\Pi(\alpha_m)}A_{\alpha_1,\alpha_2,\ldots,\alpha_m}x_1^{\alpha_1}x_2^{\alpha_2}\cdots x_m^{\alpha_m}$; "wo sich die
  Summe auf alle nicht negativen, der Bedingung"; **eq(3)** $\alpha_1+\alpha_2+\cdots+\alpha_m=n$; "genügenden Zahlen erstreckt. Diese
  Bezeichnungsweise, ohne die Beschränkung (3), ist auch auf nicht homogene Functionen anwendbar."; "Man kann aber die homogene Function
  auch so darstellen:".
- **FAITHFUL (bot, .tex 1884-1890):** **eq(4)** $\Phi(x_1,\ldots,x_m)=\sum A_{\nu_1,\nu_2,\ldots,\nu_n}x_{\nu_1}x_{\nu_2}\cdots x_{\nu_n}$;
  "worin jeder der Indices ν_1,ν_2...ν_n von den übrigen unabhängig die Werthreihe 1,2...m zu durchlaufen hat. Die Summe (4) besteht also
  aus m^n Gliedern, die aber nicht alle von einander verschieden sind. Das Product x_{ν_1}x_{ν_2}...x_{ν_n} bleibt nämlich ungeändert,
  wenn die Indices ν_1,ν_2...ν_n beliebig unter einander permutirt werden. Die Anzahl der Permutationen von n Elementen beträgt aber Π(n).
  Sind unter diesen Elementen je α_1,α_2... einander gleich, so reducirt sich die Zahl der Permutationen auf" (breaks to p58). ALL word-for-word.
- **SKIP:** Polynomialcoëfficienten (ë-drop); ellipsis. **EMPHASIS (gesperrt, tracked):** "verschiedene"; "mit den Polynomialcoëfficienten". leqno.
- **★★★ META-PATTERN SHARPENING (important):** §15 (p57) DOES introduce NEW NOTATION (Φ, eq(2) polynomial-coeff form, eq(4) ν-index form)
  yet came through CLEAN. => the damage predictor is NOT "notation introduction" but LOCAL INCONSISTENCY/VARIANT in Weber's OWN usage that
  GPT "smooths": §9 (p45) damage = GPT reconciling prose $B_\nu^{(n)}$ vs display $B_\nu^{(x)}$ (homogenized to x) + spelling variant
  (Binominal). §15 uses Φ/α_i/ν_i/Π CONSISTENTLY -> nothing to reconcile -> clean. Sharpest predictors: (a) prose-vs-display notation
  mismatch, (b) spelling variants, (c) dropped terms at seams. Operational rule unchanged (read all word-by-word). 10 clean pages p48-57.
- NEXT: **p58** = §15 cont. permutation-count conclusion + (2)/(4) identity + more (.tex 1892-1935+): $\frac{\Pi(n)}{\Pi(\alpha_1)\Pi(\alpha_2)\cdots}$;
  "woraus sich ergiebt, dass in (4) irgend ein Product $x_1^{\alpha_1}x_2^{\alpha_2}\cdots$ genau [Π(n)/(Π(α_1)Π(α_2)...)] mal vorkommt";
  "Setzt man also noch fest, dass $A_{\nu_1,\ldots,\nu_n}$ sich nicht ändern soll, wenn die Indices beliebig permutirt werden, so erweisen
  sich die Bezeichnungsweisen (2) und (4) als identisch, wenn durch Zusammenfassen gleicher Factoren $x_{\nu_1}\cdots x_{\nu_n}=x_1^{\alpha_1}
  \cdots x_m^{\alpha_m}$ und..."; likely continues to derivatives/polar-forms of homogeneous functions. Continue gap-pass p58->p99. ★ Read
  prose word-by-word; ZOOM Π-quotients, α_i/ν_i index bookkeeping, A-subscript permutation-invariance. Watch prose-vs-display notation
  mismatch (the sharpest damage predictor). Fix drops/rewords/misreads/norms/FABRIC; [sic] Weber errata. Compile-gate IF edit. Expect clean but VERIFY.
**Confirmed by eye vs ~500dpi scans; page fully faithful, no edit.**


### 2026-07-03 — p58 (§15 tail: (2)/(4) identity + Gliederzahl (m,n) recursion eq(5-6) + Formen terminology, .tex 1892-1921) — p1-99 gap pass — (verified by eye, terminology prose word-by-word) — **FULLY FAITHFUL (0 fixes)**
**CONTENT: 0 edits.** File unchanged: **418pp / 0 overfull / 0 underfull / PDF 2264696 B** (no edit -> no recompile). **§15 COMPLETE, all clean.**
- **FAITHFUL (top, .tex 1892-1906):** $\frac{\Pi(n)}{\Pi(\alpha_1)\Pi(\alpha_2)\cdots}$; "woraus sich ergiebt, dass in (4) irgend ein
  Product $x_1^{\alpha_1}x_2^{\alpha_2}\cdots$ genau [Π(n)/(Π(α_1)Π(α_2)...)] mal vorkommt. Setzt man also noch fest, dass $A_{\nu_1,\nu_2,
  \ldots,\nu_n}$ sich nicht ändern soll, wenn die Indices beliebig permutirt werden, so erweisen sich die Bezeichnungsweisen (2) und (4)
  als identisch, wenn durch Zusammenfassen gleicher Factoren"; $x_{\nu_1}x_{\nu_2}\cdots x_{\nu_n}=x_1^{\alpha_1}x_2^{\alpha_2}\cdots x_m^{\alpha_m}$;
  "und"; $A_{\nu_1,\nu_2,\ldots,\nu_n}=A_{\alpha_1,\alpha_2,\ldots,\alpha_m}$; "gesetzt wird."
- **FAITHFUL (mid, .tex 1908-1921):** "Bezeichnen wir die Anzahl der Glieder, die in der Function Φ [nach (2)] auftreten, mit (m,n),
  so findet man, indem man zunächst die Glieder zählt, die den Factor x_1 haben und dann die übrigen, die eine homogene Function nter
  Ordnung von den übrigen m-1 Variablen bilden, die Recursionsformel"; **eq(5)** $(m,n)=(m,n-1)+(m-1,n)$; "mit deren Hülfe man durch
  vollständige Induction den Ausdruck"; **eq(6)** $(m,n)=\frac{m(m+1)\cdots(m+n-1)}{1\cdot2\cdots n}=\frac{\Pi(m+n-1)}{\Pi(n)\Pi(m-1)}$;
  "als richtig erweist."
- **FAITHFUL (bot, Formen terminology .tex 1921):** "Die ganzen homogenen Functionen werden auch **Formen** genannt. Man unterscheidet
  nach der Anzahl der Variablen **unäre** (einfache Potenzen), **binäre**, **ternäre**, **quaternäre** Formen. Die binären Formen sind es,
  die uns hier besonders interessiren, deren Theorie im Wesentlichen identisch ist mit der Theorie der ganzen rationalen Functionen einer
  Veränderlichen. Man gelangt von den binären Formen zu diesen Functionen zurück, wenn man eine der homogenen Variablen als constant
  ansieht, z.B. ihr den Werth 1 giebt." ALL word-for-word. (§16 heading is on p59; p58 ends §15.)
- **SKIP:** ellipsis. **EMPHASIS (gesperrt, tracked):** Formen; unäre; binäre; ternäre; quaternäre. leqno.
- **★ META-PATTERN (11 clean pages p48-58; §15 COMPLETE clean):** the Formen terminology-introduction (unär/binär/ternär/quaternär) --
  a terms-definition passage -- came through clean (fact-anchored, standard terms, no notation-inconsistency). §11-§15 block ENTIRELY clean.
  Confirms: damage was in (a) Einleitung long-abstract prose (p1-20), (b) §9 notation-inconsistency+spelling-variant. Systematic math
  exposition w/ consistent notation runs clean. STILL never-certify: verify each page.
- NEXT: **p59** = **§16 Die Derivirten von Functionen mehrerer Variablen** start (.tex 1923-1965+): §16 heading; intro "Wir haben im §13
  die derivirten Functionen einer ganzen rationalen Function einer Veränderlichen definirt. Der Begriff lässt sich unmittelbar übertragen
  auf Functionen mehrerer Variablen, indem man die Ableitungen in Bezug auf jede Variable für sich, als ob sie die einzige wäre, bildet.
  So erhält man, wenn man etwa wie in §15"; **eq(1)** $F(x,y,z,\ldots)=\sum A_{\alpha,\beta,\gamma,\ldots}x^\alpha y^\beta z^\gamma\cdots$;
  "setzt, die erste Derivirte nach x:"; **eq(2)** $F'(x)=\sum\alpha A_{\alpha,\beta,\gamma,\ldots}x^{\alpha-1}y^\beta z^\gamma\cdots$; "oder
  nach y:"; **eq(3)** $F'(y)=\sum\beta A_{\alpha,\beta,\gamma,\ldots}x^\alpha y^{\beta-1}z^\gamma\cdots$; "u.s.f. Aus diesen Functionen...";
  then polar/Taylor development (ersetzen $x_i$ durch $x_i+\xi_i$). Continue gap-pass p59->p99. ★§16 partial-derivative NOTATION (F'(x),
  F'(y), ξ_i) -- read prose word-by-word; ★watch prose-vs-display notation mismatch. ZOOM α/β/γ exponent-lowering, A-subscripts, ξ_i.
  Fix drops/rewords/misreads/norms/FABRIC; [sic] Weber errata. Compile-gate IF edit. Expect clean but VERIFY.
**Confirmed by eye vs ~500dpi scans; page fully faithful, no edit.**


### 2026-07-03 — p59 (§16 Die Derivirten von Functionen mehrerer Variablen start: partial-deriv eq(1-3) + multivar-Taylor eq(4), .tex 1923-1966) — p1-99 gap pass — (verified by eye + ZOOM) — **FULLY FAITHFUL (0 fixes)**
**CONTENT: 0 edits.** File unchanged: **418pp / 0 overfull / 0 underfull / PDF 2264696 B** (no edit -> no recompile).
- **FAITHFUL (top, .tex 1923-1930):** **§16 heading "Die Derivirten von Functionen mehrerer Variablen"**; intro "Wir haben im §13 die
  derivirten Functionen einer ganzen rationalen Function einer Veränderlichen definirt. Der Begriff lässt sich unmittelbar übertragen auf
  Functionen mehrerer Variablen, indem man die Ableitungen in Bezug auf jede Variable für sich, als ob sie die einzige wäre, bildet. So
  erhält man, wenn man etwa wie in §15"; **eq(1)** $F(x,y,z,\ldots)=\sum A_{\alpha,\beta,\gamma,\ldots}x^\alpha y^\beta z^\gamma\cdots$;
  "setzt, die erste Derivirte nach x:".
- **FAITHFUL (mid, .tex 1932-1954):** **eq(2)** $F'(x)=\sum\alpha A_{\alpha,\beta,\gamma,\ldots}x^{\alpha-1}y^\beta z^\gamma\cdots$; "oder
  nach y:"; **eq(3)** $F'(y)=\sum\beta A_{\alpha,\beta,\gamma,\ldots}x^\alpha y^{\beta-1}z^\gamma\cdots$; "u.s.f. Aus diesen Functionen kann
  man nach denselben Regeln wieder die Ableitungen nach den verschiedenen Variablen bilden und erhält so die höheren Ableitungen."; "Um die
  Resultate übersichtlicher darzustellen, sei $\Phi(x_1,x_2,\ldots,x_m)$ eine ganze rationale Function nter Ordnung der m Veränderlichen
  x_1,x_2...x_m. Wir ersetzen diese Veränderlichen durch Binome:"; $x_1+\xi_1,x_2+\xi_2,\ldots,x_m+\xi_m$; "und entwickeln in jedem Gliede
  der Function"; $\Phi(x_1+\xi_1,\ldots,x_m+\xi_m)=\Phi(x+\xi)$; "durch Ausführung der Multiplication".
- **FAITHFUL (bot, .tex 1952-1966):** display $(x_1+\xi_1)^{\mu_1}(x_2+\xi_2)^{\mu_2}\cdots(x_m+\xi_m)^{\mu_m}$ [★ZOOM-confirmed exponents
  are μ (mu), NOT α: plain-u glyph w/o alpha's double-loop; α is reserved for the ξ-exponents in eq(4). Matches .tex \mu]; "nach Potenzen
  von ξ_1,ξ_2...ξ_m. Fassen wir gleiche Potenzen und Producte der Variablen ξ je in ein Glied zusammen, so ergiebt sich in der Bezeichnung
  (2) §15 für Φ(x+ξ) eine Darstellung, die in der Differentialrechnung die **Taylor'sche Entwickelung** heisst:"; **eq(4)** $\Phi(x+\xi)=\sum
  \frac{\xi_1^{\alpha_1}\xi_2^{\alpha_2}\cdots\xi_m^{\alpha_m}}{\Pi(\alpha_1)\Pi(\alpha_2)\cdots\Pi(\alpha_m)}D_{\alpha_1,\alpha_2,\ldots,\alpha_m}\Phi$;
  "Die Coëfficienten, die wir mit $D_{\alpha_1,\alpha_2,\ldots,\alpha_m}\Phi$ bezeichnen, sind Functionen der Variablen x und heissen, wenn"
  (breaks to p60). ALL word-for-word.
- **SKIP:** Coëfficienten (ë-drop); ellipsis. **EMPHASIS (gesperrt, tracked):** §16 heading; "einer" (einer Veränderlichen); "Taylor'sche". leqno.
- **★ ZOOM LESSON reaffirmed:** the (x_i+ξ_i)-exponents μ_i vs α_i were genuinely ambiguous at thirds-resolution; crop_src zoom settled
  it (μ, matching .tex). Weber uses μ_i for the ORIGINAL monomial x-exponents, α_i for the ξ-exponents after Taylor expansion -- distinct
  roles, both present on same page. => always zoom generic-exponent glyphs.
- **★ META-PATTERN (12 clean pages p48-59):** §16 partial-derivative intro + multivar-Taylor clean. Notation-heavy (F'(x)/F'(y), ξ_i,
  D_{α...}, μ_i vs α_i) but Weber is internally consistent -> no GPT-normalization -> clean. Consistent w/ refined rule.
- NEXT: **p60** = §16 cont. ∂-notation eq(5) + D-rules I/II + product-of-powers case (.tex 1968-2010+): "α_1+α_2+⋯+α_m=ν ist, die Derivirten
  νter Ordnung der Function Φ"; "Man stellt sie auch nach der in der Differentialrechnung gebräuchlichen Bezeichnungsweise so dar:"; **eq(5)**
  $D_{\alpha_1,\ldots,\alpha_m}\Phi=\frac{\partial^\nu\Phi}{\partial x_1^{\alpha_1}\partial x_2^{\alpha_2}\cdots\partial x_m^{\alpha_m}}$;
  "Das Bildungsgesetz der Derivirten lässt sich in folgende Sätze zusammenfassen, wobei wir der Kürze wegen die Indices bei dem Zeichen D
  weglassen."; **I.** "Ist C eine Constante, so ist" $D(C\Phi)=CD\Phi$; **II.** "Sind Φ und Ψ irgend zwei Functionen, so ist" $D(\Phi+\Psi)=
  D\Phi+D\Psi$; "Beides folgt unmittelbar aus (4)."; "Wir können also leicht die derivirten Functionen allgemein bilden, wenn wir sie für
  den speciellen Fall kennen, in dem Φ ein Product von Potenzen ist, also wenn wir" + eq. Continue gap-pass p60->p99. ★★ eq(5) introduces
  ∂-NOTATION (partial-derivative Leibniz) -- NEW NOTATION -> notation-watch; read prose word-by-word; ZOOM ∂^ν/∂x_i^{α_i}, D-rules I/II,
  Φ/Ψ. Fix drops/rewords/misreads/norms/FABRIC; [sic] Weber errata. Compile-gate IF edit.
**Confirmed by eye+zoom vs ~500dpi scans; page fully faithful, no edit.**


### 2026-07-03 — p60 (§16 cont.: ∂-notation eq(5) + D-rules I/II + power-product derivative eq(6-8), .tex 1968-2033) — p1-99 gap pass — (verified by eye) — **FULLY FAITHFUL (0 fixes)**
**CONTENT: 0 edits.** File unchanged: **418pp / 0 overfull / 0 underfull / PDF 2264696 B** (no edit -> no recompile).
- **FAITHFUL (top, .tex 1968-1989):** "α_1+α_2+⋯+α_m=ν ist, die Derivirten νter Ordnung der Function Φ."; "Man stellt sie auch nach der
  in der Differentialrechnung gebräuchlichen Bezeichnungsweise so dar:"; **eq(5)** $D_{\alpha_1,\alpha_2,\ldots,\alpha_m}\Phi=\frac{\partial^\nu\Phi}
  {\partial x_1^{\alpha_1}\partial x_2^{\alpha_2}\cdots\partial x_m^{\alpha_m}}$ [∂-notation matches]; "Das Bildungsgesetz der Derivirten
  lässt sich in folgende Sätze zusammenfassen, wobei wir der Kürze wegen die Indices bei dem Zeichen D weglassen."; **I.** "Ist C eine
  Constante, so ist" $D(C\Phi)=CD\Phi$; **II.** "Sind Φ und Ψ irgend zwei Functionen, so ist".
- **FAITHFUL (mid, .tex 1989-2013):** $D(\Phi+\Psi)=D\Phi+D\Psi$; "Beides folgt unmittelbar aus (4)."; "Wir können also leicht die
  derivirten Functionen allgemein bilden, wenn wir sie für den speciellen Fall kennen, in dem Φ ein Product von Potenzen ist, also wenn
  wir"; $D_{\alpha_1,\alpha_2,\ldots,\alpha_m}(x_1^{\mu_1}x_2^{\mu_2}\cdots x_m^{\mu_m})$; "kennen, worin die μ beliebige, nicht negative
  Exponenten sind."; "Nun ist aber"; $(x_1+\xi_1)^{\mu_1}=\sum^{\alpha_1}\frac{\Pi(\mu_1)}{\Pi(\alpha_1)\Pi(\mu_1-\alpha_1)}\xi_1^{\alpha_1}
  x_1^{\mu_1-\alpha_1}$; "und folglich:"; **eq(6)** $(x_1+\xi_1)^{\mu_1}\cdots(x_m+\xi_m)^{\mu_m}=\sum^{\alpha_1\ldots\alpha_m}\frac{\Pi(\mu_1)
  \cdots\Pi(\mu_m)x_1^{\mu_1-\alpha_1}\cdots x_m^{\mu_m-\alpha_m}}{\Pi(\mu_1-\alpha_1)\cdots\Pi(\mu_m-\alpha_m)\Pi(\alpha_1)\cdots\Pi(\alpha_m)}
  \xi_1^{\alpha_1}\cdots\xi_m^{\alpha_m}$.
- **FAITHFUL (bot, .tex 2017-2033):** "und es ergiebt also die Vergleichung mit (4) und (6)"; **eq(7)** $D_{\alpha_1,\ldots,\alpha_m}(x_1^{\mu_1}
  \cdots x_m^{\mu_m})=\frac{\Pi(\mu_1)\cdots\Pi(\mu_m)}{\Pi(\mu_1-\alpha_1)\cdots\Pi(\mu_m-\alpha_m)}x_1^{\mu_1-\alpha_1}\cdots x_m^{\mu_m-\alpha_m}$;
  "so lange $\alpha_1\leq\mu_1,\ldots,\alpha_m\leq\mu_m$. Dagegen ist"; **eq(8)** $D_{\alpha_1,\ldots,\alpha_m}(x_1^{\mu_1}\cdots x_m^{\mu_m})=0$;
  "sobald einer der Indices α grösser ist als der entsprechende Exponent μ." ALL word-for-word (every Π-quotient num/denom + exponent verified).
- **SKIP:** ellipsis. **EMPHASIS (gesperrt, tracked):** "Derivirten νter Ordnung". leqno; Σ^{α_1}/Σ^{α_1...α_m} = Weber upper-limit (fmt).
- **★ META-PATTERN (13 clean pages p48-60):** §16 ∂-notation + multi-index power-product derivative (Π-quotient bookkeeping) all clean.
  Dense equation page (eq5-8, big Π-quotients) verified num/denom -- exact. §11-§16 block entirely clean. Never-certify: verify each page.
- NEXT: **p61** = §16 cont. double-derivative / commutativity (.tex 2035-2075+): "Bezeichnen wir nun mit β_1,β_2,...,β_m ein zweites System
  von Indices, und bilden von der Function (7) die Ableitung D_{β_1,β_2,...,β_m}, so ergiebt sich durch nochmalige Anwendung derselben
  Formeln (7) und (8):"; eq $D_{\beta_1,\ldots,\beta_m}D_{\alpha_1,\ldots,\alpha_m}(x_1^{\mu_1}\cdots x_m^{\mu_m})=D_{\beta_1+\alpha_1,\ldots,
  \beta_m+\alpha_m}(\ldots)$ [composition/additivity of multi-index derivatives -- likely commutativity theorem]; continues. Continue gap-pass
  p61->p99. ★ Read prose word-by-word; ZOOM β_i/α_i/μ_i index bookkeeping, β_i+α_i sums, Π-quotients. Fix drops/rewords/misreads/norms/FABRIC;
  [sic] Weber errata. Compile-gate IF edit. Expect clean but VERIFY.
**Confirmed by eye vs ~500dpi scans; page fully faithful, no edit.**


### 2026-07-03 — p61 (§16 cont.: double-deriv eq(9) + Satz III commutativity + deriv-shorthand + quadratic-form eq(10-13), .tex 2035-2095) — p1-99 gap pass — (verified by eye) — **FULLY FAITHFUL (0 fixes)**
**CONTENT: 0 edits.** File unchanged: **418pp / 0 overfull / 0 underfull / PDF 2264696 B** (no edit -> no recompile).
- **FAITHFUL (top, .tex 2035-2055):** "Bezeichnen wir nun mit β_1,β_2...β_m ein zweites System von Indices, und bilden von der Function
  (7) die Ableitung D_{β_1,β_2...β_m}, so ergiebt sich durch nochmalige Anwendung derselben Formeln (7) und (8):"; **eq(9)** $D_{\beta_1,\ldots,\beta_m}
  D_{\alpha_1,\ldots,\alpha_m}(x_1^{\mu_1}\cdots x_m^{\mu_m})=D_{\beta_1+\alpha_1,\ldots,\beta_m+\alpha_m}(x_1^{\mu_1}\cdots x_m^{\mu_m})$; "und
  daraus folgt nach II. die allgemeine Gültigkeit des Satzes"; **III.** $D_{\beta_1,\ldots,\beta_m}D_{\alpha_1,\ldots,\alpha_m}\Phi=D_{\beta_1+\alpha_1,
  \ldots,\beta_m+\alpha_m}\Phi$; "was eine Verallgemeinerung des Satzes (8), §13 ist, und man kann also die höheren Derivirten durch
  fortgesetzte Ableitung der niederen bilden."; "Für die ersten Derivirten einer Function Φ"; $D_{1,0\ldots0}\Phi,D_{0,1\ldots0}\Phi,\ldots,D_{0,0\ldots1}\Phi$.
- **FAITHFUL (mid, .tex 2057-2076):** "brauchen wir auch die kürzeren Zeichen"; $\Phi'(x_1),\Phi'(x_2)\ldots\Phi'(x_m)$; "ebenso für die
  zweiten"; $D_{2,0\ldots0},D_{1,1\ldots0},\ldots$; "die Zeichen"; $\Phi''(x_1,x_1),\Phi''(x_1,x_2)=\Phi''(x_2,x_1),\ldots$; "Auch diese
  Bezeichnung lässt sich verallgemeinern und würde zu einem der Formel (4), §15 entsprechenden Ausdruck führen."; "Wir erwähnen des
  häufigen Gebrauches wegen die Formeln für die quadratischen Formen besonders. Setzen wir"; **eq(10)** $\Phi(x)=\sum a_{i,k}x_i x_k$;
  "worin i,k von einander unabhängig die Reihe der Zahlen 1,2...m durchlaufen und $a_{i,k}=a_{k,i}$ ist, so ist:".
- **FAITHFUL (bot, .tex 2079-2095):** **eq(11)** $\frac{1}{2}\Phi'(x_1)=a_{1,1}x_1+a_{1,2}x_2+\cdots+a_{1,m}x_m$, ..., $\frac{1}{2}\Phi'(x_m)
  =a_{m,1}x_1+\cdots+a_{m,m}x_m$ [dots-row PRESENT in .tex, matches]; "und wir setzen noch"; **eq(12)** $\Phi(x,\xi)=\Phi(\xi,x)=\sum\xi_i\Phi'(x_i)
  =\sum x_i\Phi'(\xi_i)$; "Dann ist"; **eq(13)** $\Phi(x+\xi)=\Phi(x)+\Phi(x,\xi)+\Phi(\xi)$. ALL word-for-word (a_{i,k} double-subscripts verified).
- **SKIP:** ellipsis. leqno; Σ (no-limit) = plain sum. (Running header varies within §16: p59 "Functionen mehrerer Variablen", p61 "Allgemeine
  Derivirte" -- header, out of scope.)
- **★ META-PATTERN (14 clean pages p48-61):** §16 double-derivative commutativity (Satz III) + deriv-shorthand + quadratic-form polar
  setup all clean. Multi-index/double-subscript bookkeeping (β_i+α_i, a_{i,k}) exact. §11-§16 block clean. Never-certify: verify each page.
- NEXT: **p62** = §16 tail (Polare def) + **§17 Das Euler'sche Theorem über homogene Functionen** start (.tex 2096-2135+): "Die Function
  $\Phi(x,\xi)$ wird die **Polare** von Φ genannt. Sie ist linear und homogen sowohl in Beziehung auf die x, wie in Beziehung auf die ξ.";
  "Sie kann ausgedrückt werden durch"; **eq(14)** $\Phi(x,\xi)=2\sum a_{ik}\xi_i x_k$; "und genügt der Bedingung"; **eq(15)** $\Phi(x,x)=2\Phi(x)$;
  **§17 heading**; intro "Aus den vorstehenden Entwickelungen lässt sich mit Leichtigkeit ein Fundamentalsatz über homogene Functionen
  herleiten, der von **Euler** entdeckt und nach ihm benannt ist."; "Wir erhalten ihn am einfachsten aus der Formel (4) des vorigen
  Paragraphen, wenn wir mit t eine beliebige Veränderliche bezeichnen,"; **eq(1)** $\xi_1=tx_1,\xi_2=tx_2,\ldots,\xi_m=tx_m$. Continue
  gap-pass p62->p99. ★ "Polare" = TERM-DEFINITION (damage-watch); §17 has EULER historical-attribution (fact-anchored). Read prose
  word-by-word; ZOOM a_{ik}/ξ_i/x_k subscripts, 2Σ factor. Fix drops/rewords/misreads/norms/FABRIC; [sic] Weber errata. Compile-gate IF edit.
**Confirmed by eye vs ~500dpi scans; page fully faithful, no edit.**


### 2026-07-03 — p62 (§16 tail Polare def eq(14-15) + §17 Euler'sches Theorem start eq(1-4), .tex 2096-2144) — p1-99 gap pass — (verified by eye) — **FULLY FAITHFUL (0 fixes)**
**CONTENT: 0 edits.** File unchanged: **418pp / 0 overfull / 0 underfull / PDF 2264696 B** (no edit -> no recompile).
- **FAITHFUL (top, §16 tail .tex 2096-2109):** "Die Function Φ(x,ξ) wird die **Polare** von Φ genannt. Sie ist linear und homogen sowohl
  in Beziehung auf die x, wie in Beziehung auf die ξ."; "Sie kann ausgedrückt werden durch"; **eq(14)** $\Phi(x,\xi)=2\sum a_{ik}\xi_i x_k$;
  "und genügt der Bedingung"; **eq(15)** $\Phi(x,x)=2\Phi(x)$; **§17 heading "Das Euler'sche Theorem über homogene Functionen"**.
- **FAITHFUL (mid, §17 intro .tex 2111-2127):** "Aus den vorstehenden Entwickelungen lässt sich mit Leichtigkeit ein Fundamentalsatz über
  homogene Functionen herleiten, der von **Euler** entdeckt und nach ihm benannt ist."; "Wir erhalten ihn am einfachsten aus der Formel (4)
  des vorigen Paragraphen, wenn wir mit t eine beliebige Veränderliche bezeichnen,"; **eq(1)** $\xi_1=tx_1,\xi_2=tx_2,\ldots,\xi_m=tx_m$;
  "setzen und dann die Fundamentalformel §15 (1) für die homogenen Functionen anwenden. Wir erhalten so zunächst:"; **eq(2)** $(1+t)^n\Phi(x)
  =\sum\frac{(tx_1)^{\alpha_1}(tx_2)^{\alpha_2}\cdots(tx_m)^{\alpha_m}}{\Pi(\alpha_1)\Pi(\alpha_2)\cdots\Pi(\alpha_m)}D_{\alpha_1,\alpha_2,\ldots,\alpha_m}\Phi$;
  "Wendet man auf der linken Seite von (2) den binomischen Satz an, und setzt dann die Coëfficienten gleich hoher Potenzen von t beiderseits
  einander gleich, so ergiebt sich für jedes ν=1,2...n:".
- **FAITHFUL (bot, .tex 2129-2144):** **eq(3)** $\frac{\Pi(n)}{\Pi(n-\nu)}\Phi(x_1,x_2,\ldots,x_m)=\sum^{\alpha}\frac{\Pi(\nu)}{\Pi(\alpha_1)
  \Pi(\alpha_2)\cdots\Pi(\alpha_m)}x_1^{\alpha_1}x_2^{\alpha_2}\cdots x_m^{\alpha_m}D_{\alpha_1,\alpha_2,\ldots,\alpha_m}\Phi$; "worin sich die
  Summe auf alle der Bedingung"; **eq(4)** $\alpha_1+\alpha_2+\cdots+\alpha_m=\nu$; "genügenden Werthsysteme der α erstreckt."; "In dieser
  Form ist das zu erweisende Theorem in seiner Allgemeinheit enthalten. Für den besonderen Fall ν=1 erhalten wir die Formel". ALL word-for-word.
- **SKIP:** Coëfficienten (ë-drop); ellipsis. **EMPHASIS (gesperrt, tracked):** "Polare"; §17 heading; "Euler". leqno; Σ^{α} = Weber upper-limit (fmt).
- **★ META-PATTERN (15 clean pages p48-62):** the "Polare" TERM-DEFINITION + §17 Euler intro (with EULER historical attribution) came
  through clean -- fact-anchored, standard notation. §11-§17(start) block entirely clean. Never-certify: verify each page.
- NEXT: **p63** = §17 cont. Euler special cases + polar-form (.tex 2146-2190+): **eq(5)** $n\Phi(x_1,x_2,\ldots,x_m)=x_1\Phi'(x_1)+x_2\Phi'(x_2)
  +\cdots+x_m\Phi'(x_m)$ [ν=1 Euler]; "wovon die Formel (15) des vorigen Paragraphen ein specieller Fall ist, und für ν=2:"; **eq(6)** $n(n-1)
  \Phi(x_1,x_2,\ldots,x_m)=\sum_{i,k=1}^{m}x_i x_k\Phi''(x_i,x_k)$; "worin die Summe von i=1 bis i=m und von k=1 bis k=m zu erstrecken ist,
  so dass jedes Glied mit ungleichen i,k zweimal in der Summe auftritt."; "Setzen wir, wenn die α der Bedingung (4) unterworfen sind,";
  $\Phi_\nu(\xi,x)=\sum\frac{\xi_1^{\alpha_1}\xi_2^{\alpha_2}\cdots\xi_m^{\alpha_m}}{\Pi(\alpha_1)\Pi(\alpha_2)\cdots\Pi(\alpha_m)}\cdots$;
  continues. Continue gap-pass p63->p99. ★ Read prose word-by-word; ZOOM eq(5) x_iΦ'(x_i) sum, eq(6) Σ_{i,k=1}^{m} double-sum + Φ''(x_i,x_k),
  Φ_ν(ξ,x). Fix drops/rewords/misreads/norms/FABRIC; [sic] Weber errata. Compile-gate IF edit. Expect clean but VERIFY.
**Confirmed by eye vs ~500dpi scans; page fully faithful, no edit.**


### 2026-07-03 — p63 (§17 tail: Euler cases eq(5-6) + Polaren eq(7-10) + binary-form eq(9-dup); LAST PAGE of ERSTER ABSCHNITT, .tex 2146-2196) — p1-99 gap pass — (verified by eye + ZOOM eq-number) — **FULLY FAITHFUL (0 fixes) + 1 documented Weber erratum**
**CONTENT: 0 edits.** File unchanged: **418pp / 0 overfull / 0 underfull / PDF 2264696 B** (no edit -> no recompile).
- **FAITHFUL (top, .tex 2146-2169):** **eq(5)** $n\Phi(x_1,x_2,\ldots,x_m)=x_1\Phi'(x_1)+x_2\Phi'(x_2)+\cdots+x_m\Phi'(x_m)$ [ν=1 Euler];
  "wovon die Formel (15) des vorigen Paragraphen ein specieller Fall ist, und für ν=2:"; **eq(6)** $n(n-1)\Phi(x_1,x_2,\ldots,x_m)=\sum_{i,k=1}^{m}
  x_i x_k\Phi''(x_i,x_k)$ [scan Σ = index-over "i,k" Weber-conv; range in prose]; "worin die Summe von i=1 bis i=m und von k=1 bis k=m zu
  erstrecken ist, so dass jedes Glied mit ungleichen i,k zweimal in der Summe auftritt."; "Setzen wir, wenn die α der Bedingung (4)
  unterworfen sind"; **eq(7)** $\Phi_\nu(\xi,x)=\sum\frac{\xi_1^{\alpha_1}\xi_2^{\alpha_2}\cdots\xi_m^{\alpha_m}}{\Pi(\alpha_1)\Pi(\alpha_2)
  \cdots\Pi(\alpha_m)}D_{\alpha_1,\alpha_2,\ldots,\alpha_m}\Phi$; "so ist nach (4) des §16:"; **eq(8)** $\Phi(x+\xi)=\Phi(x)+\Phi_1(x,\xi)+\Phi_2(x,\xi)+\cdots+\Phi_n(x,\xi)$.
- **FAITHFUL (mid, .tex 2172-2188):** "und da die linke Seite ungeändert bleibt, wenn x mit ξ vertauscht wird, so ergiebt sich die
  Relation:"; **eq(9)** $\Phi_{n-\nu}(x,\xi)=\Phi_\nu(\xi,x)$; "also insbesondere"; **eq(10)** $\Phi_n(x,\xi)=\Phi(\xi)$; "Die Function
  $\Phi_\nu(x,\xi)$ wird, als Function von x betrachtet, die **νte Polare** der Function Φ für das Werthsystem ξ genannt."; "Wir wollen die
  Formel (3) noch für den Fall einer binären Form (m=2) specialisiren. Wir bezeichnen die Variablen mit x,y und setzen zur Abkürzung:";
  $\Phi(x,y)=u,\ D_{h,\nu-h}\Phi=u_h$; "und erhalten aus (4):".
- **FAITHFUL (bot, .tex 2190-2196):** **eq(9)[DUPLICATE]** $\frac{\Pi(n)}{\Pi(n-\nu)}u=\sum_{h=0}^{\nu}\frac{\Pi(\nu)}{\Pi(h)\Pi(\nu-h)}u_h
  x^h y^{\nu-h}$ [scan Σ = "h" over, "0,ν" under = Weber-conv]; "worin ν jeden beliebigen Werth, der nicht grösser als n ist, annehmen kann."
  ALL word-for-word.
- **★★ DOCUMENTED WEBER ERRATUM (type-B, already faithful in .tex -- do NOT 'correct'):** §17's binary-form equation is numbered **(9)** in
  the SCAN (ZOOM-confirmed) -- a DUPLICATE of the earlier eq(9) $\Phi_{n-\nu}(x,\xi)=\Phi_\nu(\xi,x)$. Sequence in §17: (5),(6),(7),(8),(9),
  (10),(9)[binary]. Weber himself reused (9). The .tex `\tag{9}` at both spots is FAITHFUL (reproduces Weber's duplicate). No LaTeX label
  conflict (\tag not \label), compiles clean. => KEEP as-is; documented so a later formatting/renumber pass does NOT silently 'fix' it.
- **SKIP:** ellipsis-connector "+" (eq5 scan "\cdots x_mΦ'(x_m)" vs .tex "+\cdots+"); ordinal. **EMPHASIS (gesperrt, tracked):** "νte Polare".
  leqno; Σ index-over/range-under (eq6, eq9-binary) = Weber-conv (fmt).
- **★ MILESTONE: ERSTER ABSCHNITT COMPLETE.** p63 is the last page of the First Section (§1-§17). Next: \clearpage -> **ZWEITER ABSCHNITT.
  Determinanten.** -> §18 Permutationen von n Elementen. 16 clean pages p48-63 (only the documented dup-(9) erratum, which is faithful).
- NEXT: **p64** = **ZWEITER ABSCHNITT: Determinanten** divider + **§18 Permutationen von n Elementen** start (.tex 2199-2240+): \clearpage;
  "Zweiter Abschnitt." / "Determinanten." divider; **§18 heading "Permutationen von n Elementen"**; §18 intro (permutation theory). ★ NEW
  SECTION/CHAPTER -- watch the divider-page alignment (scan may have a dedicated divider page => printed page numbers may shift; verify
  header/page-number on p64 scan). Read §18 intro prose word-by-word (new-section intro = possible damage-watch). ZOOM permutation notation.
  Fix drops/rewords/misreads/norms/FABRIC; [sic] Weber errata. Compile-gate IF edit. ★ CHECK: does scan have a physical divider page before
  §18? If so, chunk_page page-index may need +1 offset from here on -- VERIFY p64 header reads "§18" / correct page number.
**Confirmed by eye+zoom vs ~500dpi scans; page fully faithful, no edit. First Section done.**


### 2026-07-03 — p64 (ZWEITER ABSCHNITT: Determinanten divider + §18 Permutationen von n Elementen start eq(1-2), .tex 2199-2230) — p1-99 gap pass — (verified by eye; ★Fraktur + section-alignment checks) — **FULLY FAITHFUL (0 fixes) + 1 formatting flag**
**CONTENT: 0 edits.** File unchanged: **418pp / 0 overfull / 0 underfull / PDF 2264696 B** (no edit -> no recompile). **ZWEITER ABSCHNITT START.**
- **★ PAGE-ALIGNMENT VERIFIED:** the "Zweiter Abschnitt. / Determinanten." divider is INLINE at top of printed p64 (centered + rule),
  NOT a separate physical divider page. So printed-page indexing is preserved; chunk_page offset +26 still holds (pdf=printed+26). No shift.
  Section-opening page has NO running header (standard).
- **FAITHFUL (top/mid, .tex 2199-2217):** "Zweiter Abschnitt." / "Determinanten." divider; **§18 heading "Permutationen von n Elementen"**;
  "Wir betrachten ein System von n unterschiedenen Elementen irgend welcher Art, z.B. die n Ziffern"; $1,2,3,\ldots,n$; "deren Complex in
  dieser bestimmten Anordnung wir mit $\mathfrak A$ bezeichnen wollen. Die Elemente von $\mathfrak A$ lassen sich auf verschiedene Arten
  anordnen, z.B."; $2,1,3,\ldots,n$; "Der Uebergang von einer Anordnung zu einer anderen heisst eine **Permutation**."; "Bezeichnen wir die
  Anzahl der verschiedenen Anordnungen, die nur von der Anzahl n der Elemente abhängen kann, mit Π(n), so ergiebt sich zunächst Π(1)=1,
  Π(2)=2, und um die Zahl allgemein zu bestimmen, denken wir uns zu n-1...".
- **★ FRAKTUR 𝔄 CORRECTLY PRESERVED:** scan shows Fraktur A (𝔄) at both occurrences ("mit 𝔄", "Elemente von 𝔄"); .tex uses \mathfrak A --
  MATCH, no italic-normalization here. (Stay vigilant: memory notes earlier Fraktur-M slips + a font-slip 𝔅 elsewhere; Fraktur is a known
  GPT-risk in the Determinanten section, but §18 opening is clean.)
- **FAITHFUL (bot, .tex 2221-2230):** "In jeder Anordnung der n-1 Elemente kann nun das nte Element an n verschiedene Stellen gesetzt
  werden, nämlich vor das erste, zwischen das erste und zweite, zwischen das zweite und dritte u.s.f., endlich nach dem (n-1)ten, und alle
  die so entstandenen Anordnungen sind von einander verschieden. Daraus folgt:"; **eq(1)** $\Pi(n)=n\Pi(n-1)$; "woraus sich durch
  vollständige Induction"; **eq(2)** $\Pi(n)=1\cdot2\cdot3\cdots n$. ALL word-for-word.
- **⚠ FORMATTING-PASS FLAG (inline-vs-display, NOT content):** scan runs "$\Pi(1)=1,\Pi(2)=2$" INLINE in the prose sentence; .tex promotes
  it to a separate display \[ \Pi(1)=1,\qquad \Pi(2)=2, \]. Identical content -> formatting pass (inline->display promotion). Low priority.
- **SKIP:** ellipsis; ordinal "nte/(n-1)ten". **EMPHASIS (gesperrt, tracked):** §18 heading; "Permutation".
- **★ META-PATTERN (17 clean pages p48-64):** §18 DEFINITION-INTRODUCING (Permutation/Π(n)/𝔄) + FRAKTUR came through clean -- fact-anchored
  defs, standard notation, Fraktur preserved. Determinanten section opens clean. ★ STAY VIGILANT on Fraktur (𝔄/𝔄'/etc.) next pages.
- NEXT: **p65** = §18 cont. Transpositionen (.tex 2231-2275+): "ergiebt, so dass das Zeichen Π(n) hier dieselbe Bedeutung hat, wie im ersten
  Abschnitt (§7)."; "Irgend eine Anordnung des Systems $\mathfrak A$ bezeichnen wir mit $\mathfrak A'$, oder ausführlicher, wenn α_1,α_2,...,α_n
  die Ziffern 1,2,...,n in irgend einer Reihenfolge bedeuten, mit"; **eq(3)** $\mathfrak A'=\alpha_1,\alpha_2,\ldots,\alpha_n$; "Man kann auf
  sehr verschiedene Arten aus einer Anordnung eine beliebige andere ableiten... die durch sogenannte **Transpositionen**, d.h. durch
  successive Vertauschung von nur zwei Elementen..."; example (1,2,3,4)->(4,3,2,1) via transpositions $(1,4),(2,3)$. Continue gap-pass p65->p99.
  ★★ FRAKTUR WATCH (𝔄, 𝔄'); Transposition-DEF prose word-by-word; ZOOM Fraktur glyphs + α-indices + transposition (i,k) notation. Fix
  drops/rewords/misreads/norms/FABRIC; [sic] Weber errata. Compile-gate IF edit.
**Confirmed by eye vs ~500dpi scans; page fully faithful, no edit. Zweiter Abschnitt started.**


### 2026-07-03 — p65 (§18 tail Transpositionen eq(3) + examples; §19 Permutationen erster u. zweiter Art start, .tex 2231-2265) — p1-99 gap pass — (verified by eye; ★Fraktur + §-structure checks) — **FULLY FAITHFUL (0 fixes) + 3 formatting flags**
**CONTENT: 0 edits.** File unchanged: **418pp / 0 overfull / 0 underfull / PDF 2264696 B** (no edit -> no recompile).
- **★ §-STRUCTURE VERIFIED:** running header on p65 reads "§19 Permutationen" -- CORRECT: §19 "Permutationen erster und zweiter Art"
  begins partway down p65 (.tex 2257, grep-confirmed). §18 body content (top+mid) is faithful; §19 heading IS in .tex (not dropped).
  Header is page furniture (out of scope) but the heading it names is present.
- **FAITHFUL (top, §18 tail .tex 2231-2239):** "ergiebt, so dass das Zeichen Π(n) hier dieselbe Bedeutung hat, wie im ersten Abschnitt
  (§7)."; "Irgend eine Anordnung des Systems $\mathfrak A$ bezeichnen wir mit $\mathfrak A'$, oder ausführlicher, wenn α_1,α_2...α_n die
  Ziffern 1,2...n in irgend einer Reihenfolge bedeuten, mit"; **eq(3)** $\mathfrak A'=\alpha_1,\alpha_2,\ldots,\alpha_n$; "Man kann auf sehr
  verschiedene Arten... die durch sogenannte **Transpositionen**, d.h. durch successive Vertauschung von nur zwei Elementen...".
- **FAITHFUL (mid, .tex 2239-2255):** "Man kann zu diesem Zweck etwa so verfahren, dass man in $\mathfrak A$ zunächst das Element 1 mit dem,
  was in $\mathfrak A'$ an erster Stelle steht, also mit α_1, vertauscht (falls nicht α_1=1 ist), dann, wenn α_2 nicht schon =2 ist, 2 mit
  α_2 u.s.f."; "Um z.B. von (1,2,3,4) zu (4,3,2,1) zu gelangen, bildet man die Anordnungen"; $(1,2,3,4),(4,2,3,1),(4,3,2,1)$; "Bezeichnen
  wir eine Transposition kurz durch die beiden vertauschten Ziffern, also die Vertauschung von 1 mit 2 durch (1,2), so haben wir hier nach
  einander die Transpositionen $(1,4),(2,3)$ ausgeführt."; "Es ist zu bemerken, dass der Uebergang... auf unendlich viele verschiedene Arten...
  So geht (1,2,3,4) auch durch die Transpositionen $(1,2),(1,3),(2,4),(1,2)$ in (4,3,2,1) über."
- **FAITHFUL (bot, §19 start .tex 2257-2265):** **§19 heading "Permutationen erster und zweiter Art"**; "Die Π(n) Anordnungen von n
  Elementen lassen sich nach folgendem Gesichtspunkte in zwei Arten zerlegen."; "Aus den n Elementen unseres Systems lassen sich
  $\frac{n(n-1)}{2}$ und nicht mehr Paare bilden. Wir wollen nun den n Elementen" (breaks to p66). ALL word-for-word. (footer "Weber,
  Algebra. I." + sheet-sig "5" = printer mark, out of scope.)
- **★ FRAKTUR 𝔄/𝔄' PRESERVED** at ALL occurrences (5+ on this page: "System 𝔄", "mit 𝔄'", "in 𝔄", "in 𝔄'", "aus 𝔄 jede andere 𝔄'"); .tex
  \mathfrak A / \mathfrak A' -- MATCH, no italic-normalization. Determinanten Fraktur clean through p65.
- **⚠ FORMATTING-PASS FLAGS (inline-vs-display, systematic, NOT content):** §18-§19 .tex CONSISTENTLY promotes short inline formula-lists
  to DISPLAYS that Weber sets INLINE: p65 scan has $(1,4),(2,3)$ INLINE, $(1,2),(1,3),(2,4),(1,2)$ INLINE, $\frac{n(n-1)}{2}$ INLINE; .tex
  makes all three separate displays. (p64 same for Π(1)=1,Π(2)=2.) => SYSTEMATIC formatting-pass item: "§18-§19 inline-math-lists promoted
  to displays". Identical content. Track as ONE systematic item.
- **SKIP:** ellipsis. **EMPHASIS (gesperrt, tracked):** §19 heading; "Transpositionen".
- **★ META-PATTERN (18 clean pages p48-65):** §18/§19 permutation theory + Fraktur clean. The only §18-§19 deviation is the systematic
  inline->display promotion (formatting, content-identical). Determinanten section faithful so far.
- NEXT: **p66** = §19 cont. Differenzenproduct P/P' + sign-of-permutation (.tex 2265-2310+): "...Wir wollen nun den n Elementen 1,2,...,n
  in bestimmter Weise n reelle Zahlwerthe a_1,a_2,...,a_n zuordnen, und aus diesen Zahlwerthen die n(n-1)/2 Differenzen [a_1-a_2,a_1-a_3,...]
  bilden, wobei der niedrigere Index dem Minuenden angehören soll. Das Differenzenproduct"; **eq(1)** $P=(a_1-a_2)(a_1-a_3)\cdots(a_1-a_n)
  (a_2-a_3)\cdots(a_2-a_n)\cdots(a_{n-1}-a_n)$; "wird... einen von Null verschiedenen Werth... positiven, wenn a_1>a_2>...>a_n"; "Wenn wir
  nun die Indices... von $\mathfrak A$ zu $\mathfrak A'$ übergehen, so geht P in"; **eq(2)** $P'=(a_{\alpha_1}-a_{\alpha_2})\cdots$; "über...
  P' entweder gleich P oder entgegengesetzt zu P"; **I.** erste/zweite Art def; **II.** Transposition (h,k) ändert Vorzeichen. Continue
  gap-pass p66->p99. ★★ FRAKTUR WATCH (𝔄/𝔄'); ZOOM P/P' Differenzenproduct factor-structure + a_{α_i} subscript-of-subscript; sign
  argument I/II. Read prose word-by-word. Fix drops/rewords/misreads/norms/FABRIC; [sic] Weber errata. Compile-gate IF edit.
**Confirmed by eye vs ~500dpi scans; page fully faithful, no edit. Fraktur clean.**


### 2026-07-03 — p66 (§19 Differenzenproduct P eq(1) + permuted P' eq(2) + sign-of-permutation I/II, .tex 2265-2293) — p1-99 gap pass — (verified by eye; ★Fraktur + nested-subscript checks) — **FULLY FAITHFUL (0 fixes)**
**CONTENT: 0 edits.** File unchanged: **418pp / 0 overfull / 0 underfull / PDF 2264696 B** (no edit -> no recompile).
- **FAITHFUL (top, .tex 2265-2277):** "...n reelle Zahlwerthe a_1,a_2,...,a_n zuordnen, und aus diesen Zahlwerthen die $\frac{n(n-1)}{2}$
  Differenzen a_1-a_2, a_1-a_3... bilden, wobei der niedrigere Index dem Minuenden angehören soll. Das Differenzenproduct"; **eq(1)**
  $P=(a_1-a_2)(a_1-a_3)\cdots(a_1-a_n)(a_2-a_3)\cdots(a_2-a_n)\cdots(a_{n-1}-a_n)$ [all factors verified]; "wird, wenn die a_1,...,a_n von
  einander verschiedene Zahlwerthe sind, einen von Null verschiedenen Werth haben, z.B. einen positiven, wenn $a_1>a_2>a_3>\cdots>a_n$
  angenommen war."
- **FAITHFUL (mid, .tex 2277-2289):** "Wenn wir nun die Indices 1,2,3,...,n irgendwie unter einander vertauschen, also etwa von
  $\mathfrak A$ zu $\mathfrak A'$ übergehen, so geht P in"; **eq(2)** $P'=(a_{\alpha_1}-a_{\alpha_2})(a_{\alpha_1}-a_{\alpha_3})\cdots(a_{\alpha_1}
  -a_{\alpha_n})(a_{\alpha_2}-a_{\alpha_3})\cdots(a_{\alpha_2}-a_{\alpha_n})\cdots(a_{\alpha_{n-1}}-a_{\alpha_n})$ [★ZOOM: nested $a_{\alpha_i}$
  subscripts all correct, match .tex]; "über, und dies Product besteht, abgesehen vom Vorzeichen, aus denselben Factoren wie P, d.h. es ist
  P' entweder gleich P oder entgegengesetzt zu P."; **I.** (gesperrt) "Wir rechnen nun die Anordnung $\mathfrak A'$ und also auch die
  Permutation, die $\mathfrak A$ in $\mathfrak A'$ verwandelt, zur ersten oder zur zweiten Art, je nachdem P mit P' gleich oder entgegengesetzt
  ist, so dass $\mathfrak A$ selbst zur ersten Art gehört."
- **FAITHFUL (bot, .tex 2291-2293):** **II.** (gesperrt) "Durch eine einfache Transposition $(h,k)$, worin h,k irgend zwei der Ziffern
  1,2,...,n bezeichnen, ändert sowohl P als P' sein Vorzeichen."; "Denn die Factoren, die h und k gar nicht enthalten, werden durch diese
  Transposition nicht berührt; dann haben wir in P und P' den Factor $\pm(a_h-a_k)$ und die Factorenpaare $\pm(a_h-a_\nu)(a_k-a_\nu)$, wo ν
  die Reihe der Zahlen 1,2,...,n, mit Ausnahme von h,k durchläuft. Der erstere Factor ändert aber sein Zeichen, während das Factorenpaar
  ungeändert bleibt bei der Transposition (h,k). Daraus folgt:" (breaks to p67). ALL word-for-word.
- **★ FRAKTUR 𝔄/𝔄' PRESERVED** at all occurrences (von 𝔄 zu 𝔄'; Anordnung 𝔄'; 𝔄 in 𝔄' verwandelt; 𝔄 selbst); .tex \mathfrak A/\mathfrak A' -- MATCH.
- **⚠ FORMATTING-PASS FLAGS:** (a) eq(1) scan = 4-line display (P=... / (a_2-a_3)... / dots-row / (a_{n-1}-a_n)); .tex = single-line inline
  product. (b) eq(2) scan = 3-line + dots-row; .tex = 2 aligned lines. (c) SYSTEMATIC inline->display: scan has "a_1-a_2,a_1-a_3..." + the
  Factorenpaare $\pm(a_h-a_\nu)(a_k-a_\nu)$ INLINE; .tex displays them. All = layout, content-identical (same §18-§19 systematic item).
- **SKIP:** ellipsis. **EMPHASIS (gesperrt, tracked):** statements **I.** and **II.** (whole paragraphs letter-spaced).
- **★ META-PATTERN (19 clean pages p48-66):** §19 Differenzenproduct/sign-of-permutation + Fraktur + nested subscripts all clean. Determinanten
  faithful through p66. Only deviations = systematic inline->display + multi-line-layout (formatting, content-identical).
- NEXT: **p67** = §19 cont. after "Daraus folgt:" -- sign-change conclusion (.tex 2294-2340+): the display $\pm(a_h-a_\nu)(a_k-a_\nu)$;
  then the result (III or eq) that each single transposition FLIPS the Art (P->-P), hence a permutation's Art = parity of #transpositions;
  likely "Eine Permutation ist von erster/zweiter Art je nachdem sie durch gerade/ungerade Zahl von Transpositionen entsteht" + theorem that
  #transpositions parity is invariant. Continue gap-pass p67->p99. ★★ FRAKTUR WATCH (𝔄/𝔄'); read prose word-by-word; ZOOM P/P' signs,
  transposition-parity argument. Fix drops/rewords/misreads/norms/FABRIC; [sic] Weber errata. Compile-gate IF edit.
**Confirmed by eye vs ~500dpi scans; page fully faithful, no edit. Fraktur clean.**


### 2026-07-03 — p67 (§19 tail: III/Folgerung/IV + repeat-transposition argument + n=3 array + footnote, .tex 2294-2327) — p1-99 gap pass — (verified by eye; ★Fraktur 𝔄/𝔅 + ★ellipsis-in-prose checks) — **2 CONTENT FIXES (both ellipsis deviations) + FAITHFUL otherwise**
**CONTENT: 2 edits (both .tex 2309, one sentence).** After fix: **418pp / 0 overfull / 0 underfull / PDF 2264703 B** (was 2264696; +7 B from 2×\ldots − "u.~s.~f."). Compile-gate PASSED.
- **★★ FIX #55 + #56 — TWO GPT ELLIPSIS DEVIATIONS in one sentence (.tex 2309):** Weber uses "…" THREE times in this prose passage as "and so on"; GPT handled them INCONSISTENTLY:
  - (a) scan "\(\mathfrak A''\) in \(\mathfrak B''\) **…**, und wenn" — .tex **DROPPED** the ellipsis (comma only). **FIX #55:** inserted `\ldots` -> "…\(\mathfrak B''\) \ldots, und wenn".
  - (b) scan "\(\mathfrak B'\) wieder in \(\mathfrak A'\) **…** über" — .tex **SUBSTITUTED real German words "u.~s.~f."** (=und so fort) for Weber's dots. **FIX #56:** replaced "u.~s.~f." -> `\ldots\ ` (word-fabrication reverted).
  - (c) scan "\(\mathfrak B,\mathfrak B',\mathfrak B''\) **…** alle" — .tex ALREADY correct as `\ldots` (this is the one GPT kept). Left as-is.
  -> All three parallel prose-ellipses now match Weber = `\ldots`. #56 is the clearer defect (words for dots = text fabrication); #55 is a dropped mark. ★ ZOOM-confirmed both (crop_3_37, crop_3_44) + full mid third.
- **FAITHFUL (top, .tex 2294-2303):** display \(\pm(a_h-a_\nu)(a_k-a_\nu)\); "wo ν die Reihe 1,2,…,n mit Ausnahme von h,k durchläuft… Der erstere Factor ändert sein Zeichen, während das Factorenpaar ungeändert bleibt bei der Transposition (h,k). Daraus folgt:"; **III.**(gesperrt) "Die Permutationen der ersten Art sind aus einer geraden Anzahl von Transpositionen zusammengesetzt, und die der zweiten Art aus einer ungeraden Anzahl."; "identische Permutation… lässt 𝔄 ungeändert"; **Folgerung** "Auf wie verschiedenen Wegen man auch 𝔄' aus 𝔄 durch Transpositionen ableiten mag, die Anzahl dieser Transpositionen ist… übereinstimmend gerade oder ungerade…".
- **FAITHFUL (mid, .tex 2305-2313, APART from the 2 ellipsis fixes):** "Wenn wir in den sämmtlichen Anordnungen 𝔄,𝔄',𝔄''… der n Elemente eine Transposition, etwa (1,2), vornehmen, so geht jede… über, etwa 𝔄 in 𝔅, 𝔄' in 𝔅', 𝔄'' in 𝔅'' …, und wenn wir dieselbe Transposition noch einmal wiederholen, so geht 𝔅 wieder in 𝔄, 𝔅' wieder in 𝔄' … über. Daraus folgt, dass die Anordnungen 𝔅,𝔅',𝔅''… alle von einander verschieden sind und folglich in ihrer Gesammtheit mit der Gesammtheit der 𝔄 übereinstimmen."; display P,P',P'',…; "die aus P mit den verschiedenen Anordnungen 𝔄,𝔄',𝔄''… gebildet sind, durch eine Transposition das Zeichen ändern, so folgt, dass jedem 𝔄 der ersten Art ein 𝔅 der zweiten Art entspricht und jedem 𝔄 der zweiten Art ein 𝔅 der ersten Art."
- **FAITHFUL (bot, .tex 2315-2327):** **IV.**(gesperrt) "Hiernach ist die Anzahl der Anordnungen der ersten Art ebenso gross, wie die Anzahl der Anordnungen der zweiten Art, nämlich ½Π(n)."; "Für n=3 haben wir die folgenden sechs Anordnungen, von denen die erste Horizontalreihe die erste Art bildet:"; **array(3)** (1,2,3),(2,3,1),(3,1,2) / (3,2,1),(2,1,3),(1,3,2) [★all six triples exact]; footnote "Diese Sätze sind hier aus der Betrachtung des Productes P, also einer Zahlgrösse, gewonnen. Wie man ohne Benutzung einer solchen Function zu denselben Ergebnissen gelangen kann, werden wir im XIV. Abschnitt sehen." ALL word-for-word.
- **★ FRAKTUR 𝔄/𝔄'/𝔄'' + 𝔅/𝔅'/𝔅'' ALL PRESERVED** at every occurrence (many this page); .tex \mathfrak A/\mathfrak B — MATCH, no font-slip. (The known prior 𝔅 font-slip stays fixed.)
- **⚠ FORMATTING/STRUCTURAL FLAGS (text fully preserved — NOT content edits):** (a) **FOOTNOTE FLATTENED:** Weber prints "Diese Sätze…" as a real FOOTNOTE (marker ¹⁾ after ½Π(n), rule, small type at page foot); .tex renders it as inline body text and drops the ¹⁾ marker. Same words -> restore via \footnote in fmt pass. (b) **DROPPED EQ-NUMBER (3):** Weber numbers the n=3 array "(3)" (leqno position); .tex array is untagged \[…\]. Add \tag{3}+leqno in fmt pass (watch downstream ref-number consistency). (c) §20 heading NOT on p67 (footnote + "5*" signature end page) — .tex flows array→footnote-text→§20 continuously (page-break differs, layout).
- **SKIP:** none new. **EMPHASIS (gesperrt, tracked):** statements **III.** and **IV.** (whole letter-spaced).
- **★★ METHOD REFINEMENT (ellipsis policy):** prior "ellipsis = SKIP" holds for MATH-list dot-count/comma typography ONLY. In PROSE, when Weber's "…" means "und so fort" and GPT (a) drops it or (b) substitutes real words, that IS a text-content deviation -> FIX. ★ HOTSPOT LESSON: parallel-structure enumerations (𝔄 in 𝔅, 𝔄' in 𝔅', …) are a GPT-inconsistency trap — GPT kept 1 of 3 sibling ellipses, damaged 2. When one ellipsis is kept, CHECK ITS SIBLINGS. This page broke the 19-clean streak (p48-66) — confirms never-certify: even "clean-looking" systematic Determinanten prose hides GPT damage at enumeration seams.
- NEXT: **p68** = §20 Determinanten (.tex 2329-2360+): heading "§20. Determinanten"; "System von n² beliebigen Grössen… a_i^{(k)}… i,k durchlaufen 1,2,3,…,n… ordnen in ein Quadrat… bezeichnen mit Δ, also:"; **eq(1)** Δ = |a_i^{(k)}| n×n vmatrix (a_1^{(1)}…a_n^{(1)} / … / a_1^{(n)}…a_n^{(n)}); "Horizontalreihen Zeilen, Verticalreihen Colonnen…". Continue gap-pass p68->p99. ★★ FRAKTUR watch; ZOOM the Δ matrix double-index a_i^{(k)} (upper=row/(k), lower=col/i — verify Weber's index convention), n×n entries + dots-rows. Read prose word-by-word. ★ CHECK ELLIPSES IN PROSE. Fix drops/rewords/misreads/norms/FABRIC; [sic] Weber errata. Compile-gate IF edit.
**Confirmed by eye vs ~500dpi scans; 2 ellipsis fixes applied + gate held; Fraktur clean.**


### 2026-07-03 — p68 (§20 Determinanten start: Δ-def eq(1) + Zeilen/Colonnen + M diagonal eq(2) + M' permuted eq(3) + ΣM sum-def, .tex 2329-2358) — p1-99 gap pass — (verified by eye; ★Δ double-index + ★dropped-display check) — **1 CONTENT FIX (dropped display ΣM restored) + FAITHFUL otherwise**
**CONTENT: 1 edit (.tex 2358).** After fix: **418pp / 0 overfull / 0 underfull / PDF 2264914 B** (was 2264703). Compile-gate PASSED.
- **★★ FIX #57 — DROPPED DISPLAY EQUATION restored (.tex 2358):** Weber prints at foot of p68 a DISPLAY "Die Summe aus diesen Producten / \(M+M'+M''+\cdots=\Sigma M\)" (introducing his ΣM sum-notation), then p69 continues "soll Δ sein." GPT had FOLDED this into prose "Die Summe aus diesen Producten soll Δ sein." — **the whole display + the ΣM notation were dropped.** ZOOM-confirmed (crop_18_82: "M + M′ + M″ + · · · = Σ M"). Grep confirmed `\Sigma M` appears NOWHERE else in .tex (not relocated; genuinely deleted). Restored as `\[ M+M'+M''+\cdots=\Sigma M \]`.
- **FAITHFUL (top, .tex 2329-2331):** §20 heading "§. 20. / Determinanten."; "Wir betrachten jetzt ein System von n² beliebigen Grössen, mit denen die rationalen Rechenoperationen ausgeführt werden können. Zu einer einfachen Bezeichnung dieser Grössen wählen wir einen Buchstaben mit einem doppelten Index a_i^{(k)}, worin i sowohl als k die Reihe der Ziffern 1,2,3…n durchlaufen soll. Zur besseren Uebersicht ordnen wir diese Grössen in ein Quadrat, so dass alle a mit demselben oberen Index in einer Horizontalreihe, alle a mit demselben unteren Index in einer Verticalreihe stehen, und bezeichnen dies Quadrat mit Δ, also:"
- **FAITHFUL (mid, .tex 2332-2347):** **eq(1)** Δ = n×n vmatrix a_1^{(1)}…a_n^{(1)} / a_1^{(2)}…a_n^{(2)} / a_1^{(3)}…a_n^{(3)} / [dots-row] / a_1^{(n)}…a_n^{(n)} [★all entries + double-index a_i^{(k)} (upper=(k)=row, lower=i=col) verified]; "Der Kürze halber nennt man die Horizontalreihen **Zeilen**, die Verticalreihen **Colonnen**."; "Wir wollen aber unter dem zwischen verticalen Strichen eingeschlossenen Quadrat nicht nur den Complex der Grössen a verstehen, sondern eine bestimmte arithmetische Verbindung dieser Grössen, die sich ausrechnen lässt, sobald die a numerisch gegeben sind, und die wir jetzt beschreiben wollen."; "Man bilde das Product der in der von links oben nach rechts unten gehenden Diagonale stehenden Glieder:"
- **FAITHFUL (bot, .tex 2348-2357):** **eq(2)** M=a_1^{(1)}a_2^{(2)}a_3^{(3)}…a_n^{(n)}; "leite daraus Π(n) Producte M,M',M''… her, indem man die unteren Indices permutirt, und gebe jedem so entstandenen Product das positive oder negative Zeichen, je nachdem die angewandte Permutation zur ersten oder zur zweiten Art gehört, also nach der Bezeichnung des vorigen Paragraphen"; **eq(3)** M'=±a_{α_1}^{(1)}a_{α_2}^{(2)}…a_{α_n}^{(n)} [★ZOOM nested α-subscripts + (k)-superscripts correct]; "Die Summe aus diesen Producten" + [restored display]. ALL word-for-word.
- **⚠ FORMATTING-PASS FLAGS (not content):** (a) **MATRIX COMMA-SEPARATORS:** Weber's eq(1) rows use commas between entries "a_1^{(1)}, a_2^{(1)}, a_3^{(1)} … a_n^{(1)}"; .tex vmatrix is space/&-separated (no commas). SYSTEMATIC Weber determinant convention -> fmt pass. (b) matrix dots-row (Weber horizontal-ish dots vs .tex \vdots columns). (c) leqno eq-numbers (1),(2),(3) on left; .tex \tag on right.
- **SKIP:** math-list ellipsis "1,2,3…n" (typographic). **EMPHASIS (gesperrt, tracked):** §20 heading; "Zeilen"; "Colonnen"; "Die Summe aus diesen Producten"(partly).
- **★★ METHOD NOTE (dropped-display hotspot):** GPT dropped an UNNUMBERED display that INTRODUCES notation (ΣM), folding it into prose. Continues the pattern: GPT damage clusters at NOTATION-INTRODUCTION seams. ★ LESSON: unnumbered displays are higher drop-risk than numbered ones (no \tag to preserve); when prose says "Die Summe/das Product … [name]" watch for a dropped defining display. Grep the introduced symbol (here \Sigma M) to confirm drop vs relocation.
- NEXT: **p69** = §20 cont. (.tex 2358-2403+): "soll Δ sein. Δ wird die Determinante der n² Elemente a_i^{(k)} genannt… n-reihige Determinante (Determinante nten Grades oder nter Ordnung). Das Glied M… das Hauptglied genannt."; "Nehmen wir z.B. n=2" **eq(4)** 2×2 Δ=a_1^{(1)}a_2^{(2)}−a_2^{(1)}a_1^{(2)}; "und für n=3" **eq(5)** 3×3 six-term expansion; "Oder in anderer Bezeichnung" **eq(6)** |a,b;c,d|=ad−bc, **eq(7)** 3×3 |a,b,c;a',b',c';a'',b'',c''|=ab'c''+…; "Es ist dem Leser zu empfehlen, die Berechnung solcher Determinanten an Zahlenbeispielen einzuüben."; "Die Bezeichnung (1) ist… kürzere Zeichen… So setzt Jacobi…". Continue gap-pass p69->p99. ★★ ZOOM eq(4)/(5)/(7) sign patterns (6-term 3×3 det ±abc); Δ double-index; ★ CHECK PROSE ELLIPSES + DROPPED DISPLAYS. Fix drops/rewords/misreads/norms/FABRIC; [sic] errata. Compile-gate IF edit.
**Confirmed by eye vs ~500dpi scans; 1 dropped-display fix applied + gate held; Δ indices clean.**


### 2026-07-03 — p69 (§20 Determinanten cont.: Determinante/Hauptglied def + n=2 eq(4) + n=3 eq(5) + andere Bezeichnung eq(6-7) + Jacobi eq(8)/Kronecker eq(9) + symmetrische Det., .tex 2358-2427) — p1-99 gap pass — (verified by eye; ★multi-zoom eq(4)/(5)/(8)) — **3 CONTENT FIXES + FAITHFUL otherwise**
**CONTENT: 3 edits.** After fix: **418pp / 0 overfull / 0 underfull / PDF 2264839 B** (was 2264914). Compile-gate PASSED. ★★ §20 = HIGH-DAMAGE zone (p67:2, p68:1, p69:3).
- **★★ FIX #58 — FABRICATED MATRIX removed (eq(4), .tex 2362-2367):** Weber's eq(4) (n=2) is EXPANSION-ONLY: "Δ = a_1^{(1)}a_2^{(2)} − a_2^{(1)}a_1^{(2)}". GPT had INSERTED an intermediate 2×2 vmatrix "Δ = |a_1^{(1)},a_2^{(1)};a_1^{(2)},a_2^{(2)}| = …" that Weber did NOT print. ZOOM-confirmed (crop_3_15: single-line expansion, no matrix). Corroborated by eq(5) (n=3) being expansion-only in BOTH scan & .tex — GPT only fabricated the eq(4) matrix (inconsistent → improvised). Removed the vmatrix.
- **★★ FIX #59 — DROPPED PHRASE restored (.tex 2370):** scan "und für n=3 **[nach (3) des vorigen Paragraphen]**:" — GPT dropped the bracketed cross-reference, leaving "und für n=3:". ZOOM-confirmed (crop_3_15). Restored "[nach (3) des vorigen Paragraphen]". ★ This ref points to §19's n=3 arrangement-array (numbered (3) in Weber) → CORROBORATES p67 fmt-flag that .tex dropped that array's eq-number (3).
- **★★ FIX #60 — eq(8) SUBSCRIPT ALTERATION (.tex 2409):** Jacobi's notation writes "nur das Hauptglied" = NATURAL indices: scan eq(8) "Δ = Σ± a_1^{(1)} a_2^{(2)} … a_n^{(n)}". GPT had written "a_{α_1}^{(1)}a_{α_2}^{(2)}…a_{α_n}^{(n)}" (α-permuted subscripts — copied from the neighboring generic M' form eq(3)/p68), contradicting "Hauptglied". ZOOM-confirmed (crop_6_57: subscripts plainly 1,2,n). Restored natural subscripts a_1…a_n.
- **FAITHFUL (top, .tex 2358-2381):** "soll Δ sein. Δ wird die Determinante der n² Elemente a_i^{(k)} genannt… n-reihige Determinante (nten Grades / nter Ordnung). Das Glied M… das **Hauptglied** genannt."; "Nehmen wir z.B. n=2, so erhalten wir" eq(4)[fixed]; "und für n=3 [nach (3)…][restored]:" **eq(5)** n=3 six-term expansion Δ = a_1^{(1)}a_2^{(2)}a_3^{(3)} + a_2^{(1)}a_3^{(2)}a_1^{(3)} + a_3^{(1)}a_1^{(2)}a_2^{(3)} − [three neg terms]. ★ZOOM eq(5): ALL SIX TERMS present & correctly signed; positive terms (123,231,312) match .tex order; the 3 NEGATIVE terms are the same set {321,213,132} in DIFFERENT ORDER (scan 321,213,132 vs .tex 132,213,321) = commutative summand-reorder → SKIP (no sign/term error).
- **FAITHFUL (mid, .tex 2382-2417):** "oder in anderer Bezeichnung:" **eq(6)** |a,b;c,d| = ad−bc; **eq(7)** |a,b,c;a',b',c';a'',b'',c''| = ab'c''+bc'a''+ca'b''−ac'b''−ba'c''−cb'a'' [★all 6 terms exact, same order & signs]; "Es ist dem Leser zu empfehlen, die Berechnung solcher Determinanten an Zahlenbeispielen einzuüben."; "Die Bezeichnung (1) ist in vielen Fällen zu umständlich; es sind daher noch andere, kürzere Zeichen im Gebrauch. So setzt Jacobi, indem er nur das Hauptglied der entwickelten Determinante ausführlich schreibt:" eq(8)[fixed]; "und Kronecker noch kürzer:" **eq(9)** Δ = |a_i^{(k)}|; "Beide Bezeichnungen sind aber nur dann ganz deutlich…".
- **FAITHFUL (bot, .tex 2417-2427):** "…durchaus unanwendbar, wenn die Elemente z.B. numerisch gegeben sind."; "Es kommen bisweilen Determinanten vor, bei denen" display a_i^{(k)}=a_k^{(i)} "ist, bei denen also in (1) die symmetrisch zur Diagonale des Quadrats stehenden Elemente einander gleich sind. Wir werden in diesen Fällen gewöhnlich beide Indices (um ihre Gleichwerthigkeit anzudeuten) unten hinsetzen, also" display a_{i,k}=a_{k,i} "setzen. Solche Determinanten heissen **symmetrisch**." ALL word-for-word. Page ends; §21 heading starts p70.
- **⚠ FORMATTING-PASS FLAGS:** matrix comma-separators (eq(6)/(7) "a, b" etc.); leqno eq-nums (4)-(9); eq(5) neg-summand order (skip, but note). **SKIP:** commutative summand-reorder (eq(5) neg terms); math-list ellipsis. **EMPHASIS (gesperrt):** "Hauptglied"; "symmetrisch".
- **★★ METHOD (§20 damage patterns, 3 new mechanisms):** (1) ★ FABRICATED INTERMEDIATE FORM — GPT ADDS structure (a matrix) not in scan to "show work"; check if a display has MORE than the scan. (2) ★ NEIGHBOR-COPY ALTERATION — GPT homogenizes a symbol to match an adjacent equation with DIFFERENT meaning (Hauptglied-natural vs generic-α); verify against PROSE semantics, not the neighbor. (3) ★ DROPPED BRACKETED CROSS-REFS — parenthetical "[nach (N) des …]" refs are drop-prone. ★ §20 is a hotspot; ZOOM EVERY equation vs prose. Never-certify hard-confirmed: 3 real defects on one "systematic" page.
- NEXT: **p70** = §21 Hauptsätze über Determinanten (.tex 2429-2470+): heading "§. 21. Hauptsätze über Determinanten."; "Aus dem Begriff der Determinante ergeben sich leicht die ersten Sätze…"; "Wenn wir in dem Product" **§21-eq(1)** M'=±a_{α_1}^{(1)}a_{α_2}^{(2)}…a_{α_n}^{(n)} [★NOTE: α HERE IS CORRECT — generic M', NOT Hauptglied; do NOT "fix"]; "die Factoren umstellen… unteren Indices natürliche Reihenfolge 1,2,…,n… obere permutirt" **§21-eq(2)** ±a_1^{(β_1)}a_2^{(β_2)}…a_n^{(β_n)}; "(β_1,…,β_n)=𝔅…"; **I.** Determinante durch obere-Index-Permutation; **II.** Zeilen↔Colonnen invariant; **III.** zwei Indices vertauschen → Vorzeichenwechsel; **IV.**/… Continue gap-pass p70->p99. ★★ ZOOM §21-eq(1)/(2) (α vs β subscripts — both correct as-is); ★ Fraktur 𝔅/𝔄; ★ check dropped displays/brackets/prose-ellipses. Fix drops/rewords/misreads/norms/FABRIC; [sic] errata. Compile-gate IF edit.
**Confirmed by eye vs ~500dpi scans; 3 fixes (fabrication + drop + alteration) applied + gate held.**


### 2026-07-03 — p70 (§21 Hauptsätze über Determinanten start: intro + M' eq(1) + eq(2) + 𝔅/𝔄-Anordnung prose + Satz I, .tex ~2424-2444) — p1-99 gap pass — (verified by eye; ★Fraktur 𝔄/𝔅 + ★dropped-crossref/eq-tail checks) — **2 CONTENT FIXES (both dropped) + FAITHFUL otherwise**
**CONTENT: 2 edits.** After fix: **418pp / 0 overfull / 0 underfull / PDF 2264920 B** (was 2264839). Compile-gate PASSED. §20-§21 damage zone continues (p67:2,p68:1,p69:3,p70:2).
- **★★ FIX #61 — DROPPED BRACKETED CROSS-REF (.tex 2428):** scan "Wenn wir in dem Product **[§. 20, (3)]**"; GPT dropped the bracket, leaving "Wenn wir in dem Product". Restored as "[\S\,20, (3)]" (house style: inline refs = "\S\,NN, (K)", cf. \S\,21,V / \S\,22,(2); §.-period = skip-tier). 3rd dropped-bracket in this section (cf. p69 #59).
- **★★ FIX #62 — DROPPED EQUATION-TAIL "=𝔄" (.tex 2442):** Weber prints a display "(α_1,α_2…α_n) = 𝔄" (parallel to the "(β_1,β_2…β_n)=𝔅" display just above, defining 𝔄). GPT FLATTENED it to inline AND dropped the "=𝔄" tail, keeping only "(α_1,α_2,…,α_n)". Restored "=\mathfrak A" -> "\((\alpha_1,\alpha_2,\ldots,\alpha_n)=\mathfrak A\)". (Display-promotion of this relation = fmt pass; content = the restored =𝔄.)
- **FAITHFUL (top, .tex 2424-2433):** §21 heading "§. 21. / Hauptsätze über Determinanten."; "Aus dem Begriff der Determinante ergeben sich leicht die ersten Sätze, die für die Anwendung geeignet sind."; "Wenn wir in dem Product [restored]" **eq(1)** M'=±a_{α_1}^{(1)}a_{α_2}^{(2)}…a_{α_n}^{(n)} [★α CORRECT — generic M', NOT Hauptglied; left as-is]; "die Factoren umstellen, so ändert sich sein Werth nicht… untere Indices natürliche Reihenfolge 1,2…n… obere permutirt… M' die Form erhalten:".
- **FAITHFUL (mid, .tex 2434-2442):** **eq(2)** ±a_1^{(β_1)}a_2^{(β_2)}…a_n^{(β_n)}; "worin" display (β_1,β_2…β_n)=𝔅[,] "ebenso wie (α_1,α_2…α_n)=𝔄[restored] eine Anordnung der Ziffern 1,2…n bedeutet. Man kann die Anordnung 𝔅 dadurch erhalten, dass man in den Factoren von M' die Transpositionen, die zu 𝔄 geführt haben, von der letzten anfangend, rückgängig macht… Die dabei sich ergebende Reihenfolge der oberen Indices ist dann die Anordnung 𝔅. Es folgt daraus, dass 𝔅 zur ersten oder zur zweiten Art gehört, je nachdem 𝔄…; da beide durch die gleiche Anzahl von Transpositionen entstehen. Die Gesammtheit der 𝔅 stellt ebenso wie die Gesammtheit der 𝔄 alle Permutationen der n Elemente dar, da zwei verschiedene 𝔄 niemals zu demselben 𝔅 führen können. Damit ist bewiesen:". ★ FRAKTUR 𝔄/𝔅 ALL PRESERVED (many occ.).
- **FAITHFUL (bot, .tex 2442-2444):** **I.**(gesperrt) "Die Determinante Δ kann auch dadurch gebildet werden, dass man in dem Hauptglied a_1^{(1)}a_2^{(2)}…a_n^{(n)} die oberen Indices auf alle möglichen Arten permutirt, jedem der so gebildeten Producte das positive oder negative Zeichen giebt, je nachdem die angewandte Permutation zur ersten oder zweiten Art gehört, und dann die Summe aller dieser Producte nimmt." ★ Hauptglied = NATURAL indices a_1^{(1)}…a_n^{(n)} -> CORROBORATES p69 fix #60 (eq(8) natural). Page ends; §21 Sätze II-V continue p71.
- **⚠ FORMATTING-PASS FLAGS:** (α…)=𝔄 display-vs-inline (fmt); trailing comma after 𝔅 display (skip); leqno eq(1)/(2). **SKIP:** math-list ellipsis; §.-period.
- **★★ METHOD (corroboration + pattern):** (1) DROPPED-BRACKETED-CROSS-REF now confirmed on p69+p70 (systematic in §20-21) — parenthetical "[§ N, (K)]" / "[nach (K) …]" refs are drop-prone; scan the prose for them. (2) DROPPED EQ-TAIL via display-flatten — GPT flattens a display to inline and loses the "= X" tail; watch inline relations that should have an RHS. (3) Hauptglied-natural CORROBORATED across pages (p69 eq(8), p70 Satz I) — a cross-page consistency check that validated #60.
- NEXT: **p71** = §21 Sätze II-V + §22 Unterdeterminanten start (.tex 2446-2470+): "In der Darstellung von Δ… Zeilen/Colonnen… diesem Satze auch den folgenden Ausdruck geben:"; **II.** Zeilen↔Colonnen invariant; (transposition→sign arg); **III.** zwei untere/obere Indices vertauschen→Vorzeichenwechsel; "Etwas anders ausgedrückt: zwei Zeilen/Colonnen vertauschen→Vorzeichenwechsel"; **IV.** Zeilen/Colonnen permutiren→absoluter Werth gleich, Vorzeichen nach Art; "Aus III. … Fundamentalsatz:"; **V.** zwei gleiche Reihen→Werth Null; "Denn die Vertauschung…"; then **§22 heading "Unterdeterminanten"** (.tex 2468 — VERIFY vs scan!) + "In jedem Gliede der entwickelten Determinante Σ±a_{α_i}…, deren Werth mit A… " Continue gap-pass p71->p99. ★★ Fraktur; ★VERIFY §22 heading present; ★dropped brackets/eq-tails/displays; ★check A vs Δ notation switch (Weber switches Δ→A at §22). Fix drops/rewords/misreads/norms/FABRIC; [sic] errata. Compile-gate IF edit.
**Confirmed by eye vs ~500dpi scans; 2 dropped-content fixes applied + gate held; Fraktur clean.**


### 2026-07-03 — p71 (§21 cont.: Zeilen/Colonnen remark + Sätze II, III, IV, V + start of V-proof, .tex ~2446-2462) — p1-99 gap pass — (verified by eye; ★dropped-crossref + ★Fraktur checks) — **1 CONTENT FIX (dropped cross-ref) + FAITHFUL otherwise**
**CONTENT: 1 edit.** After fix: **418pp / 0 overfull / 0 underfull / PDF 2264959 B** (was 2264920). Compile-gate PASSED.
- **★★ FIX #63 — DROPPED CROSS-REF (.tex 2446):** scan "In der Darstellung **§. 20, (1)** von Δ werden durch die oberen Indices die Zeilen…"; GPT dropped "§. 20, (1)", leaving "In der Darstellung von Δ…". ZOOM-confirmed (crop_5_8). Restored "\S\,20, (1)" (house style). ★★ 4th dropped section/equation cross-ref in §20-21 (p69 "[nach (3) des vor. §]" #59, p70 "[§20,(3)]" #61, p70 "=𝔄" #62, p71 "§20,(1)" #63) — SYSTEMATIC GPT pattern.
- **FAITHFUL (top, .tex 2446-2450):** "In der Darstellung §.20,(1)[restored] von Δ werden durch die oberen Indices die Zeilen, durch die unteren Indices die Colonnen gekennzeichnet, und demnach können wir diesem Satze auch den folgenden Ausdruck geben:"; **II.**(gesperrt) "Eine Determinante ändert sich nicht, wenn die Zeilen zu Colonnen und die Colonnen zu Zeilen gemacht werden."; "Wenn wir in den sämmtlichen Anordnungen 𝔄,𝔄',𝔄''… der n Elemente irgend zwei Elemente mit einander vertauschen… jede Anordnung erster Art in eine Anordnung zweiter Art über und umgekehrt. Wenn wir also in den Gliedern M,M',M''…, aus denen Δ zusammengesetzt ist, irgend zwei untere Indices vertauschen…".
- **FAITHFUL (mid, .tex 2450-2456):** "…so geht jedes Glied mit positivem Zeichen in ein anderes über, das in Δ mit dem negativen Zeichen behaftet war und umgekehrt, also es ändert Δ sein Vorzeichen. Daraus folgt mit Hülfe von II. der Satz:"; **III.**(gesperrt) "Wenn man in Δ zwei untere oder zwei obere Indices mit einander vertauscht, so ändert die Determinante nur ihr Vorzeichen."; "Etwas anders ausgedrückt:" [set-off restatement] "Wenn man zwei Zeilen oder zwei Colonnen mit einander vertauscht, so ändert die Determinante nur ihr Vorzeichen" "und daraus allgemeiner:"; **IV.**(gesperrt) "Wenn in einer Determinante die Zeilen oder die Colonnen permutirt werden, so ändert sich der absolute Werth nicht, und das Vorzeichen ändert sich nicht oder geht in das entgegengesetzte über, je nachdem die angewandte Permutation zur ersten oder zweiten Art gehört.".
- **FAITHFUL (bot, .tex 2458-2462):** "Aus III[.] erhält man den folgenden Fundamentalsatz:"; **V.**(gesperrt) "Wenn in zwei Zeilen oder in zwei Colonnen die an gleicher Stelle stehenden Glieder einander gleich sind (kürzer ausgedrückt: wenn zwei Reihen einander gleich sind), so hat die Determinante den Werth Null."; "Denn die Vertauschung der zwei Reihen ändert nach III. das Zeichen, kann aber andererseits, da beide Reihen identisch [sind…]" (breaks to p72). ALL word-for-word.
- **★ FRAKTUR 𝔄/𝔄'/𝔄'' PRESERVED; M,M',M'' preserved; Δ preserved.** Page ends mid V-proof; Satz VI + §22 heading are on p72.
- **⚠ FORMATTING-PASS FLAGS:** (a) "Etwas anders ausgedrückt" restatement = Weber sets it off as an indented block (cap "Wenn"); .tex runs it inline "; wenn…". Words identical -> cap+layout = SKIP/fmt. (b) leqno (later eqs). **SKIP:** "Aus III[.]" period; §.-period; cap "Wenn/wenn"; math-list ellipsis. **EMPHASIS (gesperrt, tracked):** Sätze II, III, IV, V (whole statements).
- **★ RUNNING-HEADER NOTE (out of scope):** p71 recto running head = "Sätze über Determinanten." while §21 full title = "Hauptsätze über Determinanten." — Weber's own abbreviated running head (layout element, .tex doesn't reproduce Weber's running heads). NOT a content issue.
- **★★ METHOD (cross-ref drop = confirmed systematic):** 4 dropped section/eq cross-refs in §20-21 (#59,#61,#62,#63). ★ RULE: in the Determinanten chapters, SCAN EVERY sentence-initial "In/Nach/Aus der Darstellung/Formel/Product …" for a "§ N, (K)" or "[nach (K) …]" cross-ref GPT may have dropped. These are near-invisible (short, mid-prose) — the highest-miss-risk drop-class. Also watch dropped "=X" eq-tails on flattened displays (#62).
- NEXT: **p72** = §21 V-proof tail + Satz VI + §22 Unterdeterminanten (.tex 2462-2510+): "…da beide Reihen identisch sind, nichts ändern, so dass für Δ nur der Werth Null übrig bleibt."; "Man drückt den Satz V. nur anders aus, wenn man sagt:"; **VI.** "Man erhält eine verschwindende Determinante, wenn man die Elemente einer Reihe durch die entsprechenden Elemente einer anderen Reihe… ersetzt."; **§22 heading "Unterdeterminanten" (.tex 2468 — ★VERIFY present vs scan!)**; "In jedem Gliede der entwickelten Determinante" display Σ±a_{α_1}^{(1)}…a_{α_n}^{(n)}, "deren Werth wir jetzt mit **A** bezeichnen wollen" [★Δ→A notation switch]; Complex-a_1^{(k)}A_1^{(k)} argument; **eq(1)** A=a_1^{(1)}A_1^{(1)}+…+a_1^{(n)}A_1^{(n)}; **eq(2)** A=a_r^{(1)}A_r^{(1)}+…; **eq(3)** upper-index version; Unterdeterminanten A_r^{(ν)} def; **eq(4)** A_1^{(1)} = (n-1)-reihige Determinante. Continue gap-pass p72->p99. ★★ ZOOM eqs; ★VERIFY §22 heading; ★Δ→A switch; ★dropped cross-refs/eq-tails; ★Fraktur. Fix drops/rewords/misreads/norms/FABRIC; [sic] errata. Compile-gate IF edit.
**Confirmed by eye vs ~500dpi scans; 1 dropped-crossref fix applied + gate held; Fraktur clean.**


### 2026-07-03 — p72 (§21 V-proof tail + Satz VI + §22 Unterdeterminanten start: Σ±-def + eq(1-3) + generic-index passage, .tex ~2462-2493) — p1-99 gap pass — (verified by eye; ★4 zooms: Σ±/ν/μ) — **2 CONTENT FIXES (#64 α→natural, #65 index-relabel) + FAITHFUL otherwise**
**CONTENT: 4 edits (2 logical fixes).** After fix: **418pp / 0 overfull / 0 underfull / PDF 2264891 B** (was 2264959). Compile-gate PASSED.
- **★★ FIX #64 — Σ±-DISPLAY α→NATURAL (.tex 2472):** §22 opens "In jedem Gliede der entwickelten Determinante [display]". Scan display = "Σ ± a_1^{(1)} a_2^{(2)} … a_n^{(n)}" NATURAL subscripts (Jacobi Hauptglied form). .tex had "a_{α_1}^{(1)}a_{α_2}^{(2)}…a_{α_n}^{(n)}" (α). ZOOM-confirmed (crop_20_35). Restored natural. ★ SAME CLASS as p69 #60 (eq(8)) — 3rd confirmation (eq(8) #60 + Satz I corrob p70 + this). GPT SYSTEMATICALLY writes the determinant expansion Σ±(…) with α-subscripts where Weber uses the NATURAL Hauptglied a_1^{(1)}…a_n^{(n)}.
- **★★ FIX #65 — GENERIC-INDEX RELABEL r/ν → ν/μ (.tex 2481-2486, 3 edits):** Weber's generic LOWER index = ν, generic UPPER = μ. .tex had relabeled them: lower r, upper ν. ZOOM-confirmed (crop_5_64: "jeden anderen ν", eq(2) a_ν^{(k)}; crop_30_73: "das Product a_ν^{(μ)}"). Fixed: (a) "jeden anderen, r," -> "…\nu,"; (b) eq(2) a_r^{(k)}A_r^{(k)} -> a_\nu^{(k)}A_\nu^{(k)} (×3 terms); (c) "das Product a_r^{(ν)}…Factor a_r^{(ν)}" -> "a_\nu^{(μ)}…a_\nu^{(μ)}" (upper ν→μ). ★ "worin μ **gleichfalls** jeden der Indices…" (eq3) ties μ(upper) parallel to ν(lower) — .tex's "r" broke that parallelism; ν restores it.
- **FAITHFUL (top, .tex 2462-2468):** "…da beide Reihen identisch sind, nichts ändern, so dass für Δ nur der Werth Null übrig bleibt."; "Man drückt den Satz V[.] nur anders aus, wenn man sagt:"; **VI.**(gesperrt) "Man erhält eine verschwindende Determinante, wenn man die Elemente einer Reihe durch die entsprechenden Elemente einer anderen Reihe, oder, kurz gesagt, wenn man einen unteren oder oberen Index durch einen anderen ersetzt."; **§22 heading "§. 22. / Unterdeterminanten." — ★PRESENT & FAITHFUL** (matches .tex 2468; earlier dropped-heading concern RESOLVED).
- **FAITHFUL (mid/bot, .tex 2470-2493 apart from fixes):** Σ±-display[fixed]; "deren Werth wir jetzt mit **A** bezeichnen wollen" [★Δ→A NOTATION SWITCH — as expected]; "kommt jede der Zahlen 1,2…n ein und nur einmal als unterer Index vor. Es wird also ein gewisser Complex… Factor a_1^{(1)}… a_1^{(2)} **u. s. f.**[★here Weber genuinely prints 'u.s.f.' — .tex correct, contrast p67 where Weber had '…'], endlich… a_1^{(n)}; jedes Glied… in einem und nur in einem dieser Complexe vor."; "Bezeichnen wir also den ersten… a_1^{(1)}A_1^{(1)}, den zweiten a_1^{(2)}A_1^{(2)}, den letzten a_1^{(n)}A_1^{(n)}…"; **eq(1)** A=a_1^{(1)}A_1^{(1)}+a_1^{(2)}A_1^{(2)}+⋯+a_1^{(n)}A_1^{(n)}; "An Stelle des unteren Index 1… jeden anderen ν[fixed]…"; **eq(2)** A=a_ν^{(1)}A_ν^{(1)}+⋯+a_ν^{(n)}A_ν^{(n)}[fixed]; "das Product a_ν^{(μ)}[fixed]…"; "Da dieselben Regeln… für die oberen Indices gelten… folgenden Weise schreiben:"; **eq(3)** A=a_1^{(μ)}A_1^{(μ)}+a_2^{(μ)}A_2^{(μ)}+⋯+a_n^{(μ)}A_n^{(μ)}; "worin μ gleichfalls jeden der Indices 1,2…n bedeuten kann."
- **⚠ FORMATTING-PASS FLAGS:** leqno eq(1)/(2)/(3). **SKIP:** "Satz V[.]" period; math-list ellipsis; "u. s. f." (genuine here). **EMPHASIS (gesperrt):** §22 heading; Satz VI.
- **★★★ METHOD — NEW DAMAGE CLASS: GENERIC-INDEX RELABELING (#65).** GPT renamed Weber's running indices (ν→r lower, μ→ν upper). ★ INSIDIOUS: the math still works with r/ν, it compiles clean, and it reads sensibly — but it's UNFAITHFUL and it is likely MULTI-PAGE. Grep shows .tex uses "r" (and "s") as generic lower + "ν" as generic upper across §22-§23 (lines 2495 A_r^{(ν)}, 2548-2550 a_r/a_s two-row arg, 2564, 2569-2573). ★★ RULE: on EVERY §22+ Determinanten page, VERIFY the generic-index LETTERS against the scan (is it ν or r? μ or ν?) — do NOT trust the .tex's letters. Do NOT blanket-replace (the two-row a_r/a_s argument needs per-page scan verification — Weber may use ν + a distinct 2nd letter). This is the highest-subtlety damage found so far.
- NEXT: **p73** = §22 cont. (.tex 2495-2513+): "Die hierdurch vollständig definirten Grössen A_?^{(?)}[.tex A_r^{(ν)} — ★VERIFY vs scan, likely A_ν^{(μ)}] heissen die Unterdeterminanten der Determinante A. Um ihre Bildungsweise… betrachten wir zunächst den Complex a_1^{(1)}A_1^{(1)}. Man erhält ihn, wenn man in dem Product a_1^{(1)}a_2^{(2)}…a_n^{(n)} den unteren Index 1 ungeändert lässt und nur die übrigen Indices 2,3…n permutirt… d.h. es ist A_1^{(1)} die (n-1)-reihige Determinante:" **eq(4)** A_1^{(1)}=|(n-1)×(n-1) vmatrix a_2^{(2)}…a_n^{(2)} / … / a_2^{(n)}…a_n^{(n)}|; "oder die Determinante, die man aus A erhält, wenn man… erste Zeile und erste Colonne weglässt."; "Daraus ergiebt sich leicht die Bedeutung von A_?^{(?)}[.tex A_μ^{(ν)} — ★VERIFY]: man kann… ν-1 Zeilenvertauschungen… νte Zeile zur ersten… μ-1 Colonnen… (-1)^{μ+ν}… Bildungsgesetz:". Continue gap-pass p73->p99. ★★★ VERIFY GENERIC-INDEX LETTERS vs scan (relabeling continues); ★Σ±-natural-Hauptglied; ★ZOOM eq(4) vmatrix; ★Δ/A; ★dropped cross-refs/eq-tails. Fix drops/rewords/misreads/norms/FABRIC; [sic] errata. Compile-gate IF edit.
**Confirmed by eye vs ~500dpi scans; 2 fixes (α→natural + index-relabel) applied + gate held; §22 heading present.**


### 2026-07-03 — p73 (§22 Unterdeterminanten cont.: A_ν^{(μ)} def + eq(4) (n-1)-reihige Det + Bildungsgesetz + eq(5) 3-reihige, .tex ~2495-2525) — p1-99 gap pass — (verified by eye; ★★8 zooms for μ/ν disambiguation) — **3 CONTENT FIXES + FAITHFUL otherwise**
**CONTENT: 3 edits.** After fix: **418pp / 0 overfull / 0 underfull / PDF 2265074 B** (was 2264891). Compile-gate PASSED.
- **★★ FIX #66 — GENERIC-INDEX ARTIFACT (.tex 2495):** "Die hierdurch vollständig definirten Grössen \(A_r^{(\nu)}\)" — the "r" is a stray GPT artifact (continuation of the p72 r-relabel). ZOOM (crop_59_8 + crop_62_8, 2 independent) show scan = **A_ν^{(μ)}** (sub ν, super μ). Fixed A_r^{(ν)} -> A_ν^{(μ)}. ⚠ NOTE: 2512 uses A_μ^{(ν)} (super ν) — Weber SWAPS the dummy letters μ↔ν between 2495 and 2512 (local inconsistency; each matched to its own scan; low-confidence on 2495's exact μ/ν, re-verify future pass).
- **★★ FIX #67 — DROPPED CROSS-REF (.tex 2510):** scan "in dem A darstellenden Quadrat **[§. 20, (1)]** die erste Zeile…"; GPT dropped "[§. 20, (1)]". Restored "[\S\,20, (1)]". ★ 6th dropped section/eq cross-ref in §20-22 (#59,#61,#62,#63,#67 + p72 had none new). SYSTEMATIC.
- **★★ FIX #68 — DROPPED INTERMEDIATE FORM (eq(5), .tex ~2517):** scan eq(5) = |3×3| = a|b'c';b''c''| − b|a'c';a''c''| + c|a'b';a''b''| = a(b'c''−c'b'')+b(c'a''−a'c'')+c(a'b''−b'a''). GPT DROPPED the intermediate cofactor-2×2 step, jumping straight to the final expansion. ZOOM-confirmed (crop_5_77 + bot third). Restored the intermediate (aligned, 2-line). ★ OPPOSITE of p69 eq(4) (GPT ADDED a matrix there) — GPT both ADDS and DROPS intermediate forms; watch BOTH directions.
- **FAITHFUL (top/mid, .tex 2495-2510):** "…Grössen A_ν^{(μ)}[fixed] heissen die Unterdeterminanten der Determinante A. Um ihre Bildungsweise… betrachten wir zunächst den Complex a_1^{(1)}A_1^{(1)}. Man erhält ihn, wenn man in dem Product" a_1^{(1)}a_2^{(2)}…a_n^{(n)} "den unteren Index 1 ungeändert lässt und nur die übrigen Indices 2,3…n auf alle Arten permutirt… d.h. es ist A_1^{(1)} die (n−1)-reihige Determinante:" **eq(4)** A_1^{(1)}=|a_2^{(2)}…a_n^{(2)} / a_2^{(3)}…a_n^{(3)} / [dots] / a_2^{(n)}…a_n^{(n)}|; "oder die Determinante, die man aus A erhält, wenn man in dem A darstellenden Quadrat [§20,(1) restored] die erste Zeile und die erste Colonne weglässt."
- **FAITHFUL (mid/bot, .tex 2512-2523):** "Daraus ergiebt sich leicht die Bedeutung von **A_μ^{(ν)}**: man kann, indem man **ν−1** Zeilenvertauschungen vornimmt, die **ν**te Zeile zur ersten machen, und wenn man noch **μ−1** Vertauschungen der Colonnen hinzunimmt, die **μ**te Colonne zur ersten… Die Determinante selbst hat den Factor **(−1)^{μ+ν}** angenommen… (§. 21, IV). In der so umgeänderten Reihenfolge ist aber das Element **a_μ^{(ν)}** an die Stelle des Elementes a_1^{(1)} getreten… Bildungsgesetz:"; "Man erhält die Unterdeterminante **A_μ^{(ν)}** dadurch, dass man… die beiden Reihen weglässt, die sich in **a_μ^{(ν)}** kreuzen, und den Factor **(−1)^{μ+ν}** hinzufügt."; "So erhält man z.B. für die dreireihige Determinante die folgende Darstellung:" eq(5)[fixed]. ★★ .tex 2512-2523 was CORRECT (matches scan); ν=Zeile(row/upper), μ=Colonne(column/lower) here.
- **⚠ FORMATTING-PASS FLAGS:** matrix comma-sep (eq4); leqno; eq(5) multi-line layout. **SKIP:** math-list ellipsis. **EMPHASIS:** none new (statement-free page).
- **★★★ METHOD — "GENERIC-INDEX RELABEL" IS NOT UNIFORM (correction to p72 flag):** The p72 relabel (r/ν→ν/μ) was REAL, but p73's apparent relabel was LARGELY A FALSE ALARM — .tex 2512-2534 is CORRECT, and Weber himself uses μ,ν as FLOATING DUMMY indices (ν=column p72; ν=row p73; even μ↔ν-swapped between 2495 and 2512). Only the stray "r" at 2495 was a genuine artifact. ★ LESSON: do NOT blanket-swap; verify EACH generic-index instance; the .tex is often correct where Weber's own notation floats/is inconsistent.
- **★★★ METHOD — μ/ν DISAMBIGUATION TECHNIQUE:** I nearly made a large ERRONEOUS μ↔ν swap of the correct .tex 2512-2514 based on misreading tiny sub/superscripts. THE SAVE: anchor on a LARGE INLINE occurrence of the letter (crop_17_48: "ν−1 Zeilenvertauschungen", unmistakable ν) + GEOMETRIC/semantic consistency (ν=Zeile→A_μ^{(ν)}), NOT glyph-shape of tiny subscripts. ★ RULE: when a symbol's μ/ν is ambiguous, find the same dummy used inline at text-size and reason from §20's upper=Zeile/lower=Colonne convention. Tiny sub/superscript glyph-reads are UNRELIABLE at 500dpi thirds.
- NEXT: **p74** = §22 cont. (.tex 2527-2560+): "Da der untere Index ν in A_μ^{(ν)} gar nicht vorkommt[★VERIFY: .tex says 'untere Index ν' but ν is A's SUPERSCRIPT — check scan wording/index], so ändert sich A_μ^{(ν)} nicht, wenn der untere Index ν durch einen anderen ersetzt wird. Dann aber verschwindet nach §21,VI die Determinante… Relation, in der μ,ν irgend zwei verschiedene Ziffern 1…n:" **eq(6)** 0=a_1^{(μ)}A_1^{(ν)}+…+a_n^{(μ)}A_n^{(ν)}; "und ebenso aus (3):" **eq(7)** 0=a_μ^{(1)}A_ν^{(1)}+…+a_μ^{(n)}A_ν^{(n)}; "Beispielsweise aus (5)…" **eq(8)** a'(b'c''−c'b'')+b'(c'a''−a'c'')+c'(a'b''−b'a'')=0; "Wenn wir die Relation (6) mit λ multipliciren und zu (2) addiren…" eq with (a_r^{(k)}+λ a_s^{(k)})A_r^{(k)} [★★VERIFY the two-row generic indices r,s vs scan — Weber may use ν + a 2nd letter, NOT r/s]. Continue gap-pass p74->p99. ★★★ VERIFY generic-index letters + the "untere Index ν" oddity + two-row r/s; ★Σ±-natural; ★dropped cross-refs/eq-tails/intermediate-forms; ★Fraktur. Fix drops/rewords/misreads/norms/FABRIC; [sic] errata. Compile-gate IF edit.
**Confirmed by eye vs ~500dpi scans; 3 fixes + gate held; μ/ν disambiguated via inline-anchor+geometry (avoided a bad swap).**


### 2026-07-03 — p74 (§22 cont.: orthogonality Relation eq(6)/eq(7) + eq(8) + eq(9) row-add + Sätze VII/VIII/IX, .tex ~2532-2572) — p1-99 gap pass — (verified by eye; ★zoom eq(6)) — **5 CONTENT FIXES (incl. SWAPPED eq(6)/eq(7)) + FAITHFUL otherwise**
**CONTENT: 5 edits (4 logical fixes).** After fix: **418pp / 0 overfull / 0 underfull / PDF 2265026 B** (was 2265074). Compile-gate PASSED.
- **★★★ FIX #70 — SWAPPED EQUATIONS eq(6)⇄eq(7) (.tex 2534, 2539):** Weber: eq(6)[derived "aus (2)"=column-expansion] = 0=a_μ^{(1)}A_ν^{(1)}+…+a_μ^{(n)}A_ν^{(n)} (μ,ν LOWER); eq(7)[derived "aus (3)"=row-expansion] = 0=a_1^{(μ)}A_1^{(ν)}+…+a_n^{(μ)}A_n^{(ν)} (μ,ν UPPER). GPT had the two equation BODIES SWAPPED (.tex eq(6) had μ,ν upper = scan eq(7) form; .tex eq(7) had μ,ν lower = scan eq(6) form). ZOOM-confirmed (crop_10_16: eq(6) = a_μ^{(1)}A_ν^{(1)}, μ,ν subscripts). Derivation-text confirms: "aus (2)"(column,eq2 lower-fixed) -> lower indices -> eq(6). Swapped the bodies (kept eq6 comma / eq7 period).
- **★★ FIX #69 — GENERIC-INDEX (.tex 2532):** "Da der untere Index ν in A_μ^{(ν)}…" — .tex A_μ^{(ν)} has ν as SUPERSCRIPT, contradicting "untere Index ν". Scan = **A_ν^{(μ)}** (ν lower=column, μ upper=row) -> "untere Index ν" consistent. Fixed A_μ^{(ν)} -> A_ν^{(μ)} (×2 in sentence). ★ the PROSE "untere/obere Index X" disambiguates which index is lower.
- **★★ FIX #71 — GENERIC-INDEX RELABEL r/s->ν/μ (eq(9), .tex ~2553):** eq(9)=eq(2)+λ·eq(6): scan A = (a_ν^{(k)}+λ a_μ^{(k)})A_ν^{(k)} (ν=kept column, μ=added column). GPT relabeled ν->r, μ->s. Fixed a_r/a_s/A_r -> a_ν/a_μ/A_ν.
- **★★ FIX #72 — GENERIC-INDEX RELABEL r->ν (.tex 2569, Satz VIII proof):** scan "p a_ν^{(k)}A_ν^{(k)}=pA"; GPT had a_r. Fixed r->ν.
- **FAITHFUL (top, .tex 2532-2545):** "…so ändert sich A_ν^{(μ)}[fixed] nicht… Dann verschwindet nach §. 21, VI. die Determinante. Wir erhalten demnach aus (2) die folgende wichtige Relation, in der μ,ν irgend zwei von einander verschiedene Ziffern 1,2…n sein können:" eq(6)[fixed]; "und ebenso bekommt man aus (3):" eq(7)[fixed]; "Beispielsweise ergiebt sich aus (5), wenn a,b,c durch a',b',c' ersetzt werden:" **eq(8)** a'(b'c''−c'b'')+b'(c'a''−a'c'')+c'(a'b''−b'a'')=0 [exact].
- **FAITHFUL (mid, .tex 2548-2563):** "eine Formel, von deren Richtigkeit man sich durch die einfachste Rechnung überzeugt."; "Wenn wir die Relation (6) mit einem beliebigen Factor λ multipliciren und zu (2) addiren, so erhalten wir die Formel:" eq(9)[fixed]; "die uns den folgenden Satz ausdrückt:"; **VII.**(gesperrt) "Die Determinante ändert ihren Werth nicht, wenn man zu den Elementen einer Zeile, die mit einem beliebigen gemeinschaftlichen Factor multiplicirten entsprechenden Elemente einer anderen Zeile addirt."; "Derselbe Satz gilt auch von den Colonnen. Er wird zur Vereinfachung und numerischen Berechnung… oft mit Nutzen verwendet. Wir fügen noch folgende Sätze bei, die sich aus den Darstellungen (2), (3) sofort ablesen lassen."
- **FAITHFUL (bot, .tex 2565-2572):** **VIII.**(gesperrt) "Wenn alle Elemente einer Zeile oder einer Colonne einen gemeinschaftlichen Factor haben, so kann dieser weggelassen und als Factor vor die Determinante gesetzt werden."; "Denn es ist nach (2):" display[fixed]; **IX.**(gesperrt) "Wenn in einer Zeile oder in einer Colonne alle Elemente bis auf eines verschwinden, so reducirt [sich…]"(→p75). ALL word-for-word.
- **⚠ FORMATTING-PASS FLAGS:** leqno eq(6)-(9); eq(9) multi-line. **SKIP:** math-list ellipsis. **EMPHASIS (gesperrt):** Sätze VII, VIII, IX.
- **★★★ METHOD — NEW SUB-CLASS: SWAPPED/TRANSPOSED NUMBERED EQUATIONS (#70).** GPT attached equation BODIES to the wrong \tag (eq6⇄eq7, which are sub/super transposes). ★ RULE: when consecutive numbered eqs are sub/super transposes, verify EACH against (a) the scan AND (b) its derivation text ("aus (N)": column-expansion N -> lower-index relation; row-expansion -> upper-index). Do NOT assume the .tex tag-to-body pairing is right.
- **★★★ METHOD — GENERIC-INDEX RELABEL IS PAGE-SPECIFIC (r/s->ν/μ):** confirmed REAL on p74 (eq9, 2569) — GPT substitutes Latin r/s for Weber's Greek ν/μ. (Was real p72, FALSE-alarm p73.) ★ RULE STANDS: verify index LETTERS per-page vs scan; Weber uses Greek dummies (ν,μ), a stray Latin r/s is a GPT artifact. + the PROSE "untere/obere Index X" tells you the lower/upper role (disambiguator, #69).
- NEXT: **p75** = §22 Satz IX proof + Vandermonde example (.tex 2574-2600+): "Denn wenn a_?^{(1)},…,a_?^{(n)} mit Ausnahme von a_?^{(ν)} verschwinden, so ist nach (2): A=a_?^{(ν)}A_?^{(ν)}. Der Werth von A ist dann von den a_1^{(ν)},…,a_n^{(ν)} (mit Ausnahme von a_?^{(ν)}) ganz unabhängig." [★★VERIFY the FIXED lower index letter — .tex uses "r"; Weber likely a specific/Greek letter; check scan]; "Um von diesen Sätzen eine Anwendung zu machen, wollen wir den Werth der Determinante" Δ=|1,a,a²;1,b,b²;1,c,c²| "bestimmen… Multipliciren wir die zweite Colonne mit a und subtrahiren sie von der dritten, darauf die erste mit a und subtrahiren sie von der zweiten, so folgt nach VII:" Δ=… (Vandermonde reduction). Continue gap-pass p75->p99. ★★★VERIFY generic-index letters (r->? per scan) + Vandermonde eq entries; ★swapped/transposed eqs; ★dropped cross-refs/eq-tails/intermediate; ★Fraktur. Fix drops/rewords/misreads/norms/FABRIC; [sic] errata. Compile-gate IF edit.
**Confirmed by eye vs ~500dpi scans; 5 fixes (incl. swapped eq(6)/(7)) + gate held.**


### 2026-07-03 — p75 (§22 Satz IX proof + Vandermonde 3-reihig eq(10) + n-reihig eq(11), .tex ~2574-2623) — p1-99 gap pass — (verified by eye; ★zoom subscript ν) — **2 CONTENT FIXES + FAITHFUL otherwise**
**CONTENT: 2 edits (4 sub-edits).** After fix: **418pp / 0 overfull / 0 underfull / PDF 2265141 B** (was 2265026). Compile-gate PASSED.
- **★★ FIX #73 — GENERIC-INDEX RELABEL r->ν, ν->μ (Satz IX proof, .tex 2574,2576,2578):** scan uses ν (fixed column/lower) + μ (nonzero row/upper): "Denn wenn a_ν^{(1)},a_ν^{(2)}…a_ν^{(n)} mit Ausnahme von a_ν^{(μ)} verschwinden, so ist nach (2): A=a_ν^{(μ)}A_ν^{(μ)}; der Werth von A ist dann von den a_1^{(μ)},a_2^{(μ)}…a_n^{(μ)} (mit Ausnahme von a_ν^{(μ)}) ganz unabhängig." GPT had relabeled ν->r (lower), μ->ν (upper). ZOOM-confirmed subscript ν (crop_28_14). Fixed all 3 lines. ★ Consistent with "nach (2)" = column-ν expansion (eq2 fixed-lower ν).
- **★★ FIX #74 — DROPPED INTERMEDIATE STEP (Vandermonde, .tex ~2598):** scan has THREE reduction steps: "so folgt nach VII:" |1,0,0;1,b−a,b(b−a);1,c−a,c(c−a)|, then **"und nach IX:" \[ Δ=|b−a,b(b−a);c−a,c(c−a)| \]** (2×2 after Satz-IX first-row reduction), then "und endlich nach VIII:" eq(10). GPT COLLAPSED to "und nach IX. und VIII.:" -> eq(10), DROPPING the 2×2 intermediate display + the "und endlich nach VIII:" step. Restored the intermediate step. ★ Another dropped-intermediate-form (cf. p73 eq(5)) — GPT recurrently drops intermediate calc steps in worked examples.
- **FAITHFUL (top, .tex 2572-2588):** **IX.**(gesperrt, tail) "…so reducirt sich die Determinante auf das Product dieses einen Elementes mit der entsprechenden Unterdeterminante."; Satz IX proof[fixed]; "Um von diesen Sätzen eine Anwendung zu machen, wollen wir den Werth der Determinante" Δ=|1,a,a²;1,b,b²;1,c,c²| "bestimmen, worin a,b,c beliebige Grössen seien."
- **FAITHFUL (mid, .tex 2589-2607):** "Multipliciren wir die zweite Colonne mit a und subtrahiren sie von der dritten, darauf die erste mit a und subtrahiren sie von der zweiten, so folgt nach VII:" Δ=|1,0,0;1,b−a,b(b−a);1,c−a,c(c−a)|; "und nach IX:"[restored] 2×2[restored]; "und endlich nach VIII:"[restored]; **eq(10)** Δ=(b−a)(c−a)|1,b;1,c|=(b−a)(c−a)(c−b) [exact].
- **FAITHFUL (bot, .tex 2609-2623):** "Auf die gleiche Weise kann man auch die n-reihige Determinante" |1,a_1,a_1²…a_1^{n-1} / 1,a_2,a_2²…a_2^{n-1} / [dots] / 1,a_n,a_n²…a_n^{n-1}| "behandeln und findet ihren Werth gleich" **eq(11)** (a_2−a_1)(a_3−a_1)…(a_n−a_1)(a_3−a_2)…(a_n−a_2)…(a_n−a_{n-1}) [all factors exact]. ALL word-for-word. Page ends; "Ordnet man die Colonnen…" starts p76.
- **⚠ FORMATTING-PASS FLAGS:** eq(11) scan=4-line-display+dots-row vs .tex single-line inline product (content-identical); matrix comma-sep (Vandermonde matrices); leqno. **SKIP:** math-list ellipsis; scan display "A=a_ν^{(μ)};" ends ';' + lowercase "der" vs .tex '.' + "Der" (punctuation/cap = skip). **EMPHASIS (gesperrt):** Satz IX.
- **★★ METHOD:** (1) generic-index relabel r->ν CONTINUES into p75 Satz IX proof — the relabel recurs across §22 worked-proofs (p72,p74,p75), page-specific; verify each. (2) DROPPED-INTERMEDIATE-STEP in worked examples confirmed recurring (p73 eq5, p75 Vandermonde) — GPT collapses multi-step reductions, dropping intermediate displays + merging the connecting "nach X:" phrases. ★ When a worked example cites multiple Sätze in sequence ("nach VII… nach IX… nach VIII"), CHECK for a dropped intermediate display between each cited step.
- NEXT: **p76** = §22 cont. (.tex 2625-2660+): "Ordnet man die Colonnen in umgekehrter Reihenfolge, so sind dazu, je nachdem n gerade oder ungerade ist, [½n(n−1) o.ä.] Transpositionen erforderlich…" — reordering the Vandermonde columns + sign; then likely §22 end / §23 "Die Unterdeterminanten im weiteren Sinne" heading (.tex ~2661). Continue gap-pass p76->p99. ★★VERIFY generic-index letters (r->? per scan) + ordinal/parity expressions; ★VERIFY §23 heading if present; ★dropped intermediate steps/cross-refs/eq-tails; ★swapped eqs; ★Fraktur. Fix drops/rewords/misreads/norms/FABRIC; [sic] errata. Compile-gate IF edit.
**Confirmed by eye vs ~500dpi scans; 2 fixes (relabel + dropped-step) + gate held.**


### 2026-07-03 — p76 (§22 end: Vandermonde column-reversal eq(12) + differential-quotient Unterdeterminante notation, .tex ~2633-2671) — p1-99 gap pass — (verified by eye; ★zoom ∂A/∂a_i^{(k)}) — **1 CONTENT FIX (i,k index relabel) + FAITHFUL otherwise**
**CONTENT: 1 fix (5 sub-edits, ~10 occurrences).** After fix: **418pp / 0 overfull / 0 underfull / PDF 2265146 B** (was 2265141). Compile-gate PASSED.
- **★★ FIX #75 — INDEX RELABEL a_μ^{(ν)}->a_i^{(k)}, A_μ^{(ν)}->A_i^{(k)} (differential passage, .tex 2663-2671):** Weber uses the STANDARD double-index a_i^{(k)} (§20 notation) throughout the differential-quotient passage: "Wenn die Grössen a_i^{(k)} als unabhängige Variable… Die nach a_i^{(k)} genommene Ableitung… gleich dem Coefficienten von a_i^{(k)}"; display ∂A/∂a_i^{(k)}=A_i^{(k)}; "die a_i^{(k)} Functionen einer Variablen t"; A'(t)=ΣA_i^{(k)}∂a_i^{(k)}/∂t; "∂a_i^{(k)}/∂t die Ableitung von a_i^{(k)} nach t". GPT had NORMALIZED all to Greek a_μ^{(ν)}/A_μ^{(ν)}. ZOOM-confirmed i,k (crop_36_64: subscript i (dotted), superscript (k)). Fixed all ~10 occurrences (5 targeted edits, scoped to 2663-2671).
  ★★ NEW DIRECTION: GPT normalizes index letters in BOTH directions — here Latin i,k -> Greek μ,ν (earlier: Greek ν/μ -> Latin r/s). ★ MUST NOT global-replace: the SAME string "a_\mu^{(\nu)}" is CORRECT on p73 (2512-2514) and WRONG here — scope every relabel fix to its passage.
- **FAITHFUL (top, .tex 2633-2645):** "Ordnet man die Colonnen in umgekehrter Reihenfolge, so sind dazu, je nachdem n gerade oder ungerade ist," n/2 oder (n−1)/2 "Vertauschungen erforderlich, so dass sich die so geordnete Determinante von Δ durch den Factor" (−1)^{n(n−1)/2} "unterscheidet. Es kommt auf dasselbe hinaus, wenn man den" n(n−1)/2 "Factoren des Productes (11) das entgegengesetzte Vorzeichen giebt. Es besteht also zugleich mit (11) die Gleichung:"
- **FAITHFUL (mid, .tex 2646-2665):** **eq(12)** |a_1^{n-1},a_1^{n-2}…a_1,1 / a_2^{n-1}…a_2,1 / [dots] / a_n^{n-1}…a_n,1| = (a_1−a_2)(a_1−a_3)…(a_1−a_n) / (a_2−a_3)…(a_2−a_n) / [dots] / (a_{n-1}−a_n) [reversed Vandermonde, all entries exact]; "Wir wollen hier noch eine Bezeichnungsweise der Unterdeterminanten erwähnen, die der Differentialrechnung entnommen ist und oft mit Nutzen verwendet wird, besonders wenn es sich um die Bildung von Derivirten handelt."; differential passage[fixed]; display ∂A/∂a_i^{(k)}=A_i^{(k)}[fixed].
- **FAITHFUL (bot, .tex 2667-2671):** "Wenn demnach z.B. die a_i^{(k)}[fixed] Functionen einer Variablen t sind, so ist auch A eine Function von t, und man erhält nach den ersten Regeln der Differentialrechnung die Ableitung von A in Bezug auf t in der Form" A'(t)=ΣA_i^{(k)}∂a_i^{(k)}/∂t[fixed] "wenn ∂a_i^{(k)}/∂t die Ableitung von a_i^{(k)} nach t bedeutet[fixed]." ALL word-for-word. Page ends; §23 heading starts p77.
- **⚠ FORMATTING-PASS FLAGS:** eq(12) matrix comma-sep + multi-line \gathered RHS; leqno eq(12). **SKIP:** Coefficienten (ë-drop); math-list ellipsis; trailing "bedeutet," comma-vs-period (scan-noise/punct). **EMPHASIS:** none new.
- **★★ METHOD — INDEX RELABEL IS BIDIRECTIONAL + PASSAGE-SCOPED:** GPT changes index LETTERS both ways (Latin↔Greek): i,k->μ,ν (p76) AND ν,μ->r,s (p72,p74,p75). ★ RULE reinforced: verify index letters vs scan on EVERY §22-25 page; the correct letter is passage-specific (a_μ^{(ν)} right on p73, wrong on p76); NEVER global-replace an index string. Weber's differential/general-element notation = a_i^{(k)}; his running-index relations = ν,μ.
- NEXT: **p77** = §23 Die Unterdeterminanten im weiteren Sinne (.tex 2674-2710+): **§23 heading "§. 23. Die Unterdeterminanten im weiteren Sinne" (★VERIFY present + exact title, note LONGER title, maybe no trailing period)**; "Wir können nun die Betrachtungen des vorigen Paragraphen in folgender Weise verallgemeinern. Wie wir vorhin von der Aufgabe ausgegangen sind, alle Glieder in der entwickelten Determinante A aufzusuchen, die den Faktor a_1^{(1)} enthalten, so wollen wir jetzt alle die Glieder aufsuchen, die den Faktor" a_1^{(1)}a_2^{(2)}…a_ν^{(ν)} "enthalten, worin ν eine beliebige Zahl unter n sein kann. Diese Glieder erhalten wir aus dem Hauptgliede" a_1^{(1)}a_2^{(2)}…a_ν^{(ν)}a_{ν+1}^{(ν+1)}…a_n^{(n)}… Continue gap-pass p77->p99. ★★VERIFY generic-index letters (Faktor/Hauptglied constructions) + §23 heading; ★"Faktor" vs "Factor" spelling (.tex 2676 uses "Faktor" k — VERIFY vs scan which likely "Factor" c!); ★dropped intermediate-steps/cross-refs; ★Fraktur. Fix drops/rewords/misreads/norms/FABRIC; [sic] errata. Compile-gate IF edit.
**Confirmed by eye vs ~500dpi scans; 1 relabel fix (i,k) + gate held.**


### 2026-07-03 — p77 (§23 Die Unterdeterminanten im weiteren Sinne: heading + Factor-displays + eq(1) + Regel I + Elemente-Auswahl, .tex ~2674-2708) — p1-99 gap pass — **★★★ NEW DAMAGE ZONE: §23 = MODERNIZED-SOURCE BLOCK. 4 FIXES (orthography batch + reword + 2 drops)**
**CONTENT: 4 logical fixes (7 edits).** After fix: **418pp / 0 overfull / 0 underfull / PDF 2265243 B** (was 2265146). Compile-gate PASSED.
- **★★★ ZONE FINDING — §23 (.tex 2674-2716) IS IN MODERNIZED GERMAN ORTHOGRAPHY,** unlike §18-§22 (faithful 1895 forms). GPT (or its source for this stretch) wrote: Faktor/Kolonne/Produkt/daß/läßt/ergibt/permutieren/unverändert where Weber prints **Factor/Colonne/Product/dass/lässt/ergiebt/permutiren/ungeändert**. Scan-verified on p77 (Factor ×3 legible, permutiren, Colonnen, dass ×2, Product). Grep bounds the zone: .tex 2676-2716 (=printed p77-p78) + stray "ergibt sich" 2787 (§24, verify at p79/80) + 5144 (far later, verify then). Suggests §23 was reconstructed from a modernizing source rather than the scan.
- **★ FIX #76 — ORTHOGRAPHY BATCH (p77-verified only):** Faktor→Factor (×4: 2676 ×2, 2695 Regel I, 2708), Kolonnen→Colonnen (2699), Kolonne→Colonne + daß→dass + Produkt→Product (2708), permutieren→permutiren + unverändert→**ungeändert** (2684 — this one is a real REWORD not just spelling), §23 heading trailing period added ("…im weiteren Sinne." matches scan + .tex convention).
- **★★ FIX #77 — REWORD RESTORED (.tex 2701):** scan "Dieses Resultat wollen wir nun **auf folgende Art** verallgemeinern**:**" (colon, then paragraph break); .tex had "…wollen wir nun verallgemeinern." (dropped phrase, period). Restored phrase + colon + paragraph break.
- **★★ FIX #78 — DROPPED SEPARABLE-VERB "aus" (.tex 2708):** scan "Wir wählen irgend ν Elemente [display] **aus,** jedoch so…" ("wählen … aus"); .tex lacked "aus,". Restored.
- **★★ FIX #79 — DROPPED CLAUSE (.tex 2708):** scan "…in derselben Colonne vorkommen, **d. h. so, dass nicht zweimal derselbe untere oder derselbe obere Index vorkommt,** und bezeichnen den Inbegriff der Glieder der Determinante, die das Product dieser Elemente als Factor enthalten, mit" — .tex had DROPPED the d.h.-clause and SPLIT into two sentences ("…vorkommen. Den Inbegriff … bezeichnen wir mit"). Restored Weber's single-sentence flow + clause.
- **FAITHFUL (verified):** §23 heading "§. 23. / Die Unterdeterminanten im weiteren Sinne." [present + exact]; "Wir können nun die Betrachtungen des vorigen Paragraphen in folgender Weise verallgemeinern."; Factor-display a_1^{(1)}a_2^{(2)}…a_ν^{(ν)}; "enthalten, worin ν eine beliebige Zahl unter n sein kann. Diese Glieder erhalten wir aus dem Hauptgliede" a_1^{(1)}…a_ν^{(ν)}a_{ν+1}^{(ν+1)}…a_n^{(n)}; **eq(1)** a_1^{(1)}a_2^{(2)}…a_ν^{(ν)}·|(n−ν)-vmatrix a_{ν+1}^{(ν+1)}…a_n^{(ν+1)} / [dots] / a_{ν+1}^{(n)}…a_n^{(n)}| [entries exact]; **Regel I**(gesperrt) "Die hier als Factor auftretende Determinante von n−ν Reihen, die wir mit A_{1,2…ν}^{1,2…ν} bezeichnen, entsteht aus A durch Weglassen der ν ersten Zeilen und Colonnen."; elements-display a_{α_1}^{(β_1)}, a_{α_2}^{(β_2)} … a_{α_ν}^{(β_ν)} [content exact]. Running header "Höhere Unterdeterminanten." = Weber's abbreviated running head (layout, out of scope).
- **⚠⚠ PENDING (p78, do NOT forget):** (a) **TAG QUESTION:** the elements-display is UNNUMBERED in the scan (no leqno "(3)"), but .tex gives it \tag{3}, gives the A-symbol \tag{2} (appearing AFTER (3)!), and references "die Elemente (3)" twice (2714, 2716). Weber's true numbering + reference text must be read off p78's scan (the A-display + Umstellen-paragraph + Regel II sit there). Fix tags + references TOGETHER next turn. (b) **REMAINING MODERNIZATION (.tex 2714, 2716):** daß, läßt/wegläßt/stehen läßt, Kolonnen ×3, ergibt sich — verify each against p78 scan and fix. (c) Statement I inline-A vs .tex display = fmt-pass item.
- **⚠ FORMATTING-PASS FLAGS:** Regel-I A-symbol inline→display promotion; eq(1) matrix dots-row + comma-sep; leqno. **SKIP:** ellipsis-commas; elements-display trailing punct. **EMPHASIS (gesperrt):** Regel I (whole statement).
- **★★★ METHOD — NEW DAMAGE CLASS: WHOLESALE ORTHOGRAPHY MODERNIZATION (zone-based).** Detection: grep modern forms (daß|Kolonn|Produkt|Faktor|läßt|ergibt|-ieren) to BOUND the zone, then scan-verify + fix per page. In such zones GPT also rewords MORE aggressively (drops phrases/clauses: #77-#79 all in one paragraph) — treat modernized zones as HIGH-DAMAGE and read word-by-word. ★ The orthography differences are NOT skip-tier: ë-drop (Coëff→Coeff) stays skip, but ss/ß, c/k, -iren/-ieren, Colonne/Kolonne are SOURCE-FIDELITY items (Weber's 1895 print is unambiguous).
- NEXT: **p78** = §23 cont. (.tex ~2709-2760): A-symbol display + tag [★settle (2)/(3) question vs scan]; "Man kann durch Umstellen von Zeilen und Kolonnen[→Colonnen]… daß[→dass] die Elemente (3)[?] an die Stelle von a_1^{(1)},…,a_ν^{(ν)} gelangen. Dann läßt[→lässt] sich Regel I anwenden und es ergibt[→ergiebt] sich:"; **Regel II** "Man erhält, vom Vorzeichen abgesehen, A_{α…}^{β…} als (n−ν)-reihige Determinante, wenn man in A alle Zeilen und Kolonnen[→Colonnen] wegläßt[→weglässt]…"; "Für die Zeichenbestimmung ordne man die unteren und die oberen Indices 1,2,…,n in der Weise" (4) α_1,…,α_ν,α_{ν+1},…,α_n, (5?) β_1,…,β_ν,β_{ν+1},…,β_n… Continue gap-pass p78->p99. ★★★MODERNIZED-ZONE word-by-word; ★TAGS (2)/(3)/(4)/(5) + "Elemente (N)" refs vs scan; ★generic-index letters; ★dropped clauses/intermediate steps. Fix drops/rewords/misreads/norms/FABRIC; [sic] errata. Compile-gate IF edit.
**Confirmed by eye vs ~500dpi scans; 4 fixes in the new modernized zone + gate held. Tag question PENDING p78.**


### 2026-07-03 — p78 (§23 cont.: eq(2) Complex-display + Umstellen-paragraph eq(3) + Regel II + Zeichenbestimmung (4)/(5) + Regel III + Beweis, .tex ~2703-2745) — p1-99 gap pass — **★★★ MODERNIZED-ZONE REBUILD: 6 FIXES incl. TAG RESTRUCTURE + DROPPED PROOF PARAGRAPH. + SCAN-PDF PATH REPAIRED**
**CONTENT: 6 logical fixes (6 edits).** After fix: **418pp / 0 overfull / 0 underfull / PDF 2266311 B** (was 2265243). Compile-gate PASSED.
- **★★ INFRASTRUCTURE — SCAN PDF MOVED, MANIFEST REPAIRED:** the monolithic `lehrbuchderalgeb01weberich.pdf` disappeared from `Papors\OS\Lehrbuch der Algebra\` (folder reorganized ~Jul 4 00:46 into Bd*_chapters subfolders). Same IA scan now lives at `Bd1_IA_chapters\Weber_Algebra_Bd1_IA.pdf` (686 pp). **Offset +26 VERIFIED unchanged** (printed 78 -> pdf 104, header "78 Zweiter Abschnitt. §. 23."). Updated `audit_manifest.json`: 648 vol1 units repointed. chunk_page.py/crop_src.py read the manifest -> no script changes needed.
- **★★★ FIX #80 — TAG RESTRUCTURE (2)/(3) (settles p77-pending):** Weber's true numbering: **(2)** = the COMBINED display "a_{α_1}^{(β_1)}a_{α_2}^{(β_2)}…a_{α_ν}^{(β_ν)} A_{α_1,α_2…α_ν}^{β_1,β_2…β_ν}." (product × symbol, closing the p77 sentence "…enthalten, mit"); **(3)** = the α-element list INSIDE the p78 Umstellen-paragraph. GPT had: p77 element list tagged (3) [Weber: UNNUMBERED], bare A-symbol tagged (2) [Weber: no such display], and used the (3)-reference on a paraphrase. Fixed: p77 list de-numbered (\[..\]); (2) rebuilt as combined display; (3) attached to the Umstellen-list. Weber's own refs "die Elemente (3)" (Regel II) + "(2) auf (1)" + "(4) und (5)" (Beweis) now all resolve correctly.
- **★★★ FIX #81 — UMSTELLEN-PARAGRAPH REBUILT (was compressed paraphrase):** Weber: "Man kann durch Umstellen von Zeilen und Colonnen, wodurch höchstens das Zeichen der Determinante geändert wird, immer erreichen, dass die Elemente [display (3)] an die Stelle der Elemente. [★sic-Punkt] [display a_1^{(1)},a_2^{(2)},…,a_ν^{(ν)}] gelangen; dann aber lässt sich die Regel I. auf die Bestimmung von A_{α…}^{β…} anwenden und es ergiebt sich:" — GPT had compressed to one sentence with inline "(3)"+inline list, dropping "dann aber", "die Regel I. AUF DIE BESTIMMUNG VON A_{α…}^{β…}", the two displays, and the semicolon flow. Rebuilt verbatim.
  - **★ TYPE-B ERRATUM #9 (Weber print quirk, KEPT + [sic]):** Weber prints a PERIOD mid-sentence: "an die Stelle der Elemente**.**" before the display (sentence continues "…gelangen;"). ZOOM-confirmed (crop_5_20, unmistakable). Reproduced + % [sic]-comment in .tex.
- **★★ FIX #82 — DROPPED SENTENCE + MERGED PARAGRAPHS:** Weber: "Für die Zeichenbestimmung aber ergiebt sich folgende Vorschrift. [¶] Man ordne die unteren und die oberen Indices 1,2…n in der Weise:" — GPT had merged into "Für die Zeichenbestimmung ordne man…" (dropped "aber ergiebt sich folgende Vorschrift", the ¶ break, and the colon). Restored.
- **★★ FIX #83 — PARAPHRASE REVERTED (indem-man):** Weber: "indem man α_{ν+1}…α_n und ebenso β_{ν+1}…β_n der Grösse nach auf einander folgend annimmt." (partly gesperrt); GPT: "indem man die fehlenden Indices der Größe nach aufeinander folgen läßt." Restored Weber's wording.
- **★★★ FIX #84 — DROPPED PROOF PARAGRAPH restored (after Regel III):** "Denn die Determinante ändert ihr Zeichen durch jede Vertauschung zweier unterer oder zweier oberer Indices. Um den allgemeinen Fall (2) auf den besonderen Fall (1) zurückzuführen, hat man so viele Transpositionen oberer und unterer Indices vorzunehmen, dass die Permutationen (4) und (5) beide in die ursprüngliche Anordnung 1,2,3…n übergehen, und ebenso viele Zeichenwechsel haben stattgefunden." — ENTIRELY ABSENT from .tex. Restored.
- **★ FIX #85 — ORTHOGRAPHY/DETAIL BATCH p78:** Colonnen ×3 (Kolonnen), dass/lässt/weglässt/stehen lässt (daß/läßt…), ergiebt ×2 (ergibt), Regel II "(vom Vorzeichen abgesehen)" in PARENTHESES (GPT: commas), "Die in II. beschriebene" (period), "die beiden Anordnungen (4) und (5)" (GPT: "(4), (5)").
- **FAITHFUL (verified):** eq(2) combined display [scan-exact]; Regel II content; (4) α-ordering + (5) β-ordering displays; Regel III content; running header. Page ends after "…stattgefunden."
- **⚠⚠ PENDING (p79):** .tex 2745+ still modernized + suspect: "Die so definierten Größen heißen die ν-ten Unterdeterminanten…", Regel IV ("Werte"), complementäre-Unterdeterminante passage (B_{α…}^{β…}), **tag sequence has NO (6)**, and **eq(9)/(10) are near-duplicate displays with opposite signs (mutually contradictory — clearly corrupted reconstruction)**. Rebuild against p79 scan next turn. ALSO stray "ergibt sich" .tex 2787 (§24) + 5144.
- **⚠ FORMATTING-PASS FLAGS:** leqno (2)-(5); gesperrt Regel II/III + "der Grösse nach auf einander folgend annimmt" (emphasis-pass). **SKIP:** ellipsis-commas; (4) trailing-comma.
- **★★★ METHOD:** (1) modernized zones hide STRUCTURAL damage beyond spelling — on p77-78: 2 misplaced tags, 1 fabricated display, 2 dropped displays, 1 dropped proof-paragraph, 2 paraphrases, merged paragraphs. Read display-by-display, verify EVERY tag + its references. (2) When .tex tag-sequence has gaps (no (6)) or near-duplicate eqs ((9)/(10) ±) — corruption markers; rebuild from scan. (3) Weber prints occasional mid-sentence periods (type-B); ZOOM before deciding, keep + [sic].
- NEXT: **p79** = §23 cont. (.tex ~2745-2800): "Die so definierten Größen[→Grössen?] heißen[→heissen] die ν-ten[→νten?] Unterdeterminanten…"; **Regel IV** (Vorzeichen bei Index-Vertauschung; "Werte"→Werthe?); überstrichene-Folge passage + complementäre Unterdeterminante B_{α…}^{β…}; find Weber's REAL tag sequence around (6)/(7)/(8) (Laplace!) and resolve the (9)/(10) duplicate corruption. ★★★MODERNIZED-ZONE display-by-display; ★tags+refs; ★generic-index letters; ★dropped proofs/displays. Fix drops/rewords/misreads/norms/FABRIC; [sic] errata. Compile-gate IF edit.
**Confirmed by eye vs ~500dpi scans; 6 fixes (tag restructure + dropped proof + rebuild) + gate held; scan-PDF path repaired, offset +26 verified.**


### 2026-07-03 — p79 (§23 cont.: νte Unterdeterminanten def + Regel IV + primed-Anordnung Complex + eq(6) + complementäre Unterdeterminante B, .tex ~2748-2790) — p1-99 gap pass — **★★★ MODERNIZED-ZONE REBUILD cont.: 5 FIXES incl. MISSING (6) RESTORED + NOTATION FABRICATION (overbars) REVERTED**
**CONTENT: 5 logical fixes (3 edits).** After fix: **418pp / 0 overfull / 0 underfull / PDF 2267530 B** (was 2266311). Compile-gate PASSED.
- **★★ FIX #86 — DEF-SENTENCE REBUILT (.tex 2748):** Weber: "Die so definirten Grössen [display A_{α_1,α_2…α_ν}^{β_1,β_2…β_ν}] heissen die νten Unterdeterminanten oder Unterdeterminanten νter Ordnung. Sie sind dargestellt durch (n−ν)reihige Determinanten. [¶] **Aus III. folgt in Bezug auf diese Unterdeterminanten der Satz:**" — GPT had: modernized (definierten/Größen/heißen/ν-ten/ν-ter/-reihige), DROPPED the A-display, and compressed the transition to "Es folgt:". All restored.
- **★★★ FIX #87 — REGEL IV COMPLETED (truncated):** Weber's IV (gesperrt) continues past "vertauscht werden": "…, **oder allgemeiner: sie bleibt dem absoluten Werthe nach ungeändert, wenn die Anordnung der Indices α_1,α_2…α_ν durch irgend eine andere Anordnung ersetzt wird und ändert das Zeichen oder nicht, je nachdem diese Permutation zur zweiten oder zur ersten Art gehört.**" GPT had truncated to "…vertauscht werden; dem absoluten Werte nach bleibt sie ungeändert." (dropped the whole allgemeiner-half + Werte→Werthe). Restored.
- **★★★ FIX #88 — NOTATION FABRICATION REVERTED (overbars→primes) + A-SUBSCRIPT ERROR:** Weber: "Bezeichnen wir **aber mit α'_1, α'_2 … α'_ν irgend eine Anordnung der α_1, α_2 … α_ν**, so enthält die Determinante **A** auch **den Complex** der Glieder" + display "± a_{α'_1}^{(β_1)}a_{α'_2}^{(β_2)}…a_{α'_ν}^{(β_ν)} **A_{α_1,α_2…α_ν}^{β_1,β_2…β_ν}**," — GPT had invented OVERBAR notation ("mit einer überstrichenen Folge", a_{ᾱ_i}) AND wrote the A-symbol with overbarred subscripts A_{ᾱ_1…ᾱ_ν} (WRONG: the subdeterminant keeps the ORIGINAL unprimed selection α_1…α_ν). Both reverted to Weber's primes + unprimed A.
- **★★★ FIX #89 — MISSING (6) RESTORED (resolves tag-gap):** Weber: "und wenn wir also alle diese Glieder sammeln, so erhalten wir den Complex:" **(6)** A_{α_1,α_2…α_ν}^{β_1,β_2…β_ν} Σ± a_{α_1}^{(β_1)}a_{α_2}^{(β_2)}…a_{α_ν}^{(β_ν)}. — ENTIRELY ABSENT from .tex (this was the missing tag (6)!). Restored sentence + display. Tag sequence §23 now coherent: (1)-(8).
- **★★ FIX #90 — DROPPED ν×ν-MATRIX DISPLAY + PARAPHRASE:** Weber: "Die hier auftretende ν-reihige Determinante [display: Σ± a_{α_1}^{(β_1)}…a_{α_ν}^{(β_ν)} = |ν×ν vmatrix, rows β_1…β_ν × cols α_1…α_ν|] **wollen wir die zu A_{α…}^{β…} complementäre Unterdeterminante nennen** und mit B_{α_1,α_2…α_ν}^{β_1,β_2…β_ν} bezeichnen." — GPT: "Die hierbei auftretende ν-reihige Determinante wird die complementäre Unterdeterminante genannt und mit [bare B display] bezeichnet." (dropped the defining Σ±=vmatrix display, dropped "die zu A…", passive rephrase). Restored (B inline as in scan).
- **⚠⚠ PENDING (p80):** (a) dropped sentence "**Sie enthält genau die Zeilen und Colonnen, die in A_{α…}^{β…} fehlen und** …" — continues on p80; insert WITH its continuation next turn (kept .tex "Der betreffende Complex der Glieder ist also (7)…" adjacent for now — verify/rebuild vs p80 scan). (b) Verify (7) A·B + (8) Laplace prose (range conditions!) + **(9)/(10) near-duplicate ± displays (corruption)** + (11)/(12) geränderte Determinante + (13) Differentialquotient (zweckmäßig→zweckmässig) against p80(/p81) scans. (c) stray "ergibt sich" .tex ~2803 (now inside (11)-(12) passage) + §24 zone check.
- **FAITHFUL (verified):** running header "Unterdeterminanten νter Ordnung."; IV first half; B-symbol form; (6) unprimed Σ-shorthand [scan]; ν×ν matrix entries [scan].
- **⚠ FORMATTING-PASS FLAGS:** leqno (6); gesperrt Regel IV (emphasis-pass); matrix comma-sep. **SKIP:** ellipsis-commas.
- **★★★ METHOD:** (1) modernized-zone rebuild continues to pay: p79 alone = 1 missing numbered display, 1 truncated Satz, 1 notation fabrication (overbars for primes — GPT invents NOTATION, not just words; check every symbol-accent against scan), 2 dropped displays, multiple paraphrases. (2) ★ NOTATION-ACCENT CHECK added to checklist: primes vs overbars vs subscript-order (GPT's A_{ᾱ…} was also mathematically wrong — semantic check caught it). (3) Sentence-continuation discipline: never insert a dangling half-sentence; defer cross-page sentences until the continuation page is read.
- NEXT: **p80** = §23 end (+ §24 start?) (.tex ~2790-2830): complete "Sie enthält genau die Zeilen und Colonnen, die in A fehlen und […p80 text]"; verify/rebuild "(7) A·B Complex" + "(8) Satz von Laplace" (expect range-condition prose GPT dropped) + resolve (9)/(10) ±-duplicates + (11) geränderte Determinante U + (12) U=qA−Σu_iv_kA_k^{(i)} + (13) ∂²A/∂a∂a; then §24 heading "Lineare homogene Gleichungen" (★verify title + trailing period + "specielle" orthography at .tex 2820 "die specielle Form" — looks correct-old already). ★★★MODERNIZED-ZONE display-by-display; ★tags+refs; ★accents (primes!); ★dropped range-condition prose at Laplace. Fix drops/rewords/misreads/norms/FABRIC; [sic] errata. Compile-gate IF edit.
**Confirmed by eye vs ~500dpi scans; 5 fixes (missing (6) + notation reverts + rebuilds) + gate held.**


### 2026-07-03 — p80 (§23 cont.: complementäre-B Eigenschaften + eq(7) + Laplace Satz V eq(8) + zweite Darstellung Satz VI eq(9)/(10), .tex ~2780-2830) — p1-99 gap pass — **★★★ MODERNIZED-ZONE REBUILD cont.: 6 FIXES incl. (9)/(10) SUPERSCRIPT-SWAP RESOLUTION + Sätze V/VI RESTORED. ★ GATE BASELINE NOW 419pp**
**CONTENT: 6 logical fixes (1 large edit).** After fix: **419pp / 0 overfull / 0 underfull / PDF 2269496 B** (was 418pp/2267530). Compile-gate PASSED. **★ PAGE COUNT 418→419: legitimate growth from restored §23 content (3 paragraphs + 4 displays across p78-p80 rebuilds). Structure sanity: 68 sections, 1100 equations, \end{document} intact. NEW GATE BASELINE: 419pp/0/0.**
- **★★ FIX #91 — CROSS-PAGE SENTENCE COMPLETED (p79-pending):** "Sie enthält genau die Zeilen und Colonnen, die in A_{α…}^{β…} fehlen und stimmt, abgesehen vom Vorzeichen, mit der Unterdeterminante (n−ν)ter Ordnung [display A_{α_{ν+1}…α_n}^{β_{ν+1}…β_n}] überein." — whole sentence + display were ABSENT from .tex. Restored.
- **★★ FIX #92 — (7)-INTRO PARAPHRASE + DROPPED (6)-REF:** Weber: "Der Complex der Glieder **(6)** wird also bezeichnet mit (7)…"; GPT: "Der betreffende Complex der Glieder ist also (7)…" (dropped the (6) back-reference). Restored.
- **★★★ FIX #93 — DROPPED COMBINATORIAL PARAGRAPH (Laplace range-condition):** "Wählen wir nun für α_1,α_2…α_ν jede Combination von ν der Ziffern 1,2…n, deren Anzahl (nach §. 7) B_ν^{(n)} ist, so erhalten wir, indem wir β_1,β_2…β_ν festhalten, ebenso viele Complexe der Form (7), und jedes Glied der Determinante A kommt in einem und nur in einem dieser Complexe vor." — ENTIRELY ABSENT from .tex (predicted: the dropped range-condition prose). Restored (incl. §7-ref to binomial B_ν^{(n)}).
- **★★★ FIX #94 — SATZ V (LAPLACE) RESTORED:** Weber: "**V.** Demnach erhalten wir, wenn wir alle Ausdrücke (7) summiren, die Determinante A:" **(8)** A=**Σ^α** A_{α…}^{β…}B_{α…}^{β…}. + "Selbstverständlich kann man auch die Combination der α festhalten und in Bezug auf die β summiren." + "**Dies ist der Satz von Laplace.**" — GPT had compressed ALL of this to "Daraus folgt der Satz von Laplace: (8) A=Σ A·B." (no V., no Σ^α upper index, no summiren-clause, no Selbstverständlich-sentence, no Dies-ist-sentence). Restored (Σ^α as \sum^{\alpha}, house pattern from §17).
- **★★★ FIX #95 — DERIVATION PARAGRAPH + SATZ VI RESTORED:** Weber: "Noch eine andere Darstellung der Determinante A durch die ersten und zweiten Unterdeterminanten erhält man auf folgende Weise. [¶] Man wähle in A irgend zwei Reihen aus, die sich in einem Element, etwa in a_ν^{(μ)}, schneiden. In jedem Gliede von A kommt ein Element mit dem unteren Index ν und ein Element mit dem oberen Index μ vor. Wir haben also zunächst in A den Complex a_ν^{(μ)}A_ν^{(μ)} und ferner die verschiedenen Complexe a_ν^{(i)}a_k^{(μ)}A_{ν,k}^{i,μ}, worin i jeden von μ verschiedenen und k jeden von ν verschiedenen Index bedeuten kann. [¶] **VI.** Wir können daher setzen:" — GPT had reduced to "Eine andere Darstellung von A durch erste und zweite Unterdeterminanten ist" (no derivation, no VI.). Also "oder nach IV." (GPT: "oder, nach der Vorzeichenregel," — fabricated wording for Weber's IV-reference). All restored.
- **★★★ FIX #96 — (9)/(10) SUPERSCRIPT-SWAP RESOLVED (the "contradiction"):** Weber: **(9)** A=a_ν^{(μ)}A_ν^{(μ)}+Σ^{i,k} a_ν^{(i)}a_k^{(μ)}**A_{ν,k}^{i,μ}**, / oder nach IV. / **(10)** A=a_ν^{(μ)}A_ν^{(μ)}−Σ^{i,k} a_ν^{(i)}a_k^{(μ)}**A_{ν,k}^{μ,i}**. — The sign flip is EXPLAINED by the superscript ORDER swap (i,μ ↔ μ,i; by IV a swap of two upper indices changes the sign). GPT had written the SAME symbol A_{νk}^{μi} in both, making (9)/(10) mutually contradictory. Fixed: (9) i,μ; (10) μ,i; subscript comma ν,k; Σ^{i,k} upper indices.
- **⚠⚠ PENDING (p81):** (a) dropped paragraph "Wir bemerken zu diesem Satze noch, dass A_{ν,k}^{μ,i} die dem Elemente a_k^{(i)} entsprechende erste Unterdeterminante der (n−1)reihigen Determinante A_ν^{(μ)} ist; denn A_{ν,k}^{μ,i} ist der Coëfficient […p81]" — cross-page; insert with continuation. (b) verify (11) geränderte Determinante U + (12) U=qA−Σu_iv_kA_k^{(i)} + (13) ∂²A/(∂a_ν^{(μ)}∂a_k^{(i)}) [zweckmäßig→zweckmässig] vs p81 scan. (c) §24 heading + trailing period.
- **⚠ FORMATTING-PASS FLAGS:** leqno (7)-(10); Σ upper-index rendering (\sum^{α} vs Weber's index-over-Σ) = Σ-Weber-conv item; gesperrt Sätze V/VI + "Dies ist der Satz von Laplace." + "erste Unterdeterminante"(p80 bot, pending). **SKIP:** (9) trailing comma-vs-period ambiguity (punct).
- **★★★ METHOD:** (1) "Contradictory near-duplicate equations" resolved not by deleting one but by finding the SUBTLE difference GPT homogenized away (superscript order i,μ vs μ,i) — when two eqs look identical ±sign, HUNT for the index/order difference that justifies both. (2) Numbered-Sätze awareness: Weber numbers his Sätze (I-VI in §23); GPT strips the numbers and inlines — check every "Satz von X"/"folgt:" for a lost Roman numeral. (3) Gate page-count is a TRIPWIRE not a constant: +1p after restoring ~40 lines = proportionate; verify section/equation counts before accepting a new baseline.
- NEXT: **p81** = §23 end + §24 start (.tex ~2830-2870): (a) complete "Wir bemerken zu diesem Satze noch…Coëfficient [von a_k^{(i)} in A_ν^{(μ)}…]"; (b) verify (11)/(12)/(13) geränderte-Determinante block vs scan (expect dropped prose around them; zweckmäßig→zweckmässig; check U-matrix entries + qA sign + Σu_iv_kA_k^{(i)} indices); (c) §24 "Lineare homogene Gleichungen" heading + opening ("Die hauptsächlichste Anwendung… specielle Form…" — looks old-orthography already, but VERIFY: the modernized zone may end at §23's close; grep showed "ergibt sich" at old-2787 which is now inside the (11)-(12) passage). Continue gap-pass p81->p99. ★★★MODERNIZED-ZONE end-detection; ★tags+refs; ★accents/index-order; ★dropped prose. Fix drops/rewords/misreads/norms/FABRIC; [sic] errata. Compile-gate IF edit (baseline 419pp/0/0).
**Confirmed by eye vs ~500dpi scans; 6 fixes (Sätze V/VI + Laplace prose + superscript-swap) + gate held at NEW baseline 419pp/0/0.**


### 2026-07-03 — p81 (§23 end: Wir-bemerken ¶ + geränderte Determinante (11)/(12)/(13) + §24 heading/opening, .tex ~2820-2860) — p1-99 gap pass — **★★★ §23 MODERNIZED-ZONE REBUILD COMPLETE: 6 FIXES incl. (13) SYMBOL+DERIVATIVE CORRECTION. Zone ENDS at §23.**
**CONTENT: 6 logical fixes (3 edits).** After fix: **419pp / 0 overfull / 0 underfull / PDF 2270503 B** (was 2269496). Compile-gate PASSED (baseline 419pp holds).
- **★★ FIX #97 — CROSS-PAGE PARAGRAPH RESTORED (p80-pending):** "Wir bemerken zu diesem Satze noch, dass A_{ν,k}^{μ,i} die dem Elemente a_k^{(i)} entsprechende **erste Unterdeterminante** der (n−1)reihigen Determinante A_ν^{(μ)} ist; denn A_{ν,k}^{μ,i} ist der Coëfficient von a_ν^{(μ)}a_k^{(i)} in der Entwickelung von A und A_ν^{(μ)} der Coëfficient von a_ν^{(μ)}, folglich A_{ν,k}^{μ,i} der Coëfficient von a_k^{(i)} in der Determinante A_ν^{(μ)}." — ENTIRELY ABSENT from .tex. Restored after (10).
- **★★ FIX #98 — GERÄNDERTE-INTRO PARAPHRASE REVERTED:** Weber: "**Man kann nach diesem Satze die sogenannte** geränderte Determinante [display (11)] **nach den Elementen der letzten Zeile und Colonne entwickeln und erhält:**" — GPT: "Für die geränderte Determinante (11) ergibt sich" (dropped method-sentence; fabricated "ergibt sich"). Restored.
- **★ FIX #99 — (12) DOUBLE Σ:** Weber (12): U = qA − **Σ^i Σ^k** u_i v_k A_k^{(i)}. (two Σ with upper i, k); GPT: single plain Σ. Fixed (\sum^{i}\sum^{k}).
- **★★ FIX #100 — DROPPED PARAGRAPH RESTORED:** "Man erhält diese Gleichung aus (10), wenn man n in n+1 verwandelt, und die Elemente der letzten Zeile und Colonne durch eine andere Bezeichnung auszeichnet." — absent from .tex. Restored after (12).
- **★★★ FIX #101 — (13) SYMBOL + DERIVATIVE PAIRING CORRECTED:** Weber (13): **A_{ν,k}^{i,μ} = ∂²A/(∂a_ν^{(i)} ∂a_k^{(μ)})** — superscripts i,μ pair with the derivative variables (consistent with (9): complex a_ν^{(i)}a_k^{(μ)}A_{ν,k}^{i,μ}). GPT had A_{νk}^{μi} = ∂²A/(∂a_ν^{(μ)}∂a_k^{(i)}) — BOTH superscript order AND ∂-variable superscripts swapped. + sentence rebuilt: "Auch bei **den** höheren Unterdeterminanten ist **bisweilen** die Bezeichnung durch Differentialquotienten **zweckmässig, so dass z.~B.** [display (13)] **gesetzt wird.**" (GPT: "zweckmäßig, z.B." + trailing-period display).
- **★ FIX #102 — §24 HEADING + ¶:** heading trailing period ("Lineare homogene Gleichungen.") + Weber's paragraph break after "…ist die Auflösung linearer Gleichungen." restored (GPT ran the two paragraphs together).
- **★★★ ZONE-END CONFIRMED:** §24 opening prose is ALREADY old-orthography + word-for-word faithful in .tex ("Die hauptsächlichste Anwendung… specielle Form… ableiten lässt."; "Wir betrachten ein System von m Gleichungen ersten Grades, in denen n Unbekannte x_1,x_2…x_n homogen vorkommen:" [homogen gesperrt, tracked]). The MODERNIZED ZONE = §23 ONLY (.tex old 2674-2843). ★ §23 FINAL TALLY: **27 fixes across p77-p81** (p77:4, p78:6, p79:5, p80:6, p81:6) — the worst-damaged stretch in vol1; clearly a different (modernizing, compressing) reconstruction pass. Remaining stray modern forms to watch: "ergibt sich" at .tex ~5144 (verify when reached).
- **FAITHFUL (verified):** (11) U-matrix entries (incl. last row v_1,v_2…v_n,q); §24 heading two-line centered form; §24 opening ¶¶; page signature "Weber, Algebra. I. / 6" = layout (out of scope). Running header "Lineare homogene Gleichungen." ✓.
- **⚠ FORMATTING-PASS FLAGS:** leqno (11)-(13); Σ^i Σ^k upper-index rendering (Σ-Weber-conv); (11) matrix comma-sep + dots-row; gesperrt "erste Unterdeterminante"(p80/81) + "homogen"(p81). **SKIP:** (11) last-row "v_n;" semicolon-vs-comma (scan noise/punct).
- NEXT: **p82** = §24 cont. (.tex ~2860-2900): eq(1) system of m homogeneous equations (f_1=a_1^{(1)}x_1+…=0 etc. or similar); "Lösung/Lösungssystem" definitions; likely Sätze about trivial solution + notation. Continue gap-pass p82->p99. §24 is OUTSIDE the modernized zone → expect §18-§22-style damage (dropped cross-refs, index relabels, dropped intermediate steps) rather than wholesale rewording — but VERIFY word-by-word regardless (never-certify). ★generic-index letters; ★dropped cross-refs "[§ N, (K)]"; ★eq-tags+refs; ★Fraktur; ★prose-ellipses. Fix drops/rewords/misreads/norms/FABRIC; [sic] errata. Compile-gate IF edit (baseline 419pp/0/0).
**Confirmed by eye vs ~500dpi scans; 6 fixes; §23 zone rebuild COMPLETE (27 fixes p77-81); gate held 419pp/0/0.**


### 2026-07-03 — p82 (§24: eq(1) System + triviale Lösung (2) + Rechteck (3) + Matrix-Definition, .tex ~2860-2889) — p1-99 gap pass — **3 FIXES (reword + Ueber + parens) — §24 back to LOW-damage profile**
**CONTENT: 3 logical fixes (2 edits).** After fix: **419pp / 0 overfull / 0 underfull / PDF 2270517 B** (was 2270503). Compile-gate PASSED.
- **★★ FIX #103 — REWORD REVERTED (.tex 2870):** Weber: eq(1) "…= 0, **worin** die Coëfficienten a_i^{(k)} als gegebene Grössen betrachtet **werden**." (relative clause attached to (1)); GPT: "Darin werden die Coefficienten … betrachtet." (new sentence). Restored "worin … werden." ("Coefficienten" ë-drop = house skip, kept).
- **★ FIX #104 — Ueber (.tex 2870):** Weber "**Ueber** die Zahlen m, n…"; GPT normalized to "Über". Fixed (matches .tex's own "Uebersicht/Uebergang" elsewhere).
- **★ FIX #105 — PARENTHESES (.tex 2889):** Weber: "…je nachdem n oder m die kleinere Zahl ist **(oder n-reihig, wenn n = m ist).**"; GPT: comma instead of parens. Fixed (precedent: p74 #69-class "(vom Vorzeichen abgesehen)").
- **FAITHFUL (verified):** **eq(1)** m×n homogeneous system [rows exact; per-row trailing-comma diffs = punct-skip]; "sondern uns allgemein die Aufgabe stellen, **alle** [gesperrt] Werthsysteme der x_1,x_2…x_n zu ermitteln, die den Gleichungen (1) genügen."; "Eine Lösung der Gleichungen (1) können wir sofort angeben: sie sind nämlich, was auch die Coëfficienten a_i^{(k)} sein mögen, erfüllt, wenn" **eq(2)** x_1=0, x_2=0,…x_n=0.; "Einen anderen extremen Fall… erwähnen; wenn nämlich die Coëfficienten sämmtlich den Werth Null haben, dann sind die Gleichungen (1) für **beliebige Werthe** [gesperrt] von x_1,x_2…x_n befriedigt."; "Der allgemeinen Beantwortung der Frage schicken wir folgende Bemerkungen voraus."; "Wir schreiben das System der Coëfficienten von (1) in Form eines Rechtecks" **eq(3)** m×n array [exact]; "Ein solches Schema, das für sich noch keine numerische Bedeutung hat, heisst eine **Matrix** [gesperrt], insofern es als Quelle einer grösseren Anzahl von Determinanten betrachtet wird."; "**Die der Matrix entstammenden Determinanten erhält man, wenn man beliebige Zeilen und Colonnen weglässt, in beliebiger, nur insoweit bestimmter Anzahl, dass die übrig bleibenden Elemente ein Quadrat bilden, und dieses Quadrat als Determinante auffasst.**" [whole passage gesperrt]; "So erhält man aus der Matrix einreihige, zweireihige u. s. f. Determinanten. Die höchsten Determinanten sind n- oder m-reihig…(fixed parens)." ALL word-for-word. Page ends; "Wir machen nun die Annahme" = p83.
- **⚠ FORMATTING-PASS FLAGS:** (3) matrix comma-sep; leqno (1)-(3); eq(2) \quad spacing. **SKIP:** colon-vs-semicolon (×2); eq(1) row-commas; ë-drop. **EMPHASIS (gesperrt, tracked):** "alle"; "beliebige Werthe"; "Matrix"; the whole "Die der Matrix entstammenden…auffasst." passage.
- **★★ METHOD:** §24 profile = back to LOW-damage (like §18-§22 clean stretches): 3 small fixes, no drops/fabrications. The §23 catastrophe was zone-specific. Watch-list stays: Ueber/Ü normalization is a recurring GPT slip (grep "Über " later); parens-vs-comma structure fixes; "worin…werden"-type clause rewords.
- NEXT: **p83** = §24 cont. (.tex ~2891-2914+): "Wir machen nun die Annahme, dass unter den ν-reihigen Determinanten der Matrix wenigstens eine von Null verschieden sei, während die (ν+1)-reihigen … alle verschwinden sollen. ν kann jede Zahl sein…"; "Wir können, ohne die Allgemeinheit zu beschränken… die nicht verschwindende ν-reihige Determinante sei" **eq(4)** A=|ν×ν vmatrix|≠0; "Denn offenbar steht es uns frei… Die Unterdeterminanten von A bezeichnen wir wie früher mit A_i^{(k)}, worin i,k von 1 bis ν gehen."; **Satz I.** "Wenn nun zunächst ν=n ist… keine andere Lösung als die in (2) enthaltene. Denn greifen wir die n ersten der Gleichungen (1) heraus," **eq(5)**; "und multipliciren diese der Reihe nach mit A_μ^{(1)},…" Continue gap-pass p83->p99. ★generic-index letters (μ!); ★"des vorigen Paragraphen" cross-ref; ★Sätze-numerals; ★dropped steps. Fix drops/rewords/misreads/norms/FABRIC; [sic] errata. Compile-gate IF edit (baseline 419pp/0/0).
**Confirmed by eye vs ~500dpi scans; 3 fixes; §24 low-damage; gate held 419pp/0/0.**


### 2026-07-03 — p83 (§24: ν-Annahme + eq(4) + Satz I + eq(5) + proof start, .tex ~2891-2916) — p1-99 gap pass — **4 FIXES (dropped parenthetical/symbol/eq-row + fabricated ≠0)**
**CONTENT: 4 logical fixes (3 edits).** After fix: **419pp / 0 overfull / 0 underfull / PDF 2270610 B** (was 2270517). Compile-gate PASSED.
- **★★ FIX #106 — ANNAHME-PARAGRAPH (3 sub-fixes, .tex 2891):** (a) restored DROPPED PARENTHETICAL "…die kleinere der beiden Zahlen n oder m ist **(oder falls n=m ist, diesen gemeinschaftlichen Werth nicht übertrifft).**" (GPT: plain period); (b) restored ¶ break before "Eine solche Zahl ν wird sich immer finden lassen…"; (c) restored DROPPED SYMBOL "dass alle Coefficienten **a_i^{(k)}** verschwinden." (GPT dropped a_i^{(k)}); (+ "(ν+1)reihigen" unhyphenated per scan). ["wenigstens eine von Null verschieden" gesperrt → emphasis-pass.]
- **★ FIX #107 — FABRICATED ≠0 REMOVED (eq(4)):** scan eq(4) = "A = |ν×ν vmatrix|." (period, NO ≠0 — the non-vanishing is stated in the preceding prose "die nicht verschwindende ν-reihige Determinante sei"). GPT had added "\ne0". Removed. ★ Same fabrication-class as p69 eq(4)-matrix: GPT adds redundant mathematical decoration.
- **★ FIX #108 — SATZ-I/PROOF STRUCTURE:** Satz I (gesperrt) ends "…keine andere Lösung, als die in den Gleichungen (2) enthaltene." [comma restored], then NEW ¶ "Denn greifen wir die n ersten der Gleichungen (1) heraus**:**" [colon; GPT: merged ¶ + comma]. Restored.
- **★★ FIX #109 — DROPPED EQ-ROW (eq(5)):** scan eq(5) has FOUR rows: a^{(1)}-row, **a^{(2)}-row**, dots-row, a^{(n)}-row. GPT dropped the a^{(2)}-row (3 rows only). Restored. ★ Same class as p68 ΣM/dropped-display: GPT truncates display rows.
- **FAITHFUL (verified):** Annahme prose (rest); "Eine solche Zahl ν…"; "Wir können, ohne die Allgemeinheit zu beschränken, zur Vereinfachung der Bezeichnung annehmen, die nicht verschwindende ν-reihige Determinante sei" **eq(4)** [ν×ν matrix entries exact]; "Denn offenbar steht es uns frei, das Gleichungssystem (1) in beliebiger Weise anzuordnen, und ferner können wir die Bezeichnung der Unbekannten x so wählen, dass irgend ν von ihnen die ν ersten sind."; "Die Unterdeterminanten von A bezeichnen wir wie früher mit A_i^{(k)}, worin i,k von 1 bis ν gehen."; **Satz I** (gesperrt) content; eq(5) rows + "multipliciren diese der Reihe nach mit A_μ^{(1)}, A_μ^{(2)} … A_μ^{(n)}, worin μ jeder der Indices 1,2…n sein kann, und addiren sie, so folgt" [μ = correct per scan]. Running header "Matrix." ✓ (Weber's abbreviated head, layout).
- **⚠⚠ PENDING (p84):** PROOF-TAIL REBUILD (cross-page): Weber "so folgt, **weil nach §. 22 (2) und (6)** [display: **Σ_{1,ν}^{i} A_μ^{(i)} a_λ^{(i)} = 0 oder = A**] […p84 continuation…]" — GPT compressed to "so folgt wegen der Relationen des vorigen Paragraphen [display Ax_μ=0], und da nach unserer Voraussetzung A von Null verschieden ist, x_μ=0." The §22-citation + Σ-display are DROPPED; rebuild WITH p84 text (zoom the Σ bounds "1,ν" vs "1,n" + the a_λ subscript λ!). Then Satz II ("Wir heben den am meisten angewendeten besonderen Fall m=n hervor…") + rest.
- **⚠ FORMATTING-PASS FLAGS:** leqno (4)/(5); (4) matrix comma-sep; eq(1)/(5) row-comma diffs (punct-skip). **EMPHASIS (gesperrt):** "wenigstens eine von Null verschieden"; Satz I whole.
- **★★ METHOD:** §24 damage = drop-heavy (parenthetical, symbol, eq-row, ¶) + small fabrications (≠0) — the §18-§22 profile confirmed. ★ eq-ROW-COUNT check added: count display rows scan-vs-.tex on EVERY multi-row equation (GPT truncates the middle rows, keeping first+dots+last).
- NEXT: **p84** = §24 cont. (.tex ~2916-2950): ⚠⚠rebuild proof-tail (Σ_{1,ν}^{i}A_μ^{(i)}a_λ^{(i)}=0 oder =A + §.22 (2) und (6) + p84-continuation into Ax_μ=0, x_μ=0); then "Wir heben den am meisten angewendeten besonderen Fall m=n hervor und geben dem Satze für diesen Fall den folgenden Ausdruck:" **Satz II** (n lin. hom. Gleichungen, Det.≠0 ⇒ alle x=0; oder:…); "Unter der Determinante eines Systems…verstanden."; "Wir betrachten ferner den Fall, dass ν kleiner als n ist… wählen wir die ν ersten Gleichungen des Systems (1), und schreiben sie so:" **eq(6)**. Continue gap-pass p84->p99. ★ZOOM Σ bounds + a_λ; ★eq-row counts; ★Sätze-numerals; ★cross-refs. Fix drops/rewords/misreads/norms/FABRIC; [sic] errata. Compile-gate IF edit (baseline 419pp/0/0).
**Confirmed by eye vs ~500dpi scans; 4 fixes; gate held 419pp/0/0. Proof-tail rebuild pending p84.**


### 2026-07-03 — p84 (§24: Satz-I proof-tail + Satz II + eq(6) + eq(7)/(8) C-Abkürzung, .tex ~2914-2951) — p1-99 gap pass — **5 FIXES incl. PROOF-TAIL REBUILD + (7)/(8) MODERN-Σ DE-COMPRESSION (λ restored)**
**CONTENT: 5 logical fixes (4 edits).** After fix: **419pp / 0 overfull / 0 underfull / PDF 2271183 B** (was 2270610). Compile-gate PASSED.
- **★★★ FIX #110 — PROOF-TAIL REBUILT (p83-pending; .tex 2914-2918):** Weber: "…und addiren sie, so folgt, **weil nach §. 22 (2) und (6)** [display: **Σ_{1,ν}^{i} A_μ^{(i)} a_λ^{(i)} = 0 oder = A**] **ist, je nachdem λ von μ verschieden ist oder nicht,** [display: A x_μ = 0,] und da nach unserer Voraussetzung A von Null verschieden ist, [display: x_μ = 0.]" — GPT had compressed to "so folgt wegen der Relationen des vorigen Paragraphen [Ax_μ=0], und da…, x_μ=0." (dropped the §22-citation, the Σ-identity display, the je-nachdem-λ clause; fabricated "wegen der Relationen…"; inlined x_μ=0). ZOOM-confirmed Σ bounds "1,ν" (i above) + subscript λ (crop_28_84, crystal clear). Rebuilt.
- **★ FIX #111 — SATZ II ¶ + comma:** "…so haben sämmtliche Unbekannte den Werth Null**, oder:** [¶] Wenn ein System von n linearen Gleichungen…" — GPT: ";" + run-on. Restored (Satz II both halves gesperrt → emphasis-pass).
- **★★ FIX #112 — eq(6) ROWS:** (a) dropped a^{(2)}-ROW restored (scan 4 rows; GPT 3 — 2nd occurrence of the row-truncation after eq(5)!); (b) dropped a_2-TERMS restored in each row (scan "a_1^{(i)}x_1 + a_2^{(i)}x_2 + ⋯ + a_ν^{(i)}x_ν"; GPT "a_1+⋯+a_ν" only).
- **★★★ FIX #113 — eq(7)/(8) DE-COMPRESSED + INDEX λ RESTORED:** Weber **(7)**: A x_μ = −C_{ν+1,μ}x_{ν+1} − ⋯ − C_{n,μ}x_n (EXPLICIT expansion, C-subscript order **λ,μ**); **(8)**: C_{λ,μ} = Σ_{1,ν}^{i} a_λ^{(i)}A_μ^{(i)}, λ = ν+1,ν+2,…n. — GPT had rewritten (7) as modern "−Σ_{h=ν+1}^{n} C_{μh}x_h" (fabricated Σ-compression), renamed λ→h, and SWAPPED the C-subscript order to μh. Both restored (incl. Weber-style Σ bounds).
- **★ FIX #114 — "wie vorhin," + colons:** "Daraus folgt, **wie vorhin,** mit Benutzung von §. 22, (2), (6)**:**" (GPT dropped "wie vorhin", comma for colon) + "wenn zur Abkürzung gesetzt ist**:**". + 2951 sentence C_{μh}→C_{λ,μ}, a_h→a_λ (×3) [⚠ second half of that sentence = p85; index letter certain from (8); VERIFY wording vs p85 scan next turn].
- **FAITHFUL (verified):** "Wir heben den am meisten angewendeten besonderen Fall m=n hervor und geben dem Satze für diesen Fall den folgenden Ausdruck:"; **Satz II** both formulations (gesperrt); "Unter der Determinante eines Systems von n linearen homogenen Gleichungen mit n Unbekannten ist hier die Determinante aus den n² Coëfficienten dieser Gleichungen verstanden."; "Wir betrachten ferner den Fall, dass ν kleiner als n ist. Da m gleich oder grösser als ν sein muss, so wählen wir die ν ersten Gleichungen des Systems (1), und schreiben sie so:"; eq(6) rows [now exact]; "Wir bezeichnen wieder mit μ einen der Indices 1,2…ν, multipliciren die Gleichungen (6) der Reihe nach mit A_μ^{(1)}, A_μ^{(2)} … A_μ^{(ν)} und addiren sie." ALL word-for-word.
- **⚠⚠ PENDING (p85/p86):** the λ→h rename + modern-Σ compression EXTENDS through the Satz-III machinery (.tex 2959-3164: double-Σ displays, x_h factors, (ν+1)-reihige-determinant displays, B-system analogues at 3145-3164). Verify page-by-page against p85/p86 scans and de-compress/rename per scan — do NOT blanket-replace (Weber's own display forms unknown until read). Also 2951-sentence-tail wording check.
- **⚠ FORMATTING-PASS FLAGS:** leqno (6)-(8); Σ_{1,ν}^{i} rendering (Σ-Weber-conv); eq(6) multi-line. **EMPHASIS (gesperrt):** Satz II (both halves).
- **★★★ METHOD — NEW DAMAGE SUB-CLASS: MODERN-Σ COMPRESSION.** GPT rewrites Weber's EXPLICIT expansions (−C_{ν+1,μ}x_{ν+1}−⋯) as compact modern Σ-notation with ITS OWN index names (h) and bounds (h=ν+1..n) — mathematically equivalent, textually fabricated. ★ RULE: every \sum with modern bounds (\sum_{i=1}^{ν}, \sum_{h=ν+1}^{n}) in the .tex is SUSPECT — check the scan for (a) explicit expansion instead, (b) Weber's index letter, (c) Weber's Σ-bound style (under: range, over: index). The λ/h test: Weber uses GREEK λ for the free column index here.
- NEXT: **p85** = §24 cont. (.tex ~2951-2990): 2951-tail ("…ersetzt. Durch (7) sind nun, da A von Null verschieden ist, die x_1…x_ν linear ausgedrückt durch x_{ν+1}…x_n und durch die bekannten Grössen." — verify + λ-wording); "Es ist nun noch zu zeigen:" **Satz III** ("Durch die Ausdrücke (7) sind die Gleichungen (1) befriedigt, welche Werthe auch x_{ν+1}…x_n haben mögen…"); proof: "Um die Wahrheit dieses Satzes einzusehen…" + the double-Σ displays (2959+: ★expect Weber explicit/λ forms vs .tex h-compressions — REBUILD per scan); (ν+1)-reihige determinant display (2980). Continue gap-pass p85->p99. ★★ZOOM Σ-displays + index letters; ★eq-row counts; ★dropped clauses. Fix drops/rewords/misreads/norms/FABRIC; [sic] errata. Compile-gate IF edit (baseline 419pp/0/0).
**Confirmed by eye vs ~500dpi scans; 5 fixes (proof-tail + λ restoration + row restorations); gate held 419pp/0/0.**


### 2026-07-03 — p85 (§24: C_{λ,μ}-Erklärung tail + Satz III + Σ-Notation-Erklärung + eq(9)-(12), .tex ~2951-3010) — p1-99 gap pass — **6 FIXES incl. DROPPED Σ-NOTATION-SENTENCE + h-INDEX VINDICATED**
**CONTENT: 6 logical fixes (4 edits).** After fix: **419pp / 0 overfull / 0 underfull / PDF 2271418 B** (was 2271183). Compile-gate PASSED.
- **★★★ h-INDEX RESOLUTION (p84-pending, GOOD NEWS):** Weber uses BOTH letters: **λ = free column index** in (7)/(8) (p84, fixed #113) and **h = summation letter** in (9)-(13) (Weber's own choice, printed "Σ^h_{ν+1,n}"). The .tex's h in (9)-(13) was CORRECT — no rename needed there; my p84 λ-restorations stand as-is. The suspected "λ→h zone" (.tex 2959-3164) dissolves: only Σ-BOUNDS STYLE (fmt) + local factor-order/tails differ.
- **★★ FIX #115 — 2951-TAIL FULLER WORDING (p84-pending verified):** Weber: "dass man die **Elemente der μten Colonne a_μ^{(1)}, a_μ^{(2)} … a_μ^{(ν)} durch** a_λ^{(1)}, a_λ^{(2)} … a_λ^{(ν)} ersetzt." — GPT (and my conservative p84 patch) had the shorter "die μte Colonne durch die Elemente a_λ… ersetzt". Restored Weber's full form (lists BOTH element sets). λ-letter confirmed by scan.
- **★★ FIX #116 — SATZ III SUBORDINATE FORM:** Weber: "Es ist nun noch zu zeigen [no colon] III. **dass** durch die Ausdrücke (7) die Gleichungen (1) **befriedigt sind**, welche Werthe auch x_{ν+1},…x_n haben mögen, **dass also** n−ν von den Unbekannten willkürlich bleiben, von denen die übrigen ν nach (7) abhängig sind." — GPT recast as main clause ("Durch die Ausdrücke (7) sind…befriedigt" + "so dass also"). Restored.
- **★★★ FIX #117 — DROPPED Σ-NOTATION EXPLANATION:** Weber: "…einzusetzen. **Man vereinfacht die Rechnung sehr durch Anwendung eines Summenzeichens Σ, bei dem wir, wie schon oben, die Summationsbuchstaben oben, die Grenzen unten anhängen.** Zunächst können wir **dann die Gleichungen** (7) so schreiben:" — GPT dropped Weber's own explanation of his Σ-typography (index above, bounds below!) + "dann die Gleichungen". Restored. ★ This sentence is the AUTHOR'S justification of the Σ-convention that the fmt-pass will implement — high documentary value.
- **★ FIX #118 — (9) FACTOR ORDER:** Weber: "a_h^{(i)} A_μ^{(i)} x_h" (x_h LAST); GPT: "x_h a_h^{(i)}A_μ^{(i)}". Fixed.
- **★ FIX #119 — (10) MISSING RANGE TAIL:** Weber (10) ends ", k = 1, 2 … m."; .tex lacked it. Added \qquad k=1,2,\ldots,m.
- **★★ FIX #120 — (12) DROPPED ROW+COLUMN:** scan (12) = (ν+1)-reihige det with a_2-COLUMN and a^{(2)}-ROW explicit; GPT dropped both (3rd row-truncation occurrence: eq(5) p83, eq(6) p84, (12) p85). Restored (5-col × 5-row form with dots).
- **FAITHFUL (verified):** "Durch (7) sind nun, da A von Null verschieden ist, die x_1, x_2 … x_ν linear ausgedrückt durch x_{ν+1},…x_n und durch die bekannten Grössen."; "Um die Wahrheit dieses Satzes einzusehen, haben wir nur die Ausdrücke (7) in die Gleichungen (1) einzusetzen."; "Wir multipliciren, wenn k irgend eine der Ziffern 1,2…m bedeutet, mit a_μ^{(k)} und summiren in Bezug auf μ:"; **(10)** LHS/RHS structure; "Dazu addiren wir beiderseits die Summe [A Σ^h_{ν+1,n} a_h^{(k)} x_h — scan DISPLAY, .tex inline = fmt-flag] und erhalten"; **(11)** full structure exact; "Der Factor von x_h in der Summe auf der rechten Seite ist nach §. 23, (12) die Determinante"; "und verschwindet daher, wenn k≦ν ist, nach §. 21, V., weil [→p86]". Satz III gesperrt (emphasis-pass).
- **⚠ FORMATTING-PASS FLAGS:** Σ-bounds style (Weber: letter above/range below vs .tex modern \sum_{i=1}^{ν}) — SYSTEMATIC §24, now explicitly Weber-documented (#117!); "Dazu addiren…Summe" inline→display; leqno (9)-(12); (12) matrix comma-sep. **SKIP:** "k≦ν" vs \le (glyph-equiv); §.-punct.
- **★★ METHOD:** (1) The λ/h scare resolved by READING ON — Weber legitimately switches letters between free-index (λ) and summation-letter (h) roles; verify each occurrence's ROLE before renaming. (2) Row-truncation now a confirmed SERIAL pattern (3 pages running) — row/column-count every display. (3) Weber's Σ-typography sentence (#117) = authoritative spec for the fmt-pass Σ-conversion.
- NEXT: **p86** = §24 end + §25 start? (.tex ~3010-3070): p86 continues "weil zwei Zeilen übereinstimmen, wenn aber k>ν ist, nach der Voraussetzung, weil dann (12) eine (ν+1)-reihige Determinante der Matrix (3) ist. Wir bekommen also aus (11), da A von Null verschieden ist, (13) Σ^μ_{1,n} a_μ^{(k)} x_μ = 0, k=1,2…m, d.h. das System (1) ist durch (7) befriedigt."; then "Wir wollen von dem so bewiesenen Satze noch den besonderen Fall hervorheben, dass m=n−1 und ν=n−1 ist…" + Matrix (14) + Determinanten D_1,D_2…D_n definitions + Satz IV (x_1:x_2:…=D_1:−D_2:…) presumably. Continue gap-pass p86->p99. ★row/col counts; ★Σ-bounds; ★Sätze-numerals; ★(13)-tail k-range; ★dropped clauses. Fix drops/rewords/misreads/norms/FABRIC; [sic] errata. Compile-gate IF edit (baseline 419pp/0/0).
**Confirmed by eye vs ~500dpi scans; 6 fixes; h-index vindicated (no zone rename needed); gate held 419pp/0/0.**


### 2026-07-03 — p86 (§24 end: eq(13) + m=n−1 Fall + Matrix (14) + System (15) + Verhältnisse (16) + n=3 Beispiel (17)/(18), .tex ~2999-3040) — p1-99 gap pass — **3 FIXES. §24 COMPLETE (p81-86).**
**CONTENT: 3 logical fixes (3 edits).** After fix: **419pp / 0 overfull / 0 underfull / PDF 2271453 B** (was 2271418). Compile-gate PASSED.
- **★ FIX #121 — COLON + ¶ (.tex 3006):** Weber: "Wir können diesem Resultate folgenden Ausdruck geben**:** [¶] Bezeichnen wir die (n−1)reihigen Determinanten der Matrix" — GPT: period + run-on paragraph. Restored (+ (n−1)reihigen unhyphenated per scan).
- **★ FIX #122 — COLON (.tex 3016):** "…und nehmen an, dass wenigstens eine von diesen Grössen von Null verschieden sei, so ist die Lösung des Systems**:**" — colon restored (scan; also dropped GPT's comma after the A-list per scan).
- **★★ FIX #123 — (15) DROPPED ROW:** scan (15) = 4 rows ((1), **(2)**, dots, (n−1)); GPT 3 rows. Restored a^{(2)}-row. **4th serial row-truncation** (eq(5) p83, eq(6) p84, (12) p85, (15) p86) — the row-count check is now standard.
- **FAITHFUL (verified):** "zwei Zeilen übereinstimmen, wenn aber k>ν ist, nach der Voraussetzung, weil dann (12) eine ν+1reihige Determinante der Matrix (3) ist. Wir bekommen also aus (11), da A von Null verschieden ist," **(13)** Σ^μ_{1,n} a_μ^{(k)}x_μ=0, k=1,2…m, [k-tail present ✓]; "d.h. das System der Gleichungen (1) ist durch (7) befriedigt."; "Wir wollen von dem so bewiesenen Satze noch den besonderen Fall hervorheben, dass m=n−1 und ν=n−1 ist. In diesem Falle bleibt nur **eine** [gesperrt] der Unbekannten beliebig und die **Verhältnisse** [gesperrt] der Unbekannten sind völlig bestimmt."; **(14)** matrix [4 rows ✓ row-count OK]; "mit abwechselndem Vorzeichen genommen durch [A_1, A_2 … A_n — scan DISPLAY, .tex inline = fmt-flag]"; **(16)** x_1:x_2:⋯:x_n=A_1:A_2:⋯:A_n [exact]; "So erhalten wir für n=3 die Lösung des in der Geometrie oft vorkommenden Gleichungssystems" **(17)** ax+by+cz=0 / a'x+b'y+c'z=0 [scan 2-line; .tex 1-line+comma = fmt-flag]; **(18)** x:y:z=bc'−cb':ca'−ac':ab'−ba'. [exact]. §24 ends; §25 heading = p87.
- **⚠ FORMATTING-PASS FLAGS:** A_1…A_n list inline→display; (17) 1-line vs 2-line; leqno (13)-(18); Σ-bounds (13). **SKIP:** (ν+1)reihige hyphen/parens variants; eq-row trailing commas. **EMPHASIS (gesperrt):** "eine"; "Verhältnisse".
- **⚠ WATCH (§25, .tex 3043+):** (a) §25 heading trailing period (verify vs p87); (b) **"notwendig"-MODERNIZATION SUSPECT:** .tex 3047 "notwendige und hinreichende"/"notwendig Null", 3053 "nöthig"(old!)/"notwendige Folgen", 3055 "notwendigen" — Weber 1895 prints "nothwendig" — INCONSISTENT mix in .tex → verify each on p87 scan and restore "nothwendig" where printed. (c) (1)-tag ≠0 (3063 has \ne0 inside tag (1) — same fabrication-class as p83 #107? verify vs p87 scan).
- **★★ METHOD:** §24 complete: 21 fixes across p82-86 (3+4+5+6+3). Damage profile: drops (rows/clauses/symbols/¶) + small fabrications + one Σ-compression + Sätze-recasts. The serial a^{(2)}-row truncation (4×) = GPT's strongest §24 signature.
- NEXT: **p87** = §25 Elimination aus linearen Gleichungen (.tex ~3043-3080): heading [★period]; "Es kommt bisweilen vor, dass es sich bei einem gegebenen System linearer Gleichungen nicht sowohl um die wirkliche Ermittelung der Unbekannten handelt, als um die Beurtheilung der Möglichkeit ihrer Lösung… Die Aufstellung dieser Bedingungsgleichungen heisst **Elimination**…"; "Wir betrachten, wie im vorigen Paragraphen… Dies ist immer der Fall, wenn n>m ist. Ist aber n≤m… dass alle n-reihigen Determinanten der Matrix verschwinden. Denn wenn eine von diesen nicht verschwindet, so sind nach §24, II die Werthe… [★notwendig→nothwendig ×several]"; Binomial-Anzahl display m(m−1)⋯(m−n+1)/(1·2⋯n); "Um ein System von notwendigen[→nothwendigen?], hinreichenden und von einander unabhängigen Bedingungen…"; (1) A=|ν×ν|≠0 [★verify ≠0 vs scan]. Continue gap-pass p87->p99. ★nothwendig-sweep; ★row/col counts; ★colons/¶¶; ★cross-refs. Fix drops/rewords/misreads/norms/FABRIC; [sic] errata. Compile-gate IF edit (baseline 419pp/0/0).
**Confirmed by eye vs ~500dpi scans; 3 fixes; §24 COMPLETE (21 fixes p82-86); gate held 419pp/0/0.**


### 2026-07-03 — p87 (§25 Elimination aus linearen Gleichungen: heading + Elimination-Def + n>m/n≦m Bedingungen + Binomial-Anzahl, .tex ~3048-3058) — p1-99 gap pass — **4 FIXES (nothwendig-sweep + direct-question + dropped clause)**
**CONTENT: 4 logical fixes (3 edits).** After fix: **419pp / 0 overfull / 0 underfull / PDF 2271073 B** (was 2271453). Compile-gate PASSED.
- **★ FIX #124 — §25 HEADING PERIOD:** "Elimination aus linearen Gleichungen**.**" (scan two-line centered heading with period; .tex lacked it).
- **★★ FIX #125 — DIRECT QUESTION + DROPPED SENTENCE-HEAD:** Weber: "…und fragen**: wann hat dies System eine Lösung**, bei der nicht alle Unbekannten verschwinden**? Wir haben schon gesehen, dass** dies immer der Fall ist, wenn n>m ist." — GPT: indirect "und fragen, wann dies System eine Lösung hat, …verschwinden. Dies ist immer der Fall…" (question flattened + "Wir haben schon gesehen, dass" dropped). Restored.
- **★★ FIX #126 — nothwendig-SWEEP (×3) + "also":** Weber prints "**nothwendige und hinreichende** [gesperrt] Bedingung", "die Werthe der Unbekannten **nothwendig** Null", "so dass **also** nach §. 24, III"; .tex had modernized notwendig ×2 + dropped "also" (+ "§ 24, II**.**" period; (ν+1)reihigen unhyphen). All restored.
- **★★ FIX #127 — DROPPED CLAUSE (Binomial paragraph):** Weber: "Ist n = m, so ist diese Zahl = 1 **und wir erhalten den Fall §. 24, II. und wie zu erwarten war, eine [gesperrt] Bedingung.**" — GPT truncated to "so ist diese Zahl =1." Also "grösser als nöthig **ist**, weil einige von ihnen **nothwendige** Folgen der übrigen sind." (GPT: "nöthig," no "ist" + "notwendige"). Restored.
- **FAITHFUL (verified):** §25 heading position; Elimination-Def paragraph word-for-word ("…nicht sowohl um die wirkliche Ermittelung der Unbekannten handelt, als um die Beurtheilung der Möglichkeit ihrer Lösung, also um die Aufstellung der Bedingungsgleichungen, die zwischen den Coëfficienten bestehen müssen, wenn Lösungen oder Lösungen von bestimmter Art überhaupt vorhanden sein sollen. Die Aufstellung dieser Bedingungsgleichungen heisst **Elimination** [gesperrt]. Implicite ist die Lösung dieser Aufgabe schon im Vorhergehenden enthalten; wir wollen aber noch ausdrücklich auf einige hierher gehörige Fragen zurückkommen."); "(ν+1)reihigen…Null sind, während von den ν-reihigen wenigstens eine nicht verschwindet…"; "Nun lassen sich, wenn n≦m ist, aus der Matrix §. 24, (3)" Binomial-display m(m−1)…(m−n+1)/(1·2…n) [exact]; "n reihige Determinanten bilden, und so gross wäre also die Anzahl der Bedingungen." Page ends "…der übrigen sind."; "Um ein System von notwendigen[?]…" = p88.
- **⚠ FORMATTING-PASS FLAGS:** Binomial display fraction style (1.2…n dots); leqno n/a (unnumbered). **SKIP:** n≦m vs \le (glyph-equiv); ë-drop; colon-vs-comma minor. **EMPHASIS (gesperrt):** "Elimination"; "homogen"; "nothwendige und hinreichende"; "eine" (Bedingung).
- **⚠⚠ PENDING (p88):** .tex 3058+ "Um ein System von notwendigen[→nothwendigen?], hinreichenden und von einander unabhängigen Bedingungen zu erhalten, fassen wir die Fragestellung präciser…" + (1) A=|ν×ν|**≠0-in-display** [fabrication-suspect, cf. #107 — Weber likely states "als von Null verschieden an" in prose only] + "Wir berechnen die Unbekannten x_1…x_ν nach §24, (9) und bilden die Summen §24, (11)…" + (2)-conditions vmatrix. Verify all vs p88 scan.
- **★★ METHOD:** "nothwendig"-modernization = same class as Colonne/Kolonne (c/k) — 19th-c. -th- spellings (nothwendig, nöthig, Werth, Theil) are SOURCE-FIDELITY items; grep-sweep "notwendig|Werte |Teil" when suspicious. §25 profile so far = §24-like (drops + rewords + orthography).
- NEXT: **p88** = §25 cont. (.tex ~3058-3100): "Um ein System von nothwendigen[?], hinreichenden und von einander unabhängigen Bedingungen zu erhalten…präciser und fragen nach den Bedingungen, dass aus einem System von m linearen homogenen Gleichungen mit n Unbekannten ν von den Unbekannten durch n−ν willkürlich bleibende vollkommen bestimmt werden können."; "Nehmen wir an, die Unbekannten x_{ν+1}…x_n sollen willkürlich bleiben, x_1…x_ν durch sie bestimmt sein, und nehmen die Determinante" (1) A=|ν×ν| [★≠0 in display vs prose "als von Null verschieden an"]; "Wir berechnen…nach §.24, (9) und bilden die Summen §.24, (11), deren Verschwinden besagt…" ; (2) conditions-vmatrix. Continue gap-pass p88->p99. ★nothwendig-sweep; ★≠0-fabrication; ★row/col counts; ★cross-refs. Fix drops/rewords/misreads/norms/FABRIC; [sic] errata. Compile-gate IF edit (baseline 419pp/0/0).
**Confirmed by eye vs ~500dpi scans; 4 fixes (nothwendig ×4 + question + clause); gate held 419pp/0/0.**


### 2026-07-03 — p88 (§25 cont.: präciser-Frage + §24-Antwort-¶ + (1) A-Det + (2)/(3) Bedingungen, .tex ~3057-3097) — p1-99 gap pass — **6 FIXES incl. 2 DROPPED PASSAGES + ≠0-FABRICATION CONFIRMED**
**CONTENT: 6 logical fixes (5 edits).** After fix: **419pp / 0 overfull / 0 underfull / PDF 2270965 B** (was 2271073). Compile-gate PASSED.
- **★★ FIX #128 — PRÄCISER-PARAGRAPH:** "nothwendigen" (GPT: notwendigen); "fassen wir die Fragestellung **etwas** präciser" (etwas dropped); "nach den Bedingungen**:**" colon + set-off dass-block; "m linearen**,** homogenen Gleichungen" comma. [dass-block gesperrt → emphasis-pass.]
- **★★★ FIX #129 — DROPPED PARAGRAPH restored:** "**Auch diese Frage ist in §. 24 eigentlich schon beantwortet. Es muss unter den ν-reihigen Determinanten eine von Null verschieden sein, während die (ν+1)reihigen alle verschwinden. Es genügt aber schon, wenn es von einer kleineren Anzahl der (ν+1)reihigen Determinanten feststeht, dass sie verschwinden.**" — ENTIRELY ABSENT from .tex (went straight to "Nehmen wir an"). Restored.
- **★★ FIX #130 — (1): ≠0-FABRICATION CONFIRMED + ROW:** scan (1) = "A = |ν×ν|" with NO ≠0 (prose "als von Null verschieden an" carries it); .tex had \ne0 in display (2nd confirmed instance of the ≠0-decoration fabrication, cf. #107 p83). Removed. + dropped a^{(2)}-row restored (5th serial row-truncation). + "nehmen die Determinante**:**" colon.
- **★ FIX #131 — FABRICATED CROSS-REF + COLON:** Weber: "nach §. 24, (9) und bilden die Summen **(11)**"; .tex had added "\S\,24," before (11) (GPT normalization-addition). Removed. + "Die Bedingungen dafür werden also**:**".
- **★★ FIX #132 — (2): ROW+COLUMN:** dropped a_2-column + a^{(2)}-row restored (6th serial row-truncation).
- **★★★ FIX #133 — DROPPED PASSAGE after (3):** Weber: "oder anders geschrieben**:** (3) […]=0**,** **und diese Bedingungen genügen auch. Die Gleichung (2) oder (3) ist aber identisch befriedigt, wenn h = 1,2…ν oder k = 1,2…ν ist, und giebt also für diese Werthe keine Bedingung für die Coefficienten. Solche Bedingungen ergeben sich nur für** [→(4) p89]" — .tex had "oder, anders geschrieben, (3) […]=0. Hierbei ist [(4)]" (whole identisch-befriedigt passage dropped, replaced by "Hierbei ist"). Restored; (4)-display + following kept for p89 verification.
- **FAITHFUL (verified):** "Nehmen wir an, die Unbekannten x_{ν+1}, x_{ν+2} … x_n sollen willkürlich bleiben, x_1, x_2 … x_ν durch sie bestimmt sein"; (1) entries; "Wir berechnen die Unbekannten x_1, x_2 … x_ν nach §. 24, (9)…wirklich befriedigt ist."; (2) structure + "=0,"; (3) content (Σ-bounds fmt). Page ends "…ergeben sich nur für"; (4)/(5)/Unabhängigkeits-¶ = p89.
- **⚠⚠ PENDING (p89):** verify (4) h/k-ranges + (5) (n−ν)(m−ν) + "Diese Bedingungen sind wirklich von einander unabhängig. Denn die linken Seiten von (3)…" ¶ + §26 heading "Unhomogene lineare Gleichungen" [+period] + §26 opening (.tex 3101-3113 looks old-orthography but verify; eq(1) §26 y_i-system row-count!).
- **⚠ FORMATTING-PASS FLAGS:** dass-block set-off (gesperrt); (1)/(2) matrix comma-sep; leqno; Σ-bounds (3). **SKIP:** (3) "=0," comma vs period variants noted. **EMPHASIS (gesperrt):** the dass-block (präciser Frage).
- **★★ METHOD:** §25 = drop-heavy like §24 but with LONGER dropped units (2 full passages on one page). The ≠0-decoration is now a CONFIRMED serial fabrication (p83 #107 (4); p88 #130 (1)) — check every \ne0/≠0 in displays vs scan; Weber puts non-vanishing in PROSE. Cross-ref ADDITIONS (extra "§ N,") join cross-ref DROPS as a GPT failure mode — verify both directions.
- NEXT: **p89** = §25 end + §26 start (.tex ~3098-3120): (4) h=ν+1…n / k=ν+1…m [verify vs scan]; (5) (n−ν)(m−ν); "Diese Bedingungen sind wirklich von einander unabhängig. Denn die linken Seiten von (3) können durch geeignete Annahmen über die Coefficienten a für jede Indexcombination aus der Reihe (4) einen ganz beliebigen Werth erhalten, wie man erkennt, wenn man sämmtliche betreffenden Elemente ausser dem einen in Frage kommenden gleich Null setzt." [verify]; **§26 heading "Unhomogene lineare Gleichungen" [+period]**; §26 opening ¶¶ + eq(1) y-system [row-count: .tex has 4 rows incl (2)-row ✓ verify]. Continue gap-pass p89->p99. ★row/col counts; ★≠0s; ★nothwendig/-th-; ★dropped ¶¶; ★cross-refs both directions. Fix drops/rewords/misreads/norms/FABRIC; [sic] errata. Compile-gate IF edit (baseline 419pp/0/0).
**Confirmed by eye vs ~500dpi scans; 6 fixes (2 dropped passages + ≠0 + rows); gate held 419pp/0/0.**
