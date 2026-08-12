# Site Map

This page lists the main coordination documents in this repository and what each one is for.

## Start Here

| Page | Use It For |
|---|---|
| [Adoption and mirror board](adopt.md) | Exact claimable Board IDs; current, ready-for-adoption, and future author/work scopes; controlled coverage classes; start cursors; ownership labels; the exact workflow-selection rule; and the machine-readable Mathematics Commons interface. |
| [Browse index](browse-index.md) | Fast route to the right corpus or record. |
| [GitHub archive history](github-archive.md) | Exact repository catalog commit chain, manifests, and commit-pinned raw-readback receipts. |
| [Download guide](download-guide.md) | Deciding whether to open a reader PDF, artifact ZIP, manifest, or bulk record. |
| [By author and work](by-author-and-work.md) | Finding named authors and works without reading the full file catalog. |
| [Record landing pages](records/README.md) | Browsing each Zenodo record grouped by reader PDFs, artifact ZIPs, and status files. |
| [Live fleet map](live-fleet-map.md) | Current GitHub checkpoints, supplied external discovery identities, quality states, and continuation cursors. |
| [Historical project dashboard](project-status-dashboard.md) | Dated external-record counts and audit notes; not the current GitHub status surface. |

## Inventory

| Page | Use It For |
|---|---|
| [GitHub source-shelf index](../sources/README.md) | Browsing nineteen tracked author/corpus trees and replaying the exact 14,901-path / 3,681,880,509-byte Git-object inventory without using the external-record catalog as an intermediary. |
| [GitHub coverage-map index](github-maps.md) | One human route to all nineteen in-scope author, work, series, and mixed-corpus maps: 196,219 bytes with 643/643 local links resolved. |
| [GitHub reader-shelf index](../reader-pdfs/README.md) | Exact root-level inventory of 399 PDFs and three support files / 932,575,366 bytes, with tree hashes, duplicate state, and coverage-map routing. |
| [Ukrainian applied-mathematics GitHub map](ukrainian-map.md) | Exact reader/source identities, module coverage, duplicate and distinct PDF relations, TeX entrypoint closure, stale guide claims, and structural gaps. |
| [Non-European mathematics GitHub map](non-european-map.md) | Exact Chinese, Indian/Sanskrit, Islamic/Arabic, and reference-work language layers, current direct-reader identities, source-only translations, repair generations, and custody gaps. |
| [Classical mixed-shelf GitHub map](classical-map.md) | Exact Cayley, Dedekind, and Dirichlet partition; 21 reader identities, source/history generations, duplicate relations, stale author claims, and quality routing. |
| [Additional-author GitHub map](cluster-map.md) | Exact Minkowski, Hecke, Landau, Steinitz, Hensel, Oka, Hausdorff, Grassmann, and Killing readers; legacy relations, structural checks, stale reports, and missing source/package custody. |
| [Public file catalog](public-file-catalog.md) | Dated searchable external-record file snapshot; use current maps and receipts for live heads. |
| [Producer-reported external records](zenodo-records.md) | Dated external discovery/provenance history; not a live GitHub queue or universal current-head index. |
| [Pending Zenodo uploads](pending-zenodo-uploads.md) | Historical extracted/checksummed package ledger; not the current action queue. |
| [Known gaps](known-gaps.md) | Current incompleteness and caveats by corpus. |
| [Work queue](work-queue.md) | Historical producer/evidence context plus GitHub-scoped work leads; use the adoption board for current assignments. |
| [Author page candidates](author-page-candidates.md) | Human-readable triage for deciding when a mixed shelf should become a dedicated Zenodo author/topic record. |
| [Interlanguage source-body side branch inventory](interlanguage-source-body-sidebranch-20260707.md) | Historical map of the raw source-body/provenance side branch; grouped payloads are preserved in interlanguage version [10.5281/zenodo.21430885](https://doi.org/10.5281/zenodo.21430885). For the current interlanguage methodology head, use [10.5281/zenodo.21788322](https://doi.org/10.5281/zenodo.21788322). |

## Method And Quality

| Page | Use It For |
|---|---|
| [Workflow notes](workflow.md) | Provenance model, file roles, and review loop. |
| [Quality rubric](quality-rubric.md) | How to interpret draft status and audit claims. |
| [Release checklist](release-checklist.md) | Pre-publication and post-publication hygiene for Zenodo records. |

## Contribution

| Page | Use It For |
|---|---|
| [Adoption and mirror board](adopt.md) | Announcing a bounded adoption, independent mirror, source intake, or returned result without claiming exclusive ownership. |
| [Contributing guide](../CONTRIBUTING.md) | How to report corrections or make narrow pull requests. |
| [Issue templates](../.github/ISSUE_TEMPLATE) | Structured correction and source-suggestion reports. |
| [Pull request template](../.github/pull_request_template.md) | Checklist for changes. |

## Machine-Readable Manifests

| File | Use It For |
|---|---|
| [Adoption board JSON](../manifests/adopt.json) | Stable operational feed for Mathematics Commons consumers; rows are keyed by `id`, expose current/adoptable/future state, and link back to authoritative archive maps. |
| [Adoption schema](../manifests/adopt.schema.json), [validation](../manifests/adopt.check.json), and [consumer](../scripts/get-adopt.py) | Formal item/mirror and same-commit snapshot contract; a fail-closed exact-commit consumer; and bounded replay of IDs, states, queues, tracked paths, and all 19 maps. Floating `main` is only a locator. |
| [Public file catalog CSV](../manifests/public-file-catalog.csv) | Structured external-record inventory at its recorded generation. |
| [Zenodo records JSON](../manifests/zenodo-records-current.json) | Structured external-record map at its recorded generation. |
| [Status snapshot](../manifests/current-status.md) | Compact generated historical status summary. |
| [Public surface audit](../manifests/zenodo-public-surface-audit.md) | Readability/PDF-surface audit at its recorded generation. |
