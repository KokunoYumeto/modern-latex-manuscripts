"""Nonpatching PDF comparison; all receipts/renders stay in transport_derivatives."""
from pathlib import Path
import argparse,hashlib,io,json,shutil,subprocess
from PIL import Image
from pypdf import PdfReader
from pypdf.generic import StreamObject,DictionaryObject,ArrayObject,IndirectObject
from inspect_transport import filehash

ROOT=Path(__file__).resolve().parent
STAGE=ROOT.parent
def digest(data):return hashlib.sha256(data).hexdigest().upper()
def dump(path,value):path.write_text(json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
def canonical(value,stack=None):
    stack=set() if stack is None else stack
    if isinstance(value,IndirectObject):
        key=(id(value.pdf),value.idnum,value.generation)
        if key in stack:return {'cycle':True}
        return canonical(value.get_object(),stack|{key})
    if isinstance(value,StreamObject):
        return {'decoded_stream_sha256':digest(value.get_data()),'decoded_stream_bytes':len(value.get_data()),
            'dictionary':{str(k):canonical(v,stack) for k,v in sorted(value.items()) if k not in ('/Length','/Filter','/DecodeParms')}}
    if isinstance(value,DictionaryObject):return {str(k):canonical(v,stack) for k,v in sorted(value.items())}
    if isinstance(value,(ArrayObject,list,tuple)):return [canonical(v,stack) for v in value]
    if isinstance(value,bytes):return {'bytes_sha256':digest(value),'length':len(value)}
    if isinstance(value,(str,int,float,bool)) or value is None:return value
    return str(value)
def canonical_sha(value):return digest(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8'))
def decoded_image(obj):
    if str(obj.get('/ColorSpace'))!='/DeviceGray' or int(obj.get('/BitsPerComponent',0))!=8:raise RuntimeError('unexpected image properties')
    size=(int(obj['/Width']),int(obj['/Height']))
    if str(obj.get('/Filter'))=='/JPXDecode':
        with Image.open(io.BytesIO(obj._data)) as im:
            if im.mode!='L' or im.size!=size:raise RuntimeError('JPEG2000 pixel mode/dimensions')
            data=im.tobytes()
    elif str(obj.get('/Filter'))=='/FlateDecode':
        data=obj.get_data()
        if hasattr(obj,'decoded_self'):obj.decoded_self=None
    else:raise RuntimeError('unexpected image filter')
    if len(data)!=size[0]*size[1]:raise RuntimeError('image decoded byte count')
    return data
def fonts(page):return {str(k):canonical(v) for k,v in sorted(page['/Resources'].get('/Font',{}).items())}
def outline(reader):
    def walk(items):
        out=[]
        for item in items:
            if isinstance(item,list):out.append(walk(item))
            else:out.append({'title':str(item.title),'page':reader.get_destination_page_number(item),'type':str(item.typ),
                'left':str(item.left),'top':str(item.top),'zoom':str(item.zoom)})
        return out
    return walk(reader.outline)
def compare_structure(original,candidate):
    a,b=PdfReader(original),PdfReader(candidate)
    if len(a.pages)!=len(b.pages):raise RuntimeError('page count changed')
    if dict(a.metadata or {})!=dict(b.metadata or {}):raise RuntimeError('document metadata changed')
    if outline(a)!=outline(b):raise RuntimeError('outline changed')
    pages=[];image_count=0;unique_pixels=set();font_set=set()
    for n,(x,y) in enumerate(zip(a.pages,b.pages),1):
        geometry={key:(canonical(x.get(key)),canonical(y.get(key))) for key in ['/MediaBox','/CropBox','/BleedBox','/TrimBox','/ArtBox','/Rotate','/UserUnit']}
        if any(v[0]!=v[1] for v in geometry.values()):raise RuntimeError('page geometry changed '+str(n))
        cx,cy=x.get_contents().get_data(),y.get_contents().get_data()
        if cx!=cy:raise RuntimeError('decoded page content changed '+str(n))
        fx,fy=fonts(x),fonts(y)
        if fx!=fy:raise RuntimeError('font dictionaries or embedded content changed '+str(n))
        fontsha=canonical_sha(fx);font_set.add(fontsha)
        ax=x['/Resources'].get('/XObject',{});ay=y['/Resources'].get('/XObject',{})
        if set(ax)!=set(ay):raise RuntimeError('XObject resource routes changed')
        image_rows=[]
        for name in sorted(ax):
            imx,imy=ax[name].get_object(),ay[name].get_object()
            if imx.get('/Subtype')!='/Image' or imy.get('/Subtype')!='/Image':raise RuntimeError('unexpected non-image XObject')
            dx={str(k):canonical(v) for k,v in imx.items() if k not in ('/Length','/Filter','/DecodeParms')}
            dy={str(k):canonical(v) for k,v in imy.items() if k not in ('/Length','/Filter','/DecodeParms')}
            if dx!=dy:raise RuntimeError('image dictionary changed outside compression')
            px,py=decoded_image(imx),decoded_image(imy)
            if px!=py:raise RuntimeError('native image pixels changed '+str(n)+' '+str(name))
            pixelsha=digest(px);unique_pixels.add(pixelsha);image_count+=1
            image_rows.append({'resource':str(name),'pixel_bytes':len(px),'pixel_sha256':pixelsha,'unchanged_image_dictionary_sha256':canonical_sha(dx)})
        pages.append({'page':n,'decoded_content_sha256':digest(cx),'font_content_and_dictionary_sha256':fontsha,'geometry_sha256':canonical_sha({k:v[0] for k,v in geometry.items()}),'images':image_rows})
    if image_count!=144 or len(unique_pixels)!=144:raise RuntimeError('144 image identity coverage')
    return {'status':'PASS','pages':pages,'page_count':len(pages),'image_resource_placements':image_count,'unique_image_pixel_identities':len(unique_pixels),
        'font_resource_configurations':len(font_set),'outline_entries_sha256':canonical_sha(outline(a)),'metadata_sha256':canonical_sha(dict(a.metadata or {})),
        'all_page_content_geometry_font_and_image_pixels_equal':True}
def render(tool,pdf,target,pages):
    target.mkdir(parents=True,exist_ok=True)
    marker=target/'RENDER_INPUT.json'; expected={'pdf_sha256':filehash(pdf),'dpi':200,'pages':pages,'renderer_sha256':filehash(tool)}
    if marker.exists():
        if json.loads(marker.read_text(encoding='utf-8'))!=expected:raise RuntimeError('existing render provenance mismatch')
    else:
        if list(target.glob('*.png')):raise RuntimeError('unproven existing partial render set')
        subprocess.run([str(tool),'-r','200','-png',str(pdf),str(target/'page')],check=True)
        dump(marker,expected)
    images=sorted(target.glob('page-*.png'))
    if len(images)!=pages:raise RuntimeError('render page count')
    return images
def accepted_inputs_unchanged():
    baseline=json.loads((ROOT/'TRANSPORT_INSPECTION.json').read_text(encoding='utf-8'))['accepted_gate_bound_files']
    for item in baseline:
        p=STAGE/item['path']
        if filehash(p)!=item['sha256'] or p.stat().st_size!=item['bytes']:raise RuntimeError('accepted gate-bound file changed '+item['path'])
    return baseline
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--method',type=int,choices=[1,2],required=True);args=parser.parse_args()
    folder=ROOT/('method01_flate' if args.method==1 else 'method02_reversible_jpx')
    receipt=json.loads((folder/'METHOD_RECEIPT.json').read_text(encoding='utf-8'))
    original_baseline=accepted_inputs_unchanged()
    renderer=Path(shutil.which('pdftoppm')).resolve();extractor=renderer.parent/'pdftotext.exe'
    if not extractor.exists():
        located=shutil.which('pdftotext')
        if not located:raise RuntimeError('installed text extractor missing')
        extractor=Path(located).resolve()
    docs=[]
    for row in receipt['documents']:
        original=(ROOT/row['original']['path']).resolve();candidate=ROOT/row['path'];stem=candidate.stem
        if filehash(candidate)!=row['sha256']:raise RuntimeError('candidate changed after compression')
        structure=compare_structure(original,candidate);dump(folder/(stem+'_STRUCTURAL_IDENTITY.json'),structure)
        print(json.dumps({'method':args.method,'document':stem,'structural_identity':'PASS'}),flush=True)
        before_text=folder/(stem+'_ORIGINAL.txt');after_text=folder/(stem+'_TRANSPORT.txt')
        for pdf,target in [(original,before_text),(candidate,after_text)]:subprocess.run([str(extractor),'-layout',str(pdf),str(target)],check=True)
        if before_text.read_bytes()!=after_text.read_bytes():raise RuntimeError('extracted text differs')
        before_images=render(renderer,original,ROOT/'original_renders_200dpi'/original.stem,row['pages'])
        after_images=render(renderer,candidate,folder/'renders_200dpi'/stem,row['pages'])
        renders=[]
        for number,(x,y) in enumerate(zip(before_images,after_images),1):
            with Image.open(x) as a,Image.open(y) as b:
                if a.mode!=b.mode or a.size!=b.size or a.tobytes()!=b.tobytes():raise RuntimeError('200dpi rendered pixels differ at page '+str(number))
                rastersha=digest(a.tobytes());dims=list(a.size)
            renders.append({'page':number,'dimensions':dims,'pixel_sha256':rastersha,'original_png_sha256':filehash(x),'transport_png_sha256':filehash(y),
                'png_bytes_identical':x.read_bytes()==y.read_bytes()})
        result={**{k:v for k,v in row.items() if k!='image_streams'},'lossless_verification':'PASS','native_pixel_font_content_geometry_equal':True,
            'exact_extracted_text_sha256':filehash(before_text),'extracted_text_bytes':before_text.stat().st_size,
            'structural_identity_receipt':(folder/(stem+'_STRUCTURAL_IDENTITY.json')).relative_to(ROOT).as_posix(),'structural_identity_sha256':filehash(folder/(stem+'_STRUCTURAL_IDENTITY.json')),
            'raster_comparison_dpi':200,'all_page_raster_pixels_equal':True,'all_page_png_bytes_equal':all(x['png_bytes_identical'] for x in renders),'renders':renders}
        docs.append(result);dump(folder/'LOSSLESS_VERIFICATION.json',{'schema':'d019_lossless_transport_verification_v1','status':'IN_PROGRESS','documents':docs})
        print(json.dumps({'method':args.method,'document':stem,'all_pages_200dpi_equal':True,'bytes':row['bytes'],'below_limit':row['below_100000000_bytes']}),flush=True)
    accepted_inputs_unchanged()
    final={'schema':'d019_lossless_transport_verification_v1','status':'PASS','method':args.method,'documents':docs,
        'both_below_100000000_bytes':all(x['below_100000000_bytes'] for x in docs),'accepted_gate_bound_files_unchanged':original_baseline,
        'tools':{'renderer':renderer.name,'renderer_sha256':filehash(renderer),'extractor':extractor.name,'extractor_sha256':filehash(extractor)},
        'content_gate_unchanged':True,'transport_finding':'BOTH_PDFS_BELOW_LIMIT' if all(x['below_100000000_bytes'] for x in docs) else 'LOSSLESS_PDFS_REMAIN_ABOVE_TRANSPORT_LIMIT'}
    dump(folder/'LOSSLESS_VERIFICATION.json',final)
    cursor=json.loads((ROOT/'TRANSPORT_CURSOR.json').read_text(encoding='utf-8'))
    for run in cursor['method_runs']:
        if run['method']==args.method:run['verification']='PASS';run['both_below_limit']=final['both_below_100000000_bytes'];run['verification_receipt']=(folder/'LOSSLESS_VERIFICATION.json').relative_to(ROOT).as_posix()
    cursor['status']='COMPLETE' if final['both_below_100000000_bytes'] or args.method==2 else 'IN_PROGRESS_SECOND_METHOD'
    cursor['next_action']='Report exact lossless transport finding to parent; content gate unchanged.' if cursor['status']=='COMPLETE' else 'Run method2 once, then its same full lossless verification; no content edits.'
    if any(run['method']!=args.method and run['status']=='RUNNING' for run in cursor['method_runs']):
        cursor['status']='IN_PROGRESS_COMPRESSION'
        cursor['next_action']='Poll already running second and final compression method; do not duplicate it.'
    dump(ROOT/'TRANSPORT_CURSOR.json',cursor)
    print(json.dumps({'status':'PASS','method':args.method,'transport_finding':final['transport_finding'],'verification_receipt_sha256':filehash(folder/'LOSSLESS_VERIFICATION.json')}),flush=True)
if __name__=='__main__':main()
