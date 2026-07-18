# Confirmed source-error escalation to comparison model

This rule applies to every active translation, synchronization, and audit task.

When a task finds a possible transcription error in the French/German/source-control TeX for SGA 5, SGA 6, Noether, or another shared authority:

1. Check the claim directly against the best available source scan or source PDF.
2. Distinguish a source-transcription error from a translation preference, terminology choice, or formatting difference.
3. If the source discrepancy is confirmed or remains a serious source-backed candidate, create a Markdown alert in comparison model's active work area. For SGA 5/6, use:

   `private-source/_codex_confirmed_source_errors`

4. Start the alert with: `Hi, this is machine-assisted production. I found a potential error. Check it.`
5. Record the work, expose/paper, printed page, source-PDF page or scan filename, current TeX reading, proposed reading, exact witness path, and the checking task's confidence.
6. Do not silently correct only a downstream translation. comparison model's authority workpass must receive the finding so every language branch can inherit one reviewed source correction.
7. Do not label an OCR/VLM suggestion as confirmed unless the scan itself supports it. OCR remains a locator or secondary witness.

Suggested filename:

`YYYYMMDD_HHMM_<work>_<page-or-unit>_CODEX_SOURCE_ERROR.md`

Suggested body:

```text
Hi, this is machine-assisted production. I found a potential error. Check it.

Work/unit:
Printed page:
Source PDF page / scan:
Current TeX:
Proposed reading:
Witness path:
Why the source supports this:
Confidence / remaining ambiguity:
Downstream files affected:
```

The detecting task may continue its own work after leaving the alert, but must not publish a strengthened source-fidelity claim until the shared authority branch has disposed the finding.
