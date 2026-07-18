---
title: "Interlanguage Research Method"
subtitle: "Controlled Interslavic Corpus Normalization, Tranches 002A through 007"
author: "Manuscript Typesetting Project"
date: "18 July 2026"
lang: en
---

# Purpose

This release records an executable normalization method applied to the complete
extant Noether Interslavic production corpus. It turns reviewed linguistic
decisions into bounded, inspectable changes while preserving rejected,
unreviewed, or context-sensitive forms for later review.

The associated Noether release is the publication surface for the actual
translation bodies and readers:

- Noether concept DOI: `10.5281/zenodo.20412587`
- Current version: see the public Noether record index for concept DOI `10.5281/zenodo.20412587`
- 221 canonical Latin-script TeX units and a 527-page reader
- 221 canonical Cyrillic-script TeX units and a 551-page reader

This sidecar contains the method, evidence, diffs, scripts, and quality-control
record. It does not duplicate the complete 442-body corpus.

# Governing distinction

Four forms of evidence must not be conflated:

1. **Mechanical closure** means that an authorized exact source form has no
   remaining residue in the declared corpus scope.
2. **Build and render integrity** means that the changed TeX compiles and that
   its pages have no detected blank, clipped, dark, or missing-glyph failures.
3. **Internal linguistic normalization** means that reviewed decisions were
   consistently executed across the corpus.
4. **External linguistic acceptance** requires suitable independent or
   community review and is not claimed here.

Likewise, source-faithful mathematical transcription is a separate question
from interlanguage normalization. Successful lexical or orthographic rollout
does not certify the underlying mathematical edition.

# Corpus boundary

The canonical production boundary is exactly the paired Noether translation
tree selected by `**/interslavic/v001/*.tex` and
`**/interslavic-cyrillic/v001/*.tex`. Working copies, cumulative drafts,
preimages, renders, and retained tranche material are excluded from the source
selection.

The final audit covers 221 Latin units and 221 Cyrillic units. A wider filename
and content inventory found no additional non-Noether Interslavic translation
corpus in the workspace. The aggregate path-and-file hash for the final Latin
selection is:

`D930B9CD20647FC6C23CA60EAE47214D5784B8F4D43D46C1A9451CFB95F62544`

# Tranche 002A: reviewed orthography

Tranche 002A applied only reviewed, paired-script orthographic mappings:

| Source family | Target family | Post-run source residue |
|---|---|---:|
| `vzet-` | `vzęt-` | 0 |
| `obšč-` | `obć-` | 0 |
| `dlugost-` | `dolgost-` | 0 |
| `voobče` / `vobče` | `obće` | 0 |

The pass changed 146 TeX files: 69 Latin and 77 Cyrillic. It applied 331
paired-script replacements. The previously completed Paper 06 pilot was not
silently repeated. No lexical or held family was touched.

One pre-existing Paper 35 Cyrillic defect was isolated during compilation.
Blind transliteration had altered mathematics, environment names, and the TeX
unit `pt`. Those structural spans were restored from the aligned Latin sibling
without replacing Cyrillic prose. The preimage, repair report, and diff are
retained.

The build gate compiled 146 of 146 changed units, producing 467 pages. The
recorded diagnostic counts are zero for TeX/package errors, missing characters,
overfull boxes, and underfull boxes. All 467 pages were rendered serially; no
machine page flag was raised, and the all-page sheets plus stratified samples
passed manual layout inspection.

# Tranche 002B: exact lexical surfaces

Tranche 002B applied only exact accepted surfaces:

| Exact source surface | Applied target |
|---|---|
| `odnovrěmenno` | `jednočasno` |
| `odnovremenno` | `jednočasno` |
| `odnovočasno` | `jednočasno` |
| `istočasno` | `jednočasno` |
| `korak` | `krok` |

Deterministic Cyrillic counterparts were changed in the paired units. The pass
changed 92 files, exactly 46 Latin and 46 Cyrillic, with 224 replacements. It
did not apply a broad correspondence-family substitution and did not touch held
rows.

The build gate compiled 92 of 92 changed units, producing 376 pages. Recorded
TeX/package errors, missing characters, overfull boxes, and underfull boxes are
all zero. All 376 pages rendered serially with no machine page flags; all-page
and stratified manual layout checks passed.

# Tranches 003-007: reviewed contextual families

Tranche 003 normalized the reviewed historic correspondence family across 179
units: 833 replacements, zero post-run family residue, 179 successful PDF
builds, and 556 reviewed pages. Tranche 004 adopted `jednočasno` as the corpus
default for simultaneity: 148 replacements across 71 units and 187 reviewed
pages. This is a corpus policy; both `jednočasno` and `jednovrěmenno` remain
dictionary-sanctioned forms.

Tranche 005 resolved four tokenized context queues: `vprašanj*`, genuine
standalone `slijedi`/Cyrillic `следи`, `slućaj*`, and the connective aliases
`namreč|naime|totiž`. It made 125 replacements across 49 units and retained six
embedded false positives such as `posledice`. Tranche 006 made four bounded
Paper 25 replacements from `prsten`/`прстен` to the corpus-primary algebraic
ring family `kolco`/`колцо` across two units.

Tranche 007 corrected the sole genuine residual `sledimo` token to
dictionary-canonical `slědimo` in Paper 17 section 11 and rebuilt its already
correct Cyrillic pair. The remaining five generic `sledi` probe hits are all
embedded `posledica` false positives and were not edited.

Each tranche retains preflight and post-run reports, exact change ledgers and
diffs, preimages, build and render reports, and human QA adjudication. All
reviewed source-family residual searches are zero and the rollout checks are
idempotent at their declared surfaces.

# Idempotence and evidence retention

Both passes were rerun as idempotence checks. A second run produced no further
authorized changes. For each tranche the public evidence package retains:

- exact preflight and post-run reports;
- a row-level change ledger;
- the applied unified diff;
- build journals and aggregate build reports;
- render metrics and human visual-inspection notes;
- all-page master sheets;
- the scripts used to apply, build, render, and audit the work.

This makes the change boundary inspectable without treating generated output as
independent linguistic authority.

# Policy correction preserved by the method

An earlier draft overclaimed that `jednočasno` was the single standard form.
The checked community dictionary records both `jednočasno` and
`jednovrěmenno` with complementary branch profiles. Tranche 004 subsequently
selected `jednočasno` as a declared corpus default for family/cohort breadth,
without declaring the alternative invalid. The evidence preserves that
distinction rather than rewriting editorial policy as linguistic fact.

This correction illustrates why an evidence graph, held queue, and exact
surface boundary are preferable to a scalar score or global search-and-replace.

# Open work

Tranches 003-007 and the final 221-unit streaming audit are closed. Retained
`ręd*`, `jednako*`, `slučaj*`, and `kolc*` are reviewed decisions. The sole
explicit external-authority blocker is 353 `važi*|važe*` mathematical
sense-extension probes in 101 files; changing them corpus-wide would be a new
semantic policy and is therefore not guessed away.

# Public status

This is a reproducible internal normalization and artifact-quality release. It
is not a critical edition, native-speaker certification, community approval,
peer review, or proof of mathematical source fidelity. The full Noether readers
and editable bodies are working translations and should be checked against the
German source control and source scans before scholarly reuse.

Corrections and additional evidence can be proposed through the project GitHub:

`https://github.com/KokunoYumeto/modern-latex-manuscripts`
