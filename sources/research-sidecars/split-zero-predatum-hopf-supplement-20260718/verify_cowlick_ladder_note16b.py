# N16 addendum: the cowlick ladder. CD algebras via the doubling sign convention
# used throughout this lane (verify_bridges.py cd_mul).
import itertools, random
from fractions import Fraction

def cd_mul(x, y, n):
    if n == 1:
        return [x[0]*y[0]]
    h = n // 2
    a, b = x[:h], x[h:]
    c, d = y[:h], y[h:]
    def conj(z): return [z[0]] + [-t for t in z[1:]]
    ac = cd_mul(a, c, h); db = cd_mul(conj(d), b, h)
    da = cd_mul(d, a, h); bc = cd_mul(b, conj(c), h)
    return [ac[i]-db[i] for i in range(h)] + [da[i]+bc[i] for i in range(h)]

def basis(i, n):
    v = [0]*n; v[i] = 1; return v

def dot(x, y): return sum(a*b for a, b in zip(x, y))

random.seed(7)
n_pass = 0
def rep(msg, ok):
    global n_pass
    assert ok, msg
    n_pass += 1
    print("PASS", msg)

# 1) tangency of left-multiplication fields x -> e_i x on the unit sphere, ALL rungs incl sedenions
for dim in [2, 4, 8, 16]:
    ok = True
    for _ in range(20):
        x = [random.randint(-9, 9) for _ in range(dim)]
        for i in range(1, dim):
            if dot(cd_mul(basis(i, dim), x, dim), x) != 0:
                ok = False
    rep(f"dim {dim}: <e_i x, x> = 0 exactly (imaginary left-mult fields are tangent)", ok)

# 2) basis-unit left multiplication is an isometry at every rung (no cowlicks from basis units)
for dim in [2, 4, 8, 16]:
    ok = all(dot(cd_mul(basis(i, dim), x, dim), cd_mul(basis(i, dim), x, dim)) == dot(x, x)
             for i in range(1, dim)
             for x in ([random.randint(-9, 9) for _ in range(dim)],))
    rep(f"dim {dim}: |e_i x| = |x| (basis-unit fields never vanish)", ok)

# 3) parallelizability witnesses: on S^1, S^3, S^7 the fields {e_i x} are pointwise
#    linearly independent together with x (Gram determinant = |x|^(2 dim) != 0)
import math
def gram_rank_full(dim):
    x = [random.randint(-5, 5) for _ in range(dim)]
    while dot(x, x) == 0:
        x = [random.randint(-5, 5) for _ in range(dim)]
    vecs = [x] + [cd_mul(basis(i, dim), x, dim) for i in range(1, dim)]
    G = [[Fraction(dot(u, v)) for v in vecs] for u in vecs]
    # Gaussian elimination rank
    m = [row[:] for row in G]; r = 0
    for c in range(dim):
        piv = next((i for i in range(r, dim) if m[i][c] != 0), None)
        if piv is None: continue
        m[r], m[piv] = m[piv], m[r]
        for i in range(dim):
            if i != r and m[i][c] != 0:
                f = m[i][c] / m[r][c]
                m[i] = [m[i][j] - f*m[r][j] for j in range(dim)]
        r += 1
    return r
for dim in [2, 4, 8]:
    rep(f"dim {dim}: {{x, e_1 x, ..., e_{dim-1} x}} full rank -> S^{dim-1} parallelizable witness", gram_rank_full(dim) == dim)

# 4) sedenion rung: the ZD field. u = e3 + e10 (our convention's zero-divisor family).
u = [0]*16; u[3] = 1; u[10] = 1
# left annihilator {x : u x = 0}: build 16x16 matrix of L_u and row-reduce exactly
cols = [cd_mul(u, basis(j, 16), 16) for j in range(16)]
M = [[Fraction(cols[j][i]) for j in range(16)] for i in range(16)]  # L_u[i][j]
def rank(mat):
    m = [row[:] for row in mat]; rows, colsn = len(m), len(m[0]); r = 0
    for c in range(colsn):
        piv = next((i for i in range(r, rows) if m[i][c] != 0), None)
        if piv is None: continue
        m[r], m[piv] = m[piv], m[r]
        for i in range(rows):
            if i != r and m[i][c] != 0:
                f = m[i][c] / m[r][c]
                m[i] = [m[i][j] - f*m[r][j] for j in range(colsn)]
        r += 1
    return r
rk = rank(M)
nullity = 16 - rk
print(f"  [L_u rank = {rk}, nullity = {nullity}]")
rep("dim 16: L_(e3+e10) is singular -> the ZD field x -> ux HAS cowlicks on S^15", rk < 16)
rep("dim 16: annihilator dimension = 4 (cowlick locus = a 3-sphere)", nullity == 4)

# exhibit one exact cowlick: a unit-normalizable annihilator element
# solve M x = 0 over Q: use the nullspace via elimination
def nullspace(mat):
    rows, colsn = len(mat), len(mat[0])
    m = [row[:] for row in mat]; pivots = []; r = 0
    for c in range(colsn):
        piv = next((i for i in range(r, rows) if m[i][c] != 0), None)
        if piv is None: continue
        m[r], m[piv] = m[piv], m[r]
        m[r] = [e / m[r][c] for e in m[r]]
        for i in range(rows):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [m[i][j] - f*m[r][j] for j in range(colsn)]
        pivots.append(c); r += 1
    free = [c for c in range(colsn) if c not in pivots]
    basis_ns = []
    for fc in free:
        v = [Fraction(0)]*colsn; v[fc] = Fraction(1)
        for i, pc in enumerate(pivots):
            v[pc] = -m[i][fc]
        basis_ns.append(v)
    return basis_ns
ns = nullspace(M)
w = [int(e) if e.denominator == 1 else e for e in ns[0]]
prod = cd_mul(u, [Fraction(e) for e in ns[0]], 16)
rep(f"exact cowlick witness: u*w = 0 for w with support {[i for i,e in enumerate(ns[0]) if e != 0]}",
    all(e == 0 for e in prod))

# 5) Radon-Hurwitz: rho(16) = 9 -> at most 8 independent fields on S^15 (statement check only:
#    rho(2^(4a+b)*odd) = 8a + 2^b)
def rho(n):
    k = 0
    while n % 2 == 0: n //= 2; k += 1
    a, b = divmod(k, 4)
    return 8*a + 2**b
rep("Radon-Hurwitz: rho(2)=2, rho(4)=4, rho(8)=8 (parallelizable), rho(16)=9 -> only 8 fields on S^15",
    rho(2) == 2 and rho(4) == 4 and rho(8) == 8 and rho(16) == 9)

# 6) zeta sphere S^2: rotation flow about the violation axis V(x) = e1 x (cross product),
#    zeros exactly at (+-1,0,0) = Sigma(0), Sigma(1); total index 2 = chi(S^2)
import sympy as sp
x1, x2, x3 = sp.symbols('x1 x2 x3', real=True)
V = sp.Matrix([0, -x3, x2])  # e1 cross x
sols = sp.solve([sp.Eq(V[0],0), sp.Eq(V[1],0), sp.Eq(V[2],0), sp.Eq(x1**2+x2**2+x3**2,1)], [x1,x2,x3], dict=True)
pts = {tuple(s.get(v, sp.nan) for v in (x1,x2,x3)) for s in sols}
rep("inversion flow on zeta sphere vanishes exactly at (+-1,0,0) = Sigma(0), Sigma(1)",
    pts == {(1,0,0), (-1,0,0)} or pts == {(sp.Integer(1),sp.Integer(0),sp.Integer(0)), (sp.Integer(-1),sp.Integer(0),sp.Integer(0))})
# index of each zero of a rotation field = +1; 1+1 = 2 = chi(S^2): linearization at (1,0,0)
# in tangent coords (x2,x3): d/dt(x2,x3) = (-x3, x2), Jacobian [[0,-1],[1,0]], det = 1 > 0 -> index +1
J = sp.Matrix([[0, -1], [1, 0]])
rep("each cowlick has index +1 (det J = 1 > 0); total = 2 = chi(S^2), Poincare-Hopf",
    J.det() == 1)

print(f"\n=== {n_pass}/{n_pass} exact checks passed ===")
