# SGA 5 English publication readiness

Assessment updated: 2026-07-18, Europe/Berlin.

Decision: **NOT YET READY FOR PUBLIC HANDOFF.** The repaired scholarly and
technical body has passed its reopened source/build/render gates. Publication
remains held until the scan-free replacement is frozen, its exact manifests
are generated, and an independent package review passes.

## Gate table

| Requirement | Current evidence | State |
|---|---|---|
| Editable repaired English | `00_EDITION/SGA5_English_WorkingEdition_NotCritical_20260718.tex`, SHA-256 `5A795463...B7F4C4` | pass |
| Repaired reader | `00_EDITION/SGA5_English_WorkingEdition_NotCritical_20260718.pdf`, 309 pages, SHA-256 `0455F60C...721290` | pass |
| Printed-p.14 editorial disclosure | source adjudication, adverse ledger, extracted and rendered note | pass |
| Printed-p.43 ambiguity disclosure | source adjudication, adverse ledger, extracted and rendered note; glyph remains unresolved | pass with explicit open ambiguity |
| Two-pass build | reopened pass 1 and pass 2 logs, exit code 0 | pass |
| PDF metadata | nonblank Title, Author, Subject, Keywords | pass |
| Full render QA | private 309/309 page renders and four inspected overviews; bundled 16 sequential 8-bit-sRGB contact sheets and six focused renders | pass |
| Formula and structural comparison | final formula report and updated parity ledgers | pass for documented curated scope |
| French-control reconciliation | seven-file inventory plus contradiction report | pass as control reconciliation; no certification claim |
| Live Zenodo state | official API recheck of `21430393`, 17 files, `cc-zero` metadata | pass locally; requery before publication |
| Scan-free rights-attributed support | substantive 49-file pre-freeze stage passed two independent read-only audits; review/manifests added afterward | pass at member-tree stage |
| Payload-scoped member manifest | `MANIFEST.csv` plus self-excluding `SHA256SUMS.csv` | pass after generation; verify again after compression |
| Independent pre-freeze review | `INDEPENDENT_PREFREEZE_AUDIT.md`; exact snapshot 49/49 | pass |
| Final frozen ZIP/public-payload verification | required after manifests and ZIP construction | open |
| Archive-maintenance handoff | only after the preceding gates close | open |

## Scope and source basis

The candidate covers ten curated exposés— I, III, III B, V, VI, VII, VIII, X,
XII, and XV—plus a terminological index. Source synchronization used the pinned
French TeX, with the original LNM 589 scan at ambiguous/source-critical loci.
The French-control records conflict about their own audit completion; the exact
TeX is therefore pinned as a source-language control without adopting an
independent certification claim. External English translations are style and
terminology controls only.

The surviving printed-p.43 ambiguity is disclosed, not adjudicated by guess.
The printed-p.14 source defect is preserved visibly while its coherent reading
is explained in an editorial note. These are source-critical disclosures, not
silent rewrites.

## Rights and attribution

No repository-level grant was found that authorizes this task to redistribute
the Springer scan or that settles licensing for all underlying and derivative
materials. The replacement support payload must exclude:

- the original scan;
- every scan-derived image;
- the French TeX and reader;
- the inherited English witness;
- external English candidates;
- private local paths, task/thread identifiers, and unpublished internal
  correspondence.

The package may identify the original SGA 5 exposé authors/redactors and the
machine-assisted Codex/GitHub lineage without inventing a human translator.
Its rights file must state that no new copyright or open-license conclusion is
being made.

## Zenodo disposition

Use concept DOI `10.5281/zenodo.20410947`; do not mint a duplicate. The current
version observed at 2026-07-18T14:59:03Z is `10.5281/zenodo.21430393`. Its unchanged SGA 5 English PDF and
scan-bearing support ZIP would be superseded only after the repaired candidate
is verified and published by archive maintenance; no
remote change is authorized until archive maintenance receives and verifies
the exact frozen handoff. The API's `cc-zero` record metadata is not treated as
proof of rights in the bundled works.

## Permitted claim after a successful freeze audit

The strongest permitted public description is a **machine-assisted,
source-synchronized working English edition of ten curated SGA 5 exposés**, with
documented source decisions and rendered QA. It must not be called complete
SGA 5, certified, critical, independently human-reviewed, or rights-cleared.
