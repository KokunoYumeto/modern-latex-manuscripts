#!/usr/bin/env python3
"""Verify the four sibling handoff files. This does not accept any author text."""
from pathlib import Path, PurePosixPath
import csv, hashlib, json, sys, unicodedata, zipfile

def sha(data):
    return hashlib.sha256(data).hexdigest().upper()

def verify(directory):
    cp = json.loads((directory / 'CHECKPOINT.json').read_text(encoding='utf-8'))
    for name, binding in cp['artifact_hashes'].items():
        data = (directory / name).read_bytes()
        if len(data) != binding['bytes'] or sha(data) != binding['sha256']:
            raise ValueError('Artifact binding mismatch: ' + name)
    manifest = list(csv.DictReader((directory / 'MANIFEST.tsv').read_text(encoding='utf-8').splitlines(), delimiter='\t'))
    paths = [row['path'] for row in manifest]
    if len(paths) != len(set(paths)):
        raise ValueError('Duplicate manifest member')
    with zipfile.ZipFile(directory / cp['archive_filename']) as archive:
        if archive.testzip() is not None:
            raise ValueError('ZIP CRC error')
        infos = archive.infolist()
        names = [entry.filename for entry in infos]
        if len(names) != len(set(names)) or set(names) != set(paths):
            raise ValueError('Duplicate member or inexact manifest')
        for entry in infos:
            name = entry.filename
            path = PurePosixPath(name)
            if entry.is_dir() or path.is_absolute() or '..' in path.parts or '\\' in name or '\x00' in name or ':' in name or str(path) != name or unicodedata.normalize('NFC', name) != name:
                raise ValueError('Unsafe or non-normalized path: ' + name)
        for row in manifest:
            name = row['path']
            data = archive.read(name)
            actual = {'bytes': len(data), 'sha256': sha(data)}
            if actual['bytes'] != int(row['bytes']) or actual['sha256'] != row['sha256'] or cp['member_hashes'][name] != actual:
                raise ValueError('Member binding mismatch: ' + name)
        if set(cp['member_hashes']) != set(names):
            raise ValueError('Inexact checkpoint member set')
        if json.loads(archive.read('state/CURSOR.json')) != cp['state']:
            raise ValueError('Cursor binding mismatch')
        if archive.read('SOURCE_BACKED_DIFF.tsv') != (directory / 'SOURCE_BACKED_DIFF.tsv').read_bytes():
            raise ValueError('Diff sibling mismatch')
    print('Package integrity: PASS')
    print('Prompt 01 completion: ' + str(cp['state']['prompt_completed']))
    print('Next cursor: ' + str(cp['state']['next_cursor']))
    print('Accepted author pages: ' + str(cp['state']['accepted_author_page_count']))

if __name__ == '__main__':
    try:
        verify(Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve())
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as error:
        raise SystemExit('Verification error: ' + str(error))
