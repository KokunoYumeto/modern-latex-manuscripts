# PDF visual and output-copy QA v10

Scope: controlled-Romance tranches T001–T006. This successor preserves the audited T001–T005 evidence and adds the complete three-page T006 continuation through authority line 21254.

`scripts/verify_pdf_renders_v10.py` renders every build PDF at 150 dpi with the pinned Poppler binary in one isolated temporary directory per tranche. It requires build/output byte equality, exact page counts 3/2/2/2/3/3, and byte-identical equality between every fresh PNG and its pinned QA image. Temporary render directories are removed automatically.

T006 pages were inspected at original resolution. Page 1 cleanly renders the theorem, free-module formula, three coordinate rules, and action definition. Page 2 has a deliberate top margin and cleanly renders the module axioms, mixed associativity, direct conclusion, reciprocal starred module, and left-acting column matrix. Page 3 has a safe top margin and a legible editorial sense note. No page has clipping, overlap, corrupted glyphs, overflow, or an unintended blank page. Lower whitespace is intentional for this bounded tranche.

This is layout and artifact-identity evidence only. Human observations, native-speaker observations, and intelligibility observations remain zero; `native_validated=false`, `human_validated=false`, and `pilot_claim=false`.
