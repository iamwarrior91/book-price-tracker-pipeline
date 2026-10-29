{{ config(materialized='view') }}

select
    id,
    trim(product_name) as product_name,
    price_gbp,
    availability,
    lower(rating) as rating,
    product_url,
    source,
    scraped_at,
    loaded_at
from public.raw_books
where product_name is not null