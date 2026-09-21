"""Record manual scan collation observations and source-backed edits; never infer fidelity from counts."""
from pathlib import Path
import json,hashlib,csv,shutil
R=Path(__file__).resolve().parents[2]
Q=R/'qa/s04'
def h(b):return hashlib.sha256(b).hexdigest().upper()
def preserve(rel):
 p=R/rel;t=R/'history/S03/superseded'/rel
 if not t.exists():t.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,t)
def record(page,observations,english,math,notes='No author footnote on this page.',status='COLLATED'):
 p=Q/'MANUAL_COLD_COLLATION.json';d=json.loads(p.read_text()) if p.exists() else {}
 d[str(page)]={'printed_page':page,'authority_pdf_page':page+17,'scope_leaf':page-62,'source_image':f'qa/s04/source/p{page:03}_authority.png','observations':observations,'english_structural_review':english,'mathematical_token_review':math,'notes_and_anchors':notes,'status':status,'method':'Direct visual reading of the current source image, sequential prose-line and mathematical-token comparison with the independently read FR and EN editable page files; not inferred from earlier ledgers or counts.'}
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def repair(page,layer,rel,before,after,evidence,count=1):
 p=R/rel;t=p.read_text();assert t.count(before)==count,(rel,before,t.count(before),count)
 preserve(rel)
 f=Q/'REPAIRS.json';d=json.loads(f.read_text()) if f.exists() else []
 i=len(d)+1; old=Q/f'repair_snapshots/{i:03d}_before.txt';old.parent.mkdir(parents=True,exist_ok=True);old.write_text(t)
 t=t.replace(before,after);p.write_text(t)
 d.append({'id':f'S04-{i:03d}','printed_page':str(page),'authority_pdf_page':str(page+17),'layer':layer,'before':before,'after':after,'evidence':f'Full PDF {page+17}; exact-scope leaf {page-62}; '+evidence,'disposition':'CORRECTED_TO_AUTHORITY; prior bytes retained','file':rel,'occurrences':count,'snapshot':str(old.relative_to(R))})
 f.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
 # The cumulative TSV is updated immediately with each edit; prior72 rows remain bytewise intact.
 base=(R/'history/S03/SOURCE_BACKED_DIFF_CANONICAL.tsv').read_bytes()
 (R/'SOURCE_BACKED_DIFF.tsv').write_bytes(base)
 keys=['printed_page','authority_pdf_page','layer','before','after','evidence','disposition']
 with (R/'SOURCE_BACKED_DIFF.tsv').open('a') as out:
  w=csv.DictWriter(out,fieldnames=keys,delimiter='\t',lineterminator='\n',extrasaction='ignore');w.writerows(d)
 print(d[-1]['id'],rel)
