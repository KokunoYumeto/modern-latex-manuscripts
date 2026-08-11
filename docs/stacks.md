# Commons Stacks Layer

## Status and boundary

Mathematics Commons has adopted an independently governed architecture for a
Stacks-derived reference layer. The official upstream reference is now pinned
read-only at commit `a04446e57ec1fbc252a871afcec7752fb2807b14`, tree
`3feeb703b931a6e7259782c10e7d1575adc83e5e`; exact repository, license-file,
and anonymous raw-readback evidence is bound in
[`manifests/stacks-pin.json`](../manifests/stacks-pin.json). This checkpoint
also binds an initialized [Commons overlay registry](../manifests/stacks-overlay.json)
with zero entries and a deterministic [composition contract](../manifests/stacks-compose.json)
whose preflight is blocked because no overlay exists. Those files are
control-plane infrastructure. This checkpoint still does **not** claim that an
upstream tree was copied into Commons or that a content-bearing Commons overlay,
composition run, composed build, or modified edition has been produced.

Upstream Stacks remains a respected source and synchronization target. Its
acceptance is not a dependency, approval gate, or veto over Commons editorial
work. Commons writes only to Commons-owned namespaces. An implementation must
replay the exact upstream repository, license identity, commit, and tree before
composing any output; it must never edit another task's files or protected
merge state.

## Five layers

1. **Pinned upstream mirror.** Keep one exact read-only upstream identity. The
   pin is the reproducible source baseline; floating upstream is only a sync
   locator.
2. **Commons overlay.** The registry exists with zero entries. Put original additions, historical-source mappings,
   provenance, corrections, multilingual semantic links, stable Commons IDs,
   tests, and review receipts in a clearly renamed Commons namespace. Never
   present overlay material as upstream-authored or upstream-approved.
3. **Deterministic composition.** The current preflight contract refuses to
   compose an empty registry. Build only from one approved upstream pin plus one
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
| Replay the exact upstream pin and bind the first Commons overlay | `upstream_overlay_sync` |
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
2. Replay the bound upstream repository, applicable license, commit, and tree.
3. Validate the existing zero-entry registry and blocked-preflight composition
   contract; do not create a parallel control plane.
4. Register the first provenance-complete namespaced overlay entry without
   copying mutable working state or changing upstream.
5. Bind an exact composition tool, execute the contract, and validate a minimal
   deterministic fixture.
6. Return the exact pin, overlay, build, tests, review receipt, and next sync
   cursor through the existing Commons handback interface.

The machine-readable form of this architecture is embedded in
[`manifests/adopt.json`](../manifests/adopt.json) under
`stacks_reference_layer`; Board ID `stacks-commons-layer` carries the current
operational cursor. The adoption-v3 pre-pin board transport, workflow contract,
tests, and anonymous public readback remain predecessor evidence in the
[closure](../manifests/published-github/adopt-v3-close.json) and
[source receipt](../manifests/published-github/adopt-v3.json); they do not bind
this later Stacks pin. The adoption-v2
[closure](../manifests/published-github/adopt-v2-close.json) and
[source receipt](../manifests/published-github/adopt-v2.json), plus the dedicated
Stacks-intake [closure](../manifests/published-github/stacks-intake-close.json)
and [source receipt](../manifests/published-github/stacks-intake.json) remain
predecessor intake evidence. The preceding architecture generation remains bound in the
[Commons Stacks architecture closure](../manifests/published-github/stacks-r1-close.json)
and its [source receipt](../manifests/published-github/stacks-r1.json).
