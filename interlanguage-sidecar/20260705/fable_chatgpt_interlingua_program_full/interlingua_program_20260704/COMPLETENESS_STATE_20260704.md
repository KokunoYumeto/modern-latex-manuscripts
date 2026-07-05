# Completeness State — end of insertion sprint 1
2026-07-04. The bar (Floris): full canonical-corpus insertion of all the words, correctly weighted. This summarizes where that stands after 24 insertion passes (mine) + 3 grind passes (ChatGPT web), all same-day.

## The numbers

| Metric | Session start | Now |
| --- | --- | --- |
| Token coverage (ISV Latin corpus, 265 dedup files, 142K content tokens) | 70.6% (naive baseline: 39.6%/65.2% before tooling fixes) | **93.8%** |
| Type coverage (11,907 content types) | 39.6% | **68.6%** |
| Proof-prose lexicon | 0 | **230 lemma groups** (~950 variant surfaces) |
| Uncovered types remaining | ~6,700 | **~3,700** (frequency ≤10 each; long tail) |

ChatGPT's parallel measurement (stricter 222-file set, artifact-excluded denominator): 91.31% tokens / 54.88% types after its v2 delta — two implementations agree within noise.

## The lexicon (data/proof_prose_lexicon_v2.json)
230 groups: proof_grammar 31, proof_operation 25, proof_predicate 24, math_general 21, adverbs/connectives/sequence/reference ~57, curriculum 8, rest mixed. Provenance: ChatGPT 61 groups + 320 delta types; Fable ~169 groups across passes 1–23; every entry `needs linguistic review`, permitted-use 0.35. **67 groups carry ≥4 variants — the F13 variant-scatter ledger in embryo**: each is a normalization decision (preferred surface + variant policy) awaiting the review layer.

## What the grind found beyond coverage (paper-relevant)
- F13: pervasive register-layer variant scatter (obće/obču/vobče/voobče; mora/musi; togda/tada; imenno/namreč; pytanje/vprašanje; slučaj/slućaj; odnovrěmenno/istočasno/odnovočasno…).
- F12b: connective layer is the most branch-divergent stratum (5/6 core connectives West-competitor-only).
- Held-word discipline paid: dělo=paper-header, vaga=weight-of-form (real Noether-stratum term), oběh=genitive dual — three would-be misclassifications avoided by context checks.
- Tooling hardened by the grind itself: č-class tokenizer fix, NFC order, inflection stems, eponym-stem rule, TeX-artifact exclusion (ChatGPT), preamble/env/option stripping.

## The strategy fork (needs Floris)
Per-pass deltas are now 0.1–0.3% tokens; front words occur ≤10 times each. Four ways to spend the next passes:
**(a)** keep token-grinding to ~95%+ (mechanical, diminishing);
**(b)** pivot to TYPE-ranked fronts — the lexicographic completeness the bar actually names (types 68.6% → the real distance);
**(c)** pivot to the WEIGHTING half of the bar: branch-evidence pass over all 230 lexicon groups (register W/S probes like the 6-row pilot, marker-table weight columns, normalization proposals per scatter group);
**(d)** split: hand the token long-tail to ChatGPT's backlog loop (its top-1500 queue is built for exactly this) and I take (c).
My recommendation as the working scholar: **(d)** — the tail is mechanical and ChatGPT's loop eats it well; the weighting/normalization layer is where "correctly weighted" gets earned and where review-facing value concentrates.
