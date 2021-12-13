import scrapy

class RacquetGuys(scrapy.Spider):
    name = "racquetguys"
    start_urls = [
        'https://racquetguys.ca/collections/squash-racquets',
        'https://racquetguys.ca/collections/squash-racquets?page=2',
        'https://racquetguys.ca/collections/squash-racquets?page=3',
        'https://racquetguys.ca/collections/squash-racquets?page=4',
        'https://racquetguys.ca/collections/squash-shoes',
        'https://racquetguys.ca/collections/squash-shoes?page=2',
        'https://racquetguys.ca/collections/squash-shoes?page=3',
        'https://racquetguys.ca/collections/squash-shoes?page=4',
    ]

    def parse(self, response):
        for item in response.css('a.boost-pfs-filter-product-item-title'):
            yield {
                'aff_url': response.urljoin(item.css('a::attr(href)').extract_first()),
                'aff_title': item.css('a::text').extract_first().strip(),
            }

        next_page = response.urljoin(response.xpath('//div[@id="toolbar-bottom"]/ul/li/a[contains(.,"Next")]/@href').extract_first())
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)