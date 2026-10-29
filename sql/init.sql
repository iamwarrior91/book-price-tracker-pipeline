CREATE TABLE raw_books (
    id BIGSERIAL PRIMARY KEY,
    product_name TEXT NOT NULL,
    price_gbp NUMERIC(10, 2),
    availability TEXT,
    rating TEXT,
    product_url TEXT NOT NULL,
    source TEXT NOT NULL,
    scraped_at TIMESTAMPTZ NOT NULL,
    loaded_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
