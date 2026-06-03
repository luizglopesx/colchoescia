const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  const htmlPath = path.resolve(__dirname, 'post.html');
  await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1500); // aguarda fontes

  const outDir = path.join(__dirname, 'instagram');
  fs.mkdirSync(outDir, { recursive: true });

  const feed = await page.$('.feed');
  await feed.screenshot({ path: path.join(outDir, 'post.png'), type: 'png' });
  console.log('✓ instagram/post.png');

  const story = await page.$('.story');
  await story.screenshot({ path: path.join(outDir, 'story.png'), type: 'png' });
  console.log('✓ instagram/story.png');

  await browser.close();
  console.log('\nPronto! Arquivos em instagram/');
})().catch(err => {
  console.error('Erro:', err.message);
  console.error('\nSe o Playwright não estiver instalado:');
  console.error('  npm install playwright && npx playwright install chromium');
  console.error('\nOu reutilize o node_modules de outra pasta:');
  console.error('  NODE_PATH=../../node_modules node render.js');
  process.exit(1);
});
