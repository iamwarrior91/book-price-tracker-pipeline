# Book Price Tracker: Local Data Engineering Pipeline

## Overview
This project collects book data from Books to Scrape and turns it into a dashboard-ready dataset.

## Pipeline
Scrapy → CSV → Python → PostgreSQL → dbt → Power BI

## Tools Used
- Python and Scrapy
- PostgreSQL and pgAdmin
- dbt
- Power BI

## Dashboard
The dashboard shows:
- Number of books by rating
- Average book price by rating
- Lowest and highest prices for each rating

## How It Works
1. Scrape book data with Scrapy.
2. Save the data as a CSV file.
3. Load the CSV into PostgreSQL with Python.
4. Clean and summarize the data with dbt.
5. Visualize the summary in Power BI.