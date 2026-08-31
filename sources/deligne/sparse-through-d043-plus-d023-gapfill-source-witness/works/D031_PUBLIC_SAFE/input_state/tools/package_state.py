#!/usr/bin/env python3
import pathlib,sys,zipfile
def zi(name):
 z=zipfile.ZipInfo(name,date_time=(1980,1,1,0,0,0));z.compress_type=zipfile.ZIP_DEFLATED;z.create_system=3;z.external_attr=(0o100644&0xFFFF)<<16;z.flag_bits|=0x800;return z
root=pathlib.Path(sys.argv[1]).resolve();out=pathlib.Path(sys.argv[2]).resolve()
try:out.relative_to(root);raise SystemExit('output ZIP must be outside state root')
except ValueError:pass
files=[p for p in root.rglob('*') if p.is_file()]
assert not [p for p in files if '__pycache__' in p.parts or p.suffix.lower() in ('.pyc','.pyo')]
with zipfile.ZipFile(out,'w',allowZip64=True) as z:
 for p in sorted(files,key=lambda q:(q.relative_to(root).as_posix().casefold(),q.relative_to(root).as_posix())):
  z.writestr(zi(p.relative_to(root).as_posix()),p.read_bytes(),compresslevel=9)
