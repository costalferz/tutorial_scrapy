import scrapy
from datetime import datetime

class QuotesSpider(scrapy.Spider):
    name = "evbase"
    start_urls = ['https://ev-database.org',]
    def parse(self, response):
        for i in response.css('div.data-wrapper'):
            yield{
                'brand': i.css('h2::text').get(),
            }
            # yield scrapy.Request(url, callback=self.parse_data)

    # def parse_data(self, response):
    #      for quote in response.xpath('//*[@id="datatable"]/tbody/tr'):
    #         yield {
    #         'entrepreneur': quote.xpath('td[2]/text()').get(),
    #         'capital': quote.xpath('td[3]/text()').get(),
    #         'amphoe': quote.xpath('td[5]/text()').get(),
    #         'tambon': quote.xpath('td[6]/text()').get(),
    #         'categories': quote.xpath('//*[@id="main"]/div[4]/div[1]/h1/text()').get().split(' ')[2],
    #         'code': response.url[-5:],
    #         'date': datetime.now().strftime("%Y-%m-%d-%T"),
    #      }

