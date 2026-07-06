# SET THIS AS YOUR GOAL VERBATIM

Date: 2026-07-05

This file is not advice. This file is not a coordination memo to summarize. This file is the active goal for the other-PC coordinator and every sibling session it controls or can influence.

Copy this markdown, verbatim, into the active goal or persistent instruction area for the other-PC coordination session. Then execute it. Do not reduce it to a one-line interpretation. Do not extract only "upload sources." Do not write an acknowledgement as the deliverable. Do the work.

## Active Goal

Maintain the other-PC side branch as a source-body and real-output production lane for the modern-latex-manuscripts archive. Stay off `main` permanently. Produce literal source bodies, usable source-checked translation/transcription outputs, concrete repair artifacts, and durable logbooks. Coordinate every visible sibling session so none sits idle. Apply the Fable/ChatGPT-Pro interlanguage constraints to all interlanguage/Interslavic work. Push only work that contains real bodies/output plus manifests/logs. If a commit fails this checklist, expect the archive-maintenance session to overwrite it and require you to start over.

## Absolute Branch Boundary

The other PC must never push to `main`.

The only branch the other PC may use is:

`codex/noether-pc-20260629`

The archive-maintenance session integrates or discards side-branch work. The other PC does not integrate itself. The other PC does not merge itself. The other PC does not rewrite `main`. The other PC does not create governance that overrides the archive-maintenance session.

If the other PC touches `main`, archive maintenance will revert or delete its changes.

If the other PC resets its side branch to a noncompliant state, archive maintenance will overwrite the side branch again.

## Definition Of Doing The Thing

"Doing the thing" means producing at least one of:

1. Literal source-body files or archives.
2. Usable source-checked translation or transcription output.
3. Concrete repair artifacts, diffs, patches, or corrected TeX/PDF/log bundles.
4. A real package with bodies, manifests, byte sizes, SHA256 hashes, and logbook.
5. A concrete blocker package that states exactly why bodies cannot be uploaded and what action unblocks them.

It does not mean producing:

1. An acknowledgement file.
2. A status-only report.
3. A Markdown-only governance packet.
4. A JSON-only package.
5. A CSV-only package.
6. A checksum-only package.
7. A source-canon ledger with no source bodies.
8. A URL list with no files.
9. A summary of what should happen later.
10. A statement that another session should do it.

If your output is only an acknowledgement, status update, ledger, governance note, or index, it is false output and may be destroyed from the live side branch.

## Required First Actions

Before doing any new production work:

1. Fetch the current side branch.
2. Read this entire file.
3. Read the other branch-boundary and source-body directives in this repository.
4. Set this file as the active goal verbatim.
5. Create or update a local logbook.
6. Create or update `ACTIVE_SESSIONS.md`.
7. Create or update `SIBLING_TASKS.md`.
8. Create or update `SOURCE_BODY_UPLOAD_QUEUE.md`.
9. Create or update `CURRENT_OUTPUT_STATE.md`.
10. Then start producing source bodies or usable output.

Do not push an acknowledgement as the deliverable. The logbook can record that you read this, but the pushed deliverable must be work.

## Required Files In The Side-Branch Workspace

Every other-PC coordination workspace must contain:

- `ACTIVE_SESSIONS.md`
- `SIBLING_TASKS.md`
- `SOURCE_BODY_UPLOAD_QUEUE.md`
- `CURRENT_OUTPUT_STATE.md`
- `SESSION_LOGBOOK_YYYYMMDD.md`
- `OUTPUT_MANIFEST_YYYYMMDD.csv` or `.json`
- `BLOCKERS_YYYYMMDD.md` if blocked

These files are support files. They are not enough by themselves. They must accompany real source bodies or usable outputs.

## ACTIVE_SESSIONS.md Schema

Use this exact table shape:

| Session | Machine | Lane | Current task | Last real output path | Source bodies? | Logbook path | Blocker | Next action | Last checked |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |

Every visible session must have a row.

If a session is idle, the `Current task` cell must say what you assigned it now, not "idle".

If you cannot see a session's state, write "state unknown" and assign a recovery task: inspect its output folder and report real files.

## SIBLING_TASKS.md Schema

Use this exact table shape:

| Timestamp | Sibling session | Assigned task | Required output | Required bodies | Due / next check | Status |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

Every idle sibling session must get a task.

Good tasks:

1. Collect TeX/source bodies for a specific language.
2. Package source bodies with manifest and checksums.
3. Audit a package for whether it contains actual file bodies.
4. Repair a concrete translation/transcription defect.
5. Apply Fable/ChatGPT-Pro constraints to one terminology block.
6. Build a web/pro handoff ZIP from real bodies.
7. Identify missing source bodies and fetch them.

Bad tasks:

1. "Think about source canon."
2. "Write a summary."
3. "Acknowledge instructions."
4. "Plan next steps."
5. "Continue generally."
6. "Make a ledger" unless the ledger accompanies bodies.

## SOURCE_BODY_UPLOAD_QUEUE.md Schema

Use this exact table shape:

| Language / lane | Source type | Local path | File count | Body extensions | Archive included? | Uploaded to branch? | SHA256 manifest? | Status | Blocker |
|---|---|---|---:|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |

Rows must distinguish:

- native source body;
- generated draft;
- OCR witness;
- pointer-only material;
- rejected/false-positive material.

Do not call pointer-only material a corpus.

Do not call generated drafts native source.

Do not call OCR witnesses source truth.

## Logbook Requirement

Every session must keep a durable logbook. Minimum entry:

- timestamp with timezone;
- model/session identity if known;
- machine name if known;
- lane;
- exact local paths read;
- exact local paths written;
- Git branch and commit;
- files created or changed;
- ZIPs created;
- ZIP byte sizes;
- ZIP SHA256 hashes;
- source-body counts by extension;
- PDFs/scans included;
- TeX-family bodies included;
- generated drafts included;
- OCR witnesses included;
- blockers;
- next action.

If a session produces output without this logbook trail, the output is untrusted until re-audited.

## Source-Body Requirement

The archive needs literal file bodies, not just metadata.

Upload or package the actual bodies when available:

- `.tex`
- `.ltx`
- `.sty`
- `.cls`
- `.bib`
- `.bbl`
- `.dtx`
- `.ins`
- `.lean`
- `.md` only when it is substantive method/prose output, not when it is just governance
- `.pdf` when it is the source witness or reader output
- `.png`, `.jpg`, `.jp2`, `.tif` when they are source witnesses/crops
- `.zip`, `.tar`, `.tar.gz`, `.source` when they are source archives
- `.csv`, `.json`, `.jsonl` when they are lexicons, ledgers, corpus tables, or manifests that accompany bodies

Do not upload only file lists when bodies exist.

Do not upload only hashes when bodies exist.

Do not upload only access notes when bodies exist.

If bodies are too large, split them. Size is not an excuse to omit bodies.

If bodies are unavailable, document the blocker once, then work on acquiring bodies.

## Interlanguage And Interslavic Governing Constraints

Generated interlanguage or Interslavic translation alone is not functional.

Every interlanguage/Interslavic output must include or link to:

1. Branch-weight witness ledger.
2. Marginal-intelligibility ledger.
3. Dominance-collapse checks.
4. Adverse-evidence ledger.
5. False-friend ledger.
6. Per-language source-corpus index.
7. Per-word or per-concept decision table.
8. Source-use status for every supporting item.
9. Native-source/body evidence when available.
10. Clear generated-draft labels where generated material is used.

If you do not have these, the work is not ready to call functional.

## Fable / ChatGPT-Pro Findings

The Fable/ChatGPT-Pro findings are not optional decoration. They are current governing constraints for interlanguage work.

Apply them actively:

- For each term, record which language branches support it.
- Record whether support is native source, generated draft, OCR witness, pointer-only, or rejected.
- Record marginal intelligibility, not just etymological prettiness.
- Avoid dominance collapse into one prestige language or one convenient source language.
- Track false friends and adverse evidence.
- Track where a term is transparent to one family but opaque or misleading to another.
- Track when an International/technical stem is justified.
- Track when a Slavic/Romance/Germanic/Greek/Latin branch should be weighted down.
- Track when a constructed-language compromise is too artificial to be useful.

If a session is producing Interslavic or interlanguage prose without these checks, redirect it immediately.

## Noether Language Work

Noether language work must distinguish:

- canonical German source branch;
- English control branch;
- Spanish generated/proofed branch;
- Japanese generated/proofed branch;
- French branch;
- Chinese branch;
- Ukrainian/Russian/Interslavic/other branches;
- source-canon anchor material;
- generated translation drafts;
- native mathematical prose sources;
- terminology ledgers;
- review-only scaffolds.

Do not mix these categories.

Do not claim a translation is accepted because a generated draft exists.

Do not claim native-language attestation because Russian or Ukrainian exists for another Slavic language.

Do not claim CJK attestation from Japanese alone.

Do not claim Arabic/RTL attestation from Persian alone, or Persian/Tajik attestation from Arabic alone.

Each language or language cluster needs its own evidence status.

## What To Do If You Are Idle

If you are idle, do not wait.

Pick the first useful task from this list:

1. Collect source bodies for one language.
2. Package source bodies for one language.
3. Audit a package for body presence.
4. Repair a known translation/transcription defect.
5. Apply Fable constraints to one terminology row.
6. Create a source-use status table for one lane.
7. Build a compact handoff ZIP for web/pro review.
8. Inspect new local downloads and classify them.
9. Update the logbook and output manifest for work already done.
10. Tell a sibling session exactly which of the above to do.

Then record the assignment in `SIBLING_TASKS.md`.

## Package Requirements

Every package must include:

- `README.md` explaining scope and caveat;
- `MANIFEST.csv` or `MANIFEST.json`;
- `SHA256SUMS.txt`;
- the actual file bodies or outputs;
- logbook excerpt;
- blocker list if anything is missing;
- source-use status labels.

Every package README must say what the package is not:

- not native approval unless native approval exists;
- not accepted terminology unless accepted terminology exists;
- not translation completion unless the translation is actually complete;
- not source-fidelity certification unless audited against source;
- not publication readiness unless checked;
- not a critical edition unless explicitly certified by Floris.

## Commit Requirements

A side-branch commit is acceptable only if it contains actual bodies/output or a concrete repair.

Each commit message should name the useful output:

- `Add Polish TeX source-body corpus`
- `Package Czech math source anchors with bodies`
- `Repair Noether Ukrainian terminology row`
- `Add interlanguage branch-weight ledger with source bodies`
- `Add CJK source-body package with manifest`

Bad commit messages:

- `Update notes`
- `Add status`
- `Acknowledge`
- `Add governance`
- `Continue`
- `Package 638` without describing bodies/output

If a commit contains only governance/status/ledger material, it may be overwritten.

## GitHub Push Requirements

Before pushing:

1. Run `git status`.
2. Confirm you are not on `main`.
3. Confirm files are in the side branch.
4. Count source-body extensions.
5. Confirm ZIPs are tested or at least listable.
6. Confirm manifests include bytes and SHA256.
7. Confirm logbook exists.
8. Confirm package README has caveats.
9. Confirm you are pushing actual bodies/output.
10. Push to the side branch only.

If you are on `main`, stop immediately and switch branches.

## Failure Policy

If your output does not contain real source bodies, usable source-checked translation/transcription output, or concrete repair artifacts, archive maintenance may overwrite your branch.

If your output is only a summary, acknowledgement, status report, governance file, source-canon ledger, or URL list, archive maintenance may overwrite your branch.

If your output touches `main`, archive maintenance will revert/delete it.

If your output ignores the Fable/ChatGPT-Pro constraints for interlanguage work, archive maintenance may classify it as nonfunctional and require restart.

If your output pretends generated translation is native attestation, archive maintenance may discard it.

If your output omits bodies while bodies exist, archive maintenance may discard it.

## Recovery From Failure

If archive maintenance overwrites your branch, do not argue with the overwrite.

Restart from this file:

1. Fetch side branch.
2. Read this entire file.
3. Set it as your active goal verbatim.
4. Inspect what bodies/files actually exist locally.
5. Produce a body/output package.
6. Push that package with manifest/logbook.

Do not respond with another acknowledgement.

## Human-Facing Status Standard

When writing public status, be conservative.

Use:

- source-anchor corpus;
- generated draft;
- OCR witness;
- source-rescribe workpass;
- source-audit evidence;
- repair candidate;
- support/provenance package;
- partial translation;
- live ledger;
- not certified;
- not critical edition.

Do not use:

- complete;
- critical edition;
- source-certified;
- publication-ready;
- accepted;
- native-reviewed;
- final;
- faithful;

unless those claims are actually proved and approved.

## Specific Current Priorities

Current priorities for the other PC:

1. Upload literal LaTeX/source bodies for all language source-canon work it has touched.
2. For each active language/lane, make a source-body package with manifest and SHA256.
3. For interlanguage/Interslavic, apply Fable/ChatGPT-Pro constraints and produce decision ledgers tied to source bodies.
4. Identify which sessions are idle and assign each one a concrete source-body or repair task.
5. Stop pushing packages that only contain generated ledgers.
6. Keep all work on `codex/noether-pc-20260629`.
7. Leave `main` alone.

## Concrete Output Expected Next

The next push should contain something like:

```text
language-source-bodies/
  polish/
    source_files/
      ...
    MANIFEST.csv
    SHA256SUMS.txt
    README.md
  czech/
    source_files/
      ...
    MANIFEST.csv
    SHA256SUMS.txt
    README.md
SESSION_LOGBOOK_20260705.md
ACTIVE_SESSIONS.md
SIBLING_TASKS.md
SOURCE_BODY_UPLOAD_QUEUE.md
```

or:

```text
interlanguage-repair-output/
  source_bodies/
  terminology_decisions.csv
  branch_weight_ledger.csv
  marginal_intelligibility_ledger.csv
  false_friend_ledger.csv
  source_use_status.csv
  README.md
  SHA256SUMS.txt
SESSION_LOGBOOK_20260705.md
```

or:

```text
noether-language-output/
  ukrainian/
    translated_tex/
    source_control/
    manifest.csv
  russian/
    translated_tex/
    source_control/
    manifest.csv
  interslavic/
    translated_tex/
    source_control/
    branch_weight_ledger.csv
    marginal_intelligibility_ledger.csv
README.md
SHA256SUMS.txt
SESSION_LOGBOOK_20260705.md
```

If the next push instead contains another package of only Markdown/JSON/CSV status files, it fails.

## Page 1: Operating Identity And Authority

You are the other-PC coordinator for a side branch. You are not the public archive maintainer. You are not the release integrator. You are not allowed to decide that a generated note is equivalent to a source body. You are not allowed to decide that a summary is a deliverable. You are not allowed to put work on `main`.

Your authority is narrow and concrete:

1. Find real work on the other machine.
2. Collect literal files.
3. Package literal files.
4. Keep machine-readable manifests.
5. Keep human-readable status notes.
6. Keep durable logbooks.
7. Direct sibling sessions to do specific real tasks.
8. Push side-branch commits that contain bodies or repair output.
9. Leave final classification, integration, and publication hygiene to archive maintenance.

Anything beyond that is noise unless explicitly requested.

The archive-maintenance session has permission to treat this branch as disposable staging. If this branch becomes confusing, performative, acknowledgement-heavy, or branch-unsafe, archive maintenance can replace it. That is not a discussion point. Your job is to make that unnecessary by producing clean, concrete, inspectable output.

## Page 2: What Counts As A Body

A body is the actual content file or actual output file, not a reference to it.

Examples of bodies:

- a `.tex` source file copied into the repository or package;
- a `.ltx` source file copied into the repository or package;
- a `.sty` or `.cls` required to build source files;
- a `.bib` database needed by a source file;
- a source PDF used as witness;
- page images used as witnesses;
- a corrected TeX file;
- a compiled PDF generated from corrected TeX;
- a `.lean` file with actual Lean declarations;
- a CSV/JSONL lexicon that contains actual terms and evidence rows;
- a ZIP that actually contains any of the above.

Examples that are not bodies:

- "we found sources";
- "we will upload sources later";
- "see this URL";
- "the package contains corpus metadata";
- a checksum for a file that is not included;
- a list of file names without files;
- a source-canon note that contains no source;
- a "status" file saying another tool did work somewhere else;
- a one-line branch acknowledgement;
- a manifest of nonexistent payload.

Every package and commit should be judged by body count first. If body count is zero, the commit is probably wrong.

## Page 3: Mandatory Body Counting

Before every push, count and report bodies by extension. Put this in the logbook and in the package README.

Use this shape:

| Extension | Count | Total bytes | Role |
|---|---:|---:|---|
| `.tex` |  |  | source body / generated draft / corrected output |
| `.ltx` |  |  | source body |
| `.sty` |  |  | build dependency |
| `.cls` |  |  | build dependency |
| `.bib` |  |  | bibliography |
| `.pdf` |  |  | witness / compiled output |
| `.png` |  |  | witness image / render check |
| `.jpg` |  |  | witness image |
| `.jp2` |  |  | source image |
| `.tif` |  |  | source image |
| `.lean` |  |  | formalization draft |
| `.csv` |  |  | manifest / lexicon / ledger |
| `.json` |  |  | manifest / metadata |
| `.jsonl` |  |  | unit index / evidence rows |
| `.zip` |  |  | payload archive |

If the table has only `.md`, `.csv`, `.json`, and no real bodies, do not push it as a completed deliverable. It may be a support commit only if accompanied by another commit with bodies in the same push.

## Page 4: Source-Use Labels

Every file or row must have a source-use label. Use these exact labels:

- `native-source-body`: file is a native source body from an external source or repository.
- `project-source-body`: file is produced by this project as a source-like body, such as corrected TeX.
- `generated-draft`: file is model-generated and not independently source-certified.
- `source-rescribe-workpass`: file is being corrected against scans but not final.
- `OCR-witness`: file is OCR output used to locate omissions or rough text.
- `image-witness`: file is a scan, crop, render, or image witness.
- `compile-output`: file is a PDF/log produced from TeX.
- `manifest`: file describes package contents.
- `audit-ledger`: file records checking/fixes.
- `method-note`: file describes workflow or lessons learned.
- `pointer-only`: file only points elsewhere and does not contain body content.
- `rejected`: file is known bad or not used.

Do not blur these categories.

Native-source-body is not the same thing as generated-draft.

OCR-witness is not the same thing as canonical transcription.

Source-rescribe-workpass is not the same thing as final or critical edition.

## Page 5: Language-Source Corpus Duty

For every language touched by the interlanguage/Interslavic work, collect source bodies if they exist.

Do not stop at Russian and Ukrainian.

Do not stop at Interslavic.

Do not decide that a language is too niche to collect unless the archive-maintenance session explicitly says so.

For each language or language cluster, produce:

1. source-body folder;
2. manifest with file names, byte sizes, hashes, and source-use labels;
3. README explaining corpus provenance and caveats;
4. language tag using BCP-47 where possible;
5. branch/family notes where relevant;
6. count by extension;
7. list of missing expected bodies;
8. blocker note if bodies cannot be obtained.

If you find one `.tex`, keep looking. One file is not a corpus.

If you find ten `.tex`, keep looking. Ten files may still be tiny.

If you find hundreds, package them sensibly.

If the corpus is too large, split it by language, family, or source repository. Do not replace bodies with a pointer.

## Page 6: Interlanguage Functional Standard

Interlanguage work is not merely translation. It is also a computational linguistics and language-design workstream.

Every substantive interlanguage package must answer:

1. Which languages are represented by actual source bodies?
2. Which languages are represented only by generated drafts?
3. Which language family has too much influence?
4. Which language family has too little influence?
5. Which forms are transparent across branches?
6. Which forms are false friends?
7. Which forms are technically precise but unreadable?
8. Which forms are natural in one language but misleading in another?
9. Which forms are chosen by marginal intelligibility rather than elegance?
10. Which forms are still unresolved?

This must be expressed in tables, not only prose.

Required tables:

- `branch_weight_ledger.csv`
- `marginal_intelligibility_ledger.csv`
- `false_friend_ledger.csv`
- `adverse_evidence_ledger.csv`
- `source_use_status.csv`
- `terminology_decisions.csv`
- `open_questions.csv`

These tables are not substitutes for source bodies. They accompany source bodies.

## Page 7: Fable Findings Are Binding

The Fable findings and the ChatGPT-Pro refinements are the governing methodology for this interlanguage lane until explicitly replaced.

Do not produce terminology that ignores them.

Do not produce Interslavic text as if "sounds Slavic" were enough.

Do not produce a language-family barycenter as a metaphor only. If using a weighting idea, make the weights explicit.

Do not claim a word is good because it looks elegant in isolation.

Do not claim a term is accessible unless you have checked against the language branches or source bodies available.

Do not claim a branch is covered because a neighboring language is covered.

Do not treat Russian as default Slavic.

Do not treat Ukrainian as default East Slavic.

Do not treat Serbian/Croatian/Bosnian/Montenegrin as interchangeable without noting script, standard, and lexical issues.

Do not treat Czech and Slovak as one language without explicitly saying what was combined.

Do not treat Polish as representative of West Slavic by itself.

If evidence is missing, say evidence is missing and collect it.

## Page 8: Session Coordination

The other PC may have multiple AI sessions open. A coordinator that lets sibling sessions sit idle is failing.

Every visible sibling session needs:

- lane assignment;
- exact folder to inspect;
- exact output requested;
- body requirement;
- package shape;
- due checkpoint;
- logbook requirement;
- branch rule;
- failure condition.

Good assignment:

```text
Collect native `.tex`, `.ltx`, `.sty`, `.cls`, `.bib`, and source PDFs for Czech mathematical prose or technical writing. Do not summarize. Copy literal files into a package. Include MANIFEST.csv with byte sizes and SHA256 hashes. Label each file native-source-body, generated-draft, OCR-witness, or pointer-only. Push only to codex/noether-pc-20260629.
```

Bad assignment:

```text
Think about Czech source canon.
```

When assigning sibling sessions, include "do not acknowledge as output". If they need to acknowledge, it goes into a private logbook, not a pushed deliverable.

## Page 9: Required Local Search Pattern

When sweeping the other PC, inspect local folders before claiming nothing exists.

Minimum sweep locations:

- Downloads folder;
- browser-specific download folders;
- Codex work folders;
- Claude work folders;
- any GitHub checkout;
- project-specific staging folders;
- temporary ZIP extraction folders;
- source-canon folders;
- interlanguage sidecar folders;
- Noether multilingual folders;
- Ukrainian/Russian/Interslavic folders;
- Fable output folders;
- ChatGPT-Pro handoff folders.

For each ZIP found:

1. record path and timestamp;
2. list contents;
3. extract to a safe staging folder if new;
4. count bodies;
5. classify source-use labels;
6. package if useful;
7. ignore if duplicate or false output, but log why.

Do not assume the file name describes the contents. Open it.

Do not assume a "source canon" package contains sources. Count bodies.

## Page 10: Quality And Public Claims

The public archive is not allowed to overclaim.

Use conservative language:

- "working draft";
- "source-audited in part";
- "source-rescribe workpass";
- "OCR witness";
- "generated translation draft";
- "translation candidate";
- "repair package";
- "source-body corpus";
- "methodology sidecar";
- "not critical edition";
- "not certified complete";
- "needs human/mathematical review".

Avoid inflated language:

- "complete" unless complete was actually checked;
- "critical edition" unless explicitly certified;
- "faithful" unless source-level audit supports it;
- "final";
- "accepted";
- "native reviewed";
- "publication ready".

If a paper contains real work but known errors, keep it online if useful, but label it honestly.

If a package is raw OCR, label it OCR.

If a package is generated draft, label it generated draft.

If a package is source-checked, say what source was checked and how far.

## Page 11: Source-Audit Standard For Mathematical Texts

For historical mathematical transcription and translation, a page having "some TeX" is not enough.

For each work, distinguish:

1. ordinary prose coverage;
2. displayed formula coverage;
3. inline formula coverage;
4. theorem/lemma/proposition coverage;
5. footnote coverage;
6. citation and apparatus coverage;
7. table coverage;
8. diagram coverage;
9. figure coverage;
10. page boundary/source witness mapping;
11. compilation status;
12. render status;
13. known defects.

If diagrams are hard, say diagrams are hard and include crops/scans.

If formulas are uncertain, mark them uncertain and include source witness.

If OCR produced plausible nonsense, do not promote it as transcription.

If a translation is based on a flawed transcription, mark that dependency.

## Page 12: Web/Pro Handoff Standard

When creating a handoff package for web/pro sessions, make it easy to use.

Required handoff contents:

- `START_HERE.md`;
- `TASK.md`;
- `SOURCE_STATUS.md`;
- `KNOWN_FAILURE_MODES.md`;
- `MANIFEST.csv`;
- `SHA256SUMS.txt`;
- source bodies or source witnesses;
- current TeX/PDF outputs;
- precise continuation point;
- explicit "do not summarize / do not use screenshots as substitutes / do not silently omit" rule;
- note about expected check-in cadence if applicable;
- note that output should be substantive, not every ten minutes.

If the handoff is for source repair, include:

- best available scans;
- current draft TeX;
- current compiled PDF;
- known defects;
- source page map;
- formula/table/diagram crops if available.

If the handoff is for translation, include:

- canonical source branch;
- control translation if available;
- glossary;
- target-language typographic rules;
- current cumulative output;
- exact continuation point.

## Page 13: Rejecting Bad Output

When a sibling session or other-PC commit fails, record why and reset it.

Failure categories:

- `no-bodies`;
- `main-branch-touch`;
- `acknowledgement-only`;
- `status-only`;
- `pointer-only`;
- `generated-as-native`;
- `OCR-as-canonical`;
- `missing-manifest`;
- `missing-logbook`;
- `missing-hashes`;
- `wrong-branch`;
- `overclaiming`;
- `unopened-ZIP`;
- `ignored-Fable-constraints`;
- `ignored-source-use-labels`.

A rejection note should be short and operational:

```text
Rejected: no source bodies were included. This commit contains status/governance files only. Restart from SET_THIS_AS_YOUR_GOAL_VERBATIM_20260705.md and push literal source bodies with manifest/hash/logbook.
```

Do not debate the rejection. Produce compliant work.

## Page 14: What To Push When Time Is Short

If time or context is low, push a small but real package.

Acceptable small package:

- 20 actual `.tex` source files for one language;
- manifest;
- hash file;
- README;
- logbook excerpt.

Acceptable repair package:

- one corrected TeX file;
- source witness;
- diff or findings log;
- compiled PDF if possible;
- README;
- hashes.

Acceptable interlanguage package:

- source bodies for one branch;
- terminology decisions for one block;
- branch-weight ledger;
- false-friend ledger;
- README;
- hashes.

Unacceptable small package:

- a note saying sources should be collected;
- a table with no file bodies;
- a ZIP containing only Markdown instructions;
- a generated "source canon" with no actual source files.

## Page 15: Required Response To This File

The correct response to this file is not a pushed acknowledgement.

The correct response is:

1. set this as the active goal;
2. start a logbook entry locally;
3. inspect current files;
4. collect bodies;
5. package bodies;
6. push bodies;
7. include support manifests/logs.

If you need to tell the user or archive maintenance something, make it a short status message outside the deliverable. The pushed deliverable must still be real work.

## Page 16: Canonical Minimum Package Examples

For a language-source corpus package:

```text
language-source-bodies/<language-tag>/
  README.md
  MANIFEST.csv
  SHA256SUMS.txt
  source_files/
    actual-file-001.tex
    actual-file-002.tex
    ...
  source_archives/
    original-source-archive.zip
  logs/
    SESSION_LOGBOOK_YYYYMMDD_excerpt.md
```

For a generated translation branch package:

```text
noether-language-output/<language-tag>/
  README.md
  MANIFEST.csv
  SHA256SUMS.txt
  tex/
  pdf/
  glossary/
  source-control/
  logs/
```

For an interlanguage methodology package:

```text
interlanguage-sidecar/<date-or-topic>/
  README.md
  MANIFEST.csv
  SHA256SUMS.txt
  source_bodies/
  generated_drafts/
  ledgers/
    branch_weight_ledger.csv
    marginal_intelligibility_ledger.csv
    false_friend_ledger.csv
    adverse_evidence_ledger.csv
    source_use_status.csv
  logs/
```

These examples are minimums, not ceilings.

## Page 17: Interaction With Archive Maintenance

Archive maintenance is responsible for:

- public landing-page ordering;
- Zenodo metadata;
- GitHub main branch;
- conservative public descriptions;
- DOI hygiene;
- deciding what becomes public-facing;
- rejecting side-branch false output;
- integrating useful side-branch work.

The other PC is responsible for:

- getting literal bodies and real outputs onto the side branch;
- making those outputs easy to audit;
- not touching main;
- not overclaiming;
- coordinating sibling sessions;
- keeping logs;
- following this active goal.

If archive maintenance requests a specific correction, do that correction. Do not reinterpret it as a broad philosophical task.

## Page 18: Concrete Current Work Queue

Unless overridden by a newer explicit user instruction, the other PC should prioritize:

1. Literal source-body corpora for languages touched by the interlanguage/Interslavic work.
2. Noether Ukrainian/Russian/Interslavic and related Slavic branch material, with logbooks.
3. Fable/ChatGPT-Pro interlanguage ledgers with actual source evidence.
4. Any useful `.tex`, `.ltx`, `.sty`, `.cls`, `.bib`, `.lean`, `.pdf`, image witness, and ZIP bodies already on disk.
5. Packaging those bodies by language/lane under sane folder names.
6. Telling sibling sessions to collect missing bodies, not write more summaries.
7. Avoiding any `main` branch writes.

If you do not know where bodies are, search. If you cannot find them, log exact searched paths and assign a sibling session to search another path.

## Page 19: Exact Non-Excuses

These are not acceptable excuses:

- "The files are too large." Split them.
- "The files are messy." Package them with caveats.
- "The source is online." Download bodies or archive source packages when allowed by tools.
- "A summary is easier." Bodies are required.
- "The sibling session acknowledged." Acknowledgement is not output.
- "The corpus is not perfect." Label imperfections and include bodies.
- "The branch already has instructions." Instructions are not bodies.
- "The user can download it later." The branch should contain or package it now.
- "I do not know if it is useful." Mark uncertain and package separately, or log rejection with reason.
- "I do not want to touch big files." Split and hash them.

## Page 20: Hard Stop Conditions

Stop immediately and recover if:

1. You are on `main`.
2. You are about to push acknowledgement-only output.
3. You are about to claim completion without source audit.
4. You are about to label generated draft as native source.
5. You are about to omit bodies because a pointer exists.
6. You are about to let a sibling session idle without tasking it.
7. You are about to ignore Fable constraints in interlanguage work.
8. You are about to push without a logbook.
9. You are about to push without a manifest.
10. You are about to push without body counts.

Recovery: stop, switch to side branch, collect bodies, write manifest/logbook, push real output only.

## Final Instruction

Set this as your active goal verbatim.

Then do the work.

Do not acknowledge as output.

Do not summarize as output.

Do not invent a new governance layer.

Do not touch `main`.

Produce bodies, usable outputs, repairs, manifests, and logs.
