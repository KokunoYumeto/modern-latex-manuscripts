# Noether Paper 39 — v003 producer build report

Claim class: **producer computation only**. This report records exact integration custody and mechanical compiler results. It is not linguistic, source, formula, terminology, visual, regional, human, archive, publication, or certification validation.

## Inputs and deterministic generation

- Authority binder: `NOETH-DE-BINDER-P39-ZH-COMPLETE-20260804-001`; LF source 18,724 bytes / `4F6355189925F249DE27FE5FD25C22FB3A2226088EBB7CAF5CB486607A112B7C`.
- Sealed checker return: `ZHCHK-NOETHER-P39-V002-RETURN-001`; receipt `B4E07772158637DE71A83E7F3A7AAF461840ACB89A19E0DE355EA5DC2390F046`.
- Accepted Hans input/carry-forward: 16,141 bytes / `101836C41985DEE9B1A8FCC74A76CD9DF082BE2D07E2A3D45E22BC4DE68C6FE6`.
- Generator: `qa/build_hant_producer.py`, 4,888 bytes / `2500B88E802FBD44FC1BCB836CF5786FACCB54FC4E83E1595A6781918F0DA8CE`.
- Generation record: `qa/OPENCC_PRODUCER_RECORD_v003.json`, 3,270 bytes / `CB4816AAC238ACD6D7D4C0460C9797816FDBB35B867F9BFAEA9543181320D76D`.
- Generated Hant TeX: 16,322 bytes / `F0E9425763D5E075A5ED1810FE2B1DC2BDAAF6FD48691BE8C3D64F4B158AF1C8`; byte-identical to the sealed candidate.

## Compiler execution

- Engine: XeTeX/XeLaTeX `3.141592653-2.6-0.999998`, MiKTeX `26.5`.
- Invocation: `xelatex -interaction=nonstopmode -halt-on-error Noether_Paper39_Chinese_CurrentAuthority_zh-Hant-controlled_v003.tex`.
- Pass 1: exit `0`; started `2026-08-04T12:08:11.9886751+02:00`, ended `2026-08-04T12:08:13.2428703+02:00`.
- Pass 2: exit `0`; ended `2026-08-04T12:08:14.4327607+02:00`.
- Final PDF: 274,922 bytes / `A64F7461A4F4CE451CA7E153FF3C8D55854AD6BC730A7336FD6669F8170F38C8`.
- Final log: 21,044 bytes / `F0975196D04563EFB5747D4501E4ABCA27EEC7EB0882CB72C22269EC3C8B0B30`.
- Final aux: 494 bytes / `8C7D81DCDA4B6F30A01A83FEC4ADBAB682D909EA6EAD2D032CDC14D423AF18E5`.
- Compiler transcript: four pages; zero fatal error, emergency stop, undefined-control sequence, overfull box, underfull box, or missing-character event. Known unavailable Microsoft JhengHei small-cap and italic shapes fall back to upright.

The accepted Hans TeX/PDF were carried forward byte-for-byte and were not recompiled. No PDF was rendered, opened, or visually inspected by the producer. Independent checker extraction/render/visual acceptance remains required.
