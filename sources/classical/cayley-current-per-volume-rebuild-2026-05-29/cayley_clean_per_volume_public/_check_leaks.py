import sys, re
from collections import Counter

text = sys.stdin.read()
cmds = "frac|partial|delta|psi|phi|displaystyle|ldots|text|begin|end|cdot|sqrt|sum|int|sigma|alpha|beta|gamma|theta|lambda|mu|nu|rho|tau|omega|infty|pi|cos|sin|log|left|right"
pat = r"\\(" + cmds + r")\b"
leaks = re.findall(pat, text)
print(f"True backslash-command leaks: {len(leaks)}")
print(f"By type: {Counter(leaks).most_common(15)}")

# Also check for raw dollar-sign math that didn't render
dollar = re.findall(r"\$[^$\n]{3,80}\$", text)
print(f"Visible \\$...\\$ blocks (unrendered math?): {len(dollar)}")
if dollar:
    print(f"Sample dollar: {dollar[:3]}")
