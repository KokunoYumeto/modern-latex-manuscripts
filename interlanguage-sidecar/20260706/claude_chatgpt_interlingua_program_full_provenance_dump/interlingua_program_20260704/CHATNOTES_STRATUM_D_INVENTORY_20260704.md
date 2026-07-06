# Chatnotes Stratum-D Inventory
2026-07-04. Root: `Papors\Chatnotes\CHat translates and clean\`. Scan: [chatnotes_stratum_d_scan_20260704.json](chatnotes_stratum_d_scan_20260704.json) (filename-tag language detection; counts include build artifacts and renders — treat as upper bounds; language tags are heuristic).

**Totals: 827,329 files, ~914 GB, 37 folders.** This is the "language triangulation database" Floris described: AI-era translation drafts across ≥14 languages and ~25 historical authors. All of it Stratum-D discipline: draft-linked, compaction-risk, never witnesses without verification.

## Language coverage by folder (headline rows)

| Folder | Scale | Language signals (file-tag counts) |
| --- | --- | --- |
| Noether Multilingual | 296K files / 376GB / 37.8K tex | de 32K · isv 15.9K · en 14.4K · ru 12.4K · uk 12K · **fr 7K · zh 1.7K · ar 1.5K** |
| ukranian lane | 84K / 12.7GB | **fr 3.1K** · de 580 · uk 575 · **es 267 · ar 167 · it 154** |
| Kimi | 57K / 62.6GB | fr 123 · ar 72 · la 12 · sa 2 |
| deligne restart + Delignbe | 37.6K | en+fr balanced (~3.4K/3.4K + 437/413) · de 1.9K · ru 515 |
| Weber restart + fidelity pass | 31.9K | en 3K · de 1.5K · **ar 912** |
| translations/ | 25.8K | en 3.6K · fr 1K · ar 382 |
| Bianchi | 23K | **it 1792** ↔ en 1844 (Italian pair corpus) |
| cleanup multilingual | 22.5K | **ja 1784 · ar 740 · zh 544 · sa 32** (the CJK/Arabic/Sanskrit node) |
| SGA restart + continuation 2 + high-fidelity | 31.6K | fr 5.6K ↔ en 2.9K |
| Poincare / Picard / Steinitz / Dirichlet | 39.6K | fr pairs (831/410/368/191) |
| Kneser / Gordan / Frobenius / Klein-Fricke / Kron / Kronecker | 62K | de↔en pairs (1.2–1.8K each side) |
| Mikami + Seki | 20.7K / 73GB | **ja 864** (Japanese mathematics-history pairs) |
| Gauss | 4.3K / 20GB | en 915 · **ar 257 · la 31** |
| Cayley | 19.3K / 27GB / 3.3K tex | de 356 · **ja 39** |
| Sylvester | 5.9K | en only (source-side) |
| Noether restart fidelity | 1.7K | en 629 · de 398 · **es 41 · ja 34** |
| author_aid_packages_20260603 | 3.4K | de 2K (aid packages) |

## What this changes for the program

1. **The witness-language pool is far wider than the four lanes**: Italian (Bianchi), Japanese (Mikami/Seki/cleanup), Chinese + Sanskrit (cleanup multilingual), Arabic (Weber/Gauss/cleanup), Latin (Gauss), Spanish (ukrainian-lane spillover + Noether fidelity + ES/JA zip). Each is draft-grade but *localizes* where witness extraction should start per language.
2. **Per-author × language matrix is buildable from tags alone** — the atlas's F7 interlock generalizes: not just French×3; Italian has Bianchi as its anchor author, Japanese has Mikami/Seki, Arabic has Weber/Gauss drafts. Future spine columns get an anchor-author source each.
3. **ES/JA extraction plan (for spine columns 7–8):** primary ES = noether-pc branch `r1_spanish` lane (source-native audited, p01–p43) + `Noether_Papers36_39_ES_JA_20260604.zip`; primary JA = the same zip + `cleanup multilingual` ja files + Mikami/Seki pairs. Extraction = term-level only (spine concepts), through the concept ledger, entering as linked/draft — NOT witnessed (AI translations are not native witnesses; they are candidate-form donors and consistency checks).
4. **Caveats stay loud:** compaction-era drafts; counts inflated by renders/build trees; the 376GB Noether Multilingual folder needs a dedup pass before any per-file work is planned there.
