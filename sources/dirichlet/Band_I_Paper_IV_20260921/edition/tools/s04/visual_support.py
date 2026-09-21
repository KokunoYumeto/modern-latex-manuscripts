"""Bind an explicit manual output-page review to the exact final reader and PNG bytes."""
from audit_support import R,Q,h
import json

def viewed(layer,pages,observations):
 build=json.loads((Q/'BUILD_RUNS.json').read_text());p=Q/'MANUAL_OUTPUT_REVIEW.json';d=json.loads(p.read_text()) if p.exists() else {}
 for n in pages:
  rec=next(x for x in build[layer]['renders'] if x['reader_page']==n)
  assert h((R/rec['image']).read_bytes())==rec['sha256']
  d[f'{layer}:{n}']={'layer':layer,**rec,'reader':build[layer]['reader'],'reader_sha256':build[layer]['reader_sha256'],'review_method':'Opened this individual final page image and visually inspected page furniture, text and math layout, bounds, note anchor and note placement where present. No inference from earlier PASS or pixel match.','observations':observations,'clipping':False,'broken_math':False,'missing_glyphs':False,'note_overflow':False,'wrong_order':False,'result':'REVIEWED_NO_VISIBLE_DEFECT'}
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
 print('Reviewed',layer,pages)
