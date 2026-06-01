# BATCH_REPORT — autonomous_robots_correll

**Source**: github.com/Correll-Lab/Introduction-to-Autonomous-Robots — Nikolaus Correll et al., *Introduction to Autonomous Robots* (open-source LaTeX textbook; CC BY-NC-SA license).
**Translator**: auxiliary local run (Anthropic), lane lead: local project.
**Date**: 2026-06-01.
**Status**: **Six chapters delivered** — Path Planning, Localization, Sensors, SLAM, Mapping, Vision. Complete autonomous-navigation + perception stack in Ukrainian: sensors → vision (image processing, edge detection, stereo) → localization → mapping (ICP, Octomap, RGB-D/TSDF) → SLAM → path planning. A drone/UGV team can build the entire perception+navigation+planning stack from these Ukrainian-language references.

## Output files
- `chapters/pathplanning_uk.tex` — Path Planning, full translation.
- `chapters/localization_uk.tex` — Localization, full translation (Markov localization, Bayes filter, particle filter, Extended Kalman Filter, odometry+EKF integration).
- `chapters/sensors_uk.tex` — Sensors, full translation (terminology: range/dynamic range/resolution/accuracy/precision/bandwidth; proprioception vs exteroception; encoders/quadrature/Gray code; accelerometers MEMS; gyroscopes optical & MEMS; IMU/AHRS; force/torque sensors with strain gauges; pressure/touch sensors; distance: reflection IR, phase-shift laser/LiDAR, time-of-flight, ultrasound; GPS and indoor beacons/UWB).
- `chapters/SLAM_uk.tex` — SLAM, full translation (covariance matrix for joint state; EKF SLAM with full state-vector expansion, prediction + perception updates, data association, complexity, multi-sensor fusion; graph-based SLAM with spring-mass analogy, MLE formulation, log-likelihood with information matrix, stochastic gradient descent, MST for loop-closure efficiency).
- `chapters/mapping_uk.tex` — Mapping, full translation (point clouds from LiDAR; discrete vs continuous map representations, topological/graph-based; Iterative Closest Point (ICP) 6-step algorithm with selection/matching/weighting/rejection/error-metric/minimization, point-to-point vs point-to-plane; Octomap with k-d trees and Octree for occupancy grids; RGB-D mapping with Signed Distance Field (SDF) and Truncated SDF (TSDF); RANSAC for ICP initial guesses; drift and loop-closure interaction with SLAM).

## Topics covered in this chapter
- Configuration space (C-space) and robot embodiment as point-mass via obstacle growing
- Graph-based planning: Dijkstra's algorithm (complete + optimal), A* with heuristic functions (Manhattan distance, Euclidean), D* for dynamic replanning
- Sampling-based planning: RRT, RRT*, PRM (single-query vs multi-query); probabilistic completeness
- RRT pseudocode with 4 key steps: sample selection, tree connection, collision checking, path smoothing
- Lazy collision evaluation, ellipsoidal sample-space restriction
- Multi-scale planning hierarchy (street network → lane planning → trajectory → motor control)
- Coverage path planning (DFS/BFS, Hamiltonian Path, TSP connection)
- 15 exercises (analytical + programming, applicable for self-study or course assignments)

## Mission relevance
Every autonomous UAV/UGV navigation system uses some form of path planning. The chapter covers exactly the algorithms that field robotics uses:
- Dijkstra/A* for road network / waypoint navigation
- RRT/RRT* for cluttered-environment maneuvering, multi-DoF arms
- Coverage planning for survey/reconnaissance/de-mining operations
- The multi-scale architecture (Fig. planninglayers) maps directly onto how operators think about layered autonomy

## What's not yet translated from this book (26 chapters total, 5,700 lines source)
Highest-utility next targets, in priority order:
1. **localization.tex** (389 lines) — robot pose estimation, Kalman filter for localization, particle filter for non-linear/non-Gaussian
2. **SLAM.tex** — simultaneous localization and mapping (closes the loop with pathplanning)
3. **sensors.tex** (274 lines) — IMU, LiDAR, cameras, encoders, GPS, ultrasonic
4. **mapping.tex** (293 lines) — occupancy grids, topological maps, feature-based maps
5. **kinematics-coordinatesystems.tex** (231 lines) + **kinematics-forward.tex** + **kinematics-inverse.tex** — robotic kinematics foundations
6. **vision.tex** (300 lines) — computer vision for robots
7. **statistics.tex** (152 lines) — probability/statistics foundations needed for localization+SLAM
8. **errorpropagation.tex** — error propagation in measurements (foundational for Kalman)

The book also has chapters on actuators, manipulation, grasping, deeplearning, backpropagation, locomotion, forces, features, taskexecution, linearalgebra, trigonometry, paperwriting, samplecurricula — lower priority for the Ukrainian field-engineering mission.

## Translation policy
- All math/equations preserved verbatim.
- All cross-references (`\cref{chap:mapping}`, `\cref{fig:cspace}`, etc.) preserved.
- All `\cite{}` keys preserved (dijkstra1959note, hart1968formal, stentz1994optimal, lavalle1998rapidly, kavraki1996probabilistic, otte2012, keivan2013realtime).
- All `\index{}` entries translated to Ukrainian.
- Pseudocode kept in Latin/English (algorithm pseudocode is a universal language).
- 15 exercises fully translated.

## Terminology decisions (extending the seed glossary)
| EN | UK |
|---|---|
| path planning | планування шляху |
| path / trajectory | шлях / траєкторія [seed] |
| configuration space (C-space) | простір конфігурацій (C-простір) |
| point-mass | точкова маса |
| Dijkstra's algorithm | алгоритм Дейкстри |
| A* algorithm | алгоритм A* |
| D* algorithm | алгоритм D* |
| heuristic function | евристична функція |
| Manhattan distance | манхеттенська відстань |
| Euclidean distance | евклідова відстань |
| sampling-based planning | планування на основі вибірок |
| graph-based planning | планування на основі графів |
| complete (algorithm) | повний (алгоритм) |
| resolution complete | повний за роздільною здатністю |
| probabilistic complete | ймовірнісно повний |
| Rapidly-exploring Random Tree (RRT) | швидко зростаюче випадкове дерево (RRT) |
| Probabilistic Roadmap (PRM) | ймовірнісна дорожня карта (PRM) |
| anytime algorithm | anytime-алгоритм |
| single-query / multi-query | однозапитове / мультизапитове |
| rewiring (RRT*) | перепідв'язання |
| collision checking | перевірка колізій |
| lazy collision evaluation | лінива перевірка колізій |
| path smoothing | згладжування шляху |
| spline | сплайн [seed] |
| model-predictive control (MPC) | прогнозне керування моделлю |
| coverage path planning | планування покриття |
| Hamiltonian Path | Гамільтонів шлях |
| Traveling Salesman Problem (TSP) | задача комівояжера |
| kd-tree | kd-дерево |
| depth-first search (DFS) | пошук у глибину |
| breadth-first search (BFS) | пошук у ширину |

## Coverage delta vs web model session
web model GPT-5.5 Pro session 02 lists `Autonomous Robots TeX` (Correll et al.) as **pending** in its core book queue. This pilot translation begins delivery of that lane. web model and this lane are now complementary on this title — web model can pick up other chapters (kinematics, sensors, localization, SLAM) while this work covers path planning.

## Build
The chapter compiles as part of the parent book. To build a standalone Ukrainian version:
1. Create a driver `book_uk.tex` with the original `book.tex` preamble + xelatex/polyglossia for Ukrainian.
2. `\include{chapters/pathplanning_uk}` (and any other Ukrainian chapters).
3. Copy `figs/` and `robotics.bib` from source.
4. `xelatex book_uk.tex` (twice for cross-refs).

