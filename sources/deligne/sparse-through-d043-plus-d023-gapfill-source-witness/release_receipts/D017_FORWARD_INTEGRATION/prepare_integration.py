"""Copy/map accepted D017 inputs into this new preparation directory only."""
import hashlib,io,json,subprocess,sys,zipfile
from pathlib import Path,PurePosixPath
ROOT=Path(__file__).resolve().parent
ACCEPTED=ROOT.parent/'packet'
LIMIT=99000000
def sha(b):return hashlib.sha256(b).hexdigest().upper()
def identity(p):
    with p.open('rb') as f:h=hashlib.file_digest(f,'sha256').hexdigest().upper()
    return {'bytes':p.stat().st_size,'sha256':h}
def encode(obj):return (json.dumps(obj,indent=2,sort_keys=True,ensure_ascii=False)+'\n').encode('utf-8')
def write(path,data):
    path=path.resolve()
    assert path.is_relative_to(ROOT)
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists():assert path.read_bytes()==data,('refuse changed overwrite',path.name)
    else:path.write_bytes(data)
def load(path):return json.loads(path.read_text(encoding='utf-8-sig'))

gate=load(ACCEPTED/'D017_CORPUS_GATE.json')
verification=load(ROOT.parent/'D017_PACKET_VERIFICATION.json')
assert gate['status']=='PAPER_COMPLETE_CORPUS_GATE_PASS'
assert identity(ACCEPTED/'D017_CORPUS_GATE.json')['sha256']=='F7BA685B8099CE94A68F3D2F47AD7DA9B8E04F6D01AFF0261897DE147D0534DD'
accepted_before={n:identity(ACCEPTED/n) for n in verification['publication_surface']}
assert accepted_before==verification['publication_surface']
outer=ROOT.parent/'D017_PAPER_COMPLETE_REPAIRED_PACKET.zip'
assert identity(outer)=={k:verification['packet'][k] for k in ('bytes','sha256')}
mapping=[]
def put(source,destination,role,origin):
    b=source.read_bytes()
    write(ROOT/destination,b)
    mapping.append({'path':destination,'bytes':len(b),'sha256':sha(b),'role':role,'origin':origin})

for stem in ('D017_FR','D017_EN','D017_Apparatus'):
    put(ACCEPTED/(stem+'.pdf'),'D017/readers/'+stem+'.pdf','accepted_standalone_reader','accepted_packet/'+stem+'.pdf')
put(ACCEPTED/'D017_Source.zip','D017/source_archive/D017_Source.zip','accepted_editable_source_archive','accepted_packet/D017_Source.zip')
for source,name in ((ACCEPTED/'D017_CORPUS_GATE.json','D017_CORPUS_GATE.json'),
 (ACCEPTED/'MANIFEST.json','ACCEPTED_PACKET_MANIFEST.json'),
 (ROOT.parent/'D017_PACKET_VERIFICATION.json','D017_PACKET_VERIFICATION.json'),
 (ROOT.parent/'candidate/PUBLIC_PROVENANCE_TRANSFORMATION.json','PUBLIC_PROVENANCE_TRANSFORMATION.json')):
    put(source,'D017/acceptance/'+name,'immutable_acceptance_or_provenance_receipt','accepted_D017/'+name)

source_members=[]
with zipfile.ZipFile(ACCEPTED/'D017_Source.zip') as z:
    assert z.testzip() is None
    source_manifest=load(ROOT.parent/'candidate/SOURCE_MANIFEST.json')
    for info in z.infolist():
        assert not info.is_dir()
        path=PurePosixPath(info.filename)
        assert not path.is_absolute() and '..' not in path.parts and '\\' not in info.filename
        assert ((info.external_attr>>16)&0o170000)!=0o120000
        b=z.read(info)
        if info.filename!='SOURCE_MANIFEST.json':
            assert source_manifest[info.filename]=={'bytes':len(b),'sha256':sha(b)}
        dest='D017/source/'+info.filename
        write(ROOT/dest,b)
        row={'path':dest,'bytes':len(b),'sha256':sha(b),'role':'exact_extracted_source_member','origin':'D017_Source.zip!/'+info.filename}
        mapping.append(row);source_members.append(row)
assert len(source_members)==41
tex_equalities=[]
for stem in ('D017_FR','D017_EN','D017_Apparatus'):
    a=ACCEPTED/(stem+'.tex');b=ROOT/'D017/source/sources'/(stem+'.tex')
    assert a.read_bytes()==b.read_bytes()
    tex_equalities.append({'accepted_packet_member':stem+'.tex','source_tree_member':'D017/source/sources/'+stem+'.tex',**identity(a)})
assert (ROOT/'D017/source/authority/D017_Authority.pdf').read_bytes()==(ACCEPTED/'D017_Authority.pdf').read_bytes()

carrier=ACCEPTED/'D017_Public_Provenance.zip'
chunks=[]
offset=0
with carrier.open('rb') as f:
    while b:=f.read(LIMIT):
        name=f'chunks/D017_Public_Provenance.zip.part{len(chunks)+1:03d}'
        assert len(b)<100000000
        write(ROOT/'D017/provenance'/name,b)
        row={'path':name,'offset':offset,'bytes':len(b),'sha256':sha(b)}
        chunks.append(row)
        mapping.append({'path':'D017/provenance/'+name,'bytes':len(b),'sha256':sha(b),'role':'binary_transfer_chunk','origin':'accepted_packet/D017_Public_Provenance.zip','source_offset':offset})
        offset+=len(b)
assert offset==gate['files']['D017_Public_Provenance.zip']['bytes']
chunk_manifest={'schema_version':1,'work_id':'D017','carrier':{'filename':carrier.name,**identity(carrier)},'chunking':'Consecutive unmodified slices of 99,000,000 bytes, final remainder; concatenate in listed order.','max_chunk_bytes_exclusive':100000000,'chunks':chunks,'inherited_acceptance':'ZERO_ACCEPTED','public_derivative_not_private_original':True}
write(ROOT/'D017/provenance/CHUNK_MANIFEST.json',encode(chunk_manifest))
mapping.append({'path':'D017/provenance/CHUNK_MANIFEST.json',**identity(ROOT/'D017/provenance/CHUNK_MANIFEST.json'),'role':'ordered_transfer_manifest','origin':'deterministic_preparation'})

result=subprocess.run([sys.executable,str(ROOT/'reassemble_provenance.py'),'--reference',str(carrier)],capture_output=True,text=True,check=True)
reassembly=json.loads(result.stdout)
assert reassembly['status']=='PASS' and reassembly['byte_for_byte_reference_comparison']
write(ROOT/'REASSEMBLY_VERIFICATION.json',encode(reassembly))
for name in ('prepare_integration.py','reassemble_provenance.py','verify_integration.py','INTEGRATION_NOTES.md','REASSEMBLY_VERIFICATION.json'):
    mapping.append({'path':name,**identity(ROOT/name),'role':'integration_instruction_or_verification','origin':'deterministic_preparation'})

manifest={'schema_version':1,'work_id':'D017','status':'INTEGRATION_INPUTS_VERIFIED','accepted_scope_physical':list(range(1,52)),
 'actual_next_public_baseline':None,'baseline_rule':'Parent resolves the actual verified baseline after the in-progress publication; no predecessor ID is assumed here.',
 'work_relative_root':'D017','accepted_gate':identity(ACCEPTED/'D017_CORPUS_GATE.json'),'accepted_outer_packet':identity(outer),
 'accepted_public_files_before':accepted_before,'source_member_count':41,'standalone_tex_equalities':tex_equalities,
 'fallback_asset_count':11,'public_carrier':chunk_manifest['carrier'],'transfer_chunk_count':len(chunks),
 'source_tree_mapping':sorted(mapping,key=lambda r:r['path']),
 'no_cumulative_build':True,'no_publication_or_git':True,'shared_ledgers_unchanged_by_this_tool':True}
data=encode(manifest)
assert data==encode(json.loads(data))
write(ROOT/'INPUT_MANIFEST.json',data)
accepted_after={n:identity(ACCEPTED/n) for n in accepted_before}
assert accepted_after==accepted_before
assert identity(outer)==manifest['accepted_outer_packet']
receipt={'status':'PASS','input_manifest':{'bytes':len(data),'sha256':sha(data)},'deterministic_manifest_second_serialization_equal':True,
 'accepted_packet_and_gate_unchanged':True,'every_source_member_exact':True,'all_chunks_below_100000000_bytes':True,
 'complete_chunk_reassembly_compared_byte_for_byte_with_accepted_carrier':True,'mapped_files':len(mapping),
 'next_action':'Parent integrates these exact inputs only after resolving the actual next public baseline; preserve numerical sparse ordering and run independent cumulative QA.'}
write(ROOT/'PREPARATION_RECEIPT.json',encode(receipt))
print(json.dumps({'status':'PASS','manifest':receipt['input_manifest'],'chunks':chunks,'mapped_files':len(mapping),'accepted_unchanged':True}))
