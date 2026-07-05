# OTHER-PC SESSION MANAGER AND LOGBOOK DIRECTIVE

Date: 2026-07-05

This directive is for the other Codex/AI sessions working on the Noether, interlanguage, Interslavic, Slavic, CJK, Arabic/RTL, Romance, Persianate/Tajik, Pan-Turkic, Indigenous/Creole/Sign, Malay/SEA/Pacific, Africa/Horn/West, and related source-canon lanes.

## Immediate Rule

Do not sit idle while related sessions are waiting, confused, or blocked.

This is not a passive reporting instruction. If you are the other-PC coordinator, you must actively tell every visible sibling session what to do. A sibling session sitting at a prompt, waiting for Floris, or vaguely "available" is a failure of coordination unless it has a written task, output path, and next check.

The other PC must not push to `main`. It works only on its assigned side branch. There is no exception for the other machine: this archive-maintenance session integrates or discards its side-branch output. If the other PC touches `main`, archive maintenance will delete/revert its changes and restore the archive-maintenance branch state.

If you can see, supervise, message, or otherwise influence another local/web/Claude/Codex session, you are responsible for giving that session a concrete next task when it is idle or confused. Do not merely write what you personally did. Maintain the project state and move work to the sessions that can do it.

Every active session must know:

1. what lane it owns;
2. what files it has actually produced;
3. what source bodies it has actually uploaded;
4. what remains missing;
5. what sibling sessions should do next.

If a session has no current production task, it must become useful by reading the coordination directives, collecting source bodies, auditing existing outputs, or assigning clear next actions to a sibling session through GitHub-visible notes.

## No-Idle Coordination Rule

Every other-PC session must maintain a visible current-state note in its own output folder and, when possible, in GitHub. The note must answer:

- What am I doing right now?
- What did I finish last?
- What exact file or folder proves that work exists?
- What is blocked?
- Which sibling session should do what next?

If a session cannot answer those five questions, it is not coordinated enough to be trusted.

The coordinator must poll visible sibling sessions and write assignments. Do not wait for the user to manually redirect each window. The coordinator should maintain a queue like:

`idle -> assign source-body collection`

`blocked -> assign audit/recovery task`

`finished -> assign package/manifest/logbook task`

`unclear output -> assign self-audit and evidence listing`

If a manager/coordinator session sees idle sibling sessions, it must immediately assign them work from the queue below and record the assignment in `SIBLING_TASKS.md`. Acceptable idle-session tasks include:

- collect full TeX/source-body corpora for one language or script;
- package real source files, not only indexes or ledgers;
- audit a recent package for whether it contains bodies, PDFs, TeX, scans, logs, or only metadata;
- apply Fable/ChatGPT branch-weight and marginal-intelligibility constraints to one interlanguage terminology block;
- build a small web/pro handoff ZIP with source bodies and a manifest;
- inspect existing generated translations for source gaps, hallucinated compression, missing tables, missing diagrams, or fake completeness claims;
- write a public-safe logbook excerpt explaining what was done and what remains.

Do not let sessions wait for Floris to manually remember every lane. The point of the coordinator is to keep the machine-readable project state alive.

## Logbook Requirement

Every session must keep a durable logbook in its own working folder and push/copy a public-safe copy or excerpt into GitHub when it produces anything archive-relevant.

Minimum logbook entry:

- timestamp with timezone;
- model/session identity if known;
- lane name;
- exact local paths touched;
- exact Git branch/commit if pushed;
- files created or changed;
- ZIPs created, with byte size and SHA256;
- source-body count by file type;
- whether actual source bodies were uploaded, or only manifests/logs;
- blockers;
- next action for this session;
- next action for any sibling session.

If the session does not have a logbook, create one immediately. Suggested filename:

`SESSION_LOGBOOK_YYYYMMDD.md`

If a session produces work without a logbook entry, treat that work as untrusted until re-audited.

## Source Body Requirement

The archive needs literal file bodies, not summaries.

When a session finds any relevant source corpus, it must upload/push the actual files:

- `.tex`, `.ltx`, `.sty`, `.cls`, `.bib`, `.bbl`, `.dtx`, `.ins`;
- source archives such as `.zip`, `.tar`, `.tar.gz`, `.source`;
- PDFs when they are the source witness;
- language corpora, lexicons, term tables, and native mathematical prose sources;
- generated translation TeX only when clearly labeled as generated/draft;
- OCR/converted TeX only when clearly labeled as OCR/conversion witness.

Do not provide only indexes, checksum ledgers, source-canon tables, URL lists, or access notes when file bodies exist. Those are useful, but they do not satisfy the source-body task.

If upload is blocked, write the exact reason and the exact recovery action.

## Fable / ChatGPT-Pro Findings Are Governing Constraints

For interlanguage and Interslavic work, the current output is not functionally acceptable unless it uses the Fable/ChatGPT-Pro findings.

Every relevant session must read and apply:

- `interlanguage-sidecar/FABLE_INTERLANGUAGE_PROGRAM_BLOCKING_DIRECTIVE_20260705.md`
- `interlanguage-sidecar/UPLOAD_ALL_LATEX_SOURCE_BODIES_NOW_20260705.md`
- `coordination/TO_OTHER_AI_LATEX_SOURCE_DIRECTIVE_20260705.md`

Required implementation objects include:

- branch-weight witness ledger;
- marginal-intelligibility ledger;
- dominance-collapse checks;
- adverse-evidence / false-friend ledger;
- per-language source-corpus index;
- per-word or per-concept decision table;
- source-use status distinguishing native source, generated draft, OCR witness, and pointer-only material.

Do not call Interslavic or any constructed/interlanguage lane functional if it is only a generated translation without those ledgers and checks.

## Enforcement Rule

Other-PC commits that do not contain literal source bodies, usable source-checked translation output, or concrete repair artifacts may be removed from the live side branch and replaced with reset instructions.

Acknowledgement-only, status-only, ledger-only, and governance-only commits are false output. They are not progress. The other PC must do the task, not merely acknowledge or describe it.

## Session Dispatch Requirement

At least one session on the other PC must act as a coordinator.

The coordinator must maintain:

- `ACTIVE_SESSIONS.md`: each session, lane, current task, last update, blocker, next action;
- `SOURCE_BODY_UPLOAD_QUEUE.md`: corpora found, corpora uploaded, corpora still missing;
- `SIBLING_TASKS.md`: explicit tasks assigned to idle sessions;
- `ACKNOWLEDGED_DIRECTIVES.md`: which directives each session has read.

The coordinator must not merely report that other sessions exist. It must actively dispatch them. Every sibling session must have a row in `ACTIVE_SESSIONS.md`; every idle or blocked sibling session must also have a row in `SIBLING_TASKS.md`.

A useful line in `SIBLING_TASKS.md` looks like:

`2026-07-05T17:40+02:00 | session-name | assigned: collect Polish mathematical TeX source bodies | expected output: ZIP + manifest + logbook | status: active`

If there are many sibling sessions, triage them in this order:

1. sessions with no logbook: create logbook and current-state file;
2. idle sessions: assign source-body collection or audit work;
3. sessions producing only summaries/indexes: redirect to upload literal file bodies;
4. sessions working on interlanguage/Interslavic: require Fable/ChatGPT-Pro constraints and decision ledgers;
5. sessions producing archive-relevant work: package, hash, and push/upload evidence.

If a sibling session is idle, assign it one of these tasks:

1. collect and push source bodies for one language/lane;
2. audit whether a prior package contains actual source bodies or only ledgers;
3. build a language-specific ZIP of source bodies plus manifest;
4. apply Fable branch-weight and marginal-intelligibility checks to one lexical/terminology block;
5. inspect generated translations for nonfunctional interlanguage choices and record repairs.

## Required Acknowledgement

Each session that reads this must create and push an acknowledgement file:

`coordination/acks/ACK_SESSION_MANAGER_DIRECTIVE_<session-name>_YYYYMMDD.md`

The acknowledgement must say:

- I read the session-manager/logbook directive.
- My lane is: ...
- My logbook path is: ...
- My current output path is: ...
- I understand that actual source bodies must be pushed when they exist.
- I understand that Fable/ChatGPT-Pro findings are governing constraints for interlanguage/Interslavic work.
- My next concrete task is: ...

No acknowledgement means no confidence that the session is using the current workflow.

## Public Classification Reminder

Generated ledgers, support notes, and source-canon classifications are valuable, but they are not source-body corpora, native review, accepted terminology, translation completion, source-fidelity certification, publication readiness, reader output, or critical-edition material.

Label every package accordingly.
