# Kolco-Family Internal Consistency Ledger + Quotient-Field Internal Audit

2026-07-04. Corpus's own Latin-script TeX (deduplicated). Internal-consistency evidence only — not witnesses.

**Findings addendum (same day, after glossary cross-check):**
1. **Cross-validation:** kolc* = 1059 occurrences — identical to ChatGPT's independent count on the zip feed. prsten = 2 (Paper 25), locally verified in context.
2. **Quotient-field: SECOND internal inconsistency.** Glossary decisions render *Quotientenkörper* as `polje kvocientov` (papers 06, 24, 30) but `kvocientno polje` (paper 09) — two word-orders for one concept. Correction to earlier artifacts: the comparative analysis/scores used placeholder "polje častnikov?" — the actual corpus forms are the kvocient-family ones (uk поле часток was the source of the častnik guess). W/S competitor evidence (cs podílové těleso, pl ciało ułamków) unaffected.
3. **RETRACTED (same day): the p24/p30 "glossary↔text drift" was a scan-path error, not real drift.** Those papers keep Interslavic under `working\sectionNN\interslavic\` and versioned intro files, which my per-paper probe missed; full-tree grep finds kvocient 44× (p24) and 30× (p30), including `polje kvocientov` in rendered text (p30 intro L38). Consequences: (a) the drift audit CLASS is retained as a check worth running, with correct path handling — no confirmed instance yet; (b) the scan scripts must glob per-paper trees fully (working/, versioned files), not assume one layout; (c) inconsistency #2 (polje kvocientov p06/24/30 vs kvocientno polje p09-glossary) stands at glossary level; p09 s10 tex check queued.

- Files scanned (dedup): 265; kolc* total 1059 across 43 distinct forms in 19 papers.
- prsten* occurrences: 2 — paper25 L68 (prsten); paper25 L68 (prsten)

## Top kolc* forms (compound inventory)

-   399  kolco
-   258  kolca
-   106  kolcu
-    76  kolc
-    39  podkolco
-    27  kolcom
-    23  podkolca
-    17  kolcah
-    12  podkolcu
-    11  kolcam
-    11  kolcovo
-     8  kolceva
-     7  kolcevo
-     7  kolcev
-     6  kolcovy
-     5  kolcami
-     4  podkolcom
-     4  podkolcah
-     3  podkolc
-     3  kolcevogo
-     3  kolcevoj
-     2  kolcove
-     2  kolcovyh
-     2  kolcovu
-     2  kolcevym

## Quotient-field internal usage

### isv_quotient — 12 sampled hits
- paper43 L42: …st dělimy s \(p\).  Tuto jest analog tomu, že diferencialny kvocient \(f'(x)\) polinoma \(f(x)\) jest dělimy najmanje \(…
- paper43 L44: …alna analogija. Diferentu možno razuměti kako diferencialny kvocient definujučego ideala čislovogo polja \(K\) v prirěđe…
- paper43 L44: …ialnoj oblasti od \(x_1,\ldots,x_n\), pri čem diferencialny kvocient jest vzet na městu \(x=\omega\), to jest pri \(x_1=…
- paper43 L44: …ov \(f(x)\), za ktore \(f(\omega)\) izčezava. Diferencialny kvocient \(\mathfrak M'[x\to\omega]\) jest definovany kako r…
- paper43 L44: …\(\mathfrak M'[x\to\omega]\) jest definovany kako razlikovy kvocient, vzet na městu \(x=\omega\).  Imenno, iz-za \(f(\om…