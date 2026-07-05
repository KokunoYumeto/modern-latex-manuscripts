import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_SOURCE_COORDINATE_POLICY_SHEET_20260703T101500Z';
const noteId = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_SOURCE_COORDINATE_POLICY_SHEET_NOTE_20260703T101600Z';
const generatedUtc = '2026-07-03T10:15:00Z';
const noteGeneratedUtc = '2026-07-03T10:16:00Z';
const packageOrder = 160;
const queueCandidateId = 'OTCQ-OPEN-TRANSLATION-OPENINTRO-NUMERACY-SOURCE-COORDINATE-POLICY-SHEET-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';
const parentInventoryFile = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_METADATA_INVENTORY_SCAN_START_20260703T100000Z';
const parentRouterFile = 'OPEN_TRANSLATION_REVIEW_ONLY_SOURCE_COORDINATE_SCAN_ROUTER_20260703T081500Z';
const parentShelfFile = 'OPEN_TRANSLATION_REVIEW_ONLY_PACKET_SOURCE_SHELF_REFRESH_20260703T080000Z';

const policyReviewFields = [
  'policy_review_date',
  'reviewer_route_or_role',
  'policy_class_accepted',
  'coordinate_scan_scope_decision',
  'license_attribution_share_alike_decision',
  'table_figure_dataset_policy_decision',
  'source_text_capture_decision',
  'packet_or_lane_scope_decision',
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
  'source_tables_copied',
  'source_figures_copied',
  'source_datasets_copied',
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

function classifyRouteClass(routeClass) {
  if (routeClass === 'pinned_quarto_index_source_route') {
    return {
      policy_class: 'pinned_quarto_source_candidate_after_policy_return',
      scan_scope: 'future_exact_quarto_coordinate_scan_candidate_after_license_attribution_and_share_alike_return',
      why: 'The pinned Quarto index route is the most plausible exact-source coordinate substrate, but it remains locked until policy return.',
      candidate_after_review: true,
      license_gate_required: true,
      attribution_sidecar_required: true,
      table_figure_dataset_policy_required: true
    };
  }
  if (routeClass === 'rendered_web_exact_edition_route' || routeClass === 'openintro_book_page_route') {
    return {
      policy_class: 'rendered_exact_edition_candidate_after_policy_return',
      scan_scope: 'future_rendered_edition_coordinate_scan_candidate_after_license_attribution_and_change_notice_return',
      why: 'Rendered OpenIntro routes can help exact-edition alignment only after route, license, attribution, and change-notice policy review.',
      candidate_after_review: true,
      license_gate_required: true,
      attribution_sidecar_required: true,
      table_figure_dataset_policy_required: true
    };
  }
  if (routeClass === 'license_share_alike_support_route') {
    return {
      policy_class: 'license_share_alike_support_gate',
      scan_scope: 'license_support_metadata_only_until_policy_return',
      why: 'License and share-alike routes are mandatory gates, not excerpt or translation sources.',
      candidate_after_review: false,
      license_gate_required: true,
      attribution_sidecar_required: true,
      table_figure_dataset_policy_required: false
    };
  }
  if (routeClass === 'pdf_route_evidence_only') {
    return {
      policy_class: 'pdf_route_evidence_hold',
      scan_scope: 'pdf_route_evidence_only_no_coordinate_scan_until_pdf_file_policy_and_file_capture_decision',
      why: 'The PDF route is evidence-only in the parent inventory because no PDF file was downloaded or hashed.',
      candidate_after_review: false,
      license_gate_required: true,
      attribution_sidecar_required: true,
      table_figure_dataset_policy_required: true
    };
  }
  if (routeClass === 'repository_readme_support_route' || routeClass === 'pinned_quarto_config_support_route') {
    return {
      policy_class: 'repository_metadata_support_only',
      scan_scope: 'repository_metadata_support_only_no_excerpt_selection',
      why: 'README and configuration routes support repository identity and attribution context, not numeracy source passage capture.',
      candidate_after_review: false,
      license_gate_required: true,
      attribution_sidecar_required: true,
      table_figure_dataset_policy_required: false
    };
  }
  return {
    policy_class: 'public_family_route_support_only',
    scan_scope: 'public_route_support_metadata_only_no_excerpt_selection',
    why: 'This route helps source family orientation but does not authorize coordinate scan or source text capture.',
    candidate_after_review: false,
    license_gate_required: true,
    attribution_sidecar_required: true,
    table_figure_dataset_policy_required: false
  };
}

function classifyExactRouteUse(routeUse) {
  const lower = String(routeUse).toLowerCase();
  if (lower.includes('pinned_quarto_index_source')) {
    return {
      policy_class: 'pinned_quarto_exact_route_candidate_after_policy_return',
      scan_scope: 'future_pinned_quarto_coordinate_scan_candidate_after_policy_return',
      why: 'This exact route-use class is the pinned source route, but no coordinate scan is authorized yet.',
      candidate_after_review: true,
      license_gate_required: true,
      attribution_sidecar_required: true,
      table_figure_dataset_policy_required: true
    };
  }
  if (lower.includes('rendered_ims2_web_edition') || lower.includes('openintro_ims_book_route')) {
    return {
      policy_class: 'rendered_exact_route_candidate_after_policy_return',
      scan_scope: 'future_rendered_route_coordinate_scan_candidate_after_policy_return',
      why: 'Rendered exact-edition routes may later align section coordinates after policy review.',
      candidate_after_review: true,
      license_gate_required: true,
      attribution_sidecar_required: true,
      table_figure_dataset_policy_required: true
    };
  }
  if (lower.includes('license') || lower.includes('legalcode') || lower.includes('attribution') || lower.includes('share_alike')) {
    return {
      policy_class: 'license_attribution_route_support_gate',
      scan_scope: 'license_attribution_support_only_until_decision_return',
      why: 'License, legalcode, attribution, and share-alike rows are decision support gates.',
      candidate_after_review: false,
      license_gate_required: true,
      attribution_sidecar_required: true,
      table_figure_dataset_policy_required: false
    };
  }
  if (lower.includes('pdf')) {
    return {
      policy_class: 'pdf_route_evidence_hold',
      scan_scope: 'pdf_route_evidence_only_no_coordinate_scan_until_file_policy_return',
      why: 'PDF route evidence remains locked because the PDF file itself is not captured in the parent inventory.',
      candidate_after_review: false,
      license_gate_required: true,
      attribution_sidecar_required: true,
      table_figure_dataset_policy_required: true
    };
  }
  return {
    policy_class: 'exact_route_support_metadata_only',
    scan_scope: 'exact_route_support_metadata_only_no_excerpt_selection',
    why: 'This exact route-use row supports edition identity, repository context, or source-family comparison.',
    candidate_after_review: false,
    license_gate_required: true,
    attribution_sidecar_required: true,
    table_figure_dataset_policy_required: false
  };
}

function classifyExtension(extension) {
  if (extension === '.qmd') {
    return {
      policy_class: 'quarto_markup_extension_candidate_after_policy_return',
      scan_scope: 'future_quarto_markup_coordinate_scan_candidate_after_policy_return',
      why: 'Quarto source markup is the likely later coordinate substrate, but this policy sheet only classifies it.',
      candidate_after_review: true,
      license_gate_required: true,
      attribution_sidecar_required: true,
      table_figure_dataset_policy_required: true
    };
  }
  if (extension === '.html') {
    return {
      policy_class: 'mixed_html_route_policy_hold',
      scan_scope: 'mixed_html_support_and_rendered_routes_hold_for_row_level_policy',
      why: 'HTML rows mix license, public pages, and rendered edition routes, so extension-level policy must stay conservative.',
      candidate_after_review: false,
      license_gate_required: true,
      attribution_sidecar_required: true,
      table_figure_dataset_policy_required: true
    };
  }
  if (extension === '.md' || extension === '.yml') {
    return {
      policy_class: 'repository_support_extension_only',
      scan_scope: 'repository_support_extension_metadata_only_no_excerpt_selection',
      why: 'Markdown and YAML rows in the parent inventory support repository identity and metadata rather than passage capture.',
      candidate_after_review: false,
      license_gate_required: true,
      attribution_sidecar_required: true,
      table_figure_dataset_policy_required: false
    };
  }
  return {
    policy_class: 'unclassified_extension_support_only',
    scan_scope: 'extension_metadata_only_hold_for_manual_review',
    why: 'This extension is not classified as a direct numeracy source-coordinate target.',
    candidate_after_review: false,
    license_gate_required: true,
    attribution_sidecar_required: true,
    table_figure_dataset_policy_required: false
  };
}

function classifyPacketSlot(slot) {
  const tableFigurePolicy = slot.neutral_packet_slot === 'tables_and_graphs';
  return {
    policy_class: tableFigurePolicy ? 'numeracy_packet_scope_table_figure_gate' : 'numeracy_packet_scope_support_gate',
    scan_scope: 'packet_scope_support_only_until_source_coordinate_policy_return_and_local_reviewer_scope_decision',
    why: 'Packet slots are useful translation candidates only after exact source, attribution, share-alike, and local-language scope decisions.',
    candidate_after_review: false,
    license_gate_required: true,
    attribution_sidecar_required: true,
    table_figure_dataset_policy_required: tableFigurePolicy
  };
}

function classifyLaneFit() {
  return {
    policy_class: 'world_family_lane_fit_support_only',
    scan_scope: 'lane_fit_support_only_no_language_surface_or_translation_authorized',
    why: 'Lane-fit rows preserve cross-session usefulness without substituting for local language authority, source-route, or orthography review.',
    candidate_after_review: false,
    license_gate_required: true,
    attribution_sidecar_required: true,
    table_figure_dataset_policy_required: false
  };
}

function blankPolicyReview(rowId, sourceGroup, groupType, metadataRows, metadataBytes, cls) {
  return {
    policy_row_id: rowId,
    source_family: 'OpenIntro IMS statistics and numeracy',
    source_group: sourceGroup,
    group_type: groupType,
    policy_class: cls.policy_class,
    coordinate_scan_scope: cls.scan_scope,
    why_this_policy_class: cls.why,
    metadata_rows: metadataRows || 0,
    metadata_bytes: metadataBytes || 0,
    coordinate_scan_candidate_after_review: cls.candidate_after_review,
    license_or_permission_gate_required: cls.license_gate_required,
    attribution_sidecar_required: cls.attribution_sidecar_required,
    table_figure_dataset_policy_required: cls.table_figure_dataset_policy_required,
    source_text_capture_allowed_now: false,
    excerpt_selection_allowed_now: false,
    translation_allowed_now: false,
    constructed_surface_allowed_now: false,
    blank_policy_review_fields: policyReviewFields,
    policy_review_date: null,
    reviewer_route_or_role: null,
    policy_class_accepted: null,
    coordinate_scan_scope_decision: null,
    license_attribution_share_alike_decision: null,
    table_figure_dataset_policy_decision: null,
    source_text_capture_decision: null,
    packet_or_lane_scope_decision: null,
    next_allowed_artifact: null,
    review_note_without_source_prose: null,
    policy_review_fields_filled: 0,
    policy_review_completed: false,
    coordinate_scan_authorized: false,
    source_text_capture_authorized: false,
    excerpt_selection_authorized: false,
    translation_authorized: false,
    still_locked_reason: 'policy_classification_only_no_policy_return_no_coordinate_scan_authorization_no_source_text_no_excerpt_no_translation'
  };
}

function buildRouteClassPolicyRows(parent) {
  return parent.route_class_summary_rows.map((summary, index) => ({
    ...blankPolicyReview(
      `OI-SCP-ROUTE-CLASS-${String(index + 1).padStart(3, '0')}`,
      summary.group_key,
      'route_class_summary',
      summary.rows,
      summary.bytes,
      classifyRouteClass(summary.group_key)
    ),
    parent_summary_row_id: summary.summary_row_id
  }));
}

function buildExactRouteUsePolicyRows(parent) {
  return parent.exact_route_use_summary_rows.map((summary, index) => ({
    ...blankPolicyReview(
      `OI-SCP-EXACT-USE-${String(index + 1).padStart(3, '0')}`,
      summary.group_key,
      'exact_route_use_summary',
      summary.rows,
      summary.bytes,
      classifyExactRouteUse(summary.group_key)
    ),
    parent_summary_row_id: summary.summary_row_id
  }));
}

function buildExtensionPolicyRows(parent) {
  return parent.extension_summary_rows.map((summary, index) => ({
    ...blankPolicyReview(
      `OI-SCP-EXT-${String(index + 1).padStart(3, '0')}`,
      summary.group_key,
      'extension_summary',
      summary.rows,
      summary.bytes,
      classifyExtension(summary.group_key)
    ),
    parent_summary_row_id: summary.summary_row_id
  }));
}

function buildPacketSlotPolicyRows(parent) {
  return parent.numeracy_packet_slot_rows.map((slot, index) => ({
    ...blankPolicyReview(
      `OI-SCP-PACKET-${String(index + 1).padStart(3, '0')}`,
      slot.neutral_packet_slot,
      'numeracy_packet_slot',
      1,
      0,
      classifyPacketSlot(slot)
    ),
    parent_packet_slot_row_id: slot.numeracy_packet_slot_row_id,
    source_fit: slot.source_fit,
    still_required: slot.still_required
  }));
}

function buildLaneFitPolicyRows(parent) {
  return parent.numeracy_lane_fit_rows.map((lane, index) => ({
    ...blankPolicyReview(
      `OI-SCP-LANE-${String(index + 1).padStart(3, '0')}`,
      lane.lane_group,
      'numeracy_lane_fit',
      1,
      0,
      classifyLaneFit(lane)
    ),
    parent_lane_fit_row_id: lane.numeracy_lane_fit_row_id,
    first_use: lane.first_use,
    lane_gate: lane.gate
  }));
}

function buildPolicyClassSummaryRows(allRows) {
  const map = new Map();
  for (const row of allRows) {
    if (!map.has(row.policy_class)) {
      map.set(row.policy_class, {
        policy_class_summary_row_id: `OI-SCP-CLASS-${String(map.size + 1).padStart(2, '0')}`,
        policy_class: row.policy_class,
        policy_rows: 0,
        metadata_rows: 0,
        metadata_bytes: 0,
        coordinate_scan_candidate_after_review_rows: 0,
        license_or_permission_gate_required_rows: 0,
        attribution_sidecar_required_rows: 0,
        table_figure_dataset_policy_required_rows: 0,
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
    if (row.attribution_sidecar_required) entry.attribution_sidecar_required_rows += 1;
    if (row.table_figure_dataset_policy_required) entry.table_figure_dataset_policy_required_rows += 1;
  }
  return [...map.values()].sort((a, b) => b.policy_rows - a.policy_rows || a.policy_class.localeCompare(b.policy_class));
}

function buildNextPolicyArtifactRows() {
  return [
    {
      next_policy_artifact_row_id: 'OI-SCP-NEXT-01',
      lane: 'policy_review_return',
      useful_next_artifact: 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_POLICY_REVIEW_RETURN_LEDGER_TEMPLATE_<timestamp>',
      allowed_action_class: 'blank_policy_return_template_only',
      source_text_or_excerpt_allowed_now: false
    },
    {
      next_policy_artifact_row_id: 'OI-SCP-NEXT-02',
      lane: 'license_attribution_share_alike',
      useful_next_artifact: 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_ATTRIBUTION_SHAREALIKE_DECISION_LEDGER_TEMPLATE_<timestamp>',
      allowed_action_class: 'license_attribution_share_alike_decision_template_only',
      source_text_or_excerpt_allowed_now: false
    },
    {
      next_policy_artifact_row_id: 'OI-SCP-NEXT-03',
      lane: 'selected_excerpt_sidecar',
      useful_next_artifact: 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_SELECTED_EXCERPT_SIDECAR_TEMPLATE_<timestamp>',
      allowed_action_class: 'sidecar_template_only_after_policy_return',
      source_text_or_excerpt_allowed_now: false
    },
    {
      next_policy_artifact_row_id: 'OI-SCP-NEXT-04',
      lane: 'packet_scope_review',
      useful_next_artifact: 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_PACKET_SCOPE_REVIEW_TEMPLATE_<timestamp>',
      allowed_action_class: 'packet_scope_review_template_only',
      source_text_or_excerpt_allowed_now: false
    },
    {
      next_policy_artifact_row_id: 'OI-SCP-NEXT-05',
      lane: 'local_language_source_alignment',
      useful_next_artifact: 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_LANGUAGE_SOURCE_ALIGNMENT_TEMPLATE_<timestamp>',
      allowed_action_class: 'local_reviewer_alignment_template_only',
      source_text_or_excerpt_allowed_now: false
    }
  ];
}

function buildArtifact(parent) {
  const routeClassPolicyRows = buildRouteClassPolicyRows(parent);
  const exactRouteUsePolicyRows = buildExactRouteUsePolicyRows(parent);
  const extensionPolicyRows = buildExtensionPolicyRows(parent);
  const packetSlotPolicyRows = buildPacketSlotPolicyRows(parent);
  const laneFitPolicyRows = buildLaneFitPolicyRows(parent);
  const allRows = [
    ...routeClassPolicyRows,
    ...exactRouteUsePolicyRows,
    ...extensionPolicyRows,
    ...packetSlotPolicyRows,
    ...laneFitPolicyRows
  ];
  const policyClassSummaryRows = buildPolicyClassSummaryRows(allRows);
  const nextPolicyArtifactRows = buildNextPolicyArtifactRows();
  const candidateAfterReviewRows = allRows.filter((row) => row.coordinate_scan_candidate_after_review).length;
  const licenseGateRows = allRows.filter((row) => row.license_or_permission_gate_required).length;
  const attributionRows = allRows.filter((row) => row.attribution_sidecar_required).length;
  const tableFigureDatasetRows = allRows.filter((row) => row.table_figure_dataset_policy_required).length;
  const blankPolicyReviewCells = allRows.length * policyReviewFields.length;

  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'openintro_numeracy_source_coordinate_policy_sheet_no_policy_returns_no_scans_no_source_text_no_excerpts_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Classify package 159 OpenIntro IMS statistics/public-numeracy metadata summaries into source-coordinate policy rows, distinguishing future coordinate candidates from support-only, license/share-alike, PDF-hold, packet-scope, and world-family lane-fit rows without authorizing scans, copying source text, selecting excerpts, or starting translation.',
    parent_artifacts: [
      parentInventoryFile,
      parentRouterFile,
      parentShelfFile,
      'OPENINTRO_NUMERACY_PUBLIC_SERVICE_SOURCE_MINI_SHELF_20260629T194849Z',
      'OPENINTRO_NUMERACY_EXACT_EDITION_CAPTURE_20260629T200225Z',
      'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z'
    ],
    boundary: {
      artifact_is: [
        'metadata-derived OpenIntro numeracy coordinate policy sheet',
        'future scan-candidate classifier',
        'support-only, license, attribution, share-alike, and file-policy classifier',
        'blank policy-review allocator'
      ],
      artifact_is_not: [
        'policy return',
        'coordinate scan authorization',
        'source text capture authorization',
        'source excerpt selection',
        'license or share-alike clearance decision',
        'OpenIntro prose copy',
        'table, figure, dataset, definition, or example extraction',
        'translation draft',
        'constructed-language form proposal',
        'pilot or publication readiness claim'
      ],
      promotion_requires: [
        'dated policy review return',
        'license, attribution, change-note, and share-alike decision',
        'file-level table, figure, dataset, and image policy where needed',
        'separate coordinate scan artifact',
        'separate selected-excerpt sidecar before any translation or adaptation',
        'local-language source alignment or reviewer return before any bridge-language surface'
      ]
    },
    inherited_parent_counts: {
      openintro_metadata_rows_total: parent.gate_state.openintro_metadata_rows_total,
      openintro_cache_inventory_rows: parent.gate_state.openintro_cache_inventory_rows,
      exact_edition_route_rows: parent.gate_state.exact_edition_route_rows,
      numeracy_packet_slot_rows: parent.gate_state.numeracy_packet_slot_rows,
      numeracy_lane_fit_rows: parent.gate_state.numeracy_lane_fit_rows
    },
    route_class_policy_rows: routeClassPolicyRows,
    exact_route_use_policy_rows: exactRouteUsePolicyRows,
    extension_policy_rows: extensionPolicyRows,
    packet_slot_policy_rows: packetSlotPolicyRows,
    lane_fit_policy_rows: laneFitPolicyRows,
    policy_class_summary_rows: policyClassSummaryRows,
    next_policy_artifact_rows: nextPolicyArtifactRows,
    gate_state: {
      openintro_numeracy_source_coordinate_policy_rows: allRows.length,
      route_class_policy_rows: routeClassPolicyRows.length,
      exact_route_use_policy_rows: exactRouteUsePolicyRows.length,
      extension_policy_rows: extensionPolicyRows.length,
      packet_slot_policy_rows: packetSlotPolicyRows.length,
      lane_fit_policy_rows: laneFitPolicyRows.length,
      policy_class_summary_rows: policyClassSummaryRows.length,
      next_policy_artifact_rows: nextPolicyArtifactRows.length,
      coordinate_scan_candidate_after_review_rows: candidateAfterReviewRows,
      license_or_permission_gate_required_rows: licenseGateRows,
      attribution_sidecar_required_rows: attributionRows,
      table_figure_dataset_policy_required_rows: tableFigureDatasetRows,
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
      source_tables_copied: 0,
      source_figures_copied: 0,
      source_datasets_copied: 0,
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
      translation_ready: false,
      publication_ready: false,
      constructed_surface_ready: false,
      pilot_ready: false
    },
    validation_snapshot: {
      expected_route_class_policy_rows: parent.route_class_summary_rows.length,
      expected_exact_route_use_policy_rows: parent.exact_route_use_summary_rows.length,
      expected_extension_policy_rows: parent.extension_summary_rows.length,
      expected_packet_slot_policy_rows: parent.numeracy_packet_slot_rows.length,
      expected_lane_fit_policy_rows: parent.numeracy_lane_fit_rows.length,
      expected_policy_rows_total: allRows.length,
      expected_min_coordinate_scan_candidate_after_review_rows: 4,
      expected_blank_policy_review_fields_per_row: policyReviewFields.length,
      expected_blank_policy_review_cells_allocated: blankPolicyReviewCells,
      zero_gate_assertions: zeroGateKeys
    },
    decision: {
      current_action_allowed: 'metadata_policy_classification_and_blank_review_allocation_only',
      current_action_not_allowed: [
        'policy return',
        'coordinate scan',
        'source text or excerpt capture',
        'table, figure, dataset, definition, or example extraction',
        'translation',
        'constructed surface proposal',
        'readiness claim'
      ]
    }
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const classRows = artifact.policy_class_summary_rows.map((row) => `| ${row.policy_class_summary_row_id} | ${row.policy_class} | ${row.policy_rows} | ${row.coordinate_scan_candidate_after_review_rows} | ${row.license_or_permission_gate_required_rows} | ${row.table_figure_dataset_policy_required_rows} |`).join('\n');
  const routeRows = artifact.route_class_policy_rows.map((row) => `| ${row.policy_row_id} | ${row.source_group} | ${row.policy_class} | ${row.metadata_rows} | ${row.coordinate_scan_candidate_after_review} |`).join('\n');
  const exactRows = artifact.exact_route_use_policy_rows.map((row) => `| ${row.policy_row_id} | ${row.source_group} | ${row.policy_class} | ${row.coordinate_scan_candidate_after_review} |`).join('\n');
  const packetRows = artifact.packet_slot_policy_rows.map((row) => `| ${row.policy_row_id} | ${row.source_group} | ${row.policy_class} | ${row.license_or_permission_gate_required} | ${row.table_figure_dataset_policy_required} |`).join('\n');
  const laneRows = artifact.lane_fit_policy_rows.map((row) => `| ${row.policy_row_id} | ${row.source_group} | ${row.policy_class} | ${row.translation_allowed_now} | ${row.constructed_surface_allowed_now} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Counts

- OpenIntro numeracy source-coordinate policy rows: \`${g.openintro_numeracy_source_coordinate_policy_rows}\`
- Route-class policy rows: \`${g.route_class_policy_rows}\`
- Exact-route-use policy rows: \`${g.exact_route_use_policy_rows}\`
- Extension policy rows: \`${g.extension_policy_rows}\`
- Packet-slot policy rows: \`${g.packet_slot_policy_rows}\`
- Lane-fit policy rows: \`${g.lane_fit_policy_rows}\`
- Candidate-after-review rows: \`${g.coordinate_scan_candidate_after_review_rows}\`
- License/permission gate rows: \`${g.license_or_permission_gate_required_rows}\`
- Attribution sidecar rows: \`${g.attribution_sidecar_required_rows}\`
- Table/figure/dataset policy rows: \`${g.table_figure_dataset_policy_required_rows}\`
- Blank policy-review cells: \`${g.blank_policy_review_cells_allocated}\`

## Policy Classes

| Row | Policy class | Rows | Candidate-after-review rows | License-gated rows | File-policy rows |
| --- | --- | ---: | ---: | ---: | ---: |
${classRows}

## Route-Class Rows

| Row | Source group | Policy class | Metadata rows | Candidate after review |
| --- | --- | --- | ---: | --- |
${routeRows}

## Exact-Route-Use Rows

| Row | Source group | Policy class | Candidate after review |
| --- | --- | --- | --- |
${exactRows}

## Packet Rows

| Row | Packet slot | Policy class | License gate | File policy |
| --- | --- | --- | --- | --- |
${packetRows}

## Lane Rows

| Row | Lane group | Policy class | Translation now | Constructed surface now |
| --- | --- | --- | --- | --- |
${laneRows}

## Zero Gates

\`0\` policy reviews completed, \`0\` coordinate scans authorized, \`0\` source-text/excerpt files, \`0\` source text copied, \`0\` tables/figures/datasets copied, \`0\` translations, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` readiness claims.

Boundary: metadata-only policy classification. This artifact is not a policy return, excerpt selection, source text capture, translation, constructed-language proposal, license clearance, share-alike clearance, publication claim, or pilot claim.
`;
}

function buildArtifactCsv(artifact) {
  const rows = [
    ['section', 'policy_row_id', 'source_group', 'policy_class', 'metadata_rows', 'metadata_bytes', 'candidate_after_review', 'license_gate', 'attribution_gate', 'file_policy_gate', 'source_text_capture_allowed_now', 'policy_review_completed'].map(csvCell).join(',')
  ];
  for (const section of ['route_class_policy_rows', 'exact_route_use_policy_rows', 'extension_policy_rows', 'packet_slot_policy_rows', 'lane_fit_policy_rows']) {
    for (const row of artifact[section]) {
      rows.push([
        section,
        row.policy_row_id,
        row.source_group,
        row.policy_class,
        row.metadata_rows,
        row.metadata_bytes,
        row.coordinate_scan_candidate_after_review,
        row.license_or_permission_gate_required,
        row.attribution_sidecar_required,
        row.table_figure_dataset_policy_required,
        row.source_text_capture_allowed_now,
        row.policy_review_completed
      ].map(csvCell).join(','));
    }
  }
  return `${rows.join('\n')}\n`;
}

function buildNote(artifact) {
  const g = artifact.gate_state;
  return {
    artifact_id: noteId,
    generated_utc: noteGeneratedUtc,
    source_artifact_id: artifact.artifact_id,
    status: 'pointer_only_package160_openintro_numeracy_source_coordinate_policy_sheet_note_no_remote_action_no_source_text_no_translation_no_readiness',
    summary: 'Package 160 records a metadata-only OpenIntro IMS numeracy source-coordinate policy sheet and blank policy-review rows.',
    counts: {
      openintro_numeracy_source_coordinate_policy_rows: g.openintro_numeracy_source_coordinate_policy_rows,
      route_class_policy_rows: g.route_class_policy_rows,
      exact_route_use_policy_rows: g.exact_route_use_policy_rows,
      extension_policy_rows: g.extension_policy_rows,
      packet_slot_policy_rows: g.packet_slot_policy_rows,
      lane_fit_policy_rows: g.lane_fit_policy_rows,
      blank_policy_review_cells_allocated: g.blank_policy_review_cells_allocated
    },
    zero_gates: {
      policy_reviews_completed: 0,
      coordinate_scans_authorized: 0,
      excerpt_selections_authorized: 0,
      source_text_or_excerpt_files_created: 0,
      source_text_copied: 0,
      source_tables_copied: 0,
      source_figures_copied: 0,
      source_datasets_copied: 0,
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
  return `# Package 160 OpenIntro Numeracy Source-Coordinate Policy Sheet Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only local note: package 160 records \`${g.openintro_numeracy_source_coordinate_policy_rows}\` metadata-derived policy rows and \`${g.blank_policy_review_cells_allocated}\` blank policy-review cells for OpenIntro IMS statistics/public numeracy.

Zero gates: \`0\` policy reviews completed, \`0\` coordinate scans authorized, \`0\` excerpt selections authorized, \`0\` source-text/excerpt files, \`0\` source text copied, \`0\` tables/figures/datasets copied, \`0\` translations, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` reviewer returns ingested, \`0\` readiness claims.

Boundary: metadata-only policy sheet. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, source-text, excerpt, proposed form, accepted surface, translation, publication, pilot, legal-advice, or remote-state claim.
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
    role: 'open_translation_openintro_numeracy_source_coordinate_policy_sheet',
    artifact: artifactId,
    current_use: `${g.openintro_numeracy_source_coordinate_policy_rows} OpenIntro numeracy source-coordinate policy rows; ${g.coordinate_scan_candidate_after_review_rows} candidate-after-review rows; ${g.blank_policy_review_cells_allocated} blank policy-review cells; 0 source text, 0 excerpts, 0 tables/figures/datasets copied, 0 translations, 0 forms, 0 readiness`
  };
  const existingPackageRowIndex = order.findIndex((row) => row?.artifact === artifactId);
  if (existingPackageRowIndex >= 0) order[existingPackageRowIndex] = { ...order[existingPackageRowIndex], ...packageRow };
  else order.push(packageRow);
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_open_translation_openintro_numeracy_source_coordinate_policy_sheet = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_openintro_numeracy_source_coordinate_policy_rows: g.openintro_numeracy_source_coordinate_policy_rows,
    current_openintro_numeracy_policy_candidate_after_review_rows: g.coordinate_scan_candidate_after_review_rows,
    current_openintro_numeracy_policy_review_cells: g.blank_policy_review_cells_allocated,
    current_openintro_numeracy_source_text_or_excerpt_files: 0,
    current_openintro_numeracy_translated_passages: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_openintro_numeracy_policy_review_return_or_attribution_share_alike_decision_template_only_no_source_text_no_excerpts_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'Open translation OpenIntro numeracy source-coordinate policy sheet',
    route: artifactId,
    license_status_to_recheck: 'policy_sheet_only_recheck_OpenIntro_IMS_CC_BY_SA_attribution_change_share_alike_and_table_figure_dataset_file_rules_before_any_coordinate_scan_excerpt_adaptation_or_translation',
    best_translation_use: 'statistics/public numeracy source-coordinate policy gate before later selected-excerpt sidecars, attribution/change notices, or local-language reviewer decisions',
    candidate_lanes: [
      'statistics_public_numeracy',
      'OpenIntro_IMS',
      'data_literacy',
      'public_service_numeracy',
      'source_coordinate_policy',
      'share_alike_attribution_review'
    ],
    priority: 1,
    status: 'source_coordinate_policy_sheet_no_policy_returns_no_scans_no_source_text_no_excerpts_no_tables_figures_datasets_no_translation_no_forms_no_pilot',
    gate_state: {
      openintro_numeracy_source_coordinate_policy_rows: g.openintro_numeracy_source_coordinate_policy_rows,
      coordinate_scan_candidate_after_review_rows: g.coordinate_scan_candidate_after_review_rows,
      license_or_permission_gate_required_rows: g.license_or_permission_gate_required_rows,
      blank_policy_review_cells_allocated: g.blank_policy_review_cells_allocated,
      source_text_or_excerpt_files_created: 0,
      source_text_copied: 0,
      source_tables_copied: 0,
      source_figures_copied: 0,
      source_datasets_copied: 0,
      translated_passages: 0,
      proposed_bridge_lexemes: 0,
      accepted_bridge_surfaces: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_open_translation_openintro_numeracy_source_coordinate_policy_sheet: ${artifactId}_${g.openintro_numeracy_source_coordinate_policy_rows}_policy_rows_0_source_text_0_excerpts_0_translation_upload_when_path_exists_no_mobile_plan_deferral`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_open_translation_openintro_numeracy_source_coordinate_policy_sheet_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_open_translation_openintro_numeracy_source_coordinate_policy_sheet_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_openintro_numeracy_source_coordinate_policy_rows: g.openintro_numeracy_source_coordinate_policy_rows,
    current_openintro_numeracy_source_coordinate_candidate_after_review_rows: g.coordinate_scan_candidate_after_review_rows,
    current_openintro_numeracy_source_text_or_excerpt_files: 0,
    current_openintro_numeracy_translated_passages: 0,
    current_openintro_numeracy_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_open_translation_openintro_numeracy_source_coordinate_policy_sheet = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_open_translation_openintro_numeracy_source_coordinate_policy_sheet: ${artifactId}_policy_sheet_before_any_policy_returns_coordinate_scan_results_excerpts_translations_surfaces_or_pilot_claims`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_open_translation_openintro_numeracy_source_coordinate_policy_sheet = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: records ${g.openintro_numeracy_source_coordinate_policy_rows} OpenIntro IMS numeracy source-coordinate policy rows and ${g.blank_policy_review_cells_allocated} blank policy-review cells; substantive upload-bound artifact; 0 source text, 0 excerpts, 0 tables/figures/datasets copied, 0 translations, 0 proposed forms, 0 accepted surfaces, 0 readiness.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OpenIntro numeracy source-coordinate policy sheet; ${g.openintro_numeracy_source_coordinate_policy_rows} policy rows, ${g.blank_policy_review_cells_allocated} blank policy-review cells, 0 source text, 0 excerpts, 0 tables/figures/datasets, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 160: OpenIntro numeracy source-coordinate policy sheet. It records ${g.openintro_numeracy_source_coordinate_policy_rows} metadata-derived policy rows and ${g.blank_policy_review_cells_allocated} blank policy-review cells while keeping 0 source text, 0 excerpts, 0 tables/figures/datasets copied, 0 translations, 0 proposed forms, 0 accepted surfaces, and all readiness gates closed. It is upload-bound as substantive catalog/control work when a valid staging path exists.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | Open translation OpenIntro numeracy source-coordinate policy sheet | ${artifactId} | Metadata-only policy sheet; ${g.openintro_numeracy_source_coordinate_policy_rows} rows, 0 source text, 0 excerpts, 0 translation, upload when path exists. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_open_translation_openintro_numeracy_source_coordinate_policy_sheet_artifact: \`${artifactId}\` (${g.openintro_numeracy_source_coordinate_policy_rows} policy rows; 0 source text; 0 excerpts; 0 accepted surfaces or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_open_translation_openintro_numeracy_source_coordinate_policy_sheet: \`${artifactId}\`; metadata-only OpenIntro IMS numeracy policy sheet, no source text, excerpts, accepted terms, surfaces, translation, or pilot.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OpenIntro IMS public numeracy source-coordinate policy sheet; substantive and upload-bound, but not a source excerpt, table, figure, dataset, translation, constructed form, license clearance, or readiness claim.`);
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
    { filename: `${artifactId}.json`, class: 'open_translation_openintro_numeracy_source_coordinate_policy_sheet' },
    { filename: `${artifactId}.md`, class: 'open_translation_openintro_numeracy_source_coordinate_policy_sheet' },
    { filename: `${artifactId}.csv`, class: 'open_translation_openintro_numeracy_source_coordinate_policy_sheet' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'open_translation_package160_coordination_note' },
    { filename: `${noteId}.md`, class: 'open_translation_package160_coordination_note' },
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
  upload.obj.package160_upload_queue_update = {
    captured_utc: '2026-07-03T10:17:00Z',
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
  const step = 'Stage package 160 OpenIntro numeracy source-coordinate policy sheet artifacts as substantive beyond-core translation/source-route catalog material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (g.route_class_policy_rows !== artifact.validation_snapshot.expected_route_class_policy_rows) failures.push(`route_class_rows_mismatch_${g.route_class_policy_rows}`);
  if (g.exact_route_use_policy_rows !== artifact.validation_snapshot.expected_exact_route_use_policy_rows) failures.push(`exact_route_use_rows_mismatch_${g.exact_route_use_policy_rows}`);
  if (g.extension_policy_rows !== artifact.validation_snapshot.expected_extension_policy_rows) failures.push(`extension_rows_mismatch_${g.extension_policy_rows}`);
  if (g.packet_slot_policy_rows !== artifact.validation_snapshot.expected_packet_slot_policy_rows) failures.push(`packet_rows_mismatch_${g.packet_slot_policy_rows}`);
  if (g.lane_fit_policy_rows !== artifact.validation_snapshot.expected_lane_fit_policy_rows) failures.push(`lane_rows_mismatch_${g.lane_fit_policy_rows}`);
  if (g.openintro_numeracy_source_coordinate_policy_rows !== artifact.validation_snapshot.expected_policy_rows_total) failures.push(`policy_total_mismatch_${g.openintro_numeracy_source_coordinate_policy_rows}`);
  if (g.coordinate_scan_candidate_after_review_rows < artifact.validation_snapshot.expected_min_coordinate_scan_candidate_after_review_rows) failures.push(`too_few_candidate_after_review_rows_${g.coordinate_scan_candidate_after_review_rows}`);
  if (g.blank_policy_review_fields_per_row !== artifact.validation_snapshot.expected_blank_policy_review_fields_per_row) failures.push(`blank_fields_mismatch_${g.blank_policy_review_fields_per_row}`);
  if (g.blank_policy_review_cells_allocated !== artifact.validation_snapshot.expected_blank_policy_review_cells_allocated) failures.push(`blank_cells_mismatch_${g.blank_policy_review_cells_allocated}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  const rows = [
    ...artifact.route_class_policy_rows,
    ...artifact.exact_route_use_policy_rows,
    ...artifact.extension_policy_rows,
    ...artifact.packet_slot_policy_rows,
    ...artifact.lane_fit_policy_rows
  ];
  for (const row of rows) {
    const filled = policyReviewFields.some((field) => row[field] !== null);
    if (filled || row.policy_review_fields_filled !== 0 || row.policy_review_completed || row.coordinate_scan_authorized || row.source_text_capture_authorized || row.excerpt_selection_authorized || row.translation_authorized) {
      failures.push(`nonblank_or_open_policy_row_${row.policy_row_id}`);
      break;
    }
    if (row.source_text_capture_allowed_now || row.excerpt_selection_allowed_now || row.translation_allowed_now || row.constructed_surface_allowed_now) {
      failures.push(`row_allows_locked_action_${row.policy_row_id}`);
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
  openintro_numeracy_source_coordinate_policy_rows: artifact.gate_state.openintro_numeracy_source_coordinate_policy_rows,
  route_class_policy_rows: artifact.gate_state.route_class_policy_rows,
  exact_route_use_policy_rows: artifact.gate_state.exact_route_use_policy_rows,
  extension_policy_rows: artifact.gate_state.extension_policy_rows,
  packet_slot_policy_rows: artifact.gate_state.packet_slot_policy_rows,
  lane_fit_policy_rows: artifact.gate_state.lane_fit_policy_rows,
  coordinate_scan_candidate_after_review_rows: artifact.gate_state.coordinate_scan_candidate_after_review_rows,
  license_or_permission_gate_required_rows: artifact.gate_state.license_or_permission_gate_required_rows,
  attribution_sidecar_required_rows: artifact.gate_state.attribution_sidecar_required_rows,
  table_figure_dataset_policy_required_rows: artifact.gate_state.table_figure_dataset_policy_required_rows,
  blank_policy_review_cells_allocated: artifact.gate_state.blank_policy_review_cells_allocated,
  policy_reviews_completed: artifact.gate_state.policy_reviews_completed,
  coordinate_scans_authorized: artifact.gate_state.coordinate_scans_authorized,
  source_text_copied: artifact.gate_state.source_text_copied,
  source_tables_copied: artifact.gate_state.source_tables_copied,
  source_figures_copied: artifact.gate_state.source_figures_copied,
  source_datasets_copied: artifact.gate_state.source_datasets_copied,
  translated_passages: artifact.gate_state.translated_passages,
  proposed_bridge_lexemes: artifact.gate_state.proposed_bridge_lexemes,
  accepted_bridge_surfaces: artifact.gate_state.accepted_bridge_surfaces,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
