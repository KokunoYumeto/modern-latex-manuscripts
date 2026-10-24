"""由完整LaTeX排版繁體字著作集。"""
from pathlib import Path
import os,shutil,subprocess
root=Path(__file__).resolve().parent
env=os.environ.copy()
env.update(FORCE_SOURCE_DATE='1',SOURCE_DATE_EPOCH='1788480000',TZ='UTC',MIKTEX_ENABLE_AUTO_INSTALL='0')
for passage in range(2):
    subprocess.run(['xelatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','-file-line-error','-synctex=0','-jobname=component-1','02-noether-zh-Hant.tex'],cwd=root,env=env,check=True)
shutil.copyfile(root/'component-1.pdf',root/'01-noether-zh-Hant-base.pdf')
