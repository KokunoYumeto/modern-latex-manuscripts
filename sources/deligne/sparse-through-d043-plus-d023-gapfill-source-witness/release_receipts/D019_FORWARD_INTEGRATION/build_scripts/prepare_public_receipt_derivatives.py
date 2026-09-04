"""Redact only literal local-account locators from copied public receipts."""
import importlib.util, json, os, re
from pathlib import Path
path=Path(__file__).with_name('build_d019_integration.py')
spec=importlib.util.spec_from_file_location('builder',path);b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
target=os.environ.get('USERNAME','')
if not target:raise b.Failure('no local account literal')
members=[]
for name in ('D019_CANONICAL_COLD_GATE.json','D019_CANONICAL_PRIMARY_GATE.json'):
    original=b.D019/'receipts'/name
    current=b.WORK/'receipts'/name
    identity=b.sha(original)
    b.check(current,identity)
    b.copy(original,b.BUILD/'nonpublic_original_receipts'/name)
    text=current.read_text(encoding='utf-8')
    new,count=re.subn(re.escape(target),'[LOCAL_ACCOUNT]',text,flags=re.IGNORECASE)
    if count==0:raise b.Failure('expected literal locator not found')
    b.write_text(current,new)
    members.append({'path':'receipts/'+name,'original':identity,'public_derivative':b.sha(current),'literal_substitutions':count})
receipt={'schema':'d019-public-receipt-derivative-binding-v1','status':'PASS','members':members,'transformation':'Only the case-insensitive literal local-account substring is replaced by [LOCAL_ACCOUNT] in copied receipt text. Original canonical gates and content remain unchanged.','original_gate_sha256':b.GATE_HASH,'original_receipts_preserved_locally':True,'nonpublic_originals_not_part_of_source_or_release_carriers':True,'canonical_pdf_tex_data_assets_and_source_packet_unchanged':True}
b.write(b.WORK/'receipts/D019_PUBLIC_RECEIPT_DERIVATIVE_BINDING.json',receipt)
b.write(b.AUDIT/'D019_PUBLIC_RECEIPT_DERIVATIVE_BINDING.json',receipt)
print(json.dumps(receipt,indent=2))
