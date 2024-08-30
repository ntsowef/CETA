

BOT_NAME = 'ceta_scraper'

SPIDER_MODULES = ['ceta_scraper.spiders']
NEWSPIDER_MODULE = 'ceta_scraper.spiders'

# Respect robots.txt rules
ROBOTSTXT_OBEY = True

# Enable caching to avoid hitting the server too hard
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 86400  # Cache for a day

# Set user agent to avoid being blocked
USER_AGENT = 'ceta_scraper (+http://www.bakkie-connect.co.za)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32