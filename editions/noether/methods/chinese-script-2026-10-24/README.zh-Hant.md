# 中文版與可重現的繁體字形式

本著作集有一個中文譯本，以簡體中文為基礎，並提供由程式生成、另行維護的繁體字形式。繁體字形式沿用簡體文本的詞彙；它不是另一個獨立譯本，也不宣稱已作臺灣、香港或澳門的區域語言本地化。兩種字形的正文及其訂正版均有各自的可編輯LaTeX與PDF。

## 製作方法與署名

| 工作 | 製作者／軟體 | 日期與範圍 |
|---|---|---|
| 數學原著 | Emmy Noether及各篇署名的共同作者；講義由M. Deuring記錄 | 各篇原刊年份與出處見正文 |
| 繼承的早期中文AI譯文 | Manuscript Typesetting Project / OpenAI Codex；最初逐段翻譯的準確模型及推理設定尚未確定 | 早期彙編日期為2026-06-12；這是版本日期，不是全部翻譯工作的日期 |
| R9中文彙編及繁體字轉換程式 | OpenAI Codex — GPT-5.6 Sol，Ultra推理強度 | 2026-08-12；保留既有中文譯文並編製繁簡字形轉換程式，並不據此將所有早期譯文歸給該模型 |
| 字形轉換 | `opencc-python-reimplemented` 0.1.7，`s2t`設定 | 2026-08-12；只作一次轉換，保護數學定界符內的內容，再套用固定正規化規則 |
| 當前正文的AI訂正與排版 | OpenAI Codex — GPT-6 Astra，Ultra推理強度 | 2026-10-23—2026-10-24；具體原著作者及歷史譯文署名仍然保留 |
| 本公開重建程式與版本設定 | OpenAI Codex — GPT-6 Astra，Ultra推理強度 | 2026-10-24；沿用GPT-5.6 Sol的轉換函式，加入可移植介面和指定版本的字形、排版與正文設定 |

最初轉換的簡體輸入SHA-256為`638D2F3FB7D915004A62F420CB4DF647711054E2022DCD125A755D8094B53D2E`，繁體輸出為`D2A26D0F8D3AC8F20A0CCC906CAA3398F5FE643AB7F0B0113A10BE22447434FA`。當前兩種字形各自繼承其歷史正文；因此重建當前繁體檔需要指定版本設定，不能僅對最新簡體檔盲目重複轉換。第二次轉換可能改動「了」「只」等字，故不以重複轉換達到穩定作為方法。

`script_conversion.py`保留數學定界符辨識、定界符外的一次`s2t`轉換及明確列出的十項正規化。`profiles/`辨認兩種當前輸入及輸出，並提供其所需的字形、數學式中的中文文字、字型、版本說明及正文設定。它們重建已公開的特定檔案，不構成語言或整部著作正確性的認證。

## 使用程式

需要Python 3.9或以上，以及下列指定套件：

```sh
python -m pip install -r requirements.txt
python reproduce_release.py --variant base --output reader-base.tex
python reproduce_release.py --variant emendations --output reader-emendations.tex
```

程式從指定GitHub版本取得簡體LaTeX；亦可用`--input 路徑`指定同一檔案的本地副本。程式核對輸入、轉換設定、字典及輸出的SHA-256；身分不符即停止，且不覆寫既有輸出。每個版本設定均附直接公開來源網址。原排版程式在`build-hans.py`和`build-hant.py`，應放入對應完整原始檔ZIP解壓後的根目錄使用；所需字型與TeX套件見該包的說明。

## 軟體與權利

OpenCC Python實作作者為Yichen Huang（Eugene），原始專案為[opencc-python](https://github.com/yichen0831/opencc-python)；OpenCC為[開放中文轉換](https://github.com/BYVoid/OpenCC)。本套件不重新分發其程式或字典，須依其原始Apache許可條款安裝使用。版本設定中的數學文本與衍生內容仍適用各自權利聲明；本說明不授予新的整體許可。AI製作或字形轉換不改變原著和繼承譯文的作者身分。
