from tkinter import Y
from tkinter.messagebox import YES
import scrapy

from scrapy.http.request.form import FormRequest
from scrapy.http import FormRequest
import json

class CodeSpider(scrapy.Spider):
    name = 'code'
    start_urls = ['https://data.thaiauto.or.th/statistic/get-data/stat-register-light-duty-vehicle.php']

    def start_requests(self): 
        form_data = {
        "start":0,
        "length":100,
        "ref_year":2022,
        "month": "all",
        "type":"all",
        }
        request_body = json.dumps(form_data)
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'origin': 'data.thaiauto.or.th',}
        yield scrapy.Request('https://data.thaiauto.or.th/statistic/get-data/stat-register-light-duty-vehicle.php',
                            method="POST",
                            body=request_body,
                            headers=headers,callback=self.parse )

    def parse(self, response):
        yield json.loads(response.body)

