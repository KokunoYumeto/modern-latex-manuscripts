# -*- coding: utf-8 -*-
import fitz, PIL.Image as I
doc = fitz.open(r"C:\Users\Floris\Documents\Papors\OS\sga6.pdf")
# p189 = idx 195, full page (bottom half where the sentence ends before p190's "ainsi d'ailleurs que")
page=doc[195]; M=fitz.Matrix(200/72,200/72); pm=page.get_pixmap(matrix=M)
I.frombytes("RGB",[pm.width,pm.height],pm.samples).save("_work/src/p189_idx195.png"); print("p189 full", pm.width, pm.height)
# p190 abutment (**) superscript crop, 700dpi, ~ y 0.345-0.395
p=doc[196]; r=p.rect; M2=fitz.Matrix(700/72,700/72)
c=fitz.Rect(r.width*0.52, r.height*0.345, r.width*0.82, r.height*0.395)
pm2=p.get_pixmap(matrix=M2, clip=c)
I.frombytes("RGB",[pm2.width,pm2.height],pm2.samples).save("_work/src/p190_abut.png"); print("abut", pm2.width, pm2.height)
