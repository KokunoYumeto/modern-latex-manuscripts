# Rejected public r2 attempt1 - pre-freeze verifier phrase-wrap failure

Attempt1 stopped before rename and before any custody handoff. The exact runtime
failure was:

Publication-readiness DOI/recheck text missing: never mint a duplicate record.

The required warning existed in PUBLICATION_READINESS.md as "Never" at the end
of one line and "mint a duplicate record" on the next. The case-sensitive,
contiguous assertion was defective. Attempt2 uses a contiguous lowercase policy
sentence plus a case-insensitive whitespace-tolerant verifier regex.

Preserved attempt1 surfaces:

- publication sibling
  SGA1_English_Expose_I_opening_through_I_9_2_source_audited_checkpoint_20260719_r2.__rejected_attempt1_prefreeze_verifier_phrase_wrap__:
  138 files / 8,104,240 bytes; ordered inventory digest
  3F1484AB7FFFE303619EFDAB5841F43BA368AB1B209796504E7AFA231686FCA6.
- build/I9_2_PUBLIC_R2_REJECTED_ATTEMPT1_PREFREEZE_VERIFIER_PHRASE_WRAP_BUILD_20260719:
  17 files / 763,460 bytes;
  ordered inventory digest
  7BCDB1CCCC393374C576E38C4F4786402479328A72A86C4CB954E3FA671ED80B.
- build/I9_2_PUBLIC_R2_REJECTED_ATTEMPT1_PREFREEZE_VERIFIER_PHRASE_WRAP_RENDER_A_20260719
  and
  build/I9_2_PUBLIC_R2_REJECTED_ATTEMPT1_PREFREEZE_VERIFIER_PHRASE_WRAP_RENDER_B_20260719:
  each 16 files / 6,346,588 bytes;
  ordered inventory digest
  1B65B5CE7DC5F3A4B40FF9DB5694824F5D0BFF1F1183E3D5D864C2A834185793.
- staged verifier: 23,047 bytes; SHA-256
  0C7AB407B826EE6DD2FF22348F9B5C25505FFFB7C274EB3BA02171830231B8D0.
- staged readiness: 2,423 bytes; SHA-256
  85A7EFA1C313B59FBACC0A79DB37C6A2F88FABCA94B48B86172ED014955C2E93.
- staged manifest: 174,989 bytes; SHA-256
  21C796E600438EF88CFA1936C21BB91594DD4615A85870DC26A236A948653E13.
- staged SHA256SUMS.txt: 19,002 bytes; SHA-256
  4CF57F2067C7C5D8BB099D53521A456B8B7D481EED1D05BE251849CB5E1FC17C.
- staged reader: 545,957 bytes; SHA-256
  BC97394DFABCE16F914A916F7D19D84BB5EE103C1A7BE7CFF6AFEA0E4E904A57.

Status: REJECTED and deliberately unclosed. No attempt1 file is reused,
refilled, deleted, promoted, or represented as a successful checkpoint. No
upload, archive mutation, DOI update, publication, or remote readback occurred.