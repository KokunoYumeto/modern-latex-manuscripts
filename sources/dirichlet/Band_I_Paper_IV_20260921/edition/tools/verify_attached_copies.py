"""Validate mounted original packet ZIPs and compare all extracted/loose copies.
Run in the input-bearing session; full-state resumption uses verify_handoff.py.
"""
from pathlib import Path,PurePosixPath
import zipfile,csv,json,hashlib,unicodedata
R=Path(__file__).resolve().parents[1]
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
 return h.hexdigest().upper()
masters=[];copies=[]
for path in sorted(R.parent.glob('DIRICHLET_PAPER_IV_INPUT_PACKAGE*.zip')):
 with zipfile.ZipFile(path) as z:
  assert z.testzip() is None
  names=[i.filename for i in z.infolist() if not i.is_dir()]
  assert len(names)==21 and len(set(names))==21
  assert all(n==unicodedata.normalize('NFC',n) and not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts and '\\' not in n for n in names)
  for n in names:
   b=z.read(n);assert b==(R/'input'/n).read_bytes()
  masters.append({'file':path.name,'bytes':path.stat().st_size,'sha256':sha(path),'file_members':len(names),'crc':'PASS','paths':'PASS','all_extracted_members_byte_identical':True})
assert len(masters)==2 and len({r['sha256'] for r in masters})==1
for p in sorted((R/'input').iterdir()):
 assert p.is_file();q=R.parent/p.name
 assert q.is_file() and sha(q)==sha(p)
 copies.append({'file':p.name,'bytes':p.stat().st_size,'sha256':sha(p),'loose_attached_copy_byte_identity':'PASS'})
assert len(copies)==21
(R/'qa/MASTER_ZIP_VALIDATION.json').write_text(json.dumps({'schema':'dirichlet-master-input-bytes-v1','masters':masters,'exact_extracted_files':21,'loose_project_copies':21,'status':'PASS'},indent=2)+'\n')
with (R/'qa/LOOSE_ATTACHED_COPY_VALIDATION.tsv').open('w',encoding='utf8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(copies[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(copies)
print('Both attached master ZIPs: identical, 21 files, CRC/path/extracted-byte checks PASS; 21 loose attached copies: identical.')
