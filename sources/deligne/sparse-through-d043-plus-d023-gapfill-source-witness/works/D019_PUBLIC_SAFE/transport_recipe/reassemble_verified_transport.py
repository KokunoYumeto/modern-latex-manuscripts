"""Portable exact assembly from canonical PDFs and verified encoded streams.

Requires Python 3 and pypdf==6.12.2. Does not use old operational cursors,
private receipts, method01 inputs, Zopfli, TeX, or network services.
"""
import argparse, gc, hashlib, json, zlib
from pathlib import Path
import pypdf
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject

ROOT=Path(__file__).resolve().parent
WORK=ROOT.parent
def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest().upper()
def require(value,message):
    if not value:raise RuntimeError(message)
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output-dir',required=True,type=Path);args=parser.parse_args()
    require(pypdf.__version__=='6.12.2','Exact byte replay requires pypdf 6.12.2')
    target=args.output_dir.resolve()
    require(not target.exists(),'Use a new output directory; no existing bytes are overwritten')
    target.mkdir(parents=True)
    accepted=json.loads((WORK/'transport_evidence/TRANSPORT_RESULT.json').read_text(encoding='utf-8'))
    require(accepted['status']=='PASS','transport acceptance gate')
    require(digest(WORK/'receipts/D019_CANONICAL_FINAL_GATE.json')==accepted['content_gate_sha256'],'canonical gate binding')
    method=json.loads((ROOT/'method03_zopfli/METHOD_RECEIPT.json').read_text(encoding='utf-8'))
    records={r['pixel_sha256']:r for r in method['encoded_streams']}
    require(len(records)==144,'Complete stream cache required')
    output=[]
    for item in accepted['selected_pdfs']:
        original=WORK/'canonical_build/output/pdf'/Path(item['original']['path']).name
        require(original.stat().st_size==item['original']['bytes'] and digest(original)==item['original']['sha256'],'canonical PDF identity')
        reader=PdfReader(original);writer=PdfWriter(clone_from=reader);seen=[]
        for obj in writer._objects:
            if obj is None or not hasattr(obj,'get') or obj.get('/Subtype')!='/Image':continue
            require(str(obj.get('/ColorSpace'))=='/DeviceGray' and int(obj.get('/BitsPerComponent',0))==8 and '/SMask' not in obj and '/Mask' not in obj,'canonical image dictionary')
            raw=obj.get_data();key=hashlib.sha256(raw).hexdigest().upper();row=records[key]
            require(len(raw)==row['decoded_bytes'] and int(obj['/Width'])==row['width'] and int(obj['/Height'])==row['height'],'native image dimensions')
            stream=ROOT/'method03_zopfli'/row['path'];encoded=stream.read_bytes()
            require(stream.stat().st_size==row['bytes'] and digest(stream)==row['sha256'] and zlib.decompress(encoded)==raw,'encoded stream and exact pixels')
            obj._data=encoded
            if hasattr(obj,'decoded_self'):obj.decoded_self=None
            obj[NameObject('/Filter')]=NameObject('/FlateDecode');obj.pop('/DecodeParms',None);seen.append(key)
        require(len(seen)==144 and len(set(seen))==144,'all 144 unique images')
        out=target/Path(item['path']).name
        with out.open('wb') as f:writer.write(f)
        require(out.stat().st_size==item['bytes'] and digest(out)==item['sha256'],'assembled PDF must equal the accepted transport byte-for-byte')
        output.append({'filename':out.name,'bytes':out.stat().st_size,'sha256':digest(out),'status':'PASS'})
        del writer,reader,raw,encoded;gc.collect()
    receipt={'schema':'d019-portable-transport-assembly-v1','status':'PASS','pypdf_version':pypdf.__version__,'outputs':output,'compression_rerun':False,'canonical_inputs_modified':False}
    (target/'PORTABLE_ASSEMBLY_REPLAY.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
