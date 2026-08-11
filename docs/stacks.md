# Commons Stacks Layer

## Status and boundary

Mathematics Commons has adopted an independently governed architecture for a
Stacks-derived reference layer. The official upstream reference is now pinned
read-only at commit `a04446e57ec1fbc252a871afcec7752fb2807b14`, tree
`3feeb703b931a6e7259782c10e7d1575adc83e5e`; exact repository, license-file,
and anonymous raw-readback evidence is bound in
[`manifests/stacks-pin.json`](../manifests/stacks-pin.json). This checkpoint
also binds an initialized [Commons overlay registry](../manifests/stacks-overlay.json)
with zero entries, a strict [candidate-entry schema](../manifests/stacks-entry.schema.json),
an offline [candidate validator](../scripts/check-stacks-entry.py), its
[regression suite](../scripts/test-stacks-entry.py), and a deterministic [composition contract](../manifests/stacks-compose.json).
That contract now binds an exact validator-only
[preflight executable](../scripts/stacks-preflight.py) and its
[blocked-state result](../manifests/stacks-preflight.json). Those files are
control-plane infrastructure. The separate composition executor remains
unbound. This checkpoint still does **not** claim that an upstream tree was
copied into Commons or that a candidate was accepted, or that a content-bearing Commons overlay, composition run,
output, composed build, or modified edition has been produced.

Upstream Stacks remains a respected source and synchronization target. Its
acceptance is not a dependency, approval gate, or veto over Commons editorial
work. Commons writes only to Commons-owned namespaces. An implementation must
replay the exact upstream repository, license identity, commit, and tree before
composing any output; it must never modify upstream, an independently maintained
namespace, or protected branch state.

## Five layers

1. **Pinned upstream mirror.** Keep one exact read-only upstream identity. The
   pin is the reproducible source baseline; floating upstream is only a sync
   locator.
2. **Commons overlay.** The registry exists with zero entries. Put original additions, historical-source mappings,
   provenance, corrections, multilingual semantic links, stable Commons IDs,
   tests, and review receipts in a clearly renamed Commons namespace. Never
   present overlay material as upstream-authored or upstream-approved.
3. **Deterministic composition.** The current preflight contract refuses to
   compose an empty registry. Its executable is validation-only, not the
   composition executor. Build only from one approved upstream pin plus one
   approved overlay commit and a separately bound exact executor. Record all
   inputs, the executor, generated members, bytes, hashes, tests, failures, and
   the resulting cursor.
4. **Optional modified edition.** A public modified edition is optional. If
   produced, it must follow the applicable GFDL obligations, use a distinct
   title, preserve attribution and license/history notices, and state plainly
   that upstream endorsement is not implied.
5. **Periodic upstream synchronization.** Review upstream movement against the
   last pin, import useful maintenance through an explicit sync commit, replay
   overlay tests, and preserve conflicts and rejected changes. Synchronization
   does not surrender Commons editorial control.

## Candidate-entry contract

The candidate contract validates a materialized package before any registration
decision. Its self-excluding member manifest lists every other regular file by safe
POSIX path, byte count, SHA-256, content kind, stable ID, language, source
locators, provenance receipts, supersession, and rights notice. The validator
rejects missing or extra files, unsafe or case-colliding paths, symlinks and
reparse points, namespace collisions, mixed upstream pins, duplicate stable
IDs, count/tree mismatches, and absent or misclassified provenance, test, and
review receipts. The same published schema exposes the separate member-manifest,
scope, review, and test document shapes under `$defs`; JSON object field order is
not significant, while duplicate keys and mismatched receipt subjects are
rejected. Retained validation output uses repository-logical roles and paths,
not invocation-machine paths.

Run it against one materialized candidate with:

```text
python scripts/check-stacks-entry.py --entry CANDIDATE.json --package MATERIALIZED_ROOT --schema manifests/stacks-entry.schema.json --pin manifests/stacks-pin.json --registry manifests/stacks-overlay.json
```

Success is exactly `VALID_CANDIDATE_UNREGISTERED`. It proves the declared
materialized members and structural control relationships under the bound pin. It does
not register the candidate, prove the candidate's declared Git commit or tree,
certify mathematics, imply upstream approval, or make composition ready. The
synthetic regression suite defines 54 cases: one valid, 52 invalid, and one
platform-conditional symlink case; it registers no fixture and contains no
mathematical payload.

## Executable blocked-state preflight

From the repository root, replay the exact current state with:

```text
python scripts/stacks-preflight.py --root . --expect BLOCKED_EMPTY_OVERLAY_REGISTRY
```

The `--expect` flag makes exit 0 mean only that the validator derived the exact
expected blocked outcome. It does not mean readiness, composition, build
success, or mathematical review. Without `--expect`, the same valid blocked
state exits 20. The preflight is offline and validator-only: it performs no
composition and writes no overlay or edition output. Contract v1 deliberately
rejects a nonempty registry rather than treating unbound content as ready.

The bound state is therefore exact: zero accepted candidates, zero registry entries, zero overlay content,
zero composition runs, zero generated members, zero output, zero builds, and no
modified edition. The next implementation generation requires one validated,
separately approved manifest-complete, provenance-referenced overlay entry and a separately bound exact composition
executor.

## Predecessor-assertion boundary

An unverified predecessor handoff asserts only this about a prior contribution
route: PRs **#196** and **#197** were closed unmerged at the same timestamp,
with zero public comments and zero public reviews. It did not bind a repository
or resolvable URLs for those bare numbers, so this is not independently
resolvable public evidence. No motive, policy, or private communication may be
inferred from the assertion.

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
writer, upstream repository, license, commit and tree, license hash, overlay
namespace, manifest or source-only sentinel, composition state, tests, review
plan, and synchronization cursor needed here.

The form fixes the Board ID to `stacks-commons-layer`. Choose the workflow that
matches the declared intent exactly:

| Intent | Required workflow |
|---|---|
| Prepare and validate an unregistered candidate against the exact upstream pin | `upstream_overlay_sync` |
| Independently mirror or check an existing Commons overlay | `independent_review` |
| Propose a deterministic composition and test fixture | `assembly_review` |
| Return source or license evidence only | `source_intake` |

Candidate preparation uses an exact manifest identity and the composition
sentinel `not yet bound`. Source-only intake uses `not applicable — source or
license evidence only` in both manifest and composition fields. Independent
review supplies the reviewed manifest identity and uses `not applicable —
independent overlay review` for composition. An assembly proposal must instead
name its executor, ordered inputs, generated-member manifest, replay receipt,
and before execution gate.

Parallel work remains welcome, but each Commons overlay namespace and its
ancestor/descendant chain has one writer identity at a time. Disjoint
namespaces—neither equal nor ancestor/descendant—may proceed independently.
The issue auditor requires each exact identity to occupy the whole submitted
field, rejects mixed repository revisions, and reads both executable identities
from the same human-approved commit as the board; worktree comparison is drift
detection, not the checker trust root.

1. Coordinate a single writer for the Commons namespace through that form.
2. Replay the bound upstream repository, applicable license, commit, and tree.
3. Validate the existing zero-entry registry and blocked-preflight composition
   contract with the exact executable command above; do not create a parallel
   control plane and do not treat expected-block exit 0 as readiness.
4. Materialize and validate one exact manifest-complete, provenance-referenced candidate with the
   candidate-entry command above. Preserve `VALID_CANDIDATE_UNREGISTERED` as a
   pre-registration state, not an approval claim.
5. Independently verify the candidate's declared Git commit/tree and review
   scope, then separately approve and register its namespace without copying
   mutable working state or changing upstream.
6. Bind a separate exact composition executor, advance the contract beyond v1,
   and only then execute and validate a minimal deterministic fixture.
7. Return the exact pin, overlay, build, tests, review receipt, and next sync
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
