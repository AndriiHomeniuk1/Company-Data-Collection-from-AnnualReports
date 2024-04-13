import scrapy
from scrapy.http import Response


class PdfSpider(scrapy.Spider):
    name = "pdf"
    allowed_domains = ["annualreports.com"]
    start_urls = ["https://annualreports.com"]
    f2000 = None

    def parse(self, response: Response, **kwargs):
        pass
