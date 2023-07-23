import scrapy

class AsicsSpider(scrapy.Spider):
    name = "asics"
    start_urls = [
        'https://www.asics.com/us/en-us/volleyball/c/aa40300000/?prefn1=productSubType&prefv1=Shoes&sz=96',
        'https://www.asics.com/us/en-us/pickleball/c/aa40901000/?prefn1=productSubType&prefv1=Shoes',
    ]

    def parse(self, response):
        for item in response.css('a.product-tile__link'):

            yield {
                'aff_url': response.urljoin(item.css('a::attr(href)').extract_first()),
                'aff_title': 'Asics ' + item.css('a::attr(title)').extract_first(),
            }