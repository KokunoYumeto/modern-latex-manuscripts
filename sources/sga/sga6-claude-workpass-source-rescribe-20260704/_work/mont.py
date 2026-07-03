# -*- coding: utf-8 -*-
import fitz, PIL.Image as I
doc = fitz.open(r"C:\Users\Floris\Documents\Papors\OS\sga6.pdf")
idxs=list(range(62,74))
tiles=[]
for idx in idxs:
    page=doc[idx]; r=page.rect; M=fitz.Matrix(150/72,150/72)
    c=fitz.Rect(0, r.height*0.07, r.width, r.height*0.17)  # top header band
    pm=page.get_pixmap(matrix=M, clip=c)
    im=I.frombytes("RGB",[pm.width,pm.height],pm.samples)
    tiles.append((idx,im))
W=max(t[1].width for t in tiles); H=sum(t[1].height for t in tiles)
mont=I.new("RGB",(W,H),"white"); y=0
from PIL import ImageDraw
for idx,im in tiles:
    mont.paste(im,(0,y)); d=ImageDraw.Draw(mont); d.text((5,y+2),"idx%d/p%d"%(idx,idx-6),fill="red"); y+=im.height
mont.save("_work/src/mont_62_73.png"); print("montage", mont.width, mont.height)
