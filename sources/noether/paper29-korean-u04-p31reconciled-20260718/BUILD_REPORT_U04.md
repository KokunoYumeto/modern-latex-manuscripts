# P29-KO-U04 build report

German control:

- TeX: `source/Noether_Paper29_German_P31_U04_control.tex`
- TeX SHA-256: `39330A560FAAEE4B2AD800887F2C84772E4365E1D6C2850CACCF989E14728C3F`
- engine: pdfLaTeX, two successful nonstop/halt-on-error passes
- PDF: `2EC1E72D761D61A6E09E35395570DBA5BCAFB5C8F495B235DEF05F87960EA64D`, 90,240 bytes, one page
- log: `5A9B20884457972AB6A5E5F3A8A7B89D6B66EB75849AD01133BAF4BDC812B2A9`
- extracted text: `761748564994A8133DEE6ED059EAA3D59D6DA8918B40F19898FA366C314723D4`

Preserved Korean first draft:

- TeX/PDF/render: `BF3A1427AF75CC37E7CB65FCF1FEDB5632FF6CECB2E66851C314F5136A7A8789` / `189CEC31652D4ACCCF66D4B753838AF302F82C178565FA00051E1EA3F57969F2` / `748FD72C4E6A898DA1B2AF3CF9B305653442534941735D94BE7FF11E45458FCE`
- build: two successful XeLaTeX passes, one page
- log: `3057F54BF7E9C8AC4CAD599E5EF92EE7132D9EAE3841D8D0145E85FAEE0D9925`; one underfull-box diagnostic at the long source-label line
- state: superseded after independent review, retained as genuine before evidence

Accepted Korean target:

- TeX: `ko/Noether_Paper29_Korean_U04_v001.tex`
- TeX SHA-256: `A967222517ABF3392BA10B2CF166EDCDF455F13E5D5C29A00A9A49E609ECE9A4`
- engine: XeLaTeX, two successful nonstop/halt-on-error passes
- PDF: `5AD0B7D710C82B686EA2F67820F2CA29400205E31CD7D7EA1169A530E46CC5DE`, 48,680 bytes, one page
- log: `F4DE1B5C8FAB4D93F3AD649219ADE7F6728B489A4F57F0B616B69CC43B43E8AB`
- warning/error/overfull/underfull/missing-character pattern hits: zero
- extracted text: `618CD72304BC965F3A7A26D489C67E0D3F513BA6D7E3AB853132103CD24B9E46`, 324 Hangul syllables, zero replacement/black-square glyphs

Rendering used the bundled Poppler executable directly. This build report establishes successful local builds, not reproducibility on every platform or external publication acceptance.
