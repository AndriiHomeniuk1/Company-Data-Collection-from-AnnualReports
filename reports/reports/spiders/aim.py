import scrapy
from scrapy.http import Response


class AimSpider(scrapy.Spider):
    name = "aim"
    allowed_domains = ["annualreports.com"]
    start_urls = ["https://www.annualreports.com/Companies?exch=8"]


    def parse(self, response: Response, **kwargs):
        for company in response.css(".companyName"):
            yield {
                "name":  company.css(".companyName > a::text").get(),
                "link_name": f"https://www.annualreports.com{company.css('.companyName > a::attr(href)').get()}",
            }
