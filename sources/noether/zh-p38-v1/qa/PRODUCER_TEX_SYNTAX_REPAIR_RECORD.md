# Paper 38 producer TeX syntax repair record

This records a compiler-blocking TeX transport repair only. It is not translation, formula, source, or visual checking.

- Initial segment-A SHA-256: `77896C3A3F14796C01018EC70AC4EC029A7FED0AA74AC01BA5FB079B98359D6E`.
- Initial assembled Hans SHA-256: `7C4EB3C042FF63E5E218ED0FDFF495EC6EDFFBD6DD1E708222236671BD25839D`.
- First XeLaTeX pass exit: `1`; second pass not run.
- Compiler error: `Command \end{equation*} invalid in math mode`, reported at assembled line 38.
- Cause: the source title's TeX line break `\\[0.5em]` had been transported as display-math opener `\[0.5em]` in segment A.
- Mechanical repair: changed only `\textbf{代数理论中一个主定理的证明}\[0.5em]` to `\textbf{代数理论中一个主定理的证明}\\[0.5em]`.
- Repaired segment-A SHA-256: `1589D1E80F84D2E2C1E117D0506A3F76730483DCDF7904C3C07356FE2A9E1F06`.
- Reassembled Hans SHA-256: `330053BA55A857F1BA7CE43D6D8F97DE97EC3B1E350D59C21FD2F74702E8E973`.
- No Chinese wording, formula content, source byte, citation, label, or other segment was changed.

Independent checking remains absent.
