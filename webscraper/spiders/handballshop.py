import scrapy

class HandballShopSpider(scrapy.Spider):
    name = "handballshop"
    start_urls = [
        'https://www.handballshop.com/handballshoes',
    ]

    def parse(self, response):
        for item in response.css('div.product-info h2.product-name a'):
            yield {
                'aff_url': item.css('a::attr(href)').extract_first(),
                'aff_title': item.css('a::text').extract_first(),
            }

        next_page = response.css('div.pager a.next::attr(href)').extract_first()
        
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)