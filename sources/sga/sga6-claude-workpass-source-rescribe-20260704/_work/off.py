# -*- coding: utf-8 -*-
import fitz, PIL.Image as I
doc = fitz.open(r"C:\Users\Floris\Documents\Papors\OS\sga6.pdf")
print("TOTAL PDF PAGES", doc.page_count)
for idx in (25,35,45):
    page=doc[idx]; M=fitz.Matrix(150/72,150/72)
    # top band to catch the printed page number
    r=page.rect; c=fitz.Rect(0, 0, r.width, r.height*0.10)
    pm=page.get_pixmap(matrix=M, clip=c)
    I.frombytes("RGB",[pm.width,pm.height],pm.samples).save("_work/src/off_idx%d.png"%idx)
    print("rendered idx", idx)
