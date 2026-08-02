# Active FAC/EGA provenance v4 — archive errors and recovery

Release: `all-session-mathematical-provenance-20260803-v4`

This append-only record preserves archive-side errors and recoveries. It does
not change producer mathematics, translation, transcription, source, or visual
claims.

## ZIP omission caught before Zenodo staging

- Commit `f4c636298afbd519b8c919a8475c53169673a7bb` added the v4 public
  projection, manifests, loose logbooks, and guarded scripts.
- The repository-wide `*.zip` ignore rule omitted the four complete
  provenance ZIPs from that first commit even though they remained present and
  validated locally.
- The omission was detected before release-spec construction or Zenodo draft
  creation. Commit `18d8806cc4ccd4c450b640dd30a97317f8be0656` added the
  exact four ZIP bytes explicitly.
- Anonymous commit-pinned readback subsequently passed 35/35 files from the
  first commit and 4/4 ZIPs from the correction commit. The omission was not
  hidden by rewriting the first commit.

## Local-path validation receipt corrected before commit

- The first generated local `BUILD_VALIDATION.json` for the four-concept
  release specification serialized an absolute local path to the release
  specification.
- The generated six-file directory had not been committed or uploaded. It was
  removed under an exact guarded path, the builder was corrected to emit
  `release_spec.json`, and the complete directory was regenerated.
- The regenerated controls passed a privacy scan. Their exact release-spec
  identity is 61,721 bytes / SHA-256
  `5E8502FB69C381937A746EBC60ACA686FE3B595358C648FDBE9519D31648FDC4`.

## Public Zenodo UUID false positive

- An independent broad UUID scan initially classified public Zenodo file UUIDs
  in the predecessor guard as possible private task IDs.
- The scan was corrected to distinguish public Zenodo object identities from
  producer-text task/thread identifiers. Context-specific path, credential,
  Codex-state, and workflow-marker checks then passed.
- No release byte was changed to conceal a public Zenodo identity.

## Recently published FAC record briefly reported as a draft

- One guarded publisher invocation staged all four exact same-concept drafts,
  then published methodology record `21764482`, replication record
  `21764484`, and FAC/GAGA record `21764488`.
- EGA draft `21764491` remained staged. Before its publish call, the
  authenticated account-wide deposition listing briefly still reported newly
  published FAC record `21764488` as an active FAC draft.
- The publisher state already marked FAC
  `PUBLISHED_PENDING_READBACK`; therefore the account guard expected no FAC
  draft and stopped with:
  `Untracked or parallel active draft for fac_gaga: observed=[21764488], tracked=[]`.
- The process exited. No overlapping or second publisher process was launched.
- A read-only recovery preflight then found no methodology, replication, or FAC
  draft and found only exact tracked EGA draft `21764491`. The same persisted
  transaction was resumed; no new draft was created.
- EGA record `21764491` was published and all four records passed anonymous
  outer-file and ZIP-member SHA-256 readback. Terminal target draft lists were
  empty; no duplicate concept or parallel draft was created.

## Terminal publisher-state identity

The closed publisher state is preserved in private archive custody because it
contains local absolute paths:

- bytes: 8,884
- SHA-256:
  `F24DC3567803331D6288E675FE33B51307396912194883996DC2F728C4B18043`
- status: methodology, replication, FAC/GAGA, and EGA all `CLOSED`

The public records and receipts, not this private state file, are the public
readback authority.
