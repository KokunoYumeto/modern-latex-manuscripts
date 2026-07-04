load "Division.m2";


-----------------
-- S-polinomio --
-----------------

S = (f,g) -> (
  xg := lcm (leadMonomial(f),leadMonomial(g));
  xg//leadTerm(f)*f - xg//leadTerm(g)*g
);


---------------------------------------------
-- Algoritmo de Buchberger, versión básica --
---------------------------------------------

buchberger = fs -> (
  gs := fs;
  changed := true;

  while changed do (
    changed = false;
    gs' := gs;

    for i from 0 to #gs-1 do (
      for j from i+1 to #gs-1 do (
        r := (divRemMultivar (S(gs#i,gs#j), gs))#1;
        if r != 0 and not member(r,gs') then (
          gs' = append(gs',r);
          changed = true
        )
      )
    );

    gs = gs'
  );

  gs
);









----------------------------------------------------------------
-- Una base mínima a partir de una base de Gröbner cualquiera --
----------------------------------------------------------------

minimalizeBasis = gs -> (
  gs = apply (gs, f->f//leadCoefficient(f));
  minimal = false;

  while not minimal do (
    minimal = true;

    for i from 0 when i<#gs and minimal do (
      for j from 0 when j<#gs and minimal do (
        if i != j and leadTerm(gs#i)%leadTerm(gs#j) == 0 then (
          gs = remove(gs,i);
          minimal = false
        )
      )
    )
  );

  gs
);

-----------------------------------------------------------------
-- La base reducida a partir de una base de Gröbner cualquiera --
-----------------------------------------------------------------

reduceBasis = gs -> (
  gsm := new MutableList from minimalizeBasis(gs);
  for i from 0 to #gsm-1 do
    gsm#i = (divRemMultivar (gsm#i, remove(gsm,i)))#1;
  toList gsm
);

--------------------------------------------------------
-- La base de Gröbner reducida para I = (f_1,...,f_s) --
--------------------------------------------------------

myGroebner = fs -> matrix {sort reduceBasis buchberger fs};

-- Ejemplo:
-- R = QQ[x,y,z,MonomialOrder=>GLex];
-- myGroebner (x^5+y^4+z^3-1, x^3+y^3+z^2-1)
-- Para comparar con los cálculos de Macaulay2:
-- groebnerBasis (ideal(x^5+y^4+z^3-1, x^3+y^3+z^2-1))
