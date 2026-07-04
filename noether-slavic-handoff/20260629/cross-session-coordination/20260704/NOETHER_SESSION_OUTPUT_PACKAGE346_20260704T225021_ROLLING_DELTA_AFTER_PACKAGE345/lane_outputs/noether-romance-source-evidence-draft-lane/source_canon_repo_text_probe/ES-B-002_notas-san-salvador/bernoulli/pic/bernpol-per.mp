outputtemplate := "%j.mps";

vardef bernpola (expr x) = 
  (x**2) - x + 1/6
enddef;

vardef bernpolb (expr x) = 
  (x**3) - 3/2*(x**2) + 1/2*x
enddef;

vardef bernpolc (expr x) = 
  (x**4) - 2*(x**3) + (x**2) - 1/30
enddef;

vardef bernpold (expr x) = 
  (x**5) - 5/2*(x**4) + 5/3*(x**3) - 1/6*x
enddef;

vardef bernpole (expr x) = 
  (x**6) - 3*(x**5) + 5/2*(x**4) - 1/2*(x**2) + 1/42
enddef;

verbatimtex
%&latex
\documentclass{article}
\usepackage{amsmath,amssymb}
\usepackage[sc]{mathpazo}
\usepackage[T1]{fontenc}
\begin{document}
etex

beginfig(1)
  n := 50;
  xu := 2cm;
  yu := 6cm;
  capd := 1/40;

  drawarrow (-0.1*xu,0*yu) -- (3.2*xu,0*yu);
  label.lft (btex $B_2 (x - \lfloor x\rfloor)$ etex, (-0.2*xu,0*yu));

  del := 1.0/n;

  for k=0 upto 2:
    draw (k*xu,0.5*bernpola(0)*yu)
    for i=1 upto n:
      .. ((k+del*i)*xu,0.5*bernpola(del*i)*yu)
    endfor withpen pencircle scaled 1pt;
  endfor;

  drawarrow (-0.1*xu,-0.2*yu) -- (3.2*xu,-0.2*yu);
  label.lft (btex $B_3 (x - \lfloor x\rfloor)$ etex, (-0.2*xu,-0.2*yu));

  for k=0 upto 2:
    draw (k*xu,bernpolb(0)*yu - 0.2*yu)
    for i=1 upto n:
      .. ((k+del*i)*xu,bernpolb(del*i)*yu - 0.2*yu)
    endfor withpen pencircle scaled 1pt;
  endfor;

  drawarrow (-0.1*xu,-0.4*yu) -- (3.2*xu,-0.4*yu);
  label.lft (btex $B_4 (x - \lfloor x\rfloor)$ etex, (-0.2*xu,-0.4*yu));

  for k=0 upto 2:
    draw (k*xu,bernpolc(0)*yu - 0.4*yu)
    for i=1 upto n:
      .. ((k+del*i)*xu,bernpolc(del*i)*yu - 0.4*yu)
    endfor withpen pencircle scaled 1pt;
  endfor;

  drawarrow (-0.1*xu,-0.6*yu) -- (3.2*xu,-0.6*yu);
  label.lft (btex $B_5 (x - \lfloor x\rfloor)$ etex, (-0.2*xu,-0.6*yu));

  for k=0 upto 2:
    draw (k*xu,bernpold(0)*yu - 0.6*yu)
    for i=1 upto n:
      .. ((k+del*i)*xu,bernpold(del*i)*yu - 0.6*yu)
    endfor withpen pencircle scaled 1pt;
  endfor;

  drawarrow (-0.1*xu,-0.8*yu) -- (3.2*xu,-0.8*yu);
  label.lft (btex $B_6 (x - \lfloor x\rfloor)$ etex, (-0.2*xu,-0.8*yu));

  for k=0 upto 2:
    draw (k*xu,bernpole(0)*yu - 0.8*yu)
    for i=1 upto n:
      .. ((k+del*i)*xu,bernpole(del*i)*yu - 0.8*yu)
    endfor withpen pencircle scaled 1pt;
  endfor;

  for k=0 upto 3:
    draw (k*xu,-0.9*yu) -- (k*xu,0.2*yu) dashed evenly;
  endfor;

endfig;
verbatimtex
\end{document}
etex
end
