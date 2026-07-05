import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OPEN_TRANSLATION_ALGEBRA_SOURCE_COORDINATE_POLICY_SHEET_20260703T093000Z';
const noteId = 'OPEN_TRANSLATION_ALGEBRA_SOURCE_COORDINATE_POLICY_SHEET_NOTE_20260703T093100Z';
const generatedUtc = '2026-07-03T09:30:00Z';
const noteGeneratedUtc = '2026-07-03T09:31:00Z';
const packageOrder = 157;
const queueCandidateId = 'OTCQ-OPEN-TRANSLATION-ALGEBRA-SOURCE-COORDINATE-POLICY-SHEET-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';
const parentInventoryFile = 'OPEN_TRANSLATION_ALGEBRA_METADATA_INVENTORY_SCAN_START_20260703T091500Z';
const parentRouterFile = 'OPEN_TRANSLATION_REVIEW_ONLY_SOURCE_COORDINATE_SCAN_ROUTER_20260703T081500Z';
const parentShelfFile = 'OPEN_TRANSLATION_REVIEW_ONLY_PACKET_SOURCE_SHELF_REFRESH_20260703T080000Z';

const policyReviewFields = [
  'policy_review_date',
  'reviewer_route_or_role',
  'policy_class_accepted',
  'coordinate_scan_scope_decision',
  'license_or_permission_gate_decision',
  'attribution_sidecar_decision',
  'support_only_route_confirmation',
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

function classifySourceClass(sourceClass) {
  if (sourceClass === 'github_api_contents') {
    return {
      policy_class: 'source_tree_contents_coordinate_candidate',
      scan_scope: 'future_source_tree_coordinate_scan_candidate_after_license_attribution_review',
      why: 'GitHub contents metadata names the source-tree route without copying file content.',
      candidate_after_review: true,
      license_gate_required: true
    };
  }
  if (sourceClass === 'repo_license_file') {
    return {
      policy_class: 'license_support_required_before_coordinate_scan',
      scan_scope: 'license_route_support_only_until_review_return',
      why: 'License records must be reviewed before any coordinate scan can lead toward excerpts or adaptations.',
      candidate_after_review: false,
      license_gate_required: true
    };
  }
  if (sourceClass === 'public_book_site') {
    return {
      policy_class: 'public_book_route_support_only',
      scan_scope: 'public_route_identity_metadata_only_no_excerpt_selection',
      why: 'Public book routes support source identity and access but do not by themselves authorize coordinate capture.',
      candidate_after_review: false,
      license_gate_required: true
    };
  }
  if (sourceClass === 'github_api_metadata' || sourceClass === 'github_api_branch_metadata') {
    return {
      policy_class: 'repository_identity_support_only',
      scan_scope: 'repository_identity_and_exact_branch_metadata_only',
      why: 'Repository and branch metadata support exact-source identity, not source passage selection.',
      candidate_after_review: false,
      license_gate_required: false
    };
  }
  return {
    policy_class: 'repository_support_metadata_only',
    scan_scope: 'repository_support_metadata_only_no_excerpt_selection',
    why: 'This route supports build, README, changes, project, or requirements context rather than direct algebra passage selection.',
    candidate_after_review: false,
    license_gate_required: false
  };
}

function classifyRouteUse(routeUse) {
  if (routeUse === 'source_tree_inventory_candidate') {
    return {
      policy_class: 'source_tree_inventory_coordinate_candidate',
      scan_scope: 'future_source_tree_coordinate_scan_candidate_after_policy_return',
      why: 'The route-use class already marks source-tree inventory as the plausible later coordinate layer.',
      candidate_after_review: true,
      license_gate_required: true
    };
  }
  if (routeUse === 'license_support_only') {
    return {
      policy_class: 'license_gate_support_only',
      scan_scope: 'license_support_metadata_only_until_review_return',
      why: 'License support rows are gates, not coordinate sources.',
      candidate_after_review: false,
      license_gate_required: true
    };
  }
  if (routeUse === 'public_route_support_only') {
    return {
      policy_class: 'public_route_support_only',
      scan_scope: 'public_route_support_metadata_only_no_excerpt_selection',
      why: 'Public route support helps access and attribution routing but does not authorize source text capture.',
      candidate_after_review: false,
      license_gate_required: true
    };
  }
  return {
    policy_class: 'support_route_metadata_only',
    scan_scope: 'support_route_metadata_only_no_excerpt_selection',
    why: 'This route-use class supports exact-source context rather than direct coordinate scan authorization.',
    candidate_after_review: false,
    license_gate_required: false
  };
}

function classifyContentsExtension(extension) {
  if (extension === '.xml' || extension === '.ptx') {
    return {
      policy_class: 'source_markup_coordinate_candidate',
      scan_scope: 'future_markup_file_coordinate_scan_candidate_after_policy_return',
      why: 'XML/PTX markup dominates the algebra contents inventory and is the natural future coordinate substrate.',
      candidate_after_review: true,
      license_gate_required: true
    };
  }
  if (extension === '.txt' || extension === '.md') {
    return {
      policy_class: 'repository_text_support_only',
      scan_scope: 'support_text_metadata_only_license_or_readme_context_no_excerpt_selection',
      why: 'Text/Markdown support files may inform license or route identity but should not become algebra excerpt sources without a separate decision.',
      candidate_after_review: false,
      license_gate_required: true
    };
  }
  return {
    policy_class: 'non_source_or_unclassified_support_only',
    scan_scope: 'non_source_or_unclassified_metadata_only_hold_for_manual_review',
    why: 'This extension is not a direct algebra source-coordinate target in this policy sheet.',
    candidate_after_review: false,
    license_gate_required: false
  };
}

function classifyContentsType(typeName) {
  if (typeName === 'file') {
    return {
      policy_class: 'file_item_coordinate_candidate_after_review',
      scan_scope: 'future_file_item_coordinate_scan_candidate_after_license_and_policy_return',
      why: 'File items can be routed to future coordinate scans after license and attribution gates.',
      candidate_after_review: true,
      license_gate_required: true
    };
  }
  if (typeName === 'dir') {
    return {
      policy_class: 'directory_item_support_only',
      scan_scope: 'directory_item_metadata_only_until_recursive_inventory_exists',
      why: 'Directory items require a later recursive inventory before any coordinate scan can be specified.',
      candidate_after_review: false,
      license_gate_required: false
    };
  }
  return {
    policy_class: 'contents_item_support_only',
    scan_scope: 'contents_item_metadata_only',
    why: 'No direct coordinate policy is assigned to this contents item type.',
    candidate_after_review: false,
    license_gate_required: false
  };
}

function classifyPacket(packetShape) {
  return {
    policy_class: `${packetShape}_metadata_policy_gate`,
    scan_scope: 'packet_candidate_requires_source_family_policy_return_before_coordinate_scan',
    why: 'Packet candidate rows identify translation use lanes but do not authorize any source-text or coordinate scan work.',
    candidate_after_review: false,
    license_gate_required: true
  };
}

function blankPolicyReview(rowId, sourceFamily, sourceGroup, summaryKind, metadataRows, metadataBytes, cls) {
  return {
    policy_row_id: rowId,
    source_family: sourceFamily,
    source_group: sourceGroup,
    summary_kind: summaryKind,
    policy_class: cls.policy_class,
    coordinate_scan_scope_policy: cls.scan_scope,
    policy_reason_metadata_only: cls.why,
    metadata_rows: metadataRows,
    metadata_bytes: metadataBytes,
    coordinate_scan_candidate_after_review: cls.candidate_after_review,
    license_or_permission_gate_required: cls.license_gate_required,
    blank_policy_review_fields: policyReviewFields,
    policy_review_date: null,
    reviewer_route_or_role: null,
    policy_class_accepted: null,
    coordinate_scan_scope_decision: null,
    license_or_permission_gate_decision: null,
    attribution_sidecar_decision: null,
    support_only_route_confirmation: null,
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

function buildSourceClassPolicyRows(parent) {
  return parent.source_class_summary_rows.map((summary, index) => {
    const cls = classifySourceClass(summary.group_key);
    return {
      ...blankPolicyReview(
        `ALG-SCP-SRC-CLASS-${String(index + 1).padStart(3, '0')}`,
        'FCLA/AATA algebra combined',
        summary.group_key,
        'source_class_summary',
        summary.rows,
        summary.bytes,
        cls
      ),
      parent_summary_row_id: summary.summary_row_id
    };
  });
}

function buildRouteUsePolicyRows(parent) {
  return parent.route_use_summary_rows.map((summary, index) => {
    const cls = classifyRouteUse(summary.group_key);
    return {
      ...blankPolicyReview(
        `ALG-SCP-ROUTE-USE-${String(index + 1).padStart(3, '0')}`,
        'FCLA/AATA algebra combined',
        summary.group_key,
        'route_use_summary',
        summary.rows,
        summary.bytes,
        cls
      ),
      parent_summary_row_id: summary.summary_row_id
    };
  });
}

function buildContentsExtensionPolicyRows(parent) {
  return parent.contents_extension_summary_rows.map((summary, index) => {
    const cls = classifyContentsExtension(summary.group_key);
    return {
      ...blankPolicyReview(
        `ALG-SCP-CONTENT-EXT-${String(index + 1).padStart(3, '0')}`,
        'FCLA/AATA algebra combined',
        summary.group_key,
        'contents_extension_summary',
        summary.rows,
        summary.bytes,
        cls
      ),
      parent_summary_row_id: summary.summary_row_id
    };
  });
}

function buildContentsTypePolicyRows(parent) {
  return parent.contents_type_summary_rows.map((summary, index) => {
    const cls = classifyContentsType(summary.group_key);
    return {
      ...blankPolicyReview(
        `ALG-SCP-CONTENT-TYPE-${String(index + 1).padStart(3, '0')}`,
        'FCLA/AATA algebra combined',
        summary.group_key,
        'contents_type_summary',
        summary.rows,
        summary.bytes,
        cls
      ),
      parent_summary_row_id: summary.summary_row_id
    };
  });
}

function buildPacketPolicyRows(parent) {
  return parent.algebra_packet_candidate_rows.map((row, index) => {
    const cls = classifyPacket(row.packet_shape);
    return {
      ...blankPolicyReview(
        `ALG-SCP-PACKET-${String(index + 1).padStart(3, '0')}`,
        row.source_family,
        row.packet_shape,
        'algebra_packet_candidate',
        row.contents_inventory_rows,
        0,
        cls
      ),
      parent_packet_candidate_row_id: row.algebra_packet_candidate_row_id,
      needed_next_artifact: row.needed_next_artifact
    };
  });
}

function buildPolicyClassSummaryRows(allRows) {
  const map = new Map();
  for (const row of allRows) {
    if (!map.has(row.policy_class)) {
      map.set(row.policy_class, {
        policy_class_summary_row_id: `ALG-SCP-CLASS-${String(map.size + 1).padStart(2, '0')}`,
        policy_class: row.policy_class,
        policy_rows: 0,
        metadata_rows: 0,
        metadata_bytes: 0,
        coordinate_scan_candidate_after_review_rows: 0,
        license_or_permission_gate_required_rows: 0,
        policy_reviews_completed: 0,
        coordinate_scans_authorized: 0,
        excerpt_selections_authorized: 0
      });
    }
    const entry = map.get(row.policy_class);
    entry.policy_rows += 1;
    entry.metadata_rows += row.metadata_rows || 0;
    entry.metadata_bytes += row.metadata_bytes || 0;
    if (row.coordinate_scan_candidate_after_review) entry.coordinate_scan_candidate_after_review_rows += 1;
    if (row.license_or_permission_gate_required) entry.license_or_permission_gate_required_rows += 1;
  }
  return [...map.values()].sort((a, b) => b.policy_rows - a.policy_rows || a.policy_class.localeCompare(b.policy_class));
}

function buildNextPolicyArtifactRows() {
  return [
    {
      next_policy_artifact_row_id: 'ALG-SCP-NEXT-01',
      lane: 'source_markup_policy',
      useful_next_artifact: 'OPEN_TRANSLATION_ALGEBRA_SOURCE_MARKUP_COORDINATE_POLICY_RETURN_TEMPLATE_<timestamp>',
      allowed_action_class: 'policy_return_template_only',
      source_text_or_excerpt_allowed_now: false
    },
    {
      next_policy_artifact_row_id: 'ALG-SCP-NEXT-02',
      lane: 'fcla_license_attribution_gate',
      useful_next_artifact: 'OPEN_TRANSLATION_LINEAR_ALGEBRA_FCLA_PERMISSION_ATTRIBUTION_DECISION_LEDGER_TEMPLATE_<timestamp>',
      allowed_action_class: 'permission_attribution_decision_template_only',
      source_text_or_excerpt_allowed_now: false
    },
    {
      next_policy_artifact_row_id: 'ALG-SCP-NEXT-03',
      lane: 'aata_license_attribution_gate',
      useful_next_artifact: 'OPEN_TRANSLATION_ABSTRACT_ALGEBRA_AATA_PERMISSION_ATTRIBUTION_DECISION_LEDGER_TEMPLATE_<timestamp>',
      allowed_action_class: 'permission_attribution_decision_template_only',
      source_text_or_excerpt_allowed_now: false
    },
    {
      next_policy_artifact_row_id: 'ALG-SCP-NEXT-04',
      lane: 'algebra_metadata_review',
      useful_next_artifact: 'OPEN_TRANSLATION_ALGEBRA_METADATA_INVENTORY_REVIEW_RETURN_LEDGER_TEMPLATE_<timestamp>',
      allowed_action_class: 'blank_return_template_only',
      source_text_or_excerpt_allowed_now: false
    }
  ];
}

function buildArtifact(parent) {
  const sourceClassPolicyRows = buildSourceClassPolicyRows(parent);
  const routeUsePolicyRows = buildRouteUsePolicyRows(parent);
  const contentsExtensionPolicyRows = buildContentsExtensionPolicyRows(parent);
  const contentsTypePolicyRows = buildContentsTypePolicyRows(parent);
  const packetPolicyRows = buildPacketPolicyRows(parent);
  const allRows = [
    ...sourceClassPolicyRows,
    ...routeUsePolicyRows,
    ...contentsExtensionPolicyRows,
    ...contentsTypePolicyRows,
    ...packetPolicyRows
  ];
  const policyClassSummaryRows = buildPolicyClassSummaryRows(allRows);
  const nextPolicyArtifactRows = buildNextPolicyArtifactRows();
  const blankPolicyReviewCells = allRows.length * policyReviewFields.length;
  const candidateAfterReviewRows = allRows.filter((row) => row.coordinate_scan_candidate_after_review).length;
  const licenseGateRows = allRows.filter((row) => row.license_or_permission_gate_required).length;

  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'algebra_source_coordinate_policy_sheet_no_policy_returns_no_scans_no_source_text_no_excerpts_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Classify package 156 FCLA/AATA algebra metadata inventory summaries into source-coordinate policy rows, distinguishing future markup/source-tree scan candidates from support-only, license-gated, public-route, repository-identity, and packet-gate rows without authorizing scans, copying source text, selecting excerpts, or starting translation.',
    parent_artifacts: [
      parentInventoryFile,
      parentRouterFile,
      parentShelfFile,
      'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z'
    ],
    boundary: {
      artifact_is: [
        'metadata-derived algebra coordinate policy sheet',
        'future scan-candidate classifier',
        'support-only and license-gate classifier',
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
      algebra_metadata_rows_total: parent.gate_state.algebra_metadata_rows_total,
      algebra_manifest_route_rows: parent.gate_state.algebra_manifest_route_rows,
      algebra_contents_inventory_rows: parent.gate_state.algebra_contents_inventory_rows,
      algebra_packet_candidate_rows: parent.gate_state.algebra_packet_candidate_rows
    },
    source_class_policy_rows: sourceClassPolicyRows,
    route_use_policy_rows: routeUsePolicyRows,
    contents_extension_policy_rows: contentsExtensionPolicyRows,
    contents_type_policy_rows: contentsTypePolicyRows,
    packet_policy_rows: packetPolicyRows,
    policy_class_summary_rows: policyClassSummaryRows,
    next_policy_artifact_rows: nextPolicyArtifactRows,
    gate_state: {
      algebra_source_coordinate_policy_rows: allRows.length,
      source_class_policy_rows: sourceClassPolicyRows.length,
      route_use_policy_rows: routeUsePolicyRows.length,
      contents_extension_policy_rows: contentsExtensionPolicyRows.length,
      contents_type_policy_rows: contentsTypePolicyRows.length,
      packet_policy_rows: packetPolicyRows.length,
      policy_class_summary_rows: policyClassSummaryRows.length,
      next_policy_artifact_rows: nextPolicyArtifactRows.length,
      coordinate_scan_candidate_after_review_rows: candidateAfterReviewRows,
      license_or_permission_gate_required_rows: licenseGateRows,
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
      expected_min_algebra_source_coordinate_policy_rows: 1,
      expected_source_class_policy_rows: parent.source_class_summary_rows.length,
      expected_route_use_policy_rows: parent.route_use_summary_rows.length,
      expected_contents_extension_policy_rows: parent.contents_extension_summary_rows.length,
      expected_contents_type_policy_rows: parent.contents_type_summary_rows.length,
      expected_packet_policy_rows: parent.algebra_packet_candidate_rows.length,
      expected_min_coordinate_scan_candidate_after_review_rows: 1,
      expected_blank_policy_review_fields_per_row: policyReviewFields.length,
      expected_blank_policy_review_cells_allocated: blankPolicyReviewCells,
      zero_gate_assertions: zeroGateKeys,
      readiness_claims: 0
    },
    next_valid_artifacts: nextPolicyArtifactRows.map((row) => row.useful_next_artifact),
    decision: 'Package 157 converts algebra metadata inventory summaries into a policy sheet. It names future scan-candidate classes but authorizes no scans, no source-text capture, no excerpts, no translations, no constructed forms, and no readiness.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const classRows = artifact.policy_class_summary_rows.map((row) => `| ${row.policy_class_summary_row_id} | ${row.policy_class} | ${row.policy_rows} | ${row.coordinate_scan_candidate_after_review_rows} | ${row.license_or_permission_gate_required_rows} |`).join('\n');
  const sourceRows = artifact.source_class_policy_rows.map((row) => `| ${row.policy_row_id} | ${row.source_group} | ${row.policy_class} | ${row.metadata_rows} | ${row.coordinate_scan_candidate_after_review} |`).join('\n');
  const extRows = artifact.contents_extension_policy_rows.map((row) => `| ${row.policy_row_id} | ${row.source_group} | ${row.policy_class} | ${row.metadata_rows} | ${row.coordinate_scan_candidate_after_review} |`).join('\n');
  const packetRows = artifact.packet_policy_rows.map((row) => `| ${row.policy_row_id} | ${row.source_family} | ${row.source_group} | ${row.policy_class} | ${row.license_or_permission_gate_required} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Counts

- Algebra source-coordinate policy rows: \`${g.algebra_source_coordinate_policy_rows}\`
- Source-class policy rows: \`${g.source_class_policy_rows}\`
- Route-use policy rows: \`${g.route_use_policy_rows}\`
- Contents-extension policy rows: \`${g.contents_extension_policy_rows}\`
- Contents-type policy rows: \`${g.contents_type_policy_rows}\`
- Packet policy rows: \`${g.packet_policy_rows}\`
- Candidate-after-review rows: \`${g.coordinate_scan_candidate_after_review_rows}\`
- License/permission gate rows: \`${g.license_or_permission_gate_required_rows}\`
- Blank policy-review cells: \`${g.blank_policy_review_cells_allocated}\`

## Policy Classes

| Row | Policy class | Rows | Candidate-after-review rows | License-gated rows |
| --- | --- | ---: | ---: | ---: |
${classRows}

## Source-Class Policies

| Row | Source class | Policy class | Metadata rows | Candidate after review |
| --- | --- | --- | ---: | --- |
${sourceRows}

## Contents-Extension Policies

| Row | Extension | Policy class | Metadata rows | Candidate after review |
| --- | --- | --- | ---: | --- |
${extRows}

## Packet Policies

| Row | Source family | Packet | Policy class | License gate |
| --- | --- | --- | --- | --- |
${packetRows}

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
  rows.push(['section', 'row_id', 'source_family', 'source_group', 'policy_class', 'metadata_rows', 'candidate_after_review', 'license_gate', 'review_completed'].map(csvCell).join(','));
  for (const row of [
    ...artifact.source_class_policy_rows,
    ...artifact.route_use_policy_rows,
    ...artifact.contents_extension_policy_rows,
    ...artifact.contents_type_policy_rows,
    ...artifact.packet_policy_rows
  ]) {
    rows.push([
      row.summary_kind,
      row.policy_row_id,
      row.source_family,
      row.source_group,
      row.policy_class,
      row.metadata_rows,
      row.coordinate_scan_candidate_after_review,
      row.license_or_permission_gate_required,
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
      row.metadata_rows,
      row.coordinate_scan_candidate_after_review_rows,
      row.license_or_permission_gate_required_rows,
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
    status: 'pointer_only_package157_algebra_source_coordinate_policy_sheet_note_no_remote_action_no_source_text_no_translation_no_readiness',
    summary: 'Package 157 classifies algebra metadata inventory summaries into source-coordinate policy rows without authorizing scans or excerpts.',
    counts: {
      algebra_source_coordinate_policy_rows: g.algebra_source_coordinate_policy_rows,
      coordinate_scan_candidate_after_review_rows: g.coordinate_scan_candidate_after_review_rows,
      license_or_permission_gate_required_rows: g.license_or_permission_gate_required_rows,
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
  return `# Package 157 Algebra Source Coordinate Policy Sheet Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only local note: package 157 creates \`${g.algebra_source_coordinate_policy_rows}\` algebra source-coordinate policy rows, including \`${g.coordinate_scan_candidate_after_review_rows}\` candidate-after-review rows and \`${g.license_or_permission_gate_required_rows}\` license/permission-gated rows.

Zero gates: \`0\` policy reviews completed, \`0\` coordinate scans authorized, \`0\` source-text capture authorized, \`0\` excerpt selections authorized, \`0\` source-text/excerpt files, \`0\` source text copied, \`0\` source passages selected, \`0\` translations, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` reviewer returns ingested, \`0\` readiness claims.

Boundary: metadata-derived algebra policy sheet only. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, source-text, excerpt, proposed form, accepted surface, translation, publication, pilot, legal-advice, or remote-state claim.
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
    role: 'open_translation_algebra_source_coordinate_policy_sheet',
    artifact: artifactId,
    current_use: `${g.algebra_source_coordinate_policy_rows} algebra source-coordinate policy rows; ${g.coordinate_scan_candidate_after_review_rows} candidate-after-review rows; ${g.blank_policy_review_cells_allocated} blank policy-review cells; 0 scans authorized, 0 source text, 0 excerpts, 0 translations, 0 forms, 0 readiness`
  };
  const existingPackageRowIndex = order.findIndex((row) => row?.artifact === artifactId);
  if (existingPackageRowIndex >= 0) order[existingPackageRowIndex] = { ...order[existingPackageRowIndex], ...packageRow };
  else order.push(packageRow);
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_open_translation_algebra_source_coordinate_policy_sheet = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_algebra_source_coordinate_policy_rows: g.algebra_source_coordinate_policy_rows,
    current_algebra_coordinate_scan_candidate_after_review_rows: g.coordinate_scan_candidate_after_review_rows,
    current_algebra_source_text_or_excerpt_files: 0,
    current_algebra_translated_passages: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_algebra_policy_review_return_template_or_permission_attribution_decision_template_only_no_source_text_no_excerpts_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'Open translation algebra source coordinate policy sheet',
    route: artifactId,
    license_status_to_recheck: 'policy_sheet_only_recheck_FCLA_and_AATA_license_permission_routes_before_any_coordinate_scan_excerpt_adaptation_or_translation',
    best_translation_use: 'metadata-derived policy classifier for FCLA and AATA algebra coordinate routes before later review returns or permission decisions',
    candidate_lanes: [
      'linear_algebra',
      'abstract_algebra',
      'FCLA',
      'AATA',
      'source_coordinate_policy',
      'permission_gate_review'
    ],
    priority: 1,
    status: 'algebra_source_coordinate_policy_sheet_no_policy_returns_no_scans_no_source_text_no_excerpts_no_translation_no_forms_no_pilot',
    gate_state: {
      algebra_source_coordinate_policy_rows: g.algebra_source_coordinate_policy_rows,
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
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_open_translation_algebra_source_coordinate_policy_sheet: ${artifactId}_${g.algebra_source_coordinate_policy_rows}_policy_rows_${g.coordinate_scan_candidate_after_review_rows}_candidate_after_review_rows_0_scans_0_source_text_0_excerpts_0_translation_upload_when_path_exists_no_mobile_plan_deferral`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_open_translation_algebra_source_coordinate_policy_sheet_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_open_translation_algebra_source_coordinate_policy_sheet_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_algebra_source_coordinate_policy_rows: g.algebra_source_coordinate_policy_rows,
    current_algebra_coordinate_scan_candidate_after_review_rows: g.coordinate_scan_candidate_after_review_rows,
    current_algebra_source_text_or_excerpt_files: 0,
    current_algebra_translated_passages: 0,
    current_algebra_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_open_translation_algebra_source_coordinate_policy_sheet = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_open_translation_algebra_source_coordinate_policy_sheet: ${artifactId}_policy_classes_before_any_coordinate_scan_results_excerpts_translations_surfaces_or_pilot_claims`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_open_translation_algebra_source_coordinate_policy_sheet = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: classifies algebra metadata inventory into ${g.algebra_source_coordinate_policy_rows} source-coordinate policy rows with ${g.coordinate_scan_candidate_after_review_rows} candidate-after-review rows and ${g.license_or_permission_gate_required_rows} license/permission-gated rows; substantive upload-bound artifact; 0 scans authorized, 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, 0 readiness.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - Algebra source coordinate policy sheet; ${g.algebra_source_coordinate_policy_rows} policy rows, ${g.coordinate_scan_candidate_after_review_rows} candidate-after-review rows, 0 scans authorized, 0 source text, 0 excerpts, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 157: algebra source-coordinate policy sheet for FCLA and AATA. It records ${g.algebra_source_coordinate_policy_rows} policy rows and ${g.coordinate_scan_candidate_after_review_rows} candidate-after-review rows while keeping 0 coordinate scans authorized, 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, and all readiness gates closed. It is upload-bound as substantive catalog/control work when a valid staging path exists.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | Open translation algebra source coordinate policy sheet | ${artifactId} | Metadata-derived FCLA/AATA coordinate policy; ${g.algebra_source_coordinate_policy_rows} rows, 0 scans authorized, 0 source text, 0 excerpts, 0 translation, upload when path exists. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_open_translation_algebra_source_coordinate_policy_sheet_artifact: \`${artifactId}\` (${g.algebra_source_coordinate_policy_rows} policy rows; 0 scans authorized; 0 source text; 0 excerpts; 0 accepted surfaces or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_open_translation_algebra_source_coordinate_policy_sheet: \`${artifactId}\`; metadata-derived algebra coordinate policy for FCLA plus AATA, no scans authorized, source text, excerpts, accepted terms, surfaces, translation, or pilot.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: algebra source-coordinate policy sheet over FCLA and AATA routes; substantive and upload-bound, but not a policy return, scan authorization, source excerpt, translation, constructed form, license clearance, or readiness claim.`);
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
    { filename: `${artifactId}.json`, class: 'open_translation_algebra_source_coordinate_policy_sheet' },
    { filename: `${artifactId}.md`, class: 'open_translation_algebra_source_coordinate_policy_sheet' },
    { filename: `${artifactId}.csv`, class: 'open_translation_algebra_source_coordinate_policy_sheet' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'open_translation_package157_coordination_note' },
    { filename: `${noteId}.md`, class: 'open_translation_package157_coordination_note' },
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
  upload.obj.package157_upload_queue_update = {
    captured_utc: '2026-07-03T09:32:00Z',
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
  const step = 'Stage package 157 algebra source coordinate policy sheet artifacts as substantive beyond-core translation/source-route catalog material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (g.algebra_source_coordinate_policy_rows < artifact.validation_snapshot.expected_min_algebra_source_coordinate_policy_rows) failures.push(`too_few_policy_rows_${g.algebra_source_coordinate_policy_rows}`);
  if (g.source_class_policy_rows !== artifact.validation_snapshot.expected_source_class_policy_rows) failures.push(`source_class_rows_mismatch_${g.source_class_policy_rows}`);
  if (g.route_use_policy_rows !== artifact.validation_snapshot.expected_route_use_policy_rows) failures.push(`route_use_rows_mismatch_${g.route_use_policy_rows}`);
  if (g.contents_extension_policy_rows !== artifact.validation_snapshot.expected_contents_extension_policy_rows) failures.push(`contents_ext_rows_mismatch_${g.contents_extension_policy_rows}`);
  if (g.contents_type_policy_rows !== artifact.validation_snapshot.expected_contents_type_policy_rows) failures.push(`contents_type_rows_mismatch_${g.contents_type_policy_rows}`);
  if (g.packet_policy_rows !== artifact.validation_snapshot.expected_packet_policy_rows) failures.push(`packet_rows_mismatch_${g.packet_policy_rows}`);
  if (g.coordinate_scan_candidate_after_review_rows < artifact.validation_snapshot.expected_min_coordinate_scan_candidate_after_review_rows) failures.push(`too_few_candidate_after_review_rows_${g.coordinate_scan_candidate_after_review_rows}`);
  if (g.blank_policy_review_fields_per_row !== artifact.validation_snapshot.expected_blank_policy_review_fields_per_row) failures.push(`blank_fields_mismatch_${g.blank_policy_review_fields_per_row}`);
  if (g.blank_policy_review_cells_allocated !== artifact.validation_snapshot.expected_blank_policy_review_cells_allocated) failures.push(`blank_cells_mismatch_${g.blank_policy_review_cells_allocated}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  const rows = [
    ...artifact.source_class_policy_rows,
    ...artifact.route_use_policy_rows,
    ...artifact.contents_extension_policy_rows,
    ...artifact.contents_type_policy_rows,
    ...artifact.packet_policy_rows
  ];
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
  algebra_source_coordinate_policy_rows: artifact.gate_state.algebra_source_coordinate_policy_rows,
  coordinate_scan_candidate_after_review_rows: artifact.gate_state.coordinate_scan_candidate_after_review_rows,
  license_or_permission_gate_required_rows: artifact.gate_state.license_or_permission_gate_required_rows,
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
