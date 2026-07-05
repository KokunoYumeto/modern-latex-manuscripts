# Branch-Weighting Spec — witness concentration over a language-family tree
2026-07-04. Handoff artifact for the math-heavy lane (ChatGPT). Fable validated the framing as standard, not overreach: this is phylogenetics + information theory applied to the project's own voting-machine tradition. Label = **weighted rooted-tree witness measure** (NOT "weighted automata" — automata recognize/parse trees, wrong tool, would read as decorative overreach).

## 1. Object

A language family is a rooted tree `T`: root = family, internal nodes = clades (East/West/South Slavic; sub-branches), leaves = individual standard languages. For a term `t`, its **witness set** is the multiset of leaf languages whose native sources attest a form supporting the chosen bridge form.

**Witness mass on a clade** C for term t:
  m_C(t) = Σ_{leaf ℓ ∈ C} a_ℓ(t)
where a_ℓ(t) ≥ 0 is attestation weight of leaf ℓ (raw hit count, or capped/log-scaled).

The current flat witness vector W(t) = (E, W_S, S, I, X) is exactly `T` read at depth 1, with I (Interslavic-authority) and X (international/specialist) as **non-family** axes kept outside the tree.

## 2. Statistics (all computed in branch_weighting_v0.py)

Let the family-branch distribution be p_C(t) = m_C(t) / Σ_C m_C(t).

- **Effective number of branches** (Hill number of order 1):
  D(t) = exp(H(p)),  H(p) = −Σ_C p_C log p_C.
  D near 1 = monoculture; D near |branches| = balanced coverage.
- **Skew from target**: KL(p ‖ π), where π is the voting-machine target distribution (e.g. balanced π_C = 1/k, or population/branch-fairness weights). Divergence from the *intended* balance, not from uniform per se.

**Measured on the current pre-backfill corpus (1254 terms):** family mass E 2395 / W_S 64 / S 59 → p = (0.951, 0.025, 0.023); **D = 1.26 of 3**; KL-from-balanced = 0.87. Holds per rationale class (even "pan_slavic_native" terms: D ≈ 1.28). This is the monoculture as one scalar and is the headline number for CLM-DOM-001.

## 3. The part worth formal development (ChatGPT's lane): phylogenetic down-weighting

Raw counts overcount correlated evidence: two East-Slavic leaves are near-siblings, so a second Russian source is largely redundant with the first. The fix is standard in phylogenetics — **fair-proportion / equal-splits weighting** (Redundancy-aware leaf weights; cf. phylogenetic diversity, Faith's PD, ED "evolutionary distinctness"):

- Assign each leaf ℓ a weight w_ℓ = its equal-splits share of total tree length (each internal node splits its weight equally among descendant clades). Sibling leaves share weight; distinct branches keep theirs.
- Down-weighted witness mass: m̃_C(t) = Σ_{ℓ∈C} w_ℓ · 1[ℓ attests t] (or w_ℓ·f(a_ℓ)).
- Recompute D and KL on m̃. Under this weighting, a term witnessed by {ru, uk} scores far below one witnessed by {ru, cs, hr}, *automatically*.

**Why this matters for the program:** phylogenetic down-weighting IS the formal statement of the dominance-drift cure — "one more source from the dominant branch shouldn't move the needle." It converts HEU-NONDOM-001 and the MAG variance-penalty term into a single principled leaf-weighting. Open questions for the math lane:
1. Which tree/branch lengths? (glottochronology distances vs uniform topology vs learned distances from the ILO/embedding side — the two halves of the program meet here.)
2. Relationship between equal-splits leaf weights and the Interslavic voting-machine's subgroup votes — is the voting machine an implicit, coarse equal-splits scheme? (Plausible; worth proving or refuting.)
3. Interaction with the submodular benefit layer (CLM-MARG-001): is Σ_C (coverage of branch C) submodular under down-weighted masses? (Likely yes — coverage functions on weighted ground sets stay submodular.)

## 4. Boundary
- Family axes only (E/W_S/S and deeper); I/X axes are not tree branches and must not be folded into D.
- Current numbers are a **floor**: leaf-level attestation currently exists only for East (uk/ru columns); W/S mass comes from rationale mentions + the flagship shelf, so real W/S coverage after backfill can only rise. D=1.26 is the worst-case starting point, and the backfill diff (D before → after) is the measured result.
- Down-weighting is decision support for evidence balance, not a verdict on any language or term.
