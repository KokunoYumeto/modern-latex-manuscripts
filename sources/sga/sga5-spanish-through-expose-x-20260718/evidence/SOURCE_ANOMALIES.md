# Frozen-source anomalies

Authority: `sga5_fr_workpass.tex`, SHA-256 `791F4EFFC5E02832D5D77ED03518C8156D6F07E4C8238B03545DB93D883FBB28`.

These notes document authority-level defects without silently changing the Spanish target.

## Exposé VII, Corollary 7.4 (lines 10517--10538)

Formula (7.4.2) is derived by invoking 7.2, but the frozen wording of Corollary 7.4 states only that `X` is proper and that `L` is invertible. The derivation additionally needs the preceding hyperplane-section hypotheses (in this codimension-one setting: `X` projective, `L` ample, and `Y` a smooth hyperplane section). Under the literal weaker wording, (7.4.2) is false; for example, take `X = P^1 x P^1` and let `Y` be two disjoint fibers cut out by a transverse section of `O(2,0)`. The Spanish target faithfully preserves the authority wording. The unit passed exact formula/structure parity with source-slice SHA-256 `6B084F5A5349D52A98FC6C891CE5F36BA8A982D1F0996F355F7CE4FD0FB123CE` and target SHA-256 `CC05B6862D86272482034D4CFA411EF3B1DA375E1CBA8AE9297B07A9C4471028`.

## Exposé VII, Lemma 8.4.1 (lines 10716--10744)

The statement is `p_*(c_{d-1}(check F)) = 1`, but the proof computes `c_{d-1}(F)` in (8.4.2) and then says that applying `p_*` proves the lemma. Direct pushforward of (8.4.2) gives `p_*c_{d-1}(F) = (-1)^{d-1}`. The stated result additionally uses the omitted identity `c_{d-1}(check F) = (-1)^{d-1}c_{d-1}(F)`. Later formulas consistently use the checked bundle, confirming the intended statement. The Spanish target preserves both authority formulas and does not silently supply the missing step. Source-slice SHA-256: `D21BA8F4C6827928AE512BAD9D0B62628DD71D55057EE7BA851C3EE4FB437441`; target SHA-256: `F546122E708DD38D15A2E1FDF0F1DFB8243377354EA9F48EB104A3018D3B19D6`.

## Exposé VII, Lemma 8.4.3 (lines 10746--10792)

The certified scan omits the prime in the upper-right node of diagram (8.4.5), printing `H^{p+2d}(Y)`; the frozen TeX authority deliberately has `H^{p+2d}(Y')`. The primed node is forced by the horizontal map `j^*` and the vertical pullback `g^*:H(Y)\to H(Y')`. The Spanish target follows the corrected frozen authority. The final appeal to (8.4.2) also compresses the elementary identity `c_{d-1}(check F)=(-1)^{d-1}c_{d-1}(F)` noted above. Source-slice SHA-256: `8CA79065D3C3AF3175B31202D46BFD932AA9953C82B2535B60AD43F957914675`; target SHA-256: `30FB522A6036D0684FCBB726716195683AF246442B2FA9276D9F8271BC8D1FB8`.

## Exposé VII, proof of Proposition 8.5 (lines 10841--10882)

Two frozen-authority formulas are ill-typed. First, (8.5.4) and its later expansion place `c_{d-1}(check F)` inside the argument of `g^*`, although that class lives on `Y'`; the matrix product requires `g^*(g_*(\cdot))c_{d-1}(check F)`. Second, the authority states `lambda'\circ(lambda\circ lambda')=id`, whereas the left-hand side has type `B\to A` and in fact equals `lambda'` because `lambda'\circ lambda=id_A`. With these evident corrections, both inverse-matrix products and the kernel-image argument are valid. The Spanish target faithfully preserves the frozen formulas and records the defects here. Source-slice SHA-256: `9C88F6D6A3C6FF46CF3B902274CA851455A5E632ECC855866ADF2D6108102827`; target SHA-256: `62FBA05B3B9F73D1ED47E09AE020E5B9510CFD2ECA13B98ABF57AF6432F4B890`.

## Exposé VII, proof of Lemma 9.1 (lines 11028--11055)

Formula (9.1.6) contains the isolated notation `\mathcal O'_P`, which occurs nowhere else in the frozen authority. The certified scan on p. 336 confirms that prime, so the Spanish target preserves it without speculative normalization. In context it denotes the rank-one summand in the displayed top-Chern calculation; the resulting relation `\xi c_r(\check F)=0` and the subsequent Chow decomposition are mathematically consistent. Source-slice SHA-256: `E2BC4C1F0B97DEE508429F80CEA322FBB6AA70F56CAB0F020FE32121DBD2BC80`; target SHA-256: `D68E2015BD1EB39D6646654F215E452D79A9D8ADCD00E5AA80B19BEFBC2329AE`.

## Exposé VII, proof of Lemma 9.3 (lines 11129--11160)

Formula (9.3.7) in both the frozen authority and certified scan prints `(j_1)_*g^*(\mu)`. This is ill-typed there: `g:H\to Y`, whereas `(j_1)_*` takes a class on `\widehat N`. The preceding formulas (9.3.5)--(9.3.6), the diagram, and the following connected-component argument require `g_1^*(\mu)`, with `g_1:\widehat N\to Y`. The Spanish target preserves the authority's `g^*` rather than silently correcting it. Source-slice SHA-256: `CF6B8ED093166B5CD9C9291439B778987F65B35ABAB9B82D5962694FAED28495`; target SHA-256: `DBEF11347A43BE5C07D90AAF9E9C00E83A010D5B7641B9C895AAEA67D178F26F`.

## Exposé VII, proof of Lemma 9.4 (lines 11175--11207)

In the unnumbered reduction, both the frozen authority and certified scan print `c_d(\check E)j_1^*(j_1)_*(y)=c_d(E)j_1^*(j_1)_*g_1^*(a_0)`, with a checked bundle on the left and an unchecked bundle on the right. The projection-formula argument calls for `c_d(\check E)` on both sides; as printed, the equality can differ by `(-1)^d` in odd rank. The subsequent vanishing reduction is unaffected, and the Spanish target preserves the source formula. Declared source-slice SHA-256: `8FD2C65DD26D8BA990C0DF54A477F8068FB3FBF49CF450E63490EC1ADF3D9A6B`; target SHA-256: `1F6602A21450EB98E25FE012D33E02853D88FC49E4A7781AA4B3B435AF1B2DBC`.

## Exposé VII, proof of Theorem 9.2, §9.5 (lines 11231--11266)

The printed complement glyph after `Z` on p. 342 is semantically the open complement `Z\setminus Y`, but the frozen TeX authority represents that source glyph diplomatically as `Z\doteq Y`. The Spanish target preserves the frozen-authority representation rather than silently normalizing it. This does not affect the proof: the strict transform is defined as the closure of the inverse image over the indicated complement. Source-slice SHA-256: `B304BEDD9369E8F3463F0B6874562B89437E7B77A055E9332259BF950A2FD18E`; final target SHA-256: `EFECFE8EEDF792266DB8F2547914EC21800F3D2E49B6ED15FAA77B1B9AA24687`.

## Exposé VII, proof of Theorem 9.9 (lines 11455--11516)

After `a_{d-1}=0`, multiplying `z=\sum_{i=0}^{d-1}g^*(a_i)\xi^i` by `\xi` should leave the final nonzero term `g^*(a_{d-2})\xi^{d-1}`. Both the frozen authority and printed scan instead write `g^*(a_{d-1})\xi^{d-1}`. This is an off-by-one coefficient index; the omitted `\xi^d` term already has zero coefficient because `a_{d-1}=0`, and the intended independence argument remains valid. The Spanish target faithfully preserves the source text. Source-slice SHA-256: `FB886AB865F1A16FC9EAACD68B2C827B782164723C6F137C463BA67390B1B06E`; target SHA-256: `C05880C03D6A73C14FE4F8BB9C96C40A6FDEB6E2C574C5C6BEFDFBB8B6AB7D17`.

## Exposé VIII, proof of Proposition 8.1 (lines 12072--12115)

The frozen authority and printed scan head the second proof as `Démonstration de la proposition 5.2`, although Exposé VIII §5 contains only Proposition 5.1 and the surrounding statement and final sentence identify Proposition 8.1. The proof itself is the proof of 8.1. The Spanish target faithfully retains the printed referent `proposición 5.2` and records the discrepancy instead of silently correcting it. Source-slice SHA-256: `B8A1C028AE55652B2938C77B6E83F5DCB1FBCFC4AA9526E90697C1485FF2584C`; target SHA-256: `F1C12DA5183A85893EB2DF0411409333D858F0E57D63E367E1B36F5C71F4ADD9`.

## Exposé X, proof of Proposition 2.2 (lines 12293--12325)

In the first displayed comparison on printed p.374, the right-hand side is ill-typed as `R\Gamma_X(Rp_*(\Lambda_{V,X}))`; the pushforward is a complex on `Y=X/G`, so the right-hand side must be `R\Gamma_Y(...)`. The frozen TeX authority corrects this and the later repeated equality on printed p.375 already uses `Y`. The Spanish target follows the type-correct frozen authority. Source-slice SHA-256: `68048D8C9A4A05C6AF699384139D396AA40749EFC41D8D86D10B3E787EB8A8DD`; target SHA-256: `7F2D47414B1F8E2B8F6E77DA55627223BA3E0F3F0A7BEFABA5299EA6B005236E`.

## Exposé X, duality action in §3.7 (lines 12434--12472)

Formula (3.7.1) in the printed scan appears as `g_P={}^t(g^{-1})_P`, omitting the check on the module in the left-hand subscript. The formula defines the contragredient action on `\check P`, so the frozen authority's `g_{\check P}` is type-correct. The Spanish target follows the corrected authority. Source-slice SHA-256: `9B8E261247218C663D9AE8A1501D6275CC9E8EB60DEEC2B38006FC4019349C66`; target SHA-256: `A88BA1D38D6C7517C42C299DBA74CE38537FBC2CFAE480D04779397752E62839`.

## Exposé X, Proposition 3.8 explanatory prose (lines 12474--12495)

After (3.8.1), the frozen authority and scan say that the operation on the third term is transported from the operations on `\check P^\bullet` and `\check M^\bullet`, although the displayed third term is `(\check P^\bullet\otimes_\Lambda M^\bullet)^G`. The second factor should therefore be `M^\bullet`, not `\check M^\bullet`. Both numbered formulas are correct. The Spanish target preserves the source's prose-only slip and does not alter the mathematical displays. Source-slice SHA-256: `A08CA2A68E1E845507767F913FEA19A1C6448F77088A80FCF519EE35B6BFD1A1`; target SHA-256: `547A5DE9A48FA9F8A3E10C1330991EEDC4B161050EDE63F7B2F66D6C27E2011E`.

## Exposé X, proof of Corollary 3.9 (lines 12497--12509)

The frozen authority and printed scan cite `(4.3.4)` when replacing the derived tensor expression, but there is no formula 4.3.4 in this context; the immediately preceding relevant identity is (3.8.1). The Spanish target faithfully retains the printed cross-reference and marks it in the TeX rather than silently renumbering it. Source-slice SHA-256: `35A18577D73AEEBA8431FE132B3FA3013E29473F3A57A3181A4BA961C630476A`; target SHA-256: `4C790B09BB25F21BCC79DCF8047712D8B6620D4C848C32E7B0FEDB7B89220DB9`.

## Exposé X, Lemma 4.1 graph and diagonal maps (lines 12511--12540)

The printed scan conflates the symbols for the diagonal immersion and the graph immersion in its local-ring calculation. The geometry and the pullback formulas force `\delta(x)=(x,x)`, `\gamma(x)=(x,g(x))`, `\delta^*(a\otimes b)=ab`, and `\gamma^*(a\otimes b)=a\,g^*(b)`. The frozen authority and Spanish target use these type-correct symbols. Source-slice SHA-256: `799A62AEC4534BE9BB4A8DCC1A1E0B52910F35870E44284972CECFC8D166C834`; target SHA-256: `D48D11F00177EB8F661B33BAD36C6C90D0EC9A30A103A8B3E5F0A43B5729FEA9`.

## Exposé X, §4.2 fixed-point reference and formula (4.2.3) (lines 12542--12619)

The authority and scan call the fixed-point multiplicity result `lemme 5.1`, although the result just proved is Lemma 4.1; the Spanish target retains and marks that printed reference. More materially, (4.2.3) prints `Sw'_{y'}=Sw_{y'}\otimes\mathbb Z_\ell[G_{y'}]`. This cannot have the character prescribed by (4.2.4): equations (4.2.2), (4.2.4), and (4.2.5) force addition of the regular character. The Spanish target therefore corrects the operator to the direct sum `\oplus`, after independent semantic review and 500-dpi scan confirmation of the printed glyph. Later root terminology QA normalized the covering term to canonical `recubrimiento`. Source-slice SHA-256: `75E2C342EEFC11CAD0414C43C4569350AF8929FDA30FE590F5789C5A7F48A2C1`; final target SHA-256: `7B5495D40FAA39D2760870346CD09C35B82CB82088892CA4AD6FCC0BA2956D19`.

## Exposé X, §4.3 transport-of-structure tuple (lines 12621--12635)

In the sentence comparing a second lift `y''` with `y'`, the frozen authority and printed scan say that the situation `(C',y'',G)` is obtained from `(C,y',G)`. Context suggests `(C',y',G)`, since both points lie on `C'`, but the discrepancy is prose-only and the subsequent conjugation and transport-of-structure argument is unambiguous. The Spanish target faithfully retains the source tuple. Source-slice SHA-256: `0C1C4A6E482569734C231836E7CA0990C068C7481ABAE7F5119E5A27BC3F2532`; target SHA-256: `51744F80FE92D3D404A8DE6919FEAC24B1B5A6FD1B46A88EAC9E4E3C477675A8`.

## Exposé X, proof of Proposition 4.4 (lines 12637--12648)

In the final sentence of the proof, the printed scan drops the check and displays the tautological isomorphism `Sw_{y'}\simeq Sw_{y'}`. The preceding contragredient-character calculation and the proposition being proved require `Sw_{y'}\simeq\check{Sw}_{y'}`. The frozen authority and Spanish target restore the check, consistently with the certified source-correction log. Source-slice SHA-256: `96B27430CB9E75AE990ABB4EDED65217B73684F6BDE80B951C0A682FBDA23BA2`; target SHA-256: `32CBBE005EDA1842279C0395C7C73D7DA97A4AE24721B3AC3DF39F6F1BBA3CEF`.

## Exposé X, §4.5 induced-character formulas (lines 12650--12681)

On printed p.387, the scan visibly drops or weakens several primes: it reads `y'_0\in C` where the point must lie in `C'`, begins with an inconsistent `g^*\in G` before using `g'` throughout, and makes some primes in (4.5.2) faint. The fixed-point fibre, conjugacy identity, and induced-character formulas force the primed forms. The frozen authority and Spanish target consistently use `C'`, `g'`, and the fully primed characters. Source-slice SHA-256: `9F1082E86551767C36B299D477F7AA56CF93D44D960FF784703E7E16A133B2B5`; target SHA-256: `EB2BFF645BD6E2CA1642199D1AEABC89E8E8DE73FE95164E1B205C98693CBD37`.

## Exposé X, §4.6 generic-field formula (lines 12683--12695)

The printed scan has a lacuna in the field extension, visibly leaving the argument after `k(` blank before `=K_1`. The component construction uniquely requires `K'_1=k(\eta'_1)\supset k(\eta_1)=K_1`. The frozen authority and Spanish target supply the missing `\eta_1)` and thereby retain a well-formed Galois extension with group `G_{C'_1}`. Source-slice SHA-256: `FCA1C1C873B1E4CEFB010E84BFF1325F8B0BD32DC6FCD3259D20F44375365C1F`; final target SHA-256: `59267CD39C5F83AC15D16629C7752736D9A36C1BF56D2F98F5330D85DDD9E001`.

## Exposé X, Proposition 5.1 statement (lines 12697--12741)

The printed scan contains two type/referent slips. It defines `Y'=p^{-1}(X)` even though `Y=C-U` and the complement upstairs must be `p^{-1}(Y)=C'-U'`; it then says that the first member of `(6.2)` is defined by 2.1 although the displayed formula is `(5.2)`. The frozen authority and Spanish target use the type-correct `Y'=p^{-1}(Y)` and the correct reference `(5.2)`. Root exact-build visual QA also normalized the Spanish term to ledger-established `recubrimiento principal`. Source-slice SHA-256: `EB7DC9B09E3A23FD864595BE4DFA6FC78E55FE8C488E250684CED824AE88F264`; final target SHA-256: `24E42861969F8D03B5E4C79523725EEED425A1A0231E233F66ECD906AAC54F0B`.

## Exposé X, proof of Proposition 5.1, first block (lines 12743--12791)

The authority's citation `(3.3.1)` for injectivity of the trace map is a referent slip: Proposition 3.2 is the trace monomorphism, while (3.3.1) is the induced-character formula. The Spanish target faithfully retains the printed citation. Separately, printed p.391 drops `\mathcal F` from the right-hand side of the inverse-limit identity and uses `\Lambda_\nu` in a class that must lie in `K^\bullet(\Lambda_n[G])`; the frozen authority and target restore `\mathcal F` and the running index `n`. Source-slice SHA-256: `5CC4692BC92028CADCE2DB4F91E3C1D75CE3454AE24A963F10E78C259D31FB26`; target SHA-256: `CA6DFE278CFC783743A76EF541ABC37F9BA425FDAFEA97FF7E45F725253CAAAD`.

## Exposé X, proof of Proposition 5.1, final block (lines 12835--12846)

Printed p.393 cites `(6.2.1)` when comparing with the character formula, but the relevant formula is (5.2.1), and it prints `\sigma'_y(\ell)` in the identity case even though `\ell` is not a group element. The frozen authority and Spanish target use `(5.2.1)` and the identity element `e`, yielding the classical Hurwitz formula with the correct sign and different degree. Source-slice SHA-256: `221CD463873D5AA2C6B38CF878C6C5D4724EAEB225FDB8D7D74D6723C2E44156`; target SHA-256: `7618DFB57DD4E778D985632448B4DFF03B129604405F09D19839099A6A2FC641`.

## Exposé X, §6.1 independence from the trivializing cover (lines 12870--12894)

The printed scan writes `Sw_{G,n}` once in the base-change relation. The same formula's second term is `Sw_{G',x}`, and the following sentence invokes the local character `a_{G,x}`, so the subscript must be the point `x`, not an undefined `n`. The frozen authority and Spanish target use `Sw_{G,x}`. Root terminology QA also normalized every covering occurrence in the unit to canonical `recubrimiento`. Source-slice SHA-256: `4F2A26F0A74FC30267CED44AAEB8A47282E09594D072668132E5C9B97434AEA4`; final target SHA-256: `85AEB9EAAB153B8CBF4DF24AF230141F6388ACD6AD0CE27815FF31BEED315C7A`.

## Exposé X, §6.2 tame local term (lines 12896--12917)

In the tame-ramification sentence, the raw scan appears to abbreviate or misprint the vanishing as `\alpha_x(\Delta)=0`. The defined invariant is `\alpha_x^\Delta(F)`, and its vanishing follows canonically from `Sw_x=0`. The frozen authority and Spanish target retain the fully typed expression `\alpha_x^\Delta(F)=0`, consistent with (6.2.1)--(6.2.3). Source-slice SHA-256: `2A4C413F0C45618ED9C26919DD159738D18D4C7408343AA9C20EE75FF0C03955`; target SHA-256: `63FCD363E7D82406E225C9400864DBDCCE80341EA8D353694540554226249987`.

## Exposé X, Theorem 7.1 hypotheses (lines 12927--12941)

The theorem says that `F` satisfies conditions i) and ii) “of 7.1,” but those conditions are defined in §6.1; §7.1 is the theorem itself. The meaning is unambiguous from the immediately preceding construction and formula (6.2.2). The Spanish target faithfully retains the frozen authority's circular digit reference rather than silently changing it. Source-slice SHA-256: `43926B14525A515FC19E76EED4B65A359F75CDEED6DD56DECCA014CAB54D13F4`; target SHA-256: `409E011BBAE8D87B95E54587B9F03E2487E164FCF206087DC5D7447C020B2954`.

## Exposé X, Corollary 7.12 statement (lines 13086--13109)

The printed scan duplicates an `F` in the coefficient-sheaf passage; the frozen authority removes that duplication and consistently prints `F_\ell`. That notation is itself conservative and somewhat overloaded, but the formulas and the following identification `F_\ell=\mathbb Z/\ell\mathbb Z` make the intended coefficient object clear, so the Spanish target preserves it without speculative modernization. The statement also repeats the source's reference to a category “as in 7.1,” following the same numbering slip documented for Theorem 7.1. Source-slice SHA-256: `308F958C1F0692F83FAFC80AF9083CDD93CE3A9BFE79FB608438EAF44FD1344E`; final target SHA-256: `9D490D838807A2FC32C4FD288B5F989681488698EFDFC858A41C6634BD36E95A`.

## Exposé X, Lemma 7.14 statement (lines 13111--13118)

The statement calls `\eta` “the generic point of `S`,” although `S` is not introduced locally; the surrounding arithmetic setup strongly suggests `S=\Spec R`. The frozen authority and printed scan both contain the undefined `S`, so the Spanish target preserves it rather than silently inserting a conjectural definition. Source-slice SHA-256: `C51B92624F2D41FABA12B16B69B767C89BCD5C8CE4109C323074B8D65E52A045`; target-body SHA-256: `788760524C4370F623F4D533B1F8A007E6D4769FBE6F174B30F3FC592E89E7F7`.

## Exposé X, proof of Lemma 7.14, first block (lines 13120--13140)

The profinite-group sequence in the frozen authority and printed scan ends in `0`, rather than the more usual terminal `1`; the Spanish target preserves the source exactly. The scan's historical spelling `Silov` is standardized to `Sylow` in both the frozen authority and the Spanish target. The Hochschild--Serre reduction, prime-to-`p` quotient and direct-summand argument are otherwise mathematically and typographically complete. Source-slice SHA-256: `50EA423AA3EC42C4D2F541129D2CE90EB3C09E84DFA279C159D11C8213760E67`; target-body SHA-256: `4EF64B62EE93DC348794787028FA8E489776077F7BEAB55386BB6DE2EEEF610E`.

## Exposé X, proof of Lemma 7.14, final block (lines 13141--13161)

The source alternates between `M` and `M^\bullet` while describing the same complex and its components; the Spanish target retains that notation exactly. The printed scan also carries an extra closing parenthesis after the citation to [4], p. 197; the frozen authority balances the parenthetical, and the target follows that unambiguous typographic repair. Source-slice SHA-256: `2678A888C0436F2183AF69B721A6FF79EC4C86CCDF7C26A22CE9FEBDC594B65C`; target-body SHA-256: `DC23B13C68F492A13F32B69487F3B4A27B181E9C8AACF06C8C60F6D7316EE98A`.

## Exposé X, proof of Corollary 7.12 (lines 13163--13229)

The first block preserves the authority's raw `Ri_!`/`Ri_*` notation, unbraced `Q^\bullet|Z` restriction and alternating stalk parentheses. Its Spanish wording was normalized from the calque `esquema localizado estricto` to the adopted technical term `localización estricta` (TERM-061). In the final block, the split boundary sum literally uses `\varepsilon_x^\Delta(F)` although the next sentence expands `\varepsilon_x^\Delta(i_!(F))`; both the frozen authority and printed p.405 show this shorthand, so it is preserved rather than silently regularized. First-block source/target-body SHA-256: `EF353B1794CE1EF92BA34B28E287E81D1848604D17AF484BCE0ED67D3E859980` / `5FCC3F01201732571616FE1BF1C7FE6E8A68AD3F17F4C72EBB4A1DD1E13CF30B`. Final-block source/target-body SHA-256: `666F89E4D161CD97D67E400462A36EB5A3286E981A14C2AA4133C55D20E8549A` / `D5840684D909E430FF1754E56607AA3BCD0DB8180155C1AF6C5F6CEEE2B6B15E`.

## Exposé X references (lines 13231--13239)

Printed p.406 abbreviates the second venue as `Toh.`; the frozen authority expands this to `Tohoku Math. Journal`, and the Spanish target retains that certified expansion. Bibliographic titles remain in their source languages; only the surrounding reference-list labels and publication phrases are localized into Spanish. Source-slice SHA-256: `6CB042D7269313644C30A4FBFB886FFA55E98B9E793CBD63F78EDDD851625DF8`; target-body SHA-256: `D854A2690C6DF3A60274CDEFD24B4BB23DA824E02BB3D3337F1CB17610E50763`.
