# How the Noether German authority chain failed

Date: 2026-08-04  
Scope: Noether German canon/source control only. No CJK translation review and
no SGA work were performed.

## Executive finding

The project did not primarily lose the German corpus. It lost the ability to
answer a simpler question: **which exact bytes does “current German” mean, and
why?**

The source material was unusually well preserved. Zenodo had an immutable
version chain; GitHub had later public German heads with exact hashes, build
records, diffs, and source-audit packages; local storage retained R821, P04,
P09, and large self-contained packages; CJK lanes retained exact unit slices.
Yet the control plane allowed all of the following to be called current:

- the stale shared R821 copy;
- the public R823 release;
- Zenodo's later direct P02/P04S07 file;
- GitHub's still later preferred P02-through-p49 head;
- a bounded P04 evidence cumulative;
- the unpublished P09 local successor;
- a missing sealed P31 lane input;
- the missing P16 independent-second-pass claim.

That is the failure. Storage pressure and the Drive offload exposed it, but did
not create it.

## The publication answer that should have been checked first

### Zenodo

The durable concept DOI is
[`10.5281/zenodo.20412587`](https://doi.org/10.5281/zenodo.20412587).
The current version at audit time is record/version 170,
[`10.5281/zenodo.21699405`](https://doi.org/10.5281/zenodo.21699405).

Its direct German TeX is:

`00_Noether_German_Cumulative_WorkingSourceControl_P02_P04S07_20260718.tex`

- 2,152,414 bytes
- official MD5 `c416b6ae3cd9f742d85fd2acbdb6c90d`
- SHA-256 `8851AF561D7C40B2295DB5D4108684A06015756B9B6FDD7CCE67466E0F7F8134`

Those exact bytes first appeared in record 21434690/version 166 on July 19 and
remain unchanged through records 21498737, 21499492, 21499660, and 21699405.
They are a real, authenticated public baseline.

But Zenodo's current record also retains a ZIP named
`07_Noether_Current_German_SourceControl_v26_R823_20260717.zip`, whose inner
German TeX is an older, different file:

- 2,125,031 bytes
- SHA-256 `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`

Thus even a correct Zenodo lookup exposes two differently dated artifacts with
“Current German” in their packaging.

### GitHub

The declared public repository is
[`KokunoYumeto/modern-latex-manuscripts`](https://github.com/KokunoYumeto/modern-latex-manuscripts).
Its later public package explicitly names this file the preferred overall
German working head:

`sources/noether/german-current-head-p02-through-p49-20260719/current/cum_de_Local_20260719_P02p042_049_CurrentHeadAudit.tex`

- publication commit `b2262d074c01eabbacbfc0658575e1e589060327`
- Git blob `0b07990f40d03ff47e815af516f83c95cc720513`
- 2,153,560 bytes
- SHA-256 `6FCBF5DB4E4378032B7074442C181E3FCFE975275319E49B284CE3B868EE0D5D`

At remote main `24d3278776316a510c34cd10fb4727923eefdf06`, the blob is unchanged.
The public README says this head supersedes the preceding GitHub head **only as
the preferred overall German working head**. The producer package calls it
“Current authority,” records two XeLaTeX passes, and the public replay records
byte-identical text extraction plus same-renderer page matches.

It also honestly says that only 745 of 753 page keys and 42 of 43 numbered
papers were closed, with Paper 2 printed pp. 50–57 still open. It is a working
source-audited corpus, not a complete author release or critical edition.

Zenodo's direct German file and GitHub's preferred German file are not the same
object. A line comparison reports 358 insertions and 339 deletions. GitHub
published five later cumulative German heads, while Zenodo's direct German
front remained frozen at the earlier 8851AF... bytes. No unified publication
pointer reconciled that divergence. There are no Git tags and no published
GitHub Release establishing a separate immutable release boundary for the
later head.

## Chronology of the control failure

| Date | Event | What the record actually proves |
|---|---|---|
| 2026-07-16 | R821 published and copied into the shared project pointer | An exact historical public object, later stale |
| 2026-07-17 | R823 published on Zenodo and GitHub | Exact public predecessor `EE8955...F4F21` |
| 2026-07-18 | CJK control notes that R821 is stale | Pointer debt was known, but not made blocking |
| 2026-07-18/19 | P02, P04, P29, P39 and other source repairs accumulate | Strong exact evidence, but spread across package-local ledgers |
| 2026-07-19 | Zenodo direct P02/P04S07 appears | Immutable public `8851AF...F8134` |
| 2026-07-19 | GitHub publishes later preferred P02p49 | Later public `6FCBF5...D5D` |
| 2026-07-19 | P09 local post-closure head appears | Replayable local bytes `528243...031F`, but no authenticated publication receipt |
| 2026-07-22 | CJK control adopts P16 by absolute path/hash | A historical claim `443EF9...46D27`, not a replayable successor edge |
| 2026-07-22 | Zenodo updates other reader surfaces | German direct bytes remain the July-19 8851AF file |
| 2026-08-03 | Disk consolidation/offload protects named roots | Transport integrity is checked, but embedded authority dependencies are not replayed |
| 2026-08-04 | P16 and old P31 coordinates are absent | Orphan hashes remain; the published sources still exist |

The decisive transition is July 22. P16 became a translation input because a
control log recorded an absolute path, whole hash, and pointer hash. It did not
record a parent SHA, exact predecessor-to-successor diff, DOI, Git blob,
published readback, or content-addressed retained copy. Once the date-tree path
was consolidated away, the project retained the claim but not the claimed
bytes.

P16 cannot be recreated by normalizing the surviving P09 file:

- P09 after CRLF-to-LF normalization: 2,131,048 bytes,
  SHA-256 `A9FDA0438348F1781B1AFDE1B3C0EA02F4F20254424078CD0AD68C812309B43D`;
- historical P16: 2,132,486 bytes,
  SHA-256 `443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27`.

The 1,438-byte difference is substantive or structural. Inventing P16 from P09
would therefore fabricate an authority.

## Why each layer failed

### 1. Publication discovery was optional

The repository README itself says durable releases live on Zenodo and names the
concept DOI. Nevertheless, authority work began by searching local candidates.
This inverted the evidence hierarchy: the least durable coordinate was checked
before the public record.

The correct first five minutes were:

1. resolve the concept DOI;
2. enumerate current and predecessor German objects with byte counts/checksums;
3. inspect the declared GitHub repository for later public heads;
4. compare the exact public bytes and package precedence statements;
5. only then search local storage for unpublished successors.

### 2. “Current” was a label, not a state machine

No field distinguished:

- `published_predecessor`;
- `selected_public_parent`;
- `accepted_editorial_successor`;
- `unpublished_competing_head`;
- `bounded_evidence_object`;
- `historical_missing_claim`;
- `translation_unit_snapshot`.

Without typed states, date, path depth, and filename rhetoric substituted for
authority. This is why a file named `CurrentHead`, an evidence cumulative, and
a sealed lane input could all look equivalent.

### 3. Known pointer debt did not fail closed

The Chinese control log explicitly said the shared R821 pointer was stale. The
system then continued by giving each lane its own absolute source path. That
kept work moving while silently increasing the number of authority roots.

The debt was operationally cheap until the paths disappeared. Then every lane
had a hash but no common source coordinate.

### 4. Publication handoffs had no required return receipt

Local handoffs required payloads, hashes, evidence, and supersession prose, but
did not require the publication owner to return all of:

- immutable DOI/version or Git commit/blob;
- authenticated remote byte count and checksum;
- exact path on the remote surface;
- publication state;
- readback time;
- predecessor/successor edge.

Consequently a later local document could call an artifact public even when no
public readback survived.

### 5. Transport validation was mistaken for semantic validation

Two retained Paper-31 second-pass ZIPs are structurally empty:

- COMPLETE: 2,288 bytes; fourteen empty directories;
- CORE: 1,994 bytes; empty directories plus a 28-byte header-only manifest.

Their hashes validate perfectly. The retention plan nevertheless classified
them as current/final because of their date and name. A checksum proves that a
transport object is unchanged; it does not prove that required TeX, PDF,
pointer, manifest rows, and evidence exist inside it.

### 6. Evidence objects looked like authorities

The surviving P04 cumulative, SHA-256
`4E9B87691B32DED8DCEF13D445E3E91FB76FAF1036249537D3A96CD0B369C57D`,
is explicitly a bounded hunk-integration evidence object. It happens to be a
whole TeX file. Once P16/P31 disappeared, its shape and later date made it look
like a plausible head unless its README was read.

### 7. Workflow pass names collided with paper numbers

“P31” referred both to a full-volume workflow pass and to a Paper 31 audit
package. That overloaded namespace made retention logs and lane references
look mutually corroborating when they referred to different things.

### 8. The consolidation preserved volume, not semantic closure

The large consolidation was intentionally narrow to keep the PC alive. It
validated named roots and ZIP streams rather than recursively crawling the
disk. That operational choice was sensible. The failure was upstream: no small
authority dependency manifest existed for the consolidation to follow.

As a result, hundreds of gigabytes could be retained while a 2.1 MB source head
referenced from a deep `Documents\Codex\...` path was omitted.

### 9. Google Drive was treated as if storage implied identity

The July 22 Drive status recorded a planned Noether batch of about 80.7 GB
incoming plus 133.3 GB extracted. Floris now reports an approximately 300 GB
active offload. The Drive API currently exposes no completed P16/P31 object in
the recorded Noether snapshot folders.

That does not mean the queue is empty. It means an active queue is not a
readback receipt. Authority requires completed object ID, bytes, SHA-256,
lineage, and authenticated download—not a folder name or progress belief.

### 10. The first consolidation attempt repeated the same mistake

The initial local recovery in this task selected surviving P09 and created
`NOETH-DE-RCV-0002` with a source-confirmed Paper 22 repair before Zenodo and
GitHub had been reconciled. The repair itself was right; the base-selection
method was wrong.

That branch is preserved, hashed, compiled, and explicitly superseded. The
accepted successor `NOETH-DE-ED-0001` was rebuilt from the exact selected
GitHub public parent instead. Hiding this correction would repeat the original
governance failure.

## A concrete Zenodo packaging defect

The current Zenodo evidence archive 48 advertises a prechange object with SHA
prefix `954588...C063A`. Its shipped `03_prechange` member instead hashes to
`BD1C102E...A7E66`. The postrepair member is internally consistent and is
byte-identical to the direct German 8851AF file.

This does not invalidate the direct published German file. It proves that an
archive can be authentic, readable, and checksummed while failing to replay
the parent edge described in its own prose.

## What is now controlled

The project now has one current pointer file and immutable pointer snapshots.
The initial pointer v001 remains immutable at 13,494 bytes, SHA-256
`26B611FD14181BB12E51A8E7975B1EEB1F14283209989F6C3569FA2750985235`.
After the five bounded CJK receipts were recorded, current pointer v002 was
sealed at 14,779 bytes, SHA-256
`F029150DF34AD54D03E0EB5D57D12CEF30706BE058A4CD9AEB79A311B6409DDA`.
After the Korean Paper 41 interval was independently replayed, pointer v003
superseded v002 solely to add that sixth bounded binder. That pointer was
15,345 bytes, SHA-256
`932FEDC1735A41A9CF71D15A6C662A468A4CAD016AE8B3DECDF9A71E8BA7F197`.
After exact Korean Paper 5 and Paper 7 coordinate replays, pointer v004
superseded v003 solely to add those two binders. That pointer was 16,536
bytes, SHA-256
`A1C62FDACAA34DFC1B806DC18258F2E732539F7AE9D85AA4BD9E1067B8749D9F`.
After exact Korean Paper 3 and complete Paper 4 coordinate replays, pointer
v005 superseded v004 solely to add those five immutable receipt layers. That
pointer was 19,889 bytes, SHA-256
`42E6844BFCBFB2133E9AA323A823604351CF9C49550AFCF34ECAAF7887185660`.
After the complete Chinese Paper 39 marker envelope was independently replayed
and proved LF-byte-identical to its preserved historical German witness,
pointer v006 superseded v005 solely to add that immutable receipt layer. The
pointer was 20,666 bytes, SHA-256
`DB99DD87100654674D7ED24B4ABBBBC3A9920CCF035740D276CE8A87A5313C18`.
After the complete Korean Paper 2 source envelope was independently replayed
against ED0001 and its selected GitHub parent, pointer v007 superseded v006
solely to add that immutable coordinate receipt. That pointer was 21,580 bytes,
SHA-256
`A6A8FC8E5AC24ACAF49DFD55B4B58FA3DA882EF8C3FDD4D136220C8751045156`.
After the complete Chinese Paper 8 section-to-section marker envelope was
independently replayed against ED0001, its selected GitHub parent, and both
retained recovered competing heads, pointer v008 superseded v007 solely to add
that immutable coordinate receipt. The narrower article-core extraction is
preserved as explicitly nonbinding derivative evidence. The current pointer is
22,484 bytes, SHA-256
`F13E6D896DE6403829FE902609668AB3E3FCA8C3C7FAA07BE5F7A7A72A4C33D8`.
The default German authority bytes did not change in any of these metadata
updates.

Its selected public parent is the GitHub 6FCBF5 head. Its exact default
translation authority is `NOETH-DE-ED-0001`:

- parent: 2,153,560 bytes,
  SHA-256 `6FCBF5DB4E4378032B7074442C181E3FCFE975275319E49B284CE3B868EE0D5D`;
- accepted editorial source: 2,153,565 bytes,
  SHA-256 `D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB`;
- sole semantic change: Paper 22 `\Bmod_i` to source-backed
  `\Bmod_\lambda`;
- primary witness: 1,277,724 bytes,
  SHA-256 `32C0D0626784C504CD3AC0602720E2F4502A42A7A7ABF4DCB860FEF0AA024150`;
- two serial XeLaTeX passes exit 0;
- pass 2: 466 pages, zero selected fatal/undefined/rerun/box/missing-character
  diagnostics;
- changed output page 228 rendered and visually reopened.

The patch tool changed that edited line's terminator from CRLF to LF. This is
recorded as a tooling delta rather than silently folded into the semantic
repair.

The project-level controls now include:

- append-only decisions;
- source-version nodes and successor edges;
- a 42-record deduplicated intake/adjudication ledger with explicit classes
  `original_print`, `later_transcription`, `tooling`, `target_translation`, and
  `unresolved`;
- immutable CJK unit binders;
- a machine-checkable checker-confirmed finding schema;
- build logs, hashes, source evidence, and focused render QA;
- a failure ledger containing corrective controls.

## Residual risk—what is not solved by rhetoric

1. P09 is still a replayable unpublished competing head. Its full semantic
   relationship to the selected public head has not been independently replayed.
2. P16 remains missing. Its historical hash is not authority without bytes.
3. Zenodo and GitHub remain publicly divergent until a new publication unifies
   them or explicitly records their roles.
4. `NOETH-DE-ED-0001` is an accepted local editorial successor, not yet a
   published object.
5. No independent human critical-edition validation exists for the whole
   corpus or the new Paper 22 repair receipt.
6. The public GitHub package itself reports eight Paper 2 page keys still open.
7. The Drive offload remains operationally important but cannot be counted as
   recovered authority until authenticated remote readback exists.

For those reasons this audit does **not** call the result canonical. It calls it
an exact, replayable, compiled, evidence-typed working authority.

## Durable evidence

- `published/zenodo/ZENODO_OFFICIAL_PUBLICATION_AUDIT_20260804.md`  
  SHA-256 `FD779399CFAFCD8BAC7AACBD32DF3D103F687E8419D89127F0CF51B50805D85E`
- `published/github/GITHUB_PUBLICATION_AUDIT_20260804.md`  
  SHA-256 `D198A8C45E465D77203E1BCE04BC62BD6BBCA19F729E865D01775558027102B3`
- `GOOGLE_DRIVE_RECOVERY_AUDIT_20260804.md`  
  SHA-256 `7440E693EB64ABE2F134BC6830E667F6DF9DD04C6E81FC9D6B0D9C4A521D8154`
- `ledgers/FAILURE_AUDIT.jsonl`
- `ledgers/SOURCE_VERSION_LINEAGE.jsonl`
- `ledgers/DEFECT_INTAKE_ADJUDICATION.jsonl`
- `CURRENT_GERMAN_AUTHORITY_POINTER.json`

## Append-only correction after checker-confirmed Paper 8 intake

The preceding narrative records the state through pointer v008 and must not be
read as the final state. A schema-valid independent-checker packet subsequently
confirmed that the inherited Paper 8 transcription at German line 6042 used
`\theta_1,\theta_2`, while Mathematische Annalen 77 printed page 96 visibly
reads `c_1,c_2` and immediately uses `c_1P_1+c_2P_2`.

The German owner independently reopened the primary page, found no prior
matching controlled defect, classified the error as `later_transcription`, and
created `NOETH-DE-ED-0002`. The exact successor is 2,153,554 raw bytes,
SHA-256
`C9A125167ACB33D914EE4374B65AE7CDF0052F568371B8B77B720EA178ABF0E3`.
Two serial XeLaTeX passes exited zero, produced 466 pages, and the corrected
output page 96 was rendered and visually checked. The controlling pointer is
now `NOETH-DE-AUTH-v009-20260804`, 24,741 bytes, SHA-256
`B06BE3530D9CF2E82B56FDBA7FE41D5D044DF2425DFA2A059D4939EAA2F7A6C2`.
Only the Paper 8 binder was superseded; all other bounded receipts remain
valid under an explicit adoption receipt.

The defect ledger now contains 44 records, not 42. Records 0001--0036 remain
preserved historical custody adjudications and were not falsely upgraded to a
claim that every legacy primary page was reopened in this consolidation.
`ledgers/DEF_EVIDENCE.jsonl` records that limitation and the exact evidence
state for records 0037--0044. `ledgers/DEC_DETAIL.jsonl` supplies the full
work-unit, alternatives, cursor, uncertainty, consequence, changed-artifact,
supersession, and revisit fields omitted by the compact original decision
records. `manifests/UNIT_INDEX.jsonl` and `manifests/STRUCT.jsonl` provide the
machine-valid binder and internal source-unit/tranche/locus indices.

The remaining caveats are unchanged in kind: missing P16 bytes are historical
coordinate debt; Zenodo archive-48 has an external packaging mismatch; public
Zenodo and GitHub layers differ; and neither ED0002 nor the corpus as a whole
is claimed to be a published critical edition.
