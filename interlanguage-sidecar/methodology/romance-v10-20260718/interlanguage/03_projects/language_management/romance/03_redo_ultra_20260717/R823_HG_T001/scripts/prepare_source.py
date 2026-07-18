from pathlib import Path
import csv, hashlib, json

HERE=Path(__file__).resolve().parent
TRANCHE=HERE.parent
ROMANCE=TRANCHE.parents[1]
REPO=ROMANCE.parents[3]
authority_candidates=list((ROMANCE/'02_r823_romance_translation_20260717'/'authority_extract').rglob('Noether_R823_cum_de.tex'))
if not authority_candidates:
    raise SystemExit('R823 authority extraction not found')
authority=authority_candidates[0]

def digest_bytes(b): return hashlib.sha256(b).hexdigest().upper()
def digest_file(p): return digest_bytes(p.read_bytes())

EXPECTED_AUTH='EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21'
if digest_file(authority)!=EXPECTED_AUTH: raise SystemExit('Authority hash mismatch')

lines=authority.read_text(encoding='utf-8-sig').splitlines()
metadata_start,metadata_end=20985,20990
start,end=21047,21087
slice_lines=lines[start-1:end]
exact=('\n'.join(slice_lines)+'\n').encode('utf-8')
source_dir=TRANCHE/'source'; source_dir.mkdir(parents=True,exist_ok=True)
exact_path=source_dir/'R823_HG_T001_de_exact.tex'
exact_path.write_bytes(exact)
(source_dir/'R823_HG_T001_de_numbered.txt').write_text('\n'.join(f'{n}: {lines[n-1]}' for n in range(start,end+1))+'\n',encoding='utf-8')
metadata_path=source_dir/'R823_HG_T001_de_metadata_exact.tex'
metadata_path.write_bytes(('\n'.join(lines[metadata_start-1:metadata_end])+'\n').encode('utf-8'))
(source_dir/'R823_HG_T001_de_metadata_numbered.txt').write_text(
    '\n'.join(f'{n}: {lines[n-1]}' for n in range(metadata_start,metadata_end+1))+'\n',encoding='utf-8'
)

seed=TRANCHE/'semantic'/'R823_HG_T001_clause_map_seed.csv'
rows=[]
with seed.open(encoding='utf-8-sig',newline='') as f:
    for r in csv.DictReader(f):
        a,b=int(r['source_line_start']),int(r['source_line_end'])
        text='\n'.join(lines[a-1:b])
        r['source_text_sha256']=digest_bytes((text+'\n').encode('utf-8'))
        r['source_text']=text.replace('\n',' ⏎ ')
        rows.append(r)
out=TRANCHE/'semantic'/'R823_HG_T001_clause_map.csv'
fields=list(rows[0])
with out.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

manifest={
 'artifact':'R823_HG_T001_SOURCE_MANIFEST','authority_path':str(authority),'authority_sha256':EXPECTED_AUTH,
 'body_source_lines':[start,end],'body_exact_slice_path':str(exact_path),'body_exact_slice_sha256':digest_file(exact_path),
 'metadata_source_lines':[metadata_start,metadata_end],'metadata_exact_slice_path':str(metadata_path),'metadata_exact_slice_sha256':digest_file(metadata_path),
 'expected_slice_sha256_from_independent_design_audit':'33E4D17FEC404CB5B5A7DF208EE1BC5855BB6B0F4091A04905B95B75C1D9AF64',
 'expected_metadata_sha256_after_binding':'D424D5D19D8B8E153B1DF736933F71B83098A5C54135646561B9E3E2C8519559',
 'clause_map_sha256':digest_file(out),'next_cursor_source_line':21089,
}
if manifest['body_exact_slice_sha256']!=manifest['expected_slice_sha256_from_independent_design_audit']:
    raise SystemExit(f"Slice hash mismatch {manifest['body_exact_slice_sha256']}")
if manifest['metadata_exact_slice_sha256']!=manifest['expected_metadata_sha256_after_binding']:
    raise SystemExit(f"Metadata hash mismatch {manifest['metadata_exact_slice_sha256']}")
(source_dir/'R823_HG_T001_SOURCE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps(manifest,indent=2))
