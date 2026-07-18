# P04 R823 formula recheck

Status: **superseded partial check; P04 remains blocked.** The five previously reported formula/index defects below were repaired, but the subsequent exhaustive audit found additional omissions/corruptions. This artifact must not be used to promote P04 parity.

- R823 authority: `Noether_R823_cum_de.tex`, SHA-256 `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`.
- P04 source-unit SHA-256: `9FC3F05AECA4F993BDDCE711E4D4AEFEDF2791FAA04BF5F8141A2B33776C2EB7`.
- Live P04 target-unit SHA-256 at review: `2A4CC8504C53E5EAFBDF6BB38D03085FD083963447078E6A50D10C1A97B76A66`.
- Review method: exact authority/target formula collation, including delimiter grouping, equality relation, subscripts, superscripts, and the separation of a multiplicative factor from a polar pairing.

| Authority locus | Live expanded-target locus | Exact disposition |
|---:|---:|---|
| line 3862 | line 3548 | Restored `q_{\rho-1}^{(1)}`; the prior off-by-one `q_\rho^{(1)}` is absent. |
| lines 3970–3972 | lines 3655–3659 | Formula (33) has the product `(R_{\rho-\alpha}p_{n-\rho+\alpha})` followed by the separate pair `\pair{R^{\tau-\alpha}}{p_{\tau-\alpha}}`; the two factors are no longer merged into one pair. |
| line 3989 | line 3673 | The denominator index is exactly `R_{\rho_1+\sigma_1-\alpha-\lambda}`, not the collapsed `R_\rho`. |
| line 4215 | line 3904 | The relation is equality, `(\xi^{(1)}\cdots\xi^{(n)})=\Delta`, not `\sim\Delta`. |
| lines 4445–4446 | lines 4134–4135 | The two indices are exactly `q'_{\lambda-1}` and `q''_{n-\lambda-1}`. |

The surrounding displays were read with their preceding and following equations; the repairs do not alter the French prose, theorem order, or equation labels. Final evidence generation must recompute the target-unit and whole-document hashes after P02 and all parallel edits settle.

## Later exhaustive-audit blockers

The audit of authority lines 3562–4509 against the current French P04 slice found, beyond the five passing spot checks above: the omitted two-determinant middle expansion of formula (8); collapsed ordinary-factor-times-pair products in formula (34); an extra epsilon in formula (38); corrupted untagged displays around authority lines 4058–4066; `T_{1-\sigma}` for `T_{n-\sigma}`; further ordinary factors changed into pairs; `(K-1)^{\rho_{k-1}}` reduced to `K^{\rho_{k-1}}`; an altered formula (45) range; strict `\sigma>\tau` for `\sigma\ge\tau`; a dropped prime; and `q_{n-\sigma-i}` for `q_{n-\sigma-\lambda}`. Note parity is 39/44: missing anchors/content are the title Salzburg-publication note (authority line 3563), formula-(6) Clebsch §5 citation (3639), the duplicated first formula-(7) lambda-range note occurrence (3657), the formula-(16) note linking it to (13) in rho variables (3757), and the §9 dissertation §§1–3 note (4477). The author line also requires restoration. A new full-unit artifact must replace this partial record after those defects and the continuing inline/prose audit are closed.
