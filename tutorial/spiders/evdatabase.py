import scrapy
from datetime import datetime
class Item(scrapy.Item):
    Brand = scrapy.Field()
    Model = scrapy.Field()
    Seat = scrapy.Field()
    Battery = scrapy.Field()
    Range = scrapy.Field()
    Topspeed = scrapy.Field()
    Fastcharge= scrapy.Field()
    Acceleration = scrapy.Field()
    Tow_Capacity = scrapy.Field()
    Drive = scrapy.Field()
    Price_GE = scrapy.Field()
    Price_Nl = scrapy.Field()
    Price_UK = scrapy.Field()
    Market_Segment = scrapy.Field()
class QuotesSpider(scrapy.Spider):
    name = "evbase"
    start_urls = ['https://ev-database.org',]

    def parse(self, response):
        
        for i in response.xpath('.//div[@class="data-wrapper"]'):
            item = Item()
            item['Brand'] = i.css('span::text').get()
            item['Model'] = i.css('span.model::text').get()
            item['Seat'] =  i.xpath('.//*[@title="Number of seats"]/text()').get()
            item['Battery'] = i.css('span.battery::text').get()
            item['Range'] = i.css('span.erange_real::text').get()
            item['Topspeed'] = i.css('span.topspeed::text').get()
            item['Fastcharge'] = i.css('span.fastcharge_speed_print::text').get()
            item['Acceleration'] = i.css('span.acceleration::text').get()
            item['Tow_Capacity'] = i.xpath('.//*[@title="Towing capacity in kg"]/text()').get()
            item['Drive'] = i.xpath('.//*[@class="icons"]/span[4]/@title').get()
            if item['Drive'] is None:
                item['Drive'] = i.xpath('.//*[@class="icons"]/span[2]/@title').get()
            item['Market_Segment'] = i.xpath('.//*[@title="Market Segment"]/text()').get()
            item['Price_GE'] = i.css('span.country_de::text').get()
            item['Price_Nl'] = i.css('span.country_nl::text').get()
            item['Price_UK'] = i.css('span.country_uk::text').get()
            yield item



            # yield {
            #     "Brand" : i.css('span::text').get(),
            #     "Model" : i.css('span.model::text').get(),
            #     "Seat" : i.xpath('.//*[@title="Number of seats"]/text()').get(),
            #     "Battery" : i.css('span.battery::text').get(),
            #     "Range" : i.css('span.erange_real::text').get(),
            #     "Topspeed": i.css('span.topspeed::text').get(),
            #     "Fastcharge": i.css('span.fastcharge_speed_print::text').get(),
            #     "Acceleration": i.css('span.acceleration::text').get(),
            #     "Tow_Capacity": i.xpath('.//*[@title="Towing capacity in kg"]/text()').get(),
            #     "Drive": i.xpath('.//*[@class="icons"]/span[4]/@title').get(),
            #     "Drive": i.xpath('.//*[@class="icons"]/span[2]/@title').get(),
            #     "Price_GE": i.css('span.country_de::text').get(),
            #     "Price_Nl": i.css('span.country_nl::text').get(),
            #     "Price_UK": i.css('span.country_uk::text').get(),
            #     "Market_Segment": i.xpath('.//*[@title="Market Segment"]/text()').get(),


            # }
