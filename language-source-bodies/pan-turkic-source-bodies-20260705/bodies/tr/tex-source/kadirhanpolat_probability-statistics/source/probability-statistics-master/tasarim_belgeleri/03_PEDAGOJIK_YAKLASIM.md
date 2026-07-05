# Pedagojik Yaklaşım ve Yazım İlkeleri

> **Son güncelleme:** 2026-05-29

---

## 1. Hedef Kitle Profili

### Birincil Hedef: Matematik Bölümü Lisans Öğrencisi (3-4. yıl)
- Gerçel analiz (Cantor, Weierstrass, Riemann integrali) bilgisine sahip
- Lineer cebir biliyor (matris, determinant, lineer dönüşüm)
- Soyut cebir giriş düzeyinde (grup, halka kavramı)
- İspat yazma deneyimi var (dolaylı ispat, tümevarım, karşı-örnek)
- Olasılık ve istatistikle ya hiç tanışmamış ya da mühendislik düzeyinde tanışmış

### İkincil Hedef: Lisansüstü Öğrenci (ön hazırlık)
- Yüksek lisans girişinde istatistik dersi geçmek zorunda kalanlar
- Olasılık/istatistiğin matematiksel temellerini kendi başına öğrenmek isteyenler

---

## 2. Bölüm Yapısı

Her bölüm aşağıdaki mimariye uyar:

```
[Motivasyon]        ← 1-2 sayfa; "bu bölümde ne öğreneceğiz ve neden?"
[Tarihsel Not]      ← isteğe bağlı; konuyu insan tarihi içinde konumlandırır
[Tanım / Aksiyom]  ← kutu içinde; numaralı
[Teorem]            ← kutu içinde; numaralı; her teoremin ispatı var
[İspat]             ← açık; gösterim bazen sezgiyle başlar, sonra tam ispat
[Örnek]             ← çözümlü; en az 3 örnek (kolay → orta → ileri)
[Yorum / Uyarı]    ← "Dikkat:" veya "Not:" kutucukları
[Problemler]        ← üç seviye: A (temel), B (orta), C (araştırma)
```

---

## 3. İspat Felsefesi

### İlke 1: Her Teorem İspatlanır
- Hiçbir teorem "ispatsız verilir" olarak geçmez.
- Uzun teknik ispatlar (örn. Kolmogorov'un 0-1 kanunu) tam olarak verilir; ara lemmaları bölümlere ayrılır.

### İlke 2: Sezgiden Titizliğe
Her ispat şu yapıyı izler:
1. **Fikir:** İspat neden işe yarıyor? (1-2 cümle, informal)
2. **Tam İspat:** Epsilon-delta düzeyinde titiz
3. **Açıklama (gerekirse):** Adımlar neden çalıştı?

### İlke 3: Karşı-Örnek Kültürü
- "Bu koşul neden gerekli?" → her önemli hipotez için karşı-örnek gösterilir.
- Öğrenciye: "Hangi adımda bu koşulu kullandık?"

### İlke 4: Titizlik Ölçüm Teorisinden Devşirilir
- Lebesgue integrali açıkça tanımlanmaz (bu bir analiz kitabı değil), ama gerektiğinde kullanılır.
- Ek B'de referans verilir.

---

## 4. Terminoloji İlkeleri

### Türkçe-İngilizce Denge
- Yerleşik Türkçe terimler kullanılır (TDK + matematik topluluğu geleneği)
- Her terimin ilk geçişinde İngilizce karşılığı parantez içinde verilir: *büyük sayılar kanunu (law of large numbers)*
- Tartışmalı çeviriler için dipnot

### Terim Tutarlılığı (Sözlük)
| İngilizce | Kullanılacak Türkçe |
|---|---|
| Random variable | Rasgele değişken |
| Distribution function | Dağılım fonksiyonu |
| Probability space | Olasılık uzayı |
| Sample space | Örnek uzay |
| Event | Olay |
| Expected value | Beklenti (beklenen değer değil) |
| Variance | Varyans |
| Estimator | Tahmin edici |
| Sufficient statistic | Yeterli istatistik |
| Likelihood function | Olabilirlik fonksiyonu |
| Hypothesis test | Hipotez testi |
| Power function | Güç fonksiyonu |
| Confidence interval | Güven aralığı |
| Almost surely / a.s. | Neredeyse kesin / n.k. |
| σ-algebra | σ-cebiri |
| Measurable | Ölçülebilir |
| Convergence in distribution | Dağılımla yakınsama |
| Convergence in probability | Olasılıkla yakınsama |
| UMVUE | BVTY (en küçük varyanslı tarafsız tahmin edici) |

---

## 5. Notasyon Standartları

```
P(A)           — Olasılık ölçüsü
E[X]           — Beklenti
Var(X)         — Varyans  
Cov(X,Y)       — Kovaryans
ρ(X,Y)         — Korelasyon
f_X(x)         — Yoğunluk fonksiyonu
F_X(x)         — Dağılım fonksiyonu
φ_X(t)         — Karakteristik fonksiyon
M_X(t)         — Moment üreten fonksiyon
X ~ N(μ,σ²)   — X dağılımı
X_n →^p X      — Olasılıkla yakınsama
X_n →^d X      — Dağılımla yakınsama
X_n →^{a.s.} X — Neredeyse kesin yakınsama
L(θ|x)         — Olabilirlik fonksiyonu
ℓ(θ|x)         — Log-olabilirlik
I(θ)           — Fisher bilgisi
Ω              — Örnek uzay
ℱ              — σ-cebiri
(Ω, ℱ, P)      — Olasılık uzayı
```

---

## 6. Örnek ve Problem Seviyeleri

### Seviye A — Temel Anlama
- Doğrudan tanım uygulaması
- Hesaplama ağırlıklı
- Kısa cevaplı

### Seviye B — Orta Düzey
- Birden fazla kavramı birleştiren
- Kısmi ispat içerebilen
- Bir önceki teoremden çıkarım

### Seviye C — İleri / Araştırma
- İspat gerektiren
- Kitapta açıkça verilmeyen sonuçlara uzanan
- Teorik genelleme

---

## 7. Özel Kutular

```
┌─────────────────────────────────────┐
│ TARİHSEL NOT                        │
│ Pascal ile Fermat'ın 1654 mektupları│
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ ⚠ UYARI                             │
│ Bu teoremin hipotezi gerekmektedir  │
│ çünkü...                            │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ 💡 GEOMETRİK YORUM                  │
│ Bu sonuç geometrik olarak şu anlama │
│ gelir...                            │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ KARŞI-ÖRNEK                         │
│ Hipotez olmadan teorem yanlış olur: │
│ X = ...                             │
└─────────────────────────────────────┘
```

---

## 8. Ders Programı Seçenekleri

### Seçenek A: 1 Sömestr Olasılık (30 hafta × 3 saat = 90 saat)
Bölümler: 0 → 8 (Opsiyonel 9-10 dahil değil)  
Hedef: Matematiksel olasılığa tam giriş

### Seçenek B: 1 Sömestr İstatistik (30 hafta × 3 saat = 90 saat)
Bölümler: 11 → 16 (Örneklem dağılımları hızlıca, asıl vurgu 12-15)  
Önkoşul: Seçenek A veya denk

### Seçenek C: 2 Sömestr Tam Program
Her iki Part'ın tamamı; opsiyonel bölümler seçimlik

### Seçenek D: Yoğun Lisansüstü Giriş (14 hafta)
Bölüm 1-8 (hızlı) + 11-14 + Ek okumalar

---

## 9. Bölüm Başına Tahmini Sayfa Sayısı

| Bölüm | Konu | Tahmini Sayfa |
|---|---|---|
| 0 | Ön bilgiler | 15 |
| 1 | Ölçüm teorisi | 45 |
| 2 | Olasılık uzayları | 40 |
| 3 | Rasgele değişkenler | 50 |
| 4 | Beklenti ve momentler | 45 |
| 5 | Dağılım aileleri | 60 |
| 6 | Dönüşümler | 35 |
| 7 | Büyük sayılar kanunları | 45 |
| 8 | Merkezi limit teoremi | 40 |
| 9 | Martingaller (opsiyonel) | 40 |
| 10 | Stokastik süreçler (opsiyonel) | 35 |
| 11 | İstatistiksel model ve örneklem | 50 |
| 12 | Nokta tahmin | 55 |
| 13 | Güven aralıkları | 35 |
| 14 | Hipotez testi | 55 |
| 15 | Doğrusal modeller | 45 |
| 16 | ANOVA | 30 |
| 17 | Parametresiz (opsiyonel) | 30 |
| 18 | Asimptotik istatistik (opsiyonel) | 35 |
| Ekler | A-F | 60 |
| **Toplam (opsiyoneller dahil)** | | **~800 sayfa** |
| **Toplam (çekirdek)** | | **~580 sayfa** |
