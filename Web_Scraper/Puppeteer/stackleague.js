const puppeteer = require("puppeteer");
require("dotenv").config();
const credentials = {
  email: process.env.EMAIL,
  password: process.env.PASSWORD,
};

(async () => {
  //get only 60 data on JSON file
  const getOnly = 550;

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

  //usercontribution
  const targetUrl = process.env.ADMIN_URL;
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
  const title = "MuiTypography-root MuiTypography-subtitle1";
  //contributor
  const contrib = "MuiTypography-colorTextSecondary";
  //status if pending or not
  const status = "MuiChip-label MuiChip-labelSmall";

  //get titles, contributor, and status
  const titles = await page.evaluate((title) => {
    const elements = Array.from(document.getElementsByClassName(title));
    return elements.map((element) => element.textContent.trim());
  }, title);

  const contribs = await page.evaluate((contrib) => {
    const elements = Array.from(document.getElementsByClassName(contrib));
    return elements.map((element) => element.textContent.trim());
  }, contrib);

  const stats = await page.evaluate((status) => {
    const elements = Array.from(document.getElementsByClassName(status));
    return elements.map((element) => element.textContent.trim());
  }, status);

  //console check if has data
  // console.log("Titles:", titles);
  // console.log("Contributors:", contribs);

  //put titles and contribs in JSON check only pending
  let data = [];
  for (let i = 0; i < getOnly; i++) {
    if (stats[i] === "Pending") {
      data.push({
        Title: titles[i],
        Contribution: contribs[i],
        Status: stats[i],
      });
    }
  }
  console.log(data);

  //put data in JSON
  const fs = require("fs");
  const path = require("path");
  // Create a Date object to get the current date
  const currentDate = new Date();

  // Format the date as YYYY-MM-DD
  const formattedDate = currentDate.toISOString().slice(0, 10);

  // Create the folder path with the formatted date
  const output = "../Output/stackdata";
  const folderPath = path.join(output, formattedDate);

  // Create the folder
  fs.mkdirSync(folderPath, { recursive: true });

  const fileName = "Puppeteer_web_scraped_data.json";
  const filePath = path.join(__dirname, folderPath, fileName);
  const file = fs.createWriteStream(filePath);
  file.write(JSON.stringify(data));
  file.end();
  console.log(`JSON created successfully! \n ${folderPath}${fileName}`);
  await browser.close();

  //Wait for the data to be written in JSON
  await new Promise((resolve) => {
    console.log("Writing Data (5 seconds)...)");
    setTimeout(resolve, 5000);
  });
  execute();
})();

const { exec } = require("child_process");

// Execute the python script
const execute = () => {
  const commandToRun = `Python  "../Python/PuppetCleanUp.py"`;

  exec(commandToRun, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error: ${error.message}`);
      return;
    }
    if (stderr) {
      console.error(`stderr: ${stderr}`);
      return;
    }
    console.log(`stdout: ${stdout}`);
  });
};
