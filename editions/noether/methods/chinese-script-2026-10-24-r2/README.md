# 中文版与可重现的繁体字形式

本著作集有一个中文译本，以简体中文为基础，并提供由程式生成、另行维护的繁体字形式。繁体字形式沿用简体文本的词汇；它不是另一个独立译本，也不宣称已作台湾、香港或澳门的区域语言本地化。两种字形的正文及其订正版均有各自的可编辑LaTeX与PDF。

## 制作方法与署名

| 工作 | 制作者／软体 | 日期与范围 |
|---|---|---|
| 数学原著 | Emmy Noether及各篇署名的共同作者；讲义由M. Deuring记录 | 各篇原刊年份与出处见正文 |
| 继承的早期中文AI译文 | Manuscript Typesetting Project / OpenAI Codex；最初逐段翻译的准确模型及推理设定尚未确定 | 早期汇编日期为2026-06-12；这是版本日期，不是全部翻译工作的日期 |
| R9中文汇编及繁体字转换程式 | OpenAI Codex — GPT-5.6 Sol，Ultra推理强度 | 2026-08-12；保留既有中文译文并编制繁简字形转换程式，并不据此将所有早期译文归给该模型 |
| 字形转换 | `opencc-python-reimplemented` 0.1.7，`s2t`设定 | 2026-08-12；只作一次转换，保护数学定界符内的内容，再套用固定正规化规则 |
| 当前正文的AI订正与排版 | OpenAI Codex — GPT-6 Astra，Ultra推理强度 | 2026-10-23—2026-10-24；具体原著作者及历史译文署名仍然保留 |
| 本公开重建程式与版本设定 | OpenAI Codex — GPT-6 Astra，Ultra推理强度 | 2026-10-24；沿用GPT-5.6 Sol的转换函式，加入可移植介面和指定版本的字形、排版与正文设定 |

最初转换的简体输入SHA-256为`638D2F3FB7D915004A62F420CB4DF647711054E2022DCD125A755D8094B53D2E`，繁体输出为`D2A26D0F8D3AC8F20A0CCC906CAA3398F5FE643AB7F0B0113A10BE22447434FA`。当前两种字形各自继承其历史正文；因此重建当前繁体档需要指定版本设定，不能仅对最新简体档盲目重复转换。第二次转换可能改动「了」「只」等字，故不以重复转换达到稳定作为方法。

`script_conversion.py`保留数学定界符辨识、定界符外的一次`s2t`转换及明确列出的十项正规化。`profiles/`辨认两种当前输入及输出，并提供其所需的字形、数学式中的中文文字、字型、版本说明及正文设定。它们重建已公开的特定档案，不构成语言或整部著作正确性的认证。

## 使用程式

需要Python 3.9或以上，以及下列指定套件：

```sh
python -m pip install -r requirements.txt
python reproduce_release.py --variant base --output reader-base.tex
python reproduce_release.py --variant emendations --output reader-emendations.tex
```

程式从指定GitHub版本取得简体LaTeX；亦可用`--input 路径`指定同一档案的本地副本。程式核对输入、转换设定、字典及输出的SHA-256；身分不符即停止，且不覆写既有输出。每个版本设定均附直接公开来源网址。原排版程式在`build-hans.py`和`build-hant.py`，应放入对应完整原始档ZIP解压后的根目录使用；所需字型与TeX套件见该包的说明。

## 软体与权利

OpenCC Python实作作者为Yichen Huang（Eugene），原始专案为[opencc-python](https://github.com/yichen0831/opencc-python)；OpenCC为[开放中文转换](https://github.com/BYVoid/OpenCC)。本套件不重新分发其程式或字典，须依其原始Apache许可条款安装使用。版本设定中的数学文本与衍生内容仍适用各自权利声明；本说明不授予新的整体许可。AI制作或字形转换不改变原著和继承译文的作者身分。
