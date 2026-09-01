"""Verify/reassemble the exact D017 public provenance carrier from ordered chunks.

This program never calls Git, a network endpoint, or a cumulative builder.
With --output, the destination must not exist. Without --output, the complete
concatenated byte stream is verified without creating a duplicate carrier.
"""
import argparse,hashlib,json
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--manifest',type=Path,default=Path(__file__).parent/'D017/provenance/CHUNK_MANIFEST.json')
    ap.add_argument('--reference',type=Path)
    ap.add_argument('--output',type=Path)
    a=ap.parse_args()
    m=json.loads(a.manifest.read_text(encoding='utf-8'))
    root=a.manifest.resolve().parent
    reference=a.reference.open('rb') if a.reference else None
    output=None
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        output=a.output.open('xb')
    overall=hashlib.sha256()
    count=0
    rows=[]
    try:
        for row in m['chunks']:
            assert row['offset']==count
            path=(root/row['path']).resolve()
            assert path.is_relative_to(root)
            h=hashlib.sha256()
            size=0
            with path.open('rb') as f:
                while block:=f.read(1024*1024):
                    if reference:assert reference.read(len(block))==block,('reference byte mismatch',row['path'],size)
                    if output:output.write(block)
                    overall.update(block);h.update(block);size+=len(block);count+=len(block)
            assert size==row['bytes'] and h.hexdigest().upper()==row['sha256'],row['path']
            rows.append({'path':row['path'],'bytes':size,'sha256':h.hexdigest().upper()})
        if reference:assert reference.read(1)==b''
        assert count==m['carrier']['bytes'] and overall.hexdigest().upper()==m['carrier']['sha256']
    finally:
        if reference:reference.close()
        if output:output.close()
    print(json.dumps({'status':'PASS','carrier_bytes':count,'carrier_sha256':overall.hexdigest().upper(),
                      'all_chunk_hashes_verified':True,'byte_for_byte_reference_comparison':bool(a.reference),
                      'entire_reassembled_stream_verified':True,'chunks':rows},sort_keys=True))

if __name__=='__main__':main()
