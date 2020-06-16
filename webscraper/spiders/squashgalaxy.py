import scrapy

class SqusahGalaxySpider(scrapy.Spider):
    name = "squashgalaxy"
    store_url = "https://www.squashgalaxy.com"
    start_urls = [
        #rackets
        'https://www.squashgalaxy.com/SG/category/SR_All.html',
        'https://www.squashgalaxy.com/SG/category/SS_All.html',
        'https://www.squashgalaxy.com/SG/category/SB_All.html',
        'https://www.squashgalaxy.com/SG/category/Squash_Balls.html',
        'https://www.squashgalaxy.com/SG/category/SE_All.html',
        'https://www.squashgalaxy.com/SG/category/SST_All.html',
        'https://www.squashgalaxy.com/SG/category/SG_All.html',
        ]

    def parse(self, response):
        for item in response.css('div#js-product-list div.category-product'):

            yield {
                'aff_url': response.urljoin(item.css('a::attr(href)').extract_first()),
                'aff_title': item.css('p.h6::text').extract_first(),
            }
