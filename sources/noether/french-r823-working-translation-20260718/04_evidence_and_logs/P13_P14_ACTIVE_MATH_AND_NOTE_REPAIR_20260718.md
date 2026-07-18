# P13/P14 active mathematical and note repair

Status: the exact defects below are repaired in the active 130-file dependency graph and checked against the R823 German authority. This is source-keyed support evidence for the affected loci; it is not a whole-unit certification for P13 or P14.

- German authority: `authority/R823/pkg_r823/Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717/1/01_cumulative/Noether_R823_cum_de.tex`
- Authority SHA-256: `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`
- Live cumulative wrapper at review: `working/r823_fr/tex/cum_fr_R823_COMPLETE.tex`, raw SHA-256 `3F19C982F88A24AD9834B413696C44F65CF85E4904171547DC5EA1A42EDEDE31`

## P13: arbitrary-order total differential form

R823 lines 9024--9028 define a total differential form of arbitrary order `\lambda`:

```tex
\sum a\,\dd^\lambda x_i+\sum b\,\dd^{\lambda-1}x_i\,\dd x_\varkappa+\cdots.
```

The active target `working/r823_fr/tex/N13b_fr_body.tex`, lines 323--328, now preserves the order `\lambda`, the mixed term of order `\lambda-1`, the index `\varkappa`, and the following distinction from ordinary differential forms. Current target SHA-256: `83AFA64B58BD83CF40936CE15CC05E82EF7181C0545FE0299EC9F46BBBAF8CE7`.

## P13: source note at the infinitesimal transformation

R823 lines 9030--9038 give the logarithmic example and attach source note `1)` directly to

```tex
\D u_i=p'(x).
```

The active target lines 331--343 preserve the two displayed transformations and now attach the same source-assigned note at that formula, using the cumulative document's safe `\srcfnmark{1)}` / `\srcfntext{1)}` macro pair. The French note states that the finite transformations are calculated backward from the infinitesimal ones by the method at the end of §4, matching the authority. The pre-anchor target is preserved at `working/backups/P13_note_anchor_pre_20260718/N13b_fr_body.tex`, SHA-256 `115B12FE31E62CD381317C935BD8C806F559AE4D540AB43550B0C4478FA8390A`.

## P14: last-coefficient notation in the finite-basis proof

R823 line 9141 projects a linear form onto its last coefficient and writes the resulting finitely generated ideal as

```tex
b_1a_n^{(1)}+\cdots+b_\rho a_n^{(\rho)}.
```

The active target `working/r823_fr/tex/N14a_fr_body.tex`, line 91, now uses `a_n` and `a_n^{(i)}` throughout that sentence. This restores the exact coefficient eliminated by the following induction on `n`; the previous generic/mismatched coefficient notation was not retained. Current target SHA-256: `B8B5020709FD26D699947CA9CABE59607A5CB8A29D0DF3948B99F21C19C4911C`.

No broad symbol replacement was used in either paper. Final unit hashes and the whole-expanded target hash must be regenerated only after the remaining moving-source work is frozen.

## P13: deliberate transformation-index emendation

R823 line 8934 introduces the similar transformation as unindexed `\frakT=\frakT_q\frakT_p\frakT_q^{-1}` even though the same sentence immediately assigns it the parameters/functions `r`; R823 line 8945 then writes the same transformation as `\frakT_r`. The French target uses `\mathfrak T_r` at the first occurrence as well as the later one. This is a deliberate, mathematically forced correction of the source's missing index, not an omitted authority symbol. The other transformation indices and products remain source-exact.
