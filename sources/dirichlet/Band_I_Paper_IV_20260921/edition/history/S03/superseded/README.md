# Dirichlet Band I, Paper IV — cumulative state after Prompt 03

**Next cursor: 4. Prompt 03 is complete; the independent final cold audit in Prompt 04 has not been executed. This is not a final publication-readiness claim.**

The current author editions cover printed pages **65–98 exactly once**, 34 pages in each language. The separate apparatus has 34 page records and a four-page reader. Printed pages **63–64** are the reprint title and blank verso: they remain copy matter only, excluded from both author readers. The complete scope is 36 leaves. There is no untouched author page remaining within Paper IV; `first_untouched_page` is therefore JSON `null`, not a pointer into Paper V.

## Current editable sources and readers

| Layer | Editable main | Current reader |
|---|---|---|
| Diplomatic French | `editions/fr/main.tex`, with `editions/fr/pages/p065.tex` through `p098.tex` | `readers/PAPER_IV_FR_PP065_098.pdf` — 34 pages |
| Faithful English | `editions/en/main.tex`, with independent page files | `readers/PAPER_IV_EN_PP065_098.pdf` — 34 pages |
| Separate apparatus | `apparatus/main.tex`; catalogue and page records under `apparatus/` | `readers/PAPER_IV_APPARATUS_S03.pdf` — 4 pages |

`state/CURSOR.json` is the current internal resumable state. `state/pages/` contains one accepted page record per author page. `ledgers/TOPOLOGY.tsv` maps all 36 leaves; `ledgers/COPY_MATTER_LEDGER.tsv` and `copy_matter/` preserve the two non-author leaves. Original folios, heads, imprints, signatures and rules are catalogued separately in `ledgers/PAGE_FURNITURE.tsv`.

The readers are re-typeset, not photographic facsimiles. Page boundaries, source paragraph starts, all prose and mathematical relations, display membership, local equation labels, note anchors and terminal matter are retained. Within-page typesetting reflows physical lines; no lexical modernization is inferred from this layout choice. The physical `der-` / `nière` split at 90/91 is retained in French. The English page break is at the corresponding `the last` / `equation` phrase. English running heads and imprints are translated. Source notes remain author notes; editorial observations remain in the separate apparatus.

## Authority and intake

The controlling scan is `input/10_AUTHORITY_EXACT_SCOPE_PDF_PAGES_080_115_PRINTED_PP063_098.pdf`, 36 leaves. The unchanged full-volume provenance witness is `input/11_AUTHORITY_FULL_DIRICHLET_GESAMMELTE_WERKE_BAND_I_1889.pdf`, 657 pages, 36,067,858 bytes, SHA-256 `961E55A2D32DDC88191CDD8A99F877A06BB3E721D7705F5A96C6F80AD67F9F6C`. Controls 00–09 and the literal Prompt03 are retained unchanged under `input/`.

The actual accepted predecessor was `DIRICHLET_P04_S02_CUMULATIVE_FULL_STATE.zip`, **180,461,785 bytes**, SHA-256 `7B0D13BED693B98E8D1C665DDCFA54939CBACFCFFF5FF328F137825E349665C4`. Its 517 regular members, CRCs, normalized safe names, manifest sizes/hashes, external checkpoint bindings, sidecar identity and cursor3 were validated before production. This continuation did not use the earlier zero-accepted input-access return as transcription. Initial-zero-acceptance controls are historical input, not current state.

All **21 immutable input originals** are embedded again, byte-identical to saved S02; no external immutable-file assembly is required. The R27 and R28 original archives and unpacked bytes remain unverified inherited evidence. Their accepted derivatives were source-replayed in S01/S02. Their out-of-scope cumulative readers remain preserved evidence only and are not incorporated into the Paper IV readers.

## What Prompt 03 did

Printed pages **87–98**, full-volume PDF pages **104–115**, exact-scope leaves **25–36**, were transcribed directly from the authority and translated completely. There is no inherited author transcription for this batch. The new source records contain 61 aligned structural units and 547 paired math segments. Segments include isolated variables, inline formulae, labels and display blocks; this is not a count of numbered equations or physical scan lines.

The last source leaf visibly bears printed folio98 and its terminal horizontal rule. Full-volume PDF page116 begins the next paper. Its separately named boundary image is inspection evidence only; no text from Paper V is transcribed into either edition or the apparatus as author content.

The required seams **74/75, 80/81 and 86/87** were freshly rechecked. All new internal seams through97/98 were also checked. The page record order, PDF folios and main-file inclusion lists agree with the fixed map. Each current reader includes each author page once and excludes copy matter63–64.

The known source issues on **66,70,77,82,85** remain literally unchanged. In particular, the printed `t` on77, `p²=φ²+ψ²` on82, and `t²+au²=ps` on85 have not been silently repaired. Their separate earlier apparatus explanations remain. New local primed labels retain their scope; the source open theta is represented by `\vartheta`. No new conjectural emendation is inserted.

Two refinements to the new English p97 restore explicit conditional constructions and remove an unnecessary comma at the printed equation junction. Actual earlier draft bytes, PDF build evidence and the earlier page image are preserved in `qa/s03/initial_build/`. `SOURCE_BACKED_DIFF.tsv` contains the original **70 S01/S02 rows unchanged**, followed by **2 S03 source-backed rows**. Missing formerly untouched pages are not misrepresented as inherited corrections. The session-only table is `qa/s03/SOURCE_BACKED_DIFF_S03.tsv`.

## Source and output evidence

`qa/s03/S02_INTAKE_VALIDATION.json` and `INSTRUCTION_READ_RECEIPT.json` record the intake and controls. `FULL_SCOPE_RASTER_EQUIVALENCE.tsv` verifies all36 controlling leaves against the unchanged full PDF at72dpi; `PAGEWISE_RASTER_EQUIVALENCE.tsv` records216dpi identity for the new source pages and rechecked seams. Source-page images are in `qa/s03/source/`.

`SOURCE_LINE_AUDIT.tsv`, `UNIT_ALIGNMENT.tsv` and `FORMULA_AUDIT.tsv` record the new batch. Their `CUMULATIVE_` counterparts preserve earlier audit rows and extend coverage through98. Line numbers refer to editable TeX, not claimed physical scan lines. The source collation and full translation review were visual/manual; the scripts encode that work and mechanically check bilingual math pairing. They are not OCR or an independent cold audit.

`BUILD_RUNS.json` records two final XeLaTeX passes for each of the three readers: all six exit0, with no warnings, overfull/underfull boxes or missing-character reports. Initial fresh-directory label/outlines rerun warnings were resolved by subsequent passes and are preserved, not hidden, under `initial_build/`.

All **72 current output pages** were rendered at126dpi and visually inspected. The24 new author-reader pages and4 apparatus pages were inspected individually; the44 previously accepted author-reader pages were reviewed in22 native-size pair sheets. Revised English97 was individually reinspected after its correction. `VISUAL_AUDIT.tsv` records every page. Text geometry checks and `pdffonts` output supplement but do not replace the visual review. The44 old author-reader pages are **text- and rendered-pixel-identical to S02**; see `S02_READER_REGRESSION.tsv`. All71 unaffected final page images also equal the images from the initial S03 visual review; only corrected EN97 changed.

## Preservation and resume

Every one of the **517 S02 member byte sequences** is preserved: unchanged files remain at the same relative path; replaced current wrappers, cursor, ledgers and diff have their originals under `history/S02/superseded/`. The three original external sidecars are in `history/S02/`. `qa/s03/S02_MEMBER_PRESERVATION.tsv` supplies the exact original-to-preserved path/size/hash mapping. The S01 preservation map and all earlier evidence remain. No earlier cumulative full-state ZIP is nested.

Earlier page-specific records and historical ledgers retain the statements of their original sessions, including then-current acceptance boundaries. Such historical statements do not override the current `state/CURSOR.json`, current catalogue and current readers. Previous PDFs remain evidence, not the latest editions. Historical tools are likewise preserved; **do not run S01/S02 source generators against the S03 current tree**, since they intentionally produce earlier extents.

To rebuild current readers with XeLaTeX installed, run:

```sh
python tools/s03/build_s03.py
```

Alternatively run `xelatex -interaction=nonstopmode -halt-on-error main.tex` twice from each of `editions/fr`, `editions/en`, and `apparatus`, directing outputs to separate clean directories as desired. Required TeX packages are named in the editable mains. The fonts are standard TeX-distributed Latin Modern/Computer Modern; no font files are redistributed. Build logs use this execution environment's absolute output paths; all edition input paths are relative and relocatable.

The current return is a self-contained cumulative ZIP plus three external sidecars. The exact manifest has one normalized path/size/uppercase-SHA256/role/acceptance/range/provenance row per ZIP member. To avoid circular hashes, the current external checkpoint and manifest are not current members of their own archive. The checkpoint binds the ZIP, manifest, standalone diff and every archive member; the internal cursor and identical internal diff are members. Historical checkpoints/manifests are preserved evidence, not circular current bindings.

The release verifier is `tools/s03/verify_handoff_s03.py`. Run it with `--zip`, `--checkpoint`, `--manifest` and `--diff` paths. It reopens the ZIP and verifies CRCs, safe unique normalized names, ordering, exact membership, all member hashes, sidecar bindings, cursor/accepted sets, immutable originals and predecessor-byte preservation. The ZIP is built twice from frozen member bytes with identical results; archive determinism does not assert bit-identical PDFs after rebuilding in a different TeX environment.

**Stop here at cursor4.** The remaining task is Prompt04's independent cold replay of all36 scope leaves, French lines/math, full English correspondence, notes, topology and boundary, followed by the final gates. That task has not been executed or pre-accepted in this return.
