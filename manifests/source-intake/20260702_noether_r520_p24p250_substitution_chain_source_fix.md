# Noether R520 - Paper 24 p250 Substitution-Chain Source Fix

Local ZIP:
`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_R520_LocalCodex_R519_P24p250_SubstitutionChain_SourceFix_20260702.zip`

ZIP metrics:

| Field | Value |
|---|---:|
| Bytes | 21,732,352 |
| Entries | 41 |
| SHA256 | `70359707D49A9CACF42744578DCF219AAFEE107C288579522A6C93CC22C8448F` |

R520 is now a clean packaged TeX-changing source-control candidate on top of
R519. The ZIP includes `README.md`, `summary_R520.json`,
`confirmed_fixes_R520.csv`, source witnesses, diff, render checks, and
XeLaTeX logs.

Repairs promoted from the included `confirmed_fixes_R520.csv`:

| Paper | Printed page | Current PDF page | Previous reading | New reading | Rationale |
|---|---:|---:|---|---|---|
| P24 | 250 | 258 | `-t_{i\lambda}` | `-t_{\lambda i}` | Source and surrounding formula `x_i=t_{1i}y_1+\cdots+t_{ni}y_n` require first index `\lambda`, second index `i`. |
| P24 | 250 | 258 | `\mathfrak p_{n-i+1}=\mathfrak o` | `\mathfrak p_{n-i+1},` | Source statement does not put `=\mathfrak o` in the display; the following proof derives that the last chain element must be the unit ideal. |

Build and scope:

- Base: R519 local cumulative.
- Cumulative PDF pages: 471.
- Changed output page: 258.
- Repairs: 2.
- Compile: XeLaTeX passed twice.

Source-quality caveat: P24 p250 authority is IA raw JP2 at about 400 dpi;
renders/crops are enlarged for readability only. Treat R520 as two inspected
source-control repairs only. It is not a reader release, not Paper 24
certification, not Noether closure, not whole-corpus certification, not
multilingual synchronization, and not critical-edition material.
