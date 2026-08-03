# Archive-maintenance reconstructed operating charter

Date: 2026-08-03

Status: controlling successor-session charter for the GitHub/Zenodo archive,
corpus-preservation, reader-presentation, provenance, and continuation lane.

## 1. Why this charter exists

The retired archive task `<RETIRED_OVERSIZED_ARCHIVE_TASK>` accumulated a
7,809,200,465-byte rollout and eventually entered an auto-compaction retry loop.
It must remain idle history. It must not be reopened, replayed, or treated as the
only place where operating state lives.

This charter reconstructs the durable program from:

- the complete top-level user-message extraction from the retired rollout;
- a full read of the final week and bounded reads across the earlier history,
  including the original May 26-27 mandate and later corpus/publication controls;
- the current Git tree, catalogs, receipts, public-record maps, and append-only
  archive logbooks;
- the EGA pre-Stacks and SGA/FAC/GAGA semantic-index controls;
- the dual-DOI logbook control and the successor/bootstrap protocol; and
- the current live GitHub/Zenodo closeout state.

The local top-level extraction contains 1,615 user messages from 2026-05-26
through 2026-08-02, is 1,498,941 bytes, and has SHA-256
`306B0466822951C9A8D56F96DA1C7BACEE6926796B066544F42518AA4B98C8DA`.
It is private reconstruction evidence, not a public transcript. The public
charter records the governing lessons without publishing private conversation.

## 2. Mission and ownership

This task is the preservation and publication authority for the entire modern
mathematics-manuscript/interlanguage program. It is not merely an SGA upload
queue and it is not merely a Zenodo transport script.

It owns:

1. exact private custody of producer/source states;
2. bounded coherent byte snapshots of live work;
3. derived privacy-clean public projections while leaving source bytes intact;
4. GitHub publication, branches, commits, pushes, pull requests, merges,
   catalogs, manifests, receipts, and commit-pinned public readback;
5. Zenodo concept/version/draft control, same-concept publication, metadata,
   file ordering, default previews, exact file/member verification, and
   anonymous public readback;
6. public and private provenance, decision, reversal, error, supersession, and
   continuation custody;
7. corpus-wide status and dependency maps, including the EGA and SGA semantic
   indexing/formalization scaffolds;
8. crash-safe continuity: ensuring that useful coherent work is off the PC
   promptly and can be resumed from exact cursors after compaction or failure;
9. preservation and routing of the complete source corpus, not manifest-only
   substitutes; and
10. the periodic bounded archive sweep while any production lane remains live.

Production lanes retain primary responsibility for translation, transcription,
source correction, mathematical adjudication, diagram reconstruction, and
visual QA. Archive maintenance must not duplicate or disrupt an active disjoint
producer. It nevertheless owns the program-level completion obligation: track
the exact unfinished scopes, preserve every coherent checkpoint, keep the
responsible lane moving, and resume from its immutable source/logbook/cursor if
that lane disappears or is retired. A corpus is not dropped from this goal just
because a separate task currently performs the page work.

## 3. Preserve and organize; do not editorially curate

The standing instruction is: archive and preserve the work; do not curate it,
rank it away, or keep only the generation that looks best.

Therefore:

- Preserve every distinct source byte sequence, draft, correction, decision,
  error, reversal, rejected choice, superseded generation, continuation record,
  and source witness that is within the program.
- Organize by corpus, work, language, generation, authority, provenance,
  supersession, and quality state. Organization may change the public shelf; it
  may not erase history.
- Deduplicate exact duplicate containers and transports when this makes the
  current shelf coherent. Never deduplicate distinct content merely because two
  files have similar names or claims.
- Keep unmodified producer/source snapshots in private custody. Any public
  privacy remediation is a separate derived projection with a complete,
  minimal, reproducible transformation ledger.
- Preserve rights-uncertain or privacy-bearing bytes privately when they cannot
  be public as-is. Publish a rights/privacy-clean projection, exact metadata, or
  a minimally transformed successor without silently pretending the source did
  not exist.
- Preserve predecessors through immutable Zenodo versions and Git history.
  Current-reader ordering is not permission to delete adverse history.
- Compilation success, filenames such as `complete` or `critical`, and package
  manifests are not source-fidelity proof. Claims remain scoped to actual
  authority comparison and recorded QA.

“Front the current reader” and “preserve everything” are compatible. A reader
should not have to scroll through hundreds of internal fragments before reaching
the book, while a mathematician must still be able to recover the full evidence,
source closure, decisions, and superseded history.

## 4. Corpus-completion register

### 4.1 EGA is a first-class completion obligation

The goal includes completion and preservation of the canonical diplomatic
French EGA 0-IV corpus for all eight bounded NUMDAM publications. The diplomatic
French is the immutable textual authority hub. The existing English reader is
not authority for the French and no inherited English correction survives merely
because it reads well.

Required EGA work:

- complete the continuous canonical French TeX corpus for EGA 0, I, II, the
  complete published EGA III text, and EGA IV;
- compare every inherited English source correction with the NUMDAM authority,
  retain supported corrections, and append-only reverse unsupported ones;
- preserve exact source-page, printed-page, TeX, statement, formula, diagram,
  citation, page-seam, and continuation identities;
- keep the current standalone readers and the cumulative EGA 0-IV reader
  coherent and linked as source work advances;
- preserve the eight NUMDAM authority identities, French/corrected/English
  layers, source-defect evidence, and all correction/reversal rationale; and
- never call the canonical French corpus complete until every admitted source
  page and terminal matter is represented and the cumulative checks close.

Current reader-level public completion does not discharge this obligation. The
1,356-page linked English EGA 0-IV reader on the existing EGA concept is a useful
working reader, while the canonical diplomatic French and exhaustive semantic
closure continue independently.

### 4.2 EGA pre-Stacks machine-readable scaffold

Controlling file identity:

- `EGA_PRESTACKS_MACHINE_READABLE_INDEXING_SCAFFOLD_20260802.md`
- 47,731 bytes
- SHA-256
  `4DB40D004F016D16BB620A61C11F2F963EA4629B647618769C74AFE4EEE025CA`

The scaffold is part of the deliverable, not optional administrative garnish.
Maintain one stable semantic graph rooted in diplomatic French. English and all
later natural-language or formalization layers attach to the same IDs rather
than inventing parallel object graphs.

At minimum preserve and eventually close:

- volume, chapter, section, paragraph, and unnumbered source units;
- definitions, conventions, remarks, examples, propositions, lemmas,
  corollaries, theorems, and proofs;
- formulas, exact sequences, diagrams, tables, source notes, named objects,
  constructions, hypotheses, conclusions, and scopes;
- proof-use, definition-use, comparison, forward-pointer, range,
  cross-volume, and external-citation dependencies;
- terminology and notation bindings across languages;
- source-error, English-normalization, repair, reversal, and erratum IDs; and
- candidate/verified Stacks and formalization links with explicit status.

Required machine surfaces include semantic entities, semantic relations,
source-target alignment, terminology glossary, formula/notation index, diagram
index, external-architecture map, and complete reference/action/residual tables.
Stable IDs must survive line and page-coordinate changes. Ambiguity remains
explicit. During page production capture only source-certain inexpensive facts;
do not stall continuous transcription for speculative ontology work. At bounded
and cumulative gates regenerate coordinates, close referential integrity, and
run exhaustive reference/dependency checks. The incremental EGA I page-seam
nodes through p.126 are durable starting state, not disposable notes.

### 4.3 SGA, FAC, and GAGA corpus and semantic scaffold

Controlling file identity:

- `SGA_FAC_GAGA_SEMANTIC_INDEXING_AND_FORMALIZATION_SCAFFOLD_20260802.md`
- 6,190 bytes
- SHA-256
  `F5E54638B569157DC355FFD3C3A283111BD26ABA1834C8F618A40B8BBC2F1601`

Maintain canonical diplomatic/corrected French, source-aligned English, readers,
and machine-readable semantic/provenance layers for SGA 1-7 II, FAC, and GAGA.
The semantic graph must cover works/volumes/exposés/sections, mathematical
objects and statements, formulae, diagrams, citations, terminology, source
defects, corrections, dependencies, cross-volume references, supersession,
language attachments, and Stacks/Lean candidate/verified/formalized states.
Candidate mappings are never labeled verified without mathematical comparison.

For SGA specifically:

- preserve and continue canonical French source repair/transcription across
  SGA 1-7 II;
- preserve complete standalone English readers and the clean cumulative
  SGA 1-7 II reader with internal and cross-volume navigation;
- preserve native diagrams, exhaustive references, source-correction layers,
  and all image evidence actually used for difficult readings;
- keep Loop 1 continuous text/equations moving independently of Loop 2 native
  diagrams/exhaustive references/release QA;
- never allow a disjoint Loop 2 issue to erase or stall safe Loop 1 custody;
  and
- keep every standalone reader and source closure directly recoverable even
  when the global reader is fronted.

FAC routing is currently a specific exception to the broad provenance rule. The
producer owns creation of a dedicated FAC comparative-translation/AI-evidence
DOI. Archive maintenance must not mint that concept and must not now copy the
frozen 19-file comparator package into the broad methodology/replication records.
If earlier broad records already contain related files, preserve that immutable
history and report exact differences so the dedicated FAC record can cite or
supersede it. Do not destructively erase history.

GAGA must have a separate pure new-translation concept after a finished exact
GAGA package is available. Archive maintenance owns that publication line. Do
not mix FAC translation or comparator evidence into the GAGA concept.

### 4.4 Other manuscript and interlanguage obligations

The archive goal also retains and advances, without false completion claims:

- Emmy Noether: German/source-control, the cumulative English corpus,
  multilingual readers, bounded source audits, correction/reversal history,
  and language-specific continuation states;
- Heinrich Weber: all three volumes, complete German Volume I working reader,
  the continuing cold source pass, Volume II/III work, and English
  synchronization;
- Pierre Deligne: D001-D090 and supported letters, bilingual/source-aligned
  readers, diagram/formula evidence, exact disjoint lane boundaries, and
  continuation cursors;
- Arthur Cayley: all suspect inherited material as repair provenance, source
  masters and page-level repairs, without promoting any range as source-faithful
  until exact re-audit warrants it;
- Gauss, Dedekind, Dirichlet, Riemann, Poincaré, Frobenius, Kneser, Sylvester,
  Bianchi, Gordan/Clebsch-Gordan, Steinitz, Gibbs, Maxwell, al-Battani, and the
  classical/additional author shelves;
- Galois, Eisenstein, Steiner, and other source-intake-only lanes until they
  acquire genuine reader/source-audited promotion;
- Chinese, Japanese/Seki, Indian/Sanskrit, Islamic/Arabic, Persianate, Ukrainian
  applied mathematics, historical-reference, and other non-European corpora;
- all interlanguage families actually touched: Romance, English/Germanic,
  Slavic/Interslavic, CJK, Arabic/Persianate/RTL, Turkic, Africa/Horn/West,
  Malay/SEA/Pacific, Indigenous/Creole/Sign, and later lanes;
- complete source-body trees and native-language inputs, not source-canon
  ledgers that merely point to missing files;
- compute-reuse image datasets made from recent source-audit crops actually used
  in transcription/translation, with page/folio, parent hash, rasterization,
  bbox, dimensions, DPI where known, linked unit, disposition, and image hash;
- Lean 4/mathlib-style formalization sidecars, separated from source-fidelity
  claims; and
- the split-zero research sidecar as its own exploratory record, never confused
  with manuscript-edition completion.

New substantive work in any of these families is in scope even when an older
front page has not mentioned it recently.

## 5. Public presentation rules

Every landing description is a complete current description of the project or
corpus. It is not a release-note diff, internal handoff, “hold” memo, model
status report, or account of the latest command.

For a cumulative corpus such as SGA or EGA, use this durable reader-facing order:

1. one complete current reader/source ZIP sorts first for one-click custody;
2. the clean cumulative reader PDF sorts second and is the selected/default
   preview;
3. clean standalone reader PDFs follow in mathematical/corpus order;
4. direct master TeX and buildable source closures follow;
5. provenance, QA, logbooks, decision/reversal history, prior generations, and
   other support are grouped coherently after the readers.

For author/work records without a meaningful cumulative book, adapt the same
principle: coherent reader(s) first, editable source next, complete artifacts
and history in clearly named archives. Do not expose a hundred tiny fragments
ahead of the book. Do not hide the only useful reader inside a ZIP.

Reader hygiene is strict:

- no AI/model names, workflow prose, source/status notes, task narration,
  quality disclaimers, correction-history narration, or archive commentary in
  the mathematical reader body;
- no AI-written explanatory footnotes masquerading as source text;
- genuine source-era author/editor notes remain when they belong to the work;
- project status, caveats, transformations, errors, and reversals live in the
  landing metadata, logbooks, manifests, and change/supersession records; and
- correcting presentation prose never licenses altering mathematical text.

Useful imperfect work goes online promptly under an honest working/provisional
label. A local PC crash must not erase a day of work. “Promptly” does not mean
uploading an incoherent mid-write directory: first freeze the smallest coherent
byte snapshot, then preserve/publish it. Do not withhold a coherent partial
reader merely because a later pass, diagram, or certification remains open.

## 6. Privacy, rights, provenance, and logbooks

Archive maintenance owns privacy remediation. It must not wait for a producer to
invent a privacy-clean transport.

For every substantive snapshot:

1. preserve the immutable producer/source bytes privately;
2. scan the exact proposed public boundary;
3. create a separate derived privacy-clean projection if necessary;
4. make only minimal replacements needed for privacy;
5. log original identity, derived identity, every transformation, path/member,
   bytes, hashes, and rationale;
6. verify manifests, ZIP members, rights exclusions, supersession, and
   continuation boundaries; and
7. publish/read back the derived bytes without claiming that the source package
   itself was mutated.

Do not invent a license. Distinguish underlying-work rights, scan/publisher
rights, contributor code/text licenses, and record-level metadata. Source scans
or third-party comparisons excluded from a public payload remain exact private
custody with hashes and public caveats where appropriate.

Controlling dual-DOI logbook requirement:

- `PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md`
- 2,296 bytes
- SHA-256
  `BFA1E3A3EDA94E8C3425BAE50C842610A47D508FB260BF761BA3206883012679`
- methodology concept DOI `10.5281/zenodo.21124403`
- replication concept DOI `10.5281/zenodo.20461174`

For every applicable substantive successor, privacy-clean immutable project
logbooks, decision rationale, append-only correction/reversal/error history, and
continuation surfaces are first-class deliverables on both concepts. Bind every
surface by exact relative path, bytes, SHA-256, privacy result, and supersession
state. Keep them directly discoverable and inside the appropriate provenance ZIP
where useful; never leave them only in an unpublished local tree. If size forces
splitting, use exact cross-record linkage and never drop the logs.

The FAC dedicated-DOI supersession in section 4.3 controls over the immediately
preceding broad dual-DOI FAC routing request. All other applicable producer
logbooks remain subject to the dual-DOI rule unless a later explicit corpus-
specific routing instruction supersedes it.

Keep the private raw decision history append-only. Publish a professional,
privacy-clean projection suitable for mathematicians to audit the reasoning.
Redaction or cleanup must not erase the fact, timing, rationale, or reversal of a
decision.

For `ENGLISH_GERMANIC_DECISION_LOG_v1.jsonl`, never edit, replace, or append from
a cached whole-log snapshot. Prepare one new JSON record and invoke only
`append_english_germanic_decision_log.ps1 -RecordPath <exact-record>` so the
helper rereads and validates the locked live file, rejects duplicate IDs,
flushes, and rolls back on failure.

## 7. GitHub and Zenodo transaction protocol

### 7.1 Before mutation

- Resolve the exact current public head, concept DOI, record/version DOI,
  deposition/draft state, file set, metadata, default preview, and predecessor.
- Search exact title/concept/deposition identities to prevent duplicate concepts
  and parallel drafts.
- Reconcile the local branch with current `origin/main` without destructive
  reset and without discarding unrelated user changes.
- Verify local exact paths, bytes, SHA-256, manifests, ZIP members, privacy,
  rights/caveats, scope/cursor, and supersession.
- Treat an explicit later hold/correction/supersession as controlling while
  preserving the earlier notice as adverse history.

### 7.2 Mutation

- Use one scoped branch, one coherent pull request, and the existing concept
  lineage unless a new concept is explicitly authorized.
- Keep GitHub source/custody and Zenodo publication receipts synchronized.
- Preserve unrelated current files in a Zenodo successor. Replace a same-name
  object only when the exact predecessor/successor relation is verified.
- Never create a second concept because the current record is inconvenient,
  large, imperfect, or temporarily missing a preview.
- Never stop at “staged” when publication is authorized and the coherent
  snapshot is ready. Push, merge, publish, and read back.

### 7.3 Required readback and reporting

For GitHub, capture separately:

- branch name;
- source commit and push/ref;
- pull-request number and URL;
- merge commit and URL;
- exact commit-pinned raw URLs; and
- downloaded bytes/hashes for every closeout/catalog/log surface.

For Zenodo, capture separately:

- concept DOI and URL;
- deposition/draft identity and state;
- record/version ID, DOI, and URL;
- predecessor and supersession relation;
- exact ordered file set, bytes, checksums, and default preview;
- ZIP/member replay where applicable;
- anonymous API/content readback for every changed public byte; and
- explicit confirmation of no duplicate concept and no active stray draft.

Report every branch, commit, push/ref, PR, merge, URL, concept, deposition,
draft, record, version, DOI, file set, and readback separately. Explicitly say
when GitHub, Zenodo, or producer payload state had no substantive change. Never
collapse the transaction into “archive updated.”

## 8. Crash-safe and resource-safe execution

This machine has repeatedly become unstable under unbounded disk searches,
parallel agents, and bulk high-resolution image loading. Resource safety is part
of archive correctness.

Standing execution constraints:

- Do not use subagents.
- Never recursively search all of `Documents`, the user profile, a drive root,
  or another multi-terabyte tree.
- Search only an exact known file, exact bounded producer root, exact worktree,
  or tracked Git path. Prefer manifests and `git ls-files`/`git grep` over disk
  discovery.
- Never reopen or page through the retired 7.8-GB rollout. Use this charter,
  durable files, the bounded private user-message extraction, current Git state,
  and exact producer handoffs.
- Do not bulk-render or bulk-load high-resolution page images. Reuse existing
  source-audit images. If new production QA is unavoidable, use one tightly
  targeted crop at a time at the resolution justified by the ambiguity.
- Run at most one heavy job at a time. Avoid parallel builds, recursive hashing
  of unrelated trees, and release-scale churn during live transcription.
- Do not create multiple local copies of large payloads when an exact immutable
  source plus one derived projection and one transport container suffice.
- Do not delete or move broad/computed paths. Resolve and verify exact targets
  first; preserve before any cleanup.
- Honor `stop` and explicit pauses immediately. A scheduled heartbeat does not
  override a user stop.
- During ongoing tool work, provide a concise progress update at least every
  sixty seconds.

Compute should be used generously for useful exact work, but never by repeating
an operation that is known to crash the PC or by generating evidence nobody
needs.

## 9. Current restart state after reconstruction

The active closeout worktree is on branch
`codex/sga-presentation-clean-complete-20260803` at
`6d7e992f5dbb05d27cb1cb69498e310d0ca68f93`, currently equal to
`origin/main` before the uncommitted closeout. Preserve all existing user and
task changes. Do not stage or delete `tmp/`.

Current uncommitted archive closeout includes:

- the SGA 1-7 II presentation-clean/privacy-remediated custody tree;
- `.gitattributes` support needed for scoped archive ZIP custody;
- exact SGA/methodology/replication public-readback receipts; and
- the scripts that produced the current same-concept Zenodo successors.

Current public SGA head:

- concept DOI `10.5281/zenodo.20410947`;
- record `21778810`, DOI `10.5281/zenodo.21778810`;
- 34 files / 182,736,901 bytes;
- default preview `00_SGA_1-7II_English_Global_Reader.pdf`;
- clean cumulative reader: 4,177 pages / 34,215,934 bytes / SHA-256
  `CCF136ADB5ADBEFC11231A3CDD11DF9EEDBE469FF87F1E739B312B6E1A2EF40B`;
- first complete ZIP: 99,144,470 bytes / SHA-256
  `1069944F415F7984D358C7F490D0BC699582FE1DD1F7C37085187517CE1A1715`;
- privacy remediation: 16 transformed files / 45 minimal replacement events;
- no active draft and no duplicate concept; and
- predecessor `21778605` retained as adverse history because its complete ZIP
  exposed absolute private build paths. Reader PDFs were not changed by the
  privacy remediation.

Current dual provenance heads after archive-log closure:

- methodology record `21778949`, DOI `10.5281/zenodo.21778949`, existing
  concept `10.5281/zenodo.21124403`;
- replication record `21778962`, DOI `10.5281/zenodo.21778962`, existing
  concept `10.5281/zenodo.20461174`;
- exact SGA provenance ZIP 700,154 bytes / SHA-256
  `799CCCE830A78D52D47DFFF0E473963D81BC2036E21C5CAADB3EEB0856CB2539`;
- exact English/Germanic decision log 3,191,133 bytes / SHA-256
  `067EA74FD007F45207E7E8504648FDC4683DB3CCA2ECD9A205299988B545974C`;
- no active draft and no duplicate concept on either receipt.

Immediate GitHub closeout after this charter is recorded:

1. update stale public catalogs/landing pages to the exact SGA and dual-DOI
   heads above;
2. validate the scoped uncommitted custody tree and receipts;
3. stage only the intended files, never `tmp/`;
4. commit, push one branch, open/validate/merge one pull request;
5. perform commit-pinned raw public readback of every changed closeout file;
6. append the final GitHub identities through the locked shared-log helper; and
7. leave Zenodo unchanged unless a genuinely new coherent producer successor
   arrives. Do not republish the already-closed SGA records.

FAC supersession state at reconstruction time:

- no new FAC draft, upload, record, or Zenodo mutation was performed in response
  to the now-superseded broad dual-DOI request;
- the broad methodology and replication heads already contain 16 of the 19
  frozen FAC comparator filenames byte-identically from earlier history;
- three same-name files differ there from frozen FAC R1: the self-correction
  ledger, project-logbook snapshot, and payload manifest;
- preserve/report this pre-existing state; make no correction on those broad
  records solely from the revoked request; and
- await the producer-owned dedicated FAC DOI and keep future GAGA publication
  separate.

## 10. Compaction and continuation protocol

Every substantial run must leave enough exact state that a successor can resume
without replaying a giant transcript. Before ending or crossing a compaction
boundary, record:

- active worktree and branch;
- local HEAD, upstream/main HEAD, dirty/untracked scope, and files explicitly
  excluded from staging;
- exact producer handoff ID, root, scope/cursor, file/member count, bytes,
  hashes, authority, caveats, privacy state, rights state, and supersession;
- current GitHub branch/commit/push/PR/merge/readback identities;
- current Zenodo concept/deposition/draft/record/version/DOI/file/preview/readback
  identities;
- open hold, revocation, correction, or no-duplicate state;
- current corpus and semantic-scaffold cursor;
- current logbook record IDs and hashes; and
- the single next safe action.

Use durable repo files and receipts as truth. Do not rely on memory, a chat title,
an in-progress terminal, or a staged Zenodo draft as the only state carrier.

## 11. Definition of done

This is an ongoing maintenance goal. It is not complete because one record was
published or one sweep found no payload. It can be marked complete only when all
currently authorized archive closeouts are published and read back, all tracked
corpus-completion obligations (including canonical French EGA and the semantic
scaffolds) are genuinely closed or explicitly transferred with exact durable
custody, no authorized producer successor is stranded locally, all public heads
and catalogs agree, and no required provenance/logbook surface remains only
local.

Near token, time, or context limits are never evidence of completion.
