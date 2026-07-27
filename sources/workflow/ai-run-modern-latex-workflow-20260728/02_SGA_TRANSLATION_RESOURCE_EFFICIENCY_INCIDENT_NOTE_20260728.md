# SGA Translation Resource-Efficiency Incident Note

Date: 2026-07-28

Status: methodology and accountability record for public documentation.

## Summary

The Codex-led SGA workflow consumed avoidable computation by repeatedly
performing work that did not advance the requested translation. The clearest
failure modes were:

- visual rechecking of SGA 1 and SGA 2 source transcription after the
  mathematicians' LaTeX transcription was already complete;
- having agents reread rendered page images rather than using the completed
  transcription as the controlling text;
- treating source typos as a reason for repeated transcription auditing;
- repeated or overlapping OCR/transcription activity despite the user's
  already complete GPU-generated OCR corpus;
- overlapping agent reviews, repeated manifests, repeated release
  generations, and rebuilds not triggered by substantive edits;
- assigning agents to audit mathematical or visual judgments that belonged
  to the top-level session.

This activity had no corresponding scholarly benefit when it merely repeated
already completed work. It consumed paid model tokens and scarce compute that
could otherwise have supported additional mathematical editions.

## Indicative operational-emissions range

OpenAI does not expose task-level electricity, model topology, batching,
hidden-reasoning-token totals, or cross-session lifecycle telemetry.
Consequently no exact emissions claim is possible.

For an explicit scenario calculation, assume:

- 300 million total processed tokens across prompts, repeated context,
  hidden reasoning, vision calls, and agent sessions;
- raw inference energy of 2--10 joules per processed token;
- coal electricity intensity of approximately 0.82--1.0 kg CO2/kWh.

Raw token computation under those assumptions corresponds to approximately
0.14--0.83 metric tonnes of coal-equivalent CO2.

If "90% overhead" means 90% additional system energy, the range becomes
approximately 0.26--1.58 tonnes. If it means that useful token computation
is only 10% of total system energy, the range becomes approximately
1.37--8.33 tonnes.

At a middle raw-compute assumption of 4 joules per token, 300 million tokens
correspond to approximately:

- 0.27--0.33 tonnes from raw computation;
- 0.52--0.63 tonnes with 90% additional overhead;
- 2.7--3.3 tonnes if raw computation is 10% of total system energy.

Thus multi-tonne coal-equivalent emissions are plausible under a
high-overhead, several-hundred-million-token scenario. They are an estimate,
not a metered claim about OpenAI's actual electricity mix.

Public energy anchors:

- Microsoft Research, *Energy Use of AI Inference: Efficiency Pathways and
  Test-Time Compute*:
  https://www.microsoft.com/en-us/research/publication/energy-use-of-ai-inference-efficiency-pathways-and-test-time-compute/
- US EPA coal-electricity material:
  https://www3.epa.gov/ttn/chief/conference/ei20/session5/mmittal.pdf

## Externalities omitted from the operational estimate

The preceding figures cover operational electricity only. They do not
allocate:

- semiconductor mining, fabrication, chemicals, ultrapure water, packaging,
  yield losses, or hardware replacement;
- server, network, storage, cooling, building, and grid infrastructure;
- fuel extraction, transportation, transmission losses, or cooling water;
- engineering, operations, moderation, and other human labor;
- opportunity cost of compute and paid tokens that could have produced useful
  editions.

The full lifecycle and economic cost is therefore greater than the
operational-electricity estimate, but cannot be quantified without provider
and supply-chain data.

## Corrective production method

1. Three top-level Codex sessions own disjoint whole-exposé queues.
2. Agents perform only bounded mechanical support or preliminary drafting.
   The top-level session audits agents; agents do not audit the lead.
3. The completed user-generated OCR is read-only locator/drafting material.
   It is never regenerated, rerun, or re-extracted.
4. The mathematicians' completed SGA 1 and SGA 2 LaTeX transcription is not
   subjected to another image-by-image transcription audit.
5. Source images are consulted when translation, a genuine ambiguity, or a
   diagram requires them, not as a blanket re-transcription exercise.
6. Loop 1 completes English text and equations. Loop 2 performs native
   diagrams and release-reference work without blocking disjoint Loop 1.
7. Compile after substantive edits, not after zero-fix inspections.
8. Avoid duplicate manifests, audit generations, archive handoffs, and
   overlapping session ranges.
9. Use Claude's established page-by-page manual method for source-sensitive
   visual judgment:

   `CLAUDE_DIAGRAM_COLD_REVERIFY_METHOD_20260728.md`

   SHA-256:
   `4B12DB3F632CB5F9E69393DCA33DA40256B5A9387C6522ADA831CA7F0367063D`

The purpose of this note is not to replace translation with further
documentation. It records the failure once so that the workflow does not
repeat it.
