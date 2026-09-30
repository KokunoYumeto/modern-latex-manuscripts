"""One capped serialization; PDF imports follow memory reservation."""
from pathlib import Path
import json, sys
from bounded_static_memory import reserve, observed

if __name__ == '__main__':
    job = reserve(402653184)
    from canonicalize_bilevel_padding import canonicalize
    import fitz
    if len(sys.argv) not in (2, 3):
        raise ValueError('Usage: pdf_postprocess.py input.pdf [new-output.pdf]')
    result = canonicalize(Path(sys.argv[1]), Path(sys.argv[2]) if len(sys.argv) == 3 else None)
    result['pymupdf_version'] = fitz.VersionBind
    result['memory_policy'] = observed(job)
    print(json.dumps(result))
