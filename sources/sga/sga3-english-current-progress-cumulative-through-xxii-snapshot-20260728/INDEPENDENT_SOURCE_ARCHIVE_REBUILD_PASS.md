# Independent source-archive rebuild receipt

Date: 2026-07-28

Status: **PASS**

## Object checked

- Archive: `10c8_SGA3_CurrentProgress_Source_History_Through_XXII_Snapshot_20260728.zip`
- Archive bytes: 13,552,765
- Archive SHA-256: `866FA17BDABA537C67504F514F5544F2D08998F876F43C92312A389D89D1FC79`
- Members: 1,000
- Uncompressed bytes: 17,944,640
- Self-excluding member manifest rows: 999
- Member-manifest SHA-256: `8BCBF3A628B4EA765DDD081CC08B15706A6AECAC12DB0F3BE0DE5E137E917905`
- Unsafe, duplicate, unreadable, CRC-failing, extra, missing, byte-mismatched, or hash-mismatched members: 0

## Fresh build

The archive was extracted to a fresh workspace and its included master
`SGA3_English_Current_Progress_Cumulative_Through_XXII_Snapshot.tex` was
compiled with three independent XeLaTeX passes. All three processes exited
successfully.

Candidate reader:

- 1,100 A4 pages
- 6,863,204 bytes
- SHA-256 `E401297F71F030C8EBD26F321B7F91B03799A628462A06EFF9DC4C5ADB47E739`

Fresh rebuild:

- 1,100 A4 pages
- 6,863,200 bytes
- SHA-256 `D2ACB8733885A77FFE36618C85C7287A0444198E00C14EFDC7F479C1107C6B4D`

The four-byte file-level difference is confined to ordinary generated PDF
metadata/trailer identity. The following comparisons are exact:

- extracted text: 1,100/1,100 pages
- decoded page content streams: 1,100/1,100 pages
- page geometry: 1,100/1,100 pages
- 72-dpi decoded raster output: 1,100/1,100 pages
- named destinations: 6,805/6,805
- internal GoTo actions: 3,917/3,917
- pages carrying internal links: 835/835
- invalid actions: 0/0
- URI actions: 0/0
- font resources: 63/63
- Type3 fonts: 0/0

## Scope conclusion

The packaged archive is sufficient to rebuild the front-facing current-progress
reader. It retains the required editable source closure, diagram/source-crop
assets, bounded component readers, and the immediately preceding cumulative
reader, while excluding redundant PDF-page render QA. This receipt does not
upgrade the reader's scholarly claim: the reader remains an explicitly
incomplete working SGA3 translation with the scope and gaps stated in its
README and publication-readiness notice.
