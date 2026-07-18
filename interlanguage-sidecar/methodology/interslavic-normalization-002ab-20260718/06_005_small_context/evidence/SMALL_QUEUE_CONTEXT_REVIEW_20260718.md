# Small normalization queues: token and context review

Date: 2026-07-18

## Reviewed decisions

- `vprašanj*` → `pytanj*`: 19 Latin occurrences and 19 paired Cyrillic occurrences. All are inflections of “question”; the target family is already corpus-primary (89 prior Latin root matches) and improves cross-family recognition relative to the Slovenian-shaped alias.
- `slijedi` → `slěduje`: 15 Latin and 15 Cyrillic occurrences, all finite “follows” forms. The earlier root probe reported six additional Latin `sledi` hits, but tokenization showed those were embedded strings such as `posledice`, not editable tokens. One standalone Cyrillic `следи` remains a genuine “follows” form and maps to `следује`.
- `slućaj*` → `slučaj*`: 18 Latin occurrences (7 nominative, 11 governed `-u`) in Paper 40. Cyrillic already uses canonical `случај*`; no Cyrillic edit is needed.
- `namreč`, `naime`, `totiž` → `imenno`: 19 Latin and 19 Cyrillic connective occurrences. They all introduce specification/explanation (“namely/that is”). `imenno` is corpus-primary (102 prior Latin matches).

## Connective register / intelligibility note

The normalized corpus uses `imenno` as its editorial connective. Readers coming from West/South Slavic may recognize the replaced aliases more readily: `namreč` (Slovenian), `naime` (South Slavic), and `totiž` (West Slavic). The terminology/register web must therefore retain these as aliases of canonical `imenno`; normalization is not a claim that the aliases are invalid.

## Planned coverage

125 replacements across the paired corpus: 71 Latin and 54 Cyrillic. The difference is explained by the already-normalized Cyrillic `случај*` family and inherited paired-corpus variation.

This is a typed, tokenized editorial review. It is not community certification or an independent every-sentence source audit.
