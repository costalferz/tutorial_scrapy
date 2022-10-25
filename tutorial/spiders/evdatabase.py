import scrapy
from datetime import datetime

class QuotesSpider(scrapy.Spider):
    name = "evbase"
    start_urls = ['https://ev-database.org',]

    def parse(self, response):
        
        for i in response.xpath('.//div[@class="data-wrapper"]'):
            yield {
                "brand" : i.css('span::text').get(),
                "model" : i.css('span.model::text').get(),
                "seat" : i.xpath('.//*[@title="Number of seats"]/text()').get(),
                "battery" : i.css('span.battery::text').get(),
                "range" : i.css('span.erange_real::text').get(),
                "topspeed": i.css('span.topspeed::text').get(),
                "acceleration": i.css('span.acceleration::text').get(),

            }
