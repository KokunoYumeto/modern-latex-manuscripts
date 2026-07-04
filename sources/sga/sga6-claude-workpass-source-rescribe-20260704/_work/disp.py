# -*- coding: utf-8 -*-
import fitz, PIL.Image as I
doc = fitz.open(r"C:\Users\Floris\Documents\Papors\OS\sga6.pdf")
p=doc[306]; r=p.rect; M=fitz.Matrix(500/72,500/72)
c=fitz.Rect(r.width*0.12, r.height*0.545, r.width*0.96, r.height*0.605)  # the H(K[X])≃... display
pm=p.get_pixmap(matrix=M, clip=c)
I.frombytes("RGB",[pm.width,pm.height],pm.samples).save("_work/src/p300_disp.png"); print("disp", pm.width, pm.height)
