# P29-KO-U03 build report

German control:

- TeX: source/Noether_Paper29_German_P31_U03_control.tex
- TeX SHA-256: EA0173AF280E1E18265092CA655F34F4D1385B07A60F661FAEC58087814FABD8
- engine: pdfLaTeX, two successful nonstop/halt-on-error passes
- PDF: A61A59A9FC7897AE2AAAA9B2CB40D8C4896189E1A2255D2ABD117826A2880772, 101,274 bytes, one page
- log: 4BC6898397CA7E62683CAFC5B3CCDED9371F5EAA1DE4DDF3F8173E945AB040A4
- extracted text: DC4F699C96AB8971EC76926CBED077F51AD8206AA532790E04B7AA134CC96DD7

Korean target:

- TeX: ko/Noether_Paper29_Korean_U03_v001.tex
- TeX SHA-256: 0DFEE79E2DF3A81005BDAF8488E108D9E324703133D0B9548F5A54933975CC60
- engine: XeLaTeX, two successful nonstop/halt-on-error passes
- PDF: 4E6DEC776EE572EFCC97138F21D0AE98ABA5A8F3DD4E3362E1BD2808A23D7A19, 52,700 bytes, one page
- log: 7909B82DB7BF9EC3B58E5765EB756CF2574F0A79EAB76B52C0ED65B59D8BE20F
- warning-pattern hits: zero
- extracted text: 8161AC0FD1A532C0730D2D4BCD85149539112E73E566912588A6D96832F9DC05, 379 Hangul syllables, zero replacement/square glyphs

Rendering used the bundled Poppler executable directly because the advertised wrapper pointed to a nonexistent delegated path. The failed wrapper produced no artifact or hash and remains recorded under CJK-KO-P29-U03-HARD-005.

This build report establishes successful local builds, not reproducibility on every platform or external publication acceptance.
