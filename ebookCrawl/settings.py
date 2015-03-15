# -*- coding: utf-8 -*-

# Scrapy settings for ebookCrawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ebookCrawl'

SPIDER_MODULES = ['ebookCrawl.spiders']
NEWSPIDER_MODULE = 'ebookCrawl.spiders'

# HEADER = {
# 	"Host": "pan.baidu.com",
#     "Connection": "keep-alive",
#     "Cache-Control": "no-cache",
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.53 Safari/537.36",
#     "Referer": "http://pan.baidu.com/s/1mgzcTRU",
#     "Accept-Encoding": "gzip,deflate,sdch",
#     "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2",
# }

# COOKIES={
# 	"ATS_PASS" = "1",
# }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ebookCrawl (+http://www.yourdomain.com)'
