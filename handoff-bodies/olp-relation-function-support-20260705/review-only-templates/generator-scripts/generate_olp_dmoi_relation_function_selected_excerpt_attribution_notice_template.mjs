import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_20260703T044500Z';
const noteId = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_NOTE_20260703T044600Z';
const generatedUtc = '2026-07-03T04:45:00Z';
const noteGeneratedUtc = '2026-07-03T04:46:00Z';
const packageOrder = 138;
const queueCandidateId = 'OTCQ-OLP-DMOI-RELATION-FUNCTION-SELECTED-EXCERPT-ATTRIBUTION-NOTICE-TEMPLATE-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentPolicyReturnLedger = 'OLP_DMOI_RELATION_FUNCTION_SOURCE_TEXT_CAPTURE_POLICY_RETURN_LEDGER_TEMPLATE_20260703T043000Z';
const priorAttributionGapCheck = 'OLP_DMOI_RELATION_FUNCTION_ATTRIBUTION_SCOPE_GAP_CHECK_20260702T134500Z';
const parentArtifacts = [
  parentPolicyReturnLedger,
  priorAttributionGapCheck,
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_RETURN_EVIDENCE_CRITERIA_DECISION_LEDGER_TEMPLATE_20260703T041500Z'
];

const blankNoticeFields = [
  'source_system_id',
  'source_file_or_route',
  'selected_excerpt_id',
  'exact_line_span',
  'source_title_or_edition',
  'source_author_or_project_attribution',
  'source_url_or_repository_route',
  'license_url_or_license_file_route',
  'license_compatibility_note',
  'modification_or_adaptation_notice',
  'attribution_notice_text',
  'notice_placement',
  'reviewer_scope_return_id',
  'owner_or_reviewer_acceptance_note'
];

const noticeFieldDefinitions = [
  ['source_system_id', 'source system has been selected and policy return permits use'],
  ['source_file_or_route', 'source locator policy decision and route scope are available'],
  ['selected_excerpt_id', 'excerpt selection permission and exact span exist'],
  ['exact_line_span', 'line-span selection permission exists'],
  ['source_title_or_edition', 'source identity is pinned for the selected excerpt'],
  ['source_author_or_project_attribution', 'attribution name is confirmed for the selected excerpt'],
  ['source_url_or_repository_route', 'public source route is confirmed'],
  ['license_url_or_license_file_route', 'license route is confirmed'],
  ['license_compatibility_note', 'reuse posture is reviewed'],
  ['modification_or_adaptation_notice', 'quote/adaptation/summary status is reviewed'],
  ['attribution_notice_text', 'notice body is authorized and composed'],
  ['notice_placement', 'destination sidecar or packet placement is selected'],
  ['reviewer_scope_return_id', 'non-personal reviewer-scope return exists'],
  ['owner_or_reviewer_acceptance_note', 'language/surface owner or reviewer acceptance is recorded']
].map(([field_id, required_before_fill]) => ({ field_id, required_before_fill }));

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

function buildNoticeRows(parent) {
  const attributionPolicyRows = parent.source_text_capture_policy_return_rows
    .filter((row) => row.policy_return_class === 'selected_excerpt_attribution_notice_policy_return');
  return attributionPolicyRows.map((row, index) => ({
    selected_excerpt_attribution_notice_template_row_id: `ODRF-SEL-EXC-ATTR-NOTICE-${String(index + 1).padStart(2, '0')}`,
    parent_source_text_capture_policy_return_row_id: row.source_text_capture_policy_return_row_id,
    parent_criteria_decision_packet_unit_summary_row_id: row.parent_criteria_decision_packet_unit_summary_row_id,
    parent_packet_unit: row.parent_packet_unit,
    parent_ledger_row_id: row.parent_ledger_row_id,
    parent_pointer_row_id: row.parent_pointer_row_id,
    parent_policy_return_class: row.policy_return_class,
    inherited_policy_return_received: row.return_received,
    inherited_policy_finalized: row.policy_finalized,
    inherited_source_text_capture_allowed_now: row.source_text_capture_allowed_now,
    inherited_selected_excerpt_attribution_notice_allowed_now: row.selected_excerpt_attribution_notice_allowed_now,
    inherited_exact_line_spans_selected: row.inherited_exact_line_spans_selected,
    inherited_source_prose_copied: row.inherited_source_prose_copied,
    inherited_excerpts_selected: row.inherited_excerpts_selected,
    blank_notice_fields: blankNoticeFields,
    source_system_id: null,
    source_file_or_route: null,
    selected_excerpt_id: null,
    exact_line_span: null,
    source_title_or_edition: null,
    source_author_or_project_attribution: null,
    source_url_or_repository_route: null,
    license_url_or_license_file_route: null,
    license_compatibility_note: null,
    modification_or_adaptation_notice: null,
    attribution_notice_text: null,
    notice_placement: null,
    reviewer_scope_return_id: null,
    owner_or_reviewer_acceptance_note: null,
    notice_fields_filled: 0,
    notice_template_ready_for_fill: false,
    attribution_notice_filled: false,
    attribution_notice_file_created: false,
    excerpt_sidecar_allowed_now: false,
    source_text_capture_allowed_now: false,
    surface_gate_opened: false,
    translation_gate_opened: false,
    still_locked_reason: 'missing_selected_excerpt_attribution_policy_return_exact_span_excerpt_and_reviewer_scope_return'
  }));
}

function buildPacketSummaryRows(noticeRows) {
  return noticeRows.map((row, index) => ({
    selected_excerpt_attribution_notice_packet_summary_row_id: `ODRF-SEL-EXC-ATTR-PACKET-${String(index + 1).padStart(2, '0')}`,
    parent_packet_unit: row.parent_packet_unit,
    linked_notice_template_row_id: row.selected_excerpt_attribution_notice_template_row_id,
    parent_policy_return_row_id: row.parent_source_text_capture_policy_return_row_id,
    notice_template_rows_allocated: 1,
    notice_template_rows_filled: 0,
    blank_notice_field_cells_allocated: blankNoticeFields.length,
    policy_return_received: false,
    exact_line_span_selected: false,
    excerpt_selected: false,
    attribution_notice_filled: false,
    source_text_or_excerpt_file_created: false,
    surface_or_translation_allowed: false
  }));
}

function buildFieldSummaryRows() {
  return noticeFieldDefinitions.map((field, index) => ({
    selected_excerpt_attribution_notice_field_summary_row_id: `ODRF-SEL-EXC-ATTR-FIELD-${String(index + 1).padStart(2, '0')}`,
    field_id: field.field_id,
    required_before_fill: field.required_before_fill,
    template_rows_requiring_field: 10,
    fields_filled: 0,
    field_ready_for_fill: false
  }));
}

function buildArtifact(parent, priorGapCheck) {
  const noticeRows = buildNoticeRows(parent);
  const packetSummaryRows = buildPacketSummaryRows(noticeRows);
  const fieldSummaryRows = buildFieldSummaryRows();
  const blankNoticeFieldCells = noticeRows.length * blankNoticeFields.length;
  const parentGate = parent.gate_state || {};
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_blank_no_excerpts_no_source_text_no_notice_no_surfaces_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Allocate blank selected-excerpt attribution notice template rows for the ten packet units that have attribution-policy return rows in package 137, without filling any source identity, exact span, excerpt, notice text, surface, or translation field.',
    parent_artifacts: parentArtifacts,
    inherited_attribution_gap_vocabulary: {
      source_artifact: priorGapCheck.artifact_id,
      required_gap_fields_per_row: priorGapCheck.gate_state?.required_gap_fields_per_row,
      open_required_gap_cells: priorGapCheck.gate_state?.open_required_gap_cells,
      selected_excerpt_attribution_notices_filled: priorGapCheck.gate_state?.selected_excerpt_attribution_notices_filled
    },
    selected_excerpt_attribution_notice_boundary: {
      template_is: 'blank notice template for future selected-excerpt attribution records',
      template_is_not: [
        'selected excerpt',
        'exact line span',
        'copied source text',
        'license legal advice',
        'filled attribution notice',
        'source text or excerpt sidecar',
        'surface proposal',
        'translation draft',
        'pilot or publication claim'
      ],
      allowed_now: [
        'allocate blank notice fields',
        'link notice templates to the package-137 attribution-policy return rows',
        'record every prerequisite still missing before notice fill',
        'keep all source text, excerpt, notice text, surface, and translation fields empty'
      ],
      blocked_now: [
        'inventing source identity or attribution wording',
        'selecting exact spans or excerpts',
        'copying source prose, examples, definitions, or passages',
        'creating source-text/excerpt sidecar files',
        'accepting local, bridge, or semi-constructed surfaces',
        'opening translation, pilot, or publication gates'
      ]
    },
    blank_notice_fields: blankNoticeFields,
    selected_excerpt_attribution_notice_template_rows: noticeRows,
    packet_unit_selected_excerpt_attribution_notice_summary_rows: packetSummaryRows,
    notice_field_summary_rows: fieldSummaryRows,
    gate_state: {
      selected_excerpt_attribution_notice_template_rows: noticeRows.length,
      packet_unit_selected_excerpt_attribution_notice_summary_rows: packetSummaryRows.length,
      notice_field_summary_rows: fieldSummaryRows.length,
      blank_notice_fields_per_row: blankNoticeFields.length,
      blank_notice_field_cells_allocated: blankNoticeFieldCells,
      inherited_source_text_capture_policy_return_rows: parentGate.source_text_capture_policy_return_rows,
      inherited_source_text_capture_policy_returns_received: parentGate.source_text_capture_policy_returns_received,
      inherited_source_text_capture_policy_return_rows_filled: parentGate.source_text_capture_policy_return_rows_filled,
      inherited_source_text_capture_policies_finalized: parentGate.source_text_capture_policies_finalized,
      inherited_source_text_capture_permissions_granted: parentGate.source_text_capture_permissions_granted,
      inherited_exact_line_spans_selected: parentGate.exact_line_spans_selected,
      inherited_source_text_copied: parentGate.source_text_copied,
      inherited_excerpts_selected: parentGate.excerpts_selected,
      notice_template_rows_filled: 0,
      notice_fields_filled: 0,
      notice_template_rows_ready_for_fill: 0,
      source_system_ids_filled: 0,
      source_file_or_route_fields_filled: 0,
      selected_excerpt_ids_filled: 0,
      exact_line_span_fields_filled: 0,
      source_title_or_edition_fields_filled: 0,
      source_author_or_project_attribution_fields_filled: 0,
      source_url_or_repository_route_fields_filled: 0,
      license_url_or_license_file_route_fields_filled: 0,
      license_compatibility_notes_filled: 0,
      modification_or_adaptation_notices_filled: 0,
      attribution_notice_text_fields_filled: 0,
      notice_placement_fields_filled: 0,
      reviewer_scope_return_ids_filled: 0,
      owner_or_reviewer_acceptance_notes_filled: 0,
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
      evidence_rows_filled: 0,
      evidence_values_reviewed: 0,
      evidence_source_pointers_reviewed: 0,
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
      validator: 'local_node_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_generation_prevalidation_20260703T044500Z',
      zero_gate_assertions: [
        'notice_template_rows_filled',
        'notice_fields_filled',
        'notice_template_rows_ready_for_fill',
        'source_system_ids_filled',
        'source_file_or_route_fields_filled',
        'selected_excerpt_ids_filled',
        'exact_line_span_fields_filled',
        'source_title_or_edition_fields_filled',
        'source_author_or_project_attribution_fields_filled',
        'source_url_or_repository_route_fields_filled',
        'license_url_or_license_file_route_fields_filled',
        'license_compatibility_notes_filled',
        'modification_or_adaptation_notices_filled',
        'attribution_notice_text_fields_filled',
        'notice_placement_fields_filled',
        'reviewer_scope_return_ids_filled',
        'owner_or_reviewer_acceptance_notes_filled',
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
        'evidence_rows_filled',
        'evidence_values_reviewed',
        'evidence_source_pointers_reviewed',
        'reviewer_scope_returns_received',
        'owner_or_reviewer_acceptances_recorded',
        'local_language_surfaces_filled',
        'bridge_surfaces_accepted',
        'semi_constructed_surfaces_accepted',
        'translated_passages'
      ],
      selected_excerpt_attribution_notice_template_rows: noticeRows.length,
      packet_unit_selected_excerpt_attribution_notice_summary_rows: packetSummaryRows.length,
      notice_field_summary_rows: fieldSummaryRows.length,
      blank_notice_fields_per_row: blankNoticeFields.length,
      blank_notice_field_cells_allocated: blankNoticeFieldCells
    },
    next_valid_artifacts: [
      'OLP_DMOI_RELATION_FUNCTION_SOURCE_TEXT_CAPTURE_POLICY_RETURN_LEDGER_WITH_RETURNS_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_PACKET_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_RETURN_EVIDENCE_CRITERIA_DECISION_REVIEW_PACKET_<timestamp>'
    ],
    decision: 'Package 138 creates the blank selected-excerpt attribution notice template promised by package 137 while preserving the absence of policy returns, exact spans, excerpts, source text, notice text, surfaces, translations, and readiness.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const rowLines = artifact.selected_excerpt_attribution_notice_template_rows.map((row) => `| ${row.selected_excerpt_attribution_notice_template_row_id} | ${row.parent_packet_unit} | ${row.parent_source_text_capture_policy_return_row_id} | ${row.blank_notice_fields.length} | ${row.notice_fields_filled} | ${row.attribution_notice_filled} |`).join('\n');
  const fieldLines = artifact.notice_field_summary_rows.map((row) => `| ${row.selected_excerpt_attribution_notice_field_summary_row_id} | ${row.field_id} | ${row.template_rows_requiring_field} | ${row.fields_filled} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: ${artifact.status}

## Purpose

${artifact.purpose}

## Boundary

This is a blank selected-excerpt attribution notice template. It is not a selected excerpt, exact line span, source-text capture, attribution notice, source-text/excerpt sidecar, translation, pilot, publication, commit, push, PR update, or Zenodo action.

## Counts

- Notice template rows: \`${g.selected_excerpt_attribution_notice_template_rows}\`
- Packet-unit summaries: \`${g.packet_unit_selected_excerpt_attribution_notice_summary_rows}\`
- Notice field summaries: \`${g.notice_field_summary_rows}\`
- Blank notice fields per row: \`${g.blank_notice_fields_per_row}\`
- Blank notice-field cells allocated: \`${g.blank_notice_field_cells_allocated}\`
- Filled notice rows/fields/notices: \`${g.notice_template_rows_filled}/${g.notice_fields_filled}/${g.selected_excerpt_attribution_notices_filled}\`
- Exact spans/source text/excerpts/source-text files: \`${g.exact_line_spans_selected}/${g.source_text_copied}/${g.excerpts_selected}/${g.source_text_or_excerpt_files_created}\`
- Surfaces/translations/readiness: \`${g.local_language_surfaces_filled}/${g.translated_passages}/${g.pilot_ready}\`

## Notice Template Rows

| Row | Packet unit | Parent policy row | Blank fields | Filled fields | Notice filled |
| --- | --- | --- | ---: | ---: | --- |
${rowLines}

## Notice Field Summary

| Row | Field | Template rows requiring field | Fields filled |
| --- | --- | ---: | ---: |
${fieldLines}

## Decision

${artifact.decision}
`;
}

function buildArtifactCsv(artifact) {
  const rows = [];
  rows.push(['section', 'row_id', 'packet_or_field', 'parent_id', 'blank_or_required_count', 'filled_count', 'gate_open'].map(csvCell).join(','));
  for (const row of artifact.selected_excerpt_attribution_notice_template_rows) {
    rows.push([
      'selected_excerpt_attribution_notice_template',
      row.selected_excerpt_attribution_notice_template_row_id,
      row.parent_packet_unit,
      row.parent_source_text_capture_policy_return_row_id,
      row.blank_notice_fields.length,
      row.notice_fields_filled,
      row.surface_gate_opened || row.translation_gate_opened
    ].map(csvCell).join(','));
  }
  for (const row of artifact.notice_field_summary_rows) {
    rows.push([
      'notice_field_summary',
      row.selected_excerpt_attribution_notice_field_summary_row_id,
      row.field_id,
      '',
      row.template_rows_requiring_field,
      row.fields_filled,
      row.field_ready_for_fill
    ].map(csvCell).join(','));
  }
  for (const row of artifact.packet_unit_selected_excerpt_attribution_notice_summary_rows) {
    rows.push([
      'packet_unit_summary',
      row.selected_excerpt_attribution_notice_packet_summary_row_id,
      row.parent_packet_unit,
      row.parent_policy_return_row_id,
      row.notice_template_rows_allocated,
      row.notice_template_rows_filled,
      row.surface_or_translation_allowed
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
    status: 'pointer_only_selected_excerpt_attribution_notice_template_note_no_upload_claim_no_remote_state_claim',
    purpose: 'Record package-138 OLP/DMOI relation-function selected-excerpt attribution notice template continuation while preserving no-excerpt/no-source-text/no-notice/no-translation boundaries.',
    points_to_artifacts: [
      `${artifactId}.json`,
      `${artifactId}.md`,
      `${artifactId}.csv`,
      `${artifactId}.sha256`
    ],
    summary: {
      selected_excerpt_attribution_notice_template_rows: g.selected_excerpt_attribution_notice_template_rows,
      notice_field_summary_rows: g.notice_field_summary_rows,
      blank_notice_field_cells_allocated: g.blank_notice_field_cells_allocated,
      notice_template_rows_filled: g.notice_template_rows_filled,
      notice_fields_filled: g.notice_fields_filled,
      selected_excerpt_attribution_notices_filled: g.selected_excerpt_attribution_notices_filled,
      source_text_or_excerpt_files_created: g.source_text_or_excerpt_files_created,
      exact_line_spans_selected: g.exact_line_spans_selected,
      source_text_copied: g.source_text_copied,
      excerpts_selected: g.excerpts_selected,
      surfaces_or_translations: g.local_language_surfaces_filled + g.bridge_surfaces_accepted + g.semi_constructed_surfaces_accepted + g.translated_passages,
      readiness_claims: Number(g.publication_ready) + Number(g.translation_ready) + Number(g.constructed_surface_ready) + Number(g.pilot_ready)
    },
    boundary: 'Pointer-only coordination note. No policy return, permission grant, exact line span, selected excerpt, source text, attribution notice text, source-text/excerpt sidecar, surface, translation, pilot, publication, commit, push, PR update, or Zenodo action is claimed.',
    upload_intent: 'Queue the package-138 JSON/MD/CSV/checksum and this note for the existing Noether upload path as substantive coordination material; user clarified on 2026-07-03 that substantive artifacts should not be deferred because of mobile-plan or bandwidth wording.',
    message_template: `Package 138 added ${artifactId}: 10 blank selected-excerpt attribution notice template rows, 14 notice field summaries, 140 blank notice-field cells, 0 filled notice fields, 0 exact spans, 0 source text, 0 excerpts, 0 attribution notices, 0 source-text/excerpt files, 0 surfaces/translations, 0 readiness.`
  };
}

function buildNoteMd(note) {
  return `# Package 138 Coordination Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${note.source_artifact}\`

Generated UTC: \`${note.generated_utc}\`

## Summary

- Notice template rows: \`${note.summary.selected_excerpt_attribution_notice_template_rows}\`
- Notice field summaries: \`${note.summary.notice_field_summary_rows}\`
- Blank notice-field cells allocated: \`${note.summary.blank_notice_field_cells_allocated}\`
- Filled notice rows/fields/notices: \`${note.summary.notice_template_rows_filled}/${note.summary.notice_fields_filled}/${note.summary.selected_excerpt_attribution_notices_filled}\`
- Exact spans/source text/excerpts/source-text files: \`${note.summary.exact_line_spans_selected}/${note.summary.source_text_copied}/${note.summary.excerpts_selected}/${note.summary.source_text_or_excerpt_files_created}\`
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
      role: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_support',
      artifact: artifactId,
      current_use: '10 blank selected-excerpt attribution notice template rows; 14 notice fields per row; 140 blank notice-field cells; 0 filled notices, 0 exact spans, 0 source text, 0 excerpts, 0 source-text/excerpt files, 0 surfaces, 0 translation, 0 readiness'
    });
  }
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_rows: g.selected_excerpt_attribution_notice_template_rows,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_blank_cells: g.blank_notice_field_cells_allocated,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_fields_filled: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notices_filled: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_files_created: 0,
    current_olp_dmoi_relation_function_source_text_or_excerpt_files_created: 0,
    current_olp_dmoi_relation_function_exact_line_spans_selected_after_attribution_notice_template: 0,
    current_olp_dmoi_relation_function_source_text_copied_after_attribution_notice_template: 0,
    current_olp_dmoi_relation_function_excerpts_selected_after_attribution_notice_template: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_policy_returns_or_review_packet_only_no_notice_fill_no_source_text_no_excerpt_no_surfaces_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'OLP/DMOI relation-function selected-excerpt attribution notice template',
    route: artifactId,
    license_status_to_recheck: 'blank_notice_template_only_no_policy_returns_no_exact_spans_no_source_text_no_excerpts_no_attribution_notice_no_translation',
    best_translation_use: 'future selected-excerpt attribution notice intake before any source-text/excerpt sidecar, surface, or translation',
    candidate_lanes: [
      'olp_dmoi_relation_function_attribution_notice_lane',
      'blank_selected_excerpt_attribution_notice_template',
      'review_only_construction_scaffold',
      'source_aware_excerpt_governance'
    ],
    priority: 1,
    status: 'blank_selected_excerpt_attribution_notice_template_no_excerpts_no_source_text_no_notice_no_translation',
    gate_state: {
      selected_excerpt_attribution_notice_template_rows: g.selected_excerpt_attribution_notice_template_rows,
      blank_notice_field_cells_allocated: g.blank_notice_field_cells_allocated,
      notice_fields_filled: 0,
      selected_excerpt_attribution_notices_filled: 0,
      source_text_or_excerpt_files_created: 0,
      exact_line_spans_selected: 0,
      source_text_copied: 0,
      excerpts_selected: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template: ${artifactId}_10_blank_notice_rows_140_blank_cells_0_notice_fields_0_exact_spans_0_source_text_0_excerpts_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_rows: g.selected_excerpt_attribution_notice_template_rows,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_blank_cells: g.blank_notice_field_cells_allocated,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_fields_filled: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notices_filled: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_files_created: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_source_text_or_excerpt_files: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_surfaces: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_translations: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template: ${artifactId}_blank_notice_template_only_no_exact_spans_no_source_text_no_excerpts_no_notices_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates 10 blank selected-excerpt attribution notice template rows and 140 blank notice-field cells after package 137; 0 filled notice fields, 0 policy returns, 0 exact spans, 0 source text, 0 excerpts, 0 attribution notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, 0 readiness; substantive artifacts should be uploaded when a staging path exists.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OLP/DMOI relation-function selected-excerpt attribution notice template; 10 blank notice rows, 140 blank cells, 0 exact spans, 0 source text, 0 excerpts, 0 attribution notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 138: OLP/DMOI relation-function selected-excerpt attribution notice template after package 137. It records 10 blank notice template rows, 14 notice field summaries, and 140 blank notice-field cells while keeping 0 notice fields filled, 0 exact spans, 0 source text, 0 excerpts, 0 attribution notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | OLP/DMOI relation-function selected-excerpt attribution notice template | ${artifactId} | Selected-excerpt attribution notice scaffold; 10 blank notice rows, 140 blank cells, 0 exact spans, 0 source text, 0 excerpts, 0 notices, no source-text/excerpt files, no surface, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_artifact: \`${artifactId}\` (10 blank notice rows; 140 blank notice cells; 0 exact spans; 0 source text; 0 excerpts; no attribution notices, surfaces, or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template: \`${artifactId}\`; blank attribution-notice template only, no exact spans, source text, excerpts, notices, accepted surfaces, or translation.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OLP/DMOI relation-function selected-excerpt attribution notice template; blank notice rows are not exact spans, copied source text, selected excerpts, attribution notices, source-text/excerpt sidecars, surfaces, translations, or readiness.`);
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
    { filename: `${artifactId}.json`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template' },
    { filename: `${artifactId}.md`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template' },
    { filename: `${artifactId}.csv`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'olp_dmoi_relation_function_package138_coordination_note' },
    { filename: `${noteId}.md`, class: 'olp_dmoi_relation_function_package138_coordination_note' },
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
  upload.obj.package138_upload_queue_update = {
    captured_utc: '2026-07-03T04:47:00Z',
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
  const step = 'Stage package 138 OLP/DMOI relation-function selected-excerpt attribution notice-template artifacts with this queue as substantive coordination material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (artifact.selected_excerpt_attribution_notice_template_rows.length !== 10) failures.push(`notice_rows_not_10_${artifact.selected_excerpt_attribution_notice_template_rows.length}`);
  if (artifact.packet_unit_selected_excerpt_attribution_notice_summary_rows.length !== 10) failures.push(`packet_summary_rows_not_10_${artifact.packet_unit_selected_excerpt_attribution_notice_summary_rows.length}`);
  if (artifact.notice_field_summary_rows.length !== blankNoticeFields.length) failures.push(`field_summary_rows_not_${blankNoticeFields.length}_${artifact.notice_field_summary_rows.length}`);
  if (g.blank_notice_fields_per_row !== blankNoticeFields.length) failures.push(`blank_notice_fields_per_row_not_${blankNoticeFields.length}_${g.blank_notice_fields_per_row}`);
  if (g.blank_notice_field_cells_allocated !== 10 * blankNoticeFields.length) failures.push(`blank_notice_cells_mismatch_${g.blank_notice_field_cells_allocated}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.selected_excerpt_attribution_notice_template_rows) {
    const filled = blankNoticeFields.some((field) => row[field] !== null);
    if (filled || row.notice_fields_filled !== 0 || row.notice_template_ready_for_fill || row.attribution_notice_filled || row.attribution_notice_file_created || row.excerpt_sidecar_allowed_now || row.source_text_capture_allowed_now || row.surface_gate_opened || row.translation_gate_opened) {
      failures.push(`nonblank_notice_template_row_${row.selected_excerpt_attribution_notice_template_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const parent = (await readJson(parentPolicyReturnLedger)).obj;
const priorGapCheck = (await readJson(priorAttributionGapCheck)).obj;
const artifact = buildArtifact(parent, priorGapCheck);
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
  selected_excerpt_attribution_notice_template_rows: artifact.gate_state.selected_excerpt_attribution_notice_template_rows,
  notice_field_summary_rows: artifact.gate_state.notice_field_summary_rows,
  blank_notice_fields_per_row: artifact.gate_state.blank_notice_fields_per_row,
  blank_notice_field_cells_allocated: artifact.gate_state.blank_notice_field_cells_allocated,
  notice_fields_filled: artifact.gate_state.notice_fields_filled,
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
