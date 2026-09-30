# D016: source-chain check of E03 and E09

Editorial audit by OpenAI Codex — GPT-6 Astra, Ultra effort. This is not an author-issued erratum or a full-paper acceptance.

Authority: the preserved 97-page witness of *Les constantes des équations fonctionnelles des fonctions L*, SHA-256 `F151A9A6B71CCFED11466494493552E4134112D68EF76C7B25C0816A4FFEAD56`. Physical pages 21–23, 61–65, 75–76, 80, 82–86 and 91 were inspected as rendered source pixels. Printed pagination is physical pagination plus 500. The source and revision03 remain unchanged.

## E03: the actual cohomological action, not only a commuting square

Source 2.2.2(b), physical21, makes the tame-character map equivariant with target the Tate module. Source 2.2.3, physical22, defines geometric Frobenius as the inverse of arithmetic Frobenius. Thus on the pro-ell tame quotient, geometric F satisfies F sigma F^{-1} = sigma^{1/q}. Here ell does not divide q. Source 2.3, physical23, independently fixes the Tate eigenvalue q^{-1}.

Put W=V^{P'}, as on physical84. The inertia complex is [W --(1-sigma)--> W], in degrees zero and one (10.7.1, physical85). To determine the degree-one action, let c be a continuous crossed homomorphism, with c(gh)=c(g)+g c(h). Transport gives

\[
 (Fc)(\sigma)=F\,c(F^{-1}\sigma F)
 =F\,c(\sigma^q)
 =F\left(\sum_{i=0}^{q-1}\sigma^i\right)c(\sigma)
 =\left(\sum_{i=0}^{q-1}\sigma^{i/q}\right)F c(\sigma).
\]

Changing the sign used to identify crossed homomorphisms with the complex whose differential is 1-sigma does not change this operator. Hence B=F sum sigma^i=(sum sigma^{i/q})F is the transported cohomological action. It is not chosen merely because it satisfies a chain-map equation. Indeed B(1-sigma)=(1-sigma)F. For trivial inertia B=qF, in agreement with the **source's own** H^1=W_I(-1) in (7.11.3), physical62.

The ratio (1-sigma)/(1-sigma^{1/q}) denotes this finite sum. Neither numerator nor denominator is inverted. In the torsion coefficient setting of §10, sigma has ell-power order on a finite generating set; the sum is a unit since its augmentation q is a unit and sigma-1 is nilpotent. In the complete lattice setting of 7.11.5–6 the same argument applies modulo the maximal ideal and then lifts. The corrected maps are thus automorphisms in the settings used here.

Verdict: E03's revision03 operator, diagram, determinant and local Euler factor have the correct geometric-Frobenius convention. The source's physical86 formula uses the arithmetic exponent despite explicitly naming geometric Frobenius. The correction remains an identified mathematical emendation.

## E09: determinant inversion

For a perfect complex C and an invertible endomorphism u, source (10.3.4–5), physical82, gives

\[
 \det(1-ut,C)=\det(-ut,C)\det(1-\check u t^{-1},D(C)).
\]

Source (10.4.1–2), physical82–83, identifies Z with the **inverse** of the alternating determinant. Taking inverses in the preceding identity, and applying the source's Poincare duality (10.5.1), gives precisely the inverse multiplier in (10.5.2). Applying D(j_!G)=Rj_*D(G) gives (10.6.2), whose printed inverse is visible on physical84. The even shift [2] does not change alternating parity. Therefore the multiplier identified with the local epsilon product in 10.12.1 must be det(-Ft,R Gamma(j_![chi]))^{-1}, not the un-inverted printed determinant on physical91.

The constant sheaf on P^1 checks the direction without a sign convention guess. Its eigenvalues in even degrees are 1,q; Z(t)=1/((1-t)(1-qt)). The dual Tate-twisted value at t^{-1} is 1/((1-t^{-1})(1-q^{-1}t^{-1})). Their ratio is (qt^2)^{-1}; the cohomological determinant itself is qt^2. This check applies in the universal rational-function ring; accidental coincidences after special reductions do not repair the printed formula.

The local-product identification still uses the source's functional-equation theorem and its characteristic-zero reduction in 10.12.1. This audit checks the inverse and its compatibility; it does not reprove all local epsilon-factor theory. E10's use of this inverse is consistent with the checked source chain.

## Newly exposed inherited conflicts: substantive repair required

The source comparison found linked occurrences outside physical82–97. They are present in both revision03 languages and cannot be called cleared by its scoped audit:

1. Physical63, 7.11.5: the printed F(sum sigma^i)^{-1} contradicts the cochain calculation and the printed H^1 twist. Use F(sum sigma^i). The inherited sum's index 0 through q-1 is consistent with the printed assertion that its sole residual eigenvalue is q.
2. Physical61,64,75,80: 7.11(iii), 7.11.8 and its local identity, 9.3.1, 9.9.1–2 use pt^{-1}. Under the fixed geometric convention, absorbing the Tate twist into the variable gives p^{-1}t^{-1}: at a degree-d place its factor is q^{-1}t^{-d}. This is an editorial correction of visible source readings, not an OCR restoration.
3. Physical64, 7.11.8: the ramified dual must be V^*. Physical76, 9.3.2: the right factor must be Z(Rj_*W^*,p^{-1}t^{-1}). Both printed displays omit required dual/substitution data. Source 10.6.2 supplies the explicit dual Tate formulation.
4. Physical64, the subsequent simplified determinant identity: H^1(I,omega_1 V^*) is dual to H^0(I,V) by the printed 7.11.4. If A is F on H^0, the identity is det(1-A)=det(-A)det(1-A^{-1}). Thus the left side should contain F, not the printed F^{-1}.

These are four linked editorial decisions, not four new theorems attributed to Deligne. A staged revision must disclose all occurrences and retain the unchanged witness. No whole-paper acceptance follows. Other inherited text, including the quotient-group choice in the subsequent reduction argument, still requires independent review.

## Executed checks and boundary

`CHECK_RECEIPT.json` records 21 exact regular-representation matrix cases, the alternating determinant identity in three parity degrees, and the P^1 rational-function identity. These finite tests supplement the uniform derivations above. All 17 source render identities are retained locally. The next action is to repair the mapped convention conflicts in both staged languages, build under the global mutex, review changed pages and replay the exact source patch before continuing the remaining full-paper audit.
