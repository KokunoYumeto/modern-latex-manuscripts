# Dirichlet, Band I, Paper IV — S04 final cold-audited state

**Status: COMPLETE. Prompt completed: 04. Next cursor: COMPLETE.** No pending author page or further project prompt remains. Only Paper IV is edited. Printed63–64 are separately logged title/blank copy matter; author pp.65–98 occur exactly once in each monolingual reader. The readers are re-typeset, not photographic facsimiles: physical within-page line wrapping is reflowed, while wording, lexical hyphens, paragraph boundaries, formula grouping, page seams, notes and source furniture are retained. The French der-/nière split across90/91 is explicit; the English breaks at the corresponding phrase. Editorial explanations never enter either author text.

## Current sources and readers

French: `editions/fr/main.tex` and `editions/fr/pages/p065.tex` through `p098.tex`; reader `readers/PAPER_IV_FR_PP065_098.pdf` (34pages).

English: `editions/en/main.tex` and independent page files; reader `readers/PAPER_IV_EN_PP065_098.pdf` (34pages).

Apparatus: `apparatus/main.tex`, `apparatus/pages/` and `apparatus/CATALOGUE.tsv`; reader `readers/PAPER_IV_APPARATUS_S04.pdf` (5pages). Previous apparatus readers are historical evidence only.

The current cursor is `state/CURSOR.json`. Every current `state/pages/` record binds the final editable page, apparatus entry, fresh source image and individually inspected final reader images. `ledgers/TOPOLOGY.tsv` covers all36 leaves; `copy_matter/` and the copy ledger retain63–64 outside the author readers. The original blank diplomatic copy file remains zero bytes.

## Actual fresh intake and authority

The actual S03 ZIP was freshly unpacked: 210121951bytes, SHA256 E60E5A926AFCF66800C25C357690D0097AE4573B840F836755B3581B12923007. All793 carried members and checkpoint/manifest bindings were validated. This was sequential continuation, not acceptance of an earlier zero-page access checkpoint. The canonical inherited S03 diff is its 27503-byte72-row ZIP member, SHA256 8EF129DB12EA2FD89AFFE781AE90243FA8138591F034653329192F7D2C04BE78. The stale26591-byte browser sidecar is preserved separately under `history/S03/` and was not used as current text.

Controls00–09 and literal Prompt04 are unchanged under `input/`. The controlling exact-scope PDF has36 leaves. The full-volume witness has657pages,36067858bytes,SHA256 961E55A2D32DDC88191CDD8A99F877A06BB3E721D7705F5A96C6F80AD67F9F6C. All21 immutable input originals are embedded unchanged; no external assembly dependency remains. Original R27/R28 archives and all97 unpacked members are preserved, not promoted to authority. Their out-of-scope cumulative readers remain evidence only.

## Independent cold audit

Every one of the36 source leaves was opened freshly at216dpi and replayed against the fixed map. The34 French author pages were read line-by-line and mathematical-token-by-token against full-PDF82–115; every English paragraph was checked for complete structural correspondence. This included the inherited R27/R28 regions65–80, all headings, local labels, signs, operators, accents, primes, superscripts/subscripts, brackets, punctuation, the complete p.71 note and its anchor, all33 author-page seams, and terminal matter. Full-PDF115 visibly ends PaperIV at printed98;116 was inspected only as the next-work exclusion boundary. No PaperV text was ingested.

The actual observations are `qa/s04/MANUAL_COLD_COLLATION.json`; fresh scans and detail crops are under `qa/s04/source/`. Counts and TeX-line ledgers are supplementary and are not presented as source-reading evidence. `COLD_SCOPE_REPLAY.tsv`, `ALL_AUTHOR_SEAMS.tsv`, `NOTE_AUDIT.tsv` and `BOUNDARY_AUDIT.json` bind the scope, seams, note and exclusion checks. `UNIT_ALIGNMENT.tsv` and `MATH_SEGMENT_ALIGNMENT.tsv` pair200 structural units and1461 mathematical segments; segments include isolated variables and display blocks, not1461 distinct equations.

Twenty-one new concrete correction rows are appended to the canonical72 inherited rows, for93 cumulative rows in `SOURCE_BACKED_DIFF.tsv`. They restore heading tracking, locally absent product ellipses on72–73, the printed b (not contextual delta) on89, and explicit English conditionals. The new p.89 apparatus explains the distinction without repairing the author text. Exact before/after/source locators, immediate-before snapshots and repair verification remain under `qa/s04/`. The witness issues on66,70,77,82,85 and89 remain literal; the p.71 inherited alterations are distinguished from genuine printed readings. There are no unresolved illegible-source ambiguities and no known remaining author-content defect after this audit.

## Clean builds and complete output review

Each reader was built in its own initially empty directory. The initialization pass has expected outline/page-label rerun notices; they are preserved, not hidden. Two subsequent final acceptance passes per reader (six clean passes total) had no warnings, overfull/underfull boxes or missing-glyph reports, and the two final PDFs per layer are byte-identical. Logs, recorder files and outputs are under `qa/s04/build/`; `BUILD_RUNS.json` binds them.

All73 final output pages (34French,34English,5apparatus) were rendered at126dpi and each individual page image was opened and inspected. `MANUAL_OUTPUT_REVIEW.json` binds every reviewed image to its final reader; no clipping, broken formula, missing glyph, wrong-order page or note overflow was found. Independent Poppler renders of all73 pages, font embedding and text geometry provide additional checks. The52 author-reader pages not affected by a cold-audit correction match S03 extracted text and rendered pixels exactly; the16 affected pages have source-backed revisions. Regression identity is not used as fidelity evidence.

## Preservation, reproducibility and verification

Every S03 member byte sequence remains available. Unchanged files retain their path; originals of replaced files reside under `history/S03/superseded/`, and the canonical old diff is separately preserved. `qa/s04/S03_MEMBER_PRESERVATION.tsv` supplies a793-row exact original-to-preserved path/size/SHA256 map. Earlier S01/S02 preservation evidence remains unchanged. No earlier cumulative ZIP is nested. Historical checkpoints, source claims, logs and scripts retain their original stage meanings; they do not override the current state. Do not run earlier-stage source generators on this final tree.

To rebuild the final sources with XeLaTeX and the standard packages named in the mains:

```sh
python tools/s04/build_s04.py
```

The script uses separate clean build directories, one initialization pass followed by two acceptance passes, and captures all evidence. Rebuilding changes current build evidence and requires renewed binding/visual checks before repackaging. Fonts are standard TeX-distributed Latin Modern/Computer Modern; no font files are redistributed. Edition input paths are relative; recorder logs preserve the execution environment's actual paths.

The release ZIP is built twice from frozen member bytes with fixed metadata and sorted safe normalized paths; the two archives must be identical. This determinism applies to the frozen member bytes, not a promise of PDF byte identity under a different TeX installation. The external stage-specific checkpoint and manifest are not their own archive members, avoiding circular hashes. The external checkpoint binds the ZIP, exact manifest, standalone cumulative diff and every member; the internal diff is byte-identical to the linked stage-specific standalone file. Historical sidecars remain ordinary evidence members.

Use `tools/s04/verify_handoff_s04.py` with `--zip`, `--checkpoint`, `--manifest` and `--diff` to reopen and verify CRCs, safe unique names, membership, every hash, cursor/accepted sets, current reader and visual bindings, immutable inputs and all predecessor bytes. The four final linked filenames are stage-specific to prevent reuse of stale generic browser basenames. No public upload or outside-work expansion was performed.

**Completed Prompt04. Next cursor: COMPLETE.**
