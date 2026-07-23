# SGA 6 complete layered English reader with internal links

This package is the preferred cumulative English reading and editable-source
surface for SGA 6 through the end of the available source. It covers
source-PDF pages 001--702 through idx702; there is no idx703. The reader is
378 A4 pages.

## Authority and claim limits

The authority is deliberately layered. The admitted French workpass remains
authoritative through idx684. The independently reviewed July 22 successors
supply idx685--702, and the unindexed terminological and notation indexes are
included after Expose XIV. This package does not promote the inherited prefix
to a uniformly source-certified translation, a critical edition, or a new
rights determination. Source scans and French authority files are identified
by the preserved evidence but are not redistributed here.

## Reference retrofit

The visible reader and source text are unchanged. The retrofit adds 1,492
stable named destinations and 2,256 resolved internal links. It leaves zero
ambiguous, unresolved, or uncovered internal-locator candidates. Two adjacent
Theorem 1.1 mentions retain explicit `layout_guard` status: their semantic
targets are recorded, but TeX link whatsits are omitted because they alter the
sealed line raster.

Five numbered-display destinations are placed inside their existing equation
number boxes. This preserves active destinations without changing prose-line
microtype expansion.

Validation passed with:

- 378/378 pages pixel-identical to the sealed predecessor;
- byte-identical extracted text;
- all 1,492 added destinations present and all linked targets valid;
- no URI annotations;
- all fonts embedded and Unicode-capable under the package validator;
- exact visible-source reconstruction for all 16 TeX dependencies.

The final PDF is
`output/SGA6_English_Complete_Layered_Terminal_SourceBacked_ReferenceRetrofit_20260723.pdf`,
3,289,538 bytes, SHA-256
`3CEE0FD4D50EB1D9B062637A05214B300F1F73EA7FA801CA92FE1B2E728C35D3`.

The editable master is
`working/SGA6_English_Complete_Layered_Terminal_SourceBacked_20260722.tex`;
its recursive 16-file TeX closure is included under `working/`. Archive
curation sanitized one nonprinting comment-only local scan-folder locator in
the public copy; no executable TeX or reader content changed.

## Package contents

The package contains only the cumulative PDF, the exact editable TeX closure,
the canonical target/reference ledgers, compact validation receipts, this
README, and a self-excluding SHA-256 manifest. It excludes source scans, raw
build logs, scripts, auxiliary files, full-page render dumps, private paths,
and historical scratch states.

The frozen producer delivery is bound by `controls/DELIVERY_MANIFEST.csv`
(92 self-excluding rows), its validation receipt, and
`controls/FINAL_REFERENCE_SUMMARY.json`. These controls identify the larger
source delivery without importing its intermediate build tree into this
compact archive package.

Publication must use the existing SGA Zenodo concept
`10.5281/zenodo.20410947`; no duplicate concept is authorized.
