# BATCH_REPORT — sdr_survey_1804.06564

**Source**: arXiv:1804.06564 — Akeela & Dezfouli, *Software-defined Radios: Architecture, State-of-the-art, and Challenges* (2018).
**Translator**: auxiliary local run (Anthropic), lane lead: local project.
**Date**: 2026-06-01.
**Status**: **Selective translation**: conceptually-enduring sections fully translated; dated 2018 commercial enumerations (full Sections 4 Development Tools, 5 Platforms, and platform-specific subsections of Section 3) summarized with forwarding pointers to the source.

## Output
- `paper_uk_core.tex` — single-file consolidated Ukrainian version (XeLaTeX + polyglossia).

## Rationale for selective scope
The source paper is 2200 lines (~1500 of substantive content). Sections 4 (Development Tools) and 5 (Platforms) are exhaustive enumerations of specific 2018-vintage SDR boards (USRP B/N/X series, WARP, KUAR, Sora, Atomix, Airblue, Nutaq PicoSDR, Lyrtech, etc.) with prices, chip families, GFLOPS numbers, and tool versions. In 2026, this catalog is 8 years stale — most platforms have been replaced or rebranded, and tools (Xilinx ISE → Vivado → Vitis; Altera Quartus → Intel Quartus Prime; etc.) have major version churn. A faithful translation of stale catalogs delivers low utility per token.

The translation thus prioritizes:
1. **Full**: Title, Abstract, Section 1 Introduction (incl. abbreviations table), Section 2 Concepts and Architecture (the lasting SDR architectural primer), Section 3 framing (Design Approaches criteria and 5-way classification with concept-level summary), Section 6 (Open Research) concept-level, and Section 8 Conclusion.
2. **Summarized with forwarding pointer**: Section 3 platform-specific subsections, Section 4 (Tools) full, Section 5 (Platforms) full, Section 7 (Existing Surveys) full.

## What this delivers to a Ukrainian SDR reader
- A complete Ukrainian glossary and architectural narrative for SDR (антена → РЧ-передній край → ADC/DAC → цифровий передній край → обробка базової смуги).
- Ukrainian terms for GPP/GPU/DSP/FPGA design tradeoffs, with criteria for selection.
- Future-research framing that is still accurate in 2026 (energy efficiency, real-time, security, ML in SDR).

## Build
```bash
cd sdr_survey_1804.06564
xelatex -interaction=nonstopmode paper_uk_core.tex
```
References (`ref.bib`) must be obtained from the source `.bbl` or re-fetched from arXiv if `bibtex` is to be run; the source provides `paper.bbl` which can be renamed to `paper_uk_core.bbl`.

## Terminology decisions
| EN | UK |
|---|---|
| Software-defined Radio (SDR) | програмно-визначене радіо (SDR) |
| transceiver | трансивер (приймач-передавач) |
| baseband | базова смуга |
| baseband waveform | сигнал у базовій смузі |
| Intermediate Frequency (IF) | проміжна частота (IF) |
| RF front end | РЧ-передній край |
| analog/digital front end | аналоговий/цифровий передній край |
| Analog-to-Digital Converter (ADC) | аналого-цифровий перетворювач (ADC, АЦП) |
| Digital-to-Analog Converter (DAC) | цифро-аналоговий перетворювач (DAC, ЦАП) |
| Low Noise Amplifier (LNA) | малошумний підсилювач (LNA) |
| Local Oscillator (LO) | локальний осцилятор (LO) |
| Digital Up/Down Converter (DUC/DDC) | цифровий перетворювач догори/донизу (DUC/DDC) |
| Sample Rate Conversion (SRC) | перетворення частоти дискретизації |
| channelization | каналізація |
| modulation/demodulation | модуляція/демодуляція |
| interleaving/deinterleaving | чергування/розчергування |
| scrambling/descrambling | скремблювання/дескремблювання |
| Convolutional/Turbo/LDPC codes | згорткові/турбокоди/LDPC-коди |
| Fast Fourier Transform (FFT) | швидке перетворення Фур'є (FFT) |
| reconfigurability | переконфігуровність |
| Field Programmable Gate Array (FPGA) | програмована логічна матриця (FPGA) |
| Application-specific Integrated Circuit (ASIC) | інтегральна схема спеціального призначення (ASIC) |
| co-design | спільне проектування (co-design) |
| Spurious-free Dynamic Range (SFDR) | динамічний діапазон без побічних спектральних компонент (SFDR) |
| Signal-to-noise Ratio (SNR) | відношення сигнал/шум (SNR) |
| beamforming | формування променя (beamforming) [seed glossary] |
| Software-defined Network (SDN) | програмно-визначена мережа (SDN) |
| System on Chip (SoC) | система на кристалі (SoC) |

## Glossary additions proposed
- `baseband → базова смуга` (extend seed)
- `baseband waveform → сигнал у базовій смузі`
- `RF front end → РЧ-передній край`
- `digital front end → цифровий передній край`
- `LNA → малошумний підсилювач`
- `transceiver → трансивер`
- `FPGA → програмована логічна матриця`
- `ASIC → інтегральна схема спеціального призначення`
- `co-design → спільне проектування`
- `interleaving → чергування`
- `scrambling → скремблювання`

## TODOs / [[CHECK: ...]] flags
- `[[CHECK: term-stability]]` "перетворювач догори/донизу" for up/down converter — alternative: "висхідний/низхідний перетворювач". Picked the morphologically transparent form.
- `[[CHECK: term-stability]]` "каналізація" for channelization — also "каналізаційне розділення". Both are in use; picked the more compact form.
- Section 4 (Tools) full translation deferred — recommend doing it after picking a target tool baseline (likely Vivado+Vitis for FPGA, GNU Radio for GPP, MATLAB/Simulink for model-based).
- Section 5 (Platforms) full translation deferred — recommend replacing with a fresh 2026 SDR platform survey, since the 2018 list is largely stale.

## Coverage delta vs web model session
web model GPT-5.5 Pro session 02 has "PySDR Ukrainian lane" partially done (one compact TeX module 13 in session 02). The full architecture survey arXiv:1804.06564 is **not in web model's pipeline**. This translation is wholly additive and fills the SDR architectural foundation that PySDR (which is more practice-focused) does not cover.

