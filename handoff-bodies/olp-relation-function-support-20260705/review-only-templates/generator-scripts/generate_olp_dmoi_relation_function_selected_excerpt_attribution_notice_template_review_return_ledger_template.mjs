import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_LEDGER_TEMPLATE_20260703T051500Z';
const noteId = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_LEDGER_TEMPLATE_NOTE_20260703T051600Z';
const generatedUtc = '2026-07-03T05:15:00Z';
const noteGeneratedUtc = '2026-07-03T05:16:00Z';
const packageOrder = 140;
const queueCandidateId = 'OTCQ-OLP-DMOI-RELATION-FUNCTION-SELECTED-EXCERPT-ATTRIBUTION-NOTICE-TEMPLATE-REVIEW-RETURN-LEDGER-TEMPLATE-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentReviewPacket = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_PACKET_20260703T050000Z';
const parentArtifacts = [
  parentReviewPacket,
  'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_20260703T044500Z',
  'OLP_DMOI_RELATION_FUNCTION_SOURCE_TEXT_CAPTURE_POLICY_RETURN_LEDGER_TEMPLATE_20260703T043000Z'
];

const blankReturnFields = [
  'return_date',
  'return_authority_role',
  'non_personal_review_route_or_owner_id',
  'template_structure_decision',
  'parent_policy_link_decision',
  'blank_notice_field_decision',
  'source_text_absence_decision',
  'downstream_gate_decision',
  'notice_template_approval_decision',
  'return_note'
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

function buildReturnRows(parent) {
  return parent.selected_excerpt_attribution_notice_template_review_packet_rows.map((row, index) => ({
    selected_excerpt_attribution_notice_template_review_return_ledger_row_id: `ODRF-SEL-EXC-ATTR-REVIEW-RETURN-${String(index + 1).padStart(2, '0')}`,
    parent_selected_excerpt_attribution_notice_template_review_packet_row_id: row.selected_excerpt_attribution_notice_template_review_packet_row_id,
    parent_selected_excerpt_attribution_notice_template_row_id: row.parent_selected_excerpt_attribution_notice_template_row_id,
    parent_source_text_capture_policy_return_row_id: row.parent_source_text_capture_policy_return_row_id,
    parent_packet_unit: row.parent_packet_unit,
    parent_ledger_row_id: row.parent_ledger_row_id,
    parent_pointer_row_id: row.parent_pointer_row_id,
    inherited_blank_review_fields: row.blank_review_fields,
    inherited_blank_review_field_count: row.blank_review_fields.length,
    inherited_review_fields_filled: row.review_fields_filled,
    inherited_review_packet_dispatched: row.review_packet_dispatched,
    inherited_review_return_received: row.review_return_received,
    inherited_notice_template_approved_for_fill: row.notice_template_approved_for_fill,
    blank_return_fields: blankReturnFields,
    return_date: null,
    return_authority_role: null,
    non_personal_review_route_or_owner_id: null,
    template_structure_decision: null,
    parent_policy_link_decision: null,
    blank_notice_field_decision: null,
    source_text_absence_decision: null,
    downstream_gate_decision: null,
    notice_template_approval_decision: null,
    return_note: null,
    return_fields_filled: 0,
    return_received: false,
    return_ingested: false,
    template_structure_review_passed: false,
    parent_policy_link_review_passed: false,
    blank_notice_field_review_passed: false,
    source_text_absence_review_passed: false,
    downstream_gate_review_passed: false,
    notice_template_approved_for_fill: false,
    source_text_or_excerpt_allowed_after_return: false,
    surface_gate_opened: false,
    translation_gate_opened: false,
    still_locked_reason: 'missing_dated_non_personal_review_return_policy_return_exact_span_excerpt_and_notice_fill'
  }));
}

function buildReturnFieldSummaryRows() {
  return blankReturnFields.map((field, index) => ({
    selected_excerpt_attribution_notice_template_review_return_field_summary_row_id: `ODRF-SEL-EXC-ATTR-REVIEW-RETURN-FIELD-${String(index + 1).padStart(2, '0')}`,
    return_field_id: field,
    return_rows_requiring_field: 10,
    return_fields_filled: 0,
    field_ready_to_ingest: false
  }));
}

function buildReviewFieldReturnSummaryRows(parent) {
  const fields = parent.blank_review_fields || [];
  return fields.map((field, index) => ({
    selected_excerpt_attribution_notice_template_review_field_return_summary_row_id: `ODRF-SEL-EXC-ATTR-REVIEW-RETURN-RFIELD-${String(index + 1).padStart(2, '0')}`,
    parent_review_field_id: field,
    review_packet_rows_requiring_return: 10,
    return_rows_received: 0,
    return_rows_passed: 0,
    return_rows_failed: 0,
    downstream_gate_opened: false
  }));
}

function buildArtifact(parent) {
  const returnRows = buildReturnRows(parent);
  const returnFieldRows = buildReturnFieldSummaryRows();
  const reviewFieldReturnRows = buildReviewFieldReturnSummaryRows(parent);
  const blankReturnCells = returnRows.length * blankReturnFields.length;
  const parentGate = parent.gate_state || {};
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_ledger_template_blank_no_returns_no_approvals_no_excerpts_no_source_text_no_notice_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Allocate a blank return ledger for the package-139 selected-excerpt attribution notice template review packet so future dated non-personal review returns have a fixed landing place without inventing returns, approvals, source text, excerpts, notices, surfaces, or translations.',
    parent_artifacts: parentArtifacts,
    return_ledger_boundary: {
      ledger_template_is: 'blank review-return ledger template for selected-excerpt attribution notice template review rows',
      ledger_template_is_not: [
        'review return',
        'approval to fill notices',
        'source-text capture permission',
        'selected excerpt',
        'exact line span',
        'filled attribution notice',
        'source-text or excerpt sidecar',
        'surface proposal',
        'translation draft',
        'pilot or publication claim'
      ],
      allowed_now: [
        'allocate blank return rows for existing review-packet rows',
        'make return fields explicit before any review return is ingested',
        'keep every approval, source, notice, surface, and translation field empty'
      ],
      blocked_now: [
        'inventing review returns',
        'approving notice templates for fill',
        'copying source text or excerpts',
        'filling attribution notices',
        'opening surface, translation, pilot, or publication gates'
      ]
    },
    blank_return_fields: blankReturnFields,
    selected_excerpt_attribution_notice_template_review_return_ledger_rows: returnRows,
    review_return_field_summary_rows: returnFieldRows,
    review_field_return_summary_rows: reviewFieldReturnRows,
    gate_state: {
      selected_excerpt_attribution_notice_template_review_return_ledger_rows: returnRows.length,
      review_return_field_summary_rows: returnFieldRows.length,
      review_field_return_summary_rows: reviewFieldReturnRows.length,
      blank_return_fields_per_row: blankReturnFields.length,
      blank_return_field_cells_allocated: blankReturnCells,
      inherited_review_packet_rows: parentGate.selected_excerpt_attribution_notice_template_review_packet_rows,
      inherited_review_fields_filled: parentGate.review_fields_filled,
      inherited_review_returns_received: parentGate.review_returns_received,
      inherited_notice_template_rows_approved_for_fill: parentGate.notice_template_rows_approved_for_fill,
      return_fields_filled: 0,
      review_return_rows_filled: 0,
      review_returns_received: 0,
      review_returns_ingested: 0,
      review_rows_passed: 0,
      review_rows_failed: 0,
      template_structure_reviews_passed: 0,
      parent_policy_link_reviews_passed: 0,
      blank_notice_field_reviews_passed: 0,
      source_text_absence_reviews_passed: 0,
      downstream_gate_reviews_passed: 0,
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
      validator: 'local_node_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_ledger_template_generation_prevalidation_20260703T051500Z',
      zero_gate_assertions: [
        'return_fields_filled',
        'review_return_rows_filled',
        'review_returns_received',
        'review_returns_ingested',
        'review_rows_passed',
        'review_rows_failed',
        'template_structure_reviews_passed',
        'parent_policy_link_reviews_passed',
        'blank_notice_field_reviews_passed',
        'source_text_absence_reviews_passed',
        'downstream_gate_reviews_passed',
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
      selected_excerpt_attribution_notice_template_review_return_ledger_rows: returnRows.length,
      review_return_field_summary_rows: returnFieldRows.length,
      review_field_return_summary_rows: reviewFieldReturnRows.length,
      blank_return_fields_per_row: blankReturnFields.length,
      blank_return_field_cells_allocated: blankReturnCells
    },
    next_valid_artifacts: [
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_LEDGER_WITH_RETURNS_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_RUBRIC_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SOURCE_TEXT_CAPTURE_POLICY_RETURN_LEDGER_WITH_RETURNS_<timestamp>'
    ],
    decision: 'Package 140 creates a blank review-return ledger template for package 139. It provides return slots only and preserves zero review returns, zero approvals, zero exact spans, zero source text, zero excerpts, zero notices, zero surfaces, zero translations, and zero readiness.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const returnRows = artifact.selected_excerpt_attribution_notice_template_review_return_ledger_rows.map((row) => `| ${row.selected_excerpt_attribution_notice_template_review_return_ledger_row_id} | ${row.parent_packet_unit} | ${row.parent_selected_excerpt_attribution_notice_template_review_packet_row_id} | ${row.blank_return_fields.length} | ${row.return_fields_filled} | ${row.return_received} |`).join('\n');
  const fieldRows = artifact.review_return_field_summary_rows.map((row) => `| ${row.selected_excerpt_attribution_notice_template_review_return_field_summary_row_id} | ${row.return_field_id} | ${row.return_rows_requiring_field} | ${row.return_fields_filled} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: ${artifact.status}

## Purpose

${artifact.purpose}

## Boundary

This is a blank review-return ledger template. It is not a review return, approval, selected excerpt, exact line span, source text, filled attribution notice, source-text/excerpt sidecar, surface, translation, pilot, publication, commit, push, PR update, or Zenodo action.

## Counts

- Review-return ledger rows: \`${g.selected_excerpt_attribution_notice_template_review_return_ledger_rows}\`
- Return-field summaries: \`${g.review_return_field_summary_rows}\`
- Review-field return summaries: \`${g.review_field_return_summary_rows}\`
- Blank return fields per row: \`${g.blank_return_fields_per_row}\`
- Blank return-field cells allocated: \`${g.blank_return_field_cells_allocated}\`
- Return fields/returns/ingested/pass/fail: \`${g.return_fields_filled}/${g.review_returns_received}/${g.review_returns_ingested}/${g.review_rows_passed}/${g.review_rows_failed}\`
- Notice approvals/fills/notices/files: \`${g.notice_template_rows_approved_for_fill}/${g.notice_fields_filled}/${g.selected_excerpt_attribution_notices_filled}/${g.source_text_or_excerpt_files_created}\`
- Exact spans/source text/excerpts: \`${g.exact_line_spans_selected}/${g.source_text_copied}/${g.excerpts_selected}\`
- Surfaces/translations/readiness: \`${g.local_language_surfaces_filled}/${g.translated_passages}/${g.pilot_ready}\`

## Review-Return Ledger Rows

| Row | Packet unit | Parent review row | Blank return fields | Filled return fields | Return received |
| --- | --- | --- | ---: | ---: | --- |
${returnRows}

## Return Field Summary

| Row | Return field | Rows requiring field | Fields filled |
| --- | --- | ---: | ---: |
${fieldRows}

## Decision

${artifact.decision}
`;
}

function buildArtifactCsv(artifact) {
  const rows = [];
  rows.push(['section', 'row_id', 'packet_or_field', 'parent_id', 'blank_or_required_count', 'filled_or_return_count', 'gate_open'].map(csvCell).join(','));
  for (const row of artifact.selected_excerpt_attribution_notice_template_review_return_ledger_rows) {
    rows.push([
      'selected_excerpt_attribution_notice_template_review_return_ledger',
      row.selected_excerpt_attribution_notice_template_review_return_ledger_row_id,
      row.parent_packet_unit,
      row.parent_selected_excerpt_attribution_notice_template_review_packet_row_id,
      row.blank_return_fields.length,
      row.return_fields_filled,
      row.surface_gate_opened || row.translation_gate_opened
    ].map(csvCell).join(','));
  }
  for (const row of artifact.review_return_field_summary_rows) {
    rows.push([
      'review_return_field_summary',
      row.selected_excerpt_attribution_notice_template_review_return_field_summary_row_id,
      row.return_field_id,
      '',
      row.return_rows_requiring_field,
      row.return_fields_filled,
      row.field_ready_to_ingest
    ].map(csvCell).join(','));
  }
  for (const row of artifact.review_field_return_summary_rows) {
    rows.push([
      'review_field_return_summary',
      row.selected_excerpt_attribution_notice_template_review_field_return_summary_row_id,
      row.parent_review_field_id,
      '',
      row.review_packet_rows_requiring_return,
      row.return_rows_received,
      row.downstream_gate_opened
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
    status: 'pointer_only_selected_excerpt_attribution_notice_template_review_return_ledger_template_note_no_upload_claim_no_remote_state_claim',
    purpose: 'Record package-140 OLP/DMOI relation-function selected-excerpt attribution notice template review-return ledger continuation while preserving no-review-return/no-approval/no-excerpt/no-source-text/no-notice/no-translation boundaries.',
    points_to_artifacts: [
      `${artifactId}.json`,
      `${artifactId}.md`,
      `${artifactId}.csv`,
      `${artifactId}.sha256`
    ],
    summary: {
      selected_excerpt_attribution_notice_template_review_return_ledger_rows: g.selected_excerpt_attribution_notice_template_review_return_ledger_rows,
      review_return_field_summary_rows: g.review_return_field_summary_rows,
      review_field_return_summary_rows: g.review_field_return_summary_rows,
      blank_return_field_cells_allocated: g.blank_return_field_cells_allocated,
      return_fields_filled: g.return_fields_filled,
      review_returns_received: g.review_returns_received,
      notice_template_rows_approved_for_fill: g.notice_template_rows_approved_for_fill,
      selected_excerpt_attribution_notices_filled: g.selected_excerpt_attribution_notices_filled,
      source_text_or_excerpt_files_created: g.source_text_or_excerpt_files_created,
      exact_line_spans_selected: g.exact_line_spans_selected,
      source_text_copied: g.source_text_copied,
      excerpts_selected: g.excerpts_selected,
      surfaces_or_translations: g.local_language_surfaces_filled + g.bridge_surfaces_accepted + g.semi_constructed_surfaces_accepted + g.translated_passages,
      readiness_claims: Number(g.publication_ready) + Number(g.translation_ready) + Number(g.constructed_surface_ready) + Number(g.pilot_ready)
    },
    boundary: 'Pointer-only coordination note. No review return, approval, exact line span, selected excerpt, source text, attribution notice text, source-text/excerpt sidecar, surface, translation, pilot, publication, commit, push, PR update, or Zenodo action is claimed.',
    upload_intent: 'Queue the package-140 JSON/MD/CSV/checksum and this note for the existing Noether upload path as substantive coordination material; user clarified on 2026-07-03 that substantive artifacts should not be deferred because of mobile-plan or bandwidth wording.',
    message_template: `Package 140 added ${artifactId}: 10 blank selected-excerpt attribution notice template review-return rows, 10 return-field summaries, 8 review-field return summaries, 100 blank return-field cells, 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 attribution notices, 0 source-text/excerpt files, 0 surfaces/translations, 0 readiness.`
  };
}

function buildNoteMd(note) {
  return `# Package 140 Coordination Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${note.source_artifact}\`

Generated UTC: \`${note.generated_utc}\`

## Summary

- Review-return ledger rows: \`${note.summary.selected_excerpt_attribution_notice_template_review_return_ledger_rows}\`
- Return-field summaries: \`${note.summary.review_return_field_summary_rows}\`
- Review-field return summaries: \`${note.summary.review_field_return_summary_rows}\`
- Blank return-field cells allocated: \`${note.summary.blank_return_field_cells_allocated}\`
- Return fields/returns/approvals: \`${note.summary.return_fields_filled}/${note.summary.review_returns_received}/${note.summary.notice_template_rows_approved_for_fill}\`
- Notices/source-text files/exact spans/source text/excerpts: \`${note.summary.selected_excerpt_attribution_notices_filled}/${note.summary.source_text_or_excerpt_files_created}/${note.summary.exact_line_spans_selected}/${note.summary.source_text_copied}/${note.summary.excerpts_selected}\`
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
      role: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_ledger_template_support',
      artifact: artifactId,
      current_use: '10 blank selected-excerpt attribution notice template review-return ledger rows; 10 return fields per row; 100 blank return-field cells; 10 return-field summaries; 8 review-field return summaries; 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 surfaces, 0 translation, 0 readiness'
    });
  }
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_ledger_template = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_ledger_rows: g.selected_excerpt_attribution_notice_template_review_return_ledger_rows,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_blank_cells: g.blank_return_field_cells_allocated,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_returns: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_approvals: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_source_text_or_excerpt_files: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_review_return_evidence_criteria_or_with_returns_only_no_source_text_no_excerpt_no_surfaces_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'OLP/DMOI relation-function selected-excerpt attribution notice template review-return ledger template',
    route: artifactId,
    license_status_to_recheck: 'blank_review_return_ledger_only_no_returns_no_approvals_no_exact_spans_no_source_text_no_excerpts_no_notices_no_translation',
    best_translation_use: 'future selected-excerpt attribution notice template review-return intake before approval, notice fill, source-text/excerpt sidecar, surface, or translation',
    candidate_lanes: [
      'olp_dmoi_relation_function_attribution_notice_lane',
      'blank_review_return_ledger',
      'review_only_construction_scaffold',
      'source_aware_excerpt_governance'
    ],
    priority: 1,
    status: 'blank_selected_excerpt_attribution_notice_template_review_return_ledger_no_returns_no_approvals_no_source_text_no_excerpts_no_translation',
    gate_state: {
      selected_excerpt_attribution_notice_template_review_return_ledger_rows: g.selected_excerpt_attribution_notice_template_review_return_ledger_rows,
      blank_return_field_cells_allocated: g.blank_return_field_cells_allocated,
      review_returns_received: 0,
      notice_template_rows_approved_for_fill: 0,
      selected_excerpt_attribution_notices_filled: 0,
      source_text_or_excerpt_files_created: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_ledger_template: ${artifactId}_10_blank_return_rows_100_blank_cells_0_returns_0_approvals_0_source_text_0_excerpts_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_ledger_template_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_ledger_template_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_ledger_rows: g.selected_excerpt_attribution_notice_template_review_return_ledger_rows,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_blank_cells: g.blank_return_field_cells_allocated,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_returns: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_approvals: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_source_text_or_excerpt_files: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_surfaces: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_translations: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_ledger_template = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_ledger_template: ${artifactId}_blank_review_return_ledger_only_no_returns_no_approvals_no_source_text_no_excerpts_no_notices_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_ledger_template = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates 10 blank selected-excerpt attribution notice template review-return ledger rows and 100 blank return-field cells after package 139; 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, 0 readiness; substantive artifacts should be uploaded when a staging path exists.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OLP/DMOI relation-function selected-excerpt attribution notice template review-return ledger template; 10 blank return rows, 100 blank cells, 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 140: OLP/DMOI relation-function selected-excerpt attribution notice template review-return ledger template after package 139. It records 10 blank return rows, 10 return-field summaries, 8 review-field return summaries, and 100 blank return-field cells while keeping 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | OLP/DMOI relation-function selected-excerpt attribution notice template review-return ledger template | ${artifactId} | Review-return ledger scaffold; 10 blank return rows, 100 blank cells, 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, no source-text/excerpt files, no surface, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_ledger_template_artifact: \`${artifactId}\` (10 blank review-return rows; 100 blank return cells; 0 review returns; 0 approvals; 0 exact spans; 0 source text; 0 excerpts; no notices, surfaces, or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_ledger_template: \`${artifactId}\`; blank review-return ledger only, no returns, approvals, exact spans, source text, excerpts, notices, accepted surfaces, or translation.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OLP/DMOI relation-function selected-excerpt attribution notice template review-return ledger template; blank return rows are not review returns, approvals, exact spans, copied source text, selected excerpts, attribution notices, source-text/excerpt sidecars, surfaces, translations, or readiness.`);
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
    { filename: `${artifactId}.json`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_ledger_template' },
    { filename: `${artifactId}.md`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_ledger_template' },
    { filename: `${artifactId}.csv`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_ledger_template' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'olp_dmoi_relation_function_package140_coordination_note' },
    { filename: `${noteId}.md`, class: 'olp_dmoi_relation_function_package140_coordination_note' },
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
  upload.obj.package140_upload_queue_update = {
    captured_utc: '2026-07-03T05:17:00Z',
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
  const step = 'Stage package 140 OLP/DMOI relation-function selected-excerpt attribution notice template review-return ledger artifacts with this queue as substantive coordination material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (artifact.selected_excerpt_attribution_notice_template_review_return_ledger_rows.length !== 10) failures.push(`return_rows_not_10_${artifact.selected_excerpt_attribution_notice_template_review_return_ledger_rows.length}`);
  if (artifact.review_return_field_summary_rows.length !== blankReturnFields.length) failures.push(`return_field_rows_not_${blankReturnFields.length}_${artifact.review_return_field_summary_rows.length}`);
  if (artifact.review_field_return_summary_rows.length !== 8) failures.push(`review_field_return_rows_not_8_${artifact.review_field_return_summary_rows.length}`);
  if (g.blank_return_fields_per_row !== blankReturnFields.length) failures.push(`blank_return_fields_per_row_not_${blankReturnFields.length}_${g.blank_return_fields_per_row}`);
  if (g.blank_return_field_cells_allocated !== 10 * blankReturnFields.length) failures.push(`blank_return_cells_mismatch_${g.blank_return_field_cells_allocated}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.selected_excerpt_attribution_notice_template_review_return_ledger_rows) {
    const filled = blankReturnFields.some((field) => row[field] !== null);
    if (filled || row.return_fields_filled !== 0 || row.return_received || row.return_ingested || row.notice_template_approved_for_fill || row.source_text_or_excerpt_allowed_after_return || row.surface_gate_opened || row.translation_gate_opened) {
      failures.push(`nonblank_review_return_row_${row.selected_excerpt_attribution_notice_template_review_return_ledger_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const parent = (await readJson(parentReviewPacket)).obj;
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
  selected_excerpt_attribution_notice_template_review_return_ledger_rows: artifact.gate_state.selected_excerpt_attribution_notice_template_review_return_ledger_rows,
  review_return_field_summary_rows: artifact.gate_state.review_return_field_summary_rows,
  review_field_return_summary_rows: artifact.gate_state.review_field_return_summary_rows,
  blank_return_fields_per_row: artifact.gate_state.blank_return_fields_per_row,
  blank_return_field_cells_allocated: artifact.gate_state.blank_return_field_cells_allocated,
  return_fields_filled: artifact.gate_state.return_fields_filled,
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
