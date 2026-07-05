import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_INTAKE_LEDGER_TEMPLATE_20260703T054500Z';
const noteId = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_INTAKE_LEDGER_TEMPLATE_NOTE_20260703T054600Z';
const generatedUtc = '2026-07-03T05:45:00Z';
const noteGeneratedUtc = '2026-07-03T05:46:00Z';
const packageOrder = 142;
const queueCandidateId = 'OTCQ-OLP-DMOI-RELATION-FUNCTION-SELECTED-EXCERPT-ATTRIBUTION-NOTICE-TEMPLATE-REVIEW-RETURN-EVIDENCE-INTAKE-LEDGER-TEMPLATE-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentCriteriaRubric = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_RUBRIC_20260703T053000Z';
const parentArtifacts = [
  parentCriteriaRubric,
  'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_LEDGER_TEMPLATE_20260703T051500Z',
  'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_PACKET_20260703T050000Z'
];

const blankEvidenceFields = [
  'evidence_value',
  'evidence_source_pointer',
  'evidence_reviewer_role',
  'evidence_capture_date',
  'evidence_scope_note',
  'source_text_absence_confirmation',
  'downstream_gate_limit_confirmation',
  'evidence_intake_note'
];

function parseJson(text) {
  return JSON.parse(text.charCodeAt(0) === 0xFEFF ? text.slice(1) : text);
}

async function readJson(stem) {
  const text = await readFile(path.join(outputs, `${stem}.json`), 'utf8');
  return { text, obj: parseJson(text) };
}

function sha256(data) {
  return crypto.createHash('sha256').update(data).digest('hex');
}

function sha256Upper(data) {
  return sha256(data).toUpperCase();
}

async function writeShaForJson(stem) {
  const filename = `${stem}.json`;
  const data = await readFile(path.join(outputs, filename));
  await writeFile(path.join(outputs, `${stem}.sha256`), `${sha256(data)}  ${filename}\n`, 'utf8');
}

async function writeJson(stem, obj) {
  await writeFile(path.join(outputs, `${stem}.json`), `${JSON.stringify(obj, null, 2)}\n`, 'utf8');
  await writeShaForJson(stem);
}

function ensureArray(obj, key) {
  if (!Array.isArray(obj[key])) obj[key] = [];
  return obj[key];
}

function addUnique(array, value) {
  if (!array.includes(value)) array.push(value);
}

function upsertById(array, keys, id, row) {
  const index = array.findIndex((candidate) => keys.some((key) => candidate?.[key] === id));
  if (index >= 0) array[index] = { ...array[index], ...row };
  else array.push(row);
}

function csvCell(value) {
  if (value === undefined || value === null) return '';
  const text = Array.isArray(value) ? value.join('; ') : typeof value === 'object' ? JSON.stringify(value) : String(value);
  return /[",\n]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
}

async function appendMdIfMissing(filename, marker, text) {
  const file = path.join(outputs, filename);
  let current = '';
  try {
    current = await readFile(file, 'utf8');
  } catch {
    current = '';
  }
  if (!current.includes(marker)) {
    const separator = current.endsWith('\n') || current.length === 0 ? '' : '\n';
    await writeFile(file, `${current}${separator}${text}\n`, 'utf8');
  }
}

async function countJsonFilesRecursive(dir) {
  let count = 0;
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) count += await countJsonFilesRecursive(full);
    else if (entry.name.endsWith('.json')) count += 1;
  }
  return count;
}

function titleClass(value) {
  return String(value).split('_').map((part) => (part ? `${part[0].toUpperCase()}${part.slice(1)}` : part)).join(' ');
}

function formatNumber(value) {
  return new Intl.NumberFormat('en-US').format(value);
}

function buildEvidenceRows(parent) {
  return parent.review_return_evidence_criteria_rows.map((row, index) => ({
    review_return_evidence_intake_row_id: `ODRF-SEL-EXC-ATTR-RRET-EVID-${String(index + 1).padStart(3, '0')}`,
    parent_review_return_evidence_criterion_row_id: row.review_return_evidence_criterion_row_id,
    parent_review_return_ledger_row_id: row.parent_review_return_ledger_row_id,
    parent_review_packet_row_id: row.parent_review_packet_row_id,
    parent_notice_template_row_id: row.parent_notice_template_row_id,
    parent_source_text_capture_policy_return_row_id: row.parent_source_text_capture_policy_return_row_id,
    parent_packet_unit: row.parent_packet_unit,
    criterion_type: row.criterion_type,
    criterion_label: row.criterion_label,
    required_evidence: row.required_evidence,
    inherited_criterion_unfilled: row.criterion_unfilled,
    inherited_criterion_passed: row.criterion_passed,
    inherited_criterion_failed: row.criterion_failed,
    blank_evidence_fields: blankEvidenceFields,
    evidence_value: null,
    evidence_source_pointer: null,
    evidence_reviewer_role: null,
    evidence_capture_date: null,
    evidence_scope_note: null,
    source_text_absence_confirmation: null,
    downstream_gate_limit_confirmation: null,
    evidence_intake_note: null,
    evidence_fields_filled: 0,
    evidence_value_filled: false,
    evidence_source_pointer_filled: false,
    evidence_row_ready_for_review: false,
    review_return_received: false,
    criterion_decision_allowed_after_intake: false,
    notice_template_approval_allowed_after_intake: false,
    source_text_or_excerpt_allowed_after_intake: false,
    surface_gate_opened: false,
    translation_gate_opened: false
  }));
}

function buildCriterionClassEvidenceSummaryRows(parent, evidenceRows) {
  return parent.review_return_evidence_criterion_class_summary_rows.map((row, index) => {
    const linked = evidenceRows.filter((evidence) => evidence.criterion_type === row.criterion_type);
    return {
      review_return_evidence_intake_criterion_class_summary_row_id: `ODRF-SEL-EXC-ATTR-RRET-EVID-CLASS-${String(index + 1).padStart(2, '0')}`,
      parent_criterion_class_summary_row_id: row.review_return_evidence_criterion_class_summary_row_id,
      criterion_type: row.criterion_type,
      criterion_label: row.criterion_label,
      evidence_intake_rows_required: linked.length,
      evidence_intake_rows_filled: 0,
      evidence_values_filled: 0,
      evidence_source_pointers_filled: 0,
      criteria_passed: 0,
      criteria_failed: 0,
      linked_evidence_intake_row_ids: linked.map((evidence) => evidence.review_return_evidence_intake_row_id)
    };
  });
}

function buildPacketUnitEvidenceSummaryRows(parent, evidenceRows) {
  return parent.packet_unit_review_return_evidence_criterion_summary_rows.map((row, index) => {
    const linked = evidenceRows.filter((evidence) => evidence.parent_review_return_ledger_row_id === row.parent_review_return_ledger_row_id);
    return {
      review_return_evidence_intake_packet_summary_row_id: `ODRF-SEL-EXC-ATTR-RRET-EVID-PACKET-${String(index + 1).padStart(2, '0')}`,
      parent_packet_unit: row.parent_packet_unit,
      parent_review_return_ledger_row_id: row.parent_review_return_ledger_row_id,
      evidence_intake_rows_required: linked.length,
      evidence_intake_rows_filled: 0,
      evidence_values_filled: 0,
      evidence_source_pointers_filled: 0,
      review_return_received: false,
      notice_template_approved_for_fill: false,
      source_text_or_excerpt_allowed: false,
      linked_evidence_intake_row_ids: linked.map((evidence) => evidence.review_return_evidence_intake_row_id)
    };
  });
}

function buildArtifact(parent) {
  const evidenceRows = buildEvidenceRows(parent);
  const criterionClassRows = buildCriterionClassEvidenceSummaryRows(parent, evidenceRows);
  const packetSummaryRows = buildPacketUnitEvidenceSummaryRows(parent, evidenceRows);
  const blankEvidenceCells = evidenceRows.length * blankEvidenceFields.length;
  const parentGate = parent.gate_state || {};
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_intake_ledger_template_blank_no_evidence_no_returns_no_approvals_no_excerpts_no_source_text_no_notice_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Allocate blank evidence-intake rows for each package-141 review-return evidence criterion, without filling evidence, receiving returns, approving notice fills, selecting excerpts, copying source text, opening surfaces, or drafting translations.',
    parent_artifacts: parentArtifacts,
    evidence_intake_boundary: {
      ledger_template_is: 'blank evidence-intake ledger for future review-return evidence criteria',
      ledger_template_is_not: [
        'review return',
        'evidence value',
        'evidence review',
        'criteria decision ledger',
        'approval to fill notices',
        'source-text capture permission',
        'selected excerpt',
        'exact line span',
        'filled attribution notice',
        'surface proposal',
        'translation draft',
        'pilot or publication claim'
      ],
      allowed_now: [
        'allocate one evidence-intake row per criterion row',
        'make future evidence fields explicit',
        'keep all evidence, source, notice, surface, and translation fields empty'
      ],
      blocked_now: [
        'inventing review returns or evidence',
        'reviewing or deciding criteria',
        'approving notice templates for fill',
        'copying source text or excerpts',
        'opening surface, translation, pilot, or publication gates'
      ]
    },
    blank_evidence_fields: blankEvidenceFields,
    review_return_evidence_intake_rows: evidenceRows,
    criterion_class_review_return_evidence_intake_summary_rows: criterionClassRows,
    packet_unit_review_return_evidence_intake_summary_rows: packetSummaryRows,
    gate_state: {
      review_return_evidence_intake_rows: evidenceRows.length,
      criterion_class_review_return_evidence_intake_summary_rows: criterionClassRows.length,
      packet_unit_review_return_evidence_intake_summary_rows: packetSummaryRows.length,
      blank_evidence_fields_per_row: blankEvidenceFields.length,
      blank_evidence_field_cells_allocated: blankEvidenceCells,
      inherited_review_return_evidence_criteria_rows: parentGate.review_return_evidence_criteria_rows,
      inherited_criteria_unfilled: parentGate.criteria_unfilled,
      inherited_review_returns_received: parentGate.review_returns_received,
      evidence_fields_filled: 0,
      evidence_values_filled: 0,
      evidence_source_pointers_filled: 0,
      evidence_rows_ready_for_review: 0,
      evidence_rows_reviewed: 0,
      criteria_rows_filled: 0,
      criteria_passed: 0,
      criteria_failed: 0,
      criteria_unfilled: evidenceRows.length,
      review_returns_received: 0,
      review_returns_ingested: 0,
      review_rows_passed: 0,
      review_rows_failed: 0,
      notice_template_rows_approved_for_fill: 0,
      notice_template_rows_filled: 0,
      notice_fields_filled: 0,
      selected_excerpt_attribution_notices_filled: 0,
      selected_excerpt_attribution_notice_files_created: 0,
      source_text_or_excerpt_files_created: 0,
      source_text_capture_policy_returns_received: 0,
      source_text_capture_policies_finalized: 0,
      source_locator_permissions_granted: 0,
      line_span_selection_permissions_granted: 0,
      source_text_capture_permissions_granted: 0,
      excerpt_permissions_granted: 0,
      exact_line_spans_selected: 0,
      candidate_line_ranges_selected: 0,
      source_locator_rows_selected: 0,
      source_prose_copied: 0,
      source_examples_copied: 0,
      source_passages_selected: 0,
      source_text_copied: 0,
      excerpts_selected: 0,
      reviewer_scope_returns_received: 0,
      owner_or_reviewer_acceptances_recorded: 0,
      local_language_surfaces_filled: 0,
      bridge_surfaces_accepted: 0,
      semi_constructed_surfaces_accepted: 0,
      translated_passages: 0,
      publication_ready: false,
      translation_ready: false,
      constructed_surface_ready: false,
      pilot_ready: false
    },
    validation_snapshot: {
      validator: 'local_node_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_intake_ledger_template_generation_prevalidation_20260703T054500Z',
      zero_gate_assertions: [
        'evidence_fields_filled',
        'evidence_values_filled',
        'evidence_source_pointers_filled',
        'evidence_rows_ready_for_review',
        'evidence_rows_reviewed',
        'criteria_rows_filled',
        'criteria_passed',
        'criteria_failed',
        'review_returns_received',
        'review_returns_ingested',
        'review_rows_passed',
        'review_rows_failed',
        'notice_template_rows_approved_for_fill',
        'notice_template_rows_filled',
        'notice_fields_filled',
        'selected_excerpt_attribution_notices_filled',
        'selected_excerpt_attribution_notice_files_created',
        'source_text_or_excerpt_files_created',
        'source_text_capture_policy_returns_received',
        'source_text_capture_policies_finalized',
        'source_locator_permissions_granted',
        'line_span_selection_permissions_granted',
        'source_text_capture_permissions_granted',
        'excerpt_permissions_granted',
        'exact_line_spans_selected',
        'candidate_line_ranges_selected',
        'source_locator_rows_selected',
        'source_prose_copied',
        'source_examples_copied',
        'source_passages_selected',
        'source_text_copied',
        'excerpts_selected',
        'reviewer_scope_returns_received',
        'owner_or_reviewer_acceptances_recorded',
        'local_language_surfaces_filled',
        'bridge_surfaces_accepted',
        'semi_constructed_surfaces_accepted',
        'translated_passages'
      ],
      review_return_evidence_intake_rows: evidenceRows.length,
      criterion_class_review_return_evidence_intake_summary_rows: criterionClassRows.length,
      packet_unit_review_return_evidence_intake_summary_rows: packetSummaryRows.length,
      blank_evidence_fields_per_row: blankEvidenceFields.length,
      blank_evidence_field_cells_allocated: blankEvidenceCells
    },
    next_valid_artifacts: [
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_DECISION_LEDGER_TEMPLATE_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_INTAKE_LEDGER_WITH_VALUES_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_LEDGER_WITH_RETURNS_<timestamp>'
    ],
    decision: 'Package 142 creates a blank evidence-intake ledger for package 141 criteria. It allocates intake slots only and preserves zero returns, zero evidence, zero criteria decisions, zero approvals, zero exact spans, zero source text, zero excerpts, zero notices, zero surfaces, zero translations, and zero readiness.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const classRows = artifact.criterion_class_review_return_evidence_intake_summary_rows.map((row) => `| ${row.review_return_evidence_intake_criterion_class_summary_row_id} | ${row.criterion_type} | ${row.evidence_intake_rows_required} | ${row.evidence_intake_rows_filled} |`).join('\n');
  const packetRows = artifact.packet_unit_review_return_evidence_intake_summary_rows.map((row) => `| ${row.review_return_evidence_intake_packet_summary_row_id} | ${row.parent_packet_unit} | ${row.parent_review_return_ledger_row_id} | ${row.evidence_intake_rows_required} | ${row.evidence_intake_rows_filled} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: ${artifact.status}

## Purpose

${artifact.purpose}

## Boundary

This is a blank evidence-intake ledger template. It is not a review return, evidence value, evidence review, criteria decision, approval, selected excerpt, exact line span, source text, filled attribution notice, source-text/excerpt sidecar, surface, translation, pilot, publication, commit, push, PR update, or Zenodo action.

## Counts

- Evidence-intake rows: \`${g.review_return_evidence_intake_rows}\`
- Criterion-class summaries: \`${g.criterion_class_review_return_evidence_intake_summary_rows}\`
- Packet-unit summaries: \`${g.packet_unit_review_return_evidence_intake_summary_rows}\`
- Blank evidence fields per row: \`${g.blank_evidence_fields_per_row}\`
- Blank evidence-field cells allocated: \`${g.blank_evidence_field_cells_allocated}\`
- Evidence fields/values/pointers/reviewed: \`${g.evidence_fields_filled}/${g.evidence_values_filled}/${g.evidence_source_pointers_filled}/${g.evidence_rows_reviewed}\`
- Criteria filled/pass/fail/unfilled: \`${g.criteria_rows_filled}/${g.criteria_passed}/${g.criteria_failed}/${g.criteria_unfilled}\`
- Review returns/approvals: \`${g.review_returns_received}/${g.notice_template_rows_approved_for_fill}\`
- Exact spans/source text/excerpts/notices/files: \`${g.exact_line_spans_selected}/${g.source_text_copied}/${g.excerpts_selected}/${g.selected_excerpt_attribution_notices_filled}/${g.source_text_or_excerpt_files_created}\`
- Surfaces/translations/readiness: \`${g.local_language_surfaces_filled}/${g.translated_passages}/${g.pilot_ready}\`

## Criterion Class Summary

| Row | Criterion type | Evidence rows required | Evidence rows filled |
| --- | --- | ---: | ---: |
${classRows}

## Packet Unit Summary

| Row | Packet unit | Parent return row | Evidence rows required | Evidence rows filled |
| --- | --- | --- | ---: | ---: |
${packetRows}

## Decision

${artifact.decision}
`;
}

function buildArtifactCsv(artifact) {
  const rows = [];
  rows.push(['section', 'row_id', 'packet_or_criterion', 'parent_id', 'required_or_blank_count', 'filled_count', 'gate_open'].map(csvCell).join(','));
  for (const row of artifact.review_return_evidence_intake_rows) {
    rows.push([
      'review_return_evidence_intake',
      row.review_return_evidence_intake_row_id,
      row.criterion_type,
      row.parent_review_return_evidence_criterion_row_id,
      row.blank_evidence_fields.length,
      row.evidence_fields_filled,
      row.surface_gate_opened || row.translation_gate_opened
    ].map(csvCell).join(','));
  }
  for (const row of artifact.criterion_class_review_return_evidence_intake_summary_rows) {
    rows.push([
      'criterion_class_summary',
      row.review_return_evidence_intake_criterion_class_summary_row_id,
      row.criterion_type,
      row.parent_criterion_class_summary_row_id,
      row.evidence_intake_rows_required,
      row.evidence_intake_rows_filled,
      false
    ].map(csvCell).join(','));
  }
  for (const row of artifact.packet_unit_review_return_evidence_intake_summary_rows) {
    rows.push([
      'packet_unit_summary',
      row.review_return_evidence_intake_packet_summary_row_id,
      row.parent_packet_unit,
      row.parent_review_return_ledger_row_id,
      row.evidence_intake_rows_required,
      row.evidence_intake_rows_filled,
      row.source_text_or_excerpt_allowed
    ].map(csvCell).join(','));
  }
  return `${rows.join('\n')}\n`;
}

function buildNote(artifact) {
  const g = artifact.gate_state;
  return {
    artifact_id: noteId,
    generated_utc: noteGeneratedUtc,
    source_artifact: artifact.artifact_id,
    package_order: packageOrder,
    status: 'pointer_only_selected_excerpt_attribution_notice_template_review_return_evidence_intake_ledger_template_note_no_upload_claim_no_remote_state_claim',
    purpose: 'Record package-142 OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence-intake continuation while preserving no-review-return/no-evidence/no-approval/no-excerpt/no-source-text/no-notice/no-translation boundaries.',
    points_to_artifacts: [
      `${artifactId}.json`,
      `${artifactId}.md`,
      `${artifactId}.csv`,
      `${artifactId}.sha256`
    ],
    summary: {
      review_return_evidence_intake_rows: g.review_return_evidence_intake_rows,
      criterion_class_summary_rows: g.criterion_class_review_return_evidence_intake_summary_rows,
      packet_unit_summary_rows: g.packet_unit_review_return_evidence_intake_summary_rows,
      blank_evidence_field_cells_allocated: g.blank_evidence_field_cells_allocated,
      evidence_fields_filled: g.evidence_fields_filled,
      evidence_values_filled: g.evidence_values_filled,
      evidence_source_pointers_filled: g.evidence_source_pointers_filled,
      criteria_rows_filled: g.criteria_rows_filled,
      criteria_unfilled: g.criteria_unfilled,
      review_returns_received: g.review_returns_received,
      notice_template_rows_approved_for_fill: g.notice_template_rows_approved_for_fill,
      source_text_or_excerpt_files_created: g.source_text_or_excerpt_files_created,
      exact_line_spans_selected: g.exact_line_spans_selected,
      source_text_copied: g.source_text_copied,
      excerpts_selected: g.excerpts_selected,
      surfaces_or_translations: g.local_language_surfaces_filled + g.bridge_surfaces_accepted + g.semi_constructed_surfaces_accepted + g.translated_passages,
      readiness_claims: Number(g.publication_ready) + Number(g.translation_ready) + Number(g.constructed_surface_ready) + Number(g.pilot_ready)
    },
    boundary: 'Pointer-only coordination note. No review return, evidence, evidence review, criteria decision, approval, exact line span, selected excerpt, source text, attribution notice text, source-text/excerpt sidecar, surface, translation, pilot, publication, commit, push, PR update, or Zenodo action is claimed.',
    upload_intent: 'Queue the package-142 JSON/MD/CSV/checksum and this note for the existing Noether upload path as substantive coordination material; user clarified on 2026-07-03 that substantive artifacts should not be deferred because of mobile-plan or bandwidth wording.',
    message_template: `Package 142 added ${artifactId}: 50 blank review-return evidence-intake rows, 5 criterion-class summaries, 10 packet-unit summaries, 400 blank evidence-field cells, 0 evidence, 0 review returns, 0 criteria decisions, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 attribution notices, 0 source-text/excerpt files, 0 surfaces/translations, 0 readiness.`
  };
}

function buildNoteMd(note) {
  return `# Package 142 Coordination Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${note.source_artifact}\`

Generated UTC: \`${note.generated_utc}\`

## Summary

- Review-return evidence-intake rows: \`${note.summary.review_return_evidence_intake_rows}\`
- Criterion-class summaries: \`${note.summary.criterion_class_summary_rows}\`
- Packet-unit summaries: \`${note.summary.packet_unit_summary_rows}\`
- Blank evidence-field cells allocated: \`${note.summary.blank_evidence_field_cells_allocated}\`
- Evidence fields/values/pointers: \`${note.summary.evidence_fields_filled}/${note.summary.evidence_values_filled}/${note.summary.evidence_source_pointers_filled}\`
- Criteria filled/unfilled: \`${note.summary.criteria_rows_filled}/${note.summary.criteria_unfilled}\`
- Review returns/approvals: \`${note.summary.review_returns_received}/${note.summary.notice_template_rows_approved_for_fill}\`
- Source-text files/exact spans/source text/excerpts: \`${note.summary.source_text_or_excerpt_files_created}/${note.summary.exact_line_spans_selected}/${note.summary.source_text_copied}/${note.summary.excerpts_selected}\`
- Surfaces/translations/readiness claims: \`${note.summary.surfaces_or_translations}/${note.summary.readiness_claims}\`

## Boundary

${note.boundary}

## Upload Intent

${note.upload_intent}

## Message Template

${note.message_template}
`;
}

async function writeArtifactAndNote(artifact, note) {
  await writeFile(path.join(outputs, `${artifactId}.json`), `${JSON.stringify(artifact, null, 2)}\n`, 'utf8');
  await writeFile(path.join(outputs, `${artifactId}.md`), buildArtifactMd(artifact), 'utf8');
  await writeFile(path.join(outputs, `${artifactId}.csv`), buildArtifactCsv(artifact), 'utf8');
  await writeShaForJson(artifactId);

  await writeFile(path.join(outputs, `${noteId}.json`), `${JSON.stringify(note, null, 2)}\n`, 'utf8');
  await writeFile(path.join(outputs, `${noteId}.md`), buildNoteMd(note), 'utf8');
  await writeShaForJson(noteId);
}

async function updateRegistrations(artifact) {
  const g = artifact.gate_state;
  const packageIndex = await readJson(packageIndexFile);
  const order = ensureArray(packageIndex.obj, 'current_package_order');
  if (!order.some((row) => row?.artifact === artifactId)) {
    order.push({
      order: packageOrder,
      role: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_intake_ledger_template_support',
      artifact: artifactId,
      current_use: '50 blank selected-excerpt attribution notice template review-return evidence-intake rows; 8 evidence fields per row; 400 blank evidence-field cells; 5 criterion-class summaries; 10 packet-unit summaries; 0 evidence, 0 criteria decisions, 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 surfaces, 0 translation, 0 readiness'
    });
  }
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_intake_ledger_template = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_intake_rows: g.review_return_evidence_intake_rows,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_intake_blank_cells: g.blank_evidence_field_cells_allocated,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_values: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_pointers: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_source_text_or_excerpt_files: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_criteria_decision_ledger_template_or_with_values_only_no_source_text_no_excerpt_no_surfaces_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence intake ledger template',
    route: artifactId,
    license_status_to_recheck: 'blank_evidence_intake_only_no_returns_no_evidence_no_approvals_no_exact_spans_no_source_text_no_excerpts_no_notices_no_translation',
    best_translation_use: 'future selected-excerpt attribution notice template review-return evidence intake before criteria decision, approval, notice fill, source-text/excerpt sidecar, surface, or translation',
    candidate_lanes: [
      'olp_dmoi_relation_function_attribution_notice_lane',
      'blank_review_return_evidence_intake',
      'review_only_construction_scaffold',
      'source_aware_excerpt_governance'
    ],
    priority: 1,
    status: 'blank_review_return_evidence_intake_ledger_no_returns_no_evidence_no_approvals_no_source_text_no_excerpts_no_translation',
    gate_state: {
      review_return_evidence_intake_rows: g.review_return_evidence_intake_rows,
      blank_evidence_field_cells_allocated: g.blank_evidence_field_cells_allocated,
      evidence_values_filled: 0,
      evidence_source_pointers_filled: 0,
      review_returns_received: 0,
      notice_template_rows_approved_for_fill: 0,
      source_text_or_excerpt_files_created: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_intake_ledger_template: ${artifactId}_50_blank_evidence_rows_400_blank_cells_0_evidence_0_returns_0_approvals_0_source_text_0_excerpts_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_intake_ledger_template_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_intake_ledger_template_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_intake_rows: g.review_return_evidence_intake_rows,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_intake_blank_cells: g.blank_evidence_field_cells_allocated,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_values: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_pointers: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_source_text_or_excerpt_files: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_surfaces: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_translations: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_intake_ledger_template = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_intake_ledger_template: ${artifactId}_blank_evidence_intake_only_no_returns_no_evidence_no_approvals_no_source_text_no_excerpts_no_notices_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_intake_ledger_template = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates 50 blank selected-excerpt attribution notice template review-return evidence-intake rows and 400 blank evidence-field cells after package 141; 0 evidence, 0 criteria decisions, 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, 0 readiness; substantive artifacts should be uploaded when a staging path exists.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence intake ledger template; 50 blank evidence rows, 400 blank cells, 0 evidence, 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 142: OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence intake ledger template after package 141. It records 50 blank evidence-intake rows, 5 criterion-class summaries, 10 packet-unit summaries, and 400 blank evidence-field cells while keeping 0 evidence, 0 criteria decisions, 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence intake ledger template | ${artifactId} | Review-return evidence intake scaffold; 50 blank evidence rows, 400 blank cells, 0 evidence, 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, no source-text/excerpt files, no surface, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_intake_ledger_template_artifact: \`${artifactId}\` (50 blank evidence rows; 400 blank evidence cells; 0 evidence; 0 review returns; 0 approvals; 0 exact spans; 0 source text; 0 excerpts; no notices, surfaces, or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_intake_ledger_template: \`${artifactId}\`; blank evidence intake only, no returns, evidence, approvals, exact spans, source text, excerpts, notices, accepted surfaces, or translation.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence intake ledger template; blank evidence rows are not evidence values, review returns, approvals, exact spans, copied source text, selected excerpts, attribution notices, source-text/excerpt sidecars, surfaces, translations, or readiness.`);
}

async function rebuildUploadQueueMd(queue) {
  const rows = queue.queued_items.map((item) => `| \`${item.filename}\` | ${titleClass(item.class)} | ${formatNumber(item.bytes)} | \`${item.sha256}\` |`).join('\n');
  const sourcePdfFiles = (queue.summary.source_pdf_files || 0) + (queue.summary.source_image_files || 0);
  const md = `# NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702

Status: local post-manifest upload queue, not a remote sync, commit, push, PR update, Zenodo action, or completion claim.

## Purpose

This queue preserves new coordination and translation-access artifacts created after the current indexed payload manifest. The indexed payload still lives at:

\`${queue.relationship_to_indexed_payload.indexed_payload_manifest}\`

Substantive artifacts are queued for upload when a valid checkout/staging path exists; mobile-plan or bandwidth wording should not suppress them.

## Queue Summary

- Queued files: \`${queue.summary.queued_files}\`
- Queued bytes: \`${formatNumber(queue.summary.queued_bytes)}\`
- Raw token files: \`${queue.summary.raw_token_files || 0}\`
- Source PDF/image files: \`${sourcePdfFiles}\`
- Source excerpt/source-text files: \`${queue.summary.source_text_or_excerpt_files || 0}\`
- Network actions performed now: \`0\`
- Git commits/pushes/PR updates performed now: \`0\`
- Recommended future checkout destination: \`${queue.recommended_destination_in_checkout}\`

## Queued Files

| File | Class | Bytes | SHA-256 |
| --- | --- | ---: | --- |
${rows}

## Future Staging Order

${queue.staging_order.map((step, index) => `${index + 1}. ${step}`).join('\n')}

## Boundary

This is not a manifest update, payload validator update, Git commit claim, remote branch claim, PR update, Zenodo publication, canonical-readiness claim, translation-readiness claim, or secret-storage artifact.
`;
  await writeFile(path.join(outputs, `${uploadQueueFile}.md`), md, 'utf8');
}

async function updateUploadQueue() {
  const upload = await readJson(uploadQueueFile);
  const files = [
    { filename: `${artifactId}.json`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_intake_ledger_template' },
    { filename: `${artifactId}.md`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_intake_ledger_template' },
    { filename: `${artifactId}.csv`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_intake_ledger_template' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'olp_dmoi_relation_function_package142_coordination_note' },
    { filename: `${noteId}.md`, class: 'olp_dmoi_relation_function_package142_coordination_note' },
    { filename: `${noteId}.sha256`, class: 'checksum_sidecar' }
  ];
  const destination = upload.obj.recommended_destination_in_checkout || 'noether-slavic-handoff/20260629/cross-session-coordination/20260702';
  const byFilename = new Map((upload.obj.queued_items || []).map((item) => [item.filename, item]));
  for (const file of files) {
    byFilename.set(file.filename, {
      filename: file.filename,
      class: file.class,
      bytes: 0,
      sha256: '',
      future_destination: `${destination}/${file.filename}`
    });
  }
  const refreshed = [];
  for (const item of byFilename.values()) {
    const data = await readFile(path.join(outputs, item.filename));
    refreshed.push({
      ...item,
      bytes: data.length,
      sha256: sha256Upper(data),
      future_destination: item.future_destination || `${destination}/${item.filename}`
    });
  }
  upload.obj.queued_items = refreshed;
  upload.obj.bandwidth_mode = 'upload_substantive_artifacts_when_checkout_available_no_mobile_plan_deferral';
  upload.obj.user_upload_clarification = '2026-07-03: user clarified that substantive artifacts should always be queued/uploaded when a staging path exists; do not suppress them because of mobile-plan or bandwidth wording.';
  upload.obj.package142_upload_queue_update = {
    captured_utc: '2026-07-03T05:47:00Z',
    substantive_artifacts_added_or_refreshed: files.length,
    artifact: artifactId,
    coordination_note: noteId,
    network_actions_performed_by_this_update: 0,
    commit_created: false,
    push_performed: false,
    pr_updated: false
  };
  upload.obj.summary.queued_files = upload.obj.queued_items.length;
  upload.obj.summary.queued_bytes = upload.obj.queued_items.reduce((sum, item) => sum + item.bytes, 0);
  upload.obj.summary.source_text_or_excerpt_files = 0;
  upload.obj.summary.network_actions_required_to_stage = 0;
  upload.obj.summary.network_actions_required_to_push = 1;
  upload.obj.staging_order = Array.isArray(upload.obj.staging_order) ? upload.obj.staging_order : [];
  const step = 'Stage package 142 OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence intake artifacts with this queue as substantive coordination material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (artifact.review_return_evidence_intake_rows.length !== 50) failures.push(`evidence_rows_not_50_${artifact.review_return_evidence_intake_rows.length}`);
  if (artifact.criterion_class_review_return_evidence_intake_summary_rows.length !== 5) failures.push(`criterion_class_rows_not_5_${artifact.criterion_class_review_return_evidence_intake_summary_rows.length}`);
  if (artifact.packet_unit_review_return_evidence_intake_summary_rows.length !== 10) failures.push(`packet_summary_rows_not_10_${artifact.packet_unit_review_return_evidence_intake_summary_rows.length}`);
  if (g.blank_evidence_fields_per_row !== blankEvidenceFields.length) failures.push(`blank_evidence_fields_per_row_not_${blankEvidenceFields.length}_${g.blank_evidence_fields_per_row}`);
  if (g.blank_evidence_field_cells_allocated !== 50 * blankEvidenceFields.length) failures.push(`blank_evidence_cells_mismatch_${g.blank_evidence_field_cells_allocated}`);
  if (g.criteria_unfilled !== 50) failures.push(`criteria_unfilled_not_50_${g.criteria_unfilled}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.review_return_evidence_intake_rows) {
    const filled = blankEvidenceFields.some((field) => row[field] !== null);
    if (filled || row.evidence_fields_filled !== 0 || row.evidence_value_filled || row.evidence_source_pointer_filled || row.evidence_row_ready_for_review || row.review_return_received || row.criterion_decision_allowed_after_intake || row.notice_template_approval_allowed_after_intake || row.source_text_or_excerpt_allowed_after_intake || row.surface_gate_opened || row.translation_gate_opened) {
      failures.push(`nonblank_evidence_intake_row_${row.review_return_evidence_intake_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const parent = (await readJson(parentCriteriaRubric)).obj;
const artifact = buildArtifact(parent);
const failures = validateGenerated(artifact);
if (failures.length) {
  console.error(JSON.stringify({ ok: false, failures }, null, 2));
  process.exit(1);
}

const note = buildNote(artifact);
await writeArtifactAndNote(artifact, note);
await updateRegistrations(artifact);
await updateUploadQueue();

const rootJsonFiles = (await readdir(outputs)).filter((name) => name.endsWith('.json')).length;
const recursiveJsonFiles = await countJsonFilesRecursive(outputs);
const packageIndex = (await readJson(packageIndexFile)).obj;
const queue = (await readJson(queueFile)).obj;
const upload = (await readJson(uploadQueueFile)).obj;

console.log(JSON.stringify({
  ok: true,
  artifact_id: artifactId,
  note_id: noteId,
  package_order_length: packageIndex.current_package_order?.length,
  queue_candidate_sources: queue.candidate_sources?.length,
  upload_queue_files: upload.summary?.queued_files,
  upload_queue_bytes: upload.summary?.queued_bytes,
  source_text_or_excerpt_files: upload.summary?.source_text_or_excerpt_files,
  review_return_evidence_intake_rows: artifact.gate_state.review_return_evidence_intake_rows,
  criterion_class_review_return_evidence_intake_summary_rows: artifact.gate_state.criterion_class_review_return_evidence_intake_summary_rows,
  packet_unit_review_return_evidence_intake_summary_rows: artifact.gate_state.packet_unit_review_return_evidence_intake_summary_rows,
  blank_evidence_fields_per_row: artifact.gate_state.blank_evidence_fields_per_row,
  blank_evidence_field_cells_allocated: artifact.gate_state.blank_evidence_field_cells_allocated,
  evidence_fields_filled: artifact.gate_state.evidence_fields_filled,
  evidence_values_filled: artifact.gate_state.evidence_values_filled,
  evidence_source_pointers_filled: artifact.gate_state.evidence_source_pointers_filled,
  criteria_rows_filled: artifact.gate_state.criteria_rows_filled,
  criteria_passed: artifact.gate_state.criteria_passed,
  criteria_failed: artifact.gate_state.criteria_failed,
  criteria_unfilled: artifact.gate_state.criteria_unfilled,
  review_returns_received: artifact.gate_state.review_returns_received,
  notice_template_rows_approved_for_fill: artifact.gate_state.notice_template_rows_approved_for_fill,
  selected_excerpt_attribution_notices_filled: artifact.gate_state.selected_excerpt_attribution_notices_filled,
  source_text_or_excerpt_files_created: artifact.gate_state.source_text_or_excerpt_files_created,
  exact_line_spans_selected: artifact.gate_state.exact_line_spans_selected,
  source_text_copied: artifact.gate_state.source_text_copied,
  excerpts_selected: artifact.gate_state.excerpts_selected,
  local_language_surfaces_filled: artifact.gate_state.local_language_surfaces_filled,
  translated_passages: artifact.gate_state.translated_passages,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
