import scrapy

class HolabirdSpider(scrapy.Spider):
    name = "holabird"
    start_urls = [
        'https://www.holabirdsports.com/collections/squash-racquets',
        'https://www.holabirdsports.com/collections/mens-squash-shoes',
        'https://www.holabirdsports.com/collections/womens-squash-shoes',
        'https://www.holabirdsports.com/collections/squash-balls',
        'https://www.holabirdsports.com/collections/squash-replacement-grips',
        'https://www.holabirdsports.com/collections/squash-string',
        'https://www.holabirdsports.com/collections/squash-eyeguards',
        'https://www.holabirdsports.com/collections/junior-squash-racquets',
        'https://www.holabirdsports.com/collections/squash-grips',
        'https://www.holabirdsports.com/collections/squash-bags',

    ]

    def parse(self, response):
        for item in response.css('div.product-title a.title'):
            yield {
                'aff_url': response.urljoin(item.css('a::attr(href)').extract_first()),
                'aff_title': item.css('a::text').extract_first(),
            }

        next_page = response.css('ul.pagination li a[title*="layout.pagination.next_html"]::attr(href)').extract_first()
        
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)