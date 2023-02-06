import scrapy

class squashmajik(scrapy.Spider):
    name = "squashmajik"
    start_urls = [
        'https://www.ebay.com.au/sch/i.html?_nkw=&_armrs=1&_ipg=&_from=&_ssn=squashmajik&_sop=10',
    ]

    def parse(self, response):
        for item in response.css('div.srp-river-results div.s-item__wrapper'):

            yield {
                'aff_url': item.css('div.s-item__info a::attr(href)').get(),
                'aff_title': item.css('div.s-item__info div.s-item__title span::text').get(),
                'aff_id': item.css('div.s-item__image-section a::attr(data-id)').get()
            }

        #next_page = response.css('div.pagination span.next a::attr(href)').get()
        
        #if next_page is not None:
        #    next_page = response.urljoin(next_page)
        #    yield scrapy.Request(next_page, callback=self.parse)