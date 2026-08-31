"""Nonpatching cold audit of frozen native D031 output bytes.

This is structural/math-regression evidence, not a substitute for the separately
recorded authority-pixel/translation review. It never writes inside normalized.
"""
from pathlib import Path
import csv, hashlib, json, re
import fitz

BASE=Path(__file__).resolve().parent
NORM=BASE/'normalized'
PAT=re.compile(r'<!-- BEGIN_PAGE physical=(\d+) printed=(\d+) -->\n(.*?)\n<!-- END_PAGE physical=\1 printed=\2 -->',re.S)

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest().upper()
def inventory(root):return {p.relative_to(root).as_posix():sha(p) for p in sorted(root.rglob('*')) if p.is_file()}
def records(p):
    found=list(PAT.finditer(p.read_text(encoding='utf-8')))
    assert [(int(m[1]),int(m[2])) for m in found]==[(i,i+246) for i in range(1,44)]
    return {int(m[1]):m[3] for m in found}
def math(text):
    pattern=re.compile(r'(?<!\\)\$(?!\$)(.*?)(?<!\\)\$|\\\[(.*?)\\\]',re.S)
    return [re.sub(r'\s+','',m[1] if m[1] is not None else m[2]) for m in pattern.finditer(text)]

def main():
    before=inventory(NORM);checks=[]
    identity=json.loads((BASE/'input_identity.json').read_text(encoding='utf-8'))
    for row in identity['state_members']:
        p=BASE/'input_state'/row['path'];assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256']
    checks.append('all20 input members unchanged; authority/comparator/salvage exact identities retained')
    all_records={};counts={};pdfs={};math_deltas={}
    for lang in ['french_diplomatic','english_translation']:
        inp=records(BASE/'input_state/editions'/f'{lang}.md');out=records(NORM/f'{lang}.md');all_records[lang]=out
        deltas=[]
        for page in range(1,44):
            if math(inp[page])!=math(out[page]):deltas.append(page)
        assert deltas==[3,11,15,20,31,37,41],(lang,deltas)
        math_deltas[lang]=deltas
        assert r'C(E) \arrow[ur]' in out[3] and r'C(F) \arrow[dd' in out[3]
        assert r'g\in(\mathbf C)' in out[11] and r'g\in G_{\mathbf C}(\mathbf C)' not in out[11]
        assert r'\langle\mu,z\rangle' in out[15] and '$r$' in out[15]
        assert r'\Gamma\subset G_1(\mathbf Q)^+' in out[20]
        assert r'\Gamma=\rho\widetilde G_0(A)\cap G_1(\mathbf Q)' in out[20]
        assert r"G(k')/\rho\widetilde G(k') \arrow[r] \arrow[d,hook] & G(k)/\rho\widetilde G(k) \arrow[d,hook]" in out[31]
        assert r'\cdots \arrow[u] & \pi_0\pi(T) \arrow[u,equal]' in out[37]
        assert r'\cdots \arrow[r] \arrow[u] & \pi_0\pi(T_F)' in out[37]
        for s in [r"M^0_{\mathbf C}(G_i,G'_i,X_i^+)",r"M^0_{\mathbf C}(\prod G_i,\prod G'_i,\prod X_i^+)",r"M^0_{\mathbf C}(G,G'',X^+)"]:
            assert out[41].count(s)==1
        assert r"M^0(G,G',X^+)" in out[41]
        assert r'r(g\varphi(\gamma))' not in out[16]
        assert r'r(\varphi(\gamma))' in out[16]
        assert r'r_{G,X}(\sigma)' in out[38] and r'r_{G,X}(\sigma)^{-1}' not in out[38]
        assert 'Exposé 389' in out[43] and 'Exposé 339' not in out[43]
        assert 'INSTITUT HAUTES ETUDES SCIENTIFIQUES, BURES-SUR-YVETTE' in out[43]
        assert '2.7.21' in out[43]
        md='\n'.join(out.values());tex=(NORM/f'{lang}.tex').read_text(encoding='utf-8')
        assert '\\begin{verbatim}' not in tex and '\\textbackslash' not in tex
        counts[lang]=dict(tikzcd=md.count(r'\begin{tikzcd}'),tikzpicture=md.count(r'\begin{tikzpicture}'),tags=re.findall(r'\\tag\{([^}]+)\}',md))
        assert counts[lang]['tikzcd']==23 and counts[lang]['tikzpicture']==7 and len(counts[lang]['tags'])==36
        doc=fitz.open(NORM/f'{lang}.pdf');assert len(doc)==43
        for i,p in enumerate(doc):
            assert p.get_text(clip=fitz.Rect(0,800,p.rect.width,p.rect.height)).strip()==str(i+247)
            assert not p.get_images()
        log=(NORM/f'{lang}.log').read_text(encoding='utf-8',errors='replace')
        assert 'Overfull' not in log and 'Missing character' not in log and 'LaTeX Error' not in log
        pdfs[lang]=dict(pages=len(doc),sha256=sha(NORM/f'{lang}.pdf'),bytes=(NORM/f'{lang}.pdf').stat().st_size,native_math_fonts=sorted({font[3] for p in doc for font in p.get_fonts() if any(n in font[3].lower() for n in ['lmmi','lmsy','msbm','rsfs'])}))
        assert pdfs[lang]['native_math_fonts']
    assert counts['french_diplomatic']==counts['english_translation']
    assert 'This problem is essentially equivalent to the one solved by Satake in [11].' in all_records['english_translation'][14]
    for page in range(1,44):
        fr=all_records['french_diplomatic'][page];en=all_records['english_translation'][page]
        assert re.findall(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}',fr,re.S)==re.findall(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}',en,re.S)
        assert re.findall(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}',fr,re.S)==re.findall(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}',en,re.S)
    checks.extend(['exact43 source records and PDF pages per language; printed247-289 no290','native23 TikZ-CD and7 Dynkin diagrams per language; code equality across languages','36 display tags; exact cross-language sequence','only seven explicitly corrected source pages differ mathematically from input','four mandatory inherited fault gates independently asserted plus eight new source correction groups','no raster fallback, raw TeX body, overflow, missing glyph or compile error'])
    for name in ['french_diplomatic','english_translation','apparatus']:
        for ext in ['.tex','.pdf','.md']:
            assert (NORM/f'{name}{ext}').read_bytes()==(BASE/'replay'/f'{name}{ext}').read_bytes(),f'non-deterministic {name}{ext}'
    checks.append('clean two-pass replay TeX/PDF/Markdown exact bytes')
    assert sha(BASE/'input_state_repacked.zip')=='1825E1089B2896F571BDA2AE4E845EED5D81FC05FC6E280192C80ECC2F7EDF64'
    checks.append('inherited full-state deterministic repack reproduces original ZIP SHA256')
    after=inventory(NORM);assert before==after
    receipt=dict(status='PASS_NONPATCHING_STRUCTURAL_MATH_REGRESSION_AUDIT',source_pixel_audit_required_separately=True,input_state_unchanged=True,normalized_before=before,normalized_after=after,math_changed_pages=math_deltas,pdf=pdfs,counts=counts,checks=checks,inherited_salvage='ZERO_ACCEPTED')
    (BASE/'cold_audit.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(status=receipt['status'],checks=len(checks),page_count_per_language=43)))

if __name__=='__main__':main()
