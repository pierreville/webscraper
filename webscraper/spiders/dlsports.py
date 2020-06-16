import scrapy

class HolabirdSpider(scrapy.Spider):
    name = "dlsports"
    start_urls = [
        'https://dlsports.eu/collections/squashschlager',
    ]

    def parse(self, response):
        for item in response.css('div.grid__item a.product-card'):

            name = item.css('div.product-card__name::text').extract_first()
            brand = item.css('div.product-card__brand::text').extract_first()

            yield {
                'aff_url': response.urljoin(item.css('a::attr(href)').extract_first()),
                'aff_title': brand + ' ' + name
            }

        next_page = response.css('div.pagination span.next a::attr(href)').extract_first()
        
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)