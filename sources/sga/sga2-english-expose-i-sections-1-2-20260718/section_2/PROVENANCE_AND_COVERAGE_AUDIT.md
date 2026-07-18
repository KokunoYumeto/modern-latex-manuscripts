# Recovered SGA 2 English witness: provenance and coverage audit

Audit date: 2026-07-18

## Authority boundary

The recovered English comparison-witness files listed below are controls
only. They are not the translation authority and are not promoted into the
new English workpass. This disposition does not apply to the separately
authored source-aligned target TeX/PDF. The controlling source is the
corrected/annotated French TeX in arXiv:math/0511279v1. The local French PDF
is used to verify rendering and printed-page coordinates.

## Recovered editable witnesses

| Local copy | Bytes | SHA-256 | Relationship |
|---|---:|---|---|
| candidate_A_source_intake.md | 680137 | AD6CBBBEC3CDDCC00F7EB2328EBC09F9C00F6C24181E1D02098B437D22C26A70 | CRLF/source-intake copy |
| candidate_B_batch_current.md | 666110 | 9B338AA5859B13572C34A5FBDFB4BAE2F15D2A4D875831B769F0F13BC6DF4446 | LF/batch copy |
| candidate_A_source_intake.tex | 680918 | B79B5087F440E274845EDB3460585D23B5D450F43A6F0049020431DCAD1A8EB7 | pandoc-style TeX export |
| candidate_B_batch_current.tex | 663440 | D9C421467C999CF47C29BA4DB0ED05429B97B152BF47D473AB41C629E5247E77 | LF/batch TeX export |
| candidate_A_source_intake_mathfixed.tex | 681257 | 4B28F188F22D33F9B1B14641E02A3100216E38CE61CB97D8A5D8F5536CB30470 | rendering-repair derivative |
| candidate_B_batch_mathfixed.tex | 663768 | 43C029D259CB3FA112DF469B9C8FCCEFFAA287A745518E90F0F0565B57FD3494 | rendering-repair derivative |
| candidate_B_batch_mathfixed.pdf | 857517 | EC6A727DA8E6D02BDA7E9B6A37089E41F3FEC45F8C80EAA8E7AD4E748708FB54 | 211-page control PDF |

The A and B Markdown bodies are semantically identical in a no-index Git
comparison except for one provenance sentence:

- A says “included in the source package packet”;
- B says “included in the handoff packet.”

The large byte difference is line-ending representation, not added
mathematical content. The same distinction propagates into the TeX exports.

## Self-declared provenance

Every recovered body begins with the warning:

“Consolidated from the jcreinhold LLM-generated Markdown snapshot … Not
mathematically proofed in this batch.”

No recovered local file names a model, prompt, source commit, or completed
mathematical review. The inherited name “jcreinhold” was initially only a
locator; the audit subsequently resolved it against the public primary
repository described below.

## Verified editable origin and exact lineage

The editable public origin is Jacob Reinhold's repository
`https://github.com/jcreinhold/sga`, described by its maintainer as an
English LLM-based translation of SGA. The recovered SGA 2 body pins to:

- commit: `069f3b6f7cc4c9c1001d0c2799d3e7c5cbd93c09`;
- commit date: 2026-05-22T11:51:51Z;
- immutable volume tree:
  `https://github.com/jcreinhold/sga/tree/069f3b6f7cc4c9c1001d0c2799d3e7c5cbd93c09/ii`;
- volume README:
  `https://github.com/jcreinhold/sga/blob/069f3b6f7cc4c9c1001d0c2799d3e7c5cbd93c09/ii/README.md`.

Lineage was tested rather than inferred. The local source-intake Markdown was
split at its 20 `SOURCE` markers, CRLF was normalized to LF, and each segment
was compared with the corresponding raw file in the immutable upstream tree:
20 of 20 units were byte-exact. Candidate B contains the same complete body;
A and B differ only in line endings and one wrapper phrase. They are packaging
variants of one witness, not two independent translations. The local TeX and
PDF files are Pandoc/conversion derivatives of that Markdown.

## License and attribution

The pinned upstream README and license identify the English translation as
copyright 2026 Jacob Reinhold and license it under CC BY 4.0:
`https://github.com/jcreinhold/sga/blob/069f3b6f7cc4c9c1001d0c2799d3e7c5cbd93c09/LICENSE`.
Attribution and an indication of changes are therefore required wherever the
recovered English contribution is reused. It must not be relabeled CC0. This
license concerns Reinhold's English expressive contribution; it does not by
itself establish a license for the underlying French source.

## Structural coverage

The Markdown control contains:

- an Introduction;
- Exposés I through XIV;
- a glossary/translation ledger;
- an index of notation;
- a terminological index.

The upstream unit count is 20: two front-matter files, fourteen Exposé files,
a README, glossary, notation index, and terminological index. The local
headings match all fourteen French chapter headings and all 45 numbered
French section headings. This is broad full-volume structural coverage, not
proof of sentence, formula, diagram, footnote, bibliography, or
correction-branch parity.

The Markdown has 553 explicit label comments, 29 translator-note blocks, and
307 page comments representing 261 distinct numeric values. The locator
sequence is not a certified page ledger: 35 numeric values repeat and 23
values from 1 through 284 are absent. That does not by itself prove omitted
prose, but it prevents page comments from proving complete alignment. The
211-page rendered control is correspondingly a visual/control artifact, not
a translation substrate.

## Upstream status and known caveats

The pinned README calls the work idiomatic and LLM-generated, describes it as
a translation rather than a critical edition, and makes the 2005 French TeX
the authority for mathematically material claims. The local wrapper adds
“Not mathematically proofed in this batch.” Embedded notes preserve further
warnings, including inferred alterations in Exposé VII and opaque or
apparently malformed source readings in Exposés VI--VII. These admissions are
useful review locators; they are not corrections until source-audited.

At audit time, upstream head was
`e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` (2026-07-10), fifteen commits
ahead of the pinned snapshot. GitHub reports changes in 19 of 20 SGA 2 units:
`https://github.com/jcreinhold/sga/compare/069f3b6f7cc4c9c1001d0c2799d3e7c5cbd93c09...e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e`.
Those changes have not been source-audited as merely cosmetic. Current
upstream therefore remains a newer comparison candidate, never the French
translation authority.

A later public mirror retains an SGA 2 English PDF whose extracted first page
omits the visible LLM/not-proofed warning. It is not byte-identical to the
recovered local PDF and must not be treated as a source-checked replacement.

## Demonstrated adverse findings in Exposé I §1

The first audited unit already proves that the witness cannot be silently
promoted:

- it repeatedly renders inverse-image stars as plain text, for example i*
  instead of i^*;
- it renders j^*(G) and k^*(G) as j*(G) and k*(G);
- it replaces the source’s underlined sheaf functors with ambiguous
  plain/calligraphic approximations;
- it says “replace Z by Z''” where the French source says replace Z' by Z'';
- it renumbers source equation labels in its Markdown metadata;
- it uses awkward literal phrasing such as “closed part” and capitalized
  “Modules.”

These are recorded in the normalization/adverse-delta ledger. The recovered
witness may suggest English phrasing, but every accepted sentence and every
symbol must be checked independently against the French authority.

## Further adverse findings in Exposé I §2

The second audited unit confirms the same control-only disposition:

- it replaces source-underlined sheaf-valued H, Gamma, Ext, and T functors
  with calligraphic or undecorated approximations;
- it drops the superscript star from the inverse-image functors `i^*` and
  `f^*`;
- it drops both closure bars in Remarks 2.7, thereby changing the support
  locus;
- it rewrites printed equation and statement locators into its own metadata
  scheme;
- it silently propagates or repairs several French-source anomalies instead
  of exposing the editorial decision; and
- it changes the source's `R^n` to blackboard-bold R without a recorded
  source or target reason.

The source-aligned target instead preserves the corrected French branches and
printed locators, and records four narrowly supported source emendations in
visible notes and the adverse-delta ledger.

## Audit disposition

Disposition: control-only, not public payload, not source-certified.

Permitted uses:

- locate corresponding prose;
- compare possible English wording;
- identify terminology choices and likely error classes;
- support adverse-delta analysis.

Prohibited uses:

- copying the PDF as a translation substrate;
- inferring source fidelity from broad structural coverage;
- dropping Jacob Reinhold's CC BY attribution/change notice where inherited
  English expression is reused;
- describing the complete witness as proofed, certified, source-faithful, or
  publication-ready.
