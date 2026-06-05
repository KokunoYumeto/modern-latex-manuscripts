#!/usr/bin/env python3
"""Parallelization + accuracy test: crop the Pisces sub-table from the HIGH-RES scan,
split into row-strips, batch them through a VLM (model from argv). Reports s/row, VRAM,
and the reads (UTF-8 file). Ground truth (my hand-read of these 7 Pisces rows):
 1 marbaṭ al-kattān N-leading   2 middle-of-three in cord   3 N of two in mouth of Fish
 4 N of three on tail tip       5 leading-of-three on spine 6 middle of them   7 hindmost of three
"""
import sys, time, torch, fitz
from PIL import Image
from transformers import AutoModelForImageTextToText, AutoProcessor
from qwen_vl_utils import process_vision_info

MODEL = sys.argv[1] if len(sys.argv) > 1 else "Qwen/Qwen2.5-VL-3B-Instruct"
N = 7

# crop the Pisces top sub-table straight from the scan at 600 dpi, split into N rows
d = fitz.open(r"albattani_work\source_scan\nallino_1899_albattanisivealb00batt.pdf")
p = d[20]; r = p.rect
band = fitz.Rect(r.x0, r.y0 + r.height*0.185, r.x1, r.y0 + r.height*0.415)
pix = p.get_pixmap(dpi=600, clip=band); d.close()
img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
W, H = img.size
strips = [img.crop((0, H*i//N, W, H*(i+1)//N)) for i in range(N)]

print(f"[load] {MODEL}", flush=True)
proc = AutoProcessor.from_pretrained(MODEL, max_pixels=1400*1400)
model = AutoModelForImageTextToText.from_pretrained(MODEL, torch_dtype=torch.bfloat16, device_map="auto")

P = ("This is ONE row of al-Battani's Arabic fixed-star table (1899 print). Left of the Arabic "
     "description are number columns, right-to-left: longitude (absolute ecliptic degrees 0-360 then "
     "minutes), latitude (degrees then minutes), direction (ش=north, ج=south), magnitude. Numbers are "
     "abjad letters: ا1 ب2 ج3 د4 ه5 و6 ز7 ح8 ط9 ي10 ك20 ل30 م40 ن50 س60 ع70 ف80 ص90 ق100 ر200 ش300 ت400; "
     "compound adds them (شلد=334). Read this row. Output exactly: DESC <arabic> | LON <number> | "
     "LAT <number> | DIR <N/S> | MAG <number>.")
msgs = [[{"role":"user","content":[{"type":"image","image":s},{"type":"text","text":P}]}] for s in strips]
texts = [proc.apply_chat_template(m, tokenize=False, add_generation_prompt=True) for m in msgs]
images = [process_vision_info(m)[0][0] for m in msgs]
inputs = proc(text=texts, images=images, padding=True, return_tensors="pt").to(model.device)

torch.cuda.reset_peak_memory_stats()
t0 = time.time()
with torch.no_grad():
    out = model.generate(**inputs, max_new_tokens=90, do_sample=False)
dt = time.time() - t0
trim = [o[len(i):] for i, o in zip(inputs.input_ids, out)]
res = proc.batch_decode(trim, skip_special_tokens=True)
summary = f"=== {MODEL}: {N} rows {dt:.1f}s = {dt/N:.2f}s/row | peak VRAM {torch.cuda.max_memory_allocated()/1e9:.1f} GB ==="
print(summary)
with open(r"albattani_work\rebuilt\vlm_batch_out.txt", "w", encoding="utf-8") as f:
    f.write(summary + "\n")
    for i, rr in enumerate(res, 1):
        f.write(f"row{i}: {' '.join(rr.split())[:240]}\n")
print("[written vlm_batch_out.txt]")
