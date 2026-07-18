# P19 active mathematical repair

Status: three exact mathematical-notation repairs verified in active dependencies. This support artifact does not alone certify the whole paper.

Authority: `Noether_R823_cum_de.tex`, SHA-256 `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`.

| Active target and SHA-256 | Target locus | R823 locus | Repair and meaning |
|---|---:|---:|---|
| `N19a_fr_body.tex` — `D0A881BAD7AE0008E7EC4E52407F0ADF68AE0B6AFEB90AD03395DC967F8FB57A` | line 145 | line 11327 | Restored the non-strict index condition `(r\le s)`. The proof then correctly uses divisibility along the chain to infer that both summands lie in the later ideal. |
| `N19_s09_fr_body.tex` — `3AA718D618EEEFAF5F6040F7D919B04AFB8F54B61607F3181D2875DFBE62EE23` | line 8 | line 12038 | Restored Noether's explicit symbol `(#)` for addition in the abstract ring `\Sigma`, alongside the distinct ring multiplication `(\times)`. |
| same file/hash | line 20 | line 12050 | Restored the matching distributive law `(a\# b)\gamma=a\gamma+b\gamma`. Ring addition `#` is deliberately distinct from module addition `+` on the right. |

These changes were made at the cited loci only. In particular, no blanket replacement of `+` by `#` was performed: the module operations `\alpha+\beta` and `a\gamma+b\gamma` retain ordinary `+` exactly as the source requires.
