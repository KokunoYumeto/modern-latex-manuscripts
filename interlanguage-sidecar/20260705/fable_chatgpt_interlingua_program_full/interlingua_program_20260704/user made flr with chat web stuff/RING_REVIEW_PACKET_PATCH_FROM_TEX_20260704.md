# Ring review packet patch from Slavic TeX feed — 2026-07-04

Apply to `RING_REVIEW_PACKET_v0_20260704.md` before sending externally.

## Reason

The Slavic LaTeX feed shows that the current Interslavic corpus is not absolutely uniform on the ring term. It overwhelmingly uses `kolco` / `колцо`, but Paper 25 contains two `prsten` / `прстен` occurrences in the context of residue-class rings.

## Replacement wording

Use this wording in the one-page memo:

> The corpus overwhelmingly uses `kolco`/`колцо` and its compounds for algebraic ring terminology, with strong internal corpus pressure. However, the TeX feed contains a localized Paper 25 exception: `prsten`/`прстен` occurs twice in a passage where residue classes modulo a prime ideal are said to form a ring without zero divisors and are then extended to a residue-class field. This exception is not a verdict against `kolco`; it is evidence that the review question should explicitly include variant policy. The reviewer should decide whether the `prsten` trace is accidental inconsistency, an acceptable local doublet, or a sign that the ring-family surface should be reconsidered.

## Add reviewer question

> The corpus already contains a localized `prsten` occurrence in Paper 25. Should this be normalized back to `kolco`, preserved as a contextual doublet, or treated as evidence for a broader `kolco`/`prsten` variant policy?

## Boundaries

- This patch changes review framing only.
- It does not promote `prsten`.
- It does not demote `kolco`.
- It does not count generated Ukrainian/Russian translation files as independent native witnesses.
