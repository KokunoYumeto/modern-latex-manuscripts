from pathlib import Path
import subprocess,shutil,os,json,re,fitz
ROOT=Path(__file__).resolve().parents[1]
COMMON=r'''\documentclass[11pt,twoside,leqno]{article}
\usepackage[a4paper,left=22mm,right=22mm,top=22mm,bottom=21mm,headheight=14pt,headsep=12pt,footskip=18pt]{geometry}
\usepackage{fontspec}
\setmainfont{lmroman10-regular.otf}[BoldFont=lmroman10-bold.otf,ItalicFont=lmroman10-italic.otf,BoldItalicFont=lmroman10-bolditalic.otf,SmallCapsFont=lmromancaps10-regular.otf]
\usepackage{amsmath,amssymb}
\usepackage{microtype}
\usepackage{fancyhdr}
\usepackage[unicode,hidelinks]{hyperref}
\newcommand{\leg}[2]{\left(\frac{#1}{#2}\right)}
\newcommand{\md}[1]{\;(\mathrm{mod}.#1)}
\newcommand{\sectionnumber}[1]{\par\vspace{12pt}{\centering #1.\par}\vspace{4pt}}
\newcommand{\sourcefootnote}[1]{\footnote{#1}}
\renewcommand{\thefootnote}{*)}
\setlength{\parindent}{1.5em}
\setlength{\parskip}{0pt}
\setlength{\abovedisplayskip}{6pt plus 1pt minus 1pt}
\setlength{\belowdisplayskip}{6pt plus 1pt minus 1pt}
\setlength{\abovedisplayshortskip}{4pt plus 1pt minus 1pt}
\setlength{\belowdisplayshortskip}{4pt plus 1pt minus 1pt}
\setlength{\jot}{3pt}
\linespread{1.035}
\raggedbottom
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\fancyhead[LE,RO]{\small\thepage}
'''
for lang in ['fr','en']:
 p=ROOT/f'editions/{lang}'
 if lang=='fr':
  ev='RECHERCHES SUR LES DIVISEURS PREMIERS';od="D'UNE CLASSE DE FORMULES DU QUATRIÈME DEGRÉ."
  title="Recherches sur les diviseurs premiers — Paper IV — pp.65–74";imprint="G. Lejeune Dirichlet’s Werke."
 else:
  ev='RESEARCHES ON THE PRIME DIVISORS';od='OF A CLASS OF FORMULAE OF THE FOURTH DEGREE.'
  title='Researches on the prime divisors — Paper IV — pp.65–74';imprint="G. Lejeune Dirichlet’s Works."
 template=COMMON+'\n'+rf'''\fancyhead[CE]{{\fontsize{{8}}{{10}}\selectfont {ev}}}
\fancyhead[CO]{{\fontsize{{8}}{{10}}\selectfont {od}}}
\hypersetup{{pdftitle={{{title}}},pdfauthor={{G. Lejeune Dirichlet}},pdfsubject={{Prompt 01; printed author pp.65–74 only; source-bound edition}}}}
\begin{{document}}
'''
 for page in range(65,75):
  if page>65:template+='\n\\clearpage\n'
  template+=rf'\setcounter{{page}}{{{page}}}\pdfbookmark[0]{{{page}}}{{p{page}}}'+'\n'
  template+='\\fancyfoot{}\n'
  if page in [65,73]:
   template+=rf'\fancyfoot[L]{{\fontsize{{7}}{{9}}\selectfont {imprint}}}'+'\n'
  if page in [65,67,73]:
   sig={65:'9',67:'9*',73:'10'}[page]
   template+=rf'\fancyfoot[C]{{\small {sig}}}'+'\n'
  if page==65:template+='\\fancyhead{}\n'
  if page==66:
   template+=rf'\fancyhead[LE,RO]{{\small\thepage}}\fancyhead[CE]{{\fontsize{{8}}{{10}}\selectfont {ev}}}\fancyhead[CO]{{\fontsize{{8}}{{10}}\selectfont {od}}}'+'\n'
  template+=rf'\input{{pages/p{page:03d}.tex}}'+'\n'
 template+='\\end{document}\n'
 (p/'main.tex').write_text(template,encoding='utf8')
 # Paragraph starts are explicit; editorial comments are not set.
 for pagefile in (p/'pages').glob('*.tex'):
  txt=pagefile.read_text()
  txt=re.sub(r'(% U:[^\n]+\| paragraph-start[^\n]*\n)(?:\\par(?:\\indent)?\n)*',r'\1\\par\\indent\n',txt)
  pagefile.write_text(txt,encoding='utf8')
 receipts=[]
 out=ROOT/f'qa/build/{lang}';out.mkdir(parents=True,exist_ok=True)
 for k in [1,2]:
  cmd=['xelatex','-interaction=nonstopmode','-halt-on-error',f'-output-directory={out}','main.tex']
  proc=subprocess.run(cmd,cwd=p,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,env={**os.environ,'SOURCE_DATE_EPOCH':'1790006400','FORCE_SOURCE_DATE':'1'})
  (out/f'pass{k}.stdout.txt').write_text(proc.stdout,encoding='utf8')
  if (out/'main.log').exists():shutil.copyfile(out/'main.log',out/f'pass{k}.log')
  print(lang,k,proc.returncode,proc.stdout[-500:])
  if proc.returncode:raise RuntimeError('LaTeX error; inspect log and repair')
  receipts.append({'pass':k,'exit_code':proc.returncode})
 reader=ROOT/f'readers/PAPER_IV_{lang.upper()}_PP065_074.pdf';shutil.copyfile(out/'main.pdf',reader)
 doc=fitz.open(reader)
 print(lang,'PAGES',len(doc))
 for n,page in enumerate(doc):
  odir=ROOT/f'qa/visual/{lang}';odir.mkdir(parents=True,exist_ok=True)
  page.get_pixmap(matrix=fitz.Matrix(1.75,1.75),alpha=False).save(odir/f'page{n+1:02d}_p{65+n:03d}.png')
 (out/'BUILD_RUNS.json').write_text(json.dumps({'engine':'XeLaTeX','runs':receipts,'pdf_pages':len(doc)},indent=2)+'\n')
