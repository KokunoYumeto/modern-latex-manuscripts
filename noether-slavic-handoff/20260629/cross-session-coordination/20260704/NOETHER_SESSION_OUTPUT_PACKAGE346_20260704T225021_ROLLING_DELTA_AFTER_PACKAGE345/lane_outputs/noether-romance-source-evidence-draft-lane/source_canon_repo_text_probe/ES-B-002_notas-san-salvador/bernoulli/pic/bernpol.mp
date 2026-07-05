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
  xu := 9cm;
  yu := 20cm;
  capd := 1/40;

  drawarrow (0*xu,-1/8*yu) -- (0*xu,(1/6+1/20)*yu);
  draw (1/2*xu,-1/8*yu) -- (1/2*xu,(1/6+1/20)*yu) dashed evenly;
  drawarrow (-0.3*xu,0*yu) -- (1.35*xu,0*yu);
  label.top (btex $B_k (x)$ etex, (0*xu,(1/6+1/20)*yu));
  label.rt (btex $x$ etex, (1.35*xu,0*yu));
  label.bot (btex $x=\frac{1}{2}$ etex, (1/2*xu,-1/8*yu));

  a := -0.01; b := 1.01; del := (b-a)/n;
  draw (a*xu,bernpola(a)*yu)
  for i=1 upto n:
    .. ((a+del*i)*xu,bernpola((a+del*i))*yu)
  endfor;
  label.top (btex $B_2 (x)$ etex, (1.01*xu,bernpola(1.01)*yu));

  a := -0.06; b := 1.06; del := (b-a)/n;
  draw (a*xu,bernpolb(a)*yu)
  for i=1 upto n:
    .. ((a+del*i)*xu,bernpolb((a+del*i))*yu)
  endfor;
  label.top (btex $B_3 (x)$ etex, (1.06*xu,bernpolb(1.06)*yu));

  a := -0.2; b := 1.2; del := (b-a)/n;
  draw (a*xu,bernpolc(a)*yu)
  for i=1 upto n:
    .. ((a+del*i)*xu,bernpolc((a+del*i))*yu)
  endfor;
  label.top (btex $B_4 (x)$ etex, (1.2*xu,bernpolc(1.2)*yu));

  a := -0.3; b := 1.3; del := (b-a)/n;
  draw (a*xu,bernpold(a)*yu)
  for i=1 upto n:
    .. ((a+del*i)*xu,bernpold((a+del*i))*yu)
  endfor;
  label.top (btex $B_5 (x)$ etex, (1.31*xu,bernpold(1.3)*yu));

endfig;
verbatimtex
\end{document}
etex
end
