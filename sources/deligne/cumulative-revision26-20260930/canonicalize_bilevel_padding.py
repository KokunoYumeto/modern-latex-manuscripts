"""Canonicalize only unused bilevel row bits; never edit visible image pixels.

Reproducible PDF serialization uses PyMuPDF, preserving the existing document ID.
Callers must impose their resource cap before invoking this module.
"""
from pathlib import Path
import hashlib

def canonicalize(source, destination=None):
    import fitz
    source = Path(source)
    if destination is not None:
        destination = Path(destination)
        assert destination.resolve()!=source.resolve() and not destination.exists()
    changed = []
    with fitz.open(source) as doc:
        for xref in range(1,doc.xref_length()):
            if doc.xref_get_key(xref,'Subtype')[1] != '/Image':
                continue
            if doc.xref_get_key(xref,'BitsPerComponent')[1] != '1':
                continue
            if doc.xref_get_key(xref,'ColorSpace')[1] != '/DeviceGray':
                continue
            width = int(doc.xref_get_key(xref,'Width')[1])
            height = int(doc.xref_get_key(xref,'Height')[1])
            if width%8==0:
                continue
            original = doc.xref_stream(xref)
            stride = (width+7)//8
            assert len(original)==stride*height, 'unsupported decoded image packing'
            value = bytearray(original)
            mask = (0xff << (8-width%8)) & 0xff
            changed_rows = 0
            for offset in range(stride-1,len(value),stride):
                masked = value[offset] & mask
                changed_rows += masked!=value[offset]
                value[offset] = masked
            if value!=original:
                doc.update_stream(xref,bytes(value),compress=True)
                changed.append({'xref':xref,'width':width,'height':height,
                                'unused_bits_per_row':8-width%8,'changed_rows':changed_rows})
            del original,value
        data = doc.tobytes(garbage=0,deflate=False,no_new_id=True)
    result = {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest().upper(),
              'unused_padding_normalized':changed,'visible_bits_changed':0}
    if destination is not None:
        destination.write_bytes(data)
    del data
    return result
