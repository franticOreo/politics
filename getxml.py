import scrapy


class QuotesSpider(scrapy.Spider):
    name = "politics"
    start_urls = [
        'https://www.aph.gov.au/Parliamentary_Business/Hansard',
    ]


    # get all the links for xml documents
    def parse(self, response):
        # loop over the amount of XML docs on page and get there URL's
        for link in response.xpath('//a[contains(@id, "main_0_content_1_lvHansard_hlXML")]/@href').getall():
            link = response.urljoin(link)
            yield scrapy.Request(link, callback=self.get_xml)

        back_page = response.xpath('//*[@id="main_0_content_1_hlPrevSittingWeek"]/@href').get()
        if back_page is not None:
            yield response.follow(back_page, callback=self.parse)


    def get_xml(self, response):
        with open('hansard-xml', 'a') as f:
            f.write(str(response.xpath('/hansard').getall()))
