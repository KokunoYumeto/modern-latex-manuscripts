# Continuation handoff

## Authority

- Part I: `authority_snapshot/jstage_part_I_9_2_119.pdf`, 7,305,283 bytes,
  SHA-256 `5A8E5720BC2EF8905BF85F7919C65AC4A87A31CFC854BD77E6B5084C0D2DEBEF`.
- Part II: `authority_snapshot/jstage_part_II_9_3_185.pdf`, 3,984,260 bytes,
  SHA-256 `8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53`.
- Local comparison: 12,897,534 bytes, SHA-256
  `57B8FE1A4563FAB33D56F2CA0171D4843D37FBBDE982A84859E2E232494B6D78`.
- Exact map: local 1--65 = official I 1--65 = printed 119--183; local 66 is
  blank; local 67--103 = official II 1--37 = printed 185--221.

## Admitted coverage

Printed p.119 is admitted through the terminal words `de sorte` in diplomatic
French, corrected French with no correction, and source-aligned English through
`so that`. Title, author, receipt line, Introduction heading, footnote 1, all
four body paragraphs, and all visible references are retained.

## Exact next cursor

Printed p.120, official Part-I PDF page 2, first source-bearing continuation
after p.119 `de sorte`. Resume the open Introduction no.1 paragraph; do not
repeat or rewrite p.119.

## Method

Render one page at a time in approximately 1,100--1,800-dpi-equivalent
overlapping reading bands. Escalate only genuinely ambiguous small marks to a
targeted 5,000--9,000-dpi-equivalent crop. Do not generate OCR. The image
decides. Keep all three text layers distinct; append decisions and reversals.

## Build

From this root run `powershell -NoProfile -File .\tools\build_readers.ps1
-Gate <new_gate_name>`. One reader compiles at a time. Never reuse a gate name
or overwrite an output PDF.

## Exclusions

Do not open or enter FGA, any other Grothendieck paper, EGA, SGA, Verdier, or
Illusie. Do not pass the terminal p.221 bibliography.

