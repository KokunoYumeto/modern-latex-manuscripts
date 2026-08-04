# Paper 20 Segment A — Chinese Producer Return

- Work unit: complete assigned Paper 20 segment A only.
- German source: `segments/source/P20_A_lines12377_12437.tex`
- German source SHA-256: `DFD92DE298F422E2D993CC3162E3B031D41E4ECB67E32CB967FE0A1FD6CF237E`
- Simplified-Chinese output: `segments/zh-Hans-CN/P20_A_zh-Hans-CN.tex`
- Simplified-Chinese output SHA-256: `B637B38DBD55BCF8BA6862F000B48D9108FC77F8D42D083762A5AE97081559FC`
- Target posture: PRC-oriented Simplified Chinese (`zh-Hans-CN`).

## Producer lexical choices and uncertainties

- `absolut irreduzibel` → “绝对不可约”.
- `Reduzibilitätsform` → “可约性形式”; producer alternatives: “可约形式”, “可约判别形式”.
- `algebraisch-abgeschlossener Körper` → “代数闭域”.
- `Koeffizientenbereich` → “系数域”; producer alternative: “系数范围”.
- `ganze rationale, ganzzahlige Funktion` → “整有理、整系数函数”; producer alternative: “整系数多项式”.
- `relativ ganze Funktionen` → “相对整函数”.
- `Ideal aus Polynomen` / `Primideal` → “多项式理想” / “素理想”.
- `Basispolynome` → “基多项式”; producer alternative: “基底多项式”.
- `Graderniedrigung` → “降次”.
- `irreduzibles algebraisches Gebilde` → “不可约代数构形”; producer alternative: “不可约代数簇”.
- `Parameterdarstellung` → “参数表示”; `Norm` → “范数”.
- The source's `Dimensionen l,m,l+m` for the homogenized forms was rendered “次数分别为 \(l,m,l+m\)”; the historical terminology remains a checker decision.
- Personal names `Steinitz`, `Ostrowski`, `Hilbert`, and `Kronecker` were retained in Latin spelling except for the article author line.

## Explicit no-check status

This worker translated only. The inherited Chinese witness was not compared, audited, or consulted for validation. I did not source-check, collate, semantically/formulaically/terminologically check, review, compile, render, inspect a PDF, regionalize Traditional Chinese, approve, publish, archive, certify, edit the lane log or registry, or touch another segment. The lexical alternatives above are producer uncertainty only and carry no validation claim.

## Compile-driven TeX syntax repair history

- An upstream mechanical XeLaTeX pass was reported to have stopped at segment line 17 because the exact token `(n\ge2)` left `\ge` outside math mode.
- Reported failed-build outcome: pass 1 stopped with no pages produced. This worker did not rerun or inspect that build.
- Pre-repair segment SHA-256: `B637B38DBD55BCF8BA6862F000B48D9108FC77F8D42D083762A5AE97081559FC`.
- Exact mechanical change: `(n\ge2)` → `\(n\ge2\)` at segment line 17; no other token was intentionally changed.
- Post-repair segment SHA-256: `51BDBA85125DC72494746B49540FD6EF5DE21D7DD2854F86558B726E06586B3F`.
- Follow-up compilation by this worker: not performed, as instructed.
- Status remains translation production plus a compile-driven delimiter repair only. The failure and repair do not establish source, semantic, formula-content, terminology, translation-quality, visual, native/regional, approval, publication, archive, or certification validity.

## Append-only continuation of compile-driven repair history

- The next upstream pass-1 invocation also stopped with no pages because a second exact literal `(n\ge2)` remained outside math mode in the paragraph beginning `1. 首先证明`.
- Only that second exact literal was changed to `\(n\ge2\)`, producing intermediate segment SHA-256 `F4317188496FE61F220343C1C941E7D6F7EF02707F463D3FA208203963BD1AC6`.
- The following upstream pass-1 invocation again stopped with no pages because a third exact literal `(n\ge2)` remained outside math mode in the sentence ending `必定绝对不可约`.
- Root mechanically changed only that third exact literal to `\(n\ge2\)`. Final segment SHA-256: `80AA4F63166554C74EB29806CF1DCE77A6C98F1DB31EC181FD1BF9A372CCC4DC`.
- No prose choice was changed in any of these three repairs. They were compiler-triggered delimiter restoration only, not source, semantic, formula-content, terminology, translation-quality, or visual checking.

## Append-only fourth compile-driven repair

- The next upstream pass-1 invocation advanced to one page and then stopped on the malformed inline delimiter `(F(x,y)\)`.
- Root changed only that malformed token to `\(F(x,y)\)`, without changing prose. Final segment-A SHA-256: `DC694B77A78B1D12E12BC5A3DA315147538847F23F0E46772D85A7BAE9181834`.
- A later upstream build completed, but that compilation success remains mechanical production evidence only and does not validate source fidelity, formula content, terminology, translation quality, or appearance.
