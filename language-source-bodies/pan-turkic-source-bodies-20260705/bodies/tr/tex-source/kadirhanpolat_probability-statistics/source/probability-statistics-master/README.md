# Olasılık Teorisi ve Matematiksel İstatistik

**Matematik bölümü öğrencileri için iki bölümlü ders kitabı**

---

## Kitap Hakkında

Bu proje, Türkiye'deki matematik bölümlerindeki bir boşluğu doldurmak için başlatılmıştır. Mevcut Türkçe kaynaklar ya mühendislik odaklı uygulamalı (Akdeniz, Walpole) ya da İngilizce (Feller, Casella-Berger) olduğundan, matematik öğrencileri için **ispatlı, ölçüm teorisi bilinçli ve Türkçe** bir kaynağa ihtiyaç duyulmaktadır.

### Ayırt Edici Özellikler

- Tüm teoremler ispatlanmıştır
- Ölçüm teorisi temeli verilmiştir (Bölüm 1)
- Neyman-Pearson lemması, Cramér-Rao alt sınırı, UMVUE gibi matematiksel istatistiğin temelleri
- Problem seviyeleri: A (temel) → B (orta) → C (araştırma)
- Türkçe yazılmış, her terimin İngilizce karşılığı parantez içinde

---

## Yapı

### Part I — Olasılık Teorisi (Bölüm 0–10)

| Bölüm | Konu |
|---|---|
| 0 | Ön Bilgiler: Kümeler, Fonksiyonlar, Sayılabilirlik |
| 1 | Ölçüm Teorisinin Temelleri (σ-cebiri, Lebesgue) |
| 2 | Olasılık Uzayları (Kolmogorov aksiyomları) |
| 3 | Rasgele Değişkenler ve Dağılımlar |
| 4 | Beklenti ve Momentler |
| 5 | Önemli Dağılım Aileleri |
| 6 | Dönüşümler ve Dağılım Teorisi |
| 7 | Büyük Sayılar Kanunları |
| 8 | Merkezi Limit Teoremi ve Asimptotik Teori |
| 9* | Koşullu Beklenti ve Martingaller |
| 10* | Stokastik Süreçlere Giriş |

### Part II — Matematiksel İstatistik (Bölüm 11–18)

| Bölüm | Konu |
|---|---|
| 11 | İstatistiksel Model ve Örneklem Dağılımları |
| 12 | Nokta Tahmini (MLE, UMVUE, Cramér-Rao) |
| 13 | Güven Aralıkları |
| 14 | Hipotez Testi (Neyman-Pearson, UMP testler) |
| 15 | Doğrusal Modeller ve Regresyon |
| 16 | Varyans Analizi (ANOVA) |
| 17* | Parametresiz İstatistik |
| 18* | Asimptotik İstatistik |

*Opsiyonel bölümler: İki sömestrlik programlar veya lisansüstü için

---

## Ders Programı Seçenekleri

**1 Sömestr Olasılık:** Bölüm 0–8  
**1 Sömestr İstatistik:** Bölüm 11–16 (Bölüm 7-8 önkoşul)  
**2 Sömestr Tam Program:** Tüm çekirdek bölümler  
**Lisansüstü Yoğun (14 hafta):** Bölüm 1–8 + 11–14 + seçimlik

---

## Ön Koşullar

- Gerçel Analiz (limit, türev, Riemann integrali, dizi ve seriler)
- Lineer Cebir (matris, determinant, lineer dönüşüm, öz değer)
- İspat Teknikleri (dolaylı ispat, tümevarım, karşı-örnek)

Ölçüm teorisi **ön koşul değildir**; Bölüm 1'de kitap içinde verilmektedir.

---

## Referans Kaynaklar

### Klasik Olasılık
- Feller, W. — *An Introduction to Probability Theory and Its Applications* (Vol. I & II)
- Billingsley, P. — *Probability and Measure*
- Shiryaev, A.N. — *Probability* (Springer GTM 95)
- Durrett, R. — *Probability: Theory and Examples*
- Gnedenko, B.V. — *The Theory of Probability*

### Klasik Matematiksel İstatistik
- Casella, G. & Berger, R.L. — *Statistical Inference*
- Hogg, R.V., McKean, J.W. & Craig, A.T. — *Introduction to Mathematical Statistics*
- Lehmann, E.L. & Casella, G. — *Theory of Point Estimation*
- Lehmann, E.L. & Romano, J. — *Testing Statistical Hypotheses*
- Mood, Graybill & Boes — *Introduction to the Theory of Statistics*
- Wackerly, Mendenhall & Scheaffer — *Mathematical Statistics with Applications*
- Bickel, P.J. & Doksum, K.A. — *Mathematical Statistics* (Vol. I)
- Meyer, P.L. — *Introductory Probability and Statistical Applications* (1970)

### Modern
- Klenke, A. — *Probability Theory: A Comprehensive Course*
- Williams, D. — *Probability with Martingales*
- Wasserman, L. — *All of Statistics*
- Blitzstein, J. & Hwang, J. — *Introduction to Probability*
- DeGroot, M.H. & Schervish, M.J. — *Probability and Statistics*
- Gut, A. — *Probability: A Graduate Course*

### Türkçe (temel alınan)
- Akdeniz, F. — *Olasılık ve İstatistik* (Nobel, 18. baskı, 2013)

---

## Proje Dosyaları

```
tasarim_belgeleri/
├── 00_PROJE_OZETI.md          — Proje felsefesi, hedef kitle, kapsam
├── 01_ICINDEKILER_TASLAK.md   — 18 bölümlük detaylı içindekiler + kaynak haritası
├── 02_KAYNAK_ANALIZI.md       — ~20 referans kitap, tam içindekiler, karşılaştırma tablosu
├── 03_PEDAGOJIK_YAKLASIM.md   — Bölüm mimarisi, ispat felsefesi, ders programları
├── 04_TERMINOLOJI_SOZLUGU.md  — Türkçe-İngilizce terim sözlüğü ve notasyon standartları
└── 05_BOLUM_YAZIM_SABLONU.md  — Tanım/Teorem/İspat şablonları, LaTeX ortamları
```

Teknik detaylar ve PDF okuma notu için `CLAUDE.md`'ye bakın.

---

## Durum

**Tasarım Belgeleri: v1.0 — TAMAMLANDI** (2026-05-29)

| Belge | İçerik | Durum |
|---|---|---|
| `00_PROJE_OZETI.md` | Proje felsefesi, hedef kitle, kapsam | ✅ |
| `01_ICINDEKILER_TASLAK.md` | 18 bölümlük içindekiler + kaynak haritası | ✅ |
| `02_KAYNAK_ANALIZI.md` | ~20 kitap, tam içindekiler, karşılaştırma | ✅ |
| `03_PEDAGOJIK_YAKLASIM.md` | Bölüm yapısı, ispat felsefesi, problem seviyeleri | ✅ |
| `04_TERMINOLOJI_SOZLUGU.md` | Türkçe-İngilizce terim sözlüğü | ✅ |
| `05_BOLUM_YAZIM_SABLONU.md` | LaTeX bölüm şablonu | ✅ |

**Sonraki Aşama:** Pilot bölüm yazımı (LaTeX)
