# al-Battani Geography Gazetteer

This folder contains the current reconstruction of al-Battani's geographical gazetteer from Nallino's critical edition of the *Opus Astronomicum*.

## Coverage

- Regions: 93 rows transcribed from the regional midpoint table.
- Cities: 176 rows transcribed from the city longitude/latitude table.
- Total geography entries: 269 localities with coordinates.
- Chronology, zodiac, and auxiliary numerical tables are still in progress elsewhere in the al-Battani table lane.

## Files

- `al_battani_geography_gazetteer.pdf`: rendered public reader.
- `albattani_geography.csv`: clean CSV dataset.
- `geo_cat_raw.tsv`: raw tab-separated transcription used for the build.
- `build_geography_original.py`: original build script from the Claude push queue.
- `build_geography_standalone.py`: local standalone build script adjusted to read `geo_cat_raw.tsv` from this folder.

The public record may describe this as the current complete geography-gazetteer edition. It should not describe the chronology, zodiac, or auxiliary table streams as complete.
