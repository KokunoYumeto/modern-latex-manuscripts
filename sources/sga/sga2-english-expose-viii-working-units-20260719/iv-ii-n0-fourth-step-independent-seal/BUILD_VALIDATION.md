# Build validation

Target: `SGA2_Expose_VIII_Fourth_Step_iv_Implies_ii_Induction_n0_English_SourceAligned.tex`.

Two `pdflatex -interaction=nonstopmode -halt-on-error` passes exited zero.
Pass 1 contains only the expected `rerunfilecheck` request after first
creation of the outline file. Pass 2 contains zero error, warning, overfull,
underfull, undefined-control, or missing-character diagnostic. Raw logs remain
local-only. The two public logs replace line-wrapped local-user paths and pass
both raw and whitespace-elided private-path scans.

- TeX: 1,468 bytes, SHA-256
  `071C954BE17C8F62A4222B11BC466AA573D0E37B555A403B15322394168FC877`.
- PDF: 202,494 bytes, one A4 page, SHA-256
  `76D60911836C8E2C550ED459D0F475BCC4C2B6A47BDE4F4AF6917300C8D80434`.
- Pass-1 sanitized log: 7,015 bytes, SHA-256
  `CE7A1E30177F56DF1437A8FA642315574334203FAA596A8557036BB08C583D9E`.
- Pass-2 sanitized log: 6,919 bytes, SHA-256
  `50966820F100F398CF5DE5C289C812FA002672F486E22DCA6A779E72C24CE13F`.
- Layout extraction: 998 bytes, SHA-256
  `4AC20CE5227F366D1D354F3D95534971FA64914688E1E0DF813FAB8A2F44C4FF`.
- Target render: 201,841 bytes, SHA-256
  `B258602D805D21EE178BC73DE984742718013BC2E5DFFF8EDF512DC2E480E520`.

Extraction contains one expected form-feed page delimiter and zero forbidden
non-layout control bytes. It preserves `(iv) implies (ii)`, `x in U`,
`c(x)=1`, `prof F_x >= n`, induction on `n`, and the `n=0` vacuity sentence.
All 13 font records are embedded, subset, and Unicode-mapped. The PDF is
unencrypted and searchable. It has descriptive title/author metadata but no
XMP metadata stream and is untagged; these are bounded-review limitations.

An independent isolated two-pass rebuild also exited zero. Its PDF is 202,494
bytes, SHA-256
`E38E5EF2BDB0C8ED0EC22718ECE9CAC38F8C293DA95DD879D5FFD6E6927DC7A5`;
the hash differs from the frozen target only through volatile timestamps.
Independent extraction and 300-dpi render are byte-identical to the target.
The independent final TeX log SHA-256 is
`405267045C34B98AD83E0733CA5532624C726387E2C79439706514BC8511A544`.

Status: build, extraction, font, privacy, and independent-reproducibility gates
pass for this bounded checkpoint.
