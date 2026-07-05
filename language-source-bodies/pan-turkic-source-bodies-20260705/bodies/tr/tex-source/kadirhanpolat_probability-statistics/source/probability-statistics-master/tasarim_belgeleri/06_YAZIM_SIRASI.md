# Bölüm Yazım Sırası — Bağımsızdan Bağımlıya

> **Karar tarihi:** 2026-05-30  
> **İlke:** Her bölüm yazılmadan önce bağımlı olduğu tüm bölümler tamamlanmış olmalı.

---

## Yazım Sırası

| Sıra | Bölüm | Bağımlı Olduğu Bölümler |
|---|---|---|
| 1 | **Böl. 0** — Ön Bilgiler: Kümeler, Fonksiyonlar, Sayılabilirlik | *(hiçbiri)* |
| 2 | **Böl. 1** — Ölçüm Teorisinin Temelleri | ← 0 |
| 3 | **Böl. 2** — Olasılık Uzayları | ← 0, 1 |
| 4 | **Böl. 3** — Rasgele Değişkenler ve Dağılımlar | ← 1, 2 |
| 5 | **Böl. 4** — Beklenti ve Momentler | ← 1, 2, 3 |
| 6 | **Böl. 5** — Önemli Dağılım Aileleri | ← 3, 4 |
| 7 | **Böl. 7** — Büyük Sayılar Kanunları | ← 2, 3, 4 |
| 8 | **Böl. 6** — Dönüşümler ve Dağılım Teorisi | ← 3, 4, 5 |
| 9 | **Böl. 8** — Merkezi Limit Teoremi ve Asimptotik Teori | ← 4, 7 |
| 10 | **Böl. 11** — İstatistiğin Temelleri: Model ve Örneklem | ← 3, 4, 5, 6, 7, 8 |
| 11 | **Böl. 9** *(opsiyonel)* — Koşullu Beklenti ve Martingaller | ← 4, 7, 8 |
| 12 | **Böl. 12** — Nokta Tahmini | ← 5, 7, 8, 11 |
| 13 | **Böl. 10** *(opsiyonel)* — Stokastik Süreçlere Giriş | ← 7, 8, 9 |
| 14 | **Böl. 13** — Güven Aralıkları | ← 11, 12 |
| 15 | **Böl. 14** — Hipotez Testi | ← 11, 12, 13 |
| 16 | **Böl. 17** *(opsiyonel)* — Parametresiz İstatistik | ← 11, 14 |
| 17 | **Böl. 18** *(opsiyonel)* — Asimptotik İstatistik | ← 8, 12, 14 |
| 18 | **Böl. 15** — Doğrusal Modeller ve Regresyon | ← 11, 12, 13, 14 |
| 19 | **Böl. 16** — Varyans Analizi (ANOVA) | ← 15 |

---

## Notlar

- **Paralel yazılabilecekler:** Böl. 5 ve Böl. 7 birbirine bağımlı değil; aynı anda ilerlenebilir. Benzer şekilde Böl. 9 ve Böl. 11.
- **Opsiyonel bölümler** (9, 10, 17, 18): Çekirdek bölümler tamamlandıktan sonra ele alınır.
- **Ekler** (A-F): İlgili bölümler yazıldıkça paralel olarak hazırlanabilir.

---

## İlerleme Durumu

| Bölüm | Durum | Not |
|---|---|---|
| Böl. 0 | **Sıradaki** | `part1_olasilik/bolum00_onbilgiler.tex` iskeleti hazır |
| Böl. 1–19 | Bekliyor | |

## LaTeX Altyapısı Durumu

| Dosya | Durum |
|---|---|
| `bolumler/olasilik.sty` | ✓ Hazır |
| `bolumler/maarif.sty` | ✓ Hazır (alcozum + alistirma eklendi) |
| `bolumler/main-ogrenci.tex` | ✓ Hazır |
| `bolumler/main-egitmen.tex` | ✓ Hazır |
