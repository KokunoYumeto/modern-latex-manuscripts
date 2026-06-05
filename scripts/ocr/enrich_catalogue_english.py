#!/usr/bin/env python3
"""Merge English star descriptions (from the parallel translation workflow) into the
authoritative catalogue CSV. Input grid/wf_english.json: {"stars":[{"constellation","n","english"}]}.
Constellation names from agents are Latin/English; normalised to the CSV's const_lat values.
Adds/fills an 'english' column. Reports coverage. Non-destructive to existing columns.
"""
import json, csv, os, re
HERE=os.path.dirname(os.path.abspath(__file__))
J=os.path.join(os.path.dirname(os.path.dirname(HERE)),'grind','wf_english.json')
CSVF=os.path.join(HERE,'albattani_catalogue_authoritative.csv')

def norm(s):
    s=(s or '').strip().lower()
    s=re.sub(r'[^a-z]','',s)
    # map common Latin/English variants -> the const_lat token (lowercased, no spaces)
    aliases={'ursaminor':'ursaminor','ursamaior':'ursamajor','ursamajor':'ursamajor',
      'canismaior':'canismajor','canismajor':'canismajor','canisminor':'canisminor',
      'scorpio':'scorpius','scorpius':'scorpius','capricornus':'capricornus','capricorn':'capricornus',
      'piscisaustrinus':'piscisaustrinus','piscisaustralis':'piscisaustrinus','equuleus':'equuleus',
      'coronaborealis':'coronaborealis','coronaaustralis':'coronaaustralis','coronaaustrina':'coronaaustralis',
      'serpens':'serpens','cepheus':'cepheus','bootes':'bootes'}
    return aliases.get(s,s)

def main():
    if not os.path.exists(J):
        print('no wf_english.json yet'); return
    data=json.load(open(J,encoding='utf-8'))
    stars=data.get('stars',data if isinstance(data,list) else [])
    eng={}
    for s in stars:
        try: eng[(norm(s['constellation']), int(s['n']))]=s['english'].strip()
        except Exception: pass
    rows=list(csv.DictReader(open(CSVF,encoding='utf-8')))
    cols=rows[0].keys()
    if 'english' not in cols:
        cols=list(cols)+['english']
        for r in rows: r['english']=''
    hit=0
    for r in rows:
        if r.get('const')=='LACUNA': continue
        k=(norm(r.get('const_lat') or r.get('const')), int(r['n']) if str(r['n']).isdigit() else -1)
        if k in eng and eng[k]:
            r['english']=eng[k]; hit+=1
    with open(CSVF,'w',newline='',encoding='utf-8') as fh:
        w=csv.DictWriter(fh,fieldnames=cols); w.writeheader(); w.writerows(rows)
    tot=sum(1 for r in rows if r.get('const')!='LACUNA')
    print(f'english filled {hit}/{tot} stars')

if __name__=='__main__': main()
