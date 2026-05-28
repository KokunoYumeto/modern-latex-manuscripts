# SGA 2: Local Cohomology and Lefschetz Theorems

> Consolidated from the jcreinhold LLM-generated Markdown snapshot included in the source package packet. Not mathematically proofed in this batch.



<!-- SOURCE: 00-introduction.md -->

# Introduction

<!-- label: II.introduction -->

<!-- original page 1 -->

We present here, in a revised and completed form, a photo-offset reissue of the second Séminaire de Géométrie Algébrique
of the Institut des Hautes Études Scientifiques, held in 1962 (mimeographed).

The reader is referred to the Introduction to the first of these Séminaires (cited below as SGA 1) for the aims that
these seminars pursue and their relations with the *Éléments de Géométrie Algébrique*.

The text of Exposés I through XI was written up at the time, from my oral lectures and handwritten notes, by a group of
auditors comprising I. Giorgiutti, J. Giraud, Mlle M. Jaffe (now Mme M. Hakim), and A. Laudal. These notes were
originally regarded as provisional and intended for very limited circulation, pending their absorption into the EGA (an
absorption that has by now become problematic, to say the least, just as for the other parts of the SGA). As stated in
the avertissement of the original edition, this "confidential" character of the notes was supposed to excuse certain
"weaknesses of style", which are doubtless more manifest in the present SGA 2 than in the other Séminaires. I have tried
as far as possible to remedy this in the present reissue, by a relatively close revision of the original text. In
particular, I have harmonized the numbering systems for statements used across the various Exposés by introducing
everywhere the same decimal system, which had already been used in most of the original Exposés of SGA 2, as well as in
all the other parts of the SGA. This led me, in particular, to rework entirely the numbering[^N.D.E-intro-1] of
statements in Exposés III through VIII (and, consequently, of references to those Exposés).[^intro-1] I have also tried
to extirpate from the original text the principal errors of typing or syntax (which were numerous and distracting). In
addition, Mme M. Hakim kindly agreed to rewrite Exposé IV in a less telegraphic style than the original. As in the other
reissues of the SGA, I have likewise added a certain number of footnotes, either to give additional references or to
indicate the state of a question on which progress has been made since the original text was written. Finally, this
Séminaire has been augmented by a new Exposé, namely Exposé XIV, written by Mme Michèle Raynaud in 1967, which takes up
and completes suggestions contained in the "Comments on Exposé XIII" (XIII 6) (written in March 1963). That Exposé takes
up Lefschetz-type theorems from the viewpoint of étale cohomology, using the results on étale cohomology expounded in
SGA 4 and SGA 5 (to appear in the same Series in Pure Mathematics);[^N.D.E-intro-2] it is, on that account, less
"elementary" in nature than the other Exposés of the present volume, which scarcely use more than the substance of
Chapters I through III of EGA.

Here is a sketch of the contents of the present volume.

<!-- original page 2 -->

Exposé I contains the sorites of the "cohomology with supports in $Y$", $H^{\bullet}_{Y}(X, F)$, where $Y$ is a closed
subset of a space $X$ — a cohomology that can be interpreted as a cohomology of $X$ modulo the open set $X - Y$, and
that is the abutment of a most useful "local-to-global spectral sequence" I 2.6, involving sheaves of cohomology "with
supports in $Y$", $\mathcal{H}^{\bullet}_{Y}(F)$.[^N.D.E-intro-3] This formalism can play, in many questions, a role of
"localization" analogous to the one played in differential geometry by the consideration of "tubular" neighborhoods of
$Y$. Exposé II studies the preceding notions in the case of quasi-coherent sheaves on preschemes; Exposé III gives their
relation with the classical notion of depth (III 3.3).

<!-- original page 3 -->

Exposés IV and V give notions of local duality, which one may compare with Serre's projective duality theorem (XII 1.1);
let us note that these two types of duality theorems are substantially generalized in Hartshorne's seminar (cited in a
footnote at the end of Exposé IV).[^N.D.E-intro-4]

Exposés VI and VII give some easy technical notions, used in Exposé VIII to prove the finiteness theorem (VIII 2.3),
which gives necessary and sufficient conditions, for a coherent sheaf $F$ on a noetherian scheme $X$, in order that the
local cohomology sheaves $\mathcal{H}^{i}_{Y}(F)$ be coherent for $i \leqslant n$ (or equivalently, that the sheaves
$R^{i} f_{*}(F|X - Y)$ be coherent for $i \leqslant n - 1$, where $f: X - Y \to X$ is the inclusion). This theorem is
one of the central technical results of the Séminaire, and we show in Exposé IX how a theorem of this nature can be used
to establish a "comparison theorem" and an "existence theorem" in formal geometry, by tracing and generalizing the use
made in (EGA III §§ 4 and 5) of the finiteness theorem for a proper morphism.

These last results are applied in X and XI, devoted respectively to Lefschetz-type theorems for the fundamental group
and for the Picard group.

<!-- original page 4 -->

These theorems consist in comparing, under certain conditions, the invariants ($\pi_{1}$ or `Pic`) attached respectively
to a scheme $X$ and to a subscheme $Y$ (playing the role of a hyperplane section), and in giving in particular
conditions under which they are isomorphic. Roughly speaking, the hypotheses made serve to pass from $Y$ to the formal
completion of $X$ along $Y$, and to be able to apply afterwards the results of IX to pass from there to an open
neighborhood $U$ of $Y$ in $X$. To pass from $U$ to $X$, one needs additional information ("purity" or
"parafactoriality" type) for the local rings of $X$ at the points of $Z = X - U$, (which is a finite discrete set in the
cases envisaged). This explains the interaction in the proofs of Exposés X, XI, XII between local and global results, in
particular in certain inductions. The principal results obtained in X and XI are the theorems of local nature X 3.4
(purity theorem) and XI 3.14 (parafactoriality theorem). One should note that these theorems are proved by cohomological
techniques, of essentially global nature. In XII one obtains, using the preceding local results, the global variants of
these results for projective schemes over a field, or more generally over a more or less arbitrary base scheme; among
the typical statements, let us point out XII 3.5 and XII 3.7.

In XIII, we review some of the many problems and conjectures suggested by the results and methods of the Séminaire. The
most interesting are perhaps those concerning the cohomological and homotopical Lefschetz-type theorems for complex
analytic spaces, cf. XIII pages 26 and following.[^N.D.E-intro-5] In the context of the étale cohomology of schemes, the
corresponding conjectures are proved in XIV by a duality technique that should apply equally in the complex analytic
case (cf. the comments XIII p. 25 and XIV 6.4). But the corresponding homotopical statements in the case of analytic
spaces (and more particularly the statements involving the fundamental group) seem to require entirely new techniques
(cf. XIV 6.4).

<!-- original page 5 -->

I am happy to thank all those who, in various capacities, have helped in the appearance of the present volume, among
them the collaborators already cited in this Introduction. In particular, I wish to thank Mlle Chardon for the good
grace with which she has discharged the thankless task of preparing the final manuscript materially for photo-offset.

Bures-sur-Yvette, April 1968.

A. Grothendieck.

[^N.D.E-intro-1]: *N.D.E.* The original numbering has been preserved as far as possible, adding the adverb *bis* where
    ambiguous duplicates appeared here and there.

[^intro-1]: It goes without saying that all references to SGA 2 that appear in the parts of the SGA published in the
    Series in Pure Mathematics will refer to the present volume, and not to the original edition of SGA 2!

[^N.D.E-intro-2]: *N.D.E.* In fact, these seminars are published by Springer (numbers 269, 279, 305, and 589), but,
    unfortunately, are out of print.

[^N.D.E-intro-3]: *N.D.E.* The underlined notations for the sheafified versions of functors have been preserved, the
    calligraphic analogue of $\Gamma$ not being clear. (In the present translation, the sheafified
    $\mathcal{H}^{\bullet}_{Y}(F)$ is rendered with a script-H to disambiguate, and the corresponding underlined section
    functor is kept as $\Gamma Z$.)

[^N.D.E-intro-4]: *N.D.E.* Hartshorne's book contains sign errors and, more importantly, does not really prove the
    compatibility of the trace with base change. Conrad has completely redone this work, proving this crucial and highly
    non-trivial compatibility (*Grothendieck duality and base change*, Lecture Notes in Math. **1750**, Springer-Verlag,
    Berlin, 2000). Unfortunately, errors remain (cf. two preprints: Conrad B., *Clarifications and corrections to
    "Grothendieck duality and base change"*, and *An addendum to Chapter 5 of "Grothendieck duality and base change"*).
    For a more concrete aspect, with particular attention to the notion of residue, see the works of Lipman, in
    particular (Lipman J., *Dualizing sheaves, differentials and residues on algebraic varieties*, Astérisque **117**,
    Société Mathématique de France, 1984). A categorical proof of the duality theorem, based on Brown's representability
    theorem, has been obtained by Neeman (Neeman A., *The Grothendieck duality theorem via Bousfield's techniques and
    Brown representability*, J. Amer. Math. Soc. **9** (1996), no. 1, pp. 205–236).

[^N.D.E-intro-5]: *N.D.E.* Essentially all the conjectures stated in XIII and XIV are now proved; see the footnotes of
    these sections for references and commentary.


<!-- SOURCE: 00-title-preface.md -->

# SGA 2: Local Cohomology of Coherent Sheaves and Local and Global Lefschetz Theorems

*Séminaire de Géométrie Algébrique du Bois-Marie*, 1962.

A seminar directed by Alexander Grothendieck (compiled by a group of auditors), augmented by an Exposé of Mme Michèle
Raynaud.

A new updated edition of volume 2 of the *Advanced Studies in Pure Mathematics*, published in 1968 by North-Holland
Publishing Company.

## Preface

<!-- label: II.preface -->

The present text is a new updated edition of the book *Cohomologie locale des faisceaux cohérents et théorèmes de
Lefschetz locaux et globaux* (SGA 2), Advanced Studies in Pure Mathematics 2, North-Holland Publishing Company,
Amsterdam, 1968, by A. Grothendieck *et al.* It is the second part of the SGA project initiated by B. Edixhoven, who
prepared a new edition of SGA 1. This version is meant to reproduce the original text, with some modifications,
including minor typographical corrections and footnotes from the editor (*N.D.E.*) explaining the current status of
questions raised in the first edition. Some additional detail has also been given for certain proofs. To avoid possible
confusion, the original footnotes are numbered using stars, while the new ones are numbered using integers. The page
numbers of the original version are written in the margin of the text.

Let me thank the mathematicians who carried out most of the initial typesetting in LATEX 2e, namely L. Bayle, N. Borne,
O. Brinon, J. Buresi, M. Chardin, F. Ducrot, P. Graftiaux, F. Han, P. Karwasz, L. Koelblen, D. Madore, S. Morel, D.
Naie, B. Osserman, J. Riou, and V. Sécherre, and also C. Sabbah for adapting this text to the SMF layout. Let me also
thank J.-B. Bost, P. Colmez, O. Gabber, W. Fulton, S. Kleiman, F. Orgogozo, M. Raynaud, and J.-P. Serre for their
comments and advice.

The editor, Yves Laszlo.

<!-- Editorial note: Laszlo's own English preface in the source PDF has been adopted here with only light
copy-editing for consistency with the SGA 1 translation. The French original of the preface (also in the source PDF)
is the authoritative version; this text matches it. -->

## Table of contents

<!-- label: II.toc -->

Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . 1

- **I.** Global and local cohomological invariants with respect to a closed subspace . . . . . . . . . . . . . . . . . .
  . . . 5

    1. The functors $\Gamma_{Z}$, $\Gamma Z$ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . . . . . 5
    1. The functors $H^{\bullet}_{Z}(X, F)$ and $\mathcal{H}^{\bullet}_{Z}(F)$ . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . . . . . . . . 10
    1. Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . 14

- **II.** Application to quasi-coherent sheaves on preschemes . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . . . . 15

- **III.** Cohomological invariants and depth . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . . . . . . 21

    1. Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . . . . 21
    1. Depth . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . . . 22
    1. Depth and topological properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . 26

- **IV.** Dualizing modules and dualizing functors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . . . . 33

    1. Generalities on module functors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . 33
    1. Characterization of exact functors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . 36
    1. Study of the case where $T$ is left exact and $T(M)$ is of finite type for every $M$ . . . . . . . . . . . 37
    1. Dualizing module; dualizing functor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . 39
    1. Consequences of the theory of dualizing modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       43

- **V.** Local duality and structure of the $H^{i}(M)$ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . . . . . . 47

    1. Complexes of homomorphisms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . 47
    1. The local duality theorem for a regular local ring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . 50
    1. Application to the structure of the $H^{i}(M)$ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . 50

- **VI.** The functors $Ext^{\bullet}_{Z}(X; F, G)$ and $Ext^{\bullet}_{Z}(F, G)$ . . . . . . . . . . . . . . . . . . .
  . . . . . . . . . . . . . . . . . . 57

    1. Generalities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . . . 57
    1. Applications to quasi-coherent sheaves on preschemes . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
    1. Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . 60

- **VII.** Vanishing criteria and coherence conditions for the sheaves $Ext^{i}_{Y}(F, G)$ . . . . . . . . . . . . . . .
  . . . . 61

    1. Study for $i < n$ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . 61
    1. Study for $i > n$ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . 64

- **VIII.** The finiteness theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . . . . . . . . . 67

    1. A biduality spectral sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . 67
    1. The finiteness theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . 70
    1. Applications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . . 76
    1. Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . . 77

- **IX.** Algebraic geometry and formal geometry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . . 79

    1. The comparison theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . 79
    1. The existence theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . 85

- **X.** Application to the fundamental group . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . . . . . 89

    1. Comparison of $\hat{E}t(\hat{X})$ and $\hat{E}t(Y)$ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . . . . 89
    1. Comparison of $\hat{E}t(Y)$ and $\hat{E}t(U)$, for $U$ variable . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . 89
    1. Comparison of $\pi_{1}(X)$ and $\pi_{1}(U)$ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . 94

- **XI.** Application to the Picard group . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . . . . . . 99

    1. Comparison of $\operatorname{Pic}(\hat{X})$ and $\operatorname{Pic}(Y)$ . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . . . . . . . . . . . . 99
    1. Comparison of $\operatorname{Pic}(X)$ and $\operatorname{Pic}(\hat{X})$ . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . . . . . . . . . . . 100
    1. Comparison of $P(X)$ and $P(U)$ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . 101

- **XII.** Applications to projective algebraic schemes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . 109

    1. Projective duality theorem and finiteness theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       109
    1. Lefschetz theory for a projective morphism: Grauert's comparison theorem . . . . . . . . . . . 114
    1. Lefschetz theory for a projective morphism: existence theorem . . . . . . . . . . . . . . . . . . . . . 117
    1. Formal completion and normal flatness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . 122
    1. Universal finiteness conditions for a non-proper morphism . . . . . . . . . . . . . . . . . . . . . . . . 128

- **XIII.** Problems and conjectures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . . . . . 135

    1. Relations between global and local results. Affine problems related to duality . . . . . . . . 135
    1. Problems related to $\pi_{0}$: local Bertini theorems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . 139
    1. Problems related to $\pi_{1}$ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . 143
    1. Problems related to higher $\pi_{i}$: local and global Lefschetz theorems for complex analytic spaces . . . 144
    1. Problems related to local Picard groups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . 148
    1. Comments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . . 151
    1. Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . 158

- **XIV.** Depth and Lefschetz theorems in étale cohomology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . 159

    1. Cohomological and homotopical depth . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . 159
    1. Technical lemmas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . 177
    1. Converse of the affine Lefschetz theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . 181
    1. Main theorem and variants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . 187
    1. Geometrical depth . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . 198
    1. Open questions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . 202
    1. Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . 204

- Index of notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . . . . . . . . . 205

- Terminological index . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . . . . . . 207


<!-- SOURCE: 01-invariants-cohomologiques.md -->

# Exposé I. Global and local cohomological invariants with respect to a closed subspace

<!-- label: I -->

<!-- original page 5 -->

## 1. The functors $\Gamma_{Z}$, $\Gamma Z$

<!-- label: I.1 -->

Throughout this Exposé we write $\Gamma Z$ for the sheafified section-with-support functor (underlined in the original
source) and $\Gamma_{Z}$ for the global one.

<!-- original page 6 -->

Let $X$ be a topological space, and let `C_X` be the category of abelian sheaves on $X$. Let $\Phi$ be a family of
supports in the sense of Cartan; one defines the functor $\Gamma_{\Phi}$ on `C_X` by:

```text
Γ_Φ(F) = subgroup of Γ(F) formed by the sections f such that support f ∈ Φ.
```

<!-- label: eq:I.1.1 -->

If $Z$ is a closed part of $X$, we designate by abuse of language by $\Gamma_{Z}$ the functor $\Gamma_{\Phi}$, where
$\Phi$ is the set of closed parts of $X$ contained in $Z$. Hence one has:

```text
Γ_Z(F) = subgroup of Γ(F) formed by the sections f such that support f ⊂ Z.
```

<!-- label: eq:I.1.2 -->

We wish to generalize this definition to the case where $Z$ is a locally closed part of $X$, hence closed in a suitable
open part $V$ of $X$. In this case we shall set:

$$
\Gamma_{Z}(F) = \Gamma_{Z}(F|V).
$$

<!-- label: eq:I.1.3 -->

It must be verified that $\Gamma_{Z}(F)$ "does not depend" on the open set chosen. It suffices to show that if $V'$,
with $V \supset V' \supset Z$, is an open set, then the map $\rho^{V}_{V'}: F(V) \to F(V')$ maps $\Gamma_{Z}(F|V)$
isomorphically onto $\Gamma_{Z}(F|V')$. Now

$$
\Gamma_{Z}(F|V) = \ker \rho^{V}_{V-Z},
$$

<!-- label: eq:I.1.4 -->

so if $f \in \Gamma_{Z}(F|V)$ and if $\rho^{V}_{V'}(f) = \rho^{V}_{V-Z}(f) = 0$, then $f = 0$, since $(V', V - Z)$ is a
covering of $V$. Likewise, if $f' \in \Gamma_{Z}(F|V')$, then $f' \in F(V')$ and $0 \in F(V - Z)$ define an $f \in F(V)$
such that $\rho^{V}_{V'}(f) = f'$, $f \in \Gamma_{Z}(F|V)$; hence $\rho^{V}_{V'}$ induces an isomorphism
$\Gamma_{Z}(F|V) \to \Gamma_{Z}(F|V')$.

<!-- original page 7 -->

Note that every open set $W$ of $Z$ is induced by an open set $U$ of $X$ in which $W$ is closed. It follows that
$W \mapsto \Gamma_{W}(F)$ defines a presheaf on $Z$, and one verifies that this is a sheaf, which we shall denote
$i^{!}(F)$, where $i: Z \to X$ is the canonical immersion. One finds:

$$
\Gamma_{Z}(F) = \Gamma(i^{!}(F)).
$$

<!-- label: eq:I.1.5 -->

The sheaf $i^{!}(F)$ is a subsheaf of $i*(F)$; indeed, the canonical homomorphism

```text
Γ(F|U) = Γ(U, F) ⟶ Γ(U ∩ Z, i*(F))
```

is injective on $\Gamma_{U\cap Z}(F|U) \subset \Gamma(F|U)$. Summarizing, we have the following result:

**Proposition.**

<!-- label: I.1.1 -->

There exists a unique subsheaf $i^{!}(F)$ of $i*(F)$ such that, for every open set $U$ of $X$ such that $U \cap Z$ is
closed in $U$,

```text
Γ(F|U) = Γ(U, F) ⟶ Γ(U ∩ Z, i*(F))
```

induces an isomorphism $\Gamma_{U\cap Z}(F|U) \to \Gamma(U \cap Z, i^{!}(F))$.

Note that if $Z$ is open, one will simply have

```text
i^!(F) = i*(F) = F|Z, Γ_Z(F) = Γ(Z, F).
```

<!-- label: eq:I.1.6 -->

Suppose again that $Z$ is arbitrary. Then, for $U$ a variable open set of $X$, one sees that

```text
U ⟼ Γ_{U∩Z}(F|U) = Γ(U ∩ Z, i^!(F))
```

is a sheaf on $X$, which we shall denote $\Gamma Z(F)$; more precisely, by the preceding formula (expressing that
$i^{!}$ commutes with restriction to open sets) one has an isomorphism

$$
\Gamma Z(F) = i_{*}(i^{!}(F))
$$

<!-- label: eq:I.1.7 -->

<!-- original page 8 -->

by definition, one has, for every open set $U$ of $X$,

$$
\Gamma(U, \Gamma Z(F)) = \Gamma_{U\cap Z}(F|U).
$$

<!-- label: eq:I.1.8 -->

Let us note here a characteristic difference between the case where $Z$ is closed and the case where $Z$ is open. In the
first case, formula (8) shows us that $\Gamma Z(F)$ can be regarded as a subsheaf of $F$, and one thus has a canonical
immersion

$$
\Gamma Z(F) \hookrightarrow F.
$$

<!-- label: eq:I.1.8′ -->

In the case where $Z$ is open, on the contrary, one sees from (6) that the right-hand side of (8) is
$\Gamma(U \cap Z, F)$, so receives $\Gamma(U, F)$, hence one has a canonical homomorphism in the opposite direction from
the previous one:

$$
F \longrightarrow \Gamma Z(F),
$$

<!-- label: eq:I.1.8″ -->

which is moreover none other than the canonical homomorphism[^N.D.E-I-1]

$$
F \longrightarrow i_{*} i*(F),
$$

taking into account the isomorphism

$$
\Gamma Z(F) \simeq i_{*} i*(F)
$$

<!-- label: eq:I.1.6bis -->

deduced from (6) and (7).

<!-- original page 9 -->

Of course, for $F$ variable, $\Gamma_{Z}(F)$, $\Gamma Z(F)$, $i^{!}(F)$ may be considered as functors in $F$, with
values respectively in the category of abelian groups, of abelian sheaves on $X$, and of abelian sheaves on $Z$. It is
sometimes convenient to interpret the functor

$$
i^{!}: C_{X} \longrightarrow C_{Z}
$$

as the right adjoint of a well-known functor

$$
i_{!}: C_{Z} \longrightarrow C_{X}
$$

defined by the following proposition:

**Proposition.**

<!-- label: I.1.2 -->

Let $G$ be an abelian sheaf on $Z$. Then there exists a unique subsheaf of $i_{*}(G)$, say $i_{!}(G)$, such that, for
every open set $U$ of $X$, the (identity) isomorphism

```text
Γ(U ∩ Z, G) = Γ(U, i_*(G))
```

defines an isomorphism

```text
Γ_{Φ_{U∩Z,U}}(U ∩ Z, G) = Γ(U, i_!(G)),
```

where $\Phi_{U\cap Z,U}$ denotes the set of parts of $U \cap Z$ that are closed in $U$.

The verification reduces to noting that the left-hand side is a sheaf for $U$ variable, i.e. that the property, for a
section of $i_{*}(G)$ on $U$ considered as a section of $G$ on $U \cap Z$, of having support closed in $U$ is of local
nature on $U$. The sheaf $i_{!}(G)$ just defined is also known under the name: sheaf deduced from $G$ by extension by
`0` outside $Z$, cf. [Godement]. In particular, if $Z$ is closed, one has

$$
i_{!}(G) = i_{*}(G);
$$

<!-- label: eq:I.1.9 -->

but in the general case, the canonical injection $i_{!}(G) \to i_{*}(G)$ is not an isomorphism, as is already well known
for $Z$ open. Evidently, $i_{!}(G)$ depends functorially on $G$ (and is even an exact functor in $G$). This said, one
has:

**Proposition.**

<!-- label: I.1.3 -->

There exists an isomorphism of bifunctors in $G$, $F$ ($G$ an abelian sheaf on $Z$, $F$ an abelian sheaf on $X$):

```text
Hom(i_!(G), F) = Hom(G, i^!(F)).
```

<!-- label: eq:I.1.10 -->

To define such an isomorphism, it amounts to the same to define functorial homomorphisms

```text
i_! i^!(F) ⟶ F, G ⟶ i^! i_!(G),
```

satisfying the well-known compatibility conditions (cf. for example Shih's exposé in the Cartan seminar on cohomological
operations).

Recalling that $i_{!}$ is exact, hence transforms monomorphisms into monomorphisms, one concludes:

<!-- original page 10 -->

**Corollary.**

<!-- label: I.1.4 -->

If $F$ is injective, $i^{!}(F)$ is injective, hence $\Gamma Z(F) = i_{*} i^{!}(F)$ is also injective.

Replacing $X$ by a variable open set $U$ of $X$, one also concludes from 1.3:

**Corollary.**

<!-- label: I.1.5 -->

One has an isomorphism functorial in $F$, $G$:

```text
ℋom(i_!(G), F) = i_*(ℋom(G, i^!(F))).
```

<!-- label: eq:I.1.11 -->

Taking for $G$ the constant sheaf on $Z$ defined by $\mathbb{Z}$, say $\mathbb{Z}_{Z}$, 1.3 and 1.5 specialize into

**Corollary.**

<!-- label: I.1.6 -->

One has isomorphisms functorial in $F$:

$$
\Gamma_{Z}(F) = \operatorname{Hom}(\mathbb{Z}_{Z,X}, F),
\Gamma Z(F)  = \mathcal{H}om(\mathbb{Z}_{Z,X}, F),
$$

<!-- label: eq:I.1.12 -->

where $\mathbb{Z}_{Z,X} = i_{!}(\mathbb{Z}_{Z})$ is the abelian sheaf on $X$ deduced from the constant sheaf on $Z$
defined by $\mathbb{Z}$, by extension by `0` outside $Z$.

**Remark.**

<!-- label: I.1.7 -->

Suppose that $X$ is a ringed space, and equip $Z$ with the sheaf of rings $O_{Z} = i^{-1}(O_{X})$; finally, denote by
`C_X` and `C_Z` the category of Modules on $X$, resp. $Z$. Then the preceding considerations extend word for word,
taking $F$ to be a Module on $X$ and $G$ a Module on $Z$, and interpreting accordingly statements 1.3 to 1.6.

To finish these generalities, let us examine what happens when one changes the locally closed part $Z$. Let
$Z' \subset Z$ be another locally closed part, and let

```text
j: Z′ ⟶ Z,   i′: Z′ ⟶ X,   i′ = i j
```

<!-- original page 11 -->

be the canonical inclusions. Then one has functorial isomorphisms:

```text
(i j)^! = j^! i^!,   (i j)_! = i_! j_!.
```

<!-- label: eq:I.1.13 -->

The first isomorphism (13) defines a functorial isomorphism

```text
Γ_{Z′}(F) = Γ(Z′, (i j)^!(F)) ≃ Γ(Z′, j^!(i^!(F))) = Γ_{Z′}(i^!(F)).
```

<!-- label: eq:I.1.14 -->

Suppose now that $Z'$ is closed in $Z$, and let

$$
Z'' = Z - Z'
$$

be its complement in $Z$, which is open in $Z$, hence locally closed in $X$. The canonical inclusion (8′) applied to
$i^{!}(F)$ on $Z$ equipped with $Z'$ defines, thanks to (14), an injective functorial canonical homomorphism

$$
\Gamma_{Z'}(F) \longrightarrow \Gamma_{Z}(F).
$$

<!-- label: eq:I.1.15 -->

If in (14) one replaces $Z$ by $Z''$ and uses (8″), one finds a functorial canonical homomorphism:

$$
\Gamma_{Z}(F) \longrightarrow \Gamma_{Z''}(F).
$$

<!-- label: eq:I.1.15′ -->

<!-- original page 12 -->

**Proposition.**

<!-- label: I.1.8 -->

Under the preceding conditions, the sequence of functorial homomorphisms

$$
0 \longrightarrow \Gamma_{Z'}(F) \longrightarrow \Gamma_{Z}(F) \longrightarrow \Gamma_{Z''}(F)
$$

<!-- label: eq:I.1.16 -->

is exact. If $F$ is flasque, the sequence remains exact when one puts a zero on the right.

*Proof.* Replacing $X$ by an open set $V$ in which $Z$ is closed, one reduces to the case where $Z$ is closed, hence
$Z'$ is closed. Then $Z''$ is closed in the open set $X - Z'$, and one has a canonical inclusion

```text
Γ_{Z″}(F) ⟶ Γ(X − Z′, F),
```

and the exactness of (16) simply means that the sections of $F$ with support in $Z'$ are those whose restriction to
$X - Z'$ is zero.

When $F$ is flasque, every element of $\Gamma_{Z''}(F)$, considered as a section of $F$ on $X - Z'$, can be extended to
a section of $F$ on $X$, and the latter will evidently have its support in $Z$, which proves that the last homomorphism
in (16) is then surjective.

**Corollary.**

<!-- label: I.1.9 -->

One has a functorial exact sequence

$$
0 \longrightarrow \Gamma Z'(F) \longrightarrow \Gamma Z(F) \longrightarrow \Gamma Z''(F),
$$

<!-- label: eq:I.1.16bis -->

and if $F$ is flasque, this sequence remains exact when one puts a `0` on the right.

One may interpret (1.8) in terms of results on the functors `Hom` and $\mathcal{H}om$ via 1.6, in the following way. Let
us first note that if $G$ is an abelian sheaf on $Z$, inducing the sheaves $j*(G)$ and $k*(G)$ on $Z'$ resp. $Z''$
(where $j: Z' \to Z$ and $k: Z'' \to Z$ are the canonical injections), one has a canonical exact sequence of sheaves on
$X$:

$$
0 \longrightarrow k*(G)_{X} \longrightarrow G_{X} \longrightarrow j*(G)_{X} \longrightarrow 0,
$$

<!-- label: eq:I.1.17 -->

where, to simplify the notation, the subscript $X$ designates the sheaf on $X$ obtained by extending by `0` in the
complement of the space of definition of the sheaf in question. The exact sequence (17) generalizes a well-known exact
sequence in the case $Z = X$ (cf. [Godement]), and is moreover deduced from the latter by writing the exact sequence in
question on $Z$, and applying the functor $i_{!}$. Taking $G = \mathbb{Z}_{Z}$, one concludes in particular:

**Proposition.**

<!-- label: I.1.10 -->

Under the preceding conditions, one has an exact sequence of abelian sheaves on $X$:

$$
0 \longrightarrow \mathbb{Z}_{Z'',X} \longrightarrow \mathbb{Z}_{Z,X} \longrightarrow \mathbb{Z}_{Z',X} \longrightarrow 0.
$$

<!-- label: eq:I.1.18 -->

This being so, the two exact sequences 1.8 and 1.9 are nothing other than the exact sequences deduced from (18) by
application of the functor $\operatorname{Hom}(-, F)$ resp. $\mathcal{H}om(-, F)$.

This gives an evident proof of the fact that the sequences (16) and (16 bis) remain exact when one puts a zero on the
right, provided that $F$ is injective.

<!-- original page 13 -->

## 2. The functors $H^{*}_{Z}(X, F)$ and $\mathcal{H}^{*}_{Z}(F)$

<!-- label: I.2 -->

**Definition.**

<!-- label: I.2.1 -->

One denotes by $H^{*}_{Z}(X, F)$ and $\mathcal{H}^{*}_{Z}(F)$ the derived functors in $F$ of the functors
$\Gamma_{Z}(F)$ resp. $\Gamma Z(F)$.

These are cohomological functors, with values in the category of abelian groups resp. in the category of abelian sheaves
on $X$. When $Z$ is closed, $H^{*}_{Z}(X, F)$ is, by definition, nothing other than $H^{*}_{\Phi}(X, F)$ where $\Phi$
denotes the family of closed parts of $X$ contained in $Z$. When $Z$ is open, we shall see that $H^{*}_{Z}(X, F)$ is
nothing other than $H^{*}(Z, F) = H^{*}(Z, F|Z)$, thanks to the following proposition.

**Proposition (Excision Theorem).**

<!-- label: I.2.2 -->

Let $V$ be an open part of $X$ containing $Z$. Then one has an isomorphism of cohomological functors in $F$:

```text
H^*_Z(X, F) ⟶ H^*_Z(V, F|V).
```

<!-- label: eq:I.2.19 -->

Indeed, one has a functorial isomorphism $\Gamma^{X}_{Z} \simeq \Gamma^{V}_{Z} j^{!}$, where $j: V \to X$ is the
inclusion, and where $j^{!}$ is thus the restriction functor (cf. (14)). This last is exact, and transforms injectives
into injectives by 1.4, whence the isomorphism (19) at once.

When $Z$ is open, one may take $V = Z$ and one finds:

**Corollary.**

<!-- label: I.2.3 -->

Suppose $Z$ open; then one has an isomorphism of cohomological functors:

```text
H^*_Z(X, F) = H^*(Z, F).
```

<!-- label: eq:I.2.20 -->

One concludes from isomorphisms 1.6 and from the definitions (cf. [Tôhoku]):

<!-- original page 14 -->

**Proposition.**[^N.D.E-I-2]

<!-- label: I.2.3bis -->

One has isomorphisms of cohomological functors:

```text
H^*_Z(X, F) ≃ Ext^*(X; ℤ_{Z,X}, F),
```

<!-- label: eq:I.2.21 -->

$$
\mathcal{H}^{*}_{Z}(F) \simeq \mathcal{E}xt^{*}(\mathbb{Z}_{Z,X}, F).
$$

<!-- label: eq:I.2.21bis -->

One may therefore apply the results of [Tôhoku] on the `Ext` of Modules. Let us first point out the following
interpretation of the sheaves $\mathcal{H}^{*}_{Z}(F)$ in terms of the global groups $H^{*}_{Z}(X, F)$:

**Corollary.**

<!-- label: I.2.4 -->

$\mathcal{H}^{*}_{Z}(F)$ is canonically isomorphic to the sheaf associated to the presheaf

```text
U ⟼ H^*_{Z ∩ U}(U, F|U).
```

In particular, using corollary 2.3, one finds:

**Corollary.**

<!-- label: I.2.5 -->

Suppose $Z$ open; then one has an isomorphism of cohomological functors:

```text
ℋ^*_Z(F) = R^* i_* i*(F)
```

<!-- label: eq:I.2.22 -->

(where $i: Z \to X$ is the inclusion).

The spectral sequence of `Ext` gives the important spectral sequence:

**Theorem.**

<!-- label: I.2.6 -->

One has a spectral sequence functorial in $F$, abutting to $H^{*}_{Z}(X, F)$ and with initial term

$$
E^{p,q}_{2}(F) = H^{p}(X, \mathcal{H}^{q}_{Z}(F)).
$$

<!-- label: eq:I.2.23 -->

**Remarks.**

<!-- label: I.2.7 -->

It follows at once from 2.4 that the sheaves $\mathcal{H}^{q}_{Z}(F)$ are zero in $X - Z$, and also zero in the interior
of $Z$ for $q \neq 0$ (so for such a $q$, $\mathcal{H}^{q}_{Z}(F)$ is even supported on the boundary of $Z$).

<!-- original page 15 -->

Consequently, the right-hand side of (23) may be interpreted as a cohomology group on $Z$. We shall use 2.6 in the case
where $Z$ is closed in $X$, in which case the right-hand side of (23)[^N.D.E-I-3] may be interpreted as a cohomology
group computed on $Z$:

$$
E^{p,q}_{2}(F) = H^{p}(Z, \mathcal{H}^{q}_{Z}(F)).
$$

<!-- label: eq:I.2.23bis -->

Let us also note that when $Z$ is open, the spectral sequence 2.6 is nothing other than the Leray spectral sequence for
the continuous map $i: Z \to X$, taking into account the interpretation 2.5 in the calculation of the initial term of
the Leray spectral sequence.

Let us return to the exact sequence (18);[^N.D.E-I-4] it gives rise to an exact sequence of `Ext` (cf. [Tôhoku]):

**Theorem.**

<!-- label: I.2.8 -->

Let $Z$ be a locally closed part of $X$, $Z'$ a closed part of $Z$, and $Z'' = Z - Z'$. Then one has an exact sequence
functorial in $F$:

```text
0 ⟶ H⁰_{Z′}(X, F) ⟶ H⁰_Z(X, F) ⟶ H⁰_{Z″}(X, F) ─∂─→ H¹_{Z′}(X, F) ⟶ H¹_Z(X, F) ...

... H^i_{Z′}(X, F) ⟶ H^i_Z(X, F) ⟶ H^i_{Z″}(X, F) ─∂─→ H^{i+1}_{Z′}(X, F) ...
```

<!-- label: eq:I.2.24 -->

Let us recall how this exact sequence can be obtained. Let $C(F)$ be an injective resolution of $F$; then the exact
sequence (18)[^N.D.E-I-5] gives rise to the exact sequence

$$
0 \longrightarrow \Gamma_{Z'}(C(F)) \longrightarrow \Gamma(C(F)) \longrightarrow \Gamma_{Z''}(C(F)) \longrightarrow 0,
$$

<!-- label: eq:I.2.25 -->

(which is nothing other than the one defined in 1.8). One concludes an exact sequence of cohomology, which is nothing
other than (24).

<!-- original page 16 -->

The most important case for us is the one where $Z$ is closed (and one can moreover always reduce to it by replacing $X$
by an open set $V$ in which $Z$ is closed). Then $Z'$ is closed, $Z''$ is closed in the open set $X - Z'$, and one may
write

```text
H^i_{Z″}(X, F) = H^i_{Z″}(X − Z′, F|_{X−Z′}),
```

<!-- label: eq:I.2.26 -->

which allows us to write the exact sequence (24) in terms of cohomologies with support in a given closed set. The most
frequent case is the one where $Z = X$. Setting then, for simplification, $Z' = A$, one finds:

**Corollary.**

<!-- label: I.2.9 -->

Let $A$ be a closed part of $X$. Then one has an exact sequence functorial in $F$:

```text
0 ⟶ H⁰_A(X, F) ⟶ H⁰(X, F) ⟶ H⁰(X − A, F) ─∂─→ H¹_A(X, F) ...

... H^i_A(X, F) ⟶ H^i(X, F) ⟶ H^i(X − A, F) ─∂─→ H^{i+1}_A(X, F) ...
```

<!-- label: eq:I.2.27 -->

This exact sequence shows that the cohomology group $H^{i}_{A}(X, F)$ plays the role of a relative cohomology group of
$X$ mod $X - A$, with coefficients in $F$. It is on this account that it was introduced naturally in applications. By
"sheafifying" (24) and (27), or by proceeding directly, one finds, taking into account that the sheaf associated to
$U \mapsto H^{i}(U, F)$ is zero if $i > 0$:

**Corollary.**

<!-- label: I.2.10 -->

Under the conditions of 2.8, one has an exact sequence functorial in $F$:

```text
... ℋ^i_{Z′}(F) ⟶ ℋ^i_Z(F) ⟶ ℋ^i_{Z″}(F) ─∂─→ ℋ^{i+1}_{Z′}(F) ...
```

<!-- label: eq:I.2.24bis -->

**Corollary.**

<!-- label: I.2.11 -->

Let $A$ be a closed part of $X$; then one has an exact sequence functorial in $F$:

```text
0 ⟶ ℋ⁰_A(F) ⟶ F ⟶ f_*(F|_{X−A}) ─∂─→ ℋ¹_A(F) ⟶ 0,
```

<!-- label: eq:I.2.28 -->

and canonical isomorphisms, for $i \geqslant 2$:

```text
ℋ^i_A(F) = ℋ^{i−1}_{X−A}(F) = R^{i−1} f_*(F|_{X−A}),
```

<!-- label: eq:I.2.29 -->

where $f: (X - A) \to X$ is the inclusion.

This therefore defines $\mathcal{H}^{0}_{A}(F)$ and $\mathcal{H}^{1}_{A}(F)$ respectively as the kernel and cokernel of
the canonical homomorphism

```text
F ⟶ f_* f*(F) = f_*(F|_{X−A}),
```

and the $\mathcal{H}^{i}_{A}(F)$ ($i \geqslant 2$) in terms of the derived functors of $f_{*}$.

<!-- original page 17 -->

**Corollary.**

<!-- label: I.2.12 -->

Let $F$ be an abelian sheaf on $X$. If $F$ is flasque, then for every locally closed part $Z$ of $X$ and every integer
$i \neq 0$, one has $H^{i}_{Z}(X, F) = 0$, $\mathcal{H}^{i}_{Z}(F) = 0$. Conversely, if for every closed part $Z$ of $X$
one has $H^{1}_{Z}(X, F) = 0$, then $F$ is flasque.

Suppose that $F$ is flasque; then $F$ induces a flasque sheaf on every open set, so to prove $H^{i}_{Z}(X, F) = 0$ for
$i > 0$, one may suppose $Z$ closed, and then the assertion follows from the exact sequence (27).[^N.D.E-I-6] One
concludes, for every locally closed $Z$, by "sheafifying", i.e. applying 2.4, that $\mathcal{H}^{i}_{Z}(F) = 0$ for
$i > 0$. Conversely, suppose $H^{1}_{Z}(X, F) = 0$ for every closed $Z$; then the exact sequence (27)[^N.D.E-I-7] shows
that for every such $Z$, $H^{0}(X, F) \to H^{0}(X - Z, F)$ is surjective, which means that $F$ is flasque.

Combining 2.6 and 2.8, we shall deduce from them:

**Proposition.**

<!-- label: I.2.13 -->

Let $F$ be an abelian sheaf on $X$, $Z$ a closed part of $X$, $U = X - Z$, $N$ an integer. The following conditions are
equivalent:

(i) $\mathcal{H}^{i}_{Z}(F) = 0$ for $i \leqslant N$.

(ii) For every open set $V$ of $X$, considering the canonical homomorphism

```text
H^i(V, F) ⟶ H^i(V ∩ U, F),
```

this homomorphism is:

a) bijective for $i < N$,

b) injective for $i = N$.

(When $N > 0$, one may in (ii) restrict to requiring a)).

To prove (i) ⇒ (ii), one is reduced, thanks to the local nature of the $\mathcal{H}^{i}_{Z}(F)$, to proving the

**Corollary.**

<!-- label: I.2.14 -->

If condition 2.13 (i) is satisfied, then

```text
H^i(X, F) ⟶ H^i(U, F)
```

is bijective for $i < N$, injective for $i = N$.

Indeed, by virtue of the exact sequence (27), this also means $H^{i}_{Z}(X, F) = 0$ for $i \leqslant N$, and this
relation is an immediate consequence of the spectral sequence (23 bis).[^N.D.E-I-8]

<!-- original page 18 -->

Conversely, hypothesis 2.13 (ii) means that for every open set $V$ of $X$, one has

```text
H^i_{Z ∩ V}(V, F|V) = 0 for i ⩽ N,
```

which implies 2.13 (i) thanks to 2.4. If moreover $N > 0$, hypothesis b) is superfluous. Indeed, if $N = 1$, hypothesis
a) and (28) ensure the vanishing of $\mathcal{H}^{i}_{Z}(F) = 0$ for $i \leqslant N$. If $N > 1$, hypothesis a) for
$i = N - 1 > 0$ and (29) ensure the vanishing of $\mathcal{H}^{i}_{Z}(F)$ for $i \leqslant N$.

Taking 2.11 into account, this further proves 2.13 (i)...

**Remark.**

Let $Y \to X$ be a closed immersion, and suppose that locally it is of the form
${0} \times Y \subset \mathbb{R}^{n} \times Y$. Suppose that $F$ is a locally constant sheaf on $X$; then one finds

```text
ℋ^i_Y(F) ≃ { 0            if i ≠ n,
           { F ⊗ T_{Y,X}   if i = n,    where  T_{Y,X} ≃ ℋ^n_Y(ℤ_X)
```

<!-- label: eq:I.2.30 -->

is a sheaf, extension to $X$ of a sheaf on $Y$ locally isomorphic to $\mathbb{Z}_{Y}$, called the "normal orientation
sheaf of $Y$ in $X$".

Using the spectral sequence (23 bis),[^N.D.E-I-9] one finds in this case:

```text
H^i_Y(X, F) ≃ H^{i−n}(Y, F ⊗ T_{Y,X}),
```

<!-- label: eq:I.2.31 -->

and one recovers the "Gysin homomorphism":

```text
H^j(Y, F ⊗ T_{Y,X}) ⟶ H^{j+n}(X, F).
```

<!-- label: eq:I.2.32 -->

## Bibliography

<!-- label: I.bibliography -->

**[Godement]** R. Godement — *Topologie algébrique et théorie des faisceaux*, Act. Scient. et Ind., vol. 1252, Hermann,
Paris.

**[Tôhoku]** A. Grothendieck — "Sur quelques points d'algèbre homologique", *Tôhoku Math. J.* **9** (1957), pp. 119–221.

## Footnotes

<!--
LEDGER DELTA (Exposé I):
| French | English | Note |
| sous-faisceau | subsheaf | Standard. |
| extension par 0 (en dehors de Z) | extension by 0 (outside Z) | Standard for `j_!` constructions. |
| théorème d'excision | Excision Theorem | Stated as proposition in source, but the parenthetical name is preserved. |
| faisceau d'orientation normale | normal orientation sheaf | The "T_{Y,X}" of the closing remark. |
| famille de supports | family of supports | Cartan terminology, kept verbatim. |
| à support dans Z | with support in Z | Standard. |
| faisceautiser | "sheafify" | Kept in quotation marks as in the original (Grothendieck-era coinage). |
| par abus de langage | by abuse of language | Standard. |
| à valeurs dans | with values in | Standard. |
| aboutissement (d'une suite spectrale) | abutment (of a spectral sequence) | Per glossary. |
| terme initial | initial term | Per glossary. |
-->

[^N.D.E-I-1]: *N.D.E.* The original reference was (8).

[^N.D.E-I-2]: *N.D.E.* The proposition bears the number 2.3 in the original edition.

[^N.D.E-I-3]: *N.D.E.* The equation was numbered (23) in the original edition.

[^N.D.E-I-4]: *N.D.E.* The original reference was (1.10).

[^N.D.E-I-5]: *N.D.E.* See preceding note.

[^N.D.E-I-6]: *N.D.E.* The original reference was (2.9).

[^N.D.E-I-7]: *N.D.E.* The original reference was (2.9).

[^N.D.E-I-8]: *N.D.E.* See preceding note.

[^N.D.E-I-9]: *N.D.E.* The original reference was 2.6.


<!-- SOURCE: 02-faisceaux-quasi-coherents.md -->

# Exposé II. Application to quasi-coherent sheaves on preschemes

<!-- label: II -->

<!-- original page 19 -->

**Proposition.**

<!-- label: II.1 -->

Let $X$ be a prescheme, let $Z$ be a locally closed subset of the form $Z = U - V$, where $U$ and $V$ are two open
subsets of $X$ such that $V \subset U$ and such that the canonical immersions $U \to X$, $V \to X$ are quasi-compact.
Then for every quasi-coherent Module $F$ on $X$, the sheaves $\mathcal{H}^{i}_{Z}(F)$ are quasi-coherent.

By (I 2.4),[^N.D.E-II-1] there is an exact sequence of relative cohomology

```text
⋯ → ℋ^{i−1}_U(F) → ℋ^i_V(F) → ℋ^i_Z(F) → ℋ^i_U(F) → ℋ^{i+1}_V(F) → ⋯.
```

By (EGA III 1.4.17), in order that the $\mathcal{H}^{i}_{Z}(F)$ be quasi-coherent it therefore suffices that the
$\mathcal{H}^{i}_{U}(F)$ and the $\mathcal{H}^{i}_{V}(F)$ be so. We may therefore assume that $Z$ is open and that the
canonical immersion $j: Z \to X$ is quasi-compact.

Since $Z$ is open, we have (I 2.2)[^N.D.E-II-1] a canonical isomorphism

$$
\mathcal{H}^{i}_{Z}(F) \simeq R^{i} j_{*}(F|Z),
$$

but $j$ is separated (EGA I 5.5.1) and quasi-compact, hence (EGA III 1.4.10) the
$R^{i} j_{*}(F|Z) = \mathcal{H}^{i}_{Z}(F)$ are quasi-coherent, which completes the proof.

<!-- Editorial note: The OCR shows `(I 24)`, `(I 22)`, `(I 23)`, `(I 27)`. In the renumbered 1968 edition these
correspond to the displayed exact sequence and canonical isomorphisms of Exposé I §2. The reference targets in this
file are conservative; a reader who needs the exact decimal should consult Exposé I directly. ΓZ underlined in the
source is rendered with the script-H `ℋ` for the sheafified cohomology functor and with `ΓZ` for the underlined
section functor, per the SGA 2 glossary. -->

**Corollary.**

<!-- label: II.2 -->

Let $Z$ be a closed subset of $X$ such that the canonical immersion $X - Z \to X$ is quasi-compact. Then the Modules
$\mathcal{H}^{i}_{Z}(F)$ are quasi-coherent.

**Corollary.**

<!-- label: II.3 -->

If $X$ is locally noetherian, then for every locally closed subset $Z$ of $X$ and every quasi-coherent Module $F$ on
$X$, the $\mathcal{H}^{i}_{Z}(F)$ are quasi-coherent.

This follows immediately from Corollary 2 and (EGA I 6.6.4).

**Corollary.**

<!-- label: II.4 -->

<!-- original page 20 -->

Suppose that $X$ is the spectrum of a ring $A$, and let $U$ be a quasi-compact open subset of $X$, $Y = X - U$, and $F$
a quasi-coherent Module on $X$. There is an isomorphism of cohomological functors in $F$:

$$
\mathcal{H}^{i}_{Y}(F) = (H^{i}_{Y}(X, F))~.
$$

<!-- label: eq:II.4.1 -->

<!-- original page 20 (continued) -->

In addition, one has an exact sequence functorial in $F$:

```text
0 → H⁰_Y(X, F) → H⁰(X, F) → H⁰(U, F) → H¹_Y(X, F) → 0,
```

<!-- label: eq:II.4.2 -->

and isomorphisms functorial in $F$:

```text
H^i_Y(X, F) ≃ H^{i−1}(U, F),    i ⩾ 2.
```

<!-- label: eq:II.4.3 -->

By Corollary 2, the $\mathcal{H}^{i}_{Y}(F)$ are quasi-coherent; since $X$ is affine, one therefore has
$H^{p}(X, \mathcal{H}^{i}_{Y}(F)) = 0$ for $p > 0$. The spectral sequence (I 2.3)[^N.D.E-II-1] degenerates, hence

$$
H^{i}_{Y}(X, F) = \Gamma(\mathcal{H}^{i}_{Y}(F)).
$$

Equality (4.1) then follows from (EGA I 1.1.3.7); (4.2) and (4.3) follow from the cohomology exact sequence (I
2.7)[^N.D.E-II-1] and from the fact that $H^{i}(X, F) = 0$ for $i > 0$, since $X$ is affine.

Under the hypotheses of 4,[^N.D.E-II-2] $U$ is a finite union of affine open sets $X_{f}$; we can therefore find an
ideal $I$ generated by a finite number of elements $f_{\alpha}$ and defining $Y$, say $f = (f_{\alpha})$. With the
notation of (EGA III § 1),[^N.D.E-II-3] one has:

**Proposition.**

<!-- label: II.5 -->

Suppose that $X$ is the spectrum of a ring $A$; let $f = (f_{\alpha})$ be a finite family of elements of $A$, $Y$ the
closed subset of $X$ they define, $M$ an $A$-module, and $F$ the sheaf associated with $M$. One then has isomorphisms of
$\partial$-functors in $M$:

```text
H^i((f), M) ≃ H^i_Y(X, F).
```

<!-- label: eq:II.5.1 -->

(We shall also write $H^{i}_{J}(M) = H^{i}_{Y}(X, F)$, if $Y$ is the closed subset of $X = \operatorname{Spec} A$
defined by an ideal $J$ of $A$.)

<!-- original page 21 -->

For $i = 0$ and $i = 1$, one uses the exact sequences (4.2) and (EGA III 1.4.3.2); if $i \geqslant 2$, one uses (4.3)
and (EGA III 1.4.3.1). This gives us isomorphisms functorial in $M$. One verifies that, up to a sign depending only on
$i$, they are compatible with the boundary operator, whence the existence of the isomorphism of $\partial$-functors
(5.1).

Now let $X$ be a prescheme, $Y$ a closed subset of $X$, $f: Y \to X$ the inclusion, and $I$ a quasi-coherent ideal
defining $Y$ in $X$. Let $F$ be a sheaf on $X$.

We have seen that there exist isomorphisms of $\partial$-functors in $F$

```text
Ext^i_{𝒪_X}(X; f_* f^{−1}(𝒪_X), F) → H^i_Y(X, F),
```

<!-- label: eq:II.star -->

```text
ℰxt^i_{𝒪_X}(f_* f^{−1}(𝒪_X), F) → ℋ^i_Y(F).
```

<!-- label: eq:II.starstar -->

Let $n$, $m$ be integers with $m \geqslant n \geqslant 0$; we denote by $i_{n,m}$ the canonical map
$\mathcal{O}_{Y_{m}} = \mathcal{O}_{X}/I^{m+1} \to \mathcal{O}_{X}/I^{n+1} = \mathcal{O}_{Y_{n}}$, and by $j_{n}$ the
map

<!-- original page 22 (anchor at top of source page 17) -->

$f_{*} f^{-1}(\mathcal{O}_{X}) \to \mathcal{O}_{Y_{n}}$. The pairs $(\mathcal{O}_{Y_{n}}, i_{n,m})$ form a projective
system, and the $j_{n}$ are compatible with the $i_{n,m}$.

Applying the functor $Ext^{i}_{\mathcal{O}_{X}}(X; \cdot, F)$, one deduces a morphism

```text
ϕ′: lim→_n Ext^i_{𝒪_X}(X; 𝒪_{Y_n}, F) → Ext^i_{𝒪_X}(X; f_* f^{−1}(𝒪_X), F);
```

one easily shows that this is a morphism of cohomological functors in $F$. The morphism

```text
ϕ: lim→_n Ext^i_{𝒪_X}(X; 𝒪_{Y_n}, F) → H^i_Y(X, F),
```

obtained by composing $\varphi'$ with (∗), is therefore also a morphism of cohomological functors in $F$.

<!-- original page 22 -->

One defines in the same way

```text
ϕ̲: lim→_n ℰxt^i_{𝒪_X}(𝒪_{Y_n}, F) → ℋ^i_Y(F).
```

We have in view the following theorem:

**Theorem.**

<!-- label: II.6 -->

a) Let $X$ be a locally noetherian prescheme, $Y$ a closed subset of $X$ defined by a coherent Ideal $I$, and $F$ a
quasi-coherent Module. Then `ϕ̲` is an isomorphism.

b) If $X$ is noetherian, $\varphi$ is an isomorphism.

Theorem 6 will follow from 6.a) and from:

**Lemma.**

<!-- label: II.7 -->

If the topological space underlying $X$ is noetherian and if `ϕ̲` is an isomorphism, then so is $\varphi$.

We first prove Lemma 7. We know that there is a spectral sequence

```text
H^p(X, ℋ^q_Y(F)) ⇒ H^*_Y(X, F).
```

<!-- label: eq:II.7.1 -->

On the other hand, we have an inductive system of spectral sequences

```text
H^p(X, ℰxt^q_{𝒪_X}(𝒪_{Y_n}, F)) ⇒ Ext^*_{𝒪_X}(X; 𝒪_{Y_n}, F).
```

<!-- label: eq:II.7.2n -->

It follows from the definitions of $\varphi$ and `ϕ̲` that these morphisms are associated with a homomorphism $\Phi$ of
spectral sequences from the direct limit of (7.2n) to (7.1). If the space underlying $X$ is noetherian, then by
(Godement 4.12.1)[^II-7-godement]

```text
lim→_n H^p(X, ℰxt^q_{𝒪_X}(𝒪_{Y_n}, F)) ⥲ H^p(X, lim→_n ℰxt^q_{𝒪_X}(𝒪_{Y_n}, F)),
```

so $\Phi_{2}$ can be written as a morphism

```text
H^p(X, lim→_n ℰxt^q_{𝒪_X}(𝒪_{Y_n}, F)) → H^p(X, ℋ^q_Y(F))
```

which is nothing other than the one deduced from `ϕ̲`.

If `ϕ̲` is an isomorphism, then so is $\Phi_{2}$, and consequently so is $\varphi$ by (EGA 0_III

<!-- original page 23 -->

11.1.5); Lemma 7 is therefore proved.

<!-- original page 18 -->

We shall now prove 6.a); this is a local question on $X$. By Corollary 4 and (EGA I 1.3.9 and 1.3.12) we may assume that
$X$ is the spectrum of a ring $A$. It therefore suffices to show that, under the hypotheses of Theorem 6.a), the
canonical homomorphism

```text
lim→_n Ext^i_A(A/I^n, M) → H^i_Y(X, M)
```

<!-- label: eq:II.7.3 -->

is an isomorphism.

Let $f_{\alpha}$ be a finite number of elements of $A$ generating $I$, with $f = (f_{\alpha})$; the sequence of ideals
$(f^{n})$ is then decreasing and cofinal with the sequence of $I^{n}$, so that (7.3) is equivalent to a morphism of
$\partial$-functors in $M$:

```text
lim→_n Ext^i_A(A/(f^n), M) → H^i_Y(X, M).
```

<!-- label: eq:II.7.4 -->

On the other hand, one has canonical isomorphisms

```text
lim→_n Hom_A(A/(f^n), M) ≃ lim→_n { m ∈ M | (f^n)m = 0 } ≃ H⁰((f), M).
```

<!-- label: eq:II.7.5 -->

Since $\lim\to_{n} Ext^{i}_{A}(A/(f^{n}), M)$ is a universal $\partial$-functor in $M$, there is a unique morphism of
$\partial$-functors in $M$:

```text
lim→_n Ext^i_A(A/(f^n), M) → H^i((f), M),
```

<!-- label: eq:II.7.6 -->

which coincides in degree zero with (7.5).

Since the composite of (7.3) and (5.1) is a morphism of $\partial$-functors in $M$ that coincides with (7.6) in degree
0, it coincides with (7.6) in every degree. Theorem 6.a) is therefore an immediate consequence of:

**Lemma.**

<!-- label: II.8 -->

Let $A$ be a noetherian ring, $I$ an ideal generated by a finite system $f = (f_{\alpha})$ of elements, and $M$ an
$A$-module. Then the homomorphisms (7.6) are isomorphisms.

<!-- original page 24 -->

**Lemma.**

<!-- label: II.9 -->

Let $A$ be a ring, $f = (f_{\alpha})$ a finite system of elements of $A$, $I$ the ideal generated by $f$, and $i > 0$ an
integer. The following conditions are equivalent:

a) The homomorphism (7.6) is an isomorphism for every $M$.

b) $H^{i}((f), M) = 0$ for $M$ injective.

c) The projective system $(H^{i}(f^{n}, A)) = H_{i,n}$ is essentially zero, that is: for every $n$, there exists
$n' > n$ such that $H_{i,n'} \to H_{i,n}$ is zero.

a) entails b) trivially.

b) entails a): indeed, b) implies that $M \mapsto H^{i}((f), M)$ is a universal cohomological functor, so (7.6) is then
a morphism of universal cohomological functors. It is an isomorphism in degree zero, hence in every degree.

c) entails b): indeed, if $M$ is injective, one has for every $n$

```text
H^i(f^n, M) = Hom(H^i(f^n, A), M) = Hom(H_{i,n}, M),
```

<!-- original page 19 -->

so c) implies that for every $i$ the inductive system $(H^{i}(f^{n}, M))_{n \in \mathbb{Z}}$ is essentially zero, whence
b).

b) entails c). Indeed, let $n > 0$, and let $j$ be a monomorphism of $H_{i,n}$ into an injective module $M$. Let
$n' \geqslant n$, and let $j_{n'} \in \operatorname{Hom}(H_{i,n'}, M)$ be the composite of $j$ with the transition
homomorphism $t_{n',n}: H_{i,n'} \to H_{i,n}$. The $j_{n'}$ define an element of $H^{i}((f), M)$, which is zero by
hypothesis. There therefore exists $n_{0}$ such that $j_{n'} = 0$ for $n' > n_{0}$. But since $j$ is a monomorphism,
$j_{n'} = 0$ entails $t_{n',n} = 0$, whence the proposition.

**Corollary.**

<!-- label: II.10 -->

Suppose that the space underlying $X = \operatorname{Spec}(A)$ is noetherian. In order that the preceding conditions be
satisfied for every finite family of elements of $A$ and every $i > 0$ (or equivalently: for $i = 1$), it is necessary
and sufficient that for every injective $A$-module $M$, the sheaf $F$ associated with $M$ be flasque.

It is necessary: indeed, let $f = (f_{\alpha})$ be a finite system of elements of $A$, let $Y$ be the closed subset
defined by $f$, and $U = X - Y$; one then has the exact sequence

```text
H⁰(X, F) → H⁰(U, F) → H¹((f), M) → 0,
```

and, thanks to 9.b), $H^{0}(X, F) \to H^{0}(U, F)$ is surjective.

<!-- original page 25 -->

It is sufficient by virtue of (5.1) and of the fact that for every closed subset $Y$ of $X$ and every flasque sheaf $F$
on $X$, $H^{i}_{Y}(X, F) = 0$ for $i > 0$.

**Lemma.**

<!-- label: II.11 -->

Under the hypotheses of Lemma 9, for every noetherian $A$-module $N$ and every $i > 0$, the projective system
$(H_{i,n}(N))_{n \in \mathbb{Z}}$, where $H_{i,n}(N) = H^{i}(f^{n}, N)$, is essentially zero.

Proof by induction on the number $m$ of elements of $f$.

If $m = 1$, $f$ reduces to a single element, say $f$; then $H_{i,n}(N)$ is zero for $i > 1$, and $H_{1,n}(N)$ is
canonically isomorphic to the annihilator $N_{(n)}$ of $f^{n}$ in $N$, the transition homomorphism
$N_{(n')} \to N_{(n)}$, $n' \geqslant n$, being multiplication by $f^{n' - n}$. The $N_{(n)}$ form an increasing
sequence of submodules of $N$, and since $N$ is noetherian there exists $n_{0}$ such that $N_{(n)} = N_{(n_{0})}$ for
$n \geqslant n_{0}$. Thus all the $N_{(n)}$ are annihilated by $f^{n_{0}}$, and the transition homomorphisms
$N_{(n')} \to N_{(n)}$ are all zero for $n' \geqslant n + n_{0}$. The lemma is therefore proved for $m = 1$.

We now assume that $m > 1$ and that the lemma is proved for integers $m' < m$; let then $g = (f_{1}, \cdots, f_{m-1})$
and $h = f_{m}$.

For every $n > 0$, one has (EGA III 1.1.4.1) an exact sequence

```text
0 → H⁰(h^n, H^i(g^n, N)) → H^i(f^n, N) → H¹(h^n, H^{i−1}(g^n, N)) → 0,
```

and, as $n$ varies, a projective system of exact sequences. It follows from the induction hypotheses that for $i > 0$
the $H^{i}(g^{n}, N)$ form an essentially zero projective system, and hence so do the $H^{0}(h^{n}, H^{i}(g^{n}, N))$,
which one identifies with quotients of $H^{i}(g^{n}, N)$. For the right-hand terms one factors the transition morphisms
from $n'$ to $n$ through

```text
H¹(h^{n′}, H^{i−1}(g^{n′}, N)) → H¹(h^{n′}, H^{i−1}(g^n, N)) → H¹(h^n, H^{i−1}(g^n, N)).
```

<!-- original page 20 (source page 20) -->

Since $H^{i-1}(g^{n}, N)$ is a noetherian module, it follows from the case $m = 1$ that there exists, for given $n$,

<!-- original page 26 -->

an $n' > n$ such that the second arrow is zero. We see therefore that in this projective system of exact sequences, the
outermost projective systems are essentially zero, and hence so is the middle projective system.

We have thus proved Lemma 11, hence Lemma 8, and consequently Theorem 6.

**Remark.**

<!-- label: II.remark-after-11 -->

One can also obtain Theorem 6 by establishing the condition of Corollary 10 with the help of the structure theorems for
injective modules over a noetherian ring (Matlis, Gabriel).

<!--
LEDGER DELTA (Exposé II):

| French | English | Note |
| --- | --- | --- |
| partie localement fermée | locally closed subset | Standard. |
| immersion canonique | canonical immersion | Standard. |
| suite exacte de cohomologie relative | exact sequence of relative cohomology | Standard. |
| `∂`-foncteur | `∂`-functor | Keep the partial-derivative symbol; standard derived-functor terminology. |
| foncteur cohomologique universel | universal cohomological functor | Standard. |
| système projectif essentiellement nul | essentially zero projective system | Standard SGA terminology; pinned here for cross-Exposé consistency. |
| opérateur bord | boundary operator | Standard. |
| cohomologie de Koszul | Koszul cohomology | Standard. |
| aboutissement (d'une suite spectrale) | abutment (of a spectral sequence) | Already in glossary; first use in this Exposé inside the spectral sequence `⇒` symbol. |
| Idéal cohérent (capitalisé) | coherent Ideal (capitalised) | Source capitalises Idéal and Module; preserve the capital in the translation, following SGA 1 practice. |
| Module quasi-cohérent | quasi-coherent Module | Capital preserved per source. |
-->

[^N.D.E-II-1]: *N.D.E.* The references `(I 2.4)`, `(I 2.2)`, `(I 2.3)`, `(I 2.7)` are the renumbered statements of
    Exposé I §2 in the 1968 edition; the OCR carries the older bare-number form. The reader should consult the
    corresponding statements of Exposé I directly.

[^N.D.E-II-2]: *N.D.E.* For coherence and clarity, only the equations have been numbered in parentheses.

[^N.D.E-II-3]: *N.D.E.* Recall that $H_{\bullet}(f, M)$ is the Koszul cohomology
    $H_{\bullet}(\operatorname{Hom}(K_{\bullet}(f), M))$ of $f$ (EGA III 1.1.2) with values in $M$, and that
    $H_{\bullet}((f), M)$ is the limit (loc. cit., 1.1.6.5) $\lim\to_{n} H_{\bullet}(f^{n}, M)$, the transition
    morphisms being induced by the natural morphisms $K_{\bullet}(f^{n+1}) \to K_{\bullet}(f^{n})$ (loc. cit., 1.1.6).

[^II-7-godement]: Cf. the first bibliographical reference at the end of Exposé I.


<!-- SOURCE: 03-invariants-cohomologiques-et-profondeur.md -->

# Exposé III. Cohomological invariants and depth

<!-- label: III -->

<!-- original page 27 -->

## 1. Review

<!-- label: III.1 -->

We state a few definitions and results that the reader will find, for example, in Chapter I of the course taught by
J.-P. Serre at the Collège de France in 1957–58.[^N.D.E-III-1]

**Definition.**

<!-- label: III.1.1 -->

Let $A$ be a ring (commutative with unit element, as in everything that follows) and let $M$ be an $A$-module (unitary,
as in everything that follows). One calls:

- *annihilator of $M$*, denoted `Ann M`, the set of $a \in A$ such that $am = 0$ for every $m \in M$.
- *support of $M$*, denoted `Supp M`, the set of prime ideals $p$ of $A$ such that the localization $M_{p}$ is nonzero.
- *"assassin of $M$"* or *"set of prime ideals associated with $M$"*, denoted `Ass M`, the set of prime ideals $p$ of
  $A$ such that there exists a nonzero element of $M$ whose annihilator is $p$.

If $a$ is an ideal of $A$, we shall write $r(a)$ for the radical of $a$ in $A$, i.e. the set of elements of $A$ some
power of which lies in $a$.

The following results hold under the assumption that $A$ is noetherian and $M$ is finitely generated.

**Proposition.**

<!-- label: III.1.1bis -->

1. `Ass M` is a finite set.
1. <!-- original page 28 -->
    For an element of $A$ to annihilate a nonzero element of $M$, it is necessary and sufficient that it belong to one of
    the ideals associated with $M$.
1. The radical of the annihilator of $M$, $r(Ann M)$, is the intersection of the ideals associated with $M$ that are
   minimal (for the inclusion relation in `Ass M`).

<!-- Editorial note: The source labels both the definition and the proposition that follows as "Proposition 1.1"; we
preserve the duplication and tag the second one *bis* in the spirit of the editor's note on numbering (cf. Introduction,
N.D.E. intro-1). The third assertion of this proposition is given as item (iii) in the source. -->

**Proposition.**

<!-- label: III.1.2 -->

Let $p$ be a prime ideal of $A$. The following assertions are equivalent:

1. $p \in Supp M$.
1. There exists $q \in Ass M$ such that $q \subset p$.
1. $p \supset Ann M$.
1. (iii bis) $p \supset r(Ann M)$.

**Proposition.**

<!-- label: III.1.3 -->

Let $N$ be a finitely generated $A$-module. One has the formula:

```text
Ass Hom_A(N, M) = Supp N ∩ Ass M.
```

## 2. Depth

<!-- label: III.2 -->

Throughout this paragraph, $A$ denotes a commutative ring, $I$ an ideal of $A$, and $M$, $N$ two $A$-modules. We write
$X$ for the prime spectrum of $A$ (we shall not use its structure sheaf in this paragraph) and $Y$ for the variety of
$I$, $Y = Supp(A/I) = {p \in X, p \supset I}$.

**Lemma.**

<!-- label: III.2.1 -->

Suppose that $A$ is noetherian and that the modules $M$ and $N$ are finitely generated. Suppose moreover that
$Supp N = Y$. Then the following assertions are equivalent:

1. $\operatorname{Hom}_{A}(N, M) = 0$.
1. $Supp N \cap Ass M = \emptyset$.
1. The ideal $I$ is not a zero divisor on $M$, meaning that for every $m \in M$, $Im = 0$ implies $m = 0$.
1. There exists an $M$-regular element in $I$. (An element $a$ of $A$ is said to be *$M$-regular* if multiplication by
   $a$ on $M$ is injective.)
1. For every $p \in Y$, the maximal ideal $pA_{p}$ of the local ring $A_{p}$ is not associated with $M_{p}$. In symbols:
   $pA_{p} \notin Ass M_{p}$.

*Proof.*

<!-- original page 29 -->

(i) ⇔ (ii), since $Ass \operatorname{Hom}_{A}(N, M) = \emptyset$ is equivalent to (ii) by Proposition 1.3, and to (i) by
an easy consequence of Proposition 1.2.

(iii) ⇒ (ii) by contradiction: "there exists $p \in Supp N \cap Ass M$" entails that $p \supset I$ and that there exists
$m \in M$ whose annihilator is $p$, hence $Im \subset pm = 0$, contradicting (iii).

(iv) ⇒ (iii) trivially.

(ii) ⇔ (iv), since $Supp N = Y$, so (ii) says that $I$ is contained in no ideal associated with $M$, or equivalently
(since the ideals associated with $M$ are prime and finite in number) that $I$ is not contained in the union of the
ideals associated with $M$. But by Proposition 1.1 (ii) this union is exactly the set of elements of $A$ that are not
$M$-regular.

(i) ⇒ (v): indeed, if $\operatorname{Hom}_{A}(N, M) = 0$ and if $p \in Y$, one deduces, by virtue of the formula

```text
Hom_A(N, M)_p = Hom_{A_p}(N_p, M_p),
```

that $\operatorname{Hom}_{A_{p}}(N_{p}, M_{p}) = 0$, hence, thanks to Proposition 1.3,

```text
Supp N_p ∩ Ass M_p = ∅;
```

but $pA_{p} \in Supp N_{p}$, so $pA_{p} \notin Ass M_{p}$.

(v) ⇒ (i): indeed, if $p \in Ass M$, there exists $m \in M$ whose annihilator is $p$, so the canonical image of $m$ in
$M_{p}$ is nonzero, and its annihilator is an ideal containing $p$, hence containing $pA_{p}$, hence equal to $pA_{p}$.
The ideal $pA_{p}$ is therefore associated with $M_{p}$, so $p \notin Y$ by (v), whence (i). QED

We shall now work with these conditions, replacing the functor `Hom` by its derived functors.

**Theorem.**

<!-- label: III.2.2 -->

<!-- original page 30 -->

Let $A$ be a commutative ring, $I$ an ideal of $A$, $M$ an $A$-module. Let $n$ be an integer.

a) If there exists a sequence $f_{1}, \cdots, f_{n+1}$ of elements of $I$ that is an $M$-regular sequence (i.e. $f_{1}$
is $M$-regular and $f_{i+1}$ is regular on $M/(f_{1}, \cdots, f_{i})M$ for $i \leqslant n$), then for every $A$-module
$N$ annihilated by a power of $I$, one has:

```text
Ext^i_A(N, M) = 0 for i ⩽ n.
```

b) If moreover $A$ is noetherian, $M$ is finitely generated, and there exists a finitely generated $A$-module $N$ such
that $Supp N = V(I)$ and $Ext^{i}_{A}(N, M) = 0$ for $i \leqslant n$, then there exists a sequence
$f_{1}, \cdots, f_{n+1}$ of elements of $I$ that is $M$-regular.

Let us prove a) first, by induction. If $n < 0$ the statement is empty.

Suppose $n \geqslant 0$, and that a) has been proved for $n' < n$. By hypothesis there exists $f_{1} \in I$ that is
$M$-regular. Denote by $f^{i}_{1}$ multiplication by $f_{1}$ on $Ext^{i}_{A}(N, M)$, and by $f^{M}_{1}$ multiplication
by $f_{1}$ on $M$. The sequence

```text
0 ⟶ M ──f_1^M──→ M ⟶ M/f_1 M ⟶ 0
```

<!-- label: eq:III.2.1 -->

is exact, hence so is the sequence:

```text
Ext^{i−1}_A(N, M/f_1 M) ──δ──→ Ext^i_A(N, M) ──f_1^i──→ Ext^i_A(N, M).
```

By hypothesis $I^{r} N = 0$, so $f^{0}_{1}$ is nilpotent; since $Ext^{i}$ is a universal functor, the same holds for
$f^{i}_{1}$ for every $i$. On the other hand, there is a regular sequence in $M/f_{1} M$ of length $n$, so by the
induction hypothesis,

```text
Ext^{i−1}_A(N, M) = 0 if i ⩽ n − 1.
```

<!-- Editorial note: The source displays `Ext^{i−1}_A(N, M) = 0` here, but the intended module is `M/f_1 M`. We retain
the source as printed; the argument that follows uses what the induction hypothesis provides, namely vanishing for
`M/f_1 M`. -->

One deduces that if $i \leqslant n$, then $f^{i}_{1}$ is at once nilpotent and injective, hence $Ext^{i}_{A}(N, M) = 0$.

Let us prove b), also by induction. If $n < 0$, the statement is empty.

<!-- original page 31 -->

If $n = 0$, b) follows from the implication (i) ⇒ (iv) of Lemma 2.1.

If $n > 0$, by b) for $n = 0$ there exists an element $f_{1} \in I$ that is $M$-regular; from the exact sequence (2.1)
one deduces the exact sequence:

```text
Ext^{i−1}_A(N, M) ⟶ Ext^{i−1}_A(N, M/f_1 M) ⟶ Ext^i_A(N, M).
```

<!-- label: eq:III.2.2 -->

One concludes that the hypotheses of b) are satisfied for the module $M/f_{1} M$ and the integer $n - 1$. By the
induction hypothesis, there exists a sequence of $n$ elements of $I$ that is $M/f_{1} M$-regular, which entails that
there exists a sequence of $n + 1$ elements of $I$, beginning with $f_{1}$, that is $M$-regular.

This theorem invites us to generalize, as follows, the classical definition of the depth of a finitely generated module
over a noetherian ring:

**Definition.**

<!-- label: III.2.3 -->

Let $A$ be a commutative ring with unit, $M$ an $A$-module, $I$ an ideal of $A$. One calls the *$I$-depth of $M$*, and
denotes $prof_{I} M$, the supremum in $\mathbb{N} \cup {+\infty}$ of the set of natural integers $n$ such that for every
finitely generated $A$-module $N$ annihilated by a power of $I$, one has

```text
Ext^i_A(N, M) = 0 for every i < n.
```

One deduces from the previous theorem that if $n$ is the supremum of the lengths of $M$-regular sequences of elements of
$I$, one has $n \leqslant prof_{I} M$. More precisely:

**Proposition.**

<!-- label: III.2.4 -->

Let $A$ be a commutative ring, $I$ an ideal of $A$, $M$ an $A$-module, and $n \in \mathbb{N}$. Consider the assertions:

1. $n \leqslant prof_{I} M$.

1. For every finitely generated $A$-module $N$ annihilated by a power of $I$, one has:

    ```text
    Ext^i_A(N, M) = 0 for i < n.
    ```

1. <!-- original page 32 -->

    There exists a finitely generated $A$-module $N$ such that $Supp N = V(I)$ and $Ext^{i}_{A}(N, M) = 0$ for $i < n$.

1. There exists an $M$-regular sequence of length $n$ formed of elements of $I$.

The following logical implications hold:

```text
(1) ⇐⇒ (2)
        ⇓
       (3) ⇐= (4)
```

<!-- Editorial note: The source's implication diagram shows (1) ⇔ (2), (2) ⇒ (3), and (4) ⇒ (2); we render this as a
two-line ASCII diagram. -->

Moreover, if $A$ is noetherian and $M$ is finitely generated, these conditions are equivalent.

*Proof.*

(1) ⇔ (2) by definition, and (2) ⇒ (3) by taking $N = A/I$. Moreover (4) ⇒ (2) by Theorem 2.2 a). Finally, if $A$ is
noetherian and $M$ is finitely generated, (3) ⇒ (4) by Theorem 2.2 b).

We assume $A$ noetherian and $M$ finitely generated until the end of this paragraph.

**Corollary.**

<!-- label: III.2.5 -->

Let $f \in I$ be an $M$-regular element. One has:

```text
prof_I M = prof_I(M/f M) + 1.
```

Indeed, if $n \leqslant prof_{I}(M/f M)$, there exists a sequence of elements of $I$, $f_{1}, \cdots, f_{n}$, that is
$(M/f M)$-regular, so the sequence $f, f_{1}, \cdots, f_{n}$ is $M$-regular, hence $n + 1 \leqslant prof_{I} M$, hence
$prof_{I} M \geqslant prof_{I}(M/f M) + 1$. On the other hand, by the exact sequence (2.2), if $i \leqslant prof_{I} M$
one has $Ext^{i-1}_{A}(N, M/f M) = 0$, hence $prof_{I} M - 1 \leqslant prof_{I}(M/f M)$.

**Corollary.**

<!-- label: III.2.6 -->

Every finite $M$-regular sequence formed of elements of $I$ may be extended to a maximal $M$-regular sequence, whose
length is necessarily equal to the $I$-depth of $M$.

**Remark.**

<!-- label: III.2.7 -->

<!-- original page 33 -->

One can scarcely keep oneself from saying that an $A$-module is the more beautiful the greater its depth. A module whose
support does not meet $V(I)$ is among the most beautiful; indeed, one can show that for $prof_{I} M$ to be finite, it is
necessary and sufficient that $Supp M \cap V(I) \neq \emptyset$.

**Remark.**

<!-- label: III.2.8 -->

If $A$ is a semi-local ring, let $r(A)$ be its radical and $k = A/r(A)$ its residue ring. The interesting notion of
depth is obtained by taking for $I$ the radical of $A$. We shall therefore agree to write simply `prof M` for the
$r(A)$-depth of an $A$-module $M$. One recovers in this case the notion of *homological codimension* (cf. Serre, op.
cit. note [^N.D.E-III-1], p. 21), denoted $codh_{A} M$, defined as the infimum of integers $i$ such that
$Ext^{i}_{A}(k, M) \neq 0$; indeed $Supp k = V(r(A))$.

**Proposition.**

<!-- label: III.2.9 -->

If $A$ is noetherian and $M$ is finitely generated, one has:

```text
prof_I M = inf_{p ∈ V(I)} prof M_p.
```

**Corollary.**

<!-- label: III.2.10 -->

If $A$ is a noetherian semi-local ring and $M$ is a finitely generated $A$-module, one has:

```text
prof M = inf_m prof M_m,
```

where $m$ ranges over the maximal ideals of $A$.

The corollary follows at once from Proposition 2.9; indeed, the prime ideals that contain the radical are precisely the
maximal ideals.

Moreover, let $f \in I$. If $f$ is $M$-regular, if $p \in X$ and $p \supset I$, then the image $g$ of $f$ in $A_{p}$
lies in $pA_{p}$, the maximal ideal of $A_{p}$; and $g$ is $M_{p}$-regular, as follows from the exact sequence

```text
0 ⟶ M_p ──g′──→ M_p ⟶ (M/f M)_p ⟶ 0,
```

<!-- label: eq:III.2.3 -->

where $g'$ denotes multiplication by $g$ on $M_{p}$. This exact sequence also gives that $(M/f M)_{p}$ is isomorphic to
$M_{p}/gM_{p}$; applying Corollary 2.5 to $M$ and to $M_{p}$, one deduces, by induction, that
$prof_{I} M \leqslant \nu(M)$, where one has set, for every $M$:

<!-- original page 34 -->

```text
ν(M) = inf_{p ∈ V(I)} prof M_p.
```

More precisely, still by induction, one knows that if $f$ is $M$-regular, then $\nu(M) = \nu(M/f M) + 1$; it remains
therefore to show that if $\nu(M) \geqslant 1$, there exists an $M$-regular element in $I$. But applying Lemma 2.1 to
$M_{p}$, $A_{p}$, and $pA_{p}$ for each $p \in V(I)$, one sees that $pA_{p} \notin Ass M_{p}$; hence, applying Lemma 2.1
to $A$, $M$, and $I$, the conclusion follows.

**Proposition.**

<!-- label: III.2.11 -->

Let $u: A \to B$ be a homomorphism of noetherian rings. Let $I$ be an ideal of $A$, $M$ a finitely generated $A$-module.
Set $IB = I \otimes_{A} B$ and $M_{B} = M \otimes_{A} B$. If $B$ is $A$-flat, one has:

```text
prof_{IB} M_B ⩾ prof_I M;
```

moreover, if $B$ is faithfully flat over $A$, one has equality.

Indeed, let $N = A/I$. By flatness, $N \otimes_{A} B = B/IB$; set $N_{B} = N \otimes_{A} B$. Again by flatness and the
noetherian hypotheses, one has:

```text
Ext^i_B(N_B, M_B) = Ext^i_A(N, M) ⊗_A B,
```

so $Ext^{i}_{A}(N, M) = 0$ implies $Ext^{i}_{B}(N_{B}, M_{B}) = 0$, and the converse holds if $B$ is faithfully flat
over $A$.

## 3. Depth and topological properties

<!-- label: III.3 -->

**Lemma.**

<!-- label: III.3.1 -->

Let $X$ be a topological space, $Y$ a closed subspace, $F$ a sheaf of abelian groups on $X$. Set $U = X - Y$. Let $n$ be
an integer. The following conditions are equivalent:

1. <!-- original page 35 -->

    $H^{i}_{Y}(X, F) = 0$ for $i < n$.

1. For every open $V$ of $X$, the homomorphism of groups

    ```text
    H^i(V, F) ⟶ H^i(V ∩ U, F)
    ```

    is bijective for $i < n - 1$ and injective for $i = n - 1$.

1. For every open $V$ of $X$,

    ```text
    H^i_{Y ∩ V}(V, F|V) = 0 for i < n.
    ```

*Proof.*

(ii) ⇔ (iii): indeed, let $V$ be an open of $X$, set $X' = V$, $Y' = Y \cap V$, $F' = F|V$, $U' = X' - Y'$. Then $Y'$ is
closed in $X'$, so one has an exact sequence:

```text
H^i_{Y′}(X′, F′) ⟶ H^i(X′, F′) ──ρ^i──→ H^i(U′, F′) ⟶ H^{i+1}_{Y′}(X′, F′).
```

If the outer terms vanish, the homomorphism $\rho^{i}$ is bijective; and if the left-hand term vanishes, $\rho^{i}$ is
injective. So (iii) ⇒ (ii). Conversely, if $i < n$, then $H^{i}_{Y'}(X', F')$ vanishes because $\rho^{i}$ is injective
and $\rho^{i-1}$ is surjective.

(i) ⇒ (iii): indeed, the "local-to-global" spectral sequence gives:

```text
H^p(X, ℋ^q_Y(X, F)) ⟹ H^*_Y(X, F).
```

<!-- Editorial note: The source writes `H^q_Y(X, F)` for the sheafified `ℋ^q_Y(F)` (the underline is lost by OCR). The
abutment is `H^*_Y(X, F)`; per the SGA 2 conventions adopted for this translation, the sheafified functor on the
spectral sequence's `E_2` page is rendered with script `ℋ`. -->

Now, by hypothesis $\mathcal{H}^{q}_{Y}(X, F) = 0$ for $q < n$, hence $H^{p+q}_{Y}(X, F) = 0$ for $p + q < n$.

(iii) ⇒ (i): indeed, (iii) says that the presheaf

```text
V ⟼ H^i_{Y ∩ V}(V, F|V)
```

is zero, hence so is the associated sheaf, which is $\mathcal{H}^{i}_{Y}(X, F)$, since $Y$ is closed.

**Remark.**

<!-- label: III.3.2 -->

<!-- original page 36 -->

The equivalence of (i) and (ii) was proved in Proposition I 2.13. As remarked there, if $n \geqslant 2$, one may omit
the condition that $\rho^{n-1}$ be injective.[^N.D.E-III-2]

**Proposition.**

<!-- label: III.3.3 -->

Let $X$ be a locally noetherian prescheme, $Y$ a closed subprescheme of $X$, and $F$ a coherent
$\mathcal{O}_{X}$-module. The conditions of Lemma 3.1 are equivalent to each of the following:

1. (iv) For every $x \in Y$, one has $prof F_{x} \geqslant n$.

1. (v) For every coherent $\mathcal{O}_{X}$-module $G$ on $X$ whose support is contained in $Y$, one has

    ```text
    Ext^i_{𝒪_X}(G, F) = 0 for i < n;
    ```

1. (vi) There exists a coherent $\mathcal{O}_{X}$-module $G$ whose support is equal to $Y$ such that

    ```text
    Ext^i_{𝒪_X}(G, F) = 0 for i < n.
    ```

If $X$ is affine, all the work has been done (cf. Proposition 2.4) to establish the equivalence of the three conditions
of Proposition 3.3. These conditions are local, except for the implication (v) ⇒ (vi); but in that case one may take
$G = \mathcal{O}_{Y}$ and invoke Proposition 2.4 again. It therefore suffices to prove (i) ⇒ (vi) and (v) ⇒ (i).

Let $J$ be the ideal of $Y$: it is a coherent sheaf of ideals. Set $\mathcal{O}^{m}_{Y} = \mathcal{O}_{X}/J^{m+1}$: this
is a coherent $\mathcal{O}_{X}$-module whose support is equal to $Y$, and one knows (Theorem II 6.b) that

```text
ℋ^i_Y(X, F) = lim_{→ m} Ext^i_{𝒪_X}(𝒪_Y^m, F),
```

<!-- Editorial note: The source writes `H^i_Y(X, F)` here for the sheafified Ext-limit; per the convention adopted in
this translation, the sheafified version is rendered as `ℋ^i_Y`. -->

so (v) ⇒ (i). Moreover, the transition morphisms in the projective system of the $\mathcal{O}^{m}_{Y}$ are epimorphisms.

<!-- original page 37 -->

If the functor $Ext^{i}$ is left exact in its first argument — at least when this argument is taken in the category of
coherent $\mathcal{O}_{X}$-modules with support contained in $Y$ — then the transition morphisms of the inductive system
obtained by applying $Ext^{i}$ to the $\mathcal{O}^{m}_{Y}$ will be injective; but (i) entails that the limit is zero,
so (i) will entail that the modules $Ext^{i}_{\mathcal{O}_{X}}(\mathcal{O}^{m}_{Y}, F)$ are zero for every $m$. We argue
by induction. The statement is trivial for $n < 0$. Suppose (i) ⇒ (vi) for $n < q$, then (i) ⇒ (v), so, by the long
exact sequence of `Ext`, $Ext^{q}$ is left exact in its first argument, hence the modules
$Ext^{q}_{\mathcal{O}_{X}}(\mathcal{O}^{m}_{Y}, F)$ are zero for every $m$. So (i) ⇒ (vi) for $n \leqslant q$. QED

**Example.**

<!-- label: III.3.4 -->

Let $A$ be a noetherian local ring, $m$ its maximal ideal, $M$ a finitely generated $A$-module, and $n$ an integer. Set
$X = \operatorname{Spec}(A)$, $Y = {m}$, $U = X - Y$. Let $F$ be the sheaf associated with $M$. The following conditions
are equivalent:

1. $prof M \geqslant n$.

1. The natural homomorphism

    ```text
    H^i(X, F) ⟶ H^i(U, F)
    ```

    is injective for $i = n - 1$ and bijective for $i < n - 1$.

1. $Ext^{i}_{A}(k, M) = 0$ for $i < n$, where $k = A/m$.

1. $H^{i}_{Y}(X, F) = 0$ for $i < n$.

Taking Remark 3.2 into account, one obtains:

**Corollary.**

<!-- label: III.3.5 -->

Let $X$ be a locally noetherian prescheme, $Y$ a closed subprescheme of $X$, $F$ a coherent $\mathcal{O}_{X}$-module.
The following conditions are equivalent:

1. For every $x \in Y$, $prof F_{x} \geqslant 2$.

1. <!-- original page 38 -->

    For every open $V$ of $X$, the natural homomorphism

    ```text
    H^0(V, F) ⟶ H^0(V ∩ (X − Y), F)
    ```

    is bijective.

**Theorem (Hartshorne).**

<!-- label: III.3.6 -->

Let $X$ be a locally noetherian prescheme, $Y$ a closed subprescheme of $X$. Suppose that, for every $x \in Y$,
$prof \mathcal{O}_{X,x} \geqslant 2$; then the natural map

$$
\pi_{0}(X) \longrightarrow \pi_{0}(X - Y)
$$

is bijective.

*Proof.* Since $X$ is locally noetherian, $X$ is locally connected; it therefore suffices to prove that for $X$ to be
connected it is necessary and sufficient that $X - Y$ be. Now, for a ringed space in local rings $(X, \mathcal{O}_{X})$
to be connected, it is necessary and sufficient that $H^{0}(X, \mathcal{O}_{X})$ not be a direct product of two nonzero
rings. But the hypothesis implies, by Corollary 3.5 applied to $F = \mathcal{O}_{X}$, that the homomorphism

```text
H^0(X, 𝒪_X) ⟶ H^0(X − Y, 𝒪_X)
```

is an isomorphism, whence the conclusion.

**Corollary.**

<!-- label: III.3.7 -->

Let $X$ be a locally noetherian prescheme. Let $d$ be an integer such that $\dim \mathcal{O}_{X,x} \geqslant d$ implies
$prof \mathcal{O}_{X,x} \geqslant 2$. Then, if $X$ is connected, $X$ is connected in codimension $d - 1$, i.e. if $X'$
and $X''$ are two irreducible components of $X$, there exists a sequence of irreducible components of $X$:

```text
X′ = X_0, X_1, …, X_n = X″
```

such that for every $i$ with $0 \leqslant i < n$, the codimension of $X_{i} \cap X_{i+1}$ in $X$ is at most $d - 1$.

<!-- original page 39 -->

Note first that if $X$ is Cohen-Macaulay, then $d = 2$ enjoys the property invoked above. In this connection, recall
that one defines the codimension of $Y$ in $X$ as the infimum of the dimensions of the local rings in $X$ at the points
of $Y$.

*Proof.* Let $\mathcal{F}$ be the collection of closed subsets of $X$ whose codimension in $X$ is at least $d$. One
notes that $\mathcal{F}$ is an antifilter of closed subsets of $X$. Moreover, for a closed $Y \subset X$ to belong to
$\mathcal{F}$, it is necessary and sufficient that, for every $y \in Y$, there exist an open neighborhood $V$ of $y$ in
$X$ such that $Y \cap V$ has codimension $\geqslant d$ in $V$. Finally, if $X$ is connected and $Y \in \mathcal{F}$,
then $X - Y$ is connected by Hartshorne's theorem. The corollary thus follows from the next lemma, which is of a purely
topological nature.

<!-- Editorial note: The source writes "il existe un voisinage ouvert V de X" ("an open neighborhood V of X"); the
sense requires "of `y`", which we have restored. -->

**Lemma.**

<!-- label: III.3.8 -->

Let $X$ be a connected, locally noetherian topological space, and let $\mathcal{F}$ be an antifilter of closed subsets
of $X$. Suppose that every closed $Y \subset X$ that locally belongs to $\mathcal{F}$ (i.e. for every point $x \in X$
there exist an open neighborhood $V$ of $x$ in $X$ and a $Y' \in \mathcal{F}$ such that $V \cap Y = V \cap Y'$) belongs
to $\mathcal{F}$. The following conditions are equivalent:

1. For every $Y \in \mathcal{F}$, $X - Y$ is connected.
1. If $X'$ and $X''$ are two distinct irreducible components of $X$, there exists a sequence of irreducible components
   of $X$, $X_{0}, X_{1}, \cdots, X_{n}$, such that $X' = X_{0}$, $X'' = X_{n}$ and, for each $i$ with
   $1 \leqslant i < n$, $X_{i} \cap X_{i+1} \notin \mathcal{F}$.

(ii) ⇒ (i). Let $Y \in \mathcal{F}$; we must show that the open set $U = X - Y$ is connected. Now, if $U'$ and $U''$ are
two irreducible components of $U$, there exist two irreducible components $X'$ and $X''$ of $X$ such that
$X' \cap U = U'$ and $X'' \cap U = U''$. Let $X_{0}, \cdots, X_{n}$ be a sequence of irreducible components of $X$
having the property invoked above; if one sets $U_{i} = X_{i} \cap U$ for $0 \leqslant i \leqslant n$, the $U_{i}$ are
irreducible components of $U$, and moreover $U_{i} \cap U_{i+1}$ is nonempty for $0 \leqslant i < n$, since otherwise
$X_{i} \cap X_{i+1} \subset Y$ would be an element of $\mathcal{F}$, contrary to the choice of the sequence of the
$X_{i}$. This entails that $U$ is connected.

<!-- original page 40 -->

(i) ⇒ (ii). Let $Y = \bigcup_{X', X''} X' \cap X''$, where one requires $X'$ and $X''$ to be two distinct irreducible
components of $X$ such that $X' \cap X'' \in \mathcal{F}$. The family of the $X' \cap X''$ is locally finite since $X$
is locally noetherian; moreover the $X' \cap X''$ are closed, so $Y$ is closed. Also, $Y$ belongs locally to
$\mathcal{F}$, so $Y \in \mathcal{F}$. Hence $U = X - Y$ is connected. Let $X'$ and $X''$ be two distinct irreducible
components of $X$, and let $U'$ and $U''$ be their traces on $U$, which are nonempty by construction of $Y$. These are
irreducible components of $U$; but $U$ is connected, so, $U$ being locally noetherian, there exists a sequence of
irreducible components $U_{0}, \cdots, U_{n}$ of $U$ such that $U_{0} = U'$, $U_{n} = U''$,
$U_{i} \cap U_{i+1} \neq \emptyset$, and $U_{i} \cap U_{i+1} \neq U_{i}$ for $0 \leqslant i < n$. Let
$X_{0}, \cdots, X_{n}$ be the sequence of irreducible components of $X$ such that $X_{i} \cap U = U_{i}$; if
$X_{i} \cap X_{i+1} \in \mathcal{F}$, then by the construction of $\mathcal{F}$ one would have
$U_{i} \cap U_{i+1} = \emptyset$ or $U_{i} = U_{i+1}$, which is impossible by the choice of the $U_{i}$. QED

**Corollary.**

<!-- label: III.3.9 -->

Let $A$ be a noetherian local ring. Suppose that for every prime ideal $p$ of $A$ one has:

```text
(dim A_p ⩾ 2) ⟹ (prof A_p ⩾ 2).
```

Suppose moreover that $A$ satisfies the chain condition.[^III-3-1] Then, for every minimal prime ideal $p$ of $A$,
$\dim A/p = \dim A$, or equivalently, all the irreducible components of $\operatorname{Spec} A$ have the same dimension:
that of $A$.

If $X'$ and $X''$ are two irreducible components of $X$, one joins them by a chain having the properties enumerated in
Corollary 3.7; it then suffices to show that two successive components have the same dimension, which follows from the
second hypothesis.

**Example.**

<!-- label: III.3.10 -->

<!-- original page 41 -->

Let $X$ be the union of two complementary linear subspaces, of respective dimensions 2 and 3, in a vector space of
dimension 5; more precisely, let $X = \operatorname{Spec} A$, with $A = B/p \cap q$, where
$B = k[X_{1}, \cdots, X_{5}]$, $p$ is the ideal generated by $X_{1}, X_{2}, X_{3}$ and $q$ the ideal generated by `X_4`
and `X_5`. Then $X$ can be disconnected by the intersection point $x$ of the two linear subspaces, so the depth of
$\mathcal{O}_{X,x}$ is equal to 1, since it cannot be $\geqslant 2$ by Theorem 3.6. Another reason: the
equidimensionality conclusion of the previous corollary fails.

More generally, taking a union $X$ of two linear subspaces of dimensions $p, q \geqslant 2$ in a vector space of
dimension $p + q$, for no embedding of $X$ in a regular scheme is $X$ even set-theoretically a complete intersection at
the origin: for (possibly modifying it without changing the underlying topological space in a neighborhood of the
origin), $X$ would be Cohen-Macaulay, hence of depth $\geqslant 2$ at the origin, which is not the case.

**Remark.**

<!-- label: III.3.11 -->

Let $X$ be a locally noetherian prescheme, $Y$ a closed subprescheme of $X$, $F$ an $\mathcal{O}_{X}$-module. Depth is a
purely topological notion, expressed in terms of the vanishing of the $H^{i}_{Y}(X, F)$ for $i < n$. One also wishes to
study these sheaves for a given $i$, or for $i > n$. In this connection one proves the following result:

**Lemma.**

<!-- label: III.3.12 -->

Let $m$ be an integer. For $H^{i}_{Y}(X, F) = 0$, $i > m$, to hold for every coherent $F$, it is necessary and
sufficient that it hold for $F = \mathcal{O}_{X}$.

By inductive limit, the property then holds for every quasi-coherent sheaf. For instance, if $Y$ can be described
locally by $m$ equations, or, as one says, if $Y$ is locally set-theoretically a complete intersection (which occurs for
example if $X$ and $Y$ are non-singular), it follows from the computation of the $H^{i}_{Y}(X, F)$ by the Koszul complex
that these sheaves are zero for $i > m$. We have, moreover, used this fact implicitly in Example 3.10.

<!-- original page 42 -->

This cohomological condition is, however, not sufficient, as the next example shows.

**Example.**

<!-- label: III.3.13 -->

Let $X = \operatorname{Spec}(A)$, where $A$ is a normal noetherian local ring of dimension 2. Let $Y$ be a curve in $X$.
One can show that the complement of the curve is an affine open, so[^N.D.E-III-3]
$H^{i}_{Y}(\mathcal{O}_{X}) \cong H^{i-1}_{X-Y}(\mathcal{O}_{X}) = 0$ for $i > 1$, since
$H^{i-1}(X - Y, \mathcal{O}_{X}) = 0$. Nevertheless, one can construct a curve that is not described by a single
equation.

We shall seek[^III-3-2] conditions for the $H^{i}_{Y}(X, F)$ to be coherent for a given $i$, which is not the case in
general, as obvious examples show — for instance $H^{n}_{m}(A)$ for $A$ a noetherian local ring of dimension $n > 0$;
for example when $A$ is a discrete valuation ring with field of fractions $K$, one finds $H^{1}_{m}(A) \simeq K/A$,
which is not a finitely generated module over $A$. To enlighten the reader, let us say that the problem posed is
equivalent to the following: let $f: U \to X$ be an open immersion, let $G$ be a coherent sheaf on $U$; find criteria
for the higher direct images $R^{i} f_{*} G$ to be coherent sheaves on $X$ for a given $i$. These conditions are
necessary for the use of formal geometry that we saw in Exposé IX and the following ones.

<!--
LEDGER DELTA (Exposé III):
| French | English | Note |
| ------ | ------- | ---- |
| Rappels | Review | Section title. |
| annulateur | annihilator | Standard. |
| support | support | Standard. |
| assassin de M | "assassin of `M`" | Bourbaki idiom; kept with quotes to preserve the figure of speech and the explanatory gloss that follows. |
| ensemble des idéaux premiers associés à M | set of prime ideals associated with `M` | Per source. |
| racine de a | radical of `a` | Modern English; the symbol `r(a)` is kept. |
| de type fini | finitely generated | Module-level rendering. |
| profondeur | depth | Per glossary. |
| `I`-profondeur | `I`-depth | Per glossary; notation `prof_I M` preserved. |
| `M`-régulier | `M`-regular | Per glossary. |
| diviseur de 0 | zero divisor | Standard. |
| homothétie de rapport a | multiplication by `a` | English mathematical idiom; "homothety of ratio `a`" is unidiomatic in module-theoretic prose. |
| suite régulière | regular sequence | Standard. |
| foncteur universel | universal functor | Standard (in the sense of Grothendieck's *Tôhoku*: an exact connected sequence of functors that vanishes on injectives). |
| anneau semi-local | semi-local ring | Standard. |
| radical | radical | Standard; `r(A)` preserved. |
| codimension homologique | homological codimension | Per source; alongside the more modern *depth*. |
| codh_A M | `codh_A M` | Symbol preserved. |
| platitude / fidèlement plat | flatness / faithfully flat | Standard. |
| antifiltre | antifilter | Loanword from order theory; "antifilter of closed subsets" preserved as in source. |
| chaîne | chain | "Chain condition" for *condition des chaînes*; cross-reference to EGA 0_IV preserved. |
| Cohen-Macaulay | Cohen-Macaulay | Standard. |
| composante irréductible | irreducible component | Standard. |
| connexe en codimension d−1 | connected in codimension `d − 1` | Standard. |
| sous-espace vectoriel supplémentaire | complementary linear subspace | The vector-space sense ("complementary" = direct-sum complement). |
| ensemblistement | set-theoretically | Standard. |
| intersection complète | complete intersection | Standard. |
| image directe supérieure | higher direct image | Standard; notation `R^i f_*` preserved. |
| « passage du local au global » (suite spectrale) | "local-to-global" spectral sequence | Quoted in source; quotes preserved. |
| coquille | typo | N.D.E. footnote 3. |
| théorème de Hartshorne | Hartshorne's theorem | Attribution preserved per glossary. |
| spectre premier | prime spectrum | Per source. |
| condition des chaînes | chain condition | Per EGA 0_IV reference. |
| antifiltre | antifilter | Same as above. |
-->

[^N.D.E-III-1]: *N.D.E.* The reissue of Serre's text (Serre J.-P., *Algèbre locale. Multiplicités*, course at the
    Collège de France, 1957–1958, written up by Pierre Gabriel, second edition, *Lect. Notes in Math.*, vol. 11,
    Springer-Verlag, 1965) no longer contains the proofs of these statements. The reader may consult (Bourbaki N.,
    *Algèbre commutative*, Masson), as Serre himself suggests.

[^N.D.E-III-2]: *N.D.E.* The original edition gave a proof, not entirely correct.

[^III-3-1]: Cf. EGA 0_IV 14.3.2.

[^N.D.E-III-3]: *N.D.E.* There was a typo in the original edition.

[^III-3-2]: Cf. Exp. VIII.


<!-- SOURCE: 04-modules-et-foncteurs-dualisants.md -->

# Exposé IV. Dualizing modules and dualizing functors

<!-- label: IV -->

<!-- original page 43 -->

## 1. Generalities on module functors

<!-- label: IV.1 -->

Let

- $A$ be a commutative noetherian ring,
- $C$ the category of $A$-modules of finite type,
- $C'$ the category of arbitrary $A$-modules,
- `Ab` the category of abelian groups.

The aim of this section is the study of certain properties of functors $T : C^{\circ} \to Ab$ (assumed additive). Here
$C^{\circ}$ denotes the opposite category of $C$.

Note that if $M \in Ob C$, then $T(M)$ may be canonically endowed with a structure of $A$-module, defined as follows: if
$f_{M}$ is the homothety of $M$ associated to $f \in A$, then $A$ acts on $T(M)$ by $f_{T(M)}$. In other words, $T$
factors as

```text
                         T
        C°  ───────────────────────────►  Ab
           \                            ↗
            \                        /
         T°  \                  /
              \              /
               ▼          /
                  C′
```

where $C' \to Ab$ is the canonical functor. In what follows, $T(M)$ will always be considered as endowed with this
$A$-module structure.

<!-- Editorial note: source diagram is ASCII art with @@/~~~ glyphs; rendered above as a labeled commutative
triangle. -->

Composing with the isomorphism $M \xrightarrow{\sim} \operatorname{Hom}_{A}(A, M)$ the morphism
$\operatorname{Hom}_{A}(A, M) \to \operatorname{Hom}_{A}(T(M), T(A))$, one obtains the following morphisms, each deduced
from the other in an obvious way:

$$
M \longrightarrow \operatorname{Hom}_{A}(T(M), T(A)),
M \times T(M) \longrightarrow T(A),
T(M) \longrightarrow \operatorname{Hom}_{A}(M, T(A)),
$$

and this defines a morphism $\phi_{T}$ of contravariant functors:

```text
φ_T : T ⟶ Hom_A(−, T(A)).
```

<!-- original page 44 -->

**Proposition.**

<!-- label: IV.1.1 -->

The following two properties are equivalent:

1. $\phi_{T}$ is an isomorphism of functors.
1. $T$ is left exact.

The implication (i) ⇒ (ii) is trivial.

The implication (ii) ⇒ (i) follows from the fact that, for a morphism $u : F \to F'$ of two additive left exact functors
$F$ and $F'$ from $C^{\circ}$ to `Ab`, if $u(A)$ is an isomorphism, then $u$ is an isomorphism (one uses the fact that
$A$ is noetherian, hence that every $A$-module of finite type is of finite presentation).

**Remark.**

<!-- label: IV.1.2 -->

This shows in particular that the representable functors $T : C'^{\circ} \to Ab$ are precisely those that commute with
arbitrary inverse limits (over a preordered set, not necessarily filtered).

If $\operatorname{Hom}(C^{\circ}, Ab)_{g}$ denotes the full subcategory of $\operatorname{Hom}(C^{\circ}, Ab)$ whose
objects are the left exact functors, one has proved the equivalence of categories

$$
C' \xrightarrow{\sim} \operatorname{Hom}(C^{\circ}, Ab)_{g}
$$

via the quasi-inverse functors

$$
H \mapsto \operatorname{Hom}_{A}(-, H)
$$

and

$$
T \mapsto T(A).
$$

Now let $J$ be an ideal of $A$, let $Y = V(J) \subset \operatorname{Spec} A$, and denote by `C_Y` the full subcategory
of $C$ whose objects are the $A$-modules $M$ of finite type such that $Supp M \subset Y$. One has

$$
C_{Y} = \bigcup_{n} C^{(n)},
$$

where $C^{(n)}$ is the full subcategory of `C_Y` consisting of the modules $M$ such that $J^{n} M = 0$.

<!-- original page 45 -->

**Proposition.**

<!-- label: IV.1.3 -->

With the same notation as above, let $T : C^{\circ}_{Y} \to Ab$ be a functor. To
$H = \varinjlim T(A/J^{n})$[^N.D.E-IV-1] is associated a natural morphism

```text
φ_T : T ⟶ Hom_A(−, H),
```

and the following conditions are equivalent:

1. $\phi_{T}$ is an isomorphism.
1. The functor $T$ is left exact.

*Proof.* — a) *Definition of* $\phi_{T}$.

Let $M \in Ob C_{Y}$. There exists an integer $n$ such that $J^{n} M = 0$. Then $M$ is an $A/J^{n}$-module, and if
$T_{n}$ denotes the restriction of $T$ to $C^{(n)}$, one knows how to define the morphism

```text
T_n ⟶ Hom_A(−, H_n),    where H_n = T(A/J^n);
```

<!-- original page 46 -->

whence

```text
T(M) = T_n(M) ⟶ Hom_A(M, lim_→ H_n) = Hom_A(M, H)
```

and

```text
φ_T : T ⟶ Hom_A(−, H).
```

b) *Equivalence of (i) and (ii).*

It is clear that (i) implies (ii). Suppose (ii) holds and let $M \in Ob C^{(n)}$. We have seen that
$T_{n}(M) \xrightarrow{\sim} \operatorname{Hom}_{A}(M, H_{n})$; hence for every integer $n' > n$ one has

```text
T(M) = T_n(M) = T_{n′}(M) = lim_→ T_n(M),
```

and

```text
T(M) = lim_→ Hom_A(M, H_n).
```

Since these are filtered direct limits, one also has the isomorphism

```text
lim_→ Hom_A(M, H_n) ⥲ Hom_A(M, lim_→ H_n) = Hom_A(M, H).
```

If $C'_{Y}$ denotes the category of $A$-modules with support contained in $Y$, but not necessarily of finite type, one
again has the natural equivalence of categories

$$
C'_{Y} \xrightarrow{\sim} \operatorname{Hom}(C^{\circ}_{Y}, Ab)_{g}.
$$

*Application.* — With the same notation, let

$$
T^{\bullet} : C^{\circ}_{Y} \longrightarrow Ab
$$

be an exact $\partial$-functor. For every $i \in \mathbb{Z}$, set $H^{i}_{n} = T^{i}(A/J^{n})$ and
$H^{i} = \varinjlim H^{i}_{n}$.

**Theorem.**

<!-- label: IV.1.4 -->

Let $n \in \mathbb{Z}$. If there exists $i_{0} \in \mathbb{Z}$ such that $T^{i} = 0$ for every $i < i_{0}$, then the
following three conditions are equivalent:

1. $T^{i} = 0$ for every $i < n$.
1. $H^{i} = 0$ for every $i < n$.
1. There exists a module $M_{0}$ in `C_Y` such that $Supp M_{0} = Y$ and $T^{i}(M_{0}) = 0$ for every $i < n$.

*Proof.* — It is evident that (i) implies (ii) and (iii) (take $M_{0} = A/J$).

We show by induction on $n$ that (ii) implies (i). It is true for $n = i_{0}$; suppose it has been proved up to rank
$n$. Suppose then that $H^{i} = 0$ for every $i < n + 1$; by the induction hypothesis one has $T^{i} = 0$ for $i < n$,
but $T^{n-1} = 0$ implies that $T^{n}$ is a left exact functor, and

$$
T^{n} \xrightarrow{\sim} \operatorname{Hom}_{A}(-, H^{n}) = 0.
$$

We now show that (iii) implies (ii). It is again true for $n = i_{0}$; suppose it has been proved up to rank $n$. Let
$M_{0}$ be an $A$-module in `C_Y` such that $Supp M_{0} = Y$ and $T^{i}(M_{0}) = 0$ for every $i < n + 1$; by the
induction hypothesis one then has $H^{i} = 0$ for every $i < n$; it remains to show that $H^{n} = 0$. But "$H^{i} = 0$
for every $i < n$" implies that $T^{n-1} = 0$, and therefore that
$T^{n} \xrightarrow{\sim} \operatorname{Hom}_{A}(-, H^{n})$. One then has

<!-- original page 47 -->

```text
Ass H^n = Ass Hom(M₀, H^n) = Supp M₀ ∩ Ass H^n = Ass H^n,
```

since

```text
Ass H^n ⊂ Supp H^n ⊂ Y = Supp M₀.
```

Hence $T^{n}(M_{0}) = 0 \Leftrightarrow Ass H^{n} = \emptyset \Leftrightarrow H^{n} = 0$; this completes the proof.

## 2. Characterization of exact functors

<!-- label: IV.2 -->

The ring $A$ is still assumed noetherian and commutative. The notation is that of Proposition 1.3:

```text
Y = V(J),    T : C_Y° ⟶ Ab,    H = lim_→ T(A/J^n),
```

where we assume that $T$ is a left exact functor, whence

$$
T(M) \xrightarrow{\sim} \operatorname{Hom}_{A}(M, H).
$$

**Proposition.**

<!-- label: IV.2.1 -->

The following properties are equivalent:

1. The functor $T$ is exact.
1. $H$ is injective in $C'$.

*Proof.* — It clearly suffices to show that (i) implies (ii), that is, to prove that if the restriction to `C_Y` of the
functor $\operatorname{Hom}_{A}(-, H)$ is an exact functor, then $H$ is injective. But since $A$ is noetherian, in order
to show that $H$ is injective it suffices to prove that every homomorphism $f : N \to H$ whose source is an $A$-module
$N$ of finite type, a submodule of an $A$-module $M$ of finite type, extends to a homomorphism $\bar{f} : M \to H$.

The definition of $H$ and the fact that $N$ is of finite type imply that there exists an integer $n$ such that
$J^{n} \cdot f(N) = 0$. Endow $M$ and $N$ with the $J$-adic topology. The $J$-adic topology of $N$ is equivalent to the
topology induced by the $J$-adic topology of $M$ (Krull's theorem). There therefore exists $V = J^{k} \cdot M$ such that

```text
U = V ∩ N ⊂ J^n N.
```

One then has the factorization

```text
N ──────────► N/U
 \           /
  \         /
 f \       / u
    \     /
     ▼   ▼
       H
```

<!-- original page 48 -->

with $N/U$ and $M/V$ in `C_Y`. The hypothesis therefore allows one to extend $u$ to `ū`:

```text
N/U ──────────► M/V
   \           /
    \         /
   u \       / ū
      \     /
       ▼   ▼
         H
```

and $M \to M/V \to H$ gives the desired extension $\bar{f}$.

**Corollary.**

<!-- label: IV.2.2 -->

Let $K$ be an injective $A$-module. Then the submodule $H^{0}_{J}(K)$ of $K$ consisting of the elements annihilated by
some power of $J$ is injective.

*Proof.* — It suffices to verify that the restriction to `C_Y` of the functor $\operatorname{Hom}_{A}(-, H^{0}_{J}(K))$
is exact. Now let $M \in Ob C_{Y}$; there exists $k$ such that $J^{k} \cdot M = 0$, and the inclusion

```text
Hom_A(−, H⁰_J(K)) ⟶ Hom_A(M, K)
```

is then an isomorphism. The result follows, since $\operatorname{Hom}_{A}(-, K)$ is exact.

## 3. Study of the case where T is left exact and T(M) is of finite type for every M

<!-- label: IV.3 -->

Let, as above,

$$
T : C^{\circ}_{Y} \longrightarrow Ab;
$$

we now assume that $T$ is left exact and that one has the factorization

```text
                         T
        C_Y°  ─────────────────────────►  Ab
            \                          ↗
             \                       /
              \                    /
               ▼                 /
                    C_Y
```

where, as above, $C_{Y} \to Ab$ is the forgetful functor. One can therefore define $T(T(M)) = T \circ T(M)$, and the
canonical morphism

```text
M ⟶ Hom_A(Hom_A(M, H), H)
```

defines a morphism

$$
M \longrightarrow T \circ T(M).
$$

<!-- original page 49 -->

**Proposition.**

<!-- label: IV.3.1 -->

The ring $A$ being still assumed noetherian, if one makes the additional hypothesis that $A/J$ is artinian, the
following conditions are equivalent:

1. $T$ is left exact and, for every $M \in Ob C_{Y}$, $T(M)$ is of finite type and $M \to T \circ T(M)$ is an
   isomorphism.
1. $T$ is exact and, for every residue field $k$ associated to a maximal ideal containing $J$, one has
   $T(k) \xrightarrow{\sim} k$.
1. One has $T \xrightarrow{\sim} \operatorname{Hom}_{A}(-, H)$ with $H$ injective, and, for every $k$ as in (ii), one
   has $\operatorname{Hom}_{A}(k, H) \xrightarrow{\sim} k$.
1. $T$ is exact and, for every $M \in Ob C_{Y}$, one has $long T(M) = long M$.

*Proof.* — We have already shown the equivalence of (ii) and (iii) (Prop. 2.1).

Let us show that (ii) implies (iv): first, if $M \in Ob C_{Y}$, then since $M$ is an $A/J^{n}$-module with $A/J^{n}$
artinian, `long M` is finite. We argue by induction on the length of $M$. Condition (iv) holds when $long M = 1$,
because then $M$ is a residue field falling under (ii). If $long M > 1$, there exists a submodule $M'$ of $M$ with
$M' \neq 0$ and $long M' < long M$. Form the exact sequence

$$
0 \longrightarrow M' \longrightarrow M \longrightarrow M'' \longrightarrow 0.
$$

Since $T$ is exact, one has the sequence

$$
0 \longrightarrow T(M') \longrightarrow T(M) \longrightarrow T(M'') \longrightarrow 0,
$$

and `long T(M) = long T(M′) + long T(M′′) = long M′ + long M′′ = long M`.

(ii) ⇒ (i): Since (ii) implies (iv), let $M$ be an $A$-module in `C_Y`; one has $long T(M) = long M$, hence $T(M)$ is of
finite length and therefore of finite type.

It remains to show that $M \to T \circ T(M)$ is an isomorphism; we again argue by induction on `long M`. For $M = k$ it
is true. In the general case, write the commutative diagram with exact rows

<!-- original page 50 -->

$$
0 \longrightarrow  M'  \longrightarrow  M  \longrightarrow  M'' \longrightarrow 0
      \downarrow        \downarrow       \downarrow
0 \longrightarrow T\circ T(M') \longrightarrow T\circ T(M) \longrightarrow T\circ T(M'') \longrightarrow 0,
$$

where $M'$ is a submodule of $M$ with $M' \neq 0$ and $long M' < long M$. By the induction hypothesis the outer arrows
are isomorphisms, hence

$$
M \longrightarrow T \circ T(M)
$$

is an isomorphism.

(i) ⇒ (ii): Let

$$
0 \longrightarrow M' \longrightarrow M \longrightarrow M'' \longrightarrow 0
$$

be an exact sequence of $A$-modules in `C_Y`, and let $Q$ be the cokernel of $T(M) \to T(M')$. Applying $T$ to the exact
sequence

```text
0 ⟶ T(M′) ⟶ T(M) ⟶ T(M′′) ⟶ Q ⟶ 0,
```

one obtains

$$
0 \longrightarrow T(Q) \longrightarrow T\circ T(M') \longrightarrow T\circ T(M)
                \uparrow          \uparrow
                \cong          \cong
                M'    \longrightarrow    M
$$

hence $T(Q) = 0$ and $Q \xrightarrow{\sim} T(T(Q)) = 0$.

<!-- original page 51 -->

On the other hand, let $k$ be a residue field, $k = A/\mathfrak{m}$, $J \subset \mathfrak{m}$. One must show that
$T(k) \xrightarrow{\sim} k$. For this it suffices to note that $T(k)$ is a $k$-vector space. One then deduces

```text
T(k) ≃ k ⊕ V,
T(T(k)) ≃ T(k) ⊕ T(V) ≃ k ⊕ V ⊕ T(V) ≃ k,
```

whence $V = 0$.

Finally, let us show that (iv) implies (iii): it suffices to show that $T(k) \xrightarrow{\sim} k$. Now
$long T(k) = long k = 1$, so $T(k) = k'$ is a residue field, and `Supp k′ = Supp Hom_A(k, H) ⊂ Supp k`. Hence
$k \simeq k'$.

**Remark.**

<!-- label: IV.3.2 -->

One can show that condition (iv) is equivalent to the condition

(iv)′ For every $M \in Ob C_{Y}$, one has $long T(M) = long M$.

## 4. Dualizing module; dualizing functor

<!-- label: IV.4 -->

**Definition.**

<!-- label: IV.4.1 -->

Let $A$ be a noetherian local ring with maximal ideal $\mathfrak{m}$. A *dualizing functor* for $A$ is any functor

$$
T : C^{\circ}_{\mathfrak{m}} \longrightarrow Ab,
$$

where we write $C_{\mathfrak{m}}$ in place of `C_Y` for $Y = V(\mathfrak{m})$, which satisfies the equivalent conditions
of Proposition 3.1. An $A$-module $I$ is said to be *dualizing* for $A$ if the functor
$M \mapsto \operatorname{Hom}_{A}(M, I)$ is dualizing.

Definition 4.1 can be generalized to the case where $A$ is no longer assumed to be a local ring.

**Definition.**

<!-- label: IV.4.2 -->

Let $A$ be a noetherian ring, and let $\bar{C}$ be the full subcategory of $C$ consisting of the $A$-modules of finite
length. A *dualizing functor* is any $A$-linear functor $T$ from $\bar{C}^{\circ}$ to $\bar{C}$ which is exact and such
that the morphism of functors

$$
id \longrightarrow T \circ T
$$

is an isomorphism.

We will prove an existence theorem and also that the module $I$ representing such a functor is locally artinian. We will
likewise show that, for every maximal ideal $\mathfrak{m}$ of $A$, the $\mathfrak{m}$-primary component of the socle of
$I$ is of length 1.

**Proposition.**

<!-- label: IV.4.3 -->

Let $A$ and $B$ be two noetherian local rings with maximal ideals $\mathfrak{m}_{A}$ and $\mathfrak{m}_{B}$, such that
$B$ is a finite $A$-algebra. Then, if $I$ is a dualizing module for $A$, $\operatorname{Hom}_{A}(B, I)$ is a dualizing
module for $B$.

<!-- original page 52 -->

*Proof.* — Let

$$
R : C_{\mathfrak{m}_{B}} \longrightarrow C_{\mathfrak{m}_{A}}
$$

be the restriction-of-scalars functor; it is exact. Let $T$ be a dualizing functor for $A$,

$$
T : C_{\mathfrak{m}_{A}} \longrightarrow Ab;
$$

it is exact and, for every $M \in Ob C_{\mathfrak{m}_{A}}$, the natural morphism $M \to T \circ T(M)$ is an isomorphism;
hence $T \circ R$ is a dualizing functor for $B$. If $I$ represents $T$, then by the classical formula
`Hom_A(M, I) = Hom_B(M, Hom_A(B, I))`, valid for every $B$-module $M$, we deduce that $\operatorname{Hom}_{A}(B, I)$ is
a dualizing module for $B$.

**Corollary.**

<!-- label: IV.4.4 -->

Let $A$ be a noetherian local ring and $\mathfrak{a}$ an ideal of $A$; set $B = A/\mathfrak{a}$. If $I$ is a dualizing
module for $A$, then the annihilator of $\mathfrak{a}$ in $I$ is a dualizing module for $B$.

**Lemma.**

<!-- label: IV.4.5 -->

Let $A$ be a noetherian local ring and $I$ a locally artinian $A$-module. There is a canonical isomorphism

```text
I ⥲ Î = I ⊗_A Â.
```

*Proof.* — Let $I_{n}$ denote the annihilator of $\mathfrak{m}^{n}$ in $I$, where $\mathfrak{m}$ is the maximal ideal of
$A$. To say that $I$ is locally artinian is to say that $I$ is the direct limit of the $I_{n}$ and that these are of
finite length. Now the tensor product commutes with direct limits, so one is reduced to the case where $I$ is artinian.
In this case $I$ is annihilated by some power of the maximal ideal, say $\mathfrak{m}^{k}$; therefore for
$p \geqslant k$ one has $I \xrightarrow{\sim} I \otimes_{A} A/\mathfrak{m}^{p}$, and hence
$I \xrightarrow{\sim} I \otimes_{A} \hat{A}$, since $A$ is noetherian and $I$ is of finite type.

It follows that the restriction-of-scalars functor from `Â` to $A$ and the extension-of-scalars functor induce
quasi-inverse equivalences between the category of locally artinian `Â`-modules and the category of locally artinian
$A$-modules.

<!-- original page 53 -->

**Proposition.**

<!-- label: IV.4.6 -->

Let $A$ be a noetherian local ring, `Â` its completion, and $I$ a dualizing module for $A$ (resp. for `Â`). Let $J$ be
the completion[^N.D.E-IV-2] of $I$ (resp. the $A$-module obtained by restriction of scalars). Then $J$ is a dualizing
module for `Â` (resp. for $A$). Moreover, the underlying abelian groups of $I$ and $J$ are isomorphic.

*Proof.* — One simply observes that the equivalence between the category of locally artinian $A$-modules and the
category of locally artinian `Â`-modules induces an isomorphism between the bifunctors $\operatorname{Hom}_{A}(-, -)$
and $\operatorname{Hom}_{\hat{A}}(-, -)$, and that the characterization of a dualizing functor or a dualizing module
involves only these bifunctors.

**Theorem.**

<!-- label: IV.4.7 -->

Let $A$ be a noetherian local ring.

a) There always exists a dualizing module $I$.

b) Two dualizing modules are isomorphic (by a non-canonical isomorphism).

c) For a module $I$ to be dualizing, it is necessary and sufficient that it be an injective envelope of the residue
field $k$ of $A$.

**Remark.**

<!-- label: IV.4.8 -->

Proposition 4.6 reduces the proof to the case of a complete noetherian local ring. By a structure theorem of
Cohen,[^N.D.E-IV-3] such a ring is a quotient of a regular ring. Proposition 4.3 then allows one to assume $A$ regular.
As we shall see later, this remark permits an explicit computation of the dualizing module;[^IV-4-1] nevertheless we
will prove Theorem 4.7 by other means.

*Recollections.* — Before proving the theorem, we make a few recollections on the notion of injective envelope. Cf.
Gabriel, *Thèse*, Paris 1961, *Des Catégories Abéliennes*, ch. II § 5.

<!-- original page 54 -->

Let $\mathcal{C}$ be an abelian category in which direct limits exist and are exact[^N.D.E-IV-4] (e.g. $\mathcal{C} =$
the category of modules). Every object $M$ embeds in an injective object, and one calls *injective envelope* of $M$ any
minimal injective object containing $M$. One has the following properties:

(i) Every object $M$ has an injective envelope $I$.

(ii) If $I$ and $J$ are two injective envelopes of $M$, there exists between $I$ and $J$ an isomorphism (in general not
unique) inducing the identity on $M$.

(iii) $I$ is an essential extension of $M$, that is to say $P \subset I$ and $P \cap M = {0}$ imply $P = {0}$. Moreover,
if $I$ is injective and an essential extension of $M$, then $I$ is an injective envelope of $M$.

Granting these results, to prove Theorem 4.7 it suffices to prove c).

*Proof.* — Let $I$ be a dualizing module for $A$. Then $I$ is injective and $\operatorname{Hom}_{A}(k, I)$ is isomorphic
to $k$. Composing the isomorphism $k \simeq \operatorname{Hom}_{A}(k, I)$ with the inclusion

```text
Hom_A(k, I) ↪ Hom_A(A, I) ≃ I,
```

one obtains the inclusion

$$
k \hookrightarrow I.
$$

Let us show that $I$ is an injective envelope of $k$. Let $J$ be an injective module such that

$$
k \subset J \subset I.
$$

Since $J$ is injective, there exists an injective $A$-submodule $J'$ of $I$ such that $I = J \oplus J'$. We show that
$\operatorname{Hom}_{A}(k, J') = 0$. One has

```text
Hom_A(k, I) ≃ Hom_A(k, J) ⊕ Hom_A(k, J′);
```

<!-- original page 55 -->

$\operatorname{Hom}_{A}(k, J)$ is a vector subspace of $\operatorname{Hom}_{A}(k, I) \simeq k$ not reduced to zero
(since it contains the inclusion $k \subset J$), so $\operatorname{Hom}_{A}(k, J) \simeq k$, and consequently
$\operatorname{Hom}_{A}(k, J') = 0$.

Arguing by induction on the length, one deduces that $\operatorname{Hom}_{A}(M, J') = 0$ for every $A$-module $M$ of
finite length; since $I$ is the direct limit of the modules $\operatorname{Hom}(A/\mathfrak{m}^{n}, I)$ (cf. Proposition
1.3), which are of finite length by hypothesis, the projection $I \to J'$ is zero, and consequently $J' = 0$.

Conversely, let $I$ be an injective envelope of $k$. To see that $I$ is a dualizing module, it suffices, by 2.1 and 3.1
(ii), to show that $V = \operatorname{Hom}_{A}(k, I)$ is isomorphic to $k$. Now one has the double inclusion

$$
k \subset V \subset I;
$$

$V$ is a vector space over $k$ that decomposes as the direct sum of $k$ and a vector subspace $V'$ of $I$ such that
$V' \cap k = 0$. Now $I$ is an essential extension of $k$, hence $V' = 0$ and $V = k$.

**Corollary.**

<!-- label: IV.4.9 -->

Let $A$ be a noetherian local ring; every dualizing module for $A$ is locally artinian.

*Proof.* — Let $I$ be a dualizing module; it is an injective envelope of $k$. Using the notation and the result of
Corollary 2.2, one has

$$
k \subset H^{0}_{\mathfrak{m}}(I) \subset I,
$$

and $H^{0}_{\mathfrak{m}}(I)$ is injective. One deduces that $I = H^{0}_{\mathfrak{m}}(I)$, and hence that $I$ is
locally artinian.[^N.D.E-IV-5]

## 5. Consequences of the theory of dualizing modules

<!-- label: IV.5 -->

<!-- original page 56 -->

The functor

```text
T = Hom_A(−, I) : C_𝔪 ⟶ C_𝔪
```

is an anti-equivalence. Indeed, $T \circ T$ is isomorphic to the identity functor, and the argument is formal from
there.

One deduces the usual properties of the notion of orthogonality:

Let $M* = \operatorname{Hom}_{A}(M, I) = T(M)$, and let $N \subset M$ be a submodule. Define the *orthogonal* of $N$ to
be the submodule $N'$ of $M*$ consisting of the elements of $M*$ that vanish on $N$. One thereby obtains a bijection
between the set of submodules of $M$ and the set of submodules of $M*$, which reverses the order.

In particular:

- $long_{M} N = colong_{M*} N'$.
- The monogenic modules, i.e. those such that $M/\mathfrak{m}M$ is of dimension 0 or 1, correspond under duality to the
  modules whose socle is of length 0 or 1.
- If $A$ is artinian, the ideals of $A$ correspond to the submodules of $I$.

and so on.

Let $A$ be a noetherian local ring, let $\mathcal{D}_{A}$ be the category of $A$-modules $M$ such that, for every
$n \in \mathbb{N}$, $M_{n} = M/\mathfrak{m}^{n+1}M$ is of finite length and such that $M = \varprojlim M_{n}$, and let
`Â` be the completion of $A$. The restriction-of-scalars functor and the completion functor are quasi-inverse
equivalences between $\mathcal{D}_{A}$ and $\mathcal{D}_{\hat{A}}$, which commute up to isomorphism with the formation
of the underlying abelian groups of the modules considered. Let $\mathcal{C}_{A}$ denote the category of locally
artinian $A$-modules with socle of finite dimension.

**Proposition.**

<!-- label: IV.5.1 -->

Let $A$ be a noetherian local ring and let $I$ be a dualizing module for $A$. The functors

```text
Hom_A(−, I) : (𝒞_A)° ⟶ 𝒟_A
```

and

```text
Hom_{Â}(−, I) : 𝒟_A ⟶ (𝒞_A)°
```

are equivalences of categories, quasi-inverse to one another.

Moreover, if one transports these functors via the equivalences of categories between $\mathcal{D}_{A}$ and
$\mathcal{D}_{\hat{A}}$ on the one hand, and $\mathcal{C}_{A}$ and $\mathcal{C}_{\hat{A}}$ on the other, one finds the
functor $\operatorname{Hom}_{\hat{A}}(-, I)$.

<!-- original page 57 -->

*Proof.* — Let $X \in Ob \mathcal{C}_{A}$. By definition,

```text
X = lim_→ X_k,    X_k = Hom_A(A/𝔪^{k+1}, X),
                  k ∈ ℕ
```

so

```text
Hom_A(X, I) = lim_← Hom_A(X_k, I).
```

Therefore $Y = \varprojlim X_{k}$ is an `Â`-module of finite type, as follows from EGA 0_I 7.2.9. We note in this
connection that $\mathcal{D}_{A}$ is also the category of `Â`-modules of finite type, or, if one prefers, that
$\mathcal{D}_{A}$ is the category of complete $A$-modules of finite type over `Â`. Let then $Y$ be such a module, and
let $f : Y \to I$ be an `Â`-homomorphism. The image of $f$ is a submodule of finite type, hence is annihilated by
$\mathfrak{m}^{k}$ for some $k$; indeed every $x \in I$ is annihilated by a power of $\mathfrak{m}$. So $f$ factors
through $Y/\mathfrak{m}^{k} Y$, whence it follows that

```text
Hom_{Â}(Y, I) = lim_→ Hom_{Â}(Y_(k), I)    with Y_(k) = Y/𝔪^{k+1}Y
                  k

              = lim_→ (Y_(k))*
                  k
```

belongs to $Ob \mathcal{C}_{A}$. It then follows immediately that the two functors of the statement are quasi-inverse to
one another.

<!-- original page 58 -->

It follows from the foregoing that neither the categories nor the functors under consideration, nor the underlying
abelian groups of the modules considered, are changed by replacing $A$ by `Â`; Proposition 5.1 then states as follows:

The restriction of the functor $\operatorname{Hom}_{\hat{A}}(-, I)$ to the category of `Â`-modules of finite type takes
its values in the category of locally artinian `Â`-modules with socle of finite dimension, and admits a quasi-inverse
functor, which is the restriction of the functor $\operatorname{Hom}_{\hat{A}}(-, I)$. On the intersection of these two
categories these two functors coincide (obviously!) and establish an auto-duality of the category of `Â`-modules of
finite length.

**Example** (Macaulay).

<!-- label: IV.5.2 -->

Let $A$ be a local ring with residue field $k$. Let $k_{0}$ be a subfield of $A$ such that $k$ is finite over $k_{0}$,
with $[k : k_{0}] = d$. Every $A$-module of finite length can be viewed as a $k_{0}$-vector space of finite dimension
equal to $d \cdot long(M)$. The functor $T$:

$$
M \longrightarrow \operatorname{Hom}_{k_{0}}(M, k_{0})
$$

is then exact and preserves length, hence is dualizing for $A$. The associated dualizing module is therefore

```text
A′ = lim_→ Hom_{k₀}(A/𝔪^n, k₀),
       n
```

the topological dual of $A$ endowed with the $\mathfrak{m}$-adic topology.

**Example.**

<!-- label: IV.5.3 -->

Let $A$ be a regular noetherian local ring of dimension $n$. Let $\mathfrak{m}$ be its maximal ideal and $k$ its residue
field. There exists a regular system of parameters $(x_{1}, x_{2}, \cdots, x_{n})$ that generates $\mathfrak{m}$ and
that is an $A$-regular sequence. One can therefore compute the $Ext^{i}_{A}(k, A)$ by the Koszul complex; one finds

```text
Ext^i_A(k, A) = 0    if i ≠ n,
Ext^n_A(k, A) ≃ k.
```

<!-- original page 59 -->

The depth of $A$ being $n$, for every $M$ annihilated by a power of $\mathfrak{m}$, $Ext^{i}_{A}(M, A) = 0$ if $i < n$;
furthermore $Ext^{i}_{A}(M, A) = 0$ if $i > n$, since the global cohomological dimension of $A$ is equal to $n$. Hence
$Ext^{n}_{A}(-, A)$ is exact, and moreover $Ext^{n}_{A}(k, A) \simeq k$; it follows that:

**Proposition.**

<!-- label: IV.5.4 -->

If $A$ is a regular noetherian local ring of dimension $n$, the functor

$$
M \longrightarrow Ext^{n}_{A}(M, A)
$$

is dualizing. The associated dualizing module is

```text
I = lim_→ Ext^n_A(A/𝔪^r, A);
      r
```

it is isomorphic to $H^{n}_{\mathfrak{m}}(A)$ (Exposé II, Th. 6).[^IV-5-1]

**Remark.**

<!-- label: IV.5.5 -->

If $A$ satisfies the hypotheses of both preceding examples, the two dualizing modules so obtained are isomorphic.
Suppose for example that $A$ is regular of dimension $n$, complete, and of equal characteristic. There then exists a
field of representatives, say $K$. If one chooses a system of parameters $(x_{1}, \cdots, x_{n})$ of $A$, one can
construct an isomorphism between $A$ and the ring of formal power series $K[[T_{1}, \cdots, T_{n}]]$; whence, as we
shall now see, an explicit isomorphism between the two dualizing modules

$$
v : H^{n}_{\mathfrak{m}}(A) \longrightarrow A'.
$$

One can find an intrinsic interpretation of this isomorphism using the module $\Omega^{n} = \Omega^{n}(A/K)$ of
completed relative differentials of maximal degree. Indeed, it is known that $\Omega^{n}$ admits a basis consisting of
the element $dx_{1} \wedge dx_{2} \cdots \wedge dx_{n}$. Whence an isomorphism

$$
u : H^{n}_{\mathfrak{m}}(\Omega^{n}) \longrightarrow H^{n}_{\mathfrak{m}}(A).
$$

A remarkable fact is then that the composite

```text
vu = w : H^n_𝔪(Ω^n) ⟶ A′
```

does not depend on the choice of system of parameters and commutes with change of base field.

<!-- original page 60 -->

To construct $v$, one computes $H^{n}_{\mathfrak{m}}(A)$ using the Koszul complex associated to the $x_{i}$; one finds

```text
H^n_𝔪(A) = lim_→ A/(x₁^r, …, x_n^r);
            r
```

where the transition morphisms are defined as follows: set $I_{r} = A/(x^{r}_{1}, \cdots, x^{r}_{n})$; let
$e^{r}_{a_{1},\cdots,a_{n}}$ denote the image of $x^{a_{1}}_{1} x^{a_{2}}_{2} \cdots x^{a_{n}}_{n}$ in $I_{r}$. The
$e^{r}_{a_{1},\cdots,a_{n}}$, for $0 \leqslant a_{i} < r$, form a basis of $I_{r}$.

That said, if $s$ is an integer, the transition morphism

```text
t_{r, r+s} : I_r ⟶ I_{r+s}
```

is multiplication by $x^{s}_{1} x^{s}_{2} \cdots x^{s}_{n}$, so

```text
u_{r, r+s}(e^r_{a₁,…,a_n}) = e^{r+s}_{a₁+s, …, a_n+s}.
```

Note that giving an $A$-homomorphism $w$ from an $A$-module $M$ to $A'$ is equivalent to giving a $K$-linear form
$w' : M \to K$ that is continuous on submodules of finite type. In the case $M = H^{n}_{\mathfrak{m}}(\Omega^{n})$, the
definition of $w$ is therefore equivalent to that of a linear form

$$
\rho : H^{n}_{\mathfrak{m}}(\Omega^{n}) \longrightarrow K,
$$

called the *residue form*.[^IV-5-2] To construct $\rho$, it suffices to define forms $\rho_{r} : I_{r} \to K$ that fit
together, and one will take

```text
ρ_r(e^r_{a₁,…,a_n}) =
    1   if a_i = r − 1 for 1 ⩽ i ⩽ n,
    0   otherwise.
```

## Translation ledger (Exposé IV-specific)

| French                                                         | English                                    | Note                                                                                           |
| -------------------------------------------------------------- | ------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| $T : C^{\circ} \to Ab$ (foncteurs additifs)                    | $T : C^{\circ} \to Ab$ (additive functors) | Contravariant; $C^{\circ}$ is the opposite category. Convention pinned at first use.           |
| homothétie $f_{M}$                                             | homothety $f_{M}$                          | Standard. Multiplication-by-$f$ map on $M$.                                                    |
| limite projective / inductive                                  | inverse limit / direct limit               | Modern English (per glossary). The source's $\varprojlim$/$\varinjlim$ notation is preserved.  |
| foncteur exact à gauche                                        | left exact functor                         | Per glossary.                                                                                  |
| de présentation finie                                          | of finite presentation                     | Standard.                                                                                      |
| ∂-foncteur exact                                               | exact $\partial$-functor                   | Original Grothendieck notation preserved; modern usage would say *exact sequence of functors*. |
| corps résiduel                                                 | residue field                              | Per glossary.                                                                                  |
| socle                                                          | socle                                      | Standard module-theoretic term; kept as in source.                                             |
| longueur (`long M`)                                            | length (`long M`)                          | Original abbreviation `long` preserved inside math.                                            |
| module dualisant / foncteur dualisant                          | dualizing module / dualizing functor       | Per glossary.                                                                                  |
| enveloppe injective                                            | injective envelope                         | Per glossary.                                                                                  |
| extension essentielle                                          | essential extension                        | Per glossary.                                                                                  |
| restriction (resp. extension) des scalaires                    | restriction (resp. extension) of scalars   | Standard.                                                                                      |
| forme résidu                                                   | residue form                               | Per glossary (§5.5).                                                                           |
| $\operatorname{Hom}_{A}(B, I)$ (with $B$ a finite $A$-algebra) | $\operatorname{Hom}_{A}(B, I)$             | Notation preserved; the $B$-module structure is via the second argument.                       |
| module localement artinien                                     | locally artinian module                    | Standard. Direct limit of finite-length submodules.                                            |
| EGA 0_I 7.2.9                                                  | EGA 0_I 7.2.9                              | Cross-reference preserved.                                                                     |
| $\Omega^{n}(A/K)$                                              | $\Omega^{n}(A/K)$                          | Completed relative differentials of maximal degree.                                            |
| C̄ (sous-catégorie des modules de longueur finie)               | $\bar{C}$                                  | Source uses an overline on $C$; rendered with the combining macron $\bar{C}$.                  |

[^N.D.E-IV-1]: *N.D.E.* The definition of $H$ is implicit in the original text.

[^N.D.E-IV-2]: *N.D.E.* Here one must understand by "the completion of $I$" the tensor product
    $\hat{I} = I \otimes_{A} \hat{A}$ (cf. Lemma 4.5), namely $I$ endowed with its canonical `Â`-module structure, and
    not the $\mathfrak{m}$-adic completion. For example, if $p$ is a prime number and $A = \hat{A} = \mathbb{Z}_{p}$ is
    the ring of $p$-adic integers, then the injective envelope of the residue field $k = \mathbb{Z}/p\mathbb{Z}$ is the
    discrete $\mathbb{Z}_{p}$-module $\mathbb{Q}_{p}/\mathbb{Z}_{p}$, whose completion for the $p$-adic topology is
    zero.

[^N.D.E-IV-3]: *N.D.E.* See Cohen I.S., "On the structure and ideal theory of complete local rings", *Trans. Amer. Math.
    Soc.* **59** (1946), pp. 54–106.

[^IV-4-1]: This was the method followed by Grothendieck (in 1957). The method by injective envelopes that now follows is
    due, it seems, to K. Morita, "Duality for modules and its applications to the theory of rings with minimum
    conditions", *Sc. Rep. Tokyo Kyoiku Daigaku* **6** (1958/59), pp. 83–142. Morita's work is, moreover, independent of
    Grothendieck's and considerably earlier than the present seminar, and is not limited to the case of commutative base
    rings.

[^N.D.E-IV-4]: *N.D.E.* Of course, what is assumed exact is the small filtered direct limits; one should also assume the
    existence of a generator. Cf. *Tôhoku*. As for the category of modules, which suffices for our purposes, one may
    also refer to Chapter 10 of Bourbaki's *Algèbre*.

[^N.D.E-IV-5]: *N.D.E.* As already observed, one may also simply remark that $I$ is the direct limit of the modules
    $\operatorname{Hom}_{A}(A/\mathfrak{m}^{n}, I)$.

[^IV-5-1]: Let $A$ be a ring, $J$ an ideal of $A$, $M$ an $A$-module, $i \in \mathbb{Z}$; one then sets
    $H^{i}_{J}(M) = H^{i}_{Y}(X, \tilde{F})$, where $X = \operatorname{Spec}(A)$, $Y = V(J)$ and
    $\tilde{F} = \tilde{M}$.

[^IV-5-2]: For a more detailed study of the notion of residue, cf. R. Hartshorne, *Residues and Duality*, Lect. Notes in
    Math., vol. 20, Springer, 1966.


<!-- SOURCE: 05-dualite-locale-et-structure-des-Hi.md -->

# Exposé V. Local duality and the structure of the H^i(M)

<!-- label: V -->

<!-- original page 47 -->

## 1. Complexes of homomorphisms

<!-- label: V.1 -->

**1.1.** Let $F\bullet$ and $G\bullet$ be two graded modules; then one writes

$$
\operatorname{Hom}\bullet(F\bullet, G\bullet)
$$

<!-- label: eq:V.1.1 -->

for the graded module of homomorphisms of graded modules from $F\bullet$ into $G\bullet$. Thus one has

```text
Homˢ(F•, G•) = ∏ₖ Hom(Fₖ, Gₖ₊ₛ).
```

<!-- label: eq:V.1.2 -->

Let $F\bullet$ (resp. $G\bullet$) be a complex, and let $d_{1}$ (resp. $d_{2}$) be its differential; then for
$h \in \operatorname{Hom}^{s}(F\bullet, G\bullet)$ one sets[^V-1-1]

```text
d(h) = h ∘ d₁ + (−1)^{s+1} d₂ ∘ h.
```

<!-- label: eq:V.1.3 -->

One verifies trivially that $d \circ d = 0$, hence that $\operatorname{Hom}\bullet(F\bullet, G\bullet)$ equipped with
$d$ is a complex. The cohomology group of this complex is written

$$
H\bullet(F\bullet, G\bullet).
$$

<!-- label: eq:V.1.4 -->

If $G\bullet$ is injective in each degree, then

$$
F\bullet \mapsto H\bullet(F\bullet, G\bullet)
$$

is an exact ∂-functor. Likewise, for arbitrary $F\bullet$,

$$
G\bullet \mapsto H\bullet(F\bullet, G\bullet)
$$

is an exact δ-functor on the category of complexes $G\bullet$ that are injective in each degree.

<!-- original page 48 -->

**Remark 1.2.**

<!-- label: V.1.2 -->

The cycles of $\operatorname{Hom}\bullet(F\bullet, G\bullet)$ are the homomorphisms from $F\bullet$ into $G\bullet$ that
commute or anticommute with the differentials, according to degree. The boundaries of
$\operatorname{Hom}\bullet(F\bullet, G\bullet)$ are the homomorphisms from $F\bullet$ into $G\bullet$ that are homotopic
to zero.

Let $A$ be a ring, let $M$ (resp. $N$) be an $A$-module, and let $R(M)$ (resp. $R(N)$) be an injective resolution of $M$
(resp. $N$). Then there exists a canonical isomorphism[^V-1-2]

```text
Hˢ(R(M), R(N)) ≅ Extˢ(M, N).
```

<!-- label: eq:V.1.3-iso -->

Indeed, let $i: M \to R(M)$ be the canonical augmentation, and let $h \in \operatorname{Hom}^{s}(R(M), R(N))$; one
writes $t_{s}$ for the map

$$
h \mapsto h^{0} \circ i
$$

from $\operatorname{Hom}^{s}(R(M), R(N))$ into $\operatorname{Hom}(M, R(N)^{s})$. The family $(t_{s})_{s\geqslant 0}$
defines a homomorphism of (ordinary) complexes[^V-1-3]

```text
t: Hom•(R(M), R(N)) → Hom•(M, R(N)),
```

i.e. one has $(dh)^{0} \circ i = d_{2} \circ h^{0} \circ i$.

One verifies easily that, upon passing to cohomology, $t$ gives an isomorphism. In particular, it follows that

$$
H\bullet(R(M), R(N))
$$

does not "depend" on the chosen injective resolution $R(M)$ (resp. $R(N)$) of $M$ (resp. $N$).

To every exact sequence of $A$-modules

$$
0 \to M' \to M \to M'' \to 0
$$

<!-- label: eq:V.1.5 -->

one associates an exact sequence of injective resolutions

$$
0 \to R(M') \to R(M) \to R(M'') \to 0.
$$

<!-- label: eq:V.1.6 -->

One verifies that the isomorphism (1.3) commutes with the homomorphisms

```text
Hˢ(R(M′), R(N)) → Hˢ⁺¹(R(M″), R(N)),
```

<!-- label: eq:V.1.8 -->

```text
Extˢ(R(M′), R(N)) → Extˢ⁺¹(R(M″), R(N)),
```

<!-- label: eq:V.1.9 -->

deduced from (6) and (5).

<!-- original page 49 -->

Let $P$ be a third $A$-module, and let $R(P)$ be an injective resolution of $P$; then composition of graded morphisms
gives a pairing

```text
Homⁱ(R(N), R(M)) × Homʲ(R(M), R(P)) → Homⁱ⁺ʲ(R(N), R(P)),
```

<!-- label: eq:V.1.10 -->

which defines a pairing

```text
Hⁱ(R(N), R(M)) × Hʲ(R(M), R(P)) → Hⁱ⁺ʲ(R(N), R(P)),
```

<!-- label: eq:V.1.11 -->

hence a homomorphism of functors in $M$:

```text
Hⁱ(R(N), R(M)) → Hom(Hʲ(R(M), R(P)), Hⁱ⁺ʲ(R(N), R(P))).
```

<!-- label: eq:V.1.4-hom -->

We shall see that (1.4) is a homomorphism of δ-functors in $M$. The exact sequences (5) and (6) give a commutative
diagram:

```text
Homⁱ(R(N), R(M′))   ──→   Hom(Homʲ(R(M′), R(P)), Homⁱ⁺ʲ(R(N), R(P)))
       │                                       ↑
       │                                  Hom(q, id)
       ↓                                       │
Homⁱ(R(N), R(M))    ──→   Hom(Homʲ(R(M), R(P)), Homⁱ⁺ʲ(R(N), R(P)))
       │
       │ p
       ↓                                       │
Homⁱ(R(N), R(M″))   ──→   Hom(Homʲ(R(M″), R(P)), Homⁱ⁺ʲ(R(N), R(P))).
```

Let $h \in \operatorname{Hom}^{i}(R(N), R(M''))$ (resp. $g \in \operatorname{Hom}^{j}(R(M'), R(P))$) be a cycle, and let
$h' \in \operatorname{Hom}^{i}(R(N), R(M))$ (resp. $g' \in \operatorname{Hom}^{j}(R(M), R(P))$) be such that $p(h') = h$
(resp. $q(g') = g$); then to say that (1.4) is a homomorphism of δ-functors in $M$ is to say that

```text
g ∘ dh′ − dg′ ∘ h
```

<!-- label: eq:V.1.12 -->

is a coboundary in $\operatorname{Hom}\bullet(R(N), R(P))$.

Now one has

```text
dh′ = h′ ∘ d₁ + (−1)^{i+1} d₂ ∘ h′,
dg′ = g′ ∘ d₂ + (−1)^{j+1} d₃ ∘ g′,
```

with the obvious notations. Hence (12) is written

```text
g ∘ h′ ∘ d₁ + (−1)^{i+1} g ∘ d₂ ∘ h′ − g′ ∘ d₂ ∘ h − (−1)^{j+1} d₃ ∘ g′ ∘ h.
```

<!-- original page 50 -->

On the other hand, since $h$ and $g$ are cycles, one has

```text
g ∘ d₂ = (−1)ʲ d₃ ∘ g,
d₂ ∘ h = (−1)ⁱ h ∘ d₁,
```

hence, finally, (12) is written

```text
d(g ∘ h′ + (−1)^{i+1} g′ ∘ h),
```

which completes the proof.

Thus (1.3) and (1.4) give a homomorphism of δ-functors in $M$:

```text
Extⁱ(N, M) → Hom(Extʲ(M, P), Extⁱ⁺ʲ(N, P)).
```

<!-- label: eq:V.1.5-final -->

## 2. The local duality theorem for a regular local ring

<!-- label: V.2 -->

Let $A$ be a regular local ring of dimension $r$, let $\mathfrak{m}$ be the maximal ideal of $A$, and let $M$ be a
finitely generated $A$-module. One sets $H^{i}(M) = H^{i}_{\mathfrak{m}}(M)$ (hence
$H^{i}(M) = \lim\to Ext^{i}(A/\mathfrak{m}^{k}, M)$). One has seen (IV 5.4) that $I = H^{r}(A)$ is a dualizing module
for $A$; denote by $D$ the associated dualizing functor. In (1.5) setting $N = A/\mathfrak{m}^{k}$, $P = A$, one obtains
a homomorphism of δ-functors in $M$

```text
φₖ: Extⁱ(A/𝔪ᵏ, M) → Hom(Extʳ⁻ⁱ(M, A), Extʳ(A/𝔪ᵏ, A)).
```

<!-- label: eq:V.2.13 -->

Passing to the direct limit over $k$, one finds a homomorphism of δ-functors

```text
φ: Hⁱ(M) → D(Extʳ⁻ⁱ(M, A)).
```

<!-- label: eq:V.2.14 -->

**Theorem 2.1** (Local duality theorem)**.**

<!-- label: V.2.1 -->

The functorial homomorphism $\phi$ above is an isomorphism.

*Proof.* If $i > r$, the right-hand side of (14) is trivially zero, and the left-hand side is zero because
$H^{i}(M) = \lim\to_{k} Ext^{i}(A/\mathfrak{m}^{k}, M)$, and this holds for each $Ext^{i}(A/\mathfrak{m}^{k}, M)$
(syzygy theorem).

If $i = r$, by what precedes, the two functors in $M$, $H^{r}(M)$ and $D(\operatorname{Hom}(M, A))$, are right exact;
since $A$ is noetherian and $M$ is finitely generated, it suffices to verify the isomorphism for $M = A$, which is
immediate.

<!-- original page 51 -->

To show that $\phi$ is a functorial isomorphism, it now suffices, proceeding by descending induction on $i$, to remark
that every finitely generated module admits a finite presentation, and that for $i < r$ the two sides of (14) are zero
when $M$ is finitely generated free. This is evident for the right-hand side, and since $H^{i}$ commutes with finite
sums it suffices, as for the left-hand side, to show that $H^{i}(A) = 0$ for $i < r$. But this follows, since
$prof(A) = r$, from (III 3.4).

## 3. Application to the structure of the H^i(M)

<!-- label: V.3 -->

**Theorem 3.1.**

<!-- label: V.3.1 -->

Let $A$ be a noetherian local ring, $D$ a dualizing functor for $A$, and $M$ a finitely generated $A$-module with
$M \neq 0$, of dimension $n$. Then one has:

(i) $H^{i}(M) = 0$ if $i < 0$ or if $i > n$.

(ii) `D(Hⁱ(M))^` is a finitely generated module over `Â`, of dimension $\leqslant i$.

(iii) $H^{n}(M) \neq 0$, and if $A$ is complete, $D(H^{n}(M))$ is of dimension $n$ and

```text
Ass(D(Hⁿ(M))) = {𝔭 ∈ Ass(M) | dim A/𝔭 = n}.
```

*Proof.* Let $I$ be the dualizing module associated to $D$. One knows that `Î` is a dualizing module for `Â`. On the
other hand, one has

```text
Hⁱ(M)^ = Hⁱ(M̂),
D(Hⁱ(M))^ = Hom(Hⁱ(M̂), Î), and
dim M̂ = dim M;
```

hence one may suppose $A$ complete. Now, by a theorem of Cohen, every complete local ring is a quotient of a regular
local ring. To reduce to that case, one needs the following lemma:

<!-- original page 52 -->

**Lemma 3.2.**

<!-- label: V.3.2 -->

Let $X$ (resp. $Y$) be a ringed space, let $X'$ (resp. $Y'$) be a closed subspace of $X$ (resp. $Y$), and let
$f: X \to Y$ be a morphism of ringed spaces such that $f^{-1}(Y') = X'$. Let $F$ be an $\mathcal{O}_{X}$-Module, and
denote by $A$ (resp. $B$) the ring $\Gamma(\mathcal{O}_{X})$ (resp. $\Gamma(\mathcal{O}_{Y})$), and by $f: B \to A$ the
ring homomorphism corresponding to $f$. There exists a spectral sequence of $B$-modules, with initial term

$$
E^{p,q}_{2} = H^{p}_{Y'}(Y, R^{g}f_{*}(F)),
$$

<!-- label: eq:V.3.15 -->

abutting to the $B$-module $H\bullet_{X'}(X, F)_{f}$.

*Proof.* Let $\mathcal{O}_{Y,Y'}$ be the sheaf $\mathcal{O}_{Y}|Y'$ extended by `0` outside $Y'$ (see Exp. I). One has
an isomorphism of $B$-modules:

```text
Hom(𝒪_{Y,Y′}, f_*(F)) ≅ Hom(f*(𝒪_{Y,Y′}), F)_[f].
```

<!-- label: eq:V.3.16 -->

Now one has

$$
f*(\mathcal{O}_{Y,Y'}) = \mathcal{O}_{X,X'},
$$

<!-- label: eq:V.3.17 -->

and moreover if $G$ is an injective $\mathcal{O}_{X}$-Module, then $f_{*}(G)$ is an injective $\mathcal{O}_{Y}$-Module,
at least if $f$ is flat — a case to which one easily reduces by replacing $\mathcal{O}_{X}$, etc., by the constant
sheaves of rings $\mathbb{Z}$. Hence the spectral sequence of the composite functor

$$
F \mapsto \operatorname{Hom}(\mathcal{O}_{Y,Y'}, f_{*}(F)),
$$

with initial term

```text
E₂^{p,q} = Extᵖ(Y; 𝒪_{Y,Y′}, Rᵍf_*(F)),
```

abuts, taking into account (16) and (17), to

$$
Ext\bullet(X; \mathcal{O}_{X,X'}, F)_{f}.
$$

The lemma then follows from (I 13 bis). QED

<!-- original page 53 -->

Let now $f: B \to A$ be a surjective homomorphism of local rings. Let

$$
f: \operatorname{Spec}(A) \to \operatorname{Spec}(B)
$$

be the corresponding morphism of affine schemes. Set $X = \operatorname{Spec}(A)$ (resp. $X' = {\mathfrak{m}_{A}}$),
$Y = \operatorname{Spec}(B)$ (resp. $Y' = {\mathfrak{m}_{B}}$), and let $M$ be an $A$-module and $\tilde{M}$ the
corresponding $\mathcal{O}_{X}$-Module. Since $R^{g}f_{*}(\tilde{M}) = 0$ for $q > 0$, the spectral sequence (15)
degenerates, and by (3.2) one obtains an isomorphism of $B$-modules:

```text
Hⁿ_{{𝔪_B}}(Y, f_*(M̃)) ≅ Hⁿ_{{𝔪_A}}(X, M̃)_[f],
```

<!-- label: eq:V.3.18 -->

hence an isomorphism of $B$-modules:

$$
H^{n}_{\mathfrak{m}_{B}}(M_{f}) \cong H^{n}_{\mathfrak{m}_{A}}(M)_{f}.
$$

<!-- label: eq:V.3.19 -->

On the other hand, if `D_A` (resp. `D_B`) is the dualizing functor for $A$ (resp. $B$), one has

$$
D_{A}(M)_{f} \cong D_{B}(M_{f}).
$$

<!-- label: eq:V.3.20 -->

Finally, since one has a ring isomorphism

```text
B/Ann M_[f] ≅ A/Ann M,
```

<!-- label: eq:V.3.21 -->

one sees that the change of base rings under consideration changes nothing. So suppose $A$ is regular of dimension $r$.

By (2.1) one has

$$
D(H^{i}(M)) = Ext^{r-i}(M, A).
$$

<!-- label: eq:V.3.22 -->

We shall prove the equivalence of the following properties:

(a) $\dim Ext^{j}(M, A) \leqslant r - j$;

(b) for every $\mathfrak{p} \in X = \operatorname{Spec}(A)$ such that $\dim A_{\mathfrak{p}} < j$, one has
$Ext^{j}(M, A)_{\mathfrak{p}} = 0$;

(c) $codim(Supp(Ext^{j}(M, A)), X) \geqslant j$.

To prove (a) ⇒ (b), let $\mathfrak{p} \in X$ with $\dim A_{\mathfrak{p}} < j$; then $\dim A/\mathfrak{p} > r - j$, hence
by (a) $Ann(Ext^{j}(M, A)) \not\subset \mathfrak{p}$, which entails $Ext^{j}(M, A)_{\mathfrak{p}} = 0$. Let
$\mathfrak{p} \in Supp(Ext^{j}(M, A))$; then $Ext^{j}(M, A)_{\mathfrak{p}} \neq 0$, so by (b)
$\dim A_{\mathfrak{p}} \geqslant j$. Hence `codim(Supp(Extʲ(M, A)), X) = inf{dim A_𝔭 | 𝔭 ∈ Supp(Extʲ(M, A))} ⩾ j`, that
is, (b) ⇒ (c). Finally (c) implies (a) trivially.

Let us now prove the theorem.

(i) Let $x = (x_{1}, \cdots, x_{r})$ be a system of parameters for $A$ such that $x_{i} \in Ann M$ for
$i = 1, \cdots, r - n$. Let $K\bullet((x^{k}), M)$ be the Koszul complex. One sees easily that the map
$K^{i}((x^{k}), M) \to K^{i}(({x^{k}}'), M)$ for $k < k'$ is zero, if $i > n$. It follows that
$H^{i}(M) = \lim\to H^{i}((x^{k}), M) = 0$ if $i > n$. On the other hand, it is trivial that $H^{i}(M) = 0$ if $i < 0$,
so (i) is proved.

(ii) Since $A$ is regular, $\dim A_{\mathfrak{p}} < j$ entails that the global homological dimension of
$A_{\mathfrak{p}}$ is strictly less than $j$, and hence
$Ext^{j}(M, A)_{\mathfrak{p}} = Ext^{j}_{A_{\mathfrak{p}}}(M_{\mathfrak{p}}, A_{\mathfrak{p}}) = 0$; so one has proved
(b) and consequently (a). (ii) then follows from (22) and from (a).

(iii) There exists a $\mathfrak{p} \in Supp(M)$ such that $\dim A_{\mathfrak{p}} = r - n$ and such that
$Supp(M_{\mathfrak{p}}) = {\mathfrak{m}_{A_{\mathfrak{p}}}}$. Since $A_{\mathfrak{p}}$ is regular if $A$ is, one finds
$prof A_{\mathfrak{p}} = r - n$, hence

```text
Extʳ⁻ⁿ_A(M, A)_𝔭 = Extʳ⁻ⁿ_{A_𝔭}(M_𝔭, A_𝔭) ≠ 0.
```

<!-- label: eq:V.3.23 -->

<!-- original page 54 -->

This implies, taking (22) into account, that on the one hand

$$
H^{n}(M) \neq 0,
$$

and on the other hand

$$
\dim D(H^{n}(M)) \geqslant n,
$$

hence by (ii)

$$
\dim D(H^{n}(M)) = n.
$$

Let now $Y = Supp(M)$. By (i) one knows that $D(H^{n}(M')) = Ext^{r-n}(M', A)$ is a functor in $M'$, left exact, on the
category $(\mathcal{C}_{Y})^{\circ}$. Hence there exists an $A$-module $H$ and an isomorphism of functors in $M'$:

```text
Extʳ⁻ⁿ(M′, A) = Hom(M′, H).
```

Let `Yᵢ`, $i = 1, \cdots, k$, be the irreducible components of $Y$ of maximum dimension. We shall see that the assertion
$Ext^{r-n}(M', A) \neq 0$ is equivalent to the assertion: there exists an $i$ such that $Supp M' \supset Y_{i}$. Indeed,
if $Supp M' \supset Y_{i}$, then $\dim(M') = n$, hence $Ext^{r-n}(M', A) \neq 0$.

If $Supp M' \not\supset Y_{i}$ for every $i = 1, \cdots, k$, then $\dim M' < n$ and

$$
D(H^{n}(M')) = Ext^{r-n}(M', A) = 0.
$$

Since `Ass(Extʳ⁻ⁿ(M, A)) = Supp M ∩ Ass(H)`, one sees that the last assertion of (iii) follows from the following lemma:

**Lemma 3.3.**

<!-- label: V.3.3 -->

Let $X = \operatorname{Spec}(A)$, let $Y$ be a closed subset of $X$, let $T: (\mathcal{C}_{Y})^{\circ} \to Ab$ be a left
exact functor, and let `Yᵢ`, $i = 1, \cdots, k$, be a family of irreducible components of $Y$ such that the assertion:
$T(M) = 0$ is equivalent to the assertion: $\forall i, Supp M \not\supset Y_{i}$. Then $T$ is representable by a module $H$
such that $Ass(H) = \bigcup^{k}_{i=1} {y_{i}}$, where `yᵢ` is the generic point of `Yᵢ`, $i = 1, \cdots, k$.

*Proof.* Let $y \in Y$; one constructs an $A$-module $M(y)$ such that $Supp(M(y)) = {y}$. Suppose that $y \neq y_{i}$
for every $i = 1, \cdots, k$; then $Y_{i} \not\subset Supp(M(y))$ for every $i = 1, \cdots, k$, so $T(M(y)) = 0$. It
follows that

```text
Ass(T(M(y))) = Supp(M(y)) ∩ Ass(H) = ∅,
```

hence $y \notin Ass(H)$. If $y = y_{i}$, then $Y_{i} \subset Supp(M(y))$, so $T(M(y)) \neq 0$, whence

```text
Ass(T(M(y))) = Supp(M(y)) ∩ Ass(H) ≠ ∅.
```

By the first part of the proof, this implies $y \in Ass(H)$, whence the lemma. QED

**Example 3.4.**

<!-- label: V.3.4 -->

Let $A$ be a noetherian ring, let $X = \operatorname{Spec}(A)$, and let $Y$ be a closed subset of $X$ such that $X - Y$
is affine; then for every irreducible component $Y_{\alpha}$ of $Y$ one has $codim(Y_{\alpha}, X) \leqslant 1$.

Indeed, consider $X$ as a prescheme over $X$. Let $y_{\alpha} \in Y_{\alpha}$ be a generic point, and consider the
morphism $\operatorname{Spec}(\mathcal{O}_{X,y_{\alpha}}) \to X$. The affine scheme obtained by base extension of $X$ to
$\operatorname{Spec}(\mathcal{O}_{X,y_{\alpha}})$ is canonically isomorphic to
$\operatorname{Spec}(\mathcal{O}_{X,y_{\alpha}})$.

By (EGA I 3.2.7) one sees that if $y_{0}$ is the unique closed point of
$Y_{0} = \operatorname{Spec}(\mathcal{O}_{X,y_{\alpha}})$, then $Y_{0} - y_{0}$ is affine. By (EGA III 1.3.1) one finds

```text
Hⁱ(Y₀ − y₀, 𝒪_{Y₀}) = 0   if i > 0,
```

<!-- original page 55 -->

hence by (I 2.9)

```text
Hⁱ⁻¹(𝒪_{X,y_α}) = Hⁱ_{{y₀}}(Y₀, 𝒪_{Y₀}) = 0   if i ⩾ 2.
```

Taking 3.1 (iii) into account, it follows that

$$
\dim \mathcal{O}_{X,y_{\alpha}} \leqslant 1,
$$

hence `codim(Y_α, X) = inf_{y ∈ Y_α} dim 𝒪_{X,y} ⩽ 1`. QED

Let $A$ be a noetherian local ring, $\mathfrak{m}$ its maximal ideal, and $M$ a finitely generated $A$-module. Suppose
that $A$ is a quotient of a regular local ring. Set $X = \operatorname{Spec}(A)$, and for every $x \in X$,
$\mathfrak{m}_{x} = \mathfrak{m}A_{x}$.

**Proposition 3.5.**

<!-- label: V.3.5 -->

The following two conditions are equivalent:

a) $H^{i}(M)$ is of finite length;

b) $\forall x \in X - {\mathfrak{m}}, H^{i-dim} {x}_{\mathfrak{m}_{x}}(M_{x}) = 0$.

*Proof.* Taking (3.2) into account, we may suppose $A$ regular. By (2.1) we have

$$
H^{i}(M) = D(Ext^{r-i}(M, A)),
$$

where $r = \dim A$. By (IV 4.7), a) is equivalent[^V-3-4] to

```text
Extʳ⁻ⁱ(M, A) is of finite length.
```

<!-- label: eq:V.3.24 -->

Now (24) is equivalent to

```text
∀ x ∈ X − {𝔪}, one has Extʳ⁻ⁱ(M, A)_x = 0.
```

<!-- label: eq:V.3.25 -->

On the other hand $A_{x}$ is regular of dimension $r - \dim {x}$, so by (2.1)

```text
Hⁱ⁻ᵈⁱᵐ {x}_{𝔪_x}(M_x) = D(Ext^{(r − dim {x}) − (i − dim {x})}_{A_x}(M_x, A_x)) = D(Extʳ⁻ⁱ_{A_x}(M_x, A_x)).
```

<!-- label: eq:V.3.26 -->

Since $M$ is finitely generated, one has

```text
Extʳ⁻ⁱ_A(M, A)_x = Extʳ⁻ⁱ_{A_x}(M_x, A_x),
```

whence the proposition.

**Corollary 3.6.**

<!-- label: V.3.6 -->

In order that $H^{i}(M)$ be of finite length for $i \leqslant n$, it is necessary and sufficient that

```text
prof(M_x) > n − dim {x}
```

for every $x \in X - {\mathfrak{m}}$.

*Proof.* Follows from (3.5) and (III 3.1).

<!--
LEDGER DELTA (Exposé V):
| French | English | Note |
| --- | --- | --- |
| Complexes d'homomorphismes | Complexes of homomorphisms | Section title; preserves the `Hom•` dot notation in body. |
| modules gradués | graded modules | Standard. |
| ∂-foncteur / δ-foncteur | ∂-functor / δ-functor | Preserve Grothendieck's distinction between `∂` and `δ`. |
| résolution injective | injective resolution | Standard. |
| augmentation canonique | canonical augmentation | Standard. |
| homomorphes à zéro | homotopic to zero | Standard. |
| accouplement | pairing | Standard category-theoretic term. |
| anneau local régulier | regular local ring | Per glossary. |
| Théorème des syzygies | syzygy theorem | Hilbert's syzygy theorem; the source uses singular "théorème", rendered as English "syzygy theorem". |
| module dualisant | dualizing module | Per glossary. |
| foncteur dualisant | dualizing functor | Per glossary. |
| limite inductive | direct limit | Per glossary; rendered "direct limit" (modern English) here. |
| espace annelé | ringed space | Per glossary. |
| `𝒪_X`-Module | `𝒪_X`-Module | Capital "Module" preserved (sheaf-of-modules) per SGA convention. |
| suite spectrale | spectral sequence | Per glossary. |
| terme initial | initial term | Per glossary. |
| aboutissement / aboutit à | abutment / abuts to | Per glossary. |
| changement d'anneaux de base | change of base rings | Standard. |
| `M`-[f] (extension of scalars) | `M_[f]` | The bracketed `[f]` denotes restriction/extension of scalars along `f`; preserved as `_[f]`. |
| Théorème de Cohen | theorem of Cohen | Cohen's structure theorem for complete local rings. |
| anneau noethérien | noetherian ring | Standard. |
| de type fini | finitely generated (for modules) | Per glossary; "of finite type" not used here since context is module-level. |
| dimension homologique globale | global homological dimension | Standard. |
| système de paramètres | system of parameters | Standard. |
| complexe de Koszul | Koszul complex | Standard. |
| composantes irréductibles | irreducible components | Standard. |
| point générique | generic point | Standard. |
| partie fermée | closed subset | Standard. |
| `(𝒞_Y)°` | `(𝒞_Y)°` | Opposite category of coherent sheaves with support in `Y`; preserved. |
| Ass | Ass | Associated primes; preserved as Ass. |
| prof | prof | Depth functor; preserved as `prof` (matches source). |
| section hyperplane | n/a | Not used in this Exposé. |
| extension du schéma de base | base extension | Standard. |
| C.Q.F.D. / Q.E.D. | QED | Preserved as English "QED" per glossary. |
| `[f]` (restriction-of-scalars subscript) | `_[f]` | The source brackets `[f]` indicate restriction of scalars; rendered as a subscript `_[f]`. |
| `^` (hat / formal completion) | `Â`, `M̂`, `Î` | Hat indicates formal completion / `m`-adic completion; rendered with Unicode combining hat. |
-->

[^V-1-1]: *N.D.E.* The original sign convention was different; but it is not compatible with the convention of Exposé
    VIII, which seems more reasonable, since in that case the cohomology in degree `0` is the set of homotopy classes of
    morphisms from $F\bullet$ into $G\bullet$. The calculations have been modified accordingly in what follows.

[^V-1-2]: *N.D.E.* The strange original numbering has been preserved.

[^V-1-3]: *N.D.E.* We still write $M$ for the complex `M[0]` consisting of $M$ placed in degree `0`.

[^V-3-4]: *N.D.E.* Indeed, the point is to show that, $E$ being a finitely generated $A$-module, if $D(E)$ is of finite
    length then $E$ is of finite length. Let $K$ (resp. $Q$) be the kernel (resp. cokernel) of the canonical morphism
    $\epsilon: E \to DD(E)$. The composition of $D(\epsilon)$ and the canonical morphism $\gamma: D(E) \to DDD(E)$ is
    the identity of $D(E)$. Since $D(E)$ is of finite length, $\gamma$ is an isomorphism, and hence so is $D(\epsilon)$.
    Since $D$ is exact, it follows that $D(K)$ and $D(Q)$ are zero. It suffices to prove that if $M$ is an $A$-module
    with zero dual, then $M$ is zero, for one will then have $E = DD(E)$ of finite length, just like $D(E)$. Indeed, let
    $M_{0}$ be a finitely generated submodule of $M$. Since $D$ is exact, $D(M_{0})$ is a quotient of $D(M)$, which is
    zero. Again by the exactness of $D$, one has $D(M_{0}/\mathfrak{m}_{A} M_{0}) = 0$, and hence, by biduality, the
    finite-length module $M_{0}/\mathfrak{m}_{A} M_{0}$ is zero. Nakayama's lemma then ensures the vanishing of $M_{0}$,
    and finally one obtains that of $M$.


<!-- SOURCE: 06-foncteurs-Ext.md -->

# Exposé VI. The functors $Ext^{\bullet}_{Z}(X; F, G)$ and $\mathcal{E}xt^{\bullet}_{Z}(F, G)$

<!-- label: VI -->

<!-- original page 72 -->

<!-- Editorial note: Throughout this Exposé we write `ℰxt^i_Z(F, G)` (script `ℰ`)
for the sheafified version of `Ext` (the variant underlined in the original source)
and `Ext^i_Z(X; F, G)` for the global one. Wherever the OCR shows two parallel
forms `ExtiZ (X; F, G)` and `ExtiZ (F, G)` for the same derived functor, the second
one is the sheafified version, and is rendered `ℰxt^i_Z(F, G)`. -->

## 1. Generalities

<!-- label: VI.1 -->

### 1.1.

<!-- label: VI.1.1 -->

Let $(X, \mathcal{O}_{X})$ be a ringed space and let $Z$ be a locally closed subset of $X$. Let $F$ and $G$ be
$\mathcal{O}_{X}$-Modules; we denote by $Ext^{i}_{Z}(X; F, G)$ (resp. $\mathcal{E}xt^{i}_{Z}(F, G)$) the $i$-th derived
functor of the functor $G \mapsto \Gamma_{Z}(\operatorname{Hom}_{\mathcal{O}_{X}}(F, G))$ (resp.
$G \mapsto \Gamma Z(\mathcal{H}om_{\mathcal{O}_{X}}(F, G))$, where $\Gamma Z$ denotes the sheafified
sections-with-support functor and $\mathcal{H}om_{\mathcal{O}_{X}}$ the sheafified `Hom`).

**Lemma.**

<!-- label: VI.1.2 -->

The sheaf $\mathcal{E}xt^{i}_{Z}(F, G)$ is canonically isomorphic to the sheaf associated with the presheaf
$U \mapsto Ext^{i}_{Z \cap U}(U; F|U, G|U)$.

This follows from (*Tôhoku*, 3.7.2) together with the fact that
$\Gamma(U; \Gamma Z(\mathcal{H}om_{\mathcal{O}_{X}}(F, G)))$ is canonically isomorphic to
$\Gamma_{Z \cap U}(\operatorname{Hom}_{\mathcal{O}_{X}|U}(F|U, G|U))$.

**Theorem (Excision theorem).**

<!-- label: VI.1.3 -->

Let $V$ be an open subset of $X$ containing $Z$. Then one has an isomorphism of cohomological functors

```text
Ext^•_X(X; F, G) ≃ Ext^•_V(V; F|V, G|V).
```

<!-- label: eq:VI.1.3.1 -->

Indeed, if $G^{\bullet}$ is an injective resolution of $G$, then $G^{\bullet}|V$ is an injective resolution of $G|V$.
The theorem follows immediately.

### 1.4.

<!-- label: VI.1.4 -->

Let $\mathcal{O}_{X,Z}$ be the $\mathcal{O}_{X}$-Module defined by the following conditions ([Godement], 2.9.2):
$\mathcal{O}_{X,Z}|_{X - Z} = 0$ and $\mathcal{O}_{X,Z}|_{Z} = \mathcal{O}_{X}|_{Z}$. We have seen that for every
$\mathcal{O}_{X}$-Module $H$ there is a functorial isomorphism
$\Gamma_{Z}(H) \simeq \operatorname{Hom}_{\mathcal{O}_{X}}(\mathcal{O}_{X,Z}, H)$. From this we deduce functorial
isomorphisms in $F$ and $G$:

```text
Γ_Z(Hom_{𝒪_X}(F, G)) ≃ Hom_{𝒪_X}(𝒪_{X,Z}, Hom_{𝒪_X}(F, G)),
```

<!-- label: eq:VI.1.4.1 -->

```text
Γ_Z(Hom_{𝒪_X}(F, G)) ≃ Hom_{𝒪_X}(𝒪_{X,Z} ⊗_{𝒪_X} F, G),
```

<!-- label: eq:VI.1.4.2 -->

```text
Γ_Z(Hom_{𝒪_X}(F, G)) ≃ Hom_{𝒪_X}(F, Hom_{𝒪_X}(𝒪_{X,Z}, G)) = Hom_{𝒪_X}(F, Γ_Z(G)).
```

<!-- label: eq:VI.1.4.3 -->

<!-- original page 73 -->

It follows in particular from (1.4.2) that there is a $\partial$-functorial isomorphism in $F$ and $G$

```text
θ: Ext^i_{𝒪_X}(𝒪_{X,Z} ⊗_{𝒪_X} F, G) ⥲ Ext^i_Z(X; F, G).
```

<!-- original page 74 -->

<!-- Editorial note: the source paginates the displayed θ-isomorphism at the
foot of page 73 and the section heading 1.5 at the top of page 74; the running
header on page 74 is the Exposé title, which we omit. -->

### 1.5.

<!-- label: VI.1.5 -->

By definition, the functor $G \mapsto \Gamma_{Z}(\operatorname{Hom}_{\mathcal{O}_{X}}(F, G))$ is the composite of the
functor $G \mapsto \operatorname{Hom}_{\mathcal{O}_{X}}(F, G)$ and the functor $\Gamma_{Z}$. Since $\Gamma_{Z}$ is left
exact (I 1.9), since $\operatorname{Hom}_{\mathcal{O}_{X}}(F, G)$ is flasque whenever $G$ is injective, and since
$\Gamma_{Z}$ is exact on flasque sheaves (I 2.12), it follows from (*Tôhoku*, 2.4.1) that there is a spectral functor
abutting to $Ext^{\bullet}_{Z}(X; F, G)$ whose initial term is
$H^{p}_{Z}(X, \mathcal{E}xt^{q}_{\mathcal{O}_{X}}(F, G))$.

On the other hand, it follows from (1.4.3) that $\Gamma_{Z}(\operatorname{Hom}_{\mathcal{O}_{X}}(F, G))$ is the
composite of $\Gamma_{Z}$ and the functor $H \mapsto \operatorname{Hom}_{\mathcal{O}_{X}}(F, H)$.

Since the functor $\Gamma_{Z}$ takes injectives to injectives (I 1.4), it follows from (*Tôhoku*, 2.4.1) that there is a
spectral functor abutting to $Ext^{\bullet}_{Z}(X; F, G)$ whose initial term is
$Ext^{p}_{\mathcal{O}_{X}}(X; F, \mathcal{H}^{q}_{Z}(G))$.

It follows finally, from (1.4.2) and the spectral sequence for `Ext`, that there is a spectral functor abutting to
$Ext^{\bullet}_{Z}(X; F, G)$ whose initial term is $H^{p}(X; \mathcal{E}xt^{q}_{Z}(F, G))$. Whence the

**Theorem.**

<!-- label: VI.1.6 -->

There exist three spectral functors abutting to $Ext^{\bullet}_{Z}(X; F, G)$ whose initial terms are respectively

$$
H^{p}_{Z}(X, \mathcal{E}xt^{q}_{\mathcal{O}_{X}}(F, G))
$$

<!-- label: eq:VI.1.6.1 -->

$$
H^{p}(X, \mathcal{E}xt^{q}_{Z}(F, G))
$$

<!-- label: eq:VI.1.6.2 -->

$$
Ext^{p}_{\mathcal{O}_{X}}(X; F, \mathcal{H}^{q}_{Z}(G)).
$$

<!-- label: eq:VI.1.6.3 -->

### 1.7.

<!-- label: VI.1.7 -->

Let now $Z'$ be a closed subset of $Z$ and let $Z'' = Z - Z'$. We have an exact sequence

$$
0 \to \mathcal{O}_{X,Z''} \to \mathcal{O}_{X,Z} \to \mathcal{O}_{X,Z'} \to 0
$$

<!-- label: eq:VI.1.7.1 -->

which generalizes the exact sequence of ([Godement], 2.9.3). This exact sequence splits locally; hence for every
$\mathcal{O}_{X}$-Module $F$ we have a further exact sequence:

```text
0 → F ⊗_{𝒪_X} 𝒪_{X,Z″} → F ⊗_{𝒪_X} 𝒪_{X,Z} → F ⊗_{𝒪_X} 𝒪_{X,Z′} → 0.
```

<!-- label: eq:VI.1.7.2 -->

Let now $G$ be an $\mathcal{O}_{X}$-Module; applying the functor $\operatorname{Hom}_{\mathcal{O}_{X}}(\bullet, G)$ to
the exact sequence (1.7.2), one deduces from (1.4.2) and the long exact sequence for `Ext` the following theorem:

**Theorem.**

<!-- label: VI.1.8 -->

Let $Z$ be a locally closed subset of $X$, let $Z'$ be a closed subset of $Z$, and let $Z'' = Z - Z'$. Then there is an
exact sequence, functorial in $F$ and $G$:

```text
0 → Hom_{Z′}(F, G) → Hom_Z(F, G) → Hom_{Z″}(F, G) → Ext^1_{Z′}(F, G) → ⋯
    ⋯ → Ext^i_Z(F, G) → Ext^i_{Z″}(F, G) → Ext^{i+1}_{Z′}(F, G) → ⋯
```

**Corollary.**

<!-- label: VI.1.9 -->

Let $Y$ be a closed subset of $X$ and let $U = X - Y$. Then there is an exact sequence, functorial in $F$ and $G$:

```text
0 → Hom_Y(F, G) → Hom_{𝒪_X}(F, G) → Hom_{𝒪_X|U}(F|U, G|U) → Ext^1_Y(F, G) → ⋯
    ⋯ → Ext^i_{𝒪_X}(F, G) → Ext^i_{𝒪_X|U}(F|U, G|U) → Ext^{i+1}_Y(F, G) → ⋯
```

This corollary is an immediate consequence of theorem (1.3) and theorem (1.8).

<!-- original page 75 -->

## 2. Applications to quasi-coherent sheaves on preschemes

<!-- label: VI.2 -->

**Proposition.**

<!-- label: VI.2.1 -->

Let $X$ be a locally noetherian prescheme. For every locally closed subset $Z$ of $X$, every coherent Module $F$, and
every quasi-coherent Module $G$ on $X$, the sheaves $\mathcal{E}xt^{i}_{Z}(F, G)$ are quasi-coherent.

One shows, as in (1.6.3), that the Modules $\mathcal{E}xt^{i}_{Z}(F, G)$ are the abutment of a spectral sequence with
initial term $\mathcal{E}xt^{p}_{\mathcal{O}_{X}}(F, \mathcal{H}^{q}_{Z}(G))$. By (II, cor. 3) the
$\mathcal{H}^{q}_{Z}(G)$ are quasi-coherent, and so are the
$\mathcal{E}xt^{p}_{\mathcal{O}_{X}}(F, \mathcal{H}^{q}_{Z}(G))$, since $F$ is coherent. The proposition follows
immediately.

### 2.2.

<!-- label: VI.2.2 -->

Let now $Y$ be a closed subprescheme of $X$ and let $\mathcal{I}$ be a defining ideal of $Y$. Let $m$ and $n$ be
integers with $m \geqslant n \geqslant 0$; we denote by $i_{n,m}$ the canonical map
$\mathcal{O}_{Y_{m}} = \mathcal{O}_{X}/\mathcal{I}^{m+1} \to \mathcal{O}_{X}/\mathcal{I}^{n+1} = \mathcal{O}_{Y_{n}}$
and by $j_{n}$ the map $\mathcal{O}_{X,Y} \to \mathcal{O}_{Y_{n}}$. The system $(\mathcal{O}_{Y_{n}}, i_{n,m})$ forms a
projective system, and the maps $j_{n}$ are compatible with the $i_{n,m}$.

Applying the functor $Ext^{i}_{\mathcal{O}_{X}}(F \otimes \bullet, G)$, one deduces a morphism

```text
φ′: lim_{→ n} Ext^i_{𝒪_X}(X; F ⊗ 𝒪_{Y_n}, G) → Ext^i_{𝒪_X}(X; F ⊗ 𝒪_{X,Y}, G);
```

this is a morphism of cohomological functors in $G$. The morphism

```text
φ: lim_{→ n} Ext^i_{𝒪_X}(X; F ⊗ 𝒪_{Y_n}, G) → Ext^i_Y(X; F, G)
```

obtained as the composite of $\phi'$ with $\theta$ (cf. 1.4) is therefore likewise a morphism of cohomological functors
in $G$.

One defines in the same way

```text
φ̲: lim_{→ n} ℰxt^i_{𝒪_X}(F ⊗ 𝒪_{Y_n}, G) → ℰxt^i_Y(F, G).
```

<!-- Editorial note: in the source both arrows are called `ϕ`; here `φ̲`
(underlined `φ`) denotes the sheafified variant, to match the global/sheafified
split used elsewhere in this Exposé. -->

**Theorem.**

<!-- label: VI.2.3 -->

<!-- original page 76 -->

Let $X$ be a locally noetherian prescheme, let $Y$ be a closed subset of $X$ defined by a coherent ideal $\mathcal{I}$,
let $F$ be a coherent Module and let $G$ be a quasi-coherent Module. Then:

a) `φ̲` is an isomorphism.

b) If $X$ is noetherian, $\phi$ is an isomorphism.

The proof of b) being almost word for word that of (II 6 b)), thanks to the spectral sequence 1.6.2, we shall not
reproduce it.

For the proof of a), one may, by (2.1), assume $X$ affine with ring $A$, $F$ (resp. $G$) defined by an $A$-module $M$
(resp. $N$), and $\mathcal{I}$ by an ideal $I$. It suffices to prove that the homomorphism

```text
lim_{→ n} Ext^i_A(M/I^n M, N) → Ext^i_Y(X, F, G)
```

<!-- label: eq:VI.2.3.1 -->

deduced from `φ̲` is an isomorphism.

Indeed, for $i = 0$, one can canonically identify both sides of (2.3.1) with the submodule of
$\operatorname{Hom}_{A}(M, N)$ consisting of those elements of $\operatorname{Hom}_{A}(M, N)$ annihilated by some power
of $I$. One then sees that the homomorphism (2.3.1) is none other than the identity map.

The functor $N \mapsto \lim_{\to n} Ext^{\bullet}_{A}(M/I^{n} M, N)$ is a universal $\partial$-functor. We shall show
that the same holds for the functor $N \mapsto Ext^{\bullet}_{Y}(M, N)$. Indeed, if $N$ is an injective module, by (9
and 11), $\mathcal{H}^{q}_{Y}(N) = 0$ for $q \neq 0$; and by (IV.2.2), $\mathcal{H}^{0}_{Y}(N)$ is injective.

<!-- Editorial note: the citations "(9 and 11)" in the source most plausibly
refer to results from the present section's preceding Exposés (likely I 1.4 and
the depth/injectivity material of IV); they are kept verbatim, as in the
French. -->

It follows then that $Ext^{p}_{\mathcal{O}_{X}}(X; M, \mathcal{H}^{q}_{Y}(N)) = 0$ for $p + q \neq 0$; hence, by
(1.6.3), $Ext^{i}_{Y}(M, N) = 0$ for $i \neq 0$ and $N$ injective. This completes the proof.

## Bibliography

Same references as those listed at the end of Exp. I, cited respectively \[*T\hat{o}hoku*\] and [Godement].

<!-- ────────────────────────────────────────────────────────────────────── -->

<!-- Ledger delta — Exposé VI                                                -->

<!-- ────────────────────────────────────────────────────────────────────── -->

<!--
The following terminological choices were fixed in the present Exposé. They
extend the entries already recorded in `glossary.md`; merge into the master
glossary on the next consolidation pass.

| French                                          | English                                            | Note                                                                                  |
| ----------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `Ext^i_Z(X; F, G)`                              | `Ext^i_Z(X; F, G)`                                 | Global Ext with support in `Z`. Non-sheafified.                                       |
| `Ext^i_Z(F, G)` (underlined in source)          | `ℰxt^i_Z(F, G)`                                    | Sheafified Ext with support in `Z`. Script `ℰ` marks the underline in the source.     |
| `ϕ` (global) vs. `ϕ` underlined (sheafified)    | `φ` vs. `φ̲`                                       | The sheafified comparison morphism is rendered with combining low line; parallel to `ΓZ` / `Γ_Z`. |
| `Théorème d'excision`                           | excision theorem                                   | Per source. Attribution kept on the theorem statement (Theorem 1.3).                  |
| `aboutissant à`                                 | abutting to                                        | Standard spectral-sequence term.                                                      |
| `foncteur spectral`                             | spectral functor                                   | SGA usage; the modern phrasing would be "spectral sequence functor".                  |
| `terme initial`                                 | initial term                                       | `E_2`-term in modern parlance; the source says *terme initial* throughout.            |
| `idéal de définition`                           | defining ideal                                     | Of a closed subprescheme.                                                             |
| `presque mot à mot`                             | almost word for word                               | Proof-movement idiom; kept literal.                                                   |

Unresolved / flagged:

- The citation "(9 and 11)" in the proof of Theorem 2.3 is opaque in the source.
  It almost certainly refers to numbered items inside SGA 2 (Exposé I, no. 1.4
  for the injectivity-preservation of `Γ_Z`, and Exposé IV for the depth
  vanishing); the bare "(9 and 11)" reading is preserved with a Editorial note,
  pending a cross-reference pass against the renumbered statements.
- The morphism called `ϕ` twice in the source — once globally, once sheafified —
  has been disambiguated as `φ` / `φ̲` to mirror the `Γ_Z` / `ΓZ` convention
  pinned at first use in this Exposé.
-->


<!-- SOURCE: 07-criteres-de-nullite-coherence.md -->

# Exposé VII. Vanishing criteria and coherence conditions for the sheaves ℰxt^i_Y(F, G)

<!-- label: VII -->

<!-- original page 61 -->

<!-- Editorial note: Throughout this Exposé, following the convention pinned in Exposé VI, the underlined `Ext^i_Z` of
the source — the sheafified Ext functor on `X` — is rendered with a script-E as `ℰxt^i_Z(F, G)`. The non-underlined
global `Ext^i_Z(X; F, G)` is unchanged. Likewise the sheafified local cohomology functor of Exposé I is `ℋ^i_Y(F)`,
while the global one is `H^i_Y(X, F)`. -->

## 1. Study for $i < n$

<!-- label: VII.1 -->

We prove a lemma.

<!-- original page 77 -->

**Lemma.**

<!-- label: VII.1.1 -->

Let $X$ be a locally noetherian prescheme, $Y$ a closed subset of $X$, and $G$ a quasi-coherent
$\mathcal{O}_{X}$-Module. Suppose that for every coherent $\mathcal{O}_{X}$-Module $F$ with support contained in $Y$,
one has

$$
\mathcal{E}xt^{n-1}(F, G) = 0.
$$

Then for every coherent $\mathcal{O}_{X}$-Module $F$ and every closed subset $Z$ of $X$ such that
$Y \supset Supp F \cap Z$, one has

```text
ℰxt^n_Z(F, G) ≅ ℋom(F, ℋ^n_Y(G)).
```

We first remark that

```text
ℰxt^i_Z(F, G) = ℰxt^i_{Z ∩ Supp F}(F, G)
```

(trivial, cf. Exposé VI). We first carry out the proof for $Z = X$, so that $Supp F \subset Y$. The functor

$$
F \mapsto \mathcal{E}xt^{n}(F, G),
$$

defined on the category of coherent $\mathcal{O}_{X}$-Modules with support contained in $Y$, is left exact. By (IV 1.3),
it is represented by

```text
I = lim_{→ k} ℰxt^n(𝒪_X/𝓘^{k+1}, G),
```

where $\mathcal{I}$ is the ideal of definition of $Y$. Now, by (II 6), one knows that

```text
ℋ^n_Y(G) ≅ lim_{→ k} ℰxt^n(𝒪_X/𝓘^{k+1}, G).
```

Whence the conclusion when $Z = X$. Still by (VI 2.3), one knows that

<!-- original page 78 -->

```text
ℰxt^n_Z(F, G) ≅ lim_{→ k} ℰxt^n(F/𝓙^{k+1}F, G),
```

where $\mathcal{J}$ is the ideal of definition of $Z$. The support of $F/\mathcal{J}^{k+1}F$ is contained in $Y$
whenever $Z \cap Supp F \subset Y$; by what we have just proved, we therefore have

```text
ℰxt^n_Z(F, G) ≅ lim_{→ k} ℋom(F/𝓙^{k+1}F, ℋ^n_Y(G)).
```

It remains to show that the natural homomorphism

```text
lim_{→ k} ℋom(F/𝓙^{k+1}F, ℋ^n_Y(G)) → ℋom(F, ℋ^n_Y(G))
```

is an isomorphism when $Z \cap Supp F \subset Y$. Now $X$ can be covered by noetherian affine open sets; one is thus
reduced to the case where $X$ is noetherian affine. Then $F(X)$ is a finitely generated $\mathcal{O}_{X}(X)$-Module and
$Supp \mathcal{H}^{n}_{Y}(G) \subset Y$. Hence every homomorphism $u: F(X) \to \mathcal{H}^{n}_{Y}(G)(X)$ is annihilated
by a power of $\mathcal{I}$, and therefore by a power of $\mathcal{J}$. QED.

**Proposition.**

<!-- label: VII.1.2 -->

Let $X$ be a locally noetherian prescheme, $Y$ a closed subset of $X$, $G$ a quasi-coherent $\mathcal{O}_{X}$-Module,
and $n$ an integer. For any closed subsets $Z$ and $S$ of $X$ such that $Z \cap S = Y$, the following conditions are
equivalent:

1. <!-- label: VII.1.2.i --> `ℋ^i_Y(G) = 0` for `i < n`;

1. <!-- label: VII.1.2.ii --> there exists a coherent `𝒪_X`-Module `F`, of support `S`, such that

    ```text
    ℰxt^i_Z(F, G) = 0 for i < n;
    ```

1. <!-- label: VII.1.2.iii --> for every coherent `𝒪_X`-Module `F` with support contained in `S` (i.e.

    $Supp F \cap Z = Supp F \cap Y$), one has

    ```text
    ℰxt^i_Z(F, G) = 0 for i < n;
    ```

    <!-- original page 79 -->

1. <!-- label: VII.1.2.iv --> for every coherent `𝒪_X`-Module `F`, one has

    ```text
    ℰxt^i_Y(F, G) = 0 for i < n.
    ```

Moreover, if these conditions hold, then for every coherent $\mathcal{O}_{X}$-Module $F$ and every closed subset $Z'$ of
$X$ such that $Z' \cap Supp F = Y \cap Supp F$, one has isomorphisms

```text
ℰxt^n_Z(F, G) ≅ ℰxt^n_Y(F, G) ≅ ℋom(F, ℋ^n_Y(G)).
```

*Proof.* We argue by induction. The proposition is trivial for $n < 0$. Suppose it has been proved for $n < q$. If one
of the conditions holds for $n = q$, and for two subsets $Z$ and $S$ as stated, then by the induction hypothesis we
have, for every closed subset $Z'$ of $X$ and every coherent $\mathcal{O}_{X}$-Module $F$ such that
$Z' \cap Supp F = Y \cap Supp F$, isomorphisms

```text
ℰxt^{q−1}_{Z'}(F, G) ≅ ℋom(F, ℋ^{q−1}_Y(G)) ≅ ℰxt^{q−1}_Y(F, G).
```

<!-- label: eq:VII.1.1 -->

Hence:

- (i) ⇒ (iv), by taking $Z' = Y$ in (1.1);

- (iv) ⇒ (iii), by taking $Z' = Z$ in (1.1);

- (iii) ⇒ (ii), by taking $F = \mathcal{O}_{S}$;

- (ii) ⇒ (i), by taking $Z' = Z$ in (1.1); this gives $\mathcal{H}om(F, \mathcal{H}^{q-1}_{Y}(G)) = 0$. One then remarks
  that

    <!-- original page 63 -->

    ```text
    Supp ℋ^{q−1}_Y(G) ⊂ Y = Z ∩ S ⊂ S = Supp F,
    ```

    and one applies the following lemma:

**Lemma.**

<!-- label: VII.1.3 -->

Let $X$ be a prescheme, let $P$ be a coherent $\mathcal{O}_{X}$-Module, and let $H$ be a quasi-coherent
$\mathcal{O}_{X}$-Module such that

```text
ℋom(P, H) = 0 and Supp P ⊃ Supp H.
```

Then $H = 0$.

It suffices to prove the lemma when $X$ is affine, since the affine open sets form a base of the topology of $X$ and the
hypotheses are preserved by restriction to an open set.

<!-- original page 80 -->

Now in that case one is reduced to a problem on $A$-modules, where $X = \operatorname{Spec}(A)$. One applies the formula
(valid under the sole hypothesis that $M$ is of finite type)

```text
Ass Hom_A(P, H) = Supp P ∩ Ass H.
```

One knows that `Ass H ⊂ Supp H ⊂ Supp P` and that $Ass \operatorname{Hom}_{A}(P, H) = \emptyset$; hence
$Ass H = \emptyset$, so $H = 0$.

<!-- Editorial note: The source states the formula `Ass Hom_A(P, H) = Supp P ∩ Ass H` "under the sole hypothesis that
`M` is of finite type"; in context the finite-type module is `P` (the source uses `M` and `P` interchangeably in this
passage). The formula is the standard one for finitely generated `P` over a noetherian ring. -->

To complete the proof of the proposition, it remains to observe that (iv) allows us to apply 1.1.

**Corollary.**

<!-- label: VII.1.4 -->

Let $G$ be a coherent Cohen-Macaulay $\mathcal{O}_{X}$-Module, and let $n \in \mathbb{Z}$. The conditions of 1.2 are
equivalent to:

1. <!-- label: VII.1.2.v -->
    ```text
    codim(Y ∩ Supp G, Supp G) ⩾ n.
    ```

Recall first that an $\mathcal{O}_{X}$-module is said to be Cohen-Macaulay if, for every $x \in X$, the stalk $G_{x}$ is
a Cohen-Macaulay $\mathcal{O}_{X,x}$-module, i.e. one has for every $x \in S = Supp G$:

```text
prof G_x = dim G_x = dim 𝒪_{S,x}.
```

<!-- label: eq:VII.1.2 -->

By Proposition III 3.3, condition (i) of 1.2 is equivalent to

```text
prof_Y G = inf_{x ∈ Y} prof G_x ⩾ n,
```

<!-- label: eq:VII.1.3 -->

and therefore also to

```text
prof_Y G = inf_{x ∈ Y ∩ S} prof G_x ⩾ n,
```

since the depth of a zero module is infinite. Now, by definition,

```text
codim(Y ∩ S, S) = inf_{x ∈ S ∩ Y} dim 𝒪_{S,x},
```

whence the conclusion, by applying formula (1.2).

We shall now prove a result that lets us deduce the coherence conditions we have in view from certain vanishing
criteria.

<!-- original page 81 -->

<!-- original page 64 -->

**Lemma.**

<!-- label: VII.1.5 -->

Let $X$ be a locally noetherian prescheme. Let $T^{\bullet}$ be an exact contravariant $\partial$-functor, defined on
the category of coherent $\mathcal{O}_{X}$-Modules, with values in the category of $\mathcal{O}_{X}$-Modules. Let $Y$ be
a closed subset of $X$. Let $i \in \mathbb{Z}$. Suppose that, for every coherent $\mathcal{O}_{X}$-Module with support
contained in $Y$, $T^{i} F$ and $T^{i-1} F$ are coherent. Let $F$ be a coherent $\mathcal{O}_{X}$-Module. For $T^{i} F$
to be coherent, it is necessary and sufficient that $T^{i} F''$ be coherent, where we have set

$$
F'' = F/\Gamma_{Y}(F).
$$

Indeed, $F' = \Gamma_{Y}(F)$ is coherent because $X$ is locally noetherian; the cohomology exact sequence of
$T^{\bullet}$ then gives

```text
T^{i−1} F' → T^i F'' → T^i F → T^i F',
```

where the outer terms are coherent, whence the conclusion.

**Lemma.**

<!-- label: VII.1.6 -->

If $F$ and $G$ are coherent, and if $Supp F \subset Y$, then $\mathcal{E}xt^{i}_{Y}(F, G)$ is coherent.

Indeed, $\mathcal{E}xt^{i}_{Y}(F, G)$ is isomorphic to $\mathcal{E}xt^{i}(F, G)$; this is valid, moreover, on any ringed
space $X$: if $Z$ is a closed subset containing $Y \cap Supp F$, then $\mathcal{E}xt^{i}_{Z}(F, G)$ is isomorphic to
$\mathcal{E}xt^{i}_{Y}(F, G)$ (cf. Exposé VI).

**Proposition.**

<!-- label: VII.1.7 -->

Suppose $F$ and $G$ are coherent, and set $S = Supp F$, $S' = S \cap (X - Y)$. Suppose that, for every
$x \in Y \cap S'$, one has $prof G_{x} \geqslant n$. Then $\mathcal{E}xt^{i}_{Y}(F, G)$ is coherent for $i < n$.

Indeed, 1.6 allows us to apply 1.5 to $T^{\bullet}(F) = \mathcal{E}xt^{\bullet}_{Y}(F, G)$. Setting
$F'' = F/\Gamma_{Y}(F)$, one sees that $Supp F'' = S'$. Now, by III 3.3, the hypothesis on the depth of $G$ ensures the
vanishing of $\mathcal{H}^{i}_{Y \cap S'}(G)$ for $i < n$; by 1.2, one deduces the vanishing of $T^{i} F''$ for $i < n$,
whence the conclusion by 1.5.

## 2. Study for $i > n$

<!-- label: VII.2 -->

<!-- original page 82 -->

Let $X$ be a locally noetherian regular prescheme, that is, one all of whose local rings are regular. Let $Y$ be a
closed subset of $X$. Let $F$ and $G$ be two coherent $\mathcal{O}_{X}$-Modules. Set $S = Supp F$,
$S' = S \cap (X - Y)$. Set

```text
m = sup_{x ∈ Y ∩ S} dim 𝒪_{X,x},
n = sup_{x ∈ Y ∩ S'} dim 𝒪_{X,x};
```

one has $n \leqslant m$.

**Proposition.**

<!-- label: VII.2.1 -->

In the situation just described, one has:

1. $\mathcal{E}xt^{i}_{Y}(F, G) = 0$ for $i > m$,
1. $\mathcal{E}xt^{i}_{Y}(F, G)$ is coherent for $i > n$.

<!-- original page 65 -->

Note first that $\mathcal{E}xt^{i}_{Y}(F, G)$ is coherent for every $i$ when $Supp F \subset Y$. Moreover, setting
$F'' = F/\Gamma_{Y}(F)$ as above, one sees that $Supp F'' = S'$, so that (2) follows from (1) and from 1.3.

<!-- Editorial note: The source reference here reads "1.3" (= Lemma VII.1.3) but the argument actually invokes Lemma
VII.1.5 to swap `F` for `F''`. We have preserved the source's "1.3"; readers checking the proof should compare 1.5. -->

To prove (1), one first remarks that

```text
ℰxt^i_Y(F, G) ≅ lim_{→ k} ℰxt^i(F/𝓙^k F, G),
```

where $\mathcal{J}$ is the ideal of definition of $Y$. On the other hand, it follows from Theorem 4.2.2 of (A.
Grothendieck, "Sur quelques points d'algèbre homologique", *Tôhoku Mathematical Journal* **9** (1957), pp. 119–221) that
the Ext sheaves commute with the formation of stalks, at least when $X$ is a locally noetherian prescheme and the first
argument is coherent; since the same is true of direct limits, one finds isomorphisms

```text
(ℰxt^i_Y(F, G))_x ≅ lim_{→ k} Ext^i_{𝒪_{X,x}}((F/𝓙^k F)_x, G_x)
```

for every $x \in X$. Since $Supp \mathcal{E}xt^{i}_{Y}(F, G) \subset S \cap Y$, to conclude it suffices to remark that
$x \in Y \cap S$ entails $\dim \mathcal{O}_{X,x} \leqslant m$, hence

<!-- original page 83 -->

```text
Ext^i_{𝒪_{X,x}}((F/𝓙^k F)_x, G_x) = 0 for i > m,
```

since the global cohomological dimension of a regular local ring is equal to its dimension.[^VII-2-1]

Let $X$ be a locally noetherian prescheme; for every subset $P$ of $X$, set

```text
D(P) = { dim 𝒪_{X,p} | p ∈ P }.
```

**Lemma.**

<!-- label: VII.2.2 -->

If $P$ is the underlying space of a connected subprescheme of $X$, then $D(P)$ is an interval.

<!-- Editorial note: The source reads "sous-préschéma connexe de A"; the symbol "A" is almost certainly an OCR slip
for "X" — the lemma is about subpreschemes of the ambient `X` of the section. We render it as `X`. -->

Indeed, let $\alpha$ and $\beta$ belong to $D(P)$, corresponding to points $p$ and $q$ of $P$. We show that there exists
a sequence of points of $P$, $(p = p_{1}, \cdots, p_{n} = q)$, such that for $1 \leqslant i < n$ one has
$|\dim \mathcal{O}_{X,p_{i}} - \dim \mathcal{O}_{X,p_{i+1}}| = 1$; it will follow that $D(P)$ contains the interval
$[\alpha, \beta]$. For this, one remarks that $p$ and $q$ can be joined by a chain of irreducible components of $P$ such
that two successive components meet. One is reduced to the case where $p$ is the generic point of an irreducible
component $Q$ of $P$, and where $q \in Q$, and so $q \supset p$ as ideals of $\mathcal{O}_{q}$, where the assertion is
trivial from the definition of dimension.

<!-- Editorial note: The source displayed equation reads `dim 𝒪_{X,p_i} − dim 𝒪_{X,p_{i+1}} = 1`, but for the
argument to give an interval-filling chain one needs unit jumps in either direction; we read this as an absolute value
and have rendered it `| … | = 1`. The source also writes the interval as `[p, q]` where `[α, β]` is intended. -->

**Proposition.**

<!-- label: VII.2.3 -->

Let $X$ be a locally noetherian regular prescheme, $Y$ a closed subset of $X$, and $F$ a coherent
$\mathcal{O}_{X}$-Module. Let $P = Y \cap Supp F \cap (X - Y)$. Let $n \in \mathbb{Z}$, and suppose that
$n \notin D(P)$. Then $\mathcal{E}xt^{n}_{Y}(F, \mathcal{O}_{X})$ is coherent.

<!-- original page 66 -->

The conclusion is local and the hypotheses are preserved by restriction to an open set. Now $P$ is closed and so locally
noetherian, hence locally connected; we may therefore assume $X$ affine and noetherian, and $P$ connected. Set
`D(P) = [a, b[`, which is legitimate by the preceding lemma. If $n > b$, we conclude by 2.1; if $n < a$, then
$n < \dim \mathcal{O}_{X,x} = prof \mathcal{O}_{X,x}$ for every $x \in P$, and we conclude by 1.7.

<!-- Editorial note: The source defines `P = Y ∩ Supp F ∩ (X − Y)`, which is empty as written; the intended set is
almost certainly the closure intersection that appears in §1, e.g. `P = Supp F ∩ (closure of (Supp F ∩ (X − Y)))` or
`P = Y ∩ (Supp F ∩ closure …)`, depending on parsing. We have kept the source's expression literally and flagged it
here. The proof below works for any closed `P ⊂ Y ∩ Supp F` on which the dimension function is bounded by an interval
`[a, b[`. -->

## Translation ledger delta

| French                               | English                            | Note                                                                                                        |
| ------------------------------------ | ---------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| critères de nullité                  | vanishing criteria                 | Title-level. Per task spec.                                                                                 |
| conditions de cohérence              | coherence conditions               | Title-level. Per task spec.                                                                                 |
| $Ext^{i}_{Y}(F, G)$ (underlined)     | $\mathcal{E}xt^{i}_{Y}(F, G)$      | Sheafified Ext, per the script-E convention pinned in Exposé VI.                                            |
| $Ext^{i}_{Z}(F, G)$ (non-underlined) | $Ext^{i}_{Z}(X; F, G)$             | Global Ext (when displayed with the ambient $X$); unchanged.                                                |
| `Hom` (underlined)                   | $\mathcal{H}om$                    | Sheaf-Hom, parallel to the $\mathcal{E}xt$ convention.                                                      |
| $H^{i}_{Y}$ (underlined)             | $\mathcal{H}^{i}_{Y}$              | Sheafified local cohomology, matching the glossary entry.                                                   |
| $\Gamma_{Y}(F)$ (underlined)         | $\Gamma_{Y}(F)$                    | Sheafified sections-with-support; rendered without underline per the SGA 2 glossary's note on $\Gamma_{Z}$. |
| $\partial-foncteur$                  | $\partial$-functor                 | Standard.                                                                                                   |
| profondeur (`prof`)                  | depth (`prof`)                     | Standard SGA 2 usage; symbol `prof` kept.                                                                   |
| anneau de Cohen-Macaulay             | Cohen-Macaulay (ring / module)     | Standard.                                                                                                   |
| dimension cohomologique globale      | global cohomological dimension     | Per source.                                                                                                 |
| limite inductive                     | direct limit                       | Modern English; matches glossary policy for SGA 2.                                                          |
| Tôhoku                               | *Tôhoku*                           | Italicized journal title; accent restored.                                                                  |
| il est licite de                     | it is legitimate to                | "Legitimate" reads better than "permitted" in this register.                                                |
| quelles que soient $Z$ et $S$        | for any closed subsets $Z$ and $S$ | Re-articulated as English universal quantifier.                                                             |
| C.Q.F.D.                             | QED                                | Standard.                                                                                                   |
| en vertu de                          | by                                 | "By" suffices for a citation tag.                                                                           |
| compte tenu de                       | (not occurring)                    | —                                                                                                           |
| il en résulte                        | it follows                         | Standard.                                                                                                   |
| toujours d'après                     | still by                           | Standard.                                                                                                   |
| $7\to$, $-\to$, $\sim=$              | $\mapsto$, $\to$, $\cong$          | OCR repair, per the SGA 2 glossary.                                                                         |

[^VII-2-1]: Cf. EGA 0_IV 17.3.1.


<!-- SOURCE: 08-theoreme-de-finitude.md -->

# Exposé VIII. The finiteness theorem

<!-- label: VIII -->

<!-- original page 67 -->

<!-- Editorial note: per the SGA 2 glossary, the sheafified section functor (underlined `ΓZ` in the source) is
rendered with a script-H in cohomological degrees, so `ℋ^i_Y(F)` denotes the sheafified local-cohomology functor and
`H^i_Y(X, F)` its global version. -->

## 1. A biduality spectral sequence[^VIII-1-1]

<!-- label: VIII.1 -->

Let us state the result we want to reach:

**Proposition.**

<!-- label: VIII.1.1 -->

Let $A$ be a noetherian ring and let $I$ be an ideal of $A$. Set $X = \operatorname{Spec}(A)$ and $Y = V(I)$. Let $M$ be
a finitely generated $A$-module of finite projective dimension. Let $F = \tilde{M}$ be the $\mathcal{O}_{X}$-Module
associated with $M$.

1. There exists a spectral sequence

```text
E₂^{p,q} = Ext^p_Y(Ext^{-q}(M, A), A) ⇒ H^{p+q}_Y(X, F).
```

1. There exists a spectral sequence

```text
E₂^{p,q} = Ext^p_Y(Ext^{-q}(F, 𝒪_X), 𝒪_X) ⇒ H^{p+q}_Y(X, F).
```

Of course, 2) is deduced from 1) by remarking that, if $M$ and $N$ are two finitely generated $A$-modules, and if one
sets $F = \tilde{M}$ and $G = \tilde{N}$, then one has isomorphisms

```text
ℋ^•_Y(F) ≅ H̃^•_Y(X, F),
Ext^•_Y(F, G) ≅ Ẽxt^•_Y(F, G),
Ext^•_{𝒪_X}(F, G) ≅ Ẽxt^•_A(M, N).
```

Let $C$ be the category of $A$-modules and `Ab` that of abelian groups. Let $F$ be the functor

```text
F : C → Ab    defined by    M ↦ Γ_Y(M̃).
```

We know from Exposé II that there is an isomorphism of $\partial$-functors

```text
H^•_Y(X, M̃) ≅ R^• F(M).
```

<!-- original page 68 -->

Furthermore, let $Ext^{\bullet}_{Y}$ denote the right derived functors in the second argument of

```text
F ∘ Hom : C° × C → Ab.
```

We know from Exposé VI that there is an isomorphism of $\partial$-functors

```text
Ext^•_Y(M, N) ≃ Ext^•_Y(M̃, Ñ).
```

Let us finally record the following result from Exposé VI: if $C$ is an injective $A$-module and $N$ is a finitely
generated $A$-module, then the sheaf $\operatorname{Hom}(\tilde{N}, \tilde{C}) \cong \operatorname{Hom}\tilde{N, C}$ is
flasque, hence

$$
R^{1} F(\operatorname{Hom}(N, C)) = 0.
$$

It remains to prove the following result:

**Lemma.**

<!-- label: VIII.1.2 -->

Let $A$ be a noetherian ring and let $C$ be the category of $A$-modules. Let $F : C \to Ab$ be a left exact additive
functor such that, for every finitely generated $A$-module $N$ and every injective $A$-module $C$, one has
$R^{1} F(\operatorname{Hom}(N, C)) = 0$. Let $M$ be a finitely generated $A$-module of finite projective dimension. Then
there exists a spectral sequence

```text
E₂^{p,q} = Ext^p_F(Ext^{-q}(M, A), A) ⇒ R^{p+q} F(M),
```

where $Ext^{p}_{F}$ denotes the $p$-th right derived functor of $F \circ \operatorname{Hom}$.

We shall consider only complexes whose differential has degree `+1`. By the hypothesis on $M$, there exists a projective
resolution of $M$ of finite length

$$
u : L^{\bullet} \to M,
$$

where, moreover, the $L^{p}$ are finitely generated modules and $L^{p} = 0$ if $p \notin [-n, 0]$. Let, on the other
hand, $v : M \to I^{\bullet}$ be an injective resolution of $M$. We claim that

```text
v ∘ u : L^• → I^•
```

<!-- label: eq:VIII.1.1 -->

is an injective resolution of $L^{\bullet}$. We must specify what this means.

**Definition.**

<!-- label: VIII.1.3 -->

Let $X^{\bullet}$ be a complex of $A$-modules; by an *injective resolution* of $X^{\bullet}$ one means a homomorphism of
complexes

$$
x : X^{\bullet} \to C^{\bullet}_{X},
$$

such that $C^{p}_{X}$ is injective for every $p \in \mathbb{Z}$, and such that $x$ induces an isomorphism on homology.

**Proposition.**

<!-- label: VIII.1.4 -->

Every left-bounded complex — i.e. such that there exists $q \in \mathbb{Z}$ with $X^{p} = 0$ for $p < q$ — admits an
injective resolution. Moreover, if $u : X^{\bullet} \to Y^{\bullet}$ is a homomorphism of complexes (both left-bounded)
and if $x : X^{\bullet} \to C^{\bullet}_{X}$ and $y : Y^{\bullet} \to C^{\bullet}_{Y}$ are injective resolutions of
$X^{\bullet}$ and $Y^{\bullet}$, then there exists a homomorphism of complexes

$$
C_{u} : C^{\bullet}_{X} \to C^{\bullet}_{Y},
$$

<!-- original page 69 -->

unique up to homotopy, such that the diagram

```text
        x
X^•  ────────►  C_X^•
 │                │
 u                C_u
 │                │
 ▼      y         ▼
Y^•  ────────►  C_Y^•
```

is commutative up to homotopy.

The proof is left to the reader.[^VIII-1-2]

Let us recall a notation introduced in Exposé V.

**Notation.**

Let $X^{\bullet}$ and $Y^{\bullet}$ be two complexes. We denote by
$\operatorname{Hom}^{\bullet}(X^{\bullet}, Y^{\bullet})$ the simple complex whose component of degree $n$ is

```text
(Hom^•(X^•, Y^•))^n = ∏_{−p+q=n} Hom(X^p, Y^q),
```

also written $\operatorname{Hom}^{n}(X^{\bullet}, Y^{\bullet})$, and whose differential is given by

```text
∂^n : Hom^n(X^•, Y^•) → Hom^{n+1}(X^•, Y^•),
∂^n = d′ + (−1)^{n+1} d″,
```

where $d'$ and $d''$ are the differentials (of degree `+1`) induced by those of $X^{\bullet}$ and $Y^{\bullet}$.

Let then $A^{\bullet}$ be the complex defined by $A^{p} = 0$ if $p \neq 0$ and $A^{0} = A$. Let

$$
a : A^{\bullet} \to C^{\bullet}_{A}
$$

be an injective resolution of $A^{\bullet}$. Consider the double complex

```text
Q^{p,q} = Hom(Hom(L^{-q}, A), C_A^p).
```

<!-- label: eq:VIII.1.2 -->

The first spectral sequence of the bicomplex $F Q^{\bullet\bullet}$ will yield the conclusion of Lemma 1.2.

Set

$$
L'^{\bullet} = \operatorname{Hom}^{\bullet}(L^{\bullet}, A^{\bullet}),
$$

<!-- label: eq:VIII.1.3 -->

and

$$
P^{\bullet} = \operatorname{Hom}^{\bullet}(L'^{\bullet}, C^{\bullet}_{A}).
$$

<!-- label: eq:VIII.1.4 -->

One sees easily that $P^{\bullet}$ is the simple complex associated with $Q^{\bullet\bullet}$. Let us compute the
abutment of the spectral sequence, i.e. the homology of $F P^{\bullet}$. For this, using the fact that $L^{\bullet}$ is
finitely generated projective in every dimension, one proves that $L^{\bullet}$ is isomorphic to
$\operatorname{Hom}^{\bullet}(L'^{\bullet}, A^{\bullet})$. From the homomorphism $a : A^{\bullet} \to C^{\bullet}_{A}$
one deduces a homomorphism

```text
b : Hom^•(L′^•, A^•) → Hom^•(L′^•, C_A^•),
```

or equivalently, a homomorphism

$$
c : L^{\bullet} \to P^{\bullet}.
$$

<!-- label: eq:VIII.1.5 -->

<!-- original page 70 -->

This being said, it is easy to see, using the fact that $L'^{\bullet}$ is finitely generated projective in every
dimension and left-bounded, that (1.5) is an injective resolution of $L^{\bullet}$. Applying Proposition 1.4, one
concludes that $P^{\bullet}$ is homotopy-equivalent to $I^{\bullet}$, where $I^{\bullet}$ is the injective resolution of
$M$ introduced earlier (1.1). One deduces that the abutment of the first spectral sequence of the double complex
$F Q^{\bullet\bullet}$, which is $H^{\bullet}(F P^{\bullet})$, is isomorphic to $R^{\bullet} F(M)$.

The initial term of the first spectral sequence of the bicomplex $F Q^{\bullet\bullet}$ is

$$
E^{p,q}_{2} = 'H^{p}(''H^{q}(F Q^{\bullet\bullet})).
$$

For every $p \in \mathbb{Z}$, $C^{p}_{A}$ is injective. By the hypothesis on $F$, the functor (restricted to the
category of finitely generated modules)

```text
N ↦ F Hom(N, C_A^p)
```

is exact. Hence one deduces isomorphisms

```text
″H^q(F Hom(L′^•, C_A^p)) ≅ F Hom(H^{-q}(L′^•), C_A^p).
```

By the definition of $Ext^{\bullet}_{F}$ as the derived functor of $F \circ \operatorname{Hom}$, one deduces
isomorphisms

$$
E^{p,q}_{2} \cong Ext^{p}_{F}(H^{-q}(L'^{\bullet}), A).
$$

Now $L'^{\bullet} = \operatorname{Hom}^{\bullet}(L^{\bullet}, A^{\bullet})$, where $L^{\bullet}$ is a projective
resolution of $M$, whence isomorphisms

$$
Ext^{-q}(M, A) \cong H^{-q}(L'^{\bullet}),
$$

which gives the conclusion. QED.

<!-- Editorial note: the OCR carries `H^q(L′^•)` and `Ext^q(M, A) ≅ H^q(L′^•)` in this paragraph, with the sign of `q`
flipped relative to the intermediate step `″H^q(F Hom(L′^•, C_A^p)) ≅ F Hom(H^{-q}(L′^•), C_A^p)` (line 184-185 of the
source) and relative to the statement of Proposition 1.1 (whose `Ext^{-q}(M, A)` indexes the spectral sequence the
same way). The sign `−q` is the one consistent with both ends of the proof; this is rendered above with the `−q`
convention. The universal isomorphism `Ext^q(M, A) ≅ H^q(L′^•)` is correct in either sign — the displayed form here is
just the `q ↦ −q` reindexing that aligns with E₂. -->

## 2. The finiteness theorem

<!-- label: VIII.2 -->

**Theorem.**[^N.D.E-VIII-1]

<!-- label: VIII.2.1 -->

Let $X$ be a locally noetherian prescheme, $Y$ a closed subset of $X$, and $F$ a coherent $\mathcal{O}_{X}$-Module.
Suppose that $X$ is locally embeddable in a regular prescheme.[^VIII-2-1] Let $i \in \mathbb{Z}$. Suppose that:

a) for every $x \in U = X - Y$, one has

$$
H^{i-c(x)}(F_{x}) = 0,
$$

<!-- original page 71 -->

where one has set[^N.D.E-VIII-2]

```text
c(x) = codim({x}̄ ∩ Y, {x}̄).
```

<!-- label: eq:VIII.2.1 -->

Then:

b) $\mathcal{H}^{i}_{Y}(F)$ is coherent.

**Corollary.**[^N.D.E-VIII-3]

<!-- label: VIII.2.2 -->

Under the hypotheses of the preceding theorem, condition a) is equivalent to:

c) for every $x \in U$ such that $c(x) = 1$, one has $H^{i-1}(F_{x}) = 0$.

**Corollary.**

<!-- label: VIII.2.3 -->

Let $X$ be a locally noetherian prescheme that is locally embeddable in a regular prescheme, let $Y$ be a closed subset
of $X$, let $F$ be a coherent $\mathcal{O}_{X}$-Module, and let $n$ be an integer. The following conditions are
equivalent:

(i) for every $x \in U$, one has $prof F_{x} > n - c(x)$;

(ii) for every $x \in U$ such that $c(x) = 1$, one has $prof F_{x} \geqslant n$;

(iii) for every $i \in \mathbb{Z}$, $\mathcal{H}^{i}_{Y}(F)$ is coherent if $i \leqslant n$;

(iv) $R^{i} i_{*}(F|U)$ is coherent for $i < n$.[^N.D.E-VIII-4]

Suppose these results acquired when $X$ is the spectrum of a regular noetherian ring $A$ and when $F$ is the sheaf
associated with an $A$-module of finite projective dimension.

Let us first remark that, if $(X_{j})_{j \in J}$ is an open covering of $X$ by opens embeddable in a regular scheme,
then each of the above conditions is equivalent to the conjunction of the analogous conditions obtained by replacing $X$
by $X_{j}$, $Y$ by $Y_{j} = Y \cap X_{j}$, and $F$ by $F|X_{j}$. Indeed, only the conditions involving $c(x)$ can
present a difficulty. Let $x \in U$. If $x \in X_{j}$, setting

```text
c_j(x) = codim(X_j ∩ {x}̄ ∩ Y, X_j ∩ {x}̄),
```

one has necessarily $c_{j}(x) \geqslant c(x)$. Let $y \in \bar{x} \cap Y$ which "gives the codimension", i.e. such that
$c(x) = \dim \mathcal{O}_{\bar{x}, y}$, and let $X_{j}$ be an open of the covering such that $y \in X_{j}$; then
$x \in X_{j}$, hence $c_{j}(x) = c(x)$, which lets us conclude that a) for the $X_{j}$ implies a) for $X$.

<!-- original page 72 -->

At this stage, one has only a partial converse, namely that a) for $X$ implies a) for the $X_{j}$ such that
$c(x) = c_{j}(x)$, which suffices for our purposes.[^N.D.E-VIII-5]

One chooses a covering of $X$ by opens embeddable in a regular prescheme. Applying the preceding, one sees that one can
suppose $X$ closed in a regular $X'$. The reduction to $X'$ is then immediate.

One can therefore suppose $X$ regular, and even affine by covering $X$ by affine opens. That one can suppose
$F = \tilde{M}$, where $M$ is of finite projective dimension, will result from the following lemma:

**Lemma.**

<!-- label: VIII.2.4 -->

Let $X$ be a regular noetherian prescheme. Let $F$ be a coherent $\mathcal{O}_{X}$-Module. The function which to each
$x \in X$ assigns the projective dimension of $F_{x}$ is upper-bounded.

Indeed, let $x \in X$ and let $U$ be an affine open neighborhood of $x$. Let $L^{\bullet}$ be a projective resolution of
the module $F(U)$, where the $L^{i}$ are finitely generated. By hypothesis, the ring $\mathcal{O}_{X,x}$ is regular,
hence the projective dimension of $F_{x}$ is finite; let $d$ be that integer. Let

$$
K = \ker(L^{-d} \to L^{-d+1}).
$$

The module $K_{x}$ is free, because $d$ is the projective dimension of $F_{x}$ ([M], Ch. VI, Prop. 2.1). By (EGA 0_I
5.4.1 Errata), one deduces that the $\mathcal{O}_{U}$-Module $\tilde{K}$ is free on a neighborhood $U'$ of $x$, with
$U' \subset U$. Choosing $f \in \mathcal{O}_{X}(U)$ such that $x \in D(f) \subset U'$, one therefore has a projective
resolution of $M_{f}$ (with $M = F(U)$):

$$
0 \to K_{f} \to (L^{d-1})_{f} \to \cdots \to M_{f} \to 0,
$$

which proves that the function under study is upper semi-continuous. Now $X$ is quasi-compact, whence the conclusion.

We henceforth suppose $X$ affine noetherian regular and we suppose that $F = \tilde{M}$, where $M$ is a finitely
generated $A$-module, necessarily of finite projective dimension. We shall proceed in several steps. First, we find a
condition d), equivalent to a), and prove that it is also equivalent to c). Then, using the spectral sequence of the
preceding number, we prove d) ⇒ b). It then remains to prove that (iii) ⇒ (ii); indeed, (i) ⇔ (ii) ⇒ (iii) follows
immediately from a) ⇔ c) ⇒ b).

Let $x \in U$; by hypothesis $\mathcal{O}_{X,x}$ is a regular local ring. Denoting by $D$ the dualizing functor relative
to the local ring $\mathcal{O}_{X,x}$, it follows from (V 2.1) that

```text
D H^{i-c(x)}(F_x) ≅ Ext^{d(x)-i}_{𝒪_{X,x}}(F_x, 𝒪_{X,x}),
```

<!-- original page 73 -->

where one has set

```text
d(x) = dim 𝒪_{X,x} + c(x) = dim 𝒪_{X,x} + codim({x}̄ ∩ Y, {x}̄).
```

<!-- label: eq:VIII.2.2 -->

Now $X$ is noetherian and $F$ is coherent, hence

```text
D H^{i-c(x)}(F_x) ≅ (Ext^{d(x)-i}_{𝒪_X}(F, 𝒪_X))_x.
```

<!-- label: eq:VIII.2.3 -->

Moreover, for a module to be zero, it is necessary and sufficient that its dual be (cf. editor's note (4) on page 54).
For every $q \in \mathbb{Z}$, set

```text
S_q = Supp Ext^q_{𝒪_X}(F, 𝒪_X),
S′_q = S_q ∩ U,    (U = X − Y),
Z_q = S̄′_q ∩ Y.
```

<!-- label: eq:VIII.2.4 -->

From formula (2.3), it follows that a) and c) are respectively equivalent to:

- a′) for every $q \in \mathbb{Z}$ and every $x \in S'_{q}$, one has $q + i \neq d(x)$.
- c′) for every $q \in \mathbb{Z}$ and every $x \in S'_{q}$, if $c(x) = 1$, one has $q + i \neq d(x)$.

Here is the condition d) promised above:

- d) for every $q \in \mathbb{Z}$ and every $y \in Z_{q}$, one has $q + i \neq \dim \mathcal{O}_{X,y}$.

These conditions are equivalent:

a′) ⇒ c′) is trivial.

d) ⇒ a′). Indeed, let $q \in \mathbb{Z}$ and let $x \in S'_{q}$; let $y \in \bar{x} \cap Y$ which[^N.D.E-VIII-6] "gives
the codimension", i.e. such that

```text
dim 𝒪_{{x}̄, y} = codim({x}̄ ∩ Y, {x}̄) = c(x).
```

<!-- label: eq:VIII.2.5 -->

From the fact that $X$ is regular at $y$, one deduces

```text
dim 𝒪_{X, y} = d(x)    (cf. (2.2)).
```

<!-- label: eq:VIII.2.6 -->

But $y \in \bar{x}$, hence $y \in Z_{q}$, whence the conclusion.

c′) ⇒ d). Let $q \in \mathbb{Z}$ and let $y \in Z_{q}$. Provisionally admit that there exists $x \in S'_{q}$ such that

```text
y ∈ {x}̄    and    dim 𝒪_{{x}̄, y} = 1
```

(one also says that $x$ *follows* $y$). It follows that $c(x) = 1$, since $y$ "gives the codimension of $\bar{x} \cap Y$
in $\bar{x}$", because $x \notin Y$. By c′) we extract

$$
q + i \neq d(x).
$$

Whence the conclusion, on noting that $d(x) = \dim \mathcal{O}_{X, y}$ (2.6). The admitted result is expressed in the
following lemma:

<!-- original page 74 -->

**Lemma.**

<!-- label: VIII.2.5 -->

Let $X$ be a locally noetherian prescheme and let $Y$ be a closed subset of $X$. Set $U = X - Y$ and suppose that $U$ is
dense in $X$. For every $y \in Y$, there exists $x \in U$ "which follows it", i.e. such that

```text
y ∈ {x}̄    and    dim 𝒪_{{x}̄, y} = 1.
```

We have applied the lemma taking for $X$ the prescheme $\bar{S}'_{q}$ and for $Y$ the part $Y \cap \bar{S}'_{q}$.

*Proof of 2.5.* — There exists $x \in U$ such that $y \in \bar{x}$; let us therefore choose $x \in U$ such that
$y \in \bar{x}$ and such that $\dim \mathcal{O}_{\bar{x}, y} = r$ be minimal. We must prove that $r = 1$. Since we have
chosen $x$ so that every $z \in \operatorname{Spec}(\mathcal{O}_{\bar{x}, y})$, $z \neq x$, lies in $Y$, ${x}$ is open
in $\operatorname{Spec}(\mathcal{O}_{\bar{x}, y})$. Whence the conclusion.

The second step consists in deducing b) from d).

Set $D(Z_{q}) = {\dim \mathcal{O}_{X,y} | y \in Z_{q}}$. By d), we know that, for every $q \in \mathbb{Z}$,
$q + i \notin D(Z_{q})$. One then applies VII.2.3, and sees that

```text
Ext^{q+i}_Y(Ext^q(F, 𝒪_X), 𝒪_X)    is coherent.
```

The initial term of the spectral sequence of the preceding number is given by

```text
E₂^{p,q} = Ext^p_Y(Ext^{-q}(F, 𝒪_X), 𝒪_X).
```

One deduces that $E^{p,q}_{2}$ is coherent for every $p \in \mathbb{Z}$ and every $q \in \mathbb{Z}$ such that
$p + q = i$. Now there are only finitely many pairs $(p, q)$ with $p + q = i$, and this spectral sequence converges to
$H^{\bullet}_{Y}(F)$, whence the conclusion.

It remains to prove that (iii) ⇒ (ii). Let us write

$$
i : U \to X
$$

for the canonical immersion of $U$ in $X$. Taking into account the exact homology sequence of the closed subset $Y$ (I
2.11), one sees that (iii) is equivalent to:

(iv) $R^{i} i_{*}(F|U)$ is coherent for $i < n$.

Indeed, one has an exact sequence

```text
0 → ℋ^0_Y(F) → F → i_*(F|U) → ℋ^1_Y(F) → 0.
```

Now $\mathcal{H}^{0}_{Y}(F)$ is a quasi-coherent subsheaf of the coherent sheaf $F$, hence is coherent. Therefore
$\mathcal{H}^{1}_{Y}(F)$ is coherent if and only if $i_{*}(F|U)$ is. Moreover, for $p > 0$, the exact cohomology
sequence of the closed subset $Y$ reduces to isomorphisms

$$
R^{p} i_{*}(F|U) \xrightarrow{\sim} \mathcal{H}^{p+1}_{Y}(F).
$$

We shall prove that (iv) ⇒ (ii). For this, recall (ii):

(ii) for every $x \in U$ such that $c(x) = 1$, one has $prof F_{x} \geqslant n$.

We argue by induction on $n$.

If $n = 0$, the two conditions are empty.

<!-- original page 75 -->

If $n = 1$, one supposes that $i_{*}(F|U)$ is coherent. Argue by contradiction and suppose there exists $x \in U$ such
that $c(x) = 1$ and $prof F_{x} = 0$, i.e. $x \in Ass F_{x}$. Let $y \in \bar{x} \cap Y$ such that
$\dim \mathcal{O}_{\bar{x}, y} = 1$. Set

```text
A = 𝒪_{X, y}    and    X′ = Spec(A).
```

Carry out the base change $v : X' \to X$, which is flat:

```text
            v′
   U′ = X′ ×_X U  ──────►  U
        │                   │
       i′                   i
        │                   │
        ▼          v        ▼
       X′  ──────────────► X.
```

<!-- label: eq:VIII.2.7 -->

The morphism $i$ is separated (since it is an immersion), and of finite type (since it is an open immersion and $X$ is
locally noetherian); the base change is flat, hence (EGA III 1.4.15) one has an isomorphism

$$
v^{*}(i_{*}(F|U)) \cong i'_{*}(v'^{*}(F|U)).
$$

<!-- label: eq:VIII.2.8 -->

Let us denote by $\mathfrak{x}$ (resp. $\mathfrak{y}$) the ideal of $A$ corresponding to $x$ (resp. $y$). Set
$G = v'^{*}(F|U)$; then $G$ is coherent and $\mathfrak{x} \in Ass G$, so there exists a monomorphism
$\mathcal{O}_{\bar{x}} \to G$, and consequently $i'_{*}(\mathcal{O}_{\bar{x}}|U')$ is coherent. By the choice of $y$,
$\dim A/\mathfrak{x} = 1$, and consequently the support of $\mathcal{O}_{\bar{x}}$ is reduced to
$\bar{x} = {x} \cup {y}$, since $\bar{x} = \operatorname{Spec}(A/\mathfrak{x})$ as a scheme. It follows that

$$
(\mathcal{O}_{\bar{x}}|U')(U') = Frac(A/\mathfrak{x}),
$$

the field of fractions of $A/\mathfrak{x}$, and

$$
i'_{*}(\mathcal{O}_{\bar{x}}|U')(X') = Frac(A/\mathfrak{x}).
$$

But $Frac(A/\mathfrak{x})$ is not a finitely generated $A$-module, because $\mathfrak{x}$ differs from the maximal ideal
of $A$. Whence a contradiction.

Suppose $n > 1$ and that the result is acquired for the $n' < n$. By the induction hypothesis, for every $x \in U$ such
that $c(x) = 1$, one has $x \notin Ass F_{x}$. Let such an $x$, and let $y \in \bar{x} \cap Y$ such that $x$ follows
$y$, i.e. $\dim \mathcal{O}_{\bar{x}, y} = 1$. Carry out the base change
$v : \operatorname{Spec}(\mathcal{O}_{X, y}) \to X$, keeping the notation of diagram (2.7). One finds, applying (EGA III
1.4.15), isomorphisms

```text
v^*(R^p i_*(F|U)) ≃ R^p i′_*(v′^*(F|U)),    p ∈ ℤ.
```

One thus reduces to the case where $X$ is the spectrum of a local ring $A$ in which $\mathfrak{x}$ is a prime ideal of
dimension `1`, i.e. $\dim A/\mathfrak{x} = 1$. Then set $F' = \Gamma_{Y}(F)$ and $F'' = F/F'$. One sees that
$F_{x} \simeq F''_{x}$ and that $\mathfrak{y} \notin Ass F''$. Moreover $F'|U = 0$, whence, by the exact sequence of the
$R^{p} i_{*}$, isomorphisms

```text
R^p i_*(F|U) ≃ R^p i_*(F″|U),    p ∈ ℤ.
```

<!-- original page 76 -->

Since $n > 1$, one deduces that neither $\mathfrak{x}$ nor $\mathfrak{y}$ belongs to $Ass F''$. Now
$\mathfrak{x}, \mathfrak{y}$ are the only prime ideals of $A$ containing $\mathfrak{x}$; it follows (III 2.1) that there
exists an element $g \in \mathfrak{x}$ which is $M$-regular, where one has set $F = \tilde{M}$, $M = F(X)$. Whence an
exact sequence

```text
0 → M ──g·→ M → N → 0,
```

in which $g\cdot$ denotes multiplication by $g$ in $M$. By the exact homology sequence, one sees that

```text
R^p i_*(Ñ|U)    is coherent for p < n − 1,
```

hence, by the induction hypothesis, $prof(\tilde{N})_{x} \geqslant n - 1$, and therefore $prof F_{x} \geqslant n$. QED.

## 3. Applications

<!-- label: VIII.3 -->

One deduces from these results a coherence condition for the higher direct images of a coherent sheaf under a morphism
that is not proper.

**Theorem.**

<!-- label: VIII.3.1 -->

Let $f : X \to Y$ be a morphism of preschemes. Suppose that $Y$ is locally noetherian and that $f$ is proper. Suppose
that $X$ is locally embeddable in a regular prescheme. Let $n \in \mathbb{Z}$. Let $U$ be an open of $X$ and let $F$ be
a coherent $\mathcal{O}_{U}$-Module. Suppose that, for every $x \in U$ such that
$codim(\bar{x} \cap (X - U), \bar{x}) = 1$, one has $prof F_{x} \geqslant n$. Then the $\mathcal{O}_{Y}$-Modules
$R^{p}(f \circ g)_{*}(F)$ are coherent for $p < n$, where $g$ is the canonical immersion of $U$ in $X$.

Indeed, there exists a Leray spectral sequence whose abutment is $R^{\bullet}(f \circ g)_{*}(F)$ and whose initial term
is given by

```text
E₂^{p,q} = R^p f_*(R^q g_*(F)).
```

Moreover, there exists a coherent $\mathcal{O}_{X}$-Module $G$ such that $G|U \simeq F$ (EGA I 9.4.3). It then follows
from the preceding paragraph that condition (iv) of page 74 is satisfied, i.e. that $R^{q} g_{*}(G|U)$ is coherent for
$q < n$. One then applies the finiteness theorem of EGA III 3.2.1 to $f$ and to the sheaves $R^{q} g_{*}(F)$, and finds
that $E^{p,q}_{2}$ is coherent for $q < n$, whence the conclusion.

**Proposition.**

<!-- label: VIII.3.2 -->

Let $X$ be a locally noetherian prescheme that is locally embeddable in a regular prescheme. Let $U$ be an open of $X$
and let $i : U \to X$ be the canonical immersion. Let $n \in \mathbb{Z}$. Finally, let $F$ be a coherent and
Cohen-Macaulay $\mathcal{O}_{U}$-Module (on $U$!). The following conditions are equivalent:

(a) $R^{p} i_{*}(F)$ is coherent for $p < n$;

(b) for every irreducible component $S'$ of the closure $\bar{S}$ of the support $S$ of $F$, one has

```text
codim(S′ ∩ (X − U), S′) > n.
```

Let $G$ be a coherent $\mathcal{O}_{X}$-Module such that $G|U \simeq F$ (EGA I 9.4.3). Applying Corollary 2.3 to $G$,
one finds that condition (a) is equivalent to:

<!-- original page 77 -->

(c) for every $x \in \bar{S}$, one has $prof F_{x} > n - c(x)$, with

```text
c(x) = codim({x}̄ ∩ Y, {x}̄).
```

(a) ⇒ (b). Indeed, let $S'$ be an irreducible component of $\bar{S}$ and let $s$ be its generic point. Since $F$ is
Cohen-Macaulay, one has $prof F_{s} = \dim \mathcal{O}_{\bar{S}, s} = 0$. Moreover, $\bar{s} = S'$, whence the
conclusion.

(b) ⇒ (a). Let $x \in \bar{S}$ and let $S'$ be an irreducible component of $\bar{S}$ such that $x \in S'$. Let $s$ be
the generic point of $S'$. Since $F$ is Cohen-Macaulay, one knows that

```text
prof F_x = dim 𝒪_{{s}̄, x}.
```

If $c(x) = +\infty$, there is nothing to prove. Otherwise, there exists $y \in Y \cap \bar{x}$ such that

```text
c(x) = dim 𝒪_{{x}̄, y}.
```

Now $\mathcal{O}_{X, y}$ is a quotient of a regular local ring by hypothesis, hence

```text
dim 𝒪_{{s}̄, y} = dim 𝒪_{{s}̄, x} + dim 𝒪_{{x}̄, y} > n.
```

QED.

## Bibliography

1. [M] H. Cartan and S. Eilenberg, *Homological Algebra*, Princeton Math. Series vol. 19, Princeton University Press,
   1956\.

## Translation ledger — Exposé VIII

Terms confirmed or first activated in this Exposé (consult `glossary.md` for the volume-wide list):

| French                                            | English                                   | Note                                                                                                             |
| ------------------------------------------------- | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| suite spectrale de bidualité                      | biduality spectral sequence               | Title-level, §1.                                                                                                 |
| théorème de finitude                              | finiteness theorem                        | Title of §2 and of Exposé.                                                                                       |
| résolution injective (d'un complexe)              | injective resolution (of a complex)       | Definition VIII.1.3.                                                                                             |
| complexe limité à gauche                          | left-bounded complex                      | Used in Proposition VIII.1.4.                                                                                    |
| double complexe / bicomplexe                      | double complex / bicomplex                | Source uses both interchangeably; preserved.                                                                     |
| aboutissement                                     | abutment                                  | Standard for spectral sequences.                                                                                 |
| terme initial                                     | initial term                              | Used for $E_{2}$ page.                                                                                           |
| localement immergeable dans un préschéma régulier | locally embeddable in a regular prescheme | Standing hypothesis of Theorem VIII.2.1.                                                                         |
| $c(x) = codim(\bar{x} \cap Y, \bar{x})$           | $c(x)$ as written                         | Preserved verbatim from (2.1); closures are reduced (cf. N.D.E.).                                                |
| profondeur ($prof F_{x}$)                         | depth ($prof F_{x}$)                      | Per glossary; the source uses `prof`.                                                                            |
| « x suit y »                                      | "$x$ follows $y$"                         | Translator keeps quotation marks since the source flags it; Lemma VIII.2.5.                                      |
| sous-faisceau quasi-cohérent                      | quasi-coherent subsheaf                   | Standard.                                                                                                        |
| de Cohen-Macaulay (sur U !)                       | Cohen-Macaulay (on $U$!)                  | Exclamation preserved; the parenthetical insists $F$ is Cohen-Macaulay on the open $U$, not on a global ambient. |
| condition (a), (b), (c), (d)                      | condition (a), (b), (c), (d)              | Lowercase Latin letters in this Exposé (not Roman); (i)–(iv) in Corollary 2.3 stay Roman, per the source.        |

Note on the $\Gamma Z$/$\mathcal{H}^{\bullet}_{Y}$ typographic convention: in this Exposé, sheafified local cohomology
is rendered $\mathcal{H}^{i}_{Y}(F)$ (script-H) and global sections with support remain $H^{i}_{Y}(X, F)$. The
underlined section functor of the source is, when it appears, written $\Gamma_{Y}$ in line with the volume-wide
convention recorded in the introduction.

[^VIII-1-1]: The reader familiar with the language of Verdier's derived categories will recognize the spectral sequence
    associated with a biduality isomorphism. Cf. SGA 6 I.

[^VIII-1-2]: Cf. also H. Cartan and S. Eilenberg, *Homological Algebra*, Princeton Math. Series, vol. 19, Princeton
    University Press, 1956.

[^N.D.E-VIII-1]: *N.D.E.* For an analogous statement, but in a somewhat more general situation, see Mme Raynaud (Raynaud
    M., "Théorèmes de Lefschetz en cohomologie des faisceaux cohérents et en cohomologie étale. Application au groupe
    fondamental", *Ann. Sci. Éc. Norm. Sup.* (4) **7** (1974), pp. 29–52, proposition II.2.1).

[^VIII-2-1]: This condition can be generalized to the hypothesis of the existence locally on $X$ of a "dualizing
    complex", in the sense defined in R. Hartshorne, *Residues and duality* (cited in footnote (\*) of Exp. IV p. 46).

[^N.D.E-VIII-2]: *N.D.E.* As in Exposé V, $H^{\bullet}_{x}(F)$ denotes the local cohomology
    $H^{\bullet}_{\mathfrak{m}_{x}}(F_{x})$.

[^N.D.E-VIII-3]: *N.D.E.* Strictly speaking, this is a corollary of the proof that follows and not of the statement. The
    implication c) ⇒ a) is tautological. The other direction is not, but follows from the proof. To be precise: as
    below, one covers $X$ by opens embeddable in regular schemes, which allows one, as explained below, to reduce to
    $X = \operatorname{Spec}(A)$ affine regular and $F = \tilde{M}$ where $M$ is an $A$-module of finite projective
    dimension. It is shown in this case that conditions a) and c) are equivalent to the dual conditions a′) and c′). One
    then shows that c′) implies condition d) (see below) which itself implies a′). See the considerations following 2.4.

[^N.D.E-VIII-4]: *N.D.E.* This condition appeared only in the body of the proof, but not in the statement of the
    corollary; since it is used in §3, we have added it.

[^N.D.E-VIII-5]: *N.D.E.* In fact, a) for $X$ implies a) for all the $X_{j}$ as asserted in the original text, but to
    see this one must read the proof that follows in detail. This implication does not seem formal at this stage. Let us
    indeed denote by an index $J$ the conjunctions of a property a), b), or c) for the $X_{j}$. It is proved in the
    proof below that c_J) ⇒ a_J) (this is the chain of implications c′) ⇒ d) ⇒ a′)). Now one has tautologically a) ⇒ c),
    and c) ⇔ c_J), whence a) ⇒ a_J).

[^N.D.E-VIII-6]: *N.D.E.* In all that follows, closures of points are equipped with the reduced structure.


<!-- SOURCE: 09-geometrie-algebrique-et-formelle.md -->

# Exposé IX. Algebraic geometry and formal geometry

<!-- label: IX -->

<!-- original page 99 -->

The goal of this Exposé is to generalize, to the case of a morphism that is not proper, Theorems 3.4.2 and 4.1.5 of EGA
III.

## 1. The comparison theorem

<!-- label: IX.1 -->

Let $f: X \to X'$ be a separated morphism of preschemes of finite type. Suppose that $X$ is locally noetherian. Let $Y'$
be a closed subset of $X'$ and let $Y = f^{-1}(Y')$.

Let $\hat{X}$ and $\hat{X}'$ be the formal completions of $X$ and $X'$ along $Y$ and $Y'$. Let $\hat{f}$ be the morphism
deduced from $f$ by passing to the completions.

```text
    X ◀───── Y               X̂ ──j──▶  X
    │                        │           │
    │ f                      │ f̂         │ f
    ▼                        ▼           ▼
    X′ ◀──── Y′      ,       X̂′ ──i──▶ X′.
```

<!-- label: eq:IX.1.1 -->

<!-- Editorial note: The source diagram (1.1) places the inclusions `Y → X` and `Y′ → X′` to the left, and the
completion-passing square on the right; the OCR has fractured the layout. The left half merely records the closed
subsets `Y ⊂ X` and `Y′ = f(Y) ⊂ X′`, with `f` restricting to `f: Y → Y′`. The square that matters in what follows is
the one on the right. -->

We denote by $j$ (resp. $i$) the homomorphism from $\hat{X}$ into $X$ (resp. from $\hat{X}'$ into $X'$). It is known
that $i$ and $j$ are flat.

Let $I'$ be an ideal of definition of $Y'$, and let $J = f*(I')\cdot \mathcal{O}_{X}$; this is an ideal of definition of
$Y$. One therefore has:

```text
X̂′ = (Y′, lim_{k ∈ ℕ} 𝒪_{X′}/I′^{k+1}),    X̂ = (Y, lim_{k ∈ ℕ} 𝒪_X/J^{k+1}).
```

<!-- label: eq:IX.1.2 -->

For every $k \in \mathbb{N}$, set:

```text
Y′_k = (Y′, 𝒪_{X′}/I′^{k+1}),    Y_k = (Y, 𝒪_X/J^{k+1}).
```

<!-- label: eq:IX.1.3 -->

Let $F$ be a coherent $\mathcal{O}_{X}$-Module. For every $k \in \mathbb{N}$, we set:

```text
F_k = F/J^{k+1}F,    F̂ = j*(F) ≃ lim_{k} F_k.
```

<!-- label: eq:IX.1.4 -->

<!-- original page 100 -->

If we set:

```text
R^i f_*(F)^∧ = lim_{k ∈ ℕ} (R^i f_*(F) ⊗_{𝒪_{X′}} 𝒪_{Y′_k}),    i ∈ ℤ,
```

<!-- label: eq:IX.1.5 -->

<!-- original page 80 -->

one has a natural homomorphism:

```text
r_i: i*(R^i f_*(F)) → R^i f_*(F)^∧,
```

<!-- label: eq:IX.1.6 -->

which is an isomorphism when $R^{i} f_{*}(F)$ is coherent.

As is explained in EGA III 4.1.1, one has a commutative diagram:

```text
                       ρ_i
   i*(R^i f_*(F))  ──────▶  R^i f̂_*(F̂)
        │                       │
     r_i│                       │ψ_i
        ▼          ϕ_i          ▼
   R^i f_*(F)^∧  ──────▶  lim_{k ∈ ℕ} R^i f_*(F_k).
```

<!-- label: eq:IX.1.7 -->

In loc. cit. one finds a commutative diagram, since one knows that $R^{i} f_{*}(F)$ is coherent, and one identifies the
source and target of (1.6). In our case, $R^{i} f_{*}(F)$ will be coherent only for certain values of $i$, for which we
shall study (1.7).

Consider the graded ring

```text
S = ⨁_{k ∈ ℕ} I′^k,
```

<!-- label: eq:IX.1.8 -->

and the graded $S$-Module:

```text
H^i = ⨁_{k ∈ ℕ} R^i f_*(J^k F),    i ∈ ℤ,
```

<!-- label: eq:IX.1.9 -->

whose $S$-Module structure is defined as follows.

<!-- original page 101 -->

The sheaf $R^{i} f_{*}(J^{k} F)$ is associated with the presheaf which, to every affine open $U'$ of $X'$, associates:

```text
H^i(f⁻¹(U′), J^k F | f⁻¹(U′)).
```

<!-- label: eq:IX.1.10 -->

Let $U'$ then be an affine open of $X'$, set

$$
U = f^{-1}(U'),
$$

and let $x' \in I'^{m}(U')$. Let $x$ be the image of $x'$ in $J^{m}(U)$. The homothety of ratio $x$ on $F | U$ maps
$J^{k} F | U$ into $J^{k+m} F | U$, whence, by functoriality, a morphism:

```text
μ^i_{x′, k}(U′): H^i(U, J^k F | U) → H^i(U, J^{k+m} F | U),
```

<!-- label: eq:IX.1.11 -->

defined for every $i \in \mathbb{Z}$ and every $k \in \mathbb{N}$, which gives, by passing to the associated sheaf, the
graded $S$-Module structure on $H^{i}$.

**Theorem.**

<!-- label: IX.1.1 -->

Let $n$ be an integer. Suppose that the graded $S$-Module $H^{i}$ is of finite type for $i = n - 1$ and $i = n$. Then:

(0) $r_{n}$ and $r_{n-1}$ are isomorphisms, and $R^{i} \hat{f}_{*}(\hat{F})$ is coherent for $i = n - 1$;

(1) for $i = n - 1$, $\rho_{i}$, $\varphi_{i}$, and $\psi_{i}$ are topological isomorphisms (in particular, the
filtration defined on $R^{n-1} f_{*}(F)$ by the kernels of the homomorphisms

```text
R^{n−1} f_*(F) → R^{n−1} f_*(F_k)
```

<!-- label: eq:IX.1.12 -->

is $I'$-good);

<!-- original page 81 -->

(2) for $i = n$, $\rho_{i}$, $\varphi_{i}$, and $\psi_{i}$ are monomorphisms; furthermore, the filtration on
$R^{n} f_{*}(F)$ is $I'$-good and $\psi_{n}$ is an isomorphism;

(3) the projective system of the $R^{i} f_{*}(F_{k})$ satisfies, for $i = n - 2, n - 1$, the uniform Mittag-Leffler
condition, i.e. there exists a fixed integer $k \geqslant 0$ such that, for every $p \geqslant 0$ and every
$p' \geqslant p + k$, one has:

```text
Im[R^i f_*(F_{p′}) → R^i f_*(F_p)] = Im[R^i f_*(F_{p+k}) → R^i f_*(F_p)].
```

<!-- original page 102 -->

Proceeding as in EGA III 4.1.8, it is easy to reduce to the case where $X'$ is the spectrum of a noetherian ring $A$. In
this case, one knows that

```text
R^i f_*(F) = H^i(X, F)^~     (cf. 1.10).
```

<!-- label: eq:IX.1.13 -->

Let $I$ be the ideal of $A$ such that $\tilde{I} = I'$, and let

```text
S = ⨁_{k ∈ ℕ} I^k,
```

<!-- label: eq:IX.1.14 -->

```text
H^i = ⨁_{k ∈ ℕ} H^i(X, J^k F),    i ∈ ℤ,
```

<!-- label: eq:IX.1.15 -->

where $H^{i}$ is equipped with the graded $S$-module structure defined by 1.11, where one has taken $U' = X'$.

The proof is modelled on that of EGA III 4.1.5; let us give a summary.

We work on $\varphi_{i}$ and $\psi_{i}$, which correspond to homomorphisms of modules:

```text
                              H^i(X̂, F̂)
                                  │
                                  │ψ_i
                  ϕ_i             ▼
   H^i(X, F)^∧  ──────▶  lim_{k} H^i(X, F_k).
```

<!-- label: eq:IX.1.16 -->

<!-- original page 103 -->

(a) We assume only that $H^{i}$ is a graded $S$-module of finite type. We deduce that the filtration defined on
$H^{i}(X, F)$ by the modules:

```text
R^i_k = ker(H^i(X, F) → H^i(X, F_k))
```

<!-- label: eq:IX.1.17 -->

is $I$-good. For this, we use the cohomology exact sequence:

```text
H^i(X, J^{k+1} F) → H^i(X, F) → H^i(X, F_k),
```

<!-- label: eq:IX.1.18 -->

which shows that the graded $S$-module $\bigoplus_{k \in \mathbb{N}} R^{i}_{k}$ is a quotient of the graded
$S$-submodule

```text
⨁_{k ∈ ℕ} H^i(X, J^{k+1} F)
```

of $H^{i}$, hence is of finite type, since $S$ is noetherian. Whence this first point.

Set:

```text
M^i = H^i(X, F),    H^i_k = H^i(X, F_k).
```

<!-- label: eq:IX.1.19 -->

<!-- original page 82 -->

One has a commutative diagram:

```text
                     s_i
   H^i(X, F)^∧  ─────────▶  lim_{k} (M^i / R^i_k)
        \                         │
         \                        │
          \ ϕ_i                   │ t_i
           \                      ▼
            ──────────────▶  lim_{k} H^i_k,
```

<!-- label: eq:IX.1.20 -->

in which $s_{i}$ is an isomorphism; indeed, the filtration of $H^{i}(X, F)$ is $I$-good. Moreover, $t_{i}$ is a
monomorphism; indeed, the functor `lim` is left exact, and, for every $k \geqslant 0$, the natural morphism
$M^{i} / R^{i}_{k} \to H^{i}_{k}$ is a monomorphism, by definition of $R^{i}_{k}$.

To study the surjectivity of $t_{i}$, we introduce:

```text
Q^i_k = coker(H^i(X, F) → H^i(X, F_k)),
```

<!-- label: eq:IX.1.21 -->

<!-- original page 104 -->

whence a projective system of exact sequences:

```text
0 → R^i_k → M^i → H^i_k → Q^i_k → 0.
```

<!-- label: eq:IX.1.22 -->

Using the cohomology exact sequence:

```text
H^i(X, F) → H^i(X, F_k) → H^{i+1}(X, J^{k+1} F),
```

<!-- label: eq:IX.1.23 -->

one sees that the graded $S$-module

```text
Q^i = ⨁_{k ∈ ℕ} Q^i_k
```

<!-- label: eq:IX.1.24 -->

is a graded $S$-submodule of $H^{i+1}$. Moreover, for every $k \geqslant 0$, one has:

$$
I^{k+1} Q^{i}_{k} = 0,
$$

<!-- label: eq:IX.1.25 -->

since $Q^{i}_{k}$ is the image of $H^{i}_{k}$.

(b) We assume only that $H^{i+1}$ is of finite type, and we focus on $t_{i}$ (forgetting $s_{i}$). Since $S$ is
noetherian, $Q^{i}$ is of finite type; since $I^{k+1} Q^{i}_{k}$ vanishes, we find that there exist an integer
$r \geqslant 0$ and an integer $k_{0} \geqslant 0$ such that

```text
I^r Q^i_k = 0    for k ⩾ k₀.
```

<!-- label: eq:IX.1.26 -->

It follows that the projective system $(Q^{i}_{k})_{k \in \mathbb{N}}$ is essentially zero, and hence the projective
system $(H^{i}_{k})_{k \in \mathbb{N}}$ satisfies the uniform Mittag-Leffler condition. From the exact sequence (1.22)
one deduces the exact sequence

```text
0 → M^i / R^i_k → H^i_k → Q^i_k → 0,
```

<!-- label: eq:IX.1.27 -->

whence the exact sequence:

```text
0 → lim_{k} M^i / R^i_k  ──t_i──▶  lim_{k} H^i_k → lim_{k} Q^i_k.
```

<!-- label: eq:IX.1.28 -->

<!-- original page 105 -->

Now the projective system $(Q^{i}_{k})_{k \in \mathbb{N}}$ is essentially zero, hence $t_{i}$ is an isomorphism.

(c) Let us prove that, if $H^{i}$ is of finite type, then $\psi_{i}$ is an isomorphism. It suffices to apply EGA 0_III
13.3.1, taking as a basis of opens of $X$ the affine opens. This is legitimate;

<!-- original page 83 -->

indeed, by (b), the projective system $(H^{i-1}_{k})_{k \in \mathbb{N}}$ satisfies the Mittag-Leffler condition.

The theorem follows formally from (a), (b), and (c). One will note that, in fact, the proof uses, at each step, the
finiteness of $H^{i}$ only for a single value of $i$.

Let us give some examples in which the hypothesis of Theorem 1.1 is satisfied.

**Corollary.**

<!-- label: IX.1.2 -->

Suppose that $I'$ is generated by a section $t'$ of $\mathcal{O}_{X'}$, and denote by $t$ the corresponding section of
$\mathcal{O}_{X}$. Let $F$ be a coherent $\mathcal{O}_{X}$-module and let $n$ be an integer. Suppose that:

(i) $t$ is $F$-regular (i.e. the homothety of ratio $t$ on $F$ is a monomorphism).

(ii) $R^{i} f_{*}(F)$ is coherent for $i = n - 1$ and $i = n$.

Then the hypothesis of Theorem 1.1 is satisfied.

Indeed, one observes that multiplication by $t^{k}$ defines an isomorphism $F \xrightarrow{\sim} J^{k} F$, and one
deduces that

```text
H^i ≃ R^i f_*(F) ⊗_{𝒪_{X′}} 𝒪_{X′}[T],
```

<!-- label: eq:IX.1.29 -->

where $T$ is an indeterminate. Whence the conclusion.

**Corollary.**

<!-- label: IX.1.3 -->

<!-- original page 106 -->

Suppose that $X' = \operatorname{Spec}(A)$, where $A$ is a noetherian ring separated and complete for the $I$-adic
topology. Suppose that the $S$-module $H^{i}$ is of finite type for $i = n - 1$ and $i = n$ (cf. 1.14 and 1.15). Then
the hypotheses of Theorem 1.1 are satisfied, and one finds a commutative diagram of isomorphisms:

```text
                    ρ′_i
   H^i(X, F)  ─────────────▶  H^i(X̂, F̂)
         \                      /
          \                    /
           \ ϕ′_i         ψ_i /
            \                /
             ▼              ▼
              lim_{k} H^i(X, F_k)              for i = n − 1.
```

<!-- label: eq:IX.1.3.1 -->

<!-- Editorial note: The source labels this diagram "(1.1)" which conflicts with diagram (1.1) above; I label it
eq:IX.1.3.1 to disambiguate, following the SGA 2 numbering convention. -->

[^N.D.E-IX-1]

<!-- original page 84 -->

One simply notes that $H^{i}(X, F)$ is of finite type, hence isomorphic to its completion. One obtains (1.1) by
transcribing the diagram of Modules (1.7) into the category of $A$-modules, and replacing the left vertical by
$H^{i}(X, F)$.

**Proposition.**

<!-- label: IX.1.4 -->

Let $A$ be a noetherian ring. Let $t \in A$ and suppose that $A$ is separated and complete for the `(tA)`-adic topology.
Set:

```text
X′ = Spec(A),    Y′ = V(t),    I = (tA).
```

<!-- label: eq:IX.1.31 -->

Let $T$ be a closed subset of $X'$; set

```text
X = X′ − T,    Y = Y′ ∩ X = Y′ − (Y′ ∩ T).
```

<!-- label: eq:IX.1.32 -->

Let $F$ be a coherent $\mathcal{O}_{X}$-Module. Finally, let

```text
T′ = {x ∈ X′ | codim({x} ∩ T, {x}) = 1}.
```

<!-- label: eq:IX.1.33 -->

Suppose that:

a) $t$ is $F$-regular,

b) $prof_{T'}(F) \geqslant n + 1$,

c) $A$ is a quotient of a regular noetherian ring.

Then, in diagram (1.1), the morphisms $\rho'_{i}$, $\varphi'_{i}$, and $\psi_{i}$ are isomorphisms for $i < n$ and
monomorphisms for $i = n$. Moreover $\psi_{n}$ is an isomorphism.

<!-- original page 107 -->

By virtue of 1.3 and 1.2, it suffices to prove that $R^{i} f_{*}(F)$ is coherent for $i \leqslant n$, which follows from
the finiteness theorem 2.1.[^N.D.E-IX-4]

In particular:

**Example.**

<!-- label: IX.1.5 -->

One will apply 1.4 when $A$ is a local ring and $t$ belongs to the radical $r(A)$ of $A$. One will then take
$T = {r(A)}$. In this case, for $n = 1$, one obtains the following statement:

If $A$ is noetherian, separated and complete for the $t$-adic topology, and a quotient of a regular ring (for example,
if $A$ is complete), if moreover $t$ is $F$-regular and if $prof F_{x} \geqslant 2$ for every
$x \in \operatorname{Spec}(A)$ such that $\dim A/x = 1$, then the natural homomorphism

```text
Γ(X, F) → Γ(X̂, F̂)
```

is an isomorphism.

Indeed, keeping the notation of 1.4, one has $T = {r(A)}$, and formula (1.33) says that

```text
T′ = {x ∈ Spec(A) | dim A/x = 1}.
```

<!-- original page 85 -->

## 2. The existence theorem

<!-- label: IX.2 -->

Let us first state EGA III 3.4.2 in a slightly more general form.

Let $f: X \to X'$ be an adic morphism[^IX-2-star] of formal preschemes, with $X'$ noetherian. Let $I'$ be an ideal of
definition of $X'$; since $f$ is adic, $f*I' = J$ is[^N.D.E-IX-2] an ideal of definition of $X$.

For every $n \in \mathbb{N}$, set

$$
X_{n} = (X, \mathcal{O}_{X}/J^{n+1});
$$

<!-- label: eq:IX.2.1 -->

this is an ordinary prescheme having the same underlying topological space as $X$.

Let $F$ be a coherent $\mathcal{O}_{X}$-Module. For every $k \in \mathbb{N}$, the $\mathcal{O}_{X_{k}}$-Modules

<!-- original page 108 -->

$$
F_{k} = F/J^{k+1} F
$$

<!-- label: eq:IX.2.2 -->

are coherent. For every $i$, one has a homomorphism

```text
ψ_i: R^i f_*(F) → lim_{k} R^i f_*(F_k),
```

<!-- label: eq:IX.2.3 -->

deduced by functoriality from the natural homomorphism:

$$
F \to F_{k}.
$$

<!-- label: eq:IX.2.4 -->

Set

```text
S = gr_{I′} 𝒪_{X′} = ⨁_{k ∈ ℕ} I′^k / I′^{k+1},
```

<!-- label: eq:IX.2.5 -->

```text
gr_J(F) = ⨁_{k ∈ ℕ} J^k F / J^{k+1} F,
```

<!-- label: eq:IX.2.6 -->

```text
K^i = R^i f_*(gr_J(F)) = ⨁_{k ∈ ℕ} R^i f_*(J^k F / J^{k+1} F).
```

<!-- label: eq:IX.2.7 -->

It is clear that $K^{i}$ is equipped with a graded $S$-Module structure.

**Theorem.**

<!-- label: IX.2.1 -->

Suppose that $K^{i}$ is a graded $S$-Module of finite type for $i = n - 1$, $i = n$, $i = n + 1$. Then:

(i) $R^{n} f_{*}(F)$ is coherent.

(ii) The homomorphism $\psi_{n}$ (2.3) is a topological isomorphism. The natural filtration of the right-hand side of
(2.3) is $I'$-good.

(iii) The projective system of the $R^{n} f_{*}(F_{k})$ satisfies the uniform Mittag-Leffler condition.

<!-- original page 109 -->

The proof is very easy from EGA 0_III 13.7.7 (cf. EGA III 3.4.2), provided one corrects the text on page 78 as indicated
in (EGA III 2, Err_III 24).

<!-- original page 86 -->

**Theorem.**

<!-- label: IX.2.2 -->

[^N.D.E-IX-3]

Let $A$ be a noetherian adic ring and let $I$ be an ideal of definition of $A$. Let $T$ be a closed subset of
$X' = \operatorname{Spec}(A)$. Suppose that $I$ is generated by a $t \in A$. Take up the notation 1.31, 1.32, and 1.33.
Let $F$ be a coherent $\mathcal{O}_{\hat{X}}$-Module. Set

$$
F_{0} = F/J F,
$$

<!-- label: eq:IX.2.2.1 -->

where $J = t\mathcal{O}_{\hat{X}}$ is an ideal of definition of $\hat{X}$. Suppose that $A$ is a quotient of a regular
noetherian ring and that:

(1) $t$ is $F$-regular,

(2) $prof_{T'} F_{0} \geqslant 2$.

Then there exists a coherent $\mathcal{O}_{X}$-Module $\tilde{F}$ such that $\tilde{F}^{\wedge} \simeq F$.

<!-- Editorial note: In the source the conclusion is "il existe un O_X-Module cohérent F tel que F̂ ≃ F"; the input
`F` (on `X̂`) and the constructed `F` (on `X`) share the same symbol. To disambiguate the conclusion in English without
altering the mathematics, we write `F̃` for the constructed `𝒪_X`-Module; in the source these are typographically the
same letter. -->

It suffices to prove that $\hat{f}_{*}(F)$ is a coherent $\mathcal{O}_{\hat{X}'}$-Module, where
$\hat{f}: \hat{X} \to \hat{X}'$ is the morphism of formal preschemes deduced from the injection of $X$ into $X'$ by
completion with respect to $t$. Indeed, $A$ is separated and complete for the $t$-adic topology, so there will exist an
$A$-module $F'$ whose completion will be isomorphic to $\hat{f}_{*}(F)$. Since $X$ is an open of $X'$, one will be able
to take $\tilde{F} = \tilde{F}' | X$.

It remains to show that 2.1 is applicable to the morphism of formal preschemes $\hat{f}$ and to $F$. Now, by hypothesis
(1), for every $k \in \mathbb{N}$ one has an isomorphism:

```text
J^k F / J^{k+1} F → F/J F,
```

<!-- original page 110 -->

whence it follows that the hypothesis of 2.1 will be satisfied if one knows that

```text
R^i f_*(F₀) is coherent for i ⩽ 1.
```

Now this follows from (2) and from the finiteness theorem 2.1.[^N.D.E-IX-4] Whence the conclusion.

It remains to specialize this statement by supposing that $A$ is a local ring.

**Corollary.**

<!-- label: IX.2.3 -->

Let $A$ be a noetherian local ring and let $t \in r(A)$ be an element of the radical of $A$. Suppose that $A$ is
separated and complete for the $t$-adic topology and, moreover, a quotient of a regular ring (for example, suppose that
$A$ is a complete noetherian local ring). Set

```text
X′ = Spec A,    T = {r(A)},
```

<!-- label: eq:IX.2.9 -->

<!-- original page 87 -->

and take up the notation (1.31), (1.32), and (1.33). Let $F$ be an $\mathcal{O}_{\hat{X}}$-Module. Suppose that:

(1) $t$ is $F$-regular,

(2) $prof_{T'} F_{0} \geqslant 2$, with $F_{0} = F/J F$ and $J = t\mathcal{O}_{\hat{X}}$.

Then there exists a coherent $\mathcal{O}_{X}$-Module $\tilde{F}$ such that $\tilde{F}^{\wedge} \simeq F$.

Note that here $T'$ is the set of prime ideals $p$ of $A$ such that $\dim A/p = 1$.

<!--
LEDGER DELTA (Exposé IX):

| French | English | Note |
| --- | --- | --- |
| complété formel (de X le long de Y) | formal completion (of X along Y) | Glossary entry. Hat notation `X̂` preserved across OCR breaks. |
| morphisme déduit de f par passage aux complétés | morphism deduced from f by passing to the completions | Standard SGA proof movement. |
| idéal de définition | ideal of definition | Standard. |
| `I′`-bonne (filtration) | `I′`-good (filtration) | Standard EGA terminology for "good filtration"; kept literal. |
| homothétie de rapport t | homothety of ratio t | Standard. |
| F-régulier | F-regular | Per glossary. |
| morphisme adique | adic morphism | Standard EGA term. |
| condition de Mittag-Leffler uniforme | uniform Mittag-Leffler condition | Standard. |
| système projectif essentiellement nul | essentially zero projective system | Standard SGA terminology (cf. Exposé II ledger). |
| théorème de comparaison | comparison theorem | Glossary. |
| théorème d'existence | existence theorem | Glossary. |
| théorème de finitude | finiteness theorem | Glossary; here refers to the Exposé VIII statement (VIII 2.3). |
| anneau noethérien adique | noetherian adic ring | Standard. |
| séparé et complet pour la topologie I-adique | separated and complete for the `I`-adic topology | Standard. |
| préschéma formel | formal prescheme | Standard. |
| Module gradué de type fini | graded Module of finite type | Standard (capital Module preserved per source). |
| anneau gradué associé `gr_I` | associated graded ring `gr_I` | Standard. |
| `S`-Module gradué | graded `S`-Module | Capital preserved per source convention. |
| profondeur (prof_T) | depth (prof_T) | Per SGA 2 glossary entry "profondeur". |
| Or | Now | Pivot conjunction; not "but". |
| À savoir | namely | Standard. |
| D'où la conclusion | Whence the conclusion | Register supports "Whence" in proof closure. |
-->

[^N.D.E-IX-1]: *N.D.E.* In the same vein, see the article by Chow (Chow W.-L., "Formal functions on homogeneous spaces",
    *Invent. Math.* **86** (1986), no. 1, pp. 115–130). The author proves the following result. Let $X$ be an algebraic
    variety over a field, homogeneous under an algebraic group $G$, and let $Z$ be a complete subvariety of $X$ of
    dimension `> 0`. Suppose that $Z$ generates $X$ in the following sense: given $p \in Z$, let $\Gamma_{p}$ be the set
    of elements of $G$ sending $p$ into $Z$. One then says that $Z$ generates if the group generated by the connected
    component of `1` of $\Gamma_{p}$ is the whole of $G$. In this case, every formal rational function on $X$ along $Z$
    is algebraic; compare with the results of Hironaka and Matsumura cited in editor's note (3) p. 138. In the line of
    the techniques introduced by these authors, let us point out the very pretty algebraization result due to Gieseker
    (Gieseker D., "On two theorems of Griffiths about embeddings with ample normal bundle", *Amer. J. Math.* **99**
    (1977), no. 6, pp. 1137–1150, Theorems 4.1 and 4.2). Let $X$ be a connected projective variety of dimension `> 0`,
    locally a complete intersection (over an algebraically closed field). Suppose one has two embeddings of $X$ into
    smooth projective varieties `Y, W`. Then, if the formal completions of $X$ in $Y$ and $W$ are equivalent, there
    exists a scheme $U$ containing $X$ (as a closed subscheme) which embeds into $Y$ and $W$ as an étale neighborhood of
    $X$ in $Y$ and $W$. In other words, formally equivalent entails étale-equivalent. See also the article of Faltings
    (Faltings G., "Formale Geometrie und homogene Räume", *Invent. Math.* **64** (1981), pp. 123–165).

[^N.D.E-IX-4]: *N.D.E.* The "finiteness theorem 2.1" referenced here is the finiteness theorem of Exposé VIII (VIII
    2.3), not the Theorem 2.1 of the present Exposé; the source's local cross-reference is to the
    cohomological finiteness statement on which the existence theorem is built.
        <!-- Editorial note: The source writes "théorème de
    finitude 2.1" but the only Theorem 2.1 in the present Exposé is the existence theorem itself. The intended
    reference is to the Exposé VIII finiteness theorem, which is the "finiteness theorem" referenced in the
    Introduction and at the head of this Exposé. -->

[^IX-2-star]: This hypothesis is not essential; cf. XII, p. 118.

[^N.D.E-IX-2]: *N.D.E.* By definition itself, cf. EGA I 10.12.1.

[^N.D.E-IX-3]: *N.D.E.* Numerous algebraization statements have been obtained since, not to mention those cited below;
    cf. the articles of Faltings or of Mme Raynaud cited in editor's notes (22) p. 155 and (7) p. 203 respectively. One
    has in mind in particular the results of Artin (see notably Artin M., "Algebraization of formal moduli. I", in
    *Global Analysis (Papers in Honor of K. Kodaira)*, Univ. Tokyo Press, Tokyo, 1969, pp. 21–71), but also the recent
    algebraicity results for leaves of foliations; see notably Bost J.-B., "Algebraic leaves of algebraic foliations
    over number fields", *Publ. Math. Inst. Hautes Études Sci.* **93** (2001), pp. 161–221, and Chambert-Loir A.,
    "Théorèmes d'algébricité en géométrie diophantienne (d'après J.-B. Bost, Y. André, D. & G. Chudnovsky)", in
    *Séminaire Bourbaki, Vol. 2000/2001*, *Astérisque*, vol. 282, Société mathématique de France, Paris, 2002, Exp. 886,
    pp. 175–209, and the references cited therein. In particular, one will find in these two articles discussions of the
    link between algebraization questions and the theory of diophantine approximation.


<!-- SOURCE: 10-application-au-groupe-fondamental.md -->

# Exposé X. Application to the fundamental group

<!-- label: X -->

<!-- original page 89 -->

Throughout this Exposé, $X$ will denote a locally noetherian prescheme, $Y$ a closed part of $X$, $U$ a variable open
neighborhood of $Y$ in $X$, and $\hat{X}$ the formal completion of $X$ along $Y$ (EGA I 10.8). For every prescheme $Z$,
we denote by $\hat{E}t(Z)$ the category of étale coverings of $Z$, and by $L(Z)$ the category of locally free coherent
Modules on $Z$.

## 1. Comparison of $\hat{E}t(\hat{X})$ and $\hat{E}t(Y)$

<!-- label: X.1 -->

Let $I$ be an ideal of definition of $Y$ in $X$. Set, for every $n \in \mathbb{N}$,
$Y_{n} = (Y, (\mathcal{O}_{X}/I^{n+1})|Y)$. The $Y_{n}$ form a direct system of ordinary preschemes, or also of formal
preschemes, by equipping the structure sheaves with the discrete topology. One knows (EGA I 10.6.2) that $\hat{X}$ is
the direct limit, in the category of formal preschemes, of the direct system of the $Y_{n}$. One also knows (EGA I
10.13) that to give a formal $\hat{X}$-prescheme of finite type $R$ is the same as to give a direct system of
$Y_{n}$-preschemes $R_{n}$ of finite type, such that $R_{n} \simeq (R_{n+1}) \times_{(Y_{n+1})} (Y_{n})$. Moreover, in
order that $R$ be an étale covering of $\hat{X}$, it is necessary and sufficient that for every $n$, $R_{n}$ be an étale
covering of $Y_{n}$. This said, it is easy to see that nilpotent elements do not matter for étale coverings (SGA 1 8.3),
that is, that the base-change functor

$$
\hat{E}t(Y_{n+1}) \longrightarrow \hat{E}t(Y_{n})
$$

is an equivalence of categories for every $n \in \mathbb{N}$. Hence:

**Proposition.**

<!-- label: X.1.1 -->

With the notation introduced above, the natural functor $\hat{E}t(\hat{X}) \to \hat{E}t(Y)$ is an equivalence of
categories (cf. SGA 1 8.4).

## 2. Comparison of $\hat{E}t(Y)$ and $\hat{E}t(U)$, for $U$ variable

<!-- label: X.2 -->

<!-- original page 90 -->

We shall introduce two conditions from which the announced comparison theorem will follow easily. Let $X$ be a locally
noetherian prescheme and let $Y$ be a closed part of $X$. One says that the pair $(X, Y)$ satisfies the *Lefschetz
condition*, written $Lef(X, Y)$, if, for every open $U$ of $X$ containing $Y$ and every locally free coherent sheaf $E$
on $U$, the natural homomorphism

```text
Γ(U, E) ⟶ Γ(X̂, Ê)
```

is an isomorphism.

One says that the pair $(X, Y)$ satisfies the *effective Lefschetz condition*, written $Leff(X, Y)$, if $Lef(X, Y)$
holds and if, moreover, for every locally free coherent sheaf $E$ on $\hat{X}$, there exist an open neighborhood $U$ of
$Y$, a locally free coherent sheaf $E$ on $U$, and an isomorphism $\hat{E} \simeq E$.

These conditions are satisfied in two important examples:

**Example.**[^N.D.E-X-1]

<!-- label: X.2.1 -->

Let $A$ be a noetherian ring and let $t \in \mathfrak{r}(A)$ be an $A$-regular element belonging to the radical
$\mathfrak{r}(A)$ of $A$. Suppose that $A$ is a quotient of a regular local ring and that $A$ is complete for the
$t$-adic topology (for example $A$ complete for the $\mathfrak{r}(A)$-adic topology). Set $X' = \operatorname{Spec}(A)$
and $Y' = V(t)$; further, set $x = \mathfrak{r}(A)$ and $X = X' - {x}$, $Y = Y' - {x}$. So $X$ is open in $X'$ and
$Y = X \cap Y'$. Then:

1. If, for every prime ideal $\mathfrak{p}$ of $A$ such that $\dim A/\mathfrak{p} = 1$ (i.e. for every closed point of
   $X$), one has $prof A_{\mathfrak{p}} \geqslant 2$, then $Lef(X, Y)$ holds;
1. if, moreover, for every prime ideal $\mathfrak{p}$ of $A$ such that $t \in \mathfrak{p}$ and
   $\dim A/\mathfrak{p} = 1$ (i.e. for every closed point of $Y$), one has $prof A_{\mathfrak{p}} \geqslant 3$, then
   $Leff(X, Y)$ holds.

Let us first show that, for every open neighborhood $U$ of $Y$ in $X$, the complement of $U$ in $X$ is a union of a
finite number of closed points (in $X$). Note that $U$ is open in $X$, hence in $X'$, so $Z' = X' - U$ is closed.

<!-- original page 91 -->

Let $I$ be an ideal of definition of $Z'$; it suffices to prove that $A/I$ is of dimension `1`. But $Z' \cap Y' = {x}$,
so $A/(I + (t))$ is artinian, whence the conclusion by the "Hauptidealsatz".

The first hypothesis is equivalent to: "for every prime ideal $\mathfrak{p}$ of $A$,
$\mathfrak{p} \neq \mathfrak{r}(A)$, one has $prof A_{\mathfrak{p}} \geqslant 3 - \dim A/\mathfrak{p}$". Indeed, $A$ is
a quotient of a regular ring, so one may apply VIII 2.3 to the prescheme $X'$, to the closed part ${x}$, and to the
coherent sheaf $\mathcal{O}_{X'}$, observing that $c(\mathfrak{p}) = \dim(A/\mathfrak{p})$ for
$\mathfrak{p} \in U = X' - {x}$ (since $x$ is the closed point of $X'$).

Let $U$ be an open neighborhood of $Y$ in $X$ and let $E$ be a locally free $\mathcal{O}_{U}$-module. Set $Z = X - U$
and let $u: U \to X$ be the canonical immersion. We shall first prove that $u_{*}(E)$ is a coherent
$\mathcal{O}_{X}$-Module, or what amounts to the same, that $\mathcal{H}^{i}_{Z}(E')$ is coherent for $i = 0, 1$, where
$E'$ is a coherent extension of $E$ to $X$. To do this, one applies Theorem VIII 2.1 to the prescheme $X$, to the closed
part $Z$, and to the coherent sheaf $E'$. It suffices to verify that for every point $\mathfrak{p} \in U$ such that
$c(\mathfrak{p}) = 1$, one has $prof E'_{\mathfrak{p}} \geqslant 1$, where we have set

```text
c(𝔭) = codim({𝔭}̄ ∩ Z, {𝔭}̄).
```

Now if $\mathfrak{p} \in U$ and $c(\mathfrak{p}) = 1$, denoting again by $\mathfrak{p}$ the ideal of $A$ corresponding
to $\mathfrak{p}$, one sees that $\dim A/\mathfrak{p} = 2$, since the complement of $U$ is a union of a finite number of
closed points and $A$ is a quotient of a regular ring. Moreover, $E$ is locally free, so for every
$\mathfrak{p} \in Supp E$ one has $prof E_{\mathfrak{p}} = prof \mathcal{O}_{U,\mathfrak{p}}$. Finally, if
$\mathfrak{p} \in U$ and $c(\mathfrak{p}) = 1$, one has

```text
prof E′_𝔭 = prof E_𝔭 = prof 𝒪_{U,𝔭} = prof A_𝔭 ⩾ 3 − 2 = 1.
```

We must now prove that the natural homomorphism

```text
Γ(U, E) ⟶ Γ(X̂, Ê)
```

<!-- label: eq:X.2.1.1 -->

is an isomorphism. Setting then $\tilde{E} = u_{*}(E)$, one notes that `Ẽ` is coherent and of depth $\geqslant 2$ at
every closed point of $X$. It follows that $R^{i} f_{*}(\tilde{E})$ is coherent for $i = 0, 1$, where $f: X \to X'$
denotes the canonical immersion of $X$ into $X' = \operatorname{Spec}(A)$ (Exp. VIII). One then applies (IX 1.5) and
concludes that

<!-- original page 92 -->

```text
Γ(U, E) ⟶ Γ(X̂, Ê)
```

<!-- label: eq:X.2.1.2 -->

is an isomorphism, since $A$ is complete for the $t$-adic topology. One has a commutative diagram

```text
       Γ(X, Ẽ) ────≃────→ Γ(U, E)
            ╲              ╱
             ╲            ╱
              ≃          ↓
               ╲        ╱
                ↘     ↙
                Γ(X̂, Ê)
```

whence the conclusion.

Now let $E$ be a locally free coherent sheaf on $\hat{X}$. If one has proved that $E$ is algebraizable, i.e. is
isomorphic to the formal completion of a coherent $\mathcal{O}_{X}$-Module `Ẽ`, it is easy to see that `Ẽ` is locally
free in a neighborhood of $Y$, hence to prove $Leff(X, Y)$. Let $\hat{X}'$ be the formal spectrum of $A$ for the
$t$-adic topology, which is identified with the formal completion of $X'$ along $Y'$. Denote by $f$ the canonical
immersion of $X$ in $X'$, by $f'$ the canonical immersion of $Y$ in $Y'$, and by $\hat{f}$ the morphism deduced by
passing to the completions. In order that $E$ be algebraizable, it suffices that $\hat{f}_{*}(E)$ be a coherent
$\mathcal{O}_{\hat{X}'}$-Module, since $A$ is complete for the $t$-adic topology. Let $I = t\mathcal{O}_{\hat{X}}$; this
is an ideal of definition of $\hat{X}$.

For every $n \geqslant 0$, set $E_{n} = E/I^{n+1}E$. At every closed point $y \in Y$, the depth of $E_{0}$ is
$\geqslant 2$; indeed, $t$ is an $A$-regular element, so
$prof \mathcal{O}_{Y_{0},y} = prof \mathcal{O}_{X,y} - 1 \geqslant 2$. One concludes that $\hat{f}_{*}(E)$ is coherent
(IX 2.3). QED.

<!-- original page 92 -->

**Example** (Will allow comparison of the fundamental group of a projective variety and a hyperplane section).

<!-- label: X.2.2 -->

Let $K$ be a field and let $X$ be a proper $K$-prescheme. Let $L$ be an ample invertible $\mathcal{O}_{X}$-Module. Let
$t \in \Gamma(X, L)$ be an $\mathcal{O}_{X}$-regular element, which means that, for every open $U$ and every isomorphism
$u: L|U \to \mathcal{O}_{U}$, $u(t)$ is a non-zero-divisor in $\mathcal{O}_{U}$ (a condition that does not depend on
$u$). Let $Y = V(t)$ be the subscheme of $X$ of equation $t = 0$.[^N.D.E-X-2] Then:

1. If, for every closed point $x$ in $X$, one has $prof \mathcal{O}_{X,x} \geqslant 2$, then $Lef(X, Y)$ holds;
1. if, moreover, for every closed point $y \in Y$ one has $prof \mathcal{O}_{X,y} \geqslant 3$, then $Leff(X, Y)$ holds.

This example will be treated in detail in Exp. XII.

Let $S$ be a prescheme; one knows (EGA II 6.1.2) that the functor which to every finite flat covering $r: R \to S$
associates the $\mathcal{O}_{X}$-Algebra $r_{*}(\mathcal{O}_{R})$ induces an equivalence between the category of finite
flat coverings of $S$ and the category of locally free coherent $\mathcal{O}_{X}$-Algebras. Let $U$ be an open
neighborhood of $Y$, and let $r: R \to U$ be a finite flat covering of $U$. Let $\hat{R}$ be the finite flat covering of
$\hat{X}$ deduced from it by base change. One has
$\hat{r}_{*}(\mathcal{O}_{\hat{R}}) \simeq r_{*}\hat{\mathcal{O}_{R}}$.

Suppose then that $Lef(X, Y)$ holds. This implies that, for every $U$, the inverse image functor

$$
L(U) \longrightarrow L(\hat{X})
$$

is fully faithful. Indeed, let $E$ and $F$ be two locally free coherent $\mathcal{O}_{U}$-Modules;
$\operatorname{Hom}(E, F)$ is also coherent and locally free. By hypothesis the natural map

```text
Γ_U(Hom(E, F)) ⟶ Γ_{X̂}(Hom(E, F)̂)
```

is an isomorphism, whence the conclusion, since `Hom` commutes with `̂` since everything is locally free. Now the `̂`
commutes with the tensor product, from which one deduces that the functor which to every locally free coherent
$\mathcal{O}_{U}$-Algebra $A$ associates the $\mathcal{O}_{\hat{X}}$-Algebra `Â` is fully faithful. Better, if $E$ is a
locally free coherent $\mathcal{O}_{U}$-Module, there is a bijective correspondence between the commutative
$\mathcal{O}_{\hat{X}}$-Algebra structures on `Ê`.

<!-- original page 92 (continued) -->

**Proposition.**

<!-- label: X.2.3 -->

Let $X$ be a locally noetherian prescheme and let $Y$ be a closed part of $X$. Let $\hat{X}$ be the formal completion of
$X$ along $Y$. For every open $U$ of $X$, $U \supset Y$, denote by `L_U` (resp. `P_U`, resp. `E_U`) the functor which to
every locally free coherent $\mathcal{O}_{U}$-Module (resp. every finite flat covering of $U$, resp. every étale
covering of $U$) associates its inverse image by $\hat{X} \to X$.

1. If $Lef(X, Y)$ holds, then for every open neighborhood $U$ of $Y$, the functors `L_U`, `P_U`, and `E_U` are fully
   faithful.

<!-- original page 93 -->

1. If $Leff(X, Y)$ holds, then for every locally free coherent $\mathcal{O}_{\hat{X}}$-Module $E$ (resp. ...), there
   exist an open $U$ and a locally free coherent $\mathcal{O}_{U}$-Module `Ẽ` (resp. ...), such that
   $L_{U}(\tilde{E}) \simeq E$ (resp. ...).

(i) Has been seen.

(ii) Follows from (i) and from the hypothesis, at least for `L_U` and `P_U`. Moreover, if $R$ is an étale covering of
$\hat{X}$, there exist an open neighborhood $U$ of $Y$ in $X$ and a finite flat covering $R'$ of $U$ such that
$\hat{R}' \simeq R$. From it one deduces a covering $R''$ of $Y$ which is étale by 1.1, so $R'$ is étale in a
neighborhood $U'$ of $Y$. QED.

**Corollary.**

<!-- label: X.2.4 -->

If $Lef(X, Y)$ holds, then in order that a finite flat covering $R$ of an open neighborhood $U$ of $Y$ be connected, it
is necessary and sufficient that $R \times_{U} \hat{X}$ be connected. In particular, in order that $Y$ be connected, it
is necessary and sufficient that the open neighborhood $U$ of $Y$ be connected, or again that $\hat{X}$ be connected.

Indeed, in order that a ringed space in local rings $(X, \mathcal{O}_{X})$ be connected, it is necessary and sufficient
that $\Gamma(X, \mathcal{O}_{X})$ not be a direct product of two non-zero rings. Now one has

```text
Γ(U, r_*(𝒪_R)) ≃ Γ(X̂, r̂_*(𝒪_{R̂}))
```

by $Lef(X, Y)$.

**Corollary.**

<!-- label: X.2.5 -->

If $Lef(X, Y)$ holds, then for every $U$, the functor

$$
\hat{E}t(U) \longrightarrow \hat{E}t(Y)
$$

is fully faithful. If $Leff(X, Y)$ holds, then for every étale covering $R$ of $Y$, there exist an open neighborhood $U$
of $Y$ and a covering $R'$ of $U$ such that $R' \times_{U} Y \simeq R$.

**Corollary.**[^N.D.E-X-3]

<!-- label: X.2.6 -->

If $Lef(X, Y)$ holds and $Y$ is connected, then every open neighborhood $U$ of $Y$ is connected and the natural
homomorphism $\pi_{1}(Y) \to \pi_{1}(U)$ is surjective. If, moreover, $Leff(X, Y)$ holds, the natural homomorphism

```text
π₁(Y) ⟶ lim_{←, U} π₁(U)
```

is an isomorphism. (N.B. One assumes that a "base-point" has been chosen in $Y$, which one also takes as base-point in
$X$, for the definition of the fundamental groups.)

All of this follows trivially from Proposition 1.1 and Proposition 2.3.

<!-- original page 94 -->

## 3. Comparison of $\pi_{1}(X)$ and $\pi_{1}(U)$

<!-- label: X.3 -->

**Definition.**

<!-- label: X.3.1 -->

Let $X$ be a prescheme and $Z$ a closed part of $X$. Set $U = X - Z$. One says that the pair $(X, Z)$ is *pure* if, for
every open $V$ of $X$, the functor

```text
Êt(V) ⟶ Êt(V ∩ U)
V′ ↦ V′ ×_V (V ∩ U)
```

is an equivalence of categories.[^X-3-pur-star]

**Definition.**

<!-- label: X.3.2 -->

<!-- original page 94 (continued) -->

Let $A$ be a noetherian local ring. Set $X = \operatorname{Spec} A$. Let $\mathfrak{r}(A)$ be the radical of $A$ and let
$x = \mathfrak{r}(A)$ be the closed point of $X$. One says that $A$ is *pure* if the pair `(X, {x})` is.

We leave to the reader the task of not proving the following proposition:

**Proposition.**

<!-- label: X.3.3 -->

Let $X$ be a locally noetherian prescheme and let $Z$ be a closed part of $X$. In order that the pair $(X, Z)$ be pure
it is necessary and sufficient that, for every $z \in Z$, the ring $\mathcal{O}_{X,z}$ be pure.[^X-3-pur-starstar]

This said, the following theorem is the essential result of this number:

**Theorem** (Purity theorem).[^N.D.E-X-4]

<!-- label: X.3.4 -->

1. A regular noetherian local ring of dimension $\geqslant 2$ is pure (Zariski–Nagata purity theorem).
1. A noetherian local ring of dimension $\geqslant 3$ which is a complete intersection is pure.

<!-- original page 95 -->

Recall that one says that a local ring is a *complete intersection* if there exist a regular noetherian local ring $B$
and a $B$-regular sequence $(t_{1}, \cdots, t_{k})$ of elements of the radical $\mathfrak{r}(B)$ of $B$ such that

$$
A \simeq B/(t_{1}, \cdots, t_{k}).
$$

In this connection, let us remark that it would be less ambiguous to say that $A$ is an *absolute* complete
intersection, by opposition with the situation, already encountered, in which $X$ is a locally noetherian prescheme
(which need not be regular) and $Y$ is a closed part of $X$, of which one says that it is "locally set-theoretically a
complete intersection in $X$".

Let us first prove a few lemmas.

**Lemma.**

<!-- label: X.3.5 -->

Let $X$ be a locally noetherian prescheme and let $U$ be an open part of $X$. Set $Z = X - U$. Let $i: U \to X$ be the
canonical immersion of $U$ into $X$. The following conditions are equivalent:

1. For every open $V$ of $X$, if one sets $V' = V \cap U$, the functor $F \mapsto F|V'$ from the category of locally
   free coherent $\mathcal{O}_{V}$-Modules to the category of locally free coherent $\mathcal{O}_{V'}$-Modules is fully
   faithful;
1. the natural homomorphism $\mathcal{O}_{X} \to i_{*}(\mathcal{O}_{U})$ is an isomorphism;
1. for every $z \in Z$, one has $prof \mathcal{O}_{X,z} \geqslant 2$.

One has already seen (III 3.3) the equivalence of (ii) and (iii). Let us show that (ii) implies (i). Let $F$ and $G$ be
two locally free coherent $\mathcal{O}_{V}$-Modules; $\operatorname{Hom}(F, G)$ is also one, so
$\operatorname{Hom}(F, G) \to i_{*}(\operatorname{Hom}(F|V', G|V'))$ is an isomorphism, so
$\operatorname{Hom}(F, G) \simeq \operatorname{Hom}(F|V', G|V')$. Conversely, one takes $F = G = \mathcal{O}_{X}$ and
applies (i) to every open $V$ of $X$.

Here is a useful "descent lemma":

**Lemma.**

<!-- label: X.3.6 -->

Let $X$ be a locally noetherian prescheme and let $Z$ be a closed part of $X$. Set $U = X - Z$. Suppose that the
homomorphism $\mathcal{O}_{X} \to i_{*}(\mathcal{O}_{U})$ is an isomorphism. Let $f: X_{1} \to X$ be a faithfully flat
and quasi-compact morphism. Set $Z_{1} = f^{-1}(Z)$. If the pair $(X_{1}, Z_{1})$ is pure, then so is $(X, Z)$.

Note that the hypothesis $\mathcal{O}_{X} \simeq i_{*}(\mathcal{O}_{U})$ is preserved by flat extension of the base,
since $i$ is a quasi-compact morphism and, in that case, direct image commutes with inverse image. Now this hypothesis
implies that the functor

$$
\hat{E}t(V) \longrightarrow \hat{E}t(U \cap V)
$$

defined by

```text
V′ ↦ V′ ×_V (V ∩ U)
```

is fully faithful, as shown by the interpretation of an étale covering in terms of locally free coherent Algebras. It
remains to prove effectivity.

<!-- original page 95 (continued) -->

One can, for example, introduce the square $X_{2}$ and the cube $X_{3}$ of $X_{1}$ over $X$ and observe that a
faithfully flat and quasi-compact morphism is a morphism of universal effective descent for the fibered category of
étale coverings, above the category of preschemes. The conclusion is formal from there.[^X-3-giraud-star]

**Remark.**

<!-- label: X.3.7 -->

<!-- original page 96 -->

We have shown in passing that if $\mathcal{O}_{X} \to i_{*}(\mathcal{O}_{U})$ is an isomorphism, then $X$ is connected
if and only if $U$ is, and then $\pi_{1}(U) \to \pi_{1}(X)$ is surjective.

**Corollary.**

<!-- label: X.3.8 -->

Let $A$ be a noetherian local ring. Suppose that $prof A \geqslant 2$. Then if `Â` is pure, $A$ is pure.

Follows from Lemma 3.5 and Lemma 3.6.

The following lemma is the essential point in the proof of the purity theorem:

**Lemma.**

<!-- label: X.3.9 -->

Let $A$ be a noetherian local ring and let $t \in \mathfrak{r}(A)$ be an $A$-regular element. Suppose that $A$ is
complete for the $t$-adic topology and is, moreover, a quotient of a regular local ring (for example $A$ complete). Set
$B = A/tA$.

1. If for every prime ideal $\mathfrak{p}$ of $A$ such that $\dim A/\mathfrak{p} = 1$, one has
   $prof A_{\mathfrak{p}} \geqslant 2$, then $B$ pure implies $A$ pure.
1. If for every prime ideal $\mathfrak{p}$ of $A$ such that $\dim A/\mathfrak{p} = 1$, one has
   $prof A_{\mathfrak{p}} \geqslant 2$, if $A_{\mathfrak{p}}$ is pure when $t \notin \mathfrak{p}$, and if[^N.D.E-X-5]
   $prof A_{\mathfrak{p}} \geqslant 3$ when $t \in \mathfrak{p}$, then $A$ pure implies $B$ pure.

Let $X' = \operatorname{Spec}(A)$ and $Y' = V(t)$, which one identifies with the spectrum of $B$. Let
$x = \mathfrak{r}(A)$, and set $X = X' - {x}$ and $Y = Y' - {x} = X \cap Y'$. Denote by $\hat{X}'$ the formal spectrum
of $A$ for the $t$-adic topology, which is identified with the formal completion of $X'$ along $Y'$.

Since $A$ is complete for the $t$-adic topology, one notes that $\hat{E}t(X') \to \hat{E}t(\hat{X}')$ is an equivalence
of categories. Likewise $\hat{E}t(\hat{X}') \to \hat{E}t(Y')$ by Proposition 1.1, so $\hat{E}t(X') \to \hat{E}t(Y')$ is
an equivalence of categories.

<!-- original page 97 -->

Let us show (i). Consider the diagrams

```text
   X′  ←──  X                    Êt(X′)  ──a──→  Êt(X)
   ↑        ↑                       │              │
   │        │                       c              b
   │        │                       ↓              ↓
   Y′  ←──  Y                    Êt(Y′)  ──d──→  Êt(Y)
```

We have just seen that $c$ is an equivalence; $d$ is also one by the hypothesis that $B$ is pure; and finally $b$ is
fully faithful as seen in Example 2.1, cf. 2.3 (i).

Let us show (ii). This time one assumes that $A$ is pure, so $a$ is an equivalence; likewise $c$. Let us see that $b$ is
an equivalence. By Example 2.1 we know that $Leff(X, Y)$ holds, so $b$ is already fully faithful; let us prove that it
is essentially surjective. One uses 2.3 (ii), noting that if $U$ is an open neighborhood of $Y$ in $X$, the complement
of $U$ in $X$ is a union of a finite number of closed points; the pair $(X, X - U)$ is thus pure by Proposition 3.3,
since at such a point $\mathfrak{p}$, $\mathcal{O}_{X,\mathfrak{p}} = A_{\mathfrak{p}}$ is pure by hypothesis. Whence
the conclusion.

**Proof of the purity theorem.**

Let us first prove (i) by induction on the dimension. Let $A$ be a noetherian local ring of dimension `2`. Set
$X' = \operatorname{Spec}(A)$, $x = \mathfrak{r}(A)$, $X = X' - {x}$. One has $prof A = 2$. One may therefore apply
Lemma 3.5 to the pair $(X', {x})$, and so $\hat{E}t(X') \to \hat{E}t(X)$ is fully faithful. Let now $r: R \to X$ be an
étale covering defined by a locally free coherent and étale $\mathcal{O}_{X}$-Algebra $A = r_{*}(\mathcal{O}_{R})$.
Denote by $i: X \to X'$ the canonical immersion of $X$ into $X'$. I claim that $i_{*}(A) = B$ is a coherent
$\mathcal{O}_{X'}$-Algebra. Indeed, it suffices to apply the "finiteness theorem" VIII 2.3. I claim that this algebra is
of depth $\geqslant 2$ at $x$. Indeed, it is the direct image of an $\mathcal{O}_{X}$-Module, with $X = X' - {x}$. Since
$A$ is a regular ring of dimension `2`, one has $dp B + prof B = \dim A = 2$, where `dp B` denotes the projective
dimension of $B$. So $dp B = 0$, hence $B$ is projective, hence free. It follows that $B$ defines a finite flat covering
of $X' = \operatorname{Spec}(A)$. The set of points of $X'$ where this covering is not étale is a closed part of $X'$
whose equation is a principal ideal: the discriminant ideal of $B/A$. Now, by construction, this closed set is contained
in $x = \mathfrak{r}(A)$, hence is empty since $\dim A = 2$.

<!-- original page 97 (continued) -->

Let $A$ be a regular noetherian local ring, $\dim A = n \geqslant 3$. Suppose (i) proved for rings of dimension $< n$.
To prove that $A$ is pure, one may assume $A$ complete by 3.8. Let $t \in \mathfrak{r}(A)$ whose image in
$\mathfrak{r}(A)/\mathfrak{r}(A)^{2}$ is nonzero. Then $B = A/tA$ is a regular noetherian local ring of dimension
$n - 1$, hence is pure, since $n - 1 \geqslant 2$. One concludes by Lemma 3.9 (i), which is applicable since $A$ is
complete.

Let us show (ii). Let $A$ be a noetherian local ring of dimension $\geqslant 3$. Suppose that there exist a regular
noetherian local ring $B$ and a $B$-sequence $(t_{1}, \cdots, t_{k})$ such that $A \simeq B/(t_{1}, \cdots, t_{k})$. Let
us prove that $A$ is pure, by induction on $k$. If $k = 0$, one knows it by (i). Suppose $k \geqslant 1$ and the result
acquired for $k' < k$. By Corollary 3.8[^TRANSLATOR-X-1] one may assume that $A$ (hence also $B$) is complete. Set
$C = B/(t_{1}, \cdots, t_{k-1})$, so $A \simeq C/t_{k} C$ and $t_{k}$ is $C$-regular. By the induction hypothesis one
knows that $C$ is pure; it suffices to prove that Lemma 3.9 (ii) is applicable. Notation: the $A$ and $B$ of the lemma
become $C$ and $A$. One has $\dim C \geqslant 4$, so for every prime ideal $\mathfrak{p}$ of $C$ such that
$\dim C/\mathfrak{p} = 1$, one has $prof C_{\mathfrak{p}} \geqslant 3$. Moreover, $C_{\mathfrak{p}}$ is a complete
intersection with $k' \leqslant k - 1$, hence is pure by the induction hypothesis. QED.

**Theorem.**

<!-- label: X.3.10 -->

<!-- original page 97 (continued) -->

Let $X$ be a locally noetherian prescheme and let $Y$ be a closed part of $X$. Suppose that one has $Leff(X, Y)$ (cf.
Examples 2.1 and 2.2). Suppose moreover that, for every open neighborhood $U$ of $Y$ and every $x \in X - U$, the local
ring $\mathcal{O}_{X,x}$ is regular of dimension $\geqslant 2$ or a complete intersection of dimension $\geqslant 3$.
Then

$$
\pi_{0}(Y) \longrightarrow \pi_{0}(X)
$$

<!-- original page 98 -->

is a bijection, and if $X$ is connected

$$
\pi_{1}(Y) \longrightarrow \pi_{1}(X)
$$

is an isomorphism.

There is nothing more to prove. One remarks that, in the two examples cited 2.1 and 2.2, the complement of $U$ is a
union of a finite number of closed points, from which it follows that the hypothesis on the dimension of
$\mathcal{O}_{X,x}$ is not a farce.

<!--
LEDGER DELTA (Exposé X):

| French | English | Note |
| --- | --- | --- |
| revêtement étale | étale covering | Per SGA 1 glossary. |
| Module cohérent localement libre | locally free coherent Module | Capital `M` preserved per SGA capitalisation. |
| complété formel (de X le long de Y) | formal completion (of X along Y) | Standard; hat `X̂` preserved. |
| condition de Lefschetz / Lefschetz effective | Lefschetz condition / effective Lefschetz condition | `Lef(X, Y)` / `Leff(X, Y)` notation preserved. |
| couple pur de préschémas | pure pair of preschemes | Per glossary; rendered "the pair `(X, Z)` is pure". |
| anneau local pur | pure local ring | Per glossary. |
| théorème de pureté de Zariski-Nagata | Zariski–Nagata purity theorem | Central local result X 3.4. |
| anneau régulier (local noethérien) | regular (noetherian local) ring | Standard. |
| intersection complète (absolue) | (absolute) complete intersection | Grothendieck's qualifier "absolue" preserved. |
| suite B-régulière | B-regular sequence | Standard. |
| Hauptidealsatz | Hauptidealsatz | Kept as Krull's principal-ideal theorem name. |
| algébrisable | algebraizable | Standard formal-geometry term. |
| canularesque | a farce / farcical | Grothendieck slang; preserves the joking register of "canularesque" (from "canular", hoax/joke). |
| Je dis que … | I claim that … | Preserve the first-person move. |
| « point-base » | "base-point" | Preserved with quotes. |
| Nous laissons au lecteur le soin de ne pas démontrer | We leave to the reader the task of not proving | Grothendieck's joke about the obviousness of 3.3; preserve literally. |
| morphisme fidèlement plat et quasi-compact | faithfully flat and quasi-compact morphism | Standard. |
| descente effective universelle | universal effective descent | Standard. |
| dimension projective (dp) | projective dimension (dp) | Auslander–Buchsbaum formula context. |
| idéal discriminant | discriminant ideal | Standard. |
| dim A/𝔭 = 1 (point fermé) | closed point | French phrase "i.e. pour tout point fermé" preserved. |
| 𝔯(A) | 𝔯(A) | Radical of `A`; preserve fraktur. |
-->

[^N.D.E-X-1]: *N.D.E.* One can slightly improve (i): see Mme Raynaud (Raynaud M., "Théorèmes de Lefschetz en cohomologie
    des faisceaux cohérents et en cohomologie étale. Application au groupe fondamental", *Ann. Sci. Éc. Norm. Sup.* (4)
    **7** (1974), pp. 29–52, corollaries I.1.4 and I.5); the condition (ii) can be improved so as to get rid of the
    depth conditions along $Y$ (see Theorem 3.3 of loc. cit. for a precise statement). The proof of this last point is
    very technical, the article cited above giving only indications of proof and referring to a detailed earlier version
    published in the *Bulletin de la Société mathématique de France*.

[^N.D.E-X-2]: *N.D.E.* Condition (ii) is superfluous; see footnote on page 90.

[^N.D.E-X-3]: *N.D.E.* Joined with 3.3 and the criteria 2.4 and 3.4, one obtains the following relative Lefschetz
    theorem. Let $f: X \to S$ be a projective flat morphism of connected noetherian schemes and let $D$ be an effective
    relative Cartier divisor in $X$ which is relatively ample. If, for every $s \in S$, the depth of $X_{s}$ at each
    closed point is $\geqslant 2$, then $D$ is connected and, for every open $U$ of $X$ containing $D$, the arrow
    $i_{U}: \pi_{1}(D) \to \pi_{1}(U)$ is surjective. If, moreover, the depth of $X_{s}$ along each closed point of
    $D_{s}$ is $\geqslant 3$, and if the local rings of $X$ at its closed points are pure — for example, complete
    intersections (cf. X 3.4) — then $i_{X}$ is an isomorphism. Cf. Bost J.-B., "Lefschetz theorem for Arithmetic
    Surfaces", *Ann. Sci. Éc. Norm. Sup.* (4) **32** (1999), pp. 241–312, Theorems 1.1 and 2.1. In the case where $X$ is
    simply a smooth and geometrically connected projective surface over a field, connectedness of $D$ and surjectivity
    of $\pi_{1}(D) \to \pi_{1}(U)$ (where $U$ is an open containing $D$) always hold for $D$ only nef of square `> 0`
    (cf. loc. cit., Theorem 2.3 and also Theorem 2.4 for surfaces only normal and complete). In the case of an
    arithmetic surface (normal and quasi-projective) $X$ over a ring of integers $\mathcal{O}_{K}$, Bost, improving on
    results of Ihara (Ihara Y., "Horizontal divisors on arithmetic surfaces associated with Belyĭ uniformizations", in
    *The Grothendieck theory of dessins d'enfants* (Luminy, 1993), London Math. Soc. Lect. Note Series, vol. 200,
    Cambridge Univ. Press, Cambridge, 1994, pp. 245–254 or loc. cit., corollary 7.2), has shown that if a point
    $P \in X(\mathcal{O}_{K})$, playing the role of the divisor $D$ in the geometric situation, satisfies certain
    positivity conditions, then the arrow $\pi_{1}(X) \to \pi_{1}(\operatorname{Spec} \mathcal{O}_{K})$ deduced from the
    projection was invertible with inverse the arrow $\pi_{1}(\operatorname{Spec} \mathcal{O}_{K}) \to \pi_{1}(X)$
    deduced from $P$ (loc. cit., Theorem 1.2).

[^X-3-pur-star]: For a more satisfactory notion in some respects, cf. the commentary XIV 1.6 d).

[^X-3-pur-starstar]: Compare with the non-commutative case of XIV 1.8, whose proof is essentially the same as that of
    3.3.

[^N.D.E-X-4]: *N.D.E.* For the history of the methods employed, see Grothendieck's letter of October 1, 1961 to Serre,
    *Correspondance Grothendieck–Serre*, edited by Pierre Colmez and Jean-Pierre Serre, Documents Mathématiques, vol. 2,
    Société Mathématique de France, Paris, 2001.

[^X-3-giraud-star]: Cf. J. Giraud, *Méthode de la descente*, Mémoire no. 2 du Bulletin de la Société Mathématique de
    France (1964).

[^N.D.E-X-5]: *N.D.E.* This last condition can be improved, cf. the editor's note (1) on page 90.

[^TRANSLATOR-X-1]:
    <!-- Editorial note: The French source reads "D'après le corollaire 3.9", but the result invoked
    is Corollary 3.8 (the reduction to the complete case via `Â`). Lemma 3.9 itself is applied in the next sentence.
    The reference has been silently corrected here; the original numbering anomaly is preserved as a translator
    note. -->


<!-- SOURCE: 11-application-au-groupe-de-picard.md -->

# Exposé XI. Application to the Picard group

<!-- label: XI -->

<!-- original page 99 -->

This Exposé is modeled on the preceding one, but this time the result of no. 1 is weaker.

Throughout this Exposé, $X$ will denote a locally noetherian prescheme, $I$ a quasi-coherent ideal of `O_X` (so that
$Y = V(I)$ is a closed part of $X$), $U$ a variable open neighborhood of $Y$ in $X$, and $\hat{X}$ the formal completion
of $X$ along $Y$. For every ringed space $(Z, O_{Z})$, we denote by $P(Z)$ the category of invertible `O_Z`-Modules — in
other words, locally free of rank 1 — and by $\operatorname{Pic}(Z)$ the group of isomorphism classes of invertible
Modules on $Z$.

<!-- original page 100 -->

## 1. Comparison of Pic(X̂) and Pic(Y)

<!-- label: XI.1 -->

For every $n \in \mathbb{N}$, set $X_{n} = (Y, O_{X}/I^{n+1})$ and $P_{n} = I^{n+1}/I^{n+2}$. The sequence of sheaves of
abelian groups on $Y$

```text
0 ⟶ P_n ──u──→ O*_{X_{n+1}} ──v──→ O*_{X_n} ⟶ 1
```

<!-- label: eq:XI.1.1 -->

is exact. Let us be precise: the group structure on $P_{n}$ is the additive structure, $u(x) = 1 + x$ for every
$x \in P_{n}$, and $v$ is the homomorphism deduced from the injection $I^{n+2} \to I^{n+1}$. We see that $v$ is
surjective by remarking that, for every $y \in Y$, $O_{X_{n}, y}$ is a local ring, the quotient of $O_{X_{n+1}, y}$ by a
nilpotent ideal; the rest is equally trivial. From (1.1) we deduce an exact cohomology sequence:

```text
(∗)   H¹(Y, P_n) ──u¹──→ H¹(Y, O*_{X_{n+1}}) ──v¹──→ H¹(Y, O*_{X_n}) ──d──→ H²(Y, P_n).
```

<!-- label: eq:XI.1.star -->

On the other hand, for every $n \in \mathbb{N}$, one knows how to identify $\operatorname{Pic}(X_{n})$ with
$H^{1}(Y, O*_{X_{n}})$; moreover, if $E$ is an invertible $O_{X_{n+1}}$-Module corresponding to a cohomology class
$c(E)$, the cohomology class corresponding to the inverse image of $E$ on $X_{n}$ is equal to $v^{1}(c(E))$.

<!-- original page 101 -->

Whence the following proposition:

**Proposition.**

<!-- label: XI.1.1 -->

Retain the notations introduced above. Let $p \in \mathbb{N}$. The map
$\operatorname{Pic}(\hat{X}) \to \operatorname{Pic}(Y_{n})$:

1. is injective for $n \geqslant p$, if $H^{1}(Y, P_{n}) = 0$ for $n \geqslant p$;
1. is an isomorphism for $n \geqslant p$, if $H^{i}(Y, P_{n}) = 0$ for $n \geqslant p$ and $i = 1, 2$.

Of course, the exact sequence (∗) contains more information than the proposition above. The reader will have noticed
that we have said nothing about the functor $P(\hat{X}) \to P(Y)$. Given two invertible $O_{\hat{X}}$-Modules $E$, $F$,
the sheaf $H = \operatorname{Hom}(E, F)$ is also invertible. If we indicate reduction modulo $I^{n+1}$ by a subscript
$n$, we find an exact sequence:

```text
0 ⟶ H_0 ⊗ P_n ⟶ Hom(E_{n+1}, F_{n+1}) ⟶ Hom(E_n, F_n) ⟶ 0.
```

<!-- label: eq:XI.1.2 -->

Whence an exact cohomology sequence that we shall not write down and whose interpretation is evident; one may use this
remark to study the functor $P$.

## 2. Comparison of Pic(X) and Pic(X̂)

<!-- label: XI.2 -->

The reader will find in Exposé X, no. 2, the proof of what follows:

**Proposition.**

<!-- label: XI.2.1 -->

Suppose that $Lef(X, Y)$ holds; then for every open neighborhood $U$ of $Y$ in $X$, the functor

$$
P(U) \longrightarrow P(\hat{X})
$$

<!-- label: eq:XI.2.1 -->

is fully faithful, so that the map

$$
\operatorname{Pic}(U) \longrightarrow \operatorname{Pic}(\hat{X})
$$

<!-- label: eq:XI.2.2 -->

<!-- original page 102 -->

is injective. If $Leff(X, Y)$ holds, then the map (2.3) is an isomorphism:

```text
lim→_U Pic(U) ⟶ Pic(X̂).
```

<!-- label: eq:XI.2.3 -->

**Corollary.**

<!-- label: XI.2.2 -->

Suppose that $Lef(X, Y)$ holds and that $H^{1}(Y, P_{n}) = 0$ for every integer $n \geqslant p$; then for every open
$U \supset Y$, the maps

```text
Pic(X) ⟶ Pic(U) ⟶ Pic(Y_n)
```

are injective for $n \geqslant p$. If $Leff(X, Y)$ holds and if, moreover, $H^{i}(Y, P_{n}) = 0$ for every integer
$n \geqslant p$ and $i = 1, 2$, then the map

```text
lim→_U Pic(U) ⟶ Pic(Y_n)
```

is an isomorphism for $n \geqslant p$.

<!-- original page 103 -->

## 3. Comparison of P(X) and P(U)

<!-- label: XI.3 -->

A definition:

**Definition.** [^XI-3-star1]

<!-- label: XI.3.1 -->

Let $X$ be a prescheme and let $Z$ be a closed part of $X$. Set $U = X - Z$. We say that $X$ is *parafactorial at the
points of* $Z$ if, for every open set $V$ of $X$, the functor $P(V) \to P(V \cap U)$ is an equivalence of categories. We
also say that the pair $(X, Z)$ is *parafactorial*.

Recall that $P(Z)$ denotes the category of Modules locally free of rank 1 on $Z$.

**Definition.**

<!-- label: XI.3.2 -->

A noetherian local ring is said to be *parafactorial* if the pair $(\operatorname{Spec}(A), {r(A)})$ is parafactorial.

One proves the following proposition, which shows that the notion is "pointwise":

**Proposition.**

<!-- label: XI.3.3 -->

Suppose $X$ is locally noetherian. In order that the pair $(X, Z)$ be parafactorial, it is necessary and sufficient
that, for every $z \in Z$, the local ring $O_{X,z}$ be so.

Note that in "parafactorial" there is "fully faithful". One proves, as in Lemma 3.5 of Exposé X, the:

**Lemma.**

<!-- label: XI.3.4 -->

If $X$ is a locally noetherian prescheme and if $Z = X - U$ is a closed part of $X$, the following conditions are
equivalent:

1. for every open set $V$ of $X$, the functor $P(V) \to P(V \cap U)$ is fully faithful;
1. the homomorphism $O_{X} \to i_{*}(O_{U})$ is an isomorphism;
1. for every $z \in Z$, one has $prof(O_{X,z}) \geqslant 2$.

Thus "parafactorial" means that the conditions of 3.4 are satisfied and that, for every open set $V$ of $X$, the
homomorphism $\operatorname{Pic}(V) \to \operatorname{Pic}(V \cap U)$ is surjective. In particular, if $X$ is the
spectrum of a noetherian local ring, we find:

**Proposition.**

<!-- label: XI.3.5 -->

Let $A$ be a noetherian local ring; in order that it be parafactorial, it is necessary and sufficient that
$prof A \geqslant 2$ and $\operatorname{Pic}(X' - {x}) = 0$, where we have set $X' = \operatorname{Spec}(A)$ and $x$ is
the unique closed point of $X'$.

Note that a local ring of dimension $\leqslant 1$ is never parafactorial, since its depth is $\leqslant 1$. Hence
"factorial" does not imply "parafactorial"; however, the converse holds for noetherian local rings of dimension
$\geqslant 2$, as we shall see below.

<!-- original page 104 -->

**Lemma.**

<!-- label: XI.3.6 -->

Let $X$ be a locally noetherian prescheme and let $Z$ be a closed part of $X$. Let $f: X_{1} \to X$ be a faithfully flat
and quasi-compact morphism. Set $Z_{1} = f^{-1}(Z)$. If $(X_{1}, Z_{1})$ is parafactorial, then so is $(X, Z)$.

We first remark that, if $i: (X - Z) \to X$ denotes the canonical immersion of $U = X - Z$ into $X$, the formation of
the direct image by $i$ of a quasi-coherent `O_U`-Module commutes with the base change $f$, since the latter is flat. It
is therefore equivalent to assume the equivalent conditions of Lemma 3.5 for $(X, Z)$ or for $(X_{1}, Z_{1})$, since $f$
is a morphism of descent for the category of quasi-coherent sheaves. It remains to prove that, for every open set $V$ of
$X$, $\operatorname{Pic}(V) \to \operatorname{Pic}(V \cap U)$ is surjective. We make the base change $V \to X$, which
changes nothing (*sic*), and we are reduced to the case $V = X$. We then remark that, if $L$ is an invertible
`O_U`-Module and if $L$ admits a locally free prolongation, this prolongation is isomorphic to $i_{*}(L)$, because of
what has just been seen. It remains to prove that $i_{*}(L)$ is invertible. Using once more the fact that the direct
image by $i$ commutes with flat base change, and that "locally free of rank 1" is a property that descends by faithfully
flat and quasi-compact morphism, we are done.

**Corollary.**

<!-- label: XI.3.7 -->

Let $A$ be a noetherian local ring; if `Â` is parafactorial, so is $A$.

Do not believe that, if $A$ is parafactorial, so is `Â`.[^N.D.E-XI-1]

Before stating the principal theorem of this section, let us make the connection with the theory of divisors and the
notion of factorial ring.[^XI-3-star2]

Let $X$ be a noetherian and normal prescheme. Let $Z^{1}(X)$ be the free abelian group generated by the $x \in X$ such
that $\dim O_{X,x} = 1$. The local ring of such a point is a discrete valuation ring. We shall write $v_{x}$ for the
corresponding normalized valuation. Let $K(X)$ be the ring of rational functions on $X$ and let

$$
p: K(X)* \longrightarrow Z^{1}(X)
$$

be the map that to every $f \in K(X)*$ associates the codimension-one cycle:

```text
(f) = Σ_{x ∈ X, dim O_{X,x} = 1} v_x(f) · x.
```

<!-- original page 105 -->

The image of $p$ is denoted $P(X)$, and its elements are called *principal divisors*.[^XI-3-star3] We set

$$
Cl(X) = Z^{1}(X)/P(X).
$$

Let $Z'^{1}(X)$ be the subgroup of $Z^{1}(X)$ whose elements are the locally principal divisors. One knows that

$$
\operatorname{Pic}(X) \simeq Z'^{1}(X)/P(X),
$$

and consequently $\operatorname{Pic}(X)$ is identified with a subgroup of $Cl(X)$.

Note that if $U$ is a dense open of $X$, then $K(X) \to K(U)$ is an isomorphism, and that if
$codim(X - U, X) \geqslant 2$, i.e. if every $x \in X$ such that $\dim O_{X,x} \leqslant 1$ belongs to $U$, the
homomorphism $Z^{1}(X) \to Z^{1}(U)$, and consequently $Cl(X) \to Cl(U)$, is also an isomorphism. Finally, if every
$x \in U$ is factorial — i.e. $O_{X,x}$ is so — then $Z^{1}(U) = Z'^{1}(U)$, and so
$\operatorname{Pic}(U) \simeq Cl(U)$.

**Proposition.**

<!-- label: XI.3.7.1 -->

Let $X$ be a noetherian and normal prescheme. Let $(U_{i})_{i \in I}$ be a family of open sets of $X$ such that:

1. the $U_{i}$ form a filter base;[^N.D.E-XI-2]
1. if one sets $Y_{i} = X - U_{i}$, then $codim(Y_{i}, X) \geqslant 2$ for every $i$;
1. if $x \in U_{i}$ for every $i \in I$, then $O_{X,x}$ is factorial.

Then one has an isomorphism:

```text
lim→_{i ∈ I} Pic(U_i) ──≅──→ Cl(X).
```

Note that b) implies that every $x \in X$ such that $\dim O_{X,x} \leqslant 1$ belongs to $U_{i}$ for every $i$. Hence
the $U_{i}$ are dense, and moreover the homomorphism $Z^{1}(U_{i}) \to Z^{1}(X)$ is an isomorphism, as is
$K(U_{i}) \to K(X)$. So $\operatorname{Pic}(U) \subset Cl(U_{i}) \simeq Cl(X)$. To prove what is desired, it therefore
suffices to show that every $D \in Z^{1}(X)$ belongs to $Z'^{1}(U_{i})$ for a suitable $i$. It suffices to do this for
irreducible positive "divisors". Let then $x \in X$ be such that $\dim O_{X,x} = 1$. It suffices to prove that there
exists $i \in I$ such that ${x}$ is locally principal at the points of $U_{i}$. Let $I$ be the largest ideal of
definition of the closed set ${x}$. The set of points in whose neighborhood $I$ is free is an open set $U$. Now
$U \supset \bigcap_{i \in I} U_{i}$ by c). If we set $Y = X - U$, then $Y \subset \bigcup_{i \in I} Y_{i}$ with
$Y_{i} = X - U_{i}$; now $Y$ is closed, so admits a finite number of generic points, so is contained in the union of
finitely many $Y_{i}$, hence in some $Y_{j}$ for a $j \in I$, because the $U_{i}$ form a filter base. Thus
$U \supset U_{j}$. QED.

**Corollary.**

<!-- label: XI.3.8 -->

Let $X$ be a noetherian and normal prescheme and let $Y$ be a closed part of codimension $\geqslant 2$. Suppose that,
for every $p \in X - Y$, $O_{X,p}$ is factorial; then

```text
Pic(X − Y) ⟶ Cl(X − Y) ⟶ Cl(X)
```

are isomorphisms.

<!-- original page 106 -->

**Corollary.**

<!-- label: XI.3.9 -->

Let $A$ be a noetherian, normal local ring. Set $X' = \operatorname{Spec}(A)$ and $x = r(A)$. In order that $A$ be
factorial, it is necessary and sufficient that $\operatorname{Pic}(X' - {x}) = 0$ and that $p \in X' - {x}$ implies
$A_{p}$ factorial.

Indeed, in order that $A$ be factorial, it is necessary and sufficient that $Cl(X') = 0$.[^N.D.E-XI-3]

**Corollary.**

<!-- label: XI.3.10 -->

Let $A$ be a noetherian local ring of dimension $\geqslant 2$. Set $X' = \operatorname{Spec}(A)$ and let $x = r(A)$. Set
$X = X' - {x}$. The following conditions are equivalent:

1. $A$ is factorial;
1. a) for every $y \in X$, $O_{X,y}$ is factorial, and b) $A$ is parafactorial, i.e. $prof A \geqslant 2$ and
   $\operatorname{Pic}(X) = 0$.

<!-- original page 107 -->

Before proving this corollary, let us state the:

**Serre's criterion of normality.** [^XI-3-star4]

<!-- label: XI.3.11 -->

Let $A$ be a noetherian local ring. In order that $A$ be normal, it is necessary and sufficient that

1. for every prime ideal $p$ of $A$ such that $\dim A_{p} \leqslant 1$, $A_{p}$ be normal;
1. for every prime ideal $p$ of $A$ such that $\dim A_{p} \geqslant 2$, one have $prof A_{p} \geqslant 2$.

Let us prove 3.10.

(i) ⇒ (ii). Knowing that a localization of a factorial ring is factorial, we have (ii) a). Moreover $A$ is normal, so
$prof A \geqslant 2$, since $\dim A \geqslant 2$ (3.11 (ii)). Finally $A$ is parafactorial; indeed
$\operatorname{Pic}(X) \simeq Cl(X') = 0$ (cf. 3.9).

(ii) ⇒ (i). We first prove that $A$ is normal by applying Serre's criterion. Since $\dim A \geqslant 2$, condition (i)
of the criterion is among the hypotheses. Moreover, for every $p \in X$, $A_{p}$ is factorial, hence normal, hence of
depth $\geqslant 2$, at least if $\dim A_{p} \geqslant 2$. Finally $prof A \geqslant 2$ by (ii) b). It remains to apply
3.9.

Let us summarize the preceding:

**Proposition.**

<!-- label: XI.3.12 -->

Let $X$ be a locally noetherian prescheme and let $I$ be a quasi-coherent ideal of $X$. Set $Y = V(I)$. Let
$p \in \mathbb{N}$. Suppose that:

1. $Leff(X, Y)$ holds (Exposé X);
1. $H^{i}(X, I^{n+1}/I^{n+2}) = 0$ if $i = 1$ or `2` and if $n \geqslant p$;
1. for every open neighborhood $U$ of $Y$ in $X$ and every $x \in X - U$, the ring $O_{X,x}$ is parafactorial.

Then, for every $n \geqslant p$ and every open neighborhood $U$ of $Y$, the homomorphisms

```text
Pic(X) ⟶ Pic(U) ⟶ Pic(X_n)
```

(with the canonical commutative triangle) are isomorphisms.

One knows some parafactorial rings:

<!-- original page 108 -->

**Theorem.**

<!-- label: XI.3.13 -->

1. (Auslander–Buchsbaum)[^N.D.E-XI-4] A regular noetherian local ring is factorial (hence parafactorial if its dimension
   is $\geqslant 2$).
1. A noetherian local ring of dimension $\geqslant 4$ that is a complete intersection is parafactorial.

**Corollary** (Samuel conjecture)[^N.D.E-XI-5]**.**

<!-- label: XI.3.14 -->

A noetherian local ring $A$ that is a complete intersection and that is factorial in codimension $\geqslant 3$ (i.e.
$\dim A_{p} \leqslant 3$ implies that $A_{p}$ is factorial) is factorial.

*Proof of the corollary.* We argue by induction on the dimension of $A$. If $\dim A \leqslant 3$, then $A$ is factorial
by hypothesis. If $\dim A > 3$, by the induction hypothesis, and remarking that a localization of a complete
intersection is also a complete intersection, all localizations of $A$ other than $A$ itself are factorial. By Theorem
3.13 (ii), $A$ is parafactorial, hence factorial by 3.10.

*Proof of 3.13 (i)* (following Kaplansky).[^XI-3-star5]

Let $A$ be a regular noetherian local ring; set $\dim A = n$. If $n = 0$ or `1`, the result is known. Suppose
$n \geqslant 2$, and argue by induction on $n$: suppose $n \geqslant 2$ and the theorem proved for rings of dimension
$< n$. Set $X' = \operatorname{Spec}(A)$ and $X = X' - {x}$, where $x = r(A)$. The localizations of $A$ other than $A$
are regular and of dimension $< n$, hence factorial. Moreover $prof A = \dim A \geqslant 2$. It therefore suffices to
prove that $\operatorname{Pic}(X) = 0$ (Cor. 3.10). Let then $L$ be an invertible `O_X`-Module; one knows that one can
prolong it to a coherent $O_{X'}$-Module $L'$. There exists a resolution of $L'$ by free $O_{X'}$-Modules:

$$
0 \longleftarrow L' \longleftarrow L'_{1} \longleftarrow \cdots \longleftarrow L'_{n} \longleftarrow 0,
$$

since the cohomological dimension of $A$ is finite. By restriction to $X$ one obtains a finite free resolution. It
therefore suffices to prove the following lemma:

<!-- original page 109 -->

**Lemma.**

<!-- label: XI.3.15 -->

Let $(X, O_{X})$ be a ringed space and let $L$ be a locally free `O_X`-Module that admits a finite resolution by free
modules of finite type. Then $det(L) \simeq O_{X}$.

Recall that one defines $det(L)$ as the maximal exterior power of $L$. In the case envisaged, $det(L) \simeq L$ since
$L$ is invertible, so the lemma allows us to conclude. Let us prove this lemma. Let

```text
0 ⟵ L_0 ⟵ L_1 ⟵ L_2 ⟵ ⋯ ⟵ L_n ⟵ 0
```

be the announced exact sequence, where $L_{0} = L$. Since everything is locally free, one has:

```text
⨂_{0 ⩽ i ⩽ n} (det(L_i))^{(−1)^i} ≃ O_X;
```

now all the $L_{i}$ for $i > 0$ are free, so their determinants are free as well, hence so is the determinant of
$L_{0} = L$. QED.

It remains to prove (ii) of the theorem. Beforehand, let us prove a lemma that will permit us to proceed by induction:

**Lemma.**

<!-- label: XI.3.16 -->

Let $A$ be a noetherian local ring that is a quotient of a regular ring. Let $t \in r(A)$ be an $A$-regular element.
Suppose that $A$ is complete for the $t$-adic topology. Set $X' = \operatorname{Spec}(A)$,
$Y' = V(t) \simeq \operatorname{Spec}(B)$, $B = A/tA$, $X = X' - {x}$, $Y = Y' - {x}$, $x = r(A)$. Suppose that:

1. for every $y \in X$ closed in $X$, one has $prof O_{X,y} \geqslant 2$,
1. $prof A/tA \geqslant 3$,

then the map $\operatorname{Pic}(X) \to \operatorname{Pic}(Y)$ is injective. In particular, if $B$ is parafactorial,
then so is $A$.

One knows that a) implies $Lef(X, Y)$ thanks to X 2.1. If we prove that $H^{1}(Y, P_{n}) = 0$ for every $n \geqslant 0$,
we shall know thanks to (2.2) that $\operatorname{Pic}(X) \to \operatorname{Pic}(Y)$ is injective. If, moreover, $B$ is
parafactorial, we shall know that $\operatorname{Pic}(Y) = 0$ (3.5), hence $\operatorname{Pic}(X) = 0$; now
$prof(A) \geqslant 3 + 1 \geqslant 2$ since $t$ is $A$-regular, so $A$ will be parafactorial by 3.5.[^TRANSLATOR-XI-1]

Let $I = (tA)^{\sim}$ be the $O_{X'}$-Module associated with the ideal `tA`. In no. 1, we set
$P_{n} = (I^{n+1}/I^{n+2})|Y$ for every $n \geqslant 0$. Now $t$ is $A$-regular, so $P_{n} \simeq O_{Y}$. It therefore
remains to prove that $H^{1}(Y, O_{Y}) = 0$. Now $Y = Y' - {x}$ is an open subset of $Y'$, so we have an exact sequence
(I (27)):

```text
H¹(Y′, O_{Y′}) ⟶ H¹(Y, O_Y) ⟶ H²_x(Y′, O_{Y′}),
```

whose right-hand term is zero by virtue of hypothesis b), and whose left-hand term is zero because $Y'$ is affine. QED.

**Lemma.**

<!-- label: XI.3.17 -->

Retaining the hypotheses of 3.16, suppose moreover that:

1. (c) for every $y$ closed in $Y$, $prof O_{X,y} \geqslant 3$,
1. (d) $prof A/tA \geqslant 4$ (stronger than b),
1. (e) for every $y$ closed in $X$ with $y \in Y$, the ring $O_{X,y}$ is parafactorial.

Then the map $\operatorname{Pic}(X) \to \operatorname{Pic}(Y)$ is an isomorphism; in particular, in order that $A$ be
parafactorial, it is necessary and sufficient that $B$ be so.

One knows (X 2.1) that a) and c) imply $Leff(X, Y)$. Moreover, by the reasoning just made, d) implies that
$H^{i}(Y, P_{n}) = 0$ for every $n \geqslant 0$ and $i = 1$ or $i = 2$. Furthermore, for every open neighborhood $U$ of
$Y$ in $X$, the complement of $U$ in $X$ consists of a finite number of closed points. Thanks to e) and Theorem 3.12, we
deduce that $\operatorname{Pic}(X) \to \operatorname{Pic}(Y)$ is an isomorphism. On the other hand,
$prof A \geqslant prof B \geqslant 2$; by criterion 3.5, we deduce that $A$ is parafactorial if and only if $B$ is so.

Let us now prove 3.13 (ii). Let $R$ be a regular noetherian local ring. Let $(t_{1}, \cdots, t_{k})$ be an $R$-sequence.
Set $B = R/(t_{1}, \cdots, t_{k})$ and suppose $\dim B \geqslant 4$. We must prove that $B$ is parafactorial. We argue
by induction on $k$. If $k = 0$, then $B$ is regular, hence factorial by 3.13 (i), hence parafactorial by 3.10. Suppose
$k \geqslant 1$ and the theorem proved for $k' < k$. Set $A = R/(t_{1}, \cdots, t_{k-1})$, so $B = A/t_{k} A$. We may
suppose $B$ complete by 3.7. By the induction hypothesis, $A$ is parafactorial. Let us prove that we may apply Lemma
3.17. We have supposed $B$ complete, hence so is $A$, and therefore $A$ is complete for the $t_{k}$-adic topology. If
$x \in X$, and if $x$ is closed in $X$, then $A_{x}$ is a complete intersection of dimension $\geqslant 4$, with
$k' < k$. By the induction hypothesis, $A_{x}$ is parafactorial, and moreover of depth $\geqslant 4$. This gives a), c),
and e). Moreover $\dim A \geqslant 5$, whence d). QED.

**Theorem.**

<!-- label: XI.3.18 -->

Let $X$ be a locally noetherian prescheme and let $I$ be a coherent sheaf of ideals on $X$. Set $Y = V(I)$. Let $n$ be
an integer. Suppose that:

1. $Leff(X, Y)$ holds (cf. examples X 2.1 and X 2.2);
1. for every $p \geqslant n$, one has $H^{i}(Y, I^{p+1}/I^{p+2}) = 0$ for $i = 1$ and $i = 2$;
1. for every open $U \supset Y$ and every $x \in X - U$, the ring $O_{X,x}$ is regular of dimension $\geqslant 2$ or a
   complete intersection of dimension $\geqslant 4$.

Then, for every open $U \supset Y$ and every integer $p \geqslant n$, the homomorphisms

```text
Pic(X) ⟶ Pic(U) ⟶ Pic(Y_p)
```

are isomorphisms, where $Y_{p}$ denotes the prescheme $(Y, O_{X}/I^{p+1})$.

It suffices to combine 3.12 and 3.13.

<!--
LEDGER DELTA (Exposé XI):

| French | English | Note |
| --- | --- | --- |
| application au groupe de Picard | application to the Picard group | Title. |
| calqué sur | modeled on | Standard. Not "traced from"; the French sense is structural mimicry. |
| Module inversible | invertible Module | Capital preserved per source. |
| classe à isomorphisme près | isomorphism class | Standard. |
| complété formel `X̂` | formal completion `X̂` | Standard; hat preserved across OCR line breaks. |
| voisinage ouvert variable | variable open neighborhood | Preserves the "running variable" sense. |
| Pic(X̂) | Pic(X̂) | Notation preserved; the OCR repeatedly breaks the hat across a line ("Pic( b\nX)"). |
| `X_n = (Y, O_X/I^{n+1})` | `X_n = (Y, O_X/I^{n+1})` | Source uses both `X_n` and `Y_n` for this prescheme; preserved as-is. |
| `Y_n` (in Prop 1.1, Cor 2.2) | `Y_n` | Same prescheme as `X_n`; the source switches subscript carrier between §1 and §2. Y_p is explicitly redefined this way in 3.18. |
| `Lef(X, Y)`, `Leff(X, Y)` | `Lef(X, Y)`, `Leff(X, Y)` | Lefschetz / effective Lefschetz condition; defined in Exp. X. |
| pleinement fidèle | fully faithful | Standard. |
| parafactoriel aux points de Z | parafactorial at the points of Z | Per glossary. |
| couple parafactoriel | parafactorial pair | Per glossary. |
| anneau local parafactoriel | parafactorial local ring | Per glossary. |
| factoriel | factorial | Standard (unique factorization). |
| intersection complète | complete intersection | Standard. |
| factoriel en codimension `⩾ 3` | factorial in codimension `⩾ 3` | Standard. |
| critère de normalité de Serre | Serre's criterion of normality | Standard. |
| diviseur principal | principal divisor | Standard. |
| diviseur localement principal | locally principal divisor | EGA-style terminology. |
| diviseur de Cartier | Cartier divisor | Standard. |
| anneau régulier | regular ring | Standard. |
| anneau de valuation discrète | discrete valuation ring | Standard. |
| résolution libre finie | finite free resolution | Standard. |
| dimension cohomologique | cohomological dimension | Standard. |
| base de filtre | filter base | The N.D.E. glosses this as a "decreasing filtered family". |
| `A`-régulier (élément, suite) | `A`-regular (element, sequence) | Standard; cf. SGA 2 glossary on `M`-regular. |
| topologie `t`-adique | `t`-adic topology | Standard. |
| déterminant `det(L)` | determinant `det(L)` | Maximal exterior power; per the lemma. |
| sic | sic | Source-author marker; preserved. |
| C.Q.F.D. | QED | Per glossary. |
| théorème d'Auslander–Buchsbaum | Auslander–Buchsbaum theorem | Per glossary. |
| conjecture de Samuel | Samuel conjecture | Per glossary. |
| morphisme fidèlement plat et quasi-compact | faithfully flat and quasi-compact morphism | Standard. |
| morphisme de descente | morphism of descent | Standard. |
-->

[^XI-3-star1]: For a more detailed study of the notion of parafactoriality, and the proof of 3.3, cf. EGA IV 21.13,
    21.14.

[^N.D.E-XI-1]: *N.D.E.* For a precise study of the link between the factoriality of $A$ and that of its completion, see
    (Heitmann R., "Characterization of completions of unique factorization domains", *Trans. Amer. Math. Soc.* **337**
    (1993), no. 1, pp. 379–387).

[^XI-3-star2]: For the generalities that follow, cf. also EGA IV 21.

[^XI-3-star3]: In conformity with the terminology of EGA IV 21, we now prefer to reserve the name "divisors" for
    "locally principal divisors" or "Cartier divisors".

[^N.D.E-XI-2]: *N.D.E.* i.e. a decreasing filtered family.

[^N.D.E-XI-3]: *N.D.E.* See Bourbaki, *Algèbre commutative* VII.1.4, cor. to th. 2, and VII.3.2, th. 1.

[^XI-3-star4]: Cf. EGA IV 5.8.6.

[^N.D.E-XI-4]: *N.D.E.* To be compared with the following purity result, due to Gabber. Let $X$ be the spectrum of a
    regular local ring $A$ of dimension 3, $a$ an element of nonzero differential, i.e. $a \in m - m^{2}$, and $U$ the
    complement of $V(a)$. Then a vector bundle on $U$ is free (for a simple proof, see Swan R.G., "A simple proof of
    Gabber's theorem on projective modules over a localized local ring", *Proc. Amer. Math. Soc.* **103** (1988), no. 4,
    pp. 1025–1030). The rank-1 case is a particular case of Theorem 3.13. For purity results concerning vector bundles
    of arbitrary rank, in either the analytic or the algebraic setting, see (Gabber O., "On purity theorems for vector
    bundles", *Internat. Math. Res. Notices* (2002), no. 15, pp. 783–788).

[^N.D.E-XI-5]: *N.D.E.* For a proof in the same vein, but more elementary, see Call F. & Lyubeznik G., "A simple proof
    of Grothendieck's theorem on the parafactoriality of local rings", in *Commutative algebra: syzygies,
    multiplicities, and birational algebra* (South Hadley, MA, 1992), Contemp. Math., vol. 159, American Mathematical
    Society, Providence, RI, 1994, pp. 15–18.

[^XI-3-star5]: It is the proof reproduced in EGA IV 21.11.1.

[^TRANSLATOR-XI-1]:
    <!-- Editorial note: The source literally has "prof(A) = 3 + 1 ⩾ 2 car t est A-régulier". The
    intended chain is: since `t ∈ r(A)` is `A`-regular and `A` is complete for the `t`-adic topology, `prof(A) ⩾
    prof(A/tA) + 1 = prof(B) + 1`; using b) `prof(B) ⩾ 3` gives `prof(A) ⩾ 4`, and only `⩾ 2` is needed for the
    application of 3.5. The translation preserves the "3 + 1" numeric form. -->


<!-- SOURCE: 12-schemas-algebriques-projectifs.md -->

# Exposé XII. Applications to projective algebraic schemes

<!-- label: XII -->

<!-- original page 109 -->

## 1. Projective duality theorem and finiteness theorem

<!-- label: XII.1 -->

[^XII-1-star]

The following theorem, essentially contained in *FAC*[^XII-1-starstar] (except that at the time Serre did not yet have
at his disposal the language of `Ext` of sheaves of modules[^N.D.E-XII-1]), is the global analogue of the local duality
theorem (Exp. IV), which was modelled on it.

**Theorem.**

<!-- label: XII.1.1 -->

Let $k$ be a field, $X = P^{r}_{k}$ projective space of dimension $r$ over $k$, and $F$ a variable coherent module on
$X$. Then one has an isomorphism of $\partial$-functors in $F$:

```text
Hⁱ(X, F)′ ⥲ Ext^{r−i}(X; F, Ωʳ_{X/k}),
```

<!-- label: eq:XII.1.1 -->

where one sets

$$
\Omega^{r}_{X/k} = O_{P^{r}_{k}}(-r - 1).
$$

<!-- label: eq:XII.1.2 -->

**Remark.**

Of course, this module is also the module of relative differentials of degree $r$ of $X$ over $k$. In this form, the
theorem remains true if $X$ is a proper and smooth scheme over $k$ (for the projective case, see A. Grothendieck,
"Théorèmes de dualité pour les faisceaux algébriques cohérents", *Séminaire Bourbaki*, May 1957).[^XII-1-starstarstar]
When $F$ is locally free, one recovers Serre's duality theorem

```text
Hⁱ(X, F)′ ⥲ H^{r−i}(Hom_{O_X}(F, Ωʳ_{X/k})).
```

Theorem 1.1 (which moreover recovers the case of $X$ projective over $k$, as in *loc. cit.*) will suffice for our
purposes.

<!-- original page 110 -->

The homomorphism (1) is deduced from the Yoneda pairing

```text
Hⁱ(X, F) × Ext^{r−i}(X; F, Ωʳ_{X/k}) → Hʳ(X, Ωʳ_{X/k}),
```

<!-- label: eq:XII.1.3 -->

and from a well-known isomorphism (cf. *FAC*, or *EGA* III 2.1.12):

```text
Hʳ(X, Ωʳ_{X/k}) = Hʳ(P^r_k, O_{P^r_k}(−r − 1)) ⥲ k.
```

<!-- label: eq:XII.1.4 -->

To show that (1) is an isomorphism, one proceeds as in the case of the local duality theorem, noting that $H^{r}(X, F)$,
as a functor in $F$, is right exact (since $H^{n}(X, F) = 0$ for $n > r$), and that every coherent module is isomorphic
to a quotient of a direct sum of modules of the form $O(-m)$ with $m$ large. This reduces us, by descending induction on
$i$, to making the verification for a sheaf of the form $O(-m)$, where it is contained in the well-known explicit
computations (*FAC*, or *EGA* III 2.1.12). One may moreover assume $-m \leqslant -r - 1$, in which case
$H^{i}(X, O(-m)) = 0$ for $i \neq r$.

**Corollary.**

<!-- label: XII.1.2 -->

For $F$ coherent and given, and $m$ large enough, one has a canonical isomorphism

```text
Hⁱ(X, F(−m))′ ⥲ H⁰(X, ℰxt^{r−i}_{O_X}(F, Ωʳ_{X/k})(m))
```

<!-- label: eq:XII.1.5 -->

(where $'$ denotes the vector-space dual).

Indeed, on projective space $X$, for any pair of coherent sheaves $F$, $G$ and for $n$ large enough one has a canonical
isomorphism:

```text
Extⁿ(X; F(−m), G) ≅ Extⁿ(X; F, G(m)) ⥲ H⁰(X, ℰxtⁿ_{O_X}(F, G)(m)),
```

<!-- label: eq:XII.1.6 -->

(the isomorphism of the first two terms being trivially true for any $m$), as follows from the spectral sequence of
global `Ext`

```text
Hᵖ(X, ℰxt^q_{O_X}(F, G(m))) ⇒ Ext^•(X; F, G(m)),
```

<!-- original page 111 -->

which degenerates for $m$ large thanks to the fact that

```text
ℰxt^q_{O_X}(F, G(m)) ≅ ℰxt^q_{O_X}(F, G)(m),
```

and that the $\mathcal{E}xt^{q}_{O_{X}}(F, G)$ are coherent sheaves. Hence (5) follows from (6) and (1).

**Corollary.**

<!-- label: XII.1.3 -->

For given `i, F`, the following conditions are equivalent:

1. $H^{i}(X, F(-m)) = 0$ for $m$ large.
1. (i bis) $H^{i}(X, F(\cdot)) = \bigoplus_{m \in \mathbb{Z}} H^{i}(X, F(-m))$ is a finitely generated $S$-module, where
   $S = k[t_{0}, \cdots, t_{r}]$.
1. $\mathcal{E}xt^{r-i}_{O_{X}}(F, \Omega^{r}_{X/k}) = 0$.
1. (ii bis) $\mathcal{E}xt^{r-i}_{O_{X}}(F, O_{X}) = 0$.
1. $H^{i}_{x}(F_{x}) = 0$ for every closed point $x$ of $X$.
1. $H^{i+1}_{x}(\tilde{F}_{x}) = 0$ for every closed point $x$ of the punctured projecting cone
   $\tilde{X} = \operatorname{Spec}(S) - \operatorname{Spec}(k)$ of $X$, where $\tilde{F}$ denotes the inverse image of
   $F$ under the canonical morphism $\tilde{X} \to X$.

*Proof.*

(i) ⇔ (i bis) since the submodule of $H^{i}(X, F(\cdot))$ formed by the sum of the homogeneous components of degree
$\geqslant \nu$ is finitely generated over $S$ (in fact, for $i \neq 0$, it is even finitely generated over $k$), cf.
*FAC* or *EGA* III 2.2.1 and 2.3.2.

(i) ⇔ (ii) by virtue of Corollary 1.2.

(ii) ⇔ (ii bis) since $\Omega^{r}_{X/k}$ is locally isomorphic to `O_X`.

(ii bis) ⇔ (iii) by virtue of the local duality theorem for $O_{X,x}$ (which is a regular local ring of dimension $r$),
according to which the "dual" of $\mathcal{E}xt^{r-i}_{O_{X}}(F, O_{X})_{x}$ is identified with $H^{i}_{x}(F_{x})$ (V
2.1).

(ii bis) is equivalent to the analogous relation

$$
\mathcal{E}xt^{r-i}_{O_{\tilde{X}}}(\tilde{F}, O_{\tilde{X}}) = 0
$$

(thanks to the fact that $\tilde{X} \to X$ is faithfully flat, so the inverse image of
$\mathcal{E}xt^{r-i}_{O_{X}}(F, O_{X})$ is isomorphic to
$\mathcal{E}xt^{r-i}_{O_{\tilde{X}}}(\tilde{F}, O_{\tilde{X}})$), and this last relation is equivalent to (iv) by the
local duality theorem for the local ring $O_{\tilde{X},x}$, which is regular of dimension $r + 1$.

In particular, applying this to all $i \leqslant n$, one finds:

**Corollary.**

<!-- label: XII.1.4 -->

Equivalent conditions for given `n, F`:

1. $H^{i}(X, F(-m)) = 0$ for $i \leqslant n$ and $m$ large.
1. (i bis) $H^{i}(X, F(\cdot))$ is a finitely generated $S$-module for $i \leqslant n$.
1. $prof(F_{x}) > n$ for every closed point $x$ of $X$.
1. $prof(\tilde{F}_{x}) > n + 1$ for every closed point $x$ of $\tilde{X}$.

The interest of Corollaries 1.3 and 1.4 is to express a global condition (i) or (i bis) in terms of local conditions,
namely the vanishing of local invariants such as $H^{i}_{x}(X, F_{x})$ or $H^{i}_{x}(\tilde{X}, \tilde{F}_{x})$, or an
inequality on depth. In this form, these results remain trivially valid for an arbitrary projective scheme $X$ and a
very ample invertible sheaf $O_{X}(1)$ on $X$, as one sees by inducing the latter using a suitable projective immersion
$X \to P^{r}_{k}$. (Of course, conditions 1.3 (ii) and 1.3 (ii bis) are no longer equivalent to the others in this
general case, except if one assumes for example that $X$ is regular.) One may moreover generalize to the case of a
projective morphism $X \to S$ as follows:

**Proposition.**

<!-- label: XII.1.5 -->

<!-- original page 112 -->

Let $f: X \to S$ be a projective morphism with $S$ noetherian, $O_{X}(1)$ an invertible module on $X$ very ample
relatively to $S$, $F$ a coherent module on $X$, flat with respect to $S$, $s$ an element of $S$, $X_{s}$ the fiber of
$X$ at $s$ (considered as a projective scheme over $k(s)$), $F_{s}$ the sheaf induced on $X_{s}$ by $F$, finally $i$ an
integer. Suppose that for every closed point $x$ of $X_{s}$, one has $H^{i}_{x}(F_{s,x}) = 0$ (for example
$prof(F_{s,x}) > i$). Then there exists an open neighborhood $U$ of $s$ such that the same condition is verified for
$s' \in U$. Moreover, for such a $U$, one has

```text
Rⁱf_∗(F(−m)) = 0 for m large,
```

and if $\mathcal{S}$ is a graded quasi-coherent algebra on $S$, generated by $\mathcal{S}^{1}$, that defines $X$
together with $O_{X}(1)$ as $X = \operatorname{Proj}(\mathcal{S})$, $O_{X}(1) = \operatorname{Proj}(\mathcal{S}(1))$,
then the $\mathcal{S}$-module

```text
Rⁱf_∗(F(·)) = ⨁_{m ∈ ℤ} Rⁱf_∗(F(m))
```

is finitely generated on $U$.

Embed $X$ in some $X' = P^{r}_{S}$ so that $O_{X}(1)$ is induced by $O_{X'}(1)$ (which is possible, possibly by
replacing $S$ by an affine neighborhood of $s$). Set[^XII-1-star2] for every integer $j$ and every $t \in S$:

$$
E^{j}(t) = Ext^{j}_{O_{X'_{t}}}(F'_{t}, O_{X'_{t}}(-r - 1)).
$$

<!-- label: eq:XII.1.7 -->

Thus $E^{j}(t)$ is a coherent module on $X_{t}$. I claim that, for variable $t$, the family of these modules is
"constructible" in the following sense: for every $t \in S$ there exists a non-empty open subset $V$ of the closure of
$t$, which one endows with the induced reduced structure, and a coherent module $E^{j}(V)$ on $X_{V} = X \times_{S} V$,
flat relatively to $V$, such that for every $t' \in V$, $E^{j}(t')$ is isomorphic to the module induced by $E^{j}(V)$ on
$X_{t'}$. To verify this assertion, setting $Z = {t}$ with its induced structure, one considers the coherent modules

$$
E^{j}(Z) = Ext^{j}_{O_{X'_{Z}}}(F_{Z}, O_{X'_{Z}}(-r - 1))
$$

(where the subscript $Z$ means again that one induces over $Z$), and one takes for $V$ a non-empty open subset of $Z$
such that the modules $E^{j}(Z)$ are flat over $V$: this is possible since one checks immediately that $E^{j}(Z) = 0$
for $j$ not lying in the interval `[0, r]`, and one may apply *SGA* 1 IV 6.11. One then takes
$E^{j}(V) = E^{j}(Z)|X_{V}$, and one verifies easily that it answers the question.

<!-- original page 113 -->

From the preceding remark it follows that there exists a finite partition of $S$ formed by sets $V_{\alpha}$ of the form
$V = V(t)$ as above (noetherian induction), and applying Serre's theorem *EGA* III 2.2.1 to the $E^{j}(V_{\alpha})$, one
sees that there exists an integer $m_{0}$ such that

```text
Rⁱf_{V_α∗}(Eʲ(V_α)) = 0 for i ≠ 0, m ⩾ m₀, for all j,
```

whence it follows, using the flatness of $E^{j}(V_{\alpha})$ with respect to $V_{\alpha}$ and easy Künneth-type
relations (cf. *EGA* III, §7), that

```text
Hⁱ(X_t, Eʲ(t)(m)) = 0 for i ≠ 0, m ⩾ m₀, for all j,
```

for every $t \in V_{\alpha}$, hence for every $t$ since the $V_{\alpha}$ cover $S$. From this and the spectral sequence
of global `Ext` follows, thanks to 1.1 and as in the proof of 1.2, an isomorphism

```text
Hⁱ(X_t, F_t(−m))′ ⥲ H⁰(X_t, E^{r−i}(t)(m)) for m ⩾ m₀,
```

<!-- label: eq:XII.1.8 -->

every integer $i$, and every $t \in S$.

Let us now use the hypothesis on $F_{s}$, which is written

$$
E^{r-i}(s) = 0,
$$

<!-- label: eq:XII.1.9 -->

and which, thanks to (8), is equivalent to

```text
Hⁱ(X_s, F_s(−m)) = 0 for m ⩾ m₀.
```

<!-- label: eq:XII.1.10 -->

Since $F$, hence $F(-m)$, is flat with respect to $S$, it follows by the Künneth-type relations already invoked that
(for $m$ given) the same relation (10) holds when $s$ is replaced by a $t$ near $s$, in particular for any generization
$t$ of $s$. By virtue of (8), one will therefore have, for such a generization,

$$
E^{r-i}(t) = 0,
$$

<!-- label: eq:XII.1.11 -->

now the set of $t \in S$ for which this relation holds is plainly a constructible set (since it induces an open set on
each $V_{\alpha}$); since it contains the generizations of $s$, it contains an open neighborhood $U$ of $s$. This proves
the first assertion of 1.5. Moreover, for $t \in U$, one concludes from (11) and (8) that

```text
Hⁱ(X_t, F_t(−m)) = 0 for m ⩾ m₀, t ∈ U,
```

<!-- label: eq:XII.1.12 -->

which, by virtue of the Künneth-type relations, implies (in fact, is much stronger than)

```text
Rⁱf_∗(F(−m)) = 0 on U, for m ⩾ m₀.
```

<!-- label: eq:XII.1.13 -->

This proves the second assertion of 1.5. Finally the last assertion follows at once, by proceeding as at the start of
the proof of 1.3.

**Remark.**

<!-- label: XII.1.6 -->

[^XII-1-star3]

The proof simplifies notably (by eliminating any consideration of constructibility) when one assumes already that the
hypothesis made for $s \in S$ is verified at every $s' \in S$. In fact, when one makes the hypothesis that $F_{s}$ is of
depth $> i$ at the closed points of $X_{s}$, one has at one's disposal a general statement, local in nature on $X$,
which says that the same condition is verified for all $X_{t}$, on condition of replacing $X$ by a suitable open
neighborhood of the fiber $X_{s}$ (in other words, a certain part of $X$, defined by conditions on the modules induced
by $F$ on the fibers, is open, cf. *EGA* IV). Since $f$ is proper here, one may therefore take this neighborhood of the
form $f^{-1}(U)$, which recovers the first assertion of 1.5 without any tedious dévissage. In this general case, one may
still prove by the method of *loc. cit.* that the first assertion of 1.5 (proved here by global means, using that $X$ is
projective over $S$) follows from a purely local statement on $X$ (which the reader will spell out if he thinks it
useful).

<!-- original page 114 -->

## 2. Lefschetz theory for a projective morphism: Grauert's comparison theorem

<!-- label: XII.2 -->

It is the following theorem:

**Theorem.**

<!-- label: XII.2.1 -->

Let $f: X \to S$ be a projective morphism with $S$ noetherian, $O_{X}(1)$ an invertible module on $X$, ample relatively
to $S$, $Y$ the prescheme of zeros of a section $t$ of $O_{X}(1)$, $\mathcal{J}$ the ideal defining $Y$, $X_{n}$ the
subprescheme of $X$ defined by $\mathcal{J}^{n+1}$, $\hat{X}$ the formal completion of $X$ along $Y$,
$\hat{f}: \hat{X} \to S$ the composite morphism $\hat{X} \to X \to S$, $F$ a coherent module on $X$, flat relatively to
$S$. Suppose moreover that for every $s \in S$, the module $F_{s}$ induced on the fiber $X_{s}$ is of depth $> n$ at the
points of that fiber, and that $t$ is $F$-regular. Under these conditions:

1. The canonical homomorphism

    ```text
    Rⁱf_∗(F) → Rⁱf̂_∗(F̂)
    ```

    is an isomorphism for $i < n$, a monomorphism for $i = n$.

1. The canonical homomorphism

    ```text
    Rⁱf̂_∗(F̂) → lim_m Rⁱf_∗(F_m)
    ```

    is an isomorphism for $i \leqslant n$.

*Proof.*

One reduces at once to the case where $S$ is affine, and to proving in this case the following:

**Corollary.**

<!-- label: XII.2.2 -->

Under the conditions of 2.1, suppose moreover that $S$ is affine. Then:

1. The canonical homomorphism

    ```text
    Hⁱ(X, F) → Hⁱ(X̂, F̂)
    ```

    is an isomorphism for $i < n$, a monomorphism for $i = n$.

1. <!-- original page 115 -->

    The canonical homomorphism

    ```text
    Hⁱ(X̂, F̂) → lim_m Hⁱ(X_m, F_m)
    ```

    is an isomorphism for $i \leqslant n$.

Replacing $O_{X}(1)$ by a tensor power, and $t$ by a power of $t$ if necessary, one may assume $O_{X}(1)$ very ample
relatively to $S$. On the other hand, $t$, hence `tᵐ`, being $F$-regular, multiplication by `tᵐ`, considered as a
homomorphism from $F(-m)$ to $F$, is injective; so one has for every $m \geqslant 0$ an exact sequence:

```text
0 → F(−m) ──tᵐ──→ F → F_m → 0,
```

<!-- label: eq:XII.2.14 -->

whence a cohomology exact sequence

```text
Hⁱ(X, F(−m)) → Hⁱ(X, F) → Hⁱ(X, F_m) → H^{i+1}(X, F(−m)).
```

Now by virtue of 1.5 one has $H^{i}(X, F(-m)) = 0$ for $i \leqslant n$ and $m$ large enough, which proves the following:

**Lemma.**

<!-- label: XII.2.3 -->

For $m$ large, the canonical homomorphism

```text
Hⁱ(X, F) → Hⁱ(X, F_m)
```

is bijective if $i < n$, injective if $i = n$.

This shows that for $i < n$, the projective system $(H^{i}(X_{m}, F_{m}))_{m\geqslant 0}$ is essentially constant, *a
fortiori* satisfies the Mittag-Leffler condition; therefore (taking into account $\hat{F} = \lim F_{m}$) one concludes
(ii) by *EGA* 0_III 13.3. On the other hand, (i) follows trivially, taking into account 2.3.

**Corollary.**

<!-- label: XII.2.4 -->

[^N.D.E-XII-2]

Let $f: X \to S$ be a flat projective morphism with $S$ locally noetherian, $O_{X}(1)$ an invertible module on $X$,
ample relatively to $S$, $t$ a section of this module that is `O_X`-regular, $Y$ the subprescheme of zeros of $t$,
$\hat{X}$ the formal completion of $X$ along $Y$. Suppose that for every $s \in S$, $X_{s}$ is of depth $\geqslant 1$
(resp. of depth $\geqslant 2$) at its closed points. Then for every open neighborhood $U$ of $Y$, the functor

$$
F \mapsto \hat{F}
$$

from the category of locally free coherent modules on $U$ to the category of locally free coherent modules on $\hat{X}$
is faithful (resp. fully faithful, i.e. the Lefschetz condition (Lef) of X 2 is verified).

For two locally free modules $F$ and $G$ on $U$ introduce the module

$$
H = \operatorname{Hom}_{O_{U}}(F, G);
$$

one is reduced to proving that the canonical homomorphism

```text
H⁰(U, H) → H⁰(Û, Ĥ)
```

<!-- label: eq:XII.2.15 -->

is injective (resp. bijective). Now the modules $H_{t}$ are of depth $\geqslant 1$ (resp. $\geqslant 2$) at the closed
points of $X_{t}$; one may therefore apply 2.1, which implies the conclusion of 2.4 in the case where $U = X$. In the
case of an arbitrary $U$, one notes that the question is local on $S$, so one may assume $S$ affine. Then every coherent
module on $X$ is a quotient of a locally free coherent module (since $O_{X}(1)$ is a relatively ample invertible module
on $X$). Since the dual module $H' = \operatorname{Hom}(H, O_{U})$ extends to a coherent module on $X$, which is
therefore isomorphic to a cokernel of a homomorphism of locally free modules on $X$, it follows by transposition that
one may find a homomorphism

$$
u': L'^{0} \to L'^{1}
$$

<!-- original page 116 -->

of locally free modules on $X$, inducing a homomorphism

$$
u: L^{0} \to L^{1}
$$

of locally free modules on $U$, such that one has an exact sequence

```text
0 → H → L⁰ ──u──→ L¹.
```

Using the five lemma (which becomes the three lemma), and the left exactness of the functor $H^{0}$, one is reduced to
proving that (15) is injective (resp. bijective) when $H$ is replaced by $L^{0}$, $L^{1}$, which reduces us to the case
where $H$ is induced by a locally free module $H'$ on $X$. Moreover, in the non-respective case this reduction is even
unnecessary, since the kernel of (15) is in any case formed of the sections of $H$ on $U$ that vanish in a suitable open
neighborhood $V$ of $Y$; now the restriction homomorphism $H^{0}(U, H) \to H^{0}(V, H)$ is injective, since $H$ is of
depth $\geqslant 1$ at the points of any closed subset $Z$ of $X$ not meeting $Y$ (cf. the lemma below). In the
respective case, one is reduced to proving that

```text
H⁰(X, H′) → H⁰(U, H′)
```

is bijective, which follows from the fact that $H'$ is of depth $\geqslant 2$ at every point of a closed subset
$Z = X - U$ of $X$ not meeting $Y$. One therefore needs only to prove the following:

**Lemma.**

<!-- label: XII.2.5 -->

Let $F$ be a coherent module on $X$, flat with respect to $S$, such that for every $s \in S$, $F_{s}$ is of depth
$\geqslant n$ at every closed point of $X_{s}$. Then for any closed subset $Z$ of $X$ not meeting $Y$, $F$ is of depth
$\geqslant n$ at every point of $Z$.

Indeed, for every $x \in X$, setting $s = f(x)$, one has

$$
prof(F_{x}) \geqslant prof(F_{s,x}),
$$

<!-- label: eq:XII.2.16 -->

<!-- original page 117 -->

as one sees by lifting in any way a maximal $F_{s,x}$-regular sequence of elements of $\mathfrak{r}(O_{X_{s},x})$, which
yields an $F_{x}$-regular sequence by virtue of *SGA* 1 IV 5.7. Now if $x$ belongs to a $Z$ as in Lemma 2.5, then $x$ is
necessarily closed in $X_{s}$; in other words, $Z$ is finite over $S$. Indeed $Z$ (endowed with a structure induced by
$X$) is projective over $S$ as a closed subprescheme of $X$ which is so, and $Z$ is affine over $S$ as a closed
subprescheme of $X - Y$, which is so.

**Remark.**

<!-- label: XII.2.6 -->

Suppose that for every $s \in S$ the section $t_{s}$ of $O_{X_{s}}(1)$ induced by $t$ is $O_{X_{s}}$-regular (which
implies, by *SGA* 1 IV 5.7, that $t$ is `O_X`-regular). Then the hypotheses made are stable under base extension
$S' \to S$ ($S'$ locally noetherian). Hence the conclusion remains valid after any base change.

## 3. Lefschetz theory for a projective morphism: existence theorem

<!-- label: XII.3 -->

**Theorem.**

<!-- label: XII.3.1 -->

[^N.D.E-XII-3]

Let $f: X \to S$ be a projective morphism, with $S$ noetherian, $O_{X}(1)$ an invertible module on $X$ ample relatively
to $S$, $X_{0}$ the subprescheme of zeros of a section $t$ of $O_{X}(1)$, $\hat{X}$ the formal completion of $X$ along
$X_{0}$, $\mathcal{F}$ a coherent module on $\hat{X}$, $\mathcal{F}_{0}$ the module that it induces on $X_{0}$. Suppose
moreover:

- a) $\mathcal{F}$ is flat with respect to $S$.
- b) For every $s \in S$, the section $t_{s}$ induced by $t$ on $X_{s}$ is $\mathcal{F}_{s}$-regular (which implies that
  $\mathcal{F}_{0}$ is also flat with respect to $S$, cf. *SGA* 1 IV 5.7).
- c) For every $s \in S$, $\mathcal{F}_{0,s}$ is of depth $\geqslant 2$ at the closed points of $X_{0,s}$.

Suppose moreover that $S$ admits an ample invertible sheaf. Under these conditions, there exists a coherent module $F$
on $X$ and an isomorphism of its formal completion $\hat{F}$ with $\mathcal{F}$.

This statement will follow from the following:

**Corollary.**

<!-- label: XII.3.2 -->

Under conditions a), b), c) above, one has the following:

1. <!-- original page 118 -->

    The module $\hat{f}_{\ast}(\mathcal{F})$ on $S$ is coherent; hence for every $n$, the module $\hat{f}_{\ast}(\mathcal{F}(n))$ on $S$ is coherent.

1. For $n$ large, the canonical homomorphism $\hat{f}*\hat{f}_{\ast}(\mathcal{F}(n)) \to \mathcal{F}(n)$ is surjective.

Let us admit the corollary for the moment, and prove 3.1. Thanks to the last hypothesis made in 3.1, one may reduce to
the case where $X = P^{r}_{S}$, by replacing $O_{X}(1)$, $t$ by a suitable power. I claim that one may moreover assume
that for every $s$, $t_{s} \neq 0$. Otherwise, indeed, one has $\mathcal{F}_{s} = 0$ by b), or what amounts to the same
by Nakayama, $\mathcal{F}_{0,s} = 0$ i.e. $s$ does not belong to the image of $Supp \mathcal{F}_{0}$ by the morphism
$f_{0}: X_{0} \to S$ induced by $f$. Now this image $S'$ is open by virtue of a), b), since $\mathcal{F}_{0}$ is flat
with respect to $S$; and it is obvious that it suffices to prove the conclusion of 3.1 in the situation obtained by
restricting above $S'$, since the coherent module $F'$ on $X|S'$ obtained will be the restriction of a coherent module
$F$ on $X$, which will answer the question. One may therefore assume that, in addition to hypotheses a), b), c), the
following hypotheses are also verified:

- a′) `O_X` is flat with respect to $S$.
- b′) For every $s \in S$, the section $t_{s}$ is $O_{X_{s}}$-regular.
- c′) For every $s \in S$, $O_{X_{0,s}}$ is of depth $\geqslant 2$ at the closed points of $X_{0,s}$.

(It suffices to choose $X = P^{r}_{S}$ with $r \geqslant 3$, which is permissible.)

Now 3.2 implies that one may find an epimorphism

$$
\hat{L} \to \mathcal{F} \to 0,
$$

<!-- label: eq:XII.3.17 -->

where $L$ is a module on $X$ of the form $f*(G)(-n)$, $G$ being a locally free coherent module on $S$: for $n$ large, it
suffices indeed to represent the coherent module $\hat{f}_{\ast}(\mathcal{F})$ on $S$ as a quotient of such a $G$. On
the other hand, the hypotheses a), b), c) on $f$, $t$ imply that $\hat{L}$ satisfies the same conditions a), b), c) as
$\mathcal{F}$. One concludes easily that the same holds for the kernel of (17), to which one may therefore apply the
same argument; so that $\mathcal{F}$ is represented as a cokernel of a homomorphism

$$
\hat{L}' \to \hat{L},
$$

<!-- label: eq:XII.3.18 -->

where $L$, $L'$ are locally free modules on $X$. Now by virtue of a′) and the second part of c′), and of 2.1 or 2.4 as
preferred, the homomorphism (18) comes from a homomorphism $L' \to L$ of modules on $X$. It suffices now to take for $F$
the cokernel of $L' \to L$, and one wins.

It remains to prove 3.2. This had been done in the seminar by a somewhat tedious expedient, consisting in interpreting
everything in terms of cohomology on the punctured projecting cone of $X$ relative to $S$, in order to reduce to Theorem
2.1. A more direct and more satisfactory way (although substantially the same) seems to me now the following. It
consists in noting that in IX, no. 2 (and with the notation of that exposé), the hypothesis that the morphism
$f: \mathcal{X} \to \mathcal{X}'$ be adic does not intervene anywhere in the proof of 2.1, via *EGA* 0_III 13.7.7; it
suffices to assume in its place that $\mathcal{X}$ is also adic, and to choose two ideals of definition $\mathcal{J}$
for $\mathcal{X}'$, $\mathcal{I}$ for $\mathcal{X}$, such that $\mathcal{J} O_{\mathcal{X}} \subset \mathcal{I}$, and to
define $\mathcal{S} = gr_{\mathcal{J}}(O_{\mathcal{X}'})$, and to consider $gr_{\mathcal{I}}(\mathcal{F})$. In any case,
2.1 may be applied directly to the morphism $\hat{f}: \hat{X} \to S$ considered in the present section, where one simply
takes $\mathcal{J} = 0$. Thus, to verify that $\hat{f}_{\ast}(\mathcal{F})$ is coherent, it suffices, by virtue of *loc.
cit.*, to verify that `Rⁱf₀_∗(gr_ℐ(ℱ))` is coherent on $S$ for $i = 0, 1$; for this one notes that by virtue of a) and
b), the module considered is none other than `⨁_{m⩾0} Rⁱf₀_∗(ℱ₀(−m))`, which is indeed coherent by virtue of hypothesis
c) and of 1.5.

This proves 3.2 (i). For 3.2 (ii), we shall need the following:

**Lemma.**

<!-- label: XII.3.3 -->

<!-- original page 119 -->

Under conditions a), b), c) of 3.1, set

```text
G_m = f̂_∗(ℱ(·)_m) = ⨁_n f_∗(ℱ_m(n)).
```

Then the projective system $(G_{m})$ satisfies the Mittag-Leffler condition.

One may assume $S$ affine, with ring $A$. Let $\mathcal{S}$ then be a finitely generated graded $A$-algebra with
positive degrees, and $t' \in \mathcal{S}_{1}$, such that $X$ immerses into $\operatorname{Proj}(\mathcal{S})$,
$O_{X}(1)$ being induced by $O(1)$ and the section $t$ being the image of $t'$. Equip $\mathcal{S}$ with the
$\mathcal{J}$-adic filtration, where $\mathcal{J} = t'\mathcal{S}$, and consider the projective system of the
$\mathcal{F}(\cdot)_{m}$ in the category of abelian sheaves on $X_{0}$. One is again under the preliminary conditions of
*EGA* 0_III 13.7.7[^XII-3-star] and moreover $H^{i}(X_{0}, gr(\mathcal{F}(\cdot)))$ is a finitely generated module on
$gr_{\mathcal{J}}(\mathcal{S})$ for $i = 0, 1$. Indeed, since $t'$ is $\mathcal{F}$-regular, one sees at once that as a
module on $(\mathcal{S}/t'\mathcal{S})[T]$ (of which $gr_{\mathcal{J}}(\mathcal{S})$ is a quotient), the module under
consideration is identified with
$H^{i}(X_{0}, \mathcal{F}_{0}(\cdot)) \otimes_{\mathcal{S}/t'\mathcal{S}} (\mathcal{S}/t'\mathcal{S})[T]$; now by virtue
of 1.5, $H^{i}(X_{0}, \mathcal{F}_{0}(\cdot))$ is finitely generated on $\mathcal{S}$, hence on
$\mathcal{S}/t'\mathcal{S}$, for $i = 0, 1$, which proves our assertion. Consequently one is under the conditions for
applying 0_III 13.7.7 with $n = 1$, which proves 3.3.

This point being acquired (and assuming $S$ still affine, which is permissible for proving 3.2 (ii)) let $m_{0}$ be such
that $m \geqslant m_{0}$ implies $Im(G_{m} \to G_{0}) = Im(G_{m_{0}} \to G_{0})$, so that both sides are also equal to
$Im(\lim G_{m} \to G_{0}) = Im(\hat{f}_{\ast}(\mathcal{F}(\cdot)) \to f_{\ast }\mathcal{F}_{0}(\cdot))$. Note now that
for $n$ large, $\mathcal{F}_{m_{0}}(n)$ is generated by its sections; hence $\mathcal{F}_{0}(n)$ is generated by
sections that lift to $\mathcal{F}_{m_{0}}$, and so (thanks to the choice of $m_{0}$) that lift to $\mathcal{F}$. So the
sections of $\mathcal{F}$ generate $\mathcal{F}_{0}$, hence also $\mathcal{F}$ thanks to Nakayama. This proves 3.2 (ii),
hence 3.1.

**Corollary.**

<!-- label: XII.3.4 -->

Let $f: X \to S$ be a flat projective morphism with $S$ locally noetherian, $O_{X}(1)$ an invertible module on $X$,
ample relatively to $S$, $t$ a section of this module such that for every $s \in S$ the section $t_{s}$ induced on the
fiber $X_{s}$ is $O_{X_{s}}$-regular, $X_{0}$ the subprescheme of zeros of $t$, $\hat{X}$ the formal completion of $X$
along $X_{0}$. Suppose that for every $s \in S$, $X_{0,s}$ is of depth $\geqslant 2$ at its closed points (i.e. $X_{s}$
is of depth $\geqslant 3$ at the closed points of $X_{0,s}$), and $X_{s}$ is of depth $\geqslant 2$ at its closed
points. Under these conditions, the pair $(X, X_{0})$ satisfies the effective Lefschetz condition (Leff) of paragraph 2
of Exposé X, i.e.:

1. <!-- original page 120 -->

    For every open neighborhood $U$ of $X_{0}$ in $X$, the functor

    ```text
    F ↦ F̂
    ```

    from the category of locally free coherent modules on $U$ to the category of locally free coherent modules on $\hat{X}$ is
    fully faithful.

1. For every locally free coherent module $\mathcal{F}$ on $\hat{X}$, there exists an open neighborhood $U$ of $X_{0}$,
   and a locally free coherent module $F$ on $U$ such that $\hat{F}$ is isomorphic to $\mathcal{F}$.

Indeed, a) has already been noted in 2.4 under weaker conditions. For b), one applies 3.1, which gives the conclusion,
at least if $S$ is noetherian and admits an absolutely ample invertible module, in particular if $S$ is affine. Indeed,
if $F$ is a coherent module on $X$ such that $\hat{F}$ is isomorphic to $\mathcal{F}$ and hence locally free, it follows
that $F$ is locally free on a neighborhood $U$ of $X_{0}$, and $F|U$ will satisfy the required condition. But let us now
note that by virtue of 2.5, for such an $F$, its image under the immersion $U \to X$ is coherent, and moreover is
independent of the chosen solution $(U, F)$ (taking into account the fact that two solutions coincide in a neighborhood
of $X_{0}$, by virtue of a)). Precisely, one may find a coherent module $F$ on $X$ and an isomorphism
$\hat{F} \xrightarrow{\sim} \mathcal{F}$ such that $F$ is of depth $\geqslant 2$ at every point of $X$ that is closed in
its fiber, and this determines $F$ up to a unique isomorphism. Thanks to this uniqueness property, the solutions of the
problem found by inducing above the affine open subsets of $S$ glue together, yielding a coherent $F$ on all of $X$ and
an isomorphism $\hat{F} \cong \mathcal{F}$. Restricting $F$ to the open subset $U$ of points where it is free, one finds
what one was looking for.

Thanks to 2.4 and 3.4, one may exploit, in the situation of a projective algebraic scheme and a "hyperplane section"
thereof, the general facts established in Exposés X and XI concerning the conditions (Lef) and (Leff). Thus:

**Corollary.**

<!-- label: XII.3.5 -->

Let $X$ be a projective algebraic scheme equipped with an ample invertible module $O_{X}(1)$, let $t$ be a section of
this module that is `O_X`-regular, and let $X_{0}$ be the subscheme of zeros of $t$. Suppose that $X$ is of depth
$\geqslant 2$ at its closed points (resp. and of depth $\geqslant 3$ at the closed points of $X_{0}$). Then
$\pi_{0}(X_{0}) \to \pi_{0}(X)$ is bijective, in particular $X$ is connected if and only if $X_{0}$ is, and choosing a
geometric base point in $X_{0}$, $\pi_{1}(X_{0}) \to \pi_{1}(X)$ is surjective, and more generally for every open subset
$U \supset X_{0}$, the homomorphism $\pi_{1}(X_{0}) \to \pi_{1}(U)$ is surjective (resp. the homomorphism
$\pi_{1}(X_{0}) \to \lim_{U} \pi_{1}(U)$ is bijective). In the respective case, if one assumes moreover that the local
ring of every closed point of $X$ not in $X_{0}$ is pure (3.2) (for example is regular, or only a complete
intersection), then $\pi_{1}(X_{0}) \to \pi_{1}(X)$ is an isomorphism.

One applies 2.4 and 3.4. One will note that in the respective case the hypothesis that $X$ be of depth $\geqslant 3$ at
the closed points of $X_{0}$ implies that all the irreducible components of dimension $\neq 0$ of $X$ are of dimension
$\geqslant 3$ (as one sees by noting that any such component necessarily meets $X_{0}$, and looking at a closed point of
the intersection).

**Remark.**

When $X$ is normal, of dimension $\geqslant 2$ at all its points, it is of depth $\geqslant 2$ at its closed points and
one is under the non-respective conditions of 3.5. In this case, one has a more elementary proof of the surjectivity of
$\pi_{1}(X_{0}) \to \pi_{1}(X)$ using Bertini's theorem (cf. *SGA* 1 X.2.10). If one assumes moreover $X_{0}$ normal,
and $X$ of dimension $\geqslant 3$ at all its points, then one is under the respective conditions of 3.5. In this case,
3.5 was established by Grauert (indeed, thanks to the normality hypothesis, one then succeeds in dispensing with the
existence theorem 3.1 by certain expedients). It is this proof of Grauert that was the starting point of the "Lefschetz
theory" that is the subject of the present seminar.

<!-- original page 121 -->

**Corollary.**

<!-- label: XII.3.6 -->

Let $X, O_{X}(1), t, X_{0}$ be as in 3.5. Suppose that $X$ is of depth $\geqslant 2$ at its closed points, and that

$$
H^{i}(X_{0}, O_{X_{0}}(-n)) = 0
$$

for $n > 0$ and for $i = 1$ (resp. for $i = 1$ and for $i = 2$), which implies by virtue of 1.4 that $X_{0}$ is of depth
$\geqslant 2$ (resp. $\geqslant 3$) at its closed points, i.e. that $X$ is of depth $\geqslant 3$ (resp. $\geqslant 4$)
at the closed points of $X_{0}$. Under these conditions, for every open neighborhood $U$ of $X_{0}$,
$\operatorname{Pic}(U) \to \operatorname{Pic}(X_{0})$ is injective, in particular
$\operatorname{Pic}(X) \to \operatorname{Pic}(X_{0})$ is injective (resp. `lim_U Pic(U) → Pic(X₀)` is bijective). In the
respective case, if one assumes moreover that the local ring of $X$ at every closed point not in $X_{0}$ is
parafactorial (3.1) (for example is regular, or more generally a complete intersection), then
$\operatorname{Pic}(X) \to \operatorname{Pic}(X_{0})$ is bijective.

One applies XI 3.12 and 3.13, noting that the respective hypothesis implies that the irreducible components of dimension
$\neq 0$ of $X$ are of dimension $\geqslant 4$. One finds in particular, by applying this to the case where $X$ is a
global complete intersection of dimension $\geqslant 4$ in projective space:

**Corollary.**

<!-- label: XII.3.7 -->

Let $X$ be an algebraic scheme of dimension $\geqslant 3$, which is a complete intersection in a scheme $P^{r}_{k}$.
Then $\operatorname{Pic}(X)$ is the free group generated by the class of the sheaf $O_{X}(1)$.

One reasons by induction on the number of hypersurfaces of which $X$ is the intersection, applying 3.6 and noting that
for a complete intersection $X$ of dimension $\geqslant 3$, one has $H^{i}(X, O_{X}(n)) = 0$ for $i = 1, 2$ and every
$n$.

**Remark.**

<!-- label: XII.3.8 -->

In the case where $X$ is a non-singular hypersurface, 3.7 is due to Andreotti. The result 3.7 may also be expressed
(when $X$ is non-singular) by saying that the homogeneous coordinate ring of $X$ is factorial, and in this form is
contained in XI 3.13 (ii). Let us also point out that Serre had given a proof of 3.7 in the non-singular case, by
transcendental means, using a specialization argument to reduce to the case of characteristic 0, where one has the
Lefschetz theorem in its classical form. Of course, the fact that the purely algebraic proof given here makes it
possible to dispense with non-singularity hypotheses in the statement of Lefschetz's theorem invites one to reconsider
the latter also in the classical case. Cf. the following exposé, which proposes conjectures in this direction.

<!-- original page 122 -->

In Corollaries 3.5 and 3.7 we have placed ourselves over a base field, whereas the key theorems 2.4 and 3.4 are valid
over an arbitrary base. To generalize Corollaries 3.5 and 3.6 to a general $S$, we must give serviceable criteria for a
point of $X$ (flat over $S$) to have a "pure" or, respectively, parafactorial local ring. This will be the object of the
following section.

## 4. Formal completion and normal flatness

<!-- label: XII.4 -->

**Theorem.**

<!-- label: XII.4.1 -->

Let $X$ be a locally noetherian prescheme, locally immersible in a regular scheme, $Y$ a closed part of $X$,
$U = X - Y$, $X_{0}$ a closed subprescheme of $X$ defined by an ideal $\mathcal{J}$, $\hat{X}$ the formal completion of
$X$ along $X_{0}$, $U_{0}$ the trace of $X_{0}$ on $U$, `Û` the formal completion of $U$ along $U_{0}$, $i: U \to X$ and
$\hat{i}: \hat{U} \to \hat{X}$ the canonical immersions, $n$ an integer. Suppose:

- a) $X$ is normally flat along $X_{0}$ at the points of $Y \cap X_{0}$, i.e. at these points the modules
  $\mathcal{J}^{n}/\mathcal{J}^{n+1}$ on $X_{0}$ are flat, i.e. locally free.
- b) For every $x \in Y \cap X_{0}$, one has $prof O_{X_{0},x} \geqslant n + 2$.

Under these conditions, one has the following:

1. Let $F$ be a coherent module on $U$; suppose that one has:

    - c) For every $x \in Y - Y \cap X_{0}$, one has $prof O_{X,x} \geqslant n + 2$.
    - d) $F$ is free at the points of $U_{0}$, and of depth $\geqslant n + 1$ at every point of $U$ where it is not
      free.

    Then the graded module

    ```text
    ⨁_{m⩾0} Rᵖi_∗(𝒥ᵐF)
    ```

    on $\bigoplus_{m\geqslant 0} \mathcal{J}^{m}$ is finitely generated for $p \leqslant n$.

1. Let $F$ be a coherent module on `Û`. Then the graded module

    ```text
    ⨁_{m⩾0} Rᵖi_∗(𝒥ᵐF/𝒥^{m+1}F)
    ```

    on $\bigoplus_{m\geqslant 0} \mathcal{J}^{m}/\mathcal{J}^{m+1} = gr_{\mathcal{J}}(O_{X})$ is finitely generated for $p \leqslant n$.

*Proof.*

(1) Let $X' = \operatorname{Spec}(\bigoplus_{m\geqslant 0} \mathcal{J}^{m})$; the base change $f: X' \to X$ then defines
$U' = X' - Y'$, $X'_{0}$, $U'_{0} = X'_{0} \cap U'$, and immersions $i': U' \to X'$, $i'_{0}: U'_{0} \to X'_{0}$. One
has therefore a cartesian square

```text
       i′
X′ ←──── U′
│         │
f│         │g
↓    i    ↓
X ←────── U
```

and one has

```text
⨁_{m⩾0} Rᵖi_∗(𝒥ᵐF) = Rᵖi_∗(⨁_{m⩾0} 𝒥ᵐF) = Rᵖi_∗(g_∗(F′)),
```

<!-- label: eq:XII.4.19 -->

<!-- original page 123 -->

where $F' = g*F$, so that one has indeed a canonical isomorphism

$$
g_{\ast}(F') \xrightarrow{\sim} \bigoplus_{m\geqslant 0} \mathcal{J}^{m}F,
$$

since this is true at the points of $U_{0}$, due to the fact that $F$ is free there by virtue of d), and also at the
points outside $U_{0}$, due to the fact that there one has $\mathcal{J}^{m} = O_{U}$ (so that in both cases,
$\mathcal{J}^{m} \otimes_{O_{U}} F \to \mathcal{J}^{m}F$ is an isomorphism).

On the other hand, since $f$ and consequently $g$ are affine, one has

```text
Rᵖi_∗(g_∗(F′)) = Rᵖ(ig)_∗(F′) = Rᵖ(fi′)_∗(F′) = f_∗(Rᵖi′_∗(F′)),
```

<!-- label: eq:XII.4.20 -->

so comparing (19) and (20), one sees that assertion (1) is equivalent to the following: $R^{p}i'_{\ast}(F')$ is a
finitely generated module, i.e. coherent on $X'$, for every $p \leqslant n$. Now since $X$ is locally immersible in a
regular scheme, the same holds of $X'$, which is of finite type over $X$, and one may apply the coherence criterion VIII
2.3 to a coherent extension $F''$ of $F'$: one wants to express that $H^{p}_{Y'}(F'')$ is coherent for
$p \leqslant n + 1$, and this is also equivalent to saying that for every $x' \in U'$ such that

$$
codim({x'} \cap Y', {x'}) = 1,
$$

<!-- label: eq:XII.4.20bis -->

one has

$$
prof F'_{x'} \geqslant n + 1.
$$

<!-- label: eq:XII.4.21 -->

Now this condition is verified at the points $x'$ where $F'$ is not free, since for such an $x'$ one has
$x' \notin U'_{0}$ by virtue of d), so $g$ is an isomorphism there, and by virtue of d) again, $F$ is of depth
$\geqslant n + 1$ at $g(x')$, so $F'$ is of depth $\geqslant n + 1$ at $x'$. It therefore suffices to verify condition
(21) at the $x' \in U'$ satisfying (20 bis) and at which $F'$ is free. For this, it suffices to prove that one has

$$
prof O_{X',x'} \geqslant n + 1
$$

<!-- label: eq:XII.4.21bis -->

at these points, *a fortiori* it suffices to establish that one has this relation at all points $x'$ of $U'$ satisfying
(20 bis). Now, again by virtue of criterion 2.3 of Exposé VIII, this is equivalent to the assertion that the modules

```text
Hᵖ_{Y′}(O_{X′}) for p ⩽ n + 1
```

are coherent. In fact, we are going to prove that they are even zero, or what amounts to the same by virtue of Exposé
III, that one has

```text
prof O_{X′,x′} ⩾ n + 2 for every x′ ∈ Y′.
```

<!-- label: eq:XII.4.22 -->

<!-- original page 124 -->

For this, we distinguish two cases. If $x' \notin X'_{0}$, then $f$ is an immersion at $x'$, and it is necessary to
verify that $F$ is of depth $\geqslant n + 2$ at the image $x = f(x')$, which is none other than condition c). If on the
contrary $x' \in X'_{0}$, i.e. $x = f(x') \in X_{0}$ so $x \in Y \cap X_{0}$, one applies conditions a) and b) thanks to
the following:

**Lemma.**

<!-- label: XII.4.2 -->

Let $X$ be a locally noetherian prescheme, $X_{0}$ a closed subprescheme of $X$ defined by an ideal $\mathcal{J}$,
$X' = \operatorname{Spec}(\bigoplus_{m\geqslant 0} \mathcal{J}^{m})$,
$X'_{0} = \operatorname{Spec}(\bigoplus_{m\geqslant 0} \mathcal{J}^{m}/\mathcal{J}^{m+1}) = X' \times_{X} X_{0}$, $x$ a
point of $X_{0}$ at which $X$ is normally flat along $X_{0}$, i.e. such that
$gr_{\mathcal{J}}(O_{X}) = \bigoplus_{m\geqslant 0} \mathcal{J}^{m}/\mathcal{J}^{m+1}$ is flat there as a module on
$X_{0}$. Then for any sequence of elements $f_{i} (1 \leqslant i \leqslant m)$ of $O_{X,x}$ whose images in
$O_{X_{0},x}$ form an $O_{X_{0},x}$-regular sequence, and for every $x' \in X'$ above $x$, the images of the $f_{i}$ in
$O_{X',x'}$ (resp. in $O_{X'_{0},x'}$) form respectively an $O_{X',x'}$-regular sequence (resp. an
$O_{X'_{0},x'}$-regular sequence); in particular one has

```text
prof O_{X′,x′} ⩾ prof O_{X₀,x},  prof O_{X′₀,x′} ⩾ prof O_{X₀,x}.
```

<!-- label: eq:XII.4.23 -->

To prove this, one may assume that $X$ is local with closed point $x$, hence affine of ring $A = O_{X,x}$, $\mathcal{J}$
being defined by an ideal $J$; and it suffices to prove that for any sequence $f_{i} (1 \leqslant i \leqslant m)$ of
elements of $A$ whose images in $A/J$ form an $A/J$-regular sequence, the $f_{i}$ form an
$(\bigoplus_{m\geqslant 0} J^{m})$-regular sequence and an $(\bigoplus_{m\geqslant 0} J^{m}/J^{m+1})$-regular sequence,
i.e. for every $m$, they form a `Jᵐ`-regular sequence and a $J^{m}/J^{m+1}$-regular sequence. The second assertion is
trivial, since $J^{m}/J^{m+1}$ is a free module on $A/J$. The first follows by looking at the $J$-adic filtration of
`Jᵐ` and noting that, for the graded module associated with `Jᵐ` for this filtration, the sequence of the $f_{i}$ is
regular.

This proves 4.2 and consequently 4.1, (1).

Let us prove 4.1, (2). For this, let us use the cartesian square

```text
        i′₀
X′₀ ←────── U′₀
│            │
f₀│            │g₀
↓     i₀     ↓
X₀ ←──────── U₀
```

and proceeding as at the beginning of the proof of (1), one finds that

```text
⨁_{m⩾0} Rᵖi_∗(𝒥ᵐF/𝒥^{m+1}F) ≅ f₀_∗(Rᵖi′₀_∗(F′₀)),
```

<!-- label: eq:XII.4.24 -->

where $F_{0} = F/\mathcal{J}F$ and $F'_{0} = g_{0}*(F_{0})$ (using the fact that $F$ is locally free). Hence the
conclusion of (2) amounts to saying that for $p \leqslant n$, `Rᵖi′₀_∗(F′₀)` is a coherent module.

Here again, taking into account that $F'_{0}$ is locally free, criterion VIII 2.3 lets us reduce to proving that this is
so when one replaces $F'_{0}$ by $O_{U'_{0}}$, i.e. to proving that the modules

```text
Hᵖ_{Y′₀}(O_{X′₀}) for p ⩽ n + 1  (where Y′₀ = Y′ ∩ X′₀ = X′₀ − U′₀)
```

<!-- original page 125 -->

are coherent. One proves again that they are in fact zero, i.e. that one has

```text
prof O_{X′₀,x′} ⩾ n + 2 for every x′ ∈ Y′₀.
```

<!-- label: eq:XII.4.25 -->

Now this indeed follows from conditions a) and b), taking into account 4.2. This completes the proof of 4.1.

**Remark.**

<!-- label: XII.4.3 -->

One sees at once, by descent, that the hypothesis: $X$ locally immersible in a regular scheme, may be replaced by the
following weaker one: there exists a morphism $\bar{X} \to X$, faithfully flat and quasi-compact, such that $\bar{X}$ is
locally immersible in a regular scheme.

Theorem 4.1 puts us in a position to apply the results of Exposé IX (comparison and existence theorems). We shall be
particularly interested in the following:

**Corollary.**

<!-- label: XII.4.4 -->

Suppose conditions a), b), c) of Theorem 4.1 verified, with $n = 1$, and $X = \operatorname{Spec}(A)$, $A$ being
separated and complete for the $\mathcal{J}$-adic topology. Then:

1. The functor $F \mapsto \hat{F}$ from the category of locally free coherent modules on $U$ to the category of locally
   free coherent modules on `Û` is fully faithful.
1. For every locally free coherent module $\mathcal{F}$ on `Û`, there exists a coherent module $F$ on $U$ and an
   isomorphism $\hat{F} \xrightarrow{\sim} \mathcal{F}$.

In particular, if for every $x \in U$ whose closure in $U$ does not meet $U_{0}$, i.e. such that
${x} \cap X_{0} \subset Y$, one has $prof O_{U,x} \geqslant 2$, then the pair $(U, U_{0})$ satisfies the effective
Lefschetz condition (Leff) of Exposé X.

(For the last assertion, one proceeds as in X 2.1.)

A particular case of 4.4:

**Corollary.**

<!-- label: XII.4.5 -->

Let $A$ be a noetherian ring, $J$ an ideal of $A$ contained in the radical, $A_{0} = A/J$. Suppose

1. $prof A_{0} \geqslant 3$.
1. $gr_{J}(A)$ is a free $A_{0}$-module.
1. $A$ is complete for the $J$-adic topology.

Let $X = \operatorname{Spec}(A)$, $X_{0} = \operatorname{Spec}(A_{0}) = V(J)$, $a$ the closed point of $X$,
$U = X - {a}$, $U_{0} = X_{0} - {a}$, `Û` the formal completion of $U$ along $U_{0}$. Then the functor
$F \mapsto \hat{F}$ from the category of locally free coherent modules on $U$ to the category of locally free coherent
modules on `Û` is fully faithful. Moreover, for every locally free coherent module $\mathcal{F}$ on `Û`, there exists a
coherent module (not necessarily locally free!) $F$ on $U$, and an isomorphism $\hat{F} \cong \mathcal{F}$.

One will note that thanks to 4.3, we did not have to suppose that $A$ is a quotient of a regular ring, since the
completion of $A$ for the $\mathfrak{r}(A)$-adic topology satisfies this condition in any case.

Proceeding as in Exposés X and XI, one concludes from 4.5:

**Corollary.**

<!-- label: XII.4.6 -->

Under the conditions of 4.5, one has the following:

- a) $U$ and $U_{0}$ are connected (III 3.1).

    Choosing a geometric base point in $U_{0}$, the homomorphism

    ```text
    π₁(U₀) → π₁(U)
    ```

    is surjective.

- b) The homomorphism

    ```text
    Pic(U) → Pic(U₀)
    ```

    is injective.

<!-- original page 126 -->

To prove b), taking 4.5 into account, this amounts to verifying that any isomorphism $L'_{0} \xrightarrow{\sim} L_{0}$
lifts to an isomorphism $\hat{L}' \xrightarrow{\sim} \hat{L}$. Now for this one lifts step by step to isomorphisms
$L'_{n} \xrightarrow{\sim} L_{n}$; the obstructions lie in $H^{1}(U_{0}, \mathcal{J}^{n}/\mathcal{J}^{n+1})$, and these
modules are zero because $J^{n}/J^{n+1}$ is free and $prof A_{0} \geqslant 3$.

We are now in a position to prove the following:

**Theorem.**

<!-- label: XII.4.7 -->

Let $A$ be a noetherian local ring, $J$ an ideal of $A$ contained in its radical, $A_{0} = A/J$. Suppose

1. $prof A_{0} \geqslant 3$.
1. $gr_{J}(A)$ is a free module on $A_{0}$.

Then, if $A_{0}$ is "pure" (X 3.1) (resp. parafactorial (XI 3.1)), so is $A$.

*Proof.*

By descent, one may assume that one also has

1. $A$ is complete for the $J$-adic topology.

Indeed, by virtue of (i) and (ii), one has $prof(A) \geqslant 3$, hence $prof(\hat{A}) \geqslant 3$, where `Â` is the
completion of $A$ for the $J$-adic topology, and one applies X 3.6 and XI 3.6. One is therefore under the conditions of
4.5. Since $prof(A) \geqslant 3 \geqslant 2$, to say that $A$ is parafactorial means simply that
$\operatorname{Pic}(U) = 0$, and by virtue of 4.6 b) it suffices for this that $\operatorname{Pic}(U_{0}) = 0$, i.e.
that $A_{0}$ be parafactorial. To prove that $A$ is "pure" if $A_{0}$ is, one needs to prove that if $V$ is an étale
cover of $U$, defined by an algebra $B$ on $U$, then $H^{0}(U, B)$ is a finite étale algebra over $A$. Now $A_{0}$ being
pure, the same holds of the $A_{n}$ (which differ from it only by nilpotent elements), so for every $n$,
$B_{n} = H^{0}(U, B_{n})$ is an étale algebra over $A/J^{n+1}$, and these algebras of course glue, so that $\lim B_{n}$
is an étale algebra over $A$. Now by virtue of 4.5, this algebra is none other than $H^{0}(U, B)$, which establishes our
assertion.

**Corollary.**

<!-- label: XII.4.8 -->

Let $f: X \to Y$ be a flat morphism of locally noetherian preschemes, $x \in X$, $y = f(x)$; suppose that $O_{X_{y},x}$
is a "pure" (resp. parafactorial) local ring of depth $\geqslant 3$. Then the same holds for $O_{X,x}$.

This is the result of the type promised at the end of the preceding section, in order to generalize Corollaries 3.5 and
following. One thus finds, using 3.4, the following:

**Corollary.**

<!-- label: XII.4.9 -->

<!-- original page 127 -->

Let $f: X \to S$ be a flat projective morphism with $S$ locally noetherian, $O_{X}(1)$ an invertible module on $X$ ample
with respect to $S$, $t$ a section of $O_{X}(1)$ such that for every $s \in S$ the section $t_{s}$ induced on $X_{s}$ is
$O_{X_{s}}$-regular, $X_{0}$ the subscheme of zeros of $t$, $X_{m}$ the subscheme of zeros of $t^{m+1}$. Suppose that
for every $s \in S$, $X_{s}$ is of depth $\geqslant 3$ at all its closed points. Then:

- a) If the local rings of the closed points of $X_{s} - X_{0,s}$ ($s \in S$) are "pure", for example are complete
  intersections, then the functor $X' \mapsto X'_{0} = X' \times_{X} X_{0}$ from the category of étale covers of $X$ to
  the category of étale covers of $X_{0}$ is an equivalence of categories; in particular, choosing a geometric base
  point in $X_{0}$, the homomorphism

    ```text
    π₁(X₀) → π₁(X)
    ```

    is an isomorphism.[^N.D.E-XII-4]

- b) If the local rings of the closed points of $X_{s} - X_{0,s}$ ($s \in S$) are "parafactorial", for example regular,
  or complete intersections of dimension $\geqslant 4$, then for every integer $m$ such that `Rⁱf₀_∗(O_{X₀}(−n)) = 0`
  for $n > m$ and $i = 1, 2$, the map $\operatorname{Pic}(X) \to \operatorname{Pic}(X_{m})$ is bijective.

Moreover, if $S$ is noetherian and the $X_{0,s}$ are of depth $\geqslant 3$ at their closed points, there exist such $m$
(cf. 1.5).

**Remark.**

<!-- label: XII.4.10 -->

Under the conditions of the last assertion of 4.9 b), one has seen in 1.5 that there exists an $m$ such that $n > m$
implies even $H^{i}(X_{0}, O_{X_{0}}(-n)) = 0$ for $i = 1, 2$ (and even for $i \leqslant 2$). This condition is stronger
than $R^{i}f_{\ast}(O_{X_{0}}(-n)) = 0$ for $i = 1, 2$, and it has moreover the advantage of being stable under base
change. The same holds of the depth hypotheses made in 4.9, and also of a hypothesis of the type "the $X_{s}$ are
locally complete intersections". It then follows, under these conditions, that 4.9 b) also implies that the functor
morphism

$$
\operatorname{Pic}_{X/S} \to \operatorname{Pic}_{X_{n}/S}
$$

in $Sch/S$ is an isomorphism, hence also the morphism for the relative Picard schemes, when these exist:

$$
\operatorname{Pic}_{X/S} \to \operatorname{Pic}_{X_{n}/S}.
$$

Even in the case where $S$ is the spectrum of an algebraically closed field, this statement is markedly more precise
than the statement saying merely that $\operatorname{Pic}(X) \to \operatorname{Pic}(X_{n})$ is bijective.

<!-- original page 128 -->

One may ask whether one can always take $n = 0$ in the preceding conclusions (assuming therefore the $X_{0,s}$ of depth
$\geqslant 3$ at their closed points). When $X_{0}$ is smooth over $S$ and the residue characteristics of $S$ are zero,
this is indeed so, by virtue of Kodaira's "vanishing theorem" (proved by transcendental means, using a Kählerian metric)
which implies that for every smooth connected projective scheme of dimension $n$ over a field $k$ of characteristic
zero, and every ample invertible module $L$ on $X$, one has $H^{i}(X, L^{-1}) = 0$ for $i \neq n$. It is not
known[^N.D.E-XII-5] at present whether this theorem may be replaced by a generalization in characteristic $p > 0$, and
whether the smoothness hypothesis may be replaced by a hypothesis of a more general nature (bearing on depth, or of
"complete intersection" type ...).

## 5. Universal finiteness conditions for a non-proper morphism

<!-- label: XII.5 -->

Let us recall for the record the following:

**Proposition.**

<!-- label: XII.5.1 -->

Let $f: X \to S$ be a proper morphism of preschemes with $S$ locally noetherian, $U$ an open part of $X$, $g: U \to X$
the canonical immersion, $h = fg: U \to S$, $F$ a module on $U$. Suppose that the modules $R^{i}g_{\ast}(F)$ are
coherent for $i \leqslant n$ (a hypothesis of local nature on $X$, which is verified in practice using criterion VIII
2.3). Then $R^{i}h_{\ast}(F)$ is coherent for $i \leqslant n$.

This follows at once from the Leray spectral sequence

$$
E^{p,q}_{2} = R^{p}f_{\ast}(R^{qg}_{\ast}(F)) \Rightarrow R^{\ast }h_{\ast}(F),
$$

<!-- label: eq:XII.5.26 -->

and from the fact that the higher direct images by $f$ of a coherent module on $X$ are coherent (*EGA* III 3.2.1).

**Proposition.**

<!-- label: XII.5.2 -->

<!-- original page 129 -->

Let $S$ be a locally noetherian prescheme, $\mathcal{S}$ a quasi-coherent graded algebra of finite type on $S$,
generated by $\mathcal{S}_{1}$, $X$ a subprescheme of $\operatorname{Proj}(\mathcal{S})$, $O_{X}(1)$ the invertible
module on $X$ very ample relatively to $S$ induced by $\operatorname{Proj}(\mathcal{S}(1))$, $U$ an open part of $X$,
$g: U \to X$ the canonical immersion, $h = fg: U \to S$, $F$ a quasi-coherent module on $U$, whence twisted modules
$F(m) = F \otimes O_{X}(m)$ ($m \in \mathbb{Z}$), $n$ an integer, $m_{0}$ an integer. The following conditions are
equivalent:

1. $R^{i}g_{\ast}(F)$ is coherent for $i \leqslant n$.
1. $\bigoplus_{m>m_{0}} R^{i}h_{\ast}(F(m))$ is a finitely generated $\mathcal{S}$-module for $i \leqslant n$.

*Proof.*

Replacing $F$ by $F(m)$ in the spectral sequence above one finds a spectral sequence of graded $\mathcal{S}$-modules

```text
E₂^{p,q} = ⨁_{m⩾m₀} Rᵖf_∗(R^qg_∗(F(m))) ⇒ ⨁_{m⩾m₀} R^∗h_∗(F(m)).
```

Since one has

$$
R^{qg}_{\ast}(F(m)) \cong R^{qg}_{\ast}(F)(m),
$$

one sees that if the $R^{i}g_{\ast}(F)$ are coherent, $E^{p,q}_{2}$ is finitely generated on $\mathcal{S}$ for
$q \leqslant n$, thanks to part a) of Lemma 5.3 below, which implies that the abutment is finitely generated on
$\mathcal{S}$ in degree $i \leqslant n$. This proves (i) ⇒ (ii). Moreover, reasoning in the abelian category of graded
$\mathcal{S}$-modules modulo the thick subcategory $C$ of those that are quasi-coherent of finite type, one finds by the
preceding spectral sequence

```text
⨁_{m⩾m₀} R^{n+1}h_∗(F(m)) ≅ ⨁_{m⩾m₀} f_∗(R^{n+1}g_∗(F)(m)) mod C,
```

which proves that if the left-hand side is a finitely generated $\mathcal{S}$-module, then $R^{n+1}g_{\ast}(F)$ is
coherent, by virtue of part b) of Lemma 5.3. This proves the implication (ii) ⇒ (i) by induction on $n$. It remains to
prove:

**Lemma.**

<!-- label: XII.5.3 -->

Let $S$, $\mathcal{S}$, $X$, $f$ be as in 5.2, and $G$ a quasi-coherent module on $X$, $m_{0}$ an integer. Then:

- a) If $G$ is coherent, then for every integer $i$, the graded module

    ```text
    ⨁_{m⩾m₀} Rⁱf_∗(G(m))
    ```

    on $\mathcal{S}$ is finitely generated.

- b) Conversely, suppose that the module $\bigoplus_{m\geqslant m_{0}} R^{i}f_{\ast}(G(m))$ on $\mathcal{S}$ is finitely
  generated; then $G$ is coherent.

*Proof of 5.3.*

For a), the case $i = 0$ is given in *EGA* III 2.3.2; the case $i > 0$ follows from *EGA* III 2.2.1 (i)(ii), which says
that the $R^{i}f_{\ast} G(m)$ are coherent, and zero for $m$ large (if one assumes $S$ noetherian, which is
permissible).

<!-- original page 130 -->

For b), one notes that $G$ is isomorphic to $\operatorname{Proj}(\bigoplus_{m\geqslant m_{0}} f_{\ast}(G(m)))$ (*EGA* II
3.4.4 and 3.4.2), which proves that $G$ is coherent if $\bigoplus_{m\geqslant m_{0}} f_{\ast}(G(m))$ is finitely
generated on $\mathcal{S}$, by virtue of *loc. cit.* 3.4.4.

**Corollary.**

<!-- label: XII.5.4 -->

($S$ noetherian.) Suppose that $R^{i}g_{\ast}(F)$ is coherent for $i \leqslant n$; then for $i \leqslant n + 1$ and $m$
large, one has a canonical isomorphism:

$$
R^{i}h_{\ast}(F(m)) \cong f_{\ast}(R^{i}g_{\ast}(F)(m)).
$$

Indeed the spectral sequence (26) for $F(m)$ then degenerates in degree $\leqslant n$, by *EGA* III 2.2.1 (ii), whence
at once the result (which moreover recovers the implication (ii) ⇒ (i) of 5.2).

**Corollary.**

<!-- label: XII.5.5 -->

Under the preliminary conditions of 5.2, $S$ noetherian, the following conditions are equivalent:

1. $\bigoplus_{m\geqslant m_{0}} h_{\ast}(F(m))$ is finitely generated on $\mathcal{S}$, and $R^{i}h_{\ast}(F(m)) = 0$
   for $0 < i \leqslant n$ and $m$ large.
1. $g_{\ast}(F)$ is coherent, and $R^{i}g_{\ast}(F) = 0$ for $0 < i \leqslant n$.
1. (ii bis) $g_{\ast}(F)$ is coherent, and $prof_{Y} g_{\ast}(F) > n + 1$.

The equivalence of (ii) and (ii bis) is contained in III 3.3. Moreover, by virtue of 5.2 conditions (i) and (ii) both
imply that the $R^{i}g_{\ast}(F)$ ($i \leqslant n$) are coherent. The equivalence of (i) and (ii) then follows from 5.4,
taking into account the fact that for a coherent module $G$ on $X$, one has $G = 0$ if and only if $f_{\ast}(G(m)) = 0$
for $m$ large, for instance by virtue of *EGA* III 2.2.1 (iii).

**Remark.**

<!-- label: XII.5.6 -->

One may interpret criteria 5.2 and 5.5 by saying that the "simultaneous finiteness condition" 5.2 (ii) is expressed by
properties of local regularity (in terms of depth, thanks to VIII 2.1) of $F$ at the points of $U$ neighboring
$Y = X - U$, whereas the "asymptotic vanishing condition" 5.5 (i) is of a markedly stronger nature, and is expressed by
conditions of local regularity of $g_{\ast}(F)$ at the points of $Y$ itself. It would be interesting, in order to
generalize the Lefschetz-type theorems for projective morphisms to quasi-projective morphisms, to find local criteria on
$X$ necessary and sufficient for the $\mathcal{S}$-modules $\bigoplus_{m\geqslant 0} R^{i}h_{\ast}(F(m))$ for
$i \leqslant n$ to be finitely generated. When $S$ is the spectrum of a field (and doubtless more generally, when it is
the spectrum of an artinian ring) and $Y = X - U$ is finite, one can show that it is necessary and sufficient that the
following conditions be verified:

<!-- original page 131 -->

1. $prof F_{x} > n$ for every closed point $x$ of $U$ (compare 1.4).
1. $R^{i}g_{\ast}(F)$ is coherent for $i \leqslant n$, or what amounts to the same, there exists an open neighborhood
   $V$ of $Y$ such that for every closed point $x$ of $U \cap V$, one has $prof F_{x} > n + 1$.

**Proposition.**

<!-- label: XII.5.7 -->

Let $S$ be a locally noetherian prescheme, $g: U \to X$ a morphism of preschemes of finite type over $S$,[^XII-5-star]
with structural morphisms $h$ and $f$, $F$ a quasi-coherent module on $U$, $n$ an integer. The following conditions are
equivalent:

1. For every base change $S' \to S$ with $S'$ noetherian, the module $R^{n}g'_{\ast}(F')$ on $X'$ is coherent.

1. For every base change as above, and every coherent ideal $J$ on $S'$, denoting by $\mathcal{I}$ the ideal $J O_{X'}$
   on $X'$, the graded module

    ```text
    ⨁_{m⩾0} Rⁿg′_∗(ℐᵐF′)
    ```

    on $\bigoplus_{m\geqslant 0} \mathcal{I}^{m}$ is finitely generated.

1. For every base change $S' \to S$, and $J$ as above, the graded module

    ```text
    ⨁_{m⩾0} Rⁿg′_∗(ℐᵐF′/ℐ^{m+1}F′)
    ```

    on $gr_{\mathcal{I}}(O_{X'}) = \bigoplus_{m\geqslant 0} \mathcal{I}^{m}/\mathcal{I}^{m+1}$ is finitely generated.

Plainly (ii) ⇒ (i) and (iii) ⇒ (i), as one sees by setting $\mathcal{I} = 0$ in conditions (ii) and (iii). The reverse
implications are obtained by applying (i) to the composite base change $S'' \to S' \to S$, where $S''$ is equal to
$\operatorname{Spec}(\bigoplus_{m\geqslant 0} J^{m})$ resp.
$\operatorname{Spec}(\bigoplus_{m\geqslant 0} J^{m}/J^{m+1})$.

The interest of this proposition is that conditions of form (ii) are those that intervene in the "algebraic-formal
comparison theorems", whereas conditions of form (iii) intervene in the "existence theorems" that complement them, cf.
Exposé IX. A first interesting case is the one where $f: X \to S$ is the identity, and where it is therefore a question
of conditions on a morphism $h: U \to S$ locally of finite type and a quasi-coherent module $F$ on $U$ flat with respect
to $S$. To obtain sufficient conditions, we are going to assume that $U$ embeds, via $g: U \to X$, as an open
subprescheme of an $X$ proper over $S$. Applying 5.1, one sees therefore:

**Corollary.**

<!-- label: XII.5.8 -->

Let $f: X \to S$ be a proper morphism with $S$ locally noetherian, $U$ an open subset of $X$, $g: U \to X$ the canonical
immersion, $h = fg: U \to S$, $F$ a quasi-coherent module on $X$, flat with respect to $S$. Suppose that for every base
change $S' \to S$ with $S'$ locally noetherian, one has $R^{i}g'_{\ast}(F')$ coherent on $X'$ for $i \leqslant n$. Then
one has the following:

1. For every base change $S' \to S$ with $S'$ locally noetherian, $R^{i}h'_{\ast}(F')$ is coherent on $S'$ for
   $i \leqslant n$.

1. For every $S' \to S$ as above, and every coherent ideal $J$ on $S'$, the graded modules

    ```text
    ⨁_{m⩾0} Rⁱh′_∗(JᵐF′)
    ```

    <!-- original page 132 -->

    on $\bigoplus_{m\geqslant 0} J^{m}$ are finitely generated for $i \leqslant n$.

1. For every $S' \to S$ and $J$ as above, the graded modules

    ```text
    ⨁_{m⩾0} Rⁱh′_∗(JᵐF′/J^{m+1}F′)
    ```

    on $gr_{J}(O_{S'}) = \bigoplus_{m\geqslant 0} J^{m}/J^{m+1}$ are finitely generated for $i \leqslant n$.

Moreover, under the conditions of (ii), and by virtue of the comparison theorem 1.1, denoting by $\hat{S}'$ the formal
completion of $S'$ along $J$ and by $\hat{U}'$ that of $U'$ along $J O_{U'}$, the canonical homomorphisms

```text
R̂ⁱh′_∗(F′) → Rⁱĥ′_∗(F̂′) → lim_k Rⁱh′_∗(F′_k)
```

are isomorphisms for $i \leqslant n - 1$.

**Remark.**

<!-- label: XII.5.9 -->

Suppose moreover under the conditions of 5.8 with $F$ coherent, and consider a base change $S' \to S$ as in 5.9 (i).
Suppose moreover that $S'$ is locally immersible in a regular scheme, or more generally, that there exists a morphism
$S'' \to S'$ faithfully flat and quasi-compact such that $S''$ is locally immersible in a regular scheme; this condition
is verified in particular if $S'$ is local. Then the conclusion of 5.8 (i) and (ii) remains valid when $F'$ is replaced
by a module $G'$ on $U'$ such that every point of $U'$ has an open neighborhood on which $G'$ is isomorphic to a module
of the form $F'^{n}$. Indeed, one is reduced to the case where $S'$ itself is locally immersible in a regular scheme, so
that the same holds of $S'' = \operatorname{Spec}(\bigoplus_{m\geqslant 0} J^{m})$ and of
$X'' = X' \times_{S'} S'' = X \times_{S} S''$, which are of finite type over it. One then applies the finiteness
criterion VIII 2.3 to the direct images for $i \leqslant n$ of $G''$ under the immersion $U'' \to X''$, noting that they
are satisfied by hypothesis for $F''$, hence also for $G''$, since they are expressed in terms of depth and $G''$ is
locally isomorphic to a $F''^{n}$. The same argument shows that if $\mathcal{G}'$ is a coherent module on $\hat{U}'$
(completion of $U'$ along the ideal $J O_{U'}$) such that $\mathcal{G}'_{0} = \mathcal{G}'/J \mathcal{G}'$ is locally of
the form $F'^{n}_{0}$, then the conclusion of (iii) remains valid when $F'$ is replaced there by $\mathcal{G}'$. One
thus obtains the following result, using the results of Exposé IX:

**Corollary.**

<!-- label: XII.5.10 -->

Let $f: X \to S$ be a proper morphism with $S$ locally noetherian, $U$ an open part of $X$; suppose $U$ flat with
respect to $S$, and that for every base change $S' \to S$ with $S'$ locally noetherian, one has $R^{i}g'_{\ast}(O_{U'})$
coherent on $X'$ for $i = 0, 1$. Suppose then that $S'$ is of the form $\operatorname{Spec}(A)$, where $A$ is a
noetherian ring equipped with an ideal $J$ such that $A$ is separated and complete for the $J$-adic topology. Under
these conditions:

1. The functor $F \mapsto \hat{F}$ from the category of locally free modules on $U'$ to the category of locally free
   modules on $\hat{U}'$ is fully faithful.
1. For every locally free module $\mathcal{F}$ on $\hat{U}'$, there exists a coherent module $F$ on $U'$ (not
   necessarily locally free, alas), and an isomorphism $\hat{F} \cong \mathcal{F}$.

It remains only to prove (ii), thanks to 5.9. Now by that remark and 2.1, it follows that $\mathcal{F}$ is induced by a
coherent module $\mathcal{G}$ on $\hat{X}'$. By the existence theorem *EGA* III 5.1.4, $\mathcal{G}$ is of the form
$\hat{F}$, where $F$ is coherent on $X$, whence the conclusion.

<!-- original page 133 -->

**Remarks.**

<!-- label: XII.5.11 -->

1. Using 5.10, 4.7 and a suitable hypothesis, saying that certain local rings of the geometric fibers of $X' \to S'$ are
   "pure" resp. parafactorial, one ought to be able to obtain statements saying that the functor $Z' \mapsto \hat{Z}'$
   from the category of étale covers of $X'$ to the category of étale covers of $\hat{X}'$ (or what amounts to the same,
   of $X'_{0}$) is an equivalence of categories, resp. that the functor $L \mapsto \hat{L}$ from the category of
   invertible modules on $X'$ to the category of invertible modules on $\hat{X}'$ is an equivalence. Using recent
   results of Murre, it is probable that one ought to be able to deduce existence theorems for Picard schemes of certain
   non-proper algebraic schemes.[^N.D.E-XII-6] More generally, the elimination of purity hypotheses in various existence
   theorems, notably of representability of functors like Hilbert or Picard functors, by means of the techniques
   developed in this seminar, deserves a systematic study.

1. One may set oneself the problem of giving handy necessary and sufficient conditions, in terms of depth, for the
   universal finiteness condition envisaged in 5.10 to be verified. When $S$ is the spectrum of a field, it follows
   easily from *EGA* III 1.4.15 that it is necessary and sufficient that the $R^{i}g_{\ast}(F)$ ($i \leqslant n$) be
   coherent, which is expressed in terms of depth thanks to VIII 2.3. In the general case, one will note however that it
   does not suffice to require that the preceding condition be verified for all the fibers $U_{s} \subset X_{s}$
   ($s \in S$), even in the case where $n = 0$. Take for example $X = S$, $S$ the spectrum of a discrete valuation ring,
   $U$ the open subset reduced to the generic point, $F = O_{U}$.

1. Here is, however, a sufficient condition ensuring that one is under the conditions of the hypothesis of 5.10: it
   suffices that $f$ be flat, and that for every $s \in S$ and every $x \in Y_{s} = X_{s} - U_{s}$, one has

    ```text
    prof O_{X_s,x} ⩾ n + 2.
    ```

    Indeed, taking into account Lemma 2.5 (cf. relation (16) after 2.5), it follows that one then has $g_{\ast}(O_{U}) \cong O_{X}$
    and $R^{i}g_{\ast}(O_{U}) = 0$ for $0 < i \leqslant n$, and the same relations will plainly be verified after any base change
    $S' \to S$.

<!-- ────────────────────────────────────────────────────────────────────── -->

<!-- Ledger delta — Exposé XII                                               -->

<!-- ────────────────────────────────────────────────────────────────────── -->

<!--
The following terminological choices were fixed in the present Exposé. They
extend the entries already recorded in `glossary.md`; merge into the master
glossary on the next consolidation pass.

| French                                            | English                                          | Note                                                                                  |
| ------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------- |
| `schéma algébrique projectif`                     | projective algebraic scheme                      | Title-level term for the Exposé.                                                      |
| `théorème de dualité projective`                  | projective duality theorem                       | Serre, *FAC*; modelled on local duality (Exp. IV).                                    |
| `théorème de comparaison de Grauert`              | Grauert's comparison theorem                     | Heading of §2.                                                                        |
| `cône projetant épointé`                          | punctured projecting cone                        | `X̃ = Spec(S) − Spec(k)` of `X = P^r_k`.                                              |
| `section hyperplane`                              | hyperplane section                               | Zeros of a regular section of `O_X(1)`.                                               |
| `Module cohérent`                                 | coherent module                                  | Capital "Module" in the source preserved as lowercase in English.                     |
| `Algèbre graduée quasi-cohérente`                 | quasi-coherent graded algebra                    | As above; capital "Algèbre" lowercased.                                               |
| `Idéal cohérent`                                  | coherent ideal                                   | As above.                                                                             |
| `Ext_OX(F, G)` (underlined in source)             | `ℰxt_{O_X}(F, G)`                                | Sheafified Ext rendered with calligraphic `ℰ`, matching Exp. VI convention.           |
| `complété formel de X le long de Y`               | formal completion of `X` along `Y`               | Notation `X̂` preserved across line breaks.                                           |
| `platitude normale`                               | normal flatness                                  | Heading of §4; `gr_𝒥(O_X)` flat on `X₀`.                                              |
| `couple (X, X₀)`                                  | pair `(X, X₀)`                                   | Per SGA 2 master glossary.                                                            |
| `pur` (anneau local), respecté `respé`            | "pure" (local ring); the "respective" case       | Quotation marks preserve the SGA-era technical usage of `pur` (X 3.1).                |
| `parafactoriel`                                   | parafactorial                                    | XI 3.1.                                                                               |
| `condition de Lefschetz effective (Leff)`         | effective Lefschetz condition (Leff)             | X §2.                                                                                 |
| `morphisme adique`                                | adic morphism                                    | IX §2; the source notes the hypothesis is dispensable in 3.2's proof.                 |
| `générisation`                                    | generization                                     | Topological term used in 1.5.                                                         |
| `condition de finitude universelle`               | universal finiteness condition                   | Heading of §5; appears in 5.7 (i)–(iii).                                              |
| `condition de finitude simultanée`                | simultaneous finiteness condition                | 5.6: 5.2 (ii) reinterpreted.                                                          |
| `condition de nullité asymptotique`               | asymptotic vanishing condition                   | 5.6: 5.5 (i) reinterpreted.                                                           |
| `morphisme quasi-projectif`                       | quasi-projective morphism                        | 5.6.                                                                                  |
| `revêtement étale`                                | étale cover                                      | Per glossary; "covering" reserved for general topological covers.                     |
| `aboutissement`                                   | abutment                                         | Per glossary.                                                                         |
| `système projectif essentiellement constant`      | essentially constant projective system           | Mittag-Leffler reduction in proof of 2.2.                                             |
| `loisible`                                        | permissible                                      | "Allowable" reads too casual in proof prose.                                          |
| `tedious dévissage` (`pénible dévissage`)         | tedious dévissage                                | 1.6; "dévissage" kept as loanword per glossary.                                       |
| `expedient` (`expédient`)                         | expedient                                        | 3.5 Remark; "a somewhat tedious expedient".                                           |
| `on gagne`                                        | one wins                                         | End of proof of 3.1; preserved literally as a Grothendieckism.                        |

Unresolved / flagged:

- The source uses the Grothendieck-era capital "Module", "Algèbre", "Idéal" to
  signal sheaves of modules / algebras / ideals on a scheme; in English these
  are uniformly rendered with lowercase initial letter, since the typographic
  device is not standard in present-day mathematical English. The accompanying
  word (e.g. "coherent module", "graded algebra", "coherent ideal") preserves
  the technical content.
- The source labels equation (20 bis) and (21 bis) in §4; these are rendered
  as `eq:XII.4.20bis` and `eq:XII.4.21bis` to keep the numbering visible.
- The Roman-numbered conditions a)/b)/c) inside 3.1 and a′)/b′)/c′) inside the
  proof of 3.1 are kept as in the source; they are not Markdown-numbered list
  items because of the prime in a′), b′), c′).
- The "Comments on Exposé XIII (XIII 6)" reference visible in the introduction
  is not cited in Exposé XII proper; no action needed.
- Footnote [^N.D.E-XII-6] is very long because the source footnote (6) on
  pp. 133–134 carries a full bibliographic survey; it is rendered verbatim.
-->

[^XII-1-star]: The present exposé, written up in January 1963, is markedly more detailed than the oral exposé was, in
    June 1962.

[^XII-1-starstar]: J.-P. Serre, "Faisceaux algébriques cohérents", *Ann. of Math.* **61** (1955), pp. 197–278.

[^N.D.E-XII-1]: *N.D.E.* The reader fond of the History of Mathematics will consult with interest the letter that
    Grothendieck wrote to Serre on 15 December 1955 and the latter's reply of 22 December of the same year; see
    *Correspondance Grothendieck-Serre*, edited by Pierre Colmez and Jean-Pierre Serre, Documents Mathématiques, vol. 2,
    Société Mathématique de France, Paris, 2001.

[^XII-1-starstarstar]: For a more general duality theorem, cf. the Hartshorne seminar cited at the end of Exp. IV.

[^XII-1-star2]: The first part of 1.5 may be obtained at once by applying the purely local statement *EGA* IV 12.3.4 to
    the preceding `Eʲ`, which short-circuits the greater part of the proof that follows.

[^XII-1-star3]: This remark is made more precise by the footnote on page 112.

[^N.D.E-XII-2]: *N.D.E.* See Corollary I.1.4 of the article of Mme Raynaud (Raynaud M., "Théorèmes de Lefschetz en
    cohomologie des faisceaux cohérents et en cohomologie étale. Application au groupe fondamental", *Ann. Sci. Éc.
    Norm. Sup.* (4) **7** (1974), pp. 29–52).

[^N.D.E-XII-3]: *N.D.E.* For a version without flatness hypothesis, see (Raynaud M., "Théorèmes de Lefschetz en
    cohomologie des faisceaux cohérents et en cohomologie étale. Application au groupe fondamental", *Ann. Sci. Éc.
    Norm. Sup.* (4) **7** (1974), pp. 29–52, Theorem II.3.3).

[^XII-3-star]: Rectified as indicated in IX p. 85.

[^N.D.E-XII-4]: *N.D.E.* Let us point out the spectacular connectedness result obtained since by Fulton and Hansen, in
    the case where $S = \operatorname{Spec}(k)$ ($k$ an algebraically closed field). Let
    $g: X \to P^{m}_{k} \times P^{m}_{k}$ be such that $\dim g(X) > m$; then the inverse image of the diagonal is
    connected. Among other things, this allows one to generalize Corollary 4.9 when $f$ is the structural morphism of
    the projective space $P^{m}_{k}$ over $S = \operatorname{Spec}(k)$: precisely, an irreducible subvariety $X$ of
    $P^{m}_{k}$ of dimension $> m/2$ has trivial fundamental group! (cf. Fulton W. & Hansen J., "A connectedness theorem
    for projective varieties, with applications to intersections and singularities of mappings", *Ann. of Math.* (2)
    **110** (1979), no. 1, pp. 159–166). For generalizations to the case of Grassmannians or abelian varieties, see
    Debarre O., "Théorèmes de connexité pour les produits d'espaces projectifs et les grassmanniennes", *Amer. J. Math.*
    **118** (1996), no. 6, pp. 1347–1367 and "Théorèmes de connexité et variétés abéliennes", *Amer. J. Math.* **117**
    (1995), no. 3, pp. 787–805. The triviality result for the fundamental group of $X$ as above was obtained
    independently by Faltings, who proves moreover that $\operatorname{Pic}(X)$ has no torsion prime to the
    characteristic of $k$, by methods of algebraization of formal vector bundles, more in the line of Grothendieck's
    techniques, cf. (Faltings G., "Algebraization of some formal vector bundles", *Ann. of Math.* (2) **110** (1979),
    no. 3, pp. 501–514).

[^N.D.E-XII-5]: *N.D.E.* As Raynaud has remarked, the decomposition result for the de Rham complex of Deligne and
    Illusie easily entails the vanishing of the group $H^{i}(X, L^{-1})$ (with $L$ ample on $X$ projective and smooth
    over $k$ of characteristic $p > 0$) for $i < \inf(p, \dim(X))$ as soon as one assumes that $X$ is liftable to a flat
    scheme over $W_{2}(k)$ (cf. Deligne P. & Illusie L., "Relèvements modulo $p^{2}$ et décomposition du complexe de de
    Rham", *Invent. Math.* **89** (1987), no. 2, pp. 247–270); this gives a purely algebraic proof of Kodaira's result
    for projective varieties in characteristic zero. If $X$ is not liftable, it is well known that the "vanishing
    theorem" is false; cf. the example in (Raynaud M., "Contre-exemple au 'vanishing theorem' en caractéristique
    $p > 0$", in *C.P. Ramanujam — a tribute*, Tata Inst. Fund. Res. Studies in Math., vol. 8, Springer, Berlin–New
    York, 1978, pp. 273–278); see also the very pretty examples in (Haboush W. & Lauritzen N., "Varieties of unseparated
    flags", in *Linear algebraic groups and their representations (Los Angeles, CA, 1992)*, Contemp. Math., vol. 153,
    American Mathematical Society, Providence, RI, 1993, pp. 35–57), simplified in (Lauritzen N. & Rao A.P., "Elementary
    counterexamples to Kodaira vanishing in prime characteristic", *Proc. Indian Acad. Sci. Math. Sci.* **107** (1997),
    no. 1, pp. 21–25). On the other hand, I do not know an example where the map
    $\operatorname{Pic}(X_{n+1}) \to \operatorname{Pic}(X_{n})$ is not surjective for $n > 1$ in positive
    characteristic, where $X_{n}$ denotes a thickened hyperplane section of $X$ projective and smooth as above.

[^XII-5-star]: It suffices in fact that $g$ be quasi-compact and quasi-separated (*EGA* IV 1.2.1), without conditions on
    $U$, $X$.

[^N.D.E-XII-6]: *N.D.E.* Of course, in the projective case one refers to Grothendieck's existence theorems of *FGA*; cf.
    Grothendieck A., "Technique de descente et théorèmes d'existence en géométrie algébrique. VI. Les schémas de Picard:
    propriétés générales", in *Séminaire Bourbaki*, vol. 7, Société mathématique de France, Paris, 1995, Exp. 236, pp.
    221–243 and "Technique de descente et théorèmes d'existence en géométrie algébrique. V. Les schémas de Picard:
    théorèmes d'existence", in *Séminaire Bourbaki*, vol. 7, Société mathématique de France, Paris, 1995, Exp. 232, pp.
    143–161. The nine finiteness conjectures contained therein are proved in Exposés XII and XIII of Mme Raynaud and
    Kleiman in SGA 6. For an excellent elementary text on the subject, see Kleiman's expository article (Kleiman S.,
    "The Picard scheme", to appear in *Contemp. Math.*). For an application of these techniques to the global
    generalized Jacobians of a relative smooth curve, see (Contou-Carrère C., "La jacobienne généralisée d'une courbe
    relative; construction et propriété universelle de factorisation", *C. R. Acad. Sci. Paris Sér. A-B* **289** (1979),
    no. 3, A203–A206 and "Jacobiennes généralisées globales relatives", in *The Grothendieck Festschrift*, Vol. II,
    Progr. Math., vol. 87, Birkhäuser, Boston, 1990, pp. 69–109). See also, by the same author, in the purely local
    context, the construction and study of the "local generalized Jacobian" functor ("Jacobienne locale, groupe de
    bivecteurs de Witt universel, et symbole modéré", *C. R. Acad. Sci. Paris Sér. I Math.* **318** (1994), no. 8, pp.
    743–746). Moreover, while in the case of a projective and smooth morphism the connected components of the Picard
    scheme are proper, this is no longer the case in the singular case. The problem of compactifying Picard schemes
    arises naturally: this problem has been studied in detail, notably in (Altman A.B. & Kleiman S., "Compactifying the
    Picard scheme", *Adv. in Math.* **35** (1980), no. 1, pp. 50–112, and "Compactifying the Picard scheme. II", *Amer.
    J. Math.* **101** (1979), no. 1, pp. 10–41). The case of curves had been studied earlier (D'Souza C.,
    "Compactification of generalised Jacobians", *Proc. Indian Acad. Sci. Sect. A Math. Sci.* **88** (1979), no. 5, pp.
    419–457). One even knows exactly when the compactified Jacobian of a curve is irreducible (Rego C.J., "The
    compactified Jacobian", *Ann. Sci. Éc. Norm. Sup.* (4) **13** (1980), no. 2, pp. 211–223), this being the closure of
    the (ordinary) Jacobian when the curve is geometrically integral and locally planar; for a family construction of
    compactified Jacobians, see (Esteves E., "Compactifying the relative Jacobian over families of reduced curves",
    *Trans. Amer. Math. Soc.* **353** (2001), no. 8, pp. 3045–3095). Since then, existence results for the Picard scheme
    in the proper case have progressed since the original edition of SGA 2; cf. (Murre J.P., "On contravariant functors
    from the category of pre-schemes over a field into the category of abelian groups (with an application to the Picard
    functor)", *Publ. Math. Inst. Hautes Études Sci.* **23** (1964), pp. 5–43) and especially (Artin M., "Algebraization
    of formal moduli. I", in *Global Analysis (Papers in Honor of K. Kodaira)*, Univ. Tokyo Press, Tokyo, 1969, pp.
    21–71). See also (Raynaud M., "Spécialisation du foncteur de Picard", *Publ. Math. Inst. Hautes Études Sci.* **38**
    (1970), pp. 27–76) in the case of a proper scheme over a discrete valuation ring, but not necessarily flat. For a
    discussion of more recent results, particularly those of Artin, for the Picard functor of proper and flat schemes,
    in particular in the cohomologically flat case in dimension 0, see Chapter VIII of (Bosch S., Lütkebohmert W. &
    Raynaud M., *Néron models*, Ergebnisse der Mathematik und ihrer Grenzgebiete (3), vol. 21, Springer-Verlag, Berlin,
    1990) and the references cited. Much more recently, very fine results have been obtained in the case of relative
    curves $f: X \to S$ over the spectrum $S$ of a discrete valuation ring with perfect residue field. More precisely,
    one assumes that $f$ is proper and flat, $X$ regular and $f_{\ast} O_{X} = O_{S}$. On the other hand, one does not
    assume $f$ cohomologically flat in dimension 0, i.e. one does not assume $H^{1}(X, O)$ torsion-free. The Picard
    scheme is then not representable, either by a scheme or an algebraic space, as soon as the torsion in question is
    non-zero. Let $J$ be the Néron model of the generic fiber of $f$: it is a quotient of the Picard functor $P$. Then,
    Raynaud has shown that the kernel of the tangent map $H^{1}(X, O) = Lie(P) \to Lie(J)$ coincides with the torsion
    subgroup of $H^{1}$ and that the cokernel has the same length (see Theorem 3.1 of (Liu Q., Lorenzini D. & Raynaud
    M., "Néron models, Lie algebras, and reduction of curves of genus one", *Invent. Math.* **157** (2004), pp.
    455–518)). This result allows the above-mentioned authors to study the link between the Birch–Swinnerton-Dyer and
    Artin–Tate conjectures (see Theorem 6.6 of *loc. cit.*). Concerning the local Picard scheme, see Boutot's thesis,
    cited in editor's note (13) page 149.


<!-- SOURCE: 13-problemes-et-conjectures.md -->

# Exposé XIII. Problems and conjectures

<!-- label: XIII -->

<!-- original page 135 -->

## 1. Relations between global and local results. Affine problems related to duality

<!-- label: XIII.1 -->

<!-- original page 172 -->

It is well known that many statements concerning a projective scheme $X$ can be formulated in terms of statements
concerning a certain graded ring, or better a complete local ring, namely the homogeneous coordinate ring of $X$ (i.e.
the affine ring of the projecting cone $\tilde{X}$ of $X$), or its completion (i.e. the completion of the local ring of
the vertex of $\tilde{X}$). The interest of this reformulation is that it often allows one, starting from known global
results, to conjecture, and even to prove, analogous results for complete noetherian local rings more general than those
which really appear in the global statement, for instance for local rings that are not necessarily of equal
characteristic. Thus, Serre's duality theorem for projective space (XII 1.1) suggested the useful local duality theorem
(V 2.1). Serre's fundamental theorem on the cohomology of coherent Modules on projective space (finiteness, asymptotic
behavior for large $n$ of $H^{i}(X, F(n))$, cf. EGA III 2.2.1) generalizes to a structure theorem for the local
invariants $H^{i}_{\mathfrak{m}}(M)$, see V 3. Likewise, the Lefschetz theorems for the fundamental group, and for the
Picard group ("equivalence criteria"), well familiar in the classical case and subsequently extended to an arbitrary
base field, suggested the "local" Lefschetz theorems of Exposés X and XI. Of course, the local theorems are in turn
precious tools for obtaining global statements. For example, local duality permits one to formulate a global asymptotic
property (XII 1.3 (i)) by the vanishing of certain local invariants $H^{i}(F_{x})$. More substantially, the local
Lefschetz theorems, implying for instance the "purity" or the parafactoriality of certain local rings that are complete
intersections (X 3.4 and XI 3.13), allow one, in the global Lefschetz theorems, to dispose of certain non-singularity
hypotheses, as in X 3.5, 3.6, 3.7.

<!-- original page 173 -->

Another useful generalization of the theorems concerning projective schemes over a field $k$ consists in replacing $k$
by a general base scheme. Thus, the sequel of EGA III will give[^N.D.E-XIII-1] a generalization in this direction of
Serre duality[^XIII-1-1]; the theorems on finiteness and asymptotic behavior of the $H^{i}(X, F(n))$ were stated in EGA
III 2.2.1 over a general base scheme, and finally the Lefschetz theorems can equally be developed for a projective
morphism, as we saw in XII 4.9, thanks to the local theorem XII 4.7. Of course, working over a general base scheme also
leads to essentially new statements, such as the "comparison theorem" EGA III 4.15 and the existence theorem for sheaves
EGA III 5.1.4 (which, as we saw moreover in IX, derive from the same key cohomological theorems as the Lefschetz
theorems for $\pi_{1}$ and `Pic`).

It then becomes necessary to extract theorems that simultaneously encompass the two generalizations we have just
indicated of statements concerning projective schemes over a field. The natural objects for such a common generalization
are noetherian rings that are separated and complete for an $I$-adic topology. Their study, from this point of view, has
not yet been seriously addressed, and seems to me at the present time the most interesting subject in the local theory
of coherent sheaves. Here is a typical problem in this direction:

**Conjecture 1.1** ("Second affine finiteness theorem"[^XIII-1-2][^N.D.E-XIII-2]).

<!-- label: XIII.1.1 -->

Let $M$ be a finitely generated module over a noetherian ring $A$ (which one will, if necessary, assume to be a quotient
of a regular ring), and let $J$ be an ideal of $A$. Prove that the modules $H^{i}_{J}(M)$ are

<!-- original page 174 -->

"$J$-cofinite", i.e. that the modules

$$
\operatorname{Hom}_{A}(A/J, H^{i}_{J}(M))
$$

are finitely generated.

Recall that $H^{i}_{J}(M)$ denotes the module $H^{i}_{Y}(X, \tilde{M})$ (where $X = \operatorname{Spec}(A)$, $Y = V(J)$)
of Exposé I, interpreted in II in terms of a direct limit of cohomologies of Koszul complexes, or again for
$i \geqslant 2$ the module $H^{i-1}(X - Y, \tilde{M})$. Actually, 1.1 should be a consequence of a more precise
statement, implying that the $H^{i}_{J}(M)$ lie in a suitable abelian subcategory $\mathcal{D}_{J}$ of the category
$\mathcal{C}_{J}$ of $A$-modules of support $\subset Y = V(J)$, such that $H \in Ob \mathcal{D}_{J}$ implies that $H$ is
$J$-cofinite. (N.B. The category of modules $H$ of support contained in $V(J)$ that are $J$-cofinite is unfortunately
not stable under passage to a quotient!). The essential problem would then consist in defining $\mathcal{D}_{J}$. More
precisely, the solution of problem 1.1 should follow (at least if $A$ is a quotient of a regular ring) from a duality
theory, generalizing both local duality and the duality theory of projective morphisms to which we alluded above, and
which would be of the following kind:

**Conjecture 1.2** ("Affine duality"[^XIII-1-3]).

<!-- label: XIII.1.2 -->

Suppose $A$ is regular, separated and complete for the $J$-adic topology. Let $C\bullet(A)$ be an injective resolution
of $A$.

(i) Prove that the functor

```text
D_J : L• ↦ Hom_J(L•, C•(A))
```

from the category of complexes of $A$-modules that are free of finite type in each dimension and bounded above in degree
(where morphisms are homomorphisms of complexes up to homotopy) into the category of complexes of $A$-modules $K\bullet$
that are injective in each dimension and bounded above in degree (where the morphisms are defined similarly) is fully
faithful.

(ii) Prove that for every $K\bullet$ of the form $D_{J}(L\bullet)$, the
$H^{i}(K\bullet) (= Ext^{i}_{Y}(X; L\bullet, \mathcal{O}_{X}))$ are $J$-cofinite.

(iii) More precisely, prove that the $K\bullet$ that are homotopic to a complex of the form $D_{J}(L\bullet)$ can be
characterized by finiteness properties of the $H^{i}(K\bullet)$, stronger than the one envisaged in (ii), for example by
the property $H^{i}(K\bullet) \in Ob \mathcal{D}_{J}$,

<!-- original page 175 -->

where $\mathcal{D}_{J}$ is a suitable abelian category, as envisaged above.

Note that the problem is resolved in the affirmative when $A$ is local and $J$ is an ideal of definition of it (cf. Exp.
IV), and also when $J$ is the zero ideal. In these two cases, exceptionally, one can confine oneself to taking for
$\mathcal{D}_{J}$ the category of Modules with support $V(J)$ that are $J$-cofinite, (which in the second case signifies
simply that one takes the category of finitely generated Modules over $A$). An affirmative solution of

<!-- original page 138 -->

conjecture 1.2 in general would give one for 1.1, by taking for $L\bullet$ the dual of a free finitely generated
resolution of $M$. On the other hand, an affirmative solution of 1.1 would give an affirmative answer to the first part
of the following conjecture, which we formulate in "global" form:

**Conjecture 1.3.**

<!-- label: XIII.1.3 -->

Let $X \subset \mathbf{P}^{r}_{k}$ be a closed subscheme of standard projective space that is locally a complete
intersection and every irreducible component of which is of codimension $\geqslant s$. Let $U = \mathbf{P}^{r}_{k} - X$.

(i) Prove that for every coherent Module $F$ on $U$, one has

```text
dim Hⁱ(U, F) < +∞   for i ⩾ s.
```

[^XIII-1-4]

(ii) Give an example, with $X$ connected and regular, where one has

$$
H^{s}(U, F) \neq 0.
$$

To see that (i) is a particular case of 1.1, one considers

```text
Hⁱ(U, F(·)) = ⊕_n Hⁱ(U, F(n)) = Hⁱ(𝐄^{r+1} − X̃, F̃)
```

as a module over the affine ring $k[t_{0}, \cdots, t_{r}]$ of the projecting cone $\mathbf{E}^{r+1}$ of
$\mathbf{P}^{r}$. This module is none other than $H^{i+1}_{J}(M)$, where $J$ is the ideal of the projecting cone
$\tilde{X}$ of $X$ in $\mathbf{E}^{r+1}$.

<!-- original page 176 -->

On the other hand, from the hypothesis made on $X$, which implies that $\tilde{X}$ is also a complete intersection of
codimension $\geqslant s$ at every point of $\mathbf{E}^{r+1}$ distinct from the origin, it follows that
$H^{i+1}_{J}(M)$ is zero outside the origin for $i \geqslant s$. If it is therefore $J$-cofinite as 1.1 demands, it is
*a fortiori* $\mathfrak{m}$-cofinite, which easily implies that it is finite-dimensional in each degree[^N.D.E-XIII-3].
Note moreover that conjecture 1.3 is already posed for a non-singular irreducible curve $X$ in $\mathbf{P}^{3}$; one
does not know in this case whether the $H^{2}(\mathbf{P}^{3} - X, \mathcal{O}_{X}(n))$ are finite-dimensional, or
whether they are necessarily zero[^XIII-1-5]. One does not even know whether there exists an irreducible curve in
$\mathbf{P}^{3}$ that is not set-theoretically the intersection of two hypersurfaces[^N.D.E-XIII-4].

**Problem 1.4.**

<!-- label: XIII.1.4 -->

Give an affine variant of the "comparison theorem" EGA III 4.1.5 as a theorem of commutation of the functors $H^{i}_{J}$
with certain inverse limits.

Finally, in the present order of ideas, I had posed the following problem: let $A$ be a complete regular noetherian
local ring, $K$ its fraction field; prove that $Ext^{i}_{A}(K, A) = 0$ for every $i$. An affirmative answer was given on
the spot by M. Auslander: the regularity hypothesis can be replaced by the assumption that $A$ is integral, and in fact
it is true that $Ext^{i}_{A}(K, M) = 0$ for every $i$, as soon as $M$ is finitely generated over $A$. This follows
immediately from the following statement, due to Auslander: if $A$ is a complete noetherian local ring, then for every
finitely generated module $M$ over $A$, the functors $Ext^{i}_{A}(\cdot, M)$ transform direct limits into inverse
limits[^N.D.E-XIII-5].

## 2. Problems related to $\pi_{0}$: local Bertini theorems

<!-- label: XIII.2 -->

Let $A$ be a complete noetherian local ring, $f$ an element of its maximal ideal, $X = \operatorname{Spec}(A)$,
$Y = \operatorname{Spec}(A/fA)$. The use of the local "Lefschetz" technique allows one to give criteria for
$Y' = X' \cap Y$ (where $X' = X - {\mathfrak{m}}$) to be connected, in terms of hypotheses on $X'$. Thus, it suffices
that one have: a) $X'$ connected, b) $prof \mathcal{O}_{X',x} \geqslant 2$

<!-- original page 177 -->

for every closed point $x$ of $X'$, c) $f$ is $A$-regular. One notes however that hypotheses b) and c) are not of purely
topological nature; for instance, they are not invariant under replacing $X$ by $X_{red}$. In the analogous situation
for a projective scheme $X'$ over a field and a hyperplane section $Y'$ of $X'$, the use of "Bertini's theorem" and
Zariski's "connection theorem" allows one in fact to obtain results of distinctly more satisfactory appearance, which
had led me in the oral seminar to state a conjecture, which I have since resolved in the affirmative. Let us therefore
state here:

**Theorem 2.1.**

<!-- label: XIII.2.1 -->

Let $A$ be a complete noetherian local ring, $X$ its spectrum, $a$ the closed point of $X$, $X' = X - {a}$. Suppose that
$X$ satisfies the conditions (where $k$ denotes an integer $\geqslant 1$):

$a_{k}$) The irreducible components of $X'$ are of dimension $\geqslant k + 1$.

<!-- original page 140 -->

$b_{k}$) $X'$ is connected in dimension $\geqslant k$, i.e. one cannot disconnect $X'$ by a closed part of dimension
$< k$ (cf. III 3.8).

Let $m$ be an integer, $0 \leqslant m \leqslant k$, and let $f_{1}, \cdots, f_{m} \in \mathfrak{r}(A)$; set
$B = A / \sum_{i} f_{i}A$, $Y = \operatorname{Spec}(B) = V(f_{1}) \cap \cdots \cap V(f_{m})$,
$Y' = X' \cap Y = Y - {a}$. Then $Y$ satisfies the conditions $a_{k-m}$), $b_{k-m}$). In particular, for every sequence
of $m \leqslant k$ elements $f_{1}, \cdots, f_{m}$ of $\mathfrak{r}(A)$,
$Y' = X' \cap V(f_{1}) \cap \cdots \cap V(f_{m})$ is connected.

It is moreover easy to see that if the last conclusion holds (it evidently suffices to take $m = k$ there), and
excluding the case where $X$ would be irreducible of dimension 0 or 1, it follows that the irreducible components of
$X'$ are of dimension $\geqslant k + 1$, and $X'$ is connected in dimension $\geqslant k$, so that in a sense, 2.1 is a
"best possible" result.

Let us give the principle of the proof of 2.1. Only condition $b_{k-m}$) for $Y$ poses a problem. One reduces easily,
for given $k$, to the case where $X$ is integral, and even (by passing to the normalization, which is finite over $X$)

<!-- original page 178 -->

to the case where $X$ is normal. If $k = 1$, hence $\dim X' \geqslant 2$, then $X'$ is of depth $\geqslant 2$ at its
closed points, and one can apply the result recalled at the beginning of the section, which shows that
$Y' = X' \cap V(f)$ is connected. In the case $k \geqslant 1$, one supposes the theorem proved for $k' < k$. By
induction on $m$, one is reduced to the case where $m = 1$, i.e. to verifying that for $f_{1} \in \mathfrak{r}(A)$,
$X' \cap V(f_{1})$ is connected in dimension $\geqslant k - 1$. If it were not, i.e. if it were disconnected by a $Z'$
of dimension $< k - 1$, there would exist a sequence $f_{2}, \cdots, f_{k}$ such that
$X' \cap V(f_{1}) \cap \cdots \cap V(f_{k})$ is disconnected, and in this sequence one can choose
$f_{2} \in \mathfrak{r}(A)$ arbitrarily, subject to the sole condition of not vanishing at any point of a certain finite
part $F$ of $X'$ (namely the set of maximal points of $Z'$). Moreover, one verifies easily, using the fact that $X'$ is
normal, hence satisfies Serre's condition ($S_{2}$)[^XIII-2-1], that there exists a finite part $F'$ of $X'$ such that
$f \in \mathfrak{r}(A)$, $V(f) \cap F' = \emptyset$ implies that $V(f) \cap X'$ also satisfies condition ($S_{2}$). One
can then choose $f_{2}$ in such a way that $f_{2}$ vanishes neither on $F$ nor on $F'$, hence such that
$X' \cap V(f_{2})$ satisfies ($S_{2}$). But then, by virtue of Hartshorne's theorem III 3.6, $X' \cap V(f_{2})$ is
connected in codimension 1, hence (since every component of $X' \cap V(f_{2})$ is of dimension $\geqslant k$) it is
connected in dimension $\geqslant k - 1$. Applying the induction hypothesis to
$V(f_{2}) = \operatorname{Spec}(A/f_{2}A)$, it follows that
$X' \cap V(f_{2}) \cap V(f_{1}) \cap V(f_{3}) \cap \cdots \cap V(f_{k})$ is connected, whereas it had been constructed
disconnected — absurd.

Let us point out some interesting corollaries:

**Corollary 2.2.**

<!-- label: XIII.2.2 -->

Let $f : X \to Y$ be a proper morphism of locally noetherian preschemes, with $Y$ integral, $y_{0} \in Y$, $y_{1}$ the
generic point of $Y$. Suppose

a) $Y$ is unibranch at $y_{0}$, and every irreducible component of $X$ dominates $Y$.

<!-- original page 141 -->

b) The irreducible components of $X_{y_{1}}$ are of dimension $\geqslant k + 1$, and $X_{y_{1}}$ is connected in
dimension $\geqslant k$.

<!-- original page 179 -->

Then the irreducible components of $X_{y_{0}}$ are of dimension $\geqslant k + 1$, and $X_{y_{0}}$ is connected in
dimension $\geqslant k$.

Indeed, Zariski's connection theorem (cf. EGA III 4.3.1) implies that $X_{y_{0}}$ is connected; to show that it is not
disconnected by a closed part of dimension $< k$, one is reduced to showing that the local rings at points
$x \in X_{y_{0}}$ such that $\dim x < k$ have a spectrum not disconnected by $x$. Now this is true without assuming
either $f$ proper, or $Y$ unibranch at $y_{0}$. One reduces, to see this, to the case where $X$ is integral dominating
$Y$, and if one wishes $Y$ affine of finite type over $\mathbb{Z}$, so that one is under the conditions of the dimension
formula for $\mathcal{O}_{X,x}$ over $\mathcal{O}_{Y,y_{0}}$. Using in this case the finiteness of the normal closure,
one can even suppose $X$ normal, hence by virtue of a theorem of Nagata[^XIII-2-2], the completion of a local ring
$\mathcal{O}_{X,x}$ of $X'$ is again normal; hence (if $\mathcal{O}_{X,x}$ is of dimension $N$)
$\operatorname{Spec}(\hat{\mathcal{O}}_{X,x})$ is connected in dimension $\geqslant N - 1$. Let
$n = \dim \mathcal{O}_{Y,y_{0}}$; then $deg tr k(x)/k(y) < k$ implies
$\dim \mathcal{O}_{X,x} > n + (k + 1) - k = n + 1$, taking into account $\dim X_{y_{1}} \geqslant k + 1$, and taking a
system $f_{1}, \cdots, f_{n}$ of parameters of $\mathcal{O}_{Y,y_{0}}$ which one lifts to elements of
$\mathcal{O}_{X,x}$, one sees by 2.1 that
$\operatorname{Spec}(\hat{\mathcal{O}}_{X,x} / \sum f_{i} \hat{\mathcal{O}}_{X,x})$ is connected in dimension
$\geqslant 1$, i.e. is not disconnected by its closed point, or equivalently,
$\operatorname{Spec}(\hat{\mathcal{O}}_{X_{y_{0}},x})$ is not disconnected by its closed point; *a fortiori* the same
holds for $\operatorname{Spec}(\mathcal{O}_{X_{y_{0}},x})$.

As in the case of the ordinary connection theorem, one can vary 2.2 by taking geometric fibers (over the algebraic
closures of the residue fields), provided one supposes $Y$ geometrically unibranch at $y_{0}$, or (without other
hypothesis than $Y$ noetherian) that $f$ is universally open. Applying this to the case where $Y$ is the dual scheme of
a projective scheme $\mathbf{P}^{r}_{k}$ over a field, one recovers a strengthened form of the global result that had
inspired 2.1, namely:

**Corollary 2.3**[^N.D.E-XIII-6].

<!-- label: XIII.2.3 -->

Let $X$ be a closed subscheme of $\mathbf{P}^{r}_{k}$ ($k$ a field); suppose the irreducible components of $X$ are of
dimension $\geqslant l + 1$, and $X$ geometrically connected in dimension $\geqslant l$.

<!-- original page 180 -->

Then for every sequence $H_{1}, \cdots, H_{m}$ of $m$ hyperplanes of $\mathbf{P}^{r}_{k}$
($0 \leqslant m \leqslant l - 1$), $X \cap H_{1} \cap \cdots \cap H_{m}$ satisfies the same condition with $l - m$, in
particular is geometrically connected in dimension $\geqslant l - 1$.

One can moreover modify this statement in an obvious way for the case where one is given a proper morphism
$X \to \mathbf{P}^{r}_{k}$, which is not necessarily an immersion; an analogous extension is possible for 2.1 (by
considering a proper scheme over $X'$).

<!-- original page 142 -->

These statements are moreover formally deduced from the statements given here, taking into account the ordinary
connection theorem which reduces us to the case of a finite morphism.

**Corollary 2.4.**

<!-- label: XIII.2.4 -->

Let $A$ be a complete noetherian normal local ring of dimension $\geqslant k + 2$. Let $X = \operatorname{Spec}(A)$,
$X' = X - {a}$, and $f_{1}, \cdots, f_{k}$ elements of $\mathfrak{r}(A)$; then
$Y' = X' \cap V(f_{1}) \cap \cdots \cap V(f_{k})$ is connected, and $\pi_{1}(Y') \to \pi_{1}(X')$ is surjective.

One proceeds as in SGA 1 X 2.11.

In all this, only questions of connectedness were at issue. Now in the global case, well-known theorems assert that for
an irreducible projective variety $X \subset \mathbf{P}^{r}_{k}$, $k$ algebraically closed, its intersection with a
sufficiently "general" hyperplane $H$ is irreducible (and not merely connected): this is Bertini's theorem, proved by
Zariski, which in turn implies, by Zariski's connection theorem, that for every $H$, $H \cap X$ is connected (although
not necessarily irreducible). One can moreover proceed in the reverse direction, proving this latter result by a
Lefschetz-type technique, and deducing Bertini's theorem, reducing to the case where $X$ is normal, and using the
following result: for $H$ "sufficiently general", $X \cap H$ is also normal. This suggests:

**Conjecture 2.5**[^N.D.E-XIII-7].

<!-- label: XIII.2.5 -->

<!-- original page 181 -->

Let $A$ be a complete noetherian normal local ring. Show that there exists a nonzero $f \in \mathfrak{r}(A)$ such that
$Y' = X' \cap V(f) = Y - {a}$ (where $Y = \operatorname{Spec}(A/fA)$) is normal (hence irreducible by 2.1 if
$\dim A \geqslant 3$).

To do things properly, one would have to show that, in a suitable sense, there exist even "many" elements $f$ having the
property in question, for example that one can choose $f$ in an arbitrary power of the maximal ideal. Using Serre's
normality criterion and the remark made above for Serre's property ($S_{2}$), one sees that one would have an
affirmative answer to 2.5 if one had one to:

**Conjecture 2.6**[^N.D.E-XIII-8].

<!-- label: XIII.2.6 -->

Let $A$ be a complete noetherian local ring, $U$ an open part of its spectrum $X$, $F$ a finite part of $X' = X - {a}$.
Suppose $U$ is regular. Prove that there exists $f \in \mathfrak{r}(A)$ such that $V(f) \cap U$ is regular, and
$V(f) \cap F = \emptyset$.

For a "local Bertini"-type result, see Chow [2].

## 3. Problems related to $\pi_{1}$

<!-- label: XIII.3 -->

Here again, one has numerous questions, suggested by the global results or by the transcendental results.

**Conjecture 3.1**[^N.D.E-XIII-9].

<!-- label: XIII.3.1 -->

Let $A$ be a complete noetherian local ring with algebraically closed residue field, $X = \operatorname{Spec}(A)$,
$X' = X - {a}$, $a$ the closed point. Suppose the irreducible components of $X$ are of dimension $\geqslant 2$, and $X'$
connected.

(i) Prove that $\pi_{1}(X')$ is topologically finitely generated.

(ii) If $p$ is the characteristic exponent of the residue field $k$ of $A$, prove that the largest topological quotient
group of $\pi_{1}(X')$ that is "of order prime to $p$" is finitely presented.

<!-- original page 182 -->

For part (i), using the theory of descent SGA 1 IX 5.2 and theorem 2.4, one is reduced to the case where $A$ is normal
of dimension 2. In this case, a systematic method for studying the fundamental group of $X'$, inaugurated by Mumford [5]
in the transcendental setting, consists in desingularizing $X$, i.e. in considering a projective birational morphism
$Z \to X$, with $Z$ integral regular, inducing an isomorphism $Z' = Z|_{X'} \to X'$; it is plausible that such a $Z$
always exists, this is in any case what Abhyankar's method [1] demonstrates in the case of "equal
characteristics"[^XIII-3-1]. Let $C$ be the fiber of the closed point of $X$ by $Z \to X$; it is an algebraic curve over
the residue field $k$, connected by virtue of the connection theorem. The solution of 3.1 then seems linked to:

**Problem 3.2.**

<!-- label: XIII.3.2 -->

With the preceding notation, put $\pi_{1}(X')$ in relation with the topological invariants of $C$, in particular its
fundamental group, (in order to bring out the topological finite generation of $\pi_{1}(X')$, by using for instance SGA
1, theorem X 2.6).

Another method would be to consider $A$ as a finite algebra over a complete regular local ring $B$ of dimension 2,
ramified along a curve $C$ contained in $\operatorname{Spec}(B) = Y$. One is thus led to:

**Problem 3.3.**

<!-- label: XIII.3.3 -->

Let $A$ be a complete regular local ring of dimension 2, with algebraically closed residue field $k$, $X$ its spectrum,
$C$ a closed part of $X$ of dimension 1. Define local invariants of the embedded curve $C$, having a sense independent
of the residual characteristic, and the knowledge of which permits one to calculate the

<!-- original page 144 -->

fundamental group of $X - C$ by generators and relations when $k$ is of characteristic zero. Prove that when $k$ is of
characteristic $p > 0$, the "tame" fundamental group of $X - C$ is a quotient of the preceding one, and that the two
fundamental groups (in characteristic 0, and in characteristic $p > 0$) have the same maximal quotient of order prime to
$p$.

Of course, 3.3 shows us that in 3.1, there is also occasion to replace $X'$ by a scheme of the form $X - Y$, where $Y$
is a closed part of $X$ that is of codimension $\geqslant 2$ in every component of $X$ containing it.

<!-- original page 183 -->

When one abandons this restriction on $Y$, there must still exist an analogous finiteness result, on condition of
imposing "tame"-type restrictions on the ramification at the maximal points of the irreducible components of $Y$ that
are of codimension 1.

**Problem 3.4.**

<!-- label: XIII.3.4 -->

Let $A$ be a complete noetherian local ring of dimension 2, with algebraically closed residue field. Let again
$X = \operatorname{Spec}(A)$, $X' = X - {a}$. Find particular structural properties of $\pi_{1}(X')$ in the case where
$A$ is a complete intersection.

A satisfactory solution of this problem would perhaps permit one to resolve the following old problem:

**Conjecture 3.5**[^N.D.E-XIII-10].

<!-- label: XIII.3.5 -->

Find an irreducible curve in $\mathbf{P}^{3}_{k}$ ($k$ algebraically closed field), preferably non-singular, that is not
set-theoretically the intersection of two hypersurfaces.

(Kneser [4] shows that one can always obtain it as the intersection of three hypersurfaces).

## 4. Problems related to higher $\pi_{i}$: local and global Lefschetz theorems for complex analytic spaces[^N.D.E-XIII-11]

<!-- label: XIII.4 -->

Let $X$ be a scheme locally of finite type over the field of complex numbers $\mathbb{C}$; one can associate to it an
analytic space $X_{h}$ over $\mathbb{C}$, whence homotopy and homology invariants $\pi_{i}(X_{h})$, $H_{i}(X_{h})$,
$H^{i}(X_{h})$ etc. One knows moreover that $X$ is connected if and only if $X_{h}$ is, hence one has a bijection

$$
\pi_{0}(X_{h}) \to \pi_{0}(X).
$$

Likewise, since every étale covering $X'$ of $X$ defines an étale covering $X'_{h}$

<!-- original page 184 -->

of $X_{h}$, one has a canonical homomorphism

$$
\pi_{1}(X_{h}) \to \pi_{1}(X),
$$

which one knows, using a theorem of Grauert-Remmert, identifies the second group with the completion of the first for
the topology of subgroups of finite index (which simply expresses the fact that $X' \mapsto X'_{h}$ is an equivalence of
the category of étale coverings of $X$ with the category of finite étale coverings of $X_{h}$). It follows that the
results of this seminar (by purely algebraic means) on $\pi_{0}(X)$ and $\pi_{1}(X)$ imply results for $\pi_{0}(X_{h})$
and $\pi_{1}(X_{h})$ (which are of transcendental nature). Moreover, if $X$ is proper, the well-known exact sequence
$0 \to \mathbb{Z} \to \mathbb{C} \to \mathbb{C}* \to 0$ allows one to show that the Néron-Severi group of $X$ (the
quotient of its Picard group by the connected component of the identity) is isomorphic to a subgroup of
$H^{2}(X_{h}, \mathbb{Z})$; in the non-singular Kähler case, it is the subgroup denoted $H^{(1,1)}(X_{h}, \mathbb{Z})$
(classes of type `(1, 1)`):

```text
Pic(X) / Pic⁰(X) ⊂ H²(X, ℤ).
```

Consequently, the information we have obtained on Picard groups implies information, very partial it is true, about the
groups $H^{2}(X_{h}, \mathbb{Z})$. It is tempting to complete all these fragmentary results by conjectures.

Very precise indications, going in the same direction as those just mentioned, are furnished by a classical theorem of
Lefschetz [7]. It asserts that if $X$ is a non-singular irreducible projective analytic space of dimension $n$, and if
$Y$ is a non-singular hyperplane section, then the injection

$$
Y_{n-1} \to X_{n}
$$

induces a homomorphism

<!-- original page 185 -->

$$
\pi_{i}(Y_{n-1}) \to \pi_{i}(X_{n})
$$

which is an isomorphism for $i \leqslant n - 2$, an epimorphism for $i = n - 1$. The analogous statement follows for the
homomorphisms

$$
H_{i}(Y_{n-1}) \to H_{i}(X_{n})
$$

on homology (integral, to fix ideas), while in cohomology,

$$
H^{i}(X_{n}) \to H^{i}(Y_{n-1})
$$

is an isomorphism in dimension $i \leqslant n - 2$, a monomorphism in dimension $i = n - 1$. We have obtained variants
of these results in the framework of schemes, for $\pi_{0}$, $\pi_{1}$, `Pic`, valid moreover without non-singularity
hypotheses to a large extent, cf. Exp. XII. Moreover, in the elimination of non-singularity hypotheses, we have used in
an essential way "local" variants of these global Lefschetz theorems. All this suggests the following problems, which
doubtless will have to be attacked simultaneously[^XIII-4-1].

**Problem 4.1.**

<!-- label: XIII.4.1 -->

Let $X$ be an analytic space, $Y$ a closed analytic part of $X$ (or simply a closed part?[^N.D.E-XIII-12]) such that for
every $x \in Y$, the local ring $\mathcal{O}_{X,x}$ is a complete intersection. Let $n$ be the complex codimension of
$Y$ in $X$. Is the canonical homomorphism

$$
\pi_{i}(X - Y) \to \pi_{i}(X)
$$

<!-- original page 146 -->

an isomorphism for $i \leqslant n - 2$, and an epimorphism for $i = n - 1$?

In this problem and the following ones, one supposes evidently implicitly a base-point chosen to define the homotopy
groups. To state the next problem, one must define, for an analytic space $X$ (more generally, for a locally
path-connected space) and $x \in X$, local invariants $\Pi^{x}_{i}(X)$[^XIII-4-2].

<!-- original page 186 -->

To do this, one chooses a non-constant map $f$ from the interval `[0, 1]` into $X$, such that $f(0) = x$ and
$f(t) \neq x$ for $t \neq 0$ (such maps exist if $x$ is not an isolated point). Then for every neighborhood $U$ of $x$,
there exists an $\epsilon > 0$ such that $0 < t < \epsilon$ implies $f(t) \in U$, and the homotopy groups
$\pi_{i}(U - x, f(t))$ are essentially independent of $t$ (they are, for varying $t$, related by a transitive system of
isomorphisms); one can denote them $\pi_{i}(U - x, f)$. One then sets

```text
Π^x_i(X) = lim_{← U} πᵢ₋₁(U − x, f),
```

the inverse limit being taken over the system of open neighborhoods $U$ of $x$. Strictly speaking, this limit depends on
$f$, and should be denoted $\Pi^{x}_{i}(X, f)$, but one verifies that for varying $f$, these groups are isomorphic to
each other[^XIII-4-3]; more precisely, they form a local system on the space of paths of the type envisaged issuing from
$x$. These invariants are the homotopical version of the local cohomology invariants $H^{x}_{i}(F)$ for a sheaf $F$ on
$X$, introduced in I, and should play the role of relative local homotopy groups of $X$ modulo $X - x$. Their vanishing
for $i \leqslant n$ and for every $x \in Y$, where $Y$ is a closed part of $X$ of topological dimension $\leqslant d$,
should entail that the homomorphisms

$$
\pi_{i}(X - Y) \to \pi_{i}(X)
$$

are bijective for $i < n - d$, and surjective for $i = n - d$[^XIII-4-4]. From this point of view, 4.1 would imply (for
$Y$ reduced to a point) a conjecture of purely local nature, expressing itself by

```text
Π^x_i(X) = 0   for i ⩽ n − 1
```

when $X$ is a complete intersection of dimension $n$ at $x$.

<!-- original page 147 -->

As an example of local invariants $\Pi^{x}_{i}(X)$, note that if $x$ is a non-singular point of $X$ of complex dimension
$n$, then

<!-- original page 187 -->

$$
\Pi^{x}_{i}(X) = \pi_{i-1}(S^{2n-1}),
$$

where $S^{2n-1}$ denotes the sphere of dimension $2n - 1$. In particular in this case $\Pi^{x}_{i}(X) = 0$ for
$i \leqslant 2n - 1$, which corresponds to the fact that if from a topological manifold $X$ one removes a closed part
$Y$ of codimension $\geqslant m$, then $\pi_{i}(X - Y) \to \pi_{i}(X)$ is an isomorphism for $i \leqslant m - 2$ and an
epimorphism for $i = m - 1$.

This being said:

**Problem 4.2.**

<!-- label: XIII.4.2 -->

Let $X$ be an analytic space, $x \in X$, $t$ a section of $\mathcal{O}_{X}$ vanishing at $x$, $Y$ the set of zeros of
$t$. Suppose the following conditions satisfied:

a) $t$ is regular at $x$ (i.e. not a zero-divisor at $x$, a hypothesis perhaps superfluous, moreover).

b) At the points $x'$ of $X - Y$ near $x$, $\mathcal{O}_{X,x'}$ is a complete intersection (a hypothesis which should be
replaceable by the following more general one if 4.1 is true: for $x'$ as above, $\Pi^{x'}_{i}(X) = 0$ for
$i \leqslant n - 1$).

c) At the points $y$ of $Y - {x}$ near $x$, one has

$$
prof \mathcal{O}_{X,y} \geqslant n
$$

(it suffices for example that one have $prof \mathcal{O}_{X,x} \geqslant n$).

Under these conditions, is the canonical homomorphism

$$
\Pi^{x}_{i}(Y) \to \Pi^{x}_{i}(X)
$$

an isomorphism for $i \leqslant n - 2$, an epimorphism for $i = n - 1$?

Here finally is a global variant of 4.2, which should be deduced from it by consideration of the projecting cone at its
origin, and which would generalize the classical Lefschetz theorems:

**Problem 4.3.**

<!-- label: XIII.4.3 -->

<!-- original page 188 -->

Let $X$ be a projective analytic space, equipped with an ample invertible Module $L$, $t$ a section of $L$, $Y$ the set
of zeros of $t$. Suppose:

a) $t$ is a regular section (hypothesis perhaps superfluous).

b) For every $x \in X - Y$, $\mathcal{O}_{X,x}$ is a complete intersection (should be replaceable by
$\Pi^{x}_{i}(X) = 0$ for $i \leqslant n - 1$).

c) For every $x \in Y$, $prof \mathcal{O}_{X,x} \geqslant n$.

Under these conditions, is the homomorphism

$$
\pi_{i}(Y) \to \pi_{i}(X)
$$

an isomorphism for $i \leqslant n - 2$, an epimorphism for $i = n - 1$?

<!-- original page 148 -->

We shall leave it to the reader to state analogous conjectures of cohomological nature[^XIII-4-5], the hypotheses and
conclusions then bearing on local cohomological invariants (with coefficients in a given group). In any case, the key
result seems bound to be 4.2, when hypothesis b) there is taken in the form just discussed, — whether one places oneself
from the point of view of homology, or of homotopy.

We have stated these conjectures in the transcendental setting, in the hope of interesting topologists in them and
convincing them that "Lefschetz"-type questions are far from being closed. Of course, now that we are about to dispose
of a good theory of cohomology of schemes (with finite coefficients), thanks to the recent work of M. Artin, the same
questions arise in the framework of schemes, and it is difficult to doubt that they will not receive a positive answer,
in the near future[^XIII-4-6].

## 5. Problems related to local Picard groups

<!-- label: XIII.5 -->

<!-- original page 189 -->

A first fundamental problem, signaled for the first time by Mumford [5] in a particular case, is the following. Let $A$
be a complete local ring with residue field $k$, $X = \operatorname{Spec}(A)$, $U = \operatorname{Spec}(A) - {a}$, where
$a$ is the maximal ideal of $A$, i.e. the closed point of $\operatorname{Spec}(A)$. One proposes to construct a strict
projective system $G$ of locally algebraic groups `Gᵢ` over $k$, and a natural isomorphism

$$
\operatorname{Pic}(U) \simeq G(k)
$$

<!-- label: eq:XIII.5.plus -->

where one of course sets `G(k) = lim_{← } Gᵢ(k)`. Heuristically, one proposes to "put an algebraic group structure" (or,
at least, pro-algebraic, in a suitable sense) on the group $\operatorname{Pic}(U)$.

It is evident that as it stands, the problem is not precise enough, for the datum of an isomorphism (+) is far from
characterizing the pro-object $G$. If $A$ contains a subfield, still denoted $k$, that is a field of representatives,
one can make the problem precise by requiring that for a variable extension $k'$ of $k$, one have an isomorphism,
functorial in $k'$:

$$
\operatorname{Pic}(U') \simeq G(k')
$$

<!-- label: eq:XIII.5.plus-prime -->

where $U'$ is the open part analogous to $U$ in $\operatorname{Spec}(A')$, $A' = A \hat{\otimes}_{k} k'$. One can
proceed in an analogous way even if $A$ has no field of representatives, provided that $k$ is perfect, which then
permits one to construct functorially an $A'$ "by residual extension $k'/k$". Moreover, when $A$ admits a field of
representatives, the algebraic structure that one will find on $\operatorname{Pic}(U)$ will depend essentially on the
choice of this field of representatives (as one sees already on the projecting cone of an elliptic curve); it seems
therefore that one must start from a "pro-algebraic ring over $k$" in the sense of Greenberg [3], in order to arrive at

<!-- original page 149 -->

defining the pro-object $G$. It is moreover conceivable that in the case where there is no given field of
representatives, one finds only a projective system of quasi-algebraic groups in the sense of Serre, or rather
quasi-locally-algebraic groups

<!-- original page 190 -->

(the groups `Gᵢ` obtained will not in general be of finite type over $k$, but only locally of finite type over $k$). It
is even possible that one will find in general only a still weaker structure on $\operatorname{Pic}(U)$, of the kind
encountered by Néron [6] in his theory of degeneration of abelian varieties defined over local fields.

A method for attacking the problem, also introduced by Mumford, consists in desingularizing $X$, i.e. in considering a
projective birational morphism $Y \to X$ with $Y$ regular. When $U$ is regular (i.e. $a$ is an isolated singular point),
one can often find $Y$ in such a way that $Y|_{U} = V \to U$ is an isomorphism. In this case, one will therefore have

```text
Pic(U) ≃ Pic(V) ≃ Pic(Y) / Im ℤ^I,
```

where $I$ is the set of irreducible components of the fiber $Y_{a}$ (each of these defining an element of
$\operatorname{Pic}(Y)$, being a locally principal divisor, thanks to $Y$ regular). On the other hand, using the
technique of formal geometry EGA III 4 and 5, notably the existence theorem, one finds

```text
Pic(Y) ≃ lim_{← } Pic(Y_n),
```

where $Y_{n} = Y \otimes_{A} A_{n}$, $A_{n} = A/\mathfrak{m}^{n+1}$. When $A$ admits a field of representatives $k$, one
has at one's disposal the theory of Picard schemes of the projective schemes $Y_{n}$ over $k$, hence one has

$$
\operatorname{Pic}(Y_{n}) \simeq \operatorname{Pic}_{Y_{n}/k}(k).
$$

This therefore furnishes a construction of a projective system of locally algebraic groups
$\operatorname{Pic}_{Y_{n}/k} / Im \mathbb{Z}^{I}$, which is the desired system[^N.D.E-XIII-13]. In the case envisaged
here, one can moreover see (using that $a$ is an isolated singular point) that the connected components of the
universal-image subgroups in this projective system form an essentially constant projective system, so that in this case
one finds a locally algebraic group $G$ as solution of the problem. If one supposes furthermore $A$ normal of dimension
2, then a remark of Mumford (stating that the intersection matrix of the components of $Y_{a}$ in $X$ is negative
definite[^N.D.E-XIII-14]) implies that $G$ is even

<!-- original page 191 -->

<!-- original page 150 -->

an algebraic group, i.e. of finite type over $k$ (the number of its connected components being moreover equal to the
determinant of the intersection matrix envisaged a moment ago).

If on the contrary $a$ is not an isolated singularity, one convinces oneself by examples (with $A$ of dimension 2) that
one finds a projective system of algebraic groups, not reducing to a single algebraic group.

Once one had at one's disposal a good notion of "local Picard scheme", there would be occasion to strengthen the notion
of parafactoriality, by saying that $A$ is "geometrically parafactorial" when not only $A$ and even `Â` are
parafactorial, but the local Picard scheme $G(\hat{A})$ is the trivial group (which is stronger, when the residue field
is not algebraically closed, than saying that $G$ has no other rational point over $k$ than the unit). One realizes the
necessity of a strengthened notion of parafactoriality by recalling that there exist complete normal local rings of
dimension 2 that are factorial, but that admit finite étale algebras that are not[^N.D.E-XIII-15]. A "geometrically
factorial" local ring would then be a normal ring $A$ such that all the localizations of dimension $\geqslant 2$ are
geometrically parafactorial, or better, such that the localizations of `Â` are parafactorial[^XIII-5-1]. Of course, it
would be interesting to find a "good" definition of these notions, independent of the theory, still to be done, of local
Picard schemes[^N.D.E-XIII-16].

It is in any case plausible that one will need these notions if one wishes to obtain statements of the following type:
Let $A$ be a "good ring" (for example, an algebra of finite type over $\mathbb{Z}$, or over a complete local ring, for
example over a field). Let $U$ be the set of $x \in X = \operatorname{Spec}(A)$ such that $\mathcal{O}_{X,x}$ is
"geometrically factorial"; is $U$ open? Or again: Let $f : X \to Y$ be a flat morphism of finite type with $Y$ locally
noetherian, let $U$ be the set of $x \in X$ such that $\mathcal{O}_{X_{f(x)},x}$ is "geometrically factorial"; is $U$
open, at least under sympathetic supplementary conditions on $f$? I doubt that with the usual notion of factorial ring,
there exist true statements of this type.

<!-- original page 192 -->

We have raised here, in a particular case, the question of the study of geometric properties of "variable" local rings,
for example the $\mathcal{O}_{X,x}$ as $x$ ranges over a prescheme $X$. When $X$ is a scheme of finite type over a
field, for example, one knows[^N.D.E-XIII-17] that there exists on $X$ a projective system of finite algebras
$P^{X/k}_{n}$ (obtained by completing $X \times_{k} X$ along the diagonal), whose fiber at every point $x \in X$
rational over $k$ is isomorphic to the projective system of $\mathcal{O}_{X,x}/\mathfrak{m}^{n+1}_{X}$. It is then
natural to relate the study of the completions of the local rings $\mathcal{O}_{X,x}$, for varying $x$, to that of the
"algebraic family of complete local rings" given by the $P_{n}$, by noting that for every $x \in X$ (rational over $k$
or not), one obtains a complete local ring

```text
P_∞(x) = lim_{← } P_n(x)
```

(where $P_{n}(x)$ = reduced fiber $P_{n} \otimes_{\mathcal{O}_{X,x}} k(x)$). A particular interest will attach for
example to the complete ring thus associated to the generic point, and one will expect that its algebraic-geometric
properties (expressing themselves for instance by its local Picard groups, or homotopy groups, or homology groups), will
be essentially those of the completions $\hat{\mathcal{O}}_{X,x}$ for $x$ in a suitable dense open $U$.

One can, in general, propose to make the simultaneous study of the complete local rings obtained in this way from an
adic projective system $(P_{n})$ of finite algebras over a given scheme $X$. It is plausible that one will find, subject
to certain regularity conditions (such as the flatness of the $P_{n}$), that the local homotopy groups arise from a
projective system of finite group schemes over $X$,

<!-- original page 193 -->

and that one will have analogous results for the local Picard groups. As regards the latter, a first interesting case
that deserves to be investigated is that where one starts from an algebraic surface $X$ having singular curves, and one
proposes to study the local Picard schemes at variable points on them, in terms of a suitable pro-group scheme defined
on the singular locus.

## 6. Comments[^XIII-6-1]

<!-- label: XIII.6 -->

<!-- original page 194 -->

The point of view of "étale cohomology" of schemes and recent progress in this theory lead us to make precise and at the
same time to broaden certain of the problems posed. For the notion of "topology" and of "étale topology of a scheme", I
refer to M. Artin, *Grothendieck Topologies*, Harvard University 1962 (mimeographed notes)[^XIII-6-2].

This theory, by a finer notion of localization than that furnished by the traditional "Zariski topology", leads one to
attach a particular interest to *strictly local rings*, i.e. henselian local rings with separably closed residue field.
For every local ring $A$ with residue field $k$, and every separable closure $k'$ of $k$, one can find a local
homomorphism of $A$ into a strictly local ring $A'$, the strictly local closure of $A$, with residue field $k'$, having
an obvious universal property. $A'$ is henselian, flat over $A$, and $A' \otimes_{A} k \simeq k'$; it is noetherian if
and only if $A$ is. (Cf. loc. cit. Chap. III, section 4)[^XIII-6-3].

<!-- original page 152 -->

If $X$ is a prescheme, and $x$ a point of $X$, $x'$ a point above $x$, the spectrum of a separable closure $k'$ of
$k = k(x)$, one is led to define the *strictly local ring of $X$ at $x'$*, $\mathcal{O}'_{X,x'}$, as the strictly local
closure of the usual local ring $\mathcal{O}_{X,x}$, relatively to the residual extension $k'/k$. It is the strictly
local rings at the "geometric" points of $X$ that, from the point of view of the étale topology, are supposed to reflect
the local properties of the prescheme $X$. They also play, in many respects, the role that one used to assign to the
completions of the local rings of $X$ (say, at the points with algebraically closed residue field), while remaining
"closer" to $X$ and permitting an easier passage to "neighboring points".

It is then in order to take up again a good number of questions, that one generally poses for complete local rings
(eventually restricted to having an algebraically closed residue field), for noetherian henselian local rings (resp.

<!-- original page 195 -->

noetherian strictly local rings). Thus the topological problems raised in nos 2 and 3 are posed more generally for
strictly local rings. One can moreover state conjecturally, for "good" strictly local rings, certain properties of
simple connectedness and acyclicity for the geometric fibers of the canonical morphism
$\operatorname{Spec}(\hat{A}) \to \operatorname{Spec}(A)$, which would show that for many "topological"-nature
properties, it amounts to the same to prove them for the ring $A$, or for its completion `Â`. Certain results already
obtained in this direction[^XIII-6-4] allow one to hope that one will soon have at one's disposal complete results in
this direction.

The notion of étale localization furnishes a definition that seems reasonable of the notion of "geometrically
parafactorial" or "geometrically factorial" local ring (the need for which was indicated in no 5, p. 150): one will call
thus a local ring whose strictly local closure is parafactorial, resp. factorial. Hypotheses of this nature introduce
themselves effectively in a natural way in the study of the étale cohomology of preschemes[^N.D.E-XIII-18]. Thus, if $X$
is a locally noetherian prescheme whose strictly local rings are factorial (i.e. whose ordinary local rings are
"geometrically factorial"), one shows that the $H^{i}(X_{\acute{e}}t, \mathbf{G}_{m})$

<!-- original page 153 -->

are torsion groups for $i \geqslant 2$ (which allows one sometimes to express these groups in terms of cohomology groups
with coefficients in the groups $\mu_{n}$ of $n$-th roots of unity), and if $X$ is integral with fraction field $K$, the
natural homomorphism $H^{2}(X_{\acute{e}}t, \mathbf{G}_{m}) \to H^{2}(K, \mathbf{G}_{m}) = Br(K)$ is
injective[^N.D.E-XIII-19]; examples show that these conclusions can fail, even for $X$ local, if one supposes only $X$
factorial instead of geometrically factorial[^XIII-6-5].

Concerning the problems of local and global Lefschetz type raised in 3.4[^TRANSLATOR-NOTE-XIII-1], and their analogues
in scheme theory, the homological version of these questions has been considerably clarified, all resulting formally
from three general theorems: one concerning the cohomological dimension of certain affine schemes (resp. of Stein
spaces), such as affine schemes $X$ of finite type over an algebraically closed field: their cohomological dimension is
$\leqslant \dim X$ ("affine Lefschetz theorem")[^XIII-6-6];

<!-- original page 196 -->

the other being a duality theorem for the cohomology (with discrete coefficients) of a projective morphism[^XIII-6-7],
and finally the last a local duality theorem of analogous nature[^XIII-6-8]. In Algebraic Geometry, only this last is
not proved at the time of writing these lines (it is however proved in characteristic 0, using Hironaka's resolution of
singularities). Moreover, in the transcendental setting, one disposes from now on of global and local duality, recently
demonstrated by Verdier[^N.D.E-XIII-20]. Let us limit ourselves to indicating that in the statement of the homological
versions of problems 4.2 and 4.3 (which from now on deserve the name of conjectures), the conditions a) and c) "at
infinity" are certainly superfluous; only the local cohomological structure of $X - Y$ is important, which one will
suppose for example locally a complete intersection of dimension $\geqslant n$. Moreover, in 4.3 say, the fact that $Y$
is a hyperplane section should not play a role, and should be replaceable by the sole hypothesis that $X$ is compact and
$X - Y$ is Stein (i.e. in the case of Algebraic Geometry, $X$ is proper over $k$ and $X - Y$ affine; as we said, the
homological version of this conjecture is demonstrated for algebraic spaces over the field $\mathbb{C}$)[^XIII-6-9].

<!-- Editorial note: The source says "3.4" but the problems referenced are those of section 4 (4.2, 4.3). The reading
"section 4" (or "no 4") is consistent with the surrounding discussion of Lefschetz-type problems and the conjectures
A–D below; we have kept the source's "3.4" literally and flagged it. -->

In the definition (p. 146) of the $\Pi^{x}_{i}(X)$, one must suppose $i \geqslant 2$. For $i = 0, 1$, there is no
reasonable definition of the $\Pi^{x}_{i}(X)$; one should replace them by $H^{x}_{0}(X)$ and $H^{x}_{1}(X)$, defined
respectively as the cokernel and the kernel in the natural homomorphism

```text
lim_{← } H⁰(U − {x}, ℤ) → lim_{← } H⁰(U, ℤ).
```

At a pinch, and for convenience of formulation, one can set $\Pi^{x}_{i}(X) = H^{x}_{i}(X)$ for $i \leqslant 1$;
otherwise one must complete the subsequent assertions concerning the $\Pi^{x}_{i}$ by the corresponding assertions for
$H^{x}_{0}$, $H^{x}_{1}$. If $x$ is an isolated point of $X$, it is appropriate to set $\Pi^{x}_{i}(X) = 0$ for
$i \neq 0$, $\Pi^{x}_{0}(X) = H^{x}_{0}(X) = \mathbb{Z}$.

<!-- original page 197 -->

The assertion that the $\Pi^{x}_{i}(U, f)$ be isomorphic to each other is true only when $X$ is not disconnected by $x$
in a neighborhood of $x$, i.e. if $\Pi^{x}_{i}(X) = 0$ for $i = 0, 1$. In the general case $\Pi^{x}_{i}(X)$ can
designate only a family of groups, not necessarily isomorphic to each other; however the expression $\Pi^{x}_{i}(X) = 0$
retains an obvious sense.

Page 146, where I predict that the vanishing of the local homotopy invariants $\Pi^{x}_{i}(X)$ for $x \in Y$,
$i \leqslant n$, should entail the bijectivity of $\pi_{i}(X - Y) \to \pi_{i}(X)$ for $i < n - d$, the surjectivity for
$i = n - d$, it is appropriate to be cautious, failing to be able to dispose in the present context (as in Algebraic
Geometry) of "general" points at which the local conditions will also have to apply. It will doubtless be necessary, for
this reason, to call upon *relative local homotopy invariants*

```text
Π^Y_i(X, f) = Π^Y_i(X, x) = lim_{← U} πᵢ₋₁(U − U ∩ Y, f(t))   for i ⩾ 2,
```

(and an *ad hoc* definition as above for $i = 0, 1$), where $Y$ is a closed part of $X$; or to make up for the absence
of general points by expressing the hypotheses on $X$ in terms of properties of topological nature (for the étale
topology) of the spectra of the local rings of $X$, which allows one to recover general points. The same reservation
applies to the generalization of conjectures 4.2 and 4.3 to the case where $X - Y$ is not assumed locally a complete
intersection, a generalization suggested in the statement of conditions b) of these conjectures.

To formulate the expurgated versions of conjectures 4.2 and 4.3 suggested by the results to which we alluded above, it
is appropriate to pose:

<!-- original page 155 -->

**Definition 1.**

<!-- label: XIII.6.def1 -->

Let $X$ be a topological space, $Y$ a locally closed part of $X$, and $n$ an integer. One says that $X$ is of
*homotopical depth $\geqslant n$ along $Y$*, and one writes $prof htp_{Y}(X) \geqslant n$, if for every $x \in Y$, one
has $\Pi^{Y}_{i}(X, x) = 0$ for $i < n$.

<!-- original page 198 -->

It should be equivalent to say that for every open $X'$ of $X$, and every $x \in X' \cap U = U'$ (where $U = X - Y$),
the canonical homomorphism

```text
πᵢ(U', x) → πᵢ(X', x)
```

is an isomorphism for $i < n - 1$, a monomorphism for $i = n - 1$[^N.D.E-XIII-21].

**Definition 2.**

<!-- label: XIII.6.def2 -->

Let $X$ be a complex analytic space, $n$ an integer; one says that the *rectified homotopical depth of $X$* is
$n$[^XIII-6-10], if for every locally closed analytic part $Y$ of $X$, one has

```text
prof htp_Y(X) ⩾ n − dim Y
```

<!-- label: eq:XIII.6.x -->

(where, of course, $\dim Y$ denotes the complex dimension of $Y$).

It should be equivalent to say that for every irreducible analytic part $Y$ locally closed in $X$, there exists a closed
analytic part $Z$ of $Y$, of dimension $< \dim Y$, such that the relation (x) is valid for $Y - Z$ in place of $Y$. This
would permit one for example in definition 2 to confine oneself to the case where $Y$ is non-singular[^N.D.E-XIII-22].

The following conjecture, of purely topological nature, is in the nature of a "local Hurewicz theorem".

**Conjecture A** ("local Hurewicz theorem"[^N.D.E-XIII-23]).

<!-- label: XIII.6.A -->

Let $X$ be a topological space, $Y$ a locally closed part, subject if necessary to "smoothness"-type conditions such as
local triangulability of the pair $(X, Y)$, $n$ an integer $\geqslant 3$. For one to have $prof htp_{Y}(X) \geqslant n$,
it is necessary and sufficient that one have

<!-- original page 199 -->

```text
H^Y_i(ℤ_X) = 0   for i < n
```

<!-- original page 156 -->

(one then says that $X$ is of *cohomological depth $\geqslant n$ along $Y$*), and that the local fundamental groups

```text
Π^Y_2(X, x) = lim_{← U ∋ x} π₁(U − U ∩ Y)
```

be zero (one then says that $X$ is "pure along $Y$").

One notes that if $X$ is an analytic space, $Y$ an analytic subspace, and if $X$ is pure along $Y$, then for every
$x \in Y$, the local ring $\mathcal{O}_{X,x}$, as well as its localizations with respect to prime ideals containing the
ideal defining the germ $Y$ at $x$ (i.e. in the inverse image $Y_{x}$ of $Y$ by
$\operatorname{Spec}(\mathcal{O}_{X,x}) = X_{x} \to X$), are pure in the sense of Exp. X; it seems plausible that the
converse is also true. Analogous remarks hold for cohomological depth, it being understood that one works with the étale
topology on the $\operatorname{Spec}(\mathcal{O}_{X,x})$.

Conjecture 4.1 then generalizes to:

**Conjecture B** ("Purity"[^N.D.E-XIII-24]).

<!-- label: XIII.6.B -->

Let $E$ be an analytic space, $X$ an analytic part of $E$. Suppose that $E$ is non-singular of dimension $N$ at
$x \in X$, and that $X$ can be described by $p$ analytic equations in a neighborhood of every point. Then the rectified
homotopical depth of $X$ is $\geqslant N - p$.

In particular, a local complete intersection of dimension $n$ at every point would be of rectified homotopical depth
$\geqslant n$, which is none other than conjecture 4.1.

Conjectures 4.2 and 4.3 generalize respectively to:

**Conjecture C** ("Local Lefschetz"[^N.D.E-XIII-25]).

<!-- label: XIII.6.C -->

Let $X$ be an analytic space, $Y$ a closed analytic part, $x$ a point of $Y$; suppose that $X - Y$ is Stein in a
neighborhood of $x$ (for example $Y$ defined by an equation at $x$), and that $X - Y$ is of rectified homotopical depth
$\geqslant n$ in a neighborhood of $x$ (for example, is at every point of $X - Y$ near $x$ a complete intersection of
dimension $\geqslant n$, cf. conjecture B). Then the canonical homomorphism

$$
\Pi^{x}_{i}(Y) \to \Pi^{x}_{i}(X)
$$

is an isomorphism for $i < n - 1$, an epimorphism for $i = n - 1$.

<!-- original page 200 -->

**Conjecture D** ("Global Lefschetz"[^N.D.E-XIII-26]).

<!-- label: XIII.6.D -->

Let $X$ be a compact analytic space, $Y$ an analytic subspace of $X$ such that $U = X - Y$ is Stein, and is of

<!-- original page 157 -->

rectified homotopical depth $\geqslant n$ (for example a complete intersection of dimension $\geqslant n$ at every
point). Then the canonical homomorphism

$$
\pi_{i}(Y) \to \pi_{i}(X)
$$

is an isomorphism for $i < n - 1$, an epimorphism for $i = n - 1$.

**Remark.**

<!-- label: XIII.6.remark -->

When, in statements C and D, one replaces the hypothesis that $X - Y$ is Stein by the hypothesis that $X - Y$ is the
union of $c + 1$ Stein opens (which will play the role of a hypothesis of topological "concavity"), the conclusions must
be modified simply by replacing $n$ there by $n - c$[^N.D.E-XIII-27].

Let us make explicit, finally, in the "global case" D, the conjecture concerning the fundamental group (obtained by
taking $n = 3$):

**Conjecture D'** (Global Lefschetz for the fundamental group[^N.D.E-XIII-29]).

<!-- label: XIII.6.D-prime -->

Let $X$ be a compact analytic space over the field of complex numbers, $Y$ a closed analytic part such that $U = X - Y$
is Stein. Suppose moreover the following conditions satisfied:

(i) For every $x \in U$, the local fundamental group $\Pi^{x}_{2}(X, x)$ is zero (i.e. $X$ is "pure at $x$"), or only
the local ring $\mathcal{O}_{X,x}$ is pure.

(ii) The local rings of points of $U$ are "connected in dimension $\geqslant 2$".

(iii) The local rings of points of $U$ are of dimension $\geqslant 3$.

Under these conditions, for every $x \in Y$, the homomorphism

```text
π₁(Y, x) → π₁(X, x)
```

<!-- original page 201 -->

is an isomorphism (and $\pi_{2}(Y, x) \to \pi_{2}(X, x)$ an epimorphism).

One notes that the local conditions (i) (ii) (iii) on $U$ are satisfied if $U$ is locally a complete intersection of
dimension $\geqslant 3$. From the point of view of Algebraic Geometry, (when $U$ comes from a scheme, still denoted
$U$), the conditions (i) to (iii) correspond to hypotheses on the local invariants $\Pi^{x}_{i}(U)$, namely
$\Pi^{x}_{i}(U) = 0$ for $i < 3 - deg tr k(x)/k$, for points $x$ such that one has respectively
$deg tr k(x)/k = 0, 1, 2$. The global condition on $U$ ($U$ Stein) will be satisfied if $X$ is projective and $Y$ a
hyperplane section.

<!-- original page 158 -->

## Bibliography

<!-- label: XIII.bibliography -->

<!-- original page 202 -->

1. S. Abhyankar — "Local uniformisation on algebraic surfaces over ground fields of characteristics $p \neq 0$", *Annals
   of Math.* **63** (1956), p. 491–526.
1. W.L. Chow — "On the theorem of Bertini for local domains", *Proc. Nat. Acad. Sci. U.S.A.* **44** (1958), p. 580–584.
1. M. Greenberg — "Schemata over local rings", *Annals of Math.* **73** (1961), p. 624–648.
1. M. Kneser — "Über die Darstellung algebraischer Raumkurven als Durchschnitte von Flächen", *Archiv der Math.* **XI**
   (1960), p. 157–158.
1. D. Mumford — "The topology of normal singularities of an algebraic surface, and a criterion for simplicity", *Publ.
   Math. Inst. Hautes Études Sci.* **9** (1961), p. 5–22.
1. A. Néron — "Modèles minimaux des variétés abéliennes sur les corps locaux et globaux", *Publ. Math. Inst. Hautes
   Études Sci.* **21** (1964), p. 5–128.
1. A.H. Wallace — *Homology Theory of algebraic Varieties*, Pergamon Press, 1958.
1. S. Abhyankar — "Resolution of singularities of arithmetical surfaces", in *Arithmetical Algebraic Geometry*, Harper
   and Row, New York, 1965, p. 111–152.
1. [HL] H.A. Hamm & Lê Dũng Tráng — "Rectified homotopical depth and Grothendieck conjectures", in *The Grothendieck
   Festschrift, Vol. II*, Progr. Math., vol. **87**, Birkhäuser Boston, 1990, p. 311–351.

## Footnotes

## Translation ledger delta

| French                                               | English                                        | Note                                                                                                                                            |
| ---------------------------------------------------- | ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| problèmes et conjectures                             | problems and conjectures                       | Title-level. Per task spec.                                                                                                                     |
| relations entre résultats globaux et locaux          | relations between global and local results     | Section 1 title.                                                                                                                                |
| problèmes affines liés à la dualité                  | affine problems related to duality             | Section 1 title.                                                                                                                                |
| théorèmes de Bertini locaux                          | local Bertini theorems                         | Per task spec.                                                                                                                                  |
| théorèmes de Lefschetz cohomologiques / homotopiques | cohomological / homotopical Lefschetz theorems | Per task spec.                                                                                                                                  |
| théorèmes de Lefschetz locaux et globaux             | local and global Lefschetz theorems            | Section 4 title.                                                                                                                                |
| espaces analytiques complexes                        | complex analytic spaces                        | Per task spec.                                                                                                                                  |
| groupes de Picard locaux                             | local Picard groups                            | Per task spec.                                                                                                                                  |
| groupes d'homotopie locale                           | local homotopy groups                          | Per source index; notation $\Pi^{x}_{i}(X)$.                                                                                                    |
| $\pi ix$, $\pi i^{x}$                                | $\Pi^{x}_{i}$                                  | The "local πᵢ at x" of the source — rendered with capital pi-superscript to disambiguate from the ordinary πᵢ.                                  |
| profondeur homotopique                               | homotopical depth                              | Per glossary.                                                                                                                                   |
| profondeur homotopique rectifiée                     | rectified homotopical depth                    | Per glossary.                                                                                                                                   |
| profondeur cohomologique                             | cohomological depth                            | Per glossary.                                                                                                                                   |
| géométriquement factoriel / parafactoriel            | geometrically factorial / parafactorial        | Per task spec.                                                                                                                                  |
| anneau strictement local                             | strictly local ring                            | Per task spec.                                                                                                                                  |
| clôture strictement locale                           | strictly local closure                         | Standard.                                                                                                                                       |
| hensélisé strict                                     | strict henselization                           | Modern English for the strictly local closure in N.D.E. footnotes.                                                                              |
| corps de représentants                               | field of representatives                       | Standard for Cohen-structure-theory phrase.                                                                                                     |
| théorème de connexion (de Zariski)                   | (Zariski's) connection theorem                 | Standard.                                                                                                                                       |
| $J$-cofini                                           | $J$-cofinite                                   | Per Hartshorne usage cited in N.D.E.                                                                                                            |
| dualité affine                                       | affine duality                                 | Title of Conjecture 1.2.                                                                                                                        |
| « bon anneau »                                       | "good ring"                                    | Kept the scare quotes as in source.                                                                                                             |
| courbe immergée                                      | embedded curve                                 | Standard.                                                                                                                                       |
| « tame » (groupe fondamental)                        | "tame" (fundamental group)                     | Kept the English loanword in scare quotes as in source.                                                                                         |
| anneaux locaux variables                             | "variable" local rings                         | Kept scare quotes.                                                                                                                              |
| sous-schéma fermé                                    | closed subscheme                               | Standard.                                                                                                                                       |
| section hyperplane                                   | hyperplane section                             | Per glossary.                                                                                                                                   |
| schéma dual                                          | dual scheme                                    | Standard.                                                                                                                                       |
| fibre géométrique                                    | geometric fiber                                | Standard.                                                                                                                                       |
| $\operatorname{Spec}(\hat{A})$ / complété            | $\operatorname{Spec}(\hat{A})$ / completion    | Standard, hat preserved.                                                                                                                        |
| $prof htp_{Y}(X)$                                    | $prof htp_{Y}(X)$                              | Symbol preserved verbatim per source.                                                                                                           |
| « théorème de Hurewicz local »                       | "local Hurewicz theorem"                       | Kept scare quotes; per source.                                                                                                                  |
| Stein                                                | Stein                                          | Standard analytic-geometry term, kept.                                                                                                          |
| « concavité » topologique                            | topological "concavity"                        | Kept scare quotes.                                                                                                                              |
| pur le long de $Y$                                   | pure along $Y$                                 | Per Exp. X usage.                                                                                                                               |
| connexe en dimension $\geqslant k$                   | connected in dimension $\geqslant k$           | Standard.                                                                                                                                       |
| théorème de Bertini                                  | Bertini's theorem                              | Standard.                                                                                                                                       |
| anneau gradué / cône projetant                       | graded ring / projecting cone                  | Standard.                                                                                                                                       |
| anneau de coordonnées homogènes                      | homogeneous coordinate ring                    | Standard.                                                                                                                                       |
| schéma de Picard local                               | local Picard scheme                            | Per Boutot-era usage.                                                                                                                           |
| groupe pro-algébrique / quasi-algébrique             | pro-algebraic / quasi-algebraic group          | Standard.                                                                                                                                       |
| matrice d'intersection                               | intersection matrix                            | Standard.                                                                                                                                       |
| il y a tout lieu de penser                           | there is every reason to think                 | Per task modality table; not used in this Exposé (the surrounding modality leans on *il semble*, *plausible*, *on s'attend*, *il est tentant*). |
| il est tentant de                                    | it is tempting to                              | Translation of *il est tentant de*; preserves the speculative register.                                                                         |
| plausible                                            | plausible                                      | Kept as cognate; the source uses *il est plausible que* / *plausible que*. Preserves modality.                                                  |
| on s'attendra à ce que                               | one will expect that                           | Future-modal; preserves the projection of expectation forward.                                                                                  |
| il semble                                            | it seems                                       | Per modality table.                                                                                                                             |
| il doit être équivalent de dire                      | it should be equivalent to say                 | Preserves the projected-but-unproven equivalence.                                                                                               |
| doit pouvoir se remplacer                            | should be replaceable                          | Preserves the conditional / projected feasibility.                                                                                              |
| sans doute                                           | doubtless                                      | Per modality table.                                                                                                                             |
| il est difficile de douter que                       | it is difficult to doubt that                  | Litotes preserved.                                                                                                                              |
| à vrai dire                                          | actually                                       | Idiomatic English equivalent.                                                                                                                   |
| il est tentant de compléter                          | it is tempting to complete                     | Preserves speculative register.                                                                                                                 |
| N.D.E.                                               | *N.D.E.*                                       | Editor's note, italicized abbreviation per glossary.                                                                                            |
| $7\to$, $-\to$, $\sim=$                              | $\mapsto$, $\to$, $\cong$                      | OCR repair, per glossary.                                                                                                                       |
| $\pi 1$, $\pi 0$, $\pi i$                            | $\pi_{1}$, $\pi_{0}$, $\pi_{i}$                | Unicode subscripts in backticks, per task spec.                                                                                                 |

[^N.D.E-XIII-1]: *N.D.E.* In fact, this generalization is not to be found there; see note below, and the editor's note
    (4) on page 2.

[^XIII-1-1]: Cf. *Séminaire Hartshorne*, cited at the end of Exp. IV.

[^XIII-1-2]: This conjecture, and conjecture 1.2 below, are false, as R. Hartshorne has shown, "Affine duality and
    cofinite modules", *Invent. Math.* **9** (1969/70), p. 145–164, section 3.

[^N.D.E-XIII-2]: *N.D.E.* However, if $A$ is complete local (resp. regular of positive characteristic) and $J$ is the
    maximal ideal, the statement is true for $M$ finitely generated (resp. $M = A$), cf. (Hartshorne R., "Affine duality
    and cofinite modules", *Invent. Math.* **9** (1969/70), p. 145–164, corollary 1.4) (resp. (Huneke C. & Sharp R.,
    "Bass numbers of local cohomology modules", *Trans. Amer. Math. Soc.* **339** (1993), no. 2, p. 765–779), which
    moreover contains far stronger results). For completely different methods ($\mathcal{D}$-modules) allowing one to
    approach characteristic zero, see (Lyubeznik G., "Finiteness properties of local cohomology modules (an application
    of $\mathcal{D}$-modules to commutative algebra)", *Invent. Math.* **113** (1993), no. 1, p. 41–55); see also by the
    same author "Finiteness properties of local cohomology modules for regular local rings of mixed characteristic: the
    unramified case", *Comm. Algebra* **28** (2000), no. 12, p. 5867–5882, Special issue in honor of Robin Hartshorne,
    and "Finiteness properties of local cohomology modules: a characteristic-free approach", *J. Pure Appl. Algebra*
    **151** (2000), no. 1, p. 43–50. The notion of cofinite module has evolved since under Hartshorne's aegis. One says
    that $M$ is *$J$-cofinite* if its support is contained in $V(J)$ and if all $Ext^{i}_{A}(A/J, H^{i}_{J}(M))$ are
    finitely generated. On this subject, see for example (Delfino D. & Marley Th., "Cofinite modules and local
    cohomology", *J. Pure Appl. Algebra* **121** (1997), no. 1, p. 45–52).

[^XIII-1-3]: This conjecture, false as it stands, has nonetheless been established in a rather close form by R.
    Hartshorne, "Affine duality and cofinite modules", *Invent. Math.* **9** (1969/70), p. 145–164.

[^XIII-1-4]: Part (i) of this conjecture is proved by R. Hartshorne when $X$ is smooth; cf. *Ample subvarieties of
    algebraic varieties*, Notes written in collaboration with C. Musili, Lect. Notes in Math., vol. 156,
    Springer-Verlag, Berlin–New York, 1970, theorem III.5.2. The same author also found an example for (ii), cf. R.
    Hartshorne, "Cohomological dimension of algebraic varieties", *Ann. of Math. (2)* **88** (1968), p. 403–450, example
    page 449.

[^N.D.E-XIII-3]: *N.D.E.* Hartshorne has proved (Hartshorne R., "Cohomological dimension of algebraic varieties", *Ann.
    of Math. (2)* **88** (1968), p. 403–450) that the cohomology $H^{n-1}(\mathbf{P}^{n}_{k} - X, F)$ is zero for $F$
    coherent and $X$ of positive dimension ($k$ algebraically closed). In fact, thanks essentially to Serre duality and
    to Lichtenbaum's theorem — vanishing of the cohomology of coherent sheaves in maximal dimension of irreducible
    non-complete quasi-projective varieties — one reduces to proving that the formal completion
    $\hat{\mathbf{P}}^{n}_{k}$ and $X$ have the same field of rational functions. This is the difficult point (theorem
    7.2 of *loc. cit.*); in other words, $\mathbf{P}^{n}_{k}$ is *G3* in the terminology of (Hironaka H. & Matsumura H.,
    "Formal functions and formal embeddings", *J. Math. Soc. Japan* **20** (1968), p. 52–82). These authors proved
    independently the preceding results, and in fact much better ones. They proved that $X$ is universally *G3* and
    computed the field of rational functions of the formal completion of an abelian variety along a subvariety of
    positive dimension. It is in this article that the conditions *G1*, *G2*, *G3*, now classical, appear for the first
    time.

[^XIII-1-5]: The question has just been resolved in the affirmative by R. Hartshorne (Hartshorne R., "Ample vector
    bundles", *Publ. Math. Inst. Hautes Études Sci.* **29** (1966), p. 63–94, theorem 8.1) and H. Hironaka.

[^N.D.E-XIII-4]: *N.D.E.* See conjecture 3.5 and the corresponding note.

[^N.D.E-XIII-5]: *N.D.E.* Write $K = \lim_{a \neq 0} A[1/a]$ and observe that $a \neq 0$ is $A$-regular.

[^XIII-2-1]: Cf. EGA IV 5.7.2.

[^XIII-2-2]: Cf. EGA IV 7.8.3 (i) (ii) (v).

[^N.D.E-XIII-6]: *N.D.E.* For a very beautiful direct proof, see (Fulton W. & Lazarsfeld R., "Connectivity and its
    applications in algebraic geometry", in *Algebraic geometry (Chicago, Ill., 1980)*, Lect. Notes in Math., vol. 862,
    Springer, Berlin–New York, 1981, p. 26–92, theorem 2.1). Cf. also [HL], cited in the editor's note (22) page 155.

[^N.D.E-XIII-7]: *N.D.E.* See the following editor's note.

[^N.D.E-XIII-8]: *N.D.E.* One now finds a proof of this conjecture in the literature, and so the preceding one must also
    be considered as proved as indicated above. One can also find two attempts at proofs, published earlier but alas
    unsuccessful, by Flenner and Trivedi. See Trivedi V., "Erratum: 'A local Bertini theorem in mixed characteristic'",
    *Comm. Algebra* **25** (1997), no. 5, p. 1685–1686. However, the editor has not verified that the proof is by now
    complete.

[^N.D.E-XIII-9]: *N.D.E.* The analogous statement is true for (connected) schemes $X$ of finite type over a separably
    closed field $k$ under the hypothesis of strong desingularization for all $k$-schemes (of finite type), in
    particular if $k$ is of characteristic zero or $X$ of dimension $\leqslant 2$. To this end one reduces to the case
    of quasi-projective surfaces by Lefschetz-type techniques developed by Mme Raynaud, cf. notes *supra*; see SGA 7.I,
    theorem II.2.3.1.

[^XIII-3-1]: The possibility of "resolving" $A$ is proved now in full generality by Abhyankar [8].

[^N.D.E-XIII-10]: *N.D.E.* This problem is, as of autumn 2004, still open.

[^N.D.E-XIII-11]: *N.D.E.* The statements are made precise in the Comments (section 6). The conjectures that appear
    there have become theorems, cf. the footnotes of section 6.

[^XIII-4-1]: The formulations 4.1 to 4.3 that follow are provisional. See conjectures A to D below, in "comments on Exp.
    XIII", for more satisfactory formulations, as well as Exp. XIV.

[^N.D.E-XIII-12]: *N.D.E.* The meaning of this question is not clear; indeed, the very statement of the problem does not
    seem to have a sense in this case, since the codimension of $Y$ in $X$ is not defined when $Y$ is no longer assumed
    analytic.

[^XIII-4-2]: If $i \geqslant 2$. For the case $i \leqslant 1$, cf. Comments in no 6 below, page 154.

[^XIII-4-3]: At least if $x$ does not disconnect $X$ in a neighborhood of $x$, cf. Comments below, page 154.

[^XIII-4-4]: For a corrected formulation, cf. Comments below, page 154.

[^XIII-4-5]: Cf. Exp. XIV for the corresponding results in scheme theory.

[^XIII-4-6]: See previous note.

[^N.D.E-XIII-13]: *N.D.E.* The question has been greatly clarified by the results of Boutot (Boutot J.-F., *Schéma de
    Picard local*, Lect. Notes in Math., vol. 632, Springer, Berlin, 1978). In particular, if $A$ is a complete
    (noetherian) local $k$-algebra of depth $\geqslant 2$ such that $H^{2}_{\mathfrak{m}}(A)$ is finite-dimensional over
    $k$, the local Picard group is a group scheme locally of finite type over $k$, with tangent space at the origin
    $H^{2}_{\mathfrak{m}}(A)$. If $A$ is moreover normal of dimension $\geqslant 3$, Serre's normality criterion XI 3.11
    together with corollary V 3.6 ensure the required finiteness and, hence, the existence of the local Picard scheme.
    See also (Lipman J., "The Picard group of a scheme over an Artin ring", *Publ. Math. Inst. Hautes Études Sci.*
    **46** (1976), p. 15–86) for an approach closer to that of Grothendieck sketched above.

[^N.D.E-XIII-14]: *N.D.E.* Mumford D., "The topology of normal singularities of an algebraic surface and a criterion for
    simplicity", *Publ. Math. Inst. Hautes Études Sci.* **9** (1961), p. 5–22.

[^N.D.E-XIII-15]: *N.D.E.* Factorial rings with non-factorial henselization arise naturally when one studies moduli
    spaces of vector bundles. See for example (Drézet J.-M., "Groupe de Picard des variétés de modules de faisceaux
    semi-stables sur $\mathbf{P}^{2}$", in *Singularities, representation of algebras, and vector bundles (Lambrecht,
    1985)*, Lect. Notes in Math., vol. 1273, Springer, Berlin, 1987, p. 337–362). Strictly speaking, Drézet shows that
    the completion is not factorial, but in fact the proof gives the result for the henselization: the point is that
    Luna's étale slice theorem (Luna D., "Slices étales", in *Sur les groupes algébriques*, Mém. Soc. math. France, vol.
    33, Société mathématique de France, Paris, 1973, p. 81–105) describes the local ring of a quotient in the sense of
    invariant geometry near a semi-stable point locally for the étale topology.

[^XIII-5-1]: For a more flexible notion of "geometrically factorial" local ring, cf. Comments, page 152.

[^N.D.E-XIII-16]: *N.D.E.* See page 152: a local ring is geometrically factorial (resp. parafactorial) if its strict
    henselization is factorial (resp. parafactorial).

[^N.D.E-XIII-17]: *N.D.E.* See EGA IV.16.

[^XIII-6-1]: Written in March 1963.

[^XIII-6-2]: Or, preferably, SGA 4.

[^XIII-6-3]: Or EGA IV 18.8.

[^XIII-6-4]: Cf. M. Artin in SGA 4 XIX.

[^N.D.E-XIII-18]: *N.D.E.* See for example (Strano R., "The Brauer group of a scheme", *Ann. Mat. Pura Appl. (4)*
    **121** (1979), p. 157–169) where the hypothesis of geometric parafactoriality of the local rings of a scheme $X$
    sometimes allows one to show the coincidence of the Brauer groups of $X$ (computed in terms of Azumaya algebras) and
    of the cohomological Brauer group of $X$.

[^N.D.E-XIII-19]: *N.D.E.* The link between Brauer group and Picard group is intimate. Let us cite in this connection
    the following results of Saito (Saito S., "Arithmetic on two-dimensional local rings", *Invent. Math.* **85**
    (1986), no. 2, p. 379–414) in the case of surfaces, the first being local, the other global. Let $A$ be an excellent
    local ring of dimension 2, normal and henselian with finite residue field, and $X$ the complement of the closed
    point in $\operatorname{Spec}(A)$. Then one has a perfect duality of torsion groups
    $\operatorname{Pic}(X) \times Br(X) \to \mathbb{Q}/\mathbb{Z}$ — by Brauer group of $X$, one means cohomological
    Brauer group $Br(X) = H^{2}_{\acute{e}}t(X, \mathbf{G}_{m})$. In the global case, one has the following
    generalization of a result of Lichtenbaum (Lichtenbaum S., "Duality theorems for curves over $p$-adic fields",
    *Invent. Math.* **7** (1969), p. 120–136): let $k$ be the field of fractions of a complete discrete valuation ring
    $\mathcal{O}$ with finite residue field and $X$ a projective, smooth and geometrically complete curve over $k$. The
    group $\operatorname{Pic}^{0}(X)$ is equipped with the topology induced from the adic topology of $k$, and
    $\operatorname{Pic}(X)$ is the topological group that makes $\operatorname{Pic}^{0}(X)$ an open subgroup. Then one
    has a perfect duality of topological groups $\operatorname{Pic}(X) \times Br(X) \to \mathbb{Q}/\mathbb{Z}$. Note
    that this statement, which concerns curves, is of course proved by considering a regular (proper and flat) model of
    $X$ over $\mathcal{O}$: it is a result about surfaces.

[^XIII-6-5]: Cf. A. Grothendieck, *Le groupe de Brauer II* (Séminaire Bourbaki no 297, Nov. 1965), notably 1.8 and 1.11
    b.

[^XIII-6-6]: Cf. SGA 4 XIV.

[^XIII-6-7]: Cf. SGA 4 XVIII.

[^XIII-6-8]: Cf. SGA 5 I.

[^N.D.E-XIII-20]: *N.D.E.* See Verdier J.-L., "Dualité dans la cohomologie des espaces localement compacts", in
    *Séminaire Bourbaki, vol. 9*, Société mathématique de France, Paris, 1995, Exp. 300, p. 337–349.

[^XIII-6-9]: Cf. Exp. XIV.

[^N.D.E-XIII-21]: *N.D.E.* When the pair $(X, Y)$ is moreover polyhedral, this equivalence is true; cf. (Eyral C.,
    "Profondeur homotopique et conjecture de Grothendieck", *Ann. Sci. Éc. Norm. Sup. (4)* **33** (2000), no. 6, p.
    823–836).

[^XIII-6-10]: In the first edition of these notes, we had employed the term "true homotopical depth". In the present
    version, we follow EGA IV 10.8.1.

[^N.D.E-XIII-22]: *N.D.E.* All the conjectures that follow, suitably rectified if I dare say so, have become theorems
    thanks to the work of Hamm and Lê Dũng Tráng (Hamm H.A. & Lê Dũng Tráng, "Rectified homotopical depth and
    Grothendieck conjectures", in *The Grothendieck Festschrift, Vol. II*, Progr. Math., vol. 87, Birkhäuser, Boston,
    1990, p. 311–351), cited [HL] in what follows. As regards the two conjecturally equivalent definitions of rectified
    depth, they are even equivalent to a third, expressing itself in terms of Whitney stratification (cf. *loc. cit.*,
    theorem 1.4).

[^N.D.E-XIII-23]: *N.D.E.* As observed in [HL], example 3.1.3, this conjecture is false already for
    $X = {z \in \mathbb{C}^{n} \mid z^{2}_{1} + z^{3}_{2} + \cdots + z^{3}_{n} = 0}$, $n \geqslant 4$ and $Y$ reduced to
    the origin. But, suitably modified, it is true (theorem 3.1.4 of *loc. cit.*).

[^N.D.E-XIII-24]: *N.D.E.* This conjecture is proved, even in the case where $E$ is singular, in \[HL\]: it is theorem
    3.2.1.

[^N.D.E-XIII-25]: *N.D.E.* This conjecture is proved in [HL], even in its strong form of the remark that follows, cf.
    theorem 3.3.1 of *loc. cit.*

[^N.D.E-XIII-26]: *N.D.E.* This conjecture is again proved in [HL], even in its strong form of the remark that follows,
    cf. theorem 3.4.1 of *loc. cit.*

[^N.D.E-XIII-27]: *N.D.E.* Let us finally signal the following result of Fulton, to be compared with the Fulton-Hansen
    result cited in editor's note (4) page 127: let $X$ and $H$ be closed subschemes of $\mathbf{P}^{m}_{\mathbb{C}}$,
    $n$ the dimension of $X$ and $d$ the codimension of $H$. Then the map

    ```text
    πᵢ(X, X ∩ H) → πᵢ(𝐏^n_ℂ, H)
    ```

    is an isomorphism if $i \leqslant n - d$ and is surjective if $i = n - d - 1$; see (Fulton W., "Connectivity and its
    applications in algebraic geometry", in *Algebraic geometry (Chicago, Ill., 1980)*, Lect. Notes in Math., vol. 862,
    Springer, Berlin–New York, 1981, p. 26–92).

[^N.D.E-XIII-29]: *N.D.E.* This conjecture is demonstrated in [HL], cf. theorem 3.5.1 of *loc. cit.*


<!-- SOURCE: 14-profondeur-lefschetz-cohomologie-etale.md -->

# Exposé XIV. Depth and Lefschetz theorems in étale cohomology

*by Mme M. Raynaud, after unpublished notes of A. Grothendieck*[^XIV-0-1]

<!-- label: XIV -->

> **Editorial note.** Per Raynaud's opening footnote, this Exposé adopts the modern terminology in which *scheme*
> denotes what Exposés I–XIII of SGA 2 called *prescheme*, and *separated scheme* denotes what they called *scheme*.
> This Exposé therefore breaks with the prescheme/scheme convention used elsewhere in this translation; the shift is
> deliberate and matches Raynaud's own.

> **Typographic note.** Throughout this Exposé we write $R\Gamma_{Y}$ for the sheafified derived functor (underlined in
> source) and $R\Gamma_{Y}$ for the global one; context disambiguates. Likewise, $\mathcal{H}^{p}_{Y}(F)$ denotes the
> sheafified local cohomology and $H^{p}_{Y}(X, F)$ the global one.

<!-- original page 203 -->

In §1 we define a notion of "étale depth" which is, in étale cohomology, the analogue of the notion of depth studied in
III in the cohomology of coherent sheaves. After a technical part, we prove in §4 some "Lefschetz theorems", the central
theorem being 4.2. Let $X$ be a scheme, $Y$ a closed part of $X$, $U$ the complementary open set $X - Y$, and $F$ an
abelian sheaf on $X$ for the étale topology; in a general manner, the aim of the Lefschetz theorems is to show that, if
$F$ satisfies certain local conditions on $U$, expressible in terms of étale depth at the points of $U$, then under
certain supplementary global conditions on $U$ (for example $U$ affine), the natural map of étale cohomology groups

```text
H^i(X, F) → H^i(Y, F|Y)
```

is an isomorphism for values $i < n$, where $n$ is a certain explicit integer. By taking for $F$ a constant sheaf, one
obtains in this way conditions for $\pi_{0}(X)$ to equal $\pi_{0}(Y)$ and conditions for the abelianized fundamental
groups of $X$ and $Y$ to be the same. In §5, the introduction of a notion of "geometrical depth" enables us to give
useful particular cases of the Lefschetz theorems (5.7). Finally in §6 we mention some conjectures, concerning in
particular "non-commutative" variants of the theorems obtained.

## 1. Cohomological and homotopical depth

<!-- original page 204 -->

**1.0.** Fix the following notations. Let $X$ be a scheme[^XIV-1-1], $Y$ a closed part of $X$, $U$ the complementary
open set, and $i : Y = X - U \to X$ the canonical immersion. Let $\Gamma Y$ be the functor that, to an abelian sheaf on
$X$, associates the "sheaf of sections with support in $Y$", that is $\Gamma Y = i_{*} i^{!}$ (cf. SGA 4 IV 3.8 and VIII
6.6), and let $\Gamma_{Y}$ be the functor $\Gamma \circ \Gamma Y$ (where $\Gamma$ is the "global sections" functor).
Consider the derived category $D^{+}(X)$ and the derived functor $R\Gamma_{Y}$ (resp. $R\Gamma_{Y}$) of $\Gamma_{Y}$
(resp. of $\Gamma Y$) (cf. [3]). Given a complex $F$ of abelian sheaves on $X$ bounded below, we may consider it as an
element of $D^{+}(X)$; we then denote by $\mathcal{H}^{p}_{Y}(F)$ the $p$-th cohomology sheaf of $R\Gamma_{Y}(F)$
(sheafified) and by $H^{p}_{Y}(X, F)$ the $p$-th cohomology group of $R\Gamma_{Y}(F)$. The results of (SGA 4 V 4.3 and
4.4) extend trivially to $\mathcal{H}^{p}_{Y}(F)$ and $H^{p}_{Y}(X, F)$.

**Proposition 1.1.**

<!-- label: XIV.1.1 -->

Let $X$ be a scheme, $Y$ a closed part of $X$, $U$ the complementary open set, and $i : U \to X$ the canonical
immersion. Denote by $F$ either a sheaf of sets on $X$, a sheaf of groups on $X$, or a complex of abelian sheaves on $X$
bounded below. Fix the following notations: if $X' \to X$ is a morphism, $U'$ and $F'$ denote the inverse images of $U$
and $F$ on $X'$; furthermore, if $y$ is a geometric point of $X$, $\bar{X}$ denotes the strict localization of $X$ at
$y$ and `Ū`, $\bar{F}$ the inverse images of $U$ and $F$ on $\bar{X}$.

<!-- original page 205 -->

1°) Let $F$ be a sheaf of sets on $X$ and $n$ an integer $\leqslant 2$; then the following conditions are equivalent:

(i) The canonical morphism

```text
F → i_* i^* F
```

is injective if $n \geqslant 1$, bijective if $n \geqslant 2$.

(ii) For every scheme $X'$ étale over $X$, the canonical morphism

```text
H⁰(X′, F′) → H⁰(U′, F′)
```

is injective if $n \geqslant 1$, bijective if $n \geqslant 2$.

Suppose moreover that $U$ is retrocompact in $X$; then the preceding conditions are equivalent to the following:

(iii) For every geometric point $y$ of $Y$, the canonical morphism

```text
H⁰(X̄, F̄) → H⁰(Ū, F̄)
```

is injective if $n \geqslant 1$, and bijective if $n \geqslant 2$.

2°) Let $F$ be a sheaf of groups on $X$ and $n$ an integer $\leqslant 3$; then the following conditions are equivalent:

(i) The canonical morphism

```text
F → i_* i^* F
```

is injective if $n \geqslant 1$, bijective if $n \geqslant 2$, and if $n \geqslant 3$, in addition to the preceding
conditions, the pointed sheaf of sets $R^{1} i_{*} (i^{*} F)$ is null.

(ii) For every scheme $X'$ étale over $X$, the canonical morphism

```text
H⁰(X′, F′) → H⁰(U′, F′)
```

<!-- original page 206 -->

is injective if $n \geqslant 1$, bijective if $n \geqslant 2$, and moreover the canonical morphism

```text
H¹(X′, F′) → H¹(U′, F′)
```

is injective if $n \geqslant 2$, bijective if $n \geqslant 3$.

(ii bis) Identical to (ii), except in the case $n = 2$ where one only supposes $H^{0}(X', F') \to H^{0}(U', F')$
bijective.

Suppose moreover that $U$ is retrocompact in $X$; then the preceding conditions are also equivalent to the following:

(iii) For every geometric point $y$ of $Y$, the canonical morphism

```text
H⁰(X̄, F̄) → H⁰(Ū, F̄)
```

is injective if $n \geqslant 1$, bijective if $n \geqslant 2$; finally if $n \geqslant 3$, in addition to the preceding
conditions, $H^{1}(\bar{U}, \bar{F})$ is null.

3°) Let $F$ be a complex of abelian sheaves bounded below and $n$ an integer; then the following conditions are
equivalent:

(i) One has $\mathcal{H}^{p}_{Y}(F) = 0$ for $p < n$ (cf. 1.0).

(ii) For every scheme $X'$ étale over $X$, the canonical morphism

```text
H^p(X′, F′) → H^p(U′, F′)
```

is bijective for $p < n - 1$, injective for $p = n - 1$.

Suppose $U$ retrocompact in $X$, then the preceding conditions are also equivalent to the following:

(iii) For every geometric point $y$ of $Y$, the canonical morphism

```text
H^p(X̄, F̄) → H^p(Ū, F̄)
```

is bijective for $p < n - 1$, injective for $p = n - 1$.

<!-- original page 207 -->

In the case where $F$ is an abelian sheaf and $n \geqslant 2$, conditions (i) and (ii) are also equivalent to the
following:

(ii bis) For every scheme $X'$ étale over $X$, the canonical morphism

```text
H^p(X′, F′) → H^p(U′, F′)
```

is bijective for $p < n - 1$.

*Proof.*

1°) It is clear that (i) ⇔ (ii). Let us show that, if $U$ is retrocompact in $X$, (i) ⇔ (iii). Indeed, (i) amounts to
saying that for every geometric point $y$ of $X$, the morphism $F_{y} \to (i_{*} i^{*} F)_{y}$ is injective if
$n \leqslant 1$ and bijective if $n \leqslant 2$ (SGA 4 VIII 3.6). Since this morphism is bijective in any case when $y$
is a geometric point of $U$, one can restrict to geometric points $y$ of $Y$. Now it follows from the fact that $i$ is
quasi-compact and from (SGA 4 VIII 5.3) that the morphism

```text
F_y → (i_* i^* F)_y
```

is canonically identified with the morphism

```text
H⁰(X̄, F̄) → H⁰(Ū, F̄),
```

whence the equivalence of (i) and (iii).

2°) (i) ⇒ (ii). The assertions about $H^{0}$ follow from 1°). Let $i'$ be the canonical immersion of $U'$ into $X'$; the
assertions about $H^{1}$ follow from the exact sequence (SGA 4 XII 3.2)

```text
0 → H¹(X′, i′_* i′^* F′) → H¹(U′, F′) → H⁰(X′, R¹ i′_* (i′^* F′)).
```

<!-- original page 208 -->

(ii bis) ⇒ (i). By 1°), it suffices to show that, for $n \geqslant 3$, one has $R^{1} i_{*} (i^{*} F) = 0$. Now
$R^{1} i_{*} (i^{*} F)$ is the sheaf associated to the presheaf $X' \mapsto H^{1}(U', F')$, that is, by hypothesis, the
sheaf associated to the presheaf $X' \mapsto H^{1}(X', F')$, which is null.

(i) ⇔ (iii). Taking 1°) into account, the only thing that remains to see is that the relation
$R^{1} i_{*} (i^{*} F) = 0$ is equivalent to the fact that $H^{1}(\bar{U}, \bar{F}) = 0$ for every geometric point $y$
of $Y$. Since $R^{1} i_{*} (i^{*} F)$ is null outside $Y$, it amounts to the same to say that
$R^{1} i_{*} (i^{*} F) = 0$ or that $(R^{1} i_{*} (i^{*} F))_{y} = 0$ for every geometric point $y$ of $Y$. It then
suffices to note that, $i$ being quasi-compact, one has $(R^{1} i_{*} (i^{*} F))_{y} = H^{1}(\bar{U}, \bar{F})$ (SGA 4
VIII 5.3).

3°) (i) ⇒ (ii). Let $X'$ be a scheme étale over $X$; one has the exact sequence (SGA 4 V 4.5)

```text
(∗)    → H^p_{Y′}(X′, F′) → H^p(X′, F′) → H^p(U′, F′) →;
```

so (ii) is equivalent to $H^{p}_{Y'}(X', F') = 0$ for $p < n$ and for every scheme $X'$ étale over $X$. Consider then
the spectral sequence

```text
E_2^{pq} = H^p(X′, ℋ^q_{Y′}(F)) ⟹ H^{p+q}_{Y′}(X′, F′);
```

by hypothesis, $\mathcal{H}^{q}_{Y}(F) = 0$ for $q < n$, whence $E^{pq}_{2} = 0$ for $p + q < n$ and consequently
$H^{p}_{Y'}(X', F') = 0$ for $p < n$.

(ii) ⇒ (i). The sheaf $\mathcal{H}^{p}_{Y}(F)$ is associated to the presheaf $X' \mapsto H^{p}_{Y'}(X', F')$; since we
have already remarked that (ii) is equivalent to the relation $H^{p}_{Y'}(X', F') = 0$ for $p < n$ and for every scheme
$X'$ étale over $X$, one indeed has $\mathcal{H}^{p}_{Y}(F) = 0$ for $p < n$.

(i) ⇔ (iii). The sheaves $\mathcal{H}^{p}_{Y}(F)$ are concentrated on $Y$; consequently it amounts to the same

<!-- original page 209 -->

to say that $\mathcal{H}^{p}_{Y}(F) = 0$ or that, for every geometric point $y$ of $Y$, the fiber
$(\mathcal{H}^{p}_{Y}(F))_{y}$ is null. Now, $i$ being quasi-compact, one deduces from (SGA 4 VIII 5.2) that one has
$(\mathcal{H}^{p}_{Y}(F))_{y} = H^{p}_{\bar{Y}}(\bar{X}, \bar{F})$. The equivalence of (i) and (iii) follows, taking
into account the analogue on $\bar{X}$ of the exact sequence (∗).

(ii bis) ⇒ (ii) in the case where $F$ is an abelian sheaf. The only thing that remains to show is that
$\mathcal{H}^{n-1}_{Y}(F) = 0$. Now, for $n > 2$, the sheaf $\mathcal{H}^{n-1}_{Y}(F)$ is associated to the presheaf
$X' \mapsto H^{n-2}(U', F') = H^{n-2}(X', F')$, hence is null. The case $n = 2$ follows from the fact that
$\mathcal{H}^{1}_{Y}(F)$ is the cokernel of the morphism $F \to i_{*} i^{*} F$.

**Definition 1.2.**

<!-- label: XIV.1.2 -->

The notations are those of 1.1. One says that $F$ is of $Y$-étale depth $\geqslant n$ and writes

$$
prof_{Y}(F) \geqslant n
$$

if $F$ satisfies the equivalent conditions (i) and (ii) of 1.1. If $F$ is a complex of abelian sheaves, one calls
$Y$-étale depth of $F$ the supremum of the $n$

<!-- original page 210 -->

for which $prof_{Y}(F) \geqslant n$; one will use the same notation if $F$ is a sheaf of sets, resp. of
not-necessarily-commutative groups (so that one then has $0 \leqslant prof_{Y}(F) \leqslant 2$, resp.
$0 \leqslant prof_{Y}(F) \leqslant 3$, when context does not allow confusion as to which of the three variants envisaged
here one is using).

If $L$ is a set of prime numbers, one says that the $Y$-étale depth for $L$ of $X$ is $\geqslant n$ and writes

$$
prof^{L}_{Y}(X) \geqslant n
$$

if, for every constant sheaf of the form $\mathbb{Z}/\ell \mathbb{Z}$ with $\ell \in L$, one has
$prof_{Y}(\mathbb{Z}/\ell \mathbb{Z}) \geqslant n$. One defines in the obvious way the $Y$-étale depth for $L$ of $X$.
If $L = P$, the set of all prime numbers, and if there is no risk of confusion with the notation of (EGA IV 5.7.1)
(relative to the case $F = O_{X}$), one omits $L$ in the notation; otherwise one writes $prof^{\acute{e}}_{Y}t(X)$.

Finally one says that $X$ is of $Y$-homotopical depth $\geqslant 3$ for $L$ and writes

$$
prof^{hopL}_{Y}(X) \geqslant 3
$$

if, for every constant finite sheaf of $L$-groups $F$ on $X$, one has $prof_{Y}(F) \geqslant 3$. If $L = P$, one omits
$L$ in the notation.

**Corollary 1.3.**

<!-- label: XIV.1.3 -->

Under the conditions of 1.1, if $prof_{Y}(F) \geqslant n$, then for every closed subset $Z$ of $Y$, one has

$$
prof_{Z}(F) \geqslant n.
$$

Let us, for example, carry out the reasoning in the case where $F$ is a complex of abelian sheaves bounded below. We use
1.1 3°) (ii). Let $V = X - Z$ and consider, for every integer $p$, the sequence of morphisms

```text
H^p(X, F) --f--> H^p(V, F) --g--> H^p(U, F).
```

By hypothesis $g$ and $f \circ g$ are bijective for $p < n - 1$ and injective for $p = n - 1$; the same therefore holds
for $f$. Since the reasoning is valid when one replaces $X$ by a scheme $X'$ étale over $X$, this proves 1.3.

**Corollary 1.4.**

<!-- label: XIV.1.4 -->

<!-- original page 211 -->

The notations are those of 1.1 2°). If $X'$ is a scheme over $X$, denote by $\Phi'$ the functor that associates to an
étale covering of $X'$ its restriction to $U'$, and by $\Phi'_{F'}$ the functor that associates to a torsor[^XIV-1-2]
under $F'$ its restriction to $U'$. Then the following conditions are equivalent:

(i) One has $prof_{Y}(F) \geqslant 1$ (resp. $prof_{Y}(F) \geqslant 2$, resp. $prof_{Y}(F) \geqslant 3$).

(ii) For every scheme $X'$ étale over $X$, the functor $\Phi'_{F'}$ is faithful (resp. fully faithful, resp. an
equivalence of categories).

In particular, in order that $prof_{Y}(X) \geqslant 1$ (resp. $prof_{Y}(X) \geqslant 2$, resp.
$prof^{hop}_{Y}(X) \geqslant 3$), it is necessary and sufficient that the functor $\Phi'$ be faithful (resp. fully
faithful, resp. an equivalence of categories).

This indeed follows from 1.1 2°) (ii), taking into account the interpretation of $H^{1}(X', F')$ as the set of classes
(mod isomorphism) of torsors under $F'$ (SGA 4 VII 2), and of étale coverings $Z$ of degree $n$ of a scheme as
associated to Galois principal coverings with group the symmetric group $S_{n}$, where to $Z$ is associated the covering
$Isom_{X}(Z_{0}, Z)$, where $Z_{0}$ is the trivial covering of $X$ of degree $n$.

**Corollary 1.5.**

<!-- label: XIV.1.5 -->

Under the conditions of 1.1 3°), suppose that $prof_{Y}(F) \geqslant n$; then one has

```text
H^n_Y(X, F) ≃ H⁰(X, ℋ^n_Y(F)).
```

The corollary follows from the spectral sequence

```text
E_2^{pq} = H^p(X, ℋ^q_Y(F)) ⟹ H^{p+q}_Y(X, F).
```

Indeed, one has by hypothesis $E^{pq}_{2} = 0$ for $q < n$, whence

```text
H^n_Y(X, F) = E_2^{0,n} = H⁰(X, ℋ^n_Y(F)).
```

**Remarks 1.6.**

<!-- label: XIV.1.6 -->

<!-- original page 212 -->

a) The notion of $Y$-depth, in the form of the equivalent conditions (i) and (ii) of 1.1, makes sense for any site. In
the particular case where $X$ is a locally noetherian scheme equipped with the Zariski topology, and $F$ a sheaf of
coherent `O_X`-modules, one finds the usual notion of $Y$-depth as the infimum of the depths at the points of $Y$ (III).

b) For $n \leqslant 2$, the notion of $Y$-étale depth of $X$ is independent of $L$. For $n = 1$, it simply means that
$U$ is dense in $X$. Indeed this condition is necessary in order that $prof_{Y}(F) \geqslant 1$, and it is also
sufficient since one may suppose $X$ reduced, the case in which the condition $U$ dense in $X$ is preserved by étale
base change (EGA IV 11.10.5 (ii) b)). If $U$ is retrocompact in $X$, the relation $prof_{Y}(X) \geqslant 1$ is also
equivalent to saying that $Y$ contains no maximal point of $X$ (EGA I 6.6.5). For $n = 2$ and $U$ retrocompact in $X$,
the condition $prof_{Y}(X) \geqslant 2$ is equivalent to the fact that, for every geometric point $y$ of $Y$, `Ū` is
connected non-empty, that is, "$Y$ does not disconnect $X$ locally for the étale topology".

c) If $X$ is of $Y$-depth $\geqslant n$ for $L$ and $U$ retrocompact in $X$, then for every locally constant abelian
sheaf of $L$-torsion $F$ on $X$, one has $prof_{Y}(F) \geqslant n$. Indeed, since the property $prof_{Y}(F) \geqslant n$
is local for the étale topology, one may suppose $F$ constant; then $F$ is a filtered direct limit of sheaves that are
finite sums of sheaves of the form $\mathbb{Z}/p^{m} \mathbb{Z}$, where $m$ is a positive integer and $p \in L$. Using
1.1 (iii)

<!-- original page 213 -->

and (SGA 4 VII 3.3), one sees that one may reduce to the case $F = \mathbb{Z}/p^{m} \mathbb{Z}$, then, by induction on
$m$, to the case $F = \mathbb{Z}/p\mathbb{Z}$ for which the assertion follows from the definition.

d) By 1.4, if $prof_{Y}(X) \geqslant 3$, the pair $(X, Y)$ is pure in the sense of X 3.1. In fact the pure pairs that
one encounters in practice (cf. X 3.4) satisfy the stronger condition of homotopical depth $\geqslant 3$, and this
notion may therefore advantageously be substituted for that of pure pair.

e) Let $F$ be a complex of abelian sheaves and $T(F)$ the complex obtained by applying to $F$ the translation functor
([3]); then one evidently has:

$$
prof_{Y}(T(F)) = prof_{Y}(F) - 1.
$$

f) Let us note that the recent works of Artin-Mazur ([1]) allow one to define the notion of homotopical depth
$\geqslant n$ for every integer $n$ (not only for $n \geqslant 3$).

g) Under the conditions of 1.1 3°), in order that $prof_{Y}(F) = \infty$, it is necessary and sufficient that
$F \xrightarrow{\sim} Ri_{*}(i^{*} F)$ in $D^{+}(X)$. Indeed, the $\mathcal{H}^{p}_{Y}(F)$ are the cohomology sheaves of
the cone (= mapping cylinder) of the canonical morphism $F \to Ri_{*} i^{*}(F)$.

**Definition 1.7.**

<!-- label: XIV.1.7 -->

Let $X$ be a scheme, $x$ a point of $X$, $\bar{x}$ a geometric point above $x$, and $\bar{X}$ the strict localization of
$X$ at $\bar{x}$. As before, $F$ denotes either a sheaf of sets on $X$, a sheaf of groups on $X$, or a complex of
abelian sheaves on $X$ bounded below; $\bar{F}$ its inverse image on $\bar{X}$, and $L$ a set of prime numbers. One says
that $F$ is of étale depth $\geqslant n$ at the point $x$ (resp. that the étale depth for $L$ of $X$ at $x$ is

<!-- original page 214 -->

$\geqslant n$, resp. that the homotopical depth for $L$ of $X$ at $x$ is $\geqslant 3$) and one writes
$prof_{x}(F) \geqslant n$ (resp. $prof^{L}_{x}(X) \geqslant n$, resp. $prof^{hopL}_{x}(X) \geqslant 3$) if one has
$prof_{\bar{x}}(\bar{F}) \geqslant n$ (resp. $prof^{L}_{\bar{x}}(\bar{X}) \geqslant n$, resp.
$prof^{hopL}_{\bar{x}}(\bar{X}) \geqslant 3$). One defines in the obvious way the integer $prof^{L}_{x}(X)$ and, if $F$
is a complex of abelian sheaves, the integer $prof_{x}(F)$. If $L$ is the set of all prime numbers, one omits $L$ in the
notation $prof^{L}_{x}(X)$, unless there is a risk of confusion with the notation of (EGA IV 5.7.1), in which case one
writes $prof^{\acute{e}}_{x}t(X)$.

One then has the following pointwise characterization of depth:

**Theorem 1.8.**

<!-- label: XIV.1.8 -->

Let $X$ be a scheme, $Y$ a closed part of $X$ such that the open set $U = X - Y$ is retrocompact in $X$. If $F$ is
either a sheaf of sets on $X$, a sheaf of groups on $X$, or a complex of abelian sheaves on $X$ bounded below, then one
has

```text
prof_Y(F) = inf_{y ∈ Y} prof_y(F).
```

**1.8.1.** Let us first show that, for every point $y$ of $Y$, one has the inequality
$prof_{y}(F) \geqslant prof_{Y}(F)$. Indeed, let `ȳ` be a geometric point above $y$, $\bar{X}$ the strict localization
of $X$ at `ȳ`, $\bar{F}$ and `Ȳ` the inverse images of $F$ and $Y$ on $\bar{X}$. By 1.7 and 1.3,

```text
prof_y(F) = prof_{ȳ}(F̄) ⩾ prof_{Ȳ}(F̄) ⩾ prof_Y(F),
```

the last inequality using the hypothesis "$U$ retrocompact", via the conditions (iii) in 1.1 and the transitivity in the
formation of strict localizations.

<!-- original page 215 -->

**1.8.2.** Conversely, suppose that, for every point $y$ of $Y$, one has $prof_{y}(F) \geqslant n$ ($n$ an integer) and
let us show that one then has $prof_{Y}(F) \geqslant n$.

Let us first recall the following well-known results (SGA 4 VIII):

**Lemma 1.8.2.1.**

<!-- label: XIV.1.8.2.1 -->

Let $X$ be a scheme, $F$ a sheaf of sets on $X$ (resp. $G \to F$ a monomorphism of sheaves of sets on $X$). Then, in
order that two sections $s$ and $s'$ of $F$ coincide (resp. that a section $s$ of $F$ come from a section of $G$), it is
necessary and sufficient that this hold locally. In particular, if $s$ and $s'$ are two sections of $F$, there exists a
largest open set $V$ of $X$ on which they coincide (resp. if $s$ is a section of $F$ over $X$, there exists a largest
open set $V$ of $X$ such that $s|V$ comes from a section of $G$ over $V$). This open set is also the set of points $x$
of $X$ such that, denoting by $\bar{x}$ a geometric point above $x$, the sections $s$ and $s'$ have the same image in
the fiber $F_{\bar{x}}$ (resp. that the image of $s$ in $F_{\bar{x}}$ comes from an element of $G_{\bar{x}}$).

Let us return to the proof of 1.8.

1°) Case where $F$ is a sheaf of sets. If $n = 1$, it suffices to show that the canonical morphism

```text
H⁰(X, F) → H⁰(U, F)
```

is injective, the result still applying when one replaces $X$ by a scheme étale over $X$. Let $s$ and $s'$ be two
sections of $F$ over $X$ having the same image in $H^{0}(U, F)$ and let $V$ be the largest open set over which they are
equal; one evidently has $V \supset U$. Suppose $V \neq X$ and let $y$ be a maximal point of $X - V$, `ȳ` a

<!-- original page 216 -->

geometric point above $y$, $\bar{X}$ the strict localization of $X$ at `ȳ`, and $\bar{V}$ and $\bar{F}$ the inverse
images of $V$ and $F$ on $\bar{X}$. By the choice of $y$, one has $\bar{X} - \bar{y} = \bar{V}$, and by hypothesis the
morphism

```text
H⁰(X̄, F̄) → H⁰(X̄ − ȳ, F̄) = H⁰(V̄, F̄)
```

is injective. It follows that $s$ and $s'$ coincide at the point $y$, which is absurd. If $n = 2$, it suffices to show,
taking the preceding into account, that the morphism

```text
H⁰(X, F) → H⁰(U, F) = H⁰(X, i_* i^* F)
```

is surjective (where $i$ is the canonical immersion of $U$ in $X$). Let $s$ be a section of $i_{*} i^{*} F$ over $X$ and
$V$ the largest open set over which it comes from a section of $F$. Suppose $V \neq X$ and let $y$ be a maximal point of
$X - V$; with the preceding notations, it follows from the hypothesis that the canonical morphism

```text
H⁰(X̄, F̄) → H⁰(X̄ − ȳ, F̄) = H⁰(V̄, F̄)
```

is bijective; consequently $s|V$ extends to the point $y$, which is absurd and completes the proof in case 1°).

2°) Case where $F$ is a sheaf of groups. Taking 1°) into account, the only thing that remains to show is that, in the
case $n = 3$, the morphism

```text
H¹(X, F) = H¹(X, i_* i^* F) → H¹(U, F)
```

<!-- original page 217 -->

is bijective. One already knows that it is injective by 1°) and 1.1 2°) (ii bis). For surjectivity, one uses the exact
sequence (SGA 4 XII 3.2)

```text
0 → H¹(X, i_* i^* F) → H¹(U, F) --d--> H⁰(X, R¹ i_* (i^* F)).
```

Let $s \in H^{1}(U, F)$ and $V \supset U$ the largest open set over which $d(s) = 0$; it is also the largest open set
such that $s$ comes from an element of $H^{1}(V, F)$. Suppose $V \neq X$ and let $y$ be a maximal point of $X - V$; if
$\bar{X}$ is the strict localization of $X$ at a geometric point `ȳ` above $y$, one has, with obvious notations, the
exact sequence

```text
0 → H¹(X̄, i_* (i^* F̄)) → H¹(Ū, F̄) --d--> H⁰(X̄, R¹ i_* (i^* F̄)).
```

Since $i : U \to X$ is quasi-compact, $R^{1} i_{*} (i^{*} \bar{F})$ is the inverse image of $R^{1} i_{*} (i^{*} F)$ by
the morphism $\bar{X} \to X$, whence $H^{0}(\bar{X}, R^{1} i_{*} (i^{*} \bar{F})) = (R^{1} i_{*} (i^{*} F))_{\bar{y}}$.
By hypothesis and given that $y \in Y$, the morphism

```text
H¹(X̄, F̄) → H¹(V̄, F̄)
```

is bijective. The image $\bar{s}$ of $s$ in $H^{1}(\bar{U}, \bar{F})$, which extends to $\bar{V}$ by definition of $V$,
therefore also extends to $\bar{X}$; it follows that $d(\bar{s}) = 0$, hence the image of $d(s)$ in the geometric fiber
$(R^{1} i_{*} (i^{*} F))_{\bar{y}}$ is null; but this contradicts the definition of $V$, whence case 2°).

3°) Case where $F$ is a complex of abelian sheaves bounded below. One reasons by induction on $n$. The conclusion is
satisfied for $n$ sufficiently small, since $F$ is bounded below. So suppose that $prof_{Y}(F) \geqslant n - 1$ and let
us show that $prof_{Y}(F) \geqslant n$, knowing that, for every point $y$ of $Y$, one has $prof_{y}(F) \geqslant n$. It
suffices to see that the canonical morphism

```text
(∗)    H^{n−2}(X, F) → H^{n−2}(U, F)
```

is surjective and that

```text
(∗∗)   H^{n−1}(X, F) → H^{n−1}(U, F)
```

is injective (the result applying when one replaces $X$ by a scheme étale over $X$).

<!-- original page 218 -->

a) Surjectivity of (∗). The proof is analogous to that of 2°). Taking 1.5 and (SGA 4 V 4.5) into account, one has the
exact sequence

```text
H^{n−2}(X, F) → H^{n−2}(U, F) --d--> H^{n−1}_Y(X, F) = H⁰(X, ℋ^{n−1}_Y(F)).
```

Let $s \in H^{n-2}(U, F)$ and $V \supset U$ the largest open set over which $d(s) = 0$, which is also the largest open
set such that $s$ extends to $H^{n-2}(V, F)$. Suppose $V \neq X$ and let $y$ be a maximal point of $X - V$ and $\bar{X}$
the strict localization of $X$ at a geometric point `ȳ` above $y$. Since $i : U \to X$ is quasi-compact, the formation
of $\mathcal{H}^{n-1}_{Y}(F)$ commutes with the base change $\bar{X} \to X$ and one therefore has (with obvious
notations) the exact sequence

```text
H^{n−2}(X̄, F̄) → H^{n−2}(Ū, F̄) --d--> H^{n−1}_Ȳ(X̄, F̄) = (ℋ^{n−1}_Y(F))_ȳ,
```

the last equality resulting from the retrocompactness hypothesis on $U$.

Now one has by hypothesis the isomorphism

```text
H^{n−2}(X̄, F̄) ⥲ H^{n−2}(X̄ − ȳ, F̄) = H^{n−2}(V̄, F̄);
```

consequently the image $\bar{s}$ of $s$ in $H^{n-2}(\bar{U}, \bar{F})$, which extends (by definition of $V$) to
$H^{n-2}(\bar{V}, \bar{F})$, also extends to $H^{n-2}(\bar{X}, \bar{F})$; but this shows that $d(\bar{s}) = 0$, that is,
that $d(s)$ is null at $y$, which is absurd.

b) Injectivity of (∗∗). Using the surjectivity of (∗), one obtains the exact sequence

```text
0 → H⁰(X, ℋ^{n−1}_Y(F)) → H^{n−1}(X, F) → H^{n−1}(U, F)
```

<!-- original page 219 -->

and one must show that every element $s \in H^{0}(X, \mathcal{H}^{n-1}_{Y}(F))$ is null. Let $V$ be the largest open set
over which $s = 0$. Suppose $V \neq X$ and let $y$ be a maximal point of $X - V$, $\bar{X}$ a strict localization of $X$
at a geometric point `ȳ` above $y$. By the inductive hypothesis and by 1.8.1, one has the relation
$prof_{\bar{Y}}(\bar{F}) \geqslant prof_{Y}(F) \geqslant n - 1$, whence the fact that the map $e$ in the diagram below
is injective:

```text
H⁰(X̄, ℋ^{n−1}_Ȳ(F̄)) = (ℋ^{n−1}_Y(F))_ȳ --e--> H^{n−1}(X̄, F̄) --f--> H^{n−1}(V̄, F̄).
```

The same holds for $f$ by virtue of the hypothesis; the left equality follows from the retrocompactness hypothesis on
$U$. Let $\bar{s}$ be the image of $s$ in $(\mathcal{H}^{n-1}_{Y}(F))_{\bar{y}}$; since $s$ vanishes over $V$, one has
$f \cdot e(\bar{s}) = 0$, whence $\bar{s} = 0$, which contradicts the choice of $y$ and completes the proof.

**Remark 1.9.**

<!-- label: XIV.1.9 -->

A result analogous to 1.8 is doubtless valid in the case where one replaces the étale topos of a scheme $X$ by a "topos
locally of finite type", that is, definable by a site locally of finite type (SGA 4 VI 1.1). To see this, one must use a
result of P. Deligne (SGA 4 VI.9), asserting that there are "sufficiently many fiber functors" in such a topos.

We are going to deduce from 1.8 important cases where one can determine the étale depth.

**Theorem 1.10** (Cohomological semi-purity theorem)[^N.D.E-XIV-1].

<!-- label: XIV.1.10 -->

Denote by $X$ either a smooth scheme over a field $k$, or a regular excellent scheme (EGA IV 7.8.2) of characteristic
zero (N.B. if one admits resolution of singularities in the sense of (SGA 4 XIX), it suffices to suppose, more
generally, that $X$ is a regular excellent scheme of equal characteristic). Let $Y$ be a closed part of $X$ and $L$ the
set

<!-- original page 220 -->

of prime numbers distinct from the characteristic of $X$. Then one has

$$
prof^{L}_{Y}(X) = 2 codim(Y, X).
$$

*Proof.* It follows from 1.8 that one has

```text
prof_Y^L(X) = inf_{y ∈ Y} prof_y^L(X).
```

Since on the other hand `codim(Y, X) = inf_{y ∈ Y} dim O_{X,y}`, one is reduced to showing that

$$
prof^{L}_{y}(X) = 2 \dim O_{X,y},
$$

which follows from (SGA 4 XVI 3.7 and XIX 3.2).

**Theorem 1.11** (Homotopical purity theorem)[^N.D.E-XIV-2].

<!-- label: XIV.1.11 -->

If $X$ is a locally noetherian scheme that is regular (resp. whose local rings are complete intersections), $Y$ a closed
part of $X$ such that $codim(Y, X) \geqslant 2$ (resp. $codim(Y, X) \geqslant 3$), then one has

$$
prof^{hop}_{Y}(X) \geqslant 3.
$$

It indeed follows from 1.8 that one has `prof_Y^{hop}(X) = inf_{y ∈ Y} prof_y^{hop}(X)`. Now the strictly local rings of
$X$ at the various points of $Y$ are regular rings of dimension $\geqslant 2$ (resp. complete intersections of dimension
$\geqslant 3$). It then follows from the purity theorem X 3.4 that $prof^{hop}_{y}(X) \geqslant 3$, which proves the
theorem.

**Example 1.12.**

<!-- label: XIV.1.12 -->

Let $X$ be a locally noetherian scheme, $Y$ a closed part of $X$, and $n = 1$ or `2`. Then, if
$prof_{Y}(O_{X}) \geqslant n$ ($prof_{Y}(O_{X})$ denoting the $Y$-depth in the sense of coherent sheaves, cf. 1.6 a)),
one also has $prof_{Y}(X) \geqslant n$; this is evident for $n = 1$ and, for $n = 2$, it is none other than Hartshorne's
theorem

<!-- original page 221 -->

(III 1). On the other hand, the analogous assertion is false for $n \geqslant 3$. Take for example an

<!-- original page 222 -->

affine space of dimension $\geqslant 3$ over a field of characteristic $\neq 2$ and let $\mathbb{Z}/2\mathbb{Z}$ act by
symmetry with respect to the origin. Let $X$ be the quotient and $Y = {x}$ the image of the origin in $X$. Then
$O_{X,x}$ is a Cohen-Macaulay ring, hence one has $prof_{x}(O_{X}) \geqslant 3$; but the affine space minus the origin
is an étale covering of $X - {x}$ that does not extend to an étale covering of $X$; hence one has by 1.4
$prof_{Y}(X) = 2$.

The following theorem is the analogue of (EGA IV 6.3.1):

**Theorem 1.13.**

<!-- label: XIV.1.13 -->

Let $f : X \to S$ be a morphism of schemes, $Y$ a closed part of $X$, $Z$ a closed part of $S$ such that
$f(Y) \subset Z$. Suppose that the local rings of $X$ at the various points of $Y$ are noetherian and that the open sets
$X - Y$ and $S - Z$ are retrocompact in $X$ and $S$ respectively. Let `p, q, r` be integers such that $p \geqslant -r$,
$q \geqslant 0$, $L$ a set of prime numbers and $F$ a complex of abelian sheaves of $L$-torsion on $S$ such that the
cohomology sheaves $H^{i}(F)$ are null for $i < -r$. Suppose that

a) The morphism $f$ is locally $(p + q + r - 2)$-acyclic for $L$ (SGA 4 XV 1.11).

b) One has

$$
prof_{Z}(F) \geqslant p.
$$

c) For every point $s$ of $Z$, one has

$$
prof^{L}_{Y_{s}}(X_{s}) \geqslant q.
$$

Then one has

```text
prof_Y(f^* F) ⩾ p + q.
```

We shall need the following lemma:

**Lemma 1.13.1.**

<!-- label: XIV.1.13.1 -->

Let $L$ be a set of prime numbers, $n$ and $r$ integers, $f : X \to S$ a morphism locally $n$-acyclic for $L$. Let $F$
be a complex of abelian sheaves with cohomology sheaves of $L$-torsion such that $H^{i}(F) = 0$ for $i < -r$, $Z$ a
closed part of $S$ such that $S - Z$ is retrocompact in $S$, and $T = f^{-1}(Z)$. Then the canonical morphism

```text
f^* (ℋ^i_Z(F)) → ℋ^i_T(f^* F)
```

is bijective for $i < n - r + 2$ and injective for $i = n - r + 2$.

Set $U = S - Z$ and $V = X - T$, so that one has the cartesian square

```text
V --g--> U
|        |
k        j
|        |
v        v
X --f--> S
```

Consider the commutative diagram below whose rows are exact

```text
→ f^*(ℋ^i_Z(F))    → f^*(H^i(F))    → f^*(H^i(R j_*(j^* F)))    →
                       ≀
→ ℋ^i_T(f^* F)     → H^i(f^* F)     → H^i(R k_*(k^* f^* F))     → ;
```

it follows that one is reduced to showing that the morphism

```text
f^*(H^i(R j_*(j^* F))) → H^i(R k_*(k^* f^* F))
```

<!-- original page 223 -->

is bijective for $i < n - r + 1$ and injective for $i = n - r + 1$. Now such a morphism comes from the following
morphism between hypercohomology spectral sequences

```text
f^* E_2^{p,q} = f^* (R^p j_*(H^q(j^* F)))     ⟹ f^*(H^*(R j_*(j^* F)))
       ↓                                         ↓
E′_2^{p,q} = R^p k_*(H^q(k^* f^* F))           ⟹ H^*(R k_*(k^* f^* F)).
```

Since $j$ is quasi-compact, it follows from (SGA 4 XV 1.10) that the morphism $f^{*}(E^{p,q}_{2}) \to E'^{p,q}_{2}$ is
bijective for $p \leqslant n$ and injective for $p = n + 1$; in particular it is bijective for $p + q \leqslant n - r$
and injective for $p + q = n - r + 1$. The conclusion follows immediately.

Let us return to the proof of 1.13. Let $T = f^{-1}(Z)$. By 1.13.1 and condition a), the canonical morphism
$f^{*}(\mathcal{H}^{i}_{Z}(F)) \to \mathcal{H}^{i}_{T}(f^{*} F)$ is an isomorphism for $i \leqslant p + q$. It therefore
follows from b) that $\mathcal{H}^{i}_{T}(f^{*} F) = 0$ for $i < p$ and, for $i < p + q$, $\mathcal{H}^{i}_{T}(f^{*} F)$
restricted to $T$ is the inverse image of a sheaf $G_{i}$ on $Z$. Let

$$
f_{T} : T \to Z
$$

be the restriction of $f$ to $T$. It then follows from c) and from the corollary that follows that
$\mathcal{H}^{j}_{Y}(f^{*}_{T}(G_{i})) = 0$ for $j < q$. One concludes that

```text
ℋ^j_Y(ℋ^i_T(f^* F)) = 0 for i + j < p + q,
```

since the inequality $i + j < p + q$ entails either $i < p$ and then $\mathcal{H}^{i}_{T}(f^{*} F) = 0$, or $j < q$ and
then $\mathcal{H}^{j}_{Y}(\mathcal{H}^{i}_{T}(f^{*} F)) = 0$. Given that one has, with the notations of 1.0,
$\Gamma_{Y} = \Gamma_{Y} \cdot \Gamma_{T}$, one has the spectral sequence

```text
(1.13.2)    E_2^{i,j} = ℋ^j_Y(ℋ^i_T(f^* F)) ⟹ ℋ^{i+j}_Y(f^* F);
```

<!-- label: eq:XIV.1.13.2 -->

since $E^{i,j}_{2} = 0$ for $i + j < p + q$, one sees that $\mathcal{H}^{k}_{Y}(f^{*} F) = 0$ for $k < p + q$.

<!-- original page 224 -->

The theorem will therefore be proved if one proves the following corollary (which is the particular case of 1.13
obtained by taking $Z = S$, $r = p = 0$ and $F$ reduced to degree `0`).

**Corollary 1.14.**

<!-- label: XIV.1.14 -->

Let $f : X \to S$ be a morphism, $Y$ a closed part such that the complementary open set $X - Y$ is retrocompact in $X$
and that the local rings of $X$ at the various points of $Y$ are noetherian. Let $L$ be a set of prime numbers, $q$ an
integer, and $F$ an abelian sheaf of $L$-torsion on $S$. Suppose

that $f$ is locally $(q - 2)$-acyclic for $L$ and that, for every point $s$ of $S$, one has
$prof^{L}_{Y_{s}}(X_{s}) \geqslant q$. Then one has $prof_{Y}(f^{*} F) \geqslant q$.

1°) Reduction to the case where $X$ and $S$ are strictly local schemes, $f$ a local morphism, and $Y$ reduced to a
closed point of $X$.

By 1.8, to establish 1.14, one must show that one has for every point $y$ of $Y$:

$$
prof_{y}(f^{*} F) \geqslant q.
$$

Let $s = f(y)$, $\bar{s}$ a geometric point above $s$, `ȳ` a geometric point above $y$ and over $\bar{s}$, $\bar{X}$ and
$\bar{S}$ the strict localizations of $X$ and $S$ at `ȳ` and $\bar{s}$ respectively, $\bar{f} : \bar{X} \to \bar{S}$ the
canonical morphism, and $\bar{F}$ the inverse image of $F$ on $\bar{S}$. Since one has the relation
$prof_{y}(f^{*} F) = prof_{\bar{y}}(\bar{f}^{*} \bar{F})$, it suffices to show that the hypotheses of 1.14 are preserved
when one replaces $f$ (resp. $Y$, resp. $F$) by $\bar{f}$ (resp. ${\bar{y}}$, resp. $\bar{F}$). The retrocompactness
condition

<!-- original page 225 -->

follows from the noetherian hypothesis on $O_{X,x}$, which implies that $\bar{X}$ is noetherian. By (SGA 4 XV 1.10 (i)),
$\bar{f}$ is still locally $(q - 2)$-acyclic for $L$. Moreover the fiber $(\bar{X})_{\bar{s}}$ of $\bar{X}$ over
$\bar{s}$ is identified with the strict localization of $X_{s}$ at `ȳ`, hence satisfies the relation
$prof_{\bar{y}}((\bar{X})_{\bar{s}}) \geqslant q$. Since an analogous relation is trivially verified for the fibers of
the $\bar{S}$-scheme $\bar{X}$ other than the closed fiber, this completes the reduction.

2°) Case where $X$ and $S$ are strictly local, $f$ a local homomorphism, and $Y$ reduced to the closed point of $X$. Let

```text
g : U = X − {y} → S
```

be the structural morphism of $U$. One must show that the canonical morphism

```text
u_i : H^i(X, f^* F) → H^i(U, f^* F)
```

is bijective for $i \leqslant q - 2$ and injective for $i = q - 1$. Consider the commutative diagram

```text
H^i(X, f^* F) --u_i--> H^i(U, f^* F)
       ↖ v_i           ↗ w_i
          H^i(S, F)
```

The morphism $v_{i}$ is evidently bijective for every $i$. On the other hand $g$ is locally $(q - 2)$-acyclic for $L$;
moreover its fibers are $(q - 2)$-acyclic for $L$, as follows from the fact that $prof_{y}(X_{s}) \geqslant q$ and that
the fibers of $f$ are $(q - 2)$-acyclic for $L$; since $g$ is quasi-compact (as $X$ is noetherian), it follows from (SGA
4 XV 1.16) that $g$ is $(q - 2)$-acyclic for $L$. Consequently $w_{i}$, hence also $u_{i}$, is bijective

<!-- original page 226 -->

for $i \leqslant q - 2$ and injective for $i = q - 1$, which completes the proof of 1.14.

**Corollary 1.15.**

<!-- label: XIV.1.15 -->

Let $f : X \to S$ be a morphism of schemes, $L$ a set of prime numbers, $m$ and $r$ integers, and $F$ a complex of
abelian sheaves of $L$-torsion on $S$ such that $H^{i}(F) = 0$ for $i < -r$. Let $x$ be a point of $X$, $s = f(x)$

<!-- original page 227 -->

and suppose that the local ring $O_{X,x}$ is noetherian. Then, if $f$ is locally $m$-acyclic for $L$, one has the
relation

```text
(∗)    prof_x(f^* F) ⩾ inf(prof_s(F) + prof_x^L(X_s), n)   where n = m − r + 2.
```

In particular, if $n \geqslant prof_{s}(F) + prof^{L}_{x}(X_{s})$, for example if $f$ is locally acyclic for $L$, one
has

```text
(∗∗)   prof_x(f^* F) ⩾ prof_s(F) + prof_x^L(X_s).
```

If $L$ is reduced to one element $\ell$ and if one has $n \geqslant prof_{s}(F) + prof^{L}_{x}(X_{s})$, the preceding
inequality is an equality.

One reduces to the case where $s$ and $x$ are closed points by taking the strict localizations of $S$ and $x$ at
geometric points $\bar{s}$ above $s$ and $\bar{x}$ above $x$ and $\bar{s}$. If one has the inequality
$n \geqslant prof_{s}(F) + prof^{L}_{x}(X_{s})$, then (∗) is obtained from 1.13 by taking $p = prof_{s}(F)$ and
$q = prof^{L}_{x}(X_{s})$ (the hypothesis that $S - {s}$ is retrocompact in $S$ follows from the fact that $X - X_{s}$
is retrocompact in $X$ and that $f$ is surjective since it is $(-1)$-acyclic (except perhaps if the conclusion of 1.15
is empty)). If $n < prof_{s}(F) + prof^{L}_{x}(X_{s})$, the inequality (∗) is again obtained from 1.13 by taking for
example $p = prof_{s}(F)$ and $q = n - p$. It remains to prove the last assertion. Let $p = prof_{s}(F)$ and
$q = prof_{x}(X_{s})$; it follows from (1.13.2) that one has

$$
H^{p+q}_{x}(f^{*}(F)) \simeq H^{q}_{x}(f^{*}(H^{p}_{s}(F))).
$$

Since $prof_{s}(F) = p$, the sheaf $H^{p}_{s}(F)$ is a sheaf of $\ell$-torsion, constant on $s$, non-zero. Consequently
the sheaf $G = f^{*}(H^{p}_{s}(F))$ is a sheaf of $\ell$-torsion, constant on $X_{s}$, non-zero, hence contains a
subsheaf isomorphic to $\mathbb{Z}/\ell \mathbb{Z}$; since $H^{q}_{x}(\mathbb{Z}/\ell \mathbb{Z})$ is non-zero, one
indeed has $H^{q}_{x}(G) \neq 0$.

**Corollary 1.16.**

<!-- label: XIV.1.16 -->

Let $f : X \to S$ be a regular morphism of excellent schemes (EGA IV 7.8.2) of characteristic zero, $\ell$ a prime
number, and $F$ a complex of sheaves of $\ell$-torsion on $S$. Let $x \in X$, $s = f(x)$; then one has

```text
prof_x(f^* F) = prof_s(F) + 2 dim(O_{X_s,x}).
```

Indeed $f$ is locally acyclic (SGA 4 XIX 4.1). It then follows from 1.15 that one has

```text
prof_x(f^* F) = prof_s(F) + prof_x(X_s).
```

Now one has by 1.10

$$
prof_{x}(X_{s}) = 2 \dim O_{X_{s},x},
$$

whence the result.

**Remark 1.17.**

<!-- label: XIV.1.17 -->

It follows from 1.15 that 1.13 remains valid when one replaces b) and c) by the conditions:

<!-- original page 228 -->

b′) For every point $s \in f(Y)$, one has $prof_{s}(F) \geqslant p$.

c′) For every point $x \in Y$, if $s = f(x)$, one has $prof^{L}_{x}(X_{s}) \geqslant q$.

In the case of a sheaf of sets or of groups, one has the following theorem analogous to 1.13.

**Theorem 1.18.**

<!-- label: XIV.1.18 -->

Let $f : X \to S$ be a morphism of schemes, $Y$ a closed part of $X$ such that $X - Y$ is retrocompact in $X$ and that,
for every point $x$ of $Y$, the local ring $O_{X,x}$ is noetherian.

1°) Let $F$ be a sheaf of sets on $S$ and $n$ an integer equal to `1` or `2`. Suppose that $f$ is locally
$(n - 2)$-acyclic and that, for every point $s$ of $f(Y)$, one has:

$$
prof_{Y_{s}}(X_{s}) + prof_{s}(F) \geqslant n.
$$

Then one has:

$$
prof_{Y}(f^{*} F) \geqslant n.
$$

2°) Let $L$ be a set of prime numbers and $F$ a sheaf of ind-$L$-groups. Suppose that $f$ is locally `1`-aspherical for
$L$ (SGA 4 XV 1.11) and that, for every point $s$ of $f(Y)$, one has:

```text
prof_{Y_s}^{hopL}(X_s) + prof_s(F) ⩾ 3.
```

Then one has:

$$
prof_{Y}(f^{*} F) \geqslant 3.
$$

<!-- original page 229 -->

*Proof.* One reduces, as in 1.14 and 1.15, to the case where $X$ and $S$ are strictly local schemes, $f$ a local
homomorphism, and $Y$ the closed point $x$ of $X$. Let $s = f(x)$ be the closed point of $S$; one has the commutative
diagram:

```text
X − X_s --i--> X − {x} --j--> X
        \         |          /
         \        g         /
          \       |        / f
           \      v       /
            \   S − {s}  /
             \    |k    /
              \   v    /
                  S
```

1°) a) Case $n = 1$.

If $prof_{s}(F) \geqslant 1$, then the morphism $F \to k_{*} k^{*} F$ is injective, hence the morphism
$f^{*} F \to f^{*}(k_{*} k^{*} F)$ is also injective. On the other hand it follows from the fact that $f$ is locally
$(-1)$-acyclic that the morphism $f^{*}(k_{*} k^{*} F) \to (j \cdot i)_{*}(f^{*} F|_{X - X_{s}})$ is injective. Finally,
the composite morphism $f^{*} F \to (j \cdot i)_{*}(f^{*} F|_{X - X_{s}})$ is injective, which shows that one has
$prof_{X_{s}}(f^{*} F) \geqslant 1$, hence also $prof_{x}(f^{*} F) \geqslant 1$.

If $prof_{x}(X_{s}) \geqslant 1$, one considers the commutative diagram

```text
                          v
H⁰(X, f^* F)          ----→    H⁰(X − {x}, f^* F)
    | ≀                            ↑
    v                              |
H⁰(X_s, f^* F)        --v′--→ H⁰(X_s − {x}, f^* F);
(∗)
```

By hypothesis, $v'$ is injective, hence the same holds for $v$.

<!-- original page 230 -->

b) Case $n = 2$. One considers the commutative diagram

```text
            u
H⁰(S, F)  ----→   H⁰(S − {s}, F)
   m ≀                  n ≀
   |                      |
   v                      v
            v                     w
H⁰(X, f^* F) --→ H⁰(X − {x}, f^* F) --→ H⁰(X − X_s, f^* F);
(∗∗)
```

one must show that $v$ is bijective. The morphism $m$ is evidently bijective, and, since $f$ is `0`-acyclic, $n$ is also
bijective.

If $prof_{s}(F) \geqslant 2$, $u$ is bijective. As one has seen in a), the single hypothesis $prof_{s}(F) \geqslant 1$
entails the relation $prof_{X_{s}}(f^{*} F) \geqslant 1$; consequently $v$ and $w$ are injective; it then follows from
(∗∗) that $v$ is bijective.

If $prof_{x}(X_{s}) \geqslant 2$, then $g$ is `0`-acyclic (since it is locally `0`-acyclic and its fibers are
`0`-acyclic). It follows that $v \cdot m$ is bijective, hence $v$ is bijective.

If $prof_{s}(F) \geqslant 1$ and $prof_{x}(X_{s}) \geqslant 1$, then one already knows that $v$ and $w$ are injective.
Let $z$ be a maximal point of $X_{s} - {x}$ (such a point exists by the hypothesis $prof_{x}(X_{s}) \geqslant 1$),
$\bar{Z}$ the strict localization of $X$ at a geometric point above $z$, and $f^{*} \bar{F}$ the inverse image of
$f^{*} F$ on $\bar{Z}$. Consider the commutative diagram

```text
H⁰(S, F) ----→ H⁰(S − {s}, F)
   |m ≀                |n ≀
   v                    v
H⁰(X, f^* F) --v--→ H⁰(X − {x}, f^* F) --w--→ H⁰(X − X_s, f^* F)
   |m′ ≀                |r                       |
   v                    v                        v
H⁰(Z̄, f^* F̄) ----→  H⁰(Z̄ − {z̄}, f^* F̄)
```

The morphism $m' \cdot m$ is evidently bijective, and it follows from the fact that $f$ is locally `0`-acyclic that
$n' \cdot n$ is bijective; consequently $m'$ and $n'$ are also bijective. Since $w$ is injective, $r$ is also injective,
and consequently $v$ is bijective.

2°) Taking b) into account, one already knows that $prof_{x}(f^{*} F) \geqslant 2$.

If $prof_{s}(F) \geqslant 3$, then $R^{1} k_{*}(k^{*} F) = 1$[^N.D.E-XIV-3]. Since $f$ is locally `1`-aspherical,

<!-- original page 231 -->

one has $R^{1}(j \cdot i)_{*}(f^{*} F|_{X - X_{s}}) = f^{*}(R^{1} k_{*}(k^{*} F)) = 1$. One therefore has
$prof_{X_{s}}(f^{*} F) \geqslant 3$ and consequently $prof_{x}(f^{*} F) \geqslant 3$.

If $prof_{x}(X_{s}) \geqslant 3$, then $g$ is `1`-aspherical (since $g$ is locally `1`-aspherical and its fibers are
`1`-aspherical). One therefore has $H^{1}(X - {x}, f^{*} F) = H^{1}(S, F) = 1$ and consequently
$prof_{x}(f^{*} F) \geqslant 3$.

If $prof_{s}(F) \geqslant 2$ and $prof_{x}(X_{s}) \geqslant 1$, one uses the exact sequence (SGA 4 XII 3.2):

```text
1 → R¹ j_*(i_*(f^* F|_{X − X_s})) → R¹(j · i)_*(f^* F|_{X − X_s}) → j_*(R¹ i_*(f^* F|_{X − X_s})).
```

Since $f$ and $g$ are locally `1`-aspherical, one has

```text
R¹(j · i)_*(f^* F|_{X − X_s}) ≃ f^*(R¹ k_*(k^* F))
R¹ i_*(f^* F|_{X − X_s}) ≃ g^*(R¹ k_*(k^* F));
```

the preceding exact sequence then writes in the form

```text
(∗∗∗)  1 → R¹ j_*(i_*(f^* F|_{X − X_s})) → f^*(R¹ k_*(k^* F)) --a--> j_*(j^*(f^*(R¹ k_*(k^* F)))).
```

The hypothesis $prof_{s}(F) \geqslant 2$ shows that the morphism $F \to k_{*} k^{*} F$ is bijective; applying $g^{*}$,
one finds, taking into account the fact that $g$ is locally `0`-acyclic,
$f^{*} F|_{X - {x}} = i_{*}(f^{*} F|_{X - X_{s}})$. The hypothesis $prof_{x}(X_{s}) \geqslant 1$ shows that the morphism
$a$ is injective (note that $f^{*}(R^{1} k_{*}(k^{*} F))$ is a sheaf equal to `1` outside $X_{s}$ and constant on
$X_{s}$). It then follows from (∗∗∗) that one has $R^{1} j_{*}(f^{*} F|_{X - {x}}) = 1$, hence

<!-- original page 232 -->

$prof_{x}(f^{*} F) \geqslant 3$.

If $prof_{s}(F) \geqslant 1$ and $prof_{x}(f^{*} F) \geqslant 2$, one considers the sheaf of homogeneous spaces $G$
defined by the exact sequence

```text
1 → F → k_* k^* F → G → 1.
```

Applying to this exact sequence the exact functor $g^{*}$ and using (SGA 4 XII 3.1), one obtains the following
commutative diagram whose rows are exact:

```text
f^*(k_* k^* F)       →     f^* G                   → 1
        |                    |b
        v                    v u
j_*(g^*(k_* k^* F)) --u-->  j_*(g^* G)      → R¹ j_*(g^* F) → R¹ j_*(g^*(k_* k^* F)).
```

Since $prof_{x}(X_{s}) \geqslant 2$, the morphism $b$ is bijective hence $u$ is surjective, and one thus has a map with
kernel reduced to the neutral element:

```text
1 → R¹ j_*(g^* F) → R¹ j_*(g^*(k_* k^* F)) = R.
```

Since $g^{*}(k_{*} k^{*} F) \simeq i_{*}(f^{*} F|_{X - X_{s}})$ (because $g$ is locally `0`-acyclic), $R$ is identified
with the first term of the exact sequence (∗∗∗); now one saw in the preceding case that $R = 1$ as soon as one has
$prof_{x}(X_{s}) \geqslant 1$, which shows that $prof_{x}(f^{*} F) \geqslant 3$ and completes the proof of 1.18.

The following corollaries are generalizations of (SGA 4 XVI 3.2 and 3.3).

**Corollary 1.19.**

<!-- label: XIV.1.19 -->

Let $f : X \to S$ be a flat morphism with separable fibers of locally noetherian schemes,

<!-- original page 233 -->

and $Y$ a closed part of $X$. Suppose that for every point $s \in f(Y)$, the fiber $Y_{s}$ is rare[^N.D.E-XIV-4] in
$X_{s}$ and that one of the two following conditions is verified:

a) the closure of $f(Y)$ is rare in $S$.

b) $X_{s}$ is geometrically unibranch at the points of $Y_{s}$.

Then one has

$$
prof_{Y}(X) \geqslant 2.
$$

It indeed follows from the hypothesis on $f$ that $f$ is locally `0`-acyclic (SGA 4 XV 4.1). One then applies 1.13. The
hypothesis $Y_{s}$ rare in $X_{s}$ (resp. $f(Y)$ rare in $S$) is by 1.6 b) equivalent to the relation
$prof_{Y_{s}}(X_{s}) \geqslant 1$ (resp. $prof_{f(Y)}(S) \geqslant 1$). The hypothesis $X_{s}$ geometrically unibranch
at each point of $Y_{s}$ is equivalent to saying that the strict localization of $X_{s}$ at a geometric point of $Y_{s}$
is irreducible; knowing that $Y_{s}$ is rare in $X_{s}$, this evidently entails $prof_{Y_{s}}(X_{s}) \geqslant 2$, by
1.8. In either case 1.13 indeed gives $prof_{Y}(X) \geqslant 2$.

**Corollary 1.20.**

<!-- label: XIV.1.20 -->

Let $f : X \to S$ be a regular morphism (EGA IV 6.8.1) of locally noetherian schemes, $Y$ a closed part of $X$. Suppose
that, for every point $s \in f(Y)$, one of the following conditions is realized:

a) One has $codim(Y_{s}, X_{s}) \geqslant 2$.

b) One has $codim(Y_{s}, X_{s}) \geqslant 1$ and $prof_{s}(S) \geqslant 1$.

c) One has $prof^{hop}_{s}(S) \geqslant 3$.

Then one has

<!-- original page 234 -->

$$
prof^{hop}_{Y}(X) \geqslant 3.
$$

This indeed follows from 1.18, given that hypothesis a) implies $prof^{hop}_{Y_{s}}(X_{s}) \geqslant 3$ (cf. 1.11), and
that the condition $codim(Y_{s}, X_{s}) \geqslant 1$ evidently implies $prof_{Y}(X) \geqslant 2$.

## 2. Technical lemmas

**2.1.** Let $S$ be a locally noetherian scheme, $f : X \to S$ a morphism locally of finite type, $t$ a point of $S$. If
$x \in X$ is such that $s = f(x) \in \operatorname{Spec} O_{S,t}$, one sets

```text
δ_t(x) = deg.tr. k(x)/k(s) + dim({s}),
```

where ${s}$ denotes the closure of $s$ in $\operatorname{Spec} O_{S,t}$, $k(x)$ and $k(s)$ the residue fields of $x$ and
$s$ respectively. If $S$ is a local ring with closed point $t$, one writes also $\delta(x)$ instead of $\delta_{t}(x)$
(cf. SGA 4 XIV 2.2).

**Lemma 2.1.1.**

<!-- label: XIV.2.1.1 -->

Let

```text
X′ --h--> X
|         |
f′        f
|         |
v         v
S′ --g--> S
```

be a cartesian square, where $S$ and $S'$ are noetherian local rings with closed points $t$ and $t'$ respectively, $g$ a
faithfully flat morphism such that $g^{-1}(t) = t'$, $f$ a morphism locally

<!-- original page 235 -->

of finite type. Let $x' \in X'$, $x = h(x')$, $s = f(x)$, $s' = f'(x')$; then one has

$$
\delta(x') \leqslant \delta(x).
$$

Moreover the preceding inequality is an equality if and only if one has:

```text
deg.tr. k(x)/k(s) = deg.tr. k(x′)/k(s′)   and   dim({s}) = dim({s′}).
```

In particular, given $x \in X$, one can find $x'$ such that $\delta(x) = \delta(x')$.

One has indeed (EGA IV 6.11)

$$
\dim({s}) = \dim g^{-1}({s}).
$$

It follows that, for every point $s'$ of $g^{-1}(s)$, one has the relation $\dim({s'}) \leqslant \dim({s})$, and that,
$s$ being given, one can find $s' \in g^{-1}(s)$ such that one has the equality. Denote then by $Z$ the schematic
closure of $x$ in the fiber $X_{s}$ of $X$ at $s$, and let
$Z' = Z \times_{\operatorname{Spec} k(s)} \operatorname{Spec} k(s')$. Then $Z'$ is equidimensional of dimension
$deg.tr. k(x)/k(s)$; one therefore has, for every point $x' \in Z'_{x}$,

```text
deg.tr. k(x′)/k(s′) ⩽ deg.tr. k(x)/k(s),  with equality
```

when $x'$ is a maximal point of $Z'_{x}$. Whence immediately the announced conclusion.

**2.2.** Let $f : X \to S$ be a morphism locally of finite type and $T$ a closed part of $S$. Let $x \in X$, $s = f(x)$;
we shall set

```text
δ_T(x) = deg.tr. k(x)/k(s) + codim({s} ∩ T, {s}) = inf_{t ∈ T ∩ {s}} δ_t(x).
```

<!-- original page 236 -->

**Lemma 2.2.1.**

<!-- label: XIV.2.2.1 -->

Let

```text
X′ --h--> X
|         |
f′        f
|         |
v         v
S′ --g--> S
```

be a cartesian square, where the schemes $S$ and $S'$ are locally noetherian, catenary, the morphism $f$ locally of
finite type, and $g$ faithfully flat. Let $T$ be a closed part of $S$, $T'$ a closed part of $S'$ such that
$g(T') \subset T$, $x'$ an element of $X'$, $x = h(x')$ and

```text
h_{x′} : Spec O_{X′,x′} → Spec O_{X,x}
```

the morphism induced by $h$. Then one has:

```text
δ_T(x) − δ_{T′}(x′) ⩽ dim h_{x′}^{−1}(x).
```

Let $s' = f'(x')$, $s = f(x)$. By definition:

```text
δ_T(x) − δ_{T′}(x′) = deg.tr. k(x)/k(s) − deg.tr. k(x′)/k(s′)
                     + codim({s} ∩ T, {s}) − codim({s′} ∩ T′, {s′}).
```

Since $g$ is faithfully flat, it follows from (EGA IV 6.1.4) that one has

```text
(∗) codim({s} ∩ T, {s}) = codim(g^{−1}({s}) ∩ g^{−1}(T), g^{−1}({s}))
                       ⩽ codim(g^{−1}({s}) ∩ T′, g^{−1}({s}));
```

since $S'$ is catenary, one has, by (EGA 0_IV 14.3.2 b)):

```text
codim({s′} ∩ T′, g^{−1}({s})) = codim({s′} ∩ T′, {s′}) + codim({s′}, g^{−1}({s}))
   = codim({s′} ∩ T′, g^{−1}({s}) ∩ T′) + codim(g^{−1}({s}) ∩ T′, g^{−1}({s})).
```

One deduces from this relation and (∗)

<!-- original page 237 -->

```text
δ_T(x) − δ_{T′}(x′) ⩽ deg.tr. k(x)/k(s) − deg.tr. k(x′)/k(s′) + codim({s′}, g^{−1}({s})).
```

Let us compute $codim({s'}, g^{-1}({s})) = \dim O_{S'_{s}, s'}$ (where $S'_{s}$ is the fiber of $S'$ at $s$). Let $Z$ be
the closed image of $x$ in $X_{s}$ and $Z' \subset X'_{s}$ the scheme defined by the cartesian square

```text
Z′ ----→ Z
|        |
v        v
S′_s --→ Spec k(s)
```

The morphism $Z \to \operatorname{Spec} k(s)$ is flat, locally of finite type, and one has $\dim Z = deg.tr. k(x)/k(s)$.
It then follows from (EGA IV 6.1.2) that

```text
dim(O_{Z′,x′}) = dim(O_{S′_s, s′}) + deg.tr. k(x)/k(s) − deg.tr. k(x′)/k(s′);
```

taking into account the fact that $Z'_{s'} \simeq Z \otimes_{k(s)} k(s')$, one obtains:

$$
\delta_{T}(x) - \delta_{T'}(x') \leqslant \dim(O_{Z',x'}).
$$

Now $\operatorname{Spec}(O_{Z',x'})$ is identified with the fiber at $x$ of the morphism

$$
(\operatorname{Spec}(O_{X',x'}))_{s} \to (\operatorname{Spec}(O_{X,x}))_{s},
$$

hence also with the fiber at $x$ of $h_{x'}$, which proves the theorem.

**2.3.** The proofs of the theorems of §4 are based on duality theory; they use the following lemmas. Let $m$ be an
integer that is a power of a prime number $\ell$; if $X$ is a scheme, all the sheaves considered on $X$ are sheaves of
$\mathbb{Z}/m\mathbb{Z}$-modules; one then has

<!-- original page 238 -->

the notion of dualizing complex on $X$ (SGA 5 I 1.7). Suppose there exists such a complex $K$ on $X$; then, for each
geometric point $\bar{x}$ above a point $x$ of $X$, one deduces from $K$ (cf. SGA 5 I 4.5) a dualizing complex
$K_{\bar{x}}$ on $\operatorname{Spec} k(\bar{x})$, so that one has $K_{\bar{x}} \simeq \mathbb{Z}/m\mathbb{Z}[n]$ (the
bracket denoting the translation functor) for some integer $n$ depending only on $x$. We shall set

$$
\delta^{K}(x) = n.
$$

If $K$ is normalized at the point $x$ (SGA 5 I 4.5), one therefore has $n = 0$.

**Lemma 2.3.1.**

<!-- label: XIV.2.3.1 -->

Let $X$ be a locally noetherian scheme equipped with a dualizing complex $K$. If $x$ and $x'$ are two points of $X$ such
that $x$ is a specialization of $x'$ and that $codim({x}, {x'}) = 1$, then one has

$$
\delta^{K}(x) = \delta^{K}(x') - 2.
$$

One can first reduce to the case where $X$ is a strictly local scheme. Indeed, let $\bar{X}$ be the strict localization
of $X$ at a geometric point $\bar{x}$ above $x$, $i : \bar{X} \to X$ the canonical morphism, and $\bar{x}'$ a geometric
point of $\bar{X}$ above $x'$. Then $i^{*} K$ is a dualizing complex on $\bar{X}$ and one has (SGA 5 I 4.5)

```text
(i^* K)_{x̄} ≃ K_{x̄} and (i^* K)_{x̄′} ≃ K_{x̄′},
```

<!-- original page 239 -->

which completes the reduction to the strictly local case.

If $j : {x'} \to X$ denotes the immersion of the reduced closed subscheme of $X$ with underlying space ${x'}$, then
$R^{!} j(K)$ is a dualizing complex on ${x'}$ and one sees immediately, using (SGA 5 I 4.5), that it suffices to prove
the lemma for ${x'}$. One is thus reduced to the case where $X$ is a strictly local integral scheme of dimension `1`.

Let then $X'$ be the normalization of $X$ and $f : X' \to X$ the canonical morphism; $f$ is an integral, surjective,
radicial morphism, and it follows that $f^{*} K$ is a dualizing complex on $X'$ and that it suffices to prove the lemma
for $X'$ and for the points above $x$ and $x'$. One is thus reduced to the case where $X$ is a regular integral local
scheme of dimension `1`, but one knows (cf. SGA 5 I 4.6.2 and 5.1) that then $\mu_{m}[2]$ and $\mathbb{Z}/m\mathbb{Z}$
are dualizing complexes, normalized respectively at the points $x$ and $x'$; the lemma follows immediately.

**Lemma 2.3.2.**

<!-- label: XIV.2.3.2 -->

Let $S$ be a noetherian local scheme, $f : X \to S$ a morphism of finite type. If $K$ is a dualizing complex on $S$,
normalized at the closed point $t$ of $S$, and if $R^{!} f(K) = K'$ is a dualizing complex on $X$ (cf. SGA 5 I 3.4.3),
one has, for every point $x$ of $X$:

$$
\delta^{K'}(x) = 2 \delta(x).
$$

Indeed let $s = f(x)$ and $x'$ a closed point of the fiber $X_{s}$; then one has $\delta^{K'}(x') = \delta^{K}(s)$ and
by 2.3.1

```text
δ^K(s) = 2 codim({t}, {s}) = 2 dim({s}).
```

<!-- original page 240 -->

Since one can choose for $x'$ a specialization of $x$, one has by 2.3.1

```text
δ^{K′}(x) = δ^{K′}(x′) + 2 codim({x}, {x′}) = δ^{K′}(x′) + 2 deg.tr. k(x)/k(s);
```

the lemma follows immediately.

The following lemma will be used only for the converse of the Lefschetz theorem in §4:

**Lemma 2.3.3.**

<!-- label: XIV.2.3.3 -->

Let

```text
X′ --h--> X
|         |
f′        f
|         |
v         v
S′ --g--> S
```

be a cartesian square, where $S$ is a strictly local excellent scheme of characteristic zero, $S'$ the completion of
$S$, and $f$ a morphism of finite type. Let $\ell$ be a prime number, $x \in X$, $Z$ the

<!-- original page 241 -->

schematic closure of $X'_{x}$ in $X'$, and $i : X'_{x} \to Z$, $j : Z \to X$ the canonical morphisms. Then, if
$k : X' \to R$ is a closed immersion of $X'$ into a regular excellent scheme $R$ of characteristic zero, the complex

$$
K' = i^{*}(R^{!}(k \cdot j)(\mathbb{Z}/\ell \mathbb{Z}))
$$

is a dualizing complex on $X'_{x}$ that is constant (that is, having only one non-null cohomology sheaf, isomorphic to
$\mathbb{Z}/\ell \mathbb{Z}$).

Taking (SGA 5 I 3.4.3) into account, the only thing to prove is that $K'$ is constant. Now, since $Z$ is excellent, the
set of points of $Z$ whose local rings are regular is an open set $U$ (EGA IV 7.8.3 (iv)), and $U$ evidently contains
$X'_{x}$ which is regular. Let then

$$
u : U \to R
$$

be the canonical immersion of $U$ in $R$; it follows from the purity theorem (SGA 4 XIX 3.2 and 3.4) and from the
isomorphism

$$
(\mu_{\ell})_{S} \simeq (\mathbb{Z}/\ell \mathbb{Z})_{S}
$$

($S$ strictly local) that one has

$$
R^{!} u(\mathbb{Z}/\ell \mathbb{Z}) \simeq \mathbb{Z}/\ell \mathbb{Z}[2c],
$$

where $c$ is a locally constant function on $U$, necessarily constant in a neighborhood of $X'_{x}$, since the fibers of
$g$ are geometrically integral by (EGA IV 18.9.1) hence $X'_{x}$ integral. The lemma follows immediately.

## 3. Converse of the affine Lefschetz theorem

The present section will be used in §4 to prove a converse to the "Lefschetz theorem"; a reader interested only in the
direct part of the said theorem may therefore omit the reading of the present section.

**3.1.** Let us recall the statement of the affine Lefschetz theorem[^N.D.E-XIV-5] (SGA 4 XIX 6.1 bis):

Let $S$ be a strictly local excellent scheme of characteristic zero, $f : X \to S$ an affine morphism of finite type,
and $F$ a torsion sheaf on $X$. Then, if one sets

<!-- original page 242 -->

```text
δ(F) = sup{δ(x) | x ∈ X and F_x ≠ 0},
```

one has

```text
H^q(X, F) = 0 for q > δ(F).
```

Before stating the converse, let us prove a few lemmas.

**Lemma 3.2.**

<!-- label: XIV.3.2 -->

Let $K$ be a field, $\ell$ a prime number distinct from the characteristic of $K$, and $F$ an $\ell$-torsion sheaf on
$K$, constructible, non-null. Suppose that the $\ell$-cohomological dimension of $K$ (SGA 4 X 1) is equal to $n$ (this
is realized for example if $K$ is the field of fractions of a strictly local excellent integral ring of characteristic
zero of dimension $n$ (SGA 4 XIX 6.3), or if $K$ is a finitely generated extension of transcendence degree $n$ of a
separably closed field (SGA 4 X 2.1)). Then one can find a finite separable extension $L$ of $K$ such that:

$$
H^{n}(L, F|_{L}) \neq 0.
$$

One can find a finite extension $K'$ of $K$ such that the restrictions of $F$ and $\mu_{\ell}$ to
$\operatorname{Spec} K'$ are constant sheaves. One then has $cd_{\ell}(K') = cd_{\ell}(K) = n$ (SGA 4 X 2.1), and it
follows from ([2] II §3 Prop. 4 (iii)) that one can find a finite extension $L$ of $K'$ such that

<!-- original page 243 -->

```text
H^n(L, μ_ℓ) ≠ 0, i.e. H^n(L, ℤ/ℓℤ) ≠ 0.
```

Now the functor $H^{n}(L, \cdot)$ is right exact on the category of $\ell$-torsion sheaves, since $cd_{\ell}(L) = n$;
since $F$ admits a quotient isomorphic to $\mathbb{Z}/\ell \mathbb{Z}$, one also has $H^{n}(L, F|_{L}) \neq 0$.

**Corollary 3.3.**

<!-- label: XIV.3.3 -->

Let $k$ be a field, $K$ a finitely generated extension of transcendence degree $n$ of $k$, $F$ a constructible non-null
$\ell$-torsion sheaf on $K$, with $\ell$ prime to the characteristic of $k$. Then one can find a finite separable
extension $L$ of $K$ such that, if $u : \operatorname{Spec} L \to \operatorname{Spec} k$ denotes the canonical morphism,
one has

$$
R^{n} u_{*}(F|_{\operatorname{Spec} L}) \neq 0.
$$

When the field $k$ is separably closed, the corollary is a particular case of 3.2. In the general case, one can find a
finite separable extension $k_{1}$ of $k$ such that the irreducible components of $K \otimes_{k} k_{1}$ are
geometrically irreducible (EGA IV 4.5.11); let `K_1` be one of them. If $k'$ is a separable closure of $k_{1}$, then
$K' = K_{1} \otimes_{k_{1}} k'$ is a field, and one has by (EGA IV 4.2)

```text
deg.tr. K′/k′ = deg.tr. K/k = n.
```

It then follows from 3.2 that one can find a finite separable extension $L'$ of $K'$ such that one has
$H^{n}(L', F|_{L'}) \neq 0$. But $k' = \lim_{i} k_{i}$ (direct limit), where $k_{i}$ runs over the finite extensions of
$k_{1}$ contained in $k'$, and consequently $K' = \lim_{i} (k_{i} \otimes_{k_{1}} K_{1})$. It follows that one

<!-- original page 244 -->

can find an index $i$ and a finite separable extension $L$ of $k_{i} \otimes_{k_{1}} K_{1} = K_{i}$ such that one has
$L' \simeq L \otimes_{K_{i}} K'$. The extension $L$ of $K$ answers the question; indeed it follows from the commutative
diagram

```text
        Spec L
       /     \
      v       u
     /         \
    v           \
Spec k_i --w--> Spec k,
```

with $w$ finite, hence $R^{q} w_{*} = 0$ if $q > 0$, that one has

```text
R^n u_*(F|_{Spec L}) ≃ w_*(R^n v_*(F|_{Spec L})).
```

Now $R^{n} v_{*}(F|_{\operatorname{Spec} L}) \neq 0$, since $H^{n}(L', F|_{L'}) \neq 0$; one therefore also has
$R^{n} u_{*}(F|_{\operatorname{Spec} L}) \neq 0$.

Let us recall the following well-known lemma (cf. EGA 0_III 10.3.1.2 and EGA IV 18.2.3):

**Lemma 3.4.**

<!-- label: XIV.3.4 -->

Let $X$ be a scheme, $x$ a point of $X$, $K$ a finite separable extension of $k(x)$. Then there exists a scheme `X_1`
étale over $X$, affine, and a point $x_{1} \in X_{1}$ above $x$ such that $k(x_{1})$ is $k(x)$-isomorphic to $K$.

We shall use in §4 the following technical form of the converse of 3.1.

**Proposition 3.5.**

<!-- label: XIV.3.5 -->

<!-- original page 245 -->

Let

```text
X′ --h--> X
|         |
f′        f
|         |
v         v
S′ --g--> S,
```

be a cartesian square where the schemes $S$ and $S'$ are strictly local excellent of characteristic zero, the morphism
$f$ locally of finite type, $g$ regular (EGA IV 6.8.1) surjective, with closed fiber of $g$ reduced to the closed point
of $S'$. Given an $S$-scheme `X_1` (resp. an $S$-morphism $f_{1}$, etc.), we shall denote by $X'_{1}$ (resp. $f'_{1}$,
etc.) the scheme $X_{1} \times_{S} S'$ (resp. the morphism $(f_{1})_{(S')}$, etc.). Let $F$ be a constructible sheaf of
$\mathbb{Z}/m\mathbb{Z}$-modules on $X'$ ($m$ a power of a prime number $\ell$) satisfying the following conditions:

(i) For every point $x \in X$, one can find a finite separable extension $K$ of $k(x)$ such that the restriction of $F$
to the fiber $(X')_{(\operatorname{Spec} K)}$ comes by inverse image from a constructible sheaf on
$\operatorname{Spec} K$.

(ii) For every morphism $f_{1} : X_{1} \to S$, with `X_1` étale over $X$, affine, for every point $s \in S$, and for
every integer $q > 0$, one can find a finite separable extension $K$ of $k(s)$ such that the restriction of
$R^{q} f'_{1*}(F|_{X'_{1}})$ to the fiber $S'_{(\operatorname{Spec} K)}$ comes by inverse image from a constructible
sheaf on $\operatorname{Spec} K$.

Let $n$ be an integer, and suppose that for every scheme `X_1` étale over $X$, affine, one has

<!-- original page 246 -->

```text
H^i(X′_1, F) = 0 for i > n.
```

Then, if $\bar{x}'$ is a geometric point above the point $x' \in X'$ such that $F_{\bar{x}'} \neq 0$, one has

$$
\delta(x') \leqslant n.
$$

Let $Z'$ be the set of points $x'$ of $X'$ such that $F_{\bar{x}'} = 0$. Then, if $Z = h(Z')$, one has by (i)
$Z' = h^{-1}(Z)$; let $x' \in X'$, $x = h(x')$, $s' = f'(x')$, $s = f(x)$. It follows from 2.1.1 and from the fact that
the function $\delta$ decreases under specialization that it suffices to prove the inequality $\delta(x') \leqslant n$
when $x$ is a maximal point of $Z$ and $x'$ is such that

```text
r = deg.tr. k(x)/k(s) = deg.tr. k(x′)/k(s′) and d = dim {s} = dim {s′}.
```

Let $x'$ be such a point; it suffices to show that one can find a scheme `X_1` étale over $X$, affine, such that one has

$$
H^{d+r}(X'_{1}, F) \neq 0.
$$

The set $Z'$ is constructible (SGA 4 IX 2.4), hence the same holds for $Z$ (EGA IV 1.9.12); one can then suppose, by
restricting $X$ to a neighborhood of $x$, that $Z$ is an irreducible closed set with generic point $x$. Let $T = f(Z)$;
$T$ is a constructible set contained in ${s}$; one can therefore find an affine open $U$ of $S$ such that $s \in U$ and
that $T \cap U = T_{U}$ is an irreducible closed set of $U$ with generic point $s$.

<!-- original page 247 -->

Let then $V$ be a scheme étale over $X$, affine, whose image in $X$ contains $x$ and whose image in $S$ is contained in
$U$; let `Z_V` be the inverse image of $Z$ in $V$ and $u : Z_{V} \to T_{U}$ the canonical morphism. Let $W$ be a scheme
étale over $U$, affine; we then denote by `T_W` the inverse image of `T_U` in $W$ and let $X_{1} = W \times_{U} V$.
Since $F$ is null outside $Z'$, one has the spectral sequence

```text
E_2^{pq} = H^p((T_W)′, R^q u′_*(F|_{(Z_V)′})) ⟹ H^{p+q}(X′_1, F).
```

We shall show that one can choose $V$ and $W$ such that one has

a) $E^{pq}_{2} = 0$ for $p > d$ and for $q > r$.

b) $E^{dr}_{2} \neq 0$.

It will then follow from the spectral sequence that $H^{d+r}(X'_{1}, F) \neq 0$.

1°) Set $G^{q} = R^{q} u'_{*}(F|_{(Z_{V})'})$; then one has:

$$
(G^{q})_{s'} = H^{q}((Z_{V})'_{s'}, F|_{(Z_{V})'_{s'}}),
$$

since $s'$ is a maximal point of $(T_{U})'$. Since the fiber $(Z_{V})'_{s'}$ is an affine scheme of finite type of
dimension $r$ over a separably closed field, it follows from 3.1 that one has

```text
(G^q)_{s′} = 0 for q > r.
```

<!-- original page 248 -->

For $q > r$, let $Y'_{q}$ be the set of points of $(T_{U})'$ where the geometric fiber of $G^{q}$ is $\neq 0$ and
$Y_{q} = g(Y'_{q})$; then one has $Y'_{q} = g^{-1}(Y_{q})$ by (ii), so $Y_{q}$ is a constructible subset of `T_U` (SGA 4
XIX 5.1 and EGA 1.9.12) which does not contain $s$; restricting $U$ to an open neighborhood of $s$, one can suppose that
one has $G^{q} = 0$ for $q > r$, hence $E^{pq}_{2} = 0$ for $q > r$.

Moreover, since $(T_{W})'$ is an affine scheme of finite type over $g^{-1}({s})$, one has, whatever $q$ (cf. 3.1):

```text
H^p((T_W)′, G^q) = 0 for p > dim g^{−1}({s}) = d,
```

whence condition a).

2°) Let us show that one can choose $V$ such that $(G^{r})_{s'} \neq 0$. By (i), there exists a constructible sheaf $I$,
defined on a finite separable extension $K$ of $k(x)$, whose inverse image on $(X')_{(\operatorname{Spec} K)}$ is
isomorphic to $F|_{(X')_{(\operatorname{Spec} K)}}$. By 3.3, one finds a finite separable extension $L$ of $K$ such
that, if $v : \operatorname{Spec} L \to \operatorname{Spec} k(s)$ denotes the canonical morphism, one has
$R^{r} v_{*}(I) \neq 0$. Since the morphism $S'_{s} \to \operatorname{Spec} k(s)$ is regular, one has by (SGA 4 XIX
4.2):

```text
R^r v′_*(F|_{(Spec L)′}) ≃ (R^r v_*(I))′ ≠ 0.
```

By Lemma 3.4, one can find a scheme `X_2` étale over $X$, affine, and a point $x_{2}$ of `X_2` above $x$ such that $L$
is $k(x)$-isomorphic to $k(x_{2})$, and one can suppose `X_2` over $U$. Since $x$ is a maximal point of $Z$, one has

<!-- original page 249 -->

```text
Spec L ≃ lim ← _V Z_V,
```

where $V$ runs over the affine open neighborhoods of $x_{2}$. One deduces by passage to the limit (SGA 4 VII 5.8), after
restriction to the geometric fiber at $s'$:

```text
(R^r v′_*(F|_{Spec L})′)_{s′} = lim → _V (R^r u′_*(F|_{(Z_V)′}))_{s′},
```

which shows that one can find $V$ such that $(G^{r})_{s'} \neq 0$.

3°) The scheme $V$ having been chosen in 2°), let us show that one can choose the scheme $W$ such that one has

$$
E^{dr}_{2} = H^{d}((T_{W})', G^{r}) \neq 0.
$$

By (ii), there exists a constructible sheaf $J$, defined on a finite separable extension $K$ of $k(s)$, whose inverse
image on $(S')_{(\operatorname{Spec} K)}$ is isomorphic to $G^{r}|_{(S')_{(\operatorname{Spec} K)}}$. By Lemma 3.2, one
can find a finite separable extension $L$ of $K$ such that one has $H^{d}(\operatorname{Spec} L, J) \neq 0$. Since the
morphism $(S')_{(\operatorname{Spec} L)} \to \operatorname{Spec} L$ is acyclic (SGA 4 XIX 4.1 and XV 1.10 and 1.16), one
has

```text
H^d((Spec L)′, G^r|_{(S′)_{(Spec L)}′}) = H^d(Spec L, J) ≠ 0.
```

By 3.4, one can find a scheme `U_1` étale over $U$, affine, and a point $s_{1}$ above $s$, such that $k(s_{1})$ is
$k(s)$-isomorphic to $L$. Now, $s$ being a maximal point of `T_U`, one has

```text
Spec L ≃ lim ← _W T_W,
```

where $W$ runs over the affine open neighborhoods of $s_{1}$. One deduces that $(\operatorname{Spec} L)' \simeq$

<!-- original page 250 -->

$\lim \leftarrow {}_{W} (T_{W})'$, and by passage to the limit (SGA 4 VII 5.8):

```text
H^d((Spec L)′, G^r|_{(Spec L)′}) ≃ lim → _W H^d((T_W)′, G^r|_{(T_W)′});
```

consequently one can find $W$ such that one has

$$
H^{d}((T_{W})', G^{r}|_{(T_{W})'}) \neq 0,
$$

which completes the proof of the theorem.

**Corollary 3.6.**

<!-- label: XIV.3.6 -->

The hypotheses concerning $S, S', f, f', m$ are those of 3.5. Denote now by $F$ a complex of sheaves of
$\mathbb{Z}/m\mathbb{Z}$-modules on $X'$, bounded below and with constructible cohomology, and whose cohomology sheaves
satisfy conditions (i) and (ii) of 3.5. Let $n$ be an integer, and suppose that, for every scheme `X_1` étale over $X$,
affine, one has

```text
H^i(X′_1, F) = 0 for i > n.
```

Then, if $\bar{x}'$ is a geometric point above a point $x'$ of $X'$ such that, for some integer $j$,
$(H^{j}(F))_{\bar{x}'} \neq 0$, one has

$$
\delta(x') \leqslant n - j.
$$

Let $T'$ be the set of points of $X'$ where the conclusion of 3.7 fails, and suppose $T' \neq \emptyset$; let
$T = f(T')$, $x$ a maximal point of $T$, and $x'$ a point of $X'$ above

<!-- original page 251 -->

$x$. Let $j$ be the largest integer such that $(H^{j}(F))_{\bar{x}'} \neq 0$; one therefore has $r = \delta(x) > n - j$.
Let $Z'_{q}$ be the set of points where the geometric fiber of $H^{q}(F)$ is `= 0` and $Z_{q} = h(Z'_{q})$; as in the
proof of 3.5, $Z_{q}$ is constructible. One evidently has $Z'_{q} = \emptyset$ for $q > n$ and for $q$ sufficiently
small. The other values of $q$ are distributed in three subsets. Let

```text
Q_1 = {q | x ∈ Z_q and a generization of x distinct from x is ∉ Z_q}.
```

One has $j \in Q_{1}$ and one can find an affine open neighborhood `U_1` of $x$ such that, for every $q \in Q_{1}$,
$U_{1} \cap Z_{q}$ is an irreducible closed set with generic point $x$. If $q \in Q_{1}$, one has

```text
(∗)    δ(H^q(F)|_{U′_1}) = δ(x)    (for the definition of δ(H^q(F)) cf. 3.1).
```

Let

```text
Q_2 = {q | no generization of x belongs to Z_q}.
```

Then, if $j < q \leqslant n$, one has $q \in Q_{2}$, and one can find an affine open neighborhood `U_2` of $x$ such
that, for every $q \in Q_{2}$, one has $Z_{q} \cap U_{2} = \emptyset$; thus

```text
(∗∗)   H^q(F)|_{U′_2} = 0 for q ∈ Q_2.
```

Let finally

```text
Q_3 = {q | Z_q contains strict generizations of x}.
```

Then one can find an affine open neighborhood `U_3` of $x$ such that, for every $q \in Q_{3}$, all the maximal points of
$Z_{q} \cap U_{3}$ are generizations of $x$. If $q \in Q_{3}$, one has

$$
(\ast\ast\ast)  \delta(H^{q}(F)|_{U'_{3}}) \leqslant n - q.
$$

For every scheme `X_1` étale over $U_{1} \cap U_{2} \cap U_{3}$, affine, consider the

<!-- original page 252 -->

hypercohomology spectral sequence

```text
E_2^{pq} = H^p(X′_1, H^q(F)) ⟹ H^{p+q}(X′_1, F).
```

One has $E^{pq}_{2} = 0$ for $q \in Q_{2}$ by (∗∗). One has $E^{pq}_{2} = 0$ for $p + q \geqslant r + j$ except perhaps
for $p = r$, $q = j$. Indeed this is clear if $q \in Q_{2}$; if $q \in Q_{1}$, one has $p > r$ unless $p = r$, $q = j$,
and this follows from 3.1 taking (∗) into account; finally if $q \in Q_{3}$, since $r > n - j$, one has $p > n - q$ and
the assertion follows from 3.1 taking (∗∗∗) into account. Given that $H^{r+j}(X'_{1}, F) = 0$, it follows from the
spectral sequence that one has

$$
H^{r}(X'_{1}, H^{j}(F)) = 0;
$$

now this entails, by 3.5, $\delta(x) < r$, which is absurd.

**Corollary 3.7.**

<!-- label: XIV.3.7 -->

Let $S$ be a strictly local excellent scheme of characteristic zero, $f : X \to S$ a morphism locally of finite type,
$m$ a power of a prime number, $F$ a complex of sheaves of $\mathbb{Z}/m\mathbb{Z}$-modules on $X$, bounded below with
constructible cohomology, and $n$ an integer. Then the following conditions are equivalent:

(i) For every scheme `X_1` étale over $X$, affine, one has

```text
H^i(X_1, F) = 0 for i > n.
```

(ii) For every geometric point $\bar{x}$ above the point $x$ of $X$ and for every integer $j$

<!-- original page 253 -->

such that $(H^{j}(F))_{\bar{x}} \neq 0$, one has

$$
\delta(x) \leqslant n - j.
$$

(i) ⇒ (ii) is the particular case of 3.6 obtained by taking $S = S'$.

(ii) ⇒ (i) follows immediately from 3.1, using the hypercohomology spectral sequence

```text
H^p(X_1, H^q(F)) ⟹ H^*(X_1, F).
```

## 4. Main theorem and variants

**4.0.** Let $g : X \to S$ be a separated morphism of finite type, $T$ a closed part of $S$, $Z = g^{-1}(T)$, and $F$ a
complex of abelian sheaves on $X$ bounded below. We call $i$-th cohomology group of $F$ with proper support, with
support in $Z$, the group

```text
H^i_{Z!}(X/S, F) = H^i_T(S, R^! g(F)),
```

<!-- original page 254 -->

where $R^{!} g$ denotes "direct image with proper support" (SGA 4 XVII). In the particular case where $g$ is proper, one
simply has

```text
H^i_{Z!}(X/S, F) = H^i_Z(X, F).
```

**Proposition 4.1.**

<!-- label: XIV.4.1 -->

Let $f : U \to S$ be a morphism of finite type, $F$ a complex of abelian sheaves on $U$ bounded below. Suppose one has a
factorization of $f$:

```text
U --i--> X
 \      /
  \    /
   f  g
    \/
    S
```

where $i$ is an open immersion and $g$ a separated morphism of finite type, and denote by $G$ a complex of abelian
sheaves on $X$ bounded below that prolongs $F$. Let $Y$ be a closed subscheme of $X$ with underlying space $X - U$, so
that one has a commutative diagram:

```text
Y --j--> X
 \      /
  h    g
   \  /
    S
```

Let finally $n$ be an integer and $T$ a closed part of $S$. Then the following conditions are equivalent:

(i) One has $prof_{T}(R^{!} f(F)) \geqslant n$.

(ii) The canonical morphism

```text
ℋ^i_T(R^! g(G)) → ℋ^i_T(R^! h(j^* G))
```

is bijective for $i < n - 1$, injective for $i = n - 1$.

<!-- original page 255 -->

(iii) For every scheme $S'$ étale over $S$, if one denotes by $X'$ (resp. $f'$, resp. etc.) the scheme $X \times_{S} S'$
(resp. the morphism $f_{(S')}$, resp. etc.), the canonical morphism

```text
H^i_{g′^{−1}(T′)!}(X′/S′, G′) → H^i_{h′^{−1}(T′)!}(Y′/S′, j′^* G′)
```

is bijective for $i < n - 1$, injective for $i = n - 1$.

Consider in the derived category $D^{+}(X)$ (cf. [3]) the distinguished triangle

```text
        j_* j^* G
       ↗      ↘
   i_! F ←-------- G.
```

In applying to this triangle the functor $R^{!} g$, one obtains the triangle

```text
              R^! h(j^* G)
             ↗            ↘
(∗)    R^! f(F) ←--------- R^! g(G).
```

Let us show (i) ⇔ (ii). Indeed, by Definition 1.2, (i) is equivalent to the relation

```text
ℋ^i_T(R^! f(F)) = 0 for i < n;
```

now one deduces from (∗) the exact sequence of sheaves

```text
→ ℋ^i_T(R^! f(F)) → ℋ^i_T(R^! g(G)) → ℋ^i_T(R^! h(j^* G)) →,
```

whence the equivalence of (i) and (ii).

<!-- original page 256 -->

(i) ⇔ (iii). Indeed (i) is equivalent to saying that, for every scheme $S'$ étale over $S$, one has the relation

```text
(∗∗) H^i_{T′}(S′, R^! f′(F′)) = 0 for i < n.
```

Now one deduces from (∗) the exact sequence of abelian groups

```text
→ H^i_{T′}(S′, R^! f′(F′)) → H^i_{T′}(S′, R^! g′(G′)) → H^i_{T′}(S′, R^! h′(j′^* G′)) →;
```

taking 4.0 into account, this exact sequence writes in the form

```text
→ H^i_{T′}(S′, R^! f′(F′)) → H^i_{g′^{−1}(T′)!}(X′/S′, G′) → H^i_{h′^{−1}(T′)!}(Y′/S′, j′^* G′) →.
```

The equivalence of (i) and (iii) follows, taking the form (∗∗) of (i) into account.

**4.2.0.** When $f : U \to S$ is affine, we shall give local conditions on $F$ for conditions (i) to (iii) of 4.1 to be
verified. In what follows, the schemes considered are excellent schemes of characteristic zero, the sheaves are sheaves
of $\mathbb{Z}/m\mathbb{Z}$-modules, where $m$ is a power of a prime number. If one had resolution of singularities in
the sense of (SGA 4 XIX), the results stated, as well as their proofs, would still be valid for excellent schemes of
equal characteristic, with $m$ prime to the characteristic.

**Theorem 4.2.**

<!-- label: XIV.4.2 -->

<!-- original page 257 -->

Let $S$ be an excellent scheme of characteristic zero and $f : U \to S$ a separated morphism of finite type. Let $F$ be
a complex of sheaves of $\mathbb{Z}/m\mathbb{Z}$-modules on $U$, bounded below with constructible cohomology, $n$ an
integer, and $T$ a closed part of $S$. Then the following conditions are equivalent:

(i) For every scheme `U_1` étale over $U$, affine over $S$, one has, denoting by $f_{1}$ the structural morphism of
`U_1` and by `F_1` the restriction of $F$ to `U_1`:

$$
prof_{T}(R^{!} f_{1}(F_{1})) \geqslant n
$$

(cf. Prop. 4.1 on the meaning of this relation).

(ii) For every point $u$ of $U$, one has:

$$
prof_{u}(F) \geqslant n - \delta_{T}(u),
$$

where one sets (cf. 2.2): $\delta_{T}(u) = deg.tr.(k(x)/k(s)) + codim({s} \cap T, {s})$.

*Proof.*

1°) Let $t$ be a point of $T$, $\bar{S}$ the strict localization of $S$ at a geometric point above $t$, and $S'$ the
completion of $\bar{S}$ with closed point $t'$; then $\bar{S}$ is excellent by (EGA IV 7.9.5), so $S'$ is a complete
strictly local excellent scheme. Given a scheme $U$ over $X$ (resp. an $S$-morphism $f$, resp. etc.), we shall denote by
$U'$ (resp. $f'$, resp. etc.) the scheme $U \times_{S} S'$ (resp. the morphism $f_{(S')}$, resp. etc.). One has the
cartesian square

```text
U′ --h--> U
|         |
f′        f
|         |
v         v
S′ --g--> S,
```

<!-- original page 258 -->

in which the morphism $g$ is regular (EGA IV 7.8.2). Let us show that it suffices to prove that (for every point
$t \in T$) the two following properties are equivalent:

(i)\_t For every scheme `U_1` étale over $U$, affine over $S$, setting $f_{1} : U_{1} \to S$, one has

$$
prof_{t'}(R^{!} f'_{1}(F'_{1})) \geqslant n.
$$

(ii)\_t For every point $u'$ of $U'$, one has

$$
prof_{u'}(F') \geqslant n - \delta_{t'}(u').
$$

It suffices to prove the following lemma:

**Lemma 4.2.1.**

<!-- label: XIV.4.2.1 -->

One has (i) ⇔ (i)\_t for every $t \in T$ and (ii) ⇔ (ii)\_t for every $t \in T$.

(i) ⇔ (i)\_t for every $t \in T$. Indeed (i) is equivalent to saying that, for every scheme `U_1` étale over $U$, affine
over $S$, one has

$$
prof_{T}(R^{!} f_{1}(F_{1})) \geqslant n;
$$

now by 1.8

```text
prof_T(R^! f_1(F_1)) = inf_{t ∈ T} prof_t(R^! f_1(F_1)).
```

Since $g^{*}(R^{!} f_{1}(F_{1})) \simeq R^{!} f'_{1}(F'_{1})$ (SGA 4 XVII), one has by 1.16

```text
prof_t(R^! f_1(F_1)) = prof_{t′}(R^! f′_1(F′_1)),
```

<!-- original page 259 -->

so (i) is equivalent to saying that one has, for every $t \in T$, $prof_{t'}(R^{!} f'_{1}(F'_{1})) \geqslant n$, which
is none other than (i)\_t.

(ii)\_t for every $t \in T$ ⇒ (ii). Indeed let $u \in U$; one must show the relation

$$
prof_{u}(F) \geqslant n - \delta_{T}(u),
$$

where $\delta_{T}(u) = \inf_{t \in T \cap {s}} \delta_{t}(u)$ (cf. 2.2); one is therefore reduced to showing that one
has, for every $t \in T \cap {s}$

$$
prof_{u}(F) \geqslant n - \delta_{t}(u).
$$

Let $u'$ be a point of $U'$ such that $h(u') = u$ and $\delta_{t'}(u') = \delta_{t}(u)$ (cf. 2.1.1). Since $h$ is
locally acyclic (SGA 4 XIX 4.1), it follows from 1.16 and from the fact that $u'$ is a generic point of $U'_{u}$ that
one has

$$
prof_{u'}(F') = prof_{u}(F).
$$

But one has by (ii)\_t $prof_{u}(F) = prof_{u'}(F') \geqslant n - \delta_{t}(u)$, which proves (ii).

(ii) ⇒ (ii)\_t for every $t$. With the notations of 2.2.1, for every point $u'$ of $U'$, one has by 1.16

```text
prof_{u′}(F′) ⩾ prof_u(F) + 2 dim h_{u′}^{−1}(u) ⩾ prof_u(F) + dim h_{u′}^{−1}(u).
```

Taking 2.2.1 and (ii) into account, one obtains

```text
prof_{u′}(F′) ⩾ n − δ_T(u) + dim h_{u′}^{−1}(u) ⩾ n − δ_{t′}(u′),
```

which is none other than (ii)\_t.

<!-- original page 260 -->

2°) (ii)\_t ⇔ (i)\_t. One immediately reduces to the case where $F$ is bounded, by truncating $F$ at a sufficiently high
rank. One can realize $S'$ as a closed subset of a complete regular local scheme, hence excellent; it then follows from
(SGA 5 I 3.4.3) that there exists a dualizing complex $K$ on $S'$ and that $R^{!} f'(K) = K'$ is a dualizing complex on
$U'$. We shall choose $K$ such that $\delta^{K}(t') = 0$ (for the definition of $\delta^{K}(t')$, cf. 2.3), and denote
by $DF'$ the dual of $F'$ with respect to $K'$. One can reformulate hypothesis (ii)\_t as follows:

**Lemma 4.2.2.**

<!-- label: XIV.4.2.2 -->

Let $u'$ be a point of $U'$; then the following conditions are equivalent:

(i) One has $prof_{u'}(F') \geqslant n - \delta_{t'}(u')$.

(ii) One has $(H^{q}(DF'))_{\bar{u}'} = 0$ for $q > -n - \delta_{t'}(u')$ ($\bar{u}'$ geometric point above $u'$).

Let $\bar{U}'$ be the strict localization of $U'$ at $\bar{u}'$ and $\bar{F}'$ the inverse image of $F'$ by the morphism
$\bar{U}' \to U'$. The relation $prof_{u'}(F') \geqslant n - \delta_{t'}(u')$ is equivalent by definition to:

```text
(∗) H^i_{ū′}(F̄′) = 0 for i > n − δ_{t′}(u′).
```

Let $DH^{i}_{\bar{u}'}(\bar{F}')$ be the dual of the abelian group $H^{i}_{\bar{u}'}(\bar{F}')$ with respect to
$\mathbb{Z}/m\mathbb{Z}$. By 2.3.2, $K'[-2 \delta_{t'}(u')] = K''$ satisfies $\delta^{K''}(u') = 0$; since $F'$ has
constructible cohomology, one has $DF' = D(\bar{F}')$ and the local duality theorem (SGA 5 I 4.5.3) shows then

<!-- original page 261 -->

that one has

$$
DH^{i}_{\bar{u}'}(\bar{F}') \simeq H^{-i - 2 \delta_{t'}(u')}(DF')_{\bar{u}'}.
$$

So (∗) is equivalent to the relation

```text
(∗∗) (H^q(DF′))_{ū′} = 0 for q > −n − δ_{t′}(u′).
```

We are now in a position to prove the theorem. The relation (ii)\_t is equivalent to the relation (∗∗). Let
$G^{q} = H^{q}(DF')$; the affine Lefschetz theorem (3.1) entails in particular that, for every scheme `U_1` étale over
$U$, affine over $S$, one has

```text
H^p(U′_1, G^q) = 0 for p > δ(G^q),
```

where $\delta(G^{q})$ is the supremum of the $\delta_{t'}(u')$ for the $u'$ such that $(G^{q})_{\bar{u}'} \neq 0$; by
(∗∗) one has $\delta(G^{q}) \leqslant -n - q$, so (ii)\_t entails the relation

```text
H^p(U′_1, H^q(DF′)) = 0 for p > −q − n.
```

Taking the hypercohomology spectral sequence of the functor "sections over $U'_{1}$" with respect to the complex $DF'$:

```text
E_2^{pq} = H^p(U′_1, H^q(DF′)) ⟹ H^{p+q}(U′_1, DF′),
```

one obtains the relation

```text
(∗∗∗) H^i(U′_1, DF′) = 0 for i > −n.
```

<!-- original page 262 -->

Conversely, suppose the preceding relation verified, for every `U_1` étale over $U$, affine over $S$. Apply Proposition
3.6 by replacing $S$ by $\bar{S}$; the hypotheses of 3.6 concerning $S$ are satisfied, since for every scheme `U_1`
étale over $U$, affine, one can find a scheme over `U_1` that comes by inverse image from an étale scheme over $U$
affine over $S$; as for the hypotheses concerning $F$, they are satisfied thanks to 2.3.3. One thus has, for every point
$u'$ of $U'$ such that $(H^{q}(DF'))_{\bar{u}'} \neq 0$:

$$
\delta_{t'}(u') \leqslant -n - q,
$$

which is none other than the relation (∗∗); one has therefore proved the equivalence

$$
(ii)_{t} \Leftrightarrow (\ast\ast\ast).
$$

We are going to transform the relation (∗∗∗); one has first

```text
H^i(U′_1, DF′) = H^i(R f′_{1*}(DF′_1))_{t′};
```

but by (SGA 5 I 1.12), there exists a canonical isomorphism

```text
R f′_{1*}(DF′_1) ≃ D(R^! f′_1(F′_1)),
```

where $D(R^{!} f'_{1}(F'_{1}))$ denotes the dual of $R^{!} f'_{1}(F'_{1})$ with respect to $K$. One sees thus that
(ii)\_t is equivalent to

```text
(H^i(D(R^! f′_1(F′_1))))_{t′} = 0 for i > −n.
```

<!-- original page 263 -->

Applying again the local duality theorem (SGA 5 I 4.5.3), but this time at the point $t'$, one finds

```text
H^i(D(R^! f′_1(F′_1)))_{t′} ≃ D(H^{−i}_{t′}(R^! f′_1(F′_1))),
```

and finally (ii)\_t is equivalent to the relation

```text
H^i_{t′}(R^! f′_1(F′_1)) = 0 for i < n,
```

that is, $prof_{t'}(R^{!} f'_{1}(F'_{1})) \geqslant n$, which completes the proof of the theorem.

**Remark 4.2.3.**

<!-- label: XIV.4.2.3 -->

The reasoning simplifies considerably when one supposes that $S$ admits (at least locally) a dualizing complex (for
example is locally immersible in a regular scheme). This avoids recourse to a completion (the passage to the strictly
local case being immediate), to 2.3.3, and to the rather unpleasant technical statement 3.6, which one can then replace
by the more sympathetic reference 3.7.

**Corollary 4.3.**

<!-- label: XIV.4.3 -->

Let $S$ be an excellent scheme of characteristic zero and $f : U \to S$ a separated morphism of finite type, such that
$U$ is the union of $c + 1$ open sets, affine over $S$. Let $F$ be a complex of sheaves of
$\mathbb{Z}/m\mathbb{Z}$-modules, bounded below with constructible cohomology, $n$ an integer, and $T$ a closed part of
$S$. Suppose that, for every point $u \in U$, one has

$$
prof_{u}(F) \geqslant n - \delta_{T}(u).
$$

Then one has

<!-- original page 264 -->

```text
prof_T(R^! f(F)) ⩾ n − c.
```

Let indeed $U_{j}$, $0 \leqslant j \leqslant c$, be a covering of $U$ by open sets $U_{j}$ affine over $S$. Resuming the
notations of the proof of 4.2, one has, for every $j$,

```text
H^i(U′_j, H^q(DF′)) = 0 for i > −n.
```

Using the spectral sequence relating the cohomology of $U$ to that of the covering formed by the $U_{j}$ (SGA 4 V 2.4),
the preceding relation shows that one has

```text
H^i(U′, H^q(DF′)) = 0 for i > −n + c.
```

The corollary follows from the end of the proof of 4.2.

**Corollary 4.4.**

<!-- label: XIV.4.4 -->

Let $S$ be an excellent scheme of characteristic zero, $g : X \to S$ a morphism, $U$ an open set of $X$, union of
$c + 1$ opens affine over $S$, $Y$ a closed subscheme with underlying space $X - U$, and $j : Y \to X$ the natural
morphism. Let $F$ be a complex of sheaves of $\mathbb{Z}/m\mathbb{Z}$-modules on $X$, bounded below with constructible
cohomology, $T$ a closed part of $S$, and $n$ an integer. Suppose that, for every point $u$ of $U$, one has

$$
prof_{u}(F) \geqslant n - \delta_{T}(u).
$$

Then the canonical morphism

<!-- original page 265 -->

```text
H^i_{g^{−1}(T)!}(X/S, F) → H^i_{(g^{−1}(T) ∩ Y)!}(Y/S, j^* F)
```

is bijective for $i < n - c - 1$, injective for $i = n - c - 1$.

This follows immediately from 4.1 and 4.3.

**Corollary 4.5** (Local Lefschetz theorem).

<!-- label: XIV.4.5 -->

Let $S$ be an excellent henselian local scheme of characteristic zero, $t$ the closed point of $S$, $X$ a scheme proper
over $S' = S - {t}$, and $U$ an open set of $X$, union of $c + 1$ affine opens. Let $Y$ be a closed subscheme of $X$
with underlying space $X - U$, $j : Y \to X$ the canonical morphism, $F$ a complex of sheaves of
$\mathbb{Z}/m\mathbb{Z}$-modules on $X$, bounded below with constructible cohomology, and $n$ an integer. Suppose that,
for every point $u$ of $U$, one has

```text
prof_u(F) ⩾ n − δ_{t′}(u), where δ_{t′}(u) = δ_t(u) − 1.
```

Then the canonical morphism

```text
H^i(X, F) → H^i(Y, j^* F)
```

is bijective for $i < n - c - 1$, injective for $i = n - c - 1$.

Let $f : U \to S$ be the canonical morphism; it follows from 4.2, applied by replacing $n$ by $n + 1$, that one has

```text
prof_t(R^! f(F|_U)) ⩾ n + 1 − c.
```

<!-- original page 266 -->

The preceding relation shows that the canonical morphism

```text
H^i(S, R^! f(F|_U)) → H^i(S′, R^! f(F|_U))
```

is bijective for $i < n - c$, injective for $i = n - c$. Since $R^{!} f(F|_{U})$ is null outside $S'$, one has
$H^{i}(S, R^{!} f(F|_{U})) \simeq H^{i}(R^{!} f(F|_{U}))_{t} = 0$, and consequently

```text
(∗) H^i(S′, R^! f(F|_U)) = 0 for i < n − c.
```

Let $g : X \to S'$, $h : Y \to S'$, $f' : U \to S'$ be the canonical morphisms. It follows from the distinguished
triangle

```text
              R h_*(j^* F)
             ↗            ↘
   R^! f′(F|_U) ←----------- R g_*(F)
```

that condition (∗) is equivalent to the fact that the morphism

```text
H^i(S′, R g_*(F)) → H^i(S′, R h_*(j^* F))
```

is bijective for $i < n - c - 1$, injective for $i = n - c - 1$. Since this morphism is canonically identified with the
morphism

```text
H^i(X, F) → H^i(Y, j^* F),
```

the conclusion follows immediately.

**Corollary 4.6** (Global Lefschetz theorem).

<!-- label: XIV.4.6 -->

<!-- original page 267 -->

Let $S$ be the spectrum of a field, $X$ a scheme proper over $S$, and $U$ an open set of $X$ union of $c + 1$ affine
opens. Let $Y$ be a closed subscheme of $X$ with underlying space $X - U$, $j : Y \to X$ the canonical morphism, $F$ a
complex of sheaves of $\mathbb{Z}/m\mathbb{Z}$-modules on $X$, bounded below with constructible cohomology, and $n$ an
integer. Suppose that, for every point $u$ of $U$, one has

$$
prof_{u}(F) \geqslant n - \dim({u}).
$$

Then the canonical morphism

```text
H^i(X, F) → H^i(Y, j^* F)
```

is bijective for $i < n - c - 1$, injective for $i = n - c - 1$.

More generally, if $g : X \to S$ is a separated morphism of finite type, the hypotheses on $S$, $U$, $Y$, $F$ being the
same as before, then the canonical morphism

```text
H^i_!(X/S, F) → H^i_!(Y/S, j^* F)
```

(where $H^{i}_{!}$ denotes cohomology with proper support, that is, $H^{i}_{!}(X/S, F) = H^{i}(S, R^{!} g(F))$) is
bijective for $i < n - c - 1$, injective for $i = n - c - 1$.

The corollary is a particular case of 4.4, with $T = S$.

Here is a partial converse to 4.3:

**Proposition 4.7.**

<!-- label: XIV.4.7 -->

<!-- original page 268 -->

Let $S$ be a noetherian scheme, $f : U \to S$ a morphism of finite type. Suppose that there exists a dualizing complex
$K$ on $S$ and that $R^{!} f(K)$ is a dualizing complex on $U$. Let $T$ be a closed part of $S$ and $c$ an integer. Then
the following conditions are equivalent:

(i) For every complex of sheaves of $\mathbb{Z}/m\mathbb{Z}$-modules $F$ on $U$, bounded below with constructible
cohomology, and for every integer $n$ such that, for every point $u$ of $U$,

$$
prof_{u}(F) \geqslant n - \delta_{T}(u),
$$

one has

```text
prof_T(R^! f(F)) ⩾ n − c.
```

(ii) For every constructible sheaf of $\mathbb{Z}/m\mathbb{Z}$-modules $G$ on $U$ and for every point $t \in T$, one has

```text
(R^p f_*(G))_t = 0 for p > δ(G, f, t) + c
```

(let us recall from (SGA 4 XIX 6.0) that $\delta(G, f, t) = \sup{\delta_{t}(u) | t \in {u} and G_{u} \neq 0}$).

N.B. Condition (ii) is satisfied by virtue of 3.1 if $f$ is separated and if $U$ is, locally on $S$ for the étale
topology, a union of $c + 1$ opens affine over $S$, so 4.7 contains 4.3.[^XIV-4-1]

One can evidently suppose that $S$ is local and that $T$ is the closed point $t$ of $S$.

<!-- original page 269 -->

The proof of (ii) ⇒ (i) is essentially identical to part 2°) of the proof of 4.2. Let us show briefly that (i) ⇒ (ii).
The local duality theorem (SGA 5 I 4.3.2) applied to `DG` shows that

```text
D H^i_u(DG) ≃ H^{−i − 2 δ_t(u)}(G)_u.
```

Since $G$ is reduced to degree `0`, one therefore has $H^{i}_{u}(DG) = 0$ except perhaps for $i = -2 \delta_{t}(u)$;
more precisely

```text
prof_u(DG) = { −2 δ_t(u)  if G_u ≠ 0,
              { ∞          if G_u = 0.
```

It follows that one has, whatever $u \in U$:

$$
prof_{u}(DG) \geqslant -n - \delta_{t}(u).
$$

<!-- original page 270 -->

It then follows from hypothesis (i) that one has $prof_{t}(R^{!} f(DG)) \geqslant -n - c$. One transforms this relation
using the isomorphism $R^{!} f(DG) \simeq D(R f_{*}(G))$ (SGA 5 I 1.12) and applying the local duality theorem at the
point $t$; one obtains thus

```text
H^i(R f_*(G))_t = 0 for i > n + c,
```

which is none other than (ii).

**4.8.** The hypotheses being those of 4.4 with $g$ proper (resp. 4.5, resp. 4.6 with $g$ proper), if $V$ is an open
neighborhood of $Y$ in $X$, the morphism

```text
H^i(V, F) → H^i(Y, j^* F)
```

is bijective for $i < n - c - 1$, injective for $i = n - c - 1$. If $\iota : V \to X$ is the canonical morphism, it
suffices indeed to see that one applies 4.4 (resp. 4.5, resp. 4.6) to the complex $R \iota_{*}(F|_{V})$. One can ask
whether the preceding morphism is bijective for $i = n - c - 1$, injective for $i = n - c$. It evidently suffices for
the hypotheses to be verified when one replaces $n$ by $n + 1$; the proposition that follows shows that it suffices to
require a little less.

**Proposition 4.9.**

<!-- label: XIV.4.9 -->

Let $S$ be a local excellent scheme of characteristic zero with closed point $t$ (resp. in addition to the preceding
conditions, one supposes $S$ henselian), $f : X \to S$ a scheme proper over $S$ (resp. proper over $S - {t}$), and $U$
an open set of $X$ union of $c + 1$ affine opens. Let $Y$ be a closed subscheme of $X$ with underlying space $X - U$,
$j : Y \to X$ the canonical morphism, $F$ a complex of sheaves of $\mathbb{Z}/m\mathbb{Z}$-modules on $X$, bounded below
with constructible cohomology, and $n$ an integer. Suppose that one has, for every point $u$ of $U$,

```text
prof_u(F) ⩾ inf(n − 1, n − δ_t(u))  (resp. prof_u(F) ⩾ inf(n − 1, n + 1 − δ_t(u))).
```

<!-- original page 271 -->

Then for every open neighborhood $V$ of $Y$ in $X$, the canonical morphism

```text
H^i_{f^{−1}(t)}(V, F) → H^i_{f^{−1}(t) ∩ Y}(Y, j^* F)   (resp. H^i(V, F) → H^i(Y, j^* F))
```

is bijective for $i < n - c - 2$ and injective for $i = n - c - 2$. Moreover, there exists an open neighborhood `V_0` of
$Y$ in $X$ such that, for every other such $V$ with $V \subset V_{0}$, the canonical morphism

```text
H^i_{f^{−1}(t) ∩ V}(V, F) → H^i_{f^{−1}(t) ∩ Y}(Y, j^* F)   (resp. H^i(V, F) → H^i(Y, j^* F))
```

is bijective for $i < n - c - 1$, injective for $i = n - c - 1$.

*Proof.* Let us set, for simplicity, $\delta_{t'}(u) = \delta_{t}(u)$ (resp. $\delta_{t'}(u) = \delta_{t}(u) - 1$). One
deduces from 4.8 the first assertion of 4.9, since the hypotheses of 4.4 (resp. 4.5) are verified when one replaces $n$
by $n - 1$. They are also verified for $n$ itself, except at the points $u$ such that $\delta_{t'}(u) = 0$. Now, for
$u \in U$, to say that $\delta_{t'}(u) = 0$ is equivalent to saying that $u$ is a closed point of $U_{t}$ (resp. a
closed point of $X$). Let $E$ be the set of points of $U$ such that $\delta_{t'}(u) = 0$; let us show that, for all the
points $u \in E$, except a finite number, one has $prof_{u}(F) \geqslant n$. Let $\bar{S}$ be the strict localization of
$S$ at $t$, $S'$ the completion of $\bar{S}$ with closed point $t'$, and consider the cartesian square

```text
U′ --h--> U
|         |
f′        f
|         |
v         v
S′ --g--> S.
```

<!-- original page 272 -->

The depth hypotheses at the points of $U$ are preserved when one replaces $U$ by $U'$ and $F$ by the inverse image $F'$
of $F$ on $U'$. Indeed let $u' \in U'$ and $u = h(u')$. If $u \notin E$, one has the relation
$prof_{u}(F) \geqslant n - \delta_{t'}(u)$, and it follows from 4.2.1 that this entails the relation
$prof_{u'}(F') \geqslant n - \delta_{t'}(u')$. If $u \in E$, $u'$ is a closed point of $U'_{t}$ (resp. a closed point of
$X' = X \times_{S} S'$), and since the fiber $U'_{u}$ of $h$ at $u$ is of dimension zero and $h$ regular, it follows
from 1.16 that one has $prof_{u'}(F') = prof_{u}(F) \geqslant n - 1$.

Let then $K$ be a dualizing complex on $S'$, normalized at the closed point $t'$, and $DF'$ the dual of $F'$ with
respect to $R^{!} f(K)$. By 4.2.2, the étale depth hypotheses at the points of $U'$ translate by the relations:

```text
(H^q(DF′))_{ū′} = 0 for q > −n − δ_{t′}(u′)  (resp. q > −n − 2 − δ_{t′}(u′)),
```

if $u'$ is not a point of $E' = h^{-1}(E)$,

```text
(H^q(DF′))_{ū′} = 0 for q > −(n − 1)  (resp. q > −n − 1), if u′ ∈ E′.
```

Let $G = H^{-(n - 1)}(DF')$ (resp. $G = H^{-n - 1}(DF')$); since $G$ is a constructible sheaf, the set of points at
which the geometric fiber is non-null is a constructible set (SGA 4 IX 2.4 (iv)); now by hypothesis this set is
contained in the set $E'$ of closed points of $U'_{t'}$ (resp. of points of $U'$ closed in $X'$); it therefore follows
from 4.9.1 below that this set reduces to a finite number of points. Applying 4.2.2, one sees that, for all the points
of $E'$ except a finite number, one has $prof_{u'}(F') \geqslant n$. It follows by 1.16 that, for all the points of $E$
except a finite number, one has

<!-- original page 273 -->

$$
prof_{u}(F) \geqslant n.
$$

Let $V$ be an open neighborhood of $Y$ in $X$, contained in the complement in $X$ of the finite set of points $u$ of $E$
for which one has $prof_{u}(F) = n - 1$. If $\iota : V \to X$ is the canonical immersion, let

$$
F_{1} = R \iota_{*}(F|_{V});
$$

then `F_1` is a complex of sheaves on $X$ with constructible cohomology (SGA 4 XIX 5.1) and bounded below. We shall see
that, for every point $u$ of $U$, the complex `F_1` verifies the relation

$$
(\ast)  prof_{u}(F_{1}) \geqslant n - \delta_{t'}(u).
$$

If $u \in U \cap V$, one has $prof_{u}(F_{1}) = prof_{u}(F)$, and the relation (∗) is verified by hypothesis at the
points of $U$ not belonging to $E$; for the latter, it is also verified by the choice of $V$. Finally, if $u \in U$ and
$u \notin V$, one has by 1.6 g) $prof_{u}(F_{1}) = \infty$. One then applies 4.4 (resp. 4.5) replacing $F$ by `F_1`; one
obtains the announced result, taking into account that one has, for every $i$:

```text
H^i_{f^{−1}(t)}(X, R ι_*(F|_V)) ≃ H^i_{f^{−1}(t) ∩ V}(V, F)  (resp. H^i(X, R ι_*(F|_V)) ≃ H^i(V, F)).
```

**Lemma 4.9.1.**

<!-- label: XIV.4.9.1 -->

A constructible set $E$ contained in the set of closed points of a noetherian scheme $X$

<!-- original page 274 -->

is reduced to a finite number of points.

Indeed, $E$ is a finite union of sets of the form $U \cap \complement V$, where $U$ and $V$ are open sets of $X$; by
hypothesis all the points of $U \cap \complement V$ are maximal points of this set, hence they are finite in number.

## 5. Geometrical depth

To apply 4.2 and its corollaries in practice, one needs a convenient criterion to verify the étale-depth hypotheses at
the points of $U$. We shall give such a criterion, using the local Lefschetz theorem 4.5.

**5.1.** Let $A$ be a noetherian local ring; when we speak of the étale depth of $A$, this will mean the depth at the
closed point. We are going to introduce a notion of "geometrical depth of $A$", and use 4.5 to compare it to the étale
depth $prof^{\acute{e}}t(A)$.

**Proposition 5.2.**

<!-- label: XIV.5.2 -->

Let $A$ be a noetherian local ring; suppose that $A$ is isomorphic to a quotient of a regular local ring $B$ by an ideal
$I$ (this is true, for example, when $A$ is complete by virtue of the Cohen theorem (EGA 0_IV 19.8.8)). Let $q$ be the
minimal number of generators of $I$; then the number $\dim(B) - q$ is independent of the choice of $B$.

The minimal number of generators of $I$ is also equal to the rank of the $k$-vector space $I \otimes_{B} k$, where $k$
denotes the residue field of $A$. One reduces immediately to the case where $A$ is complete, since one has
$\hat{A} \simeq \hat{B}/\hat{I}$ with $\dim \hat{B} = \dim B$ and
$rg_{k}(I \otimes_{B} k) = rg_{k}(\hat{I} \otimes_{\hat{B}} k)$; for the same reason one can suppose $B$ complete.

<!-- original page 275 -->

Let $B$ and $B'$ be two complete regular local rings, $f : B \to A$, $f' : B' \to A$ two surjective homomorphisms, and
$I = Ker(f)$, $I' = Ker(f')$. One must show that

```text
dim B − rg_k(I ⊗_B k) = dim B′ − rg_k(I′ ⊗_{B′} k).
```

Let us first place ourselves in the case where one has a factorization of the form

```text
B --f--> A
 \      /
  g    f′
   \  /
    B′
```

with $g$ surjective. Let $J = Ker(g)$; then $J \subset I$ and $I/J = I'$. Since $B'$ is regular,
$\dim(B') = \dim(B) - rg_{k}(J \otimes_{B} k)$ and $J$ is generated by elements forming part of a regular system of
parameters of $B$. It follows that one has the exact sequence

```text
0 → J ⊗_B k → I ⊗_B k → J/I ⊗_{B′} k → 0,
```

and consequently

```text
dim B − rg_k(I ⊗_B k) = dim B − rg_k(J ⊗_B k) − rg_k(J/I ⊗_{B′} k) = dim B′ − rg_k(I′ ⊗_{B′} k).
```

The general case reduces to the preceding; to see this, it suffices to show that one can find a complete regular local
ring $B''$ and surjective homomorphisms $g : B'' \to B$ and $g' : B'' \to B'$, rendering commutative the diagram

<!-- original page 276 -->

```text
                  B
                ↗    ↘ f
              g        \
(∗)      B′′            A
              g′       /
                ↘    ↗ f′
                  B′.
```

Now, if $W$ is a Cohen ring with residue field $k$, one has a local morphism $W \to A$ that lifts to $B$ and $B'$ (EGA
IV 19.8.6), so that one has the commutative diagram

```text
                  B
                ↗
               /
          W              A
               \
                ↘
                  B′.
```

One can find integers $n$ and $n'$ and surjective morphisms $h : W[[T_{1}, \cdots, T_{n}]] \to B$ and
$h' : W[[T'_{1}, \cdots, T'_{n'}]] \to B'$ that are morphisms of $W$-algebras (EGA 0_IV 19.8.8); if one then sets
$B'' = W[[T_{1}, \cdots, T_{n}, T'_{1}, \cdots, T'_{n'}]]$ and if one defines $g$ and $g'$ as morphisms of $W$-algebras
such that

```text
g(T_i) = h(T_i),  g(T′_i) = b_i,  g′(T_i) = b′_i,  g′(T′_i) = h′(T′_i),
```

where $b_{i}$ (resp. $b'_{i}$) is an element of $B$ (resp. of $B'$) lifting $(f' \circ h')(T'_{i})$ (resp.
$(f \circ h)(T_{i})$), the diagram (∗) is indeed commutative.

Proposition 5.2 justifies the following definition:

**Definition 5.3.**

<!-- label: XIV.5.3 -->

<!-- original page 277 -->

Let $A$ be a noetherian local ring, `Â` its completion, which is therefore isomorphic to the quotient of a complete
regular local ring $B$ by an ideal $I$; if $q$ is the minimal number of generators of $I$, one calls geometrical depth
of $A$ the number

```text
prof.géom(A) = dim B − q.
```

**Proposition 5.4.**

<!-- label: XIV.5.4 -->

Let $A$ be a noetherian local ring. Then one has

$$
prof.g\acute{e}om(A) \leqslant \dim A,
$$

and one has equality if and only if $A$ is a complete intersection.

One can suppose $A$ complete. Let then $A = B/I$, where $B$ is a complete regular local ring and $I$ an ideal of $B$. If
$(x_{1}, \cdots, x_{q})$ is a minimal system of generators of $I$, one has $\dim A \geqslant \dim B - q$, and to say
that $\dim A = \dim B - q$ is equivalent to saying that $(x_{1}, \cdots, x_{q})$ forms part of a system of parameters of
$B$ (EGA 0_IV 16.3.7); the proposition follows immediately.

**Proposition 5.5.**

<!-- label: XIV.5.5 -->

Let $A$ and $A'$ be noetherian local rings, $f : A \to A'$ a local homomorphism. Suppose that $f$ is flat and that,
denoting by $k$ the residue field of $A$, $A' \otimes_{A} k$ is a field, a separable extension of $k$. Then one has

$$
prof.g\acute{e}om(A) = prof.g\acute{e}om(A').
$$

<!-- original page 278 -->

By replacing $A$ and $A'$ by their completions, one can suppose $A$ and $A'$ complete (it follows from (EGA 0_III
10.2.1) that the flatness hypothesis is preserved and this is evident for the other hypotheses). Let then $A = B/I$,
where $B$ is a regular local ring and $I$ an ideal of $B$. Since $A'$ is formally smooth over $A$ (EGA 0_IV 19.8.2), it
follows from (EGA 0_IV 19.7.2) that one can find a complete noetherian local ring $B'$ and a local homomorphism
$B \to B'$ such that $B'$ is a flat $B$-module and $B' \otimes_{B} A \simeq A'$. One therefore has $A' \simeq B'/IB'$;
moreover the ring $B'$ is regular; indeed, if $\mathfrak{m}$ is the maximal ideal of $B$, $\mathfrak{m} B'$ is the
maximal ideal of $B'$, and since $\mathfrak{m}$ is generated by a regular sequence by definition of "regular",
$\mathfrak{m} B'$ is generated by a $B'$-regular sequence (EGA 0_IV 15.1.14). Since one evidently has
$\dim B = \dim B'$, and since $I$ and $IB'$ have the same minimal number of generators, the assertion follows.

**Theorem 5.6.**[^N.D.E-XIV-6]

<!-- label: XIV.5.6 -->

Let $A$ be an excellent local ring of characteristic zero. Then one has

$$
prof^{\acute{e}}t(A) \geqslant prof.g\acute{e}om(A).
$$

One can suppose $A$ strictly local complete, since the geometrical depth and the étale depth are preserved by passage to
the strict henselization and to the completion by 5.5 and 1.16. Let $A \simeq B/I$, where $B$ is a complete regular
local ring, and let $(f_{1}, \cdots, f_{q})$ be a minimal system of generators of the ideal $I$. One therefore has

<!-- original page 279 -->

```text
π = prof.géom(A) = dim B − q.
```

Consider the closed immersion

```text
Y = Spec A → X = Spec B,
```

and let $U = X - Y = \bigcup_{1 \leqslant i \leqslant q} X_{f_{i}}$. If $a$ denotes the closed point of $X$, one must
show that, for every prime number $p$, one has

```text
H^i_a(Y, ℤ/pℤ) = 0 for i < π.
```

Since $B$ is regular excellent, one has $prof^{\acute{e}}t(B) = 2 \dim X$ (cf. 1.10) and consequently
$H^{i}_{a}(X, \mathbb{Z}/p\mathbb{Z}) = 0$ for $i < 2 \dim X$. To prove the theorem, it therefore suffices to show that
the morphism

```text
(∗) H^i_a(X, ℤ/pℤ) → H^i_a(Y, ℤ/pℤ)
```

is bijective for $i < \pi$. One applies for this the local Lefschetz theorem 4.5 with $n = \pi + q - 1$, $c = q - 1$, so
$n - c = \pi$. Note that $U = X - Y$ is the union of the $q$ affine opens $X_{f_{i}}$. Let us show that one has, for
every point $u$ of $U$:

```text
prof^ét_u(X) ⩾ π + q − 1 − dim({u}) = dim O_{X,u}
```

(where ${u}$ denotes the closure of $u$ in $X - {a}$). Indeed it follows from 1.10 that one has

```text
prof^ét_u(X) = 2 dim O_{X,u} ⩾ dim O_{X,u}.
```

Using 4.5, one sees that (∗) is bijective for $i < \pi$, which completes the proof

<!-- original page 280 -->

of the theorem.

**Corollary 5.7.**

<!-- label: XIV.5.7 -->

Let $S$ be the spectrum of a field of characteristic zero (resp. an excellent henselian local scheme of characteristic
zero), $f : X \to S$ a scheme proper over $S$ (resp. over $S - {s}$). Let $U$ be a union of $c + 1$ affine opens of $X$,
$Y$ a closed subscheme with underlying space $X - U$, $n$ and $m$ positive integers. Suppose that, for every point $u$
of $U$, one has

$$
prof.g\acute{e}om(O_{X,u}) \geqslant n - \dim({u})
$$

(${u}$ closure of $u$ in $X$). Then the canonical morphism

```text
H^i(X, ℤ/mℤ) → H^i(Y, ℤ/mℤ)
```

is bijective for $i < n - c - 1$, injective for $i = n - c - 1$.

One applies 4.5 and 4.6. The étale-depth hypotheses at the points of $U$ are verified, since by 5.6

```text
prof^ét_u(X) ⩾ prof.géom(O_{X,u}) ⩾ n − dim({u}).
```

## 6. Open questions

**6.1.** One can ask whether the implication (ii) ⇒ (i) of 4.2 is valid more generally for torsion sheaves $F$, not
necessarily annihilated by a given integer $m$

<!-- original page 281 -->

and not necessarily constructible. In the case where $S$ is not of characteristic zero, it seems possible that this
implication remains valid, even for $p$-torsion sheaves ($p$ the residual characteristic). Finally it is not clear
either that the hypothesis $S$ excellent cannot be lifted.

**6.2.** Let $X$ be a scheme proper over a field $k$, or the complement of the closed point of a henselian local scheme,
and $j : Y \to X$ a closed subscheme of $X$ whose complement $U$ is affine. Then, if $F$ is a sheaf of sets on $X$ or a
sheaf of not-necessarily-commutative groups, the statements 4.5 or 4.6 and 4.9 still have a meaning for such an $F$,
provided one restricts to small values of $n$. If $u$ is a point of $U$, one denotes by `ū` a geometric point above $u$,
by $X_{(u)}$ the strict localization of $X$ at `ū`, and by $F_{u}$ the fiber of $F$ at `ū`. Then, by making possibly
certain hypotheses on $X$ and on $F$, for example by supposing $X$ excellent (possibly of characteristic zero, or of
equal characteristic by using resolution of singularities) and $F$ ind-finite (or if needed even $L$-ind-finite with $L$
prime to the characteristic of $X$), one would like to prove the following statements:

a) Let $F$ be a sheaf of sets (resp. a sheaf of groups) and suppose that, for every point $u$ of $U$, one has

```text
F_u → H⁰(X_{(u)} − ū, F)  injective if dim({u}) ⩽ 1
```

(that is, for such a $u$, one has $prof_{u}(F) \geqslant 1$). Then, when $V$ runs over the set

<!-- original page 282 -->

of open neighborhoods of $Y$, the canonical morphism

```text
lim → _V H⁰(V, F) → H⁰(Y, j^* F)
```

is bijective (resp. one has the preceding conclusion and moreover the morphism
$\lim \to {}_{V} H^{1}(V, F) \to H^{1}(Y, j^{*} F)$ is injective). If $F$ is constructible, one can replace the
$\lim \to$ by the cohomology of $V$ for $V$ "small enough".

b) Let $F$ be a sheaf of sets (resp. a sheaf of groups) and suppose that, for every point $u$ of $U$, one has
$prof_{u}(F) \geqslant 2 - \dim({u})$, which translates also by the relations

```text
F_u → H⁰(X_{(u)} − ū, F) is bijective if dim({u}) = 0
F_u → H⁰(X_{(u)} − ū, F) is injective if dim({u}) = 1.
```

Then the canonical morphism

```text
H⁰(X, F) → H⁰(Y, j^* F)
```

is bijective (resp. one has the preceding conclusion and moreover the morphism $H^{1}(X, F) \to H^{1}(Y, j^{*} F)$ is
injective).

c) Let $F$ be an ind-finite sheaf of groups. Suppose that, for every point $u$ of $U$, one has

```text
F_u → H⁰(X_{(u)} − ū, F) bijective if dim({u}) = 0 or 1,
F_u → H⁰(X_{(u)} − ū, F) injective if dim({u}) = 2.
```

Then, when $V$ runs over the set of open neighborhoods of $Y$, the canonical

<!-- original page 283 -->

morphisms

```text
lim → _V H⁰(V, F) → H⁰(Y, j^* F)  and  lim → _V H¹(V, F) → H¹(Y, j^* F)
```

are bijective. If $F$ is constructible, one can replace the $\lim \to$ by the cohomology of $V$ for $V$ small enough.

d) Let $F$ be a sheaf of groups. Suppose that, for every point $u$ of $U$, one has
$prof_{u}(F) \geqslant 3 - \dim({u})$, which translates also by the conditions

```text
F_u → H⁰(X_{(u)} − ū, F) bijective, and H¹(X_{(u)} − ū, F) = 0 if dim({u}) = 0,
F_u → H⁰(X_{(u)} − ū, F) bijective if dim({u}) = 1,
F_u → H⁰(X_{(u)} − ū, F) injective if dim({u}) = 2.
```

Then the canonical morphisms

```text
H⁰(X, F) → H⁰(Y, j^* F)  and  H¹(X, F) → H¹(Y, j^* F)
```

are bijective.

As an indication in favor of these statements[^N.D.E-XIV-7], we mention XIII 2.1, X 3.4 and XII 3.5. Note that, thanks
to the argument of 4.8 and 4.9, statement a) (resp. c)) would follow from b) (resp. d)).

**6.3.** From d) would follow the statement, analogous to 5.6: if $A$ is a noetherian local ring (possibly excellent)
and if $prof.g\acute{e}om(A) \geqslant 3$, then one has

<!-- original page 284 -->

$prof^{hop}(A) \geqslant 3$. To see this, one realizes $Y' = \operatorname{Spec} A$ as a closed subset of a regular
local scheme $X' = \operatorname{Spec} B$, whose complement is a union of $q$ affine opens, with the relation
$\dim B - q = prof.g\acute{e}om(A)$. One has, for every point $x$ of $X'$, if $n = \dim B$,
`prof^{hop}_x(X) ⩾ inf(3, n − dim({x}))` (cf. 1.11), and one deduces from d) that this entails
`prof^{hop}_y(Y′) ⩾ inf(3, n − q − dim({y}))` for every point $y$ of $Y'$. The result is obtained then by taking for $y$
the closed point of $Y'$.

**6.4.** A variant of 4.2, at least of the implication (ii) ⇒ (i), should still be valid in the complex analytic case,
provided one works with "analytically constructible" sheaves (cf. XIII); the proof would be analogous to that of 4.2,
using the duality theory of J.-L. Verdier. Note, on the other hand, that for the complex analytic analogue of the
non-commutative variants signalled in 6.2, one does not even have a method of attack for the statements concerning the
fundamental group suggested by the results of Exposés X, XII, XIII recalled at the end of 6.2. The methods of the
Séminaire indeed seem irremediably tied to the case of finite coverings (which can be studied in terms of coherent
sheaves of algebras).

## Bibliography

1. M. Artin & B. Mazur — "Homotopy of Varieties in Etale Topology", in *Proceedings of a Conference on Local Fields*,
   Springer, 1967.
1. J.-P. Serre — *Cohomologie Galoisienne*, Springer-Verlag, 1964.
1. J.-L. Verdier — *Des catégories dérivées des catégories abéliennes*, with a preface by Luc Illusie, edited by Georges
   Maltsiniotis, Astérisque, vol. 239, Société mathématique de France, Paris, 1996.

## Footnotes

<!--
LEDGER DELTA (Exposé XIV):
| French | English | Note |
| ------ | ------- | ---- |
| schéma (Exp. XIV) | scheme | Modern usage = prescheme of Exp. I–XIII, per Raynaud's footnote. |
| schéma séparé (Exp. XIV) | separated scheme | Modern usage = scheme of Exp. I–XIII. |
| profondeur étale | étale depth | `prof_Y^ét(X)`, `prof_x^ét(X)`. |
| profondeur homotopique | homotopical depth | `prof_Y^{hopL}(X)`, `prof_x^{hopL}(X)`. |
| profondeur géométrique | geometrical depth | `prof.géom(A)`. |
| théorème de Lefschetz affine | affine Lefschetz theorem | 3.1; SGA 4 XIX 6.1 bis. |
| théorème de pureté cohomologique | cohomological purity theorem | 1.10 (semi-purity) and Gabber's absolute purity in N.D.E. |
| théorème de semi-pureté cohomologique | cohomological semi-purity theorem | 1.10. |
| théorème de pureté homotopique | homotopical purity theorem | 1.11. |
| théorème de Lefschetz local / global | local / global Lefschetz theorem | 4.5 / 4.6. |
| rare | rare | "Of empty interior" (Bourbaki TG IX.52); kept as a loanword per N.D.E.-XIV-4. |
| H^i_{Z!}(X/S, F) | H^i_{Z!}(X/S, F) | Cohomology with proper support, support in Z (4.0). |
| ΓY underlined | ℋ^p_Y / RΓ_Y (sheafified) | Convention pinned at 1.0. |
| ind-L-groupes | ind-`L`-groups | Per 1.18, 6.2. |
| 1-asphérique | 1-aspherical | Per 1.18 (SGA 4 XV 1.11). |
| n-acyclique | n-acyclic | Standard. |
| revêtement principal galoisien | Galois principal covering | 1.4 proof. |
| corps strictement local | strictly local field / strictly local ring | 3.2 and surrounding. |
-->

[^XIV-0-1]: After unpublished notes of A. Grothendieck.

[^XIV-1-1]: In accordance with the new terminology (cf. the re-edition of EGA I), we shall here call *scheme* what was
    previously called *prescheme* and *separated scheme* what was called *scheme*.

[^XIV-1-2]: I.e. a "principal homogeneous fiber bundle" in older terminology.

[^N.D.E-XIV-1]: Editors' note: Gabber proved since — in 1994 — the absolute cohomological purity conjecture of
    Grothendieck: if $Y$ is a closed subscheme of absolute noetherian schemes of pure codimension $c$ and $n$ an integer
    invertible on $X$, then $\mathcal{H}^{q}_{Y}(\Lambda)$ is null if $q \neq 2c$ and equals $\Lambda_{Y}(-c)$ (Tate
    twist) otherwise, where one has set $\Lambda = \mathbb{Z}/n\mathbb{Z}$. See (Fujiwara K., "A Proof of the Absolute
    Purity Conjecture (after Gabber)", in *Algebraic geometry 2000, Azumino (Hotaka)*, Adv. Stud. in Pure Math., vol.
    36, 2002, pp. 153-183). For applications to the existence of the dualizing complex, see (SGA 5, Lect. Notes in
    Math., vol. 589, Springer-Verlag, 1977, p. 1672), exposé 1 and loc. cit., §8. This conjecture had been proved in the
    case $n = \ell^{\nu}$ with $\ell$ prime invertible on $X$ sufficiently large by using $K$-theory crucially (Thomason
    R.W., "Absolute cohomological purity", Bull. Soc. Math. France 112 (1984), no. 3, p. 397-406). $K$-theory enters
    Gabber's proof via the Atiyah-Hirzebruch-Thomason spectral sequence relating étale cohomology and $K$-theory, a
    method already used in Thomason's approach. Besides this result, the other fundamental argument is the
    generalization of the Lefschetz theorem cited in note (5), page 181.

[^N.D.E-XIV-2]: Editors' note: recently, de Jong and Oort have obtained the following purity statement: let
    $\tilde{S} \to S$ be a resolution of singularities of the spectrum $S$ of a normal noetherian local ring of
    dimension 2 and let $U$ be the complement of the closed point $s$ in $S$. Suppose moreover that $k(s)$ is
    algebraically closed. Then, for every prime number $p$, in particular if $S$ is of characteristic $p$, the
    restriction morphism $H^{1}_{\acute{e}}t(\tilde{S}, \mathbb{Q}_{p}) \to H^{1}_{\acute{e}}t(U, \mathbb{Q}_{p})$ is
    bijective (de Jong A.J. & Oort F, "Purity of the stratification by Newton polygons", J. Amer. Math. Soc. 13 (2000),
    no. 1, p. 209-241, theorem 3.2). If $k = \mathbb{C}$ and $A$ is the completion of a surface singularity, this result
    is due to Mumford (see page 158, [5]).

[^N.D.E-XIV-3]: Editors' note: the trivial torsor is successively denoted `0` or `1` in what follows; we have left this
    double notation, which, on reflection, brings no ambiguity.

[^N.D.E-XIV-4]: Editors' note: "rare" = "of empty interior", cf. Bourbaki TG IX.52.

[^N.D.E-XIV-5]: Editors' note: Gabber has proved the following generalization. Let $Y$ be a strictly local scheme of
    arithmetic type over a regular noetherian scheme $S$ of dimension $\leqslant 1$. Let $f : X \to Y$ be an affine
    morphism of finite type, $\Lambda = \mathbb{Z}/n\mathbb{Z}$ with $n$ invertible on $X$ and $F$ a $\Lambda$-sheaf.
    Then $H^{q}(X, F) = 0$ if $q > \delta(F)$. From this one deduces the following local Lefschetz theorem. Let $O$ be
    strictly local of arithmetic type over $S$. For every $f \in O$ not a zero divisor and every $\Lambda$-sheaf $F$ on
    $\operatorname{Spec}(O[f^{-1}])$, one has $H^{q}(\operatorname{Spec}(O[f^{-1}]), F) = 0$ for $q > \dim(O)$. Cf.
    (Fujiwara K., "A Proof of the Absolute Purity Conjecture (after Gabber)", in *Algebraic geometry 2000, Azumino
    (Hotaka)*, Adv. Stud. in Pure Math., vol. 36, 2002, p. 153-183, §5) and especially the article of Illusie (Illusie
    L., "Perversité et variation", Manuscripta Math. 112 (2003), p. 271-295). This result is one of the crucial points
    used by Gabber in his proof of the Grothendieck purity theorem (cf. note (1), page 168).

[^XIV-4-1]: At least in the case where $S$ admits locally a dualizing complex, for example $S$ locally immersible in a
    regular scheme.

[^N.D.E-XIV-6]: Editors' note: Illusie has since shown the inequality
    $prof_{x}(\mathbb{Z}/\ell^{\nu} \mathbb{Z}) \geqslant prof.g\acute{e}om_{x}(X/S) - \delta(x) + 1$ for $x$ a point of
    $X$ a scheme of finite type over a trait $S$ of residual characteristic prime to $\ell$, and $\nu \geqslant 1$. If
    $S$ is of characteristic zero, this is a consequence of theorem 5.6; see (Illusie L., "Perversité et variation",
    Manuscripta Math. 112 (2003), p. 271-295).

[^N.D.E-XIV-7]: Editors' note: all the statements of 6.2, apart from the constructible variants, have been proved by Mme
    Raynaud; see (Raynaud M., "Théorèmes de Lefschetz en cohomologie des faisceaux cohérents et en cohomologie étale.
    Application au groupe fondamental", Ann. Sci. Éc. Norm. Sup. (4) 7 (1974), p. 29-52, corollary III.1.3).


<!-- SOURCE: README.md -->

# SGA 2: Local Cohomology of Coherent Sheaves and Local and Global Lefschetz Theorems

*Séminaire de Géométrie Algébrique du Bois-Marie*, 1962.

A. Grothendieck (with collaborators I. Giorgiutti, J. Giraud, M. Hakim *née* Jaffe, A. Laudal). Augmented by Exposé XIV
of Mme Michèle Raynaud (1967). Revised reprint, IHÉS, Bures-sur-Yvette, April 1968. Modern LaTeX edition by Yves Laszlo
*et al.* (2005).

## Abstract

This volume develops the theory of local cohomology of coherent sheaves on noetherian schemes and applies it to prove
local and global theorems of Lefschetz type — for the fundamental group, the Picard group, and projective algebraic
schemes — through a systematic interplay between local results and global ones. Exposés I–II set up the formalism of
cohomology with supports $H^{i}_{Y}(X, F)$; III relates it to the classical notion of depth; IV–V develop local duality
and dualizing modules in the style later subsumed by Hartshorne's *Residues and Duality*; VI–VIII prove the central
finiteness theorem for $H^{i}_{Y}(F)$; IX uses it to obtain comparison and existence theorems in formal geometry,
parallel to those of EGA III for proper morphisms; X–XII apply these to Lefschetz-type theorems for $\pi_{1}$, `Pic`,
and projective schemes; XIII surveys open problems; and Raynaud's XIV recasts the Lefschetz theorems in étale
cohomology, drawing on SGA 4 and SGA 5.

## Reading order

Files are numbered so alphanumeric order matches reading order.

- [Title page, preface (Laszlo), and table of contents](00-title-preface.md)
- [Introduction (Grothendieck, 1968)](00-introduction.md)
- [Exposé I — Global and local cohomological invariants with respect to a closed subspace](01-invariants-cohomologiques.md)
- [Exposé II — Application to quasi-coherent sheaves on preschemes](02-faisceaux-quasi-coherents.md)
- [Exposé III — Cohomological invariants and depth](03-invariants-cohomologiques-et-profondeur.md)
- [Exposé IV — Dualizing modules and dualizing functors](04-modules-et-foncteurs-dualisants.md)
- [Exposé V — Local duality and the structure of the $H^{i}(M)$](05-dualite-locale-et-structure-des-Hi.md)
- [Exposé VI — The functors $Ext^{\bullet}_{Z}(X; F, G)$ and $Ext^{\bullet}_{Z}(F, G)$](06-foncteurs-Ext.md)
- [Exposé VII — Vanishing criteria and coherence conditions for the sheaves $Ext^{i}_{Y}(F, G)$](07-criteres-de-nullite-coherence.md)
- [Exposé VIII — The finiteness theorem](08-theoreme-de-finitude.md)
- [Exposé IX — Algebraic geometry and formal geometry](09-geometrie-algebrique-et-formelle.md)
- [Exposé X — Application to the fundamental group](10-application-au-groupe-fondamental.md)
- [Exposé XI — Application to the Picard group](11-application-au-groupe-de-picard.md)
- [Exposé XII — Applications to projective algebraic schemes](12-schemas-algebriques-projectifs.md)
- [Exposé XIII — Problems and conjectures](13-problemes-et-conjectures.md)
- [Exposé XIV — Depth and Lefschetz theorems in étale cohomology (Raynaud)](14-profondeur-lefschetz-cohomologie-etale.md)
- [Index of notation](zz-index-notations.md)
- [Terminological index](zz-index-terminologique.md)
- [Translation glossary](glossary.md)

## Reference convention

Following the source, SGA 2 is cited as `(Exp. N, M.K)` where $N$ is the Exposé Roman numeral and `M.K` is the decimal
numbering inside that Exposé — for example `(VIII, 2.3)` for Théorème 2.3 of Exposé VIII. The 1968 revised reprint
introduced a uniform decimal numbering across Exposés III–VIII; the original 1962 numbering is occasionally preserved
with the adverb *bis* where collisions occurred. Cross-references to other SGA volumes follow the same source
conventions (e.g. `SGA 4 IV 3.8`).

## Editorial conventions

- **Terminology**. Exposés I–XIII keep the historical SGA/EGA distinction between *prescheme* (`préschéma`) and *scheme*
  (`schéma`, in the older sense of separated prescheme). Exposé XIV, added in 1967 by Raynaud, explicitly adopts the
  modern usage in which *scheme* means what was previously called *prescheme*, and *separated scheme* means what was
  previously called *scheme*; her opening footnote announces this. The translation honors that per-Exposé split; a
  Editorial note at the head of Exposé XIV recalls it.

- **Editor footnotes (N.D.E.)**. The 2005 LaTeX edition by Yves Laszlo *et al.* added footnotes (*Notes de l'éditeur*,
  abbreviated *N.D.E.*) recording corrections, updates, and the current status of questions raised in the original. In
  this translation, original Grothendieck-era footnotes use slugs like $[{}^{I}-3-1]$, while editor footnotes use
  $[{}^{N}.D.E-IV-2]$ so the two are visibly distinct.

- **Page marks**. HTML comments `<!-- original page N -->` mark the start of page $N$ in the 1968 IHÉS edition, whose
  pagination is preserved in the margin of the modern LaTeX edition.

- **Mathematics**. Mathematics is written with Unicode and wrapped in backticks where formatter mangling is a risk.
  Displayed equations use fenced ```` ```text ```` blocks, optionally pinned with `<!-- label: eq:N.X.Y -->`.

- **The $\Gamma Z$ / $\Gamma_{Z}$ distinction**. SGA 2 systematically uses an underlined $\Gamma Z$ for the *sheafified*
  version of the sections-with-support functor and a non-underlined $\Gamma_{Z}$ for the global-section version. The
  translation preserves this; where the source OCR has lost the underline, the surrounding French reveals which functor
  is meant. A small typographic note at first use in each Exposé fixes the convention there.

## Provenance

This is a translation, not a critical edition. The authoritative text remains the French 2005 LaTeX edition, derived
from the IHÉS/North-Holland 1968 reprint as recomposed by Y. Laszlo. For any claim that matters mathematically, consult
the source: this English version exists to make the volume readable, not to replace it.


<!-- SOURCE: glossary.md -->

# Glossary and Translation Ledger — SGA 2

This file records the translation choices made for the SGA 2 Markdown translation. It is the authoritative reference for
the parallel translators of individual Exposés; every translator must consult it before drafting and must obey it where
it applies.

## Core terminology

| French                                     | English                                       | Note                                                                                                                                              |
| ------------------------------------------ | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| préschéma                                  | prescheme                                     | Historical SGA/EGA term. Used through Exposés I–XIII. *Not* silently modernized.                                                                  |
| schéma                                     | scheme                                        | In Exposés I–XIII, denotes a separated prescheme. In Exposé XIV, the modern meaning (= prescheme of Exp. I–XIII), per Raynaud's opening footnote. |
| schéma séparé (Exp. XIV)                   | separated scheme                              | Raynaud's modern terminology in Exposé XIV.                                                                                                       |
| faisceau                                   | sheaf                                         | Standard.                                                                                                                                         |
| faisceau (quasi-)cohérent                  | (quasi-)coherent sheaf                        | Standard.                                                                                                                                         |
| espace annelé                              | ringed space                                  | Standard.                                                                                                                                         |
| espace topologique                         | topological space                             | Standard.                                                                                                                                         |
| application                                | map                                           | "Function" only in elementary set-theoretic contexts.                                                                                             |
| morphisme                                  | morphism                                      | Standard.                                                                                                                                         |
| morphisme étale / lisse / plat / propre    | étale / smooth / flat / proper morphism       | Standard; matches SGA 1 glossary.                                                                                                                 |
| revêtement étale                           | étale covering                                | Per SGA 1 glossary.                                                                                                                               |
| immersion / immersion fermée / ouverte     | immersion / closed immersion / open immersion | Standard.                                                                                                                                         |
| ouvert / fermé / localement fermé          | open / closed / locally closed                | Standard.                                                                                                                                         |
| voisinage                                  | neighborhood                                  | American spelling.                                                                                                                                |
| recouvrement                               | covering                                      | "Cover" only in casual prose.                                                                                                                     |
| corps                                      | field                                         | False friend: not "body".                                                                                                                         |
| anneau                                     | ring                                          | Commutative by SGA convention unless stated.                                                                                                      |
| anneau local (noethérien)                  | (noetherian) local ring                       | Standard.                                                                                                                                         |
| anneau local régulier                      | regular local ring                            | Standard.                                                                                                                                         |
| corps résiduel                             | residue field                                 | Denoted $\kappa(x)$ or $\kappa(A)$ (per SGA 1).                                                                                                   |
| module de type fini                        | finitely generated module                     | "Of finite type" if matching adjacent SGA 1 prose.                                                                                                |
| de type fini (morphisme, présentation)     | of finite type                                | Morphism-level terminology, EGA-standard.                                                                                                         |
| catégorie                                  | category                                      | Standard.                                                                                                                                         |
| foncteur / foncteur dérivé                 | functor / derived functor                     | Standard.                                                                                                                                         |
| foncteur exact / exact à gauche / à droite | exact / left exact / right exact functor      | Standard.                                                                                                                                         |
| sous-foncteur                              | subfunctor                                    | Standard.                                                                                                                                         |
| catégorie dérivée $D^{+}(X)$               | derived category $D^{+}(X)$                   | Used principally in Exposé XIV.                                                                                                                   |
| catégorie abélienne                        | abelian category                              | Standard.                                                                                                                                         |
| limite projective / inductive              | inverse / direct limit                        | Modern English. Flag the SGA-era usage in a Editorial note on first occurrence per Exposé.                                                       |
| fibre                                      | fiber                                         | American spelling.                                                                                                                                |
| spécialisation                             | specialization                                | American spelling.                                                                                                                                |
| canonique                                  | canonical                                     | Do *not* translate as "natural" unless the source specifically appeals to naturality.                                                             |
| fonctoriel                                 | functorial                                    | Standard.                                                                                                                                         |
| naturel                                    | natural                                       | Reserve for genuine naturality.                                                                                                                   |
| à isomorphisme près                        | up to isomorphism                             | Standard.                                                                                                                                         |
| nécessaire et suffisant                    | necessary and sufficient                      | Sometimes "if and only if" in theorem statements.                                                                                                 |
| si et seulement si                         | if and only if                                | "Iff" only if local idiom permits.                                                                                                                |

## SGA 2 topics

| French                                                      | English                                                                                                                    | Note                                                                                                                                                 |
| ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| cohomologie locale                                          | local cohomology                                                                                                           | Title-level. Not "cohomology locally".                                                                                                               |
| cohomologie à support dans Y                                | cohomology with supports in Y                                                                                              | Match the SGA 1 phrasing.                                                                                                                            |
| $H^{i}_{Y}(X, F)$ (sections with support)                   | $H^{i}_{Y}(X, F)$                                                                                                          | Global, non-underlined.                                                                                                                              |
| $\mathcal{H}^{i}_{Y}(F)$ (sheafified, underlined in source) | $\mathcal{H}^{i}_{Y}(F)$                                                                                                   | Use the script-H Unicode $\mathcal{H}$ to mark the sheafified functor. Where OCR drops the underline, the surrounding French reveals which is meant. |
| $\Gamma_{Z}$ (global sections with support in $Z$)          | $\Gamma_{Z}$                                                                                                               | Global, non-underlined functor.                                                                                                                      |
| $\Gamma Z$ underlined (sheafified)                          | $\Gamma_{Z}$ (sheafified) — render as $\Gamma Z$ or $\Gamma_{Z}$ with a one-line typographic note at first use per Exposé. | The translator should pin the convention at first use in each Exposé.                                                                                |
| sorite                                                      | sorites                                                                                                                    | Loanword, kept (per SGA 1).                                                                                                                          |
| dévissage                                                   | dévissage                                                                                                                  | Loanword, kept.                                                                                                                                      |
| Hartogs (phénomène de —)                                    | Hartogs phenomenon                                                                                                         | Standard.                                                                                                                                            |
| profondeur                                                  | depth                                                                                                                      | Standard.                                                                                                                                            |
| profondeur cohomologique                                    | cohomological depth                                                                                                        | Per source index.                                                                                                                                    |
| profondeur étale                                            | étale depth                                                                                                                | Per source index.                                                                                                                                    |
| profondeur homotopique                                      | homotopical depth                                                                                                          | Per source index.                                                                                                                                    |
| profondeur homotopique rectifiée                            | rectified homotopical depth                                                                                                | Per source index.                                                                                                                                    |
| profondeur géométrique                                      | geometrical depth                                                                                                          | Per source index. ("Geometrical" with -ical, as the index uses it.)                                                                                  |
| $M$-régulier                                                | $M$-regular                                                                                                                | For sequences regular on $M$.                                                                                                                        |
| anneau de Cohen-Macaulay                                    | Cohen-Macaulay ring                                                                                                        | Standard.                                                                                                                                            |
| théorème de comparaison                                     | comparison theorem                                                                                                         | Per source index.                                                                                                                                    |
| théorème d'existence                                        | existence theorem                                                                                                          | Per source index.                                                                                                                                    |
| théorème de finitude                                        | finiteness theorem                                                                                                         | Per source index.                                                                                                                                    |
| théorème de dualité (locale / projective)                   | (local / projective) duality theorem                                                                                       | Per source index.                                                                                                                                    |
| théorème d'excision                                         | excision theorem                                                                                                           | Per source index.                                                                                                                                    |
| module dualisant / foncteur dualisant                       | dualizing module / dualizing functor                                                                                       | Per source index.                                                                                                                                    |
| enveloppe injective                                         | injective envelope                                                                                                         | Per source index.                                                                                                                                    |
| extension essentielle                                       | essential extension                                                                                                        | Per source index.                                                                                                                                    |
| forme résidu                                                | residue form                                                                                                               | Per source index.                                                                                                                                    |
| résolution injective / projective                           | injective / projective resolution                                                                                          | Standard.                                                                                                                                            |
| résolution flasque                                          | flasque (flabby) resolution                                                                                                | Use "flasque" (the SGA term) inline; "flabby" only if the local prose already uses it.                                                               |
| faisceau flasque                                            | flasque sheaf                                                                                                              | Per SGA usage.                                                                                                                                       |
| faisceau mou / fin                                          | soft / fine sheaf                                                                                                          | Less common in SGA 2; if encountered, use these renderings.                                                                                          |
| suite spectrale                                             | spectral sequence                                                                                                          | Standard.                                                                                                                                            |
| terme initial / aboutissement                               | initial term / abutment                                                                                                    | Standard.                                                                                                                                            |
| homomorphisme de Gysin                                      | Gysin homomorphism                                                                                                         | Per source index.                                                                                                                                    |
| théorème de pureté de Zariski-Nagata                        | Zariski-Nagata purity theorem                                                                                              | Per source index.                                                                                                                                    |
| théorème de pureté cohomologique                            | cohomological purity theorem                                                                                               | Per source index.                                                                                                                                    |
| théorème de semi-pureté cohomologique                       | cohomological semi-purity theorem                                                                                          | Per source index.                                                                                                                                    |
| couple parafactoriel de préschémas                          | parafactorial pair of preschemes                                                                                           | Per source index. ("Pair" preserves the *couple* sense.)                                                                                             |
| anneau local parafactoriel                                  | parafactorial local ring                                                                                                   | Per source index.                                                                                                                                    |
| anneau local pur                                            | pure local ring                                                                                                            | Per source index.                                                                                                                                    |
| couple pur de préschémas                                    | pure pair of preschemes                                                                                                    | Per source index.                                                                                                                                    |
| géométriquement factoriel / parafactoriel                   | geometrically factorial / parafactorial                                                                                    | Per source index.                                                                                                                                    |
| anneau strictement local                                    | strictly local ring                                                                                                        | Per source index.                                                                                                                                    |
| condition de Lefschetz                                      | Lefschetz condition                                                                                                        | Per source index.                                                                                                                                    |
| condition de Lefschetz effective                            | effective Lefschetz condition                                                                                              | Per source index.                                                                                                                                    |
| théorème de Lefschetz affine                                | affine Lefschetz theorem                                                                                                   | Per source index.                                                                                                                                    |
| théorèmes de Lefschetz (du type —)                          | Lefschetz-type theorems / Lefschetz theorems                                                                               | Either rendering, depending on rhythm.                                                                                                               |
| groupes d'homotopie locale                                  | local homotopy groups                                                                                                      | Per source index.                                                                                                                                    |
| platitude normale                                           | normal flatness                                                                                                            | Standard.                                                                                                                                            |
| complétion formelle                                         | formal completion                                                                                                          | Standard.                                                                                                                                            |
| complété formel (de $X$ le long de $Y$)                     | formal completion (of $X$ along $Y$)                                                                                       | Standard; the hat $\hat{X}$ notation is preserved.                                                                                                   |
| section hyperplane                                          | hyperplane section                                                                                                         | Standard.                                                                                                                                            |
| schéma algébrique projectif                                 | projective algebraic scheme                                                                                                | Title-level for Exposé XII.                                                                                                                          |
| théorème de représentabilité de Brown                       | Brown's representability theorem                                                                                           | If cited in N.D.E. footnotes.                                                                                                                        |
| Tôhoku                                                      | *Tôhoku*                                                                                                                   | Cite as the journal/article; italicize.                                                                                                              |

## Proof movement

These follow $references/french-math-idiom.md$ of the translation skill, with SGA-specific tweaks.

| French                                | English                                         | Note                                                                           |
| ------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------ |
| Soit / Soient X / X et Y              | Let X / X and Y be                              | Match singular / plural.                                                       |
| Supposons (que)                       | Suppose (that) / Assume                         | "Assume" if the sentence is a hypothesis register.                             |
| Posons                                | Set / Put                                       | "Put" for variable assignments; "Set" for ad-hoc definitions.                  |
| Notons                                | Denote / Write / Note                           | Choose by what follows; *Notons que* is "Note that".                           |
| On a                                  | We have                                         | Not "one has" except for register.                                             |
| On en déduit                          | We deduce                                       | "It follows" if the inference is non-trivial.                                  |
| Montrons (que)                        | We show (that)                                  | "It remains to show" if it closes a reduction.                                 |
| Il suffit de                          | It suffices to                                  | Standard.                                                                      |
| Il reste à montrer                    | It remains to show                              | Standard.                                                                      |
| Il en résulte (que) / Il résulte (de) | It follows (that) / It follows (from)           | Choose by structure; "hence" in compact proof prose.                           |
| Par suite                             | Consequently / hence                            | Avoid "as a result of this".                                                   |
| D'où                                  | Hence / whence                                  | "Whence" only if register supports it.                                         |
| En effet                              | Indeed                                          | Standard introduces a justification.                                           |
| Or                                    | Now                                             | Pivot conjunction; "but" only if the sentence really contrasts.                |
| Donc                                  | Thus / hence / so                               | Choose by rhythm.                                                              |
| D'une part … d'autre part             | On the one hand … on the other hand             | Keep both clauses.                                                             |
| Cela achève la démonstration          | This completes the proof                        | Standard.                                                                      |
| CQFD                                  | QED                                             | Or "This proves the claim."                                                    |
| à savoir                              | namely                                          | Standard.                                                                      |
| compte tenu de                        | taking into account / in view of                | Choose by clause weight.                                                       |
| en vertu de                           | by virtue of / by                               | "By" usually suffices.                                                         |
| moyennant                             | by means of / using                             | Standard.                                                                      |
| quitte à                              | (possibly) by … / replacing X by Y if necessary | A standard French move; "replacing X by Y if necessary" reads best in English. |
| à condition que                       | provided that                                   | Standard.                                                                      |
| dès que                               | as soon as                                      | Standard.                                                                      |
| chaque fois que                       | whenever                                        | Standard.                                                                      |

## Modality and certainty

Preserve modality exactly; do *not* upgrade certainty.

| French                               | English                                  |
| ------------------------------------ | ---------------------------------------- |
| il est clair que                     | it is clear that                         |
| il est évident que                   | it is evident that                       |
| manifestement / il est manifeste que | manifestly / it is manifest that         |
| il semble que                        | it seems that                            |
| on s'attend à ce que                 | one expects that                         |
| il est probable que                  | it is probable that                      |
| sans doute                           | doubtless / probably (context-dependent) |
| conjecturalement                     | conjecturally                            |
| il y a tout lieu de penser que       | there is every reason to think that      |
| on peut conjecturer                  | one may conjecture                       |
| il n'est pas exclu que               | it is not excluded that                  |
| il se peut que                       | it may be that                           |
| vraisemblablement                    | presumably                               |

## Common OCR repairs

These recur across the source files. Apply them locally as the translator reads each block; do not silently "correct"
the mathematics — only repair what the OCR clearly mangled, and flag anything genuinely ambiguous with a
`<!-- Editorial note: ... -->` comment.

- **Dropped sub/superscripts on big operators.** $\Gamma$, $H^{i}$, $Ext^{i}$, $R^{i} f_{*}$, `O_X`, $H^{\bullet}$,
  $H_{\bullet}$ routinely lose their indices. The surrounding French sentence almost always names them ("la cohomologie
  locale de F le long de Y", "les $H^{i}$ de F", etc.); recover from context.
- **Underline loss on sheafified functors.** SGA 2 distinguishes $\Gamma Z$ (the global section functor —
  non-underlined) from $\Gamma Z$ (the sheafified functor — underlined). The OCR routinely loses the underline. In the
  translation, render the sheafified functor with a script-H $\mathcal{H}$ for the cohomology version
  ($\mathcal{H}^{i}_{Y}(F)$) and keep an explicit $\Gamma Z$ for the underlined section functor, pinning the convention
  at first use per Exposé with a small note.
- **Hat across line break.** Formal-completion hats break across lines: $Et( b / X)$ is $\hat{E}t(\hat{X})$. `X b` after
  a closing paren is $\hat{X}$. Repair as needed.
- **OCR substitutions for arrows.**
    - $7\to$ is $\mapsto$.
    - $-\to$ is $\to$.
    - $\sim=$ (often broken across lines) is $\cong$.
    - `\sim\n\to` (OCR artefact, with literal newline) is $\xrightarrow{\sim}$ or $\to$ annotated with `~`; pick the
      rendering that matches what is being claimed.
- **OCR substitutions for accents.**
    - $Et(X)$ should be $\hat{E}t(X)$ (the étale site / category of étale objects).
    - `etale` should be `étale`.
    - `Tohoku` should be *Tôhoku*.
- **Greek subscripts.** $\pi 1$, $\pi 0$, `H1`, `H0` etc. should be $\pi_{1}$, $\pi_{0}$, $H^{1}$, $H^{0}$ etc.
  (Unicode), inside backticks.
- **Math run-ons.** When a displayed equation has been broken into prose by the OCR, restore it as a fenced
  ```` ```text ```` block. - **Embedded N.D.E. footnotes.** Source convention is $(N) N.D.E. : <text>$ at the bottom of
  a page. Recover the whole footnote (which may span lines) and render it as $[{}^{N}.D.E-N]$ (or
  $[{}^{N}.D.E-<expose>-<n>]$ if multiple Exposés might collide) with its English translation in the footnote body. -
  **Dash lead-ins.** Statement bodies preceded by `—` in the source (after `Proposition X.Y.`,
  $Th\acute{e}or\grave{e}me X.Y.$, etc.) are rendered SGA 1-style: bold keyword on its own line, then a paragraph break,
  then the body.

## Cross-Exposé additions (discovered during translation)

Consolidated from the per-Exposé ledger deltas appended at the foot of each translation file. Refer to that file for the
original context. New cross-cutting terms encountered during translation:

| French                                            | English                                                 | Note                                                                      |
| ------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------- |
| sous-faisceau                                     | subsheaf                                                | Standard.                                                                 |
| extension par 0 (en dehors de Z)                  | extension by 0 (outside Z)                              | Standard for $j_{!}$ constructions.                                       |
| famille de supports (au sens de Cartan)           | family of supports (in Cartan's sense)                  | Kept verbatim from the source.                                            |
| à support dans Z                                  | with support in Z                                       | Standard.                                                                 |
| faisceautiser                                     | "sheafify"                                              | In quotes when the source treats it as a coinage.                         |
| par abus de langage                               | by abuse of language                                    | Standard.                                                                 |
| à valeurs dans                                    | with values in                                          | Standard.                                                                 |
| aboutissement                                     | abutment                                                | Of a spectral sequence.                                                   |
| terme initial                                     | initial term                                            | Of a spectral sequence.                                                   |
| immersion canonique                               | canonical immersion                                     | Standard.                                                                 |
| partie localement fermée                          | locally closed subset                                   | Standard.                                                                 |
| suite exacte de cohomologie relative              | exact sequence of relative cohomology                   | Standard.                                                                 |
| $\partial$-foncteur / $\delta$-foncteur           | $\partial$-functor / $\delta$-functor                   | Preserve Grothendieck's distinction.                                      |
| foncteur cohomologique universel                  | universal cohomological functor                         | Standard.                                                                 |
| système projectif essentiellement nul             | essentially zero projective system                      | Standard SGA terminology.                                                 |
| opérateur bord                                    | boundary operator                                       | Standard.                                                                 |
| cohomologie de Koszul / complexe de Koszul        | Koszul cohomology / Koszul complex                      | Standard.                                                                 |
| `Module`, `Idéal`, `Algèbre` (capitalised)        | `Module`, `Ideal`, `Algebra` (capitalised)              | Per SGA convention for sheaves of modules/ideals/algebras. Preserve case. |
| annulateur                                        | annihilator                                             | Standard.                                                                 |
| assassin de M                                     | "assassin of $M$"                                       | Bourbaki idiom; kept in quotes with explanatory gloss.                    |
| racine de $a$                                     | radical of $a$                                          | Symbol $r(a)$ preserved.                                                  |
| $M$-régulier (élément, suite)                     | $M$-regular (element, sequence)                         | Per glossary; matches the depth taxonomy.                                 |
| homothétie de rapport $a$                         | multiplication by $a$                                   | "Homothety of ratio" is unidiomatic in module-theoretic prose.            |
| suite régulière                                   | regular sequence                                        | Standard.                                                                 |
| anneau semi-local                                 | semi-local ring                                         | Standard.                                                                 |
| codimension homologique ($codh_{A} M$)            | homological codimension ($codh_{A} M$)                  | Older terminology for depth; symbol preserved.                            |
| platitude / fidèlement plat                       | flatness / faithfully flat                              | Standard.                                                                 |
| antifiltre                                        | antifilter                                              | Order-theoretic loanword.                                                 |
| chaîne (condition des chaînes)                    | chain (chain condition)                                 | Standard.                                                                 |
| connexe en codimension $d - 1$                    | connected in codimension $d - 1$                        | Standard.                                                                 |
| ensemblistement                                   | set-theoretically                                       | Standard.                                                                 |
| intersection complète (absolue)                   | (absolute) complete intersection                        | Standard.                                                                 |
| image directe supérieure                          | higher direct image                                     | $R^{i} f_{*}$ notation preserved.                                         |
| Module gradué                                     | graded Module                                           | Capital preserved per SGA convention.                                     |
| modules gradués                                   | graded modules                                          | Lowercase when context is module-level, not sheaf-of-modules.             |
| résolution injective                              | injective resolution                                    | Standard.                                                                 |
| augmentation canonique                            | canonical augmentation                                  | Standard.                                                                 |
| homotopes à zéro                                  | homotopic to zero                                       | Standard.                                                                 |
| accouplement                                      | pairing                                                 | Standard.                                                                 |
| théorème des syzygies                             | syzygy theorem                                          | Hilbert's syzygy theorem.                                                 |
| théorème de Cohen                                 | Cohen's theorem                                         | Structure theorem for complete local rings.                               |
| dimension homologique globale                     | global homological dimension                            | Standard.                                                                 |
| système de paramètres                             | system of parameters                                    | Standard.                                                                 |
| composantes irréductibles                         | irreducible components                                  | Standard.                                                                 |
| point générique                                   | generic point                                           | Standard.                                                                 |
| morphisme déduit de $f$ par passage aux complétés | morphism deduced from $f$ by passing to the completions | Standard SGA proof movement.                                              |
| idéal de définition                               | ideal of definition                                     | Standard.                                                                 |
| $I'$-bonne (filtration)                           | $I'$-good (filtration)                                  | EGA terminology for "good filtration".                                    |
| morphisme adique                                  | adic morphism                                           | Standard EGA term.                                                        |
| condition de Mittag-Leffler uniforme              | uniform Mittag-Leffler condition                        | Standard.                                                                 |
| préschéma formel                                  | formal prescheme                                        | Standard.                                                                 |
| anneau noethérien adique                          | noetherian adic ring                                    | Standard.                                                                 |
| séparé et complet pour la topologie $I$-adique    | separated and complete for the $I$-adic topology        | Standard.                                                                 |
| anneau gradué associé $gr_{I}$                    | associated graded ring $gr_{I}$                         | Standard.                                                                 |
| Module inversible                                 | invertible Module                                       | Capital preserved per source.                                             |
| pleinement fidèle                                 | fully faithful                                          | Standard.                                                                 |
| factoriel / factoriel en codimension $\geq k$     | factorial / factorial in codimension $\geq k$           | Standard (unique factorization).                                          |
| critère de normalité de Serre                     | Serre's criterion of normality                          | Standard.                                                                 |
| diviseur principal / localement principal         | principal / locally principal divisor                   | Standard.                                                                 |
| diviseur de Cartier                               | Cartier divisor                                         | Standard.                                                                 |
| anneau de valuation discrète                      | discrete valuation ring                                 | Standard.                                                                 |
| résolution libre finie                            | finite free resolution                                  | Standard.                                                                 |
| dimension cohomologique                           | cohomological dimension                                 | Standard.                                                                 |
| dimension projective (`dp`)                       | projective dimension (`dp`)                             | Auslander–Buchsbaum formula context.                                      |
| base de filtre                                    | filter base                                             | "Decreasing filtered family" per N.D.E.                                   |
| algébrisable                                      | algebraizable                                           | Standard formal-geometry term.                                            |
| Hauptidealsatz                                    | Hauptidealsatz                                          | Krull's principal-ideal theorem; kept untranslated.                       |
| canularesque (Grothendieck slang)                 | farcical / a farce                                      | From `canular` (hoax). Preserves the joking register.                     |
| Je dis que                                        | I claim that                                            | Preserves the first-person move.                                          |
| "point-base"                                      | "base-point"                                            | In quotation marks.                                                       |

## Style anchors (style is non-negotiable for cross-volume consistency)

These are inherited from SGA 1's translation; deviate only if SGA 1 itself is inconsistent.

- **File naming.** `00-title-preface.md`, `00-introduction.md`, `NN-<slug>.md` for Exposés, `glossary.md`,
  `zz-index-*.md` for indexes.
- **Heading hierarchy.** `# Exposé N. <English Title>`, then `## 1. <Section Title>`, then `### <Subsection>` if
  needed. The Exposé heading carries a `<!-- label: N -->` comment on the next line.
- **Statement blocks.** `**Proposition.**`, `**Lemma.**`, `**Theorem.**`, `**Corollary.**`, `**Definition.**`,
  `**Remark.**`, `**Example.**` on their own line. The label `<!-- label: N.X.Y -->` follows on the next line (after a
  blank line). The body begins after another blank line.
- **Math.** Unicode math wrapped in backticks for inline. Displayed math in fenced ```` ```text ```` blocks. Numbered
  displayed equations get a `<!-- label: eq:N.X.Y -->` comment immediately after the closing fence.
- **Footnotes.** Markdown `[^slug]` syntax. The footnote body goes at the end of the section (or end of file).
  Original Grothendieck-era footnotes: `[^<exposenum>-<sec>-<n>]` slugs (e.g. `[^I-1-1]`). Editor footnotes:
  $[{}^{N}.D.E-<expose>-<n>]$ (e.g. $[{}^{N}.D.E-IV-2]$).
- **Page marks.** `<!-- original page N -->` on its own line at page boundaries.
- **Cross-references.** Use the source's own convention: `(VIII 2.3)`, `(EGA III 4.1.5)`, `(SGA 4 IV 3.8)`.
- **Bibliographies.** Each Exposé's own bibliography section, at its end, is preserved as a `## Bibliography` section
  with entries as a numbered list, journal titles in italics, with the original keys (e.g. `[1]`, `[2]`) preserved as
  leading bracketed labels.


<!-- SOURCE: zz-index-notations.md -->

# Index of notation

<!-- label: II.index-notations -->

A reference index of notation used throughout SGA 2. Locators are of the form `<Exposé Roman>.<section>(.<sub>)` or
$<Expos\acute{e} Roman> (p. <page>)$.

| Notation                                                                            | Where introduced    |
| ----------------------------------------------------------------------------------- | ------------------- |
| $\Gamma_{Z}$, $\Gamma Z$ (sheafified)                                               | I.1                 |
| $i^{!}$, $i_{!}$                                                                    | I.1                 |
| $Z_{Z,X}$                                                                           | I.1.6               |
| $H^{i}_{Z}(X, F)$, $\mathcal{H}^{i}_{Z}(F)$ (sheafified)                            | I.2                 |
| $H^{i}_{J}(M)$, $H^{i}((f), M)$, $H^{i}(M)$                                         | IV.5.4, V.2 (p. 50) |
| `Ass M`, `Supp M`, `Ann M`, $r(a)$                                                  | III.1.1             |
| $prof_{I}(M)$, $prof_{Y}(F)$                                                        | III.2.3, III.2.8    |
| `Ab` (the category of abelian groups)                                               | IV.1 (p. 33)        |
| $\operatorname{Hom}_{\bullet}(F_{\bullet}, G_{\bullet})$ (complex of homomorphisms) | V.1.1               |
| $Ext^{i}_{Z}(X; F, G)$, $\mathcal{E}xt^{i}_{Z}(F, G)$ (sheafified)                  | VI.1.1              |
| $\hat{E}t(X)$, $L(Z)$                                                               | X (p. 89)           |
| $Lef(X, Y)$, $Leff(X, Y)$                                                           | X.2 (p. 90)         |
| $P(X)$ (Picard functor), $\operatorname{Pic}(X)$ (Picard group)                     | XI (p. 99)          |
| $\Pi^{x}_{i}(X)$ (local homotopy groups)                                            | XIII (p. 146)       |
| $D^{+}(X)$ (derived category)                                                       | XIV.1.0             |
| $prof_{Y}(F) \geqslant n$                                                           | XIV.1.2             |
| $prof^{L}_{Y}(X) \geqslant n$ (depth with respect to a set of primes $L$)           | XIV.1.2             |
| $prof^{\acute{e}}_{Y}t(X)$ (étale depth)                                            | XIV.1.2             |
| $L$ (a set of prime numbers)                                                        | XIV.1.2             |
| $prof_{x}(F) \geqslant n$                                                           | XIV.1.7             |
| $prof^{L}_{x}(X) \geqslant n$                                                       | XIV.1.7             |
| $prof^{hopL}_{x}(X) \geqslant 3$                                                    | XIV.1.7             |
| $prof^{\acute{e}}_{x}t(X)$                                                          | XIV.1.7             |
| $\delta_{t}(x)$, $\delta(n)$                                                        | XIV.2.1             |
| $H^{i}_{Z!}(X/S, F)$                                                                | XIV.4.0             |


<!-- SOURCE: zz-index-terminologique.md -->

# Terminological index

<!-- label: II.index-terminologique -->

A reference index of terminology used throughout SGA 2. Locators are of the form `<Exposé Roman>.<section>(.<sub>)` or
$<Expos\acute{e} Roman> (p. <page>)$.

| Term                                                           | Where introduced        |
| -------------------------------------------------------------- | ----------------------- |
| Auslander–Buchsbaum theorem                                    | XI.3.13                 |
| comparison theorem                                             | IX.1.1, XII.2.1         |
| local duality theorem                                          | V.2.1                   |
| projective duality theorem                                     | XII.1.1                 |
| injective envelope                                             | IV (p. 41)              |
| excision theorem                                               | I.2.2, VI.1.3           |
| existence theorem                                              | IX.2.1, XII.3.1         |
| essential extension                                            | IV (p. 41)              |
| finiteness theorem                                             | VIII.2.1, XII.1.5       |
| dualizing functor                                              | IV.4.1, IV.4.2          |
| residue form                                                   | IV.5.5                  |
| geometrically factorial (resp. geom. parafactorial) local ring | XIII (pp. 20, 24)       |
| local homotopy groups                                          | XIII (p. 146)           |
| Gysin homomorphism                                             | I (p. 14)               |
| Hartshorne theorem                                             | III.3.6                 |
| Lefschetz condition                                            | X.2 (p. 90)             |
| effective Lefschetz condition                                  | X.2 (p. 90)             |
| affine Lefschetz theorem                                       | XIV.3.1                 |
| dualizing module                                               | IV.4.1                  |
| orthogonal of a submodule                                      | IV.5                    |
| parafactorial pair of preschemes                               | XI.3.1                  |
| parafactorial local ring                                       | XI.3.2                  |
| depth                                                          | III.2.3                 |
| étale depth                                                    | XIV.1.2                 |
| geometrical depth of a noetherian local ring                   | XIV.5.3                 |
| homotopical depth                                              | XIII.6, Def. 1 (p. 154) |
| homotopical depth (with respect to $L$)                        | XIV.1.2                 |
| rectified homotopical depth                                    | XIII, Def. 2 (p. 155)   |
| pure local ring                                                | X.3.2                   |
| pure pair of preschemes                                        | X.3.1                   |
| Zariski–Nagata purity theorem                                  | X.3.4                   |
| cohomological purity theorem                                   | XIV.1.11                |
| $M$-regular                                                    | III.2.1                 |
| Samuel conjecture                                              | XI.3.14                 |
| cohomological semi-purity theorem                              | XIV.1.10                |
| strictly local ring                                            | XIII.6 (p. 151)         |

