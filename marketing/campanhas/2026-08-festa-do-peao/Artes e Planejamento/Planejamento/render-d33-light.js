const { chromium } = require("playwright");
const path = require("path");

(async () => {
  const browser = await chromium.launch({
    executablePath: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
  });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1080 } });
  const htmlPath = path.resolve(__dirname, "post-piloto-v2-d33-light.html");

  await page.goto(`file://${htmlPath}`, { waitUntil: "networkidle" });
  await page.waitForTimeout(1200);

  const feed = await page.$(".feed");
  await feed.screenshot({
    path: path.join(__dirname, "..", "Artes", "post-piloto-v2-feed-d33-light.png"),
    type: "png",
  });

  await browser.close();
  console.log("✓ post-piloto-v2-feed-d33-light.png");
})().catch((error) => {
  console.error("Erro:", error.message);
  process.exit(1);
});
