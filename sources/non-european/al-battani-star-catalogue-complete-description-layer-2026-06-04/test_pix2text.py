#!/usr/bin/env python3
"""Smoke-test Pix2Text (existing OS tool) on a real math+Japanese page from the corpus."""
import fitz
from PIL import Image
from pix2text import Pix2Text

PDF = r"C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\4\translations\japanese\pdf\Noether_Paper02_chunk04_JA_sections_18_26_tables.pdf"
d = fitz.open(PDF)
# pick a mid page likely to have equations
p = d[min(4, d.page_count-1)]
pix = p.get_pixmap(dpi=200); d.close()
img_path = r"albattani_work\rebuilt\noether_math_page.png"
pix.save(img_path)
print("[p2t] loading models (first run downloads)...", flush=True)
p2t = Pix2Text.from_config(device="cpu")
try:
    res = p2t.recognize(img_path, return_text=True)
except TypeError:
    res = p2t.recognize(img_path)
out = res if isinstance(res, str) else str(res)
with open(r"albattani_work\rebuilt\pix2text_out.md", "w", encoding="utf-8") as f:
    f.write(out)
print("[p2t] done -> pix2text_out.md (chars:", len(out), ")")
