"""Reproduce only this extracted edition, once, under the machine-wide slot."""
from pathlib import Path
import datetime as dt
import hashlib,json,shutil
from tex_worker import Mutex,tex_pass,scan_log_anomalies
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'rebuild';RECEIPT=OUT/'REBUILD_RECEIPT.json'
assert not OUT.exists(),'Preserve an existing rebuild; do not restart it'
def sha(p):
    with p.open('rb') as s:return hashlib.file_digest(s,'sha256').hexdigest().upper()
manifest=json.loads((ROOT/'MANIFEST.json').read_text(encoding='utf-8'))
for item in manifest['files']:
    p=ROOT/item['path'];assert p.stat().st_size==item['bytes'] and sha(p)==item['sha256'],item['path']
engine=shutil.which('pdflatex');assert engine,'Installed pdfLaTeX required; no installer is launched'
OUT.mkdir()
receipt=dict(schema='d016-portable-rebuild-v1',utc=dt.datetime.now(dt.timezone.utc).isoformat(),status='PREPARED',
             acquisition_timeout_ms=30000,tex_passes_launched=0,mutex_acquired=False,documents=[])
def save():RECEIPT.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
env={'SOURCE_DATE_EPOCH':'946684800','FORCE_SOURCE_DATE':'1','TZ':'UTC','MIKTEX_ENABLE_INSTALLER':'0',
     'TEXINPUTS':str(ROOT/'TEX_DEPENDENCIES').replace('\\','/')+'//;'}
try:
    with Mutex(timeout_ms=30000) as mutex:
        receipt.update(mutex_acquired=True,mutex_wait_ms=mutex.wait_ms,mutex_abandoned_recovery=mutex.abandoned,status='RUNNING');save()
        for lane in ('FR','EN'):
            slot=OUT/lane;slot.mkdir();name=f'Deligne_{lane}.tex'
            shutil.copyfile(ROOT/f'D016_{lane}.tex',slot/name)
            row=dict(lane=lane,source_sha256=sha(ROOT/f'D016_{lane}.tex'),passes=[]);receipt['documents'].append(row)
            for number in (1,2,3):
                receipt['tex_passes_launched']+=1;save()
                result=tex_pass(mutex,engine,slot,name,env,slot/f'pass{number}.stdout',180)
                row['passes'].append(result);save();assert result['return_code']==0,result
                result['pdf_sha256']=sha(slot/f'Deligne_{lane}.pdf')
            row['log_anomalies']=scan_log_anomalies(slot/f'Deligne_{lane}.log')
            assert not any(row['log_anomalies'].values())
            assert row['passes'][-1]['pdf_sha256']==row['passes'][-2]['pdf_sha256']==sha(ROOT/f'D016_{lane}.pdf')
            row['exact_pdf_identity']=True;save()
    receipt.update(status='EXACT_PDF_REBUILD_PASS',mutex_released=True);save()
except Exception as error:
    receipt.update(status='FAILED',failure=str(error));save();raise
print(json.dumps({'status':receipt['status'],'passes':receipt['tex_passes_launched'],'peak_bytes':max(p['peak_job_memory_bytes'] for r in receipt['documents'] for p in r['passes'])}))
