"""Build the Volume VIII reader from the editable LaTeX source directory."""

import argparse
from importlib.util import find_spec
import json
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import mkdtemp


def run_logged(arguments, directory, log):
    with log.open("wb") as stream:
        result = subprocess.run(arguments, cwd=directory, stdout=stream, stderr=subprocess.STDOUT)
    if result.returncode:
        raise RuntimeError(f"{Path(arguments[0]).name} exited with status {result.returncode}. See {log}")


def compile_component(xelatex, component, work, main, first_page):
    work.mkdir()
    entry = main
    if first_page is not None:
        wrapper = work / "reader_entry.tex"
        wrapper.write_text(
            rf"\AtBeginDocument{{\setcounter{{page}}{{{first_page}}}}}" + "\n"
            + rf"\input{{{main}}}" + "\n",
            encoding="utf-8",
            newline="\n",
        )
        entry = str(wrapper)
    arguments = [
        xelatex, "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "-no-shell-escape",
        f"-output-directory={work}", "-jobname=source", entry,
    ]
    for pass_number in (1, 2):
        run_logged(arguments, component, work / f"xelatex-pass-{pass_number}.log")
    return work / "source.pdf"


def build_reader(root, output, xelatex):
    import fitz

    if find_spec("fontTools") is None:
        raise ModuleNotFoundError("fontTools is not installed")
    volume = json.loads((root / "volume.json").read_text(encoding="utf-8"))
    assembler = root / "assemble_reader.py"
    mapper = root / "pdf_text_mapping.py"
    for companion in (assembler, mapper):
        if not companion.is_file():
            raise FileNotFoundError(companion)
    for part in volume["parts"]:
        entry = root / "parts" / part["id"] / part["main"]
        if not entry.is_file():
            raise FileNotFoundError(entry)

    output.parent.mkdir(parents=True, exist_ok=True)
    work = Path(mkdtemp(prefix="viii-components-", dir=output.parent))
    continuous = volume.get("continuous_folios", False)
    next_page = 1
    component_pdfs = []
    for part in volume["parts"]:
        identifier = part["id"]
        print(f"XeLaTeX: {identifier}", flush=True)
        component_pdf = compile_component(
            xelatex, root / "parts" / identifier, work / identifier,
            part["main"], next_page if continuous else None,
        )
        component_pdfs.append(str(component_pdf))
        with fitz.open(component_pdf) as document:
            next_page += len(document)

    inputs = work / "reader_inputs.json"
    inputs.write_text(json.dumps(component_pdfs), encoding="utf-8")
    unmapped = work / "reader-unmapped.pdf"
    mapped = work / "reader.pdf"
    run_logged(
        [sys.executable, str(assembler), "--inputs", str(inputs), "--output", str(unmapped)],
        root, work / "assemble_reader.log",
    )
    run_logged(
        [sys.executable, str(mapper), str(unmapped), str(mapped)],
        root, work / "pdf_text_mapping.log",
    )

    expected = {f"native-{leaf}" for leaf in volume["native_anchors"]}
    with fitz.open(mapped) as document:
        anchors = {name for name in document.resolve_names() if name.startswith("native-")}
    if anchors != expected:
        raise RuntimeError(f"Native destinations differ from volume.json. See {work / 'assemble_reader.log'}")
    mapped.replace(output)
    print(f"Reader: {output}")
    print(f"Component PDFs and logs: {work}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=Path(__file__).resolve().parent,
                        help="directory containing volume.json (default: this script's directory)")
    parser.add_argument("--output", type=Path, default=Path("build/Gauss_Werke_VIII.pdf"),
                        help="reader PDF path, relative to the source root unless absolute")
    parser.add_argument("--xelatex", default="xelatex", help="XeLaTeX executable name or path")
    args = parser.parse_args()

    xelatex = shutil.which(args.xelatex)
    if xelatex is None:
        parser.error(f"XeLaTeX executable not found: {args.xelatex}")
    root = args.source_root.resolve()
    output = root / args.output
    try:
        # TeX Live may select the LaTeX format from the xelatex symlink name.
        build_reader(root, output, str(Path(xelatex).absolute()))
    except ImportError as error:
        print(f"{error}. Install PyMuPDF and fontTools with python -m pip install PyMuPDF fonttools.", file=sys.stderr)
        return 1
    except (OSError, RuntimeError) as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
