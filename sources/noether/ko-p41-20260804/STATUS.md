# Noether Paper 41 — Korean translation-producer status

Date: 2026-08-04  
State: **complete substantive draft-text coverage in U01–U12; every unit independently UNCHECKED**

## Coverage

- U01: source-snapshot lines 1–11 — title, publication line, programmatic introduction and bibliography notes.
- U02: lines 13–20 — § 1 heading, field/Galois setup, crossed-product introduction.
- U03: lines 22–46 — relations (1)–(5), crossed product, algebra/factor-system classes, Brauer group.
- U04: lines 48–56 — cyclic-algebra specialization (1′)–(5′).
- U05: lines 58–66 — extension group and three formulations of the minimal principal-genus theorem.
- U06: lines 68–78 — proof/equivalence of the three formulations and Schur-index extension.
- U07: lines 80–95 — § 2 and induced ideal-class partition, definition, principal-class condition.
- U08: lines 97–105 — three formulations of the principal-genus theorem.
- U09: lines 107–120 — proof setup, ideal-level Lemma 1 and split-algebra Lemma 2.
- U10: lines 122–129 — local decomposition algebra and unramified-place setup.
- U11: lines 131–143 — normalized cyclic presentation, unit/norm argument, Lemma 2 conclusion.
- U12: lines 145–151 — final proof, cyclic specialization, receipt.

Stored-source lines 153–154 are `\clearpage` and `\setcounter{footnote}{0}` control matter and are not Korean prose units. Blank separators are outside the closed slices. The twelve units therefore cover all substantive Paper 41 text present in the bound snapshot, but this is draft-text coverage only—not checked, assembled, compiled, rendered, final, approved, certified, or published Paper 41.

## Authority state

- Preserved German snapshot: 27,110 bytes; SHA-256 `C265058425E5E2D1A2289CC03A9DDEDDDF4803A3215DC3F173B93E7AB69D60ED`.
- Historical whole-source coordinates: lines 19709–19862 / bytes `[1787529,1814639)` / historical whole SHA-256 `443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27`.
- Current live pointer: `NOETH-DE-AUTH-v003-20260804`, 15,345 bytes, SHA-256 `932FEDC1735A41A9CF71D15A6C662A468A4CAD016AE8B3DECDF9A71E8BA7F197`; it supersedes v002 only to register the verified P41 binder.
- Default exact whole German translation authority: `NOETH-DE-ED-0001`, 2,153,565 bytes, SHA-256 `D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB`.
- Canon receipt `NOETH-DE-BINDER-P41-KO-U01-U12-20260804-001` classifies the complete snapshot as `safe_normalized_identical_current_authority_span`; exact receipt: 9,522 bytes, SHA-256 `95D0E69B6D32FD93801C3FDC4C519FAA9AB7CA867538E1CD9E2096EFAB253A91`. This closes coordinate debt only; no defect claim or target review occurred.

## Target standard and open choices

- Producer target: Hangul-first `ko-KR`.
- No unverified Hanja expansion was inserted as authority evidence.
- No Korean-native `ko-KP` evidence or localization was available; no North-Korean or pan-Korean claim is made.
- Mandarin-Simplified dominance in the surviving custody shelf is qualitative evidence debt only, never a readiness scalar. Chinese/Japanese targets do not authorize Korean.
- Provisional terms and sense windows are exposed in `TRANSLATION_CHOICES_U01_U12.md`, including the unresolved P41 `극대차수` versus P42 `극대 오더` conflict.

## Preserved producer-write failures

- U01–U04 initially lost inline TeX math delimiters through JavaScript string escaping; repaired before frozen hashes, so failed prehash identities are unavailable.
- First-return U05–U08 files had the same delimiter-loss class. Their damaged bytes/hashes are retained in `CJK-KO-P41-002` and the difficulty ledger; only the missing delimiters were restored, with Korean wording unchanged.
- U09–U12 were written with doubled escape characters and needed no repair.
- `TRANSLATION_CHOICES_U01_U12.md` had a separate metadata-only delimiter-loss incident, repaired before its frozen hash.
- The first difficulty-ledger build produced valid record self-hashes but an invalid predecessor chain because PowerShell function scope left every later predecessor null. The failed JSONL/CSV and machine FAIL report remain preserved. An attempted in-place regeneration was then correctly blocked by the append-only guard; the invalid active files were moved, not deleted. `CJK-KO-P41-HARD-013` and `HARD-014` retain both events.
- Two compact PowerShell inventory shapes also failed before writing: a comma-separated `Join-Path` array bound later entries as `AdditionalChildPath`, and the already-known direct `foreach`-to-pipeline parser failure recurred in the handoff sweep. `HARD-015` and `HARD-016` preserve them.

These are producer write-integrity repairs, not source, formula, completeness, or Korean review.

## Producer reproducibility evidence

- Structural hierarchy authority: `evidence\structural_index\PRODUCER_STRUCTURAL_INDEX.jsonl`, 129 records / 213,997 bytes / SHA-256 `D825FC810574A54CDD3B7C97370EC5FFCA8F21A567664D721C2C6FA8EFF021F7`; latest `NOE-P41-KO-U12-RECEIPT-001`. Schema SHA-256 `14800B151BC67B7E5E2CF6DD7DD3B5CE4C44DBFE860B4934473F02FD07575FDD`; builder/validator `26F7DCBFE1F9D407A9845BD331F02B60D4D7026F5B389C130B4CC50F5852FC85`; PASS report `38E0F3E3B5CC2552863F9A2970F5424F4E03D0059156F5DF4759242F5A06E751`. The frozen records predate the delivered binder and retain historical-pointer debt in their authority-state field; the exact canon binder and this status supersede that metadata field without rewriting the index.
- Append-only difficulty authority: `evidence\difficulty\difficulty_ledger.jsonl`, 16 records / 72,530 bytes / SHA-256 `4C5195896923C6816D695A0AA21107F9FD27B19EBAAC9DD61EDECDCDFADB8488`; latest `CJK-KO-P41-HARD-016`, chain head `DC6FA2D8B46A1C229AE42313D0198FBC8D4650D83ABA973EAC60167C888810B3`. CSV projection 10,396 bytes / `EE4E61F0DE8DE3CD41287668E3B2BE03FE5192A8A3F553A434B86DD53935F7A3`; schema `9E658939B2CE4317146B0381637934C870CFB8ED3AD5C217485687A9D4568312`; validator `4E1FC01DE3C0867FBF21AE30EF1CE3DC69BE7B2F216548A1E3D6111A88AEAEA8`; 16-record PASS report `D02B4D228B5588C3E8BEFE17945D81391510470B72A744043DA06641266CD3EE`. The initial invalid chain and its FAIL report remain separate immutable evidence.
- Visual-evidence authority: `evidence\visual\visual_evidence_index.jsonl`, zero bytes / zero records / SHA-256 `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855`; CSV `BC0415A85D1DB95A4F129CDFFC8D43FE5B44BF7B959592653B5309B363AE6F2A`; schema `C1F066E21053961F3119A29FCDCA5F6A88808B1E168A2C57BA03EC134F0E5F60`; validator `D17340DC5A05FC04C3D3908D92EB49325C84C11B1E4BB4A211D735AE29CA47CB`; PASS report `FEC4FB4D994532487290AF34E90AAC2F8B97E93C498EA4C2FFC1C55342599349`. No source image, crop, equation image, render, contact sheet, before/after image, segmentation raster, or overlay was used or created.
- The three current CSV projections imported through `@oai/artifact-tool` as rectangular tables with nonblank unique headers and no spreadsheet formula-error strings. Report: `evidence\csv_artifact_validation\CSV_PROJECTIONS_ARTIFACT_TOOL_VALIDATION_REPORT.json`, 2,731 bytes / SHA-256 `91C2B03308ACD722223B3CE2A909F62BA17C7DE2BAC1569CD541E7E2F02CDE3D`, status pass. Rendering was deliberately skipped under the translation-only boundary.

All passes above concern evidence serialization and projection integrity only. They do not validate German, Korean, formulas, completeness, compilation, rendering, or publication readiness.

The exact independent-checker request is `CHECKER_HANDOFF_U01_U12.md`, 18,534 bytes / SHA-256 `430FAB4BF94DB1C4FA7B659E44B73DE714E2F56C608E6BD9716F66BCEEB40728`. It binds all source/target identities and evidence authorities but is itself a producer handoff, not a checker receipt.

Archive disposition follows `CJK-KO-ARCH-001`: this unchecked, uncompiled, unrendered, unassembled producer state is eligible for immediate preservation and publication as honestly labeled mathematical work. Missing checker/build/QA states are metadata, not release holds. Archive maintenance owns coherent snapshots, public projections, privacy/security remediation, and publication; the translation producer does not perform or claim those operations.

## Explicitly unperformed

- source/scan/branch comparison, German adjudication, or German patching;
- Korean semantic, formula, completeness, terminology, style, Hangul/Hanja, or ko-KP review;
- compilation, build-log inspection, rendering, visual QA, assembly, packaging, certification, approval, publication, or archive package creation;
- SGA work.

Next state transition: a separately assigned independent Korean checker. The exact Paper 41 canon binder and pointer v003 are delivered and change no target state. Decision anchors: `CJK-KO-P41-001`–`004`; latest difficulty record: `CJK-KO-P41-HARD-016`.
