# Tohoku canonical bilingual corpus - intake and ownership

Record opened: 2026-08-04T01:26:45.3252505Z

## Durable objective

Produce a complete canonical bilingual scholarly edition of both published
parts of Alexandre Grothendieck's *Sur quelques points d'algèbre homologique*,
Tohoku Mathematical Journal (Second Series), volume 9 (1957), pp. 119--221.
Deliver diplomatic French, separately corrected French, source-aligned English,
one complete paper reader plus sensible part-level readers, complete semantic
references/indexes, and a pre-Stacks graph.

## Exclusive ownership

- Owning task: `019fca5a-c29e-7330-acdc-c93f4a3dc9fb`, Grothendieck Tohoku -
  Canonical Bilingual + Stacks Scaffold.
- Exclusive corpus: both published parts of *Sur quelques points d'algebre
  homologique*, printed pp. 119--221.
- Opening cursor: printed p.119, first source-bearing line of Part I.
- Terminal cursor: printed p.221, end of Part II. Hard stop after the paper.
- Work root: this directory only.

## Live no-overlap inspection

Read-only live task inspection at 2026-08-04T01:26:45.3252505Z found:

- `019fca5a-bcf8-7813-93dd-1adff100c52d`: FGA only;
- `019fca5a-c80e-7890-a46b-4948ff443e6d`: Verdier Astérisque 239 only;
- `019fca5a-ce42-7ad1-baed-0e0564fe5ff7`: Illusie LNM 239 and 283 only;
- `019f711e-cac3-7a10-a0e6-dc0131799c3a`: SGA/FAC/GAGA production; its
  controlling handoff expressly does not own or overlap the four new corpora;
- active EGA, Deligne, Noether, CJK, archive, and unrelated tasks have no
  Tohoku ownership.

Result: **NO OVERLAP**. No second live Tohoku owner was present. This task does
not cede or enter FGA, any other Grothendieck paper, EGA, SGA, Verdier, or
Illusie.

## Bootstrap replay

- Handoff manifest: 1,184 bytes, SHA-256
  `F50A8D9171E44448083A42E6F0A668E49DD60EFD7EDE8BA6C77BDD6A75191E45`.
- Handoff validation: 465 bytes, SHA-256
  `B57817D9CA29CD01011603889CFFC2089EFE0F387774B2DFA386290A7A2DBA0D`.
- Read-only replay: 11 manifest rows, 40,193 payload bytes, 4 allocation rows,
  7 precedent rows, `PASS`, `errors=[]`.
- All seven exact precedents matched their listed byte counts and SHA-256
  identities and were read through EOF.

## Starting local witness

Private authority alias: `<LOCAL_TOHOKU_103P_WITNESS>`.

- bytes: 12,897,534;
- physical pages: 103;
- SHA-256:
  `57B8FE1A4563FAB33D56F2CA0171D4843D37FBBDE982A84859E2E232494B6D78`;
- page geometry: 517 x 729 pt; PDF 1.4; unencrypted.

The local witness is preserved read-only. Admission remains conditional on
the official two-part comparison recorded in `SOURCE_AUTHORITY.csv` and the
page map. No OCR is authorized or generated.

## Official record identities at intake

- Part I: J-STAGE article key `tmj1949/9/2/9_2_119`; printed pp. 119--183;
  DOI `10.2748/tmj/1178244839`.
- Part II: J-STAGE article key `tmj1949/9/3/9_3_185`, displayed title
  *Chapitre IV Les Ext de faisceaux de modules*; catalogued pp. 185--221;
  DOI `10.2748/tmj/1178244774`.

The corpus brief gives Part II's paper boundary as printed pp. 184--221. The
official Part-II catalogue begins at p.185, while the 103-page local witness
contains printed p.184 between the two official catalogue envelopes. This is
an explicit authority-boundary question, not a license to omit p.184. It must
be resolved by direct page comparison before the first textual unit is
admitted.

## Intake holds before textual admission

1. Freeze the exact official Part-I and Part-II PDF bytes and hashes in the
   isolated `authority_snapshot` below this root.
2. Compare official page envelopes with all 103 local pages, including printed
   p.184, and record the controlling image witness page by page.
3. Confirm the exact first source-bearing line on printed p.119 by direct
   rendered-image inspection.
4. Enumerate any unreadable marks or source-boundary discrepancies and fail
   closed until resolved.

This record is append-only. Later corrections or reversals receive new dated
entries; prior text is not rewritten.
