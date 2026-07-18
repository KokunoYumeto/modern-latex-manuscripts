from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "00_Interlanguage_Methodology_Current_v12_20260718.pdf"

INK = colors.HexColor("#17212B")
TEAL = colors.HexColor("#087F8C")
GREEN = colors.HexColor("#2D6A4F")
RUST = colors.HexColor("#A33B20")
GOLD = colors.HexColor("#B7791F")
PALE = colors.HexColor("#F3F5F6")
RULE = colors.HexColor("#CBD2D9")
WHITE = colors.white


class NumberedDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str) -> None:
        super().__init__(
            filename,
            pagesize=A4,
            leftMargin=20 * mm,
            rightMargin=20 * mm,
            topMargin=19 * mm,
            bottomMargin=18 * mm,
            title="Interlanguage and Mathematical Translation Methodology",
            author="Manuscript Typesetting Project",
            subject="Language-manager fleet snapshot and public archive map",
        )
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="normal",
        )
        self.addPageTemplates(
            PageTemplate(id="main", frames=[frame], onPage=self.draw_page)
        )

    def draw_page(self, canvas, doc) -> None:
        canvas.saveState()
        canvas.setStrokeColor(RULE)
        canvas.setLineWidth(0.5)
        canvas.line(
            doc.leftMargin,
            13 * mm,
            A4[0] - doc.rightMargin,
            13 * mm,
        )
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#53606D"))
        canvas.drawString(
            doc.leftMargin,
            8.5 * mm,
            "Interlanguage methodology sidecar - v0.12 - 18 July 2026",
        )
        canvas.drawRightString(
            A4[0] - doc.rightMargin,
            8.5 * mm,
            f"Page {doc.page}",
        )
        canvas.restoreState()


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="CoverTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=26,
        leading=30,
        textColor=INK,
        alignment=TA_LEFT,
        spaceAfter=8 * mm,
    )
)
styles.add(
    ParagraphStyle(
        name="Subtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=12,
        leading=17,
        textColor=TEAL,
        spaceAfter=6 * mm,
    )
)
styles.add(
    ParagraphStyle(
        name="H1x",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=22,
        textColor=INK,
        spaceBefore=3 * mm,
        spaceAfter=4 * mm,
    )
)
styles.add(
    ParagraphStyle(
        name="H2x",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=15,
        textColor=TEAL,
        spaceBefore=3 * mm,
        spaceAfter=2 * mm,
    )
)
styles.add(
    ParagraphStyle(
        name="Bodyx",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9.2,
        leading=13.2,
        textColor=INK,
        spaceAfter=2.5 * mm,
    )
)
styles.add(
    ParagraphStyle(
        name="Smallx",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=7.8,
        leading=10.2,
        textColor=INK,
    )
)
styles.add(
    ParagraphStyle(
        name="SmallBold",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=7.8,
        leading=10.2,
        textColor=INK,
    )
)
styles.add(
    ParagraphStyle(
        name="SmallHeader",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=7.8,
        leading=10.2,
        textColor=WHITE,
    )
)
styles.add(
    ParagraphStyle(
        name="Linkx",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=8.6,
        leading=11.6,
        textColor=TEAL,
        spaceAfter=1.5 * mm,
    )
)
styles.add(
    ParagraphStyle(
        name="Status",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=9,
        leading=12,
        textColor=RUST,
        alignment=TA_CENTER,
    )
)


def para(text: str, style: str = "Bodyx") -> Paragraph:
    return Paragraph(text, styles[style])


def callout(text: str, color=TEAL) -> Table:
    table = Table([[para(text, "Bodyx")]], colWidths=[164 * mm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PALE),
                ("BOX", (0, 0), (-1, -1), 0.8, color),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    return table


def payload_table() -> Table:
    rows = [
        [
            para("Public record", "SmallHeader"),
            para("What a reader gets", "SmallHeader"),
            para("Current boundary", "SmallHeader"),
        ],
        [
            para("<b>Noether</b><br/>10.5281/zenodo.21423112", "Smallx"),
            para(
                "German R823 source control; English working reader; "
                "source-reconciled Spanish and French readers; paired-script "
                "Interslavic readers; bounded CJK, RTL, and Indonesian units.",
                "Smallx",
            ),
            para(
                "Working corpus. Not a critical edition or universal "
                "mathematical certification.",
                "Smallx",
            ),
        ],
        [
            para("<b>SGA 5 and SGA 6</b><br/>10.5281/zenodo.21422245", "Smallx"),
            para(
                "French workpasses; 309-page SGA 5 English working "
                "translation; corrected 381-page layered SGA 6 English "
                "reader; bounded SGA 6 Spanish tranche.",
                "Smallx",
            ),
            para(
                "Authority layers and known weaknesses are retained. "
                "Not critical editions.",
                "Smallx",
            ),
        ],
        [
            para("<b>Interlanguage</b><br/>10.5281/zenodo.21124403", "Smallx"),
            para(
                "Source-body baselines, automata and term ledgers, research "
                "handoffs, normalization evidence, release gates, and this "
                "manager snapshot.",
                "Smallx",
            ),
            para(
                "Methodology and evidence sidecar; actual full readers live "
                "on author or series records.",
                "Smallx",
            ),
        ],
    ]
    table = Table(rows, colWidths=[39 * mm, 79 * mm, 46 * mm], repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), INK),
                ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
                ("GRID", (0, 0), (-1, -1), 0.35, RULE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, PALE]),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    return table


LANES = [
    (
        "English / Germanic",
        "SGA 5 English and layered full-range SGA 6 English are public. "
        "Noether English remains an inherited working reader requiring "
        "continued checking.",
        "Public working editions with source, build, and audit evidence. "
        "Inherited or OCR-derived layers remain identified.",
        GREEN,
    ),
    (
        "Romance",
        "Noether Spanish and French R823 readers are public. SGA 6 Spanish "
        "has one bounded tranche. SGA 5 Spanish is active and partial.",
        "Source-reconciled working readers, not native-language "
        "certification. The moving SGA 5 workpass is not sealed here.",
        TEAL,
    ),
    (
        "Slavic / Interslavic",
        "Noether Interslavic has 221 Latin-script and 221 Cyrillic-script "
        "units. A bounded Paper 6 Slavic tranche also exists.",
        "Reproducible normalized working corpus; no community or "
        "native-speaker certification.",
        GOLD,
    ),
    (
        "CJK",
        "Full inherited Simplified Chinese and Japanese readers exist. "
        "Current R823 Papers 26 and 36 exist in Chinese, Japanese, and Korean.",
        "Real cumulative readers plus bounded R823 units. Full readers are "
        "not certified as wholly synchronized to R823; Korean is bounded.",
        RUST,
    ),
    (
        "Arabic / Persianate / RTL",
        "Current Noether Paper 6 opening units exist in Arabic and Iranian "
        "Persian, with TeX, PDFs, decision records, and bidi checks.",
        "Compiled bounded working translations. External and native review "
        "remain open.",
        TEAL,
    ),
    (
        "Turkic",
        "A substantial source and evidence corpus is indexed. Three one-page "
        "Hefferon review drafts build in Kyrgyz, Uyghur, and Uzbek.",
        "Manager consolidation plus explicitly unreviewed buildable drafts. "
        "The publication-candidate folder remains empty.",
        GOLD,
    ),
    (
        "Africa / Horn / West",
        "A 113-word OpenStax excerpt has separate Somali and Oromo TeX/PDF "
        "microtranches, source notes, terminology records, and QA.",
        "Technically complete microtranches; unreviewed and not a readiness "
        "claim.",
        GREEN,
    ),
    (
        "Malay / SEA / Pacific",
        "Noether Paper 36 has a complete current Indonesian working "
        "translation with source and terminology evidence.",
        "One-page source-reconciled working translation; no native review "
        "and no Malay continuation yet.",
        RUST,
    ),
]


def lane_table(items) -> Table:
    rows = [
        [
            para("Lane", "SmallHeader"),
            para("Substantive state", "SmallHeader"),
            para("Classification", "SmallHeader"),
        ]
    ]
    colors_for_rows = []
    for name, state, boundary, color in items:
        rows.append(
            [
                para(f"<b>{name}</b>", "Smallx"),
                para(state, "Smallx"),
                para(boundary, "Smallx"),
            ]
        )
        colors_for_rows.append(color)
    table = Table(rows, colWidths=[35 * mm, 68 * mm, 61 * mm], repeatRows=1)
    commands = [
        ("BACKGROUND", (0, 0), (-1, 0), INK),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("GRID", (0, 0), (-1, -1), 0.35, RULE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]
    for index, color in enumerate(colors_for_rows, start=1):
        commands.extend(
            [
                ("LINEBEFORE", (0, index), (0, index), 3, color),
                (
                    "BACKGROUND",
                    (0, index),
                    (-1, index),
                    WHITE if index % 2 else PALE,
                ),
            ]
        )
    table.setStyle(TableStyle(commands))
    return table


def build_story():
    story = [
        Spacer(1, 17 * mm),
        para("INTERLANGUAGE PROGRAMME", "Subtitle"),
        para("Language-manager fleet and public archive map", "CoverTitle"),
        para(
            "Methodology sidecar v0.12 | frozen snapshot of eight active "
            "language lanes | 18 July 2026",
            "Subtitle",
        ),
        Spacer(1, 3 * mm),
        callout(
            "<b>Reader warning.</b> This is a map of genuine working outputs "
            "and their evidence levels. A complete microtranche is not a "
            "complete language edition; a successful build is not native "
            "review; and a source-reconciled reader is not a critical edition.",
            RUST,
        ),
        Spacer(1, 8 * mm),
        para("Three public homes", "H1x"),
        para(
            "<b>Noether:</b> 10.5281/zenodo.21423112<br/>"
            "<b>SGA 5 and SGA 6:</b> 10.5281/zenodo.21422245<br/>"
            "<b>Interlanguage methodology:</b> 10.5281/zenodo.21124403<br/>"
            "<b>GitHub:</b> github.com/KokunoYumeto/modern-latex-manuscripts",
            "Linkx",
        ),
        Spacer(1, 7 * mm),
        para(
            "The public archive is designed so that a machine failure on the "
            "working PC does not erase the meaningful work. Full readers, "
            "editable packages, evidence ledgers, and conservative status "
            "notes are pushed to Zenodo and mirrored on GitHub when they form "
            "a reproducible checkpoint.",
            "Bodyx",
        ),
        PageBreak(),
        para("Public payloads", "H1x"),
        para(
            "The author and seminar records carry reader-facing texts. This "
            "sidecar carries cross-language methodology, provenance, manager "
            "state, and the small bounded experiments that do not belong on "
            "a single author record.",
            "Bodyx",
        ),
        payload_table(),
        Spacer(1, 6 * mm),
        callout(
            "<b>Large bodies are not duplicated in v0.12.</b> Earlier numbered "
            "Interlanguage ZIPs already preserve the multi-gigabyte source "
            "corpora. The new package adds the current map and manager layer.",
            TEAL,
        ),
        Spacer(1, 6 * mm),
        para("Classification vocabulary", "H2x"),
        para(
            "<b>Source-reconciled working reader</b> means the declared source "
            "units and artifact bindings pass the recorded checks. "
            "<b>Bounded working translation</b> means only the named unit is "
            "covered. <b>Review draft</b> means the text builds but language "
            "or domain review remains open. <b>Control infrastructure</b> "
            "means ledgers, source maps, or workflow evidence rather than a "
            "translation body.",
            "Bodyx",
        ),
        PageBreak(),
        para("Fleet state: established lanes", "H1x"),
        para(
            "These lanes already have substantial reader bodies or completed "
            "bounded units in the public archive. Their unresolved gates are "
            "shown alongside the substantive work.",
            "Bodyx",
        ),
        lane_table(LANES[:4]),
        PageBreak(),
        para("Fleet state: developing lanes", "H1x"),
        para(
            "These lanes are earlier in production. The manager snapshot "
            "preserves useful work without promoting it beyond its actual "
            "review state.",
            "Bodyx",
        ),
        lane_table(LANES[4:]),
        Spacer(1, 7 * mm),
        callout(
            "<b>Moving work excluded from the sealed snapshot:</b> the SGA 5 "
            "Spanish workpass and SGA 6 French audit workpass were actively "
            "changing at capture time. They remain live production lanes and "
            "will be published at their next stable, reproducible checkpoint.",
            GOLD,
        ),
        PageBreak(),
        para("Inside the v0.12 manager ZIP", "H1x"),
        para(
            "The compact ZIP has one root, a complete file manifest, SHA-256 "
            "checksums, and four small classes of actual working output:",
            "Bodyx",
        ),
        para(
            "<b>1. Somali and Oromo:</b> separate OpenStax prealgebra "
            "microtranches with translated TeX, one-page PDFs, source note, "
            "terminology/adverse ledger, build results, extraction check, and "
            "visual QA.",
            "Bodyx",
        ),
        para(
            "<b>2. Arabic and Iranian Persian:</b> the current Noether Paper 6 "
            "opening tranche with exact segment scope, TeX, one-page PDFs, "
            "typed decisions, bidi invariants, source-use record, terminology "
            "note, and render evidence.",
            "Bodyx",
        ),
        para(
            "<b>3. Indonesian:</b> complete Noether Paper 36 TeX plus the exact "
            "R823 source block, segment map, terminology/adverse ledger, build "
            "results, and render check.",
            "Bodyx",
        ),
        para(
            "<b>4. Kyrgyz, Uyghur, and Uzbek:</b> Hefferon vector-operations "
            "review drafts with two-pass XeLaTeX builds, one-page PDFs, text "
            "extraction, render QA, and explicit open review gates.",
            "Bodyx",
        ),
        Spacer(1, 5 * mm),
        para("Manager controls", "H2x"),
        para(
            "The ZIP also freezes the stable control directories for all eight "
            "lanes: work registries, source floors, evidence graphs, cohort "
            "trees, terminology and adverse ledgers, drift audits, build "
            "handoffs, release ledgers, continuation cursors, and public-state "
            "baselines. These files are operational evidence, not replacement "
            "translation bodies.",
            "Bodyx",
        ),
        Spacer(1, 5 * mm),
        callout(
            "<b>Correction route:</b> GitHub issues and pull requests are the "
            "preferred way to propose better scans, corrected TeX, terminology "
            "evidence, or status corrections.",
            GREEN,
        ),
        PageBreak(),
        para("Evidence boundary", "H1x"),
        para(
            "Every status word in this archive is scoped. A complete Paper 36 "
            "translation is complete for that paper, not for an author corpus. "
            "A full-range layered SGA reader covers the range, but individual "
            "layers can still carry inherited transcription or compression "
            "risk. A 35-check release gate binds the checks it declares; it "
            "does not prove semantic perfection.",
            "Bodyx",
        ),
        para(
            "OCR and VLM outputs are source witnesses, locators, and omission "
            "detectors unless a later source audit promotes their content. "
            "Rendered PDFs prove that TeX builds and pages can be inspected; "
            "they do not prove that every symbol matches the scan.",
            "Bodyx",
        ),
        para(
            "No file in this v0.12 release is claimed as peer reviewed, "
            "universally mathematically correct, or critically complete. "
            "Native-language and domain review remain visible open gates where "
            "they have not occurred.",
            "Bodyx",
        ),
        Spacer(1, 5 * mm),
        callout(
            "<b>Archive policy:</b> meaningful reproducible checkpoints are "
            "published, not left indefinitely in a private staging folder. "
            "Actively changing work is withheld only until its files, scope, "
            "and evidence can be frozen coherently.",
            INK,
        ),
        Spacer(1, 8 * mm),
        para("Persistent identifiers", "H2x"),
        para(
            "Interlanguage concept DOI: 10.5281/zenodo.21124403<br/>"
            "Noether concept DOI: 10.5281/zenodo.20412587<br/>"
            "SGA concept DOI: 10.5281/zenodo.20410947<br/>"
            "Workflow concept DOI: 10.5281/zenodo.20461174",
            "Linkx",
        ),
    ]
    return story


def main() -> None:
    document = NumberedDocTemplate(str(OUTPUT))
    document.build(build_story())
    print(OUTPUT)


if __name__ == "__main__":
    main()
