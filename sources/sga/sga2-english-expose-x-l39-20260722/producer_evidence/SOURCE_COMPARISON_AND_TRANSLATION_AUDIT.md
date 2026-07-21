# SGA2 Expose X - Lemma 3.9 statement

Status: `producer_pass_pending_independent_review`. This is a
no-overwrite bounded successor, not a seal, public payload, or archive
handoff.

## Authority, scope, and coordinates

- Sole textual authority: corrected arXiv French TeX
  `smf_doc-math_4_01.tex`, 586,789 bytes, SHA-256
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Exact scope: French lines 3544--3553 inclusive, SHA-256
  `1938246ACBCA9D6DBE4F16CDFD933184C8005562DACE517CBD982098629F0231`.
- Structural unit: Expose X, Lemma 3.9 statement, two enumerated items and
  one numbered editor's note.
- Locators: original printed page 120; same-edition PDF physical page 104;
  recomposed running page 96.
- Excluded before: transition line 3542 and blank line 3543.
- Excluded after: blank line 3554 and proof from line 3555.
- Raw cursor: 3554. Next substantive cursor: 3555.
- French authority bytes are unchanged.

The 216-page same-edition reader, SHA-256
`41AD02C57321A8D2200FF32A929BC93ADBC3DE0D59DCD5A284D28D859FB87A90`,
is manifestation and layout evidence only. Its agreement is not independent
original-print corroboration. The current jcreinhold `e7a259f` Markdown,
SHA-256
`2BDDBC3D15EECE7A47FDBDFBE31DAE735446BC14480A75113E704F63901C7BF5`,
is one LLM-generated comparison lineage and is not an authority.

## Source structure and target policy

The target preserves the lemma number, local noetherian ring hypothesis,
the condition that `t` lie in the radical and be `A`-regular, `t`-adic
completeness, the regular-local-quotient hypothesis and its parenthetical,
the definition `B=A/tA`, both numbered items, every prime/dimension/depth
condition, both purity implications, and editor's note (5). `prof` is
rendered as the standard English mathematical operator `depth`, consistently
with the immediately preceding Corollary 3.8 unit; no inequality or subscript
changes. `lorsque` is rendered as `whenever` in the two quantified
conditions. The French implication phrasing `pur entraine` is expanded to
ordinary English implication phrasing without changing logical direction.

Rejected choices are recorded rather than silently disappearing: retaining
the French operator label `prof` in English; changing `noetherian` to British
capitalization or spelling variants; treating `pur` as `normal`; omitting
the parenthetical complete-ring example; collapsing the two numbered items;
or moving editor's note (5) away from the third hypothesis.

## Line 3551 adjudicated source defect

Final decision
`EG-SGA2-X-L3551-MISSING-EST-SOURCE-DEFECT-ADJUDICATION-20260722-0001`
assigns stable ID `SGA2-X-L3551-MISSING-EST-SRCDEF-001`. The durable control
is 2,426 bytes, SHA-256
`D70AACF890B5CDA27AE29B2E6877094CC3B5689CF4EEF93A7C135EA2EE8D547B`.
French line 3551 reads `si $A_\pp$ pur lorsque $t\notin\pp$`, omitting the
finite copula `est`. The line is 366 bytes without EOL, SHA-256
`D1F96292E7D0962E92CC4E7C487CE7E7ACE7AF462AECB3AB88E6CCD00A10AD04`,
and 367 bytes with LF, SHA-256
`8A0D1B4E1E4A57424A70FDF8F875A9B6064BF71ABC24844F8E94E59BCFAA5321`.

The target therefore says `if A_p is pure whenever t is not in p` and
places an immediate visible stable-ID source note inside item (ii). The
provisional candidate
`SGA2-X-L3551-MISSING-EST-SRCCAND-001@1` is preserved append-only and
superseded by the final stable ID. The current French branch already emits
the later `si` before the depth-at-least-three condition; no second missing
`si` is diagnosed or supplied.

## Gate

The producer froze exact source/comparison/adjudication slices, built three
deterministic clean passes, rendered and inspected the target page plus
source physical page 104, validated the 26-column CSV and structured JSONL
including revision/reference closure, and ran Artifact Tool full-table
inspection and panel rendering. Privacy, rights, and exact-manifest gates are
bound in separate machine receipts. A fresh independent review is still
required before any seal, cumulative inclusion, or archive handoff.
