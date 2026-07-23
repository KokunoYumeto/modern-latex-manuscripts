# Machine-readable internal references convention v2 — exhaustive

This convention supersedes v1 for final coverage claims. V1 remains preserved
as the historical initial specification.

## Outcome

Every source-visible locator that points to a destination present in the same
reader must retain exactly the same visible text while becoming a real PDF
link to a stable semantic target. The complete graph must also be recoverable
from rectangular UTF-8 CSV ledgers without parsing PDF geometry.

## Targets

- Assign each semantic destination a stable identifier qualified by work,
  exposé/volume, structural context, kind, and printed number.
- Cover numbered and explicitly cited chapters, sections, paragraphs,
  definitions, propositions, theorems, lemmas, corollaries, remarks, examples,
  equations/displays, figures, tables, appendices, and index destinations.
- Do not use PDF object numbers, source lines, hashes, mutable counters, or
  automatic Hyperref destination names as public semantic IDs.
- Preserve titles, numbers, equation tags, spacing, and prose exactly.
- Record every destination in `REFERENCE_TARGETS.csv`, including stable ID,
  LaTeX/PDF destination, work/exposé/context, kind, unchanged visible locator,
  source file/line, source coordinates when available, and compiled status.

## Edges

- Wrap only the exact pre-existing visible locator token; removing the wrapper
  must reconstruct the input TeX exactly.
- Candidate discovery is exhaustive, not cue-word-only. It must cover:
  named references; parenthesized locators; bare formula/statement numbers;
  range and list members; attached or separated Roman/alphabetic subitems;
  cross-exposé locators; abbreviated locators; references in headings,
  footnotes, captions, indexes, terminology tables, and backmatter.
- Absence of words such as “see”, “by”, or “equation” is not evidence that a
  target-bearing dotted number is a nonreference.
- Resolve by explicit scope, nearby scope, a table/index scope column, or a
  separately documented source-backed adjudication. Preserve any source
  numbering/kind slip visibly and ledger both literal and contextual readings.
- Leave external, unavailable, and genuinely unresolved tokens visibly
  untouched. They must still appear in `REFERENCE_CANDIDATES.csv` with exact
  evidence and a final disposition.
- Record each accepted edge in `REFERENCE_EDGES.csv` with stable edge ID,
  source location, exact visible token, reference form, scope, target stable
  ID/label, resolution basis, and compiled status.

## Exhaustive residual audit

After insertion, scan every included TeX dependency again for all locator-like
signatures. Every occurrence must be assigned exactly one final class:

1. linked internal edge;
2. structural declaration/tag;
3. external-work citation;
4. unavailable source target;
5. mathematical numeric expression;
6. typography/layout/geometry value;
7. other positively demonstrated nonreference.

There may be zero unadjudicated occurrences and zero unwrapped internally
resolvable locators. A generic `untriggered_numeric` or similar fallback is not
a final disposition. Every nonreference/external/unavailable row must be
positively checked, and an independent audit must sample or exhaustively
replay the residual classification. Dedicated parsers are required where
structure supplies scope, for example an exposé column beside terminology-index
section cells.

## Required validation gates

1. Stable target IDs and LaTeX labels are unique; every admitted target occurs
   exactly once and has a compiled PDF destination.
2. Every admitted edge points to one declared compiled target and produces a
   real internal PDF link annotation.
3. Candidate and residual ledgers contain no ambiguous, unresolved-adjudication,
   or internally resolvable unwrapped row.
4. Removing only inserted target/edge markup reconstructs every source
   dependency byte-for-byte (or decoded-text-exact where the frozen baseline
   uses a declared encoding).
5. The build converges with no undefined/multiply-defined reference, missing
   citation, rerun request, or fatal diagnostic.
6. Original internal/external links remain present. Link/destination counts and
   target/edge coverage are independently replayed against AUX/PDF structures.
7. Page count and continuous visible PDF content remain exact. Any page-flow or
   metadata-only variance is disclosed.
8. Fonts remain embedded/Unicode-capable as applicable. First, middle,
   transition, formula/diagram-heavy, changed, index, and terminal pages are
   rendered and visually checked.
9. CSVs are rectangular, unique-ID, reference-closed, and formula-safe.
10. A self-excluding exact checksum manifest replays every delivered artifact.

## Delivery

Deliver the reader source/PDF, target/edge/candidate/residual ledgers,
source-preservation proof, compiled/PDF validation, visual-QA receipt, and exact
checksum manifest together. Raw path-bearing logs remain internal unless
sanitized. State the precise scope of any non-goal backlog; an incomplete
backlog cannot coexist with an “exhaustive internal references” PASS.
