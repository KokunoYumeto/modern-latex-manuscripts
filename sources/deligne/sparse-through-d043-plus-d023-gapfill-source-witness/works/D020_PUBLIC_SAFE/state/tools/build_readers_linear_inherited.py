#!/usr/bin/env python3
import argparse,csv,html,json,pathlib
PAGES=36
LAYERS=[
 ('source_language','source_status','fr','Pierre Deligne — La conjecture de Weil I — Édition française diplomatique'),
 ('english_standalone','english_status','en','Pierre Deligne — The Weil Conjecture I — Standalone English'),
 ('apparatus','apparatus_status','en','Pierre Deligne — La conjecture de Weil I — Apparatus'),
]
def rows(p):
 with p.open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
def records(root,layer):
 out={}
 for n,line in enumerate((root/'edition'/f'{layer}.ndjson').read_text(encoding='utf-8').splitlines(),1):
  if not line.strip():continue
  obj=json.loads(line);page=int(obj['physical_page']);assert page not in out,f'duplicate {layer} page {page}';out[page]=obj
 return out
def render(layer,status_key,lang,title,coverage,recs):
 accepted=[r for r in coverage if r[status_key] in ('ACCEPTED','FROZEN')]
 article=[r for r in accepted if r['disposition']=='INCLUDE_ARTICLE']
 shown=accepted if layer=='apparatus' else article
 out=['<!doctype html>',f'<html lang="{lang}">','<meta charset="utf-8">','<meta name="viewport" content="width=device-width,initial-scale=1">',f'<title>{html.escape(title)}</title>',
 '<style>body{font:18px/1.52 Georgia,serif;max-width:78rem;margin:2rem auto;padding:0 1rem;color:#181818}header.reader{border-bottom:2px solid #222;margin-bottom:2rem}article{border-top:1px solid #bbb;padding:1.25rem 0 1.75rem}article:first-of-type{border-top:0}h1{font-size:2rem;line-height:1.2}h2{font-size:1.08rem;font-family:system-ui,sans-serif;color:#444}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:1rem/1.55 Georgia,serif;margin:0}figure{text-align:center;page-break-inside:avoid;margin:1rem auto 1.5rem}figure img{display:block;max-width:82%;max-height:20rem;margin:.6rem auto}figcaption{display:block;max-width:60rem;margin:.6rem auto;font:0.9rem/1.35 system-ui,sans-serif;color:#444}.boundary{background:#f4f4f4;border:1px solid #ccc;padding:1rem}</style>',
 '<body>','<header class="reader">',f'<h1>{html.escape(title)}</h1>',f'<p>Accepted physical-page dispositions: {len(accepted)} of {PAGES}. Included article pages: {len(article)} of 35.</p>','</header>']
 for row in shown:
  page=int(row['physical_page']);rec=recs[page]
  if row['disposition']=='INCLUDE_ARTICLE':label=f'Printed page {row["printed_page"]} — authority physical page {page}'
  else:label=f'Authority physical page {page} — repository-cover boundary disposition'
  cls=' class="boundary"' if row['disposition']!='INCLUDE_ARTICLE' else ''
  out += [f'<article id="page-{page:04d}"{cls}><h2>{html.escape(label)}</h2>']
  text=str(rec.get('text',''));assets=list(rec.get('assets',[]));placed=set();cursor=0
  for idx,asset in enumerate(assets):
   marker=str(asset.get('placement_after',''))
   if not marker:continue
   pos=text.find(marker,cursor)
   if pos<0:continue
   end=pos+len(marker);out.append(f'<pre>{html.escape(text[cursor:end])}</pre>')
   out += [f'<figure><img src="../{html.escape(str(asset["raw_path"]),quote=True)}" alt="raw authority crop"><img src="../{html.escape(str(asset["presentation_path"]),quote=True)}" alt="presentation derivative"><figcaption>{html.escape(str(asset.get("caption",asset.get("id","source asset"))))}</figcaption></figure>']
   placed.add(idx);cursor=end
  out.append(f'<pre>{html.escape(text[cursor:])}</pre>')
  for idx,asset in enumerate(assets):
   if idx in placed:continue
   out += [f'<figure><img src="../{html.escape(str(asset["raw_path"]),quote=True)}" alt="raw authority crop"><img src="../{html.escape(str(asset["presentation_path"]),quote=True)}" alt="presentation derivative"><figcaption>{html.escape(str(asset.get("caption",asset.get("id","source asset"))))}</figcaption></figure>']
  out.append('</article>')
 out += ['</body>','</html>',''];return '\n'.join(out)
p=argparse.ArgumentParser();p.add_argument('root',nargs='?',default='.');p.add_argument('--check',action='store_true');a=p.parse_args();root=pathlib.Path(a.root).resolve();coverage=rows(root/'coverage'/'coverage.tsv');stale=[]
for layer,status,lang,title in LAYERS:
 expected=render(layer,status,lang,title,coverage,records(root,layer));path=root/'readers'/f'{layer}.html'
 if a.check:
  if not path.is_file() or path.read_text(encoding='utf-8')!=expected:stale.append(path.name)
 else:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(expected,encoding='utf-8',newline='\n')
if stale:raise SystemExit('stale readers: '+', '.join(stale))
print(json.dumps({'result':'PASS','mode':'check' if a.check else 'write'},sort_keys=True))
