# Branch-weighted witness trees — spec for hard-math development
2026-07-04, Fable → ChatGPT handoff. Origin: Floris's heuristic "weighted automata / branch-following tree thing: how heavy are we in language branch X/Y/Z per term?" Fable's validation: the idea is sound; the right formal object is a **weighting scheme on the rooted family tree + concentration statistics**, not tree automata (automata recognize/score tree-structured inputs; nothing here is a parse tree — using that label would be decorative math).

## What is already implemented and measured (v0)

Data: 1254 Interslavic term rows, each with witness vector over depth-1 Slavic clades (E = East, W = West, S = South; Interslavic-authority I and international X kept off-tree).

- Branch mass m_C = Σ_terms witness weight under clade C. Measured: E 2395, W 64, S 59 (95.1% East).
- Effective number of branches = exp(Shannon entropy of normalized branch masses) — a Hill number D₁. **Measured: 1.257 of max 3.**
- KL(observed ‖ balanced target) = 0.87 nats.
- Per-reason-class slice: terms with rationale "pan_slavic_native" measure eff = 1.28 — nearly as East-concentrated as unstated ones. Claimed breadth ≠ witnessed breadth, quantified.
- Artifacts: branch_weighting_v0_20260704.json; scripts/branch_weighting_v0.py; inputs hash-pinned upstream.

## What we want ChatGPT to develop rigorously

1. **Phylogenetic down-weighting.** Sibling languages give correlated evidence: a second East-Slavic witness should add less than a first West-Slavic one. Candidate schemes from phylogenetics: equal-splits, fair-proportion ("evolutionary distinctiveness"). Task: pick/derive the scheme appropriate for witness *evidence weighting* (not conservation ranking), state its axioms, and give the update rule for witness value as a function of tree position of already-present witnesses. This is the formal core of dominance-penalty: "one more Russian source doesn't help."
2. **Deeper tree.** Extend from depth-1 (E/W/S) to the standard Slavic tree (E: uk/ru/be; W: pl/cs/sk/hsb-dsb; S-West: sl/hr/sr/bs; S-East: bg/mk). Define branch-mass and D₁/D₂ (Hill numbers) at every internal node; report a concentration profile per depth, not one number.
3. **Target distribution.** The Interslavic voting machine's 6 subgroups with split votes IS a discrete target distribution π over the tree. Task: state the voting machine as the special case of branch-weighted aggregation it is