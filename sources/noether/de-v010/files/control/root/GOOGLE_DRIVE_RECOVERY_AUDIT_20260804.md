# Google Drive recovery audit — Noether German authority

Date: 2026-08-04  
Scope: read-only recovery check for missing Noether German authority objects;
not a general Drive inventory.

## Result

Google Drive did not expose a completed, byte-addressable copy of the missing
P16 or old sealed P31 German heads at audit time. Drive therefore supplied no
object that could outrank or reconstruct the public Zenodo/GitHub sources.

This is not a claim that the local Google Drive client has no active queue.
Floris reports that approximately 300 GB of Noether material is actively being
offloaded to Drive to keep the PC stable. The connector result only describes
completed remote objects visible through the Drive API during this audit.

## Exact Drive controls inspected

- `PROJECT_STORAGE_OFFLOAD_STATUS_20260722.md`
  - Drive file ID: `15dufMR_HPtn58R9kdsdZP5Ja8P-Qq6q_`
- `PC_STORAGE_OFFLOAD_20260722`
  - folder ID: `1QWzO2VX2aTPMIir9vKaFhBhYb8GUBxQw`
- `02_FULL_LOCAL_SNAPSHOTS`
  - folder ID: `1WE1vLS6R4XUk4kl1dPB8R88Qb76PqIjh`
- `Noether_WEB_DOWNLOADS_LAST_14_DAYS_FULL_AUDIT_20260703`
  - folder ID: `1Hwe3rr5j3DAwuJjeRwYLbYcnSs8_k2tC`
- `00_incoming_zips`
  - folder ID: `1CIBOl9KDvt8s3L8rAfss5PCFxYQ1RNEc`
- `01_extracted_unique_zips`
  - folder ID: `1ZYdqLvLLoqJFit3sOnjezeT8oqaLr5nL`

The two Noether child folders returned no completed file objects through the
API. Exact-filename searches returned no object named
`Noether_P16_IndependentSecondPass_20260722_cum_de.tex` and no recoverable old
sealed P31 whole-head file.

## Historical offload status versus current user report

The July 22 status file records a planned Noether batch of approximately
80.7 GB incoming ZIP material plus 133.3 GB extracted material. It also records
that the next batch had not completed after a Windows/DriveFS interruption and
that project sources had not been deleted at that time.

Floris's current report of an approximately 300 GB active offload is later and
controls the present operational context. The older status file cannot prove
the current queue state. Conversely, an active queue cannot prove that any
specific authority object has reached remote storage.

## Authority ruling

Drive is a recovery and storage transport, not an authority namespace. A Drive
object becomes usable for authority only after all of the following exist:

1. exact completed remote object ID and stable coordinate;
2. downloaded byte count and SHA-256;
3. authenticated match to a recorded pointer or predecessor;
4. exact source-version lineage and publication/editorial state;
5. readback receipt after offload.

Until then, publication-first resolution applies: use Zenodo/GitHub as the
public lineage anchor and preserve missing P16/P31 references as historical
claims rather than reconstructing them from names or partial custody quotes.
