const { chromium } = require('playwright');
const path = require('path');

const posts = [
  { html: 'post1-dormir-bem.html', feed: 'post1-feed.png', story: 'post1-story.png' },
  { html: 'post2-preco-vizinho.html', feed: 'post2-feed.png', story: 'post2-story.png' },
  { html: 'post3-sono-merece.html', feed: 'post3-feed.png', story: 'post3-story.png' },
];

(async () => {
  const browser = await chromium.launch();

  for (const post of posts) {
    const page = await browser.newPage();
    const htmlPath = path.resolve(__dirname, post.html);
    await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle' });
    await page.waitForTimeout(1500);

    const feed = await page.$('.feed');
    await feed.screenshot({ path: path.join(__dirname, post.feed), type: 'png' });
    console.log('✓ ' + post.feed);

    const story = await page.$('.story');
    await story.screenshot({ path: path.join(__dirname, post.story), type: 'png' });
    console.log('✓ ' + post.story);

    await page.close();
  }

  await browser.close();
  console.log('\nPronto! 3 posts + 3 stories renderizados.');
})().catch(err => {
  console.error('Erro:', err.message);
  process.exit(1);
});
