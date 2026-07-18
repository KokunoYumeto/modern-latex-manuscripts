# Structural index schema

Each nonblank line of `STRUCTURAL_INDEX.jsonl` is one UTF-8 JSON object. Required fields are `record_id`, `revision`, `status`, `kind`, `r823_lines`, `printed_pages`, `physical_pages`, `parent_id`, `children`, `formula_labels`, `target_markers`, and `disposition`. IDs are stable. Revisions are append-only positive integers; a later revision must name the preceding revision in `supersedes_record_revision`. The active child ranges must partition R823 lines 4045--4110 exactly once.
