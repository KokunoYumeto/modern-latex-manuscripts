# Artifact Tool and manifest QA

The exact manifest is deliberately self-excluding. It covers substantive
editable, built, source-render, target-render, ledger, and human-review files.
It excludes its own bytes; the generated machine-validation report; local-only
build logs and extracted text; TeX auxiliary files; and the Artifact Tool
preview subtree. Those validation-layer exclusions prevent cyclic hashes.

The preview subtree remains part of this working checkpoint. Its five full
CSV previews, five stable-ID previews, and NDJSON execution receipt are
enumerated and hashed in `MACHINE_READABLE_VALIDATION.json`. The final
`UNIT_HASHES.csv` itself is imported and rendered only after the manifest has
been refreshed, so its preview corresponds to the exact final 31-row table.

Status: exact-manifest scope documented and independently checked for this
sealed bounded unit. This is not a cumulative or full-volume claim.
