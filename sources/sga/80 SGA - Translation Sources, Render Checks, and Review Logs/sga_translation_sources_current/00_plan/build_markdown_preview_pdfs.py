from pathlib import Path
import unicodedata, re, sys, os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch

FONT_REG = False
BODY = 'DejaVuSans'
BOLD = 'DejaVuSans-Bold'
MONO = 'DejaVuSansMono'

def register_fonts():
    global FONT_REG
    if FONT_REG:
        return
    pdfmetrics.registerFont(TTFont(BODY, '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
    pdfmetrics.registerFont(TTFont(BOLD, '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
    pdfmetrics.registerFont(TTFont(MONO, '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'))
    FONT_REG = True

_slug_re = re.compile(r'[^A-Za-z0-9_. -]+')

def normalize_text(s):
    s = unicodedata.normalize('NFKC', s.rstrip('\n'))
    # avoid characters unsupported or visually confusing in text preview
    trans = {
        '\u2212':'-', '\u2010':'-', '\u2011':'-', '\u2012':'-', '\u2013':'-', '\u2014':'--', '\u2015':'--',
        '\u2018':"'", '\u2019':"'", '\u201c':'"', '\u201d':'"', '\u00a0':' ', '\u2009':' ', '\u202f':' ',
        '\u21d2':'=>', '\u21d0':'<=', '\u2192':'->', '\u2190':'<-', '\u21a6':'|->', '\u2205':'empty',
    }
    return ''.join(trans.get(ch, ch) for ch in s)

def split_long_word(word, font, size, max_width):
    chunks=[]; cur=''
    for ch in word:
        if pdfmetrics.stringWidth(cur+ch, font, size) <= max_width or not cur:
            cur += ch
        else:
            chunks.append(cur); cur=ch
    if cur: chunks.append(cur)
    return chunks

def wrap_text(text, font, size, max_width):
    if text == '':
        return ['']
    # keep indentation but avoid very long leading spaces
    leading = len(text) - len(text.lstrip(' '))
    prefix = ' ' * min(leading, 8)
    words = text.strip().split()
    if not words:
        return ['']
    lines=[]; cur=prefix
    for w in words:
        candidate = (cur + (' ' if cur.strip() else '') + w) if cur.strip() else prefix + w
        if pdfmetrics.stringWidth(candidate, font, size) <= max_width:
            cur = candidate
        else:
            if cur.strip():
                lines.append(cur)
            if pdfmetrics.stringWidth(prefix+w, font, size) <= max_width:
                cur = prefix + w
            else:
                chunks = split_long_word(w, font, size, max_width - pdfmetrics.stringWidth(prefix, font, size))
                for ch in chunks[:-1]:
                    lines.append(prefix+ch)
                cur = prefix + chunks[-1]
    if cur.strip():
        lines.append(cur)
    return lines

def draw_page_header(c, title, page_no, width, height, margin):
    c.setFont(BODY, 7.5)
    c.drawString(margin, height - margin + 8, title[:90])
    c.drawRightString(width - margin, margin/2, str(page_no))

def md_to_pdf(md_path, pdf_path, title):
    register_fonts()
    width, height = letter
    margin = 0.65 * inch
    c = canvas.Canvas(str(pdf_path), pagesize=letter)
    c.setTitle(title)
    page_no = 1
    y = height - margin
    max_width = width - 2*margin
    # First page carries its own large title; subsequent pages get a running header.

    def new_page():
        nonlocal page_no, y
        c.showPage()
        page_no += 1
        y = height - margin
        draw_page_header(c, title, page_no, width, height, margin)

    def ensure(space):
        nonlocal y
        if y - space < margin:
            new_page()

    def draw_wrapped(text, font=BODY, size=9, leading=11, gap_after=0, indent=0):
        nonlocal y
        text = normalize_text(text)
        lines = wrap_text(text, font, size, max_width-indent)
        ensure(max(leading*len(lines), leading))
        c.setFont(font, size)
        for line in lines:
            if y < margin + leading:
                new_page(); c.setFont(font, size)
            c.drawString(margin+indent, y, line)
            y -= leading
        y -= gap_after

    c.setFont(BOLD, 16)
    c.drawCentredString(width/2, y, title)
    y -= 22
    c.setFont(BODY, 9)
    note = 'Preview PDF generated from the existing Markdown translation snapshot. Mathematical formulae are rendered as source text where they were not already plain text; authoritative editable source is the accompanying Markdown/LaTeX file.'
    for line in wrap_text(note, BODY, 9, max_width):
        c.drawString(margin, y, line); y -= 11
    y -= 12

    in_code = False
    for raw in Path(md_path).read_text(encoding='utf-8', errors='replace').splitlines():
        line = normalize_text(raw)
        if line.strip().startswith('```'):
            in_code = not in_code
            draw_wrapped(line, MONO, 7.8, 9.5, 1)
            continue
        if in_code:
            draw_wrapped(line, MONO, 7.4, 9.0, 0)
            continue
        stripped=line.strip()
        if not stripped:
            y -= 5
            if y < margin: new_page()
            continue
        if stripped.startswith('#'):
            level = len(stripped) - len(stripped.lstrip('#'))
            text = stripped[level:].strip()
            size = {1:14,2:12.5,3:11,4:10}.get(level,9.5)
            font = BOLD if level <= 3 else BODY
            ensure(size+18)
            y -= 5 if level<=2 else 2
            draw_wrapped(text, font, size, size+2, 5)
            continue
        if stripped.startswith('|') or stripped.startswith('$$') or stripped.startswith('\\[') or stripped.startswith('\\]') or stripped.startswith('\\begin') or stripped.startswith('\\end'):
            draw_wrapped(line, MONO, 7.4, 9.0, 1)
        else:
            draw_wrapped(line, BODY, 8.7, 10.8, 2)
    c.save()
    return page_no

if __name__ == '__main__':
    out_dir = Path(sys.argv[1]); out_dir.mkdir(parents=True, exist_ok=True)
    inputs = [
        ('SGA1_existing_english_from_jcreinhold.md', 'SGA 1 - Existing English translation snapshot'),
        ('SGA2_existing_english_from_jcreinhold.md', 'SGA 2 - Existing English translation snapshot'),
        ('SGA3_existing_english_from_jcreinhold.md', 'SGA 3 - Existing English translation snapshot'),
    ]
    src = Path('/mnt/data/sga_batch003_package/01_existing_translations_latex')
    for fn, title in inputs:
        pages = md_to_pdf(src/fn, out_dir/(fn.replace('.md','_preview.pdf')), title)
        print(f'{fn}: {pages} pages')
