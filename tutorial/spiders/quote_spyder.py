import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['https://www.dataforthai.com/business/objective',]

    def parse_page1(self, response):
        for i in response.css('tr.click-able-row a::attr(href)').getall():
            return scrapy.Request("https://www.dataforthai.com"+i,callback=self.parse_page2)

    def parse_page2(self, response):
        for quote in response.xpath('//*[@id="datatable"]/tbody/tr'):
            yield {
                'entrepreneur': quote.xpath('td[2]/text()').get(),
                'capital': quote.xpath('td[3]/text()').get(),
                'amphoe': quote.xpath('td[5]/text()').get(),
                'tambon': quote.xpath('td[6]/text()').get(),
            }
        self.logger.info("Visited %s", response.url)
        # def first_page(self, response):
        # href = response.css('tr.click-able-row a::attr(href)').getall()
        # for i in href:
        #     url = 'https://www.dataforthai.com'+i
        #     self.logger.info("Parsing match on url: " + url)
        #     yield response.Request(url=url, callback=self.parse)
