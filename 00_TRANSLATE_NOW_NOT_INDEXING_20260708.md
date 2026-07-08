# Other PC Directive: Translate Now

This branch now has enough source-body, route, provenance, and Fable/interlanguage support material to start producing translation payloads.

Stop making acknowledgement-only commits, route-only commits, source-body-only commits, and broad status ledgers as the main output.

The next useful commit must contain actual translation work.

## Set This As The Active Goal

Produce concrete translated TeX/PDF tranche packages from the existing available source bodies and canonical support material, starting with the interlanguage / Interslavic / Slavic lane.

Do not summarize the goal. Do not merely acknowledge it. Set it as the pursued goal and work it.

## Required Next Payload Shape

Each next commit should contain at least one real translation tranche with:

- translated `.tex`
- translated `.pdf` if compilation succeeds
- compile log or failure log
- render-check note if PDF exists
- source-use note saying which source bodies and support ledgers were used
- terminology note, including Fable / weighted-automata / branch-weight constraints where relevant
- `MANIFEST.csv`
- `SHA256SUMS.txt`
- short session logbook excerpt

## Priority Order

1. Interslavic / Slavic mathematical translation repair and production using the available Fable constraints and source-canon material.
2. Slavic non-Russian, non-Ukrainian branches where enough source-body material exists.
3. Ukrainian / Russian / Interslavic Noether or mathematical branches, keeping Ukrainian and Russian paired where that is project policy.
4. Other language-family branches only after the Slavic/Interslavic translation lane has real payload output.

## What Not To Do As Main Output

- Do not only say sources exist.
- Do not only build indexes.
- Do not only restate route plans.
- Do not only upload screenshots.
- Do not only write markdown about future work.
- Do not promote generated drafts as source witnesses.

Source collection remains allowed only when a specific missing source blocks a concrete translation tranche.

## Acceptance Rule

If the commit does not include actual translated TeX or a clearly failed compilation from an actual translated TeX attempt, it is not a useful translation-production commit.
