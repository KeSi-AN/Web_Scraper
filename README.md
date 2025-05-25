# RERA Odisha Projects Scraper

This Python script scrapes the first 6 "Projects Registered" from the [Odisha RERA website](https://rera.odisha.gov.in/projects/project-list) using Playwright.

## Features

- Extracts the following details from the first 6 registered projects:
  - Project Name
  - RERA Registration Number
  - Promoter Name
  - Promoter Address
  - Promoter GST Number

## Why Playwright?

Playwright is used instead of Selenium because:
- No external drivers are needed
- Better support for JavaScript-heavy websites
- Faster execution and easier installation
- Built-in headless mode and browser management

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

Then install the required browsers for Playwright:

```bash
playwright install
```

## How to Run

Run the scraper with:

```bash
python scrape_rera.py
```

This will launch a headless browser, scrape the required data, and print it to the console.