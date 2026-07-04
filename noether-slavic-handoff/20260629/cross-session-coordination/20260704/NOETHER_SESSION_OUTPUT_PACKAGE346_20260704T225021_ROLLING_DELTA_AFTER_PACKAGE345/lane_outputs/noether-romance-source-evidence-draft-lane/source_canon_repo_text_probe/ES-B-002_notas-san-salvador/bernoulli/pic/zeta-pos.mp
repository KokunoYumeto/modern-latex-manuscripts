outputtemplate := "%j.mps";

verbatimtex
%&latex
\documentclass{article}
\usepackage{amsmath,amssymb}
\usepackage[sc]{mathpazo}
\usepackage[T1]{fontenc}
\begin{document}
etex

beginfig(1)
  x = 3cm;
  y = 0.5cm;

  drawarrow (0, -0.5*y) -- (0, 11*y);
  draw (1*x, -0.5*y) -- (1*x, 11*y) dashed evenly;
  drawarrow (-0.25*x, 0) -- (4.1*x, 0);
  draw (-0.25*x, 1*y) -- (4.1*x, 1*y) dashed evenly;

  label.bot (btex $s = 1$ etex, (1*x, -0.5*y));
  label.top (btex $\zeta (s)$ etex, (0, 11*y));
  label.rt (btex $s$ etex, (4.1*x, 0));

  draw (1.075*x, 13.915983*y) .. (1.1*x, 10.584448*y) dashed evenly;

  draw (1.1*x, 10.584448*y) ..
       (1.2*x, 5.591582*y) ..
       (1.3*x, 3.931949*y) ..
       (1.4*x, 3.105547*y) ..
       (1.5*x, 2.612375*y) ..
       (1.6*x, 2.285766*y) ..
       (1.7*x, 2.054289*y) ..
       (1.8*x, 1.882230*y) ..
       (1.9*x, 1.749746*y) ..
       (2.0*x, 1.644934*y) ..
       (2.1*x, 1.560217*y) ..
       (2.2*x, 1.490543*y) ..
       (2.3*x, 1.432418*y) ..
       (2.4*x, 1.383343*y) ..
       (2.5*x, 1.341487*y) ..
       (2.6*x, 1.305478*y) ..
       (2.7*x, 1.274265*y) ..
       (2.8*x, 1.247031*y) ..
       (2.9*x, 1.223134*y) ..
       (3.0*x, 1.202057*y) ..
       (3.1*x, 1.183384*y) ..
       (3.2*x, 1.166773*y) ..
       (3.3*x, 1.151945*y) ..
       (3.4*x, 1.138664*y) ..
       (3.5*x, 1.126734*y) ..
       (3.6*x, 1.115989*y) ..
       (3.7*x, 1.106288*y) ..
       (3.8*x, 1.097511*y) ..
       (3.9*x, 1.089552*y) ..
       (4.0*x, 1.082323*y);

endfig;

verbatimtex
\end{document}
etex
end

