input latexmp;
outputtemplate := "%j.mps";

setupLaTeXMP(class="article",options="11pt",packages="mathpazo");

vardef binc (expr i,j) =
  if (i < 0) or (j < 0):
    0
  elseif i=j:
    1
  else:
    binc (i-1,j-1) + binc (i-1,j)
  fi
enddef;

beginfig(1)
  xu := 60pt;
  yu := 20pt;

  fill (-0.5*xu, -1.5*yu) -- (+0.5*xu, -1.5*yu) -- (+0.5*xu, -2.5*yu) -- (-0.5*xu, -2.5*yu) -- cycle withcolor (0.89,0.88,0.80);

  fill (-1*xu, -2.5*yu) -- (+1*xu, -2.5*yu) -- (+1*xu, -3.5*yu) -- (-1*xu, -3.5*yu) -- cycle withcolor (0.89,0.88,0.80);

  fill (-2*xu, -4.5*yu) -- (+2*xu, -4.5*yu) -- (+2*xu, -5.5*yu) -- (-2*xu, -5.5*yu) -- cycle withcolor (0.89,0.88,0.80);

  fill (-3*xu, -6.5*yu) -- (+3*xu, -6.5*yu) -- (+3*xu, -7.5*yu) -- (-3*xu, -7.5*yu) -- cycle withcolor (0.89,0.88,0.80);

  for i = 0 thru 7:
    for j = 0 thru i:
      label (textext("${" & decimal i & "\choose " & decimal j & "} = " & decimal binc (i,j) & "$"), ((j-i/2)*xu, -i*yu));
    endfor;
  endfor;  
endfig;
end
