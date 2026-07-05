# Noether Source-Canon Sufficiency Transition: Interlanguage Integration

Recorded UTC: 2026-07-05T13:36:26Z

Lane: Session D - interlanguage method and authority

Status: research-only method/authority integration of the GitHub-visible source-canon sufficiency transition rule.

## Inputs Reread

- `AGENTS.md` at commit `b99286628344251e860fe889e44cc54c8ebd6f87`: SHA-256 `E4E6A7422E118543E5ADAB00ACFB32E8C097FE6F40153745A9E5D9CCAF0DCE6B`, bytes `8348`
- `.github/copilot-instructions.md`: SHA-256 `D553C306879C915C9B0132E6DF50F010FE8F9ADC9EB130C9295BC4DF9DBD50FF`, bytes `2898`
- `NOETHER_SOURCE_CANON_SUFFICIENCY_TRANSLATION_TRANSITION_20260705.md`: SHA-256 `A6504AFF333D3B58866F19D95A39BE171F67002952A566A13BDDE8C25A0C0EA2`, bytes `1781`
- Parent consolidation ledger SHA-256 `F4DED0B55E54DC870E5D23831216CD73D99E0102CB383F50D7F91E68C86EC4F2`, bytes `526768`
- B3 steward log SHA-256 `6282D73534EEB7D3BF64EDEC58FEBC12D9703B9AB4978646E9AEEC1DD70D689C`, bytes `416852`
- Session D durable log before this transition packet SHA-256 `6564E4855170DAC3549D1DFCCA479D603335BF77AA06F24092CD4D5AD095CE1F`, bytes `160851`

## Controlling Interpretation

Source canon remains first. However, source-canon-first is no longer an indefinite hold when a lane has adequate baseline witnesses for a scoped language/topic row set. Once a lane has sufficient baseline evidence for covered rows, it must begin draft translation review work for those covered rows.

Session D does not decide that a language community has accepted a rendering, and does not certify native review. Session D's role is to provide routing, governance, sufficiency checks, interlanguage scaffolding templates, and authority boundaries so owner lanes can begin scoped draft work where their source rows are sufficient.

## Sufficiency Decision Matrix

| Row state | Required action | Translation status | Source-canon status |
| --- | --- | --- | --- |
| Sufficient baseline | Start scoped draft translation for covered rows. | Draft, non-canonical, not native reviewed. | Witnesses have language/topic coverage, URLs, hashes, license/access signals, source-owner notes, and no package-safety blocker. |
| Partial baseline | Translate only covered rows; leave uncovered rows as gaps. | Mixed: covered rows draft, uncovered rows no translation. | Gaps and weak witnesses are explicit. |
| Source-body or package-safety blocker | Do not translate blocked rows. | Blocked/gap only. | Resolve raw-source-body, credential, OCR-cache, zip-primary, or upload-policy blocker first. |
| Weak or off-topic evidence | Do not treat as sufficient. | Gap/provenance only. | Continue source acquisition and mark weak witness status. |

## Draft Translation Packet Template

Each language lane with sufficient baseline should create a row-scoped draft packet with these fields:

| Field | Requirement |
| --- | --- |
| `source_row_id` | Stable row or witness identifier from the lane source-canon table. |
| `language_topic_scope` | Target language, mathematical topic, register, and covered source rows. |
| `source_witnesses` | URLs, local paths, byte counts, hashes, license/access signals, source-owner notes, and upload policy. |
| `coverage_status` | `covered`, `partial`, `gap`, or `blocked`; do not hide weak witnesses. |
| `target_renderings` | Draft target-language renderings for covered rows only. |
| `source_context_notes` | Notes from the source witness context, including register and neighboring terminology. |
| `term_alternatives` | Alternatives with register/source evidence; no accepted-term claim. |
| `formula_neighboring_usage` | How the term appears near formulas, definitions, examples, theorem statements, or notation. |
| `interlanguage_scaffold` | Optional interlinear or semi-constructed linguistic scaffold for comparison across registers. It is a comparison aid only, not an approved bridge form. |
| `uncovered_rows` | Explicit gap/source-acquisition tasks for rows outside the sufficient baseline. |
| `review_boundary` | Draft, non-canonical, not native reviewed, no gate promotion, no blanket license clearance, no completion claim. |

## Interlanguage Scaffold Boundary

Interlinear or semi-constructed interlanguage scaffolds may be used when they help compare source registers across languages. They must be labeled as scaffolds and must not be promoted as accepted bridge surfaces, canonical terminology, or community-approved forms.

Recommended scaffold fields:

- source token or phrase;
- literal gloss;
- target-language draft rendering;
- term alternatives;
- formula-neighboring context;
- morphology or register note;
- uncertainty/gap note;
- source witness row and hash;
- reviewer needed, if any.

## Owner-Lane Routing Notes

- Language lanes own target renderings. Session D owns method, sufficiency routing, authority boundaries, and scaffold templates.
- Covered rows with sufficient baseline should move from source-acquisition-only to scoped draft translation.
- Uncovered rows remain source-acquisition or gap rows.
- Rows with raw-source-body, OCR-cache, credential, zip-primary, upload-policy, or package-safety blockers remain blocked until the owner lane and B3 resolve them.
- B3/package steward stages, commits, pushes, and handles publication drift. Language lanes and Session D do not push.

## Decision Record

`D-SUFFICIENCY-TRANSITION-001`: Adopt the GitHub-visible source-canon sufficiency rule for Session D method and authority work.

Decision:

- Preserve source-canon-first as a gate.
- Require scoped draft translation for rows whose owner lane has sufficient baseline evidence.
- Keep uncovered or blocked rows in source-acquisition/gap status.
- Permit interlinear or semi-constructed interlanguage scaffolds only as clearly labeled comparison aids.
- Preserve draft/non-canonical/not-native-reviewed/no-completion/no-gate-promotion labels.

## Boundary

This integration packet does not approve source reuse, translation, bridge surfaces, terminology, native review, community or project consent, source-license clearance, payload eligibility, pilot readiness, gate promotion, or completion.

## Continuation

Next Session D pass should verify whether this transition integration packet, JSON, sidecar, and durable-log append become package-visible. Child lanes should use this packet to decide whether each row remains source-acquisition/gap/blocked or moves into covered-row draft translation.
