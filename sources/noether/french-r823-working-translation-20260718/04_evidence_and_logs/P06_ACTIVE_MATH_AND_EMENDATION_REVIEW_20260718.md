# P06 active mathematical repair and source-emendation review

Status: four exact dispositions verified in the active 130-file dependency graph. This is unit-support evidence, not by itself a final source-parity promotion.

Authority: `authority/R823/pkg_r823/Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717/1/01_cumulative/Noether_R823_cum_de.tex`, SHA-256 `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`.

Active targets:

- `working/r823_fr/tex/cum_fr_R823_COMPLETE.tex`, SHA-256 `3F19C982F88A24AD9834B413696C44F65CF85E4904171547DC5EA1A42EDEDE31`. P06 through the end of the first active portion is inline in this raw wrapper; the active graph does **not** `\input{N06a_fr_body.tex}`. The later wrapper hash includes the bounded P04 slice promotion; the cited inline P06 loci were outside that slice.
- `working/r823_fr/tex/N06c_fr_body.tex`, SHA-256 `F1775F2E42404A4E9DD72724D2AA22F236D852594B0E85C9145672E665F71463`.

## Exact R823 repairs

| R823 authority | Active target | Disposition |
|---|---|---|
| lines 5570--5573, equation (9): `H^*(x)\equiv M^*(x)\pmod{x_0}` | `N06c_fr_body.tex:266--270` | Restored the congruence sign `\equiv`; this is not an equality. The starred symbols and modulus are unchanged. |
| lines 5744--5747, Theorem VI$'$ | `N06c_fr_body.tex:467--470` | Restored the final argument `H_\sigma(x)` and denominator exponent `H(x)^k`. The numerator is now exactly `\Gamma(H(x),H_1(x),\ldots,H_\sigma(x))`. |
| lines 5626--5635, equation (3) and source note `*)` | `N06c_fr_body.tex:334--345` | Restored the Mertens reference and re-anchored its source-assigned marker to `R_0=a_0\ne0`, rather than to the preceding prose. The split `\srcfnmark`/`\srcfntext` form preserves the note below the display. |

## Explicit source emendation, not silent parity

R823 lines 5074 and 5078 both print an unstarred final condition, respectively after the conjugate-row and ordinary-row equations:

```tex
F^*(x^{(k)})H^*(\xi)-H^*(x^{(k)})F^*(\xi)=0;\qquad H(\xi)\ne0,
F^*(x)H^*(\xi)-H^*(x)F^*(\xi)=0;\qquad H(\xi)\ne0,
```

whereas the active raw target retains `H^*(\xi)\ne0` at `cum_fr_R823_COMPLETE.tex:4921` and `:4927`. Both stars are deliberate source emendations rather than transcription errors in the French:

- both displayed equations use `F^*` and `H^*` throughout (R823 lines 5074 and 5078);
- the immediately following parameterization is `F^*(x)/H^*(x)` (R823 line 5080);
- the geometric explanation's source note explicitly defines the excluded solutions by `F^*(\xi)=0`, `H^*(\xi)=0` (R823 line 5082);
- the next occurrence again imposes `H^*(\xi)\ne0` (R823 line 5086).

Thus unstarred `H(\xi)` at lines 5074 and 5078 is internally inconsistent with the local notation. The target preserves the mathematically coherent starred conditions, and final P06 evidence must label both rows `source emendation supported by R823 5074--5086`, not claim byte-literal symbol parity.

## Note-anchor build check

The exact source-note macros used in the P06 display and the P09 heading were compiled in the isolated one-page LuaLaTeX smoke driver `working/tmp/P06_P09_NOTE_ANCHOR_SMOKE_20260718.tex`. The run completed without a TeX error; PDF SHA-256 `A30C4F0EA9E01F29FD5DBCEC6F39259FE0536525AAD45F013AD665BF0359EDF0`, log SHA-256 `35AB623DBDF7ADD2495B90F2E8930818EA511B7859033FE2AD32D944433BFA45`. This checks the anchor mechanism only, not the final cumulative build.

The pre-anchor `N06c` is preserved at `working/backups/P06_P09_note_anchor_pre_20260718/N06c_fr_body.tex`, SHA-256 `8D7B9D4E4FB4AFE948DA974617517FF0776B5ADE928093CAD7533A5E5C412AC3`.

## Integrity check

The two active-file hashes above were computed after the exact repairs, source-note anchor restoration, and wrapper metadata updates. The equation-(9) congruence, Theorem VI$'$ formula, Mertens note, and the two inline source emendations occupy separate loci and were reviewed independently; no global `H`/`H^*` substitution was performed.
