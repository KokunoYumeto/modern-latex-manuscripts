from pathlib import Path
import csv, hashlib, json, re, subprocess

HERE=Path(__file__).resolve().parent; T=HERE.parent
tex=T/'tex'/'R823_HG_T001_romance.tex'; source=T/'source'/'R823_HG_T001_de_exact.tex'
metadata=T/'source'/'R823_HG_T001_de_metadata_exact.tex'; source_manifest=T/'source'/'R823_HG_T001_SOURCE_MANIFEST.json'
clause=T/'semantic'/'R823_HG_T001_clause_map.csv'; terms=T/'terminology'/'R823_HG_T001_TERMINOLOGY_v1.csv'
grammar=T/'grammar'/'CONTROLLED_ROMANCE_GRAMMAR_TEST_v1.csv'
pdf=T/'build'/'R823_HG_T001_romance.pdf'; extracted=T/'qa'/'R823_HG_T001_extracted.txt'
pdfinfo=T/'qa'/'R823_HG_T001_pdfinfo.txt'
text=tex.read_text(encoding='utf-8'); src=source.read_text(encoding='utf-8'); ext=extracted.read_text(encoding='utf-8',errors='replace')
pdfinfo_text=pdfinfo.read_text(encoding='utf-8',errors='replace')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest().upper()

manifest=json.loads(source_manifest.read_text(encoding='utf-8'))
with clause.open(encoding='utf-8-sig',newline='') as f: clauses=list(csv.DictReader(f))
with terms.open(encoding='utf-8-sig',newline='') as f: termrows=list(csv.DictReader(f))
with grammar.open(encoding='utf-8-sig',newline='') as f: grammarrows=list(csv.DictReader(f))
ids=[]
for r in clauses:
    ids.extend(x.strip() for x in r['target_sentence_ids'].split(';'))
target_markers=set(re.findall(r'\bT-(?:\d{3}[A-Z]?|[A-Z]\d+)\b',text))
missing=[x for x in ids if x not in target_markers]
assert not missing,missing
assert all(r['review_status']=='accounted' for r in clauses)
assert len(clauses)==27
assert len(termrows)>=35
assert all(r['source_term'] and r['target_term'] and r['sense'] and r['status'] and r['source_evidence'] for r in termrows)
assert len(grammarrows)==18
assert all(all(r.get(field,'').strip() for field in ('feature','decision','alternatives_considered','supporting_rationale','adverse_evidence','status')) for r in grammarrows)
assert {r['feature'] for r in grammarrows} >= {'definite_article','indefinite_article','plural','adjective','copula','lexical_present','passive_impersonal','negation','coordination','relative','conditional','not_only_but','demonstrative','possessive','prepositions','derivation','left_right_actions','pronunciation'}
assert {r['status'] for r in grammarrows} <= {'test_only','held'}

required=[
 r'\mathfrak{o}\to\mathfrak D\subseteq\mathsf T_n',
 r'\mathfrak{o}\mapsto\mathfrak D^*\subseteq\mathsf T_n^*',
 r'c^*\!\cdot d^*=(dc)^*',
 r'al producto $cd$ corresponde $d^*\!\cdot c^*$',
 r'al suma $c+d$ corresponde $c^*+d^*$',
]
assert all(x in text for x in required)
assert not re.search(r'\b(TODO|FIXME|UNTRANSLATED|PLACEHOLDER)\b',text,re.I)
solidus_tokens=re.findall(r'(?<!\S)\S*/\S+(?!\S)',text)
date_ranges=re.findall(r'\b(?:18|19|20)\d{2}/\d{2,4}\b',text)
lexical_slash_bundles=re.findall(r'(?iu)\b[^\W\d_]+(?:-[^\W\d_]+)*\s*/\s*[^\W\d_]+(?:-[^\W\d_]+)*\b',text)
unclassified_solidus=[x for x in solidus_tokens if not re.search(r'\b(?:18|19|20)\d{2}/\d{2,4}\b',x)]
assert not lexical_slash_bundles,lexical_slash_bundles
assert not unclassified_solidus,unclassified_solidus
assert 'la elemento' not in text and 'la numeros' not in text and '\nson ' not in text
assert source.read_bytes().endswith(b'\n')
assert sha(source)=='33E4D17FEC404CB5B5A7DF208EE1BC5855BB6B0F4091A04905B95B75C1D9AF64'
assert metadata.read_bytes().endswith(b'\n')
assert sha(metadata)=='D424D5D19D8B8E153B1DF736933F71B83098A5C54135646561B9E3E2C8519559'
assert manifest['body_source_lines']==[21047,21087] and manifest['metadata_source_lines']==[20985,20990]
assert manifest['body_exact_slice_sha256']==sha(source) and manifest['metadata_exact_slice_sha256']==sha(metadata)
assert manifest['clause_map_sha256']==sha(clause)
assert pdf.exists() and pdf.stat().st_size>20000
assert 'R823-HG-T001' in ext and 'c∗ · d∗ = (dc)∗' in ext
assert re.search(r'^Pages:\s+3\s*$',pdfinfo_text,re.M)
assert re.search(r'^Page size:\s+595\.276 x 841\.89 pts \(A4\)\s*$',pdfinfo_text,re.M)

log={
 'artifact':'R823_HG_T001_VALIDATION','status':'PASS','authority_body_slice_sha256':sha(source),'authority_metadata_slice_sha256':sha(metadata),'source_manifest_sha256':sha(source_manifest),'target_tex_sha256':sha(tex),'pdf_sha256':sha(pdf),
 'extracted_text_sha256':sha(extracted),'pdfinfo_sha256':sha(pdfinfo),
 'clause_map_sha256':sha(clause),'terminology_sha256':sha(terms),'grammar_sha256':sha(grammar),
 'clause_rows':len(clauses),'target_ids':len(ids),'terminology_rows':len(termrows),'grammar_rows':len(grammarrows),'grammar_required_features_checked':True,'all_source_segments_accounted':True,
 'product_order_reversal_present':True,'addition_order_preserved':True,'display_count_source':src.count('\\['),'display_count_target':text.count('\\['),
 'placeholders':0,'solidus_tokens_total':len(solidus_tokens),'date_ranges_exempted':len(date_ranges),
 'date_range_tokens':date_ranges,'lexical_alternative_bundles_in_running_prose':len(lexical_slash_bundles),
 'unclassified_solidus_tokens':len(unclassified_solidus),'slash_bundles_in_running_prose':len(lexical_slash_bundles),
 'validator_sha256':sha(HERE/'validate_t001.py'),'human_validation_rows':0,'pilot_claim':False,
}
assert log['display_count_source']==3 and log['display_count_target']==3
(T/'qa'/'R823_HG_T001_validation.json').write_text(json.dumps(log,indent=2)+'\n',encoding='utf-8')
print(json.dumps(log,indent=2))
