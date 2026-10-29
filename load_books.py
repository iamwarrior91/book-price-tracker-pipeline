import csv
from datetime import datetime
from decimal import Decimal
from getpass import getpass
from pathlib import Path

import psycopg


CSV_PATH = Path("data/raw/books.csv")

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "price_tracker",
    "user": "postgres",
}


def clean_price(raw_price: str) -> Decimal:
    """Turn £51.77 into Decimal('51.77')."""
    numbers_only = "".join(
        character
        for character in raw_price
        if character.isdigit() or character == "."
    )
    return Decimal(numbers_only)


def load_books():
    if not CSV_PATH.exists():
        raise FileNotFoundError(
            f"Cannot find {CSV_PATH}. Run the Scrapy CSV export first."
        )

    password = getpass("Enter your PostgreSQL password: ")

    rows_to_insert = []

    with CSV_PATH.open(mode="r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            rows_to_insert.append(
                (
                    row["product_name"],
                    clean_price(row["price_gbp"]),
                    row["availability"],
                    row["rating"],
                    row["product_url"],
                    row["source"],
                    datetime.fromisoformat(row["scraped_at"]),
                )
            )

    insert_sql = """
        INSERT INTO raw_books (
            product_name,
            price_gbp,
            availability,
            rating,
            product_url,
            source,
            scraped_at
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """

    with psycopg.connect(**DB_CONFIG, password=password) as connection:
        with connection.cursor() as cursor:
            cursor.executemany(insert_sql, rows_to_insert)

    print(f"Success: loaded {len(rows_to_insert)} books into raw_books.")


if __name__ == "__main__":
    load_books()