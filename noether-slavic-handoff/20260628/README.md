# Noether Slavic Handoff Metadata, 2026-06-28

This folder was salvaged from the separate branch `origin/codex/noether-slavic-handoff-20260628` without merging that branch. The branch itself had a destructive diff against the main archive branch, so only this handoff/audit folder was imported.

The files here describe a Ukrainian, Russian, Interslavic Latin, and Interslavic Cyrillic Noether handoff package. They are useful as coordination, validation, terminology, render-integrity, and source-review metadata.

Important limits:

- The actual ZIP package named in the validation files is not present in this repository.
- A local sweep on 2026-06-28 did not find `Noether_Slavic_Post44_Papers01_45PlusBibliography_Update_20260628T070354Z.zip`.
- The package validation JSONs have been sanitized to remove producer-local absolute paths while preserving package names, hashes, byte counts, file counts, and scope text.
- The audits report strong artifact/render/glossary evidence, but only Paper 01 has first-pass Codex source review; Papers 02-43 and endmatter still need Codex source review and external/native-language authority review before any final canonical claim.

Use this folder as a Slavic translation lane control/handoff record, not as proof that the public Noether Zenodo record already contains the package.

Follow-up note: the same remote branch later added
`noether-slavic-handoff/20260629/CODEX_LAPTOP_LANGUAGE_PLANNING_CHECKPOINT_20260629T022535Z.md`.
That 2026-06-29 file is also metadata only. It points to a laptop-local
`Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260629T022535Z.zip`
that was not uploaded to GitHub and has not yet been verified on this PC.

The 2026-06-28 `latest/` pointer directory was imported on 2026-06-29 after
re-reading the remote branch. It points to a newer locally validated package:

- `Noether_Slavic_Post44_Papers01_45PlusBibliography_Update_20260628T203324Z.zip`
- SHA256 `4F9A629F42C8292BF4CC5FB43E58EBB951EC2A383E01D0812A20E6644E0999C9`
- 771,690,649 bytes; 5382 ZIP entries; independent validation overall pass
  reported as true.

It also points to an external-review role-packet bundle:

- `Noether_Slavic_ExternalReview_RolePackets_SelfContained_20260628T200514Z.zip`
- SHA256 `A2985DA390620A8982A8BFA526CC9C5CD2EF3FEB63AF9E8E369BFC2F58550799`
- 221,484,776 bytes; 2739 ZIP entries; independent validation overall pass
  reported as true.

Neither binary package was found on this PC by exact-name sweep on
2026-06-29, so the imported `latest/` directory remains pointer/control
metadata, not a Zenodo-ready binary upload.
