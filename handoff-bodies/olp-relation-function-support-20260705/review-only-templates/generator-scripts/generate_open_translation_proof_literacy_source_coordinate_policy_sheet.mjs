import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OPEN_TRANSLATION_PROOF_LITERACY_SOURCE_COORDINATE_POLICY_SHEET_20260703T084500Z';
const noteId = 'OPEN_TRANSLATION_PROOF_LITERACY_SOURCE_COORDINATE_POLICY_SHEET_NOTE_20260703T084600Z';
const generatedUtc = '2026-07-03T08:45:00Z';
const noteGeneratedUtc = '2026-07-03T08:46:00Z';
const packageOrder = 154;
const queueCandidateId = 'OTCQ-OPEN-TRANSLATION-PROOF-LITERACY-SOURCE-COORDINATE-POLICY-SHEET-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';
const parentInventoryFile = 'OPEN_TRANSLATION_PROOF_LITERACY_METADATA_INVENTORY_SCAN_START_20260703T083000Z';
const parentRouterFile = 'OPEN_TRANSLATION_REVIEW_ONLY_SOURCE_COORDINATE_SCAN_ROUTER_20260703T081500Z';
const parentShelfFile = 'OPEN_TRANSLATION_REVIEW_ONLY_PACKET_SOURCE_SHELF_REFRESH_20260703T080000Z';

const policyReviewFields = [
  'policy_review_date',
  'reviewer_route_or_role',
  'policy_class_accepted',
  'coordinate_scan_scope_decision',
  'permission_or_license_gate_decision',
  'attribution_sidecar_decision',
  'excluded_route_confirmation',
  'source_text_capture_decision',
  'next_allowed_artifact',
  'review_note_without_source_prose'
];

const zeroGateKeys = [
  'policy_reviews_completed',
  'coordinate_scans_authorized',
  'source_text_capture_authorized',
  'excerpt_selections_authorized',
  'source_text_or_excerpt_files_created',
  'source_text_copied',
  'source_definitions_copied',
  'source_examples_copied',
  'source_passages_selected',
  'exact_line_spans_selected',
  'candidate_line_ranges_selected',
  'translated_passages',
  'proposed_bridge_lexemes',
  'proposed_bridge_morphemes',
  'proposed_bridge_syntax_rules',
  'proposed_bridge_display_surfaces',
  'accepted_bridge_surfaces',
  'accepted_local_language_terms',
  'reviewer_returns_ingested',
  'license_rechecks_completed',
  'pilot_ready_claims'
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

function classifyOlpExtension(extension) {
  if (extension === '.tex') {
    return {
      policy_class: 'primary_text_source_coordinate_candidate',
      scan_scope: 'future_file_level_and_macro_aware_coordinate_scan_candidate_after_license_attribution_review',
      why: 'TeX is the dominant OLP source-file class in the metadata inventory and is the natural first coordinate layer.',
      candidate_after_review: true
    };
  }
  if (extension === '.md' || extension === '.bib' || extension === '.yml') {
    return {
      policy_class: 'support_metadata_only',
      scan_scope: 'support_route_metadata_only_for_license_attribution_build_or_bibliography_context',
      why: 'This extension is useful for route identity, attribution, or build context rather than proof-literacy excerpt selection.',
      candidate_after_review: false
    };
  }
  if (['.sty', '.cls', '.bst', '.pcr', '[none]', '.html'].includes(extension)) {
    return {
      policy_class: 'build_or_configuration_support_only',
      scan_scope: 'build_configuration_or_generated_support_metadata_only',
      why: 'This extension is not a proof-literacy passage target without a separate route-specific decision.',
      candidate_after_review: false
    };
  }
  if (['.pdf', '.png', '.eps', '.tikz'].includes(extension)) {
    return {
      policy_class: 'asset_or_derived_output_support_only',
      scan_scope: 'asset_or_derived_output_support_metadata_only_no_text_capture',
      why: 'Asset and derived-output routes require a separate diagram/output policy before any text or figure use.',
      candidate_after_review: false
    };
  }
  return {
    policy_class: 'unclassified_support_only',
    scan_scope: 'hold_for_manual_route_review',
    why: 'No coordinate policy class has been assigned beyond support-only review.',
    candidate_after_review: false
  };
}

function classifyOlpTopLevel(groupKey) {
  if (groupKey === 'content') {
    return {
      policy_class: 'primary_content_coordinate_candidate',
      scan_scope: 'future_content_file_coordinate_scan_candidate_after_policy_return',
      why: 'The content tree holds the overwhelming majority of OLP file metadata rows and is the likely proof-literacy source route.',
      candidate_after_review: true
    };
  }
  if (groupKey === 'courses') {
    return {
      policy_class: 'course_assembly_support_only',
      scan_scope: 'course_or_packet_assembly_metadata_only',
      why: 'Course assembly routes can shape packet order but should not select source passages by themselves.',
      candidate_after_review: false
    };
  }
  if (['assets', 'sty', 'include', 'misc', 'bib', '.github', '[root]'].includes(groupKey)) {
    return {
      policy_class: 'repository_support_metadata_only',
      scan_scope: 'repository_support_metadata_only_no_excerpt_selection',
      why: 'This top-level group supports source identity, assets, build files, or governance rather than direct proof-literacy passage selection.',
      candidate_after_review: false
    };
  }
  return {
    policy_class: 'unclassified_top_level_support_only',
    scan_scope: 'hold_for_manual_route_review',
    why: 'No direct proof-literacy coordinate policy has been assigned.',
    candidate_after_review: false
  };
}

function classifyBookOfProofSourceClass(sourceClass, status) {
  if (status !== 'cached') {
    return {
      policy_class: 'excluded_failed_or_unavailable_route',
      scan_scope: 'exclude_until_route_is_available_and_rechecked',
      why: 'The route is not currently a cached usable source route.',
      candidate_after_review: false,
      permission_gate_required: true
    };
  }
  if (sourceClass === 'official_pdf') {
    return {
      policy_class: 'permission_gate_before_pdf_coordinate_scan',
      scan_scope: 'pdf_coordinate_scan_candidate_only_after_permission_license_and_no_derivatives_review',
      why: 'The PDF is a likely source route, but Book of Proof permission/licensing must be resolved before any excerpt or adaptation path.',
      candidate_after_review: true,
      permission_gate_required: true
    };
  }
  if (sourceClass === 'official_landing_page' || sourceClass === 'license_deed' || sourceClass === 'external_approval_route') {
    return {
      policy_class: 'permission_and_route_support_metadata_only',
      scan_scope: 'permission_or_authority_support_metadata_only',
      why: 'This route supports permission, attribution, or source identity rather than direct excerpt selection.',
      candidate_after_review: false,
      permission_gate_required: true
    };
  }
  return {
    policy_class: 'book_of_proof_support_only',
    scan_scope: 'support_metadata_only',
    why: 'No direct coordinate-scan role is assigned without a later permission route decision.',
    candidate_after_review: false,
    permission_gate_required: true
  };
}

function blankPolicyReview(rowId, sourceFamily, sourceGroup, policyClass, scope, why, candidateAfterReview, permissionGateRequired = false) {
  return {
    policy_row_id: rowId,
    source_family: sourceFamily,
    source_group: sourceGroup,
    policy_class: policyClass,
    coordinate_scan_scope_policy: scope,
    policy_reason_metadata_only: why,
    coordinate_scan_candidate_after_review: candidateAfterReview,
    permission_or_license_gate_required: permissionGateRequired,
    blank_policy_review_fields: policyReviewFields,
    policy_review_date: null,
    reviewer_route_or_role: null,
    policy_class_accepted: null,
    coordinate_scan_scope_decision: null,
    permission_or_license_gate_decision: null,
    attribution_sidecar_decision: null,
    excluded_route_confirmation: null,
    source_text_capture_decision: null,
    next_allowed_artifact: null,
    review_note_without_source_prose: null,
    policy_review_fields_filled: 0,
    policy_review_completed: false,
    coordinate_scan_authorized: false,
    source_text_capture_authorized: false,
    excerpt_selection_authorized: false,
    translation_authorized: false,
    still_locked_reason: 'metadata_policy_class_only_no_policy_return_no_coordinate_scan_authorization_no_excerpt_permission'
  };
}

function buildOlpExtensionPolicyRows(parent) {
  return parent.olp_extension_summary_rows.map((summary, index) => {
    const cls = classifyOlpExtension(summary.group_key);
    return {
      ...blankPolicyReview(
        `PL-SCP-OLP-EXT-${String(index + 1).padStart(3, '0')}`,
        'Open Logic Project',
        summary.group_key,
        cls.policy_class,
        cls.scan_scope,
        cls.why,
        cls.candidate_after_review,
        false
      ),
      parent_summary_row_id: summary.summary_row_id,
      summary_kind: 'olp_extension',
      metadata_file_rows: summary.file_rows,
      metadata_bytes: summary.bytes
    };
  });
}

function buildOlpTopLevelPolicyRows(parent) {
  return parent.olp_top_level_summary_rows.map((summary, index) => {
    const cls = classifyOlpTopLevel(summary.group_key);
    return {
      ...blankPolicyReview(
        `PL-SCP-OLP-TOP-${String(index + 1).padStart(3, '0')}`,
        'Open Logic Project',
        summary.group_key,
        cls.policy_class,
        cls.scan_scope,
        cls.why,
        cls.candidate_after_review,
        false
      ),
      parent_summary_row_id: summary.summary_row_id,
      summary_kind: 'olp_top_level',
      metadata_file_rows: summary.file_rows,
      metadata_bytes: summary.bytes
    };
  });
}

function buildBookOfProofPolicyRows(parent) {
  return parent.book_of_proof_manifest_route_rows.map((row, index) => {
    const cls = classifyBookOfProofSourceClass(row.source_class, row.status);
    return {
      ...blankPolicyReview(
        `PL-SCP-BOP-ROUTE-${String(index + 1).padStart(3, '0')}`,
        'Book of Proof',
        row.source_class || '[missing]',
        cls.policy_class,
        cls.scan_scope,
        cls.why,
        cls.candidate_after_review,
        cls.permission_gate_required
      ),
      parent_inventory_row_id: row.inventory_row_id,
      manifest_record_id: row.manifest_record_id,
      summary_kind: 'book_of_proof_route_record',
      route_status: row.status,
      metadata_file_rows: 1,
      metadata_bytes: row.bytes
    };
  });
}

function buildPolicyClassSummaryRows(allRows) {
  const map = new Map();
  for (const row of allRows) {
    if (!map.has(row.policy_class)) {
      map.set(row.policy_class, {
        policy_class_summary_row_id: `PL-SCP-CLASS-${String(map.size + 1).padStart(2, '0')}`,
        policy_class: row.policy_class,
        policy_rows: 0,
        metadata_file_rows: 0,
        metadata_bytes: 0,
        coordinate_scan_candidate_after_review_rows: 0,
        permission_or_license_gate_required_rows: 0,
        policy_reviews_completed: 0,
        coordinate_scans_authorized: 0,
        excerpt_selections_authorized: 0
      });
    }
    const entry = map.get(row.policy_class);
    entry.policy_rows += 1;
    entry.metadata_file_rows += row.metadata_file_rows || 0;
    entry.metadata_bytes += row.metadata_bytes || 0;
    if (row.coordinate_scan_candidate_after_review) entry.coordinate_scan_candidate_after_review_rows += 1;
    if (row.permission_or_license_gate_required) entry.permission_or_license_gate_required_rows += 1;
  }
  return [...map.values()].sort((a, b) => b.policy_rows - a.policy_rows || a.policy_class.localeCompare(b.policy_class));
}

function buildNextPolicyArtifactRows() {
  return [
    {
      next_policy_artifact_row_id: 'PL-SCP-NEXT-01',
      lane: 'olp_content_tex',
      useful_next_artifact: 'OPEN_TRANSLATION_PROOF_LITERACY_OLP_CONTENT_TEX_COORDINATE_SCAN_POLICY_RETURN_TEMPLATE_<timestamp>',
      allowed_action_class: 'policy_return_template_only',
      source_text_or_excerpt_allowed_now: false
    },
    {
      next_policy_artifact_row_id: 'PL-SCP-NEXT-02',
      lane: 'book_of_proof_permission_gate',
      useful_next_artifact: 'OPEN_TRANSLATION_PROOF_LITERACY_BOOK_OF_PROOF_PERMISSION_ROUTE_DECISION_LEDGER_TEMPLATE_<timestamp>',
      allowed_action_class: 'permission_route_decision_template_only',
      source_text_or_excerpt_allowed_now: false
    },
    {
      next_policy_artifact_row_id: 'PL-SCP-NEXT-03',
      lane: 'proof_literacy_metadata_review',
      useful_next_artifact: 'OPEN_TRANSLATION_PROOF_LITERACY_METADATA_INVENTORY_REVIEW_RETURN_LEDGER_TEMPLATE_<timestamp>',
      allowed_action_class: 'blank_return_template_only',
      source_text_or_excerpt_allowed_now: false
    },
    {
      next_policy_artifact_row_id: 'PL-SCP-NEXT-04',
      lane: 'selected_excerpt_prevention',
      useful_next_artifact: 'OPEN_TRANSLATION_PROOF_LITERACY_SELECTED_EXCERPT_SIDECAR_<timestamp>_only_after_policy_returns',
      allowed_action_class: 'blocked_until_review_and_permission',
      source_text_or_excerpt_allowed_now: false
    }
  ];
}

function buildArtifact(parent) {
  const extensionPolicyRows = buildOlpExtensionPolicyRows(parent);
  const topLevelPolicyRows = buildOlpTopLevelPolicyRows(parent);
  const bookOfProofPolicyRows = buildBookOfProofPolicyRows(parent);
  const allRows = [...extensionPolicyRows, ...topLevelPolicyRows, ...bookOfProofPolicyRows];
  const classSummaryRows = buildPolicyClassSummaryRows(allRows);
  const nextPolicyArtifactRows = buildNextPolicyArtifactRows();
  const blankPolicyReviewCells = allRows.length * policyReviewFields.length;
  const candidateAfterReviewRows = allRows.filter((row) => row.coordinate_scan_candidate_after_review).length;
  const permissionGateRows = allRows.filter((row) => row.permission_or_license_gate_required).length;

  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'proof_literacy_source_coordinate_policy_sheet_no_policy_returns_no_scans_no_source_text_no_excerpts_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Classify package 153 proof-literacy metadata inventory summaries into source-coordinate policy rows for OLP and Book of Proof, distinguishing future scan candidates from support-only, permission-gated, asset/derived, and excluded routes without authorizing scans, copying source text, selecting excerpts, or starting translation.',
    parent_artifacts: [
      parentInventoryFile,
      parentRouterFile,
      parentShelfFile,
      'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z'
    ],
    boundary: {
      artifact_is: [
        'metadata-derived coordinate policy sheet',
        'future scan-candidate classifier',
        'support-only and permission-gate classifier',
        'blank policy-review allocator'
      ],
      artifact_is_not: [
        'policy return',
        'coordinate scan authorization',
        'source text capture authorization',
        'source excerpt selection',
        'license or permission clearance decision',
        'translation draft',
        'constructed-language form proposal',
        'pilot or publication readiness claim'
      ],
      promotion_requires: [
        'dated policy review return',
        'license or permission decision where required',
        'attribution sidecar decision',
        'separate coordinate scan artifact',
        'separate selected-excerpt sidecar before any translation or adaptation'
      ]
    },
    inherited_parent_counts: {
      metadata_inventory_rows_total: parent.gate_state.metadata_inventory_rows_total,
      open_logic_project_inventory_rows: parent.gate_state.open_logic_project_inventory_rows,
      book_of_proof_manifest_route_rows: parent.gate_state.book_of_proof_manifest_route_rows
    },
    olp_extension_policy_rows: extensionPolicyRows,
    olp_top_level_policy_rows: topLevelPolicyRows,
    book_of_proof_route_policy_rows: bookOfProofPolicyRows,
    policy_class_summary_rows: classSummaryRows,
    next_policy_artifact_rows: nextPolicyArtifactRows,
    gate_state: {
      source_coordinate_policy_rows: allRows.length,
      olp_extension_policy_rows: extensionPolicyRows.length,
      olp_top_level_policy_rows: topLevelPolicyRows.length,
      book_of_proof_route_policy_rows: bookOfProofPolicyRows.length,
      policy_class_summary_rows: classSummaryRows.length,
      next_policy_artifact_rows: nextPolicyArtifactRows.length,
      coordinate_scan_candidate_after_review_rows: candidateAfterReviewRows,
      permission_or_license_gate_required_rows: permissionGateRows,
      blank_policy_review_fields_per_row: policyReviewFields.length,
      blank_policy_review_cells_allocated: blankPolicyReviewCells,
      policy_reviews_completed: 0,
      coordinate_scans_authorized: 0,
      source_text_capture_authorized: 0,
      excerpt_selections_authorized: 0,
      source_text_or_excerpt_files_created: 0,
      source_text_copied: 0,
      source_definitions_copied: 0,
      source_examples_copied: 0,
      source_passages_selected: 0,
      exact_line_spans_selected: 0,
      candidate_line_ranges_selected: 0,
      translated_passages: 0,
      proposed_bridge_lexemes: 0,
      proposed_bridge_morphemes: 0,
      proposed_bridge_syntax_rules: 0,
      proposed_bridge_display_surfaces: 0,
      accepted_bridge_surfaces: 0,
      accepted_local_language_terms: 0,
      reviewer_returns_ingested: 0,
      license_rechecks_completed: 0,
      pilot_ready_claims: 0,
      publication_ready: false,
      translation_ready: false,
      constructed_surface_ready: false,
      pilot_ready: false
    },
    validation_snapshot: {
      expected_source_coordinate_policy_rows: allRows.length,
      expected_olp_extension_policy_rows: parent.olp_extension_summary_rows.length,
      expected_olp_top_level_policy_rows: parent.olp_top_level_summary_rows.length,
      expected_book_of_proof_route_policy_rows: parent.book_of_proof_manifest_route_rows.length,
      expected_min_coordinate_scan_candidate_after_review_rows: 1,
      expected_blank_policy_review_fields_per_row: policyReviewFields.length,
      expected_blank_policy_review_cells_allocated: blankPolicyReviewCells,
      zero_gate_assertions: zeroGateKeys,
      readiness_claims: 0
    },
    next_valid_artifacts: nextPolicyArtifactRows.map((row) => row.useful_next_artifact),
    decision: 'Package 154 converts proof-literacy metadata inventory summaries into a policy sheet. It names future scan-candidate classes but authorizes no scans, no source-text capture, no excerpts, no translations, no constructed forms, and no readiness.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const classRows = artifact.policy_class_summary_rows.map((row) => `| ${row.policy_class_summary_row_id} | ${row.policy_class} | ${row.policy_rows} | ${row.coordinate_scan_candidate_after_review_rows} | ${row.permission_or_license_gate_required_rows} |`).join('\n');
  const extRows = artifact.olp_extension_policy_rows.map((row) => `| ${row.policy_row_id} | ${row.source_group} | ${row.policy_class} | ${row.metadata_file_rows} | ${row.coordinate_scan_candidate_after_review} |`).join('\n');
  const topRows = artifact.olp_top_level_policy_rows.map((row) => `| ${row.policy_row_id} | ${row.source_group} | ${row.policy_class} | ${row.metadata_file_rows} | ${row.coordinate_scan_candidate_after_review} |`).join('\n');
  const bopRows = artifact.book_of_proof_route_policy_rows.map((row) => `| ${row.policy_row_id} | ${row.source_group} | ${row.route_status} | ${row.policy_class} | ${row.permission_or_license_gate_required} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Counts

- Source-coordinate policy rows: \`${g.source_coordinate_policy_rows}\`
- OLP extension policy rows: \`${g.olp_extension_policy_rows}\`
- OLP top-level policy rows: \`${g.olp_top_level_policy_rows}\`
- Book of Proof route policy rows: \`${g.book_of_proof_route_policy_rows}\`
- Coordinate-scan candidate-after-review rows: \`${g.coordinate_scan_candidate_after_review_rows}\`
- Permission/license gate required rows: \`${g.permission_or_license_gate_required_rows}\`
- Blank policy-review cells: \`${g.blank_policy_review_cells_allocated}\`

## Policy Classes

| Row | Policy class | Rows | Candidate-after-review rows | Permission-gated rows |
| --- | --- | ---: | ---: | ---: |
${classRows}

## OLP Extension Policies

| Row | Extension | Policy class | Metadata file rows | Candidate after review |
| --- | --- | --- | ---: | --- |
${extRows}

## OLP Top-Level Policies

| Row | Top-level group | Policy class | Metadata file rows | Candidate after review |
| --- | --- | --- | ---: | --- |
${topRows}

## Book of Proof Route Policies

| Row | Source class | Route status | Policy class | Permission gate |
| --- | --- | --- | --- | --- |
${bopRows}

## Zero Gates

- Policy reviews completed: \`0\`
- Coordinate scans / source-text capture / excerpt selections authorized: \`0 / 0 / 0\`
- Source text/excerpt files: \`0\`
- Source text/definitions/examples copied: \`0 / 0 / 0\`
- Source passages selected: \`0\`
- Exact spans / candidate line ranges: \`0 / 0\`
- Translated passages: \`0\`
- Proposed bridge lexemes / morphemes / syntax / displays: \`0 / 0 / 0 / 0\`
- Accepted bridge surfaces / local-language terms: \`0 / 0\`
- Reviewer returns / license rechecks completed: \`0 / 0\`
- Readiness: \`publication=false, translation=false, constructed_surface=false, pilot=false\`

Boundary: policy classes only. This artifact authorizes no coordinate scan, source-text capture, excerpt selection, translation, constructed form, or readiness claim.
`;
}

function buildArtifactCsv(artifact) {
  const rows = [];
  rows.push(['section', 'row_id', 'source_family', 'source_group', 'policy_class', 'metadata_rows', 'candidate_after_review', 'permission_gate', 'review_completed'].map(csvCell).join(','));
  for (const row of [...artifact.olp_extension_policy_rows, ...artifact.olp_top_level_policy_rows, ...artifact.book_of_proof_route_policy_rows]) {
    rows.push([
      row.summary_kind,
      row.policy_row_id,
      row.source_family,
      row.source_group,
      row.policy_class,
      row.metadata_file_rows,
      row.coordinate_scan_candidate_after_review,
      row.permission_or_license_gate_required,
      row.policy_review_completed
    ].map(csvCell).join(','));
  }
  for (const row of artifact.policy_class_summary_rows) {
    rows.push([
      'policy_class_summary',
      row.policy_class_summary_row_id,
      '',
      '',
      row.policy_class,
      row.metadata_file_rows,
      row.coordinate_scan_candidate_after_review_rows,
      row.permission_or_license_gate_required_rows,
      row.policy_reviews_completed
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
    status: 'pointer_only_package154_proof_literacy_source_coordinate_policy_sheet_note_no_remote_action_no_source_text_no_translation_no_readiness',
    summary: 'Package 154 classifies proof-literacy metadata inventory summaries into source-coordinate policy rows without authorizing scans or excerpts.',
    counts: {
      source_coordinate_policy_rows: g.source_coordinate_policy_rows,
      coordinate_scan_candidate_after_review_rows: g.coordinate_scan_candidate_after_review_rows,
      permission_or_license_gate_required_rows: g.permission_or_license_gate_required_rows,
      blank_policy_review_cells_allocated: g.blank_policy_review_cells_allocated
    },
    zero_gates: {
      policy_reviews_completed: 0,
      coordinate_scans_authorized: 0,
      source_text_capture_authorized: 0,
      excerpt_selections_authorized: 0,
      source_text_or_excerpt_files_created: 0,
      source_text_copied: 0,
      source_passages_selected: 0,
      translated_passages: 0,
      proposed_bridge_lexemes: 0,
      accepted_bridge_surfaces: 0,
      reviewer_returns_ingested: 0,
      readiness_claims: 0
    },
    no_remote_action_by_this_note: true
  };
}

function buildNoteMd(note, artifact) {
  const g = artifact.gate_state;
  return `# Package 154 Proof-Literacy Source Coordinate Policy Sheet Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only local note: package 154 creates \`${g.source_coordinate_policy_rows}\` source-coordinate policy rows, including \`${g.coordinate_scan_candidate_after_review_rows}\` candidate-after-review rows and \`${g.permission_or_license_gate_required_rows}\` permission/license-gated rows.

Zero gates: \`0\` policy reviews completed, \`0\` coordinate scans authorized, \`0\` source-text capture authorized, \`0\` excerpt selections authorized, \`0\` source-text/excerpt files, \`0\` source text copied, \`0\` source passages selected, \`0\` translations, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` reviewer returns ingested, \`0\` readiness claims.

Boundary: metadata-derived policy sheet only. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, source-text, excerpt, proposed form, accepted surface, translation, publication, pilot, legal-advice, or remote-state claim.
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
  const packageRow = {
    order: packageOrder,
    role: 'open_translation_proof_literacy_source_coordinate_policy_sheet',
    artifact: artifactId,
    current_use: `${g.source_coordinate_policy_rows} source-coordinate policy rows; ${g.coordinate_scan_candidate_after_review_rows} candidate-after-review rows; ${g.blank_policy_review_cells_allocated} blank policy-review cells; 0 scans authorized, 0 source text, 0 excerpts, 0 translations, 0 forms, 0 readiness`
  };
  const existingPackageRowIndex = order.findIndex((row) => row?.artifact === artifactId);
  if (existingPackageRowIndex >= 0) order[existingPackageRowIndex] = { ...order[existingPackageRowIndex], ...packageRow };
  else order.push(packageRow);
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_open_translation_proof_literacy_source_coordinate_policy_sheet = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_proof_literacy_source_coordinate_policy_rows: g.source_coordinate_policy_rows,
    current_proof_literacy_coordinate_scan_candidate_after_review_rows: g.coordinate_scan_candidate_after_review_rows,
    current_proof_literacy_source_text_or_excerpt_files: 0,
    current_proof_literacy_translated_passages: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_policy_review_return_template_or_permission_route_decision_template_only_no_source_text_no_excerpts_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'Open translation proof-literacy source coordinate policy sheet',
    route: artifactId,
    license_status_to_recheck: 'policy_sheet_only_recheck_OLP_license_and_Book_of_Proof_permission_route_before_any_coordinate_scan_excerpt_adaptation_or_translation',
    best_translation_use: 'metadata-derived policy classifier for OLP and Book of Proof proof-literacy coordinate routes before later review returns or permission decisions',
    candidate_lanes: [
      'proof_literacy',
      'Open_Logic_Project',
      'Book_of_Proof',
      'source_coordinate_policy',
      'permission_gate_review'
    ],
    priority: 1,
    status: 'source_coordinate_policy_sheet_no_policy_returns_no_scans_no_source_text_no_excerpts_no_translation_no_forms_no_pilot',
    gate_state: {
      source_coordinate_policy_rows: g.source_coordinate_policy_rows,
      coordinate_scan_candidate_after_review_rows: g.coordinate_scan_candidate_after_review_rows,
      policy_reviews_completed: 0,
      coordinate_scans_authorized: 0,
      source_text_or_excerpt_files_created: 0,
      source_text_copied: 0,
      translated_passages: 0,
      proposed_bridge_lexemes: 0,
      accepted_bridge_surfaces: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_open_translation_proof_literacy_source_coordinate_policy_sheet: ${artifactId}_${g.source_coordinate_policy_rows}_policy_rows_${g.coordinate_scan_candidate_after_review_rows}_candidate_after_review_rows_0_scans_0_source_text_0_excerpts_0_translation_upload_when_path_exists_no_mobile_plan_deferral`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_open_translation_proof_literacy_source_coordinate_policy_sheet_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_open_translation_proof_literacy_source_coordinate_policy_sheet_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_proof_literacy_source_coordinate_policy_rows: g.source_coordinate_policy_rows,
    current_proof_literacy_coordinate_scan_candidate_after_review_rows: g.coordinate_scan_candidate_after_review_rows,
    current_proof_literacy_source_text_or_excerpt_files: 0,
    current_proof_literacy_translated_passages: 0,
    current_proof_literacy_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_open_translation_proof_literacy_source_coordinate_policy_sheet = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_open_translation_proof_literacy_source_coordinate_policy_sheet: ${artifactId}_policy_classes_before_any_coordinate_scan_results_excerpts_translations_surfaces_or_pilot_claims`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_open_translation_proof_literacy_source_coordinate_policy_sheet = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: classifies proof-literacy metadata inventory into ${g.source_coordinate_policy_rows} source-coordinate policy rows with ${g.coordinate_scan_candidate_after_review_rows} candidate-after-review rows and ${g.permission_or_license_gate_required_rows} permission-gated rows; substantive upload-bound artifact; 0 scans authorized, 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, 0 readiness.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - Proof-literacy source coordinate policy sheet; ${g.source_coordinate_policy_rows} policy rows, ${g.coordinate_scan_candidate_after_review_rows} candidate-after-review rows, 0 scans authorized, 0 source text, 0 excerpts, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 154: proof-literacy source-coordinate policy sheet for OLP and Book of Proof. It records ${g.source_coordinate_policy_rows} policy rows and ${g.coordinate_scan_candidate_after_review_rows} candidate-after-review rows while keeping 0 coordinate scans authorized, 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, and all readiness gates closed. It is upload-bound as substantive catalog/control work when a valid staging path exists.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | Open translation proof-literacy source coordinate policy sheet | ${artifactId} | Metadata-derived OLP and Book of Proof coordinate policy; ${g.source_coordinate_policy_rows} rows, 0 scans authorized, 0 source text, 0 excerpts, 0 translation, upload when path exists. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_open_translation_proof_literacy_source_coordinate_policy_sheet_artifact: \`${artifactId}\` (${g.source_coordinate_policy_rows} policy rows; 0 scans authorized; 0 source text; 0 excerpts; 0 accepted surfaces or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_open_translation_proof_literacy_source_coordinate_policy_sheet: \`${artifactId}\`; metadata-derived proof-literacy coordinate policy for OLP plus Book of Proof, no scans authorized, source text, excerpts, accepted terms, surfaces, translation, or pilot.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: proof-literacy source-coordinate policy sheet over OLP and Book of Proof routes; substantive and upload-bound, but not a policy return, scan authorization, source excerpt, translation, constructed form, license clearance, or readiness claim.`);
}

async function rebuildUploadQueueMd(queue) {
  const rows = (queue.queued_items || []).map((item) => `| \`${item.filename}\` | ${titleClass(item.class)} | ${formatNumber(item.bytes)} | \`${item.sha256}\` |`).join('\n');
  const sourcePdfFiles = (queue.summary.source_pdf_files || 0) + (queue.summary.source_image_files || 0);
  const stagingOrder = Array.isArray(queue.staging_order) ? queue.staging_order : [];
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

${stagingOrder.map((step, index) => `${index + 1}. ${step}`).join('\n')}

## Boundary

This is not a manifest update, payload validator update, Git commit claim, remote branch claim, PR update, Zenodo publication, canonical-readiness claim, translation-readiness claim, or secret-storage artifact.
`;
  await writeFile(path.join(outputs, `${uploadQueueFile}.md`), md, 'utf8');
}

async function updateUploadQueue() {
  const upload = await readJson(uploadQueueFile);
  const files = [
    { filename: `${artifactId}.json`, class: 'open_translation_proof_literacy_source_coordinate_policy_sheet' },
    { filename: `${artifactId}.md`, class: 'open_translation_proof_literacy_source_coordinate_policy_sheet' },
    { filename: `${artifactId}.csv`, class: 'open_translation_proof_literacy_source_coordinate_policy_sheet' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'open_translation_package154_coordination_note' },
    { filename: `${noteId}.md`, class: 'open_translation_package154_coordination_note' },
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
  upload.obj.package154_upload_queue_update = {
    captured_utc: '2026-07-03T08:47:00Z',
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
  const step = 'Stage package 154 proof-literacy source coordinate policy sheet artifacts as substantive beyond-core translation/source-route catalog material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (g.source_coordinate_policy_rows !== artifact.validation_snapshot.expected_source_coordinate_policy_rows) failures.push(`policy_rows_mismatch_${g.source_coordinate_policy_rows}`);
  if (g.olp_extension_policy_rows !== artifact.validation_snapshot.expected_olp_extension_policy_rows) failures.push(`olp_ext_rows_mismatch_${g.olp_extension_policy_rows}`);
  if (g.olp_top_level_policy_rows !== artifact.validation_snapshot.expected_olp_top_level_policy_rows) failures.push(`olp_top_rows_mismatch_${g.olp_top_level_policy_rows}`);
  if (g.book_of_proof_route_policy_rows !== artifact.validation_snapshot.expected_book_of_proof_route_policy_rows) failures.push(`bop_policy_rows_mismatch_${g.book_of_proof_route_policy_rows}`);
  if (g.coordinate_scan_candidate_after_review_rows < artifact.validation_snapshot.expected_min_coordinate_scan_candidate_after_review_rows) failures.push(`too_few_candidate_after_review_rows_${g.coordinate_scan_candidate_after_review_rows}`);
  if (g.blank_policy_review_fields_per_row !== artifact.validation_snapshot.expected_blank_policy_review_fields_per_row) failures.push(`blank_fields_mismatch_${g.blank_policy_review_fields_per_row}`);
  if (g.blank_policy_review_cells_allocated !== artifact.validation_snapshot.expected_blank_policy_review_cells_allocated) failures.push(`blank_cells_mismatch_${g.blank_policy_review_cells_allocated}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  const rows = [...artifact.olp_extension_policy_rows, ...artifact.olp_top_level_policy_rows, ...artifact.book_of_proof_route_policy_rows];
  for (const row of rows) {
    const filled = policyReviewFields.some((field) => row[field] !== null);
    if (filled || row.policy_review_fields_filled !== 0 || row.policy_review_completed || row.coordinate_scan_authorized || row.source_text_capture_authorized || row.excerpt_selection_authorized || row.translation_authorized) {
      failures.push(`nonblank_or_open_policy_row_${row.policy_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const parent = (await readJson(parentInventoryFile)).obj;
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
  bandwidth_mode: upload.bandwidth_mode,
  source_text_or_excerpt_files: upload.summary?.source_text_or_excerpt_files,
  source_coordinate_policy_rows: artifact.gate_state.source_coordinate_policy_rows,
  coordinate_scan_candidate_after_review_rows: artifact.gate_state.coordinate_scan_candidate_after_review_rows,
  permission_or_license_gate_required_rows: artifact.gate_state.permission_or_license_gate_required_rows,
  blank_policy_review_cells_allocated: artifact.gate_state.blank_policy_review_cells_allocated,
  policy_reviews_completed: artifact.gate_state.policy_reviews_completed,
  coordinate_scans_authorized: artifact.gate_state.coordinate_scans_authorized,
  source_text_copied: artifact.gate_state.source_text_copied,
  translated_passages: artifact.gate_state.translated_passages,
  proposed_bridge_lexemes: artifact.gate_state.proposed_bridge_lexemes,
  accepted_bridge_surfaces: artifact.gate_state.accepted_bridge_surfaces,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
