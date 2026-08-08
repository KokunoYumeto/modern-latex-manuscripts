# GitHub Source Shelves

This is the shortest route from the repository front page to the source trees
that this GitHub-maintenance task is allowed to catalog. It lists preserved
working editions, translation drafts, evidence, and historical generations;
it does not promote every shelf to a current reader or certified edition.

Use a shelf's README or linked coverage map when one exists. A bare directory
link is an honest preserved landing: inspect its filenames and internal status
files before choosing a generation. Do not infer that the alphabetically first
or newest-looking directory is the current continuation head.

All nineteen task-maintained author, work, series, and mixed-corpus maps are
also collected in the [GitHub coverage-map index](../docs/github-maps.md).

## Current Mapped Corpora

| Author or corpus | GitHub shelf | Best status map |
|---|---|---|
| Alexandre Grothendieck, EGA | [EGA readers and source](ega/README.md) | [EGA coverage](../docs/ega-map.md) |
| Alexandre Grothendieck, Tôhoku | [Tôhoku checkpoint](tohoku/r1/README.md) | [Tôhoku coverage](../docs/tohoku-map.md) |
| Alexandre Grothendieck and collaborators, FGA | [FGA checkpoint](fga/cp9/README.md) | [FGA coverage](../docs/fga-map.md) |
| Jean-Louis Verdier | [Verdier checkpoint](verdier/r1/README.md) | [Verdier coverage](../docs/verdier-map.md) |
| Luc Illusie | [Illusie checkpoints](illusie/README.md) | [Illusie coverage](../docs/illusie-map.md) |
| Emmy Noether | [Noether source archive](noether/README.md) | [Noether language/work coverage](../docs/noether-map.md) |
| Pierre Deligne | [Deligne source shelf](deligne/) | [Deligne coverage](../docs/deligne-map.md) |
| Heinrich Weber | [Weber source shelf](weber/) | [Weber coverage](../docs/weber-map.md) |
| Richard Dedekind | [Dedekind source shelf](dedekind/) | [Dedekind coverage](../docs/dedekind-map.md) |
| P. G. Lejeune Dirichlet | [Dirichlet source shelf](dirichlet/) | [Dirichlet coverage](../docs/dirichlet-map.md) |
| Carl Friedrich Gauss | [Gauss source shelf](gauss/) | [Gauss coverage](../docs/gauss-map.md) |
| Bernhard Riemann | [Riemann source shelf](riemann/) | [Riemann coverage](../docs/riemann-map.md) |
| Ernst Steinitz | [Steinitz source shelf](steinitz/) | [Steinitz coverage](../docs/steinitz-map.md) |
| James Joseph Sylvester | [Sylvester source shelf](sylvester/) | [Sylvester coverage](../docs/sylvester-map.md) |
| Arthur Cayley | [Cayley source generations](classical/) | [Cayley custody and gap map](../docs/cayley-map.md) |
| Ukrainian applied mathematics | [Ukrainian source shelf](ukrainian-applied-math/) | [Exact reader/source coverage](../docs/ukrainian-map.md) |
| Non-European mathematical texts | [Multilingual source shelf](non-european/README.md) | [Exact work/language coverage](../docs/non-european-map.md) |

## Mixed And Supporting Shelves

| Shelf | What it preserves |
|---|---|
| [Classical algebra and arithmetic](classical/) | Exact mixed-root custody for Cayley, Dedekind, and Dirichlet only: 811 source/history files paired with 21 direct readers. Use the [classical shelf map](../docs/classical-map.md) before assigning or counting work. |
| [Additional author cluster](author-cluster/) | Three tracked reports/triage files only; pair with the [exact ten-reader map](../docs/cluster-map.md). No TeX, source PDF, or routed package ZIP is present in this root. |
| [Workflow](workflow/) | Preserved workflow and methodology briefings. |

Separately owned or explicitly prohibited project surfaces are intentionally not
enumerated here. Their absence from this task-maintained map is a custody
boundary, not evidence that their files do not exist.

## Exact Git-Object Audit

The nineteen allowed shelves contain 14,901 tracked files and
3,681,880,509 committed bytes. Every path, byte count, Git blob SHA-1, and mode
is in the [per-file index](../manifests/github-custody/20260807_sources_r5.csv).
The [compact summary](../manifests/github-custody/20260807_sources_r5.json) binds
each root's Git tree SHA-1 plus a SHA-256 digest over its ordinal canonical
path/size/blob stream.

There are 11,257 unique Git blob identities and 1,726 repeated-blob groups.
Only one repeated identity crosses roots: the same 8-byte `.gitattributes`
control appears at 57 paths across six roots. It is repository scaffolding,
not 57 independent mathematical objects. Distinct paths and generations remain
preserved; the audit does not deduplicate or delete them.

The committed-byte inventory is kept separate from checkout representation.
No source blob was opened, rehashed, compiled, rendered, OCRed, or rewritten
to produce this index; the source inventory uses Git tree and blob metadata.

The earlier landing-only audit remains as history:
[`20260805_source_shelves.json`](../manifests/github-custody/20260805_source_shelves.json).
