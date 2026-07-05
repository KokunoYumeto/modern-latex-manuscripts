import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OLP_DMOI_RELATION_FUNCTION_SOURCE_TEXT_CAPTURE_POLICY_RETURN_LEDGER_TEMPLATE_20260703T043000Z';
const noteId = 'OLP_DMOI_RELATION_FUNCTION_SOURCE_TEXT_CAPTURE_POLICY_RETURN_LEDGER_TEMPLATE_NOTE_20260703T043100Z';
const generatedUtc = '2026-07-03T04:30:00Z';
const noteGeneratedUtc = '2026-07-03T04:31:00Z';
const packageOrder = 137;
const queueCandidateId = 'OTCQ-OLP-DMOI-RELATION-FUNCTION-SOURCE-TEXT-CAPTURE-POLICY-RETURN-LEDGER-TEMPLATE-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentCriteriaDecision = 'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_RETURN_EVIDENCE_CRITERIA_DECISION_LEDGER_TEMPLATE_20260703T041500Z';

const parentArtifacts = [
  parentCriteriaDecision,
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_RETURN_EVIDENCE_INTAKE_LEDGER_TEMPLATE_20260703T040000Z',
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_RETURN_EVIDENCE_CRITERIA_RUBRIC_20260703T034500Z'
];

const blankReturnFields = [
  'return_date',
  'return_authority_role',
  'non_personal_policy_route_or_owner_id',
  'source_locator_policy_decision',
  'candidate_line_range_policy_decision',
  'exact_line_span_selection_policy_decision',
  'source_text_capture_policy_decision',
  'excerpt_selection_policy_decision',
  'attribution_notice_requirement',
  'license_or_terms_note',
  'privacy_review_note',
  'next_allowed_artifact'
];

const policyClasses = [
  {
    policy_class: 'source_locator_permission_route_policy_return',
    label: 'Source locator permission route policy return',
    required_before: [
      'source_system_decision_recording',
      'source_locator_selection',
      'candidate_range_capture'
    ],
    specific_blank_fields: [
      'source_locator_policy_decision',
      'non_personal_policy_route_or_owner_id',
      'license_or_terms_note'
    ]
  },
  {
    policy_class: 'candidate_line_range_selection_policy_return',
    label: 'Candidate line-range selection policy return',
    required_before: [
      'candidate_line_range_selection',
      'exact_line_span_selection',
      'source_passage_selection'
    ],
    specific_blank_fields: [
      'candidate_line_range_policy_decision',
      'exact_line_span_selection_policy_decision',
      'privacy_review_note'
    ]
  },
  {
    policy_class: 'source_text_capture_policy_return',
    label: 'Source text capture policy return',
    required_before: [
      'source_text_capture',
      'source_prose_copying',
      'source_example_copying'
    ],
    specific_blank_fields: [
      'source_text_capture_policy_decision',
      'license_or_terms_note',
      'privacy_review_note'
    ]
  },
  {
    policy_class: 'selected_excerpt_attribution_notice_policy_return',
    label: 'Selected excerpt attribution notice policy return',
    required_before: [
      'selected_excerpt_attribution_notice',
      'excerpt_sidecar',
      'surface_or_translation_sidecar'
    ],
    specific_blank_fields: [
      'excerpt_selection_policy_decision',
      'attribution_notice_requirement',
      'next_allowed_artifact'
    ]
  }
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
  const packetRows = parent.packet_unit_criteria_decision_summary_rows || [];
  const rows = [];
  for (const packet of packetRows) {
    for (const policy of policyClasses) {
      const index = rows.length + 1;
      rows.push({
        source_text_capture_policy_return_row_id: `ODRF-SRC-CAP-POL-RETURN-${String(index).padStart(3, '0')}`,
        parent_criteria_decision_packet_unit_summary_row_id: packet.criteria_decision_packet_unit_summary_row_id,
        parent_packet_unit: packet.packet_unit,
        parent_ledger_row_id: packet.parent_ledger_row_id,
        parent_pointer_row_id: packet.parent_pointer_row_id,
        policy_return_class: policy.policy_class,
        policy_return_label: policy.label,
        policy_return_required_before: policy.required_before,
        blank_return_fields: blankReturnFields,
        policy_specific_blank_fields: policy.specific_blank_fields,
        inherited_criteria_decision_rows_required: packet.criteria_decision_rows_required,
        inherited_criteria_decision_rows_unfilled: packet.criteria_rows_unfilled,
        inherited_permission_returns_received: packet.permission_returns_received,
        inherited_line_span_candidate_permissions_recorded: packet.line_span_candidate_permissions_recorded,
        inherited_source_text_capture_permissions_recorded: packet.source_text_capture_permissions_recorded,
        inherited_exact_line_spans_selected: packet.exact_line_spans_selected,
        inherited_source_prose_copied: packet.source_prose_copied,
        inherited_excerpts_selected: packet.excerpts_selected,
        return_received: false,
        return_date: null,
        return_authority_role: null,
        non_personal_policy_route_or_owner_id: null,
        source_locator_policy_decision: null,
        candidate_line_range_policy_decision: null,
        exact_line_span_selection_policy_decision: null,
        source_text_capture_policy_decision: null,
        excerpt_selection_policy_decision: null,
        attribution_notice_requirement: null,
        license_or_terms_note: null,
        privacy_review_note: null,
        next_allowed_artifact: null,
        policy_finalized: false,
        source_locator_decision_allowed_now: false,
        candidate_line_range_selection_allowed_now: false,
        exact_line_span_selection_allowed_now: false,
        source_text_capture_allowed_now: false,
        selected_excerpt_attribution_notice_allowed_now: false,
        evidence_intake_allowed_now: false,
        surface_gate_opened: false,
        translation_gate_opened: false,
        still_locked_reason: 'missing_dated_non_personal_source_text_capture_policy_return'
      });
    }
  }
  return rows;
}

function buildPacketSummaryRows(parent, returnRows) {
  const rowsByPacket = new Map();
  for (const row of returnRows) {
    if (!rowsByPacket.has(row.parent_packet_unit)) rowsByPacket.set(row.parent_packet_unit, []);
    rowsByPacket.get(row.parent_packet_unit).push(row);
  }
  return (parent.packet_unit_criteria_decision_summary_rows || []).map((packet, index) => {
    const rows = rowsByPacket.get(packet.packet_unit) || [];
    return {
      source_text_capture_policy_packet_summary_row_id: `ODRF-SRC-CAP-POL-PACKET-${String(index + 1).padStart(2, '0')}`,
      parent_criteria_decision_packet_unit_summary_row_id: packet.criteria_decision_packet_unit_summary_row_id,
      packet_unit: packet.packet_unit,
      parent_ledger_row_id: packet.parent_ledger_row_id,
      parent_pointer_row_id: packet.parent_pointer_row_id,
      policy_return_rows_required: rows.length,
      policy_return_rows_received: 0,
      blank_return_field_cells_allocated: rows.length * blankReturnFields.length,
      inherited_criteria_decision_rows_required: packet.criteria_decision_rows_required,
      inherited_criteria_decision_rows_unfilled: packet.criteria_rows_unfilled,
      inherited_returns_received: packet.returns_received,
      inherited_blockers_resolved: packet.blockers_resolved,
      inherited_permission_returns_received: packet.permission_returns_received,
      inherited_source_text_capture_permissions_recorded: packet.source_text_capture_permissions_recorded,
      inherited_exact_line_spans_selected: packet.exact_line_spans_selected,
      inherited_source_prose_copied: packet.source_prose_copied,
      inherited_excerpts_selected: packet.excerpts_selected,
      source_text_capture_policy_readiness: 'not_ready_return_ledger_blank_only',
      first_missing_requirement: 'dated_non_personal_source_text_capture_policy_return',
      source_text_capture_allowed_now: false,
      excerpt_notice_allowed_now: false,
      surface_allowed: false,
      translation_allowed: false,
      linked_source_text_capture_policy_return_row_ids: rows.map((row) => row.source_text_capture_policy_return_row_id)
    };
  });
}

function buildPolicyClassSummaryRows(returnRows) {
  return policyClasses.map((policy, index) => {
    const rows = returnRows.filter((row) => row.policy_return_class === policy.policy_class);
    return {
      source_text_capture_policy_class_summary_row_id: `ODRF-SRC-CAP-POL-CLASS-${String(index + 1).padStart(2, '0')}`,
      policy_return_class: policy.policy_class,
      policy_return_label: policy.label,
      policy_return_rows_required: rows.length,
      policy_return_rows_received: 0,
      blank_return_field_cells_allocated: rows.length * blankReturnFields.length,
      required_before: policy.required_before,
      return_decisions_filled: 0,
      policies_finalized: 0,
      downstream_gate_opened: false,
      linked_source_text_capture_policy_return_row_ids: rows.map((row) => row.source_text_capture_policy_return_row_id)
    };
  });
}

function buildArtifact(parent) {
  const returnRows = buildReturnRows(parent);
  const packetSummaryRows = buildPacketSummaryRows(parent, returnRows);
  const policyClassSummaryRows = buildPolicyClassSummaryRows(returnRows);
  const blankReturnFieldCells = returnRows.length * blankReturnFields.length;
  const parentGate = parent.gate_state || {};
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'olp_dmoi_relation_function_source_text_capture_policy_return_ledger_template_blank_no_policy_returns_no_source_text_no_excerpts_no_surfaces_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Allocate a blank source-text capture policy return ledger after package 136 so future dated non-personal policy returns have a fixed place to land before any source locator, line span, source text, excerpt, attribution notice, surface, or translation work.',
    parent_artifacts: parentArtifacts,
    source_text_capture_policy_boundary: {
      ledger_template_is: 'blank future return ledger for source-text capture policy decisions',
      ledger_template_is_not: [
        'received policy return',
        'permission grant',
        'source locator decision',
        'candidate line-range selection',
        'exact line-span selection',
        'source text capture',
        'selected excerpt attribution notice',
        'surface proposal',
        'translation draft',
        'pilot or publication claim'
      ],
      allowed_now: [
        'allocate blank policy return rows by packet unit and policy class',
        'record which downstream actions remain locked',
        'preserve the user clarification that substantive queued artifacts should be uploaded when a staging path exists',
        'keep source text, excerpt, attribution notice, surface, and translation fields empty'
      ],
      blocked_now: [
        'inventing policy returns',
        'granting source text capture permission',
        'selecting exact spans or excerpts',
        'copying source prose, definitions, examples, or passages',
        'filling attribution notices',
        'opening surface, translation, pilot, or publication gates'
      ]
    },
    blank_return_fields: blankReturnFields,
    source_text_capture_policy_return_rows: returnRows,
    packet_unit_source_text_capture_policy_summary_rows: packetSummaryRows,
    policy_class_source_text_capture_policy_summary_rows: policyClassSummaryRows,
    gate_state: {
      source_text_capture_policy_return_rows: returnRows.length,
      packet_unit_source_text_capture_policy_summary_rows: packetSummaryRows.length,
      policy_class_source_text_capture_policy_summary_rows: policyClassSummaryRows.length,
      blank_return_fields_per_row: blankReturnFields.length,
      blank_return_field_cells_allocated: blankReturnFieldCells,
      inherited_criteria_decision_rows: parentGate.criteria_decision_rows,
      inherited_criteria_rows_unfilled: parentGate.criteria_rows_unfilled,
      inherited_decision_fields_filled: parentGate.decision_fields_filled,
      inherited_criteria_decisions_recorded: parentGate.criteria_decisions_recorded,
      inherited_evidence_values_reviewed: parentGate.evidence_values_reviewed,
      inherited_evidence_source_pointers_reviewed: parentGate.evidence_source_pointers_reviewed,
      inherited_returns_received: parentGate.returns_received,
      inherited_blockers_resolved: parentGate.blockers_resolved,
      inherited_permission_returns_received: parentGate.permission_returns_received,
      source_text_capture_policy_returns_received: 0,
      source_text_capture_policy_return_rows_filled: 0,
      source_text_capture_policy_return_fields_filled: 0,
      source_text_capture_policies_finalized: 0,
      source_locator_policy_decisions_filled: 0,
      candidate_line_range_policy_decisions_filled: 0,
      exact_line_span_selection_policy_decisions_filled: 0,
      source_text_capture_policy_decisions_filled: 0,
      excerpt_selection_policy_decisions_filled: 0,
      attribution_notice_requirements_filled: 0,
      license_or_terms_notes_filled: 0,
      privacy_review_notes_filled: 0,
      next_allowed_artifacts_filled: 0,
      source_system_decisions_recorded: 0,
      scope_decisions_recorded: 0,
      route_scope_notes_recorded: 0,
      source_locator_permissions_granted: 0,
      line_span_selection_permissions_granted: 0,
      source_text_capture_permissions_granted: 0,
      excerpt_permissions_granted: 0,
      line_span_candidate_permissions_recorded: 0,
      source_text_capture_permissions_recorded: 0,
      exact_line_spans_selected: 0,
      candidate_line_ranges_selected: 0,
      source_locator_rows_selected: 0,
      source_prose_copied: 0,
      source_examples_copied: 0,
      source_passages_selected: 0,
      source_text_copied: 0,
      excerpts_selected: 0,
      selected_excerpt_attribution_notices_filled: 0,
      selected_excerpt_attribution_notice_files_created: 0,
      source_text_or_excerpt_files_created: 0,
      evidence_rows_filled: 0,
      evidence_values_reviewed: 0,
      evidence_source_pointers_reviewed: 0,
      returns_received: 0,
      returns_ingested: 0,
      blockers_resolved: 0,
      true_precondition_cells: 0,
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
      validator: 'local_node_olp_dmoi_relation_function_source_text_capture_policy_return_ledger_template_generation_prevalidation_20260703T043000Z',
      zero_gate_assertions: [
        'source_text_capture_policy_returns_received',
        'source_text_capture_policy_return_rows_filled',
        'source_text_capture_policy_return_fields_filled',
        'source_text_capture_policies_finalized',
        'source_locator_policy_decisions_filled',
        'candidate_line_range_policy_decisions_filled',
        'exact_line_span_selection_policy_decisions_filled',
        'source_text_capture_policy_decisions_filled',
        'excerpt_selection_policy_decisions_filled',
        'attribution_notice_requirements_filled',
        'license_or_terms_notes_filled',
        'privacy_review_notes_filled',
        'next_allowed_artifacts_filled',
        'source_system_decisions_recorded',
        'scope_decisions_recorded',
        'route_scope_notes_recorded',
        'source_locator_permissions_granted',
        'line_span_selection_permissions_granted',
        'source_text_capture_permissions_granted',
        'excerpt_permissions_granted',
        'line_span_candidate_permissions_recorded',
        'source_text_capture_permissions_recorded',
        'exact_line_spans_selected',
        'candidate_line_ranges_selected',
        'source_locator_rows_selected',
        'source_prose_copied',
        'source_examples_copied',
        'source_passages_selected',
        'source_text_copied',
        'excerpts_selected',
        'selected_excerpt_attribution_notices_filled',
        'selected_excerpt_attribution_notice_files_created',
        'source_text_or_excerpt_files_created',
        'evidence_rows_filled',
        'evidence_values_reviewed',
        'evidence_source_pointers_reviewed',
        'returns_received',
        'returns_ingested',
        'blockers_resolved',
        'true_precondition_cells',
        'local_language_surfaces_filled',
        'bridge_surfaces_accepted',
        'semi_constructed_surfaces_accepted',
        'translated_passages'
      ],
      source_text_capture_policy_return_rows: returnRows.length,
      packet_unit_source_text_capture_policy_summary_rows: packetSummaryRows.length,
      policy_class_source_text_capture_policy_summary_rows: policyClassSummaryRows.length,
      blank_return_fields_per_row: blankReturnFields.length,
      blank_return_field_cells_allocated: blankReturnFieldCells
    },
    next_valid_artifacts: [
      'OLP_DMOI_RELATION_FUNCTION_SOURCE_TEXT_CAPTURE_POLICY_RETURN_LEDGER_WITH_RETURNS_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_RETURN_EVIDENCE_CRITERIA_DECISION_REVIEW_PACKET_<timestamp>'
    ],
    decision: 'Package 137 turns the package-136 next-valid source-text policy path into a blank policy return ledger. It keeps all source locator, exact-span, source-text, excerpt, attribution, surface, translation, pilot, and publication gates closed.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const policyRows = artifact.policy_class_source_text_capture_policy_summary_rows.map((row) => `| ${row.source_text_capture_policy_class_summary_row_id} | ${row.policy_return_class} | ${row.policy_return_rows_required} | ${row.policy_return_rows_received} | ${row.blank_return_field_cells_allocated} |`).join('\n');
  const packetRows = artifact.packet_unit_source_text_capture_policy_summary_rows.map((row) => `| ${row.source_text_capture_policy_packet_summary_row_id} | ${row.packet_unit} | ${row.policy_return_rows_required} | ${row.policy_return_rows_received} | ${row.source_text_capture_policy_readiness} |`).join('\n');
  const returnRows = artifact.source_text_capture_policy_return_rows.map((row) => `| ${row.source_text_capture_policy_return_row_id} | ${row.parent_packet_unit} | ${row.policy_return_class} | ${row.blank_return_fields.length} | ${row.return_received} | ${row.source_text_capture_allowed_now} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: ${artifact.status}

## Purpose

${artifact.purpose}

## Boundary

This is a blank source-text capture policy return ledger. It is not a received return, permission grant, source locator decision, candidate range, exact line span, copied source text, selected excerpt, attribution notice, surface, translation, pilot, publication, commit, push, PR update, or Zenodo action.

## Counts

- Source-text capture policy return rows: \`${g.source_text_capture_policy_return_rows}\`
- Packet-unit summaries: \`${g.packet_unit_source_text_capture_policy_summary_rows}\`
- Policy-class summaries: \`${g.policy_class_source_text_capture_policy_summary_rows}\`
- Blank return fields per row: \`${g.blank_return_fields_per_row}\`
- Blank return-field cells allocated: \`${g.blank_return_field_cells_allocated}\`
- Policy returns/finalized policies: \`${g.source_text_capture_policy_returns_received}/${g.source_text_capture_policies_finalized}\`
- Source locators/exact spans/source text/excerpts/attribution notices: \`${g.source_locator_rows_selected}/${g.exact_line_spans_selected}/${g.source_text_copied}/${g.excerpts_selected}/${g.selected_excerpt_attribution_notices_filled}\`
- Surfaces/translations/readiness: \`${g.local_language_surfaces_filled}/${g.translated_passages}/${g.pilot_ready}\`

## Policy Class Summary

| Row | Policy class | Rows required | Returns received | Blank cells |
| --- | --- | ---: | ---: | ---: |
${policyRows}

## Packet Unit Summary

| Row | Packet unit | Rows required | Returns received | Readiness |
| --- | --- | ---: | ---: | --- |
${packetRows}

## Return Rows

| Row | Packet unit | Policy class | Blank fields | Return received | Source text capture allowed |
| --- | --- | --- | ---: | --- | --- |
${returnRows}

## Decision

${artifact.decision}
`;
}

function buildArtifactCsv(artifact) {
  const rows = [];
  rows.push(['section', 'row_id', 'packet_or_policy_class', 'parent_id', 'rows_required_or_blank_fields', 'returns_received', 'downstream_gate_open'].map(csvCell).join(','));
  for (const row of artifact.policy_class_source_text_capture_policy_summary_rows) {
    rows.push([
      'policy_class_summary',
      row.source_text_capture_policy_class_summary_row_id,
      row.policy_return_class,
      '',
      row.policy_return_rows_required,
      row.policy_return_rows_received,
      row.downstream_gate_opened
    ].map(csvCell).join(','));
  }
  for (const row of artifact.packet_unit_source_text_capture_policy_summary_rows) {
    rows.push([
      'packet_unit_summary',
      row.source_text_capture_policy_packet_summary_row_id,
      row.packet_unit,
      row.parent_criteria_decision_packet_unit_summary_row_id,
      row.policy_return_rows_required,
      row.policy_return_rows_received,
      row.source_text_capture_allowed_now
    ].map(csvCell).join(','));
  }
  for (const row of artifact.source_text_capture_policy_return_rows) {
    rows.push([
      'source_text_capture_policy_return',
      row.source_text_capture_policy_return_row_id,
      row.policy_return_class,
      row.parent_criteria_decision_packet_unit_summary_row_id,
      row.blank_return_fields.join('; '),
      row.return_received,
      row.source_text_capture_allowed_now || row.surface_gate_opened || row.translation_gate_opened
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
    status: 'pointer_only_source_text_capture_policy_return_ledger_template_note_no_upload_claim_no_remote_state_claim',
    purpose: 'Record package-137 OLP/DMOI relation-function source-text capture policy return continuation while preserving no-return/no-permission/no-source-text/no-excerpt/no-translation boundaries.',
    points_to_artifacts: [
      `${artifactId}.json`,
      `${artifactId}.md`,
      `${artifactId}.csv`,
      `${artifactId}.sha256`
    ],
    summary: {
      source_text_capture_policy_return_rows: g.source_text_capture_policy_return_rows,
      packet_unit_summary_rows: g.packet_unit_source_text_capture_policy_summary_rows,
      policy_class_summary_rows: g.policy_class_source_text_capture_policy_summary_rows,
      blank_return_field_cells_allocated: g.blank_return_field_cells_allocated,
      source_text_capture_policy_returns_received: g.source_text_capture_policy_returns_received,
      source_text_capture_policies_finalized: g.source_text_capture_policies_finalized,
      source_locator_permissions_granted: g.source_locator_permissions_granted,
      source_text_capture_permissions_granted: g.source_text_capture_permissions_granted,
      exact_line_spans_selected: g.exact_line_spans_selected,
      source_text_copied: g.source_text_copied,
      excerpts_selected: g.excerpts_selected,
      attribution_notices_filled: g.selected_excerpt_attribution_notices_filled,
      source_text_or_excerpt_files_created: g.source_text_or_excerpt_files_created,
      surfaces_or_translations: g.local_language_surfaces_filled + g.bridge_surfaces_accepted + g.semi_constructed_surfaces_accepted + g.translated_passages,
      readiness_claims: Number(g.publication_ready) + Number(g.translation_ready) + Number(g.constructed_surface_ready) + Number(g.pilot_ready)
    },
    boundary: 'Pointer-only coordination note. No policy return, permission grant, source locator, exact line span, source text, excerpt, attribution notice, surface, translation, pilot, publication, commit, push, PR update, or Zenodo action is claimed.',
    upload_intent: 'Queue the package-137 JSON/MD/CSV/checksum and this note for the existing Noether upload path as substantive coordination material; user clarified on 2026-07-03 that substantive artifacts should not be deferred because of mobile-plan or bandwidth wording.',
    message_template: `Package 137 added ${artifactId}: 40 blank source-text capture policy return rows, 10 packet-unit summaries, 4 policy-class summaries, 480 blank return-field cells, 0 returns, 0 permissions, 0 source locators, 0 exact spans, 0 source text, 0 excerpts, 0 attribution notices, 0 surfaces/translations, 0 readiness.`
  };
}

function buildNoteMd(note) {
  return `# Package 137 Coordination Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${note.source_artifact}\`

Generated UTC: \`${note.generated_utc}\`

## Summary

- Source-text capture policy return rows: \`${note.summary.source_text_capture_policy_return_rows}\`
- Packet-unit summaries: \`${note.summary.packet_unit_summary_rows}\`
- Policy-class summaries: \`${note.summary.policy_class_summary_rows}\`
- Blank return-field cells allocated: \`${note.summary.blank_return_field_cells_allocated}\`
- Policy returns/finalized policies: \`${note.summary.source_text_capture_policy_returns_received}/${note.summary.source_text_capture_policies_finalized}\`
- Permissions/source locators/exact spans/source text/excerpts/attribution notices: \`${note.summary.source_text_capture_permissions_granted}/${note.summary.source_locator_permissions_granted}/${note.summary.exact_line_spans_selected}/${note.summary.source_text_copied}/${note.summary.excerpts_selected}/${note.summary.attribution_notices_filled}\`
- Source-text or excerpt files created: \`${note.summary.source_text_or_excerpt_files_created}\`
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
      role: 'olp_dmoi_relation_function_source_text_capture_policy_return_ledger_template_support',
      artifact: artifactId,
      current_use: '40 blank source-text capture policy return rows; 10 packet-unit summaries; 4 policy-class summaries; 480 blank return-field cells; 0 returns, 0 finalized policies, 0 permissions, 0 source locators, 0 exact spans, 0 source text, 0 excerpts, 0 attribution notices, 0 surfaces, 0 translation, 0 readiness'
    });
  }
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_olp_dmoi_relation_function_source_text_capture_policy_return_ledger_template = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_olp_dmoi_relation_function_source_text_capture_policy_return_rows: g.source_text_capture_policy_return_rows,
    current_olp_dmoi_relation_function_source_text_capture_policy_packet_summaries: g.packet_unit_source_text_capture_policy_summary_rows,
    current_olp_dmoi_relation_function_source_text_capture_policy_class_summaries: g.policy_class_source_text_capture_policy_summary_rows,
    current_olp_dmoi_relation_function_source_text_capture_policy_blank_cells: g.blank_return_field_cells_allocated,
    current_olp_dmoi_relation_function_source_text_capture_policy_returns_received: 0,
    current_olp_dmoi_relation_function_source_text_capture_policy_finalized: 0,
    current_olp_dmoi_relation_function_source_text_permissions_granted: 0,
    current_olp_dmoi_relation_function_exact_line_spans_selected: 0,
    current_olp_dmoi_relation_function_source_text_copied: 0,
    current_olp_dmoi_relation_function_excerpts_selected: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notices: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_dated_non_personal_source_text_capture_policy_returns_or_selected_excerpt_attribution_notice_template_only_no_source_text_no_excerpt_no_surfaces_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'OLP/DMOI relation-function source-text capture policy return ledger template',
    route: artifactId,
    license_status_to_recheck: 'blank_policy_return_ledger_only_no_returns_no_permission_grants_no_source_text_no_excerpts_no_surfaces_no_translation',
    best_translation_use: 'future dated non-personal source-text capture policy return intake before source locators, exact spans, excerpts, attribution notices, surfaces, or translations',
    candidate_lanes: [
      'olp_dmoi_relation_function_source_text_policy_lane',
      'blank_source_text_capture_policy_return_ledger',
      'selected_excerpt_attribution_notice_prerequisite_lane',
      'review_only_construction_scaffold'
    ],
    priority: 1,
    status: 'blank_source_text_capture_policy_return_ledger_no_returns_no_permissions_no_source_text_no_excerpts_no_translation',
    gate_state: {
      source_text_capture_policy_return_rows: g.source_text_capture_policy_return_rows,
      blank_return_field_cells_allocated: g.blank_return_field_cells_allocated,
      source_text_capture_policy_returns_received: 0,
      source_text_capture_policies_finalized: 0,
      source_text_capture_permissions_granted: 0,
      source_text_copied: 0,
      excerpts_selected: 0,
      selected_excerpt_attribution_notices_filled: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_source_text_capture_policy_return_ledger_template: ${artifactId}_40_blank_return_rows_480_blank_cells_0_returns_0_permissions_0_source_text_0_excerpts_0_attribution_notices_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_olp_dmoi_relation_function_source_text_capture_policy_return_ledger_template_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_source_text_capture_policy_return_ledger_template_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_olp_dmoi_relation_function_source_text_capture_policy_return_rows: g.source_text_capture_policy_return_rows,
    current_olp_dmoi_relation_function_source_text_capture_policy_blank_cells: g.blank_return_field_cells_allocated,
    current_olp_dmoi_relation_function_source_text_capture_policy_returns_received: 0,
    current_olp_dmoi_relation_function_source_text_capture_policy_finalized: 0,
    current_olp_dmoi_relation_function_source_text_capture_permissions_granted: 0,
    current_olp_dmoi_relation_function_source_text_copied: 0,
    current_olp_dmoi_relation_function_excerpts_selected: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notices: 0,
    current_olp_dmoi_relation_function_source_text_capture_policy_surfaces: 0,
    current_olp_dmoi_relation_function_source_text_capture_policy_translations: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_olp_dmoi_relation_function_source_text_capture_policy_return_ledger_template = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_olp_dmoi_relation_function_source_text_capture_policy_return_ledger_template: ${artifactId}_blank_policy_returns_only_no_source_text_no_excerpts_no_attribution_notices_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_olp_dmoi_relation_function_source_text_capture_policy_return_ledger_template = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates 40 blank source-text capture policy return rows and 480 blank return-field cells after package 136; 0 policy returns, 0 finalized policies, 0 permission grants, 0 source locators, 0 exact spans, 0 source text, 0 excerpts, 0 attribution notices, 0 surfaces, 0 translations, 0 readiness; user clarified substantive artifacts should be uploaded when a staging path exists.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OLP/DMOI relation-function source-text capture policy return ledger template; 40 blank policy return rows, 480 blank cells, 0 returns, 0 permissions, 0 source locators, 0 exact spans, 0 source text, 0 excerpts, 0 attribution notices, 0 surfaces, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 137: OLP/DMOI relation-function source-text capture policy return ledger template after package 136. It records 40 blank policy return rows, 10 packet-unit summaries, 4 policy-class summaries, and 480 blank return-field cells while keeping 0 policy returns, 0 finalized policies, 0 permission grants, 0 source locators, 0 exact spans, 0 source text, 0 excerpts, 0 attribution notices, 0 surfaces, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | OLP/DMOI relation-function source-text capture policy return ledger template | ${artifactId} | Source-text capture policy return scaffold; 40 blank return rows, 480 blank cells, 0 returns, 0 permissions, 0 source text, 0 excerpts, no surface, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_olp_dmoi_relation_function_source_text_capture_policy_return_ledger_template_artifact: \`${artifactId}\` (40 blank policy return rows; 480 blank return cells; 0 returns; 0 permissions; 0 source text; 0 excerpts; no surfaces, no translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_olp_dmoi_relation_function_source_text_capture_policy_return_ledger_template: \`${artifactId}\`; policy return ledger only, no returns, permissions, source text, excerpts, attribution notices, accepted surfaces, or translation.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OLP/DMOI relation-function source-text capture policy return ledger template; blank return rows are not permission grants, source locators, exact spans, copied source text, excerpts, attribution notices, surfaces, translations, or readiness.`);
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
    { filename: `${artifactId}.json`, class: 'olp_dmoi_relation_function_source_text_capture_policy_return_ledger_template' },
    { filename: `${artifactId}.md`, class: 'olp_dmoi_relation_function_source_text_capture_policy_return_ledger_template' },
    { filename: `${artifactId}.csv`, class: 'olp_dmoi_relation_function_source_text_capture_policy_return_ledger_template' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'olp_dmoi_relation_function_package137_coordination_note' },
    { filename: `${noteId}.md`, class: 'olp_dmoi_relation_function_package137_coordination_note' },
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
  upload.obj.package137_upload_queue_update = {
    captured_utc: '2026-07-03T04:32:00Z',
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
  const step = 'Stage package 137 OLP/DMOI relation-function source-text capture policy return-ledger artifacts with this queue as substantive coordination material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  const expectedReturnRows = (artifact.packet_unit_source_text_capture_policy_summary_rows.length || 0) * policyClasses.length;
  if (artifact.source_text_capture_policy_return_rows.length !== expectedReturnRows) failures.push(`source_text_capture_policy_return_rows_not_${expectedReturnRows}_${artifact.source_text_capture_policy_return_rows.length}`);
  if (artifact.packet_unit_source_text_capture_policy_summary_rows.length !== 10) failures.push(`packet_summary_rows_not_10_${artifact.packet_unit_source_text_capture_policy_summary_rows.length}`);
  if (artifact.policy_class_source_text_capture_policy_summary_rows.length !== 4) failures.push(`policy_class_summary_rows_not_4_${artifact.policy_class_source_text_capture_policy_summary_rows.length}`);
  if (g.blank_return_fields_per_row !== blankReturnFields.length) failures.push(`blank_return_fields_per_row_not_${blankReturnFields.length}_${g.blank_return_fields_per_row}`);
  if (g.blank_return_field_cells_allocated !== artifact.source_text_capture_policy_return_rows.length * blankReturnFields.length) failures.push(`blank_return_cells_mismatch_${g.blank_return_field_cells_allocated}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.source_text_capture_policy_return_rows) {
    const filled = blankReturnFields.some((field) => row[field] !== null && !(Array.isArray(row[field]) && row[field].length === 0));
    if (filled || row.return_received || row.policy_finalized || row.source_locator_decision_allowed_now || row.exact_line_span_selection_allowed_now || row.source_text_capture_allowed_now || row.selected_excerpt_attribution_notice_allowed_now || row.surface_gate_opened || row.translation_gate_opened) {
      failures.push(`nonblank_policy_return_row_${row.source_text_capture_policy_return_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const parent = (await readJson(parentCriteriaDecision)).obj;
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
  source_text_capture_policy_return_rows: artifact.gate_state.source_text_capture_policy_return_rows,
  packet_unit_source_text_capture_policy_summary_rows: artifact.gate_state.packet_unit_source_text_capture_policy_summary_rows,
  policy_class_source_text_capture_policy_summary_rows: artifact.gate_state.policy_class_source_text_capture_policy_summary_rows,
  blank_return_fields_per_row: artifact.gate_state.blank_return_fields_per_row,
  blank_return_field_cells_allocated: artifact.gate_state.blank_return_field_cells_allocated,
  source_text_capture_policy_returns_received: artifact.gate_state.source_text_capture_policy_returns_received,
  source_text_capture_policy_return_fields_filled: artifact.gate_state.source_text_capture_policy_return_fields_filled,
  source_text_capture_permissions_granted: artifact.gate_state.source_text_capture_permissions_granted,
  source_locator_permissions_granted: artifact.gate_state.source_locator_permissions_granted,
  exact_line_spans_selected: artifact.gate_state.exact_line_spans_selected,
  source_text_copied: artifact.gate_state.source_text_copied,
  excerpts_selected: artifact.gate_state.excerpts_selected,
  selected_excerpt_attribution_notices_filled: artifact.gate_state.selected_excerpt_attribution_notices_filled,
  local_language_surfaces_filled: artifact.gate_state.local_language_surfaces_filled,
  translated_passages: artifact.gate_state.translated_passages,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
