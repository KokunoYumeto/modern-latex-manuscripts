import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_PACKET_20260703T050000Z';
const noteId = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_PACKET_NOTE_20260703T050100Z';
const generatedUtc = '2026-07-03T05:00:00Z';
const noteGeneratedUtc = '2026-07-03T05:01:00Z';
const packageOrder = 139;
const queueCandidateId = 'OTCQ-OLP-DMOI-RELATION-FUNCTION-SELECTED-EXCERPT-ATTRIBUTION-NOTICE-TEMPLATE-REVIEW-PACKET-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentNoticeTemplate = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_20260703T044500Z';
const parentArtifacts = [
  parentNoticeTemplate,
  'OLP_DMOI_RELATION_FUNCTION_SOURCE_TEXT_CAPTURE_POLICY_RETURN_LEDGER_TEMPLATE_20260703T043000Z',
  'OLP_DMOI_RELATION_FUNCTION_ATTRIBUTION_SCOPE_GAP_CHECK_20260702T134500Z'
];

const blankReviewFields = [
  'review_date',
  'reviewer_role',
  'template_structure_review',
  'parent_policy_link_review',
  'blank_notice_field_review',
  'source_text_absence_review',
  'downstream_gate_review',
  'review_note'
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

function buildReviewRows(parent) {
  return parent.selected_excerpt_attribution_notice_template_rows.map((row, index) => ({
    selected_excerpt_attribution_notice_template_review_packet_row_id: `ODRF-SEL-EXC-ATTR-REVIEW-${String(index + 1).padStart(2, '0')}`,
    parent_selected_excerpt_attribution_notice_template_row_id: row.selected_excerpt_attribution_notice_template_row_id,
    parent_source_text_capture_policy_return_row_id: row.parent_source_text_capture_policy_return_row_id,
    parent_packet_unit: row.parent_packet_unit,
    parent_ledger_row_id: row.parent_ledger_row_id,
    parent_pointer_row_id: row.parent_pointer_row_id,
    inherited_blank_notice_fields: row.blank_notice_fields,
    inherited_blank_notice_field_count: row.blank_notice_fields.length,
    inherited_notice_fields_filled: row.notice_fields_filled,
    inherited_attribution_notice_filled: row.attribution_notice_filled,
    inherited_attribution_notice_file_created: row.attribution_notice_file_created,
    inherited_source_text_capture_allowed_now: row.source_text_capture_allowed_now,
    inherited_excerpt_sidecar_allowed_now: row.excerpt_sidecar_allowed_now,
    blank_review_fields: blankReviewFields,
    review_date: null,
    reviewer_role: null,
    template_structure_review: null,
    parent_policy_link_review: null,
    blank_notice_field_review: null,
    source_text_absence_review: null,
    downstream_gate_review: null,
    review_note: null,
    review_fields_filled: 0,
    review_packet_dispatched: false,
    review_return_received: false,
    review_passed: false,
    review_failed: false,
    notice_template_approved_for_fill: false,
    source_text_or_excerpt_allowed_after_review: false,
    surface_gate_opened: false,
    translation_gate_opened: false,
    still_locked_reason: 'missing_reviewer_return_policy_return_exact_span_excerpt_and_notice_fill'
  }));
}

function buildNoticeFieldReviewSummaryRows(parent) {
  return parent.notice_field_summary_rows.map((row, index) => ({
    selected_excerpt_attribution_notice_field_review_summary_row_id: `ODRF-SEL-EXC-ATTR-REVIEW-FIELD-${String(index + 1).padStart(2, '0')}`,
    parent_notice_field_summary_row_id: row.selected_excerpt_attribution_notice_field_summary_row_id,
    field_id: row.field_id,
    required_before_fill: row.required_before_fill,
    template_rows_requiring_field: row.template_rows_requiring_field,
    inherited_fields_filled: row.fields_filled,
    review_rows_requiring_field_check: 10,
    field_review_returns_received: 0,
    field_review_passed: 0,
    field_review_failed: 0,
    field_ready_for_fill_after_review: false
  }));
}

function buildArtifact(parent) {
  const reviewRows = buildReviewRows(parent);
  const fieldReviewRows = buildNoticeFieldReviewSummaryRows(parent);
  const blankReviewCells = reviewRows.length * blankReviewFields.length;
  const parentGate = parent.gate_state || {};
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_packet_blank_no_review_returns_no_excerpts_no_source_text_no_notice_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Allocate a blank review packet for the package-138 selected-excerpt attribution notice template so future reviewers can check template structure, parent-policy linkage, blank notice fields, source-text absence, and downstream gate closure without receiving source text or approving excerpts.',
    parent_artifacts: parentArtifacts,
    review_packet_boundary: {
      packet_is: 'blank review packet for selected-excerpt attribution notice template rows',
      packet_is_not: [
        'review return',
        'approval to fill notices',
        'selected excerpt',
        'exact line span',
        'source text or excerpt sidecar',
        'filled attribution notice',
        'surface proposal',
        'translation draft',
        'pilot or publication claim'
      ],
      allowed_now: [
        'allocate review rows for existing blank notice-template rows',
        'make review criteria explicit before any notice fill',
        'keep review, source, notice, surface, and translation fields empty'
      ],
      blocked_now: [
        'inventing review returns',
        'approving notice template rows for fill',
        'copying source text or excerpts',
        'filling attribution notice text',
        'opening surface, translation, pilot, or publication gates'
      ]
    },
    blank_review_fields: blankReviewFields,
    selected_excerpt_attribution_notice_template_review_packet_rows: reviewRows,
    notice_field_review_summary_rows: fieldReviewRows,
    gate_state: {
      selected_excerpt_attribution_notice_template_review_packet_rows: reviewRows.length,
      notice_field_review_summary_rows: fieldReviewRows.length,
      blank_review_fields_per_row: blankReviewFields.length,
      blank_review_field_cells_allocated: blankReviewCells,
      inherited_notice_template_rows: parentGate.selected_excerpt_attribution_notice_template_rows,
      inherited_notice_fields_filled: parentGate.notice_fields_filled,
      inherited_selected_excerpt_attribution_notices_filled: parentGate.selected_excerpt_attribution_notices_filled,
      inherited_source_text_or_excerpt_files_created: parentGate.source_text_or_excerpt_files_created,
      review_fields_filled: 0,
      review_packets_dispatched: 0,
      review_returns_received: 0,
      review_returns_ingested: 0,
      review_rows_passed: 0,
      review_rows_failed: 0,
      review_field_returns_received: 0,
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
      validator: 'local_node_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_packet_generation_prevalidation_20260703T050000Z',
      zero_gate_assertions: [
        'review_fields_filled',
        'review_packets_dispatched',
        'review_returns_received',
        'review_returns_ingested',
        'review_rows_passed',
        'review_rows_failed',
        'review_field_returns_received',
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
      selected_excerpt_attribution_notice_template_review_packet_rows: reviewRows.length,
      notice_field_review_summary_rows: fieldReviewRows.length,
      blank_review_fields_per_row: blankReviewFields.length,
      blank_review_field_cells_allocated: blankReviewCells
    },
    next_valid_artifacts: [
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_LEDGER_TEMPLATE_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SOURCE_TEXT_CAPTURE_POLICY_RETURN_LEDGER_WITH_RETURNS_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_RETURN_EVIDENCE_CRITERIA_DECISION_REVIEW_PACKET_<timestamp>'
    ],
    decision: 'Package 139 creates a blank review packet for package 138. It records what must be reviewed later while preserving zero review returns, zero approvals, zero exact spans, zero source text, zero excerpts, zero notices, zero surfaces, zero translations, and zero readiness.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const reviewRows = artifact.selected_excerpt_attribution_notice_template_review_packet_rows.map((row) => `| ${row.selected_excerpt_attribution_notice_template_review_packet_row_id} | ${row.parent_packet_unit} | ${row.parent_selected_excerpt_attribution_notice_template_row_id} | ${row.blank_review_fields.length} | ${row.review_fields_filled} | ${row.review_return_received} |`).join('\n');
  const fieldRows = artifact.notice_field_review_summary_rows.map((row) => `| ${row.selected_excerpt_attribution_notice_field_review_summary_row_id} | ${row.field_id} | ${row.review_rows_requiring_field_check} | ${row.field_review_returns_received} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: ${artifact.status}

## Purpose

${artifact.purpose}

## Boundary

This is a blank review packet. It is not a review return, approval, selected excerpt, exact line span, source text, filled attribution notice, source-text/excerpt sidecar, surface, translation, pilot, publication, commit, push, PR update, or Zenodo action.

## Counts

- Review packet rows: \`${g.selected_excerpt_attribution_notice_template_review_packet_rows}\`
- Notice-field review summaries: \`${g.notice_field_review_summary_rows}\`
- Blank review fields per row: \`${g.blank_review_fields_per_row}\`
- Blank review-field cells allocated: \`${g.blank_review_field_cells_allocated}\`
- Review dispatches/returns/pass/fail: \`${g.review_packets_dispatched}/${g.review_returns_received}/${g.review_rows_passed}/${g.review_rows_failed}\`
- Notice approvals/fills/notices/files: \`${g.notice_template_rows_approved_for_fill}/${g.notice_fields_filled}/${g.selected_excerpt_attribution_notices_filled}/${g.source_text_or_excerpt_files_created}\`
- Exact spans/source text/excerpts: \`${g.exact_line_spans_selected}/${g.source_text_copied}/${g.excerpts_selected}\`
- Surfaces/translations/readiness: \`${g.local_language_surfaces_filled}/${g.translated_passages}/${g.pilot_ready}\`

## Review Packet Rows

| Row | Packet unit | Parent notice row | Blank review fields | Filled review fields | Return received |
| --- | --- | --- | ---: | ---: | --- |
${reviewRows}

## Notice Field Review Summary

| Row | Field | Review rows requiring check | Review returns received |
| --- | --- | ---: | ---: |
${fieldRows}

## Decision

${artifact.decision}
`;
}

function buildArtifactCsv(artifact) {
  const rows = [];
  rows.push(['section', 'row_id', 'packet_or_field', 'parent_id', 'blank_or_required_count', 'filled_or_return_count', 'gate_open'].map(csvCell).join(','));
  for (const row of artifact.selected_excerpt_attribution_notice_template_review_packet_rows) {
    rows.push([
      'selected_excerpt_attribution_notice_template_review_packet',
      row.selected_excerpt_attribution_notice_template_review_packet_row_id,
      row.parent_packet_unit,
      row.parent_selected_excerpt_attribution_notice_template_row_id,
      row.blank_review_fields.length,
      row.review_fields_filled,
      row.surface_gate_opened || row.translation_gate_opened
    ].map(csvCell).join(','));
  }
  for (const row of artifact.notice_field_review_summary_rows) {
    rows.push([
      'notice_field_review_summary',
      row.selected_excerpt_attribution_notice_field_review_summary_row_id,
      row.field_id,
      row.parent_notice_field_summary_row_id,
      row.review_rows_requiring_field_check,
      row.field_review_returns_received,
      row.field_ready_for_fill_after_review
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
    status: 'pointer_only_selected_excerpt_attribution_notice_template_review_packet_note_no_upload_claim_no_remote_state_claim',
    purpose: 'Record package-139 OLP/DMOI relation-function selected-excerpt attribution notice template review-packet continuation while preserving no-review-return/no-excerpt/no-source-text/no-notice/no-translation boundaries.',
    points_to_artifacts: [
      `${artifactId}.json`,
      `${artifactId}.md`,
      `${artifactId}.csv`,
      `${artifactId}.sha256`
    ],
    summary: {
      selected_excerpt_attribution_notice_template_review_packet_rows: g.selected_excerpt_attribution_notice_template_review_packet_rows,
      notice_field_review_summary_rows: g.notice_field_review_summary_rows,
      blank_review_field_cells_allocated: g.blank_review_field_cells_allocated,
      review_fields_filled: g.review_fields_filled,
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
    upload_intent: 'Queue the package-139 JSON/MD/CSV/checksum and this note for the existing Noether upload path as substantive coordination material; user clarified on 2026-07-03 that substantive artifacts should not be deferred because of mobile-plan or bandwidth wording.',
    message_template: `Package 139 added ${artifactId}: 10 blank selected-excerpt attribution notice template review rows, 14 notice-field review summaries, 80 blank review-field cells, 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 attribution notices, 0 source-text/excerpt files, 0 surfaces/translations, 0 readiness.`
  };
}

function buildNoteMd(note) {
  return `# Package 139 Coordination Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${note.source_artifact}\`

Generated UTC: \`${note.generated_utc}\`

## Summary

- Review packet rows: \`${note.summary.selected_excerpt_attribution_notice_template_review_packet_rows}\`
- Notice-field review summaries: \`${note.summary.notice_field_review_summary_rows}\`
- Blank review-field cells allocated: \`${note.summary.blank_review_field_cells_allocated}\`
- Review fields/returns/approvals: \`${note.summary.review_fields_filled}/${note.summary.review_returns_received}/${note.summary.notice_template_rows_approved_for_fill}\`
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
      role: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_packet_support',
      artifact: artifactId,
      current_use: '10 blank selected-excerpt attribution notice template review-packet rows; 8 review fields per row; 80 blank review-field cells; 14 notice-field review summaries; 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 surfaces, 0 translation, 0 readiness'
    });
  }
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_packet = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_packet_rows: g.selected_excerpt_attribution_notice_template_review_packet_rows,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_blank_cells: g.blank_review_field_cells_allocated,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_returns: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_approvals: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_source_text_or_excerpt_files: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_review_return_ledger_template_or_policy_returns_only_no_source_text_no_excerpt_no_surfaces_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'OLP/DMOI relation-function selected-excerpt attribution notice template review packet',
    route: artifactId,
    license_status_to_recheck: 'blank_review_packet_only_no_review_returns_no_approvals_no_exact_spans_no_source_text_no_excerpts_no_notices_no_translation',
    best_translation_use: 'future selected-excerpt attribution notice template review before notice fill, source-text/excerpt sidecar, surface, or translation',
    candidate_lanes: [
      'olp_dmoi_relation_function_attribution_notice_lane',
      'blank_review_packet',
      'review_only_construction_scaffold',
      'source_aware_excerpt_governance'
    ],
    priority: 1,
    status: 'blank_selected_excerpt_attribution_notice_template_review_packet_no_returns_no_source_text_no_excerpts_no_translation',
    gate_state: {
      selected_excerpt_attribution_notice_template_review_packet_rows: g.selected_excerpt_attribution_notice_template_review_packet_rows,
      blank_review_field_cells_allocated: g.blank_review_field_cells_allocated,
      review_returns_received: 0,
      notice_template_rows_approved_for_fill: 0,
      selected_excerpt_attribution_notices_filled: 0,
      source_text_or_excerpt_files_created: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_packet: ${artifactId}_10_blank_review_rows_80_blank_cells_0_returns_0_approvals_0_source_text_0_excerpts_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_packet_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_packet_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_packet_rows: g.selected_excerpt_attribution_notice_template_review_packet_rows,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_blank_cells: g.blank_review_field_cells_allocated,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_returns: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_approvals: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_source_text_or_excerpt_files: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_surfaces: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_translations: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_packet = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_packet: ${artifactId}_blank_review_packet_only_no_returns_no_approvals_no_source_text_no_excerpts_no_notices_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_packet = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates 10 blank selected-excerpt attribution notice template review-packet rows and 80 blank review-field cells after package 138; 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, 0 readiness; substantive artifacts should be uploaded when a staging path exists.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OLP/DMOI relation-function selected-excerpt attribution notice template review packet; 10 blank review rows, 80 blank cells, 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 139: OLP/DMOI relation-function selected-excerpt attribution notice template review packet after package 138. It records 10 blank review-packet rows, 14 notice-field review summaries, and 80 blank review-field cells while keeping 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | OLP/DMOI relation-function selected-excerpt attribution notice template review packet | ${artifactId} | Review packet scaffold; 10 blank review rows, 80 blank cells, 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, no source-text/excerpt files, no surface, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_packet_artifact: \`${artifactId}\` (10 blank review rows; 80 blank review cells; 0 review returns; 0 approvals; 0 exact spans; 0 source text; 0 excerpts; no notices, surfaces, or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_packet: \`${artifactId}\`; blank review packet only, no returns, approvals, exact spans, source text, excerpts, notices, accepted surfaces, or translation.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OLP/DMOI relation-function selected-excerpt attribution notice template review packet; blank review rows are not review returns, approvals, exact spans, copied source text, selected excerpts, attribution notices, source-text/excerpt sidecars, surfaces, translations, or readiness.`);
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
    { filename: `${artifactId}.json`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_packet' },
    { filename: `${artifactId}.md`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_packet' },
    { filename: `${artifactId}.csv`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_packet' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'olp_dmoi_relation_function_package139_coordination_note' },
    { filename: `${noteId}.md`, class: 'olp_dmoi_relation_function_package139_coordination_note' },
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
  upload.obj.package139_upload_queue_update = {
    captured_utc: '2026-07-03T05:02:00Z',
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
  const step = 'Stage package 139 OLP/DMOI relation-function selected-excerpt attribution notice template review-packet artifacts with this queue as substantive coordination material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (artifact.selected_excerpt_attribution_notice_template_review_packet_rows.length !== 10) failures.push(`review_rows_not_10_${artifact.selected_excerpt_attribution_notice_template_review_packet_rows.length}`);
  if (artifact.notice_field_review_summary_rows.length !== 14) failures.push(`field_review_rows_not_14_${artifact.notice_field_review_summary_rows.length}`);
  if (g.blank_review_fields_per_row !== blankReviewFields.length) failures.push(`blank_review_fields_per_row_not_${blankReviewFields.length}_${g.blank_review_fields_per_row}`);
  if (g.blank_review_field_cells_allocated !== 10 * blankReviewFields.length) failures.push(`blank_review_cells_mismatch_${g.blank_review_field_cells_allocated}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.selected_excerpt_attribution_notice_template_review_packet_rows) {
    const filled = blankReviewFields.some((field) => row[field] !== null);
    if (filled || row.review_fields_filled !== 0 || row.review_packet_dispatched || row.review_return_received || row.review_passed || row.review_failed || row.notice_template_approved_for_fill || row.source_text_or_excerpt_allowed_after_review || row.surface_gate_opened || row.translation_gate_opened) {
      failures.push(`nonblank_review_packet_row_${row.selected_excerpt_attribution_notice_template_review_packet_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const parent = (await readJson(parentNoticeTemplate)).obj;
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
  selected_excerpt_attribution_notice_template_review_packet_rows: artifact.gate_state.selected_excerpt_attribution_notice_template_review_packet_rows,
  notice_field_review_summary_rows: artifact.gate_state.notice_field_review_summary_rows,
  blank_review_fields_per_row: artifact.gate_state.blank_review_fields_per_row,
  blank_review_field_cells_allocated: artifact.gate_state.blank_review_field_cells_allocated,
  review_fields_filled: artifact.gate_state.review_fields_filled,
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
