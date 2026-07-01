# SGA

Zenodo record: [20822648](https://doi.org/10.5281/zenodo.20410947)

Public title: Seminaire de Geometrie Algebrique (SGA): Working Translation and Source-Audit Drafts

**Quality warning:** This generated page lists public files and current record notes. It does not certify a critical edition. Legacy filenames can include terms such as `Complete`, `Strict`, `Source-Checked`, or `Critical`; use the status notes, source witnesses, and audit ledgers before relying on mathematical details.

| Files | PDFs | ZIPs | Total MB |
|---:|---:|---:|---:|
| 100 | 74 | 25 | 3306.5 |

## How To Read This Record

Open the reader/reference PDFs first. Use artifact ZIPs when you need TeX, source witnesses, OCR, page images, render checks, or provenance material.

Current caveat from the 2026-06-24 SGA audit-support updates, with 2026-06-26 hand-audit reconciliation: the latest published record is DOI 10.5281/zenodo.20822648. SGA5 is explicitly not certified complete. The latest local compact SGA5 control delta is SGA5_FullAudit_WebDrop_p260_p265_workpass_delta_20260626.zip, which advances the page-local French workpass/source-audit boundary from p259 to p265 and sets p266 as the next cursor. The larger SGA5_FullAudit_WebDrop_p001_p254_certified_staged_p255_p484_20260626.zip remains provenance/source-witness material, and the p255-p259 compact delta is preserved as superseded cursor/provenance. The p260-p265 delta preserves the current workpass TeX/PDF/log snapshot, CERT_LOG/AGENT_SCORECARD, method/status notes, source crops for p260-p265, inventory, and checksums. The included workpass compiles to a 307-page PDF. p260-p265 cover Expose VI Remarque after Prop. 1.2.5, Prop. 1.2.6 and proof, tensor products, Prop. 1.3.2, cHom, invertibles/Tate twist, A-faisceaux, D143 (the A-action square), and the opening of Q_l-faisceaux. p266 and later crops/cursor text are active/pending scratch only and are not promoted by this delta. The p69 scope note clarifies that the source scan is the full 484-page LNM 589, but the local TeX is a curated 10-expose selection (I, III, IIIB, V, VI, VII, VIII, X, XII, XV); current p1-p265 evidence is opening-range workpass evidence, not global SGA5 certification. Local ledger terms such as certified/clean/complete are interpreted as page-local workpass status only. This is preservation/support evidence for ongoing repair, not a certified edition, not an independently packaged or promoted edition, not English synchronization, and not closure of diagram/formula/notation/typography queues. Treat SGA6 and SGA7 as substantial working drafts with explicit compression caveats unless a specific packet declares source-checked coverage. Older filenames containing words such as Complete, Source-Checked, Strict, or High-Fidelity are legacy package names, not current global certification. Witness-aid ZIPs are source-witness/anchor aids, not authority by themselves.

2026-07-01 local audit follow-up: the local SGA5 hand-audit/workpass ledger under `SGA continuation 2/_claude_aid/sga5_full_audit_20260623` has advanced through Exposé V around book p.234. The latest `CERT_LOG.md` and `AGENT_SCORECARD.md` are recorded in `manifests/source-intake/20260701_sga5_full_audit_p234_local_log_update.md/json`; the earlier p227 checkpoint remains preserved as provenance. The p234 scorecard reports 234 pages inspected, 21 TeX fixes plus one cosmetic fix, 38 source typos tracked, 8 TeX content errors found and fixed, and 136 diagrams tracked. This is a live local audit/provenance update only; it is not a new promoted reader package, not SGA5 completion, not English synchronization, and not critical-edition material. A compact package should be built before any Zenodo upload.

2026-07-01 later local audit follow-up: `manifests/source-intake/20260701_sga5_full_audit_p270_certlog_update.md/json` records that `CERT_LOG.md` in the same local SGA5 workpass folder now has 270 completed page rows, with p270 covering Exposé VI §1.4.6 fin, §1.4.7 on `L`-faisceaux, and the opening of §1.5 on `(AR,Z_l)`-faisceaux. The companion `AGENT_SCORECARD.md` changed too, but its extracted page-header inventory currently has 265 headers with maximum page header p269, and the compiled `sga5_fr_workpass.pdf` hash is unchanged from the p234 checkpoint. Treat this as a ledger/provenance advance only, not a promoted compact delta, not SGA5 completion, not English synchronization, and not critical-edition material.

2026-07-01 later local audit follow-up: `manifests/source-intake/20260701_sga5_full_audit_p271_certlog_update.md/json` records the next `CERT_LOG.md` checkpoint, now with 271 completed page rows. p271 covers Exposé VI §1.5 on `(AR,Z_l)`-faisceaux: the end of Definition 1.5.1, abelianity/stability under kernels and cokernels, §1.5.2 on locally AR-null objects, and the opening of Definition 1.5.3. The companion scorecard now exposes 267 page headers with maximum page header p271, and the local workpass PDF was rebuilt to 307 pages after the ledger update. Treat this as the latest live ledger/provenance marker only; do not promote it as a compact delta or SGA5 certification.

2026-07-01 latest local audit follow-up: `manifests/source-intake/20260701_sga5_full_audit_p274_certlog_update.md/json` records the current `CERT_LOG.md` checkpoint, now with 274 completed page rows. p272 closes Exposé VI §1.5 and records notation normalization `(AR-Z_l)` to `(AR,Z_l)` already present in the rebuilt workpass; p273 opens Exposé VI §2 and checks §2.1 on inverse image `f^*`; p274 checks §2.2 on higher direct images with proper support, Lemmas 2.2.1/2.2.2, and the exact delta-functor `R^i f_!`. The local TeX/PDF/log hashes remain those of the p271 rebuild, and `pdfinfo` reports a 307-page workpass PDF. p275 and later source renders/crops remain cursor/scratch material. Treat this as the latest live ledger/provenance marker only; do not promote it as a compact delta, SGA5 completion, English synchronization, or critical-edition material.

2026-07-01 latest local audit follow-up: `manifests/source-intake/20260701_sga5_full_audit_p275_certlog_update.md/json` records the current `CERT_LOG.md` checkpoint, now with 275 completed page rows. p275 checks Exposé VI §2.2 through Definition 2.2.3, the following remark, and the opening of Proposition 2.2.4 on the Leray spectral sequence. It records `.tex` fix #23 at line 8861, restoring the source-faithful operator-prefix form `R^i_!g(R^j_!f(F)) => R^{i+j}_!(g \circ f)(F)` in place of one modernized statement form. `pdfinfo` reports a 307-page workpass PDF, and the companion scorecard has caught up to the p275 row. The p276 checkpoint is recorded separately below; later source renders remain cursor/scratch material. Treat this as the latest live ledger/provenance marker only; do not promote it as a compact delta, SGA5 completion, English synchronization, or critical-edition material.

2026-07-01 latest local audit follow-up: `manifests/source-intake/20260701_sga5_full_audit_p276_certlog_update.md/json` records the current `CERT_LOG.md` checkpoint, now with 276 completed page rows. p276 checks Exposé VI Proposition 2.2.4, the core of the Leray spectral-sequence proof: `Sp(C)`, the ordinary Leray spectral sequence prolonged to projective systems, the `(S)` spectral sequence, compatibility with `(1)`, `(2)`, `(3)`, and biregularity. `pdfinfo` reports a 307-page workpass PDF. No new TeX change is recorded for p276; the p275 source-faithful operator-prefix repair remains the latest TeX change. Treat this as the latest live ledger/provenance marker only; do not promote it as a compact delta, SGA5 completion, English synchronization, or critical-edition material.

2026-07-01 latest local audit follow-up: `manifests/source-intake/20260701_sga5_full_audit_p320_certlog_update.md/json` records the current live SGA5 workpass checkpoint, now with 320 completed page rows. p318 opens Exposé VII §7 `Intersections complètes` and the Lefschetz theorem statement; p319 checks Lemme 7.1.1, the proof of Théorème 7.1(ii), Remarque 7.1.3, and closes the Lefschetz proof; p320 checks Corollaire 7.2 on the `Z_l` Lefschetz theorem, its proof, and the opening of Lemme 7.2.1. The local workpass PDF compiles to 307 pages and p321 is the next cursor. Treat this as the latest live ledger/provenance marker only; do not promote it as a compact delta, SGA5 completion, English synchronization, or critical-edition material.

**Legacy filename warning before the file list:** the SGA5 source-scan filename and the SGA6 reader/source filenames below still contain phrases such as `Complete High-Fidelity`, `Complete Strict`, and `Source-Checked Edition`. Those strings are preserved Zenodo filenames, not current maintainer claims. Current status is governed by the caveat above.

Corrections, source comparisons, LaTeX fixes, and translation improvements can be suggested through GitHub issues or pull requests: <https://github.com/KokunoYumeto/modern-latex-manuscripts>.

## Reader And Reference PDFs

| Size MB | File |
|---:|---|
| 1.5375 | [01 SGA 5 - Current English Working Draft unsynchronized carry-forward.pdf](https://zenodo.org/records/20822648/files/01%20SGA%205%20-%20Current%20English%20Working%20Draft%20unsynchronized%20carry-forward.pdf) |
| 5.0861 | [02 SGA 3 - Existing English Translation Clean Rebuild.pdf](https://zenodo.org/records/20822648/files/02%20SGA%203%20-%20Existing%20English%20Translation%20Clean%20Rebuild.pdf) |
| 1.6048 | [02 SGA 5 - Current French Working Draft with repair012 patches.pdf](https://zenodo.org/records/20822648/files/02%20SGA%205%20-%20Current%20French%20Working%20Draft%20with%20repair012%20patches.pdf) |
| 54.9596 | [03 SGA 5 - Exact Source Scan for Complete High-Fidelity Edition.pdf](https://zenodo.org/records/20822648/files/03%20SGA%205%20-%20Exact%20Source%20Scan%20for%20Complete%20High-Fidelity%20Edition.pdf) |
| 1.2002 | [10 SGA 1 - Existing English Translation Snapshot.pdf](https://zenodo.org/records/20822648/files/10%20SGA%201%20-%20Existing%20English%20Translation%20Snapshot.pdf) |
| 0.7950 | [11 SGA 2 - Existing English Translation Snapshot.pdf](https://zenodo.org/records/20822648/files/11%20SGA%202%20-%20Existing%20English%20Translation%20Snapshot.pdf) |
| 2.0727 | [13 SGA 4 - English Translation Working Draft.pdf](https://zenodo.org/records/20822648/files/13%20SGA%204%20-%20English%20Translation%20Working%20Draft.pdf) |
| 1.9559 | [20 SGA 6 - Complete Strict Source-Checked Edition - English Translation.pdf](https://zenodo.org/records/20822648/files/20%20SGA%206%20-%20Complete%20Strict%20Source-Checked%20Edition%20-%20English%20Translation.pdf) |
| 1.9176 | [21 SGA 6 - Complete Strict Source-Checked Edition - French Reconstruction.pdf](https://zenodo.org/records/20822648/files/21%20SGA%206%20-%20Complete%20Strict%20Source-Checked%20Edition%20-%20French%20Reconstruction.pdf) |
| 51.7662 | [22 SGA 6 - Exact Source Scan for Complete Strict Edition.pdf](https://zenodo.org/records/20822648/files/22%20SGA%206%20-%20Exact%20Source%20Scan%20for%20Complete%20Strict%20Edition.pdf) |
| 0.2749 | [23 SGA 6 - Expose III Perfection and Semicontinuity Pages 253-280 - French Reconstruction.pdf](https://zenodo.org/records/20822648/files/23%20SGA%206%20-%20Expose%20III%20Perfection%20and%20Semicontinuity%20Pages%20253-280%20-%20French%20Reconstruction.pdf) |
| 0.2864 | [24 SGA 6 - Expose III Perfection and Semicontinuity Pages 253-280 - English Translation.pdf](https://zenodo.org/records/20822648/files/24%20SGA%206%20-%20Expose%20III%20Perfection%20and%20Semicontinuity%20Pages%20253-280%20-%20English%20Translation.pdf) |
| 2.1724 | [25 SGA 6 - Source Scan Slice for Expose III Pages 253-280.pdf](https://zenodo.org/records/20822648/files/25%20SGA%206%20-%20Source%20Scan%20Slice%20for%20Expose%20III%20Pages%20253-280.pdf) |
| 0.3053 | [26 SGA 6 - Expose IV Grothendieck Groups Pages 281-303 - French Reconstruction.pdf](https://zenodo.org/records/20822648/files/26%20SGA%206%20-%20Expose%20IV%20Grothendieck%20Groups%20Pages%20281-303%20-%20French%20Reconstruction.pdf) |
| 0.3041 | [27 SGA 6 - Expose IV Grothendieck Groups Pages 281-303 - English Translation.pdf](https://zenodo.org/records/20822648/files/27%20SGA%206%20-%20Expose%20IV%20Grothendieck%20Groups%20Pages%20281-303%20-%20English%20Translation.pdf) |
| 1.6939 | [28 SGA 6 - Source Scan Slice for Expose IV Pages 281-303.pdf](https://zenodo.org/records/20822648/files/28%20SGA%206%20-%20Source%20Scan%20Slice%20for%20Expose%20IV%20Pages%20281-303.pdf) |
| 0.2831 | [29 SGA 6 - Expose V Lambda Rings Opening Pages 304-330 - French Reconstruction.pdf](https://zenodo.org/records/20822648/files/29%20SGA%206%20-%20Expose%20V%20Lambda%20Rings%20Opening%20Pages%20304-330%20-%20French%20Reconstruction.pdf) |
| 0.7989 | [30 SGA 5 - Current English Working Draft from Available Segments.pdf](https://zenodo.org/records/20822648/files/30%20SGA%205%20-%20Current%20English%20Working%20Draft%20from%20Available%20Segments.pdf) |
| 0.2944 | [30 SGA 6 - Expose V Lambda Rings Opening Pages 304-330 - English Translation.pdf](https://zenodo.org/records/20822648/files/30%20SGA%206%20-%20Expose%20V%20Lambda%20Rings%20Opening%20Pages%20304-330%20-%20English%20Translation.pdf) |
| 1.8639 | [31 SGA 6 - Source Scan Slice for Expose V Pages 304-330.pdf](https://zenodo.org/records/20822648/files/31%20SGA%206%20-%20Source%20Scan%20Slice%20for%20Expose%20V%20Pages%20304-330.pdf) |
| 0.7016 | [32 SGA 7-I - Current English Working Draft through Expose IX Section 6.6.pdf](https://zenodo.org/records/20822648/files/32%20SGA%207-I%20-%20Current%20English%20Working%20Draft%20through%20Expose%20IX%20Section%206.6.pdf) |
| 0.4235 | [33 SGA 7-I - Expose VII Section 2.3 to Expose IX Section 6.6 Continuation.pdf](https://zenodo.org/records/20822648/files/33%20SGA%207-I%20-%20Expose%20VII%20Section%202.3%20to%20Expose%20IX%20Section%206.6%20Continuation.pdf) |
| 0.2579 | [34 SGA 6 - Expose V Pages 331-353 - French Reconstruction.pdf](https://zenodo.org/records/20822648/files/34%20SGA%206%20-%20Expose%20V%20Pages%20331-353%20-%20French%20Reconstruction.pdf) |
| 0.2566 | [35 SGA 6 - Expose V Pages 331-353 - English Translation.pdf](https://zenodo.org/records/20822648/files/35%20SGA%206%20-%20Expose%20V%20Pages%20331-353%20-%20English%20Translation.pdf) |
| 1.6395 | [36 SGA 6 - Source Scan Slice for Expose V Pages 331-353.pdf](https://zenodo.org/records/20822648/files/36%20SGA%206%20-%20Source%20Scan%20Slice%20for%20Expose%20V%20Pages%20331-353.pdf) |
| 0.2742 | [37 SGA 6 - Expose V Pages 354-371 - French Reconstruction.pdf](https://zenodo.org/records/20822648/files/37%20SGA%206%20-%20Expose%20V%20Pages%20354-371%20-%20French%20Reconstruction.pdf) |
| 0.2719 | [38 SGA 6 - Expose V Pages 354-371 - English Translation.pdf](https://zenodo.org/records/20822648/files/38%20SGA%206%20-%20Expose%20V%20Pages%20354-371%20-%20English%20Translation.pdf) |
| 1.2499 | [39 SGA 6 - Source Scan Slice for Expose V Pages 354-371.pdf](https://zenodo.org/records/20822648/files/39%20SGA%206%20-%20Source%20Scan%20Slice%20for%20Expose%20V%20Pages%20354-371.pdf) |
| 0.2258 | [39A SGA 6 - Expose VI Pages 372-396 - French Reconstruction.pdf](https://zenodo.org/records/20822648/files/39A%20SGA%206%20-%20Expose%20VI%20Pages%20372-396%20-%20French%20Reconstruction.pdf) |
| 0.2248 | [39B SGA 6 - Expose VI Pages 372-396 - English Translation.pdf](https://zenodo.org/records/20822648/files/39B%20SGA%206%20-%20Expose%20VI%20Pages%20372-396%20-%20English%20Translation.pdf) |
| 1.8891 | [39C SGA 6 - Source Scan Slice for Expose VI Pages 372-396.pdf](https://zenodo.org/records/20822648/files/39C%20SGA%206%20-%20Source%20Scan%20Slice%20for%20Expose%20VI%20Pages%20372-396.pdf) |
| 0.3100 | [39D SGA 6 - Expose VI Pages 397-422 - French Reconstruction.pdf](https://zenodo.org/records/20822648/files/39D%20SGA%206%20-%20Expose%20VI%20Pages%20397-422%20-%20French%20Reconstruction.pdf) |
| 0.3087 | [39E SGA 6 - Expose VI Pages 397-422 - English Translation.pdf](https://zenodo.org/records/20822648/files/39E%20SGA%206%20-%20Expose%20VI%20Pages%20397-422%20-%20English%20Translation.pdf) |
| 1.9663 | [39F SGA 6 - Source Scan Slice for Expose VI Pages 397-422.pdf](https://zenodo.org/records/20822648/files/39F%20SGA%206%20-%20Source%20Scan%20Slice%20for%20Expose%20VI%20Pages%20397-422.pdf) |
| 0.2460 | [39G SGA 6 - Expose VII Regular Immersions and Blowups Pages 423-454 - French Reconstruction.pdf](https://zenodo.org/records/20822648/files/39G%20SGA%206%20-%20Expose%20VII%20Regular%20Immersions%20and%20Blowups%20Pages%20423-454%20-%20French%20Reconstruction.pdf) |
| 0.2426 | [39H SGA 6 - Expose VII Regular Immersions and Blowups Pages 423-454 - English Translation.pdf](https://zenodo.org/records/20822648/files/39H%20SGA%206%20-%20Expose%20VII%20Regular%20Immersions%20and%20Blowups%20Pages%20423-454%20-%20English%20Translation.pdf) |
| 2.5520 | [39I SGA 6 - Source Scan Slice for Expose VII Pages 423-454.pdf](https://zenodo.org/records/20822648/files/39I%20SGA%206%20-%20Source%20Scan%20Slice%20for%20Expose%20VII%20Pages%20423-454.pdf) |
| 0.2851 | [39J SGA 6 - Expose VII Filtration and Blowup K-Theory Pages 455-472 - French Reconstruction.pdf](https://zenodo.org/records/20822648/files/39J%20SGA%206%20-%20Expose%20VII%20Filtration%20and%20Blowup%20K-Theory%20Pages%20455-472%20-%20French%20Reconstruction.pdf) |
| 0.2834 | [39K SGA 6 - Expose VII Filtration and Blowup K-Theory Pages 455-472 - English Translation.pdf](https://zenodo.org/records/20822648/files/39K%20SGA%206%20-%20Expose%20VII%20Filtration%20and%20Blowup%20K-Theory%20Pages%20455-472%20-%20English%20Translation.pdf) |
| 1.2758 | [39L SGA 6 - Source Scan Slice for Expose VII Pages 455-472.pdf](https://zenodo.org/records/20822648/files/39L%20SGA%206%20-%20Source%20Scan%20Slice%20for%20Expose%20VII%20Pages%20455-472.pdf) |
| 0.2772 | [39M SGA 6 - Expose VIII Riemann-Roch Statement Pages 473-492 - French Reconstruction.pdf](https://zenodo.org/records/20822648/files/39M%20SGA%206%20-%20Expose%20VIII%20Riemann-Roch%20Statement%20Pages%20473-492%20-%20French%20Reconstruction.pdf) |
| 0.2754 | [39N SGA 6 - Expose VIII Riemann-Roch Statement Pages 473-492 - English Translation.pdf](https://zenodo.org/records/20822648/files/39N%20SGA%206%20-%20Expose%20VIII%20Riemann-Roch%20Statement%20Pages%20473-492%20-%20English%20Translation.pdf) |
| 1.4448 | [39O SGA 6 - Source Scan Slice for Expose VIII Pages 473-492.pdf](https://zenodo.org/records/20822648/files/39O%20SGA%206%20-%20Source%20Scan%20Slice%20for%20Expose%20VIII%20Pages%20473-492.pdf) |
| 0.2475 | [39P SGA 6 - Expose VIII Riemann-Roch Proof Pages 493-504 - French Reconstruction.pdf](https://zenodo.org/records/20822648/files/39P%20SGA%206%20-%20Expose%20VIII%20Riemann-Roch%20Proof%20Pages%20493-504%20-%20French%20Reconstruction.pdf) |
| 0.2456 | [39Q SGA 6 - Expose VIII Riemann-Roch Proof Pages 493-504 - English Translation.pdf](https://zenodo.org/records/20822648/files/39Q%20SGA%206%20-%20Expose%20VIII%20Riemann-Roch%20Proof%20Pages%20493-504%20-%20English%20Translation.pdf) |
| 0.7805 | [39R SGA 6 - Source Scan Slice for Expose VIII Pages 493-504.pdf](https://zenodo.org/records/20822648/files/39R%20SGA%206%20-%20Source%20Scan%20Slice%20for%20Expose%20VIII%20Pages%20493-504.pdf) |
| 0.2670 | [39S SGA 6 - Expose IX K-Groups and Computations, Pages 505-525 - English.pdf](https://zenodo.org/records/20822648/files/39S%20SGA%206%20-%20Expose%20IX%20K-Groups%20and%20Computations%2C%20Pages%20505-525%20-%20English.pdf) |
| 0.2649 | [39T SGA 6 - Expose IX K-Groups and Computations, Pages 505-525 - French.pdf](https://zenodo.org/records/20822648/files/39T%20SGA%206%20-%20Expose%20IX%20K-Groups%20and%20Computations%2C%20Pages%20505-525%20-%20French.pdf) |
| 1.4666 | [39U SGA 6 - Source Scan Slice for Expose IX Pages 505-525.pdf](https://zenodo.org/records/20822648/files/39U%20SGA%206%20-%20Source%20Scan%20Slice%20for%20Expose%20IX%20Pages%20505-525.pdf) |
| 0.2675 | [39V SGA 6 - Expose XIII Picard Finiteness Opening Pages 619-653 - English Translation.pdf](https://zenodo.org/records/20822648/files/39V%20SGA%206%20-%20Expose%20XIII%20Picard%20Finiteness%20Opening%20Pages%20619-653%20-%20English%20Translation.pdf) |
| 0.2384 | [39W SGA 6 - Expose XIII Picard Finiteness Opening Pages 619-653 - French Reconstruction.pdf](https://zenodo.org/records/20822648/files/39W%20SGA%206%20-%20Expose%20XIII%20Picard%20Finiteness%20Opening%20Pages%20619-653%20-%20French%20Reconstruction.pdf) |
| 2.5200 | [39X SGA 6 - Source Scan Slice for Expose XIII Pages 619-653.pdf](https://zenodo.org/records/20822648/files/39X%20SGA%206%20-%20Source%20Scan%20Slice%20for%20Expose%20XIII%20Pages%20619-653.pdf) |
| 0.2567 | [39Y SGA 6 - Expose XIII Neron-Severi and Hodge Index Pages 654-669 - English Translation.pdf](https://zenodo.org/records/20822648/files/39Y%20SGA%206%20-%20Expose%20XIII%20Neron-Severi%20and%20Hodge%20Index%20Pages%20654-669%20-%20English%20Translation.pdf) |
| 0.2591 | [39Z SGA 6 - Expose XIII Neron-Severi and Hodge Index Pages 654-669 - French Reconstruction.pdf](https://zenodo.org/records/20822648/files/39Z%20SGA%206%20-%20Expose%20XIII%20Neron-Severi%20and%20Hodge%20Index%20Pages%20654-669%20-%20French%20Reconstruction.pdf) |
| 1.1034 | [39ZA SGA 6 - Source Scan Slice for Expose XIII Pages 654-669.pdf](https://zenodo.org/records/20822648/files/39ZA%20SGA%206%20-%20Source%20Scan%20Slice%20for%20Expose%20XIII%20Pages%20654-669.pdf) |
| 0.1494 | [39ZB SGA 6 - Terminological and Notation Indexes Pages 693-702 - English Translation.pdf](https://zenodo.org/records/20822648/files/39ZB%20SGA%206%20-%20Terminological%20and%20Notation%20Indexes%20Pages%20693-702%20-%20English%20Translation.pdf) |
| 0.1496 | [39ZC SGA 6 - Terminological and Notation Indexes Pages 693-702 - French Reconstruction.pdf](https://zenodo.org/records/20822648/files/39ZC%20SGA%206%20-%20Terminological%20and%20Notation%20Indexes%20Pages%20693-702%20-%20French%20Reconstruction.pdf) |
| 0.3685 | [39ZD SGA 6 - Source Scan Slice for Indexes Pages 693-702.pdf](https://zenodo.org/records/20822648/files/39ZD%20SGA%206%20-%20Source%20Scan%20Slice%20for%20Indexes%20Pages%20693-702.pdf) |
| 2.4478 | [40 SGA 1 - French Reference PDF.pdf](https://zenodo.org/records/20822648/files/40%20SGA%201%20-%20French%20Reference%20PDF.pdf) |
| 1.5039 | [41 SGA 2 - French Reference PDF.pdf](https://zenodo.org/records/20822648/files/41%20SGA%202%20-%20French%20Reference%20PDF.pdf) |
| 5.4631 | [42 SGA 3 Part 1 - French Reference PDF.pdf](https://zenodo.org/records/20822648/files/42%20SGA%203%20Part%201%20-%20French%20Reference%20PDF.pdf) |
| 3.8318 | [43 SGA 3 Part 2 - French Reference PDF.pdf](https://zenodo.org/records/20822648/files/43%20SGA%203%20Part%202%20-%20French%20Reference%20PDF.pdf) |
| 2.9650 | [44 SGA 3 Part 3 - French Reference PDF.pdf](https://zenodo.org/records/20822648/files/44%20SGA%203%20Part%203%20-%20French%20Reference%20PDF.pdf) |
| 2.4100 | [45 SGA 4 Part 1 - French Reference PDF.pdf](https://zenodo.org/records/20822648/files/45%20SGA%204%20Part%201%20-%20French%20Reference%20PDF.pdf) |
| 2.2773 | [46 SGA 4 Part 2 - French Reference PDF.pdf](https://zenodo.org/records/20822648/files/46%20SGA%204%20Part%202%20-%20French%20Reference%20PDF.pdf) |
| 3.2955 | [47 SGA 4 Part 3 - French Reference PDF.pdf](https://zenodo.org/records/20822648/files/47%20SGA%204%20Part%203%20-%20French%20Reference%20PDF.pdf) |
| 1.8876 | [48 SGA 4.5 - French Reference PDF.pdf](https://zenodo.org/records/20822648/files/48%20SGA%204.5%20-%20French%20Reference%20PDF.pdf) |
| 56.2983 | [49 SGA 5 - French Reference PDF.pdf](https://zenodo.org/records/20822648/files/49%20SGA%205%20-%20French%20Reference%20PDF.pdf) |
| 51.8090 | [50 SGA 6 - French Reference PDF.pdf](https://zenodo.org/records/20822648/files/50%20SGA%206%20-%20French%20Reference%20PDF.pdf) |
| 35.6319 | [51 SGA 7 Tome 1 - French Reference PDF.pdf](https://zenodo.org/records/20822648/files/51%20SGA%207%20Tome%201%20-%20French%20Reference%20PDF.pdf) |
| 26.2210 | [52 SGA 7 Tome 2 - French Reference PDF.pdf](https://zenodo.org/records/20822648/files/52%20SGA%207%20Tome%202%20-%20French%20Reference%20PDF.pdf) |
| 0.2394 | [53 SGA 7-I - Source-Checked Working Edition Pages 1-24 - English Translation.pdf](https://zenodo.org/records/20822648/files/53%20SGA%207-I%20-%20Source-Checked%20Working%20Edition%20Pages%201-24%20-%20English%20Translation.pdf) |
| 0.2152 | [54 SGA 7-I - Source-Checked Working Edition Pages 1-24 - French Reconstruction.pdf](https://zenodo.org/records/20822648/files/54%20SGA%207-I%20-%20Source-Checked%20Working%20Edition%20Pages%201-24%20-%20French%20Reconstruction.pdf) |
| 1.6562 | [55 SGA 7-I - Source Scan Slice Pages 1-24.pdf](https://zenodo.org/records/20822648/files/55%20SGA%207-I%20-%20Source%20Scan%20Slice%20Pages%201-24.pdf) |

## Artifact ZIPs

| Size MB | File |
|---:|---|
| 358.8781 | [80 SGA - Current TeX Sources, Manifests, and Build Logs.zip](https://zenodo.org/records/20822648/files/80%20SGA%20-%20Current%20TeX%20Sources%2C%20Manifests%2C%20and%20Build%20Logs.zip) |
| 373.7911 | [81 SGA - Prior Segment Source Packets through Sequence 033.zip](https://zenodo.org/records/20822648/files/81%20SGA%20-%20Prior%20Segment%20Source%20Packets%20through%20Sequence%20033.zip) |
| 0.0050 | [82 SGA - Correction A TeX Sources and Metadata for SGA5 SGA6 and SGA7-I Pages 1-24.zip](https://zenodo.org/records/20822648/files/82%20SGA%20-%20Correction%20A%20TeX%20Sources%20and%20Metadata%20for%20SGA5%20SGA6%20and%20SGA7-I%20Pages%201-24.zip) |
| 74.2903 | [95 SGA - Update Packets 2026-06-07.zip](https://zenodo.org/records/20822648/files/95%20SGA%20-%20Update%20Packets%202026-06-07.zip) |
| 115.9803 | [SGA.zip](https://zenodo.org/records/20822648/files/SGA.zip) |
| 74.2894 | [SGA5_onward_ordered_rebuild_010_sga7i_001_036.zip](https://zenodo.org/records/20822648/files/SGA5_onward_ordered_rebuild_010_sga7i_001_036.zip) |
| 201.7440 | [SGA5_onward_ordered_rebuild_011_sga7i_037_050.zip](https://zenodo.org/records/20822648/files/SGA5_onward_ordered_rebuild_011_sga7i_037_050.zip) |
| 74.9229 | [sga5_repair004_20260609.zip](https://zenodo.org/records/20822648/files/sga5_repair004_20260609.zip) |
| 101.0843 | [sga5_repair006_20260609.zip](https://zenodo.org/records/20822648/files/sga5_repair006_20260609.zip) |
| 83.9335 | [SGA5_repair006_next_aid_footnotes_diagrams_20260609.zip](https://zenodo.org/records/20822648/files/SGA5_repair006_next_aid_footnotes_diagrams_20260609.zip) |
| 82.5564 | [sga5_repair007_20260609.zip](https://zenodo.org/records/20822648/files/sga5_repair007_20260609.zip) |
| 85.3250 | [sga5_repair008_20260609.zip](https://zenodo.org/records/20822648/files/sga5_repair008_20260609.zip) |
| 60.6566 | [sga5_repair009_20260609.zip](https://zenodo.org/records/20822648/files/sga5_repair009_20260609.zip) |
| 51.7115 | [sga5_repair010_20260609.zip](https://zenodo.org/records/20822648/files/sga5_repair010_20260609.zip) |
| 70.9450 | [sga5_repair011_20260610.zip](https://zenodo.org/records/20822648/files/sga5_repair011_20260610.zip) |
| 80.9819 | [sga5_repair012_20260610.zip](https://zenodo.org/records/20822648/files/sga5_repair012_20260610.zip) |
| 71.1987 | [SGA5_repair032_audit_support_20260624.zip](https://zenodo.org/records/20822648/files/SGA5_repair032_audit_support_20260624.zip) |
| 118.1306 | [sga5_sga6_repair016_20260611.zip](https://zenodo.org/records/20822648/files/sga5_sga6_repair016_20260611.zip) |
| 133.1503 | [sga5_sga6_repair017_20260611.zip](https://zenodo.org/records/20822648/files/sga5_sga6_repair017_20260611.zip) |
| 142.2608 | [sga5_sga6_repair018_20260612.zip](https://zenodo.org/records/20822648/files/sga5_sga6_repair018_20260612.zip) |
| 139.0969 | [sga5_sga6_repair019_20260612.zip](https://zenodo.org/records/20822648/files/sga5_sga6_repair019_20260612.zip) |
| 138.9594 | [sga5_sga6_repair020_20260612.zip](https://zenodo.org/records/20822648/files/sga5_sga6_repair020_20260612.zip) |
| 197.7602 | [sga5_sga6_repair022_20260612.zip](https://zenodo.org/records/20822648/files/sga5_sga6_repair022_20260612.zip) |
| 4.0173 | [sga5_sga6_repair027_cumulative_20260613.zip](https://zenodo.org/records/20822648/files/sga5_sga6_repair027_cumulative_20260613.zip) |
| 115.9803 | [SGA_current_sga5_sga6_sga7i_001_050_20260608.zip](https://zenodo.org/records/20822648/files/SGA_current_sga5_sga6_sga7i_001_050_20260608.zip) |

## Manifest And Status Files

| Size MB | File |
|---:|---|
| 0.0097 | [99 SGA - Public Summary.json](https://zenodo.org/records/20822648/files/99%20SGA%20-%20Public%20Summary.json) |

## Local Audit Reconciliation, 2026-06-27

The current local SGA5 status reflected by this record has two layers. The latest compact promoted delta is still `SGA5_FullAudit_WebDrop_p260_p265_workpass_delta_20260626`, which promotes only p260-p265 as page-local French workpass/source-audit evidence. Later live ledger/provenance checkpoints now record `CERT_LOG.md` through 320 completed page rows, with p318-p320 entering Exposé VII §7 around intersections complètes, Lefschetz, Corollaire 7.2, and Lemme 7.2.1; the local workpass PDF is 307 pages and p321 is the next cursor. The broader folder `SGA continuation 2/_claude_aid/sga5_full_audit_20260623` contains live workpass TeX/PDF, `CERT_LOG.md`, `AGENT_SCORECARD.md`, method notes, and many source crops, but those folder-level materials are evidence/provenance, not a global quality certificate. Later crops or cursor text beyond p320 remain active scratch unless explicitly packaged in a later compact delta.

Important: these are audit/support and synchronization-control materials, not an accepted complete edition. The SGA5 folder notes and agent scorecards are useful for source repair, but the public archive should still treat SGA5 as under review, not independently certified, not English-synchronized, and not a critical edition. SGA6 repair107 is part of the English-sync repair chain and still leaves global SGA6 certification plus later sync work open.
