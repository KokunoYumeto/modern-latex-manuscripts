"""Independent D019 inserted-glyph and native-image placement verification."""
import hashlib, importlib.util, json, re
from pathlib import Path
import fitz

path=Path(__file__).with_name('build_d019_integration.py')
spec=importlib.util.spec_from_file_location('builder',path);b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)

def chars(page):
    out=[]
    for block in page.get_text('rawdict')['blocks']:
        if block['type']!=0:continue
        for line in block['lines']:
            for span in line['spans']:
                for c in span['chars']:out.append((c['c'],c['bbox']))
    return out

def images(page):
    return [{k:i[k] for k in ('bbox','width','height','colorspace','bpc','digest')} for i in page.get_image_info(hashes=True)]

def main():
    result={'schema':'d019-inserted-native-image-glyph-geometry-v1','status':'RUNNING','languages':{},'maximum_position_tolerance_points':0.1}
    detail=[]
    for lang in ('EN','FR'):
        pdf=b.SOURCE/f'Deligne_{lang}.pdf'
        part=next(p for p in b.includes(b.SOURCE,lang,pdf) if p['work']=='D019')
        glyphs=im_count=0;maximum=0
        with fitz.open(pdf) as current,fitz.open(b.SOURCE/part['path']) as source:
            for offset in range(part['pages']):
                page=current[part['first']+offset-1];ref=source[offset]
                a,c=chars(page),chars(ref)
                if len(a)!=len(c):raise b.Failure(f'{lang} glyph count mismatch {offset+1}')
                deviation=0
                for ca,cc in zip(a,c):
                    if ca[0]!=cc[0]:raise b.Failure(f'{lang} glyph sequence mismatch {offset+1}')
                    deviation=max(deviation,max(abs(x-y) for x,y in zip(ca[1],cc[1])))
                pi,si=images(page),images(ref)
                if len(pi)!=len(si):raise b.Failure('native image count mismatch')
                for x,y in zip(pi,si):
                    if any(x[k]!=y[k] for k in ('width','height','colorspace','bpc','digest')):raise b.Failure('native image samples or dictionary mismatch')
                    deviation=max(deviation,max(abs(i-j) for i,j in zip(x['bbox'],y['bbox'])))
                if deviation>0.1:raise b.Failure(f'inserted geometry changes {lang} {offset+1}: {deviation}')
                glyphs+=len(a);im_count+=len(pi);maximum=max(maximum,deviation)
                detail.append({'language':lang,'standalone_page':offset+1,'cumulative_page':part['first']+offset,'glyphs':len(a),'native_images':len(pi),'maximum_coordinate_deviation_points':round(deviation,8),'status':'PASS'})
        if im_count!=144:raise b.Failure('not all 144 D019 presentation images verified')
        result['languages'][lang]={'pages':part['pages'],'glyphs':glyphs,'native_images':im_count,'maximum_coordinate_deviation_points':maximum,'pdf':b.sha(pdf),'standalone':b.sha(b.SOURCE/part['path'])}
    result.update(status='PASS',page_details=b.tsv(b.AUDIT/'D019_INSERTED_GLYPH_IMAGE_GEOMETRY.tsv',detail),all_native_image_pixels_exact=True,all_glyph_sequences_exact=True)
    b.write(b.AUDIT/'D019_INSERTED_GLYPH_IMAGE_GEOMETRY.json',result)
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
