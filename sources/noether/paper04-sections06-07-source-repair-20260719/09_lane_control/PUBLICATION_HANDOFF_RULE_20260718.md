# Publication handoff rule

The public archive task owns publication to the public GitHub repository and Zenodo records.

Production and language-management tasks must not create competing Zenodo drafts, publication staging records, or claims that material has been uploaded. Continue the substantive work locally. When a bounded payload is genuinely ready, write a handoff note in the lane's `00_lane_control` directory and notify the archive maintainer with:

- exact absolute payload path;
- exact scope and continuation cursor;
- public authority level and explicit caveats;
- PDF page count and editable-source count;
- build, render, source-check, and independent-review evidence actually completed;
- SHA-256 values for every proposed public file;
- names of public files that the payload supersedes.

Do not call a work complete, critical, certified, source-faithful, or diagram-checked unless the evidence proves that exact claim. OCR, VLM, and CUDA extraction remain witness or locator material unless a source-audited body is present.

The archive maintainer will package, validate, publish to the existing concept DOI, set the reader-facing preview, mirror the exact release to GitHub, update public status pages, and log the publication. A valid handoff should be published promptly rather than left in a local staging area.

Working files remain in their production lanes. Do not delete or relocate them as part of a handoff.
