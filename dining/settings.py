# -*- coding: utf-8 -*-

# Scrapy settings for dining project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'dining'

SPIDER_MODULES = ['dining.spiders']
NEWSPIDER_MODULE = 'dining.spiders'

ITEM_PIPELINES = {
    'dining.pipelines.FilterItem': 300,
    'dining.pipelines.JsonWriterPipeline': 400,
}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dining (+http://www.yourdomain.com)'
