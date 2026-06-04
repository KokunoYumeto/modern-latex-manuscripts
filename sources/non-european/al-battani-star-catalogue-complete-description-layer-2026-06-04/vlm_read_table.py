#!/usr/bin/env python3
"""First-pass VLM reader for al-Battani abjad star-table pages (RTX 4080 SUPER).
Usage: python vlm_read_table.py <image.png> [model]
Default model Qwen2-VL-2B-Instruct (safe on 16GB); pass Qwen/Qwen2-VL-7B-Instruct to upgrade.
Output is a draft CSV that a human/Claude verifies — NOT trusted blind.
"""
import sys, torch
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
from qwen_vl_utils import process_vision_info

img = sys.argv[1]
MODEL = sys.argv[2] if len(sys.argv) > 2 else "Qwen/Qwen2-VL-2B-Instruct"

PROMPT = (
 "This image is one constellation block from al-Battani's Arabic star catalogue (Nallino 1899 print). "
 "It is a table. Reading RIGHT-TO-LEFT the columns are: "
 "(1) star description in Arabic; "
 "(2) longitude (الطول) in abjad numerals as ABSOLUTE ecliptic degrees 0-360, then minutes; "
 "(3) latitude (العرض) in abjad: degrees then minutes; "
 "(4) direction (علامات الجهة): ش = north, ج = south; "
 "(5) magnitude (مراتب العظمة) as a small number. "
 "Abjad values: ا1 ب2 ج3 د4 ه5 و6 ز7 ح8 ط9 ي10 ك20 ل30 م40 ن50 س60 ع70 ف80 ص90 ق100 ر200 ش300 ت400 ث500. "
 "Compound numbers add letters (شلد = 300+30+4 = 334). Watch the dots: ش(300, three dots) vs س(60, none); "
 "ب/ت/ث/ن/ي share a skeleton and differ only by dots. "
 "Transcribe EVERY row. For each star output one line: "
 "description ~ long_abjad=long_number ~ lat_abjad=lat_number ~ direction ~ magnitude. "
 "Output ONLY the rows, one per star."
)

print(f"[vlm] loading {MODEL} ...", flush=True)
model = Qwen2VLForConditionalGeneration.from_pretrained(MODEL, torch_dtype=torch.bfloat16, device_map="auto")
proc = AutoProcessor.from_pretrained(MODEL)
messages = [{"role":"user","content":[{"type":"image","image":img},{"type":"text","text":PROMPT}]}]
text = proc.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
imgs, vids = process_vision_info(messages)
inputs = proc(text=[text], images=imgs, videos=vids, padding=True, return_tensors="pt").to("cuda")
with torch.no_grad():
    out = model.generate(**inputs, max_new_tokens=1200, do_sample=False)
trimmed = [o[len(i):] for i, o in zip(inputs.input_ids, out)]
print("=== VLM OUTPUT ===", flush=True)
print(proc.batch_decode(trimmed, skip_special_tokens=True)[0])
