# Adopt or Mirror a Work

This is the operational layer of the project: a board for adopting, mirroring,
checking, or extending a bounded author/work corpus. The existing archive maps,
source shelves, reader shelves, manifests, and receipts remain the authoritative
record of what bytes and claims already exist. This page does not replace them.

Use the [machine-readable board](../manifests/adopt.json) for automation or a
Mathematics Commons mirror. Use the
[adoption issue](https://github.com/KokunoYumeto/modern-latex-manuscripts/issues/new?template=adopt.yml)
to announce a scope, mirror, or result.

## Three Different States

| State | Meaning |
|---|---|
| **Current work** | A project lane is actively advancing the scope. Independent checking and declared parallel mirrors are welcome, but the row is not an unclaimed assignment. |
| **Ready for adoption** | Existing readers, sources, maps, or an exact continuation cursor make a bounded contribution possible now. No exclusive owner is asserted. |
| **Future** | The author or corpus is worth exposing, but the repository does not yet bind enough source/cursor evidence for a responsible production start. Source discovery or intake binding comes first. |

`Priority` measures likely mathematical/public value, not quality or prestige.
`Readiness` measures how directly a contributor can begin from current GitHub
evidence. Neither field certifies a translation or source edition.

## Current Work

| Scope | Maintained as | Existing surface | Parallel contribution |
|---|---|---|---|
| Emmy Noether multilingual papers | Kokuno Yumeto project lanes | [Language/work map](noether-map.md) | Review an existing language/work target, propagate a verified German correction, or mirror a bounded paper with exact inputs. |
| Grothendieck-school corpus: SGA, EGA, FGA, Verdier, Tôhoku, Illusie, and Deligne | Kokuno Yumeto project lanes; individual producer lanes retain their own publication custody | [EGA](ega-map.md), [FGA](fga-map.md), [Verdier](verdier-map.md), [Tôhoku](tohoku-map.md), [Illusie](illusie-map.md), [Deligne](deligne-map.md), and the preserved [SGA landing](records/sga.md) | Check a named page/range or build an explicitly independent mirror. Do not silently overwrite a producer generation. |
| Heinrich Weber, *Lehrbuch der Algebra* | Kokuno Yumeto project lanes | [Weber map](weber-map.md) | Continue the exact Volume II frontier or independently check a bounded existing section. |

The maintainer label describes current coordination, not ownership of the
underlying mathematics and not an exclusive reservation. Declared overlap is
useful when it creates an independent comparison rather than an untraceable
replacement.

## Ready for Adoption

| Priority | Author/work | Readiness | Bounded start |
|---|---|---|---|
| High | Carl Friedrich Gauss, *Werke* II | Exact cursor | Recover the registered continuation packet and continue after printed p.303, with p.305 next. Start at the [Gauss map](gauss-map.md). |
| High | James Joseph Sylvester, collected papers Volume I | Exact cursor | Continue at book p.494 from the [Sylvester map](sylvester-map.md). |
| High | Paul Gordan, *Vorlesungen über Invariantentheorie* I | Exact cursor | Continue after source p.28; retain the article-corpus register. See [known gaps](known-gaps.md#gordan--clebsch-gordan). |
| High | James Clerk Maxwell, *Treatise on Electricity and Magnetism* I | Exact cursor | Continue at printed p.80 from the existing p.1–79 sequence. See the [work queue](work-queue.md#highest-value-typesetting-and-source-check-work). |
| High | J. Willard Gibbs, *Scientific Papers* I, Paper 3 | Exact cursor | Continue after printed p.134 from the current source-witnessed sequence. See the [work queue](work-queue.md#highest-value-typesetting-and-source-check-work). |
| High | Arthur Cayley, collected papers | Repair-ready | Choose a small range, recover its source witness, and perform a page-level glyph/source audit before re-promotion. Start at the [Cayley map](cayley-map.md). |
| High | Erich Hecke, *Vorlesungen über die Theorie der algebraischen Zahlen* | Review-ready | Audit completeness, chapter/page resets, and publisher matter in the 184-page assembly. Start at the [additional-author map](cluster-map.md). |
| High | Wilhelm Killing, transformation groups | Expansion-ready | The current reader is only the twelve-page second part; bind the missing parts before building an author-level reader. Start at the [additional-author map](cluster-map.md). |
| High | Albert Einstein, *Annalen der Physik* contributions | Intake-ready | Bind the observed source-intake files to a work register, then choose one bounded paper. See the [source-intake note](../manifests/source-intake/20260623_math_annalen_90_96_and_os_sources.json). |
| Medium | Hermann Minkowski, collected works II | Review-ready | Check whether the selected-paper assembly represents the intended volume, then recover source/package closure. Start at the [additional-author map](cluster-map.md). |
| Medium | Felix Klein, collected works | Intake-ready | Turn the observed collected-works source intake into an exact volume/work register before transcription. See the [source-intake note](../manifests/source-intake/20260623_math_annalen_90_96_and_os_sources.json). |
| Medium | Adolf Hurwitz, mathematical works | Intake-ready | Bind the observed source material to an exact work register and select a bounded first paper. See the [source-intake note](../manifests/source-intake/20260623_math_annalen_90_96_and_os_sources.json). |
| Medium | Non-European mathematical texts | Review-ready | Check or assemble an existing direct/source-only language layer before starting any new translation. Start at the [exact map](non-european-map.md). |
| Medium | Ukrainian applied mathematics modules | Continuation-ready | Use the closed public driver and continue only the mapped partial modules. Start at the [exact map](ukrainian-map.md). |

## Future / Source Discovery First

| Priority | Author/work | Why it is not yet adoption-ready | First useful result |
|---|---|---|---|
| High | Sophus Lie, selected foundational works | No verified author/work source shelf or continuation cursor is currently bound by this board. | A bibliographic work register plus exact public source identities and one bounded pilot proposal. |
| Medium | Évariste Galois, *Oeuvres* and manuscripts | Source-intake packets are noted, but no promoted transcription or translation is bound as current. | Reconcile the printed and manuscript witnesses into a small, exact first-work intake. |
| Medium | Gotthold Eisenstein, *Mathematische Abhandlungen* | Source-intake packets exist without a promoted reader. | Select one work, bind the best source witness, and produce a reproducible page map. |
| Medium | Jakob Steiner, *Gesammelte Werke* | Volume-source intake exists without a promoted transcription or translation. | Bind Volume I/II witnesses and select one bounded paper or range. |

Future rows are invitations to prepare evidence, not claims that the corpus is
absent everywhere or that production should begin from an arbitrary web PDF.

## Mirror Workflow

1. Open the row's coverage map and source/reader roots. Do not infer absence
   from an unchecked label or missing cumulative PDF.
2. Choose a bounded author/work/range/language scope and record its exact
   starting cursor, input paths, hashes, and source authority.
3. Open one [adoption issue](https://github.com/KokunoYumeto/modern-latex-manuscripts/issues/new?template=adopt.yml)
   with the board ID and, if applicable, a mirror repository URL. This declares
   overlap; it does not reserve the work exclusively.
4. Preserve the source and predecessor generation. Add a new generation rather
   than overwriting contradictory or superseded evidence.
5. Produce a readable target plus editable source and a short manifest of
   paths, bytes, hashes, scope, status, and continuation cursor.
6. Run the checks appropriate to the claim: compile, source comparison,
   formula/diagram/table/reference checks, language review, and bounded visual
   inspection. Record failures and reversals as well as passes.
7. Compare with an independent mirror when one exists. Return exact corrections
   and reusable workflow findings; do not reduce disagreement to a winner label.
8. Submit a focused pull request or result issue. The archive map and this board
   are updated only when the corresponding bytes or exact external identity are
   inspectable.

## Machine Interface

The stable interface is
[`manifests/adopt.json`](../manifests/adopt.json), governed by the formal
[`adopt.schema.json`](../manifests/adopt.schema.json) contract and bounded
[`adopt.check.json`](../manifests/adopt.check.json) validation result. Its
`items` array defines:

- `id`, `author`, `work`, `series`, and `corpus`;
- `lane_state`, `coverage_state`, `adoption_status`, `priority`, and `readiness`;
- `owner`, `owner_scope`, and `languages`;
- `archive_path`, `related_paths`, and `source_basis`;
- `next_cursor`, `prerequisites`, `workflow`, and `claim_url`;
- `updated` and `notes`.

The top-level `mirrors` array records declared parallel work without forcing a
single exclusive owner. Each mirror row has `id`, `item_id`, `owner`, `scope`,
`url`, `status`, and `updated`. An empty array means no inspectable mirror has
yet been integrated into the board; it does not mean no one is working
elsewhere.

The stable raw endpoint for a Mathematics Commons consumer is:

<https://raw.githubusercontent.com/KokunoYumeto/modern-latex-manuscripts/main/manifests/adopt.json>

Schema and current validation endpoints:

- <https://raw.githubusercontent.com/KokunoYumeto/modern-latex-manuscripts/main/manifests/adopt.schema.json>
- <https://raw.githubusercontent.com/KokunoYumeto/modern-latex-manuscripts/main/manifests/adopt.check.json>

Consumers should treat `lane_state` as the top-level partition and use
`priority` only within a partition. Preserve unknown fields, accept additional
enum values, key rows by `id`, and never reinterpret the board as the archive
inventory. Follow `archive_path` for the authoritative coverage claim.
