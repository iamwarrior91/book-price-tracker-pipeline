BOT_NAME = "price_tracker"

SPIDER_MODULES = ["price_tracker.spiders"]
NEWSPIDER_MODULE = "price_tracker.spiders"

# Respect the site's crawl instructions and avoid sending rapid requests.
ROBOTSTXT_OBEY = True
USER_AGENT = "price-tracker-learning-project/1.0"
DOWNLOAD_DELAY = 1

FEED_EXPORT_ENCODING = "utf-8"
