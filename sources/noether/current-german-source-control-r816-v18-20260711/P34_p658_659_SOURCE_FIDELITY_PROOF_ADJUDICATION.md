# P34 pp. 658-659 source-fidelity and proof adjudication

## Authority

The authority for this pass is the GDZ full-resolution page-image sequence for *Hyperkomplexe Größen und Darstellungstheorie*, printed pp. 650-662. Prior audit ledgers were used only as archaeology and were not accepted as certification.

## Printed p. 658

The source prints

```tex
\mr_1\simeq \mo/(\mr_2+\cdots+\mr_n)=\mr_1'+\mr_2'.
```

The cumulative instead had `\mr_1'+\mr_1''`, which is mathematically expected from the immediately preceding decomposition but is not what the printed page says. v18 restores the printed `\mr_2'` and records the likely source typo here. No silent editorial correction or reader-facing note was inserted into the transcription.

## Printed p. 659

The source proof reads

```tex
\mr\mo=\mr(\ma_i+\mb_i)=(\mr\ma_i,\mr\mb_i)
\subseteq(\mr,\ma_i\mb_i)=(\mr,0)=\mr.
```

The prior cumulative omitted `\subseteq(\mr,\ma_i\mb_i)` and therefore converted the proof into a false compressed equality chain. v18 restores the complete source argument.

## Responsibility and prior closure failure

LocalCodex independently found both loci during the 2026-07-11 second pass. The user did not identify either specific formula. The earlier 2026-06-28 page ledger called p. 658 no-patch and did not expose the p. 659 omission; both prior dispositions are superseded.

## QA

XeLaTeX passed twice. The second-pass log contains no undefined-reference, rerun, fatal, or emergency-stop flag. The cumulative remains 466 pages. Changed output pages 327-328 were rendered and visually checked.
