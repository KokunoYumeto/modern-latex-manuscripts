# Pending Claude fixes noticed by Codex: SGA6 idx625--635

This file is a durable flag, not a modification of the French authority. The English fragment applies the high-confidence corrections below provisionally because the scan, internal logic, and adjacent formulas make the intended reading clear. Claude should decide how to encode them in the French workpass.

## High-confidence workpass transcription defects

1. **idx626 / printed 613 / source-PDF 616, Lemma 4.4 point functor.** The scan reads `S_n(T)={phi}` in the true case; the workpass has `S_n(T)={\varnothing}`. English uses `{phi}`.
2. **idx626, same sentence.** The scan reads `R^i(f_T)_*(F_T)` for every `i>=n`; the workpass has `R^1(f_T)_*(F_T)`. English uses `R^i`.
3. **idx630 / printed 617 / source-PDF 620.** The workpass `tikzcd` for Proposition 1.3 has a missing parenthesis in `H^0(G(n+1)` and does not faithfully encode the printed diagram. The English diagram was reconstructed directly from the scan.
4. **idx632 / printed 619 / source-PDF 622.** The workpass has `\mapsto n^1(F(n))`; the scan reads `n\mapsto h^1(F(n))`. English uses the scan reading.
5. **idx632, Definition 1.5 (1.5.2).** The workpass repeats `sigma_1` as the last member of the zero sequence; the scan has `sigma_i`. English uses `sigma_1,...,sigma_i`.
6. **idx632, Proposition 1.6(i).** The same repeated-`sigma_1` transcription error occurs again; the scan again has `sigma_i`.

## Source-level defects or inconsistencies (workpass accurately reproduces a bad/ambiguous source reading)

1. **idx625 / printed 612 / source-PDF 615, first paragraph.** The source and workpass call `Rec` the functor of gluing data "on `f^*L`". Here `L` is already an invertible sheaf on `X`, so `f^*L` is ill-typed; moreover, the next sentence defines `Rec=Isom(p_1^*L,p_2^*L)`, confirming that this is the gluing-data functor on `L` relative to `f`. English provisionally corrects the phrase to `on L` and leaves this flag for the French workpass.
2. **idx627 / printed 614 / source-PDF 617, Lemma 4.4 proof.** The printed source and workpass say that `R^n f_*(F)` is flat for `i>=n+1`. This mixes a fixed exponent `n` with a quantified `i`. Descending induction requires `R^i f_*(F)` flat for every `i>=n+1`, followed by the distinct conclusion that `R^n f_*(F)` commutes with base change. English applies that correction.
3. **idx627, Lemma 4.6.** The source and workpass say that `u:F->G` is a homomorphism of `O_Y`-modules, while the same lemma declares `lambda:X->S` and its proof uses `lambda(Supp(Coker u))` and `lambda(Supp(Ker u))`. The modules must live on `X`. English uses `O_X`.
4. **idx631 / printed 618 / source-PDF 621.** The proof of Proposition 1.4 cites `2.3(i)`, but the invoked regularity result is Proposition `1.3(i)`. English uses `1.3(i)`.
5. **idx632 / printed 619 / source-PDF 622.** The continuation cites `2.3(ii)`; the invoked multiplication-surjectivity result is Proposition `1.3(ii)`. English uses `1.3(ii)`.
6. **idx633 / printed 620 / source-PDF 623, Proposition 1.6 proof.** The source defines `S'=A_k^N` and then calls `T` an open subset of `S`, although no `S` exists in this setup. It must be an open subset of `S'`. English restores the prime.
7. **idx633, Lemma 1.7.** The source and workpass print `0 -> F(1) -> F -> G -> 0`, but the proof immediately uses `chi(F(n))-chi(F(n-1))`, and Proposition 1.8 repeats the same construction correctly as `0 -> F(-1) -> F -> G -> 0`. English uses `F(-1)`.

## Literal oddities preserved pending editorial policy

- Lemmas 4.4 and 4.5 call the representing map a **surjective monomorphism of finite presentation** and explicitly warn in 4.5 that it need not be an immersion. This is unusual but unambiguous in the source and has been preserved.
- The prose immediately after the first Proposition 1.3 diagram refers to the "first" horizontal row and the "second column" in a compressed way. The diagram and prose were translated without attempting a mathematical rewrite.
- Printed page 615 ends Exposé XII without the concluding paragraph added by the inherited English witness. No conclusion was invented.
