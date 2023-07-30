import scrapy

class SquashGearSpider(scrapy.Spider):
    name = "squashgear"
    start_urls = [
        'https://www.squashgear.com/collections/dunlop-squash-rackets',
        'https://www.squashgear.com/collections/tecnifibre-squash-rackets',
        'https://www.squashgear.com/collections/prince-squash-rackets',
        'https://www.squashgear.com/collections/eye-squash-rackets',
        'https://www.squashgear.com/collections/wilson-squash-rackets',
        'https://www.squashgear.com/collections/harrow-squash-rackets',
        'https://www.squashgear.com/collections/head-squash-rackets',
        'https://www.squashgear.com/collections/black-knight-squash-rackets',
        'https://www.squashgear.com/collections/karakal-squash-rackets',
        'https://www.squashgear.com/collections/manta-squash-rackets',
        'https://www.squashgear.com/collections/unsquashable-squash-rackets',
        'https://www.squashgear.com/collections/asics-squash-shoes',
        'https://www.squashgear.com/collections/eye-squash-shoes',
        'https://www.squashgear.com/collections/prince-squash-shoes',
        'https://www.squashgear.com/collections/yonex-squash-shoes',
        'https://www.squashgear.com/collections/salming-squash-shoes',
        'https://www.squashgear.com/collections/adidas-squash-shoes',
        'https://www.squashgear.com/collections/harrow-squash-shoes',
        'https://www.squashgear.com/collections/wilson-squash-shoes',
        'https://www.squashgear.com/collections/hi-tec-squash-shoes',
        'https://www.squashgear.com/collections/junior-squash-shoes',
    ]

    def parse(self, response):
        for item in response.css('.product-index'):
            yield {
                'aff_url': response.urljoin(item.css('a::attr(href)').extract_first()),
                'aff_title': item.css('div.prod-title::text').extract_first(),
            }
