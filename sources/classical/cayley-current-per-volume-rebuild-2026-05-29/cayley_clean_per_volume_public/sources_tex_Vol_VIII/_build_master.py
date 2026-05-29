"""Build the merged Vol VIII PDF from completed chunks, with gap placeholders."""
import subprocess
from pathlib import Path
from pypdf import PdfWriter, PdfReader

DIR = Path(r"local workspace\Documents\local repair pass PLEASE DONT DELETE WINDOWS 32\local repair pass_OUTPUTS\cayley_clean_per_volume\sources_tex_Vol_VIII")
OUT_PDF = Path(r"local workspace\Documents\local repair pass PLEASE DONT DELETE WINDOWS 32\local repair pass_OUTPUTS\cayley_clean_per_volume\Cayley_Collected_Mathematical_Papers_Vol_VIII_partial.pdf")
PDFLATEX = r"local workspace\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe"

# Ordered list of chunks (start_page, end_page, file_or_None)
chunks = [
    (1, 16, "cayley_vol08_pages_001_016.pdf"),
    (17, 66, "cayley_vol08_pages_017_066.pdf"),  # NOTE: undersized, only 6 pp of ~50
    (67, 116, "cayley_vol08_pages_067_116.pdf"),
    (117, 166, "cayley_vol08_pages_117_166.pdf"),
    (167, 216, "cayley_vol08_pages_167_216.pdf"),
    (217, 241, None),  # gap
    (242, 266, "cayley_vol08_pages_242_266.pdf"),
    (267, 291, "cayley_vol08_pages_267_291.pdf"),
    (292, 316, None),  # gap
    (317, 366, "cayley_vol08_pages_317_366.pdf"),
    (367, 416, "cayley_vol08_pages_367_416.pdf"),
    (417, 441, "cayley_vol08_pages_417_441.pdf"),
    (442, 466, "cayley_vol08_pages_442_466.pdf"),
    (467, 516, "cayley_vol08_pages_467_516.pdf"),
    (517, 566, None),  # gap
    (567, 570, "cayley_vol08_pages_567_570.pdf"),
]

# Build gap-marker PDF (one-page placeholder per gap)
gap_tex_template = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{geometry}
\geometry{paperwidth=6.5in,paperheight=9.5in,margin=1in}
\thispagestyle{empty}
\begin{document}
\vspace*{2in}
\begin{center}
{\large\bfseries Cayley, Collected Mathematical Papers, Vol.~VIII}\\[1em]
{\large Book pages __START__--__END__}\\[2em]
\textit{Modern LaTeX typesetting pending.}\\[1em]
The direct scan-based typesetting pass did not complete this range
during the current batch (automated-pass blocks during agent runs).
Refer to the source-scan PDF for these pages.
\end{center}
\end{document}
"""

writer = PdfWriter()
notes = []
for start, end, fname in chunks:
    if fname:
        path = DIR / fname
        if not path.exists():
            notes.append(f"MISSING FILE for pp {start}-{end}: {fname}")
            continue
        reader = PdfReader(str(path))
        for page in reader.pages:
            writer.add_page(page)
        writer.add_outline_item(f"Book pp {start}-{end}", len(writer.pages) - len(reader.pages))
        notes.append(f"Added pp {start}-{end}: {len(reader.pages)} PDF pages from {fname}")
    else:
        # Build a placeholder one-pager
        gap_dir = DIR / "_gap_placeholders"
        gap_dir.mkdir(exist_ok=True)
        gap_tex = gap_dir / f"gap_{start:03d}_{end:03d}.tex"
        gap_pdf = gap_tex.with_suffix(".pdf")
        if not gap_pdf.exists():
            tex_src = gap_tex_template.replace("__START__", str(start)).replace("__END__", str(end))
            gap_tex.write_text(tex_src, encoding="utf-8")
            subprocess.run([PDFLATEX, "-interaction=nonstopmode", "-output-directory",
                          str(gap_dir), str(gap_tex)], capture_output=True, timeout=60)
        if gap_pdf.exists():
            r = PdfReader(str(gap_pdf))
            for page in r.pages:
                writer.add_page(page)
            writer.add_outline_item(f"GAP: pp {start}-{end}", len(writer.pages) - 1)
            notes.append(f"GAP PLACEHOLDER for pp {start}-{end}")
        else:
            notes.append(f"FAILED to build placeholder for pp {start}-{end}")

with open(OUT_PDF, "wb") as f:
    writer.write(f)

print(f"Wrote {OUT_PDF.name}: {len(writer.pages)} pages")
print()
for n in notes:
    print(f"  {n}")
