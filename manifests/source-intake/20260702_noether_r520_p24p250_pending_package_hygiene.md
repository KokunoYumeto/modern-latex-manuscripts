# Noether R520 - Paper 24 p250 Pending Package-Hygiene Note

Local folder:
`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_R520_LocalCodex_R519_P24p250_SubstitutionChain_SourceFix_20260702`

This folder appears to contain a TeX-changing Paper 24 p250 source-fix candidate
on top of R519, but it is **not** yet a clean package. Its `README.md` and audit
folder still describe R519, and no `summary_R520.json` or
`confirmed_fixes_R520.csv` was present when swept. Do not advertise R520 as the
current public Noether source-control head until the package metadata is repaired
and the source dispositions are made explicit.

Observed R520 TeX diff against the folder's R519 input:

- Paper 24 p250: `-t_{i\lambda}` changed to source-style `-t_{\lambda i}`.
- Paper 24 p250, Satz VII chain display: terminal `=\frako` removed from the
  displayed chain after `\frakp_{n-i+1}`.

Measured local files:

| File | Bytes | SHA256 |
|---|---:|---|
| `cum/cum_de_R520_p24p250_substitution_chain.tex` | 2,145,855 | `5B11AD53F4411F1579C2F0911F0003995063E00FA6B0A0013E8CE183D33CDA21` |
| `cum/cum_de_R520_p24p250_substitution_chain.pdf` | 2,642,929 | `EBB12D93AEFA8CA68715BC6B94CC0E2941A07DC610A658422996604AF63EEE80` |
| `rendered_fixed/R520_cum_pdf_page258.png` | 588,766 | `0675836C94F4C0E5B7F08D70B21412B8E00879D2992FA92748F4264D2761E5F4` |
| `source/P24_print_p250_leaf_0255.jp2` | 417,332 | `AD62069CB04D846314364B83140718747B3F7E9250F0912AE5B87DC8628EFFD9` |
| `source/P24_p250_render1000_equiv.png` | 5,945,576 | `461DCE42E46AF79CD5BCDECB2E0261BB08AC5B04694689417607B362A8E2BDD2` |

Classification: local pending source-fix candidate / package-hygiene blocker.
Not a clean ZIP, not a public reader release, not Paper 24 certification, not
Noether closure, not whole-corpus certification, not multilingual
synchronization, and not critical-edition material.
