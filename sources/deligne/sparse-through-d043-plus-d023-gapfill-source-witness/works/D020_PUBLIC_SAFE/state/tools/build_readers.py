#!/usr/bin/env python3
"""Deterministic offline native-MathML replay of the editable math layer."""
import argparse,html,importlib.util,json,pathlib,re,sys
sys.dont_write_bytecode=True
p=argparse.ArgumentParser();p.add_argument('root',nargs='?',default='.');p.add_argument('--check',action='store_true');a=p.parse_args()
root=pathlib.Path(a.root).resolve();sys.path.insert(0,str(root/'tools'/'vendor'))
from latex2mathml.converter import convert
spec=importlib.util.spec_from_file_location('math_reader',root/'tools'/'build_math_readers.py');mr=importlib.util.module_from_spec(spec);spec.loader.exec_module(mr)

def fragment(tex):
    protected=[]
    def save(value):
        protected.append(value);return f'@@SAVED{len(protected)-1}@@'
    def mathml(s,display=False):
        labels=re.findall(r'\\tag\{([^{}]+)\}',s);s=re.sub(r'\\tag\{[^{}]+\}','',s)
        # Converter 3.81.0 maps single-letter mathrm to an ASCII numeric
        # entity without mathvariant. Scoped rm retains explicit upright mi.
        s=re.sub(r'\\mathrm\{([^{}]+)\}',lambda m:r'{\rm '+m[1]+'}',s)
        s=re.sub(r'\\mathrm\s+([A-Za-z])',lambda m:r'{\rm '+m[1]+'}',s)
        value=convert(s,display='block' if display else 'inline').replace(' xmlns="http://www.w3.org/1998/Math/MathML"','')
        if display:value='<div class="formula">'+value+(' <span class="equation-label">('+html.escape(labels[0])+')</span>' if labels else '')+'</div>'
        return save(value)
    tex=re.sub(r'\\seqsplit\{([^{}]+)\}',r'\1',tex)
    tex=re.sub(r'\\includegraphics\[[^\]]*\]\{([^}]+)\}',lambda m:save('<img class="authority-figure" src="../assets/presentation_derivatives/'+html.escape(m[1],quote=True)+'" alt="Authority lacets figure, conservative lossless presentation">'),tex)
    tex=re.sub(r'\\begin\{equation\*\}(.*?)\\end\{equation\*\}',lambda m:mathml(m[1],True),tex,flags=re.S)
    tex=re.sub(r'\\\[(.*?)\\\]',lambda m:mathml(m[1],True),tex,flags=re.S)
    tex=re.sub(r'\\\((.*?)\\\)',lambda m:mathml(m[1]),tex,flags=re.S)
    tex=re.sub(r'\\section\*\{([^{}]*)\}',lambda m:save('<h3>'+html.escape(m[1])+'</h3>'),tex)
    tex=re.sub(r'\\textsc\{([^{}]*)\}',lambda m:save('<span style="font-variant:small-caps">'+html.escape(m[1])+'</span>'),tex)
    tex=re.sub(r'\\textbf\{([^{}]*)\}',lambda m:save('<strong>'+html.escape(m[1])+'</strong>'),tex)
    tex=re.sub(r'\\textup\{([^{}]*)\}',lambda m:save('<span style="font-style:normal">'+html.escape(m[1])+'</span>'),tex)
    tex=re.sub(r'\\textsuperscript\{([^{}]*)\}',lambda m:save('<sup>'+html.escape(m[1])+'</sup>'),tex)
    tex=re.sub(r'\\emph\{([^{}]*)\}',lambda m:save('<em>'+html.escape(m[1])+'</em>'),tex)
    tex=re.sub(r'\{\\itshape ([^{}]*)\}',lambda m:save('<em>'+html.escape(m[1])+'</em>'),tex)
    tex=html.escape(tex).replace(r'\begin{center}','<div class="center">').replace(r'\end{center}','</div>').replace(r'\\ ','<br>')
    tex=tex.replace(r'\begin{flushright}','<div style="text-align:right">').replace(r'\end{flushright}','</div>')
    tex=tex.replace(r'\noindent ','<p>').replace(r'\par','</p>').replace(r'\dotfill',' <span class="leaders"></span> ')
    tex=tex.replace(r'\textbackslash{}','&#92;').replace(r'\#','#').replace(r'\%','%').replace(r'\&amp;','&amp;').replace(r'\_','_').replace(r'\{','{').replace(r'\}','}')
    for _ in range(3):tex=re.sub(r'@@SAVED([0-9]+)@@',lambda m:protected[int(m[1])],tex)
    return tex

titles={'source_language':('fr','La conjecture de Weil. I'),'english_standalone':('en','The Weil Conjecture. I'),'apparatus':('en','Separate page-addressed apparatus')}
stale=[]
for layer,(language,title) in titles.items():
    recs=[json.loads(s) for s in (root/'edition'/f'{layer}.ndjson').read_text(encoding='utf-8').splitlines()];mr.LAYER=layer
    parts=['<!doctype html>',f'<html lang="{language}"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',f'<title>Pierre Deligne - {title}</title>',
    '<style>body{font:18px/1.5 Cambria,Georgia,serif;max-width:58rem;margin:2rem auto;padding:0 1rem;color:#191919}h1{font-size:1.9rem}h2{font:0.85rem/1.4 system-ui,sans-serif;color:#555}h3{font-size:1.3rem}article{border-top:1px solid #bbb;margin-top:2rem;padding-top:1rem}p{margin:.65rem 0}math{font-family:"Cambria Math",serif;font-size:1em}.formula{position:relative;margin:1.1rem 0;overflow-x:auto;padding:.35rem 3.5rem .35rem .5rem}.equation-label{position:absolute;right:.2rem;top:40%;font-size:.8rem}.center{text-align:center}.authority-figure{display:block;max-width:75%;height:auto;margin:1rem auto}.leaders{display:inline-block;width:20%;border-bottom:1px dotted #777}em math{font-style:normal}</style>',
    '<style>.formula{padding-left:4.5rem}.equation-label{right:auto;left:.2rem;font-weight:bold}</style>',
    f'<body><header><h1>{title}</h1><p>Pierre Deligne</p><p>36 authority physical-page dispositions; 35 article pages. Native mathematical text; separate apparatus and retained authority provenance.</p></header>']
    for rec in recs:
        page=rec['physical_page'];mr.PAGE=page
        if page==1 and layer!='apparatus':continue
        if page==2 and layer!='apparatus':
            first,rest=rec['text'].split('\n\n',1)
            if first.startswith(('LA CONJECTURE','THE WEIL')):rec=dict(rec,text=rest)
        label=f'Authority physical page {page}; printed {rec["printed_page"]}' if page>1 else 'Authority physical page 1; repository-cover boundary disposition'
        parts.append(f'<article id="page-{page:04d}"><h2>{label}</h2>');parts.append(fragment(mr.record_text(rec)));parts.append('</article>')
    parts+=['</body></html>',''];expected='\n'.join(parts);assert '<script' not in expected and '<pre' not in expected
    path=root/'readers'/f'{layer}.html'
    if a.check:
        if not path.exists() or path.read_text(encoding='utf-8')!=expected:stale.append(path.name)
    else:path.write_text(expected,encoding='utf-8',newline='\n')
if stale:raise SystemExit('stale native MathML readers: '+','.join(stale))
print(json.dumps({'result':'PASS','mode':'check' if a.check else 'write','representation':'NATIVE_MATHML','converter':'latex2mathml 3.81.0'}))
