#!/usr/bin/env python3
import argparse, pathlib, subprocess, re
p=argparse.ArgumentParser(); p.add_argument("tex"); p.add_argument("--passes",type=int,default=2)
a=p.parse_args(); tex=pathlib.Path(a.tex)
for i in range(a.passes):
    proc=subprocess.run(["pdflatex","-interaction=nonstopmode","-halt-on-error",tex.name],cwd=tex.parent,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    out=proc.stdout.decode("utf-8","replace"); (tex.parent/f"{tex.stem}_pdflatex_{i+1}.log").write_text(out)
    if proc.returncode: raise SystemExit(out[-3000:])
log=(tex.parent/f"{tex.stem}.log").read_text(errors="replace") if (tex.parent/f"{tex.stem}.log").exists() else ""
for pat in ["Overfull", "LaTeX Warning", "Undefined references"]:
    if re.search(pat,log): print("WARN",pat)
