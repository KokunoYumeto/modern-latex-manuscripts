-- PRIMER EJEMPLO DE PROGRAMACIÓN EN MACAULAY2:
-- DIVISIÓN CON RESTO EN UNA VARIABLE
-- (LA CLASE DE 12/03/2019)
-- http://cadadr.org/san-salvador/2019-groebner/


--------------------------------------------------------
-- División con resto para polinomios en una variable --
--------------------------------------------------------

-- divRem
-- Entrada: f, g
-- Salida: (q,r)

divRem = (f,g) -> (
  q := 0;
  r := f;

  while r != 0 and degree(x,g) <= degree (x,r) do (
    h := x^(degree(x,r)-degree(x,g))*leadCoefficient(r)/leadCoefficient(g);
    q = q + h;
    r = r - h*g
  );
  (q,r)
);

-- Ejemplo:
-- R = QQ[x]
-- divRem (x^6, x^2+1)

-- En la vida real, en lugar de divRem (f,g) hay que usar
-- quotientRemainder (f,g)
-- o los operadores // (cociente) y % (resto).