# -*- coding: utf-8 -*-
import fitz, PIL.Image as I
doc = fitz.open(r"C:\Users\Floris\Documents\Papors\OS\sga6.pdf")
p=doc[306]; r=p.rect; M=fitz.Matrix(450/72,450/72)
c=fitz.Rect(r.width*0.11, r.height*0.485, r.width*0.98, r.height*0.540)
pm=p.get_pixmap(matrix=M, clip=c)
I.frombytes("RGB",[pm.width,pm.height],pm.samples).save("_work/src/p300_disp3.png"); print("disp3", pm.width, pm.height)
