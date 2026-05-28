# SGA 1--7 Translation Project: consolidated plan, standard style, and batch protocol

Generated in this session from the uploaded `SGA_TRANSLATION_SOURCE PACKAGE_1_7_COMPACT_FOR_WEB_UNDER_512MB_20260527_0916.zip` packet.

## 1. Current packet audit

The source package packet contains four distinct classes of material.

First, it contains baseline French sources for SGA 1--4. SGA 1 and SGA 2 have modern French TeX/PDF sources from arXiv; SGA 3 has modern reference PDFs but no raw French TeX found in the prior pass; SGA 4 has the Orgogozo/Laszlo French TeX source. The packet metadata states that no clear public English translation was found for SGA 4.

Second, it contains public English translation attempts for SGA 1--3. The most complete of these is the jcreinhold Markdown snapshot, described in its own README as an LLM-generated English translation of SGA 1, SGA 2, and SGA 3. Those translations were converted in this working draft section into standalone LaTeX files, without mathematical proofreading and without claiming final editorial status.

Third, it contains partial public SGA 1 material from the jmoellermath repository and partial SGA 1/SGA 6 material from the thosgood repository. These should be used as secondary comparison material, not as the project baseline, because the source package status file says they are partial.

Fourth, it contains current working LaTeX for SGA 5, SGA 6, SGA 7-I, and SGA 7-II, both as four combined files and as page-sliced files. The source package packet describes these as working machine/web-session outputs, not as proofed editions. The page-sliced files are the better working substrate because the combined files contain repeated/conflicting preambles from concatenation.

## 2. Coverage decision

The immediate editorial path is:

1. Preserve and normalize the existing SGA 1--3 English translations into LaTeX as provisional drafts.
2. Treat SGA 4 as the earliest genuinely missing English translation and begin there from the Orgogozo/Laszlo TeX source.
3. Run SGA 5--7 in parallel from the page-sliced TeX packet, translating in 20--50 page units when the source is clean, and in shorter theorem-bounded units when OCR or macro damage requires repair.
4. Keep every translation batch in compilable, standalone LaTeX, with the original SGA volume, exposé, source section range, and batch status in comments at the top.

The first new translation batch therefore begins at SGA 4, Exposé I, because SGA 1--3 already have provisional English material and SGA 4 does not. A separate SGA 5 opening translation is included because SGA 5--7 are the newly available TeX target corpus.

## 3. Standard translation register

The register is modern mathematical English with SGA structure preserved. The translation should not sound archaic, but it should not erase the formal architecture of the seminar. Preserve the original numbering of exposés, sections, propositions, definitions, lemmas, corollaries, equations, footnotes, and page-origin markers when they are present.

Use `Exposé` as the structural unit, not `Chapter`, because it is a canonical SGA reference form. In running prose, `exposé` may be translated as `lecture` only when the word is not acting as a formal label.

Use `scheme` for `préschéma` except where the historical distinction is itself under discussion. If a section depends on the original EGA convention that `scheme` means a separated prescheme, add a editorial note or keep `prescheme` locally. In SGA 4 and SGA 5 foundations, this policy avoids burdening the reader with obsolete terminology while preserving precision where necessary.

Use American mathematical spelling consistently: `fiber`, `fibered`, `neighbor`, `analyze`; but keep established French-derived terms with accents where standard, e.g. `étale`.

Do not modernize theorem content by silently replacing hypotheses with stronger or weaker modern variants. Modernization is linguistic and notational, not mathematical. Any genuinely modern reformulation should be placed in an editorial note or a separate recasting project, not in the faithful translation text.

## 4. Core terminology

| French | Standard English |
|---|---|
| faisceau | sheaf |
| préfaisceau | presheaf |
| faisceau abélien | sheaf of abelian groups / abelian sheaf, according to context |
| faisceau constructible | constructible sheaf |
| faisceau constant tordu | locally constant constructible sheaf, when that is the intended Deligne terminology; otherwise twisted constant sheaf |
| morphisme étale | étale morphism |
| revêtement étale | étale covering |
| morphisme lisse | smooth morphism |
| morphisme plat | flat morphism |
| morphisme propre | proper morphism |
| propreté cohomologique | cohomological properness |
| changement de base | base change |
| passage à la limite | passage to the limit; when categorical, passage to the inverse/direct limit |
| limite projective | inverse limit; retain `projective limit` in historical phrases if needed |
| limite inductive | direct limit / filtered colimit; choose by context |
| image directe | direct image / pushforward |
| image directe à supports propres | direct image with proper supports, `f_!` |
| foncteur fibre | fiber functor |
| catégorie fibrée | fibered category |
| descente | descent |
| torseur | torsor |
| schéma en groupes | group scheme |
| groupe de type multiplicatif | group of multiplicative type |
| groupe réductif | reductive group |
| donnée radicielle | root datum |
| immeuble | building |
| classe de cohomologie associée à un cycle | cycle class / cohomology class associated with a cycle |
| correspondance cohomologique | cohomological correspondence |
| terme local | local term |
| formule des traces | trace formula |
| formule de Lefschetz | Lefschetz formula |
| formule de Lefschetz-Verdier | Lefschetz--Verdier formula |
| dualisant | dualizing |
| complexe dualisant | dualizing complex |
| bidualité | biduality |
| pureté | purity |
| résolution des singularités | resolution of singularities |
| caractéristique résiduelle | residue characteristic |

## 5. LaTeX standard

Each translated unit should compile as standalone LaTeX and also be easy to include in a future master book. Use UTF-8 and modern packages only. Avoid copying the source preamble unless it is actually needed.

Recommended top matter:

```tex
% SGA TRANSLATION PROJECT
% Volume: SGA n
% Expose: ...
% Source: ...
% Range translated in this working draft section: ...
% Status: draft translation, not proofed against scan
```

Recommended theorem environments:

```tex
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{construction}[theorem]{Construction-Definition}
\newtheorem{remark}[theorem]{Remark}
```

The batch files created here use a simpler local variant when original numbering must be preserved exactly, e.g. `Definition 1.1` as a visible text label rather than relying on automatic counters.

## 6. QA protocol

Every translation batch should have four checks.

First, a range check: confirm volume, exposé, section range, source filename, and exact start/end anchors.

Second, a mathematical vocabulary check: verify all category-theoretic, cohomological, and scheme-theoretic terms against the shared glossary.

Third, a formula-preservation check: compare displayed formulae, arrows, indices, hypotheses, and numbering against the source. Do not translate inside math mode except for operator names that are textual in the original.

Fourth, a compile check: run LaTeX or at minimum a syntax pass. If full compilation is not run, mark the file `not compile-checked` in the worklog. The converted SGA 1--3 files are syntax-generated by Pandoc and are not proofed mathematical LaTeX.

## 7. Batch sequencing

working draft section created in this session contains:

- provisional LaTeX consolidation of the existing SGA 1--3 English Markdown translations;
- a new draft translation of SGA 4, Exposé I, opening through Proposition 1.4;
- a new draft translation of the SGA 5 volume introduction opening and exposé map.

