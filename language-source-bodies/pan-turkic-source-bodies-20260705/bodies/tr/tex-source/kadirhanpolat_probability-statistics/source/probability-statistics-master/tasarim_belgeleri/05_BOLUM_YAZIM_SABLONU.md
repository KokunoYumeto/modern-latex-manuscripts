# Bölüm Yazım Şablonu — Olasılık Teorisi ve Matematiksel İstatistik

> Bu belge, kitabın her bölümü için uyulacak yapıyı, tipografi kurallarını ve içerik kalıplarını tanımlar.

---

## 1. Bölüm Kapağı

```
═══════════════════════════════════════════════════════
BÖLÜM [N]

[BÖLÜM BAŞLIĞI]

"[Seçilmiş alıntı — matematikçi ya da düşünür]"
                                        — Ad Soyad (yıl)

Ön Koşullar: Bölüm X, Bölüm Y
Tahmini Okuma Süresi: ~ [n] saat
═══════════════════════════════════════════════════════
```

---

## 2. Bölüm Başı Kazanım Listesi (TYMM Gereksinimi)

Her bölümün başında net, ölçülebilir öğrenme çıktıları:

```
Bu bölümün sonunda öğrenci:
• [Kavram]'ı tanımlayabilmeli ve örnekler üretebilmeli
• [Teorem]'i ispatlayabilmeli
• [Yöntem]'i uygulayarak problem çözebilmeli
• ...  (5-7 madde)
```

---

## 3. Motivasyon (1-3 Sayfa)

**Amaç:** Öğrencinin "neden bu bölümü öğreniyorum?" sorusunu yanıtlamak.

**Yapı:**
1. Somut bir problem ya da paradoks (matematiksel ya da gerçek hayattan)
2. **Köprü Kurma (TYMM):** "Lise matematiğinde ... gördünüz. Bu bölümde o bilgiyi ... için kullanacağız." (1-2 cümle)
3. "Bu bölümde şunları öğreneceğiz..." (kazanım listesine bağlantı)
4. Bu bölümün kitabın genel yapısındaki yeri (1 cümle)

**Örnek kalıp:**
> Bir saati boyunca gelecek olan yolcu sayısını tahmin etmek istiyorsunuz...  
> Bu bölümde şunları öğreneceğiz:  
> — Rasgele bir değişkenin beklentisinin Lebesgue integrali olarak nasıl tanımlandığını  
> — Beklentinin önemli özellikleri ve eşitsizlikleri  
> — ...

---

## 3. Tarihsel Not (Opsiyonel, 0.5-1 Sayfa)

```
┌──────────────────────────────────────────────────────┐
│ TARİHSEL NOT                                         │
│                                                      │
│ [Konu ile ilgili tarihi arka plan; konuyu geliştiren │
│ matematikçiler; tarihsel motivasyon]                 │
│                                                      │
│ Kaynaklar: [...]                                     │
└──────────────────────────────────────────────────────┘
```

---

## 4. Ana İçerik Yapısı

### 4.1. Tanım Kutusu

```
╔══════════════════════════════════════════════════════╗
║ TANIM N.k — [Tanım Adı]                              ║
║                                                      ║
║ [Matematiksel tanım]                                 ║
║                                                      ║
║ [Eğer varsa: "Buna ... da denir."]                   ║
╚══════════════════════════════════════════════════════╝
```

**Kurallar:**
- Her tanımın bir numarası var: N bölüm numarası, k sıra numarası
- Tanım yalnızca matematiksel içerik; motivasyon önceden verilmiş olmalı
- İngilizce terim parantez içinde, tanımın ilk satırında

### 4.2. Teorem Kutusu

```
╔══════════════════════════════════════════════════════╗
║ TEOREM N.k — [Teorem Adı]                            ║
║                                                      ║
║ [Hipotezler (Varsayımlar)]                           ║
║                                                      ║
║ [Sonuç / İddia]                                      ║
╚══════════════════════════════════════════════════════╝
```

**Kurallar:**
- Her teoremin hemen ardından ispat gelir
- İspat "İspat." başlığı ile açılır, "□" ile kapanır
- İspat birden fazla adım içeriyorsa numaralandırılır: **Adım 1, Adım 2, ...**

### 4.3. İspat Yapısı

```
İspat.
[Fikir: Bu teoremin neden doğru olduğuna dair sezgisel açıklama — 1-2 cümle]

[Tam ispat:]
  Adım 1. ...
  Adım 2. ...
  ...
□
```

**Kurallar:**
- "Fikir:" kısmı zorunludur; matematiği "kara büyü" gibi göstermez
- Her adım kendi paragrafında
- Uzun ispatlar lemmalar ile bölünür

### 4.4. Lemma

```
LEMMA N.k — [Lemma Adı]
[İçerik]
İspat. [...] □
```

Lemma, teoremin ispatında kullanılan ara sonuçtur.

### 4.5. Sonuç (Corollary)

```
SONUÇ N.k — [Sonuç Adı]
[Teoremin özel bir durumu ya da doğrudan çıkarımı]
İspat. Teorem N.j'den doğrudan elde edilir. □
```

### 4.6. Önerme (Proposition)

Teorem kadar önemli olmayan ama ispatlanması gereken sonuçlar için:

```
ÖNERME N.k
[İçerik]
İspat. [...] □
```

### 4.7. Uyarı Kutusu

```
┌──────────────────────────────────────────────────────┐
│ ⚠ UYARI                                              │
│                                                      │
│ [Sık yapılan hata, dikkat edilmesi gereken incelik,  │
│ ya da karşı-örnek]                                   │
└──────────────────────────────────────────────────────┘
```

### 4.8. Not Kutusu

```
┌──────────────────────────────────────────────────────┐
│ NOT                                                  │
│                                                      │
│ [Ek bilgi, bağlantı, yorum]                          │
└──────────────────────────────────────────────────────┘
```

### 4.9. Geometrik / Sezgisel Yorum Kutusu

```
┌──────────────────────────────────────────────────────┐
│ SEZGİSEL YORUM                                       │
│                                                      │
│ [Bu sonucun geometrik, grafik ya da fiziksel          │
│ yorumu]                                              │
└──────────────────────────────────────────────────────┘
```

### 4.10. Disiplinlerarası Bağlantı Kutusu (TYMM Gereksinimi)

Her bölümde en az 1 adet:

```
┌──────────────────────────────────────────────────────┐
│ DİSİPLİNLERARASI BAĞLANTI                           │
│                                                      │
│ [Bu kavramın fizik / biyoloji / ekonomi /            │
│ mühendislik / sosyal bilimlerdeki kullanımı;         │
│ somut bir örnek]                                     │
└──────────────────────────────────────────────────────┘
```

---

## 5. Çözümlü Örnekler (Her Bölümde En Az 8 Örnek)

### Örnek Başlığı

```
Örnek N.k.
[Problem ifadesi]

Çözüm.
[Adım adım çözüm]

[Yorum (gerekliyse): Bu sonuç ... anlamına gelir.]
```

**Seviye dağılımı:**
- Örneklerin ~40%'ı A seviyesi (doğrudan tanım uygulaması)
- ~40%'ı B seviyesi (birden fazla kavramı birleştiren)
- ~20%'si C seviyesi (ispat veya ileri analiz gerektiren)

---

## 6. Bölüm Sonu Özeti (0.5 Sayfa)

```
─────────────────────────────────────────────────────
BÖLÜM ÖZETİ

Bu bölümde öğrendiklerimiz:
• [Kavram 1]: ...
• [Kavram 2]: ...
• [Önemli teorem]: ...
• [Önemli bağlantı]: ...

Notasyon özeti:
  [simge] — [açıklama]
  ...
─────────────────────────────────────────────────────
```

---

## 7. Bölüm Sonu Alıştırma Yapısı

### Üç Çıktı, Tek Kaynak

`maarif.sty`'nin `\ifmaarifcozum` mekanizması üç farklı PDF üretir:

| Dosya | İçerik | Hedef |
|---|---|---|
| `main-ogrenci.tex` | Çözümlü alıştırmalar + çözümsüz problemler | Öğrenci |
| `main-egitmen.tex` | Tüm problemlerin tam çözümleri | Eğitmen kılavuzu |
| `main-tam.tex` | Her şey görünür | İç arşiv |

### Bölüm Sonu Sırası

```
\cozumlualistirmalar   % ── Çözümlü Alıştırmalar başlığı ──

\begin{alistirma}[Al.N.1]{A}{Başlık}
  [Problem ifadesi]
\end{alistirma}
\alcozum{[Tam çözüm — öğrencide görünür, her iki sürümde]}

\begin{alistirma}[Al.N.2]{B}{Başlık}
  [Problem ifadesi]
\end{alistirma}
\alcozum{[Tam çözüm — öğrencide görünür]}

\alistirmalar           % ── Alıştırmalar başlığı ──

\begin{alistirma}[Al.N.3]{A}{Başlık}
  [Problem ifadesi]
\end{alistirma}
\alcozum{[Tam çözüm — YALNIZCA eğitmen sürümünde görünür]}

\begin{alistirma}[Al.N.4]{B}{Başlık}
  [Problem ifadesi]
\end{alistirma}
\alcozum{[Tam çözüm — YALNIZCA eğitmen sürümünde görünür]}

\begin{alistirma}[Al.N.5]{C}{Başlık}
  [İspat gerektiren / araştırma sorusu]
\end{alistirma}
\alcozum{[İpucu + tam çözüm — YALNIZCA eğitmen sürümünde]}
```

### Alıştırma Yazım Kuralları

- **Çözümlü alıştırmalar:** Bölüm içi örneklerden daha uzun; birden fazla adım içeren, rehberli problem çözümü. Hem öğrenci hem eğitmen sürümünde tam çözüm görünür.
- **Çözümsüz alıştırmalar:** Öğrenci sürümünde çözüm yok. `\alcozum{}` her zaman yazılır ama yalnızca eğitmen PDF'inde görünür.
- C seviyesi problemlerde `\alcozum{}` içinde önce `\begin{ipucu}{1}...\end{ipucu}` ipucu hiyerarşisi, ardından tam çözüm.

### Minimum Alıştırma Sayısı

| Bölüm türü | Çözümlü | A (çözümsüz) | B (çözümsüz) | C (çözümsüz) | Toplam |
|---|---|---|---|---|---|
| Teori ağırlıklı (Böl. 1-9) | 3 | 6 | 6 | 4 | 19+ |
| İstatistik ağırlıklı (Böl. 11-16) | 4 | 8 | 8 | 5 | 25+ |

---

## 8. Bölüm Başı Ön Koşul Tablosu

Her bölümün başında:

```
┌──────────────────────────────────────────────────────┐
│ BU BÖLÜMÜ OKUMADAN ÖNCE                              │
│                                                      │
│ Bilinmesi gerekenler:                                │
│  □ Gerçel analiz: limit, süreklilik, Riemann integ.  │
│  □ Bölüm 1: σ-cebiri, Lebesgue integrali            │
│  □ Bölüm 2: Olasılık uzayı, bağımsızlık             │
│                                                      │
│ Bu bölümün kullanıldığı sonraki bölümler:            │
│  → Bölüm 4 (beklenti için)                          │
│  → Bölüm 11 (örneklem dağılımları için)             │
└──────────────────────────────────────────────────────┘
```

---

## 9. İçerik Sırası — Standart Akış

```
[Bölüm Kapağı]
[Kazanım Listesi]              ← TYMM
[Motivasyon + Köprü Kurma]     ← TYMM
[Tarihsel Not — isteğe bağlı]
  §N.1. [Alt bölüm başlığı]
    [kesif + \ogrencialani]    ← tanımdan önce keşif
    [tanimgerekce]             ← neden bu tanım böyle?
    [Tanımlar]
    [kritiksorgu]              ← koşul kalkarsa?
    [Teoremler + İspatlar]
    [ispatiskele]              ← B seviyesi için
    [hataanalizi / karsiornek]
    [disiplinlerarası bağlantı] ← TYMM
    [kendinleifade]
    [mikroozet]
  §N.2. [...]
  ...
[Bölüm Özeti]
[ozyansima]                    ← TYMM
[kopru]                        ← ileri okuma + sonraki bölüm
[Çözümlü Alıştırmalar]         ← \cozumlualistirmalar
[Alıştırmalar: A / B / C]      ← \alistirmalar (eğitmende çözümlü)
[Kaynaklar ve İleri Okuma]
```

---

## 10. LaTeX Ortamları — Kaynak Dosyalar

Kitap iki stil dosyası kullanır:

| Dosya | İçerik |
|---|---|
| `maarif.sty` | Pedagojik kutular (motivasyon, kesif, hataanalizi, alistirma, alcozum, …) |
| `olasilik.sty` | Matematik ortamları (tanim, teorem, ispat, …) + olasılık makroları |

### `olasilik.sty` Ortamları (topoloji.sty yapısından türetilecek)

```latex
% Teorem ortamları
\newtheorem{tanim}{Tanım}[chapter]
\newtheorem{teorem}[tanim]{Teorem}
\newtheorem{onerme}[tanim]{Önerme}
\newtheorem{lemma}[tanim]{Lemma}
\newtheorem{sonuc}[tanim]{Sonuç}
\newtheorem{ornek}[tanim]{Örnek}
\newtheorem*{uyari}{Uyarı}
\newtheorem*{notkutu}{Not}
\renewcommand{\qedsymbol}{$\blacksquare$}

% Olasılık makroları
\newcommand{\P}{\mathbb{P}}
\newcommand{\E}{\mathbb{E}}
\newcommand{\Var}{\operatorname{Var}}
\newcommand{\Cov}{\operatorname{Cov}}
\newcommand{\Cor}{\operatorname{Cor}}
\newcommand{\iid}{\overset{\text{i.i.d.}}{\sim}}
\newcommand{\asto}{\xrightarrow{\text{n.k.}}}   % neredeyse kesin
\newcommand{\pto}{\xrightarrow{\mathbb{P}}}      % olasılıkla
\newcommand{\dto}{\xrightarrow{d}}               % dağılımla
\newcommand{\sigalg}{\mathcal{F}}
\newcommand{\Borel}{\mathcal{B}}
\newcommand{\olas}[1]{(\Omega,\mathcal{F},#1)}   % olasılık uzayı
```

### `maarif.sty` Pedagojik Kutular — Kullanım Örneği

```latex
\begin{motivasyon}
  Bir saati boyunca gelen araç sayısını modelliyoruz...
\end{motivasyon}

\begin{kesif}[σ-cebiri neden gerekli?]
  Hangi küme ailesi olasılık için "iyi" çalışır? Deneyin:
  \ogrencialani[4cm]
\end{kesif}

\begin{tanimgerekce}
  Sadece sonlu kesişim değil, sayılabilir kesişim istiyoruz çünkü...
\end{tanimgerekce}

\begin{tanim}[σ-Cebiri]
  ...
\end{tanim}

\begin{kritiksorgu}
  Sayılabilirlik koşulu kalksa ne bozulur?
\end{kritiksorgu}

% Bölüm sonu
\cozumlualistirmalar
\begin{alistirma}[Al.2.1]{A}{Örnek σ-cebirleri}
  ...
\end{alistirma}
\alcozum{Çözüm adımları...}

\alistirmalar
\begin{alistirma}[Al.2.5]{B}{İspat}
  ...
\end{alistirma}
\alcozum{Tam ispat — yalnızca eğitmen PDF'inde görünür.}
```

### Üretim Komutu

```latex
% main-ogrenci.tex
\usepackage{maarif}          % \alcozum gizli

% main-egitmen.tex
\usepackage[cozumler]{maarif} % \alcozum görünür
```

---

## 11. Dil ve Üslup Kuralları

1. **Cümle uzunluğu:** Teoremler ve tanımlar için kısa, kesin cümleler. Açıklamalar için biraz daha uzun ama aşırıya kaçmadan.

2. **Aktif ifadeler:** "Kanıtlıyoruz" değil "kanıtlayacağız"; "gösterilir" değil "göstereceğiz" — okuyucuyu dahil eden üslup.

3. **"Açıktır ki" ve "kolayca görülür" ifadelerinden kaçın:** Her adım açıklanır.

4. **Soru cümleleri:** İspatın ara noktalarında "Peki neden...?" şeklinde sorular sorun — öğrenci gibi düşünün.

5. **İlk geçiş kuralı:** Her teknik terimin Türkçe adı ilk kullanımda İngilizce karşılığıyla birlikte verilir: *yeterli istatistik (sufficient statistic)*.

6. **Dipnot politikası:** Kısa açıklamalar ve terminoloji notları için dipnot. Tarihsel notlar ve genişlemeler için kutu veya bölüm sonu notu.
