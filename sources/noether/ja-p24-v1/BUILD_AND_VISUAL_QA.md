# Build and visual QA

- Engine: MiKTeX XeLaTeX. After all semantic and pagination changes, two consecutive `-halt-on-error` passes exited 0 against the same exact TeX.
- Accepted TeX: SHA-256 `E597F143D06B8EC4CD0CE5CBE42A1DB77C86D65FD080CDE6206C57379930704E`; article-span SHA-256 `C623010EC3232EFECFA1AC9EE8372C66D1A8882BBA194864207455E9D5CDB3BA`.
- Accepted PDF: `output/pdf/Noether_Paper24_Japanese_SourceReconciled_v001.pdf`, SHA-256 `C1032A418366B61DCC9F7EC743FDA29E60C6CB2CB7032DA4AAC941D95820DBDB`, 472,241 bytes, 16 A4 pages.
- Final build transcripts: `output/pdf/build_final_pass1_console.log` and `output/pdf/build_final_pass2_console.log`. Both passes completed successfully.
- Diagnostic scan: zero fatal errors, undefined controls, missing characters, overfull boxes, underfull boxes, LaTeX warnings, package warnings, and font warnings.
- Text extraction: `output/pdf/Noether_Paper24_Japanese_SourceReconciled_v001.txt`, 98,953 bytes, SHA-256 `D7A6765954426D566A1902B5F31105908028F966C83E7553DEFB3978BC64F6E4`. The extraction preserves the title/apparatus, Japanese body, formula families, notes, dated receipt line, and article boundary.
- The accepted PDF was freshly rendered to 16 individual PNG pages at 200 ppi. Every page was inspected at original detail. The final set has no clipping, collision, missing glyph, margin overflow, or Japanese lexical unit divided across a page boundary.

## Rejected pagination history

Successive otherwise clean candidates were rejected after individual-page inspection exposed page-boundary splits in `拡大`, `素イデアル`, `なぜなら`, `係数領域`, `再び`, `そのとき`, `任意`, `互いに対応する`, `随伴素イデアル`, `剰余体`, `用いるとき`, or `ノルム`. These were not repaired by assuming fixed page numbers: each textual or nonbreak adjustment was followed by two fresh builds, extraction, complete rerendering, and renewed inspection because pagination moved between candidates.

The exact E597/C103 final render removes all twelve rejected lexical splits. Some page boundaries continue complete mathematical phrases across pages, but none divides a Japanese lexical unit or creates a legibility defect.

## Rejected QA artifact

`render_check/CONTACT_SHEET.png` rendered effectively blank even when its constituent page PNGs were valid. It is rejected and is not visual evidence. The individual original-detail page PNGs are the sole render authority.

Build success and internal visual inspection do not imply external/community certification or independent human-reader validation.
