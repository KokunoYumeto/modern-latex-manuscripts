"""Rebuild the three D017 mathematical PDFs from their editable source files.

Usage: python rebuild_readers.py --source sources --output build
Requires Python 3 and XeLaTeX with the packages named in the TeX preambles.
No network, shell escape, publication, or source-file modification is used.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--source',type=Path,default=Path(__file__).parent/'sources')
    parser.add_argument('--output',type=Path,default=Path(__file__).parent/'build')
    parser.add_argument('--xelatex',default='xelatex')
    a=parser.parse_args()
    src=a.source.resolve()
    out=a.output.resolve()
    assert src!=out, 'Build output must not overwrite editable sources.'
    out.mkdir(parents=True,exist_ok=True)
    stems=('D017_FR','D017_EN','D017_Apparatus')
    for stem in stems:
        shutil.copy2(src/(stem+'.tex'),out/(stem+'.tex'))
    if (src/'assets').exists():
        (out/'assets').mkdir(exist_ok=True)
        for file in sorted((src/'assets').glob('*.png')):
            shutil.copy2(file,out/'assets'/file.name)
    env=os.environ.copy()
    env.update(SOURCE_DATE_EPOCH='1577836800',FORCE_SOURCE_DATE='1')
    result={}
    for stem in stems:
        for run in (1,2):
            p=subprocess.run([a.xelatex,'-no-shell-escape','-interaction=nonstopmode',
                              '-halt-on-error',stem+'.tex'],cwd=out,env=env,
                             capture_output=True,text=True,errors='replace')
            (out/f'{stem}.pass{run}.txt').write_text(p.stdout+p.stderr,encoding='utf-8')
            if p.returncode:
                raise RuntimeError(f'{stem}: XeLaTeX pass {run} failed; see build log.')
        log=(out/(stem+'.log')).read_text(encoding='utf-8',errors='replace')
        assert not re.search(r'Overfull|Missing character|Undefined control|^!',log,re.M), stem
        pdf=out/(stem+'.pdf')
        result[pdf.name]={'bytes':pdf.stat().st_size,
                         'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest().upper()}
    (out/'BUILD_RESULT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))

if __name__=='__main__':
    main()
