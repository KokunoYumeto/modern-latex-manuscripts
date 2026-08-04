# Noether Paper 39 — authority-bound v002 mechanical build report

Claim class: **producer computation only**. This report records deterministic generation, compiler execution, PDF container facts, and file custody. It is not source, semantic, formula, linguistic, visual, regional, human, archive, publication, or certification validation.

## Source and target identity

- Binder: `NOETH-DE-BINDER-P39-ZH-COMPLETE-20260804-001`; receipt SHA-256 `39C97E6424B0ACCD8FFDFD218A422F59501BFC48456000BAB717F0CC15951E8C`.
- Pointer: `NOETH-DE-AUTH-v006-20260804`; snapshot SHA-256 `DB99DD87100654674D7ED24B4ABBBBC3A9920CCF035740D276CE8A87A5313C18`.
- Retained LF source: 18,724 bytes / `4F6355189925F249DE27FE5FD25C22FB3A2226088EBB7CAF5CB486607A112B7C`.
- Canon-owner delta: zero translation-visible text; 90 CR bytes only.
- The v002 Hans and Hant document bodies beginning at `\documentclass` are each byte-identical to their v001 counterparts. Only authority metadata comments changed.

## Controlled Hant generation

- Generator: `qa/build_hant_producer.py`, SHA-256 `C4D7BC0BDA17BCDE088D4182265D6558A1E4A10F75B99F7C48C88D0E7BB8A50A`.
- Record: `qa/OPENCC_PRODUCER_RECORD_v002.json`, 2,969 bytes / `0A09917DFBD4BECCE7E2C4186563A447DAA61069F0B9502F667AC6FDF095CB8C`.
- Converter: `opencc-python-reimplemented` 0.1.7, `s2t`, followed by the recorded controlled normalizations.
- Output is controlled-generic Hant only; it is not Taiwan, Hong Kong, or Macao localization.

## Compiler

- Engine: XeTeX/XeLaTeX `3.141592653-2.6-0.999998`, MiKTeX `26.5`.
- Invocation: `xelatex -interaction=nonstopmode -halt-on-error <target.tex>`.
- Execution: two serial passes for Hans, followed by two serial passes for Hant.
- Result: all four invocations exited `0`.

## zh-Hans-CN v002

- TeX: 16,141 bytes / `101836C41985DEE9B1A8FCC74A76CD9DF082BE2D07E2A3D45E22BC4DE68C6FE6`.
- PDF: 261,533 bytes / `367061323E97D9D7431B883D48F190A214A224D62F3901C8E01DD1BCA7125BA1`.
- Final log: 20,963 bytes / `75C218C59E80671625D4686DCFA5E31FD01717F6EB601CE92C5F841E274D7105`.
- Log scan: zero fatal/emergency/undefined-control, zero overfull, zero underfull. Two unavailable font shapes plus the summary substitution warning remain.
- `mutool info -M`: PDF 1.5, four pages.

## controlled-generic zh-Hant v002

- TeX: 16,322 bytes / `DEF7DFDCF1545066447880698B1A1C109D4BBED2CEDC4B8409D786044FCEEE33`.
- PDF: 276,331 bytes / `EE22B4475DB19B48FDD7838A307C0069CE06682EBDC370AB4A9BBE46DEC431C5`.
- Final log: 21,044 bytes / `D6AC05C3D9C96451E68569E35ABFA0960D8D8E163890ED714E821C7F0F15BFC2`.
- Log scan: zero fatal/emergency/undefined-control, zero overfull, zero underfull. Two unavailable font shapes plus the summary substitution warning remain.
- `mutool info -M`: PDF 1.5, four pages.

## Tooling adverse evidence

The installed `pdfinfo.cmd` wrapper failed with exit code `1` and `The system cannot find the path specified.` It changed no file. The bounded fallback used the exact installed `mutool.exe` and succeeded for both PDFs. No target PDF was opened, rendered, or visually inspected by the producer.

## Required independent work

An independent checker must verify source/translation/formula/terminology fidelity, controlled Hant behavior, extract/render both PDFs, and inspect every page. Mechanical success and body identity are not acceptance.
