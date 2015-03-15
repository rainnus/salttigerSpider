# -*- coding: utf-8 -*-
from scrapy.http import Request
from ebookCrawl.select_result import list_first_item,strip_null,deduplication,clean_url
from ebookCrawl.items import EbookcrawlItem
from scrapy.spider import Spider
from scrapy.spider  import BaseSpider
import os
# class blogSpider1(BaseSpider):
#     """docstring for blogSpider"""
#     name = "ebookSpider"
#     allowed_domains = {'salttiger.com'}
#     start_urls = {
#         'http://www.salttiger.com/page/2/'
#     }

#     def parse(self, response):
#     	for item in response.xpath(u'//article'):
# 	    	ebook_item = EbookcrawlItem()
# 	        ebook_item['bookName'] = item.xpath(u'//a[@rel="bookmark"]/@href').extract()
# 	        ebook_item['downloadUrl'] = item.xpath(u'//div[@class="entry-content"]/p[1]//a[2]/@href').extract()
# 	        itemDiscribution = clean_url(item.xpath(u'//div[@class="entry-content"]/p[2]/a[1]/@href').extract())
# 	        yield Request(url=itemDiscribution, callback=self.parse_discribution)
# 	        yield ebook_item
#         next_page = list_first_item(response.xpath(u'//a[@class="nextpostslink"]/@href').extract())
#         if next_page:
#             next_page = clean_url(response.url,next_page,response.encoding)
#             yield Request(url=next_page, callback=self.parse)
#             print next_page

#     # def parse_detail(self, response):


#     def parse_discribution(self, response):
#     	content = response.xpath(u'//article/div[@class="entry-content"]/p[4]').extract()
#     	return content
        
class blogSpider1(BaseSpider):
    """docstring for blogSpider"""
    name = "ebookSpider"
    allowed_domains = {'salttiger.com'}
    start_urls = {
        'http://www.salttiger.com/page/90/'
    }

    def parse(self, response):
    	ed2k = open('ed2k', 'a+')
    	for item in range(1,6):
			ebook_item = EbookcrawlItem()
			ebook_item['bookName'] = response.xpath(u'//article['+ str(item) +']//a[@rel="bookmark"]/text()').extract()
			ebook_item['downloadUrl'] = response.xpath(u'//article['+ str(item) +']/div[1]/p[1]//a[2]/@href').extract()
			yield ebook_item
			url = "".join(ebook_item['downloadUrl'])
			if url:
				if url[0] == 'h':
					bp="python /Users/rainnus/Documents/iScript-master/pan.baidu.com.py"
					string = bp + ' s '+ url + ' /ebook'
					os.system(string)
				elif url[0] == 'e':
					
					ed2k.write(url)
					
				else :
				 	continue
		# ed2k.close()
	        # itemDiscribution = clean_url(item.xpath(u'//div[@class="entry-content"]/p[2]/a[1]/@href').extract())
	        # yield Request(url=itemDiscribution, callback=self.parse_discribution)
	        

        next_page = response.xpath(u'//a[@class="nextpostslink"]/@href').extract()
        next_page = "".join(next_page)
        if next_page:
            yield Request(url=next_page, callback=self.parse)
            print next_page

    # def parse_detail(self, response):


    def parse_discribution(self, response):
    	content = response.xpath(u'//article/div[@class="entry-content"]/p[4]').extract()
    	return content