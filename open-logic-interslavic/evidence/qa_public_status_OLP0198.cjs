const fs = require('fs');
const path = require('path');
const { pathToFileURL } = require('url');
const { chromium } = require('playwright');

const root = path.resolve(__dirname, '..');
const publicRoot = path.join(root, 'public_status_olp0198');
const htmlPath = path.join(publicRoot, 'index.html');
const output = path.join(root, 'evidence', 'html_qa_OLP0198');
const metricsPath = path.join(output, 'browser-metrics.json');

if (fs.existsSync(output)) throw new Error(`No-overwrite QA directory exists: ${output}`);
fs.mkdirSync(output, { recursive: true });

function localLinkAudit() {
  const html = fs.readFileSync(htmlPath, 'utf8');
  const references = [
    ...[...html.matchAll(/\bhref="([^"]+)"/g)].map(match => ({ attribute: 'href', value: match[1] })),
    ...[...html.matchAll(/\bdata="([^"]+)"/g)].map(match => ({ attribute: 'data', value: match[1] })),
  ];
  const rows = [];
  for (const reference of references) {
    const value = reference.value;
    if (/^(?:https?:|mailto:|#)/i.test(value)) continue;
    const decoded = decodeURIComponent(value.split(/[?#]/, 1)[0]);
    const target = path.resolve(publicRoot, decoded);
    const relative = path.relative(publicRoot, target);
    if (relative.startsWith('..') || path.isAbsolute(relative)) throw new Error(`Unsafe local ${reference.attribute}: ${value}`);
    rows.push({ attribute: reference.attribute, value, target: relative.replaceAll('\\', '/'), exists: fs.existsSync(target), bytes: fs.existsSync(target) ? fs.statSync(target).size : null });
  }
  const missing = rows.filter(row => !row.exists);
  if (missing.length) throw new Error(`Missing local references: ${JSON.stringify(missing)}`);
  return rows;
}

async function inspectPage(browser, name, viewport, isMobile) {
  const page = await browser.newPage({ viewport, deviceScaleFactor: 1, isMobile });
  const consoleErrors = [];
  const pageErrors = [];
  page.on('console', message => { if (message.type() === 'error') consoleErrors.push(message.text()); });
  page.on('pageerror', error => pageErrors.push(String(error)));
  await page.goto(pathToFileURL(htmlPath).href, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  const metrics = await page.evaluate(() => {
    const root = document.documentElement;
    const bodyText = document.body.innerText;
    const tableWrapper = document.querySelector('.tablewrap');
    const english = document.querySelector('.columns article[lang="en"]');
    const readerObject = document.querySelector('.reader object[type="application/pdf"]');
    const jsonLd = [...document.querySelectorAll('script[type="application/ld+json"]')].map(node => JSON.parse(node.textContent));
    return {
      viewport: { width: window.innerWidth, height: window.innerHeight },
      document: { clientWidth: root.clientWidth, scrollWidth: root.scrollWidth, scrollHeight: root.scrollHeight, horizontalOverflow: root.scrollWidth > root.clientWidth },
      tableWrapper: tableWrapper ? { clientWidth: tableWrapper.clientWidth, scrollWidth: tableWrapper.scrollWidth, overflowX: getComputedStyle(tableWrapper).overflowX } : null,
      markers: {
        checkpoint: bodyText.includes('OLP-0198'),
        interslavicPrimary: bodyText.includes('Open Logic na medžuslovjanskom jezyku'),
        englishParallel: bodyText.includes('Complete English counterpart'),
        acceptedMeaning: bodyText.includes('Neprijeta ne znači, že postoji kandidat') && bodyText.includes('Pending does not imply that a candidate exists'),
        title: bodyText.includes('Teorema interpolacije'),
        expertLog: bodyText.toLocaleLowerCase('en').includes('ekspertna knjiga odluka'),
        canonRange: bodyText.includes('OLISV-T0346') && bodyText.includes('OLISV-T0400'),
        nextUnit: bodyText.includes('OLP-0199'),
        readerPages: bodyText.includes('777'),
      },
      englishPanelVisible: !!english && !!(english.offsetWidth || english.offsetHeight || english.getClientRects().length),
      readerObject: readerObject ? { data: readerObject.getAttribute('data'), width: readerObject.clientWidth, height: readerObject.clientHeight, visible: !!(readerObject.offsetWidth || readerObject.offsetHeight || readerObject.getClientRects().length) } : null,
      jsonLdCount: jsonLd.length,
      jsonLdVersion: jsonLd[0]?.version ?? null,
      jsonLdLanguages: jsonLd[0]?.inLanguage ?? null,
    };
  });
  await page.screenshot({ path: path.join(output, `${name}-top.png`) });
  await page.screenshot({ path: path.join(output, `${name}-full.png`), fullPage: true });
  if (name === 'mobile') {
    await page.locator('.columns article[lang="en"]').first().screenshot({ path: path.join(output, 'mobile-english-panel.png') });
    await page.locator('.tablewrap').screenshot({ path: path.join(output, 'mobile-accepted-units-table.png') });
  }
  await page.close();
  if (consoleErrors.length || pageErrors.length) throw new Error(`${name} browser errors: ${JSON.stringify({ consoleErrors, pageErrors })}`);
  return { ...metrics, consoleErrors, pageErrors };
}

(async () => {
  const browser = await chromium.launch({
    headless: true,
    executablePath: 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
    args: ['--allow-file-access-from-files'],
  });
  try {
    const desktop = await inspectPage(browser, 'desktop', { width: 1280, height: 720 }, false);
    const mobile = await inspectPage(browser, 'mobile', { width: 390, height: 844 }, true);
    const localReferences = localLinkAudit();
    for (const [name, metrics] of Object.entries({ desktop, mobile })) {
      if (metrics.document.horizontalOverflow) throw new Error(`${name} document has horizontal overflow`);
      if (!Object.values(metrics.markers).every(Boolean) || !metrics.englishPanelVisible) throw new Error(`${name} required content is not visible: ${JSON.stringify({ markers: metrics.markers, englishPanelVisible: metrics.englishPanelVisible })}`);
      if (!metrics.readerObject?.visible || metrics.readerObject.data !== 'reader/OpenLogic-Interslavic-OLP0198-visual-checkpoint.pdf') throw new Error(`${name} PDF reader object mismatch`);
      if (metrics.jsonLdCount !== 1 || metrics.jsonLdVersion !== 'continuous-frontier-OLP-0198') throw new Error(`${name} JSON-LD mismatch`);
      if (JSON.stringify(metrics.jsonLdLanguages) !== JSON.stringify(['isv-Latn', 'en'])) throw new Error(`${name} JSON-LD language mismatch`);
    }
    if (mobile.tableWrapper.overflowX !== 'auto' || mobile.tableWrapper.scrollWidth <= mobile.tableWrapper.clientWidth) throw new Error('mobile accepted-units table is not locally scrollable');
    const result = { schema: 'openlogic-isv-local-html-browser-metrics/1.1', status: 'PASS', checkpoint: 'OLP-0198', source: 'public_status_olp0198/index.html', desktop, mobile, localReferences };
    fs.writeFileSync(metricsPath, JSON.stringify(result, null, 2) + '\n', 'utf8');
    process.stdout.write(JSON.stringify({ status: result.status, checkpoint: result.checkpoint, localReferences: localReferences.length, desktop, mobile }, null, 2) + '\n');
  } finally {
    await browser.close();
  }
})().catch(error => { process.stderr.write(String(error.stack || error) + '\n'); process.exitCode = 1; });
