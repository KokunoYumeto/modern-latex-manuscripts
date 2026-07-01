# Classical Audit Lean Sidecars - Local Source Intake - 2026-07-02

Local ZIP:
`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Lean formalization sidecars\ClassicalAudit_LeanSidecars_Noether_Steinitz_Weber_Jordan_20260630.zip`

ZIP metrics:

| Field | Value |
|---|---:|
| Bytes | 9,834 |
| Entries | 14 |
| SHA256 | `E9E494210774F814505CEC76F5AA5F2D6C8309EC46EA8B1A70CB77B070691FA9` |

Included files:

- `NoetherIdealtheorie.lean`
- `Steinitz.lean`
- `Weber.lean`
- `AffineGroup.lean`
- Lean build logs for the four sidecars
- minimal `lakefile.toml`, `lake-manifest.json`, and `lean-toolchain`
- README / Noether pilot README / `SHA256SUMS.csv`

Package self-description:

The package is a project-relevant extraction from a local Lean/Mathlib working
tree. It keeps only small classical-manuscript audit sidecars and minimal Lean
project files needed to reproduce the checks. It explicitly excludes unrelated
side research files.

Noether pilot anchors:

- `noetherianRing_iff_every_ideal_finitely_generated`
- `primaryIdeal_iff_factor_or_power_condition`

Build-log caveat:

The included `NoetherIdealtheorie.buildlog.txt` records Lean declarations and
axiom dependencies (`propext`, `Classical.choice`, `Quot.sound` as applicable).

Classification:

This is formalization-aided sanity-anchor material, not a proof that the
historical transcription or translation is correct. It can help catch drift in
definitions and theorem statements where a clean Mathlib analogue exists. It
cannot certify prose, historical exposition, page completeness, table layout,
formula typography, or source-image fidelity.

Suggested public handling:

Keep as a Lean/formalization support or workflow-sidecar candidate. If published
to Zenodo, front it as a small support packet and cross-link Noether/Steinitz/
Weber/workflow records, but do not present it as mathematical certification of
the editions.
