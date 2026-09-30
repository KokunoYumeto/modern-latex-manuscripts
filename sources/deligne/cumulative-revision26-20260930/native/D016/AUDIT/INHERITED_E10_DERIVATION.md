# D016 revision03: independent check of E10

Status: scoped editorial derivation, not full-paper acceptance and not an author-issued erratum. Audit written by OpenAI Codex — GPT-6 Astra, Ultra effort. Earlier transcription and translation are inherited; this attribution does not assign their authorship to this audit.

## Source and conventions

P. Deligne, *Les constantes des équations fonctionnelles des fonctions L*, LNM 349 (1973), pp. 501–597. The retained 97-page comparison witness has SHA-256 `F151A9A6B71CCFED11466494493552E4134112D68EF76C7B25C0816A4FFEAD56`. Physical page numbers below are printed page numbers minus 500. Source pixels inspected for this calculation: 23, 27, 28, 50, 55, 86, 91, 92.

The target is equation (10.13.2), physical92. Its printed positive conductor sum is a transcription restoration. Replacing the second sum's q_v by q_v^{-1}, the Gauss-sum minus by plus, and the exponent 1+n_v by -1-n_v are explicitly editorial emendations. They are not reported as literal readings of the scan.

Retain the source's hypotheses: characteristic p global function field, ell different from p, a continuous additive idèle-class character alpha with values in Z/ell^m, and chi=1+epsilon alpha, epsilon^2=0. Extend coefficients by a primitive p-th root as in §10.13. At a place put q=#k, n=n(psi), a=alpha(pi), c=alpha(-1), r=q^{-1}, z=t^{deg(v)}. The character on units factors through k*; hence (q-1)alpha(u)=0 and 2c=0. Division by 2 in the coefficient ring is never used.

Prerequisites retained explicitly: E03 uses geometric Frobenius on the inertia complex, with degree-one operator B=(sum_{i=0}^{q-1} sigma^{i/q})F. E09 uses the inverse determinant as the multiplier in (10.7.4). This note checks the consequences of those conventions; it does not replace their complete source-chain audits.

## 1. Conductor shell and local epsilon ratio

Definition3.4 (physical27) makes n the largest integer for which psi is trivial on pi^{-n}O. Therefore

\[
 \bar\psi(x)=\psi(\pi^{-1-n}\widetilde x)
\]

is a well-defined nontrivial additive residue-field character. Changing a lift adds an element of pi^{-n}O. Its sum on k* is -1; this identity remains valid over the specified coefficient extension because p is invertible there.

Formula3.4.3.4 (physical28), reiterated in5.8.2 (physical50) and extended to coefficient rings in6.4 (physical55), integrates chi^{-1}psi on the shell pi^{-1-n}O*. Put T=sum_{x in k*}alpha(x)barpsi(x). On that shell,

\[
 \chi^{-1}(\pi^{-1-n}\widetilde x)
 =1+\epsilon((n+1)a-\alpha(x)).
\]

The common measure factor cancels in the ratio to the trivial character. Summing and dividing by -1 gives

\[
 \frac{\varepsilon_0(\chi,\psi,dx)}{\varepsilon_0(1,\psi,dx)}
 =1+\epsilon((n+1)a+T).
\]

The common unramified omega^t factor also cancels on this valuation shell. Outside S, the unramified formula5.9 gives coefficient n a instead. Thus the global epsilon-ratio coefficient is R+sum_{v in S}a_v, where R=sum_v n_v a_v+sum_v T_v; T_v=0 outside S.

## 2. Ramified dual local factor, including ell=2

Source2.3 (physical23) identifies geometric Frobenius with a uniformizer and the Tate character with the local absolute value. Thus on the dual Tate character F=r(1-epsilon a). Write sigma=1-epsilon b for its tame inertia action. Since q is invertible,

\[
 B=\left(\sum_{i=0}^{q-1}\sigma^{i/q}\right)F
   =1-\epsilon\left(a+q^{-2}\binom q2 b\right).
\]

For odd q, c=((q-1)/2)b and (q-1)c=0, so q^{-2}binom(q,2)b=q^{-1}c=c. For even q, ell is odd, c=0, and binom(q,2)b=(q/2)(q-1)b=0. In both cases B=1-epsilon(a+c). The integer binomial coefficient is formed before reduction; no inverse of 2 is introduced.

The ratio of the ramified dual local factor det(1-Fz^{-1})^{-1}det(1-Bz^{-1}) to the trivial-character factor therefore has epsilon coefficient

\[
 -a\frac{rz^{-1}}{1-rz^{-1}}
 +(a+c)\frac{z^{-1}}{1-z^{-1}}.
\]

The accompanying finite-ring test checks this B coefficient in 8,198 cases, including powers of 2. Those cases supplement the uniform algebraic argument; they are not its proof.

## 3. Restoring all places

Write A_v=a_v z/(1-z), D_v=a_v r z^{-1}/(1-rz^{-1}), C_v=c_v/(1-z). The ratio of the two functional equations (10.7.4), with E09's multiplier, gives

\[
 \sum_{v\notin S}A_v
 =R+\sum_{v\in S}a_v-\sum_vD_v
 +\sum_{v\in S}(a_v+c_v)\frac{z^{-1}}{1-z^{-1}}.
\]

For each omitted place,

\[
 a_v+A_v+(a_v+c_v)\frac{z^{-1}}{1-z^{-1}}=-C_v.
\]

Since c_v=0 outside S, this is exactly

\[
 \sum_vA_v+\sum_vD_v+\sum_vC_v
 =\sum_v n_v a_v+\sum_vT_v,
\]

the revision03 formula. The first two infinite sums have the rational-function interpretation specified by (10.13.1); this argument does not assert ordinary convergence at arbitrary t.

## 4. Uniformizer independence and a global check

Under pi'=u pi put b=alpha(u). Then a'=a+b. Substituting y=u^{-1-n}x in the finite sum gives T'=T-(n+1)b. Consequently the right side changes by -b. The left side changes by

\[
 b\left(\frac z{1-z}+\frac{q^{-1}z^{-1}}{1-q^{-1}z^{-1}}\right).
\]

The bracket plus 1 equals (q-1)z/((1-z)(qz-1)); multiplication by b kills it. The change is therefore also -b. This independently checks the linked exponent and signs.

For the degree character on P^1, let L(t)=t/(1-t)+qt/(1-qt). Direct simplification gives L(t)+L(q^{-1}t^{-1})=-2, agreeing with degree -2 of a canonical divisor. This is a consistency check, not a replacement for the derivation above.

## Verification boundary and exact next work

`CHECK_RECEIPT.json` records five symbolic identities and the finite-ring cases. This note supplies the conductor, dual-factor and all-place derivations that the symbolic identities alone do not prove. Edition bindings are EN `551302AAF402F6EE035ED538222C04523D0036A8A9FB78045A0A034118E20BA0`, FR `E55AAE6676C86B506EF15DD00DF505A907E36AC6084EFBA925B6CA0FC59647EC`.

Continue independent E03/E09 source-chain verification, the remaining E01–E17 assertions, and inherited physical1–81. Then perform the complete French/English source-content and full-paper nonpatching gate. Until then revision03 remains a complete working edition, not an independently accepted replacement for public D016.
