import scrapy

class HandballShopSpider(scrapy.Spider):
    name = "handballshop"
    start_urls = [
        'https://www.handballshop.com/handballshoes/_brand-adidas_brand-ASICS_brand-Salming?page=1&sort=name_s%20asc',
        'https://www.handballshop.com/handballshoes/_brand-adidas_brand-ASICS_brand-Salming?page=2&sort=name_s%20asc',
        'https://www.handballshop.com/handballshoes/_brand-adidas_brand-ASICS_brand-Salming?page=3&sort=name_s%20asc',
        'https://www.handballshop.com/handballshoes/_brand-adidas_brand-ASICS_brand-Salming?page=4&sort=name_s%20asc',
        'https://www.handballshop.com/handballshoes/_brand-adidas_brand-ASICS_brand-Salming?page=5&sort=name_s%20asc',
    ]

    def parse(self, response):

        # These notes are my best understanding, by trial and error, of how this is working

        for item in response.css('script[type="application/ld+json"]'): # Each item contains a chunk of HTML but for reasons unknown, I can't work with this in Python directly
            
            chunk = item.get() # If we get the first chunk into a variable we can work with it in Python?!
            
            name_start = chunk.find('name') + 7 # Get the starting point of the name 
            name_end = chunk.find('brand') - 3 # Get the ending point of the name
            name = chunk[name_start:name_end] # Put it together...

            url_start = chunk.find('url') + 6
            url_end = chunk.find('image') - 3
            url_raw = chunk[url_start:url_end]
            url_clean = url_raw.replace('\\','')

            yield {
                'aff_title': name,
                'aff_url': url_clean,
            }

        #next_page_check = response.css('span._disabled').extract_first()
        
        #if next_page_check is not None:
 #           yield scrapy.Request(next_page, callback=self.parse)