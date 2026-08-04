# Noether Paper 43 — producer TeX syntax-repair record

Scope: producer-side syntax changes required for halt-on-error compilation. This is not source, semantic, formula, terminology, or visual checking.

## Bound file history

- Initial translated segment D SHA-256: `D43A90BA340D45B53288CCD047736367951E75C6AA9E56B52151B389B0481EC3` (16,266 bytes).
- Captured intermediate segment D hashes: `B04C8EB7F9CE16BD91C325B6E4320595900A630F1E2E8FF3121649F5F3CF8593`, then `51B5D78B4E522F42C5E87261092271943E6D20C7423F1A7752EF441B39F82C9C`.
- Penultimate segment D SHA-256 before the missing-glyph repair: `B97E4B30D93C96E983EA6DDF19892F48BA1F25571060FF74EB3B64E776AC4EE5`.
- Final segment D SHA-256: `97445D1F80BAD43B4908E9AEE7500E14BD1221DA88524B3E5861AB595D00DCFE` (16,340 bytes).
- Segments A, B, and C were not changed during this repair sequence.

## Mechanical changes

The compiler stopped successively where producer text placed TeX commands, subscripts, or superscripts outside math mode. The following expression classes were wrapped in existing inline-math notation without changing their symbol strings: `K^{(i)}`; `K=\mathfrak o_P`; `x-\xi`; `y-\eta`; `e^{(1)}`; `t_1,\ldots,t_n`; `t_2-\alpha_2,\ldots,t_n-\alpha_n`; `A_i`; `e,z,\ldots,z^{n-1}`; `c=c_1T_1+\cdots+c_nT_n` and neighboring coefficient conditions; `e,t_2,\ldots,t_n`; `u_1,\ldots,u_n`; and the section-7 `p^t`, idempotent, congruence, and polynomial expressions containing TeX control sequences. The final missing-character diagnostic was removed by changing display text `\text{ 中}。` to `\text{ 中。}` so that the Chinese full stop uses the CJK text font.

Plain parenthetical mathematical prose that did not itself break compilation was not systematically normalized. That typographic question remains for the independent checker.

## Compile result and adverse state

- Final Hans TeX/PDF/log SHA-256: `FDAF1A0B9F55DD5A972396E41A03F69DD966CC9BEDA8D82365B7010EBC3501D7` / `673088FCDC3AFB5620279ABA2667305AF95B18CB141F1608058A9E7F0DE72EE9` / `D58CA102FE30A81D987DCF21F7DC916CBCCFA4707F03306CE3C782F76FF869AE`.
- Final controlled-Hant TeX/PDF/log SHA-256: `4896BE04492C3BB5EBE2AAA7668F70E45D50A6224721EF4B873B6BB21F93156E` / `E75110A64B5A8532347FDF92C42BEDAC4D762CAD2973ECA3773C01B4204B5B21` / `9BB0272A00377BC2369EFFB890B917D7C6C2627983E1E234EB3CA3AB886A63BC`.
- Both final targets completed two halt-on-error passes with exit code 0 and compiler-reported 17 pages.
- Final logs contain zero error/fatal/missing-dollar, overfull, underfull, and missing-character matches. Each retains an italic CJK font-shape substitution warning and its summary occurrence.
- Partial PDFs/logs from failed attempts were overwritten. Not every intermediate assembled-file hash was captured; the hashes above are the exact captured milestones. This limitation is recorded rather than silently reconstructed.

## Epistemic and review state

Compiler locations and file hashes are computation/file facts. Choosing math delimiters and moving punctuation inside `\text{}` are producer implementation decisions. No claim is made that any formula, symbol choice, wording, source passage, or rendered page is correct. Independent checking remains absent.
