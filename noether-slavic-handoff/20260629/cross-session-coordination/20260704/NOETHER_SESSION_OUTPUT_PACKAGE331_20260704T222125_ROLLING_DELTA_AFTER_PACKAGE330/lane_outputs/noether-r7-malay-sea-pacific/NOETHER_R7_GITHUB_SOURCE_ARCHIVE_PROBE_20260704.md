# Noether R7 Malay-Indonesian/SEA-Pacific GitHub Source-Archive Probe

Date: 2026-07-04

Scope: source-canon/provenance only. This pass searched for source-level mathematical corpus witnesses for Malay, Indonesian, Brunei/Singapore Malay, and SEA/Pacific target rows. It does not translate, approve terms, claim native review, claim canonical approval, clear licenses, promote gates, or push Git.

Primary row table:

- `NOETHER_R7_GITHUB_SOURCE_ARCHIVE_PROBE_ROWS_20260704.csv`

Method:

- Used `gh search code` against public GitHub TeX blobs with Malay/Indonesian/SEA-Pacific algebra terms.
- Kept searches manifest-only: no raw TeX/source bodies were downloaded into the lane.
- Used GitHub tree metadata for blob SHA and byte counts where a candidate path was present in a public tree.
- Used `gh repo view` metadata for public/private/fork/license signals.
- Preserved false positives and search gaps as rows, because the source-canon lane needs explicit absence/blocker evidence, not silent omissions.

## Summary Counts

- Total rows: 19.
- Source-level TeX/blob metadata rows: 14.
- Explicit gap/blocker rows: 5.
- Direct target-math candidates: 3.
- Limited-topic candidates: 6.
- False-positive/context-only rows: 5.
- Raw source bodies downloaded: 0.
- Upload policy on every row: `manifest_only_no_raw_source_body_payload_for_language_lane`.

## Candidate Rows

Direct target-math candidates:

- `R7GH003`: `KlinikAA/ONMIPA`, `ONMIPA Nasional/Soal/ONMIPA Nasional.tex`, Git blob SHA `3aba757d28f98b45df0042f1b6c2610ff6eeef16`, 70515 bytes. Query hits included `gelanggang`, `ideal gelanggang`, `modul gelanggang`, `aljabar gelanggang`, and `matematik gelanggang`. Public GitHub repo; no GitHub licenseInfo detected.
- `R7GH004`: `KlinikAA/ONMIPA`, `ONMIPA Wilayah/Soal/ONMIPA Wilayah.tex`, Git blob SHA `d1dae4f65ee2c1e9a6899b7f685b8b25c24350fb`, 210314 bytes. Same algebra-term query cluster. Public GitHub repo; no GitHub licenseInfo detected.
- `R7GH005`: `TetewHeroez/Tugas-Kuliah`, `Semester 8/Metode Penelitian/Proposal Tesis/Inti/bab 2.tex`, Git blob SHA `795c5b27d8490b0751249498dd36cd610131c213`, 27164 bytes. Query hits included `gelanggang`, `ideal gelanggang`, `aljabar gelanggang`, and `matematik gelanggang`. Public GitHub repo; no GitHub licenseInfo detected.

Limited-topic source candidates:

- `R7GH002`: `TetewHeroez/Olympiad`, UGM selection TeX source. Contest/problem source, not specialist Noether/ring/module authority.
- `R7GH006`: `TetewHeroez/Tugas-Kuliah`, final-project Bab 2 TeX source. Invariant/algebra term candidate; exact relevance still source-gated.
- `R7GH007`: `rafikamindra98/Materi-Coolyeah`, `Aljabar Linear` eigen-space source. Indonesian linear-algebra material; not ring/module/Noether specialist evidence.
- `R7GH008`: `IRK-23/algeo2-frontendbackenddeadend`, `docs/main.tex`. Classroom/project TeX candidate with MIT repo license signal; exact mathematical terminology remains source-gated.
- `R7GH010`: `kurniawanchandraw/Undergraduate_Thesis`, `Backup Bab 2.tex`. Thesis TeX candidate; exact algebra relevance and license remain blocked.
- `R7GH011`: `indahswj/FILE-APLIKOM`, `EMT ALJABAR...tex`. Indonesian assignment source candidate surfaced by a Brunei query; keep out of Brunei/Singapore rows.

Context-only or false-positive source rows:

- `R7GH001`: `mesolitica/research-paper`, `malaysian-mistral/neurips_2023.tex`. Malay/Malaysian NLP context, not algebra corpus authority.
- `R7GH009`: `birrulwldain/skripsi-21`, `catatan.tex`. Physics thesis context, not algebra corpus authority under current evidence.
- `R7GH012`: `lutfi-r/Aplikasi-Komputer`, assignment TeX source. Indonesian coursework false positive for Brunei/Singapore source return.
- `R7GH013` and `R7GH014`: `chenxingqiang/thinkbase-project`, Noetherian/ring search hits. Not target-language Malay/Indonesian source canon.

## Gaps And Blockers

- `R7GHG01`: Malay/Malaysian algebra TeX source gap. `Malaysia gelanggang` found a Malay NLP/preprint context row, but no Malay algebra/ring/module source witness in this pass.
- `R7GHG02`: target-language Noetherian/ring TeX exact source gap. `Noetherian Indonesia` and `ring Noetherian Indonesia` returned non-target/AI-output context only.
- `R7GHG03`: Brunei/Singapore Malay math TeX source gap. `Singapura matematik aljabar` returned zero TeX hits; `Brunei matematik aljabar` returned Indonesian assignment false positives.
- `R7GHG04`: Tagalog/Filipino higher-algebra TeX source gap. Queries returned CV/NLP/security/template false positives, not target-language mathematical algebra publication sources.
- `R7GHG05`: GitHub legacy code-search blocker. A rapid quoted query batch hit HTTP 403; smaller unquoted batches succeeded. Future searches should throttle and use simple query syntax.

## Boundary

These rows are source-canon/provenance candidates and gap records only. They are not translation evidence, term approval, review evidence, license clearance, gate promotion, canonical approval, or completion proof. Any row with a source-level TeX candidate still needs exact content capture and license/access handling before downstream use.
