-----------------------------------------------
-- Comparación con los cálculos de Macaulay2 --
-----------------------------------------------

testGroebner = (d,R) -> (
  f  := random (d,R); g := random (d,R); h := random (d,R);

  print (f);
  print (g);
  print (h);

  print "groebnerBasis:";
  G := groebnerBasis (ideal (f,g,h));
  print (G);

  print "Nuestra implementación:";
  G' := myGroebner (f,g,h);
  print (G');

  if rank (target G) != rank (target G') then
    return false;

  for i from 0 when i < rank (target G) do
    if G'_(0,i) != G_(0,i)//leadCoefficient (G_(0,i)) then
      return false;

  return true;
);

-- (Cuidado: nuestra implementación es MUY lenta)

-- Ejemplo:
-- testGroebner (3,QQ[x,y])
-- testGroebner (3,ZZ/23[x,y])
