# Interslavic normalization status and continuation — 2026-07-18

## Bottom line

The reviewed spelling layer is normalized across the canonical Noether Interslavic corpus, and two of Fable 5's three accepted lexical directions have now been executed at the exact, authorized surface level. This is substantial normalization success, but it is not whole-language completion: the correspondence family still needs a reviewed sense-and-inflection table, the simultaneous doublet needs an explicit corpus policy, and held rows still require appropriate external review.

Current status: **internal normalization advanced; not community-certified and not unified-v6.2 ready**.

A workspace-wide filename inventory found 1,072 Interslavic-named TeX paths when ignored material and retained copies are included. A separate TeX-content search for Interslavic/Medžuslovjansky labels found 286 files and likewise found no non-Noether work. Every extant translation source belongs to Noether; the remaining matches are Noether workspaces, renders, tranche preimages, or the Paper 06 Noether handoff. No SGA or other non-Noether Interslavic TeX corpus currently exists in this workspace. The 221-pair canonical Noether corpus is therefore the complete extant production corpus, not an arbitrary work-specific sample.

## What Fable 5 actually handed off

`03_projects/noether/FABLE_FINDINGS_FOR_SLAVIC_NOETHER_LANE_20260717.md` identifies itself as the Fable 5 handoff and states:

1. **Tranche 001 was already “WELL DONE — spec honored.”** That was the Paper 06-only orthography pilot defined in `00_governance/FABLE_TRANCHE_001_EXECUTABLE_SPEC_20260710.md`: apply the reviewed orthography mappings, rebuild the Cyrillic sibling and renders, and apply no lexical switches.
2. After that pilot and Floris's sign-off, the next separate tranche was the three accepted directions: `odnovrěmenno -> jednočasno`, `sootvětstvovati-family -> odpovědati-family`, and `korak -> krok`.
3. `ręd`, `jednako`, `važiti`, `slučaj` wording, and the ring family were held and were not to be silently settled.
4. State C, not older/withdrawn scores, was the evidence snapshot to quote.

The already-completed Paper 06 pilot was therefore not repeated. This activation satisfied the user-sign-off gate and continued from it.

## Current intelligibility evidence

The current serialized State C snapshot is:

- East `E=2341`
- West `W=223`
- South `S=239`
- `D1=1.7537043785` out of 3
- `KL=0.5368819503`

This shows a strongly East-heavy evidence distribution. It is a provenance/routing diagnostic, not a scalar definition of intelligibility and not linguistic certification. W0 (`E=2341`, `W=333`, `S=348`, `D1≈1.993192`) remains only a context-review projection. Decisions must use the typed evidence graph plus a declared family/cohort tree, with support, adverse, competitor, gap, and candidate channels kept distinct.

## Work executed in this activation

### Tranche 002A — corpus-wide reviewed orthography

- Scope: 221 paired canonical Latin/Cyrillic units; working/cumulative drafts excluded.
- Changed 146 TeX files: 69 Latin and 77 Cyrillic.
- Applied 331 paired-script replacements: `obšč -> obć`, `vzet -> vzęt`, `voobče/vobče -> obće`, and `dlugost -> dolgost`, with deterministic Cyrillic counterparts.
- Paper 06 remained unchanged because its pilot was already complete.
- Idempotence passed; no lexical or held rows were touched.
- Build gate: 146/146 PDFs, 467 pages, 14,152,797 bytes; zero TeX/package, missing-character, overfull, or underfull warnings.
- Render gate: all 467 pages rendered serially; zero blank/dark/edge flags; all master sheets and the stratified sample passed manual inspection.
- One pre-existing Paper 35 Cyrillic compile defect was repaired separately: blind transliteration had altered mathematics, environment names, and `pt`. The repair restored those structural spans from the aligned Latin sibling while leaving Cyrillic prose unchanged; its repair report, preimage, and diff are retained.

### Tranche 002B — exact accepted lexical surfaces

- Changed 92 TeX files: exactly 46 Latin and 46 Cyrillic.
- Applied 224 paired-script replacements.
- Exact authorized simultaneity sources removed: `odnovrěmenno`, `odnovremenno`, `odnovočasno`, and `istočasno` became `jednočasno` (with Cyrillic counterparts).
- `korak` became `krok` (with the Cyrillic counterpart).
- The correspondence family and all held rows were untouched.
- Idempotence passed.
- Build gate: 92/92 PDFs, 376 pages, 10,126,828 bytes; zero TeX/package, missing-character, overfull, or underfull warnings.
- Render gate: all 376 pages rendered serially; zero machine flags; all four all-page master sheets, seven larger sample sheets, and all six Paper 35 Cyrillic pages passed manual inspection.

## Post-work corpus status

The final TeX-aware audit covers 221 canonical Latin files (aggregate path-and-file hash `D930B9CD20647FC6C23CA60EAE47214D5784B8F4D43D46C1A9451CFB95F62544`).

| Family | Reviewed source residues | Current target probe | Status |
| --- | ---: | ---: | --- |
| `vzet -> vzęt` | 0 | `vzęt`: 71 | complete |
| `obšč -> obć` | 0 | `obć`: 194 | complete |
| `dlugost -> dolgost` | 0 | `dolgost`: 17 | complete |
| `voobče/vobče -> obće` | 0 | `obće`: 148 | complete |
| exact authorized simultaneity sources -> `jednočasno` | 0 | `jednočasno`: 82 | complete at authorized surface boundary |
| `korak -> krok` | 0 | `krok`: 44 | complete |
| correspondence family | 398 in 89 files | `odpověd*`: 71 | accepted direction; execution pending reviewed table |

### Correction to the R1 draft

The R1 draft called `jednočasno` “THE standard” and treated the other family as if it lacked dictionary standing. The actual community dictionary contradicts that simplification:

- `jednočasno`, ID 3852, line 5038: `bg+ hr~ pl+ ru- sk+ sr+ uk+`, frequency field 6708.
- `jednovrěmenno`, ID 16948, line 5068: `bg+ hr+ pl- ru+ sk- sr+ uk+`, frequency field 6700.

Dictionary file SHA-256: `072DE8E512EB386780D199FBD6F0ACF2639D3096EA920F1AF2D0AFCC5535E842`.

Both are sanctioned headwords with complementary recorded profiles. Consequently, the tranche retained 61 `jednovrěmenno`-family occurrences in 27 files: 59 adverb surfaces (including sentence capitalization) and 2 adjectival `jednovrěmennom` surfaces. It also held 14 nearby unreviewed forms in 9 files: `Jednovremenno` 5, `istovrěmenno` 3, and `samočasno` 6. These are policy/context work, not failed mechanical cleanup.

## What still needs to be done

### 1. Correspondence-family mapping — next executable tranche

The new TeX-aware inventory records exactly 398 occurrences, 58 distinct surfaces, and 89 affected files. The surfaces mix verbs, adjectives, adverbs, nouns, spelling variants, and likely malformed derivatives. Examples include `sootvětuje` (52), `sootvětně` (48), `sootvětno` (42), `sootvětny` (42), and `sootvětujut` (20).

Next action is to turn those 58 surfaces into a reviewed table with, for each surface:

- part of speech and inflection;
- intended mathematical sense in context;
- approved `odpovědati`-family or other target surface;
- Latin/Cyrillic deterministic pair;
- adverse/homograph warning;
- representative source contexts and reviewer status.

Only then should a paired dry-run, exact preflight, source edit, compile, render, and post-audit occur. A broad substring replacement is explicitly not authorized.

### 2. Simultaneous-doublet corpus policy

Decide whether both sanctioned headwords remain register variants, whether one is preferred only in particular contexts, and how adjective/adverb forms are handled. Do not infer a single standard from the R1 draft.

### 3. Smaller context-review queues

- `vprašanj*`: 19 root-probe candidates in 6 files; alias policy needed.
- `slijedi/sledi`: 21 case-insensitive root-probe hits in 5 files; the audit examples show embedded-string collisions such as `posledice`, so these must be tokenized/context-reviewed before any edit.
- `slućaj`: 18 spelling hits in one file, but the `slučaj` wording row remains held; no edit was made.
- `namreč/naime/totiž`: 19 hits in 16 files; any `imenno` preference requires explicit West/South register documentation.

The current root probes are routing inventories. They are case-insensitive and may include inflections or embedded strings; they are not replacement counts.

### 4. Held external-authority rows

No change was made to `ręd` (610 probe hits), `jednako` (79), `važi/važe` (353), `slučaj` wording (391), `kolc*` (792), or the isolated ring competitors (2). They remain held for homograph, register-extension, or terminology-family review.

## Evidence and continuation cursor

- `evidence/NORMALIZATION_STATUS_AUDIT.json` — final TeX-aware status, dictionary correction, limits, and examples.
- `evidence/CORRESPONDENCE_FAMILY_SURFACE_INVENTORY.json` — exact 58-surface next-tranche inventory.
- `evidence/NORMALIZATION_COMPLETION_CURSOR.json` — machine-readable resume point and evidence hashes.
- `tranche_002a_orthography/evidence/` — preflight, report, ledger, diff, preimages, build, render, and visual inspection.
- `tranche_002b_lexical_exact/evidence/` — preflight, report, ledger, diff, preimages, build, render, and visual inspection.

All scans, builds, and renders were serial and bounded to one source or PDF at a time. No whole-corpus body or parallel renderer set was materialized.
