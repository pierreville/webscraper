import scrapy

class ControltheTSpider(scrapy.Spider):
    name = "controlthet"
    start_urls = [
        'https://controlthet.com/collections/latest-arrivals-squash',
        'https://controlthet.com/collections/latest-arrivals-indoor-court-shoes',
    ]

    def parse(self, response):
        for item in response.css('div.prod-image'):
            yield {
                'aff_url': response.urljoin(item.css('a::attr(href)').extract_first()),
                'aff_title': item.css('a::attr(title)').extract_first(),
            }

        next_page = response.urljoin(response.css('div.paginext a::attr(href)').extract_first())
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)