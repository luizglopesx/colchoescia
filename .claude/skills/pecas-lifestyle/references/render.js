const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

// Ajuste esta lista com os ids reais de <div class="feed" id="..."> e
// <div class="story" id="..."> do post.html da peça antes de rodar.
const FEED_IDS = ['peca-01'];
const STORY_IDS = ['peca-01-story'];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  const htmlPath = path.resolve(__dirname, 'post.html');
  await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1500);

  fs.mkdirSync(__dirname, { recursive: true });

  for (const id of FEED_IDS) {
    const el = await page.$(`#${id}`);
    await el.screenshot({ path: path.join(__dirname, `${id}.png`), type: 'png' });
    console.log(`✓ ${id}.png`);
  }

  for (const id of STORY_IDS) {
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
