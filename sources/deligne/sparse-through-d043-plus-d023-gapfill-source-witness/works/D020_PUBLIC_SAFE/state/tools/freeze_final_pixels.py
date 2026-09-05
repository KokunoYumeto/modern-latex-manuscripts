#!/usr/bin/env python3
"""Freeze exact current TIFF artifacts plus serialization-independent pixels."""
import csv,hashlib,io,json,pathlib,sys
from pypdf import PdfReader
from PIL import Image
root=pathlib.Path(sys.argv[1]).resolve()
def canonical(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def sha(x):return hashlib.sha256(x).hexdigest().upper()
auth=root/'source/20_AUTHORITY_DELIGNE_D020_WEIL_I_NUMDAM_36PP.pdf'
assert sha(auth.read_bytes())=='8392B345D4854E6DC55FB42CFC0B616D941935983723627237239A87348F42E5'
pdf=PdfReader(auth);p=root/'edition/source_language.ndjson';records=[json.loads(x) for x in p.read_text(encoding='utf-8').splitlines()]
folder=root/'control/authority_native_final';assert not folder.exists();folder.mkdir()
rows=[]
for r,page in zip(records,pdf.pages):
    assert sha(page.get_contents().get_data())==r['provenance']['content_stream_sha256']
    if r['physical_page']==1:assert not page.images;continue
    assert len(page.images)==1;item=page.images[0];data=item.data
    im=Image.open(io.BytesIO(data));pixelsha=sha(im.tobytes());target=folder/f"P{r['physical_page']:04d}.tiff";target.write_bytes(data)
    prior=r['provenance']['embedded_images'][0]
    prior['prior_tiff_sha256']=prior['tiff_sha256']
    prior.update(tiff_path=target.relative_to(root).as_posix(),tiff_bytes=len(data),tiff_sha256=sha(data),pixel_mode=im.mode,pixel_size=list(im.size),pixel_sha256=pixelsha,serialization_note='Exact stored TIFF serialization from the final runtime; source-pixel identity, not a synthetic TIFF header, is the cross-runtime fidelity test. Prior serialization digest retained separately.')
    rows.append([r['physical_page'],prior['tiff_path'],len(data),prior['tiff_sha256'],im.mode,*im.size,pixelsha])
p.write_text('\n'.join(canonical(x) for x in records)+'\n',encoding='utf-8',newline='\n')
with (root/'audit/FINAL_PIXEL_PROVENANCE.tsv').open('w',encoding='utf-8',newline='') as stream:
    w=csv.writer(stream,delimiter='\t',lineterminator='\n');w.writerow(['physical_page','tiff_path','bytes','sha256','pixel_mode','width','height','pixel_sha256']);w.writerows(rows)
with (root/'audit/FINAL_SOURCE_FREEZE_V3.tsv').open('w',encoding='utf-8',newline='') as stream:
    w=csv.writer(stream,delimiter='\t',lineterminator='\n');w.writerow(['physical_page','printed_page','french_record_path','bytes','sha256','canonical_record_sha256'])
    for r in records:
        f=r['final_french_freeze'];w.writerow([r['physical_page'],r['printed_page'],f['path'],f['bytes'],f['sha256'],sha(canonical(r).encode())])
print(json.dumps({'status':'FINAL_SOURCE_FROZEN_WITH_REPLAYABLE_NATIVE_PIXELS','ndjson_sha256':sha(p.read_bytes()),'stored_native_images':35}))
