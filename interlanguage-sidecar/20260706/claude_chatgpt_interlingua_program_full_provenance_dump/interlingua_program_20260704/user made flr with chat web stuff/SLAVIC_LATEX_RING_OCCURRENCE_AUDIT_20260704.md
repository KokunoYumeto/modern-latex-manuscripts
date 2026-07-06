# Slavic LaTeX ring-term occurrence audit — 2026-07-04

Input: `Slavic_LaTeX_ProMode_Feed_20260704.zip`.

Boundary: this is a **TeX-feed occurrence audit**. It supports internal-consistency and corpus-pressure claims about the generated Slavic/Interslavic corpus. It does **not** turn Ukrainian/Russian generated translation files into independent language-family witnesses, and it does **not** create West/South Slavic witness status.

## Method

- Read `00_manifest/selected_slavic_tex_manifest.csv`.
- Restricted the main count to files whose package path contains `/translations/`.
- Deduplicated exact content by `(category, sha256)` within each category.
- Counted conservative ring-family stems and competitor stems.
- Did not modify or promote any term.

Package counts from manifest:

| Category | TeX files | Translation files |
|---|---:|---:|
| Interslavic Cyrillic | 429 | 245 |
| Interslavic Latin | 448 | 265 |
| Ukrainian | 582 | 265 |
| Russian | 453 | 265 |

## Headline findings

1. The internal Interslavic corpus pressure for `kolco` is real and large: 1059 Latin-script `kolc*` occurrences across 125 deduplicated translation files, and 983 Cyrillic `колц*` occurrences across 111 deduplicated translation files.

2. The Interslavic corpus is **not completely uniform**: Paper 25 already contains `prsten` twice in Latin and `прстен` twice in Cyrillic. This should be added to the ring review packet as an internal exception / possible doublet trace, not ignored.

3. The secondary Ukrainian/Russian translation files show the expected East-Slavic cognate pressure: 1025 Ukrainian `кільц*` occurrences and 1029 Russian `кольц*` occurrences in the translation layer.

4. No `okruh*`, `pierśc*`, or `kolobar*` occurrences were found in the Interslavic TeX feed under the translation-file/deduplicated pass. Those remain W/S native-shelf evidence, not internal Interslavic corpus forms.

## Count table

| Pattern | Category | Occurrences | Files | Top forms |
|---|---|---:|---:|---|
| `kolc*` | ISV Latin | 1059 | 125 | `kolco` 399, `kolca` 258, `kolcu` 106, `kolc` 76, `podkolco` 39, `kolcom` 27, `podkolca` 23, `kolcah` 17 |
| `колц*` | ISV Cyrillic | 983 | 111 | `колцо` 357, `колца` 235, `колцу` 105, `колц` 69, `подколцо` 37, `колцом` 27, `подколца` 21, `колцах` 16 |
| `prsten*` | ISV Latin | 2 | 1 | `prsten` 2 |
| `прстен*` / `пръстен*` | ISV Cyrillic | 2 | 1 | `прстен` 2 |
| `кільц*` | Ukrainian translation | 1025 | 133 | `кільця` 317, `кільце` 315, `кільцем` 127, `кільці` 57, `підкільця` 36, `підкільце` 30, `кільцю` 25, `кільцева` 24 |
| `кольц*` | Russian translation | 1029 | 133 | `кольцо` 332, `кольца` 290, `кольцом` 97, `кольце` 68, `кольцу` 48, `подкольцо` 30, `подкольца` 30, `кольцевая` 24 |

## Interslavic `prsten` exception

The exception is in:

`Slavic_LaTeX_ProMode_Feed_20260704/02_primary_interslavic_latin/germanOut/translations/paper25/interslavic/v001/Noether_Paper25_Interslavic_v001.tex`

Line 68 contains the relevant passage. The sentence says that residue classes modulo a prime ideal form a ring without zero divisors and that, by forming quotients, that ring may be extended to a residue-class field.

Excerpt:

```text
\noindent II. \emph{Konstrukcija polja nuljev za prost ideal $\frakp$.} Ostatkove klasy po prostom idealu tvoret po definiciji prsten bez nuljevyh děliteljev, ktory imaje najmanje jeden element različny od nuljevogo elementa, skoro $\frakp$ različny jest od jediničnogo ideala; tvorjenjem kvocientov toj prsten može se zato razširiti do polja ostatkovyh klasov $(\frakR)$ ideala $\frakp$. Vsegda možno konstruovati razširjujoče polje $\frakR$ polja $P$, izomorfno k $(\frakR)$, ktoro stavaje poljem nuljev $\frakp$; t. j. $\frakR=P(\alpha_1,\ldots,\alpha_n)$, kde $\alpha_1,\ldots,\alpha_n$ označaje nulu $\frakp$. Pri tom $\frakR$ jest stepenja transcendencije $k$ $(0\leq k<n)$ vzhodno k $P$, zato obsahuje $k$ algebraično nezavisnyh vzhodno k $P$ elementov, medžu tym kako vsakih $(k+1)$ elementov stavajut algebraično zavisnymi vzhodno k $P$. Obratno, vsako polje nuljev stepenja transcendencije $k$, ležeče v razširjujočem polju polja $P$, jest izomorfno polju ostatkovyh klasov $(\frakR)$; polje nuljev stepenja transcendencije $k$ i polje ostatkovyh klasov sut zato abstraktno identične.
```

## Ring-family distribution by work, Interslavic translation files

| Work | Latin `kolc*` | Latin `prsten*` | Cyrillic `колц*` | Cyrillic `прстен*` |
|---|---:|---:|---:|---:|
| `endmatter/post44` | 156 | 0 | 78 | 0 |
| `endmatter/post45` | 1 | 0 | 1 | 0 |
| `endmatter/postbibliography` | 1 | 0 | 1 | 0 |
| `paper19` | 34 | 0 | 34 | 0 |
| `paper24` | 111 | 0 | 103 | 0 |
| `paper25` | 0 | 2 | 0 | 2 |
| `paper26` | 3 | 0 | 3 | 0 |
| `paper28` | 4 | 0 | 4 | 0 |
| `paper29` | 24 | 0 | 24 | 0 |
| `paper30` | 110 | 0 | 110 | 0 |
| `paper31` | 206 | 0 | 206 | 0 |
| `paper32` | 10 | 0 | 10 | 0 |
| `paper33` | 17 | 0 | 17 | 0 |
| `paper34` | 155 | 0 | 155 | 0 |
| `paper35` | 10 | 0 | 20 | 0 |
| `paper37` | 13 | 0 | 13 | 0 |
| `paper38` | 1 | 0 | 1 | 0 |
| `paper39` | 6 | 0 | 6 | 0 |
| `paper40` | 125 | 0 | 125 | 0 |
| `paper41` | 7 | 0 | 7 | 0 |
| `paper42` | 4 | 0 | 4 | 0 |
| `paper43` | 61 | 0 | 61 | 0 |

## Required patch to the ring review packet

Replace any wording that says the Interslavic corpus uses `kolco` uniformly with:

> The Interslavic corpus overwhelmingly uses `kolco`/`колцо` and its compounds, but the TeX feed contains a localized Paper 25 exception: `prsten`/`прстен` occurs twice in the context of residue-class rings. The review question is therefore not only `kolco` versus W/S alternatives, but whether the existing `prsten` trace is accidental inconsistency, acceptable local doublet, or evidence for a broader variant policy.

## Next bounded use of the Slavic LaTeX feed

1. Route the `prsten` exception into `RING_REVIEW_PACKET_v1`.
2. Produce a `KOLCO_FAMILY_INTERNAL_CONSISTENCY_LEDGER` with all `kolc*` compounds and file contexts.
3. Run the same occurrence audit for the second hard row: `quotient field`.
4. Use only internal-consistency status from this zip; keep branch-witness status tied to native W/S sources.
