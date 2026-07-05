import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_DECISION_REVIEW_RETURN_EVIDENCE_CRITERIA_RUBRIC_20260703T064500Z';
const noteId = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_DECISION_REVIEW_RETURN_EVIDENCE_CRITERIA_RUBRIC_NOTE_20260703T064600Z';
const generatedUtc = '2026-07-03T06:45:00Z';
const noteGeneratedUtc = '2026-07-03T06:46:00Z';
const packageOrder = 146;
const queueCandidateId = 'OTCQ-OLP-DMOI-RELATION-FUNCTION-SELECTED-EXCERPT-ATTRIBUTION-NOTICE-TEMPLATE-REVIEW-RETURN-EVIDENCE-CRITERIA-DECISION-REVIEW-RETURN-EVIDENCE-CRITERIA-RUBRIC-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentReviewReturnLedger = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_DECISION_REVIEW_RETURN_LEDGER_TEMPLATE_20260703T063000Z';
const parentArtifacts = [
  parentReviewReturnLedger,
  'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_DECISION_REVIEW_PACKET_20260703T061500Z',
  'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_DECISION_LEDGER_TEMPLATE_20260703T060000Z'
];

const criterionClasses = [
  {
    criterion_type: 'dated_non_personal_review_return_evidence_identity',
    criterion_label: 'Dated non-personal review-return evidence identity',
    required_evidence: 'future return evidence records a return date, reviewer role, and non-personal route or owner id matching the parent review-return ledger row'
  },
  {
    criterion_type: 'parent_review_return_row_match',
    criterion_label: 'Parent review-return row match',
    required_evidence: 'future return evidence points to the intended package-145 return-ledger row and inherited package-144 review-packet row without changing packet unit or criterion identity'
  },
  {
    criterion_type: 'blank_return_field_preservation',
    criterion_label: 'Blank return-field preservation',
    required_evidence: 'future return evidence confirms blank return fields, review fields, notice-template fields, and attribution-notice fields were not filled by the rubric step'
  },
  {
    criterion_type: 'criteria_decision_absence_confirmation',
    criterion_label: 'Criteria-decision absence confirmation',
    required_evidence: 'future return evidence confirms this rubric did not itself record a criteria decision, evidence review result, notice approval, source locator, line range, or exact span'
  },
  {
    criterion_type: 'downstream_gate_limit_confirmation',
    criterion_label: 'Downstream gate-limit confirmation',
    required_evidence: 'future return evidence keeps notice fill, source-text/excerpt sidecar, local surface, translation, pilot, and publication gates closed'
  }
];

const blankCriterionFields = [
  'evidence_value',
  'evidence_source_pointer',
  'evidence_reviewer_role',
  'criterion_pass_fail_decision',
  'criterion_decision_note',
  'next_allowed_artifact'
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

function buildCriterionRows(parent) {
  const rows = [];
  for (const returnRow of parent.review_return_evidence_criteria_decision_review_return_ledger_rows) {
    for (const criterion of criterionClasses) {
      const index = rows.length + 1;
      rows.push({
        review_return_evidence_criteria_decision_review_return_evidence_criterion_row_id: `ODRF-SEL-EXC-ATTR-RRET-EVID-DEC-REVRET-ECRIT-${String(index).padStart(3, '0')}`,
        parent_review_return_evidence_criteria_decision_review_return_ledger_row_id: returnRow.review_return_evidence_criteria_decision_review_return_ledger_row_id,
        parent_review_return_evidence_criteria_decision_review_packet_row_id: returnRow.parent_review_return_evidence_criteria_decision_review_packet_row_id,
        parent_review_return_evidence_criteria_decision_row_id: returnRow.parent_review_return_evidence_criteria_decision_row_id,
        parent_review_return_evidence_intake_row_id: returnRow.parent_review_return_evidence_intake_row_id,
        parent_review_return_evidence_criterion_row_id: returnRow.parent_review_return_evidence_criterion_row_id,
        parent_review_return_ledger_row_id: returnRow.parent_review_return_ledger_row_id,
        parent_review_packet_row_id: returnRow.parent_review_packet_row_id,
        parent_notice_template_row_id: returnRow.parent_notice_template_row_id,
        parent_source_text_capture_policy_return_row_id: returnRow.parent_source_text_capture_policy_return_row_id,
        parent_packet_unit: returnRow.parent_packet_unit,
        parent_criterion_type: returnRow.criterion_type,
        parent_criterion_label: returnRow.criterion_label,
        parent_required_evidence: returnRow.required_evidence,
        criterion_type: criterion.criterion_type,
        criterion_label: criterion.criterion_label,
        required_evidence: criterion.required_evidence,
        inherited_return_fields_filled: returnRow.return_fields_filled,
        inherited_review_return_received: returnRow.review_return_received,
        inherited_review_return_ingested: returnRow.review_return_ingested,
        inherited_review_passed: returnRow.review_passed,
        inherited_review_failed: returnRow.review_failed,
        inherited_criteria_decision_approved_after_return: returnRow.criteria_decision_approved_after_return,
        blank_criterion_fields: blankCriterionFields,
        evidence_value: null,
        evidence_source_pointer: null,
        evidence_reviewer_role: null,
        criterion_pass_fail_decision: null,
        criterion_decision_note: null,
        next_allowed_artifact: null,
        criterion_fields_filled: 0,
        evidence_value_filled: false,
        evidence_source_pointer_filled: false,
        criterion_passed: false,
        criterion_failed: false,
        criterion_unfilled: true,
        review_return_received: false,
        review_return_ingested: false,
        return_evidence_reviewed: false,
        notice_template_approved_for_fill_after_criterion: false,
        source_text_or_excerpt_allowed_after_criterion: false,
        surface_gate_opened: false,
        translation_gate_opened: false,
        still_locked_reason: 'missing_review_return_received_ingested_evidence_values_criteria_decisions_notice_approval_exact_span_and_source_text_permission'
      });
    }
  }
  return rows;
}

function buildCriterionClassSummaryRows(criteriaRows) {
  return criterionClasses.map((criterion, index) => {
    const linked = criteriaRows.filter((row) => row.criterion_type === criterion.criterion_type);
    return {
      review_return_evidence_criteria_decision_review_return_evidence_criterion_class_summary_row_id: `ODRF-SEL-EXC-ATTR-RRET-EVID-DEC-REVRET-ECRIT-CLASS-${String(index + 1).padStart(2, '0')}`,
      criterion_type: criterion.criterion_type,
      criterion_label: criterion.criterion_label,
      required_evidence: criterion.required_evidence,
      criterion_rows_required: linked.length,
      criterion_rows_filled: 0,
      criteria_passed: 0,
      criteria_failed: 0,
      criteria_unfilled: linked.length,
      review_returns_received: 0,
      return_evidence_reviewed: 0,
      linked_criterion_row_ids: linked.map((row) => row.review_return_evidence_criteria_decision_review_return_evidence_criterion_row_id)
    };
  });
}

function buildPacketUnitSummaryRows(parent, criteriaRows) {
  return parent.packet_unit_review_return_evidence_criteria_decision_review_return_summary_rows.map((row, index) => {
    const linked = criteriaRows.filter((criterion) => criterion.parent_review_return_ledger_row_id === row.parent_review_return_ledger_row_id);
    return {
      review_return_evidence_criteria_decision_review_return_evidence_criterion_packet_summary_row_id: `ODRF-SEL-EXC-ATTR-RRET-EVID-DEC-REVRET-ECRIT-PACKET-${String(index + 1).padStart(2, '0')}`,
      parent_review_return_evidence_criteria_decision_review_return_packet_summary_row_id: row.review_return_evidence_criteria_decision_review_return_packet_summary_row_id,
      parent_packet_unit: row.parent_packet_unit,
      parent_review_return_ledger_row_id: row.parent_review_return_ledger_row_id,
      criterion_rows_required: linked.length,
      criterion_rows_filled: 0,
      criteria_passed: 0,
      criteria_failed: 0,
      criteria_unfilled: linked.length,
      review_returns_received: 0,
      return_evidence_reviewed: 0,
      notice_template_approved_for_fill: false,
      source_text_or_excerpt_allowed: false,
      linked_criterion_row_ids: linked.map((criterion) => criterion.review_return_evidence_criteria_decision_review_return_evidence_criterion_row_id)
    };
  });
}

function buildArtifact(parent) {
  const criterionRows = buildCriterionRows(parent);
  const criterionClassRows = buildCriterionClassSummaryRows(criterionRows);
  const packetSummaryRows = buildPacketUnitSummaryRows(parent, criterionRows);
  const blankCriterionCells = criterionRows.length * blankCriterionFields.length;
  const parentGate = parent.gate_state || {};
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_rubric_blank_no_returns_no_evidence_no_decisions_no_approvals_no_excerpts_no_source_text_no_notice_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Allocate blank return-evidence criterion rows for future package-145 review-return ledger rows, without receiving returns, filling evidence, recording decisions, reviewing evidence, approving notice fills, selecting excerpts, copying source text, opening surfaces, or drafting translations.',
    parent_artifacts: parentArtifacts,
    criteria_boundary: {
      rubric_is: 'blank evidence-criteria rubric for future received review returns against package-145 return-ledger rows',
      rubric_is_not: [
        'received review return',
        'ingested review return',
        'return evidence value',
        'evidence intake ledger with values',
        'criteria decision ledger',
        'evidence review result',
        'notice-template approval',
        'source-text capture permission',
        'candidate line range',
        'exact line span',
        'selected excerpt',
        'attribution notice text',
        'source-text or excerpt sidecar file',
        'local-language surface',
        'translation draft',
        'publication or pilot claim'
      ],
      downstream_gate_policy: 'criterion rows are allocated only; all return receipt, evidence, decision, source, excerpt, notice-fill, surface, translation, publication, and pilot gates remain closed'
    },
    criterion_classes: criterionClasses,
    blank_criterion_fields: blankCriterionFields,
    review_return_evidence_criteria_decision_review_return_evidence_criteria_rows: criterionRows,
    criterion_class_review_return_evidence_criteria_decision_review_return_evidence_criteria_summary_rows: criterionClassRows,
    packet_unit_review_return_evidence_criteria_decision_review_return_evidence_criteria_summary_rows: packetSummaryRows,
    gate_state: {
      review_return_evidence_criteria_decision_review_return_evidence_criteria_rows: criterionRows.length,
      criterion_class_review_return_evidence_criteria_decision_review_return_evidence_criteria_summary_rows: criterionClassRows.length,
      packet_unit_review_return_evidence_criteria_decision_review_return_evidence_criteria_summary_rows: packetSummaryRows.length,
      blank_criterion_fields_per_row: blankCriterionFields.length,
      blank_criterion_field_cells_allocated: blankCriterionCells,
      inherited_review_return_ledger_rows: parentGate.review_return_evidence_criteria_decision_review_return_ledger_rows || 0,
      inherited_return_fields_filled: parentGate.return_fields_filled || 0,
      inherited_review_returns_received: parentGate.review_returns_received || 0,
      inherited_review_returns_ingested: parentGate.review_returns_ingested || 0,
      inherited_criteria_decisions_recorded: parentGate.criteria_decisions_recorded || 0,
      criterion_fields_filled: 0,
      evidence_values_filled: 0,
      evidence_source_pointers_filled: 0,
      return_evidence_reviewed: 0,
      criteria_rows_filled: 0,
      criteria_passed: 0,
      criteria_failed: 0,
      criteria_unfilled: criterionRows.length,
      review_returns_received: 0,
      review_returns_ingested: 0,
      review_rows_passed: 0,
      review_rows_failed: 0,
      criteria_decisions_recorded: 0,
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
      expected_criterion_rows: 250,
      expected_criterion_class_summary_rows: 5,
      expected_packet_unit_summary_rows: 10,
      expected_blank_criterion_fields_per_row: blankCriterionFields.length,
      expected_blank_criterion_field_cells_allocated: blankCriterionCells,
      zero_gate_assertions: [
        'inherited_return_fields_filled',
        'inherited_review_returns_received',
        'inherited_review_returns_ingested',
        'inherited_criteria_decisions_recorded',
        'criterion_fields_filled',
        'evidence_values_filled',
        'evidence_source_pointers_filled',
        'return_evidence_reviewed',
        'criteria_rows_filled',
        'criteria_passed',
        'criteria_failed',
        'review_returns_received',
        'review_returns_ingested',
        'review_rows_passed',
        'review_rows_failed',
        'criteria_decisions_recorded',
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
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_DECISION_REVIEW_RETURN_EVIDENCE_INTAKE_LEDGER_TEMPLATE_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_DECISION_REVIEW_RETURN_EVIDENCE_CRITERIA_DECISION_LEDGER_TEMPLATE_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_DECISION_REVIEW_RETURN_LEDGER_WITH_RETURNS_<timestamp>'
    ],
    decision: 'Package 146 creates a blank return-evidence criteria rubric after package 145. It allocates criteria only and preserves zero returns, zero evidence values, zero evidence review, zero criteria decisions, zero approvals, zero exact spans, zero source text, zero excerpts, zero notices, zero surfaces, zero translations, and zero readiness.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const classRows = artifact.criterion_class_review_return_evidence_criteria_decision_review_return_evidence_criteria_summary_rows.map((row) => `| ${row.review_return_evidence_criteria_decision_review_return_evidence_criterion_class_summary_row_id} | ${row.criterion_type} | ${row.criterion_rows_required} | ${row.criteria_unfilled} |`).join('\n');
  const packetRows = artifact.packet_unit_review_return_evidence_criteria_decision_review_return_evidence_criteria_summary_rows.map((row) => `| ${row.review_return_evidence_criteria_decision_review_return_evidence_criterion_packet_summary_row_id} | ${row.parent_packet_unit} | ${row.parent_review_return_ledger_row_id} | ${row.criterion_rows_required} | ${row.criteria_unfilled} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

Purpose: ${artifact.purpose}

## Counts

- Return-evidence criterion rows: \`${g.review_return_evidence_criteria_decision_review_return_evidence_criteria_rows}\`
- Criterion-class summary rows: \`${g.criterion_class_review_return_evidence_criteria_decision_review_return_evidence_criteria_summary_rows}\`
- Packet-unit summary rows: \`${g.packet_unit_review_return_evidence_criteria_decision_review_return_evidence_criteria_summary_rows}\`
- Blank criterion fields per row: \`${g.blank_criterion_fields_per_row}\`
- Blank criterion-field cells: \`${g.blank_criterion_field_cells_allocated}\`
- Criteria filled/pass/fail/unfilled: \`${g.criteria_rows_filled}/${g.criteria_passed}/${g.criteria_failed}/${g.criteria_unfilled}\`

## Zero Gates

- Review returns received/ingested: \`0 / 0\`
- Return evidence reviewed: \`0\`
- Evidence values/source pointers filled: \`0 / 0\`
- Criteria decisions recorded: \`0\`
- Notice-template approvals: \`0\`
- Attribution notices/files: \`0 / 0\`
- Source-text/excerpt files: \`0\`
- Source locators/candidate line ranges/exact spans: \`0 / 0 / 0\`
- Source text/prose/examples copied: \`0 / 0 / 0\`
- Excerpts selected: \`0\`
- Surfaces/translations/readiness: \`0 / 0 / false\`

## Criterion-Class Summary

| Row | Criterion type | Required rows | Unfilled rows |
| --- | --- | ---: | ---: |
${classRows}

## Packet Summary

| Row | Packet unit | Parent review-return row | Required criteria | Unfilled criteria |
| --- | --- | --- | ---: | ---: |
${packetRows}

Boundary: this is a blank return-evidence criteria rubric only. It is not a received return, evidence value, evidence review, criteria decision, notice approval, source-text capture, excerpt selection, attribution notice text, a source-text/excerpt sidecar, a surface, a translation, or a readiness claim.
`;
}

function buildArtifactCsv(artifact) {
  const rows = [];
  rows.push(['section', 'row_id', 'packet_or_criterion', 'parent_id', 'required_or_blank_count', 'filled_or_pass_count', 'gate_open'].map(csvCell).join(','));
  for (const row of artifact.review_return_evidence_criteria_decision_review_return_evidence_criteria_rows) {
    rows.push([
      'return_evidence_criterion',
      row.review_return_evidence_criteria_decision_review_return_evidence_criterion_row_id,
      row.criterion_type,
      row.parent_review_return_evidence_criteria_decision_review_return_ledger_row_id,
      row.blank_criterion_fields.length,
      row.criterion_fields_filled,
      row.source_text_or_excerpt_allowed_after_criterion || row.surface_gate_opened || row.translation_gate_opened
    ].map(csvCell).join(','));
  }
  for (const row of artifact.criterion_class_review_return_evidence_criteria_decision_review_return_evidence_criteria_summary_rows) {
    rows.push([
      'criterion_class_summary',
      row.review_return_evidence_criteria_decision_review_return_evidence_criterion_class_summary_row_id,
      row.criterion_type,
      '',
      row.criterion_rows_required,
      row.criteria_passed,
      false
    ].map(csvCell).join(','));
  }
  for (const row of artifact.packet_unit_review_return_evidence_criteria_decision_review_return_evidence_criteria_summary_rows) {
    rows.push([
      'packet_unit_summary',
      row.review_return_evidence_criteria_decision_review_return_evidence_criterion_packet_summary_row_id,
      row.parent_packet_unit,
      row.parent_review_return_ledger_row_id,
      row.criterion_rows_required,
      row.criterion_rows_filled,
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
    status: 'pointer_only_package146_coordination_note_no_remote_action_no_source_text_no_excerpt_no_translation_no_readiness',
    summary: 'Package 146 queues a blank selected-excerpt attribution notice template review-return evidence criteria-decision review-return evidence criteria rubric derived from package 145 return-ledger rows.',
    counts: {
      review_return_evidence_criteria_decision_review_return_evidence_criteria_rows: g.review_return_evidence_criteria_decision_review_return_evidence_criteria_rows,
      criterion_class_review_return_evidence_criteria_decision_review_return_evidence_criteria_summary_rows: g.criterion_class_review_return_evidence_criteria_decision_review_return_evidence_criteria_summary_rows,
      packet_unit_review_return_evidence_criteria_decision_review_return_evidence_criteria_summary_rows: g.packet_unit_review_return_evidence_criteria_decision_review_return_evidence_criteria_summary_rows,
      blank_criterion_fields_per_row: g.blank_criterion_fields_per_row,
      blank_criterion_field_cells_allocated: g.blank_criterion_field_cells_allocated,
      inherited_review_return_ledger_rows: g.inherited_review_return_ledger_rows
    },
    zero_gates: {
      review_returns_received: 0,
      review_returns_ingested: 0,
      return_evidence_reviewed: 0,
      evidence_values_filled: 0,
      evidence_source_pointers_filled: 0,
      criteria_decisions_recorded: 0,
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
  return `# Package 146 Coordination Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only update: package 146 creates an OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria-decision review-return evidence criteria rubric with \`${g.review_return_evidence_criteria_decision_review_return_evidence_criteria_rows}\` blank criterion rows, \`${g.blank_criterion_fields_per_row}\` blank criterion fields per row, and \`${g.blank_criterion_field_cells_allocated}\` blank criterion-field cells.

Zero gates: \`0\` review returns received/ingested, \`0\` return evidence reviewed, \`0\` evidence values or source pointers filled, \`0\` criteria decisions, \`0\` notice approvals, \`0\` exact line spans, \`0\` source text/prose/examples copied, \`0\` excerpts, \`0\` attribution notices or files, \`0\` source-text/excerpt files, \`0\` surfaces, \`0\` translations, \`0\` readiness claims.

Boundary: return-evidence criteria rubric only. This note makes no commit, push, PR, Zenodo, dispatch, return receipt, return ingestion, evidence review, source-text, excerpt, attribution notice fill, translation, publication, pilot, legal-advice, or remote-state claim.
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
      role: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_rubric_support',
      artifact: artifactId,
      current_use: '250 blank return-evidence criterion rows; 6 criterion fields per row; 1,500 blank criterion-field cells; 5 criterion-class summaries; 10 packet-unit summaries; 0 returns, 0 ingestion, 0 evidence values, 0 evidence review, 0 decisions, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 surfaces, 0 translation, 0 readiness'
    });
  }
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_rubric = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_rows: g.review_return_evidence_criteria_decision_review_return_evidence_criteria_rows,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_blank_cells: g.blank_criterion_field_cells_allocated,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_returns_received: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_source_text_or_excerpt_files: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_return_evidence_intake_or_criteria_decision_only_after_external_return_no_source_text_no_excerpt_no_surfaces_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria-decision review-return evidence criteria rubric',
    route: artifactId,
    license_status_to_recheck: 'blank_return_evidence_criteria_rubric_only_no_returns_no_ingestion_no_evidence_values_no_decisions_no_approvals_no_exact_spans_no_source_text_no_excerpts_no_notices_no_translation',
    best_translation_use: 'future return-evidence criteria rubric before any return evidence intake, criteria decision, notice fill, source-text/excerpt sidecar, surface, or translation',
    candidate_lanes: [
      'olp_dmoi_relation_function_attribution_notice_lane',
      'blank_review_return_evidence_criteria_rubric',
      'review_only_construction_scaffold',
      'source_aware_excerpt_governance'
    ],
    priority: 1,
    status: 'blank_review_return_evidence_criteria_rubric_no_returns_no_evidence_values_no_decisions_no_source_text_no_excerpts_no_translation',
    gate_state: {
      review_return_evidence_criteria_decision_review_return_evidence_criteria_rows: g.review_return_evidence_criteria_decision_review_return_evidence_criteria_rows,
      blank_criterion_field_cells_allocated: g.blank_criterion_field_cells_allocated,
      review_returns_received: 0,
      return_evidence_reviewed: 0,
      criteria_decisions_recorded: 0,
      notice_template_rows_approved_for_fill: 0,
      source_text_or_excerpt_files_created: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_rubric: ${artifactId}_250_blank_criterion_rows_1500_blank_cells_0_returns_0_evidence_0_decisions_0_approvals_0_source_text_0_excerpts_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_rubric_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_rubric_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_rows: g.review_return_evidence_criteria_decision_review_return_evidence_criteria_rows,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_blank_cells: g.blank_criterion_field_cells_allocated,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_returns_received: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_source_text_or_excerpt_files: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_surfaces: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_translations: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_rubric = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_rubric: ${artifactId}_blank_criteria_only_no_returns_no_evidence_no_decisions_no_approvals_no_source_text_no_excerpts_no_notices_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_rubric = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates 250 blank return-evidence criteria rows and 1,500 blank criterion-field cells after package 145; 0 returns, 0 ingestion, 0 evidence values, 0 evidence review, 0 decisions, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, 0 readiness; substantive artifacts should be uploaded when a staging path exists.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria-decision review-return evidence criteria rubric; 250 blank criteria rows, 1,500 blank cells, 0 returns, 0 ingestion, 0 evidence values, 0 evidence review, 0 decisions, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 146: OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria-decision review-return evidence criteria rubric after package 145. It records 250 blank criteria rows, 5 criterion-class summaries, 10 packet-unit summaries, and 1,500 blank criterion-field cells while keeping 0 returns, 0 ingestion, 0 evidence values, 0 evidence review, 0 decisions, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria-decision review-return evidence criteria rubric | ${artifactId} | Return-evidence criteria scaffold; 250 blank criteria rows, 1,500 blank cells, 0 returns, 0 evidence values, 0 evidence review, 0 decisions, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, no source-text/excerpt files, no surface, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_rubric_artifact: \`${artifactId}\` (250 blank criteria rows; 1,500 blank criterion cells; 0 returns; 0 evidence; 0 decisions; 0 approvals; 0 exact spans; 0 source text; 0 excerpts; no notices, surfaces, or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_rubric: \`${artifactId}\`; blank criteria rubric only, no returns, evidence values, evidence review, decisions, approvals, exact spans, source text, excerpts, notices, accepted surfaces, or translation.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria-decision review-return evidence criteria rubric; blank criteria rows are not received returns, ingested returns, evidence values, evidence review, criteria decisions, approvals, exact spans, copied source text, selected excerpts, attribution notices, source-text/excerpt sidecars, surfaces, translations, or readiness.`);
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
    { filename: `${artifactId}.json`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_rubric' },
    { filename: `${artifactId}.md`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_rubric' },
    { filename: `${artifactId}.csv`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_evidence_criteria_rubric' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'olp_dmoi_relation_function_package146_coordination_note' },
    { filename: `${noteId}.md`, class: 'olp_dmoi_relation_function_package146_coordination_note' },
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
  upload.obj.package146_upload_queue_update = {
    captured_utc: '2026-07-03T06:47:00Z',
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
  const step = 'Stage package 146 OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria-decision review-return evidence criteria rubric artifacts with this queue as substantive coordination material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  const rows = artifact.review_return_evidence_criteria_decision_review_return_evidence_criteria_rows;
  if (rows.length !== 250) failures.push(`criterion_rows_not_250_${rows.length}`);
  if (artifact.criterion_class_review_return_evidence_criteria_decision_review_return_evidence_criteria_summary_rows.length !== 5) failures.push(`criterion_class_rows_not_5_${artifact.criterion_class_review_return_evidence_criteria_decision_review_return_evidence_criteria_summary_rows.length}`);
  if (artifact.packet_unit_review_return_evidence_criteria_decision_review_return_evidence_criteria_summary_rows.length !== 10) failures.push(`packet_summary_rows_not_10_${artifact.packet_unit_review_return_evidence_criteria_decision_review_return_evidence_criteria_summary_rows.length}`);
  if (g.blank_criterion_fields_per_row !== blankCriterionFields.length) failures.push(`blank_criterion_fields_per_row_not_${blankCriterionFields.length}_${g.blank_criterion_fields_per_row}`);
  if (g.blank_criterion_field_cells_allocated !== rows.length * blankCriterionFields.length) failures.push(`blank_criterion_cells_mismatch_${g.blank_criterion_field_cells_allocated}`);
  if (g.criteria_unfilled !== rows.length) failures.push(`criteria_unfilled_not_${rows.length}_${g.criteria_unfilled}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of rows) {
    const filled = blankCriterionFields.some((field) => row[field] !== null);
    if (filled || row.criterion_fields_filled !== 0 || row.evidence_value_filled || row.evidence_source_pointer_filled || row.criterion_passed || row.criterion_failed || row.review_return_received || row.review_return_ingested || row.return_evidence_reviewed || row.notice_template_approved_for_fill_after_criterion || row.source_text_or_excerpt_allowed_after_criterion || row.surface_gate_opened || row.translation_gate_opened) {
      failures.push(`nonblank_criterion_row_${row.review_return_evidence_criteria_decision_review_return_evidence_criterion_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const parent = (await readJson(parentReviewReturnLedger)).obj;
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
  review_return_evidence_criteria_decision_review_return_evidence_criteria_rows: artifact.gate_state.review_return_evidence_criteria_decision_review_return_evidence_criteria_rows,
  criterion_class_review_return_evidence_criteria_decision_review_return_evidence_criteria_summary_rows: artifact.gate_state.criterion_class_review_return_evidence_criteria_decision_review_return_evidence_criteria_summary_rows,
  packet_unit_review_return_evidence_criteria_decision_review_return_evidence_criteria_summary_rows: artifact.gate_state.packet_unit_review_return_evidence_criteria_decision_review_return_evidence_criteria_summary_rows,
  blank_criterion_fields_per_row: artifact.gate_state.blank_criterion_fields_per_row,
  blank_criterion_field_cells_allocated: artifact.gate_state.blank_criterion_field_cells_allocated,
  criterion_fields_filled: artifact.gate_state.criterion_fields_filled,
  evidence_values_filled: artifact.gate_state.evidence_values_filled,
  evidence_source_pointers_filled: artifact.gate_state.evidence_source_pointers_filled,
  review_returns_received: artifact.gate_state.review_returns_received,
  review_returns_ingested: artifact.gate_state.review_returns_ingested,
  return_evidence_reviewed: artifact.gate_state.return_evidence_reviewed,
  criteria_decisions_recorded: artifact.gate_state.criteria_decisions_recorded,
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
