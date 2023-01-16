import scrapy

class DLSportsSpider(scrapy.Spider):
    name = "decathlonde"
    start_urls = [
        'https://www.decathlon.de/browse/c0-alle-sportarten-a-z/c1-squash/c2-squashschlager/_/N-181u26b',
        'https://www.decathlon.de/browse/c0-alle-sportarten-a-z/c1-squash/c2-squashschuhe/_/N-1kl6fiv',
    ]

    def parse(self, response):
        for item in response.css('div.product-list div.dpb-holder'):

            yield {
                'aff_url': response.urljoin(item.css('a::attr(href)').extract_first()),
                'aff_title': item.css('h2::text').extract_first()
            }

        #next_page = response.css('div.pagination span.next a::attr(href)').extract_first()
        
        #if next_page is not None:
        #    next_page = response.urljoin(next_page)
        #    yield scrapy.Request(next_page, callback=self.parse)