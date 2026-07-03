# -*- coding: utf-8 -*-
import fitz, PIL.Image as I
doc = fitz.open(r"C:\Users\Floris\Documents\Papors\OS\sga6.pdf")
page=doc[35]; M=fitz.Matrix(150/72,150/72)
pm=page.get_pixmap(matrix=M)
I.frombytes("RGB",[pm.width,pm.height],pm.samples).save("_work/src/full_idx35.png")
print("full idx35", pm.width, pm.height)
