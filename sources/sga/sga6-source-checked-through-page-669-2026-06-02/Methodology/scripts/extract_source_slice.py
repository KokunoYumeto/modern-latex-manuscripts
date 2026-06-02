#!/usr/bin/env python3
import argparse, fitz
p=argparse.ArgumentParser(); p.add_argument("source_pdf"); p.add_argument("start",type=int); p.add_argument("end",type=int); p.add_argument("output_pdf")
a=p.parse_args(); d=fitz.open(a.source_pdf); o=fitz.open(); o.insert_pdf(d, from_page=a.start-1, to_page=a.end-1); o.save(a.output_pdf)
