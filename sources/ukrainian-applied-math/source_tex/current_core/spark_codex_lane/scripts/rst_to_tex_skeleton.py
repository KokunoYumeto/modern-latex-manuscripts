#!/usr/bin/env python3
"""Minimal RST/Markdown-to-TeX skeleton converter for human/model cleanup.
It intentionally does not try to be perfect; Spark can improve the output.
"""
from __future__ import annotations
import sys, pathlib, re

if len(sys.argv) != 3:
    print('usage: rst_to_tex_skeleton.py input.rst output.tex')
    raise SystemExit(2)

src = pathlib.Path(sys.argv[1])
dst = pathlib.Path(sys.argv[2])
text = src.read_text(errors='replace')
lines = text.splitlines()
out=[]
i=0
while i < len(lines):
    line=lines[i]
    # RST title underlines
    if i+1 < len(lines) and set(lines[i+1].strip()) in [set('#'), set('*'), set('='), set('-')]:
        underline=lines[i+1].strip()
        if underline and len(underline) >= max(3, len(line.strip())//2):
            level = underline[0]
            cmd = {'#':'chapter','*':'section','=':'subsection','-':'subsubsection'}.get(level,'section')
            out.append(f'\\{cmd}'+'{'+line.strip()+'}')
            i += 2
            continue
    if line.strip().startswith('.. image::'):
        out.append('% FIGURE TODO: '+line.strip())
        i += 1
        continue
    if line.startswith('```'):
        out.append('\\begin{lstlisting}')
        i += 1
        while i < len(lines) and not lines[i].startswith('```'):
            out.append(lines[i]); i += 1
        out.append('\\end{lstlisting}')
        i += 1
        continue
    # Escape only the most dangerous characters in plain prose, leave math-ish lines alone.
    out.append(line)
    i += 1

dst.write_text('\n'.join(out)+'\n')
print(f'wrote {dst}')
