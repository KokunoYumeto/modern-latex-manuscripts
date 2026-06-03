# Zenodo Upgrade Sweep - 2026-06-03

Generated after the current GitHub mirror pass through the Cayley Volume IX `051_075` rhizic-curve/Cartesian diagram and formula repair.

## Publishing Capability

- No local Zenodo API token is currently available in `ZENODO_ACCESS_TOKEN`, `ZENODO_TOKEN`, `SANDBOX_ZENODO_ACCESS_TOKEN`, or `ZENODO_API_TOKEN`.
- This sweep therefore records what needs the next Zenodo version, but does not publish a new version.
- Large raw/source/provenance uploads should stay on the main landing/provenance record (`10.5281/zenodo.20393488`) rather than being repeatedly uploaded to every author/corpus satellite record.

## Public API Snapshot

Checked against the public Zenodo API on 2026-06-03.

| Lane | Concept record | Latest public DOI | Public version seen |
|---|---:|---|---|
| Main landing / raw provenance | 20393488 | `10.5281/zenodo.20458953` | 2026-06-01 landing/provenance refresh |
| Workflow packet | 20461174 | `10.5281/zenodo.20480520` | 2026-05-31 workflow packet |
| SGA | 20410947 | `10.5281/zenodo.20498621` | 2026-06-01 current SGA working record: SGA 6 through source page 525 |
| Noether | 20412587 | `10.5281/zenodo.20504343` | 2026-06-02 Noether record: complete French Paper 02 pilot |
| Non-European / multilingual | 20410957 | `10.5281/zenodo.20488731` | 2026-06-01 al-Battani table phase 5 |
| Ukrainian applied mathematics | 20490906 | `10.5281/zenodo.20498682` | 2026-06-01 engineering library public reader |
| Classical shelf: Cayley / Dedekind / Dirichlet | 20414787 | `10.5281/zenodo.20503771` | 2026-06-02 Cayley slices plus Dedekind/Dirichlet starts |
| Author cluster: Sylvester etc. | 20411006 | `10.5281/zenodo.20442003` | 2026-05-29 author cluster refresh |
| Gauss | 20410934 | `10.5281/zenodo.20503774` | 2026-06-02 Gauss cumulative readers plus Band II pilot |
| Weber | 20412153 | `10.5281/zenodo.20498553` | 2026-06-01 Weber through Volume I section 147 |
| Deligne | 20410853 | `10.5281/zenodo.20498666` | 2026-06-01 Manin 1987 letter sections 1 through 5 |

## Upgrade Queue

### 1. SGA - urgent

Public Zenodo is behind local/GitHub.

Local GitHub state:

- `reader-pdfs/sga/20 SGA 6 - Complete Strict Source-Checked Edition - English Translation.pdf`
- `reader-pdfs/sga/21 SGA 6 - Complete Strict Source-Checked Edition - French Reconstruction.pdf`
- `reader-pdfs/sga/39ZB` through `39ZD` final index segment and source-scan witness.
- `sources/sga/sga6-complete-source-checked-through-page-702-2026-06-02/`
- Manifest: `manifests/sga6_complete_source_checked_through_page702_20260602.md`

Action: publish a new SGA version using existing metadata `zenodo-metadata/metadata_satellite_sga_working_translation_public_current.json`, which already describes the complete page-702 SGA 6 edition.

### 2. Classical shelf - Cayley/Dedekind/Dirichlet

Public Zenodo predates the newest Cayley repairs and some current local GitHub reader hashes.

Local GitHub state now includes:

- Cayley Volume V rebuilt after native TikZ repair of four geometry figures in `501_525`.
- Recent Cayley repairs already pushed for Volumes II, IV, V, VI, VII, IX, X, XI, XII, and XIII.
- Latest Cayley status log: `manifests/cayley_current_duty_status_20260602.md`.
- Current Volume II reader hash: `cfc91d2cdf2d1ece6cdcf7427f7f4395a050ecb9709f014700d85712419c79c6` (312 pages; 4508460 bytes).
- Current Volume V reader hash: `74dcb274b1d39bc7fb22e19af4071545f8e1aba399f5f3c37f07f674bfd19097`.
- Current Volume III reader hash: `00545308a22e91efef1628be76e040d3c4f49d9787d16d65ca4bb7b5c79a4d5f` (322 pages; 3774202 bytes).
- Current Volume IX reader hash: `40a1aae1577d480833b12bd661df2baf1e06a184674c798ecb398006708d5151` (348 pages; 5211862 bytes).
- Current Volume X reader hash: `ef98957df8d0cfd1dded4fe553c9ea07ef5b8ef8a175eabee7707933f9f04a60` (575 pages; 6660654 bytes).
- Current Volume XI reader hash: `17da539f453a78d53eb8cad6a63d9d03e996afb8dec5d4d0838588436aa56e41` (415 pages; 4704908 bytes).
- Current Volume XII reader hash: `f018c62296595f43871ca153fba52030f937b8f9eafe5136fe3af58131c1624b`.

Action: publish a new classical-shelf version with current reader PDFs and the current status/manifest. Keep raw/provenance heavy bundles on the main landing record.

### 3. Noether

Public Zenodo is behind both the canonical numbered-paper completion and the multilingual lane.

Local/GitHub state:

- German/English numbered-paper readers through Paper 43 are present.
- Product-table patch is integrated as separate top-level readers (`54`, `55`) and in the canonical audit package.
- Spanish/Japanese GitHub readers are present through Paper 09.
- External local work has advanced further: `Noether Multilingual` contains Paper 10, Paper 11, and Paper 12 ES/JA packages dated 2026-06-02/03.
- Canonical final audit folder: `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether restart fidelity\Noether_FINAL_AUDIT_numbered_papers_complete_PATCHED`.

Action: first mirror Paper 10-12 ES/JA if accepted, then publish Noether with a clear split: numbered German/English complete; ES/JA pilot through the latest accepted paper; French pilot only where actually complete.

### 4. Ukrainian applied mathematics

Public Zenodo is behind local/GitHub.

Local GitHub state:

- Reader PDFs `13` through `17` add high-density state-estimation, ESKF, micro-Lie, VIO/SLAM, and practical Kalman-filtering material.
- Source packet: `sources/ukrainian-applied-math/high-density-state-estimation-lie-vio-kalman-2026-06-02/`.
- Metadata file `zenodo-metadata/metadata_satellite_ukrainian_applied_math_current.json` already describes the current high-density update.

Action: publish the Ukrainian record update as a normal mathematics/engineering translation update. Do not add special safety framing.

### 5. Non-European / multilingual

Public Zenodo is behind the al-Battani table work.

Latest external local candidates:

- `cleanup multilingual/round83_albattani_canonical_reference_v083`
- `cleanup multilingual/round82_albattani_canonical_reference_v082`
- `cleanup multilingual/round80_albattani_canonical_reference`
- `cleanup multilingual/round78_albattani_table_phase12_source_checked`
- `cleanup multilingual/non_eu_round75_albattani_table_phase9_text_only_transcription_nested`

Action: do not blindly upload the newest round. Curate the latest canonical al-Battani package against the table/source completeness requirement, then update the non-European record with the accepted reader-facing PDFs and compact TeX/work packets.

### 6. Author cluster / Sylvester

Public Zenodo is much older than local Sylvester.

Local state noted by external thread:

- Sylvester Volume I cumulative through book pp. 1-202 exists in `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Sylvester\sylvester_batch11`, with source PDF pp. 19-220 and source-page PNGs included.
- The local formula-crop assist workflow is useful as localization/checking support, not insertion-grade TeX.

Action: mirror the current accepted Sylvester cumulative readers and source packet into GitHub, then publish/update Sylvester as an author-level record rather than leaving it buried inside the general author cluster. Keep the cluster as a temporary shelf only for less mature starts.

### 7. Gauss / Dirichlet / Dedekind

Public Gauss and classical records are close but not necessarily current.

Recent external local paths include:

- `Gauss\gauss_nachlass_solutio_congruentiae_pp199_211_round09_20260602`
- `Dirichlet\Dirichlet_Round09_Rigid_Body_and_Gauss_Reciprocity_Clean_Cumulative_20260602`
- `dedekind\Dedekind_Round07_Dirichlet_Paratext_LVI_LIX_pp408_427_20260602`

Action: after Cayley priority work, compare these against GitHub and promote only clean cumulative readers/source packets.

### 8. Weber

Weber aid is currently outsourced and should not block Cayley.

Public Zenodo is at Volume I section 147. GitHub already has later local Weber material, and external work has moved into Volume II. Because the user explicitly marked Weber aid as outsourced, defer further Weber packaging until an accepted cumulative package is available.

### 9. Deligne

Many local Deligne drops exist, but the user has repeatedly flagged some as unreliable/trash.

Action: only publish Deligne updates after explicit curation of source-faithful packets. Do not promote new Deligne material simply because a folder exists.

## Recommended Publish Order Once Token Is Available

1. SGA complete page-702 update.
2. Classical shelf with current Cayley repairs.
3. Noether canonical numbered completion plus accepted ES/JA multilingual state.
4. Ukrainian high-density applied-math update.
5. Non-European al-Battani canonical/table update after source-completeness check.
6. Author cluster with Sylvester through the latest accepted cumulative.
7. Gauss / Dirichlet / Dedekind incremental updates.
8. Weber after outsourced package acceptance.
9. Deligne only after selective audit.
