# ISV full-corpus lexicon insertion pass — v2 (ChatGPT)
Generated 2026-07-04. This is a mechanical corpus-coverage pass over the Interslavic Latin TeX translation feed. It is an internal consistency / insertion artifact, not a language-family witness artifact.
## Scope and method
- Source: `Slavic_LaTeX_ProMode_Feed_20260704.zip`.
- Translation files selected: **222** v001 Latin TeX files, excluding working/intermediate chunks.
- Tokenizer: Unicode word tokens after TeX-command/math stripping; diacritic-safe for Latin Slavic text.
- Known coverage set: current interlingual marker table, Interslavic concept ledger, Slavic term dataset, retrofit ledger, weighted score rows, and a small explicit proof/function stoplist.
- Boundary: exact/stem coverage only. A covered token is not certified; an uncovered token is not necessarily missing, because inflectional families are still only partly modeled.

## Headline numbers
- **selected_latin_translation_files**: 222
- **total_word_tokens**: 121928
- **unique_word_types**: 11003
- **known_token_entries**: 3631
- **known_stem_entries**: 4576
- **covered_tokens**: 96227
- **covered_types**: 5623
- **coverage_token_pct**: 78.92
- **coverage_type_pct**: 51.1
- **uncovered_tokens**: 25701
- **uncovered_types**: 5380

## Classification counts
- low_frequency_backlog: 4963
- stem_known: 4228
- exact_known: 1253
- short_function_or_artifact: 192
- proof_or_general_register_candidate: 143
- proof_grammar_known_stem: 142
- math_insert_candidate: 67
- proof_grammar_insert_candidate: 12
- artifact_residue: 3

## Top uncovered queue by class

### proof_or_general_register_candidate
`togda` (1207), `nehaj` (489), `važi` (243), `osoblivo` (177), `poneže` (171), `znovu` (169), `teper` (161), `jego` (145), `pokazuje` (144), `rędov` (123), `jeden` (106), `dobiva` (106), `imenno` (102), `ješče` (98), `točno` (94), `mora` (92), `naleži` (92), `teda` (87), `kromě` (79), `napr` (75), `nazyvaje` (74), `vodi` (73), `tvori` (71), `pokazati` (69), `trěba` (67)

### proof_grammar_insert_candidate
`poněže` (172), `smatrjati` (37), `naziva` (8), `smatrjajut` (5)

### math_insert_candidate
`bazoju` (25), `děli` (23), `bazě` (13), `transformujut` (9), `gordan` (7), `dělo` (6), `děla` (6), `permutacije` (6), `bazoj` (5), `gordana` (5), `dělu` (5), `reducirano` (4)

### low_frequency_backlog
`nazyvajut` (19), `morajut` (19), `toliko` (19), `koliko` (19), `samu` (19), `opreděljenje` (19), `imamo` (19), `několiko` (19), `nove` (19), `sadrži` (19), `plati` (19), `gore` (19), `davajut` (19), `metody` (19), `analogno` (19), `rędah` (19), `pytanja` (19), `byly` (19), `prvi` (19), `razumějemo` (18), `obće` (18), `sigurno` (18), `legko` (18), `redu` (18), `rěšenje` (18)

## Next insertion loop
1. Promote high-frequency `proof_grammar_insert_candidate` and `proof_or_general_register_candidate` rows into a proof-prose marker ledger, with English gloss and ISV lemma/stem.
2. Promote high-frequency `math_insert_candidate` rows into the concept ledger only when a source-side concept or existing glossary row is identified.
3. Expand inflectional/stem rules from accepted rows, then re-run this same measurement.
4. Keep generated TeX corpus evidence separate from language-family witnesses; this pass measures internal coverage only.
