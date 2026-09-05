#!/usr/bin/env python3
"""Make a new, never-overwritten disposable subject and exact byte manifest."""
import hashlib,json,pathlib,shutil,sys
root=pathlib.Path(sys.argv[1]).resolve();destination=pathlib.Path(sys.argv[2]).resolve()
assert root.name=='S06_math_v3' and destination.name=='S06_math_v3_01'
assert not destination.exists(), 'Audit subject must be new'
destination.mkdir(parents=True)
subject=destination/'state';subject.mkdir();(destination/'evidence').mkdir()
rows=[]
for p in sorted(root.rglob('*')):
    rel=p.relative_to(root)
    if not p.is_file() or rel.parts[:2]==('audit','native_reader_qa'):continue
    assert '__pycache__' not in rel.parts and p.suffix not in ('.pyc','.pyo')
    target=subject/rel;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,target)
    data=p.read_bytes();assert target.read_bytes()==data
    rows.append({'path':rel.as_posix(),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest().upper()})
manifest={'schema':'d020-immutable-cold-subject-v1','status':'IN_PROGRESS','source_workspace':str(root),'subject':str(subject),'exclusion':'Derived native PNG cache only; independent auditor must render fresh images.','files':rows}
(destination/'SUBJECT_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'subject':str(subject),'files':len(rows),'bytes':sum(r['bytes'] for r in rows),'manifest_sha256':hashlib.sha256((destination/'SUBJECT_MANIFEST.json').read_bytes()).hexdigest().upper()}))
