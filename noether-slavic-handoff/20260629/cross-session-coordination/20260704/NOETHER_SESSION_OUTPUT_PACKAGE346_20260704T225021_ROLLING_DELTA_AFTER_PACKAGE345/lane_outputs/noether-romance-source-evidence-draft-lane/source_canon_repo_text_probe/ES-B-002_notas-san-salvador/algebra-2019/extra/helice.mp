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
  u = 1.2cm;

  path helix;

  helix = (0,0.5)*u .. (0.5,0.25)*u .. (1,-0.5)*u .. (0,-1)*u .. (-1,-0.5)*u .. (0,0)*u ..
    (1,-0.5-0.7)*u .. (0,-1-0.7)*u .. (-1,-0.5-0.7)*u .. (0,0-0.7)*u ..
    (1,-0.5-2*0.7)*u .. (0,-1-2*0.7)*u .. (-1,-0.5-2*0.7)*u .. (0,0-2*0.7)*u ..
    (1,-0.5-3*0.7)*u .. (0,-1-3*0.7)*u .. (-1,-0.5-3*0.7)*u .. (0,0-3*0.7)*u ..
    (1,-0.5-4*0.7)*u;

  draw subpath (0,5.55) of helix;
  draw subpath (5.7,8.3) of helix;
  draw subpath (8.45,9.22) of helix;
  draw subpath (9.35, 9.55) of helix;

  draw subpath (9.7,12.3) of helix;
  draw subpath (12.45,13.22) of helix;
  draw subpath (13.35, 13.55) of helix;

  draw subpath (13.7,16.3) of helix;
  draw subpath (16.45,17.22) of helix;
  draw subpath (17.35,17.6) of helix;
  draw subpath (17.8,18) of helix;

  draw fullcircle xscaled (2*u) yscaled (1.2*u) shifted (0,-4*u);

  dotlabel.urt (btex $-1$ etex, (0,0)*u);
  dotlabel.urt (btex $0$ etex, (0,-0.7)*u);
  dotlabel.urt (btex $1$ etex, (0,-2*0.7)*u);
  dotlabel.urt (btex $2$ etex, (0,-3*0.7)*u);

  dotlabel.bot (btex $1$ etex, (0,-3.4)*u);
  dotlabel.bot (btex $-1$ etex, (0,-3.4-1.2)*u);
endfig;
verbatimtex
\end{document}
etex
end
