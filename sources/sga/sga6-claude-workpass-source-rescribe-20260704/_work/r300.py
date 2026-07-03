# -*- coding: utf-8 -*-
import fitz, PIL.Image as I
doc = fitz.open(r"C:\Users\Floris\Documents\Papors\OS\sga6.pdf")
page=doc[306]; M=fitz.Matrix(200/72,200/72); pm=page.get_pixmap(matrix=M)
I.frombytes("RGB",[pm.width,pm.height],pm.samples).save("_work/src/p300_idx306.png"); print("p300", pm.width, pm.height)
