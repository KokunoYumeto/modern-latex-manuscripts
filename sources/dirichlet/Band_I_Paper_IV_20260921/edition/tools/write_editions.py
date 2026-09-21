from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FR={}
FR[65]=r'''% Authority: exact-scope leaf 3; full PDF page 82; printed p.65 (folio not printed).
% U:p065.title | heading
\begin{center}
{\large RECHERCHES SUR LES DIVISEURS PREMIERS D'UNE CLASSE\\
DE FORMULES DU QUATRIÈME DEGRÉ.}\par
\vspace{5pt}\rule{18mm}{0.25pt}\par\vspace{5pt}
1\textsuperscript{er} Mémoire.
\end{center}
% U:p065.u01 | paragraph-start
On trouve, dans les annonces littéraires de Gottingue (11 avril 1825),
l'extrait d'un mémoire d'analyse indéterminée que M. \textsc{Gauss} a présenté à la
Société Royale des Sciences de cette ville, mais qui n'a pas encore été imprimé.
Ce mémoire est le premier d'une suite de mémoires que l'illustre auteur
des \emph{Disquisitiones arithmeticae} se propose de donner sur la théorie des résidus
biquadratiques, et a pour objet de déterminer les caractères distinctifs des
nombres premiers diviseurs de la formule $x^4-2$. L'auteur y établit deux théorèmes
extrêmement élégants qui peuvent servir à décider, si un nombre premier,
diviseur de $x^2-2$, divise ou ne divise pas la formule précédente. Ayant eu
connaissance, dans le courant de l'année qui vient de finir, de l'extrait cité
qui ne contient que les énoncés des deux théorèmes dont il vient d'être question,
et de quelques propositions auxiliaires, j'eus le désir de démontrer de mon côté
les beaux théorèmes découverts par M. \textsc{Gauss}. Les recherches que je fis dans
cette vue me firent trouver une démonstration fondée sur des considérations
extrêmement simples et probablement tout-à-fait différente de celle de M. \textsc{Gauss},
qui paraît exiger des recherches préliminaires très délicates et assez étendues.
J'appliquai ensuite des considérations analogues à d'autres questions et particulièrement
à la recherche des propriétés qui distinguent les diviseurs premiers
de la formule $\alpha x^4+\beta x^2+\gamma$; et je parvins ainsi à un grand nombre de théorèmes
intéressants. L'exposition rapide d'une partie des résultats auxquels ces
recherches m'ont conduit, est l'objet du présent mémoire. Je commence par
poser quelques définitions et par énoncer quelques théorèmes très faciles à
établir et sur lesquels nous aurons à nous appuyer dans la suite.
% U:p065.rule | terminal-rule
\par\vspace{7pt}\centerline{\rule{46mm}{0.25pt}}
'''
FR[66]=r'''% Authority: exact-scope leaf 4; full PDF page 83; printed p.66.
% U:p066.section | heading
\sectionnumber{1}
% U:p066.u01 | paragraph-start
„Si l'on peut attribuer à l'indéterminée $x$ une valeur telle que $x^4-A$
devienne divisible par $B$, $A$ sera dit résidu biquadratique par rapport à $B$.“
% U:p066.u02 | paragraph-start
\par
Il est facile de voir que, si un nombre $A$ est résidu biquadratique par
rapport à un nombre $B$, ou en d'autres termes, si $B$ est diviseur de $x^4-A$,
chaque facteur premier de $B$ sera pareillement diviseur de $x^4-A$, et réciproquement,
que si cette condition a lieu par rapport à tout facteur premier
du nombre $B$, $B$ sera lui-même diviseur de $x^4-A$. On peut donc se borner,
lorsqu'il s'agit d'assigner tous les nombres qui divisent la formule $x^4-A$, à ne
considérer que les nombres premiers.
% U:p066.u03 | paragraph-start
\par
Il n'est pas moins évident que, pour qu'un nombre divise la formule
$x^4-A$, il est nécessaire que ce nombre soit diviseur de $x^2-A$. Il n'y a donc
à examiner que les nombres premiers diviseurs de cette dernière formule,
c'est-à-dire les nombres premiers par rapport auxquels $A$ est résidu quadratique.
On peut ajouter que, relativement à ceux de ces derniers qui sont de la forme
$4n+3$, la question ne présente aucune difficulté; car on s'assure par un raisonnement
très simple que tout nombre premier $4n+3$, diviseur de $x^2-A$, divise
aussi la formule $x^4-A$.
% U:p066.u04 | paragraph-start
\par
Soit $p$ un nombre premier $4n+1$, diviseur de $x^2-A$, $A$ désignant
un nombre positif ou négatif, non-divisible par $p$; on a, comme l'on sait,
$A^{\frac{p-1}{2}}\equiv1\md{p}$. On conclut de là, $A^{\frac{p-1}{4}}\equiv\pm1\md{p}$ et l'on prouve facilement
que le signe supérieur ou inférieur aura lieu, selon que $p$ divise ou ne
divise pas la formule $x^4-A$. On peut donc énoncer ce théorème:
% U:p066.u05 | paragraph-start
\par
„$A$ désignant un nombre résidu quadratique par rapport au nombre
premier $p=4n+1$, on aura $A^{\frac{p-1}{4}}\equiv1$ ou $A^{\frac{p-1}{4}}\equiv-1\md{p}$. Dans le premier
cas, $A$ sera résidu biquadratique par rapport à $p$, dans le second, $A$ sera non-résidu
biquadratique par rapport à $p$.“
% U:p066.u06 | paragraph-start
\par
Si l'on applique ce théorème au cas où $A=-1$, on trouvera que $-1$
est résidu biquadratique par rapport aux nombres premiers $8n+1$, et au contraire
non-résidu relativement à ceux de la forme $8n+5$. Du théorème précédent
on déduit facilement cet autre, dans l'énoncé duquel on suppose, comme
dans tout ce qui suivra, que $p$ soit un nombre premier $4n+1$, et que $A$ et $A'$
désignent des nombres non-divisibles par $p$ et qui sont l'un et l'autre des résidus
quadratiques par rapport à $p$.
'''
FR[67]=r'''% Authority: exact-scope leaf 5; full PDF page 84; printed p.67.
% U:p067.u01 | paragraph-start
„Si les nombres $A$ et $A'$ sont tous les deux des résidus biquadratiques
ou tous les deux des non-résidus biquadratiques par rapport à $p$, le produit
$AA'$ sera résidu biquadratique par rapport à $p$; si, au contraire, l'un des nombres
$A$ et $A'$ est résidu, l'autre non-résidu biquadratique relativement à $p$, $AA'$ sera
non-résidu biquadratique par rapport à $p$.“
% U:p067.u02 | paragraph-start
\par
En faisant $A'=-1$, et en ayant égard à ce qui précède, on verra que,
si $p$ est de la forme $8n+1$, $A$ sera en même temps que $-A$ résidu ou
non-résidu biquadratique, et qu'au contraire, si $p$ est de la forme $8n+5$,
l'un des nombres $A$ et $-A$ sera résidu, l'autre non-résidu biquadratique par
rapport à $p$.
% U:p067.section | heading
\sectionnumber{2}
% U:p067.u03 | paragraph-start; continues through p.68 and p.69
Après avoir établi ces préliminaires, nous allons nous occuper de la recherche
des caractères qui distinguent les diviseurs premiers de la formule $x^4-2$.
On sait que les diviseurs premiers de $x^2-2$ sont de l'une de ces deux formes:
$8n+1$, $8n+7$, et que réciproquement tout nombre premier de l'une de ces
formes divise la formule $x^2-2$. D'après ce que nous avons dit dans le paragraphe
précédent, nous n'avons pas besoin d'avoir égard à la dernière de ces
deux formes, et il suffira de considérer les nombres premiers $8n+1$. Soit $p$
un nombre premier de cette espèce, et posons, comme il est permis de le faire,
$p=t^2+2u^2$, où $u$ sera pair, $t$ impair. Faisons $u=2^\nu kk'k''\ldots$, $2^\nu$ étant la
puissance la plus élevée de $2$ qui divise $u$, et $k$, $k'$, $k''$, $\ldots$ désignant des
nombres premiers impairs, dont plusieurs peuvent être égaux entre eux.
L'équation $t^2+2u^2=p$ donne immédiatement $t^2\equiv p\md{k}$. Le nombre $p$
est donc résidu quadratique par rapport à $k$, ce que nous écrirons ainsi:
$\leg{p}{k}=1$, en adoptant la notation employée par M. \textsc{Legendre}. On se rappelle
que, si $c$ désigne un nombre premier et $M$ un nombre quelconque, non divisible
par $c$, cet illustre géomètre se sert du signe $\leg{M}{c}$, pour désigner le reste
que l'on obtient, en divisant par $c$ la puissance $M^{\frac{c-1}{2}}$, reste que l'on sait être
égal à $1$ ou $-1$, selon que $M$ est ou n'est pas résidu quadratique par rapport
à $c$. En appliquant à la relation $\leg{p}{k}=1$, le théorème connu sous le nom
de loi de réciprocité (\emph{theorema fundamentale} de M. \textsc{Gauss}), on aura, $p$ étant
'''
FR[68]=r'''% Authority: exact-scope leaf 6; full PDF page 85; printed p.68.
% U:p068.u01 | continuation of p067.u03
\noindent
de la forme $4n+1$, $\leg{k}{p}=1$. On trouve de la même manière:
\[
\leg{k'}{p}=1,\quad \leg{k''}{p}=1,\quad\text{etc.}
\]
D'un autre côté, comme $p$ est de la forme $8n+1$, on a aussi $\leg{2}{p}=1$, et par
conséquent $\leg{2^\nu}{p}=1$. Multipliant cette dernière relation par toutes les précédentes,
il viendra:
\[
\leg{2^\nu kk'k''\ldots}{p}=\leg{u}{p}=1.
\]
% U:p068.u02 | continuation
Considérons maintenant les facteurs simples du nombre impair $t$, que nous partagerons
en deux classes. La première classe comprendra les diviseurs premiers
de l'une de ces deux formes: $8n+1$, $8n+7$, et les nombres qui en font partie
seront désignés par $g$, $g'$, $g''$, $\ldots$; la seconde classe se composera de nombres
$h$, $h'$, $h''$, $\ldots$, contenus dans ces deux formes: $8n+3$, $8n+5$. On a d'abord:
\[
t=gg'g''\ldots\times hh'h''\ldots,
\]
et l'on conclura ensuite de l'équation $p=t^2+2u^2$:
\[
\begin{aligned}
\leg{2p}{g}&=1, &\leg{2p}{g'}&=1, &\leg{2p}{g''}&=1, &\text{etc.}\\
\leg{2p}{h}&=1, &\leg{2p}{h'}&=1, &\leg{2p}{h''}&=1, &\text{etc.}
\end{aligned}
\]
% U:p068.u03 | continuation
D'un autre côté, on a en vertu de théorèmes connus:
\[
\begin{aligned}
\leg{2}{g}&=1, &\leg{2}{g'}&=1, &\leg{2}{g''}&=1, &\text{etc.}\\
\leg{2}{h}&=-1, &\leg{2}{h'}&=-1, &\leg{2}{h''}&=-1, &\text{etc.}
\end{aligned}
\]
% U:p068.u04 | continuation
Si l'on compare maintenant ces relations aux précédentes, on trouvera:
\[
\begin{aligned}
\leg{p}{g}&=1, &\leg{p}{g'}&=1, &\leg{p}{g''}&=1, &\text{etc.}\\
\leg{p}{h}&=-1, &\leg{p}{h'}&=-1, &\leg{p}{h''}&=-1, &\text{etc.}
\end{aligned}
\]
% U:p068.u05 | continuation
L'application de la loi de réciprocité à ces dernières relations donnera celles-ci:
\[
\begin{aligned}
\leg{g}{p}&=1, &\leg{g'}{p}&=1, &\leg{g''}{p}&=1, &\text{etc.}\\
\leg{h}{p}&=-1, &\leg{h'}{p}&=-1, &\leg{h''}{p}&=-1, &\text{etc.}
\end{aligned}
\]
'''
FR[69]=r'''% Authority: exact-scope leaf 7; full PDF page 86; printed p.69.
% U:p069.u01 | continuation of p067.u03
\noindent
d'où il suit, en multipliant:
\[
\leg{gg'g''\ldots\times hh'h''\ldots}{p}=\leg{t}{p}=\pm1,
\]
où il faudra prendre le signe supérieur ou inférieur, selon que les nombres $h$,
$h'$, $h''$, $\ldots$ sont en nombre pair ou impair. Or, il est facile de voir, par
l'équation $t=gg'g''\ldots\times hh'h''\ldots$, que le premier cas aura lieu, lorsque $t$ est de
l'une de ces formes: $8n+1$, $8n+7$, le second, lorsque $t$ est contenu dans l'une
de celles-ci: $8n+3$, $8n+5$. On a donc:
\[
\begin{aligned}
\leg{t}{p}&=1, &&\text{lorsque }t=8n+1\quad\text{ou}\quad8n+7,\\
\leg{t}{p}&=-1, &&\text{lorsque }t=8n+3\quad\text{ou}\quad8n+5.
\end{aligned}
\]
% U:p069.u02 | continuation
Reprenons l'équation $t^2+2u^2=p$ et mettons-la sous la forme d'une congruence:
\[
t^2\equiv-2u^2\md{p}.
\]
En élevant les deux membres à la puissance $\dfrac{p-1}{4}$, on aura $\left(\dfrac{p-1}{4}\text{ étant pair}\right)$:
\[
t^{\frac{p-1}{2}}\equiv2^{\frac{p-1}{4}}u^{\frac{p-1}{2}}\md{p},
\]
ou, ce qui revient au même, ayant prouvé que $\leg{u}{p}=1$:
\[
t^{\frac{p-1}{2}}\equiv2^{\frac{p-1}{4}}\md{p}.
\]
On voit donc que $\pm2$ (on peut mettre le double signe attendu que $p=8n+1$)
est ou n'est pas résidu biquadratique par rapport à $p$, selon que l'on a $\leg{t}{p}=1$
ou $\leg{t}{p}=-1$. En comparant ce résultat à ce qui précède, on aura ce théorème:
% U:p069.u03 | paragraph-start
\par
„$p$ désignant un nombre premier $8n+1$, si l'on fait $p=t^2+2u^2$, je dis
que $\pm2$ sera ou ne sera pas résidu biquadratique par rapport à $p$, selon que
$t$ est de l'une de ces formes: $8n+1$, $8n+7$ ou de l'une de celles-ci: $8n+3$,
$8n+5$.“
% U:p069.u04 | paragraph-start
\par
C'est le premier des deux théorèmes de M. \textsc{Gauss}, dont il a été question
dans le préambule de ce mémoire. Le second de ces théorèmes est relatif à
la décomposition du nombre $p$ en deux carrés, et peut être facilement déduit
de celui qui vient d'être établi.
% U:p069.u05 | paragraph-start
\par
Faisons $p=\varphi^2+\psi^2$ (où $\psi$ est supposé divisible par $4$) et égalons cette
valeur de $p$ à celle que nous venons de considérer.
'''
FR[70]=r'''% Authority: exact-scope leaf 8; full PDF page 87; printed p.70.
% U:p070.u01 | paragraph-start
Nous aurons ainsi:
\[
p=t^2+2u^2=\varphi^2+\psi^2,
\]
et en transposant:
\[
t^2-\psi^2=(t+\psi)(t-\psi)=\varphi^2-2u^2.
\]
% U:p070.u02 | paragraph-start
\par
Comme $\varphi$ est impair, le plus grand diviseur commun de $\varphi$ et $u$ sera
impair; désignons-le par $m$ et faisons $\varphi=m\varphi'$, $u=mu'$. La substitution de
ces valeurs dans l'équation précédente la changera en celle-ci:
\[
(t+\psi)(t-\psi)=m^2(\varphi'^2-2u'^2).
\]
% U:p070.u03 | continuation
On voit que le nombre impair $t+\psi$ est composé de deux facteurs $E$ et $K$,
dont le premier divise $m^2$, le second $\varphi'^2-2u'^2$, et qu'il en est de même de
$t-\psi$ dont nous désignerons les facteurs par $F$ et $L$, $L$ pouvant être négatif.
Nous avons donc les équations:
\[
\begin{aligned}
t+\psi&=EK, &t-\psi&=FL,\\
m^2&=EF, &\varphi'^2-2u'^2&=KL.
\end{aligned}
\]
% U:p070.u04 | continuation
Il est facile de s'assurer que les nombres $E$ et $F$ sont premiers entre eux. En
effet, soit $\delta$ un diviseur premier de $E$, et supposons que $\delta$ divise en même
temps $F$. Le nombre $\delta$ serait diviseur commun de $t+\psi$ et $t-\psi$, et diviserait
par conséquent le nombre $t$, qui est la demi-somme des précédents. D'un autre
côté, de ce que $\delta$ est diviseur premier de $E$, il suit successivement, en ayant
égard aux équations $EF=m^2$, $u=mu'$, que $m^2$, $m$ et $u$ sont multiples de $\delta$.
Les nombres $t$ et $u$ auraient donc le diviseur commun $\delta$, et $p=t^2+2u^2$ ne
serait pas un nombre premier.
% U:p070.u05 | paragraph-start
\par
Le produit des nombres $E$ et $F$, qui sont premiers entre eux, étant un
carré, chacun d'eux est aussi un carré. Faisons $E=e^2$, et nous aurons
$t+\psi=e^2K$. Le carré impair $e^2$ est de la forme $8n+1$, et $K$, comme diviseur
impair de $\varphi'^2+2u'^2$ (où $\varphi'$ et $u'$ sont premiers entre eux), de l'une de celles-ci:
$8n+1$, $8n+7$. Le nombre $t+\psi$ sera donc lui-même de l'une des formes
$8n+1$, $8n+7$. Le nombre $\psi$ que nous savons être divisible par $4$, sera de
la forme $8n$ ou de celle-ci: $8n+4$. Il suit, de ce qui précède, que, dans le
premier cas, $t$ sera de l'une de ces deux formes: $8n+1$, $8n+7$, dans le second
de l'une de celles-ci: $8n+3$, $8n+5$. En comparant ce résultat au théorème
précédent, on aura cet autre théorème:
% U:p070.u06 | paragraph-start
\par
„$p$ désignant un nombre premier $8n+1$, et ayant fait $p=\varphi^2+\psi^2$ (où
$\psi$ est supposé divisible par $4$), $\pm2$ sera ou ne sera pas résidu biquadratique
par rapport à $p$, selon que $\psi$ est de la forme $8n$ ou de celle-ci: $8n+4$.“
'''
FR[71]=r'''% Authority: exact-scope leaf 9; full PDF page 88; printed p.71.
% U:p071.u01 | paragraph-start
Il y a un troisième théorème propre à décider si $\pm2$ est ou n'est pas
résidu biquadratique relativement à un nombre premier $p=8n+1$, et qui peut
s'énoncer comme il suit:
% U:p071.u02 | paragraph-start
\par
„Ayant fait d'une manière quelconque $p=t^2-2u^2$, $\pm2$ sera ou ne sera
pas résidu biquadratique par rapport à $p$, selon que $t$ est de l'une des formes
$8n+1$, $8n+3$, ou de l'une de celles-ci: $8n+5$, $8n+7$.“
% U:p071.u03 | paragraph-start
\par
Nous ne nous arrêterons pas à démontrer ce théorème que l'on peut
établir d'une manière directe et par des considérations analogues à celles sur
lesquelles est fondée la démonstration du premier des deux théorèmes précédents.
On peut aussi le déduire de chacun des précédents à-peu-près comme on vient
de passer du premier au second.
% U:p071.section | heading
\sectionnumber{3}
% U:p071.u04 | paragraph-start; note anchor after impair
Nous allons maintenant passer à des considérations plus générales. Soit
$b$ un nombre premier $4n+3$, $p$ un nombre premier $4n+1$ susceptible d'être
mis sous la forme $t^2-bu^2$, et proposons-nous de décider si $-b$ est ou n'est
pas résidu biquadratique par rapport à $p$. Il est facile de voir que, si $p$ peut
être mis sous la forme $t^2-bu^2$, on peut toujours le faire de manière que $u$
soit pair, et par conséquent $t$ impair\sourcefootnote{%
Pour prouver que cela est toujours possible, nous allons faire voir que, si l'on a $t^2-bu^2=p$,
$t$ étant pair, il est facile de déduire des valeurs de $t$ et de $u$, d'autres nombres $t'$ (impair) et $u'$ qui satisfassent
également à l'équation $t'^2-bu'^2=p$. Soient $r$ et $s$ les moindres nombres tels que $r^2-bs^2=1$, je dis
que $r$ sera pair. En effet, on sait que, si $b$ désigne un nombre premier $4n+3$, l'équation $\rho^2-b\sigma^2=\pm2$ est
toujours possible, et que, $\rho$ et $\sigma$ étant supposés les plus petits nombres qui y satisfassent, on a $r=b\sigma^2\pm1$,
$s=\rho\sigma$ (\emph{Théorie des Nombres}, no.\,44.\,45). Il suit de là et de ce que les nombres $\rho$ et $\sigma$ sont évidemment
impairs l'un et l'autre, que $r$ est un nombre pair. Cela posé, si l'on multiplie entre elles les équations
$r^2-bs^2=1$, $t^2-bu^2=p$, il viendra $(rt\pm bsu)^2-b(ru\pm st)^2=p$, et l'on verra facilement que $rt\pm bsu$
est un nombre impair.}.
Faisons donc $p=t^2-bu^2$, et posons
$u=2^\nu kk'k''\ldots$, $k$, $k'$, $k''$, $\ldots$ étant les facteurs impairs simples de $u$. On
conclut immédiatement de l'équation précédente:
\[
\leg{p}{k}=1,\quad \leg{p}{k'}=1,\quad \leg{p}{k''}=1,\quad\text{etc.}
\]
% U:p071.u05 | continuation
L'application de la loi de réciprocité donne ensuite, $p$ étant de la forme $4n+1$:
\[
\leg{k}{p}=1,\quad \leg{k'}{p}=1,\quad \leg{k''}{p}=1,\quad\text{etc.}
\]
% U:p071.u06 | continuation to p.72
Multipliant ces relations entre elles et avec la relation identique $\leg{2^\nu}{p}=\leg{2^\nu}{p}$,
'''
FR[72]=r'''% Authority: exact-scope leaf 10; full PDF page 89; printed p.72.
% U:p072.u01 | continuation of p071.u06
\noindent
on aura ce résultat:
\begin{equation*}
\leg{u}{p}=\leg{2^\nu}{p}.\tag{$\alpha$}
\end{equation*}
% U:p072.u02 | continuation
Décomposons actuellement le nombre impair $t$ en ses facteurs simples et partageons
ces facteurs en deux classes. Ceux de la première classe seront désignés
par $g$, $g'$, $g''$, $\ldots$, et sont tels que:
\begin{equation*}
\leg{-b}{g}=1,\quad\leg{-b}{g'}=1,\quad\leg{-b}{g''}=1,\quad\text{etc.}\tag{$\beta$}
\end{equation*}
% U:p072.u03 | continuation
Quant à ceux qui forment la seconde classe et que nous désignerons par $h$,
$h'$, $h''$, $\ldots$, ils sont tels que:
\begin{equation*}
\leg{-b}{h}=-1,\quad\leg{-b}{h'}=-1,\quad\leg{-b}{h''}=-1,\quad\text{etc.}\tag{$\beta'$}
\end{equation*}
% U:p072.u04 | continuation
Le produit de tous ces nombres est égal à $t$, c'est-à-dire que:
\[
t=gg'g''\ldots\times hh'h''\ldots.
\]
L'inspection de l'équation $t^2-bu^2=p$ donne ces résultats:
\[
\begin{aligned}
\leg{-bp}{g}&=1, &\leg{-bp}{g'}&=1, &\leg{-bp}{g''}&=1, &\text{etc.}\\
\leg{-bp}{h}&=1, &\leg{-bp}{h'}&=1, &\leg{-bp}{h''}&=1, &\text{etc.}
\end{aligned}
\]
% U:p072.u05 | continuation
La comparaison de ces relations avec les précédentes donnera ensuite:
\[
\begin{aligned}
\leg{p}{g}&=1, &\leg{p}{g'}&=1, &\leg{p}{g''}&=1, &\text{etc.}\\
\leg{p}{h}&=-1, &\leg{p}{h'}&=-1, &\leg{p}{h''}&=-1, &\text{etc.}
\end{aligned}
\]
% U:p072.u06 | continuation
Appliquant maintenant la loi de réciprocité, il viendra:
\[
\begin{aligned}
\leg{g}{p}&=1, &\leg{g'}{p}&=1, &\leg{g''}{p}&=1, &\text{etc.}\\
\leg{h}{p}&=-1, &\leg{h'}{p}&=-1, &\leg{h''}{p}&=-1, &\text{etc.}
\end{aligned}
\]
% U:p072.u07 | continuation to p.73
Multipliant ces relations entre elles, on aura:
\[
\leg{gg'g''\ldots\times hh'h''\ldots}{p}=\leg{t}{p}=\pm1,
\]
le signe supérieur ou inférieur ayant lieu, selon que les nombres $h$, $h'$, $h''$, $\ldots$
sont en nombre pair ou impair. D'un autre côté, si l'on applique la loi de
réciprocité aux relations $(\beta)$ et $(\beta')$, il viendra, $b$ étant de la forme $4n+3$:
'''
FR[73]=r'''% Authority: exact-scope leaf 11; full PDF page 90; printed p.73.
% U:p073.u01 | continuation of p072.u07
\[
\begin{aligned}
\leg{g}{b}&=1, &\leg{g'}{b}&=1, &\leg{g''}{b}&=1, &\text{etc.}\\
\leg{h}{b}&=-1, &\leg{h'}{b}&=-1, &\leg{h''}{b}&=-1, &\text{etc.}
\end{aligned}
\]
égalités qui, étant multipliées entre elles, donneront celle-ci:
\[
\leg{gg'g''\ldots\times hh'h''\ldots}{b}=\leg{t}{b}=\pm1,
\]
où il faut prendre le signe supérieur ou inférieur, selon que les nombres $h$,
$h'$, $h''$, $\ldots$ sont en nombre pair ou impair.
% U:p073.u02 | paragraph-start
\par
La comparaison de ce résultat avec celui que nous avons obtenu, il n'y
a qu'un instant, fait voir qu'on a toujours:
\begin{equation*}
\leg{t}{p}=\leg{t}{b}.\tag{$\gamma$}
\end{equation*}
% U:p073.u03 | continuation
Reprenons maintenant l'équation $p=t^2-bu^2$, et mettons-la sous la forme d'une
congruence:
\[
t^2\equiv bu^2\md{p}.
\]
On tire de là, en élevant les deux membres à la puissance $\dfrac{p-1}{4}$:
\[
t^{\frac{p-1}{2}}\equiv b^{\frac{p-1}{4}}u^{\frac{p-1}{2}}\md{p}.
\]
% U:p073.u04 | continuation
La formule $(\alpha)$, qui est celle-ci: $\leg{u}{p}=\leg{2^\nu}{p}$, $2^\nu$ désignant la puissance la plus
élevée qui divise $u$, peut être présentée d'une autre manière. Il faut pour cela
distinguer deux cas, selon que $p$ est de la forme $8n+1$ ou de celle-ci: $8n+5$.
Si $p$ est un nombre premier $8n+1$, on a, comme on sait, $\leg{2}{p}=1$, et par
conséquent $\leg{2^\nu}{p}=1$; la formule dont il s'agit se change donc dans ce cas en
celle-ci: $\leg{u}{p}=1$. Si $p$ est un nombre premier $8n+5$, le nombre $\nu$ est $=1$;
car si $\nu$ était plus grand que l'unité, $u^2$ serait divisible par $8$, et $p=t^2-bu^2$
serait de la forme $8n+1$. Comme d'ailleurs dans ce cas $\leg{2}{p}=-1$, la formule
$(\alpha)$ se changera en celle-ci: $\leg{u}{p}=-1$. Les deux cas que nous venons
d'examiner sont compris dans la formule $\leg{u}{p}=(-1)^{\frac{p-1}{4}}$, qui équivaut à cette
congruence: $u^{\frac{p-1}{2}}\equiv(-1)^{\frac{p-1}{4}}\md{p}$. En substituant la valeur qu'elle donne
'''
FR[74]=r'''% Authority: exact-scope leaf 12; full PDF page 91; printed p.74.
% U:p074.u01 | continuation of p073.u04
\noindent
pour $u^{\frac{p-1}{2}}$ dans la congruence obtenue plus haut, on aura:
\[
t^{\frac{p-1}{2}}\equiv(-b)^{\frac{p-1}{4}}\md{p},
\]
résultat qui montre que $-b$ sera ou ne sera pas résidu biquadratique par
rapport à $p$, selon que $t$ est ou n'est pas résidu quadratique par rapport à $p$.
Si l'on compare maintenant ce résultat avec celui qui est contenu dans la formule
$(\gamma)$, on arrivera au théorème que nous allons énoncer:
% U:p074.u02 | paragraph-start
\par
„Désignons par $b$ un nombre premier $4n+3$, et par $p$ un nombre
premier $4n+1$, susceptible d'être mis sous la forme $t^2-bu^2$. Ayant fait
$p=t^2-bu^2$ (où $t$ est supposé impair), je dis que $-b$ sera ou ne sera pas
résidu biquadratique par rapport à $p$, selon que $t$ est ou n'est pas résidu quadratique
par rapport à $b$.“
% U:p074.section | heading
\sectionnumber{4}
% U:p074.u03 | paragraph-start
Nous allons maintenant déduire de ce théorème un autre, au moyen
duquel on peut décider plus promptement encore, si $-b$ est ou n'est pas résidu
biquadratique par rapport à $p$. Conservons les notations précédentes et
faisons $p=\varphi^2+\psi^2$ (où $\psi$ est supposé pair). En égalant cette valeur de $p$
à celle que nous avons considérée précédemment, on aura:
\[
p=t^2-bu^2=\varphi^2+\psi^2,
\]
et en transposant:
\[
t^2-\psi^2=(t+\psi)(t-\psi)=\varphi^2+bu^2.
\]
% U:p074.u04 | continuation
Il y a maintenant deux cas à distinguer, selon que $\varphi$ est ou n'est pas divisible
par $b$. Nous commençons par l'examen du dernier de ces deux cas. Soit
$m$ le plus grand commun diviseur de $\varphi$ et $u$ qui sera impair ($\varphi$ étant impair)
et non-divisible par $b$, et posons $\varphi=m\varphi'$, $u=mu'$. La substitution de ces
valeurs dans la dernière équation, la changera en celle-ci:
\[
(t+\psi)(t-\psi)=m^2(\varphi'^2+bu'^2).
\]
% U:p074.u05 | continuation; section 4 continues on p.75, not produced in S01
Il est évident, par cette équation, que $t+\psi$ est composé de deux facteurs $E$
et $K$ dont le premier divise $m^2$, le second $\varphi'^2+bu'^2$, et qu'il en est de même
de $t-\psi$. Désignant les facteurs de ce dernier nombre par $F$ et $L$, nous
aurons ces équations:
\[
\begin{aligned}
t+\psi&=EK, &t-\psi&=FL,\\
m^2&=EF, &\varphi'^2+bu'^2&=KL.
\end{aligned}
\]
'''
EN={}
EN[65]=r'''% Authority: exact-scope leaf 3; full PDF page 82; printed p.65.
% U:p065.title | heading
\begin{center}
{\large RESEARCHES ON THE PRIME DIVISORS OF A CLASS\\
OF FORMULAE OF THE FOURTH DEGREE.}\par
\vspace{5pt}\rule{18mm}{0.25pt}\par\vspace{5pt}
1\textsuperscript{st} Memoir.
\end{center}
% U:p065.u01 | paragraph-start
In the literary announcements of Göttingen (11 April 1825) one finds the extract
of a memoir of indeterminate analysis which Mr. \textsc{Gauss} presented to the
Royal Society of Sciences of that city, but which has not yet been printed.
This memoir is the first of a series of memoirs which the illustrious author
of the \emph{Disquisitiones arithmeticae} proposes to give on the theory of biquadratic
residues, and its object is to determine the distinctive characters of the prime
divisors of the formula $x^4-2$. The author establishes in it two extremely elegant
theorems which can serve to decide whether a prime number, divisor of $x^2-2$,
divides or does not divide the preceding formula. Having learned, in the course
of the year just ended, of the cited extract, which contains only the statements
of the two theorems just mentioned and of some auxiliary propositions, I wished
to demonstrate on my side the beautiful theorems discovered by Mr. \textsc{Gauss}.
The researches which I made with this aim led me to find a proof founded on
extremely simple considerations and probably entirely different from that of
Mr. \textsc{Gauss}, which appears to require very delicate and rather extensive
preliminary researches. I then applied analogous considerations to other questions
and particularly to the search for the properties which distinguish the prime
divisors of the formula $\alpha x^4+\beta x^2+\gamma$; and I thus arrived at a large number
of interesting theorems. The rapid exposition of part of the results to which
these researches have led me is the object of the present memoir. I begin by
setting down some definitions and by stating some theorems very easy to establish
and on which we shall have to rely in what follows.
% U:p065.rule | terminal-rule
\par\vspace{7pt}\centerline{\rule{46mm}{0.25pt}}
'''
EN[66]=r'''% Authority: exact-scope leaf 4; full PDF page 83; printed p.66.
% U:p066.section | heading
\sectionnumber{1}
% U:p066.u01 | paragraph-start
“If one can assign to the indeterminate $x$ a value such that $x^4-A$ becomes
divisible by $B$, $A$ will be called a biquadratic residue with respect to $B$.”
% U:p066.u02 | paragraph-start
\par
It is easy to see that, if a number $A$ is a biquadratic residue with respect to
a number $B$, or in other words, if $B$ is a divisor of $x^4-A$, each prime factor
of $B$ will likewise be a divisor of $x^4-A$, and reciprocally, that if this condition
holds with respect to every prime factor of the number $B$, $B$ will itself be
a divisor of $x^4-A$. Thus, when it is a question of assigning all the numbers
which divide the formula $x^4-A$, one can confine oneself to considering prime numbers.
% U:p066.u03 | paragraph-start
\par
It is no less evident that, for a number to divide the formula $x^4-A$, it is
necessary that this number be a divisor of $x^2-A$. There are therefore only
the prime divisors of this latter formula to examine, that is to say, the prime
numbers with respect to which $A$ is a quadratic residue. One may add that,
relative to those among these latter which are of the form $4n+3$, the question
presents no difficulty; for one verifies by a very simple reasoning that every
prime number $4n+3$, divisor of $x^2-A$, also divides the formula $x^4-A$.
% U:p066.u04 | paragraph-start
\par
Let $p$ be a prime number $4n+1$, divisor of $x^2-A$, $A$ designating a positive
or negative number not divisible by $p$; one has, as is known,
$A^{\frac{p-1}{2}}\equiv1\md{p}$. From this one concludes
$A^{\frac{p-1}{4}}\equiv\pm1\md{p}$ and one proves easily that the upper or lower
sign will hold according as $p$ divides or does not divide the formula $x^4-A$.
Thus one may state this theorem:
% U:p066.u05 | paragraph-start
\par
“$A$ designating a number which is a quadratic residue with respect to the
prime number $p=4n+1$, one will have $A^{\frac{p-1}{4}}\equiv1$ or
$A^{\frac{p-1}{4}}\equiv-1\md{p}$. In the first case, $A$ will be a biquadratic
residue with respect to $p$, in the second, $A$ will be a biquadratic non-residue
with respect to $p$.”
% U:p066.u06 | paragraph-start
\par
If this theorem is applied to the case where $A=-1$, one will find that $-1$
is a biquadratic residue with respect to the prime numbers $8n+1$, and on the
contrary a non-residue relative to those of the form $8n+5$. From the preceding
theorem one easily deduces the following other theorem, in whose statement one
supposes, as in all that follows, that $p$ is a prime number $4n+1$, and that
$A$ and $A'$ designate numbers not divisible by $p$ and which are both quadratic
residues with respect to $p$.
'''
EN[67]=r'''% Authority: exact-scope leaf 5; full PDF page 84; printed p.67.
% U:p067.u01 | paragraph-start
“If the numbers $A$ and $A'$ are both biquadratic residues or both biquadratic
non-residues with respect to $p$, the product $AA'$ will be a biquadratic residue
with respect to $p$; if, on the contrary, one of the numbers $A$ and $A'$ is a
residue and the other a biquadratic non-residue relative to $p$, $AA'$ will be a
biquadratic non-residue with respect to $p$.”
% U:p067.u02 | paragraph-start
\par
Taking $A'=-1$, and having regard to what precedes, one will see that, if $p$
is of the form $8n+1$, $A$ will at the same time as $-A$ be a biquadratic residue
or non-residue, and that, on the contrary, if $p$ is of the form $8n+5$, one of
the numbers $A$ and $-A$ will be a residue and the other a biquadratic non-residue
with respect to $p$.
% U:p067.section | heading
\sectionnumber{2}
% U:p067.u03 | paragraph-start; continues through p.68 and p.69
After establishing these preliminaries, we shall deal with the search for the
characters which distinguish the prime divisors of the formula $x^4-2$. It is
known that the prime divisors of $x^2-2$ are of one of these two forms:
$8n+1$, $8n+7$, and that reciprocally every prime number of one of these forms
divides the formula $x^2-2$. According to what we said in the preceding paragraph,
we need not take account of the latter of these two forms, and it will suffice
to consider the prime numbers $8n+1$. Let $p$ be a prime number of this kind,
and put, as one is permitted to do, $p=t^2+2u^2$, where $u$ will be even and
$t$ odd. Let $u=2^\nu kk'k''\ldots$, $2^\nu$ being the highest power of $2$ which
divides $u$, and $k$, $k'$, $k''$, $\ldots$ designating odd prime numbers, several
of which may be equal to one another. The equation $t^2+2u^2=p$ immediately
gives $t^2\equiv p\md{k}$. The number $p$ is therefore a quadratic residue
with respect to $k$, which we shall write thus: $\leg{p}{k}=1$, adopting the
notation used by Mr. \textsc{Legendre}. Recall that, if $c$ designates a prime
number and $M$ any number not divisible by $c$, this illustrious geometer uses
the sign $\leg{M}{c}$ to designate the remainder which one obtains by dividing
by $c$ the power $M^{\frac{c-1}{2}}$, a remainder which is known to be equal to
$1$ or $-1$, according as $M$ is or is not a quadratic residue with respect to $c$.
Applying to the relation $\leg{p}{k}=1$ the theorem known under the name law
of reciprocity (the \emph{theorema fundamentale} of Mr. \textsc{Gauss}), one will have, $p$ being
'''
EN[68]=r'''% Authority: exact-scope leaf 6; full PDF page 85; printed p.68.
% U:p068.u01 | continuation of p067.u03
\noindent
of the form $4n+1$, $\leg{k}{p}=1$. One finds in the same way:
\[
\leg{k'}{p}=1,\quad \leg{k''}{p}=1,\quad\text{etc.}
\]
On the other hand, since $p$ is of the form $8n+1$, one also has $\leg{2}{p}=1$,
and consequently $\leg{2^\nu}{p}=1$. Multiplying this last relation by all the
preceding ones, one obtains:
\[
\leg{2^\nu kk'k''\ldots}{p}=\leg{u}{p}=1.
\]
% U:p068.u02 | continuation
Now consider the simple factors of the odd number $t$, which we shall divide
into two classes. The first class will comprise the prime divisors of one of
these two forms: $8n+1$, $8n+7$, and the numbers belonging to it will be designated
by $g$, $g'$, $g''$, $\ldots$; the second class will be composed of numbers
$h$, $h'$, $h''$, $\ldots$, contained in these two forms: $8n+3$, $8n+5$.
One first has:
\[
t=gg'g''\ldots\times hh'h''\ldots,
\]
and one will then conclude from the equation $p=t^2+2u^2$:
\[
\begin{aligned}
\leg{2p}{g}&=1, &\leg{2p}{g'}&=1, &\leg{2p}{g''}&=1, &\text{etc.}\\
\leg{2p}{h}&=1, &\leg{2p}{h'}&=1, &\leg{2p}{h''}&=1, &\text{etc.}
\end{aligned}
\]
% U:p068.u03 | continuation
On the other hand, by known theorems one has:
\[
\begin{aligned}
\leg{2}{g}&=1, &\leg{2}{g'}&=1, &\leg{2}{g''}&=1, &\text{etc.}\\
\leg{2}{h}&=-1, &\leg{2}{h'}&=-1, &\leg{2}{h''}&=-1, &\text{etc.}
\end{aligned}
\]
% U:p068.u04 | continuation
Comparing these relations with the preceding ones, one finds:
\[
\begin{aligned}
\leg{p}{g}&=1, &\leg{p}{g'}&=1, &\leg{p}{g''}&=1, &\text{etc.}\\
\leg{p}{h}&=-1, &\leg{p}{h'}&=-1, &\leg{p}{h''}&=-1, &\text{etc.}
\end{aligned}
\]
% U:p068.u05 | continuation
The application of the law of reciprocity to these last relations gives:
\[
\begin{aligned}
\leg{g}{p}&=1, &\leg{g'}{p}&=1, &\leg{g''}{p}&=1, &\text{etc.}\\
\leg{h}{p}&=-1, &\leg{h'}{p}&=-1, &\leg{h''}{p}&=-1, &\text{etc.}
\end{aligned}
\]
'''
EN[69]=r'''% Authority: exact-scope leaf 7; full PDF page 86; printed p.69.
% U:p069.u01 | continuation of p067.u03
\noindent
hence, on multiplying:
\[
\leg{gg'g''\ldots\times hh'h''\ldots}{p}=\leg{t}{p}=\pm1,
\]
where the upper or lower sign must be taken according as the numbers $h$,
$h'$, $h''$, $\ldots$ are even or odd in number. But it is easy to see, from the
equation $t=gg'g''\ldots\times hh'h''\ldots$, that the first case will occur when
$t$ is of one of these forms: $8n+1$, $8n+7$, and the second when $t$ is contained
in one of these: $8n+3$, $8n+5$. Thus one has:
\[
\begin{aligned}
\leg{t}{p}&=1, &&\text{when }t=8n+1\quad\text{or}\quad8n+7,\\
\leg{t}{p}&=-1, &&\text{when }t=8n+3\quad\text{or}\quad8n+5.
\end{aligned}
\]
% U:p069.u02 | continuation
Return to the equation $t^2+2u^2=p$ and put it in the form of a congruence:
\[
t^2\equiv-2u^2\md{p}.
\]
Raising both sides to the power $\dfrac{p-1}{4}$, one will have $\left(\dfrac{p-1}{4}\text{ being even}\right)$:
\[
t^{\frac{p-1}{2}}\equiv2^{\frac{p-1}{4}}u^{\frac{p-1}{2}}\md{p},
\]
or, what comes to the same thing, having proved that $\leg{u}{p}=1$:
\[
t^{\frac{p-1}{2}}\equiv2^{\frac{p-1}{4}}\md{p}.
\]
Thus one sees that $\pm2$ (the double sign may be put, since $p=8n+1$) is or is
not a biquadratic residue with respect to $p$ according as one has
$\leg{t}{p}=1$ or $\leg{t}{p}=-1$. Comparing this result with what precedes,
one has the theorem:
% U:p069.u03 | paragraph-start
\par
“$p$ designating a prime number $8n+1$, if one writes $p=t^2+2u^2$, I say that
$\pm2$ will or will not be a biquadratic residue with respect to $p$ according as
$t$ is of one of these forms: $8n+1$, $8n+7$ or of one of these: $8n+3$, $8n+5$.”
% U:p069.u04 | paragraph-start
\par
This is the first of the two theorems of Mr. \textsc{Gauss} mentioned in the
preamble of this memoir. The second of these theorems is relative to the
decomposition of the number $p$ into two squares, and can easily be deduced
from the one just established.
% U:p069.u05 | paragraph-start
\par
Let $p=\varphi^2+\psi^2$ (where $\psi$ is supposed divisible by $4$) and equate this
value of $p$ with the one we have just considered.
'''
EN[70]=r'''% Authority: exact-scope leaf 8; full PDF page 87; printed p.70.
% U:p070.u01 | paragraph-start
We shall thus have:
\[
p=t^2+2u^2=\varphi^2+\psi^2,
\]
and, after transposing:
\[
t^2-\psi^2=(t+\psi)(t-\psi)=\varphi^2-2u^2.
\]
% U:p070.u02 | paragraph-start
\par
Since $\varphi$ is odd, the greatest common divisor of $\varphi$ and $u$ will be odd;
designate it by $m$ and put $\varphi=m\varphi'$, $u=mu'$. Substitution of these
values in the preceding equation changes it into:
\[
(t+\psi)(t-\psi)=m^2(\varphi'^2-2u'^2).
\]
% U:p070.u03 | continuation
The odd number $t+\psi$ is thus composed of two factors $E$ and $K$, the first
of which divides $m^2$, the second $\varphi'^2-2u'^2$; and the same is true of
$t-\psi$, whose factors we denote by $F$ and $L$, $L$ being allowed to be negative.
We therefore have the equations:
\[
\begin{aligned}
t+\psi&=EK, &t-\psi&=FL,\\
m^2&=EF, &\varphi'^2-2u'^2&=KL.
\end{aligned}
\]
% U:p070.u04 | continuation
It is easy to verify that the numbers $E$ and $F$ are relatively prime. Indeed,
let $\delta$ be a prime divisor of $E$, and suppose that $\delta$ also divides $F$.
The number $\delta$ would be a common divisor of $t+\psi$ and $t-\psi$, and consequently
would divide the number $t$, which is the half-sum of the preceding two numbers.
On the other hand, from the fact that $\delta$ is a prime divisor of $E$, it follows
successively, having regard to the equations $EF=m^2$, $u=mu'$, that $m^2$, $m$,
and $u$ are multiples of $\delta$. The numbers $t$ and $u$ would therefore have the
common divisor $\delta$, and $p=t^2+2u^2$ would not be a prime number.
% U:p070.u05 | paragraph-start
\par
The product of the numbers $E$ and $F$, which are relatively prime, being a
square, each of them is also a square. Let $E=e^2$; then $t+\psi=e^2K$. The odd
square $e^2$ is of the form $8n+1$, and $K$, as an odd divisor of
$\varphi'^2+2u'^2$ (where $\varphi'$ and $u'$ are relatively prime), is of one of
these forms: $8n+1$, $8n+7$. Thus the number $t+\psi$ will itself be of one of
the forms $8n+1$, $8n+7$. The number $\psi$, which we know to be divisible by $4$,
will be of the form $8n$ or of the form $8n+4$. It follows from the preceding
that, in the first case, $t$ will be of one of these two forms: $8n+1$, $8n+7$,
and in the second of one of these: $8n+3$, $8n+5$. Comparing this result with
the preceding theorem, one has this other theorem:
% U:p070.u06 | paragraph-start
\par
“$p$ designating a prime number $8n+1$, and having written $p=\varphi^2+\psi^2$
(where $\psi$ is supposed divisible by $4$), $\pm2$ will or will not be a biquadratic
residue with respect to $p$ according as $\psi$ is of the form $8n$ or of the form $8n+4$.”
'''
EN[71]=r'''% Authority: exact-scope leaf 9; full PDF page 88; printed p.71.
% U:p071.u01 | paragraph-start
There is a third theorem suitable for deciding whether $\pm2$ is or is not a
biquadratic residue relative to a prime number $p=8n+1$, which may be stated
as follows:
% U:p071.u02 | paragraph-start
\par
“Having made, in any manner, $p=t^2-2u^2$, $\pm2$ will or will not be a biquadratic
residue with respect to $p$ according as $t$ is of one of the forms $8n+1$, $8n+3$,
or of one of these: $8n+5$, $8n+7$.”
% U:p071.u03 | paragraph-start
\par
We shall not stop to prove this theorem, which can be established directly
and by considerations analogous to those on which the proof of the first of
the two preceding theorems is founded. One can also deduce it from each of the
preceding theorems almost as one has just passed from the first to the second.
% U:p071.section | heading
\sectionnumber{3}
% U:p071.u04 | paragraph-start; note anchor after odd
We now pass to more general considerations. Let $b$ be a prime number $4n+3$,
$p$ a prime number $4n+1$ capable of being put under the form $t^2-bu^2$, and let
us propose to decide whether $-b$ is or is not a biquadratic residue with respect
to $p$. It is easy to see that, if $p$ can be put under the form $t^2-bu^2$, one
can always do so in such a way that $u$ is even, and consequently $t$ odd\sourcefootnote{%
To prove that this is always possible, we shall show that, if one has $t^2-bu^2=p$,
$t$ being even, it is easy to deduce from the values of $t$ and $u$ other numbers $t'$ (odd) and $u'$ which likewise
satisfy the equation $t'^2-bu'^2=p$. Let $r$ and $s$ be the least numbers such that $r^2-bs^2=1$; I say that
$r$ will be even. Indeed, it is known that, if $b$ designates a prime number $4n+3$, the equation $\rho^2-b\sigma^2=\pm2$
is always possible, and that, $\rho$ and $\sigma$ being supposed the least numbers which satisfy it, one has $r=b\sigma^2\pm1$,
$s=\rho\sigma$ (\emph{Theory of Numbers}, no.\,44.\,45). From this, and from the fact that the numbers $\rho$ and $\sigma$
are evidently both odd, it follows that $r$ is an even number. This being so, if one multiplies together the equations
$r^2-bs^2=1$, $t^2-bu^2=p$, one obtains $(rt\pm bsu)^2-b(ru\pm st)^2=p$, and one will easily see that $rt\pm bsu$
is an odd number.}.
Let therefore $p=t^2-bu^2$, and put $u=2^\nu kk'k''\ldots$, where $k$, $k'$, $k''$, $\ldots$
are the simple odd factors of $u$. One concludes immediately from the preceding
equation:
\[
\leg{p}{k}=1,\quad \leg{p}{k'}=1,\quad \leg{p}{k''}=1,\quad\text{etc.}
\]
% U:p071.u05 | continuation
The application of the reciprocity law then gives, $p$ being of the form $4n+1$:
\[
\leg{k}{p}=1,\quad \leg{k'}{p}=1,\quad \leg{k''}{p}=1,\quad\text{etc.}
\]
% U:p071.u06 | continuation to p.72
Multiplying these relations together and with the identical relation $\leg{2^\nu}{p}=\leg{2^\nu}{p}$,
'''
EN[72]=r'''% Authority: exact-scope leaf 10; full PDF page 89; printed p.72.
% U:p072.u01 | continuation of p071.u06
\noindent
one has the result:
\begin{equation*}
\leg{u}{p}=\leg{2^\nu}{p}.\tag{$\alpha$}
\end{equation*}
% U:p072.u02 | continuation
Now decompose the odd number $t$ into its simple factors and divide these
factors into two classes. Those of the first class will be designated by $g$,
$g'$, $g''$, $\ldots$, and are such that:
\begin{equation*}
\leg{-b}{g}=1,\quad\leg{-b}{g'}=1,\quad\leg{-b}{g''}=1,\quad\text{etc.}\tag{$\beta$}
\end{equation*}
% U:p072.u03 | continuation
As for those which form the second class and which we shall designate by $h$,
$h'$, $h''$, $\ldots$, they are such that:
\begin{equation*}
\leg{-b}{h}=-1,\quad\leg{-b}{h'}=-1,\quad\leg{-b}{h''}=-1,\quad\text{etc.}\tag{$\beta'$}
\end{equation*}
% U:p072.u04 | continuation
The product of all these numbers is equal to $t$, that is:
\[
t=gg'g''\ldots\times hh'h''\ldots.
\]
Inspection of the equation $t^2-bu^2=p$ gives the results:
\[
\begin{aligned}
\leg{-bp}{g}&=1, &\leg{-bp}{g'}&=1, &\leg{-bp}{g''}&=1, &\text{etc.}\\
\leg{-bp}{h}&=1, &\leg{-bp}{h'}&=1, &\leg{-bp}{h''}&=1, &\text{etc.}
\end{aligned}
\]
% U:p072.u05 | continuation
Comparison of these relations with the preceding ones then gives:
\[
\begin{aligned}
\leg{p}{g}&=1, &\leg{p}{g'}&=1, &\leg{p}{g''}&=1, &\text{etc.}\\
\leg{p}{h}&=-1, &\leg{p}{h'}&=-1, &\leg{p}{h''}&=-1, &\text{etc.}
\end{aligned}
\]
% U:p072.u06 | continuation
Applying now the reciprocity law, one obtains:
\[
\begin{aligned}
\leg{g}{p}&=1, &\leg{g'}{p}&=1, &\leg{g''}{p}&=1, &\text{etc.}\\
\leg{h}{p}&=-1, &\leg{h'}{p}&=-1, &\leg{h''}{p}&=-1, &\text{etc.}
\end{aligned}
\]
% U:p072.u07 | continuation to p.73
Multiplying these relations together, one will have:
\[
\leg{gg'g''\ldots\times hh'h''\ldots}{p}=\leg{t}{p}=\pm1,
\]
the upper or lower sign holding according as the numbers $h$, $h'$, $h''$, $\ldots$
are even or odd in number. On the other hand, if one applies the reciprocity
law to the relations $(\beta)$ and $(\beta')$, one obtains, $b$ being of the form $4n+3$:
'''
EN[73]=r'''% Authority: exact-scope leaf 11; full PDF page 90; printed p.73.
% U:p073.u01 | continuation of p072.u07
\[
\begin{aligned}
\leg{g}{b}&=1, &\leg{g'}{b}&=1, &\leg{g''}{b}&=1, &\text{etc.}\\
\leg{h}{b}&=-1, &\leg{h'}{b}&=-1, &\leg{h''}{b}&=-1, &\text{etc.}
\end{aligned}
\]
equalities which, when multiplied together, give:
\[
\leg{gg'g''\ldots\times hh'h''\ldots}{b}=\leg{t}{b}=\pm1,
\]
where the upper or lower sign must be taken according as the numbers $h$,
$h'$, $h''$, $\ldots$ are even or odd in number.
% U:p073.u02 | paragraph-start
\par
Comparison of this result with the one obtained a moment ago shows that
one always has:
\begin{equation*}
\leg{t}{p}=\leg{t}{b}.\tag{$\gamma$}
\end{equation*}
% U:p073.u03 | continuation
Let us now return to the equation $p=t^2-bu^2$ and put it in congruence form:
\[
t^2\equiv bu^2\md{p}.
\]
From this, raising both sides to the power $\dfrac{p-1}{4}$, one obtains:
\[
t^{\frac{p-1}{2}}\equiv b^{\frac{p-1}{4}}u^{\frac{p-1}{2}}\md{p}.
\]
% U:p073.u04 | continuation
The formula $(\alpha)$, namely $\leg{u}{p}=\leg{2^\nu}{p}$, where $2^\nu$ denotes the
highest power dividing $u$, can be presented in another manner. For this it
is necessary to distinguish two cases, according as $p$ is of the form $8n+1$
or of the form $8n+5$. If $p$ is a prime number $8n+1$, one has, as is known,
$\leg{2}{p}=1$, and consequently $\leg{2^\nu}{p}=1$; the formula in question
therefore becomes in this case $\leg{u}{p}=1$. If $p$ is a prime number $8n+5$,
the number $\nu$ is $=1$; for if $\nu$ were greater than unity, $u^2$ would be divisible
by $8$, and $p=t^2-bu^2$ would be of the form $8n+1$. Moreover, since in this
case $\leg{2}{p}=-1$, formula $(\alpha)$ becomes $\leg{u}{p}=-1$. The two cases
just examined are included in the formula $\leg{u}{p}=(-1)^{\frac{p-1}{4}}$, which
is equivalent to the congruence $u^{\frac{p-1}{2}}\equiv(-1)^{\frac{p-1}{4}}\md{p}$.
Substituting the value which this gives
'''
EN[74]=r'''% Authority: exact-scope leaf 12; full PDF page 91; printed p.74.
% U:p074.u01 | continuation of p073.u04
\noindent
for $u^{\frac{p-1}{2}}$ in the congruence obtained above, one has:
\[
t^{\frac{p-1}{2}}\equiv(-b)^{\frac{p-1}{4}}\md{p},
\]
a result which shows that $-b$ will or will not be a biquadratic residue with
respect to $p$ according as $t$ is or is not a quadratic residue with respect to $p$.
Comparing this result with that contained in formula $(\gamma)$, one arrives at
the theorem which we shall state:
% U:p074.u02 | paragraph-start
\par
“Let $b$ designate a prime number $4n+3$, and $p$ a prime number $4n+1$ capable
of being put under the form $t^2-bu^2$. Having written $p=t^2-bu^2$ (where $t$
is supposed odd), I say that $-b$ will or will not be a biquadratic residue with
respect to $p$ according as $t$ is or is not a quadratic residue with respect to $b$.”
% U:p074.section | heading
\sectionnumber{4}
% U:p074.u03 | paragraph-start
We shall now deduce from this theorem another by means of which one can
decide still more quickly whether $-b$ is or is not a biquadratic residue with
respect to $p$. Preserve the preceding notations and put $p=\varphi^2+\psi^2$
(where $\psi$ is supposed even). Equating this value of $p$ to the one considered
above, one has:
\[
p=t^2-bu^2=\varphi^2+\psi^2,
\]
and, after transposing:
\[
t^2-\psi^2=(t+\psi)(t-\psi)=\varphi^2+bu^2.
\]
% U:p074.u04 | continuation
There are now two cases to distinguish, according as $\varphi$ is or is not
divisible by $b$. We begin with the latter of these two cases. Let $m$ be the
greatest common divisor of $\varphi$ and $u$, which will be odd ($\varphi$ being odd)
and not divisible by $b$, and put $\varphi=m\varphi'$, $u=mu'$. Substitution of
these values in the last equation changes it into:
\[
(t+\psi)(t-\psi)=m^2(\varphi'^2+bu'^2).
\]
% U:p074.u05 | continuation; section 4 continues on p.75, not produced in S01
It is evident, from this equation, that $t+\psi$ is composed of two factors
$E$ and $K$, the first of which divides $m^2$, the second $\varphi'^2+bu'^2$,
and that the same is true of $t-\psi$. Denoting the factors of this last
number by $F$ and $L$, we shall have the equations:
\[
\begin{aligned}
t+\psi&=EK, &t-\psi&=FL,\\
m^2&=EF, &\varphi'^2+bu'^2&=KL.
\end{aligned}
\]
'''
for lang,pages in [('fr',FR),('en',EN)]:
 for p,txt in pages.items():
  (ROOT/f'editions/{lang}/pages/p{p:03d}.tex').write_text(txt,encoding='utf8')
print('Wrote',len(FR),'French and',len(EN),'English page records')
