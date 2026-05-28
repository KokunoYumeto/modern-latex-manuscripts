# SGA 1: Étale Coverings and the Fundamental Group

> Consolidated from the jcreinhold LLM-generated Markdown snapshot included in the source package packet. Not mathematically proofed in this batch.



<!-- SOURCE: 00-avertissement.md -->

# Foreword

<!-- label: I.avertissement -->

Each written exposé gives the substance of several consecutive oral lectures. It did not seem useful to specify their
dates.

Exposé VII, to which reference is made several times in the course of Exposé VIII, was not written up by the lecturer.
In the oral lectures he had limited himself to sketching the language of descent in general categories, taking a
strictly utilitarian point of view and without entering into the logical difficulties raised by this language. It became
clear that a correct exposition of this language would exceed the limits of the present notes, if only by its length.
For a fully formed exposition of descent theory, I refer to an article in preparation by Jean Giraud. Pending its
publication,[^foreword-1] I think an attentive reader will have no difficulty supplying by his own means the phantom
references in Exposé VIII.

Other oral exposés, placed after Exposé XI and alluded to at certain points in the text, were likewise not written up,
and were intended to form the substance of Exposé XII and Exposé XIII. The first of these oral exposés took up, in the
framework of schemes and analytic spaces with nilpotent elements as introduced in the Cartan Seminar 1960/61, the
construction of the analytic space associated to a prescheme locally of finite type over a complete valued field k, the
GAGA-type theorems in the case where k is the field of complex numbers, and the application to the comparison of the
fundamental group defined by transcendental methods with the fundamental group studied in these notes; compare A.
Grothendieck, _Fondements de la Géométrie Algébrique_, Séminaire Bourbaki no. 190, page 10, December 1959.

The last oral exposés sketched the generalization of the methods developed in the text for the study of coverings
admitting tame ramification, and of the structure of the fundamental group of a complete curve deprived of a finite
number of points; compare the same source, no. 182, page 27, Theorem 14. These exposés introduce no essentially new
idea, which is why it did not seem indispensable to give them a formal written version before the appearance of the
corresponding chapters of the _Éléments de Géométrie Algébrique_.[^foreword-2]

By contrast, Lefschetz-type theorems for the fundamental group and the Picard group, both locally and globally, were the
subject of a separate seminar in 1962, which has been completely written up and is available to users.[^foreword-3] Let
us point out that the results developed both in the present Seminar and in that of 1962 will be used in an essential way
in the publication of several key results in the étale cohomology of preschemes, which will be the subject of a seminar,
conducted by M. Artin and myself, in 1963/64 and currently in preparation.[^foreword-4]

Exposés I through IV, essentially local and very elementary in nature, will be entirely absorbed by Chapter IV of the
_Éléments de Géométrie Algébrique_, whose first part is in press and will doubtless be published toward the end of 1964.
They may nevertheless be useful to a reader who wishes to acquaint himself with the essential properties of smooth,
étale, or flat morphisms before entering the arcana of a systematic treatise. As for the other exposés, they will be
absorbed into Chapter VIII[^foreword-5] of the _Éléments_, whose publication can hardly be contemplated before several
years.

Bures, June 1963.

[^foreword-1]: Now published: J. Giraud, _Méthodes de la descente_, Mémoire no. 2 of the Société mathématique de France,
    1964\.

[^foreword-2]: They are included in the present volume in Exposé XII by Mme Raynaud, with a proof different from the
    original proof presented in the oral seminar; cf. the introduction.

[^foreword-3]: _Cohomologie étale des faisceaux cohérents et théorèmes de Lefschetz locaux et globaux_ (SGA 2),
    published by North-Holland Publishing Company.

[^foreword-4]: _Cohomologie étale des schémas_ (cited as SGA 4), to appear in this same series.

[^foreword-5]: In fact, because of a change in the initially planned outline of the _Éléments_, the study of the
    fundamental group is postponed there to a chapter later than the one just indicated. Compare the introduction
    preceding the present Foreword.


<!-- SOURCE: 00-introduction.md -->

# Introduction

<!-- label: I.0 -->

In the first part of this introduction, we give details on the contents of the present volume; in the second, on the
whole of the “Séminaire de Géométrie Algébrique du Bois-Marie”, of which the present volume is the first tome.

## 1

<!-- label: I.introduction.1 -->

The present volume presents the foundations of a theory of the fundamental group in algebraic geometry, from the
“Kroneckerian” point of view that makes it possible to treat on the same footing the case of an algebraic variety in the
usual sense and, for example, that of the ring of integers of a number field. This point of view can be expressed
satisfactorily only in the language of schemes, and we shall freely use this language, as well as the principal results
set out in the first three chapters of the _Éléments de Géométrie Algébrique_ by J. Dieudonné and A. Grothendieck, cited
below as EGA. The study of the present volume of the “Séminaire de Géométrie Algébrique du Bois-Marie” requires no other
knowledge of algebraic geometry, and can therefore serve as an introduction to current techniques in algebraic geometry
for a reader wishing to become familiar with them.

Exposés I through XI of this book are a textual reproduction, practically unchanged, of the mimeographed notes of the
oral seminar, which were distributed by the Institut des Hautes Études Scientifiques.[^intro-1] We have limited
ourselves to adding a few footnotes to the original text, correcting a few typographical errors, and making one
terminological adjustment: in particular, the term “simple morphism” was in the meantime replaced by “smooth morphism”,
which does not give rise to the same confusions.

Exposés I through IV present the local notions of étale morphism and smooth morphism; they make little use of the
language of schemes, set out in Chapter I of the _Éléments_.[^intro-2] Exposé V presents the axiomatic description of
the fundamental group of a scheme, useful even in the classical case where the scheme reduces to the spectrum of a
field, where one finds a very convenient reformulation of the usual Galois theory. Exposés VI and VIII present descent
theory, which has taken on growing importance in algebraic geometry in recent years and could render analogous services
in analytic geometry and topology. It should be noted that Exposé VII had not been written up, and that its substance is
incorporated into a work of J. Giraud, _Méthode de la Descente_, _Bulletin de la Société Mathématique de France_,
Mémoire 2, 1964, viii + 150 pages.

In Exposé IX, one studies more specifically the descent of étale morphisms, obtaining a systematic approach to Van
Kampen type theorems for the fundamental group, which appear here as simple translations of descent theorems. It is
essentially a method for computing the fundamental group of a connected scheme X, equipped with a surjective and proper
morphism, say X′ → X, in terms of the fundamental groups of the connected components of X′ and of the fiber products X′
×\_X X′, X′ ×\_X X′ ×\_X X′, and of the homomorphisms induced between these groups by the canonical simplicial morphisms
between the preceding schemes. Exposé X gives the theory of specialization of the fundamental group for a proper and
smooth morphism; its most striking result consists in the determination, up to a small ambiguity, of the fundamental
group of a smooth algebraic curve in characteristic p > 0, thanks to the result known by transcendental methods in
characteristic zero. Exposé XI gives some examples and complements, making explicit in cohomological form Kummer’s
theory of coverings and Artin-Schreier’s.

For other comments on the text, see the “Foreword” to the multigraphed version, which follows the present Introduction.

Since this Seminar was written in 1961, M. Artin and I have developed the language of the étale topology and a
corresponding cohomological theory, set out in SGA 4, “Cohomologie étale des schémas”, of the _Séminaire de Géométrie
Algébrique_, to appear in the same series as the present volume. This language, and the results already available in it,
provide a particularly flexible tool for the study of the fundamental group, making it possible to understand better,
and to go beyond, some of the results set out here. The theory of the fundamental group should therefore be taken up
again entirely from this point of view; in fact all the key results already appear in that work.

This was what had been planned for the chapter of the _Éléments_ devoted to the fundamental group, which was also to
contain several other developments that could not find a place here, relying on the technique of resolution of
singularities: the computation of the “local fundamental group” of a complete local ring in terms of a suitable
resolution of the singularities of that ring; local and global Künneth formulas for the fundamental group without a
properness hypothesis (cf. Exposé XIII); and M. Artin’s results on the comparison of the local fundamental groups of an
excellent henselian local ring and of its completion (SGA 4 XIX). Let us also point out the need to develop a theory of
the fundamental group of a topos, which will encompass at once the ordinary topological theory, its semi-simplicial
version, the “profinite” variant developed in Exposé V of the present volume, and the slightly more general pro-discrete
variant of SGA 3 X 7, adapted to the case of schemes that are non-normal and not unibranch.

While awaiting a complete recasting of the theory in this spirit, Exposé XIII by Mme Raynaud, using the language and
results of SGA 4, is intended to show the use that can be made of it in a few typical questions, especially by
generalizing some results of Exposé X to non-proper relative schemes. In particular, it gives the structure of the
prime-to-p fundamental group of a non-complete algebraic curve in arbitrary characteristic, which I had announced in
1959 but for which no proof had been published to date.

Despite these many gaps and imperfections, or as others would say because of these gaps and imperfections, I think the
present volume may be useful to the reader who wishes to become familiar with the theory of the fundamental group, and
also as a reference work, while awaiting the writing and publication of a text escaping the criticisms I have just
enumerated.

## 2

<!-- label: I.introduction.2 -->

The present volume is tome 1 of the “Séminaire de Géométrie Algébrique du Bois-Marie”, whose following volumes are
planned to appear in the same series. The aim of the _Séminaire_, parallel to the treatise _Éléments de Géométrie
Algébrique_ by J. Dieudonné and A. Grothendieck, is to lay the foundations of algebraic geometry according to the points
of view of the latter work. The standard reference for all volumes of the _Séminaire_ consists of Chapters I, II, and
III of the _Éléments de Géométrie Algébrique_, cited as EGA I, II, and III; the reader is assumed to possess the
background in commutative algebra and homological algebra implied by those chapters.[^intro-3] In addition, in each
volume of the _Séminaire_, reference will be made freely, as needed, to earlier volumes of the same _Séminaire_, or to
other published or soon-to-appear chapters of the _Éléments_.

Each part of the _Séminaire_ is centered on a main subject, indicated in the title of the corresponding volume or
volumes; the oral seminar generally covers one academic year, sometimes more. The exposés within each part of the
_Séminaire_ are generally in close logical dependence on one another; by contrast, the different parts of the
_Séminaire_ are, to a large extent, logically independent of one another. Thus the part “Group Schemes” is almost
entirely independent of the two parts of the _Séminaire_ that chronologically precede it, although it frequently appeals
to results of EGA IV. Here is the list of the parts of the _Séminaire_ that are to appear shortly, cited below as SGA 1
through SGA 7:

- SGA 1. Étale coverings and the fundamental group, 1960 and 1961.
- SGA 2. Local cohomology of coherent sheaves and local and global Lefschetz theorems, 1961/62.
- SGA 3. Group schemes, 1963 and 1964, three volumes, in collaboration with M. Demazure.
- SGA 4. Theory of topoi and étale cohomology of schemes, 1963/64, three volumes, in collaboration with M. Artin and J.
  L. Verdier.
- SGA 5. ℓ-adic cohomology and L-functions, 1964 and 1965, two volumes.
- SGA 6. Intersection theory and the Riemann-Roch theorem, 1966/67, two volumes, in collaboration with P. Berthelot and
  L. Illusie.
- SGA 7. Local monodromy groups in algebraic geometry.

Three of these partial seminars were directed in collaboration with other mathematicians, who will appear as co-authors
on the covers of the corresponding volumes. As for the other active participants in the _Séminaire_, whose role, both
editorial and mathematical, has grown from year to year, each participant’s name appears at the head of the exposés for
which he is responsible as lecturer or writer, and the list of those appearing in a given volume is indicated on that
volume’s flyleaf.

It is appropriate to give a few details on the relation between the _Séminaire_ and the _Éléments_. The latter were
intended in principle to give an overall account of the notions and techniques judged most fundamental in algebraic
geometry, as those notions and techniques themselves emerge through the natural play of demands of logical and aesthetic
coherence. From this viewpoint, it was natural to consider the _Séminaire_ as a preliminary version of the _Éléments_,
destined sooner or later to be absorbed almost entirely into them. This process had already begun to some extent several
years ago, since Exposés I through IV of the present volume SGA 1 are entirely encompassed by EGA IV, and Exposés VI
through VIII were to be so within a few years in EGA VI.

However, as the work of building undertaken in the _Éléments_ and in the _Séminaire_ develops, and as the overall
proportions become clearer, the initial principle, according to which the _Séminaire_ would constitute only a
preliminary and provisional version, appears less and less realistic, for reasons including the limits prudently imposed
by nature on the length of human life. Given the care generally taken in writing the different parts of the _Séminaire_,
there will doubtless be reason to take up such a part again in the _Éléments_, or in treatises that might take over from
them, only when later progress permits very substantial improvements, at the cost of fairly deep modifications. This is
already the case for the present seminar SGA 1, as said above, and also for SGA 2, thanks to recent results of Mme
Raynaud. By contrast, nothing at present indicates that this will be so in the near future for any of the parts cited
above, SGA 3 through SGA 7.

References inside the “Séminaire de Géométrie Algébrique du Bois Marie” are given as follows. An internal reference to
one of the parts SGA 1 through SGA 7 of the _Séminaire_ is given in the style III 9.7, where the numeral III denotes the
number of the exposé, which appears at the top of each page of the exposé in question, and 9.7 denotes the number of the
statement, definition, remark, or similar item inside that exposé. If needed, longer decimal numbers may be used, for
example 9.7.1 and 9.7.2 to designate the various steps in the proof of Proposition 9.7. The reference III 9 denotes
paragraph 9 of Exposé III. The number of the exposé is omitted for references internal to an exposé. For a reference to
another part of the _Séminaire_, the same sigla are used, but preceded by the mention of the SGA part in question, for
example SGA 1 III 9.7. Similarly, the reference EGA IV 11.5.7 means: _Éléments de Géométrie Algébrique_, Chapter IV,
statement, definition, etc. 11.5.7; here, the first Arabic numeral again denotes the paragraph number. Apart from these
conventions, in force throughout the SGA, the bibliography for an exposé will generally be gathered at its end, and
inside the exposé it will be referred to by numbers in square brackets, such as [3], according to custom.

Finally, for the reader’s convenience, whenever it seems necessary, we shall append to the end of SGA volumes an index
of notation and a terminological index containing, where appropriate, an English translation of the French terms used.

I wish to add an extra-mathematical comment to this introduction. In November 1969 I learned that the Institut des
Hautes Études Scientifiques, where I had been a professor essentially since its founding, had for three years been
receiving subsidies from the Ministry of the Armed Forces. Already as a beginning researcher I had found extremely
regrettable the lack of scruple shown by most scientists in accepting collaboration in one form or another with military
apparatuses. My motivations at that time were essentially moral in nature, and hence not very likely to be taken
seriously. Today they acquire a new force and a new dimension, given the danger of destruction of the human species with
which we are threatened by the proliferation of military apparatuses and of the means of mass destruction at their
disposal.

I have explained myself elsewhere in more detail on these questions, much more important than the advancement of any
science, mathematics included; one may for example consult on this subject G. Edwards’s article in number 1 of the
journal _Survivre_ (August 1970), summarizing a more detailed exposition of these questions that I had given elsewhere.
Thus I found myself working for three years in an institution while it was taking part, unbeknownst to me, in a mode of
financing that I consider immoral and dangerous.[^intro-4] Being at present alone in holding this opinion among my
colleagues at the IHES, which has doomed to failure my efforts to obtain the removal of military subsidies from the IHES
budget, I have taken the necessary decision and leave the IHES on September 30, 1970, and likewise suspend all
scientific collaboration with this institution as long as it continues to accept such subsidies.

I have asked M. Motchane, director of the IHES, that from October 1, 1970 the IHES abstain from distributing
mathematical texts of which I am the author, or which form part of the Séminaire de Géométrie Algébrique du Bois Marie.
As was said above, distribution of this seminar will be carried out by the Julius Springer publishing house, in the
Lecture Notes series. I am happy to thank Springer and Mr. K. Peters here for the effective and courteous help they gave
me in making this publication possible, in particular by taking charge of the typing for photo-offset of the new exposés
added to old seminars, and of the missing exposés in incomplete seminars.

I also thank Mr. J. P. Delale, who took on the thankless task of compiling the index of notation and the terminological
index.

Massy, August 1970.

[^intro-1]: As were the notes of the seminars following this one. Since this mode of distribution proved impractical and
    insufficient in the long run, all the “Séminaire de Géométrie Algébrique du Bois-Marie” will henceforth appear in
    book form, as the present volume does.

[^intro-2]: A more complete study is now available in the _Éléments_, Chapter IV, §§17 and 18.

[^intro-3]: See the Introduction to EGA I for details on this point.

[^intro-4]: It goes without saying that the opinion I have just expressed engages only my own responsibility, and not
    that of the Springer publishing house, which is editing the present volume.


<!-- SOURCE: 00-title-preface.md -->

# SGA 1: Étale Coverings and the Fundamental Group

Séminaire de Géométrie Algébrique du Bois Marie, 1960-61.

A seminar directed by A. Grothendieck, augmented by two exposés by Mme M. Raynaud.

## Abstract

This volume is a retypeset and annotated edition of _Revêtements Étales et Groupe Fondamental_, Lecture Notes in
Mathematics 224, Springer-Verlag, Berlin-Heidelberg-New York, 1971, by Alexander Grothendieck et al.

The text presents the foundations of a theory of the fundamental group in algebraic geometry, from the “Kroneckerian”
point of view that makes it possible to treat on the same footing the case of an algebraic variety in the usual sense
and, for example, that of the ring of integers of a number field.

## Subject Class

14-02, 14A15, 14B25, 14D15, 14E20, 14F35, 14H30

## Keywords

Étale morphism, smooth morphism, flat morphism, scheme, fundamental group, covering, descent theory, specialization.

## Preface

The present text is a retypeset and annotated edition of _Revêtements Étales et Groupe Fondamental_, Lecture Notes in
Mathematics 224, Springer-Verlag, Berlin-Heidelberg-New York, 1971, by Alexander Grothendieck et al.

The composition in LaTeX 2e was carried out by volunteers participating in a project directed by Bas Edixhoven; more
details can be found at `http://www.math.leidenuniv.nl/~edix/`. The page layout was completed by the Société
mathématique de France.

This is a slightly corrected version of the original text. It is published by the Société mathématique de France in the
series _Documents Mathématiques_. Some updates were made by Michel Raynaud. They are delimited by brackets and marked by
the symbol `(MR)`: remarks on pages X.2.14, XI.1.4, XII.5.6, XIII.2.13, and the note III.6.6.p24. To make the notation
uniform, the residue field of a point x is denoted κ(x), and the residue field of a local ring A is denoted κ(A).

There also exists an electronic version intended to reproduce the original text.

The two versions are produced from a single source file, located on the arXiv.org e-print server at $http://arxiv.org/$.
The differences between the two versions are documented in the source file.

The old page numbering is incorporated in the margin; the number n indicates the beginning of page n.


<!-- SOURCE: 01-morphismes-etales.md -->

# Exposé I. Étale Morphisms

<!-- label: I -->

<!-- original page 1 -->

To simplify the exposition, we assume that all preschemes under consideration are locally noetherian, at least after no.
I.2.

## 1. Notions of Differential Calculus

<!-- label: I.1 -->

Let $X$ be a prescheme over $Y$, and let $\Delta_{X/Y}$, or simply $\Delta$, denote the diagonal morphism
$X \to X \times_{Y} X$. It is an immersion, hence a closed immersion of $X$ into an open subset $V$ of $X \times_{Y} X$.
Let $\mathcal{I}_{X}$ be the ideal of the closed subprescheme corresponding to the diagonal in $V$. Note that if one
wants to do things intrinsically, without assuming $X$ separated over $Y$, a hypothesis that would be farcical here, one
should consider the set-theoretic inverse image of $\mathcal{O}_{X\times X}$ in $X$, and designate by $\mathcal{I}_{X}$
the augmentation ideal in the latter.

The sheaf $\mathcal{I}_{X}/\mathcal{I}^{2}_{X}$ may be regarded as a quasi-coherent sheaf on $X$; it is denoted
$\Omega^{1}_{X/Y}$. It is of finite type if $X \to Y$ is of finite type. It behaves well with respect to an extension of
the base $Y' \to Y$.

One also introduces the sheaves

$$
\mathcal{O}_{X\times_{Y} X}/\mathcal{I}^{n+1}_{X} = \mathcal{P}^{n}_{X/Y}.
$$

These are sheaves of rings on $X$, making $X$ into a prescheme that may be denoted $\Delta^{n}_{X/Y}$ and called the
n-th infinitesimal neighborhood of $X/Y$. The sorites for this are of total triviality, although rather long;[^I-1-1] it
would be prudent to speak of them only when one has something useful to say about them, namely with smooth morphisms.

## 2. Quasi-Finite Morphisms

<!-- label: I.2 -->

**Proposition.**

<!-- label: I.2.1 -->

Let $A \to B$ be a local homomorphism; from now on the rings are noetherian. Let $\mathfrak{m}$ be the maximal ideal of
$A$. The following conditions are equivalent:

1. $B/\mathfrak{m}B$ is finite-dimensional over $k = A/\mathfrak{m}$.
1. $\mathfrak{m}B$ is an ideal of definition, and $B/\mathfrak{r}(B) = \kappa(B)$ is an extension of $k = \kappa(A)$.
1. The completion $\hat{B}$ is finite over the completion `Â` of $A$.

One then says that $B$ is quasi-finite over $A$.

<!-- original page 2 -->

A morphism $f: X \to Y$ is said to be quasi-finite at $x$, or the $Y$-prescheme $f$ is said to be quasi-finite at $x$,
if $\mathcal{O}_{x}$ is quasi-finite over $\mathcal{O}_{f(x)}$. This is also equivalent to saying that $x$ is isolated
in its fiber $f^{-1}(f(x))$. A morphism is said to be quasi-finite if it is so at every point.[^I-2-1]

**Corollary.**

<!-- label: I.2.2 -->

If $A$ is complete, quasi-finite is equivalent to finite.

One could give the usual sorites (i), (ii), (iii), (iv), (v) for quasi-finite morphisms, but that does not seem
indispensable here.

## 3. Unramified or Net Morphisms

<!-- label: I.3 -->

**Proposition.**

<!-- label: I.3.1 -->

Let $f: X \to Y$ be a morphism of finite type, let $x \in X$, and let $y = f(x)$. The following conditions are
equivalent:

1. $\mathcal{O}_{x}/\mathfrak{m}_{y}\mathcal{O}_{x}$ is a finite separable extension of $\kappa(y)$.
1. $\Omega^{1}_{X/Y}$ vanishes at $x$.
1. The diagonal morphism $\Delta_{X/Y}$ is an open immersion in a neighborhood of $x$.

For the implication (i) ⇒ (ii), Nakayama immediately reduces us to the case $Y = \operatorname{Spec}(k)$,
$X = \operatorname{Spec}(k')$, where this is well known and, moreover, trivial from the definition of separability. The
implication (ii) ⇒ (iii) follows from a pleasant and easy characterization of open immersions, using Krull. For (iii) ⇒
(i), one is again reduced to the case where $Y = \operatorname{Spec}(k)$ and where the diagonal morphism is everywhere
an open immersion. One must then prove that $X$ is finite with separable coordinate ring over $k$; for this, one reduces
to the case where $k$ is algebraically closed. But then every closed point of $X$ is isolated, since it is identical
with the inverse image of the diagonal by the morphism $X \to X \times_{k} X$ defined by $x$; hence $X$ is finite. We
may then suppose that $X$ is reduced to a point, with ring $A$, so that $A \otimes_{k} A \to A$ is an isomorphism,
whence $A = k$, as required.

**Definition.**

<!-- label: I.3.2 -->

1. One then says that $f$ is net, or also unramified, at $x$, or that $X$ is net, or unramified, at $x$ over $Y$.
1. Let $A \to B$ be a local homomorphism. One says that it is net, or unramified, or that $B$ is a local algebra net, or
   unramified, over $A$, if $B/\mathfrak{r}(A)B$ is a finite separable extension of $A/\mathfrak{r}(A)$, i.e. if
   $\mathfrak{r}(A)B = \mathfrak{r}(B)$, and $\kappa(B)$ is a separable extension of $\kappa(A)$.[^I-3-1]

**Remark.**

<!-- original page 3 -->

The fact that $B$ is net over $A$ can already be recognized on the completions of $A$ and $B$. Net implies quasi-finite.

**Corollary.**

<!-- label: I.3.3 -->

The set of points where $f$ is net is open.

**Corollary.**

<!-- label: I.3.4 -->

Let $X'$ and $X$ be two preschemes of finite type over $Y$, and let $g: X' \to X$ be a $Y$-morphism. If $X$ is net over
$Y$, the graph morphism $\Gamma_{g}: X' \to X \times_{Y} X$ is an open immersion.

Indeed, it is the inverse image of the diagonal morphism $X \to X \times_{Y} X$ by

```text
g ×_Y id_{X′}: X′ ×_Y X → X ×_Y X.
```

One may also introduce the annihilator ideal $\mathfrak{d}_{X/Y}$ of $\Omega^{1}_{X/Y}$, called the different ideal of
$X/Y$; it defines a closed subprescheme of $X$ which, set-theoretically, is the set of points where $X/Y$ is ramified,
i.e. not net.

**Proposition.**

<!-- label: I.3.5 -->

1. An immersion is net.
1. The composite of two net morphisms is net.
1. A base extension of a net morphism is again net.

This is seen indifferently from (ii) or (iii), the second seeming to me more amusing. One can of course also be more
precise by giving pointwise statements; this is only apparently more general, except in the setting of definition b),
and tedious. As usual, one obtains the following corollaries.

**Corollaries.**

<!-- label: I.3.6 -->

1. The cartesian product of two net morphisms is again net.
1. If `gf` is net, then $f$ is net.
1. If $f$ is net, then $f_{red}$ is net.

**Proposition.**

<!-- label: I.3.7 -->

Let $A \to B$ be a local homomorphism, and suppose that the residue extension $\kappa(B)/\kappa(A)$ is trivial, or that
$\kappa(A)$ is algebraically closed. For $B/A$ to be net, it is necessary and sufficient that $\hat{B}$ be, as an
`Â`-algebra, a quotient of `Â`.

**Remarks.**

- In the case where the residue extension is not assumed trivial, one can reduce to that case by making a suitable
  finite flat extension over $A$ that kills the given extension.
- Give the example where $A$ is the local ring of an ordinary double point of a curve, and $B$ that of a point of the
  normalization: then $A \subset B$, $B$ is net over $A$ with trivial residue extension, and $\hat{A} \to \hat{B}$ is
  surjective but not injective.

<!-- original page 4 -->

We shall therefore strengthen the notion of netness.

## 4. Étale Morphisms. Étale Coverings

<!-- label: I.4 -->

We shall admit everything that will be necessary for us concerning flat morphisms; these facts will be proved later, if
needed.[^I-4-1]

**Definition.**

<!-- label: I.4.1 -->

1. Let $f: X \to Y$ be a morphism of finite type. One says that $f$ is étale at $x$ if $f$ is flat at $x$ and net at
   $x$. One says that $f$ is étale if it is so at all points. One says that $X$ is étale at $x$ over $Y$, or that it is
   a $Y$-prescheme étale at $x$, etc.
1. Let $f: A \to B$ be a local homomorphism. One says that $f$ is étale, or that $B$ is étale over $A$, if $B$ is flat
   and unramified over $A$.[^I-4-2]

**Proposition.**

<!-- label: I.4.2 -->

For $B/A$ to be étale, it is necessary and sufficient that $\hat{B}/\hat{A}$ be étale.

Indeed, this is true separately for "net" and for "flat".

<!-- original page 5 -->

**Corollary.**

<!-- label: I.4.3 -->

Let $f: X \to Y$ be of finite type, and let $x \in X$. The fact that $f$ is étale at $x$ depends only on the local
homomorphism $\mathcal{O}_{f(x)} \to \mathcal{O}_{x}$, and even only on the corresponding homomorphism for completions.

**Corollary.**

<!-- label: I.4.4 -->

Suppose that the residue extension $\kappa(A) \to \kappa(B)$ is trivial, or that $\kappa(A)$ is algebraically closed.
Then $B/A$ is étale if and only if $\hat{A} \to \hat{B}$ is an isomorphism.

One combines flatness with I.3.7.

**Proposition.**

<!-- label: I.4.5 -->

Let $f: X \to Y$ be a morphism of finite type. Then the set of points where it is étale is open.

Indeed, this is true separately for "net" and for "flat".

This proposition shows that in the study of morphisms of finite type that are étale somewhere, one may drop the
"pointwise" statements.

**Proposition.**

<!-- label: I.4.6 -->

1. An open immersion is étale.
1. The composite of two étale morphisms is étale.
1. Base extension.

Indeed, (i) is trivial, and for (ii) and (iii) it suffices to note that this is true for "net" and for "flat". To tell
the truth, there are also corresponding statements for local homomorphisms, without finiteness conditions, which in any
case should appear in the multiplodocus, beginning with the net case.

**Corollary.**

<!-- label: I.4.7 -->

A cartesian product of two étale morphisms is likewise étale.

**Corollary.**

<!-- label: I.4.8 -->

Let $X$ and $X'$ be of finite type over $Y$, and let $g: X \to X'$ be a $Y$-morphism. If $X'$ is unramified over $Y$ and
$X$ is étale over $Y$, then $g$ is étale.

Indeed, $g$ is the composite of the graph morphism $\Gamma_{g}: X \to X \times_{Y} X'$, which is an open immersion by
I.3.4, and the projection morphism, which is étale because it is deduced from the étale morphism $X \to Y$ by the base
change $X' \to Y$.

**Definition.**

<!-- label: I.4.9 -->

An étale covering, respectively a net covering, of $Y$ is a $Y$-scheme $X$ that is finite over $Y$ and étale,
respectively net, over $Y$.

The first condition means that $X$ is defined by a coherent sheaf $\mathcal{B}$ of algebras on $Y$. The second then
means that $\mathcal{B}$ is locally free over $Y$, respectively says nothing at all, and that moreover, for every
$y \in Y$, the fiber $\mathcal{B}(y) = \mathcal{B}_{y} \otimes_{\mathcal{O}_{y}} \kappa(y)$ is a separable algebra, that
is, a finite product of finite separable extensions, over $\kappa(y)$.

**Proposition.**

<!-- label: I.4.10 -->

Let $X$ be a flat covering of $Y$ of degree $n$, defined by a coherent locally free sheaf $\mathcal{B}$ of algebras. One
defines, in the well-known way, the trace homomorphism $\mathcal{B} \to \mathcal{A}$, which is a homomorphism of
$\mathcal{A}$-modules, where $\mathcal{A} = \mathcal{O}_{Y}$. For $X$ to be étale, it is necessary and sufficient that
the corresponding bilinear form $tr_{\mathcal{B}/\mathcal{A}}(xy)$ define an isomorphism from $\mathcal{B}$ to its dual,
or equivalently that the discriminant section

```text
d_{X/Y} = d_{𝓑/𝓐} ∈ Γ(Y, ∧ⁿ𝓑̌ ⊗_𝓐 ∧ⁿ𝓑̌)
```

be invertible, or finally that the discriminant ideal defined by this section be the unit ideal.

Indeed, one is reduced to the case $Y = \operatorname{Spec}(k)$, and then this is a well-known separability criterion,
and trivial after passage to the algebraic closure of $k$.

**Remark.**

<!-- original page 6 -->

We shall have a less trivial statement below, when one does not suppose a priori that $X$ is flat over $Y$ but makes a
normality hypothesis.

## 5. The Fundamental Property of Étale Morphisms

<!-- label: I.5 -->

**Theorem.**

<!-- label: I.5.1 -->

Let $f: X \to Y$ be a morphism of finite type. For $f$ to be an open immersion, it is necessary and sufficient that it
be an étale and radicial morphism.

Recall that radicial means: injective, with radicial residue extensions; one may also recall that this means that the
morphism remains injective after every base extension. Necessity is trivial; sufficiency remains. We shall give two
different proofs, the first shorter, the second more elementary.

1. A flat morphism is open, so we may suppose, replacing $Y$ by $f(X)$, that $f$ is a homeomorphism onto $Y$. After any
   base extension, it remains true that $f$ is flat, radicial, and surjective, hence a homeomorphism, a fortiori closed.
   Thus $f$ is proper. Therefore $f$ is finite, by Chevalley's theorem, and is defined by a coherent sheaf $\mathcal{B}$
   of algebras. The sheaf $\mathcal{B}$ is locally free; moreover, by the hypothesis, it has rank 1 everywhere. Thus
   $X = Y$, as required.

1. One may suppose $Y$ and $X$ affine. Moreover, one easily reduces to proving the following: if
   $Y = \operatorname{Spec}(A)$, with $A$ local, and if $f^{-1}(y)$ is nonempty, where $y$ is the closed point of $Y$,
   then $X = Y$. Indeed, this will imply that every $y \in f(X)$ has an open neighborhood $U$ such that $X|U = U$. We
   have $X = \operatorname{Spec}(B)$, and we want to prove $A = B$. For this, one is reduced to proving the analogous
   assertion after replacing $A$ by `Â` and $B$ by $B \otimes_{A} \hat{A}$, taking into account that `Â` is faithfully
   flat over $A$. We may therefore suppose $A$ complete. Let $x$ be the point over $y$. By Corollary I.2.2,
   $\mathcal{O}_{x}$ is finite over $A$, hence, being flat and radicial over $A$, is identical with $A$. Thus
   $X = Y \amalg X'$, a disjoint sum. Since $X$ is radicial over $Y$, $X'$ is empty. This completes the proof.

**Corollary.**

<!-- label: I.5.2 -->

Let $f: X \to Y$ be a closed immersion and étale. If $X$ is connected, $f$ is an isomorphism from $X$ onto a connected
component of $Y$.

Indeed, $f$ is also an open immersion. We deduce:

**Corollary.**

<!-- label: I.5.3 -->

<!-- original page 7 -->

Let $X$ be a net $Y$-scheme, with $Y$ connected. Then every section of $X$ over $Y$ is an isomorphism from $Y$ onto a
connected component of $X$. Thus there is a one-to-one correspondence between the set of these sections and the set of
connected components $X_{i}$ of $X$ such that the projection $X_{i} \to Y$ is an isomorphism, or equivalently, by I.5.1,
is surjective and radicial. In particular, a section is known once its value at one point is known.

Only the first assertion requires proof. By I.5.2, it is enough to observe that a section is a closed immersion, since
$X$ is separated over $Y$, and is étale by I.4.8.

**Corollary.**

<!-- label: I.5.4 -->

Let $X$ and $Y$ be two preschemes over $S$, with $X$ net and separated over $S$ and $Y$ connected. Let $f$ and $g$ be
two $S$-morphisms from $Y$ to $X$, and let $y$ be a point of $Y$. Suppose $f(y) = g(y) = x$ and that the residue
homomorphisms $\kappa(x) \to \kappa(y)$ defined by $f$ and $g$ are identical, that is, $f$ and $g$ coincide
geometrically at $y$. Then $f$ and $g$ are identical.

This follows from I.5.3 by reducing to the case $Y = S$, replacing $X$ by $X \times_{S} Y$.

Here is a particularly important variant of I.5.3.

**Theorem.**

<!-- label: I.5.5 -->

Let $S$ be a prescheme, $X$ and $Y$ two $S$-preschemes, $S_{0}$ a closed subprescheme of $S$ having the same underlying
space as $S$, and let $X_{0} = X \times_{S} S_{0}$ and $Y_{0} = Y \times_{S} S_{0}$ be the "restrictions" of $X$ and $Y$
to $S_{0}$. Suppose $X$ is étale over $S$. Then the natural map

```text
Hom_S(Y, X) → Hom_{S₀}(Y₀, X₀)
```

is bijective.

One is again reduced to the case $Y = S$, and then this follows from the "topological" description of sections of $X/Y$
given in I.5.3.

**Scholium.** This result includes both a uniqueness assertion and an existence assertion for morphisms. It may also be
expressed, when $X$ and $Y$ are both taken étale over $S$, by saying that the functor $X \mapsto X_{0}$ from the
category of étale $S$-schemes to the category of étale $S_{0}$-schemes is fully faithful, i.e. establishes an
equivalence of the first category with a full subcategory of the second. We shall see below that it is even an
equivalence between the first and the second; this will be an existence theorem for étale $S$-schemes.

<!-- original page 8 -->

The following form, apparently more general, of I.5.5 is often convenient.

**Corollary ("Extension theorem for liftings").**

<!-- label: I.5.6 -->

Consider a commutative diagram

$$
Y_{0} \to X
\downarrow    \downarrow
Y  \to S
$$

of morphisms, where $X \to S$ is étale and $Y_{0} \to Y$ is a bijective closed immersion. Then one can find a unique
morphism $Y \to X$ making the two corresponding triangles commute.

Indeed, replacing $S$ by $Y$ and $X$ by $X \times_{S} Y$, one is reduced to the case $Y = S$, and then this is the
special case of I.5.5 for $Y = S$.

Let us also record the following immediate consequence of I.5.1, which we did not give as Corollary 1 so as not to
interrupt the line of ideas developed after I.5.1.

**Proposition.**

<!-- label: I.5.7 -->

Let $X$ and $X'$ be two preschemes of finite type and flat over $Y$, and let $g: X \to X'$ be a $Y$-morphism. For $g$ to
be an open immersion, respectively an isomorphism, it is necessary and sufficient that for every $y \in Y$, the induced
morphism on fibers

```text
g ⊗_Y κ(y): X ⊗_Y κ(y) → X′ ⊗_Y κ(y)
```

be an open immersion, respectively an isomorphism.

It suffices to prove sufficiency; since this is true for the notion of surjection, one is reduced to the case of an open
immersion. By I.5.1, one must verify that $g$ is radicial, which is trivial, and that it is étale, which follows from
Corollary I.5.9 below.

**Corollary.**

<!-- label: I.5.8 -->

(This should go in no. I.3.) Let $X$ and $X'$ be two $Y$-preschemes, let $g: X \to X'$ be a $Y$-morphism, let $x$ be a
point of $X$, and let $y$ be its projection to $Y$. For $g$ to be quasi-finite, respectively net, at $x$, it is
necessary and sufficient that the same be true of $g \otimes_{Y} \kappa(y)$.

Indeed, the two algebras over $k(g(x))$ that must be considered to ensure that one has a quasi-finite, respectively net,
morphism at $x$ are the same for $g$ and for $g \otimes_{Y} \kappa(y)$.

**Corollary.**

<!-- label: I.5.9 -->

<!-- original page 9 -->

With the notation of I.5.8, suppose $X$ and $X'$ are flat and of finite type over $Y$. For $g$ to be flat, respectively
étale, at $x$, it is necessary and sufficient that $g \otimes_{Y} \kappa(y)$ be so.

For "flat" the statement is included only as a reminder; it is one of the fundamental criteria for flatness.[^I-5-1] For
"étale", it follows from this, taking I.5.8 into account.

## 6. Application to Étale Extensions of Complete Local Rings

<!-- label: I.6 -->

This number is a special case of results on formal preschemes that should appear in the multiplodocus. Nevertheless,
here one gets by at less cost, i.e. without the explicit local determination of étale morphisms in no. I.7, which uses
the Main Theorem. That may be a sufficient reason to keep the present number, even in the multiplodocus, in this place.

**Theorem.**

<!-- label: I.6.1 -->

Let $A$ be a complete local ring, noetherian of course, with residue field $k$. For every $A$-algebra $B$, let
$R(B) = B \otimes_{A} k$, considered as a $k$-algebra; it thus depends functorially on $B$. Then $R$ defines an
equivalence from the category of $A$-algebras finite and étale over $A$ to the category of finite-rank separable
algebras over $k$.

First of all, the functor in question is fully faithful, as follows from the more general fact:

**Corollary.**

<!-- label: I.6.2 -->

Let $B$ and $B'$ be two $A$-algebras finite over $A$. If $B$ is étale over $A$, then the canonical map

```text
Hom_{A-alg}(B, B′) → Hom_{k-alg}(R(B), R(B′))
```

is bijective.

One is reduced to the case where $A$ is artinian, replacing $A$ by $A/\mathfrak{m}^{n}$, and then this is a special case
of I.5.5.

It remains to prove that for every finite separable $k$-algebra, why not say étale, since it is shorter, $L$, there
exists $B$ étale over $A$ such that $R(B)$ is isomorphic to $L$. We may suppose that $L$ is a separable extension of
$k$; as such it admits a generator $x$, i.e. is isomorphic to an algebra $k[t]/Fk[t]$, where $F \in k[t]$ is a monic
polynomial. Lift $F$ to a monic polynomial $F_{1}$ in `A[t]`, and take $B = A[t]/F_{1}A[t]$.

## 7. Local Construction of Unramified and Étale Morphisms

<!-- label: I.7 -->

<!-- original page 10 -->

**Proposition.**

<!-- label: I.7.1 -->

Let $A$ be a noetherian ring, $B$ a finite algebra over $A$, $u$ a generator of $B$ over $A$, $F \in A[t]$ such that
$F(u) = 0$, where $F$ is not assumed monic, $u' = F'(u)$, where $F'$ is the derived polynomial, $\mathfrak{q}$ a prime
ideal of $B$ not containing $u'$, and $\mathfrak{p}$ its trace on $A$. Then $B_{\mathfrak{q}}$ is net over
$A_{\mathfrak{p}}$.

In other words, putting $Y = \operatorname{Spec}(A)$, $X = \operatorname{Spec}(B)$, and
$X_{u'} = \operatorname{Spec}(B_{u'})$, $X_{u'}$ is unramified over $Y$. The statement follows from the following more
precise one.

**Corollary.**

<!-- label: I.7.2 -->

The different ideal of $B/A$ contains $u'B$, and is equal to it if the natural homomorphism $A[t]/FA[t] \to B$, sending
$t$ to $u$, is an isomorphism.

Let $J$ be the kernel of the homomorphism $C = A[t] \to B$. This kernel contains `FA[t]`, and is equal to it in the
second case considered in I.7.2. Since the homomorphism is surjective, $\Omega^{1}_{B/A}$ identifies with the quotient
of $\Omega^{1}_{C/A}$ by the submodule generated by $J\Omega^{1}_{C/A}$ and $d(J)$; one should have made explicit in no.
I.1 the definition of the homomorphism $d$ and the computation of $\Omega^{1}$ for a polynomial algebra. Identifying
$\Omega^{1}_{C/A}$ with $C$ by means of the basis `dt`, one finds $B/B\cdot J'$, so the different is generated by the
set $J'$ of images in $B$ of the derivatives of $G \in J$, and it suffices to take $G$ running through generators of
$J$.

Since $F \in J$, respectively since $F$ is a generator of $J$, we are done. Note that I.7.2 should be made the
proposition and I.7.1 the corollary. We find:

**Corollary.**

<!-- label: I.7.3 -->

Under the conditions of I.7.1, suppose $F$ is monic and that $A[t]/FA[t] \to B$ is an isomorphism. For
$B_{\mathfrak{q}}$ to be étale over $A_{\mathfrak{p}}$, it is necessary and sufficient that $\mathfrak{q}$ not contain
$u'$.

Indeed, since $B$ is flat over $A$, étale is equivalent to net, and one may apply I.7.2.

**Corollary.**

<!-- label: I.7.4 -->

Under the conditions of I.7.3, for $B$ to be étale over $A$, it is necessary and sufficient that $u'$ be invertible, or
again that the ideal generated by $F$ and $F'$ in `A[t]` be the unit ideal.

The last criterion follows from the first and from Nakayama, in $B$.

<!-- original page 11 -->

A monic polynomial $F \in A[t]$ having the property stated in Corollary I.7.4 is called a separable polynomial. If $F$
is not monic, one would at least have to require that the coefficient of its leading term be invertible; in the case
where $A$ is a field, one recovers the usual definition.

**Corollary.**

<!-- label: I.7.5 -->

Let $B$ be a finite algebra over the local ring $A$. Suppose that $K(A)$ is infinite or that $B$ is local. Let $n$ be
the rank of $L = B \otimes_{A} K(A)$ over $K(A) = k$. For $B$ to be net, respectively étale, over $A$, it is necessary
and sufficient that $B$ be isomorphic to a quotient of, respectively isomorphic to, $A[t]/FA[t]$, where $F$ is a monic
separable polynomial, which one may suppose, respectively which is necessarily, of degree $n$.

Only necessity has to be proved. Suppose $B$ is net over $A$, hence $L$ is separable over $k$. It then follows from the
hypothesis made that $L/k$ admits a generator $\xi$, so the $\xi^{i}$, with $0 \leq i < n$, form a basis of $L$ over
$k$. Let $u \in B$ lift $\xi$. Then, by Nakayama, the $u^{i}$, with $0 \leq i < n$, generate the $A$-module $B$,
respectively form a basis of it. In particular, one can find a monic polynomial $F \in A[t]$ such that $F(u) = 0$, and
$B$ will be isomorphic to a quotient of, respectively isomorphic to, $A[t]/FA[t]$. Finally, by I.7.4 applied to $L/k$,
$F$ and $F'$ generate `A[t]` modulo $\mathfrak{m}A[t]$, hence by Nakayama in $A[t]/FA[t]$, $F$ and $F'$ generate `A[t]`.
This completes the proof.

**Theorem.**

<!-- label: I.7.6 -->

Let $A$ be a local ring, and let $A \to \mathcal{O}$ be a local homomorphism such that $\mathcal{O}$ is isomorphic to a
localized algebra of an algebra of finite type over $A$. Suppose $\mathcal{O}$ is net over $A$. Then one can find an
$A$-algebra $B$, integral over $A$, a maximal ideal $\mathfrak{n}$ of $B$, a generator $u$ of $B$ over $A$, and a monic
polynomial $F \in A[t]$, such that $\mathfrak{n}$ does not contain $F'(u)$ and $\mathcal{O}$ is isomorphic, as an
$A$-algebra, to $B_{\mathfrak{n}}$. If $\mathcal{O}$ is étale over $A$, one can take $B = A[t]/FA[t]$.

Of course, these are also sufficient conditions.

Let us first record the pleasant corollaries.

**Corollary.**

<!-- label: I.7.7 -->

For $\mathcal{O}$ to be net over $A$, it is necessary and sufficient that $\mathcal{O}$ be isomorphic to the quotient of
an analogous algebra that is étale over $A$.

Indeed, take $\mathcal{O}' = {{B'_{\mathfrak{n}}}'}$, where $B' = A[t]/FA[t]$ and where $\mathfrak{n}'$ is the inverse image
of $\mathfrak{n}$ in $B'$.

**Corollary.**

<!-- label: I.7.8 -->

<!-- original page 12 -->

Let $f: X \to Y$ be a morphism of finite type, and let $x \in X$. For $f$ to be net at $x$, it is necessary and
sufficient that there exist an open neighborhood $U$ of $x$ such that $f|U$ factors as $U \to X' \to Y$, where the first
arrow is a closed immersion and the second is an étale morphism.

This is a simple translation of I.7.7.

Let us show how the jargon of I.7.6 follows from the principal statement: indeed, by I.7.7 there exists an epimorphism
$\mathcal{O}' \to \mathcal{O}$, where $\mathcal{O}$ has the required properties; but since $\mathcal{O}'$ and
$\mathcal{O}$ are étale over $A$, the morphism $\mathcal{O}' \to \mathcal{O}$ is étale by I.4.8, hence an isomorphism.

### Proof of I.7.6

This repeats a proof from Chevalley's seminar. By the Main Theorem, one will have $\mathcal{O} = B_{\mathfrak{n}}$,
where $B$ is a finite algebra over $A$ and $\mathfrak{n}$ is a maximal ideal of $B$. Then
$B/\mathfrak{n} = K(\mathcal{O})$ is a separable, hence monogenic, extension of $k$. If $\mathfrak{n}_{i}$,
$1 \leq i \leq r$, are the maximal ideals of $B$ distinct from $\mathfrak{n}$, there therefore exists an element $u$ of
$B$ that belongs to all the $\mathfrak{n}_{i}$ and whose image in $B/\mathfrak{n}$ is a generator. But
$B/\mathfrak{n} = B_{\mathfrak{n}}/\mathfrak{n}B_{\mathfrak{n}} = B_{\mathfrak{n}}/\mathfrak{m}B_{\mathfrak{n}}$, where
$\mathfrak{m}$ is the maximal ideal of $A$. Let us admit for a moment the following lemma.

**Lemma.**

<!-- label: I.7.9 -->

Let $A$ be a local ring, $B$ a finite algebra over $A$, $\mathfrak{n}$ a maximal ideal of $B$, and $u$ an element of $B$
whose image in $B_{\mathfrak{n}}/\mathfrak{m}B_{\mathfrak{n}}$ generates it as an algebra over $k = A/\mathfrak{m}$, and
which lies in every maximal ideal of $B$ distinct from $\mathfrak{n}$. Let $B' = B[u]$ and
$\mathfrak{n}' = \mathfrak{n}B'$. Then the canonical homomorphism ${{B'_{\mathfrak{n}}}'} \to B_{\mathfrak{n}}$ is an
isomorphism.

**Lemma.**

<!-- label: I.7.10 -->

(This should have appeared as a corollary to I.7.1, before I.7.5, which it implies.) Let $B$ be a finite algebra over
$A$ generated by an element $u$, and let $\mathfrak{n}$ be a maximal ideal of $B$ such that $B_{\mathfrak{n}}$ is
unramified over $A$. Then there exists a monic polynomial $F \in A[t]$ such that $F(u) = 0$ and
$F'(u) \notin \mathfrak{n}$.

Indeed, let $n$ be the rank of the $k$-algebra $L = B \otimes_{A} k$. By Nakayama, there exists a monic polynomial of
degree $n$ in `A[t]` such that $F(u) = 0$. Let $f$ be the polynomial deduced from $F$ by reduction mod $\mathfrak{m}$.
Then $L$ is $k$-isomorphic to $k[t]/fk[t]$, hence by I.7.3, $f'(\xi)$ is not contained in the maximal ideal of $L$
corresponding to $\mathfrak{n}$, where $\xi$ denotes the image of $t$ in $L$, i.e. the image of $u$ in $L$. Since
$f'(\xi)$ is the image of $F'(u)$, we are done.

<!-- original page 13 -->

Theorem I.7.6 now follows by combining I.7.9 and I.7.10. It remains to prove I.7.9. Put $S' = B' - \mathfrak{n}'$, so
$B'S'^{-1} = {{B'_{\mathfrak{n}}}'}$. Similarly let $S = B - \mathfrak{n}$, so $BS^{-1} = B_{\mathfrak{n}}$. We therefore
have a natural homomorphism $B S'^{-1} \to BS^{-1} = B_{\mathfrak{n}}$. Let us prove that it is an isomorphism, i.e.
that the elements of $S$ are invertible in $B S'^{-1}$, i.e. that every maximal ideal $\mathfrak{p}$ of the latter does
not meet $S$, i.e. induces $\mathfrak{n}$ on $B$.

Indeed, since $B S'^{-1}$ is finite over $B'S'^{-1} = {{B'_{\mathfrak{n}}}'}$, $\mathfrak{p}$ induces the unique maximal
ideal $\mathfrak{n}'{{B'_{\mathfrak{n}}}'}$ of ${{B'_{\mathfrak{n}}}'}$, hence induces the maximal ideal $\mathfrak{n}'$ of
$B'$. Since $B$ is finite over $B'$, the ideal $\mathfrak{q}$ of $B$ induced by $\mathfrak{p}$, lying over
$\mathfrak{n}'$, is necessarily maximal and does not contain $u$, hence is identical with $\mathfrak{n}$. Here we have
just used that $u$ belongs to every maximal ideal of $B$ distinct from $\mathfrak{n}$.

Let us now prove that $B S'^{-1}$ equals $B'S'^{-1}$. Since it is finite over the latter, Nakayama reduces us to proving
equality modulo $\mathfrak{n}'B S'^{-1}$, and a fortiori it suffices to prove equality modulo $\mathfrak{m}B S'^{-1}$.
But

```text
B S′⁻¹ / 𝔪B S′⁻¹ = B_𝔫 / 𝔪B_𝔫
```

is generated over $k$ by $u$, using here the other property of $u$. Thus the image of $B'$, and a fortiori of
$B'S'^{-1}$, in it is everything, as a subring containing $k$ and the image of $u$.

**Remark.** One should be able to state Theorem I.7.6 for a ring $\mathcal{O}$ that is only semilocal, so as also to
cover I.7.5: one would make the hypothesis that $\mathcal{O}/\mathfrak{m}\mathcal{O}$ is a monogenic $k$-algebra. One
could then find $u \in B$ whose image in $B/\mathfrak{m}B$ is a generator and which belongs to all maximal ideals of $B$
not coming from $\mathcal{O}$. Lemmas I.7.9 and I.7.10 should adapt without difficulty. More generally, ...

## 8. Infinitesimal Lifting of Étale Schemes. Application to Formal Schemes

<!-- label: I.8 -->

**Proposition.**

<!-- label: I.8.1 -->

Let $Y$ be a prescheme, $Y_{0}$ a subprescheme, $X_{0}$ an étale $Y_{0}$-scheme, and $x$ a point of $X_{0}$. Then there
exists an étale $Y$-scheme $X$, a neighborhood $U_{0}$ of $x$ in $X_{0}$, and a $Y_{0}$-isomorphism
$U_{0} \cong X \times_{Y} Y_{0}$.

Indeed, let $y$ be the projection of $x$ in $Y_{0}$. Applying I.7.6 to the étale local homomorphism $A_{0} \to B_{0}$ of
the local rings of $y$ and $x$ in $Y_{0}$ and $X_{0}$, one finds an isomorphism

```text
B₀ = (C₀)_{𝔫₀},     C₀ = A₀[t]/F₀A₀[t],
```

where $F_{0}$ is a monic polynomial and $\mathfrak{n}_{0}$ is a maximal ideal of $C_{0}$ not containing the class of
$F'_{0}(t)$ in $C_{0}$. Let $A$ be the local ring of $y$ in $Y$, let $F$ be a monic polynomial in `A[t]` giving $F_{0}$
under the surjective homomorphism $A \to A_{0}$, by lifting the coefficients of $F_{0}$, and finally let
$C = A[t]/FA[t]$, and let $\mathfrak{n}$ be the maximal ideal of $C$ which is the inverse image of $\mathfrak{n}_{0}$
under the natural epimorphism $C \to C \otimes_{A} A_{0} = C_{0}$. Put $B = C_{\mathfrak{n}}$. It is immediate by
construction and I.7.1 that $B$ is étale over $A$, and that one has an isomorphism $B \otimes_{A} A_{0} = A_{0}$.

One knows, from EGA Chapter I as indicated in the introduction, that there exists a $Y$-scheme of finite type $X$ and a
point $z$ of $X$ over $y$ such that $\mathcal{O}_{z}$ is $A$-isomorphic to $C$. Since the latter is étale over
$A = \mathcal{O}_{y}$, one may, by taking $X$ small enough, suppose that $X$ is étale over $Y$. Let
$X'_{0} = X \times_{Y} Y_{0}$. Then the local ring of $z$ in $X'_{0}$ identifies with
$\mathcal{O}_{z} \otimes_{A} A_{0} = B \otimes_{A} A_{0}$, hence is isomorphic to $B_{0}$. This isomorphism is defined
by an isomorphism from a neighborhood $U_{0}$ of $x$ in $X_{0}$ onto a neighborhood of $z$ in $X'_{0}$, and by taking
$X$ small enough one may suppose this neighborhood identical with $X'_{0}$. We are done.

**Corollary.**

<!-- label: I.8.2 -->

There is an analogous statement for étale coverings, assuming the residue field $\kappa(y)$ infinite.

The proof is the same, with I.7.5 replacing I.7.6.

**Theorem.**

<!-- label: I.8.3 -->

The functor considered in I.5.5 is an equivalence of categories.

By Theorem I.5.5, it remains to show that every étale $S_{0}$-scheme $X_{0}$ is isomorphic to an $S_{0}$-scheme
$X \times_{S} S_{0}$, where $X$ is an étale $S$-scheme. The underlying topological space of $X$ must necessarily be
identical with that of $X_{0}$, with $X_{0}$ furthermore identifying with a closed subprescheme of $X$.

The problem is therefore equivalent to the following one: find on the underlying topological space $|X_{0}|$ of $X_{0}$
a sheaf of algebras $\mathcal{O}_{X}$ over `f₀⁎(𝒪_S)`, where $f_{0}$ is the projection $X_{0} \to S_{0}$, here regarded
as a continuous map of underlying spaces, making $|X_{0}|$ into an étale $S$-prescheme $X$, together with a homomorphism
of algebras $\mathcal{O}_{X} \to \mathcal{O}_{X_{0}}$, compatible with the homomorphism `f₀⁎(𝒪_S) → f₀⁎(𝒪_{S₀})` on the
sheaves of scalars, and inducing an isomorphism

```text
𝒪_X ⊗_{f₀⁎(𝒪_S)} f₀⁎(𝒪_{S₀}) ≅ 𝒪_{X₀}.
```

Then $X$ will be an étale $S$-prescheme reducing to $X_{0}$.

<!-- original page 15 -->

Thus $X$ will be separated over $S$, since $X_{0}$ is separated over $S_{0}$, and $X$ answers the question. Moreover, if
$(U_{i})$ is a covering of $X_{0}$ by open subsets, and if one has found a solution of the problem in each $U_{i}$, then
it follows from the uniqueness theorem I.5.5 that these solutions glue, i.e. that the sheaves of algebras defining them,
equipped with their augmentation homomorphisms, glue; one immediately checks that the locally ringed space thereby
constructed over $S$ is an étale $S$-prescheme $X$ equipped with an isomorphism $X \times_{S} S_{0} \cong X_{0}$. It
therefore suffices to find a solution locally, which is assured by I.8.1.

**Corollary.**

<!-- label: I.8.4 -->

Let $S$ be a locally noetherian formal prescheme, equipped with an ideal of definition $J$, and let
$S_{0} = (|S|, \mathcal{O}_{S}/J)$ be the corresponding ordinary prescheme. Then the functor
$\mathfrak{X} \mapsto \mathfrak{X} \times_{S} S_{0}$ from the category of étale coverings of $S$ to the category of
étale coverings of $S_{0}$ is an equivalence of categories.

Of course, by an étale covering of a formal prescheme $S$ we mean a covering of $S$, i.e. a formal prescheme over $S$
defined by a coherent sheaf $\mathcal{B}$ of algebras, such that $\mathcal{B}$ is locally free and such that the residue
fibers $\mathcal{B}_{s} \otimes_{\mathcal{O}_{s}} \kappa(s)$ of $\mathcal{B}$ are separable algebras over $\kappa(s)$.
If $S_{n}$ denotes the ordinary prescheme $(|S|, \mathcal{O}_{S}/J^{n+1})$, the data of a coherent sheaf of algebras
$\mathcal{B}$ on $S$ is equivalent to the data of a sequence of coherent sheaves of algebras $\mathcal{B}_{n}$ on the
$S_{n}$, equipped with a transitive system of homomorphisms $\mathcal{B}_{m} \to \mathcal{B}_{n}$, for $m \geq n$,
defining isomorphisms

```text
𝓑_m ⊗_{𝒪_{S_m}} 𝒪_{S_n} ≅ 𝓑_n.
```

It is immediate that $\mathcal{B}$ is locally free if and only if the $\mathcal{B}_{n}$ on the $S_{n}$ are locally free,
and that the separability condition is satisfied if and only if it is satisfied for $\mathcal{B}_{0}$, or equivalently
for all the $\mathcal{B}_{n}$. Thus $\mathcal{B}$ is étale over $S$ if and only if the $\mathcal{B}_{n}$ over the
$S_{n}$ are étale. Taking this into account, I.8.4 follows at once from I.8.3.

**Remark.** It was not necessary in I.8.4 to restrict to the case of coverings. It is, however, the only case used for
the moment.

## 9. Permanence Properties

<!-- label: I.9 -->

Let $A \to B$ be a local and étale homomorphism. We examine here a few cases where a certain property of $A$ implies the
same property for $B$, or conversely.

<!-- original page 16 -->

A certain number of such propositions are already consequences of the simple fact that $B$ is quasi-finite and flat over
$A$, and we shall limit ourselves to "recalling" a few of them: $A$ and $B$ have the same Krull dimension and the same
depth, "cohomological codimension" in Serre's still-current terminology. It follows, for example, that $A$ is
Cohen-Macaulay if and only if $B$ is Cohen-Macaulay.

Moreover, for every prime ideal $\mathfrak{q}$ of $B$ inducing $\mathfrak{p}$ on $A$, $B_{\mathfrak{q}}$ will again be
quasi-finite and flat over $A_{\mathfrak{p}}$, provided $B$ is assumed to be a localization of an algebra of finite type
over $A$; this follows from the fact that the set of points where a morphism of finite type is quasi-finite,
respectively flat, is open. And moreover every prime ideal $\mathfrak{p}$ of $A$ is induced by a prime ideal
$\mathfrak{q}$ of $B$, because $B$ is faithfully flat over $A$. It follows for example that $\mathfrak{p}$ and
$\mathfrak{q}$ have the same rank, and also that $A$ has no embedded prime ideal if and only if $B$ has none.

We shall therefore restrict ourselves to propositions more special to the case of étale morphisms.

**Proposition.**

<!-- label: I.9.1 -->

Let $A \to B$ be a local étale homomorphism. For $A$ to be regular, it is necessary and sufficient that $B$ be regular.

Indeed, let $k$ be the residue field of $A$, and $L$ that of $B$. Since $B$ is flat over $A$ and $L = B \otimes_{A} k$,
i.e. $\mathfrak{n} = \mathfrak{m}B$, where $\mathfrak{m}$ and $\mathfrak{n}$ are the maximal ideals of $A$ and $B$, the
$\mathfrak{m}$-adic filtration on $B$ is identical with its $\mathfrak{n}$-adic filtration, and one will have

```text
gr*(B) = gr*(A) ⊗_k L.
```

It follows that $gr*(B)$ is a polynomial algebra over $L$ if and only if $gr*(A)$ is a polynomial algebra over $k$. This
proves the assertion. Note that we did not use the fact that $L/k$ is separable.

**Corollary.**

<!-- label: I.9.2 -->

Let $f: X \to Y$ be an étale morphism. If $Y$ is regular, then $X$ is regular; the converse is true if $f$ is
surjective.

**Proposition.**

<!-- label: prop:I.9.2 -->

Let $f: X \to Y$ be an étale morphism. If $Y$ is reduced, then so is $X$; the converse is true if $f$ is surjective.

This is equivalent to:

**Corollary.**

<!-- label: I.9.3 -->

<!-- original page 17 -->

Let $f: A \to B$ be a local étale homomorphism, with $B$ isomorphic to a localized $A$-algebra of an $A$-algebra of
finite type. For $A$ to be reduced, it is necessary and sufficient that $B$ be reduced.

Necessity is trivial, since $A \to B$ is injective, $B$ being faithfully flat over $A$. For sufficiency, let
$\mathfrak{p}_{i}$ be the minimal prime ideals of $A$. By hypothesis the natural map
$A \to \prod_{i} A/\mathfrak{p}_{i}$ is injective; tensoring with the flat $A$-module $B$, one finds that
$B \to \prod_{i} B/\mathfrak{p}_{iB}$ is injective, and one is reduced to proving that the $B/\mathfrak{p}_{iB}$ are
reduced. Since $B/\mathfrak{p}_{iB}$ is étale over $A/\mathfrak{p}_{i}$, one is reduced to the case where $A$ is
integral.

Let $K$ be its field of fractions. Since $A \to K$ is injective, the same is true, $B$ being $A$-flat, of
$B \to B \otimes_{A} K$; we are reduced to proving that this latter ring is reduced. But $B$, being a localization of an
$A$-algebra of finite type over $A$, is the local ring of a point $x$ of a scheme $X = \operatorname{Spec}(C)$ of finite
type and étale over $Y = \operatorname{Spec}(A)$. Thus $B \otimes_{A} K$ is a localized ring, with respect to a suitable
multiplicatively stable set, of the ring $C \otimes_{A} K$ of $X \otimes_{A} K$. Since $X \otimes_{A} K$ is étale over
$K$, its ring is a finite product of fields, separable extensions of $K$, and the same is therefore true of
$B \otimes_{A} K$. This proves the assertion.

**Corollary.**

<!-- label: I.9.4 -->

Let $f: A \to B$ be a local étale homomorphism, and suppose $A$ analytically reduced, i.e. the completion `Â` of $A$ has
no nilpotent elements. Then $B$ is analytically reduced, and a fortiori reduced.

Indeed, $\hat{B}$ is finite and étale over `Â`, and one applies I.9.3.

**Theorem.**

<!-- label: I.9.5 -->

Let $f: A \to B$ be a local homomorphism, with $B$ isomorphic to a localized algebra of an $A$-algebra of finite type.
Then:

1. If $f$ is étale, $A$ is normal if and only if $B$ is normal.
1. If $A$ is normal, $f$ is étale if and only if $f$ is injective and net; then $B$ is normal by (i).

We shall give two different proofs of (i). The first uses some properties of quasi-finite flat morphisms, recalled at
the beginning of this number, without using I.7.6, and hence without using the Main Theorem; for the second proof the
reverse is true. Finally, for (ii), it seems that one needs the Main Theorem in any case.

### First Proof

We use the following necessary and sufficient condition for normality of a noetherian local ring $A$ of nonzero
dimension.

<!-- original page 18 -->

**Serre's Criterion.** (i) For every prime ideal $\mathfrak{p}$ of $A$ of rank 1, $A_{\mathfrak{p}}$ is normal, or
equivalently regular. (ii) For every prime ideal $\mathfrak{p}$ of $A$ of rank $\geq 2$,
$depth A_{\mathfrak{p}} \geq 2$.[^I-9-1]

We shall admit this criterion here; it is supposed to appear in the paragraph on flat morphisms. Its principal advantage
is that it does not suppose a priori that $A$ is reduced, nor a fortiori integral. Here, we may already suppose
$\dim A = \dim B \neq 0$.

By the reminders at the beginning of this number, the prime ideals $\mathfrak{p}$ of $A$ of rank 1, respectively of rank
$\geq 2$, are exactly the traces on $A$ of the prime ideals $\mathfrak{q}$ of $B$ of rank 1, respectively of rank
$\geq 2$. Finally, if $\mathfrak{p}$ and $\mathfrak{q}$ correspond, $B_{\mathfrak{q}}$ is étale over $A_{\mathfrak{p}}$,
hence has the same depth as $A_{\mathfrak{p}}$, and is regular if and only if $A_{\mathfrak{p}}$ is regular, by I.9.1.
Applying Serre's criterion, one finds that $A$ is normal if and only if $B$ is.

### Second Proof

Suppose $B$ normal, let $L$ be its field of fractions, and $K$ that of $A$; $A$ is integral since $B$ is. We saw in the
proof of I.9.3 that $B \otimes_{A} K$ is a finite product of fields. Since it is contained in $L$, it is a field, and
since it contains $B$, it is $L$. An element of $K$ integral over $A$ is integral over $B$, hence lies in $B$ since $B$
is normal, and therefore lies in $A$ because $B \cap K = A$, as follows from the fact that $B$ is faithfully flat over
$A$.

Now suppose $A$ normal, and prove that $B$ is normal. By I.7.6 one has $B = B'_{\mathfrak{n}}$, where $B' = A[t]/FA[t]$,
with $F$ and $\mathfrak{n}$ as in I.7.6. Thus $L = B \otimes_{A} K$ will be a localization of
$B' \otimes_{A} K = K[t]/FK[t]$, and a product of fields, finite separable extensions of $K$. This latter product, as
happens whenever one localizes an artinian ring, here $B'_{K}$ with respect to a multiplicatively stable set, is a
direct factor of $B'_{K}$, hence corresponds to a decomposition $F = F_{1}F_{2}$ in `K[t]`, with the generator of $L$
corresponding to $t$ already annihilated by $F_{1}$.

But since $A$ is normal, the $F_{i}$ lie in `A[t]`, assuming them monic. Observing that $B \to L = B \otimes_{A} K$ is
injective, since $A \to K$ is injective and $B$ is flat over $A$, it follows that one already has $F_{1}(u) = 0$, with
$u$ the class of $t$ in $L$. If $F$ has been chosen of minimal degree, it follows that $F_{2} = 1$. Note that
$F'(u) = F'_{1}(u)F_{2}(u) + F_{1}(u)F'_{2}(u) = F'_{1}(u)F_{2}(u)$, since $F_{1}(u) = 0$; hence $F'_{1}(u) \neq 0$
since $F'(u) \neq 0$.

<!-- original page 19 -->

Thus one has

```text
(*)  L = B ⊗_A K = K[t]/FK[t],
```

and $F$ is consequently a separable polynomial in `K[t]`, though evidently not necessarily in `A[t]`. Note that for the
moment, one has only shown, essentially, that in I.7.6 one can choose $F$ and $\mathfrak{n}$ in such a way that, with
the notation used here, $B' \to B'_{\mathfrak{n}} = B$ is injective. We used the normality of $A$ for this; I do not
know whether it remains true without the normality hypothesis.

Recall now the well-known lemma, extracted from Serre's course of last year.

**Lemma.**

<!-- label: I.9.6 -->

Let $K$ be a ring, $F \in K[t]$ a monic separable polynomial, $L = K[t]/FK[t]$, and $u$ the class of $t$ in $L$, so that
$F'(u)$ is an invertible element of $L$. Then one has the following formulas, where $n = deg F$:

```text
tr_{L/K}(uⁱ/F′(u)) = 0    if 0 ≤ i < n − 1,
tr_{L/K}(uⁿ⁻¹/F′(u)) = 1.
```

**Corollary.**

<!-- label: I.9.7 -->

The determinant of the matrix

$$
(u^{j} \cdot u^{i}/F'(u))_{0\leq i,j\leq n-1}
$$

is equal to $(-1)^{n(n-1)}/^{2}$, hence is invertible in every subring $A$ of $K$.

**Corollary.**

<!-- label: I.9.8 -->

Let $A$ be a subring of $K$, let $V$ be the $A$-module generated by the $u^{i}$, $0 \leq i \leq n - 1$, in $L$, and let
$V'$ be the sub-$A$-module of $L$ formed by the $x \in L$ such that $tr_{L/K}(xy) \in A$ for every $y \in V$, i.e. for
$y$ of the form $u^{i}$, $0 \leq i \leq n - 1$. Then $V'$ is the $A$-module having as basis the $u^{i}/F'(u)$,
$0 \leq i \leq n - 1$.

**Corollary.**

<!-- label: I.9.9 -->

Suppose $K$ is the field of fractions of a normal integral ring $A$, and that $F$ has its coefficients in $A$. Then,
with the notation of I.9.8, $V'$ contains the normal closure $A'$ of $A$ in $L$, which is therefore contained in
$A[u]/F'(u)$, and a fortiori in $A[u][F'(u)^{-1}]$.

Apply this last corollary to the situation obtained in the proof: since $F'(u)$ is invertible in $B$, which contains
`A[u]`, $B$ contains $A'$. By the Main Theorem, or from the fact that $B = A[u]_{\mathfrak{n}}$, $B$ is a localized
algebra of $A'$. Since $A'$ is normal, so is $B$.

### Proof of (ii)

<!-- original page 20 -->

Proceed as in the preceding proof to show that in I.7.6 one can choose $F$ in such a way that `(*)` still holds. The
only a priori obstacle is that, $B$ no longer being assumed flat over $A$, one can no longer assert that $B \to L$ is
injective, so the reasoning applies a priori only to the image $B_{1}$ of $B$ under that homomorphism. It follows at
once that $B_{1}$ is flat over $A$, as a localization of a free algebra over $A$. By I.4.8 the morphism $B \to B_{1}$ is
étale, hence an isomorphism, which completes the proof.

From the editorial point of view, the last two proofs should be interchanged, and the formal computations of the lemma
and its corollaries should be put in a separate number.

**Corollary.**

<!-- label: I.9.10 -->

Let $f: X \to Y$ be an étale morphism. If $Y$ is normal, then $X$ is normal; the converse is true if $f$ is surjective.

**Corollary.**

<!-- label: I.9.11 -->

Let $f: X \to Y$ be a dominant morphism, with $Y$ normal and $X$ connected. If $f$ is net, then $f$ is étale; hence $X$
is normal and therefore, being connected, irreducible.

Let $U$ be the set of points where $f$ is étale. It is open, and it suffices to show that it is also closed and
nonempty. The set $U$ contains the inverse image of the generic point of $Y$, since for an algebra over a field,
unramified equals étale; hence, since $X$ dominates $Y$, $U$ is nonempty. If $x$ belongs to the closure of $U$, then it
belongs to the closure of an irreducible component $U_{i}$ of $U$, hence to an irreducible component
$X_{i} := closure(U_{i})$ of $X$ that meets $U$, and therefore dominates $Y$, since every component of $U$, being flat
over $Y$, dominates $Y$. Consequently, if $y$ is the projection of $x$ to $Y$, $\mathcal{O}_{y} \to \mathcal{O}_{x}$ is
injective, taking into account that $\mathcal{O}_{y}$ is integral. Since $\mathcal{O}_{y}$ is normal and
$\mathcal{O}_{y} \to \mathcal{O}_{x}$ is net, one concludes using I.9.5(ii).

**Corollary.**

<!-- label: I.9.12 -->

Let $f: X \to Y$ be a dominant morphism of finite type, with $Y$ normal and $X$ irreducible. Then the set of points
where $f$ is étale is identical with the complement of the support of $\Omega^{1}_{X/Y}$, i.e. with the complement of
the subprescheme of $X$ defined by the different ideal $\mathfrak{d}_{X/Y}$.

<!-- original page 21 -->

This is the "less trivial" statement alluded to in the remark in no. I.4.

**Remark.** One should be careful not to believe that a connected étale covering of an irreducible scheme is itself
irreducible, when the base is not assumed normal. This question will be studied in no. I.11.

## 10. Étale Coverings of a Normal Scheme

<!-- label: I.10 -->

**Proposition.**

<!-- label: I.10.1 -->

Let $X$ be a prescheme étale and separated over a connected normal $Y$ with field $K$. Then the connected components
$X_{i}$ of $X$ are integral, their fields $K_{i}$ are finite separable extensions of $K$, and $X_{i}$ identifies with a
nonempty open part of the normalization of $Y$ in $K_{i}$; hence $X$ identifies with a dense open part of the
normalization of $Y$ in $R(X) = L = \prod K_{i}$.

By I.9.10, $X$ is normal; a fortiori its local rings are integral, so the connected components of $X$ are irreducible.
Since $X_{i}$ is normal, and finite and dominant over $Y$, it follows from a special case, almost trivial moreover, of
the Main Theorem that $X_{i}$ is an open subset of the normalization of $Y$ in the field $K_{i}$ of $X$.

**Corollary.**

<!-- label: I.10.2 -->

Under the conditions of I.10.1, $X$ is finite over $Y$, i.e. an étale covering of $Y$, if and only if $X$ is isomorphic
to the normalization $Y'$ of $Y$ in $L = R(X)$, the ring of rational functions on $X$.

Indeed, one knows that this normalization is finite over $Y$, since $Y$ is normal and $R/K$ is separable. Conversely, if
$X$ is finite over $Y$, it is finite over $Y'$, so its image in $Y'$ is closed; on the other hand it is dense.

An algebra $L$ of finite rank over $K$ will be said to be unramified over $X$, or simply unramified over $K$ if $X$ is
understood, if $L$ is a separable algebra over $K$, i.e. a direct product of separable extensions $K_{i}$, and if the
normalization $Y'$ of $Y$ in $L$, the disjoint sum of the normalizations of $Y$ in the $K_{i}$, is unramified, hence
étale by I.9.11, over $Y$. Thus:

**Corollary.**

<!-- label: I.10.3 -->

For every $X$ finite over $Y$ and such that every irreducible component dominates $Y$, let $R(X)$ be the ring of
rational functions on $X$, the product of the local rings of the generic points of the irreducible components of $X$.

<!-- original page 22 -->

Thus $X \mapsto R(X)$ is a functor, with values in algebras of finite rank over $K = R(Y)$. This functor establishes an
equivalence from the category of connected étale coverings of $Y$ to the category of extensions $L$ of $K$ unramified
over $Y$.

The inverse functor is the normalization functor.

Suppose $Y$ affine, hence defined by a normal ring $A$ with field of fractions $K$. Let $L$ be a finite extension of $K$
that is a direct product of fields. Then, by definition, the normalization $Y'$ of $Y$ in $L$ is isomorphic to
$\operatorname{Spec}(A')$, where $A'$ is the normalization of $A$ in $L$. Saying that $L$ is unramified over $Y$ means
that $A'$ is unramified, or equivalently étale, over $A$. If $A$ is local, this is equivalent to saying that the local
rings $A'_{\mathfrak{n}}$, where $\mathfrak{n}$ runs through the finite set of maximal ideals of $A'$, i.e. of its prime
ideals inducing the maximal ideal $\mathfrak{m}$ of $A$, are unramified, hence étale, over the local ring $A$.

Finally, note also that the discriminant criterion I.4.10 can also be applied in this situation. More generally, a
variant of that criterion should be stated as follows, without a preliminary flatness condition when $X$ dominates $Y$,
though $Y$ is still assumed locally integral: $A \to B$ and $B \to B \otimes_{A} K = L$ are injective, so $tr_{L/K}$ is
defined, and $tr_{L/K}(xy)$ induces a fundamental bilinear form $B \times B \to A$, i.e. there exist $x_{i} \in B$,
$1 \leq i \leq n$, with $n$ the rank of $L$ over $K$, such that `tr(x_ix_j) ∈ A` for all `i, j`, and `det(tr(x_ix_j))`
is invertible in $A$.

The sorites I.4.6 immediately imply the sorites of unramifiedness in the classical setting.

**Proposition.**

<!-- label: I.10.4 -->

Let $Y$ be a normal integral prescheme, with field $K$.

1. $K$ is unramified over $Y$.
1. If $L$ is an extension of $K$ unramified over $Y$, if $Y'$ is a normal prescheme with field $L$ and dominating $Y$,
   for example the normalization of $Y$ in $L$, and if $M$ is an extension of $L$ unramified over $Y'$, then $M/K$ is
   unramified over $Y$. This is the transitivity of unramifiedness.
1. Let $Y'$ be a normal integral prescheme dominating $Y$, with field $K'/K$. If $L$ is an extension of $K$ unramified
   over $Y$, then $L \otimes_{K} K'$ is an extension of $K'$ unramified over $Y'$. This is the translation property.

<!-- original page 23 -->

Moreover:

**Corollary.**

<!-- label: I.10.5 -->

Under the conditions of (iii), if $Y = \operatorname{Spec}(A)$ and $Y' = \operatorname{Spec}(A')$, then the
normalization $\bar{A}'$ of $Y'$ in $L' = L \otimes_{K} K'$ identifies with $\bar{A} \otimes_{A} A'$, where `Ā` is the
normalization of $A$ in $L$.

Usually, people, who are reluctant to consider nonintegral rings, even when they are direct products of fields, state
the translation property in the following weaker form:

**Corollary.**

<!-- label: I.10.6 -->

Under the conditions of (iii), let $L_{1}$ be a compositum of $L/K$, unramified over $Y$, and $K'/K$. Then $L_{1}/K'$ is
unramified over $Y'$. In the case where $Y = \operatorname{Spec}(A)$, $Y' = \operatorname{Spec}(A')$, one furthermore
has

$$
\bar{A}' = A[\bar{A}, A'],
$$

i.e. the normalized ring $\bar{A}'$ of $A'$ in $L_{1}$ is the $A$-algebra generated by $A'$ and the normalization `Ā` of
$A$ in $L$.

This last fact is false without the unramifiedness hypothesis, even in the case of composita of number fields.

To finish this number, we shall give the interpretation of the notion of étale covering corresponding to the intuitive
image of that notion: there should be the "maximum number" of points over the point under consideration $y \in Y$, and
in particular there should not be "several points merged together" over $y$. To prove the results in this direction with
all desirable generality, we shall admit here Proposition I.10.7 below, whose proof will be in the multiplodocus,
Chapter IV, paragraph 15, and uses Chevalley's technique of constructible sets and a little descent theory.

A morphism of finite type $f: X \to Y$ is said to be universally open if for every base extension $Y' \to Y$, with $Y'$
locally noetherian, the morphism $f': X' = X \times_{Y} Y' \to Y'$ is open, i.e. sends open sets to open sets. One may
moreover restrict to the case where $Y'$ is of finite type over $Y$, and even where $Y'$ is of the form
$Y[t_{1},...,t_{r}]$, with the $t_{i}$ indeterminates.

A universally open morphism is a fortiori open, the converse being false. On the other hand, if $f$ is open, with $X$
and $Y$ irreducible, then all components of all fibers of $f$ have the same dimension, namely the dimension of the
generic fiber

<!-- original page 24 -->

$f^{-1}(z)$, where $z$ is the generic point of $Y$. Finally, if $Y$ is normal, this latter condition already implies
that $f$ is universally open, by Chevalley's theorem. It follows, for example, that if $f: X \to Y$ is a quasi-finite
morphism, with $Y$ normal and irreducible, then $f$ is universally open, or simply open, if and only if every
irreducible component of $X$ dominates $Y$. Recall also that a flat morphism of finite type, being open, is also
universally open. With these preliminaries in place, "recall":

**Proposition.**

<!-- label: I.10.7 -->

Let $f: X \to Y$ be a quasi-finite, separated, universally open morphism. For every $y \in Y$, let $n(y)$ be the
"geometric number of points of the fiber $f^{-1}(y)$", equal to the sum of the separable degrees of the residue
extensions $\kappa(x)/\kappa(y)$, for $x \in f^{-1}(y)$. Then the function $y \mapsto n(y)$ on $Y$ is upper
semicontinuous. For it to be constant in a neighborhood of the point $y$, i.e. for $n(y) = n(z_{i})$, where the $z_{i}$
are the generic points of the irreducible components of $Y$ containing $y$, it is necessary that there exist a
neighborhood $U$ of $y$ such that $X|U$ is finite over $U$.[^I-10-1]

**Corollary.**

<!-- label: I.10.8 -->

If $y \mapsto n(y)$ is constant and $Y$ is geometrically unibranch,[^I-10-2] then the irreducible components of $X$ are
disjoint.

**Proposition.**

<!-- label: I.10.9 -->

Let $f: X \to Y$ be an étale separated morphism. With the notation of I.10.7, the function $y \mapsto n(y)$ is upper
semicontinuous. For it to be constant in a neighborhood of the point $y$, i.e. for $n(y) = n(z_{i})$, where the $z_{i}$
are the generic points of the irreducible components of $Y$ containing $y$, it is necessary and sufficient that there
exist an open neighborhood $U$ of $y$ such that $X|U$ is finite over $U$, i.e. is an étale covering of $U$.

**Corollary.**

<!-- label: I.10.10 -->

For an étale separated morphism $f: X \to Y$, with $Y$ connected, to be finite, i.e. to make $X$ an étale covering of
$Y$, it is necessary and sufficient that all fibers of $f$ have the same geometric number of points.

In I.10.7 and its corollary, there was no normality hypothesis on $Y$. If one makes such a hypothesis, one finds the
stronger statement, most often taken as the definition of unramifiedness of a covering:

**Theorem.**

<!-- label: I.10.11 -->

<!-- original page 25 -->

Let $f: X \to Y$ be a quasi-finite separated morphism. Suppose that $Y$ is irreducible, that every component of $X$
dominates $Y$, and that $X$ is reduced, i.e. that $\mathcal{O}_{X}$ has no nilpotent elements. Let $n$ be the degree of
$X$ over $Y$, the sum of the degrees over the field $K$ of $Y$ of the fields $K_{i}$ of the irreducible components
$X_{i}$ of $X$. Let $y$ be a normal point of $Y$. Then the geometric number $n(y)$ of points of $X$ over $y$ is
$\leq n$, and equality holds if and only if there exists an open neighborhood $U$ of $y$ such that $X|U$ is an étale
covering of $U$.

The "only if" being trivial, let us prove the "if". Let $z$ be the generic point of $Y$. We have $n(z) =$ the sum of the
separable degrees of the $K_{i}/K$, hence $n(z) \leq n$; and by I.10.7 one has $n(y) \leq n(z) \leq n$, with equality
implying that $X|U$ is finite over $U$ for a suitable neighborhood $U$ of $y$. One may therefore suppose $X$ finite over
$Y$ and the function $n(y')$ on $Y$ constant. Finally, by I.10.8, $X$ is then the disjoint union of its irreducible
components, and to prove that it is unramified at $y$, one is reduced to the case where $X$ is irreducible, hence
integral. Finally, one may suppose $Y = \operatorname{Spec}(\mathcal{O}_{y})$. The theorem is then reduced to the
following classical statement:

**Corollary.**

<!-- label: I.10.12 -->

Let $A$ be a normal local ring, noetherian as always, with field $K$; let $L$ be a finite extension of $K$ of degree
$n$, with separable degree $n_{s}$; let $B$ be a subring of $L$ finite over $A$, with field of fractions $L$; let
$\mathfrak{m}$ be the maximal ideal of $A$, and let $n'$ be the separable degree of $B/\mathfrak{m}B$ over
$A/\mathfrak{m}A = k$, i.e. the sum of the separable degrees of the residue extensions of this ring. One has
$n' \leq n_{s}$ and a fortiori $n' \leq n$. This last inequality is an equality if and only if $B$ is unramified, hence
étale, over $A$.

It remains only to show that $n' = n$ implies that $B$ is étale over $A$. Recall the proof when $k$ is infinite: one
need only show that $R = B/\mathfrak{m}B$ is separable over $k$. If this were not the case, it would follow, by a known
lemma, that there exists an element $a$ of $R$ whose minimal polynomial over $k$ has degree $> n'$. This element comes
from an element $x$ of $B$, whose minimal polynomial over $K$, as an element of $L$, has degree $\leq n$. On the other
hand, this latter polynomial has its coefficients in $A$ since $A$ is normal, and therefore gives by reduction mod
$\mathfrak{m}$ a monic polynomial $F \in k[t]$, of degree $\leq n = n'$, such that $F(a) = 0$, a contradiction.

<!-- original page 26 -->

In the general case, where $k$ may be finite, returning to geometric language, consider
$Y' = \operatorname{Spec}(A[t])$, which is faithfully flat over $Y$, and the generic point $y'$ of the fiber
$\operatorname{Spec}(k[t])$ of $Y'$ over $y$. Then $X$ is net over $Y$ at $y$ if and only if
$X' = X \times_{Y} Y' = \operatorname{Spec}(B[t])$ is net at $y'$ over $Y'$, as one checks immediately. On the other
hand, by the choice of $y'$, its residue field is $k(t)$, hence infinite. Since $y'$ is a normal point of $Y'$, one is
reduced to the preceding case.

## 11. Some Complements

<!-- label: I.11 -->

We have already said that a connected étale covering of an integral scheme is not necessarily integral. Here are two
examples of this fact.

**a)** Let $C$ be an algebraic curve with an ordinary double point $x$, let $C'$ be its normalization, and let $a$ and
$b$ be the two points of $C'$ above $x$. Let $C'_{i}$, for $i = 1, 2$, be two copies of $C'$, and let $a_{i}$ and
$b_{i}$ be the points of $C'_{i}$ corresponding to $a$ and $b$ respectively. In the sum curve $C'_{1} \amalg C'_{2}$,
identify $a_{1}$ with $b_{2}$ on the one hand, and $a_{2}$ with $b_{1}$ on the other. We leave to the reader the task of
making this identification process precise; it will be explained in Chapter VI of the multiplodocus, but in the case of
curves over an algebraically closed field it is treated in Serre's book on algebraic curves.

One obtains a connected and reducible curve $C''$, which is an étale covering of degree 2 of $C$. The reader will verify
that, in general, the connected "Galois" étale coverings $C''$ of $C$ whose inverse image $C'' \times_{C} C'$ is a
trivial covering of $C'$, i.e. isomorphic to the sum of a certain number of copies of $C'$, are "cyclic" of degree $n$;
and for every integer $n > 0$, one can construct a connected cyclic étale covering of degree $n$. In the language of the
fundamental group to be developed later, this means that the quotient of $\pi_{1}(C)$ by the closed normal subgroup
generated by the image of $\pi_{1}(C') \to \pi_{1}(C)$, the homomorphism induced by the projection, is isomorphic to the
profinite completion of $\mathbb{Z}$. More precisely, one should be able to show that the fundamental group of $C$ is
isomorphic to the topological free product of the fundamental group of $C'$ with the profinite completion of
$\mathbb{Z}$. Note that questions of this kind gave rise to descent theory for schemes.

**b)** Let $A$ be a complete integral local ring. One knows that its normalization $A'$ is finite over $A$, by Nagata;
hence it is a complete semilocal ring, and therefore local since it is integral. Suppose that the residue extension
$L/k$ it defines is not radicial. Otherwise, one will say that $A$ is geometrically unibranch; cf. below. This will be
the case, for example, for the ring

$$
\mathbb{R}[[s,t]]/(s^{2}+t^{2})\mathbb{R}[[s,t]],
$$

where $\mathbb{R}$ is the field of real numbers.

Let $k'$ be a finite Galois extension of $k$ such that $L \otimes_{k} k'$ decomposes, and let $B$ be a finite étale
algebra over $A$ corresponding to the residue extension $k'$; recall that $B$ is essentially unique. Then
$B' = A' \otimes_{A} B$ over $B$ has residue algebra $L \otimes_{k} k'$, which is not local; hence $B'$ is not a local
ring, and therefore, being complete, has zero divisors.

<!-- original page 27 -->

Since $B'$ is contained in the total ring of fractions of $B$, because it is free over $A'$, hence torsion-free over
$A'$, hence torsion-free over $A$, and therefore contained in

```text
B′ ⊗_A K = B′_(K) = A′_(K) ⊗_K B_(K) = B_(K),
```

since $A'_{K} = K$, it follows that $B$ is not integral. In the case of the ring
$\mathbb{R}[[s,t]]/(s^{2}+t^{2})\mathbb{R}[[s,t]]$, taking $k'/k = \mathbb{C}/\mathbb{R}$, one obtains for $B$ the local
ring of two intersecting lines in the plane at their point of intersection.

Note moreover that if there exists a connected étale covering $X$ of an integral $Y$ that is not irreducible, then every
irreducible component of $X$ gives an example of an unramified covering $X'$ of $Y$, dominating $Y$, that is not étale
over $Y$. In the case of example a), one obtains in this way that $C'$ is unramified over $C$ without being étale at the
two points $a$ and $b$. This is also seen directly by inspecting the completions of the local rings of $x$ and $a$: from
the "formal" point of view, $C'$ at the point $a$ identifies with a closed subscheme of $C$ at the point $x$, namely one
of the two "branches" of $C$ passing through $x$.

In a) and b), one sees that the failure of the conclusions of I.9.5(i) and (ii) is directly linked to the fact that a
point of $Y$ "bursts" into distinct points of the normalization. In b), the fact that the residue extension is not
radicial must be interpreted geometrically in this way.

More precisely, we shall say that an integral local ring $A$ is geometrically unibranch if its normalization has only
one maximal ideal, the corresponding residue extension being radicial. A point $y$ of an integral prescheme is said to
be geometrically unibranch if its local ring is. Examples: a normal point, an ordinary cusp of a curve, etc.

<!-- original page 28 -->

It seems that if $Y$ has a point that is not unibranch, there always exists a connected nonirreducible étale covering of
$Y$; at least this is what we showed in case b), when $Y$ is the spectrum of a complete local ring. By contrast, one can
show that if all points of $Y$ are geometrically unibranch, then every connected unramified $Y$-prescheme dominating $Y$
is étale and irreducible. The proof repeats that of I.9.5, using the following generalization of Theorem I.8.3, which
will be proved later using descent theory:[^I-11-1]

Let $Y' \to Y$ be a finite, radicial, surjective morphism, i.e. what one might call a "universal homeomorphism".
Consider the functor $X \mapsto X \times_{Y} Y' = X'$ from $Y$-preschemes to $Y'$-preschemes. This functor induces an
equivalence from the category of étale $Y$-schemes to the category of étale $Y'$-schemes.

One may apply this result, for example, in the case where $Y'$ is the normalization of $Y$, with $Y$ assumed unibranch
and $Y'$ finite over $Y$, which is true in all cases one encounters in practice; or in the case of a $Y''$ "sandwiched"
between $Y$ and its normalization, which no longer needs to be finite over $Y$.

<!-- end of Exposé I source block: next chapter begins at smf_doc-math_3_01.tex line 2519 -->

[^I-1-1]: Cf. EGA IV 16.3.

[^I-2-1]: In EGA II 6.2.3 one assumes in addition that $f$ is of finite type.

[^I-3-1]: Cf. remorse in III 1.2.

[^I-4-1]: Cf. Exposé IV.

[^I-4-2]: Cf. remorse in III 1.2.

[^I-5-1]: Cf. IV 5.9.

[^I-9-1]: Cf. EGA IV 5.8.6.

[^I-10-1]: Cf. EGA IV 15.5.1.

[^I-10-2]: For the definition, cf. below no. I.11.

[^I-11-1]: Cf. IX 4.10. For a more direct proof, cf. EGA IV 18.10.3, using a variant of I.9.5 for geometrically
    unibranch local rings.


<!-- SOURCE: 02-morphismes-lisses-generalites-proprietes-differentielles.md -->

# Exposé II. Smooth Morphisms: Generalities, Differential Properties

<!-- label: II -->

<!-- original page 29 -->

References to Exposé I are indicated by I. Recall that rings are noetherian, and preschemes locally noetherian.

## 1. Generalities

<!-- label: II.1 -->

Let $Y$ be a prescheme, and let $t_{1},...,t_{n}$ be indeterminates. Put

```text
Y[t₁,...,t_n] = Y ⊗_ℤ ℤ[t₁,...,t_n].
```

<!-- label: eq:II.1.1 -->

Thus $Y[t_{1},...,t_{n}]$ is a $Y$-scheme, affine over $Y$, defined by the quasi-coherent sheaf of algebras
$\mathcal{O}_{Y}[t_{1},...,t_{n}]$. Giving a section of this prescheme over $Y$ is therefore equivalent to giving $n$
sections of $\mathcal{O}_{Y}$, corresponding to the images of the $t_{i}$ under the corresponding homomorphism. If $Y'$
is over $Y$, one has

```text
Y[t₁,...,t_n] ×_Y Y′ = Y′[t₁,...,t_n],
```

<!-- label: eq:II.1.2 -->

which implies that giving a $Y$-morphism from $Y'$ to $Y[t_{1},...,t_{n}]$ is equivalent to giving $n$ sections of
$\mathcal{O}_{Y'}$. On the other hand, one has

$$
(Y[t_{1},...,t_{n}])[t_{n+1},...,t_{m}] = Y[t_{1},...,t_{m}],
$$

<!-- label: eq:II.1.3 -->

by the analogous formula for polynomial rings over $\mathbb{Z}$. Formula II.1.2 implies that $Y[t_{1},...,t_{n}]$ varies
functorially with $Y$.

The prescheme $Y[t_{1},...,t_{n}]$ is of finite type and flat over $Y$.

**Definition.**

<!-- label: II.1.1 -->

Let $f: X \to Y$ be a morphism, making $X$ into a $Y$-prescheme. One says that $f$ is smooth[^II-1-1] at $x \in X$, or
that $X$ is smooth over $Y$ at $x$, if there exist an integer $n \geq 0$, an open neighborhood $U$ of $x$, and an étale
$Y$-morphism from $U$ to $Y[t_{1},...,t_{n}]$. One says that $f$, respectively $X$, is smooth if it is smooth at all
points of $X$. An algebra $B$ over a ring $A$ is said to be smooth at a prime ideal $\mathfrak{p}$ of $B$ if
$\operatorname{Spec}(B)$ is smooth over $\operatorname{Spec}(A)$ at the point $\mathfrak{p}$.

<!-- original page 30 -->

The algebra $B$ is said to be smooth over $A$ if it is smooth over $A$ at every prime ideal $\mathfrak{p}$ of $B$.
Finally, a local homomorphism $A \to B$ of local rings is said to be smooth, or $B$ is said to be smooth over
$A$,[^II-1-2] if $B$ is a localization of an algebra of finite type $B_{1}$ smooth over $A$.

Note that the notion of smoothness of $X$ over $Y$ is local on $X$ and on $Y$. If $X$ is smooth over $Y$, it is locally
of finite type over $Y$.

**Proposition.**

<!-- label: prop:II.1.1 -->

The set of points $x$ of $X$ at which $f$ is smooth is open.

This is trivial from the definition.

**Corollary.**

<!-- label: II.1.2 -->

If $B$ is smooth over $A$ at $\mathfrak{p}$, then it is smooth over $A$ at every prime ideal $\mathfrak{q}$ of $B$
contained in $\mathfrak{p}$.

Proposition II.1.1 also implies that the last two definitions II.1.1 coincide on their common domain of existence.

**Proposition.**

<!-- label: II.1.3 -->

1. An étale morphism, in particular an open immersion or an identity morphism, is smooth.
1. Base extension in a smooth morphism gives a smooth morphism.
1. The composite of two smooth morphisms is smooth.

Statement (i) is trivial from the definition; more precisely, one has:

**Corollary.**

<!-- label: II.1.4 -->

étale = quasi-finite + smooth.

Statement (ii) follows immediately from the analogous fact for étale morphisms (I 4.6) and for the projections
$Y[t_{1},...,t_{n}] \to Y$; cf. II.1.2. For (iii), it follows formally from the fact that this is separately true for
“étale” (I 4.6) and for projections of the type $Y[t_{1},...,t_{n}] \to Y$, cf. II.1.3, together with the two facts
cited for (ii).

Suppose $Y$ is smooth over $Z$ and $X$ smooth over $Y$; prove that $X$ is smooth over $Z$. We may suppose $Y$ is étale
over $Z[t_{1},...,t_{n}]$ and $X$ is étale over $Y[s_{1},...,s_{m}]$. The first hypothesis therefore implies that
$Y[s_{1},...,s_{m}]$ is étale over $Z[t_{1},...,t_{n}][s_{1},...,s_{m}] = Z[t_{1},...,s_{m}]$. Hence $X$ is étale over
$Z[t_{1},...,s_{m}]$, as required.

**Remark.**

<!-- label: II.1.5 -->

The integer $n$ appearing in Definition II.1.1 is well determined, since one checks immediately

<!-- original page 31 -->

that it is the dimension of the local ring of $x$ in its fiber $f^{-1}(f(x))$. It is called the relative dimension of
$X$ over $Y$. It behaves additively under composition of morphisms.

## 2. Some Smoothness Criteria for a Morphism

<!-- label: II.2 -->

**Theorem.**

<!-- label: II.2.1 -->

Let $f: X \to Y$ be a morphism locally of finite type, let $x \in X$, and let $y = f(x)$. For $f$ to be smooth at $x$,
it is necessary and sufficient that (a) $f$ be flat at $x$, and (b) $f^{-1}(y)$ be smooth over $\kappa(y)$ at $x$.

Since the composite of two flat morphisms is flat, and $Y[t_{1},...,t_{n}] \to Y$ is flat, one sees that smooth implies
flat. Taking II.1.3(ii) into account, this proves necessity.

Suppose (a) and (b) verified. Let $V$ be an affine neighborhood of $y$ with ring $A$, and $U$ an affine neighborhood of
$x$ over $V$, with ring $B$. Taking $U$ small enough, we may suppose by (b) that there exists an étale
$\kappa(y)$-morphism

```text
g: U|f⁻¹(y) → Spec k[t₁,...,t_n],     k = κ(y),
```

defined by $n$ sections $g_{i}$ of the structural sheaf of $U|f^{-1}(y)$. One checks easily that one may suppose the
$g_{i}$, which a priori are elements of $B \otimes_{A} k = BS^{-1}$, where $S = A - \mathfrak{p}$ and $\mathfrak{p}$ is
the prime ideal of $A$ corresponding to $y$, come from sections of the structural sheaf of $U$. Thus $g$ is induced by a
morphism, still denoted $g$,

$$
g: U \to Y[t_{1},...,t_{n}],
$$

after multiplying the $g_{i}$ by a common nonzero element of $k$ if necessary. Now $U$ is flat over $Y$ by (a), as is
$Y[t_{1},...,t_{n}]$; on the other hand, $g$ induces an étale morphism between the fibers over $y$. Hence $g$ is étale
at $x$ by I 5.8. This proves the assertion.

**Corollary.**

<!-- label: II.2.2 -->

Let $S$ be a prescheme, let $f: X \to Y$ be an $S$-morphism of finite type, with $Y$ of finite type and flat over $S$,
let $x \in X$, and let $s$ be the projection of $x$ to $S$. For $f$ to be smooth at $x$, it is necessary and sufficient
that $X$ be flat, or equivalently smooth, over $S$ at $x$, and that the morphism $f_{s}: X_{s} \to Y_{s}$ induced on the
fibers of $s$ be smooth at $x$.

Only sufficiency requires proof, and it follows from criterion II.2.1 together with the flatness criterion I 5.9.

<!-- original page 32 -->

To state the following result, “recall” that a morphism $f: X \to Y$ locally of finite type is said to be
equidimensional at the point $x \in X$ if, putting $y = f(x)$, one can find an open neighborhood $U$ of $x$, every
component of which dominates a component of $Y$, such that, for every $y' \in Y$, the irreducible components of
$f^{-1}(y') \cap U$ all have the same dimension independent of $y'$. In this condition it is enough, moreover, to take
$y'$ to be the generic points of the irreducible components of $Y$ passing through $y$, and the point $y$ itself.

If, for example, $X$ and $Y$ are integral and $f$ is dominant, the condition means that the components of $f^{-1}(y)$
passing through $x$ have the “right” dimension, i.e. the dimension of the generic fiber; recall that they are always at
least the dimension of the generic fiber. If $f$ is equidimensional at $x$, the dimension of its fiber at $x$ being $n$,
and if $g: U \to Y' = Y[t_{1},...,t_{n}]$ is a $Y$-morphism from a neighborhood $U$ of $x$, inducing on the fibers of
$y$ a morphism that is quasi-finite at $x$, or equivalently if $g$ is quasi-finite at $x$, then one shows that every
irreducible component of $U$ passing through $x$ dominates an irreducible component of $Y'$. Moreover, by the
“normalization lemma”, such a $g$ always exists. Conversely, if there exists a quasi-finite $Y$-morphism $g$ from an
open neighborhood $U$ of $x$ into a $Y$-scheme of the form $Y' = Y[t_{1},...,t_{n}]$, such that every component of $U$
passing through $x$ dominates a component of $Y'$, then $f$ is equidimensional at $x$. This said:

**Proposition.**

<!-- label: II.2.3 -->

Let $f: X \to Y$ be a morphism locally of finite type, let $x$ be a point of $X$, and let $y = f(x)$. Suppose
$\mathcal{O}_{y}$ is normal. For $f$ to be smooth at $x$, it is necessary and sufficient that $f$ be equidimensional at
$x$ and that $f^{-1}(y)$ be smooth over $\kappa(y)$ at $x$.

One sees immediately from the definition that a smooth morphism is equidimensional. Note that a flat morphism of finite
type is not necessarily equidimensional at $x$, even if its fiber at $x$ is irreducible. Let us prove the converse.
Since $f^{-1}(y)$ is smooth over $\kappa(y)$ at $x$, we may suppose, replacing $X$ if necessary by a suitable
neighborhood of $x$, that there exists a $Y$-morphism

```text
g: X → Y[t₁,...,t_n] = Y′
```

inducing an étale morphism on the fibers of $y$, and a fortiori quasi-finite at $x$.

<!-- original page 33 -->

Thus $g$ is unramified, and since $f$ is equidimensional at $x$, the irreducible components of $X$ passing through $x$
each dominate a component of $Y'$. A fortiori the homomorphism $\mathcal{O}_{y'} \to \mathcal{O}_{x}$ deduced from $g$,
where $y' = g(x)$, is injective. This homomorphism is moreover unramified, and $\mathcal{O}_{y'}$ is normal, since it is
a localization of the ring $\mathcal{O}_{y}[t_{1},...,t_{n}]$, which is normal because $\mathcal{O}_{y}$ is. Thus the
homomorphism $\mathcal{O}_{y'} \to \mathcal{O}_{x}$ is étale by I 9.5(ii).

**Remarks.**

<!-- label: II.2.4 -->

The preceding statement remains valid if one replaces the hypothesis that $\mathcal{O}_{y}$ is normal by the weaker
hypothesis that $Y$ is geometrically unibranch at $y$, cf. I 11, since I 9.5 is valid under this hypothesis. Let us take
the occasion to point out at the same time that if the residue field of an integral local ring $A$ is algebraically
closed, then analytically integral, i.e. `Â` is integral, implies geometrically unibranch. The converse is moreover true
in every category of “good rings”, more precisely in a category of rings stable under the usual operations and in which
the completion of a normal local ring is normal; this condition is fulfilled, by Zariski’s “analytic normality theorem”,
in the category of affine algebras and their localizations.[^II-2-1]

Finally, “recall” in the present context the following result, due to Hironaka,[^II-2-2] which sometimes makes it
possible to ensure that $f^{-1}(y)$ is a reduced scheme, i.e. that it is also what many algebraic geometers would
abusively regard as the fiber without multiplicity of $f$ over $x$, namely $f^{-1}(y)_{red}$:

**Proposition.**

<!-- label: II.2.5 -->

Let $f: X \to Y$ be a dominant morphism of finite type of reduced preschemes, and let $y$ be a point of $Y$ such that
$\mathcal{O}_{y}$ is regular. Suppose that all components of $f^{-1}(y)$ have multiplicity 1, cf. definition below, and
that $f^{-1}(y)_{red}$ is normal. Then $f^{-1}(y)$ is reduced, hence normal; $X$ is normal at all points of $f^{-1}(y)$;
and finally $X$ is flat over $Y$ at all points of $f^{-1}(y)$.

<!-- original page 34 -->

One says that a component $Z$ of $f^{-1}(y)$ has multiplicity 1 if, with $x$ denoting the generic point of $Z$, one has:
(i) $\dim \mathcal{O}_{x} = \dim \mathcal{O}_{y}$, i.e. $Z$ is not an “excess component”, in other words is not “of too
large a dimension”; (ii) the maximal ideal of $\mathcal{O}_{x}$ is generated by the maximal ideal of $\mathcal{O}_{y}$,
which a priori, by the choice of $x$, generates an ideal of definition of $\mathcal{O}_{x}$.

Taking II.2.3 or II.2.1 into account, one obtains:

**Corollary.**

<!-- label: II.2.6 -->

Let $f: X \to Y$ be a dominant morphism of finite type of reduced preschemes, and let $y$ be a point of $Y$ such that
$\mathcal{O}_{y}$ is regular. For $f$ to be smooth at the points of $X$ above $y$, it is necessary and sufficient that
the components of $f^{-1}(y)$ have multiplicity 1 and that $f^{-1}(y)_{red}$ be smooth over $\kappa(y)$.

This situation was considered especially in the past when $Y$ was the spectrum of a discrete valuation ring $A$, and was
commonly designated by phrases such as: “if the reduction of $X$ with respect to the given valuation is pretty”...
Moreover, $X$ then denoted a closed subscheme, if one may say so, of a $\mathbb{P}^{n}_{K}$, where $K$ is the field of
fractions of $A$, and for lack of an adequate language, the more intrinsic role of an object “defined over $A$”, and not
only over $K$, hardly appeared.

## 3. Permanence Properties

<!-- label: II.3 -->

**Proposition.**

<!-- label: II.3.1 -->

Let $f: X \to Y$ be a morphism, let $x \in X$, and let $y = f(x)$. Suppose $f$ is smooth at $x$. For $\mathcal{O}_{x}$
to be reduced, respectively regular, respectively normal, it is necessary and sufficient that $\mathcal{O}_{y}$ be so.

This statement is indeed known when $X$ is of the form $Y[t_{1},...,t_{n}]$, and it was proved in I, no. I.9 for an
étale morphism; the general case follows at once by Definition II.1.1.

We do not detail here the other permanence properties, which already follow from flatness alone, or from the fact that
$X$ is locally quasi-finite and flat over a $Y$-prescheme of the form $Y[t_{1},...,t_{n}]$, or, as we shall say,

<!-- original page 35 -->

that $X$ is Cohen-Macaulay over $Y$. Let us only point out that from this latter fact one obtains

```text
dim 𝒪_x = dim 𝒪_y + n − d,
depth 𝒪_x = depth 𝒪_y + n − d,
```

<!-- label: eq:II.3.1 -->

where $n$ is the dimension of the fiber of $f$ at $x$, and $d$ is the transcendence degree of $\kappa(x)$ over
$\kappa(y)$. Hence, putting `codepth = dim − depth`,[^II-3-1]

```text
codepth 𝒪_x = codepth 𝒪_y.
```

<!-- label: eq:II.3.2 -->

It follows, for example, that $\mathcal{O}_{x}$ is Cohen-Macaulay, respectively has no embedded components, if and only
if the same is true of $\mathcal{O}_{y}$.

## 4. Differential Properties of Smooth Morphisms

<!-- label: II.4 -->

For simplicity, we shall restrict ourselves essentially to differential calculus of order 1, limiting ourselves to rapid
indications for higher order, where the results are just as simple.

For the definition of the sheaf $\Omega^{1}_{X/Y}$ of 1-differentials of a $Y$-prescheme $X$, cf. I no. I.1. Suppose $X$
and $Y$ are $S$-preschemes, with structural morphism $f: X \to Y$ an $S$-morphism. Then $f$ defines a homomorphism of
modules, compatible with $f$,

$$
f*: \Omega^{1}_{Y/S} \to \Omega^{1}_{X/S}.
$$

<!-- label: eq:II.4.1 -->

In other words, $\Omega^{1}_{X/S}$ is contravariant in the $S$-prescheme $X$. Moreover II.4.1 is equivalent to a
homomorphism of modules on $X$,

$$
f*(\Omega^{1}_{Y/S}) \to \Omega^{1}_{X/S},
$$

<!-- label: eq:II.4.1bis -->

also denoted $f*$ for lack of anything better, and fitting into a canonical exact sequence of module homomorphisms

$$
f*(\Omega^{1}_{Y/S}) \to \Omega^{1}_{X/S} \to \Omega^{1}_{X/Y} \to 0.
$$

<!-- label: eq:II.4.2 -->

All these homomorphisms are defined by the condition of being local in nature, which reduces to the affine case, and of
commuting with the operators $d$. The exactness of II.4.2 is classical and trivial, and in the affine case it is
transcribed as the exact sequence corresponding to a homomorphism $B \to C$ of $A$-algebras:

```text
Ω¹_{B/A} ⊗_B C → Ω¹_{C/A} → Ω¹_{C/B} → 0.
```

<!-- label: eq:II.4.2bis -->

**Lemma.**

<!-- label: II.4.1 -->

<!-- original page 36 -->

Let $f: X \to Y$ be a morphism of $S$-preschemes. If $f$ is unramified, respectively étale, then

$$
f*(\Omega^{1}_{Y/S}) \to \Omega^{1}_{X/S}
$$

is surjective, respectively an isomorphism. The converse is true in the unramified case, if $f$ is assumed locally of
finite type.

The unramified case follows from the exact sequence II.4.2 and from I 3.1, but can also be seen directly as in the étale
case. Consider the diagram

```text
X → X ×_Y X → X ×_S X
    ↓           ↓
    Y →       Y ×_S Y
```

in which $X \times_{Y} X$ identifies with the fiber product of $Y$ and $X \times_{S} X$ over $Y \times_{S} Y$. Since $f$
is unramified, $X \to X \times_{Y} X$ is an open immersion; hence the “conormal” sheaf of the composite immersion
$\Delta_{X/S}$ of the latter with $X \times_{Y} X \to X \times_{S} X$ is isomorphic to the inverse image on $X$ of the
conormal sheaf for the immersion $X \times_{Y} X \to X \times_{S} X$. On the other hand, since $X \to Y$ is étale, hence
flat, $X \times_{S} X \to Y \times_{S} Y$ is flat. Thus the conormal sheaf for the immersion
$X \times_{Y} X \to X \times_{S} X$ is isomorphic to the inverse image of the conormal sheaf for the immersion
$Y \to Y \times_{S} Y$, i.e. the inverse image of $\Omega^{1}_{Y/S}$. The conclusion follows.

**Lemma.**

<!-- label: II.4.2 -->

Let $X = Y[t_{1},...,t_{n}]$, with $Y$ an $S$-prescheme. Then the sequence of canonical homomorphisms

$$
0 \to f*(\Omega^{1}_{Y/S}) \to \Omega^{1}_{X/S} \to \Omega^{1}_{X/Y} \to 0
$$

is exact, and $\Omega^{1}_{X/Y}$ is free with basis $d_{X/Y}t_{i}$.

The verification, purely affine, is immediate. Note that we already know the exactness of II.4.2.

Combining these two statements and Definition II.1.1, one finds:

**Theorem.**

<!-- label: II.4.3 -->

Let $f: X \to Y$ be a smooth morphism of $S$-preschemes. Then:

1. The sequence of canonical homomorphisms

$$
0 \to f*(\Omega^{1}_{Y/S}) \to \Omega^{1}_{X/S} \to \Omega^{1}_{X/Y} \to 0
$$

is exact. 2. $\Omega^{1}_{X/Y}$ is locally free, and its rank $n$ at $x$ is equal to the relative dimension of $f$ at
$x$.

**Corollary.**

<!-- label: II.4.4 -->

<!-- original page 37 -->

The homomorphism

$$
f*(\Omega^{1}_{Y/S}) \to \Omega^{1}_{X/S}
$$

is injective; its image in $\Omega^{1}_{X/S}$ is locally a direct factor.

Let $u: F \to G$ be a homomorphism of modules on the prescheme $X$. We say that it is **universally injective** at
$x \in X$ if the homomorphism $F_{x} \to G_{x}$ of $\mathcal{O}_{x}$-modules is injective and remains so after tensoring
with every $\mathcal{O}_{x}$-algebra, or equivalently with every $\mathcal{O}_{x}$-module. It is enough, for example,
that there exist an open neighborhood $U$ of $x$ such that $u$ induces an isomorphism from $F|U$ onto a direct factor of
$G|U$. This condition is also necessary when $F$ and $G$ are free, of finite type, in a neighborhood of $x$. More
precisely, in that case the following conditions are equivalent:

1. $u$ is injective at $x$ and `Coker u` is free at $x$.
1. There is an open neighborhood $U$ of $x$ such that $u$ induces an isomorphism from $F|U$ onto a direct factor of
   $G|U$.
1. $u$ is universally injective at $x$.
1. The induced homomorphism on the restricted fibers

```text
F_x ⊗ κ(x) → G_x ⊗ κ(x)
```

is injective. 5. The transposed homomorphism $\check{G} \to \check{F}$ is surjective at the point $x$, or equivalently
in a neighborhood of $x$.

For the circular proof, (iv) ⇒ (v) follows from Nakayama, and (v) ⇒ (i) because a locally free quotient sheaf is
necessarily a direct factor. Geometrically, the situation considered means that $u$ corresponds to an isomorphism from
the vector bundle whose sheaf of sections is $F$ onto a sub-bundle of the analogous vector bundle defined by $G$. Of
course it is not enough for this that $F \to G$ be injective.

**Corollary.**

<!-- label: II.4.5 -->

Let $f: X \to Y$ be a morphism of $S$-preschemes, locally of finite type; let $x \in X$, $y = f(x)$, and let $s$ be the
image of $x$ and $y$ in $S$. Suppose that $Y$ is smooth at $y$ over $S$. The following conditions are equivalent:

1. $f$ is smooth at $x$.
1. $X$ is smooth over $S$ at $x$, and

$$
f*(\Omega^{1}_{Y/S}) \to \Omega^{1}_{X/S}
$$

is universally injective at $x$, i.e. it is an injective homomorphism at $x$ and its cokernel $\Omega^{1}_{X/Y}$ is free
at $x$.

The necessity follows from II.1.3 (iii) and II.4.3 (i), (ii). We prove the sufficiency. Since the `d g`, with
$g \in \mathcal{O}_{x}$, generate the module $\Omega^{1}_{X/Y}$ at $x$, one can find $g_{i}$, $1 \leq i \leq n$, such
that the images of the $d g_{i}$ in $(\Omega^{1}_{X/Y})_{x}$ form a basis of this module. Taking $X$ small enough, we
may suppose that the $g_{i}$ come from sections of $\mathcal{O}_{X}$, and therefore define a $Y$-morphism

```text
g: X → Y′ = Y[t₁,...,t_n].
```

Using the hypothesis and Lemma II.4.2, one easily sees that the corresponding homomorphism

$$
g*(\Omega^{1}_{Y'/S}) \to \Omega^{1}_{X/S}
$$

is bijective at $x$. This reduces us to proving the following statement.

**Corollary.**

<!-- label: II.4.6 -->

Let $f: X \to Y$ be a morphism of smooth $S$-preschemes. In order that $f$ be étale at $x \in X$, it is necessary and
sufficient that

$$
f*(\Omega^{1}_{Y/S}) \to \Omega^{1}_{X/S}
$$

be an isomorphism at $x$.

We know by II.4.1 that this is necessary, and the same lemma implies that this condition makes $f$ unramified at $x$. By
II.2.2, we are reduced to the case $S = \operatorname{Spec}(k)$. Since $Y$ is smooth over $k$, it is regular, hence a
fortiori normal, and by I.9.5 (ii) we are reduced to proving that $\mathcal{O}_{y} \to \mathcal{O}_{x}$ is injective, or
again that $\mathcal{O}_{y}$ and $\mathcal{O}_{x}$ have the same dimension. These dimensions are respectively the ranks
of $\Omega^{1}_{Y/k}$ and $\Omega^{1}_{X/k}$ at $y$ and $x$, hence are equal by the hypothesis.

**Remarks.**

<!-- label: II.4.7 -->

When $X$ and $Y$ are assumed smooth over $S$, the smoothness criterion II.4.5 (ii) for $f: X \to Y$ can also be stated
by saying that for every $x \in X$, the **tangent** map of $f$ at $x$, relative to the base $S$, namely the transpose of
the homomorphism of finite-dimensional $\kappa(x)$-vector spaces given by the restricted fibers of
$f*(\Omega^{1}_{Y/S})$ and $\Omega^{1}_{X/S}$ at $x$, is **surjective**. This is a very familiar hypothesis, especially
among those who work with analytic spaces. The nonsingularity hypothesis that they ordinarily impose, meaning that $X$
and $Y$ are “smooth over $\mathbb{C}$”, cf. II.5, seems due only to the fear still inspired in many geometers by
singular points of algebraic varieties or analytic spaces.

Let us point out the following special case of II.4.6.

**Corollary.**

<!-- label: II.4.8 -->

Let $X$ be an $S$-prescheme, let $g: X \to S[t_{1},...,t_{n}]$ be an $S$-morphism defined by sections $g_{i}$,
$1 \leq i \leq n$, of $\mathcal{O}_{X}$, and let $x$ be a point of $X$ such that $X$ is smooth over $S$ at $x$. In order
that $g$ be étale at $x$, it is necessary and sufficient that the $d g_{i}$, $1 \leq i \leq n$, form a basis of
$\Omega^{1}_{X/S}$ at $x$; equivalently, that their images in

```text
Ω¹_{X/S}(x) = (Ω¹_{X/S})_x ⊗_{𝒪_x} κ(x)
```

<!-- original page 39 -->

form a basis of this vector space over $\kappa(x)$.

Let $X$ be a prescheme, and let $Y$ be a closed sub-prescheme of $X$ defined by a coherent sheaf $\mathcal{J}$ of
ideals. Thus $\mathcal{J}/\mathcal{J}^{2}$ may be regarded as a coherent sheaf on $Y$, the **conormal sheaf** of $Y$ in
$X$. If now $X$ is an $S$-prescheme, there is a canonical exact sequence of quasi-coherent sheaves on $Y$

```text
𝒥/𝒥² --d→ Ω¹_{X/S} ⊗_{𝒪_X} 𝒪_Y → Ω¹_{Y/S} → 0.
```

<!-- label: eq:II.4.3 -->

Its right-hand part is just II.4.2, with the roles of $X$ and $Y$ interchanged and taking into account that
$\Omega^{1}_{Y/X} = 0$, while the homomorphism
$\mathcal{J}/\mathcal{J}^{2} \to \Omega^{1}_{X/S} \otimes_{\mathcal{O}_{X}} \mathcal{O}_{Y}$ is obtained from the, in
general nonlinear, homomorphism $g \mapsto d g$ by passing to quotients. The exactness of II.4.3 is classical and in any
case trivial; in the affine case it is interpreted by the following exact sequence, corresponding to a surjective
homomorphism $B \to C$ of $A$-algebras, with kernel $J$:

```text
J/J² → Ω¹_{B/A} ⊗_B C → Ω¹_{C/A} → 0,     C = B/J.
```

<!-- label: eq:II.4.3bis -->

This exact sequence had already been used implicitly in the proof of I.7.2.

**Proposition.**

<!-- label: II.4.9 -->

Let $X$ be an $S$-prescheme, let $Y$ be a closed sub-prescheme of $X$ defined by a coherent sheaf $\mathcal{J}$ of
ideals on $X$, let $x$ be a point of $X$, let $g_{i}$, $1 \leq i \leq n$, be sections of $\mathcal{O}_{X}$ defining an
$S$-morphism

```text
g: X → S[t₁,...,t_n] = X′,
```

and finally let $p$ be an integer, $0 \leq p \leq n$. Suppose that $X$ is **smooth over $S$ at $x$**. The following
conditions are equivalent:

1. There is an open neighborhood $X_{1}$ of $x$ in $X$ such that $g|X_{1}$ is **étale** and such that
   $Y_{1} = Y \cap X_{1}$, the trace of $Y$ on $X_{1}$, is the **inverse image** of the closed sub-prescheme
   $Y' = S[t_{p+1},...,t_{n}]$ of $X' = S[t_{1},...,t_{n}]$; equivalently, the $g_{i}$, $1 \leq i \leq p$, generate
   $\mathcal{J}|X_{1}$:

$$
Y_{1}  \to  X_{1}
\downarrow       \downarrow \acute{e}tale
Y'  \to  X'
$$

1. $Y$ is **smooth over $S$ at $x$**, the $g_{i}$, $1 \leq i \leq p$, define **elements of** $\mathcal{J}_{x}$, the
   $d g_{i}(x)$, $1 \leq i \leq n$, form a **basis of** $\Omega^{1}_{X/S}(x)$ over $\kappa(x)$, and the $d g'_{i}(x)$,
   $p + 1 \leq i \leq n$, form a **basis of** $\Omega^{1}_{Y/S}(x)$ over $\kappa(x)$, where the $g'_{i}$ denote the
   restrictions of the $g_{i}$ to $Y$; the differentials are taken relative to $S$.
1. The $g_{i}$, $1 \leq i \leq p$, define a **system of generators** of $\mathcal{J}_{x}$, and the $d g_{i}(x)$,
   $1 \leq i \leq n$, form a **basis of** $\Omega^{1}_{X/S}(x)$ over $\kappa(x)$.
1. $Y$ is **smooth over $S$** at $x$, the $g_{i}$, $1 \leq i \leq p$, form a **minimal system of generators of**
   $\mathcal{J}_{x}$, and the $d g'_{i}(x)$, $p + 1 \leq i \leq n$, form a **basis of** $\Omega^{1}_{Y/S}(x)$ over
   $\kappa(x)$.

Moreover, under these conditions, $\mathcal{J}/\mathcal{J}^{2}$ is a free module on $Y$ at $x$, having as **basis at
$x$** the classes of the $g_{i}$, $1 \leq i \leq p$, and the canonical homomorphism

$$
\mathcal{J}/\mathcal{J}^{2} \to \Omega^{1}_{X/S} \otimes \mathcal{O}_{Y}
$$

is **universally injective at $x$**.

**Remark.** This implies that $p$ is well determined by the other conditions, either as the **rank** of the free module
$\mathcal{J}/\mathcal{J}^{2}$ on $Y$ at $x$, or again as the **minimum number of generators** of $\mathcal{J}_{x}$ on
$X$, or finally by the fact that the relative dimension of $Y$ relative to $S$ at $x$ is $n - p$.

**Proof.** Suppose first that (i) holds. Then by I.4.6 (iii), $Y_{1}$ is étale over $Y'$; hence by definition it is
smooth over $S$ at $x$, of relative dimension $n - p$, and the same is therefore true of $Y$. It then follows from
II.4.8 that the $d g_{i}$, $1 \leq i \leq n$, form a basis of $\Omega^{1}_{X/S}$ at $x$, and that the $d g'_{i}$,
$p + 1 \leq i \leq n$, form a basis of $\Omega^{1}_{Y/S}$ at $x$. By the exact sequence II.4.3, it follows that the
$g_{i}$, $1 \leq i \leq p$, are linearly independent in $\mathcal{J}/\mathcal{J}^{2}$, considered as a module on $Y$, at
$x$. Since the $g_{i}$, $1 \leq i \leq p$, generate $\mathcal{J}_{x}$, it follows that the $g_{i}$ modulo
$\mathcal{J}^{2}_{x}$ form a **basis of** $\mathcal{J}/\mathcal{J}^{2}$ at $x$. This implies, on the one hand, that the
$g_{i}$, $1 \leq i \leq p$, form a **minimal** system of generators of $\mathcal{J}_{x}$, and, on the other hand, that
the homomorphism $\mathcal{J}/\mathcal{J}^{2} \to \Omega^{1}_{X/S} \otimes \mathcal{O}_{Y}$ in II.4.3 is universally
injective at $x$, since it sends a basis of a module free at $x$ to part of a basis of a module free at $x$; note that
these are $Y$-modules. This proves that (i) implies (ii), (iii), (iv), as well as the last assertions of Proposition
I.4.9.

(iii) implies (i) by Corollary I.4.8.

<!-- original page 41 -->

(ii) implies (i). Indeed, the first hypothesis in (ii) means that, after replacing $X$ by an open neighborhood of $x$ in
$X$, $g$ induces a morphism $h: Y \to Y'$. By II.4.8, the two other hypotheses in (ii) mean that $g$ is étale at $x$ and
$h$ is étale at $x$. Let $Y''$ be the inverse image of $Y'$ by $g$. Then $Y$ is a closed sub-prescheme of $Y''$, which
is étale over $Y'$ at $x$ by I.4.6 (iii), since $g$ is étale at $x$. Thus the immersion morphism $Y \to Y''$ is itself
étale by I.4.8, hence is an open immersion by I.5.8 or I.5.2. Replacing $X$ again by a suitable open neighborhood
$X_{1}$ of $x$, we obtain (i).

The preceding establishes the equivalence of conditions (i), (ii), (iii), and the fact that they imply (iv). It remains
to prove that (iv) ⇒ (ii), which is immediate, taking into account that $\Omega^{1}_{X/S}$ is free on $X$ at $x$, once
one knows that the fact that $Y$ is smooth over $S$ at $x$ implies that $\mathcal{J}/\mathcal{J}^{2}$ is free on $Y$ at
$x$ and that the homomorphism

$$
\mathcal{J}/\mathcal{J}^{2} \to \Omega^{1}_{X/S} \otimes \mathcal{O}_{Y}
$$

is universally injective at $x$. This last point is included in the following theorem.

**Theorem.**

<!-- label: II.4.10 -->

Let $X$ be a smooth $S$-prescheme, let $Y$ be a closed sub-prescheme of $X$ defined by a coherent sheaf $\mathcal{J}$ of
ideals on $X$, and let $x$ be a point of $X$. The following conditions are equivalent:

1. $Y$ is **smooth over $S$ at $x$**.
1. There is an open neighborhood $X_{1}$ of $x$ in $X$ and an **étale** $S$-morphism

```text
g: X₁ → X′ = S[t₁,...,t_n]
```

such that $Y_{1} = Y \cap X_{1}$, the trace of $Y$ on $X_{1}$, is the sub-prescheme of $X_{1}$ that is the **inverse
image** under $g$ of the closed sub-prescheme $Y' = S[t_{p+1},...,t_{n}]$ of $X' = S[t_{1},...,t_{n}]$, for a suitable
$p$. 3. There are **generators $g_{i}$, $1 \leq i \leq p$, of $\mathcal{J}_{x}$** such that the $d g_{i}$ form part of a
basis of $\Omega^{1}_{X/S}$ at $x$; equivalently, such that the $d g_{i}(x)$ in $\Omega^{1}_{X/S}$ are linearly
independent over $\kappa(x)$. 4. The sheaf $\mathcal{J}/\mathcal{J}^{2}$ is free on $Y$ at $x$, and the canonical
homomorphism

```text
d: 𝒥/𝒥² → Ω¹_{X/S} ⊗ 𝒪_Y
```

is universally injective at $x$; or again, the sequence of canonical homomorphisms

```text
0 → 𝒥/𝒥² → Ω¹_{X/S} ⊗ 𝒪_Y → Ω¹_{Y/S} → 0
```

is exact at $x$, and $\Omega^{1}_{Y/S}$ is locally free at $x$.

**Proof.** We already know from the preceding that (ii) implies (i), (iii), and (iv). We prove (i) ⇒ (ii), which will at
the same time finish the proof of I.4.9. By Theorem II.4.3 (ii), the last two terms in the exact sequence II.4.3 are
free modules on $Y$. Thus, since the images in $\Omega^{1}_{X/S} \otimes_{\mathcal{O}_{X}} \mathcal{O}_{Y}$ of the
`d g`, for $g \in \mathcal{O}_{X}$, generate this module at $x$, hence their images in $\Omega^{1}_{Y/S}$ generate the
latter at $x$, one can find $g_{i}$, $p + 1 \leq i \leq n$, in $\mathcal{O}_{X}$ such that the $d g'_{i}$ form a basis
of $\Omega^{1}_{Y/S}$. Then, by exactness of II.4.3, one can complete the system of the $d g_{i}$,
$p + 1 \leq i \leq n$, to a basis of the middle term by elements of the form $d g_{i}$, $1 \leq i \leq n$, where the
$g_{i}$, $1 \leq i \leq p$, **belong to $\mathcal{J}_{x}$**. The $g_{i}$ come from sections of $\mathcal{O}_{X}$ on a
neighborhood of $x$ in $X$, which we may suppose equal to $X$. We are then under the conditions of II.4.8 (ii), and we
have established that these imply condition II.4.8 (i), whence II.4.10 (ii).

The implication (iii) ⇒ (ii) in II.4.10 follows at once from the implication (iii) ⇒ (i) in II.4.8. Thus (i), (ii),
(iii) are equivalent and imply (iv). Finally, it is trivial that (iv) implies (iii), taking into account that elements
$g_{i} \in \mathcal{J}_{x}$ whose classes form a basis of $\mathcal{J}_{x}$ modulo $\mathcal{J}^{2}_{x}$ generate
$\mathcal{J}_{x}$ by Nakayama.

Moreover, the preceding proof shows the following.

**Corollary.**

<!-- label: II.4.11 -->

Let $X$ be an $S$-prescheme, let $Y$ be a closed sub-prescheme defined by a coherent sheaf $\mathcal{J}$ of ideals on
$X$, and let $x$ be a point of $Y$. Suppose that **$X$ and $Y$ are smooth over $S$ at $x$**. Let $g_{i}$ be sections of
$\mathcal{J}$, $1 \leq i \leq p$. The following conditions are equivalent:

1. The $g_{i}$ **generate** $\mathcal{J}_{x}$ and the $d g_{i}(x)$ are **linearly independent** in $\Omega^{1}_{X/S}(x)$
   over $\kappa(x)$.
1. The $g_{i}$ modulo $\mathcal{J}^{2}$ form a basis of $\mathcal{J}/\mathcal{J}^{2}$ at $x$.
1. The $g_{i}$ form a minimal system of generators of $\mathcal{J}_{x}$.
1. One can find other sections $g_{i}$, $p + 1 \leq i \leq n$, of $\mathcal{O}_{X}$ on a neighborhood $X_{1}$ of $x$,
   defining together with the preceding ones an **étale** morphism $X_{1} \to X' = S[t_{1},...,t_{n}]$ such that
   $Y_{1} = Y \cap X_{1}$ is the **inverse image** under $g$ of the closed sub-prescheme $Y' = S[t_{p+1},...,t_{n}]$ of
   $X' = S[t_{1},...,t_{n}]$.

<!-- original page 43 -->

In particular:

**Corollary.**

<!-- label: II.4.12 -->

Let $X$ be an $S$-prescheme, let $F$ be a section of $\mathcal{O}_{X}$, let $Y$ be the sub-prescheme of the zeros of
$F$, defined by the coherent ideal $F\cdot \mathcal{O}_{X}$, and let $x$ be a point of $Y$. Suppose that $X$ is smooth
over $S$ at $x$. In order that $Y$ be smooth over $S$ at $x$, it is necessary and sufficient that either $F$ be zero in
a neighborhood of $x$, or $dF(x) \neq 0$, where $dF(x)$ denotes the image of `dF` in the vector space
$\Omega^{1}_{X/S}(x)$ over $\kappa(x)$.

This is sufficient by criterion (iii) of II.4.10. It is necessary, because since $\mathcal{J}$ is generated by one
element, it is first necessary that $\mathcal{J}/\mathcal{J}^{2}$ at the point $x$ be free of rank $\leq 1$. If this
rank is 0, i.e. if $\mathcal{J}/\mathcal{J}^{2} = 0$ at $x$, it follows that $\mathcal{J} = 0$ at $x$ by Nakayama, i.e.
$F$ is zero in a neighborhood of $x$. If this rank is 1, then $F$ forms a minimal system of generators of $\mathcal{J}$
at $x$, and one concludes by II.4.11, equivalence of (i) and (iii).

**Corollary.**

<!-- label: II.4.13 -->

Let $Y$ be an $S$-prescheme locally of finite type, let $S'$ be a **flat** $S$-prescheme, let $Y' = Y \times_{S} S'$,
let $x'$ be a point of $Y'$, and let $x$ be its canonical image in $Y$. In order that $Y$ be smooth over $S$ at $x$, it
is necessary and sufficient that $Y'$ be smooth over $S'$ at $x'$. In particular, if $S' \to S$ is flat and surjective,
$Y$ is smooth over $S$ if and only if $Y'$ is smooth over $S'$.

Only the sufficiency has to be proved; the necessity was seen in II.1.3 (ii). We may suppose, after replacing $Y$ by a
suitable neighborhood of $x$ and $Y'$ by its inverse image, that $Y$ is affine of finite type over affine $S$; hence $Y$
is isomorphic to a closed sub-prescheme of a scheme $S[t_{1},...,t_{n}]$. It follows that $Y'$ identifies with a closed
sub-prescheme of $X' = X \times_{S} S'$. Since $X$ is smooth over $S$, and hence $X'$ is smooth over $S'$, the
smoothness criteria II.4.10 may be applied. Here criterion (iv) gives the result at once.

**Remarks.**

<!-- label: II.4.14 -->

Criterion (iii) of Theorem II.4.10 deserves to be called the **Jacobian criterion for smoothness**. It makes it
possible, theoretically, to recognize whether a given $S$-prescheme $Y$ is smooth over $S$ at a point $x$ of $Y$, since
there is always a neighborhood of $Y$ isomorphic to a sub-prescheme of a smooth $S$-prescheme $X$, for instance
$X = S[t_{1},...,t_{n}]$. It is indeed for $X = S[t_{1},...,t_{n}]$, $S = \operatorname{Spec}(A)$, that the Jacobian
criterion is usually stated; of course, in the classical case considered by Zariski, $A$ was a field. We leave it to the
reader to give the statement, to which one is thus led, in terms of an ideal $J$ of $A[t_{1},...,t_{n}]$ and a prime
ideal containing it. Let us note that at present it seems, especially since Nagata succeeded in generalizing by
non-differential methods Zariski's theorem saying that the set of regular points of an algebraic scheme is open, that
the Jacobian criterion has scarcely any interest except in the form in which we give it here, i.e. using exclusively
**relative** differentials and not **absolute** differentials, i.e. differentials relative to the absolute ring of
constants $\mathbb{Z}$. As very often, considering differentials is more convenient here than considering derivations.
Finally, note that if $Y$ is smooth over $S$ at $x$, of relative dimension $m$, then there is an open neighborhood of
$x$ in $Y$ isomorphic to a sub-prescheme of $X = S[t_{1},...,t_{n}]$ with $n = m + 1$, as follows from the definition
and from I.7.6.

Let $A$ be a noetherian ring, let $x_{i}$, $1 \leq i \leq n$, be elements of $A$, and let $J$ be the ideal generated by
the $x_{i}$. We say that the $x_{i}$ form a **regular system of generators** of $J$ if the canonical surjective
homomorphism

$$
(A/J)[t_{1},...,t_{n}] \to gr^{J}(A)
$$

defined by the $x_{i}$, where the second member denotes the graded ring associated with $A$ filtered by the powers of
$J$, is an **isomorphism**. This condition also means that:

1. The canonical surjective homomorphism

$$
S_{A/J}(J/J^{2}) \to gr^{J}(A),
$$

where the first member denotes the symmetric algebra of the $A/J$-module $J/J^{2}$, is an isomorphism. 2. $J/J^{2}$ is
free and has as basis the classes of the $x_{i}$ modulo $J^{2}$.

In this form one sees that if $J \neq A$, the $x_{i}$ form a **minimal system of generators** of $J$, and that **every
other minimal system of generators** of $J$ **is a regular system of generators**. Here “minimal” is taken in the strict
sense: minimum number of elements, which is equivalent to minimality for inclusion only if $A$ is local. On the other
hand, if $J = A$, every system of generators of $J$ is regular.

<!-- original page 45 -->

The regularity condition for a system of generators of an ideal is stable under localization by an arbitrary
multiplicatively stable set. Moreover, one sees immediately that, in order for $(x_{i})$ to be a minimal system of
generators of $J$, it already suffices that for every **maximal ideal $\mathfrak{m}$ containing $J$**, the $x_{i}$
define a regular system of generators of $J A_{\mathfrak{m}}$ in $A_{\mathfrak{m}}$. We are therefore reduced to the
case where $A$ is a local ring with maximal ideal $\mathfrak{m}$, and where the $x_{i}$ are in $\mathfrak{m}$. **Then
the $x_{i}$ form a regular system of generators of $J$ if and only if they form an $A$-sequence in the sense of Serre**,
that is, if for every $i$ with $1 \leq i \leq n$, $x_{i}$ is not a zero-divisor in $A/(x_{1},...,x_{i-1})A$.[^ii-4-14-1]

Finally, in the case where $A$ is an algebra over a ring $B$, and where $A/J$ is isomorphic as a $B$-algebra to $B$, so
that $J$ is the kernel of a homomorphism of $B$-algebras $A \to B$, the $x_{i}$ form a regular system of generators of
$J$ if and only if the canonical homomorphism

$$
B[[t_{1},...,t_{n}]] \to \hat{A}
$$

defined by the $x_{i}$, where the second member denotes the separated completion $\lim A/J^{n+1}$ of $A$ for the
topology defined by the powers of $J$, is an **isomorphism**; it is in any case **surjective**.

All these facts are well known and, no doubt with minor differences, appear in Serre's course on commutative algebra
written up by Gabriel, where one finds N other characterizations of $A$-sequences in the case where $A$ is a local ring.

Let $J$ be an ideal in a noetherian ring $A$. We shall say that $J$ is a **regular ideal** if, for every prime ideal
$\mathfrak{p}$ of $A$, $J A_{\mathfrak{p}}$ admits a regular system of generators. It is of course enough to verify this
for $\mathfrak{p} \supset J$, and one may furthermore restrict to maximal $\mathfrak{p}$. More generally, let
$\mathcal{J}$ be an ideal on a locally noetherian prescheme $X$. We say that $\mathcal{J}$ is a **regular ideal** if,
for every $x \in X$, $\mathcal{J}_{x}$ is an ideal of $\mathcal{O}_{x}$ admitting a regular system of generators. This
is equivalent to the conjunction of the following two conditions:

1. The canonical surjective homomorphism

$$
S_{\mathcal{O}_{X}/\mathcal{J}}(\mathcal{J}/\mathcal{J}^{2}) \to gr^{\mathcal{J}}(\mathcal{O}_{X})
$$

is an isomorphism. 2. The sheaf of $\mathcal{O}_{X}/\mathcal{J}$-modules $\mathcal{J}/\mathcal{J}^{2}$ is locally free.

<!-- original page 46 -->

One also then says that the sub-prescheme $Y$ of $X$ defined by $\mathcal{J}$, so that $\mathcal{O}_{Y}$ extended by 0
is isomorphic to $\mathcal{O}_{X}/\mathcal{J}$, is **regularly immersed** in $X$. In the same evident way one defines
the notion of a morphism that is a **regular immersion**, respectively **regular at a point $x$**: an immersion morphism
$Y \to X$ identifying $Y$, respectively a suitable neighborhood of $x$, with a closed sub-prescheme regularly immersed
in an open of $X$. One should not say “regular sub-prescheme”, since that would mean that the local rings of $Y$ are
regular. Finally, sections $x_{i}$ of $\mathcal{J}$ are called a **regular system of generators** if, for every
$x \in X$, the corresponding elements of $\mathcal{O}_{x}$ form a regular system of generators of $\mathcal{J}_{x}$;
this terminology is compatible with that introduced for generators of an ideal of a ring. This also means that the
canonical surjective homomorphism

$$
\mathcal{O}_{Y}[t_{1},...,t_{n}] \to gr^{\mathcal{J}}(\mathcal{O}_{X})
$$

defined by the $x_{i}$ is an isomorphism. If one knows in advance that the ideal $\mathcal{J}$ is regular, this simply
means that at every point $x$ **of $Y$**, the $x_{i}$ define a **basis** of $\mathcal{J}/\mathcal{J}^{2}$ over
$\mathcal{O}_{Y,x}$. This condition is empty if $Y$ is empty. Thus, in order that $\mathcal{J}$ admit a regular system
of generators, it is necessary and sufficient that $\mathcal{J}$ be regular and that the $\mathcal{O}_{Y}$-module
$\mathcal{J}/\mathcal{J}^{2}$ be globally free, not merely locally free; that is, that the canonical homomorphism
$S_{\mathcal{O}_{Y}}(\mathcal{J}/\mathcal{J}^{2}) \to gr^{\mathcal{J}}(\mathcal{O}_{X})$ be surjective and that the
$\mathcal{O}_{Y}$-module $\mathcal{J}/\mathcal{J}^{2}$ be globally free.

An **augmented ring is said to be regular** if the ideal of augmentation is regular. Thus, if $A$ is a local ring,
regarded as augmented into its residue field $k$, then $A$ is a regular local ring if and only if it is a regular
augmented ring.

To tell the truth, it seems that it was unnecessary to begin by making the preliminary sorites for rings; there is some
advantage in starting with sheaves at once. If one wants something in the noetherian case, it is the definition adopted
here, a priori less strict than Serre's definition by $A$-sequences, that seems preferable for the needs of differential
calculus. Of course, to do the job properly, one would also have to develop at least part of the theory of smooth
morphisms in the non-noetherian setting,[^ii-4-14-2] probably by starting from the Jacobian criterion, so as to obtain
if possible all the essential formal properties of smooth morphisms and of étale morphisms, i.e. smooth and quasi-finite
morphisms; only the converses would appeal to noetherian hypotheses.

After these long terminological preliminaries, a small theorem:

**Theorem.**

<!-- label: II.4.15 -->

Let $X$ be an $S$-prescheme locally of finite type, let $Y$ be a closed sub-prescheme of $X$ defined by a coherent sheaf
$\mathcal{J}$ of ideals on $X$, and let $x$ be a point of $X$. We now suppose **$Y$ smooth over $S$ at $x$**, and assume
nothing about $X$. Then the following conditions are equivalent:

1. $X$ is smooth over $S$ at $x$.
1. The immersion $i: Y \to X$ is regular at $x$, i.e. $\mathcal{J}_{x}$ is a regular ideal of $\mathcal{O}_{x}$.

**Corollary.**

<!-- label: II.4.16 -->

Suppose $Y$ is **smooth** over $S$. In order that $X$ be smooth over $S$ in a neighborhood of $Y$, i.e. at the points of
$Y$, it is necessary and sufficient that $Y$ be regularly embedded in $X$, i.e. that the immersion $i: Y \to X$ be
regular.

**Proof.** (i) implies (ii). Apply criterion (ii) of II.4.10. Since $g: X_{1} \to X$ is **flat**, in order to show that
the inverse image by $g$ of the sub-prescheme $Y'$ of $X'$ is regularly embedded, we are reduced to proving that
$Y' = S[t_{p+1},...,t_{n}]$ is regularly embedded in $S[t_{1},...,t_{n}]$, which is trivial: the $t_{i}$,
$1 \leq i \leq p$, form a regular system of generators of the ideal defining $Y'$ in $X'$.

(ii) implies (i). Let $g_{i}$, $1 \leq i \leq p$, be a regular system of generators of $\mathcal{J}_{x}$, and let
$g_{i}$, $p + 1 \leq i \leq n$, be elements of $\mathcal{O}_{X,x}$ such that their images $g'_{i}$ in
$\mathcal{O}_{Y,x}$ define an **étale** morphism

$$
Y_{1} \to Y' = S[t_{p+1},...,t_{n}]
$$

from a neighborhood $Y_{1}$ of $x$ in $Y$. The $g_{i}$, $1 \leq i \leq n$, come from sections, denoted by the same
names, of $\mathcal{O}_{X}$ on a neighborhood $X_{1}$ of $x$, and we may suppose $X_{1} = X$ and $Y_{1} = Y$. We thereby
obtain a morphism

```text
g: X → X′ = S[t₁,...,t_n],
```

and everything comes down to showing that this morphism is **étale** at $x$. Taking $X_{1}$ small enough, we may suppose
that the $g_{i}$, $1 \leq i \leq p$, form a regular system of generators of $\mathcal{J}$ on all of $X$. In particular,
they generate $\mathcal{J}$, so the sub-prescheme $Y$ of $X$ identifies with the inverse image by $g$ of the
sub-prescheme $Y'$ of $X'$. Let $x' = g(x)$. Then the fiber of $X \to X'$ at $x'$ is identical with the fiber of
$Y \to Y'$ at $x$, hence is étale over $\kappa(x')$, and therefore $g$ is **unramified** at $x$. It remains to prove
that $g$ is **flat** at $x$. The graded ring associated with $\mathcal{O}_{X',x'}$, filtered by the powers of
$\mathcal{J}'_{x'}$, is **free** over $\mathcal{O}_{Y',x'}$ in every degree; on the other hand, the graded ring
associated with $\mathcal{O}_{X,x}$, filtered by the powers of $\mathcal{J}_{x} = \mathcal{J}'_{x} \mathcal{O}_{X,x}$,
is isomorphic, under the canonical homomorphism, to the tensor product of the preceding one with $\mathcal{O}_{Y,x}$,
since both rings are polynomial rings in $n - p$ indeterminates with rings of constants $\mathcal{O}_{Y',x'}$ and
$\mathcal{O}_{Y,x}$, respectively. Finally, over $\mathcal{O}_{X',x'}/\mathcal{J}'_{x'} = \mathcal{O}_{Y',x'}$, the
quotient $\mathcal{O}_{X,x}/\mathcal{J}_{x} = \mathcal{O}_{Y,x}$ is flat.

By a general flatness criterion, valid for a local homomorphism of noetherian local rings $A' \to A$, where $A'$ is
equipped with an ideal $J' \neq A'$ whose associated graded ring is free over $A'/J'$ in every dimension, it follows
that $X$ is flat over $X'$ at $x$, as required.

**Corollary.**

<!-- label: II.4.17 -->

Let $X$ be a prescheme locally of finite type over $Y$, let $i$ be a section of $X$ over $Y$, let $y$ be a point of $Y$,
let $x = i(y)$, and let $\mathcal{J}$ be the sheaf of ideals on $X$ defined by the sub-prescheme $i(Y)$, which we
suppose closed in order to simplify the statement, a condition satisfied if $X$ is a scheme.

The following conditions are equivalent:

1. $X$ is smooth over $Y$ at $x$.
1. $i$ is a regular immersion at $y$.
1. The $\mathcal{O}_{y}$-algebra obtained by completing $\mathcal{O}_{x}$ for the topology defined by the powers of
   $\mathcal{J}_{x}$ is isomorphic to a formal power-series algebra $\mathcal{O}_{y}[[t_{1},...,t_{n}]]$.
1. There is an open neighborhood $U$ of $y$ such that the sheaf of algebras $\lim i*(\mathcal{O}_{X}/\mathcal{J}^{n+1})$
   on $\mathcal{O}_{Y}$ is isomorphic over $U$ to a sheaf of the form $\mathcal{O}_{Y}[[t_{1},...,t_{n}]]$.
1. There is an open neighborhood $U$ of $y$, an open neighborhood $V$ of $x$, and finally a $Y$-morphism
   $g: V \to U[t_{1},...,t_{n}]$, such that $g$ is étale, such that $i$ induces a section of $V$ over $U$, and such that
   $g$ carries this section to the zero section of $U[t_{1},...,t_{n}]$ over $U$.

The equivalence of (i) and (ii) is a special case of Theorem II.4.15, taking $Y = S$. The equivalence of (ii) and (iii),
and morally of (ii) and (iii bis), was indicated in the “reminders”. As for the equivalence of (i) and (iv), it follows
easily from Theorem II.4.10, namely from the equivalence of conditions (i) and (ii) there.

**Corollary.**

<!-- label: II.4.18 -->

Let $X$ be a prescheme smooth over $S$. Then the diagonal morphism

```text
Δ_{X/S}: X → X ×_S X
```

is a **regular immersion**, or, as one also says, $X$ is “**differentially smooth**” over $S$.

Indeed, this is a special case of Corollary II.4.16, since $X$ and $X \times_{S} X$ are both smooth over $S$.

**Remarks.**

<!-- label: rem:II.4.18 -->

Recall from I.1 that if $X$ is a prescheme over $S$, one introduces the quasi-coherent sheaves of algebras

```text
𝒫ⁿ_{X/S} = 𝒪_{X ×_S X}/𝓘_X^{n+1}
```

on $X$, where $\mathcal{I}_{X}$ denotes the sheaf of ideals defining the diagonal in $X \times_{S} X$, regarded as a
sheaf of $\mathcal{O}_{X}$-algebras through the first projection $pr_{1}: X \times_{S} X \to X$. The
$\mathcal{P}^{n}_{X/S}$ form a projective system of algebras on $X$, whose projective limit is denoted
$\mathcal{P}^{\infty}_{X/S}$; it is nothing other than the structure sheaf of the formal completion of $X \times_{S} X$
along the diagonal, now supposing $X$ locally of finite type over $S$, hence the $\mathcal{P}^{n}_{X/S}$ coherent. To
say that $X$ is differentially smooth over $S$, i.e. that the diagonal morphism $\Delta_{X/S}$ is a regular immersion,
also means that $\mathcal{P}^{\infty}_{X/S}$ is regular as a sheaf of augmented algebras toward $\mathcal{O}_{X}$, i.e.
that $\Omega^{1}_{X/S}$ is locally free and the canonical surjective homomorphism

$$
S_{\mathcal{O}_{X}}(\Omega^{1}_{X/S}) \to gr_{*}(\mathcal{P}^{\infty}_{X/S})
$$

is an isomorphism; or finally that every point of $X$ has an open neighborhood on which the sheaf of augmented algebras
$\mathcal{P}^{\infty}_{X/S}$ is isomorphic to a sheaf $\mathcal{O}_{X}[[t_{1},...,t_{n}]]$.

Let $s$ be a section of $X$ over $S$, and let $\mathcal{J}$ be the sheaf of ideals on $X$ that it defines, supposing for
simplicity that $s(S)$ is closed. Then there are canonical isomorphisms of augmented $\mathcal{O}_{X}$-algebras:

```text
s*(𝒫ⁿ_{X/S}) = 𝒪_X/𝒥^{n+1},    s*(𝒫^∞_{X/S}) = lim_n 𝒪_X/𝒥^{n+1}.
```

<!-- label: eq:II.4.4 -->

These isomorphisms are functorial in the evident sense under base change and, taking this fact into account, again give
a characterization of the sheaves of algebras $\mathcal{P}^{n}_{X/S}$ on $S$. If, for example,
$S = \operatorname{Spec}(k)$, with $k$ a field, then giving a section $s$ of $X$ over $S$ is equivalent to giving a
point $x$ of $X$ rational over $k$, and the preceding formulas mean that there is an isomorphism of $k$-algebras

$$
\mathcal{P}^{n}_{X/S}(x) = \mathcal{O}_{x}/\mathfrak{m}^{n+1}_{x}.
$$

<!-- label: eq:II.4.5 -->

This justifies the name “**sheaf of principal parts of order $n$ on $X$ relative to $S$**” given to
$\mathcal{P}^{n}_{X/S}$. One sees moreover from II.4.4 that **if $X$ is differentially smooth over $S$ at every point of
$s(S)$, then $X$ is smooth over $S$ at every point of $s(S)$**, by Corollary II.4.17, **the converse also being true**,
by Corollary II.4.18. Taking II.4.13 into account, one easily concludes that if $X$ is an $S$-prescheme locally of
finite type, **$X$ is smooth over $S$ if and only if it is flat over $S$ and differentially smooth over $S$**. Note that
the flatness hypothesis is essential, as one sees by taking $X$ to be a closed sub-prescheme of $S$.

Let us also recall that one obtains a **second algebra structure** on $\mathcal{P}^{n}_{X/S}$ through the projection
$pr_{2}: X \times_{S} X \to X$; it is in fact obtained from the preceding one by means of the **canonical involution**
of the sheaf of rings $\mathcal{P}^{n}_{X/S}$, induced by the symmetry automorphism of $X \times_{S} X$. We denote by
$d^{n}_{X/S}$, or simply $d^{n}$, the homomorphism of sheaves of rings

$$
d^{n}_{X/S}: \mathcal{O}_{X} \to \mathcal{P}^{n}_{X/S}
$$

<!-- label: eq:II.4.6 -->

that corresponds to this second algebra structure. Taking the isomorphism II.4.4 into account, this homomorphism
transforms a section $f$ of $\mathcal{O}_{X}$ into a section $d^{n}(f)$ of $\mathcal{P}^{n}_{X/S}$ whose inverse image
by a section $s$ of $X$ over $S$ identifies with the canonical image of $f$ in
$\Gamma(X, \mathcal{O}_{X}/\mathcal{J}^{n+1})$. This justifies the name “**system of principal parts of order $n$ of
$f$**” given to $d^{n}f$, notably in the case $S = \operatorname{Spec}(k)$ considered in formula II.4.5.

Finally, note that the homomorphism II.4.6 may be regarded as the **universal differential operator of order
$\leq n$**[^ii-4-18-1] on $\mathcal{O}_{X}$, relative to the prescheme of constants $S$, provided one agrees to call a
homomorphism of sheaves $D$ from $\mathcal{O}_{X}$ into a module $F$ a differential operator of order $\leq n$ when it
factors as

```text
D: 𝒪_X --dⁿ→ 𝒫ⁿ_{X/S} --u→ F
```

where $u$ is a homomorphism of $\mathcal{O}_{X}$-modules, necessarily uniquely determined by $D$. This definition agrees
with the intuitive recursive definition: $D$ is a differential operator of order $\leq n$ if for every section $g$ of
$\mathcal{O}_{X}$ on an open $U$ of $X$, the map $f \mapsto D(fg) - gD(f)$ is a differential operator of order
$\leq n - 1$ on $U$. It follows that **if $X$ is differentially smooth over $S$, the sheaf of rings of differential
operators of all orders has the familiar simple structure** from differential calculus on differentiable manifolds, and
in particular admits locally, as an $\mathcal{O}_{X}$-module, a basis formed from the **divided powers** in commuting
operators $\delta/\delta x_{i}$, $1 \leq i \leq n$. If $S$ is a sheaf of $\mathbb{Q}$-algebras, where $\mathbb{Q}$ is
the field of rational numbers, it is enough to take the ordinary polynomials in the $\delta/\delta x_{i}$. In that case,
moreover, and very exceptionally, for $X$ to be differentially smooth over $S$ it already suffices that
$\Omega^{1}_{X/S}$ be locally free.

**Remark.**

<!-- label: II.4.19 -->

The terminology “regular immersion”, “regular ideal”, etc. introduced in this number met with rather lively and general
opposition from Chevalley and Serre. “Cohen-Macaulay ideal”, or “Macaulay ideal”, or “Macaulayan ideal” was proposed,
which would morally oblige one also to adopt “Cohen-Macaulay immersion” or “Macaulay immersion”. This terminology,
however, conflicts with another already used in future drafts of the multiplodocus, where a morphism of finite type is
said to be “Cohen-Macaulay” at a point if it is flat at that point and if the fiber passing through that point has there
a local ring that is a Cohen-Macaulay ring. Pending a satisfactory solution, we shall keep, with every reservation, the
terminology introduced in this number.[^ii-4-19-1]

## 5. Case of a Base Field

<!-- label: II.5 -->

<!-- original page 52 -->

**Proposition.**

<!-- label: II.5.1 -->

Let $k$ be a field, let $X$ be a prescheme of finite type over $k$, let $x$ be a point of $X$, let $n$ be the dimension
of $X$ at $x$, and let

```text
f: X → Spec k[t₁,...,t_n] = Y
```

be a morphism defined by elements $f_{i} \in \Gamma(X, \mathcal{O}_{X})$. The following conditions are equivalent, and
imply that $X$ is smooth over $k$ at $x$, and a fortiori regular at $x$ by II.3.1:

1. $f$ is étale at $x$.
1. The $d f_{i}$ form a basis of $\Omega^{1}_{X/k}$ at $x$.
1. The $d f_{i}$ generate $\Omega^{1}_{X/k}$ at $x$.

Since (i) implies that $X$ is smooth over $k$ at $x$, the implication (i) ⇒ (ii) is a special case of II.4.8; (ii) ⇒
(iii) is trivial. It remains to prove (iii) ⇒ (i). If (iii) holds, $f$ is unramified at $x$ by Lemma II.4.1, hence,
after replacing $X$ by an open neighborhood of $x$, quasi-finite, and therefore dominant for dimension reasons. Since
$Y$ is regular, it follows that $f$ is étale by I.9.5 (ii) or I.9.11.

**Corollary.**

<!-- label: II.5.2 -->

Under the preliminary conditions of II.5.1, suppose that $\kappa(x)$ is a **finite separable** extension of $k$, and
that the $f_{i}$, $1 \leq i \leq n$, define elements of $\mathfrak{m}_{x}$. Then the preceding conditions are equivalent
to:

1. The $f_{i}$ form a system of generators of $\mathfrak{m}_{x}$; equivalently, the $f_{i}$ modulo
   $\mathfrak{m}^{2}_{x}$ form a basis of $\mathfrak{m}_{x}/\mathfrak{m}^{2}_{x}$ over $\kappa(x)$.

Indeed, (iv) ⇒ (iii) by the exact sequence

$$
\mathfrak{m}_{x}/\mathfrak{m}^{2}_{x} \to \Omega^{1}_{\mathcal{O}_{x}/k} \to \Omega^{1}_{\kappa(x)/k} \to 0
$$

<!-- label: eq:II.5.1 -->

and the fact that $\Omega^{1}_{\kappa(x)/k} = 0$, since $\kappa(x)$ is étale over $k$. On the other hand, (ii) implies
(iv), because since $X$ and $\operatorname{Spec}(\kappa(x))$ are smooth over $k$ at $x$, one may put a 0 on the left in
the preceding exact sequence by II.4.10 (iv).

**Corollary.**

<!-- label: II.5.3 -->

Let $x$ be a point of $X$, of finite type over $k$. If $X$ is smooth over $k$ at $x$, then $\mathcal{O}_{x}$ is regular;
the converse is true if $\kappa(x)$ is a finite separable extension of $k$.

Indeed, the converse follows from II.5.2 by taking a regular system $(f_{i})$ of generators of $\mathfrak{m}_{x}$.
Instead of II.5.2 one may also invoke Theorem II.4.15. We conclude:

**Proposition.**

<!-- label: II.5.4 -->

Let $X$ be a prescheme of finite type over $k$. If $X$ is smooth over $k$, then it is regular; the converse is true if
$k$ is perfect.

For the converse, note that by II.5.3, $X$ is smooth over $k$ at every closed point, hence everywhere, since the set of
points where it is smooth is open.

**Theorem.**

<!-- label: II.5.5 -->

Let $X$ be a prescheme of finite type over $k$, let $x$ be a point of $X$, let $n$ be the dimension of $X$ at $x$, and
let $k'$ be a perfect extension of $k$. The following conditions are equivalent:

1. $X$ is smooth over $k$ at $x$.
1. $\Omega^{1}_{X/k}$ is free of rank $n$ at $x$.
1. $\Omega^{1}_{X/k}$ is generated by $n$ elements at $x$.
1. $X$ is differentially smooth over $k$ at $x$.
1. There is an open neighborhood $U$ of $x$ such that $U \otimes_{k} k'$ is regular, i.e. the local rings of its points
   are regular.

We have (i) ⇒ (ii) by II.4.3 (ii), (ii) ⇒ (ii bis) trivially, and (ii bis) ⇒ (i) by II.5.1. Since $X$ is flat over $k$,
we have (i) ⇔ (iii) by II.4.18. We have (i) ⇒ (iv) because smoothness is invariant under extension of the base and
implies regularity; and (iv) ⇒ (i), because by Proposition II.5.4 one sees that $U \otimes_{k} k'$ is smooth over $k'$,
hence $U$ is smooth over $k$ by II.4.13.

Taking $x$ to be the generic point of $X$, supposed irreducible, one obtains:

**Corollary.**

<!-- label: II.5.6 -->

Let $K$ be a local Artin ring obtained by localizing an algebra of finite type over the field $k$; for example, $K$ may
be an extension of finite type of $k$. Let $n$ be the transcendence degree over $K$ of its residue field. The following
conditions are equivalent:

1. $K$ is a finite separable extension of a purely transcendental extension $k(t_{1},...,t_{n})$ of $k$.
1. $\Omega^{1}_{K/k}$ is a free $K$-module of rank $n$.
1. $\Omega^{1}_{K/k}$ is a $K$-module admitting $n$ generators.
1. The completion $O'$ of $K \otimes_{k} K$ for the topology defined by the powers of the augmentation ideal
   $K \otimes_{k} K \to K$ is a “regular” augmented $K$-algebra, i.e. isomorphic to a formal power-series algebra over
   $K$. If $K$ is a field, this is equivalent to saying that $O'$ is a regular local ring.
1. $K$ is a separable extension of $k$.

Indeed, one may always regard $K$ as the local ring of the generic point of an irreducible scheme $X$ of finite type
over $k$, and the conditions under consideration are the conditions with the same names in II.5.5, taking in (iv) an
algebraically closed extension of $k$ for $k'$. Only the implication “$K$ separable over $k$ ⇒ $X$ smooth over $k$ at
$x$” requires a proof. By II.4.13 one is immediately reduced to the case where the base field is $k'$, hence
algebraically closed, and therefore where there exists a point $a$ of $X$ rational over $k$. But then $X$ is smooth over
$k$ at $a$ by II.5.4, and a fortiori it is smooth over $k$ at the generic point $x$.[^ii-5-6-1]

One will notice that in the case where $K$ is an extension of finite type of $k$, the equivalence of (i), (ii), (ii
bis), and (iv) is well known, but that we have not used any of these already-known equivalences. Of course Proposition
II.5.1 contains as a special case the well-known fact that a sequence of elements $x_{i}$, $1 \leq i \leq n$, is a
“separating transcendence basis” of $K$ over $k$ if and only if the $d x_{i}$ form a basis of the $K$-module
$\Omega^{1}_{K/k}$.

**Corollary.**

<!-- label: II.5.7 -->

Let $X$ be a prescheme of finite type over a field $k$. In order that $X$ be smooth over $k$, it is necessary and
sufficient that $\Omega^{1}_{X/k}$ be locally free and that the local rings at the generic points of the irreducible
components of $X$ be separable extensions of $k$. The latter condition is automatically satisfied if $k$ is perfect and
$X$ is reduced.

We may suppose $X$ connected, and let $n$ be the rank of $\Omega^{1}_{X/k}$, assumed locally free. By the hypothesis and
II.5.6, this is also the transcendence degree of the extensions of $k$ defined by the local rings at the generic points
of $X$. Hence all irreducible components of $X$ have dimension $n$. We then conclude by II.5.5.

Care must be taken that if $K$ is a finite, not necessarily separable, extension of $k$, then $\Omega^{1}_{K/k}$ is a
free $k$-module; hence, putting $X = \operatorname{Spec}(K)$, $\Omega^{1}_{X/k}$ is a locally free sheaf and $X$ is
reduced, without $X$ necessarily being smooth over $k$. Extending scalars then to the algebraic closure of $k$, one
obtains an analogous example where $k$ is algebraically closed, but $X$, in contrast, is not reduced.

**Corollary.**

<!-- label: II.5.8 -->

Let $X$ be a prescheme of finite type over the field $k$, let $x$ be a point of $X$, let $n$ be the dimension of $X$ at
$x$, and let $p$ be the dimension of $\mathcal{O}_{x}$, i.e. the codimension in $X$ of the closure $Y$ of $x$ in $X$;
thus $n - p$ is the transcendence degree of $\kappa(x)$ over $k$. Let $f_{i}$, $1 \leq i \leq n$, be elements of
$\mathcal{O}_{x}$, with $f_{i} \in \mathfrak{m}_{x}$ for $1 \leq i \leq p$. The following conditions are equivalent:

1. The germ at $x$ of the morphism

$$
X \to \operatorname{Spec}(k[t_{1},...,t_{n}])
$$

defined by the $f_{i}$ is étale at $x$. 2. The $f_{i}$, $1 \leq i \leq p$, generate $\mathfrak{m}_{x}$, i.e. form a
regular system of parameters of $\mathcal{O}_{x}$, and the classes in $\kappa(x)$ of the $f_{j}$, $p + 1 \leq j \leq n$,
form a separating transcendence basis; equivalently, the $d \bar{f}_{j}$, $p + 1 \leq j \leq n$, form a basis of
$\Omega^{1}_{\kappa(x)/k}$, or again generate $\Omega^{1}_{\kappa(x)/k}$.

Suppose (i) holds. It follows that the $d f_{i}(x)$ form a basis of $\Omega^{1}_{X/k}(x)$ by II.4.8; hence their images
$d \bar{f}_{i}(x)$ in $\Omega^{1}_{\kappa(x)/k}$ generate this vector space over $k$. Since the $\bar{f}_{i}$ for
$1 \leq i \leq p$ are zero, it follows that it suffices to take the $d \bar{f}_{i}(x)$ with $p + 1 \leq i \leq n$. Since
the transcendence degree of $\kappa(x)$ over $k$ is $n - p$, Corollary II.5.6, criterion (iii), applied to
$K = \kappa(x)$, then implies that $Y$ is smooth over $k$ at its generic point $x$, and that the $d \bar{f}_{i}(x)$,
$p + 1 \leq i \leq n$, form a **basis** of $\Omega^{1}_{\kappa(x)/k}$ over $\kappa(x)$. Consequently condition (ii) of
II.4.9 is satisfied, hence also condition (iii), and in particular the $f_{i}$, $1 \leq i \leq p$, form a system of
generators of $\mathfrak{m}_{x}$. Since $\mathcal{O}_{x}$ has dimension $p$, they therefore form a regular system of
parameters at $x$. This proves (ii).

Suppose (ii) holds. By the exact sequence II.5.1, it follows that the $d f_{i}(x)$ generate $\Omega^{1}_{X/k}$; hence
(i) follows from Proposition II.5.1.

**Corollary.**

<!-- label: II.5.9 -->

Let $X$ be a prescheme of finite type over the field $k$, let $x$ be a point of $X$, let $n$ be the dimension of $X$ at
$x$, and let $p$ be the dimension of $\mathcal{O}_{x}$, i.e. the codimension of the closure $Y$ of $x$ in $X$; thus
$n - p$ is the transcendence degree of $\kappa(x)$ over $k$. The following conditions are equivalent:

1. $\mathcal{O}_{x}$ is regular and $\kappa(x)$ is a separable extension of $k$.
1. $X$ is smooth over $k$ at $x$, and the canonical homomorphism

```text
𝔪_x/𝔪_x² → Ω¹_{𝒪_x/k} ⊗_{𝒪_x} κ(x) = Ω¹_{X/k}(x)
```

is injective. 3. There are $f_{i} \in \mathcal{O}_{x}$, $1 \leq i \leq n$, with $f_{i} \in \mathfrak{m}_{x}$ for
$1 \leq i \leq p$, such that the germ at $x$ of the morphism from $X$ to $\operatorname{Spec}(k[t_{1},...,t_{n}])$
defined by the $f_{i}$ is étale at $x$; equivalently, by II.5.1, such that the $d f_{i}(x)$ generate
$\Omega^{1}_{X/k}(x)$. 4. There are $f_{i} \in \mathcal{O}_{x}$, $1 \leq i \leq n$, such that the $f_{i}$,
$1 \leq i \leq p$, generate $\mathfrak{m}_{x}$ and the $d f_{j}(x)$, $p + 1 \leq j \leq n$, generate
$\Omega^{1}_{\kappa(x)/k}$ over $\kappa(x)$.

The equivalence of (iii) and (iv) follows from Corollary II.5.8. By II.4.9, these conditions are also equivalent to the
fact that $X$ is smooth over $k$ at $x$ and that condition (ii) of II.4.10 is satisfied. Thus they are equivalent to the
fact that $X$ is smooth over $k$ at $x$ and that condition (iv) of II.4.10 is satisfied, hence to II.5.9 (ii). Or
equivalently, to the fact that $X$ is smooth over $k$ at $x$ and that condition (i) of II.4.10 is satisfied, which here
simply means that $\kappa(x)$ is separable over $k$. This implies II.5.9 (i). It remains to prove that II.5.9 (i)
implies it, i.e. to prove:

**Corollary.**

<!-- label: II.5.10 -->

Let $x$ be a point of a prescheme of finite type over the field $k$, such that $\kappa(x)$ is separable over $k$. In
order that $X$ be smooth over $k$ at $x$, it is necessary and sufficient that it be regular at $x$, i.e. that the local
ring $\mathcal{O}_{x}$ be regular.

Indeed, if this is so, one can evidently find $f_{i} \in \mathcal{O}_{x}$, $1 \leq i \leq n$, satisfying condition
II.5.9 (iv).

### Errata

<!-- label: II.fin.errata -->

<!-- original page 57 -->

In the present number, in the proof of II.5.6, we used the fact that a nonempty reduced scheme of finite type over an
algebraically closed field has at least one regular, hence smooth, point, a fact usually proved by differential means,
via Zariski's theorem that the set of regular points of $X$ is open. If one wants to avoid a vicious circle, one must
prove that if $K/k$ is a separable extension of finite type, and if the $f_{i} \in K$ are such that $d_{K/k} f_{i}$ form
a basis of $\Omega^{1}_{K/k}$, $1 \leq i \leq n$, then $n$ is the transcendence degree of $K$ over $k$, i.e. the $f_{i}$
are algebraically independent. The proof of this fact using Mac Lane's criterion is well known; cf. Bourbaki, Algebra,
Chapter V, paragraph 9, theorem 2. One takes a polynomial $g \in k[t_{1},...,t_{n}]$ of minimal degree such that
$g(f_{1},...,f_{n}) = 0$. We then have

```text
Σ_i (∂g/∂t_i)(f₁,...,f_n) d f_i = 0.
```

Hence, since the $d f_{i}$ form a basis of $\Omega^{1}_{K/k}$, the $\partial g/\partial t_{i}$ vanish at
$(f_{1},...,f_{n})$, and therefore are zero by the minimality of $g$. Thus if $k$ has characteristic 0, one has $g = 0$,
while if $k$ has characteristic $p \neq 0$, one has $g = h(t^{p}_{1},...,t^{p}_{n})$. Using Mac Lane's criterion, one
sees that the polynomial $h \in k[t_{1},...,t_{n}]$ also vanishes at $(f_{1},...,f_{n})$, whence again $g = 0$ by the
minimality of $g$.

<!-- end of Exposé II source block: next chapter begins at smf_doc-math_3_01.tex line 4492 -->

[^II-1-1]: Older terminology: $f$ is simple at $x$, or $x$ is a simple point for $f$. This terminology led to confusion
    in various contexts, such as simple algebras and simple groups, and had to be abandoned.

[^II-1-2]: It is better then to say, as in EGA IV 18.6.1, that $B$ is “essentially smooth” over $A$.

[^II-2-1]: Cf. EGA IV 7.8.

[^II-2-2]: Cf. EGA IV 5.12.10.

[^II-3-1]: For these formulas, cf. EGA IV 6.1 and 6.3.

[^ii-4-14-1]: We would now rather say “$A$-regular sequence”, cf. EGA 0_IV 15.1.7 and 15.1.11.

[^ii-4-14-2]: As was said in the preface, this has now been done; cf. EGA IV 17, 18.

[^ii-4-18-1]: For everything concerning the present paragraph, one may consult EGA IV 16.8 to 16.12.

[^ii-4-19-1]: This is the terminology adopted in EGA 0_IV 15.1.7.

[^ii-5-6-1]: Cf. the Errata at the end of the present Exposé II, p. 57 in the original numbering.


<!-- SOURCE: 03-morphismes-lisses-proprietes-de-prolongement.md -->

# Exposé III. Smooth Morphisms: Extension Properties

<!-- label: III -->

<!-- original page 58 -->

## 1. Formally Smooth Homomorphisms

<!-- label: III.1 -->

In II, we limited ourselves to homomorphisms of finite type and, consequently, in local homomorphisms $A \to B$ of local
rings, to the case where B is isomorphic to a localization of an A-algebra of finite type. This case is insufficient for
various applications, notably in formal geometry or analytic geometry. For example, the formal power-series ring
$B = A[[t_{1},...,t_{n}]]$ has, from the point of view of formal geometry, the properties of a smooth algebra over A. In
analytic geometry, the same is true of the local ring of a point (y,z) of a product $Y \times \mathbb{C}^{n}$, regarded
as an algebra over the local ring of y; moreover, the completion of this algebra is isomorphic to the algebra of formal
power series in n indeterminates over the completion of the base ring $\mathcal{O}_{x}$. This leads to the following
definition.

**Definition.**

<!-- label: III.1.1 -->

Let $u: A \to B$ be a local homomorphism of local rings, noetherian as recalled. Suppose that $\kappa(B)$ is finite over
$\kappa(A)$. We say that u is a **formally smooth homomorphism**, or that the algebra B is **formally smooth over** A,
if there exists a local finite $\bar{A}$-algebra $A'$, free over $\bar{A}$, such that the local components of the
semi-local ring $\bar{B} \otimes_{\bar{A}} A' = B'$ are $A'$-isomorphic to algebras of formal power series over
$A'$.[^iii-1-1-1]

Here $\bar{A}$ and $\bar{B}$ denote the completions of A and B. Since $B'$ is finite and free over $\bar{B}$, it is
indeed a semi-local ring, a direct sum of complete local rings, each of which is still a free module over $\bar{B}$,
hence has the same dimension as $\bar{B}$, and therefore as B. It follows that the number of variables $t_{i}$ in the
formal power-series rings considered in III.1.1 is equal to `dim B̄ − dim Ā = dim B − dim A`, and in particular is
independent of the local component chosen. One sees at once that it is also the dimension of the ring
$B \otimes k = B/\mathfrak{m}B$, where $k = A/\mathfrak{m}$ is the residue field of A; we shall call it the **relative
dimension of** B **with respect to** A.

<!-- original page 59 -->

**Remarks.**

<!-- label: III.1.2 -->

It is clear that Definition III.1.1 depends only on the homomorphism on completions $\bar{A} \to \bar{B}$ deduced from
$A \to B$, which justifies the terminology to some extent. We repent here of Definitions I.3.2 b) and I.4.1 b), which
risk being misleading, and prefer to say “formally unramified” and “formally étale” in the cases considered in those
definitions, reserving the terminology “unramified” and “étale” for the case where B is a localization of an A-algebra
of finite type.[^iii-1-2-1] The reader will immediately verify that “formally étale” is equivalent to “formally smooth
and quasi-finite”. Finally, let us point out that there is a reasonable definition of “formally smooth” without any
prior hypothesis on the residual extension $\kappa(B)/\kappa(A)$, supposed finite here, encompassing among others the
local homomorphisms $A \to B$ such that B is **flat** over A and $B/\mathfrak{m}B$ is a **separable extension** of
$A/\mathfrak{m} = k$, not necessarily of finite type. For example, a Cohen p-ring is formally smooth over the ring of
p-adic integers. It is the lifting property for homomorphisms, compare III.2.1, that should become the definition in
this general case. For the applications we have in view, the case treated in Definition III.1.1 will suffice; in what
follows, in “formally smooth” we shall understand “with finite residual extension”.

**Lemma.**

<!-- label: III.1.3 -->

If B is formally smooth over A, then B is flat over A.

Since flatness is invariant under completion, we may suppose A and B complete. Since flatness is invariant under a local
flat, hence faithfully flat, extension of the base ring, Definition III.1.1 reduces us to the case where B is a formal
power-series algebra over A. But then, as an A-module, B is isomorphic to a product of A-modules isomorphic to A; hence,
since the base ring A is noetherian, B is A-flat as a product of flat A-modules.

Let us place ourselves under the conditions of III.1.1. Since the residual extensions of the local components of $B'$
over $A'$ are trivial, it follows that $L \otimes_{k} k'$ is an artinian $k'$-algebra whose local components have
trivial residual extensions, where L, k, $k'$ are the residue fields of A, B, and $A'$. This necessary condition for the
finite free extension $A'$ to satisfy the condition stated in III.1.1 is also sufficient, as follows at once from
III.1.4 (i) and III.1.5 below.

<!-- original page 60 -->

**Proposition.**

<!-- label: III.1.4 -->

Let $A \to B$ be a local homomorphism of local rings with finite residual extension, and let $A'$ be a finite local
A-algebra over A, so that $B' = B \otimes_{A} A'$ is finite over B and hence is a semi-local ring, also noetherian.

1. If B is formally smooth over A, then the localizations of $B'$ at its maximal ideals are formally smooth over $A'$.
1. The converse is true if $A'$ is free over A.

We are immediately reduced to the case where A and B are complete.

For (i), let $A''$ be a finite free local extension of A such that the local components of $B'' = B \otimes_{A} A''$ are
formal power-series algebras over $A''$. Extending scalars $A'' \to A'' \otimes_{A} A' \to A'''$, where $A'''$ is a
local component of $A'' \otimes_{A} A'$, one sees that the local components of
$B'' \otimes_{A''} A''' = B \otimes_{A} A'''$ are formal power-series algebras over $A'''$. But we also have

```text
B ⊗_A A‴ = (B ⊗_A A′) ⊗_{A′} A‴ = B′ ⊗_{A′} A‴.
```

Moreover, since $A''$ is free over A, $A'' \otimes_{A} A'$ is free over $A'$, and consequently so is $A'''$, which is a
direct factor of it. This proves that $B'$ is formally smooth over $A'$.

For (ii), let $A''$ be a finite free local $A'$-algebra such that the local components of
$B' \otimes_{A'} A'' = B \otimes_{A} A''$ are formal power-series algebras over $A''$. Since $A'$ is free over A, so is
$A''$; hence B is formally **smooth** over A.

**Proposition.**

<!-- label: III.1.5 -->

Let $A \to B$ be a local homomorphism of local rings with **trivial** residual extension. In order that B be formally
smooth over A, it is necessary and sufficient that $\bar{B}$ be isomorphic to a formal power-series algebra over
$\bar{A}$.

Only the necessity has to be proved, and we may suppose A and B complete. Let $\mathfrak{m}$ and $\mathfrak{n}$ be the
maximal ideals of A and B, respectively, and let $t_{1},...,t_{n}$ be elements of $\mathfrak{n}$ defining a basis of the
vector space

$$
(\mathfrak{n}/\mathfrak{n}^{2})/Im(\mathfrak{m}/\mathfrak{m}^{2}) = \mathfrak{n}/(\mathfrak{n}^{2} + \mathfrak{m}B).
$$

These elements therefore define a homomorphism of local A-algebras

$$
B_{1} = A[[t_{1},...,t_{n}]] \to B.
$$

We prove that it is an isomorphism. It suffices to prove that for every power $\mathfrak{m}^{q}$ of $\mathfrak{m}$, one
obtains an isomorphism after reducing modulo $\mathfrak{m}^{q}$, since $B_{1}$ and B are the projective limits of the
corresponding rings reduced modulo $\mathfrak{m}^{q}$, with q variable. Since B and $B_{1}$ are flat A-modules, the
graded rings associated with the $\mathfrak{m}$-adic filtration are obtained by tensoring over $k = A/\mathfrak{m}$ with
$gr(A)$ the rings $B_{1}/\mathfrak{m}B_{1}$ and $B/\mathfrak{m}B$, respectively. We are thus reduced to showing that
$B_{1}/\mathfrak{m}B_{1} \to B/\mathfrak{m}B$ is an isomorphism. Taking III.1.3 into account, we are thereby reduced to
the case where A is a **field** k. On the other hand, if $A'$ is a finite free local A-algebra such that
$B \otimes_{A} A'$ is a formal power-series algebra over $A'$, note that this algebra is local since the residual
extension of B over A is trivial. To prove that $B_{1} \to B$ is an isomorphism, it suffices to prove that
$B_{1} \otimes_{A} A' \to B \otimes_{A} A'$ is one. This reduces us to the case where B is already a formal power-series
algebra; this reduction should have been made first, before reducing to the case of a base field. But then B is a
regular local ring with coefficient field k, and it is well known, and immediate by considering the graded rings
associated with the $\mathfrak{n}_{1}$-adic and $\mathfrak{n}$-adic filtrations on $B_{1}$ and B, that $B_{1} \to B$ is
an isomorphism. This completes the proof.

**Corollary.**

<!-- label: III.1.6 -->

If B is formally smooth over A, then there exists a finite local A-algebra $A'$ such that the local components of

```text
B̄ ⊗_{Ā} A′̄ = completion of (B ⊗_A A′)
```

are isomorphic to formal power-series algebras over $A\bar{'}$.

Indeed, if L/k is the residual extension of B/A, consider an extension $k'/k$ such that the residual extensions in the
$k'$-algebra $L \otimes_{k} k'$ are trivial. Let $A'$ be an algebra finite and free over A such that
$A'/\mathfrak{m}A' = k'$; one knows that such an algebra exists, for example by reducing step by step to the case where
$k'/k$ is monogenic, and then lifting to A the coefficients of the minimal polynomial of a generator of $k'$ over k. It
is local. Then $B \otimes_{A} A'$ has, at its maximal ideals, trivial residual extensions over that $k'$ of $A'$, and
the conclusion follows with the help of III.1.5.

**Corollary.**

<!-- label: III.1.7 -->

Let $A \to B$ be a local homomorphism of local rings. In order that B be formally smooth over A, it is necessary and
sufficient that B be flat over A and that $B/\mathfrak{m}B$ be formally smooth over $k = A/\mathfrak{m}$.

Making a suitable finite free local extension $A'$ of A and using III.1.4 (ii), we are reduced to the case where the
residual extension of B/A is trivial. We know moreover by III.1.4 (i) and III.1.3 that the stated conditions are
necessary. For the sufficiency, it suffices to observe that the proof of III.1.5 proves, under the hypotheses made here,
that B is a formal power-series algebra over A, supposing A and B complete, which is permissible.

<!-- original page 62 -->

**Remark.**

<!-- label: III.1.8 -->

It would not be difficult to develop, for formally smooth homomorphisms, the analogue of all the properties of smooth
morphisms studied in II. For the differential properties, however, this requires a modification of the usual definition
of Kähler differentials, cf. I.1, with completed tensor products replacing ordinary tensor products. We shall content
ourselves with evoking these abysses here, what precedes being sufficient for our purpose.

It remains to make the link between formal smoothness and the notion of smoothness developed in II, which we have not
yet used at all.

**Proposition.**

<!-- label: III.1.9 -->

Let $A \to B$ be a local homomorphism, with B a localization of an A-algebra of finite type. In order that B be smooth
over A, it is necessary and sufficient that it be formally smooth over A.

Using III.1.7 and II.2.1, we are reduced to the case where A is a field.

Using III.1.4 (ii) and II.4.13, a suitable extension $k'$ of k reduces us to the case where the residual extension for
B/k is trivial. By III.1.5, respectively II.5.2, B is smooth over k, respectively formally **smooth over** k, if and
only if B is a regular local ring, respectively its completion is a formal power-series algebra over k. But it is well
known that these two conditions are equivalent when the residual extension is trivial.

## 2. The Lifting Property Characteristic of Formally Smooth Homomorphisms

<!-- label: III.2 -->

**Theorem.**

<!-- label: III.2.1 -->

Let $A \to B$ be a local homomorphism of local rings defining a finite residual extension. The following conditions are
equivalent:

1. B is formally smooth over A.
1. For every local homomorphism $A \to C$, where C is a **complete** local ring, every ideal J of C contained in the
   radical $\mathfrak{r}(C)$, and every local A-homomorphism $B \to C/J$, there exists an A-homomorphism, necessarily
   local, $B \to C$ lifting it.
1. For every A-algebra C, not necessarily noetherian, every nilpotent ideal J of C, and every continuous A-homomorphism
   $B \to C/J$, i.e. one vanishing on a power of $\mathfrak{r}(B)$, there exists an A-homomorphism $B \to C$,
   necessarily continuous as well, lifting it.
1. The same statement as (ii) and (iii), but with C a local artinian ring finite over A.
1. As in (iv), but with J moreover square-zero.

**Remark.** For the rest of this exposé, we shall use only the implication (iv) ⇒ (i), or (iv bis) ⇒ (i). The direct
implication (i) ⇒ (ii) will be proved by another method in the next number when B is a localization of an algebra of
finite type over A. Recall that in the “good” theory of Cohen theorems,[^iii-2-1-1] property (ii) or (iii) becomes the
definition of formally smooth homomorphisms, while III.1.1 becomes a characteristic property valid only in the case of a
finite residual extension. Care should be taken that neither of properties (ii) and (iii) is more general than the
other. One could give an equivalent property covering both by introducing a linearly topologized ring C, **separated**
and **complete**, a **closed topologically nilpotent** ideal of C, and a continuous homomorphism $A \to C$, thus making
C a topological A-algebra; we leave this modification to the reader.

**Proof of III.2.1.** We shall prove (i) ⇒ (iii) ⇒ (ii), then (iv) ⇒ (i). Since (ii) ⇒ (iv) is trivial, and the
equivalence of (iv) and (iv bis) is seen by an immediate induction on the integer n such that $J^{n} = 0$, this will
finish the proof.

(i) ⇒ (iii). An immediate induction reduces us to the case J² = 0. Since C is finite over A, some power
$\mathfrak{m}^{q}$ of the maximal ideal of A annihilates C. Dividing by $\mathfrak{m}^{q}$, and noting that
$B/\mathfrak{m}^{qB}$ is still formally smooth over $A/\mathfrak{m}^{q}$ by III.1.4 (i), we may suppose A artinian.
Since B is flat over A by III.1.3, B **is free over** A because A is artinian. Thus there exists an **A-module
homomorphism**

$$
w: B \to C
$$

lifting the given homomorphism $u: B \to C/J$. Put

```text
f(x,y) = w(xy) − w(x)w(y),     x,y ∈ B.
```

Then f(x,y) ∈ J, and f is therefore an A-bilinear map from $B \times B$ to J. For there to exist a lift $v: B \to C$ of
u that is an algebra homomorphism, it is necessary and sufficient that there exist an A-linear map $g: B \to J$ such
that $v = w + g$ is an algebra homomorphism, which is written

```text
g(1) = 1 − w(1),
g(xy) − u(x)g(y) − u(y)g(x) = −f(x,y),     x,y ∈ B.
```

This is a system of **linear** equations in $\operatorname{Hom}_{A}(B,J)$, with right-hand sides in J. Hence it has a
solution if and only if the corresponding system in $\operatorname{Hom}_{A}(B,J) \otimes_{A} A'$, with right-hand sides
in $J' = J \otimes_{A} A'$, has a solution, where $A'$ denotes a faithfully flat algebra over A. Let $A'$ be an algebra
finite and free over A, local, such that $B' = B \otimes_{A} A'$ is a formal power-series algebra over $A'$. In our
proof we may suppose A and B complete, as is immediately checked. Since $A'$ is free of finite type over A, we have

```text
Hom_A(B,J) ⊗_A A′ = Hom_{A′}(B′,J′),
```

and one verifies that the system of equations obtained in $\operatorname{Hom}_{A'}(B',J')$ is the one that determines
the homomorphisms of $A'$-algebras $B' \to C' = C \otimes_{A} A'$ lifting the homomorphism $u': B' \to C'/J'$ deduced
from u by extension of scalars, by “correcting” by an $A'$-module homomorphism $g': B' \to J'$ the $A'$-module
homomorphism $w': B' \to C'$ deduced from w by extension of scalars. Note that B generates $B'$ as an $A'$-module. We
are thereby reduced to proving (iii) when B is a **formal power-series algebra** over A, $B = A[[t_{1},...,t_{n}]]$.
Lift arbitrarily the images in C/J of the $t_{i}$ to elements $z_{i}$ of C. Since the $z_{i}$ modulo J are nilpotent,
$u: B \to C/J$ being continuous, the $z_{i}$ themselves are nilpotent, since J is nilpotent. Thus the $z_{i}$ define a
continuous homomorphism of topological A-algebras from B to the discrete ring C, evidently lifting u, as required.

(iii) ⇒ (ii). Let $\mathfrak{n}$ be the maximal ideal of C, and for every integer q > 0 put

```text
C_q = C/𝔫^q,    J_q = (J + 𝔫^q)/𝔫^q.
```

Thus $C_{q}/J_{q}$ identifies with a quotient algebra of C/J. On the other hand, the composite homomorphism
$u_{q}: B \to C/J \to C_{q}/J_{q}$ is continuous from B to the discrete ring $C_{q}/J_{q}$, and $J_{q}$ is a nilpotent
ideal in $C_{q}$. We then construct, step by step, A-homomorphisms

$$
v_{q}: B \to C_{q}
$$

such that (a) $v_{q}$ lifts $u_{q}$ and (b) $v_{q}$ lifts $v_{q-1}$. The possibility of the induction is checked easily:
since

```text
u_q: B → C/(J + 𝔫^q)     and     v_{q−1}: B → C/𝔫^{q−1}
```

define the same homomorphism

```text
B → C/((J + 𝔫^q) + 𝔫^{q−1}) = C/(J + 𝔫^{q−1}) = C_{q−1}/J_{q−1},
```

namely $u_{q-1}$, they define a homomorphism

```text
B → C/J′_q,    where J′_q = (J + 𝔫^q) ∩ 𝔫^{q−1} ⊃ 𝔫^q,
```

from which both arise by reduction. We are therefore reduced to lifting a homomorphism $B \to C/J'_{q}$ from B into a
quotient of $C_{q}$ by an ideal $J'_{q}/\mathfrak{n}^{q}$ contained in $J_{q}$, hence nilpotent; this is possible by
hypothesis (iii).

This done, the $v_{q}$ define a homomorphism from B into the projective limit C of the $C_{q}$. Since J is closed, J is
the projective limit of the $J_{q}$; hence v lifts u, as required.

(iv) ⇒ (i). First one observes at once that if (iv) holds, then (iv) remains true for the local components of
$B \otimes_{A} A'$ over $A'$, if $A'$ is a finite local algebra over A. Taking $A'$ free over A and such that the
residual extensions of $B'$ over $A'$ are trivial, we are reduced, by III.1.4 (ii), to the case where the residual
extension of B over A is trivial. We shall then prove the slightly more precise result:

**Corollary.**

<!-- label: III.2.2 -->

Under the conditions of III.2.1, suppose moreover that the residual extension of B over A is trivial. Then the
equivalent conditions of III.2.1 are also equivalent to the following two conditions, supposing in (v) that A and B are
complete:

1. As in (iv), but with the local artinian ring C finite over A restricted to have trivial residual extension; and
   moreover, if one wants, with the ideal J square-zero.
1. There exists a local A-homomorphism, where $n = \dim \mathfrak{n}/(\mathfrak{n}^{2} + \mathfrak{m}B)$,

```text
u: B → B₁ = A[[t₁,...,t_n]]
```

inducing an **isomorphism**

```text
𝔫/(𝔫² + 𝔪B) → 𝔫₁/(𝔫₁² + 𝔪B₁),
```

where $\mathfrak{n}$ and $\mathfrak{n}_{1}$ are the maximal ideals of B and $B_{1}$, respectively, and $\mathfrak{m}$ is
that of A.

**Proof.** Since (iv bis) evidently implies (iv ter), setting aside the square-zero-ideal joke, it will suffice to prove
(iv ter) ⇒ $(v) \Rightarrow (i)$.

For (iv ter) ⇒ (v), choose a basis $a_{1},...,a_{n}$ of $\mathfrak{n}/(\mathfrak{n}^{2} + \mathfrak{m}B)$. This
therefore defines a local homomorphism of A-algebras

```text
B → B₁/(𝔫₁² + 𝔪B₁) = k[t₁,...,t_n]/(t₁,...,t_n)²,
```

which can be lifted step by step, by (iv ter), to homomorphisms of A-algebras from B into $B_{1}/\mathfrak{n}^{2}_{1}$,
$B_{1}/\mathfrak{n}^{3}_{1}$, and so on; passing to the projective limit gives the homomorphism $B \to B_{1}$ with the
desired property.

For $(v) \Rightarrow (i)$, in the commutative diagram

```text
𝔪/𝔪² → 𝔫/𝔫² → 𝔫/(𝔫² + 𝔪B) → 0
↓       ↓       ↓
𝔪/𝔪² → 𝔫₁/𝔫₁² → 𝔫₁/(𝔫₁² + 𝔪B₁) → 0
```

the two rows are exact, and the extreme vertical arrows are surjective; the middle arrow is therefore surjective, and it
follows, since B is complete, that $B \to B_{1}$ is **surjective**. Let $x_{i}$, $1 \leq i \leq n$, be elements of B
lifting the $t_{i}$. They define a homomorphism of A-algebras $B_{1} \to B$, which is surjective for the same reason as
u, and whose composite with u is the identity by construction. Thus $B_{1} \to B$ is also injective, and consequently is
an isomorphism. We obtain:

**Corollary.**

<!-- label: III.2.3 -->

Under the conditions of III.2.2 (v), u is necessarily an isomorphism.

This finishes the proof that B is formally smooth over A. At the same time we have recovered III.1.5, though there is
little merit in that.

## 3. Local Infinitesimal Extension of Morphisms into a Smooth S-Scheme

<!-- label: III.3 -->

**Theorem.**

<!-- label: III.3.1 -->

Let $f: X \to Y$ be a morphism locally of finite type. The following conditions are equivalent:

1. f is smooth.
1. For every prescheme $Y'$ over Y, every closed sub-prescheme $Y'_{0}$ of $Y'$ having the same underlying space as
   $Y'$, every Y-morphism $g_{0}: Y'_{0} \to X$, and every $z \in Y'_{0}$, there exists an open neighborhood U of z in
   $Y'$ and an extension g of $g_{0}|_{Y'_{0} \cap U}$ to a Y-morphism $U \to X$.
1. For $Y'$, $Y'_{0}$, and z as in (ii), putting $X' = X \times_{Y} Y'$ and $X'_{0} = X \times_{Y} Y'_{0}$, every
   section of $X'_{0}$ over $Y'_{0}$ extends to a section of $X'$ over an open neighborhood U of z.
1. For every Y-scheme $Y'$ that is the spectrum of a local artinian ring finite over some $\mathcal{O}_{y}$, with
   $y \in Y$, every nonempty closed sub-prescheme $Y'_{0}$ of $Y'$, and every Y-morphism $g_{0}: Y'_{0} \to X$, there
   exists a Y-morphism $g: Y' \to X$ extending $g_{0}$.
1. For every $Y'$ and $Y'_{0}$ as in (iii), putting $X' = X \times_{Y} Y'$ and $X'_{0} = X \times_{Y} Y'_{0}$, every
   section of $X'_{0}$ over $Y'_{0}$ extends to a section of $X'$ over $Y'$.

**Proof.** The equivalence of (ii) and (ii bis), on the one hand, and of (iii) and (iii bis), on the other, is trivial,
as is the implication (ii) ⇒ (iii). It remains to prove (i) ⇒ (ii) and (iii) ⇒ (i).

(i) ⇒ (ii). Let $x = g_{0}(z)$. Replacing X by a suitable open neighborhood of x, and $Y'$ by the prescheme induced on
the open inverse image of the latter under $g_{0}$, we may suppose that X is étale over $Y[t_{1},...,t_{n}]$. Consider
the composite Y-morphism $Y'_{0} \to X \to Y[t_{1},...,t_{n}]$; it is defined by n sections of the sheaf
$\mathcal{O}_{Y'_{0}}$, which can therefore be extended in a neighborhood of z to sections of $\mathcal{O}_{Y'}$. Thus
we may suppose that the morphism in question has been extended to a Y-morphism $Y' \to Y[t_{1},...,t_{n}]$. By I.5.6,
there is then a unique Y-morphism $g: Y' \to X$ lifting the preceding one and at the same time extending $g_{0}$.

<!-- original page 68 -->

(iii) ⇒ (i). Since the set of points where f is smooth is open, it suffices to prove that it contains every $x \in X$
that is **closed** in its fiber. Let y = f(x). Then $\mathcal{O}_{x}$ is an algebra over $\mathcal{O}_{y}$, a
localization of an algebra of finite type, with finite residual extension. On the other hand, hypothesis (iii) implies
that every homomorphism from $\mathcal{O}_{x}$ into an algebra A/J, where A is a local artinian algebra finite over
$\mathcal{O}_{y}$ and J is an ideal contained in its radical, lifts to a homomorphism from $\mathcal{O}_{x}$ into the
algebra A, taking into account that a morphism from $\operatorname{Spec}(B)$, with B local, into X is determined
bijectively by a local homomorphism from some $\mathcal{O}_{x}$, $x \in X$, into B. By III.2.1 it follows that
$\mathcal{O}_{x}$ is formally smooth over $\mathcal{O}_{y}$, hence smooth over $\mathcal{O}_{y}$ by III.1.9.

**Corollary.**

<!-- label: III.3.2 -->

Let $f: X \to Y$ be as in III.3.1. The following conditions are equivalent:

1. f is étale.
1. Condition (ii) of III.3.1 holds with **uniqueness** of the extension g of $g_{0}$ to U.
1. Condition (iii) of III.3.1 holds with **uniqueness** of g.

It suffices to note, in the proof of (i) ⇒ (ii) above, that one can have uniqueness, when $Y'_{0}$ is not identical to
$Y'$ in a neighborhood of z, only if $n = 0$, a condition that is known to be sufficient.

**Corollary.**

<!-- label: III.3.3 -->

Let X be a prescheme locally of finite type over a **complete** local ring A, let y be the closed point of
$Y = \operatorname{Spec}(A)$, and let x be a point of $f^{-1}(y)$ **rational** over $\kappa(y)$. If X is **smooth over A
at x**, then there exists a section s of X over Y “passing through x”, i.e. such that s(y) = x.

In particular, if X is smooth over A, then the natural map

```text
Γ(X/Y) → Γ(X ⊗_A k / k)
```

from sections of X over Y to the set of points of the fiber $f^{-1}(y) = X \otimes_{A} k$ rational over k is surjective.
This fact was especially well known and used when A is a discrete valuation ring and X is proper over A, in fact
projective over A. In that case the sections of X over Y, i.e. the “points of X with values in A”, also identify with
the rational sections, i.e. with the points of $X \otimes_{A} K = X_{K}$, which is a proper smooth scheme over K, with
values in K, the field of fractions of A; in other words, with the points of X rational over K.

## 4. Local Infinitesimal Extension of Smooth S-Schemes

<!-- label: III.4 -->

**Theorem.**

<!-- label: III.4.1 -->

Let Y be a locally noetherian prescheme, let $Y_{0}$ be a closed sub-prescheme with the same underlying space, let
$X_{0}$ be a smooth $Y_{0}$-prescheme, and let x be a point of $X_{0}$. Then there exist an open neighborhood $U_{0}$ of
x, a prescheme X smooth over Y, and a $Y_{0}$-isomorphism

```text
h: U₀ → X ×_Y Y₀.
```

Moreover, if `(U′₀`, $X'$, `h′)` is another solution of this problem, then “it is isomorphic to the first in a
neighborhood of x”.

We leave it to the reader to make precise what is meant by this. One may note that, for $U_{0}$ given, a solution of the
stated problem amounts to giving on $U_{0}$ a sheaf of algebras $\mathcal{B}$ over $f^{-1}_{0}(\mathcal{O}_{Y})$, where
$f_{0}$ is the continuous map underlying the structural morphism $U_{0} \to Y_{0}$, together with a homomorphism of
rings $\mathcal{B} \to \mathcal{O}_{U_{0}}$ compatible with the homomorphism
$f^{-1}(\mathcal{O}_{Y}) \to f^{-1}(\mathcal{O}_{Y_{0}})$, such that:

1. This homomorphism induces an isomorphism

```text
ℬ ⊗_{f⁻¹(𝒪_Y)} f⁻¹(𝒪_{Y₀}) → 𝒪_{Y₀}.
```

1. $U_{0}$ equipped with $\mathcal{B}$ becomes a smooth Y-prescheme.

In this way the precise meaning of the assertion of local uniqueness becomes particularly evident.

**Proof.** We may already suppose that $X_{0}$ is étale over some $Y_{0}[t_{1},...,t_{n}] = Y'_{0}$. But the latter may
be regarded as a closed sub-prescheme of $Y' = Y[t_{1},...,t_{n}]$ having the same underlying space. By I.8.3, there
exists an X étale over $Y'$ and a $Y'_{0}$-isomorphism $X \times_{Y'} Y'_{0} \to X'$. We have won existence. For
uniqueness, use property III.3.1 (ii) of smooth morphisms, taking into account the following lemma.

<!-- original page 70 -->

**Lemma.**

<!-- label: III.4.2 -->

Let Y be a prescheme, let $Y_{0}$ be a closed sub-prescheme defined by a locally nilpotent sheaf of ideals
$\mathcal{J}$, let X and $X'$ be Y-preschemes, and let $u: X \to X'$ be a Y-morphism. Suppose X is flat over Y. In order
that u be an isomorphism, it is necessary and sufficient that

```text
u₀: X ×_Y Y₀ → X′ ×_Y Y₀
```

be an isomorphism.

The proof is easy, by passing to the affine case and looking at associated graded rings. One should note moreover that
the analogous statement obtained by replacing “isomorphism” by “closed immersion” is also valid, and without the
flatness hypothesis.

**Remark.**

<!-- label: III.4.3 -->

It is essential to note that the local extension X obtained in III.4.1 **is not canonical**; in other words, the local
isomorphism between two solutions is not unique, i.e. in general there exist nontrivial Y-automorphisms of X inducing
the identity on the closed sub-prescheme $X_{0} = X \times_{Y} Y_{0}$. This is why, for the construction of **global**
infinitesimal extensions of smooth preschemes, one must expect the existence of an obstruction of cohomological nature,
which will be made precise below in III.6.

## 5. Global Infinitesimal Extension of Morphisms

<!-- label: III.5 -->

Let T be a topological space, let $\mathcal{G}$ be a sheaf of groups on X, and let $\mathcal{P}$ be a sheaf of sets on T
on which $\mathcal{G}$ acts, on the right to fix ideas. We say that $\mathcal{P}$ is **formally principal homogeneous**
under $\mathcal{G}$ if the familiar homomorphism

```text
𝒢 × 𝒫 → 𝒫 × 𝒫
```

of sheaves of sets, deduced from the operations of $\mathcal{G}$ on $\mathcal{P}$, is an **isomorphism**. This is
equivalent to saying that for every $x \in T$, $\mathcal{P}_{x}$ is **empty or a principal homogeneous space** under the
ordinary group $\mathcal{G}_{x}$; or also that for every open U of T, $\mathcal{P}(U)$ is empty or a principal
homogeneous space under the ordinary group $\mathcal{G}(U)$. We say that $\mathcal{P}$ is a **principal homogeneous
sheaf** under $\mathcal{G}$ if it is so formally and if, in addition, the $\mathcal{P}_{x}$ are nonempty; in other
words, if **all** the $\mathcal{P}_{x}$ are principal homogeneous spaces, hence nonempty, under the
$\mathcal{G}_{x}$.[^iii-5-0-1] Recall that the set of classes, up to isomorphism, of principal homogeneous sheaves under
$\mathcal{G}$ identifies with the cohomology set $H^{1}(T,\mathcal{G})$, which is also the usual cohomology group of T
with coefficients in $\mathcal{G}$ when $\mathcal{G}$ is commutative. Thus, for every principal homogeneous
$\mathcal{P}$, there is a characteristic class $c(\mathcal{P}) \in H^{1}(T,\mathcal{G})$, whose triviality is necessary
and sufficient for $\mathcal{P}$ to be trivial, i.e. isomorphic to $\mathcal{G}$, on which $\mathcal{G}$ acts by right
translations, or equivalently for $\mathcal{P}$ to have a section.

**Proposition.**

<!-- label: III.5.1 -->

Let S be a prescheme, let X and Y be preschemes over S, and let $Y_{0}$ be a closed sub-prescheme of Y defined by an
ideal $\mathcal{J}$ on Y **of square zero**. Let $g_{0}$ be an S-morphism from $Y_{0}$ to X, and let
$\mathcal{P}(g_{0})$ be the sheaf on Y whose sections on an open U are the extensions $g: U \to X$ of
$g_{0}|_{U \cap Y_{0}}$ to an S-morphism g. Then $\mathcal{P}(g_{0})$ is, naturally, a **formally principal
homogeneous** sheaf under the commutative sheaf of groups

$$
\mathcal{G} = \operatorname{Hom}_{\mathcal{O}_{Y_{0}}}(g_{0}*(\Omega^{1}_{X/S}), \mathcal{J}).
$$

Put $\mathcal{P} = \mathcal{P}(g_{0})$. For every open U of Y we must define a map

$$
\mathcal{P}(U) \times \mathcal{G}(U) \to \mathcal{P}(U)
$$

so that: for fixed $g \in \mathcal{P}(U)$, the map s ↦ gs from $\mathcal{G}(U)$ to $\mathcal{P}(U)$ is bijective;
$\mathcal{P}(U)$ becomes a set with group of operators $\mathcal{G}(U)$; and these maps are compatible with restriction
operators for an open $V \subset U$. The verification of the last point is trivial, so for simplicity we may suppose
$U = Y$. The verification of the second point, which is local if one wants, is left to the reader. We shall limit
ourselves, for a given $g \in \mathcal{P}(Y)$, to defining a natural bijection from $\mathcal{G}(Y)$ onto
$\mathcal{P}(Y)$. Thus suppose already given an S-morphism $g: Y \to X$, and seek a canonical bijection

$$
\operatorname{Hom}_{\mathcal{O}_{Y_{0}}}(g_{0}*(\Omega^{1}_{X/S}), \mathcal{J}) \to \mathcal{P}(Y),
$$

<!-- label: eq:III.5.1.* -->

where $\mathcal{P}(Y)$ is the set of S-morphisms $g'$ from Y to X inducing the same morphism $g_{0}: Y_{0} \to X$ as g.
Giving such a $g'$ is equivalent to giving an S-morphism $h: Y \to X \times_{S} X$ such that $pr_{1} \circ h = g$ and
$h \circ i = (g_{0},g_{0})$, where $pr_{1}: X \times_{S} X \to X$ is the first projection, $i: Y_{0} \to Y$ is the
canonical immersion, and $(g_{0},g_{0}): Y_{0} \to X \times_{S} X$ is the morphism $\Delta_{X/S} g_{0}$ with components
$g_{0},g_{0}:$

```text
Y₀ --h₀=(g₀,g₀)--> X ×_S X
|                         |
i                         pr₁
v                         v
Y  --------g----------->  X
```

Since $h_{0}$ factors through the diagonal immersion $\Delta_{X/S}$, and since Y is in the first-order infinitesimal
neighborhood of $Y_{0}$, i.e. $\mathcal{J}^{2} = 0$, the desired h necessarily factor, uniquely, through the first-order
infinitesimal neighborhood of the diagonal. This neighborhood identifies, as an X-prescheme via $pr_{1}$, with the
spectrum $X'$ of the sheaf of algebras $\mathcal{O}_{X} + \Omega^{1}_{X/S}$, where the second term is regarded as a
square-zero ideal; the diagonal morphism $X \to X'$ corresponds to the canonical augmentation of this sheaf of algebras.
Put $Y' = X' \times_{X} Y$ and $Y'_{0} = Y' \times_{Y} Y_{0} = X' \times_{X} Y_{0}$. The desired h are then in bijective
correspondence with sections u of $Y'$ over Y extending a given section $u_{0}$ of $Y'_{0}$ over $Y_{0}$. We may
moreover identify $Y'$ with the spectrum of the sheaf of algebras on Y

```text
𝒜 = g*(𝒪_X + Ω¹_{X/S}) = 𝒪_Y + g*(Ω¹_{X/S}),
```

and $Y'_{0}$ with the sheaf of algebras

```text
𝒜₀ = 𝒜 ⊗_{𝒪_Y} 𝒪_{Y₀} = 𝒪_{Y₀} + g₀*(Ω¹_{X/S}).
```

Then $u_{0}$ is the section defined by the canonical augmentation of $\mathcal{A}_{0}$ into $\mathcal{O}_{Y_{0}}$. Thus
$\mathcal{P}(Y)$ identifies with the set of algebra homomorphisms $\mathcal{A} \to \mathcal{O}_{Y}$ inducing the
canonical augmentation $\mathcal{A}_{0} \to \mathcal{O}_{Y_{0}}$. But the algebra homomorphisms
$\mathcal{A} \to \mathcal{O}_{Y}$ correspond bijectively to module homomorphisms $\mathcal{M} \to \mathcal{O}_{Y}$,
putting for simplicity $\mathcal{M} = g*(\Omega^{1}_{X/S})$, and we are interested in those inducing the **zero**
homomorphism $\mathcal{M}_{0} \to \mathcal{O}_{Y_{0}}$, where
$\mathcal{M}_{0} = \mathcal{M} \otimes_{\mathcal{O}_{Y}} \mathcal{O}_{Y_{0}}$; that is, those sending $\mathcal{M}$ into
the augmentation ideal $\mathcal{J}$. We therefore find the set

$$
\operatorname{Hom}_{\mathcal{O}_{Y}}(\mathcal{M},\mathcal{J}) = \operatorname{Hom}_{\mathcal{O}_{Y_{0}}}(\mathcal{M}_{0},\mathcal{J}),
$$

since $\mathcal{J}$ is annihilated by $\mathcal{J}$. This is the desired canonical bijection $III.5.1.*$.

Taking into account the implication (i) ⇒ (iii) in III.3.1, one obtains:

**Corollary.**

<!-- label: III.5.2 -->

<!-- original page 73 -->

If X is smooth over S, at least at the points of $g_{0}(Y_{0})$, then $\mathcal{P}$ is even a **principal homogeneous
sheaf** under the commutative sheaf of groups $\mathcal{G}$, which in this case may also be written

```text
𝒢 = g₀*(𝔤_{X/S}) ⊗_{𝒪_{Y₀}} 𝒥,
```

where $\mathfrak{g}_{X/S}$ is the sheaf on X dual to $\Omega^{1}_{X/S}$, i.e. the **tangent sheaf**, or **sheaf of
derivations**, of X relative to S. This last formula comes from the fact that $\Omega^{1}_{X/S}$ is then free of finite
type.

In particular, this principal homogeneous sheaf determines a cohomology class in $H^{1}(Y_{0},\mathcal{G})$, whose
vanishing is necessary and sufficient for the existence of an S-morphism g extending $g_{0}$. And if such an extension
exists, the set of all possible extensions is a homogeneous space under the group $H^{0}(Y_{0},\mathcal{G})$.

In applying the methods of formal geometry, the situation is most often the following. We are given two S-preschemes X
and Y, and a coherent ideal $\mathcal{I}$ on S. Let $S_{n}$ denote the closed sub-prescheme of S defined by
$\mathcal{I}^{n+1}$, and put

```text
X_n = X ×_S S_n,    Y_n = Y ×_S S_n.
```

Suppose we have an $S_{n}$-morphism

$$
g_{n}: Y_{n} \to X_{n}
$$

or, what amounts to the same thing, an S-morphism $Y_{n} \to X$, or again an $S_{n+1}$-morphism $Y_{n} \to X_{n+1}$,
since such a morphism necessarily induces $Y_{n} \to X_{n}$. We seek to extend it to an $S_{n+1}$-morphism

$$
g_{n+1}: Y_{n+1} \to X_{n+1}.
$$

If this can be continued indefinitely, one obtains a morphism $\hat{Y} \to \hat{X}$ for the formal preschemes obtained
by completing Y and X for the ideals $\mathcal{I}\mathcal{O}_{Y}$ and $\mathcal{I}\mathcal{O}_{X}$. We may apply III.5.1
with $(S,X,Y,Y_{0},g_{0})$ replaced by `(S_{n+1}`, $X_{n+1}$, $Y_{n+1}$, $Y_{n}$, `g_n)`. The sheaf $\mathcal{G}$ here
becomes the sheaf of module homomorphisms from $g_{n}*(\Omega^{1}_{X_{n+1}/S_{n+1}})$ into

$$
\mathcal{J} = \mathcal{I}^{n+1}\mathcal{O}_{Y} / \mathcal{I}^{n+2}\mathcal{O}_{Y}.
$$

Since $\mathcal{J}$ is annihilated by $\mathcal{I}\mathcal{O}_{Y}$, we may then replace
$g_{n}*(\Omega^{1}_{X_{n+1}/S_{n+1}})$ by the sheaf it induces on $Y_{0}$, namely $h_{0}*(\Omega^{1}_{X/S})$, where
$h_{0}$ is the composite $Y_{0} \to Y_{n} \to X_{n+1}$, or again the composite $Y_{0} \to X_{0} \to X_{n+1}$, where
$g_{0}: Y_{0} \to X_{0}$ is induced by $g_{n}$. Since the inverse image of $\Omega^{1}_{X_{n+1}/S_{n+1}}$ on
$X_{0} = X_{n+1} \times_{S_{n+1}} S_{0}$ is $\Omega^{1}_{X_{0}/S_{0}}$, one sees that one also has

```text
𝒢 = Hom_{𝒪_{Y₀}}(g₀*(Ω¹_{X₀/S₀}), 𝓘^{n+1}𝒪_Y / 𝓘^{n+2}𝒪_Y).
```

Thus we obtain:

**Corollary.**

<!-- label: III.5.3 -->

Let S, X, Y, $\mathcal{I}$, and $g_{n}$ be as above, and let $\mathcal{P}(g_{n})$ be the sheaf on Y whose sections on an
open U are the extensions $g_{n+1}$ of $g_{n}$ to an $S_{n+1}$-morphism $Y_{n+1} \to X_{n+1}$. Then $\mathcal{P}(g_{n})$
is a formally principal homogeneous sheaf under the sheaf of groups

$$
\mathcal{G} = \operatorname{Hom}_{\mathcal{O}_{Y_{0}}}(g_{0}*(\Omega^{1}_{X_{0}/S_{0}}), gr^{n+1}_{\mathcal{I}\mathcal{O}_{Y}}(\mathcal{O}_{Y})).
$$

In particular:

**Corollary.**

<!-- label: III.5.4 -->

If moreover X is smooth over S, at least at the points of $g_{0}(Y_{0})$, then $\mathcal{P}(g_{n})$ is even a principal
homogeneous sheaf. In particular, it defines an obstruction class in $H^{1}(Y_{0},\mathcal{G})$, whose vanishing is
necessary and sufficient for the existence of a global extension $g_{n+1}$ of $g_{n}$. And if such an extension exists,
the set of all global extensions is a principal homogeneous space under $H^{0}(Y_{0},\mathcal{G})$. Finally, in the case
considered, the sheaf $\mathcal{G}$ may also be written

```text
𝒢 = g₀*(𝔤_{X₀/S₀}) ⊗_{𝒪_{Y₀}} gr^{n+1}_{𝓘𝒪_Y}(𝒪_Y).
```

Proceeding step by step, one sees therefore that if all the $H^{1}(Y_{0},\mathcal{G}_{n})$ vanish, where

$$
\mathcal{G}_{n} = g_{0}*(\mathfrak{g}_{X_{0}/S_{0}}) \otimes gr^{n}_{\mathcal{I}\mathcal{O}_{Y}}(\mathcal{O}_{Y}),
$$

then, starting with an arbitrary $g_{k}$, one can extend it successively to $g_{k+1}$, and so on. In particular, if
$\mathcal{I}$ is nilpotent, one will be able to find an extension g of $g_{k}$ to Y. The vanishing condition for the H¹
is satisfied in particular if $Y_{0}$ is affine. Thus one obtains:

**Corollary.**

<!-- label: III.5.5 -->

<!-- original page 75 -->

In the statement of Theorem III.3.1, one obtains a necessary and sufficient condition equivalent to the others by
supposing that the $Y'$ occurring in (ii), or (ii bis), is affine, and by requiring the existence of a **global
extension** g of $g_{0}$ to all of $Y'$.

Note that the proof of III.3.1 could not have given this result directly.

An important case is that where Y is **flat** over S. Then one has

```text
gr^n(𝒪_Y) = gr^n(𝒪_S) ⊗_{𝒪_{S₀}} 𝒪_{Y₀},
```

and when, moreover, the $gr^{n}(\mathcal{O}_{S})$ are **locally free on** S, one finds

```text
𝒢_n = Hom_{𝒪_{Y₀}}(g₀*(Ω¹_{X₀/S₀}), 𝒪_{Y₀}) ⊗_{𝒪_{S₀}} gr^n(𝒪_S),
```

or again, if $\Omega^{1}_{X_{0}/S_{0}}$ is itself locally free, for example if X is smooth over S,

```text
𝒢_n = g₀*(𝔤_{X₀/S₀}) ⊗_{𝒪_{S₀}} gr^n(𝒪_S).
```

If, for example, S is affine with affine ring A, and $\mathcal{I}$ is defined by an ideal I of A, one finds

```text
H^i(Y₀,𝒢_n) = H^i(Y₀,𝒢₀) ⊗_A gr_I^n(A)
```

for every i; indeed, the question is local on $S_{0}$, and one is reduced to the case where one tensors by a free
module. **In this case, the vanishing of $H^{1}(Y_{0},\mathcal{G}_{0})$ implies that all obstructions to the successive
extensions of $g_{n}$ vanish.** Thus one obtains:

**Corollary.**

<!-- label: III.5.6 -->

Let $(S,X,Y,\mathcal{I},g_{n})$ be as above. Suppose moreover that X is smooth over S and Y is flat over S, and finally
that S is affine and the

$$
gr^{n}(\mathcal{O}_{S}) = \mathcal{I}^{n}/\mathcal{I}^{n+1}
$$

are locally free. Then the obstruction to constructing $g_{n+1}$ lies in

$$
H^{1}(Y_{0},\mathcal{G}_{0}) \otimes_{A} gr^{n+1}_{I}(A),
$$

where A is the ring of S and I the ideal of A defining $\mathcal{I}$, with

$$
\mathcal{G}_{0} = g_{0}*(\mathfrak{g}_{X_{0}/S_{0}}).
$$

If $H^{1}(Y_{0},\mathcal{G}_{0}) = 0$, then $g_{n}$ can be extended to an `Ŝ`-morphism ĝ: $\hat{Y} \to \hat{X}$.

Of course, this result would remain valid exactly as stated if, instead of starting with ordinary S-preschemes X and Y,
one started with formal $\hat{\mathcal{I}}$-adic `Ŝ`-preschemes $\mathfrak{X}$ and $\mathfrak{Y}$. It allows one to
prove, for example, that certain formal schemes proper over a complete local ring are in fact algebraic. Indeed,
proceeding as in Lemma III.4.2, one finds:

<!-- original page 76 -->

**Corollary.**

<!-- label: III.5.7 -->

Under the conditions of III.5.6, if $g_{0}$ is an isomorphism, then so is ĝ.

The same result holds for closed immersions.

Thus one obtains:

**Proposition.**

<!-- label: III.5.8 -->

Let A be a complete local ring with maximal ideal $\mathfrak{m}$ and residue field k. Let $\mathfrak{X}$ and
$\mathfrak{Y}$ be two $\mathfrak{m}$-adic formal preschemes over A, flat over A, meaning that for every n, $X_{n}$ and
$Y_{n}$ are flat over $A_{n} = A/\mathfrak{m}^{n+1}$. Suppose $X_{0} = \mathfrak{X} \otimes_{A} k$ is smooth over k and
$H^{1}(X_{0},\mathfrak{g}_{X_{0}/k}) = 0$. Then every k-isomorphism from $Y_{0}$ onto $X_{0}$ extends to an
A-isomorphism from $\mathfrak{Y}$ onto $\mathfrak{X}$; this extension is unique if moreover
$H^{0}(X_{0},\mathfrak{g}_{X_{0}/k}) = 0$.

This gives in particular a result on the **uniqueness** of a smooth formal prescheme over A reducing to a given
prescheme $X_{0}$, provided $H^{1}(X_{0},\mathfrak{g}_{X_{0}/k}) = 0$. Moreover, if $\mathfrak{X}$ and $\mathfrak{Y}$
come from ordinary proper schemes over A, say X and Y, then by the existence theorem for sheaves in formal geometry, cf.
the Bourbaki seminar exposé no. 182,[^iii-5-8-1] there is a bijective correspondence between the A-isomorphisms
$Y \to X$ and the A-isomorphisms of the formal completions. Hence:

**Corollary.**

<!-- label: III.5.9 -->

The preceding statement III.5.8 remains valid when $\mathfrak{X}$ and $\mathfrak{Y}$ are replaced by ordinary A-schemes
X and Y, **proper** over A.

Finally, when $\mathfrak{X}$ is a formal scheme proper over A, and $\mathfrak{Y}$ is of the form `Ŷ` where Y is an
ordinary proper scheme over A, Proposition III.5.8 gives sufficient conditions for finding an isomorphism of
$\mathfrak{X}$ with `Ŷ`, and hence for the formal scheme $\mathfrak{X}$ to be in fact “algebraic”, i.e. isomorphic to an
$\hat{X}$, with X an ordinary proper scheme over A, which will then be canonically determined. This happens notably if
$X_{0} = \mathbb{P}^{r}_{k}$, or more generally if $X_{0}$ is a Severi-Brauer scheme, i.e. becomes isomorphic to the
standard projective space over the algebraic closure of k: every formal scheme proper and flat over A, with fiber
$\mathbb{P}^{r}_{k}$, is algebraizable, and more precisely is isomorphic to the $\mathfrak{m}$-adic formal completion of
$\mathbb{P}^{r}_{A}$. In particular, thanks to the “existence theorem”, every ordinary proper scheme over A with fiber
$\mathbb{P}^{r}_{k}$ is isomorphic to $\mathbb{P}^{r}_{A}$, where A is a complete local ring. Using descent theory, one
can prove that if A is not complete, X becomes isomorphic to $\mathbb{P}^{r}$ after making a finite étale extension
$A \to A'$ of the base; in this form, the result remains valid for a fiber that is a Severi-Brauer scheme.

## 6. Global Infinitesimal Extension of Smooth S-Schemes

<!-- label: III.6 -->

Under the conditions of Theorem III.4.1, we propose to seek whether there exists a prescheme X smooth over Y such that
$X \times_{Y} Y_{0}$ is $Y_{0}$-isomorphic to $X_{0}$, knowing that such a scheme “exists locally on $X_{0}$”. Taking up
again the step-by-step construction method, we are led to replace Y by the letter S, to suppose given a closed
sub-prescheme $S_{0}$ of S defined by a sheaf of ideals $\mathcal{I}$, which it is no longer necessary to suppose
locally nilpotent, to introduce the closed sub-preschemes $S_{n}$ of S defined by the $\mathcal{I}^{n+1}$, and to
suppose given a sub-prescheme $X_{n}$ smooth over $S_{n}$. We propose to find an $S_{n+1}$-prescheme $X_{n+1}$ “reducing
to $X_{n}$”, i.e. equipped with an isomorphism

```text
X_n → X_{n+1} ×_{S_{n+1}} S_n
```

that is **smooth** over $S_{n+1}$, or equivalently by II.2.1, **flat** over $S_{n+1}$. As we noted in III.4, such data
amount to giving a sheaf of algebras $\mathcal{B}$ over $f^{-1}(\mathcal{O}_{S_{n+1}})$, where f is the continuous map
underlying the structural morphism $X_{n} \to S_{n}$, equipped with an augmentation
$\mathcal{B} \to \mathcal{O}_{X_{n}}$ compatible with the augmentation
$f^{-1}(\mathcal{O}_{S_{n+1}}) \to f^{-1}(\mathcal{O}_{S_{n}})$, and satisfying two conditions (a) and (b) that we shall
not rewrite, merely noting that they are **local in nature** on the topological space underlying $X_{n}$. By III.4.1, a
solution exists locally. It is moreover unique up to nonunique isomorphism, at least locally. Let us begin by making
this point precise.

<!-- original page 78 -->

**Proposition.**

<!-- label: III.6.1 -->

Let $X_{n+1}$ over $S_{n+1}$ reduce to $X_{n}$ over $S_{n}$. Then the sheaf, on the topological space underlying
$X_{n}$, or equivalently $X_{0}$, of $S_{n+1}$-automorphisms of $X_{n+1}$ inducing the identity on $X_{n}$ is
canonically isomorphic to

```text
𝒢 = 𝔤_{X₀/S₀} ⊗_{𝒪_{S₀}} gr^{n+1}_𝓘(𝒪_S)
```

as a sheaf of groups.

Indeed, by III.5.4 and III.4.2 this sheaf is a principal homogeneous sheaf under $\mathcal{G}$. Since it has a
distinguished section, the identity automorphism of $X_{n+1}$, it identifies as a sheaf of sets with $\mathcal{G}$. One
must verify that this identification is compatible with the group structures. This is easy, and is moreover a special
case of a more general result on the compatibility of the principal-bundle structures in III.5.1 and III.5.3 with
composition of morphisms, a result that we do not state here but that ought to appear in the hyperplodocus.

In particular, the sheaf on $X_{0}$ of germs of automorphisms of $X_{n+1}$, with the structures just made explicit, is
**commutative**. It follows that if $X'_{n+1}$ is another solution of the problem, isomorphic to $X_{n+1}$ over the open
U of $X_{0}$, then the isomorphism from $\operatorname{Aut}(X_{n+1})|U$ to $\operatorname{Aut}(X'_{n+1})|U$ deduced by
transport of structure from an isomorphism $X_{n+1}|U \to X'_{n+1}|U$ **does not depend** on the choice of the latter.
It is in fact nothing but the identity isomorphism of $\mathcal{G}$, when both automorphism sheaves are identified with
$\mathcal{G}$ by III.6.1.

From III.6.1 one deduces:

**Corollary.**

<!-- label: III.6.2 -->

Let $X_{n+1}$ and $X'_{n+1}$ be smooth over $S_{n+1}$ and “reduce to $X_{n}$”. Then the sheaf, on the space underlying
$X_{0}$, of $S_{n+1}$-isomorphisms from $X_{n+1}$ to $X'_{n+1}$ inducing the identity on $X_{n}$ is naturally a
principal homogeneous sheaf under $\mathcal{G}$.

This expresses indeed that $X_{n+1}$ and $X'_{n+1}$ are locally isomorphic, and that the sheaf of germs of automorphisms
of the first is $\mathcal{G}$.

Now note that by III.4.1 one can always find a covering $(U_{i})$ of $X_{n}$ by opens, which may be supposed affine, and
for each i a smooth scheme $X^{i}$ over $S_{n+1}$ reducing to $U_{i}$. Suppose for simplicity that $X_{n}$ is
**separated**, so the $U_{ij} = U_{i} \cap U_{j}$ are still **affine** opens of $X_{n}$. Since H¹ of such an open with
values in the quasi-coherent sheaf $\mathcal{G}$ is zero, Corollary III.6.2 implies that $X^{i}|U_{ij}$ is isomorphic to
$X^{j}|U_{ij}$; let

$$
f_{ji}: X^{i}|U_{ij} \to X^{j}|U_{ij}
$$

be such an isomorphism. It is determined up to a section of $\mathcal{G}$ on $U_{ij}$. For every triple of indices put

```text
f_{ji}^{(k)} = f_{ji}|U_{ijk},    where U_{ijk} = U_i ∩ U_j ∩ U_k.
```

If one had

$$
f^{(i)}_{kj} f^{(k)}_{ji} = f^{(j)}_{ki},
$$

<!-- label: eq:III.6.1 -->

it would follow that the $X^{i}$ glue by the $f_{ji}$, and hence define a solution $X = X_{n+1}$ of the desired problem.
Such a solution exists more generally if one can modify the $f_{ji}$ into $f'_{ji}:$

```text
f′_{ji} = f_{ji} g_{ji},    g_{ji} ∈ Γ(U_{ij},𝒢),
```

<!-- label: eq:III.6.2 -->

so that the $f'_{ji}$ satisfy the preceding transitivity condition. This sufficient condition for the existence of a
solution is also necessary, as one sees by recalling that such a solution X must, on each $U_{i}$, be isomorphic to
$X^{i}$; this allows one to choose isomorphisms

$$
f_{i}: X|U_{i} \to X^{i}
$$

and to define

```text
f′_{ji} = (f_j|U_{ij})(f_i|U_{ij})^{-1}: X^i|U_{ij} → X^j|U_{ij},
```

satisfying the gluing condition.

Now put

```text
f_{ijk} = (f_{ki}^{(j)})^{-1} f_{kj}^{(i)} f_{ji}^{(k)}.
```

<!-- label: eq:III.6.3 -->

This is an automorphism of $X^{i}|U_{ijk}$, which we identify with a section of $\mathcal{G}$ by III.6.1. One checks, by
a small formal calculation left to the reader, that it is a **2-cocycle** f of the open covering
$\mathcal{U} = (U_{i})$, with coefficients in $\mathcal{G}$. The same calculation shows that, under III.6.2, the gluing
condition III.6.1 **for the** $f'_{ij}$ is equivalent to the formula

```text
f = dg,
```

<!-- label: eq:III.6.4 -->

where $g = (g_{ij})$ is regarded as a 1-cochain of $\mathcal{U}$ with coefficients in $\mathcal{G}$. Thus **the
necessary and sufficient condition for the existence of a solution of the problem is that the cohomology class in
$H^{2}(\mathcal{U},\mathcal{G})$ defined by the cocycle III.6.3 be zero**. Moreover, since $\mathcal{U} = (U_{i})$ is an
affine covering of $X_{0}$, which is a **scheme**, $H^{2}(\mathcal{U},\mathcal{G})$ identifies with
$H^{2}(X_{0},\mathcal{G})$. It is immediate that the cohomology class thus obtained in $H^{2}(X_{0},\mathcal{G})$ does
not depend on the affine covering considered. We shall call it the **obstruction class to extending $X_{n}$ to a scheme
$X_{n+1}$ smooth over $S_{n+1}$**.

Suppose this obstruction is zero. Then the argument sketched above shows that every solution $X = X_{n+1}$ is isomorphic
to a solution obtained by gluing from isomorphisms $f'_{ji}$, which may be supposed of the form III.6.2, the gluing
condition being just III.6.3. The set of admissible g is therefore a principal homogeneous space under the group
$Z^{1}(\mathcal{U},\mathcal{G})$ of 1-cocycles of $\mathcal{U}$ with coefficients in $\mathcal{G}$. Moreover, one sees
at once that **two cochains g and $g'$**, with dg = $dg' = f$, **define isomorphic solutions if and only if the cocycle
$g - g'$ is of the form dh**, with $h = (h_{i}) \in C^{0}(\mathcal{U},\mathcal{G})$. Thus one obtains:

**Theorem.**

<!-- label: III.6.3 -->

Let $(S,\mathcal{I},X_{n})$ be as above, with $X_{n}$ assumed separated.[^iii-6-3-1] Then one can define canonically an
obstruction class in $H^{2}(X_{0},\mathcal{G})$, where $\mathcal{G}$ is defined in III.6.1, whose vanishing is necessary
and sufficient for the existence of a scheme $X_{n+1}$, smooth over $S_{n+1}$, reducing to $X_{n}$. If this obstruction
is zero, then the set of isomorphism classes, with isomorphisms inducing the identity on $X_{n}$, of
$S_{n+1}$-preschemes $X_{n+1}$ reducing to $X_{n}$ is naturally a principal homogeneous space under
$H^{1}(X_{0},\mathcal{G})$.

**Remarks.**

<!-- label: III.6.4 -->

Starting from III.6.1, the arguments made here are purely formal, and are advantageously transcribed in the setting of
local categories, or even of general fibered categories. The obstruction class to the existence of a “global” object of
a category, where one can find an object “locally”, any two objects are always “locally isomorphic”, and the
automorphism group of any object is commutative, obtained in this general context, contains as a special case the
“second boundary homomorphism” in an exact sequence of sheaves of not necessarily commutative groups, studied for
example by Grothendieck in Kansas or Tôhoku. The silly cocycle calculation made here should therefore be regarded as a
makeshift, due to the absence of a satisfactory reference text.

### 6.5

<!-- label: III.6.5 -->

Note that in III.6.3 there is in general no distinguished element in the principal homogeneous space under
$H^{1}(X_{0},\mathcal{G})$ under consideration. This is reflected in particular by the fact that, after localizing on S,
one obtains a principal homogeneous sheaf on $S_{0}$ with structural group $R^{1}f_{*}(\mathcal{G})$, which is not
necessarily trivial, i.e. which defines a cohomology class in $H^{1}(S_{0},R^{1}f_{*}(\mathcal{G}))$ that is not
necessarily zero. This is when one supposes that the class d ∈ $H^{2}(X_{0},\mathcal{G})$ is not zero, but is zero
“locally over S”, i.e. defines a zero section of $R^{2}f_{*}(\mathcal{G})$, equivalently a zero element in
$H^{0}(S_{0},R^{2}f_{*}(\mathcal{G}))$.

### 6.6

<!-- label: III.6.6 -->

For the moment we know almost nothing about the general algebraic mechanism of the cohomology classes introduced in this
number and their relations with the preceding number, and we have nothing precise to say about them in the simplest
particular cases, such as the case of abelian schemes over artinian rings.[^iii-6-6-1] One hopes that people will be
found to work the question out thoroughly; it seems particularly interesting. It is intimately linked, in particular, to
the “module theory” of algebraic structures.

**Corollary.**

<!-- label: III.6.7 -->

Suppose $H^{2}(X_{0},\mathcal{G}) = 0$. Then an $X_{n+1}$ exists, and it is unique up to isomorphism if moreover
$H^{1}(X_{0},\mathcal{G}) = 0$.

In particular, proceeding step by step, and observing that an affine scheme is acyclic for a quasi-coherent sheaf, one
concludes:

**Corollary.**

<!-- label: III.6.8 -->

<!-- original page 82 -->

Under the conditions of Theorem III.4.1, if $X_{0}$ is affine, then there exists an X smooth over Y reducing to $X_{0}$,
and this X is unique up to nonunique isomorphism.

Note that the direct proof of Theorem III.4.1 could not have given this result.

**Corollary.**

<!-- label: III.6.9 -->

Under the conditions of III.6.3, suppose S is affine with ring A, $\mathcal{I}$ is defined by an ideal I of A, and
finally the

$$
gr^{n}_{\mathcal{I}}(\mathcal{O}_{S}) = \mathcal{I}^{n}/\mathcal{I}^{n+1}
$$

are locally free. Then $H^{i}(X_{0},\mathcal{G})$ identifies with

$$
H^{i}(X_{0},\mathcal{G}_{0}) \otimes_{A} gr^{n+1}_{I}(A),
$$

where

$$
\mathcal{G}_{0} = \mathfrak{g}_{X_{0}/S_{0}}.
$$

Thus the obstruction class to extending $X_{n}$ lies in $H^{2}(X_{0},\mathcal{G}_{0}) \otimes_{A} gr^{n+1}_{I}(A)$, and,
if it is zero, the set of isomorphism classes of solutions is a principal homogeneous space under
$H^{1}(X_{0},\mathcal{G}_{0}) \otimes_{A} gr^{n+1}_{I}(A)$.

In particular:

**Corollary.**

<!-- label: III.6.10 -->

Under the conditions of III.6.9, suppose

$$
H^{2}(X_{0},\mathfrak{g}_{X_{0}/S_{0}}) = 0.
$$

Then there exists an $\hat{\mathcal{I}}$-adic formal scheme $\mathfrak{X}$ over the $\mathcal{I}$-adic formal completion
`Ŝ` of S, “smooth over S”, i.e. such that the $\mathfrak{X}_{p}$ are smooth over the $S_{p}$, and reducing to $X_{n}$,
i.e. equipped with an isomorphism

```text
X_n → 𝔛 ×_S S_n.
```

If moreover $H^{1}(X_{0},\mathfrak{g}_{X_{0}/S_{0}}) = 0$, then such a $\mathfrak{X}$ is unique up to isomorphism.

Indeed, one constructs $X_{n+1}$, $X_{n+2}$, and so on step by step, whence $\mathfrak{X}$ by passing to the inductive
limit of the $X_{i}$. The uniqueness assertion already appears in the preceding number.

## 7. Application to the Construction of Formal Schemes and Ordinary Smooth Schemes over a Complete Local Ring A

<!-- label: III.7 -->

The results of the preceding number sometimes make it possible to prove the existence of an $\mathfrak{m}$-adic formal
scheme over such a ring, reducing to a given smooth scheme $X_{0}$ over k. Distinguish two cases.

1. **A is “of equal characteristics”.** This is the case in particular if k has characteristic 0. Then one knows that
   there exists a **coefficient subfield of** A, i.e. a subfield $k'$ such that $A \to k$ induces an isomorphism
   $k' \to k$. **Then there even exists an ordinary smooth scheme over A reducing to $X_{0}$**, namely
   $X = X_{0} \otimes_{k} A$, with A regarded as an algebra over k by the homomorphism $k \to k' \to A$ defined by $k'$.
   It should be noted, however, that this construction is not “natural”. It is easy to convince oneself, already in the
   case where A = k[t]/(t²), the algebra of dual numbers, that another lifting homomorphism $k \to A$, in this case
   defined by an absolute derivation of k into itself, defines an $X'$ over A that in general **is not isomorphic to
   X**, if $H^{1}(X_{0},\mathfrak{g}_{X_{0}/k}) \neq 0$. It would moreover be interesting to study, for k of
   characteristic 0, or imperfect of characteristic p > 0, which X smooth over A are obtained in this way, and under
   what condition two homomorphisms $k \to A$ define isomorphic A-schemes. Nevertheless, the existence of $k'$ is enough
   to imply that the first obstruction to lifting $X_{0}$, which lies in
   $H^{2}(X_{0},\mathfrak{g}_{X_{0}/k}) \otimes_{k} \mathfrak{m}/\mathfrak{m}^{2}$, is necessarily zero. Of course, once
   $X_{0}$ has then been lifted to $X_{1}$ smooth over $A/\mathfrak{m}^{2}$, the new obstruction to constructing $X_{2}$
   will in general not be zero: it will depend on a variable element in a certain principal homogeneous space under
   $H^{1}(X_{0},\mathcal{G}_{0}) \otimes \mathfrak{m}/\mathfrak{m}^{2}$ and lies in
   $H^{2}(X_{0},\mathcal{G}_{0}) \otimes \mathfrak{m}^{2}/\mathfrak{m}^{3}$. The situation ought to be studied in
   detail.[^iii-7-a-1]

2) **A is of unequal characteristics.** In this case we know nothing, except if by luck
   $H^{2}(X_{0},\mathfrak{g}_{X_{0}/k}) = 0$, in which case one can construct an $\mathfrak{m}$-adic formal smooth
   scheme over A reducing to k. Even if $A = \mathbb{Z}/p^{2}\mathbb{Z}$ and $X_{0}$ is an “abelian” scheme of dimension
   2, one does not know whether it can be lifted to an $X = X_{1}$ smooth over A;[^iii-7-b-1] on the other hand, we have
   no example of an $X_{0}$ that has been proved not to come from an ordinary scheme X smooth over A. I have the
   impression that such examples should exist, with $X_{0}$ a projective surface.[^iii-7-b-2] Let us simply point out
   that by Cohen's theorem, there exists a Cohen p-ring B with residue field k and a homomorphism $B \to A$ inducing the
   identity isomorphism on residue fields. Consequently, the “strongest” lifting result would be obtained by taking A to
   be a Cohen p-ring: if there is an ordinary or formal solution over such a ring, there is one over every complete
   local ring with residue field k. In particular, since for a Cohen p-ring $\mathfrak{m}/\mathfrak{m}^{2}$ identifies
   canonically with k, one sees that **for every smooth scheme $X_{0}$ over a field k of characteristic p > 0, there
   exists a cohomology class in $H^{2}(X_{0},\mathfrak{g}_{X_{0}/k})$**, the first obstruction to lifting $X_{0}$ to a
   smooth scheme over a Cohen p-ring. We do not know whether it can be nonzero.[^iii-7-b-3]

Even if one succeeds step by step in constructing the $X_{n}$ reducing to $X_{0}$, this generally gives only a
**formal** scheme $\mathfrak{X}$ smooth over A, reducing to $X_{0}$. When $X_{0}$ is proper over A, there remains the
question whether $\mathfrak{X}$ is in fact algebraizable, in order to obtain an **ordinary** proper scheme over A,
smooth over A, reducing to $X_{0}$. The only known criterion, noted in the Bourbaki seminar and appearing in the
Éléments, Chapter III, 4.7.1, is the following: if $\mathfrak{X}$ is proper over A, and if $\mathcal{L}$ is an
invertible sheaf on $\mathfrak{X}$ such that the induced sheaf $\mathcal{L}_{0}$ on $X_{0}$ is ample, i.e. some tensor
power $\mathcal{L}^{\otimes n}_{0}$, n > 0, comes from a projective immersion of $X_{0}$, then there exists a scheme X
projective over A, and an ample invertible sheaf on X, such that $(\mathfrak{X},\mathcal{L})$ is obtained from it by
$\mathfrak{m}$-adic completion. This leads us, given a locally free sheaf $\mathcal{E}_{0}$ on $X_{0}$, which we shall
choose invertible and ample for our purpose, to extend it to a locally free sheaf $\mathcal{E}$ on $\mathfrak{X}$. For
this, one is reduced to constructing step by step locally free sheaves $\mathcal{E}_{n}$ on the $X_{n}$. The discussion
is entirely analogous to that of III.6, cf. Remark III.6.4; the essential role is played by the **sheaf of
automorphisms** of an $\mathcal{E}_{n+1}$ inducing the identity on $\mathcal{E}_{n}$. One shows at once that this sheaf
identifies with

```text
𝒢 = Hom_{𝒪_{X₀}}(𝓔₀, 𝓔₀ ⊗ gr^{n+1}_𝓘(𝒪_X))
  = Hom_{𝒪_{X₀}}(𝓔₀,𝓔₀) ⊗ gr^{n+1}_𝓘(𝒪_X),
```

which is again a sheaf of commutative groups. One obtains:

<!-- original page 85 -->

**Proposition.**

<!-- label: III.7.1 -->

Let S be a prescheme equipped with a quasi-coherent sheaf of ideals $\mathcal{I}$, let X be a prescheme over S, let
$S_{n}$ be the sub-prescheme of S defined by $\mathcal{I}^{n+1}$, and let $X_{n} = X \times_{S} S_{n}$ for every integer
n. Let $\mathcal{E}_{n}$ be a locally free sheaf on $X_{n}$, and seek to extend it to a locally free sheaf
$\mathcal{E}_{n+1}$ on $X_{n+1}$. Then $\mathcal{E}_{n}$ defines a canonical obstruction class in
$H^{2}(X_{0},\mathcal{G})$, where $\mathcal{G}$ is the quasi-coherent sheaf given by the formula above. The vanishing of
this class is necessary and sufficient for the existence of an $\mathcal{E}_{n+1}$ extending $\mathcal{E}_{n}$. If this
class is zero, then the set of isomorphism classes, with isomorphisms inducing the identity on $\mathcal{E}_{n}$, of
solutions $\mathcal{E}_{n+1}$ is a principal homogeneous space under $H^{1}(X_{0},\mathcal{G})$.

This proposition gives rise to the usual corollaries. Let us only point out that if X is **flat** over S, then one may
write

```text
𝒢 = Hom_{𝒪_{X₀}}(𝓔₀,𝓔₀) ⊗_{𝒪_{S₀}} gr^{n+1}_𝓘(𝒪_S),
```

whence, if S is affine with ring A and the $\mathcal{I}^{n}/\mathcal{I}^{n+1}$ are locally free, the sufficient
condition

```text
H²(X₀,𝒢₀) = 0,    with    𝒢₀ = Hom_{𝒪_{X₀}}(𝓔₀,𝓔₀),
```

for the existence of an $\mathcal{E}_{n+1}$, and hence, step by step, for the existence of successive extensions
$\mathcal{E}_{m}$, $m = n$, $n + 1$, etc.

Returning to the initial situation, we therefore find:

**Proposition.**

<!-- label: III.7.2 -->

Let A be a complete local ring, and let $\mathfrak{X}$ be a formal scheme proper and flat over A, such that $X_{0}$ is
projective and $H^{2}(X_{0},\mathcal{O}_{X_{0}}) = 0$. Then there exists a scheme X projective over A whose
$\mathfrak{m}$-adic formal completion is isomorphic to $\mathfrak{X}$.

Combining this with III.6.10, one finds:

**Theorem.**

<!-- label: III.7.3 -->

Let A be a complete local ring with residue field k, and let $X_{0}$ be a projective smooth scheme over k such that

$$
H^{2}(X_{0},\mathfrak{g}_{X_{0}/k}) = H^{2}(X_{0},\mathcal{O}_{X_{0}}) = 0.
$$

Then there exists a smooth and projective scheme X over A reducing to $X_{0}$.

More generally, if one is given an $X_{n}$ smooth over $A_{n} = A/\mathfrak{m}^{n+1}$ reducing to $X_{0}$, then there
exists an X smooth and proper over A and an isomorphism $X \otimes_{A} A_{n} = X_{n}$.

**Corollary.**

<!-- label: III.7.4 -->

Every smooth proper curve over k is obtained by reduction from a smooth proper curve over A.

This result will be the essential tool, together with the existence theorem for sheaves in formal geometry, for studying
the fundamental group of $X_{0}$ by transcendental means.

<!-- original page 86 -->

<!-- end of Exposé III source block: next chapter begins at smf_doc-math_3_01.tex line 6269 -->

[^iii-1-1-1]: For a more general and more conceptual definition, motivated by III.2.1 below, cf. EGA 0_IV 19.3.1.

[^iii-1-2-1]: Or better, “essentially unramified”, respectively “essentially étale”; compare EGA IV 18.6.1.

[^iii-2-1-1]: Cf. EGA 0_IV 19.3, 19.8.

[^iii-5-0-1]: It seems preferable to adopt the shorter and more expressive term “torsor under $\mathcal{G}$”, introduced
    in J. Giraud's thesis.

[^iii-5-8-1]: Cf. EGA III 5.4.1 for the proof.

[^iii-6-3-1]: This condition is in fact unnecessary, and one can avoid the cocycle calculations above. Cf. J. Giraud,
    _Cohomologie Non Abélienne_, forthcoming from Springer Verlag, 1971. Compare Remarks III.6.4.

[^iii-6-6-1]: It is now known that this obstruction is always zero in this case \[added in 2003 by MR: cf. F. Oort,
    “Finite group schemes, local moduli for abelian varieties and lifting problems”, *Algebraic Geometry Oslo
    1970*, Wolters-Noordhoff, 1972, pp. 223-254\].

[^iii-7-a-1]: It is probably described by the Kodaira-Spencer bracket operation; cf. Séminaire Cartan, 1960/61, Exposé
    4\.

[^iii-7-b-1]: This is now proved; cf. note III.6.6, page 81 in the original numbering.

[^iii-7-b-2]: Such an example was later constructed by J.-P. Serre, _Proc. Nat. Acad. Sci. USA_ **47** (1961), no. 1,
    pp. 108-109, at least in certain dimensions. D. Mumford gave an unpublished example with an algebraic **surface**.

[^iii-7-b-3]: It can be nonzero, as indicated in note iii-7-b-2.


<!-- SOURCE: 04-morphismes-plats.md -->

# Exposé IV. Flat Morphisms

<!-- label: IV -->

<!-- original page 87 -->

Here we give above all the flatness properties that were used in the preceding exposés. A more detailed study will be
found in Chapter IV of the Éléments de Géométrie Algébrique in preparation,[^iv-0-1] where the following situation is
studied systematically: $X$ locally of finite type over locally noetherian $Y$, and $\mathcal{F}$ coherent on $X$ and
$Y$-flat; one seeks relations among the properties of $Y$, those of $\mathcal{F}$, and those of the coherent sheaves
induced by $\mathcal{F}$ on the fibers of $X \to Y$, especially from the viewpoints of dimension, cohomological
dimension, depth, etc. There is in particular a systematic way of obtaining theorems of **Seidenberg** or **Bertini**
type, for hyperplane sections. The essential result for applying flatness methods in this context is the following,
proved below: if $Y$ is integral, $X$ of finite type over $Y$, and $\mathcal{F}$ coherent on $X$, then there exists a
nonempty open $U$ of $Y$ such that $\mathcal{F}$ is $Y$-flat at the points of $X$ lying over $U$. A second, no doubt
still more important, way in which flatness enters algebraic geometry is **descent theory**: see, for example,
Grothendieck's two exposés on the subject in the Bourbaki seminar,[^iv-0-2] and Exposés VIII and IX below. Flatness thus
seems to be one of the central technical notions in algebraic geometry.

Recall that the notion of flatness and faithful flatness was introduced by Serre in GAGA. An exposition of the following
numbers IV.1 and IV.2 is also found in Bourbaki's _Algèbre Commutative_, which of course, as the title of the book
indicates, is not restricted to commutative base rings.[^iv-0-3]

Contrary to the preceding exposés, we do not suppose that the rings under consideration are necessarily noetherian.

## 1. Sorites on Flat Modules

<!-- label: IV.1 -->

A module $M$ over a ring $A$ is said to be **flat**, or $A$-flat if one wants to specify $A$, if the functor

```text
T_M: N ↦ M ⊗_A N
```

which is in any case right exact, is **exact**, i.e. transforms monomorphisms into monomorphisms. Equivalently, the
first right-derived functor, or all the right-derived functors, vanish; that is, one has

```text
Tor^A_1(M,N) = 0     for all N,
```

respectively

```text
Tor^A_i(M,N) = 0     for i > 0 and all N.
```

Since the $Tor_{i}$ commute with inductive limits, it is enough to verify these conditions for $N$ of finite type;
indeed, taking then a composition series of $N$ with monogenic quotients, it is enough to have

$$
Tor^{A}_{1}(M,N) = 0
$$

for $N$ monogenic, i.e. of the form $A/I$, where $I$ is an ideal of $A$. Note moreover that

```text
Tor^A_1(M,A/I) = 0  ⇔  I ⊗_A M → M = A ⊗_A M is injective,
```

as one sees from the exact sequence of Tor, taking into account that $Tor^{A}_{1}(M,A) = 0$. Thus $M$ flat is equivalent
to saying that for every ideal $I$, the natural homomorphism

```text
I ⊗_A M → IM
```

is an isomorphism. It is enough to verify this for $I$ of finite type; a fortiori it is enough to verify that the
functor $M \otimes -$ is exact on **modules of finite type**.

As always when one has an exact functor $T$, if for a subobject $N'$ of $N$ one identifies $T(N')$ with a subobject of
$T(N)$, then for two subobjects $N'$, $N''$ of $N$ one has

```text
T(N′ ∩ N″) = T(N′) ∩ T(N″),
T(N′ + N″) = T(N′) + T(N″).
```

A direct sum of flat modules, and a direct factor of a flat module, is flat. In particular, since $A$ is flat, a
**free** module, hence also a **projective** module, is flat. The tensor product of two flat modules is flat; and if $M$
is flat over $A$, then $M \otimes_{A} B$ is flat over $B$ for every base change $A \to B$, by associativity of the
tensor product and the fact that a composite of exact functors is exact. If $M$ is flat over $B$, and $B$ flat over $A$,
then $M$ is flat over $A$, for the same reason.

The exact sequence of Tor, plus the “commutativity” of Tor, gives:

**Proposition.**

<!-- label: IV.1.1 -->

Let

$$
0 \to M' \to M \to M'' \to 0
$$

be an exact sequence of $A$-modules, with $M''$ flat. Then:

1. This sequence remains exact after tensoring by any $A$-module $N$.
1. $M$ is flat if and only if $M'$ is flat.

Thus one may say that, from the point of view of behavior under tensor products, flat modules are “as good” as free or
projective modules; in particular, the exact sequence of IV.1.1 is “as good” as if it split.

Let $S$ be a multiplicatively stable subset of $A$. Then $S^{-1}A$ is flat over $A$, because
$S^{-1}A \otimes N = S^{-1}N$ is an exact functor in $N$. If $M$ is $A$-flat, then $S^{-1}M = S^{-1}A \otimes M$ is
$S^{-1}A$-flat; the converse is true if $M \to S^{-1}M$ is an isomorphism, i.e. if the $s \in S$ are bijective on $M$,
by transitivity of flatness, since $S^{-1}A$ is flat over $A$. More generally, the case of a morphism of preschemes
$X \to Y$ and a quasi-coherent sheaf $\mathcal{F}$ on $X$ whose flatness relative to $Y$ one wants to study leads to the
situation with two rings.

**Proposition.**

<!-- label: IV.1.2 -->

Let $A \to B$ be a homomorphism of rings, let $M$ be a $B$-module, and let $T$ be a multiplicatively stable subset of
$B$.

1. If $M$ is $A$-flat, then $T^{-1}M$ is $A$-flat, hence also $S^{-1}A$-flat for every multiplicatively stable subset
   $S$ of $A$ mapping into $T$.
1. Conversely, if $M_{\mathfrak{n}}$ is flat over $A_{\mathfrak{n}}$ for every maximal ideal $\mathfrak{n}$ of $B$,
   equivalently over $A_{\mathfrak{m}}$ where $\mathfrak{m}$ is the prime ideal of $A$ inverse image of $\mathfrak{n}$,
   then $M$ is $A$-flat.

Indeed, there is the formula, functorial in the $A$-module $N$:

```text
T⁻¹M ⊗_A N = T⁻¹(M ⊗_A N),
```

for the two sides are functorially isomorphic to $T^{-1}B \otimes_{B} M \otimes_{B} N_{(B)}$, with
$N_{(B)} = N \otimes_{A} B$, by the associativity formulas for $\otimes$. It follows at once that if $M \otimes_{A} N$
is exact in $N$, then the same is true of $T^{-1}M \otimes_{A} N$, as a composite of two exact functors; this gives (i).
And (ii) follows in the same way, since to verify exactness of a sequence of $B$-modules it is enough to verify
exactness of the localizations at all maximal ideals of $B$.

**Proposition.**

<!-- label: IV.1.3 -->

1. Let $M$ be a flat $A$-module. If $x \in A$ is not a zero-divisor in $A$, then it is not a zero-divisor in $M$. In
   particular, if $A$ is integral, $M$ is torsion-free.
1. Suppose $A$ is integral and that for every maximal ideal $\mathfrak{m}$ of $A$, $A_{\mathfrak{m}}$ is principal, for
   example $A$ is a Dedekind ring, or even a principal ideal domain. In order that the $A$-module $M$ be flat, it is
   necessary and sufficient that it be torsion-free.

For (i), note that homothety by $x$ on $M$ is obtained by tensoring homothety by $x$ on $A$ with $M$. For (ii), by
IV.1.2 (ii) one may already suppose $A$ principal. One must show that if $M$ is torsion-free, then for every ideal $I$
of $A$, the injection $I \to A$, tensored by $M$, is an injection. This means that the generator $x$ of $I$ is not a
zero-divisor in $M$, as required.

## 2. Faithfully Flat Modules

<!-- label: IV.2 -->

A functor $F$ from one category to another is said to be **faithful** if, for all $X$ and $Y$, the map
$\operatorname{Hom}(X,Y) \to \operatorname{Hom}(F(X),F(Y))$ is injective. If $F$ is an additive functor between additive
categories, this is equivalent to saying that $F(u) = 0$ implies $u = 0$, and this implies that $F(X) = 0$ implies
$X = 0$. For $F$ to be **faithful and exact**, it is necessary and sufficient that the following condition hold: for
every sequence $M' \to M \to M''$ of morphisms in $\mathcal{C}$, the transformed sequence $F(M') \to F(M) \to F(M'')$ is
exact **if and only if** the original one is exact. Or again: $F$ is exact, and $F(X) = 0$ implies $X = 0$. To speak of
exactness, of course, the categories involved must be **abelian**.

Suppose one has a family $(M_{i})$ of nonzero objects of $\mathcal{C}$ such that every nonzero object of $\mathcal{C}$
has a subobject admitting a quotient isomorphic to some $M_{i}$. Then $F$ is faithful and exact if and only if $F$ is
exact and $F(M_{i}) \neq 0$ for all $i$. If $\mathcal{C}$ is the category of modules over a ring $A$, one may take for
$(M_{i})$, for example, the family of $A/\mathfrak{m}$, with $\mathfrak{m}$ running through the maximal ideals of $A$.
Indeed, every nonzero module admits a nonzero monogenic submodule, hence one isomorphic to $A/I$, with $I$ an ideal
$\neq A$, which by Krull admits a quotient $A/\mathfrak{m}$. From these sorites one deduces in particular:

**Proposition.**

<!-- label: IV.2.1 -->

Let $M$ be an $A$-module. The following conditions are equivalent:

1. The functor $M \otimes_{A} -$ is faithful and exact.
1. $M$ is flat, and $M \otimes_{A} N = 0$ implies $N = 0$.
1. $M$ is flat, and $M \otimes A/\mathfrak{m} \neq 0$ for every maximal ideal $\mathfrak{m}$ of $A$.
1. For every sequence of homomorphisms $N' \to N \to N''$, the sequence tensored by $M$ is exact if and only if the
   initial sequence is exact.

One then says that $M$ is a **faithfully flat** $A$-module. In particular, if $M$ is faithfully flat, then $N \to N'$ is
a monomorphism, epimorphism, or isomorphism if and only if the homomorphism obtained by tensoring by $M$ is one. A
faithfully flat module is **faithful**, since homothety by $f$ on $M$ is obtained by tensoring homothety by $f$ on $A$
with $M$.

As in IV.1, one sees the usual transitivity properties: the tensor product of two faithfully flat modules is faithfully
flat; if $M$ is faithfully flat over $A$, then $M \otimes_{A} B$ is faithfully flat over $B$ for every extension of the
base $A \to B$; if $B$ is an $A$-algebra faithfully flat over $A$ and $M$ is a faithfully flat $B$-module, then $M$ is a
faithfully flat $A$-module.

**Corollary.**

<!-- label: IV.2.2 -->

Let $A \to B$ be a local homomorphism of local rings, and let $M$ be a $B$-module of finite type. In order that $M$ be
faithfully flat over $A$, it is necessary and sufficient that it be flat over $A$ and nonzero.

This follows from criterion (i ter) and Nakayama. In particular, **for $B$ to be $A$-flat, it is necessary and
sufficient that it be faithfully $A$-flat**.

**Proposition.**

<!-- label: IV.2.3 -->

Let $A \to B$ be a homomorphism of rings, and let $M$ be a $B$-module faithfully flat over $A$. For every prime ideal
$\mathfrak{p}$ of $A$, there exists a prime ideal $\mathfrak{q}$ of $B$ inducing it.

Dividing by $\mathfrak{p}$, we are reduced to the case $\mathfrak{p} = 0$. Localizing at the prime ideal `0`, we are
reduced to the case where $A$ is a field. But $M$, being faithfully flat over $A$, is nonzero; a fortiori $B \neq 0$,
hence $B$ has a prime ideal, which can only induce the unique prime ideal of $A$. Geometrically, one may say that the
existence of a quasi-coherent sheaf $\mathcal{F}$ on $X = \operatorname{Spec}(B)$ that is “faithfully flat” relative to
$A$ implies that $X \to Y = \operatorname{Spec}(A)$ is **surjective**.

**Corollary.**

<!-- label: IV.2.4 -->

Suppose $M$ is flat over $A$, of finite type over $B$, and $Supp M = \operatorname{Spec}(B)$, i.e.
$M_{\mathfrak{q}} \neq 0$ for every prime ideal $\mathfrak{q}$ of $B$. Then the prime ideals $\mathfrak{q}$ of $B$
containing $\mathfrak{p}B$ and minimal among such ideals induce $\mathfrak{p}$.

<!-- original page 92 -->

We are again reduced to the case $\mathfrak{p} = 0$, since all the hypotheses are preserved by dividing, hence $A$ is
integral. We are reduced to the following statement.

**Corollary.**

<!-- label: IV.2.5 -->

With $M$ as above, every minimal prime ideal $\mathfrak{q}$ of $B$ induces a prime ideal $\mathfrak{p}$ of $A$ that is
minimal.

Indeed, localizing at $\mathfrak{p}$ and $\mathfrak{q}$, we are reduced to proving that if $A$ and $B$ are local,
$A \to B$ is local, $M$ is a nonzero $B$-module flat over $A$, and $B$ has dimension `0`, then $A$ has dimension `0`. By
IV.2.2 and IV.2.3, every prime ideal of $A$ is induced by a prime ideal of $B$, hence by the maximal ideal of $B$, and
therefore is the maximal ideal, as required. Geometrically, IV.2.5 means that every irreducible component of
$X = \operatorname{Spec}(B)$ dominates some irreducible component of $Y = \operatorname{Spec}(A)$, provided there exists
a quasi-coherent sheaf of finite type on $X$, with support $X$, and flat relative to $Y$.

Note that in IV.2.4 we did not have to suppose $M$ faithfully flat over $A$, but then nothing guarantees the existence
of a prime ideal containing $\mathfrak{p}B$, and hence of a minimal one among such ideals.

**Proposition.**

<!-- label: IV.2.6 -->

Let $i: A \to B$ be a homomorphism of rings. The following conditions are equivalent:

1. $B$ is a faithfully flat $A$-module.
1. $B$ is flat over $A$, and $\operatorname{Spec}(B) \to \operatorname{Spec}(A)$ is surjective.
1. $B$ is flat over $A$, and every maximal ideal is induced by an ideal of $B$.
1. $i$ is injective and `Coker i` is a flat $A$-module.
1. The functor $M_{(B)} = M \otimes_{A} B$ in the $A$-module $M$ is exact, and the canonical functorial homomorphism
   $M \to M_{(B)}$ is injective.
1. For every ideal $I$ of $A$, $I \otimes_{A} B \to IB$ is an isomorphism, and the inverse image of `IB` in $A$ is equal
   to $I$.

We have (i) ⇒ (ii) by IV.2.3; (ii) ⇒ (ii bis) is trivial; (ii bis) ⇒ (i) by criterion (i ter) of IV.2.1. We have (iii) ⇒
(iv) by IV.1.1; (iv) ⇒ (iv bis) trivially, taking $M = A/I$ in the second condition (iv bis); and (iv bis) ⇒ (i) by the
flatness criterion by ideals seen at the beginning of IV.1 and by criterion IV.2.1 (i ter). Finally, (iv) ⇒ (iii) by an
easy converse of IV.1.1, and (i) ⇒ (iv), because if $N$ is the kernel of $M \to M \otimes_{A} B = T(M)$, then, since $T$
is exact, $N \to T(N)$ is zero; hence $T(N) = N \otimes_{A} B = 0$, whence $N = 0$.

## 3. Relations with Completion

<!-- label: IV.3 -->

Let $A$ be a noetherian ring, let $I$ be an ideal in $A$, let `Â` be the separated completion of $A$ for the $I$-preadic
topology, and for every $A$-module $M$, let $\hat{M}$ be its completion for the $I$-preadic topology. This is an
`Â`-module, whence a canonical homomorphism

```text
M ⊗_A Â → M̂.
```

When $M$ ranges over **modules of finite type**, the functor $M \mapsto \hat{M}$ is exact, as follows easily from
**Krull's theorem: if $N \subset M$, then the topology of $N$ is the one induced by the topology of $M$**. Since
$M \otimes_{A} \hat{A}$ is right exact, one easily concludes, by resolving $M$ by $L \to L' \to M$ with $L$ and $L'$
free of finite type, that the functorial homomorphism above is an **isomorphism**, since $\hat{M}$ is also right exact,
and consequently that $M \otimes_{A} \hat{A}$ is also an **exact** functor in $M$. Therefore:

**Proposition.**

<!-- label: IV.3.1 -->

Let $A$ be a noetherian ring and $I$ an ideal of $A$. Then the separated completion `Â` of $A$, for the $I$-preadic
topology, is **flat** over $A$.

**Corollary.**

<!-- label: IV.3.2 -->

In order that `Â` be faithfully flat over $A$, it is necessary and sufficient that $I$ be contained in the radical of
$A$.

Indeed, it suffices to apply criterion IV.2.1 (i ter).

These results summarize all that can be said, from the viewpoint of linear algebra, about the relations between $A$ and
`Â`. Corollary IV.3.2 is used especially when $A$ is a noetherian local ring and $I$ is contained in the maximal ideal
$\mathfrak{m}$, and most often is equal to it.

## 4. Relations with Free Modules

<!-- label: IV.4 -->

**Proposition.**

<!-- label: IV.4.1 -->

Let $A$ be a ring, let $I$ be an ideal of $A$, and let $M$ be an $A$-module. Suppose one is under one or the other of
the following hypotheses:

1. $I$ is nilpotent.
1. $A$ is noetherian, $I$ lies in the radical of $A$, and $M$ is of finite type.

In order that $M$ be free over $A$, it is necessary and sufficient that $M \otimes A/I$ be free over $A/I$ and that
$Tor^{A}_{1}(M,A/I) = 0$.

This is necessary. We prove the sufficiency. Let $(e_{i})$ be a family of elements of $M$ whose image in
$M \otimes A/I = M/IM$ defines a basis there over $A/I$; it is a finite family in case (b). Let $L$ be the free
$A$-module constructed on the same index set. Thus there is a homomorphism $L \to M$ such that tensoring $T$ by $A/I$
induces an isomorphism $T(L) \to T(M)$. If $Q$ is the cokernel of $L \to M$, then $T(Q) = 0$, whence $Q = 0$ by
Nakayama, valid under either condition (a) or (b). Thus $L \to M$ is surjective. Let $R$ be its kernel. We then have an
exact sequence

$$
0 \to R \to L \to M \to 0,
$$

whence, since $Tor^{A}_{1}(M,A/I) = 0$, an exact sequence $0 \to T(R) \to T(L) \to T(M) \to 0$, whence $T(R) = 0$, and
hence $R = 0$ again by Nakayama, taking into account that in case (b), $R$ is of finite type because $A$ was assumed
noetherian.

**Corollary.**

<!-- label: IV.4.2 -->

One may replace the condition $Tor^{A}_{1}(M,A/I) = 0$ by: the canonical surjective homomorphism

```text
gr_I^0(M) ⊗_{A/I} gr_I(A) → gr_I(M)
```

<!-- label: eq:IV.2.* -->

is an isomorphism.

Indeed, if $M$ is free, this is certainly verified. Thus one must prove that if $M \otimes A/I$ is free over $A/I$ and
the condition on the associated graded objects is verified, then $M$ is free. Resume the proof above by constructing
$L \to M$. The hypothesis implies that this homomorphism induces an isomorphism on associated graded objects; hence its
kernel is contained in the intersection of the $I^{nL}$, and so is zero, trivially in (a), and by a well-known fact in
(b). This proves the assertion.

**Corollary.**

<!-- label: IV.4.3 -->

Suppose $A/I$ is a field. Then the following conditions on $M$ are equivalent:

1. $M$ is free.
1. $M$ is projective.
1. $M$ is flat.
1. $Tor^{A}_{1}(M,A/I) = 0$.
1. The canonical homomorphism IV.4.2 is bijective.

Indeed, in the case considered, $M \otimes A/I$ is automatically free.

The preceding result is valid in the following two cases:

1. $M$ is an **arbitrary** module over a local ring $A$ whose maximal ideal $I$ is **nilpotent**, for example an
   artinian local ring.
1. $M$ is a module **of finite type** over a **noetherian local** ring.

Recall, for reference:

**Corollary.**

<!-- label: IV.4.4 -->

<!-- original page 95 -->

Suppose $A$ is a **noetherian local integral** ring with maximal ideal $\mathfrak{m} = I$, residue field $k = A/I$, and
field of fractions $K$. Let $M$ be a module of finite type over $A$. Then the preceding equivalent conditions (i) to (v)
are also equivalent to:

1. $M \otimes_{A} K$ and $M \otimes_{A} k$ are vector spaces of the same dimension, i.e. the rank of $M$ over $A$ is
   equal to the minimum number of generators of the $A$-module $M$.

The proof is immediate. We leave it to the reader to generalize to the case where $A$ is only assumed to have no
nilpotent elements; one must then require that the ranks of $M$ at the minimal prime ideals of $A$ be equal to the
dimension of the vector space $M \otimes_{A} k$.

## 5. Local Flatness Criteria

<!-- label: IV.5 -->

**Proposition.**

<!-- label: IV.5.1 -->

Let $A$ be a ring equipped with an ideal $I$, and let $M$ be an $A$-module. Suppose

$$
Tor^{A}_{1}(M,A/I^{n}) = 0     for n > 0.
$$

Then the canonical surjective homomorphism

```text
gr_I^0(M) ⊗_{A/I} gr_I(A) → gr_I(M)
```

<!-- label: eq:IV.5.1.* -->

is an isomorphism. The converse is true if $I$ is nilpotent.

The hypothesis means that the homomorphisms

```text
I^n ⊗_A M → I^nM
```

are isomorphisms, whence at once the fact that the homomorphisms

```text
I^n/I^{n+1} ⊗_A M → I^nM/I^{n+1}M
```

are isomorphisms. Conversely, suppose this condition holds and $I$ is nilpotent. We prove $Tor^{A}_{1}(M,A/I^{n}) = 0$
for every $n$. This is true for large $n$, so proceed by descending induction on $n$, supposing it proved for $n + 1$.
We have a commutative diagram

```text
        M ⊗ I^{n+1}  →  M ⊗ I^n  →  M ⊗ (I^n/I^{n+1})  →  0
              ↓              ↓                 ↓
0  →       MI^{n+1}  →      MI^n  →       MI^n/MI^{n+1} →  0
```

whose rows are exact. By hypothesis, the last vertical arrow is an isomorphism, and the induction hypothesis also means
that the first vertical arrow is one. The same is therefore true of the middle vertical arrow, which completes the
proof.

The following proposition was isolated by Serre at the time of the Seminar; it allows substantial simplifications in the
present number.

**Proposition.**

<!-- label: IV.5.2 -->

Let $A \to B$ be a homomorphism of rings, and let $M$ be an $A$-module. The following conditions are equivalent:

1. For every $B$-module $N$, one has $Tor^{A}_{1}(M,N) = 0$.
1. $Tor^{A}_{1}(M,B) = 0$, and $M_{(B)} = M \otimes_{A} B$ is $B$-flat.

There is a functorial isomorphism

```text
M ⊗_A N = (M ⊗_A B) ⊗_B N,
```

which expresses the left-hand side, regarded as a functor in $M$, as a composite of two functors
$M \mapsto M \otimes_{A} B$ and $P \mapsto P \otimes_{B} N$. Since the first sends free $A$-modules to free $B$-modules,
hence projectives to projectives, one has the spectral sequence for composite functors

```text
Tor^A_n(M,N) ⇐ Tor^B_p(Tor^A_q(M,B),N),
```

whence an exact sequence in low degrees

```text
0 ← Tor^B_1(M ⊗_A B,N) ← Tor^A_1(M,N) ← Tor^A_1(M,B) ⊗_A N.
```

If (i) holds, then from this exact sequence one concludes $Tor^{B}_{1}(M \otimes_{A} B,N) = 0$ for every $N$, i.e.
$M \otimes_{A} B$ is $B$-flat, hence (ii). Conversely, if (ii) holds, then in the exact sequence the terms surrounding
$Tor^{A}_{1}(M,N)$ are zero, hence (i) holds.

**Corollary.**

<!-- label: IV.5.3 -->

Suppose $B = A/I$. Then the preceding conditions are equivalent to:

1. $Tor^{A}_{1}(M,N) = 0$ for every $A$-module $N$ annihilated by a power of $I$.

Indeed, (i) means that this holds if $N$ is annihilated by $I$. One deduces (iii) by applying the hypothesis to the
$I^{nN}/I^{n+1}N$.

**Corollary.**

<!-- label: IV.5.4 -->

Under the conditions of IV.5.3, the conditions under consideration imply that the functorial homomorphism

```text
gr_I^0(M) ⊗_{A/I} gr_I(A) → gr_I(M)
```

<!-- label: eq:IV.5.* -->

is an isomorphism, and that $M \otimes_{A} A/I$ is flat over $A/I$.

It suffices to apply (iii) and IV.5.1. Using the converse of IV.5.1 when $I$ is nilpotent, one finds:

**Corollary.**

<!-- label: IV.5.5 -->

Let $A$ be a ring equipped with a nilpotent ideal $I$, and let $M$ be an $A$-module. The following conditions are
equivalent:

1. $M$ is $A$-flat.
1. $M \otimes_{A} A/I$ is $A/I$-flat, and $Tor^{A}_{1}(M,A/I) = 0$.
1. $M \otimes_{A} A/I$ is $A/I$-flat, and the canonical homomorphism $IV.5.*$ on associated graded objects is an
   isomorphism.

Indeed, these are respectively the preceding conditions (iii) and (ii), and those of Corollary IV.5.4.

No longer suppose $I$ nilpotent. Then in IV.5.5 one will only have a priori the implications (i) ⇒ (ii) ⇒ (iii). On the
other hand, since condition (iii) remains stable after dividing by a power of $I$, one sees by IV.5.5 that it implies:

1. **For every integer $n$, $M \otimes A/I^{n}$ is flat over $A/I^{n}$.**

We propose to give conditions under which one can conclude (i), i.e. that $M$ is $A$-flat. I say that it suffices for
this that $A$ be noetherian and that $M$ satisfy the following finiteness condition: **for every module $N$ of finite
type over $A$, $M \otimes_{A} N$ is separated for the $I$-preadic topology**. It would suffice to verify this when $N$
is an ideal of finite type in $A$. Indeed, let us prove that under these conditions, if $N' \to N$ is a monomorphism of
finite-type modules, then $M \otimes_{A} N' \to M \otimes_{A} N$ is a monomorphism. It is enough to show that the kernel
is contained in the

```text
I^n(M ⊗_A N′) = Im(M ⊗_A I^nN′ → M ⊗_A N′),
```

or again in the

```text
Im(M ⊗_A V′_n → M ⊗_A N′) = Ker(M ⊗_A N′ → M ⊗_A (N′/V′_n)),
```

where $V'_{n}$ runs through a countable fundamental system of neighborhoods of `0` in $N'$, endowed with its $I$-adic
topology. By Krull's theorem, the $I$-adic topology of $N'$ is induced by that of $N$, so one may take
$V'_{n} = N' \cap I^{nN}$. Consider then the commutative diagram

```text
M ⊗_A N′          →  M ⊗_A (N′/V′_n)
↓                    ↓
M ⊗_A N           →  M ⊗_A (N/I^nN).
```

<!-- original page 98 -->

Since $N'/V'_{n}$ and $N/I^{nN}$ are annihilated by $I^{n}$, the second vertical homomorphism identifies with the one
obtained from the **injective** homomorphism $N'/V'_{n} \to N/I^{nN}$ by tensoring over $A/I^{n}$ with the **flat**
$A/I^{n}$-module $M \otimes_{A} A/I^{n}$; it is therefore **injective**. Consequently, the kernel of
$M \otimes_{A} N' \to M \otimes_{A} N$ is contained in the kernel of $M \otimes_{A} N' \to M \otimes_{A} (N'/V'_{n})$,
which is what was required.

The “finiteness” condition considered for $M$ is satisfied in particular if $M$ is a module of finite type over a
noetherian $A$-algebra $B$ such that `IB` is contained in the radical of $B$: indeed, then $M \otimes_{A} N$ is a module
of finite type over $B$ for every module $N$ of finite type over $A$, hence is separated by Krull for the $I$-adic
topology, which is its `IB`-adic topology. Thus one obtains:

**Theorem.**

<!-- label: IV.5.6 -->

Let $A \to B$ be a homomorphism of noetherian rings, let $I$ be an ideal of $A$ such that `IB` is contained in the
radical of $B$, and let $M$ be a $B$-module of finite type. The following conditions are equivalent:

1. $M$ is $A$-flat.
1. $M \otimes_{A} A/I$ is $A/I$-flat, and $Tor^{A}_{1}(M,A/I) = 0$.
1. $M \otimes_{A} A/I$ is $A/I$-flat, and the canonical homomorphism

```text
gr_I^0(M) ⊗_{A/I} gr_I(A) → gr_I(M)
```

is an isomorphism. 4. For every integer $n$, $M \otimes_{A} A/I^{n}$ is flat over $A/I^{n}$.

This result applies especially when $A$ and $B$ are **local** noetherian rings, $A \to B$ a local homomorphism, and $I$
an ideal of $A$ contained in its maximal ideal; and one can immediately reduce IV.5.6 to this case. An interesting case
is that where $A/I$ is a field, i.e. $I$ is maximal; then the condition that $M \otimes_{A} A/I$ be flat over $A/I$
becomes superfluous. Moreover, since the $A/I^{n}$ are artinian local rings, condition (iv) means that the
$M \otimes_{A} A/I^{n}$ are **free** over the $A/I^{n}$.

**Corollary.**

<!-- label: IV.5.7 -->

Let $A \to B$ be a local homomorphism of noetherian local rings, and let $u: M' \to M$ be a homomorphism of $B$-modules
of finite type. Suppose $M$ is flat over $A$. Then the following conditions are equivalent:

1. $u$ is injective, and `Coker u` is flat over $A$.
1. $u \otimes_{A} k: M' \otimes_{A} k \to M \otimes_{A} k$ is injective,

where $k$ denotes the residue field of $A$.

(i) ⇒ (ii) by IV.1.1. We prove the converse. First, $u$ is injective, for it suffices to verify this on associated
graded objects, where it follows from a commutative square that the reader will write. Let $M''$ be its cokernel. We
then have an exact sequence

$$
0 \to M' \to M \to M'' \to 0.
$$

By the exact sequence of Tor, taking into account hypothesis (ii) and $Tor^{A}_{1}(M,k) = 0$, we get
$Tor^{A}_{1}(M'',k) = 0$; hence $M''$ is flat over $A$ by Theorem IV.5.6.

**Corollary.**

<!-- label: IV.5.8 -->

Under the conditions of IV.5.6, let $J$ be an ideal of $B$ containing `IB` and contained in the radical. Let `Â` be the
$I$-adic completion of $A$, and let $\hat{B}$ and $\hat{M}$ be the $J$-adic completions of $B$ and $M$. In order that
$M$ be $A$-flat, it is necessary and sufficient that $M$ be `Â`-flat.

The sufficiency would already follow easily from IV.3.2. One uses criterion (iii) of IV.5.6 in the situation $(A,B,I,M)$
and in the situation $(\hat{A},\hat{B},I\hat{A},\hat{M})$. One observes that the conditions obtained in the two cases
are equivalent by IV.3.2.

**Corollary.**

<!-- label: IV.5.9 -->

Let $A \to B \to C$ be local homomorphisms of noetherian local rings, and let $M$ be a $C$-module of finite type. Here
$C$ occurs only so that a finiteness condition can be placed on $M$. Suppose $B$ is flat over $A$. Let $k$ be the
residue field of $A$. The following conditions are equivalent:

1. $M$ is flat over $B$.
1. $M$ is flat over $A$, and $M \otimes_{A} k$ is flat over $B \otimes_{A} k$.

The implication (i) ⇒ (ii) is trivial. We prove (ii) ⇒ (i). Apply criterion (iii) of IV.5.6 to
$(B,C,\mathfrak{m}B = I,M)$. Since

```text
M ⊗_B (B/I) = M ⊗_B (B ⊗_A k) = M ⊗_A k,
```

the first condition of this criterion says precisely that $M \otimes_{A} k$ is flat over $B \otimes_{A} k$. The second
condition of the criterion is satisfied because $M$ is flat over $A$ and $B$ is flat over $A$, by an associativity
formula for the tensor product. Of course, referring to IV.5.5 instead of IV.5.6, one obtains an analogous statement
without noetherian and finiteness assumptions, when one supposes instead that the ideal $\mathfrak{m}$ of $A$ is
nilpotent. The fact that $\mathfrak{m}$ was taken maximal did not enter; but in a sense the case “$\mathfrak{m}$
maximal” is “the best possible”.

## 6. Flat Morphisms and Open Sets

<!-- label: IV.6 -->

Recall first some results on constructible sets, which are proved in circulating notes from the Dieudonné-Rosenlicht
Seminar on Schemes.[^iv-6-0-1]

Let $X$ be a topological space. Following Chevalley, a subset of $X$ is called **constructible** if it is a finite union
of locally closed subsets.

**Lemma.**

<!-- label: IV.6.1 -->

Let $X$ be a noetherian topological space, and let $Z$ be a subset of $X$. In order that $Z$ be constructible, it is
necessary and sufficient that for every irreducible closed subset $Y$ of $X$, $Z \cap Y$ is nondense in $Y$ or contains
a nonempty open subset of the space $Y$.

One deduces from this, using a well-known lemma of commutative algebra:

**Lemma (Chevalley).**

<!-- label: IV.6.2 -->

Let $f: X \to Y$ be a morphism of finite type of preschemes, with $Y$ noetherian. Then $f(X)$ is constructible.

**Lemma.**

<!-- label: IV.6.3 -->

Let $X$ be a noetherian topological space in which every irreducible closed subset admits a generic point, let $U$ be a
constructible subset of $X$, and let $x \in X$. In order that $U$ be a neighborhood of $x$, it is necessary and
sufficient that every generization $y$ of $x$, i.e. every $y \in X$ such that $x \in closure(y)$, belongs to $U$.

In particular:

**Corollary.**

<!-- label: IV.6.4 -->

Let $X$ be a noetherian topological space in which every irreducible closed subset admits a generic point, and let $U$
be a subset of $X$. In order that $U$ be open, it is necessary and sufficient that it satisfy the following two
conditions:

1. $U$ contains every generization of each of its points.
1. If $x \in U$, then $U \cap closure(x)$ contains a nonempty open subset of the space $closure(x)$.

Indeed, $U$ is necessarily constructible by IV.6.1, and one applies criterion IV.6.2, which proves that $U$ is a
neighborhood of each of its points.

**Corollary.**

<!-- label: IV.6.5 -->

Let $f: X \to Y$ be a morphism of finite type of preschemes, with $Y$ locally noetherian, let $x$ be a point of $X$, and
let $y = f(x)$. In order that $f$ transform every neighborhood of $x$ into a neighborhood of $y$, it is necessary and
sufficient that for every generization $y'$ of $y$, there exist a generization $x'$ of $x$ such that $f(x') = y'$.

We may evidently suppose $X$ and $Y$ affine, hence noetherian. The condition is sufficient, for it is enough to prove
that $f(X)$ is a neighborhood of $y$; but $f(X)$ is constructible by IV.6.1, and it suffices to apply criterion IV.6.3.
The condition is necessary: let $Y' = closure(y')$, and let $F$ be the union of the irreducible components of
$f^{-1}(Y')$ that do not contain $x$. Then $X - F$ is an open neighborhood of $x$, so its image is a neighborhood of
$y$, and a fortiori contains $y'$. Thus there exists $x'_{1} \in X - F$ such that $f(x'_{1}) = y'$. Consider an
irreducible component of $f^{-1}(Y')$ containing $x'_{1}$; it necessarily contains $x$

otherwise it would be contained in $F$. Let $x'$ be its generic point. This is a generization of $x$, and $f(x')$ is a
generization of $f(x'_{1}) = y'$ contained in $Y'$, hence is equal to $y'$, as required.

**Theorem.**

<!-- label: IV.6.6 -->

Let $f: X \to Y$ be a morphism locally of finite type, with $Y$ locally noetherian, and let $F$ be a coherent sheaf on
$X$ with support $X$, flat relative to $Y$. Then $f$ is an open morphism, i.e. transforms open sets into open sets.

It suffices to prove criterion IV.6.5 for every point $x \in X$. The generizations $x'$ of $x$ correspond to the prime
ideals of $\mathcal{O}_{x}$, those $y'$ of $y$ correspond to the prime ideals of $\mathcal{O}_{y}$, and therefore one
must verify that every prime ideal of $\mathcal{O}_{y}$ is induced by a prime ideal of $\mathcal{O}_{x}$. But $F_{x}$ is
a nonzero $\mathcal{O}_{x}$-module, flat over $\mathcal{O}_{y}$, hence faithfully flat over $\mathcal{O}_{y}$ by IV.2.2.
We may therefore apply IV.2.3, which completes the proof.

**Remarks.** Since flatness is preserved under extension of the base, one sees that under the conditions of IV.6.5, $f$
is even **universally open**. I do not know, however, when $Y$ is integral and $X$ is of finite type over $Y$, whether
$f$ induces on every component $X_{i}$ of $X$ an open morphism, or even only an equidimensional one,[^iv-6-6-1] i.e. one
whose fiber components all have the same dimension; one only knows that $X_{i}$ **dominates** $Y$. The question is
related to the following one: let $A \to B$ be a local homomorphism of noetherian local rings, such that $B$ is flat
over $A$ and $\mathfrak{m}B$ is an ideal of definition of $B$, which implies moreover $\dim B = \dim A$. Is it true that
for every minimal prime ideal $\mathfrak{p}_{i}$ of $B$ one has $\dim B/\mathfrak{p}_{i} = \dim B$? Let us only point
out that the answer to the first question is negative if one replaces the flatness hypothesis of IV.6.5 by the sole
hypothesis that $f$ is universally open.

**Lemma.**

<!-- label: IV.6.7 -->

Let $A$ be a noetherian integral ring, let $B$ be an $A$-algebra of finite type, and let $M$ be a $B$-module of finite
type. Then there exists a nonzero element $f$ of $A$ such that $M_{f}$ is a free, a fortiori flat, module over $A_{f}$.

Let $K$ be the field of fractions of $A$. Then $B \otimes_{A} K$ is an algebra of finite type over $K$, and
$M \otimes_{A} K$ is a module of finite type over it. Let $n$ be the dimension of the support of this module; we argue
by induction on $n$. If $n < 0$, i.e. if $M \otimes_{A} K = 0$, then taking a finite set of generators of $M$ over $B$,
one sees that there exists $f \in A$ annihilating these generators, hence annihilating $M$; thus $M_{f} = 0$, and we are
done. Suppose $n \geq 0$. We know that the $B$-module $M$ admits a composition series whose successive quotients are
isomorphic to modules $B/\mathfrak{p}_{i}$, with $\mathfrak{p}_{i}$ prime ideals of $B$. Since an extension of free
modules is free, we are reduced to the case where $M$ itself is of the form $B/\mathfrak{p}$, or again identical with
$B$, with $B$ an **integral** $A$-algebra. Applying Noether's normalization lemma to the $K$-algebra $B \otimes_{A} K$,
one sees easily that there exists a nonzero element $f$ of $A$ such that $B_{f}$ is integral over the subring
$A_{f}[t_{1},...,t_{n}]$, where the $t_{i}$ are indeterminates. Thus we may already suppose $B$ is integral over
$C = A[t_{1},...,t_{n}]$; it is then a finite torsion-free $C$-module. Let $m$ be its rank. There is therefore an exact
sequence of $C$-modules

$$
0 \to C^{m} \to B \to M' \to 0
$$

where $M'$ is a torsion $C$-module. It follows that the Krull dimension of the $C \otimes_{A} K$-module
$M' \otimes_{A} K$ is strictly less than the dimension $n$ of $C \otimes_{A} K$. By the induction hypothesis, after
localizing with respect to a suitable nonzero $f$ of $A$, we may suppose that $M'$ is a free $A$-module. On the other
hand, $C^{m}$ is a free $A$-module. Hence $B$ is then a free $A$-module, and we are done.

**Lemma.**

<!-- label: IV.6.8 -->

Let $A$ be a noetherian ring, $B$ an algebra of finite type over $A$, $M$ a $B$-module of finite type, $\mathfrak{p}$ a
prime ideal of $B$, and $\mathfrak{q}$ the prime ideal it induces on $A$. Suppose $M_{\mathfrak{p}}$ is flat over
$A_{\mathfrak{q}}$, equivalently over $A$. Then there exists $g \in B - \mathfrak{p}$ such that:

1. $(M/\mathfrak{q}M)_{g}$ is flat over $A/\mathfrak{q}$.
1. $Tor^{A}_{1}(M,A/\mathfrak{q})_{g} = 0$.

Indeed, applying IV.6.7 to $(A/\mathfrak{q}, B/\mathfrak{q}B, M/\mathfrak{q}M)$, one first sees that there exists $f$ in
$A - \mathfrak{q}$ such that $(M/\mathfrak{q}M)_{f}$ is flat over $A/\mathfrak{q}$. On the other hand, since
$M_{\mathfrak{p}}$ is flat over $A$, we have

$$
Tor^{A}_{1}(M,A/\mathfrak{q})_{\mathfrak{p}} = Tor^{A}_{1}(M_{\mathfrak{p}},A/\mathfrak{q}) = 0.
$$

Since $Tor^{A}_{1}(M,A/\mathfrak{q})$ is a $B$-module of finite type, there exists $g \in B - \mathfrak{p}$ such that
(b) holds. Replacing $g$ by `gf`, we may then suppose that (a) also holds, which proves the corollary.

**Corollary.**

<!-- label: IV.6.9 -->

With the notation of IV.6.8, for every prime ideal $\mathfrak{p}'$ of $B$ containing $\mathfrak{p}$ and not containing
$g$, $M_{\mathfrak{p}'}$ is flat over $A$, equivalently over $A_{\mathfrak{q}'}$, where $\mathfrak{q}'$ is the prime
ideal of $A$ induced by $\mathfrak{p}'$.

It suffices to apply criterion IV.5.6 (ii) to the system $(A, B_{\mathfrak{q}'}, \mathfrak{q}, M_{\mathfrak{q}'})$,
using localization of Tor.

**Theorem.**

<!-- label: IV.6.10 -->

Let $f: X \to Y$ be a morphism of finite type, with $Y$ locally noetherian, and let $F$ be a coherent sheaf on $X$. Let
$U$ be the set of points $x \in X$ such that $F_{x}$ is flat over $\mathcal{O}_{f(x)}$. Then $U$ is an **open** set.

**Proof.** We may suppose $X$ and $Y$ affine, with rings $B$ and $A$, so $F$ is defined by a $B$-module $M$ of finite
type. We apply criterion IV.6.4. Condition (a) is trivially verified by IV.1.2 (i); it remains to verify condition (b)
of IV.6.4. This is what was done in Lemma IV.6.8 and Corollary IV.6.9.

In many questions, the following weaker form of Theorem IV.6.10 is sufficient; it already follows from Lemma IV.6.7, and
therefore requires neither the technique of constructible sets nor Theorem IV.5.6.

**Corollary.**

<!-- label: IV.6.11 -->

Under the conditions of IV.6.10, if one supposes $Y$ integral, then there exists a nonempty open $V$ in $Y$ such that
$F$ is flat relative to $Y$ at all points of $f^{-1}(V)$.

Indeed, the open set $U$ contains the fiber of the generic point of $Y$, since the local ring of this point is a field;
hence it contains an open set of the form $f^{-1}(V)$, since $X$ is of finite type over $Y$. From IV.6.11 one also
easily concludes the following result, where $Y$ is supposed noetherian but not necessarily integral: there exists a
partition of $Y$ into locally closed subsets $Y_{i}$ such that, giving $Y_{i}$ the induced reduced structure, $F$
induces on each $X_{i} = X \times_{Y} Y_{i}$ a sheaf flat relative to $Y_{i}$.

<!-- end of Exposé IV source block: next chapter begins at smf_doc-math_3_01.tex line 7383 -->

[^iv-0-1]: Cf. EGA IV 11 and 12.

[^iv-0-2]: And, for a more detailed exposition, Exposés VIII and IX below.

[^iv-0-3]: N. Bourbaki, _Algèbre Commutative_, Chap. I, Modules plats, Act. Sci. Ind. 1290, Paris, Hermann, 1961.

[^iv-6-0-1]: Cf. EGA 0_III 9, EGA IV 1.8 and 1.10.

[^iv-6-6-1]: The answer to the second question is affirmative, and to the first negative even if $f$ is étale; cf. EGA
    IV 12.1.1.5 and EGA Err_IV 33.


<!-- SOURCE: 05-le-groupe-fondamental-generalites.md -->

# Exposé V. The Fundamental Group: Generalities

<!-- label: V -->

<!-- original page 105 -->

## Introduction

The present Seminar is the continuation of the 1960 Seminar. We refer to the latter by sigla such as I.9.7, meaning:
Séminaire de Géométrie Algébrique, Exposé I, no. 9.7. The numbers of the 1961 exposés will follow those of 1960. We
refer to the Éléments de Géométrie Algébrique of Dieudonné-Grothendieck by sigla such as EGA I 8.7.3.

The present exposé summarizes, with slight additions, the last exposés of 1960, which had not been written up.

As in 1961, we shall generally restrict ourselves to locally noetherian preschemes, although this restriction is often
inessential. In Exposé VI we shall admit the theory of faithfully flat descent, summarized in Bourbaki Seminar no. 190.
If need be, we shall give a more detailed exposition in a later exposé,[^v-intro-1] once the reader has had occasion to
convince himself of the usefulness of this technique for the theory of the fundamental group.

## 1. Prescheme with a Finite Group of Operators; Quotient Prescheme

<!-- label: V.1 -->

Let $X$ be a prescheme, and let $G$ be a finite group operating on $X$ by automorphisms, on the right to fix ideas. If
$X$ is affine with ring $A$, then $G$ operates by automorphisms on the left on $A$.

For every prescheme $Z$, $G$ operates on the left on the set $\operatorname{Hom}(X,Z)$, so one may consider the set

$$
\operatorname{Hom}(X,Z)^{G}
$$

of morphisms invariant under $G$. This depends functorially on $Z$; one may ask whether this functor is “representable”,
i.e. isomorphic to a functor $Z \mapsto \operatorname{Hom}(Y,Z)$. This means that one can find a prescheme $Y$ and a
morphism invariant under $G$,

$$
p: X \to Y,
$$

such that for every $Z$, the corresponding map $g \mapsto gp$,

$$
\operatorname{Hom}(Y,Z) \to \operatorname{Hom}(X,Z)^{G}
$$

is bijective. One then says that $(Y,p)$ is a **quotient prescheme** of $X$ by $G$; it is determined up to unique
isomorphism.

**Proposition.**

<!-- label: V.1.1 -->

Let $A$ be a ring on which the finite group $G$ operates on the left, let $B = A^{G}$ be the subring of invariants of
$A$, let $X = \operatorname{Spec}(A)$ and $Y = \operatorname{Spec}(B)$, and let $p: X \to Y$ be the canonical morphism,
evidently invariant under $G$. Then:

1. $A$ is integral over $B$, i.e. $p$ is an **integral** morphism.
1. The morphism $p$ is surjective, its fibers are the orbits of $G$, and the topology of $Y$ is the quotient of that of
   $X$.
1. Let $x \in X$, $y = p(x)$, and let $G_{x}$ be the stabilizer of $x$. Then $\kappa(x)$ is a quasi-Galois algebraic
   extension of $\kappa(y)$, and the canonical map from $G_{x}$ to the group $\operatorname{Gal}(\kappa(x)/\kappa(y))$
   of $\kappa(y)$-automorphisms of $\kappa(x)$ is surjective.
1. $(Y,p)$ is a quotient prescheme of $X$ by $G$.

The statements (i), (ii), (iii) are well known in commutative algebra[^v-1-1-1] and are included only for reference,
except for the assertion on the topology, which comes from the following general fact, an easy consequence of the
Cohen-Seidenberg theorem: an integral morphism is closed, i.e. transforms closed sets into closed sets. Let us note at
once:

**Corollary.**

<!-- label: V.1.2 -->

Under the preceding conditions, the natural homomorphism

$$
\mathcal{O}_{Y} \to p_{*}(\mathcal{O}_{X})^{G}
$$

is an isomorphism.

This follows at once from the formula

$$
(S^{-1}A)^{G} = S^{-1}(A^{G})
$$

valid for every multiplicatively stable subset $S$ of $B = A^{G}$. This formula is modular and is stated more generally
for a base change $A \to A'$ that is **flat**; apply it to the case where $S$ is generated by an element $f$ of $B$.

Assertion (ii) and Corollary V.1.2 easily imply (iv). More generally, we shall have the following.

**Proposition.**

<!-- label: V.1.3 -->

Let $X$ be a prescheme with a finite group $G$ of automorphisms, and let $p: X \to Y$ be an invariant affine morphism
such that

$$
\mathcal{O}_{Y} \to p_{*}(\mathcal{O}_{X})^{G}
$$

is an isomorphism. Then the conclusions (i), (ii), (iii), (iv) of V.1.1 are still valid.

Indeed, for (i), (ii), (iii), we may suppose $Y$ and hence $X$ affine; if $B$ and $A$ are their rings, the hypothesis
implies $B = A^{G}$, and it suffices to apply V.1.1. For (iv), use (ii) and
$\mathcal{O}_{Y} = p_{*}(\mathcal{O}_{X})^{G}$.

**Corollary.**

<!-- label: V.1.4 -->

Under the conditions of V.1.3, for every open $U$ of $Y$, $U$ is a quotient of $X|U = p^{-1}(U)$ by $G$.

Indeed, $p^{-1}(U) \to U$ induced by $p$ satisfies the same hypotheses as $p$.

If now $X$ is a $Z$-prescheme and the operations of $G$ are $Z$-automorphisms, then by (iv) $Y$ is a $Z$-prescheme. With
this understood:

**Corollary.**

<!-- label: V.1.5 -->

In order that $X$ be affine, respectively separated, over $Z$, it is necessary and sufficient that $Y$ be so. If $X$ is
of finite type over $Z$, then it is **finite** over $Y$; if moreover $Z$ is locally noetherian, then $Y$ is of finite
type over $Z$.

Since $X$ is affine, and a fortiori separated, over $Y$, if $Y$ is affine, respectively separated, over $Z$, then so is
$X$. Conversely, suppose $X$ affine over $Z$; we prove that $Y$ is so. By V.1.4 we may suppose $Z$ affine, and we are
reduced to proving that if $X$ is affine, then $Y$ is affine. This follows from the explicit determination of $Y$ as
$\operatorname{Spec}(A^{G})$ made in V.1.1. Similarly, since $p: X \to Y$ is integral, hence universally closed, and
surjective, it follows that if $X$ is separated over $Z$, then so is $Y$; this is a lemma to be isolated. Indeed, in the
diagram

```text
X ×_Z X  --p×_Zp-->  Y ×_Z Y
↑                     ↑
X   --------p------>  Y,
```

where the vertical arrows are the diagonals, the morphism $X \times_{Z} X \to Y \times_{Z} Y$ is closed, hence
transforms the diagonal, closed in $X \times_{Z} X$, into a closed subset of $Y \times_{Z} Y$, which is moreover just
the diagonal of the latter since $p$ is surjective.

If $X$ is of finite type over $Z$, it is a fortiori of finite type over $Y$; hence it is finite over $Y$, since it is
already integral over $Y$. Suppose moreover $Z$ locally noetherian; we prove that $Y$ is of finite type over $Z$. By
V.1.4 we may suppose $Z$ affine. Since the topological space $X$ is quasi-compact and $p: X \to Y$ is surjective, $Y$ is
also quasi-compact, hence a finite union of affine opens; by V.1.4 we are reduced to the case where $Y$ is affine, and
hence $X$ affine. But then the ring $A$ of $X$ is an algebra of finite type over the ring $C$ of $Z$, which is
noetherian, and it is known that $B = A^{G}$ is then also an algebra of finite type over $C$: indeed, $A$ is integral,
hence finite, over a subalgebra $B'$ of $B$ of finite type over $C$; since $B'$ is noetherian, $B$ is also finite over
$B'$, hence of finite type over $C$.

**Corollary.**

<!-- label: V.1.6 -->

In order that $X$ be affine, respectively a scheme, it is necessary and sufficient that $Y$ be so.

**Definition.**

<!-- label: V.1.7 -->

<!-- original page 109 -->

Let $X$ be a prescheme on which a finite group $G$ operates on the right. We say that $G$ **operates admissibly** if
there exists a morphism $p: X \to Y$ having the properties of V.1.3, which implies that $X/G$ exists and is isomorphic
to $Y$.

**Proposition.**

<!-- label: V.1.8 -->

Let $X$ be a prescheme on which the finite group $G$ operates on the right. In order that $G$ operate admissibly, it is
necessary and sufficient that $X$ be a union of affine opens invariant under $G$, or again that every orbit of $G$ in
$X$ be contained in an affine open.

The latter condition is evidently implied by the first, and in turn it implies the first. Indeed, let $T$ be an orbit of
$G$ and $U$ an affine open containing it. The intersection of the transforms of $U$ by the $g$ in $G$ is then an open
$U'$ stable under $G$, containing $T$ and contained in the affine open $U$. Since in $U$ every finite subset has a
fundamental system of affine open neighborhoods, there exists an affine open neighborhood $V$ of $T$ contained in $U'$.
Its transforms by the $g$ in $G$ are affine and contained in $U'$, which is **separated**; hence their intersection
$U''$ is an affine open, invariant under $G$ and containing $T$.

With this established, the condition considered in V.1.8 is **necessary**, for one takes the inverse images $X_{i}$ of
affine opens $Y_{i}$ covering $Y$. It is sufficient, because then by V.1.1 one can construct the quotients
$Y_{i} = X_{i}/G$. In each $Y_{i}$, the image of $X_{i} \cap X_{j}$ is an open $Y_{ij}$ identifying with $X_{ij}/G$ by
V.1.4; in particular, one deduces isomorphisms $Y_{ij} \to Y_{ji}$ allowing the $Y_{i}$ to be glued to construct $Y$.
Serre prefers to construct directly the topological quotient space $Y$ of $X$ by $G$, put on it the sheaf
$p_{*}(\mathcal{O}_{X})^{G}$, and verify that $Y$ thereby becomes a prescheme and that one is then under the conditions
of V.1.3.

**Corollary.**

<!-- label: cor:V.1.7 -->

If $G$ operating on $X$ is admissible, the same is true for every subgroup $H$ of $G$; hence $X/H$ exists.

This may also be verified directly in the situation V.1.3, noting that one may always suppose $X$ affine over some $Z$
and the $s \in G$ operate by $Z$-automorphisms, for instance by taking $Z = Y$. Indeed:

**Corollary.**

<!-- label: cor:V.1.8 -->

Suppose $X$ is affine over $Z$, and the operations of $G$ are $Z$-automorphisms. Then $G$ operates on $X$ admissibly. If
$X$ is defined by a quasi-coherent sheaf of algebras $\mathcal{A}$, $Y$ is defined by the sheaf $\mathcal{A}^{G}$ of
invariants of $\mathcal{A}$ under $G$.

**Proposition.**

<!-- label: V.1.9 -->

Suppose $G$ operates admissibly on $X$, and $X/G = Y$ is a prescheme over $Z$. Consider a base-change morphism
$Z' \to Z$, and put $X' = X \times_{Z} Z'$ and $Y' = Y \times_{Z} Z'$, so that $G$ still operates on $X'$ by transport
of structure, the morphism $p': X' \to Y'$ being invariant. If $Z'$ is **flat** over $Z$, then $p'$ still satisfies the
hypotheses of V.1.3, i.e.

$$
\mathcal{O}_{Y'} \to p'_{*}(\mathcal{O}_{X'})^{G}
$$

is an isomorphism, $p'$ being affine in any case. Thus $G$ operates admissibly on $X'$, and

```text
(X/G) ×_Z Z′ ≃ (X ×_Z Z′)/G.
```

We may evidently suppose $Z = Y$, reducing to the case where moreover $Y$ and $Y'$ are affine. One must show that if $B$
is the subring of invariants of $G$ operating in $A$, and if $B'$ is an algebra over $B$ flat over $B$, then $B'$ is the
subalgebra of invariants of $A' = A \otimes_{B} B'$. This is immediate, because the exact sequence

```text
0 → B --i→ A --j→ A^(G)
```

where the last term means a power of $A$, and where $j(x)$ is the system of $s\cdot x - x$, $s \in G$, remains exact
after tensoring by $B'$.

Care must be taken that the flatness hypothesis is essential for the validity of the result. In particular, if $Y'$ is a
closed sub-prescheme of $Y$, for instance even a closed point of $Y$, and $X'$ is its inverse image in $X$, then $Y'$
**does not identify** in general with $X'/G$. We shall see that it does if $X$ is étale over $Y$.

Finally, let us give a formalism that is as convenient as it is trivial. Let $Y$ be a prescheme. Since direct sums exist
in the category of preschemes, for every set $E$ one may consider the prescheme that is the sum of a family
$(Y_{i})_{i\in E}$ of preschemes all identical to $Y$; this prescheme will be denoted $Y \times E$. It is characterized
by the formula

```text
Hom(Y × E,Z) = Hom(E,Hom(Y,Z)),
```

<!-- label: eq:V.1.* -->

<!-- original page 110 -->

where the second `Hom` evidently denotes the set of maps from the set $E$ to the set $\operatorname{Hom}(Y,Z)$. There is
a canonical morphism

$$
Y \times E \to Y
$$

making $Y \times E$ a prescheme over $Y$. Since fiber products commute with direct sums in the category of preschemes,
if $Y$ is a prescheme over another $Z$, then for a base change $Z' \to Z$ one has

```text
(Y × E) ×_Z Z′ = (Y ×_Z Z′) × E,
```

a formula useful especially if $Z = Y$. On the other hand, one concludes trivially from the definition that

```text
(Y × E) × F = Y × (E × F) = (Y × E) ×_Y (Y × F),
```

the last formula, however, following from the commutativity noted above.

For fixed $Y$, one may regard $Y \times E$ as a functor in $E$, with values in the preschemes over $Y$. By the preceding
formula this functor commutes with finite products, allowing for example every ordinary group $G$ to correspond to a
group scheme $Y \times G$ over $Y$, which is finite over $Y$ if $G$ is, etc. More generally, this functor is “left
exact”, but we shall not need that here. This functor also trivially commutes with direct sums, and it is also “right
exact”, as one sees at once from the defining formula $V.1.*$. In particular, if the finite group $G$ operates on the
right on the set $E$, then it operates on the right on $Y \times E$, and one has

```text
(Y × E)/G = Y × (E/G),
```

where in fact the quotient on the left satisfies the conditions of V.1.3; this is immediate.

## 2. Decomposition and Inertia Groups. The Étale Case

<!-- label: V.2 -->

Let $G$ be a finite group operating on the right on the prescheme $X$. If $x \in X$, the **decomposition group of $x$**
is the stabilizer $G_{d}(x)$ of $x$. This group operates canonically, on the left, on the residue field $\kappa(x)$, and
the set of elements of $G_{d}(x)$ that operate trivially is called the **inertia group** of $x$, denoted $G_{i}(x)$.

Suppose $G$ operates on $X$ admissibly and $Y$ is a prescheme over a prescheme $Z$. Fix $z \in Z$, and an algebraically
closed extension $\Omega$ of $\kappa(z)$ having transcendence degree greater than that of the $\kappa(x)/\kappa(z)$,
where $x$ is a point of $X$ over $z$. We may regard $\operatorname{Spec}(\Omega)$ as a $Z$-scheme, and the points of $X$
with values in $\Omega$ correspond to homomorphisms of $\kappa(z)$-algebras $\kappa(x) \to \Omega$, where $x$ is a point
of $X$ over $z$. Since $\Omega$ was taken large enough, every point $x$ of $X$ over $z$ is the locality of a point of
$X$ with values in $\Omega$. If $X(\Omega)$ and $Y(\Omega)$ denote respectively the sets of points of $X$ and $Y$ with
values in $\Omega$, there is a natural map

$$
X(\Omega) \to Y(\Omega).
$$

On the other hand, $G$ operates on $X(\Omega)$, and the preceding map is invariant under $G$. With this understood,
conclusions (ii) and (iii) of V.1.3 are also interpreted as follows: **the preceding map is surjective and identifies
$Y(\Omega)$ with the quotient $X(\Omega)/G$. Moreover, if $x$ is the locality of $a \in X(\Omega)$, then the stabilizer
of $a$ in $G$ is exactly the inertia group $G_{i}(x)$**. All this is in fact true without supposing $\Omega$ “large
enough”; this last hypothesis serves only to ensure that the inertia group of every element of $X$ over $z$ can be
characterized as a “geometric” stabilizer. One concludes at once, for example:

**Proposition.**

<!-- label: V.2.1 -->

Make a base extension $Z' \to Z$, whence $X' = X \times_{Z} Z'$. Let $x'$ be a point of $X'$ and $x$ its image in $X$.
Then $G_{i}(x) = G_{i}(x')$.

It suffices, in the considerations above, to take $\Omega$ to be a sufficiently large extension of $\kappa(z')$, where
$z$ and $z'$ are the images of $x$ and $x'$ in $Z$ and $Z'$.

**Proposition.**

<!-- label: V.2.2 -->

Under the conditions of V.1.3, suppose $Y$ locally noetherian and $X$ finite over $Y$. Let $H$ be a subgroup of $G$,
consider $X' = X/H$, cf. V.1.7, and let $x \in X$, $x'$ its image in $X'$, and $y$ its image in $Y$.

1. If $H \supset G_{d}(x)$, then the homomorphism $\mathcal{O}_{y} \to \mathcal{O}_{x'}$ induces an isomorphism on
   completions.
1. If $H \supset G_{i}(x)$, then the homomorphism $\mathcal{O}_{y} \to \mathcal{O}_{x'}$ is étale, i.e. $X'$ is étale
   over $Y$ at $x'$.

Let $Y_{1} = \operatorname{Spec}(\hat{\mathcal{O}}_{y})$. Make the base change $Y_{1} \to Y$. We obtain
$X_{1} = X \times_{Y} Y_{1}$ finite over $Y_{1}$, on which $G$ operates, with quotient $Y_{1}$ by V.1.9. Let $y_{1}$ be
the unique point of $Y_{1}$ over $y$. Since $\kappa(y) = \kappa(y_{1})$, it follows that the fiber of $X$ at $y$ is
isomorphic to that of $X_{1}$ at $y_{1}$, whence a unique point $x_{1}$ of $X_{1}$ over $x$. Moreover, by V.1.9 we have
$X_{1}/H = X'_{1} = X' \times_{Y} Y_{1}$. Let $x'_{1}$ be the image of $x_{1}$ in $X'_{1}$. It lies over $x'$, and one
verifies easily, since $X'$ is of finite type over $Y$, that the homomorphism
$\mathcal{O}_{x'} \to \mathcal{O}_{x'_{1}}$ induces an isomorphism on completions. Thus we are reduced to the case where
$Y$ is the spectrum of a complete local ring $B$; hence $X$ is the spectrum of a finite ring $A$ over $B$, a product of
finitely many local rings $A_{x}$ corresponding to the points $x_{i}$ of $X$ over $Y$. If $A_{0}$ corresponds to
$x = x_{0}$, then $A$ identifies with the ring $\operatorname{Hom}_{G_{d}}(G,A_{0})$ of functions $f: G \to A_{0}$ such
that $f(st) = s f(t)$ for $s \in G_{d}$, the operations of $G$ on these functions being defined by $(u f)(t) = f(tu)$.
Thus, if $H$ is any subgroup of $G$, $A^{H}$ is the ring of functions $f: G \to A_{0}$ such that

```text
f(stu) = s f(t),     s ∈ G_d, u ∈ H.
```

It is therefore a semi-local ring whose local components correspond to the double classes $G_{d} a H$ in $G$; to the
double class defined by $a \in G$ corresponds, by the map $f \mapsto f(a)$, the subring $A^{H(a)}_{0}$ of $A_{0}$, where
$H(a) = G_{d} \cap a H a^{-1}$. Moreover, the local component of $A^{H}$ corresponding to the image $x'$ of $x$ is also
the one corresponding to the double class $G_{d} H$ of the identity element; its local component is therefore
$A^{G_{d} \cap H}_{0}$. If $G_{d} \subset H$, one finds $A^{G_{d}}_{0} = A^{G} = B$, which proves (i). To prove (ii), by
passing to a suitable finite flat extension of $A$ and using V.2.1, one may reduce to the case where the residual
extension $\kappa(x)/\kappa(y)$ is trivial. But then $G_{i}(x) = G_{d}(x)$, and one is reduced to the preceding case.

**Corollary.**

<!-- label: V.2.3 -->

Under the conditions of V.2.2, suppose $G_{i}(x) = (e)$. Then $X$ is étale over $Y$ at $x$. Hence if $G_{i}(x) = (e)$
for every $x \in X$, then $X \to Y$ is an étale morphism.

There is a partial converse:

**Corollary.**

<!-- label: V.2.4 -->

Suppose $X$ connected and the group $G$ faithful on $X$. In order that $p: X \to Y = X/G$ be étale, it is necessary and
sufficient that the inertia groups of the points of $X$ be reduced to the identity element. If this is so, $G$
identifies with the group of all $Y$-automorphisms of the $Y$-scheme $X$.

Taking V.2.3 into account, we may suppose $X$ étale over $Y$. But if $s \in G$ lies in some $G_{i}(x)$, it follows from
I.5.4 that $s$ operates trivially on $X$, hence is the identity element since $G$ is faithful. This proves the first
assertion. Let $u$ be a $Y$-automorphism of $X$, and let $x \in X$. By Proposition V.1.3, there exists $s \in G$ such
that $s(x) = u(x)$, inducing the same residual homomorphism $\kappa(x) \to \kappa(x')$ as $u$. By the cited place, one
has $s = u$, completing the proof.

**Remark.**

<!-- label: V.2.5 -->

The hypothesis that $G$ operates faithfully is obviously not superfluous in Corollary V.2.4. The same is true of the
hypothesis that $X$ is connected, as one sees for example by taking $X = Y \times E$, with $E$ a finite set, and $G$ the
group of permutations of $E$: $G$ operates with plenty of inertia, nevertheless $(Y \times E)/G = Y \times (E/G) = Y$,
and $X$ is étale over $Y$. Taking for $G$ a group strictly smaller than the symmetric group of $E$, but operating
transitively on $E$, one sees that there will also be $Y$-automorphisms of $X$ not coming from $G$.

The typical example of a group $G$ operating without inertia is that of $Y \times G$, on which $G$ operates through its
operations on the factor $G$ by right translations: a $Y$-prescheme $X$ with a right group of operators $G$ is said to
be **trivial** if it is isomorphic to $Y \times G$.

To make the link between preschemes with finite groups of operators and the notion of principal bundle in a category, a
link we shall not need in the sequel of the seminar but which is important in other contexts, the following
considerations are useful. We fix a base prescheme $Y$ and place ourselves in the category of $Y$-preschemes. If $G$ is
a finite group, write for short $G_{Y} = Y \times G$. This is a finite group scheme over $Y$, cf. no. 1; and if $X$ is a
$Y$-prescheme, then

```text
X ×_Y G_Y = X × G.
```

Giving a $Y$-morphism $X \times_{Y} G_{Y} \to X$ is therefore equivalent to giving a $Y$-morphism $X \times G \to X$,
i.e. to giving, for every $g \in G$, a $Y$-morphism $T_{g}: X \to X$. One verifies at once that in order for the data of
the $T_{g}$ to define on $X$ a structure of prescheme with a right group of operators $G$, i.e. $T_{gg'} = T_{g'} T_{g}$
and $T_{e} = id_{X}$, it is necessary and sufficient that the corresponding $Y$-morphism $X \times_{Y} G_{Y} \to X$
define on $X$ a structure of $Y$-prescheme with $Y$-group scheme of operators, in the general sense of objects with
$\mathcal{C}$-group of operators in a category $\mathcal{C}$. Suppose this is so. Recall that $X$ is said to be
**formally principal homogeneous** under `G_Y`[^v-2-5-1] if the canonical morphism

```text
X ×_Y G_Y → X ×_Y X,
```

whose components are respectively $pr_{1}$ and the multiplication morphism $\pi: X \times_{Y} G_{Y} \to X$, is an
isomorphism. In the present case, identifying the first member with $X \times G$, the morphism considered is the one
that associates to every $g \in G$ the morphism

```text
(id_X,T_g) = (id_X ×_Y T_g) Δ_{X/Y}: X → X ×_Y X.
```

Thus to say that $X$ is formally principal homogeneous under `G_Y` also means that $X \times_{Y} X$ is isomorphic to the
direct sum of the transforms of the diagonal by the elements $(e,g)$ of $G \times G$, operating on $X \times_{Y} X$ in
the evident way, where $e$ denotes the identity element of $G$. If one does not want to distinguish left and right, and
wants to give a formula that remains applicable to a product of more than two factors identical to $X$, one may
formulate the condition by saying that the canonical morphism

```text
X ×_G (G × G) → X ×_Y X
```

obtained by attaching to the pair $(g,g')$ the morphism

```text
(T_g,T_{g′}) = (T_g ×_Y T_{g′}) Δ_{X/Y}: X → X ×_Y X
```

and making $G$ operate on the left on $G \times G$ by the diagonal homomorphism,

$$
s(g,g') = (sg,sg'),
$$

is an **isomorphism**.

The notion of **principal homogeneous space** is deduced from that of formally principal homogeneous space by adding an
additional axiom, ensuring that the “quotient” of $X$ by `G_Y` exists and is precisely the right unit object of the
category, here $Y$. This axiom may vary with the context, and is often most conveniently made explicit, in the yoga of
“descent”, by requiring that the object with operators become “trivial”, i.e. isomorphic to the product
$X \times_{Y} G_{Y}$, here $X \times G$, after a suitable base change of specified type, so as in practice to allow
descent techniques; cf. Grothendieck, _Technique de descente et théorèmes d'existence en Géométrie Algébrique_,
Séminaire Bourbaki no. 190, pp. 26-28.[^v-2-5-2] In this spirit, let us note here the characterization of principal
homogeneous bundles with group $G$, in the sense of the cited place:

**Proposition.**

<!-- label: V.2.6 -->

Let $Y$ be a locally noetherian prescheme, and let $X$ be a $Y$-prescheme with a finite group $G$ of operators operating
on the right. The following conditions are equivalent:

1. $X$ is finite over $Y$, $Y = X/G$, and the inertia groups of the points of $X$ are reduced to the identity.
1. There exists a faithfully flat and quasi-compact base change $Y_{1} \to Y$ such that $X_{1} = X \times_{Y} Y_{1}$ is
   a trivial $Y_{1}$-prescheme with operators, i.e. isomorphic to $Y_{1} \times G$.
1. As in (ii), but with $Y_{1} \to Y$ finite, étale, and surjective.
1. $X$ is formally principal homogeneous under `G_Y`, and faithfully flat and quasi-compact over $Y$.

**Proof.** (i) ⇒ (ii bis). Take $Y_{1} = X$, noting that $X \to Y$ is indeed finite, étale by V.2.3, and surjective. We
show that $X_{1}$ is then trivial over $Y_{1}$; this will follow from:

**Corollary.**

<!-- label: V.2.7 -->

If (i) holds and $X$ has a section over $Y$, then $X$ is a trivial space with operators.

Indeed, this section allows one to define a $G$-morphism $X \times G \to X$, surjective because $G$ is transitive on the
fibers of $X$, injective because $G$ operates without inertia; finally, it is a local isomorphism by I.5.3 since $X$ is
étale over $Y$. Hence it is an isomorphism.

(ii bis) trivially implies (ii), which implies (i), because the ingredients of (i) are “invariant” under faithfully flat
quasi-compact extension of the base: for “finite”, cf. the Bourbaki seminar cited above; for inertia groups, apply
V.2.1; and for $Y = X/G$, use a converse to V.1.9 in the case of a **faithfully flat** base change, which we forgot to
spell out.

We proved (i) ⇒ (iii) in passing, by proving (i) ⇒ (ii bis). Finally, (iii) ⇒ (ii), because the first hypothesis in
(iii) means precisely that $X$ becomes trivial after the base change $Y_{1} = X$; hence (ii), since $X$ is faithfully
flat and quasi-compact over $Y$.

**Definition.**

<!-- label: V.2.8 -->

A $Y$-prescheme $X$ with right group of operators $G$ satisfying the equivalent conditions of V.2.6 is called a
**principal covering of $Y$, with Galois group $G$**.

## 3. Automorphisms and Morphisms of Étale Coverings

<!-- label: V.3 -->

**Proposition.**

<!-- label: V.3.1 -->

Let $X$ be étale, separated, and of finite type over locally noetherian $Y$, and let $G$ be a finite group operating on
$X$ by $Y$-automorphisms. Then $G$ operates admissibly, and the quotient prescheme $X/G$ is étale over $Y$.

We do not suppose $X$ finite over $Y$; however, $X$ is quasi-projective over $Y$, whence the existence of $X/G$ by
V.1.8. We first prove:

**Corollary.**

<!-- label: V.3.2 -->

The morphism $X \to X/G$ is étale.

We may evidently suppose $G$ transitive on the set of connected components of $X$; then, by considering the stabilizer
of a connected component, we may suppose $X$ itself connected. Finally, we may suppose $G$ operates faithfully. But
then, as in V.2.4, $G$ operates without inertia, so by V.2.3 it follows that $X \to X/G$ is étale. We conclude using:

**Lemma (remorse about Exposé I).**

<!-- label: V.3.3 -->

Let $X \to X' \to Y$ be morphisms of finite type, and let $x$ be a point of $X$, with images $x'$ and $y$. Suppose $Y$
locally noetherian. If two of the morphisms under consideration are étale at the marked points, then so is the third.

It remains only to consider the case where $X \to X'$ and $X \to Y$ are étale at $x$ and prove that $X' \to Y$ is étale
at $x'$, which is the case needed for V.3.1. Making a suitable flat extension of the base $Y$, one is reduced to the
case where the residual extension $\kappa(x)/\kappa(y)$ is trivial. Consider the homomorphisms
$\mathcal{O}_{y} \to \mathcal{O}_{x'} \to \mathcal{O}_{x}$ and the homomorphisms deduced by passage to completions. The
hypothesis means that $\hat{\mathcal{O}}_{y} \to \hat{\mathcal{O}}_{x}$ and
$\hat{\mathcal{O}}_{x'} \to \hat{\mathcal{O}}_{x}$ are isomorphisms; hence at once
$\hat{\mathcal{O}}_{y} \to \hat{\mathcal{O}}_{x'}$ is one, proving the lemma.

**Corollary.**

<!-- label: V.3.4 -->

If $X$ is finite and étale over $Y$, then $X/G$ is finite and étale over $Y$.

**Proposition.**

<!-- label: V.3.5 -->

Let $X$ and $X'$ be two étale coverings of $Y$. Then every $Y$-morphism $f: X \to X'$ factors as the product of a
surjective étale morphism $X \to X''$ and the canonical immersion $X'' \to X'$ of a subset $X''$ of $X'$ that is both
open and closed.

We know by I.4.8 that $f$ is étale, hence an open morphism. On the other hand, since $X$ is finite over $Y$, $f$ is
closed, so $f(X) = X''$ is both open and closed in $X'$. This finishes the proof. It would have been enough for $X'$,
instead of being an étale covering, to be unramified over $Y$.

**Corollary.**

<!-- label: V.3.6 -->

With the preceding notation, $X \to X''$ is a strict epimorphism in the category of preschemes, and $X'' \to X'$ is a
monomorphism, indeed a strict monomorphism, in the category of preschemes.

The first assertion means by definition that the sequence of morphisms

```text
X ×_{X″} X ⇉ X → X″
```

is exact, and this follows from the fact that $X \to X''$ is finite and faithfully flat, as is easily seen; cf.
Grothendieck, loc. cit. The dual assertion for $X'' \to X'$ is even more trivial.

Corollary V.3.6 will be useful for the theory of the fundamental group in the next number. For those who do not like the
notion of strict epimorphism, it is possible to replace Corollary V.3.6 by whatever variant the reader arranges to his
personal taste. Let us only take the occasion to point out that a factorization $f = f'f''$, with $f''$ a strict
epimorphism and $f'$ a monomorphism, is necessarily unique up to unique isomorphism in any category. However, there may
simultaneously exist a factorization $f = f_{1}f_{2}$ having the dual properties: $f_{2}$ is an epimorphism and $f_{1}$
a strict monomorphism, also unique up to unique isomorphism, which is not isomorphic to the preceding one. It is enough
to take, for example, the category of topological vector spaces, separated if desired, and for $u: X \to X'$ a morphism
such that $u(X)$ is not closed.

**Proposition.**

<!-- label: V.3.7 -->

Let $Y$ be a **connected** locally noetherian prescheme, let $y$ be a point of $Y$, and let $\Omega$ be an algebraically
closed extension of $\kappa(y)$. For every $X$ over $Y$, denote by $X(\Omega)$ the set of points of $X$ with values in
$\Omega$. Let $X$ and $X'$ be étale coverings of $Y$, and let $u: X \to X'$ be a $Y$-morphism such that the
corresponding map $X(\Omega) \to X'(\Omega)$ is an isomorphism. Then $u$ is an isomorphism.

We are immediately reduced to the case where $X'$ is connected. Since $X \to X'$ is finite and étale, we know that the
geometric number of points in a fiber of $X \to X'$ is constant, and is equal to 1 if and only if the morphism under
consideration is an isomorphism. But this number is also the number of elements in a fiber of
$X(\Omega) \to X'(\Omega)$, whence the conclusion.

## 4. Axiomatic Conditions for a Galois Theory

<!-- label: V.4 -->

Let $\mathcal{C}$ be a category, and let $F$ be a covariant functor from $\mathcal{C}$ to the category of finite sets.
Suppose the following conditions are satisfied:

**(G 1)** $\mathcal{C}$ has a final object,[^v-4-1] and the fiber product of two objects over a third exists in
$\mathcal{C}$. This axiom may also be stated by saying that finite projective limits exist in $\mathcal{C}$.

**(G 2)** Finite sums in $\mathcal{C}$ exist, hence also an initial object $\emptyset_{\mathcal{C}}$ playing the role of
the empty set, as does the quotient of an object of $\mathcal{C}$ by a finite group of automorphisms.

**(G 3)** Let $u: X \to Y$ be a morphism in $\mathcal{C}$. Then $u$ factors as a product $X --u'\to Y' --u''\to Y$, with
$u'$ a **strict** epimorphism and $u''$ a monomorphism, which is an isomorphism onto a direct summand of $Y$.

**(G 4)** The functor $F$ is left exact, i.e. transforms the right unit into the right unit and commutes with fiber
products.

**(G 5)** $F$ commutes with finite direct sums, transforms strict epimorphisms into epimorphisms, and commutes with
passage to the quotient by a finite group of automorphisms.

**(G 6)** Let $u: X \to Y$ be a morphism in $\mathcal{C}$ such that $F(u)$ is an isomorphism. Then $u$ is an
isomorphism.

Our aim is to construct a topological group $\pi$, a projective limit of finite groups, and an equivalence of the
category $\mathcal{C}$ with the category $\mathcal{C}(\pi)$ **of finite sets on which** $\pi$ **operates continuously**,
i.e. so that the stabilizer of a point is an open subgroup, or equivalently so that there exists a discrete quotient
group already operating on the set in question. The equivalence constructed will transform the given functor $F$ into
the evident inclusion functor from $\mathcal{C}(\pi)$ into the category of finite sets. Note at once that the category
$\mathcal{C}(\pi)$ constructed from a topological group $\pi$, and the preceding inclusion functor, do satisfy
conditions (G 1) to (G 6).

We proceed in several steps.

1. Let $u: X \to Y$ be in $\mathcal{C}$. In order that $u$ be a monomorphism, it is necessary and sufficient that $F(u)$
   be one. This uses (G 1), (G 4), (G 6).

Indeed, to say that $u$ is a monomorphism means that the projection $pr_{1}: X \times_{Y} X \to X$ is an isomorphism.

1. Every object $X$ of $\mathcal{C}$ is artinian.

Indeed, if $X' \to X'' \to X$ are monomorphisms such that $F(X')$ and $F(X'')$ have the same image in $F(X)$, then by
(a) $F(X') \to F(X'')$ is an isomorphism, hence $X' \to X''$ is an isomorphism by (G 6).

1. The functor $F$ is **strictly pro-representable**; cf. Grothendieck, _Technique de descente et théorèmes d'existence
   en Géométrie Algébrique_, II, Séminaire Bourbaki 195, February 1960.

Indeed, by the cited place, Proposition V.3.1, this follows from (b) and (G 4). We may therefore find a projective
system over a filtered ordered set $I$,

$$
P = (P_{i})_{i\in I},
$$

in $\mathcal{C}$, regarded as a pro-object of $\mathcal{C}$, and a functorial isomorphism

```text
F(X) = Hom_{Pro(𝒞)}(P,X) = colim_i Hom_𝒞(P_i,X).
```

<!-- label: eq:V.4.* -->

This isomorphism is realized by an element

```text
φ ∈ lim_i F(P_i) = F(P).
```

One may moreover suppose that the transition homomorphisms $\phi_{ji}: P_{i} \to P_{j}$, for $i \geq j$, are
**epimorphisms**, and that **every epimorphism** $P_{i} \to P'$ is equivalent to an epimorphism $P_{i} \to P_{j}$ for
suitable $j \leq i$. This determines the projective system $P$ in an essentially unique way.

An object $X \in \mathcal{C}$ is called **connected** if it is not isomorphic to the sum of two objects of $\mathcal{C}$
not isomorphic to the initial object $\emptyset_{\mathcal{C}}$.

1. The $P_{i}$ are connected and not isomorphic to $\emptyset_{\mathcal{C}}$.

If $X$ is a left unit, then $F(X) = \emptyset$ by (G 5), applied to the direct sum of an empty family, and conversely by
(G 6). Thus if $X'$ is an object of $\mathcal{C}$ that is not a left unit, i.e. such that $F(X') \neq \emptyset$, there
is no morphism from $X'$ to $X$. Hence if some $P_{i}$ is a left unit, then $i$ is a greatest element of the filtered
ordered index set $I$, and formula $V.4.*$ would mean $F(X) = \operatorname{Hom}(P_{i},X)$, a one-element set for every
$X$; this is absurd since $F(\emptyset_{\mathcal{C}}) = \emptyset$. Thus the $P_{i}$ are not isomorphic to
$\emptyset_{\mathcal{C}}$.

Suppose $P_{i} = A \amalg B$. By (G 5), $F(P_{i}) = F(A) \amalg F(B)$. In particular the element $a_{i}$ of $F(P_{i})$,
corresponding by $V.4.*$ to the identity homomorphism $P_{i} \to P_{i}$, lies in $F(A) \amalg F(B)$, for instance in
$F(A)$. This means that there exists $j \geq i$ such that $\phi_{ij}: P_{j} \to P_{i}$ factors as
$P_{j} \to A \to P_{i} = A \amalg B$, where the second arrow is canonical. Thus $F(P_{j}) \to F(P_{i})$ factors as
$F(P_{j}) \to F(A) \to F(P_{i}) = F(A) \amalg F(B)$; since $F(P_{j}) \to F(P_{i})$ is surjective by (G 5), it follows
that $F(B) = \emptyset$, hence $B$ is isomorphic to $\emptyset_{\mathcal{C}}$.

1. Every morphism $u: X \to Y$ in $\mathcal{C}$, with $X$ not isomorphic to $\emptyset_{\mathcal{C}}$ and $Y$ connected,
   is a strict epimorphism. Every endomorphism of a connected object is an automorphism.

Consider the factorization (G 3) of $u$. Since $X \neq \emptyset_{\mathcal{C}}$, by (G 6) $F(X) \neq \emptyset$, hence
$F(Y') \neq \emptyset$, and therefore $Y' \neq \emptyset_{\mathcal{C}}$. Since $Y$ is connected, $Y'$ identifies with
$Y$, so $u$ is a strict epimorphism. Suppose $u$ is an endomorphism of the connected object $X$; we prove it is an
automorphism. We may suppose $X$ not isomorphic to $\emptyset_{\mathcal{C}}$, hence $u$ is a strict epimorphism by what
precedes. Thus $F(u)$ is an epimorphism by (G 5), and since $F(X)$ is a finite set, $F(u)$ is bijective. Therefore $u$
is an automorphism by (G 6).

In particular, **every endomorphism of a $P_{i}$ is an automorphism**.

1. The following conditions on a $P_{i}$ are equivalent:

1. The natural injective map $\operatorname{Hom}(P_{i},P_{i}) \to \operatorname{Hom}(P,P_{i}) \simeq F(P_{i})$ is also
   surjective; i.e. for every $u: P \to P_{i}$ there exists $v: P_{i} \to P_{i}$ such that $u = v \phi_{i}$, where
   $\phi_{i}$ is the canonical homomorphism $P \to P_{i}$.

1. The group $\operatorname{Aut}(P_{i})$ operates transitively on $F(P_{i})$.

1. The group $\operatorname{Aut}(P_{i})$ operates simply transitively on $F(P_{i})$.

Indeed, identifying $\operatorname{Hom}(P,P_{i})$ with $F(P_{i})$, the map considered in (i) is just
$v \mapsto F(v)(\phi_{i})$. The equivalence of the three conditions then comes from the fact that
$\operatorname{Hom}(P_{i},P_{i}) = \operatorname{Aut}(P_{i})$ and that the preceding map is already injective.

A $P_{i}$ satisfying the equivalent conditions (i), (ii), (iii) of (f) is called **Galois**.

1. For every $X$ in $\mathcal{C}$, there exists a Galois $P_{i}$ such that every $u \in \operatorname{Hom}(P,X)$ factors
   as $P --\phi_{i}\to P_{i} \to X$.

Let $J = \operatorname{Hom}(P,X) = F(X)$. This is a finite set, so there exists $P_{j}$ such that every $u: P \to X$
factors as $P \to P_{j} \to X$, or equivalently such that the natural morphism

```text
P → X^J,     J = Hom(P,X),
```

factors as

```text
P --φ_j→ P_j → X^J.
```

By (G 3), the morphism $P_{j} \to X^{J}$ factors as a product of a monomorphism and a strict epimorphism, which may be
taken in the form $\phi_{ij}: P_{j} \to P_{i}$. We are therefore reduced to proving that $P_{i}$ is Galois. Let $k$ be
an index $\geq j$ such that every morphism $P \to P_{i}$ factors through $P --\phi_{k}\to P_{k} \to P_{i}$. Note that
the natural morphism $P_{k} \to X^{J}$ still factors as the composite

```text
P_k --φ_{ik}→ P_i --U→ X^J,
```

where the first arrow is a strict epimorphism by (e), and the second a monomorphism. We want to prove that for a given
morphism $\psi: P_{k} \to P_{i}$, there exists an endomorphism $v$ of $P_{i}$ such that $\psi = v \phi_{ik}$. For every
$u \in \operatorname{Hom}(P_{i},X)$, consider $u\psi \in \operatorname{Hom}(P_{k},X)$. It is therefore of the form
$u' \phi_{ik}$, with $u' \in \operatorname{Hom}(P_{i},X)$ uniquely determined. The map $u \mapsto u'$ from $J$ to $J$
thus defined by $\psi$ is injective, since $\psi$ is an epimorphism by (e); it is therefore bijective, since $J$ is
finite. The bijective map $u \mapsto u'$ from $J$ to $J$ therefore defines an isomorphism $\alpha: X^{J} \to X^{J}$
making the diagram

```text
P_k --φ_{ik}→ P_i --U→ X^J
 |                         | α ≃
 =                         v
P_k ---ψ--→ P_i --U→ X^J
```

commutative. By the uniqueness properties of factoring a morphism as a product of a monomorphism and a strict
epimorphism, it follows, since $\psi$ is also a strict epimorphism by (e), that one can find a morphism
$v: P_{i} \to P_{i}$ making the diagram commute, as required.

It follows in particular that **the Galois $P_{i}$ form a cofinal system in the system of the $P_{j}$**. Therefore,
since for a Galois object $P_{i}$ one has

```text
Hom(P,P_i) = Hom(P_i,P_i) = Aut(P_i),
```

passing to the limit gives

```text
Hom(P,P) = lim_i Hom(P,P_i) = lim_i Hom(P_i,P_i) = lim_i Aut(P_i),
```

where the projective limit is taken over the Galois $P_{i}$. Moreover, under the identification
$\operatorname{Hom}(P,P_{i}) = F(P_{i})$, and taking into account that $F$ transforms epimorphisms into epimorphisms,
one sees that the transition homomorphisms in the preceding projective system are surjective. We conclude from all this:

1. One has

```text
Hom(P,P) = Aut(P) = lim_i F(P_i) = lim_i Aut(P_i),
```

where the projective limit is taken over the Galois $P_{i}$.

In particular, $\operatorname{Aut}(P)$ appears as the projective limit of a projective system of finite groups, with
surjective transition homomorphisms; we equip it with the projective-limit topology from the discrete topologies. **We
denote by $\pi$ and call the fundamental group** of $\mathcal{C}$ equipped with $F$ **the group opposite to**
$\operatorname{Aut}(P)$. This group therefore operates **on the right** on $P$; it is the projective limit of finite
groups $\pi_{i}$ operating on the right on the Galois $P_{i}$, where $\pi_{i}$ is the group opposite to
$\operatorname{Aut}(P_{i})$.

Taking the functorial isomorphism

$$
F(X) = \operatorname{Hom}(P,X)
$$

and the definition of $\pi$ into account, one sees that $\pi$ operates **on the left** on $F(X)$, and moreover
continuously by (g), since with the notation of (g), it is in fact $\pi_{i}$ that operates on $F(X)$. It is trivial that
for every morphism $u: X \to Y$ in $\mathcal{C}$, the morphism $F(u): F(X) \to F(Y)$ is compatible with the operations
of $\pi$. **Thus from now on one may regard** $F$ **as a covariant functor**

$$
F: \mathcal{C} \to \mathcal{C}(\pi),
$$

where $\mathcal{C}(\pi)$ is the category of finite sets on which $\pi$ operates on the left continuously.

We now define a functor in the opposite direction:

$$
G: \mathcal{C} \leftarrow \mathcal{C}(\pi)
$$

by the formula

```text
G(E) = P ×_π E,
```

where $P \times_{\pi} E$ is defined as the solution of the universal problem summarized by

```text
Hom_𝒞(P ×_π E, X) ≃ Hom_π(E, Hom(P,X)).
```

In the second member $\operatorname{Hom}(P,X) = F(X)$ is regarded as a set on which $\pi$ operates on the left. One must
prove the existence of the object $P \times_{\pi} E$.

1. Let $Q$ be an object of $\mathcal{C}$ on which a finite group $G$ operates on the right, and let $E$ be a finite set
   on which $G$ operates on the left. Then $Q \times_{G} E$ exists, and the canonical map

```text
F(Q) ×_G E → F(Q ×_G E)
```

is an isomorphism.

Since finite direct sums exist in $\mathcal{C}$ by (G 2), and $F$ commutes with them by (G 5), one is immediately
reduced to the case where $G$ operates transitively on $E$; if the $E_{j}$ are the orbits of $G$ in $E$, one will have

```text
Q ×_G E = ⨿_j Q ×_G E_j.
```

Let $a \in E$, and let $H$ be its stabilizer. One sees at once from the definition that $Q \times_{G} E$ identifies with
$Q/H$. Hence existence follows from (G 2), and the commutation property for $F$ from (G 5).

1. Let $E$ be an object of $\mathcal{C}(\pi)$, and let $P_{i}$ be Galois such that $\pi_{i}$ already operates on $E$.
   Then $P_{i} \times_{\pi_{i}} E$ exists and there is a canonical isomorphism

```text
E → F(P_i ×_{π_i} E).
```

If $j \geq i$ is such that $P_{j}$ is Galois, then the canonical homomorphism
$P_{j} \times_{\pi_{j}} E \to P_{i} \times_{\pi_{i}} E$ is an isomorphism.

The first assertion is a special case of (i), taking into account that $\pi_{i}$ operates simply transitively on
$F(P_{i})$, which is equipped with a marked point $\phi_{i}$, whence an isomorphism
$F(P_{i}) \times_{\pi_{i}} E \simeq E$. For the second assertion, use for example (G 6).

For every $j$, let $\mathcal{C}_{j}$ be the full subcategory of $\mathcal{C}$ formed by the $X$ such that
$\operatorname{Hom}(P_{j},X) \to \operatorname{Hom}(P,X) \simeq F(X)$ is bijective. We know by (g) that $\mathcal{C}$
**is the filtered union of the** $\mathcal{C}_{j}$. Thus for $X \in \mathcal{C}_{j}$ one has

```text
Hom_π(E,Hom(P,X))
  ≃ Hom_π(E,Hom(P_j,X))
  ≃ Hom_{π_j}(E,Hom(P_j,X))
  ≃ Hom(P_j ×_{π_j} E, X).
```

Taking the last assertion in (j) into account, one finds an isomorphism, functorial in the object $X$ of
$\mathcal{C}_{j}$,

```text
Hom_π(E,Hom(P,X)) ≃ Hom(P_i ×_{π_i} E, X).
```

Since this is true for every $j$, and since these functorial isomorphisms for varying $j$ induce one another, we
conclude:

1. Under the conditions of (j), the composite of the canonical morphisms

```text
E → Hom(P_i, P_i ×_{π_i} E) → Hom(P, P_i ×_{π_i} E)
```

makes $P_{i} \times_{\pi_{i}} E$ a solution of the universal problem defining $P \times_{\pi} E$; i.e. the latter exists
and there is an isomorphism

```text
P ×_π E → P_i ×_{π_i} E.
```

This completes the construction of the functor $G(E)$. On the other hand, there is a functorial homomorphism

$$
\alpha: id_{\mathcal{C}(\pi)} \to FG,
$$

i.e. a homomorphism functorial in the object $E$ of $\mathcal{C}(\pi)$,

```text
α(E): E → FG(E) = F(P ×_π E),
```

namely the composite of the canonical morphisms

```text
E → F(P) ×_π E → F(P ×_π E),
```

where the first comes from the marked point $\phi \in F(P)$. Combining (j) and (k), one finds:

1. The homomorphism $\alpha$ is an isomorphism.

One similarly defines a functorial homomorphism

$$
\beta: GF \to id_{\mathcal{C}},
$$

i.e. a homomorphism functorial in the object $X$ of $\mathcal{C}$,

```text
β(X): P ×_π F(X) → X,
```

as associated with the $\pi$-homomorphism

$$
F(X) \to \operatorname{Hom}(P,X)
$$

inverse to the canonical isomorphism $\operatorname{Hom}(P,X) \to F(X)$.

1. The composites

```text
F(X) --α(F(X))→ FGF(X) --F(β(X))→ F(X),
G(E) --G(α(E))→ GFG(E) --β(G(E))→ G(E)
```

are the identity isomorphisms.

The donkey trots.

Taking (l) into account, it follows:

1. The homomorphism $\beta$ is an isomorphism.

We have thus obtained the promised result:

**Theorem.**

<!-- label: V.4.1 -->

Let $\mathcal{C}$ be a category satisfying conditions **(G 1)**, **(G 2)**, **(G 3)** from the beginning of this number,
and let $F$ be a covariant functor from $\mathcal{C}$ to the category of finite sets satisfying **(G 4)**, **(G 5)**,
and **(G 6)**. Then the preceding canonical constructions define quasi-inverse equivalences of categories
$F: \mathcal{C} \to \mathcal{C}(\pi)$ and $G: \mathcal{C}(\pi) \to \mathcal{C}$. More precisely, there exists a
pro-object $P$ of $\mathcal{C}$ and a functorial isomorphism $F(X) \leftarrow \operatorname{Hom}(P,X)$; $\pi$ is the
group opposite to the automorphism group of $P$, topologized suitably, so that $\pi$ operates continuously on the sets
$\operatorname{Hom}(P,X) \simeq F(X)$. Finally, $G$ is given by $G(E) \simeq P \times_{\pi} E$.

**Remarks.**

<!-- label: V.4.2 -->

The statement of conditions (G 1) to (G 6) becomes simpler and more agreeable if one replaces (G 2) and (G 5),
respectively, by:

**(G′ 2)** Finite inductive limits exist in $\mathcal{C}$.

**(G′ 5)** The functor $F$ is right exact, i.e. commutes with finite inductive limits.

These conditions appear stronger than (G 2) and (G 5), but it follows at once from the structure theorem V.4.1 that they
are implied by (G 1) to (G 6). Note, however, that in the cases that will interest us, verifying (G 2) and (G 5) seems
effectively simpler than verifying (G′ 2) and (G′ 5). I do not know whether, in condition (G 3), the fact that $u''$ is
an isomorphism onto a direct summand of $Y$ could be omitted.

## 5. Galois Categories

<!-- label: V.5 -->

<!-- original page 127 -->

**Definition.**

<!-- label: V.5.1 -->

A **Galois category** is a category $\mathcal{C}$ equivalent to a category $\mathcal{C}(\pi)$, where $\pi$ is a compact
group, a projective limit of finite groups, i.e. totally disconnected.

For the definition of $\mathcal{C}(\pi)$, cf. the beginning of V.4. By Theorem V.4.1, $\mathcal{C}$ is Galois if and
only if it satisfies conditions (G 1) to (G 3), and there exists a functor $F$ from $\mathcal{C}$ to the category of
finite sets satisfying conditions (G 4) to (G 6), i.e. which is **exact** and **conservative**, in general terminology.
Such a functor will be called a **fundamental functor** of the Galois category $\mathcal{C}$;[^v-5-1-1] it is
pro-representable by a pro-object that we denote `P_F`. A pro-object $P$ such that the associated functor $F$ is
fundamental is called a **fundamental pro-object**.

In this way, the category of fundamental functors on $\mathcal{C}$ is anti-equivalent to the category of fundamental
pro-objects. If $F$ and $P$ correspond, the group $\operatorname{Aut} F$ is therefore isomorphic to the opposite of the
group $\operatorname{Aut} P$; hence the group denoted $\pi$ in the preceding number is none other than
$\operatorname{Aut} P$. Recall that in the preceding number, starting from a **given** fundamental functor $F$, we
constructed an equivalence of $\mathcal{C}$ with $\mathcal{C}(\pi)$, where $\pi = \operatorname{Aut}(F)$, that
transforms $F$ into the canonical functor from $\mathcal{C}(\pi)$ to the category of finite sets. In the typical case
$\mathcal{C} = \mathcal{C}(\pi)$, with $F$ the canonical functor, the fundamental pro-object associated with $F$ is
nothing other than the projective system of the discrete quotients $\pi_{i}$ of $\pi$.

It may be useful to spell out the category of pro-objects of $\mathcal{C}(\pi)$. One finds:

**Proposition.**

<!-- label: V.5.2 -->

The category $Pro-\mathcal{C}(\pi)$ is canonically equivalent to the category $\mathcal{C}'(\pi)$ of spaces, with
topological group $\pi$ of operators, which are compact and totally disconnected.

Since the latter contains $\mathcal{C}(\pi)$ as a full subcategory, corresponding to compact discrete spaces with
operators, and since projective limits exist in it, we have in any case a canonical functor

$$
g: Pro-\mathcal{C}(\pi) \to \mathcal{C}'(\pi),
$$

which sends the projective system $Q = (Q_{i})$ to the object $X = \lim_{i} Q_{i}$ of $\mathcal{C}'(\pi)$. To define a
functor in the opposite direction, it is enough to define a contravariant functor from $\mathcal{C}'(\pi)$ to the
category of left-exact functors $\mathcal{C} \to Set$; for $X \in \mathcal{C}'(\pi)$, take the functor

$$
h(X)(E) = \operatorname{Hom}(X,E),
$$

<!-- original page 128 -->

where `Hom` is taken in $\mathcal{C}'(\pi)$. It is immediate from the definitions that $h$ and $g$ are adjoint to one
another, and that `hg` is canonically isomorphic to the identity functor of $Pro-\mathcal{C}(\pi)$. It remains, in order
to prove that $g$ and $h$ are quasi-inverse to one another, to show that every object of $\mathcal{C}'(\pi)$ is
isomorphic to an object of the form $g(Q)$, with $Q \in Pro-\mathcal{C}(\pi)$; in other words: **every space $X$ with
topological group $\pi$ of operators, compact and totally disconnected, is isomorphic to a projective limit of finite
discrete spaces with operators**.

Since $X$ is the projective limit of its finite discrete quotients, as a topological space without operators, we are
reduced to showing that, among these quotients, there is a cofinal system invariant under $\pi$. For this it is enough
to show that, for such a quotient $X'$, the set of transforms of this quotient by the operations of $\pi$ is finite; one
then takes the supremum of these transforms, which will be an invariant quotient dominating $X'$. Equivalently, there is
an open invariant subgroup $\pi'$ of $\pi$ whose elements leave $X'$ fixed. Now $X'$ corresponds to a finite partition
of $X$ into open sets `Xᵢ`. By continuity and compactness of $\pi$, there exists a neighborhood $V$ of the identity
element of $\pi$ such that $s \in V$ implies $s \cdot X_{i} \subset X_{i}$ for every $i$, and hence $s$ leaves $X'$
fixed. But the open invariant subgroups of $\pi$ are known to form a fundamental system of neighborhoods of the identity
element. This finishes the proof.

Let us note that one sees still more simply that the category $Ind-\mathcal{C}(\pi)$ is canonically equivalent to the
category of sets on which $\pi$ operates continuously. We shall not need this here.

**Proposition.**

<!-- label: V.5.3 -->

Let $\mathcal{C}$ be a Galois category, $F$ a fundamental functor on $\mathcal{C}$, and $P = (P_{i})$ the associated
pro-object, normalized in the usual way. Let $X \in \mathcal{C}$. Then $X$ is connected if and only if $\pi$ operates
transitively on $E = F(X)$.

This reduces to the typical case $\mathcal{C} = \mathcal{C}(\pi)$, with $F$ the canonical functor, where it is trivial.

**Corollary.**

<!-- label: V.5.4 -->

For $X$, the following conditions are equivalent:

1. $X$ is connected and `X ≄ ∅_𝒞`.
1. The group $\pi$ is transitive on $E = F(X)$, and $F(X) \neq \emptyset$.
1. $X$ is isomorphic to some `Pᵢ`.

<!-- original page 129 -->

The equivalence of (1) and (3) also follows already easily from V.4, e).

**Proposition.**

<!-- label: V.5.5 -->

Let $Q = (Q_{i})_{i}\in I$ be a pro-object of $\mathcal{C}$, normalized in the usual way, and let $G$ be the
corresponding functor $G(X) = \operatorname{Hom}(Q,X)$ from $\mathcal{C}$ to `Set`. The following conditions are
equivalent:

1. $G$ commutes with finite direct sums.
1. $G$ commutes with the sum of two objects.
1. The `Qᵢ` are connected and `Qᵢ ≄ ∅_𝒞`.
1. $Q$ is isomorphic to $\pi/H$, where $H$ is a closed subgroup of $\pi$.
1. The functor $G$ is isomorphic to the functor $E \mapsto E^{H}$, the set of $H$-invariants, defined by a closed
   subgroup $H$ of $\pi$.

N.B. In the statement of (4) and (5), one assumes that a fundamental functor has been chosen, allowing $\mathcal{C}$ to
be identified with the category $\mathcal{C}(\pi)$.

**Proof.** We may suppose $\mathcal{C} = \mathcal{C}(\pi)$. The implication (1) ⇒ (2) is trivial, and (2) ⇒ (3) is
proved as property d) of V.4. Let us prove (3) ⇒ (4). Indeed, $\lim_{i} Q_{i}$ is nonempty as a projective limit of
nonempty finite sets. Let $a$ be a point of $\lim_{i} Q_{i}$; it defines a homomorphism of spaces with operators

$$
\pi \to Q
$$

which is **surjective**, since for every $i$ the composite $\pi \to Q \to Q_{i}$ is surjective, because $\pi$ is
transitive on `Qᵢ` by V.5.3. If $H$ is the stabilizer subgroup of $a$, one obtains an isomorphism $\pi/H \simeq Q$. The
implications (4) ⇒ (5) and (5) ⇒ (1) are again trivial.

**Proposition.**

<!-- label: V.5.6 -->

Let $\mathcal{C}$ be a Galois category, $P$ a fundamental pro-object of $\mathcal{C}$, and $F$ the associated
fundamental functor. Let $P' = (P'_{i})_{i}\in I$ be a pro-object of $\mathcal{C}$, put in normal form, and let $F'$ be
the associated functor $F'(X) = \operatorname{Hom}(P',X)$ from $\mathcal{C}$ to `Set`. The following conditions are
equivalent:

1. $P' \simeq P$, or equivalently $F' \simeq F$.
1. $P'$ is fundamental, or equivalently $F'$ is fundamental.
1. $F'$ transforms a sum of two objects into a sum, and `X ≄ ∅_𝒞` implies $F(X) \neq \emptyset$.
1. The objects of $\mathcal{C}$ that are connected and $\neq \emptyset_{\mathcal{C}}$ are exactly the objects isomorphic
   to some $P'_{i}$.

<!-- original page 130 -->

We have trivially (1) ⇒ (3) and (1) ⇒ (2); furthermore (2) ⇒ (4) by V.5.4, applied to $P'$ instead of $P$. Moreover, (3)
or (4) implies, by V.5.5, that $P'$ is of the form $\pi/H$, where $H$ is a closed subgroup of $\pi$. In case (3), for
every open invariant subgroup $\pi'$ of $\pi$ there exists a $\pi$-homomorphism $P' = \pi/H \to \pi/\pi'$, hence
$H \subset \pi'$; thus $H = (0)$, and consequently (1), as required.

**Corollary.**

<!-- label: V.5.7 -->

Let $\mathcal{C}$ be a Galois category. The fundamental pro-objects are isomorphic; the fundamental functors are
isomorphic.

In other words, **the category of fundamental functors is a connected groupoid $\Gamma$**, which one may call the
**fundamental groupoid** of the Galois category $\mathcal{C}$. If $\mathcal{C} = \mathcal{C}(\pi)$, the automorphism
group of an object of the fundamental groupoid is isomorphic to $\pi$, this isomorphism being well determined up to
inner automorphism. Here a **groupoid** means a category in which all morphisms are isomorphisms, and a **connected**
groupoid means a groupoid all of whose objects are isomorphic. The fundamental pro-objects of $\mathcal{C}$ form a
connected groupoid equivalent to the **opposite** of the fundamental groupoid.

If $F, F'$ are two fundamental functors, associated with fundamental pro-objects $P, P'$, then
$\operatorname{Hom}(F,F') = Isom(F,F')$ is sometimes denoted $\pi_{F',F}$ and plays the role of a “set of **path
classes** from $F$ to $F'$”. In particular, $\pi_{F,F} = \pi_{F}$ is nothing other than the **fundamental group of
$\mathcal{C}$** at $F$ constructed in the preceding number. As for the pro-object $P$ associated with $F$, it plays the
role of a **universal covering at $F$** of the final object $e_{\mathcal{C}}$ of $\mathcal{C}$.

It can be convenient to have a description of $\mathcal{C}$, up to equivalence, in terms of its fundamental groupoid
$\Gamma$, without going through the choice of one particular object $F$ of $\Gamma$. To every object $X$ of
$\mathcal{C}$ there is associated the functor `E_X` on the fundamental groupoid, defined by

$$
E_{X}(F) = F(X),
$$

with values in `Set`. Such a functor is known in topology under the name “local system” on the groupoid.
$F(X) = E_{X}(F)$ may be called the **fiber** of $X$ at $F$, and the functor `E_X` the fiber-functor associated with
$X$. The functor `E_X` has the following property:

<!-- original page 131 -->

**for every $F$, $E_{X}(F)$ is a finite set on which the topological group $\pi_{F} = \operatorname{Aut}(F)$ operates
continuously**.

For a given covariant functor $\xi$ from the fundamental groupoid to `Set`, the preceding condition is moreover
equivalent to the same condition for **one** arbitrary fixed $F$. This being so:

**Proposition.**

<!-- label: V.5.8 -->

The functor $X \mapsto E_{X}$ is an equivalence of the category $\mathcal{C}$ with the category of covariant functors
from the fundamental groupoid $\Gamma$ of $\mathcal{C}$ to `Set` that satisfy the condition displayed above.

Indeed, let $F_{0}$ be an object of the fundamental groupoid, and let $\pi_{0} = \operatorname{Aut}(F_{0})$. Then the
functor $\xi \mapsto \xi(F_{0})$ is an equivalence from the second category considered in V.5.8 to the category
$\mathcal{C}(\pi_{0})$, as one sees at once. On the other hand, the composite of this functor with $X \mapsto E_{X}$ is
the natural equivalence $\mathcal{C} \to \mathcal{C}(\pi_{0})$. It follows that the functor $X \mapsto E_{X}$ itself is
an equivalence.

**Corollary.**

<!-- label: V.5.9 -->

The category $Pro-\mathcal{C}$ is canonically equivalent to the category of covariant functors $\xi$ from the
fundamental groupoid $\Gamma$ to the category of topological spaces satisfying the following condition: for every object
$F$ of $\Gamma$, $\xi(F)$ is a compact totally disconnected space with topological group $\pi_{F}$ of operators.

Here again, to check this condition on $\xi$, it is enough to check it for **one** $F$. The proof is the same as for
V.5.8.

**Remark.**

<!-- label: V.5.10 -->

Let $(F_{s})_{s\in S}$ be a family of objects of the fundamental groupoid $\Gamma$. Put, for $s, s' \in S$,

$$
\operatorname{Hom}(s,s') = \operatorname{Hom}(F_{s},F_{s}'),
$$

so that $S$ itself becomes a connected groupoid, and the map $s \mapsto F_{s}$ becomes a fully faithful functor $f$ from
$S$ to $\Gamma$. Considering then the functor $X \mapsto E_{X} \circ f$ from $\mathcal{C}$ to the category of functors
$\operatorname{Hom}(S,Set)$, one obtains a variant of V.5.8, and V.5.9, with $\Gamma$ replaced by $S$. The statement so
obtained reduces to Theorem V.4.1 when $S$ is reduced to a point, and is none other than V.5.8 itself if $S$ is the set
of objects of $\Gamma$.

We are going to use V.5.9 to define a canonical pro-object of $\mathcal{C}$. For this, we consider the functor from
$\Gamma$ to the category of topological spaces, indeed of topological groups,

<!-- original page 132 -->

```text
f: F ↦ Aut(F) = π_F.
```

This functor satisfies the condition considered in V.5.8: the space with operators $f(F)$, under $\pi_{F}$, is none
other than $\pi_{F}$ considered as a space with operators under itself by inner automorphisms. Thus the functor $f$
corresponds to a pro-object of $\mathcal{C}$, determined up to unique isomorphism, which is even a pro-group of
$\mathcal{C}$ and is called the **fundamental pro-group of $\mathcal{C}$**, playing the role of a local system of
fundamental groups. It is therefore a pro-group $\Pi$ of $\mathcal{C}$ defined by the condition that one have an
isomorphism functorial in $F$:

$$
F(\Pi) \simeq \pi_{F}.
$$

If $X$ is any pro-object of $\mathcal{C}$, one has a canonical morphism

$$
\Pi \times X \to X
$$

which makes $X$ an object with a left group of operators $\Pi$ in $Pro-\mathcal{C}$. For this it is enough to note that,
for variable $F$, one has a canonical map

$$
\Pi(F) \times X(F) \to X(F),
$$

i.e.

```text
Aut(F) × E_X(F) → E_X(F),    or    π_F × F(X) → F(X),
```

which is functorial in $F$. It is also functorial in $X$, so for every morphism $X \to Y$ of pro-objects, the
corresponding diagram

$$
\Pi \times X  \to  X
  \downarrow       \downarrow
\Pi \times Y  \to  Y
$$

is commutative.

**Remark.**

<!-- label: V.5.11 -->

One should be careful not to confuse a fundamental pro-object $P$, which is not endowed with a group structure and is
connected, with the fundamental pro-group, which is a pro-**group** and in general is not connected. More precisely,
$\Pi$ is connected if and only if $\pi_{F}$, operating on itself by inner automorphisms, is transitive, i.e. if $\pi$ is
reduced to the identity element, or again if $\mathcal{C}$ is equivalent to the category of finite sets. Another
essential difference is that $\Pi$ is determined up to unique isomorphism, while $P$ is determined only up to non-unique
isomorphism.

<!-- original page 133 -->

Let $E$ be a finite set, and consider the constant functor on the groupoid $\Gamma$ with value $E$. By V.5.8, it defines
an object of $\mathcal{C}$, denoted $E_{\mathcal{C}}$, which can also be interpreted as the sum of $E$ copies of the
final object $e_{\mathcal{C}}$ of $\mathcal{C}$. One may regard $E_{\mathcal{C}}$ as a functor in $E$, from the category
of finite sets to the category $\mathcal{C}$, and this functor is **exact**; hence it transforms finite groups into
$\mathcal{C}$-groups, etc. Thus if $X$ is an object of $\mathcal{C}$ on which the finite group $G$ operates on the
right, one sees that $X$ may be regarded as an object of $\mathcal{C}$ having a right $\mathcal{C}$-group of operators
$G_{\mathcal{C}}$.

By extension of the general terminology concerning objects with $\mathcal{C}$-groups of operators, we shall therefore
say that $X$ is **formally principal homogeneous** under $G$ if $X$ is formally principal homogeneous under
$G_{\mathcal{C}}$, i.e. if the canonical morphism

```text
X × G_𝒞 → X × X
```

deduced from the right operation of $G_{\mathcal{C}}$ on $X$ is an isomorphism. We say that $X$ is **principal
homogeneous** under $G$ if it is so under $G_{\mathcal{C}}$, i.e. if it is formal in the preceding sense and if,
moreover, the quotient $X/G = X/G_{\mathcal{C}}$ is $e_{\mathcal{C}}$.

If a fundamental functor is fixed, hence an equivalence of $\mathcal{C}$ with a category $\mathcal{C}(\pi)$, then $X$
corresponds to a set $E = F(X)$ on which $\pi$ operates continuously on the left. Making $G$ operate on $X$ on the right
then amounts to making $G$ operate on the set $E$ on the right, in such a way that the operations of $G$ commute with
those of $\pi$. One checks at once that $X$ is principal homogeneous under $G$ if and only if the set $E$ is a principal
homogeneous space under $G$, i.e. if and only if $G$ operates on it simply transitively. Moreover, $X$ is formally
principal homogeneous if and only if $E$ is principal homogeneous or empty.

Comparing with V.5.3, one sees that if $X$ is principal homogeneous under $G$ **and connected**, then the given
homomorphism from $G$ to the group opposite to $\operatorname{Aut}(X)$ is an **isomorphism**; and moreover, for an
object $X$ of $\mathcal{C}$ to be connected and principal homogeneous under the group opposite to
$\operatorname{Aut}(X)$, it is necessary and sufficient, with the notation of V.4, that it be isomorphic to a Galois
`Pᵢ`. In the typical case $\mathcal{C} = \mathcal{C}(\pi)$, this means that $X$ is isomorphic to a quotient of $\pi$ by
an invariant subgroup.

Suppose still that a fundamental functor $F$ is given. Then the data of an $X$ principal homogeneous under a finite
group $G$ operating on the right, together with a point $a \in F(X)$, is equivalent to the data of a homomorphism from
$\pi$ to the group $G$.

<!-- original page 134 -->

Indeed, to such a homomorphism one associates the set $E = G$, making $\pi$ operate on it on the left by means of the
given homomorphism $\pi \to G$ and the left translations of $G$, and making $G$ operate on it on the right by right
translation; the marked point $a$ of $E$ is the identity element of $G$. By what precedes, one thus obtains, in an
essentially unique way, every triple $(X,G,a)$ having the properties considered above, since a pointed set that is
principal homogeneous under a group $G$ is identified with that group. In this way, one has a direct geometric
interpretation of the functor $G \mapsto \operatorname{Hom}(\pi,G)$ from the category of finite groups to `Set`, a
functor which is pro-representable by $\pi$ and whose consideration would therefore give another construction of the
group $\pi$ associated with $F$.

## 6. Exact Functors from One Galois Category to Another

<!-- label: V.6 -->

**Proposition.**

<!-- label: V.6.1 -->

Let $\mathcal{C}, \mathcal{C}'$ be two Galois categories, $H: \mathcal{C} \to \mathcal{C}'$ a covariant functor, $F'$ a
fundamental functor on $\mathcal{C}'$, and $F = F' \circ H$. The following conditions are equivalent:

1. $H$ is **exact**, i.e. left exact and right exact.
1. $H$ is left exact, transforms finite sums into finite sums, and transforms epimorphisms into epimorphisms;
   equivalently, it transforms objects `≉ ∅_𝒞` into objects `≉ ∅_𝒞′`.
1. $F$ is a fundamental functor on $\mathcal{C}$.

The implication (1) ⇒ (2) is a general fact about categories. Moreover, the first form given for (2) implies the second:
if $X$ is an object of $\mathcal{C}$, then $X$ is `≉ ∅_𝒞` if and only if the morphism $X \to e_{\mathcal{C}}$ is an
epimorphism; one notes that $F$, being assumed left exact, transforms $e_{\mathcal{C}}$ into $e_{\mathcal{C}}'$. The
second form of (2) implies (3), because $F$, being left exact and hence pro-representable, falls under the criterion
V.5.6, (3). Finally, (3) implies (1), as follows from the fact that $F$ is exact and “conservative”, i.e. satisfies
axiom (G 6) of V.4.

Let $\Gamma$ be the fundamental groupoid of $\mathcal{C}$ and $\Gamma'$ that of $\mathcal{C}'$. Thus, if $H$ is exact,
then

$$
F' \mapsto F' \circ H
$$

is a functor from the groupoid $\Gamma'$ to the groupoid $\Gamma$, which we shall denote by `ᵗH`:

<!-- original page 135 -->

$$
{}^{t}H(F')(X) = F'(H(X)).
$$

This may also be written, with the notation $F(X) = E_{X}(F)$ introduced in V.6, as

$$
E_{H(X)}(F') = E_{X}({}^{t}H(F')).
$$

This last formula shows, taking V.5.8 or V.4.1 into account, that the exact functor $H$ is determined, up to unique
isomorphism, once the corresponding functor `ᵗH` is known. Fix an $F'$, and put $F = {}^{t}H(F')$. Then `ᵗH` defines a
homomorphism

```text
ᵗH: π_{F′} → π_F,    where F = ᵗH(F′) = F′ ∘ H.
```

Moreover, the formula above shows, taking V.5.8 into account, that this homomorphism has the following property: for
every finite set $E$ on which $\pi_{F}$ operates continuously, the group $\pi_{F'}$ also operates **continuously** by
means of the preceding homomorphism $\pi_{F'} \to \pi_{F}$. Applying this to the quotients of $\pi_{F}$ by its open
invariant subgroups, one sees that the preceding condition also says that the homomorphism under consideration is
continuous.

Conversely, suppose we are given an object $F$ of $\Gamma$, an object $F'$ of $\Gamma'$, and a continuous homomorphism

$$
u: \pi_{F'} \to \pi_{F}.
$$

To it there corresponds a functor from $\mathcal{C}(\pi)$ to $\mathcal{C}(\pi')$, manifestly exact; hence, by V.4.1,
there corresponds to it a functor $H$ from $\mathcal{C}$ to $\mathcal{C}'$ which is exact and such that
${}^{t}H: \pi_{F'} \to \pi_{F}$ is precisely $u$. One may also, instead of starting from a group homomorphism, start
from a **functor**

$$
U: \Gamma' \to \Gamma
$$

such that, for **every** $F' \in \Gamma'$, or for **one** $F' \in \Gamma'$, which comes to the same thing, the
corresponding homomorphism $\pi_{F'} \to \pi_{F}$ is continuous. Such a functor is isomorphic to a functor of the form
`ᵗH`, where $H: \mathcal{C} \to \mathcal{C}'$ is an exact functor determined up to unique isomorphism. Thus:

**Corollary.**

<!-- label: V.6.2 -->

For a functor $H: \mathcal{C} \to \mathcal{C}'$ of Galois categories to be exact, it is necessary and sufficient that
there exist equivalences $\mathcal{C}(\pi) \to \mathcal{C}$ and $\mathcal{C}' \to \mathcal{C}(\pi')$ that transform the
functor $H$ into the functor $\mathcal{C}(\pi) \to \mathcal{C}(\pi')$ associated with a homomorphism of topological
groups $\pi' \to \pi$.

<!-- original page 136 -->

**Corollary.**

<!-- label: V.6.3 -->

Let $\mathcal{C}, \mathcal{C}'$ be two Galois categories, and let $\Gamma, \Gamma'$ be their fundamental groupoids. Then
the category of exact functors from $\mathcal{C}$ to $\mathcal{C}'$ is equivalent to the category of functors
$U: \Gamma' \to \Gamma$ having the following property: for every $F'$ in $\Gamma'$, or for **one** $F'$ in $\Gamma'$,
which comes to the same thing, if $F = U(F')$, the homomorphism

```text
π_{F′} = Aut(F′) → π_F = Aut(F)
```

defined by $U$ is continuous.

Consider the fundamental pro-group $\Pi$ of $\mathcal{C}$. An exact functor $H$ transforms it into a pro-group $H(\Pi)$
of $\mathcal{C}'$. We are going to define a homomorphism

$$
\Pi' \to H(\Pi),
$$

where $\Pi'$ is the fundamental pro-group of $\mathcal{C}'$, by requiring that, for every object $F'$ of $\Gamma'$, the
corresponding homomorphism

```text
F′(Π′) = π_{F′} → F′(H(Π)) = π_F    where F = F′ ∘ H = ᵗH(F′)
```

be the natural homomorphism

$$
\operatorname{Aut}(F') \to \operatorname{Aut}(F' \circ H).
$$

Since the latter is functorial in $F'$, it indeed defines, by V.5.8, a homomorphism of pro-objects, and in fact of
pro-groups, of $\mathcal{C}'$. This homomorphism is said to be **associated** with the functor $H$.

Let now $H'$ be a second exact functor, from the Galois category $\mathcal{C}'$ to a Galois category $\mathcal{C}''$. It
is trivial that

$$
{}^{t}(H'H) = {}^{t}H {}^{t}H'.
$$

N.B. this is an identity of functors, and not merely a canonical isomorphism. There is an analogous transitivity
property for the associated homomorphisms of fundamental pro-groups.

We shall now interpret the properties of the exact functor $H$ in terms of the corresponding homomorphism

<!-- original page 137 -->

```text
u: π_{F′} → π_F,    where F = F′ ∘ H.
```

It is convenient to introduce the notion of a **pointed object** of the Galois category $\mathcal{C}$, endowed with its
fundamental functor $F$. By definition, this is an object $X$ of $\mathcal{C}$ together with an element $a$ of $F(X)$.
It is therefore interpreted as a finite set on which $\pi_{F}$ operates continuously on the left, together with a point
$a$. Thus the **connected** pointed objects of $\mathcal{C}$ are identified, by V.5.3, with the open subgroups of
$\pi_{F}$. If $U$ and $V$ are two such subgroups, corresponding to connected pointed objects $X$ and $Y$ of
$\mathcal{C}$, then there exists a pointed homomorphism from $X$ to $Y$ if and only if $U \subset V$, and that
homomorphism is then unique.

Of course the functor $H$ transforms pointed objects into pointed objects, since $F = F' \circ H$. On the other hand,
note that a closed subgroup of a group such as $\pi_{F}$ is the intersection of the open subgroups containing it;
consequently, if $M$ and $N$ are two closed subgroups, then $M \subset N$ if and only if every open subgroup that
contains $N$ also contains $M$. With these remarks, one easily proves the following results:

**Proposition.**

<!-- label: V.6.4 -->

Let $X$ be a connected pointed object of $\mathcal{C}$, associated with an open subgroup $U$ of $\pi_{F}$. In order that
$U$ contain $u(\pi_{F'})$, respectively the closed invariant subgroup generated by $u(\pi_{F'})$, it is necessary and
sufficient that $H(X)$ admit a pointed section, respectively be completely decomposed.

A **section**, understood as over the final object, of an object $X$ of a Galois category $\mathcal{C}$ is a morphism
from the final object $e_{\mathcal{C}}$ to $X$; this amounts to the data of an element $a$ of $F(X)$ invariant under
$\pi_{F}$. If $X$ is pointed, one says that one has a **pointed section** if it is compatible with the pointed
structures on $X$ and $e_{\mathcal{C}}$, i.e. if $a$ is precisely the marked object of $F(X)$. Such a section is
therefore unique, and exists if and only if the marked object of $F(X)$ is invariant under $\pi_{F}$. Finally, an object
of a Galois category is said to be **completely decomposed** if it is isomorphic to a sum of final objects, i.e. if
$\pi_{F}$ operates trivially on $F(X)$, a condition evidently stronger than the existence of a pointed section when $X$
is pointed. Proposition V.6.4 follows trivially from the preceding definitions and remarks.

**Corollary.**

<!-- label: V.6.5 -->

For $u$ to be trivial, it is necessary and sufficient that, for every object $X$ of $\mathcal{C}$, $H(X)$ be completely
decomposed.

<!-- original page 138 -->

**Proposition.**

<!-- label: V.6.6 -->

Let $X'$ be a connected pointed object of $\mathcal{C}'$, associated with an open subgroup $U'$ of $\pi_{F'}$. In order
that $U'$ contain `Ker u`, it is necessary and sufficient that there exist a connected pointed object $X$ of
$\mathcal{C}$ and a pointed homomorphism from the pointed connected component $X'_{0}$ of $H(X)$ to $X'$. Equivalently,
$X'$ must be isomorphic, as a pointed object, to a quotient of the neutral connected component of the inverse image of a
pointed object of $\mathcal{C}$. If $u$ is surjective, the preceding condition is also equivalent to the following: $X'$
is isomorphic to an $H(X)$, where $X$ is a pointed object of $\mathcal{C}$.

The **neutral connected component** of a pointed object $X$ of a Galois category $\mathcal{C}$ means the unique
connected pointed subobject of $X$. By V.5.3, it corresponds to the orbit under $\pi_{F}$ of the marked point of $F(X)$.
Since the fact that $U'$ contains `Ker u` does not depend on the chosen pointing of $X'$, another pointing merely
replacing $U$ by a subgroup conjugate to $U$, one sees:

**Corollary.**

<!-- label: V.6.7 -->

For $U'$ to contain `Ker u`, it is necessary and sufficient that there exist an object $X$ of $\mathcal{C}$, which may
be supposed connected, and a morphism from a connected component of $H(X)$ to $X'$. If $u$ is surjective, this also
means that $X'$ is isomorphic to an object of the form $H(X)$.

**Corollary.**

<!-- label: V.6.8 -->

For $u$ to be injective, it is necessary and sufficient that, for every object $X'$ of $\mathcal{C}'$, there exist an
object $X$ of $\mathcal{C}$ and a homomorphism from a connected component of $H(X)$ to $X'$.

**Proposition.**

<!-- label: V.6.9 -->

The following conditions are equivalent:

1. The homomorphism $u: \pi_{F'} \to \pi_{F}$ is surjective.
1. For every connected object $X$ of $\mathcal{C}$, $H(X)$ is connected.
1. The functor $H$ is fully faithful.

This last fact means that, for two objects `X, Y` of $\mathcal{C}$, the natural map

$$
\operatorname{Hom}(X,Y) \to \operatorname{Hom}(H(X),H(Y))
$$

is bijective.

**Corollary.**

<!-- label: V.6.10 -->

<!-- original page 139 -->

For $u$ to be an isomorphism, it is necessary and sufficient that $H$ be an equivalence of categories, or equivalently
that the following two conditions hold:

1. for every connected object $X$ of $\mathcal{C}$, $H(X)$ is connected;
1. every object of $\mathcal{C}'$ is isomorphic to an object of the form $H(X)$.

**Proposition.**

<!-- label: V.6.11 -->

Let $H: \mathcal{C} \to \mathcal{C}'$ and $H': \mathcal{C}' \to \mathcal{C}''$ be exact functors between Galois
categories, let $F''$ be a fundamental functor on $\mathcal{C}''$, put $F' = F''H'$ and $F = F'H$, and consider the
associated homomorphisms

```text
u′: π_{F″} → π_{F′},       u: π_{F′} → π_F.
```

In order that $Ker u \subset Im u'$, i.e. in order that $uu'$ be the trivial homomorphism, it is necessary and
sufficient that, for every object $X$ of $\mathcal{C}$, $H'(H(X))$ be completely decomposed. In order that
$Ker u \supset Im u'$, it is necessary and sufficient that, for every connected pointed object $X'$ of $\mathcal{C}'$
such that $H'(X')$ admits a pointed section, there exist an object $X$ of $\mathcal{C}$ and a homomorphism from a
connected component of $H(X)$ to $X'$.

The first assertion follows from the last assertion of V.6.4. The second follows from the conjunction of V.6.4 and
V.6.6.

**Remark.**

<!-- label: V.6.12 -->

It is not true in general, under the conditions of V.6.8, that $X'$ is isomorphic to an object of the form $H(X)$. One
can show that, in order that every connected object, and hence every object, of $\mathcal{C}'$ be isomorphic to an
object of the form $H(X)$, it is necessary and sufficient that $u$ be an isomorphism from $\pi_{F'}$ onto a **direct
factor** subgroup of $\pi_{F}$. In practice, however, one directly constructs a homomorphism $\pi_{F} \to \pi_{F'}$
inverse to $u$ on the right, by means of a suitable exact functor from $\mathcal{C}'$ to $\mathcal{C}$.

**Proposition.**

<!-- label: V.6.13 -->

Let $\mathcal{C}$ be a Galois category endowed with a fundamental functor $F$, let $S$ be a connected object of
$\mathcal{C}$, and let $\mathcal{C}'$ be the category of objects of $\mathcal{C}$ over $S$. Then $\mathcal{C}'$ is a
Galois category, and the functor $X \mapsto H(X) = X \times S$ from $\mathcal{C}$ to $\mathcal{C}'$ is exact. Let
$a \in F(S)$, and let $F'$ be the functor from $\mathcal{C}'$ to the category of finite sets defined by

```text
F′(X′) = inverse image of a under F(X′) → F(S).
```

Then one has an isomorphism $F \simeq F' \circ H$, and the corresponding homomorphism

$$
u: \pi_{F'} \to \pi_{F}
$$

<!-- original page 140 -->

is an isomorphism from $\pi_{F'}$ onto the open subgroup $U$ of $\pi_{F}$ stabilizing the marked element $a$ of $F(S)$.

The proof is left to the reader.

## 7. The Case of Preschemes

<!-- label: V.7 -->

Let $S$ be a locally noetherian and **connected** prescheme, and let

$$
a: \operatorname{Spec}(\Omega) \to S
$$

be a geometric point of $S$, with values in an algebraically closed field $\Omega$. We shall put

```text
𝒞 = category of étale coverings of S,
```

and, for an object $X$ of $\mathcal{C}$, i.e. an étale covering $X$ of $S$, we put

```text
F(X) = set of geometric points of X lying over a.
```

Thus $F$ becomes a functor on $\mathcal{C}$ with values in the category of finite sets. Properties (G 1) to (G 6) are
satisfied: (G 1) is contained in the sorites of I.4.6; (G 2) follows from V.3.4; (G 3) from V.3.5; (G 4) is trivial by
definition; (G 5) follows from V.3.5 and the beginning of V.2; finally, (G 6) is proved in V.3.7. We may therefore apply
the results of V.4, V.5, and V.6.

This makes it possible in particular to define a pro-object $P$ of $\mathcal{C}$ representing $F$, called the
**universal covering of $S$ at the point $a$**, and a topological group
$\pi = \operatorname{Aut}(F) = \operatorname{Aut}^{0}(P)$, called the **fundamental group of $S$ at $a$**, denoted
$\pi_{1}(S,a)$. The functor $F$ then defines an equivalence of the category $\mathcal{C}$ with the category of finite
sets on which $\pi = \pi_{1}(S,a)$ operates continuously. This equivalence therefore allows the usual operations of
finite projective and inductive limits on coverings, products, fiber products, sums, passage to the quotient, etc., to
be interpreted in terms of the analogous operations in $\mathcal{C}(\pi)$, i.e. in terms of the evident operations on
finite sets on which $\pi$ operates.

Moreover, since the topological connected components of an étale covering are also étale coverings, **an object $X$ of
$\mathcal{C}$ is connected in $\mathcal{C}$ if and only if it is topologically connected**. By V.5.3 this therefore
means that $\pi_{1}$ operates transitively on $F(X)$.

<!-- original page 141 -->

Note that, in order for an object $X$ of $\mathcal{C}$ to be faithfully flat and quasi-compact over $S$, since it is
already flat and quasi-compact over $S$, it is necessary and sufficient that $X \to S$ be surjective, i.e. be an
epimorphism in $\mathcal{C}$, or equivalently that $X \neq \emptyset$. It follows from criterion V.2.6 (iii) that $X$
**is a principal covering of $S$ with group $G$ if and only if it is a principal homogeneous space under $G$ in the
category $\mathcal{C}$**, in the sense defined in V.5.

If $a'$ is another geometric point of $S$, corresponding to an algebraically closed field $\Omega'$, which may be
different from $\Omega$ and may even have different characteristic, it defines a fiber functor $F' = F_{a'}$ from
$\mathcal{C}$ to the category of finite sets, again exact and hence isomorphic to $F = F_{a}$. Consequently the
fundamental groups $\pi_{1}(S;a)$, with $a$ variable, are isomorphic to one another.

If $\pi_{1}(S;a,a')$ denotes the set of isomorphisms, or what amounts to the same thing, the set of homomorphisms,
$F_{a} \to F_{a'}$ of the associated fiber functors, one obtains a **groupoid** whose set of objects is the set of
geometric points of $S$, the fundamental groups being the automorphism groups of the objects of this groupoid. The set
$\pi_{1}(S;a',a)$ may be called the **set of path classes from $a$ to $a'$**. These classes therefore compose in the
evident way.

Finally, one can define a pro-group $\Pi^{S}_{1}$ of $\mathcal{C}$, which may be called the **fundamental pro-group of
$S$** or the **local system of fundamental groups on $S$**, determined up to unique isomorphism by the condition that
one have an isomorphism, functorial in the geometric point $a$ of $S$,

$$
F_{a}(\Pi^{S}_{1}) = \pi_{1}(S;a)
$$

cf. Remark V.5.10. In particular, if $s$ is an ordinary point of $S$, the fiber of $\Pi^{S}_{1}$ at $s$ is a pro-group
over $\kappa(s)$, a projective limit of finite étale groups over $\kappa(s)$. One could call this pro-group **the
fundamental group of $S$ at the ordinary point $s$ of $S$**, and denote it $\pi_{1}(S,s)$. By definition, its points
with values in an algebraically closed extension $\Omega$ of $\kappa(s)$ are the elements of $\pi_{1}(S;a)$, where $a$
is the geometric point of $S$ defined by that extension. In particular, taking $S$ to be the spectrum of a field, there
is associated canonically and functorially to every field $k$ a pro-group over $k$, which one might denote $\pi_{1}(k)$,
a projective limit of finite étale groups over $k$, whose points in an algebraically closed extension $\Omega$ of $k$
are identified

<!-- original page 142 -->

with the elements of the topological Galois group of $\bar{k}/k$, where $\bar{k}$ is the Galois closure of $k$ in
$\Omega$; cf. V.8.1. This group $\pi_{1}(k)$ does not seem yet to have attracted the attention of algebraists.

Let now

$$
f: S' \to S
$$

be a morphism from one connected locally noetherian prescheme to another, let $a'$ be a geometric point of $S'$, and let
$a = f(a')$ be its direct image in $S$. Then the inverse-image functor induces a functor from the category
$\mathcal{C}(S)$ of étale coverings of $S$ to the category $\mathcal{C}(S')$ of étale coverings of $S'$:

```text
f⁎: 𝒞(S) → 𝒞(S′).
```

Moreover, one has an isomorphism of functors

```text
F_a ≃ F_{a′} ∘ f⁎,
```

so that `f⁎` is an **exact** functor, to which the results of V.6 apply. In particular, one has a canonical homomorphism

```text
u = π₁(f;a′): π₁(S′,a′) → π₁(S,a),    where a = f(a′),
```

which allows the inverse-image functor to be reconstructed as an operation of restriction of groups of operators. The
properties of the functor `f⁎` are therefore expressed simply by the properties of the associated group homomorphism, as
made explicit in V.6. If in particular $S'$ is an étale covering of $S$, then $u$ is an isomorphism from
$\pi_{1}(S',a')$ onto the open subgroup of $\pi_{1}(S,a)$ that defines the connected pointed étale covering $S'$ of $S$,
i.e. the stabilizer $U$ of $a' \in F_{a}(S')$ in $\pi_{1}(S,a)$.

If one wants to interpret the homomorphisms $\pi_{1}(f;a')$ for variable geometric point $a'$, then, in accordance with
what was said in V.6, one must consider a homomorphism

```text
Π₁(f): Π₁^{S′} → f⁎(Π₁^S)
```

of pro-groups over $S'$, and take the corresponding homomorphism on geometric fibers.

## 8. The Case of a Normal Base Prescheme

<!-- label: V.8 -->

<!-- original page 143 -->

**Proposition.**

<!-- label: V.8.1 -->

Let $S$ be the spectrum of a field $k$, and let $\Omega$ be an algebraically closed extension of $k$, defining a
geometric point $a$ of $S$ with values in $\Omega$. Let $\bar{k}$ be the separable closure of $k$ in $\Omega$. Then
there exists a canonical isomorphism from $\pi_{1}(S,a)$ onto the topological Galois group of $\bar{k}/k$.

Let $k'$ be the algebraic closure of $k$ in $\Omega$; it therefore corresponds to a geometric point $b$ of $S$, with
values in $k'$. The natural homomorphism of functors $F_{b} \to F_{a}$ is evidently an isomorphism, because a
$k$-homomorphism from a finite separable extension of $k$ into $\Omega$ necessarily takes its values in $\bar{k}$, and a
fortiori in $k'$. On the other hand, the group $\pi'$ of $k$-automorphisms of $k'/k$ operates evidently on $F_{b}$,
whence a homomorphism

```text
π′ → Aut(F_b) ≃ Aut(F_a) = π₁(S;a).
```

It is well known, moreover, that the natural homomorphism from $\pi'$ to the group $\pi$ of automorphisms of $\bar{k}/k$
is an isomorphism. One thus obtains a canonical homomorphism $\pi \to \pi_{1}(S;a)$; it remains to show that this is an
isomorphism. Indeed, this homomorphism is injective, because an element of the kernel is an automorphism of $\bar{k}/k$
that induces the identity on every finite separable subextension, hence is trivial. It is surjective, because if $X$ is
a **connected** étale covering of $S$, hence defined by a finite separable **extension** $L/k$, then $\pi$ is transitive
on the set of $k$-homomorphisms from $L$ into $k'$, as is well known.

**Proposition.**

<!-- label: V.8.2 -->

Let $S$ be a connected, locally noetherian, normal prescheme; let $K = \kappa(s)$ be its function field, i.e. the
residue field at its generic point $s$; and let $\Omega$ be an algebraically closed extension of $K$, defining a
geometric point $a'$ of $S' = \operatorname{Spec}(K)$ and a geometric point $a$ of $S$. Then the homomorphism
$\pi_{1}(S';a') \to \pi_{1}(S;a)$ is surjective. When the first group is identified with the Galois group of the
separable closure $\bar{K}$ of $K$ in $\Omega$, cf. V.8.1, the kernel of the preceding homomorphism corresponds by
Galois theory to the subextension of $\bar{K}/K$ composed of the finite extensions of $K$ in $\Omega$ that are
unramified over $S$.

The first assertion means that the inverse image on $S'$ of a connected étale covering $X$ of $S$ is connected, i.e.
that $X$ is integral; this is nothing other than I.10.1. The kernel of the preceding homomorphism is then interpreted as
consisting of the automorphisms of $\bar{K}/K$ that induce the identity on the sets $F_{a}(X)$,

<!-- original page 144 -->

where the étale covering $X$ of $S$ may be supposed connected. But this means that this automorphism induces the
identity on the finite subextensions of $\bar{K}/K$ that are unramified over $S$, which proves the last assertion.

**Remark.** Thanks to this interpretation of the fundamental group of the normal prescheme $S$ in terms of ordinary
Galois theory, the definition had been known in this case for a long time.

## 9. The Case of Nonconnected Preschemes: Multi-Galois Categories

<!-- label: V.9 -->

Let $S$ be a locally noetherian prescheme, and let $(S_{i})_{i}\in I$ be its connected components. Then the category
$\mathcal{C}(S)$ of étale coverings of $S$ is equivalent to the product category of the $\mathcal{C}(S_{i})$, which are
interpreted in terms of the fundamental groups of the `Sᵢ` once a geometric point has been chosen in each `Sᵢ`. In
applying descent theory for étale morphisms, it is sometimes inconvenient to choose a geometric point of `Sᵢ` for every
`Sᵢ`. It is then more convenient to use the natural generalization of V.5.8 to interpret $\mathcal{C}(S)$ as a category
of functors on the groupoid of geometric points of $S$, regarded as the sum of the groupoids corresponding to the
connected components of $S$. The functors in question are functors with values in the category of finite sets satisfying
the continuity property analogous to the one invoked in V.5.8.

In practice, one will have a family $(a_{t})_{t\in E}$ of geometric points of $S$ such that every connected component
`Sᵢ` of $S$ contains at least one of them, and then, as in V.5.10, one may replace the groupoid of all geometric points
of $S$ by the analogous groupoid whose underlying set is $E$. Of course, these considerations should be fitted into
general definitions concerning categories that are equivalent to product categories of categories of the form
$\mathcal{C}(\pi)$, and that one may call **multi-Galois categories**. We leave the details to the reader.

[^v-intro-1]: Cf. Exposé VI and Exposé VIII.

[^v-1-1-1]: Cf. N. Bourbaki, _Algèbre Commutative_, Chap. 5, §1 and §2, Th. 2.

[^v-2-5-1]: One now rather says: $X$ is a pseudo-torsor under `G_Y`.

[^v-2-5-2]: Cf. Exposé VIII for the theory of flat descent.

[^v-4-1]: Recall that an object $e$ of $\mathcal{C}$ is called a **final object** if, for every $X$ in $\mathcal{C}$,
    $\operatorname{Hom}(X,e)$ has exactly one element. Dually one defines an **initial object** of $\mathcal{C}$.

[^v-5-1-1]: It seems preferable to adopt the more expressive term “fiber functor”.


<!-- SOURCE: 06-categories-fibrees-et-descente.md -->

# Exposé VI. Fibered Categories and Descent

<!-- label: VI -->

<!-- original page 145 -->

## 0. Introduction

Contrary to what had been announced in the introduction to the preceding exposé, it has turned out to be impossible to
do descent in the category of preschemes, even in particular cases, without first having developed with sufficient care
the language of descent in general categories.

The notion of “descent” supplies the general framework for all procedures of “gluing” objects, and consequently of
“gluing” categories. The most classical case of gluing is relative to the data of a topological space $X$ and a covering
of $X$ by open subsets `Xᵢ`. Suppose one is given, for every $i$, a fiber space, say, `Eᵢ` over `Xᵢ`, and for every pair
$(i,j)$ an isomorphism $f_{ji}$ from $E_{i}|X_{ij}$ to $E_{j}|X_{ij}$, where $X_{ij} = X_{i} \cap X_{j}$, satisfying the
well-known transitivity condition, written in abbreviated form $f_{kj} f_{ji} = f_{ki}$. One knows that there exists a
fiber space $E$ on $X$, defined up to isomorphism by the condition that one have isomorphisms
$f_{i}: E|X_{i} \simeq E_{i}$ satisfying the relations $f_{ji} = f_{j} f^{-1}_{i}$, with the usual abuse of notation.

Let $X'$ be the sum space of the `Xᵢ`; it is therefore a fiber space over $X$, i.e. endowed with a continuous map
$X' \to X$. The data of the `Eᵢ` can be interpreted more concisely as a fiber space $E'$ over $X'$, and the data of the
$f_{ji}$ as an isomorphism between the two inverse images, by the two canonical projections, $E''_{1}$ and $E''_{2}$ of
$E'$ on $X'' = X' \times_{X} X'$. The gluing condition can then be written as an identity between isomorphisms of fiber
spaces $E'''_{1}$ and $E'''_{3}$ over the triple fiber product $X''' = X' \times_{X} X' \times_{X} X'$, where $E'''_{i}$
denotes the inverse image of $E'$ on $X'''$ by the canonical projection of index $i$. The construction of $E$ from $E'$
and $f$ is a typical case of a “descent” procedure.

<!-- original page 146 -->

Moreover, starting from a fiber space $E$ on $X$, one says that $X$ is “locally trivial”, with fiber $F$, if there
exists an open covering $(X_{i})$ of $X$ such that the $E|X_{i}$ are isomorphic to $F \times X_{i}$, or what amounts to
the same thing, such that the inverse image $E'$ of $E$ on $X' = \coprod_{i} X_{i}$ is isomorphic to $X' \times F$.

Thus the notion of “gluing” objects, like that of “localization” of a property, is tied to the study of certain types of
“base changes” $X' \to X$. In algebraic geometry, many other types of base change, and notably faithfully flat morphisms
$X' \to X$, must be regarded as corresponding to a procedure of “localization” relative to preschemes, or other objects,
“over” $X$. This type of localization is used just as much as ordinary topological localization, of which it is moreover
a special case. The same is true, to a lesser extent, in analytic geometry.

Most of the proofs, reducing to verifications, are omitted or merely sketched. Where appropriate, we specify the less
evident diagrams that enter into a proof.

## 1. Universes, Categories, Equivalence of Categories

<!-- label: VI.1 -->

To avoid certain logical difficulties, we shall admit here the notion of a **Universe**, which is a set “large enough”
that one does not leave it under the usual operations of set theory; an “**axiom of Universes**” guarantees that every
object lies in a Universe. For details, see a book in preparation by C. Chevalley and the speaker.[^vi-1-1] Thus the
symbol `Set` denotes not the category of all sets, a notion that has no sense, but the category of sets that lie in a
given Universe, which we shall not specify in the notation. Similarly, `Cat` will denote the category of categories
lying in the Universe in question; the “morphisms” from one object $X$ of `Cat` to another $Y$ are, by definition, the
**functors** from $X$ to $Y$.

<!-- original page 147 -->

If $\mathcal{C}$ is a category, we denote by $Ob(\mathcal{C})$ **the set of objects** of $\mathcal{C}$, and by
$Fl(\mathcal{C})$ **the set of arrows** of $\mathcal{C}$, or morphisms of $\mathcal{C}$. We shall therefore write
$X \in Ob(\mathcal{C})$, avoiding the common abuse of notation $X \in \mathcal{C}$. If $\mathcal{C}$ and $\mathcal{C}'$
are two categories, a **functor** from $\mathcal{C}$ to $\mathcal{C}'$ will always mean what is commonly called a
**covariant** functor from $\mathcal{C}$ to $\mathcal{C}'$. Its data include both the target category and the source
category, $\mathcal{C}$ and $\mathcal{C}'$. The functors from $\mathcal{C}$ to $\mathcal{C}'$ form a set, denoted
$\operatorname{Hom}(\mathcal{C},\mathcal{C}')$, which is the set of objects of a category denoted `Hom̲(𝒞,𝒞′)`. By
definition, a **contravariant functor** from $\mathcal{C}$ to $\mathcal{C}'$ is a functor from the **opposite category**
$\mathcal{C}^{\circ}$ of $\mathcal{C}$ to $\mathcal{C}'$.

We shall admit the notions of **projective limit** and **inductive limit** of a functor
$F: \mathcal{I} \to \mathcal{C}$, and in particular the most common special cases of these notions: cartesian products
and fiber products, the dual notions of direct sums and amalgamated sums, and the usual formal properties of these
operations.

For example, in the category `Cat` introduced above, projective limits, relative to categories $\mathcal{I}$ lying in
the chosen Universe, exist. The set of objects, respectively the set of arrows, of the projective-limit category
$\mathcal{C}$ of the $\mathcal{C}_{i}$ is obtained by taking the projective limit of the sets of objects, respectively
the sets of arrows, of the categories $\mathcal{C}_{i}$. The best-known case is that of the product of a family of
categories. We shall constantly use, in what follows, the fiber product of two categories over a third.

For everything concerning categories and functors, pending the book in preparation already mentioned, see [VI.1], which
is necessarily quite incomplete, even as concerns the generalities sketched in the present number.

Let us take this occasion to spell out the notion of equivalence of categories, which is not presented satisfactorily in
[VI.1]. A functor $F: \mathcal{C} \to \mathcal{C}'$ is said to be **faithful**, respectively **fully faithful**, if for
every pair of objects $S$, $T$ of $\mathcal{C}$, the map $u \mapsto F(u)$ from $\operatorname{Hom}(S,T)$ to
$\operatorname{Hom}(F(S),F(T))$ is injective, respectively bijective. One says that $F$ is an **equivalence** of
categories if

<!-- original page 148 -->

$F$ is fully faithful and, moreover, every object $S'$ of $\mathcal{C}'$ is isomorphic to an object of the form $F(S)$.
One shows that this is the same as saying that there exists a functor $G$ from $\mathcal{C}'$ to $\mathcal{C}$
**quasi-inverse** to $F$, i.e. such that `GF` is isomorphic to $id_{\mathcal{C}}$ and `FG` is isomorphic to
$id_{\mathcal{C}}'$.

When this is so, giving a functor $G: \mathcal{C}' \to \mathcal{C}$ and an isomorphism $\phi: FG \to id_{\mathcal{C}}'$
is equivalent to giving, for every $S' \in Ob(\mathcal{C}')$, a pair $(S,u)$ formed by an object $S$ of $\mathcal{C}$
and an isomorphism $u: F(S) \to S'$, namely $(G(S'), \phi(S'))$. With this notation, there exists a unique functor
$\mathcal{C}' \to \mathcal{C}$ having the given map $S' \mapsto G(S')$ as its object map, and such that the map
$S' \mapsto \phi(S')$ is a homomorphism of functors $FG \to id_{\mathcal{C}}'$.

Finally, if $G$ is a functor quasi-inverse to $F$, and if one chooses isomorphisms $\phi: FG \simeq id_{\mathcal{C}}'$
and $\psi: GF \simeq id_{\mathcal{C}}$, then the two compatibility conditions on $\phi$ and $\psi$ stated in [VI.1,
I.1.2] are in fact equivalent to one another; and for every chosen isomorphism $\phi$, there exists a unique isomorphism
$\psi$ such that those conditions are satisfied.

## 2. Categories over Another Category

<!-- label: VI.2 -->

Let $\mathcal{E}$ be a category in the chosen Universe. It is therefore an object of `Cat`, and one may consider the
category $Cat_{/}\mathcal{E}$ of “objects of `Cat` over $\mathcal{E}$”. An object of this category is therefore a
functor

$$
p: \mathcal{F} \to \mathcal{E}.
$$

One also says that the category $\mathcal{F}$, endowed with such a functor, is a **category over** $\mathcal{E}$, or an
**$\mathcal{E}$-category**. Thus an **$\mathcal{E}$-functor** from a category $\mathcal{F}$ over $\mathcal{E}$ to a
category $\mathcal{G}$ over $\mathcal{E}$ will mean a functor

$$
f: \mathcal{F} \to \mathcal{G}
$$

such that

```text
qf = p,
```

where $p$ and $q$ are the projection functors for $\mathcal{F}$ and $\mathcal{G}$ respectively. The set of
$\mathcal{E}$-functors $f$ from $\mathcal{F}$ to $\mathcal{G}$ is therefore in bijective correspondence with the set of
arrows with source $\mathcal{F}$ and target $\mathcal{G}$ in $Cat_{/}\mathcal{E}$,

<!-- original page 149 -->

without this being an identity, since the data of an $f$ as above does not determine $\mathcal{F}$ and $\mathcal{G}$ as
categories over $\mathcal{E}$. Of course, as in any other category $\mathcal{C}_{/}S$, we shall routinely make the abuse
of language that identifies $\mathcal{E}$-functors, in the sense just explained, with arrows in a category
$Cat_{/}\mathcal{E}$.

We shall denote by

$$
\operatorname{Hom}_{\mathcal{E}}(\mathcal{F},\mathcal{G})
$$

the set of $\mathcal{E}$-functors from $\mathcal{F}$ to $\mathcal{G}$. Of course, a composite of $\mathcal{E}$-functors
is an $\mathcal{E}$-functor, the composition in question corresponding by definition to the composition of arrows in
$Cat_{/}\mathcal{E}$.

Now consider two $\mathcal{E}$-functors

$$
f,g: \mathcal{F} \to \mathcal{G}
$$

and a homomorphism of functors

$$
u: f \to g.
$$

One says that $u$ is an **$\mathcal{E}$-homomorphism**, or a “**homomorphism of $\mathcal{E}$-functors**”, if for every
$\xi \in Ob(\mathcal{F})$, one has

$$
q(u(\xi)) = id_{p(\xi)}.
$$

In words: putting $S = p(\xi) = qf(\xi) = qg(\xi) \in Ob(\mathcal{E})$, the morphism

$$
u(\xi): f(\xi) \to g(\xi)
$$

in $\mathcal{G}$ is an $id_{S}$-morphism. In general, for every morphism $\alpha: T \to S$ in $\mathcal{E}$ and every
category $\mathcal{G}$ over $\mathcal{E}$, a morphism $v$ in $\mathcal{G}$ is called an **$\alpha$-morphism** if
$q(v) = \alpha$, where $q$ denotes the projection functor $\mathcal{G} \to \mathcal{E}$. If one has a third
$\mathcal{E}$-functor $h: \mathcal{F} \to \mathcal{G}$ and an $\mathcal{E}$-homomorphism $v: g \to h$, then `vu` is
again an $\mathcal{E}$-homomorphism.

<!-- original page 150 -->

Thus **the $\mathcal{E}$-functors from $\mathcal{F}$ to $\mathcal{G}$, and the $\mathcal{E}$-homomorphisms between them,
form a subcategory of the category `Hom̲(ℱ,𝒢)` of all functors from $\mathcal{F}$ to $\mathcal{G}$; it will be called the
category of $\mathcal{E}$-functors from $\mathcal{F}$ to $\mathcal{G}$ and denoted**

```text
Hom̲_{ℰ/-}(ℱ,𝒢).
```

It is also the kernel subcategory of the pair of functors

```text
R,S: Hom̲(ℱ,𝒢) ⇉ Hom̲(ℱ,ℰ),
```

where $R$ is the constant functor defined by the object $p$ of `Hom̲(ℱ,ℰ)`, and $S$ is the functor $f \mapsto q \circ f$
defined by $q: \mathcal{G} \to \mathcal{E}$.

To finish these generalities, it remains to define the natural pairings between the categories `Hom̲_{ℰ/-}(ℱ,𝒢)` by
composition of $\mathcal{E}$-functors. In other words, one wants to define a “composition functor”

```text
(i)  Hom̲_{ℰ/-}(ℱ,𝒢) × Hom̲_{ℰ/-}(𝒢,ℋ) → Hom̲_{ℰ/-}(ℱ,ℋ)
```

when $\mathcal{F}$, $\mathcal{G}$, $\mathcal{H}$ are three categories over $\mathcal{E}$, in such a way that this
functor induces, on objects, the composition map $(f,g) \mapsto gf$ for $\mathcal{E}$-functors
$f: \mathcal{F} \to \mathcal{G}$ and $g: \mathcal{G} \to \mathcal{H}$. For this, recall that one defines a canonical
functor

```text
(ii) Hom̲(ℱ,𝒢) × Hom̲(𝒢,ℋ) → Hom̲(ℱ,ℋ),
```

which on objects is just the composition map $(f,g) \mapsto gf$ of functors, and which transforms an arrow $(u,v)$,
where

```text
u: f → f′,    v: g → g′,
```

are arrows in `Hom̲(ℱ,𝒢)`, respectively in `Hom̲(𝒢,ℋ)`, into the arrow

```text
v ∗ u: gf → g′f′
```

defined by the relation

<!-- original page 151 -->

```text
(v ∗ u)(ξ) = v(f′(ξ)) · g(u(ξ)) = g′(u(ξ)) · v(f(ξ)).
```

It is well known that one indeed obtains in this way a homomorphism from `gf` to $g'f'$, and that, for variable $f$, $g$
and $u$, $v$, one obtains the functor (ii); that is, one has

```text
(I)   id_g ∗ id_f = id_{gf},
```

and

```text
(II)  (v′ ∗ u′) ∘ (v ∗ u) = (v′ ∘ v) ∗ (u′ ∘ u).
```

Recall also that one has an associativity formula for the canonical pairings (ii), expressed on the one hand by the
associativity $(hg)f = h(gf)$ of the composition of functors, and on the other hand by the formula

```text
(III) (w ∗ v) ∗ u = w ∗ (v ∗ u)
```

for the composition products of homomorphisms of functors, where $u: f \to f'$ and $v: g \to g'$ are as above, and where
one supposes given in addition a homomorphism $w: h \to h'$ of functors $h,h': \mathcal{H} \to \mathcal{K}$.

I now say that **when $\mathcal{F}$ and $\mathcal{G}$ are $\mathcal{E}$-categories, the canonical composition functor
(ii) induces a functor (i)**. Since we already know that the composite of two $\mathcal{E}$-functors is an
$\mathcal{E}$-functor, this amounts to saying that **when $u: f \to f'$ and $v: g \to g'$ are homomorphisms of
$\mathcal{E}$-functors, then $v \ast u: gf \to g'f'$ is also a homomorphism of $\mathcal{E}$-functors**. This follows
trivially from the definitions. Since the pairings (i) are induced by the pairings (ii), they satisfy the same
associativity property, also expressed in the formulas $(hg)f = h(gf)$ and $(w \ast v) \ast u = w \ast (v \ast u)$, for
$\mathcal{E}$-functors and $\mathcal{E}$-homomorphisms of $\mathcal{E}$-functors.

To complete the formulary (I), (II), (III), recall also the formulas

```text
(IV)  v ∗ id_ℱ = v    and    id_𝒢 ∗ u = u,
```

<!-- original page 152 -->

where, for simplicity, one writes $v \ast f$ or $u \ast g$ instead of $v \ast u$ when $u$, respectively $v$, is the
identity automorphism of $f$, respectively $g$.

It follows from the definition of the pairings (i) that **`Hom̲_{ℰ/-}(ℱ,𝒢)` is a functor in $\mathcal{F}$ and
$\mathcal{G}$, from the product category $Cat_{/}\mathcal{E}^{\circ} \times Cat_{/}\mathcal{E}$ to the category `Cat`**.
Indeed, if $g: \mathcal{G} \to \mathcal{G}_{1}$ is an $\mathcal{E}$-functor, i.e. an object of `Hom̲_{ℰ/-}(𝒢,𝒢₁)`, then
by taking $\mathcal{H} = \mathcal{G}_{1}$ in (i), there corresponds to it a functor

```text
g_*: Hom̲_{ℰ/-}(ℱ,𝒢) → Hom̲_{ℰ/-}(ℱ,𝒢₁).
```

One defines analogously, for an $\mathcal{E}$-functor $f: \mathcal{F}_{1} \to \mathcal{F}$, a functor

```text
f^*: Hom̲_{ℰ/-}(ℱ,𝒢) → Hom̲_{ℰ/-}(ℱ₁,𝒢).
```

For short, these functors are also denoted by the symbols $f \mapsto g \circ f$ and $g \mapsto g \circ f$ respectively;
these in fact denote only the corresponding maps on the sets of objects. It follows from the associativity property
indicated above that one does indeed obtain in this way, as announced, a functor `Cat_/ℰ° × Cat_/ℰ → Cat`.

## 3. Base Change in Categories over ℰ

<!-- label: VI.3 -->

Since projective limits exist in `Cat`, relative to categories $\mathcal{I}$ belonging to the Universe, the same is true
in $Cat_{/}\mathcal{E}$. In particular, cartesian products exist there; these are interpreted as fiber products in
`Cat`. In accordance with the general notation, if $\mathcal{F}$ and $\mathcal{G}$ are categories over $\mathcal{E}$, we
denote by

$$
\mathcal{F} \times_{\mathcal{E}} \mathcal{G}
$$

their product in $Cat_{/}\mathcal{E}$, i.e. their fiber product over $\mathcal{E}$ in `Cat`, regarded as a category over
$\mathcal{E}$. Thus $\mathcal{F} \times_{\mathcal{E}} \mathcal{G}$ is endowed with two $\mathcal{E}$-functors $pr_{1}$
and $pr_{2}$, which define, for every category $\mathcal{H}$ over $\mathcal{E}$, a bijection

<!-- original page 153 -->

```text
Hom_ℰ(ℋ, ℱ ×_ℰ 𝒢) ≃ Hom_ℰ(ℋ,ℱ) × Hom_ℰ(ℋ,𝒢).
```

This bijection moreover comes from an isomorphism of categories

```text
Hom̲_{ℰ/-}(ℋ, ℱ ×_ℰ 𝒢) ≃ Hom̲_{ℰ/-}(ℋ,ℱ) × Hom̲_{ℰ/-}(ℋ,𝒢),
```

by taking the sets of objects of the two sides. The displayed functor is the one whose components are the functors
$h \mapsto pr_{1} \circ h$ and $h \mapsto pr_{2} \circ h$ from the first member to the two factors of the second. We
leave to the reader the verification that one indeed obtains an isomorphism in this way; the analogous fact is true more
generally whenever one has a projective limit of categories, and not only in the case of a fiber product.

Recall moreover, as was said in VI.1, that

```text
Ob(ℱ ×_ℰ 𝒢) = Ob(ℱ) ×_{Ob(ℰ)} Ob(𝒢),
Fl(ℱ ×_ℰ 𝒢) = Fl(ℱ) ×_{Fl(ℰ)} Fl(𝒢),
```

the composition of arrows being carried out componentwise.

In what follows, we consider a functor

$$
\lambda: \mathcal{E}' \to \mathcal{E},
$$

and, for every category $\mathcal{F}$ over $\mathcal{E}$, we regard $\mathcal{F} \times_{\mathcal{E}} \mathcal{E}'$ as a
category over $\mathcal{E}'$ by means of $pr_{2}$. In other words, we interpret the “fiber product” operation as an
operation of **“base change”**, the functor $\lambda: \mathcal{E}' \to \mathcal{E}$ being called the **“base-change
functor.”** In accordance with the well-known general facts, one obtains in this way a functor, called the **base-change
functor** for $\lambda$:

<!-- original page 154 -->

$$
\lambda*: Cat_{/}\mathcal{E} \to Cat_{/}\mathcal{E}'.
$$

It is adjoint to the “restriction of the base” functor, which sends every category $\mathcal{F}'$ over $\mathcal{E}'$,
with projection functor $p'$, to $\mathcal{F}'$ regarded as a category over $\mathcal{E}$ by the functor
$p = \lambda p'$. As is well known for a base-change functor in a category, the base-change functor “commutes with
projective limits”, and in particular “transforms” fiber products over $\mathcal{E}$ into fiber products over
$\mathcal{E}'$.

Let $\mathcal{F}$ and $\mathcal{G}$ be two categories over $\mathcal{E}$. We shall define a **canonical isomorphism**

```text
(i)  Hom̲_{ℰ′/-}(ℱ′,𝒢′) ≃ Hom̲_{ℰ/-}(ℱ ×_ℰ ℰ′,𝒢),
     where ℱ′ = ℱ ×_ℰ ℰ′ and 𝒢′ = 𝒢 ×_ℰ ℰ′.
```

For this, consider the functor

```text
pr₁: 𝒢′ = 𝒢 ×_ℰ ℰ′ → 𝒢,
```

and define (i) by

$$
F \mapsto pr_{1} \circ F,
$$

which a priori denotes a functor

```text
(ii) Hom̲(ℱ′,𝒢′) → Hom̲(ℱ′,𝒢).
```

It remains only to verify that this latter functor induces a functor on the subcategories in (i), and that this induced
functor is an isomorphism. That (ii) induces a bijection

```text
Hom_{ℰ′/-}(ℱ′,𝒢′) ≃ Hom_{ℰ/-}(ℱ ×_ℰ ℰ′,𝒢)
```

is the characteristic property of the base-change functor. It remains therefore

<!-- original page 155 -->

to prove that if $F$, $G$ are $\mathcal{E}'$-functors $\mathcal{F}' \to \mathcal{G}'$, then **the map**

$$
u \mapsto pr_{1} \circ u
$$

**induces a bijection**

```text
Hom_{ℰ′}(F,G) ≃ Hom_ℰ(pr₁ ∘ F, pr₁ ∘ G).
```

The verification of this fact is immediate and is left to the reader.

It follows from this isomorphism (i), and from the end of the preceding number, that

```text
Hom̲_{ℰ′/-}(ℱ ×_ℰ ℰ′, 𝒢 ×_ℰ ℰ′)
```

**may be regarded as a functor in $\mathcal{E}'$, $\mathcal{F}$, $\mathcal{G}$, from the category
`Cat_/ℰ° × Cat_/ℰ° × Cat_/ℰ` to the category `Cat`**, isomorphic to the functor defined by the expression

```text
Hom̲_{ℰ/-}(ℱ ×_ℰ ℰ′,𝒢).
```

In particular, for fixed $\mathcal{F}$ and $\mathcal{G}$, one obtains a functor in $\mathcal{E}'$. Thus the
$\mathcal{E}$-functor of projection $\lambda: \mathcal{E}' \to \mathcal{E}$ defines a morphism, i.e. a functor

```text
λ*_{ℱ,𝒢}: Hom̲_{ℰ/-}(ℱ,𝒢) → Hom̲_{ℰ′/-}(ℱ′,𝒢′),
```

which we now spell out. On the sets of objects of the two sides, it is the map

```text
f ↦ f′ = f ×_ℰ ℰ′,
```

expressing the functorial dependence of $\mathcal{F} \times_{\mathcal{E}} \mathcal{E}'$ on the object $\mathcal{F}$ over
$\mathcal{E}$. On the other hand, consider two $\mathcal{E}$-functors

$$
f,g: \mathcal{F} \to \mathcal{G}
$$

and a homomorphism of $\mathcal{E}$-functors

$$
u: f \to g.
$$

We shall spell out the corresponding homomorphism of $\mathcal{E}'$-functors

<!-- original page 156 -->

$$
u': f' \to g'.
$$

For every

$$
\xi' = (\xi,S') \in Ob(\mathcal{F}')
$$

with

```text
ξ ∈ Ob(ℱ),    S′ ∈ Ob(ℰ′),    p(ξ) = λ(S′) = S,
```

the morphism

```text
u′(ξ′): f′(ξ′) = (f(ξ),S′) → g′(ξ′) = (g(ξ),S′)    in 𝒢′
```

is defined by the formula

$$
u'(\xi') = (u(\xi), id_{S'}).
$$

This is indeed an $S'$-morphism in $\mathcal{G}'$, since $q(u(\xi)) = \lambda(id_{S'}) = id_{S}$.

Now consider any $\mathcal{E}$-functor

$$
\lambda': \mathcal{E}'' \to \mathcal{E}'
$$

and the corresponding functor

```text
Hom̲_{ℰ′/-}(ℱ ×_ℰ ℰ′, 𝒢 ×_ℰ ℰ′)
  → Hom̲_{ℰ″/-}(ℱ ×_ℰ ℰ″, 𝒢 ×_ℰ ℰ″).
```

I say that this functor is none other than the one obtained by the preceding process, starting from $\mathcal{F}'$ and
$\mathcal{G}'$ over $\mathcal{E}'$ and regarding $\mathcal{E}''$ as a category over $\mathcal{E}'$, taking into account
the isomorphisms of **“transitivity of base change”**

```text
ℱ′ ×_ℰ′ ℰ″ ≃ ℱ″ = ℱ ×_ℰ ℰ″,
𝒢′ ×_ℰ′ ℰ″ ≃ 𝒢″ = 𝒢 ×_ℰ ℰ″,
```

which imply a canonical isomorphism

```text
Hom̲_{ℰ″/-}(ℱ′ ×_ℰ′ ℰ″, 𝒢′ ×_ℰ′ ℰ″)
  ≃ Hom̲_{ℰ″/-}(ℱ ×_ℰ ℰ″, 𝒢 ×_ℰ ℰ″).
```

<!-- original page 157 -->

The verification of this compatibility is immediate and is left to the reader.

The functors just defined are compatible with the pairings defined in the preceding number. More precisely, if
$\mathcal{F}$, $\mathcal{G}$, $\mathcal{H}$ are categories over $\mathcal{E}$ and if one puts

```text
ℱ′ = ℱ ×_ℰ ℰ′,    𝒢′ = 𝒢 ×_ℰ ℰ′,    ℋ′ = ℋ ×_ℰ ℰ′,
```

one has commutativity in the following diagram of functors:

```text
Hom̲_{ℰ/-}(ℱ,𝒢) × Hom̲_{ℰ/-}(𝒢,ℋ)  →  Hom̲_{ℰ/-}(ℱ,ℋ)
        ↓ λ*_{ℱ,𝒢} × λ*_{𝒢,ℋ}              ↓ λ*_{ℱ,ℋ}
Hom̲_{ℰ′/-}(ℱ′,𝒢′) × Hom̲_{ℰ′/-}(𝒢′,ℋ′) → Hom̲_{ℰ′/-}(ℱ′,ℋ′),
```

where the horizontal arrows are the composition functors defined in the preceding number. This commutativity is
expressed by the formulas

$$
(gf)' = g'f'
$$

for $f \in \operatorname{Hom}_{\mathcal{E}}(\mathcal{F},\mathcal{G})$,
$g \in \operatorname{Hom}_{\mathcal{E}}(\mathcal{G},\mathcal{H})$, a formula which simply expresses the functoriality of
base change, and

```text
(v ∗ u)′ = v′ ∗ u′
```

when $u: f \to f_{1}$ is an arrow of `Hom̲_{ℰ/-}(ℱ,𝒢)` and $v: g \to g_{1}$ is an arrow of `Hom̲_{ℰ/-}(𝒢,ℋ)`. The
verification of this formula follows easily from the definitions.

In what follows, we shall be chiefly interested in `Hom̲_ℰ(ℱ,𝒢)`, and certain remarkable subcategories of it, when
$\mathcal{F} = \mathcal{E}$. For this reason we introduce a special notation:

```text
Γ̲(𝒢/ℰ) = Hom̲_ℰ(ℰ,𝒢),
Γ(𝒢/ℰ) = Ob(Γ̲(𝒢/ℰ)) = Hom_ℰ(ℰ,𝒢).
```

**Remarks.** When $\mathcal{E}$ is a point category, i.e. $Ob(\mathcal{E})$ and $Fl(\mathcal{E})$ are reduced to a
single element, which also means that $\mathcal{E}$ is a final object of the category `Cat`, then the data of a category
over $\mathcal{E}$ is equivalent to the data of a category in the ordinary sense, since there will be a unique functor
from $\mathcal{F}$ to $\mathcal{E}$. More precisely, $Cat_{/}\mathcal{E}$ is then isomorphic to `Cat`. Moreover, the
categories `Hom̲_{ℰ/-}(ℱ,𝒢)` are then none other than the `Hom̲(ℱ,𝒢)`.

<!-- original page 158 -->

Recall then that the fundamental formula

```text
Hom(ℋ, Hom̲(ℱ,𝒢)) ≃ Hom(ℱ × ℋ, 𝒢),
```

functorial in the three arguments appearing in it, allows `Hom̲(ℱ,𝒢)` to be interpreted axiomatically, in terms internal
to the category `Cat`. Thus the familiar formulary for `Hom̲`-categories appears as a special case of a formulary valid
in categories such as `Cat`, where “`Hom̲`-objects”, defined by the preceding formula, exist. There is an analogous
interpretation of `Hom̲_{ℰ/-}(ℱ,𝒢)`, when $\mathcal{E}$ is again arbitrary, by the formula

```text
Hom(ℋ, Hom̲_{ℰ/-}(ℱ,𝒢)) ≃ Hom_ℰ(ℱ × ℋ, 𝒢),
```

functorial in the three arguments. In this way, the formal properties set out in VI.2 and VI.3 are special cases of more
general results, valid in categories where the objects `Hom̲_{ℰ/-}(ℱ,𝒢)`, for $\mathcal{F}$ and $\mathcal{G}$ two objects
of the category over a third object $\mathcal{E}$, exist.

## 4. Fiber Categories; Equivalence of ℰ-Categories

<!-- label: VI.4 -->

Let $\mathcal{F}$ be a category over $\mathcal{E}$, and let $S \in Ob(\mathcal{E})$. The **fiber category** of
$\mathcal{F}$ at $S$ is the subcategory $\mathcal{F}_{S}$ of $\mathcal{F}$ that is the inverse image of the point
subcategory of $\mathcal{E}$ defined by $S$.

<!-- original page 159 -->

Thus the objects of $\mathcal{F}_{S}$ are the objects $\xi$ of $\mathcal{F}$ such that $p(\xi) = S$, and its morphisms
are the morphisms $u$ of $\mathcal{F}$ such that $p(u) = id_{S}$, i.e. the $S$-morphisms in $\mathcal{F}$. Of course,
$\mathcal{F}_{S}$ is canonically isomorphic to the fiber product $\mathcal{F} \times_{\mathcal{E}} {S}$, where ${S}$
denotes the point subcategory of $\mathcal{E}$ defined by $S$, endowed with its inclusion functor into $\mathcal{E}$. It
follows, taking the transitivity of base change into account, that if one makes a base change
$\lambda: \mathcal{E}' \to \mathcal{E}$, then for every $S' \in Ob(\mathcal{E}')$, **the projection
$pr_{1}: \mathcal{F}' = \mathcal{F} \times_{\mathcal{E}} \mathcal{E}' \to \mathcal{F}$ induces an isomorphism**

```text
ℱ′_{S′} → ℱ_S,    where S = λ(S′).
```

**Proposition.**

<!-- label: VI.4.1 -->

Let $f: \mathcal{F} \to \mathcal{G}$ be an $\mathcal{E}$-functor. If $f$ is fully faithful, then for every base change
$\mathcal{E}' \to \mathcal{E}$, the corresponding functor

```text
f′: ℱ′ = ℱ ×_ℰ ℰ′ → 𝒢′ = 𝒢 ×_ℰ ℰ′
```

is fully faithful.

The verification is immediate. More generally, one can show that every projective limit of fully faithful functors, here
$f$ and the identity functors in $\mathcal{E}$ and $\mathcal{E}'$, is a fully faithful functor.

One should note that the assertion analogous to 4.1, with “fully faithful” replaced by “equivalence of categories”, is
false, already for $\mathcal{G} = \mathcal{E}$. However:

**Proposition.**

<!-- label: VI.4.2 -->

Let $f: \mathcal{F} \to \mathcal{G}$ be an $\mathcal{E}$-functor. The following conditions are equivalent:

1. There exists an $\mathcal{E}$-functor $g: \mathcal{G} \to \mathcal{F}$ and $\mathcal{E}$-isomorphisms

```text
gf ≃ id_ℱ,    fg ≃ id_𝒢.
```

1. For every category $\mathcal{E}'$ over $\mathcal{E}$, the functor

```text
f′ = f ×_ℰ ℰ′: ℱ′ = ℱ ×_ℰ ℰ′ → 𝒢′ = 𝒢 ×_ℰ ℰ′
```

is an equivalence of categories.

<!-- original page 160 -->

1. $f$ is an equivalence of categories, and for every $S \in Ob(\mathcal{E})$, the functor
   $f_{S}: \mathcal{F}_{S} \to \mathcal{G}_{S}$ induced by $f$ is an equivalence of categories.

1. $f$ is fully faithful, and for every $S \in Ob(\mathcal{E})$ and every $\eta \in Ob(\mathcal{G}_{S})$, there exist
   $\xi \in Ob(\mathcal{F}_{S})$ and an $S$-isomorphism $u: f(\xi) \to \eta$.

**Proof.** Evidently (1) implies that $f$ is an equivalence of categories, a notion defined by the same condition but
without requiring the isomorphisms of functors to be $\mathcal{E}$-morphisms. On the other hand, it follows from the
functorialities of the preceding number that condition (1) is preserved after base change
$\mathcal{E}' \to \mathcal{E}$. Hence (1) ⇒ (2). Evidently (2) ⇒ (3), since it is enough to take
$\mathcal{E}' = \mathcal{E}$ and $\mathcal{E}' = {S}$. It is still more trivial that (3) ⇒ (4). It remains to prove (4)
⇒ (1).

For this, choose for every $\eta \in Ob(\mathcal{G})$ an object $g(\eta) \in Ob(\mathcal{F})$ and an isomorphism
$u(\eta): f(g(\eta)) \to \eta$ such that $q(u(\eta)) = id_{S}$, where $S = q(\eta)$. This is possible by the second
condition in (4). As is known and immediate, the fact that $f$ is fully faithful implies that $g$ can be regarded in a
unique way as a functor from $\mathcal{G}$ to $\mathcal{F}$, so that the $u(\eta)$ define a functorial homomorphism,
hence isomorphism,

$$
u: fg \simeq id_{\mathcal{G}}.
$$

Moreover, by construction, $g$ is an $\mathcal{E}$-functor and $u$ an $\mathcal{E}$-homomorphism. To the preceding data
there then corresponds a functorial isomorphism $v: gf \to id_{\mathcal{F}}$, defined by the condition
$f \ast v = u \ast f$, and one sees at once that it is also an $\mathcal{E}$-morphism. This proves the assertion.

**Definition.**

<!-- label: VI.4.3 -->

If the preceding conditions are satisfied, one says that $f$ is an **equivalence of categories over $\mathcal{E}$**, or
an **$\mathcal{E}$-equivalence**.

**Corollary.**

<!-- label: VI.4.4 -->

Suppose that the projection functor $p: \mathcal{F} \to \mathcal{E}$ is a transportable functor, i.e. that for every
isomorphism $\alpha: T \to S$ in $\mathcal{E}$ and every object $\xi$ in $\mathcal{F}_{T}$, there exists an isomorphism
$u$ in $\mathcal{F}$ with source $\xi$ such that $p(u) = \alpha$. Then every $\mathcal{E}$-functor
$f: \mathcal{F} \to \mathcal{G}$ that is an equivalence of categories is an $\mathcal{E}$-equivalence.

This follows

<!-- original page 161 -->

from criterion (4).

**Corollary.**

<!-- label: VI.4.5 -->

Let $f: \mathcal{F} \to \mathcal{G}$ be an $\mathcal{E}$-equivalence. Then for every category $\mathcal{H}$ over
$\mathcal{E}$, the corresponding functors

```text
Hom̲_{ℰ/-}(𝒢,ℋ) → Hom̲_{ℰ/-}(ℱ,ℋ),
Hom̲_{ℰ/-}(ℋ,ℱ) → Hom̲_{ℰ/-}(ℋ,𝒢)
```

are equivalences of categories.

This follows from criterion (1) by the usual argument.

## 5. Cartesian Morphisms, Inverse Images, Cartesian Functors

<!-- label: VI.5 -->

Let $\mathcal{F}$ be a category over $\mathcal{E}$, with projection functor $p$.

**Definition.**

<!-- label: VI.5.1 -->

Consider a morphism

$$
\alpha: \eta \to \xi
$$

in $\mathcal{F}$, and let

```text
S = p(ξ),    T = p(η),    f = p(α).
```

One says that $\alpha$ is a **cartesian morphism** if, for every $\eta' \in Ob(\mathcal{F}_{T})$ and every $f$-morphism
$u: \eta' \to \xi$, there exists a unique $T$-morphism $\bar{u}: \eta' \to \eta$ such that $u = \alpha \circ \bar{u}$.

This therefore means that, for every $\eta' \in Ob(\mathcal{F}_{T})$, the map $v \mapsto \alpha \circ v$

$$
(i)  \operatorname{Hom}_{T}(\eta',\eta) \to \operatorname{Hom}_{f}(\eta',\xi)
$$

is bijective. It also means that the pair $(\eta,\alpha)$ **represents, as a functor in $\eta'$**, the functor
$\mathcal{F}^{\circ}_{T} \to Set$ given by the second member.

If, for a given morphism $f: T \to S$ in $\mathcal{E}$ and a given $\xi \in Ob(\mathcal{F}_{S})$, such a pair
$(\eta,\alpha)$ exists, i.e. a cartesian morphism $\alpha$ in $\mathcal{F}$ with target $\xi$ and with $p(\alpha) = f$,
then $\eta$ is determined in $\mathcal{F}_{T}$ up to unique isomorphism. One then says that **the inverse image of $\xi$
by $f$ exists**, and an object $\eta$ of $\mathcal{F}_{T}$ endowed with a cartesian $f$-morphism $\alpha: \eta \to \xi$
is called **an inverse image of $\xi$ by $f$**.

<!-- original page 162 -->

Often, once $\mathcal{F}$ is fixed, one assumes such an inverse image chosen whenever it exists. The inverse image will
then be denoted by symbols such as $f*_{\mathcal{F}}(\xi)$, or simply $f*(\xi)$, or $\xi \times_{S} T$ when these
notations cause no confusion. In what follows, the canonical morphism $\alpha: \eta \to \xi$ will then be denoted
$\alpha_{f}(\xi)$.

If for every $\xi \in Ob(\mathcal{F}_{S})$ the inverse image of $\xi$ by $f$ exists, one also says that **the
inverse-image functor by $f$ in $\mathcal{F}$ exists**, and $f*(\xi)$ then becomes a **covariant functor in $\xi$**,
from $\mathcal{F}_{S}$ to $\mathcal{F}_{T}$. This comes from the fact that the second member in (i) depends covariantly
on $\xi$, or more precisely denotes a functor from $\mathcal{F}^{\circ}_{T} \times \mathcal{F}_{S}$ to `Set`.

This functorial dependence of $f*(\xi)$ is made explicit as follows. Consider cartesian $f$-morphisms

```text
α: η → ξ,    α′: η′ → ξ′
```

and an $S$-morphism $\lambda: \xi \to \xi'$. Then there exists a unique $T$-morphism $\mu: \eta \to \eta'$ such that

```text
α′ μ = λ α,
```

as follows from the fact that $\alpha'$ is cartesian.

Also note the following immediate fact. Consider a commutative diagram in $\mathcal{F}$

```text
η  --α-->  ξ
|         |
μ         λ
↓         ↓
η′ --α′-> ξ′
```

<!-- original page 163 -->

where $\alpha$ and $\alpha'$ are $f$-morphisms, $\lambda$ is an $S$-isomorphism, and $\mu$ is a $T$-isomorphism. **Then
$\alpha$ is cartesian if and only if $\alpha'$ is cartesian**.

**Definition.**

<!-- label: VI.5.2 -->

An $\mathcal{E}$-functor $F: \mathcal{F} \to \mathcal{G}$ is called a **cartesian functor** if it transforms cartesian
morphisms into cartesian morphisms. We denote by `Hom̲_cart(ℱ,𝒢)` the full subcategory of `Hom̲_{ℰ/-}(ℱ,𝒢)` formed by the
cartesian functors.

For example, regarding $\mathcal{E}$ as a category over $\mathcal{E}$ by means of the identity functor, every morphism
of $\mathcal{E}$ is cartesian. Thus a cartesian functor from $\mathcal{E}$ to $\mathcal{F}$ is a section functor
$F: \mathcal{E} \to \mathcal{F}$ that transforms every morphism of $\mathcal{E}$ into a cartesian morphism. Such a
functor is called a **cartesian section** of $\mathcal{F}$ over $\mathcal{E}$.

**Proposition.**

<!-- label: VI.5.3 -->

1. A functor $F: \mathcal{F} \to \mathcal{G}$ that is an $\mathcal{E}$-equivalence is a cartesian functor.
1. Let $F$, $G$ be two **isomorphic** $\mathcal{E}$-functors $\mathcal{F} \to \mathcal{G}$. If one is cartesian, then so
   is the other.
1. The composite of two cartesian functors $\mathcal{F} \to \mathcal{G}$ and $\mathcal{G} \to \mathcal{H}$ is a
   cartesian functor.

Assertion (3) is trivial from the definition; (2) follows from the remark preceding VI.5.2; (1) follows easily from the
definition and criterion VI.4.2 (3). More precisely, a morphism $\alpha$ in $\mathcal{F}$ is cartesian if and only if
$F(\alpha)$ is cartesian.

**Corollary.**

<!-- label: VI.5.4 -->

Let $F: \mathcal{F} \to \mathcal{G}$ be an $\mathcal{E}$-equivalence. Then for every category $\mathcal{H}$ over
$\mathcal{E}$, the corresponding functors $G \mapsto G \circ F$ and $G \mapsto F \circ G$ induce equivalences of
categories:

```text
Hom̲_cart(𝒢,ℋ) ≃ Hom̲_cart(ℱ,ℋ),
Hom̲_cart(ℋ,ℱ) ≃ Hom̲_cart(ℋ,𝒢).
```

This follows in the usual way from criterion VI.4.2 (1) and from VI.5.3 (1), (2), (3).

<!-- original page 164 -->

One can specify that **the $\mathcal{E}$-functor $G: \mathcal{G} \to \mathcal{H}$ is cartesian if and only if
$G \circ F$ is cartesian**, and likewise **an $\mathcal{E}$-functor $G: \mathcal{H} \to \mathcal{F}$ is cartesian if and
only if $F \circ G$ is cartesian**.

It follows from VI.5.4 (3) that, if one considers the subcategory $Cat^{cart}_{/}\mathcal{E}$ of $Cat_{/}\mathcal{E}$
whose objects are the same as those of $Cat_{/}\mathcal{E}$ and whose morphisms are the **cartesian** functors, then, as
in VI.2, one has pairings

```text
Hom̲_cart(ℱ,𝒢) × Hom̲_cart(𝒢,ℋ) → Hom̲_cart(ℱ,ℋ)
```

induced by those of VI.2. These pairings allow one to regard `Hom̲_cart(ℱ,𝒢)` as a functor in $\mathcal{F}$ and
$\mathcal{G}$, from the category `(Cat^cart_/ℰ)° × Cat^cart_/ℰ` to `Cat`. We shall need this remark chiefly in the case
$\mathcal{F} = \mathcal{G}$.

**Definition.**

<!-- label: VI.5.5 -->

Let $\mathcal{F}$ be a category over $\mathcal{E}$. We denote by

$$
Lim\leftarrow(\mathcal{F}/\mathcal{E})
$$

the category of cartesian $\mathcal{E}$-functors $\mathcal{E} \to \mathcal{F}$, i.e. the cartesian sections of
$\mathcal{F}$ over $\mathcal{E}$.

By what has just been said, $Lim\leftarrow(\mathcal{F}/\mathcal{E})$ is a functor in $\mathcal{F}$, from the category
$Cat^{cart}_{/}\mathcal{E}$ to the category `Cat`.

We shall see below the relations between this operation $Lim\leftarrow$ and the notion of projective limit of
categories, as well as numerous examples.

## 6. Fibered Categories and Prefibered Categories. Products and Base Change in Them

<!-- label: VI.6 -->

**Definition.**

<!-- label: VI.6.1 -->

A category $\mathcal{F}$ over $\mathcal{E}$ is called a **fibered category**, and the functor
$\mathcal{F} \to \mathcal{E}$ is then said to be **fibrant**, if it satisfies the two following axioms:

**Fib I.** For every morphism $f: T \to S$ in $\mathcal{E}$, the inverse-image functor by $f$ in $\mathcal{F}$ exists.

**Fib II.** The composite of two cartesian morphisms is cartesian.

A category $\mathcal{F}$ over $\mathcal{E}$ satisfying condition **Fib I** is called a **prefibered category over
$\mathcal{E}$**.

If $\mathcal{F}$ is a fibered, respectively prefibered, category over $\mathcal{E}$, a subcategory $\mathcal{G}$ of
$\mathcal{F}$ is called a **fibered subcategory**, respectively a **prefibered subcategory**, if it is a fibered,
respectively prefibered, category over $\mathcal{E}$ and, moreover, the inclusion functor is cartesian. If, for example,
$\mathcal{G}$ is a **full** subcategory of $\mathcal{F}$, one sees that this means that, for every morphism $f: T \to S$
in $\mathcal{E}$ and every $\xi \in Ob(\mathcal{G}_{S})$, $f*_{\mathcal{F}}(\xi)$ is $T$-isomorphic to an object of
$\mathcal{G}_{T}$.

Another interesting case is the following. Let $\mathcal{F}$ be a fibered category over $\mathcal{E}$, and consider the
subcategory $\mathcal{G}$ of $\mathcal{F}$ with the same objects and whose morphisms are the **cartesian** morphisms of
$\mathcal{F}$; in particular the morphisms of $\mathcal{G}_{S}$ are the isomorphisms of $\mathcal{F}_{S}$. One sees at
once that this is indeed a fibered subcategory of $\mathcal{F}$, because in the bijection

<!-- original page 165 -->

$$
\operatorname{Hom}_{T}(\eta',\eta) \simeq \operatorname{Hom}_{f}(\eta',\xi)
$$

relative to a cartesian $f$-morphism $\alpha$ in $\mathcal{F}$, the $T$-isomorphisms of the first member correspond to
the cartesian morphisms of the second. By definition, the cartesian sections $\mathcal{E} \to \mathcal{F}$ then
correspond bijectively to arbitrary $\mathcal{E}$-functors $\mathcal{E} \to \mathcal{G}$. However, note that the natural
functor

```text
Hom̲_{ℰ/-}(ℰ,𝒢) → Hom̲_cart(ℰ,ℱ) = Lim←(ℱ/ℰ)
```

is faithful, but in general is not fully faithful, i.e. is not an isomorphism.

**Remarks.** Let $\mathcal{F}$ be a category over $\mathcal{E}$. The following conditions are equivalent:

1. All morphisms of $\mathcal{F}$ are cartesian.
1. $\mathcal{F}$ is a fibered category over $\mathcal{E}$, and the $\mathcal{F}_{S}$ are groupoids, i.e. every morphism
   in $\mathcal{F}_{S}$ is an isomorphism.

One then says that $\mathcal{F}$ is a category **fibered in groupoids** over $\mathcal{E}$.

<!-- original page 166 -->

These are the ones encountered especially in “theory of moduli”. If $\mathcal{E}$ is a groupoid, one shows that
conditions (1) and (2) are also equivalent to the following:

1. $\mathcal{F}$ is a groupoid, and the projection functor $p: \mathcal{F} \to \mathcal{E}$ is transportable; cf.
   VI.4.4.

For example, if $\mathcal{E}$ and $\mathcal{F}$ are groupoids such that $Ob(\mathcal{E})$ and $Ob(\mathcal{F})$ are
reduced to a point, so that $\mathcal{E}$ and $\mathcal{F}$ are defined, up to isomorphism, by groups $E$ and $F$, and
the functor $p: \mathcal{F} \to \mathcal{E}$ is defined by a group homomorphism $p: F \to E$, then $\mathcal{F}$ is
fibered over $\mathcal{E}$ if and only if $p$ is surjective, i.e. if $p$ defines an **extension** of the group $E$ by
the group $G = Ker p$.

**Proposition.**

<!-- label: VI.6.2 -->

Let $F: \mathcal{F} \to \mathcal{G}$ be an $\mathcal{E}$-equivalence. In order that $\mathcal{F}$ be a fibered,
respectively prefibered, category over $\mathcal{E}$, it is necessary and sufficient that $\mathcal{G}$ be so.

This follows easily from the definitions and from the remark made above that a morphism $\alpha$ in $\mathcal{F}$ is
cartesian if and only if $F(\alpha)$ is.

**Proposition.**

<!-- label: VI.6.3 -->

Let $\mathcal{F}_{1}$, $\mathcal{F}_{2}$ be two categories over $\mathcal{E}$, and let
$\alpha = (\alpha_{1},\alpha_{2})$ be a morphism in
$\mathcal{F} = \mathcal{F}_{1} \times_{\mathcal{E}} \mathcal{F}_{2}$. Then $\alpha$ is cartesian if and only if its
components are cartesian.

Indeed, let $\xi_{i}$ be the target and $\eta_{i}$ the source of $\alpha_{i}$, and let $f: T \to S$ be the morphism of
$\mathcal{E}$ such that $\alpha_{1}$ and $\alpha_{2}$ are $f$-morphisms. For every $\eta' = (\eta'_{1},\eta'_{2})$ in
$\mathcal{F}_{T}$, one has a commutative diagram

$$
\operatorname{Hom}_{T}(\eta',\eta)  \to  \operatorname{Hom}_{f}(\eta',\xi)
     \downarrow              \downarrow
\operatorname{Hom}_{T}(\eta'_{1},\eta_{1}) \times \operatorname{Hom}_{T}(\eta'_{2},\eta_{2})
  \to \operatorname{Hom}_{f}(\eta'_{1},\xi_{1}) \times \operatorname{Hom}_{f}(\eta'_{2},\xi_{2}),
$$

where the vertical arrows are bijections. Thus if one of the horizontal arrows is a bijection, the same is true of the
other. This already shows that if $\alpha_{1}$ and $\alpha_{2}$ are cartesian, hence the second horizontal arrow is
bijective, then $\alpha$ is cartesian. The converse is seen by taking, in the diagram above, $\eta'_{i} = \eta_{i}$,
whence $\operatorname{Hom}_{T}(\eta'_{i},\eta_{i}) \neq \emptyset$: first for $i = 2$, which proves that $\alpha_{1}$ is
cartesian, then for $i = 1$, which proves that $\alpha_{2}$ is cartesian.

**Corollary.**

<!-- label: VI.6.4 -->

<!-- original page 167 -->

Let $\mathcal{F} = \mathcal{F}_{1} \times_{\mathcal{E}} \mathcal{F}_{2}$, and let $F = (F_{1},F_{2})$ be an
$\mathcal{E}$-functor $\mathcal{G} \to \mathcal{F}$. Then $F$ is cartesian if and only if $F_{1}$ and $F_{2}$ are
cartesian. One obtains in this way an isomorphism of categories

```text
Hom̲_cart(𝒢, ℱ₁ ×_ℰ ℱ₂) ≃ Hom̲_cart(𝒢,ℱ₁) × Hom̲_cart(𝒢,ℱ₂),
```

and in particular, taking $\mathcal{G} = \mathcal{E}$, an isomorphism of categories

```text
Lim←((ℱ₁ ×_ℰ ℱ₂)/ℰ) ≃ Lim←(ℱ₁/ℰ) × Lim←(ℱ₂/ℰ).
```

**Corollary.**

<!-- label: VI.6.5 -->

Let $\mathcal{F}_{1}$ and $\mathcal{F}_{2}$ be two fibered, respectively prefibered, categories over $\mathcal{E}$. Then
their fiber product $\mathcal{F} = \mathcal{F}_{1} \times_{\mathcal{E}} \mathcal{F}_{2}$ is a fibered, respectively
prefibered, category over $\mathcal{E}$.

These results moreover extend to the case of the fiber product of an arbitrary family of categories over $\mathcal{E}$.

**Proposition.**

<!-- label: VI.6.6 -->

Let $\mathcal{F}$ be a category over $\mathcal{E}$, with projection functor $p$, and let
$\lambda: \mathcal{E}' \to \mathcal{E}$ be a functor. Regard
$\mathcal{F}' = \mathcal{F} \times_{\mathcal{E}} \mathcal{E}'$ as a category over $\mathcal{E}'$ by the projection
functor $p' = p \times_{\mathcal{E}} id_{\mathcal{E}}'$. Let $\alpha'$ be a morphism of $\mathcal{F}'$. Then $\alpha'$
is a cartesian morphism if and only if its image $\alpha$ in $\mathcal{F}$ is cartesian.

The proof is immediate and is left to the reader.

**Corollary.**

<!-- label: VI.6.7 -->

For every cartesian functor $F: \mathcal{F} \to \mathcal{G}$ of categories over $\mathcal{E}$, the functor

```text
F′ = F ×_ℰ ℰ′
```

from $\mathcal{F}' = \mathcal{F} \times_{\mathcal{E}} \mathcal{E}'$ to
$\mathcal{G}' = \mathcal{G} \times_{\mathcal{E}} \mathcal{E}'$ is cartesian.

Consequently, the functor `Hom̲_ℰ(ℱ,𝒢) → Hom̲_ℰ′(ℱ′,𝒢′)` considered in VI.3 induces a functor

```text
Hom̲_cart(ℱ,𝒢) → Hom̲_cart(ℱ′,𝒢′).
```

In other words, for fixed $\mathcal{F}$ and $\mathcal{G}$, **one may regard**

```text
Hom̲_cart(ℱ ×_ℰ ℰ′, 𝒢 ×_ℰ ℰ′)
```

<!-- original page 168 -->

**as a functor in $\mathcal{E}'$, from the category $Cat_{/}\mathcal{E}^{\circ}$ to `Cat`**. If $\mathcal{F}$ and
$\mathcal{G}$ are also allowed to vary, one finds a functor from the category

```text
Cat_/ℰ° × (Cat^cart_/ℰ)° × Cat^cart_/ℰ
```

to `Cat`.

When one takes into account the isomorphism

```text
Hom_ℰ′(ℱ′,𝒢′) ≃ Hom_ℰ(ℱ ×_ℰ ℰ′,𝒢)
```

considered in VI.3, the cartesian $\mathcal{E}'$-functors from $\mathcal{F}'$ to $\mathcal{G}'$ correspond to the
$\mathcal{E}$-functors $\mathcal{F} \times_{\mathcal{E}} \mathcal{E}' \to \mathcal{G}$ that transform every morphism
whose first projection is a cartesian morphism of $\mathcal{F}$ into a cartesian morphism of $\mathcal{G}$. Taking
$\mathcal{F} = \mathcal{E}$, one finds, after a change of notation:

**Corollary.**

<!-- label: VI.6.8 -->

$Lim\leftarrow(\mathcal{F}'/\mathcal{E}')$ is isomorphic to the full subcategory of `Hom̲_{ℰ/-}(ℰ′,ℱ)` formed by the
$\mathcal{E}$-functors $\mathcal{E}' \to \mathcal{F}$ that transform arbitrary morphisms into cartesian morphisms. In
particular, if $\mathcal{F}$ is a fibered category and if $\tilde{\mathcal{F}}$ is the subcategory of $\mathcal{F}$
whose morphisms are the cartesian morphisms of $\mathcal{F}$, then one has a bijection

$$
Ob Lim\leftarrow(\mathcal{F}'/\mathcal{E}') \simeq \operatorname{Hom}_{\mathcal{E}/-}(\mathcal{E}',\tilde{\mathcal{F}}).
$$

This makes precise the way in which the expression

$$
Lim\leftarrow((\mathcal{F} \times_{\mathcal{E}} \mathcal{E}')/\mathcal{E}')
$$

must be regarded as a functor in $\mathcal{E}'$ and $\mathcal{F}$, from the category `Cat_/ℰ° × Cat^cart_/ℰ` to the
category `Cat`. Later we shall see a more complete functorial dependence with respect to $\mathcal{E}'$ when
$\mathcal{F}$ is required to be a fibered category.

**Corollary.**

<!-- label: VI.6.9 -->

If $\mathcal{F}$ is a fibered, respectively prefibered, category over $\mathcal{E}$, then
$\mathcal{F}' = \mathcal{F} \times_{\mathcal{E}} \mathcal{E}'$ is a fibered, respectively prefibered, category over
$\mathcal{E}'$.

**Proposition.**

<!-- label: VI.6.10 -->

Let $\mathcal{F}$ and $\mathcal{G}$ be prefibered categories over $\mathcal{E}$, and let $F$ be a cartesian
$\mathcal{E}$-functor from $\mathcal{F}$ to $\mathcal{G}$. In order that $F$ be faithful, respectively fully faithful,
respectively an $\mathcal{E}$-equivalence, it is necessary and sufficient that for every $S \in Ob(\mathcal{E})$, the
induced functor

<!-- original page 169 -->

$$
F_{S}: \mathcal{F}_{S} \to \mathcal{G}_{S}
$$

be faithful, respectively fully faithful, respectively an equivalence.

The proof is immediate from the definitions.

To finish this number, we give a few properties of fibered categories using axiom **Fib II**.

**Proposition.**

<!-- label: VI.6.11 -->

Let $\mathcal{F}$ be a prefibered category over $\mathcal{E}$. In order that $\mathcal{F}$ be fibered, it is necessary
and sufficient that it satisfy the following condition:

**Fib II′.** Let $\alpha: \eta \to \xi$ be a cartesian morphism in $\mathcal{F}$ over the morphism $f: T \to S$ of
$\mathcal{E}$. For every morphism $g: U \to T$ in $\mathcal{E}$, and every $\zeta \in Ob(\mathcal{F}_{U})$, the map
$u \mapsto \alpha \circ u$

$$
\operatorname{Hom}_{g}(\zeta,\eta) \to \operatorname{Hom}_{fg}(\zeta,\xi)
$$

is bijective.

In other words, in a category **fibered** over $\mathcal{E}$, cartesian diagrams are characterized by a property a
priori stronger than the one in the definition, which is recovered by taking $g = id_{T}$ in the preceding statement.

**Corollary.**

<!-- label: VI.6.12 -->

Let $\mathcal{F}$ be a category over $\mathcal{E}$ and let $\alpha$ be a morphism in $\mathcal{F}$. In order that
$\alpha$ be an isomorphism, it is necessary that $p(\alpha) = f$ be an isomorphism and that $\alpha$ be cartesian. The
converse is true if $\mathcal{F}$ is fibered over $\mathcal{E}$.

Indeed, if $\alpha$ is an isomorphism then evidently so is $f = p(\alpha)$. For every $\eta' \in Ob(\mathcal{F}_{T})$,
the map $u \mapsto \alpha \circ u$

$$
\operatorname{Hom}(\eta',\eta) \to \operatorname{Hom}(\eta',\xi)
$$

is bijective. Since $f$ is an isomorphism, one sees at once that an element of the first member is a $T$-morphism if and
only if its image in the second is an $f$-morphism. Thus one obtains a bijection

$$
\operatorname{Hom}_{T}(\eta',\eta) \to \operatorname{Hom}_{f}(\eta',\xi),
$$

<!-- original page 170 -->

which proves the first assertion. Conversely, suppose that $f$ is an isomorphism and that $\alpha$ satisfies the
condition stated in **Fib II′**, which means, when $\mathcal{F}$ is fibered over $\mathcal{E}$, that $\alpha$ is
cartesian. Then one sees at once that for every $\zeta \in Ob(\mathcal{F})$, the map $u \mapsto \alpha \circ u$ from
$\operatorname{Hom}(\zeta,\eta)$ to $\operatorname{Hom}(\zeta,\xi)$ is bijective, and hence $\alpha$ is an isomorphism.

**Corollary.**

<!-- label: VI.6.13 -->

Let $\alpha: \eta \to \xi$ and $\beta: \zeta \to \eta$ be two composable morphisms in the category $\mathcal{F}$ fibered
over $\mathcal{E}$. If $\alpha$ is cartesian, then $\beta$ is cartesian if and only if $\alpha \beta$ is cartesian.

One uses the definition of cartesian morphisms in the strengthened form VI.6.11.

## 7. Categories Cloven over ℰ

<!-- label: VI.7 -->

**Definition.**

<!-- label: VI.7.1 -->

Let $\mathcal{F}$ be a category over $\mathcal{E}$. A **cleavage** of $\mathcal{F}$ over $\mathcal{E}$ means a function
that attaches to every $f \in Fl(\mathcal{E})$ an inverse-image functor for $f$ in $\mathcal{F}$, denoted $f*$. The
cleavage is said to be **normalized** if $f = id_{S}$ implies $f* = id_{\mathcal{F}_{S}}$. A **cloven category**,
respectively a **normalized cloven category**, means a category $\mathcal{F}$ over $\mathcal{E}$ endowed with a
cleavage, respectively with a normalized cleavage.

It is evident that $\mathcal{F}$ admits a cleavage if and only if $\mathcal{F}$ is prefibered over $\mathcal{E}$, and
then $\mathcal{F}$ admits a normalized cleavage. The set of cleavages on $\mathcal{F}$ is in bijective correspondence
with the set of subsets $K$ of $Fl(\mathcal{F})$ satisfying the following conditions:

1. The $\alpha \in K$ are cartesian morphisms.
1. For every morphism $f: T \to S$ in $\mathcal{E}$ and every $\xi \in Ob(\mathcal{F}_{S})$, there exists a unique
   $f$-morphism in $K$ with target $\xi$.

For the cleavage defined by $K$ to be normalized, it is necessary and sufficient that $K$ also satisfy the condition:

1. The identity morphisms in $\mathcal{F}$ belong to $K$.

<!-- original page 171 -->

The morphisms that are elements of $K$ may be called the **“transport morphisms”** for the cleavage in question.

The notion of isomorphism of cloven categories over $\mathcal{E}$ is clear. More generally, one can define morphisms of
cloven $\mathcal{E}$-categories as functors of $\mathcal{E}$-categories $\mathcal{F} \to \mathcal{G}$ that send
transport morphisms to transport morphisms. These are, in particular, cartesian functors. In this way the cloven
categories over $\mathcal{E}$ are the objects of a category, the **category of cloven categories over $\mathcal{E}$**.
The reader may spell out the existence of products, tied to the fact that if a category over $\mathcal{E}$ is the
product of categories $\mathcal{F}_{i}$ over $\mathcal{E}$, each endowed with a cleavage, then $\mathcal{F}$ is endowed
with the corresponding natural cleavage. We also leave to the reader the task of spelling out the notion of base change
in cloven categories.

We shall denote by $\alpha_{f}(\xi)$ the canonical morphism

$$
\alpha_{f}(\xi): f*(\xi) \to \xi.
$$

As was said, it is functorial in $\xi$, i.e. one has a functorial homomorphism

```text
α_f: i_T f* → i_S,
```

where for every $S \in Ob(\mathcal{E})$, $i_{S}$ denotes the inclusion functor

$$
i_{S}: \mathcal{F}_{S} \to \mathcal{F}.
$$

Now consider morphisms

```text
f: T → S    and    g: U → T
```

in $\mathcal{E}$, and let $\xi \in Ob(\mathcal{F}_{S})$. There then exists a unique $U$-morphism

$$
c_{f,g}(\xi): g*f*(\xi) \to (fg)*(\xi)
$$

making commutative

<!-- original page 172 -->

the diagram

$$
g*f*(\xi) --\alpha_{g}(f*(\xi))--> f*(\xi)
   | c_{f,g}(\xi)           | \alpha_{f}(\xi)
   \downarrow                      \downarrow
(fg)*(\xi) --\alpha_{fg}(\xi)-->   \xi,
$$

by the definition of $(fg)*(\xi)$. For variable $\xi$, this homomorphism is functorial; that is, one has a homomorphism

$$
c_{f,g}: g*f* \to (fg)*
$$

of functors $\mathcal{F}_{S} \to \mathcal{F}_{U}$. Note at once:

**Proposition.**

<!-- label: VI.7.2 -->

In order that the cloven category $\mathcal{F}$ over $\mathcal{E}$ be fibered, it is necessary and sufficient that the
$c_{f,g}$ be isomorphisms.

It follows, taking $f$ to be an isomorphism and $g$ its inverse, and considering the isomorphisms $c_{f,g}$ and
$c_{g,f}$:

**Corollary.**

<!-- label: VI.7.3 -->

If $\mathcal{F}$ is a **fibered** cloven category over $\mathcal{E}$, then for every isomorphism $f: T \to S$ in
$\mathcal{E}$, $f*$ is an equivalence of categories $\mathcal{F}_{S} \to \mathcal{F}_{T}$.

**Proposition.**

<!-- label: VI.7.4 -->

Let $\mathcal{F}$ be a cloven category over $\mathcal{E}$. One has:

```text
A)
  c_{f,id_T}(ξ) = α_{id_T}(f*(ξ)),
  c_{id_S,f}(ξ) = f*(α_{id_S}(ξ)).
```

and

```text
B)  c_{f,gh}(ξ) · c_{g,h}(f*(ξ))
      = c_{fg,h}(ξ) · h*(c_{f,g}(ξ)).
```

In these formulas, $f$, $g$, $h$ denote morphisms

```text
V → U → T → S
```

<!-- original page 173 -->

and $\xi$ is an object of $\mathcal{F}_{S}$.

In the case of a normalized cleavage, the first and second relations take the simpler form

```text
A′) c_{f,id_T} = id_{f*},    c_{id_S,f} = id_{f*}.
```

As for the third, it is visualized by the commutativity of the diagram

$$
h*g*f*(\xi) --c_{g,h}(f*(\xi))--> (gh)*f*(\xi)
    | h*(c_{f,g}(\xi))              | c_{f,gh}(\xi)
    \downarrow                             \downarrow
h*(fg)*(\xi) --c_{fg,h}(\xi)-->    (fgh)*(\xi).
$$

In the case of fibered categories, where the $c_{f,g}$ are isomorphisms, this commutativity may be expressed intuitively
by saying that **the successive use of isomorphisms of the form $c_{f,g}$ does not lead to “contradictory
identifications.”** One may also write this formula without the argument $\xi$, using the convolution product of
homomorphisms of functors:

```text
c_{fg,h} ∘ (h* ∗ c_{f,g}) = c_{f,gh} ∘ (c_{g,h} ∗ f*).
```

The proof of the first two formulas in VI.7.4 is trivial; let us sketch that of the third. For this, consider, in
addition to the square `(D)`, the square of homomorphisms

$$
g*f*(\xi) --\alpha_{g}(f*(\xi))--> f*(\xi)
   | c_{f,g}(\xi)            | \alpha_{f}(\xi)
   \downarrow                       \downarrow
(fg)*(\xi) --\alpha_{fg}(\xi)-->    \xi,
$$

<!-- original page 174 -->

which is commutative by definition of $c_{f,g}(\xi)$. Consider the diagram obtained by joining the vertices of `(D)` to
the corresponding vertices of this square by homomorphisms of the form $\alpha$:

$$
\alpha_{h}(g*f*(\xi)),       \alpha_{gh}(f*(\xi)),
\alpha_{h}((fg)*(\xi)),      \alpha_{fgh}(\xi).
$$

The four lateral faces of the cube so obtained are also commutative. For the left face, this comes from the fact that
the left column of `(D)` is obtained from the left column of the preceding square by applying $h$, and that $\alpha_{h}$
is a functorial homomorphism. For the other three faces, this is nothing other than the definition of the operations $c$
on the remaining three sides of `(D)`. Thus the five faces of the cube other than the upper face are commutative. It
follows that the two `(fgh)`-morphisms $h*g*f*(\xi) \to (fgh)*(\xi)$ defined by `(D)` have the same composite with
$\alpha_{fgh}(\xi): (fgh)*(\xi) \to \xi$. Hence they are equal by the definition of $(fgh)*$.

Let us confine ourselves, in what follows, to **normalized** cloven categories. Such a category gives rise to the
following objects:

1. A map $S \mapsto \mathcal{F}_{S}$ from $Ob(\mathcal{E})$ to `Cat`.
1. A map $f \mapsto f*$, associating to every $f \in Fl(\mathcal{E})$, with source $T$ and target $S$, a functor
   $f*: \mathcal{F}_{S} \to \mathcal{F}_{T}$.
1. A map $(f,g) \mapsto c_{f,g}$, associating to every pair of arrows $(f,g)$ of $\mathcal{E}$ a functorial homomorphism
   $c_{f,g}: g*f* \to (fg)*$.

Moreover, these data satisfy the conditions expressed in formulas A′) and B) above. N.B. If one had not confined oneself
to the case of a normalized cleavage, one would have had to introduce an additional object, namely a function
$S \mapsto \alpha_{S}$ associating to every object $S$ of $\mathcal{E}$ a functorial homomorphism
$\alpha_{S}: (id_{S})* \to id_{\mathcal{F}_{S}}$; condition A′) would then be replaced by condition A).

<!-- original page 175 -->

We shall now show how one can reconstruct, up to unique isomorphism, the normalized cloven category $\mathcal{F}$ over
$\mathcal{E}$ from the preceding objects.

## 8. Cloven Category Defined by a Pseudofunctor ℰ° → Cat

<!-- label: VI.8 -->

For short, call a **pseudofunctor** from $\mathcal{E}^{\circ}$ to `Cat`, one should say a **normalized** pseudofunctor,
a set of data a), b), c) as above, satisfying conditions A′) and B). In the preceding number we associated to a
normalized cloven category over $\mathcal{E}$ a pseudofunctor $\mathcal{E}^{\circ} \to Cat$. Here we indicate the
inverse construction. We shall leave to the reader the verification of most of the details, as well as of the fact that
these constructions are indeed “inverse” to one another. More precisely, one should regard the pseudofunctors
$\mathcal{E}^{\circ} \to Cat$ as the objects of a new category, and show that our constructions provide equivalences,
quasi-inverse to one another, between this latter category and the category of cloven categories over $\mathcal{E}$
defined in the preceding number.

Put

$$
\mathcal{F}^{\circ} = \coprod_{S\in Ob(\mathcal{E})} Ob(\mathcal{F}(S)),
$$

the sum set of the sets $Ob(\mathcal{F}(S))$. N.B. here we write $\mathcal{F}(S)$, and not $\mathcal{F}_{S}$, for the
value at the object $S$ of $\mathcal{E}$ of the given pseudofunctor, to avoid notational confusion later. We therefore
have an evident map

$$
p^{\circ}: \mathcal{F}^{\circ} \to Ob(\mathcal{E}).
$$

Let

```text
ξ̄ = (S,ξ),    η̄ = (T,η),    with ξ ∈ Ob(ℱ(S)), η ∈ Ob(ℱ(T)),
```

be two elements of $\mathcal{F}^{\circ}$, and let $f \in \operatorname{Hom}(T,S)$. Put

$$
h_{f}(\bar{\eta},\bar{\xi}) = \operatorname{Hom}_{\mathcal{F}(T)}(\eta, f*(\xi)).
$$

<!-- original page 176 -->

If in addition one has a morphism $g: U \to T$ in $\mathcal{E}$ and $\zeta \in Ob(\mathcal{F}(U))$, one defines a map,
denoted $(u,v) \mapsto u \circ v$,

$$
h_{f}(\bar{\eta},\bar{\xi}) \times h_{g}(\bar{\zeta},\bar{\eta}) \to h_{fg}(\bar{\zeta},\bar{\xi}),
$$

i.e. a map

```text
Hom_{ℱ(T)}(η, f*(ξ)) × Hom_{ℱ(U)}(ζ, g*(η))
  → Hom_{ℱ(U)}(ζ, (fg)*(ξ)),
```

by the formula

```text
u ∘ v = c_{f,g}(ξ) · g*(u) · v.
```

That is, $u \circ v$ is the composite of the sequence

```text
ζ --v--> g*(η) --g*(u)--> g*f*(ξ) --c_{f,g}(ξ)--> (fg)*(ξ).
```

On the other hand, put

$$
h(\bar{\eta},\bar{\xi}) = \coprod_{f\in \operatorname{Hom}(T,S)} h_{f}(\bar{\eta},\bar{\xi}).
$$

The preceding pairings define pairings

$$
h(\bar{\eta},\bar{\xi}) \times h(\bar{\zeta},\bar{\eta}) \to h(\bar{\zeta},\bar{\xi}),
$$

while the definition of the $h(\bar{\eta},\bar{\xi})$ gives an evident map

$$
p_{\bar{\eta},\bar{\xi}}: h(\bar{\eta},\bar{\xi}) \to \operatorname{Hom}(T,S).
$$

This being said, one verifies the following points:

1. Composition between elements of the $h(\bar{\eta},\bar{\xi})$ is **associative**.

1. For every $\bar{\xi} = (S,\xi)$ in $\mathcal{F}^{\circ}$, consider the identity element of

<!-- original page 177 -->

$$
h_{id_{S}}(\bar{\xi},\bar{\xi}) = \operatorname{Hom}_{\mathcal{F}(S)}(id_{S}*(\xi),\xi) = \operatorname{Hom}_{\mathcal{F}(S)}(\xi,\xi),
$$

and its image in $h(\bar{\xi},\bar{\xi})$. This object is a **left and right unit** for composition between elements of
the $h(\bar{\eta},\bar{\xi})$.

This already shows that **one obtains a category** $\mathcal{F}$ by putting

$$
Ob(\mathcal{F}) = \mathcal{F}^{\circ},
Fl(\mathcal{F}) = \coprod_{\bar{\xi},\bar{\eta}\in \mathcal{F}^{\circ}} h(\bar{\eta},\bar{\xi}).
$$

N.B. one cannot simply take $Fl(\mathcal{F})$ to be the **union** of the sets $h(\bar{\eta},\bar{\xi})$, since these
latter sets are not necessarily disjoint. Moreover:

1. The maps $p^{\circ}: Ob(\mathcal{F}) \to Ob(\mathcal{E})$ and
   $p_{1} = (p_{\bar{\eta},\bar{\xi}}): Fl(\mathcal{F}) \to Fl(\mathcal{E})$ define a **functor**
   $p: \mathcal{F} \to \mathcal{E}$. In this way $\mathcal{F}$ becomes a category over $\mathcal{E}$; moreover, the
   evident map $h_{f}(\bar{\eta},\bar{\xi}) \to \operatorname{Hom}(\bar{\eta},\bar{\xi})$ induces a **bijection**

$$
h_{f}(\bar{\eta},\bar{\xi}) \simeq \operatorname{Hom}_{f}(\bar{\eta},\bar{\xi}).
$$

1. The evident maps

```text
Ob(ℱ(S)) → ℱ° = Ob(ℱ),    Fl(ℱ(S)) → Fl(ℱ),
```

where the second is defined by the evident maps

$$
\operatorname{Hom}_{\mathcal{F}(S)}(\xi,\xi') = h_{id_{S}}(\bar{\xi},\bar{\xi}') \to \operatorname{Hom}(\bar{\xi},\bar{\xi}'),
$$

define an **isomorphism**

$$
i_{S}: \mathcal{F}(S) \simeq \mathcal{F}_{S}.
$$

1. For every object $\bar{\xi} = (S,\xi)$ of $\mathcal{F}$, and every morphism $f: T \to S$ of $\mathcal{E}$, consider

<!-- original page 178 -->

the element $\bar{\eta} = (T,\eta)$ of $\mathcal{F}_{T}$, with $\eta = f*(\xi)$, and the element $\alpha_{f}(\xi)$ of
$\operatorname{Hom}(\bar{\eta},\bar{\xi})$, image of $id_{f*(\xi)}$ by the morphism

$$
\operatorname{Hom}_{\mathcal{F}(T)}(f*(\xi),f*(\xi)) = h_{f}(\bar{\eta},\bar{\xi}) \to \operatorname{Hom}_{f}(\bar{\eta},\bar{\xi}).
$$

**This element is cartesian, and it is the identity of $\bar{\xi}$ if $f = id_{S}$**. In other words, the set of the
$\alpha_{f}(\xi)$ defines a **normalized cleavage of $\mathcal{F}$ over $\mathcal{E}$**. Moreover, by construction, one
has commutativity in the diagram of functors

$$
\mathcal{F}(S) --f*--> \mathcal{F}(T)
 | i_{S}        | i_{T}
 \downarrow            \downarrow
\mathcal{F}_{S} --f*_{\mathcal{F}}-> \mathcal{F}_{T},
$$

where $f*_{\mathcal{F}}$ is the inverse-image functor by $f$, relative to the cleavage considered on $\mathcal{F}$.
Finally:

1. The homomorphisms $c_{f,g}$ given with the pseudofunctor are transformed, by the isomorphisms $i_{S}$, into the
   functorial homomorphisms $c_{f,g}$ associated with the cleavage of $\mathcal{F}$.

We restrict ourselves to giving the verification of 1), which is, if anything, less trivial than the others. It suffices
to prove associativity of composition between objects of sets of the form $h_{f}(\bar{\eta},\bar{\xi})$. Thus consider
in $\mathcal{E}$ morphisms

```text
S ←^f T ←^g U ←^h V
```

and objects

```text
ξ, η, ζ, τ
```

in $\mathcal{F}(S)$, $\mathcal{F}(T)$, $\mathcal{F}(U)$, $\mathcal{F}(V)$, and finally elements

```text
u ∈ h_f(η̄,ξ̄) = Hom_{ℱ(T)}(η, f*(ξ)),
v ∈ h_g(ζ̄,η̄) = Hom_{ℱ(U)}(ζ, g*(η)),
w ∈ h_h(τ̄,ζ̄) = Hom_{ℱ(V)}(τ, h*(ζ)).
```

<!-- original page 179 -->

We want to prove the formula

```text
(u ∘ v) ∘ w = u ∘ (v ∘ w),
```

which is an equality in $\operatorname{Hom}_{\mathcal{F}(V)}(\tau,(fgh)*(\xi))$. By the definitions, the two members of
this equality are obtained by composition along the upper and lower contours of the diagram below:

```text
τ --w--> h*(ζ) --h*(v)--> h*g*(η) --h*g*(u)--> h*g*f*(ξ) --h*(c_{f,g}(ξ))--> h*(fg)*(ξ)
 \____________________ v∘w ____________________/       | c_{g,h}(f*(ξ))              | c_{fg,h}(ξ)
                         ↓                              ↓                             ↓
                  (gh)*(η) --(gh)*(u)-->        (gh)*f*(ξ) --c_{f,gh}(ξ)-->       (fgh)*(ξ).
```

The middle square is commutative because $c_{g,h}$ is a functorial homomorphism, and the square on the right is
commutative by condition B) for a pseudofunctor. This gives the asserted result.

Of course, it remains to specify, when the pseudofunctor considered already comes from a normalized cloven category
$\mathcal{F}'$ over $\mathcal{E}$, how one obtains a natural isomorphism between $\mathcal{F}'$ and $\mathcal{F}$. We
leave the details to the reader.

We likewise leave to the reader the interpretation, in terms of pseudofunctors, of the notion of inverse image of a
cloven category $\mathcal{F}$ over $\mathcal{E}$ by a base-change functor $\mathcal{E}' \to \mathcal{E}$.

## 9. Example: Cloven Category Defined by a Functor ℰ° → Cat; Split Categories over ℰ

<!-- label: VI.9 -->

Suppose one has a functor

$$
\phi: \mathcal{E}^{\circ} \to Cat.
$$

It then defines a pseudofunctor by putting

```text
ℱ(S) = φ(S),    f* = φ(f),    c_{f,g} = id_{(fg)*}.
```

<!-- original page 180 -->

Thus the construction of the preceding number gives us a category $\mathcal{F}$ cloven over $\mathcal{E}$, said to be
associated with the functor $\phi$. For a cloven category over $\mathcal{E}$ to be isomorphic to a cloven category
defined by a functor $\phi: \mathcal{E}^{\circ} \to Cat$, it is manifestly necessary and sufficient that it satisfy the
conditions

```text
(fg)* = g*f*,    c_{f,g} = id_{(fg)*}.
```

In terms of the set $K$ of transport morphisms, this also simply means that **the composite of two transport morphisms
is a transport morphism**. A cleavage of a category $\mathcal{F}$ over $\mathcal{E}$ satisfying the preceding condition
is called a **splitting** of $\mathcal{F}$ over $\mathcal{E}$, and a category $\mathcal{F}$ over $\mathcal{E}$ endowed
with a splitting is called a **split category over $\mathcal{E}$**. It is therefore a special case of the notion of
cloven category. The category of split categories over $\mathcal{E}$ is therefore equivalent to `Hom̲(ℰ°,Cat)`. Note that
a split category over $\mathcal{E}$ is a fortiori a cloven category over $\mathcal{E}$.

If $\mathcal{F}$ is a fibered category over $\mathcal{E}$, there does not always exist a splitting on $\mathcal{F}$.
Suppose for example that $Ob(\mathcal{E})$ and $Ob(\mathcal{F})$ are reduced to one element, and that the set of
endomorphisms of that element is a group $E$, respectively $F$, so that the projection functor $p$ is given by a group
homomorphism $p: F \to E$, surjective since $p$ is fibrant. One verifies at once that the set of cleavages of
$\mathcal{F}$ over $\mathcal{E}$ is in bijective correspondence with the set of maps $s: E \to F$ such that
$ps = id_{E}$, i.e. the set of “systems of representatives” for the classes modulo the subgroup $G$ that is the kernel
of the surjective homomorphism $p: F \to E$. A cleavage is a splitting if and only if $s$ is a group homomorphism. To
say that a splitting exists therefore means that the group extension $F$ of $E$ by $G$ is trivial, which is expressed,
when $G$ is commutative, by the vanishing of a certain cohomology class in $H^{2}(E,G)$, where $G$ is regarded as a
group on which $E$ operates.

Suppose, however, that $\mathcal{F}$ is a fibered category over $\mathcal{E}$ such that the

<!-- original page 181 -->

$\mathcal{F}_{S}$ are **rigid** categories, i.e. the automorphism group of every object of $\mathcal{F}_{S}$ is reduced
to the identity. It is then easy to prove that $\mathcal{F}$ admits a splitting over $\mathcal{E}$. Indeed, one first
observes that the question of existence of a splitting is not changed if $\mathcal{F}$ is replaced by an
$\mathcal{E}$-equivalent category. This reduces us in the present case to the case where the $\mathcal{F}_{S}$ are rigid
**and reduced** categories, i.e. two isomorphic objects in $\mathcal{F}_{S}$ are identical. But if $G$ is a rigid and
reduced category, every isomorphism between two functors $H \to G$, where $H$ is any category, is an identity. It
follows that if $\mathcal{F}$ is a fibered category over $\mathcal{E}$ whose fiber categories are rigid and reduced,
then there exists a **unique** cleavage of $\mathcal{F}$ over $\mathcal{E}$, which is necessarily a splitting. Thus
$\mathcal{F}$ is isomorphic to the category defined by a functor $\phi: \mathcal{E}^{\circ} \to Cat$ such that the
$\phi(S)$ are rigid and discrete categories, and the functor $\phi$ is defined up to isomorphism.

## 10. Co-Fibered Categories, Bi-Fibered Categories

<!-- label: VI.10 -->

Consider a category $\mathcal{F}$ over $\mathcal{E}$, with projection functor

$$
p: \mathcal{F} \to \mathcal{E}.
$$

It defines a category $\mathcal{F}^{\circ}$ over $\mathcal{E}^{\circ}$ by the projection functor

$$
p^{\circ}: \mathcal{F}^{\circ} \to \mathcal{E}^{\circ}.
$$

A morphism $\alpha: \eta \to \xi$ in $\mathcal{F}$ is said to be **co-cartesian** if it is a cartesian morphism for
$\mathcal{F}^{\circ}$ over $\mathcal{E}^{\circ}$. Spelling this out, one sees that it means that for every object $\xi'$
of $\mathcal{F}_{S}$, the map $u \mapsto u \circ \alpha$

$$
\operatorname{Hom}_{S}(\xi,\xi') \to \operatorname{Hom}_{f}(\eta,\xi')
$$

is bijective. One then also says that $(\xi,\alpha)$ is a **direct image** of $\eta$ by $f$, in the category
$\mathcal{F}$ over $\mathcal{E}$. If it exists for every $\eta$ in $\mathcal{F}_{T}$, one says that the direct-image
functor by $f$ exists; once it has been chosen, this functor is denoted

<!-- original page 182 -->

$$
f*_{\mathcal{F}}    or    f_{*}.
$$

It is therefore defined by an isomorphism of bifunctors on $\mathcal{F}^{\circ}_{T} \times \mathcal{F}_{S}$:

$$
\operatorname{Hom}_{S}(f_{*}(\eta),\xi) \simeq \operatorname{Hom}_{f}(\eta,\xi).
$$

Thus, if $f_{*}$ exists, then for $f*$ to exist it is necessary and sufficient that $f_{*}$ admit an adjoint functor,
i.e. that there exist a functor $f*: \mathcal{F}_{S} \to \mathcal{F}_{T}$ and an isomorphism of bifunctors

$$
\operatorname{Hom}_{S}(f_{*}(\eta),\xi) \simeq \operatorname{Hom}_{T}(\eta,f*(\xi)).
$$

Let $g: U \to T$ be another morphism in $\mathcal{E}$, and suppose that the inverse and direct images by $f$, $g$, and
`fg` exist. Consider then the functorial homomorphisms

```text
c^{f,g}: f_* g_* ← (fg)_*,
c_{f,g}: g* f* → (fg)*.
```

One observes that, if $f_{*} g_{*}$ and $g* f*$ are regarded as a pair of adjoint functors, and likewise $(fg)_{*}$ and
$(fg)*$, then the two preceding homomorphisms are adjoint to one another. Thus one is an isomorphism if and only if the
other is. In particular:

**Proposition.**

<!-- label: VI.10.1 -->

Suppose that the category $\mathcal{F}$ over $\mathcal{E}$ is prefibered and co-prefibered. In order that it be fibered,
it is necessary and sufficient that it be co-fibered.

Of course, $\mathcal{F}$ is said to be co-prefibered, respectively co-fibered, over $\mathcal{E}$ if
$\mathcal{F}^{\circ}$ is prefibered, respectively fibered, over $\mathcal{E}$. We shall say that $\mathcal{F}$ is
**bi-fibered** over $\mathcal{E}$ if it is both fibered and co-fibered over $\mathcal{E}$.

## 11. Various Examples

<!-- label: VI.11 -->

### a) Categories of Arrows of ℰ

Let $\mathcal{E}$ be a category. Denote by $\Delta^{1}$ the category associated with the totally ordered set with two
elements `[0,1]`. It therefore has two objects `0` and `1`, and besides the two identity morphisms one arrow `(0,1)`
with source `0` and target `1`. Let

<!-- original page 183 -->

```text
Ar(ℰ) = Hom̲(Δ¹,ℰ).
```

This is called the **category of arrows of** $\mathcal{E}$. The object `1` of $\Delta^{1}$ defines a canonical functor,
called the **target functor**

$$
Ar(\mathcal{E}) \to \mathcal{E}
$$

the functor defined by the object `0` of $\Delta^{1}$ being called the **source functor**. For every object $S$ of
$\mathcal{E}$, the fiber category $Ar(\mathcal{E})_{S}$ is canonically isomorphic to the category $\mathcal{E}_{/}S$ of
objects of $\mathcal{E}$ over $S$.

Consider a morphism $f: T \to S$ in $\mathcal{E}$. To it there corresponds a canonical functor

```text
f_*: ℰ_/T = ℱ_T → ℰ_/S = ℱ_S
```

and a functorial isomorphism

$$
\operatorname{Hom}_{S}(f_{*}(\eta),\xi) \simeq \operatorname{Hom}_{f}(\eta,\xi),
$$

which therefore makes $f_{*}$ a direct-image functor for $f$ in $\mathcal{F}$. Moreover, here

```text
(id_S)_* = id_{ℱ_S},    (fg)_* = f_* g_*,    c^{f,g} = id_{(fg)},
```

i.e. $\mathcal{F}$ is endowed with a co-splitting over $\mathcal{E}$. A fortiori, $\mathcal{F}$ is co-fibered over
$\mathcal{E}$. Note now that the set of morphisms in $\mathcal{F}$ is in bijective correspondence with the set of
commutative square diagrams in $\mathcal{E}$:

```text
Y --f′--> X
| v      | u
↓        ↓
T --f--> S.
```

<!-- original page 184 -->

By definition, the morphism in question is cartesian if the square is cartesian in $\mathcal{E}$, i.e. if it makes $Y$ a
fiber product of $X$ and $T$ over $S$. The inverse-image functor $f*$ therefore exists if and only if, for every object
$X$ over $S$, the fiber product $X \times_{S} T$ exists. It follows from VI.10.1 that if the product of two objects over
a third always exists in $\mathcal{E}$, i.e. if $\mathcal{F}$ is prefibered over $\mathcal{E}$, then $\mathcal{F}$ is
even fibered over $\mathcal{E}$.

### b) Category of Presheaves or Sheaves on Variable Spaces

Let $\mathcal{E} = Top$ be the category of topological spaces. If $T$ is a topological space, we denote by
$\mathcal{U}(T)$ the category of open subsets of $T$, whose morphisms are inclusion maps. If $\mathcal{C}$ is a
category, a functor $\mathcal{U}(T)^{\circ} \to \mathcal{C}$ is called a **presheaf** on $T$ with values in
$\mathcal{C}$, and a **sheaf** if it satisfies a left-exactness condition that we shall not repeat here.

The **category $\mathcal{P}(T)$ of presheaves on $T$ with values in $\mathcal{C}$** is, by definition, the category
`Hom̲(𝒰(T)°,𝒞)`, and the category $\mathcal{F}(T)$ of sheaves on $T$ with values in $\mathcal{C}$ is the full subcategory
whose objects are the objects of `Hom̲(𝒰(T)°,𝒞)` that are sheaves. If $f: T \to S$ is a morphism in $\mathcal{E}$, i.e. a
continuous map of topological spaces, then by the increasing map $U \mapsto f^{-1}(U)$ there corresponds to it a functor
$\mathcal{U}(S) \to \mathcal{U}(T)$, whence a functor

```text
f_*: Hom̲(𝒰(T)°,𝒞) → Hom̲(𝒰(S)°,𝒞)
```

called the **direct-image functor of presheaves by** $f$. One sees at once that the direct image of a sheaf is a sheaf.
Thus the functor $f_{*}: \mathcal{P}(T) \to \mathcal{P}(S)$ induces a functor, also denoted

$$
f_{*}: \mathcal{F}(T) \to \mathcal{F}(S).
$$

Moreover, one verifies trivially, by associativity of composition of functors, that for a second continuous map
$g: U \to T$ one has the identity

```text
(gf)_* = g_* f_*,    and likewise    (id_S)_* = id_{𝒫(S)}.
```

In this way one obtains a functor

$$
S \mapsto \mathcal{P}(S)
$$

respectively

$$
S \mapsto \mathcal{F}(S)
$$

<!-- original page 185 -->

from $\mathcal{E}$ to `Cat`. In fact, we are interested in the corresponding functor

```text
S ↦ 𝒫(S)°,    respectively    S ↦ ℱ(S)°.
```

It defines a co-fibered, indeed co-split, category over the category of topological spaces, called the **co-fibered
category of presheaves**, respectively **sheaves**, **with values in** $\mathcal{C}$, understood as on variable spaces.
Spelling out the construction of VI.8, one sees that a morphism from a presheaf $B$ on $T$ to a presheaf $A$ on $S$ is a
pair $(f,u)$ formed by a continuous map from $T$ to $S$ and a morphism $u: A \to f_{*}(B)$ in the category
$\mathcal{P}(S)$. This description is equally valid for morphisms of sheaves, $\mathcal{F}$ being a full subcategory of
$\mathcal{P}$.

In the most important cases, the category $\mathcal{P}$ and the category $\mathcal{F}$ over $\mathcal{E}$ are also
fibered categories; that is, for every continuous map, the direct-image functors $\mathcal{P}(T) \to \mathcal{P}(S)$ and
$\mathcal{F}(T) \to \mathcal{F}(S)$ have an adjoint functor, then denoted $f*$ and called the inverse-image functor of
presheaves, respectively the inverse-image functor of sheaves, by the continuous map $f$. This functor exists, for
example, if $\mathcal{C} = Set$. One can show that the functor $f*: \mathcal{P}(S) \to \mathcal{P}(T)$ exists whenever
inductive limits, relative to diagrams in the Universe under consideration, exist in $\mathcal{C}$. The question is less
easy for $\mathcal{F}$. Indeed, even in the case $\mathcal{C} = Set$, the inverse image of a presheaf that is a sheaf is
not in general a sheaf; in other words, the inverse-image functor of sheaves is not isomorphic to the functor induced by
the inverse-image functor of presheaves, despite the common notation $f*$. Thus $\mathcal{F}$ is a co-fibered
subcategory of $\mathcal{P}$, but not a fibered subcategory; i.e. **the inclusion functor $\mathcal{F} \to \mathcal{P}$
is not fibrant**.

The co-fibered category $\mathcal{P}$ can be deduced from a more general co-fibered, or rather fibered, category
obtained as follows. For every category $\mathcal{U}$ in the fixed Universe, put

```text
𝒫(𝒰) = Hom̲(𝒰,𝒞),
```

and

<!-- original page 186 -->

note that $\mathcal{U} \mapsto \mathcal{P}(\mathcal{U})$ is naturally a contravariant functor in $\mathcal{U}$, from the
category `Cat` to `Cat`. It therefore defines a split category over $\mathcal{E} = Cat$, which we shall denote
$Cat_{/}/\mathcal{C}$. The objects of this category are pairs $(\mathcal{U},p)$, where $\mathcal{U}$ is a category and
$p: \mathcal{U} \to \mathcal{C}$ is a functor; a morphism from $(\mathcal{U},p)$ to $(\mathcal{V},q)$ is essentially a
pair $(f,u)$, where $f$ is a functor $\mathcal{U} \to \mathcal{V}$ and $u$ is a homomorphism of functors $u: p \to qf$.
We leave to the reader the task of spelling out the composition of morphisms in $Cat_{/}/\mathcal{C}$.

The projection functor

```text
ℱ = Cat_//𝒞 → ℰ = Cat
```

sends the pair $(\mathcal{U},p)$ to the object $\mathcal{U}$. The fiber category at $\mathcal{U}$ is the category
`Hom̲(𝒰,𝒞)`, up to isomorphism. When inductive limits exist in $\mathcal{C}$, one shows easily that the fibered category
$Cat_{/}/\mathcal{C}$ over `Cat` is also co-fibered over `Cat`; i.e. one can define the notion of **direct image of a
functor** $p: \mathcal{U} \to \mathcal{C}$ by a functor $f: \mathcal{U} \to \mathcal{V}$.

The category of presheaves is deduced from the preceding fibered category by the base change

$$
Top^{\circ} \to Cat
$$

the functor $S \mapsto \mathcal{U}(S)$ defined above. This gives a fibered category over $Top^{\circ}$, and by passing
to the opposite category one obtains the co-fibered category $\mathcal{P}$ of presheaves over `Top`. The notion of
inverse image of a functor corresponds to that of direct image of a presheaf; the notion of direct image of a functor
corresponds to that of inverse image of a presheaf.

### c) Objects with Operators over an Object with Operators

Let $\mathcal{F}$ be a category over $\mathcal{E}$, and let $S$ be an object of $\mathcal{E}$ on which a group $G$
operates, on the left to fix ideas. This object with operators can be interpreted as corresponding to a functor
$\lambda: \mathcal{E}' \to \mathcal{E}$ from the category $\mathcal{E}'$ defined by $G$, with a single object and $G$ as
its group of endomorphisms, to the category $\mathcal{E}$. It therefore defines by base change a category $\mathcal{F}'$
over $\mathcal{E}'$, which is fibered, respectively co-fibered, when $\mathcal{F}$ is so over $\mathcal{E}$.

<!-- original page 187 -->

A section of $\mathcal{E}'$ over $\mathcal{F}'$, necessarily cartesian, since $\mathcal{E}'$ is a groupoid and every
isomorphism in $\mathcal{F}'$ is cartesian by VI.6.12, can also be interpreted as an $\mathcal{E}$-functor
$\mathcal{E}' \to \mathcal{F}$ over $\lambda$, or also as an object with operators $\xi$ in $\mathcal{F}$ “over” the
object with operators $S$.

### d) Pairs of Quasi-Inverse Adjoint Functors; Autodualities

When the base category $\mathcal{E}$ is reduced to two objects $a$, $b$ and, besides the identity arrows, to two
isomorphisms $f: a \to b$ and $g: b \to a$ inverse to one another, i.e. $\mathcal{E}$ is a connected rigid groupoid with
two objects, a normalized cloven category over $\mathcal{E}$ is essentially the same thing as the system formed by two
categories $\mathcal{F}_{a}$ and $\mathcal{F}_{b}$ and a **pair of adjoint functors**
$G: \mathcal{F}_{a} \to \mathcal{F}_{b}$ and $F: \mathcal{F}_{b} \to \mathcal{F}_{a}$ that are equivalences of
categories, hence quasi-inverse to one another. One takes for $\mathcal{F}_{a}$ and $\mathcal{F}_{b}$ the fiber
categories of $\mathcal{F}$, for $F$ and $G$ the functors $f*$ and $g*$, and the two isomorphisms

```text
u: FG ≃ id_{ℱ_a},    v: GF ≃ id_{ℱ_b}
```

are $c_{g,f}$ and $c_{f,g}$. The two usual compatibility conditions between $u$ and $v$ are nothing other than condition
VI.7.4 B) for the composites `fgf` and `gfg`. It is easy to show that these conditions suffice to imply that one indeed
has a pseudofunctor $\mathcal{E}^{\circ} \to Cat$.

An interesting case is the one in which

```text
ℱ_b = ℱ_a°,    G = F°,    v = u°.
```

An **autoduality** in a category $\mathcal{C}$ means the data of a functor $D: \mathcal{C} \to \mathcal{C}^{\circ}$ and
an isomorphism $u: DD^{\circ} \simeq id_{\mathcal{C}}$ such that $u$ and the isomorphism
$u^{\circ}: D^{\circ}D \simeq id^{\circ}_{\mathcal{C}}$ make $(D,D^{\circ})$ a pair of adjoint functors, necessarily
quasi-inverse to one another. This condition is written

```text
D(u(x)) = u(D(x))    for every x ∈ Ob(𝒞).
```

### e) Categories over a Discrete Category ℰ

<!-- original page 188 -->

One says that $\mathcal{E}$ is a **discrete category** if every arrow in it is an identity arrow, so that $\mathcal{E}$
is defined up to unique isomorphism by knowing the set $I = Ob(\mathcal{E})$. The data of a category $\mathcal{F}$ over
$\mathcal{E}$ is therefore equivalent, up to unique isomorphism, to the data of a family of categories
$\mathcal{F}_{i}$, $i \in I$, the fiber categories. Every category $\mathcal{F}$ over $\mathcal{E}$ is fibered; every
$\mathcal{E}$-functor $\mathcal{F} \to \mathcal{G}$ is cartesian; one has a canonical isomorphism

```text
Hom̲_{ℰ/-}(ℱ,𝒢) ≃ ∏ᵢ Hom̲(ℱᵢ,𝒢ᵢ).
```

In particular, one obtains

```text
Γ̲(ℱ/ℰ) = Lim←(ℱ/ℰ) ≃ ∏ᵢ ℱᵢ.
```

### f) Suppose that ℰ Has Exactly Two Objects S and T

Suppose that, besides the identity morphisms, $\mathcal{E}$ has one morphism $f: T \to S$. Then a category $\mathcal{F}$
over $\mathcal{E}$ is defined, up to unique $\mathcal{E}$-isomorphism, by the data of two categories $\mathcal{F}_{S}$
and $\mathcal{F}_{T}$ and a bifunctor $H(\eta,\xi)$ on $\mathcal{F}^{\circ}_{T} \times \mathcal{F}_{S}$ with values in
`Set`. Indeed, if $\mathcal{F}$ is a category over $\mathcal{E}$, one associates to it the two fiber categories
$\mathcal{F}_{S}$ and $\mathcal{F}_{T}$ and the bifunctor $H(\eta,\xi) = \operatorname{Hom}_{f}(\eta,\xi)$. We leave to
the reader the task of spelling out the construction in the opposite direction. For the category in question to be
fibered, or prefibered, which comes to the same thing, it is necessary and sufficient that the functor $H$ be
representable with respect to the argument $\xi$. For it to be co-fibered, it is necessary and sufficient that $H$ be
representable with respect to the argument $\eta$.

### g)

Let $\mathcal{F} = \mathcal{C} \times \mathcal{E}$, regarded as a category over $\mathcal{E}$ by means of $pr_{2}$. Then
$\mathcal{F}$ is fibered and co-fibered over $\mathcal{E}$, and is even endowed with a canonical splitting and
co-splitting, corresponding to the constant functor on $\mathcal{E}$, respectively on $\mathcal{E}^{\circ}$, with values
in `Cat` and value $\mathcal{C}$. One has

```text
Γ̲(ℱ/ℰ) ≃ Hom̲(ℰ,𝒞),
```

and

<!-- original page 189 -->

$Lim\leftarrow(\mathcal{F}/\mathcal{E})$ corresponds to the full subcategory formed by the functors
$F: \mathcal{E} \to \mathcal{C}$ that transform arbitrary morphisms into isomorphisms.

## 12. Functors on a Cloven Category

<!-- label: VI.12 -->

Let $\mathcal{F}$ be a normalized cloven category over $\mathcal{E}$. For every object $S$ of $\mathcal{E}$, denote by

$$
i_{S}: \mathcal{F}_{S} \to \mathcal{F}
$$

the inclusion functor. Thus one has a functorial homomorphism, for every morphism $f: T \to S$ in $\mathcal{E}$,

```text
α_f: i_T f* → i_S,
```

where $f*$ is the base-change functor $\mathcal{F}_{S} \to \mathcal{F}_{T}$ for $f$ defined by the cleavage. Let now

$$
F: \mathcal{F} \to \mathcal{C}
$$

be a functor from $\mathcal{F}$ to a category $\mathcal{C}$. Put, for every $S \in Ob(\mathcal{E})$,

```text
F_S = F ∘ i_S: ℱ_S → 𝒞,
```

and for every $f: T \to S$ in $\mathcal{E}$,

```text
φ_f = F ∗ α_f: F_T f* → F_S.
```

Thus to every functor $F: \mathcal{F} \to \mathcal{C}$ there is associated a family `(F_S)` of functors
$\mathcal{F}_{S} \to \mathcal{C}$, and a family $(\phi_{f})$ of homomorphisms of functors $F_{T} f* \to F_{S}$. These
families satisfy the following conditions:

a) $\phi_{id_{S}} = id_{F_{S}}$.

b) For two morphisms $f: T \to S$ and $g: U \to T$ in $\mathcal{E}$, one has commutativity in the square of functorial
homomorphisms:

```text
F_U g* f* --F_U ∗ c_{f,g}--> F_U(fg)*
    | φ_g ∗ f*                  | φ_{fg}
    ↓                           ↓
F_T f* ------φ_f-------------> F_S.
```

<!-- original page 190 -->

The first relation is trivial, and the second relation is obtained by applying the functor $F$ to the commutative
diagram

```text
g*f*(ξ) --c_{f,g}(ξ)--> (fg)*(ξ)
   | α_g(f*(ξ))             | α_{fg}(ξ)
   ↓                        ↓
f*(ξ) --α_f(ξ)----------->  ξ
```

for variable $\xi$ in $\mathcal{F}_{S}$.

If $G$ is a second functor $\mathcal{F} \to \mathcal{C}$, giving rise to functors
$G_{S}: \mathcal{F}_{S} \to \mathcal{C}$ and functorial homomorphisms $\psi_{f}: G_{T} f* \to G_{S}$, and if
$u: F \to G$ is a functorial homomorphism, then to it there correspond the functorial homomorphisms $u \ast i_{S}$:

$$
u_{S}: F_{S} \to G_{S}.
$$

One checks at once that, for every morphism $f: T \to S$ in $\mathcal{E}$, one has commutativity in the squares

```text
c)  F_T f* --φ_f--> F_S
       | u_T ∗ f*      | u_S
       ↓               ↓
    G_T f* --ψ_f--> G_S.
```

**Proposition.**

<!-- label: VI.12.1 -->

Let $\mathcal{H}(\mathcal{F},\mathcal{C})$ be the category whose objects are pairs of families `(F_S)`,
$S \in Ob(\mathcal{E})$, of functors $\mathcal{F}_{S} \to \mathcal{C}$, and of families $(\phi_{f})$,
$f \in Fl(\mathcal{E})$, of functorial homomorphisms $F_{T} f* \to F_{S}$ satisfying conditions **a)** and **b)**, and
whose morphisms are the families $(u_{S})$, $S \in Ob(\mathcal{E})$, of homomorphisms $F_{S} \to G_{S}$ verifying the
commutativity condition **c)** written above; composition of morphisms is by composition of homomorphisms of functors
$\mathcal{F}_{S} \to \mathcal{C}$. Then the two laws just described define an **isomorphism** $K$ from the category
`Hom̲(ℱ,𝒞)` to the category $\mathcal{H}(\mathcal{F},\mathcal{C})$.

<!-- original page 191 -->

It is trivial that this is indeed a **functor** from the first category to the second. This functor is fully faithful:
for given $F$, $G$, the map $\operatorname{Hom}(F,G) \to \operatorname{Hom}(K(F),K(G))$ is trivially injective. To show
that it is surjective, it suffices to note that commutativity condition c) expresses the functoriality of the maps

```text
u(ξ) = u_S(ξ): F(ξ) = F_S(ξ) → G(ξ) = G_S(ξ)
```

for homomorphisms of the form $\alpha_{f}(\xi)$ in $\mathcal{F}$. On the other hand, one has functoriality on each fiber
category, i.e. for morphisms in $\mathcal{F}$ that are $T$-morphisms with $T \in Ob(\mathcal{E})$. Hence one has
functoriality for every morphism in $\mathcal{F}$, since an $f$-morphism, where $f: T \to S$ is a morphism in
$\mathcal{E}$, is uniquely a composite of a morphism $\alpha_{f}(\xi)$ and a $T$-morphism.

It remains therefore to prove that the functor $K$ is bijective on objects. The preceding argument already shows that
$K$ is injective on objects; it remains to prove that it is surjective. That is, suppose we start from a system `(F_S)`,
$(\phi_{f})$ satisfying a) and b), and define a map $Ob(\mathcal{F}) \to Ob(\mathcal{C})$ by

```text
F(ξ) = F_S(ξ)    for ξ ∈ Ob(ℱ_S) ⊂ Ob(ℱ),
```

and a map $Fl(\mathcal{F}) \to Fl(\mathcal{C})$ by

$$
F(\alpha_{f}(\xi)u') = \phi_{f}(\xi) F_{T}(u'),
$$

for every morphism $f: T \to S$ in $\mathcal{E}$, every object $\xi$ of $\mathcal{F}_{S}$, and every $T$-morphism $u'$
with target $f*(\xi)$. Then one obtains a **functor** $F$ from $\mathcal{F}$ to $\mathcal{C}$. Indeed, the relation
$F(id_{\xi}) = id_{F(\xi)}$ is trivial; it remains to prove multiplicativity $F(uv) = F(u)F(v)$ when one has an
$f$-morphism $u: \eta \to \xi$ and a $g$-morphism $v: \zeta \to \eta$, with $f: T \to S$ and $g: U \to T$ morphisms of
$\mathcal{E}$. Putting $w = uv$, one has

```text
u = α_f(ξ)u′,    v = α_g(η)v′,    w = α_{fg}(ξ)w′
```

<!-- original page 192 -->

with

```text
w′ = c_{f,g}(ξ) g*(u′) v′        cf. VI.8.
```

With this notation, one must prove commutativity of the outer contour of the diagram below:

```text
F_U(ζ) --F_U(v′)--> F_U g*(η) --F_U g*(u′)--> F_U g*f*(ξ) --F_U(c_{f,g}(ξ))--> F_U(fg)*(ξ)
   \________________ F(v) ________________/        | φ_g(f*(ξ))                         | φ_{fg}(ξ)
                                                    ↓                                    ↓
                                      F_T(η) --F_T(u′)--> F_T f*(ξ) --φ_f(ξ)--> F_S(ξ).
```

The left triangle is commutative by definition of $F(v)$; the middle square is commutative because it is deduced from
the homomorphism $u'$ by the functorial homomorphism $\phi_{g}$; finally the right square is commutative by condition
b). The desired conclusion follows.

Suppose now that $\mathcal{C}$ is also a normalized cloven category over $\mathcal{E}$, which from now on we shall call
$\mathcal{G}$, and that we are interested in $\mathcal{E}$-functors from $\mathcal{F}$ to $\mathcal{G}$. If $F$ is such
a functor, it induces functors

$$
F_{S}: \mathcal{F}_{S} \to \mathcal{G}_{S}
$$

on the fiber categories. On the other hand, for every morphism $f: T \to S$ in $\mathcal{E}$ and every object $\xi$ in
$\mathcal{F}_{S}$, the $f$-morphism $F(\alpha_{f}(\xi))$ factors uniquely through a $T$-morphism

$$
\phi_{f}(\xi): F_{T}(f*_{\mathcal{F}}(\xi)) \to f*_{\mathcal{G}}(F_{S}(\xi)),
$$

where the subscript $\mathcal{F}$ or $\mathcal{G}$ indicates the cloven category in which the inverse-image functor is
being taken. Hence one obtains a functorial homomorphism of functors from $\mathcal{F}_{S}$ to $\mathcal{G}_{T}$:

```text
φ_f: F_T f*_ℱ → f*_𝒢 F_S.
```

<!-- original page 193 -->

The two systems `(F_S)` and $(\phi_{f})$ satisfy the following conditions:

a′) $\phi_{id_{S}} = id_{F_{S}}$.

b′) For two morphisms $f: T \to S$ and $g: U \to T$ in $\mathcal{E}$, one has commutativity in the following diagram of
functorial homomorphisms:

```text
F_U g*_ℱ f*_ℱ --F_U ∗ c^ℱ_{f,g}--> F_U(fg)*_ℱ
       | φ_g ∗ f*_ℱ                         | φ_{fg}
       ↓                                    ↓
g*_𝒢 F_T f*_ℱ
       | g*_𝒢 ∗ φ_f
       ↓
g*_𝒢 f*_𝒢 F_S --c^𝒢_{f,g} ∗ F_S--> (fg)*_𝒢 F_S.
```

We leave to the reader the verification, as well as the statement and proof of the analogue of Proposition VI.12.1,
which implies that one obtains in this way a bijective correspondence between the set of $\mathcal{E}$-functors from
$\mathcal{F}$ to $\mathcal{G}$ and the set of systems `(F_S)`, $(\phi_{f})$ satisfying conditions a′) and b′) above. Of
course, in this correspondence, the cartesian functors are characterized by the property that the homomorphisms
$\phi_{f}$ are isomorphisms.

**Remark.** Of course, it is usually better to reason directly on fibered categories without using explicit cleavages.
This avoids, in particular, having to appeal, for the simple notion of ℰ-functor or cartesian ℰ-functor, to a heavy
interpretation such as the one above. It is in order to avoid unbearable heaviness, and to obtain more intrinsic
statements,

<!-- original page 194 -->

that we have had to give up starting, as in [VI.2], from the notion of cloven category, called “fibered category” in the
cited text, which now takes second place in favor of the notion of fibered category. It is moreover probable that,
contrary to the still prevailing usage, tied to old habits of thought, it will eventually prove more convenient in
universal problems not to put the emphasis on **one** solution supposed chosen once and for all, but to put all
solutions on an equal footing.

## Bibliography

<!-- label: VI.13 -->

[VI.1] A. Grothendieck, “Sur quelques points d’algèbre homologique,” Tôhoku Math. J. **9** (1957), 119–221.

[VI.2] A. Grothendieck, “Technique de descente et Théorèmes d’existence, I,” Séminaire Bourbaki 190, December 1959.

<!-- Exposé VII does not exist. -->

[^vi-1-1]: The eventual authors are C. Chevalley and P. Gabriel. The book is due out in the year 3000. Meanwhile, cf.
    also SGA 4 I.


<!-- SOURCE: 07-n-existe-pas.md -->

# Exposé VII. Does Not Exist

<!-- label: I.VII -->

Exposé VII does not exist in this volume; the numbering jumps directly from Exposé VI to Exposé VIII. As recorded in the
[Foreword](00-avertissement.md), the lecturer (Grothendieck) sketched the language of descent in general categories only
orally, taking a strictly utilitarian point of view and without entering into the logical difficulties raised by that
language; a written exposition was deemed beyond the scope of these notes. For a fully formed account, see J. Giraud,
*Méthodes de la descente*, Mémoires de la Société mathématique de France, no. 2 (1964), to which Exposé VIII refers in
place of its phantom citations to Exposé VII.


<!-- SOURCE: 08-descente-fidelement-plate.md -->

# Exposé VIII. Faithfully Flat Descent

<!-- label: VIII -->

<!-- original page 195 -->

## 1. Descent of Quasi-Coherent Modules

<!-- label: VIII.1 -->

Let `Sch` be the category of preschemes. Proceeding as in VI.11.b, one finds that the category of pairs $(X,F)$, where
$X$ is a prescheme and $F$ is a Module on $X$, with morphisms defined as there by means of the notion of direct image of
a Module by a morphism of ringed spaces, can be regarded as a fibered category over `Sch`. The base-change functor
relative to a morphism $f: X \to Y$ in `Sch` is the inverse-image functor of Modules by $f$. Note that the fiber
category at $X \in Ob(Sch)$ of the preceding fibered category is the category **opposite** to the category of Modules on
$X$.

Since the inverse image of a quasi-coherent Module is quasi-coherent, the full subcategory of the category of pairs
$(X,F)$, formed by the pairs for which $F$ is quasi-coherent, is a fibered subcategory of the preceding fibered
category. By contrast, if no hypotheses are made on $f$, the direct image of a quasi-coherent Module is not in general a
quasi-coherent Module. We shall simply call this fibered category the **fibered category of quasi-coherent Modules on
preschemes**.

Recall, on the other hand, that a morphism $f: X \to Y$ of ringed spaces is said to be **faithfully flat** if it is
**flat**, i.e. for every $x \in X$, $\mathcal{O}_{X,x}$ is a flat module over $\mathcal{O}_{Y,f(x)}$, cf. IV, and
**surjective**. One says that $f$ is a **quasi-compact** morphism if the inverse image by $f$ of every quasi-compact
subset is quasi-compact. When $f$ is a morphism of preschemes, this also means that the inverse image by $f$ of an
affine open subset of $Y$ is a **finite** union of affine open subsets of $X$.

**Theorem.**

<!-- label: VIII.1.1 -->

<!-- original page 196 -->

Let $\mathcal{F}$ be the fibered category of quasi-coherent Modules on preschemes. Let $g: S' \to S$ be a faithfully
flat and quasi-compact morphism of preschemes. Then $g$ is a morphism of effective $\mathcal{F}$-descent.

Recall[^viii-1-1] that this means two things:

**Corollary. Descent of Homomorphisms of Modules.**

<!-- label: VIII.1.2 -->

Let $g: S' \to S$ be a faithfully flat and quasi-compact morphism of preschemes; let $F$ and $G$ be two quasi-coherent
Modules on $S$; let $F'$ and $G'$ be their inverse images on $S'$; and finally let $F''$ and $G''$ be their inverse
images on $S'' = S' \times_{S} S'$. Consider the diagram of maps of sets defined by the base-change functors by $g$,
$p_{1}$, $p_{2}$, where `p₁,p₂: S′ ×_S S′ ⇉ S′` are the two projections:

```text
Hom_S(F,G) → Hom_{S′}(F′,G′) ⇉ Hom_{S″}(F″,G″).
```

This diagram is exact, i.e. it defines a bijection from the first set onto the set of coincidences of the two maps
written from the second set to the third.

In other words, the base-change functor by $g$, $F \mapsto F'$, defines a **fully faithful** functor from the category
of quasi-coherent Modules on $S$ to the category of quasi-coherent Modules on $S'$ endowed with descent data relative to
$g$. Moreover:

**Corollary. Descent of Modules.**

<!-- label: VIII.1.3 -->

For every quasi-coherent Module $F'$ on $S'$, every descent datum on $F'$ relative to $g$ is **effective**, i.e. $F'$,
with its descent datum, is isomorphic to the inverse image by $g$ of a quasi-coherent Module on $S$, determined up to
unique isomorphism by VIII.1.2.

In other words, the preceding fully faithful functor is even an **equivalence**. In practice, this means that giving a
quasi-coherent Module on $S$ is the same as giving a quasi-coherent Module on $S'$ endowed with descent data relative to
$g$.

**Proof of VIII.1.1.** Let first $T$ be an $S$-prescheme that is $S$-isomorphic to the sum of a family of induced open
subsets `Sᵢ` of $S$ covering $S$. Then it is evident that the structural morphism $T \to S$ is a morphism of effective
$\mathcal{F}$-descent. This means precisely that giving a quasi-coherent Module $F$ on $S$ is equivalent to giving
quasi-coherent Modules `Fᵢ` on the `Sᵢ`, together with gluing isomorphisms
$\phi_{ji}: F_{i}|S_{i}\cap S_{j} \to F_{j}|S_{i}\cap S_{j}$ satisfying the familiar cocycle condition. By VII, 8,

<!-- original page 197 -->

it follows that, in order to verify that $g: S' \to S$ is a morphism of effective $\mathcal{F}$-descent, it suffices to
verify it for the morphism $g_{T}: T' = T \times_{S} S' \to T$ deduced from $g$ by the base change $T \to S$. Note that
the hypothesis on $T \to S$ remains stable under arbitrary base change, hence $T \to S$ is in fact a **universal**
morphism of effective $\mathcal{F}$-descent. Taking for the `Sᵢ` affine open subsets covering $S$, we are therefore
reduced to the case where $S$ is affine.

Then $S'$ is a finite union of affine open subsets; taking the $S$-scheme sum of these, one obtains an affine $S$-scheme
$S_{1}$ and an $S$-morphism $S_{1} \to S'$ that is flat and surjective. Thus $S_{1}$ is also faithfully flat over $S$.
If, therefore, one proves that a faithfully flat affine morphism is a morphism of effective $\mathcal{F}$-descent, hence
a strict universal morphism of $\mathcal{F}$-descent, the hypothesis being stable under base change, it follows in
particular that the structural morphism $S_{1} \to S$ is a strict universal morphism of $\mathcal{F}$-descent. Since
there exists an $S$-morphism $S_{1} \to S'$, it will indeed follow, by [VIII.D], that $g: S' \to S$ is a strict morphism
of $\mathcal{F}$-descent.

Thus we are reduced to the case where $g$ is an affine morphism; as we have seen, we may then moreover suppose $S$
affine. Hence **we may suppose $S$ and $S'$ affine**. In this case, VIII.1.2 is equivalent to:

**Lemma.**

<!-- label: VIII.1.4 -->

Let $A$ be a ring, $A'$ a faithfully flat $A$-algebra, $M$ and $N$ two $A$-modules, $M'$ and $N'$ the $A'$-modules
obtained by change of rings $A \to A'$, and $M''$, $N''$ the $A'' = A' \otimes_{A} A'$-modules obtained by change of
rings $A \to A''$. Then the sequence of maps of sets

```text
Hom_A(M,N) → Hom_{A′}(M′,N′) ⇉ Hom_{A″}(M″,N″)
```

is exact.

<!-- original page 198 -->

Since the homomorphism $N \to N'$ is injective, $A'$ being faithfully flat over $A$, the first arrow is injective. It
remains to prove that if an $A'$-homomorphism $u': M' \to N'$ is compatible with the descent data, then it comes from an
$A$-homomorphism $u: M \to N$. But this also simply means that $u'$ maps the subset $M$ of $M'$ into the subset $N$ of
$N'$. The induced map $u: M \to N$ will then automatically be $A$-linear, since $u'$ is $A'$-linear, and one sees
similarly that $u'$ is necessarily equal to $u \otimes_{A} A'$.

Now if $x \in M$, then $u'(x)$ is an element in the kernel of the pair of maps `N′ ⇉ N″`. Thus, in order to prove
VIII.1.4, we are reduced to the following special case, corresponding to the case $M = A$:

**Corollary.**

<!-- label: VIII.1.5 -->

Let $N$ be an $A$-module. Then the sequence of maps of sets

```text
N → N′ ⇉ N″
```

is exact.

Indeed, let $A_{1}$ be a faithfully flat $A$-algebra. To show that the sequence under consideration is exact, it
suffices to prove that the sequence deduced from it by the change of rings $A \to A_{1}$ is exact. But the latter, as
one sees at once, is the sequence relative to the $A_{1}$-module $N_{1} = N \otimes_{A} A_{1}$ and to the
$A_{1}$-algebra $A'_{1} = A_{1} \otimes_{A} A'$. It is therefore enough to find an $A_{1}$ faithfully flat over $A$ such
that $\operatorname{Spec}(A'_{1}) \to \operatorname{Spec}(A_{1})$ is a strict morphism of $\mathcal{F}$-descent. It
indeed suffices to take $A_{1} = A'$, for then the preceding morphism admits a right inverse, hence by [VIII.D] it is a
morphism of effective descent for any fibered category over `Sch`.

It remains finally to show that if $N'$ is an $A'$-module endowed with descent data for $A \to A'$, i.e. endowed with an
isomorphism

$$
\phi: N'_{1} \simeq N'_{2}
$$

between the two modules deduced from $N'$ by the changes of rings `A′ ⇉ A′ ⊗_A A′`, then

<!-- original page 199 -->

$N'$ is isomorphic, with its descent datum, to a module $N \otimes_{A} A'$. Taking VIII.1.5 into account, one sees
easily that this statement is equivalent to the following:

**Lemma.**

<!-- label: VIII.1.6 -->

Let $N'$ be an $A'$-module endowed with descent data relative to $A \to A'$, where $A'$ is an $A$-algebra. Let $N$ be
the $A$-submodule of $N'$ formed by the $x$ such that

```text
φ(x ⊗_{A′} 1_{A′}) = 1_{A′} ⊗_{A′} x,
```

and consider the canonical homomorphism

```text
N ⊗_A A′ → N′,
```

which is then compatible with the descent data. If $A'$ is faithfully flat over $A$, this homomorphism is an
isomorphism.

Let us prove this lemma. Let again $A_{1}$ be a faithfully flat $A$-algebra. To show that the morphism under
consideration is an isomorphism, it suffices to prove that it becomes so after the change of rings $A \to A_{1}$. Now,
using the flatness of $A_{1}$ over $A$, one sees that the homomorphism so obtained is none other than the one that would
be obtained directly in terms of the module $N' \otimes_{A} A_{1}$ over $A'_{1} = A' \otimes_{A} A_{1}$, endowed with
the descent datum relative to $A_{1} \to A'_{1}$ canonically deduced by change of rings from the datum given on $N'$.
Thus it suffices to find an $A_{1}$ faithfully flat over $A$ such that
$\operatorname{Spec}(A'_{1}) \to \operatorname{Spec}(A_{1})$ is a morphism of effective $\mathcal{F}$-descent. As above,
take $A_{1} = A'$. This finishes the proof of VIII.1.6, and hence the proof of VIII.1.1.

**Corollary. Descent of Sections of Modules.**

<!-- label: VIII.1.7 -->

Let $g: S' \to S$ be a faithfully flat and quasi-compact morphism of preschemes. For every quasi-coherent Module $G$ on
$S$, let $G'$ and $G''$ be its inverse images on $S'$ and $S'' = S' \times_{S} S'$, and consider the diagram of
homomorphisms of Modules on $S$:

```text
G → g_*(G′) ⇉ h_*(G″),
```

where $h: S'' \to S$ is the structural morphism. This diagram is **exact**.

<!-- original page 200 -->

Indeed, this means that for every open $U$ in $S$, the corresponding diagram formed by the sections over $U$ is exact.
One may evidently suppose $U = S$, and the exactness in question is then a special case of VIII.1.2, obtained by taking
$F = \mathcal{O}_{S}$.

Since the inverse-image functor of Modules is right exact, one concludes formally from VIII.1.1:

**Corollary. Descent of Quotient Modules.**

<!-- label: VIII.1.8 -->

With the notation of VIII.1.7, let moreover $Quot(F)$, for every quasi-coherent Module $F$ on a prescheme, denote the
set of quasi-coherent quotient Modules of $F$. With this convention, the diagram of maps of sets

```text
Quot(G) → Quot(G′) ⇉ Quot(G″)
```

is exact.

One would evidently have the same statement with submodules instead of quotient Modules, since the two correspond
bijectively. Taking in particular $G = \mathcal{O}_{S}$, one obtains:

**Corollary. Descent of Closed Subpreschemes.**

<!-- label: VIII.1.9 -->

For every prescheme $X$, let $H(X)$ be the set of closed subpreschemes of $X$. With this notation, and under the
conditions of VIII.1.7, the following diagram of maps of sets

```text
H(S) → H(S′) ⇉ H(S″)
```

**is exact**.

Theorem VIII.1.1 should be completed by the following result:

**Proposition. Descent of Properties of Modules.**

<!-- label: VIII.1.10 -->

Let $g: S' \to S$ be a faithfully flat and quasi-compact morphism, and let $F$ be a quasi-coherent Module on $S$. In
order that $F$ be of finite type, respectively of finite presentation, respectively locally free and of finite type, it
is necessary and sufficient that its inverse image $F'$ on $S'$ be so.

It remains only to prove the “suffices” direction. One may evidently suppose $S$ affine,

<!-- original page 201 -->

and then, replacing $S'$ by a sum of affine open subsets covering $S'$, one is reduced to the case where $S'$ is also
affine. Then our statement is equivalent to the following:

**Corollary.**

<!-- label: VIII.1.11 -->

Let $A$ be a ring, $A'$ a faithfully flat $A$-algebra, $M$ an $A$-module, and $M'$ the $A'$-module $M \otimes_{A} A'$.
In order that $M$ be of finite type, respectively of finite presentation, respectively locally free of finite type, it
is necessary and sufficient that $M'$ be so.

Indeed, $M = colim_{i} M_{i}$, where the `Mᵢ` are the finite-type submodules of $M$. Hence $M' = colim_{i} M'_{i}$, and
if $M'$ is of finite type, then $M'$ is equal to one of the $M'_{i}$; by faithful flatness, $M$ is equal to `Mᵢ`, hence
$M$ is of finite type. Consequently there exists an exact sequence

$$
0 \to R \to L \to M \to 0,
$$

with $L$ free of finite type, whence an exact sequence

$$
0 \to R' \to L' \to M' \to 0,
$$

with $L'$ free of finite type. Thus if $M'$ is of finite presentation, $R'$ is of finite type, and by what precedes $R$
is of finite type, hence $M$ is of finite presentation. Finally, saying that $M$ is locally free and of finite type
means that it is of finite presentation and flat, cf. IV in the noetherian case; the general case is left to the reader.
Since each of these properties descends, so does their conjunction. This finishes the proof.

**Remark.**

<!-- label: VIII.1.12 -->

The conjunction of VIII.1.1 and VIII.1.10 shows that the statement VIII.1.1 remains valid when one replaces the fibered
category $\mathcal{F}$ by the fibered subcategory formed by quasi-coherent Modules of finite type, respectively of
finite presentation, respectively locally free of finite type, respectively locally free of given rank $n$.

## 2. Descent of Affine Preschemes over Another

<!-- label: VIII.2 -->

<!-- original page 202 -->

Since the inverse-image functor of Modules is compatible with tensor product and other tensor operations, Theorem
VIII.1.1 implies various variants, obtained by considering, instead of a single quasi-coherent Module, a quasi-coherent
Module or a system of quasi-coherent Modules endowed with various additional structures expressed by means of tensor
operations.

For example, the data of three quasi-coherent Modules $F$, $G$, $H$ on $S$ and a pairing

$$
F \otimes G \to H
$$

is equivalent to the data of three quasi-coherent Modules $F'$, $G'$, $H'$ on $S'$, endowed with descent data relative
to $g: S' \to S$, and endowed with a pairing

$$
F' \otimes G' \to H'
$$

“compatible” with these descent data, in the evident sense. For example, if $F = G = H$, one sees that the data of a
quasi-coherent Module $F$ on $S$ endowed with an algebra law, which for the moment we do not suppose to satisfy any
axiom of associativity, commutativity, or existence of a unit section, is equivalent to the same data on $S'$, endowed
in addition with descent data. Using the results of the preceding number, one checks at once that $F$ satisfies one of
the usual axioms just mentioned if and only if $F'$ does.

For example, the data of a quasi-coherent Algebra $\mathcal{A}$ on $S$, by which from now on we mean associative,
commutative, and with unit section, is equivalent to the data of a quasi-coherent Algebra $\mathcal{A}'$ on $S'$ endowed
with descent data relative to $g: S' \to S$. Recalling the equivalence between the dual category of quasi-coherent
Algebras on $S$ and the category of affine $S$-preschemes over $S$, EGA II, §1, one obtains at once:

**Theorem.**

<!-- label: VIII.2.1 -->

Let $\mathcal{F}'$ be the fibered category of affine morphisms of preschemes $f: X \to S$, regarded as a fibered
subcategory of the fibered category

<!-- original page 203 -->

of arrows in the category `Sch` of preschemes, VI.11.a. Let $g: S' \to S$ be a faithfully flat and quasi-compact
morphism of preschemes. Then $g$ is a morphism of effective $\mathcal{F}'$-descent.

## 3. Descent of Set-Theoretic Properties and Finiteness Properties of Morphisms

<!-- label: VIII.3 -->

_\[Translator’s note: the source section title has a footnote referring to further results of the same kind in EGA IV
2.3, 2.6, and 2.7.\]_

**Proposition.**

<!-- label: VIII.3.1 -->

Let $f: X \to Y$ be an $S$-morphism, let $g: S' \to S$ be a surjective morphism, and let
$f': X' = X \times_{S} S' \to Y' = Y \times_{S} S'$ be the morphism deduced from $f$ by base change using $g: S' \to S$.
In order that $f$ be surjective, respectively radicial, it is necessary and sufficient that $f'$ be so.

Note that $f'$ can also be obtained by the base change $Y' \to Y$, which is also surjective since it is deduced from the
surjective morphism $g: S' \to S$. On the other hand, for every $y \in Y$ and every $y' \in Y'$ lying over $y$, one has
an isomorphism

```text
X′_{y′} ≃ X_y ⊗_{κ(y)} κ(y′),
```

where $X_{y}$ denotes the fiber of $X$ at $y$, and $X'_{y'}$ that of $X'$ at $y'$. It follows that $X_{y}$ is nonempty,
respectively has at most one point and that point corresponds to a radicial residue extension, if and only if $X'_{y'}$
has the same property. This proves VIII.3.1.

**Corollary.**

<!-- label: VIII.3.2 -->

Under the conditions of VIII.3.1, if $f'$ is injective, respectively bijective, then $f$ is likewise.

This comes from the fact that if $X'_{y'}$ has at most one point, respectively exactly one point, then the same is true
of $X_{y}$. This is indeed so, since the morphism $X'_{y'} \to X_{y}$ is surjective, being deduced from
$\operatorname{Spec}(\kappa(y')) \to \operatorname{Spec}(\kappa(y))$, which is surjective.

**Proposition.**

<!-- label: VIII.3.3 -->

With the notation of VIII.3.1, suppose that $g: S' \to S$ is surjective and quasi-compact, respectively faithfully flat
and quasi-compact. In order that $f$ be quasi-compact, respectively of finite type, it is necessary and sufficient that
$f'$ be so.

<!-- original page 204 -->

Only the “suffices” direction has to be proved. One may evidently suppose $S = Y$, since the hypothesis made on
$g: S' \to S$ is preserved for $Y' \to Y$. Moreover, one may suppose $Y$ affine. Then $Y'$ is quasi-compact, hence $X'$
is quasi-compact, since $f'$ is so by hypothesis. Let $(X_{i})_{i}\in I$ be a family of affine open subsets of $X$
covering $X$. Then the $X'_{i}$ are open subsets of $X'$ covering $X'$, so a finite subfamily covers $X'$. Since
$X' \to X$ is surjective, it follows that the corresponding `Xᵢ` already cover $X$, and hence $X$ is quasi-compact, i.e.
$f$ is quasi-compact.

Suppose now that $f'$ is of finite type, and prove that $f$ is so, assuming $g$ faithfully flat. Replacing $Y'$ by the
sum of a family of affine open subsets covering it, one may suppose $Y'$ affine. Finally, since $X$ is covered by
finitely many affine open subsets `Xᵢ` by what precedes, it remains to show that they are of finite type over $Y$,
knowing that $X'_{i}$ is of finite type over $Y'$. This reduces us to:

**Corollary.**

<!-- label: VIII.3.4 -->

Let $B$ be an $A$-algebra, $A'$ a faithfully flat $A$-algebra, and $B' = B \otimes_{A} A'$ the $A'$-algebra deduced from
$B$ by change of rings. In order that $B$ be of finite type, it is necessary and sufficient that $B'$ be so.

Only the “suffices” direction has to be proved. We have $B = colim_{i} B_{i}$, where the `Bᵢ` are the finite-type
subalgebras of $B$. Thus $B' = colim_{i} B'_{i}$, and if $B'$ is of finite type over $A'$, then $B'$ is equal to one of
the $B'_{i}$; hence $B$ is equal to `Bᵢ`, and is therefore of finite type.

**Corollary.**

<!-- label: VIII.3.5 -->

Again suppose that the base-change morphism $g: S' \to S$ is faithfully flat and quasi-compact. In order that $f$ be
quasi-finite, it is necessary and sufficient that $f'$ be so.

Indeed, the property “quasi-finite” is by definition the conjunction of “of finite type” and “with finite fibers”; each
descends by $g$, the first by VIII.3.3, the second by the reasoning of VIII.3.1, which uses only the surjectivity of
$g$.

**Remarks.**

<!-- label: VIII.3.6 -->

Let $A$ be a ring and $X$ an $A$-prescheme. One sees easily that the following conditions are equivalent:

1. There exists a noetherian ring $A_{0}$, which one may if desired suppose to be a finite-type subring of $A$, an
   $A_{0}$-prescheme $X_{0}$ of finite type, a homomorphism $A_{0} \to A$, and an $A$-isomorphism
   $X \simeq X_{0} \times_{A_{0}} A$.
1. The diagonal morphism $X \to X \times_{\operatorname{Spec}(A)} X$ is quasi-compact, a void condition if $X$ is
   separated over $A$; $X$ is a finite union of affine open subsets `Xᵢ` whose rings `Bᵢ` are algebras of finite
   presentation over $A$, i.e. quotients of polynomial algebras in finitely many indeterminates by finite-type ideals.

<!-- original page 205 -->

If $X$ itself is affine, with ring $B$, these conditions simply mean that $B$ is an algebra of finite presentation over
$A$.

A morphism $f: X \to Y$ is said to be a **morphism of finite presentation**, and one also says that $X$ is of finite
presentation over $Y$, if $Y$ is a union of affine open subsets `Yᵢ` such that $X|Y_{i}$, as a `Yᵢ`-prescheme, satisfies
the preceding equivalent conditions. The same is then true for $X|Y'$ for **every** affine open subset $Y'$ in $Y$. This
is a property stable under base change, and moreover the composite of two morphisms of finite presentation is of finite
presentation.

With these notions in place, one sees from (2), proceeding as in VIII.1.10, that that statement remains valid when the
words “of finite type” are replaced by “of finite presentation”.

## 4. Descent of Topological Properties

<!-- label: VIII.4 -->

**Theorem.**

<!-- label: VIII.4.1 -->

Let $g: Y' \to Y$ be a morphism, and let $Z$ be a subset of $Y$. Suppose that $g$ is flat, and that there exists a
quasi-compact morphism $f: X \to Y$ such that $Z = f(X)$. N.B. if $Y$ is noetherian, this latter condition is implied by
“$Z$ is constructible”. Then

$$
g^{-1}(closure(Z)) = closure(g^{-1}(Z)).
$$

One may suppose $Y$ affine, then $Y'$ affine. Since $Y$ is affine, $X$ is a finite union of affine open subsets `Xᵢ`,
and replacing $X$ by the sum of the `Xᵢ`, one may also suppose $X$ affine. Let $A$, $A'$, $B$ be the rings of $Y$, $Y'$,
$X$, and let $B' = B \otimes_{A} A'$ be the ring of $X' = X \times_{Y} Y'$. Let $I$ be the kernel of $A \to B$, and $I'$
the kernel of $A' \to B'$. Thus the closed subsets of $Y$ and $Y'$ defined by these ideals are respectively the closure
of $Z = f(X)$ and the closure of $Z' = f'(X') = g^{-1}(Z)$. We want to show that the latter is equal to
$g^{-1}(closure(Z))$, which follows from $I' = IA'$, itself a consequence of the flatness of $A'$ over $A$.

<!-- original page 206 -->

**Corollary.**

<!-- label: VIII.4.2 -->

Let $g: Y' \to Y$ be a flat and quasi-compact morphism, and let $Z'$ be a closed subset of $Y'$ saturated for the
set-theoretic equivalence relation defined by $g$. Then

$$
Z' = g^{-1}(closure(g(Z'))).
$$

Indeed, $Z' = g^{-1}(Z)$, with $Z = g(Z')$. One may then apply VIII.4.1, noting that the condition imposed on $Z$ in
VIII.4.1 is indeed satisfied by taking for $X$ the prescheme $Z'$ endowed with the reduced structure induced by $Y'$.
The fact that $g$ is quasi-compact then ensures that the induced morphism $f: Z' \to Y$ is quasi-compact.

Statement VIII.4.2 also means that **the topology on $g(Y')$ induced by $Y$ is the quotient of the topology of $Y'$**.
In particular:

**Corollary.**

<!-- label: VIII.4.3 -->

Let $g: Y' \to Y$ be a faithfully flat and quasi-compact morphism. Then $g$ makes $Y$ a quotient topological space of
$Y'$; i.e. for a subset $Z$ of $Y$, $Z$ is closed, respectively open, if and only if $Z' = g^{-1}(Z)$ is so.

Recall now that two elements `a,b` of $Y'$ have the same image in $Y$ if and only if they are of the form
$p_{1}(c), p_{2}(c)$ for a suitable element $c$ in $Y'' = Y' \times_{Y} Y'$. It follows that, if $g$ is surjective, one
has an **exact** diagram of sets

```text
𝒫(Y) → 𝒫(Y′) ⇉ 𝒫(Y″),
```

where for every set $E$, $\mathcal{P}(E)$ denotes the set of its subsets. This being so, VIII.4.3 can also be
interpreted as follows:

**Corollary. Descent of Open, Respectively Closed, Subsets.**

<!-- label: VIII.4.4 -->

<!-- original page 207 -->

Let $g: Y' \to Y$ be as in VIII.4.3. For every prescheme $X$, let $Open(X)$, respectively $Closed(X)$, be the set of its
open subsets, respectively the set of its closed subsets. Then one has exact diagrams of set maps, deduced from $g$ and
the two projections of $Y'' = Y' \times_{Y} Y'$:

```text
Open(Y)   → Open(Y′)   ⇉ Open(Y″),
Closed(Y) → Closed(Y′) ⇉ Closed(Y″).
```

We have the following complement to VIII.4.3:

**Corollary.**

<!-- label: VIII.4.5 -->

Let $g: Y' \to Y$ be as in VIII.4.3, and let $Z$ be a subset of $Y$ such that there exists a quasi-compact morphism
$f: X \to Y$ with image $Z$ (for example, $Z$ constructible and $Y$ noetherian). Then $Z$ is a locally closed subset of
$Y$ if and only if $Z' = g^{-1}(Z)$ is a locally closed subset of $Y'$.

It is enough to prove the “if” direction. Let $Y_{1}$ be the closed subprescheme of $Y$, the closure of $Z$ endowed with
the induced reduced structure, and let $Y_{1}' = Y_{1} \times_{Y} Y'$ be the closed subprescheme of $Y'$ inverse image
of $Y_{1}$. Its underlying set is $g^{-1}(Y_{1}) = g^{-1}(cl(Z))$, hence by VIII.4.1 it is equal to $cl(Z')$. Since $Z'$
is locally closed in $Y'$, it is open in $cl(Z')$, hence open in $Y_{1}'$. But $Y_{1}'$ is faithfully flat and
quasi-compact over $Y_{1}$, so by VIII.4.3 it follows that $Z$ is open in $Y_{1}$, that is, in $cl(Z)$; this says
exactly that $Z$ is locally closed.

**Corollary.**

<!-- label: VIII.4.6 -->

Let $g: S' \to S$ be a faithfully flat and quasi-compact morphism, let $f: X \to Y$ be an $S$-morphism, and let
$f': X' \to Y'$ be the $S'$-morphism obtained from it by base change. Suppose that $f'$ is an open map (respectively a
closed map, respectively quasi-compact and a homeomorphism into its image, respectively a homeomorphism onto). Then $f$
has the same property.

Since $Y'$ is faithfully flat and quasi-compact over $Y$, one may suppose $Y = S$. Let $Q$ be a subset of $X$; then,
denoting by $h$ the projection morphism $X' \to X$, one has

<!-- original page 208 -->

$$
g^{-1}(f(Q)) = f'(h^{-1}(Q)).
$$

If $Q$ is open (respectively closed), so is $h^{-1}(Q)$, hence so is $f'(h^{-1}(Q))$ if $f'$ is assumed to be an open
map (respectively a closed map); therefore $f(Q)$ has the same property, by the preceding formula and VIII.4.3. This
proves the first two assertions in VIII.4.6.

It remains to examine the case where $f'$ is a homeomorphism into its image, and then to prove that $f$ is a
homeomorphism into its image. The case of a homeomorphism onto follows from VIII.3.1. By VIII.3.2, $f$ is injective; it
remains to prove that the map $X \to f(X)$ is open. We already know that $f$ is quasi-compact by VIII.3.3. It suffices
to prove that for every closed subset $Z$ of $X$ one has $Z = f^{-1}(cl(f(Z)))$. Since $h: X' \to X$ is surjective, this
is equivalent to the analogous formula after inverse image by $h$, namely

$$
Z' = f'^{-1}(g^{-1}(cl(f(Z)))),
$$

where $Z' = h^{-1}(Z)$. By VIII.4.1 applied to the subset $f(Z)$ of $Y$, one has $g^{-1}(cl(f(Z))) = cl(g^{-1}(f(Z)))$,
and the formula to be proved is equivalent to

$$
Z' = f'^{-1}(cl(f'(Z'))),
$$

which follows from the hypothesis that $f'$ is a homeomorphism into its image.

N.B. In this last argument, once $f$ is already assumed quasi-compact, we have not used that $g$ is quasi-compact, but
only that $g$ is faithfully flat. Thus under this hypothesis one can descend the property “homeomorphism into its
image,” or “homeomorphism onto,” or again, by the preceding argument, the property “$f'$ is quasi-compact and makes
$f'(X')$ a quotient topological space of $X'$.”

We shall say that a morphism $f: X \to Y$ of preschemes is **universally open** (respectively **universally closed**,
respectively **universally bicontinuous**, etc.) if for every base change $Y' \to Y$, the morphism $f': X' \to Y'$ is
open (respectively closed, respectively a homeomorphism onto its image). We then deduce from VIII.4.6:

**Corollary.**

<!-- label: VIII.4.7 -->

<!-- original page 209 -->

Under the conditions of VIII.4.6, $f$ is universally open (respectively universally closed, respectively a universal
homeomorphism into its image, respectively a universal homeomorphism) if and only if $f'$ is.

**Corollary.**

<!-- label: VIII.4.8 -->

Under the conditions of VIII.4.6, $f$ is separated (respectively proper) if and only if $f'$ is.

To say that $f$ is separated means that the diagonal morphism $X \to X \times_{Y} X$ is closed, or also universally
closed; the first assertion of VIII.4.8 therefore follows from VIII.4.7. To say that $f$ is proper means that $f$
satisfies the conditions: a) $f$ is of finite type, b) $f$ is separated, c) $f$ is universally closed. Condition a)
descends by VIII.3.3; condition b) also descends by what we have just seen; finally condition c) descends by VIII.4.7.

**Remarks.**

<!-- label: VIII.4.9 -->

Recall that when $g: Y' \to Y$ is a flat morphism of finite type, with $Y$ locally noetherian, then $g$ is an open
morphism (VI IV.6.6), which is a sharper result than VIII.4.3. One should note, however, that if $f$ is a faithfully
flat and quasi-compact morphism of noetherian preschemes, then $f$ is not in general an open morphism. For instance, let
$Y$ be an irreducible scheme whose generic point $y$ is not open (for example an algebraic curve), and take $Y'$ to be
the sum scheme $Y \amalg \operatorname{Spec}(\kappa(y))$; then the image, under the structural morphism $Y' \to Y$, of
the open part $\operatorname{Spec}(\kappa(y))$ is not an open subset of $Y$.

The reader should also observe that various statements of the present exposé become false if one drops the hypothesis
that the faithfully flat morphism under consideration is also quasi-compact. The typical counterexample is obtained by
taking $Y'$ to be the sum scheme of the spectra of the local rings of the points of $Y$. For example, again taking $Y$
to be an irreducible algebraic curve and $Z$ to be the subset of $Y$ consisting of the generic point, its inverse image
in $Y'$ is open, while $Z$ is not open.

### 4.10.

<!-- label: VIII.4.10 -->

<!-- original page 210 -->

Various statements of the present exposé remain valid if the hypothesis that $Y'$ be flat over $Y$ is replaced by the
following one: there exists a finite-type Module $F$ on $Y'$, with support $Y'$, flat relative to $Y$. Faithful flatness
is then to be replaced by the preceding hypothesis together with the hypothesis that $Y' \to Y$ is surjective. This
applies to the first two assertions in VIII.1.10, to VIII.3.3, VIII.3.5, VIII.4.1, and consequently to all the results
of the present number.

## 5. Descent of Morphisms of Preschemes

<!-- label: VIII.5 -->

**Proposition.**

<!-- label: VIII.5.1 -->

Let $g: S' \to S$ be a morphism of preschemes.

a) Suppose that $g$ is surjective and that the homomorphism

$$
g*: \mathcal{O}_{S} \to g_{*}(\mathcal{O}_{S}')
$$

is injective. Then $g$ is an epimorphism in the category of preschemes, and even in the category of ringed spaces.

b) Suppose that $g$ is surjective and makes $S$ a quotient topological space of $S'$. Let $S'' = S' \times_{S} S'$, let
$h: S'' \to S$ be the structural morphism, and consider the canonical diagram of homomorphisms

```text
𝒪_S → g_*(𝒪_S′) ⇉ h_*(𝒪_S″).
```

Suppose this diagram is **exact**. Then $g$ is an effective epimorphism in the category of preschemes (and also in the
category of ringed spaces), that is, the diagram

$$
S \leftarrow S' \Leftrightarrow S''
$$

is exact.

**Proof.** a) We must show that a morphism of ringed spaces $f: S \to Z$ is known once `fg` is known. Since $g$ is
surjective, the underlying set map $f_{0}$ of $f$ is known; it remains to determine the homomorphism of sheaves of rings
$\mathcal{O}_{Z} \to \mathcal{O}_{S}$, or equivalently the homomorphism

<!-- original page 211 -->

$$
u: f^{-1}_{0}(\mathcal{O}_{Z}) \to \mathcal{O}_{S}
$$

defined by $f$. We already know the homomorphism

$$
(fg)^{-1}_{0}(\mathcal{O}_{Z}) = g^{-1}_{0}(f^{-1}_{0}(\mathcal{O}_{Z})) \to \mathcal{O}_{S}'
$$

defined by `fg`, or equivalently we have a homomorphism

$$
f^{-1}_{0}(\mathcal{O}_{Z}) \to g_{0}*(\mathcal{O}_{S}') = g_{*}(\mathcal{O}_{S}').
$$

One immediately checks that the latter is none other than the composite of
$g*: \mathcal{O}_{S} \to g_{*}(\mathcal{O}_{S}')$ with $u$; since $g*$ is injective, $u$ is known once $g*u$ is known.

\[
N.B. We have obviously not used the fact that $g: S' \to S$ is a morphism of preschemes; the statement would hold for an
arbitrary morphism of ringed spaces. The same remark applies to b), both in the category of ringed spaces and in the
category of spaces ringed by local rings. Notice also that if $g$ is a morphism of preschemes, not necessarily
surjective, such that $g*: \mathcal{O}_{S} \to g_{*}(\mathcal{O}_{S}')$ is injective, then for two morphisms $f_{1}, f_{2}$ from $S$ to a **scheme** $Z$
such that $f_{1}g = f_{2}g$, one has $f_{1} = f_{2}$. Indeed, if $I$ is the Ideal on $S$ defining the subprescheme of $S$ where $f_{1}$
and $f_{2}$ coincide (the inverse image of the diagonal subprescheme of $Z \times Z$ by $(f_{1},f_{2})$), one sees that $I$ is
contained in $Ker(g*)$.
\]

b) We must show that for every ringed space $Z$, the following diagram of maps is exact,

```text
Hom(S,Z) → Hom(S′,Z) ⇉ Hom(S″,Z),
```

and likewise when $Z$ is a space ringed by local rings and one restricts to homomorphisms of spaces ringed by local
rings. Since by a) we already know that the first map is injective, it remains to see that if $f': S' \to Z$ is a
homomorphism of ringed spaces such that $f'p_{1} = f'p_{2}$, then $f'$ is of the form `fg`, where $f: S \to Z$ is a
homomorphism of ringed spaces.

<!-- original page 212 -->

Since $g$ is surjective, it is then evident that if $f'$ is a morphism of spaces ringed by local rings, the same will be
true for $f$.

The hypothesis on $f'$ implies that the underlying set map $f_{0}'$ is constant on the fibers of the map $g_{0}$. Since
$g_{0}$ is surjective, $f_{0}'$ factors uniquely as $f_{0}' = f_{0}g_{0}$, where $f_{0}: S \to Z$ is a map, necessarily
continuous because $g_{0}$ identifies $S$ with a quotient topological space of $S'$. Now consider the homomorphism

$$
f^{-1}_{0}(\mathcal{O}_{Z}) \to g_{*}(\mathcal{O}_{S}')
$$

deduced from the homomorphism $(f_{0}g_{0})^{-1}(\mathcal{O}_{Z}) \to \mathcal{O}_{S}'$ corresponding to $f'$. The
hypothesis $f'p_{1} = f'p_{2}$ is then interpreted as saying that the composites of the preceding homomorphism with the
two homomorphisms

```text
g_*(𝒪_S′) ⇉ h_*(𝒪_S″)
```

are the same. Hence, by hypothesis b), it factors through a morphism

$$
f^{-1}_{0}(\mathcal{O}_{Z}) \to \mathcal{O}_{S}.
$$

This latter morphism defines a morphism of ringed spaces $f: S \to Z$, which is the desired morphism.

**Theorem.**

<!-- label: VIII.5.2 -->

Let $\mathcal{F}$ be the fibered category of arrows in the category `Sch` of preschemes (VI VI.11.a). Then every
faithfully flat and quasi-compact morphism $g: S' \to S$ is a morphism of $\mathcal{F}$-descent (or, as one also says, a
descent morphism in `Sch`).

This means the following: let $S'' = S' \times_{S} S'$, and for two preschemes `X,Y` over $S$, consider their inverse
images $X',Y'$ over $S'$ and their inverse images $X'',Y''$ over $S''$; this gives a diagram of maps

```text
Hom_S(X,Y) → Hom_S′(X′,Y′) ⇉ Hom_S″(X″,Y″).
```

In these notations, VIII.5.2 says that this diagram is exact. Notice that it is not true in general that $g$ is a
morphism of effective descent, that is, that for every prescheme $X'$ over $S'$, every descent datum on $X'$ relative to
$g: S' \to S$ is effective. The question of effectivity, often delicate, will be examined in no. VIII.7.

<!-- original page 213 -->

We have seen in [VIII.D], taking into account that fiber products exist in `Sch`, that statement VIII.5.2 is equivalent
to the following:

**Corollary.**

<!-- label: VIII.5.3 -->

A faithfully flat and quasi-compact morphism of preschemes is a universal effective epimorphism.

Since a faithfully flat and quasi-compact morphism remains so after any base extension, we are reduced to proving that
it is an effective epimorphism. We then apply the criterion VIII.5.1 b), which gives the desired result, taking VIII.4.3
and VIII.1.7 into account.

**Corollary.**

<!-- label: VIII.5.4 -->

Let $g: S' \to S$ be a faithfully flat and quasi-compact morphism, let $f: X \to Y$ be an $S$-morphism, and let
$f': X' \to Y'$ be the $S'$-morphism obtained from it by the base change $S' \to S$. Then $f$ is an isomorphism if and
only if $f'$ is an isomorphism.

Indeed, if $f'$ is an isomorphism, it is also an isomorphism for the natural descent structures on $X'$ and $Y'$; and
since the functor $X \mapsto X'$ from $Sch_{/}S$ to the category of objects of $Sch_{/}S'$ with descent data is fully
faithful by VIII.5.2, it follows that $f$ is an isomorphism.

**Corollary.**

<!-- label: VIII.5.5 -->

Under the conditions of VIII.5.4, $f$ is a closed immersion (respectively an open immersion, respectively a
quasi-compact immersion) if and only if $f'$ is.

As usual, one may suppose $Y = S$, and only the “if” direction has to be proved. Notice that the fact that $X'/Y'$ is
endowed with a descent datum relative to $g: Y' \to Y$, and that the structural morphism $f': X' \to Y'$ is an
immersion, hence a monomorphism, implies that the two subobjects of $Y''$ obtained as inverse images of $X'/Y'$ by the
two projections from $S''$ to $S'$ are the same.

<!-- original page 214 -->

If $f'$ is a closed immersion, it follows from VIII.1.9 that there exists a closed subprescheme $X_{1}$ of $Y$ whose
inverse image by $g: Y' \to Y$ is $X'$. Thus, by uniqueness of the solution of a descent problem relative to a morphism
of $\mathcal{F}$-descent, $X_{1}$ is $Y$-isomorphic to $X$, so $f: X \to Y$ is a closed immersion. One proceeds in the
same way for an open immersion, using VIII.4.4. Finally, if $f'$ is a quasi-compact immersion, then $f$ is quasi-compact
by VIII.3.3; therefore one can apply the criterion VIII.4.5 to the subset $f(X)$ of $Y$. This proves that $f(X)$ is
locally closed, since its inverse image $f'(X')$ in $Y'$ is locally closed. Replacing $Y$ by an open subset in which
$f(X)$ is closed, one is reduced to the case where $f'$ is a closed immersion, hence $f$ is one by what precedes.

**Corollary.**

<!-- label: VIII.5.6 -->

Under the conditions of VIII.5.4, $f$ is affine if and only if $f'$ is.

One proceeds as in VIII.5.5, using VIII.2.1. One may also use Serre’s cohomological criterion [EGA II 5.2], which proves
VIII.5.6 without using descent techniques.

**Corollary.**

<!-- label: VIII.5.7 -->

Under the conditions of VIII.5.4, $f$ is integral (respectively finite, respectively finite and locally free) if and
only if $f'$ is.

Only the “if” direction has to be proved, and as usual one may suppose $Y = S$, with $Y$ affine and $Y'$ affine. Since
the hypothesis implies that $f'$ is affine, $f$ is affine as well by VIII.5.6; hence $X$, and consequently $X'$, are
affine. Let $A$, $A'$, $B$, and $B' = B \otimes_{A} A'$ be the rings of $Y$, $Y'$, $X$, and $X'$. One has
$B = colim_{i} B_{i}$, where $B_{i}$ runs through the sub-$A$-algebras of $B$ that are of finite type over $A$; hence
$B' = colim_{i} B_{i}'$, where the $B_{i}'$ are finite-type subalgebras of the $A'$-algebra $B'$. If $B'$ is integral
over $A'$, the $B_{i}'$ are finite-type modules over $A'$; since $A'$ is faithfully flat over $A$, the $B_{i}$ are
finite-type modules over $A$, that is, $B$ is integral over $A$. One sees in the same way that if $B'$ is finite over
$A'$, then $B$ is finite over $A$. The same conclusion holds for “locally free of finite type”; see VIII.1.11.

**Corollary.**

<!-- label: VIII.5.8 -->

<!-- original page 215 -->

Under the conditions of VIII.5.4, suppose $f$ quasi-compact, and let $\mathcal{L}$ be an invertible Module on $X$, with
inverse image $\mathcal{L}'$ on $X'$. Then $\mathcal{L}$ is ample (respectively very ample) relative to $f$ if and only
if $\mathcal{L}'$ is ample (respectively very ample) relative to $f'$.

Only the “if” direction has to be proved. The hypothesis on $\mathcal{L}'$ implies in any case that $f'$ is separated,
hence $f$ is separated by VIII.4.8. Since $f$ is quasi-compact and $g: Y' \to Y$ is flat, the computation of direct
images by affine coverings shows that for every integer $n$ one has isomorphisms

$$
g*(f_{*}(\mathcal{L}^{\otimes }n)) \simeq f'_{*}(\mathcal{L}'^{\otimes }n),
$$

and therefore an isomorphism

$$
g*(\mathcal{S}) \simeq \mathcal{S}',
$$

where $\mathcal{S}$ (respectively $\mathcal{S}'$) denotes the quasi-coherent graded Algebra on $Y$ (respectively on
$Y'$) given by the direct sum of the $f_{*}(\mathcal{L}^{\otimes }n)$ (respectively of the
$f'_{*}(\mathcal{L}'^{\otimes }n)$) for $n \geq 0$. Notice that, for every $n \geq 0$, the cokernel of the canonical
homomorphism $f'_{*}(\mathcal{S}'_{n}) \to \mathcal{L}'^{\otimes }n$ is the inverse image by $X' \to X$ of the cokernel
of $f_{*}(\mathcal{S}_{n}) \to \mathcal{L}^{\otimes }n$; hence its support $Z'_{n}$ is the inverse image of the support
$Z_{n}$. If $\mathcal{L}'$ is ample, the intersection of the $Z'_{n}$ is empty; since $X' \to X$ is surjective, the
intersection of the $Z_{n}$ is empty, that is, one has a canonical morphism

$$
j: X \to \operatorname{Proj}(\mathcal{S})
$$

(EGA II 3). Moreover, the analogous morphism

$$
j': X' \to \operatorname{Proj}(\mathcal{S}')
$$

is none other than the one deduced from the preceding morphism by the base change $Y' \to Y$ (loc. cit.). With this
said, to say that $\mathcal{L}'$ is ample relative to $f'$ means that $j'$ is an immersion, necessarily quasi-compact
since $f'$ is quasi-compact. Thus by VIII.5.5, $j$ is an immersion; that is, $\mathcal{L}$ is ample relative to $f$.

One proceeds in an entirely analogous way in the case of “very ample,” restricting above to $n = 1$ and replacing
$\operatorname{Proj}(\mathcal{S})$ by the projective bundle $\mathcal{P}(\mathcal{S}_{1})$ associated with
$\mathcal{S}_{1}$.

<!-- original page 216 -->

Recall (EGA II 5.1.1) that a quasi-compact morphism $f$ is called **quasi-affine** if, for every affine open $U$ in $Y$,
$f^{-1}(U)$ is a prescheme isomorphic to an open subscheme of an affine scheme. One shows (loc. cit.) that this is
equivalent to saying that $\mathcal{O}_{X}$ is ample (or also very ample) relative to $f$. Thus VIII.5.8 implies:

**Corollary.**

<!-- label: VIII.5.9 -->

Under the conditions of VIII.5.4, and assuming $f$ quasi-compact, $f$ is quasi-affine if and only if $f'$ is.

**Remarks.**

<!-- label: VIII.5.10 -->

Hironaka’s example of a non-projective variety shows that one can have a proper morphism $f: X \to Y$ of nonsingular
algebraic varieties (with $Y$ projective), such that $Y$ is the union of two open subsets $Y_{i}$ for which
$X_{i} = X \times_{Y} Y_{i}$ is projective over $Y_{i}$, while $f$ is not projective. Thus, putting
$Y' = Y_{1} \amalg Y_{2}$, $Y'$ is faithfully flat and quasi-compact (and even quasi-finite) over $Y$, and
$f': X' \to Y'$ is projective, but $f$ is not projective. One must therefore be careful: in order to apply VIII.5.8 and
deduce from the fact that $f'$ is projective the same conclusion for $f$, one must already have on $X'$ an invertible
Module $\mathcal{L}'$ ample for $f'$, **endowed with a descent datum relative to** $X' \to X$. This allows
$\mathcal{L}'$ to be regarded as the inverse image of an invertible Module $\mathcal{L}$ on $X$, which will then be
ample for $f$ by VIII.5.8. When $g: S' \to S$ is finite and locally free, however, see VIII.7.7.

## 6. Application to Finite and Quasi-Finite Morphisms

<!-- label: VIII.6 -->

\[
Translator note: the section title contains a footnote in the source: “Cf. EGA IV 18.12 for generalizations to
preschemes not necessarily locally noetherian.”
\]

We shall prove the following two theorems:

**Theorem.**

<!-- label: VIII.6.1 -->

Let $f: X \to Y$ be a morphism **proper with finite fibers**, with $Y$ locally noetherian. Then $f$ is finite.

**Theorem.**

<!-- label: VIII.6.2 -->

Let $f: X \to Y$ be a **quasi-finite** and **separated** morphism, with $Y$ locally noetherian. Then $f$ is
quasi-affine, and a fortiori quasi-projective.

**Remarks.**

<!-- label: VIII.6.3 -->

<!-- original page 217 -->

Theorem VIII.6.1 is well known, and is due to Chevalley in the case of algebraic varieties. One also finds a simple
proof in [EGA III 4], using the “theorem on formal functions.” The proof given here does not use that theorem, but
instead uses descent theory; we give it as a bonus to the reader, since it comes “for free” at the same time as the
proof of VIII.6.2. Recall also ([EGA III 4] or [VIII.1]) that the global form of Zariski’s “Main Theorem,” deduced from
the “theorem on formal functions,” asserts that if $f: X \to Y$ is quasi-finite and **quasi-projective**, with $Y$
noetherian, then $X$ is $Y$-isomorphic to an open subprescheme of a **finite** $Y$-prescheme $Z$. The conjunction of the
“Main Theorem” and VIII.6.2 is therefore:

**Corollary.**

<!-- label: VIII.6.4 -->

Let $f: X \to Y$ be a quasi-finite and separated morphism, with $Y$ noetherian. Then $X$ is $Y$-isomorphic to an open
subprescheme of a finite $Y$-prescheme $Z$.

Another interesting consequence of VIII.6.2 for descent theory will be given with VIII.7.9.

**Proof of VIII.6.1 and VIII.6.2.** We shall admit the following fact, whose proof is easy:

**Lemma.**

<!-- label: VIII.6.5 -->

Let $X$ be a prescheme of finite type over a locally noetherian $Y$, and let $y \in Y$. Then there exists an open
neighborhood $U$ of $y$ such that $X|U$ is finite (respectively quasi-affine, respectively ...) over $U$ if and only if
$X \times_{Y} \operatorname{Spec}(\mathcal{O}_{y})$ is finite (respectively quasi-affine, respectively ...) over
$\operatorname{Spec}(\mathcal{O}_{y})$.

[Translator note: the source footnote refers to EGA IV 8.]

Since, on the other hand, the property for $f: X \to Y$ of being finite, respectively quasi-affine, is local on $Y$, in
order to prove VIII.6.1 and VIII.6.2 we are reduced to the case where $Y$ is the spectrum of a local ring, and hence has
finite dimension. We proceed by induction on

$$
n = \dim(Y),
$$

the assertion being trivial for $n < 0$.

<!-- original page 218 -->

We may therefore suppose $n \geq 0$ and the assertion proved in all dimensions $n' < n$. Again one may suppose that $Y$
is the spectrum of a noetherian local ring $A$ of dimension $n$. Notice that the hypotheses made in VIII.6.1 and
VIII.6.2 are stable under base change (we already used this in the initial reduction), and they will remain true after
the base change $\operatorname{Spec}(\hat{A}) \to \operatorname{Spec}(A)$. Since the latter is faithfully flat and
quasi-compact, the statements VIII.5.7 and VIII.5.9 reduce us to the case where $A$ is moreover complete.

Using then the fact that every noetherian local ring $B$ over $A$ that is quasi-finite over $A$ is finite over $A$, and
the fact that $X$ is separated over $Y$ and the fiber over $y$ consists of isolated points, one obtains a decomposition

$$
X = X' \amalg X'',
$$

where $X'$ is **finite** over $Y$ and the fiber of $X''$ at $y$ is empty. If $X$ is proper over $Y$, then so is $X''$,
and therefore its image in $Y$ is closed; since it does not contain $y$, it is empty, hence $X'' = \emptyset$ and
$X = X'$. This shows that $X$ is finite over $Y$ and proves VIII.6.1. Notice that the induction hypothesis is not used
here.

If $X$ is quasi-finite over $Y$, then $X''$ is also quasi-finite; but $X''$ in fact lies over the open set $Y - {y}$ of
$Y$, **which has dimension** $< n$. By the induction hypothesis, $X''$ is quasi-affine over $Y - {y}$, hence also over
$Y$. Evidently the same is true for $X'$, and hence for their sum $X$. This proves VIII.6.2.

**Remark.**

<!-- label: VIII.6.6 -->

Theorems VIII.6.1 and VIII.6.2 remain valid if $Y$ is no longer assumed locally noetherian, provided one specifies that
$f$ is assumed to be of finite presentation (cf. VIII.3.6). Indeed, one may again suppose $Y$ affine, and then one
verifies without difficulty that the situation $f: X \to Y$ is deduced, by a base change $Y \to Y_{0}$, from a situation
$f_{0}: X_{0} \to Y_{0}$ satisfying the same hypotheses as $f$, with $Y_{0}$ **noetherian**. Thus by VIII.6.1,
respectively VIII.6.2, $f_{0}$ is finite, respectively quasi-affine, and hence the same is true of $f$. This kind of
argument is often useful for getting rid of noetherian hypotheses, which in applications always end up becoming awkward.

<!-- original page 219 -->

## 7. Effectivity Criteria for a Descent Datum

<!-- label: VIII.7 -->

As usual, consider a morphism of preschemes

$$
g: S' \to S
$$

and an $S'$-prescheme $X'$. In accordance with the general facts of VII, 9, the giving of a descent datum on $X'$
relative to $g$ is equivalent to the giving of an equivalence pair

```text
q₁,q₂: X″ ⇉ X′
```

such that the structural morphism $X' \to S'$ is compatible with this pair and with the equivalence pair

```text
p₁,p₂: S″ = S′ ×_S S′ ⇉ S′
```

defined by $g$, and such that the two squares (or either one of them, which is the same by symmetry) extracted from the
corresponding diagram

$$
X' \leftarrow X''
\downarrow    \downarrow
S' \leftarrow S''
$$

using either $p_{1},q_{1}$ or $p_{2},q_{2}$, are **cartesian**. A solution of the descent problem posed by this descent
datum, that is, an object $X$ over $S$ endowed with an isomorphism $X \times_{S} S' \leftarrow X'$ compatible with the
descent data, is equivalent to the giving of a **cartesian** square

$$
X  \leftarrow X'
\downarrow    \downarrow
S  \leftarrow S'
$$

satisfying $hq_{1} = hq_{2}$.

<!-- original page 220 -->

Since the class of faithfully flat and quasi-compact morphisms is stable under base change, and since a faithfully flat
and quasi-compact morphism is an effective epimorphism by VIII.5.3, the general theory [VIII.D] gives:

**Proposition.**

<!-- label: VIII.7.1 -->

Suppose $g: S' \to S$ faithfully flat and quasi-compact. A descent datum on $X'$ relative to $g$ is effective if and
only if the equivalence relation $R = (q_{1},q_{2})$ that it defines is effective (that is, the quotient $X'/R$ exists
and $X''$ becomes the fiber square of $X'$ over $X'/R$), and the canonical morphism $X' \to X'/R$ is faithfully flat and
quasi-compact.

Thus the question of effectivity of a descent datum is a special case of the question of effectivity of an equivalence
graph, and various effectivity criteria given in this number can be obtained in this way. Nevertheless, in the context
of descent one has Theorem VIII.2.1, which implies that **if $X'$ is affine over $S'$, every descent datum on $X'$
relative to $g$ is effective**; this statement has no analogue for passage to the quotient by a general flat equivalence
graph. All the effectivity criteria we give here can also be regarded as consequences of the preceding statement.

Let $U'$ be a subprescheme of $X'$ (or more generally a subobject of $X'$ in the category `Sch`). We say that $U'$ is
**stable under the descent datum** on $X'$ if one can put on $U'$ a descent datum relative to $g$ such that the
immersion $U' \to X'$ is compatible with the descent data. This also means that the inverse images of $U'$ in $X''$ by
$q_{1}$ and $q_{2}$ are the same (or, as one also says, that $U'$ is **stable under the equivalence relation** $R$). Of
course the descent datum in question on $U'$ is then unique, and is called the **induced descent datum** from that of
$X'$. With this understood:

**Proposition.**

<!-- label: VIII.7.2 -->

Let $(X_{i}')$ be a covering of $X'$ by open subsets $X_{i}'$ stable under the descent datum. The descent datum on $X'$
is effective if and only if the induced descent data on the $X_{i}'$ are effective.

<!-- original page 221 -->

This is an easy consequence of VIII.7.1, for example, and the details of the proof are left to the reader.

**Corollary.**

<!-- label: VIII.7.3 -->

Let $(S_{i})$ be an open covering of $S$, and for each $i$ let $S_{i}'$ and $X_{i}'$ be deduced from $S'$ and $X'$ by
the base change $S_{i} \to S$. The descent datum on $X'$ is effective if and only if, for every $i$, the descent datum
on $X_{i}'$ relative to $g_{i}: S_{i}' \to S_{i}$ is effective.

This criterion almost always reduces us to the case where $S$ is affine. In the case where $S'$ is also affine, which is
the most frequent case in applications, one has:

**Corollary.**

<!-- label: VIII.7.4 -->

Suppose $S$ and $S'$ affine. The descent datum on $X'$ is effective if and only if $X'$ is the union of affine open
subsets $X_{i}'$ stable under the descent datum.

Sufficiency follows from VIII.7.2 and from the fact that, if $X_{i}'$ is affine, it is affine over $S'$ and one can
apply VIII.2.1. For necessity, note that if $X'$ comes from $X$, and if $X$ is covered by affine open subsets $X_{i}$,
then the $X_{i}' = X_{i} \times_{S} S'$ are affine open subsets stable under the descent data and covering $X'$.

**Corollary.**

<!-- label: VIII.7.5 -->

Let $g: S' \to S$ be a faithfully flat, quasi-compact, and **radicial** morphism. Then $g$ is a morphism of
**effective** descent; that is, for every $X'$ over $S'$, every descent datum on $X'$ relative to $g: S' \to S$ is
effective.

Indeed, by VIII.7.3 one may suppose $S$ affine. Since $S'$ is radicial over $S$, hence separated, $S'$ is separated.
Moreover, for every $x' \in X'$, the fiber $R(x') = q_{2}(q^{-1}_{1}(x'))$ of the set-theoretic equivalence relation
defined by $R$ is reduced to one point: since $g$ is radicial, the same is true of $p_{1},p_{2}$, which are deduced from
it by the base change $S' \to S$, and hence also of $q_{1},q_{2}$, which are deduced from the preceding ones by the base
change $X' \to S''$.

<!-- original page 222 -->

Thus **every open subset of $X'$ is stable** under the descent datum. Cover $X'$ by affine open subsets $X_{i}'$. These
are affine over $S$ because $S'$ is separated, so the induced descent datum is effective by VIII.2.1. We then conclude
by VIII.7.2.

Notice that VIII.7.5 gives the only known case of an effective descent morphism in the category of preschemes, and
probably the only case indeed, even if one restricts to noetherian schemes or to schemes of finite type over a field.

When $S$ is assumed locally noetherian and $S'$ of finite type over $S$, statement VIII.7.5 is also a special case of
the following one, which generalizes Weil’s Galois descent and Cartier’s inseparable descent:

**Corollary.**

<!-- label: VIII.7.6 -->

Let $g: S' \to S$ be a finite locally free morphism (that is, defined by an Algebra on $S$ that is a locally free module
of finite type) and surjective. Then $g$ is faithfully flat and quasi-compact, hence a descent morphism. Let $X'$ be an
$S'$-prescheme endowed with a descent datum. This datum is effective if and only if, for every $x' \in X'$, the fiber
$R(x') = q_{2}(q^{-1}_{1}(x'))$ is contained in an affine open subset. This condition is automatically satisfied if $X'$
is quasi-projective over $S'$.

The parenthetical assertion comes from the fact that, if $s$ is the point of $S$ below $x'$, then $R(x')$ is finite and
contained in the fiber $X'_{s}$; on the other hand, since $X'$ is quasi-projective over $S'$ and $S'$ is finite over
$S$, $X'$ is quasi-projective over $S$, which implies that a fiber of $X'$ over $S$ is contained in an affine open
subset.

Since every finite subset of an affine scheme has a fundamental system of affine neighborhoods, one does not lose the
hypothesis by restricting over an affine open subset of $S$; by VIII.7.3 this reduces us to the case where $S$ is
affine. By VIII.7.4, we are reduced to showing that $x'$ is contained

<!-- original page 223 -->

in an affine open subset **stable** under the descent datum. Indeed, let $U$ be an affine open subset containing
$R(x')$. Then the saturation

```text
R(X′ − U) = q₂(q₁⁻¹(X′ − U))
```

does not meet $R(x')$; moreover, since $q_{2}$ is finite (because $g$, hence $p_{2}$, is finite), and therefore closed,
the right-hand side is a closed subset of $X'$. Let $U'$ be its complement in $X'$. This is a **saturated** open subset,
and one has

$$
R(x') \subset U' \subset U,
$$

with $U$ affine, but $U'$ not a priori affine. Since a finite subset $R(x')$ in an affine scheme $U$ has a fundamental
system of affine neighborhoods of the form $U_{f}$, replacing $f$ by its restriction to $U'$ shows that there exists a
section $f$ of $\mathcal{O}_{U}$ such that

```text
R(x′) ⊂ U′_f,    U′_f is affine.
```

Let $U'' = q^{-1}_{1}(U') = q^{-1}_{2}(U')$, still denoting by $q_{1},q_{2}$ the induced morphisms $U'' \to U'$, and
consider

```text
f′ = Norm_q₂(q₁*(f)),
```

where `Norm_q₂` denotes the **norm** relative to the finite locally free morphism $q_{2}: U'' \to U'$. The compatibility
of the formation of the norm with base change easily implies that $f'$ is an **invariant** section:

$$
q_{1}*(f') = q_{2}*(f'),
$$

which implies that ${U'_{f}}'$ is a saturated open subset of $U'$. More precisely, denoting by $Z(f')$ the set of zeros of
a section $f'$, one finds from the properties of norms that

```text
Z(f′) = q₂(Z(q₁*(f))) = q₂(q₁*(Z(f))) = R(U′ − U′_f).
```

<!-- original page 224 -->

This implies that ${U'_{f}}' = U' - Z(f')$ is saturated, contains $R(x')$, and is contained in $U'_{f}$. Since the latter
is affine, it follows that ${U'_{f}}'$ is also affine (being equal to $(U'_{f})_{f}''$, with $f'' = f'$ restricted to
${U'_{f}}'$). It is therefore a saturated affine open subset containing $R(x')$, hence $x'$, which completes the proof.

Notice that this argument applies whenever one has an equivalence relation (or even only a pre-equivalence relation; see
[VIII.3]) in a prescheme $X'$, finite and locally free; indeed VIII.7.6 is also a special case of the analogous result
for finite locally free pre-equivalences, loc. cit. The same remark applies to VIII.7.7 below.

Once the existence of a saturated quasi-affine open subset $U'$ containing $x'$ has been obtained, one can also appeal
to VIII.7.9 and VIII.7.2, which avoids the use of norms.

Notice moreover that under the conditions of VIII.7.6, if the descent datum on $X'$ is effective, with $X'$ coming from
$X$ over $S$, then the morphism $X' \to X$ is finite, locally free, and surjective, since it is deduced from $g$ by the
base change $X \to S$. It follows (EGA II 6.6.4) that if $X'$ is quasi-projective over $S'$, hence over $S$, then $X$ is
quasi-projective over $S$. A relatively ample invertible sheaf on $X$ is obtained by taking the **norm** of an
invertible sheaf on $X'$ relatively ample over $S$, or over $S'$, which is the same thing. Thus one obtains:

**Corollary.**

<!-- label: VIII.7.7 -->

A finite locally free and surjective morphism $g: S' \to S$ is a morphism of effective descent for the fibered category
of preschemes quasi-projective over other preschemes; that is, for every $X'$ quasi-projective over $S'$, every descent
datum on $X'$ relative to $g$ is effective, and the descended $S$-prescheme $X$ is quasi-projective over $S$.

**Proposition.**

<!-- label: VIII.7.8 -->

Let $g: S' \to S$ be a faithfully flat and quasi-compact morphism. Then $g$ is a morphism of effective descent for the
fibered category of preschemes $Z$ quasi-compact

<!-- original page 225 -->

over a prescheme $T$ and endowed with an invertible sheaf ample relative to $T$. In particular, for every prescheme $X'$
over $S'$, endowed with a descent datum relative to $g: S' \to S$, and every invertible sheaf $\mathcal{L}'$ on $X'$
ample relative to $S'$ and likewise endowed with a descent datum relative to the given one on $X'$ (that is, endowed
with an isomorphism from $q_{1}*(\mathcal{L}')$ to $q_{2}*(\mathcal{L}')$, satisfying the usual transitivity condition),
the descent datum on $X'$ is effective, and the invertible sheaf $\mathcal{L}$ on the descended prescheme $X$, deduced
from $\mathcal{L}'$ by descent, is ample relative to $S$.

The proof is entirely analogous to that of VIII.5.8. One notes that on the quasi-coherent graded Algebra $\mathcal{S}'$
on $S'$ defined by $\mathcal{L}'$ there is a descent datum, allowing one to construct a quasi-coherent graded Algebra
$\mathcal{S}$ on $S$ by VIII.1.1, whence a $P = \operatorname{Proj}(\mathcal{S})$ over $S$ such that
$P' = \operatorname{Proj}(\mathcal{S}')$ is identified, together with its descent datum, with $P \times_{S} S'$. Since
by hypothesis $X'$ is identified with an open subset of $P'$, necessarily stable under the descent datum on $P'$, the
descent datum on $X'$ is also effective, and one obtains the descended prescheme as an open subset of $P$. The details
are left to the reader.

In particular, taking $\mathcal{L}' = \mathcal{O}_{X}'$, one finds:

**Corollary.**

<!-- label: VIII.7.9 -->

Let $g: S' \to S$ be a faithfully flat and quasi-compact morphism, and let $X'$ be a **quasi-affine** prescheme over
$S'$. Then every descent datum on $X'$ relative to $g$ is effective, and the descended prescheme $X$ is quasi-affine
over $S$.

By VIII.6.2, this result applies in particular if $S'$ is locally noetherian and $X'$ is quasi-finite and separated over
$S'$; more generally, if $S'$ is arbitrary and $X'$ is of finite presentation, quasi-finite, and separated over $S'$
(cf. VIII.6.6).

**Remarks.**

<!-- label: VIII.7.10 -->

The results given in this number exhaust the currently known effectivity criteria, and probably even all useful existing
criteria. \[Translator note: the corrected source adds that this opinion turned out to be partly erroneous, referring
for example to J.-P. Murre, Séminaire Bourbaki 294 (Appendix), May 1965, and to special results, notably of Néron and
Raynaud; for descent of group schemes, see M. Raynaud’s 1968 thesis.\] Notice the following counterexamples in support
of this assertion:

<!-- original page 226 -->

1. If $S$ is the spectrum of a field, and $S'$ is the spectrum of a quadratic Galois extension, one can find an $X'$
   over $S'$, proper and smooth over $S'$, of dimension 3, endowed with a descent datum that is not effective (Serre).

1. One can find an $S$ equal to the spectrum of a regular local ring of dimension 3 (if desired, the local ring of an
   algebraic scheme over a field of prescribed characteristic), and a principal covering $T$ of $S$ with group
   $\mathbb{Z}/2\mathbb{Z}$, such that, if $t$ denotes one of the points of $T$ above the closed point $s$ of $S$, and
   $S' = T - s$, one can find an $X'$ **projective** over $S'$, regular, endowed with a descent datum relative to
   $g: S' \to S$, this descent datum not being effective.

For these constructions one uses Hironaka’s example of non-projective varieties. For (i), it is enough to use the fact
that one can find over $k$ a proper and smooth scheme $X_{0}$ of dimension 3, on which $G = \mathbb{Z}/2\mathbb{Z}$ acts
without inertia, and in which there exist two rational points `a,b` congruent under $G$ and not contained in any affine
open subset. One then puts $X' = X_{0} \times_{k} k'$, and lets $G$ act on $X'$ through the actions of $G$ on the two
factors; this gives a descent datum on $X'$ relative to $g: \operatorname{Spec}(k') \to \operatorname{Spec}(k)$. Above
$a$, respectively $b$, there is exactly one point $a'$, respectively $b'$, with quadratic residue extension, and $a'$
and $b'$ are congruent under $G$, since $X' \to X_{0}$ is compatible with the actions of $G$. Then $a'$ and $b'$ cannot
be contained in an affine open subset $U'$, for then $U = X_{0} - Im(X' - U')$ would be an open subset of $X_{0}$
containing $(a,b)$, whose inverse image in $X'$ would be contained in $U'$, hence quasi-affine; therefore $U$ would be
quasi-affine, and consequently $(a,b)$ would have an affine neighborhood in $U$.

For (ii), one uses the fact that in Hironaka’s example, $X_{0}$ is obtained as a prescheme proper over a projective
$k$-scheme $Y$, smooth over $k$. The morphism $f: X_{0} \to Y$ is birational, though this is immaterial. The group $G$
also acts on $Y$ compatibly with its actions on $X_{0}$. Finally, putting $S' = Y - f(b)$ and $X' = X_{0}|S'$, $X'$ is
projective over $S'$.

<!-- original page 227 -->

Then $X_{0}$ is endowed with a natural descent datum relative to the canonical morphism $Y \to S = Y/G$, by means of the
actions of $G$ on $X_{0}$ compatible with its actions on $Y$. This descent datum is not effective, since $(a,b)$ is not
contained in an affine open subset. The induced descent datum on $X'$ relative to $g: S' \to S$ is then not effective,
as is easily verified.

## Bibliography

**[VIII.D]** J. Giraud, _Méthode de la descente_, Mémoire no. 2 de la Société Mathématique de France, 1964.

**[VIII.1]** A. Grothendieck, Séminaire Bourbaki: _Géométrie formelle et Géométrie algébrique_, May 1959, no. 182.

**[VIII.2]** A. Grothendieck, Séminaire Bourbaki: _Technique de descente et Théorèmes d’existence I_, December 1959, no.
190\.

**[VIII.3]** A. Grothendieck, Séminaire Bourbaki: _Technique de descente et Théorèmes d’existence III_, February 1961,
no. 212.

[^viii-1-1]: We admit here the general theory of descent set out in detail in the article of J. Giraud cited in the
    footnote to the Warning, a work that we shall cite as [VIII.D] below. Cf. also [VIII.2] for a succinct account.


<!-- SOURCE: 09-descente-des-morphismes-etales.md -->

# Exposé IX. Descent of Étale Morphisms. Application to the Fundamental Group

<!-- label: IX -->

<!-- original page 228 -->

## 1. Reminders on Étale Morphisms

<!-- label: IX.1 -->

We shall review here the properties of étale morphisms, developed in Exposé I, that we shall need, taking the
opportunity to remove the superfluous noetherian hypotheses from the theory. The reader should note that even if one is
interested only in noetherian schemes, descent techniques lead one to introduce non-noetherian schemes, such as
$\operatorname{Spec}(\hat{A} \otimes_{A} \hat{A})$, where $A$ is a noetherian local ring; and in order to apply the
language of fibered categories, it is important to define notions such as étale morphism, etc., without introducing
noetherian restrictions. A reader reluctant to verify or admit that the statements below are true without noetherian
hypotheses may content himself with admitting them under the noetherian hypotheses of Exposé I, provided that the same
noetherian hypotheses are introduced into the statements of the following numbers, and that Definition IX.1.1 below is
used for the non-noetherian schemes that enter the arguments.

**Definition.**

<!-- label: IX.1.1 -->

Let $f: X \to S$ be a morphism of preschemes, and let $x$ be a point of $X$. We say that $f$ is **étale at** $x$, or
that $X$ is étale over $S$ at $x$, if there exist an affine open neighborhood $U$ of $s = f(x)$, an affine open
neighborhood $V$ of $x$ over $U$, a noetherian affine scheme $U_{0}$, an affine $U_{0}$-scheme $V_{0}$ that is étale in
the sense of Exposé I, a morphism $U \to U_{0}$, and a $U$-isomorphism

`V ≃ V₀ ×_U₀ U`.

<!-- original page 229 -->

When $S$ is locally noetherian, this terminology agrees with that of loc. cit. Similarly, we shall say that $f$ **is
étale**, or that $X$ **is étale over** $S$, if $f$ is étale at every point $x$ of $X$. With these definitions, the
propositions below reduce without difficulty to the noetherian case, where they are proved in I.4, I.5, and I.7. For
details, the reader may consult EGA IV. [Translator note: more precisely, EGA IV 17 and 18.]

**Remarks.**

<!-- label: IX.1.2 -->

If $f$ is étale at $x$, then $f$ is “**of finite presentation at** $x$” (VIII.3.5), the local ring of $x$ in the fiber
$f^{-1}(s)$ is a **finite separable extension** of $\kappa(s)$, and $f$ is **flat at** $x$. One can show that the
converse is true; hence Definition IX.1.1 is the same as in the case where $S$ is locally noetherian, except that the
condition “of finite type at $x$” must be replaced by “of finite presentation at $x$.” Since this result has a delicate
proof, we have not wanted to take it here as the definition of an étale morphism, as it does not lend itself directly to
the proof of the properties that follow.

First note the trivial fact:

**Proposition.**

<!-- label: IX.1.3 -->

If $f: X \to S$ is étale, then every morphism $f': X' \to S'$ obtained from it by base change $S' \to S$ is also étale.

Thus one can say that étale morphisms form a **fibered subcategory** of the category of arrows in `Sch` (cf. VI VI.11
a). The object of the present exposé is the study of the exactness properties of this fibered category over `Sch`.

**Proposition.**

<!-- label: IX.1.4 -->

Let $f: X \to S$ be a morphism of preschemes. It is an open immersion if and only if it is étale and radicial.

Cf. I.5.1. It follows that if $X$ is étale over $S$, every section of $X$ over $S$ is an open immersion. Using IX.1.4
once more, one obtains:

**Corollary.**

<!-- label: IX.1.5 -->

Let $X$ be an étale $S$-prescheme. Then there is a one-to-one correspondence between the set of sections of $X$ over $S$
and the set of open subsets $\Gamma$ of $X$ such that the morphism $\Gamma \to S$ induced by the structural morphism is
**radicial** and **surjective**.

<!-- original page 230 -->

If moreover $X$ is separated over $S$, $\Gamma$ will be a subset of $X$ both open and closed, but this is immaterial.
Making the evident base change, one can put IX.1.5 in the following apparently more general form:

**Corollary.**

<!-- label: IX.1.6 -->

Let $X$ and $Y$ be two $S$-preschemes, with $Y$ étale over $S$. Then the map $f \mapsto \Gamma_{f}$ associating to every
$S$-morphism $f$ from $X$ to $Y$ the subset of $X \times_{S} Y$ underlying the graph of $f$ is a bijection from
$\operatorname{Hom}_{S}(X,Y)$ onto the set of open subsets $\Gamma$ of $X \times_{S} Y$ such that the morphism
$\Gamma \to X$ induced by $pr_{1}$ is **radicial** and **surjective**.

**Proposition.**

<!-- label: IX.1.7 -->

Let $S_{0}$ be the subprescheme of $S$ defined by a quasi-coherent nil-ideal, that is, such that $S_{0}$ has the same
underlying set as $S$. Then the functor $X \mapsto X \times_{S} S_{0}$ from the category of preschemes étale over $S$ to
the category of preschemes étale over $S_{0}$ is an equivalence of categories.

The fact that this functor is fully faithful is an immediate consequence of IX.1.6. The fact that it is essentially
surjective is contained in I.8.3. Notice that under the preceding equivalence, $X$ is of finite type, that is,
quasi-finite over $S$ (respectively finite, that is, an étale covering of $S$), if and only if $X_{0}$ satisfies the
analogous condition over $S_{0}$; the same remark applies to separatedness. These facts are immediate, and are also
contained in IX.2.4 below.

**Corollary.**

<!-- label: IX.1.8 -->

Let $A$ be a complete noetherian local ring with residue field $k$. Then the functor $B \mapsto B \otimes_{A} k$ is an
equivalence from the category of finite étale $A$-algebras to the category of finite étale $k$-algebras, that is, finite
direct products of finite separable extensions of $k$.

**Proposition.**

<!-- label: IX.1.9 -->

For $X$ to be an **étale covering** of $S$, that is, finite and étale over $S$, it is necessary and sufficient that $X$
be $S$-isomorphic to the spectrum of an Algebra $\mathcal{A}$ on $S$, which is a locally free Module of finite type, and
such that for every

<!-- original page 231 -->

$s \in S$, $\mathcal{A}_{s} \otimes_{\mathcal{O}_{s}} \kappa(s)$ is a separable algebra over $\kappa(s)$, hence in this
case a direct product of finite separable extensions of $\kappa(s)$.

Finally, the following result is less elementary in nature, being the conjunction of I.8.4 and the **existence theorem
for sheaves in algebraic geometry** (EGA III 5; cf. also [IX.1], theorem 3).

**Theorem.**

<!-- label: IX.1.10 -->

Let $S$ be the spectrum of a complete noetherian local ring, let $X$ be a proper $S$-scheme, and let $X_{0}$ be the
fiber of $X$ at the closed point of $S$, so that $X_{0}$ is a closed subscheme of $X$. Then the restriction functor
$X' \mapsto X' \times_{X} X_{0}$ is an equivalence from the category of étale coverings of $X$ to the category of étale
coverings of $X_{0}$.

## 2. Submersive and Universally Submersive Morphisms

<!-- label: IX.2 -->

**Definition.**

<!-- label: IX.2.1 -->

A morphism $g: S' \to S$ of preschemes is called **submersive** if it is surjective and makes $S$ a quotient topological
space of $S'$; that is, a subset $U$ of $S$ whose inverse image $f^{-1}(U)$ is open is itself open. One says that $f$ is
**universally submersive** if, for every morphism $T \to S$, the morphism $f': T' = S' \times_{S} T \to T$ deduced from
$f$ by base change is submersive.

It is immediate that the composite of two submersive (respectively universally submersive) morphisms is submersive
(respectively universally submersive), and that a base change of a universally submersive morphism is universally
submersive. If `fg` is submersive (respectively universally submersive), then $f$ is so.

**Examples.**

<!-- label: IX.2.2 -->

a) A surjective morphism that is open, or closed, is submersive. Hence a surjective universally closed or universally
open morphism is universally submersive. For example, **a proper surjective morphism is universally submersive**. On the
other hand, **a faithfully flat and quasi-compact morphism is universally submersive** (VIII.4.3). These will be the two
most important cases for us.

<!-- original page 232 -->

One can apply to a submersive or universally submersive morphism $g: S' \to S$ the arguments of VIII.4.3. In particular
one finds:

**Proposition.**

<!-- label: IX.2.3 -->

Suppose $g: S' \to S$ submersive. Then the following diagram of maps is exact:

`Open(S) → Open(S′) ⇉ Open(S″)`,

where $S'' = S' \times_{S} S'$, and where $Open(X)$ denotes the set of open subsets of the prescheme $X$.

**Proposition.**

<!-- label: IX.2.4 -->

Let $g: S' \to S$ be a universally submersive morphism, let $f: X \to Y$ be an $S$-morphism, and let $f': X' \to Y'$ be
the $S'$-morphism deduced from it by base change. For $f$ to be open (respectively closed), it is enough that $f'$ be
so. For $f$ to be universally open, respectively universally closed, respectively separated, it is necessary and
sufficient that $f'$ be so. If in addition $g$ is quasi-compact and $f$ is locally of finite type, then $f$ is proper if
and only if $f'$ is proper.

For this last point, note that if $f'$ is proper, hence quasi-compact, then $f$ is quasi-compact (VIII.3.3), hence of
finite type since it is locally of finite type. On the other hand it is separated and universally closed by what
precedes; therefore it is proper.

**Proposition.**

<!-- label: IX.2.5 -->

Let $S'$ be a prescheme of finite type over the spectrum $S$ of a complete noetherian local ring. Suppose that the fiber
over the closed point $s$ of $S$ is finite, so that the local rings in $S'$ at the points $s'$ of this fiber are finite
over $A = \mathcal{O}_{s}$. Let $S''$ be the sum scheme of the spectra of the $\mathcal{O}_{S',s'}$ in question,
regarded as a finite $S$-scheme. Then $g: S' \to S$ is universally submersive if and only if the structural morphism
$S'' \to S'$ is surjective.

Since there is a natural $S$-morphism $S'' \to S'$, and since a finite surjective morphism is universally submersive by
IX.2.2, the stated condition is sufficient. Conversely, suppose $S'' \to S'$ is not surjective; we show that $g$ is not
universally submersive. Let $t$ be a point of $S$ not in the image of $S''$. There then exists an $S$-scheme $T$, the
spectrum of a discrete valuation ring, whose image in $S$ is `{s,t}`.

<!-- original page 233 -->

Notice that the image of $S''$ in $S'$ is open, because the morphism $S'' \to S'$ is a local isomorphism; moreover this
image contains $S'_{s}$ and does not meet $S'_{t}$. It follows that the inverse image of this open subset in
$T' = S' \times_{S} T$ is **open** and identical with the inverse image of the closed point of $T$. This shows that
$T' \to T$ is not submersive, and hence $S' \to S$ is not universally submersive.

**Remark.**

<!-- label: IX.2.6 -->

Using the criterion IV.6.3 for a constructible subset of a noetherian space to be open, one easily obtains the following
valuative criterion for a morphism $g: S' \to S$ **of finite type**, with $S$ locally noetherian, to be universally
submersive: it is necessary and sufficient that, for every $S$-scheme $T$ that is the spectrum of a discrete valuation
ring, putting $T' = S' \times_{S} T$, the inverse image in $T'$ of the closed point of $T$ be non-open.

## 3. Descent of Morphisms of Étale Preschemes

<!-- label: IX.3 -->

**Proposition.**

<!-- label: IX.3.1 -->

Let $g: S' \to S$ be a **surjective** morphism of preschemes, let $X$ and $Y$ be two preschemes over $S$, and let $X'$,
$Y'$ be their inverse images over $S'$. If $Y$ is unramified over $S$, then the canonical map

$\operatorname{Hom}_{S}(X,Y) \to \operatorname{Hom}_{S'}(X',Y')$

is injective.

Indeed, by IX.1.6, an $S$-morphism $f: X \to Y$ is known once one knows the underlying set of its graph $\Gamma$, which
is a subset of $Z = X \times_{S} Y$. Since

$Z' = Z \times_{S} S' = X' \times_{S'} Y' \to Z$

is surjective (because $S' \to S$ is), this subset $\Gamma$ is known once one knows its inverse image in
$X' \times_{S'} Y'$, which is nothing other than the underlying set of the graph of $f'$. This proves the assertion.

A subset $\Gamma$ of $Z$ is the graph of an $S$-morphism $f: X \to Y$ if and only if it is open and if the morphism
induced by $pr_{1}$ from $\Gamma$ to $X$ is radicial

<!-- original page 234 -->

and surjective; cf. IX.1. When the first property is verified, the second is verified if and only if the inverse image
$\Gamma'$ of $\Gamma$ in $Z'$ satisfies the same condition, by VIII.3.1. If one finally knows that $Z' \to Z$ is
submersive, which will be the case in particular if $S' \to S$ is universally submersive, then $\Gamma$ is open if and
only if $\Gamma'$ is open.

Thus the set $\operatorname{Hom}_{S}(X,Y)$ is then in one-to-one correspondence with the set of open subsets $\Gamma'$
of $Z'$ such that the projection morphism $pr_{1}: Z' \to X'$ is radicial and surjective (that is, corresponding to an
$S'$-morphism $f': X' \to Y'$), and which are saturated for the equivalence relation defined by $Z' \to Z$; that is,
whose two inverse images in $Z'' = Z' \times_{Z} Z' = Z \times_{S} S''$, where $S'' = S' \times_{S} S'$, by the two
projections, are equal. But these latter subsets are the graphs of the two $S''$-morphisms $X'' \to Y''$ deduced from
$f'$ by base change along the two projections $S'' \to S'$. We have therefore obtained:

**Proposition.**

<!-- label: IX.3.2 -->

Let $g: S' \to S$ be a **universally submersive** morphism of preschemes, let $S'' = S' \times_{S} S'$, let $X$ and $Y$
be two $S$-preschemes, let $X'$ and $Y'$ be their inverse images over $S'$, and let $X''$ and $Y''$ be their inverse
images over $S''$. If $Y$ is étale over $S$, then the following canonical diagram of maps is exact:

`Hom_S(X,Y) → Hom_{S′}(X′,Y′) ⇉ Hom_{S″}(X″,Y″)`.

Taking $X$ and $Y$ étale over $S$, one obtains the following statement, which moreover gives back IX.3.2, even if one
restricts to $X = S$; indeed in IX.3.2 one can always reduce to that case by the base change $X \to S$.

**Corollary.**

<!-- label: IX.3.3 -->

A universally submersive morphism of preschemes is a descent morphism for the fibered category of preschemes étale over
other preschemes.

I do not know, however, whether it is necessarily a morphism of **effective** descent for the fibered category in
question, even under the additional hypotheses that $S$ be noetherian and $g$ of finite type, and even restricting to
étale coverings. We shall nevertheless give useful criteria of effectivity in the next number.

**Corollary.**

<!-- label: IX.3.4 -->

<!-- original page 235 -->

Let $g: S' \to S$ be a universally submersive morphism whose fibers $g^{-1}(s)$ are “geometrically connected,” that is,
for every extension $K/\kappa(s)$, $g^{-1}(s) \otimes_{\kappa(s)} K$ is connected. Then $S'$ is connected if $S$ is. The
functor from the category of preschemes étale over $S$ to the category of preschemes étale over $S'$ defined by $g$ is
fully faithful.

A subset of $S'$ that is both open and closed is saturated for the set-theoretic equivalence relation defined by $g$,
since the fibers are connected; it is therefore the inverse image of a subset of $S$, necessarily both open and closed
because $g$ is submersive. Thus if $S$ is connected, $S'$ is connected.

This also implies the following fact: the composite `fg` of two morphisms with universally connected fibers, with $f$
universally submersive, has universally connected fibers; if $S_{1}'$ and $S_{2}'$ over $S$ have universally connected
fibers, the same is true of $S_{1}' \times_{S} S_{2}'$. In particular, under the conditions of IX.3.4, $S''$ has
universally connected fibers over $S$.

Let $X$ and $Y$ be étale over $S$, and let $u'$ be an $S'$-morphism from $X'$ to $Y'$. We prove that it is compatible
with the descent data, which gives the desired conclusion by IX.3.3. Let $u_{1}''$ and $u_{2}''$ be the two $S''$-morphisms
$X'' \to Y''$ deduced from $u'$. The subprescheme of $S''$ on which $u_{1}''$ and $u_{2}''$ coincide is an induced open subprescheme,
fiberwise closed, as the inverse image of the diagonal prescheme of $Y''$ over $S''$. \[Translator note: the source
footnote observes that the fibers of $S'$ over $S$ are separated.\] It is therefore the inverse image of a subset of
$S$. Since it contains the diagonal in $S''$, it is all of $S''$. Hence $u_{1}'' = u_{2}''$, as required.

## 4. Descent of Étale Preschemes: Effectivity Criteria

<!-- label: IX.4 -->

**Proposition.**

<!-- label: IX.4.1 -->

Let $g: S' \to S$ be a faithfully flat and quasi-compact morphism. Then $g$ is a morphism of effective descent for the
fibered category of preschemes étale, separated, and of finite type over other preschemes.

Indeed, it is a descent morphism for the fibered category in question, by IX.3.3 or by VIII.5.2. It remains to show that
if $X'$ is étale, separated, and of finite type over $S'$, and endowed with a descent datum relative to $g: S' \to S$,
then this datum is effective in the fibered category in question. But one sees easily that if $X$ is a prescheme over
$S$, then it is étale over $S$ if and only if it is étale over $S'$, by Definition IX.1.1 and VIII.3.6. Hence it is
étale, separated, and of finite type over $S$ if and only if $X'$ is so over $S'$; cf. for example IX.2.4.

<!-- original page 236 -->

It is therefore enough to ensure effectivity of the descent datum on $X$ for the fibered category of arrows of `Sch`.
But $X'$ is quasi-affine over $S'$ by VIII.6.2 and VIII.6.6. One can then conclude using VIII.7.9. Notice that if one
restricts to preschemes étale and **finite** over others, the proof requires less, since one can invoke VIII.2.1
directly.

**Corollary.**

<!-- label: IX.4.2 -->

Let $g: S' \to S$ be a universally submersive morphism, let $X'$ be an $S'$-prescheme étale, separated, and of finite
type, endowed with a descent datum relative to $g$, and let $S_{1} \to S$ be faithfully flat and quasi-compact. Let
$S_{1}'$ and $X_{1}'$ be deduced from $S'$ and $X'$ by base change, so that $S_{1}' \to S_{1}$ is universally submersive
and $X_{1}'$ is étale, separated, and of finite type over $S_{1}'$, endowed with a descent datum relative to
$g_{1}: S_{1}' \to S_{1}$. Then the descent datum on $X'$ is effective if and only if the descent datum on $X_{1}'$ is
effective.

This follows from descent theory in categories [IX.D], taking IX.4.1 and IX.3.3 into account.

Similarly one proves:

**Corollary.**

<!-- label: IX.4.3 -->

Let $g: S' \to S$ be a universally submersive morphism, let $X'$ be an $S'$-prescheme étale and endowed with a descent
datum relative to $g$, and let $(S_{i})$ be an open covering of $S$. Then the descent datum is effective if and only if,
for every $i$, the corresponding descent datum on $X_{i}' = X' \times_{S} S_{i}$, relative to the morphism
$g_{i}: S_{i}' = S' \times_{S} S_{i} \to S_{i}$, is effective.

This last result leads to a local effectivity criterion:

**Proposition.**

<!-- label: IX.4.4 -->

Let $g: S' \to S$ be a morphism of finite presentation (VIII.3.6) and universally submersive, let $X'$ be a prescheme
étale and of finite presentation over $S'$, endowed with a descent datum relative to $g$, and let $a$ be a point of $S$.

<!-- original page 237 -->

Then there exists an open neighborhood $U$ of $a$ such that the corresponding descent datum on
$X_{U}' = X' \times_{S} U$ relative to

$g_{U}: S_{U}' = S' \times_{S} U \to S_{U} = U$

is effective if and only if the corresponding descent datum on
$X_{a}' = X' \times_{S} \operatorname{Spec}(\mathcal{O}_{a})$, relative to

$g_{a}: S_{a}' = S' \times_{S} \operatorname{Spec}(\mathcal{O}_{a}) \to S_{a} = \operatorname{Spec}(\mathcal{O}_{a})$,

is effective.

Necessity is trivial; let us prove sufficiency. We have an étale prescheme of finite type $X_{a}$ over $S_{a}$, and an
isomorphism

$(*)  X_{a}' \simeq X_{a} \times_{S_{a}} S_{a}'$

compatible with the descent data. By a standard and easy sorites on preschemes defined over an inductive limit of rings
(here the rings $A_{f}$, where $A$ is the ring of an affine open neighborhood of $a$, and $f$ runs through the elements
of $A$ not in the prime ideal corresponding to $a$), one can find an open neighborhood $U$ of $a$, an étale prescheme of
finite type `X_U` over $U = S_{U}$, and an $S_{a}$-isomorphism $X_{a} \simeq X_{U} \times_{S_{U}} S_{a}$. Moreover,
after taking $U$ small enough, one may suppose that the isomorphism `(*)` comes from an isomorphism

$X_{U}' \simeq X_{U} \times_{S_{U}} S_{U}'$.

The latter might not be compatible with the descent data; however, after shrinking $U$, it will be compatible with them.
This completes the proof.

**Corollary.**

<!-- label: IX.4.5 -->

Under the conditions of IX.4.4, the descent datum on $X'$ is effective if and only if, for every $a \in S$, the
corresponding descent datum on $X_{a}'$ relative to the morphism
$S_{a}' = S' \times_{S} \operatorname{Spec}(\mathcal{O}_{a}) \to \operatorname{Spec}(\mathcal{O}_{a})$ is effective.
When $S$ is locally noetherian and $X'$ is separated over $S'$, one may also replace $\mathcal{O}_{a}$ by its completion
in the preceding criterion.

<!-- original page 238 -->

The first assertion follows from IX.4.4 and IX.4.3, and the second is then a consequence of IX.4.2. Using IX.4.2 once
more, and the fact that for every noetherian local ring $A$ one can find a complete noetherian local ring $B$ and a
local homomorphism $A \to B$ such that $B$ is flat over $A$ and $B/\mathfrak{m}B$ is any prescribed extension of the
residue field $k = A/\mathfrak{m}$ of $A$, one obtains:

**Corollary.**

<!-- label: IX.4.6 -->

Under the conditions of IX.4.4, suppose in addition that $X'$ is separated over $S'$ and that $S$ is locally noetherian.
Then the descent datum on $X'$ is effective if and only if, for every prescheme $S_{1}$ over $S$ that is the spectrum of
a complete local ring with algebraically closed residue field, the corresponding descent datum on
$X_{1}' = X' \times_{S} S_{1}$, relative to $g_{1}: S_{1}' \to S_{1}$, is effective.

**Theorem.**

<!-- label: IX.4.7 -->

Let $g: S' \to S$ be a finite, surjective morphism of finite presentation (the last hypothesis follows from the others
if $S$ is locally noetherian). \[Translator note: the source footnote says that in fact it is enough for $g$ to be
integral, by a limit argument in the style of EGA IV 8.\] Then $g$ is a morphism of effective descent for the fibered
category of preschemes étale, separated, and of finite type over other preschemes.

We must show that if $X'$ is étale, separated, and of finite type over $S'$, and endowed with a descent datum relative
to $g$, then this datum is effective. Using IX.4.3, one easily reduces to the case where $S$ is noetherian. By IX.4.5,
one may then suppose $S$ is the spectrum of a noetherian local ring, hence in particular

$\dim S = n < +\infty$.

We argue by induction on $\dim S = n$, the assertion being trivial for $n < 0$. Suppose therefore $n \geq 0$ and the
theorem proved in dimensions $n' < n$. By IX.4.6 we are reduced to the case where $S$ is the spectrum of a complete
local ring; then $S'$ is a finite union of spectra of complete local rings. Hence

$X' = X_{1}' \amalg X_{2}'$,

where $X_{1}'$ is **finite** over $S'$, and $X_{2}'$ has no point above any of the closed points

<!-- original page 239 -->

of $S'$. Consider the morphisms

`q₁,q₂: X″ ⇉ X′`

corresponding to the descent datum, compatible with `p₁,p₂: S″ ⇉ S′`. One sees at once that

$X'' = q^{-1}_{i}(X_{1}') \amalg q^{-1}_{i}(X_{2}')$, $i = 1,2$,

is the analogous canonical decomposition of $X''$ over $S''$. This implies $q^{-1}_{1}(X_{1}') = q^{-1}_{2}(X_{1}')$,
and consequently $X_{1}'$ and $X_{2}'$ carry induced descent data.

Let $T$ be the open subset of $S$ complementary to its closed point. Then $T' = S' \times_{S} T$ is the part of $S'$
complementary to the set of closed points, and $X_{2}'$, which lies entirely over $T'$, is endowed with a descent datum
relative to the morphism $T' \to T$ induced by $g$. Since the latter is finite surjective and $\dim T < \dim S = n$,
this descent datum is effective by the induction hypothesis. Thus it remains only to prove that the descent datum on
$X_{1}'$ is effective; we may therefore suppose from now on that $X'$ is étale and **finite** over $S'$. Notice that the
induction argument is unnecessary if one restricts statement IX.4.7 to étale coverings.

Let $S_{0}$ be the spectrum of the residue field of $A$, let $S_{0}' = S' \times_{S} S_{0}$, and define $S_{0}''$,
$S_{0}'''$ similarly from the fiber squares and cubes $S''$ and $S'''$ of $S'$ over $S$. By IX.1.8, the morphisms
$S_{0} \to S$, $S_{0}' \to S'$, etc. induce equivalences for the categories of étale coverings of $S$ and $S_{0}$, of
$S'$ and $S_{0}'$, etc. From the sorites of descent theory in categories [IX.D], it follows that $g: S' \to S$ is a
morphism of effective descent for the fibered category of étale coverings if and only if the same is true of
$g_{0}: S_{0}' \to S_{0}$. But this is indeed the case, for example as a special case of IX.4.1. This completes the
proof.

**Corollary.**

<!-- label: IX.4.8 -->

The conclusion of IX.4.7 remains true if one assumes only that $S' \to S$ is universally submersive, of finite type, and
quasi-finite, provided that $S$ is locally noetherian.

<!-- original page 240 -->

Indeed, by IX.4.6, one may suppose that $S$ is the spectrum of a complete noetherian local ring. Then by IX.2.5, there
exists a finite surjective morphism $S_{1} \to S$ and an $S$-morphism $S_{1} \to S'$. Since $S_{1} \to S$ is a strict
universal descent morphism for the fibered category under consideration by IX.4.7, and since $S' \to S$ is a universal
descent morphism for it, IX.4.8 follows from the general sorites [IX.D].

**Corollary.**

<!-- label: IX.4.9 -->

Let $g: S' \to S$ be a morphism of finite type, surjective and universally open, with $S$ locally noetherian. Then $g$
is a morphism of effective descent for the fibered category of preschemes étale, separated, and of finite type over
other preschemes.

Proceeding as in IX.4.7, one is reduced to the case where $S$ is the spectrum of a complete noetherian local ring $A$.
Let $A_{1}$ be a finite $A$-algebra, with spectrum $S_{1}$, such that $S_{1} \to S$ is finite and **surjective**, hence
a universal effective descent morphism for the fibered category under consideration by IX.4.7. It follows from the
general theorems [IX.D] that $g$ is a morphism of effective descent for that fibered category if and only if the
corresponding morphism $g_{1}: S_{1}' = S' \times_{S} S_{1} \to S_{1}$ is so. Since the latter satisfies the same
hypotheses as $g$, we are reduced to proving IX.4.9 for $S_{1}$ in place of $S$.

Taking first for $A_{1}$ the direct product of the $A/\mathfrak{p}_{i}$, for the minimal prime ideals $\mathfrak{p}_{i}$
of $A$, we are reduced to the case where $A$ is **integral**. One then shows [Translator note: the source refers to EGA
IV 14.3.13 and 14.5.4] that there exists an integral subscheme $S_{1}$ of $S'$, quasi-finite over $S$ and dominant over
$S$, passing through a point of the fiber of $S'$ over the closed point $y$ of $S$. This uses the fact that $S'$ is
universally open of finite type over the integral noetherian local $S$ and that $S'_{y}$ is nonempty. Since $A$ is
complete, $S_{1}$ is finite over $S$, and since it dominates $S$, the morphism $S_{1} \to S$ is surjective. Replacing
$S$ once more by $S_{1}$, we are reduced to the case where $S'$ has a section over $S$, where the statement is trivial.

**Theorem.**

<!-- label: IX.4.10 -->

Let $g: S' \to S$ be a finite radicial surjective morphism of finite presentation. The last condition is superfluous if
$S$ is locally noetherian. \[Translator note: the source footnote says it even suffices that $g$ be integral, radicial,
and surjective, by an easy reduction to the case in the text, in the style of EGA IV 8; cf. SGA 4 VIII 1.1.\]

<!-- original page 241 -->

Then the inverse image functor induces an equivalence from the category of preschemes étale over $S$ to the category of
preschemes étale over $S'$.

Since the diagonal morphisms from $S'$ into $S' \times_{S} S'$ and $S' \times_{S} S' \times_{S} S'$ are surjective
immersions, they induce, by IX.1.9, equivalences from the categories of preschemes étale over $S' \times_{S} S'$,
respectively $S' \times_{S} S' \times_{S} S'$, with the category of preschemes étale over $S'$. It follows from the
descent sorites [IX.D] that every $X'$ étale over $S'$ is endowed with one and only one descent datum relative to
$g: S' \to S$. Hence IX.3.3 implies that the inverse image functor by $g$, from preschemes étale over $S$ to preschemes
étale over $S'$, is **fully faithful**. It remains to show that it is essentially surjective, that is, that every $X'$
étale over $S'$ is isomorphic to the inverse image of an $X$ étale over $S$. Since the question is plainly local on $S$
**and on** $X'$, one may suppose $S$, $S'$, and $X'$ affine. Then $X'$ is separated and of finite type over $S'$, and
one can apply the effectivity criterion IX.4.7.

**Corollary.**

<!-- label: IX.4.11 -->

The conclusion of IX.4.9 remains true if the hypothesis on $g$ is replaced by: $g$ is faithfully flat, quasi-compact,
and radicial.

The proof is the same, invoking IX.4.1 instead of IX.4.7.

Notice that the proof of IX.4.7 is “elementary” in that it does not use the finiteness and comparison theorems for
proper morphisms (EGA III 3, 4, 5). This is no longer true of the following result:

**Theorem.**

<!-- label: IX.4.12 -->

Let $g: S' \to S$ be a proper, surjective morphism of finite presentation (the last hypothesis follows from the first if
$S$ is locally noetherian). Then $g$ is a morphism of effective descent for the fibered category of étale coverings of
preschemes.

By IX.3.3 and IX.2.2, we are reduced to proving that for every étale covering $X'$ over $S'$, endowed with a descent
datum relative to $g: S' \to S$, this descent datum is effective. Using IX.4.3, one is easily reduced

<!-- original page 242 -->

to the case where $S$ is noetherian; using IX.4.6, one may then suppose that $S$ is the spectrum of a **complete**
noetherian local ring $A$. Introduce $S''$ and $S'''$ as usual, let $S_{0}$ be the spectrum of the residue field of $A$,
and let $S_{0}'$, $S_{0}''$, $S_{0}'''$ be deduced from $S'$, $S''$, $S'''$ by the base change $S_{0} \to S$, that is,
the fibers of $S'$, $S''$, $S'''$ at the closed point of $S$. By IX.1.10, the morphisms $S_{0} \to S$, $S_{0}' \to S'$,
etc. induce equivalences from the category of étale coverings over the target scheme with the category of étale
coverings over the source scheme. Consequently, $g: S' \to S$ is a strict descent morphism for the fibered category of
étale coverings of preschemes if and only if $g_{0}: S_{0}' \to S_{0}$ is so; this is indeed the case by IX.4.1. This
completes the proof of IX.4.12.

In this argument, from IX.1.10 one needed only the fact that the functor considered there is **fully faithful**, which
does **not** use the existence theorem for coherent sheaves in algebraic geometry.

## 5. Translation in Terms of the Fundamental Group

<!-- label: IX.5 -->

Let

$g: S' \to S$

be a **morphism of effective descent** for the fibered category of **étale coverings** of preschemes, for example a
proper, surjective morphism of finite presentation (IX.4.12), or a faithfully flat and quasi-compact morphism.
Introducing as usual $S''$ and $S'''$, and denoting by $\mathcal{C}$, $\mathcal{C}'$, $\mathcal{C}''$, $\mathcal{C}'''$
the categories of étale coverings of $S$, $S'$, $S''$, $S'''$ respectively, one has a 2-exact diagram of categories

`𝓒 → 𝓒′ ⇉ 𝓒″ ⇉⇉ 𝓒‴`

corresponding to the diagram

$S \leftarrow S' \Leftarrow S'' \Leftarrow\Leftarrow S'''$.

<!-- original page 243 -->

Suppose that the preschemes $S$, $S'$, $S''$, $S'''$ are disjoint sums of connected preschemes; this is the case in
particular if they are locally connected, hence a fortiori if they are locally noetherian (for example if $S'$ is of
finite type over a locally noetherian $S$). Then the categories $\mathcal{C}$, $\mathcal{C}'$, ... in the preceding
diagram are multigaloisian categories (V.9), each described by a collection of totally disconnected compact topological
groups, namely the fundamental groups of the connected components of $S$, $S'$, $S''$, $S'''$.

For simplicity we suppose $S$ connected, and we shall give a calculation procedure for its fundamental group in terms of
the fibered category formed from $\mathcal{C}'$, $\mathcal{C}''$, $\mathcal{C}'''$, made explicit using the fundamental
groups expressing these categories. The reader should note that the sketched procedure is in fact valid in the general
setting of multigaloisian categories, which need not come from given preschemes $S$, $S'$, $S''$, $S'''$. It is the
analogue of the well-known procedure for calculating the fundamental group of a topological space $S$, a locally finite
union of closed subspaces $S_{i}$ (or an arbitrary union of open subspaces $S_{i}$), from the fundamental groups of the
components of the $S_{i}$ and of the components of $S_{i} \cap S_{j}$. Of course, the analogous situation for preschemes
fits exactly into the general framework of descent by introducing the prescheme $S'$ that is the sum of the $S_{i}$ and
the canonical morphism $g: S' \to S$.

Put

$E' = \pi_{0}(S')$, $E'' = \pi_{0}(S'')$, $E''' = \pi_{0}(S''')$,

where $\pi_{0}$ denotes the functor “set of connected components.” Since the fiber products of $S'$ over $S$ form a
simplicial object of `Sch`, applying $\pi_{0}$ gives a simplicial set whose components in dimensions `0, 1, 2` are $E'$,
$E''$, $E'''$. We shall use the simplicial maps

$q_{i} = \pi_{0}(p_{i})$, $i = 1,2$, $q_{ij} = \pi_{0}(p_{ij})$, $(i,j) = (2,1),(3,2),(3,1)$.

Objects of $E'$ will be denoted with a prime, such as $s'$; objects of $E''$ and $E'''$ will be denoted with double and
triple primes. The fact that $S$ is connected is expressed by $\pi_{0}(K) = 0$, where $K$ is the simplicial set defined
by $g: S' \to S$; equivalently, the equivalence relation in $E'$ generated by the pair of maps $(q_{1},q_{2})$ is
transitive.

<!-- original page 244 -->

Choose once and for all an element $s_{0}'$ in $E'$, and for each $s'$ in $E'$ choose an element $\bar{s}' \in E''$ such that
$q_{1}(\bar{s}') = s_{0}'$ and $q_{2}(\bar{s}') = s'$, thereby displaying the connectedness of $S$. \[Translator note: the source footnote
warns that such an element need not exist in all cases; the stated theorem must then be modified, though the corollaries
remain valid.\] For every $s' \in E'$ choose a geometric point underlined $s'$ in the connected component $s'$ of $S'$;
this point enters in fact through the corresponding fiber functor $F_{s'}'$ on the multigaloisian category $\mathcal{C}'$. The
automorphism group of this functor, that is, the fundamental group of $S'$ at that geometric point, will be denoted
$\pi_{s'}$. Choose similarly geometric points underlined $s''$ and underlined $s'''$, giving fiber functors $F_{s''}''$ and
$F_{s'''}'''$ and fundamental groups $\pi_{s''}$ and $\pi_{s'''}$. Thus

$\pi_{s'}  = \pi_{1}(S', underlined s')$, $\pi_{s''}  = \pi_{1}(S'', underlined s'')$,
$\pi_{s'''}  = \pi_{1}(S''', underlined s''')$.

For every $s'' \in E''$, $p_{1}(underlined s'')$ lies in the same connected component as underlined $q_{1}(s'')$, so
there is an isomorphism of fiber functors

$F_{s''}'' \circ p^{*}_{1} \simeq F_{q_{1}(s'')}'$

that is, a “path class” from $p_{1}(underlined s'')$ to underlined $q_{1}(s'')$. The same observation applies to $q_{2}$
and to the $q_{ij}$. Choose all these path classes:

$F_{s''}'' \circ p^{*}_{i} \simeq F_{q_{i}(s'')}'$, $F_{s'''}''' \circ p^{*}_{ij} \simeq F_{q_{ij}(s''')}''$,

for $i = 1,2$ and $(i,j) = (2,1),(3,2),(3,1)$. They give in particular group homomorphisms

$q^{s''}_{i}: \pi_{s''} \to \pi_{q_{i}(s'')}$, $q^{s'''}_{ij}: \pi_{s'''} \to \pi_{q_{ij}(s''')}$.

<!-- original page 245 -->

Finally, recall that the split fibered-category structure with fibers $\mathcal{C}'$, $\mathcal{C}''$, $\mathcal{C}'''$
also contains isomorphisms of functors

$p^{*}_{21} p^{*}_{1} \simeq p^{*}_{31} p^{*}_{1}$, $p^{*}_{21} p^{*}_{2} \simeq p^{*}_{32} p^{*}_{1}$,
$p^{*}_{31} p^{*}_{2} \simeq p^{*}_{32} p^{*}_{2}$,

deduced from isomorphisms of the two sides respectively with $u^{*}_{i}$ ($i = 1,2,3$), where $u_{i}$ are the three
projections from $S'''$ to $S'$. Making these data explicit, one finds for every $s'''$ a well-determined element

$a^{s'''}_{i} \in \pi_{v_{i}(s''')}$,

where $v_{i}$, $i = 1,2,3$, are the three maps $E''' \to E'$ defined by $v_{i} = \pi_{0}(u_{i})$, subject to the
compatibility conditions such as

$q^{s_{1}''}_{1} q^{s'''}_{21} = int(a^{s'''}_{1}) q^{s_{2}''}_{1} q^{s'''}_{31}$,

with $s_{1}'' = q_{21}(s''')$, $s_{2}'' = q_{31}(s''')$, and the two analogous conditions involving $a_{2}$ and $a_{3}$.

The data just described allow one to reconstruct, up to equivalence of fibered categories, the fibered category with
fibers $\mathcal{C}'$, $\mathcal{C}''$, $\mathcal{C}'''$. Hence in principle they must allow one to reconstruct
$\mathcal{C}$ up to equivalence, and therefore its fundamental group up to isomorphism. In fact, we shall determine the
fundamental group at the geometric point $p(underlined s_{0}')$ of $S$, that is, the automorphism group of
$F_{s_{0}'}' \circ p^{*}$.

An object $X'$ of $\mathcal{C}'$ is essentially the same as the data of finite sets $X'_{s'}$, for $s' \in E'$, on which
the $\pi_{s'}$ act continuously.

<!-- original page 246 -->

A gluing datum on such an object is then the giving, for every $s'' \in E''$, of a bijection

$\phi_{s''}: X'_{q_{1}(s'')} \simeq X'_{q_{2}(s'')}$

compatible with the actions of $\pi_{s''}$, acting on the two sides through the homomorphisms
$q^{s''}_{i}: \pi_{s''} \to \pi_{q_{i}(s'')}$. Taking first the $s''$ of the form $\bar{s}'$, one sees that such data
define bijections

$\psi_{s'}: {{X'_{s_{0}}}'} = F_{0}'(X') \to X'_{s'}$,

which allow all the $X'_{s'}$ to be identified with the same set $F_{0}'(X') = {{X'_{s_{0}}}'}$, on which all the groups
$\pi_{s'}$ will then act. With this understood, the bijections $\phi_{s''}$ correspond to bijections

$g_{s''}: F_{0}'(X') \simeq F_{0}'(X')$,

subject first to the commutation relations with $\pi_{s''}$:

a) $g_{s''} q^{s''}_{1}(g'') = q^{s''}_{2}(g'') g_{s''}$ for $s'' \in E''$ and $g'' \in \pi_{s''}$,

and also to the relations

b) $g_{\bar{s}'} = g_{\bar{s}_{0}'}$ for $s' \in E'$,

which express the way in which we identified the $X'_{s'}$ with one another. Making explicit the condition that such a
gluing datum is in fact a descent datum gives the relations

c) $a^{s'''}_{3} g_{q_{31}(s''')} a^{s'''}_{1} = g_{q_{32}(s''')} a^{s'''}_{2} g_{q_{21}(s''')}$ for $s''' \in E'''$.

This gives an equivalence between the category of objects of $\mathcal{C}'$ endowed with a descent datum

<!-- original page 247 -->

and the category of finite sets on which the groups $\pi_{s'}$ act continuously, endowed in addition with bijections
$g_{s''}$ satisfying relations a), b), c). Let $G$ be the group generated by the groups $\pi_{s'}$ and the new
generators $g_{s''}$, subject to relations a), b), c), and let $\pi$ be the inverse limit of the quotients of $G$ by
subgroups of finite index whose inverse images in the groups $\pi_{s'}$ are open subgroups. One also says that $\pi$ is
the **group of galoisian type generated by the $\pi_{s'}$ and the $g_{s''}$, subject to relations a), b), c)**. One
checks at once that the category under consideration is also equivalent to the category of finite sets on which the
topological group $\pi$ acts continuously. This proves:

**Theorem.**

<!-- label: IX.5.1 -->

Let $g: S' \to S$ be a morphism of preschemes that is a morphism of effective descent for the fibered category of étale
coverings of preschemes (cf. IX.4.9 and IX.4.12). Suppose $S$ connected, and suppose $S'$, its fiber square $S''$, and
its fiber cube $S'''$ are sums of connected preschemes (for example, this holds if $S'$ is of finite type over a locally
noetherian connected $S$). Choose as above: a geometric point in every connected component of $S'$, $S''$, $S'''$;
certain path classes; an $s_{0}' \in E'$; and for every $s' \in E'$ an $s'' \in E''$ whose two images in $E'$ are
$s_{0}'$ and $s'$. Here $E'$, $E''$, $E'''$ denote the sets of connected components of $S'$, $S''$, $S'''$ respectively.
Then the fundamental group of $S$ at the geometric point image of $s_{0}'$ is canonically isomorphic to the group of
galoisian type generated by the $\pi_{s'} = \pi_{1}(S', underlined s')$, for $s' \in E'$, and generators $g_{s''}$, for
$s'' \in E''$, subject to relations a), b), c) above, involving the elements of the groups
$\pi_{s''} = \pi_{1}(S'', underlined s'')$ and the elements $a^{s'''}_{i}$, for $i = 1,2,3$ and $s''' \in E'''$,
introduced above.

**Corollary.**

<!-- label: IX.5.2 -->

Suppose $S'$ and $S''$ have only finitely many connected components, and that the fundamental groups of the connected
components of $S'$ are topologically finitely generated. Then the fundamental group of $S$ is topologically finitely
generated.

<!-- original page 248 -->

Thus we shall prove later that the fundamental group of a normal projective scheme over an algebraically closed field is
topologically finitely generated. Using Chow’s lemma and normalization of algebraic schemes, it will follow that the
same result is true for every proper scheme over an algebraically closed field.

**Corollary.**

<!-- label: IX.5.3 -->

Suppose $S'$, $S''$, $S'''$ have only finitely many connected components, that the fundamental groups of the connected
components of $S'$ are topologically **finitely presented**, and that the fundamental groups of the connected components
of $S''$ are topologically **finitely generated**. Then the fundamental group of $S$ is topologically **finitely
presented**.

One may express IX.4.9 (restricted to étale **coverings**) by saying that **a finite radicial surjective morphism of
noetherian preschemes induces an isomorphism of fundamental groups**. Figuratively, one can therefore say that the
fundamental group is a **topological invariant** for preschemes. More generally, with the help of IX.5.1, one can make
explicit the effect on the fundamental group of operations on preschemes, such as “pinching” a prescheme along a finite
set of points, which have a simple topological meaning. For example:

**Corollary.**

<!-- label: IX.5.4 -->

Let $g: S' \to S$ be a finite morphism of finite presentation, and let $T$ be a discrete subset of $S$. For every
$s \in S$, let $n(s)$ be the “geometric number of points” in the fiber $g^{-1}(s)$, which can also be made explicit as
the separable degree of $g^{-1}(s)$ over $\kappa(s)$, the sum of the separable degrees of its residue extensions.
Suppose that for $s \in S - T$ one has $n(s) = 1$. For every $s \in T$, let $K_{s}$ be an algebraically closed extension
of $\kappa(s)$, let $I_{s}$ be the set of geometric points of $S'$ with values in $K_{s}$ (a set with $n(s)$ elements),
let $I_{s}'$ be the complement of one chosen point of $I_{s}$, and let $I'$ be the union of the $I_{s}'$. Suppose $S'$
connected. Then the fundamental group of $S$ is isomorphic to the group of galoisian type generated by the fundamental
group of $S'$ and generators $g_{i}$ for $i \in I'$, subject to no additional relation.

<!-- original page 249 -->

The details of the proof are left to the reader. The statement obtained is only the translation, into the language of
group theory, of the fact that one has an equivalence between the category $\mathcal{C}$ of étale coverings of $S$ and
the category of étale coverings $X'$ of $S'$ **endowed**, for every $s \in T$, with a transitive system of bijections
between the $n(s)$ fibers of $X'$ at the points of $g^{-1}(s)$ with values in $K_{s}$. In this intrinsic form, of
course, it is no longer necessary to suppose $S'$ connected.

**Example.**

<!-- label: IX.5.5 -->

One proves easily that the rational curve $\mathbb{P}^{1}_{k}$ over an algebraically closed field $k$ is simply
connected. \[Translator note: the source refers to Expos\acute{e} XI.1.1.\] Hence the fundamental group of a complete
rational curve having exactly one double point, with $n$ analytic branches, is the free group of galoisian type on
$n - 1$ generators. For example, in the case of an ordinary double point, one finds the fundamental group
$\hat{\mathbb{Z}}$, as announced in I.11 a). On the other hand, the existence of a cusp (which is a “geometrically
unibranch” point) has no influence on the fundamental group.

**Corollary.**

<!-- label: IX.5.6 -->

Let $g: S' \to S$ be a universally submersive morphism of preschemes, with geometrically connected fibers, $S$ being
connected. Then $S'$ is connected, and, choosing a geometric point $s'$ in $S'$ and denoting by $s$ its image in $S$,
the homomorphism

$\pi_{1}(S',s') \to \pi_{1}(S,s)$

is **surjective**. If $g$ is a morphism of effective descent for the fibered category of étale coverings of preschemes
(cf. IX.4.12), introducing the geometric point $s'' = diag(s')$ of $S'' = S' \times_{S} S'$ and the two homomorphisms

$p^{*}_{1}, p^{*}_{2}: \pi_{1}(S'',s'') \to \pi_{1}(S',s')$

induced by the two projections, $\pi_{1}(S,s)$ is isomorphic to the cokernel of this pair of morphisms in the category
of groups of galoisian type, that is, to the quotient of $\pi_{1}(S',s')$ by the closed normal subgroup generated by the
elements

<!-- original page 250 -->

$p^{*}_{1}(g'') p^{*}_{2}(g'')^{-1}$, $g'' \in \pi_{1}(S'',s'')$.

Indeed, by IX.3.4 the functor $X \mapsto X \times_{S} S'$ from étale coverings of $S$ to étale coverings of $S'$ is
fully faithful; this is equivalent to saying that the homomorphism on fundamental groups is an epimorphism (V.6.9). The
last assertion is an immediate consequence of the description IX.5.1.

**Remark.**

<!-- label: IX.5.7 -->

It is not known at present whether the fundamental group of a proper scheme over an algebraically closed field $k$ is
topologically finitely presented. \[Translator note: the source footnote says this seems very unlikely for smooth curves
of genus $g \geq 2$ in characteristic $p > 0$; for the largest prime-to-$p$ quotient, however, known techniques seem to
give an affirmative answer, even without properness, and it refers to work in preparation by J.-P. Murre.\] Using
IX.5.3, a well-known technique of hyperplane sections, and desingularization of normal surfaces, one reduces to the case
of a **smooth surface over** $k$. This at least allows one to show, by transcendental methods, that the answer is
affirmative in characteristic `0`, without having to assume triangulability of singular algebraic varieties. In
characteristic $p > 0$, the main difficulty seems to lie in the case of curves, for which one only knows that the
fundamental group is a quotient of the one appearing in the classical case (cf. the next exposé), but the kernel by
which one divides is very poorly known.

**Remark.**

<!-- label: IX.5.8 -->

One could make explicit other special cases besides IX.5.4 and IX.5.6 in which IX.5.1 takes a particularly simple form.
An interesting case is that in which $S$ is the quotient of $S'$ by a finite group $\Gamma$ of automorphisms. **Then the
category of étale coverings of $S$ is equivalent to the category of étale coverings $X'$ of $S'$ on which $\Gamma$ acts
compatibly with its action on $S'$, in such a way that for every $s' \in S'$ and every $g \in \Gamma_{s'}$** (where
$\Gamma_{s'}$ denotes **the inertia group** of $s'$ in $\Gamma$), **$g$ acts trivially on the fiber** $X'_{s'}$.

If $S'$ is connected, this statement is interpreted as follows. Let $\mathcal{C}_{0}'$ be the category of étale
coverings of $S'$ on which $\Gamma$ acts compatibly with its action on $S'$, without necessarily satisfying the
preceding condition on inertia groups of points of $S'$. One sees easily that this is a galoisian category (V.5), and
that for every geometric point $a'$ of $S'$, the fiber functor $X' \mapsto X'_{a'}$ on $\mathcal{C}_{0}'$ is a
fundamental functor. Let $\pi_{1}(S',\Gamma;a') = G$ be the automorphism group of this functor, with its usual topology.
Then there is a canonical exact sequence

<!-- original page 251 -->

$e \to \pi_{1}(S',a') \to G \to \Gamma \to e$.

Moreover, for every geometric point $b'$ of $S'$, one has an isomorphism
$\pi_{1}(S',\Gamma;b') \to G = \pi_{1}(S',\Gamma;a')$, defined up to inner automorphism coming from $\pi_{1}(S',a')$.
Since $\Gamma_{b'}$ maps evidently into the first group, one obtains a homomorphism

$u_{b'}: \Gamma_{b'} \to G$,

defined up to inner automorphism coming from $\pi_{1}(S',a')$, whose composite with $G \to \Gamma$ is the canonical
immersion $\Gamma_{b'} \to \Gamma$. With this understood, **the fundamental group $\pi_{1}(S,a)$ is canonically
isomorphic to the quotient group of $G = \pi_{1}(S',\Gamma;a')$ by the closed normal subgroup generated by the images of
the homomorphisms $\Gamma_{b'} \to G$**. In particular, the image of $\pi_{1}(S',a')$ in $\pi_{1}(S,a)$ is a normal
subgroup, and the corresponding quotient is isomorphic to a quotient of $\Gamma$.

One can reduce the number of “relations” introduced as follows. For every $g \in \Gamma$, $g \neq e$, introduce the
subprescheme $S'_{g}$ where the automorphisms $id_{S}$ and $g$ coincide; choose a geometric point $b'_{g,i}$ in each
connected component of $S'_{g}$, then one of the corresponding homomorphisms $\pi_{1}(S',\Gamma;b'_{g,i}) \to G$, giving
lifts $\bar{g}_{i}$ of $g$ in $G$. It is enough to take the quotient of $G$ by the closed normal subgroup generated by
the $\bar{g}_{i}$.

When $a'$ is fixed by $\Gamma$, $\Gamma$ acts naturally on $\pi_{1}(S',a')$, and $G$ identifies with the corresponding
semidirect product. Identifying $\Gamma$ with a subgroup of $G$, one sees that among the relations introduced above,
taking $b' = a'$ gives “$g = e$” for $g$ in the inertia group. Therefore **if $S'$ has a geometric point $a'$ fixed by**
$\Gamma$ (that is, a point $s'$ whose inertia group is $\Gamma$), **then $\pi_{1}(S,a)$ is a quotient of the quotient
group of galoisian type of $\pi_{1}(S',a')$ obtained by making the actions of $\Gamma$ on $\pi_{1}(S',a')$ trivial**; it
is even isomorphic to this latter group if, for every $g \in \Gamma$, the inertia locus $S'_{g}$ is connected, hence
passes through the locality of $a'$.

<!-- original page 252 -->

This last assertion is contained in the second description above of the relations to be introduced in $G$.

This result applies in particular if one takes $S'$ to be the cartesian power $X^{n}$ of a connected prescheme over an
algebraically closed field, $\Gamma$ to be the symmetric group $\mathfrak{S}_{n}$ acting in the usual way, and $S$ to be
the $n$-th symmetric power of $X$. Taking $a'$ to be a geometric point localized on the diagonal, one is under the
preceding conditions, since all inertia loci $S'_{g}$ contain the diagonal. Using the fact, proved in the next exposé,
that if $X$ is proper and connected over $k$, the fundamental group of $X^{n}$ identifies with $\pi_{1}(X)^{n}$, one
obtains the following amusing result: **If $X$ is proper and connected over an algebraically closed $k$, the fundamental
group of its $n$-th symmetric power, $n \geq 2$, is isomorphic to the abelianization of the fundamental group of $X$.**
I do not know whether the analogous fact in algebraic topology is known; it should be provable by the same descent
method. Taking for example $X$ to be the rational curve $X = \mathbb{P}^{1}_{k}$, one obtains yet another proof that
$\mathbb{P}^{r}_{k}$ is simply connected, using the fact that $\mathbb{P}^{1}_{k}$ is. Taking now $X$ to be a
nonsingular curve over $k$, and $n \geq 2g - 1$, so that $Sym^{n}(X)$ is fibered over the Jacobian $J$ with
projective-space fibers, and hence, as will be seen using the results of the next two exposés, has the same fundamental
group as $J$, one recovers without dévissage the well-known fact that **the fundamental group of the Jacobian of $X$ is
isomorphic to the abelianization of the fundamental group of $X$**.

## 6. A Fundamental Exact Sequence. Descent by Morphisms with Relatively Connected Fibers

<!-- label: IX.6 -->

<!-- original page 253 -->

**Theorem.**

<!-- label: IX.6.1 -->

Let $S$ be the spectrum of an artinian ring $A$ with residue field $k$, let $\bar{k}$ be an algebraic closure of $k$,
let $X$ be an $S$-prescheme, $X_{0} = X \otimes_{A} k$, $\bar{X}_{0} = X \otimes_{A} \bar{k}$, let `ā` be a geometric
point of $\bar{X}$, let $a$ be its image in $X$, and let $b$ be its image in $S$. Suppose $X_{0}$ is quasi-compact and
**geometrically connected** over $k$. (If $X$ is proper over $S$, this means that $H^{0}(X_{0},\mathcal{O}_{X_{0}})$ is
a **local** artinian ring with residue field **radicial** over $k$.) Then the sequence of canonical homomorphisms

$e \to \pi_{1}(\bar{X}_{0},\bar{a}) \to \pi_{1}(X,a) \to \pi_{1}(S,b) \to e$

is exact, and one has

$\pi_{1}(S,b) \simeq \pi_{1}(k,\bar{k})$ = the Galois group of $\bar{k}$ over $k$.

Since fundamental groups do not change after killing nilpotents, one may suppose $A = k$, which already makes the last
isomorphism evident. Let $k'$ be the separable closure of $k$ in $\bar{k}$, and consider $X' = X \otimes_{k} k'$ and the
image $a'$ of `ā` in $X'$. One has a canonical sequence

$e \to \pi_{1}(\bar{X}_{0},\bar{a}) \to \pi_{1}(X',a') \to \pi_{1}(S',b') \to e$,

where $S' = \operatorname{Spec}(k')$. There is also a canonical homomorphism from this sequence to the corresponding
sequence for $X/k$, coming from the evident diagram. This homomorphism of sequences is an isomorphism by IX.4.11. We are
therefore reduced to proving that the second sequence is exact, that is, we may suppose $k$ **perfect**.

Let $k_{i}$ be the finite Galois subextensions of $k$ in $\bar{k}$, put $X_{i} = X \otimes_{k} k_{i}$, and let $a_{i}$
be the image of `ā` in $X_{i}$. The reader may verify that the natural homomorphism

$\pi_{1}(\bar{X}_{0},\bar{a}) \simeq \lim_{i} \pi_{1}(X_{i},a_{i})$

is an isomorphism. This simply means that an étale covering of $\bar{X}$ comes from an étale covering of some $X_{i}$,
and that the latter is essentially unique after passing to an $X_{j}$ with $j \geq i$.

<!-- original page 254 -->

On the other hand, let $\pi_{i}$ be the Galois group of $k_{i}$ over $k$, that is, the opposite group of the group of
$S$-automorphisms of $S_{i} = \operatorname{Spec}(k_{i})$. Since the functor $S' \mapsto X \times_{S} S'$ from étale
coverings of $S$ to étale coverings of $X$ is fully faithful by IX.3.4, it follows that $\pi_{i}$ is also isomorphic to
the opposite of the group of $X$-automorphisms of the connected principal covering $X_{i}$ of $X$. Hence by V.6.13 one
has an exact sequence

$e \to \pi_{1}(X_{i},a_{i}) \to \pi_{1}(X,a) \to \pi_{i} \to e$.

Passing to the inverse limit over $i$ in these exact sequences gives an exact sequence, since we are in the category of
groups of galoisian type, and this is precisely the sequence considered in IX.6.1.

The geometric translation of right exactness in IX.6.1 is the following:

**Corollary.**

<!-- label: IX.6.2 -->

With the preceding notation, let $X'$ be an étale covering of $X$, and let $\bar{X}_{0}'$ be the corresponding étale
covering of $\bar{X}_{0}$. The following conditions are equivalent:

1. There exists an $S'$ étale over $S$ and an $X$-isomorphism $X' \simeq X \times_{S} S'$. The $S'$ is then determined
   up to unique isomorphism by IX.3.4.
1. $\bar{X}_{0}'$ is completely decomposed over $\bar{X}_{0}$.

If $X'$ is connected, these conditions are also equivalent to:

2 bis. $\bar{X}_{0}'$ has a section over $\bar{X}_{0}$.

This last supplement is essential: the equivalence of 1 and 2 means only that $\pi_{1}(S,b)$ is the quotient group of
$\pi_{1}(X,a)$ by the closed normal subgroup generated by the image of $\pi_{1}(\bar{X}_{0},\bar{a})$, and not by this
image itself. Under the preceding conditions, we shall say that $X'$ is a **geometrically trivial** covering of $X$.

<!-- original page 255 -->

**Remark.**

<!-- label: IX.6.3 -->

In IX.6.1 one cannot replace $\bar{k}$ by an arbitrary algebraically closed extension of $k$, even if $k$ is already
assumed algebraically closed. In other words, it is not generally true that if $X$ is a connected algebraic scheme over
an algebraically closed field $k$, its fundamental group is unchanged after replacing $k$ by an algebraically closed
extension. This already fails, for instance, in characteristic $p > 0$ for the affine line over $k$, because of “higher
ramification” phenomena at the point at infinity, which imply a “continuous” structure for the fundamental group. We
shall see in the next exposé, however, that such phenomena cannot occur if $X$ is **proper** over $k$. We shall also
show by transcendental methods that the same is true if $k$ has characteristic zero.

**Corollary.**

<!-- label: IX.6.4 -->

Suppose that $a$ is localized at an $x \in X$ that is rational over $k$ (or more generally has residue field radicial
over $k$). Then the exact sequence IX.6.1 is split.

One may suppose $S = \operatorname{Spec}(k)$. If $x$ is rational over $k$, it corresponds to a section $S \to X$ of $X$
over $S$, sending $b$ to $a$ and defining a homomorphism $\pi_{1}(S,b) \to \pi_{1}(X,a)$ that is the required splitting.
If $\kappa(x)$ is radicial over $k$, one reduces to the preceding case by the base extension
$\operatorname{Spec}(\kappa(x)) \to \operatorname{Spec}(k)$.

**Theorem.**

<!-- label: IX.6.5 -->

Let $f: X \to S$ be a proper and surjective morphism of finite presentation, with geometrically connected fibers; let
$X'$ be a prescheme of finite presentation and proper over $X$; let $s$ be a point of $S$; let $F = X_{s}$ be the fiber
of $X$ at $s$; and let $F_{1}'$ be a connected component of the fiber $F' = X'_{s}$ of $X'$ at $s$. There exists an open
neighborhood $X_{1}'$ of $F_{1}'$ in $X'$, an $S$-scheme $S_{1}'$ étale over $S$, and an $X$-isomorphism
$X_{1}' \simeq S_{1}' \times_{S} X$ if and only if $X'$ is étale over $X$ at the points of $F_{1}'$ and $F_{1}'$ is a
geometrically trivial covering of $F$.

Necessity is trivial, so it remains to prove sufficiency. One reduces easily to the case where $S$ is noetherian.
Consider the Stein factorization $X \to T \to S$ of $f$, where $T$ is the spectrum of the Algebra
$f_{*}(\mathcal{O}_{X})$ on $S$. Since the fibers of $X$ over $S$ are geometrically connected and $f$ is surjective, the
morphism $T \to S$ is finite, surjective, and radicial; hence by IX.4.10 every $T'$ étale over $T$ comes by inverse
image from an $S'$ étale over $S$. This reduces us to proving IX.6.5 with $S$ replaced by $T$, that is, to the case
where $f_{*}(\mathcal{O}_{X}) = \mathcal{O}_{S}$.

Consider then the Stein factorization $X' \to S' \to S$ of the proper morphism $h: X' \to S$, where $S'$ is the spectrum
of the Algebra $h_{*}(\mathcal{O}_{X'})$. The morphisms $X' \to X$ and $X' \to S'$ define a canonical morphism

$X' \to X \times_{S} S'$,

and our assertion is contained in the following:

**Corollary.**

<!-- label: IX.6.6 -->

Let $f: X \to S$ be a proper morphism of locally noetherian preschemes such that
$f_{*}(\mathcal{O}_{X}) = \mathcal{O}_{S}$, and let $X'$ be a prescheme proper over $X$. Consider the **Stein**
factorization $X' \to S' \to S$ for $X' \to S$ and the canonical morphism $X' \to X \times_{S} S'$. Let $s$ be a point
of $S$, and let $s'$ be a point of $S'$ above $s$, corresponding to a connected component $F_{1}'$ of the fiber $X'_{s}$
of $X'$ at $s$. The morphism $X' \to X \times_{S} S'$ is an isomorphism above an open neighborhood $U'$ of $s'$ étale
over $S$ if and only if $X'$ is étale over $X$ at the points of $F_{1}'$ and $F_{1}'$ is a geometrically trivial
covering of the fiber $F = X_{s}$.

Necessity is again trivial; it remains to prove sufficiency. The conclusion also says that a) the morphism deduced from
$X' \to X \times_{S} S'$ by base change $\operatorname{Spec}(\hat{O}_{s'}) \to S'$ is an isomorphism, and b) $S'$ is
étale over $S$ at $s'$, that is, $\hat{O}_{s'}$ is étale over $\hat{O}_{s}$. In this form, the conclusion is invariant
under the base change $\operatorname{Spec}(\hat{O}_{s}) \to S$. Since the hypotheses are likewise stable under this base
change, one may suppose $S$ is the spectrum of a complete noetherian local ring. One may also plainly suppose $X'$
connected, which here implies $S' = \operatorname{Spec}(\mathcal{O}_{s'})$ and $F' = F_{1}'$.

<!-- original page 257 -->

Since the set of points of $X'$ at which $X'$ is étale over $X$ is open and contains the fiber $X'_{s'} = F'$, and since
$X'$ is proper over $S$, it follows that $X'$ is étale over $X$. Since it induces on $F = X_{s}$ an étale covering
isomorphic to $F \otimes_{\kappa(s)} L$, where $L$ is étale over $\kappa(s)$, IX.1.10 implies that it is isomorphic to a
covering of the form $X \times_{S} T$, with $T$ étale over $S$. Here again it is enough to use full faithfulness of the
functor in IX.1.10, which follows from the fact that a formal isomorphism of coherent sheaves on $X$ comes from an
isomorphism of those sheaves.

Thus, if $T$ is defined by the finite $A$-algebra $B$, $X'$ identifies with the spectrum of the Algebra
$\mathcal{O}_{X} \otimes_{A} B$ over $X$. Since $f_{*}(\mathcal{O}_{X}) = \mathcal{O}_{S}$, it follows at once that
$h_{*}(\mathcal{O}_{X'})$ is defined by $B$, hence the canonical homomorphism $X' \to X \times_{S} S'$ is precisely the
isomorphism $X' \simeq X \times_{S} T$ under consideration. This completes the proof.

**Corollary.**

<!-- label: IX.6.7 -->

Under the conditions of IX.6.5, there exists a prescheme $S'$ étale over $S$ and an $X$-isomorphism
$X' \simeq X \times_{S} S'$ if and only if $X'$ is étale over $X$ and for every $s \in S$, the fiber $X'_{s}$ is a
geometrically trivial covering of $X_{s}$.

Indeed, if this holds, $X'$ is the union of open subsets $X_{i}'$ that are isomorphic to inverse images of $S_{i}'$
étale over $S$. One then sees easily that these $S_{i}'$ glue to an $S'$ étale over $S$, and that one obtains an
isomorphism $X' \simeq X \times_{S} S'$. For example, one may say that the $X_{i}'$ carry descent data relative to
$X \to S$, which necessarily glue to a descent datum on all of $X'$ relative to $X \to S$; since this datum is effective
on the $X_{i}'$, it follows easily (by a sorites omitted in no. IX.4) that it is effective. One can also state IX.6.7 as
follows:

**Corollary.**

<!-- label: IX.6.8 -->

Let $f: X \to S$ be a proper surjective morphism of finite presentation, with geometrically connected fibers. Then $f$
is a morphism of effective descent for the fibered category of preschemes finite étale over other preschemes. The
functor $S' \mapsto X \times_{S} S'$ induces an equivalence from the category of preschemes finite étale over $S$ to the
category of preschemes

<!-- original page 258 -->

finite étale over $X$ that induce on each fiber $X_{s}$ a geometrically trivial covering.

**Remark.**

<!-- label: IX.6.9 -->

Let $f: X \to S$ be a proper and surjective morphism, with $S$ locally noetherian. Then $f$ factors as a morphism
$X \to S'$ satisfying the hypothesis of IX.6.8 followed by a finite surjective morphism $S' \to S$ covered by IX.4.7.
Thus $f$ is a composite of two morphisms that are **universal effective descent morphisms** for the fibered category of
preschemes finite étale over other preschemes. It follows that $f$ itself is a universal effective descent morphism for
the fibered category in question. This recovers IX.4.12 by a different method.

**Remark.**

<!-- label: IX.6.10 -->

The conclusion of IX.6.7 does not remain valid if the hypothesis that $f$ is proper is replaced by: $X$ is of finite
type over $S$ and admits a section over $S$ (so $f$ is universally submersive and a descent morphism for the fibered
category of preschemes étale over other preschemes), even when $S$ is the spectrum of a discrete valuation ring and $X'$
is an étale covering of $X$. To see this, start with a $Z$ proper over $S$ whose generic fiber is a nonsingular rational
curve and whose special fiber $Z_{0}$ consists of two intersecting lines. For example, if $t$ is a uniformizer of the
valuation ring $A$, take the closed subscheme $Z$ of $\mathbb{P}^{2}_{A}$ defined by the homogeneous equation
$x^{2} + y^{2} + tz^{2} = 0$. Let $X$ be the complement of the singular point $a$ of $Z_{0}$ in the union
$Z \cup \mathbb{P}^{2}_{k}$. The fibers of $X$ are $\mathbb{P}^{1}_{k}$ and $\mathbb{P}^{2}_{k} - a$, hence
geometrically simply connected, meaning that every étale covering of such a fiber is geometrically trivial.

<!-- original page 259 -->

However, proceeding as in no. IX.4, one easily constructs étale coverings of $X$ that do not come from étale coverings
of $S$, by gluing trivial coverings of $Z - a$ and of $\mathbb{P}^{2}_{k} - a$. It is possible, on the other hand, that the conclusion
of IX.6.7 remains true if the properness hypothesis is replaced by the hypothesis that $X$ be **universally open** of
finite presentation over $S$. \[Translator note: the source adds that this is now proved, with `g` only universally open
and surjective; cf. SGA 4 XV 1.15.\] This is at least true if the fibers of $X$ over $S$ are geometrically irreducible,
and not merely geometrically connected. We only point out that in this question one can reduce to the case where $S$ is
the spectrum of a complete discrete valuation ring with algebraically closed residue field.

The interpretation of IX.6.7 in terms of the fundamental group is the following:

**Corollary.**

<!-- label: IX.6.11 -->

Let $f: X \to S$ be a proper surjective morphism of finite presentation, with geometrically connected fibers. Suppose
$X$, hence $S$, connected. Let $a$ be a geometric point of $X$, $b$ its image in $S$, and for every $s \in S$ choose an
algebraic closure $\kappa\bar{s}$ of $\kappa(s)$, a geometric point $a_{s}$ of $X_{s}$ with values in this extension,
and a path class from $a_{s}$ to $a$. This gives a homomorphism

$\pi_{1}(\bar{X}_{s},a_{s}) \to \pi_{1}(X,a)$,

where $\bar{X}_{s} = X_{s} \otimes_{\kappa(s)} \kappa\bar{s}$. Then the homomorphism $\pi_{1}(X,a) \to \pi_{1}(S,b)$ is
surjective, and its kernel is the closed normal subgroup of $\pi_{1}(X,a)$ generated by the images of the
$\pi_{1}(\bar{X}_{s},a_{s})$.

**Remark.**

<!-- label: IX.6.12 -->

Under the conditions of IX.6.7, assuming $S$ noetherian, one sees easily that the set of points $s \in S$ such that the
corresponding fiber is geometrically trivial over $X_{s}$ is constructible; if $X'$ is proper over $X$, it is even open,
as one sees from IX.6.6. Thus, if $S$ is a Jacobson prescheme (for example of finite type over a field), or if $X'$ is
proper over $X$,

<!-- original page 260 -->

it is enough, in order to verify the conditions of IX.6.7, to restrict to the **closed** points $s$ of $S$. Likewise, in
IX.6.11 it is then enough to take the $\pi_{1}(\bar{X}_{s},a_{s})$ for the closed points of $S$.

## Bibliography

**[IX.D]** J. Giraud, _Méthode de la descente_, Mémoire no. 2 de la Société Mathématique de France, 1964.

**[IX.1]** A. Grothendieck, _Géométrie algébrique et Géométrie formelle_, Séminaire Bourbaki, vol. 11, 1959, no. 182.


<!-- SOURCE: 10-theorie-de-la-specialisation-du-groupe-fondamental.md -->

# Exposé X. Theory of Specialization of the Fundamental Group

<!-- label: X -->

<!-- original page 261 -->

In the present exposé, we restrict ourselves to the study of the fundamental group of geometric fibers in a **proper**
morphism, that is, of the fundamental group of a variable **proper** algebraic scheme. In a later exposé, we shall
generalize the technique used here to étale coverings **tamely ramified** “at infinity.” This will give, for example, a
solution of the “three point problem” in the case of Galois coverings of order prime to the characteristic, that is, a
determination of the Galois coverings of the line $\mathbb{P}^{1}_{k}$ ramified at most at three given points and tamely
ramified at those points, together with its evident variants.

## 1. The Homotopy Exact Sequence for a Proper and Separable Morphism

<!-- label: X.1 -->

**Definition.**

<!-- label: X.1.1 -->

A prescheme $X$ over a field $k$ is called **separable**, or **separable over $k$**, if for every extension $K$ of $k$,
$X \otimes_{k} K$ is reduced. If $f: X \to Y$ is a morphism of preschemes, one says that $f$ is **separable**, or that
$X$ **is separable over $Y$**, if $X$ is flat over $Y$ and if for every $y \in Y$, the fiber $X \otimes_{Y} \kappa(y)$
is separable over $\kappa(y)$.

If $X$ is a prescheme over a field $k$, to say that it is separable also means that it is **reduced**, and that the
fields $\kappa(x)$, for $x$ the generic point of an irreducible component of $X$, are separable extensions of $k$. If
$k$ is perfect, this is therefore the same as saying that $X$ is reduced.

Notice that if $X$ is separable over $Y$, then for every base change $Y' \to Y$, $X' = X \times_{Y} Y'$ is separable
over $Y'$. One can also prove, under suitable finiteness hypotheses, that the composite of two separable morphisms is

<!-- original page 262 -->

separable. We shall need this only in the following form: **if $X$ is separable over $Y$ and $X'$ is étale over $X$,
then $X'$ is separable over $Y$.** This is an immediate consequence of the definitions and I.9.2. Moreover, the
hypothesis “separable morphism” will be used through the following proposition:

**Proposition.**

<!-- label: X.1.2 -->

Let $f: X \to Y$ be a proper and separable morphism, with $Y$ locally noetherian, and consider its **Stein**
factorization $X \to Y' \to Y$, where $f'_{*}(\mathcal{O}_{X}) = \mathcal{O}_{Y'}$, with $Y'$ finite over $Y$ and
isomorphic to the spectrum of the algebra $f_{*}(\mathcal{O}_{X})$. Then $Y'$ is an **étale covering** of $Y$.

This proposition will appear in EGA III 7. [Translator note: the source footnote cites EGA III 7.8.10(i).] Let us
indicate the principle of the proof. One reduces easily to the case where $Y$ is the spectrum of a complete local ring
$A$, and, after making a suitable finite flat extension of the latter corresponding to a suitable residue extension, one
may suppose that the connected components of the fiber over the closed point $y$ are geometrically connected. This also
means that $H^{0}(X_{y}, \mathcal{O}_{X_{y}})$ decomposes as a product of fields identical with $k = \kappa(y)$.
Supposing then that $X$ is connected, as one may, one has $H^{0}(X_{y}, \mathcal{O}_{X_{y}}) = k$, hence the
homomorphism $A \to H^{0}(X_{y}, \mathcal{O}_{X_{y}})$ is **surjective**. By a general proposition of Künneth type, one
concludes that $f_{*}(\mathcal{O}_{X})$ is defined by a module $B$ over $A$ that is free over $A$, and that
$B/\mathfrak{m}B \to H^{0}(X_{y}, \mathcal{O}_{X_{y}}) = k$ is bijective. Thus in the present case $B$ is an étale
algebra over $A$, completing the proof.

**Theorem.**

<!-- label: X.1.3 -->

Let $f: X \to Y$ be a proper and separable morphism, with $Y$ locally noetherian and connected, and suppose
$f_{*}(\mathcal{O}_{X}) = \mathcal{O}_{Y}$. This implies that the fibers of $X$ over $Y$ are geometrically connected,
and conversely by X.1.2. Let $y$ be a point of $Y$, let $\kappa\bar{y}$ be an algebraic closure of $\kappa(y)$, and let
$\bar{X}_{y} = X_{y} \otimes_{\kappa(y)} \kappa\bar{y}$. Finally, let $X'$ be a **connected** étale covering of $X$, and
let $\bar{X}'_{y} = X'_{y} \otimes_{\kappa(y)} \kappa\bar{y}$. Then there exists an étale covering $Y'$ of $Y$ and an
$X$-isomorphism

<!-- original page 263 -->

```text
X′ ≃ X ×_Y Y′
```

if and only if $\bar{X}'_{y}$ admits a section over $\bar{X}_{y}$.

Putting $Y' = \operatorname{Spec}(h_{*}(\mathcal{O}_{X'}))$, where $h: X' \to Y$ is the composite $X' \to X \to Y$, it
is enough to prove that the canonical $Y$-morphism

```text
X′ → X ×_Y Y′
```

is an **isomorphism**, and that $Y'$ is étale over $Y$. We already know by X.1.2 that $Y'$ is étale over $Y$, hence
$X \times_{Y} Y'$ is étale over $X$, and therefore the morphism $X' \to X \times_{Y} Y'$ is also étale (I.4.8).
Moreover, $Y'$ is connected as the image of $X'$, which is connected; hence $X \times_{Y} Y'$ is connected, since $X$
has connected fibers over $Y$ (IX.3.4 and V.6.9(iii)). Thus to prove that $X' \to X \times_{Y} Y'$ is an isomorphism, it
is enough to see that its projection degree at **one** point of $X \times_{Y} Y'$ is equal to 1. This follows easily
from the hypothesis that $\bar{X}'_{y}$ admits a section over $\bar{X}_{y}$, either by using IX.6.6 or more simply by
noting that it is enough to prove the existence of such a point in $X \times_{Y} Y'$ after the base change
$\operatorname{Spec}(\kappa\bar{y}) \to Y$, where this is evident. This proves X.1.3.

Taking IX.3.4 and the dictionary V.6.9 and V.6.11 into account, one can put X.1.3 in the following equivalent form:

**Corollary.**

<!-- label: X.1.4 -->

With the preceding notation for $f: X \to Y$ and $\bar{X}_{y}$, let `ā` be a geometric point of $\bar{X}_{y}$, let $a$
be its image in $X$, and let $b$ be its image in $Y$. Then the following sequence of group homomorphisms is **exact**:

```text
π₁(X̄_y,ā) → π₁(X,a) → π₁(Y,b) → e.
```

**Remarks.**

<!-- label: X.1.5 -->

Notice that the proof of X.1.3 uses X.1.2 in an essential way and hence the “first comparison theorem” in
algebraic-formal geometry. By contrast, the descent theory of Exposé IX entered only through IX.3.4, for which a direct
proof is easy in the case of a **proper** morphism $f: X \to Y$ such that $f_{*}(\mathcal{O}_{X}) = \mathcal{O}_{Y}$.

<!-- original page 264 -->

Indeed, let $Y'$ be étale over $Y$ and suppose $X' = X \times_{Y} Y'$ is the disjoint sum of two nonempty open subsets;
we prove that the same is true of $Y'$. One has $Y' = \operatorname{Spec}(\mathcal{A})$, hence
$X' = \operatorname{Spec}(\mathcal{B})$, with $\mathcal{B} = \mathcal{A} \otimes_{\mathcal{O}_{Y}} \mathcal{O}_{X}$, and
the decomposition of $X'$ as a direct sum corresponds to a decomposition of $\mathcal{B}$ as a product of two nonzero
Algebras $\mathcal{B}_{1}$ and $\mathcal{B}_{2}$. Since $f_{*}(\mathcal{O}_{X}) = \mathcal{O}_{Y}$, one easily concludes
$f_{*}(\mathcal{B}) = \mathcal{A}$, so $\mathcal{A}$ is a sum of two Algebras, also nonzero because their unit sections
are nonzero, namely $f_{*}(\mathcal{B}_{1})$ and $f_{*}(\mathcal{B}_{2})$.

### 1.6.

<!-- label: X.I.6 -->

Suppose again that $f$ is proper and separable, but no longer make any hypothesis on $f_{*}(\mathcal{O}_{X})$, which
will correspond to a well-determined étale covering $Y'$ of $Y$, pointed above $b$ by the image $b'$ of $a$. Applying
X.1.4 to the canonical morphism $X \to Y'$, and supposing $f$ surjective, the exact sequence X.1.4 is replaced by the
following, analogous to the homotopy exact sequence of fiber spaces in algebraic topology:

```text
π₁(X̄_y,ā) → π₁(X,a) → π₁(Y,b) →
π₀(X̄_y,ā) → π₀(X,a) → π₀(Y,b) → e.
```

Of course, in X.1.4 one cannot in general assert that the homomorphism $\pi_{1}(\bar{X}_{y}, \bar{a}) \to \pi_{1}(X, a)$
is injective; in algebraic topology its kernel is the image of $\pi_{2}(Y, b)$, and in algebraic geometry as well there
would be reason to introduce homotopy groups in all dimensions, and the complete homotopy exact sequence for a proper
morphism satisfying suitable hypotheses, for example being smooth. At present no result in this direction is available,
except for a reasonable, though perhaps not definitive, definition of higher homotopy groups.

**Corollary.**

<!-- label: X.1.7 -->

Let $k$ be an algebraically closed field, and let $X$ and $Y$ be two connected preschemes over $k$. Suppose $X$ proper
over $k$ and $Y$ locally

<!-- original page 265 -->

noetherian. Let $a$ be a geometric point of $X$, and let $b$ be a geometric point of $Y$ with values in the same
algebraically closed extension $K$ of $k$. Consider the geometric point $c = (a, b)$ of $X \times_{k} Y$, and the
homomorphism

```text
π₁(X ×_k Y,c) → π₁(X,a) × π₁(Y,b)
```

deduced from the homomorphisms on fundamental groups associated with the two projections $X \times_{k} Y \to X$ and
$X \times_{k} Y \to Y$. This homomorphism is an **isomorphism**.

First suppose $K = k$. Put $Z = X \times_{k} Y$, consider the projection $f: Z \to Y$ and the locality $y$ of the
geometric point $b$ of $Y$, and apply X.1.4 to this situation. Notice that, after replacing $X$ by $X_{red}$ (which does
not change the fundamental groups in question), one may assume $X$ reduced, hence separable over $k$; therefore $Z$ is
separable over $k$, and plainly has geometrically connected fibers, since $X$ is connected. The geometric fiber of $Z$
at $b$ is canonically isomorphic to $X \otimes_{k} K = X$.

On the other hand, since the composite $X \to Z \to X$ is the identity, one finds that $\pi_{1}(X, a) \to \pi_{1}(Z, c)$
is injective, and X.1.4 gives an exact sequence

```text
e → π₁(X,a) → π₁(Z,c) → π₁(Y,b) → e.
```

There is also the canonical exact sequence

```text
e → π₁(X,a) → π₁(X,a) × π₁(Y,b) → π₁(Y,b) → e,
```

where the maps written are the canonical injection and projection. Finally, the canonical homomorphism
$\pi_{1}(Z, c) \to \pi_{1}(X, a) \times \pi_{1}(Y, b)$, together with the identity maps on the two end terms, gives a
homomorphism from the first exact sequence to the second. The commutativity of the resulting diagram is immediate. Since
the homomorphisms on the end terms are isomorphisms, the same is true for the middle terms; this proves X.1.7 in this
case.

When $K$ is no longer assumed equal to $k$, one obtains only an isomorphism

```text
π₁(Z,c) → π₁(X ⊗_k K,a) × π₁(Y,b),
```

<!-- original page 266 -->

and X.1.7 is then equivalent to the following special case:

**Corollary.**

<!-- label: X.1.8 -->

Let $X$ be a proper connected scheme over an algebraically closed field $k$, let $k'$ be an algebraically closed
extension of $k$, let $a'$ be a geometric point of $X \otimes_{k} k'$, and let $a$ be its image in $X$. Then the
canonical homomorphism

```text
π₁(X ⊗_k k′,a′) → π₁(X,a)
```

is an **isomorphism**.

The fact that this homomorphism is surjective is equivalent to saying that if $X'$ is a connected étale covering of $X$,
then $X' \otimes_{k} k'$ is also connected; this follows at once from the fact that $k$ is algebraically closed, and is
also a special case of IX.3.4. The properness hypothesis on $X$ has not yet been used.

It remains to say that injectivity of the homomorphism under consideration means: **every étale covering of
$X \otimes_{k} k'$ is isomorphic to the inverse image of an étale covering of $X$.** It is essentially sorital that one
can find a sub-$k$-algebra $A$ of $k'$, of finite type over $k$, and an étale covering of $X \otimes_{k} A$ whose
inverse image on $X \otimes_{k} k'$ is isomorphic to the given covering. Let $Y = \operatorname{Spec}(A)$, an integral
$k$-scheme of finite type, hence having $k$-rational points. Applying X.1.7 to the fundamental group of $X \times Y$ at
a point $(a, b)$ rational over $k$, one finds that every connected étale covering of $X \times Y$ is isomorphic to a
quotient of a covering $X' \times Y'$, where $X'$ and $Y'$ are Galois étale coverings of $X$ and $Y$ with groups $G$ and
$G'$, by a subgroup $H$ of $G \times G'$.

It follows that the inverse image of this covering of $X \times Y$ on $X \times Y'$ is isomorphic to a covering of the
form $X_{1}' \times Y'$, where $X_{1}'$ is an étale covering of $X$. If $L$ is the function field of $Y$, equal to the
fraction field of $A$ in $k'$, the étale covering of $X \otimes_{k} L$ induced by the given covering of $X \times_{k} Y$
is such that there exists a finite separable extension $L'$ of $L$ for which the inverse image of that covering on
$X \otimes_{k} L'$ is isomorphic to $X_{1}' \otimes_{k} L'$. Since $k'$ is algebraically closed, one may suppose the
extension $L'$ of $L$ is contained in $k'$. This proves that the given étale covering of $X \otimes_{k} k'$ is
isomorphic to $X_{1}' \otimes_{k} k'$.

The explicit form just mentioned for étale coverings of a product

<!-- original page 267 -->

$X \times_{k} Y$ immediately implies:

**Corollary.**

<!-- label: X.1.9 -->

Let $k$ be an algebraically closed field, let $X$ and $Y$ be two locally noetherian preschemes over $k$, let
$Z = X \times_{k} Y$ be their product, and let $Z'$ be an étale covering of $Z$. For every point $y \in Y$ rational over
$k$, let $i_{y}: \operatorname{Spec}(k) \to Y$ be the associated canonical morphism, and let
$j_{y} = id_{X} \times_{k} i_{y}$ be the corresponding morphism $X \to Z$. Finally, let $X_{y}'$ be the étale covering
of $X$ obtained as inverse image of $Z'$ by $j_{y}$. Suppose $Y$ connected, and suppose $X$ or $Y$ proper over $k$. Then
the coverings $X_{y}'$ of $X$ are all isomorphic.

Figuratively, one may say that **a family of étale coverings of $X$, parametrized by a connected prescheme $Y$, is
constant if $X$ or the parameter prescheme $Y$ is proper over $k$.**

**Remarks.**

<!-- label: X.1.10 -->

Corollaries X.1.7 to X.1.9 are due to Lang and Serre [X.2] in the case of normal algebraic schemes. Their work was the
initial motivation for the theory of the fundamental group developed in this seminar. As these authors observed, these
results become false if the properness hypothesis is dropped, at least in characteristic $p > 0$. Taking for example $X$
to be the affine line $X = \operatorname{Spec}(k[t])$, it is not difficult to see that the coverings of $X$,
parametrized by the affine line $Y = \operatorname{Spec}(k[s])$, defined by the equations

$$
x^{p} - x = st,
$$

are étale and pairwise non-isomorphic. This contradicts X.1.9 and a fortiori X.1.7; similarly, if $s$ is regarded as a
transcendental element over $k$ in an algebraically closed extension $K$ of $k$, one obtains an étale covering $X'$ of
$X \otimes_{k} K$ that does not come from an étale covering of $X$.

## 2. Application of the Existence Theorem for Sheaves: Semicontinuity Theorem for Fundamental Groups of Fibers of a Proper and Separable Morphism

<!-- label: X.2 -->

<!-- original page 268 -->

**Theorem.**

<!-- label: X.2.1 -->

Let $Y$ be the spectrum of a **complete** noetherian local ring, with residue field $k$; let $X$ be a proper $Y$-scheme;
let $X_{0} = X \otimes_{A} k$; let $a_{0}$ be a geometric point of $X_{0}$; and let $a$ be the corresponding geometric
point of $X$. Then the canonical homomorphism

$$
\pi_{1}(X_{0},a_{0}) \to \pi_{1}(X,a)
$$

is an **isomorphism**.

This is only a translation, into the language of the fundamental group, of the result recalled in IX.1.10. It is here
that the existence theorem for sheaves in algebraic-formal geometry enters essentially into the theory of the
fundamental group.

Now introduce an algebraic closure $\bar{k}$ of the residue field $k$, and the geometric fiber
$\bar{X}_{0} = X_{0} \otimes_{k} \bar{k}$. We have the exact sequence (IX.6.1)

```text
e → π₁(X̄₀,ā) → π₁(X₀,a₀) → π₁(k,k̄) → e.
```

On the other hand, we have the isomorphism X.2.1 and the analogous, more elementary isomorphism

$$
\pi_{1}(k,\bar{k}) \to \pi_{1}(Y,b),
$$

where $b$ is the image of $a$ in $Y$. Thus one obtains:

**Corollary.**

<!-- label: X.2.2 -->

With the preceding notation, suppose $\bar{X}_{0} = X_{0} \otimes_{k} \bar{k}$ connected, and let $\bar{a}_{0}$ be a
geometric point of $\bar{X}_{0}$, let $a_{0}$ be its image in $X$, and let $b_{0}$ be its image in $Y$. Then the
following sequence of canonical homomorphisms is exact:

```text
e → π₁(X̄₀,ā) → π₁(X,a₀) → π₁(Y,b₀) → e.
```

Compare this sequence with the exact sequence X.1.4, but note that: a) no flatness or fiberwise separability hypothesis
has had to be made for $X \to Y$; b) one has the important supplement that **the morphism
$\pi_{1}(\bar{X}_{0}, \bar{a}_{0}) \to \pi_{1}(X, a_{0})$ is injective.**

This last fact will allow us to compare the fundamental group of the other

<!-- original page 269 -->

geometric fibers of $X$ over $Y$ with that of $\bar{X}_{0}$. Indeed, let $y_{1}$ be any point of $Y$, let $X_{1}$ be its
fiber and $\bar{X}_{1}$ its geometric fiber relative to an algebraically closed extension of $\kappa(y_{1})$, let
$\bar{a}_{1}$ be a geometric point of $\bar{X}_{1}$, and let $a_{1}$ and $b_{1}$ be its images in $X$ and $Y$. Choose a
“path class” from $a_{1}$ to $a_{0}$, whence a path class from $b_{1}$ to $b_{0}$. This gives a commutative diagram of
homomorphisms

```text
π₁(X̄₁,ā₁) → π₁(X,a₁) → π₁(Y,b₁) → e
     ↓            ↓≃           ↓≃
e → π₁(X̄₀,ā₀) → π₁(X,a₀) → π₁(Y,b₀) → e,
```

where the two displayed vertical arrows in the middle and on the right are isomorphisms. Since the second row is exact,
one obtains a canonical homomorphism, which we shall call **the specialization homomorphism for the fundamental group**.
It depends only on the chosen path class from $a_{1}$ to $a_{0}$, and is therefore **defined modulo inner automorphism
of** $\pi_{1}(X, a_{0})$:

$$
\pi_{1}(\bar{X}_{1},\bar{a}_{1}) \to \pi_{1}(\bar{X}_{0},\bar{a}_{0}).
$$

When the first row above is also exact, it follows at once that the specialization homomorphism is surjective. Thus,
taking X.1.4 into account:

**Corollary.**

<!-- label: X.2.3 -->

Under the conditions of X.2.1, suppose in addition that the morphism $f: X \to Y$ is **separable** (X.1.1) and that
$\bar{X}_{0}$ is connected. Then, by X.1.2, $f_{*}(\mathcal{O}_{X}) = \mathcal{O}_{Y}$. For every geometric fiber
$\bar{X}_{1}$ of $X$ over $Y$, endowed with a geometric point $\bar{a}_{1}$, the specialization homomorphism defined
above is **surjective**.

This is a **semicontinuity** result for the fundamental group, and it does not yet seem to have an analogue in algebraic
topology. It can also be stated under more general conditions:

**Corollary.**

<!-- label: X.2.4 -->

<!-- original page 270 -->

Let $f: X \to Y$ be a proper morphism with geometrically connected fibers, with $Y$ locally noetherian. Let $y_{0}$ and
$y_{1}$ be two points of $Y$ such that $y_{0} \in cl({y_{1}})$, let $\bar{X}_{0}$ and $\bar{X}_{1}$ be the geometric
fibers of $X$ corresponding to given algebraically closed extensions of $\kappa(y_{0})$ and $\kappa(y_{1})$, and let
$\bar{a}_{0}$, respectively $\bar{a}_{1}$, be a geometric point of $\bar{X}_{0}$, respectively $\bar{X}_{1}$. Then one
can define naturally a specialization homomorphism

$$
\pi_{1}(\bar{X}_{1},\bar{a}_{1}) \to \pi_{1}(\bar{X}_{0},\bar{a}_{0}),
$$

defined up to inner automorphism, and it is **surjective** if $f$ is separable (X.1.1).

Indeed, X.1.8 first implies that X.2.4 is essentially independent of the chosen algebraically closed extensions of the
residue fields $\kappa(y_{0})$ and $\kappa(y_{1})$. This allows us to replace $Y$ by a prescheme $Y'$ over $Y$ having a
point $y_{0}'$, respectively $y_{1}'$, above $y_{0}$, respectively $y_{1}$. We then take $Y'$ to be the spectrum of the
completion of the local ring of $y_{0}$ in $Y$, and apply X.2.3.

**Remarks.**

<!-- label: X.2.5 -->

The final conclusion of X.2.4 on surjectivity of the specialization homomorphism, and a fortiori the results X.1.3 and
X.1.4 of which it is a consequence, become false if one no longer assumes $f: X \to Y$ to be separable, even for
projective schemes over an algebraically closed field of characteristic 0. We shall see examples later, both in the case
where $f$ is flat but has a nonseparable fiber (with $X$ and $Y$ nevertheless smooth over $k$), and in the case where
the fibers of $f$ are separable but $f$ is not flat, for instance with $f: X \to Y$ a birational morphism of normal
integral schemes; cf. XI.3. In these examples it can happen that the fundamental group of the generic geometric fiber is
trivial, while that of a suitable special geometric fiber is not.

On the other hand, even if $f: X \to Y$ is a proper separable morphism as in X.2.4, the specialization morphism often
fails to be an isomorphism.

<!-- original page 271 -->

For instance, it is easy to give examples where $\bar{X}_{1}$ is a nonsingular elliptic curve, so its fundamental group
is commutative and its $\ell$-primary component for a prime $\ell$ different from the characteristic is isomorphic to
$\mathbb{Z}^{2}_{\ell}$ (cf. XI), while $\bar{X}_{0}$ is formed either of two nonsingular rational curves meeting in two
points, or of two rational curves tangent at one point, or finally of a rational curve with a singularity that is a
cusp. For the complete classification of degenerate elliptic curves, see the recent work of Kodaira [X.1] and Néron. In
these cases the fundamental group of $\bar{X}_{0}$ is respectively $\hat{\mathbb{Z}}$, $e$, $e$, hence “strictly
smaller” than that of $\bar{X}_{1}$.

We shall see later, however, that when $f$ is a **smooth** morphism there is an upper bound on the kernel of the
specialization homomorphism, implying in particular that if $\kappa(y_{0})$ has **characteristic** 0, the specialization
homomorphism is an isomorphism. But even for a smooth morphism, if the characteristic of $\kappa(y_{0})$ is `> 0`, the
specialization homomorphism may fail to be an isomorphism, as one sees for example when $X$ is an abelian scheme over
$Y$ (of relative dimension 1, if desired); cf. XI.2.

A satisfactory theory of specialization of the fundamental group must take into account the “continuous component” of
the “true” fundamental group, corresponding to the classification of principal coverings with structural group an
infinitesimal group. Once this is done, one would be entitled to expect that the “true” fundamental groups of the
geometric fibers of a smooth and proper morphism $f: X \to Y$ form a nice local system on $X$, an inverse limit of
finite flat group schemes over $X$. \[Translator note: the source footnote says this very attractive conjecture is
unfortunately contradicted by an unpublished example of M. Artin, already for fibers that are algebraic curves of fixed
genus $g \geq 2$.\] We shall return later to this viewpoint; our present aim is, on the contrary, to push as far as
possible the phenomena common to the topological theory and the schematic theory of the fundamental group.

Let now $X_{0}$ be a proper, smooth, connected curve of genus $g$ over an algebraically closed field $k$. If $k$ has
characteristic zero, its fundamental group can be determined by transcendental methods as follows. One knows that
$X_{0}$ is obtained by base extension from a curve defined over an algebraically closed extension of finite
transcendence degree of the prime field $\mathbb{Q}$; taking X.1.8 into account, one may suppose $k$ itself has finite
transcendence degree over $\mathbb{Q}$. Hence one may suppose $k$ is a subfield of the complex numbers $\mathbb{C}$, and
another application of X.1.8 allows one to suppose $k = \mathbb{C}$.

It is then not difficult to verify that the fundamental group of $X$ is isomorphic to the profinite completion of the
fundamental group of the associated topological space $\tilde{X}$, a compact oriented surface of genus $g$, for the topology
defined by subgroups of finite index. \[Translator note: the source footnote says this deduction was explained in one of
the oral expos\acute{e}s that were not written up.\] Classically, the topological fundamental group is generated by `2g`
generators $s_{i}, t_{i}$, $1 \leq i \leq g$, subject to the single relation

```text
(s₁t₁s₁⁻¹t₁⁻¹)⋯(s_gt_gs_g⁻¹t_g⁻¹) = 1.
```

Thus the fundamental group of $X$ admits `2g` **topological** generators $s_{i}, t_{i}$, $1 \leq i \leq g$, bound by the
preceding single relation.

If now $k$ has characteristic $p > 0$, let $A$ be the ring of Witt vectors built from $k$, and let $K$ be an
algebraically closed extension of its fraction field. We saw in III.7.4 that there exists a scheme $X$ over
$Y = \operatorname{Spec}(A)$, proper and smooth over $Y$, reducing to $X_{0}$. Applying X.2.3 to it, one obtains a
**surjective** morphism

$$
\pi_{1}(X_{1}) \to \pi_{1}(X_{0}),
$$

where $X_{1} = X \otimes_{A} K$. It is immediate (cf. EGA IV 12.2) that $X_{1}$ is smooth over $K$, connected (X.1.2),
of dimension 1, and that its genus is equal to $g$, by invariance of the Euler-Poincaré characteristic (cf. EGA III 7).
Since $K$ has characteristic 0, the preceding result applies to it. We have thus proved, by **transcendental methods**:

**Theorem.**

<!-- label: X.2.6 -->

Let $X_{0}$ be a smooth, proper, connected algebraic curve over an algebraically closed field $k$, and let $g$ be its
genus. Then $\pi_{1}(X_{0})$ admits a system of `2g` topological generators, bound by the relation written above. When
the characteristic of $k$ is 0, $\pi_{1}(X_{0})$ is even the group of galoisian type freely generated by the preceding
generators and relation.

<!-- original page 273 -->

**Remarks.**

<!-- label: X.2.7 -->

At present, to the editor’s knowledge, there is no purely algebraic proof of the preceding result, except in genera 0
and 1. To begin with, it is hardly clear how to distinguish `2g` elements in $\pi_{1}(X_{0})$ which one could then expect to
form a system of topological generators. In this respect, the situation of the rational line punctured at $n$ points,
and the study of its coverings tamely ramified at those points, is more sympathetic, since the ramification groups at
these $n$ points provide $n$ elements of the fundamental group to be studied, which one indeed shows generate it
topologically, as we shall see later. \[Translator note: the source footnote refers to Expos\acute{e} XII and notes that these
elements are really determined only up to conjugacy, so a judicious simultaneous choice of representatives is
required.\] But even in this particularly concrete case, there does not seem to be a purely algebraic proof. Such a
proof would plainly be extremely interesting. The only fact concerning the fundamental group of a curve that one knows
how to prove by purely algebraic methods, apart from the weak finiteness theorem X.2.12 below proved algebraically by
Lang and Serre [X.2], seems to be the determination of the abelianized fundamental group via the Jacobian, mentioned at
the end of IX.5.8.

### 2.8.

<!-- label: X.2.8 -->

The last assertion of X.2.6 is no longer valid in characteristic $p > 0$, as one already sees for elliptic curves. As we
have already pointed out, we do not know whether the fundamental group of $X_{0}$ is topologically finitely presented;
this seems quite improbable.

**Theorem.**

<!-- label: X.2.9 -->

Let $k$ be an algebraically closed field, and let $X$ be a proper connected scheme over $k$. Then the fundamental group
of $X$ is topologically finitely generated.

<!-- original page 274 -->

We proceed by induction on $n = \dim X$, the assertion being trivial for $n \leq 0$. Suppose $n > 0$ and the theorem
proved in dimensions $n' < n$. By Chow’s lemma (EGA II 5.6.2), there exists a projective scheme $X'$ over $k$ and a
surjective morphism $X' \to X$. One may plainly suppose $X'$ reduced, and after passing to the normalization, normal. By
descent theory, it is enough to prove that the fundamental groups of the connected components of $X'$ are topologically
finitely generated (IX.5.2). This reduces us to the case where $X$ is **projective** and **normal**. If $n = 1$, it is
enough to apply X.2.6. If $n \geq 2$, consider a projective immersion $X \to \mathbb{P}^{r}_{k}$ and a hyperplane
section $Y = X \cdot H$, endowed with the induced reduced structure, such that $Y \neq X$, that is, $H$ does not contain
$X$. Then $\dim Y < n$, and by the induction hypothesis it is enough to prove that $\pi_{1}(Y) \to \pi_{1}(X)$ is
**surjective**. More generally:

**Lemma.**

<!-- label: X.2.10 -->

Let $X$ be a prescheme proper over an algebraically closed field $k$, and let $g: X \to \mathbb{P}^{r}_{k}$ be a
morphism. Suppose $X$ irreducible and normal and $\dim g(X) \geq 2$. Let $H$ be a hyperplane of $\mathbb{P}^{r}_{k}$ and
let $Y = X \times_{\mathbb{P}^{r}} H$. Then $Y$ is connected, and the homomorphism $\pi_{1}(Y) \to \pi_{1}(X)$ is
surjective.

These assertions follow from:

**Corollary.**

<!-- label: X.2.11 -->

Under the preceding conditions, let $X'$ be a connected étale covering of $X$, and let
$Y' = X' \times_{X} Y = X' \times_{\mathbb{P}^{r}} H$ be the induced covering on $Y$. Then $Y'$ is connected.

Since $X$ is normal, $X'$ is normal; being connected, it is irreducible, and its image in $\mathbb{P}^{r}_{k}$ has
dimension $\geq 2$. A well-known lemma due to Zariski, called the **Bertini theorem**, implies that if $H_{1}'$ is the
generic hyperplane in $\mathbb{P}^{r}_{k}$, defined over an extension $K$ of $k$, then
$X' \times_{\mathbb{P}^{r}} H_{1}$ is universally irreducible, hence universally connected over $K$. Zariski’s
connectedness theorem (EGA III 4) then implies that for **every** hyperplane $H$, defined over any extension of $k$,
$X' \times_{\mathbb{P}^{r}} H$ is geometrically connected. This proves X.2.11, hence X.2.9.

**Corollary (Lang-Serre).**

<!-- label: X.2.12 -->

<!-- original page 275 -->

Under the conditions of X.2.9, for every finite group $G$, the set of isomorphism classes of principal coverings of $X$
with group $G$ is finite.

**Remark.**

<!-- label: X.2.13 -->

Under the conditions of X.2.10, when $\dim g(X) \geq 3$ we shall prove, at least when $g$ is an immersion and $X$
regular, a sharper result known in algebraic geometry as the **Lefschetz theorem**: $\pi_{1}(Y) \to \pi_{1}(X)$ **is an
isomorphism**. [Translator note: the corrected source refers to the subsequent seminar SGA 2, theorem X 3.10.] In the
classical cases there are analogous statements for homology groups and higher homotopy groups, which sooner or later
must be incorporated into abstract algebraic geometry. Even for Hodge cohomology $H^{p}(X, \Omega^{q})$, the question
does not seem to have been studied; moreover, it is hardly likely that for the latter the Lefschetz theorems remain
valid as stated in characteristic $p > 0$.

**Remark (M. Raynaud).**

<!-- label: X.2.14 -->

Let $R$ be a complete discrete valuation ring, with algebraically closed residue field $k$ of characteristic $p > 0$,
fraction field $K$, and let $Y$ be a proper, smooth, connected curve of genus $g$ over $R$. There is a surjective
specialization morphism $sp: \pi_{1}(Y_{\bar{K}}) \to \pi_{1}(Y_{k})$. We have already observed that if $K$ has
characteristic 0, `sp` is not an isomorphism as soon as $g \geq 1$. Suppose $K$ has characteristic $p$, so that $R$ is
isomorphic to the power series ring `k[[T]]`.

In equal characteristic $p > 0$, the fundamental group is not determined by the genus $g$, as one already sees for
elliptic curves, which may be ordinary or supersingular. We quote the recent result of A. Tamagawa, not yet published.
If $G$ is a profinite group, write $G^{res}$ for the profinite quotient of $G$ that is the inverse limit of the finite
solvable topological quotients of $G$.

**Theorem (A. Tamagawa).** Suppose $g \geq 2$, that the special fiber $Y_{k}$ is definable over a finite field, and that
the morphism `sp^res: π₁(Y_K̄)^res → π₁(Y_k)^res` deduced from `sp` by passage to the quotient is bijective. Then the
curve $Y$ is constant over $R$.

Notice that the Galois group of $\bar{K}/K$ is solvable. The preceding statement can also be translated as follows:
suppose that every finite étale covering $X_{K} \to Y_{K}$ of the generic fiber `Y_K`, Galois with solvable Galois
group, has potentially good reduction, that is, extends to a finite étale covering of $Y$ after possibly replacing $R$
by its normalization in a finite extension of $K$. Then $Y$ is constant over $R$.

## 3. Application of the Purity Theorem: Continuity Theorem for Fundamental Groups of Fibers of a Proper and Smooth Morphism

<!-- label: X.3 -->

Recall without proof the following theorem. [Translator note: the source refers for a proof to SGA 2 X.3.4.]

**Purity Theorem (Zariski-Nagata).**

<!-- label: X.3.1 -->

Let $f: X \to Y$ be a quasi-finite and dominant morphism of integral preschemes, with $X$ normal and $Y$ regular locally
noetherian, and let $Z$ be the set of points of $X$ at which $f$ is not étale, that is, where $f$ is ramified
(equivalently, I.9.5(ii)). If $Z \neq X$, then $Z$ has codimension 1 in $X$ at all its points; that is, for every
irreducible component $Z'$ of $Z$ with generic point $z$, the Krull dimension of $\mathcal{O}_{X, z}$ is equal to 1.

Recall that a prescheme is called **normal**, respectively **regular**, if its local rings are normal, respectively
regular, and that the relation $Z \neq X$ also means that the finite extension $R(Z)/R(X)$, where $R$ denotes the field
of rational functions, is **separable**. Placing ourselves at the generic point $z$ of a component $Z'$ of $Z$, and
localizing at the point $y$ of $Y$ below $z$, one obtains

<!-- original page 276 -->

the equivalent statement:

**Corollary.**

<!-- label: X.3.2 -->

Let $A$ be a regular noetherian local ring, and let $A \to B$ be an injective local homomorphism such that $B$ is
normal, a localization of a finite-type $A$-algebra, and **quasi-finite** over $A$. Suppose moreover that
$\dim A (= \dim B) \geq 2$, and that for every prime ideal $\mathfrak{p}$ of $B$ distinct from the maximal ideal, $B$ is
étale over $A$ at $\mathfrak{p}$, that is, $B_{\mathfrak{p}}$ is étale over $A_{\mathfrak{q}}$, where
$\mathfrak{q} = A \cap \mathfrak{p}$. Then $B$ is étale over $A$.

It is not difficult to reduce this last statement to the case where $A$ is a **complete** local ring, hence where $B$ is
**finite** over $A$. Zariski [X.5] gives a simple proof of this result, valid in the equal-characteristic case. The
general case is due to Nagata [X.3], who relies on a delicate result of Chow; the latter was not verified by any of the
participants in the seminar, and should be the subject of a later exposé.

We record here only the very simple proof in the special case $\dim A = 2$, which is enough for the most important
application we shall make of it in the present number. Since $B$ is normal, it is a $B$-module of depth (old
terminology: cohomological codimension) $\geq 2$; hence it is an $A$-module of depth $\geq 2$. Since $A$ is regular of
dimension 2, it follows that $B$ is a **free module** over $A$. [Translator note: the source refers to EGA 0_IV 17.3.4.]
It then follows from I.4.10 that the set of prime ideals $\mathfrak{q}$ of $A$ at which $B$ is ramified over $A$ is the
subset of $\operatorname{Spec}(A)$ defined by a principal ideal (generated by the discriminant of a basis of $B$ over
$A$). Thus it is empty if it is contained in the closed point of $\operatorname{Spec}(A)$, proving X.3.2 when
$\dim A = 2$.

We shall mainly use X.3.1 in the following equivalent form:

**Corollary.**

<!-- label: X.3.3 -->

Let $X$ be a locally noetherian regular prescheme, and let $U$ be an open subset of $X$ whose complement is a closed
subset $Z$ of $X$ of codimension $\geq 2$. Then the functor $X' \mapsto X' \times_{X} U$ from the category of étale
coverings of $X$ to the category of étale coverings of $U$ is an equivalence

<!-- original page 277 -->

of categories. In particular, if $a$ is a geometric point of $U$, the canonical homomorphism
$\pi_{1}(U, a) \to \pi_{1}(X, a)$ is an isomorphism.

The last assertion is plainly a consequence of the first; for the first, one may plainly suppose $X$ connected, hence
irreducible. The normality of $X$ already implies that the functor $X' \mapsto X' \times_{X} U$ from the category of
locally free coverings (not necessarily étale) of $X$ to the category of coverings of $U$ is fully faithful, because the
functor $\mathcal{E} \mapsto \mathcal{E}|U$ from locally free Modules on $X$ to locally free Modules on $U$ is fully
faithful.

It remains to prove that for every **étale** covering $U'$ of $U$, there exists an étale covering $X'$ of $X$,
necessarily unique by what precedes, such that $U'$ is isomorphic to $X' \times_{X} U$. One may plainly suppose $U'$
connected, hence irreducible since $U'$ is normal ($U$ being normal). Let $K$ be the field of rational functions on $X$,
or on $U$, which is the same, and let $K'$ be that of $U'$. Then $U'$ identifies with the normalization of $U$ in $K'$
(I.10.3). Let $X'$ be the normalization of $X$ in $K'$ (EGA II 6.3); then $X' \times_{X} U \simeq U'$. Moreover $X'$ is
normal and integral, and the structural morphism $f: X' \to X$ is **finite** and dominant, since $X$ is normal and
$K'/K$ is a finite separable extension. It is étale over $U' = f^{-1}(U)$, and since $Z$ has codimension $\geq 2$ in
$X$, $f^{-1}(Z)$ has codimension $\geq 2$ in $X'$. We conclude from X.3.1 that $X'$ is étale over $X$, completing the
proof.

Now let $f: X \to Y$ be a rational map from a locally noetherian regular prescheme $X$ to a prescheme $Y$, and suppose
$f$ is defined on an open subset $U$ whose complement is a closed subset of codimension $\geq 2$. Then X.3.3 gives a
functor, defined up to isomorphism, from the category of étale coverings of $Y$ to the category of étale coverings of
$X$; hence for every geometric point $a$ of $U$, with image $b$ in $Y$, a canonical homomorphism

$$
\pi_{1}(X,a) \to \pi_{1}(Y,b),
$$

<!-- original page 278 -->

deduced from the canonical homomorphism $\pi_{1}(U, a) \to \pi_{1}(Y, b)$ by means of the isomorphism
$\pi_{1}(U, a) \simeq \pi_{1}(X, a)$. When $f$ is a dominant morphism, with $X$ and $Y$ integral of function fields $K$
and $L$, so that $K$ is an extension of $L$, and with $Y$ normal, these correspondences become more precise in terms of
field extensions: for every finite extension $L'$ of $L$ unramified over $Y$, the $K$-algebra $K' = L' \otimes_{L} K$ is
unramified over $X$.

In particular, these reflections show that the fundamental group of connected locally noetherian regular preschemes,
pointed by geometric points localized in codimension $\leq 1$, is a **functor** when as morphisms in this category one
takes dominant rational maps defined on complements of closed subsets of codimension $\geq 2$. Recalling, for example,
that a rational map from a normal scheme over a field $k$ to a proper scheme over $k$ is defined on the complement of a
set of codimension $\geq 2$, one obtains:

**Corollary. Birational Invariance of the Fundamental Group.**

<!-- label: X.3.4 -->

Let $k$ be a field, let $X$ and $Y$ be two proper regular schemes over $k$, let $f: X \to Y$ be a birational map from
$X$ to $Y$, and let $\Omega$ be an algebraically closed extension of the function field $K$ of $X$ allowing one to
define the fundamental group of $X$ and the fundamental group of $Y$. These groups are then canonically isomorphic.

This also means that for a finite extension $K'$ of $K$, if it is unramified over one nonsingular proper “model” $X$ of
$K$, it is unramified over every other nonsingular proper model.

**Remark.**

<!-- label: X.3.5 -->

For other applications of the purity theorem, see the work of Abhyankar presented in [X.4], inspired by the results of
Zariski [X.6, Chapter VIII], proved by topological methods. These latter results are far from having been assimilated by
“abstract” algebraic geometry and deserve renewed effort.

<!-- original page 279 -->

We shall need a few elementary facts from ramification theory. Let $V$ be a discrete valuation ring with fraction field
$K$ and residue field $k$; let $L$ be a Galois extension of $K$ with group $G$; let $V'$ be the normalization of $V$ in
$L$, which is a free $V$-module of rank $n = [L:K]$; let $\mathfrak{m}'$ be a maximal ideal of $V'$; let $G_{d}$ be the
subgroup of $G$ consisting of the elements that leave $\mathfrak{m}'$ invariant, so that $G_{d}$ acts on the residue
extension $k' = V'/\mathfrak{m}'$ of $k$; and let $G_{i}$ be the subgroup of elements of $G_{d}$ acting trivially.
Recall that $G_{d}$ and $G_{i}$ are called respectively the **decomposition** and **inertia** subgroups of $G$.

One says that $L$ is **tamely ramified** over $V$ if $n_{i} = [G_{i}:e]$ is of order prime to the characteristic $p$ of
$k$, a condition always satisfied if $k$ has characteristic 0. It is well known that $G_{i}$ then embeds canonically in
the group $k'*$, and is therefore isomorphic to the group of $n_{i}$-th roots of unity in $k'*$. In particular, $G_{i}$
**is cyclic**. The typical case is $L = K[t]/(t^{n} - u)$, where $u$ is a uniformizer of $V$ and $n$ is prime to $p$: if
$K$ contains the $n$-th roots of unity, $L$ is a totally ramified Galois extension of $K$, with Galois group $G = G_{i}$
isomorphic to $\mathbb{Z}/n\mathbb{Z}$.

**Lemma (Abhyankar’s Lemma).**

<!-- label: X.3.6 -->

Let $V$ be a discrete valuation ring with fraction field $K$. Let $L$ and $K'$ be two Galois extensions of $K$ **tamely
ramified** over $V$, and let $n$ and $m$ be the orders of the corresponding inertia groups. Let $L'$ be a composite
extension of $L$ and $K'$ over $K$. If $m$ is a multiple of $n$, then $L'$ is unramified over the localizations of the
normal closure $V'$ of $V$ in $K'$.

Indeed, let $W'$ be the normalization of $V'$ in $L'$, let $\mathfrak{m}'$ be a maximal ideal of $V'$, let
$\mathfrak{n}'$ be a maximal ideal of $W'$ above $\mathfrak{m}'$, and let $\mathfrak{n}$ be the maximal ideal that it
induces on the normalization $W$ of $V$ in $L$. Let $G$, $H$, $M$ be the Galois groups of $L$, $K'$, $L'$ over $K$, and
let $G_{i}$, $H_{i}$, $M_{i}$ be the inertia groups corresponding to the chosen maximal ideals. Then $M$ embeds in
$G \times H$ and $M_{i}$ in $G_{i} \times H_{i}$, in such a way that the projections $M \to G$ and $M \to H$, and
$M_{i} \to G_{i}$

<!-- original page 280 -->

and $M_{i} \to H_{i}$, are surjective (the standard intermediate-field sorites). It already follows, since $G_{i}$ and
$H_{i}$ are by hypothesis cyclic of orders $m$ and $n$ prime to $p$, that $M_{i}$ has order prime to $p$, hence is
cyclic. Since $m$ is a multiple of $n$, all elements of $G_{i} \times H_{i}$ have $m$-th power equal to the identity;
hence $M_{i}$ has order dividing $m$, and therefore order exactly $m$ because $M_{i} \to H_{i}$ is surjective. This last
homomorphism is therefore also injective. But its kernel is the inertia group of $\mathfrak{n}'$ over $\mathfrak{m}'$,
which proves that $L'$ is unramified over $K'$ at $\mathfrak{n}'$. This proves the lemma.

Place ourselves now under the conditions of X.2.4, where one has a **surjective** specialization homomorphism

$$
\pi_{1}(\bar{X}_{1},\bar{a}_{1}) \to \pi_{1}(\bar{X}_{0},\bar{a}_{0})
$$

relative to a proper and separable morphism $f: X \to Y$. We want to make its kernel more precise. Proceeding as in the
proof of X.2.4, one sees that for this question one may always suppose that $Y$ is the spectrum of a **complete discrete
valuation ring $V$ with algebraically closed residue field**, since one can always find such a ring and a morphism from
its spectrum $Y'$ into $Y$ whose image is ${y_{0}, y_{1}}$. Then $X_{0} = \bar{X}_{0}$, $\kappa(y_{0}) = k$ is the
residue field of $V$, and $\kappa(y_{1}) = K$ is the fraction field of $V$. Let $K_{s}$ be the separable closure of $K$,
$\bar{K}$ its algebraic closure, and for every subring $W$ of $\bar{K}$ containing $V$ put $X_{W} = X \otimes_{V} W$. In
particular,

```text
X_V = X,    X_K = X₁,    X_K̄ = X̄₁.
```

Moreover the canonical morphism $\bar{X}_{1} = X_{\bar{K}} \to X_{K_{s}}$ induces an isomorphism on fundamental groups
(IX.4.11). Thus, taking into account the isomorphism X.2.1, $\pi_{1}(X_{0}) \to \pi_{1}(X)$, we are reduced to studying
the surjective homomorphism

```text
π₁(X_K_s) → π₁(X)
```

associated with the canonical morphism $X_{K_{s}} \to X$.

<!-- original page 281 -->

Determining the kernel of this latter homomorphism is equivalent to solving the following problem: **given a connected
principal covering $Z_{K_{s}}$ of $X_{K_{s}}$ with group $G$** (hence associated with a homomorphism from
$\pi_{1}(X_{K_{s}})$ to $G$), **determine under what conditions it is isomorphic to the inverse image of a principal
covering $Z$ of $X$ with group $G$.**

First note that $K_{s}$ is the filtered increasing union of its finite subextensions $K'$ over $K$, and therefore
$Z_{K_{s}}$ is isomorphic to the inverse image of a principal covering $Z_{K'}$ of $X_{K'}$ for a suitable $K'$. Be
careful, however, that for fixed $K'$, $Z_{K'}$ is not uniquely determined. To say that $Z_{K_{s}}$ is isomorphic to the
inverse image of a principal covering $Z$ of $X$ means that there exists a finite subextension $K'' \supset K'$ of
$K_{s}$ such that $Z_{K''} = Z_{K'} \otimes_{K'} K''$ is isomorphic to $Z \otimes_{V} K''$.

Now, for a finite subextension $K'$ of $K_{s}$, denote by $V'$ the normalization of $V$ in $K'$. This is a complete
discrete valuation ring with residue field $k$. The canonical morphism $X_{V'} \to X_{V}$ therefore induces an
isomorphism on the fibers above the closed points of $Y = \operatorname{Spec}(V)$ and $Y' = \operatorname{Spec}(V')$;
applying X.2.1 to `X_V` and $X_{V'}$, it follows that the induced homomorphism on fundamental groups
$\pi_{1}(X_{V'}) \to \pi_{1}(X_{V})$ is an isomorphism. Equivalently, every principal covering of $X_{V'}$ is the
inverse image of a principal covering of `X_V`, determined up to isomorphism. This implies:

**Lemma.**

<!-- label: X.3.7 -->

Let $Z_{K'}$ be a connected principal covering of $X_{K'}$ with group $G$, and let $Z_{K_{s}}$ be its inverse image on
$X_{K_{s}}$. Then $Z_{K_{s}}$ is isomorphic to the inverse image of a principal covering $Z$ of $X$ if and only if there
exists a finite extension $K'' \supset K'$ of $K$ in $K_{s}$ such that the principal covering $Z_{K''}$ of $X_{K''}$ is
induced by a principal covering of $X_{V''}$.

Suppose in particular that the $X_{V''}$ are normal. It is enough, for example, that $X_{0}$ be normal, and a fortiori
that $X_{0}$ be simple; cf. I.9.1.

<!-- original page 282 -->

Since they are connected, they are then irreducible. Let $L$ be the field of rational functions of $X$ and `X_K`, let
$L'$ be the field for $X_{V'}$ and $X_{K'}$, and let $L''$ be the field for $X_{V''}$ and $X_{K''}$. Under the
conditions of X.3.7, $Z_{K'}$ defines a finite separable extension $R'$ of $L'$, and $Z_{K''}$ defines the extension
$R'' = R' \otimes_{L'} L'' = R' \otimes_{K'} K''$. The condition considered in X.3.7 therefore also means that there
exists a finite separable extension $K''$ of $K'$ such that $R'' = R' \otimes_{K'} K''$ is **unramified** over the
normal scheme $X_{V''}$ with function field $L'' = L' \otimes_{K'} K''$, and not only over the open part $X_{K''}$ of
$X_{V''}$.

From now on suppose that $f: X \to Y$ is a **smooth** morphism. Then the morphisms $X_{V'} \to \operatorname{Spec}(V')$
are smooth, and therefore the schemes $X_{V'}$ are **regular**. Notice that the fiber of the closed point of
$\operatorname{Spec}(V')$ in $X_{V'}$ is irreducible and of codimension 1. Let $\mathfrak{o}'$ be its local ring; this
is a discrete valuation ring with fraction field $L'$ and residue field isomorphic to the field of rational functions of
$X_{0}$, hence with the same characteristic as $k$. Define similarly $\mathfrak{o}''$ in $L''$; it is plainly the
normalization of $\mathfrak{o}'$ in $L''$. It then follows from the purity theorem X.3.1, or X.3.3, that $R''$ is
unramified over $X_{V''}$ if and only if $R''$ is unramified over $\mathfrak{o}''$, the normalization of $\mathfrak{o}'$
in $L''$.

Now note that if $u'$ is a uniformizer of $V'$, it is also a uniformizer of $\mathfrak{o}'$. If $n$ is an integer prime
to the characteristic $p$ of $k$, and if one takes $K'' = K'[t]/(t^{n} - u')$, then $K''$ is a finite Galois extension
of $K'$ and $L''$ is isomorphic to $L'[t]/(t^{n} - u')$, hence is tamely ramified over $\mathfrak{o}'$ with inertia
group of order $n$. Suppose now that $G$ has order prime to $p$. Then $R'$ is tamely ramified over $\mathfrak{o}'$. Take
$n$ to be a multiple prime to $p$ of the order of the inertia group of $R'$ over $\mathfrak{o}'$, for example
$n = [G:e]$. Applying Abhyankar’s lemma X.3.6, one sees that the condition considered in X.3.7 is satisfied.

This proves the following theorem:

**Theorem.**

<!-- label: X.3.8 -->

Let $f: X \to Y$ be a proper and smooth morphism with geometrically connected fibers, with $Y$ locally noetherian. Let
$y_{0}$ and $y_{1}$ be two points of $Y$ such that $y_{0} \in cl({y_{1}})$, let $\bar{X}_{0}$ and $\bar{X}_{1}$ be the
corresponding geometric fibers, and consider the specialization homomorphism of X.2.4

$$
\pi_{1}(\bar{X}_{1}) \to \pi_{1}(\bar{X}_{0}).
$$

This homomorphism is surjective, and every continuous homomorphism from $\pi_{1}(\bar{X}_{1})$ to a finite group $G$ of
order prime to the characteristic $p$ of $\kappa(y_{0})$ comes from a homomorphism from $\pi_{1}(\bar{X}_{0})$ to $G$.

<!-- original page 283 -->

In other words:

**Corollary.**

<!-- label: X.3.9 -->

If $\kappa(y_{0})$ has characteristic zero, then the specialization homomorphism is an isomorphism. If $\kappa(y_{0})$
has characteristic $p > 0$, then the kernel of the specialization homomorphism is contained in the intersection of the
kernels of the continuous homomorphisms from $\pi_{1}(\bar{X}_{1})$ to finite groups of order prime to $p$, or
equivalently in the closed normal subgroup generated by a $p$-Sylow subgroup of the group of galoisian type
$\pi_{1}(\bar{X}_{1})$. Thus, if $\pi_{1}(\bar{X}_{1})^{p}$ denotes the quotient group of $\pi_{1}(\bar{X}_{1})$ by the
preceding closed subgroup, and if $\pi_{1}(\bar{X}_{0})^{p}$ is defined similarly, then the specialization homomorphism
induces an **isomorphism**

$$
\pi_{1}(\bar{X}_{1})^{p} \simeq \pi_{1}(\bar{X}_{0})^{p}.
$$

Notice that the proof of X.3.8 is purely algebraic. Proceeding as in X.2.6, one concludes by **transcendental methods**:

**Corollary.**

<!-- label: X.3.10 -->

Let $X_{0}$ be a proper, smooth, connected curve of genus $g$ over an algebraically closed field of characteristic $p$.
With the notation introduced in X.3.9, the group $\pi_{1}(X_{0})^{p}$ is isomorphic to $\Gamma^{p}$, where $\Gamma$ is
the group of galoisian type generated by generators $s_{i}, t_{i}$, $1 \leq i \leq g$, bound by the relation

```text
(s₁t₁s₁⁻¹t₁⁻¹)⋯(s_gt_gs_g⁻¹t_g⁻¹) = 1.
```

**Remarks.**

<!-- label: X.3.11 -->

<!-- original page 284 -->

When $\kappa(y_{0})$ has characteristic zero, the result X.3.9 is well known by transcendental methods. Notice that the
proof of X.3.10 appeals to the purity theorem in the unequal-characteristic case, but only for rings of dimension 2,
where the proof of that theorem is easy and was recalled in the text.

## Bibliography

**[X.1]** K. Kodaira, “On compact analytic surfaces,” _Annals of Mathematics_ **71** (1960), pp. 111–152.

**[X.2]** S. Lang and J.-P. Serre, “Sur les revêtements non ramifiés des variétés algébriques,” _American Journal of
Mathematics_ **79** (1957), pp. 319–330.

**[X.3]** M. Nagata, “On the purity of branch loci in regular local rings,” _Illinois Journal of Mathematics_ **3**
(1959), pp. 328–333.

**[X.4]** J.-P. Serre, _Revêtements ramifiés du plan projectif (d’après S. Abhyankar)_, Séminaire Bourbaki, May 1960.

**[X.5]** O. Zariski, “On the purity of the branch locus of algebraic functions,” _Proceedings of the National Academy
of Sciences USA_ **44** (1958), pp. 791–796.

**[X.6]** O. Zariski, _Algebraic Surfaces_, Ergebnisse, 1948; Chelsea, New York.


<!-- SOURCE: 11-exemples-et-complements.md -->

# Exposé XI. Examples and Complements

<!-- label: XI -->

<!-- original page 285 -->

## 1. Projective Spaces, Unirational Varieties

<!-- label: XI.1 -->

**Proposition.**

<!-- label: XI.1.1 -->

Let $k$ be an algebraically closed field, and let $X = \mathbb{P}^{r}_{k}$ be projective space of dimension $r$ over
$k$. Then $X$ is **simply connected**, that is, $\pi_{1}(X) = 0$.

For $r = 0$ this is trivial. If $r = 1$, one must show that if $X'$ is a nonempty connected étale covering of
$X = \mathbb{P}^{1}_{k}$, then $X' \simeq X$. The genus formula gives, if $g$ and $g'$ are the genera of $X$ and $X'$,

$$
1 - g' = d(1 - g),
$$

where $d$ is the degree of $X'$ over $X$. Since $g = 0$, we have $1 - g' = d$, which forces $d = 1$ because $g' \geq 0$;
this proves $X' \simeq X$.

When $r \geq 2$, one proceeds by induction on $r$, assuming ${\mathbb{P}^{r}}'$ simply connected for $r' < r$. Applying
this to a hyperplane of $\mathbb{P}^{r}$ and using X.2.10, it follows that $\mathbb{P}^{r}$ is simply connected. Another
proof: by X.1.7 one has

```text
π₁(ℙ¹ × ⋯ × ℙ¹) = π₁(ℙ¹) × ⋯ × π₁(ℙ¹),
```

so $(\mathbb{P}^{1})^{r}$ is simply connected because $\mathbb{P}^{1}$ is. Hence $\mathbb{P}^{r}$ is simply connected by
birational invariance of the fundamental group (X.3.4). This proof shows more generally:

**Corollary.**

<!-- label: XI.1.2 -->

Let $X$ be a proper normal scheme over an algebraically closed field $k$. If $X$ is a rational variety, that is,
integral and with function field a purely transcendental extension of $k$, then $X$ is simply connected.

This result applies in particular to Grassmann varieties and, more generally,

<!-- original page 286 -->

to varieties $G/H$, where $G$ is a connected linear group over $k$ and $H$ is an algebraic subgroup containing a Borel
subgroup of $G$.

Recall that a variety **unirational over $k$** means a proper integral scheme over $k$ whose function field $K$ is
contained in a purely transcendental extension $K'$ of $k$, finite over $K$ (that is, with the same transcendence degree
over $k$ as $K$), or equivalently, for which there exists a dominant rational map $f: \mathbb{P}^{r}_{k} \to X$ with
$r = \dim X$. If $X$ is normal, the reflections preceding X.3.4 show that for every connected étale covering $X'$ of
$X$, with function field $L/K$, the $K'$-algebra $L \otimes_{K} K'$ is unramified over the model $\mathbb{P}^{r}$, hence
completely decomposed by XI.1.1. This shows that $L$ is $K$-isomorphic to a subextension of $K'/K$. Taking V.8.2 into
account, this proves:

**Corollary.**

<!-- label: XI.1.3 -->

The fundamental group of a normal unirational variety over an algebraically closed field is finite.

Notice that in the definition of “unirational,” one did not need $K'/K$ to be finite.

**Remarks.**

<!-- label: XI.1.4 -->

The results of this number are, of course, well known. Moreover, J.-P. Serre showed [XI.10] that when $X$ is a smooth
projective unirational variety over an algebraically closed field of **characteristic zero**, $X$ is simply connected.
His proof is transcendental, using Hodge symmetry.

[M. Raynaud, added in 2003.] Restrict to the case of an algebraically closed field $k$ of characteristic $p \geq 0$. In
characteristic $p > 0$, the definition of a unirational $k$-variety given above is that of a weakly unirational
$k$-variety, as opposed to a strongly unirational $k$-variety, where one also assumes that $K'$ is a separable extension
of $K$.

In dimension 2, there exist smooth projective weakly unirational surfaces with nontrivial fundamental group (finite by
XI.1.3), and hence nonrational surfaces; see T. Shioda, “On unirationality of supersingular surfaces,” _Mathematische
Annalen_ **225** (1977), pp. 155–159. By contrast, a strongly unirational surface is rational: this follows from
Castelnuovo’s rationality criterion, extended to characteristic $p > 0$ by O. Zariski; cf. J.-P. Serre, Séminaire
Bourbaki no. 146, 1957, and _Œuvres/Collected Papers_, vol. 1, p. 467.

Over the field $\mathbb{C}$ of complex numbers, examples are known of smooth projective varieties of dimension $\geq 3$
that are unirational and nonrational; cf. P. Deligne, “Variétés unirationnelles non rationnelles (d’après M. Artin et D.
Mumford),” Séminaire Bourbaki no. 402, 1971-72, Lecture Notes vol. 317. A smooth cubic hypersurface in projective
4-space is one such example. Some of these examples extend to characteristic `> 0` to give strongly unirational
nonrational varieties; cf. J.-P. Murre, “Reduction of the proof of the non-rationality of a non singular cubic threefold
to a result of Mumford,” _Compositio Mathematica_ **27** (1973), pp. 63–82.

Let $V$ be a normal integral projective $k$-variety. One says that $V$ is rationally connected if there exist an
integral finite-type $k$-scheme $T$ and a $k$-morphism $F: T \times \mathbb{P}^{1} \to V$ such that the morphism

```text
T × ℙ¹ × ℙ¹ → V × V,
(t,u,u′) ↦ (F(t,u), F(t,u′))
```

is dominant. In particular, through two sufficiently general rational points of $V$ there passes a rational curve. The
terminology is justified by the fact that if $V$ is rationally connected, two rational points can be joined by a finite
chain of rational curves. If $k$ has characteristic $p > 0$, one strengthens the preceding definition by requiring that
the displayed map be generically smooth. This gives the notion of separably rationally connected variety. Thus
unirational varieties are rationally connected, and in characteristic $p > 0$ strongly unirational varieties are
separably rationally connected. J. Kollár showed that separably rationally connected varieties have trivial algebraic
fundamental group; cf. O. Debarre, “Variétés rationnellement connexes (d’après T. Graber, J. Harris, J. Starr et A. J.
de Jong),” Séminaire Bourbaki no. 906, 2001-2002.

## 2. Abelian Varieties

<!-- label: XI.2 -->

Let $k$ be an algebraically closed field, let $A$ be an abelian variety over $k$, that is, a group scheme over $k$,
proper, smooth, and connected over $k$, and finally let $G$ be a commutative group scheme of finite type over $k$.
Denote by $Ext(A,G)$ the group of classes of commutative extensions of $A$ by $G$, and by $H^{1}(A,G)$ the group of
classes of principal bundles on $A$ with group $G$ (compare no. XI.4 below). Consider the canonical homomorphism

$$
Ext(A,G) \to H^{1}(A,G).
$$

<!-- original page 287 -->

An argument of Serre [XI.5, Chapter VII, Theorem 5] shows that this is an injective homomorphism, whose image is the set
of “primitive elements” of $H^{1}(A,G)$, that is, the elements $\xi$ for which

$$
\pi*(\xi) = pr_{1}*(\xi) + pr_{2}*(\xi),
$$

where $pr_{i}$ are the two projections from $A \times A$ to $A$, and $\pi: A \times A \to A$ is the composition law of
$A$. Serre states his theorem only for $G$ linear and connected, and of course smooth over $k$, but by simplifying the
first part of his argument one sees that these restrictions are unnecessary. It is enough to note that every morphism
from $A$ to a group scheme $E$ of finite type over $k$ that sends the identity to the identity is a group homomorphism,
and to apply this to sections over $A$ of an extension $E$ of $A$ by $G$.

We shall apply this result when $G$ is a finite separable group over $k$, that is, an ordinary finite group, assumed
commutative. Using $\pi_{1}(A \times A) \simeq \pi_{1}(A) \times \pi_{1}(A)$ (X.1.7), and interpreting $H^{1}(X,G)$ as
$\operatorname{Hom}(\pi_{1}(X),G)$ for every algebraic scheme $X$, in particular for $X = A$ or $X = A \times A$, one
sees that every class in $H^{1}(A,G)$ is primitive. Thus one has an isomorphism

$$
Ext(A,G) \simeq H^{1}(A,G).
$$

In other words, **every principal covering of $A$ with commutative structural group $G$, pointed above the origin of
$A$, is endowed in a unique way with a structure of algebraic group having the marked point as origin, and such that
$A' \to A$ is a homomorphism of algebraic groups.** In particular, if $A'$ is connected, it is also an abelian variety,
isogenous to $A$.

On the other hand, since the functor $X \mapsto \pi_{1}(X)$ from pointed algebraic schemes $X$ to groups commutes with
products (IX.1.7), it sends a group in the first category to a group in the category of groups, that is, to a
**commutative** group. Hence **if $A$ is an abelian variety, $\pi_{1}(A)$**

<!-- original page 288 -->

**is a commutative group.** Thus, to know $\pi_{1}(A)$, it is enough to know the functor

$$
G \mapsto H^{1}(A,G) = \operatorname{Hom}(\pi_{1}(A),G)
$$

as $G$ varies through finite **commutative** groups. Finally, recall that for every integer $n > 0$, the
multiplication-by-$n$ homomorphism in $A$,

$$
A --n\to A,
$$

is surjective, hence has finite kernel, that is, it is an isogeny; it follows that every isogeny $A' \to A$ is a
quotient of an isogeny of the preceding type. From this, and from standard arguments (cf. for example [XI.6]), one
obtains:

**Theorem (Serre-Lang).**

<!-- label: XI.2.1 -->

Let $A$ be an abelian variety over an algebraically closed field $k$. For every integer $n > 0$, let $K_{n}$ be the
ordinary finite group underlying the kernel ${}_{nA}$ of multiplication by $n$ in $A$, and put, for every prime number
$\ell$,

$$
T_{\ell}(A) = \lim_{r} K^{r}_{\ell}
$$

and

```text
T_·(A) = ∏_ℓ T_ℓ(A) = lim_n K_n,
```

where, for $m$ a multiple of $n$, $m = ns$, one sends $K_{m}$ to $K_{n}$ by multiplication by $s$. Then $\pi_{1}(A)$ is
canonically isomorphic to $T_{\cdot}(A)$. Hence for every prime number $\ell$, the $\ell$-primary component of
$\pi_{1}(A)$ is canonically isomorphic to $T_{\ell}(A)$.

Notice that these isomorphisms are functorial in $A$. The module $T_{\ell}(A)$ is called the **$\ell$-adic Tate module**
of the abelian variety $A$. It is an additive functor in $A$; in particular it gives rise to a representation of the
ring $\operatorname{Hom}(A,A)$ of endomorphisms of $A$ in $T_{\ell}(A)$, called the **$\ell$-adic Weil representation**,
which plays an important role in the theory of abelian varieties (cf. for example [XI.4, Chapter VII]). Theorem XI.2.1
gives an interpretation of it in terms of the natural representation in the **$\ell$-adic homology group** of $A$,

$$
H_{1}(A,\mathbb{Z}_{\ell}) = \pi_{1}(A)_{\ell},
$$

<!-- original page 289 -->

which is plainly more satisfactory a priori, especially from the point of view of the Lefschetz formula \[XI.4, Chapter
V\]. Recall Weil’s results on the structure of $T_{\ell}(A)$:

a) If $n$ is prime to $char(k)$, then $K_{n}$ is a free module of rank $2 \dim A$ over $\mathbb{Z}/n\mathbb{Z}$. Hence
if $\ell$ is a prime number different from $char(k)$, $T_{\ell}(A)$ is a free module of rank $2 \dim A$ over the ring
$\mathbb{Z}_{\ell}$ of $\ell$-adic integers.

b) If $n$ is a power of $char(k) = p$, then $K_{n}$ is a free module of rank $\nu \leq \dim A$ over
$\mathbb{Z}/n\mathbb{Z}$, with $\nu$ independent of $n$. Hence $T_{p}(A)$ is a free module of rank $\nu \leq \dim A$
over the ring $\mathbb{Z}_{p}$ of $p$-adic integers.

This shows that in the theory of the fundamental group developed here, the fundamental group of a variable abelian
variety does not vary regularly with the parameter: its $p$-primary component may suddenly drop for values of the
parameter $t$ corresponding to residual characteristic $p$. The best-known case of this phenomenon is that of elliptic
curves.

Notice, however, that for every $n$, whether or not $n$ is prime to the characteristic, the true kernel ${}_{nA}$ in $A$
of multiplication by $n$ is a finite group scheme over $k$ of degree $n^{2g}$, where $g = \dim A$; it is nonseparable
over $k$ if $n$ is a multiple of $p = char(k)$. Moreover, when $A$ varies in a family of abelian varieties, that is,
when one has an abelian scheme $A$ over a base scheme $S$, one shows more generally that ${}_{nA}$ is a finite flat
group scheme over $S$, of degree $n^{2g}$ over $S$. In other words, provided that the infinitesimal parts of the kernels
${}_{nA}$ are taken into account, they behave regularly for every $n$.

This suggests that the “true” fundamental group of an abelian variety $A$ is the pro-algebraic group (formal inverse
limit of finite groups over $k$)

$$
\lim_{n} {}_{nA},
$$

where by the “true fundamental group” of an algebraic scheme $X$ one should mean the pro-group that classifies principal
coverings of $X$ with structural group an arbitrary finite group scheme $G$ over $k$, not necessarily separable over
$k$. In this way, for example, from the representations of $\operatorname{Hom}(A,A)$ in the $p$-primary component of the
true fundamental group of $A$, one recovers the Weil characteristic polynomial defined by the latter using the
$\ell \neq p$, in a more natural way than Serre’s construction [XI.8].

## 3. Projective Cones, Zariski’s Example

<!-- label: XI.3 -->

<!-- original page 290 -->

For simplicity, keep $k$ algebraically closed, and let $V$ be a connected projective $k$-scheme, a closed subscheme of
$\mathbb{P}^{r}_{k}$, which one may assume nonsingular if desired. Let $Y = \hat{C}$ be the projective cone over $V$,
let $y_{0}$ be its vertex, let $X = \hat{C}_{V}$ be the usual projective closure of the vector bundle
$C_{V} = V(\mathcal{O}_{V}(1))$ associated with $\mathcal{O}_{V}(1)$, and finally let

$$
f: X \to Y
$$

be the canonical morphism contracting the zero section $X_{0}$ of `C_V` on $X$ to a point (EGA II 8.6.4). Since $X$ is a
locally trivial bundle over $V$ with fibers $\mathbb{P}^{1}$, hence with simply connected fibers, the morphism
$p: X \to V$ induces, by X.1.4, an isomorphism

$$
\pi_{1}(X) \simeq \pi_{1}(V).
$$

Since $p$ induces an isomorphism $X_{0} \to V$, it follows that **an étale covering of $X$ is completely decomposed if
and only if its restriction to $X_{0}$ is so**. But for every étale covering $Y'$ of $Y$, the inverse image
$X' = X \times_{Y} Y'$ is an étale covering of $X$ completely decomposed over the fiber $X_{0}$, hence trivial. Since
the homomorphism $\pi_{1}(X) \to \pi_{1}(Y)$ is surjective (IX.3.4), it follows that

$$
\pi_{1}(Y) = (e).
$$

In other words, **every projective cone is simply connected.** In characteristic 0, the same result remains true with
$Y$ taken to be the affine cone.

Now suppose $V$ regular, that is, smooth over $k$. Then $X$ is regular, and for a suitable projective embedding of $V$
one obtains a **normal** projective cone $Y$. If $V$ is not simply connected, hence $X$ is not simply connected, let
$X'$ be a nontrivial connected étale covering of $X$. Since the fibers of $X$ over the points $y \in Y$ distinct from
$y_{0}$ are reduced to a point, the restriction of $X'$ to its fibers, in particular to the

<!-- original page 291 -->

generic fiber, is trivial. Nevertheless $X'$ does not come by inverse image from an étale covering of $Y$, since $Y$ is
simply connected and $X'$ would then be completely decomposed. This shows that X.1.3 and X.1.4 become false if the
hypothesis that $f$ is separable is replaced by the weaker hypothesis that its fibers are separable algebraic schemes,
or even smooth schemes, over the $\kappa(s)$. Similarly, the fundamental groups of the geometric fibers $\bar{X}_{y}$
for $y \neq y_{0}$ are plainly reduced to `(e)`, since these fibers are reduced to a point, while
$\pi_{1}(X_{0}) \neq e$; hence the semicontinuity theorem X.2.4 also fails for $f$.

Finally let us indicate the example, pointed out by Zariski, that makes the same theorems fail when the hypothesis that
$f$ is separable is replaced by the hypothesis that $f$ is flat. Let $f: X \to Y$ be a morphism from a nonsingular
projective surface to the rational line $Y = \mathbb{P}^{1}$, such that $K = k(X)$ is a “regular” extension, that is,
primary and separable, of $k(f)$ (equivalently, the geometric generic fiber is connected and separable), and such that
the divisor $(f) = X_{0} - X_{\infty}$ is an $n$-th multiple of a divisor, where $n$ is an integer prime to the
characteristic. Such examples can be constructed in every characteristic.

Let $X'$ be the normalization of $X$ in $K(f^{1/n})$, where $K = k(X)$ is the function field of $X$. The hypothesis on
`(f)` implies that $X'$ is étale over $X$. Let $Y'$ be the normalization of $Y$ in $k(t)(t^{1/n})$; it is ramified over
$Y$ exactly at $t = 0$ and $t = \infty$, and the restriction $X'|f^{-1}(U)$ is isomorphic to the inverse image of $Y'|U$. In
particular, the restriction of $X'$ to the **geometric** generic fiber of $X$ over $Y$ decomposes completely.
Nevertheless $X'$ is not isomorphic to the inverse image of an étale covering of $Y$, since one sees immediately that
the latter would necessarily be $Y'$, which is absurd because $Y'$ is ramified over $Y$. \[Translator note: the source
footnote observes that, from the viewpoint of the étale topology (SGA 4 VII), in this example $R^{1}(f_{et})_{*}(\mathbb{Z}/n\mathbb{Z})$ is
“non-separated” over $S$.\]

Here is a simple way, due to Serre, to realize the conditions of this example, inspired by [XI.5, no. 20]. Take $n$ to
be a prime number $\geq 5$, distinct from the characteristic, and let $G = \mathbb{Z}/n\mathbb{Z}$ act on affine 4-space $k^{4}$ by multiplying
the coordinates by four distinct characters of $G$, which is possible since $n \geq 5$. \[M. Raynaud, added in 2003: $k^{4}$
denotes affine 4-space over $k$.\] Then $G$ acts on projective space $\mathbb{P}^{3}_{k}$, and the only fixed points under $G$ are the
four points corresponding to the coordinate axes. The surface $X'$ with equation

```text
xⁿ + yⁿ + zⁿ + tⁿ = 0
```

is smooth over

<!-- original page 292 -->

$k$ by the Jacobian criterion, and contains none of the fixed points. Since $G$ has prime order, it acts on $X'$
“without fixed points,” that is, $X'$ is a principal covering of $X = X'/G$ with group $G$.

Let $g = x/y$ in $k(X') = K'$. This is a Kummer generator of $K'$ over $K = k(X)$ if the chosen characters were
$\chi^{i}$, $i = 0,1,2,3$, with $\chi$ a primitive character. Let $f$ be its $n$-th power, which is an element of $K$.
One sees at once that $K'$ is a regular extension of $k(g)$. This follows from the fact that the plane curve with
homogeneous equation in `U,T,Z`

$$
T^{n} + Z^{n} + (1 + g^{n})U^{n} = 0
$$

is smooth over $k(g)$, by the Jacobian criterion, and from the fact that every plane curve is connected. On the other
hand, $k(f) = K \cap k(g)$, since the right-hand side is an extension of $k(f)$ contained in the prime-degree extension
$k(g)$, and distinct from $k(g)$ because $g \notin K$. This implies that $K$ is a regular extension of $k(f)$.

Finally, the divisor of $f$ on $X$ is an $n$-th multiple of a divisor, since its inverse image on $X'$ is the divisor of
$g^{n}$, hence an $n$-th multiple, and one can descend because $X'$ is étale over $X$. We would be done if the rational
map $f: X \to \mathbb{P}^{1}$ were a morphism, that is, if the divisors of zeros and poles of $f$ did not meet. In fact,
one verifies easily, again by looking on $X'$, that the two divisors in question are the products by $n$ of two smooth
curves over $k$ meeting transversely at one point $a$. Replacing $X$ by the scheme obtained by blowing up $a$, the
preceding conditions ($div(f)$ divisible by $n$, and $k(X_{1}) = k(X)$ a regular extension of $k(f)$) remain satisfied,
but moreover $f$ is a **morphism** $X_{1} \to \mathbb{P}^{1}$. Thus we are in the desired situation.

## 4. The Cohomology Exact Sequence

<!-- label: XI.4 -->

Let $S$ be a prescheme, so that the category $Sch_{/}S$ of preschemes over $S$ is determined, and hence also the notion of
a group in it; such a group will also be called a **group prescheme over $S$**, or simply an **$S$-group**. To simplify
the exposition and fix ideas, in what follows we shall most often restrict to groups that are **affine** and **flat**
over $S$. \[Translator note: the source footnote says that quasi-affineness instead of affineness would suffice for what
follows; cf. the footnote referred to as note 296 in the source.\] This will be enough for the applications we have in
view. Of course, there are many cases where neither hypothesis is satisfied.

<!-- original page 293 -->

Let $G$ be such an $S$-group, and let $P$ be a prescheme over $S$ on which $G$ acts on the right; in particular this
gives a morphism

```text
π: P ×_S G → P
```

in the category $Sch_{/}S$, satisfying the familiar axioms. We say that $P$ is **formally principal homogeneous under**
$G$ if the morphism

```text
P ×_S G → P ×_S P
```

with components $pr_{1}$ and $\pi$ is an isomorphism. Equivalently, for every object $S'$ of $Sch_{/}S$, the set
$P(S') = \operatorname{Hom}_{S}(S',P)$, regarded as a set with operator group $G(S') = \operatorname{Hom}_{S}(S',G)$, is
either empty or principal homogeneous, that is, empty or isomorphic to $G(S')$ with $G(S')$ acting by right
translations.

We say that $P$ is **trivial** if $P$ is isomorphic to $G$, with $G$ acting on itself by right translations, or
equivalently if each of the operator sets $P(S')$ under $G(S')$ is trivial. One verifies, for example by the patented
procedure of passing to the set-theoretic case, that $P$ **is trivial if and only if it is formally principal
homogeneous and admits a section over $S$**. This last fact can be phrased categorically by saying that $P$ has a
section over the final object $e = S$ of $Sch_{/}S$, that is, that there exists a morphism from $e$ to $P$.

To define the notion of a principal homogeneous bundle $P$ under $G$, stronger than that of a formally principal
homogeneous bundle, one must first specify in $Sch_{/}S$ a class of morphisms to be used for “descent,” and which will
play the role of “localization morphisms” for “trivializing” bundles. The most suitable choice varies with context; no
one choice contains all the others. [Translator note: the source refers here to SGA 3 IV, especially §4.] Here it is
convenient to adopt the following definition:

**Definition.**

<!-- label: XI.4.1 -->

Let $G$ be an $S$-group. A **principal homogeneous bundle** (on the right) under $G$ is an $S$-prescheme $P$ with a
right action of the $S$-group $G$, such that there exists a covering of $S$ by open subsets $U_{i}$, and for each $i$ a
faithfully flat and quasi-compact base-change morphism $S'_{i} \to U_{i}$, such that $P' = P \times_{S} S'$ is a trivial
operator prescheme under $G' = G \times_{S} S'$, where $S'$ is the $S$-prescheme that is the disjoint sum of the
$S'_{i}$.

<!-- original page 294 -->

The base-change functor $X \mapsto X' = X \times_{S} S'$, being left exact, sends groups to groups and objects with
operator group to objects with operator group. Notice that XI.4.1 is **stable under base change**. Also:

**Proposition.**

<!-- label: XI.4.2 -->

Let $G$ be an $S$-group, flat and quasi-compact over $S$, and let $P$ be an $S$-prescheme on which $G$ acts on the
right. The following conditions are equivalent:

1. $P$ is a principal homogeneous bundle under $G$.
1. $P$ is formally principal homogeneous under $G$, and the structural morphism $P \to S$ is faithfully flat and
   quasi-compact.

If $P$ is principal homogeneous under $G$, then with the notation of XI.4.1, $P'$ is faithfully flat and quasi-compact
over $S'$, since $G'$ is so and $P'$ is $S'$-isomorphic to it. Hence $P$ has the same properties over $S$ (for
“surjective” and “quasi-compact,” cf. VIII.3.1; for “flat,” this is an omission in the sorites of Exposé VIII).
Conversely, if 2 holds, take the base change $S' = P$, which is indeed faithfully flat and quasi-compact over $S$. Then
$P'$ is formally principal homogeneous over $S'$ because $P$ is so over $S$ and base change is left exact. Moreover $P'$
has a section over $S'$, namely the diagonal section, hence it is a trivial principal bundle. This proves the assertion.

**Corollary.**

<!-- label: XI.4.3 -->

If $G$ is affine and flat over $S$, every principal homogeneous bundle $P$ under $G$ is affine and flat over $S$.

Indeed, it becomes so after a faithfully flat and quasi-compact base extension, and one applies VIII.5.6.

The usefulness of Definition XI.4.1 for $S$-groups **flat** and **affine** over $S$ rests on VIII.2.1, that is, on the
fact that the morphisms $S' \to S$ considered in XI.4.1 are morphisms of effective descent for the category of
preschemes affine over other preschemes. Thanks to this fact, the verification of the facts sketched below is
essentially “categorical.” [Translator note: the source refers again to the footnote cited above.]

Let $E$ be an $S$-prescheme on which the $S$-group $G$ acts on the left, and let $P$ be a principal homogeneous bundle
on the right under $G$. We want to define an associated bundle $E^{P}$, “locally” isomorphic to $E$. To do this, make
$G$ act on the right on $P \times_{S} E$ by the law

$$
(x,y) \mapsto (xg,g^{-1}y),
$$

<!-- original page 295 -->

which describes such actions in the set-theoretic context and extends to categories by the patented procedure. We put,
subject to existence,

```text
E^(P) = (P ×_S E)/G.
```

With this convention, $P \times_{S} E$ will be a prescheme over $T = E^{P}$, with right operator group
$G_{T} = G \times_{S} T$; one would like, for comfort, $P \times_{S} E$ to be a principal homogeneous bundle over $T$
with group `G_T`.

To verify the existence of $E^{P}$ and the preceding property, take the $S'$ from Definition XI.4.1 and look at the
inverse-image situation over $S'$. Since $P'$ is trivial, that is, isomorphic to $G'_{d}$, one sees at once that
$E'^{P'}$ exists and has the desired exactness property. In fact, $E' \times_{S}' P'$ is $G'$-isomorphic to the product
$E' \times_{S}' G'$, and therefore $E'^{P'}$ is isomorphic to $E'$. Moreover, the formation of the “associated bundle”
in the case of a trivial operator space commutes with every base extension. Taking here the various base extensions
`S″ ⇉ S′` and `S‴ ⇉⇉ S′`, where $S''$ and $S'''$ are the double and triple fiber products of $S'$ over $S$, one sees
that $E'^{P'}$ **is endowed with a descent datum relative to $S' \to S$, and $E^{P}$ exists with the required properties
if and only if this descent datum is effective**. Of course $E^{P}$ is then precisely the descended object. Use here the
fact that $S' \to S$ is a descent morphism in the category of $S$-preschemes; cf. VIII.5.2. It follows that **the
associated bundle exists if $E$ is affine over $S$**.

We shall apply this construction in the case where one has a homomorphism of $S$-groups $G \to H$, and where $E$ is the
$S$-prescheme $H$ endowed with the left actions of $G$ on $H$ arising from the given morphism. Since $H$ acts on itself
on the right in a way that commutes with the actions of $G$ on $H$, and since (subject to existence over $S$) the
formation of the associated bundle commutes with base extension, one easily sees that $H$ acts on the right on $P^{H}$.
Thus $P^{H}$ is a principal homogeneous bundle under $H$ in the sense of XI.4.1, and

<!-- original page 296 -->

more precisely it is trivialized by the same morphism $S' \to S$ as $P$. In particular, **to every principal homogeneous
bundle $P$ under $G$ and every homomorphism of $S$-groups $G \to H$, with $H$ affine over $S$, there is associated a
principal homogeneous bundle with group $H$**, functorially in $(G \to H)$, and compatibly with arbitrary base changes
$T \to S$.

**Definition.**

<!-- label: XI.4.4 -->

Let $G$ be an $S$-prescheme. We write $H^{0}(S,G)$ for the set of sections of $G$ over $S$, considered as a group when $G$
is an $S$-group. In that case, we write $H^{1}(S,G)$ for the set of isomorphism classes of principal homogeneous bundles
over $S$ with group $G$, regarding $H^{1}(S,G)$ as endowed with the “marked point” corresponding to the trivial bundles.
\[Translator note: the source footnote says this notation is consistent with the general cohomological notation (SGA 4
V) only when one has effectivity criteria for descent, which are scarcely ensured except when $G$ is affine, or merely
quasi-affine; cf. VIII.7.9.\]

Thus $H^{0}(S,G)$ is a functor in the $S$-prescheme $G$, with values in sets. This functor is left exact, and a fortiori
commutes with finite products; indeed this implies that it sends groups to groups and commutative groups to commutative
groups. Similarly, $H^{1}(S,G)$ is a functor in the **affine** $S$-group $G$, with values in sets, by formation of
associated bundles; one checks easily that this functor commutes with finite products. In particular it sends groups in
the category of affine $S$-groups, that is, **commutative affine** $S$-groups, to groups, and indeed to commutative
groups. Thus, **if $G$ is a commutative affine $S$-group, $H^{1}(S,G)$ is a commutative group**, and a homomorphism
$G \to H$ of commutative affine $S$-groups gives rise to a group homomorphism $H^{1}(S,G) \to H^{1}(S,H)$.

For simplicity, from now on we restrict to **affine and commutative** $S$-groups. Let

$$
0 \to G' \to G \to G'' \to 0
$$

be a sequence of morphisms of such groups. **We say that this sequence is exact if the composite $G' \to G \to G''$ is
zero** (which allows $G$ to be regarded as a prescheme over $G''$ with right operator group ${G'_{G}}''$)

<!-- original page 297 -->

**and if $G$ is a principal homogeneous bundle over $G''$ with group ${G'_{G}}'' = G' \times_{S} G''$**. This implies in
particular that $u: G' \to G$ is a kernel of $v: G \to G''$, and a fortiori it implies exactness of

$$
0 \to H^{0}(S,G') \to H^{0}(S,G) \to H^{0}(S,G'').
$$

It also makes it possible to define a map

$$
\partial: H^{0}(S,G'') \to H^{1}(S,G'),
$$

by associating to every section of $G''$ over $S$, that is, to every $S$-morphism $f: S \to G''$, the principal
homogeneous bundle $P_{f}$ with group $G' \simeq f*({G'_{G}}'')$ over $S$, inverse image of the principal homogeneous
bundle $G$ over $G''$. From the viewpoint of $S$-preschemes, this is simply the inverse image by $v: G \to G''$ of the
subprescheme image of $S$ by the immersion $f$; the operations of $G'$ on $P_{f}$ are induced by the right operations of
$G'$ on $G$.

We also leave to the reader the verification of the following proposition, which presents no difficulties other than
those of writing it out:

**Proposition.**

<!-- label: XI.4.5 -->

The map $\partial: H^{0}(S,G'') \to H^{1}(S,G')$ is a group homomorphism. The following sequence of homomorphisms is
exact:

```text
0 → H⁰(S,G′) → H⁰(S,G) → H⁰(S,G″) → H¹(S,G′) → H¹(S,G) → H¹(S,G″),
```

where all homomorphisms other than $\partial$ come from the functoriality of $H^{0}$, respectively $H^{1}$.

**Remarks.**

<!-- label: XI.4.6 -->

The point of view set out here for the study of principal homogeneous bundles is visibly inspired by Serre [XI.7], which
the reader would do well to consult. When one wants a formalism that also applies to structural $S$-groups
quasi-projective over $S$, in order to include projective abelian schemes in particular, it is useful to modify XI.4.1
by requiring $S'$ to be a sum of preschemes $S'_{i}$ finite and locally free over open subsets $S_{i}$ covering $S$. The
preceding developments are then valid, including in particular XI.4.5, after replacing the affine hypothesis everywhere
by the quasi-projective hypothesis, and interpreting accordingly the definition given above of an exact sequence of
$S$-groups. It is enough to replace the reference to VIII.2.1

<!-- original page 298 -->

by VIII.7.7: the morphisms $S' \to S$ used are morphisms of effective descent for the fibered category of preschemes
quasi-projective over other preschemes. Be careful, however, that this second notion of principal homogeneous bundle is
more restrictive than the first, XI.4.1.

### 4.7.

<!-- label: XI.4.7 -->

One obtains an even more restrictive notion of principal homogeneous bundle by requiring $S$ to be covered by open
subsets $S_{i}$ such that for every $i$, $P|S_{i}$ is a trivial operator bundle under $G|S_{i}$; in this case one says
that $P$ is a **locally trivial** principal homogeneous bundle. The classes of these bundles, for fixed $G$, form a
subset of $H^{1}(X,G)$, in one-to-one correspondence with $H^{1}(X,\mathcal{O}_{X}(G))$, where $\mathcal{O}_{X}(G)$ is
the ordinary sheaf of sections of $G$ over $S$; cf. [XI.2]. For these $H^{1}$ to again give rise to a cohomology exact
sequence XI.4.5, one must plainly assume that the sequence $0 \to G' \to G \to G'' \to 0$ is exact in the reasonable
sense for this new context, that is, that $G$ is a locally trivial bundle over $G''$ with group ${G'_{G}}''$. This also
means that $u: G' \to G$ is a kernel of $v: G \to G''$, and that $G$ admits local sections over $G''$.

### 4.8.

<!-- label: XI.4.8 -->

It is plainly very desirable to continue the exact sequence XI.4.5 by introducing the higher cohomology groups
$H^{i}(X,G)$. This is possible in the framework of “Weil cohomology”: one considers the category $\mathcal{B}$ of
quasi-compact preschemes over $S$, endowed with the class $\mathcal{M}$ of faithfully flat and quasi-compact morphisms,
called localizing morphisms. An abelian “Weil sheaf” on $S$, or better, on $(\mathcal{B},\mathcal{M})$, is a
contravariant functor $\mathcal{F}$ from $\mathcal{B}$ to abelian groups, sending sums to products and every sequence
`T″ = T′ ×_T T′ ⇉ T′ → T`, with $T' \to T$ in $\mathcal{M}$, to an **exact** diagram of sets

```text
𝓕(T) → 𝓕(T′) ⇉ 𝓕(T″).
```

The Weil sheaves form an abelian category with exact filtered colimits and a generator, hence with enough injective
objects [XI.1]. The right derived functors of $\Gamma(\mathcal{F}) = \mathcal{F}(S)$ are denoted $H^{i}(S,\mathcal{F})$.
On the other hand, every commutative $S$-group plainly defines a Weil sheaf (VIII.5.2), whose $H^{0}$ and $H^{1}$ are
just $H^{0}(S,G)$ and $H^{1}(S,G)$. This gives a reasonable definition of the other $H^{i}(S,G)$.

<!-- original page 299 -->

Moreover, one shows that an exact sequence of $S$-groups defines an exact sequence of Weil sheaves, allowing one to
recover and extend the exact sequence XI.4.5. \[Translator note: the source footnote refers, for a systematic study of
this point of view, to SGA 4 I-IX.\]

### 4.9.

<!-- label: XI.4.9 -->

It would be appropriate to develop the noncommutative variants of XI.4.5 as in [XI.2]. For a systematic development, in
the proper framework, of the various cohomological notions sketched in the present number, we refer to work in
preparation by J. Giraud. \[Translator note: the corrected source identifies this as J. Giraud, *Cohomologie non
ab\acute{e}lienne*, Springer-Verlag, 1971.\]

## 5. Special Cases of Principal Bundles

<!-- label: XI.5 -->

Suppose now that $S$ is connected and endowed with a geometric point $a$, hence with a fundamental group $\pi_{1}(S,a)$
classifying the étale coverings of $S$: the category of étale coverings of $S$ is equivalent to the category of finite
sets on which $\pi_{1}$ acts continuously. It follows that a finite étale group scheme $G$ over $S$ is determined,
essentially, by an ordinary finite group $\mathcal{G}$ on which $\pi_{1}$ acts continuously by group automorphisms. An
étale covering $P$ of $S$ on which $G$ acts on the right is determined, essentially, by a finite set $\mathcal{P}$ on
which $\pi_{1}$ acts continuously on the left, and on which $\mathcal{G}$ acts on the right in a way compatible with the
operations of $\pi_{1}$:

```text
s(p · g) = (sp) · (sg),     for s ∈ π₁, p ∈ 𝒫, g ∈ 𝒢.
```

One verifies that $P$ is a principal homogeneous bundle in the sense of XI.4.1 if and only if $\mathcal{P}$ is a
principal homogeneous set under $\mathcal{G}$; for example, use the criterion XI.4.2. In other words, **the category of
principal homogeneous bundles over $S$ with group $G$ is equivalent to the category of principal homogeneous bundles
with group $G$ in the category of finite sets on which $\pi_{1}$ acts continuously**. In particular one deduces a
canonical bijection, functorial in $G$:

<!-- label: eq:XI.5.etoile -->

$$
(*)   H^{1}(S,G) \simeq H^{1}(\pi_{1},\mathcal{G}),
$$

where

<!-- original page 300 -->

the second member denotes the set of classes, up to isomorphism, of principal homogeneous bundles under $\mathcal{G}$ in
the category of finite sets on which $\pi_{1}$ acts; it is in fact needless to specify “continuously.” This set is made
explicit in the familiar way as the quotient of the set $Z^{1}(\pi_{1},G)$ of 1-cocycles
$\phi: \pi_{1} \to \mathcal{G}$, satisfying

```text
φ(1) = 1,     φ(st) = φ(s)(s · φ(t)),
```

by the natural action of the group $\mathcal{G}$.

<!-- label: page-300 -->

An important case is the one where $\pi_{1}$ acts trivially on $\mathcal{G}$, that is, where $G$ is a completely
decomposed covering of $S$, isomorphic to the sum of $\mathcal{G}$ copies of $S$. One then also writes
$H^{1}(S,\mathcal{G})$ instead of $H^{1}(S,G)$, and this set is in one-to-one correspondence, by (\*), with
$H^{1}(\pi_{1},\mathcal{G}) = \operatorname{Hom}(\pi_{1},\mathcal{G})$ modulo inner automorphisms of $\mathcal{G}$.
Notice, moreover, that in this case a principal homogeneous bundle over $S$ with group $G$ is nothing other than a
**principal covering** of $S$ with group $\mathcal{G}$ (V.2.7), and the preceding one-to-one correspondence is the one
deduced from the correspondence between principal coverings of $S$ with group $\mathcal{G}$, **pointed** above $a$, and
continuous homomorphisms from $\pi_{1}(S,a)$ to $\mathcal{G}$ (V, end of no. V.5).

The interest of relating the theory of étale coverings with that of principal bundles, already implicit in A. Weil,
_Généralisation des Fonctions Abéliennes_, and made explicit by S. Lang in his geometric theory of class fields, cf.
Serre [XI.5], comes from the following fact. Every $S$-group that is finite and étale over $S$ can be embedded in an
$S$-group $H$, affine and smooth over $S$, with connected fibers, and commutative when $G$ is. Therefore, by the exact
sequence XI.4.5, and possibly its noncommutative variants, the “discrete” classification of principal coverings with
group $G$ can be studied by means of the “continuous” classification of principal bundles with group $H$, and conversely
as well. For the idea of the general construction of the immersion of $G$ into $H$, apparently rather little used in
practice, see [XI.5, VI 2.8]. We shall content ourselves in the following number with developing two important special
cases, classical ones at that. We shall need the following auxiliary result.

**Proposition.**

<!-- label: XI.5.1 -->

Let

<!-- original page 301 -->

$S$ be a prescheme, and let $G$ be an $S$-group isomorphic to $GL(n)_{S}$, for example $\mathbb{G}_{m},S$, or to
$\mathbb{G}_{a},S$. Then every principal homogeneous bundle under $G$ is locally trivial.

Here $GL(n)_{S}$, for an integer $n \geq 0$, denotes the $S$-group representing the contravariant functor

$$
T \mapsto GL(n, \Gamma(T,\mathcal{O}_{T}))
$$

on the $S$-prescheme $T$. In particular $\mathbb{G}_{m},S$, the “multiplicative group over $S$,” represents the
contravariant functor

$$
T \mapsto \Gamma(T,\mathcal{O}^{*}_{T}),
$$

and therefore, as a prescheme over $S$, is isomorphic to $\operatorname{Spec} \mathcal{O}_{S}[t,t^{-1}]$, where $t$ is
an indeterminate. Similarly $\mathbb{G}_{a},S$ represents the contravariant functor

$$
T \mapsto \Gamma(T,\mathcal{O}_{T}),
$$

and hence is isomorphic as an $S$-prescheme to $\operatorname{Spec}(\mathcal{O}_{S}[t])$, where $t$ is an indeterminate.
Notice that, by dévissage, XI.5.1 recovers Rosenlicht’s local-triviality result for the case where $G$ admits a
“composition series” whose successive factors are groups of the type considered here. For a finer study of questions of
local triviality of principal homogeneous bundles, cf. [XI.7] and [XI.3].

The first assertion is proved by observing that $G(T) = \operatorname{Aut}(\mathcal{O}^{n}_{T})$, and that the morphisms
$S' \to S$ occurring in XI.4.1, that is, those which are faithfully flat and quasi-compact, are morphisms of effective
descent for the fibered category of modules locally isomorphic to $\mathcal{O}^{n}_{T}$, that is, locally free of rank
$n$ (VIII.1.12). The second is proved in an analogous way, noting that in this case
$G(T) = \operatorname{Aut}(\mathcal{E}_{T})$, where $\mathcal{E}_{T}$ is the trivial **extension** of $\mathcal{O}_{T}$
by $\mathcal{O}_{T}$, and where the automorphisms must of course respect the extension structure. The morphisms
$S' \to S$ occurring in XI.4.1 are morphisms of effective descent for the fibered category of extensions of
$\mathcal{O}_{T}$ by $\mathcal{O}_{T}$, as follows easily from VIII.1.1, and such extensions are automatically locally
trivial.

**Remark.**

<!-- label: XI.5.2 -->

Notice that the same type of proof applies to the symplectic group $Symp(2n)_{S}$, since an alternating form on a module
locally isomorphic to $\mathcal{O}^{2n}_{S}$, which is “nondegenerate,” that is, defines an isomorphism from this module
to its dual, is locally isomorphic to the standard form. The corresponding result for the orthogonal group is false,
however, already when $S$ is the spectrum of a field, since there may be quadratic forms over a field that are not
isomorphic to the standard form.

<!-- original page 302 -->

Moreover, it is shown essentially in [XI.3] that the groups `GL`, `Symp`, $\mathbb{G}_{a}$, and those which can be
dévissés into such groups, are, up to small qualifications, the only ones for which one has a local-triviality result of
the type considered here.

**Corollary.**

<!-- label: XI.5.3 -->

There are canonical bijections

$$
H^{1}(S,GL(n)_{S}) \simeq H^{1}(S,GL(n,\mathcal{O}_{S})),
$$

in particular

$$
H^{1}(S,\mathbb{G}_{m},S) \simeq H^{1}(S,\mathcal{O}^{*}_{S}),
$$

and

$$
H^{1}(S,\mathbb{G}_{a},S) \simeq H^{1}(S,\mathcal{O}_{S}),
$$

where the second members denote cohomology groups of the topological space $S$ with coefficients in ordinary sheaves.

In particular, $H^{1}(S,GL(n)_{S})$ identifies with the set of isomorphism classes of modules locally free of rank $n$
on $S$, and $H^{1}(S,\mathbb{G}_{a},S)$ identifies with the set of classes of extensions of the module $\mathcal{O}_{S}$
by itself.

## 6. Application to Principal Coverings: Kummer and Artin-Schreier Theories

<!-- label: XI.6 -->

**Proposition.**

<!-- label: XI.6.1 -->

Let $S$ be a prescheme, let $n$ be an integer `> 0`, let

$$
u_{n}: \mathbb{G}_{m},S \to \mathbb{G}_{m},S
$$

be the $n$-th power homomorphism, and let $\mu_{n},S$ be its kernel. Then $\mu_{n},S$ is finite and locally free of rank
$n$ over $S$, and it is étale over $S$ if and only if for every $s \in S$, the characteristic of $s$ is prime to $n$.
The sequence of homomorphisms

```text
0 → μ_n,S → 𝔾_m,S --u_n→ 𝔾_m,S → 0
```

is exact in the sense of no. XI.4. It will be called the **Kummer exact sequence** over $S$, relative to the integer
$n$.

One has

<!-- original page 303 -->

$$
\mathbb{G}_{m} = \operatorname{Spec} \mathcal{O}_{S}[t,t^{-1}],
$$

and $u_{n}$ corresponds to the homomorphism $u_{n}$ on affine $\mathcal{O}_{S}$-algebras given by

$$
u_{n}(t) = t^{n}.
$$

On the other hand, the unit section of $\mathbb{G}_{m},S$ corresponds to the augmentation homomorphism of
$\mathcal{O}_{S}$-algebras given by

$$
\epsilon(t) = 1,
$$

whose kernel is therefore the principal ideal $(t - 1)$. The image of this ideal by $u_{n}$ is thus the principal ideal
$(1 - t^{n})$, and one finds

```text
μ_n,S = Spec 𝒪_S[t]/(1 − tⁿ).
```

This shows in particular that $\mu_{n},S$ is finite over $S$, and is defined by an algebra over $S$ that is free of rank
$n$, with basis formed by the $t^{i}$ for $0 \leq i \leq n - 1$. For it to be étale at $s \in S$, it is necessary and sufficient
that the reduced algebra $k[t]/(1 - t^{n})$, where $k = \kappa(s)$, obtained by formally adjoining the $n$-th roots of unity to
$k$, be separable over $k$; that is, that the roots of $1 - t^{n}$ in an algebraic closure of $k$ all be distinct. This is
equivalent to $n$ being prime to the characteristic. Finally, to show that the sequence of homomorphisms in XI.6.1 is
exact, the criterion XI.4.2 reduces us to proving that $u_{n}$ is faithfully flat. \[Translator note: the corrected source
replaces an erroneous “v” here by $u_{n}$.\] We may plainly suppose that $S$ is affine with ring $A$, hence that $\mathbb{G}_{m},S$
is affine with ring $B = A[t,t^{-1}]$. It is enough to verify that $u_{n}$ makes $B$ a free module of rank $n$ over $B$;
equivalently, that $u_{n}$ is injective and that $A[t,t^{-1}]$ is a free module of rank $n$ over $A[t^{n},t^{-n}]$. Indeed, one
checks easily that the $t^{i}$ for $0 \leq i \leq n - 1$ form a basis of the former over the latter, which completes the proof.

**Definition.**

<!-- label: XI.6.2 -->

<!-- original page 304 -->

The group $\mu_{n},S$ is called the **Kummer group of rank $n$ over $S$**, and a **Kummer principal covering of rank $n$
over $S$** is a principal homogeneous bundle over $S$ whose group is the Kummer group of rank $n$. \[Translator note:
the corrected source reads “rank $n$ over $S$,” correcting the old text’s malformed “n S.”\]

The set of these coverings is a group, denoted $H^{1}(S,\mu_{n},S)$, or simply $H^{1}(S,\mu_{n})$. Notice that the
formation of the Kummer group of rank $n$ over $S$ is compatible with extension of the base, so that $\mu_{n},S$ comes
by base extension from the **absolute Kummer group $\mu_{n}$** over $\operatorname{Spec}(\mathbb{Z})$.

Let $(\mathbb{Z}/n\mathbb{Z})_{S}$ denote the $S$-group defined by the ordinary finite group $\mathbb{Z}/n\mathbb{Z}$.
If $G$ is any $S$-group, the homomorphisms of $S$-groups $u$ from $(\mathbb{Z}/n\mathbb{Z})_{S}$ to $G$ are in
one-to-one correspondence, compatibly with base change, with the sections of $G$ over $S$ whose $n$-th power is the unit
section: to $u$ one associates the image by $u$ of the section of $(\mathbb{Z}/n\mathbb{Z})_{S}$ over $S$ defined by the
generator $1 mod n\mathbb{Z}$ of $\mathbb{Z}/n\mathbb{Z}$. With this understood:

**Corollary.**

<!-- label: XI.6.3 -->

If $\mu_{n},S$ is étale over $S$, one thereby obtains a one-to-one correspondence between isomorphisms of $S$-groups

$$
(\mathbb{Z}/n\mathbb{Z})_{S} \simeq \mu_{n},S
$$

and sections of $\mathcal{O}_{S}$ that are of exact order $n$ on each connected component of $S$; such a section will be
called a “primitive $n$-th root of unity over $S$.” Therefore, for $\mu_{n},S$ to be isomorphic as an $S$-group to
$(\mathbb{Z}/n\mathbb{Z})_{S}$, it is necessary and sufficient that it be étale over $S$, that is, that the residual
characteristics of $S$ be prime to $n$, and that there exist a primitive $n$-th root of unity over $S$.

This explains the role played in classical Kummer theory by the hypothesis that the base field, playing the role of $S$,
have characteristic prime to $n$ and contain the $n$-th roots of unity, and by the choice of a primitive $n$-th root of
unity. Once the language of schemes is available, there is no longer any reason to burden oneself with these hypotheses;
one should reason directly with $\mu_{n}$ instead of $\mathbb{Z}/n\mathbb{Z}$. Thus the conjunction of XI.6.1, XI.4.5,
and XI.5.3 gives the following general relation between the theory of Kummer principal coverings and that of Picard
groups.

**Proposition.**

<!-- label: XI.6.4 -->

Let

<!-- original page 305 -->

$S$ be a prescheme. There is a canonical exact sequence

```text
0 → H⁰(S,μ_n) → H⁰(S,𝒪_S^*) → H⁰(S,𝒪_S^*) → H¹(S,μ_n)
  → H¹(S,𝒪_S^*) → H¹(S,𝒪_S^*),
```

hence, putting $H^{1}(S,\mathcal{O}^{*}_{S}) = \operatorname{Pic}(S)$, and denoting for every abelian group $A$ by
${}_{nA}$ and $A_{n}$ the kernel and cokernel of multiplication by $n$ in $A$, the exact sequence

$$
0 \to H^{0}(S,\mathcal{O}_{S})^{*}_{n} \to H^{1}(S,\mu_{n}) \to {}_{nPic}(S) \to 0.
$$

\[Translator note: the corrected source fixes the definition of $\operatorname{Pic}(S)$ here from $H^{1}(S,\mathcal{O}_{S})$ to $H^{1}(S,\mathcal{O}^{*}_{S})$.\]

We shall spell out two important cases, where one or the other extreme term of this exact sequence is zero.

**Corollary.**

<!-- label: XI.6.5 -->

Suppose ${}_{nPic}(S) = 0$, for example that $S$ is the spectrum of a local ring or of a factorial ring, and let $A$ be
the ring $H^{0}(S,\mathcal{O}_{S})$. Then there is a canonical isomorphism

$$
H^{1}(S,\mu_{n}) \simeq A^{*}/(A^{*})^{n}.
$$

This is essentially the classical statement of Kummer theory when $S$ is the spectrum of a field.

**Corollary.**

<!-- label: XI.6.6 -->

Suppose that every element of $H^{0}(S,\mathcal{O}_{S})$ is an $n$-th power, for example that $H^{0}(S,\mathcal{O}_{S})$
is a composite of algebraically closed fields, or that $S$ is reduced and proper over an algebraically closed field $k$.
Then there is a canonical isomorphism

$$
H^{1}(S,\mu_{n}) \simeq {}_{nPic}(S).
$$

In particular, when $S$ is proper and connected over an algebraically closed field $k$, this relates the fundamental
group of $S$ with the points of finite order of the Picard scheme $P$ of $S$ over $k$. Thus one has an isomorphism

$$
\operatorname{Hom}(\pi_{1}(S),\mathbb{Z}/n\mathbb{Z}) \simeq {}_{nP}(k)
$$

for $n$ prime to the characteristic, a relation often used in algebraic

<!-- original page 306 -->

geometry. As an application, when the connected component $P^{0}$ of $P$ is a complete group scheme of dimension $g$,
one sees, using the results recalled in no. XI.2 and the finiteness of the Néron-Severi torsion group, that for every
prime number $\ell$ prime to the characteristic, the $\ell$-primary component of the abelianized fundamental group
$\pi_{1}(S)$ is a module of finite type and rank `2g` over the ring $\mathbb{Z}_{\ell}$ of $\ell$-adic integers; indeed
it is free except for at most finitely many values of $\ell$. As Serre observed, this allows one to prove under certain
conditions that when $X$ is a flat and projective scheme over connected $S$, the Picard schemes of the fibers of $X$ all
have the same dimension, by applying the semicontinuity theorem (X.2.3). Serre’s argument applies as soon as the Picard
scheme of $X$ over $S$ exists and the connected Picards of the fibers of $X$ over $S$ are proper group schemes; for
example when the geometric fibers of $X$ over $S$ are normal, with $X$ still flat and projective over $S$, and in
particular if $X$ is smooth and projective over $S$.

Now let $p$ be a prime number, and suppose that $S$ is a prescheme of characteristic $p$, that is,
$p \cdot \mathcal{O}_{S} = 0$. Then the $p$-th power homomorphism in $\mathcal{O}_{S}$ is additive, and the
corresponding morphism, obtained by replacing $S$ by a variable $T$ over $S$,

$$
F: \mathbb{G}_{a},S \to \mathbb{G}_{a},S
$$

is therefore a homomorphism of $S$-groups, called the **Frobenius homomorphism**. Note that such a morphism is defined
for every $S$-prescheme $G$ which comes by base extension from a prescheme $G_{0}$ over the prime field
$\mathbb{Z}/p\mathbb{Z}$, and that this morphism is a group homomorphism if $G_{0}$ is a group prescheme. We put

```text
wp = id − F: 𝔾_a,S → 𝔾_a,S.
```

On the other hand, consider the $S$-group $(\mathbb{Z}/p\mathbb{Z})_{S}$ defined by the ordinary finite group
$\mathbb{Z}/p\mathbb{Z}$. We said that for every $S$-group $G$, the homomorphisms of $S$-groups from
$(\mathbb{Z}/p\mathbb{Z})_{S}$ to $G$ are in one-to-one correspondence with the sections of $G$ over $S$ whose $p$-th
power is the unit section. When $G = \mathbb{G}_{a},S$, they therefore correspond

<!-- original page 307 -->

to arbitrary sections of $G$ over $S$. Taking in particular the section of $\mathbb{G}_{a},S$ over $S$ corresponding to
the unit section of the sheaf of rings $\mathcal{O}_{S}$, one obtains a homomorphism of $S$-groups

$$
i: (\mathbb{Z}/p\mathbb{Z})_{S} \to \mathbb{G}_{a},S.
$$

**Proposition.**

<!-- label: XI.6.7 -->

The sequence of homomorphisms of $S$-groups

$$
0 \to (\mathbb{Z}/p\mathbb{Z})_{S} \to \mathbb{G}_{a},S \to \mathbb{G}_{a},S \to 0
$$

is exact in the sense of no. XI.4. It is called the **Artin-Schreier exact sequence** over $S$. \[Translator note: the
corrected source fixes the last group symbol in the displayed sequence.\]

It is enough to prove this over the prime field $k = \mathbb{Z}/p\mathbb{Z}$. It is enough to observe that the
homomorphism $wp*: k[t] \to k[t]$ defined by $wp*(t) = t - t^{p}$ makes `k[t]` a free module of rank $p$ over `k[t]`;
more precisely, `k[t]` is a free module over `k[s]`, where $s = t - t^{p}$, with basis formed by the $t^{i}$ for
$0 \leq i \leq p - 1$.

Using XI.4.5 and XI.5.3, we conclude:

**Proposition.**

<!-- label: XI.6.8 -->

There is a canonical exact sequence

```text
0 → H⁰(S,ℤ/pℤ) → H⁰(S,𝒪_S) → H⁰(S,𝒪_S) → H¹(S,ℤ/pℤ)
  → H¹(S,𝒪_S) → H¹(S,𝒪_S),
```

hence an exact sequence

```text
0 → H⁰(S,𝒪_S)/wp H⁰(S,𝒪_S) → H¹(S,ℤ/pℤ) → H¹(S,𝒪_S)^F → 0,
```

where the exponent $F$ in the last term denotes the subgroup of invariants under the endomorphism $F$, equal to the
kernel of $wp = id - F$.

Let us spell out two extreme cases:

**Corollary.**

<!-- label: XI.6.9 -->

Suppose $H^{1}(S,\mathcal{O}_{S})^{F} = 0$, for example that $S$ is an affine scheme. Then, putting
$A = H^{0}(S,\mathcal{O}_{S})$, there is a canonical isomorphism

$$
H^{1}(S,\mathbb{Z}/p\mathbb{Z}) \simeq A/wp A.
$$

This is **Artin-Schreier theory** in its classical form, at least when $A$ is the spectrum of a field. \[Translator
note: the source says “when $A$ is the spectrum of a field”; mathematically one expects “when $S$ is the spectrum of a
field,” or “when $A$ is a field.”\]

**Corollary.**

<!-- label: XI.6.10 -->

Suppose

<!-- original page 308 -->

$wp H^{0}(S,\mathcal{O}_{S}) = H^{0}(S,\mathcal{O}_{S})$, for example that $H^{0}(S,\mathcal{O}_{S})$ is a composite of
algebraically closed fields, or that $S$ is proper over an algebraically closed field. Then there is a canonical
isomorphism

$$
H^{1}(S,\mathbb{Z}/p\mathbb{Z}) \simeq H^{1}(S,\mathcal{O}_{S})^{F}.
$$

**Remarks.**

<!-- label: XI.6.11 -->

The last statement is due to J.-P. Serre [XI.9]. It is also possible to develop an analogous theory for the structural
group $\mathbb{Z}/p^{n}\mathbb{Z}$ for arbitrary $n$, using in place of $\mathbb{G}_{a}$ the Witt group scheme $W_{n}$; cf. loc. cit. Notice that in
characteristic $p > 0$, Kummer theory no longer gives information on principal coverings of order $p$, since $\mu_{p}$ is
then an “infinitesimal” group, that is, radicial over the base, and hence has no direct relation with $\mathbb{Z}/p\mathbb{Z}$. Thus at
first sight, the theory of these coverings no longer falls, when $S$ is a proper scheme over an algebraically closed
field for definiteness, under the theory of the Picard scheme as in XI.6.6. Nevertheless, if one recalls that the
Zariski tangent space at the origin in $\operatorname{Pic}_{S}/K$ \[Translator note: the source footnote refers for the definition of
$\operatorname{Pic}_{S}/K$ to A. Grothendieck, Séminaire Bourbaki no. 232, February 1962.\] identifies with $H^{1}(S,\mathcal{O}_{S})$, one sees that
**knowledge of the group scheme `_pPic_S/k`, the kernel of multiplication by $p$ in $\operatorname{Pic}_{S}/k$, implies knowledge of
$H^{1}(S,\mathbb{Z}/p\mathbb{Z})$ as well as of $H^{1}(S,\mu_{p})$; notice that it also implies knowledge of $H^{1}(S,\alpha_{p})$**, where $\alpha_{p}$ denotes the
infinitesimal group scheme over the prime field, the kernel of $F: \mathbb{G}_{a} \to \mathbb{G}_{a}$, which can also be described as the
spectrum of the restricted enveloping algebra of the trivial one-dimensional $p$-Lie algebra. Indeed, the exact sequence
XI.4.5 gives here

```text
H¹(S,α_p) ≃ Ker(F: H¹(S,𝒪_S) → H¹(S,𝒪_S)),
```

and more generally, denoting by $\alpha^{n}_{p}$ the kernel in $\mathbb{G}_{a}$ of the $n$-th iterate of $F$, one has

```text
H¹(S,α_pⁿ) ≃ Ker(Fⁿ: H¹(S,𝒪_S) → H¹(S,𝒪_S)).
```

In fact, knowledge of `_pPic_S/k` is equivalent to knowledge of $H^{1}(S,G)$ for every finite commutative algebraic

<!-- original page 309 -->

group annihilated by $p$; more generally, knowledge of ${}^{n}_{p}\operatorname{Pic}_{S}/k$ is equivalent to knowledge
of $H^{1}(S,G)$ for every finite commutative algebraic group $G$ annihilated by $p^{n}$, by virtue of the following
theorem, which in the case under consideration includes both Kummer theory and Artin-Schreier theory:

Let $G$ be a finite algebraic group over $k$, and let $D(G) = SheafHom_{k}-groups(G,\mathbb{G}_{m})$ be its **Cartier
dual**; the affine algebra of $D(G)$ is carried by the vector space dual to the affine algebra of $G$, that is, by the
hyperalgebra of $G$ in the sense of Dieudonné-Cartier. Then there is a canonical isomorphism:

<!-- label: eqXI.6.11 -->

```text
(*)   H¹(S,G) ≃ Hom_k-groups(D(G),Pic_S/k).
```

Here $S$ is a proper scheme over algebraically closed $k$ such that $H^{0}(S,\mathcal{O}_{S}) = k$. This formula may
also be expressed by saying that the “true fundamental group” of $S$ alluded to in no. XI.2, after abelianization, is
isomorphic to the projective limit of the $D(P_{i})$, where $P_{i}$ ranges over the **finite** algebraic subgroups of
$\operatorname{Pic}_{S}/k$; we shall denote it by $T\bullet(\operatorname{Pic}_{X}/k)$. When $S$ is an abelian variety,
we saw in XI.2.1 that this group is also isomorphic to the “true” Tate module $T_{\bullet}(S) = \lim {}_{nS}$, and the
isomorphism (\*) is then written in the more striking form

$$
Ext^{1}(A,G) \simeq \operatorname{Hom}(D(G),B),
$$

where $A$ is an abelian variety, $B$ its dual, and $G$ a finite algebraic group over $k$. The results just indicated can
moreover be generalized to the case where $k$ is replaced by an arbitrary base prescheme, and to coefficient groups $G$
other than finite groups.

## Bibliography

<!-- original page 310 -->

1. A. Grothendieck, “Sur quelques points d’algèbre homologique,” Tôhoku Math. J. 9 (1957), pp. 119-221.
1. A. Grothendieck, “A general theory of fibre spaces with structure sheaf,” University of Kansas, 1955.
1. A. Grothendieck, “Torsion homologique et sections rationnelles,” Séminaire Chevalley, 16 June 1958.
1. S. Lang, _Abelian Varieties_, Interscience Tracts in Pure and Applied Mathematics, no. 7, New York.
1. J.-P. Serre, _Groupes algébriques et corps de classes_, Actualités Scientifiques et Industrielles no. 1264, Hermann,
   Paris, 1959.
1. J.-P. Serre, “Groupes proalgébriques,” Publications Mathématiques de l’IHÉS 7 (1960), pp. 1-67.
1. J.-P. Serre, “Espaces fibrés algébriques,” Séminaire Chevalley, 21 April 1958.
1. J.-P. Serre, “Quelques propriétés des variétés abéliennes en caractéristique p,” Amer. J. Math. 80 (1958), pp.
   715-739.
1. J.-P. Serre, “Sur la topologie des variétés algébriques en caractéristique p,” Symposium Internacional de Topologia
   Algebraica, 1958.
1. J.-P. Serre, “On the fundamental group of a unirational variety,” J. London Math. Soc. 34 (1959), pp. 481-484.


<!-- SOURCE: 12-geometrie-algebrique-et-geometrie-analytique.md -->

# Exposé XII. Algebraic Geometry and Analytic Geometry

<!-- label: XII -->

<!-- original page 311 -->

Mme M. Raynaud. [Translator note: according to unpublished notes of A. Grothendieck.]

Proceeding as in [XII.10], one associates to every scheme $X$ locally of finite type over the field of complex numbers
$\mathbb{C}$ an analytic space $X^{an}$, whose underlying set is $X(\mathbb{C})$.

<!-- label: indnot:lb -->

In nos. XII.2 and XII.3 of this exposé, we give a “dictionary” between the usual properties of $X$ and of $X^{an}$, and
between the properties of a morphism $f: X \to Y$ and of the associated morphism $f^{an}: X^{an} \to Y^{an}$.

<!-- label: indnot:lc -->

We then show that the comparison theorems between coherent sheaves on $X$ and $X^{an}$, established in [XII.10, no. 12]
for a projective variety, are still valid when $X$ is a proper scheme.

Finally, in no. XII.5 we prove the equivalence between the category of finite étale coverings of $X$ and the category of
finite étale coverings of $X^{an}$. As a bonus for the reader, we give a new proof of the Grauert-Remmert theorem
[XII.6], using resolution of singularities [XII.8].

## 1. The Analytic Space Associated with a Scheme

<!-- label: XII.1 -->

<!-- original page 312 -->

Let $X$ be a scheme locally of finite type over $\mathbb{C}$. Let $\Phi$ be the functor from the category of analytic
spaces \[XII.4, no. 9\] to the category of sets which associates to an analytic space $\mathcal{X}$ the set of morphisms
of ringed spaces in $\mathbb{C}$-algebras $\operatorname{Hom}_{\mathbb{C}}(\mathcal{X},X)$. One has the following
theorem:

**Theorem-Definition.**

<!-- label: XII.1.1 -->

The functor $\Phi$ is representable by an analytic space $X^{an}$ and a morphism $\phi: X^{an} \to X$. One says that
$X^{an}$ is the analytic space associated with $X$.

If $|X^{an}|$ is the underlying set of $X^{an}$, $\phi$ induces a bijection from $|X^{an}|$ to the set $X(\mathbb{C})$
of points of $X$ with values in $\mathbb{C}$. Moreover, for each point $x$ of $X^{an}$, the morphism

$$
\phi_{x}: \mathcal{O}_{X},\phi(x) \to \mathcal{O}^{an}_{X},x,
$$

which is necessarily local, gives after passage to completions an isomorphism

$$
\hat{\phi}_{x}: \hat{\mathcal{O}}_{X},\phi(x) \simeq \hat{\mathcal{O}}^{an}_{X},x.
$$

In particular the morphism $\phi$ is flat.

Notice that the fact that $\phi$ induces a bijection from $X^{an}$ to $X(\mathbb{C})$ follows from the universal
property of $X^{an}$. On the other hand, one has the following assertions:

a. If the theorem is true for a scheme $Y$, then it is also true for every subscheme $X$ of $Y$. Suppose first that $X$
is an open subscheme of $Y$. If $\psi: Y^{an} \to Y$ is the canonical morphism, $\psi^{-1}(X)$ is an open subset

<!-- original page 313 -->

of $Y^{an}$, endowed with the analytic-space structure induced by that of $Y^{an}$. Since every morphism from an
analytic space $\mathcal{X}$ to $X$ factors through $Y^{an}$ by the universal property of the latter, and hence through
$X^{an}$, which is the fiber product $Y^{an} \times_{Y} X$, $X^{an}$ is the analytic space associated with $X$. Finally,
the assertion concerning the $\phi_{x}$ is evident.

It remains only to consider the case where $X$ is a closed subscheme of $Y$. Let $I$ be the coherent
$\mathcal{O}_{Y}$-ideal defining $X$. Then $I \cdot \mathcal{O}^{an}_{Y}$ is a coherent sheaf of ideals on
$\mathcal{O}^{an}_{Y}$ defining a closed analytic subspace $X^{an}$ of $Y^{an}$. As in the case of an open subscheme,
one sees that $X^{an}$ is the analytic space associated with $X$. Let $\phi: X^{an} \to X$ be the canonical morphism.
For every point $x$ of $X^{an}$, the morphism $\phi_{x}$ is none other than the morphism

```text
𝒪_Y,ψ(x)/I_ψ(x) → 𝒪_Y^an,x / I_ψ(x) · 𝒪_Y^an,x
```

induced by $\psi_{x}$. Its completion

$$
\hat{\mathcal{O}}_{Y},\psi(x) / I_{\psi}(x) \cdot \hat{\mathcal{O}}_{Y},\psi(x)
  \to \hat{\mathcal{O}}^{an}_{Y},x / I_{\psi}(x) \cdot \hat{\mathcal{O}}^{an}_{Y},x
$$

is an isomorphism, since $\hat{\psi}_{x}$ is one; this proves a.

b. If one has two $\mathbb{C}$-schemes $X_{1}$, $X_{2}$, such that $X^{an}_{1}$ and $X^{an}_{2}$ exist, then
$(X_{1} \times X_{2})^{an}$ also exists. Indeed, let $\phi_{1}: X^{an}_{1} \to X_{1}$ and
$\phi_{2}: X^{an}_{2} \to X_{2}$ be the canonical morphisms, and let $p_{1}$, $p_{2}$ be the two projections from
$X^{an}_{1} \times X^{an}_{2}$. It follows formally from EGA I 1.8.1 that $X_{1} \times X_{2}$ is the product of $X_{1}$
and $X_{2}$ in the category of ringed spaces in local rings. Consequently the morphisms $\phi_{1} \cdot p_{1}$ and
$\phi_{2} \cdot p_{2}$ define a

<!-- original page 314 -->

morphism $\phi: X^{an}_{1} \times X^{an}_{2} \to X_{1} \times X_{2}$, and the pair
$(X^{an}_{1} \times X^{an}_{2}, \phi)$ represents the functor
$\mathcal{X} \mapsto \operatorname{Hom}_{\mathbb{C}}(\mathcal{X}, X_{1} \times X_{2})$.

c. If $\mathcal{E}^{1}$ denotes affine space of dimension 1, that is, the topological space $\mathbb{C}$ endowed with the sheaf of holomorphic
functions, the functor $\mathcal{X} \mapsto \operatorname{Hom}_{\mathbb{C}}(\mathcal{X},E^{1}_{\mathbb{C}})$ is representable by $\mathcal{E}^{1}$, the canonical morphism $\phi: \mathcal{E}^{1} \to E^{1}_{\mathbb{C}}$ being the
evident morphism. \[Translator note: the corrected source adds in 2003 that $E^{1}_{\mathbb{C}}$ denotes the algebraic affine line
over $\mathbb{C}$.\] Indeed, to give a morphism from an analytic space $\mathcal{X}$ to $E^{1}_{\mathbb{C}}$ is equivalent to giving an element of
$\Gamma(\mathcal{X},\mathcal{O}_{\mathcal{X}})$, which is also equivalent to giving a morphism from $\mathcal{X}$ to $\mathcal{E}^{1}$. Plainly one has a bijection $|\mathcal{E}^{1}| \simeq E^{1}(\mathbb{C})$,
and, for each point $x \in \mathcal{E}^{1}$, the morphism $\hat{\phi}_{x}$ is none other than the identity morphism of a ring of formal power
series in one variable over $\mathbb{C}$.

It follows from b and c that the theorem is true for affine space $E^{n}_{\mathbb{C}}$, $n \geq 0$. Using a, one sees
that it is also true for every affine scheme $X$ locally of finite type over $\mathbb{C}$. If $X$ is no longer assumed
affine and if $(X_{i})$ is a covering of $X$ by affine opens, it follows from the universal property and from a that the
$X^{an}_{i}$ glue and thus define the analytic space $X^{an}$ associated with $X$.

### 1.2.

<!-- label: XII.1.2 -->

Let $f: X \to Y$ be a morphism of $\mathbb{C}$-schemes locally of finite type. If $\phi: X^{an} \to X$ and
$\psi: Y^{an} \to Y$ are the canonical morphisms, it follows from the universal property of $Y^{an}$ that there exists a
unique morphism $f^{an}: X^{an} \to Y^{an}$ such that the diagram

```text
X^an → X
 |      |
f^an   f
 |      |
Y^an → Y
```

is

<!-- original page 315 -->

commutative. We have therefore defined a functor $\Phi$ from the category of $\mathbb{C}$-schemes locally of finite type
to the category of analytic spaces.

The functor $\Phi$ commutes with finite projective limits. Indeed it is enough to see that $\Phi$ commutes with fiber
products. But if $X$, $Y$, $Z$ are schemes locally of finite type over $\mathbb{C}$, it follows from the fact that
$X \times_{Z} Y$ is the fiber product of $X$ and $Y$ over $Z$ in the category of ringed spaces in local rings that
$X^{an} \times^{an}_{Z} Y^{an}$ satisfies the universal property characterizing $(X \times_{Z} Y)^{an}$.

### 1.3.

<!-- label: XII.1.3 -->

Let $X$ be a $\mathbb{C}$-scheme locally of finite type, let $X^{an}$ be the associated analytic space, and let
$\phi: X^{an} \to X$ be the canonical morphism. If $F$ is an $\mathcal{O}_{X}$-module, the inverse image
$\phi*F = F^{an}$ is a sheaf of modules over $\mathcal{O}^{an}_{X}$. This defines a functor from the category of
$\mathcal{O}_{X}$-modules to the category of modules on $X^{an}$. This functor commutes with inductive limits (EGA 0
4.3.2). Since the sheaf $\mathcal{O}^{an}_{X}$ is coherent [XII.4, no. 18, §2, th. 2], it sends coherent sheaves to
coherent sheaves (EGA 0 5.3.11). Moreover:

**Subproposition.**

<!-- label: XII.1.3.1 -->

The functor which associates to an $\mathcal{O}_{X}$-module $F$ its inverse image $F^{an}$ on $X^{an}$ is exact,
faithful, and conservative.

Exactness follows from the fact that the morphism $\phi: X^{an} \to X$ is flat (XIII.1.1). Let us prove that the functor
$F \mapsto F^{an}$ is faithful. Taking exactness into account, it is enough to show that if $F^{an}$ is zero, then $F$
itself is zero. But for every point $x$ of $X^{an}$ one then has

```text
F_φ(x) ⊗_𝒪_X,φ(x) 𝒪_X^an,x = 0.
```

Since the morphism $\mathcal{O}_{X},\phi(x) \to \mathcal{O}^{an}_{X},x$ is faithfully flat, one has $F_{\phi}(x) = 0$
for every closed point $\phi(x)$ of $X$; and since $X$ is Jacobson (EGA IV 10.4.8), this implies that $F$ is zero.

The

<!-- original page 316 -->

fact that the functor $F \mapsto F^{an}$ is conservative is formal from exactness and faithfulness.

## 2. Comparison of Properties of a Scheme and of the Associated Analytic Space

<!-- label: XII.2 -->

**Proposition.**

<!-- label: XII.2.1 -->

Let $X$ be a $\mathbb{C}$-scheme locally of finite type, let $X^{an}$ be the associated analytic space, and let $n$ be
an integer. Consider the property $P$ of being:

```text
(i)    nonempty
(i′)   discrete
(ii)   Cohen-Macaulay
(iii)  (S_n)
(iv)   regular
(v)    (R_n)
(vi)   normal
(vii)  reduced
(viii) of dimension n.
```

Then $X$ has property $P$ if and only if $X^{an}$ has property $P$.

Let $\phi: X^{an} \to X$ be the canonical morphism. Assertion (i) follows from the fact that $|X^{an}| = X(\mathbb{C})$
(XIII.1.1) and from the fact that $X$ is Jacobson (EGA IV 10.4.8). To say that $X$, respectively $X^{an}$, is discrete
is equivalent to saying that $\dim X = 0$, respectively $\dim X^{an} = 0$ by [XII.4, no. 19, §4, cor. 6]; hence (i′)
follows from (viii).

Let $P$ be one of the properties (ii) through (vii). For $X$ to have property $P$, it is necessary and sufficient that
$P$ hold at every closed point of $X$. Indeed, since $X$ is excellent (EGA IV 7.8.6 (iii)), the set of points

<!-- original page 317 -->

where $X$ satisfies $P$ is open, and if this open contains all closed points, it is equal to all of $X$. Thus to say
that $X$, respectively $X^{an}$, has property $P$ is equivalent to saying that for every point $x$ of $X^{an}$, the
local ring $\mathcal{O}_{X},\phi(x)$, respectively $\mathcal{O}^{an}_{X},x$, has property $P$. Since the fact that an
excellent local ring has property $P$ can be detected after passage to the completion, the proposition follows from the
isomorphisms

$$
\hat{\mathcal{O}}_{X},\phi(x) \simeq \hat{\mathcal{O}}^{an}_{X},x
$$

in cases (ii) through (vii). The same holds in case (viii), taking into account the relations

```text
dim X = sup_x dim 𝒪_X,φ(x),     dim X^an = sup_x dim 𝒪_X^an,x,
```

where $x \in X^{an}$. This completes the proof.

**Proposition.**

<!-- label: XII.2.2 -->

Let $X$ be a $\mathbb{C}$-scheme locally of finite type, let $\phi: X^{an} \to X$ be the canonical morphism, and let $T$
be a locally constructible subset of $X$. Then one has the relation

$$
\phi^{-1}(closure(T)) = closure(\phi^{-1}(T)).
$$

We may suppose that $T$ is a dense open subset of $X$. Let $H$ be the reduced closed subscheme of $X$ whose underlying
space is $X - T$. The associated space $H^{an}$ is a closed analytic subspace of $X^{an}$ whose underlying space is
$X^{an} - \phi^{-1}(T)$. We must show that every point $x$ of $H^{an}$ belongs to $closure(\phi^{-1}(T))$. But at such a
point $x$, the germ of analytic space $(X^{an},x)$ contains the subgerm $(H^{an},x)$, and this is defined by a
non-nilpotent ideal of $\mathcal{O}^{an}_{X},x$. It then follows from the Nullstellensatz [XII.4, no. 19, §4, cor. 3]
that every open neighborhood of $x$ contains points of $X^{an}$ which do not belong to $H^{an}$. This proves that
$x \in closure(\phi^{-1}(T))$.

**Corollary.**

<!-- label: XII.2.3 -->

Let

<!-- original page 318 -->

$X$ be a $\mathbb{C}$-scheme locally of finite type, let $\phi: X^{an} \to X$ be the canonical morphism, and let $T$ be
a locally constructible subset of $X$. For $T$ to be an open subset, respectively a closed subset, respectively a dense
subset, it is necessary and sufficient that $\phi^{-1}(T)$ have the corresponding property.

The corollary follows from XII.2.2 and from the fact that, since $X$ is a Jacobson scheme (EGA IV 10.4.8), two locally
constructible subsets of $X$ that have the same trace on the very dense set $X(\mathbb{C})$ are equal.

**Proposition.**

<!-- label: XII.2.4 -->

Let $X$ be a $\mathbb{C}$-scheme locally of finite type. For $X$ to be connected, respectively irreducible, it is
necessary and sufficient that $X^{an}$ be connected, respectively irreducible.

Suppose $X^{an}$ is connected, respectively irreducible. The image $X(\mathbb{C})$ of $X^{an}$ in $X$ is then connected,
respectively irreducible. It follows that $X$ is connected, respectively irreducible, because closed subsets of $X$ and
of $X(\mathbb{C})$ correspond bijectively (EGA IV 10.1.2).

Conversely suppose $X$ is connected, respectively irreducible, and let us show that the same is true of $X^{an}$. We may
restrict to the case where $X$ is irreducible. Indeed, suppose $X$ is connected. Given a point $x$ of $X$, the set of
points $y \in X$ for which there exists a finite sequence of irreducible closed subschemes $X_{1}, \cdots, X_{n}$ of
$X$, with $x \in X_{1}$, $y \in X_{n}$, and $X_{i} \cap X_{i+1} \neq \emptyset$ for $1 \leq i \leq n - 1$, is both open
and closed, hence equal to all of $X$. For a sequence $X_{1}, \cdots, X_{n}$ as above, one also has
$X^{an}_{i} \cap X^{an}_{i+1} \neq \emptyset$ for $1 \leq i \leq n - 1$; if the $X^{an}_{i}$ are known to be connected,
then $X^{an}$ is connected as well.

From now on

<!-- original page 319 -->

suppose $X$ is irreducible. We may also suppose $X$ affine. Indeed, if $(U_{i})_{i\in I}$ is a covering of $X$ by affine
opens, any two of these opens have nonempty intersection, and the same property is therefore true for the covering
$(U^{an}_{i})_{i\in I}$ of $X^{an}$. If the $U^{an}_{i}$ are known to be irreducible, then $X^{an}$ is irreducible as
well.

We may further suppose that $X$ is normal. Indeed, let $\tilde{X}$ be the normalization of $X$. Since the morphism
$\tilde{X} \to X$ is surjective, so is $\tilde{X}^{an} \to X^{an}$, which proves that if $\tilde{X}^{an}$ is
irreducible, then $X^{an}$ is irreducible as well.

From now on suppose $X$ is affine normal. Since the local rings of $X^{an}$ are integral domains, saying that $X^{an}$
is irreducible is equivalent to saying that it is connected. Indeed, if $\mathcal{F}$ is a closed analytic subset of
$X^{an}$, the set of points $x$ of $X^{an}$ at which $codim_{x}(\mathcal{F},X^{an}) = 0$ is a closed analytic subset of
$X^{an}$ [XII.4, no. 20 A, cor. 1] which is also open. If $X^{an}$ is connected, this proves that, whenever
$\mathcal{F} \neq X^{an}$, $\mathcal{F}$ is rare; hence $X^{an}$ is irreducible. We are thus reduced to showing that
$X^{an}$ is connected.

Let

$$
i: X \to P
$$

be a compactification of $X$, where $P$ is a normal projective $\mathbb{C}$-scheme and $i$ is a dominant open immersion.
It then follows from [XII.10, no. 12, th. 1] that $P^{an}$ is connected. Since $X^{an}$ is obtained by removing from
$P^{an}$ a rare closed analytic subset, it follows from XII.2.5 below that $X^{an}$ is also connected.

**Lemma.**

<!-- label: XII.2.5 -->

Let

<!-- original page 320 -->

$\mathcal{P}$ be a connected normal analytic space, and let $\mathcal{Y}$ be a rare closed analytic subset. Then
$\mathcal{X} = \mathcal{P} - \mathcal{Y}$ is connected.

When $\mathcal{Y}$ has codimension $\geq 2$, the proposition follows from [XII.11, no. 3, prop. 4]. In the general case
one may suppose, after removing from $\mathcal{P}$ a closed analytic subset of codimension $\geq 2$, that $\mathcal{P}$
and $\mathcal{Y}$, regarded as a reduced analytic subspace of $\mathcal{P}$, are regular. By the implicit function
theorem, every point $y$ of $\mathcal{Y}$ has a neighborhood $\mathcal{U}$ isomorphic to a ball in an affine space
$\mathcal{E}^{n}$, such that $\mathcal{U} \cap \mathcal{Y}$ is defined by the vanishing of a certain number of
coordinate functions. This proves that $\mathcal{U} - \mathcal{U} \cap \mathcal{Y}$ is connected, and hence that
$\mathcal{X}$ is connected.

**Corollary.**

<!-- label: XII.2.6 -->

Let $X$ be a $\mathbb{C}$-scheme locally of finite type. The morphism

$$
\pi_{0}(X^{an}) \to \pi_{0}(X)
$$

induced by the canonical morphism $X^{an} \to X$ is bijective.

## 3. Comparison of Properties of Morphisms

<!-- label: XII.3 -->

**Proposition.**

<!-- label: XII.3.1 -->

Let $f: X \to Y$ be a morphism of $\mathbb{C}$-schemes locally of finite type, and let $f^{an}: X^{an} \to Y^{an}$ be
the morphism deduced from $f$ on the associated analytic spaces. Let $P$ be the property of being:

```text
(i)    flat
(ii)   net, that is, unramified
(iii)  étale
(iv)   smooth
(v)    normal
(vi)   reduced
(vii)  injective
(viii) separated
(ix)   an isomorphism
(x)    a monomorphism
(xi)   an open immersion.
```

Then $f$ has property $P$ if and only if $f^{an}$ has property $P$.

Let $\phi: X^{an} \to X$ and $\psi: Y^{an} \to Y$ be the canonical morphisms. Let $x$ be a point of $X^{an}$, and put
$y = f^{an}(x)$. The morphisms $\mathcal{O}^{an}_{Y},y \to \mathcal{O}^{an}_{X},x$ and
$\mathcal{O}_{Y},\psi(y) \to \mathcal{O}_{X},\phi(x)$ deduced from $f^{an}$ and $f$ give the same morphism after passage
to completions (XII.1.1). By [XII.2, ch. 3, §5, prop. 4], respectively EGA IV 17.4.4, it is therefore equivalent to say
that $f^{an}$ satisfies property (i), respectively (ii), and to say that $f$ satisfies (i), respectively (ii), at every
closed point of $X$. Since the set of points of $X$ where (i), respectively (ii), holds is open (EGA IV 11.1.1 and I
3.3), this proves (i) and (ii), hence also (iii).

Let $P$ be property (iv), respectively (v), respectively (vi). Taking XII.2.1 ((v), (vi), (vii)) into account, it is
equivalent to say that the geometric fibers of $f^{an}$ at the various points $y$ of $Y^{an}$ are regular, respectively
normal, respectively reduced, and to say that the same is true of the geometric fibers of $f$ at the various closed
points $\psi(y)$ of $Y$. Cases (iv), respectively (v), respectively (vi), then follow from (i) and from the fact that
the set of points of $Y$ where the geometric fibers of $f$ are regular is open (EGA IV 12.1.7).

(vii). If $f$ is injective, so is $f^{an}$. Conversely suppose $f^{an}$ is injective and let us show that $f$ is
injective. We may suppose

<!-- original page 322 -->

$f$ of finite type. Since $f^{an}$ is injective, the fibers of $f$ at closed points of $Y$ are radicial. Since the set
of points of $Y$ whose fiber is radicial is locally constructible (EGA IV 9.6.1), and since $Y$ is a Jacobson scheme,
all fibers of $f$ are radicial; hence $f$ is injective.

(viii). Let $\Delta: X \to X \times_{Y} X$ and $\Delta^{an}: X^{an} \to X^{an} \times_{Y^{an}} X^{an}$ be the diagonal
immersions, and let $\Theta: X^{an} \times_{Y^{an}} X^{an} \to X \times_{Y} X$ be the canonical morphism. By XII.2.3,
saying that $\Delta(X)$ is closed in $X \times_{Y} X$ is equivalent to saying that $\Delta^{an}(X^{an})$ is closed in
$X^{an} \times_{Y^{an}} X^{an}$.

Since an open immersion is nothing other than an étale injective morphism (EGA IV 17.9.1 and [XII.4, no. 13, §1]), (xi)
follows from (iii) and (vii). Since an isomorphism is the same thing as a surjective open immersion, (ix) follows from
(xi) and XII.3.2 (i) below. Saying that $f$ is a monomorphism is equivalent to saying that the diagonal morphism
$\Delta: X \to X \times_{Y} X$ is an isomorphism, so (x) follows from (ix).

**Proposition.**

<!-- label: XII.3.2 -->

Let $X$ and $Y$ be two $\mathbb{C}$-schemes locally of finite type, let $f: X \to Y$ be a morphism of finite type, and
let $f^{an}: X^{an} \to Y^{an}$ be the morphism deduced from $f$ on the associated analytic spaces. Let $P$ be the
property of being:

```text
(i)   surjective
(ii)  dominant
(iii) a closed immersion
(iv)  an immersion
(v)   proper
(vi)  finite.
```

Then $f$ has property $P$ if and only if $f^{an}$ has property $P$. \[Translator note: the source footnote says that a
morphism of analytic spaces is called proper if it is proper in the sense of [XII.1, ch. 1, §10, no. 1] and is
separated.\]

<!-- original page 323 -->

Let $\phi: X^{an} \to X$ and $\psi: Y^{an} \to Y$ be the canonical morphisms.

(i). If $f$ is surjective, then for every point $y$ of $Y^{an}$, $f^{-1}(\psi(y))$ is a nonempty closed subset of $X$;
hence it contains at least one closed point, which proves that $f^{an}$ is surjective. Conversely, if $f^{an}$ is
surjective, $f(X)$ is a locally constructible subset of $Y$ (EGA IV 1.8.4) containing all closed points of $Y$; hence
$f(X) = Y$.

(ii) follows from XII.2.2.

(iii). If $f$ is a closed immersion, then so is $f^{an}$ by XII.1.1 a. Conversely, if $f^{an}$ is a closed immersion,
then so is $f$ by XII.3.1 (x) and XII.3.2 (v), since this is equivalent to saying that $f$ is a proper monomorphism (EGA
IV 8.11.5).

(iv). It is clear that if $f$ is an immersion, then so is $f^{an}$. Conversely suppose $f^{an}$ is an immersion, and let
$T$ be the image of $X$ in $Y$, and $\bar{T}$ the scheme-theoretic closure of $f$. There is a factorization of $f$

```text
X --i→ T̄ --j→ Y,
```

where $j$ is a closed immersion and $i$ is the canonical morphism; from it one deduces the following factorization of
$f^{an}$:

```text
X^an --i^an→ T̄^an --j^an→ Y^an.
```

Since

<!-- original page 324 -->

$T = f(X)$ is a locally constructible subset of $Y$ (EGA IV 1.8.4), one has, by XII.2.2,
$\bar{T}^{an} = closure(f^{an}(X^{an}))$. It follows that $i^{an}(X^{an})$ is open in $\bar{T}^{an}$, hence that $i(X)$
is open in $\bar{T}$. Consider the canonical factorization of $i$

```text
X --i₁→ i(X) --i₂→ T̄.
```

The morphism $i^{an}_{1}$ is a proper monomorphism, hence so is $i_{1}$ by XII.3.2 (v) and XII.3.1 (x). This proves that
$i_{1}$, and hence also $f$, is an immersion.

(v). Suppose $f$ is proper and let us show that $f^{an}$ is proper. Since properness of $f^{an}$ is local on $Y^{an}$,
we may suppose $Y$ affine. By Chow’s lemma (EGA II 5.6.1), one can find a projective $Y$-scheme $X'$ and a projective
surjective morphism

$$
g: X' \to X.
$$

The morphism $(fg)^{an} = f^{an} g^{an}$ is projective, hence proper; $g^{an}$ is surjective; and it follows from \[XII.1, ch.
1, §10\] that $f^{an}$ is proper.

Conversely suppose $f^{an}$ is proper and let us show that $f$ is proper. By XII.3.1 (viii), $f$ is separated. It
remains to prove that $f$ is universally closed, and it is even enough to show that $f$ is closed. Indeed, for every
$Y$-scheme $Y'$ locally of finite type, the morphism

```text
f_(Y′) = h: X ×_Y Y′ → Y′
```

will also be closed since $h^{an}$ is proper. Let $T$ be a closed subset of $X$. The set $f(T)$ is locally
constructible, and one has

$$
f^{an}(\phi^{-1}(T)) = \psi^{-1}(f(T)).
$$

Since

<!-- original page 325 -->

$f^{an}$ is proper, $\psi^{-1}(f(T))$ is a closed subset of $Y^{an}$, and therefore it follows from XII.2.2 that

$$
\psi^{-1}(closure(f(T))) = \psi^{-1}(f(T)).
$$

This implies $f(T) = closure(f(T))$, that is, $f$ is closed; hence $f$ is proper.

(vi). Saying that a morphism is finite is equivalent to saying that it is proper with finite fibers (EGA III 4.4.2 and
[XII.4, no. 19, §5]). Since the set of points where the fibers of $f$ are finite is locally constructible (EGA IV
9.7.9), the fibers of $f$ are finite if and only if the fibers of $f^{an}$ are finite. Thus (vi) follows from (v).

**Remark.**

<!-- label: XII.3.3 -->

a. Let $f: X \to Y$ be a morphism of $\mathbb{C}$-schemes locally of finite type. The fact that $f^{an}$ is a local isomorphism does
not imply that $f$ is one. Indeed, if $f$ is étale, $f^{an}$ is étale and hence is a local isomorphism \[XII.4, no. 13,
§1\], but this need not be true of $f$.

b. The statement XII.3.2 is not true if $f$ is not assumed of finite type. For example, $f^{an}$ can be a closed
immersion without $f$ being one. It is enough to take $X$ to be the sum of $\mathbb{Z}$ copies of
$\operatorname{Spec} \mathbb{C}$, $Y$ to be the affine line, and $f$ the morphism obtained by sending the points of $X$
to distinct points of $Y$ forming a discrete subset.

## 4. Cohomological Comparison Theorems and Existence Theorems

<!-- label: XII.4 -->

<!-- original page 326 -->

The purpose of this number is to reprove the results of [XII.3, no. 2, ths. 5 and 6]. These generalize to the case of a
proper scheme the theorems established in [XII.10, no. 12] when $X$ is projective, and extend them to the relative case.
More general results, concerning relative proper schemes over an analytic space, are proved in [XII.7, ch. VIII, no. 3].

Recall that the Čech cohomology used in [XII.10, no. 12] coincides with the usual cohomology in the algebraic case as
well as in the analytic case (EGA III 1.4.1 and [XII.5, II 5.10]).

### 4.1.

<!-- label: XII.4.1 -->

Let $f: X \to Y$ be a morphism of $\mathbb{C}$-schemes locally of finite type, and consider the commutative diagram

```text
X^an --φ→ X
 |        |
f^an     f
 |        |
Y^an --ψ→ Y.
```

If $F$ is an $\mathcal{O}_{X}$-module, then for every integer $p \geq 0$ one has morphisms

```text
Rᵖf_*F --i→ Rᵖf_*(φ_*F^an) --j→ Rᵖ(f·φ)_*F^an --k→ ψ_*(Rᵖf_*^an F^an),
```

where $i$ is deduced from the canonical morphism $F \to \phi_{*}F^{an}$, and $j$, $k$ are “edge homomorphisms” of Leray
spectral sequences. With the composite $k \cdot j \cdot i$ there is associated a canonical morphism

<!-- label: eq:XII.4.1.1 -->

$$
(4.1.1)   \theta_{p}: (R^{p}f_{*}F)^{an} \to R^{p}f^{an}_{*}(F^{an}).
$$

**Theorem.**

<!-- label: XII.4.2 -->

Let

<!-- original page 327 -->

$f: X \to Y$ be a proper morphism of $\mathbb{C}$-schemes locally of finite type, and let $F$ be a coherent
$\mathcal{O}_{X}$-module. Then, for every integer $p \geq 0$, the morphism (4.1.1)

$$
\theta_{p}: (R^{p}f_{*}F)^{an} \to R^{p}f^{an}_{*}(F^{an})
$$

is an isomorphism.

1. **The case where $f$ is projective.** The proof is analogous to that of [XII.10, no. 13]. Let us recall it briefly.
   One reduces to the case where $X$ is a projective space of type $\mathbb{P}^{r}_{Y}$ over $Y$. Let
   $\mathcal{Y} = Y^{an}$ and $\mathcal{P} = \mathbb{P}^{r}_{\mathcal{Y}}$. One first proves that

```text
f_*^an 𝒪_𝓟 = 𝒪_𝓨,     Rᵖf_*^an(𝒪_𝓟) = 0 for p > 0.
```

To verify the preceding relations, one may reduce to the case where $\mathcal{Y}$ is a ball $\mathcal{B}$ in an affine
space $\mathcal{E}^{n}$. One considers the “standard covering” ${\mathcal{U}_{i}}$ of $\mathcal{P}$ by $r + 1$ open
subsets isomorphic to $\mathcal{B} \times \mathcal{E}^{r}$. Since these opens are Stein, one has, for every integer
$p \geq 0$, isomorphisms

$$
H^{p}({\mathcal{U}_{i}},\mathcal{O}_{\mathcal{P}}) \simeq H^{p}(\mathcal{P},\mathcal{O}_{\mathcal{P}}).
$$

One can then express the sections of the structural sheaf $\mathcal{O}_{\mathcal{P}}$ on the opens $\mathcal{U}_{i}$ and
on their intersections in terms of Laurent series. An easy calculation proves that

```text
H⁰(𝓟,𝒪_𝓟) ≃ H⁰(𝓨,𝒪_𝓨),     Hᵖ(𝓟,𝒪_𝓟) = 0 for p > 0.
```

The proof is then completed by copying [XII.10, no. 12, lemma 5], with cohomology groups replaced by cohomology sheaves.

2.

<!-- original page 328 -->

**The case where $f$ is proper.** One uses EGA III 3.1.2 to reduce to the projective case. Let $\mathcal{K}$ be the
category of coherent $\mathcal{O}_{X}$-modules such that $\theta_{p}$ is an isomorphism for every $p \geq 0$. It is
enough to prove that, for every exact sequence $0 \to F' \to F \to F'' \to 0$ whose two terms are in $\mathcal{K}$, the
third is also in $\mathcal{K}$; that a direct factor of an object of $\mathcal{K}$ is in $\mathcal{K}$; and that, for
every point $x$ of $X$, one can find an object $F$ of $\mathcal{K}$ such that $F_{x} \neq 0$.

The first condition follows by applying the five lemma to the following commutative diagram, whose rows are exact:

```text
… → (Rᵖf_*F′)^an → (Rᵖf_*F)^an → (Rᵖf_*F″)^an → (Rᵖ⁺¹f_*F′)^an → …
      ↓                ↓                 ↓                   ↓
… → Rᵖf_*^an F′^an → Rᵖf_*^an F^an → Rᵖf_*^an F″^an → Rᵖ⁺¹f_*^an F′^an → …
```

The second condition is verified analogously.

To verify the third condition, one may restrict to the case where $X$ is an irreducible scheme with generic point $x$.
We could have supposed $Y$ noetherian from the beginning. By Chow’s lemma (EGA II 5.6.1), one can find a projective
$Y$-scheme $X'$ and a projective surjective morphism $g: X' \to X$. On the other hand, there exists an integer $n$ such
that $R^{p}g_{*}(\mathcal{O}_{X}'(n)) = 0$ for all $p > 0$ and such that the canonical morphism
$g*g_{*}(\mathcal{O}_{X}'(n)) \to \mathcal{O}_{X}'(n)$ is surjective (EGA III 2.2.1). If one puts
$F = g_{*}(\mathcal{O}_{X}'(n))$, the sheaf $F$ answers the question. Indeed $F_{x} \neq 0$; moreover, the Leray
spectral sequence

$$
R^{p}f_{*}(R^{qg}_{*}(\mathcal{O}_{X}'(n))) \Rightarrow R^{p+q}(f\cdot g)_{*}(\mathcal{O}_{X}'(n))
$$

is degenerate, so one has an isomorphism

$$
R^{p}f_{*}F \simeq R^{p}(f\cdot g)_{*}(\mathcal{O}_{X}'(n)).
$$

<!-- original page 329 -->

As in the algebraic case, one has a canonical isomorphism

$$
R^{p}f^{an}_{*} F^{an} \simeq R^{p}(f\cdot g)^{an}_{*}(\mathcal{O}_{X}'(n)^{an}),
$$

and the diagram

$$
(R^{p}f_{*}F)^{an}  \simeq  (R^{p}(f\cdot g)_{*}(\mathcal{O}_{X}'(n)))^{an}
      \downarrow \theta_{p}                \downarrow \psi_{p}
R^{p}f^{an}_{*} F^{an} \simeq R^{p}(f\cdot g)^{an}_{*}(\mathcal{O}_{X}'(n)^{an})
$$

is commutative. By 1, $\psi_{p}$ is an isomorphism; hence $\theta_{p}$ is also an isomorphism. This completes the proof.

**Corollary.**

<!-- label: XII.4.3 -->

Let $X$ be a proper $\mathbb{C}$-scheme, and let $F$ be a coherent $\mathcal{O}_{X}$-module. Then, for every integer
$p \geq 0$, the canonical morphism

$$
H^{p}(X,F) \to H^{p}(X^{an},F^{an})
$$

is an isomorphism.

**Theorem.**

<!-- label: XII.4.4 -->

Let $X$ be a proper $\mathbb{C}$-scheme. The functor which associates to every coherent $\mathcal{O}_{X}$-module $F$ its
inverse image $F^{an}$ on $X^{an}$ is an equivalence of categories.

1. **The functor is fully faithful.** Indeed, let $F$ and $G$ be two coherent $\mathcal{O}_{X}$-modules. The canonical
   morphism

```text
Hom_𝒪_X(F,G) → Hom_𝒪_X^an(F^an,G^an)
```

identifies with the canonical morphism

```text
H⁰(X,SheafHom_𝒪_X(F,G)) → H⁰(X^an,SheafHom_𝒪_X(F,G))
```

<!-- original page 330 -->

(EGA `0_I` 6.7.6). Since `SheafHom_𝒪_X(F,G)` is coherent, it follows from XII.4.3 that this morphism is bijective.

1. **The functor is essentially surjective.** When $X$ is projective, the assertion follows from \[XII.10, no. 12, th.
   3\]. The general case reduces to the preceding one by using Chow’s lemma (EGA II 5.6.1). Indeed, let $X'$ be a
   projective $\mathbb{C}$-scheme, let $f: X' \to X$ be a projective surjective morphism, and let $U$ be a dense open
   subset of $X$ such that $f$ induces an isomorphism $f^{-1}(U) \simeq U$. We reason by noetherian induction on $X$;
   hence we may suppose that for every coherent sheaf $\mathcal{G}$ on $X^{an}$ for which one can find a closed subset
   $Y$ of $X$, distinct from $X$, satisfying $Y^{an} \supset Supp \mathcal{G}$, there exists a coherent sheaf $G$ on $X$
   such that $G^{an} \simeq \mathcal{G}$.

Let $\mathcal{F}$ be a coherent sheaf of modules over $\mathcal{O}^{an}_{X}$, and let $\mathcal{K}$ and $\mathcal{L}$ be
the coherent sheaves defined by requiring the sequence

```text
0 → 𝓚 → 𝓕 → f_*^an f^an*𝓕 → 𝓛 → 0
```

to be exact. Since $X'$ is projective, there exists a coherent $\mathcal{O}_{X}'$-module $F'$ such that
$F'^{an} \simeq f^{an}*\mathcal{F}$. From XII.4.2 one then deduces an isomorphism
$(f_{*}F')^{an} \simeq f^{an}_{*} f^{an}*\mathcal{F}$. Since $\mathcal{K}|U^{an}$ and $\mathcal{L}|U^{an}$ are zero,
there exist coherent $\mathcal{O}_{X}$-modules $K$ and $L$ such that $K^{an} \simeq \mathcal{K}$ and
$L^{an} \simeq \mathcal{L}$. By 1, the morphism $f^{an}_{*} f^{an}*\mathcal{F} \to \mathcal{L}$ comes from a unique
morphism $f_{*}F' \to L$. Let $I = Ker(f_{*}F' \to L)$. The sheaf $\mathcal{F}$ is then an extension of $I^{an}$ by
$K^{an}$, and it remains only to see that this extension comes

<!-- original page 331 -->

by inverse image from an extension of $I$ by $K$. It is therefore enough to prove that the canonical morphism

<!-- label: eq:XII.4.* -->

```text
(*)   Ext^q_𝒪_X(I,K)^an ≃ Ext^q_𝒪_X^an(I^an,K^an),     q = 1,
```

is bijective. \[Translator note: the source prints “$q \neq 1$,” but the preceding sentence shows that the needed case is
$q = 1$; this is a mathematical correction rather than a change of argument.\] Now one has isomorphisms

```text
ExtSheaf^q_𝒪_X(I,K)^an ≃ ExtSheaf^q_𝒪_X^an(I^an,K^an)
```

for every integer $q \geq 0$ (EGA $0_{III}$ 12.3.5), and a morphism of spectral sequences

```text
Hᵖ(X,ExtSheaf^q_𝒪_X(I,K))              ⇒ Ext^(p+q)_𝒪_X(I,K)
     ↓                                             ↓
Hᵖ(X^an,ExtSheaf^q_𝒪_X^an(I^an,K^an)) ⇒ Ext^(p+q)_𝒪_X^an(I^an,K^an).
```

This morphism is an isomorphism because, by XII.4.3, it is so on the $E^{p,q}_{2}$-terms; this proves the bijectivity of
`(*)`.

**Corollary.**

<!-- label: XII.4.5 -->

The functor which associates $X^{an}$ to every proper $\mathbb{C}$-scheme $X$ is fully faithful.

We must show that, if $X$ and $Y$ are two proper $\mathbb{C}$-schemes, the canonical map

$$
\operatorname{Hom}_{\mathbb{C}}(X,Y) \to \operatorname{Hom}(X^{an},Y^{an})
$$

is bijective. But to give a morphism from $X$ to $Y$, respectively from $X^{an}$ to $Y^{an}$, is equivalent to giving
its graph, that is, a closed subscheme $Z$ of $X \times Y$, respectively a closed analytic subspace $\mathcal{Z}$ of
$X^{an} \times Y^{an}$, such that the restriction of the first projection $X \times Y \to X$ to $Z$, respectively of
$X^{an} \times Y^{an} \to X^{an}$ to $\mathcal{Z}$, is

<!-- original page 332 -->

an isomorphism. Since giving a closed subscheme of $X \times Y$, respectively a closed analytic subspace of
$X^{an} \times Y^{an}$, is equivalent to giving a coherent sheaf of ideals on $\mathcal{O}_{X\times Y}$, respectively on
$\mathcal{O}_{X^{an}\times Y^{an}}$, the corollary follows from XII.4.4.

**Corollary.**

<!-- label: XII.4.6 -->

Let $X$ be a proper $\mathbb{C}$-scheme. The functor which associates $X'^{an}$ to every finite, respectively finite
étale, scheme $X'$ over $X$ is an equivalence from the category of finite, respectively finite étale, schemes over $X$
to the category of finite, respectively finite étale, analytic spaces over $X^{an}$.

Indeed, to give a finite morphism $X' \to X$, respectively $X'^{an} \to X^{an}$, is equivalent to giving a coherent
sheaf of algebras over $\mathcal{O}_{X}$, respectively over $\mathcal{O}^{an}_{X}$ [XII.4, no. 19, §5, th. 2]. The
corollary therefore follows from XII.4.4 in the non-respective case, and the respective case follows from it in view of
XII.3.1 (iii).

## 5. Comparison Theorems for Étale Coverings

<!-- label: XII.5 -->

### 5.0.

<!-- label: XII.5.0 -->

Let us make precise the notion of a finite covering of an analytic space. If $\mathcal{X}$ is an analytic space, an
analytic space $\mathcal{X}'$ finite over $\mathcal{X}$ is called a finite covering of $\mathcal{X}$ if every
irreducible component of $\mathcal{X}'$ dominates an irreducible component of $\mathcal{X}$.

**Theorem (“Riemann existence theorem”).**

<!-- label: XII.5.1 -->

Let $X$ be a $\mathbb{C}$-scheme locally of finite type, and let $X^{an}$ be the analytic space associated with $X$. The
functor $\Psi$ which associates $X'^{an}$ to every finite étale covering $X'$ of $X$ is an equivalence

<!-- original page 333 -->

from the category of finite étale coverings of $X$ to the category of finite étale coverings of $X^{an}$.

1. **The functor $\Psi$ is fully faithful.** Let $X'$ and $X''$ be two finite étale coverings of $X$, and let us prove
   that the canonical map

<!-- label: eq:XII.5.* -->

$$
(*)   \operatorname{Hom}_{X}(X',X'') \to \operatorname{Hom}^{an}_{X}(X'^{an},X''^{an})
$$

is bijective. We may suppose $X'$ connected. To give an $X$-morphism from $X'$ to $X''$ is equivalent to giving a
connected component $X_{i}$ of $X' \times_{X} X''$ such that the morphism $X_{i} \to X'$ induced by the first projection
is an isomorphism. Since the connected components of $X' \times_{X} X''$ correspond bijectively to the connected
components of $X'^{an} \times_{X^{an}} X''^{an}$ (XII.2.6), and since a morphism $X_{i} \to X'$ is an isomorphism if and
only if $X^{an}_{i} \to X'^{an}$ is one, this proves the bijectivity of `(*)`.

1. **The functor $\Psi$ is essentially surjective.** Let $\mathcal{X}'$ be a finite étale covering of $X^{an}$, and let
   us prove that there exists an étale covering $X'$ of $X$ such that one has an isomorphism
   $X'^{an} \simeq \mathcal{X}'$. In view of 1, the question is local on $X$, so we may suppose $X$ affine.

a. **Reduction to the case where $X$ is normal.** We may suppose $X$ reduced. Indeed, suppose the theorem proved for
$X_{red}$. The functor which associates to a finite étale covering $X'$ of $X$ the finite étale covering $X'^{an}_{red}$
of $X^{an}_{red}$ is then an equivalence. Since it is obtained by composing $\Psi$ with the functor $\Theta$ which
associates to a finite étale covering of $X^{an}$ its inverse image on $X^{an}_{red}$, and since $\Theta$ is fully
faithful, this shows that $\Psi$ is an equivalence of categories.

We

<!-- original page 334 -->

may suppose $X$ normal. Indeed, let $\tilde{X}$ be the normalization of $X$, and let $p: \tilde{X} \to X$ be the
canonical morphism. Since $p$ is finite, $p$ is a morphism of effective descent for the category of étale coverings
(IX.4.7). Supposing the theorem proved for $\tilde{X}$, put
$\tilde{\mathcal{X}}' = \mathcal{X}' \times_{X^{an}} \tilde{X}^{an}$. There exists an étale covering $\tilde{X}'$ of
$\tilde{X}$ and an isomorphism $\tilde{X}'^{an} \simeq \tilde{\mathcal{X}}'$. It then follows from 1 that the natural
descent datum on $\tilde{\mathcal{X}}'$ lifts to a descent datum on $\tilde{X}'$ relative to $\tilde{X} \to X$. This
proves the existence of an étale covering $X'$ of $X$ such that one has an isomorphism

```text
i: X′^an ×_{X^an} X̃^an ≃ 𝓧̃′,
```

whose inverse images by the two projections from $\tilde{X}^{an} \times_{X^{an}} \tilde{X}^{an}$ are the same. By
IX.3.2, whose proof is valid in the analytic case, the morphism $\tilde{X}^{an} \to X^{an}$ is a morphism of descent for
the category of étale coverings, and consequently $i$ comes from an isomorphism $X'^{an} \simeq \mathcal{X}'$.

b. **Reduction to the case where $X$ is regular.** Let $U$ be the open subset of regular points of $X$, and let
$i: U \to X$ and $i^{an}: U^{an} \to X^{an}$ be the canonical morphisms. Since $X$ is normal, one has
$codim(X - U, X) \geq 2$. Suppose that there exists an étale covering $U'$ of $U$ such that
$U'^{an} \simeq \mathcal{X}'|U^{an}$, and let us show that $U'$ then extends to an étale covering $X'$ of $X$ such that
$X'^{an} \simeq \mathcal{X}'$. It is enough to see that $U'$ extends to an étale covering $X'$ of $X$. Indeed, one will
then have an isomorphism $X'^{an}|U^{an} \simeq \mathcal{X}'|U^{an}$; but if $\mathcal{F}$ and $\mathcal{G}$ are the
coherent sheaves of algebras on $\mathcal{O}^{an}_{X}$ defining respectively $\mathcal{X}'$ and $X'^{an}$, the fact that
$X$ is normal and that $codim(X - U, X) \geq 2$ implies that the canonical morphisms

```text
𝓕 → i_*^an(𝓕|U^an),     𝓖 → i_*^an(𝓖|U^an)
```

are

<!-- original page 335 -->

isomorphisms [XII.11, no. 3, prop. 4]. It follows that $\mathcal{F}$ and $\mathcal{G}$, and hence also $X'^{an}$ and
$\mathcal{X}'$, are isomorphic.

Let $\phi: X^{an} \to X$ be the canonical morphism. Since the problem of extending $U'$ to $X$ is local on $X$, it is
enough to prove that, for every point $y$ of $X^{an} - U^{an}$, the étale covering

```text
U′_φ(y) = U′ ×_X Spec 𝒪_X,φ(y)
```

of

```text
U_φ(y) = U ×_X Spec 𝒪_X,φ(y)
```

extends to $\operatorname{Spec} \mathcal{O}_{X},\phi(y)$. Let $H$ be the coherent $\mathcal{O}_{U}$-algebra defining
$U'$. The canonical morphism

```text
α: (i_*H)^an → i_*^an(H^an) = 𝓕
```

defines a morphism of sheaves of modules on $\operatorname{Spec} \mathcal{O}^{an}_{X},y$:

$$
\alpha_{y}: (i_{*}H)^{an}_{y} \to \mathcal{F}_{y},
$$

whose restriction to

```text
U_y = U_φ(y) ×_{Spec 𝒪_X,φ(y)} Spec 𝒪_X^an,y
```

is an isomorphism. But this proves that $H|U_{y}$ is trivial, hence that $U'_{\phi}(y)$ extends to
$\operatorname{Spec} \mathcal{O}_{X},\phi(y)$.

c. **The case where $X$ is affine regular.** Let

$$
j: X \to P
$$

be a compactification of $X$, where $P$ is a projective $\mathbb{C}$-scheme and $j$ is a dominant open immersion. By the
resolution of singularities theorem [XII.8], one can find a regular scheme $R$ and a projective morphism $r: R \to P$,
such that $r$ induces an isomorphism $r^{-1}(X) \simeq X$ and such that $r^{-1}(X)$ is the complement in $R$ of a
divisor with normal crossings. Let

<!-- original page 336 -->

$$
k: X \to R
$$

be the canonical immersion. We shall show that there exists a finite normal covering $\mathcal{R}'$ of $R^{an}$, in the
sense of XII.5.0, which extends the étale covering $X'^{an}$. By Proposition XII.5.3 below, such a covering is unique;
the problem of extending $X'^{an}$ is therefore local on $R^{an}$ near $R^{an} - X^{an}$. But each point of
$R^{an} - X^{an}$ has an open neighborhood $\mathcal{V}$ isomorphic to a ball in an affine space $\mathcal{E}^{n}$, such
that $\mathcal{V} - \mathcal{V} \cap X^{an}$ is defined by the vanishing of the first $p$ coordinate functions
$z_{1}, \cdots, z_{p}$, with $0 \leq p \leq n$. The fundamental group of $\mathcal{U} = \mathcal{V} \cap X^{an}$ is
isomorphic to $\mathbb{Z}^{p}$, and every étale covering of $\mathcal{U}$ is a quotient of a covering of the form

```text
𝓤″ = 𝓤[T₁,…,T_p]/(T₁ⁿ¹ − z₁, …, T_pⁿᵖ − z_p),
```

where the $n_{i}$ are integers `> 0`, by a subgroup $H$ of the Galois group
$\mathbb{Z}/n_{1}\mathbb{Z} \times \cdots \times \mathbb{Z}/n_{p}\mathbb{Z}$ of $\mathcal{U}''$. But $\mathcal{U}''$
extends to the regular covering

```text
𝓥″ = 𝓥[T₁,…,T_p]/(T₁ⁿ¹ − z₁, …, T_pⁿᵖ − z_p)
```

of $\mathcal{V}$ on which $H$ acts, and the quotient of $\mathcal{V}''$ by $H$ is the desired extension.

The proof is then completed by XII.4.6. The covering $\mathcal{R}'$ comes from a finite covering $R'$ of $R$; the
restriction of $R'$ to $X$ is a covering $X'$ of $X$ such that $X'^{an} \simeq \mathcal{X}'$, and by XII.3.1 (iii), $X'$
is an étale covering of $X$.

**Corollary.**

<!-- label: XII.5.2 -->

Let

<!-- original page 337 -->

$X$ be a connected $\mathbb{C}$-scheme locally of finite type, let $\phi: X^{an} \to X$ be the canonical morphism, and
let $x$ be a point of $X^{an}$. Let $\pi_{1}(X^{an},x)$ be the fundamental group of the topological space $X^{an}$ at
$x$, and let $\pi_{1}(X,\phi(x))$ be the fundamental group of the scheme $X$ at $\phi(x)$ (V.7). Then
$\pi_{1}(X,\phi(x))$ is canonically isomorphic to the completion of $\pi_{1}(X^{an},x)$ for the topology of subgroups of
finite index.

Indeed, let $\mathcal{C}$ be the category of finite étale coverings of $X^{an}$, let $F$ be the functor from
$\mathcal{C}$ to Sets which associates to every finite étale covering $\mathcal{X}'$ of $X^{an}$ the set of points of
$\mathcal{X}'$ above $x$, and let $\hat{\pi}_{1}(X^{an},x)$ be the profinite group associated with $\mathcal{C}$ and $F$
as in V.4. Since every finite étale covering of $X^{an}$ is a quotient of the universal covering by a subgroup of finite
index, $\hat{\pi}_{1}(X^{an},x)$ is nothing other than the completion of $\pi_{1}(X^{an},x)$ for the topology of
subgroups of finite index. The corollary therefore follows from XII.5.1 and V.6.10.

**Proposition.**

<!-- label: XII.5.3 -->

Let $\mathcal{X}$ be a normal analytic space, and let $\mathcal{Y}$ be a closed analytic subset such that
$\mathcal{U} = \mathcal{X} - \mathcal{Y}$ is dense in $\mathcal{X}$. Then the functor which associates to every normal
finite covering $\mathcal{X}'$ of $\mathcal{X}$, in the sense of XII.5.0, its restriction to $\mathcal{U}$ is fully
faithful.

Let $\mathcal{X}'$ and $\mathcal{X}''$ be two finite normal coverings of $\mathcal{X}$. We must show that the canonical
map

$$
\operatorname{Hom}_{\mathcal{X}}(\mathcal{X}',\mathcal{X}'') \to \operatorname{Hom}_{\mathcal{U}}(\mathcal{X}'|\mathcal{U},\mathcal{X}''|\mathcal{U})
$$

is bijective. Let $u$, $v$ be two $\mathcal{X}$-morphisms from $\mathcal{X}'$ to $\mathcal{X}''$ whose restrictions to
$\mathcal{U}$ are the same, and let us prove that $u = v$. The morphisms $u$ and

<!-- original page 338 -->

$v$ coincide on the dense open $\mathcal{U} \times_{\mathcal{X}} \mathcal{X}'$, hence on the underlying topological
spaces. By [XII.4, no. 19, §4, cor. 5], this proves $u = v$.

Let now $u$ be a $\mathcal{U}$-morphism from $\mathcal{X}'|\mathcal{U}$ to $\mathcal{X}''|\mathcal{U}$, and let us show
that it extends to all of $\mathcal{X}'$. We may suppose $\mathcal{X}'$ regular. Indeed, since $\mathcal{X}'$ is normal,
one can find an open subset $\mathcal{V}$ of $\mathcal{X}$ whose complement is an analytic subset of codimension
$\geq 2$, such that $\mathcal{X}' \times_{\mathcal{X}} \mathcal{V} = \mathcal{V}'$ is regular. Let
$\mathcal{V}'' = \mathcal{X}'' \times_{\mathcal{X}} \mathcal{V}$, and suppose the proposition proved for $\mathcal{V}$.
Consider the commutative diagram

```text
𝓥′  → 𝓧′
 ↓      ↓
𝓥   → 𝓧

and similarly 𝓥″ → 𝓧″ over 𝓥 → 𝓧.
```

With $u$ there is associated a morphism of $\mathcal{O}_{\mathcal{V}}$-algebras

$$
g''_{*}\mathcal{O}_{\mathcal{V}}'' \to g'_{*}\mathcal{O}_{\mathcal{V}}',
$$

from which one deduces a morphism

$$
i_{*}g''_{*}\mathcal{O}_{\mathcal{V}}'' \to i_{*}g'_{*}\mathcal{O}_{\mathcal{V}}'.
$$

Taking into account the isomorphisms $i'_{*}\mathcal{O}_{\mathcal{V}}' \simeq \mathcal{O}_{\mathcal{X}}'$ and
$i''_{*}\mathcal{O}_{\mathcal{V}}'' \simeq \mathcal{O}_{\mathcal{X}}''$ [XII.11, no. 3, prop. 4], one deduces a morphism
of $\mathcal{O}_{\mathcal{X}}$-algebras

$$
f''_{*}\mathcal{O}_{\mathcal{X}}'' \to f'_{*}\mathcal{O}_{\mathcal{X}}',
$$

hence the desired morphism $\mathcal{X}' \to \mathcal{X}''$.

We

<!-- original page 339 -->

now suppose $\mathcal{X}'$ regular. Let $\mathcal{U}' = \mathcal{U} \times_{\mathcal{X}} \mathcal{X}'$ and
$\mathcal{Y}' = \mathcal{X}' - \mathcal{U}'$. We regard $\mathcal{Y}'$ as a reduced analytic subspace of $\mathcal{X}'$.
If $\mathcal{Y}'_{1}$ is the singular closed subset of $\mathcal{Y}'$, then $\dim \mathcal{Y}'_{1} < \dim \mathcal{Y}'$
[XII.4, no. 20 D, th. 3]. Thus, by induction on the dimension of $\mathcal{Y}'$, one may suppose $\mathcal{Y}'$ smooth.
Since it is enough to extend $u$ to an open neighborhood of each point of $\mathcal{Y}'$, the implicit function theorem
lets us suppose that $\mathcal{X}'$ is a ball in an affine space $\mathcal{E}^{n}$ and that $\mathcal{Y}'$ is the closed
subset defined by the vanishing of the first $p$ coordinate functions $z_{1}, \cdots, z_{p}$, with $0 \leq p \leq n$.

To $u$ one associates a section $s$ of

```text
p: 𝓧′ ×_𝓧 𝓧″ → 𝓧′
```

above $\mathcal{U}'$. After restricting $\mathcal{X}'$ if necessary, one may suppose that
$p_{*}(\mathcal{O}_{\mathcal{X}'\times_{\mathcal{XX}}''})$ is generated by elements $x_{1}, \cdots, x_{q}$ of
$\Gamma(\mathcal{X}', p_{*}\mathcal{O}_{\mathcal{X}'\times_{\mathcal{XX}}''})$. Let
$u_{1}, \cdots, u_{q} \in \Gamma(\mathcal{U}',\mathcal{O}_{\mathcal{X}}')$ be the images by $s$ of
$x_{1}|\mathcal{U}', \cdots, x_{q}|\mathcal{U}'$. Saying that $s$ extends to $\mathcal{X}'$ is equivalent to saying that
$u_{1}, \cdots, u_{q}$ extend to sections of $\Gamma(\mathcal{X}',\mathcal{O}_{\mathcal{X}}')$. But, since $f$ is
finite, each $u_{i}$ is a Laurent series in $z_{1}, \cdots, z_{p}$ with coefficients that are convergent power series in
$z_{p+1}, \cdots, z_{n}$, and satisfies integral-dependence relations. It follows that $u_{i}$ is bounded, hence is a
convergent power series in $z_{1}, \cdots, z_{n}$, and therefore extends to $\mathcal{X}'$.

One may ask whether the functor introduced in XII.5.3 is an equivalence of categories. This question has an answer by
the theorem of Grauert-Remmert [XII.6], for which we give below a proof using resolution of singularities. One could
also have used the Grauert-Remmert theorem to prove XII.5.1; that was what was done before [XII.8] was available.

**Theorem (Grauert-Remmert theorem).**

<!-- label: XII.5.4 -->

Let

<!-- original page 340 -->

$\mathcal{X}$ be a normal analytic space, and let $\mathcal{Y}$ be a closed analytic subset such that
$\mathcal{U} = \mathcal{X} - \mathcal{Y}$ is dense in $\mathcal{X}$. Let $\mathcal{U}'$ be a normal finite covering of
$\mathcal{U}$. Suppose that there exists a rare closed analytic subset $\mathcal{S}$ of $\mathcal{X}$ such that the
restriction of $\mathcal{U}'$ to $\mathcal{U} - \mathcal{U} \cap \mathcal{S}$ is étale. Then there exists a normal
finite covering $\mathcal{X}'$ of $\mathcal{X}$ extending $\mathcal{U}'$, and $\mathcal{X}'$ is unique up to
isomorphism.

Uniqueness follows from XII.5.3. The problem of extending $\mathcal{U}'$ is therefore local on $\mathcal{X}$. We may
suppose $\mathcal{U}$ regular and $\mathcal{U}'$ étale over $\mathcal{U}$. Indeed, the set of regular points of
$\mathcal{U}$ is a dense open subset $\mathcal{V}$ of $\mathcal{X}$ whose complement is an analytic subset [XII.4, no.
20 D, th. 2], and it is enough to replace $\mathcal{U}$ by the open subset $\mathcal{V} - \mathcal{V} \cap \mathcal{S}$.

Let $y$ be a point of $\mathcal{X} - \mathcal{U}$ and let us show that one can extend $\mathcal{U}'$ to a neighborhood
of $y$. After restricting $\mathcal{X}$ to an open neighborhood of $y$, it follows from the resolution of singularities
theorem [XII.8] that one can find a regular analytic space $\mathcal{X}_{1}$ and a projective morphism
$f: \mathcal{X}_{1} \to \mathcal{X}$ inducing by restriction to $\mathcal{U}$ an isomorphism
$\mathcal{U}_{1} = f^{-1}(\mathcal{U}) \simeq \mathcal{U}$, such that $\mathcal{U}_{1}$ is the complement in
$\mathcal{X}_{1}$ of a divisor with normal crossings. Let us show that $\mathcal{U}'$ extends to a normal finite
covering of $\mathcal{X}_{1}$. Since the question is local on $\mathcal{X}_{1}$, one may suppose that $\mathcal{X}_{1}$
is a ball in an affine space $\mathcal{E}^{n}$ and that $\mathcal{X}_{1} - \mathcal{U}_{1}$ is defined by the vanishing
of the first $p$ coordinate functions $z_{1}, \cdots, z_{p}$, with $0 \leq p \leq n$.
\[Translator note: the corrected source fixes $z_{q}$ to $z_{p}$ in this list.\] The étale covering $\mathcal{U}'$ of
$\mathcal{U}_{1}$ is a quotient of a covering of the form

```text
𝓤₂ = 𝓤₁[T₁,…,T_p]/(T₁ⁿ¹ − z₁, …, T_pⁿᵖ − z_p)
```

by a subgroup $H$ of the Galois group of $\mathcal{U}_{2}$. The covering $\mathcal{U}_{2}$ extends

<!-- original page 341 -->

to the covering

```text
𝓧₂ = 𝓧₁[T₁,…,T_p]/(T₁ⁿ¹ − z₁, …, T_pⁿᵖ − z_p)
```

of $\mathcal{X}_{1}$ on which $H$ acts, and $\mathcal{X}_{2}/H$ extends $\mathcal{U}'$ to $\mathcal{X}_{1}$.

Let $\mathcal{X}'_{1}$ denote the normal finite covering of $\mathcal{X}_{1}$ extending $\mathcal{U}'$, and let
$\mathcal{F}_{1}$ be the coherent `𝒪_𝓧₁`-algebra defining $\mathcal{X}'_{1}$. By the finiteness theorem of
Grauert-Remmert [XII.4, no. 15, th. 1.1], $f_{*}\mathcal{F}_{1}$ is a coherent $\mathcal{O}_{\mathcal{X}}$-algebra. It
therefore corresponds to a finite covering $\mathcal{X}'$ of $\mathcal{X}$, which is normal since $\mathcal{X}'_{1}$ is,
and $\mathcal{X}'$ is the desired extension of $\mathcal{U}'$.

**Remark.**

<!-- label: XII.5.5 -->

In the statement XII.5.4, one cannot remove the hypothesis on the locus of points where the morphism
$\mathcal{U}' \to \mathcal{U}$ is not étale. For example, let $\mathcal{X}$ be the unit disk in the complex plane, let
$\mathcal{U}$ be the complement of the origin in $\mathcal{X}$, and let

$$
\mathcal{U}' = \mathcal{U}[T]/(T^{2} - \sin(1/z)),
$$

where $z$ is the coordinate function on $\mathcal{X}$. Then $\mathcal{U}'$ is a normal finite covering of $\mathcal{U}$
which does not extend to $\mathcal{X}$. Indeed, suppose $\mathcal{U}'$ extended to a finite covering $\mathcal{X}'$ of
$\mathcal{X}$. The locus of points of $\mathcal{X}$ where the morphism $\mathcal{X}' \to \mathcal{X}$ is not étale would
then be a closed analytic subset containing all points $z$ such that $\sin(1/z) = 0$, which is absurd.

One can, however, remove the hypothesis on the singular locus of the morphism $\mathcal{U}' \to \mathcal{U}$ when
$codim(\mathcal{X} - \mathcal{U},\mathcal{X}) \geq 2$. Indeed, one may suppose $\mathcal{U}$ regular. The locus of
points of $\mathcal{U}$ where $\mathcal{U}' \to \mathcal{U}$ is not étale is a divisor of $\mathcal{U}$, and it follows
from the Remmert-Stein theorem [XII.9, th. 3] that it is

<!-- original page 342 -->

the trace on $\mathcal{U}$ of a divisor of $\mathcal{X}$. In this case, if $\mathcal{A}$ is a coherent $\mathcal{O}_{\mathcal{U}}$-algebra such that $\mathcal{U}' = \operatorname{Spec}_{an}(\mathcal{A})$, and
if $i: \mathcal{U} \to \mathcal{X}$ is the canonical morphism, it is enough to take $\mathcal{X}' = \operatorname{Spec}_{an}(i_{*}\mathcal{A})$; indeed one knows that $i_{*}\mathcal{A}$ is
coherent [XII.11, no. 1, th. 1]. \[Translator note: the corrected source fixes the adjective “coherent” to agree with
`i_*𝓐`.\]

**Remark (M. Raynaud, added in 2003).**

<!-- label: XII.5.6 -->

There exist nontrivial finitely presented groups $G$ which have no subgroups of finite index distinct from $G$, for
example G. Higman’s group; cf. J.-P. Serre, _Arbres et amalgames_, Astérisque no. 46, prop. 6, ch. I, §1. Consequently,
if such a group is realized as the topological fundamental group of a scheme $V$ over $\mathbb{C}$, say smooth and projective,
the topological space $V_{top}$ underlying $V$ is not simply connected, but $V$ is algebraically simply connected. At
present no such $V$ is known. Let us nevertheless mention that D. Toledo constructed smooth projective schemes $V$ over
$\mathbb{C}$ whose topological fundamental group is not separated for the topology of subgroups of finite index; the natural
morphism $\pi_{1}(V_{top}) \to \pi_{1}(V_{alg})$ is not injective. \[D. Toledo, “Projective varieties with non-residually finite
fundamental group,” Publ. Math. IHÉS 77 (1993), pp. 103-119.\]

## Bibliography

<!-- original page 343 -->

1. N. Bourbaki, _Topologie Générale_, Hermann, Paris, 1960.
1. N. Bourbaki, _Algèbre Commutative_, Hermann, Paris, 1961.
1. H. Cartan, Séminaire E.N.S., Paris, 1956-57.
1. H. Cartan, Séminaire E.N.S., Paris, 1960-61.
1. R. Godement, _Théorie des Faisceaux_, Hermann, Paris, 1958.
1. H. Grauert and R. Remmert, “Komplexe Räume,” Math. Ann. 136 (1958), pp. 245-318.
1. M. Hakim, _Schémas relatifs_, thesis, Paris, 1967.
1. H. Hironaka, “Resolution of singularities of an algebraic variety over a field of characteristic zero,” Ann. of Math.
   39 (1964), pp. 109-236.
1. R. Remmert and K. Stein, “Ueber die wesentlichen Singularitäten analytischer Mengen,” Math. Ann. 126 (1953), pp.
   263-306.
1. J.-P. Serre, “Géométrie algébrique et géométrie analytique,” Ann. Inst. Fourier (Grenoble) 6 (1956), pp. 1-42.
1. J.-P. Serre, “Prolongement de faisceaux analytiques cohérents,” Ann. Inst. Fourier (Grenoble) 16 (1966), pp. 363-374.


<!-- SOURCE: 13-proprete-cohomologique.md -->

# Exposé XIII. Cohomological Properness of Sheaves of Sets and of Sheaves of Noncommutative Groups

<!-- label: XIII -->

<!-- original page 344 -->

By Mme M. Raynaud. [Translator note: according to unpublished notes of A. Grothendieck.]

This exposé proposes to use étale cohomology to generalize certain results of Exposés IX and X. It also shows how one
can extend to sheaves of not necessarily commutative groups those results of SGA 5 II that still make sense for such
sheaves. The notions of étale cohomology set out in SGA 4 are assumed known.

The main result (XIII.2.4) gives an important example of a nonproper morphism $f: U \to S$ that is "cohomologically
proper in dimension ≤ 1," that is, such that, for certain sheaves of groups $F$ on $U$, in the sense of the étale
topology, the formation of $f_{*}F$ and $R^{1}f_{*}F$ commutes with every base change $S' \to S$. This property is
indeed satisfied by the open $U$ of a scheme $X$ proper over $S$, the complement of a divisor $D$ with normal crossings
relative to $S$, at least if one requires $F$ to be finite constant of order prime to the residual characteristics of
$S$. If $F$ is no longer assumed of order prime to the residual characteristics of $S$, one has an analogous result by
replacing $R^{1}f_{*}F$ by the subsheaf $R^{1}_{tame} f_{*}F$ obtained by restricting to torsors under $F$ "tamely
ramified on $X$ relative to $S$." In particular, this makes it possible to show that the tamely ramified fundamental
group of a proper smooth algebraic curve over a separably closed field, with finitely many closed points removed, is
topologically of finite type (XIII.2.12).

<!-- original page 345 -->

No. XIII.4 is devoted to the homotopy exact sequence and to the Künneth formula.

Finally, an appendix gives useful variants of Abhyankar’s lemma proved in X.3.6.

## 0. Reminders on the Theory of Stacks

<!-- label: XIII.0 -->

We shall use in what follows the theory of stacks set out in [XIII.1] and [XIII.2]. We restrict ourselves to the case of
the étale site of a scheme. Given a scheme X, write X_et for the étale site of X. Recall that a stack F on X is a
fibered category over X_et such that, for every scheme X′ étale over X and every pair of objects x, y of the fiber F_X′,
the presheaf SheafHom_X′(x,y) is a sheaf, and such that, for every surjective étale morphism X″ → X′, every object of
F_X″ endowed with a descent datum relative to X″ → X′ is the inverse image of an object of F_X′. \[Translator note: the
corrected source writes “stack F” and corrects “pair of object” to “pair of objects.”\]

We write F(X′) for the category of cartesian sections of F/X′. More generally, if Sch_X is the category of schemes over
X endowed with the étale topology, the stack F may be extended to a stack 𝓕 on Sch_X, and for every morphism f: X′ → X,
one again writes F(X′) for the category of cartesian sections of this stack 𝓕 over X′.

A gerbe is a stack such that, for every scheme X′ étale over X and every pair of objects x, y of F_X′, every morphism
from x to y is an isomorphism, x and y are locally isomorphic, and the set of objects X′ of X_et such that F_X′ is
nonempty is a refinement of X_et. For example, the stack of torsors under a sheaf of groups is a gerbe which, moreover,
has a cartesian section. Conversely, a gerbe which has a section, that is, such that there exists an object x of F_X, is
equivalent to the stack of torsors under the sheaf

<!-- original page 346 -->

of groups SheafAut_X(x).

There is an evident notion of subgerbe and maximal subgerbe of a stack F. Given a cartesian section x of F(X), there
exists a unique maximal subgerbe G_x of F such that x factors through G_x. One calls G_x the subgerbe generated by x; it
is by definition a trivial gerbe. The presheaf SF

<!-- label: indnot:mb -->

defined by

```text
SF(X′) = { maximal subgerbes of F|X′ }
```

is a sheaf, called the sheaf of maximal subgerbes of F. Let O be the presheaf defined by

```text
O(X′) = { classes of objects of F_X′ modulo isomorphism }.
```

By associating to every object x of F_X′ the maximal subgerbe of F|X′ generated by x, one obtains a morphism

$$
O \to SF;
$$

by [XIII.2, III 2.1.4], this morphism makes SF a sheaf associated with O.

A stack F is said to be **constructible**, respectively **ind-ℒ-finite**, where ℒ is a set of prime numbers, if for
every scheme X′ étale over X and every object x of F_X′, the same is true of the sheaf SheafAut_X′(x) \[XIII.2, VII
2.2.1\]. A stack is said to be **1-constructible** if it is constructible and if its sheaf of maximal subgerbes is
constructible.

## 1. Cohomological Properness

<!-- label: XIII.1 -->

### 1.0.

<!-- label: XIII.1.0 -->

Let S be a scheme, and let f: X → Y be a morphism of S-schemes. If S′ is an S-scheme, consider the following diagram,
all of whose squares are cartesian:

<!-- original page 347 -->

<!-- label: eq:XIII.1.0.1 -->

```text
X′ → X
 |    |
f′   f
 |    |
Y′ → Y
 |    |
S′ → S.
```

If Y₁ is a scheme étale over Y, put X₁ = X ×\_Y Y₁ and Y₁′ = Y′ ×\_Y Y₁, and consider the cartesian square

<!-- label: eq:XIII.1.0.2 -->

```text
X₁′ → X₁
 |      |
f₁′    f₁
 |      |
Y₁′ → Y₁.
```

**Definition.**

<!-- label: XIII.1.1 -->

Let F be a stack on X. One says that (F,f) is **cohomologically proper relative to S in dimension ≤ −1**, respectively
in dimension ≤ 0, respectively in dimension ≤ 1, if for every S-scheme S′, the canonical functor, defined in the evident
way by the universal property of inverse image of stacks,

$$
g*f_{*}F \to f'_{*}h*F       (cf. 1.0.1)
$$

is faithful, respectively fully faithful, respectively an equivalence of categories.

If there is no possible confusion about S, in particular if S = Y, we say cohomologically proper instead of
cohomologically proper relative to S.

### 1.2.

<!-- label: XIII.1.2 -->

Let F be a sheaf of sets on X, and let Φ be the stack in discrete categories associated with F, that is, the stack whose
fiber above every scheme X₁ étale over X is the discrete category whose set of objects is F(X₁). One says that (F,f) is
cohomologically proper relative to S in dimension ≤ −1, respectively in dimension ≤ 0, if (Φ,f) is cohomologically
proper relative to S in dimension ≤ 0, respectively in dimension ≤ 1.

The

<!-- original page 348 -->

canonical morphism

<!-- label: eq:XIII.1.2.1 -->

$$
g*f_{*}F \to f'_{*}h*F
$$

gives, after passage to the associated stacks in discrete categories, the canonical morphism

$$
g*f_{*}\Phi \to f'_{*}h*\Phi.
$$

Consequently, saying that (F,f) is cohomologically proper relative to S in dimension ≤ −1, respectively in dimension ≤
0, is equivalent to saying that, for every S-scheme S′, the morphism above is injective, respectively bijective.

### 1.3.

<!-- label: XIII.1.3 -->

Let F be a sheaf of groups on X, and let Φ be the stack of torsors on X with group F [XIII.1, II 2.3.2]. One says that
(F,f) is cohomologically proper relative to S in dimension ≤ −1, respectively ≤ 0, respectively ≤ 1, if (Φ,f) is
cohomologically proper relative to S in dimension ≤ −1, respectively ≤ 0, respectively ≤ 1. The condition of
cohomological properness can be made explicit as follows.

**Subproposition.**

<!-- label: XIII.1.3.1 -->

The notation is that of (XIII.1.0.1) and (XIII.1.0.2). Let F be a sheaf of groups on X. Write F′, respectively F₁, F₁′,
etc., for the inverse image of F on X′, respectively on X₁, X₁′, etc. Then the following conditions are equivalent:

(i) (F,f) is cohomologically proper relative to S in dimension ≤ −1, respectively ≤ 0, respectively ≤ 1.

(ii) For every morphism S′ → S, every scheme Y₁ étale over Y, and every torsor P on X₁ with group F₁, if ^P F₁ denotes
the group obtained by twisting F₁ by P [XIII.1, II 4.1.2.3], the canonical morphism

```text
a₀: g₁*(f₁*(^P F₁)) → f₁′*(^P′ F₁′)
```

is injective, respectively a₀ is bijective and the canonical morphism

$$
a_{1}: g*(R^{1}f_{*}F) \to R^{1}f'_{*}F'
$$

is

<!-- original page 349 -->

injective, respectively a₀ and a₁ are bijective.

(ii bis) For every morphism S′ → S, every scheme Y₁ étale over Y, every torsor P on X₁ with group F₁, and every torsor R
under ^P F₁, the canonical morphism

$$
\alpha_{0}: g_{1}*(f_{1}*R) \to f_{1}'*R'
$$

is injective, respectively α₀ is bijective, respectively the morphisms α₀ and

```text
α₁: g₁*(R¹f₁*(^P F₁)) → R¹f₁′*(^P′ F₁′)
```

are bijective.

**Proof.**

(i) ⇒ (ii bis). By [XIII.1, II 4.2.5], every torsor R with group ^P F₁ is of the form

```text
R = Q ∧^F₁ P°,
```

where $Q$ is a torsor with group $F_{1}$ and $P^{\circ}$ is the opposite of $P$. One then has
$R' \simeq Q' {\wedge^{F}_{1}}' P'^{\circ}$. Let $\Phi$ be the stack of torsors under $F$, and let $x$, $y$, respectively
$x'$, $y'$, be the objects of the fiber category `(g*f_*Φ)_Y₁′`, respectively `(f′_*Φ′)_Y₁′`, associated with $P$, $Q$,
respectively $P'$, $Q'$. One has the relation

```text
Q ∧^F₁ P° ≃ SheafHom_F₁(P,Q),
```

and hence canonical isomorphisms

```text
SheafHom_Y₁′(x,y) ≃ g₁*f₁*(Q ∧^F₁ P°),
SheafHom_Y₁′(x′,y′) ≃ f₁′*(Q′ ∧^F₁′ P′°).
```

Consequently the morphism α₀ identifies with the morphism

```text
SheafHom_Y₁′(x,y) → SheafHom_Y₁′(x′,y′).
```

It follows that, if (F,f) is cohomologically proper relative to S in dimension ≤ −1, α₀ is injective, and if (F,f) is
cohomologically proper in dimension ≤ 0, α₀ is bijective.

Suppose now that (F,f) is cohomologically proper relative to S in dimension ≤ 1, that is, that the canonical morphism

<!-- original page 350 -->

$$
\phi: g*f_{*}\Phi \to f'_{*}\Phi'
$$

is an equivalence. Let $G$ be the sheaf of maximal subgerbes of the stack $f_{*}\Phi$ [XIII.1, III 2.1.8]; one then has
an isomorphism $G \simeq R^{1}f_{*}F$. Since $g*G$ is the sheaf of maximal subgerbes of $g*f_{*}\Phi$ [XIII.2, III
2.1.5.5], the morphism $\alpha_{1}$ is obtained from $\phi|Y_{1}'$ by taking sheaves of maximal subgerbes, and hence is
an isomorphism.

(ii bis) ⇒ (ii). It is enough to show that, if the morphisms $\alpha_{0}$ are bijective, then the morphisms $a_{1}$ are
injective. Let $Y_{1}'$ be a scheme étale over $Y'$, and let $s$ and $t$ be two elements of $g*(R^{1}f_{*}F)(Y_{1}')$
having the same image in $R^{1}f'_{*}F'(Y_{1}')$; let us show that $s = t$. The assertion is local for the étale
topology of $Y_{1}'$, and, taking into account the definition of the inverse image $g*(R^{1}f_{*}F)$, one may suppose
that $Y_{1}'$ is the inverse image of a scheme $Y_{1}$ étale over $Y$ and that $s$ and $t$ come from torsors $P$ and $Q$
on $X_{1}$. The hypothesis on $s$ and $t$ then means that the inverse images $P'$ and $Q'$ of $P$ and $Q$ on $X_{1}'$
are locally isomorphic for the étale topology of $Y_{1}'$. If one puts `R = SheafHom_F₁(P,Q)`, the fact that the
morphism

$$
g_{1}*f_{1}*R \to f_{1}'*R'
$$

is bijective proves that P and Q are locally isomorphic for the étale topology of Y₁, hence that s = t.

(ii) ⇒ (i). To prove that $\phi$ is faithful, respectively fully faithful, it is enough to show that, if $Y_{1}$ is a
scheme étale over $Y$, if $P$, $Q$ are two torsors on $X_{1}$ with group $F_{1}$, and if $x$, $y$, respectively $x'$,
$y'$, are the objects of `(g*f_*Φ)_Y₁′`, respectively `(f′_*Φ′)_Y₁′`, associated with $P$, $Q$, respectively $P'$, $Q'$,
then the morphism

$$
a: \operatorname{Hom}(x,y) \to \operatorname{Hom}(x',y')
$$

is injective, respectively bijective. But a identifies with the canonical morphism

```text
H⁰(Y₁′, g₁*f₁*(Q ∧^F₁ P°))
  → H⁰(Y₁′, f₁′*(Q′ ∧^F₁′ P′°)).
```

If

<!-- original page 351 -->

Hom(x,y) ≠ ∅, then Q ∧^F₁ P° is a torsor under ^P F₁ locally trivial on Y₁; hence f₁\*(Q ∧^F₁ P°) is a torsor under
f₁\*(^P F₁), and g₁*f₁*(Q ∧^F₁ P°) is a trivial torsor. The morphism a then identifies with the canonical morphism

```text
H⁰(Y₁, g₁*f₁*(^P F₁)) → H⁰(Y₁′, f₁′*(^P′ F₁′)).
```

The same is true if Hom(x′,y′) ≠ ∅ and if a₁ is injective; for then Q′ ∧^F₁′ P′° is trivial, and it follows from the
injectivity of a₁ that P and Q are locally isomorphic on Y₁. We conclude that, if a₀ is injective, respectively if a₀ is
bijective and a₁ injective, then φ is faithful, respectively fully faithful.

It remains to show that, if $a_{0}$ and $a_{1}$ are bijective, the functor $\phi$ is essentially surjective. Let $Y''$
be a scheme étale over $Y'$, put $X'' = X' \times_{Y}' Y''$, and let $P''$ be a torsor on $X''$ with group
$F'' = F'|X''$. We shall show that there exists an element $x$ of $(g*f_{*}\Phi)_{Y}''$ whose image in
$(f'_{*}\Phi')_{Y}''$ is isomorphic to $P''$. Let $p''$ be the class of $P''$. Since $a_{1}$ is surjective, one can find
a surjective étale morphism $Y''_{1} \to Y''$, an étale morphism $Y_{1} \to Y$, a morphism $Y''_{1} \to Y_{1}'$, and a
torsor $P_{1}$ on $X_{1}$ with group $F_{1}$ whose inverse image $P''_{1}$ on $X''_{1}$ is isomorphic to the inverse
image of $P''$. Using the fact that $\phi$ is fully faithful, one sees that the object $x_{1}$ of
${(g*f_{*}\Phi)_{Y}''}_{1}$ corresponding to $P''_{1}$ is endowed with a descent datum relative to $Y''_{1} \to Y''$, and
hence comes from an element $x$ of $(g*f_{*}\Phi)_{Y}''$. Since the image of $x$ in $(f'_{*}\Phi')_{Y}''$ is $P''$, this
proves that $\phi$ is essentially surjective and completes the proof.

**Example.**

<!-- label: XIII.1.4 -->

Let f: X → Y be a proper morphism. It follows from [XIII.2, VII 2.2.2] that, for every ind-finite stack F on X, the pair
(F,f) is cohomologically proper, relative to Y, in dimension ≤ 1. In particular, for every sheaf of sets, respectively
every sheaf of groups, respectively every sheaf of ind-finite groups, F on X, the pair (F,f) is cohomologically

<!-- original page 352 -->

proper in dimension ≤ 0, respectively in dimension ≤ 0, respectively in dimension ≤ 1.

**Remarks.**

<!-- label: XIII.1.5 -->

a. Let F be a sheaf of groups on X such that (F,f) is cohomologically proper relative to S in dimension ≤ −1,
respectively ≤ 0. If F is regarded as a sheaf of sets, then (F,f) is cohomologically proper relative to S in dimension ≤
−1, respectively ≤ 0, but the converse is false.

For example, let Y be the spectrum of a strictly local discrete valuation ring, with closed point t and generic point s;
let f: X → Y be a nonempty scheme over Y whose closed fiber is empty; let F be a nontrivial constant sheaf of groups on
X; and let P be a torsor under F such that H⁰(X_s, ^P F|X_s) = 1. Then (^P F,f) is cohomologically proper relative to Y
in dimension ≤ −1 when ^P F is regarded as a sheaf of sets. If ^P F is regarded as a sheaf of groups, one has an
isomorphism ^P°(^P F) ≃ F; since the canonical morphism

$$
H^{0}(X,F) \to H^{0}(X_{t},F|X_{t}) = 1
$$

is not injective, this proves that (^P F,f) is not cohomologically proper relative to Y in dimension ≤ −1.

b. Suppose f is coherent, that is, quasi-compact and quasi-separated. Let F be a stack on X. For every geometric point ȳ
of Y′, write Ȳ, respectively Ȳ′, for the strict localization of Y, respectively Y′, at ȳ, and put X̄ = X ×\_Y Ȳ, X̄′ = X′
×\_Y′ Ȳ′, etc. For (F,f) to be cohomologically proper relative to S in dimension ≤ −1, respectively ≤ 0, respectively ≤
1, it is necessary and sufficient that, for every S-scheme S′ and every geometric point ȳ of Y′, the canonical functor

$$
\bar{F}(\bar{X}) \to \bar{F}'(\bar{X}')
$$

be faithful, respectively fully faithful, respectively an equivalence.

Indeed,

<!-- original page 353 -->

if S′ is an S-scheme, then for the functor

$$
g*f_{*}F \to f'_{*}F'
$$

to be faithful, respectively fully faithful, respectively an equivalence, it is necessary and sufficient that the same
be true of the functor induced on the fibers at the various geometric points ȳ′ of Ȳ′ [XIII.2, III 2.1.5.9]. The
assertion therefore follows from the calculation of geometric fibers of the direct image of a stack by a coherent
morphism [XIII.2, VII 2.1.5].

c. Let F be a stack on X. The fact that (F,f) is cohomologically proper relative to S in dimension ≤ −1, respectively ≤
0, respectively ≤ 1, is local on Y for the étale topology.

Let S′ be an S-scheme, and let F′ be the inverse image of F on X′; cf. (XIII.1.0.1). If (F,f) is cohomologically proper
relative to S in dimension ≤ 1, then the same is true of (F′,f′). But if (F,f) is cohomologically proper relative to S
in dimension ≤ −1, respectively ≤ 0, this need not remain true for (F′,f′).

For example, let S′ be a discrete valuation ring, let f′: E_S′ → S′ be affine space over S′, let x be a closed point of
E_S′ above the generic point of S′, and let F′ be the sheaf of sets on E_S′ whose restriction to E_S′ − {x} is the
constant sheaf with one element and whose fiber at a geometric point above x has two elements. Then (F′,f′) is not
cohomologically proper relative to S′ in dimension ≤ −1. Let S = S′[Z], let f: E_S → S be affine space over S, and let T
be a closed subset of X = E_S which does not meet the closed subset Z = 0 and such that f(T) contains the generic point
of S. Let G be the inverse image of F′ on X, and let F be the sheaf on X obtained by extending G|X−T by the empty sheaf.
Then (F,f) is cohomologically proper relative to S in dimension ≤ −1, but this is no longer true after the base change
S′ → S defined by Z = 0.

d.

<!-- original page 354 -->

Let F be a stack on X such that (F,f) is cohomologically proper relative to Y in dimension ≤ −1, respectively ≤ 0,
respectively ≤ 1. Then, for every geometric point ȳ of Y, the canonical functor

$$
(f_{*}F)_{\bar{y}} \to F(X_{\bar{y}})
$$

is faithful, respectively fully faithful, respectively an equivalence of categories.

**Proposition.**

<!-- label: XIII.1.6 -->

Let f: X → Y and g: Y → Z be two S-morphisms, and let Φ be a stack on X.

1. Suppose that $(\Phi,f)$ and $(f_{*}\Phi,g)$ are cohomologically proper relative to $S$ in dimension ≤ −1,
   respectively ≤ 0, respectively ≤ 1. Then the same is true of $(\Phi,gf)$.

1. Suppose that $(\Phi,gf)$ is cohomologically proper relative to $S$ in dimension ≤ −1, respectively that $(\Phi,gf)$
   is cohomologically proper relative to $S$ in dimension ≤ 0 and $(\Phi,f)$ cohomologically proper relative to $S$ in
   dimension ≤ −1, respectively that $(\Phi,gf)$ is cohomologically proper relative to $S$ in dimension ≤ 1 and
   $(\Phi,f)$ cohomologically proper relative to $S$ in dimension ≤ 0. Then $(f_{*}\Phi,g)$ is cohomologically proper
   relative to $S$ in dimension ≤ −1, respectively in dimension ≤ 0, respectively in dimension ≤ 1.

For every S-scheme S′, consider the following diagram, all of whose squares are cartesian:

<!-- label: eq:XIII.1.6.1 -->

```text
X′ --f′→ Y′ --g′→ Z′ → S′
 |        |        |     |
h        k        m     |
 |        |        |     |
X  --f→  Y  --g→  Z  → S.
```

[Translator note: the corrected source capitalizes the sentence after the diagram.] The canonical morphism

$$
m*(g_{*}f_{*}\Phi) \to g'_{*}f'_{*}(h*\Phi)
$$

identifies

<!-- original page 355 -->

with the composite of the canonical morphisms

```text
m*(g_*f_*Φ) --i→ g′_*(k*f_*Φ) --j→ g′_*f′_*(h*Φ).
```

1. The hypothesis implies that i and j are faithful, respectively fully faithful, respectively equivalences; hence the
   same is true of ji.

1. The hypothesis implies that ji is faithful, respectively that ji is fully faithful and j is faithful, respectively
   that ji is an equivalence and j is fully faithful. [Translator note: the corrected source fixes a typo in “fully.”]
   It follows that i is faithful, respectively fully faithful, respectively an equivalence.

**Corollary.**

<!-- label: XIII.1.7 -->

Let $f: X \to Y$ and $g: Y \to Z$ be two $S$-morphisms, and let $F$ be a sheaf of groups on $X$. Suppose that `(F,gf)`
is cohomologically proper relative to $S$ in dimension ≤ −1, respectively that `(F,gf)` is cohomologically proper
relative to $S$ in dimension ≤ 0 and that $(F,f)$ is cohomologically proper relative to $S$ in dimension ≤ −1. Then
$(f_{*}F,g)$ is cohomologically proper relative to $S$ in dimension ≤ −1, respectively in dimension ≤ 0.

Return to the notation of (XIII.1.6.1), and for every scheme $Y_{1}$ étale over $Y$, write $f_{1}$, $F_{1}$ for the
respective inverse images of $f$, $F$ by the morphism $Y_{1} \to Y$. Let $\Phi$ be the stack of torsors under $F$, and
let $\Psi$ be the stack of torsors under $f_{*}F$. There is a canonical functor

$$
\phi: \Psi \to f_{*}\Phi,
$$

obtained by associating to every scheme Y₁ étale over Y and every torsor P on Y₁ with group f₁*F₁ the torsor P̃ on X₁
deduced from f₁*P by extension of the structural group f₁*f₁*F₁ → F₁. The functor φ is fully faithful. Indeed, if P and
Q are two torsors on Y₁ with group f₁\*F₁, one has a canonical morphism

```text
SheafIsom_f₁*F₁(P,Q) → f₁*(SheafIsom_F₁(P̃,Q̃))
```

which

<!-- original page 356 -->

is an isomorphism because it is so locally. It follows that the canonical morphism

```text
Isom_f₁*F₁(P,Q) → Isom_F₁(P̃,Q̃)
```

is an isomorphism, hence that φ is fully faithful.

There is a commutative diagram

$$
g'_{*}k*\Psi        \to  m*(g_{*}\Psi)
   \downarrow                \downarrow
g'_{*}k*(f_{*}\Phi)   \to  m*(g_{*}f_{*}\Phi),
$$

where the horizontal arrows are the base-change morphisms. It follows from XIII.1.6 2 that the lower horizontal arrow is
faithful, respectively fully faithful. Since g′_*k*(φ) and m\*g_\*(φ) are fully faithful, the diagram above implies that
the upper horizontal arrow is faithful, respectively fully faithful.

**Corollary.**

<!-- label: XIII.1.8 -->

Let f: X → Y be a coherent S-morphism, let g: Y → Z be a proper S-morphism, and let Φ be an ind-finite stack on X
[XIII.2, VII 2.2.1]. Suppose that (Φ,f) is cohomologically proper relative to S in dimension ≤ −1, respectively ≤ 0,
respectively ≤ 1. Then the same is true of (Φ,gf).

Since $f$ is coherent, $f_{*}\Phi$ is an ind-finite stack (SGA 4 IX 1.6 (ii)). The corollary therefore follows from
XIII.1.6 1 and XIII.1.4.

**Corollary.**

<!-- label: XIII.1.9 -->

Let f: X → Y be an integral S-morphism, and let g: Y → Z be an S-morphism. If F is a sheaf of sets on X, then (f\*\*F,g)
is cohomologically proper relative to S in dimension ≤ −1, respectively ≤ 0, if and only if the same is true of (F,gf).
If F is a sheaf of groups on X, then (f\*\*F,g) is cohomologically proper relative to S in dimension ≤ −1, respectively
≤ 0, respectively ≤ 1, if and only if the same is true of (F,gf).

The assertion

<!-- original page 357 -->

concerning the case of a sheaf of sets follows from XIII.1.6 and from the fact that $(F,f)$ is cohomologically proper
relative to $S$ in dimension ≤ 0. Let $F$ be a sheaf of groups on $X$, and let $\Phi$ be the stack of torsors under $F$.
By SGA 4 VIII 5.8, every torsor under $F$ is locally trivial on $Y$. It follows that the stack $f_{*}\Phi$ is equivalent
to the stack of torsors under $f_{*}F$, the equivalence being obtained by associating to every scheme $Y_{1}$ étale over
$Y$ and every torsor $P$ on $X_{1} = X \times_{Y} Y_{1}$ with group $F|X_{1}$ the torsor $f_{*}P$ with group
$f_{*}F|Y_{1}$. Since $(F,f)$ is cohomologically proper relative to $S$ in dimension ≤ 1, the corollary follows from
XIII.1.6.

**Definitions.**

<!-- label: XIII.1.10 -->

### 1.10.1.

<!-- label: XIII.1.10.1 -->

Let E be a category and consider a diagram

```text
Φ --p→ Φ₁ ⇉ Φ₂,
```

where Φ, Φ₁, Φ₂ are fibered categories over E and the arrows are morphisms of fibered categories, together with an
isomorphism of functors

$$
a: p_{1}p \simeq p_{2}p.
$$

One says that the diagram above is exact if the following condition is satisfied:

a. For every pair of objects x, y of Φ and every morphism f: p(x) → p(y) such that p₁(f) = p₂(f), with p₁p and p₂p
identified by means of a, there exists a unique morphism g: x → y such that p(g) = f.

### 1.10.2.

<!-- label: XIII.1.10.2 -->

Consider the diagram

```text
Φ --p→ Φ₁ ⇉ Φ₂ ⇉⇉ Φ₃,
```

where

<!-- original page 358 -->

Φ and Φ_i, 1 ≤ i ≤ 3, are fibered categories over E and the arrows are morphisms of fibered categories. Suppose given
isomorphisms of functors

```text
a: p₁p ≃ p₂p,
a₁: p₃₁p₂ ≃ p₁₂p₁,     a₂: p₁₂p₂ ≃ p₂₃p₁,     a₃: p₂₃p₂ ≃ p₃₁p₁,
```

such that the evident hexagonal compatibility diagram commutes. We identify p₁p with p₂p, p₃₁p₂ with p₁₂p₁, and so on.

One says that the diagram above is exact if the following conditions are satisfied:

a. The analogue of condition a of XIII.1.10.1.

b. For every object x₁ of Φ₁ and every isomorphism

$$
u: p_{1}(x_{1}) \simeq p_{2}(x_{1})
$$

such that

<!-- label: eq:XIII.1.10.2.1 -->

$$
(1.10.2.1)   p_{23}(u) p_{31}(u) = p_{12}(u)^{-1},
$$

there exists an object x of Φ and an isomorphism i: p(x) ≃ x₁ making the diagram

<!-- label: eq:XIII.1.10.2.2 -->

```text
p₁p(x) = p₂p(x)
  |        |
p₁(i)    p₂(i)
  |        |
p₁(x₁) --u→ p₂(x₁)
```

commute.

### 1.10.3.

<!-- label: XIII.1.10.3 -->

One defines in the evident way the notion of a morphism of exact diagrams of fibered categories over a category E.

### 1.10.4.

<!-- label: XIII.1.10.4 -->

We shall use

<!-- original page 359 -->

in particular the notion of exact diagram in the case where E is a site and Φ, Φ_i, 1 ≤ i ≤ 3, are stacks on E.

Let f: E → E′ be a morphism of sites and let

<!-- label: eq:XIII.1.10.4.1 -->

```text
Φ → Φ₁ ⇉ Φ₂ ⇉⇉ Φ₃
```

be an exact diagram of stacks on E. Taking direct images gives a diagram

```text
f_*Φ → f_*Φ₁ ⇉ f_*Φ₂ ⇉⇉ f_*Φ₃
```

which is evidently exact.

If h: E″ → E is a morphism of sites, one likewise has an exact diagram

```text
h*Φ → h*Φ₁ ⇉ h*Φ₂ ⇉⇉ h*Φ₃.
```

Let us first verify condition a of XIII.1.10.2. Let $F''$ be an object of $E''$, let $x''$ and $y''$ be two objects of
$(h*\Phi)_{F}''$, let $x''_{1}$ and $y''_{1}$ be their respective images in $h*\Phi_{1}$, and let $x''_{2}$ and
$y''_{2}$ be their images in $h*\Phi_{2}$. Let $u''_{1}: x''_{1} \to y''_{1}$ be a morphism such that
$p''_{1}(u''_{1}) = p''_{2}(u''_{1})$, and let us prove that $u''_{1}$ comes from a unique morphism $u'': x'' \to y''$.
Since the question is local on $F''$, one may suppose that one has an object $F_{1}$ of $E$, a morphism from $F''$ to
the inverse image $F''_{1}$ of $F_{1}$ by $h$, and objects $x$, $y$ of `Φ_F₁` whose inverse images on $F''$ are $x''$
and $y''$. Let $x_{1}$, $y_{1}$, respectively $x_{2}$, $y_{2}$, be the images of $x$, $y$ in $\Phi_{1}$, respectively
$\Phi_{2}$. We may suppose that $u''_{1}$ comes from a morphism $u_{1}: x_{1} \to y_{1}$ such that
$p_{1}(u_{1}) = p_{2}(u_{1})$. By exactness of (XIII.1.10.4.1), one obtains a unique morphism $u: x \to y$ whose inverse
image by $h$ is the desired morphism $u''$.

The

<!-- original page 360 -->

condition b of XIII.1.10.2 is verified analogously. Let $x''_{1}$ be an object of $(h*\Phi_{1})_{F}''$, and let
$u'': p''_{1}(x''_{1}) \to p''_{2}(x''_{1})$ be a morphism satisfying

$$
p''_{23}(u'')p''_{31}(u'') = p''_{12}(u'')^{-1}.
$$

We must prove that there exists an object $x''$ of $(h*\Phi)_{F}''$ and an isomorphism $i'': p''(x'') \simeq x''_{1}$
making a diagram analogous to (XIII.1.10.2.2) commute. Since the question is local on $F''$, one may suppose that one
has an object $F_{1}$, a morphism $F'' \to F''_{1}$ as above, and an object $x_{1}$ of `(Φ₁)_F₁` whose inverse image in
$(h*\Phi_{1})_{F}''$ is $x''_{1}$. Likewise one may suppose that $u''$ comes from a morphism
$u: p_{1}(x_{1}) \to p_{2}(x_{1})$ satisfying (XIII.1.10.2.1). The existence of an object $x$ of `Φ_F₁` whose inverse
image by $h$ is an element $x''$ answering the question follows from the exactness of (XIII.1.10.4.1).

**Examples.**

<!-- label: XIII.1.11 -->

1. Let f: X₁ → X be a **morphism of descent** for the category of étale sheaves on variable schemes, for example a
   universally submersive morphism (SGA 4 VIII 9.3). Let X₂ = X₁ ×\_X X₁, let g: X₂ → X be the canonical projection, and
   let F be a sheaf of sets on X. It then follows from loc. cit. that one has an exact sequence of sheaves of sets

<!-- label: eq:XIII.1.11.1 -->

```text
F → f_*f*F ⇉ g_*g*F.
```

If Φ is the stack in discrete categories associated with F and Φ₃ is the final stack on X, that is, the stack all of
whose fibers are reduced to a single object with the identity as its only morphism, saying that the sequence
(XIII.1.11.1) is exact is equivalent to saying that the following diagram of stacks is exact:

```text
Φ → f_*f*Φ ⇉ g_*g*Φ ⇉⇉ Φ₃.
```

2.

<!-- original page 361 -->

Let f: X₁ → X be a **morphism of effective descent** for the category of étale sheaves on variable schemes, for example
a proper surjective morphism, an integral surjective morphism, or a faithfully flat morphism locally of finite
presentation (SGA 4 VIII 9.4). Let X₂ = X₁ ×*X X₁, let g: X₂ → X be the canonical projection, let X₃ = X₁ ×\_X X₁ ×\_X
X₁, and let h: X₃ → X be the canonical morphism. Let Φ be a stack on X, Φ₁ = f\*\*f*Φ, Φ₂ = g**g\*Φ, and Φ₃ = h**h\*Φ.
Then one has an exact diagram

```text
Φ → Φ₁ ⇉ Φ₂ ⇉⇉ Φ₃,
```

where the arrows are the canonical morphisms associated with the projections.

Indeed, regard Φ as a stack on the category Sch_X of schemes over X, endowed with the étale topology. Then, by \[XIII.2,
VII 2.2.8\], Φ is also a stack for the finest topology on Sch_X for which the covering morphisms are the morphisms of
effective descent for the category of étale sheaves. The exactness of the diagram above follows immediately.

**Proposition.**

<!-- label: XIII.1.12 -->

Let S be a scheme, and let f: X → Y be an S-morphism.

1. Let

```text
Φ → Φ₁ ⇉ Φ₂
```

be an exact diagram of stacks on X. Suppose that (Φ₁,f) is cohomologically proper relative to S in dimension ≤ 0 and
that (Φ₂,f) is cohomologically proper relative to S in dimension ≤ −1. Then (Φ,f) is cohomologically proper relative to
S in dimension ≤ 0.

1. Let

```text
Φ → Φ₁ ⇉ Φ₂ ⇉⇉ Φ₃
```

be an exact diagram of stacks on X. Suppose that (Φ₁,f) is cohomologically proper relative to S in dimension ≤ 1, that
(Φ₂,f) is cohomologically proper

<!-- original page 362 -->

relative to S in dimension ≤ 0, and that (Φ₃,f) is cohomologically proper relative to S in dimension ≤ −1. Then (Φ,f) is
cohomologically proper relative to S in dimension ≤ 1. \[Translator note: the corrected source inserts a missing
“relative.”\]

For every S-scheme S′, consider the following commutative diagram, all of whose squares are cartesian:

```text
X′ --f′→ Y′ → S′
 |        |     |
h        g     |
 |        |     |
X  --f→  Y  → S.
```

Let us prove 2; the proof of 1 is analogous. Since direct-image and inverse-image functors send exact diagrams of stacks
to exact diagrams (XIII.1.10.4), one has the following morphism of exact diagrams of stacks:

```text
g*f_*Φ  → g*f_*Φ₁ ⇉ g*f_*Φ₂ ⇉⇉ g*f_*Φ₃
  ↓          ↓           ↓           ↓
f′_*h*Φ → f′_*h*Φ₁ ⇉ f′_*h*Φ₂ ⇉⇉ f′_*h*Φ₃.
```

By hypothesis, the second vertical functor is an equivalence of categories, the third is fully faithful, and the fourth
is faithful. It follows from the preceding diagram that the first vertical functor is an equivalence.

**Proposition.**

<!-- label: XIII.1.13 -->

Let f: X → Y be an S-morphism.

1. Let

```text
F → G ⇉ H
```

be an exact diagram of sheaves of sets on X. Suppose that (G,f) is cohomologically proper relative to S in dimension ≤ 0
and that (H,f) is cohomologically proper relative to S in dimension ≤ −1. Then (F,f) is cohomologically proper relative
to S in dimension ≤ 0.

2.

<!-- original page 363 -->

Let F → G be a monomorphism of sheaves of groups on X. If Y₁ is a scheme étale over Y, put X₁ = Y₁ ×\_Y X, and write f₁,
respectively F₁, respectively G₁, for the inverse image of f, respectively F, respectively G, on Y₁; cf. (XIII.1.0.2).
Suppose that (G,f) is cohomologically proper relative to S in dimension ≤ 0, respectively in dimension ≤ 1, and that for
every scheme Y₁ étale over Y and every torsor Q under G₁, the pair (Q/F₁,f₁) is cohomologically proper relative to S in
dimension ≤ −1, respectively in dimension ≤ 0. Then (F,f) is cohomologically proper relative to S in dimension ≤ 0,
respectively in dimension ≤ 1.

1. Let F → G be a monomorphism of sheaves of groups on X. Suppose that (F,f) is cohomologically proper relative to S in
   dimension ≤ 1 and that (G,f) is cohomologically proper relative to S in dimension ≤ 0. Then, for every torsor Q under
   G, the pair (Q/F,f) is cohomologically proper relative to S in dimension ≤ 0.

**Proof.**

1. Let Φ, respectively Φ₁, respectively Φ₂, be the stack in discrete categories associated with F, respectively G,
   respectively H, and let Φ₃ be the final stack on X. One then has an exact diagram

```text
Φ → Φ₁ ⇉ Φ₂ ⇉⇉ Φ₃.
```

By hypothesis, (Φ₁,f) is cohomologically proper relative to S in dimension ≤ 1 and (Φ₂,f) is cohomologically proper
relative to S in dimension ≤ 0 (XIII.1.2). Since (Φ₃,f) is evidently cohomologically proper relative to S in dimension ≤
−1, it follows from XIII.1.12 that (Φ,f) is cohomologically proper relative to S in dimension ≤ 1, that is, that (F,f)
is cohomologically proper relative to S in dimension ≤ 0.

1. Let us first show that, if (G,f) is cohomologically proper relative to S in dimension ≤ 0 and if the (Q/F₁,f₁) are
   cohomologically

<!-- original page 364 -->

proper relative to S in dimension ≤ −1, then (F,f) is cohomologically proper relative to S in dimension ≤ 0. By
XIII.1.3.1, it is enough to prove that, for every scheme Y₁ étale over Y and every torsor P on X₁ with group F₁, the
pair (^P F₁,f₁) is cohomologically proper relative to S in dimension ≤ 0 when ^P F₁ is regarded as a sheaf of sets, and
that the canonical morphism

$$
d: g*(R^{1}f_{*}F) \to R^{1}f'_{*}F'
$$

is injective. The first assertion follows at once from 1: if Q denotes the torsor deduced from P by extension of the
structural group F₁ → G₁, one has an isomorphism

```text
^Q G₁ / ^P F₁ ≃ Q/F₁.
```

Let us show that d is injective. It is enough to prove that, if Y₁ is a scheme étale over Y and P, P̃ are two torsors
under F₁ whose inverse images P′ and P̃′ on X₁′ are isomorphic, then, after possibly making a surjective étale extension
of Y₁, P and P̃ become isomorphic. Choose an isomorphism p′: P′ ≃ P̃′. Let Q, respectively Q̃, be the torsor deduced from
P, respectively P̃, by extension of the structural group F₁ → G₁. The inverse images Q′, respectively Q̃′, of Q,
respectively Q̃, on X₁′ are deduced from P′, respectively P̃′, by extension of the structural group F₁′ → G₁′; [Translator
note: the corrected source inserts the missing article before “extension.”] let q′: Q′ ≃ Q̃′ be the isomorphism obtained
in the same way from p′. Since (G,f) is cohomologically proper relative to S in dimension ≤ 0, after possibly making a
surjective étale extension of Y₁, one may suppose that q′ is the image of an isomorphism q: Q ≃ Q̃. To the torsor P,
respectively P̃, is associated a section x of Q/F₁, respectively a section x̃ of Q̃/F₁, and for P and P̃ to be isomorphic,
it is necessary and sufficient that there be an isomorphism Q ≃ Q̃ such that the induced isomorphism

$$
e: H^{0}(X_{1},Q/F_{1}) \to H^{0}(X_{1},\tilde{Q}/F_{1})
$$

sends x to x̃. We take the isomorphism q. The sections e(x) and x̃ of H⁰(X₁,Q̃/F₁) have the same image in H⁰(X₁′,Q̃′/F₁′).
Since (Q̃/F₁,f₁) is cohomologically proper relative to S in dimension ≤ −1,

<!-- original page 365 -->

after possibly making a surjective étale extension of Y₁, one indeed has e(x) = x̃. This proves the injectivity of d.

To finish the proof, it remains to prove that if (G,f) is cohomologically proper relative to S in dimension ≤ 1, and if
for every scheme Y₁ étale over Y and every torsor Q on X₁ with group G₁, the pair (Q/F₁,f₁) is cohomologically proper
relative to S in dimension ≤ 0, then the morphism d is surjective. Let P′ be a torsor on X₁′ with group F₁′, and let Q′
be the torsor under G₁′ obtained from P′ by extension of the structural group. Giving P′ is equivalent to giving Q′ and
a section x′ of H⁰(X₁′,Q′/F₁′). It then follows from the surjectivity of the morphism

$$
g*(R^{1}f_{*}G) \to R^{1}f'_{*}G'
$$

that, after possibly making a surjective étale extension of Y₁, there exists a torsor Q under G₁ whose inverse image on
X₁′ is isomorphic to Q′. Using the fact that (Q/F₁,f₁) is cohomologically proper relative to S in dimension ≤ 0, one may
similarly suppose that there exists an element x of H⁰(X₁,Q/F₁) whose image in H⁰(X₁′,Q′/F₁′) is x′. The data of Q and x
determine a torsor P under F₁ whose inverse image on X₁′ is isomorphic to P′, which proves the surjectivity of d.

1. Let us show that (Q/F,f) is cohomologically proper relative to S in dimension ≤ −1, that is, that for every S-scheme
   S′ and every scheme Y₁ étale over Y, if x and x̃ are two elements of H⁰(X₁,Q₁/F₁) whose images x′ and x̃′ in
   H⁰(X₁′,Q₁′/F₁′) are equal, then, after a surjective extension of Y₁, one has x = x̃. To x, respectively x̃, is
   associated a torsor P, respectively P̃, under F₁, such that Q₁ is deduced from P, respectively P̃, by extension of the
   structural group F₁ → G₁. From the relation x′ = x̃′ it follows that one has an isomorphism u′: P′ ≃ P̃′ such that the
   isomorphism induced on Q₁′ by u′ is the identity. Since (F,f) is cohomologically proper relative to S in dimension ≤
   0, it follows that,

<!-- original page 366 -->

after a surjective étale extension of Y₁, one has an isomorphism u: P → P̃ lifting u′. The fact that (G,f) is
cohomologically proper relative to S in dimension ≤ −1 then implies that x = x̃.

Let us show that (Q/F,f) is cohomologically proper relative to S in dimension ≤ 0. Let Y″ be a scheme étale over Y′, and
let x″ be an element of H⁰(X″,Q″/F″). To x″ is associated a torsor P″ on X″ with group F″. Since (F,f) is
cohomologically proper relative to S in dimension ≤ 1, one can find surjective étale morphisms Y″₁ → Y″ and Y₁ → Y, with
a morphism Y″₁ → Y₁′, and a torsor P on X₁ with group F₁ whose inverse image on X″₁ is isomorphic to the inverse image
of P″. It then follows from the fact that (G,f) is cohomologically proper relative to S in dimension ≤ 0 that one may
even choose Y″₁ and Y₁ so that the torsor deduced from P by extension of the structural group F₁ → G₁ is isomorphic to
Q₁. To P there corresponds an element x of H⁰(X₁,Q₁/F₁), whose image in H⁰(X″₁,Q″₁/F″₁) is isomorphic to the inverse
image of x″. This completes the proof.

**Proposition.**

<!-- label: XIII.1.14 -->

Let f: X → S be an S-scheme, and let F be a sheaf of sets or groups on X, respectively a sheaf of ind-ℒ-groups, where ℒ
is a set of prime numbers. Suppose F is locally constant, (F,f) is cohomologically proper in dimension ≤ 0, respectively
in dimension ≤ 1, and f is locally 0-acyclic, respectively locally 1-aspherical for ℒ (SGA 4 XV 1.11). Then, for every
specialization s̄₁ → s̄₂ of geometric points of S, the specialization morphism (SGA 4 VIII 7.1)

```text
a₀: (f_*F)_s̄₂ → (f_*F)_s̄₁
```

is an isomorphism; and, if F is a sheaf of groups, the morphism

```text
a₁: (R¹f_*F)_s̄₂ → (R¹f_*F)_s̄₁
```

is injective, respectively the morphisms a₀ and a₁ are isomorphisms.

The

<!-- original page 367 -->

proof is obtained by copying word for word that of SGA 4 XVI 2.3, but replacing the expression “proper” by the
expression “cohomologically proper.”

**Corollary.**

<!-- label: XIII.1.15 -->

Let f: X → S be a morphism, let Φ be a stack on X, and let ℒ be a set of prime numbers. Suppose that, for every scheme
X₁ étale over X and every pair of objects x, y of Φ_X₁, the sheaf SheafHom_X₁(x,y) is locally constant, that the sheaf
SheafAut_X₁(x) is a locally constant ind-ℒ-group, and that the sheaf SΦ of maximal subgerbes of Φ [XIII.1, III 2.1.7] is
locally constant. Suppose that (Φ,f) is cohomologically proper in dimension ≤ 1 and that f is locally 1-aspherical for
ℒ. Then, for every specialization s̄₁ → s̄₂ of geometric points of S, the specialization morphism

```text
a: (f_*Φ)_s̄₂ → (f_*Φ)_s̄₁
```

is an equivalence of categories.

Let S̄₁, respectively S̄₂, be the strict localization of S at s̄₁, respectively at s̄₂, let X̄₂, Φ̄₂, respectively X̄₁, Φ̄₁, be
the inverse images of X₂, Φ₂ on S̄₂, respectively of X₁, Φ₁ on S̄₁, and consider the cartesian square

```text
X̄₁ --h→ X̄₂
 |        |
f̄₁      f̄₂
 |        |
S̄₁ --g→ S̄₂.
```

We must show that the functor

$$
\phi: \bar{\Phi}_{2}(\bar{X}_{2}) \to \bar{\Phi}_{1}(\bar{X}_{1})
$$

is an equivalence. The functor φ is fully faithful. Indeed, let

<!-- original page 368 -->

$x$ and $y$ be two objects of `(Φ̄₂)_X̄₂`; the canonical morphism

```text
Hom_X̄₂(x,y) → Hom_X̄₁(φ(x),φ(y))
```

identifies with the canonical morphism

```text
H⁰(X̄₂,SheafHom_X̄₂(x,y)) → H⁰(X̄₁,h*(SheafHom_X̄₂(x,y))).
```

This morphism is an isomorphism by XIII.1.14.

Let us show that φ is an equivalence. Let x₁ be an object of Φ̄₁(X̄₁), and let G₁ be the maximal subgerbe of Φ̄₁ generated
by x₁. The morphism

$$
H^{0}(\bar{X}_{2},S\bar{\Phi}_{2}) \to H^{0}(\bar{X}_{1},h*(S\bar{\Phi}_{2})) = H^{0}(\bar{X}_{1},S\bar{\Phi}_{1})
$$

is bijective; hence there exists a maximal subgerbe G₂ of Φ̄₂ such that h\*G₂ is isomorphic to G₁. It remains only to
prove that the functor

$$
G_{2} \to h_{*}h*G_{2}
$$

is an equivalence. But in this form the question is local for the étale topology on X̄₂. We may therefore suppose that G₂
is a gerbe of torsors under the automorphism group of an object of G₂, a case in which the assertion follows from
XIII.1.14.

**Corollary.**

<!-- label: XIII.1.16 -->

The hypotheses are those of XIII.1.14. If in addition $F$ is a sheaf of sets, respectively of ind-$\mathcal{L}$-groups,
and $f_{*}F$, respectively $R^{1}f_{*}F$, is constructible, then $f_{*}F$, respectively $R^{1}f_{*}F$, is locally
constant.

The corollary follows from XIII.1.14 by SGA 4 IX 2.11.

**Remark.**

<!-- label: XIII.1.17 -->

Recall that the condition that f be locally 0-acyclic is satisfied if f is flat with separable fibers and X and Y are
locally noetherian (SGA 4 XV 4.1), and that the condition that f be locally 1-aspherical

<!-- original page 369 -->

for ℒ is satisfied if f is smooth, ℒ being the set of prime numbers distinct from the residual characteristics of S (SGA
4 XV 2.1).

## 2. A Special Case of Cohomological Properness: Relative Normal-Crossings Divisors

<!-- label: XIII.2 -->

### 2.0.

<!-- label: XIII.2.0 -->

Let $R$ be a discrete valuation ring with field of fractions $K$, and let $L$ be an étale $K$-algebra. Then $L$ is a
direct product of finitely many fields $L_{i}$, where $L_{i}$ is an étale extension of $K$. If $L'_{i}$ denotes the
Galois extension generated by $L_{i}$ in an algebraic closure of $L_{i}$, one says that $L$ is **tamely ramified** over
$R$ if the $L'_{i}$ are tamely ramified extensions in the sense of X.3, that is, if an inertia group $I_{i}$ of
$L'_{i}|K$ has order prime to the residual characteristic $p$ of $R$.

One knows that $I_{i}$ is in any case an extension of a cyclic group of order prime to $p$ by a $p$-group. This follows
from [XIII.5, ch. IV, prop. 7, cor. 4] when the residual extension of $R$ is separable. The proof given there extends to
the general case as follows. Resume the hypotheses and notation of loc. cit., but without assuming the residual
extension separable. Let $H_{i}$ be the subgroup of the inertia group $G_{0}$ consisting of the elements $s$ of $G_{0}$
such that $s\pi/\pi \in U^{i}$ for every uniformizer $\pi$ of `A_L`. One then verifies that $G_{0}/H_{1}$ is a group of
order prime to $p$ and that, for $i \geq 1$, the $H^{i}/H^{i+1}$ are $p$-groups, from which the announced result
follows.

### 2.0.1.

<!-- label: XIII.2.0.1 -->

In the case where $R$ is strictly local, one has the following simple characterization: the $K$-algebra $L$ is tamely
ramified over $R$ if and only if the $[L_{i}:K]$ are prime to $p$. Moreover, if $L$ is tamely ramified over $R$, the
$L_{i}$ are cyclic extensions of $K$. Indeed, when $R$ is strictly local, $I_{i}$ is equal to the Galois group

<!-- original page 370 -->

of $L'_{i}$ over $K$. As just recalled, $I_{i}$ is an extension of a cyclic group of order prime to $p$ by a $p$-group.
If $L'_{i}$ is assumed tamely ramified over $R$, $I_{i}$ is then a cyclic group of order prime to $p$. It follows that
$[L_{i}:K]$ is prime to $p$ and that $L_{i} = L'_{i}$. Conversely, if $[L_{i}:K]$ is prime to $p$, $I_{i}$ cannot
contain a nontrivial normal $p$-subgroup; hence $I_{i}$ is a cyclic group of order prime to $p$, which proves that
$L_{i}$ is tamely ramified over $R$.

### 2.0.2.

<!-- label: XIII.2.0.2 -->

Let R be a discrete valuation ring with field of fractions K, let L be an étale K-algebra, and let R̄ be a strict
localization of R, K̄ its field of fractions, and L̄ = L ⊗\_K K̄. Then L is tamely ramified over R if and only if L̄ is
tamely ramified over R̄. Indeed, one reduces to the case where L is a field. Let L̄ = ∏\_i L̄_i, where the L̄_i are
fields extending K̄. If L′ is the Galois extension generated by L, and if L̄′ = L′ ⊗\_K K̄, \[Translator note: the
corrected source fixes L' to \bar{L}' here and in the following displayed product.\] then one likewise has a decomposition of
L̄′ as a product of fields,

$$
\bar{L}' = \prod_{j} \bar{L}'_{j},
$$

and each $\bar{L}_{i}$ is a subextension of at least one of the $\bar{L}'_{j}$. Since $L'$ is a Galois extension of $K$,
the $\bar{L}'_{j}$ are Galois extensions of $\bar{K}$. Suppose $L$ is tamely ramified over $R$. Since the Galois group
of $\bar{L}'_{j}|\bar{K}$ is isomorphic to the inertia group of $L'|K$, the $\bar{L}'_{j}$ are also tamely ramified over
$\bar{R}$, and hence so are the $\bar{L}_{i}$. Conversely, suppose $\bar{L}$ is tamely ramified over $\bar{R}$. For each
$j$, let $v_{j}$ be the discrete valuation of $\bar{L}'_{j}$ extending the valuation of $\bar{K}$, and again write
$v_{j}$ for the valuation induced on $L'$. As $j$ varies, $v_{j}$ runs through the set of valuations of $L'$ extending
the valuation of $K$. Let $G = \operatorname{Gal}(L'|K)$, $H = \operatorname{Gal}(L'|L)$, $I_{j}$ be the inertia group
of $L'|K$ at $v_{j}$, and $J_{j}$ the inertia group of $L'|L$ at $v_{j}$. The group $I_{j}$ is an extension of a cyclic
group of order prime to $p$ by a $p$-group $P_{j}$. Since the $\bar{L}_{i}$ are tamely ramified over $\bar{R}$,
$I_{j}/J_{j}$ has order prime to $p$, hence $P_{j} \subset J_{j}$. Consequently $H$ contains all the $P_{j}$, and
therefore also the group $P$ generated by

<!-- original page 371 -->

the P_j as j varies. But P is invariant in G, because an inner automorphism of G transforms the I_j among themselves and
hence also the P_j among themselves. It follows that P is a subgroup of H normal in G; hence, since L′ is the Galois
extension generated by L, one has P = 1. This proves that L is tamely ramified over R.

More generally, let R → R′ be a morphism of discrete valuation rings such that the image of a uniformizer π of R is a
uniformizer π′ of R′ and such that the residual extension κ(R′) is a separable extension of κ(R). Let K be the field of
fractions of R, K′ the field of fractions of R′, L an étale K-algebra, and L′ = L ⊗\*K K′. Then L is tamely ramified
over R if and only if L′ is tamely ramified over R′. Indeed, one may suppose R and R′ strictly local. By XIII.2.0.1 it
is enough to prove that, when L is a field, L′ is also a field. Let R̃ be the normalization of R in L, let π̃ be a
uniformizer of R̃, and let R̃′ = R̃ ⊗\_R R′. Since the extension κ(R̃)|κ(R) is radicial and the extension κ(R′)|κ(R) is
étale, κ(R̃) ⊗\*κ(R) κ(R′) is a field [EGA IV 4.3.2 and 4.3.5]. This proves that R̃′ is a local ring; and since π maps to
π′ in R′, one has κ(R̃′) = R′/(π̃). Consequently R̃′ is a discrete valuation ring [XIII.5, ch. I, §2, prop. 2], and hence
L′ is a field.

### 2.0.3.

<!-- label: XIII.2.0.3 -->

By reduction to the strictly local case, one sees that a subalgebra of a tamely ramified algebra is tamely ramified,
that the tensor product of two tamely ramified algebras is tamely ramified, that a tamely ramified algebra remains
tamely ramified after extension of the discrete valuation ring, and that an algebra which becomes tamely ramified after
a tamely ramified extension is tamely ramified.

### 2.1.

<!-- label: XIII.2.1 -->

Let

<!-- original page 372 -->

$X$ be an $S$-scheme, and let $D$ be a divisor $\geq 0$ on $X$. Recall (SGA 5 II 4.2) that $D$ is said to be **strictly
with normal crossings relative to $S$** if there exists a finite family $(f_{i})_{i}\in I$ of elements of
$\Gamma(X,\mathcal{O}_{X})$, such that $D = \sum_{i\in I} divisor(f_{i})$ and the following condition is satisfied:

### 2.1.0.

<!-- label: XIII.2.1.0 -->

For every point $x$ of `Supp D`, $X$ is smooth over $S$ at $x$, and, if $I(x)$ denotes the set of $i \in I$ such that
$f_{i}(x) = 0$, the subscheme $V((f_{i})_{i}\in I(x))$ is smooth over $S$ of codimension `card I(x)` in $X$.

The divisor D is said to be **with normal crossings relative to S** if, locally on X for the étale topology, it is
strictly with normal crossings.

Let D be a divisor with normal crossings relative to S. Put Y = Supp D and U = X − Y, and write i: U → X for the
canonical immersion. For every geometric point s̄ of S and every maximal point y of the geometric fiber Y_s̄, the ring R =
𝒪_X_s̄,y is a discrete valuation ring.

In the sequel of this number, we shall use the following technical definition:

**Subdefinition.**

<!-- label: XIII.2.1.1 -->

Let F be a sheaf of sets on U. One says that F is **tamely ramified on X**, along D, **relative to S**, if for every
geometric point s̄ of S, the following condition is satisfied:

For every maximal point y of Y_s̄, the restriction of F to the field of fractions K of 𝒪_X_s̄,y is representable by the
spectrum of an étale K-algebra L, tamely ramified over 𝒪_X_s̄,y.

Most often, when no confusion can result, we shall omit mention of D in the terminology.

**Subdefinition.**

<!-- label: XIII.2.1.2 -->

If

<!-- original page 373 -->

F is a sheaf of groups on U, tamely ramified on X relative to S, we denote by

<!-- label: indnot:mc -->

$$
H^{1}_{tame}(U,F)
$$

the subset of H¹(U,F) formed by the classes of torsors under F that are tamely ramified on X relative to S.

Let

```text
U --i→ X
 \    |
  \   f
   g  |
    \ |
      T
```

be a commutative diagram of S-schemes, with i as in XIII.2.1. We denote by

<!-- label: indnot:md -->

$$
R^{1}_{tame} g_{*}F
$$

the sheaf on T associated with the presheaf

$$
T' \mapsto H^{1}_{tame}(U',F),
$$

where $T'$ ranges over the schemes étale over $T$ and $U' = U \times_{T} T'$. The sheaf $R^{1}_{tame} g_{*}F$ is a
subsheaf of $R^{1}g_{*}F$.

Notice that, if g is coherent, if t̄ is a geometric point of T, T̄ is the strict localization of T at t̄, and Ū = U ×\_T T̄,
one has an isomorphism

<!-- label: eq:XIII.2.1.2.1 -->

$$
(R^{1}_{tame} g_{*}F)_{\bar{t}} \simeq H^{1}_{tame}(\bar{U},\bar{F}).
$$

### 2.1.3.

<!-- label: XIII.2.1.3 -->

Let C_t((U,X)/S), or simply C_t,

<!-- label: indnot:me -->

be the category of étale coverings of U that are tamely ramified on X relative to S. Suppose U is connected and let a be
a geometric point of U. Let Γ_t be the functor which associates to an étale covering U′ of U, tamely ramified on X
relative to S, the set of geometric points of U′ above a. It follows from XIII.2.0 that the pair (C_t,Γ_t) satisfies
axioms (G₁) to (G₆) of V.4. Consequently Γ_t is representable by a pro-object called the **tamely ramified universal
covering**

<!-- original page 374 -->

of (U,X) relative to S pointed at a. The group opposite to the group of U-automorphisms of the tamely ramified universal
covering is called the **tamely ramified fundamental group** and is denoted

<!-- label: indnot:mf -->

```text
π₁^tame((U,X)/S,a), or simply π₁^tame(U,a), or even π₁^tame(U).
```

It is evidently a quotient of the fundamental group π₁(U,a) (V.6.9).

### 2.1.4.

<!-- label: XIII.2.1.4 -->

Let F be a sheaf of groups on U, let P be a right torsor with group F, and let Q be a left torsor with group F. Suppose
P and Q are tamely ramified on X relative to S. Then the same is true of P ∧^F Q. Indeed, one reduces to showing that,
if R is a discrete valuation ring with field of fractions K, if F is a finite étale group scheme over K, and if P and Q
are two torsors under F tamely ramified over R, then P ∧^F Q is also tamely ramified over R. But T = P ∧^F Q is a
quotient of P ×\_K Q. If L, M, N denote the K-algebras representing T, P, Q respectively, then L is a subalgebra of M
⊗\_K N, and it follows from XIII.2.0.3 that L is tamely ramified over R.

From the preceding one deduces that, if F is a sheaf of groups on U and if there exists a torsor with group F tamely
ramified on X relative to S, then F is tamely ramified on X relative to S. Indeed, the opposite torsor P° of P is tamely
ramified on X relative to S, since it is isomorphic to P as a sheaf of sets. If ^P F is the group obtained by twisting F
by P, one has an isomorphism

```text
F ≃ P° ∧^(^P F) P,
```

and consequently F is tamely ramified on X relative to S.

As before, one sees that, if F → F′ is a morphism of sheaves of groups on U, tamely ramified on X relative to S, and if
P is a torsor under F tamely ramified on X relative

<!-- original page 375 -->

to S, then the torsor P′ deduced from P by extension of the structural group F → F′ is tamely ramified on X relative to
S.

In particular, the canonical morphism

$$
H^{1}(U,F) \to H^{1}(U,F')
$$

restricts to a canonical morphism

$$
H^{1}_{tame}(U,F) \to H^{1}_{tame}(U,F').
$$

### 2.1.5.

<!-- label: XIII.2.1.5 -->

Let S′ → S be a morphism, and write U′, respectively X′, etc., for the inverse image of U, respectively X, etc., on S′.
If F is a sheaf of sets on U tamely ramified on X relative to S, it follows from Definition XIII.2.1.1 and from
XIII.2.0.3 that F′ is tamely ramified on X′ relative to S′.

If now F is a sheaf of groups on U, the inverse image on S′ of a torsor under F tamely ramified on X relative to S is a
torsor under F′ tamely ramified on X′ relative to S′. In particular, one has a canonical functor

<!-- label: eq:XIII.2.1.5.1 -->

$$
C_{t}((U,X)/S) \to C_{t}((U',X')/S').
$$

Suppose U and U′ are connected, and let a be a geometric point of U and a′ a geometric point of U′ above a. From the
preceding one deduces a canonical morphism

<!-- label: eq:XIII.2.1.5.2 -->

$$
\pi^{tame}_{1}(U',a') \to \pi^{tame}_{1}(U,a).
$$

If S′ → S is a morphism and h: T′ → T is the canonical projection, the morphism

$$
h*(R^{1}g_{*}F) \to R^{1}g'_{*}F'
$$

restricts to a canonical morphism

<!-- label: eq:XIII.2.1.5.3 -->

```text
h*(R¹_tame g_*F) → R¹_tame g′_*F′.
```

### 2.1.6.

<!-- label: XIII.2.1.6 -->

Let

<!-- original page 376 -->

F be a sheaf of groups on U, tamely ramified on X relative to S. With the notation of XIII.2.1.2, one has canonical
exact sequences:

<!-- label: eq:XIII.2.1.6.1 -->

```text
1 → H¹(X,i_*F) → H¹_tame(U,F) → H⁰(X,R¹_tame i_*F),

1 → R¹f_*(i_*F) → R¹_tame g_*F → f_*(R¹_tame i_*F).
```

The first is obtained from the exact sequence (SGA 4 III 3.2)

$$
1 \to H^{1}(X,i_{*}F) \to H^{1}(U,F) \to H^{0}(X,R^{1}i_{*}F).
$$

Indeed, it is enough to show that the image of H¹(X,i\*\*F) in H¹(U,F) is in fact contained in H¹_tame(U,F), and that
the image of H¹_tame(U,F) in H⁰(X,R¹i\*\*F) is in fact contained in H⁰(X,R¹*tame i**F). But the inverse image on U of a
torsor under i**F is a torsor under i*i\*\*F which is evidently tamely ramified on X relative to S; hence the same is
true after extension of the structural group i*i*\*F → F. This proves the existence of the arrow H¹(X,i\*\*F) →
H¹\*tame(U,F). The fact that the image of H¹_tame(U,F) in H⁰(X,R¹i**F) is contained in H⁰(X,R¹\*tame i**F) follows at
once from the definition of R¹\*tame i\*\*F. This proves the existence of the first exact sequence, and the second is
deduced from it by localization.

### 2.2.

<!-- label: XIII.2.2 -->

We keep the notation of XIII.2.1. We shall define a notion of tamely ramified object of a stack Φ on U when this stack
is given, locally **on** X and on S for the étale topology, as the **inverse image of a stack** Ψ **on** S.

First let G be a gerbe on U, and suppose given a surjective étale morphism S₁ → S, a surjective étale morphism X₂ → X
×\_S S₁, a trivial gerbe H on S₁, and an isomorphism

$$
G|U_{2} \to H|U_{2},
$$

where

<!-- original page 377 -->

U₁ = U ×\_X X₁ and U₂ = U ×\_X X₂. When one chooses a trivialization of H|X₂, the isomorphism above identifies G|U₂ with
the stack of torsors under a sheaf of groups F. One says that an element x of G_U is tamely ramified on X relative to S
if the restriction of x to U₂ is a torsor tamely ramified on X relative to S. By XIII.2.1.4, this notion does not depend
on the way in which H|X₂ has been trivialized.

Now let Φ be a stack on U, and suppose given a surjective étale morphism S₁ → S, a surjective étale morphism X₂ → X ×\_S
S₁, a stack Ψ on S₁, and an isomorphism

$$
i: \Phi|U_{2} \to \Psi|U_{2}.
$$

Let x be an element of Φ_U, let G_x be the maximal subgerbe of Φ generated by x [XIII.1, III 2.1.7], and let SΦ be the
sheaf of maximal subgerbes of Φ. The isomorphism i induces an isomorphism

$$
S\Phi|U_{2} \to S\Psi|U_{2}.
$$

It follows from XIII.5.7 that, after replacing S₁ by a surjective étale extension if necessary, one has a unique maximal
subgerbe H of Ψ, which may be supposed trivial, such that i defines an isomorphism

$$
G_{x}|U_{2} \to H|U_{2}.
$$

One says that the element x is tamely ramified on X relative to S if it is so as an element of G_x endowed with the
isomorphism above.

### 2.2.1.

<!-- label: XIII.2.2.1 -->

Let Φ be a stack on U given, locally on X and S, as the inverse image of a stack on S, and let

```text
U --i→ X
 \    |
  \   f
   g  |
    \ |
      T
```

be a diagram as in XIII.2.1.2. For every scheme $T'$ étale over $T$, if $U' = U \times_{T} T'$, consider the subset
$(g^{tame}_{*} \Phi)_{T}'$

<!-- label: indnot:mg -->

of $(g_{*}\Phi)_{T}' = \Phi_{U}'$ formed

<!-- original page 378 -->

by the elements of Φ_U′ which are tamely ramified on X relative to S. The **tamely ramified direct image** of Φ by g,
denoted

$$
g^{tame}_{*} \Phi,
$$

is the full subcategory of $g_{*}\Phi$ whose objects over a scheme $T'$ étale over $T$ are the elements of
$(g^{tame}_{*} \Phi)_{T}'$. It is clear that $g^{tame}_{*} \Phi$ is a substack of $g_{*}\Phi$.

### 2.2.2.

<!-- label: XIII.2.2.2 -->

By reduction to the case of a stack of torsors, one sees that, if Φ is a stack on U which is locally for the étale
topology of S and X the inverse image of a stack on S, the canonical morphism

$$
h*(g_{*}\Phi) \to g'_{*}\Phi'
$$

restricts to a canonical morphism

```text
h*(g_*^tame Φ) → g′_*^tame Φ′.
```

**Remarks.**

<!-- label: XIII.2.3 -->

a. If F is a locally constant constructible sheaf of sets on U, then for F to be tamely ramified on X relative to S, it
is enough that the condition of XIII.2.1.1 be satisfied for the geometric points of S above the maximal points of S. To
see this, one may suppose the divisor D strictly with normal crossings. The sheaf F is representable by an étale
covering V of U. If s̄ is a geometric point of S and y is a maximal point of Y_s̄, write S̄ for the strict localization of
S at s̄, X̄ for the strict localization of X at ȳ, Ū = U ×\_X X̄, and V̄ = V ×\_X X̄. If the condition of XIII.2.1.1 is
satisfied at the geometric points above the maximal points of S, it follows from XIII.5.5 below that V̄ is a covering of
Ū tamely ramified on X̄ relative to S̄. Consequently V is an étale covering of U tamely ramified on X relative to S.

b.

<!-- original page 379 -->

Let F be a sheaf of groups on U tamely ramified on X relative to S. If s̄ is a geometric point of S and y is a maximal
point of Y_s̄, write K for the field of fractions of 𝒪_X_s̄,y. Suppose that, for every s̄ and every y, the K-algebra L
whose spectrum represents F|K has rank prime to the residual characteristic p of 𝒪_X_s̄. We shall sometimes say, by abuse
of language, that F is prime to the residual characteristics of S. When this holds, every torsor P under F is tamely
ramified on X relative to S.

Indeed, let R̄ be the strict localization of 𝒪_X_s̄,y at ȳ, let K̄ be its field of fractions, and let F̄ be the inverse
image of F on K̄. Let us show that one may suppose F constant. Since F is tamely ramified on X relative to S, F̄ is
representable by the spectrum of a K̄-algebra L = ∏ L_i, where the L_i are extensions of K̄ of degree prime to p. One can
therefore find an extension K′ of K̄ of degree prime to p such that F̄|K′ is a constant sheaf. By XIII.2.0.3, to prove
that P|K̄ is tamely ramified over R̄, it is enough to see that P|K′ is tamely ramified over the integral closure of R̄ in
K′; this gives the reduction to the case where F̄ is constant. Suppose from now on that F̄ is constant. The K̄-algebra H
representing P|K̄ is then a product of mutually isomorphic extensions H_i of K̄. Since the rank of H is prime to p, so is
[H₁:K̄], which proves that H is tamely ramified on X relative to S.

c. Let X be a regular scheme, let D be a divisor with normal crossings on X (SGA 5 I 3.1.5), let U = X − Supp D, and let
F be a sheaf of sets on U. If y is a maximal point of Supp D, write K for the field of fractions of 𝒪_X,y. One says that
F is **tamely ramified relative to D** if, for every maximal point y of Supp D, F|K is representable by a K-algebra
tamely ramified over 𝒪_X,y.

**Theorem.**

<!-- label: XIII.2.4 -->

Let

<!-- original page 380 -->

f: X → S be an S-scheme, let D be a divisor on X with normal crossings relative to S (XIII.2.1), let Y = Supp D, let U =
X − Y, and let i: U → X be the canonical immersion. Let F be a sheaf of sets, respectively of groups, on U, satisfying
one of the following conditions:

a. F is locally for the étale topology **on** X and on S the inverse image of a sheaf of sets, respectively a
constructible sheaf of groups, on S.

b. F is locally constant constructible on U and tamely ramified on X relative to S.

Then the following conclusions hold:

1. $(F,i)$ is cohomologically proper relative to $S$ in dimension ≤ 0; respectively, for every morphism $h: S' \to S$,
   if $i': U' \to X'$ is the inverse image of $i$ on $S'$, if $F' = F|U'$, and if $k = h_{X}$, the canonical morphism

```text
Ψ: k*(R¹_tame i_*F) → R¹_tame i′_*F′
```

is an isomorphism.

If F is a sheaf of groups prime to the residual characteristics of S (XIII.2.3 b), tamely ramified on X relative to S,
then (F,i) is cohomologically proper relative to S in dimension ≤ 1.

1. If F is a constructible sheaf of sets, respectively of groups, then i\*\*F, respectively R¹_tame i\*\*F, is
   constructible.

**Proof.** For every S-scheme S′, consider the following diagram, all of whose squares are cartesian:

```text
U′ → U
|     |
i′    i
|     |
X′ → X
|     |
S′ → S.
```

Since

<!-- original page 381 -->

the question is local on X for the étale topology, one may suppose that D is a divisor strictly with normal crossings
relative to S (XIII.2.1). Moreover, after restricting X to a neighborhood of Y if necessary, one may suppose X smooth
over S.

**Proof of XIII.2.4 1.**

### 2.4.1.

<!-- label: XIII.2.4.1 -->

**Case of a sheaf of sets satisfying a.** We may suppose that F = g\*G, where G is a sheaf on S. It then follows from
SGA 4 XVI 3.2 that the canonical morphism

<!-- label: eq:XIII.2.4.1.1 -->

$$
f*G \to i_{*}F
$$

is an isomorphism. For every $S$-scheme $h: S' \to S$, one likewise has an isomorphism $f'*G' \to i'_{*}F'$;
consequently the canonical morphism

$$
\phi: k*(i_{*}F) \to i'_{*}F'
$$

identifies with the natural isomorphism

$$
k*f*G \simeq f'*G'.
$$

### 2.4.2.

<!-- label: XIII.2.4.2 -->

**Case of a sheaf of sets satisfying b.** We must show that φ is an isomorphism, and it is enough to check this at every
geometric point x̄′ of X′. Let S̄, respectively X̄, S̄′, X̄′, be the strict localization of S, respectively X, S′, X′, at x̄′,
and put Ū = U\*(X̄), Ū′ = U\*(X̄′), etc. The morphism φ_x̄ identifies with the canonical morphism

$$
\bar{\phi}: H^{0}(\bar{U},\bar{F}) \to H^{0}(\bar{U}',\bar{F}').
$$

One can find a principal covering V of Ū of the type occurring in XIII.5.4 such that the inverse image of F̄ on V is a
constant sheaf with value C. If Π is the Galois group of V over Ū, Π acts on F̄|V, and one has

<!-- label: eq:XIII.2.4.2.1 -->

$$
H^{0}(\bar{U},\bar{F}) \simeq H^{0}(V,C_{V})^{\Pi},
$$

where the second member denotes the set of elements of H⁰(V,C_V) invariant

<!-- original page 382 -->

under Π. Since V′ = V ×\_Ū Ū′ is a principal covering of Ū′ with Galois group Π′ ≃ Π, one sees that the morphism φ̄ is
obtained, by taking invariants under Π, from the canonical morphism

$$
H^{0}(V,C_{V}) \to H^{0}(V',C_{V}').
$$

Since V and V′ are connected (XIII.5.4), this morphism, and hence also φ̄, is an isomorphism.

Notice that if moreover F is a sheaf of groups and if P is a torsor on Ū with group F̄, tamely ramified relative to D, it
follows from the preceding proof and from XIII.2.2 that (^P F̄,ī) is cohomologically proper relative to S in dimension ≤
0.

### 2.4.3.

<!-- label: XIII.2.4.3 -->

**Case of a sheaf of groups.** To show that Ψ is an isomorphism, it is enough to prove that, for every geometric point
ȳ′ of Y′, the morphism

```text
Ψ_ȳ′: (k*(R¹_tame i_*F))_ȳ′ → (R¹_tame i′_*F′)_ȳ′
```

is an isomorphism. But, by XIII.2.1.2, Ψ_ȳ′ identifies with the canonical morphism

$$
\bar{\Psi}: H^{1}_{tame}(\bar{U},\bar{F}) \to H^{1}_{tame}(\bar{U}',\bar{F}').
$$

Let Ũ be the tamely ramified universal covering of Ū (XIII.2.1.3), and let F̃ be the inverse image of F̄ on Ũ. It follows
from XIII.5.7 in case a and from XIII.5.5 in case b that H¹_tame(Ū,F̄) identifies with the subset of H¹(Ū,F̄) formed by
the classes of F̄-torsors whose inverse image on Ũ is trivial. On the other hand, a classical argument (cf. IX.5, p. 300)
shows that the set of elements of H¹(Ū,F̄) whose inverse image on Ũ is trivial identifies with

$$
H^{1}(\pi^{tame}_{1}(\bar{U}), H^{0}(\tilde{U},\tilde{F})).
$$

Thus one obtains a canonical isomorphism

<!-- label: eq:XIII.2.4.3.1 -->

$$
H^{1}_{tame}(\bar{U},\bar{F}) \simeq H^{1}(\pi^{tame}_{1}(\bar{U}), H^{0}(\tilde{U},\tilde{F})).
$$

Consequently the morphism Ψ̄ identifies with the canonical morphism

$$
H^{1}(\pi^{tame}_{1}(\bar{U}), H^{0}(\tilde{U},\tilde{F}))
  \to H^{1}(\pi^{tame}_{1}(\bar{U}'), H^{0}(\tilde{U}',\tilde{F}')).
$$

Let us show

<!-- original page 383 -->

that this morphism is an isomorphism. The morphism π₁^tame(Ū′) → π₁^tame(Ū) is an isomorphism by XIII.5.6, and the same
is true of the morphism H⁰(Ũ,F̃) → H⁰(Ũ′,F̃′). Indeed, this is evident in case b, since F̃ is constant and Ũ and Ũ′ are
connected. In case a, let Ḡ be a constructible sheaf of groups on S̄ such that F̄ = ḡ\*Ḡ. Since the morphisms Ũ → S̄ and Ũ′
→ S̄′ are 0-acyclic (XIII.5.7), one has

```text
H⁰(Ũ,F̃) ≃ H⁰(S̄,Ḡ) ≃ H⁰(S̄′,Ḡ′) ≃ H⁰(Ũ′,F̃′),
```

which implies that Ψ is an isomorphism. The last assertion of XIII.2.4 1 follows from the preceding, taking XIII.2.3 b
into account.

**Proof of XIII.2.4 2.**

The case of a constructible sheaf of sets satisfying a follows at once from (XIII.2.4.1.1). Let $F = g*G$ be a sheaf of
groups satisfying a, where $G$ is a constructible sheaf. We may suppose $S$ affine. Let $(S_{j})_{j}\in J$ be a finite
family of reduced closed subschemes of $S$ whose union covers $S$, such that the inverse image of $G$ on $S_{j}$ is
locally constant. Taking XIII.2.4 1 into account, to establish that $R^{1}_{tame} i_{*}F$ is constructible, it is enough
to see that it becomes so after the base change $S_{j} \to S$ for each $j \in J$. We are therefore reduced to case b,
where $F$ is locally constant.

From now on suppose that F is a sheaf of sets or groups satisfying b. Since the question is local for the étale topology
on X, one may suppose X of finite presentation over S, and, by passage to the limit, one may suppose X and S noetherian.

Let $D = \sum_{1\leq i\leq r} divisor f_{i}$, where, for each point $x$ of `Supp D`, if $I(x)$ is the set of $i$ such
that $f_{i}(x) = 0$, the subscheme $V((f_{i})_{i}\in I(x))$ is smooth over $S$ of codimension `card I(x)` in $X$. Let
$\mathcal{P}$ be the set of subsets of `[1,r]`, and for each $I \in \mathcal{P}$ put

```text
X_I = (⋂_{i∈I} V(f_i)) ∩ (⋂_{i∉I} X_{f_i}).
```

Let

<!-- original page 384 -->

z be a point of X_I. After first restricting to an étale neighborhood of z, one can find an open W of X containing z and
a principal covering V of U ∩ W, tamely ramified on W relative to S, of the type considered in XIII.5.6.1, such that the
inverse image of F on V is a constant sheaf with value C. Let π be the Galois group of the covering V. For every
geometric point x̄ of X_I, one then has, by (XIII.2.4.2.1),

$$
H^{0}(\bar{U},\bar{F}) \simeq H^{0}(V,C_{V})^{\pi}.
$$

It follows that i\*\*F|X_I∩W is locally constant (SGA 4 IX 2.13), and hence that i\*\*F is constructible.

Finally let us show that if F is a locally constant sheaf of groups, R¹*tame i*\*F|X_I is constructible. If x̄ is a
geometric point of X, we obtained in (XIII.2.4.3.1) the expression

$$
H^{1}_{tame}(\bar{U},\bar{F}) \simeq H^{1}(\pi^{tame}_{1}(\bar{U}), H^{0}(\tilde{U},\tilde{F})).
$$

If p is the residual characteristic of X̄, then, by XIII.5.6,

```text
π₁^tame(Ū) = ∏_{ℓ≠p} ℤ_ℓ(1)^card I.
```

Let ℒ be the set of prime numbers dividing the order of the finite group H⁰(Ũ,F̃), and let

```text
K = ∏_{ℓ∈ℒ, ℓ≠p} ℤ_ℓ(1)^card I.
```

It follows from [XIII.4, I §5 ex. 2] that

$$
H^{1}_{tame}(\bar{U},\bar{F}) \simeq H^{1}(K,H^{0}(\tilde{U},\tilde{F})).
$$

Since K is topologically of finite type and H⁰(Ũ,F̃) is finite, it follows first that the fibers of the sheaf R¹*tame
i\*\*F|X*I are finite. On the other hand, the set ℒ does not depend on the point x̄. For every q ∈ ℒ, let X_I,q be the
closed subset of X_I with equation q = 0, and let X_I′ be the open subset of X_I complementary to the union of the
X_I,q. Then R¹_tame i\**F|X*I,q and R¹_tame i\*\*F|X_I′ are locally constant: indeed, a specialization arrow of
geometric points of X_I,q, respectively of X_I′, induces an isomorphism on the groups K (XIII.5.6.1), hence also on the
sets H¹_tame(Ū,F̄), and one may apply SGA 4 IX 2.13.

**Corollary.**

<!-- label: XIII.2.5 -->

Let

<!-- original page 385 -->

f: X → S be a morphism, let D be a divisor on X with normal crossings relative to S (XIII.2.1), let Y = Supp D, let U =
X − Y, and let i: U → X be the canonical immersion. Let Φ be a stack on U and suppose given surjective étale morphisms
S₁ → S and X₂ → X ×\_S S₁, a stack Ψ on S₁, and an isomorphism Φ|U₂ ≃ Ψ|U₂; cf. XIII.2.2.

Then, for every morphism $h: S' \to S$, if $k = h_{X}$, the canonical functor

$$
\phi: k*i_{*}\Phi \to i'_{*}\Phi'
$$

is fully faithful. If Ψ is constructible, the canonical functor

```text
ψ: k*i_*^tame Φ → i′_*^tame Φ′
```

is an equivalence of categories.

Moreover, if the stack Ψ is constructible, respectively if Ψ is 1-constructible (XIII.0) and S is locally noetherian,
then i\*\*Φ is constructible, respectively i\*\*^tame Φ is 1-constructible.

Let us show that φ is fully faithful. It is enough to see that, for every geometric point x̄′ of X′, the same is true of
the functor

$$
\bar{\phi}: \Phi(\bar{U}) \to \Phi'(\bar{U}'),
$$

where we have resumed the notation of XIII.2.4.2. Let a, b be two elements of Φ(Ū), and let a′, b′ be their images by φ̄.
Since the morphism Ū → S̄ is locally 0-acyclic (XIII.5.7), one has an isomorphism

$$
H^{0}(\bar{U},S\bar{\Phi}) \simeq H^{0}(\bar{S},S\bar{\Psi}).
$$

Consequently a and b come by inverse image from elements of Ψ, and the same is therefore true of F = SheafHom_Ū(a,b).
Since the sheaf F′ = SheafHom_Ū′(a′,b′) is the inverse image of F on Ū′, it follows from XIII.2.4.1 that the canonical
morphism

$$
H^{0}(\bar{U},F) \to H^{0}(\bar{U}',F')
$$

is an isomorphism, which proves that φ̄ is fully faithful.

Let us show

<!-- original page 386 -->

that, for every geometric point x̄′ of X′, the functor

```text
ψ̄: i_*^tame Φ(X̄′) → i′_*^tame Φ′(X̄′)
```

is an equivalence. By what precedes, ψ̄ is fully faithful. Let us show that ψ̄ is essentially surjective. Let a′ be an
element of Φ′(Ū′) tamely ramified on X′ relative to S′ (XIII.2.2), and let us show that it is the image of a tamely
ramified element of Φ(Ū). It follows from XIII.2.4 1 that the canonical morphism

$$
H^{0}(\bar{U},S\bar{\Phi}) \to H^{0}(\bar{U}',S\bar{\Phi}')
$$

is an isomorphism. Let G′ be the maximal subgerbe of Φ′ generated by a′. There exists a maximal subgerbe G of Φ̄, inverse
image of a gerbe on S̄, such that

$$
\bar{m}*G \simeq G',
$$

where m is the morphism Ū′ → Ū. The canonical functor

<!-- label: eq:XIII.2.5.* -->

```text
(*)   k̄*ī_*^tame G → ī′_*^tame G′
```

is an equivalence, because G identifies with a gerbe of torsors under a constructible sheaf of groups coming from S̄, and
one can apply XIII.2.4 1. It then follows from (\*) that there exists an element a of G(Ū), tamely ramified on X
relative to S, whose inverse image on Ū′ is a′. This proves that ψ is an equivalence.

If $\Psi$ is constructible, then so is $i_{*}\Phi$. Indeed, an object $x$ of $i_{*}\Phi$ is, locally for the étale
topology of $S$, the inverse image of an object $y$ of $\Psi$; it therefore follows from (XIII.2.4.1.1) that
$SheafAut(x)$ is the inverse image of $SheafAut(y)$, and hence is constructible. Finally, if $\Psi$ is 1-constructible,
then $i^{tame}_{*} \Phi$ is also 1-constructible by XIII.6.3 below.

**Corollary.**

<!-- label: XIII.2.6 -->

The

<!-- original page 387 -->

notation is that of XIII.2.4. Suppose that S has characteristic zero at every point s such that Y_s ≠ ∅. Then, if 𝓕 is a
locally constant constructible sheaf of groups on U, respectively a constructible stack on U which is locally on X and S
the inverse image of a constructible stack on S, the pair (𝓕,i) is cohomologically proper relative to S in dimension ≤
1\.

Since every constructible sheaf of sets on U is tamely ramified on X relative to S, the corollary follows from XIII.2.4,
respectively XIII.2.5.

**Corollary.**

<!-- label: XIII.2.7 -->

The notation is that of XIII.2.4, but in addition one is given an S-scheme T and a proper morphism p: X → T, and X and T
are assumed of finite presentation over S. Let q = pi. Let 𝓕 be a constructible sheaf of sets on U satisfying one of
conditions a or b of XIII.2.4, respectively a sheaf of groups satisfying one of conditions a, b of XIII.2.4,
respectively a stack on U which is locally on X and S the inverse image of a constructible stack G on S. Then the
following conclusions hold:

1. $(\mathcal{F},q)$ is cohomologically proper relative to $S$ in dimension ≤ 0; respectively, for every morphism
   $h: S' \to S$, if $m = h_{T}$, the canonical morphism

```text
Θ: m*(R¹_tame q_*𝓕) → R¹_tame q′_*𝓕′
```

is an isomorphism; respectively, for every morphism S′ → S, the canonical morphism

```text
ξ: m*(q_*^tame 𝓕) → q′_*^tame 𝓕′
```

is an equivalence.

1. The sheaf $q_{*}\mathcal{F}$, respectively the sheaf $R^{1}_{tame} q_{*}\mathcal{F}$, respectively the stack
   $q^{tame}_{*} \mathcal{F}$, is constructible. In the last case, if $S$ is assumed locally noetherian and $G$ is
   1-constructible, then $q^{tame}_{*} \mathcal{F}$ is also 1-constructible.

<!-- original page 388 -->

The first part follows at once from XIII.2.4, XIII.2.5, and the proof of XIII.1.8. Let us prove 2. If $\mathcal{F}$ is a
constructible sheaf of sets on $U$ satisfying XIII.2.4 a or XIII.2.4 b, it follows from XIII.2.4 2 that
$i_{*}\mathcal{F}$ is constructible; hence the same is true of $q_{*}\mathcal{F} = p_{*}(i_{*}\mathcal{F})$ (SGA 4 XIV
1.1).

Let 𝓕 be a constructible sheaf of groups on U satisfying XIII.2.4 a or XIII.2.4 b, and let us prove that R¹*tame q*\*𝓕
is constructible. By passage to the limit (EGA IV 8.10.5 and 17.7.8) and using 1, one may suppose S noetherian. Let Φ be
the stack on X whose fiber over every scheme X′ étale over X is formed by the torsors on U′ = U ×\_X X′, with group 𝓕|U,
that are tamely ramified on X relative to S. Thus one has

```text
S(i_*^tame Φ) ≃ R¹_tame i_*𝓕,
```

and this sheaf is constructible by XIII.2.4 2. \[Translator note: the source correction says the reference here was
wrong in the older text.\] It follows from XIII.6.3 below that S(p\*\*Φ) is constructible, that is, that R¹_tame q\*\*𝓕
is constructible.

Finally, if $\mathcal{F}$ is a stack on $U$ which is locally on $X$ and $S$ the inverse image of a constructible stack
on $S$, then $i^{tame}_{*} \mathcal{F}$ is constructible, and hence so is
$q^{tame}_{*} \mathcal{F} = p_{*}(i^{tame}_{*} \mathcal{F})$. If in addition $S$ is locally noetherian and `SG` is
constructible, then $S(i^{tame}_{*} \mathcal{F})$ is constructible by XIII.6.3; hence the same is true of
$S(q_{*}i^{tame}_{*} \mathcal{F})$, that is, of $S(q^{tame}_{*} \mathcal{F})$, by XIII.6.2.

**Corollary.**

<!-- label: XIII.2.8 -->

Let

```text
U --i→ X
 \    |
  \   f
   g  |
    \ |
      S
```

be a commutative diagram of schemes in which U is the open complement

<!-- original page 389 -->

in X of a divisor with normal crossings relative to S, and f is a **proper** morphism of finite presentation. Let ℒ be a
set of prime numbers. Suppose g is locally 0-acyclic, respectively locally 1-aspherical for ℒ. Then, if 𝓕 is a sheaf of
sets on U, respectively a sheaf of ℒ-groups on U, locally constant constructible and tamely ramified on X relative to S,
f\*\*𝓕, respectively R¹_tame f\*\*𝓕, is locally constant constructible and (𝓕,f) is cohomologically proper relative to S
in dimension ≤ 0; respectively, the formation of R¹\*tame f\*\*𝓕 commutes with every base change S′ → S. In the
non-respective case, if 𝓕 is a sheaf of groups, then for every specialization s̄₁ → s̄₂ of geometric points of S, the
specialization morphism

```text
(R¹_tame f_*𝓕)_s̄₂ → (R¹_tame f_*𝓕)_s̄₁
```

is injective.

The corollary follows at once from XIII.2.6 and XIII.1.14, respectively from the analogue of XIII.1.14 for R¹*tame
f*\*𝓕, which is proved as in loc. cit.

**Corollary.**

<!-- label: XIII.2.9 -->

Let

```text
U --i→ X
 \    |
  \   f
   g  |
    \ |
      S
```

be a commutative diagram of schemes in which $U$ is the open complement in $X$ of a divisor with normal crossings
relative to $S$, and $f$ is a proper smooth morphism of finite presentation. Let $\mathcal{L}$ be the set of prime
numbers distinct from the residual characteristics of $S$. Let $\mathcal{F}$ be a locally constant constructible sheaf
of $\mathcal{L}$-groups on $U$, tamely ramified on $X$ relative to $S$. Then $R^{1}f_{*}\mathcal{F}$ is locally constant
constructible and $(\mathcal{F},f)$ is cohomologically proper relative

<!-- original page 390 -->

to S in dimension ≤ 1.

The corollary follows from XIII.2.8 and from the fact that $R^{1}_{tame} f_{*}\mathcal{F} = R^{1}f_{*}\mathcal{F}$
(XIII.2.3 b).

### 2.10.

<!-- label: XIII.2.10 -->

If U is a connected scheme, a is a geometric point of U, and ℒ is a set of prime numbers, write

<!-- label: eq:XIII.2.10.0 -->

<!-- label: indnot:mi -->

$$
\pi^{\mathcal{L}}_{1}(U,a)
$$

for the projective limit of the finite quotients of π₁(U,a) whose orders have all their prime factors in ℒ.

We shall define specialization morphisms for the fundamental group, generalizing X.2.

Let g: U → S be a coherent morphism with geometrically connected fibers; respectively, let g be of the form g = fi,
where f: X → S is a proper morphism of finite presentation and i: U → X is an open immersion such that U is the
complement in X of a divisor with normal crossings relative to S (cf. XIII.2.8). Let ℒ be a set of prime numbers and
suppose, in the non-respective case, that for every finite constant ℒ-group C, the pair (C_U,g) is cohomologically
proper relative to S in dimension ≤ 1. Let s̄₁ → s̄₂ be a specialization morphism of geometric points of S, let S̄ be the
strict localization of S at s̄₂, and let Ū = U ×\_S S̄. One has a commutative diagram

```text
U_s̄₁ → Ū ← U_s̄₂
  |      |     |
 s̄₁  → S̄ ← s̄₂.
```

If a₁ is a geometric point of U_s̄₁ and a₂ a geometric point of U_s̄₂, the two morphisms define canonical morphisms

```text
π₁: π₁^ℒ(U_s̄₁,a₁) → π₁^ℒ(Ū,a₁),
π₂: π₁^ℒ(U_s̄₂,a₂) → π₁^ℒ(Ū,a₂),
```

respectively

<!-- original page 391 -->

```text
π₁: π₁^tame(U_s̄₁,a₁) → π₁^tame(Ū,a₁),
π₂: π₁^tame(U_s̄₂,a₂) → π₁^tame(Ū,a₂).
```

See V.7 and (XIII.2.1.5.2). The hypotheses of cohomological properness, respectively XIII.2.8, prove that π₂ is an
isomorphism. If one chooses a path class from a₁ to a₂, one obtains an isomorphism

$$
\pi_{12}: \pi^{\mathcal{L}}_{1}(\bar{U},a_{1}) \simeq \pi^{\mathcal{L}}_{1}(\bar{U},a_{2}),
$$

respectively

$$
\pi_{12}: \pi^{tame}_{1}(\bar{U},a_{1}) \simeq \pi^{tame}_{1}(\bar{U},a_{2}),
$$

[Translator note: the corrected source notes that the last isomorphism had been written only as a morphism.] hence a
morphism π = π₂⁻¹π₁₂π₁:

```text
π: π₁^ℒ(U_s̄₁,a₁) → π₁^ℒ(U_s̄₂,a₂),
```

respectively

```text
π: π₁^tame(U_s̄₁,a₁) → π₁^tame(U_s̄₂,a₂).
```

Changing the path class from a₁ to a₂ modifies π by an inner automorphism of π₁^ℒ(X_s̄₂,a₂), respectively of
π₁^tame(X_s̄₂,a₂). One calls one of the morphisms defined above the **specialization morphism for the fundamental group**
associated with the morphism s̄₁ → s̄₂, and writes simply

```text
π: π₁^ℒ(X_s̄₁) → π₁^ℒ(X_s̄₂),
```

respectively

```text
π: π₁^tame(X_s̄₁) → π₁^tame(X_s̄₂).
```

**Lemma.**

<!-- label: XIII.2.11 -->

Let f: X → S be a proper morphism of finite presentation, let D be a divisor on X with normal crossings relative to S,
let Y = Supp D, let U = X − Y, let i: U → X be the canonical morphism, let s̄₁ → s̄₂ be a specialization morphism of
geometric points of S, and let y₁ be a geometric point of Y_s̄₁ and y₂ a geometric point of Y_s̄₂ such that the projection
z₁ of y₁ on X is a generization of the projection z₂ of y₂. Let I_y₁ be an inertia subgroup of π₁^tame(U_s̄₁) at y₁. Then
the image of I_y₁ by the specialization morphism

```text
π: π₁^tame(U_s̄₁) → π₁^tame(U_s̄₂)
```

is

<!-- original page 392 -->

an inertia subgroup of π₁^tame(U_s̄₂) at y₂.

Indeed, let X̄, respectively X̃, be the strict localization of X at y₂, respectively at y₁, and let Ū = U ×\_X X̄,
respectively Ũ = U ×\_X X̃. There is a canonical morphism Ũ → Ū, and it follows from XIII.1.10 that one has a commutative
diagram

```text
π₁^tame(Ũ_s̄₁) → π₁^tame(Ū_s̄₂)
      ↓                 ↓
π₁^tame(U_s̄₁) → π₁^tame(U_s̄₂),
```

where the upper horizontal morphism π′ is the composite of the canonical morphism π₁^tame(Ũ_s̄₁) → π₁^tame(Ū_s̄₁) and the
specialization morphism. Since π₁^tame(Ũ_s̄₁), respectively π₁^tame(Ū_s̄₁), is an inertia group of π₁^tame(U_s̄₁) at y₁,
respectively of π₁^tame(U_s̄₂) at y₂, it is enough to prove that π′ is surjective. This follows from the expression
obtained in XIII.5.6.

**Corollary.**

<!-- label: XIII.2.12 -->

Let X be a connected proper smooth curve of genus g over a separably closed field k of characteristic p ≥ 0. Let U be
the open subset obtained by removing from X n distinct closed points a₁, …, a_n. Then the tamely ramified fundamental
group π₁^tame(U) (XIII.2.1.3) can be generated by 2g + n elements x_i, y_i, σ_j, with 1 ≤ i ≤ g and 1 ≤ j ≤ n, such that
σ_j is a generator of an inertia group corresponding to a_j and one has the relation

<!-- label: eq:XIII.2.12.* -->

```text
(*)   ∏_{1≤i≤g}(x_i y_i x_i⁻¹ y_i⁻¹) · ∏_{1≤j≤n} σ_j = 1.
```

For every finite group G **of order prime to** p, generated by elements x̄_i, ȳ_i, σ̄_j satisfying relation (\*), there
exists an étale covering of U with group G, corresponding to a homomorphism π₁^tame(U) → G which

<!-- original page 393 -->

sends x_i, y_i, σ_j to x̄_i, ȳ_i, σ̄_j respectively. In other words, if p′ denotes the set of prime numbers distinct from
p, π₁^p′(U) is the pro-p′ group generated by the generators x_i, y_i, σ_j subject to the single relation (\*).

**Proof.** We may suppose $k$ algebraically closed. First suppose $k$ has characteristic zero. There then exists an
algebraically closed subextension $k'$ of $k$, of finite transcendence degree over $\mathbb{Q}$, such that $X$ comes by
extension of scalars from a proper smooth curve $X'$ defined over $k'$, and one may suppose that the points
$a_{1}, \cdots, a_{n}$ come from rational points $a'_{1}, \cdots, a'_{n}$ of $X'$. Since $k'$ has finite transcendence
degree over $\mathbb{Q}$, one can find an embedding of $k'$ into the field of complex numbers $\mathbb{C}$. Let
$\tilde{U} = U' \times_{k}' \mathbb{C}$. Let $k''$ be an algebraically closed extension of $k'$ such that there are
$k'$-morphisms from $k$ and from $\mathbb{C}$ to $k''$. If $g': U' \to k'$ is the structural morphism, and if
$\mathcal{F}$ is a finite constant sheaf of groups on $U''$, it follows from XIII.2.9 that the specialization morphisms

$$
(R^{1}g'_{*}\mathcal{F}')_{\mathbb{C}} \to (R^{1}g'_{*}\mathcal{F}')_{k}'' \leftarrow (R^{1}g'_{*}\mathcal{F}')_{k}
$$

are isomorphisms. In terms of fundamental groups, this shows that one has an isomorphism, defined up to inner
automorphism,

$$
\pi_{1}(U) \to \pi_{1}(\tilde{U}),
$$

and it is clear that this isomorphism transforms an inertia group relative to a point of X′ − U′ into an inertia group
relative to the same point. We may therefore suppose k = ℂ. In this last case, it follows from the Riemann existence
theorem (XII.5.2) that the fundamental group π₁(U) is nothing other than the completion, for the topology of subgroups
of finite index, of the fundamental group of the analytic space associated with U. But the latter can be computed
transcendently \[XIII.3, ch. 7, §47\]:

<!-- original page 394 -->

it can be generated by 2g + n elements x_i, y_i, σ_j such that σ_j is the image of a generator of the local fundamental
group π₁(D_j) of a small disk centered at a_j, that is, a generator of an inertia group corresponding to the point a_j,
these elements satisfying the single relation (\*).

Now suppose k has characteristic p > 0. One can find a complete discrete valuation ring A, with residue field k and
field of fractions K of characteristic zero, and a connected scheme X₁, proper and smooth over S = Spec A, such that X₁
×\_S Spec k ≃ X (III.7.4). The points a_j then lift to sections s_j of X₁ over S. Let Y₁j be the reduced closed
subscheme with underlying space s_j(S), let Y₁ be the union of the Y₁j, let U₁ = X₁ − Y₁, and let g₁: U₁ → S be the
structural morphism. Let K̄ be an algebraically closed extension of K and let Ū = U₁ ×\_S K̄. If C is a finite constant
group, it follows from XIII.2.8 that the specialization morphism

```text
(R¹g₁*C_U₁)_k → (R¹g₁*C_U₁)_K̄
```

is injective, and even bijective if C has order prime to p. In terms of fundamental groups, this means that the
specialization morphism (XIII.1.10)

$$
\pi: \pi_{1}(\bar{U}) \to \pi^{tame}_{1}(U)
$$

is surjective, and that the specialization morphism

$$
{\pi^{p}_{1}}'(\bar{U}) \to {\pi^{p}_{1}}'(U)
$$

is bijective. Finally, if x_i, y_i, σ_j are generators of π₁(Ū) such that σ_j is a generator of an inertia group
corresponding to the point b_j = Y₁j(K̄) of X̄, then by XIII.1.11, π(σ_j) is a generator of an inertia group corresponding
to a_j. This completes the proof.

**Remark (M. Raynaud, added in 2003).**

<!-- label: XIII.2.13 -->

Let k be an algebraically closed field of characteristic p > 0, let X be a connected proper smooth algebraic curve over
k of genus g, and let U be an affine open of X, the complement of r ≥ 1 rational points of X. One has the fundamental
group π₁(U), its quotient π₁^tame(U), which classifies finite étale coverings of U tamely ramified at the points of X −
U, and the quotient π₁^p′(U) of π₁^tame(U), which classifies Galois étale coverings of U with Galois group of order
prime to p.

In “Coverings of algebraic curves,” Amer. J. Math. 79 (1957), pp. 825-856, S. Abhyankar formulated a number of
conjectures on the structure of the finite groups that occur as Galois groups of finite étale coverings of U.

The conjectures concerning the finite groups which are Galois groups of connected étale coverings of U of order prime to
p are proved and made precise in Corollary XIII.2.12. Before turning to the finite quotients of π₁(U), let us begin by
giving some indications about the “size” of this group. Let X = Spec(A). One knows that Hom_cont(π₁(U),ℤ/pℤ) is
described by Artin-Schreier theory (Corollary XI.6.9). This group is isomorphic to A/wp(A), where wp is the map from A
to A sending a to aᵖ − a. First suppose that U is the affine line 𝔸¹, with ring k[T]. Let E be the set of elements of
k[T] of the form ∑\_i a_iT^i, with a_i = 0 when p divides i. It is immediate that the composite map E → k[T] → k[T]/wp
k[T] is bijective. Hence the coefficients a_i, with (i,p) = 1, behave like coordinates of a space parametrizing cyclic
degree-p coverings of the affine line. In particular, one deduces that π₁(𝔸¹) is not topologically of finite type and
that, if one makes an extension k → k′ of algebraically closed fields, the natural morphism π₁(𝔸¹ ×\_k k′) → π₁(𝔸¹),
which is surjective, is not bijective, unlike the proper case. In the general case, the curve U can be realized as a
finite scheme over the affine line, and one concludes that the same phenomena occur for π₁(U), and indeed more generally
for π₁(V) for every connected affine k-scheme V of finite type and dimension ≥ 1.

With this said, if G is a finite group, write G^(p′) for the largest quotient group of G of order prime to p. For a
finite group G to be a topological quotient of π₁(U), it is necessary that G^(p′) be a topological quotient of π₁^p′(U),
a condition one knows in principle how to answer by Corollary XIII.2.12. In the article cited above, Abhyankar
conjectures that this necessary condition is also sufficient. This conjecture was proved by M. Raynaud in the case of
the affine line and by D. Harbater in the general case (Invent. Math. 116 (1994), pp. 425-462, and 117, pp. 1-25). For
example, in the case of the affine line, π₁^p′(𝔸¹) = 1, and one concludes that a finite group G is the Galois group of a
connected étale covering of 𝔸¹ if and only if G^(p′) = 1, that is, if and only if G is generated by its Sylow
p-subgroups. Thus every finite simple group whose order is a multiple of p is suitable.

## 3. Cohomological Properness and Generic Local Acyclicity

<!-- label: XIII.3 -->

<!-- original page 395 -->

**Theorem.**

<!-- label: XIII.3.1 -->

Let S be an irreducible scheme with generic point s, let X and Y be two S-schemes of finite presentation, and let f: X →
Y be an S-morphism. For every S-scheme S′, write Y′, X′, etc. for the inverse images of Y, X, etc. by the morphism S′ →
S. The following properties hold:

1. a. One can find a nonempty open subset $S'$ of $S$ such that, for every finite constant sheaf of sets $F'$ on $X'$,
   $f'_{*}F'$ is constructible and $(F',f')$ is cohomologically proper relative to $S'$ in dimension ≤ 0.

1. b. Let $F$ be a constructible sheaf of sets on $X$. Then one can find a nonempty open subset $S'$ of $S$, depending
   on $F$, such that $f'_{*}F'$ is constructible and $(F',f')$ is cohomologically proper relative to $S'$ in dimension ≤
   0\.

1. Suppose that schemes of finite type of dimension ≤ dim X_s over an algebraic closure k̄ of κ(s) are strongly
   desingularizable (SGA 5 I 3.1.5). Then one has in addition the following properties:

1. a. One can find a nonempty open subset $S'$ of $S$ such that, for every finite constant sheaf of groups $F'$ on $X'$
   of order prime to the residual characteristics of $S$, if $\Phi'$ is the stack of torsors under $F'$, then
   $f'_{*}\Phi'$ is 1-constructible and $(F',f')$ is cohomologically proper relative to $S'$ in dimension ≤ 1.

1. b. Let $\mathcal{L}$ be the set of prime numbers distinct from the residual characteristics of $S$, and let $\Phi$ be
   a 1-constructible ind-$\mathcal{L}$-stack on $X$ (XIII.0) such that, for every scheme $X_{1}$ étale over $X$ and
   every pair of objects $x$, $x_{1}$ of `Φ_X₁`, the sheaf `SheafHom_X₁(x,x₁)` is constructible. Assume moreover that
   $S$ is locally noetherian. Then one can find a nonempty open subset $S'$ of $S$ such that $f'_{*}\Phi'$ is
   1-constructible, such that, for every pair of objects $y$, $y_{1}$ of a fiber `(f′_*Φ′)_Y₁`, the sheaf
   `SheafHom_Y₁(y,y₁)` is constructible,

<!-- original page 396 -->

and such that (Φ′,f′) is cohomologically proper relative to S′ in dimension ≤ 1.

**Proof.** One may suppose S affine. By SGA 4 VIII 1.1, one may suppose S integral. Finally, by passage to the limit,
one may suppose that S is the spectrum of an algebra of finite type over ℤ; in particular S is then noetherian. Since
the question is local on Y, one may suppose Y affine. Moreover, to prove the theorem it is enough to do so after a
finite extension S′ → S, where S′ is an integral scheme and S′ → S is a composite of étale morphisms and finite
surjective radicial morphisms.

**1. The Case of Constant Sheaves of Sets**

1.1. **Reduction to the case where $X$ is normal over $S$.** Let `X₁_s̄` be the normalization of $(X_{\bar{s}})_{red}$.
After replacing $S$ by a nonempty open subset and making a radicial extension of $S$, one may suppose that `X₁_s̄` comes
from a scheme $X_{1}$ normal over $S$, and that the morphism `X₁_s̄ → X_s̄` comes from a finite surjective morphism
$p: X_{1} \to X$ (EGA IV 8.8.2 and 9.6.1). Suppose the theorem proved for `fp`. After restricting $S$ to an open subset,
one may suppose that, for every constant sheaf of sets $F$ on $X$, $(p*F,fp)$ is cohomologically proper relative to $S$
in dimension ≤ 0 and $f_{*}p_{*}(p*F)$ is constructible. By XIII.1.9, $(p_{*}p*F,f)$ is then cohomologically proper
relative to $S$ in dimension ≤ 0. The morphism

$$
F \to p_{*}p*F = G
$$

is a monomorphism. It already follows, since $f_{*}F$ is a subsheaf of $f_{*}G$, that $f_{*}F$ is constructible (SGA 4
IX 2.9 (ii)) and that $(F,f)$ is cohomologically proper relative to $S$ in dimension ≤ −1.

Let X₂ = X₁ ×\_X X₁, and let q: X₂ → X be the canonical morphism. By XIII.1.11 1,

<!-- original page 397 -->

one has an exact sequence

```text
F → G ⇉ q_*q*F.
```

By what we have just proved, applied to `fq` instead of $f$, one may suppose, after restricting $S$ to a nonempty open
subset, that for every constant sheaf of sets $F$ on $X$, $(q*F,fq)$ is cohomologically proper relative to $S$ in
dimension ≤ −1, hence that $(q_{*}q*F,f)$ is cohomologically proper relative to $S$ in dimension ≤ −1. It then follows
from XIII.1.13 1 that $(F,f)$ is cohomologically proper relative to $S$ in dimension ≤ 0.

1.2. **Reduction to the case where X is normal affine over S.**

Let U_s be an affine open subset of X_s dense in X_s. After restricting S to a nonempty open subset, one may suppose
that U_s → X_s lifts to an open immersion i: U → X, schematically dominant relative to S (EGA IV 8.9.1). Since the
morphism X → S is normal, one has by SGA 2 XIV 1.18:

$$
prof_{et},S-U(X) \geq 2;
$$

hence, for every constant sheaf F on X, the canonical morphism

$$
F \to i_{*}i*F
$$

is an isomorphism. It follows that, if the theorem is supposed proved for fi and i, then, after restricting S to a
nonempty open subset, (i*F,i) and (i*F,fi) are cohomologically proper relative to S in dimension ≤ 0. The same is
therefore true of (F,f) (XIII.1.6 2). Since moreover f\*\*F = (fi)\*\*(i\*F) is constructible, this completes the
reduction.

1.3. **End of the proof.**

One may suppose S normal (EGA IV 7.8.3). One can find a compactification of X_s:

<!-- original page 398 -->

```text
X_s → P_s
 \    |
  \   g_s
   f_s|
     Y_s,
```

where j_s is a dominant open immersion and g_s is proper. After making a radicial extension of κ(s) and replacing P_s by
its normalization, which does not change X_s, one may suppose P_s geometrically normal. After restricting S to a
nonempty open subset and making a surjective radicial extension, one may suppose that the diagram above comes from a
diagram

```text
X → P
 \  |
  \ g
   f|
    Y,
```

where $P$ is a scheme normal over $S$, $j$ is an open immersion schematically dominant relative to $S$, and $g$ is
proper (EGA IV 6.9.1, 9.9.4, and 9.6.1). For every finite constant sheaf of sets $F$ on $X$ with value $C$, $j_{*}F$ is
the constant sheaf with value $C$ (SGA 4 2.14.1), and the same remains true after every base change $S' \to S$. It
follows that $(F,j)$ is cohomologically proper relative to $S$ in dimension ≤ 0. Hence the same is true of $(F,f)$,
since $g$ is proper (XIII.1.8). Since $g$ is proper, $f_{*}F = g_{*}C_{P}$ is constructible, which completes the proof
of 1 a.

**2. The Case of a Constructible Sheaf of Sets**

Let F be a constructible sheaf of sets on X. By SGA 4 IX 2.14 (ii), one can find a finite family of morphisms p_i: Z_i →
X and, on each Z_i, a finite constant sheaf of sets C_i, such that one has a monomorphism

<!-- original page 399 -->

```text
j: F → ∏_i (p_i)_*C_i = G.
```

By 1 a, after restricting S to a nonempty open subset, one may suppose that the (C*i,fp_i) are cohomologically proper
relative to S in dimension ≤ 0, and that the f\*\*(p*i)\**C*i are constructible. One already concludes that (G,f) is
cohomologically proper relative to S in dimension ≤ 0 (XIII.1.9), hence that (F,f) is cohomologically proper relative to
S in dimension ≤ −1, and that f\*\*F is constructible. Let K be the amalgamated sum K = G ⨿\_F G. Since F and G are
constructible, so is K. We therefore conclude from the preceding that, after restricting S to a nonempty open subset,
one may suppose that (K,f) is cohomologically proper relative to S in dimension ≤ −1. It then follows from XIII.1.13 1
that (F,f) is cohomologically proper relative to S in dimension ≤ 0.

**3. The Case of Constant Sheaves of Groups**

If F is a constant sheaf of groups on X, write Φ for the stack of torsors under F.

3.1. Let us first show that, after restricting $S$ to a nonempty open subset, for every constant sheaf of groups $F$ on
$X$ whose order is prime to the residual characteristics of $S$, the pair $(F,f)$ is cohomologically proper relative to
$S$ in dimension ≤ 0 and $f_{*}\Phi$ is constructible.

For this, one reduces to the case where X is smooth over S. After making a finite extension of κ(s), which is allowed
since it may be regarded as the composite of an étale extension and a radicial extension, one can find a proper
surjective morphism p_s: X₁s → X_s, where X₁s is a scheme smooth over S of the same dimension as X_s. After restricting
S to a nonempty open subset, one may suppose that p_s comes from a proper surjective morphism p: X₁ → X, where X₁ is a
scheme smooth over S

<!-- original page 400 -->

(EGA IV 9.6.1 and 12.1.6). Let X₂ = X₁ ×\_X X₁, and let q: X₂ → X be the canonical morphism. There is an exact diagram
of stacks on X

```text
Φ → p_*p*Φ ⇉ q_*q*Φ
```

(XIII.1.11 2). Supposing the theorem proved in the smooth case, one sees first that one may suppose $f_{*}p_{*}p*\Phi$
constructible; hence the same is true of $f_{*}\Phi$ (XIII.3.1.1 below). Moreover, by XIII.1.6 2, one may suppose
$(p_{*}p*\Phi,f)$ cohomologically proper relative to $S$ in dimension ≤ 0. It follows that $(\Phi,f)$ is cohomologically
proper relative to $S$ in dimension ≤ −1. One may therefore suppose that $(q_{*}q*\Phi,f)$ is cohomologically proper
relative to $S$ in dimension ≤ −1, and this implies that $(\Phi,f)$ is cohomologically proper relative to $S$ in
dimension ≤ 0 (XIII.1.12 1).

One then reduces, as in 1.2, to the case where X is smooth and affine over S. Let

```text
X → P
 \  |
  \ q
   f|
    Y
```

be a compactification of X, where i is a dominant open immersion and q is proper. Since dim P_s = dim X_s, the
hypothesis of resolution of singularities can be applied to P_s̄. After making an étale extension and a radicial
extension of S, one can find a proper morphism r: Z → P, where Z is smooth over S, r⁻¹(X) ≃ X, and r⁻¹(X) is the
complement in Z of a divisor with normal crossings relative to S. Every torsor under F is then tamely ramified on Z
relative to S (XIII.2.3 b). It follows from XIII.2.7 that (F,f) is cohomologically proper relative to S in dimension ≤
0, proving our assertion.

3.2. **Reduction to the case where X is smooth over S.**

<!-- original page 401 -->

After making a finite extension of κ(s), one can find a proper surjective morphism p_s: X₁s → X, where X₁s is a scheme
smooth over s, and one may suppose that p_s comes from a proper surjective morphism p: X₁ → X, where X₁ is smooth over
S. Suppose the theorem proved for fp and let us prove it for f. Let F be a finite constant sheaf of groups on X, of
order prime to the residual characteristics of S, and let Φ be the stack of torsors under F. Let X₂ = X₁ ×\_X X₁, X₃ =
X₁ ×\_X X₁ ×\_X X₁, and let q: X₂ → X, r: X₃ → X be the canonical morphisms. By XIII.1.11 2, one has an exact diagram of
stacks

```text
Φ → p_*p*Φ ⇉ q_*q*Φ ⇉⇉ r_*r*Φ.
```

To prove that (Φ,f) is cohomologically proper relative to S in dimension ≤ 1, it is enough to show that the same is true
of (p**p\*Φ,f), that (q**q*Φ,f) is cohomologically proper relative to S in dimension ≤ 0, and that (r\*\*r*Φ,f) is
cohomologically proper relative to S in dimension ≤ −1 (XIII.1.12 2). By 3.1 above, one may suppose that, for every
finite constant sheaf of groups F, the pairs (q*Φ,fq), (q*Φ,q), (r*Φ,fr), and (r*Φ,r) are cohomologically proper
relative to S in dimension ≤ 0. It then follows from XIII.1.6 2 that (q**q\*Φ,f) and (r**r*Φ,f) are cohomologically
proper relative to S in dimension ≤ 0. Since the theorem is assumed proved in the smooth case, (p*Φ,fp) and (p*Φ,p), and
hence also (p\*\*p*Φ,f) (XIII.1.6 2), are cohomologically proper relative to S in dimension ≤ 1. This shows that (Φ,f)
is cohomologically proper relative to S in dimension ≤ 1.

Moreover $f_{*}p_{*}p*\Phi$ is 1-constructible by hypothesis. By XIII.3.1 one may suppose $f_{*}q_{*}q*\Phi$
constructible; it therefore follows from XIII.3.1.1 below that $f_{*}\Phi$ is 1-constructible.

3.3. **Reduction to the case where X is smooth affine over S.**

<!-- original page 402 -->

By 3.2, one may suppose $X$ smooth over $S$. Let $(U_{i})_{i}\in I$ be a finite covering of $X$ by affine opens, let
$X_{1}$ be the direct sum of the $U_{i}$, and let $p: X_{1} \to X$ be the canonical morphism. Since $p$ is a morphism of
effective descent for the category of étale sheaves of finite type on variable schemes, one sees as in 3.2 that, if the
theorem is assumed proved for the $U_{i}$, that is, for $X_{1}$, it is also true for $X$.

3.4. **The case where X is smooth affine over S.**

As in 3.1, after restricting S to a nonempty open subset and making an étale extension and a surjective radicial
extension of S, one can find a commutative diagram

```text
X → P
 \  |
  \ q
   f|
    Y
```

where $P$ is smooth over $S$, $X$ is the complement in $P$ of a divisor with normal crossings relative to $S$, and $q$
is proper. If $F$ is a constant sheaf of order prime to the residual characteristics of $S$, every torsor under $F$ is
tamely ramified on $P$ relative to $S$ (XIII.2.3 b). The fact that $(F,f)$ is cohomologically proper relative to $S$ in
dimension ≤ 1 and that $f_{*}\Phi$ is constructible then follows from XIII.2.7.

**4. Proof of 2 b**

4.1. **The case where Φ is a gerbe.**

One can find a surjective étale morphism of finite type p: X₁ → X such that p\*Φ is a trivial gerbe. By descent, as in
3.2, it is enough to prove the theorem for X₁, X₁ ×\_X X₁, and

<!-- original page 403 -->

X₁ ×\_X X₁ ×\_X X₁. We are therefore reduced to the case where Φ is the gerbe of torsors under a constructible sheaf of
groups F whose fibers have order prime to the residual characteristics of S.

By SGA 4 IX 2.14, one can find a finite family of finite morphisms p_i: Z_i → X and, for each i, a finite constant sheaf
of groups C_i, of order prime to the residual characteristics of S, such that one has a monomorphism \[Translator note:
the corrected source fixes “morphism” to “monomorphism.”\]

```text
j: F → ∏_i p_i*C_i = G.
```

Let Φ*i be the stack of torsors under C_i, and let Ψ be the stack of torsors under G. It follows from 2 a that, after
restricting S to a nonempty open subset, one may suppose that the (C_i,fp_i) are cohomologically proper relative to S in
dimension ≤ 1, and that the stacks f\*\*p_i*Φ*i are 1-constructible. It then follows from XIII.1.9 that the (p_i*C_i,f)
are cohomologically proper relative to S in dimension ≤ 1; hence the same is true of (G,f). Moreover, since p_i*Φ_i is
equivalent to the stack of torsors under the group p_i\*C_i (SGA 4 VIII 5.8), one sees that f*\*Ψ is 1-constructible.

Since $R^{1}f_{*}G$ is constructible, one can find a sheaf representable by an étale $Y$-scheme of finite type $T$ and
an epimorphism

$$
a: T \to R^{1}f_{*}G
$$

(SGA 4 IX 2.7). Moreover, one may suppose that the image of the identity section of T(T) is defined by a torsor Q on X
×*Y T = X_T with group G|X_T. Let f_T: X_T → T be the canonical morphism, and put F_T = F|X_T, etc. By 1 b, after
restricting S to a nonempty open subset, one may suppose that (Q/F_T,f_T) is cohomologically proper relative to S in
dimension ≤ 0 and that f_T\*(Q/F_T) is constructible. It then follows from XIII.3.1.2 that f*\*Ψ is constructible.

Let us show that (F,f) is cohomologically proper relative to

<!-- original page 404 -->

S in dimension ≤ 1. By XIII.1.13 2, it is enough to prove that, for every scheme Y₁ étale over Y and every torsor Q₁ on
X₁ = X ×\_Y Y₁, if f₁: X₁ → Y₁ is the canonical morphism, then (Q₁/F₁,f₁) is cohomologically proper relative to S in
dimension ≤ 0. But by definition of T, Q₁ is, locally for the étale topology of Y₁, the inverse image of Q. This proves
our reduction.

4.2. **The general case.**

Using Lemma XIII.6.1.1, 4.1, and 1 a, one sees that, after restricting $S$ to a nonempty open subset, one may suppose
$S(f_{*}\Phi)$ constructible and $(S\Phi,f)$ cohomologically proper relative to $S$ in dimension ≤ 0. One can then find
a sheaf representable by an étale $Y$-scheme of finite type $T$ and an epimorphism

$$
a: T \to S(f_{*}\Phi).
$$

We resume the notation of 4.1 and put moreover $Z = T \times_{Y} T$, $X_{Z} = X \times_{Y} Z$, and write
$f_{Z}: X_{Z} \to Z$ for the canonical morphism. One may suppose $T$ chosen so that the image $q$ of the identity
section of $T(T)$ by $a$ is defined by an object $p$ of `(f_*Φ)_T = Φ_X_T`. Let $p_{1}$ and $p_{2}$, respectively
$q_{1}$ and $q_{2}$, be the inverse images of $p$, respectively $q$, by the two projections from $Z$ to $T$. After
restricting $S$ to a nonempty open subset, one may suppose that `(SheafAut_X_T(p),f_T)` is cohomologically proper
relative to $S$ in dimension ≤ 1, that `(SheafHom_X_Z(p₁,p₂),f_Z)` is cohomologically proper relative to $S$ in
dimension ≤ 0, and that `f_T_*(SheafAut_X_T(p))` and `f_Z_*(SheafHom_X_Z(p₁,p₂))` are constructible (1 a and 4.1).

One first deduces that, for every scheme $Y_{1}$ étale over $Y$ and every pair of objects $y$, $y_{1}$ of `(f_*Φ)_Y₁`,
the sheaf `SheafAut_Y₁(y)`, respectively `SheafHom_Y₁(y,y₁)`, is constructible: such a sheaf is, locally for the étale
topology of $Y_{1}$, the inverse image of `f_T_*(SheafAut_X_T(p))`, respectively of `f_Z_*(SheafHom_X_Z(p₁,p₂))`.

It remains to prove that (Φ,f) is cohomologically proper relative

<!-- original page 405 -->

to S in dimension ≤ 1. For this it is enough to show that, for every S-scheme S′ and every geometric point ȳ′ of Y, if Ȳ
denotes the strict localization of Y at y′, X̄ = X ×\_Y Ȳ, etc., then the canonical functor

$$
\bar{\phi}: \Phi(\bar{X}) \to \Phi'(\bar{X}')
$$

is an equivalence of categories.

Let us show that φ̄ is fully faithful. Let x, y ∈ Φ(X̄), and let x′, y′ be their images in Φ′(X̄′). We must show that the
canonical morphism

<!-- label: eq:XIII.4.* -->

$$
(*)   \operatorname{Hom}_{\bar{X}}(x,y) \to \operatorname{Hom}_{\bar{X}}'(x',y')
$$

is bijective. By definition of T, there exist two morphisms from Ȳ to T such that x and y are the inverse images of p by
these two morphisms. This amounts to saying that there is a morphism Ȳ → Z, hence a morphism h: X̄ → X_Z, such that

```text
h*(p₁) = x,     h*(p₂) = y.
```

Consequently one has a canonical isomorphism

```text
SheafHom_X̄(x,y) = h*(SheafHom_X_Z(p₁,p₂)).
```

But, taking into account the fact that (SheafHom_X_Z(p₁,p₂),f_Z) is cohomologically proper relative to S in dimension ≤
0, one sees that the same is true of (SheafHom_X̄(x,y),f̄), which proves that the morphism (\*) is bijective.

Let us show that φ̄ is essentially surjective. Let x′ ∈ Φ′(X̄′). Since (SΦ,f) is cohomologically proper relative to S in
dimension ≤ 0, the canonical morphism

$$
H^{0}(\bar{X},S\bar{\Phi}) \to H^{0}(\bar{X}',S\bar{\Phi}')
$$

is bijective. Let G′ be the maximal subgerbe of Φ′ generated by x′. There then exists a maximal subgerbe G of Φ̄ whose
inverse image on X̄′ is G′. By 4.1, (G,f̄) is cohomologically proper relative to S in dimension ≤ 1; consequently the
canonical functor

$$
G(\bar{X}) \to G'(\bar{X}')
$$

<!-- original page 406 -->

is an equivalence of categories. This proves the existence of an element x of Φ(X̄) whose image in Φ′(X′) is isomorphic
to x′, and completes the proof of the theorem.

**Sublemma.**

<!-- label: XIII.3.1.1 -->

Let S be a locally noetherian scheme, and let

```text
Φ → Φ₁ ⇉ Φ₂
```

be an exact diagram of stacks on $S$ (XIII.1.10.1). If $\Phi_{1}$ is constructible, then so is $\Phi$. If, for every scheme $S'$
étale over $S$ and every pair of objects $x_{1}$, $y_{1}$ of $(\Phi_{1})_{S}'$, the sheaf $SheafHom_{S}'(x_{1},y_{1})$ is constructible, then
for every pair of objects $x$, $y$ of $\Phi_{S}'$, the same is true of $SheafHom_{S}'(x,y)$. \[Translator note: the corrected
source fixes "object" to "objects."\] Suppose $\Phi_{1}$ is 1-constructible (XIII.0) and $\Phi_{2}$ is constructible; then $\Phi$ is
1-constructible.

For every scheme S′ étale over S and every object x of Φ_S′, one has a monomorphism

$$
SheafAut_{S}'(x) \to SheafAut_{S}'(p(x)).
$$

It follows from SGA 4 IX 2.9 that, if Φ₁ is constructible, then so is Φ; the second assertion of the lemma is proved in
the same way.

Now suppose Φ₁ is 1-constructible and Φ₂ constructible. The morphism p induces on the sheaves of maximal subgerbes a
morphism

$$
\phi: S\Phi \to S\Phi_{1}.
$$

Let G be the image of SΦ by φ. By SGA 4 IX 2.9, G is a constructible sheaf. Thus one can find a sheaf representable by
an étale S-scheme of finite type T and an epimorphism

$$
a: T \to G
$$

(SGA 4 IX 2.7).

<!-- original page 407 -->

Moreover, $T$ may be chosen so that the image $y$ of the identity section of $T(T)$ by $a$ is defined by an object
$x_{1}$ of $(\Phi_{1})_{T}$ of the form $x_{1} = p(x)$, with $x \in \Phi_{T}$.

It is enough to show that, for every point $s$ of $S$, there exists a nonempty open subset $U$ of $closure({s})$ such
that $S\Phi|U$ is locally constant constructible. Let $s \in S$, let $\bar{s}$ be a geometric point above $s$, and let
$\bar{y}_{1}, \cdots, \bar{y}_{n}$ be the elements of $G_{\bar{s}}$. By definition of $T$, there exist morphisms
$h_{i}: \bar{s} \to T$ such that $h_{i}*(y) = \bar{y}_{i}$. Let $S'$ be the fiber product over $S$ of $n$ schemes
isomorphic to $T$, let $h: \bar{s} \to S'$ be the fiber product of the $h_{i}$, and let $y_{i}$, respectively $x_{i}$,
be the inverse image of $y$, respectively $x$, by the $i$-th projection from $S'$ to $T$. Let $F_{i}$ be the subsheaf of
$S\Phi|S'$ inverse image of $y_{i}$, and let us show that the $F_{i}$ are constructible. The sheaf $F_{i}$ is a quotient
of the sheaf $F'_{i}$ such that, for every scheme $S''$ étale over $S'$,

```text
F′_i(S″) =
{ isomorphism classes of objects z of Φ_S″ endowed
  with an isomorphism i: p(z) ≃ p(x_i|S″) }.
```

[Translator note: the corrected source fixes a missing closing brace in this displayed definition.] It is enough to show
that the $F'_{i}$ are constructible. But if one puts $z_{i} = p_{1}p(x_{i})$ and $z'_{i} = p_{2}p(x_{i})$, one has a
monomorphism

```text
Ψ_i: F′_i → SheafIsom_S′(z_i,z′_i),
```

obtained by associating to every scheme $S''$ étale over $S'$ and every object $z$ of $\Phi_{S}''$ with an isomorphism
$i: p(z) \simeq p(x_{i}|S'')$, the isomorphism from $z_{i}$ to $z'_{i}$ defined by the condition that the diagram

```text
p₁p(z) --p₁(i)→ z_i
  |j             |
  |              |
p₂p(z) --p₂(i)→ z′_i
```

commute, where j is the canonical morphism associated with the exact diagram.

<!-- original page 408 -->

The morphism $\Psi_{i}$ is injective, because saying that two objects $z$, $z'$, with isomorphisms
$i: p(z) \simeq p(x_{i}|S'')$ and $i': p(z') \simeq p(x_{i}|S'')$, define the same element of
$SheafIsom_{S}''(z_{i},z'_{i})$ amounts to saying that $p_{1}(i'^{-1}i) = p_{2}(i'^{-1}i)$, that is, that $i'^{-1}i$
comes from an isomorphism $z \to z'$. The sheaf $F'_{i}$, being a subsheaf of $SheafIsom_{S}'(z_{i},z'_{i})$, is
constructible.

Since one can find a nonempty open subset U of closure({s}) such that y₁|U, …, y_n|U generate G, it follows from Lemma
XIII.6.1.2 below that SΦ|U is constructible, hence, after possibly shrinking U, that SΦ|U is locally constant
constructible.

**Sublemma.**

<!-- label: XIII.3.1.2 -->

Let S be a locally noetherian scheme, let f: X → S be a morphism, let F → G be a monomorphism of sheaves of groups on X,
let Ψ, respectively Ψ₁, be the stack of torsors under F, respectively under G, and put Φ = f\*\*Ψ, Φ₁ = f\*\*Ψ₁. Suppose
given a sheaf on S representable by an étale S-scheme of finite type T and a surjective morphism

```text
a: T → SΦ₁ ≃ R¹f_*G,
```

such that there exists a torsor Q on X*T = X ×\_S T with group G|X_T which defines in R¹f*_G(T) the image by a of the
identity section of T(T). Let f_T: X_T → T be the canonical morphism and put F_T = F|X_T. Suppose Φ₁ is 1-constructible
and f_T_(Q/F_T) is constructible. Then Φ is 1-constructible.

Indeed, it is enough to copy the proof of XIII.3.1.1, replacing the existence of the morphisms Ψ_i by the fact that one
has isomorphisms

$$
F'_{i} \simeq f_{*}(Q/F_{T})|S'.
$$

**Subremark.**

<!-- label: XIII.3.1.3 -->

Suppose

<!-- original page 409 -->

κ(s) has characteristic zero. Then schemes of finite type over k̄ of dimension ≤ dim X are strongly desingularizable, and
the proof of XIII.3.1 gives the following results:

a. There exists a nonempty open subset S₁ of S such that, for every scheme S′ over S₁ whose maximal points have
characteristic zero and every locally constant constructible sheaf of sets F on X′ = X ×\_S S′, the pair (F,f′) is
cohomologically proper relative to S′ in dimension ≤ 0.

b. If all residual characteristics of S are zero, there exists a nonempty open subset S₁ of S such that, for every
scheme S′ over S₁ and every locally constant constructible sheaf of groups F on X′, the pair (F,f′) is cohomologically
proper relative to S′ in dimension ≤ 1.

It is enough, indeed, to copy the proof of XIII.3.1.2 a). Proposition XIII.2.7, used in 3.4, applies to the case of a
locally constant sheaf F, since, with the notation of 3.4, every torsor under F is tamely ramified on P relative to S
because all residual characteristics of S are zero.

**Corollary.**

<!-- label: XIII.3.2 -->

Let k be a field of characteristic p ≥ 0, let p′ be the set of prime numbers distinct from p, and let f: X → k be a
coherent morphism.

1. For every sheaf of sets F, the pair (F,f) is cohomologically proper in dimension ≤ 0.

1. Suppose one of the following two conditions is satisfied:

a. f is of finite type and the finite type schemes of dimension ≤ dim X over an algebraic closure of k are strongly
desingularizable.

b. The finite type schemes over an algebraic closure of k are strongly desingularizable.

<!-- original page 410 -->

Then, for every sheaf of ind-p′-groups F, the pair (F,f) is cohomologically proper in dimension ≤ 1.

Let F be a sheaf of sets, respectively of ind-p′-groups. By SGA 4 IX 2.7.2 one may write F as a filtered inductive limit

$$
F = colim_{i} F_{i},
$$

where the $F_{i}$ are constructible sheaves of sets, respectively of ind-$p'$-groups. Since $f$ is coherent, $f_{*}$,
respectively $R^{1}f_{*}$, commutes with inductive limits (SGA 4 VII 3.3). If one knows that the pairs $(F_{i},f)$ are
cohomologically proper in dimension ≤ 0, respectively that every sheaf of sets is cohomologically proper in dimension ≤
0 and that the pairs $(F_{i},f)$ are cohomologically proper in dimension ≤ 1, the same will be true of $(F,f)$. We may
therefore suppose $F$ constructible.

If f is assumed of finite type, respectively satisfying a), the proposition follows from XIII.3.1 1 b), respectively
from XIII.3.1 2 b). Let us now prove XIII.3.2 when f is no longer assumed of finite type. For every scheme S′ over k and
every geometric point s̄ of S′, write k̄, respectively S̄′, for the strict localization of k at s̄, respectively of S′ at s̄,
write X̄ for the inverse image of X over k̄, and consider the cartesian square

```text
X̄′ --g→ X̄
 |        |
f̄′       f̄
 |        |
S̄′  →   k̄.
```

It is enough to prove that, for every S′ and every s̄, the canonical morphism

$$
H^{0}(\bar{X},\bar{F}) \to H^{0}(\bar{X}',\bar{F}')
$$

respectively

$$
H^{1}(\bar{X},\bar{F}) \to H^{1}(\bar{X}',\bar{F}'),
$$

is an isomorphism. It is enough to show that one has the relations

<!-- original page 411 -->

<!-- label: eq:XIII.3.* -->

```text
(*)  F̄ ≃ g_*g*F̄,
     respectively R¹g_*(g*F̄) = 0.
```

[Translator note: the corrected source removes an extra parenthesis in the second formula.] In this form, the question
is local on X for the étale topology. We may therefore suppose X affine; by passage to the limit, we may suppose X of
finite type over k. One then knows that (F,f) is cohomologically proper in dimension ≤ 0, respectively ≤ 1, and that the
same remains true when X is replaced by an étale scheme of finite type over X, which proves (\*).

**Theorem.**

<!-- label: XIII.3.3 -->

Let S be an irreducible scheme with generic point s, and let f: X → S be a morphism of finite presentation. Suppose that
the finite type schemes of dimension ≤ dim X_s over an algebraic closure k̄ of k are desingularizable (EGA IV 7.9.1).
Then, if ℒ denotes the set of prime numbers distinct from the residual characteristics of S, there exists a nonempty
open subset S₁ of S such that the morphism f|S₁ is universally locally 1-aspherical for ℒ.

We may suppose S integral and X reduced (SGA 4 VIII 1.1). By passage to the limit we may suppose S noetherian. Moreover,
to prove the theorem, it is enough to do so after a finite extension S₁ → S, where S₁ is an integral scheme and S₁ → S
is a composite of étale extensions and surjective radicial extensions.

First let us show that, after possibly restricting $S$ to a nonempty open subset, $f$ is universally locally 0-acyclic.
After possibly making a radicial extension of $\kappa(s)$, we may suppose that the morphism $(X_{s})_{red} \to s$ is
separable; hence, after possibly restricting $S$ to a nonempty open subset and making a surjective radicial extension of
$S$, we may suppose that $f$ is flat, with geometrically separable fibers (EGA IV 12.1.1). It follows that $f$ is
universally 0-acyclic (SGA 4 XV 4.1).

Let us show that, after possibly restricting S to a nonempty open subset, f is universally locally 1-aspherical for ℒ.
After possibly making a finite extension of κ(s), which is allowed since it may be regarded as a composite of an étale
extension and a radicial extension,

<!-- original page 412 -->

one can find a proper surjective morphism p_s: Y_s → X_s, where Y_s is a smooth S-scheme of the same dimension as X_s,
and one may suppose that p_s comes from a proper surjective morphism p: Y → X, where Y is smooth over S (EGA IV 9.6.1
and 12.1.6). It is enough to show that, after possibly restricting S to a nonempty open subset, for every diagram with
cartesian squares

```text
S″ ←f″- X″
 |i       |j
S′ ←f′- X′
 |        |
S  ←f-- X,
```

where i is étale of finite presentation, and for every sheaf of ind-ℒ-groups F on S″, if Φ is the stack of torsors under
F, then the canonical morphism

```text
f′* i_*Φ → j_* f″*Φ
```

is an equivalence. Put Z = Y ×\_X Y and T = Y ×\_X Y ×\_X Y. In a natural way one has a commutative diagram

```text
S″ ← X″ ← Y″ ⇔ Z″ ⇔⇔ T″
 |    |    |     |      |
S′ ← X′ ← Y′ ⇔ Z′ ⇔⇔ T′
 |    |    |     |      |
S  ← X  ← Y  ⇔ Z  ⇔⇔ T,
```

where all vertical squares are cartesian, the double arrows are the two projections from Z to Y, and the triple arrows
are the three projections from T to Z. Let q: Z → X and r: T → X be the canonical morphisms, with q′, r′, q″, r″ having
their evident meanings. By XIII.1.11 2), one has the following essentially commutative diagram, whose rows are exact:

<!-- original page 413 -->

```text
f′*i_*Φ → p′_*p′*(f′*i_*Φ) ⇉ q′_*q′*(f′*i_*Φ) ⇉⇉ r′_*r′*(f′*i_*Φ)
   |a             |b                    |c                       |d
j_*f″*Φ → j_*p″_*p″*(f″*Φ) ⇉ j_*q″_*q″*(f″*Φ) ⇉⇉ j_*r″_*r″*(f″*Φ).
```

[Translator note: the corrected source fixes the upper second entry of this diagram, replacing i_x by i\_\*.] Since Y is
smooth over S, the morphism fp is universally locally 1-aspherical for ℒ (SGA 4 XV 2.1), and it follows from SGA 4 VII
2.1.7 that b is an equivalence of categories. On the other hand, after possibly restricting S to a nonempty open subset,
we may suppose that the morphisms Z → S and T → S are universally locally 0-acyclic. It follows that the functors c and
d are fully faithful, and the diagram above then shows that a is an equivalence. This completes the proof.

**Corollary.**

<!-- label: XIII.3.4 -->

Let k be a field of characteristic p ≥ 0, let p′ be the set of prime numbers distinct from p, and let f: X → k be a
coherent morphism. Suppose one of the following two conditions is satisfied:

a. f is of finite type and the finite type schemes of dimension ≤ dim X over an algebraic closure of k are
desingularizable.

b. The finite type schemes over an algebraic closure of k are desingularizable.

Then f is universally locally 1-aspherical for p′.

Case a) follows from XIII.3.3. In case b), since the question is local on X, we may suppose X affine; by passage to the
limit (SGA 4 XV 1.3), one is reduced to the case where X is of finite type over k.

**Corollary.**

<!-- label: XIII.3.5 -->

Let S be an irreducible scheme with generic point s, and let f: X → S be a morphism of finite presentation.

<!-- original page 414 -->

Suppose that the finite type schemes of dimension ≤ dim X_s over an algebraic closure k̄ of κ(s) are strongly
desingularizable (SGA 5 I 3.1.5). If ℒ denotes the set of prime numbers distinct from the residual characteristics of S,
there exists a nonempty open subset S₁ of S such that, for every specialization s̄₁ → s̄₂ of geometric points of S₁, the
specialization morphism

```text
π₁^ℒ(X_s̄₁) → π₁^ℒ(X_s̄₂)
```

is bijective.

By XIII.3.1 and XIII.3.3, after possibly restricting S to a nonempty open subset, we may suppose that f is locally
1-aspherical for ℒ, and that, for every constant finite sheaf of ℒ-groups F on X, the pair (F,f) is cohomologically
proper in dimension ≤ 1. It then follows from XIII.1.14 that, for every specialization s̄₁ → s̄₂ of geometric points of
S₁, the specialization morphism

```text
(R¹f_*F)_s̄₂ → (R¹f_*F)_s̄₁
```

is bijective. The corollary is nothing other than the translation of the preceding assertion in terms of fundamental
groups.

## 4. Exact Homotopy Sequences

<!-- label: XIII.4 -->

### 4.0.

<!-- label: XIII.4.0 -->

Let X and S be two connected schemes, let f: X → S be a morphism, let a be a geometric point of X, and let ℒ be a set of
prime numbers. Let K be the kernel of the canonical homomorphism π₁(X,a) → π₁(S,a), and let N be the smallest
distinguished pro-subgroup of K such that K/N is a pro-ℒ-group K^ℒ. Then N is distinguished in π₁(X,a), and the quotient
of π₁(X,a) by N is denoted

$$
\pi_{1}'(X,a).
$$

If a is a geometric point of a geometric fiber X_s̄, the canonical morphisms

$$
\pi_{1}(X_{\bar{s}},a) \to \pi_{1}(X,a) \to \pi_{1}(S,a)
$$

define canonical morphisms

```text
π₁^ℒ(X_s̄,a) --u→ π₁′(X,a) --v→ π₁(S,a).
```

One has vu = 0.

<!-- original page 415 -->

**Proposition.**

<!-- label: XIII.4.1 -->

Let $S$ be a connected scheme and let $f: X \to S$ be a locally 0-acyclic morphism (SGA 4 XV 1.11); suppose moreover
that $f$ is 0-acyclic, which, when $f$ is coherent, amounts to saying that the geometric fibers of $f$ are connected
(SGA 4 XV 1.16). Let $\mathcal{L}$ be a set of prime numbers. If $S'$ is an étale scheme over $S$, write $X'$, $f'$ for
the inverse images of $X$, $f$ over $S'$. Suppose that, for every étale covering $S'$ of $S$ and every étale covering
$E$ of $X'$ which is a quotient of a Galois covering whose group is an $\mathcal{L}$-group, $(E,f')$ is cohomologically
proper relative to $S'$ in dimension ≤ 0 and $f'_{*}E$ is constructible. Then, if $\bar{s}$ is a geometric point of $S$
and $a$ is a geometric point of the fiber $X_{\bar{s}}$, the sequence of group homomorphisms

<!-- label: eq:XIII.4.1.1 -->

```text
π₁^ℒ(X_s̄,a) --u→ π₁′(X,a) --v→ π₁(S,a) → 1
```

is exact.

This statement generalizes X.1.4, whose proof we shall copy.

First let us show that v is surjective. It is enough to show that, for every connected étale covering S′ of S, X′ is
also connected (V.6.9). Let C be a set with at least two elements. Since f is 0-acyclic, the canonical morphism

$$
H^{0}(S',C_{S}') \to H^{0}(X',C_{X}')
$$

is bijective, hence X′ is connected, whence the surjectivity of v.

<!-- original page 416 -->

By definition of K^ℒ (XIII.4.0), one has the exact sequence

$$
1 \to K^{\mathcal{L}} \to \pi_{1}'(X,a) \to \pi_{1}(S,a) \to 1.
$$

Let S̃ be the universal covering of S and put X̃ = S̃ ×\_S X; the group K^ℒ classifies the Galois coverings P with group an
ℒ-group, such that there exist an étale covering S′ of S and a Galois covering Q of X′ = X ×\_S S′ for which one has an
isomorphism P ≃ Q ×\_X′ X̃. For the sequence XIII.4.1.1 to be exact, it is necessary and sufficient that the canonical
morphism

$$
\pi^{\mathcal{L}}_{1}(X_{\bar{s}},a) \to K^{\mathcal{L}}
$$

be surjective. By the interpretation of $K^{\mathcal{L}}$ this amounts to saying that, for every étale covering $S'$ of
$S$ and every Galois covering $Q$ of $X'$ with group an $\mathcal{L}$-group, such that $P = Q \times_{X}' \tilde{X}$ is
connected, $Q|X_{\bar{s}}$ is connected. Let us show that this last condition is satisfied. Indeed, let $S'$ be an étale
covering of $S$ and let $Q$ be a Galois covering of $X'$ with group an $\mathcal{L}$-group $F$, such that
$Q|X_{\bar{s}}$ is disconnected; we shall show that, after possibly replacing $S'$ by an étale covering, $Q$ becomes
disconnected. There exists a subgroup $G$ of $F$ distinct from $F$ and a torsor $R$ under $G|X_{\bar{s}}$ such that
$Q|X_{\bar{s}}$ is obtained from $R$ by extension of the structural group $G \to F$. The étale covering $E = Q/G$ of
$X'$ is such that $E|X_{\bar{s}}$ has a section. By XIII.1.16, $f_{*}E$ is locally constant constructible and, after
possibly replacing $S'$ by an étale covering, we may even suppose that $f_{*}E$ is constant. Since $(E,f')$ is
cohomologically proper relative to $S'$ in dimension ≤ 0 and since $H^{0}(X_{\bar{s}},E|X_{\bar{s}})$ is nonempty, one
sees that $E$ has a section. But this proves that $Q$ is disconnected, completing the proof.

We deduce from XIII.4.1 the following lemma, which will be used in XIII.4.6.

**Lemma.**

<!-- label: XIII.4.2 -->

Let S be a connected scheme, let f: X → S be a locally 0-acyclic and 0-acyclic morphism, and let ℒ be a set of prime
numbers.

<!-- original page 417 -->

Suppose that, for every constant finite sheaf of $\mathcal{L}$-groups $F$ on $X$, $(F,f)$ is cohomologically proper
relative to $S$ in dimension ≤ 1, and that, for every étale covering $S'$ of $S$ and every étale covering $E$ of $X'$
which is a quotient of a Galois covering with group an $\mathcal{L}$-group, $f'_{*}E$ is constructible. Then, if
$\bar{s}$ is a geometric point of $S$ and $a$ is a geometric point of the fiber $X_{\bar{s}}$, the sequence of group
homomorphisms

$$
\pi^{\mathcal{L}}_{1}(X_{\bar{s}},a) \to \pi_{1}'(X,a) \to \pi_{1}(S,a) \to 1
$$

is exact.

The hypotheses of XIII.4.1 are satisfied. Indeed, it follows from XIII.1.13 3) that, for every scheme S′ étale over S
and every étale covering E of X′ which is a quotient of a Galois covering with group an ℒ-group, (E,f′) is
cohomologically proper relative to S′ in dimension ≤ 0.

**Proposition.**

<!-- label: XIII.4.3 -->

Let S be a connected scheme, let ℒ be a set of prime numbers, let f: X → S be a 0-acyclic morphism, locally 1-aspherical
for ℒ (SGA 4 XV 1.11), and let g: S → X be a section of f. Let s̄ be a geometric point of S and a a geometric point of
the fiber X*s̄. Suppose that, for every constant sheaf of ℒ-groups F, (F,f) is cohomologically proper in dimension ≤ 1,
that the direct image by f of the stack of torsors under F is a 1-constructible stack (XIII.0), and that, for every
étale covering E of X′ which is a quotient of a Galois covering with group an ℒ-group, f′*\*E is constructible. Then the
sequence of group homomorphisms

<!-- label: eq:XIII.4.3.1 -->

```text
1 → π₁^ℒ(X_s̄,a) --u→ π₁′(X,a) --v→ π₁(S,a) → 1
```

is exact.

In view of XIII.4.2, it remains only to show the injectivity of u, that is, to prove that, for every principal covering
Z̄ of X_s̄

<!-- original page 418 -->

with group an ℒ-group C, there exists an étale covering Z of X and a morphism from a connected component of Z|X_s̄ into Z̄
(V.6.8). Let then Z̄ be a principal covering of X_s̄ with group an ℒ-group C and let z̄ be its class in H¹(X_s̄,C_X_s̄). By
XIII.1.5 d), one has a canonical isomorphism

```text
(R¹f_*C_X)_s̄ ≃ H¹(X_s̄,C_X_s̄),
```

and by XIII.1.16, R¹f\*\*C_X is a locally constant constructible sheaf. We can therefore find an étale covering S′ of S
such that R¹f\*\*C\*X|S′ is constant. If s̄ → S′ is a geometric point above the geometric point s̄ → S, there exists an
element z of H⁰(S′,R¹f\**C*X) whose image in H¹(X_s̄,C_X_s̄) is z̄. By Lemma XIII.4.3.1 below, one can find an étale
covering S′₁ of S′ and a torsor P on X′₁ with group C whose image in H⁰(S′₁,R¹f\*\*C) is equal to the restriction of z.
The torsor P is representable by an étale covering Z of X′₁ = X ×\_S S′₁ such that Z ×\_X′₁ X_s̄ is isomorphic to Z̄. If Z
is regarded as an étale covering of X, one then has a morphism from Z ×\_X X_s̄ into Z̄, completing the proof.

**Sublemma.**

<!-- label: XIII.4.3.1 -->

Let f: X → S be a 0-acyclic and locally 0-acyclic morphism, and let g be a section of f. Let C be a finite constant
group such that (C*X,f) is cohomologically proper in dimension ≤ 0 and such that the direct image by f of the stack of
torsors under C_X is constructible. Then, for every section z of H⁰(S,R¹f*\*C_X), one can find an étale covering S₁ of S
and, if X₁ = X ×\_S S₁, an element of H¹(X₁,C_X₁) whose image by the canonical morphism

```text
H¹(X₁,C_X₁) → H⁰(S₁,R¹f_*C_X₁)
```

is equal to the restriction of $z$ to `H⁰(S₁,R¹f_*C_X₁)`.

For every scheme S′ étale over S, put X′ = X ×\_S S′, and write g′, respectively F′, and so on, for the inverse image of
g, respectively F, and so on, by the morphism S′ → S.

<!-- original page 419 -->

The presheaf G on S defined by

```text
G(S′) =
{ isomorphism classes of torsors P on X′ with group C_X′,
  endowed with an isomorphism g′*P ≃ C_S′ }
```

is then a sheaf. Indeed this follows by descent from the fact that an isomorphism of a torsor P on X′ is completely
determined by its restriction to g′(S′). Moreover, one has a surjective morphism

$$
G \to R^{1}f_{*}C.
$$

Let $z$ be an element of $H^{0}(S,R^{1}f_{*}C_{X})$, and let $H$ be the subsheaf of $G$ which is the inverse image of
$z$. It is enough to show that $H$ is a locally constant constructible sheaf. Since this property is local on $S$, one
may suppose that $z$ comes from an element of $H^{1}(X,C_{X})$ represented by a torsor $P$ such that $g*P$ is isomorphic
to `C_S`. To give an isomorphism $i: g*P \simeq C_{S}$ amounts to giving a global section of `SheafAut_C_S(g*P)`, and
two isomorphisms $i$ and $i'$ define the same element of $G(X)$ if and only if $ii'^{-1}$ is the image of an element of
`Aut_C_X(P)`. If one considers the canonical injection

```text
f_*SheafAut_C_X(P) → SheafAut_C_S(g*P) ≃ C,
```

H is therefore identified with the quotient of SheafAut*C_S(g\*P) by f\*\*SheafAut*C_X(P). By XIII.1.16,
f\*\*SheafAut_C_X(P) is locally constant; hence the same is true of H, completing the proof.

**Examples.**

<!-- label: XIII.4.4 -->

Note that, if S is a connected scheme, the hypotheses of XIII.4.1 are satisfied when f is proper, flat, of finite
presentation, with connected separable geometric fibers, ℒ arbitrary (cf. X.1.3). The hypotheses of XIII.4.3 are
satisfied if moreover f is smooth and has a section, with ℒ denoting the set of prime numbers distinct from the residual
characteristics of S (SGA 4 XV 2.1 and XVI 5.2).

The hypotheses of XIII.4.1 are also satisfied if S is connected and if one has a scheme Z proper of finite presentation,
flat over S,

<!-- original page 420 -->

with connected separable geometric fibers, such that X is the complement in Z of a normal-crossings divisor relative to
S, ℒ being the set of prime numbers distinct from the residual characteristics of S (XIII.2.9). The hypotheses of
XIII.4.3 are satisfied if moreover f is smooth and has a section.

### 4.5.

<!-- label: XIII.4.5 -->

Resume the notation and hypotheses of XIII.4.3. If s̄ is a geometric point of S and a = g(s̄), the section g defines a
morphism

$$
w: \pi_{1}(S,a) \to \pi_{1}'(X,a),
$$

so that π₁′(X,a) is identified with the semidirect product of π₁(S,a) by π₁(X_s̄,a). The profinite group π₁(S,a)
therefore operates on π₁(X_s̄,a). Since π₁^ℒ(X_s̄,a) is a strict projective limit of groups invariant under the action of
π₁(S,a), the datum of π₁^ℒ(X_s̄,a) endowed with this action is equivalent to the datum of a strict projective system of
finite étale group schemes over S, denoted

```text
π₁^ℒ(X/S,g,s̄), or simply π₁^ℒ(X/S,g).
```

One then has the following properties:

#### 4.5.1.

<!-- label: XIII.4.5.1 -->

For every finite étale group scheme G over S whose fibers are ℒ-groups, the set E of classes of torsors P under the
inverse image G_X of G on X, endowed with an isomorphism g\*P ≃ G, is canonically isomorphic to the set

```text
Hom_S(π₁^ℒ(X/S,g,s̄),G) modulo inner automorphisms of G.
```

#### 4.5.2.

<!-- label: XIII.4.5.2 -->

For every finite étale group scheme $G$ over $S$ whose fibers are $\mathcal{L}$-groups, the sheaf $R^{1}f_{*}G_{X}$ is
canonically isomorphic to the sheaf associated with the presheaf

```text
S′ ↦ Hom_S′(π₁^ℒ(X/S,g,s̄),G) modulo inner automorphisms of G.
```

Here S′ denotes a scheme étale over S.

#### 4.5.3.

<!-- label: XIII.4.5.3 -->

Let S′ be a connected S-scheme, let s̄ be a geometric point of S′, and let X′, g′ be the respective inverse images of X,
g over S′. Then π₁^ℒ(X′/S′,g′,s̄) is canonically isomorphic to the inverse image of π₁^ℒ(X/S,g,s̄) over S′. For every
geometric point ξ of S, the fiber π₁^ℒ(X/S,g,s̄)*ξ is isomorphic to π₁^ℒ(X*ξ).

Indeed, giving G is equivalent to giving an abstract ℒ-group 𝔾 on which π₁(S,a) operates, hence an action of π₁′(X,a) on
𝔾. The isomorphism defined in XIII.4.5.1 is then obtained by restriction to the subset E from the canonical morphism

```text
H¹(π₁′(X,a),𝔾) →
H¹(π₁^ℒ(X_s̄,a),𝔾)
  = Hom(π₁^ℒ(X_s̄,a),𝔾) modulo inner automorphisms of G,
```

where E maps bijectively onto the subset of morphisms from π₁^ℒ(X_s̄,a) to 𝔾 which are compatible with the action of
π₁(S,a). Assertion XIII.4.5.3 then follows from the definition of π₁^ℒ(X/S,g,s̄), taking into account the exact homotopy
sequence XIII.4.3.1, and XIII.4.5.2 follows from XIII.4.5.1 and XIII.4.5.3.

**Proposition (Künneth formula).**

<!-- label: XIII.4.6 -->

Let k be a separably closed field of characteristic p ≥ 0, let X and Y be two connected k-schemes, let a be a geometric
point of X, b a geometric point of Y, and c a geometric point of X ×\_k Y above a and b. Suppose one of the following
two conditions is satisfied:

a. X is of finite type over k, and the finite type schemes over an algebraic closure k̄ of k, of dimension ≤ dim X, are
strongly desingularizable (SGA 5 I 3.1.5).

b. X is quasi-compact and quasi-separated, and every finite type scheme over k̄ is strongly desingularizable.

Then, if p′ is the set of prime numbers distinct from p, the morphism

<!-- label: eq:XIII.4.6.0 -->

```text
π₁^{p′}(X ×_k Y,c) → π₁^{p′}(X,a) × π₁^{p′}(Y,b),
```

deduced

<!-- original page 422 -->

from the homomorphisms on fundamental groups associated with the projections

```text
X ×_k Y → X,    X ×_k Y → Y,
```

is an isomorphism.

We may suppose k algebraically closed and X reduced (SGA 4 VIII 1.1). Let Z = X ×*k Y, and let g: X → k and f: Z → Y be
the canonical morphisms. By XIII.3.5 the morphism g, and therefore also f, is universally locally 1-aspherical for p′.
Since X is connected, f is 0-acyclic (SGA 4 XV 1.16). On the other hand, it follows from XIII.3.2 that, for every finite
p′-group C, (C_X,g) is cohomologically proper relative to k in dimension ≤ 1. It follows that (C_Z,f) is cohomologically
proper relative to Y in dimension ≤ 1 (XIII.1.5 c), and that f\*\*C*Z and R¹f\*\*C_Z are constant sheaves. Consequently
f satisfies all the hypotheses of XIII.4.2. \[Translator note: the French source says “g satisfies”; the surrounding
sentence and the use of XIII.4.2 require f: Z → Y.\] Thus one has the exact sequence

$$
\pi^{p'}_{1}(X_{b},c) \to \pi^{p'}_{1}(Z,c) \to \pi^{p'}_{1}(Y,b) \to 1.
$$

Moreover the composite morphism

$$
\pi^{p'}_{1}(X_{b},c) \to \pi^{p'}_{1}(Z,c) \to \pi^{p'}_{1}(Y,b)
$$

is an isomorphism, and one therefore has the exact sequence

$$
1 \to \pi^{p'}_{1}(X,a) \to \pi^{p'}_{1}(Z,c) \to \pi^{p'}_{1}(Y,b) \to 1.
$$

On the other hand, the morphism XIII.4.6.0 defines a morphism from this exact sequence to the exact sequence

```text
1 → π₁^{p′}(X,a) → π₁^{p′}(X,a) × π₁^{p′}(Y,b) → π₁^{p′}(Y,b) → 1,
```

and it follows that the morphism XIII.4.6.0 is an isomorphism.

### 4.7.

<!-- label: XIII.4.7 -->

Let

```text
X_s̄ → X_U → X
 |      |     |
 s̄  → U  → S
```

be a diagram whose squares are cartesian, where S is an arcwise connected scheme (SGA 4 IX 2.12), U is a connected open
subset of S, and s̄ is a geometric point of U. Let a be a geometric point of X_s̄ and let ℒ be a set of prime numbers. Let
g be a section of f and suppose the following conditions are satisfied:

a. The morphism f is 0-acyclic and locally 0-acyclic, and for every étale covering S′ of S and every étale covering E of
X ×*S S′ which is a quotient of a Galois covering with group an ℒ-group, (E,f*(S′)) is cohomologically proper relative
to S′ in dimension ≤ 0.

b. The morphism f_U is locally 1-aspherical for ℒ, and, for every constant finite sheaf of ℒ-groups F on X_U, (F,f_U) is
cohomologically proper in dimension ≤ 1 and the fibers of R¹f_U\*F are finite.

<!-- original page 423 -->

One then deduces from XIII.4.1 and XIII.4.3 the following commutative diagram, whose rows are exact:

<!-- label: eq:XIII.4.7.0 -->

```text
1 → π₁^ℒ(X_s̄,a) → π₁′(X_U,a) → π₁(U,a) → 1
      |                 |              |
      =                 |              |
1 → π₁^ℒ(X_s̄,a) → π₁′(X,a)   → π₁(S,a) → 1.
```

Thanks to the section g, one has morphisms

```text
π₁(U,a) → π₁′(X_U,a),    π₁(S,a) → π₁′(X,a);
```

from this one obtains a morphism from the amalgamated sum of π₁(S,a) and π₁′(X_U,a) over π₁(U,a) into π₁′(X,a):

<!-- label: eq:XIII.4.7.1 -->

```text
φ: π = π₁(S,a) ⨿_{π₁(U,a)} π₁′(X_U,a) → π₁′(X,a).
```

Suppose the following condition is satisfied:

c. If T = S − U, one has prof ét_T(S) ≥ 2 (SGA 2 XIV 1.1).

Then the functor which sends an étale covering of S to its restriction to U is fully faithful (SGA 2 XVI 1.4). It
follows that the morphism π₁(U,a) → π₁(S,a) is surjective (V.6.9), and one deduces from the diagram XIII.4.7.0 that the
same is true of the morphism

<!-- original page 424 -->

π₁′(X_U,a) → π₁′(X,a); a fortiori φ is an epimorphism. Let

<!-- label: eq:XIII.4.7.2 -->

$$
K = Ker(\pi_{1}(U,a) \to \pi_{1}(S,a)).
$$

The group $\pi$ of XIII.4.7.1 is identified with the quotient of $\pi_{1}'(X_{U},a)$ by the closed invariant subgroup
generated by the image $L$ of $K$ in $\pi_{1}'(X_{U},a)$. Regard $\pi_{1}'(X_{U},a)$ as the semidirect product of
$\pi_{1}(U,a)$ by $\pi^{\mathcal{L}}_{1}(X_{\bar{s}},a)$. Then $K$ operates by inner automorphisms on
$\pi^{\mathcal{L}}_{1}(X_{\bar{s}},a)$, and the quotient $\pi = \pi_{1}'(X_{U},a)/L$ is identified with the semidirect
product of $\pi_{1}(U,a)/K = \pi_{1}(S,a)$ by the group $\pi^{\mathcal{L}}_{1}(X_{\bar{s}},a)_{K}$ of coinvariants of
$\pi^{\mathcal{L}}_{1}(X_{\bar{s}},a)$ under $K$. Finally one has an epimorphism

<!-- label: eq:XIII.4.7.3 -->

```text
φ: π = π₁^ℒ(X_s̄,a)_K ⋅ π₁(S,a) → π₁′(X,a).
```

The following proposition gives conditions under which the morphism φ is an isomorphism.

**Subproposition.**

<!-- label: XIII.4.7.4 -->

The notation is that of XIII.4.7. Suppose that, in addition to conditions a), b), c), the following conditions are
satisfied:

d. For every point t of T = S − U, the morphism f is locally 1-aspherical for ℒ at g(t).

e. For every point t ∈ T, every irreducible component of the fiber X_t contains g(t), and, for every point x of X_t −
{g(t)} which is not maximal, one has

```text
prof_hop_x(X) ≥ 3     (SGA 2 XIV 1.2),
```

and the ring $\mathcal{O}_{X,x}$ is noetherian.

Then the morphism XIII.4.7.3 is an isomorphism.

As said above, the group π is identified with the quotient of π₁′(X_U,a) by the closed invariant subgroup L generated by
the image of K (XIII.4.7.2) in π₁′(X_U,a). This amounts to saying that π classifies the principal coverings Z of X_U
such that g_U⁻¹(Z) extends to an étale covering of S,

<!-- original page 425 -->

and which induce on X_s̄ a covering obtained by extension of the structural group from a principal covering whose group
is an ℒ-group. To prove that φ is an isomorphism, it is enough to show that such a covering Z extends to all of X.

First let us show that Z extends to an étale covering of an open subset containing X_U and g(S). Let W be a scheme étale
over X whose image contains X_U and g(S), and put W_U = W ×\_S U. Since the morphism W → S is 0-acyclic and since prof
ét_T S ≥ 2, one has

$$
prof \acute{e}t_{W-W_{U}} W \geq 2
$$

(SGA 2 XIV 1.13). Consequently, if Z|W_U extends to an étale covering of W, this extension is unique up to unique
isomorphism. It follows that the problem of extending Z to a neighborhood of g(S) ∪ X_U is local for the étale topology
near the points of g(T). If t is a point of T, put x = g(t), and write X̄, respectively S̄, for the strict localization of
X at x̄, respectively of S at t̄; write Ū = U ×\_S S̄, X̄_U = X̄ ×\_X X_U, and let ḡ: S̄ → X̄ be the morphism deduced from g.
It is enough to show that, for every point t of T, the inverse image Z̄ of Z on X̄_U extends to X̄, or equivalently is
trivial. By definition of Z, the inverse image of Z̄ on Ū is trivial. To prove that Z̄ is trivial, it is enough to show
that it has the form f̄_U*E, where E is a principal covering of Ū; indeed then E ≃ ḡ_U*f̄_U*E ≃ ḡ_U*Z̄, hence the result,
since ḡ_U\*Z̄ is trivial. But since the morphism f̄_U is 0-acyclic and locally 0-acyclic, to prove that Z̄ comes from Ū it
is enough to show that, for every algebraic geometric point above a point of Ū, which we may suppose to be the point s̄,
the restriction Z̄|X_s̄ is trivial (SGA 4 XV 1.15). Since Z̄|X_s̄ is obtained by extension of the structural group from a
principal covering whose group is an ℒ-group, this follows from the fact that the morphism f̄ is 1-aspherical for ℒ.

<!-- original page 426 -->

We have therefore shown that there exists an open neighborhood V of g(S) ∪ X_U such that Z extends to an étale covering
Z_V of V. Let us show that Z_V extends to all of X. It is enough to see that, for every point x of X − V, one has

```text
prof_hop_x X ≥ 3.
```

But this follows from hypothesis e) and from the fact that a point x of X − V cannot be maximal in its fiber X_t, since,
every irreducible component of X_t containing g(t), every maximal point of X_t belongs to V.

**Corollary.**

<!-- label: XIII.4.8 -->

The hypotheses are those of XIII.4.7.4, but suppose in addition that π₁(S,a) = 1. Then one has an isomorphism

<!-- label: eq:XIII.4.8.* -->

$$
\pi^{\mathcal{L}}_{1}(X,a) \simeq \pi^{\mathcal{L}}_{1}(X_{\bar{s}},a)_{K}.
$$

In particular, if π₁^ℒ(X_s̄,a) is topologically of finite presentation and if K operates on π₁^ℒ(X_s̄,a) through a group
of finite type, then π₁^ℒ(X,a) is topologically of finite presentation.

The isomorphism XIII.4.8.\* was proved in XIII.4.7.4. Suppose $\pi^{\mathcal{L}}_{1}(X_{\bar{s}},a)$ is the quotient of
the free pro-$\mathcal{L}$-group on $n$ generators $L(x_{1},\cdots,x_{n})$ by the closed invariant subgroup generated by
elements $y_{1},\cdots,y_{p}$ of $L(x_{1},\cdots,x_{n})$, and suppose $K$ acts through a group generated by elements
$k_{1},\cdots,k_{q}$. If, for every $i \in [1,n]$ and $j \in [1,q]$, $z_{ij}$ denotes an element of
$L(x_{1},\cdots,x_{n})$ lifting the element $(k_{j} \cdot x_{i})x^{-1}_{i}$, then
$\pi^{\mathcal{L}}_{1}(X_{\bar{s}},a)_{K}$ is the quotient of $L(x_{1},\cdots,x_{n})$ by the closed invariant subgroup
generated by the elements $(y_{i})_{i\in[1,p]}$ and $(z_{ij})_{i\in[1,n], j\in[1,q]}$.

**Remarks.**

<!-- label: rem:XIII.4.6 -->

[Translator note: the source notes that the original numbering returns here to 4.6.]

a. Conditions a) through e) of XIII.4.7 are satisfied when S is a connected normal scheme, U a dense retrocompact open
subset of S, and f a proper morphism of finite presentation, with geometrically connected and irreducible fibers at
every point t of T, f being moreover separable, smooth at the points of X_U ∪ g(T), ℒ being the set of prime numbers
distinct from the residual characteristics of S, and X being regular at every point of X_t. Indeed condition a) follows
from SGA 4 XV 4.1 and 1.4; conditions b) and d) follow from XIII.1.4 and SGA 4 XV 2.1 and XVI 5.2. Finally e) follows
from SGA 4 XIV 1.11.

<!-- original page 427 -->

b. Corollary XIII.4.8 applies to compute the fundamental group π₁^{p′}(X) of a proper smooth surface X over a separably
closed field k of characteristic p, where p′ denotes the set of prime numbers distinct from p. The method was
communicated to us by J. P. Murre; it consists in reducing, by blowing up X, to the case where one has a fibration X →
ℙ¹_k and an open subset U of ℙ¹_k satisfying the hypotheses of XIII.4.7 (see SGA 7 for more details). The same method
may be used more generally (loc. cit.) to prove that, if X is a connected k-scheme of finite type, and if the finite
type schemes of dimension ≤ dim X over an algebraic closure of k are strongly desingularizable (SGA 5 I 3.1.5), then
π₁^{p′}(X) is topologically of finite presentation.

## 5. Appendix I: Variations on Abhyankar’s Lemma

<!-- label: XIII.5 -->

This appendix contains different variants of Abhyankar’s lemma.

**Proposition.**

<!-- label: XIII.5.1 -->

Let X = Spec A be a regular local scheme, and let

$$
D = \Sigma_{1\leq i\leq r} div(f_{i})
$$

be a normal-crossings divisor, where the f_i are elements of the maximal ideal of A which form part of a regular system
of parameters. Let n_i, 1 ≤ i ≤ r, be integers ≥ 0 and put

```text
X′ = X[T₁,…,T_r]/(T₁^{n₁} − f₁, …, T_r^{n_r} − f_r),
```

and $U' = U \times_{X} X'$. Then $X'$ is regular and $U'$ is the complement in $X'$ of the normal-crossings divisor
$\Sigma_{1\leq i\leq r} div(T_{i})$. If the integers $n_{i}$ are prime to the residual characteristic $p$ of $X$, then
$U'$ is a connected étale covering of $U$, tamely ramified relative to $D$ (XIII.2.3 c).

Indeed $X'$ is the spectrum of a local ring $A'$ whose maximal ideal is generated by $T_{1},\cdots,T_{r}$. One may
suppose $r = \dim(A)$. Since $A'$ is finite and flat over $A$, hence of dimension $r$, $A'$ is regular (EGA `0_IV`
17.1.1), and the $T_{i}$ form a regular system of parameters of $A'$. Suppose the $n_{i}$ are prime to $p$. Since all
$f_{i}$ are invertible on $U$, the fact that $U'$ is étale over $U$ follows from I.7.4. Moreover $U'$ is tamely ramified
relative to $D$. Indeed, let $x_{i}$ be the generic point of $V(f_{i})$, let $\bar{R}$ be the strict localization of
$R = \mathcal{O}_{X,x_{i}}$, and let $\bar{K}$ be the fraction field of $\bar{R}$. Then the $\bar{K}$-algebra
representing $U'|\bar{K}$ is obtained from the field $\bar{K}[T_{i}]/(T^{n_{i}}_{i} - f_{i})$ by making an unramified
extension; it is therefore tamely ramified over $\bar{R}$.

**Proposition (Absolute Abhyankar Lemma).**

<!-- label: XIII.5.2 -->

Let X be a regular local scheme,

$$
D = \Sigma_{1\leq i\leq r} div(f_{i})
$$

a normal-crossings divisor as in XIII.5.1, let $Y = Supp D$, and let $U = X - Y$. Let $V$ be an étale covering of $U$,
tamely ramified relative to $D$. If $x_{i}$ is the generic point of the closed subset $V(f_{i})$, then
$\mathcal{O}_{X,x_{i}}$ is a discrete valuation ring with fraction field $K_{i}$, and one has

$$
V|K_{i} = \operatorname{Spec}(\Pi_{j\in J_{i}} L_{j}),
$$

where the L_j are finite separable extensions of K_i. Let n_j denote the order of the inertia group of a Galois
extension generated by L_j, and let n_i be the least common multiple of the n_j as j ranges over J_i. If one puts

```text
X′ = X[T₁,…,T_r]/(T₁^{n₁} − f₁, …, T_r^{n_r} − f_r),
```

and U′ = U\*(X′), V′ = V\*(X′), etc., then the étale covering V′ of U′ extends uniquely, up to unique isomorphism, to an
étale covering of X′, and the n_i are prime to the residual characteristic p of X.

Uniqueness follows from the fact that X′ is normal (XIII.5.1). Indeed, an étale covering of X′ extending V′ is
isomorphic to the normalization of X′ in the fiber of V′ at the generic point of X′ (I.10.2).

<!-- original page 429 -->

If x̄′ is a geometric point of Y′, write X̄′ for the strict localization of X′ at x̄′, V̄′ = V′_(X̄′), and so on. By descent,
taking uniqueness into account, it is enough to show that, for every geometric point x̄′ of Y′, the étale covering V̄′ of
Ū′ extends to X̄′. Since an étale covering of an open subset of the regular scheme X′ which contains all points x′ such
that dim 𝒪_{X′,x′} ≤ 1 extends to all of X (SGA 2 XIV 1.11), one may even restrict to the points x̄′ which project to a
maximal point of Y′. At such a point x̄′, the fact that V̄′ extends to an étale covering of X̄′ follows from X.3.6.

Let us show that the n_i are prime to p. Indeed, otherwise one would have, for instance, p | n₁. After replacing X by

```text
X[T₁,…,T_r]/(T₁^{n₁/p} − f₁, T₂^{n₂} − f₂, …, T_r^{n_r} − f_r),
```

one is reduced to the case $X' = X[T_{1}]/(T^{p}_{1} - f_{1})$. It is enough to show that $V$ extends to an étale
covering of $X$, since then $n_{1} = 1$, contrary to the hypothesis. For this one may suppose $X$ strictly local. Let
$Z$ be the closed subscheme of $X$ defined by $p = 0$ and let $Z_{1} = Z \cap X_{f_{1}}$; $Z_{1}$ is a nonempty open
subset of $Z$. By what precedes, the étale covering $V'$ of $U'$ extends to an étale covering $W'$ of $X'$. Let
$W''_{1}$ and $W''_{2}$ be the inverse images of $W'$ by the two projections `X″ = X′ ×_X X′ ⇉ X′`, and let us show that
the descent isomorphism $u: W''_{1}|U'' \to W''_{2}|U''$ extends to an $X''$-morphism $W''_{1} \to W''_{2}$, which will
necessarily be descent data on $W'$ relative to $X' \to X$. Let $Z''$, respectively $Z''_{1}$, be the inverse image of
$Z$, respectively $Z_{1}$, in $X''$. Since the morphism $Z'' \to Z$ is radicial, there exists an isomorphism
$v: W''_{1}|Z'' \to W''_{2}|Z''$ extending the isomorphism $u|Z''_{1}$. But since $X$ is henselian, one has a bijection

$$
\operatorname{Hom}_{X}''(W''_{1},W''_{2}) \simeq \operatorname{Hom}_{Z}''(W''_{1}|Z'',W''_{2}|Z''),
$$

whence a morphism w: W″₁ → W″₂ lifting v. The subscheme of X″ over which u and w coincide is both open

<!-- original page 430 -->

and closed and contains Z″₁, hence is equal to X″; this proves that V extends to X.

#### 5.3.0.

<!-- label: XIII.5.3.0 -->

Resume the hypotheses and notation of XIII.5.2, assuming moreover that X is strictly local. \[Translator note: the
corrected source fixes “S” to “X” here.\] It then follows from loc. cit. that every connected étale covering of U,
tamely ramified relative to D, is a quotient of a tamely ramified covering of the form

```text
U′ = U[T₁,…,T_r]/(T₁^{n₁} − f₁, …, T_r^{n_r} − f_r),
```

where the $n_{i}$ are integers prime to $p$. Let $\mu_{n}$ be the group of $n$-th roots of unity of $U$. The group of
$U$-automorphisms of $U'$ is just the group $\mu_{n_{1}} \times \cdots \times \mu_{n_{r}}$, an $n_{i}$-th root of unity
$\xi_{i}$ acting on $U'$ by sending $T_{i}$ to `ξ_iT_i`. Thus one has the following statement.

**Corollary.**

<!-- label: XIII.5.3 -->

Let $X$ be a strictly local regular scheme of residual characteristic $p \geq 0$, let
$D = \Sigma_{1\leq i\leq n} div(f_{i})$ be a normal-crossings divisor on $X$, and let $U = X - Supp D$. Put

```text
Ũ = lim_{(n_i)} U[T₁,…,T_r]/(T₁^{n₁} − f₁, …, T_r^{n_r} − f_r),
```

the projective limit being taken over the filtered ordered set, for divisibility, of families of integers n_i > 0 prime
to p. Then Ũ is a universal tamely ramified covering of U. Consequently the tamely ramified fundamental group of U is

```text
π₁^tame(U) ≃ Π_{ℓ≠p} ℤ_ℓ[1]^r       (canonical isomorphism),
```

where $\mathbb{Z}_{\ell}[1] = \lim_{n>0} \mu_{\ell^{n}}$. The group $\pi^{tame}_{1}(U)$ is noncanonically isomorphic to
$\Pi_{\ell\neq p} \mathbb{Z}^{r}_{\ell}$.

**Proposition.**

<!-- label: XIII.5.4 -->

Let $f: X \to S$ be a morphism of schemes, and let $D = \Sigma_{1\leq i\leq r} div(f_{i})$ be a normal-crossings divisor
relative to $S$ (XIII.2.1), where,

<!-- original page 431 -->

for each point $x$ of $Y = Supp D$, if $I(x) \subset [1,r]$ is the set of $i$ such that $f_{i}(x) = 0$, the subscheme
$V((f_{i})_{i\in I(x)})$ is smooth over $S$ of codimension `card I(x)` in $X$. Let $U = X - Y$. Let $x$ be a point of
$Y$, $X_{1} = \operatorname{Spec} \mathcal{O}_{X,x}$, $U_{1} = U \times_{X} X_{1}$, let $n_{i}$, $i \in I(x)$, be
integers, and put

$$
X' = X[T_{i}]_{i\in I(x)}/(T^{n_{i}}_{i} - f_{i}).
$$

Then, if x′ is the point of X′ above x, X′ is smooth over S at x′. If the integers n_i are prime to the characteristic p
of κ(x), then U′₁ = U₁ ×\_X X′ is a connected étale covering of U₁, tamely ramified over X₁ relative to S₁ (XIII.2.1.1).

If $s = f(x)$, the geometric fiber $X'_{\bar{s}}$ is regular at $x'$ (XIII.5.1); since $X'$ is flat over $S$ in a
neighborhood of $Y$, this proves that $X'$ is smooth over $S$ at $x'$ (EGA IV 12.1.6). If the integers $n_{i}$ are prime
to $p$, $U'_{1}$ is an étale covering of $U_{1}$ (I.7.4); it is tamely ramified over $X_{1}$ relative to $S$ because
this is true on the geometric fibers over every point of $S$ (XIII.5.1). Finally, the fact that $U'_{1}$ is connected
follows from SGA 4 XVI 3.2.

**Proposition (Relative Abhyankar Lemma).**

<!-- label: XIII.5.5 -->

Let X be an S-scheme, and let D be a normal-crossings divisor relative to S as in XIII.5.4. Let Y = Supp D, U = X − Y,
let x be a point of Y, let X₁ be the strict localization of X at a geometric point above x, let U₁ = U ×\_X X₁, and let
V₁ be an étale covering of U₁. Suppose that, for every maximal point s of S, V₁_s̄ is tamely ramified over X₁_s̄ relative
to s̄. Then one can find integers n_i prime to the characteristic p of κ(x), with i ∈ I(x), such that, if one puts

$$
X'_{1} = X_{1}[T_{i}]_{i\in I(x)}/(T^{n_{i}}_{i} - f_{i}),
$$

and $U'_{1} = U_{1} \times_{X_{1}} X'_{1}$, etc., the étale covering $V'_{1}$ of $U'_{1}$ extends uniquely, up to unique
isomorphism, to an étale covering of $X'_{1}$. In particular

<!-- original page 432 -->

V₁ is tamely ramified over X₁ relative to S.

We may suppose $S$ local noetherian with closed point $f(x)$. For each maximal point $s$ of $S$ and each $i \in I(x)$,
let $x_{i}$ be the generic point of the closed subset $V(f_{i})$ of the fiber `X₁_s̄`. The local ring
$(\mathcal{O}_{X_{1},x_{i}})_{red}$ is a discrete valuation ring with fraction field $K_{i}$, and one has

$$
V_{1}|K_{i} = \operatorname{Spec}(\Pi_{j\in I(x_{i})} L_{j}),
$$

where L_j is a finite separable extension of K. Let n_j be the order of the inertia group of a Galois extension
generated by L_j, and let n_i be the least common multiple of the n_j as s ranges over the maximal points of S and j ∈
I(x_i). [Translator note: the corrected source replaces J(x_i) by I(x_i) in this passage.]

With the $n_{i}$ so chosen, we shall show that $V'_{1}$ extends uniquely to an étale covering of $X'_{1}$. Uniqueness
follows from the fact that, since $X'$ is smooth over $S$ at the points of $Y$, one has
$prof \acute{e}t_{Y'_{1}}(X'_{1}) \geq 2$ (SGA 4 XVI 3.2 or SGA 2 XIV 1.19). Let $x'_{1}$ be a point of $Y'_{1}$, let
$\bar{x}'_{1}$ be a geometric point above $x'_{1}$, and write $\bar{X}'_{1}$ for the strict localization of $X'_{1}$ at
$\bar{x}'_{1}$, `Ū′₁ = U′₁_(X̄′₁)`, and so on. By descent, taking uniqueness into account, it is enough to show that
$\bar{V}'_{1}$ extends to $\bar{X}'_{1}$. Moreover one may restrict to maximal points $x'_{1}$ of $Y'_{1}$. Indeed, then
one will have an extension of $V'_{1}$ over an open subset $W'_{1}$ of $X'_{1}$ containing the maximal points of
$Y'_{1}$; if $Z'_{1} = X'_{1} - W'_{1}$, then `codim(Z′₁_s,X′₁_s) ≥ 2` when $s$ is a maximal point of $S$, and
`codim(Z′₁_s,X′₁_s) ≥ 1` and $prof \acute{e}t_{s}(S) \geq 1$ when $s$ is a nonmaximal point of $S$. The fact that
$V'_{1}$ extends to all of $X'_{1}$ then follows from SGA 2 XIV 1.20. But, at a geometric point $\bar{x}'_{1}$ above a
maximal point of $Y'_{1}$, `X′₁_red` is the spectrum of a discrete valuation ring, and the fact that $\bar{V}'_{1}$
extends to $\bar{X}'_{1}$ follows from X.3.6.

Let us show that the $n_{i}$ are prime to $p$. Indeed, otherwise there would be an index $i_{0} \in I(x)$ such that $p$
divides $n_{i_{0}}$. After replacing $X$ by

```text
X₁[T_{i₀},T_i]_{i∈I(x)}/(T_{i₀}^{n_{i₀}/p} − f_{i₀}, T_i^{n_i} − f_i),
```

one is reduced to the case $X'_{1} = X_{1}[T]/(T^{p} - f_{i_{0}})$. By what precedes, the étale covering

<!-- original page 433 -->

$V'_{1}$ of $U'_{1}$ extends to an étale covering $E'_{1}$ of $X'_{1}$. Let $\eta$ be the closed point of $S$; since the
morphism $X'_{1}\eta \to X_{1}\eta$ is radicial, $V_{1}\eta$ extends to an étale covering $E_{1}\eta$ of $X_{1}\eta$.
One then deduces, as in XIII.5.2, that $E'_{1}$ is endowed with descent data relative to the morphism
$X'_{1} \to X_{1}$, extending the natural descent data on $E'_{1}|U'_{1}$. It follows that $V_{1}$ extends to $X_{1}$;
but this implies $n_{i_{0}} = 1$, contrary to the hypothesis $n_{i_{0}} = p$.

**Corollary.**

<!-- label: XIII.5.6 -->

Let $X$ be an $S$-scheme, and let $D = \Sigma_{1\leq i\leq r} div(f_{i})$ be a normal-crossings divisor relative to $S$,
as in XIII.5.4. Let $\bar{x}$ be a geometric point of $X$, let $\bar{X}$ be the strict localization of $X$ at $\bar{x}$,
let $\bar{Y} = Y_{\bar{X}}$, $\bar{U} = \bar{X} - \bar{Y}$, and

```text
Ũ = lim_{(n_i)} Ū[T_i]_{i∈I(x)}/(T_i^{n_i} − f_i),
```

the projective limit being taken over the filtered set of families of integers n_i > 0, prime to the characteristic p of
κ(x). Then Ũ is a universal tamely ramified covering of Ū relative to S. Consequently the tamely ramified fundamental
group of Ū is

```text
π₁^tame(Ū) ≃ Π_{ℓ≠p} ℤ_ℓ[1]^{I(x)}       (canonical isomorphism).
```

The group $\pi^{tame}_{1}(\bar{U})$ is noncanonically isomorphic to $\Pi_{\ell\neq p} \mathbb{Z}^{I(x)}_{\ell}$.

**Subremark.**

<!-- label: XIII.5.6.1 -->

Let $X$ be an $S$-scheme, let $D = \Sigma_{1\leq i\leq r} div(f_{i})$ be a normal-crossings divisor relative to $S$, as
in XIII.5.4, and let $U = X - Supp D$. For every subset $I \subset [1,r]$, put

```text
X_I = (⋂_{i∈I} V(f_i)) ∩ (⋂_{i∈complement I} X_{f_i}).
```

Let p be a prime integer or zero, and let Z be a subset of X_I all of whose points have characteristic p. Let

<!-- original page 434 -->

```text
Ũ_I = lim_{(n_i)} U[T_i]_{i∈I}/(T_i^{n_i} − f_i),
```

where the projective limit is taken over the filtered set of families of integers n_i > 0 prime to p. \[Translator note:
the corrected source supplies the missing index set i\in I in U[T_{i}].\] Then, for every geometric point x̄ of Z, the
inverse image of Ũ_I on Ū is identified with the universal tamely ramified covering of Ū.

**Corollary.**

<!-- label: XIII.5.7 -->

The notation is that of XIII.5.6. Let S̄ be the strict localization of S at x̄, and let

```text
ḡ: Ū → S̄,     g̃: Ũ → S̃
```

be the canonical morphisms. Then the morphisms ḡ and g̃ are 0-acyclic (SGA 4 XV 1.3). Let G be a constructible sheaf of
groups on S̄, let F = ḡ\*G, and let P be a torsor under F. Then P is tamely ramified over X̄ relative to S̄ if and only if
its inverse image P̃ on Ũ is trivial.

Indeed, for every scheme

$$
\bar{X}' = \bar{X}[T_{i}]_{i\in I(x)}/(T^{n_{i}}_{i} - f_{i}),
$$

where the n_i are integers > 0 prime to p, the morphism f̄′: X̄′ → S̄ is 0-acyclic. The geometric fibers of f̄′ at the
various points of S̄ are therefore connected, indeed irreducible. The same is therefore true of the geometric fibers of
the morphisms ḡ′: Ū′ → S̄, which proves that the ḡ′, and hence also g̃, are 0-acyclic (SGA 4 XV 1.16).

It is clear that a torsor P on Ū with group F whose inverse image on Ũ is trivial is tamely ramified over X̄ relative to
S̄. Conversely, let us show that, if P is tamely ramified over X̄ relative to S̄, its inverse image on Ũ is trivial.

It follows from SGA 4 IX 2.14(ii) that one can find a finite morphism $n: S_{1} \to \bar{S}$, a constant sheaf of groups
$C$ on $S_{1}$, and a monomorphism $G \to n_{*}C$. Consider the following commutative diagram with cartesian squares:

```text
Ũ₁ → U₁ --g₁→ S₁
 |     |q       |n
 r     |        |
Ũ  → Ū --ḡ→ S̄.
```

<!-- original page 435 -->

Let C₁, respectively C̃₁, be the inverse image of C on U₁, respectively on Ũ₁. One has a commutative diagram in which i
and j are isomorphisms (SGA 4 VIII 5.8):

<!-- label: eq:XIII.5.7.* -->

```text
H¹(Ū,q_*C₁) --i→ H¹(U₁,C₁)
      |              |
      v              v
H¹(Ũ,r_*C̃₁) --j→ H¹(Ũ₁,C̃₁).
```

Let Q be the torsor under q\*\*C₁ deduced from P by extension of the structural group F → q\*\_C₁. By XIII.2.1.4, Q is
tamely ramified over X̄ relative to S̄. Via i, the torsor Q corresponds to a torsor Q₁ under C₁, and it is clear that Q₁
is tamely ramified over X₁ = X̄ ×_S̄ S₁ relative to S₁. It therefore follows from XIII.5.6 that the inverse image Q̃₁ of Q₁
on Ũ₁ is trivial, and the diagram XIII.5.7._ then shows that the inverse image Q̃ of Q on Ũ is trivial.

Consider the following commutative diagram, whose second row is exact (SGA 4 XII 3.1):

<!-- label: eq:XIII.5.7.** -->

```text
H⁰(S̄,n_*C/G) → H¹(S̄,G) = 1
      |k              |
      v              v
H⁰(Ũ,r_*C̃₁/F̃) → H¹(Ũ,F̃) → H¹(Ũ,r_*C̃₁).
```

Since the morphism Ũ → S̄ is 0-acyclic, k is an isomorphism. The fact that P̃ is trivial follows from XIII.5.7.\*\*.

## 6. Appendix II: Finiteness Theorem for Direct Images of Stacks

<!-- label: XIII.6 -->

**Proposition.**

<!-- label: XIII.6.1 -->

Let S be a locally noetherian scheme, and let f: X → S be a morphism. If S′ is an S-scheme, write X′, respectively f′,
and so on, for the inverse image of X, respectively f, and so on, by the morphism S′ → S. Suppose that, for every scheme
S′ étale over S and every constructible sheaf of sets F on X′, f′_\*F is constructible, and that, for every
constructible sheaf of groups F on X′, R¹f′_\*F is constructible.

<!-- original page 436 -->

Let $\Phi$ be a 1-constructible stack on $X$ (XIII.0). Then $f_{*}\Phi$ is 1-constructible.

For every scheme $S'$ étale over $S$ and every object $x$ of $(f_{*}\Phi)_{S}'$, one has an isomorphism

$$
SheafAut_{S}'(x) \simeq f'_{*}SheafAut_{X}'(x),
$$

where, on the right-hand side, $x$ is regarded as an object of $\Phi_{X}'$. The hypotheses made therefore imply that
$f_{*}\Phi$ is constructible. Let $S\Phi$ be the sheaf of maximal subgerbes of $\Phi$ (Giraud, III 2.1.7). Since
$f_{*}(S\Phi)$ is constructible, one may apply SGA 4 IX 2.7 to it, and the fact that $f_{*}\Phi$ is 1-constructible then
follows from the lemma below.

**Sublemma.**

<!-- label: XIII.6.1.1 -->

Let S be a locally noetherian scheme, let f: X → S be a morphism, and let Φ be a stack on X. Suppose given a sheaf on S,
representable by an étale S-scheme of finite type T, a surjective morphism

$$
a: T \to f_{*}(S\Phi),
$$

and an object $p$ of the fiber $\Phi_{X_{T}}$, where $X_{T} = X \times_{S} T$, defining in
$f_{*}(S\Phi)(T) = S\Phi(X_{T})$ an element equal to the image $q$ by $a$ of the identity section of $T(T)$. Let
$f_{T}: X_{T} \to T$ be the canonical morphism and suppose that the sheaf `R¹f_{T_*}(SheafAut_X_T(p))` is constructible.
Then the same is true of $S(f_{*}\Phi)$.

The canonical morphism $f*f_{*}\Phi \to \Phi$ gives a morphism

$$
S(f*f_{*}\Phi) \simeq f*(S(f_{*}\Phi)) \to S\Phi,
$$

hence a canonical morphism

$$
\phi: S(f_{*}\Phi) \to f_{*}(S\Phi).
$$

<!-- original page 437 -->

Let $F = S(f_{*}\Phi)$ and let $G$ be the image of $F$ by $\phi$. By SGA 4 IX 2.9, $G$ is a constructible sheaf.

It is enough to show that, for every point s of S, there exists a nonempty open neighborhood U of s such that F|U is
locally constant constructible. Let s ∈ S, let s̄ be a geometric point above s, and let q̄₁,…,q̄_n be the elements of G_s̄.
By definition of T, there exist S-morphisms h_i: s̄ → S′ such that q̄_i = h_i\*(q). Let S′ be the fiber product over S of
n schemes isomorphic to T, let s̄ → S′ be the fiber product of the h_i, let X′ = X ×\_S S′, and let q_i, respectively
p_i, be the inverse image of q, respectively p, by the i-th projection from S′ to T. If Ψ_i is the maximal subgerbe of
Φ|X′ generated by p_i, then the sheaf

$$
F_{i} = R^{1}f'_{*}(SheafAut_{X}'(p_{i}))
$$

is just the sheaf S(f′_\*Ψ_i) of maximal subgerbes of f′_\*Ψ_i. In particular, the canonical injection Ψ_i → Φ|X′ gives
a morphism

$$
\alpha_{i}: F_{i} \to F|S'.
$$

We shall show that $\alpha_{i}$ is a bijection from $F_{i}$ onto the inverse image of $q_{i}$ in $F|S'$. For every
scheme $S''$ étale over $S'$, every section $y$ of $F_{i}(S'')$ has image $q_{i}|S''$ in $F(S'')$, because locally for
the étale topology on $S''$, $y$ is defined by an object $x$ of $\Phi_{X}''$ which is isomorphic to $p_{i}|X''$.
Conversely, if $y \in F(S'')$ has image $q_{i}|S''$ in $F(S'')$, then locally for the étale topology on $S''$, $y$ is
defined by an object $x$ of $\Phi_{X}''$ which is isomorphic to $p_{i}$; hence $x$ is an object of $\Psi_{i,X''}$, and
therefore $y \in F_{i}(S'')$.

The proof is completed by using XIII.6.1.2 below. Indeed, one can find an open neighborhood U′ of s such that
q₁|U′,…,q_n|U′ are sections of G(U′) and generate this sheaf. Since the F_i|U′ and G|U′ are constructible, so is F|U′ by
XIII.6.1.2; after possibly replacing U by a smaller open subset, F|U is locally constant, completing the proof.

**Sublemma.**

<!-- label: XIII.6.1.2 -->

Let

<!-- original page 438 -->

S be a locally noetherian scheme, and let F → G be a surjective morphism of sheaves of groups on S. Let q_i be a finite
family of sections of G on X which generate G, and, for each i, let F_i be the subsheaf of F inverse image of q_i. Then,
if G and the F_i are constructible, so is F.

To prove that F is constructible, it is enough to show that, for every point s of S, there exists an open neighborhood U
of s such that F|U is locally constant constructible. Let s be a point of S. Since the sheaves F_i and G are
constructible, one can find an open neighborhood U of s such that F_i|U and G|U are locally constant. Let us then show
that F|U is locally constant. By SGA 4 IX 2.13(i), it is enough to see that, if s̄ is a geometric point above s, s̃ is a
geometric point of U, and s̄ → s̃ is a specialization morphism, the canonical morphism

$$
F_{\tilde{s}} \to F_{\bar{s}}
$$

is bijective.

Consider the commutative diagrams

```text
(F_i)_s̃ --ã_i→ F_s̃ --ã→ G_s̃
    |≃          |b        |≃
    v           v         v
(F_i)_s̄ --ā_i→ F_s̄ --ā→ G_s̄.
```

Let $\bar{q}_{i}$, respectively $\tilde{q}_{i}$, be the inverse image of $q_{i}$ in $G_{\bar{s}}$, respectively
$G_{\tilde{s}}$. The morphisms `ā` and `ã` are surjective, and $\bar{a}_{i}$, respectively $\tilde{a}_{i}$, induces a
bijection from $(F_{i})_{\bar{s}}$, respectively $(F_{i})_{\tilde{s}}$, onto $\bar{a}^{-1}(q_{i})$, respectively
$\tilde{a}^{-1}(q_{i})$. It therefore follows from the diagram above that $b$ is an isomorphism.

**Corollary.**

<!-- label: XIII.6.2 -->

Let

<!-- original page 439 -->

$S$ be a locally noetherian scheme and let $f: X \to S$ be a proper morphism. Let $\Phi$ be a 1-constructible stack on
$X$. Then $f_{*}\Phi$ is a 1-constructible stack.

The proof of XIII.6.1 also proves the following result, in view of XIII.2.4 2).

**Corollary.**

<!-- label: XIII.6.3 -->

Let $S$ be a locally noetherian scheme, let $f: X \to S$ be a morphism, let $D$ be a divisor on $X$ with normal
crossings relative to $S$ (XIII.2.1), let $Y = Supp D$, $U = X - Y$, and let $i: U \to X$ be the canonical immersion.
Let $\Phi$ be a stack on $U$ given, locally for the étale topology on $X$ and $S$, as the inverse image of a
1-constructible stack $\Psi$ on $S$. Then the stack $i^{tame}_{*} \Phi$ is 1-constructible.

## Bibliography

1. J. Giraud, _Cohomologie non abélienne de degré 2_, thesis, Paris (1966).

1. J. Giraud, _Cohomologie non abélienne_, Springer, Berlin-New York (1971).

1. H. Seifert and W. Threlfall, _Lehrbuch der Topologie_, Chelsea, New York (1934).

1. J.-P. Serre, _Cohomologie galoisienne_, Lecture Notes no. 5, Springer, Berlin (1964).

1. J.-P. Serre, _Corps locaux_, Hermann, Paris (1962).


<!-- SOURCE: README.md -->

# SGA 1: Étale Coverings and the Fundamental Group

*Séminaire de Géométrie Algébrique du Bois-Marie*, 1960–61.

A. Grothendieck, with two additional Exposés by Mme M. Raynaud. First published as Lecture Notes in Mathematics 224
(Springer-Verlag, 1971); reissued in the SMF *Documents Mathématiques* series with editorial updates by M. Raynaud. The
LaTeX 2e composition was carried out by a volunteer project directed by Bas Edixhoven.

## Abstract

This volume develops the foundations of a theory of the fundamental group in algebraic geometry, from the "Kroneckerian"
point of view that allows the case of an algebraic variety in the usual sense and the case of the ring of integers of a
number field to be treated on the same footing. Exposés I–IV present the local notions of *étale* and *smooth* morphism;
Exposé V gives the axiomatic description of the fundamental group of a scheme, recovering the usual Galois theory in the
case of a field; Exposés VI and VIII develop faithfully flat descent (with Exposé VII, on descent in general categories,
omitted and supplied later by Giraud's *Méthodes de la descente*); Exposé IX applies descent to the étale case,
obtaining Van Kampen–type theorems; Exposé X proves the specialization theorem for the fundamental group under a proper
smooth morphism, and uses it to determine, up to nearly precise specifications, the fundamental group of a smooth
algebraic curve in positive characteristic; Exposé XI gives examples and complements (Kummer and Artin–Schreier theory
cohomologically); Exposé XII (Mme Raynaud) treats analytification and GAGA-type comparison; Exposé XIII (Mme Raynaud)
gives the étale-cohomological refinement of the theory, drawing on SGA 4 and SGA 5.

## Reading order

Files are numbered so alphanumeric order matches reading order.

- [Title page, abstract, and preface (Edixhoven et al.)](00-title-preface.md)
- [Introduction (Grothendieck, August 1970)](00-introduction.md)
- [Foreword to the original notes (Grothendieck)](00-avertissement.md)
- [Exposé I — Étale morphisms](01-morphismes-etales.md)
- [Exposé II — Smooth morphisms: generalities, differential properties](02-morphismes-lisses-generalites-proprietes-differentielles.md)
- [Exposé III — Smooth morphisms: extension properties](03-morphismes-lisses-proprietes-de-prolongement.md)
- [Exposé IV — Flat morphisms](04-morphismes-plats.md)
- [Exposé V — The fundamental group: generalities](05-le-groupe-fondamental-generalites.md)
- [Exposé VI — Fibered categories and descent](06-categories-fibrees-et-descente.md)
- [Exposé VII — Does not exist](07-n-existe-pas.md)
- [Exposé VIII — Faithfully flat descent](08-descente-fidelement-plate.md)
- [Exposé IX — Descent of étale morphisms; application to the fundamental group](09-descente-des-morphismes-etales.md)
- [Exposé X — Theory of specialization of the fundamental group](10-theorie-de-la-specialisation-du-groupe-fondamental.md)
- [Exposé XI — Examples and complements](11-exemples-et-complements.md)
- [Exposé XII — Algebraic geometry and analytic geometry (Mme Raynaud)](12-geometrie-algebrique-et-geometrie-analytique.md)
- [Exposé XIII — Cohomological properness of sheaves of sets and of noncommutative groups (Mme Raynaud)](13-proprete-cohomologique.md)
- [Index of notation](zz-index-notations.md)
- [Translation glossary](glossary.md)

## Reference convention

Following the source, SGA 1 is cited as `(Exp. N, M.K)` where $N$ is the Exposé Roman numeral and `M.K` is the decimal
numbering inside that Exposé — for example `(V, 4.1)` for statement 4.1 of Exposé V. A bare `4.1` refers to the
statement of that name in the same Exposé. Cross-references to other SGA volumes use the parallel form (e.g.
`SGA 2 III, 1.2`), and citations to the *Éléments de Géométrie Algébrique* use `EGA X, x.y.z`.

## Editorial conventions

- **Terminology**. SGA 1 retains the historical SGA/EGA distinction between *prescheme* (`préschéma`) and *scheme*
  (`schéma`, in the older sense of separated prescheme); the translation honors this throughout. The Introduction notes
  that the old term *simple morphism* was replaced during preparation by *smooth morphism*, and the translation uses
  *smooth morphism* uniformly.

- **Update markers `(MR)`**. The SMF re-edition incorporated several editorial updates by Michel Raynaud, delimited in
  the source by square brackets `[ ]` and marked `(MR)`. These appear on pages X.2.14, XI.1.4, XII.5.6, XIII.2.13, and
  footnote III.6.6.p24. The translation preserves the `(MR)` markers in place.

- **Footnotes**. Original Séminaire footnotes use short slugs like $[{}^{I}-3-1]$. Footnotes added in the SMF re-edition
  are reproduced verbatim where they appear in the source.

- **Page marks**. HTML comments `<!-- original page N -->` mark the start of page $N$ in the SMF re-edition, whose
  pagination is preserved in the margin of the LaTeX source.

- **Mathematics**. Mathematics is written with Unicode and wrapped in backticks where formatter mangling is a risk (most
  identifier-rich expressions). Displayed equations use fenced ```` ```text ```` blocks, optionally pinned with
  `<!-- label: eq:N.X.Y -->`.

- **Residue fields**. Per the SMF preface, the residue field of a point $x$ is denoted $\kappa(x)$, and the residue
  field of a local ring $A$ is denoted $\kappa(A)$.

## Provenance

This is a translation, not a critical edition. The authoritative text remains the French SMF *Documents Mathématiques*
edition (arXiv $math.AG/0206203$, $orig=false$ corrected variant) derived from the 1971 Springer LNM 224 typescript by
the LaTeX 2e volunteer project of B. Edixhoven, with editorial updates by M. Raynaud. For any claim that matters
mathematically, consult the source: this English version exists to make the volume readable, not to replace it.


<!-- SOURCE: glossary.md -->

# Glossary

This glossary records translation choices for the SGA 1 Markdown translation.

| French                    | English                 | Note                                                                   |
| ------------------------- | ----------------------- | ---------------------------------------------------------------------- |
| préschéma                 | prescheme               | Historical SGA/EGA terminology; do not silently modernize to “scheme”. |
| schéma                    | scheme                  | Preserve the source’s distinction from “prescheme”.                    |
| revêtement étale          | étale covering          | Use “étale cover” only where the prose idiom is clearly better.        |
| morphisme étale           | étale morphism          | Standard.                                                              |
| morphisme lisse           | smooth morphism         | Replaces the older “simple morphism” noted in the introduction.        |
| morphisme plat            | flat morphism           | Standard.                                                              |
| descente fidèlement plate | faithfully flat descent | Standard.                                                              |
| catégorie fibrée          | fibered category        | Use American spelling for consistency.                                 |
| champ                     | stack                   | In Exposé XIII, in the SGA/Giraud sense.                               |
| spécialisation            | specialization          | Use American spelling for consistency.                                 |
| corps résiduel            | residue field           | Denoted κ(x) or κ(A).                                                  |
| groupe fondamental        | fundamental group       | Standard.                                                              |
| topologie étale           | étale topology          | Standard.                                                              |
| ramification modérée      | tame ramification       | Standard.                                                              |
| premier à p               | prime to p              | Use in prose; avoid TeX notation.                                      |


<!-- SOURCE: zz-index-notations.md -->

# Index of notation

<!-- label: I.index-notations -->

A reference index of notation used throughout SGA 1. Locators are given as `<Exposé Roman>.<section>(.<sub>)` or
$<Expos\acute{e} Roman> (p. <page>)$ when known; the source's OCR-extracted index does not carry page locators, so the
locator column reconstructs them from first use in the relevant Exposé. Where the OCR mangled an identifier (most
commonly by dropping the $\pi$ prefix in $\pi_{1}(...)$ or the script-O / hat over a category), the original symbol is
restored and the restoration noted. Unresolved cases are marked with a translator note rather than silently fixed.

## Sheaves of differentials and infinitesimal neighborhoods (Exposés II–III)

| Notation                                                                                                                                                                                  | Where introduced |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| $\Delta_{X/Y}$, or simply $\Delta$                                                                                                                                                        | II.1             |
| $\Omega^{1}_{X/Y}$ (sheaf of relative differentials)                                                                                                                                      | II.1             |
| $\mathcal{P}^{n}_{X/Y}$ (sheaf of principal parts of order $n$) <!-- TRANSLATOR NOTE: source has the script-O artefact `𝓞P_X/Y^n`; canonical EGA IV notation `𝒫^n_{X/Y}` is restored. --> | II.1             |
| $\Delta^{n}_{X/Y}$ (n-th infinitesimal neighborhood of the diagonal)                                                                                                                      | II.1             |
| $\mathcal{m}\Delta_{X/Y}$ (ideal sheaf of the diagonal) <!-- TRANSLATOR NOTE: source `𝔪d_X/Y`; the `d` is a misrendered Δ. -->                                                            | II.1             |
| $d^{n}_{X/S}$ (n-th differential / iterated differential)                                                                                                                                 | II               |
| $\mathcal{m}g_{X/S}$ <!-- TRANSLATOR NOTE: source `𝔪g_X/S`; symbol not fully resolved — `g` likely denotes a generic ideal sheaf or a graded component. -->                               | II               |

## Categories, morphisms, and 2-categorical infrastructure (Exposé VI)

| Notation                                                                                                                                                                                                                   | Where introduced |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `C(...)` (a category) <!-- TRANSLATOR NOTE: source `𝓞C( )`; the leading script-O is an OCR artefact attached to the category symbol throughout. -->                                                                        | VI               |
| `Pro-C(...)` (pro-objects of $C$)                                                                                                                                                                                          | VI               |
| $\Gamma$ (sections / global-section functor; context-dependent)                                                                                                                                                            | VI               |
| `(Ens)` (category of sets)                                                                                                                                                                                                 | VI               |
| `Cat` (category of categories)                                                                                                                                                                                             | VI               |
| $Ob(C)$ (objects of $C$)                                                                                                                                                                                                   | VI               |
| $Fl(C)$ (arrows / "fleches" of $C$)                                                                                                                                                                                        | VI               |
| $\operatorname{Hom}(C, C')$ (functors $C \to C'$)                                                                                                                                                                          | VI               |
| $C^{\circ}$ (opposite category)                                                                                                                                                                                            | VI               |
| $Cat_{/E}$ (categories over $E$ / fibered over $E$)                                                                                                                                                                        | VI               |
| $\operatorname{Hom}_{E/-}(F, G)$ (cartesian functors over $E$)                                                                                                                                                             | VI               |
| $v\ast u$ (vertical composition of 2-cells / Godement product) <!-- TRANSLATOR NOTE: source `v*u`; interpreted as horizontal/vertical composition in the 2-category of fibered categories. -->                             | VI               |
| $F \times_{E} G$ (fibre product of fibered categories) <!-- TRANSLATOR NOTE: source `𝓞F×_𝓞E𝓞G`. -->                                                                                                                        | VI               |
| $f^{\ast}: Cat_{/E} \to Cat_{/E'}$ (base change of fibered categories) <!-- TRANSLATOR NOTE: source `^*: Cat_/𝓞E→ Cat_/𝓞E'`. -->                                                                                           | VI               |
| $\Gamma(G/E)$, `Γ̲(G/E)` (sections / sheaf of sections of a fibered category) <!-- TRANSLATOR NOTE: source `Γ (𝓞G/𝓞E) et Γ (𝓞G/𝓞E)`; the two are distinguished by an underline in the original which the OCR collapses. --> | VI               |
| `F_S` (fibre of a fibered category over $S$)                                                                                                                                                                               | VI               |
| $f^{\ast}_{F}(...)$ or $f^{\ast}(...)$ (inverse image along $f$)                                                                                                                                                           | VI               |
| $\Gamma_{f}(...)$                                                                                                                                                                                                          | VI               |
| $\operatorname{Hom}_{\bullet}(F, G)$ <!-- TRANSLATOR NOTE: source `Hom_ (𝓞F,𝓞G)`; subscript glyph not recovered from OCR. -->                                                                                              | VI               |
| $\hat{C}at_{/E}$ (a hatted variant — pseudo-functorial 2-category) <!-- TRANSLATOR NOTE: source `Cat^_/𝓞E`; the hat is restored on `Cat`. -->                                                                              | VI               |
| $F/E$ (fibered category $F$ over $E$)                                                                                                                                                                                      | VI               |
| $f^{F}_{\ast}$ or $~f_{\ast}$ (direct image; "tilde" variant)                                                                                                                                                              | VI               |

## Fundamental group (Exposé V) and étale-topology refinements (Exposé XIII)

| Notation                                                                                                                                                                                           | Where introduced |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| $\pi_{1}(S, a)$ (fundamental group at the geometric point $a$) <!-- TRANSLATOR NOTE: source `_1(S,a)`; the OCR systematically drops the `π` prefix on `π_1`. Restored here and below. -->          | V                |
| $\pi_{1}(S; a, a')$ (set of paths from $a$ to $a'$)                                                                                                                                                | V                |
| $\pi_{1}(f; a')$ (induced morphism on fundamental groups)                                                                                                                                          | V                |
| $C(S)$ (category of finite étale covers of $S$) <!-- TRANSLATOR NOTE: source `𝓞C(S)`; the script-O is artefactual. -->                                                                             | V                |
| `Sch` (category of schemes)                                                                                                                                                                        | V                |
| $\mu_{n, S}$ (group scheme of $n$-th roots of unity over $S$)                                                                                                                                      | XI               |
| $X^{an}$, $f^{an}$ (analytification)                                                                                                                                                               | XII              |
| `SF` or $S(F)$ (sheaf associated to a presheaf $F$)                                                                                                                                                | XII              |
| $H^{1}_{t}(U, F)$ (Čech $H^{1}$ for the topology $t$)                                                                                                                                              | XII              |
| $R^{1}_{t} g_{\ast} F$ (higher direct image for the topology $t$)                                                                                                                                  | XII              |
| $C_{t}((U, X)/S)$ or $C_{t}$ (category for the topology $t$)                                                                                                                                       | XII              |
| $\pi^{t}_{1}((U, X)/S, a)$, $\pi^{t}_{1}(U, a)$, $\pi^{t}_{1}(U)$ (fundamental group for $t$) <!-- TRANSLATOR NOTE: source `_1^t(...)`; `π` prefix restored. -->                                   | XIII             |
| $(g^{t}_{\ast} \Phi)_{T'}$                                                                                                                                                                         | XIII             |
| $H^{0}(V, C_{V})^{\Pi}$                                                                                                                                                                            | XIII             |
| $\pi^{\mathbf{L}}_{1}(U, a)$ (fundamental group with prime-to-$\mathbf{L}$ coefficients) <!-- TRANSLATOR NOTE: `𝐋` denotes a set of prime numbers; source `_1^𝐋 (U,a)`. -->                        | XIII             |
| $\pi_{1}'(X, a)$ (a derived / first variant of $\pi_{1}$) <!-- TRANSLATOR NOTE: source `_1'(X,a)`. -->                                                                                             | XIII             |
| $\pi^{\mathbf{L}}_{1}(X/S, g, \bar{s})$ or $\pi^{\mathbf{L}}_{1}(X/S, g)$ (fundamental group of a relative scheme) <!-- TRANSLATOR NOTE: source `_1^𝐋 (X/S,g,bar s)`; "bar s" rendered as `s̄`. --> | XIII             |
| $\pi^{\mathbf{L}}_{1}(X_{\bar{s}}, a)_{K}$ (fundamental group of a geometric fibre, base extension to $K$) <!-- TRANSLATOR NOTE: source `_1^𝐋 (X_bar s,a)_K`. -->                                  | XIII             |
| $\mathbf{Z}_{\ell}[1]$ (a Tate-twist–like degree shift)                                                                                                                                            | XIII             |
