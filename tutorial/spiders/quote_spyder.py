import scrapy
from datetime import datetime

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['https://www.dataforthai.com/business/objective',]
    def parse(self, response):
        for i in response.css('tr.click-able-row a::attr(href)'):
            url = response.urljoin(i.extract())
            yield scrapy.Request(url, callback=self.parse_data)
            self.logger.info('Processing %s', response.url)

    def parse_data(self, response):
         for quote in response.xpath('//*[@id="datatable"]/tbody/tr'):
            yield {
            'entrepreneur': quote.xpath('td[2]/text()').get(),
            'capital': quote.xpath('td[3]/text()').get(),
            'amphoe': quote.xpath('td[5]/text()').get(),
            'tambon': quote.xpath('td[6]/text()').get(),
            'categories': quote.xpath('//*[@id="main"]/div[4]/div[1]/h1/text()').get().split(' ')[2],
            'code': response.url[-5:],
            'date': datetime.now().strftime("%Y-%m-%d-%T"),
         }

