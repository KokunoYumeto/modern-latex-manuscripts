# Chinese Noether Paper 35 — corrected producer translation notes

## Scope and authority

This workspace is the active sibling correction revision for complete Noether Paper 35, *Über Maximalbereiche aus ganzzahligen Funktionen*. It contains PRC-oriented Simplified Chinese (`zh-Hans-CN`) and a controlled-generic Traditional-script derivative (`zh-Hant-controlled`). It contains no Singapore-specific Simplified-Chinese target and no Taiwan, Hong Kong, or Macao localization.

The bounded translation source remains the immutable span selected by German-canon task `019fca5c-f549-7e71-a314-66f7265343ca` in binder `NOETH-DE-BINDER-P35-20260804-001`:

- Zenodo concept DOI `10.5281/zenodo.20412587`; selected version DOI `10.5281/zenodo.21699405`.
- Complete source-native P35 span: 34,355 bytes, SHA-256 `2E205B2C51B9093FC61C77A9A1DF1C3399FCF098706CEC69134400F1ECC8E491`.
- LF translation source: 34,091 bytes, SHA-256 `DAED6EF21C297425F018C0AE6B23BC5BDD05C0B86984B3FC25FB5937DCBEBD6A`.
- Binder custody: `source/current/CHINESE_P35_BINDER_20260804.json`, 6,520 bytes, SHA-256 `CFE2D81FB1E5C74EC1F73A1076F6D002A895D01056A5CEE26F844F882AF70CF3`.

Pointer v004 is control metadata for future packets/units only. It did not reopen or replace this P35 binder. The Chinese producer made no German comparison or adjudication.

## Independent checker correction basis

The immutable v001 producer package was independently checked by task `019fca9c-f549-7e71-a314-66f7265343ca`. Return `ZHCHK-NOETHER-P35-RETURN-001` froze fourteen findings: eleven target-translation defects, two tooling defects, and one unresolved advisory. `F001` was blocking because the target repeatedly converted ring/domain objects into fields.

This revision applies `F001`--`F012` and `F014` exactly from the checker candidate. `F013` remains held: it concerns unresolved German punctuation without bounded primary-print evidence; the producer created no German packet and changed no German source.

The corrected Hans editable body is the byte-exact concatenation of:

- A: 11,737 bytes, SHA-256 `26A7615B9EFD825ADF20DABF9DE34673CB1F52807AC7E07A0F0118F79E8DD3EF`.
- B: 7,451 bytes, SHA-256 `5A2EB988239E78102D18F22AC552978AD987CE299E5B6A0D738FFA87034B2424`.
- C: 10,620 bytes, SHA-256 `5F62E3139C5528ABCD4ACB978EA6CC14AF1B052E6E3E78CBAFBB10161B5B01B3`.
- Concatenation: 29,808 bytes, SHA-256 `54061274DFDE806F491EE424277886ED4C4CEEF3F7E0315DFD1039AACF69F18A`.

That body occurs exactly once in both the producer Hans TeX and checker Hans candidate. The controlled-Hant translated body is likewise byte-identical to the checker Hant v002 candidate, 29,808 bytes, SHA-256 `E8B36BFF9AB5ABE1CB6FE1AF45370C101B11BBA8EA5A0491EAAC0B63CD05F2D0`. Whole-file identities differ because producer and checker wrappers have separate custody/provenance comments.

## Correction highlights

The substantive checker-frozen changes include:

- Ring/domain type repair: `极大整环`, `给定整环`, `多项式环`, and localization `系数环`, while genuine fields remain `域`.
- Consistent `整性基（即有限代数生成组）`, followed by `整性基`.
- Modern sense-first `代数无关系统`, with the historical `不可约系统` label retained only in an attributed first-use note.
- `雅可比矩阵` / `雅可比行列式` for derivative-matrix terminology.
- Explicit ideal containment rather than opaque `倍理想`.
- `非整代数数`, `每个 λ_i`, and `生成元` at the frozen loci.
- Target-only punctuation, note-reference, sentence, and display-presentation repairs.
- Controlled-Hant normalizations `這隻會→這只會`, `幷→並`, corrected `在…中` display wording inherited from Hans, and `代數無關係統→代數無關系統`.

Exact findings, alternatives, uncertainty, evidence, and checker validation state remain preserved in `controls/checker_return_001/P35_FINDING_LEDGER.jsonl`. The producer correction overlays under `evidence/revision2/` record disposition, sense windows, lexical-attractor basins, qualitative Mandarin-Simplified dominance debt, explicit localization absence, and adverse evidence. Those dominance records are never readiness scalars.

## Current targets

- Hans TeX/PDF: `DDF7E898E706552028C2BCEAC4BBDE3D45487C6A339F7FA0A43968FF7E1F465C` / `F6626C3DC6FFB82E3CFD5C21FA3F74B99459D477E39093715802C49E91E2A18C`.
- Controlled-Hant TeX/PDF: `FD16882FAC33B7FD7D0FFB882345168E40FA7F1F22FDEE83AFA2420627D1C054` / `8E77A4C511462C8ECF5876CE7EED0E3A9C4CAD8820A492BD8E665FB47FA50CF1`.
- Both targets completed two serial XeLaTeX passes and report six pages in retained logs.
- Neither PDF was opened or rendered by the producer.

## Claim boundary and next gate

These files are corrected producer outputs, not accepted translations. The producer performed no source-fidelity, semantic, formula, terminology, translation-quality, visual, native-speaker, or regional-localization check. The persistent Chinese checker must independently recheck the exact frozen revision, freshly render and inspect every page, and issue a second sealed return.

Japanese and Korean forms were not consulted and do not authorize Chinese. `zh-Hans-SG`, `zh-Hant-TW`, `zh-Hant-HK`, and `zh-Hant-MO` remain absent. Human/community certification, archive intake, and publication intake remain absent. SGA remains held pending explicit Floris authorization.
