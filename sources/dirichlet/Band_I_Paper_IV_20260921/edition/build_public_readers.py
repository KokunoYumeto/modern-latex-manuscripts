from pathlib import Path
import subprocess,shutil
root=Path(__file__).resolve().parent
target=root/'public_build'
if target.exists():raise SystemExit('Choose a new build directory or archive the previous public_build first.')
for lane,source in [('fr','editions/fr'),('en','editions/en'),('apparatus','apparatus')]:
    dest=target/lane; shutil.copytree(root/source,dest)
    for n in (1,2):
        p=subprocess.run(['xelatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','main.tex'],cwd=dest,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (dest/f'pass{n}.stdout.txt').write_bytes(p.stdout)
        if p.returncode:raise SystemExit(f'{lane}: compilation failed; consult saved output.')
    print(lane, dest/'main.pdf')
