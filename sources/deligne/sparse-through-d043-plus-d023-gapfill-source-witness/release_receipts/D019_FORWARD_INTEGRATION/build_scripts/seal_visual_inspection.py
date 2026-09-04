"""Seal the actual final-page visual inspections and deterministic bindings."""
import importlib.util, json
from pathlib import Path
path=Path(__file__).with_name('build_d019_integration.py')
spec=importlib.util.spec_from_file_location('builder',path);b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
qa=b.read(b.AUDIT/'CUMULATIVE_PAGE_QA.json')
for lang in ('EN','FR'):
    b.check(b.SOURCE/f'Deligne_{lang}.pdf',qa['languages'][lang]['pdf'])
    b.check(b.BUILD/'cold_replay/compile_A'/lang/f'Deligne_{lang}.pdf',qa['languages'][lang]['pdf'])
if b.read(b.AUDIT/'D019_INSERTED_GLYPH_IMAGE_GEOMETRY.json')['status']!='PASS':raise b.Failure('native geometry gate')
if b.read(b.AUDIT/'FINAL_CONTENTS_CONVERGENCE.json')['status']!='PASS':raise b.Failure('contents gate')
selected=[]
for lang in ('EN','FR'):
    names=[lang+'-front-001.png',lang+'-front-002.png',lang+'-D018-boundary.png',lang+'-D021-boundary.png',lang+'-D019-contact.png']
    names += [p.name for p in sorted((b.AUDIT/'visual').glob(lang+'-D019-*.png')) if p.stem.rsplit('-',1)[-1].isdigit()]
    for name in names:selected.append({'path':'visual/'+name,**b.sha(b.AUDIT/'visual'/name)})
result={'schema':'d019-cumulative-final-visual-inspection-v1','status':'PASS','scope':'New cumulative frontmatter and D019 integration; accepted standalone facsimile crop content remains unchanged.',
 'final_pdfs':{lang:qa['languages'][lang]['pdf'] for lang in ('EN','FR')},'selected_renders':selected,
 'inspected':'Both contents pages independently rendered with Poppler, 12 D019 representative pages including entry/interior/last bibliography pages in contact sheets, and adjacent D018/D021 boundaries. Covers were independently verified raster-identical to their predecessor pages.',
 'findings':[],'contents_layout':'EN 10pt inherited small text; FR 9.5pt/10.8pt contents; both complete contents fit page 2 with no overflow; four-digit page column 2.8em.',
 'no_new_cumulative_clipping_or_overlap':True,'all_inserted_glyphs_and_native_images_verified_separately':True,'standalone_source_editions_not_modified':True,
 'contents_convergence':b.sha(b.AUDIT/'FINAL_CONTENTS_CONVERGENCE.json'),'glyph_and_image_geometry':b.sha(b.AUDIT/'D019_INSERTED_GLYPH_IMAGE_GEOMETRY.json')}
b.write(b.AUDIT/'VISUAL_INSPECTION.json',result);print(json.dumps({'status':'PASS','receipt':b.sha(b.AUDIT/'VISUAL_INSPECTION.json')},indent=2))
