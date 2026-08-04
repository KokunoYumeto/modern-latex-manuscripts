# P06 T10 producer metadata — UNCHECKED

## Custody/state

- Pointer v008: 22,484 B / `F13E6D896DE6403829FE902609668AB3E3FCA8C3C7FAA07BE5F7A7A72A4C33D8`.
- ED0001: 2,153,565 raw B / `D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB`.
- Source §9: lines5326--5390, 7,469 LF B / `F2008C648951570F5FEA878657310E3EF0FF3BDD64E2B352A3277D4D4952FE05`.
- Route: `T10_ROUTE.md`, 2,715 B / `CF56041D51E47914DCDE8D30D3D5FC542F4331FEABD644C647678B8C5D8D6AFE`.
- Targets: U123--U143,21 files /17,956 B; every file LF-only, BOM false, CR0, ESC0.
- Next source: §10 line5391.
- State: complete producer-draft text coverage only; all targets `UNCHECKED`, uncompiled, unrendered, unassembled, unreviewed, uncertified.
- Images/renders: zero. German findings: none asserted or routed.

## Manifest

| Unit | Target B | Target SHA-256 |
|---|---:|---|
| U123 | 580 | `58736144100A4D082BFB76245526618747BF0A83A2702976E3C461AF4F39106C` |
| U124 | 616 | `5D6866618E139C2CAA857660F993C81FE932BF79FBEC94CA11C200DBEE5AEBDF` |
| U125 | 618 | `E00348FAF22D7114D6FC50AC56120DBEC6F28A56B7C49BACCFF5804F8599666E` |
| U126 | 740 | `82700267F401F52E803EFF9ACBC5438EDA06EEEAAF5C10D1C394C6084F1B0B61` |
| U127 | 631 | `9B23D6147187C16B9C2B9D8AE42CF0689A7335A0E4169CE0D705FF6643A72120` |
| U128 | 1,033 | `B449557FE70176164D798B63CE8C9A3BA8C63BE3D33BF6C0471EF78505758B4E` |
| U129 | 1,108 | `AF021E56AFE1BD34340DE49A334BABB61A710E32C94CBF43FA1786E50B81FDE8` |
| U130 | 760 | `AF7D581DA14BF98ECFB5D8B1F413CCABCE85C690F415DA88C93B0200CDAB5B26` |
| U131 | 1,277 | `3F823B3357FADBFA42ABBE17C0EFB068C59EAFB684E8F3DB1E1E5033E16D0DC0` |
| U132 | 609 | `08E45855D0F200098E55637CF1A9D4252FA55931960DC0EB917D96274427260D` |
| U133 | 724 | `53B5199A7DD5B3A35121E4482170CE70DA62758A1274DBE1D319DD304D7BF241` |
| U134 | 565 | `A3DECC6CC2A1E418F7539C3304466C5601C1EF93749365D9AC8F17B637157125` |
| U135 | 808 | `1ADB688D39E8071D0E8B62A4F9965BA30EFCF83C093BD78A82C1904328F7DA4B` |
| U136 | 794 | `29D8920258653B8A3927FF733851273EB2AD4334AB6FC0ADD0647D1FA67F9649` |
| U137 | 753 | `3137EE00D3D2CBAEC3CC281E30EF3AC28DD7DE31AF81788099A9CB92719F9CDB` |
| U138 | 1,238 | `46D41C943B9168A7D5B1D15CBEE1BC8F2DD0E5005E5FF4F1D546CECAA2A23014` |
| U139 | 740 | `6EB571DB12AD783EBB3B8459124BDBF7490A9DCAF04E2FEB111CB7432EBB321D` |
| U140 | 672 | `27D3B91C0F3D99722C5C7B4072CD192669EA4C81DACD1914AA7347D23C191A82` |
| U141 | 832 | `4823045938DF1C4E9FC9D0DF422671D836AAFA6701D9D5B6AE2DD6DA77E7CBD7` |
| U142 | 1,435 | `48F5833AA84B3BB59CD0E9EE5CC69B0832715B743089C18F563AEABA2FA54C76` |
| U143 | 1,423 | `864B85072DCEF98FEB23066C77104611A1DFE31178B8D8DE9DBE51D355BB7C42` |

Files are `targets/T10_U{unit}.tex`.

## Terms/adverse evidence

- `relativ-ganzer Bereich`: `상대정역(相對整域)`; `상대정수영역` remains an evidence-dependent alternative.
- `ganz in den Unbestimmten`: `부정원들에 관한 정식(整式)`, explicitly equated with polynomial in the source.
- `algebraisch-ganz / relativ-algebraisch-ganz`: `대수적으로 정수적 / 상대대수적으로 정수적`; `대수적 정`, `정수인` remain register alternatives.
- `höchster Koeffizient die Einheit`: `최고차항의 계수는 1`; leading-coefficient terminology requires checker review.
- `Integritätsbereich aus relativ-ganzen Funktionen`: `상대정함수의 정역`; historical Hilbert terminology remains open.
- `abspalten`: `분리해 내다`; the force of `höchstens ein gemeinsamer Teiler` remains unresolved.
- `Abbildungsbereich`: `사상영역`; mapping/specialization semantics require review.
- `정역(整域)`, `체(體)`, and `相對整域` use Hanja for provisional disambiguation only. Korean evidence is required; Mandarin-Simplified dominance is qualitative debt, never a scalar. ko-KP is `unverified_do_not_claim`.

## Checker handoff

Compare every clause/formula with ED0001 lines5326--5390. Verify condition4a iff/nonzero scope, both identity arguments, Hilbert definition and citations, divisor simplification, Definition V and monicity, divisibility by the irreducible equation, Gauss-theorem consequence, construction of the smallest relative-integral domain, involution-form factor removal, both footnote examples, mapping/specialization counterexample, every macro/display/index, Hanja, and regional usage. Return separate linguistic/formula/build/render/visual states and exact versioned corrections. Only personally confirmed German findings may go to the sole canon owner. No producer review or build is asserted.
