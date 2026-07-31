# Double-blind transcription check — SGA 7 II, folios 1–4

## Why this exists

The project owner asked the question that actually matters: **"is even a single page correct?"**

Coverage screens cannot answer it. `omitscan.py` tells you text is *present*; it cannot tell you
it is *right*. Auditing diagrams tells you about diagrams. Neither measures transcription accuracy.

So: I transcribed folios 1–4 of Exposé X **by hand**, from the page images, before the agent batch
covering the same pages was assembled. Neither pass saw the other. That is a genuine double-blind,
and the disagreement rate is a direct measure of accuracy.

## Result

**731 words compared. Word agreement 0.982.**

| page | my words | agent words | agreement |
|---|---|---|---|
| folio 1 | 244 | 245 | 0.998 |
| folio 2 | 189 | 190 | 0.987 |
| folio 3 | 154 | 155 | 0.984 |
| folio 4 | 144 | 147 | 0.969 |

Most disagreements were markup artifacts of the comparison (`\lg` stripped as a control sequence
on my side but present as a word on theirs; `aligned` vs `array` for the same visual result).

## The two genuine disagreements — the agent was right both times

### 1. folio 2 — `faisceauxcohérents`
The typescript runs the two words together with **no space**: "de la catégorie des
faisceauxcohérents de $\underline{O}_{Z_o}$-modules". Verified at 7000 dpi.

* **agent:** reproduced the words run together ✔
* **me:** silently inserted a space ✘

I normalised the author's typing. That is precisely the failure this project exists to avoid, and
I made it by hand while checking the machine's work.

⏳ One residual: the glyph after "faisceaux" is ambiguous between `o` and `c` because of ink
break — the agent read `cc`. Unresolved, and it does not affect the spacing finding.

### 2. folio 4 — `disjoints`
The scan reads "sont **disjoints**" — masculine plural, correct for *diviseurs* $D$ and $E$.

* **agent:** `disjoints` ✔
* **me:** `disjointes` ✘

## What this does and does not establish

**Does:** on 731 words of real text, an independent hand pass and the agent pass agree to 98.2%,
and on every genuine disagreement the agent was the faithful one. The specific worry — that agents
substitute plausible text for what is printed — is not what the evidence shows. Both errors were
mine, and both were *normalisations*: making the source tidier than it is.

**Does not:** four pages is four pages. It says nothing about the other 520, and it is one book in
letterpress-clean condition compared with the SGA typescripts. Repeat on a harder sample before
treating 98% as a general figure.
