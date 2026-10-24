"""Build editable Noether LaTeX sources. AI-created: OpenAI Codex, GPT-6 Astra,
Ultra, 2026-10-24. See the edition's localized README for usage and prerequisites.
"""
import argparse,json,os,shutil,subprocess,tempfile
from pathlib import Path,PurePosixPath

HEADER='%% NOETHER EDITABLE LATEX COLLECTION 1\n'
BEGIN='%% BEGIN NOETHER SOURCE '
END='\n%% END NOETHER SOURCE\n'

def unpack(text):
    if not text.startswith(HEADER):raise ValueError('Unsupported source format')
    line,rest=text[len(HEADER):].split('\n',1)
    config=json.loads(line.removeprefix('%% '));files={}
    while rest:
        if not rest.startswith(BEGIN):raise ValueError('Invalid source boundary')
        line,rest=rest.split('\n',1);name=json.loads(line[len(BEGIN):])
        p=PurePosixPath(name)
        if p.is_absolute() or '..' in p.parts or '\\' in name or ':' in name or name in files:
            raise ValueError('Invalid source path')
        content,rest=rest.split(END,1);files[name]=content.encode('utf-8')
    if not config['components'] or any(x not in files for x in config['components']):
        raise ValueError('Missing component')
    return config,files

def write_sources(root,files):
    for name,data in files.items():
        p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)

def compile_sources(root,config,output,engine):
    from pypdf import PdfReader,PdfWriter
    env=os.environ.copy()
    env.update(FORCE_SOURCE_DATE='1',SOURCE_DATE_EPOCH='1788480000',TZ='UTC',MIKTEX_ENABLE_AUTO_INSTALL='0')
    pdfs=[]
    for number,name in enumerate(config['components'],1):
        source=root/name;job='component-'+str(number)
        for passage in range(1,5):
            subprocess.run([engine,'-no-shell-escape','-interaction=nonstopmode','-halt-on-error',
                '-file-line-error','-synctex=0','-jobname='+job,source.name],cwd=source.parent,
                env=env,check=True,timeout=600)
            log=(source.parent/(job+'.log')).read_text('utf-8',errors='replace')
            rerun=any(t in log for t in ['Rerun to get cross-references right','Label(s) may have changed','Rerun to get outlines right'])
            if passage>=2 and not rerun:break
        if rerun:raise RuntimeError('Unresolved cross-references')
        pdf=source.parent/(job+'.pdf');PdfReader(pdf,strict=True);pdfs.append(pdf)
    if len(pdfs)==1:shutil.copyfile(pdfs[0],output)
    else:
        writer=PdfWriter()
        for pdf in pdfs:writer.append(pdf)
        with output.open('wb') as stream:writer.write(stream)
        writer.close()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('source',type=Path);p.add_argument('--output',type=Path)
    p.add_argument('--extract',type=Path);p.add_argument('--engine',default='xelatex')
    a=p.parse_args();config,files=unpack(a.source.read_bytes().decode('utf-8'))
    if a.extract:
        a.extract.mkdir(parents=True,exist_ok=False);write_sources(a.extract,files)
    if a.output:
        output=a.output.resolve()
        if output.exists():raise FileExistsError(output)
        output.parent.mkdir(parents=True,exist_ok=True)
        with tempfile.TemporaryDirectory(prefix='noether-build-',dir=output.parent) as work:
            root=Path(work);write_sources(root,files);compile_sources(root,config,output,a.engine)
    if not a.extract and not a.output:p.error('Specify --output or --extract')

if __name__=='__main__':main()
