import scrapy
import re

class RacquetScienceSpider(scrapy.Spider):
    name = "racquetscience"
    start_urls = [
        'https://racquet-science.com/collections/squash-racquets',
        'https://racquet-science.com/collections/squash-shoes',
    ]

    def parse(self, response):
        for item in response.css('div.productitem h2.productitem--title'):

            yield {
                'aff_url': response.urljoin(item.css('a::attr(href)').extract_first()),
                'aff_title': item.css('a::text').extract_first().strip(),
            }

        next_page = response.css('nav.pagination--container li.pagination--next a::attr(href)').extract_first()
        
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)