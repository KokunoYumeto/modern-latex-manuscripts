# P29 Korean U02 build report

The compact German control and Korean target each completed two XeLaTeX passes with `-interaction=nonstopmode -halt-on-error` and produced a one-page A4 PDF.

| Artifact | Result | Pages | Page size | Log QA |
|---|---|---:|---|---|
| `source/Noether_Paper29_German_P31_U02_control.pdf` | pass | 1 | A4 | zero fatal/undefined/missing-character/overfull/underfull pattern hits |
| `ko/Noether_Paper29_Korean_U02_v001.pdf` | pass | 1 | A4 | zero fatal/undefined/missing-character/overfull/underfull pattern hits |

Final Korean artifacts:

- TeX: 6,043 bytes, SHA-256 `B694D05E57B58E1B0373D976356E6B3B3F4883D7CC9398081DB12111877B6A7C`.
- PDF: 66,423 bytes, SHA-256 `EE0A0ED2E150A5EC48945EA7E47C3F394667F288FF5E933BB00DDF193FBE8988`.
- build log: SHA-256 `35C9716B03E2C83FF903D52F641B0164E492A9004115A674C826C78A732EFB0C`.
- extracted text: 4,795 bytes, SHA-256 `03809CD17FC50AEEFAFC93F301148BADCCB0DC90C80A36353553001AAB91DB1B`.
- extraction diagnostics: 2,720 PowerShell string characters, 1,035 Hangul syllables, no U+FFFD replacement character, and no square placeholder.

Final compact German control artifacts:

- TeX: SHA-256 `2EE37B4F71D27EC61BFFA7C3603DCC019362FC31270533F4930B9D9189809B6A`.
- PDF: 37,422 bytes, SHA-256 `7B053D7AF86A83E371F278CFB6BB57EAF6765EF847B816A09FB7B5340FBCCAAF`.
- build log: SHA-256 `EF46444B2FAFB0E21F0C4E32DBF2E3E2C43A7862F87ACE389D09FAEF81C3944C`.
- extracted text: 4,668 bytes; 4,604 PowerShell string characters; no U+FFFD replacement character or square placeholder.

The earlier 11pt German control produced an almost-empty second page and is retained only as failed/superseded evidence. The prior Korean reviewed state is likewise retained by hash in decision `CJK-KO-P29-006`. The earliest stranded-footnote draft was overwritten before hashing; its hash is honestly unavailable.

Build success is not source, semantic, visual, or external certification. Overbars disappear in plain-text extraction, so the PDF render is the controlling notation-visibility check.
