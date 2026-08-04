$ErrorActionPreference = 'Stop'

$workspace = Split-Path -Parent $PSScriptRoot
$evidenceDir = Join-Path $workspace 'evidence'
New-Item -ItemType Directory -Force -Path $evidenceDir | Out-Null

$sourceHash = 'F6C923B79406542E3DE64298DCD38887FF9A52141C71B8FF2BEBE6D14625FAEA'
$witnessHash = 'BB4686153D7241CD0F8A74164B6486C31C3BF731722334CC25B5E81AA8884AF8'
$hansHash = 'B121BC5D5649F63904444A25179FB4D882F55EF9435A5C81C1689414639BE8F4'
$hantHash = '36648843726340B02C9B7FF31EEC28008AC3CD66594F469F7769540E29DEFC79'

$evidenceClass = 'producer editorial choice in the assembled Hans target with inherited Simplified-Chinese drafting witness; independent checking absent; provenance binding: German source SHA-256 F6C923B79406542E3DE64298DCD38887FF9A52141C71B8FF2BEBE6D14625FAEA; Hans target SHA-256 B121BC5D5649F63904444A25179FB4D882F55EF9435A5C81C1689414639BE8F4; controlled-Hant target SHA-256 36648843726340B02C9B7FF31EEC28008AC3CD66594F469F7769540E29DEFC79'
$hantStatus = 'controlled generic script derivative only; not zh-Hant-TW/HK/MO; regional lexical localization absent'
$reviewState = 'independent check absent; pending'
$jaKoStatus = 'JA and KO not consulted and not authorized as Chinese evidence'

$terms = @(
    [ordered]@{
        id='001'; locator='title, opening paragraph, and section 4'; german='Endlichkeitssatz'; scope='finiteness theorem asserting finite generation of the invariant system for a finite group'; hans='有限性定理'; hant='有限性定理';
        sense='The named invariant-theoretic theorem establishing that finitely many invariants suffice, as used in the title and later comparison with a separate proof.';
        excluded='finiteness of a set; termination of a procedure; a generic compactness theorem; a theorem merely assuming a finite group';
        alternatives='有限生成定理; 不变量有限定理; 有限定理'; basin='modern Sino-xenic coinage/calque';
        risk='High: 有限性定理 follows Mainland-style abstract-noun compounding and does not itself expose the finite-generation content; regional historical terminology is untested.';
        reason='The title and surrounding argument concern finite generation of invariants, not a bare cardinality or termination statement.';
        note='The compact title form is recorded as the producer selection; whether 有限生成定理 would be clearer remains for independent review.'
    },
    [ordered]@{
        id='002'; locator='title and throughout sections 1--4'; german='Invariante'; scope='polynomial or rational invariant under the stated finite group of linear transformations'; hans='不变量'; hant='不變量';
        sense='An algebraic expression left unchanged by every transformation in the finite group, with absolute and relative subtypes distinguished later.';
        excluded='a merely unchanged numerical parameter; a conserved physical quantity; a topological invariant without this group action; the adjective invariant used without a mathematical object';
        alternatives='不变式; 恒量; invariant'; basin='modern Sino-xenic coinage/calque';
        risk='High: 不变量 is strongly Mainland-standard wording, while 不变式 remains a live mathematical attractor and regional preferences were not researched.';
        reason='The paper explicitly defines the objects by identity under all transformations and repeatedly treats them as algebraic functions.';
        note='The producer uses 不变量 consistently; competing 不变式 terminology remains visible for independent and regional review.'
    },
    [ordered]@{
        id='003'; locator='title, opening paragraph, definition paragraph, and section 4'; german='endliche Gruppe'; scope='finite group of h invertible linear transformations acting on the variables'; hans='有限群'; hant='有限群';
        sense='A group with finitely many elements, here the h listed nonsingular linear transformations A_1 through A_h.';
        excluded='a group containing a finite subset; a bounded family without group structure; a finitely generated infinite group; a nonmathematical social group';
        alternatives='有穷群; 有限阶群; 有限变换群'; basin='modern Sino-xenic coinage/calque';
        risk='Medium: 有限群 is Mainland-standard and transparent in context, but historical 有穷群 and regional register were not investigated.';
        reason='The text enumerates exactly h transformations and explicitly calls them a group.';
        note='The general group-theoretic term is not expanded to 有限变换群 because the producer target retains the compact source label.'
    },
    [ordered]@{
        id='004'; locator='opening paragraph, Hilbert theorem reference'; german='Modulbasis'; scope='module basis in the Hilbert theorem invoked by the customary existence proof'; hans='模基'; hant='模基';
        sense='The module-basis notion in Hilbert''s theorem that supports the customary existence proof for finite invariant systems.';
        excluded='a vector-space basis with no module context; the base ring itself; a matrix basis; a modular arithmetic base';
        alternatives='模的基; 模基定理; 模组基底'; basin='modern Sino-xenic coinage/calque';
        risk='High: 模基 is a compressed Mainland technical compound whose segmentation may be opaque, while 模组基底 reflects a different regional lexical system not researched here.';
        reason='The phrase is explicitly the title-content of the cited Hilbert theorem, not a free-standing basis calculation in the paper.';
        note='The inherited compact form is retained without claiming cross-regional equivalence or terminological certification.'
    },
    [ordered]@{
        id='005'; locator='definition paragraph and sections 1--3'; german='ganze rationale Invariante'; scope='whole rational invariant, historically a polynomial invariant in the variables'; hans='整有理不变量'; hant='整有理不變量';
        sense='An invariant that is a ganze rationale Funktion in the paper''s historical algebraic register, contrasted later with a merely rational absolute invariant.';
        excluded='an invariant taking integer values; an invariant with integer coefficients by default; an arbitrary rational-function invariant; an algebraic integer';
        alternatives='多项式不变量; 整式不变量; 整有理不变式'; basin='mixed/contested';
        risk='High: 整有理 is a literal historical calque that can attract modern readings involving integers rather than polynomials; Mainland terminology and the inherited witness dominate the evidence shelf.';
        reason='The text contrasts ganze rationale invariants with rational invariants and treats the former by polynomial symmetric-function constructions.';
        note='The producer preserves the historical literal form; modernization to 多项式不变量 is an explicit checker decision, not made here.'
    },
    [ordered]@{
        id='006'; locator='definition paragraph and section 3'; german='absolute Invariante'; scope='absolute invariant fixed identically by every transformation, as contrasted with a relative invariant'; hans='绝对不变量'; hant='絕對不變量';
        sense='An invariant unchanged without an accompanying character or scalar factor under the group action.';
        excluded='an absolute value; an invariant independent of all context; a relative invariant; an absolute geometric invariant in an unrelated theory';
        alternatives='绝对不变式; 绝对型不变量; 严格不变量'; basin='modern Sino-xenic coinage/calque';
        risk='High: 绝对不变量 is Mainland-shaped and semantically broad; the precise contrast with 相对不变量 supplies the intended sense, while regional usage remains untested.';
        reason='The paper defines invariance by literal identity and separately labels relative invariants in the final note.';
        note='The modifier 绝对 is retained as the producer choice without asserting a regionally preferred formulation.'
    },
    [ordered]@{
        id='007'; locator='definition paragraph and section 1'; german='Größenreihe'; scope='one indexed row or tuple of transformed variables x^(k) used in the multisymmetric-function argument'; hans='变量组'; hant='變量組';
        sense='A finite tuple or row of variables such as (x^(k)), one for each group transformation, treated as a unit in the symmetric-function theorem.';
        excluded='an infinite numerical series; a sequence ordered by magnitude; a power series; a list of scalar sizes with no variable-row structure';
        alternatives='变量列; 变量序列; 量组'; basin='mixed/contested';
        risk='High: 变量组 is an interpretive Mainland-oriented normalization rather than a close lexical match to historical Größenreihe; 列 and 序列 are competing attractors, and regional history is untested.';
        reason='The notation displays each Reihe as the n-tuple (x_1^(k),...,x_n^(k)) and the theorem permutes these rows.';
        note='The producer form emphasizes grouped variables; whether the historical row/series nuance warrants 变量列 is left open.'
    },
    [ordered]@{
        id='008'; locator='opening paragraph and sections 1--2'; german='symmetrische Funktion'; scope='function symmetric in the h rows of transformed variables'; hans='对称函数'; hant='對稱函數';
        sense='A function unchanged under permutation of the relevant variable rows, within the multisymmetric-function argument.';
        excluded='an even function; a visually symmetric graph; a symmetric relation; a symmetric polynomial in only one unspecified variable set';
        alternatives='对称式; 对称多项式; 对称函数式'; basin='modern Sino-xenic coinage/calque';
        risk='Medium: 对称函数 is Mainland-standard but broad; it can hide the paper''s row-symmetric setting, and no regional terminology was consulted.';
        reason='The argument explicitly invokes the theorem on symmetric functions of Größenreihen and represents invariants through their elementary symmetric functions.';
        note='The producer retains the general term and leaves the multisymmetric specialization to context.'
    },
    [ordered]@{
        id='009'; locator='section 1 and section 2 source note'; german='einförmiger Fall'; scope='special simplest row-symmetric case in which each summand contains only one variable row'; hans='单式情形'; hant='單式情形';
        sense='Noether''s named special case where every summand f(x^(k)) contains just the single row x^(k), not a general uniformity condition.';
        excluded='a uniform case in the modern analytic sense; a one-form in differential geometry; a monomial case; an assertion that all objects have identical shape';
        alternatives='单型情形; 一列型情形; 同型情形'; basin='mixed/contested';
        risk='High: 单式情形 is an inherited interpretive form with weak modern transparency and a strong risk of being read as a formula-type or monomial label; no regional evidence was gathered.';
        reason='The immediately preceding clause defines the case by one Größenreihe per summand, and the later note refers back to the same bounded construction.';
        note='The compact producer form is preserved while its nonstandard opacity is recorded as adverse evidence.'
    },
    [ordered]@{
        id='010'; locator='section 1 and section 2 conclusion'; german='symmetrische Elementarfunktion'; scope='elementary symmetric function of the transformed variable rows or of the auxiliary linear forms'; hans='初等对称函数'; hant='初等對稱函數';
        sense='One of the elementary symmetric functions used to generate symmetric functions in the designated rows or auxiliary variables.';
        excluded='an elementary analytic function; a merely basic symmetric example; an arbitrary symmetric function; an elemental operation in programming';
        alternatives='初等对称式; 基本对称函数; 初等对称多项式'; basin='modern Sino-xenic coinage/calque';
        risk='Medium: 初等对称函数 is Mainland-standard but the 函数/式/多项式 distinction varies by register and region; no localized evidence was consulted.';
        reason='The paper identifies these functions with coefficients of the resolvent and later substitutes them for the first h power sums.';
        note='The producer chooses the broad conventional compound and does not certify regional lexical preference.'
    },
    [ordered]@{
        id='011'; locator='section 1 theorem and section 3'; german='Galoissche Resolvente'; scope='displayed Galois resolvent polynomial Phi(z,u) whose coefficients form a full invariant system'; hans='Galois 预解式'; hant='Galois 預解式';
        sense='The polynomial resolvent built as the product over the group-transformed linear forms, with invariant coefficients G.';
        excluded='the analytic resolvent of an operator; resolution of a singularity; a Galois group; a generic equation-solving procedure';
        alternatives='Galois 预解多项式; 伽罗瓦预解式; Galois 预解方程'; basin='mixed/contested';
        risk='High: the Latin-name-plus-预解式 form reflects Mainland mathematical prose and 预解式 is not self-explanatory; transliterated 伽罗瓦 and regional alternatives were not researched.';
        reason='The paper explicitly names the displayed product Φ(z,u) and then refers to its coefficients as invariants.';
        note='The producer preserves the Latin surname and compact term; expansion to 预解多项式 remains for independent review.'
    },
    [ordered]@{
        id='012'; locator='opening paragraph and theorem statements in sections 1--2'; german='volles Invariantensystem'; scope='complete finite generating system from which every invariant is expressed integrally and rationally'; hans='完整不变量系'; hant='完整不變量系';
        sense='A full generating system of invariants sufficient to express every invariant in the manner stated by the theorem.';
        excluded='a complete enumeration with no generating property; a basis asserted to be independent; a dynamical system whose states are invariant; all invariants as an infinite class';
        alternatives='完全不变量系; 完备不变量系统; 不变量的完整系统'; basin='modern Sino-xenic coinage/calque';
        risk='High: 完整不变量系 is Mainland-oriented compressed terminology and 系 may be read as a family without the stated generating property; 完备/完全 alternatives and regional usage are untested.';
        reason='Both theorem statements define the system by its ability to express every invariant using finitely many listed invariants.';
        note='The producer form follows the target''s compact register; the generating-system sense is fixed only by the recorded window.'
    },
    [ordered]@{
        id='013'; locator='section 2, power-sum construction and conclusion'; german='Potenzsumme'; scope='power-sum symmetric expression S_mu in the h transformed linear forms'; hans='幂和'; hant='冪和';
        sense='The sum of the μ-th powers of the h displayed linear forms, used in Newton-type relations with elementary symmetric functions.';
        excluded='a power series; an exponential sum; a sum exponent in complexity analysis; an arbitrary arithmetic total involving powers';
        alternatives='幂和式; 幂次和; 乘方和'; basin='modern Sino-xenic coinage/calque';
        risk='Medium: 幂和 is Mainland-standard and compact but can be read generically outside symmetric-function theory; regional variants were not consulted.';
        reason='The text explicitly defines S_mu as the μ-th power sum of h linear forms and then relates the first h such sums to elementary symmetric functions.';
        note='The producer retains the standard short compound with its bounded algebraic context recorded.'
    },
    [ordered]@{
        id='014'; locator='section 3 heading sentence and section 4'; german='rationale Darstellung'; scope='expression of rational absolute invariants as rational functions of resolvent coefficients'; hans='有理表示'; hant='有理表示';
        sense='A rational expression or presentation of one invariant in terms of specified invariant generators, not a group representation.';
        excluded='a rational representation of a group on a vector space; a reasonable presentation in ordinary prose; a decimal representation of a rational number; graphic depiction';
        alternatives='有理表达; 有理表出; 有理表示式'; basin='mixed/contested';
        risk='High: 有理表示 strongly attracts the modern representation-theoretic sense in Mainland Chinese, whereas the passage concerns rational expression; regional terminology is untested.';
        reason='The section states that each rational absolute invariant can be written as a quotient and expressed rationally through the resolvent coefficients.';
        note='The inherited producer choice is recorded with the representation-theory collision explicitly exposed for checker review.'
    },
    [ordered]@{
        id='015'; locator='section 4 second source note'; german='relative Invariante'; scope='relative invariant that transforms by a factor and whose class does not form a field'; hans='相对不变量'; hant='相對不變量';
        sense='An invariant of relative type, contrasted with absolute invariants and noted not to form a field as a collection.';
        excluded='an approximately invariant quantity; an invariant relative only to informal context; a relational-database invariant; a normalized absolute invariant';
        alternatives='相对不变式; 协变不变量; 权相对不变量'; basin='modern Sino-xenic coinage/calque';
        risk='High: 相对不变量 is Mainland-standard but underspecifies the transformation factor and competes with 相对不变式; regional usage was not researched.';
        reason='The source note explicitly contrasts these objects with the absolute/rational case and states that they do not form a field.';
        note='No transformation-law expansion is inserted into the lexical form; the note''s technical distinction remains for independent checking.'
    },
    [ordered]@{
        id='016'; locator='section 4, title of the cited 1915 paper'; german='Körper rationaler Funktionen'; scope='field of rational functions named in the cited earlier paper title'; hans='有理函数域'; hant='有理函數域';
        sense='A field whose elements are rational functions, in the algebraic sense of Körper.';
        excluded='a physical body of rational functions; merely the set of rational functions without field operations; a vector space; the polynomial ring';
        alternatives='有理函数体; 有理函数场; 有理函数的域'; basin='modern Sino-xenic coinage/calque';
        risk='High: 域 is Mainland-standard field terminology, while 体 and 場/场 are competing historical or regional attractors; generic Hant conversion is not localization.';
        reason='The phrase occurs as the title of an algebraic paper and Körper has its field-theoretic role there.';
        note='The producer uses 域 consistently and records the body/field regional competition as terminology debt.'
    },
    [ordered]@{
        id='017'; locator='section 1 coefficient description and section 2 final theorem'; german='Grad'; scope='total polynomial degree in the variables x of an invariant coefficient'; hans='次数'; hant='次數';
        sense='The total degree α_1+...+α_n in the x variables, later bounded by the group order h.';
        excluded='an academic degree; an angular degree; a group order; matrix rank; an ordinal stage';
        alternatives='度数; 多项式次数; 阶数'; basin='modern Sino-xenic coinage/calque';
        risk='Medium: 次数 is Mainland-standard but can overlap iteration counts, while 度数 is a regional/historical attractor not investigated here.';
        reason='The displayed formula identifies the degree with the sum of exponents and the concluding theorem compares it numerically with h.';
        note='The producer selects 次数 without expanding to 多项式次数 because the variable context is explicit.'
    },
    [ordered]@{
        id='018'; locator='section 2 second theorem and concluding sentence'; german='Ordnung der Gruppe'; scope='cardinality h of the finite group, used as the upper degree bound'; hans='群的阶'; hant='群的階';
        sense='The number h of elements in the finite group, not the order of a particular group element.';
        excluded='the order of one element; a linear ordering on the group; the sequence in which transformations are listed; an administrative command';
        alternatives='群阶; 群之阶; 群的次序'; basin='modern Sino-xenic coinage/calque';
        risk='Medium: 群的阶 is Mainland-standard and contextually clear, but 阶 can also denote degree or filtration level and regional wording was not researched.';
        reason='The paper defines h as the number of listed transformations and explicitly says h means the group order.';
        note='The producer retains the explicit possessive form rather than shortening it to 群阶.'
    }
)

$terminology = foreach ($term in $terms) {
    [pscustomobject][ordered]@{
        decision_id = "P07-ZH-T$($term.id)"
        source_locator = $term.locator
        exact_german_phrase = $term.german
        concept_scope = $term.scope
        zh_hans_cn_choice = $term.hans
        sense_window = $term.sense
        excluded_senses = $term.excluded
        alternatives_considered = $term.alternatives
        lexical_attractor_basin = $term.basin
        mandarin_simplified_dominance_risk_debt = $term.risk
        evidence_class = $evidenceClass
        controlled_hant_form = $term.hant
        controlled_hant_status = $hantStatus
        independent_check_status = $reviewState
        producer_note = $term.note
    }
}

$adverse = foreach ($term in $terms) {
    [pscustomobject][ordered]@{
        adverse_id = "P07-ZH-A$($term.id)"
        term_decision_id = "P07-ZH-T$($term.id)"
        source_locator = $term.locator
        exact_german_phrase = $term.german
        zh_hans_cn_producer_choice = $term.hans
        trap_or_adverse_reading = $term.excluded
        contextual_reason_for_exclusion = $term.reason
        alternative_held_for_independent_review = $term.alternatives
        lexical_attractor_basin = $term.basin
        mandarin_simplified_dominance_risk_debt = $term.risk
        evidence_class = $evidenceClass
        controlled_hant_status = $hantStatus
        review_state = $reviewState
    }
}

$crosswalk = foreach ($term in $terms) {
    [pscustomobject][ordered]@{
        crosswalk_id = "P07-ZH-X$($term.id)"
        term_decision_id = "P07-ZH-T$($term.id)"
        source_locator = $term.locator
        exact_german_phrase = $term.german
        zh_hans_cn_producer_form = $term.hans
        zh_hant_controlled_form = $term.hant
        zh_hant_status = $hantStatus
        ja_form = ''
        ko_form = ''
        ja_ko_evidence_status = $jaKoStatus
        sense_window = $term.sense
        excluded_senses = $term.excluded
        lexical_attractor_basin = $term.basin
        mandarin_simplified_dominance_risk_debt = $term.risk
        evidence_class = $evidenceClass
        independent_check_status = $reviewState
    }
}

$terminology | Export-Csv -LiteralPath (Join-Path $evidenceDir 'TERMINOLOGY_LEDGER.csv') -NoTypeInformation -Encoding utf8
$adverse | Export-Csv -LiteralPath (Join-Path $evidenceDir 'ADVERSE_EVIDENCE_LEDGER.csv') -NoTypeInformation -Encoding utf8
$crosswalk | Export-Csv -LiteralPath (Join-Path $evidenceDir 'CJKV_CROSSWALK.csv') -NoTypeInformation -Encoding utf8

$nodes = [System.Collections.Generic.List[object]]::new()
$edges = [System.Collections.Generic.List[object]]::new()
foreach ($term in $terms) {
    $n = $term.id
    $nodes.Add([ordered]@{ id="P07-LOC-$n"; type='source_locus'; locator=$term.locator; exact_german_phrase=$term.german })
    $nodes.Add([ordered]@{ id="P07-CON-$n"; type='concept'; scope=$term.scope; sense_window=$term.sense; excluded_senses=$term.excluded })
    $nodes.Add([ordered]@{ id="P07-HANS-$n"; type='form'; language_scope='zh-Hans-CN producer'; form=$term.hans })
    $nodes.Add([ordered]@{ id="P07-HANT-$n"; type='form'; language_scope='zh-Hant-controlled nonregional producer record'; form=$term.hant; status=$hantStatus })
    $nodes.Add([ordered]@{ id="P07-CHOICE-$n"; type='producer_choice'; decision_id="P07-ZH-T$n"; dominance_risk_debt=$term.risk; evidence_class=$evidenceClass; review_state=$reviewState })

    $edges.Add([ordered]@{ id="P07-E$n-1"; type='occurs_at'; from="P07-CON-$n"; to="P07-LOC-$n" })
    $edges.Add([ordered]@{ id="P07-E$n-2"; type='decides_for'; from="P07-CHOICE-$n"; to="P07-CON-$n" })
    $edges.Add([ordered]@{ id="P07-E$n-3"; type='selects_hans_form'; from="P07-CHOICE-$n"; to="P07-HANS-$n" })
    $edges.Add([ordered]@{ id="P07-E$n-4"; type='records_controlled_hant_form'; from="P07-CHOICE-$n"; to="P07-HANT-$n" })
    $edges.Add([ordered]@{ id="P07-E$n-5"; type='controlled_form_of'; from="P07-HANT-$n"; to="P07-HANS-$n" })
}

$graph = [ordered]@{
    graph_id = 'NOE-P07-ZH-PRODUCER-CONCEPT-GRAPH-001'
    work_unit = 'Noether Paper 7 Chinese producer translation'
    graph_status = [ordered]@{
        purpose = 'producer-side translation-decision evidence only'
        decision_count = 18
        independent_check = 'absent'
        external_native_source_research = 'not performed'
        japanese_or_korean_evidence = 'not consulted or used'
        scan_inspection = 'not performed'
        source_branch_comparison = 'not performed'
        compilation_or_rendering = 'mechanical build records exist outside this evidence-packaging subtask; rendered pages not inspected'
        controlled_hant_scope = $hantStatus
        translation_validation_or_readiness_claim = 'none'
    }
    provenance = [ordered]@{
        german_snapshot = [ordered]@{
            path = 'source/Noether_Paper07_German_current_exact_CRLF.tex'
            sha256 = $sourceHash
            use = 'translation source wording and locator only; no source/apparatus check'
        }
        inherited_hans_witness = [ordered]@{
            path = 'witness/Noether_Paper07_SimplifiedChinese_inherited_exact_CRLF.tex'
            sha256 = $witnessHash
            use = 'drafting witness only; not authority'
        }
        hans_target = [ordered]@{
            path = 'zh-Hans-CN/Noether_Paper07_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex'
            sha256 = $hansHash
            use = 'producer choice record; independent check absent'
        }
        controlled_hant_target = [ordered]@{
            path = 'zh-Hant-controlled/Noether_Paper07_Chinese_CurrentAuthority_zh-Hant-controlled_v001.tex'
            sha256 = $hantHash
            use = $hantStatus
        }
        evidence_class = $evidenceClass
    }
    node_type_definitions = [ordered]@{
        source_locus = 'Locator and phrase in the supplied German fragment; not a source-validation assertion.'
        concept = "Producer's bounded sense window and excluded lexical attractors."
        form = 'Proposed Chinese form with explicit Hans or nonregional controlled-Hant scope.'
        producer_choice = 'Editorial selection with qualitative Mandarin-Simplified dominance debt and open review state; lexical-attractor basin is recorded only in the CSV ledgers.'
    }
    edge_type_definitions = [ordered]@{
        occurs_at = 'Concept to supplied-source locator.'
        decides_for = 'Producer choice to concept.'
        selects_hans_form = 'Producer choice to Hans form.'
        records_controlled_hant_form = 'Producer choice to nonregional controlled-Hant form.'
        controlled_form_of = 'Controlled-Hant script form to Hans lexical base without Taiwan/Hong Kong/Macao equivalence claim.'
    }
    nodes = $nodes
    edges = $edges
}

$graph | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath (Join-Path $evidenceDir 'CONCEPT_EVIDENCE_GRAPH.json') -Encoding utf8
