"""Verify exact returned D031 identities and extract bounded state, preserving inputs."""
from pathlib import Path, PurePosixPath
import csv, hashlib, json, zipfile

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]
EXTRACT = ROOT / 'NM_EXTRACT/20260831/D031_DELIGNE_D031_SHIMURA_CANONICAL_MODELS_FINAL_GLOBAL_AUDIT_BUNDLE_B5496ADB3A06'
ARCHIVE = Path('C:/Users/[LOCAL_ACCOUNT]/Documents/Papors/Chatnotes/CHat translates and clean/Noether Multilingual/DELIGNE_D031_SHIMURA_CANONICAL_MODELS_FINAL_GLOBAL_AUDIT_BUNDLE.zip')
EXPECTED = 'B5496ADB3A06E7FAE228E49461A9EC2A2C192B3AAED8E719BE140C4282BA345F'

def digest(data): return hashlib.sha256(data).hexdigest().upper()

def main():
    data = ARCHIVE.read_bytes()
    assert len(data) == 72931554 and digest(data) == EXPECTED
    outer = list(csv.DictReader((EXTRACT / '_EXTRACTION_MEMBERS.tsv').open(encoding='utf-8-sig', newline=''), delimiter='\t'))
    receipts = []
    for row in outer:
        p = Path(row['extracted_path']); b = p.read_bytes()
        assert len(b) == int(row['bytes']) and digest(b) == row['sha256']
        receipts.append(dict(path=row['member_path'], bytes=len(b), sha256=digest(b)))
    nested = EXTRACT / 'DELIGNE_D031_SHIMURA_CANONICAL_MODELS_S08_CUMULATIVE_FULL_STATE.zip'
    expected_rows = {r['path']: r for r in csv.DictReader((EXTRACT/'DELIGNE_D031_SHIMURA_CANONICAL_MODELS_S08_CUMULATIVE_MANIFEST.tsv').open(encoding='utf-8-sig', newline=''), delimiter='\t') if r['scope'] == 'STATE_MEMBER'}
    state = BASE / 'input_state'; state.mkdir(exist_ok=True)
    members = []
    with zipfile.ZipFile(nested) as z:
        assert len(z.infolist()) == len(expected_rows) == 20
        assert sum(i.file_size for i in z.infolist()) < 80000000
        for i in z.infolist():
            p = PurePosixPath(i.filename)
            assert not p.is_absolute() and '..' not in p.parts and '\\' not in i.filename
            assert i.filename in expected_rows and not i.is_dir()
            assert (i.external_attr >> 16) & 0o170000 != 0o120000
            b = z.read(i); r = expected_rows[i.filename]
            assert len(b) == int(r['bytes']) and digest(b) == r['sha256']
            dest = state.joinpath(*p.parts)
            assert dest.resolve().is_relative_to(state.resolve())
            dest.parent.mkdir(parents=True, exist_ok=True)
            if dest.exists(): assert dest.read_bytes() == b
            else: dest.write_bytes(b)
            members.append(dict(path=i.filename, bytes=len(b), sha256=digest(b)))
    receipt = dict(archive=str(ARCHIVE), bytes=len(data), sha256=EXPECTED, outer_members=receipts, state_members=members, inherited_prior_work='ZERO_ACCEPTED', status='PASS_EXACT_INPUT_IDENTITY')
    (BASE/'input_identity.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(dict(status=receipt['status'], members=len(members), stage=str(state))))

if __name__ == '__main__': main()
