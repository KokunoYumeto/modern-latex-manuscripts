from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_DIR = ROOT / "evidence"

INPUTS = {
    "source_whole": (
        ROOT / "source" / "P20_CurrentGerman_lines12377_12588.tex",
        "CBC9E9CF34E6475F4256C935A58378FCDBF85A09ACC0E592FC64F3FCFDF8744D",
    ),
    "source_a": (
        ROOT / "segments" / "source" / "P20_A_lines12377_12437.tex",
        "DFD92DE298F422E2D993CC3162E3B031D41E4ECB67E32CB967FE0A1FD6CF237E",
    ),
    "source_b": (
        ROOT / "segments" / "source" / "P20_B_lines12438_12519.tex",
        "25D5BCDA8B4A35D789A8A33D256BC08FB779E057567A1673761FD7D7F97AD81E",
    ),
    "source_c": (
        ROOT / "segments" / "source" / "P20_C_lines12520_12588.tex",
        "D7B2FC4C6FB95125109A83F5F856F27B319FE25F4ABF13B3AAE6D33A99D5C2C1",
    ),
    "hans_a": (
        ROOT / "segments" / "zh-Hans-CN" / "P20_A_zh-Hans-CN.tex",
        "DC694B77A78B1D12E12BC5A3DA315147538847F23F0E46772D85A7BAE9181834",
    ),
    "hans_b": (
        ROOT / "segments" / "zh-Hans-CN" / "P20_B_zh-Hans-CN.tex",
        "143C7386FCB9DDA7159C2F7D9A2C9547530D9AED786648A85ACD488D14A8A491",
    ),
    "hans_c": (
        ROOT / "segments" / "zh-Hans-CN" / "P20_C_zh-Hans-CN.tex",
        "8972FC4AA515FF93047D0F686DFD9CCB4003287E2F815313F02BAC079ED9D734",
    ),
    "hans_target": (
        ROOT / "zh-Hans-CN" / "Noether_Paper20_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex",
        "262430D0A092818F859516F3FD5DE612D897D0BD8AAC49605BE047E389963065",
    ),
    "hant_target": (
        ROOT
        / "zh-Hant-controlled"
        / "Noether_Paper20_Chinese_CurrentAuthority_zh-Hant-controlled_v001.tex",
        "17EE7ECD25A298D8818144CE41273A31DEB85F3E49A02F08D5335B6815FF20C0",
    ),
    "return_a": (
        ROOT / "worker_returns" / "P20_A_TRANSLATOR_RETURN.md",
        "94E5A487D08A67BD692D4BC283F1C8770231D5A96F6553B8FEECD43658AD0662",
    ),
    "return_b": (
        ROOT / "worker_returns" / "P20_B_TRANSLATOR_RETURN.md",
        "4E924E588A08B14806DC5D3812D852DEAA67F23F2E8A516A1FFB7D30C9FB1816",
    ),
    "return_c": (
        ROOT / "worker_returns" / "P20_C_TRANSLATOR_RETURN.md",
        "E0C5631F520867B2BB37E78E8593453091447573AC5ECECE96A60EAE615D8520",
    ),
}

SOURCE_KEYS = ("source_a", "source_b", "source_c")
HANS_KEYS = ("hans_a", "hans_b", "hans_c")
RETURN_KEYS = ("return_a", "return_b", "return_c")

EVIDENCE_CLASS = (
    "producer terminology proposal extracted only from the supplied Paper 20 German fragments, "
    "PRC-oriented Hans producer segments/current target, and worker returns; inherited Chinese "
    "witness unconsulted; no source comparison, terminology adjudication, translation review, "
    "or independent validation"
)
HANT_STATUS = (
    "controlled generic script record only; not zh-Hant-TW/HK/MO; "
    "regional lexical localization absent"
)
REVIEW_STATE = "independent check absent; pending"
JA_KO_STATUS = "JA and KO unconsulted and non-authorizing for Chinese"

ALLOWED_BASINS = {
    "Sino-xenic inherited",
    "modern Sino-xenic coinage/calque",
    "global modern loan",
    "native coinage",
    "mixed/contested",
    "unresolved",
}


def T(
    german: str,
    hans: str,
    hant: str,
    locator: str,
    scope: str,
    sense: str,
    excluded: str,
    alternatives: str,
    basin: str,
    debt: str,
    note: str,
) -> dict[str, str]:
    return {
        "german": german,
        "hans": hans,
        "hant": hant,
        "locator": locator,
        "scope": scope,
        "sense": sense,
        "excluded": excluded,
        "alternatives": alternatives,
        "basin": basin,
        "debt": debt,
        "note": note,
    }


TERMS = [
    T(
        "absolute Irreduzibilität",
        "绝对不可约性",
        "絕對不可約性",
        "segments/source/P20_A_lines12377_12437.tex; source lines 12377, 12384, and 12386",
        "irreducibility retained after passage from the coefficient field to an algebraically closed extension",
        "The paper's field-independent irreducibility condition: the polynomial remains irreducible over the stated algebraically closed extension.",
        "irreducibility only over one fixed coefficient field; absolute value; primality of an integer; inability to simplify an expression",
        "绝对不可约; 绝对既约性; 绝对不可分解性",
        "modern Sino-xenic coinage/calque",
        "Qualitative medium debt: 绝对不可约性 is strongly normalized in Mainland algebra, but adjective/noun granularity and historical non-Mainland forms were not researched.",
        "The proposal records the producer title and theorem wording without external Chinese terminology certification.",
    ),
    T(
        "Reduzibilitätsform",
        "可约性形式",
        "可約性形式",
        "segments/source/P20_A_lines12377_12437.tex line 12386; segments/source/P20_C_lines12520_12588.tex lines 12564–12573",
        "the constructed coefficient-and-parameter form whose nonvanishing gives the paper's criterion for absolute irreducibility",
        "A specially constructed reducibility-detecting form R(Z,u), not a generic description of any reducible form.",
        "a reduced normal form; a factorable polynomial itself; a reduction formula; a discriminant automatically",
        "可约形式; 可约判别形式; 可约性判别式",
        "mixed/contested",
        "Qualitative high debt: 可约性形式 is transparent Mainland prose, while 可约形式 and 判别式 compounds are strong lexical attractors and regional historical usage is absent.",
        "The compound is a producer proposal for Noether's named construction, not a claim that it coincides with a modern discriminant.",
    ),
    T(
        "algebraisch-abgeschlossener Körper",
        "代数闭域",
        "代數閉域",
        "segments/source/P20_A_lines12377_12437.tex line 12384",
        "a field in which every one-variable polynomial splits into linear factors, as stated in the source footnote",
        "An algebraically closed field in the field-theoretic sense used to define absolute irreducibility.",
        "the algebraic closure as an extension object; a topologically closed set; a merely complete field; any algebraic extension",
        "代数封闭域; 代数闭体; 代数闭包",
        "modern Sino-xenic coinage/calque",
        "Qualitative medium debt: 代数闭域 is Mainland-standard-looking, but 闭域 can attract topological closure and non-Mainland historical labels were not consulted.",
        "The sense window distinguishes the field property from the algebraic closure construction.",
    ),
    T(
        "Koeffizientenbereich",
        "系数域",
        "係數域",
        "segments/source/P20_A_lines12377_12437.tex lines 12384 and 12392",
        "the field containing the coefficients of the polynomial under discussion",
        "The coefficient field serving as the base field for irreducibility and extension.",
        "a numerical range of coefficient values; a coefficient ring without a field assumption; a domain of a coefficient function; a list of coefficients",
        "系数范围; 系数所在域; 系数体",
        "mixed/contested",
        "Qualitative high debt: the producer narrows the historical Bereich to 域 from context; this Mainland field-term inference and regional 体/域 preferences were not independently researched.",
        "The row exposes that 系数域 is a contextual producer narrowing rather than a literal surface calque.",
    ),
    T(
        "homogene Form",
        "齐次形式",
        "齊次形式",
        "segments/source/P20_A_lines12377_12437.tex lines 12388 and 12427; segments/source/P20_B_lines12438_12519.tex line 12463",
        "a homogeneous polynomial form obtained by adjoining one variable and homogenizing the polynomial",
        "A homogeneous algebraic form in the polynomial/form sense used throughout the reduction.",
        "a differential form; an arbitrary homogeneous function; visual formatting; a form with merely equal-looking terms",
        "齐次型; 齐次多项式; 齐式",
        "modern Sino-xenic coinage/calque",
        "Qualitative medium debt: 齐次形式 is broad Mainland wording; 型 and 多项式 variants may better mark the algebraic object, and regional convention was not researched.",
        "The producer keeps the historical broad noun 形式 while the sense window fixes the polynomial context.",
    ),
    T(
        "Graderniedrigung",
        "降次",
        "降次",
        "segments/source/P20_A_lines12377_12437.tex lines 12386 and 12427; segments/source/P20_C_lines12520_12588.tex lines 12547, 12552, and 12577",
        "a drop in polynomial degree caused by specialization or dehomogenization, distinguished from factorization",
        "Degree reduction of the specialized inhomogeneous polynomial in the exact exceptional case discussed by the paper.",
        "dimension reduction; reduction modulo an ideal; cancellation without degree loss; the paper's proof reduction; lowering an index",
        "次数降低; 降低次数; 度数下降",
        "mixed/contested",
        "Qualitative high debt: the current producer target contains both 降次 and 次数降低; selecting 降次 for indexing does not resolve that internal lexical variation or regional preference.",
        "Competing producer surface forms are retained explicitly for independent convergence.",
    ),
    T(
        "Ideal aus Polynomen",
        "多项式理想",
        "多項式理想",
        "segments/source/P20_A_lines12377_12437.tex line 12425",
        "the ideal formed by polynomial relations Phi(Z) that vanish after the stated substitution",
        "An ideal in the relevant polynomial ring, characterized by closure under difference and multiplication by arbitrary ring polynomials.",
        "a single ideal polynomial; a module merely because the historical text mentions that label; an idealized polynomial; a numerical ideal",
        "多项式所成理想; 多项式族理想; 多项式环中的理想",
        "modern Sino-xenic coinage/calque",
        "Qualitative medium debt: 多项式理想 is concise Mainland terminology but can ambiguously name an ideal generated by polynomials rather than this specific relation ideal; regional wording is untested.",
        "The scope records the source's defining closure property without certifying a preferred modern algebra label.",
    ),
    T(
        "Primideal",
        "素理想",
        "素理想",
        "segments/source/P20_A_lines12377_12437.tex line 12425; segments/source/P20_C_lines12520_12588.tex lines 12571 and 12577",
        "a prime ideal, both the relation ideal P and prime ideals used in the arithmetic reduction theorem",
        "A prime ideal in the commutative-algebra or algebraic-number-theory sense instantiated by the local passage.",
        "a prime number; a maximal ideal automatically; a principal ideal; an optimal or primary objective",
        "质理想; 质素理想; prime ideal",
        "modern Sino-xenic coinage/calque",
        "Qualitative high debt: 素理想 is strongly Mainland-normalized while 質理想 is a significant regional attractor; the controlled Hant glyph record does not settle that lexical choice.",
        "The same producer form spans two local prime-ideal contexts; independent review must confirm whether one term is suitable for both.",
    ),
    T(
        "Nullstelle",
        "零点",
        "零點",
        "segments/source/P20_A_lines12377_12437.tex lines 12423, 12425, and 12427; segments/source/P20_C_lines12520_12588.tex line 12558",
        "a zero of the polynomial ideal or its basis polynomials, viewed as a coefficient tuple",
        "A point or value system at which the stated polynomial relations vanish.",
        "the scalar zero coefficient; a root only of a one-variable polynomial; a point at infinity; a null vector with no polynomial relation",
        "根; 消失点; 零值点",
        "mixed/contested",
        "Qualitative high debt: 零点 is compact Mainland usage but alternates between root and algebraic-set point senses; the tuple-valued sense and regional forms remain under-specified.",
        "The sense window prevents the short form from silently collapsing the algebraic-set and univariate-root readings.",
    ),
    T(
        "Parameterdarstellung",
        "参数表示",
        "參數表示",
        "segments/source/P20_A_lines12377_12437.tex line 12427; segments/source/P20_C_lines12520_12588.tex line 12558",
        "the representation Gamma=C(A,B) of the ideal's zeros by parameters A and B in an extension field",
        "A parametrization or parameter representation of coefficient tuples in the paper's converse construction.",
        "displaying parameter values; a statistical parameterization; a coordinate chart automatically; a merely symbolic substitution",
        "参数化表示; 参数表示式; 参数化",
        "mixed/contested",
        "Qualitative high debt: 参数表示 is Mainland-readable but may describe notation rather than surjective parametrization; 参数化 is a strong modern attractor and regional usage is unknown.",
        "The evidence row records the intended representational role without claiming global geometric parametrization properties.",
    ),
    T(
        "Kroneckersche Substitution",
        "Kronecker 代换",
        "Kronecker 代換",
        "segments/source/P20_A_lines12377_12437.tex line 12429; segments/source/P20_B_lines12438_12519.tex line 12445",
        "the exponent-encoding substitution sending the multivariable polynomial to a one-variable polynomial",
        "Kronecker's substitution in the specific base-d exponent encoding used in equations (4) and (5).",
        "Kronecker product; Kronecker delta; an arbitrary substitution named Kronecker; simple variable replacement with no exponent encoding",
        "克罗内克代换; 克罗内克替换; Kronecker 替换",
        "mixed/contested",
        "Qualitative high debt: the mixed Latin-name Mainland form follows producer practice, while full Chinese transliteration and 代换/替换 alternatives remain open and regionally unresearched.",
        "No personal-name standard was adjudicated.",
    ),
    T(
        "induzierte Exponenten",
        "诱导指数",
        "誘導指數",
        "segments/source/P20_B_lines12438_12519.tex lines 12453, 12457, 12461, and 12463; segments/source/P20_C_lines12520_12588.tex line 12543",
        "the exponents generated by the Kronecker substitution from bounded multivariable exponent tuples",
        "The encoded one-variable exponents induced by the source's base-d substitution.",
        "the exponent of a group; an induced representation; a general derived exponent; a statistical index; every exponent occurring after arbitrary multiplication",
        "导出指数; 所得指数; 诱生指数",
        "modern Sino-xenic coinage/calque",
        "Qualitative high debt: 诱导指数 is a direct Mainland calque that can attract representation-theoretic induction; no historical or regional terminology shelf was consulted.",
        "The explicit substitution sense is required because the compact Chinese form is trap-prone.",
    ),
    T(
        "Norm",
        "范数",
        "範數",
        "segments/source/P20_A_lines12377_12437.tex line 12433; segments/source/P20_B_lines12438_12519.tex lines 12465 and 12486",
        "the field norm formed as the product of the distinct conjugates of zeta over the field generated by t(a,b)",
        "An algebraic field norm in the product-of-conjugates construction used to build T(t,u).",
        "a vector or matrix norm; normalization; magnitude; a social standard; the degree of a polynomial",
        "域范数; 代数范数; 诺姆",
        "modern Sino-xenic coinage/calque",
        "Qualitative high debt: 范数 is dominant Mainland vocabulary but strongly attracts analytic vector-norm senses; the field qualifier and regional alternatives were not researched.",
        "The sense window supplies the field-norm qualifier omitted by the producer's short form.",
    ),
    T(
        "symmetrische Elementarfunktionen",
        "基本对称函数",
        "基本對稱函數",
        "segments/source/P20_B_lines12438_12519.tex lines 12480 and 12495",
        "the homogenized elementary symmetric functions r,s,t used to express symmetric functions of the a,b rows",
        "Elementary symmetric functions in the local homogenized construction, linear in each stated row.",
        "an arbitrary symmetric function; an elementary analytic function; a symmetric tensor; a basis function merely invariant under one swap",
        "初等对称函数; 初等对称多项式; 基本对称多项式",
        "mixed/contested",
        "Qualitative high debt: 基本对称函数 is the producer wording, while 初等对称多项式 is a powerful Mainland attractor; historical Funktion granularity and regional conventions are unresearched.",
        "The entry deliberately leaves 基本 versus 初等 and 函数 versus 多项式 unresolved.",
    ),
    T(
        "Konjugierte",
        "共轭量",
        "共軛量",
        "segments/source/P20_B_lines12438_12519.tex line 12486",
        "the distinct conjugates of zeta obtained by permuting the a,b row and multiplied to form the norm",
        "Algebraic conjugates relative to the stated permutation and field-norm construction.",
        "complex conjugation only; a conjugate subgroup; matrix transpose or adjoint; an arbitrary paired expression",
        "共轭式; 共轭因子; 共轭元",
        "mixed/contested",
        "Qualitative high debt: 共轭量 is an explanatory Mainland producer form; 元, 式, and 因子 compete according to algebraic object type, and regional evidence is absent.",
        "The producer later uses 共轭因子 locally; this row does not adjudicate convergence between the two forms.",
    ),
    T(
        "Erweiterungskörper",
        "扩张域",
        "擴張域",
        "segments/source/P20_A_lines12377_12437.tex lines 12425 and 12427; segments/source/P20_B_lines12438_12519.tex lines 12463 and 12508; segments/source/P20_C_lines12520_12588.tex lines 12534–12558",
        "a field extension in which coefficients or factors required by the proof exist",
        "An extension field of the relevant coefficient field, sometimes algebraic as explicitly qualified by the source.",
        "the algebraic closure automatically; a vector-space extension; continuation of a function; geographic or software extension",
        "扩域; 延拓域; 扩张体",
        "mixed/contested",
        "Qualitative high debt: the current producer text contains both 扩域 and 扩张域; this indexing choice favors explicit Mainland morphology but does not resolve that variation or regional 体/域 usage.",
        "The evidence shelf preserves 扩域 as an active producer alternative.",
    ),
    T(
        "Satz von Ostrowski",
        "奥斯特罗夫斯基定理",
        "奧斯特羅夫斯基定理",
        "segments/source/P20_C_lines12520_12588.tex line 12566",
        "the theorem that the algebraic-integer-coefficient polynomial remains irreducible modulo all but finitely many prime ideals",
        "The specific Ostrowski theorem stated and derived in Paper 20, not every theorem bearing the same name.",
        "Ostrowski's valuation theorem; the Ostrowski gap theorem; a theorem about numerical stability; an unqualified eponym",
        "Ostrowski 定理; 奥斯特洛夫斯基定理; 奥斯特罗夫斯基命题",
        "mixed/contested",
        "Qualitative high debt: the full Simplified-Chinese transliteration is Mainland-oriented, while Latin retention and variant transliterations are live and the eponym is multiply ambiguous.",
        "The sense window is essential because the eponym alone does not identify this arithmetic irreducibility theorem.",
    ),
    T(
        "ganze rationale, ganzzahlige Funktion",
        "整有理、整系数函数",
        "整有理、整係數函數",
        "segments/source/P20_A_lines12377_12437.tex line 12386",
        "the historical description of the coefficient-and-indeterminate function assigned to each generic polynomial",
        "The producer's literalized record of a polynomial-like rational integral function with integer coefficients in the source's historical algebraic register.",
        "an arbitrary rational function; an integer-valued function; an entire holomorphic function; a constant integer; any polynomial without the rational qualifier",
        "整系数多项式; 有理整函数; 整的有理整系数函数",
        "unresolved",
        "Qualitative high debt: the historical German stack ganze rationale, ganzzahlige is not transparently aligned with modern PRC taxonomy; the producer phrase risks both analytic and arithmetic misreadings.",
        "This entry records unresolved historical terminology rather than collapsing it to 整系数多项式 without checker authority.",
    ),
    T(
        "Basispolynome",
        "基多项式",
        "基多項式",
        "segments/source/P20_A_lines12377_12437.tex line 12425",
        "the finite polynomial basis or generating family used to state the common-zero conditions of the prime ideal",
        "Polynomials serving as a finite basis/generating set for the ideal in the local argument.",
        "a basis of a polynomial vector space automatically; Lagrange basis polynomials; one base polynomial; a basis function in approximation theory",
        "基底多项式; 生成多项式; 理想基",
        "mixed/contested",
        "Qualitative high debt: 基多项式 is concise Mainland wording but may attract interpolation or vector-space bases; 基底 and 生成族 distinctions were not adjudicated.",
        "The row keeps the ideal-generating context explicit and leaves modern basis taxonomy to checking.",
    ),
    T(
        "irreduzibles algebraisches Gebilde",
        "不可约代数构形",
        "不可約代數構形",
        "segments/source/P20_A_lines12377_12437.tex line 12427",
        "the irreducible algebraic object defined by the prime ideal in the historical geometric argument",
        "A historically phrased irreducible algebraic locus or object associated with the prime ideal.",
        "an irreducible algebraic variety automatically under a modern scheme; an algebraic expression; a geometric figure unrelated to an ideal; a molecular structure",
        "不可约代数簇; 不可约代数集; 不可约代数形体",
        "unresolved",
        "Qualitative high debt: 构形 is a producer hedge for historical Gebilde; modern Mainland 簇 and 集 are strong but mathematically more committal attractors, with no source-era or regional evidence consulted.",
        "The broad producer form intentionally avoids silently identifying the historical object with one modern category.",
    ),
    T(
        "ganze algebraische Zahlen",
        "代数整数",
        "代數整數",
        "segments/source/P20_C_lines12520_12588.tex line 12571",
        "algebraic integers used as coefficients in the arithmetic application",
        "Algebraic numbers integral over the ordinary integers, in the coefficient hypothesis of the Ostrowski theorem.",
        "ordinary rational integers only; arbitrary algebraic numbers; integer-valued functions; coefficients merely written without denominators",
        "整代数数; 代数整元; algebraic integers",
        "modern Sino-xenic coinage/calque",
        "Qualitative medium debt: 代数整数 is strongly normalized in Mainland algebra, while historical 整代数数 and regional variants were not researched.",
        "The entry separates this narrower class from the earlier generic algebraic-number coefficients.",
    ),
    T(
        "algebraisch gebrochene Zahlen",
        "代数分数",
        "代數分數",
        "segments/source/P20_C_lines12520_12588.tex line 12579",
        "the historical coefficient class for which a common denominator Delta is cleared before reduction modulo prime ideals",
        "Algebraic fractional numbers in the source's denominator-clearing passage; the precise modern field-of-fractions taxonomy is left open.",
        "ordinary rational fractions only; arbitrary algebraic numbers; fractional ideals; rational functions; a broken or approximate number",
        "分式代数数; 代数有理数; 代数数分式",
        "unresolved",
        "Qualitative high debt: 代数分数 is a literal Mainland-readable producer form but its historical scope is uncertain and it may be mistaken for elementary fractions; no regional evidence was consulted.",
        "The worker return explicitly leaves this historical class for checker adjudication.",
    ),
    T(
        "Restklassen",
        "剩余类",
        "剩餘類",
        "segments/source/P20_C_lines12520_12588.tex line 12577",
        "residue classes modulo a prime ideal, which form the residue field used in the irreducibility argument",
        "Congruence or residue classes in the quotient by the specified prime ideal.",
        "leftover categories; a remainder as a scalar; a social class; arbitrary equivalence classes without the modular ideal",
        "同余类; 模剩余类; 残余类",
        "mixed/contested",
        "Qualitative high debt: 剩余类 is Mainland-standard-looking, while 同余类 and regional 餘類 forms are strong attractors; the controlled Hant script form is not regional terminology evidence.",
        "The sense window binds the proposal to the residue-field construction rather than generic equivalence classes.",
    ),
]


TERM_HEADERS = [
    "decision_id",
    "source_locator",
    "exact_german_phrase",
    "concept_scope",
    "zh_hans_cn_choice",
    "sense_window",
    "excluded_senses",
    "alternatives_considered",
    "lexical_attractor_basin",
    "mandarin_simplified_dominance_risk_debt",
    "evidence_class",
    "controlled_hant_form",
    "controlled_hant_status",
    "independent_check_status",
    "producer_note",
]

ADVERSE_HEADERS = [
    "adverse_id",
    "term_decision_id",
    "source_locator",
    "exact_german_phrase",
    "zh_hans_cn_producer_choice",
    "trap_or_adverse_reading",
    "contextual_reason_for_exclusion",
    "alternative_held_for_independent_review",
    "lexical_attractor_basin",
    "mandarin_simplified_dominance_risk_debt",
    "evidence_class",
    "controlled_hant_status",
    "review_state",
]

CROSSWALK_HEADERS = [
    "crosswalk_id",
    "term_decision_id",
    "source_locator",
    "exact_german_phrase",
    "zh_hans_cn_producer_form",
    "zh_hant_controlled_form",
    "zh_hant_status",
    "ja_form",
    "ko_form",
    "ja_ko_evidence_status",
    "sense_window",
    "excluded_senses",
    "lexical_attractor_basin",
    "mandarin_simplified_dominance_risk_debt",
    "evidence_class",
    "independent_check_status",
]

TERM_KEYS = {
    "german",
    "hans",
    "hant",
    "locator",
    "scope",
    "sense",
    "excluded",
    "alternatives",
    "basin",
    "debt",
    "note",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def manifest_sha(keys: tuple[str, ...], hashes: dict[str, str]) -> str:
    payload = "\n".join(f"{key}|{hashes[key]}" for key in keys).encode("utf-8")
    return hashlib.sha256(payload).hexdigest().upper()


def validate_terms() -> None:
    if not 20 <= len(TERMS) <= 24:
        raise RuntimeError(f"Expected 20–24 terms, got {len(TERMS)}")
    for index, term in enumerate(TERMS, 1):
        if set(term) != TERM_KEYS:
            raise RuntimeError(
                f"Term {index} has invalid shape: missing={TERM_KEYS - set(term)}, "
                f"extra={set(term) - TERM_KEYS}"
            )
        if term["basin"] not in ALLOWED_BASINS:
            raise RuntimeError(f"Term {index} has invalid basin: {term['basin']}")
        for key in TERM_KEYS:
            if not term[key].strip():
                raise RuntimeError(f"Term {index} has empty required field: {key}")
        if not term["debt"].startswith("Qualitative "):
            raise RuntimeError(f"Term {index} dominance debt is not explicitly qualitative")


def validate_inputs() -> dict[str, str]:
    actual: dict[str, str] = {}
    for key, (path, expected_sha) in INPUTS.items():
        if not path.is_file():
            raise FileNotFoundError(f"Required input absent: {path}")
        actual_sha = sha256(path)
        if actual_sha != expected_sha:
            raise RuntimeError(f"{key} SHA mismatch: expected {expected_sha}, got {actual_sha}")
        actual[key] = actual_sha
    actual["source_manifest"] = manifest_sha(SOURCE_KEYS, actual)
    actual["hans_manifest"] = manifest_sha(HANS_KEYS, actual)
    actual["return_manifest"] = manifest_sha(RETURN_KEYS, actual)
    actual["generator"] = sha256(Path(__file__))
    return actual


def write_csv(path: Path, headers: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=headers,
            quoting=csv.QUOTE_ALL,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def make_term_rows() -> list[dict[str, str]]:
    rows = []
    for index, term in enumerate(TERMS, 1):
        rows.append(
            {
                "decision_id": f"P20-ZH-T{index:03d}",
                "source_locator": term["locator"],
                "exact_german_phrase": term["german"],
                "concept_scope": term["scope"],
                "zh_hans_cn_choice": term["hans"],
                "sense_window": term["sense"],
                "excluded_senses": term["excluded"],
                "alternatives_considered": term["alternatives"],
                "lexical_attractor_basin": term["basin"],
                "mandarin_simplified_dominance_risk_debt": term["debt"],
                "evidence_class": EVIDENCE_CLASS,
                "controlled_hant_form": term["hant"],
                "controlled_hant_status": HANT_STATUS,
                "independent_check_status": REVIEW_STATE,
                "producer_note": term["note"],
            }
        )
    return rows


def make_adverse_rows() -> list[dict[str, str]]:
    rows = []
    for index, term in enumerate(TERMS, 1):
        rows.append(
            {
                "adverse_id": f"P20-ZH-A{index:03d}",
                "term_decision_id": f"P20-ZH-T{index:03d}",
                "source_locator": term["locator"],
                "exact_german_phrase": term["german"],
                "zh_hans_cn_producer_choice": term["hans"],
                "trap_or_adverse_reading": term["excluded"],
                "contextual_reason_for_exclusion": term["sense"],
                "alternative_held_for_independent_review": term["alternatives"],
                "lexical_attractor_basin": term["basin"],
                "mandarin_simplified_dominance_risk_debt": term["debt"],
                "evidence_class": EVIDENCE_CLASS,
                "controlled_hant_status": HANT_STATUS,
                "review_state": REVIEW_STATE,
            }
        )
    return rows


def make_crosswalk_rows() -> list[dict[str, str]]:
    rows = []
    for index, term in enumerate(TERMS, 1):
        rows.append(
            {
                "crosswalk_id": f"P20-ZH-X{index:03d}",
                "term_decision_id": f"P20-ZH-T{index:03d}",
                "source_locator": term["locator"],
                "exact_german_phrase": term["german"],
                "zh_hans_cn_producer_form": term["hans"],
                "zh_hant_controlled_form": term["hant"],
                "zh_hant_status": HANT_STATUS,
                "ja_form": "",
                "ko_form": "",
                "ja_ko_evidence_status": JA_KO_STATUS,
                "sense_window": term["sense"],
                "excluded_senses": term["excluded"],
                "lexical_attractor_basin": term["basin"],
                "mandarin_simplified_dominance_risk_debt": term["debt"],
                "evidence_class": EVIDENCE_CLASS,
                "independent_check_status": REVIEW_STATE,
            }
        )
    return rows


def make_graph(hashes: dict[str, str]) -> dict:
    nodes = []
    edges = []
    for index, term in enumerate(TERMS, 1):
        suffix = f"{index:03d}"
        locus_id = f"P20-LOC-{suffix}"
        concept_id = f"P20-CON-{suffix}"
        hans_id = f"P20-HANS-{suffix}"
        hant_id = f"P20-HANT-{suffix}"
        choice_id = f"P20-CHOICE-{suffix}"
        nodes.extend(
            [
                {
                    "id": locus_id,
                    "type": "source_locus",
                    "locator": term["locator"],
                    "exact_german_phrase": term["german"],
                },
                {
                    "id": concept_id,
                    "type": "concept",
                    "scope": term["scope"],
                    "sense_window": term["sense"],
                    "excluded_senses": term["excluded"],
                },
                {
                    "id": hans_id,
                    "type": "form",
                    "language_scope": "zh-Hans-CN producer",
                    "form": term["hans"],
                },
                {
                    "id": hant_id,
                    "type": "form",
                    "language_scope": "zh-Hant-controlled nonregional producer record",
                    "form": term["hant"],
                    "status": HANT_STATUS,
                },
                {
                    "id": choice_id,
                    "type": "producer_choice",
                    "decision_id": f"P20-ZH-T{suffix}",
                    "dominance_risk_debt": term["debt"],
                    "evidence_class": EVIDENCE_CLASS,
                    "review_state": REVIEW_STATE,
                },
            ]
        )
        edges.extend(
            [
                {"id": f"P20-E{suffix}-1", "type": "occurs_at", "from": concept_id, "to": locus_id},
                {"id": f"P20-E{suffix}-2", "type": "decides_for", "from": choice_id, "to": concept_id},
                {"id": f"P20-E{suffix}-3", "type": "selects_hans_form", "from": choice_id, "to": hans_id},
                {
                    "id": f"P20-E{suffix}-4",
                    "type": "records_controlled_hant_form",
                    "from": choice_id,
                    "to": hant_id,
                },
                {"id": f"P20-E{suffix}-5", "type": "controlled_form_of", "from": hant_id, "to": hans_id},
            ]
        )

    source_hashes = "; ".join(f"{key}={hashes[key]}" for key in SOURCE_KEYS)
    hans_hashes = "; ".join(f"{key}={hashes[key]}" for key in HANS_KEYS)
    return_hashes = "; ".join(f"{key}={hashes[key]}" for key in RETURN_KEYS)
    return {
        "graph_id": "NOE-P20-ZH-PRODUCER-CONCEPT-GRAPH-001",
        "work_unit": "Noether Paper 20 Chinese producer translation",
        "graph_status": {
            "purpose": "producer-side translation-decision evidence packaging only",
            "decision_count": len(TERMS),
            "independent_check": "absent",
            "external_native_source_research": "not performed",
            "japanese_or_korean_evidence": "not consulted or used; non-authorizing for Chinese",
            "scan_inspection": "not performed",
            "source_branch_comparison": "not performed",
            "compilation_or_rendering": "not performed by this evidence-packaging subtask; rendered pages not inspected",
            "controlled_hant_scope": HANT_STATUS,
            "translation_validation_or_readiness_claim": "none",
        },
        "provenance": {
            "german_snapshot": {
                "path": (
                    "source/P20_CurrentGerman_lines12377_12588.tex; "
                    "segments/source/P20_A_lines12377_12437.tex; "
                    "segments/source/P20_B_lines12438_12519.tex; "
                    "segments/source/P20_C_lines12520_12588.tex"
                ),
                "sha256": (
                    f"whole={hashes['source_whole']}; manifest={hashes['source_manifest']}; "
                    f"{source_hashes}"
                ),
                "use": "supplied translation-source terminology and locators only; no source/apparatus check or branch comparison",
            },
            "inherited_hans_witness": {
                "path": "not consulted in this evidence-packaging subtask",
                "sha256": "not computed",
                "use": "explicitly excluded from the permitted input set; no witness comparison or audit",
            },
            "hans_target": {
                "path": (
                    "zh-Hans-CN/Noether_Paper20_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex; "
                    "segments/zh-Hans-CN/P20_A_zh-Hans-CN.tex; "
                    "segments/zh-Hans-CN/P20_B_zh-Hans-CN.tex; "
                    "segments/zh-Hans-CN/P20_C_zh-Hans-CN.tex"
                ),
                "sha256": (
                    f"target={hashes['hans_target']}; manifest={hashes['hans_manifest']}; "
                    f"{hans_hashes}"
                ),
                "use": (
                    f"supplied producer proposal record; worker-return manifest={hashes['return_manifest']}; "
                    f"{return_hashes}; independent check absent"
                ),
            },
            "controlled_hant_target": {
                "path": (
                    "zh-Hant-controlled/"
                    "Noether_Paper20_Chinese_CurrentAuthority_zh-Hant-controlled_v001.tex"
                ),
                "sha256": hashes["hant_target"],
                "use": (
                    "hash-bound custody only; not used to choose terminology; controlled generic "
                    "script record without Taiwan/Hong Kong/Macao localization"
                ),
            },
            "evidence_generator": {
                "path": "qa/build_p20_evidence_pack.py",
                "sha256": hashes["generator"],
                "use": (
                    "deterministic packaging of producer terminology proposals into the established "
                    "adjacent CSV and typed-graph shapes"
                ),
            },
            "evidence_class": EVIDENCE_CLASS,
        },
        "node_type_definitions": {
            "source_locus": "Locator and phrase in the supplied German fragment; not a source-validation assertion.",
            "concept": "Producer's bounded sense window and excluded lexical attractors.",
            "form": "Supplied Chinese form with explicit Hans or nonregional controlled-Hant scope.",
            "producer_choice": (
                "Supplied editorial proposal with qualitative Mandarin-Simplified dominance debt and "
                "open review state; lexical-attractor basin is recorded only in the CSV ledgers."
            ),
        },
        "edge_type_definitions": {
            "occurs_at": "Concept to supplied-source locator.",
            "decides_for": "Producer choice to concept.",
            "selects_hans_form": "Producer choice to Hans form.",
            "records_controlled_hant_form": "Producer choice to nonregional controlled-Hant form.",
            "controlled_form_of": (
                "Controlled-Hant script form to Hans lexical base without Taiwan/Hong Kong/Macao equivalence claim."
            ),
        },
        "nodes": nodes,
        "edges": edges,
    }


def main() -> None:
    validate_terms()
    hashes = validate_inputs()
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(EVIDENCE_DIR / "TERMINOLOGY_LEDGER.csv", TERM_HEADERS, make_term_rows())
    write_csv(EVIDENCE_DIR / "ADVERSE_EVIDENCE_LEDGER.csv", ADVERSE_HEADERS, make_adverse_rows())
    write_csv(EVIDENCE_DIR / "CJKV_CROSSWALK.csv", CROSSWALK_HEADERS, make_crosswalk_rows())
    graph_path = EVIDENCE_DIR / "CONCEPT_EVIDENCE_GRAPH.json"
    graph_path.write_text(
        json.dumps(make_graph(hashes), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "rows_each_csv": len(TERMS),
                "nodes": len(TERMS) * 5,
                "edges": len(TERMS) * 5,
                **hashes,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
