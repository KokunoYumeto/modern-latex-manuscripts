# Modern LaTeX Manuscript Corpus

This repository is the coordination surface for an AI-run, human-directed project that turns older mathematics manuscripts and source witnesses into inspectable modern LaTeX, reader PDFs, translations, audit packets, and citable Zenodo releases.

GitHub is not the bulk-storage layer. Large PDFs, scans, and artifact ZIPs live on Zenodo. This repository keeps manifests, small datasets, workflow scripts, issue templates, status notes, and collaboration scaffolding.

## Archive Map

- **Initial dump + raw provenance:** <https://doi.org/10.5281/zenodo.20393488>
- **Workflow / replication packet:** <https://doi.org/10.5281/zenodo.20461174>
- **Emmy Noether:** <https://doi.org/10.5281/zenodo.20412587>
- **Heinrich Weber:** <https://doi.org/10.5281/zenodo.20412153>
- **Arthur Cayley:** <https://doi.org/10.5281/zenodo.20520749>
- **James Joseph Sylvester:** <https://doi.org/10.5281/zenodo.20520692>
- **Richard Dedekind:** <https://doi.org/10.5281/zenodo.20520669>
- **P. G. Lejeune Dirichlet:** <https://doi.org/10.5281/zenodo.20520679>
- **Ernst Steinitz:** <https://doi.org/10.5281/zenodo.20530952>
- **Carl Friedrich Gauss:** <https://doi.org/10.5281/zenodo.20410934>
- **SGA working translations/transcriptions:** <https://doi.org/10.5281/zenodo.20410947>
- **EGA working translation material:** <https://doi.org/10.5281/zenodo.20414353>
- **Pierre Deligne papers and letters:** <https://doi.org/10.5281/zenodo.20410853>
- **Ukrainian applied mathematics:** <https://doi.org/10.5281/zenodo.20490906>
- **al-Battani, Opus Astronomicum / Kitab al-Zij:** <https://doi.org/10.5281/zenodo.20539593>
- **Non-European / multilingual mathematics general:** <https://doi.org/10.5281/zenodo.20410957>
- **Islamic/Arabic mathematics:** <https://doi.org/10.5281/zenodo.20415769>
- **Indian/Sanskrit mathematics:** <https://doi.org/10.5281/zenodo.20415754>
- **Chinese mathematics:** <https://doi.org/10.5281/zenodo.20415751>
- **Riemann:** <https://doi.org/10.5281/zenodo.20429778>
- **General author cluster / staging shelf:** <https://doi.org/10.5281/zenodo.20411006>
- **Classical algebra / arithmetic umbrella shelf:** <https://doi.org/10.5281/zenodo.20414787>

Use the concept DOI for citation unless you specifically need to cite one exact version.

## What This Project Is

The core output is a source-checkable working layer:

- readable generated PDFs,
- corresponding TeX/source files,
- source-witness scans or scan slices,
- provenance, manifests, and build logs,
- render checks and audit notes,
- translations where the source-language layer is stable enough.

These are working scholarly editions and translation drafts, not final critical editions. A record may contain excellent completed pieces beside material that is explicitly still being audited. The status files and Zenodo summaries should be read before treating any lane as complete.

## Current Status

- **Noether:** German/English numbered-paper corpus complete; Spanish/Japanese cumulative translations complete through Paper 43 and under recursive scan audit/backfill; recursive audit now reaches Papers 31-36 and restores missing Paper 35 material; French currently has a Codex-checked checkpoint through Papers 01-03.
- **Weber:** `Lehrbuch der Algebra` Volume I German/English complete and recursively source-audited through the Introduction; Volume II is source-checked through section 143; Volume III is in progress.
- **SGA:** SGA 5/6 translation/transcription lanes are complete at working-edition level; SGA 7-I is in progress and currently staged through source page 528.
- **Deligne:** letters/correspondence lane is complete at working-draft level; forward stream reaches Paper 016 page 70 and reverse stream has Paper 078 through pages 1-56 plus Papers 079-090; still uneven by design.
- **Cayley:** many rendered volume readers and repaired slices exist, but the lane remains a patchwork working edition with known layout and dense-table issues.
- **Sylvester:** Volume I source-checked working edition is advancing sequentially; current public staging reaches book page 511.
- **Dedekind:** GMW Volume I cumulative German/English reader now covers Items I-IV plus Item V through Article 13, with source witness packet and explicit continuation at Item V Article 14.
- **al-Battani:** work-level package combines a trilingual text working reader, complete fixed-star catalogue, complete geography gazetteer, partial chronology, source witnesses, and workflow notes. It is one work-level DOI, not a separate catalogue split.
- **Non-European / multilingual:** broad reader/source-intake layer across Chinese, Sanskrit/Indian, Islamic/Arabic, Persian-adjacent, and Japanese material. Quality varies by work; the best readers are useful now, while some items remain source-intake or repair targets.
- **Ukrainian applied mathematics:** applied mathematics and engineering translation lane, including estimation, filtering, VIO/SLAM, SDR/radar/navigation-adjacent mathematics, and related technical material.

## How To Help

Useful contributions include:

- reporting unreadable or malformed PDFs,
- correcting TeX transcription errors,
- identifying missing source witnesses,
- checking translations against original-language sources,
- splitting collected works into clean per-paper/per-work units,
- improving manifests, provenance, and build scripts,
- submitting source-aligned translation batches.

Open an issue using the templates in `.github/ISSUE_TEMPLATE/`. Small text corrections can be submitted as pull requests. For large generated artifacts, open an issue first and link the external package or Zenodo record; do not commit bulky PDFs or ZIPs directly to git.

## Repository Contents

- `STATUS.md`: current release status and active caveats.
- `ROADMAP.md`: practical next steps.
- `data/`: small manifests, audit summaries, and open datasets.
- `scripts/`: release, OCR, audit, and workflow helpers.

## License

Project coordination material, scripts, and locally generated metadata in this repository are released under CC0 1.0 unless otherwise noted. Historical works, scans, and upstream transcriptions may carry their own public-domain/source status.
