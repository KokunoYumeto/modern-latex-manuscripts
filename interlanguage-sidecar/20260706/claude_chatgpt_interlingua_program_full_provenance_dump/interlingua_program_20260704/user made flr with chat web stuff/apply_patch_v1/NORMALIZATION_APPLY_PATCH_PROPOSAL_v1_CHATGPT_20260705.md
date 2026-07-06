# Normalization apply-pass patch proposal v1 (dry run)

2026-07-05. This is a Codex-safe dry-run patch proposal built from the R1 normalization decisions and the Latin Interslavic v001 TeX feed. No source TeX was edited. No form is certified or promoted. The file locators below identify candidate occurrences for a later Codex patch after review.

## Corpus and boundary

- Target scanned: `/mnt/data/slavic_tex_feed/Slavic_LaTeX_ProMode_Feed_20260704/02_primary_interslavic_latin`

- Canonical-ish Latin v001 TeX files scanned: **395**. Working chunks and non-v001 files excluded.

- Occurrence hits emitted: **6790**.

- Source-use boundary: this uses generated/internal Interslavic TeX as an internal-consistency source only. It can support patch targeting and consistency repair, not native branch witness status or external certification.

## Occurrence counts by risk class

| Risk/action class | Occurrences |
| --- | ---: |
| human_review_only | 2765 |
| deferred_no_apply | 1510 |
| candidate_after_review | 1298 |
| citation_rehead_only | 669 |
| context_check_only | 357 |
| sanctioned_doublet_record | 191 |

## Row summary

| Row | Action | Occ. | Files | Citation | Current lemma | Candidate / warning | Surface counts |
| --- | --- | ---: | ---: | --- | --- | --- | --- |
| step | prepare_candidate_rewrites_after_review / candidate_after_review | 57 | 31 | krok | korak | krok-family; morphology must be inflected by reviewer/Codex  | korakah:24; korakov:8; korak:8; koraka:6; korakih:4; koraku:3; korakom:2; koraky:2 |
| corresponds | prepare_candidate_rewrites_after_review / candidate_after_review | 737 | 162 | odpovědati | sootvětstvovati | odpovědati-family; rehead lemma; manual inflection ⚠ lexicon group lemma should be re-headed to odpovědati | sootvětně:94; sootvětuje:94; sootvětny:83; sootvětno:74; sootvětnost:36; sootvětnogo:31; sootvětujut:28; sootvětnyh:24; sootvětne:24; sootvětnymi:22; sootvětnu:14; sootvětnujut:14 |
| reg-pytanje | prepare_candidate_rewrites_after_review / candidate_after_review | 34 | 10 | pytańje | pytanje | pytanje/pytańje-family; manual inflection  | vprašanje:16; vprašanja:8; vprašanjah:3; vprašanjom:2; vprašanjam:2; vprašanju:2; vprašanj:1 |
| reg-obći | prepare_candidate_rewrites_after_review / candidate_after_review | 132 | 68 | obći / obće (adv) | obći | obće / obć*-family; orthography/flavor normalization ⚠ root is pan (ob-ьt-j-); scatter is orthography+flavoring, not lexeme choice; sl splošen = only true competitor, gloss it | vobče:33; obščem:16; obščejše:16; voobče:14; obščnosti:11; obščih:10; obščej:6; obščejših:5; obščejšem:4; obščim:3; obščejšoj:2; obščejšim:2 |
| remain-ostati | prepare_candidate_rewrites_after_review / context_check_only | 357 | 92 | ostati / ostavati | ostati | context-check: remain vs exist; no automatic rewrite ⚠ keep nastal/nastalo OUT (nastati=arise — fixed in v2.4) | obstaja:102; obstaje:71; obstajut:38; obstavajut:33; obstajanje:20; obstajajut:20; obstava:18; obstavaje:12; obstajati:11; obstavanje:8; obstajanja:7; obstavati:4 |
| follows-from | prepare_candidate_rewrites_after_review / candidate_after_review | 32 | 6 | slědovati (slěduje iz) | slěduje | slěduje/slědovati-family, but keep W gloss; manual  | slijedi:30; sledimo:2 |
| length | prepare_candidate_rewrites_after_review / candidate_after_review | 62 | 14 | dȯlgosť (co-sanctioned: dȯlžina) | dlugost | dolgost/dȯlgosť; orthographic normalization ⚠ two sanctioned forms; corpus dlugost = pl-flavored spelling of dolgost | dlugosti:32; dlugost:26; dlugostju:2; dlugostij:2 |
| take-vzeti | prepare_candidate_rewrites_after_review / candidate_after_review | 55 | 40 | vzęti | vzęti | vzęti/vzęto; nasal orthography  | vzeti:37; vzeto:6; vzetogo:5; vzetomu:4; vzetih:3 |
| type | prepare_candidate_rewrites_after_review / candidate_after_review | 0 | 0 | tip | tip | tip-family; zero W-cost same lexeme  |  |
| reg-odnovrěmenno | prepare_candidate_rewrites_after_review / candidate_after_review | 151 | 62 | jednočasno | odnovrěmenno | jednočasno; high-value W+S switch; manual review ⚠ HIGH-VALUE SWITCH: corpus-dominant odnovrěmenno is the E-outlier; dict jednočasno buys W+S simultaneously (both branches use čas-root) — cleanest win in the whole R1 set | odnovrěmenno:115; istočasno:20; odnovočasno:11; odnovremenno:5 |
| reg-imenno | prepare_candidate_rewrites_after_review / candidate_after_review | 38 | 32 | imenno | imenno | imenno plus mandatory W/S gloss; manual ⚠ F12b poster child: imenno has ZERO W/S presence — the register documentation MUST carry totiž/mianowicie/naime or W+S readers lose the connective | naime:16; namreč:16; totiž:6 |
| reg-sostojati | record_sanctioned_doublet_no_global_replace / sanctioned_doublet_record | 6 | 6 | sȯstojati sę (iz) | sostojati | sostoji orthography only for sastoji; skladati is sanctioned doublet ⚠ do NOT eliminate skladati — community-sanctioned | sklada se:4; skladaje se:2 |
| entirely | record_sanctioned_doublet_no_global_replace / sanctioned_doublet_record | 185 | 64 | sȯvsěm | sovsěm | sovsěm/vpolně/popolno all sanctioned; no global replace ⚠ popolno is dict-sanctioned; v4 scatter note amended | popolno:165; vpolně:20 |
| holds-is-valid | human_review_before_any_apply / human_review_only | 549 | 181 | važiti (REGISTER EXTENSION) | važi | human review: register-extension holds/valid ⚠ REGISTER-EXTENSION row: document explicitly that math sense extends dict sense; candidate for reviewer question | važi:497; velja:21; važiti:17; važy:8; važit:2; važilo:2; veljalo:1; važili:1 |
| reg-rěšenje | human_review_before_any_apply / human_review_only | 110 | 34 | rěšeńje (math: solution-of-equation) | rěšenje | human review; dict-sense tension but math usage supported ⚠ dict-sense tension (decision vs solution) documented; cs řešení supports the math usage — no change needed, note kept | rěšenje:39; rěšenja:34; rěšenj:17; rěšeno:7; rěšenju:4; rěšenjam:4; rěšene:2; rěšenjami:1; rěšena:1; rěšenomu:1 |
| series-sequence-red | human_review_before_any_apply / human_review_only | 1235 | 122 | ręd (with mandatory 4-branch gloss block) | ręd | human review: high-divergence series/row/order; mandatory gloss ⚠ HIGH-DIVERGENCE ROW: no pan lexeme (F12c); ред(S/E)=order homograph; final texts should gloss on first use per paper; strongest candidate for reviewer sign-off | rędov:204; rędy:194; ręd:169; red:103; reda:86; redov:75; rěda:72; rędami:68; ręda:45; redy:41; redu:32; rędah:31 |
| however | human_review_before_any_apply / human_review_only | 191 | 84 | jednako (with homograph usage-note) | však | human review: however/equally homograph risk ⚠ HOMOGRAPH WARNING: hr/sr jednak(o)=equal(ly) — in math prose where 'equally' is frequent, prefer sentence positions that disambiguate, or use ipak for contrast; this row NEEDS the reviewer | vsak:127; však:37; jednako:23; odnako:4 |
| case-instance | human_review_before_any_apply / human_review_only | 680 | 190 | slučaj | slučaj | human review: case/instance, belongs homograph risk ⚠ hr pripada=belongs homograph noted (F12c) | slučaju:387; slučaj:163; slučajah:28; slučaja:24; slućaju:22; slućaj:14; slučaje:13; slučaji:12; slučajem:5; slučajam:3; slučajno:3; slučajev:2 |
| carry-out | citation_rehead_only_or_no_text_change / citation_rehead_only | 135 | 67 | provesti | provesti / izvesti | documentation split only: provesti=perform, izvesti=derive ⚠ dict splits the senses: provesti=perform, izvesti=derive. Corpus uses izvesti for both — register doc should adopt the dict split (provesti=carry out construction, izvesti=derive result) | izvedeny:24; izvedene:22; provesti:20; izvesti:15; izvedeno:15; izvedena:7; izvedenogo:6; izvedenym:6; izvedemo:4; izvedenomu:3; izvedenom:3; izvedenoj:2 |
| assumption-noun | citation_rehead_only_or_no_text_change / citation_rehead_only | 534 | 169 | prědpoložeńje | prědpoloženje | citation rehead/document doublet; no global replace ⚠ both prědpoloženje and prědpostavka are real formations; citation = dict form; do not erase prědpostavka | predpostavjenju:50; predpostaviti:35; predpoloženju:30; predpostavjenja:28; predpostavlja:26; predpostavce:24; prědpoloženju:20; predpostavjenje:19; prědpostavce:18; predpostavky:16; predpoloženo:13;  |
| power-exponent | deferred_no_apply / deferred_no_apply | 1216 | 176 |  |  | deferred; power/exponent variant scatter ⚠ deferred | stepena:380; stepen:165; stepenj:140; stepenev:66; stepeni:64; stepenjev:40; stepenja:39; stepenovyh:36; stepenov:29; stepenove:26; stepenu:24; stupnja:24 |
| reg-dopuščati | deferred_no_apply / deferred_no_apply | 294 | 119 |  |  | deferred; allow/admit variant scatter ⚠ deferred | dopušča:88; dopuščajut:30; dopustime:30; dopuskaje:22; dopuskajut:21; dopustimy:16; dopustet:12; dopustima:10; dopustimyh:10; dopustja:8; dopusča:8; dozvoljaje:7 |

## Apply bands

### Band A — candidate rewrites after review

These rows are the only ones that can become Codex search/replace tasks after human or project review approves the citation-form choice. Inflected replacements must be generated by a language-aware pass, not by blind string replacement.

- **step**: korak → krok; 57 hits / 31 files. krok-family; morphology must be inflected by reviewer/Codex
- **corresponds**: sootvětstvovati → odpovědati; 737 hits / 162 files. odpovědati-family; rehead lemma; manual inflection
- **reg-pytanje**: pytanje → pytańje; 34 hits / 10 files. pytanje/pytańje-family; manual inflection
- **reg-obći**: obći → obći / obće (adv); 132 hits / 68 files. obće / obć*-family; orthography/flavor normalization
- **follows-from**: slěduje → slědovati (slěduje iz); 32 hits / 6 files. slěduje/slědovati-family, but keep W gloss; manual
- **length**: dlugost → dȯlgosť (co-sanctioned: dȯlžina); 62 hits / 14 files. dolgost/dȯlgosť; orthographic normalization
- **take-vzeti**: vzęti → vzęti; 55 hits / 40 files. vzęti/vzęto; nasal orthography
- **type**: tip → tip; 0 hits / 0 files. tip-family; zero W-cost same lexeme
- **reg-odnovrěmenno**: odnovrěmenno → jednočasno; 151 hits / 62 files. jednočasno; high-value W+S switch; manual review
- **reg-imenno**: imenno → imenno; 38 hits / 32 files. imenno plus mandatory W/S gloss; manual

### Band B — sanctioned doublets / documentation, no global replace

- **reg-sostojati**: record allowed forms; 6 hits / 6 files. sostoji orthography only for sastoji; skladati is sanctioned doublet
- **entirely**: record allowed forms; 185 hits / 64 files. sovsěm/vpolně/popolno all sanctioned; no global replace
- **carry-out**: citation or sense-documentation only; 135 hits / 67 files. documentation split only: provesti=perform, izvesti=derive
- **assumption-noun**: citation or sense-documentation only; 534 hits / 169 files. citation rehead/document doublet; no global replace

### Band C — human review before any apply

- **holds-is-valid**: 549 hits / 181 files. REGISTER-EXTENSION row: document explicitly that math sense extends dict sense; candidate for reviewer question
- **reg-rěšenje**: 110 hits / 34 files. dict-sense tension (decision vs solution) documented; cs řešení supports the math usage — no change needed, note kept
- **series-sequence-red**: 1235 hits / 122 files. HIGH-DIVERGENCE ROW: no pan lexeme (F12c); ред(S/E)=order homograph; final texts should gloss on first use per paper; strongest candidate for reviewer sign-off
- **however**: 191 hits / 84 files. HOMOGRAPH WARNING: hr/sr jednak(o)=equal(ly) — in math prose where 'equally' is frequent, prefer sentence positions that disambiguate, or use ipak for contrast; this row NEEDS the reviewer
- **case-instance**: 680 hits / 190 files. hr pripada=belongs homograph noted (F12c)

### Band D — deferred / no apply

- **power-exponent**: 1216 hits / 176 files. deferred; power/exponent variant scatter
- **reg-dopuščati**: 294 hits / 119 files. deferred; allow/admit variant scatter

## Codex-safe implementation rule

1. Treat this as a dry-run locator table. 2. Apply only Band A rows explicitly approved in a follow-up review. 3. Generate replacements with morphology-aware logic; do not use blind regex replacement for inflected forms. 4. Preserve sanctioned doublets. 5. Rebuild Latin and Cyrillic outputs together after any Latin change. 6. Re-run the corpus coverage and Cyrillic sync checks.
