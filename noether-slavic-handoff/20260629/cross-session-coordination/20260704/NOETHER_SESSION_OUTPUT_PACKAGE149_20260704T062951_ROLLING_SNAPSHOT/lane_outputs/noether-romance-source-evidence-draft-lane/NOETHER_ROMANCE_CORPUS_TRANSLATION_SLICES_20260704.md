# Noether Romance Corpus Translation Slices

Status: DRAFT / NON-CANONICAL / NOT NATIVE REVIEWED / NOT APPROVED.

Lane: French and Spanish only. These are working corpus-translation sidecars, not reviewer packets and not canonical text.

German baseline:
`C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical\tmp\zenodo_20836874_inspect\localcodex\Noether_R124plus_LocalCodex_PostR124_Consolidated_WebDrop_20260624\tex\cum_de_R124plus_localcodex_current_candidate_20260624.tex`

Baseline SHA256: `C0ACCB2D4EB98F54B41BC3977DFA0CB57A349C74B7B35E06453343D15ACAB4ED`

Termbase input:
`C:\Users\memo_\Documents\Codex\2026-07-04\noether-romance-source-evidence-draft-lane\outputs\NOETHER_ROMANCE_LANE_DRAFT_TERMBASE_20260704.csv`

## Slice R01: Algebra / Commutative Algebra

Source anchor: German baseline `L18999-L19006`.

Rows covered: `term-fr-0001`, `term-fr-0002`, `term-es-0001`, `term-es-0005`.

Evidence note: exact German anchors include `Nichtkommutative Algebra`, `kommutative Algebra`, and `Algebra`; local Romance shelf evidence gives French `algèbre` 1264 hits / 42 files, French `algèbre commutative` 35 hits / 10 files, Spanish `álgebra` 417 hits, Spanish `álgebra conmutativa` 19 hits / 12 files.

Unresolved flags: none for the core terms; prose around `Abspaltungs- und Zerfällungskörper` remains draft because the historical pair does not have a single fixed modern Romance formula.

French draft:

**Algèbre non commutative.** Les principaux théorèmes de l'algèbre commutative sont, comme on le sait, contenus dans la théorie galoisienne; celle-ci est précédée par la théorie des corps qui permettent de détacher un facteur linéaire ou de décomposer entièrement un polynôme donné en facteurs linéaires. Je développe ici les parties correspondantes de l'algèbre dans le cas non commutatif, en particulier dans le cas hypercomplexe. Je travaille pour cela, par principe, avec des méthodes non commutatives: la représentation dans des corps non commutatifs. À la fin, je montre comment les théorèmes déjà mentionnés de l'algèbre commutative peuvent se fonder de manière entièrement parallèle au moyen de représentations dans des corps commutatifs.

Spanish draft:

**Álgebra no conmutativa.** Los teoremas principales del álgebra conmutativa están, como es sabido, contenidos en la teoría de Galois; a esta la precede la teoría de los cuerpos en los que un polinomio dado puede separar un factor lineal o descomponerse por completo en factores lineales. Aquí desarrollo las partes correspondientes del álgebra en el caso no conmutativo, en particular en el caso hipercomplejo. Para ello trabajo, por principio, con métodos no conmutativos: la representación en cuerpos no conmutativos. Al final muestro cómo los teoremas mencionados del álgebra conmutativa pueden fundamentarse de modo enteramente paralelo mediante representaciones en cuerpos conmutativos.

## Slice R02: Hilbert Basis / Basis Theorems / Finiteness

Source anchor: German baseline `L4558-L4586`.

Rows covered: `term-fr-0003`, `term-es-0002`, `term-es-0004`, `term-es-0007`; also supports the finiteness side of `term-fr-0014`, `term-fr-0015`, `term-es-0016`, `term-es-0017`.

Evidence note: German source uses `Hilbertsche Theorem ... Modulbasis` and `Basissätze`; Spanish shelf has `base de Hilbert` 4 hits / 4 files and `teorema de la base de Hilbert` 2 hits / 2 files. French validated shelf has 0 exact hits for `base de Hilbert`, so French use is draft and should be reviewed; for theorem contexts the sidecar prefers `théorème de la base de Hilbert`.

Unresolved flags: French exact term evidence gap for `base de Hilbert`; Spanish `finitamente generado` is a modern rendering for finite-basis/finitely generated contexts, not a literal translation of every `endlich` phrase.

French draft:

Le présent travail traite des questions de base pour des systèmes arbitraires de fonctions rationnelles et entières rationnelles. Les méthodes employées, issues de la théorie des corps, font apparaître comme essentiel le traitement de ces questions pour les corps de fonctions rationnelles; la généralisation des résultats à des systèmes arbitraires s'en déduit ensuite.

Pour les systèmes généraux, la seule question de base connue jusqu'ici est l'existence d'une base de module assurée par le théorème de Hilbert. On résout ici complètement, pour tout système arbitraire, la question de la représentation rationnelle par l'existence d'une base rationnelle; pour les corps, cette base rationnelle apparaît déjà au §4. Cette existence permet de partir partout du corps ou du système défini abstraitement, et d'éviter ainsi les difficultés qui proviennent seulement du choix particulier d'une base rationnelle, par exemple l'apparition de dénominateurs spéciaux ou de points fondamentaux des fonctions de base.

Pour les corps, on traite encore la question de la base minimale, c'est-à-dire d'une base rationnelle composée de fonctions algébriquement indépendantes. Les méthodes de la théorie des corps conduisent en outre à une base rationnelle distinguée, la base d'involution, qui devient essentielle en particulier pour les domaines d'intégrité formés de polynômes. Elle donne une représentation avec un dénominateur fixe, comme dans le cas particulier de la représentation typique des invariants.

De la représentabilité rationnelle on tire ensuite, aussi loin que possible, des conséquences pour la représentabilité entière rationnelle, c'est-à-dire pour la question de la finitude au sens strict. Les théorèmes de finitude connus jusqu'ici reposent tous sur le fait que le théorème de Hilbert sur la base de modules garantit la finitude pour les systèmes où une représentation
`F=A_1f_1+\cdots+A_kf_k`
entraîne une seconde représentation
`F=B_1f_1+\cdots+B_kf_k`,
les `B_i` appartenant au système et étant de degré plus petit que `F`.

Le théorème de la base rationnelle et les méthodes de la théorie des corps permettent en revanche de conclure à la finitude sous des hypothèses d'une autre nature. On obtient ainsi, comme réponse partielle à un problème de Hilbert, une classe de fonctions relativement entières qui forment des domaines d'intégrité finis et dont la base d'intégralité est donnée par la base d'involution mentionnée ci-dessus. On montre également que tous les systèmes réguliers de polynômes possèdent une base d'intégralité, tandis que des systèmes non réguliers sans base d'intégralité s'indiquent facilement.

Spanish draft:

El presente trabajo trata cuestiones de base para sistemas arbitrarios de funciones racionales y enteras racionales. Los métodos empleados, procedentes de la teoría de cuerpos, hacen que el tratamiento de estas cuestiones para cuerpos de funciones racionales aparezca como lo esencial; la generalización de los resultados a sistemas arbitrarios se obtiene después como consecuencia.

Para sistemas generales, hasta ahora solo se conoce la existencia de una base de módulo garantizada por el teorema de Hilbert. A continuación se resuelve por completo, para todo sistema arbitrario, la cuestión de la representabilidad racional mediante la existencia de una base racional; para los cuerpos, la base racional se obtiene ya en el §4. Esta existencia permite partir siempre del cuerpo o sistema definido abstractamente, evitando dificultades que dependen únicamente de la elección particular de una base racional, como la aparición de denominadores especiales o de puntos fundamentales de las funciones de base.

Para los cuerpos se trata además la cuestión de la base mínima, es decir, de una base racional formada por funciones algebraicamente independientes. Los métodos de la teoría de cuerpos conducen también a una base racional distinguida, la base de involución, que resulta esencial en particular para dominios de integridad de polinomios. Esta da una representación con denominador fijo, como ocurre en el caso particular de la representación típica de los invariantes.

De la representabilidad racional se extraen luego, en la mayor medida posible, consecuencias para la representabilidad entera racional, esto es, para la cuestión de finitud en sentido estricto. Los teoremas de finitud conocidos hasta ahora descansan todos en el hecho de que el teorema de Hilbert de la base de módulos garantiza la finitud para aquellos sistemas en los que una representación
`F=A_1f_1+\cdots+A_kf_k`
implica una segunda representación
`F=B_1f_1+\cdots+B_kf_k`,
donde los `B_i` pertenecen al sistema y tienen grado menor que `F`.

El teorema de la base racional y los métodos de la teoría de cuerpos permiten, en cambio, deducir finitud bajo hipótesis de otra clase. Así se obtiene, como respuesta parcial a un problema de Hilbert, una clase de funciones relativamente enteras que son dominios de integridad finitos y cuya base de integridad está dada por la base de involución antes mencionada. También se muestra que todos los sistemas regulares de polinomios poseen una base de integridad, mientras que es fácil dar sistemas no regulares sin base de integridad.

## Slice R03: Ring, Ideal, Finiteness Condition, Noetherian Interpretation

Source anchor: German baseline `L11350-L11384`.

Rows covered: `term-fr-0014`, `term-fr-0015`, `term-fr-0018`, `term-fr-0019`, `term-fr-0021`, `term-es-0016`, `term-es-0017`, `term-es-0022`, `term-es-0023`, `term-es-0025`, plus finiteness support for `term-es-0007`.

Evidence note: German source does not use modern `Noetherian`; it defines the finiteness condition: every ideal is finite / has an ideal basis, followed by the finite-chain theorem. This is the responsible source anchor for French `anneau noethérien` and Spanish `anillo noetheriano`, with the label kept as a modern explanatory rendering, not a literal German term.

Unresolved flags: `Ringbereich` is rendered contextually as `anneau`/`domaine annulaire` and `anillo`/`ámbito de anillos`; keep flagged for human review.

French draft:

**Anneau, idéal, condition de finitude.** Le domaine de base `Σ` est un anneau commutatif au sens abstrait. Il se compose d'éléments `a,b,c,...,f,g,h,...`, munis d'une relation d'égalité satisfaisant les conditions usuelles, et de deux opérations, addition et multiplication, qui associent toujours à deux éléments `a` et `b` un troisième élément, leur somme `a+b` et leur produit `a·b`. Ces opérations doivent satisfaire les lois suivantes: associativité et commutativité de l'addition, associativité et commutativité de la multiplication, distributivité, et soustraction sans restriction et univoque. Il existe donc, pour `a+x=b`, un unique élément `x`, noté `b-a`.

Il résulte de ces propriétés qu'il existe un zéro. Un anneau n'a cependant pas nécessairement d'élément unité, et le produit de deux éléments peut s'annuler sans que l'un des facteurs s'annule. Les anneaux dans lesquels l'annulation d'un produit entraîne toujours l'annulation d'un facteur, et qui possèdent en outre une unité, sont appelés domaines d'intégrité proprement dits. Pour la somme finie `a+a+...+a`, on emploie l'abréviation usuelle `na`; les entiers `n` ne sont alors que des signes abrégés, non des éléments de l'anneau.

Par idéal `M` de `Σ`, on entend un système d'éléments de `Σ` qui vérifie deux conditions: avec `f`, il contient aussi `a·f` pour tout élément `a` de `Σ`; avec `f` et `g`, il contient aussi la différence `f-g`, et donc avec `f` il contient `nf` pour tout entier `n`. Si `f` est élément de `M`, on l'exprime par `f≡0(M)` et l'on dit que `f` est divisible par `M`. Si chaque élément de `N` est aussi élément de `M`, on dit que `N` est divisible par `M`, et l'on écrit `N≡0(M)`.

Les autres notions connues se conservent littéralement. Le plus grand commun diviseur de deux idéaux `A` et `B`, noté `D=(A,B)`, est l'ensemble des éléments qui peuvent s'écrire sous la forme `a+b`, où `a` parcourt `A` et `b` parcourt `B`; cet ensemble est de nouveau un idéal. De même, le plus grand commun diviseur d'une infinité d'idéaux est défini par les sommes d'éléments pris dans un nombre fini de ces idéaux.

Si l'idéal `M` contient un nombre fini d'éléments `f_1,...,f_ρ` tels que tout `f≡0(M)` s'exprime sous la forme
`f=a_1f_1+\cdots+a_ρf_ρ+n_1f_1+\cdots+n_ρf_ρ`,
où les `a_i` sont des éléments du domaine annulaire et les `n_i` des entiers, alors `M` est appelé idéal fini, et `f_1,...,f_ρ` une base de l'idéal.

Dans la suite, on ne considère que les anneaux `Σ` qui satisfont la condition de finitude: tout idéal de `Σ` est fini, donc possède une base d'idéal. De cette condition découle directement le théorème de la chaîne finie: si `M,M_1,M_2,...` est un système dénombrable d'idéaux de `Σ`, chacun divisible par le suivant, alors tous les idéaux sont identiques à partir d'un certain indice fini. Autrement dit, toute chaîne simplement ordonnée d'idéaux dans laquelle chaque idéal est un diviseur propre du précédent s'arrête après un nombre fini d'étapes.

Spanish draft:

**Anillo, ideal, condición de finitud.** El ámbito de base `Σ` es un anillo conmutativo en sentido abstracto. Está formado por elementos `a,b,c,...,f,g,h,...`, dotados de una relación de igualdad que satisface las condiciones usuales, y por dos operaciones, suma y multiplicación, que asignan siempre a dos elementos `a` y `b` un tercer elemento, la suma `a+b` y el producto `a·b`. Estas operaciones deben satisfacer las leyes siguientes: asociatividad y conmutatividad de la suma, asociatividad y conmutatividad de la multiplicación, distributividad, y sustracción irrestricta y unívoca. Así, para `a+x=b`, existe en `Σ` un único elemento `x`, denotado `b-a`.

De estas propiedades se sigue la existencia del cero. Un anillo, sin embargo, no necesita tener unidad, y puede anularse el producto de dos elementos sin que se anule ninguno de los factores. Los anillos en los que la anulación de un producto implica siempre la anulación de un factor, y que además poseen unidad, se llaman dominios de integridad propiamente dichos. Para la suma finita `a+a+...+a` se introduce la abreviatura usual `na`; los enteros `n` se consideran solo signos abreviados, no elementos del anillo.

Por un ideal `M` de `Σ` se entiende un sistema de elementos de `Σ` que satisface dos condiciones: junto con `f` contiene también `a·f`, para todo elemento `a` de `Σ`; junto con `f` y `g` contiene también la diferencia `f-g`, y por tanto junto con `f` contiene `nf` para todo entero `n`. Si `f` es elemento de `M`, se expresa por `f≡0(M)` y se dice que `f` es divisible por `M`. Si cada elemento de `N` es también elemento de `M`, se dice que `N` es divisible por `M`, y se escribe `N≡0(M)`.

Las demás nociones conocidas se conservan literalmente. El máximo común divisor de dos ideales `A` y `B`, denotado `D=(A,B)`, es el conjunto de los elementos que pueden escribirse como `a+b`, donde `a` recorre `A` y `b` recorre `B`; este conjunto vuelve a ser un ideal. De modo análogo, el máximo común divisor de infinitos ideales se define mediante sumas de elementos tomados de un número finito de esos ideales.

Si el ideal `M` contiene un número finito de elementos `f_1,...,f_ρ` tales que todo `f≡0(M)` se expresa en la forma
`f=a_1f_1+\cdots+a_ρf_ρ+n_1f_1+\cdots+n_ρf_ρ`,
donde los `a_i` son elementos del ámbito de anillos y los `n_i` son enteros, entonces `M` se llama ideal finito, y `f_1,...,f_ρ` una base del ideal.

En lo que sigue se consideran solo anillos `Σ` que satisfacen la condición de finitud: todo ideal de `Σ` es finito, es decir, posee una base de ideal. De esta condición se deduce directamente el teorema de la cadena finita: si `M,M_1,M_2,...` es un sistema numerable de ideales de `Σ`, cada uno divisible por el siguiente, entonces a partir de algún índice finito todos los ideales son idénticos. En otras palabras, toda cadena simplemente ordenada de ideales en la que cada ideal es un divisor propio del inmediatamente anterior termina en un número finito de pasos.

## Slice R04: Irreducible Ideals

Source anchor: German baseline `L11447-L11458`.

Rows covered: `term-fr-0016`, `term-es-0018`; also supports ideal rows.

Evidence note: exact German anchor `irreduzibel`; local shelf evidence supports French `irréductible` 162 hits / 14 files and Spanish `irreducible` 321 hits / 20 files.

Unresolved flags: historical ideal lcm language kept as `plus petit commun multiple` / `mínimo común múltiplo`.

French draft:

Un idéal `M` est dit réductible lorsqu'il peut être représenté comme plus petit commun multiple de deux diviseurs propres; dans le cas contraire, `M` est dit irréductible.

On prouve alors, au moyen du théorème de la chaîne finie et de la représentation réduite, que tout idéal peut être représenté comme plus petit commun multiple d'un nombre fini d'idéaux irréductibles. En effet, un idéal arbitraire `M` est soit irréductible, auquel cas `M=[M]` est déjà une représentation du type demandé; soit `M=[B_1,C_1]`, où `B_1` et `C_1` sont des diviseurs propres de `M`, et la représentation peut être supposée réduite. La même alternative vaut pour `C_1`: il est irréductible, ou bien il admet une représentation réduite `C_1=[B_2,C_2]`. En poursuivant ainsi, on obtient une suite de représentations réduites.

Spanish draft:

Un ideal `M` se llama reducible si puede representarse como mínimo común múltiplo de dos divisores propios; en el caso contrario, `M` se llama irreducible.

Se prueba entonces, mediante el teorema de la cadena finita y usando la representación reducida, que todo ideal puede representarse como mínimo común múltiplo de un número finito de ideales irreducibles. En efecto, un ideal arbitrario `M` es o bien irreducible, en cuyo caso `M=[M]` ya es una representación del tipo requerido; o bien `M=[B_1,C_1]`, donde `B_1` y `C_1` son divisores propios de `M`, y la representación puede suponerse reducida. Para `C_1` vale la misma alternativa: es irreducible, o admite una representación reducida `C_1=[B_2,C_2]`. Continuando así se obtiene una sucesión de representaciones reducidas.

## Slice R05: Primary and Prime Ideals

Source anchor: German baseline `L11590-L11603`.

Rows covered: `term-fr-0021`, `term-es-0025`; supports ideal rows and primary-ideal context.

Evidence note: exact German anchors `Primideale`, `Primärideale`; local shelf evidence supports French `idéal premier` 127 hits / 12 files and Spanish `ideal primo` 89 hits / 13 files.

Unresolved flags: none for `prime ideal`; primary-ideal terms are outside the active Romance row list but are left in the translation because they are necessary source context.

French draft:

Il s'agit, dans ce qui suit, du rapport entre idéaux primaires et idéaux irréductibles.

Un idéal `Q` est dit primaire si, de `a·b≡0(Q)` et `a≠0(Q)`, il suit nécessairement que `b^κ≡0(Q)`, où l'exposant `κ` est fini. On peut formuler la définition ainsi: si un produit `a·b` est divisible par `Q`, alors ou bien l'un des facteurs est divisible, ou bien une puissance de chaque facteur l'est. Si, en particulier, on peut toujours prendre `κ=1`, l'idéal est appelé idéal premier.

La définition se reformule aussi en termes de produits d'idéaux. Un idéal `Q` est primaire si, de `AB≡0(Q)` et `A≠0(Q)`, il suit nécessairement que `B^λ≡0(Q)`. Si l'on peut toujours prendre `λ=1`, l'idéal est premier. Pour un idéal premier `P`, de `AB≡0(P)` et `A≠0(P)` il suit donc toujours `B≡0(P)`.

Spanish draft:

En lo que sigue se estudia la relación entre ideales primarios e ideales irreducibles.

Un ideal `Q` se llama primario si de `a·b≡0(Q)` y `a≠0(Q)` se sigue necesariamente que `b^κ≡0(Q)`, donde el exponente `κ` es finito. La definición también puede formularse así: si un producto `a·b` es divisible por `Q`, entonces o bien uno de los factores es divisible, o bien lo es una potencia de cada factor. Si, en particular, siempre puede tomarse `κ=1`, el ideal se llama ideal primo.

La definición se reformula también mediante productos de ideales. Un ideal `Q` se llama primario si de `AB≡0(Q)` y `A≠0(Q)` se sigue necesariamente que `B^λ≡0(Q)`. Si siempre puede tomarse `λ=1`, el ideal es primo. Para un ideal primo `P`, de `AB≡0(P)` y `A≠0(P)` se sigue por tanto siempre `B≡0(P)`.

## Slice R06: Modules, Finite Module Bases, Submodules

Source anchor: German baseline `L12124-L12140`.

Rows covered: `term-fr-0006`, `term-fr-0009`, `term-es-0007`, `term-es-0008`, `term-es-0011`; supports `Noetherian` finiteness rows.

Evidence note: exact German anchors include `Modul`, `Untermodul`, `endlicher Modul`, `Modulbasis`, `Endlichkeitsbedingung`. Local shelf evidence supports French `module` 1606 hits / 57 files, French `sous-module` 71 hits / 11 files, Spanish `módulo` 610 hits / 18 files, Spanish `submódulo` 95 hits / 12 files, and Spanish finite-generation terms through the page-context row.

Unresolved flags: translate `endlicher Modul` as `module fini (de type fini)` / `módulo finito (finitamente generado)` on first mention to preserve Noether's finite-basis sense.

French draft:

D'après cette définition, `T` lui-même forme un module dans `(Σ,T)`. Si, en particulier, le domaine `T` et les opérations qui y sont fixées coïncident avec le domaine `Σ` et les opérations qui y valent, alors le module `M` devient un idéal à droite `M` de `Σ`. Si `Σ` est de plus supposé commutatif, on obtient la notion ordinaire d'idéal, qui apparaît ainsi comme un cas particulier de la notion de module.

Toutes les définitions du §1 subsistent pour les modules. Ainsi `α≡0(M)` ou `N≡0(M)` signifie que `α`, ou respectivement chaque élément de `N`, est élément de `M`; autrement dit, `α` ou `N` est divisible par `M`. De même, la définition du plus grand commun diviseur et celle du plus petit commun multiple demeurent inchangées.

Si le module `M` contient un nombre fini d'éléments `α_1,...,α_ρ` tels que `M=(α_1,...,α_ρ)`, c'est-à-dire que tout `α≡0(M)` puisse s'écrire
`α=c_1α_1+\cdots+c_ρα_ρ+n_1α_1+\cdots+n_ρα_ρ`,
où les `c_i` sont des grandeurs de `Σ` et les `n_i` des entiers, alors `M` est appelé module fini, ou de type fini dans le sens moderne, et `α_1,...,α_ρ` une base de module.

Dans la suite, par analogie avec le §1, on ne considère que des domaines `(Σ,T)` qui satisfont la condition de finitude: tout module dans `(Σ,T)` est fini et possède donc une base de module. Le théorème de la chaîne finie vaut alors aussi pour les modules. Les résultats sur les représentations les plus courtes et réduites, puis la représentabilité de tout module comme plus petit commun multiple d'un nombre fini de modules irréductibles, se transfèrent directement.

Spanish draft:

Según esta definición, `T` mismo forma un módulo en `(Σ,T)`. Si, en particular, el ámbito `T` y las operaciones fijadas allí coinciden con el ámbito `Σ` y con las operaciones que rigen en él, entonces el módulo `M` pasa a ser un ideal derecho `M` de `Σ`. Si además se supone que `Σ` es conmutativo, se obtiene la noción ordinaria de ideal, que aparece así como un caso particular de la noción de módulo.

Todas las definiciones del §1 se conservan para módulos. Así, `α≡0(M)` o `N≡0(M)` significa que `α`, o respectivamente cada elemento de `N`, es elemento de `M`; en otras palabras, `α` o `N` es divisible por `M`. Asimismo, la definición de máximo común divisor y la de mínimo común múltiplo permanecen literalmente iguales.

Si el módulo `M` contiene un número finito de elementos `α_1,...,α_ρ` tales que `M=(α_1,...,α_ρ)`, es decir, tales que todo `α≡0(M)` pueda escribirse como
`α=c_1α_1+\cdots+c_ρα_ρ+n_1α_1+\cdots+n_ρα_ρ`,
donde los `c_i` son magnitudes de `Σ` y los `n_i` son enteros, entonces `M` se llama módulo finito, o finitamente generado en el sentido moderno, y `α_1,...,α_ρ` una base de módulo.

En lo que sigue, de manera análoga al §1, se consideran solo dominios `(Σ,T)` que satisfacen la condición de finitud: todo módulo en `(Σ,T)` es finito y posee, por tanto, una base de módulo. El teorema de la cadena finita vale entonces también para módulos. Los resultados sobre representaciones más cortas y reducidas, y luego la representabilidad de todo módulo como mínimo común múltiplo de un número finito de módulos irreducibles, se transfieren directamente.

## Slice R07: Hilbert Module-Basis Theorem in Polynomial Rings

Source anchor: German baseline `L12174-L12183`.

Rows covered: `term-fr-0003`, `term-es-0002`, `term-es-0004`; supports `term-fr-0016`, `term-es-0018`, `term-fr-0021`, `term-es-0025`.

Evidence note: German source explicitly cites Hilbert's theorem on module bases and uses it for polynomial rings. French exact shelf hit for `base de Hilbert` remains absent; Spanish exact shelf evidence is present.

Unresolved flags: French wording `théorème de Hilbert sur la base de modules` is closer to this source than the row shorthand `base de Hilbert`; route to human review before any canonical use.

French draft:

Le domaine annulaire de base `Σ` est le domaine de tous les polynômes en `x_1,...,x_n` à coefficients complexes arbitraires. Pour ce domaine, la condition de finitude est satisfaite d'après le théorème de Hilbert sur la base de modules. Il s'agit alors de relier les théorèmes précédents aux théorèmes connus de la théorie de l'élimination et de la théorie des modules.

Ce lien est établi par le cas particulier suivant d'un théorème connu de Hilbert. Si `f` s'annule pour tout système fini de valeurs de `x_1,...,x_n` qui est zéro de tous les polynômes d'un idéal premier `P`, alors `f` est divisible par `P`. Autrement dit, un idéal premier `P` se compose de la totalité des polynômes qui s'annulent sur ses zéros.

Si donc un produit `fg` s'annule sur tous les zéros de `P`, au moins l'un des deux facteurs s'y annule. Les zéros forment alors une variété algébrique irréductible. Réciproquement, si l'on prend cette propriété comme définition de l'objet irréductible, l'ensemble des polynômes qui s'annulent sur lui forme un idéal premier; les idéaux premiers et les objets irréductibles se correspondent ainsi biunivoquement.

Spanish draft:

El ámbito de anillos de base `Σ` está formado por todos los polinomios en `x_1,...,x_n` con coeficientes complejos arbitrarios. Para este dominio, la condición de finitud se satisface por el teorema de Hilbert de la base de módulos. Se trata entonces de relacionar los teoremas anteriores con los teoremas conocidos de la teoría de la eliminación y de la teoría de módulos.

Esta relación se establece mediante el siguiente caso particular de un teorema conocido de Hilbert. Si `f` se anula para todo sistema finito de valores de `x_1,...,x_n` que sea cero de todos los polinomios de un ideal primo `P`, entonces `f` es divisible por `P`. En otras palabras, un ideal primo `P` está formado por la totalidad de los polinomios que se anulan en sus ceros.

Así, si un producto `fg` se anula en todos los ceros de `P`, al menos uno de los factores se anula allí. Los ceros forman entonces una variedad algebraica irreducible. Recíprocamente, si se toma esta propiedad como definición del objeto irreducible, el conjunto de los polinomios que se anulan en él forma un ideal primo; los ideales primos y los objetos irreducibles se corresponden así biunívocamente.

## Slice R08: Module and Ring Homomorphisms, Quotient Modules/Rings, Isomorphism Theorems

Source anchor: German baseline `L15002-L15024`.

Rows covered: `term-fr-0007`, `term-fr-0012`, `term-fr-0013`, `term-es-0009`, `term-es-0014`, `term-es-0015`; supports ring/ideal/module rows.

Evidence note: exact German anchors include `homomorph`, `isomorph`, `Restklassenmodul`, `Restklassenring`; local shelf evidence supports French `homomorphisme` 149 hits / 27 files, French `isomorphisme` 244 hits / 38 files, Spanish `homomorfismo` 125 hits / 18 files, Spanish `isomorfismo` 169 hits / 17 files.

Unresolved flags: `Restklassenmodul` translated as `module quotient (module de classes résiduelles)` / `módulo cociente (módulo de clases residuales)`; `Restklassenring` similarly.

French draft:

Soient `M` et `\overline M` des domaines de modules relativement à `R`. On dit que `M` est homomorphe, plus précisément module-homomorphe, à `\overline M`, et l'on écrit `M∼\overline M`, si à chaque élément de `M` correspond un et un seul élément de `\overline M`, de telle sorte que `\overline M` soit entièrement parcouru, et si cette correspondance respecte la différence et la multiplication par le même élément de `R`. Ainsi, de `β∼\overline β` et `γ∼\overline γ`, il suit toujours `(β-γ)∼(\overline β-\overline γ)` et `rβ∼r\overline β`.

À un `R`-module `B` de `M` correspond donc homomorphiquement un `R`-module `\overline B` de `\overline M`. Réciproquement, l'ensemble `C*` des éléments de `M` auxquels correspondent des éléments d'un `R`-module `\overline C` de `\overline M` forme un `R`-module de `M` déterminé par `\overline C`. Si `A` est le module correspondant au zéro de `\overline M`, alors les éléments se répartissent en classes modulo `A`, et ces classes correspondent biunivoquement aux éléments de `\overline C`.

Lorsque la correspondance entre les éléments de `M` et de `\overline M` est bijective dans les deux sens, les domaines sont dits isomorphes, plus précisément module-isomorphes.

Si `A` est un `R`-module quelconque de `M`, on obtient un domaine de modules homomorphe à `M`, le module quotient `M|A` ou module de classes résiduelles, en prenant la congruence modulo `A` comme nouvelle relation d'égalité. Tout homomorphisme est engendré par ce passage au module quotient: si `M∼\overline M` et si `A` est le module envoyé sur le zéro de `\overline M`, alors `\overline M` est isomorphe au module quotient `M|A`.

Premier théorème d'isomorphisme: si `\overline M` désigne le module quotient `M|A` et si `C` est un diviseur de `A`, alors `\overline M|\overline C ≅ M|C`. Deuxième théorème d'isomorphisme: si `B` et `A` sont des modules de `M`, alors `(B,A)|A ≅ B|[B,A]`.

Les mêmes raisonnements valent pour les anneaux commutatifs lorsque les modules sont remplacés par des idéaux, et les homomorphismes et isomorphismes de modules par des homomorphismes et isomorphismes d'anneaux. On obtient alors l'anneau quotient, ou anneau de classes résiduelles, et les théorèmes d'isomorphisme correspondants.

Spanish draft:

Sean `M` y `\overline M` dominios de módulos respecto de `R`. Se dice que `M` es homomorfo, más precisamente módulo-homomorfo, a `\overline M`, y se escribe `M∼\overline M`, si a cada elemento de `M` le corresponde uno y solo un elemento de `\overline M`, de modo que `\overline M` quede agotado, y si esta correspondencia respeta la diferencia y la multiplicación por el mismo elemento de `R`. Así, de `β∼\overline β` y `γ∼\overline γ` se sigue siempre `(β-γ)∼(\overline β-\overline γ)` y `rβ∼r\overline β`.

A un `R`-módulo `B` de `M` le corresponde entonces homomórficamente un `R`-módulo `\overline B` de `\overline M`. Recíprocamente, el conjunto `C*` de los elementos de `M` a los que corresponden elementos de un `R`-módulo `\overline C` de `\overline M` forma un `R`-módulo en `M` determinado por `\overline C`. Si `A` es el módulo que corresponde al cero de `\overline M`, entonces los elementos se descomponen en clases módulo `A`, y esas clases corresponden biunívocamente a los elementos de `\overline C`.

Cuando la correspondencia entre los elementos de `M` y de `\overline M` es biyectiva en ambos sentidos, los dominios se llaman isomorfos, más precisamente módulo-isomorfos.

Si `A` es un `R`-módulo cualquiera de `M`, se obtiene un dominio de módulos homomorfo a `M`, el módulo cociente `M|A` o módulo de clases residuales, tomando la congruencia módulo `A` como nueva relación de igualdad. Todo homomorfismo se genera mediante este paso al módulo cociente: si `M∼\overline M` y `A` es el módulo que se envía al cero de `\overline M`, entonces `\overline M` es isomorfo al módulo cociente `M|A`.

Primer teorema de isomorfía: si `\overline M` denota el módulo cociente `M|A` y `C` es divisor de `A`, entonces `\overline M|\overline C ≅ M|C`. Segundo teorema de isomorfía: si `B` y `A` son módulos de `M`, entonces `(B,A)|A ≅ B|[B,A]`.

Los mismos razonamientos valen para anillos conmutativos cuando los módulos se reemplazan por ideales, y los homomorfismos e isomorfismos de módulos por homomorfismos e isomorfismos de anillos. Se obtiene entonces el anillo cociente, o anillo de clases residuales, y los teoremas de isomorfía correspondientes.

## Slice R09: Localization / Quotient Rings at Prime Ideals

Source anchor: German baseline `L16225-L16233`.

Rows covered: `term-fr-0004`, `term-es-0003`; supports prime-ideal rows.

Evidence note: German exact modern `Lokalisierung` not found; the source uses `Quotientenring` notation `o_p`, which in this context is the local/quotient construction at a prime ideal. Local shelf evidence supports French `localisation` 57 hits / 21 files and Spanish `localización` 6 hits / 5 files.

Unresolved flags: translate `Quotientenring` here as `anneau de quotients / anneau localisé` and `anillo de cocientes / anillo localizado`, not as quotient-by-ideal `anneau quotient` / `anillo cociente`.

French draft:

Les mêmes considérations valent pour l'anneau de multiplication `o`. En particulier, si `p` est un idéal premier, alors l'anneau de quotients `o_p`, c'est-à-dire l'anneau localisé en `p`, ne possède qu'un seul idéal premier distinct de l'idéal nul et de l'idéal unité. Par l'isomorphisme des anneaux de classes résiduelles, `o_p` est encore un anneau de multiplication; il devient donc un anneau principal, et la base de l'idéal premier déduit de `p` est un élément premier de `o_p`.

L'idéal étendu d'un idéal arbitraire `c` de `o` est engendré par la composante primaire de `c` appartenant à `p`; il est donc égal à `(p)^α` ou à l'idéal unité, selon que `p` intervient dans `c`, et à la puissance `α`, ou n'y intervient pas. Il en résulte que si les extensions de deux idéaux `b` et `c` de `o` coïncident dans tous les anneaux localisés `o_p`, alors `b` et `c` sont identiques.

Soit maintenant `p` un idéal premier de `o` et soit `P=T p` l'idéal étendu dans `T`. L'anneau localisé `T_P` possède une base de module composée d'éléments linéairement indépendants relativement à l'anneau principal `o_p`; en même temps, `T_P` est un ordre fini sur `o_p` dans le corps d'extension `K` du corps des quotients `Ω` de `o_p`. Ainsi le théorème du discriminant vaut pour `T_P` relativement à `o_p`.

Spanish draft:

Las mismas consideraciones valen para el anillo de multiplicación `o`. En particular, si `p` es un ideal primo, entonces el anillo de cocientes `o_p`, es decir, el anillo localizado en `p`, posee un único ideal primo distinto del ideal cero y del ideal unidad. Por el isomorfismo de los anillos de clases residuales, `o_p` sigue siendo un anillo de multiplicación; por tanto se vuelve un anillo principal, y la base del ideal primo derivado de `p` es un elemento primo de `o_p`.

El ideal extendido de un ideal arbitrario `c` de `o` está generado por la componente primaria de `c` correspondiente a `p`; por tanto es igual a `(p)^α` o al ideal unidad, según que `p` aparezca en `c`, y a la potencia `α`, o no aparezca. De aquí se sigue que si las extensiones de dos ideales `b` y `c` de `o` coinciden en todos los anillos localizados `o_p`, entonces `b` y `c` son idénticos.

Sea ahora `p` un ideal primo de `o` y sea `P=T p` el ideal extendido en `T`. El anillo localizado `T_P` posee una base de módulo formada por elementos linealmente independientes respecto del anillo principal `o_p`; al mismo tiempo, `T_P` es un orden finito sobre `o_p` en el cuerpo de extensión `K` del cuerpo de cocientes `Ω` de `o_p`. Así, el teorema del discriminante vale para `T_P` respecto de `o_p`.

## Slice R10: Modules Over a Field

Source anchor: German baseline `L16804-L16840`.

Rows covered: `term-fr-0005`, `term-fr-0006`, `term-fr-0009`, `term-es-0006`, `term-es-0008`, `term-es-0011`; supports representation rows.

Evidence note: exact German anchor `Körper`; local shelf evidence supports French `corps` 2019 hits / 64 files and Spanish `cuerpo` 1452 hits / 41 files. Spanish `campo` is not used here.

Unresolved flags: none.

French draft:

**Modules relativement à un corps. Systèmes hypercomplexes.** Un exemple presque trivial de groupes à opérateurs complètement réductibles est donné par les modules à base finie relativement à un corps, non nécessairement commutatif.

Soit `G` un `K`-module à droite, et soit l'élément unité `e` de `K` en même temps opérateur unité: `ae=a` pour `a` dans `G`. Tout sous-module `aK` déduit d'un élément `a` est simple, c'est-à-dire égal au module déduit de n'importe lequel de ses éléments non nuls. Si `H` est un sous-module déduit de certains éléments, et si `a` n'appartient pas à `H`, alors `H∩aK=E`, donc `H+aK` est une somme directe. En partant d'un élément de base `a_1`, on peut donc adjoindre successivement de nouveaux éléments de base `a_2,a_3,...`, et l'on obtient
`G=a_1K+a_2K+\cdots+a_nK`
comme somme directe. Ainsi `G` est complètement réductible.

Le nombre `n`, longueur de la série de composition, s'appelle le rang de `G` relativement à `K`. La base `a_1,...,a_n` est linéairement indépendante, en raison de l'unicité de la représentation des éléments de `G` et parce que `e` a été supposé opérateur unité.

Tout sous-module `H` est un facteur direct:
`G=H+R=(h_1K+\cdots+h_sK)+(r_1K+\cdots+r_{n-s}K)`.
Autrement dit, toute base linéairement indépendante de `H` peut être complétée en une base linéairement indépendante de `G`.

Spanish draft:

**Módulos respecto de un cuerpo. Sistemas hipercomplejos.** Un ejemplo casi trivial de grupos con operadores completamente reducibles lo dan los módulos con base finita respecto de un cuerpo, no necesariamente conmutativo.

Sea `G` un `K`-módulo derecho, y sea el elemento unidad `e` de `K` también operador unidad: `ae=a` para `a` en `G`. Todo submódulo `aK` derivado de un elemento `a` es simple, es decir, igual al módulo derivado de cualquiera de sus elementos no nulos. Si `H` es un submódulo derivado de ciertos elementos, y si `a` no pertenece a `H`, entonces `H∩aK=E`, de modo que `H+aK` es una suma directa. Partiendo de un elemento de base `a_1`, se pueden ir añadiendo nuevos elementos de base `a_2,a_3,...`, y se obtiene
`G=a_1K+a_2K+\cdots+a_nK`
como suma directa. Así, `G` es completamente reducible.

El número `n`, longitud de la serie de composición, se llama rango de `G` respecto de `K`. La base `a_1,...,a_n` es linealmente independiente, por la unicidad de la representación de los elementos de `G` y porque `e` se supuso operador unidad.

Todo submódulo `H` es un sumando directo:
`G=H+R=(h_1K+\cdots+h_sK)+(r_1K+\cdots+r_{n-s}K)`.
En otras palabras, toda base linealmente independiente de `H` puede completarse a una base linealmente independiente de `G`.

## Slice R11: Representations and Representation Modules

Source anchor: German baseline `L17591-L17655`.

Rows covered: `term-fr-0017`, `term-es-0019`; supports `term-es-0020` through adjacent representation context.

Evidence note: exact German anchors `Darstellung`, `Darstellungsmodul`, `Homomorphie`; local shelf evidence supports French `représentation` 176 hits / 43 files and Spanish `representación` 188 hits / 14 files.

Unresolved flags: `Doppelmodul` rendered as `bimodule` / `bimódulo` with `module double` / `módulo doble` on first mention.

French draft:

**Représentations et modules de représentation.** Soit `o` un anneau, et soit `K` un anneau avec élément unité. Dans les applications ultérieures, `K` est toujours un corps.

Une représentation de degré `n` de `o` dans `K` est une homomorphie `o∼D`, où `D` est un anneau de matrices de degré `n` à coefficients dans `K`.

Par module de représentation de `o` relativement à `K`, on entend un bimodule, ou module double, `M`, qui est module à gauche sur `o` et module à droite sur `K`:
`oM⊂M`, `MK⊂M`;
qui est en outre somme directe d'un nombre fini de `K`-modules monogènes,
`M=x_1K+\cdots+x_nK`;
et où l'élément unité de `K` est opérateur unité.

Tout module de représentation conduit à une représentation. Si `c` appartient à `o` et si
`cx_k=\sum_i x_iγ_{ik}`,
ou encore
`c(x_1,\ldots,x_n)=(x_1,\ldots,x_n)C`,
alors les matrices `C` forment une représentation de `c`. En effet, l'addition se traduit par l'addition des matrices, et le produit `bc` se traduit par le produit matriciel `BC`.

Réciproquement, toute représentation `D` de `o` appartient à un module de représentation, relativement à une base déterminée de ce module. On prend pour `M` l'ensemble des formes linéaires formelles
`y=\sum_i x_iα_i`.
Alors `M` est un `K`-module à droite. Si à l'élément `c` correspond la matrice `C=(γ_{ik})`, on définit
`cx_k=\sum_i x_iγ_{ik}`,
et cette règle donne l'action de `c` sur toute forme linéaire de `M`.

Spanish draft:

**Representaciones y módulos de representación.** Sea `o` un anillo, y sea `K` un anillo con elemento unidad. En las aplicaciones posteriores, `K` será siempre un cuerpo.

Una representación de grado `n` de `o` en `K` es una homomorfía `o∼D`, donde `D` es un anillo de matrices de grado `n` con elementos en `K`.

Por módulo de representación de `o` respecto de `K` se entiende un bimódulo, o módulo doble, `M`, que es módulo izquierdo sobre `o` y módulo derecho sobre `K`:
`oM⊂M`, `MK⊂M`;
que además es suma directa de un número finito de `K`-módulos monógenos,
`M=x_1K+\cdots+x_nK`;
y en el que el elemento unidad de `K` es operador unidad.

Todo módulo de representación conduce a una representación. Si `c` pertenece a `o` y
`cx_k=\sum_i x_iγ_{ik}`,
o bien
`c(x_1,\ldots,x_n)=(x_1,\ldots,x_n)C`,
entonces las matrices `C` forman una representación de `c`. En efecto, la suma se traduce en la suma de matrices, y el producto `bc` se traduce en el producto matricial `BC`.

Recíprocamente, toda representación `D` de `o` pertenece a un módulo de representación, con respecto a una base determinada de este módulo. Se toma para `M` el conjunto de las formas lineales formales
`y=\sum_i x_iα_i`.
Entonces `M` es un `K`-módulo derecho. Si al elemento `c` le corresponde la matriz `C=(γ_{ik})`, se define
`cx_k=\sum_i x_iγ_{ik}`,
y esta regla da la acción de `c` sobre toda forma lineal de `M`.

## Slice R12: Reducible Representations and Quotient Modules

Source anchor: German baseline `L17714-L17745`.

Rows covered: `term-fr-0016`, `term-fr-0017`, `term-es-0018`, `term-es-0019`, `term-es-0020`; supports module/submodule rows.

Evidence note: exact German anchors `reduzible Darstellungen`, `Untermodul`, `Darstellungsmodul`, `M/U`. Local shelf evidence supports Spanish `representación irreducible` 3 hits / 2 files; French exact active row is `représentation`, not `représentation irréductible`.

Unresolved flags: source slice is about reducible representations; irreducible representation row is covered by contrast and by `irreduzible Darstellungsklasse` in Slice R14.

French draft:

**Représentations réductibles.** Si `U` est un sous-module du module de représentation `M`, et s'il est possible de choisir pour `M` une base composée d'une base `z_1,...,z_t` de `U`, complétée par `y_1,...,y_r`, donc
`M=y_1K+\cdots+y_rK+z_1K+\cdots+z_tK`,
alors les représentations ont la forme
`C=((R,0),(S,T))`.
Les matrices `T`, prises seules, forment une représentation de degré `t`, engendrée par `U`; les matrices `R` forment une représentation de degré `r`, engendrée par le quotient `M/U`.

En effet,
`(cy_1,\ldots,cy_r,cz_1,\ldots,cz_t)=(y_1,\ldots,y_r,z_1,\ldots,z_t)C`.
Comme les `cz_i`, étant des éléments de `U`, s'expriment au moyen des seuls `z_i`, le bloc supérieur droit de `C` est nul. Si l'on nomme les autres blocs `R,S,T` dans cet ordre, alors
`(cz_1,\ldots,cz_t)=(z_1,\ldots,z_t)T`,
et les `T` forment donc la représentation donnée par `U`. De plus,
`(cy_1,\ldots,cy_r)≡(y_1,\ldots,y_r)R mod U`,
tandis que les `y_i` forment une base linéairement indépendante modulo `U`. Ainsi les `R` forment une représentation engendrée par `M/U`.

Réciproquement, si une représentation réductible de cette forme est donnée, avec `R` et `T` carrées, alors dans le module de représentation correspondant les produits de tout `c` avec les derniers éléments de base `z_1,...,z_t` s'expriment au moyen de ces éléments seuls; donc `U=(z_1,...,z_t)` est un sous-module.

Spanish draft:

**Representaciones reducibles.** Si `U` es un submódulo del módulo de representación `M`, y si es posible elegir para `M` una base formada por una base `z_1,...,z_t` de `U`, completada por `y_1,...,y_r`, es decir,
`M=y_1K+\cdots+y_rK+z_1K+\cdots+z_tK`,
entonces las representaciones tienen la forma
`C=((R,0),(S,T))`.
Las matrices `T`, por sí solas, forman una representación de grado `t`, generada por `U`; las matrices `R` forman una representación de grado `r`, generada por el cociente `M/U`.

En efecto,
`(cy_1,\ldots,cy_r,cz_1,\ldots,cz_t)=(y_1,\ldots,y_r,z_1,\ldots,z_t)C`.
Como los `cz_i`, por ser elementos de `U`, se expresan solo mediante los `z_i`, el bloque superior derecho de `C` es cero. Si se llaman `R,S,T` los demás bloques en ese orden, entonces
`(cz_1,\ldots,cz_t)=(z_1,\ldots,z_t)T`,
y los `T` forman por tanto la representación dada por `U`. Además,
`(cy_1,\ldots,cy_r)≡(y_1,\ldots,y_r)R mod U`,
mientras que los `y_i` forman una base linealmente independiente módulo `U`. Así, los `R` forman una representación generada por `M/U`.

Recíprocamente, si se da una representación reducible de esta forma, con `R` y `T` cuadradas, entonces en el módulo de representación correspondiente los productos de todo `c` con los últimos elementos de base `z_1,...,z_t` se expresan solo mediante esos elementos; por tanto `U=(z_1,...,z_t)` es un submódulo.

## Slice R13: Complete Reducibility / Semisimple Register

Source anchors: German baseline `L15846-L15850`, `L16270-L16274`, `L19361-L19366`.

Rows covered: `term-es-0021`, `term-es-0020`, `term-es-0019`; supports French representation/irreducible rows.

Evidence note: German source uses `vollständig reduzibel` and `halbeinfach`; Spanish shelf supports `semisimple` 5 hits / 1 file. The artifact treats `semisimple` as a modern Spanish register equivalent in the appropriate algebra/representation contexts, not as a literal rendering of every `vollständig reduzibel`.

Unresolved flags: `semisimple` is Spanish manual-source-review row; keep `semisimple` as draft only and require specialist review before promotion.

French draft:

Un anneau `R` est dit complètement réductible lorsque, dans la représentation de son idéal nul comme produit, toutes les composantes primaires deviennent des idéaux premiers; ce qui revient, dans le contexte indiqué, à dire que `R` se représente comme somme directe d'un nombre fini de corps. Un anneau complètement réductible est dit de première espèce si tous ses idéaux premiers sont de première espèce; sinon il est de seconde espèce.

Pour un système hypercomplexe `S` relativement à un corps `P_0`, une représentation `Γ` dans `P` est un système de matrices à coefficients dans `P` qui est image homomorphe de `S` et qui envoie les éléments de `P_0` sur des matrices diagonales `p_0E`. Les notions de représentations réductibles, irréductibles, complètement réductibles et absolument irréductibles sont alors prises dans leur sens usuel et étendues aux classes de représentations.

Si `S` est hypercomplexe avec élément unité, avec `P` comme domaine de coefficients, et si `A` est un corps de centre `P`, alors `S` possède autant de classes distinctes de représentations réciproques irréductibles de `S` dans `A` qu'il y a de classes d'idéaux à droite simples dans l'anneau de classes résiduelles de `S_A` modulo son radical. Si `S` est un système simple, il possède exactement une classe de représentation réciproque irréductible et une classe de représentation directe irréductible dans `A`.

Spanish draft:

Un anillo `R` se llama completamente reducible cuando, en la representación de su ideal cero como producto, todas las componentes primarias se vuelven ideales primos; esto equivale, en el contexto indicado, a que `R` pueda representarse como suma directa de un número finito de cuerpos. Un anillo completamente reducible se llama de primera especie si todos sus ideales primos son de primera especie; en caso contrario, de segunda especie.

Para un sistema hipercomplejo `S` respecto de un cuerpo `P_0`, una representación `Γ` en `P` es un sistema de matrices con elementos en `P` que es imagen homomorfa de `S` y que envía los elementos de `P_0` a matrices diagonales `p_0E`. Las nociones de representaciones reducibles, irreducibles, completamente reducibles y absolutamente irreducibles se toman entonces en su sentido usual y se extienden a las clases de representaciones. En el registro moderno, los contextos de completa reducibilidad de sistemas sin radical se conectan con el uso de `semisimple`, pero este rótulo queda como borrador no revisado.

Si `S` es hipercomplejo con elemento unidad, con `P` como dominio de coeficientes, y si `A` es un cuerpo con centro `P`, entonces `S` posee tantas clases distintas de representaciones recíprocas irreducibles de `S` en `A` como clases de ideales derechos simples hay en el anillo de clases residuales de `S_A` módulo su radical. Si `S` es un sistema simple, posee exactamente una clase de representación recíproca irreducible y una clase de representación directa irreducible en `A`.

## Slice R14: Automorphisms, Homomorphisms, Modules, Bimodules

Source anchors: German baseline `L19024-L19110`.

Rows covered: `term-fr-0010`, `term-fr-0012`, `term-fr-0013`, `term-es-0012`, `term-es-0014`, `term-es-0015`; supports module rows.

Evidence note: exact German anchors include `Automorphismenring`, `Homomorphismen`, `isomorph`, `Moduln`, `Doppelmoduln`. Local shelf evidence supports French `automorphisme` 137 hits / 22 files and Spanish `automorfismo` 74 hits / 10 files.

Unresolved flags: exact German baseline has no `Endomorphismus`; endomorphism rows are therefore listed in the blocker ledger rather than forced through this automorphism slice.

French draft:

**Automorphismes, modules et bimodules.** La théorie des représentations fondée sur les modules de représentation repose sur la théorie de l'anneau des automorphismes des groupes abéliens, avec ou sans opérateurs. Les raisonnements implicitement utilisés, c'est-à-dire les relations entre application et lois de calcul, sont formulés ici une fois pour toutes afin d'éviter les répétitions.

Soit d'abord `G` un groupe sans opérateurs, et soit `A` son domaine absolu d'automorphismes, c'est-à-dire le système de tous les homomorphismes de `G` dans lui-même. `A` est fermé multiplicativement, car le produit `στ` est défini par
`g(στ)=(gσ)τ`,
et satisfait manifestement la loi associative.

Un groupe `G` devient un groupe avec opérateurs lorsqu'un ensemble de symboles `O,H,...` est donné, de sorte que les liaisons `gO,gH,...` produisent des éléments déterminés de `G` et engendrent des homomorphismes de `G` dans lui-même. Si le domaine d'opérateurs `B` est fermé multiplicativement, l'application de `B` sur la partie correspondante du domaine d'automorphismes est multiplicativement homomorphe si et seulement si la relation associative
`g(OH)=(gO)H`
est satisfaite. Pour des opérateurs écrits à gauche, on obtient de façon correspondante un homomorphisme réciproque.

Si `G` est un groupe avec opérateurs, l'homomorphie d'opérateurs est définie par
`(gO)σ=(gσ)O`,
ou, pour les opérateurs à gauche, par
`(Og)σ=O(gσ)`.
Il en résulte que deux domaines d'opérateurs produisent mutuellement des automorphismes l'un de l'autre exactement lorsque leurs actions sont commutativement liées, ou lorsque vaut la loi associative traversante.

Un module à droite `M` sur un anneau `R` est un groupe abélien additif dont les éléments de `R` sont des opérateurs à droite, et où, outre la relation associative, les relations distributives
`(g+h)ρ=gρ+hρ` et `g(ρ+σ)=gρ+gσ`
sont satisfaites. La définition correspondante vaut pour les modules à gauche.

Il faut distinguer deux sortes de bimodules. Des modules à droite sur deux anneaux `R` et `S` sont des bimodules si, en plus des liaisons valables séparément pour `R` et `S`, on a `(mρ)σ=(mσ)ρ`. Des modules à gauche sur `R` et à droite sur `S` sont des bimodules si s'ajoute la loi associative traversante `ρ(mσ)=(ρm)σ`.

Spanish draft:

**Automorfismos, módulos y bimódulos.** La teoría de representaciones basada en los módulos de representación descansa en la teoría del anillo de automorfismos de los grupos abelianos, con o sin operadores. Los razonamientos utilizados implícitamente, es decir, las relaciones entre aplicación y leyes de cálculo, se formulan aquí de una vez para evitar repeticiones.

Sea primero `G` un grupo sin operadores, y sea `A` su dominio absoluto de automorfismos, es decir, el sistema de todos los homomorfismos de `G` en sí mismo. `A` es cerrado multiplicativamente, pues el producto `στ` se define por
`g(στ)=(gσ)τ`,
y satisface manifiestamente la ley asociativa.

Un grupo `G` se convierte en un grupo con operadores cuando se da un conjunto de símbolos `O,H,...`, de modo que las operaciones `gO,gH,...` produzcan elementos determinados de `G` y generen homomorfismos de `G` en sí mismo. Si el dominio de operadores `B` es cerrado multiplicativamente, la aplicación de `B` sobre la parte correspondiente del dominio de automorfismos es multiplicativamente homomorfa si y solo si se satisface la relación asociativa
`g(OH)=(gO)H`.
Para operadores escritos a la izquierda se obtiene, correspondientemente, un homomorfismo recíproco.

Si `G` es un grupo con operadores, la homomorfía de operadores se define por
`(gO)σ=(gσ)O`,
o, para operadores a la izquierda, por
`(Og)σ=O(gσ)`.
De aquí se sigue que dos dominios de operadores producen mutuamente automorfismos uno del otro exactamente cuando sus acciones están conmutativamente vinculadas, o cuando vale la ley asociativa transitiva.

Un módulo derecho `M` sobre un anillo `R` es un grupo abeliano aditivo cuyos elementos de `R` son operadores derechos, y en el que, además de la relación asociativa, se satisfacen las relaciones distributivas
`(g+h)ρ=gρ+hρ` y `g(ρ+σ)=gρ+gσ`.
La definición correspondiente vale para módulos izquierdos.

Hay que distinguir dos clases de bimódulos. Los módulos derechos sobre dos anillos `R` y `S` son bimódulos si, además de las operaciones válidas por separado para `R` y `S`, se tiene `(mρ)σ=(mσ)ρ`. Los módulos izquierdos sobre `R` y derechos sobre `S` son bimódulos si se añade la ley asociativa transitiva `ρ(mσ)=(ρm)σ`.

## Exact Blocker Ledger

These rows have valid draft terminology evidence in the Romance shelf sidecar but no responsible exact German corpus slice in the current baseline. They are not silently inserted into translated prose.

- `term-fr-0008` / `term-es-0010`, tensor product: no `Tensorprodukt` or equivalent exact tensor-product source hit found in the German baseline. Romance shelf evidence supports French `produit tensoriel` 93 hits / 20 files and Spanish `producto tensorial` 3 hits / 3 files. Status: terminology sidecar only until a canon German source slice is found.
- `term-fr-0011` / `term-es-0013`, endomorphism: no exact `Endomorphismus` source hit found in the German baseline. Automorphism/homomorphism slices exist and are translated, but they must not be used to claim an endomorphism corpus translation. Romance shelf evidence supports French `endomorphisme` 85 hits / 20 files and Spanish `endomorfismo` 20 hits / 9 files. Status: terminology sidecar only until a canon German source slice is found.
- `term-fr-0020` / `term-es-0024`, maximal ideal: no exact `Maximalideal` / `maximales Ideal` source hit found in the German baseline. The baseline contains phrases such as maximal nilpotent ideal and maximal order, which are not the same concept and were not translated as maximal ideal. Romance shelf evidence supports French `idéal maximal` 122 hits / 18 files and Spanish `ideal maximal` 45 hits / 13 files. Status: terminology sidecar only until a canon German source slice is found.
- `term-fr-0003`, Hilbert basis: German Hilbert module-basis theorem slices exist and are translated, but the validated French shelf has 0 exact `base de Hilbert` hits. Status: translated as theorem context (`théorème de Hilbert sur la base de modules` / `théorème de la base de Hilbert`) with French evidence gap flagged for review.

## Coverage Statement

All 46 active Romance rows are accounted for in this draft artifact: 40 rows are covered by translated German source slices; 6 row instances are covered by exact blocker ledger entries rather than forced corpus prose. Some translated rows still carry evidence flags, especially French `base de Hilbert`, German `Ringbereich`, localization via `Quotientenring`, and Spanish `semisimple`. No reviewer packet population, promotion, approval, or native-review claim was performed.
