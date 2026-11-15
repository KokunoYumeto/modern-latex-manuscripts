# Framework paper v0.4: insert Result 6 (F12c/F13/F14), the global-register section,
# methods addendum, consolidated artifacts. v0.3 untouched.
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\user\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
s = (BASE / "FRAMEWORK_DRAFT_ORDERED_v0.3.md").read_text(encoding="utf-8")

NEW = """## 8a. Result 6 — The register layer: quantified doublet structure, resolved decisions, trap concepts (F12c, F13, F14)

**F12c (doublet structure with numbers).** Probing all 47 doublet-carrying proof-register groups against native-branch prose (cs/pl/sk vs sl/hr/sr/bg/mk, plus be) shows a hard West/South split with ZERO crossover on 16+ groups (must: musi W145/S0 vs mora W0/S177; namely: totiž W-only vs naime/namreč S-only; question: otázka/pytanie vs pitanje/vprašanje), ~17 pan-root groups (lež-, cel-, nul-, jednoznačn-), and a small no-pan-root residue (series: řada/szereg/niz/zaporedje four ways). Method rule earned twice over: every mechanical pan-verdict requires a homograph audit — two false pans in the first run were caused by cross-branch homographs (pl jednak "however" vs hr/sr jednak "equal"; cs případ "case" vs hr pripada "belongs").

**F13 resolution state.** The 67-row variant-scatter queue is now a decision table: 47 rows carry branch-evidence profiles; the 21 highest-stakes rows have drafted register decisions anchored to the community dictionary itself (diacritic-folded lookup; the dictionary's etymological orthography defeats naive matching). Headline outcomes: jednočasno replaces odnovrěmenno (dictionary headword; the čas-root is what West AND South use — the corpus form was the East-flavored outlier); odpovědati replaces sootvětstvovati (dictionary sense "correspond"); krok is the citation for step; skladati sę iz is recognized as a community-sanctioned West-facing doublet; and popolno, previously mislabeled South-leak, is dictionary-sanctioned. An internal target-review pass accepted the orthography band and three citation switches, and held ręd, jednako, and važiti for external authority — ręd because no pan-Slavic lexeme for "series" exists at all, jednako because the dictionary's "however" collides with the South homograph "equally", važiti because its mathematical sense is a register extension beyond the dictionary sense (weigh).

**F14 (trap concepts).** Four concepts failed sense-audits in INDEPENDENT lanes with different sources and auditors: modulus (module-collision: ES módulo, FR module, Arabic مودول), ground form (every language has a generic "fundamental form": ES forma fundamental = differential geometry, Arabic شكل أساسي = generic), complete system (ODE/residue-system senses), binary form (neural-net/binary-code senses); covariant/contravariant collide with tensor-calculus and category-theory senses. These form a standing trap list: any mechanical hit on a trap concept is presumed false until a context window shows the intended sense. This is the probe-side dual of the homograph rule.

## 9a. The global mathematical register as comparator column

**Provenance.** The idea has a three-step chain, recorded in AUTHORSHIP: the originating Codex GPT-5 session listed "purpose-built mathematical interlanguages, where formula grammar and proof discourse could define a narrow, transparent controlled language" among generalization pilots in its publication reflections (June 2026); user extended it with the global-weights framing ("use the weights for any concept globally", July 2026); this program formalized it as an argmax COLUMN of the existing weighted objective — not a new lane — and measured it.

**Historical anchor.** Peano ran the experiment (Latino sine flexione; the Formulario published real mathematics in it): the notation layer survived into universal use; the prose layer died. The modern descendants of the prose half are controlled natural languages and, at the formal limit, Lean. The register decomposes on our three strata: the formula layer is ALREADY the only successful global interlanguage ever deployed; the proof-prose layer is a ~530-lemma closed register (our coverage census: 96.6% of corpus prose tokens); the concept-term layer is partially internationalized and now measurable.

**Measurements.** Two independent instruments were run and cross-checked. (i) A cognate-basin probe over the 216-concept marker table: 27% of measurable concepts have a cross-family attractor form (v0.2, after an orthography-correspondence fix — see the methods addendum), with eponyms and internationalisms dominating the attractor set and `ring` the single most fragmented concept measured (17 form-basins worldwide: every language handled Dedekind's Zahlring metaphor its own way). (ii) A source-mass scorer over the same concepts: 21 global-attractor candidates, 28 global-with-local-glosses, 27 requiring regional doublets, 11 traps, 256 needing source intake. (iii) The connective layer has NO cross-family attractor at all (15 register connectives probed; 10 lack even a Slavic-internal pan-root): the connective layer of any global register is necessarily designed or symbolic — and where formula substitutes exist (∃, ∴, ⇒, ≝) they ARE the global form and are listed first in the register's gloss-block format.

**Cautions.** The dominance trap (F6) applies with full force: a "standardized global register" without the dominance penalty collapses into relabeled English. And the founding heuristic ("mathematicians read foreign math easily") is survivor-biased: it describes readers already trained through the hegemon language; students — the access-gain target population — are exactly the readers it fails. Hence the register's correct near-term role: not a product but a COMPARATOR COLUMN. A zonal bridge is justified exactly where it beats the global attractor in marginal intelligibility — which turns the first reviewer question ("why a zonal bridge and not just international vocabulary?") into a measured, per-concept answer. The connective layer is the canonical example: zero global attractors, strong zonal inheritance — precisely where zonal bridges earn their keep.

## 10a. Methods addendum — mutual catch as instrument-bias control

The triangulation protocol (three AI systems + human direction) matured during this phase into a symmetric instrument-bias control. Tally of confirmed catches across the phase: ChatGPT-side defects caught by this program include gloss-channel contamination (dictionary prefix-matching), false root-prefix attaches, silent apply failures, occurrence-offset patching that would have CREATED mixed orthography, and an eponym-scoring artifact (source-mass scoring demoting definitionally-global eponyms). Program-side defects caught by ChatGPT or by cross-checking include a tail-router over-routing (~22% route-key contamination), an over-generic stem list that let programming-course text contaminate a probe, a unit-inconsistent branch projection (withdrawn same day), and an orthography-folding artifact that systematically undercounted global attractors (groupe/grupa split; v0.1's 22% was an undercount, corrected to 27% in v0.2). The lesson generalizes: two independent instruments with DIFFERENT biases, plus adjudication against the underlying forms, beat either instrument alone — and every quantitative claim in this paper carries its instrument's known bias note.

## 11a. Consolidated artifacts (this phase)

- CONSOLIDATED_INTERLANGUAGE_INTERFACE v1.1 (json + self-contained HTML): all 216 concepts × 25 language columns × weight summary × global-register class × history class (descriptive tier) × R1 decisions with review verdicts × trap flags × cross-check adjudications. The whole map as one object.
- GLOBAL_CONNECTIVE_TABLE_v1: the designed half of the global register, with the gloss-block specification.
- GLOBAL_COLUMN_CROSSCHECK_v1, GLOBAL_ATTRACTOR_PROBE_v0_2, NORMALIZATION_DECISIONS_R1_DRAFT_v1, BATCH0 validation + Tranche-001 executable spec (coordination layer).

"""
i = s.find("## 10. Honest limits")
s2 = s[:i] + NEW + s[i:]
s2 = s2.replace("v0.3", "v0.4", 1)
(BASE / "FRAMEWORK_DRAFT_ORDERED_v0.4.md").write_text(s2, encoding="utf-8")
print("v0.4 written:", len(s2), "chars; v0.3 untouched")

entry = """
## Done (2026-07-10, pass 48 — research loop unit 4: FRAMEWORK PAPER v0.4; loop STOPPED)
- [x] [FRAMEWORK_DRAFT_ORDERED_v0.4.md](FRAMEWORK_DRAFT_ORDERED_v0.4.md) (v0.3 untouched): + Result 6 (F12c/F13/F14 with numbers and held-rows rationale), + global-register-as-comparator-column section (Peano lineage, provenance chain, three strata, v0.2/G-class/connective measurements, dominance+survivor-bias cautions, zonal-beats-attractor frame), + methods addendum (mutual-catch tally both directions, instrument-bias lesson), + consolidated-artifacts section.
- RESEARCH PROGRAM COMPLETE (units 1-4). LOOP STOPPED.
- OPEN ITEMS: fable/coordination-20260710 branch awaits user merge (Tranche 001 spec for Codex); held rows (ring, ręd, jednako, važiti) = external-authority packet, gated on the completeness bar; usage-conscious mode continues.
"""
with (BASE / "STATUS.md").open("a", encoding="utf-8") as f:
    f.write(entry)
print("STATUS pass 48 appended")
