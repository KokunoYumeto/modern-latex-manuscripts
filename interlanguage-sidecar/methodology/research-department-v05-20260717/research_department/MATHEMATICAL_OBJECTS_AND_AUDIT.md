# Mathematical objects and audit

Date: 2026-07-17

## Executive determination

The final research stack contains useful mathematics, but several packages use “automaton” loosely. The operative model is:

```text
typed evidence DAG for provenance and routing
        +
rooted family/cohort tree for dependence and breadth
        +
multi-objective constrained decision ledger
```

A formal weighted automaton is a possible implementation of extraction or routing, not the current linguistic evidence object merely by virtue of having weighted edges.

## 1. Typed evidence graph

The final State C v3 shape is:

```text
START -> SOURCE -> CONCEPT -> FORM
      -> SUPPORT | CANDIDATE | COMPETITOR | ADVERSE | GAP
      -> DECISION
```

This is valuable because it retains typed paths, provenance, and channel separation. It supports queries such as:

- Which source and language support this form?
- Is the evidence concept-shelf or row-verified?
- Which branch provides a competitor?
- Which gap is collection work rather than adverse evidence?
- Which decision is held for authority review?

The final v3 weights are raw branch masses or permitted-use values, not calibrated probabilities. The graph is therefore an evidence-routing serialization, not a probabilistic truth machine.

## 2. Formal weighted automata

A decision-grade claim that an object is a weighted automaton must state at least:

- a finite state set `Q`;
- an input alphabet `Σ` (or ranked alphabet for a tree automaton);
- initial and final weights/states;
- a transition relation or transition-weight function;
- a semiring `(K, +, ×, 0, 1)`;
- how path weights are multiplied and alternative paths summed;
- the recognized behavior or transduction;
- the interpretation of acceptance for this task.

The current packages name states and emit edges but do not define a meaningful input language or recognized behavior. They are automaton-shaped graphs. If a later extraction system consumes source tokens or document events and transduces them into typed evidence records, the weighted-transducer formalism becomes exact and useful.

Mohri’s finite-state work provides the relevant formal basis for weighted transducers in language and speech processing, and his semiring framework covers weighted directed-graph path algorithms. Those results validate the possible implementation class; they do not validate any linguistic score automatically.

## 3. Branch concentration

For declared nonnegative branch masses `m_i`, let:

`p_i = m_i / Σ_j m_j`.

The order-1 effective branch count is:

`D1 = exp(-Σ_i p_i ln p_i)`.

The order-2 count is:

`D2 = 1 / Σ_i p_i²`.

For a declared target distribution `π`, divergence is:

`KL(p || π) = Σ_i p_i ln(p_i / π_i)`.

When `π` is uniform over three branches, `KL = ln(3) - ln(D1)`. These are concentration statistics. They do not measure intelligibility, evidence quality, or correctness.

## 4. Dependence and family-tree coverage

Raw source counts overstate repeated evidence from related languages or duplicated corpora. Let `T` be a rooted family/cohort tree with nonnegative edge lengths `λ_e`, and let `A` be the set of witnessed leaves. Edge-coverage phylogenetic diversity is:

`PD_T(A) = Σ_e λ_e 1[Desc(e) ∩ A ≠ ∅]`.

The marginal value of adding leaf `l` is the total length of its still-uncovered root path. This captures the intended rule: adding another closely related witness usually buys less breadth than adding the first witness from an unrepresented branch.

The positive edge-coverage function is monotone submodular. This supports greedy prioritization of source acquisition under a stated budget. It does **not** make the full decision objective submodular: ambiguity, collisions, script confusion, and dominance constraints can interact and remain separate vetoes or penalties.

Faith-style phylogenetic diversity is total covered tree length. Fair-proportion and equal-splits indices are different leaf-allocation views; they can disagree. Use edge coverage for marginal source breadth and declared leaf weights only for a specified reporting or governance purpose.

The current `dependence_pd` sensitivity calculation is not yet a defensible governance model. It gives East one collapsed cohort while subdividing West and South, so a single East cohort covers less tree length than a single West/South subgroup. A production model must use symmetric resolution or explicitly justify unequal topology and branch lengths.

## 5. Candidate selection versus evidence concentration

Do not confuse two objectives:

- **Evidence concentration** asks how skewed the current support is.
- **Candidate/access selection** asks which intervention adds the most usable access under constraints.

For source or review prioritization, a positive maximum-coverage objective can be written:

`F(S) = Σ_u w_u max_{a in S} q_a(u)`,

where `u` is an access task and `a` is a candidate intervention. This benefit layer is a standard monotone submodular form. Adverse evidence, dominance, ambiguity, script failures, and governance rules remain constraints or vetoes.

Hill `D1` and KL never choose the best term. A perfectly balanced set of weak or false-sense hits is still bad evidence.

## 6. Reproduced State C results

The final v3 term ledger contains:

- 1,229 rows;
- 1,215 unique term IDs;
- 27 rows participating in 13 duplicated IDs;
- 100 concept buckets;
- 9,124 graph edges.

State C current snapshot:

| Quantity | Value |
| --- | ---: |
| East mass | 2341 |
| West mass | 223 |
| South mass | 239 |
| Total | 2803 |
| East share | 0.8351765965 |
| West share | 0.0795576168 |
| South share | 0.0852657867 |
| D1 | 1.7537043785 |
| KL to equal three-branch target | 0.5368819503 |

W0 filtered candidate projection:

| Quantity | Value |
| --- | ---: |
| East mass | 2341 |
| West mass | 333 |
| South mass | 348 |
| Total | 3022 |
| D1 | 1.993192 |
| KL to equal three-branch target | 0.408875 |

W0 is a projection only. It must not overwrite State C until its source-row context checks and writeback rules are applied.

Duplicate sensitivity is negligible at corpus level: collapsing repeated term IDs by maximum branch mass changes the snapshot approximately to `(2335,223,239)` and `D1≈1.75514`. That does not excuse the duplicate IDs; stable row identity remains mandatory.

## 7. Provenance audit of State C

The branch improvement is not uniformly row-verified:

| Provenance group | Rows | East | West | South |
| --- | ---: | ---: | ---: | ---: |
| `concept_shelf` writeback | 182 | 379 | 162 | 182 |
| blank/unwritten writeback level | 1,047 | 1962 | 61 | 57 |

This means most West/South gain is attributable to concept-shelf coverage. State C is the correct current serialized dataset, but its branch number must be described as a corpus evidence snapshot, not as fully row-verified attestation.

## 8. Rejected and withdrawn numbers

- Automaton v2’s `(2396,167,169), D1≈1.581` came from stale inputs and old ID joins. Keep its architecture, not its measurement.
- The claimed State D `D1≈2.62` mixed raw token counts with concept-language presence units. It is withdrawn.
- The honest 15-concept presence-unit comparison changes from `(30,41,39), D1≈2.974` to `(39,44,76), D1≈2.866`. More evidence reduced balance because South gained disproportionately. This is a useful warning that “more sources” and “more balance” are not synonyms.
- The early baseline `(2395,64,59)` recomputes to `D1=1.2572524318` and `KL=0.8696835584`. A `1.255` occurrence in framework v0.4 is a rounding/transcription error.

## 9. Unified v6.2 readiness audit

For every nonzero row, the package’s `readiness_proxy_0_100` is reproduced by:

`100 * support_candidate_mass / (support_candidate_mass + adverse_mass + 1)`.

This causes lanes with zero support and only candidates to score above 95. It also ignores gaps, evidence provenance, branch breadth, context review, script policy, external review, and human comprehension.

Disposition:

- Preserve it as archaeology under the accurate name `evidence_mass_saturation_proxy` if needed for debugging.
- Reject it as readiness, quality, correctness, or translation priority.
- Replace readiness with a vector of hard gates and unresolved conditions.

The unified graph also includes blank concepts, IDs, and policy sentences as concepts. It is suitable for routing and source discovery after cleaning, not as direct lexical authority.

## 10. Other current mathematical claims

| Object | Current status | Permitted use |
| --- | --- | --- |
| ILO / neighborhood overlap | Proposed, not run on this corpus | Experiment design |
| `FFRisk = FormSim × SemDist` | Testable proxy, not validated | Candidate risk ranking with human checks |
| Regularized family barycenter | Theoretical model | Comparative candidate generation |
| Persistent topology / cobordism | Proposed, currently unimplemented | Research only after explicit maps and predictions |
| Global-attractor root-prefix clustering | Exploratory mechanical proxy | Candidate discovery and comparison |
| History-class prediction | Weak; precision 0.41, recall 0.37 | Description only |
| Hill D1/D2 and KL | Established arithmetic | Evidence-concentration reporting |
| Edge-coverage PD | Established set function on a declared tree | Dependence-sensitive source breadth and prioritization |
| Human comprehension tests | Not yet run | Required outcome validation |

## 11. Minimum mathematical declaration per lane

Before reporting a weight or balance number, a lane must publish:

- evidence unit;
- included and excluded source classes;
- deduplication key;
- language/cohort/branch partition;
- tree topology and edge lengths, if used;
- target distribution and its governance rationale;
- saturation or dependence rule;
- channel treatment;
- provenance distribution;
- sensitivity analysis;
- exact formula and code version;
- known missing data;
- statement that the statistic does not certify intelligibility or correctness.

If those fields are absent, the number is exploratory by definition.

## 12. Primary mathematical and empirical anchors

- Mehryar Mohri, *Finite-State Transducers in Language and Speech Processing*: https://aclanthology.org/J97-2003/
- Mehryar Mohri, *Semiring Frameworks and Algorithms for Shortest-Distance Problems*: https://jalc.de/issues/2002/issue_7_3/abs-321.pdf
- Anne Chao, Chun-Huo Chiu, and Lou Jost, *Phylogenetic diversity measures based on Hill numbers*: https://pmc.ncbi.nlm.nih.gov/articles/PMC2982003/
- Daniel Faith, *Conservation evaluation and phylogenetic diversity*: https://ricottalab.com/wp-content/uploads/2015/10/faith-1992.pdf
- Kristina Wicke and Mike Steel, *Combinatorial properties of phylogenetic diversity indices*: https://arxiv.org/abs/1902.02463
- George Nemhauser and Laurence Wolsey, *Best Algorithms for Approximating the Maximum of a Submodular Set Function*: https://pubsonline.informs.org/doi/abs/10.1287/moor.3.3.177
- Charlotte Gooskens et al., *Mutual intelligibility between closely related languages in Europe*: https://research.rug.nl/en/publications/mutual-intelligibility-between-closely-related-language-in-europe/
- Charlotte Gooskens and Vincent van Heuven, *How well can intelligibility of closely related languages in Europe be predicted by linguistic and non-linguistic variables?*: https://research.rug.nl/nl/publications/how-well-can-intelligibility-of-closely-related-languages-in-euro/

These sources support the mathematical and measurement families. They do not validate this programme’s unpublished weights or linguistic decisions.
