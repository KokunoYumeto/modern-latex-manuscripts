# Split-Zero Geometry and Common Deformation Registers

This is the navigation file for the 18 July 2026 residual-Niemeier integration
to the project-atlas release under the cite-all-versions DOI
[10.5281/zenodo.20822444](https://doi.org/10.5281/zenodo.20822444).

Start with `00_PROJECT_ATLAS_20260717.pdf`. It explains the mathematics,
status boundaries, ownership boundary, and reading routes without requiring a
reader to unpack an archive.

The newest sequence is Packets 198--202. Packets 198--200 prove the exact
K4/XOR support skeleton, audit the proposed predatum/Jordan morphisms, and show
that the full ordered source datum canonically selects the projective ray
`c_2=(3,10)` and its exact odd projector. Packet 201 adds a
universal Cayley-Dickson multiplication-frame audit, an exact four-dimensional
sedenion annihilator for `e_3+e_10`, and a corrected Poincare-Hopf/K4 sphere
account that keeps cited topology separate from generated proof. Packet 202
then resolves the displayed no-defect `L=8`, `j=2` shadow question in the
negative: its exact coefficient at `q^(1/120) qbar^(1/24)` is
`2*exp(2*pi*i/12)`, so the aggregate does not cancel. All-sector and
full-shadow questions remain open.

This version also adds the public Part 8-C2B residual-Niemeier audit. Its
source-free 19-check certificate constructs an even unimodular rank-24
extension, exhausts all 72 glue classes, proves that no new roots occur, and
therefore identifies the root system as `A5^4D4`. Identification with the
corresponding Niemeier lattice is an isometry statement using the standard
classification. The theta identity `Theta=E4^3-576*Delta`, equivalently
`Theta/Delta=J+168`, uses the standard even-unimodular theta-modularity
theorem. The bound `g4>=5` is an exact specialization of Scaduto's cited
theorem, not an independently formalized gauge-theory result. Level-six/
`R=107` compatibility and “instanton-sensitive datum” remain boundaries.

## Main files

- `00_PROJECT_ATLAS_20260717.pdf`: human front door.
- `01_PROJECT_ATLAS_20260717.md`: searchable atlas source.
- `02_CURRENT_RESULTS_COMPENDIUM_20260717.pdf`: complete result packets.
- `03_FORMALIZATION_AND_EXACT_CHECKS_20260717.zip`: Lean, Python, ledgers,
  builds, axiom audits, and the atomic six-file Part 8-C2B public bundle.
- `04_VISUAL_ATLAS_20260717.pdf`: selected explanatory visual work.
- `05_VISUALIZATIONS_AND_DATA_20260717.zip`: editable and replayable visual
  assets.
- `06_CURRENT_WORKING_TEXTS_20260717.zip`: TeX, Markdown, and text versions.
- `PROVENANCE_AND_RIGHTS.md`: what is included, excluded, and credited.
- `MANIFEST.json` and `SHA256SUMS.txt`: complete inventory and integrity data.

## Public proof closure

The atlas does not use private GitHub as a proof location. Every packet referred
to by number in the public navigation files or included packet sources is
present in the public compendium. Its TeX, Markdown, and plain text are in the
working-text ZIP; named generated checkers, outputs, ledgers, summaries, and
Lean files are in the formal ZIP; and referenced visual families are in the
visual ZIP. External theorems are identified by primary citations.

The Part 8-C2B facade, TeX, source-free checker, 19-row replay ledger, status
row, and eight-row boundary ledger are kept together under
`audits/branch32a_part8c2b/repository/` in the formal archive, preserving their
original relative paths for unchanged replay. The facade also appears in the
complete results compendium. The release gate rejects any partial C2B bundle.

The release builder scans all packet-number references, including references
inside the packet TeX and public machine-readable extracts. A 2026-07-18 audit
caught Packet 077's dependency on previously omitted Packet 076; this release
therefore includes Packet 076 and its source-crosswalk checks. The gate also
checks the Claude N16b audit trail, Packet 201 Lean facade, revised D3 family,
public C6/Sigma atlas, rights-safe K-ladder charter integration, and complete
Packet 202 replay run. The result is recorded under
`build_report.reference_closure` in
`MANIFEST.json`; a missing member aborts the build.

## Status rule

The release separates exact theorems, checked calculations, generated
constructions, obstructions, diagnostics, evidence-backed open problems, and
historical exploration. A conversational hunch is not silently converted into
a conjecture. A known-failing map is recorded as an obstruction rather than a
conditional theorem.

## Rights boundary

No JT-authored corpus dump is included. Jacolm Tobley is credited as a
researcher/project relationship. The public payload consists of generated
project work, repository-maintainer work, exact checks, and rights-screened
derivatives. See `PROVENANCE_AND_RIGHTS.md` for the complete rule.

## Citation

Use the concept DOI for the evolving project:

> The Clankers, *Split-Zero Geometry and Common Deformation Registers:
> Project Atlas, Exact Results, Formalization, and Visualizations*, Zenodo,
> 2026. https://doi.org/10.5281/zenodo.20822444

Use the version DOI displayed by Zenodo when citing this exact file state.
