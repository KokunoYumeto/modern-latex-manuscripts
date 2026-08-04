# Emmy Noether — current German authority v010

This is the current project German source-control authority, `NOETH-DE-AUTH-v010-20260804`. Start with the exact 466-page [German PDF](files/de.pdf) or the editable [German TeX](files/de.tex). The exact adopted [authority pointer](files/pointer.json) explains the source lineage, accepted corrections, build state, and translation bindings.

The current TeX is 2,153,554 bytes, SHA-256 `C9A125167ACB33D914EE4374B65AE7CDF0052F568371B8B77B720EA178ABF0E3`. The PDF is 2,654,430 bytes, SHA-256 `EA6812ED09FBCB67682180C74493452133C142FD8D54C6547E6EE1FEFC4C9B4C`.

The v010 authority includes two accepted source repairs with their primary evidence and append-only rationale:

- Paper 22: `\Bmod_i` → `\Bmod_\lambda`.
- Paper 8: `\theta_1,\theta_2` → `c_1,c_2`.

The control snapshot preserves all six German candidate files, all three build histories, all ten pointer generations, all 104 unit-control files, every current ledger/receipt/schema/template, the four evidence directories, and the retained failure/recovery audits. Nothing in the source control root was edited, renamed, deleted, compiled, or regenerated.

The producer's `MANIFEST_SEAL_20260804.csv` is retained as historical evidence, but it sealed v009 and is not represented as a v010 manifest. The current GitHub snapshot is instead bound by [manifest.csv](manifest.csv): 201 exact files, 37,023,697 bytes, canonical tree SHA-256 `D978E9C9A33AC274B52AD2780A0600B157061B3A14D3EF9D55F983D1095689C9`. Each row records the original control-root path, destination path, byte count, and SHA-256.

State: **current project German authority; machine-assisted working source control; two-pass XeLaTeX build passed; not a critical edition, human certification, or mathematical peer review**.

Older public German source generations remain elsewhere in this repository. Prior external-transport directories were not recopied into this checkpoint; this projection contains the authority and its complete bounded control surface, not duplicate transports.
