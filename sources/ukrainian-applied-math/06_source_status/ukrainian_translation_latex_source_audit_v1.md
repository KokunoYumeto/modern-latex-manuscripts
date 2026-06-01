# Ukrainian Applied-Math Translation: LaTeX / Source / OCR Audit v1
Date: 2026-05-31
Scope: local Ukrainian applied-math packet, `ukies1.zip`, `ukies2.zip`, plus quick web/preprint source search for LaTeX-ready or source-backed substitutes.
## Bottom line
- The three Ukraine-priority ZIPs contain **no `.tex`, `.sty`, `.cls`, or `.bib` files**. They are PDF/DJVU/RAR working sources only.
- Most packet PDFs have good extractable text and can be converted to TeX with controlled repair. The major local failures are **Blackman & Popoli**, **McCoy**, the scanned **Lyons DSP** copy, and the **DJVU** files unless `djvutxt`/OCR is added.
- The cleanest immediate true TeX target is **Zuazua, arXiv:2402.17894**.
- For fast source-backed Ukrainian material, add GitHub/Jupyter/LaTeX sources: **Kalman and Bayesian Filters in Python**, **Introduction to Autonomous Robots**, **Open Optimization OR Book**, **Langtangen–Mardal FEM**, **Benoit Dionne PDE notes**, **Peeter Joot antenna notes**, and selected arXiv review/tutorial papers.
## Local ZIP source inventory
| ZIP | LaTeX found? | Notes |
|---|---:|---|
| Ukrainian Applied Mathematics Translation Priority Packet 20260531.zip | 0 | 16 PDFs + queue CSV/MD only |
| ukies1.zip | 0 | PDFs/DJVU/RAR only |
| ukies2.zip | 0 | PDFs/DJVU only |
| 04_ega_community_translation_repo_style_snapshot.zip | 74 TeX-like files | useful for pure EGA/SGA style, not Ukraine applied lane |
| stacks-project-master.zip | 122 TeX-like files | excellent LaTeX source, but algebraic geometry, not current applied priority |

## OCR/text-extraction audit, local priority files
Status is based on sampled text extraction across front/middle/back pages using PyMuPDF. Full CSV: `ukrainian_priority_source_ocr_audit_v1.csv`.
| Status | Files |
|---|---|
| GOOD digital/OCR text extraction | 01 The Fourier Transform and its Applications.pdf (428 pp, 2078.3 chars/page sample); 02 Exact Controllability and Stabilization of the Wave Equation.pdf (129 pp, 1835.0 chars/page sample); 04 The Princeton Companion to Applied Mathematics.pdf (1032 pp, 3139.6 chars/page sample); 06 High Dimensional Statistics A Non Asymptotic Viewpoint.pdf (571 pp, 1923.5 chars/page sample); 07 Spectral and Algebraic Graph Theory.pdf (400 pp, 1606.0 chars/page sample); 08 Lattice Rules Numerical Integration Approximation and Discrepancy.pdf (584 pp, 1972.5 chars/page sample); 09 Continuous Parameter Markov Processes and Stochastic Differential Equations.pdf (502 pp, 2790.8 chars/page sample); 10 Foundations of Data Science.pdf (486 pp, 2364.3 chars/page sample); 11 Partial Differential Equations Modeling Analysis and Numerical Approximation.pdf (403 pp, 1873.3 chars/page sample); 12 Spectral and Spectral Element Methods for Fractional Ordinary and Partial Differential Equ.pdf (740 pp, 1888.8 chars/page sample); 13 Linear Systems Signal Processing and Hypercomplex Analysis.pdf (320 pp, 1686.4 chars/page sample); 14 Semirings Automata Languages Linear Algebra.pdf (99 pp, 1747.0 chars/page sample) + 14 more |
| USABLE extraction, verify math/layout | 03 Algorithms for Optimization.pdf (621 pp, 1422.0 chars/page sample); 05 Princeton Lectures in Analysis Volumes I IV.pdf (1589 pp, 1261.7 chars/page sample); Small Unmanned Aircraft Theory and Practice (Randal W. Beard  Timothy W. McLain).pdf (317 pp, 1471.6 chars/page sample); Strapdown Inertial Navigation Technology (Titterton, David H. Weston, John L.).pdf (462 pp, 1447.5 chars/page sample); Aircraft control and simulation  dynamics, controls design, and autonomous systems (Brian L. Stevens, Frank L. Lewis etc.).pdf (764 pp, 1225.7 chars/page sample); Introduction to Probability Models (Sheldon M. Ross) (z-library.sk, 1lib.sk, z-lib.sk).pdf (816 pp, 1442.6 chars/page sample); Liapunov Functions and Stability in Control Theory.pdf (245 pp, 1485.7 chars/page sample); Mathematical Techniques in Multisensor Data Fusion, Second Edition (David L. Hall, Sonya A.H. McMullen) (.pdf (458 pp, 1279.7 chars/page sample); Microwave Engineering (David M. Poza.pdf (756 pp, 1483.5 chars/page sample) |
| DJVU: local text not audited; needs djvutxt/OCR or replacement source | Proakis J., Salehi M. Digital Communications.djvu ( pp, 0.0 chars/page sample); goodfellow_ian_bengio_yoshua_courville_aaron_deep_learning_b.djvu ( pp, 0.0 chars/page sample) |
| POOR/none; scan or malformed text, needs OCR or source replacement | Samuel Blackman, Robert Popoli. Design and Analysis of Modern Tracking Systems.pdf (2517 pp, 0.0 chars/page sample); Understanding Digital Signal Processing (RICHARD G.LYONS).pdf (270 pp, 0.0 chars/page sample); Modern Exterior Ballistics (Robert L. McCoy.pdf (326 pp, 0.0 chars/page sample) |

## Source candidates and actions
| Priority | Lane | Target | Source status | Action |
|---|---|---|---|---|
| P0 | PDE/control | Zuazua, Exact Controllability and Stabilization of the Wave Equation | arXiv TeX source likely available; arXiv HTML exists / arXiv:2402.17894 | Fetch e-print source tarball first; use as first true TeX translation target. |
| P0 | signal/Fourier | Osgood, The Fourier Transform and its Applications | Stanford PDF/SEE course materials; no public TeX source found in quick search / Stanford SEE EE261 PDF/course page | Use pdftotext/Mathpix-style extraction or manual TeX reconstruction; OCR not a blocker. |
| P0 | state estimation | Labbe, Kalman and Bayesian Filters in Python | GitHub Jupyter-book source; PDF template includes LaTeX conversion route / rlabbe/Kalman-and-Bayesian-Filters-in-Python | Use as fast Ukrainian training text for Kalman/Bayesian filtering; translate notebooks/Markdown, not TeX. |
| P0 | state estimation/robotics | Barfoot, State Estimation for Robotics, 2nd ed draft | author PDF draft; no public TeX found / Barfoot author draft PDF | Use as reference; do not assume redistribution rights. Extract PDF text if needed. |
| P0 | state estimation/robotics | Solà–Deray–Atchuthan, A micro Lie theory for state estimation in robotics | arXiv TeX/source candidate / arXiv:1812.01537 | Fetch e-print source; excellent compact replacement/supplement for Lie groups in SLAM/VIO. |
| P1 | robotics/autonomy | Introduction to Autonomous Robots | GitHub LaTeX source; book.tex and chapter .tex files; CC BY-NC-ND / Introduction-to-Autonomous-Robots/Introduction-to-Autonomous-Robots | High-value LaTeX-ready robotics source: kinematics, sensors, localization, path planning, SLAM. |
| P1 | robotics/control | Tedrake, Underactuated Robotics | GitHub/source-backed course text; not plain book LaTeX / RussTedrake/underactuated | Use for source-backed control/robotics modules; check license and format before translation. |
| P1 | robot motion planning | LaValle, Planning Algorithms | official free PDF/HTML chapter PDFs; no public TeX source found / lavalle.pl/planning | Use PDF extraction. For TeX-ready alternatives, use arXiv planning papers and open robotics texts. |
| P1 | motion planning/recent papers | Universal Plans: One Action Sequence to Solve Them All | arXiv TeX/source candidate / arXiv:2407.02090 | Useful recent planning theory supplement; not a core textbook. |
| P1 | motion planning/recent papers | Graph-based Path Planning with Dynamic Obstacle Predictions | arXiv HTML/source candidate / arXiv:2504.12616 | Recent path-planning supplement; translate only non-operational planning math. |
| P1 | motion planning/recent papers | BIT*: Sampling-based Optimal Planning via Implicit Random Geometric Graphs | arXiv source candidate / arXiv:1405.5848 | Good algorithmic planning paper; translate as selected module if planning lane starts. |
| P1 | computer vision | Szeliski, Computer Vision: Algorithms and Applications | official PDF via author site; no public LaTeX source found / szeliski.org/Book | Use local/existing PDF extraction; source not a blocker. |
| P1 | computer vision/multiview | Hartley–Zisserman, Multiple View Geometry | publisher/PDF; no public TeX source found / VGG code exists; book source not found | Use PDF extraction and VGG code as support, not a source-text replacement. |
| P1 | sensor fusion/recent survey | A Survey of Multi-sensor Fusion Perception for Embodied AI | arXiv HTML/source candidate / arXiv:2506.19769 | Recent review; good glossary/topic-map source for sensor fusion. Check length and safety framing. |
| P1 | event/sensor fusion/recent survey | Event-based Sensor Fusion and Application on Odometry | arXiv HTML/source candidate / arXiv:2410.15480 | Good recent source for event cameras + IMU/LiDAR odometry. |
| P1 | statistics/filtering | Särkkä & Svensson, Bayesian Filtering and Smoothing, 2nd ed | free author PDF; no public TeX found / Aalto author PDF 2023 | Use PDF extraction/reference; concise and mathematically clean. |
| P1 | statistics/filtering robust | Robust Bayesian Filtering and Smoothing Using Student's t Distribution | arXiv source candidate / arXiv:1703.02428 | Good focused paper for robust filtering/outliers; source likely available from arXiv. |
| P2 | operations research | Open Optimization OR Book | GitHub source for LP/IP/NLP with Python/Julia examples / open-optimization/open-optimization-or-book | Strong LaTeX/source-ready replacement/supplement for Hillier where public source matters. |
| P2 | optimization | Kochenderfer & Wheeler, Algorithms for Optimization | book source not found; official ancillary notebooks/figure code/slides exist / algorithmsbooks/algforopt-notebooks, optimization-ancillaries, algforopt-slides | Use PDF extraction for prose; use notebooks/slides/code for examples and consistency. |
| P2 | optimization | Tufte Algorithms Book Template | LaTeX template used for Algorithms for Optimization; GitHub / sisl/tufte_algorithms_book | Useful typesetting scaffold for Ukrainian applied-math booklets. |
| P2 | convex optimization | Boyd & Vandenberghe, Convex Optimization | official free PDF; example/figure code public; no book TeX / stanford.edu/~boyd/cvxbook | Use as reference; not a TeX source. |
| P2 | PDE/numerics | Benoit Dionne PDE lecture notes | GitHub LaTeX source / BenoitDionne/PDE | Source-ready PDE replacement/supplement; check level and license. |
| P2 | finite elements/numerics | Langtangen–Mardal, Introduction to Numerical Methods for Variational Problems | GitHub source/resources; free PDF / hplgit/fem-book | High-value source-ready FEM/numerical PDE target. |
| P2 | RF/antenna | Peeter Joot ECE1229 Advanced Antenna Theory notes | GitHub LaTeX source / peeterjoot/ece1229-antenna | Potential LaTeX-ready substitute/supplement for Balanis antenna theory; check license and scope. |
| P2 | DSP | Think DSP, 2nd edition | GitHub notebook/book source; Python focus / AllenDowney/ThinkDSP2 | Practical source-backed DSP supplement; not as rigorous as Osgood but faster to translate/adapt. |
| P2 | SDR/comms | Software Defined Radio for Engineers / SDR For Engineers | free book/code repositories; no book TeX confirmed / sdrforengineers GitHub organization | Use code/labs as support; not a direct TeX source replacement. |
| P3 | data science/ML | Probabilistic Machine Learning book series | GitHub source/release ecosystem; Jupyter/HTML/PDF, MIT license for repo / probml/pml-book | Useful for ML/probability source-backed reference; not first battlefield-practical lane. |
| P3 | ML math | Mathematics for Machine Learning | GitHub companion notebooks; official PDF; source for notebooks, not full TeX book / mml-book/mml-book.github.io | Use as terminology/reference for linear algebra/PCA/Gaussian models. |
| HOLD | tracking/ballistics | Blackman & Popoli, Modern Tracking Systems | no public TeX found / local PDF only | Do not public-queue; OCR or replacement source only for authorized controlled review. |
| HOLD | ballistics | McCoy, Modern Exterior Ballistics | no public TeX found / local PDF only | Do not public-queue. Requires OCR if used under controlled review. |
| HOLD | missile guidance | Zarchan, Tactical and Strategic Missile Guidance | no public TeX found / local PDF only | Do not public-queue; if used, restrict to non-operational glossary/math foundations. |

## arXiv source fetch pattern
Use this pattern on a machine with internet access. ArXiv e-print downloads may be a gzipped TeX source tree or, for PDF-only submissions, a PDF. Always inspect before assuming it is TeX.
```bash
for id in 2402.17894 1812.01537 2506.19769 2410.15480 1703.02428 2504.12616 2407.02090 1405.5848; do
  mkdir -p "arxiv_$id"
  curl -L "https://arxiv.org/e-print/$id" -o "arxiv_$id/source"
  file "arxiv_$id/source"
  tar -tf "arxiv_$id/source" 2>/dev/null | head -40 || true
done
```

## Immediate recommendation
Start with source-backed modules, not scans: Zuazua TeX; Labbe notebooks for Kalman filtering; Introduction to Autonomous Robots LaTeX chapters for path planning/localization/SLAM; Open Optimization OR Book for LP/IP/NLP; FEM/PDE open LaTeX notes for numerical infrastructure. Use Osgood/Szeliski/LaValle/Spielman PDFs because their text extraction is already strong. Avoid spending compute on Blackman/McCoy OCR unless a controlled institutional review lane explicitly requires it.
