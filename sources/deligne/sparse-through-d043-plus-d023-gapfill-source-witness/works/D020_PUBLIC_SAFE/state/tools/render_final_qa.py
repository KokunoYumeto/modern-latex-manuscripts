#!/usr/bin/env python3
"""Render the exact final reader PDFs and make page-indexed QA contact sheets."""
import hashlib,json,pathlib,subprocess,sys
from PIL import Image,ImageOps,ImageDraw
from pypdf import PdfReader
root=pathlib.Path(sys.argv[1]).resolve()
out=root/'audit'/'native_reader_qa';out.mkdir(exist_ok=True)
inventory=[]
for layer in ('source_language','english_standalone','apparatus'):
    pdf=root/'readers'/'pdf'/f'{layer}.pdf'
    dest=out/layer;dest.mkdir(exist_ok=True)
    subprocess.run(['pdftoppm','-r','115','-png',str(pdf),str(dest/'page')],check=True)
    images=sorted(dest.glob('page-*.png'))
    assert len(images)==len(PdfReader(pdf).pages)
    inventory.append({'layer':layer,'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest().upper(),'pages':len(images),'rendered_png_sha256':[hashlib.sha256(p.read_bytes()).hexdigest().upper() for p in images]})
    for start in range(0,len(images),6):
        sheet=Image.new('RGB',(1500,1500),'#dadada');draw=ImageDraw.Draw(sheet)
        for idx,path in enumerate(images[start:start+6]):
            im=Image.open(path).convert('RGB');im.thumbnail((490,700))
            x=(idx%3)*500+(500-im.width)//2;y=(idx//3)*750+30
            sheet.paste(im,(x,y));draw.text(((idx%3)*500+12,(idx//3)*750+8),f'{layer} reader {start+idx+1}; authority {start+idx+(1 if layer=="apparatus" else 2)}',fill='black')
        sheet.save(dest/f'contact-{start+1:02d}-{min(start+6,len(images)):02d}.png')
(out/'RENDER_MANIFEST.json').write_text(json.dumps(inventory,indent=2)+'\n',encoding='utf-8')
print(json.dumps(inventory))
