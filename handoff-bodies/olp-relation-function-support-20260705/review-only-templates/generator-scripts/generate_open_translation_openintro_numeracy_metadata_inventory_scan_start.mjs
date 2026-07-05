import { readFile, writeFile, readdir, stat } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_METADATA_INVENTORY_SCAN_START_20260703T100000Z';
const noteId = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_METADATA_INVENTORY_SCAN_START_NOTE_20260703T100100Z';
const generatedUtc = '2026-07-03T10:00:00Z';
const noteGeneratedUtc = '2026-07-03T10:01:00Z';
const packageOrder = 159;
const queueCandidateId = 'OTCQ-OPEN-TRANSLATION-OPENINTRO-NUMERACY-METADATA-INVENTORY-SCAN-START-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';
const parentRouterFile = 'OPEN_TRANSLATION_REVIEW_ONLY_SOURCE_COORDINATE_SCAN_ROUTER_20260703T081500Z';
const parentShelfFile = 'OPEN_TRANSLATION_REVIEW_ONLY_PACKET_SOURCE_SHELF_REFRESH_20260703T080000Z';
const parentMiniShelfFile = 'OPENINTRO_NUMERACY_PUBLIC_SERVICE_SOURCE_MINI_SHELF_20260629T194849Z';
const parentExactEditionFile = 'OPENINTRO_NUMERACY_EXACT_EDITION_CAPTURE_20260629T200225Z';
const sourceCacheDir = 'outputs/source_cache/openintro_ims2';

const metadataReviewFields = [
  'inventory_review_date',
  'reviewer_route_or_role',
  'exact_edition_route_confirmed',
  'license_share_alike_gate_confirmed',
  'source_file_inventory_scope_accepted',
  'coordinate_scan_scope_recommended',
  'figure_table_dataset_file_policy_needed',
  'attribution_change_notice_needed',
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
  'source_tables_copied',
  'source_figures_copied',
  'source_datasets_copied',
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

function normalizeRel(value) {
  return String(value || '').replaceAll('\\', '/');
}

function extKey(filename) {
  const ext = path.extname(filename || '').toLowerCase();
  return ext || '[none]';
}

function sourceRouteClassFromFilename(name) {
  if (name.includes('license') || name.includes('legalcode') || name.includes('deed')) return 'license_share_alike_support_route';
  if (name.includes('README')) return 'repository_readme_support_route';
  if (name.includes('index_qmd')) return 'pinned_quarto_index_source_route';
  if (name.includes('quarto_yml')) return 'pinned_quarto_config_support_route';
  if (name.includes('ims2_web_home')) return 'rendered_web_exact_edition_route';
  if (name.includes('openintro_ims_book_page')) return 'openintro_book_page_route';
  if (name.includes('statistics_books')) return 'statistics_book_family_route';
  if (name.includes('leanpub')) return 'pdf_route_evidence_only';
  return 'cached_route_metadata_only';
}

async function buildCachedFileRows() {
  const entries = await readdir(path.join(root, sourceCacheDir), { withFileTypes: true });
  const rows = [];
  for (const entry of entries.filter((item) => item.isFile()).sort((a, b) => a.name.localeCompare(b.name))) {
    const relativePath = normalizeRel(path.join(sourceCacheDir, entry.name));
    const info = await stat(path.join(root, relativePath));
    const data = await readFile(path.join(root, relativePath));
    rows.push({
      openintro_cache_inventory_row_id: `OI-MINV-FILE-${String(rows.length + 1).padStart(3, '0')}`,
      source_family: 'OpenIntro IMS statistics and numeracy',
      cache_path: relativePath,
      filename: entry.name,
      extension: extKey(entry.name),
      route_class: sourceRouteClassFromFilename(entry.name),
      bytes: info.size,
      sha256: sha256Upper(data),
      source_text_copied: 0,
      source_passage_selected: false,
      source_table_selected: false,
      source_figure_selected: false,
      source_dataset_selected: false,
      excerpt_candidate: false,
      translation_started: false
    });
  }
  return rows;
}

function buildExactEditionRouteRows(exactEdition) {
  const rows = exactEdition.cached_sources || [];
  return rows.map((row, index) => ({
    exact_edition_route_row_id: `OI-MINV-EXACT-${String(index + 1).padStart(3, '0')}`,
    parent_source_row_id: row.source_row_id,
    route_use: row.route_use,
    url: row.url,
    cache_path: normalizeRel(row.cache_path),
    bytes: row.bytes,
    sha256: row.sha256,
    route_class: sourceRouteClassFromFilename(path.basename(row.cache_path || '')),
    source_text_copied: 0,
    source_passage_selected: false,
    excerpt_candidate: false,
    translation_started: false
  }));
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

function buildPacketSlotRows(miniShelf, exactEdition) {
  const slots = exactEdition.numeracy_packet_fit || miniShelf.public_service_numeracy_packet_fit || [];
  return slots.map((row, index) => ({
    numeracy_packet_slot_row_id: `OI-MINV-SLOT-${String(index + 1).padStart(2, '0')}`,
    neutral_packet_slot: row.neutral_packet_slot,
    source_fit: row.source_fit,
    still_required: row.still_required,
    source_text_or_excerpt_allowed_now: false,
    translation_allowed_now: false,
    local_surface_allowed_now: false
  }));
}

function buildLaneFitRows(miniShelf) {
  return (miniShelf.lane_fit || []).map((row, index) => ({
    numeracy_lane_fit_row_id: `OI-MINV-LANE-${String(index + 1).padStart(2, '0')}`,
    lane_group: row.lane_group,
    first_use: row.first_use,
    gate: row.gate,
    source_text_or_excerpt_allowed_now: false,
    translation_allowed_now: false,
    pilot_ready: false
  }));
}

function buildReviewRows(cachedFileRows, exactRouteRows) {
  const routeGroups = [
    {
      review_scope: 'exact_edition_and_rendered_web_routes',
      route_classes: ['rendered_web_exact_edition_route', 'openintro_book_page_route', 'statistics_book_family_route'],
      next_policy_artifact: 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_SOURCE_COORDINATE_POLICY_SHEET_<timestamp>'
    },
    {
      review_scope: 'license_share_alike_and_attribution_routes',
      route_classes: ['license_share_alike_support_route'],
      next_policy_artifact: 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LICENSE_ATTRIBUTION_POLICY_RETURN_TEMPLATE_<timestamp>'
    },
    {
      review_scope: 'repository_quarto_source_routes',
      route_classes: ['repository_readme_support_route', 'pinned_quarto_index_source_route', 'pinned_quarto_config_support_route'],
      next_policy_artifact: 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_REPOSITORY_ROUTE_POLICY_SHEET_<timestamp>'
    },
    {
      review_scope: 'pdf_and_external_access_routes',
      route_classes: ['pdf_route_evidence_only'],
      next_policy_artifact: 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_PDF_ROUTE_DECISION_LEDGER_TEMPLATE_<timestamp>'
    }
  ];
  return routeGroups.map((group, index) => {
    const linkedCachedRows = cachedFileRows.filter((row) => group.route_classes.includes(row.route_class));
    const linkedExactRows = exactRouteRows.filter((row) => group.route_classes.includes(row.route_class));
    return {
      openintro_metadata_review_row_id: `OI-MINV-REV-${String(index + 1).padStart(2, '0')}`,
      review_scope: group.review_scope,
      route_classes: group.route_classes,
      linked_cache_inventory_row_ids: linkedCachedRows.map((row) => row.openintro_cache_inventory_row_id),
      linked_exact_edition_route_row_ids: linkedExactRows.map((row) => row.exact_edition_route_row_id),
      metadata_inventory_rows_recorded: linkedCachedRows.length + linkedExactRows.length,
      metadata_inventory_bytes_recorded: [...linkedCachedRows, ...linkedExactRows].reduce((sum, row) => sum + (row.bytes || 0), 0),
      blank_metadata_review_fields: metadataReviewFields,
      inventory_review_date: null,
      reviewer_route_or_role: null,
      exact_edition_route_confirmed: null,
      license_share_alike_gate_confirmed: null,
      source_file_inventory_scope_accepted: null,
      coordinate_scan_scope_recommended: null,
      figure_table_dataset_file_policy_needed: null,
      attribution_change_notice_needed: null,
      next_coordinate_policy_artifact: group.next_policy_artifact,
      review_note_without_source_prose: null,
      metadata_review_fields_filled: 0,
      metadata_inventory_review_completed: false,
      coordinate_scan_authorized: false,
      excerpt_selection_authorized: false,
      translation_authorized: false,
      still_locked_reason: 'metadata_inventory_recorded_but_not_reviewed_no_coordinate_scan_scope_or_license_share_alike_decision'
    };
  });
}

function buildArtifact(parentRouter, parentShelf, miniShelf, exactEdition, cachedFileRows, exactRouteRows) {
  const extensionSummaryRows = summarize(cachedFileRows, 'extension', 'OI-MINV-EXT');
  const routeClassSummaryRows = summarize(cachedFileRows, 'route_class', 'OI-MINV-ROUTE');
  const exactRouteUseSummaryRows = summarize(exactRouteRows, 'route_use', 'OI-MINV-EXACT-USE');
  const packetSlotRows = buildPacketSlotRows(miniShelf, exactEdition);
  const laneFitRows = buildLaneFitRows(miniShelf);
  const reviewRows = buildReviewRows(cachedFileRows, exactRouteRows);
  const blankReviewCells = reviewRows.length * metadataReviewFields.length;
  const metadataBytes = cachedFileRows.reduce((sum, row) => sum + row.bytes, 0) + exactRouteRows.reduce((sum, row) => sum + row.bytes, 0);

  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'openintro_numeracy_metadata_inventory_scan_start_no_source_text_no_excerpts_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Start the OpenIntro IMS statistics/public-numeracy coordinate path with a metadata-only inventory of cached route files and exact-edition route rows, preserving file/path/route/license metadata while copying no source text, selecting no excerpts, and starting no translation or constructed surface work.',
    parent_artifacts: [
      parentRouterFile,
      parentShelfFile,
      parentMiniShelfFile,
      parentExactEditionFile,
      'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z'
    ],
    parent_router_rows_used: parentRouter.coordinate_router_rows
      .filter((row) => row.source_family.includes('OpenIntro'))
      .map((row) => row.coordinate_router_row_id),
    parent_route_task_rows_used: parentRouter.coordinate_route_task_rows
      .filter((row) => row.source_family.includes('OpenIntro'))
      .map((row) => row.coordinate_route_task_row_id),
    parent_shelf_rows_used: parentShelf.source_shelf_rows
      .filter((row) => row.source_family.includes('OpenIntro'))
      .map((row) => row.source_shelf_row_id),
    exact_edition_reading_metadata: {
      title: exactEdition.exact_edition_reading?.title,
      edition: exactEdition.exact_edition_reading?.edition,
      rendered_version_date: exactEdition.exact_edition_reading?.rendered_version_date,
      source_repository_head_at_capture: exactEdition.exact_edition_reading?.source_repository_head_at_capture,
      license_route: exactEdition.exact_edition_reading?.license_route,
      pdf_file_status: exactEdition.exact_edition_reading?.pdf_file_status
    },
    boundary: {
      artifact_is: [
        'metadata-only OpenIntro numeracy inventory scan start',
        'cached route and exact-edition metadata catalog',
        'blank metadata-review allocator for source, license, repository, and PDF route classes'
      ],
      artifact_is_not: [
        'source excerpt',
        'source text copy',
        'table, figure, dataset, definition, or example extraction',
        'line-span selection',
        'license or share-alike clearance decision',
        'translation draft',
        'constructed-language form proposal',
        'pilot or publication readiness claim'
      ],
      promotion_requires: [
        'metadata inventory review return',
        'CC BY-SA attribution/change/share-alike planning decision',
        'file-level figure table dataset policy if any non-prose item is considered',
        'separate coordinate policy sheet',
        'separate selected-excerpt sidecar before any translation or adaptation'
      ]
    },
    openintro_cache_inventory_rows: cachedFileRows,
    exact_edition_route_rows: exactRouteRows,
    extension_summary_rows: extensionSummaryRows,
    route_class_summary_rows: routeClassSummaryRows,
    exact_route_use_summary_rows: exactRouteUseSummaryRows,
    numeracy_packet_slot_rows: packetSlotRows,
    numeracy_lane_fit_rows: laneFitRows,
    openintro_metadata_review_rows: reviewRows,
    gate_state: {
      openintro_source_families_inventoried: 1,
      openintro_cache_inventory_rows: cachedFileRows.length,
      exact_edition_route_rows: exactRouteRows.length,
      openintro_metadata_rows_total: cachedFileRows.length + exactRouteRows.length,
      openintro_metadata_bytes_total: metadataBytes,
      extension_summary_rows: extensionSummaryRows.length,
      route_class_summary_rows: routeClassSummaryRows.length,
      exact_route_use_summary_rows: exactRouteUseSummaryRows.length,
      numeracy_packet_slot_rows: packetSlotRows.length,
      numeracy_lane_fit_rows: laneFitRows.length,
      openintro_metadata_review_rows: reviewRows.length,
      blank_metadata_review_fields_per_row: metadataReviewFields.length,
      blank_metadata_review_cells_allocated: blankReviewCells,
      metadata_inventory_reviews_completed: 0,
      coordinate_scans_authorized: 0,
      excerpt_selections_authorized: 0,
      source_text_or_excerpt_files_created: 0,
      source_text_copied: 0,
      source_definitions_copied: 0,
      source_examples_copied: 0,
      source_tables_copied: 0,
      source_figures_copied: 0,
      source_datasets_copied: 0,
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
      expected_openintro_source_families_inventoried: 1,
      expected_min_cache_inventory_rows: 1,
      expected_min_exact_edition_route_rows: 1,
      expected_metadata_review_rows: 4,
      expected_blank_metadata_review_fields_per_row: metadataReviewFields.length,
      expected_blank_metadata_review_cells_allocated: blankReviewCells,
      zero_gate_assertions: zeroGateKeys,
      readiness_claims: 0
    },
    next_valid_artifacts: [
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_SOURCE_COORDINATE_POLICY_SHEET_<timestamp>',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_METADATA_INVENTORY_REVIEW_RETURN_LEDGER_TEMPLATE_<timestamp>',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LICENSE_ATTRIBUTION_POLICY_RETURN_TEMPLATE_<timestamp>',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_SELECTED_EXCERPT_SIDECAR_<timestamp>_only_after_review_and_license_decisions'
    ],
    decision: 'Package 159 records metadata-only OpenIntro IMS numeracy inventory. It increases source-route knowledge while keeping source-text, excerpt, table, figure, dataset, translation, constructed-surface, license-clearance, pilot, and publication gates closed.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const extRows = artifact.extension_summary_rows.map((row) => `| ${row.summary_row_id} | ${row.group_key} | ${row.rows} | ${formatNumber(row.bytes)} |`).join('\n');
  const routeRows = artifact.route_class_summary_rows.map((row) => `| ${row.summary_row_id} | ${row.group_key} | ${row.rows} | ${formatNumber(row.bytes)} |`).join('\n');
  const reviewRows = artifact.openintro_metadata_review_rows.map((row) => `| ${row.openintro_metadata_review_row_id} | ${row.review_scope} | ${row.metadata_inventory_rows_recorded} | ${formatNumber(row.metadata_inventory_bytes_recorded)} | ${row.metadata_review_fields_filled} |`).join('\n');
  const slotRows = artifact.numeracy_packet_slot_rows.map((row) => `| ${row.numeracy_packet_slot_row_id} | ${row.neutral_packet_slot} | ${row.source_text_or_excerpt_allowed_now} | ${row.translation_allowed_now} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Counts

- Cache inventory rows: \`${g.openintro_cache_inventory_rows}\`
- Exact-edition route rows: \`${g.exact_edition_route_rows}\`
- Metadata rows total: \`${g.openintro_metadata_rows_total}\`
- Metadata bytes total: \`${formatNumber(g.openintro_metadata_bytes_total)}\`
- Numeracy packet slot rows: \`${g.numeracy_packet_slot_rows}\`
- Lane-fit rows: \`${g.numeracy_lane_fit_rows}\`
- Metadata review rows: \`${g.openintro_metadata_review_rows}\`
- Blank metadata-review cells: \`${g.blank_metadata_review_cells_allocated}\`

## Extension Summary

| Row | Extension | Rows | Bytes |
| --- | --- | ---: | ---: |
${extRows}

## Route Class Summary

| Row | Route class | Rows | Bytes |
| --- | --- | ---: | ---: |
${routeRows}

## Numeracy Packet Slots

| Row | Slot | Source/excerpt allowed now | Translation allowed now |
| --- | --- | --- | --- |
${slotRows}

## Metadata Review Rows

| Row | Scope | Inventory rows | Inventory bytes | Filled review fields |
| --- | --- | ---: | ---: | ---: |
${reviewRows}

## Zero Gates

- Metadata inventory reviews completed: \`0\`
- Coordinate scans / excerpt selections authorized: \`0 / 0\`
- Source text/excerpt files: \`0\`
- Source text/definitions/examples copied: \`0 / 0 / 0\`
- Tables / figures / datasets copied: \`0 / 0 / 0\`
- Source passages selected: \`0\`
- Exact spans / candidate line ranges: \`0 / 0\`
- Translated passages: \`0\`
- Proposed bridge lexemes / morphemes / syntax / displays: \`0 / 0 / 0 / 0\`
- Accepted bridge surfaces / local-language terms: \`0 / 0\`
- Reviewer returns / license rechecks completed: \`0 / 0\`
- Readiness: \`publication=false, translation=false, constructed_surface=false, pilot=false\`

Boundary: this is metadata-only inventory. It records route/file/license metadata but no source prose, tables, figures, datasets, examples, excerpts, line-span selections, translations, constructed forms, or readiness claim.
`;
}

function buildArtifactCsv(artifact) {
  const rows = [];
  rows.push(['section', 'row_id', 'source_family', 'path_or_slot', 'route_class_or_scope', 'bytes_or_rows', 'source_text_copied', 'excerpt_candidate'].map(csvCell).join(','));
  for (const row of artifact.openintro_cache_inventory_rows) {
    rows.push([
      'openintro_cache_inventory_row',
      row.openintro_cache_inventory_row_id,
      row.source_family,
      row.cache_path,
      row.route_class,
      row.bytes,
      row.source_text_copied,
      row.excerpt_candidate
    ].map(csvCell).join(','));
  }
  for (const row of artifact.exact_edition_route_rows) {
    rows.push([
      'exact_edition_route_row',
      row.exact_edition_route_row_id,
      'OpenIntro IMS statistics and numeracy',
      row.cache_path,
      row.route_use,
      row.bytes,
      row.source_text_copied,
      row.excerpt_candidate
    ].map(csvCell).join(','));
  }
  for (const row of artifact.openintro_metadata_review_rows) {
    rows.push([
      'openintro_metadata_review_row',
      row.openintro_metadata_review_row_id,
      'OpenIntro IMS statistics and numeracy',
      row.review_scope,
      row.route_classes,
      row.metadata_inventory_rows_recorded,
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
    status: 'pointer_only_package159_openintro_numeracy_metadata_inventory_note_no_remote_action_no_source_text_no_translation_no_readiness',
    summary: 'Package 159 records metadata-only OpenIntro IMS numeracy route inventory rows and blank metadata-review rows.',
    counts: {
      openintro_cache_inventory_rows: g.openintro_cache_inventory_rows,
      exact_edition_route_rows: g.exact_edition_route_rows,
      openintro_metadata_rows_total: g.openintro_metadata_rows_total,
      numeracy_packet_slot_rows: g.numeracy_packet_slot_rows,
      openintro_metadata_review_rows: g.openintro_metadata_review_rows,
      blank_metadata_review_cells_allocated: g.blank_metadata_review_cells_allocated
    },
    zero_gates: {
      metadata_inventory_reviews_completed: 0,
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
  return `# Package 159 OpenIntro Numeracy Metadata Inventory Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only local note: package 159 records \`${g.openintro_cache_inventory_rows}\` cached-file metadata rows, \`${g.exact_edition_route_rows}\` exact-edition route rows, and \`${g.openintro_metadata_review_rows}\` blank metadata-review rows for OpenIntro IMS statistics/public numeracy.

Zero gates: \`0\` metadata inventory reviews completed, \`0\` coordinate scans authorized, \`0\` excerpt selections authorized, \`0\` source-text/excerpt files, \`0\` source text copied, \`0\` tables/figures/datasets copied, \`0\` translations, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` reviewer returns ingested, \`0\` readiness claims.

Boundary: metadata-only numeracy inventory start. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, source-text, excerpt, proposed form, accepted surface, translation, publication, pilot, legal-advice, or remote-state claim.
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
    role: 'open_translation_openintro_numeracy_metadata_inventory_scan_start',
    artifact: artifactId,
    current_use: `${g.openintro_metadata_rows_total} OpenIntro numeracy metadata rows; ${g.numeracy_packet_slot_rows} packet slot rows; ${g.openintro_metadata_review_rows} blank metadata-review rows; 0 source text, 0 excerpts, 0 tables/figures/datasets copied, 0 translations, 0 forms, 0 readiness`
  };
  const existingPackageRowIndex = order.findIndex((row) => row?.artifact === artifactId);
  if (existingPackageRowIndex >= 0) order[existingPackageRowIndex] = { ...order[existingPackageRowIndex], ...packageRow };
  else order.push(packageRow);
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_open_translation_openintro_numeracy_metadata_inventory_scan_start = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_openintro_numeracy_metadata_inventory_rows: g.openintro_metadata_rows_total,
    current_openintro_numeracy_metadata_review_rows: g.openintro_metadata_review_rows,
    current_openintro_numeracy_source_text_or_excerpt_files: 0,
    current_openintro_numeracy_translated_passages: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_openintro_numeracy_source_coordinate_policy_sheet_or_metadata_review_return_template_only_no_source_text_no_excerpts_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'Open translation OpenIntro numeracy metadata inventory scan start',
    route: artifactId,
    license_status_to_recheck: 'metadata_inventory_only_recheck_OpenIntro_IMS_CC_BY_SA_attribution_change_share_alike_and_file_level_table_figure_dataset_routes_before_any_coordinate_scan_excerpt_adaptation_or_translation',
    best_translation_use: 'statistics/public numeracy file and route metadata inventory before later coordinate policy, attribution, share-alike, or local-language reviewer decisions',
    candidate_lanes: [
      'statistics_public_numeracy',
      'OpenIntro_IMS',
      'data_literacy',
      'public_service_numeracy',
      'source_coordinate_policy',
      'share_alike_attribution_review'
    ],
    priority: 1,
    status: 'metadata_inventory_scan_start_no_source_text_no_excerpts_no_tables_figures_datasets_no_translation_no_forms_no_pilot',
    gate_state: {
      openintro_metadata_rows_total: g.openintro_metadata_rows_total,
      numeracy_packet_slot_rows: g.numeracy_packet_slot_rows,
      openintro_metadata_review_rows: g.openintro_metadata_review_rows,
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
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_open_translation_openintro_numeracy_metadata_inventory_scan_start: ${artifactId}_${g.openintro_metadata_rows_total}_metadata_rows_0_source_text_0_excerpts_0_translation_upload_when_path_exists_no_mobile_plan_deferral`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_open_translation_openintro_numeracy_metadata_inventory_scan_start_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_open_translation_openintro_numeracy_metadata_inventory_scan_start_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_openintro_numeracy_metadata_inventory_rows: g.openintro_metadata_rows_total,
    current_openintro_numeracy_metadata_review_rows: g.openintro_metadata_review_rows,
    current_openintro_numeracy_source_text_or_excerpt_files: 0,
    current_openintro_numeracy_translated_passages: 0,
    current_openintro_numeracy_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_open_translation_openintro_numeracy_metadata_inventory_scan_start = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_open_translation_openintro_numeracy_metadata_inventory_scan_start: ${artifactId}_metadata_inventory_before_any_coordinate_scan_results_excerpts_translations_surfaces_or_pilot_claims`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_open_translation_openintro_numeracy_metadata_inventory_scan_start = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: records ${g.openintro_metadata_rows_total} OpenIntro IMS numeracy metadata rows and ${g.openintro_metadata_review_rows} blank metadata-review rows; substantive upload-bound artifact; 0 source text, 0 excerpts, 0 tables/figures/datasets copied, 0 translations, 0 proposed forms, 0 accepted surfaces, 0 readiness.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OpenIntro numeracy metadata inventory scan start; ${g.openintro_metadata_rows_total} metadata rows, ${g.openintro_metadata_review_rows} blank metadata-review rows, 0 source text, 0 excerpts, 0 tables/figures/datasets, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 159: OpenIntro numeracy metadata inventory scan start. It records ${g.openintro_metadata_rows_total} metadata-only inventory rows and ${g.openintro_metadata_review_rows} blank metadata-review rows while keeping 0 source text, 0 excerpts, 0 tables/figures/datasets copied, 0 translations, 0 proposed forms, 0 accepted surfaces, and all readiness gates closed. It is upload-bound as substantive catalog/control work when a valid staging path exists.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | Open translation OpenIntro numeracy metadata inventory scan start | ${artifactId} | Metadata-only OpenIntro IMS inventory; ${g.openintro_metadata_rows_total} rows, 0 source text, 0 excerpts, 0 translation, upload when path exists. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_open_translation_openintro_numeracy_metadata_inventory_scan_start_artifact: \`${artifactId}\` (${g.openintro_metadata_rows_total} metadata inventory rows; 0 source text; 0 excerpts; 0 accepted surfaces or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_open_translation_openintro_numeracy_metadata_inventory_scan_start: \`${artifactId}\`; metadata-only OpenIntro IMS numeracy inventory, no source text, excerpts, accepted terms, surfaces, translation, or pilot.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OpenIntro IMS public numeracy metadata inventory start; substantive and upload-bound, but not a source excerpt, table, figure, dataset, translation, constructed form, license clearance, or readiness claim.`);
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
    { filename: `${artifactId}.json`, class: 'open_translation_openintro_numeracy_metadata_inventory_scan_start' },
    { filename: `${artifactId}.md`, class: 'open_translation_openintro_numeracy_metadata_inventory_scan_start' },
    { filename: `${artifactId}.csv`, class: 'open_translation_openintro_numeracy_metadata_inventory_scan_start' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'open_translation_package159_coordination_note' },
    { filename: `${noteId}.md`, class: 'open_translation_package159_coordination_note' },
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
  upload.obj.package159_upload_queue_update = {
    captured_utc: '2026-07-03T10:02:00Z',
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
  const step = 'Stage package 159 OpenIntro numeracy metadata inventory scan start artifacts as substantive beyond-core translation/source-route catalog material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (g.openintro_source_families_inventoried !== artifact.validation_snapshot.expected_openintro_source_families_inventoried) failures.push(`source_family_count_mismatch_${g.openintro_source_families_inventoried}`);
  if (g.openintro_cache_inventory_rows < artifact.validation_snapshot.expected_min_cache_inventory_rows) failures.push(`too_few_cache_rows_${g.openintro_cache_inventory_rows}`);
  if (g.exact_edition_route_rows < artifact.validation_snapshot.expected_min_exact_edition_route_rows) failures.push(`too_few_exact_rows_${g.exact_edition_route_rows}`);
  if (g.openintro_metadata_review_rows !== artifact.validation_snapshot.expected_metadata_review_rows) failures.push(`review_rows_mismatch_${g.openintro_metadata_review_rows}`);
  if (g.blank_metadata_review_fields_per_row !== artifact.validation_snapshot.expected_blank_metadata_review_fields_per_row) failures.push(`blank_review_fields_mismatch_${g.blank_metadata_review_fields_per_row}`);
  if (g.blank_metadata_review_cells_allocated !== artifact.validation_snapshot.expected_blank_metadata_review_cells_allocated) failures.push(`blank_review_cells_mismatch_${g.blank_metadata_review_cells_allocated}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.openintro_metadata_review_rows) {
    const filled = metadataReviewFields.some((field) => row[field] !== null && field !== 'next_coordinate_policy_artifact');
    if (filled || row.metadata_review_fields_filled !== 0 || row.metadata_inventory_review_completed || row.coordinate_scan_authorized || row.excerpt_selection_authorized || row.translation_authorized) {
      failures.push(`nonblank_or_open_metadata_review_row_${row.openintro_metadata_review_row_id}`);
      break;
    }
  }
  if ([...artifact.openintro_cache_inventory_rows, ...artifact.exact_edition_route_rows].some((row) => row.source_text_copied !== 0 || row.source_passage_selected || row.excerpt_candidate || row.translation_started)) {
    failures.push('inventory_row_opened_source_or_translation_gate');
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const parentRouter = (await readJson(parentRouterFile)).obj;
const parentShelf = (await readJson(parentShelfFile)).obj;
const miniShelf = (await readJson(parentMiniShelfFile)).obj;
const exactEdition = (await readJson(parentExactEditionFile)).obj;
const cachedFileRows = await buildCachedFileRows();
const exactRouteRows = buildExactEditionRouteRows(exactEdition);
const artifact = buildArtifact(parentRouter, parentShelf, miniShelf, exactEdition, cachedFileRows, exactRouteRows);
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
  openintro_cache_inventory_rows: artifact.gate_state.openintro_cache_inventory_rows,
  exact_edition_route_rows: artifact.gate_state.exact_edition_route_rows,
  openintro_metadata_rows_total: artifact.gate_state.openintro_metadata_rows_total,
  openintro_metadata_bytes_total: artifact.gate_state.openintro_metadata_bytes_total,
  numeracy_packet_slot_rows: artifact.gate_state.numeracy_packet_slot_rows,
  numeracy_lane_fit_rows: artifact.gate_state.numeracy_lane_fit_rows,
  openintro_metadata_review_rows: artifact.gate_state.openintro_metadata_review_rows,
  blank_metadata_review_cells_allocated: artifact.gate_state.blank_metadata_review_cells_allocated,
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
