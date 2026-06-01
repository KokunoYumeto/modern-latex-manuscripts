# BATCH_REPORT — roth_robust_filter_1703.02428

**Source**: arXiv:1703.02428 — M.~Roth, T.~Ardeshiri, E.~Özkan, F.~Gustafsson, *Robust Bayesian Filtering and Smoothing Using Student's $t$ Distribution* (2017). Linköping University / Cambridge / METU.
**Translator**: auxiliary local run (Anthropic), lane lead: local project.
**Date**: 2026-06-01.
**Status**: **Focused translation** of practically-actionable sections — Abstract, Introduction, key results on Student's $t$ distribution (§2), filtering problem setup (§3), full $t$-filter algorithm (§4.1), drone tracking simulation example (§7.2), Concluding remarks (§8). Deferred: deeper theoretical sections (§3 exact filtering analysis, §4.2-4.4 approximation quality with KLD diagrams, §5 algorithmic extensions, §6 $t$-smoother backward pass, appendices A-B).

## Why this paper is mission-relevant
The $t$-filter is the **most practically usable algorithm** for any Kalman/EKF system operating in the presence of:
- **Sensor outliers** — broken/intermittent GPS, multipath errors, camera misdetections in dense foliage or smoke, radar ghost targets.
- **Target maneuvers** — sudden accelerations/turns that violate constant-velocity assumptions in tracking filters.
- **Linearization errors** — heavy-tailed effective process noise in extended/unscented Kalman filters.

Crucially: the $t$-filter equations are **structurally identical** to Kalman filter equations, with one extra scalar multiplier applied to the covariance update after the standard $P_{k|k} = P_{k|k-1} - K_k S_k K_k^T$ step. An existing KF/EKF implementation can be retrofitted to a $t$-filter by adding ~10 lines of code. This is the lowest-friction robustness upgrade available for state-estimation software.

The paper validates the approach with a **drone tracking simulation** (Section 7.2): 4D state (position+velocity), camera-based position measurements, maneuvers at k=25,75,125 and outliers at k=50,100. The $t$-filter recovers from both faster than the nominal KF, approaching the performance of a "clairvoyant" KF that knows when maneuvers/outliers occur (which a real system cannot know).

## Output file
- `ms_uk.tex` — consolidated single-file Ukrainian version with preserved math macros (\k, \kk, \kp, \kpk, \kkm, \xh, \N, \G, \St, \KL, etc.) and equation labels (eq:tDens, eq:tDensCond, eq:assumedStateProcessNoise, eq:tFilterMeas, eq:tFilterScaling, etc.).

## Translation policy
- All math notation, equation labels, citation keys (\cite{kailath_linear_2000}, \cite{sarkka_bayesian_2013}, \cite{roth_students_2013}, etc.) preserved verbatim.
- Author block, affiliations, ORCIDs kept in Latin.
- Algorithm names (Kalman filter, Rauch-Tung-Striebel smoother, IMM, KLD) translated with English in parens for first use where helpful.
- All system models, gain matrices, conditional density formulas preserved character-for-character.

## Key terminology
| EN | UK |
|---|---|
| Student's $t$ distribution | розподіл Стьюдента~$t$ |
| robust Bayesian filtering | стійке байєсівське фільтрування |
| heavy-tailed | важкохвостовий (з важкими хвостами) |
| outlier | викид |
| measurement outlier | викид вимірювання |
| maneuver | маневр |
| Kalman filter (KF) | фільтр Калмана (KF) |
| Rauch–Tung–Striebel (RTS) smoother | згладжувач Рауха–Тунґа–Штрібеля (RTS) |
| state-space model | просторово-станова модель |
| process noise / measurement noise | процесний / вимірювальний шум |
| degrees of freedom | ступені свободи |
| scale matrix | матриця масштабу |
| covariance matrix | коваріаційна матриця |
| moment matching | узгодження моментів |
| Kullback-Leibler divergence (KLD) | розбіжність Кульбака–Лейблера (KLD) |
| elliptically contoured distribution | еліптично-контурний розподіл |
| latent variable | скрита (latent) змінна |
| Gaussian mixture | гаусівська суміш |
| transition density / likelihood | перехідна щільність / правдоподібність |
| Bayesian filtering / smoothing / prediction | байєсівське фільтрування / згладжування / прогнозування |
| recursive Bayesian solution | рекурсивна байєсівська постановка |
| target tracking | супровід цілі |
| unmanned aerial vehicle (UAV) | безпілотний літальний апарат (БПЛА) |
| residual / innovation | залишок / інновація |
| gain matrix | матриця підсилення |
| backward pass | обернений прохід |
| gating | гейтування |

## What's not translated (recommended next pass)
- §2.2-2.3 (elliptically contoured distributions deep dive — academic)
- §3.3 (exact filtering for $t$ noise — theoretical, shows lack of closed-form recursion)
- §3.4 (scalar example with point-mass filter/smoother numerical comparison)
- §4.2-4.4 (joint $t$-density approximation analysis with KLD diagrams, marginal matrix-parameter adjustment, moment matching vs KLD comparison)
- §5 (algorithmic properties: minimum-variance optimality inheritance, square-root implementation, Monte Carlo for nonlinear models)
- §6 (full $t$-smoother backward pass derivation)
- §7.1 (scalar example revisited)
- Appendices A (quadratic forms of partitioned vectors) and B (KF + RTS equation listing)

## Build
```bash
cd roth_robust_filter_1703.02428
xelatex -interaction=nonstopmode ms_uk.tex
xelatex -interaction=nonstopmode ms_uk.tex
```
Bibliography file `student.bib` needs to be copied from source; figure PDFs are referenced but not embedded — copy from source `figures/` if a full build with figures is desired.

## Coverage delta vs web model session
web model GPT-5.5 Pro session 02 covers Kalman/ESKF foundations in its native-Ukrainian core book, but does NOT include arXiv:1703.02428. The Roth $t$-filter is wholly additive — it gives Ukrainian engineers a drop-in robustness upgrade for any Kalman-based system without redesigning the underlying filter structure.

## TODOs / [[CHECK: ...]] flags
- All math preserved verbatim from source.
- `[[CHECK: term-stability]]` "матриця масштабу" for scale matrix (Σ in $t$-distribution) — also rendered as "матриця масштабування" in some Ukrainian probabilistic texts; picked the more compact form.
- `[[CHECK: term-stability]]` "важкохвостовий" for heavy-tailed — also "з важкими хвостами" (descriptive); both used.
- `[[CHECK: term-stability]]` "ступені свободи" — standard.
- The drone tracking example uses parameters specific to the original setup (yard 300×300 m², max speed 30 m/s, sampling 0.2 s). These are realistic for small commercial drone tracking. For specific Ukrainian use cases, parameters may need re-tuning.

