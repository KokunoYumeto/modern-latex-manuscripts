#!/usr/bin/env python3
"""Validate the abjad OCR on REAL 1899 print: crop page-20 Pisces longitude-degree cells,
preprocess to the training format, predict, compare to hand-read ground truth [11,11,13,11,6,7,8].
Saves the 7 cell crops + a composite so segmentation can be eyeballed."""
import os, fitz, numpy as np, torch, torch.nn as nn
from PIL import Image

GT = [11,11,13,11,6,7,8]   # hand-read longitude-degree column, Pisces p20
SCAN = r"albattani_work\source_scan\nallino_1899_albattanisivealb00batt.pdf"
OUT = r"albattani_work\rebuilt"

d = fitz.open(SCAN); p = d[20]; r = p.rect
# longitude-degree column = just left of the descriptions (~x 0.555-0.625), 7 rows in y 0.185-0.415
band = fitz.Rect(r.x0+r.width*0.400, r.y0+r.height*0.185, r.x0+r.width*0.448, r.y0+r.height*0.415)
pix = p.get_pixmap(dpi=400, clip=band); d.close()
img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples).convert("L")
W, Hh = img.size; N = 7
cells = [img.crop((0, Hh*i//N, W, Hh*(i+1)//N)) for i in range(N)]
# composite for visual check
comp = Image.new("L", (W, Hh + 6*4), 255)
for i, c in enumerate(cells): comp.paste(c, (0, Hh*i//N + i*4))
comp.save(os.path.join(OUT, "cells_long_composite.png"))

def prep(c):
    c = c.point(lambda v: 0 if v < 140 else 255)        # binarize
    bb = c.getbbox()
    if bb: c = c.crop(bb)
    cw, ch = c.size; sc = min(70/max(cw,1), 48/max(ch,1))
    c = c.resize((max(int(cw*sc),1), max(int(ch*sc),1)))
    canvas = Image.new("L", (96,64), 255); canvas.paste(c, ((96-c.size[0])//2,(64-c.size[1])//2))
    return np.array(canvas, dtype=np.float32)/255.0

class Net(nn.Module):
    def __init__(s):
        super().__init__()
        s.b=nn.Sequential(nn.Conv2d(1,32,3,1,1),nn.ReLU(),nn.MaxPool2d(2),
            nn.Conv2d(32,64,3,1,1),nn.ReLU(),nn.MaxPool2d(2),
            nn.Conv2d(64,128,3,1,1),nn.ReLU(),nn.AdaptiveAvgPool2d(4),nn.Flatten(),
            nn.Linear(128*16,256),nn.ReLU(),nn.Dropout(0.3))
        s.h=nn.Linear(256,10); s.t=nn.Linear(256,10); s.u=nn.Linear(256,10)
    def forward(s,x): z=s.b(x); return s.h(z),s.t(z),s.u(z)

mp = os.path.join(OUT,"abjad_cnn.pt")
if os.path.exists(mp):
    net=Net(); net.load_state_dict(torch.load(mp,map_location="cpu")); net.eval()
    X=torch.tensor(np.stack([prep(c) for c in cells])[:,None],dtype=torch.float32)
    with torch.no_grad():
        ph,pt,pu=net(X); pred=(100*ph.argmax(1)+10*pt.argmax(1)+pu.argmax(1)).tolist()
    ok=sum(int(a==b) for a,b in zip(pred,GT))
    print("pred:", pred); print("true:", GT); print(f"match {ok}/{N}")
else:
    print("model not trained yet; saved cell crops for visual check only")
