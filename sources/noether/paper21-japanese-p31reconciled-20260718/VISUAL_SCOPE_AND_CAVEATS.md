# Japanese Noether Paper 21 visual-evidence scope and caveats

## Indexed payload

- Tranche root: `.`
- Image root: `render_check/`
- Accepted records: three target-render PNGs, one per page of the accepted three-page Japanese PDF.
- Exact visual bytes: 1,594,181.
- Canonical image-set manifest digest: SHA-256 `CA8A29AF82BB9F043CD3C6BDDC149762DEB96565F6B85E9E790F61AE44CE73A7`, computed over UTF-8 without BOM, LF-separated `filename,sha256,bytes` lines sorted by filename, with no terminal newline.
- Machine-readable authority: `VISUAL_EVIDENCE_INDEX.jsonl`; inspection projection: `VISUAL_EVIDENCE_INDEX.csv`; row contract: `VISUAL_EVIDENCE_INDEX.schema.json`.

Every PNG is 1654 × 2339 pixels. Embedded density is 199.9996 ppi in both axes and is normalized to the accepted 200-ppi render record. The parent PDF reports A4 pages of 595.28 × 841.89 points and rotation 0. Each record uses a full-image `pixels_top_left` bounding box and does not invent a semantic crop.

## Parent and authority binding

The parent PDF is `output/pdf/Noether_Paper21_Japanese_SourceReconciled_v001.pdf`, SHA-256 `BC9F967A46E75BC905F2ED2BBA5F12634C1E62E05F5FFF5F6E941BB31D0E524F`. The linked target TeX is SHA-256 `C8766BF85B516A356649AF5C72CC6B0C09FBDA00078C49DE4E47217907F15F42`; extraction SHA-256 is `336DC8BE58F5C557A97DED513642927E5B7A1FC4770E66B4E3B77D728D79B7DE`. The linked sealed German P31 whole-file SHA-256 is `A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F`; the raw Paper 21 source span, DE 12583–12674, has SHA-256 `21C8472242F1748C64E843DB028441C489D986AC8CA67590D470ABD4318FD8B6`.

## QA, supersession, and exclusion

All three accepted PNGs were inspected individually at original detail by the owning lane and an independent read-only reviewer. No clipping, collision, missing glyph, margin overflow, prohibited line-start small kana, or Japanese lexical page-boundary split remains. Tags `(140)`–`(146)` appear exactly once; notes `149)`–`162)` are complete. All six logical `ラグランジュ` occurrences keep `ジュ` joined, `沿って` remains joined, and page joins are clean.

The accepted set supersedes the rejected `98A820B3_line_start_small_kana_candidate`, whose page 2 began a line with `って` and which retained latent `ラグランジ／ュ` risks. Rejected renders remain under `tmp/rejected/` as internal debugging evidence and are excluded from the publication manifest. No contact sheet was created or used; individual original-detail PNGs are the visual authority.

Original German source pixels and diagnostic crops under `tmp/source_inspection/` remain local and excluded because they are source-check evidence with unresolved redistribution rights, not project-generated target renders.

This index records internal model visual review, not independent human, community, native-language, publication, or source certification.

## Rights and publication disposition

All three indexed files are project-generated target renders containing no third-party scan pixels. Publication totals are `open_payload: 3`; every other disposition is zero. The PNGs and their visual controls are to enter the next exact handoff to the existing GitHub/Zenodo public archive workflow. This package creates no competing draft and makes no archive deposit itself.
