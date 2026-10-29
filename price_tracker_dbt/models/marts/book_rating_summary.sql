{{ config(materialized='table') }}

with rating_summary as (

    select
        rating,
        count(*) as book_count,
        round(avg(price_gbp), 2) as average_price_gbp,
        min(price_gbp) as lowest_price_gbp,
        max(price_gbp) as highest_price_gbp
    from {{ ref('stg_books') }}
    group by rating

)

select
    rating,
    case rating
        when 'one' then 1
        when 'two' then 2
        when 'three' then 3
        when 'four' then 4
        when 'five' then 5
    end as rating_sort_order,
    book_count,
    average_price_gbp,
    lowest_price_gbp,
    highest_price_gbp
from rating_summary
order by rating_sort_order