#!/usr/bin/env python3
"""Test: ask the VLM to OCR the RAW Arabic letters in each numeric cell (its strength),
NOT to convert to numbers (its weakness). Abjad->number is done in code afterwards.
Crops the number columns only (left part of each row; description is on the right)."""
import sys, time, torch, fitz
from PIL import Image
from transformers import AutoModelForImageTextToText, AutoProcessor
from qwen_vl_utils import process_vision_info

MODEL = sys.argv[1] if len(sys.argv) > 1 else "Qwen/Qwen2.5-VL-3B-Instruct"
N = 7
d = fitz.open(r"albattani_work\source_scan\nallino_1899_albattanisivealb00batt.pdf")
p = d[20]; r = p.rect
band = fitz.Rect(r.x0, r.y0 + r.height*0.185, r.x1, r.y0 + r.height*0.415)
pix = p.get_pixmap(dpi=600, clip=band); d.close()
img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples); W, H = img.size
# number columns = left ~62% (rightmost ~38% is the Arabic description)
strips = [img.crop((0, H*i//N, int(W*0.62), H*(i+1)//N)) for i in range(N)]

proc = AutoProcessor.from_pretrained(MODEL, max_pixels=1600*1600)
model = AutoModelForImageTextToText.from_pretrained(MODEL, torch_dtype=torch.bfloat16, device_map="auto")
P = ("This image is the numeric portion of one row of an old Arabic table. It contains several small "
     "cells, each holding one or two Arabic letters. Transcribe the Arabic letters in each cell, going "
     "left to right, separating cells with ' | '. Output ONLY the Arabic letters cell by cell. "
     "Do NOT translate, do NOT convert to digits, do NOT add any words.")
msgs = [[{"role":"user","content":[{"type":"image","image":s},{"type":"text","text":P}]}] for s in strips]
texts = [proc.apply_chat_template(m, tokenize=False, add_generation_prompt=True) for m in msgs]
images = [process_vision_info(m)[0][0] for m in msgs]
inputs = proc(text=texts, images=images, padding=True, return_tensors="pt").to(model.device)
t0 = time.time()
with torch.no_grad():
    out = model.generate(**inputs, max_new_tokens=60, do_sample=False)
dt = time.time() - t0
trim = [o[len(i):] for i, o in zip(inputs.input_ids, out)]
res = proc.batch_decode(trim, skip_special_tokens=True)
with open(r"albattani_work\rebuilt\vlm_ocr_out.txt", "w", encoding="utf-8") as f:
    f.write(f"{MODEL} letter-OCR, {N} rows {dt:.1f}s\n")
    for i, rr in enumerate(res, 1):
        f.write(f"row{i}: {' '.join(rr.split())[:120]}\n")
print(f"done {dt:.1f}s -> vlm_ocr_out.txt")
