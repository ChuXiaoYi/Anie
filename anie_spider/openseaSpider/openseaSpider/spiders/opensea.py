import scrapy


class OpenseaSpider(scrapy.Spider):
    name = "opensea"
    allowed_domains = ["opensea.io"]
    start_urls = ["http://opensea.io/"]

    def parse(self, response):
        print(response)
        dom_list = response.xpath('//*[@id="main"]/div/div[1]/div[3]/div/div[6]/div')
        for dom in dom_list:
            print(dom.xpath('./div/a/@href'))
