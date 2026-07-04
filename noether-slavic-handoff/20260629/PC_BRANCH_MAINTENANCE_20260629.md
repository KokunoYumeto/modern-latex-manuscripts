# PC branch maintenance note - 2026-06-29

Repository: KokunoYumeto/modern-latex-manuscripts

PC-local branch: codex/noether-pc-20260629

Base branch: codex/noether-slavic-handoff-20260628

Base commit: c044884759ef269661da2f13321c6b2f39479652

Orientation session: 019ead97-38c8-7112-9b9c-e8c176d526a1

This branch is the handoff/coordination branch for Noether work continued on this PC. It should carry, or point to, anything produced by this local Codex instance for the broader Noether multilingual canonical-edition workflow.

## Scope accepted on this PC

- Maintain the completed/review-ready Slavic lane for Ukrainian, Russian, and Interslavic/Panslavic Latin+Cyrillic.
- Continue source correction intake, render fixes, terminology improvements, accepted-review ledgers, manifests, sidecar validation, cumulative TeX/PDF rebuilds, and GitHub/Drive/Zenodo handoff pointers.
- Extend the same evidence-first discipline to French, Spanish, Chinese, Japanese, Persian/Farsi/Dari/Tajik-related registers, Arabic, and other useful target lanes.
- Treat semi-constructed, constructed, and interlanguage methodology as a first-class research lane under the same translation project header.
- Maintain machine-readable status where possible so later Codex sessions do not need to reconstruct state from chat.

## Local artifact workspace

The active assembled artifact workspace on this PC is:

`C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical`

That workspace is an assembled artifact tree rather than a Git checkout. This branch therefore begins with handoff notes and exact artifact hashes, not a full generated-artifact import. A later import can use a sparse checkout or release-asset strategy if the repository is meant to hold the full PDFs/zips directly.

## Prior checkpoint context

The pasted prior-session checkpoint referenced:

- Noether Slavic cumulative zip T194100, SHA-256 `71F4710EE050142B199BE73A897FADD204551AA7737482B6637A295E56C9936D`.
- Later Noether Slavic cumulative T203324 package, SHA-256 `4F9A629F42C8292BF4CC5FB43E58EBB951EC2A383E01D0812A20E6644E0999C9`.
- Review bundle SHA-256 `A2985DA390620A8982A8BFA526CC9C5CD2EF3FEB63AF9E8E369BFC2F58550799`.

Those checkpoints established that the Slavic lane was review-ready/polish territory and that the next responsibility is broader language-lane maintenance plus the interlanguage/research-method lane.

## Current PC checkpoint

Current verified work in the assembled artifact tree includes the Simplified Chinese Paper 34 through Section 18 working checkpoint. The TeX, manifest, render ledger, and PDF hashes are recorded in:

`noether-slavic-handoff/20260629/SIMPLIFIED_CHINESE_PAPER34_SECTION18_PC_CHECKPOINT_20260629.md`

## Security note

Two GitHub tokens were pasted into chat during this handoff. They are treated as exposed secrets and should be revoked/rotated. This branch update used the existing GitHub CLI keychain authentication on the PC; the pasted token values are not stored here.

## Next maintenance steps

- Continue Simplified Chinese Paper 34 from Section 19 only after preserving the current Section 18 state.
- Build source-level evidence shelves before translation/revision for French, Spanish, Chinese, Japanese, Persian/Farsi/Dari/Tajik-related registers, Arabic, and any additional target lanes.
- Keep the constructed/interlanguage research lane publishable as methodology, not merely as project chatter.
- Decide whether full generated artifacts belong in Git, GitHub Releases, Zenodo, Drive, or a split pointer/manifest strategy.
