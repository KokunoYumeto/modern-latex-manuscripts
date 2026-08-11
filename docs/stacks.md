# Commons Stacks Layer

## Status and boundary

Mathematics Commons has adopted an independently governed architecture for a
Stacks-derived reference layer. The architecture checkpoint defines the interface and review
boundary only. It does **not** claim that an upstream repository, exact commit,
overlay tree, composed build, or modified edition has already been bound.

Upstream Stacks remains a respected source and synchronization target. Its
acceptance is not a dependency, approval gate, or veto over Commons editorial
work. Commons writes only to Commons-owned namespaces. An implementation must
bind the exact upstream repository, license, and commit before composing any
output; it must never edit another task's files or protected merge state.

## Five layers

1. **Pinned upstream mirror.** Keep one exact read-only upstream identity. The
   pin is the reproducible source baseline; floating upstream is only a sync
   locator.
2. **Commons overlay.** Put original additions, historical-source mappings,
   provenance, corrections, multilingual semantic links, stable Commons IDs,
   tests, and review receipts in a clearly renamed Commons namespace. Never
   present overlay material as upstream-authored or upstream-approved.
3. **Deterministic composition.** Build from one approved upstream pin plus one
   approved overlay commit. Record both inputs, the composition tool, generated
   members, bytes, hashes, tests, failures, and the resulting cursor.
4. **Optional modified edition.** A public modified edition is optional. If
   produced, it must follow the applicable GFDL obligations, use a distinct
   title, preserve attribution and license/history notices, and state plainly
   that upstream endorsement is not implied.
5. **Periodic upstream synchronization.** Review upstream movement against the
   last pin, import useful maintenance through an explicit sync commit, replay
   overlay tests, and preserve conflicts and rejected changes. Synchronization
   does not surrender Commons editorial control.

## Evidence boundary

The architectural handoff supplies only this public evidence about the prior
contribution route: PRs **#196** and **#197** were closed unmerged at the same
timestamp, with zero public comments and zero public reviews. The handoff did
not bind the repository containing those PR numbers. No motive, policy, or
private communication may be inferred from that evidence.

## Stable identities and review

Every overlay assertion should use a stable Commons ID and retain its upstream
locator, historical-source locator, provenance, correction history, language
relations, test result, and review receipt. Upstream IDs remain upstream IDs;
Commons IDs identify Commons overlay assertions and must not impersonate
official Stacks tags.

The layer belongs inside the Commons hardened-review network. A handback must
include exact upstream and overlay commits, deterministic build identities,
test and review results, conflicts, reversals, the next sync cursor, and an
explicit no-endorsement statement. The data model should remain exportable to
sTeX/MMT, Lean Blueprint, and formal-proof pipelines without making those
exports prerequisites for ordinary editorial work.

## First implementation cursor

Start with the dedicated
[Commons Stacks intake form](https://github.com/KokunoYumeto/modern-latex-manuscripts/issues/new?template=stacks.yml).
It keeps the ordinary adoption/handback lifecycle while requiring the exact
writer, upstream repository, license, commit, overlay namespace, deterministic
composition, tests, review plan, and synchronization cursor needed here.

The form fixes the Board ID to `stacks-commons-layer`. Choose the workflow that
matches the declared intent exactly:

| Intent | Required workflow |
|---|---|
| Bind the first exact upstream pin and Commons overlay | `upstream_overlay_sync` |
| Independently mirror or check an existing Commons overlay | `independent_review` |
| Propose a deterministic composition and test fixture | `assembly_review` |
| Return source or license evidence only | `source_intake` |

Parallel work remains welcome, but each Commons overlay namespace and its
ancestor/descendant chain has one writer identity at a time. Disjoint
namespaces—neither equal nor ancestor/descendant—may proceed independently.
The issue auditor requires each exact identity to occupy the whole submitted
field, rejects mixed repository revisions, and reads both executable identities
from the same human-approved commit as the board; local comparison is drift
detection, not the checker trust root.

1. Coordinate a single writer for the Commons namespace through that form.
2. Bind the upstream repository, applicable license, and one exact commit.
3. Create the first namespaced overlay manifest without copying mutable working
   state or changing upstream.
4. Define a deterministic composition command and a minimal regression fixture.
5. Return the exact pin, overlay, build, tests, review receipt, and next sync
   cursor through the existing Commons handback interface.

The machine-readable form of this architecture is embedded in
[`manifests/adopt.json`](../manifests/adopt.json) under
`stacks_reference_layer`; Board ID `stacks-commons-layer` carries the current
operational cursor. The current board transport, workflow contract, tests, and
anonymous public readback are bound in the adoption-v2
[closure](../manifests/published-github/adopt-v2-close.json) and
[source receipt](../manifests/published-github/adopt-v2.json). The dedicated
Stacks-intake [closure](../manifests/published-github/stacks-intake-close.json)
and [source receipt](../manifests/published-github/stacks-intake.json) remain
predecessor intake evidence. The preceding architecture generation remains bound in the
[Commons Stacks architecture closure](../manifests/published-github/stacks-r1-close.json)
and its [source receipt](../manifests/published-github/stacks-r1.json).
