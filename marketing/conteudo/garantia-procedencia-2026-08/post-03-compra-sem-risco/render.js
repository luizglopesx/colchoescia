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

  const feed = await page.$('#post-03-feed');
  await feed.screenshot({ path: path.join(__dirname, 'post.png'), type: 'png' });
  console.log('✓ post.png');

  const story = await page.$('#post-03-story');
  await story.screenshot({ path: path.join(__dirname, 'story.png'), type: 'png' });
  console.log('✓ story.png');

  await browser.close();
  console.log('\nPronto!');
})().catch(err => {
  console.error('Erro:', err.message);
  process.exit(1);
});
