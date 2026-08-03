# SGA 1--7.2 global reader / FAC / GAGA logbook

## 2026-08-03 — corrected controlling objective

- The project owner corrected the task objective after the session had been narrowed incorrectly to FAC. The controlling bounded portfolio is:
  1. canonical diplomatic and separately corrected French TeX for SGA 1--7.2, FAC, and GAGA;
  2. complete source-aligned English FAC and GAGA readers;
  3. current standalone English SGA readers and one cumulative English SGA 1--7.2 TeX/PDF reader with stable intra-volume and cross-volume references;
  4. append-only rationale, correction, reversal, provenance, continuation, build, and release logbooks.
- The prior FAC-only pursuit goal was absent when checked and was therefore not a valid representation of the task. A corrected persistent goal was created in this task, and the task title was changed to `SGA 1–7.2 Global Reader + FAC/GAGA`.
- Disk truth at intake: no cumulative SGA 1--7.2 reader exists. The 2026-08-01 coordination and archive records explicitly reserve that label for a future actual cumulative object. Existing public/archive surfaces are standalone-reader bundles, with only SGA 3 already cumulative within its own volume.
- SGA 7 I is locally bilingual-complete through EOF: complete English reader plus full diplomatic and corrected French Tome-I layers. SGA 7 II is likewise locally bilingual-complete through EOF, including the personally transcribed terminal Exposé XXII range. These are source/build closures, not yet exhaustive all-SGA reference closure.
- FAC has complete source-aligned English and complete diplomatic/corrected French layers. Its exhaustive reference-v2/package pass is unfinished; this remains a real corpus debt rather than being silently described as done.
- GAGA is not complete. The only located custody root is a complete first-pass 42-page French transcription. Its own status records 21 source defects, 82 uncertain readings, and 32 visible page-join sentinel tokens forming 16 joins. No admitted source-aligned English GAGA reader was located.
- Current live-task check found no competing SGA global-reader task. The other active production task is titled `EGA — Canonical French TeX Completion`; the manager task is on Deligne D001--D045. This root therefore becomes the sole no-overwrite SGA cumulative production root unless the project owner later changes ownership.

## Resource-safety protocol after PC crashes

- Never perform recursive/global searches over Documents, the whole workspace, Codex history, or multi-terabyte roots.
- Search and read only exact named corpus directories, shallowly and sequentially.
- Do not run OCR/CUDA; do not start background processes; do not use parallel command batches.
- Do not delegate mathematical, source, translation, or visual judgments.
- Perform one bounded edit or one lightweight process at a time. Compile only after a meaningful source checkpoint.
- Record the exact last operation and honest uncertainty if the PC fails again; never infer causation from timing alone.

## Editorial decision policy

- The printed/source authority and the diplomatic French layer remain distinct from corrected mathematical/editorial readings.
- Every functional departure from the printed source must have a stable decision identifier, exact source and target locators, the selected reading, rejected alternative, rationale, and any supersession/reversal link.
- A later-discovered mistake triggers an append-only reversal record and global repair of every affected French, English, reference, and cumulative surface.
- English normalization is not permission to rewrite an author's mathematics or register. Stylistic choices must be documented when they affect meaning, terminology, theorem voice, notation, or cross-volume consistency.
- French omnibus redistribution is not assumed. Canonical French TeX and bounded/per-volume verification readers are archival controls; the public-facing omnibus requested here is English.

## Exact continuation

1. Freeze the current best standalone input identity for each SGA volume, including SGA 4½ as its own included segment and SGA 7 I/II.
2. Determine which standalone readers already satisfy reference-v2 and which require a reference-only successor.
3. Close GAGA and remaining FAC gates without delaying safe construction of the cumulative SGA framework.
4. Build the cumulative English SGA reader only from immutable admitted inputs; regenerate all cumulative reference coordinates and cross-volume links after final pagination.

## 2026-08-03 — first exact full-reader input shelf

- Nine immutable English reader inputs are now copied or downloaded into `inputs`: SGA 1, 2, 3, 4 proper, 4½, 5, 6, 7 I, and 7 II.
- Their combined extent is 4,185 PDF pages. Every copied/downloaded byte identity matches its controlling local or published decision record.
- `INPUT_READERS.csv` has 9 rows × 12 columns, zero formula-risk cells, 4,131 bytes, SHA-256 `E22066E3E8747C1FBF3B3530BC45C93B713A039D65E0EBF8F9CA78A088ABE884`.
- This is an exact input shelf, not yet a cumulative-reader claim. Reference holds remain explicit for SGA 4½, SGA 6, and SGA 7 I/II. SGA 3's English R28 is complete/reference-linked, but the requested canonical diplomatic French TeX reconstruction remains open because no complete public editor TeX exists.

### Operational correction SGA-GLOBAL-OPS-001

- While locating the SGA 2 full reader, a recursively scoped `rg --files -g '*.pdf'` was run over the exact SGA 2 production root. It completed in 0.2 seconds and performed no writes, but returned 418 paths and 10,024 characters before display truncation. That was unnecessarily broad for the question and violated the intended one-small-surface discipline even though it was not a whole-drive search.
- Correction: no further recursive listing of a corpus production root. Use already recorded exact paths, shallow directory listings, or one exact expected file. The command produced no artifact and changed no source.

## 2026-08-03 — bounded SGA 1 annotation-preserving inclusion probe

- Selected mechanism: `pdfpages` + `newpax`, under LuaLaTeX PDF management. This preserves an admitted standalone PDF byte-for-byte as the page-content source while reinserting its link annotations and named destinations. A distinct `destsuffix` per volume prevents common destination names such as `section.1` from colliding in the cumulative reader.
- Rationale: the nine standalone readers use heterogeneous TeX classes, macros, counter systems, and engines. Directly `\input`-ing all bodies into one engine would create unnecessary mathematical and layout risk. Annotation-preserving PDF inclusion provides a buildable cumulative TeX driver without rewriting admitted mathematical source; exact editable standalone closures remain packaged beside it.
- SGA 1 annotation extraction produced `SGA1_English_Reader.newpax`: 600,252 B / 25,473 lines / SHA-256 `BA4D82A42EDAF31AC9E1817823B6032F80B786DAD798A0842288A38E14DD9FDB`.
- The five-page LuaLaTeX probe compiled on the second pass to exactly five pages. Source pages 1--5 contain 123 link annotations; the probe contains the same 123. All 123 are internal GoTo actions and zero named targets are broken. The probe imports 1,894 named destinations from the five included pages.
- This proves the mechanism on one bounded reader segment only. It does not yet claim full SGA 1 annotation replay or any multi-volume build.

### Operational corrections SGA-GLOBAL-OPS-002 through -004

- `OPS-002`: a first `texlua` extractor attempted `require("newpax")`; MiKTeX's standalone `texlua` did not expose the package through its Lua module path. It failed before writing an annotation file. The script was changed to use kpathsea.
- `OPS-003`: the kpathsea-loaded package then failed under standalone `texlua` because `newpax.lua` expects LuaTeX's PDF `file` API. It again failed before writing an annotation file. The controlling extractor is now a minimal LuaLaTeX document, as the package's own documentation prescribes; the failed Lua script is retained as adverse history and must not be used.
- `OPS-004`: the first probe build contained a documented temporary sixth page. A second identical LuaLaTeX pass removed it, yielding the expected five pages. Any cumulative build must run to page-count convergence rather than accepting the first pass.
- Annotation extraction emitted repeated `pdfe reference expected` warnings from MiKTeX's PDF library. They are not silently dismissed: the five-page replay demonstrates complete 123/123 annotation preservation for the probe, but every full-reader extraction still requires independent link-count and broken-target validation.

## 2026-08-03 — cumulative merger decision and collision correction

- A full `newpax`/`pdfpages` build remains a valid archival fallback, but it is not the selected production merger. `newpax` rereads the annotation sidecar for each included page; the 4.28 MB SGA 3 sidecar across 1,470 pages would cause roughly 6 GB of repeated text parsing before the other eight volumes are considered. The project owner's resource-safety instruction rules out imposing that avoidable load on this PC.
- A bounded `pypdf` test established that appending the complete SGA 1 reader alone preserves all 262 pages, 2,151 named destinations, 1,600 link annotations, and zero broken internal targets.
- A naive complete SGA 1 + SGA 2 append preserved 2,907 links with zero syntactically broken actions but collapsed same-named destinations shared by the two readers. It produced 3,414 names instead of the expected 3,665 and semantically misrouted 251 names such as `Doc-Start` and common AMS-generated labels. That object is retained only as adverse evidence and is not an admitted reader.
- Selected correction: prefix every imported named destination and every named GoTo action with a stable volume identifier before cloning the complete reader. The two-volume proof produced exactly 440 pages, 3,665 destinations (the exact sum), 2,907 links, zero broken targets, and zero destination/page-route mismatches.
- The production implementation is `tools/build_prefixed_pdf.py`. It reads inputs sequentially, rewrites only the PDF navigation namespace, preserves page content and link rectangles, and creates one volume-level outline entry per input. It does not rewrite translated text, mathematical content, page geometry, or standalone source files.
- This decision is reversible: admitted standalone PDFs remain immutable inputs, and all prefixes are recorded in the build evidence. Any later semantic cross-volume links will be an append-only overlay against this collision-free namespace, never an inferred replacement for unresolved citations.

## 2026-08-03 — first complete SGA 1--7.2 cumulative PDF baseline

- The nine-volume namespaced build ran as one foreground process, with no OCR, recursive search, background task, or parallel job. It completed in 97.7 seconds. Available physical memory immediately beforehand was 44.71 GiB of 63.69 GiB.
- Exact reader: `build_baseline/SGA_1_7II_English_Global_Reader_baseline.pdf`, 4,185 pages / 33,197,207 B / SHA-256 `D8AC36D95CBE613DE898EB0578E33E7252CEFDC3AD52A1AD826614C88A808FF5`.
- Exact route validation: 33,334 named destinations, 27,054 link annotations, 27,052 internal GoTo actions, two non-GoTo actions, zero missing destinations, zero destination/page mismatches, zero broken named actions, and zero malformed internal actions. Validator status: `PASS` with `errors: []`.
- The merger printed `Annotation sizes differ` notices while importing heterogeneous source outlines. These notices did not reduce page, destination, or link counts and did not produce any routing error under the exact validator. They remain recorded as a build diagnostic; imported outline hierarchy and rendered volume seams still require their own checks.
- This is deliberately named `baseline`, not `final`: it preserves the currently admitted standalone navigation exactly and solves global namespace collisions, but it does not close the known SGA 4½, SGA 6, and SGA 7 I/II exhaustive-reference holds or add newly adjudicated cross-volume edges. It is the first actual complete SGA 1--7.2 reader object, not yet the terminal release object.
- A direct rendered seam review checked the opening page, both sides of every volume boundary, and the terminal page (18 rendered pages total). All nine readers occur in the correct order with intact page geometry; no seam clipping, duplication, or overprint was found. Receipt: `qa/BASELINE_VOLUME_SEAM_VISUAL_QA.md`.

## 2026-08-03 — outline-preserving navigation successor

- Exact validation of the first baseline found no broken page links but only nine outline entries: the volume roots. Pypdf's generic append path had not retained the 823 standalone descendant bookmarks. This was a navigation omission, not a mathematical-page or link-route failure.
- `tools/build_prefixed_pdf.py` was revised to read each standalone outline tree, resolve every bookmark to its source page, append page content with automatic outline import disabled, and recreate that tree beneath the corresponding volume root at the exact cumulative offset.
- A two-volume proof first passed with 161/161 outline entries, 3,665/3,665 destinations, 2,907/2,907 links, zero broken actions, and zero route mismatches.
- Current no-overwrite successor: `build_navigation_r2/SGA_1_7II_English_Global_Reader_navigation_r2.pdf`, 4,185 pages / 33,401,384 B / SHA-256 `4EBED6384BAEC85788A80C8FA9E9988624BECDE6129AC2429DA3BDB67F667B87`.
- Its validator passes 832/832 outline entries, all nine volume roots, 33,334 destinations, 27,054 links, and every destination/page route. The former baseline remains preserved as history.

## 2026-08-03 — SGA 7 reference-v2 intake

- Both admitted SGA 7 PDFs contain zero named destinations and zero link annotations. Translation/build completion was therefore not silently equated with reference completion.
- A read-only conservative scan of the exact 187 Tome-I and 183 Tome-II component files created source-located candidate inventories without changing either source tree.
- Tome I: 3,557 rows = 1,312 target candidates + 2,245 reference candidates; CSV 708,313 B / SHA-256 `5CCAE16C0247F294D9F95E0221CA153950E978E4390761F567365CB8DB8FA20C`.
- Tome II: 3,506 rows = 1,295 target candidates + 2,211 reference candidates; CSV 692,221 B / SHA-256 `867DEB966CE328975D257C0EA1A1ADBACBB1590E215693EA8C9C9AB23140BB1F`.
- These are deliberately over-inclusive locator inventories. Decimal dimensions, self-identifying declaration numbers, repeated proof headings, contents entries, and external-work citations remain candidates until lead disposition. No automatic semantic edge or source edit has been made from these inventories.

## 2026-08-03 — SGA 7 copy-on-write reference roots

- Tome I reference root: `standalone_successors/sga7i_reference_v2_r1`. Its copied source closure is exactly one active master plus 187 active components, 188 files / 1,075,250 B. Self-excluding baseline manifest: 22,471 B / SHA-256 `D76EAB64AF13A6844DD1241AEDB0F1954DE5AA75DD616C4F5475B974094AF471`.
- Tome II reference root: `standalone_successors/sga7ii_reference_v2_r1`. Its copied source closure is exactly one active master plus 183 active components, 184 files / 757,670 B. Self-excluding baseline manifest: 23,086 B / SHA-256 `43A1CCCC94857E18ACA48345AEE717397C9E9B76545B866D7AD8919A023D4312`.
- Neither successor copies historical builds, source scans, OCR, private QA crops, literal `$build`/`$out` scratch directories, French layers, or inherited superseded workpasses. The completed bilingual producer roots remain immutable evidence and authority controls.

### Operational correction SGA-GLOBAL-OPS-005

- The first Tome-I component copy command incorrectly used `Copy-Item -LiteralPath` with a `*.tex` wildcard. PowerShell correctly refused to expand the wildcard. It copied only the already requested master, then emitted a nonterminating path error; zero component files were written by that attempt.
- Correction: the exact source component directory was enumerated shallowly with `Get-ChildItem -File -Filter '*.tex'`, and each returned literal file was copied into the already-created no-overwrite successor. Final count is 187/187 components and the exact manifest above. Tome II used the corrected method from the outset.

## 2026-08-03 — SGA 4½ exhaustive reference closure

- The admitted 175-page R2 reader already had 790 targets and 761 edges, but explicitly left 286 detected occurrences outside its reference goal. That disclosure was honest but could not support the requested exhaustive convention-v2 cumulative reader.
- A lead semantic pass classified all 286 occurrences. The final machine result is 177 structural declarations, 69 external-work citations, 26 positively demonstrated nonreferences, 8 layout/geometry values, 5 accepted internal edges, and 1 unavailable sublocator. The external count includes explicit other-SGA locators that remain external in the standalone reader and are queued for cumulative resolution.
- Five definite local references were wrapped without changing their visible text: `VI 2.2`, three Chapter-VI `Section` locators, and the Chapter-VII `Section 1` locator. Three previously unnumbered `Example 1`–`Example 3` headings received zero-content stable targets.
- One apparent `Example 2` locator was deliberately not linked. Its source context identifies a subexample inside VI 1.3, but the inherited source exposes no distinct destination. Pointing it to the enclosing section would produce a clickable but mathematically coarse misroute; the correct convention-v2 disposition is `unavailable_target` pending a future source-backed subtarget.
- The candidate-class totals differ from an earlier provisional mental count because the final pass treated explicit locators in structural titles and bibliographic contexts by their semantic function rather than by a simple `label`/`cite` regex. This is a correction of the provisional inventory, not a translation change.
- Exact successor: `standalone_successors/sga4half_reference_v2_exhaustive_r1/build_r1/SGA4half_English_Reader_1_to_8.pdf`, 175 pages / 1,955,291 B / SHA-256 `1A5896FED610EAAD00D9628798FDF8F62FCF3F106407BA02AE2CAFB95CFFCA9E`.
- Compiled delta against admitted R2: destinations 1,357→1,360; GoTo actions 1,095→1,100; no removals, no broken targets, no images, no text-page changes. All five affected page renders are byte-identical to R2 at 200 dpi and passed direct lead inspection.
- `controls/REFERENCE_VALIDATION.json` is PASS/errors[], and wrapper removal reconstructs all 17 active predecessor source files byte-for-byte. This closes SGA 4½ as an internal input; cumulative cross-volume edges and the global release still remain.

## 2026-08-03 — cumulative navigation R3 and provisional-publication decision

- The cumulative reader was rebuilt once after admitting the exhaustive SGA 4½ successor. Exact R3 PDF: 4,185 pages / 33,402,752 B / SHA-256 `8686621D6324B0F5D7EECCE4EE7B90EDF310AF253731FCEB5569587F3E762357`.
- Exact validation is PASS/errors[]: 33,337 destinations, 27,059 links, 27,057 GoTo actions, 832 valid outline entries, and zero broken/misrouted/malformed actions or bookmarks. The expected delta from R2 is exactly SGA 4½'s +3 destinations/+5 links.
- The project owner explicitly requested that the recent archive task upload this reader provisionally. The handoff therefore labels it as a working checkpoint and states every remaining gate; it does not use “complete reference release,” “certified,” or equivalent language.
- Durable handoff: `PROVISIONAL_ARCHIVE_HANDOFF_20260803.md`. It names the replacement archive task, the exact fixed file identities, the existing-concept/no-duplicate rule, the open SGA7/SGA6/cross-volume/TeX-driver gates, rights caveats, and the two unpublished cumulative predecessors superseded by R3.
