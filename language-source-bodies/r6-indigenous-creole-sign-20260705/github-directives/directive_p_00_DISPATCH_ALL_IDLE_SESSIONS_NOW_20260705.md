# DISPATCH ALL IDLE SESSIONS NOW

Date: 2026-07-05

This file is for the one other-PC session that is actually moving.

If there are twelve sessions open and only one is moving, the moving session is now the dispatcher. It must assign the other eleven sessions real work immediately. It must not spend the next hour reading instructions, writing acknowledgements, or doing one worker's worth of output while the other sessions sit idle.

## Dispatch Rule

Every visible idle session gets a concrete payload task.

For each idle session, the dispatcher must tell that session to set the complete assigned task block as its pursued goal / active goal / persistent task, exactly and verbatim.

Not a summary.

Not a shortened version.

Not "work on Slavic sources."

Not "help with interlanguage."

The whole assigned task block must become that session's pursued goal.

If the target session has a goal tool, it must use the goal tool. If it has a visible goal/task/pursuit field, paste the assigned task block there. If it cannot set a formal goal, it must copy the assigned task block at the top of its local logbook and state internally that this is the active pursued goal. The pushed output must still be payload, not that statement.

The task must request one of:

- literal source-body collection;
- source-body packaging;
- source-checked translation/transcription repair;
- package audit for body presence;
- interlanguage/Fable ledger tied to actual bodies;
- web/pro handoff ZIP with bodies;
- source-witness/crop/scan package;
- Lean/formalization body collection if already produced.

The task must not request:

- acknowledgement;
- summary;
- governance note;
- "think about it";
- "read these instructions" as final output;
- a ledger with no bodies;
- pointer-only source canon.

## Required Dispatcher Files

Create or update these files locally and in the side branch whenever possible:

- `ACTIVE_SESSIONS.md`
- `SIBLING_TASKS.md`
- `SOURCE_BODY_UPLOAD_QUEUE.md`
- `SESSION_LOGBOOK_YYYYMMDD.md`
- `CURRENT_OUTPUT_STATE.md`

If these files already exist, update them. If they do not exist, create them.

## Exact Session Assignments

Use these assignments unless the visible session state makes a more specific payload task obviously better.

### Session 01: Coordinator / Dispatcher

Set the following block as Session 01's pursued goal verbatim:

```text
You are Session 01: Coordinator / Dispatcher.

Set `SET_THIS_AS_YOUR_GOAL_VERBATIM_20260705.md` as active goal. Then assign all other sessions. Maintain `ACTIVE_SESSIONS.md`, `SIBLING_TASKS.md`, `SOURCE_BODY_UPLOAD_QUEUE.md`, and a dated logbook. Do not do body collection until the other sessions have been assigned. Push only to `codex/noether-pc-20260629`.
```

Required output:

- updated active-session table;
- task table;
- source-body queue;
- logbook;
- a payload package or clear record that sibling sessions were assigned concrete payload work.

False output:

- "I have read the instructions";
- "I will dispatch sessions";
- any acknowledgement without assignments.

### Session 02: Slavic Non-RU/UK Source Bodies

Set the following block as Session 02's pursued goal verbatim:

```text
You are Session 02: Slavic Non-RU/UK Source Bodies.

Collect literal TeX-family/source bodies for non-Russian, non-Ukrainian Slavic languages touched by the interlanguage work: Polish, Czech, Slovak, Slovenian, Serbian, Croatian, Bosnian, Montenegrin, Bulgarian, Macedonian, Belarusian, Sorbian, Church Slavonic/Old Church Slavonic where relevant, and any smaller Slavic sources encountered.

Required bodies:

`.tex`, `.ltx`, `.sty`, `.cls`, `.bib`, `.bbl`, `.dtx`, `.ins`, source PDFs, source archives, and build dependencies.
```

Required output:

`language-source-bodies/slavic-non-ru-uk/` with source files, `MANIFEST.csv`, `SHA256SUMS.txt`, `README.md`, and logbook excerpt.

False output:

URL list only, bodyless source-canon list, acknowledgement.

### Session 03: Russian/Ukrainian/Interslavic Translation Branch Bodies

Set the following block as Session 03's pursued goal verbatim:

```text
You are Session 03: Russian/Ukrainian/Interslavic Translation Branch Bodies.

Collect and package every actual Russian, Ukrainian, and Interslavic Noether/interlanguage translation body already produced on the machine. Include TeX/PDF/source-control/glossary/logbook files. Keep generated drafts separate from native/source-canon evidence.
```

Required output:

`noether-language-output/slavic-ru-uk-isv/` with translated TeX/PDF where present, glossaries, source-control notes, `MANIFEST.csv`, `SHA256SUMS.txt`, `README.md`, and logbook excerpt.

False output:

statement that translations exist somewhere else.

### Session 04: Fable / ChatGPT-Pro Interlanguage Ledgers With Bodies

Set the following block as Session 04's pursued goal verbatim:

```text
You are Session 04: Fable / ChatGPT-Pro Interlanguage Ledgers With Bodies.

Apply Fable/ChatGPT-Pro constraints to one concrete terminology block. Build the ledgers and attach actual evidence/source bodies used for the decisions.
```

Required output:

`interlanguage-sidecar/fable-ledger-block-YYYYMMDD/` with:

- `branch_weight_ledger.csv`
- `marginal_intelligibility_ledger.csv`
- `false_friend_ledger.csv`
- `adverse_evidence_ledger.csv`
- `source_use_status.csv`
- `terminology_decisions.csv`
- actual source bodies or excerpts legally/locally available in `source_bodies/`
- `README.md`
- `SHA256SUMS.txt`

False output:

methodology prose with no evidence bodies.

### Session 05: CJK Source-Body Corpus

Set the following block as Session 05's pursued goal verbatim:

```text
You are Session 05: CJK Source-Body Corpus.

Collect literal source bodies for CJK mathematical/technical prose relevant to the interlanguage and translation-style baselines: Chinese, Japanese, Korean if present. Keep native source files separate from generated translations.
```

Required output:

`language-source-bodies/cjk/` with source files/archives/PDFs, manifest, hashes, README, and logbook.

False output:

claiming Japanese Noether output is native CJK evidence.

### Session 06: Arabic / Persianate / RTL Source Bodies

Set the following block as Session 06's pursued goal verbatim:

```text
You are Session 06: Arabic / Persianate / RTL Source Bodies.

Collect literal source bodies for Arabic, Persian/Farsi, Dari, Tajik, Urdu, Ottoman/Turkic/RTL-adjacent technical or mathematical prose if present. Keep OCR witnesses separate from native source bodies and generated drafts.
```

Required output:

`language-source-bodies/rtl-persianate-arabic/` with source files/archives/PDFs, manifest, hashes, README, and logbook.

False output:

claiming Arabic evidence covers Persian, or Persian evidence covers Arabic.

### Session 07: Romance / Germanic / High-Resource Baselines

Set the following block as Session 07's pursued goal verbatim:

```text
You are Session 07: Romance / Germanic / High-Resource Baselines.

Collect literal TeX/source bodies for Spanish, French, Portuguese, Italian, German, Dutch, English, Scandinavian languages, and other high-resource baselines touched by the project. These are style/terminology witnesses for translation quality and interlanguage marginal-intelligibility checks.
```

Required output:

`language-source-bodies/romance-germanic-baselines/` with bodies, manifest, hashes, README, and logbook.

False output:

metadata-only inventory.

### Session 08: Noether Source-Control / Known Correction Bodies

Set the following block as Session 08's pursued goal verbatim:

```text
You are Session 08: Noether Source-Control / Known Correction Bodies.

Collect the latest Noether correction packages, source-control bodies, known gap repairs, multilingual branches, and audit ledgers from local downloads and working folders. Do not mark as final unless certified. Identify which files are actual corrected TeX/PDF and which are audit-only.
```

Required output:

`noether-source-control/latest-corrections-YYYYMMDD/` with real TeX/PDF/logs/source witnesses, manifest, hashes, README, and caveat.

False output:

audit note with no corrected files.

### Session 09: SGA / Deligne Source-Repair Body Audit

Set the following block as Session 09's pursued goal verbatim:

```text
You are Session 09: SGA / Deligne Source-Repair Body Audit.

Collect latest SGA5/SGA6/SGA7 and Deligne repair bodies produced on the machine. Package actual TeX/PDF/log/source-witness files and classify known weaknesses: diagrams, compression, paraphrase, incomplete source-rescribe, English sync missing.
```

Required output:

`source-repair-bodies/sga-deligne-latest-YYYYMMDD/` with actual bodies, manifest, hashes, README, and caveat.

False output:

calling SGA5 or SGA6 complete.

### Session 10: Lean/Formalization Bodies

Set the following block as Session 10's pursued goal verbatim:

```text
You are Session 10: Lean/Formalization Bodies.

Find actual Lean formalization files produced by Claude/Codex/other sessions. Package `.lean`, lake files, README/logbook, and state clearly whether they compile, are sketches, or are unrelated. Do not claim they certify the historical transcription.
```

Required output:

`formalization/lean-work-in-progress-YYYYMMDD/` with `.lean` bodies, build files if present, manifest, hashes, README, and logbook.

False output:

philosophical note about Lean with no Lean files.

### Session 11: Package Auditor

Set the following block as Session 11's pursued goal verbatim:

```text
You are Session 11: Package Auditor.

Audit the most recent side-branch package for whether it contains actual bodies. Count extensions, byte sizes, and hashes. Mark categories: body, generated draft, OCR witness, pointer-only, rejected. Produce a rejection or acceptance note.
```

Required output:

`audits/package-body-presence-YYYYMMDD/` with extension count table, body list, rejected false-output list, and manifest.

False output:

"looks fine" without file counts.

### Session 12: Transfer / GitHub Uploader

Set the following block as Session 12's pursued goal verbatim:

```text
You are Session 12: Transfer / GitHub Uploader.

Take all packages produced by Sessions 02-11 and push them to side branch `codex/noether-pc-20260629`. Do not push to `main`. Ensure manifests and hash files are included. If packages are too large, split them. Do not replace bodies with summaries.
```

Required output:

side-branch commits containing actual package bodies, not just indexes.

False output:

push of only coordination notes.

## Assignment Text To Paste Into Idle Sessions

Paste this structure into each idle session:

```text
You are idle and must start work now.

Set the complete task block I paste below as your pursued goal / active goal / persistent task, exactly and verbatim. Do not summarize it. Do not shorten it. Do not treat it as reading material.

[PASTE COMPLETE SESSION TASK BLOCK HERE]

After setting that exact pursued goal, execute it. Do not acknowledge as final output. Produce literal file bodies or concrete repair output, not a summary. Include MANIFEST.csv, SHA256SUMS.txt, README.md, source-use labels, and a logbook excerpt. Stay off main. Push or place output for side-branch codex/noether-pc-20260629 only. If you cannot find bodies, report exact searched paths and assign the next recovery action. Reading this instruction is not completion.
```

## Dispatcher Completion Standard

Dispatcher work is not complete until:

1. every visible session has a concrete task;
2. each task has required output and false-output notes;
3. task assignments are logged;
4. at least one payload-producing session has started;
5. no idle session remains unassigned;
6. the side branch receives actual bodies/output, or a concrete blocker package with searched paths.

Do this now.
