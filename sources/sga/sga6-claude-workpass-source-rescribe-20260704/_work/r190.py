# -*- coding: utf-8 -*-
import fitz, PIL.Image as I
doc = fitz.open(r"C:\Users\Floris\Documents\Papors\OS\sga6.pdf")
for idx in (196,):
    page=doc[idx]; M=fitz.Matrix(200/72,200/72)
    pm=page.get_pixmap(matrix=M)
    I.frombytes("RGB",[pm.width,pm.height],pm.samples).save("_work/src/p190_idx%d.png"%idx)
    print("rendered idx", idx)
