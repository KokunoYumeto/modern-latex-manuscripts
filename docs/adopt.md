# Adopt or Mirror a Work

This is the operational layer of the project: a board for adopting, mirroring,
checking, or extending a bounded author/work corpus. The existing archive maps,
source shelves, reader shelves, manifests, and receipts remain the authoritative
record of what bytes and claims already exist. This page does not replace them.

Use the [machine-readable board](../manifests/adopt.json) for automation or a
Mathematics Commons mirror. Use the
[adoption issue](https://github.com/KokunoYumeto/modern-latex-manuscripts/issues/new?template=adopt.yml)
to announce a scope, mirror, or result.

## Three Different States

| State | Meaning |
|---|---|
| **Current work** | A project lane is actively advancing the scope. Independent checking and declared parallel mirrors are welcome, but the row is not an unclaimed assignment. |
| **Ready for adoption** | Existing readers, sources, maps, or an exact continuation cursor make a bounded contribution possible now. No exclusive owner is asserted. |
| **Future** | The author or corpus is worth exposing, but the repository does not yet bind enough source/cursor evidence for a responsible production start. Source discovery or intake binding comes first. |

`Priority` measures likely mathematical/public value, not quality or prestige.
`Readiness` measures how directly a contributor can begin from current GitHub
evidence. Neither field certifies a translation or source edition.

## Current Work

| Board ID | Scope | Maintained as | Existing surface | Parallel contribution |
|---|---|---|---|---|
| `noether-multilingual` | Emmy Noether multilingual papers | Kokuno Yumeto project lanes | [Language/work map](noether-map.md) | Review an existing language/work target, propagate a verified German correction, or mirror a bounded paper with exact inputs. |
| `grothendieck-school` | Grothendieck-school corpus: SGA, EGA, FGA, Verdier, Tôhoku, Illusie, and Deligne | Kokuno Yumeto project lanes; individual producer lanes retain their own publication custody | [EGA](ega-map.md), [FGA](fga-map.md), [Verdier](verdier-map.md), [Tôhoku](tohoku-map.md), [Illusie](illusie-map.md), [Deligne](deligne-map.md), and the preserved [SGA landing](records/sga.md) | Check a named page/range or build an explicitly independent mirror. Do not silently overwrite a producer generation. |
| `weber-algebra` | Heinrich Weber, *Lehrbuch der Algebra* | Kokuno Yumeto project lanes | [Weber map](weber-map.md) | Continue the exact Volume II frontier or independently check a bounded existing section. |

The maintainer label describes current coordination, not ownership of the
underlying mathematics and not an exclusive reservation. Declared overlap is
useful when it creates an independent comparison rather than an untraceable
replacement.

## Ready for Adoption

| Board ID | Priority | Author/work | Readiness | Bounded start |
|---|---|---|---|---|
| `gauss-werke-ii` | High | Carl Friedrich Gauss, *Werke* II | Exact cursor | Recover the registered continuation packet and continue after printed p.303, with p.305 next. Start at the [Gauss map](gauss-map.md). |
| `sylvester-v1` | High | James Joseph Sylvester, collected papers Volume I | Exact cursor | Continue at book p.494 from the [Sylvester map](sylvester-map.md). |
| `gordan-invariantentheorie-v1` | High | Paul Gordan, *Vorlesungen über Invariantentheorie* I | Exact cursor | Continue after source p.28; retain the article-corpus register. See [known gaps](known-gaps.md#gordan--clebsch-gordan). |
| `maxwell-treatise-v1` | High | James Clerk Maxwell, *Treatise on Electricity and Magnetism* I | Exact cursor | Continue at printed p.80 from the existing p.1–79 sequence. See the [work queue](work-queue.md#highest-value-typesetting-and-source-check-work). |
| `gibbs-papers-v1-p3` | High | J. Willard Gibbs, *Scientific Papers* I, Paper 3 | Exact cursor | Continue after printed p.134 from the current source-witnessed sequence. See the [work queue](work-queue.md#highest-value-typesetting-and-source-check-work). |
| `dedekind-gmw-i` | High | Richard Dedekind, *Gesammelte Mathematische Werke* I | Exact cursor | Continue with item V at printed p.40; items I–IV through p.39 are already bound as the cumulative base. Start at the [Dedekind map](dedekind-map.md). |
| `dedekind-stetigkeit` | High | Richard Dedekind, *Stetigkeit und irrationale Zahlen* | Exact cursor | Continue §5 after printed p.328 and finish §§5–7 through p.334/335, retaining the source-checked preface and §§1–4. Start at the [Dedekind map](dedekind-map.md). |
| `dirichlet-werke-ii-xxv` | High | P. G. Lejeune Dirichlet, Werke II item XXV | Repair-ready | Repair the formula and line-level defects over printed pp.263–302 using the retained source witness and explicit repair queue. Start at the [Dirichlet map](dirichlet-map.md). |
| `dirichlet-werke-ii-xxvii` | High | P. G. Lejeune Dirichlet, Werke II item XXVII | Repair-ready | Produce the missing typed German source track for printed pp.309–356 and reconcile it with the existing English surface. Start at the [Dirichlet map](dirichlet-map.md). |
| `riemann-werke-sync` | High | Bernhard Riemann, broader *Gesammelte mathematische Werke* draft | Repair-ready | Recover or produce an exact post-trim source/control package for the current 511-page reader without conflating it with stale 512-page controls. Start at the [Riemann map](riemann-map.md). |
| `cayley-repair` | High | Arthur Cayley, collected papers | Repair-ready | Choose a small range, recover its source witness, and perform a page-level glyph/source audit before re-promotion. Start at the [Cayley map](cayley-map.md). |
| `hecke-zahlentheorie` | High | Erich Hecke, *Vorlesungen über die Theorie der algebraischen Zahlen* | Review-ready | Audit completeness, chapter/page resets, and publisher matter in the 184-page assembly. Start at the [additional-author map](cluster-map.md). |
| `killing-transformationsgruppen` | High | Wilhelm Killing, transformation groups | Expansion-ready | The current reader is only the twelve-page second part; bind the missing parts before building an author-level reader. Start at the [additional-author map](cluster-map.md). |
| `einstein-annalen` | High | Albert Einstein, *Annalen der Physik* contributions | Intake-ready | Bind the observed source-intake files to a work register, then choose one bounded paper. See the [source-intake note](../manifests/source-intake/20260623_math_annalen_90_96_and_os_sources.json). |
| `minkowski-werke-ii` | Medium | Hermann Minkowski, collected works II | Review-ready | Check whether the selected-paper assembly represents the intended volume, then recover source/package closure. Start at the [additional-author map](cluster-map.md). |
| `klein-collected` | Medium | Felix Klein, collected works | Intake-ready | Turn the observed collected-works source intake into an exact volume/work register before transcription. See the [source-intake note](../manifests/source-intake/20260623_math_annalen_90_96_and_os_sources.json). |
| `hurwitz-works` | Medium | Adolf Hurwitz, mathematical works | Intake-ready | Bind the observed source material to an exact work register and select a bounded first paper. See the [source-intake note](../manifests/source-intake/20260623_math_annalen_90_96_and_os_sources.json). |
| `riemann-selected-repair` | Medium | Bernhard Riemann, selected papers | Repair-ready | Repair the selected-papers TeX ending, recover the missing source witnesses, and prove which exact reader it builds. Start at the [Riemann map](riemann-map.md). |
| `steinitz-1906-euler` | Medium | Ernst Steinitz, 1906 Euler-polyhedron note | Intake-ready | Bind the exact work and source witness as a distinct generation before transcription. Start at the [Steinitz map](steinitz-map.md). |
| `steinitz-1908-analysis-situs` | Medium | Ernst Steinitz, 1908 *Beiträge zur Analysis Situs* | Intake-ready | Bind the exact work and source witness as a distinct generation, separate from the existing 1911/1912 work. Start at the [Steinitz map](steinitz-map.md). |
| `steinitz-witness-recovery` | Medium | Ernst Steinitz, existing nine-work witness recovery | Review-ready | Recover the ledgered scans, QA images, and missing 1897 source PDF by exact recorded hash; do not synthesize absent bytes. Start at the [Steinitz map](steinitz-map.md). |
| `non-european-review` | Medium | Non-European mathematical texts | Review-ready | Check or assemble an existing direct/source-only language layer before starting any new translation. Start at the [exact map](non-european-map.md). |
| `ukrainian-modules` | Medium | Ukrainian applied mathematics modules | Continuation-ready | Use the closed public driver and continue only the mapped partial modules. Start at the [exact map](ukrainian-map.md). |

### Existing work that must not be retranslated

These tracked editable layers do not yet have matching direct readers. Their
missing PDF is an assembly or checking gap, not evidence that the translation
does not exist.

| Board ID | Priority | Existing author/work layer | Exact start | Next result |
|---|---|---|---|---|
| `nine-chapters-arabic-assembly` | High | *Nine Chapters*, Arabic volumes 1–3 | [Arabic TeX](../sources/non-european/sources/translations/arabic/chinese/jiuzhang-suanshu-vols1-3_arabic.tex) | Check and assemble the existing source against the mapped Chinese/English layers. |
| `sunzi-arabic-assembly` | High | *Sunzi Suanjing*, Arabic | [Arabic TeX](../sources/non-european/sources/translations/arabic/chinese/sunzi-suanjing_arabic.tex) | Check and assemble the existing source-facing layer. |
| `liye-fenlei-english-v1-3` | High | Li Ye / Gu Yingxiang, *Fenlei Shishu*, English volumes 1–3 | [English-bilingual TeX](../sources/non-european/sources/translations/english_bilingual/chinese/li-ye-ceyuan-haijing-fenlei-shishu-vols1-3_bilingual.tex) | Assemble volumes 1–3, then declare any continuation from volume 4. |
| `liye-english-v10-12` | High | Li Ye, *Ceyuan Haijing*, independent English volumes 10–12 | [Independent-English TeX](../sources/non-european/sources/translations/english_bilingual/chinese/li-ye-ceyuan-haijing-vols10-12_english.tex) | Assemble and compare this independent layer with the existing reader. |
| `qin-modern-zh-f2-4` | High | Qin Jiushao, *Shuxue Jiuzhang*, modern-Chinese fascicles 2–4 | [fascicle 2](../sources/non-european/sources/translations/classical_modern_chinese/chinese/qin-jiushao-shuxue-jiuzhang-fascicle2_classical-modern_bilingual.tex), [3](../sources/non-european/sources/translations/classical_modern_chinese/chinese/qin-jiushao-shuxue-jiuzhang-fascicle3_classical-modern_bilingual.tex), and [4](../sources/non-european/sources/translations/classical_modern_chinese/chinese/qin-jiushao-shuxue-jiuzhang-fascicle4_classical-modern_bilingual.tex) | Check and restore the omitted fascicles to a successor modern-Chinese reader. |
| `ibn-al-qifti-english-assembly` | Medium | Ibn al-Qifti, *Tarikh al-Hukama*, English | [English-bilingual TeX](../sources/non-european/sources/translations/english_bilingual/references/ibn-al-qifti-tarikh-al-hukama_bilingual.tex) | Assemble and check it against the mapped reference selection. |
| `al-battani-collation` | High | al-Battani, *Opus Astronomicum* and related tables | [Exact current surface](non-european-map.md#al-battani-current-github-surface) | Continue the named Arabic-description, table-cell, region, and chronology collation residuals. |

### Current readers needing source or provenance closure

| Board ID | Priority | Author/work | Current GitHub surface | Bounded start |
|---|---|---|---|---|
| `landau-elementary-review` | Medium | Edmund Landau, *Elementary Number Theory* | [243-page English body](<../reader-pdfs/author-cluster/02 Reader PDF - Landau - Elementary Number Theory.pdf>) | Recover title/translator/publisher and exact source closure without recreating the reader. |
| `hensel-zahlentheorie-review` | Medium | Kurt Hensel, *Zahlentheorie* | [251-page German reader](<../reader-pdfs/author-cluster/04 Reader PDF - Hensel - Zahlentheorie.pdf>) | Recover exact source/editable closure and compare one bounded range. |
| `oka-memoirs-review` | Medium | Kiyoshi Oka, Memoirs I–X | [141-page English collection](<../reader-pdfs/author-cluster/05 Reader PDF - Oka - Analytic Functions of Several Variables I-X.pdf>) | Bind memoir-level source and translation provenance. |
| `hausdorff-set-theory-review` | Medium | Felix Hausdorff, *Set Theory* | [413-page English edition](<../reader-pdfs/author-cluster/06 Reader PDF - Hausdorff - Set Theory.pdf>) | Recover the source/translation closure while keeping it distinct from the German composite. |
| `grassmann-anthology-review` | Medium | Hermann Grassmann, *Ausdehnungslehre* anthology | [613-page English anthology](<../reader-pdfs/author-cluster/07 Reader PDF - Grassmann - Ausdehnungslehre and Related Works.pdf>) | Register every component work and bind its source/provenance. |
| `hausdorff-mengenlehre-review` | Medium | Felix Hausdorff, *Mengenlehre* and later writings | [675-page German composite](<../reader-pdfs/author-cluster/08 Reader PDF - Hausdorff - Mengenlehre and Descriptive Set Theory Writings.pdf>) | Register components and recover source closure without collapsing the English edition. |
| `bianchi-vol1-a2` | Medium | Luigi Bianchi, Volume I / A2 through p.0135 | [Exact work-queue description](work-queue.md#highest-value-typesetting-and-source-check-work) | Audit formulas, references, terminology, index entries, and difficult glyphs against the current compact baseline. |
| `frobenius-ra05-audit` | Medium | Ferdinand Georg Frobenius, RA05 baseline | [Exact work-queue description](work-queue.md#highest-value-typesetting-and-source-check-work) | Declare one work/range and perform a targeted source/formula/table/notation comparison. |

## Future / Source Discovery First

| Board ID | Priority | Author/work | Why it is not yet adoption-ready | First useful result |
|---|---|---|---|---|
| `lie-foundations` | High | Sophus Lie, selected foundational works | No verified author/work source shelf or continuation cursor is currently bound by this board. | A bibliographic work register plus exact public source identities and one bounded pilot proposal. |
| `galois-oeuvres` | Medium | Évariste Galois, *Oeuvres* and manuscripts | Source-intake packets are noted, but no promoted transcription or translation is bound as current. | Reconcile the printed and manuscript witnesses into a small, exact first-work intake. |
| `eisenstein-abhandlungen` | Medium | Gotthold Eisenstein, *Mathematische Abhandlungen* | Source-intake packets exist without a promoted reader. | Select one work, bind the best source witness, and produce a reproducible page map. |
| `steiner-werke` | Medium | Jakob Steiner, *Gesammelte Werke* | Volume-source intake exists without a promoted transcription or translation. | Bind Volume I/II witnesses and select one bounded paper or range. |
| `takagi-source-intake` | Medium | Teiji Takagi, Journal of the College of Science volumes 19, 41, and 44 | A source-hunt ledger exists, but current routes are low-resolution aids or explicitly provisional. | Locate and bind exact BHL/Internet Archive JP2 source identities before choosing a bounded work. |

Future rows are invitations to prepare evidence, not claims that the corpus is
absent everywhere or that production should begin from an arbitrary web PDF.

## Mirror Workflow

1. Open the row's coverage map and source/reader roots. Do not infer absence
   from an unchecked label or missing cumulative PDF.
2. Choose a bounded author/work/range/language scope and record its exact
   starting cursor, input paths, hashes, and source authority.
3. Open one [adoption issue](https://github.com/KokunoYumeto/modern-latex-manuscripts/issues/new?template=adopt.yml)
   with the board ID and, if applicable, a mirror repository URL. This declares
   overlap; it does not reserve the work exclusively.
4. Preserve the source and predecessor generation. Add a new generation rather
   than overwriting contradictory or superseded evidence.
5. Produce a readable target plus editable source and a short manifest of
   paths, bytes, hashes, scope, status, and continuation cursor.
6. Run the checks appropriate to the claim: compile, source comparison,
   formula/diagram/table/reference checks, language review, and bounded visual
   inspection. Record failures and reversals as well as passes.
7. Compare with an independent mirror when one exists. Return exact corrections
   and reusable workflow findings; do not reduce disagreement to a winner label.
8. Submit a focused pull request or result issue. The archive map and this board
   are updated only when the corresponding bytes or exact external identity are
   inspectable.

## Machine Interface

The stable interface is
[`manifests/adopt.json`](../manifests/adopt.json), governed by the formal
[`adopt.schema.json`](../manifests/adopt.schema.json) contract and bounded
[`adopt.check.json`](../manifests/adopt.check.json) validation result. Its
`items` array defines:

- `id`, `author`, `work`, `series`, and `corpus`;
- `lane_state`, `coverage_state`, `adoption_status`, `priority`, and `readiness`;
- `owner`, `owner_scope`, and `languages`;
- `archive_path`, `related_paths`, and `source_basis`;
- `next_cursor`, `prerequisites`, `workflow`, and `claim_url`;
- `updated` and `notes`.

The top-level `mirrors` array records declared parallel work without forcing a
single exclusive owner. Each mirror row has `id`, `item_id`, `owner`, `scope`,
`url`, `status`, and `updated`. An empty array means no inspectable mirror has
yet been integrated into the board; it does not mean no one is working
elsewhere.

The top-level `map_manifest` points to the authoritative 19-map custody
manifest, and `required_maps` repeats its exact ordered path set. Validation
fails unless every required map is represented by at least one item's
`archive_path` or `related_paths`. This keeps the operational board additive to,
and synchronized with, the archival catalog instead of letting it become a
second incomplete inventory.

The top-level `queue_sources` similarly binds `docs/known-gaps.md` and
`docs/work-queue.md`. The top-level `snapshot_policy` defines the immutable
consumption boundary: a human-approved exact commit, four files fetched from
that same commit, declared byte/SHA-256 replay, empty validation errors, and
formal schema validation. Mixed revisions are forbidden.

The top-level `consumer_helper` points to
[`scripts/get-adopt.py`](../scripts/get-adopt.py). Run the helper from the same
human-approved checkout whose board is being considered. It requires the exact
40-hex commit twice, fetches only the four contract files at that commit,
replays their declared identities, validates the board with Draft 2020-12, and
emits the original validated board bytes to standard output. It never resolves
or accepts `main` as input:

```console
git switch --detach <COMMIT>
python scripts/get-adopt.py --commit <COMMIT> --approve <COMMIT> > board.json
```

The helper requires the Python `jsonschema` package. A nonzero exit means the
output must not be ingested.

Maintainers and independent auditors can replay the local board contract
without replacing the tracked validation file. `ValidationPath` remains the
canonical same-commit contract identity; `OutputPath` is only where this audit
run writes its report:

```powershell
./scripts/check-adopt.ps1 -OutputPath "$env:TEMP/adopt-check.json"
```

The temporary report must still return `status == "PASS"` and `errors == []`.
Changing `ValidationPath` changes the asserted contract and therefore fails
unless the board and snapshot policy declare that exact path.

Every human-facing work row starts with its exact `Board ID`. Validation fails
if a JSON item is missing from this page, appears more than once, or if the page
introduces an unknown ID. The issue template accepts that ID verbatim, so a
contributor never has to infer it from an author name or scrape the JSON.

The stable raw `main` endpoint is a discovery locator only. It is not an
immutable snapshot:

<https://raw.githubusercontent.com/KokunoYumeto/modern-latex-manuscripts/main/manifests/adopt.json>

Schema and current validation locators:

- <https://raw.githubusercontent.com/KokunoYumeto/modern-latex-manuscripts/main/manifests/adopt.schema.json>
- <https://raw.githubusercontent.com/KokunoYumeto/modern-latex-manuscripts/main/manifests/adopt.check.json>

Do not ingest directly from those three floating URLs. A safe consumer must:

1. Resolve `main` to one exact 40-character commit and require a human to
   approve that commit for ingestion.
2. Fetch `manifests/adopt.json`, `manifests/adopt.schema.json`,
   `manifests/adopt.check.json`, and the board's referenced `map_manifest` from
   that same exact commit, using commit-pinned raw URLs.
3. Require validation `status == "PASS"` and `errors == []`. Then replay the
   declared byte lengths and SHA-256 identities for the board, schema, and map
   manifest against the same-commit responses. The validation file itself is
   bound by the human-approved commit.
4. Validate the board against the fetched schema before exposing any row.
5. Reject mixed-revision inputs even when every individual URL returns 200 or
   one floating validation file says `PASS`.

`adopt.check.json.status == "PASS"` alone is never sufficient authorization
for automated ingestion. The commit is the snapshot boundary; `main` merely
helps a person discover a candidate commit.

Consumers should treat `lane_state` as the top-level partition and use
`priority` only within a partition. Preserve unknown fields, accept additional
enum values, key rows by `id`, and never reinterpret the board as the archive
inventory. Follow `archive_path` for the authoritative coverage claim. A mirror
can ingest the raw JSON, validate it against the stable schema, reject a feed
whose `adopt.check.json` status is not `PASS`, and materialize views by
`lane_state`, `priority`, `readiness`, `owner`, `author`, `work`, `series`,
`language`, or `corpus` without scraping this Markdown page.
