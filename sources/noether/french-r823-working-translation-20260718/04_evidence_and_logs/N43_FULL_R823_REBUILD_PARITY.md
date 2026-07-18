# Paper 43 direct R823 French rebuild: full parity, build, and visual QA

Date: 2026-07-17  
Status: integrated into the production P1--43 cumulative; direct rebuild complete for Paper 43.

## Authority and preserved translation memory

Canonical package:

`C:/Users/Floris/Documents/Papors/Chatnotes/CHat translates and clean/Noether Multilingual/Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717_COMPLETE.zip`

- SHA-256: `7AFC1B865EC710F6BECE507260605CBA7C950E5CC089C7464F63CBC20A8BD738`

Exact cumulative German TeX authority:

`authority/R823/pkg_r823/Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717/1/01_cumulative/Noether_R823_cum_de.tex`

- SHA-256: `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`
- Paper 43 boundary: lines 20157--20964 inclusive.
- Normalized source-slice convention: UTF-8, LF, one trailing LF.

| R823 scope | Lines | Characters | UTF-8 bytes | SHA-256 |
|---|---:|---:|---:|---|
| Heading, editorial note, Introduction, §§1--3 | 20157--20415 | 42,175 | 42,484 | `1E3278CA4A61DBE3725D09FF38E71DADCC265E569FA18CC96EDFA2EC942DE0BB` |
| §§4--7 and receipt date | 20416--20964 | 45,943 | 46,223 | `5F8A557B78D8795B5CBAC6060F9C7D82C7F81456479423E2ADF96DDC1F035445` |
| Complete Paper 43 | 20157--20964 | 88,118 | 88,707 | `D78319A387B95C4F770F04EE22774FD031DAA1B3BD78007AE0E052B793FEBBB8` |

The recovered condensed French body remains preserved as translation memory at:

`working/backups/p1_43_pre_rebase_audit_20260717/tex/N43_fr_body.tex`

- 31,965 characters; SHA-256 `0D5FCDBF04D2F2F7791C958DC3EC06B2996B6C72D069C299934E8E3EEC632EAE`.
- It was not treated as authority and is no longer in the compiled dependency graph.

## Integrated French target

The production body is now an explicit two-fragment integration:

`working/r823_fr/tex/N43_fr_body.tex`

- SHA-256: `6C6D04189BCF34793FF038C59FE79A8E23C78910F1C01CC4577B3474815DFB60`
- It inputs, in order:
  1. `N43_rebuild_intro_s03_fr.tex` -- SHA-256 `22C0C91494CC99E3D2F42BBC8FB6E99ED71D70B4D2E299513884BB9940BD8B05`.
  2. `N43_rebuild_s04_s07_fr.tex` -- SHA-256 `6F734B867FBB03B93893F9DAE8E9D7DD160BAD2B37EDC714D80AEAECAEECF7C2`.

The two French fragments contain 92,252 characters. The direct target/source character ratio is `1.046914`, well above the binding non-condensation gate of `0.65`.

After the independent §§4--7 handoff, the deterministic Node legacy-glyph pass changed 20 literal section signs to `\S{}`. The pre-rewrite handed-off hash was `47989455C5B46A618C53257A064A0B83B6F647F8976B3A40B0FF159ADBA4651F`; no wording or mathematics changed. The fragment was recompiled after the rewrite.

## Structural and mathematical parity

| Token/block | R823 | French | Result |
|---|---:|---:|---|
| `\subsection*` (Introduction and §§1--7) | 8 | 8 | exact |
| `\paragraph{...}` | 51 | 51 | exact |
| source-note labels | 1)--13a), 14)--21) | 1)--13a), 14)--21) | exact |
| source-note macro occurrences | 26 | 26 | exact |
| display blocks, heading through §3 | 28 | 28 | exact |
| display blocks, §§4--7 | 80 | 80 | exact |
| all display blocks | 108 | 108 | exact |

For the 28 displays through §3, sequential comparison removed whitespace, punctuation, and localized `\hbox{...}` prose only; result: **0 mathematical-skeleton differences**. For §§4--7, the independent sequential comparison likewise found **0 differences across all 80 display skeletons**. In particular, the rebuild retains:

- all definitions, theorems, demonstrations, remarks, and supplements in §§1--3;
- proof components I--XI in §4;
- the complete theorem/corollary/remark apparatus of §§5--6;
- the editor's manuscript-lacuna note in §5.5;
- the centered `À partir d'ici, esquisse.` status marker at §6.3;
- all of §7 and the receipt date.

The dependency graph for `N43_fr.tex` and for `cum_fr_P43.tex` reports no missing inputs. The cumulative preamble and the standalone Paper 43 wrapper both define source-assigned footnote macros `\srcfn`, `\srcfnmark`, and `\srcfntext`.

## Standalone Paper 43 build and all-page visual QA

Wrapper: `working/r823_fr/tex/N43_fr.tex`  
Wrapper SHA-256: `99E4D72C785C3BA56AADA8929654B7D085CE6B65A6D2B9030FE5A591F5B34C40`

Build command:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=<workspace>/build/p43_r823_full N43_fr.tex
```

Outputs:

- `build/p43_r823_full/N43_fr.pdf`
  - 18 A4 pages; 392,703 bytes.
  - SHA-256 `99818A778AF6DA03AFDCF6E842D91E2CEE009D5B042E2234CA61A8A76125B3AF`.
- `build/p43_r823_full/N43_fr.log`
  - SHA-256 `5EF2FE418EE09E540B55E14BA62D58D8C73EC51A683D493B26421F24361CFE8F`.
  - Zero LaTeX/package warnings, box warnings, undefined references, errors, or fatal stops.

All 18 pages were rendered at 150 dpi to:

`tmp/pdfs/p43_r823_full_20260717/page-01.png` through `page-18.png`

They were inspected in nine two-page spreads. No clipping, overlap, malformed accents, mojibake, broken display, displaced footnote block, or missing structural marker was found. Page 18's lower white space is the expected result of the short closing §7 continuation and centered receipt date, not missing content.

## Integrated P1--43 cumulative build and spread QA

Production master:

`working/r823_fr/tex/cum_fr_P43.tex`

Checkpoint build:

- `build/cum_fr_P43_p43integration_20260717/cum_fr_P43.pdf`
  - 428 A4 pages; 2,646,722 bytes.
  - SHA-256 `3F9D9E0FD7DB0F4EA97D928787B5B4E06A4C09EEA3AC347458CE05B3FC911254`.
- `build/cum_fr_P43_p43integration_20260717/cum_fr_P43.log`
  - SHA-256 `EACE5E2C4115B800B55075C10C08C8CA3DEF77CBE7AD0036B439C2790040EAC7`.
  - Two-pass `latexmk` build completed without errors, box warnings, or undefined references.
  - The only diagnostics are the existing `rsfs` 7.5/3.75 pt font-size substitutions at master line 241, outside Paper 43.

Paper 43 occupies cumulative pages 411--428. All 18 cumulative pages were rendered at 150 dpi to `tmp/pdfs/cum_p43integration_pages411_428/`; representative opening, middle, and closing spreads (411--412, 419--420, 427--428) were inspected at original render resolution and are clean. The complete all-page standalone inspection above covers the same integrated dependency content at the same page breaks.

## Continuation cursor

Paper 43 is no longer a condensed translation-memory placeholder: it is the direct, full R823 French rebuild and passes source ratio, structure, mathematical-display, standalone build, cumulative build, and visual-QA gates. Subsequent P1--43 work can leave these two fragments untouched unless a specific source-level correction is identified.
