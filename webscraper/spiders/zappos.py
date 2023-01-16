import scrapy

class ZapposSpider(scrapy.Spider):
    name = "zappos"
    store_url = "https://www.zappos.com"
    start_urls = [
        'https://www.zappos.com/volleyball-shoes'
    ]

    def parse(self, response):
        for item in response.css('div#searchPage article'):
            brand_name = item.css('dd[itemprop="brand"] span::text').extract_first(),
            product_name = item.css('dd[itemprop="name"]::text').extract_first(),
            url = response.urljoin(item.css('a::attr(href)').extract_first()),

            whole_name = brand_name[0] + ' ' + product_name[0]
            
            yield {
                'aff_title': whole_name,
                'aff_url': url,
            }
