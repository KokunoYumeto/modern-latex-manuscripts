"""Literal local-account privacy check over only new/changed public payloads."""
import importlib.util, io, json, os, sys, zipfile
from pathlib import Path
import fitz
path=Path(__file__).with_name('build_d019_integration.py')
spec=importlib.util.spec_from_file_location('builder',path);b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
TEXT={'.json','.tsv','.txt','.md','.tex','.py','.ndjson','.csv','.bib','.yaml','.yml','.log'}
needle=os.environ.get('USERNAME','').casefold()
if not needle:raise b.Failure('no literal privacy target available')
findings=[];count=0

def inspect(name,data):
    global count
    count+=1
    if needle in name.casefold():findings.append({'member':name,'kind':'filename'})
    suffix=Path(name).suffix.casefold()
    if suffix in TEXT:
        if needle in data.decode('utf-8','replace').casefold():findings.append({'member':name,'kind':'text'})
    elif suffix=='.pdf':
        with fitz.open(stream=data,filetype='pdf') as doc:
            if needle in json.dumps(doc.metadata,ensure_ascii=False).casefold() or any(needle in p.get_text().casefold() for p in doc):findings.append({'member':name,'kind':'PDF'})
    elif suffix=='.zip':
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            for info in z.infolist():
                if Path(info.filename).suffix.casefold() in TEXT|{'.pdf','.zip'} or needle in info.filename.casefold():inspect(name+'!/'+info.filename,z.read(info))

def main():
    provenance='--provenance' in sys.argv
    prefix=b.BUILD/'provenance_tree' if provenance else b.SOURCE
    roots=(prefix/'D019',prefix/'integration_audits') if provenance else (b.WORK,b.RECEIPTS)
    paths=[p for root in roots for p in root.rglob('*') if p.is_file()]
    if not provenance:paths += [b.SOURCE/name for name in ('Deligne_EN.tex','Deligne_FR.tex','README.md')]
    for p in paths:
        if p.suffix.casefold() in TEXT|{'.pdf','.zip'} or needle in p.name.casefold():inspect(p.relative_to(prefix).as_posix(),p.read_bytes())
    scope='Only newly assembled D019 provenance and integration_audits; inherited public carrier retained byte-identically without rewriting.' if provenance else 'New D019 payload, new integration receipts, and modified cumulative masters/README; inherited source remains byte-identical to the verified public predecessor.'
    result={'schema':'d019-public-surface-literal-privacy-v1','status':'PASS' if not findings else 'FAIL','scope':scope,'literal_target':'local account name, case insensitive','members_checked':count,'findings':findings,'canonical_source_packet_members_checked':True}
    b.write(b.AUDIT/('PUBLIC_PROVENANCE_PRIVACY.json' if provenance else 'PUBLIC_SURFACE_PRIVACY.json'),result)
    print(json.dumps(result,indent=2))
    if findings:raise b.Failure('literal privacy findings require explicit derivative binding before publication')

if __name__=='__main__':main()
