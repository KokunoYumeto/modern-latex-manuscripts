# P17 active formula repair

Status: one severe omission repaired and verified in the exact active dependency. This support artifact does not by itself certify all of P17.

- German authority: `Noether_R823_cum_de.tex`, SHA-256 `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`, lines 11110--11114.
- Active target: `working/r823_fr/tex/N17_s11_12_fr_body.tex`, SHA-256 `CEFBC571ACEC20494673CF5DEA919746EF8AF37F337CB6FA2B3DD463D315335F`, lines 262--267. This later hash also includes the congruence repair documented below.

R823 defines the module by

```tex
\xi-\frac{y}{x}\eta=\xi-a.
```

The active French formula had lost the factor `\eta` after `y/x`, changing the defining generator and making the displayed equality mathematically incoherent. The target now restores the exact source expression `\xi-\frac{y}{x}\eta=\xi-a`. The following argument about the infinite quotient group and the divisor `\mM_1=(\xi-a,F(\xi,\eta))` was checked locally to confirm that the restored `\eta` is the required variable, not an optional normalization.

No global substitution was made. The ongoing P17 language/metadata pass must preserve this display and recompute the final target hash after any later prose-only edits.

## Four module congruences

R823 lines 10945--10950 state

```tex
MQ\equiv0(\mathfrak N),\qquad PQ\equiv1(\mathfrak N),
NP\equiv0(\mathfrak M),\qquad QP\equiv1(\mathfrak M).
```

The active target at lines 72--80 now preserves all four congruences. They had been collapsed to equalities, which would erase the quotient-module meaning of the statement. The repair changed only the relation signs; the four polynomials, moduli, zero/one residues, and subsequent integral argument remain in the source order.

## Staged noncommutative definition in § 2

The active `N17_s01_04_fr_body.tex`, SHA-256 `E3160D8E7678C24E204E47CA8C6D078B5D46659A32B6F33171E99603E52937EB`, lines 133--149 now follows the two-stage R823 definition at lines 10185--10198:

1. Before commutativity of the `\xi_i` is imposed, `J` consists of the word products `a\xi_1,b\xi_2,\ldots,c\xi_n` and their finite sums, and a polynomial has the word-indexed form
   ```tex
   F(\xi_1,\ldots,\xi_n)=\sum a_{\nu_1\ldots\nu_\rho}\xi_{\nu_1}\cdots\xi_{\nu_\rho}.
   ```
2. Only afterward, at target line 149 / R823 line 10198, is multiplication among `\xi_1,\ldots,\xi_n` stipulated to be commutative, so ordinary monomial notation becomes available.

The earlier target prematurely used commutative monomials in the first stage, erasing the logical order of the construction. The repair restores the exact word-product definition without changing the later commutativity hypothesis or product law (5).

## Greek `\nu` in the finite-basis argument

R823 lines 10488--10490 choose a finite basis

```tex
\ma_{i_1},\ldots,\ma_{i_\nu},\qquad i_1<\cdots<i_\nu,
```

then take `\mu>i_\nu` and expand `\ma_\mu` with coefficients through `\mx_\nu`. The active `working/r823_fr/tex/N17_s05_07_fr_body.tex`, SHA-256 `282FA06D0C4AA9D1A9FD37862E2A474C2DA92A489DCF060118E7D80AF828502E`, lines 230--233 now preserves the Greek cardinal index `\nu` consistently in all three roles. This is distinct from Latin `v` elsewhere in the corpus and was repaired locally, not by a global glyph substitution.
