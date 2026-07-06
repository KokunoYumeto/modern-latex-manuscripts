# ROUTE-B KWIC PROBE v1 — REJECTED AS-IS (defect D6) + refined spec
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
