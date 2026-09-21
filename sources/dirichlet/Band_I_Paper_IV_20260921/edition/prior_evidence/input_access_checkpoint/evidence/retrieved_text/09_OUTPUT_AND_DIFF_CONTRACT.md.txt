# Required return after every prompt

Return these four sibling files, with the session number substituted for `NN`:

- `DIRICHLET_P04_SNN_CUMULATIVE_FULL_STATE.zip` - all current editable French/English sources, built readers, apparatus, page records, ledgers, logs, QA evidence, cursor, and inherited evidence required to resume. Do not nest older cumulative ZIPs.
- `CHECKPOINT.json` - schema/version, prompt completed, next cursor, exact accepted pages by layer, first untouched page, unresolved source ambiguities, build/visual state, and hashes of every cumulative artifact.
- `MANIFEST.tsv` - normalized relative path, byte length, uppercase SHA-256, role, acceptance, printed-page range, and provenance for every ZIP member.
- `SOURCE_BACKED_DIFF.tsv` - only concrete corrections, columns: printed_page, authority_pdf_page, layer, before, after, evidence, disposition. Use `NONE` only after a real comparison finds no correction.

Reopen the ZIP and verify CRC, path safety, unique normalized names, manifest exactness, and checkpoint bindings before returning it. Show the diff rows compactly in-session; do not substitute an exposition. A correction may not be accepted without the attached authority page. `UNRESOLVED_SOURCE_AMBIGUITY` is allowed only for genuinely illegible print and must never invent text or stop unrelated work. Generic terminal HOLD/FAIL and time-limit exits are forbidden for repairable issues.
