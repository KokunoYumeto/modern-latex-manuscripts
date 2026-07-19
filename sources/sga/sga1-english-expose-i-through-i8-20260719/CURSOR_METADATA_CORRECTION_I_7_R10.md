# Cursor-metadata correction and revision history for checkpoint r10

The frozen r8 checkpoint was withheld after independent audit found one incorrect prose description in `CONTINUATION_CURSOR.md`. The subsequent r9 freeze attempt then failed closed before promotion because its public machine projection omitted a referenced historical locator record. Neither revision was handed to archive maintenance.

The numerical source boundary has remained correct throughout: French authority lines 1217--1492 are included, and line 1493 is the first excluded line. French authority lines 1493--1495, a 162-byte LF-normalized slice with SHA-256 `4422B54F8D37E0E051778F6FABDA6B70B5ADBB0AA3CE376DD1B90868A6C50A57`, give the next heading as:

> Infinitesimal lifting of étale schemes. Application to formal schemes.

Revision r10 retains that corrected descriptor and restores machine-reference closure. It does not change the translated TeX, the audited I.7 source slice, any formula or structure decision, the cumulative PDF, the 13 rendered pages, or the line-1493 continuation cursor. Revisions r8 and r9 remain preserved as nonpublic history and must not be substituted for r10.

Status: corrected metadata successor, still a bounded opening-through-I.7 working translation. It is not complete SGA 1, a critical edition, peer review, mathematical certification, independent human review, or a rights determination.
