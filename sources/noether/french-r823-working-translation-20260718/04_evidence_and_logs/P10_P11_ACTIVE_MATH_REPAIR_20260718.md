# P10/P11 active mathematical-notation repair

Status: exact loci verified in the active dependencies and a scoped 100-page LuaLaTeX driver. This support artifact does not alone certify either whole paper.

Authority: `Noether_R823_cum_de.tex`, SHA-256 `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`.

## P10

- Active target: `working/r823_fr/tex/N10_fr_body.tex`, SHA-256 `4A654335F4E3243EA604185177956189634E13925F8C967587D97C6B9836D555`, lines 234--246.
- Authority: R823 lines 7839--7847, equations at 7841 and 7845.
- Preamble support: active raw wrapper `cum_fr_R823_COMPLETE.tex:58` defines `\providecommand{\Xreal}{\mathfrak{X}}`; raw SHA-256 `F3B412B9CD8E3165F8564B9BAE9D590CE3CD7E985315EFD3EE21F87F884281FE`.

The repaired passage uses the authority's real variable `x`, the distinct fraktur quantity `\Xreal`, and exact grouping:

```tex
f(x\cdot(1\pm ic))=\Xreal(1+ic)=f(x)\cdot(1+i f(c)),
f(x)=\Xreal(\sigma+i\tau).
```

The surrounding prose now likewise distinguishes `x` from `\Xreal`. This is not an alpha-renaming: collapsing both to a single ordinary symbol loses the source's distinction between the argument and its associated real value.

## P11

- Active target: `working/r823_fr/tex/N11_fr_body.tex`, SHA-256 `448209E970F127E49DCD753542404CFA9735BB722CF9F88D9F34CE7B81180665`, line 162.
- Authority: R823 lines 7961--7965, formula at 7964.

The target now reads

```tex
\sigma_k(x)=\frac{G_k(x)}{H_k(x)}
\quad\text{ou}\quad
H_k(x)\cdot\sigma_k(x)=G_k(x),
```

removing the stray prime formerly attached only to the numerator in the first equality. Both occurrences are the same `G_k`, as the authority and the algebraic rearrangement require.

The combined P07--P17 scoped LuaLaTeX rebuild passed with the same `\Xreal=\mathfrak X` definition. No P02 candidate file or repair script was involved.
