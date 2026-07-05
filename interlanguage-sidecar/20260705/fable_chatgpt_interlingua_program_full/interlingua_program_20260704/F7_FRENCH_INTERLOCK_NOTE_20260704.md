# F7 — French Interlock Note
2026-07-04. Small note, high leverage: three lanes use the same French mathematical register; they should cite each other's witnesses instead of re-collecting. French is an interlock node, NOT an authority or hidden pivot (dominance discipline applies to it like to Spanish/Russian/English).

## The three users of the French register

1. **SGA source-fidelity lanes (SGA5 done/livrable, SGA6 active)** — French as SOURCE language; the certified .tex corpora are register ground truth for 20th-century French algebraic prose (séminaire register): `_claude_aid\sga6_full_audit_20260703\sga6_fr_workpass.tex` (18882 lines), SGA5 edition + ERRATA/CERT trail. Also Chatnotes: `SGA restart`, `SGA continuation 2`, `SGA high fidelity semi restart`.
2. **Noether→French translation lane (R1)** — French as TARGET: papers 19–40 translated with per-section ledgers (`logs/FRENCH_P*_TRANSLATION_*.md`), cumulative renders (`renders/non_slavic_existing_translation_artifacts/french_*/cum_fr_*.pdf`, 262pp+ at P24), plus `glossary/french_paper41/43/post44 term rationale` files. Also Chatnotes `Noether French Codex`.
3. **Pan-Romance bridge lane (R1)** — French as TIER-0 WITNESS: 60/60 spine rows French-attested (`french_evidence` pointers like `french/0711.3658v2/rat1e.tex:66` in the source-hit table); French co-anchors the family matrix with Spanish.

## The cross-references to institute (per lane, one line each)

- Pan-Romance spine rows SHOULD cite Noether-French translation ledgers as additional witnesses for the ~60 core concepts (same concepts, reviewed prose, already rendered) — richer than one-line hit evidence.
- Noether-French term rationales SHOULD cite SGA .tex usage where the term occurs (e.g., anneau, corps, idéal, module, noethérien are all SGA-certified usage at scale) — upgrades "translation choice" to "attested against 300+pp certified native corpus".
- SGA lanes gain nothing lexically (they are source-fidelity work) but their certified corpora should be LISTED as register witnesses in the Pan-Romance family source matrix (they currently are not — the matrix draws on downloaded shelves while a certified in-house French corpus sits next door).

## Boundary
French evidence supports French rows and Romance-family triangulation. It must not become the default surface for bridge forms (dominance_penalty applies) nor a pivot for non-Romance lanes. Registers differ (Noether-era German-mathematical-French translation vs séminaire French vs modern textbook French) — cite with register tags.

## Action items (small)
- [ ] Add `sga_certified_usage` pointer field to French rows in the Pan-Romance family source matrix (handoff to codex lane).
- [ ] Add SGA5/SGA6 .tex to the Pan-Romance source shelf list with register tag `seminaire_1960s_certified`.
- [ ] Note in the union spine v3 build: French column may carry two witness classes (translation-lane, sga-certified).
