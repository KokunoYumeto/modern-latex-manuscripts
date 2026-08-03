# SGA provisional global-reader publication error and recovery history

## Final state

- Record: <https://zenodo.org/records/21775746>
- DOI: `10.5281/zenodo.21775746`
- Existing concept DOI: `10.5281/zenodo.20410947`
- Predecessor: `10.5281/zenodo.21762813`
- Final boundary: 100 files / 851,729,584 bytes
- New payload: 8 files / 68,311,787 bytes, 8/8 exact anonymous SHA-256 readback
- Transport ZIP: 7/7 members exact, inventory SHA-256 `64BC7F089E1A6FD09AC63E9AA87B01FA414E85593405C7EE4B9DAF230B6D276F`
- Duplicate concept created: no
- Active target draft remaining: no
- Public readback closed: `2026-08-03T14:26:17Z`

## Append-only operational history

1. Read-only preflight at `2026-08-03T14:21:58Z` resolved published predecessor `21762813`, verified 92 inherited files / 783,417,797 bytes, found no target draft, found no upload-name collision, and fixed the add-only final boundary at 100 files / 851,729,584 bytes.
2. The publisher created same-concept tracked draft `21775746` only through predecessor `21762813`'s `newversion` link. The state was recorded at `2026-08-03T14:22:12Z` before upload continuation.
3. All eight new objects were uploaded. The draft then passed the exact 100-file staging guard: all 92 predecessor object UUID/size/MD5 identities were retained, all eight new size/MD5 identities matched, the default preview remained `00a_SGA1_English_Reader.pdf`, and the concept DOI remained `10.5281/zenodo.20410947`.
4. The first `POST` to `https://zenodo.org/api/records/21775746/draft/actions/publish` returned HTTP `504 Gateway Time-out`; no successful response body was captured. The publisher therefore did not claim publication.
5. Immediate read-only recovery probes found: public record `21775746` HTTP 404; authenticated draft HTTP 200, unpublished, 100 files; legacy deposition state `unsubmitted`, `submitted=false`, 100 files; latest published head still `21762813`. No blind publish retry was issued at that point.
6. A controlled retry invocation stopped before reaching any publish request because Zenodo's `versions/latest` endpoint had begun transiently reporting tracked draft `21775746`. This exposed an overly strict local guard assumption; it did not create, upload, delete, patch, or publish anything.
7. The guard was corrected to allow only the exact locally tracked draft/record IDs during recovery. The next preflight stopped again when the tracked-draft endpoint returned 404. This second stop also occurred before any publish request.
8. Exact probes then established delayed server-side success from the original publish call: public record `21775746` HTTP 200 and `is_published=true`; both successor and predecessor draft probes HTTP 404; deposition state `done`, `submitted=true`; concept latest head `21775746`; DOI `10.5281/zenodo.21775746`; 100 files. No second publish call was sent.
9. The first anonymous file-readback attempt stopped on file 1 with HTTP 406 because the local verifier incorrectly sent the InvenioRDM metadata `Accept` header to a file-content endpoint. No remote state changed and no file identity was accepted from that failed request.
10. The verifier was corrected to omit that metadata header on anonymous content downloads. The replay then downloaded all eight new files, matched all eight exact byte counts and SHA-256 values, opened the public ZIP, and matched all seven members to the direct public files. The closed state records latest head `21775746` and no active target draft.

## Corrections retained

- Publisher guard correction: a tracked same-concept draft may temporarily appear as `versions/latest`; only the exact state-bound draft/record IDs are allowed.
- Readback correction: anonymous file-content requests use the file URL without the metadata API `Accept` header.
- The HTTP 504 is retained as an adverse publication event even though the original request later completed server-side.
- The HTTP 406 is retained as a verifier error even though it did not affect any archived bytes.

No source package was mutated, no predecessor object was removed or replaced, and no completion/certification claim was introduced during recovery.

## Reader-presentation regression and hold — 2026-08-03

11. Post-publication reader inspection established that the provisional cumulative PDF `00z_SGA_1-7II_English_Global_Reader_navigation_r3_PROVISIONAL_20260803.pdf` (33,402,752 bytes; SHA-256 `8686621D6324B0F5D7EECCE4EE7B90EDF310AF253731FCEB5569587F3E762357`) inherited a generated `Source and status note` as cumulative page 2 from its admitted SGA1 input. The same prose is present in the then-default direct SGA1 preview `00a_SGA1_English_Reader.pdf` (2,763,471 bytes; SHA-256 `46406925C8EBBF4309A67CF4D84B493952EF99C067E1971F885F0F3AF326BA1E`).
12. This was an archive presentation error. Workflow narration, source-status prose, model commentary, project dates, correction rationale, and similar archive/production matter belong in external logbooks and provenance files, not in reader PDFs or reader footnotes. Genuine source-era editorial matter remains part of the mathematical edition and is not removed merely because it is editorial.
13. Earlier work had already published a reader-pure SGA1 presentation successor, 259 pages / 2,508,801 bytes / SHA-256 `6D490A8CC73FDEDC312AE0C0F7293794CBC4996A36CF5FE5DF98C571FC5F38CE`, with zero blocked reader-project-matter phrases. Later reference-v2 and cumulative publication regressed to the 262-page status-bearing surface. The clean 259-page object cannot be substituted blindly because its recorded navigation graph is smaller than the later reference-v2 surface; presentation cleanup must not silently discard reference navigation.
14. The production lane issued an urgent hold on the exact provisional cumulative PDF and is preparing a no-overwrite clean successor that preserves the substantive mathematical text while moving rationale into external logbooks. Until that successor is accepted, the provisional cumulative PDF is retained only as explicitly provisional/superseded history and is not the browser preview.
15. Anonymous whole-byte replay verified `00b_SGA2_English_Reader.pdf` as the existing clean interim preview candidate: 178 pages / 1,996,972 bytes / SHA-256 `C2E1C33CAEDF2866DA6FFC2D3E87DB243EF7CF098D8A1F25E2589245B1B7094D`; the defined reader-project-matter phrase scan returned zero hits.
16. The first in-place hold revision correctly changed `files.default_preview` to SGA2 and prefixed the public hold notice, but independent anonymous readback found an inherited lower description paragraph still claiming that SGA1 remained the browser preview. That contradictory statement was not accepted as harmless history because it described current UI state. A second in-place metadata-only revision replaced the exact stale paragraph with the truthful hold layout. This correction changed no file, file order, version, concept, DOI, or scholarly claim.

### Standing reader-surface rule

- Permanent public order for a clean cumulative successor: complete reader/source ZIP first; clean cumulative reader PDF second and selected as `default_preview`; individual reader PDFs next; cumulative and individual TeX/source surfaces after all reader PDFs; archive manifests, validation, logbooks, and history afterward.
- Do not promote a provisional reader merely because it compiles, validates structurally, or is the newest byte snapshot. Reader-facing prose must be checked separately.
- Do not delete adverse or superseded bytes from custody. Preserve them through Zenodo version history and explicit supersession records, while keeping them out of the current reader-facing preview.
