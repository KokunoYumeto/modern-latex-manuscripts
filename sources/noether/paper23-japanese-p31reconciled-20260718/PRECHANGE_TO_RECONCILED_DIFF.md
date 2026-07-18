# Prechange-to-reconciled diff — Japanese Noether Paper 23

## Inputs and authority

- Inherited Japanese witness: cumulative reader whole-file SHA-256 `4A284DF3FAC4D53D305659B539AF2FEB17902BFB4C254A7DF62A155C6BC23131`; Paper 23 witness lines 12381–12516, LF-with-terminal-newline SHA-256 `0526B08C…3FE`.
- Sealed authority: P31 whole-file SHA-256 `A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F`; Paper 23 lines 13507–13630, raw SHA-256 `7A9E4C9910FBEFECA45A652BDF99A58F9C0BD4089D1F9630D96D776739B0BCE5`.
- Reconciled Japanese target: SHA-256 `758D36CA12EA463AD4DC23A04536E801FB9A6B190F8E79E87C668EDC15FEC6D9`.

The inherited reader is retained as a translation witness only. Lines 12517–12555 are Paper 24 setup and were excluded from the Paper 23 rebase.

## Material source-fidelity changes

- Restored the complete article apparatus: repeated title, journal citation, Leipzig lecture/report line, byline, opening note group/reset and `)` numbering, received date, group closure, clear page, and final note reset.
- Restored all source-controlled formula differences: three missing primed sums, exact terminal index families, both `g(y,d y)` loci in place of inherited `\varphi`, and all 34 literal source `d` tokens in place of a custom upright-d macro.
- Recombined the inherited split Hilbert equality into one source display and restored the source hanging topology for eight numbered logical items.
- Restored all fifteen note anchors and meanings, 27 semantic emphasis loci, 48 source-name small-cap loci, six bold section numerals, and source semicolon controls.
- Rebased Japanese terminology with local Japanese evidence and explicit adverse controls: `有限生成整域`, `整基底`, `イデアル基底`, algebraic `上整`, distinct `整数係数性`, `反傾変換`, explicit `d x と同じ変換則に従う`, `ガロア分解式`, `接続`, `共変微分`, `リーマン正規座標`, and `還元定理`.
- Kept `相対的に整な関数` and `ラグランジュの変分導関数` visibly source-tethered; the latter remains held because an exact independent Japanese historical compound was not recovered.

## Final layout-only delta after semantic attestation

The semantic source-target audit passed on TeX SHA-256 `3531549A9E68BD23F07D2C291372933E9ACC9AF0EC93CE8A8ACDC336BA862D0E`. The final TeX differs only by four content-neutral layout controls:

1. `\tag*` prints already-parenthesized source labels once;
2. `\mbox{すなわち有限個}` prevents the page-boundary split;
3. `\mbox{その方法}` prevents the page-boundary split;
4. `ラグランジ\nolinebreak[4]ュ` prevents line-initial small `ュ` without boxing the whole name.

Removing exactly those controls reproduces semantic SHA `3531549A…62D0E`. Independent final integrity QA found no other post-attestation change.

## Source-defect disposition

No German mathematical or textual source defect was found. The authoritative source audit and both final source-target checks agree. Consequently there is no duplicate check or route to `4 -nterslav` for Paper 23. Japanese witness, macro, pagination, and terminology defects are target-side only.
