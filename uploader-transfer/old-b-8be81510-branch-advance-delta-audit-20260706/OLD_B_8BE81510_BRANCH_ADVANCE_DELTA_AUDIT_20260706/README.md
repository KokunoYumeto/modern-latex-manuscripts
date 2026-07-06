# OLD_B_8BE81510_BRANCH_ADVANCE_DELTA_AUDIT_20260706

Generated UTC: 
2026-07-06T09:16:29.7798265Z

Purpose: read-only old-B comparison note for branch advances from AC6F to A2C52A42, 1A1110EB, and requested current head 8BE81510. This does not stage, commit, push, edit PR metadata, use GitHub Issues, or duplicate B3 packaging.

Requested heads:
- AC6F baseline: `ac6f4eb7490b1bba788444ddb2361fc65c3d9f6e`
- A2C branch advance: `a2c52a42f5484c3889473135fd85f2fea9491aaf`
- 1A prior frontier only: `1a1110ebfcbe729d3c0db2a3fe98148e070a5389`
- 8BE requested current head: `8be81510d284b9804706e426a312f1649f39d080`

Local inspectability: all four commit objects are present in the B3 object store. The B3 worktree itself is detached at a different commit, and local `origin/codex/noether-pc-20260629` was observed at `9d7db086f00e8cce0aceeefa9d80acba9fd1af50`, which is beyond/different from the user-stated 8BE frontier. This audit records that mismatch as a B3 reconciliation item, not as old-B authority to package or push.

Primary outputs:
- BRANCH_HEAD_TREE_COUNTS.csv: committed-tree counts and tree hashes for the four heads.
- BRANCH_HEAD_DELTA_COUNTS.csv: path-change counts for AC6F->A2C, A2C->1A, 1A->8BE, and AC6F->8BE.
- BRANCH_HEAD_DELTA_PATHS.csv: full changed-path list for the same comparisons.
- DELTA_PATH_CLASS_COUNTS.csv: changed-path classes for package/manifests/source-body/logbook signals.
- LOCAL_REF_OBSERVATIONS.csv: local ref mismatch and dirty-checkout caution context.
- MANIFEST.csv and SHA256SUMS.txt: hashes for this audit packet.

Boundary: preserve source-use/provenance/gap/draft/non-canonical labels and make no native-review/accepted-terminology/approval/license-clearance/gate-promotion/source-certification/final-status/bridge-pilot/translation-completion claims.
