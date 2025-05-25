# Odisha RERA Project Scraper

This Python script uses Selenium to scrape the first 6 projects listed on the [Odisha RERA Projects List](https://rera.odisha.gov.in/projects/project-list) website. It collects the following details for each project by navigating through their respective "View Details" pages:

- **RERA Regd. No.**
- **Project Name**
- **Promoter Name** (Company Name under Promoter Details)
- **Promoter Address** (Registered Office Address)
- **GST No.**

## 🔧 Requirements

- Python 3.7+
- Google Chrome browser installed
- ChromeDriver (managed automatically via `webdriver-manager`)

### 📦 Required Python Packages

- `selenium`
- `webdriver-manager`

## 🚀 Setup Instructions

1. **Clone the repository or unzip the downloaded ZIP.**
2. **Install dependencies** (in your terminal or command prompt):
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script**:
   ```bash
   python scrape_orera.py
   ```

## 📄 Notes

- The script uses `webdriver-manager` to automatically handle downloading and setting up ChromeDriver. Ensure your Chrome browser is up-to-date.
- If you prefer to manually manage ChromeDriver, make sure it's available in your system's PATH.

## ✅ Output

The script will print the scraped details for the first 6 projects directly to the terminal.

