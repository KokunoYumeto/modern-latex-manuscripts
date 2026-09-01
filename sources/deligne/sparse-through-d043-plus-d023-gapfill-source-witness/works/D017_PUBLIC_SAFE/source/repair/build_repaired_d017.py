"""Rebuild staged D017 editions from immutable NDJSON plus explicit authority repairs.
No network, Git, publication, shared ledger, or original-source writes.
"""
from pathlib import Path
import csv, hashlib, json, os, re, shutil, sys

ROOT = Path(__file__).resolve().parent
SOURCE = Path(os.environ.get('D017_INPUT_ROOT',str(ROOT.parents[2] / 'NM_EXTRACT/20260831/D017_DELIGNE_D017_GL2_S09_CUMULATIVE_FULL_STATE_F9B5AC9B0DBF'))).resolve()
OUT = Path(os.environ.get('D017_OUTPUT_ROOT',str(ROOT / 'candidate'))).resolve()
LAYERS = ('source_language', 'english_standalone')

def sha(b): return hashlib.sha256(b).hexdigest().upper()
def dump(p, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
def load(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def tex_escape(s):
    return ''.join({'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}.get(c,c) for c in s)

PREAMBLE = r'''\documentclass[10pt,a4paper]{article}
\usepackage[margin=18mm,headheight=14pt]{geometry}
\usepackage{fontspec}
\setmainfont{Latin Modern Roman}
\usepackage{amsmath,amssymb,mathtools,enumitem,graphicx,longtable,array,fancyhdr}
\usepackage{tikz-cd}
\usepackage[unicode,hidelinks]{hyperref}
\providecommand{\GL}{\operatorname{GL}}
\providecommand{\SL}{\operatorname{SL}}
\providecommand{\PGL}{\operatorname{PGL}}
\providecommand{\Hom}{\operatorname{Hom}}
\providecommand{\Iso}{\operatorname{Iso}}
\providecommand{\Isom}{\operatorname{Isom}}
\providecommand{\Ker}{\operatorname{Ker}}
\providecommand{\Aut}{\operatorname{Aut}}
\providecommand{\Lie}{\operatorname{Lie}}
\providecommand{\Sym}{\operatorname{Sym}}
\providecommand{\Tr}{\operatorname{Tr}}
\providecommand{\Ind}{\operatorname{Ind}}
\providecommand{\car}{\operatorname{car}}
\providecommand{\im}{\operatorname{im}}
\providecommand{\red}{\operatorname{red}}
\providecommand{\sprep}{\operatorname{sp}}
\providecommand{\sprod}{\mathop{\prod}\nolimits'}
\providecommand{\R}{\mathbb R}
\providecommand{\Q}{\mathbb Q}
\providecommand{\Z}{\mathbb Z}
\providecommand{\C}{\mathbb C}
\providecommand{\A}{\mathbb A}
\providecommand{\Af}{\mathbb A^f}
\providecommand{\GA}{G_{\mathbb A}}
\providecommand{\SG}{SG}
\providecommand{\OO}{\mathcal O}
\providecommand{\M}{\mathrm M}
\providecommand{\calR}{\mathcal R}
\providecommand{\calJ}{\mathfrak F}
\providecommand{\calH}{\mathcal H}
\providecommand{\calK}{\mathcal K}
\providecommand{\cK}{\mathcal K}
\providecommand{\cS}{\mathcal S}
\providecommand{\iso}{\xrightarrow{\sim}}
\setlength{\parindent}{1em}
\setlength{\parskip}{3pt}
\setlist{nosep,leftmargin=2em}
\allowdisplaybreaks
\emergencystretch=2em
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small P. Deligne --- D017}
\fancyhead[R]{\small\nouppercase{\leftmark}}
\fancyfoot[C]{\thepage}
\begin{document}
'''

def main():
    records = {ly:{int(r['physical_page']):r for r in map(json.loads,(SOURCE/'edition'/f'{ly}.ndjson').read_text(encoding='utf-8-sig').splitlines())} for ly in LAYERS}
    assert all(sorted(records[ly]) == list(range(1,52)) for ly in LAYERS)
    authority = SOURCE/'source/20_AUTHORITY_DELIGNE_D017_GL2_51PP_IAS_300DPI.pdf'
    assert sha(authority.read_bytes()) == '4E735CA05197F215F4D45CF485D45C1F646B3B1EFD1F4A4A5A399524A02E624B'
    applied=[]
    helper = load(ROOT/'authority_fidelity/D017_P001_P026_AUTHORITY_REPLACEMENTS.json')
    for item in helper['field_replacements']:
        ly,p,f = item['language'],item['physical_page'],item['field']
        before=records[ly][p].get(f,'')
        assert sha(before.encode()) == item['before_sha256'], (ly,p,'before mismatch')
        assert sha(item['replacement'].encode()) == item['after_sha256']
        records[ly][p][f]=item['replacement']
        applied.append({'kind':'helper_field_replacement','layer':ly,'page':p,'before':item['before_sha256'],'after':item['after_sha256']})
    first6 = load(ROOT/'authority_fidelity/D017_P001_P006_EDITABLE_LATEX.json')
    for item in first6['field_replacements']:
        ly,p=item['language'],item['physical_page']
        assert 1 <= p <= 6
        records[ly][p]['editable_latex']=item['replacement']
        applied.append({'kind':'initial_math_typesetting','layer':ly,'page':p,'after':sha(item['replacement'].encode())})
    repairs=load(ROOT/'repairs_27_51.json')
    for r in repairs:
        hits=0
        for ly in (LAYERS if r['layer']=='both' else (r['layer'],)):
            text=records[ly][r['page']]['editable_latex']
            count=text.count(r['old'])
            if count:
                after=text.replace(r['old'],r['new'])
                records[ly][r['page']]['editable_latex']=after
                applied.append({'kind':'asserted_authority_repair','id':r['id'],'layer':ly,'page':r['page'],'occurrences':count,'before':sha(text.encode()),'after':sha(after.encode()),'reason':r['reason']})
                hits+=count
            elif r['layer']!='both':
                raise AssertionError(('repair not found',r['id'],ly,r['old']))
        assert hits, ('repair not found in either layer',r['id'])
    for ly,start in [('source_language','on a\n'),('english_standalone','one has\n')]:
        records[ly][49]['editable_latex']=start+records[ly][49]['editable_latex']
    cold=[]
    for name in ('COLD_01_26_FINDINGS.json','COLD_17_26_SUPPLEMENT.json'):
        cold.extend(load(ROOT/name)['findings'])
    for r in cold:
        for p in r['physical_pages']:
            for ly in r['layers']:
                before=records[ly][p]['editable_latex']
                assert r['old'] in before, ('cold repair not found',r['id'],ly,p,r['old'])
                after=before.replace(r['old'],r['new'])
                records[ly][p]['editable_latex']=after
                applied.append({'kind':'cold_authority_repair','id':r['id'],'layer':ly,'page':p,'before':sha(before.encode()),'after':sha(after.encode()),'reason':r['issue']})
    typ=load(ROOT/'TYPE_AND_LITERAL_01_26.json')
    for r in typ['rows']:
        ly,p=r['layer'],r['page']
        before=records[ly][p]['editable_latex']
        assert r['old'] in before, ('typography/literal missing',r['id'],ly,p)
        after=before.replace(r['old'],r['new'],1 if r['id'].startswith(('T25','T26')) else -1)
        records[ly][p]['editable_latex']=after
        applied.append({'kind':'typography_or_literal','id':r['id'],'layer':ly,'page':p,'before':sha(before.encode()),'after':sha(after.encode()),'reason':r['reason']})
    for r in typ['ranges']:
        ly,p=r['layer'],r['page']
        before=records[ly][p]['editable_latex']
        a=before.index(r['start'])+len(r['start'])
        b=before.index(r['end'],a) if r['end'] else len(before)
        after=before[:a]+'{\\itshape '+before[a:b]+'\\par}\n'+before[b:]
        records[ly][p]['editable_latex']=after
        applied.append({'kind':'statement_typography','layer':ly,'page':p,'before':sha(before.encode()),'after':sha(after.encode()),'reason':r['basis']})
    for ly in LAYERS:
        for p in range(1,52):
            # Protect literal bracket at an array row start from optional row-height parsing.
            records[ly][p]['editable_latex']=records[ly][p]['editable_latex'].replace('\\\\\n[','\\\\\n{}[')
    # Font normalization is explicit and orthogonal to the lexical/formula repairs.
    for ly in LAYERS:
        for p in range(30,39):
            t=records[ly][p]['editable_latex']
            t=t.replace('G_1^0',r'\mathcal A_1^0').replace('G^0',r'\mathcal A^0')
            records[ly][p]['editable_latex']=t
    cold27=load(ROOT/'authority_fidelity/cold_27_51/ASSERTED_CORRECTIONS_P027_P051.json')
    for r in cold27['corrections']:
        assert 27<=r['page']<=51
        for ly in (LAYERS if r['layer']=='both' else (r['layer'],)):
            p=r['page']
            before=records[ly][p]['editable_latex']
            assert before.count(r['old'])==r['expected_occurrences'], ('cold27 repair absent or nonunique',r['id'],ly,p)
            after=before.replace(r['old'],r['new'])
            records[ly][p]['editable_latex']=after
            applied.append({'kind':'independent_cold_authority_repair','id':r['id'],'layer':ly,'page':p,'before':sha(before.encode()),'after':sha(after.encode()),'reason':r['reason']})
    for r in cold27['typography']:
        ly,p=r['language'],r['page']
        before=records[ly][p]['editable_latex']
        assert before.count(r['old'])==1, ('cold27 typography absent/nonunique',r['label'],ly,p)
        assert r['new'].replace('{\\itshape ','',1).replace('\\par}','',1).strip()==r['old'].strip(), ('typography changed content',r['label'])
        after=before.replace(r['old'],r['new'])
        records[ly][p]['editable_latex']=after
        applied.append({'kind':'statement_typography','id':r['label'],'layer':ly,'page':p,'before':sha(before.encode()),'after':sha(after.encode()),'reason':r['reason']})
    terms=load(ROOT/'authority_fidelity/cold_27_51/ASSERTED_TERM_EMPHASIS_P029_P038_P039.json')
    for r in terms['corrections']:
        ly,p=r['layer'],r['page']
        before=records[ly][p]['editable_latex']
        assert before.count(r['old'])==r['expected_occurrences'], ('term scope absent/nonunique',r['id'])
        assert re.sub(r'\\emph\{([^{}]*)\}',r'\1',r['new'])==r['old'], ('term changed content',r['id'])
        after=before.replace(r['old'],r['new'])
        records[ly][p]['editable_latex']=after
        applied.append({'kind':'defined_term_typography','id':r['id'],'layer':ly,'page':p,'before':sha(before.encode()),'after':sha(after.encode()),'reason':r['reason']})
    out_sources=OUT/'sources'
    out_sources.mkdir(parents=True,exist_ok=True)
    for ly in LAYERS:
        fn='D017_FR.tex' if ly=='source_language' else 'D017_EN.tex'
        label='Édition française' if ly=='source_language' else 'Standalone English edition'
        title='Formes modulaires et représentations de GL(2)' if ly=='source_language' else 'Modular forms and representations of GL(2)'
        body=PREAMBLE+f'\\begin{{center}}\\Large {title}\\\\[5pt]\\large P. Deligne\\\\[5pt] {label}\\end{{center}}\n'
        cover=(r'Témoin de référence: 51 pages physiques, pages imprimées 55--105. Les graphies, abréviations et erreurs apparentes du témoin sont conservées. Les repères de page sont éditoriaux. La composition est refaite; les folios et identifiants courants sont exclus du corps. L\textquotesingle{}apparat séparé consigne les restitutions vérifiées sur le témoin.' if ly=='source_language' else r'Authority: 51 physical pages, printed pages 55--105. Source spelling, abbreviations and apparent errors are retained. Page labels below are editorial anchors, not source text. Typography is reflowed; source folios and running identifiers are excluded. The separate apparatus records authority restorations.')
        body+=r'\noindent\small '+cover+r'\normalsize\par'+'\n'
        for p in range(1,52):
            body+='\n\\clearpage\n'+f'\\markboth{{Authority {p} / printed {p+54}}}{{}}\n\\hypertarget{{authority-{p}}}{{}}\n'
            body+=records[ly][p]['editable_latex'].strip()+'\n'
        body+='\\end{document}\n'
        (out_sources/fn).write_text(body,encoding='utf-8')
        (out_sources/f'{ly}.ndjson').write_text(''.join(json.dumps({'physical_page':p,'printed_page':p+54,'editable_latex':records[ly][p]['editable_latex'],'inherited_acceptance':'ZERO_ACCEPTED'},ensure_ascii=False)+'\n' for p in range(1,52)),encoding='utf-8')
    # Concise apparatus: source anomalies and transparent correction register, no invented exposition.
    app=PREAMBLE+r'\section*{D017 --- Editorial apparatus}'+'\n'
    app+=r'\noindent Full returned scope: 51/51 authority pages (printed 55--105). The inherited web-session PASS is not an independent corpus PASS. Every inherited branch and witness remains ZERO\_ACCEPTED and is retained unchanged in the original full-state packet. This staged version restores readings checked against the authority image. No claim of correction of the original mathematical paper is made.\par'+'\n'
    app+=r'\subsection*{Transcription policy}'+'\n'
    app+=r'French preserves lexical readings, abbreviations, intrinsic punctuation and formulas, including apparent errors. English translates the assertions and retains the same printed formulas. Display spacing, line wrapping, paragraph indentation and font equivalents are normalized; punctuation separating extracted displays may be reset for sentence continuity. Parenthetical qualifications are preserved. The running Del identifiers and folios are excluded from reader bodies but remain in the complete authority. Roman operator names, blackboard-bold number fields and script mathematical spaces are consistent typographic equivalents. Typewritten statement underlining is represented by italic statement bodies; underlined defined terms are emphasized. Source bibliographic volume underlining is retained and titles remain roman.\par'+'\n'
    app+=r'\subsection*{Apparent source anomalies retained}'+'\n'
    app+=r'Physical 17 has an additional rightward isomorphism arrow ending at no printed node; this is preserved alongside the leftward and downward maps. Physical 18 omits the tilde on $\SL$ in the displayed restricted product despite the surrounding discussion of double covers. Physical 29 prints $\gamma^{\prime}\in$ before a matrix. Physical 32 (theorem 2.4.4) prints $\omega(-1)=k$, in contrast to $(-1)^k$ on physical 30, and prints conductor $n/\ell m<n$ without grouping the slash denominator. Physical 39 gives $0\le i<n$ and separately $Ne_{n-1}=0$. Physical 40 prints unprimed $W(\overline K/K)$ in Example 3.1.5 and $W(\overline K/K)$ in the proof parenthesis. Physical 42 prints $\pi$ without subscript $u$ on the right side of (A)(1). Physical 46 omits $g$ inside the left argument of the Hecke induction formula and prints labels 5.2.3.1 and 5.2.6. Physical 49 prints an unprimed dual $\pi$ in the first denominator. The repeated 3.2.9.8 labels and the unmatched closing-parenthesis glyph in reference [12] are retained. These readings are not silently repaired.\par'+'\n'
    app+=r'\subsection*{Restoration register}'+'\n'
    app+=r'\noindent Exact old/new strings, field hashes, and all replayed repairs are supplied in the machine-readable repair logs. The following record states the intervention basis, not an independent final audit verdict.\par'+'\n'
    for p in range(1,52):
        notes=[r['reason'] for r in repairs if r['page']==p and r['old']!=r['new']]
        notes.extend(r['issue'] for r in cold if p in r['physical_pages'])
        notes.extend(r['reason'] for r in typ['rows'] if p==r['page'])
        notes.extend(r['reason'] for r in cold27['corrections'] if p==r['page'])
        if p <=26:
            notes.append('Source and English rechecked against authority; exact field replacements and findings are recorded in the accompanying field-replacement log for physical pages1--26.' if p>6 else 'Text-only inherited layer independently reset as editable mathematical TeX from authority; exact replacements are recorded in the accompanying initial six-page typesetting log.')
        if notes:
            app+=f'\\paragraph{{Physical {p}; printed {p+54}.}} '+tex_escape(' '.join(dict.fromkeys(notes)))+'\n'
    app+=r'\clearpage\section*{Image fallbacks}'+'\n'
    app+=r'\noindent These unretouched authority crops preserve fragile alignment, arrows, diagram topology, and source anomalies. They supplement the editable editions; they do not replace reader pages. Crop hashes are replayed against the inherited asset ledger. The complete 51-page authority remains the controlling witness.\par'+'\n'
    fallbacks=[]
    for asset in csv.DictReader((SOURCE/'edition/asset_ledger.tsv').read_text(encoding='utf-8-sig').splitlines(),delimiter='\t'):
        if asset['kind']=='FULL_PAGE_AUTHORITY_FACSIMILE': continue
        src=SOURCE/asset['raw_crop_path']
        assert sha(src.read_bytes())==asset['raw_crop_sha256'].upper(), asset['asset_id']
        dest=out_sources/'assets'/src.name
        dest.parent.mkdir(exist_ok=True)
        if not dest.exists(): shutil.copy2(src,dest)
        assert sha(dest.read_bytes())==sha(src.read_bytes())
        app+=r'\clearpage'+f"\\subsection*{{Physical {asset['physical_page']}; printed {asset['printed_page']}}}\n"
        app+='\\noindent '+tex_escape(asset['kind'].replace('_',' ').lower())+'\\par\n'
        app+='\\begin{center}\\includegraphics[width=\\linewidth,height=.82\\textheight,keepaspectratio]{assets/'+src.name+'}\\end{center}\n'
        fallbacks.append({'asset_id':asset['asset_id'],'physical_page':int(asset['physical_page']),'path':'assets/'+src.name,'sha256':sha(src.read_bytes()),'inherited_acceptance':'ZERO_ACCEPTED','current_check':'HASH_REPLAY_PASS','bbox_pixels':asset['bbox_pixels']})
    dump(OUT/'FALLBACK_MANIFEST.json',fallbacks)
    app+='\\end{document}\n'
    (out_sources/'D017_Apparatus.tex').write_text(app,encoding='utf-8')
    dump(OUT/'APPLIED_REPAIRS.json',applied)
    dump(OUT/'BUILD_INPUTS.json',{'authority':{'relative_path':str(authority.relative_to(SOURCE)).replace('\\','/'),'sha256':sha(authority.read_bytes())},'inherited_archive_sha256':'F9B5AC9B0DBFA571DC9193AA6C61FA24FBE7D588EEB183B9962690FB1140B107','scope_physical':list(range(1,52)),'inputs':{str(p.relative_to(ROOT)).replace('\\','/'):sha(p.read_bytes()) for p in [ROOT/'repairs_27_51.json',ROOT/'COLD_01_26_FINDINGS.json',ROOT/'COLD_17_26_SUPPLEMENT.json',ROOT/'TYPE_AND_LITERAL_01_26.json',ROOT/'authority_fidelity/D017_P001_P026_AUTHORITY_REPLACEMENTS.json',ROOT/'authority_fidelity/D017_P001_P006_EDITABLE_LATEX.json',ROOT/'authority_fidelity/cold_27_51/ASSERTED_CORRECTIONS_P027_P051.json',Path(__file__)]},'status':'BUILD_CANDIDATE_NOT_COLD_AUDITED'})
    inputs=load(OUT/'BUILD_INPUTS.json')
    inputs['inputs']['authority_fidelity/cold_27_51/ASSERTED_TERM_EMPHASIS_P029_P038_P039.json']=sha((ROOT/'authority_fidelity/cold_27_51/ASSERTED_TERM_EMPHASIS_P029_P038_P039.json').read_bytes())
    dump(OUT/'BUILD_INPUTS.json',inputs)
    print(json.dumps({'status':'TEX_GENERATED','physical_pages':51,'languages':2,'applied_records':len(applied)}))

if __name__=='__main__': main()
