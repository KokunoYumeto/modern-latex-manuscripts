# P20 active specialization-symbol repair

Status: one exact source-symbol defect repaired in the active nested P20 dependency. This is locus-specific support evidence, not whole-unit certification.

- German authority: `authority/R823/pkg_r823/Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717/1/01_cumulative/Noether_R823_cum_de.tex`
- Authority SHA-256: `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`
- Active wrapper: `working/r823_fr/tex/N20_fr_body.tex`, SHA-256 `6207EC014945CD38F975F2593CC465F030E329B49E3BC6841819F7A9A1CFA1BC`, which inputs the French standalone body below.
- Active body: `working/r823_fr/external_translations/paper20/french/v001/Noether_Paper20_French_v001.tex`, SHA-256 `E58466AF6687E63C1AF04F4D682552243A921E927FF897D6BED2716CD61A7855`.

R823 line 12421 explicitly defines a bar as the notation for a polynomial or form obtained by specializing its indeterminates. R823 line 12528 therefore refers to the specialized objects as

```tex
\bar H(x) \quad\text{and}\quad \bar H(x,y).
```

The active French body at line 191 now preserves both bars in the sentence transferring identity (14) to special systems of values. The earlier unbarred `H(x)` / `H(x,y)` would incorrectly refer to the generic forms and erase the specialization that the argument requires. The change is confined to this source sentence; generic `H`, `F`, and `G` elsewhere were not globally barred.

The live cumulative wrapper at the time of review has raw SHA-256 `3F19C982F88A24AD9834B413696C44F65CF85E4904171547DC5EA1A42EDEDE31`; because P20 is a nested input, final whole-expanded and unit hashes must be recomputed after the dependency graph is frozen.
