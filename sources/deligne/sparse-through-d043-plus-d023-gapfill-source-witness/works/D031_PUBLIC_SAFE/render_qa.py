"""Read-only PDF structural checks plus deterministic QA rendering/contact sheets."""
from pathlib import Path
import argparse, hashlib, json, re, subprocess
import fitz
from PIL import Image, ImageDraw

BASE=Path(__file__).resolve().parent

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source',default='normalized');a=ap.parse_args()
    src=(BASE/a.source).resolve();assert src.is_relative_to(BASE)
    out=BASE/'qa_render'/a.source;out.mkdir(parents=True,exist_ok=True)
    result={}
    for name in ['french_diplomatic','english_translation','apparatus']:
        pdf=src/f'{name}.pdf';doc=fitz.open(pdf);findings=[];bodies=[]
        for i,page in enumerate(doc):
            text=page.get_text();bodies.append(text)
            footer=page.get_text(clip=fitz.Rect(0,800,page.rect.width,page.rect.height)).strip()
            if name!='apparatus' and footer!=str(i+247):findings.append(dict(page=i+1,wrong_footer=footer))
            blocks=page.get_text('dict')['blocks']
            for block in blocks:
                for line in block.get('lines',[]):
                    for span in line['spans']:
                        if span['text'].strip() and (span['bbox'][0]<20 or span['bbox'][2]>page.rect.width-20):
                            findings.append(dict(page=i+1,margin_outlier=span['bbox'],text=span['text']))
            pix=page.get_pixmap(matrix=fitz.Matrix(0.8,0.8),alpha=False)
            pix.save(out/f'{name}-{i+1:02}.png')
        if name!='apparatus' and len(doc)!=43:findings.append(dict(wrong_page_count=len(doc)))
        if '\\begin{' in '\n'.join(bodies) or '\\arrow[' in '\n'.join(bodies):findings.append(dict(raw_tex_visible=True))
        result[name]=dict(pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest().upper(),pages=len(doc),findings=findings,footers_checked=name!='apparatus',raster_images=sum(len(p.get_images()) for p in doc))
        for start in range(0,len(doc),6):
            sheet=Image.new('RGB',(1010,2180),'#dddddd');draw=ImageDraw.Draw(sheet)
            for off in range(min(6,len(doc)-start)):
                im=Image.open(out/f'{name}-{start+off+1:02}.png').convert('RGB');im.thumbnail((480,680))
                x=15+(off%2)*505;y=35+(off//2)*725
                sheet.paste(im,(x,y));draw.text((x,y-20),f'{name} PDF page {start+off+1}',fill='black')
            sheet.save(out/f'{name}-contact-{start//6+1:02}.png')
        (out/f'{name}.txt').write_text('\n\f\n'.join(bodies),encoding='utf-8')
    (out/'structural_qa.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
