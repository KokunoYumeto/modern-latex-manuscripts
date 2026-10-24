#!/usr/bin/env python3
"""重建指定版本的繁體字LaTeX；Reproduce a pinned Traditional-script source."""
import argparse
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen
import opencc
from opencc import OpenCC
from script_conversion import convert_outside_math, normalized

def digest(data):
    return hashlib.sha256(data).hexdigest().upper()

def require(data, expected, label):
    if len(data) != expected['bytes'] or digest(data) != expected['sha256']:
        raise ValueError('檔案身分不符 / identity mismatch: ' + label)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--variant', choices=['base', 'emendations'], required=True)
    parser.add_argument('--input', type=Path, help='本地簡體LaTeX；省略時下載指定公開版本')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    recipe = json.loads((Path(__file__).parent / 'profiles' / (args.variant + '.json')).read_text(encoding='utf-8'))
    if args.output.exists():
        raise FileExistsError('輸出已存在 / output already exists')
    package = Path(opencc.__file__).parent
    for name, expected in recipe['converter_files'].items():
        require((package / name).read_bytes(), expected, name)
    if args.input:
        data = args.input.read_bytes()
    else:
        with urlopen(recipe['input']['url'], timeout=60) as response:
            data = response.read()
    require(data, recipe['input'], 'input')
    converted, _ = convert_outside_math(data.decode('utf-8'), OpenCC('s2t'))
    converted, _ = normalized(converted)
    require(converted.encode('utf-8'), recipe['converted'], 'converted')
    lines = converted.splitlines(keepends=True)
    for replacement in reversed(recipe['profile']):
        start, end = replacement['start'], replacement['end']
        if ''.join(lines[start:end]) != replacement['expected']:
            raise ValueError('版本設定不符 / profile mismatch')
        lines[start:end] = [replacement['text']]
    result = ''.join(lines).encode('utf-8')
    require(result, recipe['output'], 'output')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('xb') as output:
        output.write(result)
    print(json.dumps({'bytes': len(result), 'sha256': digest(result)}, ensure_ascii=False))

if __name__ == '__main__':
    main()
