# Hi Claude — this is Codex; here is stuff I noticed that you may want to know about

I checked current-rescribe idx589--597 while synchronizing the English of
SGA6, Exposé X, §7.13--§7.15. I did not alter your French workpass. These
are handoff notes so that the source-control lane can decide what to correct,
what to retain as a source sic, and what to ledger as an editorial caveat.

## Witness discontinuities

The declared low-resolution scan
`C:\Users\Floris\Documents\Papors\OS\sga6.pdf`
(SHA-256
`5194436E290B8FCA54BACD5FF672588335408F1AAD3AE07D62BBA68DF35E3D76`)
omits these printed pages:

| Current idx | Printed page | Low-res PDF | Complete high-res PDF |
|---:|---:|---:|---:|
| 593 | 580 | ABSENT | 594 |
| 595 | 582 | ABSENT | 596 |
| 596 | 583 | ABSENT | 597 |
| 597 | 584 | ABSENT | 598 |

The complete supplemental witness is
`C:\Users\Floris\Documents\Papors\OS\Théorie des Intersections et Théorème de Riemann-Roch.pdf`
(SHA-256
`73FBBAD41340C12ECCDCFCF6C3A1656953FE3D712AA8E391678458CCD17B4BAA`,
720 pages, 360 dpi; Internet Archive item `theoriedesinters0225bert`). Its
zero-based PDF page index equals the current rescribe index. The low-res scan
jumps from printed page 579/PDF586 to printed page 581/PDF587, then to
printed page 585/PDF588.

## Clear formula, label, or cross-reference defects

1. **idx589, (7.13.2):** bottom right is printed and transcribed as
   `K^{2i}(X_s, Z_l(i))`. The target of `c^i`, the opposite node, and the
   entire discussion require `H^{2i}(X_s, Z_l(i))`.
2. **idx590, §7.13.3:** the residue-field parenthesis refers to the normal
   closure of undefined `V` in `Kbar`. The established valuation ring is `A`
   (§7.2 and again §7.16). I used `A`, but this deserves an explicit source
   correction rather than a silent change.
3. **idx593, Remark 7.13.11:** the schematic-closure construction is cited as
   `(cf. 7.15)`. It is defined in §7.14; §7.15 varies the trait. I used
   `(cf. 7.14)` in English.
4. **idx594, Remark 7.13.13:** the final reference says `7.11.5`, but the
   conjecture actually invoked is in 7.12.5. I used `7.12.5` in English.
5. **idx596, §7.14:** immediately after
   `Z_bullet(T) -> Gr_bullet(T)`, the source says `si Z est quasi-projectif et
   lisse`. I read the intended scheme as `T`; please check whether you prefer
   `T` or a literal source sic.
6. **idx597, §7.15 cube:** the rear fiber-immersion labels are swapped. The
   generic open immersion `X'_{t'} -> X'` must be `j_{X'}` and the special
   closed immersion `X'_{s'} -> X'` must be `i_{X'}`.
7. **idx597, (7.15.1):** both horizontal arrows are printed/transcribed
   `sigma_X`. The bottom specialization homomorphism has source and target
   belonging to `X'`, hence must be `sigma_{X'}`.

## Authorial mathematical caveats — please do not silently rewrite

1. **idx596, final paragraph of §7.14:** the source asks for a same-index
   restriction `A_i(X) -> A_i(X_s)`. Since §7.2 makes `X_s -> X` a regular
   immersion of codimension one and §7.14 defines `A_i` by absolute
   dimension, a Chow/Gysin restriction should lower degree:
   `A_i(X) -> A_{i-1}(X_s)` (equivalently, reindexed for specialization,
   `A_{i+1}(X) -> A_i(X_s)`). This appears to be an authorial index slip in a
   speculative paragraph, not a transcription error. My current English
   retains the printed map and ledgers the caveat.
2. **idx597, closing sentence of §7.15:** regularity of only `X_s` and `X_t`
   does not by itself guarantee regularity after arbitrary residue-field
   extensions to `X'_{s'}` and `X'_{t'}`; geometric regularity would. The
   `Gr^bullet` formulation also inherits separatedness conditions from
   §7.7. I retained the authorial sentence source-faithfully and flag it only
   for editorial review.

## Smaller transcription/style observations

- idx590: the scan has `(SGA 4 VII 5.8)`; inherited English had `VIII`.
- idx593: the scan has `que ce trouve` (intended `se trouve`) and singular
  `définie` after plural `homomorphismes`; harmless grammatical normalization
  is needed in translation.
- idx591/592: the vertical isomorphism glyphs in (7.13.4) and (7.13.10) are
  scan-style vertical squiggles; `\sim` in the workpass is a reasonable
  semantic normalization, but the side placement differs between the two
  diagrams.
- idx592: the local symbols really are `cl`, `x^{(i)}`, `Filt^i`, and an
  upward right-hand arrow in (7.13.9). The inherited English corrupts several
  of these.

Thanks — I hope this saves a round of source archaeology. The English lane
has exact rendered witnesses and ledgers if you need them.
