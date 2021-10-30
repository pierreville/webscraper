import scrapy
import re

class SqusahGalaxySpider(scrapy.Spider):
    name = "squashgalaxy"
    store_url = "https://www.squashgalaxy.com"
    start_urls = [
        'https://www.squashgalaxy.com/all-squash-racquets.html',
        'https://www.squashgalaxy.com/all-squash-shoes.html',
        ]

    def parse(self, response):
        for item in response.css('section.x-product-list div.x-product-list__item'):

            rawtitle = item.css('a::attr(title)').extract_first()

            yield {
                'aff_url': response.urljoin(item.css('a::attr(href)').extract_first()),

                #this splits the title at the first instance of " (" and takes the part before
                'aff_title': rawtitle.split(" (")[0]
            }
