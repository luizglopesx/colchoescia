const { chromium } = require("playwright");
const path = require("path");

(async () => {
  const browser = await chromium.launch({
    executablePath: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
  });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  const htmlPath = path.resolve(__dirname, "post-piloto-v2-story-d33-light-solteiro.html");

  await page.goto(`file://${htmlPath}`, { waitUntil: "networkidle" });
  await page.waitForTimeout(1200);

  const story = await page.$(".story");
  await story.screenshot({
    path: path.join(__dirname, "..", "Artes", "post-piloto-v2-story-d33-light-solteiro.png"),
    type: "png",
  });

  await browser.close();
  console.log("✓ post-piloto-v2-story-d33-light-solteiro.png");
})().catch((error) => {
  console.error("Erro:", error.message);
  process.exit(1);
});
