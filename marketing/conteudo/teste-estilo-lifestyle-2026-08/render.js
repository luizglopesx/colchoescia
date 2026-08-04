const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  const htmlPath = path.resolve(__dirname, 'post.html');
  await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1500);

  fs.mkdirSync(__dirname, { recursive: true });

  const ids = [
    'teste-01', 'teste-02', 'teste-03', 'teste-04', 'teste-05',
    'teste-06', 'teste-07', 'teste-08', 'teste-09', 'teste-10',
    'teste-11', 'teste-12', 'teste-13', 'teste-14', 'teste-15',
    'teste-16', 'teste-17', 'teste-18', 'teste-19', 'teste-20',
  ];

  for (const id of ids) {
    const el = await page.$(`#${id}`);
    await el.screenshot({ path: path.join(__dirname, `${id}.png`), type: 'png' });
    console.log(`✓ ${id}.png`);
  }

  await browser.close();
  console.log('\nPronto!');
})().catch(err => {
  console.error('Erro:', err.message);
  console.error('\nSe o Playwright não estiver instalado:');
  console.error('  npm install playwright && npx playwright install chromium');
  console.error('\nOu reutilize o node_modules do projeto:');
  console.error('  NODE_PATH=../../../../../../node_modules node render.js');
  process.exit(1);
});
