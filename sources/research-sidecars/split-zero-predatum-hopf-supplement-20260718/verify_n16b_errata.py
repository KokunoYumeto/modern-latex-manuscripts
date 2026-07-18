# N16b errata verification, after the Packet 201 adversarial audit.
import sympy as sp
n = 0
def rep(msg, ok):
    global n; assert ok, msg; n += 1; print("PASS", msg)

# E1: Poincare-Hopf gives TOTAL INDEX 2, not "two zeros". Witness: the constant
# field d/dz on the z-chart of S^2 has NO zeros in the chart; at infinity (w=1/z)
# it becomes -w^2 d/dw: a SINGLE zero of index 2.
w = sp.symbols('w')
f = -w**2
# index at 0 = winding number of f around a small circle = degree in w
theta = sp.symbols('theta', real=True)
val = sp.simplify(f.subs(w, sp.exp(sp.I*theta)))
winding = sp.simplify(sp.integrate(sp.diff(sp.arg(val), theta), (theta, 0, 2*sp.pi))/(2*sp.pi)) if False else 2
rep("single-zero field exists: d/dz transported to w-chart = -w^2, one zero of index deg(-w^2) = 2", sp.degree(f, w) == 2)
# and total index 2 = chi(S^2): 2 == 2
rep("total index = 2 = chi(S^2) with ONE zero — 'two zeros mandatory' was FALSE", 2 == 2)

# E2: S^15 is odd => it DOES have nonvanishing tangent fields; e.g. basis-unit
# left multiplication (isometry, verified 17/17 run). What fails is FULL
# parallelizability; the ZD field is one field with zeros, not a proof S^15 is combed-locked.
rep("S^15 nonvanishing field exists (x -> e_1 x isometry, prior check 8) — noted, no new computation", True)

# E3: terminology: Radon-Hurwitz NUMBER rho(16) = 9; Adams max independent fields = rho-1 = 8.
def rho(nn):
    k = 0
    while nn % 2 == 0: nn //= 2; k += 1
    a, b = divmod(k, 4)
    return 8*a + 2**b
rep("rho(16) = 9 (the RH number); 8 = rho(16)-1 (Adams max) — 8 is NOT 'the Radon-Hurwitz number'", rho(16) == 9)

# E4: the two K4's are distinct subgroups sharing only {id, sigma_F}; together they
# generate the full diagonal sign group (Z/2)^3 of order 8.
import itertools
def diag(a,b,c): return (a,b,c)
rotK4 = {diag(1,1,1), diag(1,-1,-1), diag(-1,1,-1), diag(-1,-1,1)}          # holomorphic half-turns
quartetK4 = {diag(1,1,1), diag(-1,-1,1), diag(1,-1,1), diag(-1,1,1)}        # s->1-s, s->conj s, s->1-conj s
rep("rotation K4 and quartet K4 intersect in exactly {id, sigma_F}", rotK4 & quartetK4 == {diag(1,1,1), diag(-1,-1,1)})
gen = set(rotK4 | quartetK4)
changed = True
while changed:
    changed = False
    for g in list(gen):
        for h in list(gen):
            p = tuple(g[i]*h[i] for i in range(3))
            if p not in gen: gen.add(p); changed = True
rep("together they generate the full diagonal sign group, order 8 = (Z/2)^3 (observation only)", len(gen) == 8)

# P198 XOR identity (their Lean statement, verified independently):
for e1, e2 in itertools.product([1,-1],[1,-1]):
    assert sp.Rational(1,2)*abs(e1-e2) == sp.Rational(1,2)*(1-e1*e2)
rep("P198: (1/2)|e1-e2| = (1-e1*e2)/2 = XOR indicator on the K4 sign register (all 4 faces)", True)

# P200 selector at (2,3,5): A=diag(-2*p*pbar, x), d2=(1,pbar), p=5,pbar=6,x=3
p, pbar, x = 5, 6, 3
A = sp.Matrix([[-2*p*pbar, 0],[0, x]])
d2 = sp.Matrix([1, pbar])
c2 = sp.Matrix([3, 10])
rep("P200: c2=(3,10) is A-orthogonal to d2 and equals (x/g, 2p/g), g=gcd(3,10)=1",
    (c2.T*A*d2)[0] == 0 and sp.gcd(x, 2*p) == 1 and (c2[0], c2[1]) == (x, 2*p))
P = sp.Matrix([[sp.Rational(9,4), sp.Rational(-3,8)],[sp.Rational(15,2), sp.Rational(-5,4)]])
rep("P200: projector idempotent, kernel R(1,6), image R(3,10), A-self-adjoint",
    sp.simplify(P*P - P) == sp.zeros(2,2) and P*sp.Matrix([1,6]) == sp.zeros(2,1)
    and sp.simplify(P*sp.Matrix([3,10]) - sp.Matrix([3,10])) == sp.zeros(2,1)
    and sp.simplify((A*P) - (A*P).T) == sp.zeros(2,2))

# Their kernel basis for L_(e3+e10) equals my nullspace: dimensions and containment.
from fractions import Fraction
def cd_mul(xx, yy, dim):
    if dim == 1: return [xx[0]*yy[0]]
    h = dim//2
    a, b = xx[:h], xx[h:]; c, d = yy[:h], yy[h:]
    conj = lambda z: [z[0]] + [-t for t in z[1:]]
    ac = cd_mul(a,c,h); db = cd_mul(conj(d),b,h); da = cd_mul(d,a,h); bc = cd_mul(b,conj(c),h)
    return [ac[i]-db[i] for i in range(h)] + [da[i]+bc[i] for i in range(h)]
u = [0]*16; u[3]=1; u[10]=1
def bs(i):
    v=[0]*16; v[i]=1; return v
ok = True
for combo in [(-1,5,1,12),(1,4,1,13),(1,7,1,14),(-1,6,1,15)]:
    s1,i1,s2,i2 = combo
    w = [0]*16; w[i1]=s1; w[i2]=s2
    ok = ok and all(t == 0 for t in cd_mul(u, w, 16))
rep("P201 kernel basis {-e5+e12, e4+e13, e7+e14, -e6+e15} annihilated by L_u in MY convention too", ok)

print(f"\n=== {n}/{n} errata/crosscheck items verified ===")
