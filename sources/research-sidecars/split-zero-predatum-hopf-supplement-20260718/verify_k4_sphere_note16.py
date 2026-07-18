# N16 verification: the K4 sphere. Ponweiser (RISC 2014) Ex 1.41/Rem 1.42 rotations
# composed with the centered map v = 2s-1 (Codex packet JTPKT-20260714-126, our exemplars).
import sympy as sp

x1, x2, x3 = sp.symbols('x1 x2 x3', real=True)
a, b = sp.symbols('a b', real=True)  # v = a + i b
v = a + sp.I*b
n = 0

def rep(msg, ok):
    global n
    assert ok, msg
    n += 1
    print(f"PASS {msg}")

def proj_inv(w):  # inverse stereographic (thesis 1.21) = Sigma_s on v
    w = sp.simplify(w)
    re, im = sp.re(w), sp.im(w)
    d = 1 + re**2 + im**2
    return sp.Matrix([2*re/d, 2*im/d, (re**2+im**2-1)/d])

P = proj_inv(v)

# 1) the three involutions as coordinate half-turns (thesis Ex 1.41, Rem 1.42)
for w, M, name, axis in [
    (1/v, sp.diag(1,-1,-1), 'v->1/v = 180deg about x1 (VIOLATION axis)', 'x1'),
    (-v,  sp.diag(-1,-1,1), 'v->-v (s->1-s, functional eq) = 180deg about x3 (polar axis)', 'x3'),
    (-1/v, sp.diag(-1,1,-1), 'v->-1/v = 180deg about x2', 'x2')]:
    lhs = proj_inv(w).applyfunc(lambda e: sp.simplify(sp.together(e)))
    rhs = (M*P).applyfunc(sp.simplify)
    rep(name, sp.simplify(lhs-rhs) == sp.zeros(3,1))

# conjugation v->conj(v) = reflection x2 -> -x2
lhs = proj_inv(sp.conjugate(v)).applyfunc(sp.simplify)
rep('v->conj(v) = reflection (x1,-x2,x3)', sp.simplify(lhs - sp.Matrix([P[0],-P[1],P[2]])) == sp.zeros(3,1))
# s->1-conj(s): v->-conj(v) = reflection through critical plane x1=0
lhs = proj_inv(-sp.conjugate(v)).applyfunc(sp.simplify)
rep('s->1-conj(s) = reflection (-x1,x2,x3): RH <=> zero images fixed', sp.simplify(lhs - sp.Matrix([-P[0],P[1],P[2]])) == sp.zeros(3,1))

# 2) fixed points on the sphere: the six piercing points
s = sp.symbols('s')
vs = 2*s-1
rep('v->1/v fixes s=0,1 (thesis: inversion fixes {+-1})',
    all(sp.simplify((1/vs - vs).subs(s, val)) == 0 for val in [0,1]))
rep('v->-1/v fixes s=1/2 +- i/2 (on critical line, sphere points (0,+-1,0))',
    all(sp.simplify(( -1/vs - vs).subs(s, val)) == 0 for val in [sp.Rational(1,2)+sp.I/2, sp.Rational(1,2)-sp.I/2]))

# 3) X_s = c_minusplus/(1+|v|^2), c_minusplus = 2(2beta-1) tessarine detector
beta, gam = sp.symbols('beta gamma', real=True)
vv = 2*(beta+sp.I*gam)-1
X = 4*(beta-sp.Rational(1,2))/(1+4*(beta-sp.Rational(1,2))**2+4*gam**2)
c_mp = 2*(2*beta-1)
rep('X_s = c_-+ /(1+|v|^2): compactified tessarine violation detector',
    sp.simplify(X - c_mp/(1+sp.Abs(vv)**2).rewrite(sp.re).expand()) == 0 or
    sp.simplify(X - c_mp/(1+(2*beta-1)**2+4*gam**2)) == 0)

# 4) packet quartet: rho = 18/25 + 3i/4 -> (2200,7500,3609)/8609 and K4 sign orbit
rho = sp.Rational(18,25)+sp.Rational(3,4)*sp.I
pt = proj_inv(2*rho-1).applyfunc(sp.nsimplify)
rep('packet quartet base point (2200,7500,3609)/8609 reproduced',
    pt == sp.Matrix([sp.Rational(2200,8609), sp.Rational(7500,8609), sp.Rational(3609,8609)]))
orbit = {tuple(proj_inv(2*r-1).applyfunc(sp.nsimplify)) for r in [rho, 1-rho, sp.conjugate(rho), 1-sp.conjugate(rho)]}
signs = {(sp.sign(p[0]), sp.sign(p[1])) for p in orbit}
rep('quartet = K4-orbit = all four sign patterns (+-X, +-Y), Z fixed',
    len(orbit) == 4 and len(signs) == 4 and all(p[2] == sp.Rational(3609,8609) for p in orbit))

# critical input: quartet degenerates to a pair (X=0)
rc = sp.Rational(1,2)+sp.Rational(3,4)*sp.I
orbit_c = {tuple(proj_inv(2*r-1).applyfunc(sp.nsimplify)) for r in [rc, 1-rc, sp.conjugate(rc), 1-sp.conjugate(rc)]}
rep('on-critical quartet degenerates to the packet pair (0,+-12/13,5/13)',
    orbit_c == {(0, sp.Rational(12,13), sp.Rational(5,13)), (0, sp.Rational(-12,13), sp.Rational(5,13))})

# 5) X_s invariance: fixed by the violation-axis half-turn, negated by the other two
Pv = proj_inv(1/v)[0]
rep('X_s invariant under v->1/v; negated under v->-v and v->-1/v',
    sp.simplify(Pv - P[0]) == 0 and sp.simplify(proj_inv(-v)[0] + P[0]) == 0
    and sp.simplify(proj_inv(-1/v)[0] + P[0]) == 0)

print(f"\n=== {n}/{n} exact checks passed ===")
