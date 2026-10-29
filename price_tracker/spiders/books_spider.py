from datetime import datetime, timezone

import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/page-1.html"]

    def parse(self, response):
        scraped_at = datetime.now(timezone.utc).isoformat()

        for book in response.css("article.product_pod"):
            rating_classes = book.css("p.star-rating::attr(class)").get("").split()

            yield {
                "product_name": book.css("h3 a::attr(title)").get(),
                "price_gbp": book.css("p.price_color::text").get(),
                "availability": " ".join(
                    text.strip()
                    for text in book.css("p.instock.availability ::text").getall()
                    if text.strip()
                ),
                "rating": rating_classes[-1] if len(rating_classes) > 1 else None,
                "product_url": response.urljoin(book.css("h3 a::attr(href)").get()),
                "source": "Books to Scrape",
                "scraped_at": scraped_at,
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
