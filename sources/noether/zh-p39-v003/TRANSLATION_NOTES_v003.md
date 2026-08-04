# Paper 39 Chinese producer notes — v003 checker-return integration

Status: **bounded producer integration complete; independent recheck pending**.

## Controlling return

- Return ID: `ZHCHK-NOETHER-P39-V002-RETURN-001`.
- Receipt: 7,402 bytes / `B4E07772158637DE71A83E7F3A7AAF461840ACB89A19E0DE355EA5DC2390F046`.
- Return manifest: 89 entries, 11,584 bytes / `7FF46673A3DE1EDB3C3D7711C55CD5495313C1B8E501D5438C7D84BE32090F77`.
- Return verifier: 14,000 bytes / `2770800FDC9C92C64EFC61FB322728D3D9F32DF69CBBA11358F66982835F0E1B`; sealed verification reports 42/42 pass.

The exact controls, finding snapshot, candidate-generation record, candidate Hant TeX/PDF, and four evidence candidates are imported under `checker_return_v002/`. Checker-owned source files remain untouched.

## Split disposition and exact integration

The accepted v002 Hans TeX and PDF are copied to v003 names without any byte change. They retain hashes `101836C4…FE6` and `36706132…BA1` respectively and were not rebuilt.

The v003 Hant generator applies the exact F001 controlled normalizations after OpenCC `s2t`: four `超復→超複`, two `一箇→一個`, and one `着手→著手`. Fresh regeneration produces 16,322 bytes / `F0E9425763D5E075A5ED1810FE2B1DC2BDAAF6FD48691BE8C3D64F4B158AF1C8`, byte-identical to the sealed checker candidate. To preserve that hash-pinned identity, the TeX's internal provenance comments retain the candidate's v002 wording; the enclosing package, filenames, status, and integration records establish v003 lineage.

F002 is integrated by exact byte-copy of all four sealed candidates:

- terminology ledger: `4772D0E74F590A5AF576900CC944259C95314C0F0A5D9A935D4259B4B4F4B591`;
- adverse-sense ledger: `66D5441C0D1543BE28136EF679D887C54B74369F858F79CDC4C6C2A000E2F0CB`;
- CJKV crosswalk: `FBE968E86983F2435EEA335973254F8413C2E43B59544A797F0EC354DE260402`;
- concept graph: `348C0CD592F89E88E759AB6B3CEA79CC9DC2F5951764E8CDD1F3087FAB1BD83F`.

These candidates reconcile T002, T012, T013, T016, and T018 exactly as frozen. Their independent-check language describes the v002 comparison; v003 package acceptance remains pending.

## Producer boundary

The producer verified custody, exact byte equality, deterministic regeneration, evidence-candidate identity, compiler exits, log diagnostics, and the compiler page count. It did not source-check, translate-check, formula-check, terminology-quality-check, render or open PDFs, visually inspect pages, perform native/regional review, approve, publish, archive, or certify. No German defect packet was created. SGA was not touched.
