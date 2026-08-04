# Korean Noether Paper 9 — T06 provenance revision 2

This immutable checkpoint preserves a provenance successor to the T01–T06 producer freeze. The translated scope and all 55 Korean targets are byte-identical to `ko-p09-t06`: German authority lines 6348–7022, with Paper 9 incomplete at line 7023.

Four producer surfaces changed: [META.md](files/root/META.md) now records the T06 rationale and retained segmentation failure; [ROUTE.md](files/root/ROUTE.md), [route.json](files/root/route.json), and [make.mjs](files/root/make.mjs) add a source-only T07 plan. T07 covers lines 7023–7133 in nine routed source units, but this checkpoint contains **zero T07 Korean targets and makes no T07 translation claim**.

Start with [META.md](files/root/META.md), [manifest.json](files/root/manifest.json), [ROUTE.md](files/root/ROUTE.md), and [validate.json](files/root/evidence/validate.json). The 55 current editable targets remain in [`targets/`](files/root/targets/).

Independent archive replay matched 55/55 targets, 9/9 manifest-listed evidence files, and all 64 routed German source slices, including the nine forward-only T07 slices. Eight JSON documents and 263 JSONL records parse. The supplied validator remains `PASS` for its unchanged T01–T06 mechanical scope only.

State: **T01–T06 complete producer draft; T07 route-only; Paper 9 incomplete; UNCHECKED, source-unchecked, formula-unchecked, Korean-unreviewed, uncompiled, unrendered, visually uninspected, unassembled, unapproved, and uncertified**.

Relative to `ko-p09-t06`, 71 files are byte-identical, four metadata/routing files changed, and no file was added or removed. This revision supersedes that checkpoint only for current provenance and forward routing; all Korean target bytes and every earlier generation remain public. No producer byte was edited or deleted by archive maintenance.
