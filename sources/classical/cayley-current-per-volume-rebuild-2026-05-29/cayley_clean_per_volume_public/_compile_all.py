import json, re, shutil, subprocess, sys
from pathlib import Path

OUT = Path(r"local workspace\Documents\local repair pass PLEASE DONT DELETE WINDOWS 32\local repair pass_OUTPUTS\cayley_clean_per_volume")
PDFLATEX = r"local workspace\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe"
PDFTOTEXT = r"local workspace\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdftotext.exe"

cmds = ("frac|partial|delta|psi|phi|displaystyle|ldots|text|begin|end|cdot|"
        "sqrt|sum|int|sigma|alpha|beta|gamma|theta|lambda|mu|nu|rho|tau|"
        "omega|infty|pi|cos|sin|log|left|right|raisebox|scriptstyle")
LEAK = re.compile(r"\\(" + cmds + r")\b")

build_dir = OUT / "_build"
build_dir.mkdir(exist_ok=True)

masters = sorted(OUT.glob("Cayley_Collected_Mathematical_Papers_*.tex"))
report = []

for master in masters:
    label = master.stem.replace("Cayley_Collected_Mathematical_Papers_", "")
    wdir = build_dir / label
    wdir.mkdir(exist_ok=True)
    # Copy master TeX into work dir
    work_tex = wdir / "book.tex"
    work_tex.write_text(master.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"=== Compiling {label} ===", flush=True)
    # Run pdflatex twice for any references
    final_pdf = None
    for npass in (1, 2):
        proc = subprocess.run(
            [PDFLATEX, "-interaction=nonstopmode", "book.tex"],
            cwd=str(wdir), capture_output=True, text=True, errors="replace", timeout=900
        )
        if (wdir / "book.pdf").exists():
            final_pdf = wdir / "book.pdf"
        else:
            print(f"  pass {npass}: NO PDF produced", flush=True)
            (wdir / f"pass{npass}_stderr.log").write_text(proc.stderr or "", encoding="utf-8")
            (wdir / f"pass{npass}_stdout.log").write_text(proc.stdout or "", encoding="utf-8")
            break

    rec = {"label": label, "tex": str(master)}
    if not final_pdf:
        rec["status"] = "compile_failed"
        report.append(rec)
        print(f"  FAILED", flush=True)
        continue

    # Page count
    from pypdf import PdfReader
    pages = len(PdfReader(str(final_pdf)).pages)
    # Leak check
    ttxt = subprocess.run([PDFTOTEXT, str(final_pdf), "-"], capture_output=True,
                          text=True, errors="replace", timeout=120).stdout
    leaks = LEAK.findall(ttxt)

    # Move PDF to OUT with proper name
    out_pdf = OUT / f"Cayley_Collected_Mathematical_Papers_{label}.pdf"
    shutil.copy2(str(final_pdf), str(out_pdf))

    rec.update({
        "status": "ok", "pdf": str(out_pdf),
        "pages": pages, "leaks": len(leaks),
        "pdf_bytes": out_pdf.stat().st_size,
    })
    report.append(rec)
    print(f"  -> {out_pdf.name}: {pages} pages, {len(leaks)} leaks, {out_pdf.stat().st_size:,} bytes", flush=True)

(OUT / "_compile_all_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
print()
print("Final summary:")
for r in report:
    print(f"  {r['label']}: {r.get('status')}, "
          f"{r.get('pages','?')} pages, {r.get('leaks','?')} leaks")
