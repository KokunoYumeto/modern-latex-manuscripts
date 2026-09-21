from pathlib import Path
import hashlib,zipfile,csv,json,io,shutil
R=Path(__file__).resolve().parents[2]; P=R.parent
H=lambda b:hashlib.sha256(b).hexdigest().upper()
Z=P/'DIRICHLET_P04_S03_CUMULATIVE_FULL_STATE.zip'
C=json.loads((P/'CHECKPOINT.json').read_text())
M=list(csv.DictReader((P/'MANIFEST.tsv').open(),delimiter='\t'))
assert Z.stat().st_size==210121951 and H(Z.read_bytes())=='E60E5A926AFCF66800C25C357690D0097AE4573B840F836755B3581B12923007'
with zipfile.ZipFile(Z) as z:
 assert z.testzip() is None
 names=z.namelist(); assert len(names)==len(set(names))==793
 assert set(names)=={r['path'] for r in M}==set(C['archive_members'])
 for r in M:
  b=z.read(r['path']); assert len(b)==int(r['bytes']) and H(b)==r['sha256']
  assert C['archive_members'][r['path']]=={'bytes':len(b),'sha256':H(b)}
  assert (R/r['path']).read_bytes()==b
  q=Path(r['path']); assert not q.is_absolute() and '..' not in q.parts and '\\' not in str(q)
 for k,f in [('cumulative_zip',Z),('manifest',P/'MANIFEST.tsv')]:
  assert f.stat().st_size==C['release_artifacts'][k]['bytes'] and H(f.read_bytes())==C['release_artifacts'][k]['sha256']
 d=z.read('SOURCE_BACKED_DIFF.tsv'); assert len(d)==27503 and H(d)==C['release_artifacts']['source_backed_diff']['sha256']
 assert len(list(csv.DictReader(io.StringIO(d.decode()),delimiter='\t')))==72
 assert C['next_cursor']==4 and C['prompt_completed']==3
 for k in ['accepted_french_pages','accepted_english_pages','accepted_apparatus_pages']:assert C[k]==list(range(65,99))
 assert C['accepted_copy_matter_pages']==[63,64]
 for f in ['CHECKPOINT.json','MANIFEST.tsv']:
  shutil.copy2(P/f,R/'history/S03'/f)
 (R/'history/S03/SOURCE_BACKED_DIFF_CANONICAL.tsv').write_bytes(d)
 shutil.copy2(P/'SOURCE_BACKED_DIFF.tsv',R/'history/S03/SOURCE_BACKED_DIFF_STALE_STANDALONE.tsv')
 # All original bytes can now be recovered from original archive during preservation finalization.
for row in csv.DictReader((R/'input/02_INPUT_PAYLOAD_INVENTORY.tsv').open(),delimiter='\t'):
 p=R/'input'/row['file']; assert p.stat().st_size==int(row['bytes']) and H(p.read_bytes())==row['sha256']
import fitz
F=fitz.open(R/'input/11_AUTHORITY_FULL_DIRICHLET_GESAMMELTE_WERKE_BAND_I_1889.pdf')
S=fitz.open(R/'input/10_AUTHORITY_EXACT_SCOPE_PDF_PAGES_080_115_PRINTED_PP063_098.pdf')
assert len(F)==657 and len(S)==36
for f in (R/'input').glob('*.zip'):
 with zipfile.ZipFile(f) as z:assert z.testzip() is None
receipt={'schema':'dirichlet-s04-intake-v1','previous_zip':{'file':Z.name,'bytes':Z.stat().st_size,'sha256':H(Z.read_bytes())},'fresh_unpack':True,'member_count':793,'all_member_size_hash_checks':True,'crc_safe_unique_paths':True,'checkpoint_manifest_bindings':True,'canonical_diff_from_zip':{'bytes':len(d),'sha256':H(d),'rows':72},'stale_standalone':{'bytes':(P/'SOURCE_BACKED_DIFF.tsv').stat().st_size,'sha256':H((P/'SOURCE_BACKED_DIFF.tsv').read_bytes()),'used_as_current':False},'authority_bytes_opened':{'full':len(F),'scope':len(S)},'editable_fr_en_pages_readable':all((R/f'editions/{l}/pages/p{p:03}.tex').is_file() for l in ['fr','en'] for p in range(65,99)),'controls_read':['input/'+p.name for p in sorted((R/'input').glob('0*'))]+['input/23_PROMPT_04_COLD_AUDIT_FINAL.md'],'current_cursor':4,'acceptance_interpretation':'Sequential intake only; no inherited fidelity claims used as cold collation evidence.'}
(R/'qa/s04/INTAKE_VALIDATION.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
