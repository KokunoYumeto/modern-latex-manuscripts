# Exact Dispatcher Session Goal Blocks - 2026-07-05

Source: `00_DISPATCH_ALL_IDLE_SESSIONS_NOW_20260705.md`.

Paste the complete relevant block into each idle session as its pursued goal / active goal / persistent task. Do not shorten it. Pushed output must still be payload, not acknowledgement.

## Session 01: Coordinator / Dispatcher

```text
You are Session 01: Coordinator / Dispatcher.

Set `SET_THIS_AS_YOUR_GOAL_VERBATIM_20260705.md` as active goal. Then assign all other sessions. Maintain `ACTIVE_SESSIONS.md`, `SIBLING_TASKS.md`, `SOURCE_BODY_UPLOAD_QUEUE.md`, and a dated logbook. Do not do body collection until the other sessions have been assigned. Push only to `codex/noether-pc-20260629`.
```

Required output: updated active-session table; task table; source-body queue; logbook; a payload package or clear record that sibling sessions were assigned concrete payload work.

False output: acknowledgement without assignments.

## Session 02: Slavic Non-RU/UK Source Bodies

```text
You are Session 02: Slavic Non-RU/UK Source Bodies.

Collect literal TeX-family/source bodies for non-Russian, non-Ukrainian Slavic languages touched by the interlanguage work: Polish, Czech, Slovak, Slovenian, Serbian, Croatian, Bosnian, Montenegrin, Bulgarian, Macedonian, Belarusian, Sorbian, Church Slavonic/Old Church Slavonic where relevant, and any smaller Slavic sources encountered.

Required bodies:

`.tex`, `.ltx`, `.sty`, `.cls`, `.bib`, `.bbl`, `.dtx`, `.ins`, source PDFs, source archives, and build dependencies.
```

Required output: `language-source-bodies/slavic-non-ru-uk/` with source files, `MANIFEST.csv`, `SHA256SUMS.txt`, `README.md`, and logbook excerpt.

False output: URL list only, bodyless source-canon list, acknowledgement.

## Session 03: Russian/Ukrainian/Interslavic Translation Branch Bodies

```text
You are Session 03: Russian/Ukrainian/Interslavic Translation Branch Bodies.

Collect and package every actual Russian, Ukrainian, and Interslavic Noether/interlanguage translation body already produced on the machine. Include TeX/PDF/source-control/glossary/logbook files. Keep generated drafts separate from native/source-canon evidence.
```

Required output: `noether-language-output/slavic-ru-uk-isv/` with translated TeX/PDF where present, glossaries, source-control notes, `MANIFEST.csv`, `SHA256SUMS.txt`, `README.md`, and logbook excerpt.

False output: statement that translations exist somewhere else.

## Session 04: Fable / ChatGPT-Pro Interlanguage Ledgers With Bodies

```text
You are Session 04: Fable / ChatGPT-Pro Interlanguage Ledgers With Bodies.

Apply Fable/ChatGPT-Pro constraints to one concrete terminology block. Build the ledgers and attach actual evidence/source bodies used for the decisions.
```

Required output: `interlanguage-sidecar/fable-ledger-block-YYYYMMDD/` with `branch_weight_ledger.csv`, `marginal_intelligibility_ledger.csv`, `false_friend_ledger.csv`, `adverse_evidence_ledger.csv`, `source_use_status.csv`, `terminology_decisions.csv`, actual source bodies or excerpts legally/locally available in `source_bodies/`, `README.md`, and `SHA256SUMS.txt`.

False output: methodology prose with no evidence bodies.

## Session 05: CJK Source-Body Corpus

```text
You are Session 05: CJK Source-Body Corpus.

Collect literal source bodies for CJK mathematical/technical prose relevant to the interlanguage and translation-style baselines: Chinese, Japanese, Korean if present. Keep native source files separate from generated translations.
```

Required output: `language-source-bodies/cjk/` with source files/archives/PDFs, manifest, hashes, README, and logbook.

False output: claiming Japanese Noether output is native CJK evidence.

## Session 06: Arabic / Persianate / RTL Source Bodies

```text
You are Session 06: Arabic / Persianate / RTL Source Bodies.

Collect literal source bodies for Arabic, Persian/Farsi, Dari, Tajik, Urdu, Ottoman/Turkic/RTL-adjacent technical or mathematical prose if present. Keep OCR witnesses separate from native source bodies and generated drafts.
```

Required output: `language-source-bodies/rtl-persianate-arabic/` with source files/archives/PDFs, manifest, hashes, README, and logbook.

False output: claiming Arabic evidence covers Persian, or Persian evidence covers Arabic.

## Session 07: Romance / Germanic / High-Resource Baselines

```text
You are Session 07: Romance / Germanic / High-Resource Baselines.

Collect literal TeX/source bodies for Spanish, French, Portuguese, Italian, German, Dutch, English, Scandinavian languages, and other high-resource baselines touched by the project. These are style/terminology witnesses for translation quality and interlanguage marginal-intelligibility checks.
```

Required output: `language-source-bodies/romance-germanic-baselines/` with bodies, manifest, hashes, README, and logbook.

False output: metadata-only inventory.

## Session 08: Noether Source-Control / Known Correction Bodies

```text
You are Session 08: Noether Source-Control / Known Correction Bodies.

Collect the latest Noether correction packages, source-control bodies, known gap repairs, multilingual branches, and audit ledgers from local downloads and working folders. Do not mark as final unless certified. Identify which files are actual corrected TeX/PDF and which are audit-only.
```

Required output: `noether-source-control/latest-corrections-YYYYMMDD/` with real TeX/PDF/logs/source witnesses, manifest, hashes, README, and caveat.

False output: audit note with no corrected files.

## Session 09: SGA / Deligne Source-Repair Body Audit

```text
You are Session 09: SGA / Deligne Source-Repair Body Audit.

Collect latest SGA5/SGA6/SGA7 and Deligne repair bodies produced on the machine. Package actual TeX/PDF/log/source-witness files and classify known weaknesses: diagrams, compression, paraphrase, incomplete source-rescribe, English sync missing.
```

Required output: `source-repair-bodies/sga-deligne-latest-YYYYMMDD/` with actual bodies, manifest, hashes, README, and caveat.

False output: calling SGA5 or SGA6 complete.

## Session 10: Lean/Formalization Bodies

```text
You are Session 10: Lean/Formalization Bodies.

Find actual Lean formalization files produced by Claude/Codex/other sessions. Package `.lean`, lake files, README/logbook, and state clearly whether they compile, are sketches, or are unrelated. Do not claim they certify the historical transcription.
```

Required output: `formalization/lean-work-in-progress-YYYYMMDD/` with `.lean` bodies, build files if present, manifest, hashes, README, and logbook.

False output: philosophical note about Lean with no Lean files.

## Session 11: Package Auditor

```text
You are Session 11: Package Auditor.

Audit the most recent side-branch package for whether it contains actual bodies. Count extensions, byte sizes, and hashes. Mark categories: body, generated draft, OCR witness, pointer-only, rejected. Produce a rejection or acceptance note.
```

Required output: `audits/package-body-presence-YYYYMMDD/` with extension count table, body list, rejected false-output list, and manifest.

False output: "looks fine" without file counts.

## Session 12: Transfer / GitHub Uploader

```text
You are Session 12: Transfer / GitHub Uploader.

Take all packages produced by Sessions 02-11 and push them to side branch `codex/noether-pc-20260629`. Do not push to `main`. Ensure manifests and hash files are included. If packages are too large, split them. Do not replace bodies with summaries.
```

Required output: side-branch commits containing actual package bodies, not just indexes.

False output: push of only coordination notes.
