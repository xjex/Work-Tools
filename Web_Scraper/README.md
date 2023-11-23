# Puppeteer WebScraper

(Limited Data only Visible to Surface)
Puppeteer script will only scrape [Title, Author, Status]

1. Run Puppeteer Script `Puppeteer/stackleague.js` to Extract Data from the web site (50 data will only be extracted. can be adjusted on the code)
2. Run `Python/PuppetCleanUp.py`, Cleaning Files and Converting JSON to Excel

### Output

- `Puppeteer/stackleague.js` -> `Puppeteer_web_scraped_data.json`
- `Python/PuppetCleanUp.py` -> [`Puppeteer_web_cleaned.json`, `Puppeteer_Clean_Excel.xlsx`, `Puppeteer_Google_Drive_Ready.xlxs`]

# API Based Data Analysis

(Slow due to high volume of data)

## Data Extractions

1. Extract Data from API Via Postman (`API.json`)
2. Run `Python/Data Analyis/API_Data_CleanUp.js` (This will clean and extract Important informations)
3. Run `Python/Data Analyis/API_Write_Data_Excel` (This will write All the Cleaned Data in an Excel File)

### Output

- `Python/Data Analyis/API_Data_CleanUp.js` -> `Clean_API.json`
- `Python/Data Analyis/API_Write_Data_Excel` -> `API_Data.xlsx`

# Author Contribution Data Analysis

Count how many contributions for each author

Pre requisite ( _Puppeteer WebScraper_ )

Puppeteer WebScraper

1. Run Puppeteer WebScraper
2. Run `Python/Data Analysis/Autor_Contribution.py`

### Output

- `Stackleague_Log_Report_analytics.txt`

---

#### `UPDATE Log`

_November 20 , 2023_

- Puppeteer WebScraper
  - Added function to mimic the google drive `Master Challenge Contribution` format (spacing and colors)

_November 21 , 2023_

- Puppeteer WebScraper
  - Added triggers to (`Puppeteer/stackleague.js`) to automatically run Python Clean up Scripts (`Python/PuppetCleanUp.py` `) after scraping.
