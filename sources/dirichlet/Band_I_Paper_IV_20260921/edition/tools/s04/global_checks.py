"""Mechanical cross-layer and topology checks supplementary to actual manual scan collation.
TeX-line/segment indices are editable-source locators, NOT physical scan-line numbers.
"""
from pathlib import Path
import re,json,csv,zipfile,hashlib
from audit_support import R,Q,h

def write_tsv(path,rows,keys=None):
 with path.open('w') as f:
  w=csv.DictWriter(f,fieldnames=keys or list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
def units(s):
 ms=list(re.finditer(r'^% U:(\S+) \| ([^\n]+)\n',s,re.M));out=[]
 for i,m in enumerate(ms):
  end=ms[i+1].start() if i+1<len(ms) else len(s)
  out.append({'id':m[1],'structure':m[2],'body':s[m.end():end],'start':s[:m.end()].count('\n')+1,'end':s[:end].count('\n')})
 return out
pat=re.compile(r'(?<!\\)\$(.*?)(?<!\\)\$|\\\[(.*?)\\\]|\\begin\{equation\*\}(.*?)\\end\{equation\*\}',re.S)
def math(s):
 s=re.sub(r'%[^\n]*','',s)
 s=re.sub(r'\\begin\{equation\*\}(.*?)\\end\{equation\*\}',lambda m:m[1] if r'\begin{minipage}' in m[1] else m[0],s,flags=re.S)
 return [('inline' if m[1] is not None else 'display',next(v for v in m.groups() if v is not None).strip()) for m in pat.finditer(s)]
def canon(s):
 s=s.replace(r'\text{lorsque }',r'\text{when }').replace(r'\text{ étant pair}',r'\text{ being even}')
 s=re.sub(r'\\(?:text|hbox)\{(ou|or)\}',r'\\text{or}',s);s=s.replace(r'\dfrac',r'\frac');s=re.sub(r'\\(?:quad|qquad)\b','',s)
 return re.sub(r'\s+','',s)
manual=json.loads((Q/'MANUAL_COLD_COLLATION.json').read_text());assert sorted(map(int,manual))==list(range(63,99))
formulas=[];align=[];mismatches=[];sources=[];structure=[]
for p in range(65,99):
 files={l:R/f'editions/{l}/pages/p{p:03}.tex' for l in ('fr','en')};text={l:path.read_text() for l,path in files.items()};uu={l:units(t) for l,t in text.items()}
 assert [u['id'] for u in uu['fr']]==[u['id'] for u in uu['en']],p
 for a,b in zip(uu['fr'],uu['en']):
  ma,mb=math(a['body']),math(b['body'])
  if len(ma)!=len(mb):mismatches.append({'page':p,'unit':a['id'],'counts':[len(ma),len(mb)]})
  for n,((ka,va),(kb,vb)) in enumerate(zip(ma,mb),1):
   same=ka==kb and canon(va)==canon(vb)
   if not same:mismatches.append({'page':p,'unit':a['id'],'segment':n,'fr':va,'en':vb})
   formulas.append({'printed_page':p,'full_pdf_page':p+17,'scope_leaf':p-62,'unit_id':a['id'],'segment':n,'placement':ka,'french_tex':va,'english_tex':vb,'cross_language_math':'EQUAL' if same else 'REVIEW','source_review':'Manual scan reading recorded separately','manual_evidence':f'qa/s04/MANUAL_COLD_COLLATION.json#/{p}'})
  align.append({'printed_page':p,'unit_id':a['id'],'fr_structure':a['structure'],'en_structure':b['structure'],'fr_tex_lines':f"{a['start']}-{a['end']}",'en_tex_lines':f"{b['start']}-{b['end']}",'math_segments':len(ma),'manual_structural_review':manual[str(p)]['english_structural_review']})
 for lang,t in text.items():
  sources.append({'printed_page':p,'language':lang,'path':str(files[lang].relative_to(R)),'bytes':files[lang].stat().st_size,'sha256':h(files[lang].read_bytes())})
  structure.append({'printed_page':p,'language':lang,'section_numbers':','.join(re.findall(r'\\sectionnumber\{([^}]+)\}',t)),'heads':';'.join(re.findall(r'\\sourceheading\{([^}]+)\}',t)),'labels':';'.join(re.findall(r'\\tag\{([^}]+)\}',t)),'author_notes':t.count('\\sourcefootnote{'),'rules':len(re.findall(r'\\rule\{',t))})
for l in ('fr','en'):
 t=(R/f'editions/{l}/main.tex').read_text()
 assert [int(x) for x in re.findall(r'\\input\{pages/p(\d+)\.tex\}',t)]==list(range(65,99))
 assert [int(x) for x in re.findall(r'\\setcounter\{page\}\{(\d+)\}',t)]==list(range(65,99))
 assert sum(x['author_notes'] for x in structure if x['language']==l)==1
 assert all(x['printed_page']==71 for x in structure if x['language']==l and x['author_notes'])
write_tsv(Q/'MATH_SEGMENT_ALIGNMENT.tsv',formulas);write_tsv(Q/'UNIT_ALIGNMENT.tsv',align);write_tsv(Q/'CURRENT_SOURCE_BINDINGS.tsv',sources);write_tsv(Q/'STRUCTURE_INVENTORY.tsv',structure)
(Q/'GLOBAL_CHECKS.json').write_text(json.dumps({'author_pages_each_language':list(range(65,99)),'scope_leaves_manually_read':36,'copy_pages':[63,64],'aligned_units':len(align),'paired_math_segments':len(formulas),'mismatches':mismatches,'note_pages_each_language':[71],'explicit_mathematical_prose_translations':['ou/or','lorsque/when','étant pair/being even'],'math_count_definition':'Includes isolated inline variables, labels and display blocks; not a count of distinct equations','reader_inputs_exact_once':True,'limitation':'Mechanical equality and counts do not establish source fidelity. Actual source-image collation observations and linked detail crops are the separate manual evidence.'},ensure_ascii=False,indent=2)+'\n')
print('units',len(align),'math segments',len(formulas),'mismatches',json.dumps(mismatches,ensure_ascii=False))
