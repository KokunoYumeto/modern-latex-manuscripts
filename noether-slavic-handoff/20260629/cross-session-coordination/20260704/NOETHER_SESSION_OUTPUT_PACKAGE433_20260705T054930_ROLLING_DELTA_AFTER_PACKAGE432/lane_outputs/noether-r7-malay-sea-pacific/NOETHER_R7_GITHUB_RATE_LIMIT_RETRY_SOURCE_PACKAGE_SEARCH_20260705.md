# Noether R7 GitHub Rate-Limit Retry Source-Package Search - 2026-07-05

Scope: source-canon/provenance only. This packet closes the prior GitHub code-search rate-limit gap for the strongest Malay-Indonesian publication and Malaysian Malay course/JQMA clusters. It does not translate, approve terms, claim native review, claim canonical approval, clear licenses, promote gates, claim completion, or push Git.

Rows:

- CSV: `NOETHER_R7_GITHUB_RATE_LIMIT_RETRY_SOURCE_PACKAGE_SEARCH_ROWS_20260705.csv`
- Row count: 13
- Payload policy: no raw TeX/PDF/source bodies were downloaded or stored in `outputs`; GitHub evidence is query status, repository metadata, tree metadata, blob SHA, URL, and explicit gap status only.

## Method

The GitHub search rate bucket was rechecked before this pass and had a fresh budget. The first diagnostic loops that used the wrong CLI method/path were discarded and not treated as evidence. The clean run used `gh api --method GET` against `search/code` and `search/repositories`, with exact quoted title/query clusters and small `per_page` limits.

## Clean Search Findings

- Exact GitHub code and repository searches returned zero hits for 9 of 11 clusters.
- `Struktur Aljabar` / `Teori Ring` returned one repository hit: `nuraeniAy/Struktur-Aljabar`. GitHub API metadata shows the repository is empty/no branch tree is available, so it is not a usable source package.
- `Ideal Prima` / `Ideal Maksimal` / `Gelanggang` returned two code hits in `KlinikAA/ONMIPA`, already known as adjacent ONMIPA TeX context. These are source-level TeX metadata rows, but they are not source packages for the UNHAS publication or any target article.
- JQMA 2025 Malay title cluster, UPM `MTH4201`, and UPM `MTH4205` clusters returned zero code and repository hits.

## Source-Level Metadata Captured

`KlinikAA/ONMIPA` metadata:

- Repository: `https://github.com/KlinikAA/ONMIPA`
- Default branch: `main`
- Commit: `630d0ad535e39ee7a2a1e9225a725eca4517b08b`
- Tree: `6878ca061fa6d04c2dc3a538fdbd9c3b3cc6656e`
- Tree summary: 25 paths; 5 TeX files; 9 PDF files; tree not truncated.
- Relevant blob SHAs from search/tree metadata:
  - `ONMIPA Nasional/Soal/ONMIPA Nasional.tex`: `3aba757d28f98b45df0042f1b6c2610ff6eeef16`
  - `ONMIPA Wilayah/Soal/ONMIPA Wilayah.tex`: `d1dae4f65ee2c1e9a6899b7f685b8b25c24350fb`
- License signal: no GitHub license detected; no license clearance claimed.

`nuraeniAy/Struktur-Aljabar` metadata:

- Repository: `https://github.com/nuraeniAy/Struktur-Aljabar`
- Default branch field: `main`
- GitHub API branch/tree status: branch not found / Git repository empty.
- License signal: no GitHub license detected; no license clearance claimed.
- Disposition: empty-repository discovery context only.

## Boundary

This retry removes the previous rate-limit ambiguity but does not change downstream authority. The strongest publication shelf still lacks matching TeX/LaTeX/e-print/source archive packages. The ONMIPA rows remain adjacent context; the empty `Struktur-Aljabar` repository remains a false lead; zero-result rows remain explicit source-package gaps.

No source body was downloaded, no license was cleared, and no row is translation evidence or term approval.
