# R9 Endonym GitHub Quota Retry For Skipped Rows

Generated: 2026-07-04T21:29:00.309494+00:00 UTC

## Boundary

This is a metadata-only retry for the four GitHub rows skipped in `R9_ENDONYM_SOURCE_ARCHIVE_PROBE_ROUND3_20260704.csv`. It records API response/header hashes and blocker states only. It does not download repositories, source bodies, datasets, PDFs, or text bodies; it does not translate, approve terms, clear licenses, or promote source-canon gates.

## Quota State

- GitHub search remaining at retry start: 10
- Retry rows: 4
- Nonzero metadata rows: 2

## Retry Results

| row | status | count | decision | summary |
|---|---:|---:|---|---|
| Wolof | 200 | 0 | metadata_only_not_admitted | no repository metadata results |
| Yoruba | 200 | 0 | metadata_only_not_admitted | no repository metadata results |
| AF05 South Sudan access target | 200 | 74 | metadata_only_not_admitted | Infrasity-Labs/awesome-developer-conferences \| lang=Python \| license=MIT \| url=https://github.com/Infrasity-Labs/awesome-developer-conferences ; RichardScottOZ/mineral-exploration-machine-learning \| lang=None \| license=missing \| url=https://github.com/RichardScottOZ/mineral-exploration-machine-learning ; hanshanley/pre1870_pop \| lang=HTML \| license=missing \| url=https://github.com/hanshanley/pre1870_pop ; ericrenone/FAIR-INFINITY-The-Universal-Architecture-of-Knowledge \| lang=None \| license=missing \| url=https://github.com/ericrenone/FAIR-INFINITY-The-Universal-Architecture-of-Knowledge ; ericrenone/CEPI-THE-WOBBLE-CURE \| lang=None \| license=missing \| url=https://github.com/ericrenone/CEPI-THE-WOBBLE-CURE |
| AF06 Omotic/Southern Non-Bantu access target | 200 | 1 | metadata_only_not_admitted | dictionaria/sidaama \| lang=Python \| license=CC-BY-4.0 \| url=https://github.com/dictionaria/sidaama |

All retry rows remain `promotion_allowed=false`.
