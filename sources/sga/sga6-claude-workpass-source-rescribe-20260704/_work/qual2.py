# -*- coding: utf-8 -*-
import fitz
for path,name in [(r"C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\SGA continuation 2\SGA6_repair033_codex_display_labels_20260621\external_witnesses\sga6_slmath_postscript_scan.pdf","slmath")]:
    try:
        doc=fitz.open(path); print(name,"pages",doc.page_count)
        for idx in (40,200,310):
            if idx<doc.page_count:
                page=doc[idx]; imgs=page.get_images(full=True)
                if imgs:
                    d=doc.extract_image(imgs[0][0]); dpi=round(d['width']/page.rect.width*72)
                    print("  idx%d: %dx%d %s ~%ddpi (page %.0fx%.0f)"%(idx,d['width'],d['height'],d['ext'],dpi,page.rect.width,page.rect.height))
                else:
                    print("  idx%d: no raster image (vector/text page?) rect %.0fx%.0f"%(idx,page.rect.width,page.rect.height))
    except Exception as e:
        print(name,"ERROR",e)
