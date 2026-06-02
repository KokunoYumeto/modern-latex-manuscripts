#!/usr/bin/env python3
import argparse, pathlib, hashlib
p=argparse.ArgumentParser(); p.add_argument("root"); p.add_argument("output")
a=p.parse_args(); root=pathlib.Path(a.root)
with open(a.output,"w") as f:
    for x in sorted(y for y in root.rglob("*") if y.is_file()): f.write(f"{hashlib.sha256(x.read_bytes()).hexdigest()}  {x.relative_to(root)}
")
