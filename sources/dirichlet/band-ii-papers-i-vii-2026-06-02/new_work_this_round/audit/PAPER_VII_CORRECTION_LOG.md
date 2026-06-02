# Paper VII correction log

Work item: Dirichlet, Band II Paper VII, “Über einen neuen Ausdruck zur Bestimmung der Dichtigkeit einer unendlich dünnen Kugelschale, wenn der Werth des Potentials derselben in jedem Punkte ihrer Oberfläche gegeben ist.”

The German TeX was checked against the Band II scan rather than against the selected reader. The following corrections are integrated into the delivered TeX/PDF.

- The coefficient in the general density-series term is kept as \((2n+1)^2/(4\pi)^2\) before specialization, and as \((2n+1)^2/(8\pi)\) after setting \(\theta=0\).
- The partial-sum coefficient in §1 is kept as \(1/\pi^2\), with Dirichlet’s variables \(\psi,\gamma\), \(\Pi(\psi)\), \(\Delta\), and \(E\).
- The finite expression at the pole is kept as
  \[
  \rho=\frac1{4\pi}\left[F(\pi)-\int_0^\pi \frac{F'(\gamma)}{\sin(\gamma/2)}\,d\gamma\right].
  \]
- The convergence condition is recorded with \(\sqrt{\varepsilon}F'(c\pm\varepsilon)\), not with \(\varepsilon F'(c+\varepsilon)\).
- In §4 the example is the Band II scan example \(f(\theta)=\sqrt{\cos\theta}\) on the hemisphere and zero on the other half, with Dirichlet’s four-period sign pattern.
- The coefficient
  \[
  A_n=-(-1)^{n(n+1)/2}\frac{2}{(2n-1)(2n+3)}
  \]
  and the corresponding series for \(V\) and \(\rho\) are retained.
- §6 is included, with the reduction for a surface near the sphere, \(r=1+\gamma z\), and the concluding rule of multiplying the prescribed spherical value by \(1+\frac12\gamma z\) and dividing the resulting density by \(1+\frac32\gamma z\).

The cumulative outputs for Papers I-VII have been rebuilt without visible page-marker insertions.
