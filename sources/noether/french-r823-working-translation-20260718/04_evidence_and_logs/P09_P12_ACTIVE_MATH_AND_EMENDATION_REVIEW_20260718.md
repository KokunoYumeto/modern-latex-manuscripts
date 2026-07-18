# P09/P12 active mathematical repairs and P12 source emendation

Status: exact loci checked in active dependencies. This is supporting evidence, not whole-unit certification.

Authority: `Noether_R823_cum_de.tex`, SHA-256 `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`.

## Exact repairs

| Unit | Active target and SHA-256 | Target locus | R823 locus | Disposition |
|---|---|---:|---:|---|
| P09 | `N09b_fr_body.tex` — `C37DBE931FC73F4BF20521CB7CD535AE8D272BF060801BA968AAF4A52AAE6865` | lines 232--237 | line 7436 | Restored the defining congruence `z\equiv a_0+\cdots+a_{\sigma-1}(\eta) \pmod{\mathfrak M_\sigma(\eta)}`; equality would change the residue-class construction. |
| P09 | same file/hash | lines 201--205 | line 7303 | Restored the Steinitz source note and anchored its source-assigned `*)` marker to the §8 heading, matching R823, rather than leaving the reference on the following prose. |
| P12 | `N12_fr_body.tex` — `D0F70C905EBC292C2D74B89C25656DD9E70BF24C96F3BD3B790389294151162B` | line 38 | line 8093 | Restored the mixed differential `d\delta x`. |
| P12 | same file/hash | lines 186, 200, 216 | lines 8228, 8241, 8255 | Restored the bold differential symbol `\bdelta x` in the Lagrange identities and their stated domains of identity. |
| P12 | same file/hash | line 217 | line 8256 | Restored the exact list `d^2x,d\delta x,\delta^2x`, rather than duplicating the first differential. |

## Explicit P12 source emendation

R823 lines 8327--8329 state that `\varphi_\rho^{(i)}` is homogeneous of order `\rho`, but its displayed scaling law at lines 8330--8332 prints only a first power:

```tex
\varphi_\rho^{(i)}\!\left(\varkappa\cdot\frac{dx}{dt}\right)
=\varkappa\varphi_\rho^{(i)}\!\left(\frac{dx}{dt}\right).
```

The active target at `N12_fr_body.tex:303--307` retains

```tex
=\varkappa^\rho\varphi_\rho^{(i)}\!\left(\frac{dx}{dt}\right),
```

which is the scaling law mathematically compelled by the source's immediately preceding homogeneity statement. Final P12 evidence must record this as `source emendation supported by R823 8327--8333`, not claim literal symbol parity and not silently force the internally inconsistent first power.

No global replacement of `\delta`, `\bdelta`, or `\varkappa` was made; each locus was reviewed in its displayed-equation context.

The pre-anchor P09 file is preserved at `working/backups/P06_P09_note_anchor_pre_20260718/N09b_fr_body.tex`, SHA-256 `40CFAB3F4FEA0148E93CD253741AA65E8E931E399388DABF9B5F5BBA6E9E81DE`. The P06/P09 source-note macro smoke run completed successfully; its PDF/log hashes are recorded in `P06_ACTIVE_MATH_AND_EMENDATION_REVIEW_20260718.md`. This scoped run is not a substitute for the final cumulative build.
