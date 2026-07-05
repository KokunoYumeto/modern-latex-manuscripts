import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OPEN_TRANSLATION_ALGEBRA_METADATA_INVENTORY_SCAN_START_20260703T091500Z';
const noteId = 'OPEN_TRANSLATION_ALGEBRA_METADATA_INVENTORY_SCAN_START_NOTE_20260703T091600Z';
const generatedUtc = '2026-07-03T09:15:00Z';
const noteGeneratedUtc = '2026-07-03T09:16:00Z';
const packageOrder = 156;
const queueCandidateId = 'OTCQ-OPEN-TRANSLATION-ALGEBRA-METADATA-INVENTORY-SCAN-START-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';
const parentRouterFile = 'OPEN_TRANSLATION_REVIEW_ONLY_SOURCE_COORDINATE_SCAN_ROUTER_20260703T081500Z';
const parentShelfFile = 'OPEN_TRANSLATION_REVIEW_ONLY_PACKET_SOURCE_SHELF_REFRESH_20260703T080000Z';

const sourceSpecs = [
  {
    source_family: 'FCLA linear algebra',
    shelf_row_id: 'OTRSS-004',
    router_row_id: 'OTCS-RTR-004',
    task_row_id: 'OTCS-TASK-005',
    packet_shape: 'linear_algebra_packet',
    manifest_path: 'outputs/source_cache/fcla_gfdl_exact_commit_20260630T070951Z/cache_manifest.json'
  },
  {
    source_family: 'AATA abstract algebra',
    shelf_row_id: 'OTRSS-005',
    router_row_id: 'OTCS-RTR-005',
    task_row_id: 'OTCS-TASK-006',
    packet_shape: 'abstract_algebra_packet',
    manifest_path: 'outputs/source_cache/aata_gfdl_exact_commit_20260630T071615Z/cache_manifest.json'
  }
];

const metadataReviewFields = [
  'inventory_review_date',
  'reviewer_route_or_role',
  'manifest_route_identity_confirmed',
  'exact_commit_or_branch_status_confirmed',
  'license_or_permission_status_confirmed',
  'source_tree_inventory_scope_accepted',
  'coordinate_scan_scope_recommended',
  'support_only_route_exclusion_note',
  'attribution_sidecar_needed',
  'next_coordinate_policy_artifact',
  'review_note_without_source_prose'
];

const zeroGateKeys = [
  'metadata_inventory_reviews_completed',
  'coordinate_scans_authorized',
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

async function readAnyJson(relativePath) {
  const text = await readFile(path.join(root, relativePath), 'utf8');
  return parseJson(text);
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

function normalizeRel(value) {
  return String(value || '').replaceAll('\\', '/');
}

function extKey(filename) {
  const ext = path.extname(filename || '').toLowerCase();
  return ext || '[none]';
}

function recordsFromManifest(obj) {
  if (Array.isArray(obj)) return obj;
  if (Array.isArray(obj?.value)) return obj.value;
  return [];
}

function routeClassUse(sourceClass) {
  if (sourceClass === 'github_api_contents') return 'source_tree_inventory_candidate';
  if (sourceClass === 'repo_license_file') return 'license_support_only';
  if (sourceClass === 'github_api_metadata' || sourceClass === 'github_api_branch_metadata') return 'repo_identity_support_only';
  if (sourceClass === 'public_book_site') return 'public_route_support_only';
  if (sourceClass === 'repo_readme' || sourceClass === 'repo_changes' || sourceClass === 'repo_project_metadata' || sourceClass === 'repo_requirements') return 'repository_support_metadata_only';
  return 'support_metadata_only';
}

async function buildManifestRouteRows() {
  const rows = [];
  for (const spec of sourceSpecs) {
    const manifest = recordsFromManifest(await readAnyJson(spec.manifest_path));
    manifest.forEach((record, index) => {
      rows.push({
        algebra_manifest_route_row_id: `ALG-MANIFEST-${String(rows.length + 1).padStart(3, '0')}`,
        source_family: spec.source_family,
        packet_shape: spec.packet_shape,
        parent_shelf_row_id: spec.shelf_row_id,
        parent_router_row_id: spec.router_row_id,
        parent_route_task_row_id: spec.task_row_id,
        manifest_record_sequence: index + 1,
        manifest_record_id: record.id || null,
        source_class: record.source_class || null,
        route_class_use: routeClassUse(record.source_class),
        url: record.url || null,
        cache_path: normalizeRel(record.cache_path),
        status: record.status || null,
        message: record.message || '',
        bytes: record.bytes || 0,
        sha256: record.sha256 || '',
        source_text_copied: 0,
        source_passage_selected: false,
        excerpt_candidate: false,
        translation_started: false
      });
    });
  }
  return rows;
}

async function buildContentsInventoryRows(manifestRows) {
  const rows = [];
  for (const route of manifestRows.filter((row) => row.source_class === 'github_api_contents' && row.status === 'cached' && row.cache_path)) {
    let items = [];
    try {
      const parsed = await readAnyJson(route.cache_path);
      items = Array.isArray(parsed) ? parsed : Array.isArray(parsed?.value) ? parsed.value : [];
    } catch {
      items = [];
    }
    items.forEach((item, index) => {
      rows.push({
        algebra_contents_inventory_row_id: `ALG-CONTENTS-${String(rows.length + 1).padStart(4, '0')}`,
        source_family: route.source_family,
        packet_shape: route.packet_shape,
        parent_manifest_route_row_id: route.algebra_manifest_route_row_id,
        parent_manifest_record_id: route.manifest_record_id,
        source_class: route.source_class,
        contents_record_sequence: index + 1,
        github_item_name: item.name || null,
        github_item_path: item.path || null,
        github_item_type: item.type || null,
        extension: extKey(item.name || item.path || ''),
        bytes: item.size || 0,
        sha_present: Boolean(item.sha),
        download_url_present: Boolean(item.download_url),
        html_url_present: Boolean(item.html_url),
        source_text_copied: 0,
        source_passage_selected: false,
        excerpt_candidate: false,
        translation_started: false
      });
    });
  }
  return rows;
}

function summarize(rows, key, idPrefix) {
  const map = new Map();
  for (const row of rows) {
    const value = row[key] || '[missing]';
    if (!map.has(value)) {
      map.set(value, {
        summary_row_id: `${idPrefix}-${String(map.size + 1).padStart(3, '0')}`,
        group_key: value,
        rows: 0,
        bytes: 0,
        source_text_copied: 0,
        translated_passages: 0
      });
    }
    const entry = map.get(value);
    entry.rows += 1;
    entry.bytes += row.bytes || 0;
  }
  return [...map.values()].sort((a, b) => b.rows - a.rows || a.group_key.localeCompare(b.group_key));
}

function buildFuturePacketRows(manifestRows, contentsRows) {
  const fclaRows = contentsRows.filter((row) => row.source_family === 'FCLA linear algebra');
  const aataRows = contentsRows.filter((row) => row.source_family === 'AATA abstract algebra');
  return [
    {
      algebra_packet_candidate_row_id: 'ALG-PACKET-CAND-01',
      packet_shape: 'linear_algebra_packet',
      source_family: 'FCLA linear algebra',
      route_basis: 'FCLA cached manifest plus GitHub contents metadata',
      manifest_route_rows: manifestRows.filter((row) => row.source_family === 'FCLA linear algebra').length,
      contents_inventory_rows: fclaRows.length,
      source_tree_candidate_rows: fclaRows.filter((row) => row.github_item_type === 'file').length,
      needed_next_artifact: 'OPEN_TRANSLATION_ALGEBRA_SOURCE_COORDINATE_POLICY_SHEET_<timestamp>',
      source_text_or_excerpt_allowed_now: false,
      translation_allowed_now: false
    },
    {
      algebra_packet_candidate_row_id: 'ALG-PACKET-CAND-02',
      packet_shape: 'abstract_algebra_packet',
      source_family: 'AATA abstract algebra',
      route_basis: 'AATA cached manifest plus GitHub contents metadata',
      manifest_route_rows: manifestRows.filter((row) => row.source_family === 'AATA abstract algebra').length,
      contents_inventory_rows: aataRows.length,
      source_tree_candidate_rows: aataRows.filter((row) => row.github_item_type === 'file').length,
      needed_next_artifact: 'OPEN_TRANSLATION_ALGEBRA_SOURCE_COORDINATE_POLICY_SHEET_<timestamp>',
      source_text_or_excerpt_allowed_now: false,
      translation_allowed_now: false
    }
  ];
}

function buildReviewRows(manifestRows, contentsRows) {
  return sourceSpecs.map((spec, index) => ({
    algebra_metadata_review_row_id: `ALG-MINV-REV-${String(index + 1).padStart(2, '0')}`,
    source_family: spec.source_family,
    packet_shape: spec.packet_shape,
    parent_shelf_row_id: spec.shelf_row_id,
    parent_router_row_id: spec.router_row_id,
    parent_route_task_row_id: spec.task_row_id,
    manifest_route_rows_recorded: manifestRows.filter((row) => row.source_family === spec.source_family).length,
    contents_inventory_rows_recorded: contentsRows.filter((row) => row.source_family === spec.source_family).length,
    manifest_bytes_recorded: manifestRows.filter((row) => row.source_family === spec.source_family).reduce((sum, row) => sum + (row.bytes || 0), 0),
    contents_bytes_recorded: contentsRows.filter((row) => row.source_family === spec.source_family).reduce((sum, row) => sum + (row.bytes || 0), 0),
    blank_metadata_review_fields: metadataReviewFields,
    inventory_review_date: null,
    reviewer_route_or_role: null,
    manifest_route_identity_confirmed: null,
    exact_commit_or_branch_status_confirmed: null,
    license_or_permission_status_confirmed: null,
    source_tree_inventory_scope_accepted: null,
    coordinate_scan_scope_recommended: null,
    support_only_route_exclusion_note: null,
    attribution_sidecar_needed: null,
    next_coordinate_policy_artifact: null,
    review_note_without_source_prose: null,
    metadata_review_fields_filled: 0,
    metadata_inventory_review_completed: false,
    coordinate_scan_authorized: false,
    excerpt_selection_authorized: false,
    translation_authorized: false,
    still_locked_reason: 'metadata_inventory_recorded_but_not_reviewed_no_coordinate_scan_scope_or_license_permission_decision'
  }));
}

function buildArtifact(parentRouter, parentShelf, manifestRows, contentsRows) {
  const sourceClassSummaryRows = summarize(manifestRows, 'source_class', 'ALG-SRC-CLASS');
  const routeUseSummaryRows = summarize(manifestRows, 'route_class_use', 'ALG-ROUTE-USE');
  const contentsTypeSummaryRows = summarize(contentsRows, 'github_item_type', 'ALG-CONTENT-TYPE');
  const contentsExtensionSummaryRows = summarize(contentsRows, 'extension', 'ALG-CONTENT-EXT');
  const sourceFamilySummaryRows = summarize([...manifestRows, ...contentsRows], 'source_family', 'ALG-SOURCE');
  const packetRows = buildFuturePacketRows(manifestRows, contentsRows);
  const reviewRows = buildReviewRows(manifestRows, contentsRows);
  const blankReviewCells = reviewRows.length * metadataReviewFields.length;
  const manifestBytes = manifestRows.reduce((sum, row) => sum + (row.bytes || 0), 0);
  const contentsBytes = contentsRows.reduce((sum, row) => sum + (row.bytes || 0), 0);

  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'algebra_metadata_inventory_scan_start_no_source_text_no_excerpts_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Start the algebra coordinate path with a metadata-only inventory of FCLA linear algebra and AATA abstract algebra cached route manifests plus GitHub contents metadata, preserving route/path/type/size/hash metadata while copying no source text, selecting no excerpts, and starting no translation or constructed surface work.',
    parent_artifacts: [
      parentRouterFile,
      parentShelfFile,
      'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z',
      'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z'
    ],
    parent_router_rows_used: parentRouter.coordinate_router_rows
      .filter((row) => row.source_family.includes('FCLA') || row.source_family.includes('AATA'))
      .map((row) => row.coordinate_router_row_id),
    parent_route_task_rows_used: parentRouter.coordinate_route_task_rows
      .filter((row) => row.source_family.includes('FCLA') || row.source_family.includes('AATA'))
      .map((row) => row.coordinate_route_task_row_id),
    parent_shelf_rows_used: parentShelf.source_shelf_rows
      .filter((row) => row.source_family.includes('FCLA') || row.source_family.includes('AATA'))
      .map((row) => row.source_shelf_row_id),
    boundary: {
      artifact_is: [
        'metadata-only algebra inventory scan start',
        'manifest route and GitHub contents metadata catalog',
        'blank metadata-review allocator for FCLA and AATA'
      ],
      artifact_is_not: [
        'source excerpt',
        'source text copy',
        'definition or example extraction',
        'line-span selection',
        'license or permission clearance decision',
        'translation draft',
        'constructed-language form proposal',
        'pilot or publication readiness claim'
      ],
      promotion_requires: [
        'metadata inventory review return',
        'license or permission route decision',
        'attribution sidecar decision',
        'separate coordinate policy sheet',
        'separate selected-excerpt sidecar before any translation or adaptation'
      ]
    },
    algebra_manifest_route_rows: manifestRows,
    algebra_contents_inventory_rows: contentsRows,
    source_family_summary_rows: sourceFamilySummaryRows,
    source_class_summary_rows: sourceClassSummaryRows,
    route_use_summary_rows: routeUseSummaryRows,
    contents_type_summary_rows: contentsTypeSummaryRows,
    contents_extension_summary_rows: contentsExtensionSummaryRows,
    algebra_packet_candidate_rows: packetRows,
    algebra_metadata_review_rows: reviewRows,
    gate_state: {
      algebra_source_families_inventoried: sourceSpecs.length,
      algebra_manifest_route_rows: manifestRows.length,
      algebra_contents_inventory_rows: contentsRows.length,
      algebra_metadata_rows_total: manifestRows.length + contentsRows.length,
      algebra_manifest_bytes_total: manifestBytes,
      algebra_contents_bytes_total: contentsBytes,
      algebra_metadata_bytes_total: manifestBytes + contentsBytes,
      source_family_summary_rows: sourceFamilySummaryRows.length,
      source_class_summary_rows: sourceClassSummaryRows.length,
      route_use_summary_rows: routeUseSummaryRows.length,
      contents_type_summary_rows: contentsTypeSummaryRows.length,
      contents_extension_summary_rows: contentsExtensionSummaryRows.length,
      algebra_packet_candidate_rows: packetRows.length,
      algebra_metadata_review_rows: reviewRows.length,
      blank_metadata_review_fields_per_row: metadataReviewFields.length,
      blank_metadata_review_cells_allocated: blankReviewCells,
      metadata_inventory_reviews_completed: 0,
      coordinate_scans_authorized: 0,
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
      expected_algebra_source_families_inventoried: 2,
      expected_min_manifest_route_rows: 2,
      expected_min_contents_inventory_rows: 1,
      expected_algebra_metadata_review_rows: 2,
      expected_blank_metadata_review_fields_per_row: metadataReviewFields.length,
      expected_blank_metadata_review_cells_allocated: blankReviewCells,
      zero_gate_assertions: zeroGateKeys,
      readiness_claims: 0
    },
    next_valid_artifacts: [
      'OPEN_TRANSLATION_ALGEBRA_SOURCE_COORDINATE_POLICY_SHEET_<timestamp>',
      'OPEN_TRANSLATION_ALGEBRA_METADATA_INVENTORY_REVIEW_RETURN_LEDGER_TEMPLATE_<timestamp>',
      'OPEN_TRANSLATION_LINEAR_ALGEBRA_FCLA_PERMISSION_ATTRIBUTION_DECISION_LEDGER_TEMPLATE_<timestamp>',
      'OPEN_TRANSLATION_ABSTRACT_ALGEBRA_AATA_PERMISSION_ATTRIBUTION_DECISION_LEDGER_TEMPLATE_<timestamp>',
      'OPEN_TRANSLATION_ALGEBRA_SELECTED_EXCERPT_SIDECAR_<timestamp>_only_after_review_and_permission_decisions'
    ],
    decision: 'Package 156 records metadata-only algebra inventory for FCLA and AATA. It increases source-route knowledge while keeping source-text, excerpt, translation, constructed-surface, license-clearance, pilot, and publication gates closed.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const sourceRows = artifact.source_family_summary_rows.map((row) => `| ${row.summary_row_id} | ${row.group_key} | ${row.rows} | ${formatNumber(row.bytes)} |`).join('\n');
  const classRows = artifact.source_class_summary_rows.map((row) => `| ${row.summary_row_id} | ${row.group_key} | ${row.rows} | ${formatNumber(row.bytes)} |`).join('\n');
  const typeRows = artifact.contents_type_summary_rows.map((row) => `| ${row.summary_row_id} | ${row.group_key} | ${row.rows} | ${formatNumber(row.bytes)} |`).join('\n');
  const packetRows = artifact.algebra_packet_candidate_rows.map((row) => `| ${row.algebra_packet_candidate_row_id} | ${row.packet_shape} | ${row.source_family} | ${row.contents_inventory_rows} | ${row.source_tree_candidate_rows} |`).join('\n');
  const reviewRows = artifact.algebra_metadata_review_rows.map((row) => `| ${row.algebra_metadata_review_row_id} | ${row.source_family} | ${row.manifest_route_rows_recorded} | ${row.contents_inventory_rows_recorded} | ${row.metadata_review_fields_filled} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Counts

- Algebra source families inventoried: \`${g.algebra_source_families_inventoried}\`
- Manifest route rows: \`${g.algebra_manifest_route_rows}\`
- GitHub contents inventory rows: \`${g.algebra_contents_inventory_rows}\`
- Metadata rows total: \`${g.algebra_metadata_rows_total}\`
- Metadata bytes total: \`${formatNumber(g.algebra_metadata_bytes_total)}\`
- Packet candidate rows: \`${g.algebra_packet_candidate_rows}\`
- Metadata review rows: \`${g.algebra_metadata_review_rows}\`
- Blank metadata-review cells: \`${g.blank_metadata_review_cells_allocated}\`

## Source Family Summary

| Row | Source family | Rows | Bytes |
| --- | --- | ---: | ---: |
${sourceRows}

## Source Class Summary

| Row | Source class | Rows | Bytes |
| --- | --- | ---: | ---: |
${classRows}

## Contents Type Summary

| Row | Contents type | Rows | Bytes |
| --- | --- | ---: | ---: |
${typeRows}

## Packet Candidates

| Row | Packet shape | Source family | Contents rows | Source-tree candidate rows |
| --- | --- | --- | ---: | ---: |
${packetRows}

## Metadata Review Rows

| Row | Source family | Manifest rows | Contents rows | Filled review fields |
| --- | --- | ---: | ---: | ---: |
${reviewRows}

## Zero Gates

- Metadata inventory reviews completed: \`0\`
- Coordinate scans / excerpt selections authorized: \`0 / 0\`
- Source text/excerpt files: \`0\`
- Source text/definitions/examples copied: \`0 / 0 / 0\`
- Source passages selected: \`0\`
- Exact spans / candidate line ranges: \`0 / 0\`
- Translated passages: \`0\`
- Proposed bridge lexemes / morphemes / syntax / displays: \`0 / 0 / 0 / 0\`
- Accepted bridge surfaces / local-language terms: \`0 / 0\`
- Reviewer returns / license rechecks completed: \`0 / 0\`
- Readiness: \`publication=false, translation=false, constructed_surface=false, pilot=false\`

Boundary: this is metadata-only inventory. It records route/path/type/size/hash metadata but no source prose, no definitions, no examples, no excerpts, no line-span selections, no translations, no constructed forms, and no readiness claim.
`;
}

function buildArtifactCsv(artifact) {
  const rows = [];
  rows.push(['section', 'row_id', 'source_family', 'class_or_type', 'path_or_record', 'status', 'bytes', 'source_text_copied', 'excerpt_candidate'].map(csvCell).join(','));
  for (const row of artifact.algebra_manifest_route_rows) {
    rows.push([
      'algebra_manifest_route_row',
      row.algebra_manifest_route_row_id,
      row.source_family,
      row.source_class,
      row.manifest_record_id,
      row.status,
      row.bytes,
      row.source_text_copied,
      row.excerpt_candidate
    ].map(csvCell).join(','));
  }
  for (const row of artifact.algebra_contents_inventory_rows) {
    rows.push([
      'algebra_contents_inventory_row',
      row.algebra_contents_inventory_row_id,
      row.source_family,
      row.github_item_type,
      row.github_item_path,
      row.extension,
      row.bytes,
      row.source_text_copied,
      row.excerpt_candidate
    ].map(csvCell).join(','));
  }
  for (const row of artifact.algebra_metadata_review_rows) {
    rows.push([
      'algebra_metadata_review_row',
      row.algebra_metadata_review_row_id,
      row.source_family,
      row.packet_shape,
      row.parent_route_task_row_id,
      row.still_locked_reason,
      row.manifest_bytes_recorded + row.contents_bytes_recorded,
      0,
      false
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
    status: 'pointer_only_package156_algebra_metadata_inventory_note_no_remote_action_no_source_text_no_translation_no_readiness',
    summary: 'Package 156 records metadata-only algebra inventory rows for FCLA and AATA route and contents metadata.',
    counts: {
      algebra_manifest_route_rows: g.algebra_manifest_route_rows,
      algebra_contents_inventory_rows: g.algebra_contents_inventory_rows,
      algebra_metadata_rows_total: g.algebra_metadata_rows_total,
      algebra_packet_candidate_rows: g.algebra_packet_candidate_rows,
      algebra_metadata_review_rows: g.algebra_metadata_review_rows,
      blank_metadata_review_cells_allocated: g.blank_metadata_review_cells_allocated
    },
    zero_gates: {
      metadata_inventory_reviews_completed: 0,
      coordinate_scans_authorized: 0,
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
  return `# Package 156 Algebra Metadata Inventory Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only local note: package 156 records \`${g.algebra_manifest_route_rows}\` manifest route rows, \`${g.algebra_contents_inventory_rows}\` GitHub contents metadata rows, and \`${g.algebra_metadata_review_rows}\` blank metadata-review rows for FCLA and AATA.

Zero gates: \`0\` metadata inventory reviews completed, \`0\` coordinate scans authorized, \`0\` excerpt selections authorized, \`0\` source-text/excerpt files, \`0\` source text copied, \`0\` source passages selected, \`0\` translations, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` reviewer returns ingested, \`0\` readiness claims.

Boundary: metadata-only algebra inventory start. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, source-text, excerpt, proposed form, accepted surface, translation, publication, pilot, legal-advice, or remote-state claim.
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
    role: 'open_translation_algebra_metadata_inventory_scan_start',
    artifact: artifactId,
    current_use: `${g.algebra_metadata_rows_total} algebra metadata rows; ${g.algebra_packet_candidate_rows} packet candidate rows; ${g.algebra_metadata_review_rows} blank metadata-review rows; 0 source text, 0 excerpts, 0 translations, 0 forms, 0 readiness`
  };
  const existingPackageRowIndex = order.findIndex((row) => row?.artifact === artifactId);
  if (existingPackageRowIndex >= 0) order[existingPackageRowIndex] = { ...order[existingPackageRowIndex], ...packageRow };
  else order.push(packageRow);
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_open_translation_algebra_metadata_inventory_scan_start = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_algebra_metadata_inventory_rows: g.algebra_metadata_rows_total,
    current_algebra_metadata_review_rows: g.algebra_metadata_review_rows,
    current_algebra_source_text_or_excerpt_files: 0,
    current_algebra_translated_passages: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_algebra_source_coordinate_policy_sheet_or_metadata_review_return_template_only_no_source_text_no_excerpts_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'Open translation algebra metadata inventory scan start',
    route: artifactId,
    license_status_to_recheck: 'metadata_inventory_only_recheck_FCLA_and_AATA_license_permission_routes_before_any_coordinate_scan_excerpt_adaptation_or_translation',
    best_translation_use: 'linear and abstract algebra file/route metadata inventory before later coordinate policy, permission, or attribution decisions',
    candidate_lanes: [
      'linear_algebra',
      'abstract_algebra',
      'FCLA',
      'AATA',
      'source_coordinate_policy',
      'beyond_core_translation_candidate'
    ],
    priority: 1,
    status: 'metadata_inventory_scan_start_no_source_text_no_excerpts_no_translation_no_forms_no_pilot',
    gate_state: {
      algebra_metadata_rows_total: g.algebra_metadata_rows_total,
      algebra_packet_candidate_rows: g.algebra_packet_candidate_rows,
      algebra_metadata_review_rows: g.algebra_metadata_review_rows,
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
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_open_translation_algebra_metadata_inventory_scan_start: ${artifactId}_${g.algebra_metadata_rows_total}_metadata_rows_0_source_text_0_excerpts_0_translation_upload_when_path_exists_no_mobile_plan_deferral`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_open_translation_algebra_metadata_inventory_scan_start_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_open_translation_algebra_metadata_inventory_scan_start_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_algebra_metadata_inventory_rows: g.algebra_metadata_rows_total,
    current_algebra_metadata_review_rows: g.algebra_metadata_review_rows,
    current_algebra_source_text_or_excerpt_files: 0,
    current_algebra_translated_passages: 0,
    current_algebra_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_open_translation_algebra_metadata_inventory_scan_start = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_open_translation_algebra_metadata_inventory_scan_start: ${artifactId}_metadata_inventory_before_any_coordinate_scan_results_excerpts_translations_surfaces_or_pilot_claims`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_open_translation_algebra_metadata_inventory_scan_start = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: records ${g.algebra_metadata_rows_total} algebra metadata inventory rows for FCLA and AATA plus ${g.algebra_metadata_review_rows} blank metadata-review rows; substantive upload-bound artifact; 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, 0 readiness.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - Algebra metadata inventory scan start; ${g.algebra_metadata_rows_total} metadata rows for FCLA and AATA, ${g.algebra_metadata_review_rows} blank metadata-review rows, 0 source text, 0 excerpts, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 156: algebra metadata inventory scan start for FCLA and AATA. It records ${g.algebra_metadata_rows_total} metadata-only inventory rows and ${g.algebra_metadata_review_rows} blank metadata-review rows while keeping 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, and all readiness gates closed. It is upload-bound as substantive catalog/control work when a valid staging path exists.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | Open translation algebra metadata inventory scan start | ${artifactId} | Metadata-only FCLA and AATA inventory; ${g.algebra_metadata_rows_total} rows, 0 source text, 0 excerpts, 0 translation, upload when path exists. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_open_translation_algebra_metadata_inventory_scan_start_artifact: \`${artifactId}\` (${g.algebra_metadata_rows_total} metadata inventory rows; 0 source text; 0 excerpts; 0 accepted surfaces or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_open_translation_algebra_metadata_inventory_scan_start: \`${artifactId}\`; metadata-only algebra inventory for FCLA plus AATA, no source text, excerpts, accepted terms, surfaces, translation, or pilot.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: algebra metadata inventory start over FCLA and AATA routes; substantive and upload-bound, but not a source excerpt, translation, constructed form, license clearance, or readiness claim.`);
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
    { filename: `${artifactId}.json`, class: 'open_translation_algebra_metadata_inventory_scan_start' },
    { filename: `${artifactId}.md`, class: 'open_translation_algebra_metadata_inventory_scan_start' },
    { filename: `${artifactId}.csv`, class: 'open_translation_algebra_metadata_inventory_scan_start' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'open_translation_package156_coordination_note' },
    { filename: `${noteId}.md`, class: 'open_translation_package156_coordination_note' },
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
  upload.obj.package156_upload_queue_update = {
    captured_utc: '2026-07-03T09:17:00Z',
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
  const step = 'Stage package 156 algebra metadata inventory scan start artifacts as substantive beyond-core translation/source-route catalog material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (g.algebra_source_families_inventoried !== artifact.validation_snapshot.expected_algebra_source_families_inventoried) failures.push(`source_family_count_mismatch_${g.algebra_source_families_inventoried}`);
  if (g.algebra_manifest_route_rows < artifact.validation_snapshot.expected_min_manifest_route_rows) failures.push(`too_few_manifest_rows_${g.algebra_manifest_route_rows}`);
  if (g.algebra_contents_inventory_rows < artifact.validation_snapshot.expected_min_contents_inventory_rows) failures.push(`too_few_contents_rows_${g.algebra_contents_inventory_rows}`);
  if (g.algebra_metadata_review_rows !== artifact.validation_snapshot.expected_algebra_metadata_review_rows) failures.push(`review_rows_mismatch_${g.algebra_metadata_review_rows}`);
  if (g.blank_metadata_review_fields_per_row !== artifact.validation_snapshot.expected_blank_metadata_review_fields_per_row) failures.push(`blank_review_fields_mismatch_${g.blank_metadata_review_fields_per_row}`);
  if (g.blank_metadata_review_cells_allocated !== artifact.validation_snapshot.expected_blank_metadata_review_cells_allocated) failures.push(`blank_review_cells_mismatch_${g.blank_metadata_review_cells_allocated}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.algebra_metadata_review_rows) {
    const filled = metadataReviewFields.some((field) => row[field] !== null);
    if (filled || row.metadata_review_fields_filled !== 0 || row.metadata_inventory_review_completed || row.coordinate_scan_authorized || row.excerpt_selection_authorized || row.translation_authorized) {
      failures.push(`nonblank_or_open_metadata_review_row_${row.algebra_metadata_review_row_id}`);
      break;
    }
  }
  if ([...artifact.algebra_manifest_route_rows, ...artifact.algebra_contents_inventory_rows].some((row) => row.source_text_copied !== 0 || row.source_passage_selected || row.excerpt_candidate || row.translation_started)) {
    failures.push('inventory_row_opened_source_or_translation_gate');
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const parentRouter = (await readJson(parentRouterFile)).obj;
const parentShelf = (await readJson(parentShelfFile)).obj;
const manifestRows = await buildManifestRouteRows();
const contentsRows = await buildContentsInventoryRows(manifestRows);
const artifact = buildArtifact(parentRouter, parentShelf, manifestRows, contentsRows);
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
  algebra_source_families_inventoried: artifact.gate_state.algebra_source_families_inventoried,
  algebra_manifest_route_rows: artifact.gate_state.algebra_manifest_route_rows,
  algebra_contents_inventory_rows: artifact.gate_state.algebra_contents_inventory_rows,
  algebra_metadata_rows_total: artifact.gate_state.algebra_metadata_rows_total,
  algebra_metadata_bytes_total: artifact.gate_state.algebra_metadata_bytes_total,
  algebra_packet_candidate_rows: artifact.gate_state.algebra_packet_candidate_rows,
  algebra_metadata_review_rows: artifact.gate_state.algebra_metadata_review_rows,
  blank_metadata_review_cells_allocated: artifact.gate_state.blank_metadata_review_cells_allocated,
  source_text_copied: artifact.gate_state.source_text_copied,
  translated_passages: artifact.gate_state.translated_passages,
  proposed_bridge_lexemes: artifact.gate_state.proposed_bridge_lexemes,
  accepted_bridge_surfaces: artifact.gate_state.accepted_bridge_surfaces,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
