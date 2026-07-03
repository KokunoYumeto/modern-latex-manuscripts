<!-- SGA6 HAND-AUDIT CERT LOG — started 2026-07-03 (pivot from SGA5, at Floris's decision). Method mirrors the SGA5 audit exactly: page-by-page cross-read of sga6_fr_workpass.tex against the sga6.pdf scan; 600-1100dpi crops for any ambiguous glyph/subscript/accent; fix genuine edition defects, catalogue book-vs-edition differences in ERRATA_SGA6.md, keep the compile gate green after every change; never certify complete. -->

## SETUP (2026-07-03)
- **Canonical workpass**: `sga6_fr_workpass.tex` (copied from `SGA6_repair033_codex_display_labels_20260621/1/SGA6/cumulative/fr/sga6_fr.tex`, dated 2026-06-22, i.e. through 33 Codex repair rounds). 18882 lines. Self-contained (`\documentclass{article}`, amsmath/tikz-cd/etc., no external figures).
- **★ COMPILE GATE established: 392 pages / 0 LaTeX errors** (pdflatex ×2, `ocr_consolidate` conda env). Baseline PDF built clean. GATE = **392pp/0err** — must hold after every edit.
- **Scan**: `C:\Users\Floris\Documents\Papors\OS\sga6.pdf` = **702 pages** = full SGA6 volume (*Théorie des intersections et théorème de Riemann-Roch*, SGA 6, 1966-67; Exposés 0 / I–XIV + the RRR appendix). The transcription covers the whole seminar.
- **OFFSET**: volume printed page = PDF 0-based index **− 6** (⇔ PDF_idx = printed + 6). Anchored: idx 35 → printed p29 (Exp 0 App RRR §1.17–1.18). Cross-checks with TOC (App p20→idx26, Exp VIII p466→idx472). *Re-verify on the first far-page render in case of inserted plates.*
- **ERRATA**: `ERRATA_SGA6.md` to be created as book-vs-edition differences accumulate (typed `[corrected]`/`[faithful]`/`[normalized]`/`[non-error]`, as in SGA5).
- **Coordination note**: the SGA6 transcription is Codex-collaborative (through repair033). Any edition fixes I land must eventually be reconciled/merged back with Codex's ongoing work (cf. reference_codex_coordination) — do not let the audit workpass silently diverge.

**NEXT**: confirm OFFSET on a far page; then begin the page-by-page audit. Natural starting point — **Exposé I (complexes parfaits)**, since that's the notion SGA5's §6 appendix / Exp VIII / XII repeatedly cite ("SGA 6 III 4", tor-dimension, perfection relative); auditing it first ties the two volumes together.

## Audit log

### #1 (2026-07-03) — orientation + OFFSET confirmation + first content contact (p190, Exposé III §3.5, cohéreur Q)
- **OFFSET=6 confirmed at 3 well-separated points**: idx35→p29, idx62→p56, idx196→p190 (all `idx = printed + 6`). Uniform across the volume. The RRR appendix (Exp 0) additionally carries a top-header "-N-" appendix-internal count (idx62/p56 shows "-36-"); that inner count does NOT affect the offset. Navigate by the **bottom-centre** volume page number.
- **TOC caveat**: the printed TOC lists "Exposé I → 56", but scan p56 is still "0 App : RRR" (appendix runs long). Don't trust TOC page numbers near the Exp-0 appendix; navigate by exposé headers + content.
- **First content-alignment check PASS**: scan p190 ↔ workpass L4653–4685 (Preuve de (3.5.1)/(3.5.2), Čech resolution `(*) 0→E→∏f_{i*}f_i^*E→…`, spectral sequence `(**)`, `(***) R^qQ(f_*f^*E)≃f_*R^qQ(f^*E)`, `R^nQ(E)≃H^n(QE')`, `Q(E)≃E cqfd`). Displays match symbol-for-symbol.
- ⚠ **2 OPEN items on p190 to adjudicate next iteration (never-infer — need more evidence first):**
  1. **Prose restructuring**: scan p190 top reads "…**ainsi d'ailleurs que** les inclusions f_{i_0…i_p}:U_{i_0…i_p}=U_{i_0}∩…∩U_{i_p}→S." (continuation from p189); workpass L4653–4657 has "**Comme S est séparé**, les inclusions f_{i_0…i_p}:U_{i_0}∩…∩U_{i_p}→S **sont des morphismes affines**." → **render p189 (idx195)** to see the full book sentence and decide: faithful paraphrase (edition policy, document) vs genuine restructuring to flag.
  2. **Abutment notation**: scan `(**)` and the (3.5.2) SS look like `⟹ R^{*}Q(E)` (heavy-asterisk superscript = total degree) where workpass has `R^{p+q}Q(E)` → **600dpi crop** the superscript; likely a `*`→`p+q` notation normalization (cf. SGA5 A^•→A^* class), but confirm the glyph before classifying.
- **Observation**: SGA6's transcription (through 33 Codex repair rounds) still shows prose/notation choices that diverge from the scan at the same granularity SGA5 did — so the same fix/normalize/faithful adjudication discipline applies. ERRATA_SGA6.md to be created once the first genuine finding lands.
- gate unchanged (392pp/0err, no .tex edit this iteration).

### #2 (2026-07-03) — resolved the two open p190 items → ERRATA_SGA6.md created
- **(b) abutment notation RESOLVED**: 700dpi crop confirms the book's superscript is a **heavy asterisk** — `⟹ R^{*}Q(E)`; workpass has `R^{p+q}Q(E)`. Notation expansion (`*` total-degree → explicit `p+q`), same object → **ERRATA [normalized]**. Watch for systematicity.
- **(a) prose sentence RESOLVED (needs a decision)**: p189 (idx195, Exp II/III "-30-", bottom p189) shows the full book sentence spanning p189→p190: "…les inclusions **f_i:U_i→S sont des morphismes affines, ainsi d'ailleurs que** les inclusions f_{i_0…i_p}:**U_{i_0…i_p}=**U_{i_0}∩…∩U_{i_p}→S." The workpass **condensed** it — dropped the `f_i` clause and the `U_{i_0…i_p}=` notation. Mathematically lossless, but it **omits authored prose** → **ERRATA [flagged — condensation]**, NOT edited yet.
- **★ STRATEGIC SIGNAL (raise with Floris):** unlike SGA5 (which reworded prose but did not drop it), the SGA6 transcription here *condenses / omits* authored text. Two questions this raises, both above the level of a single page:
  1. **Standard**: for SGA6, does Floris want strict faithfulness (restore every dropped clause — potentially a large re-transcription pass) or a clean readable edition that tolerates lossless condensation? SGA5's answer was "faithful, don't add/drop content." Default to that unless told otherwise, but **flag if condensation proves pervasive**.
  2. **Coordination**: the workpass is Codex's repair033 copy. `.tex` fixes here diverge from Codex → must be tracked (CERT_LOG) and merged. Until a protocol is set, prefer **document-in-errata over edit-in-place** for borderline items; reserve in-place edits for clear-cut math/symbol errors.
- **Method note**: to gauge scope cheaply, upcoming iterations will diff a handful of pages prose-level (not just displays) and tally condensation frequency; if low → fix instances; if high → escalate the standard question before mass-editing.
- gate unchanged (392pp/0err, no .tex edit).

### #3 (2026-07-03) — ★★★ SCOPE FINDING: the SGA6 transcription is a PARAPHRASE, not a faithful transcription → LOOP PAUSED for Floris's decision
- **Second scope-probe page: p300 (idx306, Exposé V §1.5, λ-anneaux, `H` functor / symmetric functions).** Full prose+math diff of scan p300 vs workpass L7553–7576 shows the transcription **paraphrases and condenses at multiple levels on a single page**:
  1. **adds a word** — scan "la i-ème fonction symétrique des T_j" → workpass "…symétrique **élémentaire** des T_j" (interpolation, cf. SGA5 #59);
  2. **rewords** — "qu'on en déduit" → "qui s'en déduit"; "nous permettra" → "permet" (dropped `nous`, tense change);
  3. **restructures** — book's single semicolon-joined sentence split into two;
  4. **★ drops a MATHEMATICAL step** — scan identification display is the 4-term chain `H(K[X]) ≃ H(K[T]^{𝔖_n}) →~ H(K[T])^{𝔖_n} ⊂ H(K[T])` (H of the invariant *ring*, iso to invariants *of* H); workpass (L7565) collapses to 3 terms `H(K[X]) ≃ H(K[T])^{𝔖_n} ⊂ H(K[T])`, dropping `H(K[T]^{𝔖_n}) →~`. **450dpi-confirmed.**
- **Combined with #2 (p189–190 dropped clause + notation), this is 2-for-2**: the "repair033" SGA6 transcription (33 Codex rounds) is a **readable paraphrase/condensation**, NOT a faithful page-image of the book like SGA5's edition was.
- **⇒ Consequence**: "do SGA6 the way SGA5 was done" (a *faithful* edition, page-by-page verified vs the scan) is **not an audit task here — it's a re-transcription task**, because the source I'd be auditing is itself a paraphrase. Cataloguing paraphrase-deviations page-by-page would be low-value until the target standard is set. **Per-item ERRATA_SGA6 entries are on hold pending that decision.**
- **★ DECISION NEEDED FROM FLORIS (loop paused, no wakeup re-armed):**
  - (A) **Re-transcribe SGA6 faithfully** (regenerate via the Kimi/Codex pipeline with a faithfulness-first prompt, as SGA5 evidently was), then audit → true parity with SGA5. Biggest effort.
  - (B) **Keep the paraphrase, audit for MATH only** — verify every mathematical statement/formula is correct & complete (restore drops like the p300 iso), accept prose paraphrasing; label the release honestly as a *math-verified readable rendering*, a different (lesser) standard than SGA5's faithful edition. Medium effort.
  - (C) **Accept as-is** (readable modern rendering, spot-checked), quality-statement says "paraphrased, not a faithful transcription." Least effort, lowest fidelity.
  - My lean: **(B)** as the pragmatic middle — SGA6's value is mostly in its mathematics being right & complete, which is auditable; full prose-faithfulness (A) is a large re-transcription for lower marginal value. But this is a product-standard call that's genuinely Floris's.
- gate unchanged (392pp/0err, no .tex edit; loop NOT re-armed — awaiting decision).

### #4 (2026-07-03) — ★ COURSE CORRECTION (Floris, sharply): the task is FIX, not audit; standard is SYMBOL-LEVEL SOURCE-COMPLETE (archival)
- **I framed #2/#3 wrong.** The task is NOT to "audit" or "verify the math" or weigh "faithful vs readable" — it is to **FIX SGA6 to reproduce Grothendieck's text symbol-level, source-level complete**, exactly as SGA5 was *fixed*. This is **archival work**: the value is being source-accurate ("no one wants the SGA6 Claude version, they want the SGA6 Grothendieck version"). My "math is the point / option B" editorializing was flatly wrong and unwelcome. Do not repeat.
- The paraphrase findings in #2/#3 are therefore not a "decision" — they are the **fix backlog**. Every drop/reword/interpolation I find gets **corrected in the .tex to match the scan**, page by page.
- Provenance correction: the SGA6 transcription is **Codex's** (repair-chain, latest = repair033), NOT Kimi's. Plan per Floris: (1) get the best scans, (2) Codex does the bulk transcription, (3) I go page-by-page and FIX to the source. Repair033 workpass = best available but **condensed (392pp vs 702) + paraphrased + missing Exposé XIII** → substantial fix/restore work.
- **FIRST SOURCE-FIX applied — p300 (Exp V §1.5), .tex L7555–7567**: matched the scan exactly — removed interpolated «élémentaire»; «.»→«;»; «qui s'en déduit»→«qu'on en déduit»; «permet»→«nous permettra»; inlined the two `H(...)` terms (book has them inline); **restored the dropped intermediate iso** `H(K[T]^{𝔖_n}) →~ H(K[T])^{𝔖_n}` in the identification display. Recompiled ×2 → **0 errors** (page count 392, unchanged by this small fix; SGA6 gate = "compiles 0-err", count will GROW as content is restored, not frozen like SGA5's 306).
- **Method going forward** = SGA5's, but in FIX mode: page N → render scan (idx = printed+6) → make the .tex reproduce it symbol-level (restore drops, exact wording, exact math) → recompile 0-err → log. ERRATA_SGA6 reserved for genuine *book* typos (the edition still corrects those + documents, per SGA5 policy).
- ⚠ still to do (Floris's step 1): source a **best-quality SGA6 scan**; current `OS/sga6.pdf` is readable at 200dpi+crops but flag any illegible page.

### #5 (2026-07-03) — STEP ONE (best scans): searched; all available SGA6 scans are 118 DPI → need Floris to supply hi-res
- **Scan quality**: `OS/sga6.pdf`, `SGA6_repair033/external_witnesses/sga6_slmath_postscript_scan.pdf`, and `SGA restart/SGA6_Indexes_Complete/SourceScan/SGA6_source_pages_001_702_original_complete.pdf` are ALL the same **~118 DPI** JPEG scan (1000×1374 px / 612×792pt; producer `pdfTeX pdfcrypt`, D:2002 = the 2002 SLMath/MSRI scan). Propagated across every package.
- **Contrast**: SGA5's source scan = `2176×3035 ≈ 373 DPI` (`SGA restart/.../SourceScan/SGA5 - Source Scan pages 13-496 cumulative.pdf`). So hi-res SGA scans exist; SGA6's just isn't on disk.
- **Web**: archive.org has no math SGA6 (copyright noise only); Springer LNM 225 (DOI 10.1007/BFb0066283) is the hi-res original but paywalled — not downloadable by me. SGA5 hi-res metadata stripped → no provenance lead.
- **⇒ Asked Floris to supply a hi-res SGA6 scan** (Springer via institution, or wherever SGA5's 373dpi came from); drop in `OS/` and I switch immediately. **The 118dpi scan is NOT trustworthy for finest symbol calls (prime/subscript/⁂-vs-*)** — my earlier "700dpi crops" were UPSCALING 118dpi, i.e. not real detail.
- **.tex lineage resolved**: one Codex transcription; **repair033 (392pp) = latest/longest**, the "complete 001-702" build is an earlier shorter (340pp) checkpoint of the SAME paraphrased text (verified §1.5 paraphrase identical in both). Fix repair033 workpass.
- **Interim plan (loop keeps running, not paused)**: do the scan-quality-independent restoration — de-paraphrase prose and restore dropped clauses/steps back to Grothendieck's wording (legible at 118dpi) — and RESERVE the final subtle-symbol fidelity pass for when a hi-res scan lands.

### #6 (2026-07-03) — ★ HI-RES SCAN FOUND (supersedes #5) + METHOD SET = one-shot manual page-by-page scribe
- **★ REFERENCE SCAN (use this, NOT the 118dpi one):** Floris dropped `C:\Users\Floris\Documents\Papors\OS\Théorie des Intersections et Théorème de Riemann-Roch.pdf` = the **Internet Archive** scan, item `theoriedesinters0225bert` (https://archive.org/details/theoriedesinters0225bert). **360 DPI** main image (2199×3425 jpx per page; a ~120dpi thumbnail is the 2nd image — extract image index 0/the big one), **720 pages COMPLETE**, **embedded OCR text layer** (`page.get_text()` returns garbled-but-usable French — great for fast deviation-finding; the 360dpi image is authoritative for glyphs). Same quality tier as SGA5's 373dpi. #5's "118dpi ceiling / need hi-res from Floris" is RESOLVED. (archive.org item is under the French title — I'd searched "SGA6" and missed it.)
- **★ NEW OFFSET — this IA scan uses ORIGINAL PER-EXPOSÉ page numbering** (NOT the 118dpi scan's continuous +6). Front matter idx0–13 (LNM series, title idx4, Préface idx6, Introduction idx8–10, TdM idx12–13). **Exposé 0 (Esquisse) starts idx14 = its p1**; Exp0 internal page = `idx − 13` (idx24="-11-", idx31="-18-", idx32=Biblio). **App RRR starts idx33** (title) / idx34 (Chap I); App-RRR page = `idx − 33` (idx43="-10-", idx51="-18-"). ⇒ **map each exposé's own offset as reached; verify per-page via the OCR "- N -" marker** (bottom-centre in image). Old 118dpi offset (+6) is retired.
- **★ METHOD (Floris's directive) = ONE-SHOT manual page-by-page SCRIBE.** Sweep page 1 → end, ONCE. For each scan page: read the 360dpi image (+ OCR text) and write faithful LaTeX reproducing it symbol-level — transcribe from scratch wherever the workpass paraphrases. repair033 workpass = scaffold to rewrite freely, NOT a source of truth. "When it's done, it's done." Also an efficiency experiment vs SGA5's layered pipeline (transcribe→checks→agents→page-by-page→QA); Floris's hypothesis: one-shot is cheaper token-wise.
- **Mindset (record, per Floris):** do NOT hedge on time. SGA 1–4 = ~4 yrs of seminars (1960–64) + ~decade to publish (1968–73), dozens of person-years. This project ≈ 3 weeks / 4–5 days concerted. A week to faithfully set ONE volume = publication-grade efficiency, not a cost to agonize. Just do it, page by page, for real.
- **SWEEP CURSOR → start Exposé 0 p1 = idx14.** Go in printed order. Prior fix #4 (p300 §1.5) stands; re-verify it against the 360dpi scan when the sweep reaches Exp V. Track last-faithful (idx, printed-page) here each iteration so the linear sweep resumes cleanly.

### #7 (2026-07-03) — ★ METHOD confirmed by Floris + Préface & Introduction scribed symbol-complete
- **Floris nailed down the method (final):** page 1 → end, ONE pass; **per page, first up the scan contrast, then make 3–5 zoomed PNG bands, then verify EVERY word and EVERY symbol against the scan** and make the cumulative `.tex` reproduce it — before moving to the next page. **No OCR-swap / heuristic.** "Every page is trash / SGA6 is not done / you're doing it on your own." Do it by hand, foreground, **no Workflow/agents** (overrides the ultracode nudge; this is his standing rule). Token cost is NOT a concern; compare efficiency vs SGA5's layered pipeline only at the end.
- **Contrast+crop tool built** → `%TEMP%\pgcrop.py`: fitz render (grayscale, 500 dpi) → `ImageOps.autocontrast(cutoff=1)` → `Contrast(2.0)` → `Sharpness(1.7)` → 4 vertical bands (10% overlap) saved to scratchpad `p<idx>_b<n>.png`. Enhanced bands are crisp at 500 dpi; typewriter emphasis-underlines and grave/acute accents are clearly legible. Reuse per page (adjust nb=3–5 by density).
- **PAGES DONE (faithful, scan-verified on 360 dpi IA scan):**
  - **Préface (idx6)** — workpass already faithful; book typo `régigé`→`rédigé` was already corrected. Errata logged. No `.tex` change.
  - **Introduction (idx8–10) — SCRIBED, L101–113 rewritten to match the scan symbol-complete.** Restored: the dropped **Hartshorne "Residues and Duality"** citation; **6 paren→comma** swaps back to the book's parentheses; abbreviations `Exp.\ II`, `Exp.\ XIV`, `n\textsuperscript{o/os}`; removed interpolated words («le» Séminaire Chevalley, «de» rapport Grothendieck, «du» style, «numéro»→`n°`); restored **book capitalization** «Géométrie Algébrique»; restored **underlined emphasis** (`globale`, `réguliers`, `catégories dérivées`, `site annelé`, `topos annelé`, `complexe de Modules parfait`, `théorie locale`, `anneau de Chow`); removed workpass-added guillemets/`\emph` on titles the book leaves plain. Book typos corrected+errata: `coéfficients`, `Algèbrique`(grave), `extrêment`. Compile **0-err, 392pp**.
- **SWEEP CURSOR → Table des matières (idx12–13), then Exposé 0 p1 = idx14.** Resume the linear sweep there with the contrast+bands method.

### #8 (2026-07-03) — Table des matières (idx12–13) scribed symbol-complete; ★ workpass page numbers were WRONG
- **Crop guidance from Floris (applied):** text pages → **3 bands**; math/diagram pages → **5+ bands**, diagrams analyzed whole. Affordable — confirmed.
- **★ The workpass TdM had CORRUPTED page numbers.** Scan (360 dpi) vs workpass: **I 78** (workpass 56 ✗), II 160 ✓, **III 222** (was 190 ✗), **IV 274** (was 222 ✗), V 297 ✓, VI 365 ✓, VII 416 ✓, VIII 466 ✓, IX 498 ✓, X 519 ✓, XII 595 ✓, XIII 616 ✓, XIV 667 ✓. (Some right, some wrong — repair033 numbers are unreliable; transcribe every one from the scan.) Sequence is monotonic 1,20,78,160,222,274,297,365,416,466,498,519,595,616,667.
- **Other TdM fixes to scan:** all titles restored to the book's **Title Case** (workpass had lowercased); **VII title** was paraphrased («calcul de $K^\circ$ d'un éclatement» → book «Calcul du $K^\circ$ d'un Schéma Éclaté»); **two Index entries restored** (Index Terminologique 691, Index des Notations 696 — dropped by workpass); RRR appendix listed **unlabelled under Exposé 0** (removed the workpass's invented "Appendice" column); Exp X sub-lines restored (par O. Jussila / Avec un Appendice par A. Grothendieck / Spécialisation en Théorie des Intersections). **Layout redone to the scan's heading + `\dotfill` leader style** (was a longtable). Compile **0-err, 393pp** (grew +1).
- Book typo **Fibre→Fibré** (VI) logged in errata. IX title rendered `$K_\bullet$` («Groupes K.») — **verify the glyph** when the sweep reaches Exp IX body.
- **⚠ pagination note:** these are THIS IA scan's (LNM 225) page numbers; they differ from the 118 dpi 2002 scan the workpass came from (that had offset-6 continuous numbering, e.g. old "p190 = Exp III"). Navigate the IA scan by idx + printed page; vol-page ≈ idx − 13 for Exposé 0 (verify per exposé). Old CERT_LOG #1–#3 page refs are for the 118 dpi scan — ignore for the IA sweep.
- **SWEEP CURSOR → Exposé 0 p1 = idx14** (first math-bearing content: Riemann–Roch formula — use 5+ bands).

### #9 (2026-07-03) — Exposé 0 p1 (idx14) scribed symbol-complete (5 bands) — ~15 deviations on one page
- **Title/heading:** book title is **ALL-CAPS + underlined** on two lines («ESQUISSE D'UN PROGRAMME POUR UNE THÉORIE DES INTERSECTIONS / SUR LES SCHÉMAS GÉNÉRAUX») and **par A. Grothendieck underlined** — workpass had it lowercased, not underlined, `\large`. Fixed (caps restored + `\underline`).
- **Intro para:** restored dropped citation **[2]** (« rapport de Borel--Serre [2] ou »); «l'introduction»→**«l'Introduction»** (cap); «cité [RRR] **dans** la suite,»→book **«(cité [RRR] par la suite)»** (parens + «par»).
- **§1 structure:** workpass **invented a subsection title** «1. Rappelons la formule de Riemann--Roch» and **duplicated** the opening sentence — book has only a numbered «1.» + running text. Fixed to `\subsection*{1.}` (matches the untitled §4–§7 style).
- **§1 math (book notation restored):** global `\cl` macro `cl`→**cℓ** (`\mathrm{c}\ell`); **f_! → f_∗** ×3 (book uses the star pushforward everywhere — 1.1 LHS, def, 1.2 LHS); **⊗ → ⊗_ℤ** (dropped subscript); «est notée $\cl(F)$»→«est notée **par** $\cl(F)$»; «celui du premier **membre**»→«celui du premier» (removed interpolated «membre»); «Chern sur X **et** sur Y / tangents à X **et** à Y»→book **«resp.»** both; removed 2 interpolated commas around «après multiplication par $\Todd(T_Y)^{-1}$»; def eq ends **«;»** (was «.»); **(1.2)** product **dot** $\Todd(T_f)\cdot\ch_X(F)$ (was thin space); **(1.3)** `f^*T_Y`→**`f^*(T_Y)`** (parens restored).
- **Book typos → errata:** introductif→introductive; coéfficients→coefficients; (1.2) missing closing paren balanced.
- **⚠ low-confidence:** (1.3) ends with **«,»** per the 360 dpi scan (comma vs period ambiguous; «Ainsi» follows capitalized) — set to comma, re-verify if a sharper crop is warranted.
- Compile **0-err, 393pp**.
- **SWEEP CURSOR → Exposé 0 p2 = idx15** («Ainsi $T_f$ joue le rôle…», immersion case $T_f=-\check N_{X/Y}$, then §2).

### #10 (2026-07-03) — Exposé 0 p2 (idx15) scribed symbol-complete (5 bands) — ~12 deviations
- **★ (1.3) punctuation RESOLVED:** book continues «…$\in K(X)$**,** de sorte que $T_f$ joue le rôle…» — so (1.3) ends with a **comma** (my #9 call was right) and the workpass's «**Ainsi**» was wrong → **«de sorte que»** (lowercase, continues the sentence).
- **Underlines restored:** «\underline{fibré tangent relatif virtuel}» (1st occ), «\underline{anneaux de Chow}».
- **Dropped parentheticals restored:** «(i.e.\ à application tangente partout surjective)» after «lisse»; «(fibré tangent le long des fibres)» — and $T_f=T_{X/Y}$ set as a **display** with that annotation (workpass had inlined it, no annotation).
- **Ň check restored:** «où $\check N_{X/Y}$ désigne le faisceau normal» (workpass had plain $N_{X/Y}$; the display $T_f=-\check N_{X/Y}$ already had it — internal inconsistency fixed).
- **f_! → f_∗:** §2 homomorphism $f_*:K(X)\to K(Y)$ (book star).
- **§2 invented title removed:** «\subsection*{2. La suppression du corps de base}» → **«\subsection*{2.}»** (book has only «2.» — same invented-title defect as §1).
- **List a)/b)/c):** book **Capitalizes** the first word and ends each with **«.»** (workpass had lowercase + «;»); removed interpolated «suivant» and the comma after «chemin faisant» → «du problème~:».
- **Book typo → errata:** débarasser→débarrasser (list a).
- Compile **0-err, 393pp**.
- **SWEEP CURSOR → Exposé 0 p3 = idx16** (§2.1: factorization $X\xrightarrow{i}X'\xrightarrow{f'}Y$, formula (2.1) $T_f=i^*T_{X'/Y}-\check N_{X/X'}$).

### #11 (2026-07-03) — Exposé 0 p3 (idx16) RE-TRANSCRIBED — most corrupted page yet (§2.1 formula WRONG, §2.2 fully paraphrased)
- **★ §2.1 formula was WRONG in the workpass.** Book: factorization tagged **(2.1)**, then **(2.2): $\check T_f=\cl(\underline\Omega^1_{X'/Y})-\cl(\underline N_{X/X'})$** (cotangent/conormal, the DUAL $\check T_f$). Workpass had left the factorization untagged and written a different formula «$T_f=i^*T_{X'/Y}-\check N_{X/X'}$» as (2.1). Corrected to book.
- **★ NEW RECURRING CONVENTION:** the book **underlines Module/sheaf/ideal letters** ($\underline\Omega$, $\underline N$, $\underline J$) — reproduced as `\underline{...}` (720 dpi-tight-crop confirmed). Watch for this throughout SGA6.
- **§2.1 prose restored:** «immersion fermée, et $f'$ un morphisme lisse~; par exemple on pourra prendre» (workpass «fermée et $f'$ est lisse; on pourra»); «(ou Module cotangent relatif…)» parens; «l'Idéal…définissant le sous-schéma fermé $X$» (workpass dropped «le sous-schéma fermé»); **«comme $X$ et $X'$ sont réguliers, on en conclut»** (workpass had PARAPHRASED «Les hypothèses de régularité faites…impliquent»); **«Enfin $\check T_f$ désigne le dual de $T_f$»** (workpass had WRONG «$\check N$ désigne le dual de $N$»); «(Exp.\ VIII)» (workpass «dans l'exposé VIII»).
- **★ §2.2 fully re-transcribed** (workpass was a heavy paraphrase). Book: «sur le modèle de celle déjà connue pour les schémas algébriques lisses et quasi-projectifs» (not «des variétés lisses sur un corps»); «et à fortiori il n'a pas été entrepris dans le Séminaire» (dropped); «On introduit par contre un autre anneau, qui jouera un rôle analogue à celui de l'anneau de Chow» (not «Nous adopterons donc…en définissant directement un anneau qui remplace»); «$\otimes_{\mathbb Z}\mathbb Q$ dans le cas où $X$ est quasi-projectif et lisse sur un corps $k$. Cet anneau est l'anneau gradué associé à $K(X)$…» (not «$\otimes\mathbb Q$ dans le cas classique»); «\underline{filtration topologique}» (underlined+quoted); $\operatorname{Filt}^i_{\mathrm{top}}$ (not $\Fil^i$); «moving lemma» quoted; $\Gr^{\bullet}_{\mathrm{top}}(X)$ (graded dot).
- **Book typos → errata:** quasi-porjectifs→quasi-projectifs; sous-schémas→sous-schéma; coprs→corps.
- **⚠ low-confidence:** «défini par (2.1)» — book «(2 1)» could be (2.2); kept (2.1).
- **⚠ for idx17+:** make $\Gr_{\mathrm{top}}$ consistent with $\Gr^{\bullet}_{\mathrm{top}}$ where it recurs; re-transcribe the §2.2 tail (L256 «transformant la classe…») and §2.3/§2.4 against the scan — expect heavy paraphrase.
- Compile **0-err, 393pp**.
- **SWEEP CURSOR → Exposé 0 p4 = idx17** («transformant la classe d'un cycle premier $Z$ en $\cl(\mathcal O_Z)$…», §2.2 tail, §2.3).

### #12 (2026-07-03) — Exposé 0 p4 (idx17) scribed (§2.2 tail + §2.3) — many deviations
- **Global fix (per Floris):** `\Gr_{\mathrm{top}}` → `\Gr^{\bullet}_{\mathrm{top}}` (book writes the topological graded ring with the degree dot, `Gr^·_{top}`) — replace_all. **⚠ caused a double-superscript** where L18340 had a pre-existing `\Gr_{\mathrm{top}}^\bullet` (subscript-then-superscript form); fixed by dropping the redundant trailing `^\bullet` (replace_all `\Gr^{\bullet}_{\mathrm{top}}^\bullet`→`\Gr^{\bullet}_{\mathrm{top}}`). **Lesson: a replace_all on a macro+subscript can collide with a pre-existing superscript — grep for `top}}^` after such a change.**
- **§2.2 tail:** «(transformant la classe d'un cycle premier $Z$ en $\cl(\underline O_Z)$,)» **parenthesized** (was un-parenthesized); `\mathcal O_Z`→`\underline O_Z`; «(Exp.\ XIV 4.2)» parens; «$A(X)$~;»; **★ WRONG cross-ref «6.4»→«4.4»** (real content error in workpass); «\,«moving lemma»\,» quoted.
- **§2.3:** «dans $\Gr^{\bullet}_{\mathrm{top}}(X)$,» (was «:»); (2.3) `\operatorname{Filt}^{i+1}_{\mathrm{top}}` (was `\Fil^{i+1}`); «$\lambda$-\underline{filtration}»; `\operatorname{Filt}^i` (was `\Fil^i_\lambda`) ×2; display index **r→k** ($x_r,i_r$→$x_k,i_k$); removed 2 interpolated commas around «dans le cas envisagé ici».
- **★ CONVENTION DECISION:** the **structure sheaf O is underlined** in the book → render `\underline O` (not `\mathcal O`); convert workpass `\mathcal O`→`\underline O` per page going forward.
- **Book typo → errata:** tranformant→transformant.
- **⚠ low-confidence (re-verify if a clean crop is cheap):** «$\lambda^j$ ($j\le i$)» — book glyph could be «=» (kept ≤, math-correct); «expressions» could be singular; «$\cl(F)\in K(X)$» (∈ vs ⊂).
- Compile **0-err, 393pp**.
- **SWEEP CURSOR → Exposé 0 p5 = idx18** (§2.3 tail «est un isomorphisme modulo torsion…» + §2.4; note L292 has `\cl(\mathcal O_X)`→`\underline O_X` to convert).

### #13 (2026-07-03) — Exposé 0 p5 (idx18) scribed (§2.3 tail + §2.4) — ~12 deviations
- **§2.3 tail:** «**donc**»→**«dont»** (wrong connective in workpass); «, où on remplace $\Fil_{\mathrm{top}}$ par $\Fil_\lambda$,»→**«(où on remplace $\operatorname{Filt}^i_{\mathrm{top}}$ par $\operatorname{Filt}^i$)»** (parens + correct Filt notation); «On montre, Exp. V, grâce au fait, Exp. VI,»→**«On montre (Exp.\ V), grâce au fait (Exp.\ VI)»**; «spécial»→**«\underline{spécial}»**; «c'est-à-dire un $\lambda$-anneau au sens de l'exposé V»→**«(i.e.\ un $\lambda$-anneau au sens de Exp.\ V)»**.
- **§2.4:** «$\Gr^{\bullet}_{\mathrm{top}}(X)$:»→«, c'est» (colon→comma); «torsion, c'est-à-dire à»→«torsion i.e.\ à»; «(Exp. XIV no 4)»→«(Exp.\ XIV n\textsuperscript{o}~4)»; **the homomorphism $f_*:K(X)\to K(Y)$ was DISPLAYED in the workpass — book has it INLINE** (fixed); «$\Fil^i_\lambda$»/«$\Fil^{i-d}_\lambda$»→**«$\operatorname{Filt}^i$»/«$\operatorname{Filt}^{i-d}$»** (no λ subscript); removed 2 interpolated commas around «par passage aux gradués associés»; «prouver, Exp. VII,»→«prouver (Exp.\ VII)»; **(2.5) $\otimes\mathbb Q$ → subscript $_{\mathbb Q}$** (book writes «$\Gr^\bullet(X)_{\mathbb Q}$»); «\,«image directe de cycles»\,»; «étant **un** morphisme propre»→«étant morphisme propre» (removed «un»).
- **⚠ low-confidence:** book «…dans Gr (Y).» may drop the graded dot on the 2nd Gr (kept $\Gr^\bullet(Y)$, correct); «…par Q D'autre part» book may drop the sentence period (kept «.»).
- Compile **0-err, 393pp**.
- **SWEEP CURSOR → Exposé 0 p6 = idx19** (§3 «Le cas des schémas généraux» — **check if the §3 title is invented** like §1/§2; §3.1 $K_\bullet$/$K^\bullet$ distinction; convert `\cl(\mathcal O_X)`→`\underline O_X`).

### #14 (2026-07-03) — Exposé 0 p6 (idx19) scribed (§3 + §3.1 + naive formula) — heavy page, ~14 deviations
- **§3 title «Le cas des schémas généraux» was INVENTED** → `\subsection*{3.}` (confirms the pattern: §1/§2/§3 all had invented descriptive titles the book lacks — just numbers).
- **§3.1 prose:** «cohérents, ou» comma restored; «un schéma (disons noethérien, pour simplifier) général» (parens; workpass had commas); «structure d'anneau (et même de $\lambda$-anneau augmenté), alors» (parens); **covariant class map $\cl_\bullet$** restored + **dropped parenthetical** «(où $\cl_\bullet(\underline F)$ désigne la classe de $\underline F$ dans $K_\bullet(X)$)» restored; structure sheaf `\underline O_X`; «et **à** des»→«et des»; **★ the whole sentence «Pour notre formulation…à l'exclusion de $K_\bullet(X)$, $K_\bullet(Y)$» is UNDERLINED** (author emphasis) → added `\usepackage[normalem]{ulem}`, wrapped in `\uline{…}`.
- **Naive formula:** `\cl`→**`\cl^\bullet`** (contravariant, superscript dot); sheaves **$\underline E$/$\underline F$** underlined; workpass had plain `\cl(F)`.
- **«catégories dérivées» underlined; «\,mauvais\,» guillemets; $F$→$\underline F$** in «car même si F…».
- **★ class-map family:** `cℓ` / `cℓ_•` (→$K_\bullet$) / `cℓ^•` (→$K^\bullet$), distinguished by sub/superscript dot.
- **Book typos → errata:** «servie»→«servi»; naive-formula LHS «E» (reproduced faithfully, flagged as typo for F).
- **⚠ kept «(1.2)»** (band1 looked like «(2.2)» but the far-left digit resisted a clean crop; §2.4 used «(1.2)» + math consistency → kept (1.2), likely a book typo if it really is (2.2)); **⚠ sheaf-underline consistency** — re-check p1 §1 whether $F$ is underlined there too.
- Compile **0-err, 393pp**.
- **SWEEP CURSOR → Exposé 0 p7 = idx20** (rest of «…le complexe $Rf_*(F)$ … a un sens dans $K^\bullet(Y)$» + §3.2 «localement d'intersection complète», $d(f)$).

### #15 (2026-07-03) — Exposé 0 p7 (idx20) — ★★ MASSIVE CONDENSATION restored (~3 paragraphs → 2 sentences)
- **The workpass had collapsed a whole page of §3.1** (the perfect-complexes / triangulated-category motivation) into 2 sentences. RESTORED the full book text:
  - dropped clauses «auxquels on ne saurait associer de classe dans $K^\bullet(Y)$, cependant» and «dont les $R^if_*(\underline F)$ sont des faisceaux de cohomologie»;
  - paraphrase → book «supposons que $\underline F$ soit de tor-dimension finie sur $\underline O_Y$, ce qui sera le cas si $\underline O_X$ est de tor-dimension finie sur $\underline O_Y$ et si de plus $F$ est localement libre» (workpass had «lorsque F… sur Y, par exemple lorsque f…»);
  - the full definition of **«parfait»** (2 characterisations: cohérent+tor-dim globale finie; or iso in $D(U)$ to a bounded loc-free-finite-type complex);
  - «Du point de vue de l'Algèbre Homologique… aussi bons… généralisation naturelle»;
  - «sous-catégorie triangulée… cônes (ou mapping cylinders)»;
  - «à toute catégorie triangulée $C$ on associe $K(C)$… [display $\cl(K)-\cl(K')-\cl(K'')$]… [distinguished-triangle **tikzcd diagram** $K'\to K\to K''$]»;
  - «Ce qui remplace… [RRR]… tout complexe parfait $L_\bullet$ globalement iso dans $D(Y)$ à un complexe $L'$… (Exp.\ II)… [display $K^\bullet(X)\to K(\Parf(Y))$]… isomorphisme. Donc… [display $\cl^\bullet(L_\bullet)\in K^\bullet(Y)$]».
- structure sheaf `\underline O_X/O_Y`, `\underline F` throughout.
- **★★ page 393→394** — restoring dropped content GROWS the count (as Floris predicted; the SGA6 gate is "compiles 0-err", NOT a frozen count).
- **⚠⚠ CRITICAL for idx21:** the restored §3.1 now ends MID-SENTENCE at «$\cl^\bullet(L_\bullet)\in K^\bullet(Y)$,» and the workpass's `\subsubsection*{3.2}` follows PREMATURELY — the book's **page-8 §3.1 continuation is still condensed/missing**. On idx21, restore page-8 content BEFORE §3.2 and reconcile whether the workpass's «§3.2 / Pour donner un sens à (1.2)…» is the book's real §3.2 or more §3.1.
- **⚠ low-confidence glyphs:** «L.»→$L_\bullet$; «L!»→$L'$ (prime); the $\cl(K)$ in the $K(C)$ relation (used `\cl`).
- Compile **0-err, 394pp**.
- **SWEEP CURSOR → Exposé 0 p8 = idx21** (continuation «…$\cl^\bullet(L_\bullet)\in K^\bullet(Y)$, [où …]» + rest of §3.1 + locate the real §3.2).

### #17 (2026-07-03) — Exposé 0 p8 (idx21) — restored the #15 gap (§3.1 continuation) + fixed §3.2 page-8 content
- **★ Restored the page-8 §3.1 continuation** (the mid-sentence gap from #15), BEFORE the (correctly-placed-now) §3.2: «qui n'est d'ailleurs autre que [display $\cl^\bullet(L_\bullet)=\sum_i(-1)^i\cl^\bullet(L'_i)$] où $L'$ est comme ci-dessus… Ceci posé, on définit un homomorphisme (3.1)… morphisme \underline{propre de tor-dimension finie}… [**display (3.2)** $f_*(\cl^\bullet(\underline F))=\cl^\bullet(Rf_*(\underline F))$]… $K(\Parf(X))$… [display $Rf_*:\Parf(X)\to\Parf(Y)$]».
- **★ §3.2 placement RECONCILED:** the workpass's §3.2 IS the book's §3.2 (was just premature). Book §3.2 opens «Pour donner un sens à **(1.2)**» — so the workpass's «(1.2)» there is CORRECT; the book genuinely uses (2.2) at the §3 opening AND (1.2) at §3.2.
- **§3.2 fixes:** restored **dropped formula (3.3)** $f_*:\Gr^\bullet(X)_{\mathbb Q}\to\Gr^\bullet(Y)_{\mathbb Q}$; «c'est-à-dire»→«i.e.» ×2; parens «(modulo un décalage et modulo torsion)», «(avec les notations de loc. cit.)»; `\underline N_{X/X'}`, `\underline O_{X'}`×2, «Idéal»; «plus haut,»; **★ the «On se permettra…localement…» text is a FOOTNOTE(\*) in the book** — converted from a body paragraph to `\footnote{}` on «localement d'intersection complète»; underlined the l.c.i. term.
- **Numbering now consistent:** (3.1) p6, (3.2) p8, (3.3) p8, (3.4) p9 — the workpass's «d'où un homomorphisme (3.3)» (p9) now resolves to the restored (3.3).
- **Book typos → errata:** sous-schémas→sous-schéma; défini→définie; insersection→intersection.
- **⚠ low-confidence:** display-1 LHS «cℓ(L.)» rendered $\cl^\bullet(L_\bullet)$ (superscript dot may be absent in the book's LHS).
- Compile **0-err, 394pp**.
- **SWEEP CURSOR → Exposé 0 p9 = idx22** (§3.2 cont: «Si $f$ est un morphisme l.c.i., on introduit… $d(f)$…» + formula (3.4) + «d'où un homomorphisme (3.3) de degré $-d$»; verify the workpass's $d(f)$/(3.4) block against the scan).

### #19 (2026-07-03) — Exposé 0 p9 (idx22) scribed (§3.2 tail + §3.3 + §4 opening) — no-flag pass
- **★ $d(f)$ formula: `f^{-1}`→`f'^{-1}`** — book uses $f'$ (the smooth part of the factorization $X\xrightarrow{i}X'\xrightarrow{f'}Y$): $d(f)(x)=\dim_x(f'^{-1}(f(x)))-\operatorname{codim}_x(X,X')$. Workpass had dropped the prime → real error (resolved by an 11× crop, no flag).
- **(3.4):** `\Fil`→`\operatorname{Filt}` ×2 ($f_*(\operatorname{Filt}^iK^\bullet(X)_{\mathbb Q})\subset\operatorname{Filt}^{i-d}K^\bullet(Y)_{\mathbb Q}$).
- **§3.3:** **★ «K-formalisme»→«$\lambda$-formalisme»** (real error, K vs λ); «(suivie dans Borel--Serre)» parens (was commas); «Exp. XIV, no. 1,»→«Exp.\ XIV n\textsuperscript{o}~1»; **«modules»→«Modules»** (×3 — recurring: the L357+ section systematically lowercased Module); `\uline` the clause «dans le cas d'un morphisme propre et localement d'intersection complète de schémas noethériens $X,Y$ admettant tous deux des Modules inversibles amples».
- **§4 opening** «Il nous faut enfin donner quelques indications…» clean; §4 content continues p10.
- **⚠ observation (not a flag — a heads-up):** the workpass from **L357 onward uses `\`\'\^` accent macros** (a different transcription lineage than the direct-UTF-8 earlier part); compiles fine, but it **systematically lowercases «Module(s)»** — watch/fix each occurrence in §3.3/§4+.
- Compile **0-err, 394pp**.
- **SWEEP CURSOR → Exposé 0 p10 = idx23** (§4 cont «…de Modules inversibles amples sur $X$ et $Y$» + §4.1 $K^\bullet$/$K^\bullet_{\mathrm{naif}}$ + §4.2 λ-structure + §4.3).

### #20 (2026-07-03) — Exposé 0 p10 (idx23) scribed (§4 + §4.1 + §4.2 + §4.3) — no-flag pass
- **§4.1:** ★ big multi-line **`\uline`** of the "bon invariant" claim («pour un schéma $X$ … le bon invariant … n'est pas $K^\bullet(X)$ … mais bien $K(\Parf(X))$ … que nous notons $K^\bullet_{\mathrm{naif}}(X)$»); parens «(ou plus généralement, un topos localement annelé)»; «Modules» cap; «naïf»→«naif» (book); **inlined the §4.1 $f:X\to Y$** (workpass displayed it); «Tor-dimension»→«tor-dimension»; parens «(le cas non noethérien…)»; `\underline F` ×2.
- **§4.2:** restored dropped **«(NB Si $L_\bullet$ et $L'$ … $L_\bullet\otimes^{\mathbf L}L'$)»** parenthetical (was plain «Si $L$ et $L'$…»); ★ **display target `\Gr^i`→`\Gr^\bullet`** (real error — the Chern-class map goes to $\Gr^\bullet(X)$).
- **§4.3:** **inlined $f:X\to Y$** (was displayed); parens «(où $d$ est la dimension relative virtuelle)».
- **Book typos → errata:** adopté→adoptée; tiré→tirée.
- Compile **0-err, 394pp**.
- **SWEEP CURSOR → Exposé 0 p11 = idx24** (§4.3 tail: display $T_f\in K^\bullet(X)$ + «Lorsque $f$ admet une factorisation (2.1)…»).

### #21 (2026-07-03) — Exposé 0 p11 (idx24) RESTRUCTURED (§4.3 cotangent complex + §4.4 start) — 2 dropped displays + renumber
- **★ Restored 2 dropped displays in §4.3:** the untagged **$d_{X'/X}:\underline J\subset\underline O_{X'}\to\Omega^1_{X'/Y}$** and the tagged **(4.2) $L^{X/Y}_\bullet\in\operatorname{Ob}D(X)$**. The workpass had neither → its «(4.2)» tag on the $T_f$ formula was really the book's **(4.3)**; renumbered.
- **★ (4.3) formula:** workpass «$T_f=\cl(L_{X/Y}^{\vee})$» → book **«$\check T_f=\cl^\bullet(L^{X/Y}_\bullet)$»** ($\check T_f$ dual, $\cl^\bullet$, cotangent complex $L^{X/Y}_\bullet$ — NOT $L^\vee$/dual). Confirmed by 11× crop.
- **(4.1):** `\underline N`; arrow **labelled «d»** (`\xrightarrow{d}`); `\otimes_{\underline O_{X'}}\underline O_X`. **Ω is plain here** (the book underlines Ω on p3 but NOT in (4.1)/the $d_{X'/X}$ display — reproduced per-page, 10× crop).
- **★ notation:** the cotangent complex is **$L^{X/Y}_\bullet$** (superscript X/Y, bullet subscript) throughout §4.3–4.4 — the workpass used «$L_{X/Y}$»; fixed every occurrence on the page.
- prose: «resp.» (was «respectivement» ×2 + commas); «;»→«:» (invariance sentence); §4.4 restored dropped parenthetical «(où il convient…polynômes)»; ``…''→«~…~» on this page.
- **⚠ lineage note (not a flag):** the L357+ block uses `` '' TeX quotes (different transcription lineage) — converting to «~…~» as I touch them; untouched `` '' on earlier §3.3/§4 lines to normalize in a later cleanup pass (stylistic).
- Compile **0-err, 394pp**.
- **SWEEP CURSOR → Exposé 0 p12 = idx25** (§4.4 cont: «…essentiellement non recollable. Voici une construction générale de $L^{X/Y}_\bullet$…» + the $C=A[T]\to B$ / simplicial construction).

### #50 (2026-07-04) — RRR Appendix p20 (idx53 = vol p40) scribed (§1: Chern-class axioms (2.3)–(2.7)) — DENSE, 8 fixes
- **★★ SYSTEMATIC NOTATION FIX (carry forward):** the book writes **individual Chern classes with a CAPITAL $C$** — $C^i(E)$, $C^0(E)$, $C(E)=\sum C^i(E)$ (13× crop of «$C^0(E)=1$» = cap-height C; «Chern $C^i$» crop) — the workpass had modernized them to lowercase $c^i$. Changed all p20 occurrences $c^i\to C^i$, $c^0\to C^0$. **Total class $\widetilde C$ ($=\Ctil$) and $C(E)$ already capital.** ⚠ workpass uses lowercase $c^i$ on ALL following Chern pages (L941 $c^1(L(D))$, L943, L945 $c^i(f^!E)$, …) — MUST fix $c^i\to C^i$ page-by-page as reached (do NOT global-replace — verify each page's scan; \ellc/other c-macros unaffected).
- **baseline dots (not \cdot):** (2.3) $f_*(x.f^*(y))=f_*(x).y$ (9× crop — baseline periods, workpass had `\cdot`); likewise «$C(E)=C(E').C(E'')$» dot (workpass juxtaposed).
- **displayed→inline ×2:** «des classes de Chern $C^i(E)\in A^i(X)$, ($i\geq1$),…» and «(si l'on pose $C(E)=\sum_{i\geq0}C^i(E)$, cette condition s'exprime $C(E)=C(E').C(E'')$)» — both run inline in the book (workpass had `\[…\]`).
- **dropped parens restored ×2:** «(si l'on pose … $C(E').C(E'')$)» and «(bien entendu, $\Ctil$ est … augmentations)» — the workpass had replaced the enclosing «(…)» with «. » / «; » (period/semicolon, capitalized «Si»/dropped). Restored parens + lowercase «si».
- **`;`→`.` swaps reverted ×2 (a recurrent Codex tic):** «suivantes~; on pose» (workpass «suivantes. On pose») and «$\lambda$-anneaux~; cette dernière» (workpass «anneaux. Cette»).
- **interpolated «par» removed:** «cette condition s'exprime $C(E)=…$» (workpass «s'exprime par»).
- **(2.7) fixes:** removed spurious comma between the two side-by-side formulas «$\Ctil(E)\Ctil(F)\qquad\Ctil(\Lambda^iE)…$»; **$\Ctil(\lambda^iE)\to\Ctil(\Lambda^iE)$** — exterior power $\wedge^i E$ on the LHS (real math error; RHS $\lambda^i\Ctil(E)$ correct).
- **dropped emphasis:** «\emph{classes de Chern}» (band 2), «\emph{$\lambda$-homomorphisme de $\lambda$-anneaux}» (band 4).
- **$\underline{K}(\xi(X))$** restored ×2 (bundle-class ring underlined, band 3 + (2.6)); **spurious comma** after «singulière**)**» removed; **«cf. chapitre»→«cf. Chap.»** (abbreviated, matching scan — contrast the (2.4) ref which keeps full «chapitre»).
- **verified:** (2.4) $\Ctil(E)=[\rang E,\sum_{i\geq0}C^i(E)]\in\Atil(X)$ ($\widetilde C$/$\widetilde A$ tildes, \rang spelled out); (2.5) $\Ctil(E)=\Ctil(E')+\Ctil(E'')$; footer «40», head «- 20 -». No book typos this page.
- Compile **0-err, 393pp**.
- **SWEEP CURSOR → RRR Appendix p21 = idx54** (§1 cont, already in workpass L940+: (2.8) $C^1(L(D))=\ellc(D)$, $C^i(L(D))=0$ ($i>1$) [FIX $c\to C$]; «$\ellc(Z)$ classe dans $A(X)$»; functoriality $C^i$; (2.9) $C^i(f^!(E))=f^*(C^i(E))$ [FIX $c\to C$]; (2.10) $f^!:\underline K(Y)\to\underline K(X)$ + the $f^!/f^*$ dualité footnote [Hartshorne, \emph{Residues and Duality}]; «on écrit ici $K(X)$ au lieu de $K(\xi(X))$»; a commutative diagram. ★ ON p21: apply $c^i\to C^i$ (verify on scan first); check $K(Y)/K(X)$ underline; the Hartshorne footnote text; the diagram (2.9-commutativity); $\ellc$ = cℓ class-map glyph.).

### #49 (2026-07-04) — RRR Appendix p19 (idx52 = vol p39) scribed (§1: **Théorème 2.1 (Chow moving lemma)** + (*)-footnote; pullback (2.1) $f^*$; pushforward (2.2) $f_*$)
- **Théorème 2.1 statement emphasis restored:** «\emph{Tout cycle sur $X$ est rationnellement équivalent à un cycle non singulier. Étant donnés des éléments de $A^i(X)$ et $A^j(X)$… soient $Y^{n-i}$ et $Z^{n-j}$, qui se coupent partout transversalement.}» — whole statement underlined in scan, workpass plain. («Étant» accent was already restored — kept.)
- **footnote (*) fixes:** ``moving lemma'' → «~moving lemma~» guillemets; French «~;» at «non excédentaire~; cf.». (Text «Par suite d'un malentendu… cf. Séminaire Chevalley 1958, Anneau de Chow et applications.» verified; here «cf.» **does** take a period — before a spelled-out reference.)
- **dropped parens + trailing ellipsis restored:** the explanatory «(Un cycle est dit non singulier … en position générale \dots)» is **parenthesized** in the book and trails off with «…» (workpass had dropped both parens and ended with a period).
- **dropped emphasis ×2:** «(\emph{image réciproque de classes de cycles})» (band 3); «un morphisme \emph{propre}» (band 3, defined term).
- **«cf» period fix:** «cf. [3]» → «cf [3]» — no period before the bracket citation (contrast the footnote's «cf. Séminaire»); consistent with p15 «cf § 2».
- **verified vs scan:** (2.1) $f^*:A(Y)\longrightarrow A(X)$ (star exponent, long arrow) — «Ainsi $A(X)$ devient un foncteur contravariant»; (2.2) $f_*:A(X^n)\longrightarrow A(Y^m)$ (star subscript) — «conservant la dimension des cycles, donc augmentant le degré de $m-n$»; «$X^n$/$Y^m$» dimension superscripts; «Soit $f$ un morphisme (i.e. une application régulière)…»; footer «39», head «- 19 -». No book typos this page.
- Compile **0-err, 393pp**.
- **SWEEP CURSOR → RRR Appendix p20 = idx53** (§1 cont, Chern classes — already partly in workpass L909+: «Ainsi, relativement aux morphismes propres… $A(X)$ est un foncteur covariant»; (2.3) $f_*(x\cdot f^*(y))=f_*(x)\cdot y$; classes de Chern $c^i(E)\in A^i(X)$ ($i\geq1$), $c^0(E)=1$; (2.4) $\Ctil(E)=[\rang E,\sum_{i\geq0}c^i(E)]\in\Atil(X)$; (2.5) $\Ctil(E)=\Ctil(E')+\Ctil(E'')$; $C(E)=\sum_i c^i(E)$, $C(E)=C(E')C(E'')$; (2.6) $\Ctil:K(\xi(X))\longrightarrow\Atil(X)$. ★ ON p20: verify (2.3)–(2.6) glyphs vs scan — the Chern total-class $\Ctil$ (is it $\widetilde C$ or $\mathcal C$? check), $\rang$ (rang/rk), $c^i$ vs $c_i$ (SUPERSCRIPT per A^i grading?), $K(\xi(X))$ underline? ($\underline K$ rep-ring vs plain — this is the K of vector-bundle classes, likely \underline K), $\Atil=\widetilde A$; watch «·» dots in (2.3) and the $[\rang E,\ldots]$ bracket-element; check inline-vs-display for $C(E)=\sum_i c^i(E)$ & $C(E)=C(E')C(E'')$; emphasis on any defined terms.).

### #48 (2026-07-04) — RRR Appendix p18 (idx51 = vol p38) scribed (end Démonstration Prop 1.5; **CHAPITRE II** / **§1 La théorie de Chow** begins)
- **dropped emphasis restored ×2:** «le gradué associé à $A$ est ici \emph{intègre}» (band 1); «on suppose fixé un \emph{corps de base} $k$» (band 3) — both underlined single terms, workpass plain.
- **period-order fixed:** «($A^i(X)$ étant formé des classes de cycles de dimension $n-i$**)**.» — the book puts the period **outside** the closing paren (16× crop + OCR: «n - i). Le fait»); the workpass had «$n-i$.)» (period inside). Moved out.
- **verified vs scan:** Démonstration tail «$x\lambda_{-1}(N)$ est d'augmentation nulle), tandis que $\lambda_{-1}(N)$ est de filtration $q$ (formule (1.22)), … $\gamma^n(N,x)$ est de filtration $j$, … (1.18) le gradué associé à $A$ … Utilisant les formules précédentes, on obtient immédiatement la forme indiquée pour $(\gamma^{q+j}(N,x))^{(j)}$.», cqfd right-set; «CHAPITRE II» + centered title «Classes de faisceaux algébriques cohérents / et classes de Chern» (title underlined in scan → rendered as structural heading, kept); «\S 1. La théorie de Chow» subsection (title underlined → heading); already-`\emph` defined terms confirmed against underlines: «\emph{quasi-projectif}» (band 4), «\emph{anneau de Chow}» (band 4); «$A(X)$», «$A^i(X)$» degree-grading, «équivalence rationnelle près»; footer «38», head «- 18 -». No book typos this page.
- Compile **0-err, 393pp**.
- **SWEEP CURSOR → RRR Appendix p19 = idx52** (§1 cont: «Le fait que $A(X)$ soit bien un anneau gradué résulte du théorème suivant de Chow :» → the **Théorème de Chow** statement + what follows [workpass L895+]. ★ ON p19: verify the Chow theorem statement (emphasis/underline extent, any displayed formula that's actually inline, cross-refs), cycle-class notation, and grading $A^i(X)$/product; watch for the recurrent displayed-should-be-inline and dropped-emphasis patterns.).

### #47 (2026-07-04) — RRR Appendix p17 (idx50 = vol p37) scribed (end §4: (1.37); **Proposition 1.5** + (1.38)/(1.39) + Démonstration (1.40))
- **dropped emphasis restored:** «injective» underlined (band 1) → «est \emph{injective}~;» (+ French `~;`).
- **dropped comma restored:** «on pose $\gamma^n(N,x)=\gamma^n(x_N)$**,** où $x_N$…» (workpass had no comma before «où»).
- **Prop 1.5: displayed→inline + statement emphasis.** The book runs $N=[q,1+N^1+\cdots+N^q]$ and $x=[\nu,1+\sum_{i\geq1}x^i]$ **inline** (workpass had each as its own `\[…\]` display) — inlined both. The whole statement is **underlined** → wrapped in `\emph{…}` per the established appendix Prop convention (cf. Prop 1.2 L737, Prop 1.3 L786: `\textbf{Proposition X.} \emph{statement…}`), split into two `\emph` runs around the (1.38)/(1.39) displays.
- **verified vs scan (glyphs already correct):** (1.37) $\gamma^n(N,x)=\sum_{i=0}^{n-1}\binom{n-1}{i}\lambda^i(N,x)$ display; (1.38) $(\gamma^{q+j}(N,x))^{(j)}=(-1)^{j-1}(j-1)!\,G_{q,j}(\nu,x^1,\ldots,x^j;N^1,\ldots,N^j)$ — factorial, `;` separator between x-block/N-block, `(j)` degree-component superscript; (1.39) $G_{q,j}(\nu,x^1,\ldots,N^j)N^q=(-1)^q(x*\lambda_{-1}(N))^{(q+j)}$ — the **`*` special-λ-ring product** (distinct from the p16 baseline dot & from plain juxtaposition; kept); (1.40) $\gamma^n(N,x)\lambda_{-1}(N)=\gamma^n(x\lambda_{-1}(N))$ juxtaposition; Démonstration «$A$ = anneau des polynômes… indéterminées $x^i$ et $N^j$ (avec $1\leq j\leq q$)»; «filtration $\geq q+j$» (word, not \Fil operator); «(1.22 bis)», «(1.18)», «$\widetilde A$» tilde; footer «37», head «- 17 -». (Book prints 2-dot «..» ellipses in the $G_{q,j}$ arg-lists — kept normalized to `\ldots`.) No book typos this page.
- Compile **0-err, 393pp**.
- **SWEEP CURSOR → RRR Appendix p18 = idx51** (finish Démonstration Prop 1.5: «…$x\lambda_{-1}(N)$ est d'augmentation nulle), tandis que $\lambda_{-1}(N)$ est de filtration $q$ (formule (1.22)), il en résulte que $\gamma^n(N,x)$ est de filtration $j$… le gradué associé à $A$ est ici intègre… cqfd.» [workpass L880-881] — then **CHAPITRE II** «Classes de faisceaux algébriques cohérents et classes de Chern», **§1 La théorie de Chow** [L883-895]: «Dans tout ce chapitre… corps de base $k$… algébriquement clos…»; def «espace algébrique \emph{quasi-projectif}»; «anneau de Chow $A(X)$», «$A^i(X)$… dimension $n-i$», «théorème suivant de Chow». ★ ON p18: the Démonstration tail is on L880 (one line, already scribed) — verify its p18-visible glyphs vs scan; check CHAPITRE II title/§1 formatting & the two `\emph` (quasi-projectif, anneau de Chow) against underlines; watch $A(X)$/$A^i(X)$ grading, the Chow-theorem lead-in.).

### #46 (2026-07-04) — RRR Appendix p16 (idx49 = vol p36) scribed (§4: special-λ-ring $K_N$ construction, (1.34)–(1.36))
- **false alarm cleared:** (1.35) «$\lambda_t(n,x)=(1+t)^n\sum_{p\geq0}\lambda^p(N,x)t^p$» — the **lowercase $n$** in $(n,x)$ and the exponent $(1+t)^n$ is CORRECT (an element of $K_N$ is the pair $(n,x)$, $n$=unit/integer coefficient; distinct from the module $N$ in $\lambda^p(N,x)$). Workpass already right, no change.
- **displayed→inline:** the three λ-ring identities were **centred as a display** (workpass), but the book runs them **inline** in «Il s'agit donc de vérifier les formules $\ldots$ pour $X,Y\in K_N$.» — inlined.
- **★ meaningful dot restored:** 2nd identity is «$\lambda_t(XY)=\lambda_t(X).\lambda_t(Y)$» with an explicit **baseline dot** (11× crop) — the special-λ-ring product — whereas the 1st «$\lambda_t(X+Y)=\lambda_t(X)\lambda_t(Y)$» is juxtaposition (ordinary power-series product). Workpass had juxtaposition in both; restored the dot in the 2nd.
- **arrow glyph:** «l'homomorphisme $x\longrightarrow x\mu$» is a **plain long arrow** (16× crop, no mapsto bar) — workpass had `\mapsto`; fixed to `\longrightarrow`. (Contrast: «opérations $x\mapsto\lambda^p(N,x)$» earlier on the page IS a genuine mapsto — kept.)
- **spurious comma removed:** «En tant qu'anneau commutatif $K_N$» — 18× crop shows **no comma** after «commutatif» (workpass had added one).
- **product form:** L839 tail «en les $\lambda^iN$ et les $\lambda^jx$» (workpass had subscript $\lambda_N^i,\lambda_x^j$).
- **dropped emphasis restored:** «(1.32) \emph{dans} $K$» («dans» underlined, band 1); the whole clause «\emph{muni de ces opérations, $K_N$ est un $\lambda$-anneau spécial}» underlined (band 3, extent = «muni de ces opérations» + «est un λ-anneau spécial», $K_N$ math un-underlined).
- **verified vs scan:** (1.34) «$x_Ny=xy\mu\qquad(\mu=\lambda_{-1}(N))$»; (1.36) «$K_N\longrightarrow K$» display; «un nouvel λ-anneau» (kept «nouvel»); «λ^0(N,x)=(1,0)»; «engendré par $X,Y$ et $N$ soumis aux relations $\lambda^iN=0$ pour $i>q$»; «applications $\lambda^i$»; the 2nd «λ-anneau spécial libre» is NOT underlined (kept plain); footer «36», head «- 16 -». No book typos this page.
- Compile **0-err, 393pp**.
- **SWEEP CURSOR → RRR Appendix p17 = idx50** (§4 cont: «Dans le cas actuel, sa restriction à $K$ est injective ; comme $K$ est un λ-anneau spécial… ceci achève de démontrer notre assertion.»; then (1.37) $\gamma^n(N,x)=\sum_{i=0}^{n-1}\binom{n-1}{i}\lambda^i(N,x)$ [workpass L860-862] + «$\gamma^n(N,x)=\gamma^n(x_N)$» + **Proposition 1.5** [L865, $A$ graded ring, $N=[q,1+N^1+\cdots+N^q]\in\widetilde A$]. ★ ON p17: verify (1.37) binomial/limits, the $x_N$ subscript, French «~;» at «injective ;», and whether (1.37) is inline-vs-display in the book; check Prop 1.5 statement emphasis.).

### #45 (2026-07-04) — RRR Appendix p15 (idx48 = vol p35) scribed (end of Démonstration Théorème 1.4 + Remarques a)/b) + (*) footnote)
- **p14 carryover resolved:** ℓ glyph **re-confirmed cursive $\ell$** on p15's own scan (bands 1–2, «$\ell^p(N)$» clear); `\underline{K}(G)` restored at all 5 representation-ring occurrences on this page (workpass had plain `K(G)`): L831 (×1, «l'intersection de $K(G)$») and L833 (×4: «satisfait dans $K(G)$», «$\lambda^p(N,F)\in K(G)$», «$K(G)$ est spécial», «$K(G)$ est intègre»); French `~;` at L831 («$\lambda^p(N,1)$~;»). Field of fractions / general λ-ring $K$ stays plain (band 1 «sous-anneau de $K$», band 4 «$K$ un $\lambda$-anneau»).
- **product form `λ^iN` restored:** the workpass wrote the λ-operations with a **subscript-N** ($\lambda_N^i,\lambda_N^q,\lambda_x^j$); the book prints the **juxtaposition** $\lambda^iN$ (superscript $i$ on $\lambda$, full-size $N$/x at baseline) — OCR + bands confirm. Fixed L827 ($\lambda_N^i\!\to\!\lambda^iN$, $\lambda_N^q\!\to\!\lambda^qN$), L831 (×2), Remarque a) L835 ($\lambda_N^i\!\to\!\lambda^iN$, $\lambda_x^j\!\to\!\lambda^jx$).
- **dropped emphasis restored:** «spécial» is **underlined** in the scan as the defined technical term (special λ-ring) — restored `\emph{spécial}` at L833 («$\underline{K}(G)$ est spécial») and L839 («un $\lambda$-anneau spécial quelconque»); workpass had both plain.
- **interpolated period removed:** «(cf. \S 2)» → «(cf \S 2)» — 20× crop shows the book prints «cf» **without** a period (workpass had added one). *(no errata: edition now matches book, no book-vs-edition diff.)*
- **verified vs scan:** display «$\ell^p(N)\lambda_{-1}(N)=\lambda^p(\lambda_{-1}(N))$»; «Comme on est dans un grand corps $K$…»; «$\lambda^p(F\lambda_{-1}(N))$» ×2 (F·λ_{-1}(N) product inline); «cqfd.» (lowercase, right-set); Remarques a) «$q'$ de $F$ est $\geq p$», b) footnote «$\ldots$clos\footnote{Cela se prouve en effet par la même méthode.}» marker before period; «$\mathfrak S_p$-module» Fraktur KEPT; «Riemann--Roch» en-dash; «caractéristique $0$» ×3; footer «35», head «- 15 -». No book typos this page.
- Compile **0-err, 393pp**.
- **SWEEP CURSOR → RRR Appendix p16 = idx49** (§4 cont, the special-λ-ring $K_N$ construction: «Soit maintenant K un λ-anneau spécial… soit N un élé[ment] de K tel que $\lambda^iN=0$ pour $i$ assez grand… considérer les éléments $\lambda^p(N,x)$…»; (1.34) $x_Ny=xy\mu$ ($\mu=\lambda_{-1}(N)$); (1.35) $\lambda_t(n,x)=(1+t)^n\sum_{p\geq0}\lambda^p(N,x)t^p$; «$K_N$ est un λ-anneau spécial». ★ ON p16: the L839 tail has $\lambda_N^i,\lambda_x^j$ **again** (workpass) → convert to $\lambda^iN,\lambda^jx$ per scan; «spécial» at L847 «$K_N$ est un $\lambda$-anneau spécial» — check for underline; verify (1.34)/(1.35) glyphs incl. the $x_Ny$ subscript-N product and $\lambda_t$; check «$n$» vs «$N$» in (1.35) $\lambda_t(n,x)$ vs the element $N$.).

### #44 (2026-07-04) — RRR Appendix p14 (idx47 = vol p34) scribed (§4: (1.33), N.B., Démonstration of Théorème 1.4)
- **dropped clause + wrongly displayed formula restored (inline):** the workpass had «…puis sur \[\Lambda(N^{(p)})\otimes\bigotimes^p F\]» — **dropping** «$\bigotimes^p F$ et sur» AND centring a formula the book runs inline. Restored: «puis sur $\bigotimes^p F$ et sur $\Lambda(N^{(p)})\otimes\bigotimes^p F$.» inline.
- **emphasis restored:** the whole «On fait opérer le groupe symétrique 𝔖_p … On a alors» block is **underlined** in the scan (real underlines — absent under the handwritten math, and the N.B. right below is plain, so not a contrast artifact) → wrapped in `\emph{…}` (continues the emphasized definition block begun p13 with «Soient N et F…»).
- **`=:` sign:** «$\Gl(N)\times\Gl(F)\eqqcolon G$» — 34× crop shows the **defines-RHS** «=:» (two equals-bars + colon), not plain `=` (embedded OCR dropped the colon). `\eqqcolon` (mathtools present).
- **guillemets:** ``partie alternée'' → «~partie alternée~».
- **$\underline{E}_G$** (×3: (1.33), N.B., ℓ^p formula) — operator printed underlined (16× crop), workpass had plain `E_G`. **$\underline{K}(G)$** representation ring restored on this page (workpass plain `K(G)`); field of fractions `K` (no $(G)$) stays plain.
- **N.B. math fixes:** substituted classes are the **exterior powers** $\Lambda^i(N),\Lambda^i(F)$ (workpass wrongly had $\lambda^i(N),\lambda^i(F)$); variables $\lambda^iN,\lambda^iF$ product-form (workpass had spurious subscripts $\lambda^i_N,\lambda^i_F$). French `~;` ×2 («de $M$~;»).
- **operator glyph:** cursive **$\ell^p$** (crystal-clear 12× crop), workpass had `\mathscr L^p` → `\ell^p` (fixed L829 on p14 **and** the two occurrences at L833/L835 spilling onto p15, to keep the operator glyph uniform across Théorème 1.4's proof; will re-confirm on p15 scan).
- **book typo (errata [corrected]):** ℓ^p(N) formula printed with **unbalanced parens** «$\underline{E}_G((\wedge(N^{(p)})^{\mathrm{alt}})$» (3 opens/2 closes); edition supplies the missing `)` → $\underline{E}_G((\wedge(N^{(p)}))^{\mathrm{alt}})$.
- **verified vs scan:** (1.33) $\lambda^p(N,F)=\underline{E}_G((\Lambda(N^{(p)})\otimes\bigotimes^p F)^{\mathrm{alt}})$; Démonstration via (1.32)/2nd formula (1.11), $x=1$, $\Z[\lambda^1N,\ldots,\lambda^qN]$ (upper limit q), $\lambda^p(\lambda_{-1}(N))/\lambda_{-1}(N)$ **slash** division, plain field $K$, «A priori» (Latin, unaccented — kept), «$1\leq i\leq q$», «$G=\Gl(N)$» plain `=`, cross-ref «(\S 2, théorème 1.3)»; footer «34», head «- 14 -». `\textbf` kept for the «Démonstration :» label.
- Compile **0-err, 393pp**.
- **SWEEP CURSOR → RRR Appendix p15 = idx48** (end of Démonstration Théorème 1.4: «$\ell^p(N)\lambda_{-1}(N)=\lambda^p(\lambda_{-1}(N))$» display, «Comme on est dans un grand corps $K$…», then **Remarques a) / b)** with footnote. ★ ON p15: re-confirm the $\ell$ glyph; **restore $\underline{K}(G)$** at L835 (×1) and L837 (×4, representation ring — «satisfait dans $K(G)$», «$\lambda^p(N,F)\in K(G)$», «$K(G)$ est spécial», «$K(G)$ est intègre») and French `~;` at L835 «$\ldots)$ ; les deux membres» — left for the p15 pass; keep «grand corps $K$» plain.).

### #43 (2026-07-04) — RRR Appendix p13 (idx46 = vol p33) scribed ((1.30 bis); §4 «Les opérations $\lambda^p(N,x)$»: (1.31)/(1.32), Théorème 1.4)
- **statement/emphasis restored** (`\emph`, book underlines statements): «\emph{ce qui équivaut à~:}»; the whole **Théorème 1.4 statement** «\emph{Soit $J_q$ l'idéal fermé de $A$ … isobare de poids $p$ par rapport aux variables $\lambda^i x$.}»; the emphasized setup «\emph{Soient $N$ et $F$ … le noyau de l'application} … \emph{de $N^p$ dans $N$.}»; «\emph{polynômes}».
- **inline display restored + arrow:** «…de l'application $(a_1,\ldots,a_p)\longrightarrow a_1+\cdots+a_p$ de $N^p$ dans $N$» — the workpass had centred it AND used $\longmapsto$; the book uses a **plain arrow** (crop-confirmed).
- **guillemets** ×3: «~continues~», «~$\lambda$-anneau libre engendré par $N$ et $x$~»; **French `;`/`:`** ×5 («inversible~;», «posant~:», «avec $i>q$~;», «caractéristique $0$~;», «$x$~»~;»).
- **verified vs scan:** (1.30 bis) $\ch(\lambda_{-1}(\check N))=N^q\mathcal C(N)^{-1}$; §4 setup ($A$ = formal series in $\lambda^iN,\lambda^ix$, special λ-ring); (1.31) $\lambda_{-1}(N)=\sum_{i\geq0}(-1)^i\lambda^iN$; (1.32) $\lambda^p(N,x)\lambda_{-1}(N)=\lambda^p(x\lambda_{-1}(N))$; Todd now $\mathcal C$; footer «33», head «- 13 -». No book typos this page.
- Compile **0-err, 393pp**.
- **SWEEP CURSOR → RRR Appendix p14 = idx47** (§4 cont: «On fait opérer le groupe symétrique $\mathfrak S_p$ sur $N^p$…»; (1.33) $\lambda^p(N,F)=E_G((\Lambda(N^{(p)})\otimes\bigotimes^p F)^{\mathrm{alt}})$; N.B. on $E_G$ / Euler–Poincaré in $\underline K(G)$; Démonstration — note $\mathfrak S_p$ symmetric-group Fraktur (KEEP, distinct from Todd $\mathcal C$); $\underline K(G)$ underline in the N.B.).

### #42 (2026-07-03/04) — RRR Appendix p12 (idx45 = vol p32) scribed (§3: Chern hom ch (1.27)–(1.29); Todd $\mathcal C$; Prop 1.3 (1.30))
- **★ Todd operator font: `\mathfrak C`→`\mathcal C` (all 10 in the file):** the book's Todd C is a **flowing script/calligraphic** glyph (1100 dpi crop of «$\mathcal C_f=\mathcal C$ ($\mathcal C$ est l'initiale de Todd)»), not the angular Fraktur $\mathfrak C$. `[faithful]` (errata).
- **(1.28) extra parens removed:** «$\eta(x^i)=1/(-1)^{i-1}(i-1)!\,x^i$» — the workpass had «$1/((-1)^{i-1}(i-1)!)$» (added parens the book doesn't print).
- **2 inline displays restored:** the Hirzebruch «$1+\Ahp\longrightarrow 1+(\Ahat\otimes\Q)^+$, noté $\mathcal C_f$» and Prop 1.3's «de la forme $[q,1+N^1+\cdots+N^q]$» (both centred by the workpass).
- **dropped emphasis restored** (`\emph`): the result «on a un \emph{isomorphisme} $\ch$ \emph{de l'anneau} $\widetilde A\otimes\Q$ \emph{sur l'anneau} $\Ahat\otimes\Q$»; the **Prop 1.3 statement** «\emph{Soit $N\in\widetilde A$ de la forme … Si l'on pose~:}» / «\emph{on aura~:}».
- **guillemets** «~inverser~»; **French `;`/`:`** («de $\ch$~:», «$\mathcal C_f$~;», «suivant~:»).
- **verified vs scan (crop):** (1.27) $\ch([1,1+x^1])=\exp x^1=\sum_{n\geq0}(x^1)^n/n!$; (1.29) $\ch([n,1+\sum x^i])=n+\eta(\log(1+\sum x^i))$; (1.30) $\ch(\lambda_{-1}(N))=(-1)^qN^q\mathcal C(\check N)^{-1}$; the λ_{-1}(N) sum's upper limit is **$n$** (crop-confirmed, NOT $q$); footer «32», head «- 12 -». No book typos.
- Compile **0-err, 393pp**.
- **SWEEP CURSOR → RRR Appendix p13 = idx46** (§3 tail: Prop 1.3 proof / consequences of (1.30); then likely §4 «Les opérations $\lambda^p(N,x)$» — the TOC lists §4 at appendix p13).

### #41 (2026-07-03) — RRR Appendix p11 (idx44 = vol p31) scribed (§3 cont: γ-operations (1.23)–(1.25 bis)/(1.22 bis); «L'homomorphisme de Chern» (1.26))
- **★ INTERPOLATION removed:** the workpass had «soit $K$ un λ-anneau quelconque et **$n$** par ailleurs arbitraire» — the book has **no «$n$»** («…quelconque et par ailleurs arbitraire», 1000 dpi crop). Removed the added «$n$».
- **inline display restored:** «…et que $\gamma_t(x+y)=\gamma_t(x)\gamma_t(y)$, et par suite…» (the workpass had centred it).
- **result-sentence emphasis restored** (`\emph`, book underlines it): «\emph{la composante} $x^n$ \emph{s'obtient, au facteur} $(-1)^{n-1}(n-1)!$ \emph{près, en réduisant modulo} $\widetilde A^{n+1}$ \emph{l'élément} $\gamma^n(x-\varepsilon(x))$ \emph{de} $\widetilde A^n$».
- **general λ-ring `$K$` kept PLAIN** (crop-confirmed — no underline; the `\underline K` is specific to the representation ring).
- **French `;`/`:`** ×6 («suivantes~:», «arbitraire~;», «$x$~;», «ensuite~:», «formule~:», «Chern~:», «augmentés~:»).
- **verified vs scan:** (1.23) $\gamma^n(x)=(-1)^n\sum_{i=0}^n(-1)^i\lambda^i(x+n)=\lambda^n(x+n-1)$; (1.24) $\gamma_t(x)=\sum\gamma^n(x)t^n$; (1.25) $\gamma_t(x)=\lambda_{t/(1-t)}(x)$; (1.25 bis) $\lambda_s(x)=\gamma_{s/(1+s)}(x)$; (1.22 bis) $\gamma^n(x-\varepsilon(x))=[0,1+(-1)^{n-1}(n-1)!x^n+\cdots]$; (1.26) $\ch:\widetilde A\to\Ahat\otimes\Q$; footer «31», head «- 11 -». No book typos this page.
- Compile **0-err, 393pp**.
- **SWEEP CURSOR → RRR Appendix p12 = idx45** (§3 cont: the Chern homomorphism (1.26) definition — «homomorphisme additif, transformer 1 en 1, composantes…»; likely (1.27)+ ch formulas; watch for the ch macro / $\Ahat\otimes\Q$ target).

### #40 (2026-07-03) — RRR Appendix p10 (idx43 = vol p30) scribed (§3 cont: (1.19)–(1.22), λ-ops on $\widetilde A$, Prop 1.2) — statement emphasis
- **★ (1.20) — spurious comma + subscripted argument reverted:** book «$\lambda^i[0,x]=[0,\lambda^i x]\ \ (\lambda^i x)^{(n)}=Q_{i,n}(\dots)$» — the workpass had inserted a comma between the two side-by-side equations AND subscripted «$(\lambda^i_x)$» (the λ-op acts on $x$ inline). Both reverted.
- **principal-automorphism arrow:** «$x=\sum_{i\geq0}x^i\longrightarrow\check x=\dots$» — book uses a **plain arrow** (crop-confirmed), not $\mapsto$.
- **inline formula restored** in Prop 1.2: «…de la forme $[n,1+x^1+\cdots+x^n]$ (on a donc…» (the workpass had centred the $[n,\dots]$).
- **statement/emphasis restored** (`\emph`): «\emph{homomorphisme d'anneaux}», «\emph{universels}», «\emph{spécial}», and the whole **Prop 1.2 statement** «\emph{Pour $x\in\widetilde A$ de la forme … et enfin}» (book underlines prop statements).
- **French `;`/`:`** («entiers~:», «en $A$~;»).
- **verified vs scan:** (1.19) $\eta'(x^i)=(-1)^{i-1}(i-1)!\,x^i$; (1.21) $\lambda^i[1,1+x^1]=0$ pour $i>1$; «$Q_{i,n}$ = Chern des puissances extérieures»; (1.22) $\sum_{i=0}^n(-1)^i\lambda^i(x)=[0,1-(n-1)!x^n+\cdots]$; footer «30», head «- 10 -». No book typos this page.
- Compile **0-err, 393pp**.
- **SWEEP CURSOR → RRR Appendix p11 = idx44** (§3 cont: «La formule (1.22) admet les généralisations suivantes: soit $K$ un λ-anneau… pour $x\in K$, on pose…» — the general λ-operations/Chern-character setup; expect more \underline{K}? here $K$ is a general λ-ring, not the representation ring — check whether the book underlines it).

### #39 (2026-07-03) — RRR Appendix p9 (idx42 = vol p29) scribed (§3 cont: (1.17)/(1.17 bis)/(1.18)/(1.19) — $x*y$ Chern-of-tensor-product, filtration on $\widetilde A$)
- **★ inline formula restored AND de-restructured:** the workpass had «…décomposant ``formellement'' \[x=\prod(1+\alpha_i),\ y=\prod(1+\beta_i)\]…» — but the book runs it inline AND phrases it «$x$ **en un produit** $\prod_{i=1}^n(1+\alpha_i)$ et $y$ **en un produit** $\prod_{i=1}^n(1+\beta_i)$» (not «$x=\prod$»). Restored the prose + inlined.
- **★ `\frac` → inline slash in (1.17 bis):** book writes «$(1+x^1+y^1)/(1+x^1)(1+y^1)$» (linear slash); the workpass had stacked it as `\frac`. Reverted to the slash. *(Note: (1.18) genuinely IS a stacked fraction in the book — kept `\frac` there; the book is inconsistent, each reproduced as printed.)*
- **guillemets** ×3: «~addition~», «~linéaires~», «~formellement~»; **dropped emphasis** «\emph{filtration}».
- **French `;`/`:`** ×4 («suit~:», «déduit~:», «$1\leq i<n$~;», «multiplicatif~;»).
- **verified vs scan:** (1.17) $[1,1+x^1][1,1+y^1]=[1,1+x^1+y^1]$, «$Q_i$ = classes de Chern d'un produit tensoriel»; (1.18) $(1+\sum_{i\geq m}x^i)*(1+\sum_{j\geq n}y^j)=1-\frac{(m+n-1)!}{(m-1)!(n-1)!}x^my^n+\cdots$; «$G(\widetilde A)$ s'identifie à $A$ additivement»; (1.19) $\eta'$; footer «29», head «- 9 -». No book typos this page.
- Compile **0-err, 393pp**.
- **SWEEP CURSOR → RRR Appendix p10 = idx43** (§3 cont: (1.19) $\eta'(x^i)=(-1)^{i-1}(i-1)!\,x^i$ homomorphism; the λ-operations (1.20) $\lambda^i[0,x]=[0,\lambda^ix]$, $Q_{i,n}$; further λ-structure on $\widetilde A$ / graded-ring λ-ring).

### #38 (2026-07-03) — RRR Appendix p8 (idx41 = vol p28) scribed (Remarques b)/c) + §3 Le λ-anneau défini par un anneau gradué: $\widetilde A$, (1.14)–(1.16))
- **underlined-K** ×2 in Remark b): «$\underline K(G)$ … spécial en car. 0», «$\underline K_r(G)$ en toutes car.».
- **2 inline displays restored** (book runs inline): «…avec $n\in\Z$ et $x=1+\sum_{i\geq1}x^i\in1+\Ahp$ ($x^i\in A^i$).» and «…s'écrive $[mn,x^ny^m(x*y)]$, où $x*y$…» (both were centred; dropped stray trailing commas).
- **augmentation arrow:** «$\varepsilon:[n,x]\longrightarrow n$» — the book uses a **plain arrow** (crop-confirmed), not $\mapsto$ (the workpass had $\mapsto$).
- **French `;`/`:`** («unité~;», «ainsi~:», «$y^i$~:»).
- **BOOK TYPO → errata `[corrected]`:** «compatible avec sa **strucutre** additive» → «structure».
- **verified vs scan:** §3 setup ($A$ gradué, $A^0=\Z$, $\Ahat=\prod A^i$, $\Ahp$), (1.14) $\widetilde A=\Z\times(1+\Ahp)$, (1.15) $[n,x]+[n',x']=[n+n',xx']$, $[0,1]$ nul, (1.16) $(x*y)^i=Q_i(x^1,\dots,x^i;y^1,\dots,y^i)$ ($i\geq1$); footer «28», head «- 8 -».
- Compile **0-err, 393pp**.
- **SWEEP CURSOR → RRR Appendix p9 = idx42** (§3 cont: «$Q_i$ isobare de poids $i$… classes de Chern d'un produit tensoriel»; (1.17) $[1,1+x^1][1,1+y^1]=[1,1+x^1+y^1]$; (1.17 bis) deduced from (1.17); then the $\lambda$-operations on $\widetilde A$).

### #37 (2026-07-03) — RRR Appendix p7 (idx40 = vol p27) scribed (ex.3 Corollaire + Remarques a) — underlined-K + statement emphasis
- **underlined-K restored** ×7: $\underline K_r(G)$ (Corollaire, «diviseurs de 0», «s'explicite ainsi», «s'identifie»), $\underline K(G)$/$\underline K_r(G)$/$\underline K(\xi(X))$ in Remarque a).
- **★ display separator comma→semicolon reverted:** «$\Z[\rho_1,\dots,\rho_{r'};\sigma_1,\dots,\sigma_{r''}\mathbf{,}\sigma_1^{-1},\dots]$» → book's «$\dots\sigma_{r''}\mathbf{;}\sigma_1^{-1}\dots$» (three groups all `;`-separated).
- **★ index reverted to the book:** the running-text base is «$(\sigma_i)_{1\leq i\leq r''}$» ($i$), not $\sigma_j$ (the workpass had unified it with the Corollaire's «les $\sigma_j$»); reproduced both as printed (errata `[faithful]`).
- **statement emphasis restored** (`\emph`, book underlines whole statements): Corollaire «\emph{L'anneau $\underline K_r(G)$ s'identifie…}» + «\emph{du corps des fonctions rationnelles… dans $\Q$}»; also «\emph{fondamentales}», «\emph{rang d'un fibré vectoriel}».
- **footnote marker/period order:** «…dans $\Q$\footnote{…}.» (book: «Q (\*).» — marker before the period; the workpass had «Q.\footnote»).
- **French `;`/`:`** ×6.
- **BOOK TYPO → errata `[corrected]`:** «le groupe **dévisé** $G'$» → «dérivé».
- **verified vs scan:** $G=\prod_i\Gl(n_i,k)$, «$\lambda^j(\rho_i)$ ($1\leq j\leq n_i$)», «inverses des $\lambda^{n_i}(\rho_i)$»; Remarque a) augmentation; footer «27», head «- 7 -».
- Compile **0-err, 393pp**.
- **SWEEP CURSOR → RRR Appendix p8 = idx41** (Remarques b) «$k$ non alg. clos… $K(G)$ spécial en car. 0»; c) «car. non nulle… Chevalley»; then **§3 Le λ-anneau défini par un anneau gradué**: $A$ gradué, $\hat A=\prod A^i$, $\hat A^+$, (1.14) $\widetilde A=\Z\times(1+\hat A^+)$, $[n,x]$, (1.15)…).

### #36 (2026-07-03) — RRR Appendix p6 (idx39 = vol p26) scribed (ex.3: $K(G)/K(T)$/Weyl determination, Théorème 1.1) — heavy underlined-K page
- **★ underlined-K restored throughout** (~12 occurrences): $\underline K(G)$, $\underline K_r(G)$, $\underline K(T)$, $\underline K_r(T)$ in the «3)» heading, «$\underline K(G)=\underline K_r(G)$», the inlined «$\underline K(T)=\underline K_r(T)=\Z(\That)$», (1.13) «$\underline K_r(G)\to\underline K_r(T)^W=\underline K(T)^W$», «$\underline K(T)^W$ … dans $\underline K(T)$», «base canonique de $\underline K_r(G)$».
- **inline display restored:** «on a $\underline K(T)=\underline K_r(T)=\Z(\That)$, algèbre du groupe $\That$…» (workpass had centered it).
- **★ punctuation swap reverted:** «…certains cas importants**.** On suppose» → book «importants**~:** On suppose».
- **$(k^*)^s$ → book's $k^{*s}$** (compact $s$-torus notation, reproduced as printed; errata `[faithful]`).
- **dropped emphasis restored** (`\emph`): the «3)» heading «Détermination de $\underline K(G)$ et de $\underline K_r(G)$ dans certains cas importants», «affine connexe», «réductif», and the Théorème 1.1 statement «\emph{L'homomorphisme} (1.13) \emph{est un isomorphisme.}».
- **guillemets:** «~globalement \emph{réductif}~», «~type~»; **spurious comma removed** in footnote «1956/58**~**Groupes» (book has no comma); French `;`/`:` ×5.
- **BOOK TYPO → errata `[corrected]`:** «Groupes de Lie **albébriques**» → «algébriques».
- **verified vs scan:** Théorème 1.1, tore maximal $T$, Weyl $W$, «$\That\simeq\Z^r$», footnote «Cf. Séminaire Chevalley 1956/58…»; footer «26», head «- 6 -».
- Compile **0-err, 393pp** (−1: inlining the $K(T)$ display reclaimed a page; benign, content intact).
- **SWEEP CURSOR → RRR Appendix p7 = idx40** (ex.3 tail: Corollaire «$\underline K_r(G)$ s'identifie au sous-anneau $\Z[\rho_1,\dots,\rho_{r'};\sigma_1,\dots,\sigma_{r''},\sigma_1^{-1},\dots]$» + its footnote; «$K_r(G)$ n'a pas de diviseurs de 0…», $G=\prod_i\Gl(n_i,k)$; Remarques a)/b) — expect more underlined-K).

### #35 (2026-07-03) — RRR Appendix p5 (idx38 = vol p25) scribed (§2 «Variantes» + ex.2 fibrés vectoriels $\underline K(\xi(X))$)
- **2 more formulas the workpass DISPLAYED, inlined** to match the book: «…de la forme $(E\oplus E')-(E)-(E')$, sur lequel…» and «…par les éléments $(E)-(E')-(E'')$ où $E$ est…» (dropped a stray trailing comma on the first).
- **underlined-K restored** ×2: «noté $\underline{K}(\xi(X))$», «le $\lambda$-anneau $\underline{K}(\xi(X))$ est spécial» (the fibré-vectoriel K-group — book underlines K).
- **`etc.`→`etc\dots` (ellipsis)** ×2: the book writes «etc\dots» (both in the main «…continues, etc\dots\footnote» and inside footnote 1 «…algèbre de Lie, etc\dots Nous»); the workpass had «etc.».
- **French spacing:** «précédent~:», «sur $k$~;», «Schmidt)~;», «$E''$~;», «Riemann--Roch~!», «cf.\ note».
- **verified vs scan:** ex.2 fibré-vectoriel construction, «Krull--Remak--Schmidt», «$\xi(X)$ catégorie additive des fibrés vectoriels»; footnote 1 «autres exemples de λ-anneaux… Riemann--Roch~!»; footnote «(\*) Condition inutile, cf. note de bas de page précédente.»; footer «25», head «- 5 -».
- Compile **0-err, 394pp**.
- **SWEEP CURSOR → RRR Appendix p6 = idx39** (ex.2 tail «…du premier λ-anneau défini ici…»; ex.3 «Détermination de $K(G)$ et $K_r(G)$…»: globally-reductive $G$, tore maximal $T$, $K(T)=K_r(T)=\Z(\hat T)$, Weyl $W$, (1.13) $K_r(G)\to K_r(T)^W=K(T)^W$, Théorème 1.1 iso — LOTS of underlined-K to restore + $\hat T$/$\Z$ notation).

### #34 (2026-07-03) — RRR Appendix p4 (idx37 = vol p24) scribed (§2 Exemples ex.1: $\underline K(G)$/$\underline K_r(G)$ representation λ-rings) — heavy page
- **★ underlined-K notation restored** (crop-confirmed): the representation group is $\underline{K}(G)$, $\underline{K}_r(G)$ — the workpass had dropped the underline. Restored all 7 occurrences on this page (errata `[faithful]`; apply going forward).
- **2 more punctuation swaps reverted** (the appendix «improvement» pattern): «un anneau commutatif**.** On considère» → book «commutatif**~;** on» (2nd `;`→`.` this appendix); «de ce fait**.)**» → book «de ce fait**).**» (period moved outside the paren).
- **2 formulas the workpass DISPLAYED, inlined** to match the book: «…de la forme $(\rho\oplus\rho')-(\rho)-(\rho')$ (on note…» and «…de la forme $(\rho)-(\rho')-(\rho'')$ où $\rho$ est…» (dropped the display's stray trailing comma).
- **dropped emphasis restored** (`\emph`, book underlines): «\emph{algébriquement clos de caractéristique}», «\emph{détermination explicite}», «\emph{qui sera faite plus bas}».
- **BOOK TYPO → errata `[corrected]`:** «$\rho$ est une **présentation** extension» → «représentation».
- **footnote**: «cf.\ (VI 3.3)» (parens kept); book's double «(\*)» marker noted (edition attaches once).
- French `;` ×4.
- **verified vs scan:** ex.1 $K(G)$/$K_r(G)$ construction, «Gl(m,k)×Gl(n,k)», «complète réductibilité… $K(G)=K_r(G)$»; footnote 1 text; footer «24», head «- 4 -».
- Compile **0-err, 394pp**.
- **SWEEP CURSOR → RRR Appendix p5 = idx38** («Variantes de l'exemple précédent…» + its footnote «autres exemples… Riemann–Roch !»; ex.2 $X$ variété algébrique / fibrés vectoriels — the $(E\oplus E')-(E)-(E')$ and $(E)-(E')-(E'')$ quotients; watch for underlined K / $\underline K(X)$).

### #33 (2026-07-03) — RRR Appendix p3 (idx36 = vol p23) scribed (§1 tail: (1.8)–(1.11) *special* λ-rings; §2 Exemples begins)
- **inline formula restored + dropped emphasis:** «les coefficients $c_n(\lambda^i(f))=c_n\text{ de }\lambda^i(f)$ se calculent au moyen de polynômes \emph{universels}…» (workpass had displayed the $c_n(\lambda^i(f))=\dots$ and dropped «universels»).
- **★ book COMMA restored:** the workpass changed «$K$ devient un $\lambda$-anneau**,** son élément nul est 1» into «…$\lambda$-anneau **;** son…». Reverted to the book's comma (2nd instance this appendix of the workpass swapping the book's `;`/`,`/`.` punctuation).
- **★ (1.11) 3rd line superscript reverted to the book:** «$P_{i,n}(\lambda^1x,\dots,\lambda^{\mathbf n}x)$» — the book's last index is $n$; the workpass had silently "corrected" it to $\lambda^{in}x$. Reproduced $\lambda^n x$ as printed (errata `[faithful]`, flagging the $n$-vs-$in$ inconsistency with (1.8)).
- **2 BOOK TYPOS → errata `[corrected]`:** «homomorphimse» (m/s transposition, →homomorphisme); (1.10) «$\lambda^i(\lambda_t(x)$» unbalanced open paren (→ balanced).
- **French `;`/`:` spacing** ×5 («on ait~:», «relation~:», «formules~:», «explicitement~:», «spécial~;»).
- **verified vs scan:** (1.8) $c_n=P_{i,n}(a_1,\dots,a_{in})$; (1.9) $\lambda^i(1+at)=1$; (1.7 bis) $(1+at)\circ f=f(at)$; (1.10) three special-λ formulas; (1.11) $\{\lambda^i(1)=0\ (i>1);\ \lambda^n(xy)=P_n(\dots);\ \lambda^n(\lambda^i(x))=P_{i,n}(\dots)\}$; «$P_{i,n}$ isobare de poids $in$»; footer «23», head «- 3 -».
- Compile **0-err, 394pp**.
- **SWEEP CURSOR → RRR Appendix p4 = idx37** (§2 Exemples: finish «…est spé\-cial ; mais nous n'aurons pas besoin de ce fait.»; ex.1 $K(G)$/$K_r(G)$ group-representation λ-rings [note the 2 footnotes: «$k$ alg. clos… cf VI 3.3» and «autres exemples… Riemann–Roch !»]; ex.2 $X$ variété algébrique, fibrés vectoriels).

### #32 (2026-07-03) — RRR Appendix p2 (idx35 = vol p22) scribed (§1 cont: ℤ λ-structure; the *special* λ-ring $K=1+k[[t]]^+$, (1.6)–(1.7))
- **2 formulas the workpass wrongly DISPLAYED, inlined to match the scan:** «d'où $\lambda^i(n)=\binom{n}{i}$.» and «soit $K=1+k[[t]]^+$ le groupe des séries formelles…» (both run inline in the book, not centred).
- **★ book punctuation restored:** the workpass changed the book's «d'augmentation $1$**;** on va y introduire» (semicolon, lowercase «on») into «$1$**.** On va» (period + capital). Restored to «$1$~; on va».
- **dropped emphasis restored** (`\emph`, book underlines it): «des polynômes \emph{universels} à coefficients entiers».
- **emphasis extent widened:** «$\lambda$-\emph{anneau spécial}» (book underlines «anneau spécial»; the workpass emphasized only «spécial»).
- **guillemets:** «l'~addition~» (was ``addition''); French `;`/`:` thin spaces («claire~;», «respectivement~:», «linéaires par~:», «symétriques~;»).
- **verified vs scan:** (1.4) $\lambda_t(1)=1+t$; (1.5) $\lambda_t(n)=(1+t)^n$; (1.6) $c_n=P_n(a_1,\dots,a_n;b_1,\dots,b_n)$; (1.7) $(1+at)\circ(1+bt)=1+abt$; the $f\circ g$ multiplication text; «$P_n$ isobare de poids $n$… symétrique en $a=(a_i)$ et $b=(b_i)$»; footer «22», internal head «- 2 -». λ-augmented / λ-special defn text matches.
- Compile **0-err, 394pp**.
- **SWEEP CURSOR → RRR Appendix p3 = idx36** (§1 cont: the $\lambda^i(f)$ determination — $c_n(\lambda^i(f))$, (1.8) $c_n=P_{i,n}(a_1,\dots,a_{in})$, (1.9) $\lambda^i(1+at)=1$ [+ tail], then presumably the *special* condition «de la page 3» referenced by the §1 footnote).

### #31 (2026-07-03) — RRR Appendix p1 (idx34 = vol p21) scribed (CHAPITRE I / §1 Définitions — λ-rings (1.1)–(1.5))
- **★ WRONG FORMULA (1.2) fixed:** the workpass **subscripted the arguments** — «$\lambda_x^0=1,\ \lambda_x^1=x,\ \lambda^n(x+y)=\sum\lambda_x^i\lambda_y^{n-i}$» — but the scan writes them **inline with a product dot** (800 dpi crop): «$\lambda^0x=1,\ \lambda^1x=x,\ \lambda^n(x+y)=\sum_{i=0}^n\lambda^ix\cdot\lambda^{n-i}y$». Corrected (the λ-operations act on x/y as arguments, they are not indexed by x/y).
- **arrow glyphs resolved by crop:** «$x\longmapsto\lambda_t(x)$» is a genuine **maps-to** (kept `\longmapsto`); the augmentation display «$1+\sum_{i>0}x_it^i\longrightarrow x_1$» is a **plain arrow** — fixed `\longmapsto`→`\longrightarrow` (the book distinguishes them).
- French `:` spacing «conditions suivantes~:».
- **verified vs scan:** (1.1) $\lambda^i:K\to K$; (1.3) $\lambda_t(x)=\sum_{n\geq0}\lambda^n(x)t^n\in K[[t]]$; the «$1+K[[t]]^+$», «d'augmentation 1» text; §1 footnote «pré-λ-anneau (V 2.1)… la page 3 (cf V 2.4)» matches; footer «21» (vol page).
- **★ EMPHASIS CONVENTION for the RRR appendix (decision):** the Codex appendix transcription renders the typescript's **underline-emphasis of defined terms as italic `\emph`** (e.g. «λ-anneau», «pré-λ-anneau»). The book underlines them. **Kept `\emph`** for the appendix — it is present, internally consistent, and a standard modern rendering; converting the whole appendix to `\underline` would be large + error-prone and the emphasis is *not dropped* (unlike the main text, where I restored dropped underlines as `\underline`). Documented as an intentional appendix-local convention. *(Revisit only if Floris wants strict underline parity with the main text.)*
- Compile **0-err, 394pp**.
- **SWEEP CURSOR → RRR Appendix p2 = idx35** (§1 cont: the $\mathbb Z$ λ-structure (1.4)/(1.5), $\lambda^i(n)=\binom ni$; λ-homomorphism / augmented λ-ring; the *special* λ-ring setup — $K=1+k[[t]]^+$, the $f\circ g$ multiplication (1.6) $c_n=P_n(a_1,\dots;b_1,\dots)$).

### #30 (2026-07-03) — RRR Appendix TITLE + TOC page (idx33 = SGA6 vol p20) scribed; ★ appendix offset established
- **★ OFFSET for the RRR appendix body: `appendix_page = idx − 33`** — idx34 = appendix **p1** (CHAPITRE I / §1 Définitions), confirmed against the TOC («1. Définitions … 1») and the idx34 scan. The **title+TOC page itself is SGA6 vol p20** (footer «20», running header «0 App : RRR»); the appendix's own 1,4,8,13,18,… numbering starts at idx34.
- **★ ORDERING FIX:** «Démonstration du théorème de Riemann--Roch (1er Novembre 1957).» was mis-placed by the workpass **before** the TOC; the scan has it **after** the whole TOC (below CHAP II §6 «… 49»), just above the footnote rule. Moved it there; added `\clearpage` so CHAPITRE I starts fresh (matches the scan's page break to idx34).
- **TOC verified vs scan (all entries + page refs match):** CHAP I — 1.Définitions 1 / 2.Exemples 4 / 3.Le λ-anneau défini par un anneau gradué 8 / 4.Les opérations λ^p(N,x) 13; CHAP II — 1.La théorie de Chow 18 / 2.Définition des classes de Chern des faisceaux algébriques cohérents 22 / 3.Généralités fonctorielles sur K(X) 27 / 4.Quelques résultats techniques 34 / 5.Définition faisceautique des classes de Chern. Application à l'étude des morphismes d'injection 43 / 6.Le théorème de Riemann--Roch 49.
- **footnote (\*)** verified verbatim («Ceci est la reproduction textuelle du rapport cité dans l'Introduction… (\*), (\*\*) ont été rajoutées en Octobre 1967.»).
- **noted (not fixed):** the scan's TOC repeats a page ref «…et classes de Chern …… 18» on the CHAP II *heading* line; the edition sets chapter headings as `\subsection*` (bold, no leader), so that redundant «18» (= §1 «La théorie de Chow … 18») is dropped — TOC-layout modernization, all section page refs preserved. Title/author set title-case+bold (book: all-caps+underlined) per edition heading style.
- Compile **0-err, 394pp**.
- **SWEEP CURSOR → RRR Appendix p1 = idx34** (CHAPITRE I / §1 Définitions: λ-rings — (1.1) λ^i:K→K, (1.2) λ^0x=1/λ^1x=x/λ^n(x+y)=∑λ^i x·λ^{n-i} y, (1.3) λ_t(x)=∑λ^n(x)t^n∈K[[t]], (1.4)/(1.5), λ^i(n)=C(n,i); note the §1 footnote «pré-λ-anneau (V 2.1)…»).

### #29 (2026-07-03) — Exposé 0 p19 (idx32) scribed (Bibliographie [1]–[7]) — verified every author/title/journal/vol/pages/year
- **[3]** «Pub. Math. **n\textsuperscript{o}~5**» (was «no. 5»).
- **[4]** restored parens «Princeton 1957, **(**cité [RRR] et reproduit en Appendice à l'Exp.\ 0 du Séminaire**)**» (workpass had no parens); `Exp.\ 0` spacing.
- **[6]** «à l'**IHES**» (book prints IHES without periods; workpass had «I.H.E.S.»).
- **[1] BOOK TYPO → errata `[corrected]`:** «vol. 3, **Différential** Geometry» (parasitic acute on the English «Differential»); edition keeps «Differential».
- **verified clean vs scan:** [1] Atiyah–Hirzebruch «Vector bundles and homogeneous spaces», Symposia in Pure Mathematics vol. 3, p. 7--38, 1961; [2] Borel–Serre «Le théorème de Riemann--Roch», Bull. Soc. math. France t. 86, p. 97--136 (1958); [4] Grothendieck «Classes de faisceaux…» [RRR]; [5] Grothendieck «Technique de descente…» (FGA), Séminaire Bourbaki 1957--1962; [7] Atiyah–Hirzebruch «The Riemann--Roch theorem for analytic embeddings», Topology vol. 1, p. 151--166 (1962).
- **normalizations logged** (errata): en-dash page/year ranges; italic cited titles (book plain); «J.-P. Serre» kept (entry prints «J.P.»).
- **BIBLIOGRAPHIE heading** (book: all-caps + underlined) rendered as `\section*{Bibliographie}` (bold, edition style — same as other headings).
- Compile **0-err, 394pp**.
- **SWEEP CURSOR → Exposé 0 Appendice «RRR» p1 = idx33?** (verify offset: the RRR appendix «Classes de faisceaux et théorème de Riemann–Roch» by Grothendieck reprints with its OWN page numbering — first locate its p1 in the scan; workpass L545+ has the appendix title + the (\*)/(\*\*) footnote). Check the page after idx32 for the appendix start / any blank recto.

### #28 (2026-07-03) — Exposé 0 p18 (idx31) scribed (§7 tail: «foncteur déterminant» (7.2)/(7.3); END of Exp 0 body) — det^* star + ≃ + underlines
- **★ det functor is $\det^*$ (STAR), not $\det^\bullet$** (900 dpi crop — same asterisk glyph as the cohomology-star; distinct from K-theory bullet). Fixed in (7.2) and (7.3).
- **(7.3): relation is $\simeq$, not `=`** — «$\det^*(L)\simeq\bigotimes_i\det(L_i)^{(-1)^i}$» (the workpass had `=`; the book prints a canonical-iso «≃»).
- **(7.2): category names underlined** — «$\underline{\Parf_{\mathrm{is}}}(X)\to\underline{\Inv}(X)$» (the underline covers the names $\mathrm{Parf}_{\mathrm{is}}$, $\mathrm{Inv}$ only, not the «(X)»). Kept $\Parf_{\mathrm{is}}$ as a proper subscript = modern rendering of the typewriter's inline «Parfis», same policy as «K.»→$K_\bullet$.
- **«foncteur déterminant»** is quoted **and** underlined in the book → «~\uline{foncteur déterminant}~».
- **«Modules»/«Module» capitalized** (2×: «catégorie des **Modules** inversibles», «du **Module** localement libre $L_i$») — the sheaf-Module convention; workpass had lowercased.
- **guillemets:** «~nature locale~», «~yoga~»; **`Exp.\ XI`** spacing.
- **No book typos** this page. Bibliographie is NOT on p18 (scan ends at «…exposés I à XI.»; the biblio is on p19).
- Compile **0-err, 394pp**.
- **SWEEP CURSOR → Exposé 0 p19 = idx32** (**Bibliographie** [1]–[7]: Atiyah–Hirzebruch, Borel–Serre, Grauert, Grothendieck ×2 [RRR]/[FGA], Shih, Atiyah–Hirzebruch — verify authors/titles/journals/pages vs scan).

### #27 (2026-07-03) — Exposé 0 p17 (idx30) scribed (§6 tail: transpose $f^*/f_*$; §7: Picard group, (7.1)) — 6 restored parens + 6 underlines
- **6 restored parenthetical pairs** the workpass had flattened to commas (band/OCR confirmed):
  - «des Exp.\ VI, VII, VIII **(**centrés sur la démonstration du théorème de Riemann--Roch**)** et de Exp.\ IX»
  - «le groupe de Picard, **(**ou groupe des classes de diviseurs dans la terminologie classique**)**»
  - «pour le groupe de Picard **(**annoncés sans démonstration dans [6]**)** est faite»
  - «purement numérique **(**n'utilisant pas la théorie du foncteur de Picard et de sa représentabilité**)**, dues»
  - «aux méthodes de Kleiman **(**et dont il est obligé de faire usage**)** est [6, C-07 (i)]»
  - «certains raffinements **(**incluant certains théorèmes de représentabilité pour le foncteur de Picard**)** occupe»
- **6 underlined key-terms restored** (`\uline`): «relations numériques»; «comportement de»…«par spécialisation»; «groupe de Picard»; «classes de diviseurs»; «équivalence numérique»; «théorèmes de finitude pour le groupe de Picard».
- **display connector fixed:** the two transpose homomorphisms are joined by the word **«et»** in the book («$f^*:\Gr^\bullet(Y)\to\Gr^\bullet(X)$ et $f_*:\Gr_\bullet(X)\to\Gr_\bullet(Y)$»); the workpass had a bare «,\qquad» → «\qquad\text{et}\qquad».
- **«occupent»→«occupe»** (book singular, 1000 dpi crop-confirmed) → errata `[faithful]`.
- **`Exp.\ ` spacing** (X / VI / IX / XIII), French `;` («[5]~;»).
- (7.1) «$c_1:\Pic(X)\xrightarrow{\sim}\Gr^1(X)$» verified vs scan.
- Compile **0-err, 394pp**.
- **SWEEP CURSOR → Exposé 0 p18 = idx31** (§7 tail: «foncteur déterminant» (7.2) $\det^\bullet:\Parf_{\mathrm{is}}(X)\to\Inv(X)$, (7.3) $\det^\bullet(L)=\bigotimes_i\det(L_i)^{(-1)^i}$, «yoga» remark; then start of **Bibliographie** [1]–…).

### #26 (2026-07-03) — Exposé 0 p16 (idx29) scribed (§6 cont: (6.2)–(6.6), Euler–Poincaré char., duality) — wrong symbols + big underlined passage
- **★ WRONG SYMBOLS in (6.4) — 3 corrections (crop-confirmed 850–1000 dpi):** the workpass used $\pi_X$ / $\chi_X$ / $\pi_{X*}$; the book writes the projection **$f^X$**, the Euler–Poincaré characteristic **$\lambda_X$** (lambda, not chi!), and the pushforward **$f^X_*$**. Fixed the projection display, and (6.4) «$\lambda_X=f^X_*:K_\bullet(X)\to K_\bullet(\mathrm{point})=\mathbb Z$».
- **★ big UNDERLINED passage restored** (`\uline`, crop-traced): «Dans le point de vue proposé dans le Séminaire, une théorie des intersections maniable, sur les schémas noethériens $X$ pas nécessairement réguliers, doit consister en l'étude combinée des invariants contravariants … et des invariants covariants … qui jouent des rôles de nature essentiellement différente, et dont les propriétés se complètent mutuellement.» — the whole thing is underlined in the book, breaking only around the math $K^\bullet(X),\Gr^\bullet(X)$ / $K_\bullet(X),\Gr_\bullet(X)$ (3 `\uline` segments).
- **«caractéristique d'Euler--Poincaré»** is quoted **and** underlined in the book → «~\uline{…}~».
- **guillemets:** «~formule de projection~», «~suite exacte d'homotopie~», «~degré des $0$-cycles~» (were ``…'').
- **2 restored parens / dropped comma:** «l'homomorphisme (6.2) **(**qui est $K^\bullet(Y)$-linéaire**)**»; removed the workpass comma after «formule de projection~» (book: «…projection» i.e.», no comma).
- **French `;` spacing:** «([RRR] et Exp.\ IX)~;».
- **BOOK SPELLING reproduced:** «rôles **duals**» (for «duaux») — faithful, errata `[faithful]`.
- (6.4)–(6.6), the multiplication display and $f^*/f_*$ transpose pair (6.6): all present in the workpass, verified vs scan; $\Gr_0(X)=\Fil_0K_\bullet(X)$ now renders «Filt$_0$» (macro).
- Compile **0-err, 394pp**.
- **SWEEP CURSOR → Exposé 0 p17 = idx30** (§6 tail «tout comme la cohomologie et l'homologie. Ainsi, si $f:X\to Y$…» (6.6)-transpose + «Les homomorphismes (6.4) et (6.5)…»; then §7: Picard group, (7.1) $c_1:\Pic(X)\xrightarrow{\sim}\Gr^1(X)$).

### #25 (2026-07-03) — Exposé 0 p15 (idx28) scribed (§5 tail + §6: covariant $K_\bullet$, cap-product/Poincaré-duality, filtration + (6.1)) — dropped footnote restored, macro fix, 3 crops
- **★ DROPPED FOOTNOTE restored** (the biggest miss): the book's «cap-produit\,(\*)» footnote — «Cette analogie n'est d'ailleurs pas purement verbale, et peut se préciser, après passage aux gradués $\Gr^\bullet(X)$, $\Gr_\bullet(X)$ associés, par une relation de compatibilité explicite entre la structure de module sur $\Gr_\bullet(X)$ et l'opération «~cap~».» — was **entirely absent** from the workpass. Added as `\footnote{…}` (750 dpi transcription). Marker «(\*)»→numbered (edition style).
- **★ MACRO FIX (global):** `\Fil` rendered «Fil»; the book's filtration operator is **«Filt»** (crop-confirmed on (6.1) and «$\Fil_i K_\bullet(X)$»). Redefined `\newcommand{\Fil}{\operatorname{Filt}}` — corrects all **236** occurrences document-wide.
- **2 dropped underlines restored:** «l'anneau de \underline{cohomologie} entière», «un analogue de l'\underline{homologie} entière» (both underlined in the book).
- **1 dropped underline restored (multi-word):** «\uline{classes de cycles algébriques}».
- **«module»→«Module»** (cap) in «la structure de **Module** de $K_\bullet(X)$ sur $K^\bullet(X)$» (band-2 confirmed capital; the §6 «module filtré»/«structure de module sur Gr» stay lowercase per scan — book varies).
- **2 restored parenthetical pairs** the workpass had flattened: «…sur $X$, **(**pour une relation d'équivalence… corps de base $K$**)**. Si».
- **«Gr.(X)» restored as a centred display** (the workpass had inlined it): «…noté \[ \Gr_\bullet(X), \] d'une structure…».
- **«Chern, etc.»→«Chern\dots»** (book has an ellipsis, not «etc.»).
- **«supp» lowercase** (was `\operatorname{Supp}`); **«corps de base $K$»** capital (was `$k$`) — reproduced as printed (see errata: book K/k inconsistency).
- **French `;` spacing:** «cohomologie entière~; et il».
- **3 BOOK TYPOS → errata `[corrected]`:** «rationelle»×2 (for «rationnelle»); «signalé» (for fem. «signalée»); (6.1) unbalanced open paren «Filt_j(K_•(X)».
- Compile **0-err, 394pp** (236 `\Fil`→«Filt» verified).
- **SWEEP CURSOR → Exposé 0 p16 = idx29** (§6 cont: «Si $f:X\to Y$ est un morphisme propre de schémas noethériens, alors» (6.2) $f_*:K_\bullet(X)\to K_\bullet(Y)$, (6.3) $f_*:\Gr_\bullet(X)\to\Gr_\bullet(Y)$, «formule de projection» $\Gr^\bullet(Y)$-linéaire; then the (6.4?) isomorphisms $K_\bullet(X[t])\simeq K_\bullet(X)$ etc.).

### #24 (2026-07-03) — Exposé 0 p14 (idx27) scribed (§5 cont: (5.2)/(5.3)/(5.4) topological Riemann–Roch diagrams) — 10 fixes, 4 resolved by tight crops
- **★ NEW CONVENTION resolved by crop (1000 dpi, glyphs side-by-side in (5.4)):** cohomology exponent is a **star** `H^{2*}`, K-theory a **round bullet** `K^\bullet` — the workpass had unified both to `\bullet`. Fixed `H^{2\bullet}`→`H^{2*}` in (5.4) ×2 and the bottom Chern display ×1. **Apply this distinction on all later pages.**
- **(5.4) diagram — 2 faithfulness fixes (crop-confirmed):**
  - arrow labels are **plain long arrows** «$x\longrightarrow \ch(x)\Todd(T_X)$», not $\mapsto$ (typewriter had no maps-to); `\mapsto`→`\longrightarrow` ×2.
  - vertical arrows are **BARE** in the book — removed the workpass's interpolated `\downarrow f_*` labels (both) → `\downarrow`. (The book names them in the next sentence: «la première… même que dans (5.3), … la deuxième… l'homomorphisme de Gysin».)
- **4 restored parenthetical pairs the workpass had flattened to commas** (OCR + crop confirmed):
  - «…par la formule (3.2) **(**qui utilise ici implicitement le théorème de finitude de Grauert [4] pour un morphisme propre d'espaces analytiques**)** on trouve…»
  - «…des groupes du type $K^\bullet$ **(**à l'exclusion d'anneaux du type anneaux de Chow ou de cohomologie**)**~:»
  - «…entre cette assertion **(**qui ne néglige pas les phénomènes de torsion, et se place dans un groupe $K^\bullet(Y^{\mathrm{top}})$ de nature essentiellement discrète**)**, et…»
  - «…du théorème de l'index de Atiyah--Singer **(**et de ses généralisations dues à Shih [7] et Atiyah**)**, qui…»
- **paraphrase fixed:** «savoir la commutativité du **carré**» (workpass had «du diagramme» — the scan says «carré», confirmed OCR + 650 dpi crop).
- **dropped comma restored:** «phénomènes de torsion**,** et se place» (scan has the comma).
- **guillemets:** «~Chow~», «~théorème de Riemann--Roch différentiable~» (were ``…'' TeX quotes).
- **n°:** «au n\textsuperscript{o}~4» ×2 (were «no. 4»).
- **BOOK TYPO → errata `[corrected]`:** «[1] un homomorphisme **groupes**» — «de» dropped before «groupes» (1100 dpi crop: no «de» in the gap). Edition restores «de groupes».
- **(5.3) diagram** verified vs crop: $f_*$ (left vertical) and $f^{\mathrm{top}}_*$ (right vertical) labels present & correct; kept.
- Compile **0-err, 394pp**.
- **SWEEP CURSOR → Exposé 0 p15 = idx28** (§6: covariant $K_\bullet(X)$ / cap-product / Poincaré-duality analogy; then filtration $\Fil_iK_\bullet$, (6.1) $\Fil^iK^\bullet\cdot\Fil_jK_\bullet\subset\Fil_{j-i}K_\bullet$, graded $\Gr_\bullet(X)$, (6.2) $f_*:K_\bullet(X)\to K_\bullet(Y)$, (6.3) $f_*:\Gr_\bullet(X)\to\Gr_\bullet(Y)$, projection formula).

### #23 (2026-07-03) — Exposé 0 p13 (idx26) scribed (§4.5 tail + §5 analytic/rigid-analytic Riemann–Roch) — 3 restored paren-pairs + 1 wrongly-displayed formula inlined
- **§4.5 tail:** «Voir commentaires dans Exp.\ XIV n\textsuperscript{o}~2.» (was «Exp. XIV, no. 2» — dropped the n° form, spurious comma before n°).
- **§5 (analytic RR) — 3 parenthetical pairs the workpass had flattened to commas, restored to the scan:**
  - «…d'espaces analytiques complexes **(**ou d'espaces rigide-analytiques au sens de Tate**)**.» (workpass had «complexes, ou … Tate.»).
  - «…principe expliqué dans 4.2 **(**la difficulté qui y est rencontrée … comme on le signale dans Exp.\ XIV n\textsuperscript{o}~1**)**.» (workpass had «4.2, la difficulté … Exp. XIV, no. 1.» — both the opening paren after 4.2 and the closing paren before the final period were missing).
  - «…comme dans le cas **(**déjà signalé dans 3.1**)** d'un schéma…» (workpass had no parens).
- **emphasis restored:** «le morphisme $f$ est \underline{projectif}» (underlined in the scan; workpass had it plain).
- **«et, comme»→«et comme»:** dropped the spurious comma after «et» (scan: «projectif, et comme dans le cas algébrique»).
- **wrongly-displayed formula inlined:** «Si maintenant $f:X\longrightarrow Y$ est un morphisme d'espaces analytiques non singuliers compacts» — the workpass had broken $f:X\to Y$ out into a `\[…\]` display; in the scan it runs inline. (The earlier $X^{\mathrm{top}}\to X$ and the tagged (5.1) K•(X)→K•(X^top) ARE genuine displays in the scan — kept.)
- **guillemets:** «~anneau de Chow analytique~» (was ``…'' TeX quotes — L357+ lineage, normalized on contact).
- **n°/spacing normalizations:** «dans le n\textsuperscript{o}~4»; «$X^{\mathrm{top}}$ compact~;» (French thin space); «(Exp.\ II)».
- **notation confirmed vs scan:** $\Gr^\bullet(X)$ and $\Gr^\bullet(X)_{\mathbb Q}$ (raised-dot = graded bullet ✓); $K^\bullet$ throughout (superscript-dot ✓); Riemann--Roch / Atiyah--Hirzebruch en-dashes ✓; «[RRR]», «[1]» citations ✓.
- **No book typos on this page** — no new errata entry.
- Compile **0-err, 394pp**.
- **SWEEP CURSOR → Exposé 0 p14 = idx27** (§5 cont: «…grâce à Atiyah–Hirzebruch [1] un homomorphisme de groupes» (5.2) $f^{\mathrm{top}}_*$, then (5.3) the commutative square of $K^\bullet$, and (5.4)).

### #22 (2026-07-03) — Exposé 0 p12 (idx25) scribed (§4.4 general cotangent construction + §4.5 start) — no-flag pass
- **★ underline convention REFINED (10× crops):** on this page only the **structure sheaf $O$ is underlined** ($\underline O_X$, $\underline O_Y$); the abstract algebra symbols $A,B,C,J,T$ and $\Omega$ are **plain** — a coherent authorial distinction (sheaves-on-the-space vs abstract algebra in the topos setting). Reconciles the "is J/Ω underlined?" question per-page.
- **§4.4 general construction:** $L_{X/Y}$→$L^{X/Y}_\bullet$; **inlined $f:X\to Y$** (was displayed); «(commutativement)» parens; «annelés~:» colon; $\underline O_X$, $f^{-1}(\underline O_Y)$ (parens); «Anneau»/«Algèbre» caps; **$\varphi$: label** on $C=A[T]\to B$; **$U\mapsto A(U)[T(U)]$ inlined** + appended «= $A(U)$-algèbre…engendré par $T(U)$» + parenthesized; «noyau de $\varphi$» (was «$C\to B$»); $J/J^2\xrightarrow{d}\Omega^1_{C/A}\otimes_C B$ (arrow labelled d).
- **underlines:** «\uline{complexe cotangent relatif $L^{X/Y}_\bullet$ de $X$ sur $Y$}» (definitional); \underline{parfait}; \underline{globalement}.
- **cross-ref «(4.2)»→«(4.3)»** (the $T_f$ formula was renumbered on p11).
- **§4.5:** parens «(l'hypothèse noethérienne…)»; «~sophistiqué~» guillemets.
- **Book typos → errata:** naturelle→naturel; précédent→précèdent.
- Compile **0-err, 394pp**.
- **SWEEP CURSOR → Exposé 0 p13 = idx26** (§4.5 tail «…corps algébriquement clos de caractéristique $p>0$… Exp. XIV n° 2» + §5 analytic/rigid-analytic Riemann–Roch).

### #18 (2026-07-03) — ★ METHOD CORRECTION (Floris, firm): NO FLAGGING. Resolve every ambiguity and FIX it — one-shot per page.
- Floris: «make sure you one-shot each page… why are you flagging open items? You fix. You are singularly responsible for doing SGA 6.» **⇒ NEVER leave a "documented low-confidence" flag. When a glyph is ambiguous, zoom/OCR/cross-reference until decided, then FIX it — before moving on.** A page is not done until every symbol is resolved.
- **ALL prior open flags now RESOLVED** (text-anchored `search_for` crops at 11×):
  - **(j=i) → (j≤i):** book prints `=` but «combinaison linéaire des $\lambda^j$» needs $j\le i$ → book typo, edition keeps `\le`, errata added.
  - **$\cl(F)\in K(X)$:** confirmed element-of (∈), `\in` correct — no change.
  - **display-1 LHS:** book prints **plain $\cl(L_\bullet)$** on the LHS (superscript dropped), $\cl^\bullet$ on the RHS — FIXED the LHS (`\cl^\bullet`→`\cl`).
- **Technique that works for glyph-hunting:** `page.search_for("<anchor word>")` → bbox → crop a small offset from it at 9–11× (reliable, unlike guessed pixel coords).
- Compile **0-err, 394pp**. No open flags remain on pp.1–8.

### #16 (2026-07-03) — BACK-CHECK pass (Floris: verify pages 1–20 before advancing) — caught 2 real errors + 1 self-correction
- **Corrected my own mistaken claims / open flags:**
  - **Title page: PRESENT** (workpass L80–92: «Séminaire de Géométrie Algébrique du Bois Marie / 1966–67 / Théorie des intersections et théorème de Riemann-Roch / (SGA 6) / dirigé par P. Berthelot, A. Grothendieck, L. Illusie / avec la collaboration de D. Ferrand, J.-P. Jouanolou, O. Jussila, S. Kleiman, M. Raynaud, J.-P. Serre»). My earlier «skipped the title page» was WRONG. Content complete; workpass modernizes the scan's ALL-CAPS→mixed case (title-page convention, kept).
  - **★ (1.2)→(2.2)** on p6 §3 opening: the scan's **OCR text layer reads «à la formule (2.2)»**; I had wrongly KEPT «(1.2)». **FIXED to (2.2)** (faithful to scan). Mathematically (1.2) fits better (cf. §2.4) → possible book typo, but reproduced as printed; not errata'd pending certainty. **This is exactly the kind of flagged-but-unresolved item Floris was right to push on.**
  - **«expressions»→«expression»** (idx17): OCR confirms book singular. FIXED.
- **Confirmed correct, no change:** idx16 «défini par (2.1)» (OCR «(2 1)»); idx20 «L.»=$L_\bullet$ and «L'» (OCR «L!'»); **p1 F is plain** (crops) — book VARIES: F plain in §1–2 (regular), underlined $\underline F$ in §3 (derived) — reproduced per-page, no inconsistency error.
- **Remaining documented low-confidence** (math-correct as written; book glyph ambiguous even at 360 dpi, OCR garbled): «$\lambda^j\ (j\le i)$» (=vs≤); «$\cl(F)\in K(X)$» (∈ vs ⊂). Accept as-is with note.
- **Honest status of pp. 1–7 + front matter:** each page read band-by-band vs the 360 dpi scan and corrected; NOT certified «100% complete» (never-certify) — carefully scan-verified with the 2 residual glyph-ambiguities above. Compile **0-err, 394pp**.
- **SWEEP CURSOR → Exposé 0 p8 = idx21** (continue).
