# Independent build validation - SGA2-VIII-T21

Date: 2026-07-19  
Review state: independent bounded-unit build gate passed

The independently reviewed input was the exact final TeX, 2,885 bytes,
SHA-256 `56B4A0F8E1C7D8D2F88E70960AA0023BA50E7ADE43B9F6E69EC606B98B54EFB5`.
It was copied into a clean short-path build directory and compiled twice with
`pdflatex -interaction=nonstopmode -halt-on-error`.

- pass 1 exit: 0;
- pass 2 exit: 0;
- final error, warning, overfull, underfull, undefined-reference, and
  multiply-defined-reference diagnostic hits: 0;
- independently built PDF: 330,480 bytes, one unencrypted A4 page, SHA-256
  `83A8D763B5E30713E3700F88CFFD354559EB24336FF1045B41892B82FC6336DE`;
- frozen target PDF: 330,480 bytes, SHA-256
  `CE751502A12C33CD650460850B4C1F01C5134E7BAB3762BBA1BDE9149CF92EF6`;
- independent and frozen target extracted text: byte-identical, 1,954 bytes,
  SHA-256 `D51438E889850ACB3D63F0D92F62F263CD5876DDE8B45F5BD7367E1D25DDC619`;
- independent and frozen 300/600-dpi renders: byte-identical;
- extraction: zero forbidden control bytes and one normal form-feed byte;
- fonts: 26/26 reported rows embedded, subsetted, and Unicode mapped;
- named destinations independently present: `section.2`, `theorem.2.1`, and
  `equation.2.1` (as well as the three footnote and two item destinations).

The different whole-PDF hashes arise on a fresh build with new creation and
modification metadata. Text and rendered page identity establish content and
layout parity. `INDEPENDENT_BUILD_PASS1.log` and
`INDEPENDENT_BUILD_PASS2.log` are the complete compile logs with private
machine prefixes replaced by `<USER_HOME>`; the replacement changes evidence
paths only, not diagnostics or build content.

This is a clean independent build of one bounded English unit, not a cumulative
Exposé VIII or SGA 2 build.
