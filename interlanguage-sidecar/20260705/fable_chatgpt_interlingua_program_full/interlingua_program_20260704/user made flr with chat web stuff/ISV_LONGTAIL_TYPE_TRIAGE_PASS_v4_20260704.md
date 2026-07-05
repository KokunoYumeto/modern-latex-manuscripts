# ISV long-tail type triage — pass v4

2026-07-04. ChatGPT-side token/type long-tail pass over the top-1500 uncovered queue from the strict v3 backlog. This is classification and insertion-proposal work only. No term is promoted; generated/internal TeX has permitted-use weight 0.35.

## Summary

- Input surface types: **1500**
- Represented uncovered occurrences: **6412**
- Proposed insert/attach rows: **829**

### By classification

- inflection_or_variant_of_existing: 592 types / 2655 occurrences
- needs_context_review: 264 types / 1114 occurrences
- dictionary_known_uninserted: 231 types / 914 occurrences
- unresolved_inflection_like: 191 types / 732 occurrences
- tex_or_short_artifact: 66 types / 323 occurrences
- dictionary_function_or_register: 62 types / 271 occurrences
- proof_register_candidate: 52 types / 224 occurrences
- name_or_eponym: 22 types / 94 occurrences
- math_or_noether_candidate: 17 types / 70 occurrences
- source_or_bibliographic_residue: 3 types / 15 occurrences

### By recommended action

- attach_variant: 592 types / 2655 occurrences
- context_review: 455 types / 1846 occurrences
- insert_candidate_or_inflection: 231 types / 914 occurrences
- exclude_or_stop: 66 types / 323 occurrences
- stop_or_register_review: 62 types / 271 occurrences
- insert_internal_register: 52 types / 224 occurrences
- covered_by_eponym_or_bibliography_rule: 22 types / 94 occurrences
- insert_math_or_link_to_concept: 17 types / 70 occurrences
- exclude_source_residue: 3 types / 15 occurrences

## Highest-count rows

| token | count | class | action | note |
|---|---:|---|---|---|
| `musi` | 10 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group reg-morati (morati); match=exact_variant |
| `izhodet` | 10 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group starting-point (izhodišče); match=head_match_izhod |
| `asu` | 10 | tex_or_short_artifact | exclude_or_stop | TeX/math residue or too short to classify as lexicon without context |
| `bhu` | 10 | tex_or_short_artifact | exclude_or_stop | TeX/math residue or too short to classify as lexicon without context |
| `hensel` | 10 | name_or_eponym | covered_by_eponym_or_bibliography_rule | Name/eponym; not ordinary lexicon item unless used as term modifier |
| `dobyva` | 10 | proof_register_candidate | insert_internal_register | Corpus proof/register word; internal insertion only pending linguistic review |
| `hsu` | 10 | tex_or_short_artifact | exclude_or_stop | TeX/math residue or too short to classify as lexicon without context |
| `dt` | 10 | tex_or_short_artifact | exclude_or_stop | TeX/math residue or too short to classify as lexicon without context |
| `silny` | 10 | needs_context_review | context_review | No high-confidence classification from ledger/dictionary/root rules |
| `respektivno` | 10 | proof_register_candidate | insert_internal_register | Corpus proof/register word; internal insertion only pending linguistic review |
| `riemannovoj` | 10 | name_or_eponym | covered_by_eponym_or_bibliography_rule | Name/eponym; not ordinary lexicon item unless used as term modifier |
| `sovsěm` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group entirely (sovsěm); match=exact_variant |
| `mathematische` | 9 | source_or_bibliographic_residue | exclude_source_residue | German/English/bibliographic residue; do not promote into ISV lexicon |
| `doslovno` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group literally (doslovno); match=exact_variant |
| `nastupiti` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group reg-nastupati (nastupati); match=head_match_nastu |
| `javno` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group evidently-javno (javno); match=exact_variant |
| `beremo` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group we-take (brati); match=exact_variant |
| `prihodimo` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group arrives-prihoditi (prihoditi); match=head_match_priho |
| `ničto` | 9 | dictionary_function_or_register | stop_or_register_review | Community dictionary match (exact); POS=pron.indef.; decide stoplist vs register |
| `novih` | 9 | needs_context_review | context_review | No high-confidence classification from ledger/dictionary/root rules |
| `sumi` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group reg-suma (suma); match=exact_variant |
| `znanyh` | 9 | dictionary_known_uninserted | insert_candidate_or_inflection | Community dictionary match (head_znany); needs corpus-context class |
| `mimo` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group besides-mimo (mimo); match=exact_variant |
| `faktično` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group reg-fakt (fakt); match=head_match_fakt |
| `glasi` | 9 | proof_register_candidate | insert_internal_register | Corpus proof/register word; internal insertion only pending linguistic review |
| `opreděljenogo` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group well-defined (jednoznačno oprěděljeny); match=head_match_opred |
| `oběh` | 9 | needs_context_review | context_review | No high-confidence classification from ledger/dictionary/root rules |
| `nastupajuče` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group reg-nastupati (nastupati); match=head_match_nastu |
| `naležeči` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group reg-naležati (naležati); match=head_match_nalež |
| `někojim` | 9 | dictionary_function_or_register | stop_or_register_review | Community dictionary match (head_někoj); POS=pron.indef.; decide stoplist vs register |
| `več` | 9 | tex_or_short_artifact | exclude_or_stop | TeX/math residue or too short to classify as lexicon without context |
| `čime` | 9 | needs_context_review | context_review | No high-confidence classification from ledger/dictionary/root rules |
| `pregled` | 9 | needs_context_review | context_review | No high-confidence classification from ledger/dictionary/root rules |
| `sostaji` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group reg-sostojati (sostojati); match=exact_variant |
| `nekoliko` | 9 | needs_context_review | context_review | No high-confidence classification from ledger/dictionary/root rules |
| `dostignuti` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group attains (dostigati); match=head_match_dosti |
| `mogu` | 9 | needs_context_review | context_review | No high-confidence classification from ledger/dictionary/root rules |
| `vzęti` | 9 | dictionary_known_uninserted | insert_candidate_or_inflection | Community dictionary match (exact); needs corpus-context class |
| `transformujut` | 9 | dictionary_known_uninserted | insert_candidate_or_inflection | Community dictionary match (head_trans); needs corpus-context class |
| `něčto` | 9 | dictionary_known_uninserted | insert_candidate_or_inflection | Community dictionary match (exact); needs corpus-context class |
| `vsude` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group everywhere (vsude); match=exact_variant |
| `protivnosti` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group contrary (protivno); match=head_match_proti |
| `bukvami` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group letter-symbol (bukva); match=exact_variant |
| `stati` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group becomes (stati); match=exact_variant |
| `eksistenciju` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group exists-eksist (eksistovati); match=head_match_eksis |
| `izslědovanje` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group investigation (izslědovanje); match=exact_variant |
| `někojih` | 9 | dictionary_function_or_register | stop_or_register_review | Community dictionary match (head_někoj); POS=pron.indef.; decide stoplist vs register |
| `skupaj` | 9 | proof_register_candidate | insert_internal_register | Corpus proof/register word; internal insertion only pending linguistic review |
| `sovpadati` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group coincides (sovpada); match=head_match_sovpa |
| `suščestvuje` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group exists-eksist (eksistovati); match=head_match_sušče |
| `nastajut` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group reg-nastavati (nastavati); match=head_match_nasta |
| `realnyh` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group real (realny); match=head_match_realn |
| `nastal` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group reg-nastavati (nastavati); match=exact_variant |
| `obstajanje` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group reg-obstajati (obstajati); match=head_match_obsta |
| `podmodul` | 9 | math_or_noether_candidate | insert_math_or_link_to_concept | Mathematical/Noether/root-term candidate; source-side concept link needed before certification |
| `zaměnjeno` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group substitution (zaměna); match=head_match_zaměn |
| `znak` | 9 | dictionary_known_uninserted | insert_candidate_or_inflection | Community dictionary match (exact); needs corpus-context class |
| `prědpostavce` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group assumption-noun (prědpoloženje); match=head_match_prědp |
| `neizvěstne` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group unknown-quantity (neizvěstna); match=head_match_neizv |
| `odgovorno` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group corresponds (sootvětstvovati); match=head_match_odgov |
| `sostojí` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group reg-sostojati (sostojati); match=head_match_sosto |
| `umenšenje` | 9 | unresolved_inflection_like | context_review | Looks inflected but no current lemma match; context review needed |
| `opět` | 9 | needs_context_review | context_review | No high-confidence classification from ledger/dictionary/root rules |
| `diskontinuirne` | 9 | dictionary_known_uninserted | insert_candidate_or_inflection | Community dictionary match (head_disko); needs corpus-context class |
| `obščejše` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group generality (obščnost); match=head_match_obšče |
| `obstava` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group remain-ostati (ostati); match=exact_variant |
| `nerazlozime` | 9 | unresolved_inflection_like | context_review | Looks inflected but no current lemma match; context review needed |
| `varijablov` | 9 | needs_context_review | context_review | No high-confidence classification from ledger/dictionary/root rules |
| `integriranje` | 9 | dictionary_known_uninserted | insert_candidate_or_inflection | Community dictionary match (head_integ); needs corpus-context class |
| `osoblive` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group reg-osoblivo (osoblivo); match=head_match_osobl |
| `slućaju` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group case-instance (slučaj); match=head_match_sluća |
| `dohodi` | 9 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group arrives-dohoditi (dohoditi); match=exact_variant |
| `dodavanje` | 8 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group by-adding (dodanje); match=head_match_dodav |
| `izslědovanj` | 8 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group investigation (izslědovanje); match=head_match_izslě |
| `naše` | 8 | needs_context_review | context_review | No high-confidence classification from ledger/dictionary/root rules |
| `dostavajut` | 8 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group reg-dostati (dostati/dobyti); match=head_match_dosta |
| `njim` | 8 | needs_context_review | context_review | No high-confidence classification from ledger/dictionary/root rules |
| `obě` | 8 | tex_or_short_artifact | exclude_or_stop | TeX/math residue or too short to classify as lexicon without context |
| `recimo` | 8 | inflection_or_variant_of_existing | attach_variant | Attach to existing lexicon group say-for-instance (recimo); match=exact_variant |
| `tutom` | 8 | dictionary_function_or_register | stop_or_register_review | Community dictionary match (exact); POS=adv.; decide stoplist vs register |

## Proposed insertion/attachment front

| token | count | action | attach/lemma | en hint |
|---|---:|---|---|---|
| `musi` | 10 | attach_variant | `reg-morati` |  |
| `izhodet` | 10 | attach_variant | `starting-point` |  |
| `dobyva` | 10 | insert_internal_register | `dobyva` | conqueror |
| `respektivno` | 10 | insert_internal_register | `respektivno` | respect |
| `sovsěm` | 9 | attach_variant | `entirely` |  |
| `doslovno` | 9 | attach_variant | `literally` |  |
| `nastupiti` | 9 | attach_variant | `reg-nastupati` |  |
| `javno` | 9 | attach_variant | `evidently-javno` |  |
| `beremo` | 9 | attach_variant | `we-take` |  |
| `prihodimo` | 9 | attach_variant | `arrives-prihoditi` |  |
| `sumi` | 9 | attach_variant | `reg-suma` |  |
| `znanyh` | 9 | insert_candidate_or_inflection | `znanyh` | known |
| `mimo` | 9 | attach_variant | `besides-mimo` |  |
| `faktično` | 9 | attach_variant | `reg-fakt` |  |
| `glasi` | 9 | insert_internal_register | `glasi` |  |
| `opreděljenogo` | 9 | attach_variant | `well-defined` |  |
| `nastupajuče` | 9 | attach_variant | `reg-nastupati` |  |
| `naležeči` | 9 | attach_variant | `reg-naležati` |  |
| `sostaji` | 9 | attach_variant | `reg-sostojati` |  |
| `dostignuti` | 9 | attach_variant | `attains` |  |
| `vzęti` | 9 | insert_candidate_or_inflection | `vzęti` | take |
| `transformujut` | 9 | insert_candidate_or_inflection | `transformujut` | transcribe |
| `něčto` | 9 | insert_candidate_or_inflection | `něčto` | have a nose for sth. |
| `vsude` | 9 | attach_variant | `everywhere` |  |
| `protivnosti` | 9 | attach_variant | `contrary` |  |
| `bukvami` | 9 | attach_variant | `letter-symbol` |  |
| `stati` | 9 | attach_variant | `becomes` |  |
| `eksistenciju` | 9 | attach_variant | `exists-eksist` |  |
| `izslědovanje` | 9 | attach_variant | `investigation` |  |
| `skupaj` | 9 | insert_internal_register | `skupaj` |  |
| `sovpadati` | 9 | attach_variant | `coincides` |  |
| `suščestvuje` | 9 | attach_variant | `exists-eksist` |  |
| `nastajut` | 9 | attach_variant | `reg-nastavati` |  |
| `realnyh` | 9 | attach_variant | `real` |  |
| `nastal` | 9 | attach_variant | `reg-nastavati` |  |
| `obstajanje` | 9 | attach_variant | `reg-obstajati` |  |
| `podmodul` | 9 | insert_math_or_link_to_concept | `podmodul` | submarine, underwater |
| `zaměnjeno` | 9 | attach_variant | `substitution` |  |
| `znak` | 9 | insert_candidate_or_inflection | `znak` | diacritic |
| `prědpostavce` | 9 | attach_variant | `assumption-noun` |  |
| `neizvěstne` | 9 | attach_variant | `unknown-quantity` |  |
| `odgovorno` | 9 | attach_variant | `corresponds` |  |
| `sostojí` | 9 | attach_variant | `reg-sostojati` |  |
| `diskontinuirne` | 9 | insert_candidate_or_inflection | `diskontinuirne` | discography |
| `obščejše` | 9 | attach_variant | `generality` |  |
| `obstava` | 9 | attach_variant | `remain-ostati` |  |
| `integriranje` | 9 | insert_candidate_or_inflection | `integriranje` | integration |
| `osoblive` | 9 | attach_variant | `reg-osoblivo` |  |
| `slućaju` | 9 | attach_variant | `case-instance` |  |
| `dohodi` | 9 | attach_variant | `arrives-dohoditi` |  |
| `dodavanje` | 8 | attach_variant | `by-adding` |  |
| `izslědovanj` | 8 | attach_variant | `investigation` |  |
| `dostavajut` | 8 | attach_variant | `reg-dostati` |  |
| `recimo` | 8 | attach_variant | `say-for-instance` |  |
| `prvu` | 8 | attach_variant | `reg-prvy` |  |
| `vede` | 8 | insert_internal_register | `vede` |  |
| `podrobno` | 8 | attach_variant | `in-detail` |  |
| `právě` | 8 | attach_variant | `precisely-prave` |  |
| `tolkovanje` | 8 | attach_variant | `interpretation` |  |
| `poznany` | 8 | attach_variant | `reg-znati` |  |
| `vrěme` | 8 | insert_candidate_or_inflection | `vrěme` | only a question of time |
| `izvesti` | 8 | attach_variant | `carry-out` |  |
| `zaměnjajut` | 8 | attach_variant | `substitution` |  |
| `opreděljenoj` | 8 | attach_variant | `well-defined` |  |
| `obščem` | 8 | attach_variant | `generality` |  |
| `izražaje` | 8 | attach_variant | `expresses` |  |
| `nastupati` | 8 | attach_variant | `reg-nastupati` |  |
| `prirěditi` | 8 | attach_variant | `assign` |  |
| `prěvod` | 8 | insert_candidate_or_inflection | `prěvod` | translation |
| `napriměr` | 8 | attach_variant | `reg-napr.` |  |
| `opirajut` | 8 | attach_variant | `reg-opirati se` |  |
| `libovolno` | 8 | attach_variant | `arbitrary` |  |
| `pokazujut` | 8 | attach_variant | `reg-pokazati` |  |
| `namreč` | 8 | attach_variant | `reg-imenno` |  |
| `vvesti` | 8 | attach_variant | `introduce-vvesti` |  |
| `ležeče` | 8 | insert_internal_register | `ležeče` |  |
| `nastalo` | 8 | attach_variant | `reg-nastavati` |  |
| `literaturi` | 8 | insert_candidate_or_inflection | `literaturi` | letter (alphabet) |
| `najprostějši` | 8 | insert_candidate_or_inflection | `najprostějši` | easiest, simplest |
| `naměsto` | 8 | attach_variant | `reg-vměsto` |  |
| `rěšenj` | 8 | attach_variant | `reg-rěšenje` |  |
| `dodavanja` | 8 | attach_variant | `by-adding` |  |
| `odpovědajut` | 8 | attach_variant | `respectively-adv` |  |
| `izčezati` | 8 | attach_variant | `reg-izčezati` |  |
| `kongruencija` | 8 | insert_candidate_or_inflection | `kongruencija` | congress |
| `položi` | 8 | attach_variant | `set-put` |  |
| `porađajut` | 8 | attach_variant | `generates` |  |
| `anulovany` | 8 | insert_candidate_or_inflection | `anulovany` | cancel, nullify |
| `koordinat` | 8 | insert_candidate_or_inflection | `koordinat` | coordination |
| `vpolně` | 8 | attach_variant | `fully` |  |
| `familije` | 8 | attach_variant | `family` |  |
| `podtělu` | 8 | attach_variant | `subfield` |  |
| `pomocna` | 8 | attach_variant | `by-means-of` |  |
| `priradženje` | 8 | attach_variant | `assign` |  |
| `prěseka` | 8 | insert_candidate_or_inflection | `prěseka` | move (change residence) |
| `izberemo` | 7 | insert_internal_register | `izberemo` |  |
| `ležati` | 7 | attach_variant | `reg-ležati` |  |
| `pisati` | 7 | insert_candidate_or_inflection | `pisati` | rewrite |
| `prějdti` | 7 | attach_variant | `pass-over` |  |
| `paragrafov` | 7 | attach_variant | `section-paragraf` |  |
| `način` | 7 | insert_candidate_or_inflection | `način` | begin (intr.), start (intr.) |
| `protivnom` | 7 | attach_variant | `contrary` |  |
| `ekvivalent` | 7 | attach_variant | `reg-ekvivalentny` |  |
| `ukazuje` | 7 | attach_variant | `point-out` |  |
| `viděti` | 7 | insert_internal_register | `viděti` | see |
| `někomu` | 7 | insert_candidate_or_inflection | `někomu` | strike fear into somebody, put somebody in fear |
| `sposob` | 7 | insert_candidate_or_inflection | `sposob` | manner, way, method |
| `opreděljenja` | 7 | attach_variant | `well-defined` |  |
| `poznana` | 7 | attach_variant | `reg-znati` |  |
| `izčerpavajut` | 7 | attach_variant | `exhausts` |  |
| `procedura` | 7 | insert_candidate_or_inflection | `procedura` | procedure |
| `dostajut` | 7 | attach_variant | `reg-dostati` |  |
| `postavjenje` | 7 | attach_variant | `set-put` |  |
| `opreděljeny` | 7 | attach_variant | `well-defined` |  |
| `agregat` | 7 | insert_candidate_or_inflection | `agregat` | aggregate |
| `prědhodnogo` | 7 | attach_variant | `preceding` |  |
| `znajemo` | 7 | insert_candidate_or_inflection | `znajemo` | acquaintance (person) |
| `povezane` | 7 | attach_variant | `connected` |  |
| `udovletvorjajut` | 7 | attach_variant | `satisfies` |  |
| `naležeča` | 7 | attach_variant | `reg-naležati` |  |
| `proizhodi` | 7 | attach_variant | `arbitrary` |  |
| `navedeno` | 7 | attach_variant | `cited-stated` |  |
| `ukazanje` | 7 | attach_variant | `point-out` |  |
| `obćem` | 7 | attach_variant | `reg-obći` |  |
| `obsahujut` | 7 | attach_variant | `reg-sadržati` |  |
| `ekvivalentnym` | 7 | attach_variant | `reg-ekvivalentny` |  |
| `libovolne` | 7 | attach_variant | `arbitrary` |  |
| `libovolnymi` | 7 | attach_variant | `arbitrary` |  |
| `libovolnyh` | 7 | attach_variant | `arbitrary` |  |
| `obzir` | 7 | attach_variant | `with-regard` |  |
| `sovsem` | 7 | attach_variant | `entirely` |  |
| `zaměnja` | 7 | attach_variant | `substitution` |  |
| `pokazuju` | 7 | attach_variant | `reg-pokazati` |  |
| `aditivny` | 7 | insert_math_or_link_to_concept | `aditivny` |  |
| `suščstvovanje` | 7 | attach_variant | `exists-eksist` |  |
| `vnutrny` | 7 | attach_variant | `inner` |  |
| `prijeti` | 7 | attach_variant | `accepted-adopted` |  |
| `konstruuje` | 7 | insert_candidate_or_inflection | `konstruuje` | Constantinople |
| `uvažanjem` | 7 | insert_candidate_or_inflection | `uvažanjem` | #discretion, esteem |
| `razuměju` | 7 | attach_variant | `reg-razuměti` |  |
| `koordinaty` | 7 | insert_candidate_or_inflection | `koordinaty` | coordination |
| `obstajati` | 7 | attach_variant | `reg-obstajati` |  |
| `dodavanjem` | 7 | attach_variant | `by-adding` |  |
| `pričem` | 7 | insert_candidate_or_inflection | `pričem` | trailer (vehicle) |
| `sostojat` | 7 | attach_variant | `reg-sostojati` |  |
| `sootvěčajut` | 7 | attach_variant | `respectively-adv` |  |
| `sravnjenje` | 7 | attach_variant | `cf-abbrev` |  |
| `ljubogo` | 7 | insert_candidate_or_inflection | `ljubogo` | curiosity |
| `suščstveno` | 7 | attach_variant | `exists-eksist` |  |
| `porođajut` | 7 | attach_variant | `generates` |  |

## Boundary
This pass uses generated/internal Interslavic TeX and the community dictionary as classification aids. It may feed coverage discovery, variant attachment proposals, and internal consistency repair. It may not feed native branch witness counts or reviewed bridge status.
