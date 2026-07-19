# Independent review - SGA2-VIII-L24P

Status: pass for this bounded unit only.

Scope: corrected French TeX lines 2723-2731; original printed pages 90-91;
physical source-PDF page 80; recomposed running page 72. Blank line 2732 is
excluded. The exact continuation cursor is French line 2733.

## Source and mathematical disposition

The independent source review and a separate formula/branch review confirmed
the proof structure, symbols, references, and both disclosed emendations.

- The driver sets `original=false`, so `\sisi` selects the corrected
  branch
  `K=\ker(L^{-d}\to L^{-d+1})`. The unwrapped
  `(L^{d-1})_f` at French line 2730 is therefore a stale remnant of the
  inactive historical branch. The target's `(L^{-d})_f` restores the exact
  localized sequence.
- Only `f` is introduced, `D(f)` is the chosen principal open, and the
  displayed sequence ends in `M_f`. French `M_{f'}` has no defined
  `f'`; the target's `M_f` is retained.

Both readings remain visibly labelled as editorial emendations. The French
authority is byte-unchanged. Its compiled PDF is the same corrected edition
and is layout evidence, not independent textual corroboration. The
jcreinhold candidate remains comparison-only.

## Independent build and render evidence

An isolated two-pass build completed with zero errors, warnings, undefined
references, overfull boxes, or underfull boxes. It produced one 238809-byte
A4 page. The independent reports show 15/15 fonts embedded, subsetted, and
Unicode mapped, with destinations `Doc-Start` and `page.1`.

The independent extraction is byte-identical to the frozen extraction:
2357 bytes, SHA-256
`97D27F893B26F91309FD564D5978AAC9E28EE29C5DF807123902EFB993032895`,
with zero forbidden control bytes.

Independent target renders are byte-identical to the frozen target renders:

- 300 dpi: 376490 bytes, SHA-256
  `9CD95973FA497905135C157073780A1E6D1F778DF0E37AC0D6880BDDF4926BA9`;
- 600 dpi: 764833 bytes, SHA-256
  `533BC1FB9A9CFB1F444641C32319C5756B5940BB8AB65A612B597FC84AC9FA69`.

Independent source-page renders are also byte-identical to the self-gate
source renders but remain rights-sensitive internal evidence and are excluded
from the public payload.

Public sanitized independent build logs:

- pass 1: 23025 bytes, SHA-256
  `9335392115CB3F5EEEDEEE438EBA944D86191A042332FC46735F426563EAD743`;
- pass 2: 22894 bytes, SHA-256
  `851EA2FEBDA9BE7D728FB9029CFBE5A700F412D5534D02F4F5466E7C95748814`.

The original independent logs are preserved locally under their earlier
`*_SANITIZED.log` names, but they still expose machine-specific MiKTeX font
paths and are excluded. The `*_PUBLIC_SANITIZED.log` successors remove
those paths without changing the build diagnostics.

## Disposition

No substantive target-body correction was required after the self-gate.
CSV rectangularity, primary-ID uniqueness, formula safety, JSONL parsing and
revision/reference closure, manifest identity, source-render exclusion, and
privacy are final package gates. This review seals only the bounded Lemma 2.4
proof; it does not complete Exposé VIII, SGA2, a critical edition, or final
publication.
