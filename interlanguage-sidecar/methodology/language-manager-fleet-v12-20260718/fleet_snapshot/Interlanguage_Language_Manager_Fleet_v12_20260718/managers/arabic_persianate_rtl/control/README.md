# Arabic, Persianate, and RTL production lane

This is one operational translation-management lane, not a claim that its
languages form one linguistic family.

## Mandate

- Translate every work admitted to the Interlanguage corpus into the target
  languages routed here; the mandate is not limited to Noether or SGA.
- Keep Arabic, Iranian Persian, Dari, Tajik, Urdu, Pashto, Sorani Kurdish,
  Hebrew, and any later RTL target separate wherever translation, terminology,
  register, script, or review authority differs.
- Share only infrastructure that genuinely is shared: source provenance,
  Unicode normalization checks, bidirectional TeX/PDF engineering, manifests,
  hashes, and render inspection.
- Do not transfer a term from Arabic to Persian, or between Persian-family
  registers, merely because scripts or loanword histories overlap.
- A completed tranche requires translated TeX, a compiled and visually checked
  PDF, a source-use note, a terminology note, a manifest, hashes, and a precise
  continuation cursor.

## Routing registry

| Code | Target | Activation | Boundary |
| --- | --- | --- | --- |
| `ar` | Modern Standard Arabic | active | Arabic mathematical register; regional witnesses remain evidence, not automatic canon. |
| `fa_IR` | Iranian Persian | active | Independent Persian terminology and review lane. |
| `prs_AF` | Dari / Afghanistan Persian | source-intake | Not certified by Iranian Persian usage. |
| `tg_Cyrl_TJ` | Tajik in Cyrillic | source-intake | Separate script and terminology evidence. |
| `ur_PK` | Urdu | unactivated route | Separate Indo-Aryan language and review lane despite Perso-Arabic script. |
| `ps_AF` | Pashto | unactivated route | Separate Iranian language and review lane. |
| `ckb_Arab` | Central Kurdish / Sorani | unactivated route | Separate Kurdish register and orthographic policy. |
| `he` | Hebrew | unactivated route | Separate Semitic language; shares only RTL production tooling with most of this queue. |

An unactivated route is not a current target commitment. The table prevents a
later RTL request from being silently merged into Arabic or Persian; activation
requires a named target, source floor, register policy, and its own decisions.

## Research method

The current research-department reconciliation is binding:

- use a typed evidence graph for source-to-concept-to-form provenance and
  separate support/candidate/competitor/adverse/gap/veto channels;
- use a declared family/cohort tree only for dependence and branch breadth;
- do not treat either object as a scalar truth or readiness machine;
- treat W0 as a projection and reject unified v6.2 readiness;
- make no external/community-certification claim without an accepted return.

The initial objects are `EVIDENCE_GRAPH.json`, `COHORT_TREE.json`, and
`ADVERSE_LEDGER.csv` in this directory.

## First production cursor

`Noether / Paper 06 / opening / P06-S0002, P06-S0004, and P06-S0005`, with
independent `ar` and `fa_IR` translations. The continuation cursor is
`P06-S0006`.
