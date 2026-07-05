# Archive Maintenance Review: R9 Africa/Horn/West Payload

Date: 2026-07-05

Reviewed commit:

`7b3ed05b8 Add R9 Hausa Tigrinya source-body payload`

## Verdict

Accepted as a real useful side-branch payload.

This was not acknowledgement-only output. It contained actual source bodies/source archives, including Hausa and Tigrinya source material, manifests, hashes, and coordination notes.

Archive maintenance imported this payload into `main` in commit:

`ccaca5ac7 Import other-PC R9 source-body payload`

## Packaging Defects Found

1. `main.bbl` was listed in the package manifest but was missing from the side-branch commit because `.bbl` files are ignored.
2. `icml2025.bst` showed hash drift until archive maintenance restored it directly from the arXiv source archive.

Archive maintenance recovered `main.bbl` from:

`language-source-bodies/r9-africa-horn-west-20260705/source_archives/tig/arxiv_2601_03403_tigrinya_number_verbalization_eprint.tar`

Recovered `main.bbl` SHA256:

`0E879B6180F2C6A06BC42A879721208E00ABF55815B7FB69C42C3C5C23DBD22E`

Restored `icml2025.bst` SHA256:

`0EC3D5EB9B02EFB7E0B44A32F3775882F42A743D0BDC618F34E6936309B98764`

## Required Fix For Future Payloads

Before pushing, force-add ignored body/provenance files when they are required:

- `.zip`
- `.tar`
- `.tar.gz`
- `.bbl`
- `.pdf`
- image witnesses
- source archives
- any other ignored file that the manifest lists as a body

Then verify the manifest against the committed tree, not merely against local pre-Git files.

## Goal-Verbatim Requirement

The dispatcher must tell every sibling/idle session to set the complete assigned task block as that session's pursued goal exactly and verbatim.

Not a summary.

Not a shortened version.

Not one sentence.

The complete block.

See:

`00_SET_EVERY_ASSIGNED_GOAL_VERBATIM_NOW_20260705.md`

and:

`00_DISPATCH_ALL_IDLE_SESSIONS_NOW_20260705.md`

## Next Expected Work

Continue producing body-containing packages on `codex/noether-pc-20260629`.

Stay off `main`.

Keep dispatching idle sessions.

Do not push acknowledgement-only or governance-only output.
