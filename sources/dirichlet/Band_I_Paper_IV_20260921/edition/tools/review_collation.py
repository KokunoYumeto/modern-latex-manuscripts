from pathlib import Path
import re,difflib,json
R=Path(__file__).resolve().parents[1]
oldpath=next((R/'inherited/R27').glob('*/new/orig/tex/*.tex'))
old=oldpath.read_text().split(r'\begin{document}',1)[1].split(r'\end{document}',1)[0]
new='\n'.join(p.read_text() for p in sorted((R/'editions/fr/pages').glob('*.tex')))
def norm(s):
 s=re.sub(r'%[^\n]*','',s)
 s=re.sub(r'\\unitid\{[^}]+\}','',s)
 s=re.sub(r'\\begin\{center\}.*?\\end\{center\}','',s,flags=re.S)
 s=re.sub(r'\\sectionnumber\{[^}]+\}','',s)
 s=re.sub(r'\\centerline\{\\rule\{[^}]+\}\{[^}]+\}\}','',s)
 s=re.sub(r'\\vspace\{[^}]+\}','',s)
 s=re.sub(r'\\(?:begin|end)\{[^}]+\}','',s)
 s=re.sub(r'\\(?:textsc|emph|text|footnote|sourcefootnote|tag)(?=\{)','',s)
 s=re.sub(r'\\(?:par|indent|noindent|quad|qquad)\b','',s)
 s=s.replace('\\\\','').replace(r'\[','').replace(r'\]','').replace('$','').replace('&','').replace(r'\,','')
 s=s.replace(r'\dfrac',r'\frac')
 s=re.sub(r'\\ldots|\\cdots',r'\\dots',s)
 s=s.replace('»','„').replace('«','“').replace("’","'")
 return re.findall(r'\\[a-zA-Z]+|[^\W\d_]+|\d+|[^\w\s]',s)
a=norm(old);b=norm(new)
d=[]
for op,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
 if op!='equal':
  row={'op':op,'before':' '.join(a[i:j]),'after':' '.join(b[k:l]),'left_context':' '.join(b[max(0,k-10):k]),'right_context':' '.join(b[l:l+10])}
  d.append(row)
print('TOKENS old',len(a),'new',len(b),'DIFFERENCES',len(d))
for i,row in enumerate(d):print(i+1,row)
(R/'qa/FR_TOKEN_COLLATION_REVIEW.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
