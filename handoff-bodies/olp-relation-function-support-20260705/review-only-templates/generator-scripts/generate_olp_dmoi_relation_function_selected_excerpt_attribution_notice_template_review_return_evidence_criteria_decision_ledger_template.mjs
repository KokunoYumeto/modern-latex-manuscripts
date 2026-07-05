import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_DECISION_LEDGER_TEMPLATE_20260703T060000Z';
const noteId = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_DECISION_LEDGER_TEMPLATE_NOTE_20260703T060100Z';
const generatedUtc = '2026-07-03T06:00:00Z';
const noteGeneratedUtc = '2026-07-03T06:01:00Z';
const packageOrder = 143;
const queueCandidateId = 'OTCQ-OLP-DMOI-RELATION-FUNCTION-SELECTED-EXCERPT-ATTRIBUTION-NOTICE-TEMPLATE-REVIEW-RETURN-EVIDENCE-CRITERIA-DECISION-LEDGER-TEMPLATE-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentEvidenceIntake = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_INTAKE_LEDGER_TEMPLATE_20260703T054500Z';
const parentArtifacts = [
  parentEvidenceIntake,
  'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_RUBRIC_20260703T053000Z',
  'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_LEDGER_TEMPLATE_20260703T051500Z'
];

const blankDecisionFields = [
  'decision_date',
  'decision_authority_role',
  'criterion_decision',
  'decision_basis_pointer',
  'evidence_value_reviewed',
  'evidence_source_pointer_reviewed',
  'source_text_absence_confirmed',
  'downstream_gate_limit_confirmed',
  'allowed_update_scope',
  'decision_note'
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

function buildDecisionRows(parent) {
  return parent.review_return_evidence_intake_rows.map((row, index) => ({
    review_return_evidence_criteria_decision_row_id: `ODRF-SEL-EXC-ATTR-RRET-EVID-DEC-${String(index + 1).padStart(3, '0')}`,
    parent_review_return_evidence_intake_row_id: row.review_return_evidence_intake_row_id,
    parent_review_return_evidence_criterion_row_id: row.parent_review_return_evidence_criterion_row_id,
    parent_review_return_ledger_row_id: row.parent_review_return_ledger_row_id,
    parent_review_packet_row_id: row.parent_review_packet_row_id,
    parent_notice_template_row_id: row.parent_notice_template_row_id,
    parent_source_text_capture_policy_return_row_id: row.parent_source_text_capture_policy_return_row_id,
    parent_packet_unit: row.parent_packet_unit,
    criterion_type: row.criterion_type,
    criterion_label: row.criterion_label,
    required_evidence: row.required_evidence,
    inherited_evidence_fields_filled: row.evidence_fields_filled,
    inherited_evidence_value_filled: row.evidence_value_filled,
    inherited_evidence_source_pointer_filled: row.evidence_source_pointer_filled,
    inherited_evidence_row_ready_for_review: row.evidence_row_ready_for_review,
    inherited_review_return_received: row.review_return_received,
    blank_decision_fields: blankDecisionFields,
    decision_date: null,
    decision_authority_role: null,
    criterion_decision: null,
    decision_basis_pointer: null,
    evidence_value_reviewed: null,
    evidence_source_pointer_reviewed: null,
    source_text_absence_confirmed: null,
    downstream_gate_limit_confirmed: null,
    allowed_update_scope: null,
    decision_note: null,
    decision_fields_filled: 0,
    criteria_decision_recorded: false,
    criterion_passed: false,
    criterion_failed: false,
    criterion_unfilled: true,
    evidence_value_reviewed_flag: false,
    evidence_source_pointer_reviewed_flag: false,
    review_return_received: false,
    notice_template_approval_allowed_after_decision: false,
    source_text_or_excerpt_allowed_after_decision: false,
    surface_gate_opened: false,
    translation_gate_opened: false,
    decision_row_status: 'blank_review_return_evidence_criteria_decision_row_only'
  }));
}

function buildCriterionClassDecisionSummaryRows(parent, decisionRows) {
  return parent.criterion_class_review_return_evidence_intake_summary_rows.map((row, index) => {
    const linked = decisionRows.filter((decision) => decision.criterion_type === row.criterion_type);
    return {
      review_return_evidence_criteria_decision_criterion_class_summary_row_id: `ODRF-SEL-EXC-ATTR-RRET-EVID-DEC-CLASS-${String(index + 1).padStart(2, '0')}`,
      parent_review_return_evidence_intake_criterion_class_summary_row_id: row.review_return_evidence_intake_criterion_class_summary_row_id,
      criterion_type: row.criterion_type,
      criterion_label: row.criterion_label,
      linked_criteria_decision_row_ids: linked.map((decision) => decision.review_return_evidence_criteria_decision_row_id),
      decision_rows_required: linked.length,
      decisions_recorded: 0,
      criteria_rows_passed: 0,
      criteria_rows_failed: 0,
      criteria_rows_unfilled: linked.length,
      evidence_values_reviewed: 0,
      evidence_source_pointers_reviewed: 0,
      class_ready_for_decision_review: false
    };
  });
}

function buildPacketUnitDecisionSummaryRows(parent, decisionRows) {
  return parent.packet_unit_review_return_evidence_intake_summary_rows.map((row, index) => {
    const linked = decisionRows.filter((decision) => decision.parent_review_return_ledger_row_id === row.parent_review_return_ledger_row_id);
    return {
      review_return_evidence_criteria_decision_packet_summary_row_id: `ODRF-SEL-EXC-ATTR-RRET-EVID-DEC-PACKET-${String(index + 1).padStart(2, '0')}`,
      parent_review_return_evidence_intake_packet_summary_row_id: row.review_return_evidence_intake_packet_summary_row_id,
      parent_packet_unit: row.parent_packet_unit,
      parent_review_return_ledger_row_id: row.parent_review_return_ledger_row_id,
      linked_criteria_decision_row_ids: linked.map((decision) => decision.review_return_evidence_criteria_decision_row_id),
      decision_rows_required: linked.length,
      decisions_recorded: 0,
      criteria_rows_passed: 0,
      criteria_rows_failed: 0,
      criteria_rows_unfilled: linked.length,
      evidence_values_reviewed: 0,
      evidence_source_pointers_reviewed: 0,
      review_return_received: false,
      notice_template_approved_for_fill: false,
      source_text_or_excerpt_allowed: false,
      packet_ready_for_decision_review: false
    };
  });
}

function buildArtifact(parent) {
  const decisionRows = buildDecisionRows(parent);
  const criterionClassRows = buildCriterionClassDecisionSummaryRows(parent, decisionRows);
  const packetSummaryRows = buildPacketUnitDecisionSummaryRows(parent, decisionRows);
  const blankDecisionCells = decisionRows.length * blankDecisionFields.length;
  const parentGate = parent.gate_state || {};
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_ledger_template_blank_no_decisions_no_evidence_review_no_returns_no_approvals_no_excerpts_no_source_text_no_notice_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Allocate blank criteria-decision rows for each package-142 review-return evidence-intake row, without recording decisions, reviewing evidence, receiving returns, approving notice fills, selecting excerpts, copying source text, opening surfaces, or drafting translations.',
    parent_artifacts: parentArtifacts,
    criteria_decision_boundary: {
      ledger_template_is: 'blank criteria-decision ledger for future review-return evidence-intake review',
      ledger_template_is_not: [
        'filled criteria-decision ledger',
        'review return',
        'evidence value',
        'evidence review result',
        'notice-template approval',
        'attribution notice text',
        'source-text capture permission',
        'candidate line-range selection',
        'exact line span selection',
        'source-text cache',
        'selected excerpt',
        'source-text or excerpt sidecar file',
        'local-language surface',
        'translation draft',
        'publication or pilot claim'
      ],
      downstream_gate_policy: 'all downstream source-text, excerpt, notice-fill, surface, translation, publication, and pilot gates remain closed until dated external returns/evidence and explicit decisions are supplied in future artifacts'
    },
    blank_decision_fields: blankDecisionFields,
    review_return_evidence_criteria_decision_rows: decisionRows,
    criterion_class_review_return_evidence_criteria_decision_summary_rows: criterionClassRows,
    packet_unit_review_return_evidence_criteria_decision_summary_rows: packetSummaryRows,
    gate_state: {
      review_return_evidence_criteria_decision_rows: decisionRows.length,
      criterion_class_review_return_evidence_criteria_decision_summary_rows: criterionClassRows.length,
      packet_unit_review_return_evidence_criteria_decision_summary_rows: packetSummaryRows.length,
      blank_decision_fields_per_row: blankDecisionFields.length,
      blank_decision_field_cells_allocated: blankDecisionCells,
      inherited_evidence_intake_rows: parentGate.review_return_evidence_intake_rows || 0,
      inherited_evidence_fields_filled: parentGate.evidence_fields_filled || 0,
      inherited_evidence_values_filled: parentGate.evidence_values_filled || 0,
      inherited_evidence_source_pointers_filled: parentGate.evidence_source_pointers_filled || 0,
      decision_fields_filled: 0,
      criteria_decisions_recorded: 0,
      criteria_rows_filled: 0,
      criteria_passed: 0,
      criteria_failed: 0,
      criteria_unfilled: decisionRows.length,
      evidence_values_reviewed: 0,
      evidence_source_pointers_reviewed: 0,
      review_returns_received: 0,
      notice_template_rows_approved_for_fill: 0,
      selected_excerpt_attribution_notices_filled: 0,
      attribution_notice_files_created: 0,
      source_text_or_excerpt_files_created: 0,
      source_locators_selected: 0,
      candidate_line_ranges_selected: 0,
      exact_line_spans_selected: 0,
      source_passages_selected: 0,
      source_text_copied: 0,
      source_prose_copied: 0,
      source_examples_copied: 0,
      excerpts_selected: 0,
      local_language_surfaces_filled: 0,
      translated_passages: 0,
      translation_ready: false,
      publication_ready: false,
      constructed_surface_ready: false,
      pilot_ready: false
    },
    validation_snapshot: {
      expected_decision_rows: 50,
      expected_criterion_class_summary_rows: 5,
      expected_packet_unit_summary_rows: 10,
      expected_blank_decision_fields_per_row: blankDecisionFields.length,
      expected_blank_decision_field_cells_allocated: blankDecisionCells,
      zero_gate_assertions: [
        'inherited_evidence_fields_filled',
        'inherited_evidence_values_filled',
        'inherited_evidence_source_pointers_filled',
        'decision_fields_filled',
        'criteria_decisions_recorded',
        'criteria_rows_filled',
        'criteria_passed',
        'criteria_failed',
        'evidence_values_reviewed',
        'evidence_source_pointers_reviewed',
        'review_returns_received',
        'notice_template_rows_approved_for_fill',
        'selected_excerpt_attribution_notices_filled',
        'attribution_notice_files_created',
        'source_text_or_excerpt_files_created',
        'source_locators_selected',
        'candidate_line_ranges_selected',
        'exact_line_spans_selected',
        'source_passages_selected',
        'source_text_copied',
        'source_prose_copied',
        'source_examples_copied',
        'excerpts_selected',
        'local_language_surfaces_filled',
        'translated_passages'
      ],
      source_text_or_excerpt_files_created: 0,
      copied_source_text_or_excerpts: false,
      readiness_claims: 0
    },
    next_valid_artifacts: [
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_DECISION_REVIEW_PACKET_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_DECISION_LEDGER_WITH_DECISIONS_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_LEDGER_WITH_RETURNS_<timestamp>'
    ],
    decision: {
      review_returns_accepted: false,
      criteria_decisions_recorded: false,
      notice_template_rows_approved_for_fill: false,
      source_text_or_excerpt_allowed: false,
      surface_or_translation_allowed: false,
      publication_or_pilot_allowed: false
    }
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const classRows = artifact.criterion_class_review_return_evidence_criteria_decision_summary_rows.map((row) => `| ${row.review_return_evidence_criteria_decision_criterion_class_summary_row_id} | ${row.criterion_type} | ${row.decision_rows_required} | ${row.decisions_recorded} | ${row.criteria_rows_unfilled} |`).join('\n');
  const packetRows = artifact.packet_unit_review_return_evidence_criteria_decision_summary_rows.map((row) => `| ${row.review_return_evidence_criteria_decision_packet_summary_row_id} | ${row.parent_packet_unit} | ${row.parent_review_return_ledger_row_id} | ${row.decision_rows_required} | ${row.decisions_recorded} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

Purpose: ${artifact.purpose}

## Counts

- Criteria-decision rows: \`${g.review_return_evidence_criteria_decision_rows}\`
- Criterion-class summary rows: \`${g.criterion_class_review_return_evidence_criteria_decision_summary_rows}\`
- Packet-unit summary rows: \`${g.packet_unit_review_return_evidence_criteria_decision_summary_rows}\`
- Blank decision fields per row: \`${g.blank_decision_fields_per_row}\`
- Blank decision-field cells: \`${g.blank_decision_field_cells_allocated}\`

## Zero Gates

- Decision fields filled: \`0\`
- Criteria decisions recorded: \`0\`
- Criteria passed/failed: \`0 / 0\`
- Evidence values/source pointers reviewed: \`0 / 0\`
- Review returns received: \`0\`
- Notice-template approvals: \`0\`
- Attribution notices/files: \`0 / 0\`
- Source-text/excerpt files: \`0\`
- Source locators/candidate line ranges/exact spans: \`0 / 0 / 0\`
- Source text/prose/examples copied: \`0 / 0 / 0\`
- Excerpts selected: \`0\`
- Surfaces/translations/readiness: \`0 / 0 / false\`

## Criterion-Class Summary

| Row | Criterion type | Decision rows required | Decisions recorded | Criteria unfilled |
| --- | --- | ---: | ---: | ---: |
${classRows}

## Packet Summary

| Row | Packet unit | Parent review-return row | Decision rows required | Decisions recorded |
| --- | --- | --- | ---: | ---: |
${packetRows}

Boundary: this is a blank criteria-decision ledger template only. It is not evidence review, return ingestion, notice approval, source-text capture, excerpt selection, attribution notice text, a source-text/excerpt sidecar, a surface, a translation, or a readiness claim.
`;
}

function buildArtifactCsv(artifact) {
  const rows = [];
  rows.push(['section', 'row_id', 'packet_or_criterion', 'parent_id', 'required_or_blank_count', 'filled_or_recorded_count', 'gate_open'].map(csvCell).join(','));
  for (const row of artifact.review_return_evidence_criteria_decision_rows) {
    rows.push([
      'decision_row',
      row.review_return_evidence_criteria_decision_row_id,
      row.criterion_type,
      row.parent_review_return_evidence_intake_row_id,
      row.blank_decision_fields.length,
      row.decision_fields_filled,
      row.source_text_or_excerpt_allowed_after_decision || row.surface_gate_opened || row.translation_gate_opened
    ].map(csvCell).join(','));
  }
  for (const row of artifact.criterion_class_review_return_evidence_criteria_decision_summary_rows) {
    rows.push([
      'criterion_class_summary',
      row.review_return_evidence_criteria_decision_criterion_class_summary_row_id,
      row.criterion_type,
      row.parent_review_return_evidence_intake_criterion_class_summary_row_id,
      row.decision_rows_required,
      row.decisions_recorded,
      row.class_ready_for_decision_review
    ].map(csvCell).join(','));
  }
  for (const row of artifact.packet_unit_review_return_evidence_criteria_decision_summary_rows) {
    rows.push([
      'packet_unit_summary',
      row.review_return_evidence_criteria_decision_packet_summary_row_id,
      row.parent_packet_unit,
      row.parent_review_return_ledger_row_id,
      row.decision_rows_required,
      row.decisions_recorded,
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
    source_artifact_id: artifact.artifact_id,
    status: 'pointer_only_package143_coordination_note_no_remote_action_no_source_text_no_excerpt_no_translation_no_readiness',
    summary: 'Package 143 queues a blank selected-excerpt attribution notice template review-return evidence criteria-decision ledger template derived from package 142 evidence-intake rows.',
    counts: {
      review_return_evidence_criteria_decision_rows: g.review_return_evidence_criteria_decision_rows,
      criterion_class_review_return_evidence_criteria_decision_summary_rows: g.criterion_class_review_return_evidence_criteria_decision_summary_rows,
      packet_unit_review_return_evidence_criteria_decision_summary_rows: g.packet_unit_review_return_evidence_criteria_decision_summary_rows,
      blank_decision_fields_per_row: g.blank_decision_fields_per_row,
      blank_decision_field_cells_allocated: g.blank_decision_field_cells_allocated,
      inherited_evidence_intake_rows: g.inherited_evidence_intake_rows
    },
    zero_gates: {
      decision_fields_filled: 0,
      criteria_decisions_recorded: 0,
      criteria_passed: 0,
      criteria_failed: 0,
      evidence_values_reviewed: 0,
      evidence_source_pointers_reviewed: 0,
      review_returns_received: 0,
      notice_template_rows_approved_for_fill: 0,
      source_text_or_excerpt_files_created: 0,
      exact_line_spans_selected: 0,
      source_text_copied: 0,
      excerpts_selected: 0,
      surfaces_filled: 0,
      translated_passages: 0,
      readiness_claims: 0
    },
    no_remote_action_by_this_note: true
  };
}

function buildNoteMd(note, artifact) {
  const g = artifact.gate_state;
  return `# Package 143 Coordination Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only update: package 143 creates an OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria-decision ledger template with \`${g.review_return_evidence_criteria_decision_rows}\` blank decision rows, \`${g.blank_decision_fields_per_row}\` blank decision fields per row, and \`${g.blank_decision_field_cells_allocated}\` blank decision-field cells.

Zero gates: \`0\` filled decision fields, \`0\` criteria decisions, \`0\` passed/failed criteria, \`0\` evidence values or source pointers reviewed, \`0\` review returns, \`0\` notice approvals, \`0\` exact line spans, \`0\` source text/prose/examples copied, \`0\` excerpts, \`0\` attribution notices or files, \`0\` source-text/excerpt files, \`0\` surfaces, \`0\` translations, \`0\` readiness claims.

Boundary: criteria-decision ledger template only. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, source-text, excerpt, attribution notice fill, translation, publication, pilot, legal-advice, or remote-state claim.
`;
}

async function writeArtifactAndNote(artifact, note) {
  await writeFile(path.join(outputs, `${artifactId}.json`), `${JSON.stringify(artifact, null, 2)}\n`, 'utf8');
  await writeFile(path.join(outputs, `${artifactId}.md`), buildArtifactMd(artifact), 'utf8');
  await writeFile(path.join(outputs, `${artifactId}.csv`), buildArtifactCsv(artifact), 'utf8');
  await writeShaForJson(artifactId);

  await writeFile(path.join(outputs, `${noteId}.json`), `${JSON.stringify(note, null, 2)}\n`, 'utf8');
  await writeFile(path.join(outputs, `${noteId}.md`), buildNoteMd(note, artifact), 'utf8');
  await writeShaForJson(noteId);
}

async function updateRegistrations(artifact) {
  const g = artifact.gate_state;
  const packageIndex = await readJson(packageIndexFile);
  const order = ensureArray(packageIndex.obj, 'current_package_order');
  if (!order.some((row) => row?.artifact === artifactId)) {
    order.push({
      order: packageOrder,
      role: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_ledger_template_support',
      artifact: artifactId,
      current_use: '50 blank selected-excerpt attribution notice template review-return evidence criteria-decision rows; 10 decision fields per row; 500 blank decision-field cells; 5 criterion-class summaries; 10 packet-unit summaries; 0 decisions, 0 evidence review, 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 surfaces, 0 translation, 0 readiness'
    });
  }
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_ledger_template = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_rows: g.review_return_evidence_criteria_decision_rows,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_blank_cells: g.blank_decision_field_cells_allocated,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decisions_recorded: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_values_reviewed: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_source_text_or_excerpt_files: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_review_packet_or_decisions_only_after_external_returns_no_source_text_no_excerpt_no_surfaces_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria-decision ledger template',
    route: artifactId,
    license_status_to_recheck: 'blank_criteria_decision_only_no_decisions_no_evidence_review_no_returns_no_approvals_no_exact_spans_no_source_text_no_excerpts_no_notices_no_translation',
    best_translation_use: 'future selected-excerpt attribution notice template review-return evidence criteria decision before approval, notice fill, source-text/excerpt sidecar, surface, or translation',
    candidate_lanes: [
      'olp_dmoi_relation_function_attribution_notice_lane',
      'blank_review_return_evidence_criteria_decision',
      'review_only_construction_scaffold',
      'source_aware_excerpt_governance'
    ],
    priority: 1,
    status: 'blank_review_return_evidence_criteria_decision_ledger_no_decisions_no_returns_no_evidence_review_no_approvals_no_source_text_no_excerpts_no_translation',
    gate_state: {
      review_return_evidence_criteria_decision_rows: g.review_return_evidence_criteria_decision_rows,
      blank_decision_field_cells_allocated: g.blank_decision_field_cells_allocated,
      decisions_recorded: 0,
      evidence_values_reviewed: 0,
      evidence_source_pointers_reviewed: 0,
      review_returns_received: 0,
      notice_template_rows_approved_for_fill: 0,
      source_text_or_excerpt_files_created: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_ledger_template: ${artifactId}_50_blank_decision_rows_500_blank_cells_0_decisions_0_evidence_review_0_returns_0_approvals_0_source_text_0_excerpts_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_ledger_template_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_ledger_template_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_rows: g.review_return_evidence_criteria_decision_rows,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_blank_cells: g.blank_decision_field_cells_allocated,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decisions_recorded: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_values_reviewed: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_source_text_or_excerpt_files: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_surfaces: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_translations: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_ledger_template = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_ledger_template: ${artifactId}_blank_decision_rows_only_no_decisions_no_evidence_review_no_returns_no_approvals_no_source_text_no_excerpts_no_notices_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_ledger_template = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates 50 blank selected-excerpt attribution notice template review-return evidence criteria-decision rows and 500 blank decision-field cells after package 142; 0 decisions, 0 evidence review, 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, 0 readiness; substantive artifacts should be uploaded when a staging path exists.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria-decision ledger template; 50 blank decision rows, 500 blank cells, 0 decisions, 0 evidence review, 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 143: OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria-decision ledger template after package 142. It records 50 blank criteria-decision rows, 5 criterion-class summaries, 10 packet-unit summaries, and 500 blank decision-field cells while keeping 0 decisions, 0 evidence review, 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria-decision ledger template | ${artifactId} | Review-return evidence criteria-decision scaffold; 50 blank decision rows, 500 blank cells, 0 decisions, 0 evidence review, 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, no source-text/excerpt files, no surface, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_ledger_template_artifact: \`${artifactId}\` (50 blank decision rows; 500 blank decision cells; 0 decisions; 0 evidence review; 0 review returns; 0 approvals; 0 exact spans; 0 source text; 0 excerpts; no notices, surfaces, or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_ledger_template: \`${artifactId}\`; blank decision rows only, no decisions, evidence review, returns, approvals, exact spans, source text, excerpts, notices, accepted surfaces, or translation.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria-decision ledger template; blank decision rows are not evidence review, review returns, approvals, exact spans, copied source text, selected excerpts, attribution notices, source-text/excerpt sidecars, surfaces, translations, or readiness.`);
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
    { filename: `${artifactId}.json`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_ledger_template' },
    { filename: `${artifactId}.md`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_ledger_template' },
    { filename: `${artifactId}.csv`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_ledger_template' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'olp_dmoi_relation_function_package143_coordination_note' },
    { filename: `${noteId}.md`, class: 'olp_dmoi_relation_function_package143_coordination_note' },
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
  upload.obj.package143_upload_queue_update = {
    captured_utc: '2026-07-03T06:02:00Z',
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
  const step = 'Stage package 143 OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria-decision artifacts with this queue as substantive coordination material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (artifact.review_return_evidence_criteria_decision_rows.length !== 50) failures.push(`decision_rows_not_50_${artifact.review_return_evidence_criteria_decision_rows.length}`);
  if (artifact.criterion_class_review_return_evidence_criteria_decision_summary_rows.length !== 5) failures.push(`criterion_class_rows_not_5_${artifact.criterion_class_review_return_evidence_criteria_decision_summary_rows.length}`);
  if (artifact.packet_unit_review_return_evidence_criteria_decision_summary_rows.length !== 10) failures.push(`packet_summary_rows_not_10_${artifact.packet_unit_review_return_evidence_criteria_decision_summary_rows.length}`);
  if (g.blank_decision_fields_per_row !== blankDecisionFields.length) failures.push(`blank_decision_fields_per_row_not_${blankDecisionFields.length}_${g.blank_decision_fields_per_row}`);
  if (g.blank_decision_field_cells_allocated !== 50 * blankDecisionFields.length) failures.push(`blank_decision_cells_mismatch_${g.blank_decision_field_cells_allocated}`);
  if (g.criteria_unfilled !== 50) failures.push(`criteria_unfilled_not_50_${g.criteria_unfilled}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.review_return_evidence_criteria_decision_rows) {
    const filled = blankDecisionFields.some((field) => row[field] !== null);
    if (filled || row.decision_fields_filled !== 0 || row.criteria_decision_recorded || row.criterion_passed || row.criterion_failed || !row.criterion_unfilled || row.evidence_value_reviewed_flag || row.evidence_source_pointer_reviewed_flag || row.review_return_received || row.notice_template_approval_allowed_after_decision || row.source_text_or_excerpt_allowed_after_decision || row.surface_gate_opened || row.translation_gate_opened) {
      failures.push(`nonblank_decision_row_${row.review_return_evidence_criteria_decision_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const parent = (await readJson(parentEvidenceIntake)).obj;
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
  review_return_evidence_criteria_decision_rows: artifact.gate_state.review_return_evidence_criteria_decision_rows,
  criterion_class_review_return_evidence_criteria_decision_summary_rows: artifact.gate_state.criterion_class_review_return_evidence_criteria_decision_summary_rows,
  packet_unit_review_return_evidence_criteria_decision_summary_rows: artifact.gate_state.packet_unit_review_return_evidence_criteria_decision_summary_rows,
  blank_decision_fields_per_row: artifact.gate_state.blank_decision_fields_per_row,
  blank_decision_field_cells_allocated: artifact.gate_state.blank_decision_field_cells_allocated,
  decision_fields_filled: artifact.gate_state.decision_fields_filled,
  criteria_decisions_recorded: artifact.gate_state.criteria_decisions_recorded,
  criteria_passed: artifact.gate_state.criteria_passed,
  criteria_failed: artifact.gate_state.criteria_failed,
  criteria_unfilled: artifact.gate_state.criteria_unfilled,
  evidence_values_reviewed: artifact.gate_state.evidence_values_reviewed,
  evidence_source_pointers_reviewed: artifact.gate_state.evidence_source_pointers_reviewed,
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
