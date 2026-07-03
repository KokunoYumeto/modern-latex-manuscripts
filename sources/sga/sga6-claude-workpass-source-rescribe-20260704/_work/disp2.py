# -*- coding: utf-8 -*-
import fitz, PIL.Image as I
doc = fitz.open(r"C:\Users\Floris\Documents\Papors\OS\sga6.pdf")
p=doc[306]; r=p.rect; M=fitz.Matrix(450/72,450/72)
c=fitz.Rect(r.width*0.11, r.height*0.435, r.width*0.97, r.height*0.492)
pm=p.get_pixmap(matrix=M, clip=c)
I.frombytes("RGB",[pm.width,pm.height],pm.samples).save("_work/src/p300_disp2.png"); print("disp2", pm.width, pm.height)
