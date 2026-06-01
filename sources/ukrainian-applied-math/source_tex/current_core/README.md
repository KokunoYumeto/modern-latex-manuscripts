# Ukrainian Applied Mathematics Core - prior build

TeX-first Ukrainian applied mathematics reference for signals, estimation, control, numerical methods, RF/SDR, sensor fusion, and engineering computation.

prior build additions:

- integrated reference now includes deeper Solà ESKF/IMU chapters;
- standalone Solà ESKF Ukrainian core module is included and compiled;
- latest auxiliary local run output has been preserved cleanly and compared against prior build integration;
- Codex-Spark worker pack has prompts, manifests, and helper scripts for fast token-pool use;
- PySDR Ukrainian RST-to-TeX conversion lane is explicitly queued.

Primary outputs:

- `pdf/ukrainian_applied_math_core_session05.pdf`
- `pdf/paper_modules/arxiv_1711_02508_sola_eskf_ua_core.pdf`

Build:

```bash
cd src
xelatex main.tex
xelatex main.tex
```

Standalone Solà module:

```bash
cd paper_modules/arxiv_1711_02508_sola_eskf_ua_core
xelatex main.tex
xelatex main.tex
```

Spark worker pack:

```bash
codex_worker_pack/README_SPARK_USE.md
codex_worker_pack/prompts/
codex_worker_pack/manifests/spark_task_manifest.csv
```
