# P29-KO-U03 render check

Accepted Korean render:

- path: visual_inspection/Noether_Paper29_Korean_U03_v001.png
- SHA-256: 42E78806891372C91FDB089A5374103B8BD8E4E7BECFC14D1C94C719F7911579
- dimensions: 1489×2105 at 180-DPI render setting
- inspection: original resolution
- result: no clipping, overflow, overlap, black square, missing Hangul, missing Fraktur, damaged superscript, formula loss, footnote collision, or page-break defect

German control render:

- path: visual_inspection/Noether_Paper29_German_U03_control.png
- SHA-256: 4331831B0FBF2F0E4354605897598F6A8EDDDEB8C8DFD416E15B5230550A1BFD
- dimensions: 1489×2105 at 180-DPI render setting
- result: no visible defect

The initial Korean render was overwritten before its original binary was hashed. Exact initial TeX was reconstructed at SHA-256 379C3A064823F94FDACD2419F5BCF9DAA54002FC7AA99F99A231DA0DE5FBE877; reconstructed PNG SHA-256 is 5103667C63B1CB8B114F28C1A3E5316B03B0B91E493FABB095E1382BBE0DDC6E. It is explicitly reconstructed, superseded, and not proven pixel-identical to the unavailable original.

Internal visual inspection is not external human typographic review.
