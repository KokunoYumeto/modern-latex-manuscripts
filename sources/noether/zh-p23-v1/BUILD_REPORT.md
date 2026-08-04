# Build report

On 2026-07-18, the German control, `zh-Hans-CN`, and controlled `zh-Hant` TeX files were each compiled twice with XeLaTeX using `-interaction=nonstopmode -halt-on-error`.

| Artifact | Pages | TeX SHA-256 | PDF SHA-256 | Result |
|---|---:|---|---|---|
| German control | 6 | `54E02A5D60895FF71DEBF44F63C5B1E7EB3144B5B23CF856F3A59C3C35BF12B0` | `BAD925C9E750CC4D85198E93EB8DF65330A9BA5133C767E4E1D0C6D8BAEE0C87` | pass |
| `zh-Hans-CN` | 4 | `7D3F73762F556712AA8036794125EE2118C6FD4BBFB1D0DC45CC076F4057E4B1` | `C73EF8B2CF1A277B01DAB9FE549EBC437DF9B89A22D06BC9275E1864ABCFBB78` | pass |
| controlled `zh-Hant` | 4 | `A0ACEA7828DE2E3D5B3177A76A9F250E1FD37DC4EA8A114396446CDA4EC0B101` | `B3CD0E3308CD3271D91294BD7A0ABBAF8B7E540FDF45F37FBD3B8D82ED943BB3` | pass |

There are no compile errors, LaTeX warnings, missing-character diagnostics, or overfull boxes. Each Chinese log retains the same nonfatal underfull Latin bibliography line (badness 1062). PDF byte hashes supersede earlier intermediate-build hashes; TeX hashes are unchanged.
