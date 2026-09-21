from pathlib import Path
import json, shutil, sys
from tex_worker import Mutex, tex_pass
root=Path(__file__).resolve().parent
lanes=sys.argv[1:] or ['EN','FR']
assert all(x in ('EN','FR') for x in lanes)
receipt=[]
with Mutex(timeout_ms=30000) as mutex:
    for lane in lanes:
        for n in (1,2):
            result=tex_pass(mutex,shutil.which('xelatex'),root,f'Deligne_{lane}.tex',{'SOURCE_DATE_EPOCH':'946684800','FORCE_SOURCE_DATE':'1','TZ':'UTC','MIKTEX_ENABLE_INSTALLER':'0'},root/f'build_{lane}_{n}.stdout',900)
            receipt.append(result)
            assert result['return_code']==0
(root/'BUILD_RECEIPT.json').write_text(json.dumps(receipt,indent=2))
