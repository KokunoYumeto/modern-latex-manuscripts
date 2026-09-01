# D017 integration input — accepted bytes only

This directory is a preparation bundle, not a new scholarly edition or public
release. The accepted D017 packet and gate are read-only inputs. No cumulative
reader has been built here. No predecessor record ID is assumed.

## Destination selection

The parent must first resolve the actual current, verified public corpus after
the D031 transaction finishes. Retain its existing exact Deligne path layout
and all prior complete or partial coverage. `D017/` below is a work-relative
relocation unit, not a claim about the repository's current directory name.
`INPUT_MANIFEST.json` contains every exact relative input path, size and SHA-256.

## Exact layout

- `D017/readers/`: the accepted standalone French, English and apparatus PDFs.
- `D017/source/`: all 41 members of the accepted source ZIP, extracted without
  modification. The editable TeX and page-indexed NDJSON are in `sources/`;
  its 11 fallback images are in `sources/assets/`. Keep that relative asset
  directory intact. Complete authority, repair logs and audit receipts remain
  in this same source tree.
- `D017/source_archive/D017_Source.zip`: the exact accepted source ZIP.
- `D017/acceptance/`: unchanged original final gate, packet/member manifests,
  packet verification and public-provenance transformation receipts.
- `D017/provenance/`: three ordered binary transfer chunks, each strictly less
  than 100,000,000 bytes, and `CHUNK_MANIFEST.json`.

There is no rewritten reader or witness in this integration bundle. Top-level
accepted TeX files are identical to the source ZIP's `sources/` counterparts;
the manifest records those equalities rather than creating alternate editions.

## Verify and rebuild individual readers if needed

From this directory:

    python verify_integration.py
    python reassemble_provenance.py

The first command checks all deterministic inputs, the accepted hashes, source
member mapping, and chunks. The second verifies the complete concatenated
carrier stream without writing another copy. To materialize that carrier for
the parent's consolidated archive, use a fresh output path:

    python reassemble_provenance.py --output D017_Public_Provenance.zip

The output is exactly 288,243,339 bytes, SHA-256
`9CEA8F4A0BFCE3EAD49A0E335DD3C55E2904BAF5E2505A4C70CB9D87C2FC4D1E`.
Never commit the unchunked carrier as an ordinary Git file exceeding the file
size limit. The chunks and manifest reconstruct it with no lost member.

Optional isolated individual reader reconstruction:

    python D017/source/rebuild_readers.py --source D017/source/sources --output isolated_D017_build

Do not overwrite accepted PDFs or source files. The language PDFs have already
reproduced byte-for-byte; all apparatus page rasters and text reproduced, with
PDF container-serialization variance recorded in the accepted audit.

## Parent cumulative integration sequence

1. Resolve the actual latest public baseline and retain its identities in the
   parent's durable release ledger. Do not infer a baseline from older witness
   filenames or a projected next DOI.
2. Verify this bundle. Relocate the exact `D017/` inputs using the established
   work-path convention and the supplied mapping. Stage only those explicit
   paths; never enumerate the entire repository.
3. Insert complete D017 in numerical position in each sparse cumulative reader.
   Preserve all existing complete and partial coverage. Build cumulative
   French and English editions and source corpus from that actual baseline.
4. Preserve the public name-only provenance derivative and its transformation
   receipt. Historical manifests inside it describe immutable original bytes,
   not reissued certificates. Do not substitute the private unredacted original.
5. Run the parent's deterministic cumulative, visual, mathematical, topology,
   provenance and first-name checks. The individual D017 gate does not assert
   acceptance of a not-yet-built cumulative edition.
6. Publish through the existing GitHub/Zenodo lineage; read back and hash every
   resulting public byte. No publication is performed by these preparation tools.

All inherited witnesses remain ZERO_ACCEPTED. The original rigorous audit ZIP
has SHA-256 `71B8EA274B0228CB0152ABE57228A5FF7C1E6D50A3B3818FF4A07AD6BEDFB77A`.
The accepted public derivative changes only 28 old text members containing the
literal local-account name and the containers rebuilt around them; the receipt
records original and derivative member hashes. All originals remain unchanged.
