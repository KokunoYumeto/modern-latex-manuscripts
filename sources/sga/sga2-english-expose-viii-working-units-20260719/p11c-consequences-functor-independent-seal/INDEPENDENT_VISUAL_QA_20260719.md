# Independent visual QA - 2026-07-19

Fresh independent evidence inspected at original resolution:

- source physical 75, 300 dpi: 332243 bytes, SHA-256
  `D13621ADFEC9DDB74D3A802615BB7D4AD8102DAD50F6BE0171A33BEABFCE82D2`;
- source physical 76, 300 dpi: 526199 bytes, SHA-256
  `E3EFDB05C525745D95970F4AF61531AED6A542E24F33E0AE4935DD8D6F3FD183`;
- source physical 75 critical crop, 600 dpi: 352708 bytes, SHA-256
  `D3D5626958ECD7722D786743A1956BBD640777FEA038B637E33E806B4ADA94A0`;
- source physical 76 critical crop, 600 dpi: 281289 bytes, SHA-256
  `333CB51164C78D7600582951563AD3A40F3D09541904B2F894C996DA5EE47A6C`;
- target page 1, 300 dpi: 339894 bytes, SHA-256
  `45BD554977768FCA06CDEF5C6EA5EB4270CD4786AE418B32D3B6E8AA496BA6E8`;
- target critical crop, 600 dpi: 664960 bytes, SHA-256
  `8EE665C5837A38421DEAB774AD12964725F82B0778FDE7158B04B7C2476F64ED`.

PASS: no clipping, overlap, blank output, glyph loss, broken formula, or
boundary spill. The French page break from physical 75 to 76 and the distinct
printed/running pagination are confirmed. Every required operator, tilde,
argument, category, variance marker, functor identifier, and degree is legible.
Lemma 1.2 is absent from the target.
