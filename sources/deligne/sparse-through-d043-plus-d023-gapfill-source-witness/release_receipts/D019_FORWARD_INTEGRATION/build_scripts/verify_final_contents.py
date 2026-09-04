"""Check printed TOC numbers, links, bookmarks and physical page labels."""
import argparse, importlib.util, json, re
from pathlib import Path
path=Path(__file__).with_name('build_d019_integration.py')
spec=importlib.util.spec_from_file_location('builder',path);b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--language',choices=['EN','FR']);args=parser.parse_args()
    result={'schema':'d019-final-contents-convergence-v1','status':'RUNNING','languages':{}}
    for lang in ([args.language] if args.language else ['EN','FR']):
        pdf=b.SOURCE/f'Deligne_{lang}.pdf';parts=b.includes(b.SOURCE,lang,pdf);front=parts[0]['first']-1
        with b.fitz.open(pdf) as doc:
            text='\n'.join(doc[p].get_text() for p in range(1,front))
            lines=text.split('Contents\n' if lang=='EN' else 'Sommaire\n',1)[1].splitlines()
            starts=[i for i,s in enumerate(lines) if re.match(r'^D\d{3}\s',s)]
            if len(starts)!=len(parts):raise b.Failure('contents work count')
            checks=[];links=[link for p in range(1,front) for link in doc[p].get_links() if link['kind'] in (b.fitz.LINK_GOTO,b.fitz.LINK_NAMED) and isinstance(link.get('page'),int)]
            for n,(i,part) in enumerate(zip(starts,parts)):
                end=starts[n+1]-1 if n+1<len(starts) else len(lines)
                segment=[s.strip() for s in lines[i:end] if s.strip()]
                if not segment[-1].isdigit():raise b.Failure('printed contents number extraction')
                printed=int(segment[-1]);work=re.match(r'^(D\d{3})',segment[0]).group(1)
                bookmarks=[r for r in doc.get_toc() if re.match(r'^'+work+r'\b',r[1])]
                matching=[l for l in links if l.get('page')==part['first']-1]
                if work!=part['work'] or printed!=part['first'] or len(bookmarks)!=1 or bookmarks[0][2]!=part['first'] or not matching:raise b.Failure(f'{lang} printed/bookmarked/linked contents mismatch {work}')
                label=doc[part['first']-1].get_label()
                if label not in ('',str(part['first'])):raise b.Failure('nonphysical cumulative page label')
                checks.append({'work':work,'printed_page':printed,'bookmark_page':bookmarks[0][2],'link_targets_verified':len(matching),'physical_page_label':label,'status':'PASS'})
            result['languages'][lang]={'pdf':b.sha(pdf),'pages':len(doc),'frontmatter_pages':front,'checks':checks,'goto_link_count':len(links),'status':'PASS'}
    result['status']='PASS'
    name='FINAL_CONTENTS_CONVERGENCE'+('_'+args.language if args.language else '')+'.json'
    b.write(b.AUDIT/name,result);print(json.dumps(result,ensure_ascii=True,indent=2))
if __name__=='__main__':main()
