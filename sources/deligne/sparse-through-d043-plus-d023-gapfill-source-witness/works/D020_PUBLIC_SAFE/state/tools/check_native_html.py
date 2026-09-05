#!/usr/bin/env python3
"""Read-only font/structure diagnostic for native HTML and its converter."""
import json,pathlib,re,sys
sys.dont_write_bytecode=True
root=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'tools'/'vendor'))
from latex2mathml.converter import convert
for expression in (r'\mathrm{T}',r'{\rm T}',r'\mathbf{Q}',r'\mathcal{F}',r'\xrightarrow{\sigma^*}'):
    print(repr(expression),convert(expression))
for layer in ('source_language','english_standalone','apparatus'):
    body=(root/'readers'/f'{layer}.html').read_text(encoding='utf-8')
    print(layer,{'math':body.count('<math '),'normal':body.count('mathvariant="normal"'),'literal_controls':re.findall(r'\\[A-Za-z]+',body)[:25]})
