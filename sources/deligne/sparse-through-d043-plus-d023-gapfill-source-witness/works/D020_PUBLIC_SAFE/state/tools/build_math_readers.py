#!/usr/bin/env python3
"""Typeset the frozen page records, without treating linear notation as text.

The generated TeX is an independently editable presentation layer.  Every
mathematical span is logged with its source identity and generated TeX.
No edition record is modified by this builder.
"""
from __future__ import annotations
import hashlib, json, pathlib, re, sys, unicodedata

ROOT = pathlib.Path(sys.argv[1]).resolve()
SPAN_LOG = []
LAYER = ''
PAGE = 0
PARAGRAPH = ''
OPS = {'Spec','Gal','Hom','End','Ker','Tr','GL','SL','Sp','CSp','sp','gl','deg','dim','det','log','exp','inf','div','binom','mod','lim','proj'}
LETTERS = r'A-Za-zÀ-ÖØ-öø-ÿĀ-ž'
GREEK = dict(zip('αβγδεζηθικλμνξοπρστυφχψωΓΔΘΛΞΠΣΥΦΨΩ', 'alpha beta gamma delta varepsilon zeta eta theta iota kappa lambda mu nu xi omicron pi rho sigma tau upsilon varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega'.split()))
SYMBOLS = {'∑':r'\sum','Σ':r'\sum','∏':r'\prod','⊗':r'\otimes','⊕':r'\oplus','∈':r'\in','∉':r'\notin','∩':r'\cap','∪':r'\cup','⊂':r'\subset','⊄':r'\not\subset','⊆':r'\subseteq','≠':r'\ne','≤':r'\leq','≥':r'\geq','≡':r'\equiv','≅':r'\simeq','⇒':r'\Rightarrow','⇔':r'\Leftrightarrow','↔':r'\leftrightarrow','→':r'\longrightarrow','←':r'\longleftarrow','↦':r'\longmapsto','↪':r'\hookrightarrow','↩':r'\hookleftarrow','∞':r'\infty','±':r'\pm','∤':r'\nmid','⊥':r'\perp','∨':r'\vee','ℓ':r'\ell','ℜ':r'\Re','ℱ':r'\mathcal{F}','𝓕':r'\mathcal{F}','𝓔':r'\mathcal{E}','𝒢':r'\mathcal{G}','𝒫':r'\mathcal{P}','𝔏':r'\mathfrak{L}','×':r'\times','·':r'\cdot','−':'-','…':r'\cdots','#':r'\#','′':r'\prime','″':r'\prime\prime'}
SUP = dict(zip('⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾','0123456789+-=()'))
SUB = dict(zip('₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎','0123456789+-=()'))
SYMBOLS['≃']=r'\simeq'
SYMBOLS['∘']=r'\circ'

def escape(s):
    table={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','#':r'\#','$':r'\$','%':r'\%','&':r'\&','_':r'\_','^':r'\textasciicircum{}','~':r'\textasciitilde{}'}
    return ''.join(table.get(c,c) for c in s)

def balanced(s, start):
    closing={'(':')','{':'}','[':']'}[s[start]]
    level=1
    for end in range(start+1,len(s)):
        if s[end]==s[start]: level+=1
        elif s[end]==closing:
            level-=1
            if level==0:return s[start+1:end],end+1
    raise ValueError(f'unbalanced group page {PAGE}: {s[start:]}')

def capital(char,s,after):
    """Contextual source semantic fonts, not a global bold-letter guess."""
    tail=s[after:]
    if char=='O':return r'\mathcal{O}'
    if char=='F' and re.match(r'^_(?:[qp]|\([qp])',tail):return r'\mathbf{F}'
    if char=='Q':
        polynomial=(PAGE>=31 or (PAGE==6 and tail.startswith('(t)')))
        if PAGE==5:
            polynomial=PARAGRAPH.startswith(('Écrivons','Write '))
        if PAGE==25:polynomial=PARAGRAPH.startswith(('Proposition (6.6)',))
        if PAGE==26:polynomial=not PARAGRAPH.startswith(('(6.9)','Les polynômes','The polynomials'))
        if tail.startswith('_ℓ'):polynomial=False
        return (r'\mathrm{Q}' if polynomial else r'\mathbf{Q}')
    if char=='Z':
        integer=(PAGE in (2,9,13,16,17,19,31) or tail.startswith(('_ℓ','/ℓ','/p','/N','[[','[t]')))
        if PAGE==5:integer=tail.startswith('[[') or tail.startswith('[t]')
        if tail.startswith(('_S','_0','₀')):integer=False
        return r'\mathbf{Z}' if integer else r'\mathrm{Z}'
    if char=='R' and PAGE in (9,31) and not tail.startswith(('^','_','(')):return r'\mathbf{R}'
    if char=='C':return r'\mathbf{C}'
    if char=='P' and PAGE in (12,15,18,19,20,21,23,28,29,30,31):return r'\mathbf{P}'
    if char=='P' and PAGE==34 and tail.startswith('^n'):return r'\mathbf{P}'
    return r'\mathrm{'+char+'}'

def math(s):
    original=s
    s=s.strip().replace('<=','≤').replace('>=','≥').replace('->~','≅').replace('->','→')
    s=s.replace('F*','F^*').replace('σ*','σ^*').replace('C*','C^*').replace('E*','E^*').replace('E_λ*','E_λ^*').replace('(Z/N)*','(Z/N)^*')
    s=s.replace('...','…').replace('b.q','b·q').replace('2.p','2·p').replace('ε(p).p','ε(p)·p')
    # Native fractions whose linear source syntax explicitly groups numerator
    # and denominator.  Other slash notation is retained as a quotient slash.
    special={
        'f((az+b)/(cz+d))':r'f\left(\frac{az+b}{cz+d}\right)',
        '(a b; c d)':r'\begin{pmatrix}a&b\\c&d\end{pmatrix}',
        'd/dt':r'\frac{d}{dt}',
        '(1/p)':r'\frac{1}{p}',
        '(k-1)/2':r'\frac{k-1}{2}',
        'binom(N+r,N)':r'\binom{\mathrm{N}+r}{\mathrm{N}}',
        'ι_(r)':r'\iota_{(r)}',
    }
    if PAGE in (27,30):
        special.update({'kd/2':r'\frac{kd}{2}','d/2':r'\frac{d}{2}','1/(2k)':r'\frac{1}{2k}','1/2':r'\frac{1}{2}'})
    if PAGE==10:special['−nχ(X)/2']=r'\frac{-n\chi(\mathrm{X})}{2}'
    if PAGE==14:special['β/2+1/(2k)']=r'\frac{\beta}{2}+\frac{1}{2k}'
    if PAGE in (15,16):special.update({'(β+1)/2':r'\frac{\beta+1}{2}','−β/2':r'\frac{-\beta}{2}','1/2':r'\frac{1}{2}'})
    if PAGE==24:special.update({'(n+1)/2':r'\frac{n+1}{2}','1/2':r'\frac{1}{2}'})
    placeholders={}
    for k,v in special.items():
        if k in s:
            key=chr(0xe000+len(placeholders)); placeholders[key]=v;s=s.replace(k,key)
    out=[];i=0
    while i<len(s):
        c=s[i]
        if c in placeholders:out.append(placeholders[c]);i+=1;continue
        if c=='=' and i+2<len(s) and s[i+1]=='_' and s[i+2] in '({':
            group,after=balanced(s,i+2)
            caption=r'\mathrm{dfn}' if group=='dfn' else math(group)
            if re.fullmatch(r'\d+\.\d+\.\d+',group):caption='('+caption+')'
            out.append(r'\underset{'+caption+'}{=}');i=after;continue
        if c in '→←' and i+2<len(s) and s[i+1] in '^_' and s[i+2] in '({':
            position=s[i+1];group,after=balanced(s,i+2);caption=math(group)
            arrow=r'\xrightarrow' if c=='→' else r'\xleftarrow'
            out.append(arrow+('{'+caption+'}' if position=='^' else '['+caption+']{}'));i=after;continue
        if c=='⊗' and i+1<len(s) and s[i+1]=='^':out.append(r'\bigotimes\limits');i+=1;continue
        if c=='⊕' and i+1<len(s) and s[i+1] in '^_':out.append(r'\bigoplus\limits');i+=1;continue
        if c=='⊗' and s[:i].rstrip().endswith('='):out.append(r'\bigotimes');i+=1;continue
        if c in '^_':
            script=c;i+=1
            if i>=len(s):raise ValueError(f'empty script {original}')
            if s[i] in '({':group,i=balanced(s,i)
            else:
                op=re.match(r'(deg|dim|det|Tr|Gal|End|Sp|red|an)(?=\(|\b)',s[i:])
                if op:
                    group=op.group();i+=len(group)
                    if i<len(s) and s[i]=='(':
                        inner,i=balanced(s,i);group+='('+inner+')'
                else:
                    group=s[i];i+=1
                    while i<len(s) and (unicodedata.combining(s[i]) or s[i] in "'′″"):group+=s[i];i+=1
            out.append(script+'{'+(r'\mathrm{'+group+'}' if group in ('an','red','dfn') else math(group))+'}');continue
        if c in SUP or c in SUB:
            table=SUP if c in SUP else SUB;script='^' if c in SUP else '_';group=''
            while i<len(s) and s[i] in table:group+=table[s[i]];i+=1
            out.append(script+'{'+group+'}');continue
        if c in "'′″":
            out.append("'" if c!="″" else "''");i+=1;continue
        if i+1<len(s) and unicodedata.combining(s[i+1]):
            accent={'\u0304':'overline','\u0302':'widehat','\u0303':'widetilde','\u030c':'check'}.get(s[i+1])
            if accent:
                base=(r'\mathbf{'+c+'}') if c in 'FQZ' else math(c)
                out.append('\\'+accent+'{'+base+'}');i+=2;continue
        if c in SYMBOLS:out.append(SYMBOLS[c]+' ');i+=1;continue
        if c in GREEK:out.append('\\'+GREEK[c]+' ');i+=1;continue
        if c=='~':out.append(r'\sim ');i+=1;continue
        if c=='{':out.append(r'\{');i+=1;continue
        if c=='}':out.append(r'\}');i+=1;continue
        if c.isalpha():
            match=re.match('['+LETTERS+']+',s[i:])
            if match:
                word=match.group();i+=len(word)
                if word in ('sp','gl') and PAGE in (22,23):out.append(r'\mathfrak{'+word+'}')
                elif word=='sp' and PAGE in (16,17):out.append(r'\mathit{sp}')
                elif word in OPS:out.append('\\operatorname{'+word+'}')
                elif len(word)>3 or word in ('sur','un','de','du','en','le','la','les','si','et','odd','even','on','of','at','to','in','if'):out.append('\\text{'+escape(word)+'}')
                else:
                    for j,char in enumerate(word):
                        # Source's field/ring fonts, distinguished from its
                        # polynomial Q and denominator Q in context.
                        if char.isupper():out.append(capital(char,s,i))
                        else:out.append(char)
                continue
        if c=='&':out.append(r'\&')
        elif c=='%':out.append(r'\%')
        else:out.append(c)
        i+=1
    result=''.join(out)
    # A protected fraction may pass through recursive script parsing; expand
    # every outer placeholder again after those child calls return.
    for key,value in placeholders.items():result=result.replace(key,value)
    # Labelled arrows and equality annotations are mathematical operators,
    # not subscripts attached to an adjacent variable.
    result=re.sub(r'\\longrightarrow\s*\^\{([^{}]*)\}',r'\\xrightarrow{\1}',result)
    result=re.sub(r'\\longleftarrow\s*\^\{([^{}]*)\}',r'\\xleftarrow{\1}',result)
    result=re.sub(r'\\longrightarrow\s*_\{([^{}]*)\}',r'\\xrightarrow[\1]{}',result)
    result=re.sub(r'=\s*_\{([^{}]*)\}',r'\\underset{\1}{=}',result)
    return result

def tokens(s):
    return list(re.finditer('['+LETTERS+r"]+(?:[’']["+LETTERS+r"]+)*|[0-9]+|[^"+LETTERS+r'0-9]',s))

def isbase(token):
    t=token.group()
    return (len(t)==1 and (t.isascii() and t.isalpha() and t!='a' or t in SYMBOLS or t in GREEK)) or t in OPS or t=='ch' or bool(re.fullmatch('[0-9]+',t)) or any(c in SUP or c in SUB for c in t)

def inline(s):
    # Tokenize, marking actual mathematical atoms; prose words terminate a
    # span.  Scripts/groups are retained verbatim in the span ledger.
    if LAYER=='source_language' and PAGE in (3,12,15,23):
        pronoun=re.search(r'\b(?:Il y a|il y a|y est utilisée|y est démontré)\b',s)
        if pronoun:return inline(s[:pronoun.start()])+escape(pronoun.group())+inline(s[pronoun.end():])
    title='A p-adic proof of Weil’s conjectures'
    if title in s:
        before,after=s.split(title,1)
        return inline(before)+r'A \(p\)-adic proof of Weil’s conjectures'+inline(after)
    citation=re.search(r'\b\d+(?: \(\d{4}\)|, \d{4}), (?:p\. )?\d+-\d+(?:, n(?:°|o\.)? ?\d+\.\d+)?',s)
    if citation:return inline(s[:citation.start()])+escape(citation.group())+inline(s[citation.end():])
    abbrev=re.search(r'\b(?:i\.e\.|resp\.|cf\.)',s)
    if abbrev:return inline(s[:abbrev.start()])+escape(abbrev.group())+inline(s[abbrev.end():])
    for title in ('The classical groups','Lecture Notes in Mathematics','Lecture Notes in Math.','Amer. J. Math.','Ann. of Math.','Proc. Camb. Phil. Soc.','Bull. Soc. Math. France','Bull. Am. Math. Soc.','Séminaire Bourbaki',"L'analysis situs et la géométrie algébrique",'Séminaire de Géométrie Algébrique du Bois-Marie','Cohomologie ℓ-adique et fonctions L','L’Analysis situs','L’Analysis Situs','Selected papers','a priori'):
        if title in s:
            before,after=s.split(title,1);return inline(before)+r'\emph{'+escape(title)+'}'+inline(after)
    if re.search(r'(?<![0-9A-F])[0-9A-F]{32,}(?![0-9A-F])',s):
        pieces=re.split(r'((?<![0-9A-F])[0-9A-F]{32,}(?![0-9A-F]))',s)
        return ''.join(r'\seqsplit{'+part+'}' if k%2 else inline(part) for k,part in enumerate(pieces))
    s=s.replace('<=','≤').replace('>=','≥').replace('->~','≅').replace('->','→')
    matrix='(a b; c d)'
    if matrix in s:
        left,right=s.split(matrix,1)
        return inline(left)+r'\('+math(matrix)+r'\)'+inline(right)
    ts=tokens(s);out=[];i=0
    while i<len(ts):
        next_nonspace=next((t.group() for t in ts[i+1:] if not t.group().isspace()),'')
        variable_a=(ts[i].group()=='a' and bool(next_nonspace) and (next_nonspace in '_^=∈∉≤≥<>+−-*/∪∩' or next_nonspace in SUB or next_nonspace in SUP))
        if not isbase(ts[i]) and not variable_a:out.append(escape(ts[i].group()));i+=1;continue
        a=i;b=i+1
        while b<len(ts):
            t=ts[b].group()
            if t in '^_' and b+1<len(ts):
                if ts[b+1].group() in '({':
                    group,after=balanced(s,ts[b+1].start())
                    while b<len(ts) and ts[b].start()<after:b+=1
                else:b+=2
                continue
            if isbase(ts[b]) or t.isspace() or t in '_^()[]{}=+−-*/<>|,:;.!?′″\'~' or (len(t)==1 and unicodedata.combining(t)):b+=1
            elif t in ('az','cz','dt','Tx','df','dF','Ft','ix','xy','iz','ji','jx','fu','red'):b+=1
            elif t in ('a','I') and b>a and any(x.group() in '=∈∉^_+−-*/<>≤≥' for x in ts[a:b]):b+=1
            elif t=='a' and b>=a+2 and ts[b-1].group()=='(' and ts[b-2].end()==ts[b-1].start():b+=1
            else:break
        # Don't swallow sentence punctuation, prose hyphens, or an opening
        # parenthesis belonging to the next prose phrase.
        while b>a+1 and (ts[b-1].group().isspace() or (ts[b-1].group() in ',;:.!?-([' and ts[b-2].group() not in '_^')):b-=1
        raw=s[ts[a].start():ts[b-1].end()]
        # An unmatched script argument is never silently accepted.
        try:rendered=math(raw)
        except ValueError:
            b=a+1;raw=ts[a].group();rendered=math(raw)
        if re.fullmatch(r'[0-9\s.,;:()\[\]′-]+',raw) or ('.' in raw and not re.search(r'[_^=+<>∈∉≤≥]',raw) and re.fullmatch(r'[A-Z0-9\s.,;:()-]+',raw)):out.append(escape(raw))
        else:
            out.append(r'\('+rendered+r'\)')
            SPAN_LOG.append({'layer':LAYER,'physical_page':PAGE,'kind':'inline','source':raw,'tex':rendered})
        i=b
    return ''.join(out)

def display(s):
    label='';m=re.match(r'^\s*\((\d+\.\d+\.\d+[′\']?)\)\s*',s)
    if m:label=m.group(1);s=s[m.end():]
    lines=[x.strip() for x in s.splitlines() if x.strip()]
    rendered=[]
    for line in lines:
        # Prose qualifiers within a displayed formula stay upright.
        parts=re.split(r'(\b(?:si|dans|divise|faisceau constant|le faisceau constant|un faisceau|if|in|divides|constant sheaf|the constant sheaf|a sheaf)\b)',line)
        expr=''.join(r'\text{ '+escape(part)+' }' if idx%2 else math(part) for idx,part in enumerate(parts))
        rendered.append(expr)
    body=r' \\ '.join(rendered)
    result=r'\begin{equation*}\begin{gathered}'+body+r'\end{gathered}'+(r'\tag{'+label+'}' if label else '')+r'\end{equation*}'
    SPAN_LOG.append({'layer':LAYER,'physical_page':PAGE,'kind':'display','source':s,'label':label,'tex':result})
    return result

def special_block(p):
    if LAYER=='apparatus':return None
    if PAGE==4 and p.startswith('(1.5.2)'):
        return r'''\begin{equation*}\begin{aligned}
t\frac{d}{dt}\log\mathrm Z(\mathrm X_0,t)&=\frac{t\frac{d}{dt}\mathrm Z(\mathrm X_0,t)}{\mathrm Z(\mathrm X_0,t)}
=\sum_{x\in|\mathrm X_0|}-\frac{-\deg(x)t^{\deg(x)}}{1-t^{\deg(x)}}\\
&=\sum_{x\in|\mathrm X_0|}\sum_{n>0}\deg(x)t^{n\deg(x)}
\underset{(1.4.1)}{=}\sum_n\#\mathrm X_0(\mathbf F_{q^n})\cdot t^n.
\end{aligned}\tag{1.5.2}\end{equation*}'''
    if PAGE==8 and p.startswith('(1.14.2)'):
        return r'''\begin{equation*}\begin{aligned}
t\frac{d}{dt}\log\mathrm Z(\mathrm X_0,\mathcal F_0,t)
&\underset{\mathrm{dfn}}{=}\frac{t\frac{d}{dt}\mathrm Z(\mathrm X_0,\mathcal F_0,t)}{\mathrm Z(\mathrm X_0,\mathcal F_0,t)}\\
&=\sum_n\sum_{x\in\mathrm X^{\mathrm F^n}=\mathrm X_0(\mathbf F_{q^n})}\operatorname{Tr}(\mathrm F_x^{*n},\mathcal F_0)t^n.
\end{aligned}\tag{1.14.2}\end{equation*}'''
    if PAGE==14 and p.lstrip().startswith('Z(U_0,⊗'):
        left,right=p.strip().split('=',1);numerator,denominator=right.rsplit('/',1)
        assert 'H^1(' in numerator and 'H_c^1(' not in numerator
        denominator=denominator.strip();punct=denominator[-1] if denominator[-1] in '.,;' else ''
        if punct:denominator=denominator[:-1]
        return r'\['+math(left)+'='+r'\frac{'+math(numerator)+'}{'+math(denominator)+'}'+punct+r'\]'
    if PAGE==25 and re.match(r'^\s*Z\(X_x,t\)\s*=\s*\[',p):
        left,remaining=p.strip().split('[',1);quotient,suffix=remaining.split(']',1)
        numerator,denominator=quotient.split('/',1)
        assert 'α_i' in numerator and 'β_j' in denominator
        numerator_tex=math(numerator).replace(r'\prod ',r'\prod\limits ')
        denominator_tex=math(denominator).replace(r'\prod ',r'\prod\limits ')
        return r'\['+math(left)+r'\frac{'+numerator_tex+'}{'+denominator_tex+'}'+math(suffix)+r'\]'
    if PAGE==6 and p.lstrip().startswith(('(Q_ℓ-faisceaux','(constructible')):
        return r'\begin{center}'+r'\\ '.join(inline(line.strip()) for line in p.splitlines())+r'\end{center}'
    if '│' in p or ('\n|σ' in p):
        if PAGE==7:return r'\[\begin{array}{ccc}[\mathcal F]&\xrightarrow{\mathrm F}&[\mathcal F]\\ \downarrow\!f&&\downarrow\!f\\ \mathrm X&\xrightarrow{\mathrm F}&\mathrm X\end{array}\]'
        if PAGE in (18,20,24):
            right=r'\widetilde{\mathrm X}' if PAGE!=20 else r'\mathrm Y'; left=r'\mathrm X';bottom=r'\check{\mathbf P}' if PAGE==20 else r'\mathrm D';f='g' if PAGE==20 else 'f';pi=r'\pi' if PAGE!=20 else ''
            if PAGE==24:right+='_0';left+='_0';bottom+='_0';f+='_0';pi+='_0'
            return r'\[\begin{array}{ccc}'+left+r'&\xleftarrow{'+pi+r'}&'+right+r'\\ &&\downarrow\!{'+f+r'}\\ &&'+bottom+r'\end{array}'+(r'\tag{5.1.1}' if PAGE==18 else r'\tag{6.1.1}' if PAGE==24 else '')+r'\]'
        if PAGE==33:return r'\[\begin{array}{ccccc}\mathrm X_0&\hookrightarrow&\mathrm Y_0&&\\ {\scriptstyle\sigma}\downarrow&&\downarrow&&\\ \mathrm A_0&\hookrightarrow&\mathrm P_0&\hookleftarrow\mathrm P_0^\infty&\hookleftarrow\mathrm H_0\end{array}\tag{8.6.1}\]'
        if PAGE==34:return r'\[\begin{array}{ccc}\mathrm X_{\mathrm S}&\xhookrightarrow{u}&\mathrm Z_{\mathrm S}\\ {\scriptstyle\sigma}\downarrow&&\downarrow{\scriptstyle f}\\ \mathrm A_{\mathrm S}&\xrightarrow{a}&\mathrm S\end{array}\]'
    if PAGE==16 and 'n mod 4' in p:
        return r'\[\begin{array}{crrrr}n\bmod4&0&1&2&3\\ \mathrm Tx=x\pm(x,\delta)\delta&-&-&+&+\\ (\delta,\delta)&2&0&-2&0\\ \mathrm T\delta&-\delta&\delta&-\delta&\delta\end{array}\]'
    if PAGE==11 and 'ε = {' in p:
        odd=r'\text{si }n\text{ est impair}' if LAYER=='source_language' else r'\text{if }n\text{ is odd}'
        even=r'\text{si }n\text{ est pair}' if LAYER=='source_language' else r'\text{if }n\text{ is even}'
        return r'\[\varepsilon=\begin{cases}1&'+odd+r',\\(-1)^{\mathrm N}&'+even+r'.\end{cases}\]'
    if PAGE==18 and p.lstrip().startswith('σx'):
        lines=[line.strip() for line in p.splitlines() if line.strip()]
        assert len(lines)==2
        cells=[]
        for line in lines:
            pieces=re.split(r'\s+(si|if)\s+',line,maxsplit=1);assert len(pieces)==3
            cells.append(math(pieces[0])+r'&\text{ '+pieces[1]+r' }'+math(pieces[2]))
        return r'\[\begin{array}{ll}'+r'\\'.join(cells)+r'\end{array}\]'
    return None

def italic_paragraph(p):
    p=p.replace("'",'’')
    if re.match(r'^(Théorème|Lemme|Proposition|Corollaire|Scholie|Scholium|Theorem|Lemma|Corollary) \(',p) and re.search(r'\.\s*[—-]',p[:150]):return True
    starts={
      10:('est une dualité parfaite','is a perfect duality'),
      11:('est une dualité parfaite','is a perfect duality','(i)','(ii)'),
      12:('est une dualité parfaite','is a perfect duality'),
      13:('(i)','(ii)','(iii)','Alors, ℱ','Then ℱ','est une série formelle','is a formal series'),
      22:('(i)','(ii)','Alors, 𝔏','Then 𝔏'),
      25:('écrit sous forme irréductible','when written in lowest terms'),
      26:('Alors S(t)','Then S(t)'),
      30:('W(X_0,i).',),
      31:('On suppose f','Assume that f','En d’autres termes','In other words','sont de valeur absolue','have absolute value','(i)','(ii)'),
      32:('Alors','Then','(ii)','(iii)','est une dualité parfaite','is a perfect pairing'),
      35:('Alors, χ','Then χ','Then, χ'),
    }
    return any(p.startswith(x) for x in starts.get(PAGE,()))

def bibliography(p):
    """Font-only bibliography replay; the record retains exact wording."""
    ordinal=re.match(r'^(1re|2e) ',p)
    if ordinal:
        term=ordinal.group(1)
        return term[0]+r'\textsuperscript{'+term[1:]+'} '+bibliography(p[ordinal.end():])
    author,separator,rest=p.partition(',') if re.match(r'^\[[1-4]\]',p) else (p,'','')
    pieces=re.split(r'(Grothendieck|Lefschetz|Rankin|Weil|Artin|Verdier|Deligne|Katz)',author)
    value=''.join(r'\textsc{'+escape(v)+'}' if i%2 else inline(v) for i,v in enumerate(pieces))
    value+=separator+inline(rest)
    if p.startswith('[3]'):value=value.replace(', 35 (',r', \textbf{35} (')
    if p.startswith('[4]'):value=value.replace(', 55 (',r', \textbf{55} (')
    return value

# Each entry identifies one exact source occurrence, rather than making every
# recurrence of a mathematical term italic. The English counterpart inherits
# the same semantic emphasis. Frozen wording is never changed by this layer.
EMPHASIS = {
 'source_language': {
  8:[('Ceci amène à définir le Frobenius géométrique','Frobenius géométrique')],
  9:[('a) Variétés différentiables','Variétés différentiables'),('Une orientation de X','orientation'),('La classe fondamentale de X','classe fondamentale'),('b) Variétés complexes','Variétés complexes')],
  10:[('il agit via le caractère','via'),('Le faisceau d’orientation de X','faisceau d’orientation'),('La classe fondamentale est un morphisme','classe fondamentale')],
  11:[('Via cette équivalence','Via')],
  13:[('Nous dirons que ℱ_0 est de poids β','poids')],
  16:[('en terme du cycle évanescent','cycle évanescent')],
  17:[('A) n impair','n impair')],
  18:[('B) n pair','n pair'),('a) Si δ≠0','Si'),('b) Si δ=0','Si'),('la duale de A','duale'),('forment le pinceau d’axe A','pinceau d’axe')],
  19:[('(partie évanescente de la cohomologie)','partie évanescente')],
  20:[('forment un pinceau de Lefschetz de sections hyperplanes','pinceau de Lefschetz')],
  21:[('en excluant le cas p=2, n pair','en excluant le cas p=2, n pair'),('est modérément ramifié','modérément'),('a) Si les cycles évanescents sont non nuls :','Si les cycles évanescents sont non nuls :')],
  22:[('b) Si les cycles évanescents sont nuls :','Si les cycles évanescents sont nuls :')],
  23:[('Remarque (5.12)','Remarque')],
  24:[('connexe de dimension paire','paire'),('est un pinceau de Lefschetz','pinceau de Lefschetz')],
  26:[('Préliminaires. —','Préliminaires')],
 },
 'english_standalone': {
  8:[('This leads one to define the geometric Frobenius','geometric Frobenius')],
  9:[('a) Differentiable manifolds','Differentiable manifolds'),('An orientation of X','orientation'),('The fundamental class of X','fundamental class'),('b) Complex varieties','Complex varieties')],
  10:[('it acts through the character','through'),('The orientation sheaf of X','orientation sheaf'),('The fundamental class is a morphism','fundamental class')],
  11:[('Under this equivalence','Under')],
  13:[('We shall say that ℱ_0 has weight β','weight')],
  16:[('in terms of the vanishing cycle','vanishing cycle')],
  17:[('A) n odd','n odd')],
  18:[('B) n even','n even'),('a) If δ≠0','If'),('b) If δ=0','If'),('the dual of A','dual'),('form the pencil with axis A','pencil with axis')],
  19:[('(the vanishing part of the cohomology)','vanishing part')],
  20:[('to form a Lefschetz pencil of hyperplane sections','Lefschetz pencil')],
  21:[('excluding the case p=2 with n even','excluding the case p=2 with n even'),('is tamely ramified','tamely'),('a) If the vanishing cycles are nonzero:','If the vanishing cycles are nonzero:')],
  22:[('b) If the vanishing cycles are zero:','If the vanishing cycles are zero:')],
  23:[('Remark (5.12)','Remark')],
  24:[('connected of even dimension','even'),('is a Lefschetz pencil','Lefschetz pencil')],
  26:[('Preliminaries. —','Preliminaries')],
 }
}

def prose(p):
    item=re.match(r'^\((i{1,3}|iv|v)\)\s+',p)
    if item and LAYER!='apparatus':
        return r'\textup{('+item[1]+')} '+prose(p[item.end():])
    ranges=[]
    for context,term in EMPHASIS.get(LAYER,{}).get(PAGE,[]):
        if context not in p:continue
        assert p.count(context)==1, (PAGE,context)
        start=p.index(context)+context.index(term)
        ranges.append((start,start+len(term),term,'emph'))
    upright={
      'source_language':{27:[('de dimension paire d','paire')],31:[('f cuspidale et primitive','cuspidale'),('f cuspidale et primitive','primitive')]},
      'english_standalone':{27:[('of even dimension d','even')],31:[('f is cuspidal and primitive','cuspidal'),('f is cuspidal and primitive','primitive')]},
    }
    for context,term in upright.get(LAYER,{}).get(PAGE,[]):
        if context in p:
            assert p.count(context)==1
            start=p.index(context)+context.index(term)
            ranges.append((start,start+len(term),term,'textup'))
    out=[];end=0
    for start,stop,term,command in sorted(ranges):
        assert start>=end, (PAGE,term)
        out.append(inline(p[end:start]));rendered='\\'+command+'{'+inline(term)+'}'
        out.append(rendered)
        SPAN_LOG.append({'layer':LAYER,'physical_page':PAGE,'kind':'source-emphasis','source':term,'tex':rendered})
        end=stop
    out.append(inline(p[end:]))
    return ''.join(out)

def labelled_prose(p):
    """Source label font hierarchy, separate from the statement's italics."""
    if LAYER=='apparatus':return None
    heading=re.match(r'^(Théorème|Lemme|Proposition|Corollaire|Scholie|Scholium|Theorem|Lemma|Corollary|Remarque|Remark) (\(\d+\.\d+\))((?: \([^)]*\))?\.\s*[—-]\s*)(.*)$',p,re.S)
    if heading:
        name,number,punctuation,body=heading.groups()
        body=prose(body.replace('\n',' '))
        if name not in ('Remarque','Remark'):body=r'{\itshape '+body+'}'
        return r'\emph{'+escape(name)+r'} \textbf{'+number+'}'+inline(punctuation)+body
    numbered=re.match(r'^(\(\d+\.\d+\))\s+(.*)$',p,re.S)
    if numbered:
        number,body=numbered.groups();body=prose(body.replace('\n',' '))
        if number in ('(2.14)','(5.13)'):body=r'\emph{'+body+'}'
        return r'\textbf{'+number+'} '+body
    return None

def record_text(rec):
    global PARAGRAPH
    s=rec['text']
    # Author/title running heads are provenance, not scholarly body text.
    if PAGE>2:
        s=re.sub(r'^(?:PIERRE DELIGNE|LA CONJECTURE DE WEIL\. I|THE WEIL CONJECTURE\. I|THE WEIL CONJECTURE I)\n\n','',s)
    paragraphs=re.split(r'\n\s*\n',s)
    out=[]
    # Asset placement is deliberately independent of the paragraph-rendering
    # branch.  In particular, numbered prose such as (5.2) returns through the
    # labelled-prose branch, but its authority figure still belongs immediately
    # after that paragraph in both scholarly reader layers.
    assets=rec.get('assets',[]) if LAYER!='apparatus' else []
    asset_hits=[0 for _ in assets]
    for p in paragraphs:
        PARAGRAPH=p.lstrip()
        try:
            if LAYER!='apparatus' and PAGE==36 and p.startswith(('Manuscrit reçu','Manuscript received')):
                out.append(r'\begin{flushright}\emph{'+escape(p)+r'}\end{flushright}');continue
            if LAYER!='apparatus' and ((PAGE==35 and p.startswith(('[1]','[2]','[3]'))) or (PAGE==36)):
                out.append(r'\noindent '+bibliography(p)+r'\par');continue
            special=special_block(p)
            if special:
                SPAN_LOG.append({'layer':LAYER,'physical_page':PAGE,'kind':'source-topology-override','source':p,'tex':special})
                out.append(special);continue
            if p.strip()=='(8.6.1)':continue
            if PAGE==2 and re.match(r'^1\. .*\.{3,}',p):
                for line in p.splitlines():
                    bits=re.split(r'\.{3,}',line)
                    out.append(r'\noindent '+inline(bits[0].strip())+r'\dotfill '+escape(bits[1].strip())+r'\par')
                continue
            if p.strip() in ('SOMMAIRE','CONTENTS','BIBLIOGRAPHIE','BIBLIOGRAPHY'):
                out.append(r'\section*{'+escape(p.strip())+'}');continue
            if re.match(r'^\d+\. [A-ZÉÀ]',p) and '\n' not in p:
                out.append(r'\section*{'+inline(p.strip())+'}');continue
            indented=any(line.startswith('    ') for line in p.splitlines())
            words=re.findall(r"[A-Za-zÀ-ž]+(?:[’'][A-Za-zÀ-ž]+)*",p)
            onlymath=all(len(w)==1 or w in OPS or w in ('az','cz','dt','Tx','df','dF','Ft','ix','xy','iz','ji','jx','fu','red','an') for w in words)
            labelled_formula=bool(re.match(r'^\(\d+\.\d+\.\d+[′\']?\)\s+',p))
            prose_item=bool(re.match(r'^\s*(?:[0-9]+|[A-Za-zαβγ])\)',p))
            if LAYER!='apparatus' and (labelled_formula or (indented and not p.startswith(('Théorème','Theorem','Lemma','Lemme'))) or (onlymath and not prose_item and any(c in p.replace('->','→') for c in '=^_∑Σ→'))):
                out.append(display(p));continue
            styled=labelled_prose(p)
            if styled is not None:
                out.append(r'\noindent '+styled+r'\par');continue
            list_lines=p.splitlines()
            if len(list_lines)>1 and all(re.match(r'^\s*\((?:i{1,3}|iv|v)\)',line) for line in list_lines):
                rendered=r'\\ '.join(prose(line.strip()) for line in list_lines)
            else:rendered=prose(p.replace('\n',' '))
            if LAYER!='apparatus' and re.match(r'^\((?:2\.14|5\.13)\)',p):rendered=r'\emph{'+rendered+'}'
            if LAYER!='apparatus' and italic_paragraph(p):
                rendered=r'{\itshape '+rendered+'}'
            out.append(r'\noindent '+rendered+r'\par')
        finally:
            for index,asset in enumerate(assets):
                marker=asset.get('placement_after')
                if marker and marker in p:
                    out.append(r'\begin{center}\includegraphics[width=.73\linewidth]{'+pathlib.PurePosixPath(asset['presentation_path']).name+r'}\end{center}')
                    asset_hits[index]+=1
    assert all(hits==1 for hits in asset_hits), (LAYER,PAGE,[(assets[i].get('id'),hits) for i,hits in enumerate(asset_hits)])
    return '\n\n'.join(out)

PREAMBLE=r'''\documentclass[10pt,leqno]{article}
\usepackage[a4paper,margin=22mm,headheight=14pt]{geometry}
\usepackage{fontspec}
\setmainfont{Cambria}
\usepackage{amsmath,amssymb,amscd,mathtools}
\makeatletter
\renewcommand{\tagform@}[1]{\maketag@@@{\bfseries(#1)}}
\makeatother
\usepackage{unicode-math}
\setmathfont{Cambria Math}
\usepackage{graphicx,fancyhdr,microtype,seqsplit}
\graphicspath{{../assets/presentation_derivatives/}{./}}
\usepackage[hidelinks]{hyperref}
\setlength{\parindent}{0pt}
\setlength{\parskip}{.4em}
\setlength{\emergencystretch}{3em}
\allowdisplaybreaks
\pagestyle{fancy}\fancyhf{}
\fancyhead[L]{Pierre Deligne}
\fancyhead[R]{La conjecture de Weil. I}
\fancyfoot[C]{\thepage}
\begin{document}
'''

def main():
    global LAYER,PAGE
    texdir=ROOT/'tex';texdir.mkdir(exist_ok=True)
    for LAYER in ('source_language','english_standalone','apparatus'):
        records=[json.loads(s) for s in (ROOT/'edition'/f'{LAYER}.ndjson').read_text(encoding='utf-8').splitlines() if s]
        parts=[PREAMBLE]
        for rec in records:
            PAGE=rec['physical_page']
            if PAGE==1 and LAYER!='apparatus':continue
            if PAGE==2 and LAYER!='apparatus':
                title='LA CONJECTURE DE WEIL. I' if LAYER=='source_language' else 'THE WEIL CONJECTURE. I'
                s=rec['text'].split('\n\n',1)
                rec=dict(rec,text=s[1] if s[0].startswith(('LA CONJECTURE','THE WEIL')) else rec['text'])
                parts.append(r'\begin{center}{\Large\bfseries '+title+r'}\par\medskip '+('par' if LAYER=='source_language' else 'by')+r' PIERRE DELIGNE\end{center}')
            if LAYER=='apparatus' and PAGE==1:parts.append(r'\section*{Separate page-addressed apparatus}')
            if PAGE==29 and LAYER!='apparatus':
                parts.append(r'\begingroup\setlength{\parskip}{.20em}\setlength{\abovedisplayskip}{4pt}\setlength{\belowdisplayskip}{4pt}\setlength{\abovedisplayshortskip}{2pt}\setlength{\belowdisplayshortskip}{2pt}')
            parts.append(r'\phantomsection\label{physical-'+str(PAGE)+'}'+r'\noindent{\footnotesize\color{black} '+('Authority physical page '+str(PAGE)+'; printed '+str(rec['printed_page']) if PAGE>1 else 'Authority physical page 1; repository-cover disposition')+r'}\par\smallskip')
            parts.append(record_text(rec));parts.append(r'\clearpage')
            if PAGE==29 and LAYER!='apparatus':parts.append(r'\endgroup')
        parts.append(r'\end{document}')
        (texdir/f'{LAYER}.tex').write_text('\n\n'.join(parts).replace(r'\color{black}',''),encoding='utf-8',newline='\n')
    ledger=ROOT/'audit'/'MATH_SPAN_LEDGER.ndjson'
    ledger.write_text('\n'.join(json.dumps(x,ensure_ascii=False,sort_keys=True) for x in SPAN_LOG)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'result':'BUILT_FOR_QA_NOT_ACCEPTED','spans':len(SPAN_LOG),'tex_files':3}))

if __name__=='__main__':main()
