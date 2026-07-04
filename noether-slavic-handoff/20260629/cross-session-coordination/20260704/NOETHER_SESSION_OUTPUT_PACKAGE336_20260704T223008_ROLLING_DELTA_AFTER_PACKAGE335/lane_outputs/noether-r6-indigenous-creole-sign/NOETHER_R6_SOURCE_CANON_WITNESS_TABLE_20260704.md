# NOETHER R6 Source-Canon Witness Table

Status: source_canon_witness_table_no_translation_no_authority_promotion

Generated: 2026-07-04

Lane: Session I / R6 Indigenous, Creole, and Sign Access

Purpose: provide an easy-to-find front door for source-canon/source-authority witness work before any technical lexicon, translation, pilot, visual inventory, or term-spine work. This artifact keeps R6 Indigenous, creole/contact, signed-language, and sign-access rows separate from generalized interlanguage claims.

## Primary Tables

| Artifact | Rows | Use |
|---|---:|---|
| NOETHER_R6_SOURCE_CANON_STRICT_PROVENANCE_WITNESS_TABLE_20260704.csv | 82 | Preferred strict source-canon witness table. Every row has exact source URL, local path, SHA-256 hash, license/access signal, and tags. |
| NOETHER_R6_SOURCE_CANON_REQUIRED_FIELD_MIRROR_20260704.csv | 82 | Normalized mirror using the current source-canon steering fields: lane, target, owner/author route, source type, URL, local path, license/access signal, hash, source language, TeX/source-archive flag, fallback flag, blocker note, and non-claim boundary. |
| NOETHER_R6_SOURCE_CANON_WITNESS_TABLE_20260704.csv | 93 | Broad source-plus-guardrail table from the earlier pass. Includes 10 International Sign policy/question guardrail rows and 1 DGS placeholder-URL route row that are not strict source witnesses. |
| NOETHER_R6_NON_SOURCE_GUARDRAIL_ROWS_20260704.csv | 10 | International Sign comparator policy/question guardrail rows split out because they lack source URL/local path/hash and must not be treated as source-canon witnesses. |
| NOETHER_R6_NON_STRICT_ROUTE_METADATA_ROWS_20260704.csv | 1 | DGS route metadata row with local hash but placeholder live URL; not strict exact-URL provenance until repaired. |
| NOETHER_R6_SOURCE_CANON_EXPLICIT_GAP_LEDGER_20260704.csv | 78 | One row per missing or blocked source route with missing source type, known locator or error payload when available, next gate, and blocked-before boundary; includes explicit GitHub/source-repository and URL/access gaps. |
| NOETHER_R6_WHOLE_PROGRAM_SOURCE_CANON_ALIGNMENT_20260704.md | 1 | Whole-program alignment note recording repo-visible instructions, parent/B3 readings, cross-lane source-canon checks, R6 non-claim boundaries, and next source-maintenance gates. |
| NOETHER_R6_SOURCE_CANON_FIELD_COMPLETENESS_AUDIT_20260704.md | 1 | Field-completeness audit documenting the strict witness split, non-source guardrail split, and GitHub/source-repository gap additions. |
| NOETHER_R6_STRICT_PROVENANCE_PATH_HASH_AUDIT_20260704.md | 1 | Path/hash replay audit for the 82 strict provenance rows; all local paths exist and all recorded SHA-256 values match disk. |
| NOETHER_R6_STRICT_PROVENANCE_PATH_HASH_AUDIT_20260704.csv | 82 | Per-row path existence, actual byte count, actual SHA-256, and hash match status for strict provenance rows. |
| NOETHER_R6_STRICT_PROVENANCE_URL_REACHABILITY_AUDIT_20260704.md | 1 | Headers-only URL reachability audit for strict exact-URL rows; no source bodies saved. |
| NOETHER_R6_STRICT_PROVENANCE_URL_REACHABILITY_AUDIT_20260704.csv | 82 | Per-row live URL status: 77 reachable, 5 access-restricted endpoint-present. |

## Source-Archive Result

No validated R6 native mathematical TeX, LaTeX, arXiv, e-print, GitHub source repository, CTAN-style package, or source archive package was located in the recovered R6 evidence. The source-archive absence is recorded as explicit blocker rows rather than used to infer a technical register:

| Gap row | Scope | Missing source type | Next gate |
|---|---|---|---|
| R6-SRCARCH-GAP-001 | Indigenous Americas | Native mathematical TeX/LaTeX/arXiv/e-print/source archive | Continue official source capture and reviewer/source-owner routes; do not infer technical register from TeX gap. |
| R6-SRCARCH-GAP-002 | Creole/contact | Named-language mathematical TeX/LaTeX/arXiv/e-print/source archive | Continue official/OER/math-access source capture and reviewer/source-owner routes; do not infer technical register from TeX gap. |
| R6-SRCARCH-GAP-003 | Signed language | TeX/LaTeX source package as signed-language authority | Use signed-language source routes, video/access metadata, and media/reviewer gates. |

## Witness Coverage By Target

| Target family | Language/access target | Witness rows | Source-canon state |
|---|---|---:|---|
| Indigenous Americas | Quechua Central | 1 | Official Peru Minedu EIB math PDF plus extracted text; CC-BY-4.0 signal from DSpace metadata; reviewer/source-owner and reuse gates still required. |
| Indigenous Americas | Quechua Chanka | 1 | Official Peru Minedu EIB math PDF plus extracted text; CC-BY-4.0 signal from DSpace metadata; reviewer/source-owner and reuse gates still required. |
| Indigenous Americas | Aymara | 1 | Official Peru Minedu EIB math PDF plus extracted text; CC-BY-4.0 signal from DSpace metadata; reviewer/source-owner and reuse gates still required. |
| Indigenous Americas | Bolivia Quechua candidate | 1 | Bolivia Quechua curriculum PDF candidate captured; exact authority and reuse gates unresolved. |
| Creole/contact | Kreyol / Haitian Creole | 4 | MIT-Ayiti math/numeracy HTML witnesses captured; link/corpus-access support only until source-owner, reviewer, and reuse gates return. |
| Creole/contact | Jamaican Creole / Jamaican Patois | 2 | Jamaican curriculum/STEM context PDFs captured; comparator/context only until exact named-language math witness or reviewer route is found. |
| Creole/contact | Mauritian/Seychellois/Indian Ocean Creoles | 3 | Mauritius MIE curriculum/context captures exist; exact named-language textbook/practice rows and reviewer/source-owner gates still required. |
| Creole/contact | Nigerian Pidgin | 1 | English curriculum comparator/context capture only; no Nigerian Pidgin math authority. |
| Creole/contact | Papiamento/Papiamentu - Aruba | 2 | Aruba policy/context PDF captures exist; exact Papiamento/Papiamentu math source route remains blocked. |
| Creole/contact | Sranan / Saramaccan / Ndyuka / Guyanese Creole | 2 | Suriname/Guyanas context captures exist; exact language-specific math witness remains blocked. |
| Signed language | ASL | 3 | ASL-STEM and ASL-CORE route captures exist; video/media, caption/transcript, and reviewer gates block accepted signs or visual inventory. |
| Signed language | LSQ | 28 | CCJL LSQ mathematics/STEM route and concept captures exist; dynamic/API/media/reviewer gates block accepted signs or visual inventory. |
| Signed language | DGS | 30 | DGS source-route captures exist; dynamic/API/media/reviewer gates block accepted signs or visual inventory. |
| Signed language comparator | International Sign comparator | 4 strict source rows plus 10 non-source guardrail rows | Comparator/guardrail only; not a source authority for any local signed language. |

## Explicit Gap Families

| Target family | Gap rows | Main blockers |
|---|---:|---|
| Indigenous Americas | 35 | Paraguay Guarani exact download, Ecuador EIB exact routes, Guatemala Uspanteko exact routes, Mexico CONALITEG exact routes, native mathematical source archives, GitHub/source-repository evidence, and three live Minedu URL access checks remain unresolved. |
| Creole/contact | 30 | Bislama/Vanuatu exact PDFs, Papiamento/Papiamentu exact math PDFs, MIE exact Kreol rows, Jamaican Patois exact STEM, Nigerian Pidgin/Krio/Tok Pisin and other named creole/contact rows, named-language source archives, and GitHub/source-repository evidence remain unresolved. |
| Current gap retry | 8 | Retry queue for Ecuador EIB, Bislama/Vanuatu, Paraguay Guarani, Bolivia Quechua, Guatemala Uspanteko, Papiamento/Papiamentu, Krio/Sierra Leone, and Mexico CONALITEG remains source-start only. |
| Signed language | 5 | Signed-language TeX/source archive or GitHub/source repository cannot serve as sign authority by itself; video/access source routes require media/reviewer gates, two DGS live access checks remain restricted, and one DGS placeholder URL requires exact resolution. |

## Authority Boundary

This source-canon table permits source-location, provenance, hash checking, license/permission planning, reviewer/source-owner question drafting, and non-canonical corpus-access support notes. It does not permit source-authority promotion, accepted terms, accepted signs, visual inventory acceptance, excerpt selection, copied prose/media reuse, translation output, pilot creation, community-consent claims, native-review claims, canonical approval claims, or Git push.

Current gate counts remain zero for reviewer/source-owner returns, accepted source authority rows, license/media reuse clearances, accepted terms, accepted signs, selected excerpts, translation starts, constructed surfaces, and pilots.

## Path / Hash Integrity

`NOETHER_R6_STRICT_PROVENANCE_PATH_HASH_AUDIT_20260704.csv` verifies the 82 strict provenance rows against local disk state. Result: 82/82 local paths found, 82/82 recorded SHA-256 hashes matched, 0 missing files, and 0 hash mismatches. This is provenance integrity only, not permission, authority, review, reuse, translation, or completion evidence.

## URL Reachability

`NOETHER_R6_STRICT_PROVENANCE_URL_REACHABILITY_AUDIT_20260704.csv` checks the 82 strict exact-URL rows using headers-only/range probes and stores no source bodies. Result: 77 rows reachable, 5 rows returned access-restricted endpoint-present statuses, 0 missing/moved/request-failed rows. The 5 restricted rows are now explicit `R6-URL-GAP-*` rows in the gap ledger. One DGS placeholder-URL row was split into `NOETHER_R6_NON_STRICT_ROUTE_METADATA_ROWS_20260704.csv` and is also represented as `R6-URL-GAP-006`.
