from pathlib import Path
import fitz,hashlib,csv
R=Path(__file__).resolve().parents[2]; O=R/'qa/s04/source'; O.mkdir(parents=True,exist_ok=True)
S=fitz.open(R/'input/10_AUTHORITY_EXACT_SCOPE_PDF_PAGES_080_115_PRINTED_PP063_098.pdf'); F=fitz.open(R/'input/11_AUTHORITY_FULL_DIRICHLET_GESAMMELTE_WERKE_BAND_I_1889.pdf')
rows=[]
for n in range(36):
 a=S[n].get_pixmap(matrix=fitz.Matrix(3,3)); b=F[n+79].get_pixmap(matrix=fitz.Matrix(3,3))
 assert a.width==b.width and a.height==b.height and a.samples==b.samples
 f=O/f'p{n+63:03}_authority.png'; a.save(f)
 rows.append([n+63,n+80,n+1,hashlib.sha256(a.samples).hexdigest().upper(),f.relative_to(R).as_posix(),hashlib.sha256(f.read_bytes()).hexdigest().upper(),'IDENTICAL_216DPI'])
F[115].get_pixmap(matrix=fitz.Matrix(3,3)).save(O/'boundary_pdf116_inspection_only.png')
with (R/'qa/s04/SCOPE_RASTER_EQUIVALENCE.tsv').open('w') as out:
 w=csv.writer(out,delimiter='\t',lineterminator='\n');w.writerow(['printed_page','full_pdf_page','scope_leaf','raw_pixel_sha256','image_path','image_sha256','result']);w.writerows(rows)
print('36 source images at216dpi; exact-scope/full-volume raster identity verified. Boundary image only.')
