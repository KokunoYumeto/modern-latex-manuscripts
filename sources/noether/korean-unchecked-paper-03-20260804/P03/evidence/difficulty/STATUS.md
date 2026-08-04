# Paper 3 Korean difficulty/failure ledger status

- Canonical JSONL: 14 append-only records.
- Latest record: `CJK-KO-P03-HARD-014`.
- Chain head: `3CDDEDED77A410B39E35FDC8A0B221A5546512ADCC6EDAF70F478200B8EFDCA8`.
- States: archive release hold active; Korean/ko-KP/Hanja and terminology decisions held; generator, dependency-discovery, structural-generator, and validation failures preserved even when resolved.
- No source, Korean, formula, compilation, rendering, archive, publication, or rights validation is claimed.

Frozen identities before this status file:

- `DIFFICULTY_LEDGER_SCHEMA.json`: 6,653 bytes; SHA-256 `DCF582F0C91DDA02FC89F0E1E2D27D2F5FB5AEB714E7755CA091DBDD3696410C`.
- `initialize_difficulty_ledger.ps1`: 22,632 bytes; SHA-256 `5D650B210E4647318148627151783E1F550B4BCD6C3D736157F0482FC79EE826`.
- `append_hard_012_dependency_loader_stall.ps1`: 5,191 bytes; SHA-256 `BE87B8D8B921C7276C39B071BEA485FA6882738D47ACF86D693B696CCE15B197`.
- `append_hard_013_014_metadata_correction_and_runtime_resolution.ps1`: 13,897 bytes; SHA-256 `813B9313B639B1A8C389518B770595311314354417CE00E07752061D50C69C09`.
- `validate_difficulty_ledger.ps1`: 7,640 bytes; SHA-256 `024275130948CC2FD6F4A13740DD66EE37849671A7D043718A01991912D47402`.
- `difficulty_ledger.jsonl`: 57,815 bytes; SHA-256 `861F7C2B62696214AABAE435FCD3A97B77E291495BAB549F98DFEBDAC2803DF9`.
- `difficulty_ledger.csv`: 8,826 bytes; SHA-256 `1E7F702258B39A7F258130319E5FB2E76C2CFF13DFE3B357D38FB3530749CAD3`.
- `DIFFICULTY_LEDGER_VALIDATION_REPORT.json`: 784 bytes; SHA-256 `489E8E4803CC3059D9A0DA3EE17C68BEE0A6C7A46E354D9C3F8FA4ADFDA8CC60`.
- Validator: PASS, 14 JSONL records/CSV rows, errors empty.

`CJK-KO-P03-HARD-011` is an immutable historical-malformation witness: a generator failure left several trailing semantic fields mangled while JSON and the hash chain remained valid. `CJK-KO-P03-HARD-013` supplies the complete correction by append, and the schema/validator now require that exact exception and correction. The predecessor was not rewritten.

`CJK-KO-P03-HARD-012` preserves two stalled dependency-locator calls. `CJK-KO-P03-HARD-014` resolves that hold with the exact supplied bundled Node/dependency paths and the frozen no-render artifact-tool PASS report; the canonical report is rerun after final CSV mutation.

Archive policy `CJK-KO-ARCH-001` controls: these metadata and status labels do not make Paper 3 immediately archive-eligible. Archive maintenance alone owns release disposition.
