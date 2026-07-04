# -*- coding: utf-8 -*-
import fitz, PIL.Image as I
doc = fitz.open(r"C:\Users\Floris\Documents\Papors\OS\sga6.pdf")
p=doc[196]; r=p.rect; M=fitz.Matrix(700/72,700/72)
# (**) RHS "==> R^? Q(E)" ~ y 0.283-0.330, x 0.58-0.88
c=fitz.Rect(r.width*0.58, r.height*0.283, r.width*0.90, r.height*0.332)
pm=p.get_pixmap(matrix=M, clip=c)
I.frombytes("RGB",[pm.width,pm.height],pm.samples).save("_work/src/p190_abut2.png"); print("abut2", pm.width, pm.height)
