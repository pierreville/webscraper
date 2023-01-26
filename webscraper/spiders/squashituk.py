import scrapy

class SquashGearSpider(scrapy.Spider):
    name = "squashituk"
    start_urls = [
        'https://www.squashituk.co.uk/squash-rackets',
        'https://www.squashituk.co.uk/shoes',
    ]

    def parse(self, response):
        for item in response.css('div[role="group"]'):
            yield {
                'aff_url': response.urljoin(item.css('a::attr(href)').extract_first()),
                'aff_title': item.css('h3::text').extract_first(),
            }
