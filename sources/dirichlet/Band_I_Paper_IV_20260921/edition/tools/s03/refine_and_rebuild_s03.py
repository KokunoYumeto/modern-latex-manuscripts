"""Record source-backed S03 English refinements; preserve actual pre-correction evidence."""
from pathlib import Path
import shutil,json,csv,hashlib,subprocess
R=Path(__file__).resolve().parents[2]; Q=R/'qa/s03'; D=Q/'initial_build'
if D.exists():raise RuntimeError('Initial evidence already preserved; do not rerun refinement.')
D.mkdir();shutil.copytree(Q/'build',D/'build')
for fn in ['BUILD_RUNS.json','EXTRACTED_TEXT_FR.txt','EXTRACTED_TEXT_EN.txt','EXTRACTED_TEXT_APPARATUS.txt']:
 shutil.copy2(Q/fn,D/fn)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest().upper()
(D/'VISUAL_HASHES.json').write_text(json.dumps({str(p.relative_to(Q/'visual')):sha(p) for p in sorted((Q/'visual').rglob('*.png'))},indent=2)+'\n')
f=R/'editions/en/pages/p097.tex';shutil.copy2(f,D/'p097_en_before.tex');shutil.copy2(Q/'visual/en/page33_p097.png',D/'p097_en_before.png')
s=f.read_text();s=s.replace('Replacing $\\pm t$ by','If we replace $\\pm t$ by').replace('Multiplying now,\nmember by member, this equation and the preceding one, one has','If one now multiplies\nmember by member this equation and the preceding one, one has').replace('or, which comes to the same thing:','or which comes to the same thing:');assert s!=f.read_text();f.write_text(s)
fields=['printed_page','authority_pdf_page','layer','before','after','evidence','disposition']
rows=[{'printed_page':97,'authority_pdf_page':114,'layer':'English argumentative syntax','before':'Replacing ±t by χs; Multiplying now, member by member, this equation and the preceding one','after':'If we replace ±t by χs; If one now multiplies member by member this equation and the preceding one','evidence':'Exact-scope leaf35/full PDF114: Si nous remplaçons ±t par χs; Si l’on multiplie maintenant membre par membre cette équation et la précédente. qa/s03/source/p097_authority.png; actual pre-correction draft qa/s03/initial_build/p097_en_before.tex','disposition':'CORRECTED_S03_DIRECT_SOURCE_DRAFT; explicit conditional constructions restored; mathematical tokens unchanged'}, {'printed_page':97,'authority_pdf_page':114,'layer':'English punctuation','before':'or, which comes to the same thing:','after':'or which comes to the same thing:','evidence':'Exact-scope leaf35/full PDF114, penultimate paragraph: ou ce qui revient au même:; no comma after ou. qa/s03/source/p097_authority.png','disposition':'CORRECTED_S03_DIRECT_SOURCE_DRAFT; unnecessary comma removed to follow printed junction'}]
with (Q/'SOURCE_BACKED_DIFF_S03.tsv').open('w',newline='') as out:
 w=csv.DictWriter(out,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
old=(R/'SOURCE_BACKED_DIFF.tsv').read_bytes();assert old.endswith(b'\n');add=(Q/'SOURCE_BACKED_DIFF_S03.tsv').read_bytes().split(b'\n',1)[1];(R/'SOURCE_BACKED_DIFF.tsv').write_bytes(old+add)
subprocess.run(['python',str(R/'tools/s03/build_s03.py')],check=True)
