"""Restore exact original carriers beside this script; one request per missing file."""
import hashlib, json, sys, urllib.parse, urllib.request
from pathlib import Path, PurePosixPath


def check(path, row):
    h = hashlib.sha256()
    count = 0
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            count += len(block)
            h.update(block)
    if count != row['bytes'] or h.hexdigest().upper() != row['sha256']:
        raise RuntimeError('Original-carrier identity mismatch')


def main():
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / 'RELEASE_ASSETS.json').read_text())
    for row in manifest['files']:
        relative = PurePosixPath(row['path'])
        target = (root / relative).resolve()
        if relative.is_absolute() or '..' in relative.parts or not target.is_relative_to(root):
            raise RuntimeError('Restoration path escaped source root')
        if target.exists():
            check(target, row)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        temporary = target.with_name(target.name + '.download')
        if temporary.exists():
            check(temporary, row)
        else:
            url = manifest['release_download_base'] + '/' + urllib.parse.quote(row['asset'], safe='')
            with urllib.request.urlopen(url, timeout=120) as response, temporary.open('xb') as output:
                for block in iter(lambda: response.read(1024 * 1024), b''):
                    output.write(block)
        check(temporary, row)
        temporary.replace(target)
    for row in manifest.get('archives', []):
        relative = PurePosixPath(row['path'])
        target = (root / relative).resolve()
        if relative.is_absolute() or '..' in relative.parts or not target.is_relative_to(root):
            raise RuntimeError('Archive restoration path escaped source root')
        if target.exists():
            check(target, row)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        part_paths = []
        for part in row['parts']:
            if Path(part['asset']).name != part['asset']:
                raise RuntimeError('Invalid part asset name')
            local = target.parent / part['asset']
            if not local.exists():
                url = manifest['release_download_base'] + '/' + urllib.parse.quote(part['asset'], safe='')
                with urllib.request.urlopen(url, timeout=120) as response, local.open('xb') as output:
                    for block in iter(lambda: response.read(1024 * 1024), b''):
                        output.write(block)
            check(local, part)
            part_paths.append(local)
        temporary = target.with_name(target.name + '.reassembled')
        if not temporary.exists():
            with temporary.open('xb') as output:
                for part in part_paths:
                    with part.open('rb') as stream:
                        for block in iter(lambda: stream.read(1024 * 1024), b''):
                            output.write(block)
        check(temporary, row)
        temporary.replace(target)
    print('Original carriers restored with exact byte-count and SHA-256 checks.')


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print('Restoration failed: ' + type(exc).__name__, file=sys.stderr)
        sys.exit(1)
