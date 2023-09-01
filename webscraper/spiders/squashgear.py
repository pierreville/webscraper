import scrapy

class SquashGearSpider(scrapy.Spider):
    name = "squashgear"
    start_urls = [
        'https://www.squashgear.com/collections/all',
    ]

    def parse(self, response):
        for item in response.css('.product-index'):
            yield {
                'aff_url': response.urljoin(item.css('a::attr(href)').extract_first()),
                'aff_title': item.css('div.prod-title::text').extract_first(),
            }

        next_page = response.urljoin(response.css('div.pagination a[title="Next page"]::attr(href)').extract_first())
        
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)