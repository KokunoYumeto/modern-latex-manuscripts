# Inherited witness to reconciled Japanese Paper 21

## Inherited boundary

The cumulative Japanese witness has its Paper 21 heading at line 11440 and article closure at 11546. Lines 11547–11568 are setup for Paper 22 and are not part of Paper 21. The witness is not synchronized authority.

## Source-critical changes

- Restored Riemann reference `78)` and Roman `II` in the Heun citation.
- Restored the source's deliberately nonuniform prime family: `f'(dx)` and `\delta f'`, but unprimed Hessian, formula (140), `\partial f/\partial dx_i`, and following prose `f`.
- Restored `h^{(1)}(dx,\delta x)` in the prose after (143).
- Restored all five final `\varrho` glyphs.
- Closed the Christoffel bracketed series.
- Restored source note scope and continuous `149)`–`162)` marker style.
- Preserved all five unnumbered and seven numbered displays with labels `(140)`–`(146)`.

## Japanese terminology changes

- `形式的変分計算` → `形式的変分法`.
- `微分不変量` → `微分不変式` in the historical invariant-expression sense.
- `反変` → source-law-specific `反傾` for `kontragredient`.
- `共変` as an automatic rendering of `kogredient` → explicit `d` or `dx` と同じ変換則に従う.
- `共変微分` remains reserved for `kovariante Ableitung`.
- Added concise source-defined sense guards for the Lagrange expressions/central equation, parallel transport, total divergences, and identity-like dependencies.

These choices are internally reviewed Japanese-lane decisions, not external standardization or community certification.

## Rejected interpretations and candidates

- Rejected the superseded June 28 no-prime source witness after opening the correctly identified July four-page audit.
- Rejected mechanical prime propagation to the Hessian, formula (140), numerator derivative, or prose.
- Rejected treating `反変` and `共変` as a safe one-to-one translation pair for the historical transformation-law terms.
- Rejected the first three-page render because it begins one page-2 line with `って`, splitting `沿って`.
- Source-image diagnostic crops remain local and are not open publication payload.

## Exact post-attestation delta

Independent semantic QA completed on TeX SHA-256 `98A820B396E593B13CBFB4333EC7B8265A061FAD439798F14684AF94D679011A`. The consolidated candidate TeX SHA-256 is `C8766BF85B516A356649AF5C72CC6B0C09FBDA00078C49DE4E47217907F15F42`. Its entire delta is:

1. correct the first-use `\psi_i` gloss from the full Euler–Lagrange left side to one half of that left side under the displayed normalization `2\psi_i=...`;
2. restore the source-local reference order `Vermeil\textsuperscript{92)}` then `E. Noether\textsuperscript{93)}`;
3. restore the source's emphatic exclamation after `p(d,d)=0` no longer arises from a variational problem;
4. improve the editorial parallel-transport sense window from `接続に沿う` to `接続によって定まる`;
5. restore source display punctuation at the checked Euler–Lagrange, central-identity, quadratic, `(141)`, first-kind-symbol, `(142)`, `(144)`, and `(145)` endings;
6. insert six minimal `ラグランジ\nolinebreak[4]ュ` controls and one `沿\nolinebreak[4]って` control.

An in-memory inverse of exactly these changes reproduces SHA-256 `98A820B3…011A`; no other mutation exists between the attested and consolidated snapshots.
