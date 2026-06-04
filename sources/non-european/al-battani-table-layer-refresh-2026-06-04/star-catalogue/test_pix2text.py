#!/usr/bin/env python3
"""Smoke-test Pix2Text (existing OS tool) on a real math+Japanese page from the corpus."""
import fitz
import os
from PIL import Image
from pix2text import Pix2Text

PDF = os.environ.get("TEST_PDF", "sample_math_page.pdf")
OUT_DIR = os.environ.get("TEST_OUTPUT_DIR", ".")
d = fitz.open(PDF)
# pick a mid page likely to have equations
p = d[min(4, d.page_count-1)]
pix = p.get_pixmap(dpi=200); d.close()
os.makedirs(OUT_DIR, exist_ok=True)
img_path = os.path.join(OUT_DIR, "pix2text_smoke_page.png")
pix.save(img_path)
print("[p2t] loading models (first run downloads)...", flush=True)
p2t = Pix2Text.from_config(device="cpu")
try:
    res = p2t.recognize(img_path, return_text=True)
except TypeError:
    res = p2t.recognize(img_path)
out = res if isinstance(res, str) else str(res)
with open(os.path.join(OUT_DIR, "pix2text_out.md"), "w", encoding="utf-8") as f:
    f.write(out)
print("[p2t] done -> pix2text_out.md (chars:", len(out), ")")
