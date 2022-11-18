import scrapy
from datetime import datetime

class QuotesSpider(scrapy.Spider):
    name = "ev4"
    start_urls = ['https://ev-database.org',]

    def parse(self, response):
        all_link = response.css('a.title::attr(href)')
        for link in all_link:
            print(link.get())
            yield response.follow(link, callback=self.parse_car)

    def parse_car(self, response):

        yield {
            "brand" : response.css('h1::text').get(),
            # "model" : response.css('span.model::text').get(),
            # "seat" : response.xpath('.//*[@title="Number of seats"]/text()').get(),
            # "battery" : response.css('span.battery::text').get(),
            # "range" : response.css('span.erange_real::text').get(),
            # "topspeed": response.css('span.topspeed::text').get(),
            # "acceleration": response.css('span.acceleration::text').get(),
        }