# Noether R571 Zenodo Metadata Update Pending Auth

Date: 2026-07-02 12:45 CEST.

Local GitHub-facing docs and Zenodo-ready metadata have been updated for the Noether R571/R570/R569 source-control chain:

- R571 is the current packaged local TeX-changing German source-control head.
- R570 is the latest packaged no-patch checkpoint over collected pp767-772.
- R569 is the prior substantive p761/p764 repair head.
- R571 applies the source-visible p776 / output p466 `Bd. III.2` -> `Bd.III.2` Kronecker-review repair.
- R569/R570/R571 are queued for curated rollup rather than uploaded loose under the Noether 100-file ceiling.
- This is source-control/support material only, not a reader release, Noether closure, whole-corpus certification, multilingual synchronization, or a critical edition.

Public Zenodo readback at 2026-07-02 12:43 CEST still showed the prior R569/R570 metadata on:

- Noether: `10.5281/zenodo.20836874`
- Main landing: `10.5281/zenodo.20415117`
- Workflow: `10.5281/zenodo.20836364`

Reason: `ZENODO_ACCESS_TOKEN` was not available in process, user, or machine environment, no Windows secret-store entry was discoverable, and the in-app browser had no reusable authenticated Zenodo session. The local metadata files remain ready to publish once auth is restored.

The public readback probe is saved as `20260702_noether_r571_public_readback_probe.json`.
