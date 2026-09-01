"""Read-only verification of the explicit D017 preparation manifest."""
import hashlib,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def identity(p):
    with p.open('rb') as f:h=hashlib.file_digest(f,'sha256').hexdigest().upper()
    return {'bytes':p.stat().st_size,'sha256':h}
m=json.loads((ROOT/'INPUT_MANIFEST.json').read_text(encoding='utf-8'))
for row in m['source_tree_mapping']:
    p=(ROOT/row['path']).resolve()
    assert p.is_relative_to(ROOT)
    assert identity(p)=={k:row[k] for k in ('bytes','sha256')},row['path']
for row in m['standalone_tex_equalities']:
    assert identity(ROOT/row['source_tree_member'])=={k:row[k] for k in ('bytes','sha256')}
r=subprocess.run([sys.executable,str(ROOT/'reassemble_provenance.py')],capture_output=True,text=True,check=True)
assert json.loads(r.stdout)['status']=='PASS'
assert m['actual_next_public_baseline'] is None and m['no_cumulative_build'] and m['no_publication_or_git']
print(json.dumps({'status':'PASS','mapped_files':len(m['source_tree_mapping']),'source_members':m['source_member_count'],
                  'transfer_chunks':m['transfer_chunk_count'],'whole_carrier_sha256':m['public_carrier']['sha256'],
                  'baseline_not_assumed':True},sort_keys=True))
