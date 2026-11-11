# Adapted from the original-language Volume VIII reader assembler by OpenAI GPT-6 Astra.
"""Build one reader from typeset, editable LaTeX components."""
from pathlib import Path
import argparse,json
import fitz

def assemble(root,inputs,output):
    volume=json.loads((root/'volume.json').read_text(encoding='utf-8'))
    assert len(inputs)==len(volume['parts'])
    result=fitz.open();destinations={};native={};ranges=[];links=0
    for part,input_pdf in zip(volume['parts'],inputs):
        source=fitz.open(input_pdf);start=len(result)
        assert len(source)>0 and not source.is_encrypted
        result.insert_pdf(source,links=True,annots=True)
        links+=sum(len(p.get_links()) for p in source)
        for j,page in enumerate(source):
            for link in page.get_links():
                if link['kind']==fitz.LINK_NAMED:
                    result[start+j].insert_link(dict(kind=fitz.LINK_NAMED,**{'from':link['from']},nameddest=part['id']+':'+link['nameddest']))
        for name,d in source.resolve_names().items():
            assert 'page' in d and 0<=d['page']<len(source),(part['id'],name,d)
            value=dict(d,page=d['page']+start)
            destinations[part['id']+':'+name]=value
            if name.startswith('native-'):
                assert name not in native,name
                native[name]=value;destinations[name]=value
        ranges.append(dict(id=part['id'],start=start+1,end=len(result)))
        source.close()
    entries=[]
    for name,d in sorted(destinations.items()):
        x,y=d.get('to',(0,result[d['page']].rect.height));zoom=d.get('zoom',0)
        entries.append(f'{fitz.get_pdf_str(name)} [{result.page_xref(d["page"])} 0 R /XYZ {x:.8f} {y:.8f} {zoom:.8f}]')
    dx=result.get_new_xref();result.update_object(dx,'<< /Names ['+'\n'.join(entries)+'] >>')
    nx=result.get_new_xref();result.update_object(nx,f'<< /Dests {dx} 0 R >>');result.xref_set_key(result.pdf_catalog(),'Names',f'{nx} 0 R')
    toc=[]
    for level,title,leaf in volume['bookmarks']:
        name=f'native-{leaf}'
        assert name in native, name
        toc.append([level,title,native[name]['page']+1])
    result.set_toc(toc,collapse=1)
    result.set_metadata(volume['metadata'])
    if volume.get('continuous_folios'):
        result.set_page_labels([{'startpage':0,'style':'D','firstpagenum':1}])
    result.xref_set_key(result.pdf_catalog(),'PageMode','/UseOutlines')
    output.parent.mkdir(parents=True,exist_ok=True)
    if output.exists():raise FileExistsError(output)
    result.save(output,garbage=4,deflate=True)
    report=dict(pages=len(result),parts=ranges,native_anchors=len(native),destinations=len(destinations),bookmarks=len(toc),source_links=links,output=str(output))
    result.close();return report

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--inputs',type=Path,help='JSON list of typeset component PDF paths');p.add_argument('--output',type=Path,default=Path('Gauss_Werke_VIII.pdf'));args=p.parse_args()
    root=Path(__file__).resolve().parent;volume=json.loads((root/'volume.json').read_text(encoding='utf-8'))
    inputs=json.loads(args.inputs.read_text(encoding='utf-8')) if args.inputs else [str(root/'parts'/part['id']/part['pdf']) for part in volume['parts']]
    print(json.dumps(assemble(root,inputs,args.output.resolve()),ensure_ascii=False))
