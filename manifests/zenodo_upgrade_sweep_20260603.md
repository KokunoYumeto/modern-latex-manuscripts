# Zenodo Upgrade Sweep - 2026-06-03

Generated after the current GitHub mirror pass through the Cayley Volume X `451_475` theta-symbol diagram cluster repair, Noether Spanish/Japanese Paper 15 staging, and SGA 7-I source-page-96 staging.

## Publishing Capability

- A local Zenodo API token was located through the project helper after this sweep was written.
- The SGA and Noether priority updates were published as same-concept Zenodo versions on 2026-06-03.
- Large raw/source/provenance uploads should stay on the main landing/provenance record (`10.5281/zenodo.20393488`) rather than being repeatedly uploaded to every author/corpus satellite record.

## Public API Snapshot

Checked against the public Zenodo API on 2026-06-03.

| Lane | Concept record | Latest public DOI | Public version seen |
|---|---:|---|---|
| Main landing / raw provenance | 20393488 | `10.5281/zenodo.20458953` | 2026-06-01 landing/provenance refresh |
| Workflow packet | 20461174 | `10.5281/zenodo.20480520` | 2026-05-31 workflow packet |
| SGA | 20410947 | `10.5281/zenodo.20520554` | 2026-06-03 SGA update: SGA 6 complete through indexes/source pages 693-702 plus SGA7-I through source page 96 |
| Noether | 20412587 | `10.5281/zenodo.20520501` | 2026-06-03 Noether update: numbered German/English complete plus Spanish/Japanese through Paper 15 |
| Non-European / multilingual | 20410957 | `10.5281/zenodo.20488731` | 2026-06-01 al-Battani table phase 5 |
| Ukrainian applied mathematics | 20490906 | `10.5281/zenodo.20520721` | 2026-06-03 high-density applied-math continuation with current reader PDFs 00-17 |
| Classical shelf: Cayley / Dedekind / Dirichlet | 20414787 | `10.5281/zenodo.20503771` | 2026-06-02 umbrella shelf; dedicated Cayley, Dedekind, and Dirichlet author records now exist |
| Author cluster: Sylvester etc. | 20411006 | `10.5281/zenodo.20442003` | 2026-05-29 author cluster refresh |
| Gauss | 20410934 | `10.5281/zenodo.20503774` | 2026-06-02 Gauss cumulative readers plus Band II pilot |
| Weber | 20412153 | `10.5281/zenodo.20498553` | 2026-06-01 Weber through Volume I section 147 |
| Deligne | 20410853 | `10.5281/zenodo.20498666` | 2026-06-01 Manin 1987 letter sections 1 through 5 |

## Upgrade Queue

## Completed Publications

| Lane | Concept DOI | New version DOI | Files | Payload | Notes |
|---|---|---|---:|---:|---|
| SGA | `10.5281/zenodo.20410947` | `10.5281/zenodo.20520554` | 77 | 1,222,595,716 bytes | Same-concept update with SGA 6 complete through indexes/source pages 693-702 and SGA7-I through source page 96. |
| Noether | `10.5281/zenodo.20412587` | `10.5281/zenodo.20520501` | 91 | 569,212,865 bytes | Same-concept update with German/English numbered-paper completion plus ES/JA through Paper 15 and source/witness packets. |
| Cayley | `10.5281/zenodo.20520749` | `10.5281/zenodo.20520750` | 14 | 166,685,400 bytes | New dedicated author record with thirteen current volume-level slice readers and compact source/status ZIP. |

### 1. SGA - completed

Public Zenodo is behind local/GitHub.

Local GitHub state:

- `reader-pdfs/sga/20 SGA 6 - Complete Strict Source-Checked Edition - English Translation.pdf`
- `reader-pdfs/sga/21 SGA 6 - Complete Strict Source-Checked Edition - French Reconstruction.pdf`
- `reader-pdfs/sga/39ZB` through `39ZD` final index segment and source-scan witness.
- `sources/sga/sga6-complete-source-checked-through-page-702-2026-06-02/`
- `reader-pdfs/sga/53 SGA 7-I - Source-Checked Working Edition through Source Page 96 - English Translation.pdf`
- `reader-pdfs/sga/54 SGA 7-I - Source-Checked Working Edition through Source Page 96 - French Reconstruction.pdf`
- `reader-pdfs/sga/55 SGA 7-I - Source Scan Slice through Source Page 96.pdf`
- `sources/sga/sga7-i-source-checked-through-page-096-2026-06-03/`
- Manifest: `manifests/sga6_complete_source_checked_through_page702_20260602.md`

Action: published a new SGA version using existing metadata `zenodo-metadata/metadata_satellite_sga_working_translation_public_current.json`, now updated to describe the complete page-702 SGA 6 edition and the SGA 7-I source-page-96 continuation.

### 2. Classical shelf - Cayley/Dedekind/Dirichlet author split completed

Public Zenodo predates the newest Cayley repairs and some current local GitHub reader hashes.

Local GitHub state now includes:

- Cayley Volume V rebuilt after native TikZ repair of four geometry figures in `501_525`.
- Recent Cayley repairs already pushed for Volumes II, IV, V, VI, VII, IX, X, XI, XII, and XIII.
- Latest Cayley status log: `manifests/cayley_current_duty_status_20260602.md`.
- Current Volume I reader hash: `7b44f77ba13bfa88d7681a1647a08a917605870a908bbaf03cab4a31b59fec49` (488 pages; 7764737 bytes).
- Current Volume II reader hash: `040dc6861b761ba57e6462f1a8b53d239515a922f6d08bc0f02148ed4711095c` (312 pages; 4619547 bytes).
- Current Volume IV reader hash: `0038650fea73a7e1b92b3666bbfb5dfc75cb9d5c93ba6901a0cbfbeff5283ca5` (496 pages; 5880784 bytes).
- Current Volume V reader hash: `74dcb274b1d39bc7fb22e19af4071545f8e1aba399f5f3c37f07f674bfd19097`.
- Current Volume VII reader hash: `de5d4c4803c5671c278f2b1920fbe70ffb45852d9c09fcdbe1e29480f8c3c7a5` (336 pages; 4852925 bytes).
- Current Volume III reader hash: `00545308a22e91efef1628be76e040d3c4f49d9787d16d65ca4bb7b5c79a4d5f` (322 pages; 3774202 bytes).
- Current Volume IX reader hash: `40a1aae1577d480833b12bd661df2baf1e06a184674c798ecb398006708d5151` (348 pages; 5211862 bytes).
- Current Volume X reader hash: `0a4911bdd83baca668cf9b4d1e8381900c16c7a81ab10758b1448a4b6a244fa0` (575 pages; 6667301 bytes).
- Current Volume XI reader hash: `17da539f453a78d53eb8cad6a63d9d03e996afb8dec5d4d0838588436aa56e41` (415 pages; 4704908 bytes).
- Current Volume XII reader hash: `f018c62296595f43871ca153fba52030f937b8f9eafe5136fe3af58131c1624b`.
- Current Volume XIII reader hash: `c638a651e2010f3f873bcf337711a31ad29401e48c5d49762d8af0539ff9f7ff` (487 pages; 6125844 bytes).

Action: instead of refreshing the mixed shelf again, created dedicated Cayley, Dedekind, and Dirichlet author records. Keep raw/provenance heavy bundles on the main landing record and keep the mixed shelf as an umbrella/backstop.

### 3. Noether - completed

Public Zenodo is behind both the canonical numbered-paper completion and the multilingual lane.

Local/GitHub state:

- German/English numbered-paper readers through Paper 43 are present.
- Product-table patch is integrated as separate top-level readers (`54`, `55`) and in the canonical audit package.
- Spanish/Japanese GitHub readers are present through Paper 15.
- New front-facing readers `74` through `77` add cumulative Spanish/Japanese through Paper 15 and standalone Paper 15 Spanish/Japanese readers.
- Current source packet: `sources/noether/multilingual-spanish-japanese-through-paper15-complete-2026-06-03/`.
- Canonical final audit folder: `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether restart fidelity\Noether_FINAL_AUDIT_numbered_papers_complete_PATCHED`.

Action: published Noether with a clear split: numbered German/English complete; ES/JA multilingual lane through Paper 15 complete; French pilot only where actually complete.

### 4. Ukrainian applied mathematics - completed

Public Zenodo is behind local/GitHub.

Local GitHub state:

- Reader PDFs `13` through `17` add high-density state-estimation, ESKF, micro-Lie, VIO/SLAM, and practical Kalman-filtering material.
- Source packet: `sources/ukrainian-applied-math/high-density-state-estimation-lie-vio-kalman-2026-06-02/`.
- Metadata file `zenodo-metadata/metadata_satellite_ukrainian_applied_math_current.json` already describes the current high-density update.

Action: published the Ukrainian record update as a normal mathematics/engineering translation update. No special safety framing was added.

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

- Sylvester Volume I cumulative through book pp. 1-218 is mirrored in GitHub from `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Sylvester\sylvester_batch12`, with source PDF pp. 19-236 and source-page PNGs included.
- The local formula-crop assist workflow is useful as localization/checking support, not insertion-grade TeX.

Action: create a dedicated Sylvester author-level record rather than leaving it buried inside the general author cluster. Staged metadata: `zenodo-metadata/metadata_author_sylvester_current.json`. Keep the cluster as a temporary shelf only for less mature starts.

### 6a. Dedicated author-record split

The following dedicated author records should be created once an authenticated Zenodo API token is available. Until then, their material remains preserved in GitHub and the existing shelf records:

- **Arthur Cayley**: migrated to dedicated concept DOI `10.5281/zenodo.20520749`.
- **James Joseph Sylvester**: staged metadata `zenodo-metadata/metadata_author_sylvester_current.json`; promote Volume I through book page 218 and its source packet.
- **Richard Dedekind**: staged metadata `zenodo-metadata/metadata_author_dedekind_current.json`; promote `Was sind und was sollen die Zahlen?`, `Stetigkeit und irrationale Zahlen` segment, and Dedekind/Dirichlet paratext where appropriate.
- **P. G. Lejeune Dirichlet**: staged metadata `zenodo-metadata/metadata_author_dirichlet_current.json`; promote Werke Band II Papers I-XII.
- **Ernst Steinitz**: staged metadata `zenodo-metadata/metadata_author_steinitz_current.json`; promote after local bilingual Steinitz packets are checked and mirrored.

Once these are live, the existing mixed `Cayley, Dedekind, and Dirichlet` shelf and the `Author cluster` shelf should be retained as umbrella/backstop records, not treated as the clean reader-facing entry points.

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

1. SGA complete page-702 plus SGA 7-I source-page-96 update.
2. Noether canonical numbered completion plus ES/JA through Paper 15.
3. Classical shelf with current Cayley repairs, only as an interim umbrella.
4. Ukrainian high-density applied-math update.
5. Non-European al-Battani canonical/table update after source-completeness check.
6. Create dedicated Sylvester author record.
7. Create/migrate dedicated Cayley, Dedekind, Dirichlet, and Steinitz author records where the source surface is mature enough.
8. Gauss incremental update.
9. Weber after outsourced package acceptance.
10. Deligne only after selective audit.
