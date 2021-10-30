# -*- coding: utf-8 -*-
import scrapy

class PDHsportsspider(scrapy.Spider):
    name = "pdhsports"
    start_urls = (
        'https://www.pdhsports.com/c/q/squash/squash-rackets',
        'https://www.pdhsports.com/c/q/squash/squash-shoes',
        'https://www.pdhsports.com/c/q/squash/squash-bags',
        'https://www.pdhsports.com/c/q/squash/squash-balls',
        'https://www.pdhsports.com/c/q/squash/squash-grips',
        'https://www.pdhsports.com/c/q/squash/squash-strings',
        'https://www.pdhsports.com/c/q/squash/squash-goggles-and-protective-eyewear',
        'https://www.pdhsports.com/c/q/squash/junior-squash-rackets',
        'https://www.pdhsports.com/c/q/squash/junior-squash-shoes',
    )
    seen_product_url = set()

    def parse(self, response):
        for item in response.css("span.prod-name"):
            yield {
                'aff_url': response.urljoin(item.css('a::attr(href)').extract_first()),
                'aff_title': item.css('a::text').extract_first(),
            }