# Independent source-archive rebuild

Status: `PASS`

The integration-source ZIP was extracted into a fresh temporary directory and
compiled with four consecutive XeLaTeX passes. Every pass exited successfully.

Candidate reader:

- 950 pages
- 5,760,459 bytes
- SHA-256 `8D1DC78CDE64F22B76AD89150BEE73C48A1934EAECE0738B50AA413670CDDEAA`
- 5,923 named destinations
- 3,792 internal GoTo actions
- zero invalid actions

Fresh rebuild:

- 950 pages
- 5,760,439 bytes
- SHA-256 `27AC84CEEE8D872E0A44304C5CFB67A99D2BEEFBA4D45BB211907C5611A4AB88`
- 5,923 named destinations
- 3,792 internal GoTo actions
- zero invalid actions

All 950 extracted-text pages, decompressed page-content streams, and page
geometries are exact between the candidate and rebuild. The byte-level PDF
difference is confined to build-container metadata.
