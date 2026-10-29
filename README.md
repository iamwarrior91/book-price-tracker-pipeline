# Local Price Tracker Pipeline

This local data-engineering project collects book prices from the Books to Scrape practice website. The first milestone is a timestamped JSON snapshot; later we will load the data into PostgreSQL and transform it with dbt.

## Run the first scraper

From this folder in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
scrapy crawl books -O data\raw\books.json
```

The output file will contain the book title, price, availability, rating, product URL, source, and scrape timestamp for each book.
