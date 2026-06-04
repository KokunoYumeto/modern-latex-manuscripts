# Special characters, notation, and translation conventions

## Frequently confused symbols

| Visual source | TeX | Notes |
|---|---|---|
| \(\ell\) | `\ell` | Do not use plain `l` in \(\ell\)-adic. |
| \(\kappa(x)\) | `\kappa(x)` | Do not confuse with `\chi(x)`. This was a real Paper 5 cumulative error. |
| \(\mathcal J\) | `\mathcal J` | Nilpotent ideals and sheaves often use calligraphic letters. |
| \(\pi'\), \(\pi''\) | `\pi'`, `\pi''` | Preserve prime/double-prime distinctions, especially in factorizations. |
| \(\widehat{\mathbb Z}\) | `\widehat{\mathbb Z}` or `\bZ` | Use for profinite completion. |
| \(\mathbb A_f\) | `\mathbb A_f` or `\Af` | Finite adeles. Avoid double subscripts such as `\Af_T` if `\Af` already contains `_f`; use `\mathbb A_T^f`. |
| \(\operatorname{Spec}\) | `\operatorname{Spec}` | Never italicize as a variable. |
| \(\operatorname{Hom}\), \(\operatorname{Gal}\), \(\operatorname{Sym}\) | `\operatorname{...}` | Use roman operator names. |
| \(R^1f_*\mathbb Z\) | `R^1f_*\mathbb Z` | Keep star placement visually exact. |
| \(\widetilde H^i\) | `\widetilde H^i` | Image of compact-support cohomology in ordinary cohomology. |

## French/English translation conventions

| English | French |
|---|---|
| cusp form | forme parabolique |
| sheaf | faisceau |
| locally constant constructible | localement constant constructible |
| geometric point | point géométrique |
| finite adeles | adèles finies |
| up to isogeny | à isogénie près |
| Néron model | modèle de Néron |
| Hodge filtration | filtration de Hodge |
| Hecke algebra | algèbre de Hecke |
| double coset | double classe |
| fiber product | produit fibré |

## Layout conventions

Use ordinary paragraph flow. Avoid artificial page breaks in cumulative TeX unless a major section break forces it. Use display math for long formulas. Use small matrices for source-style inline matrices and display matrices for Hecke double-coset generators.

## Clean-package forbidden strings

These strings should not occur in clean paper TeX/PDF filenames or visible text:

- source checked
- verified
- working
- audit
- report
- screenshot
- render_check
- log
- TODO
- FIXME

They may occur in this methodology packet, because this packet is not a clean paper deliverable.
