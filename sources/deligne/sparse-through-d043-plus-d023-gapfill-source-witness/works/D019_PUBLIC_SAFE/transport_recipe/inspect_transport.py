"""Bounded native-PDF inspection; writes only the transport inspection receipt."""
from pathlib import Path
import hashlib,io,json,struct,zlib
from pypdf import PdfReader
from PIL import Image,features

ROOT=Path(__file__).resolve().parent
STAGE=ROOT.parent
def sha(data): return hashlib.sha256(data).hexdigest().upper()
def filehash(path):
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for data in iter(lambda:stream.read(1024*1024),b''):h.update(data)
    return h.hexdigest().upper()
def png_payload(image):
    b=io.BytesIO(); image.save(b,format='PNG',compress_level=9)
    data=b.getvalue(); offset=8; pieces=[]
    while offset<len(data):
        length=struct.unpack('>I',data[offset:offset+4])[0]; kind=data[offset+4:offset+8]
        if kind==b'IDAT': pieces.append(data[offset+8:offset+8+length])
        offset+=12+length
    return b''.join(pieces)
def images(reader):
    seen=set()
    for page_index,page in enumerate(reader.pages,1):
        for name,ref in page.get('/Resources',{}).get('/XObject',{}).items():
            obj=ref.get_object()
            key=(ref.idnum,ref.generation)
            if obj.get('/Subtype')=='/Image' and key not in seen:
                seen.add(key); yield page_index,name,obj
def main():
    cursor=json.loads((ROOT/'TRANSPORT_CURSOR.json').read_text(encoding='utf-8'))
    gate=STAGE/'receipts/D019_CANONICAL_FINAL_GATE.json'
    if filehash(gate)!=cursor['accepted_content_gate_sha256']:raise RuntimeError('accepted gate changed')
    manifest=json.loads((STAGE/'canonical_build/output/D019_CANONICAL_DELIVERY_MANIFEST.json').read_text(encoding='utf-8'))
    frozen=[]
    for item in manifest['files']:
        p=STAGE/item['path']
        actual={'path':item['path'],'bytes':p.stat().st_size,'sha256':filehash(p)}
        if actual!=item:raise RuntimeError('accepted gate-bound file mismatch '+item['path'])
        frozen.append(actual)
    docs=[]
    for row in cursor['original_pdfs']:
        p=(ROOT/row['path']).resolve()
        if filehash(p)!=row['sha256'] or p.stat().st_size!=row['bytes']:raise RuntimeError('original PDF mismatch')
        reader=PdfReader(p); info=[]
        for index,(page,name,obj) in enumerate(images(reader)):
            item={'first_page':page,'resource':str(name),'width':int(obj['/Width']),'height':int(obj['/Height']),
                'bits':int(obj['/BitsPerComponent']),'colorspace':str(obj['/ColorSpace']),'filter':str(obj.get('/Filter')),
                'predictor':str(obj.get('/DecodeParms')),'encoded_bytes':len(obj._data)}
            if index in (0,1,20,60,100,143):
                raw=obj.get_data(); image=Image.frombytes('L',(item['width'],item['height']),raw)
                item['decoded_bytes']=len(raw); item['pixels_sha256']=sha(raw)
                item['plain_zlib9_bytes']=len(zlib.compress(raw,9)); item['png_zlib9_bytes']=len(png_payload(image))
            info.append(item)
        docs.append({'path':row['path'],'bytes':p.stat().st_size,'sha256':row['sha256'],'pages':len(reader.pages),'images':info,
            'encoded_image_bytes':sum(x['encoded_bytes'] for x in info)})
    result={'schema':'d019_transport_inspection_v1','status':'PASS','accepted_gate_bound_files':frozen,'documents':docs,
        'available_lossless_jpeg2000':features.check('jpg_2000'),'openjpeg_version':features.version('jpg_2000')}
    (ROOT/'TRANSPORT_INSPECTION.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','accepted_files_verified':len(frozen),'documents':[{k:v for k,v in d.items() if k!='images'} for d in docs],
        'sample_sizes':[[{'original':i['encoded_bytes'],'zlib9':i['plain_zlib9_bytes'],'png9':i['png_zlib9_bytes']} for i in d['images'] if 'plain_zlib9_bytes' in i] for d in docs]}))
if __name__=='__main__':main()
