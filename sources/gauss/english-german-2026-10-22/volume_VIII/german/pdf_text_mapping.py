"""Repair CMEX character mappings without changing page graphics.

Derived from the original-language Gauss Volume VII PDF mapping by
OpenAI GPT-6 Astra, with delimiter extensions and existing-map repair
by OpenAI GPT-6.1 Sol.

Usage: python pdf_text_mapping.py input.pdf output.pdf
Requires PyMuPDF and fontTools. The output must be a new file.
"""
from pathlib import Path
import io
import re
import sys
import fitz
from fontTools.cffLib import CFFFontSet
from fontTools import agl


# Unicode character assignments for the vertical delimiter pieces.
EXTENSIBLE_DELIMITERS = {
    'parenlefttp': 0x239B,
    'parenleftex': 0x239C,
    'parenleftbt': 0x239D,
    'parenrighttp': 0x239E,
    'parenrightex': 0x239F,
    'parenrightbt': 0x23A0,
    'bracketlefttp': 0x23A1,
    'bracketleftex': 0x23A2,
    'bracketleftbt': 0x23A3,
    'bracketrighttp': 0x23A4,
    'bracketrightex': 0x23A5,
    'bracketrightbt': 0x23A6,
    'bracelefttp': 0x23A7,
    'braceleftmid': 0x23A8,
    'braceleftbt': 0x23A9,
    'braceex': 0x23AA,
    'bracerighttp': 0x23AB,
    'bracerightmid': 0x23AC,
    'bracerightbt': 0x23AD,
}


def cmex_unicode(name):
    if name in EXTENSIBLE_DELIMITERS:
        return EXTENSIBLE_DELIMITERS[name]
    if name == 'vextendsingle':
        return 0x23D0
    if name == 'vextenddouble':
        return 0x2016
    if name in ('tildewide', 'tildewider', 'tildewidest'):
        return 0x0303
    # Complete delimiters map to their characters. Horizontal brace tips
    # retain separate values because Unicode has no matching components.
    if name in ('integraltext', 'integraldisplay'):
        return 0x222B
    if name in ('summationtext', 'summationdisplay'):
        return 0x2211
    for stem, value in [('parenleft', 0x28), ('parenright', 0x29),
                        ('bracketleft', 0x5B), ('bracketright', 0x5D),
                        ('braceleft', 0x7B), ('braceright', 0x7D)]:
        if name.startswith(stem) and name[len(stem):] in ('big', 'Big', 'bigg', 'Bigg'):
            return value
    known = agl.LEGACY_AGL2UV.get(name)
    if known and len(known) == 1:
        return known[0]
    pieces = ['bracehtipdownleft', 'bracehtipdownright',
              'bracehtipupleft', 'bracehtipupright']
    if name in pieces:
        return 0xE000 + pieces.index(name)
    raise ValueError('Unmapped CMEX10 glyph: ' + name)


def main(source, output):
    source, output = Path(source), Path(output)
    if output.exists() or source.resolve() == output.resolve():
        raise ValueError('The output must be a new file.')
    doc = fitz.open(source)
    fonts = {f[0]: f for page in doc for f in page.get_fonts(full=True)}
    changed = 0
    for xref, font in fonts.items():
        if not re.fullmatch(r'CMEX[0-9]+', font[3].split('+')[-1]):
            continue
        kind, previous = doc.xref_get_key(xref, 'ToUnicode')
        _, extension, _, data = doc.extract_font(xref)
        if extension != 'cff':
            raise ValueError('Expected embedded CMEX CFF font.')
        cff = CFFFontSet()
        cff.decompile(io.BytesIO(data), None)
        encoding = cff[cff.fontNames[0]].Encoding
        if not isinstance(encoding, list) or len(encoding) != 256:
            raise ValueError('Expected an explicit single-byte CFF encoding.')
        if kind == 'xref':
            original_cmap = doc.xref_stream(int(previous.split()[0]))
            cmap = original_cmap
            for code, name in enumerate(encoding):
                old_values = agl.LEGACY_AGL2UV.get(name)
                if name not in EXTENSIBLE_DELIMITERS or not old_values or len(old_values) != 1:
                    continue
                old_value = old_values[0]
                if not 0xE000 <= old_value <= 0xF8FF:
                    continue
                old_pair = f'<{code:02X}> <{old_value:04X}>'.encode('ascii')
                new_pair = f'<{code:02X}> <{cmex_unicode(name):04X}>'.encode('ascii')
                cmap = cmap.replace(old_pair, new_pair)
            if cmap == original_cmap:
                continue
            mapped = doc.get_new_xref()
            doc.update_object(mapped, '<<>>')
            doc.update_stream(mapped, cmap)
            doc.xref_set_key(xref, 'ToUnicode', f'{mapped} 0 R')
            changed += 1
            continue
        pairs = [(code, cmex_unicode(name)) for code, name in enumerate(encoding)
                 if name != '.notdef']
        mapname = re.sub('[^A-Za-z0-9]', '', font[3]) + 'UTF16'
        cmap = ('/CIDInit /ProcSet findresource begin\n12 dict begin\nbegincmap\n'
                f'/CMapName /{mapname} def\n/CMapType 2 def\n'
                '/CIDSystemInfo << /Registry (Adobe) /Ordering (UCS) /Supplement 0 >> def\n'
                '1 begincodespacerange\n<00> <FF>\nendcodespacerange\n'
                f'{len(pairs)} beginbfchar\n' +
                '\n'.join(f'<{a:02X}> <{b:04X}>' for a, b in pairs) +
                '\nendbfchar\nendcmap\nCMapName currentdict /CMap defineresource pop\nend\nend\n')
        newxref = doc.get_new_xref()
        doc.update_object(newxref, '<<>>')
        doc.update_stream(newxref, cmap.encode('ascii'))
        doc.xref_set_key(xref, 'ToUnicode', f'{newxref} 0 R')
        changed += 1
    doc.save(output)
    doc.close()
    print(f'Wrote {output.name}; updated {changed} CMEX text mapping(s).')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    main(sys.argv[1], sys.argv[2])
