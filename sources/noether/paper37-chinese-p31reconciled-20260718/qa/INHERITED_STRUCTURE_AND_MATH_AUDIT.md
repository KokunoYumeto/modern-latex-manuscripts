# Paper 37 inherited structure and mathematics audit

- Sealed logical source: `evidence://local-workspace/interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper37_zh_rebase_001_20260718\source\Noether_Paper37_German_P31_logical_article_LF.tex`, SHA-256 `68C72173E0C060BC68CB3651AF078ACE82B4D5806C8A41584632AA2BB4A9B27B`.
- Inherited logical witness: `evidence://local-workspace/interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper37_zh_rebase_001_20260718\witness\Noether_Paper37_SimplifiedChinese_Inherited_logical_article_LF.tex`, SHA-256 `50094AA7F4A8153E613496E4F2F43B6E69B7B512FD689018459BAF366736C1D1`.
- Ordered math spans: source `292`, witness `288`.
- Source/witness footnotes: `12` / `12`; source/witness emphasis scopes: `15` / `14`.
- This is an adverse-witness audit. Unequal strings require adjudication; equal counts do not establish semantic correctness.

## Known adverse findings

- `P37-W-AUTHOR-OMISSION` (source_hierarchy_omission): The author center line is absent. Restore the source author hierarchy in the target.
- `P37-W-DEURING-PRODUCTS` (mathematical_operator_error): The inherited display uses division slashes while retaining 4,2,2,4. Replace all four divisions with source multiplication and preserve the inherited form as adverse evidence.
- `P37-W-ORDER-CASE` (symbol_case_error): The inherited first symbol is \frakO, the capital order of K used elsewhere. Restore \frako.
- `P37-W-BASIS-INDEX` (symbol_index_error): The inherited text has v_1,\ldots,v_l. Restore the source index t.
- `P37-W-COEFFICIENT-FIELD` (symbol_object_error): Two inherited occurrences change subscript P to \mathfrak P while retaining Pe^{S_i} later. Restore the ordinary capital P consistently.
- `P37-W-GROUP-SUM-EXPANSION` (editorial_formula_expansion): The first occurrence is expanded to \sum_{S\in\Gg} S while the next remains \sum S. Use the exact source form unless an explicit editorial gloss is separately recorded.

## Ordered compact-math differences

| span | source line | witness line | sealed source | inherited witness |
|---:|---:|---:|---|---|
| 2 | 11 | 7 | `\frakO` | `K` |
| 3 | 11 | 7 | `K` | `\frakO` |
| 4 | 11 | 7 | `\frako` | `k` |
| 5 | 11 | 7 | `k` | `\frako` |
| 7 | 11 | 7 | `\frakp` | `k` |
| 8 | 11 | 7 | `k_\frakp` | `\frakp` |
| 9 | 11 | 7 | `k` | `k_\frakp` |
| 10 | 11 | 7 | `K_\frakp` | `K` |
| 11 | 11 | 7 | `K` | `K_\frakp` |
| 21 | 15 | 13 | `2\sqrt[5]{2}\cdot\sqrt[5]{2^4}` | ` 2\sqrt[5]{2}/\sqrt[5]{2^4},\quad \sqrt[5]{2^2}/\sqrt[5]{2^3},\quad \sqrt[5]{2^3}/\sqrt[5]{2^2},\quad \sqrt[5]{2^4}/(2\sqrt[5]{2}), ` |
| 22 | 15 | 19 | `\sqrt[5]{2^2}\cdot\sqrt[5]{2^3}` | `4,2,2,4` |
| 23 | 15 | 21 | `\sqrt[5]{2^3}\cdot\sqrt[5]{2^2}` | `\frakO/\frako` |
| 24 | 15 | 21 | `\sqrt[5]{2^4}\cdot 2\sqrt[5]{2}` | `\frako` |
| 25 | 15 | 21 | `4,2,2,4` | `\frako` |
| 26 | 17 | 21 | `\frakO/\frako` | `\frakp` |
| 27 | 17 | 21 | `\frako` | `\frakp` |
| 28 | 17 | 21 | `\frako` | `k` |
| 30 | 17 | 21 | `\frakp` | `\frakO/\frako` |
| 31 | 17 | 23 | `\frakp` | `K/k` |
| 32 | 17 | 25 | `k` | `\frakp` |
| 33 | 17 | 27 | `\frakO/\frako` | `\frakO` |
| 34 | 19 | 27 | `K/k` | `\frako_\frakp` |
| 35 | 21 | 27 | `\frakp` | `k` |
| 36 | 23 | 27 | `\frako` | `\frakp` |
| 37 | 23 | 27 | `\frako_\frakp` | `k_\frakp` |
| 38 | 23 | 27 | `k` | `\frakp` |
| 39 | 23 | 27 | `\frakp` | `k` |
| 40 | 23 | 27 | `k_\frakp` | `(\Gg)` |
| 41 | 23 | 27 | `\frakp` | `\Gg` |
| 42 | 23 | 27 | `k` | `[\Gg]` |
| 43 | 23 | 27 | `(\Gg)` | `\Gg` |
| 44 | 23 | 27 | `[\Gg]` | `n` |
| 45 | 23 | 27 | `\Gg` | `(\Gg)_k` |
| 46 | 23 | 27 | `n` | `(\Gg)_{k_\frakp}` |
| 47 | 23 | 27 | `(\Gg)_k` | `k` |
| 48 | 23 | 27 | `(\Gg)_{k_\frakp}` | `k_\frakp` |
| 49 | 23 | 27 | `k` | `[\Gg]_\frako` |
| 50 | 23 | 27 | `k_\frakp` | `[\Gg]_{\frako_\frakp}` |
| 51 | 23 | 27 | `[\Gg]_\frako` | `\frako` |
| 52 | 23 | 27 | `[\Gg]_{\frako_\frakp}` | `\frako_\frakp` |
| 53 | 23 | 29 | `\frako` | `(\Gg)_k` |
| 54 | 23 | 29 | `\frako_\frakp` | `(\Gg)_{k_\frakp}` |
| 55 | 25 | 29 | `(\Gg)_k` | `[\Gg]_\frako` |
| 56 | 25 | 29 | `(\Gg)_{k_\frakp}` | `[\Gg]_{\frako_\frakp}` |
| 57 | 25 | 29 | `[\Gg]_\frako` | `(\Gg)_k` |
| 58 | 25 | 29 | `[\Gg]_{\frako_\frakp}` | `(\Gg)_{k_\frakp}` |
| 59 | 25 | 32 | `(\Gg)_k` | `\frakp` |
| 60 | 25 | 32 | `(\Gg)_{k_\frakp}` | `\Gg` |
| 61 | 28 | 32 | `\frakp` | `n` |
| 62 | 28 | 32 | `n` | `[\Gg]_{\frako_\frakp}` |
| 63 | 28 | 32 | `\Gg` | `(\Gg)_{k_\frakp}` |
| 64 | 28 | 32 | `[\Gg]_{\frako_\frakp}` | `\frakp` |
| 65 | 28 | 32 | `(\Gg)_{k_\frakp}` | `n` |
| 66 | 28 | 32 | `\frakp` | `[\Gg]_{\frako_\frakp}` |
| 67 | 28 | 34 | `n` | `[\Gg]_\frako` |
| 69 | 30 | 34 | `[\Gg]_\frako` | `n` |
| 70 | 30 | 34 | `[\Gg]_{\frako_\frakp}` | `\frakp` |
| 72 | 30 | 34 | `\frakp` | `[\Gg]_{\frako_\frakp}` |
| 73 | 30 | 34 | `n` | `\frako_\frakp` |
| 75 | 30 | 34 | `[\Gg]_{\frako_\frakp}` | `\frako_\frakp` |
| 76 | 30 | 34 | `\frako_\frakp` | `k_\frakp` |
| 77 | 30 | 36 | `\frako_\frakp` | `\frakp` |
| 78 | 30 | 36 | `k_\frakp` | `n` |
| 79 | 32 | 37 | `\frakp` | `         \frakC=E^{(1)}[\Gg]_{\frako_\frakp}+(1-E^{(1)})[\Gg]_{\frako_\frakp},         \qquad         E^{(1)}=\frac1n\sum_{S\in\Gg} S, ` |
| 80 | 32 | 42 | `n` | `[\Gg]_{\frako_\frakp}` |
| 81 | 33 | 42 | `         \mathfrak C=E^{(1)}[\Gg]_{\frako_\frakp}+(1-E^{(1)})[\Gg]_{\frako_\frakp},         \qquad         E^{(1)}=\frac1n\sum S, ` | `E^{(1)}=\frac1n\sum S` |
| 82 | 38 | 42 | `[\Gg]_{\frako_\frakp}` | `\frakC` |
| 83 | 38 | 42 | `E^{(1)}=\frac1n\sum S` | `\frakC` |
| 84 | 38 | 42 | `\mathfrak C` | `E^{(1)}` |
| 85 | 38 | 42 | `\mathfrak C` | `(1-E^{(1)})S` |
| 86 | 38 | 42 | `E^{(1)}` | `S\in\Gg` |
| 87 | 38 | 42 | `(1-E^{(1)})S` | `E^{(1)}S=E^{(1)}` |
| 88 | 38 | 45 | `S\in\Gg` | `\frakp` |
| 89 | 38 | 45 | `E^{(1)}S=E^{(1)}` | `n` |
| 90 | 41 | 45 | `\frakp` | `[\Gg]_{\frako_\frakp}` |
| 91 | 41 | 47 | `n` | `[\Gg]_{\frako_\frakp}` |
| 92 | 41 | 47 | `[\Gg]_{\frako_\frakp}` | `\frakp` |
| 93 | 43 | 47 | `[\Gg]_{\frako_\frakp}` | `a_i` |
| 94 | 43 | 47 | `\frakp` | `a=\sum a_i` |
| 95 | 43 | 51 | `a_i` | `K/k` |
| 96 | 43 | 51 | `a=\sum a_i` | `\Gg` |
| 97 | 47 | 51 | `K/k` | `z^S` |
| 99 | 47 | 51 | `z^S` | `S` |
| 101 | 47 | 51 | `S` | `K` |
| 102 | 47 | 51 | `\Gg` | `K/k` |
| 103 | 47 | 51 | `K` | `k` |
| 104 | 47 | 51 | `\Gg` | `k` |
| 105 | 47 | 51 | `K/k` | `\Gg` |
| 106 | 47 | 51 | `k` | `K/k` |
| 107 | 47 | 51 | `k` | `(\Gg)_k` |
| 108 | 47 | 52 | `K/k` | `         z\Bigl(\sum_i S_i c_i\Bigr)=\sum_i z^{S_i}c_i,         \qquad z\in K,\; S_i\in\Gg,\; c_i\in k. ` |
| 109 | 47 | 58 | `(\Gg)_k` | `K/k` |
| 110 | 48 | 58 | `         z\Bigl(\sum_i S_i c_i\Bigr)=\sum_i z^{S_i}c_i,         \qquad z\in K,\; S_i\in\Gg,\; c_i\in k. ` | `(\Gg)_k` |
| 111 | 54 | 58 | `(\Gg)_k` | `K/k` |
| 112 | 54 | 58 | `K/k` | `[\Gg]_\frako` |
| 113 | 54 | 58 | `[\Gg]_\frako` | `\frakO/\frako` |
| 115 | 54 | 61 | `\frakO/\frako` | `(\Gg)_k` |
| 117 | 57 | 63 | `(\Gg)_k` | `z^S` |
| 118 | 59 | 63 | `K/k` | `k` |
| 119 | 59 | 63 | `z^S` | `a_1,\ldots,a_n` |
| 120 | 59 | 63 | `k` | `K/k` |
| 121 | 59 | 63 | `a_1,\ldots,a_n` | `u_i` |
| 122 | 59 | 63 | `K/k` | `S` |
| 123 | 59 | 63 | `u_i` | `\Gg` |
| 125 | 59 | 63 | `S` | `u_i` |
| 126 | 59 | 63 | `\Gg` | `k` |
| 127 | 59 | 64 | `u_i` | `         S\longmapsto z^S,         \qquad         \sum_i S_i c_i\longmapsto \sum_i z^{S_i}c_i         \quad(c_i\in k),         \quad\hbox{也即 } ST\longmapsto z^{ST}, ` |
| 129 | 60 | 74 | `         S\longmapsto z^S,         \qquad         \sum_i S_i c_i\longmapsto \sum_i z^{S_i}c_i         \quad(c_i\in k),         \quad\hbox{also } ST\longmapsto z^{ST}, ` | `\frakO/\frako` |
| 130 | 67 | 74 | `k` | `(\Gg)_k` |
| 131 | 70 | 74 | `\frakO/\frako` | `n` |
| 133 | 70 | 74 | `(\Gg)_k` | `\frakO_\frakp/\frako_\frakp` |
| 134 | 70 | 74 | `n` | `(\Gg)_{k_\frakp}` |
| 135 | 70 | 74 | `\frakO_\frakp/\frako_\frakp` | `n` |
| 137 | 70 | 76 | `n` | `(\Gg)_k` |
| 138 | 70 | 76 | `(\Gg)_{k_\frakp}` | `K/k\to(\Gg)_k` |
| 139 | 72 | 76 | `(\Gg)_k` | `[\Gg]_\frako` |
| 140 | 72 | 76 | `K/k\to(\Gg)_k` | `\frakO/\frako` |
| 141 | 72 | 76 | `[\Gg]_\frako` | `(\Gg)_k` |
| 142 | 72 | 76 | `\frakO/\frako` | `n` |
| 144 | 72 | 76 | `n` | `c_i` |
| 145 | 72 | 76 | `(\Gg)_k` | `k_\frakp` |
| 147 | 72 | 76 | `(\Gg)_{k_\frakp}` | `K_\frakp/k_\frakp` |
| 148 | 72 | 76 | `K_\frakp/k_\frakp` | `(\Gg)_{k_\frakp}` |
| 150 | 72 | 76 | `c_i` | `\frakO_\frakp/\frako_\frakp` |
| 151 | 72 | 76 | `k_\frakp` | `[\Gg]_{\frako_\frakp}` |
| 152 | 72 | 76 | `[\Gg]_{\frako_\frakp}` | `K_\frakp/k_\frakp` |
| 153 | 72 | 76 | `\frakO_\frakp/\frako_\frakp` | `k_\frakp` |
| 155 | 72 | 76 | `k_\frakp` | `K/k` |
| 156 | 72 | 79 | `K_\frakp/k_\frakp` | `K/k` |
| 157 | 72 | 79 | `K/k` | `n` |
| 159 | 75 | 79 | `n` | `\frakO_\frakp/\frako_\frakp` |
| 160 | 75 | 81 | `K/k` | `[\Gg]_{\frako_\frakp}` |
| 161 | 75 | 81 | `\frakO_\frakp/\frako_\frakp` | `(\Gg)_{k_\frakp}` |
| 162 | 77 | 81 | `[\Gg]_{\frako_\frakp}` | `n` |
| 164 | 77 | 81 | `n` | `\frakO_\frakp/\frako_\frakp` |
| 165 | 77 | 81 | `(\Gg)_{k_\frakp}` | `W[\Gg]_{\frako_\frakp}` |
| 166 | 77 | 81 | `\frakO_\frakp/\frako_\frakp` | `\frako_\frakp` |
| 167 | 77 | 81 | `W[\Gg]_{\frako_\frakp}` | `WS_i` |
| 168 | 77 | 81 | `\frako_\frakp` | `w` |
| 169 | 77 | 81 | `WS_i` | `W` |
| 170 | 77 | 81 | `w^{S_i}` | `\frakO_\frakp/\frako_\frakp` |
| 171 | 77 | 81 | `\frako_\frakp` | `w^{S_i}` |
| 173 | 77 | 81 | `w` | `\frako_\frakp` |
| 174 | 77 | 81 | `W` | `n` |
| 175 | 77 | 81 | `\frakO_\frakp/\frako_\frakp` | `w^{S_i}` |
| 176 | 77 | 81 | `n` | `\frakO_\frakp/\frako_\frakp` |
| 177 | 77 | 83 | `w^{S_i}` | `\frakp` |
| 178 | 77 | 83 | `\frakO_\frakp/\frako_\frakp` | `n` |
| 179 | 79 | 83 | `\frakp` | `\frakO_\frakp/\frako_\frakp` |
| 180 | 79 | 86 | `n` | `(\Gg)_k` |
| 181 | 79 | 86 | `\frakO_\frakp/\frako_\frakp` | `K/k` |
| 182 | 82 | 86 | `(\Gg)_k` | `K` |
| 183 | 82 | 86 | `K/k` | `k` |
| 184 | 82 | 86 | `K` | `k` |
| 186 | 82 | 86 | `k` | `n` |
| 187 | 82 | 88 | `k` | `K/k` |
| 188 | 82 | 88 | `n` | `\Gg` |
| 190 | 84 | 88 | `\Gg` | `K/k` |
| 191 | 84 | 88 | `K/k` | `K_Z/Z` |
| 192 | 84 | 90 | `K/k` | `Z` |
| 193 | 84 | 90 | `K_Z/Z` | `k` |
| 194 | 86 | 90 | `Z` | `K_Z/Z` |
| 195 | 86 | 90 | `k` | `Z` |
| 196 | 86 | 90 | `K_Z/Z` | `K/k` |
| 198 | 86 | 90 | `K/k` | `K` |
| 199 | 86 | 90 | `K_Z` | `k` |
| 200 | 86 | 90 | `Z` | `K_Z/Z` |
| 201 | 86 | 90 | `K` | `K_Z` |
| 202 | 86 | 92 | `k` | `(\Gg)_k` |
| 203 | 86 | 92 | `K_Z/Z` | `(\Gg)_Z` |
| 204 | 88 | 94 | `(\Gg)_k` | `v_1,\ldots,v_l` |
| 205 | 88 | 94 | `(\Gg)_Z` | `S\mapsto \bar S` |
| 206 | 88 | 95 | `(\Gg)_k` | `         \begin{pmatrix}\vdots\\ v_i^S\\ \vdots\end{pmatrix}         =\bar S\begin{pmatrix}\vdots\\ v_i\\ \vdots\end{pmatrix}. ` |
| 207 | 88 | 106 | `(\Gg)_Z` | `K/k` |
| 208 | 90 | 108 | `v_1,\ldots,v_t` | `w^S` |
| 209 | 90 | 108 | `S\mapsto \bar S` | `\Delta` |
| 210 | 91 | 109 | `         \begin{pmatrix}\vdots\\ v_i^S\\ \vdots\end{pmatrix}         =\bar S\begin{pmatrix}\vdots\\ v_i\\ \vdots\end{pmatrix}. ` | `         D=\bigl\|w^{ST^{-1}}\bigr\|,\qquad S,T\in\Gg ` |
| 211 | 102 | 112 | `K/k` | `D` |
| 213 | 104 | 112 | `\Delta` | `x_S` |
| 214 | 105 | 115 | `     D=\bigl\|w^{ST^{-1}}\bigr\|;\qquad S,T\in\Gg. ` | `         D=D_1^{f_1}\cdots D_t^{f_t},         \qquad         M=f_1M_1+\cdots+f_tM_t ` |
| 215 | 108 | 120 | `D` | `S\mapsto\bar S` |
| 216 | 108 | 120 | `w^S` | `M_\lambda` |
| 217 | 108 | 120 | `x_S` | `\bar S` |
| 218 | 111 | 121 | `         D=D_1^{f_1}\cdots D_t^{f_t}         \qquad\hbox{bzw.}\qquad         M=f_1M_1+\cdots+f_tM_t ` | `         M_\lambda=\sum_S w^S\bar S,         \qquad         M_\lambda^{T^{-1}}=\sum_S w^{ST^{-1}}\bar S           =\sum_R w^R\bar R\bar T=M_\lambda\bar T, ` |
| 219 | 116 | 128 | `S\mapsto\bar S` | `         D_\lambda^{T^{-1}}=D_\lambda\|\bar T\|=D_\lambda\varepsilon_T. ` |
| 220 | 116 | 131 | `M_\lambda` | `D_\lambda` |
| 221 | 116 | 131 | `\bar S` | `\varepsilon_T` |
| 222 | 117 | 131 | `         M_\lambda=\sum_S w^S\bar S,         \qquad         M_\lambda^{T^{-1}}=\sum_S w^{ST^{-1}}\bar S           =\sum_R w^R\bar R\bar T=M_\lambda\bar T, ` | `\bar T` |
| 223 | 124 | 131 | `         D_\lambda^{T^{-1}}=D_\lambda\|\bar T\|=D_\lambda\varepsilon_T. ` | `\Gg` |
| 225 | 127 | 131 | `\varepsilon_T` | `\sum w^S\chi_\lambda(S)` |
| 226 | 127 | 133 | `\bar T` | `D_\lambda` |
| 227 | 127 | 133 | `\Gg` | `K_\frakp/k_\frakp` |
| 228 | 127 | 133 | `D_\lambda` | `k_\frakp` |
| 229 | 127 | 133 | `\sum w^S\chi_\lambda(S)` | `x_S` |
| 230 | 129 | 133 | `D_\lambda` | `w^S` |
| 231 | 129 | 133 | `K_\frakp/k_\frakp` | `K_\frakp` |
| 232 | 129 | 135 | `k_\frakp` | `\lambda,\bar\lambda` |
| 233 | 129 | 136 | `x_S` | `         D_\lambda^{T^{-1}}=D_\lambda\varepsilon_T,         \qquad         D_{\bar\lambda}^{T^{-1}}=D_{\bar\lambda}\varepsilon_T^{-1}; ` |
| 234 | 129 | 141 | `w^S` | `x_S` |
| 235 | 129 | 141 | `K_\frakp` | `\lambda,\bar\lambda` |
| 236 | 131 | 141 | `\lambda,\bar\lambda` | `x_S` |
| 237 | 132 | 143 | `         D_\lambda^{T^{-1}}=D_\lambda\varepsilon_T,         \qquad         D_{\bar\lambda}^{T^{-1}}=D_{\bar\lambda}\varepsilon_T^{-1}; ` | `\Delta_\lambda=D_\lambda D_{\bar\lambda}` |
| 238 | 137 | 143 | `x_S` | `\lambda` |
| 239 | 137 | 144 | `\lambda,\bar\lambda` | `         \Delta_\lambda^T=\Delta_\lambda         \qquad\hbox{对所有 }T\hbox{ 属于 }\Gg; ` |
| 240 | 137 | 148 | `x_S` | `P` |
| 241 | 139 | 148 | `\Delta_\lambda=D_\lambda D_{\bar\lambda}` | `k_\frakp` |
| 242 | 139 | 149 | `\lambda` | `         (K_\frakp)_P=(K_\frakp)_\mathfrak P e^{S_1}+\cdots+(K_\frakp)_\mathfrak P e^{S_r} ` |
| 243 | 140 | 152 | `         \Delta_\lambda^T=\Delta_\lambda         \qquad\hbox{für alle }T\hbox{ aus }\Gg; ` | `(K_\frakp)_\mathfrak P e^{S_i}/Pe^{S_i}` |
| 244 | 144 | 152 | `P` | `\frakp` |
| 245 | 144 | 152 | `k_\frakp` | `e^{S_i}` |
| 246 | 145 | 152 | `         (K_\frakp)_P=(K_\frakp)_P e^{S_1}+\cdots+(K_\frakp)_P e^{S_r} ` | `\Delta_\lambda^T=\Delta_\lambda` |
| 247 | 148 | 152 | ` (K_\frakp)_P e^{S_i}/Pe^{S_i}` | `\Delta_\lambda` |
| 248 | 148 | 152 | `\frakp` | `i` |
| 249 | 148 | 152 | `e^{S_i}` | `Pe^{S_i}` |
| 250 | 148 | 152 | `\Delta_\lambda^T=\Delta_\lambda` | `\gamma_i e^{S_i}` |
| 251 | 148 | 152 | `i` | `\gamma_i` |
| 252 | 148 | 152 | `\Delta_\lambda` | `P` |
| 253 | 148 | 152 | `Pe^{S_i}` | `e^{S_i}` |
| 254 | 148 | 152 | `\gamma_i e^{S_i}` | `\gamma_i` |
| 255 | 148 | 152 | `\gamma_i` | `\Delta_\lambda=\gamma\sum e^{S_i}=\gamma` |
| 257 | 148 | 152 | `e^{S_i}` | `\Delta_\lambda` |
| 258 | 148 | 152 | `\gamma_i` | `\lambda` |
| 259 | 148 | 155 | `\Delta_\lambda=\gamma\sum e^{S_i}=\gamma` | `         \Delta=\Delta_1^{f_1}\cdots\Delta_t^{f_t} ` |
| 260 | 148 | 160 | `P` | `\Delta_\lambda` |
| 261 | 148 | 160 | `\Delta_\lambda` | `k` |
| 262 | 148 | 160 | `\lambda` | `\Delta_\lambda` |
| 263 | 151 | 163 | `         \Delta=\Delta_1^{f_1}\cdots\Delta_t^{f_t} ` | `k` |
| 264 | 156 | 163 | `\Delta_\lambda` | `K/k` |
| 265 | 156 | 163 | `k` | `l` |
| 267 | 159 | 163 | `k` | `K/k` |
| 269 | 159 | 165 | `l` | `\frakp` |
| 270 | 159 | 165 | `\Delta_\lambda` | `k_\varepsilon` |
| 271 | 159 | 165 | `K/k` | `l` |
| 272 | 161 | 165 | `\frakp` | `K_\varepsilon` |
| 273 | 161 | 165 | `K/k` | `K_\varepsilon` |
| 275 | 161 | 165 | `l` | `K` |
| 276 | 161 | 165 | `K_\varepsilon` | `\frakp` |
| 277 | 161 | 166 | `K_\varepsilon` | `         (p)=\frakp_1\cdots\frakp_{l-1},         \qquad         \frakp_i=\frakP_i^{\,l}, ` |
| 278 | 161 | 171 | `k_\varepsilon` | `\frakp_i` |
| 279 | 161 | 171 | `K` | `k_\varepsilon` |
| 280 | 161 | 171 | `\frakp` | `\frakP_i` |
| 281 | 162 | 171 | `         (p)=\frakp_1\cdots\frakp_{l-1},         \qquad         \frakp_i=\mathfrak P_i^{\,l}, ` | `K_\varepsilon` |
| 282 | 167 | 172 | `\frakp` | `         (\Omega_\lambda)=\frakP_1^{r_1}\cdots\frakP_{l-1}^{r_{l-1}},         \qquad         (\Omega_{\bar\lambda})=         \frakP_1^{l-r_1}\cdots\frakP_{l-1}^{l-r_{l-1}}, ` |
| 283 | 167 | 178 | `k_\varepsilon` | `r_1,\ldots,r_{l-1}` |
| 284 | 167 | 178 | `\mathfrak P` | `1,\ldots,l-1` |
| 285 | 167 | 178 | `K_\varepsilon` | `\Omega_\lambda` |
| 286 | 168 | 178 | `         (\Omega_\lambda)=\mathfrak P_1^{r_1}\cdots\mathfrak P_{l-1}^{r_{l-1}},         \qquad         (\Omega_{\bar\lambda})=         \mathfrak P_1^{l-r_1}\cdots\mathfrak P_{l-1}^{l-r_{l-1}}, ` | `D_\lambda` |
| 287 | 174 | 179 | `r_1,\ldots,r_{l-1}` | `         (\Delta_\lambda)=(D_\lambda D_{\bar\lambda})         =(\Omega_\lambda\Omega_{\bar\lambda})         =\frakP_1^{l}\cdots\frakP_{l-1}^{l}         =\frakp_1\cdots\frakp_{l-1}=(p); ` |
| 288 | 174 | 185 | `1,\ldots,l-1` | `K/k` |
| 289 | 174 |  | `\Omega_\lambda` | `` |
| 290 | 174 |  | `D_\lambda` | `` |
| 291 | 175 |  | `         (\Delta_\lambda)=(D_\lambda D_{\bar\lambda})         =(\Omega_\lambda\Omega_{\bar\lambda})         =\mathfrak P_1^{l}\cdots\mathfrak P_{l-1}^{l}         =\frakp_1\cdots\frakp_{l-1}=(p); ` | `` |
| 292 | 181 |  | `K/k` | `` |

No external, native-review, or source-owner validation is claimed.
