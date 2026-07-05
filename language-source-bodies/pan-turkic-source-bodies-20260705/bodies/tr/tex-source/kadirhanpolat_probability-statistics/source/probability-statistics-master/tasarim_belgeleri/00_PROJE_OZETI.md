# Olasılık Teorisi ve Matematiksel İstatistik — Proje Özeti

> **Yazım Durumu:** TÜM BÖLÜMLER, EKLER VE DERLEME TAMAMLANDI (2026-05-30) — `main-ogrenci.pdf` (168 s.) + `main-egitmen.pdf` (192 s.), sıfır hata.

## Kitabın Kimliği

**Başlık:** Olasılık Teorisi ve Matematiksel İstatistik  
**Hedef Kitle:** Matematik bölümü 3-4. yıl lisans öğrencileri  
**Dil:** Türkçe  
**Yapı:** İki bölümlü (Part I: 11 bölüm, Part II: 8 bölüm) + 6 ek

## Neden Bu Kitap?

Türkiye'deki matematik bölümlerinde olasılık ve istatistik eğitimi ağırlıklı olarak uygulamalı kitaplarla (Akdeniz, Walpole vb.) yürütülmektedir. Bu kitaplar mühendislik ve sosyal bilim öğrencileri için uygundur; ancak matematik öğrencileri için şu boşlukları bırakır:

- Ölçüm teorisi (measure theory) temeli eksik
- Matematiksel ispat odağı zayıf
- Limit teoremleri yüzeysel ele alınır
- İstatistiksel teorinin matematiksel temelleri (Neyman-Pearson, Fisher bilgisi, UMVUE vb.) yetersiz

Bu kitap o boşluğu doldurmayı hedefler: hem sağlam matematiksel temel hem de gerçek istatistiksel derinlik.

## Felsefi Yaklaşım

### Part I — Olasılık Teorisi
- Başlangıçta temel küme ve ölçüm teorisi araçları verilir (σ-cebiri, ölçü, Lebesgue integrali sezgisi)
- Kolmogorov aksiyomatik temeli üzerine inşa edilir
- Klasik olasılık → stokastik süreçlere uzanan bir yol izlenir
- Her teorem ispatlanır; sezgi ile titizlik birlikte yürür

### Part II — Matematiksel İstatistik
- Tahmin teorisi sıfırdan (örneklem dağılımları → nokta tahmin → güven aralıkları)
- Hipotez testinin matematiksel temeli: Neyman-Pearson lemması
- Fisher bilgisi, Cramér-Rao alt sınırı, yeterli istatistikler
- Asimptotik teori: MLE'nin normalliği, delta yöntemi
- Doğrusal modeller ve analiz varyans temelleri

## Referans Kaynaklar

### Temel Alınan / İncelenen Kaynaklar

**Türkçe:**
- Fikri Akdeniz — *Olasılık ve İstatistik* (18. Baskı, 2013, Nobel) [mevcut, kaynaklar/]

**Klasik Olasılık:**
- William Feller — *An Introduction to Probability Theory and Its Applications* (Vol. I & II)
- Andrei Kolmogorov — *Foundations of the Theory of Probability*
- B.V. Gnedenko — *The Theory of Probability*
- Patrick Billingsley — *Probability and Measure*
- Albert Shiryaev — *Probability* (Springer GTM 95)
- Rick Durrett — *Probability: Theory and Examples*

**Klasik Matematiksel İstatistik:**
- Hogg, R.V. & Craig, A.T. — *Introduction to Mathematical Statistics*
- Casella, G. & Berger, R.L. — *Statistical Inference*
- Lehmann, E.L. & Casella, G. — *Theory of Point Estimation*
- Lehmann, E.L. & Romano, J. — *Testing Statistical Hypotheses*
- Mood, Graybill & Boes — *Introduction to the Theory of Statistics*

**Modern:**
- Achim Klenke — *Probability Theory: A Comprehensive Course*
- David Williams — *Probability with Martingales*
- Larry Wasserman — *All of Statistics*
- Blitzstein & Hwang — *Introduction to Probability*
- DeGroot & Schervish — *Probability and Statistics*

## Teknik Özellikler

- **Yazım dili:** Türkçe matematiksel terminoloji (TDK + matematik bölümü geleneği)
- **Notasyon:** ISO 80000-2 standardına yakın; Türkiye'deki standart matematik notasyonu
- **Bölüm yapısı:** Her bölüm → Motivasyon → Teori → İspat → Örnekler → Problemler
- **Problem seviyeleri:** Temel (A), Orta (B), İleri/Araştırma (C)
- **Ekler:** Ölçüm teorisi özeti, analiz önbilgileri, istatistik tabloları

## Kapsam Dışı

Bu kitap aşağıdakileri kasıtlı olarak kapsamaz:
- Hesaplamalı/uygulamalı istatistik (R, Python ile analiz)
- Tam Bayesian istatistik (MCMC, hiyerarşik modeller, Bayes karar teorisi — ayrı bir kitap konusu)
- Makine öğrenmesi istatistiği
- Mühendislik uygulamaları odaklı içerik

**Bayesian not:** Bölüm 12.7'de Bayes tahmincisi, konjugat önsel dağılım, sonsal dağılım ve inanılırlık aralığı (credible interval) tanım düzeyinde ele alınır. Bayes hipotez testi kapsam dışıdır.
