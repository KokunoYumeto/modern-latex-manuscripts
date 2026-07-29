# Compact SGA release controls

The canonical SGA Zenodo reader surface should expose only direct readers,
direct editable TeX masters, and grouped archives. This package moves the
three previously loose release-control files into one deterministic ZIP
without changing their bytes.

- ZIP: `10z_SGA_Current_Release_Controls_20260729.zip`
- ZIP bytes: 6424
- ZIP SHA-256: `2F0D4D8247BEEB37A1A9C993F5A8AD18638EC0CCDB2B6EE0DDFD418C67256A39`
- ZIP members: 4
- Represented predecessor controls: 3
- Uncompressed bytes: 17775

The next same-concept Zenodo successor removes the three loose controls and
adds this ZIP. Every reader, direct TeX file, and unrelated archive is retained
byte-identically. Historical Zenodo versions remain immutable.
