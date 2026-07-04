-- divRemMultivar
-- Entrada: f, (f_1, ..., f_s)
-- Salida:  (q_1, ..., q_s), r

divRemMultivar = (f,fs) -> (
  -- pongamos q_1 := 0, ..., q_s := 0:
  q := new MutableList from (#fs : 0);

  r := 0;
  p := f;

  while p != 0 do (
    i := 0;
    divisionoccured := false;

    while i < #fs and divisionoccured == false do (
      if leadTerm(p)%leadTerm(fs#i) == 0 then (
        q#i = q#i + leadTerm(p)//leadTerm(fs#i);
        p   = p - leadTerm(p)//leadTerm(fs#i) * fs#i;
        divisionoccured = true
      )
      else
        i = i+1
    );

    if divisionoccured == false then (
      r = r + leadTerm(p);
      p = p - leadTerm(p)
    )
  );

  (toSequence q, r)
);

-- Ejemplo:
-- R = QQ[x,y, MonomialOrder=>Lex];
-- divRemMultivar (x*y^2 + 1, (x*y + 1, y+1))
-- divRemMultivar (x^2*y + x*y^2 + y^2, (x*y-1, y^2-1))
-- divRemMultivar (x^2*y + x*y^2 + y^2, (y^2-1, x*y-1))
