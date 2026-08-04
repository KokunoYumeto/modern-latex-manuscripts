# Paper 21 producer worker returns

All returns are translation/production only. No worker performed or claimed source, formula, semantic, terminology, translation-quality, rendered-visual, native/regional, approval, publication, archive, or certification checking.

## Translation segments

- `/root/p21_hans_a`: source A SHA-256 `B6653D3F08C26A60A258BD31C21E8CC7334211D2AA20C2289272BFE49C61ED8F`; Hans return SHA-256 `6A15D0FF60A90B84545D35EC2A228EA96F9323F3EA1C84C469ABFC6CF8B64984`. It exposed `formentheoretische Durchbildung`, `integralfreie formale Identität`, `kogredient`, and historical citation phrasing for checker attention.
- `/root/p21_hans_b`: source B SHA-256 `2CC054EA3471A2CA1755BF04B23C2451F708040B9A8F60B3F3B4753E445E26AA`; initial Hans SHA-256 `DE08C37CA9387CD07F43710DED1446F38768ADB640EE3F6F0F28ABFDE79E3679`, using `组量` for `Reihen`. Root changed only `组量` to `变量组`, yielding final B SHA-256 `5507F296C4AE65C5CDCF7CB452B08A5E015579A0FC506B09AF33A99E23F55383`; this is producer convergence, not validation.
- `/root/p21_hans_c`: source C SHA-256 `CA8F97A2850467896E6ECC5717605B43E22C993B2D6BDB0BD863E915A7CF27FC`; Hans return SHA-256 `24AD7EC3BD1AFC99798C341876AC49525F5E44F817554187635B7CC442F7BA76`. It exposed `Divergenzen`/`散度` for checker attention.

## Controlled Hant and build

`/root/p21_hant_build` generated controlled-generic Hant from Hans SHA-256 `F4BCD4C27ED724EA4D79B1EAC0E427E370E2CB5BA1970200B1FD7A26D58E8235` and performed two successful engine passes without viewing the PDF. Hant TeX/PDF/log SHA-256: `09ECD8499AAF75027554FF51069E4C9D054D2D617A4176307F4E01000A81C9E4` / `66094E493F6A0C94C4A51DAF5785DCBCD91EBA7E5E8212A4C915FD57C5EDB194` / `38DA188AF8953D5220348E8AF1D6A4202681EEE9C9D88E56F8207D88D151BF09`. The pass-1 wrapper parser rejected MiKTeX's byte-count-free summary only after the engine exited `0`; only that parser was broadened. Hant remained unchanged and nonregional.

## Evidence and docs

`/root/p21_evidence` produced three 20-row CSVs and a 100-node/100-edge graph, bound to exact source/witness/Hans/Hant hashes; deterministic rerun stable. Final terminology/adverse/CJKV/graph SHA-256: `679184B13B168A580424E2ADF4A6F247A68A3BB92E3FCE0FBF5300697A81FDFF`, `924CFA1EC5E80E0115800F87BF4E65A4FC99E6AACE024FC8CE1E92D36AF990E8`, `00564117245C0D188DF98E01FE9FF15BB0C013F640FA7AE979DF7EE846E0776B`, `D5F863120E65F360A44A1FB95800A800DD74ED6AE2C0171A6B51F389DAA10AA8`. Root mechanically confirmed compatible headers, row counts, and zero dangling graph references.

`/root/p21_docs` drafted `TRANSLATION_NOTES.md` and `STATUS.md` before Hant/evidence completion, initial SHA-256 `D05314E04FE0530DD162D174CBE1A2612D0DB99AE7EBB94D9A6D6170E5516CA1` / `4270C7F01FEC88C3CB16F865B710FB1FE506C37019D4C799FE870CEBFBDF89E4`. Root appended final Hant/evidence metadata; final hashes are recorded in the handoff.
