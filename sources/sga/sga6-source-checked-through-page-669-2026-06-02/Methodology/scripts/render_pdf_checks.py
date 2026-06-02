#!/usr/bin/env python3
import argparse, pathlib, fitz
p=argparse.ArgumentParser(); p.add_argument("pdf"); p.add_argument("outdir"); p.add_argument("--zoom",type=float,default=1.5)
a=p.parse_args(); out=pathlib.Path(a.outdir); out.mkdir(parents=True,exist_ok=True); d=fitz.open(a.pdf)
for i in range(d.page_count):
    pix=d.load_page(i).get_pixmap(matrix=fitz.Matrix(a.zoom,a.zoom),alpha=False); pix.save(out/f"page-{i+1:03d}.png")
print(d.page_count)
