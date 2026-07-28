# SGA 3 Exposé XII — lead native-diagram high-zoom review PASS

Date: 2026-07-28  
Reviewer: top-level Session C lead  
Status: **PASS**

## Scope and controlling evidence policy

This receipt closes the two diagram blocks owned by Session C in Exposé XII.
The delivered implementations are editable native `tikz-cd`; no raster image
is delivered as a diagram.

Existing 600-dpi and 1200-dpi evidence remains legitimate append-only
history/context. A 300-dpi image alone does not support diagram-fidelity
approval. The adjudicative comparisons below were made directly by the
top-level lead at 5000 dpi, with a targeted 9000-dpi escalation for the one
remaining ambiguity. No audit agent made or certified a visual or
mathematical judgment.

Authority:

- `Expo12.pdf`
- 490,790 bytes
- SHA-256
  `4DAE85A06B7C1D6CD98D6332DE144AED80A96D19267D0603CC9CBEF06757C15E`

## Diagram 1 — Lemma 2.3

- Authority locator: local page 10 / combined page 766.
- Delivered locator:
  `tex/components/00_expose_XII_sections1_3_en.tex:731`.
- Delivered PDF page: 12.
- Disposition: **PASS_NATIVE_5000DPI**, no TeX repair required.

The lead checked, edge by edge, the following native diagram:

```text
T  ↪  C(T)  ↪  C(R)
      ↓↪        ↓↪
   N(T)∩N(R) ↪ N(R)
      ↓↪
     N(T)
```

Objects, directions, arrowheads, hooks, attachment points, and the placement
of the lower `N(T)` branch agree with the authority.

Adjudicative evidence:

- `authority_p10_lemma23_midrow_5000dpi_r2.png`,
  105,440 bytes,
  SHA-256 `FE24704D7F1C543EC4BE460FA86FB019CA699461FE3CEC4EA5A43AC6A3BDCD7A`.
- `authority_p10_lemma23_bottom_5000dpi_r2.png`,
  42,532 bytes,
  SHA-256 `C66A9AFDC66425096957C68B7F55439DB5E46708566D5A23207502D51A5DEE3E`.
- `delivered_p12_lemma23_midrow_5000dpi_r2.png`,
  166,310 bytes,
  SHA-256 `13693806CC62DA76667C39CB680E6BA9D9F0E68FFDF5306C7703C0E9022FAAC8`.
- `delivered_p12_lemma23_bottom_5000dpi_r2.png`,
  86,768 bytes,
  SHA-256 `6F991D55DA9D8395CFBFFC2A1B8BC6B4DE22CB163039044DEFCD0FFB91E14BBB`.

The earlier non-`r2` and misframed top-row crops remain preserved but are
explicitly non-adjudicative.

## Diagram 2 — Theorem 6.6, diagram (D)

- Correct authority locator: local page 28 / combined page 784.
- Earlier local-page-26 locator: superseded as stale.
- Delivered locator:
  `tex/components/01_expose_XII_sections4_6_en.tex:1285`.
- Delivered PDF page: 30.
- Disposition: **PASS_NATIVE_5000_9000DPI_REPAIRED**.

At 5000 dpi, the objects, all horizontal and vertical arrows, directions,
arrowheads, and the labels `u`, `u'`, `v`, and `v''` matched. The placement
of `v'` remained the single material ambiguity. A direct 9000-dpi comparison
showed that the authority places `v'` on the left side of the vertical arrow
from `G'` to `H'`, while the predecessor native diagram placed it on the
right.

The no-overwrite successor was repaired from:

```tex
G' \arrow[r] \arrow[d,"v'"] &
```

to:

```tex
G' \arrow[r] \arrow[d,"v'"'] &
```

The repaired 9000-dpi output now matches the authority. Fresh 5000-dpi
top- and bottom-row renders show no regression elsewhere.

Adjudicative evidence:

- `authority_p28_D_toprow_5000dpi.png`,
  328,938 bytes,
  SHA-256 `2C15B5F2BC383EAC12B7F8910C7F205AC5721DB4885F1FF635573512D069EC01`.
- `authority_p28_D_bottomrow_5000dpi.png`,
  876,622 bytes,
  SHA-256 `DF30D8ECED386AFD8D172D3DFB4474849F57C87ED587B20E1430BF8EA96B1707`.
- `authority_p28_D_vprime_9000dpi.png`,
  450,834 bytes,
  SHA-256 `918772408C1D30683829B8FCF246C1FD5C7580688C69BA451BCE44E23C543253`.
- `delivered_p30_D_toprow_5000dpi_r2.png`,
  282,482 bytes,
  SHA-256 `1F6B7FEEA2F6801210777B39C0B0B798110E1EEAE8790D47DDECF3524CFCDFE8`.
- `delivered_p30_D_bottomrow_5000dpi_r2.png`,
  395,871 bytes,
  SHA-256 `EC9EC322E0F6D718BA45319B629E8B7FF62B83963DB20C0E084D09A032A332AC`.
- `delivered_p30_D_vprime_9000dpi_r2.png`,
  290,262 bytes,
  SHA-256 `DAD2FEBBD42573311474A6013A97AB7A94F6B972705261CAA63C0F7F747265D4`.

## Rebuild and final identities

Three consecutive XeLaTeX passes completed successfully after the repair.
The final reader has 51 A4 pages. There are zero fatal errors, undefined
control sequences, undefined references, multiply-defined labels,
duplicate destinations, missing characters, overfull/underfull boxes, or
rerun requests. The retained warnings are the pre-existing harmless XeLaTeX
`inputenc` notice and `hyperref` empty-anchor suppression.

- Master:
  `tex/SGA3_Expose_XII_English.tex`,
  1,296 bytes,
  SHA-256 `2B6F6207CFDA0ADAF046727BC62A533B090FF5A35D66C297306BFE8234335C57`.
- Component 00:
  38,445 bytes,
  SHA-256 `ED695BE3E7ADA776BF1857FD87351C5D4B6E9F60ABC57724B3A2284ED0A7ECAB`.
- Repaired component 01:
  53,907 bytes,
  SHA-256 `3896C9530493BD435DD5A3495BB382A3A0895AF4F66A9247A3BE8F010AAE2866`.
- Reader:
  `build/SGA3_Expose_XII_English.pdf`,
  282,869 bytes,
  SHA-256 `17D3646EF85FB1C1D7831B646755C199C862E912935EC4B01DAA0DF0BF48ADDC`.
- Final build log:
  38,807 bytes,
  SHA-256 `69B4C543FC09F8928781411838CBE3401A14E00E68AAB3F356F894C99DCBAA06`.

Both Exposé-XII inventory rows are closed. This is a bounded native-diagram
successor receipt, not a whole-SGA3 publication or archive claim.
