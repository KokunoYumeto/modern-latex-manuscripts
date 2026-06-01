# Spark prompt: split a large TeX source into translation batches

You are preparing a large TeX source file for Ukrainian translation.

Input: one large `.tex` file.
Output:

1. A CSV manifest with columns:
   `batch_id,source_file,start_anchor,end_anchor,section_title,priority,notes`
2. One Markdown task card per batch.
3. Do not translate yet.

Batching rules:

- Split at `\section`, `\subsection`, or strong comment separators.
- Keep equations with the prose that introduces them.
- Keep theorem/proof pairs together when possible.
- Keep table/caption/label together.
- Mark risky batches: dense formula derivation, custom macros, long tables, algorithm blocks.
- Target 800-2500 lines per batch unless logical structure forces otherwise.
