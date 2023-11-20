const puppeteer = require("puppeteer");
require("dotenv").config();
const credentials = {
  email: process.env.EMAIL,
  password: process.env.PASSWORD,
};

(async () => {
  //get only 50 data on JSON
  const getOnly = 50;

  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  // Go to the login page
  await page.goto("https://www.stackleague.com/login");
  //type credentials and click login
  await page.type(`input[name="email"]`, credentials.email);
  await page.type(`input[name="password"]`, credentials.password);
  await page.click(`button[data-cy="sign-in-button"]`);

  // Wait for the page to load
  await page.waitForNavigation().then(() => console.log("Page loaded!"));

  // Get the URL of the page
  const reload = await page.url();
  const targetUrl = "https://www.stackleague.com/admin/user-contributions";
  console.log("URL:", reload);

  //check if you are in the Contribution dashboard
  if (reload === "https://www.stackleague.com/dashboard/challenges") {
    await page.waitForNavigation().then(() => console.log("Page loaded!"));
    console.log("You are in the dashboard");
    await page.goto(targetUrl);
  } else {
    console.log("You are not in the dashboard");
    await page.goto(targetUrl);
    console.log("Navigating");

    await new Promise((resolve) => {
      console.log("Navigating (3 seconds)...");
      setTimeout(resolve, 3000);
    });
    await page.goto(targetUrl);
  }

  await new Promise((resolve) => {
    console.log("Waiting for the Components to load (3 seconds)...)");
    setTimeout(resolve, 3000);
  });
  await page.keyboard.press("Escape");

  console.log("Waiting for the data 30 seconds...");
  // Wrap setTimeout in a Promise to use async/await
  await new Promise((resolve) => {
    //countdown in console
    let count = 25;
    const interval = setInterval(() => {
      console.log(count);
      count--;
    }, 1000);

    setTimeout(() => {
      clearInterval(interval);
    }, 25000);
    setTimeout(resolve, 25000);
  });
  console.log("Finished waiting.");
  //countdown in console

  //title
  const className = "MuiTypography-root MuiTypography-subtitle1";
  //contributor
  const contrib = "MuiTypography-colorTextSecondary";
  //status if pending or not
  const status = "MuiChip-label MuiChip-labelSmall";

  //get words, contributor, and status
  const words = await page.evaluate((className) => {
    const elements = Array.from(document.getElementsByClassName(className));
    return elements.map((element) => element.textContent.trim());
  }, className);

  const contribs = await page.evaluate((contrib) => {
    const elements = Array.from(document.getElementsByClassName(contrib));
    return elements.map((element) => element.textContent.trim());
  }, contrib);

  const stats = await page.evaluate((status) => {
    const elements = Array.from(document.getElementsByClassName(status));
    return elements.map((element) => element.textContent.trim());
  }, status);

  //console check if has data
  // console.log("Titles:", words);
  // console.log("Contributors:", contribs);

  //put words and contribs in JSON
  let data = [];
  for (let i = 0; i < getOnly; i++) {
    if (stats[i] === "Pending") {
      data.push({
        Title: words[i],
        Contribution: contribs[i],
        Status: stats[i],
      });
    }
  }
  console.log(data);

  //put data in JSON
  const fs = require("fs");
  const path = require("path");
  const output = "../Output/";
  const fileName = "Puppeteer_web_scraped_data.json";
  const filePath = path.join(__dirname, output, fileName);
  const file = fs.createWriteStream(filePath);
  file.write(JSON.stringify(data));
  file.end();
  console.log(`JSON created successfully! \n ${filePath}${fileName}`);
  await browser.close();
})();
