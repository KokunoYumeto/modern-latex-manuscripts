# -*- coding: utf-8 -*-
import fitz
doc=fitz.open(r"C:\Users\Floris\Documents\Papors\OS\sga6.pdf")
print("pages", doc.page_count)
for idx in (35,196,306):
    page=doc[idx]; imgs=page.get_images(full=True)
    print("idx%d: %d images"%(idx,len(imgs)))
    for im in imgs[:3]:
        xref=im[0]; d=doc.extract_image(xref)
        print("   xref%d %dx%d %s %dbpc %s"%(xref,d['width'],d['height'],d['ext'],d.get('bpc',0),d.get('colorspace','')))
    print("   page rect", page.rect.width, page.rect.height, "-> native dpi ~", round(imgs and doc.extract_image(imgs[0][0])['width']/page.rect.width*72))
