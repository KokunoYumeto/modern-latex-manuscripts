# al-Battani Geography Gazetteer, Partial Edition

This folder contains the current partial reconstruction of al-Battani's geographical tables from Nallino's critical edition of the *Opus Astronomicum*.

## Coverage

- Regions: 93 rows transcribed from the regional midpoint table.
- Cities: 44 rows transcribed from the city longitude/latitude table.
- One city row remains explicitly marked for verification.
- Chronology, zodiac, auxiliary numerical tables, and the remaining city-gazetteer rows are still in progress elsewhere in the al-Battani table lane.

## Files

- `al_battani_geography_gazetteer.pdf`: rendered public reader.
- `albattani_geography.csv`: clean CSV dataset.
- `geo_cat_raw.tsv`: raw tab-separated transcription used for the build.
- `build_geography_original.py`: original build script from the Claude push queue.
- `build_geography_standalone.py`: local standalone build script adjusted to read `geo_cat_raw.tsv` from this folder.

The public record should describe this as a partial geography-gazetteer edition, not as the full city table.
