# Paper 29 build report

Build engine: MiKTeX-XeTeX 4.18 (MiKTeX 26.5).

Each of the German control, `zh-Hans-CN`, and controlled `zh-Hant` editions completed two consecutive builds with:

```text
xelatex -interaction=nonstopmode -halt-on-error <source.tex>
```

## Final outputs

| Edition | Pages | TeX SHA-256 | PDF SHA-256 | Diagnostic result |
|---|---:|---|---|---|
| German source control | 5 | `60F8AF840CD9CAA610F86F11C5405800910494E759894D8A7F1C36AC0E8B3AFA` | `22C1B3B546266B85302167FC84DCE9EFF63E85EC581287CE7CC4FC98C7438F5B` | pass; one non-fatal underfull hbox |
| `zh-Hans-CN` | 4 | `E7EB24FC640BE7BE1FF9A506DF867ECB00E03CA2258CF4F5C5902C5D66828FAB` | `995D16B71E39CCBFD0E576453567481A8444635A7B7F3FB3A0163C8658505A63` | clean scan |
| controlled `zh-Hant` | 4 | `3C0187C271FA870D86DEDF5941B893052ABB2C362FC922B1DAE96431BFC42040` | `1457F08EA4E3EA95BA284570DD45AEFD089E4D7AB1F86075694B930E8DD98656` | clean scan |

All three PDFs are unencrypted A4 PDF 1.5 files. Layout-preserving text extraction yielded five, four, and four form-feed page boundaries respectively. The Hans and Hant logs contain no fatal/error, undefined-control, missing-character, overfull, underfull, or warning matches. The German wrapper contains one underfull hbox at lines 37--38, badness 1394; rendered inspection found no associated defect.

The machine-readable record is `qa/BUILD_LOG.json`.
