"""Preserve completed EN replicas; repair/replay only French frontmatter."""
import importlib.util, json, shutil
from pathlib import Path
path=Path(__file__).with_name('build_d019_integration.py')
spec=importlib.util.spec_from_file_location('builder',path);b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)

def main():
    old=b.read(b.AUDIT/'COLD_REPRODUCIBILITY_RECEIPT.json')
    b.copy(b.AUDIT/'COLD_REPRODUCIBILITY_RECEIPT.json',b.BUILD/'pre_final_frontmatter/COLD_REPRODUCIBILITY_RECEIPT.json')
    b.copy(b.AUDIT/'TEX_MUTEX_RECEIPT.json',b.BUILD/'pre_final_frontmatter/TEX_MUTEX_RECEIPT.json')
    for replica in ('compile_A','compile_B','cold_replay'):
        b.copy(b.BUILD/'cold_replay'/replica/'FR/Deligne_FR.pdf',b.BUILD/'pre_final_frontmatter'/replica/'FR/Deligne_FR.pdf')
    b.copy(b.SOURCE/'Deligne_FR.pdf',b.BUILD/'pre_final_frontmatter/Deligne_FR.pdf')
    receipt={'status':'RUNNING','name':'Global\\InterlanguageTeXSlotV1','timeout_ms':600000,'passes':0,'scope':'French frontmatter final clean replicas; completed EN replicas retained unchanged','captured_tree_policy':'private kill-on-close job assigned before resume; no shell escape; zero active descendants at return'}
    b.write(b.AUDIT/'FR_FINAL_TEX_MUTEX_RECEIPT.json',receipt)
    b.cursor('FR_FINAL_FRONTMATTER_REPLAY_RUNNING','Re-poll current worker; no duplicate build. Completed English is preserved. Then repeat all-page QA and exact inserted glyph/native-image geometry.',mutex_receipt='build/cumulative/audit/FR_FINAL_TEX_MUTEX_RECEIPT.json')
    deps=['Deligne_FR.tex']+[r['path'] for r in b.includes(b.SOURCE,'FR')]; records=[]
    try:
        with b.Mutex() as mutex:
            receipt.update(acquired_utc=b.now(),abandoned_recovery=mutex.abandoned,wait_ms=mutex.wait_ms);b.write(b.AUDIT/'FR_FINAL_TEX_MUTEX_RECEIPT.json',receipt)
            for replica in ('compile_A','compile_B','cold_replay'):
                slot=b.safe(b.BUILD/'tex_slot/FR')
                if slot.exists():raise b.Failure('existing French slot')
                slot.mkdir(parents=True)
                for dep in deps:b.copy(b.SOURCE/dep,slot/dep)
                passes=[];prior_toc=None
                for i in (1,2,3):
                    passes.append(b.tex_pass(shutil.which('xelatex'),slot,'Deligne_FR.tex',b.AUDIT/'tex_logs'/f'final_{replica}_FR_{i}.txt'))
                    current_toc=b.sha(slot/'Deligne_FR.toc')
                    if i==3 and prior_toc!=current_toc:raise b.Failure('French TOC did not converge')
                    prior_toc=current_toc;receipt['passes']+=1;b.write(b.AUDIT/'FR_FINAL_TEX_MUTEX_RECEIPT.json',receipt)
                pdf=slot/'Deligne_FR.pdf';topology=b.includes(b.SOURCE,'FR',pdf)
                with b.fitz.open(pdf) as doc:pages=len(doc)
                if pages!=1053 or topology[0]['first']!=3:raise b.Failure('French frontmatter not compact/stable')
                dest=b.BUILD/'cold_replay'/replica/'FR/Deligne_FR.pdf'
                shutil.copy2(pdf,b.safe(dest))
                records.append({'replica':replica,'pdf':b.sha(pdf),'pages':pages,'frontmatter_pages':2,'passes':passes,'toc_converged':True,'toc':current_toc})
                if slot.parent!=(b.BUILD/'tex_slot').resolve():raise b.Failure('scratch boundary')
                shutil.rmtree(slot)
            if len({r['pdf']['sha256'] for r in records})!=1:raise b.Failure('French clean replay mismatch')
            shutil.copy2(b.BUILD/'cold_replay/compile_A/FR/Deligne_FR.pdf',b.safe(b.SOURCE/'Deligne_FR.pdf'))
            receipt.update(status='PASS',captured_trees_ended=True,release_utc=b.now());b.write(b.AUDIT/'FR_FINAL_TEX_MUTEX_RECEIPT.json',receipt)
    except Exception as e:
        receipt.update(status='FAIL',failure=str(e),released_utc=b.now());b.write(b.AUDIT/'FR_FINAL_TEX_MUTEX_RECEIPT.json',receipt);raise
    old['languages']['FR']={'replicas':records,'byte_identical':True,'pages':1053}
    old['tex_mutex_receipts']={'initial_en_and_superseded_fr':b.sha(b.AUDIT/'TEX_MUTEX_RECEIPT.json'),'final_fr':b.sha(b.AUDIT/'FR_FINAL_TEX_MUTEX_RECEIPT.json')}
    old['passes_per_replica']={'EN':2,'FR':3}
    old['frontmatter_repair']='French contents typography 9.5pt/10.8pt; no body page or reader changes; three-pass TOC convergence verified.'
    b.write(b.AUDIT/'COLD_REPRODUCIBILITY_RECEIPT.json',old)
    b.cursor('TEX_REPRODUCIBILITY_PASS','Run final every-page identity, inserted glyph/native-image QA, and visual inspection; package after all deterministic checks pass.',cold_reproducibility=b.sha(b.AUDIT/'COLD_REPRODUCIBILITY_RECEIPT.json'))
    print(json.dumps({'status':'PASS','pages':1053,'pdf':b.sha(b.SOURCE/'Deligne_FR.pdf'),'receipt':b.sha(b.AUDIT/'COLD_REPRODUCIBILITY_RECEIPT.json')},indent=2))
if __name__=='__main__':main()
