import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_RUBRIC_20260703T053000Z';
const noteId = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_RUBRIC_NOTE_20260703T053100Z';
const generatedUtc = '2026-07-03T05:30:00Z';
const noteGeneratedUtc = '2026-07-03T05:31:00Z';
const packageOrder = 141;
const queueCandidateId = 'OTCQ-OLP-DMOI-RELATION-FUNCTION-SELECTED-EXCERPT-ATTRIBUTION-NOTICE-TEMPLATE-REVIEW-RETURN-EVIDENCE-CRITERIA-RUBRIC-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentReviewReturnLedger = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_LEDGER_TEMPLATE_20260703T051500Z';
const parentArtifacts = [
  parentReviewReturnLedger,
  'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_PACKET_20260703T050000Z',
  'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_20260703T044500Z'
];

const criterionClasses = [
  {
    criterion_type: 'dated_non_personal_review_return_identity',
    criterion_label: 'Dated non-personal review return identity',
    required_evidence: 'return date, reviewer role, and non-personal route or owner id are present and match the review-return ledger row'
  },
  {
    criterion_type: 'parent_review_row_and_notice_template_match',
    criterion_label: 'Parent review row and notice-template match',
    required_evidence: 'return points to the intended review-packet row and selected-excerpt attribution notice template row without changing packet unit'
  },
  {
    criterion_type: 'blank_notice_template_preservation',
    criterion_label: 'Blank notice-template preservation',
    required_evidence: 'return confirms no notice field, attribution notice, source-text file, or excerpt file was filled by the review step'
  },
  {
    criterion_type: 'source_text_absence_confirmation',
    criterion_label: 'Source-text absence confirmation',
    required_evidence: 'return confirms no exact span, source prose, source example, source passage, copied source text, or selected excerpt is introduced'
  },
  {
    criterion_type: 'downstream_gate_limit_confirmation',
    criterion_label: 'Downstream gate limit confirmation',
    required_evidence: 'return keeps notice fill, source-text/excerpt sidecar, surface, translation, pilot, and publication gates closed'
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

function buildCriteriaRows(parent) {
  const rows = [];
  for (const returnRow of parent.selected_excerpt_attribution_notice_template_review_return_ledger_rows) {
    for (const criterion of criterionClasses) {
      const index = rows.length + 1;
      rows.push({
        review_return_evidence_criterion_row_id: `ODRF-SEL-EXC-ATTR-RRET-ECRIT-${String(index).padStart(3, '0')}`,
        parent_review_return_ledger_row_id: returnRow.selected_excerpt_attribution_notice_template_review_return_ledger_row_id,
        parent_review_packet_row_id: returnRow.parent_selected_excerpt_attribution_notice_template_review_packet_row_id,
        parent_notice_template_row_id: returnRow.parent_selected_excerpt_attribution_notice_template_row_id,
        parent_source_text_capture_policy_return_row_id: returnRow.parent_source_text_capture_policy_return_row_id,
        parent_packet_unit: returnRow.parent_packet_unit,
        criterion_type: criterion.criterion_type,
        criterion_label: criterion.criterion_label,
        required_evidence: criterion.required_evidence,
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
        notice_template_approved_for_fill_after_criterion: false,
        source_text_or_excerpt_allowed_after_criterion: false,
        surface_gate_opened: false,
        translation_gate_opened: false
      });
    }
  }
  return rows;
}

function buildCriterionClassSummaryRows(criteriaRows) {
  return criterionClasses.map((criterion, index) => {
    const rows = criteriaRows.filter((row) => row.criterion_type === criterion.criterion_type);
    return {
      review_return_evidence_criterion_class_summary_row_id: `ODRF-SEL-EXC-ATTR-RRET-ECRIT-CLASS-${String(index + 1).padStart(2, '0')}`,
      criterion_type: criterion.criterion_type,
      criterion_label: criterion.criterion_label,
      required_evidence: criterion.required_evidence,
      criterion_rows_required: rows.length,
      criterion_rows_filled: 0,
      criteria_passed: 0,
      criteria_failed: 0,
      criteria_unfilled: rows.length,
      linked_criterion_row_ids: rows.map((row) => row.review_return_evidence_criterion_row_id)
    };
  });
}

function buildPacketUnitSummaryRows(parent, criteriaRows) {
  return parent.selected_excerpt_attribution_notice_template_review_return_ledger_rows.map((row, index) => {
    const linked = criteriaRows.filter((criterion) => criterion.parent_review_return_ledger_row_id === row.selected_excerpt_attribution_notice_template_review_return_ledger_row_id);
    return {
      review_return_evidence_criterion_packet_summary_row_id: `ODRF-SEL-EXC-ATTR-RRET-ECRIT-PACKET-${String(index + 1).padStart(2, '0')}`,
      parent_packet_unit: row.parent_packet_unit,
      parent_review_return_ledger_row_id: row.selected_excerpt_attribution_notice_template_review_return_ledger_row_id,
      criterion_rows_required: linked.length,
      criterion_rows_filled: 0,
      criteria_passed: 0,
      criteria_failed: 0,
      criteria_unfilled: linked.length,
      review_return_received: false,
      notice_template_approved_for_fill: false,
      source_text_or_excerpt_allowed: false,
      linked_criterion_row_ids: linked.map((criterion) => criterion.review_return_evidence_criterion_row_id)
    };
  });
}

function buildArtifact(parent) {
  const criteriaRows = buildCriteriaRows(parent);
  const criterionClassRows = buildCriterionClassSummaryRows(criteriaRows);
  const packetSummaryRows = buildPacketUnitSummaryRows(parent, criteriaRows);
  const blankCriterionCells = criteriaRows.length * blankCriterionFields.length;
  const parentGate = parent.gate_state || {};
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_rubric_blank_no_evidence_no_returns_no_approvals_no_excerpts_no_source_text_no_notice_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Allocate blank evidence-criteria rows for future review returns against the package-140 review-return ledger, without filling evidence, receiving returns, approving notice fills, selecting excerpts, copying source text, opening surfaces, or drafting translations.',
    parent_artifacts: parentArtifacts,
    criteria_boundary: {
      rubric_is: 'blank criteria rubric for future selected-excerpt attribution notice template review-return evidence',
      rubric_is_not: [
        'review return',
        'evidence intake',
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
        'allocate criterion rows by parent review-return row and criterion class',
        'make future return evidence requirements explicit',
        'keep all evidence, source, notice, surface, and translation fields empty'
      ],
      blocked_now: [
        'inventing review returns or evidence',
        'passing or failing criteria',
        'approving notice templates for fill',
        'copying source text or excerpts',
        'opening surface, translation, pilot, or publication gates'
      ]
    },
    criterion_classes: criterionClasses,
    blank_criterion_fields: blankCriterionFields,
    review_return_evidence_criteria_rows: criteriaRows,
    review_return_evidence_criterion_class_summary_rows: criterionClassRows,
    packet_unit_review_return_evidence_criterion_summary_rows: packetSummaryRows,
    gate_state: {
      review_return_evidence_criteria_rows: criteriaRows.length,
      review_return_evidence_criterion_class_summary_rows: criterionClassRows.length,
      packet_unit_review_return_evidence_criterion_summary_rows: packetSummaryRows.length,
      blank_criterion_fields_per_row: blankCriterionFields.length,
      blank_criterion_field_cells_allocated: blankCriterionCells,
      inherited_review_return_ledger_rows: parentGate.selected_excerpt_attribution_notice_template_review_return_ledger_rows,
      inherited_review_returns_received: parentGate.review_returns_received,
      inherited_notice_template_rows_approved_for_fill: parentGate.notice_template_rows_approved_for_fill,
      criterion_fields_filled: 0,
      evidence_values_filled: 0,
      evidence_source_pointers_filled: 0,
      criteria_rows_filled: 0,
      criteria_passed: 0,
      criteria_failed: 0,
      criteria_unfilled: criteriaRows.length,
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
      validator: 'local_node_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_rubric_generation_prevalidation_20260703T053000Z',
      zero_gate_assertions: [
        'criterion_fields_filled',
        'evidence_values_filled',
        'evidence_source_pointers_filled',
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
      review_return_evidence_criteria_rows: criteriaRows.length,
      review_return_evidence_criterion_class_summary_rows: criterionClassRows.length,
      packet_unit_review_return_evidence_criterion_summary_rows: packetSummaryRows.length,
      blank_criterion_fields_per_row: blankCriterionFields.length,
      blank_criterion_field_cells_allocated: blankCriterionCells
    },
    next_valid_artifacts: [
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_INTAKE_LEDGER_TEMPLATE_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_DECISION_LEDGER_TEMPLATE_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_LEDGER_WITH_RETURNS_<timestamp>'
    ],
    decision: 'Package 141 creates a blank evidence-criteria rubric for future package-140 review returns. It allocates criteria only and preserves zero returns, zero evidence, zero approvals, zero exact spans, zero source text, zero excerpts, zero notices, zero surfaces, zero translations, and zero readiness.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const classRows = artifact.review_return_evidence_criterion_class_summary_rows.map((row) => `| ${row.review_return_evidence_criterion_class_summary_row_id} | ${row.criterion_type} | ${row.criterion_rows_required} | ${row.criteria_unfilled} |`).join('\n');
  const packetRows = artifact.packet_unit_review_return_evidence_criterion_summary_rows.map((row) => `| ${row.review_return_evidence_criterion_packet_summary_row_id} | ${row.parent_packet_unit} | ${row.parent_review_return_ledger_row_id} | ${row.criterion_rows_required} | ${row.criteria_unfilled} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: ${artifact.status}

## Purpose

${artifact.purpose}

## Boundary

This is a blank evidence-criteria rubric. It is not a review return, evidence intake, criteria decision, approval, selected excerpt, exact line span, source text, filled attribution notice, source-text/excerpt sidecar, surface, translation, pilot, publication, commit, push, PR update, or Zenodo action.

## Counts

- Criteria rows: \`${g.review_return_evidence_criteria_rows}\`
- Criterion-class summaries: \`${g.review_return_evidence_criterion_class_summary_rows}\`
- Packet-unit summaries: \`${g.packet_unit_review_return_evidence_criterion_summary_rows}\`
- Blank criterion fields per row: \`${g.blank_criterion_fields_per_row}\`
- Blank criterion-field cells allocated: \`${g.blank_criterion_field_cells_allocated}\`
- Filled criteria/pass/fail/unfilled: \`${g.criteria_rows_filled}/${g.criteria_passed}/${g.criteria_failed}/${g.criteria_unfilled}\`
- Review returns/approvals/evidence fields: \`${g.review_returns_received}/${g.notice_template_rows_approved_for_fill}/${g.evidence_values_filled}\`
- Exact spans/source text/excerpts/notices/files: \`${g.exact_line_spans_selected}/${g.source_text_copied}/${g.excerpts_selected}/${g.selected_excerpt_attribution_notices_filled}/${g.source_text_or_excerpt_files_created}\`
- Surfaces/translations/readiness: \`${g.local_language_surfaces_filled}/${g.translated_passages}/${g.pilot_ready}\`

## Criterion Class Summary

| Row | Criterion type | Required rows | Unfilled rows |
| --- | --- | ---: | ---: |
${classRows}

## Packet Unit Summary

| Row | Packet unit | Parent return row | Required criteria | Unfilled criteria |
| --- | --- | --- | ---: | ---: |
${packetRows}

## Decision

${artifact.decision}
`;
}

function buildArtifactCsv(artifact) {
  const rows = [];
  rows.push(['section', 'row_id', 'packet_or_criterion', 'parent_id', 'required_or_blank_count', 'filled_or_pass_count', 'gate_open'].map(csvCell).join(','));
  for (const row of artifact.review_return_evidence_criteria_rows) {
    rows.push([
      'review_return_evidence_criterion',
      row.review_return_evidence_criterion_row_id,
      row.criterion_type,
      row.parent_review_return_ledger_row_id,
      row.blank_criterion_fields.length,
      row.criterion_fields_filled,
      row.surface_gate_opened || row.translation_gate_opened
    ].map(csvCell).join(','));
  }
  for (const row of artifact.review_return_evidence_criterion_class_summary_rows) {
    rows.push([
      'criterion_class_summary',
      row.review_return_evidence_criterion_class_summary_row_id,
      row.criterion_type,
      '',
      row.criterion_rows_required,
      row.criteria_passed,
      false
    ].map(csvCell).join(','));
  }
  for (const row of artifact.packet_unit_review_return_evidence_criterion_summary_rows) {
    rows.push([
      'packet_unit_summary',
      row.review_return_evidence_criterion_packet_summary_row_id,
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
    source_artifact: artifact.artifact_id,
    package_order: packageOrder,
    status: 'pointer_only_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_rubric_note_no_upload_claim_no_remote_state_claim',
    purpose: 'Record package-141 OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence-criteria continuation while preserving no-review-return/no-evidence/no-approval/no-excerpt/no-source-text/no-notice/no-translation boundaries.',
    points_to_artifacts: [
      `${artifactId}.json`,
      `${artifactId}.md`,
      `${artifactId}.csv`,
      `${artifactId}.sha256`
    ],
    summary: {
      review_return_evidence_criteria_rows: g.review_return_evidence_criteria_rows,
      criterion_class_summary_rows: g.review_return_evidence_criterion_class_summary_rows,
      packet_unit_summary_rows: g.packet_unit_review_return_evidence_criterion_summary_rows,
      blank_criterion_field_cells_allocated: g.blank_criterion_field_cells_allocated,
      criteria_rows_filled: g.criteria_rows_filled,
      criteria_passed: g.criteria_passed,
      criteria_failed: g.criteria_failed,
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
    boundary: 'Pointer-only coordination note. No review return, evidence, criteria decision, approval, exact line span, selected excerpt, source text, attribution notice text, source-text/excerpt sidecar, surface, translation, pilot, publication, commit, push, PR update, or Zenodo action is claimed.',
    upload_intent: 'Queue the package-141 JSON/MD/CSV/checksum and this note for the existing Noether upload path as substantive coordination material; user clarified on 2026-07-03 that substantive artifacts should not be deferred because of mobile-plan or bandwidth wording.',
    message_template: `Package 141 added ${artifactId}: 50 blank review-return evidence criteria rows, 5 criterion-class summaries, 10 packet-unit summaries, 300 blank criterion-field cells, 0 evidence, 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 attribution notices, 0 source-text/excerpt files, 0 surfaces/translations, 0 readiness.`
  };
}

function buildNoteMd(note) {
  return `# Package 141 Coordination Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${note.source_artifact}\`

Generated UTC: \`${note.generated_utc}\`

## Summary

- Review-return evidence criteria rows: \`${note.summary.review_return_evidence_criteria_rows}\`
- Criterion-class summaries: \`${note.summary.criterion_class_summary_rows}\`
- Packet-unit summaries: \`${note.summary.packet_unit_summary_rows}\`
- Blank criterion-field cells allocated: \`${note.summary.blank_criterion_field_cells_allocated}\`
- Filled/pass/fail/unfilled criteria: \`${note.summary.criteria_rows_filled}/${note.summary.criteria_passed}/${note.summary.criteria_failed}/${note.summary.criteria_unfilled}\`
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
      role: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_rubric_support',
      artifact: artifactId,
      current_use: '50 blank selected-excerpt attribution notice template review-return evidence criteria rows; 5 criterion classes; 10 packet-unit summaries; 300 blank criterion-field cells; 0 evidence, 0 criteria passed/failed, 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 surfaces, 0 translation, 0 readiness'
    });
  }
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_rubric = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_rows: g.review_return_evidence_criteria_rows,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_blank_cells: g.blank_criterion_field_cells_allocated,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_filled: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_passed: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_failed: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_source_text_or_excerpt_files: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_evidence_intake_ledger_template_or_with_returns_only_no_source_text_no_excerpt_no_surfaces_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria rubric',
    route: artifactId,
    license_status_to_recheck: 'blank_evidence_criteria_only_no_returns_no_evidence_no_approvals_no_exact_spans_no_source_text_no_excerpts_no_notices_no_translation',
    best_translation_use: 'future selected-excerpt attribution notice template review-return evidence review before approval, notice fill, source-text/excerpt sidecar, surface, or translation',
    candidate_lanes: [
      'olp_dmoi_relation_function_attribution_notice_lane',
      'blank_review_return_evidence_criteria',
      'review_only_construction_scaffold',
      'source_aware_excerpt_governance'
    ],
    priority: 1,
    status: 'blank_review_return_evidence_criteria_rubric_no_returns_no_evidence_no_approvals_no_source_text_no_excerpts_no_translation',
    gate_state: {
      review_return_evidence_criteria_rows: g.review_return_evidence_criteria_rows,
      blank_criterion_field_cells_allocated: g.blank_criterion_field_cells_allocated,
      criteria_rows_filled: 0,
      criteria_passed: 0,
      criteria_failed: 0,
      review_returns_received: 0,
      notice_template_rows_approved_for_fill: 0,
      source_text_or_excerpt_files_created: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_rubric: ${artifactId}_50_blank_criteria_rows_300_blank_cells_0_evidence_0_returns_0_approvals_0_source_text_0_excerpts_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_rubric_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_rubric_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_rows: g.review_return_evidence_criteria_rows,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_blank_cells: g.blank_criterion_field_cells_allocated,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_passed: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_failed: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_source_text_or_excerpt_files: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_surfaces: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_translations: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_rubric = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_rubric: ${artifactId}_blank_criteria_only_no_returns_no_evidence_no_approvals_no_source_text_no_excerpts_no_notices_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_rubric = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates 50 blank selected-excerpt attribution notice template review-return evidence criteria rows and 300 blank criterion-field cells after package 140; 0 evidence, 0 criteria passed/failed, 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, 0 readiness; substantive artifacts should be uploaded when a staging path exists.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria rubric; 50 blank criteria rows, 300 blank cells, 0 evidence, 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 141: OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria rubric after package 140. It records 50 blank criteria rows, 5 criterion-class summaries, 10 packet-unit summaries, and 300 blank criterion-field cells while keeping 0 evidence, 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria rubric | ${artifactId} | Review-return evidence criteria scaffold; 50 blank criteria rows, 300 blank cells, 0 evidence, 0 review returns, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, no source-text/excerpt files, no surface, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_rubric_artifact: \`${artifactId}\` (50 blank criteria rows; 300 blank criterion cells; 0 evidence; 0 review returns; 0 approvals; 0 exact spans; 0 source text; 0 excerpts; no notices, surfaces, or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_rubric: \`${artifactId}\`; blank criteria only, no returns, evidence, approvals, exact spans, source text, excerpts, notices, accepted surfaces, or translation.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria rubric; blank criteria rows are not evidence, review returns, approvals, exact spans, copied source text, selected excerpts, attribution notices, source-text/excerpt sidecars, surfaces, translations, or readiness.`);
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
    { filename: `${artifactId}.json`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_rubric' },
    { filename: `${artifactId}.md`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_rubric' },
    { filename: `${artifactId}.csv`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_rubric' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'olp_dmoi_relation_function_package141_coordination_note' },
    { filename: `${noteId}.md`, class: 'olp_dmoi_relation_function_package141_coordination_note' },
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
  upload.obj.package141_upload_queue_update = {
    captured_utc: '2026-07-03T05:32:00Z',
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
  const step = 'Stage package 141 OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria-rubric artifacts with this queue as substantive coordination material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (artifact.review_return_evidence_criteria_rows.length !== 50) failures.push(`criteria_rows_not_50_${artifact.review_return_evidence_criteria_rows.length}`);
  if (artifact.review_return_evidence_criterion_class_summary_rows.length !== 5) failures.push(`criterion_class_rows_not_5_${artifact.review_return_evidence_criterion_class_summary_rows.length}`);
  if (artifact.packet_unit_review_return_evidence_criterion_summary_rows.length !== 10) failures.push(`packet_summary_rows_not_10_${artifact.packet_unit_review_return_evidence_criterion_summary_rows.length}`);
  if (g.blank_criterion_fields_per_row !== blankCriterionFields.length) failures.push(`blank_criterion_fields_per_row_not_${blankCriterionFields.length}_${g.blank_criterion_fields_per_row}`);
  if (g.blank_criterion_field_cells_allocated !== 50 * blankCriterionFields.length) failures.push(`blank_criterion_cells_mismatch_${g.blank_criterion_field_cells_allocated}`);
  if (g.criteria_unfilled !== 50) failures.push(`criteria_unfilled_not_50_${g.criteria_unfilled}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.review_return_evidence_criteria_rows) {
    const filled = blankCriterionFields.some((field) => row[field] !== null);
    if (filled || row.criterion_fields_filled !== 0 || row.evidence_value_filled || row.evidence_source_pointer_filled || row.criterion_passed || row.criterion_failed || !row.criterion_unfilled || row.review_return_received || row.notice_template_approved_for_fill_after_criterion || row.source_text_or_excerpt_allowed_after_criterion || row.surface_gate_opened || row.translation_gate_opened) {
      failures.push(`nonblank_criterion_row_${row.review_return_evidence_criterion_row_id}`);
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
  review_return_evidence_criteria_rows: artifact.gate_state.review_return_evidence_criteria_rows,
  review_return_evidence_criterion_class_summary_rows: artifact.gate_state.review_return_evidence_criterion_class_summary_rows,
  packet_unit_review_return_evidence_criterion_summary_rows: artifact.gate_state.packet_unit_review_return_evidence_criterion_summary_rows,
  blank_criterion_fields_per_row: artifact.gate_state.blank_criterion_fields_per_row,
  blank_criterion_field_cells_allocated: artifact.gate_state.blank_criterion_field_cells_allocated,
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
