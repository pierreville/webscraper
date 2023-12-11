import scrapy

class AdidasUKSpider(scrapy.Spider):
    name = "adidasuk"
    start_urls = [
        'https://www.adidas.co.uk/handball',
    ]

    def parse(self, response):
        for item in response.css('div.grid-item'):

            yield {
                'aff_url': response.urljoin(item.css('a::attr(href)').extract_first()),
                'aff_title': 'Adidas ' + item.css('p::text').extract_first(),
            }