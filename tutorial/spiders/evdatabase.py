import scrapy
from datetime import datetime

class QuotesSpider(scrapy.Spider):
    name = "evbase"
    start_urls = ['https://ev-database.org',]

    def parse(self, response):
        
        for i in response.xpath('.//div[@class="data-wrapper"]'):
            yield {
                "Brand" : i.css('span::text').get(),
                "Model" : i.css('span.model::text').get(),
                "Seat" : i.xpath('.//*[@title="Number of seats"]/text()').get(),
                "Battery" : i.css('span.battery::text').get(),
                "Range" : i.css('span.erange_real::text').get(),
                "Topspeed": i.css('span.topspeed::text').get(),
                "Fastcharge": i.css('span.fastcharge_speed_print::text').get(),
                "Acceleration": i.css('span.acceleration::text').get(),
                "Tow_Capacity": i.xpath('.//*[@title="Towing capacity in kg"]/text()').get(),
                "Drive": i.xpath('//*[@id="evdb"]/main/div[2]/div[3]/div[2]/div/div[3]/span[4]/@title').get(),
                "Price_GE": i.css('span.country_de::text').get(),
                "Price_Nl": i.css('span.country_nl::text').get(),
                "Price_UK": i.css('span.country_uk::text').get(),
                "Market_Segment": i.xpath('.//*[@title="Market Segment"]/text()').get(),


            }
